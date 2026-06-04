#!/usr/bin/env python3
"""
Venture Factory agent runner.

Usage:
  run_agent.py --agent <slug> [--input <path>] [--dry-run]

Loads factory/agents/<slug>/AGENT.md as the system prompt, calls the
Anthropic API (model per config/agent_models.yaml), and processes the
output. Four agents have structured output handlers (market_radar,
opportunity_scoring, pain_validation, daily_summary); every other agent
uses the generic action/write-block protocol from Phase 0.

--dry-run is opt-in; default behavior is a real Anthropic API call.
"""
import argparse
import glob as glob_module
import json
import os
import re
import sys
import traceback
from datetime import datetime, timedelta, timezone
from pathlib import Path

import yaml
from dotenv import load_dotenv

REPO_ROOT = Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(REPO_ROOT / "scripts"))
sys.path.insert(0, str(REPO_ROOT))  # so `factory.sources` is importable

load_dotenv(REPO_ROOT / ".env")

# Agents whose I/O the runner handles directly (structured), bypassing the
# generic action/write-block protocol.
STRUCTURED_AGENTS = {"market_radar", "opportunity_scoring", "pain_validation", "daily_summary"}

# Bound market_radar input size to keep per-run cost predictable. Real
# source-level prefiltering arrives in Phase 1.5.
MAX_PREFETCH_ITEMS = 15
PREFETCH_BODY_TRUNC = 1500

# Per-million-token prices (USD). // update from anthropic pricing page
MODEL_PRICES = {
    "claude-sonnet-4-6": (3.0, 15.0),
    "claude-opus-4-6": (15.0, 75.0),
    "claude-opus-4-5": (15.0, 75.0),
    "claude-haiku-4-5-20251001": (1.0, 5.0),
}
_DEFAULT_PRICE = (3.0, 15.0)

_PROTOCOL = """

---
## Machine Output Protocol (enforced by the runner)

**Write a file** — emit a fenced block whose fence tag is `write:<relative/path>`:
```write:opportunities/01EXAMPLE.json
{"id": "01EXAMPLE", ...}
```

**Request an external action** (email, deploy, payment, etc.) — emit:
```action
{
  "action_type": "send_outreach_email",
  "summary": "Short human-readable description",
  "payload": {},
  "cost_estimate_usd": 0.0,
  "risk": "low"
}
```
Action blocks are queued in approval_queue/ and NOT executed immediately.
"""


# ---------------------------------------------------------------------------
# Frontmatter / config
# ---------------------------------------------------------------------------

def parse_frontmatter(text: str) -> tuple[dict, str]:
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    fm_text = text[3:end].strip()
    body = text[end + 4:].lstrip()
    try:
        fm = yaml.safe_load(fm_text) or {}
    except yaml.YAMLError:
        fm = {}
    return fm, body


def load_policy() -> dict:
    p = REPO_ROOT / "config" / "approval_policy.yaml"
    if not p.exists():
        print("FATAL: config/approval_policy.yaml missing — failing closed.", file=sys.stderr)
        sys.exit(1)
    try:
        data = yaml.safe_load(p.read_text())
        if not isinstance(data, dict):
            raise ValueError("expected a YAML mapping")
        return data
    except Exception as exc:
        print(f"FATAL: config/approval_policy.yaml unparseable ({exc}) — failing closed.", file=sys.stderr)
        sys.exit(1)


def _load_yaml(rel: str) -> dict:
    p = REPO_ROOT / rel
    if not p.exists():
        return {}
    try:
        return yaml.safe_load(p.read_text()) or {}
    except yaml.YAMLError:
        return {}


def model_for(agent: str) -> tuple[str, int]:
    """Resolve (model, max_tokens) from config/agent_models.yaml."""
    cfg = _load_yaml("config/agent_models.yaml")
    defaults = cfg.get("defaults", {}) if isinstance(cfg, dict) else {}
    default_model = defaults.get("model", "claude-sonnet-4-6")
    default_max = int(defaults.get("max_tokens", 2048))
    if not cfg:
        print("WARN: config/agent_models.yaml missing/unparseable — using built-in defaults.",
              file=sys.stderr)
        return default_model, default_max
    entry = (cfg.get("agents") or {}).get(agent, {})
    return entry.get("model", default_model), int(entry.get("max_tokens", default_max))


# ---------------------------------------------------------------------------
# Small utilities
# ---------------------------------------------------------------------------

def _ulid() -> str:
    from ulid import ULID
    return str(ULID())


_ULID_RE = re.compile(r"^[0-9A-HJKMNP-TV-Z]{26}$")


def _idt_now() -> datetime:
    return datetime.now(timezone(timedelta(hours=3)))


def _idt_date() -> str:
    return _idt_now().strftime("%Y-%m-%d")


def validate_repo_path(p: Path) -> bool:
    try:
        p.resolve().relative_to(REPO_ROOT)
        return True
    except ValueError:
        return False


def _parse_json_payload(text: str):
    """Extract a JSON value from model output: prefer a ```json fence, else the
    first balanced [..]/{..}. Returns the parsed object or None."""
    candidates: list[str] = []
    m = re.search(r"```json\s*\n(.*?)\n```", text, re.DOTALL)
    if m:
        candidates.append(m.group(1))
    candidates.append(text)
    for c in candidates:
        c = c.strip()
        try:
            return json.loads(c)
        except json.JSONDecodeError:
            pass
        for i, ch in enumerate(c):
            if ch in "[{":
                try:
                    obj, _ = json.JSONDecoder().raw_decode(c[i:])
                    return obj
                except json.JSONDecodeError:
                    continue
    return None


def _opportunity_schema() -> dict:
    return json.loads((REPO_ROOT / "templates" / "opportunity.schema.json").read_text())


def _existing_opportunity_ids() -> list[str]:
    ids = []
    opp_dir = REPO_ROOT / "opportunities"
    for f in sorted(opp_dir.glob("*.opportunity.json")):
        try:
            ids.append(json.loads(f.read_text()).get("id"))
        except Exception:
            continue
    return [i for i in ids if i]


def emit_log(entry: dict, agent: str) -> None:
    log_dir = REPO_ROOT / "logs" / "runs" / _idt_date()
    log_dir.mkdir(parents=True, exist_ok=True)
    with open(log_dir / f"{agent}.jsonl", "a", encoding="utf-8") as fh:
        fh.write(json.dumps(entry) + "\n")


def write_approval_request(action: dict, agent: str) -> str:
    req_id = _ulid()
    now_ts = _idt_now().isoformat()
    request = {
        "ulid": req_id,
        "action_type": action.get("action_type", "unknown"),
        "summary": action.get("summary", f"{agent}: action request"),
        "agent": agent,
        "payload": action.get("payload", {}),
        "cost_estimate_usd": action.get("cost_estimate_usd", 0.0),
        "risk": action.get("risk", "medium"),
        "qa_result_ref": action.get("qa_result_ref"),
        "created_at": now_ts,
        "expires_at": action.get("expires_at", now_ts),
    }
    qdir = REPO_ROOT / "approval_queue"
    qdir.mkdir(parents=True, exist_ok=True)
    (qdir / f"{req_id}.json").write_text(json.dumps(request, indent=2), encoding="utf-8")
    return req_id


# ---------------------------------------------------------------------------
# Source prefetch (market_radar)
# ---------------------------------------------------------------------------

def _load_sources() -> list[dict]:
    """Source configs for market_radar. Honors MARKET_RADAR_SOURCES override
    (used by the smoke test to constrain to a single source)."""
    rel = os.environ.get("MARKET_RADAR_SOURCES", "config/market_radar_sources.yaml")
    cfg = _load_yaml(rel)
    return cfg.get("sources", []) if isinstance(cfg, dict) else []


def _prefetch_items_from_fixture(fixture_path: Path) -> list[dict]:
    try:
        data = json.loads(fixture_path.read_text(encoding="utf-8"))
    except Exception:
        return []
    items = []
    for s in data.get("sources", []):
        items.append({
            "url": s.get("url", ""),
            "title": s.get("title", ""),
            "author": s.get("author", ""),
            "captured_at": s.get("captured_at", ""),
            "body_text": s.get("content") or s.get("body_text") or s.get("snippet") or "",
        })
    return items


def _prefetch_market_radar(fixture_path: Path | None) -> list[dict]:
    if fixture_path and fixture_path.exists():
        items = _prefetch_items_from_fixture(fixture_path)
    else:
        from factory import sources as _sources
        items = []
        for src in _load_sources():
            if not src.get("enabled", False):
                continue
            try:
                items.extend(_sources.fetch(src))
            except NotImplementedError as exc:
                print(f"WARN: source {src.get('id')} not implemented: {exc}", file=sys.stderr)
            except Exception as exc:
                print(f"WARN: source {src.get('id')} fetch failed: {exc}", file=sys.stderr)
    # Bound size for predictable cost.
    items = items[:MAX_PREFETCH_ITEMS]
    for it in items:
        if isinstance(it.get("body_text"), str):
            it["body_text"] = it["body_text"][:PREFETCH_BODY_TRUNC]
    return items


# ---------------------------------------------------------------------------
# Runtime contracts (authoritative output spec injected per structured agent)
# ---------------------------------------------------------------------------

def _runtime_contract(agent: str) -> str:
    if agent == "market_radar":
        return """

---
## RUNTIME CONTRACT (authoritative — overrides any conflicting instruction above)

You are given `pre_fetched_items` (already fetched; do NOT fetch anything). Cluster
them into distinct candidate opportunities and emit a SINGLE JSON array inside one
```json fenced block. Each element MUST contain EXACTLY these fields and nothing else:

- "source": object with "type" (one of: reddit, hn, twitter, linkedin, forum,
  review_site, job_board, podcast, newsletter, support_ticket, operator_intuition,
  other), "url" (a real URL from the items), "snippet" (<=2000 chars, no personal names).
- "problem_statement": 30-500 chars, plain language.
- "target_segment": 3-200 chars.
- "geo": a two-letter UPPERCASE ISO country code (e.g. US, IL) or "GLOBAL".
- "signal_strength": integer 1-5.
- "keywords": array of 1-30 lowercase kebab-case tags (^[a-z0-9][a-z0-9-]{0,29}$).
- "notes": short free text (may be "").

Do NOT include "id", "discovered_at", or "status" — the runner assigns those.
Emit `[]` if there is no real, concrete, repeated pain. Output ONLY the JSON array."""
    if agent == "opportunity_scoring":
        return """

---
## RUNTIME CONTRACT (authoritative — overrides any conflicting instruction above)

You are given `opportunities` (array) and `scoring_model_yaml`. Score EVERY opportunity.
Emit a SINGLE JSON array inside one ```json fenced block. Each element MUST contain:

- "opportunity_id": the opportunity's "id".
- "per_dimension": object mapping each dimension name in scoring_model_yaml to an integer 0-10.
- "weighted_total": number (sum of dimension*weight, 0-10 scale), 1 decimal.
- "penalties_applied": array of {"name","deduction","reason"} (may be []).
- "total": number = weighted_total minus sum of deductions (0-10 scale), 1 decimal.
- "recommended_stage": one of "drop","validate","build","scale".
- "rationale": 1-3 sentences.
- "notes": string (may be "").

Output ONLY the JSON array."""
    if agent == "pain_validation":
        return """

---
## RUNTIME CONTRACT (authoritative — overrides any conflicting instruction above)

You are given `candidates` (array of {opportunity, scoring}) and `market_evidence_template`.
For EACH candidate emit one object. Emit a SINGLE JSON array inside one ```json fenced block.
Each element MUST contain:

- "opportunity_id": the opportunity's "id".
- "status": "validated" or "rejected".
- "severity": "mild" | "moderate" | "burning".
- "frequency": "rare" | "monthly" | "weekly" | "daily".
- "rationale": 1-3 sentences referencing the evidence available.
- "sources": array of source URLs (from the opportunity's source data).
- "market_evidence_md": a Markdown string following the template's section structure.

Output ONLY the JSON array."""
    if agent == "daily_summary":
        return """

---
## RUNTIME CONTRACT (authoritative — overrides any conflicting instruction above)

You are given today's aggregated factory state and `daily_summary_template`. Produce the
report as Markdown ONLY (no JSON, no fences), following the template's headings exactly.
The runner writes your entire output to reports/daily/<date>.md. Tag any illustrative
values that leak from the template as "EXAMPLE ONLY"; real numbers from today are untagged."""
    return ""


# ---------------------------------------------------------------------------
# Per-agent input construction
# ---------------------------------------------------------------------------

def _section(title: str, body: str) -> str:
    return f"### {title}\n{body}"


def build_inputs(agent: str, frontmatter: dict, fixture_path: Path | None) -> str:
    if agent == "market_radar":
        items = _prefetch_market_radar(fixture_path)
        parts = [
            _section("date_iso_idt", _idt_date()),
            _section("pre_fetched_items", f"```json\n{json.dumps(items, indent=2)}\n```"),
            _section("opportunity_schema",
                     f"```json\n{json.dumps(_opportunity_schema(), indent=2)}\n```"),
            _section("existing_opportunity_ids",
                     f"```json\n{json.dumps(_existing_opportunity_ids())}\n```"),
        ]
        return "\n\n".join(parts)

    if agent == "opportunity_scoring":
        opp_dir = REPO_ROOT / "opportunities"
        unscored = []
        for f in sorted(opp_dir.glob("*.opportunity.json")):
            base = f.name[: -len(".opportunity.json")]
            if (opp_dir / f"{base}.scoring.json").exists():
                continue
            try:
                unscored.append(json.loads(f.read_text()))
            except Exception:
                continue
        unscored = unscored[:25]
        parts = [
            _section("date_iso_idt", _idt_date()),
            _section("opportunities", f"```json\n{json.dumps(unscored, indent=2)}\n```"),
            _section("scoring_model_yaml",
                     f"```yaml\n{(REPO_ROOT / 'config' / 'scoring_model.yaml').read_text()}\n```"),
        ]
        return "\n\n".join(parts)

    if agent == "pain_validation":
        opp_dir = REPO_ROOT / "opportunities"
        sm = _load_yaml("config/scoring_model.yaml")
        threshold = (sm.get("thresholds", {}) or {}).get("min_total_to_validate", 5.5)
        candidates = []
        for sf in sorted(opp_dir.glob("*.scoring.json")):
            base = sf.name[: -len(".scoring.json")]
            if (opp_dir / f"{base}.verdict.json").exists():
                continue
            try:
                scoring = json.loads(sf.read_text())
            except Exception:
                continue
            if float(scoring.get("total", 0)) < float(threshold):
                continue
            opp_file = opp_dir / f"{base}.opportunity.json"
            if not opp_file.exists():
                continue
            try:
                opp = json.loads(opp_file.read_text())
            except Exception:
                continue
            candidates.append({"opportunity": opp, "scoring": scoring})
        candidates = candidates[:10]
        tmpl_path = REPO_ROOT / "templates" / "service_template" / "market_evidence.md"
        tmpl = tmpl_path.read_text() if tmpl_path.exists() else ""
        parts = [
            _section("date_iso_idt", _idt_date()),
            _section("candidates", f"```json\n{json.dumps(candidates, indent=2)}\n```"),
            _section("market_evidence_template", f"```markdown\n{tmpl}\n```"),
        ]
        return "\n\n".join(parts)

    if agent == "daily_summary":
        return _build_daily_summary_inputs()

    # Generic: inject declared inputs / fixture (Phase-0 behavior).
    return _build_generic_inputs(frontmatter, fixture_path)


def _build_daily_summary_inputs() -> str:
    today = _idt_date()
    log_dir = REPO_ROOT / "logs" / "runs" / today
    agent_activity: dict[str, dict] = {}
    if log_dir.exists():
        for lf in sorted(log_dir.glob("*.jsonl")):
            for line in lf.read_text(encoding="utf-8").splitlines():
                if not line.strip():
                    continue
                try:
                    e = json.loads(line)
                except json.JSONDecodeError:
                    continue
                a = agent_activity.setdefault(
                    e.get("agent", lf.stem),
                    {"runs": 0, "errors": 0, "last_status": "", "last_finished": ""},
                )
                a["runs"] += 1
                a["errors"] += len(e.get("errors", []) or [])
                a["last_status"] = e.get("status", "")
                a["last_finished"] = e.get("finished_at", "")

    opp_dir = REPO_ROOT / "opportunities"
    opp_counts: dict[str, int] = {}
    for f in opp_dir.glob("*.opportunity.json"):
        try:
            st = json.loads(f.read_text()).get("status", "candidate")
        except Exception:
            st = "unparseable"
        opp_counts[st] = opp_counts.get(st, 0) + 1
    scoring_count = len(list(opp_dir.glob("*.scoring.json")))
    verdict_count = len(list(opp_dir.glob("*.verdict.json")))

    now = _idt_now()
    approvals = []
    qdir = REPO_ROOT / "approval_queue"
    if qdir.exists():
        for qf in sorted(qdir.glob("*.json")):
            if qf.name.endswith((".approved.json", ".rejected.json")):
                continue
            try:
                obj = json.loads(qf.read_text())
            except Exception:
                continue
            created = obj.get("created_at", "")
            age_h = None
            try:
                age_h = round((now - datetime.fromisoformat(created)).total_seconds() / 3600, 1)
            except Exception:
                pass
            approvals.append({
                "ulid": obj.get("ulid"), "action_type": obj.get("action_type"),
                "summary": obj.get("summary", "")[:80], "age_hours": age_h,
                "expires_at": obj.get("expires_at"),
            })

    services = []
    svc_dir = REPO_ROOT / "services"
    if svc_dir.exists():
        for status_md in svc_dir.glob("*/status.md"):
            services.append({"slug": status_md.parent.name,
                             "status_excerpt": status_md.read_text()[:400]})

    tmpl_path = REPO_ROOT / "templates" / "daily_summary.md"
    tmpl = tmpl_path.read_text() if tmpl_path.exists() else ""

    aggregate = {
        "agent_activity": agent_activity,
        "opportunity_counts_by_status": opp_counts,
        "scoring_files": scoring_count,
        "verdict_files": verdict_count,
        "approval_queue": approvals,
        "services": services,
    }
    return "\n\n".join([
        _section("date_iso_idt", today),
        _section("aggregated_state", f"```json\n{json.dumps(aggregate, indent=2)}\n```"),
        _section("daily_summary_template", f"```markdown\n{tmpl}\n```"),
    ])


def _build_generic_inputs(frontmatter: dict, fixture_path: Path | None) -> str:
    parts: list[str] = []
    if fixture_path and fixture_path.exists():
        content = fixture_path.read_text(encoding="utf-8")
        parts.append(f"**Input file: {fixture_path.name}**\n```json\n{content}\n```")
    else:
        for pattern in frontmatter.get("inputs", []):
            for match in glob_module.glob(str(REPO_ROOT / pattern)):
                mp = Path(match)
                if mp.is_file():
                    rel = mp.relative_to(REPO_ROOT)
                    body = mp.read_text(encoding="utf-8")[:4000]
                    parts.append(f"**Input: {rel}**\n```\n{body}\n```")
    if not parts:
        parts.append("No input files found. Proceed based on your agent instructions.")
    return "\n\n".join(parts)


# ---------------------------------------------------------------------------
# Dry-run synthetic output (still supported for offline runs)
# ---------------------------------------------------------------------------

def _dry_run_output(agent: str, fixture_path: Path | None) -> str:
    if agent == "market_radar":
        items = _prefetch_market_radar(fixture_path)
        first = items[0] if items else {"url": "https://example.com/dry-run", "title": "",
                                        "body_text": "Dry-run signal."}
        opp = {
            "source": {"type": "hn", "url": first.get("url", "https://example.com/dry-run"),
                       "snippet": (first.get("body_text") or "Dry-run signal.")[:2000]},
            "problem_statement": ("Freelancers spend hours each month reconciling invoices "
                                  "with bank transactions by hand, paying accountants for cleanup."),
            "target_segment": "Freelancers and small businesses with 20-200 monthly transactions",
            "geo": "GLOBAL",
            "signal_strength": 3,
            "keywords": ["invoicing", "reconciliation", "bookkeeping"],
            "notes": "Dry-run synthetic opportunity.",
        }
        return f"```json\n{json.dumps([opp])}\n```"

    if agent == "opportunity_scoring":
        opp_dir = REPO_ROOT / "opportunities"
        out = []
        for f in sorted(opp_dir.glob("*.opportunity.json")):
            base = f.name[: -len(".opportunity.json")]
            if (opp_dir / f"{base}.scoring.json").exists():
                continue
            try:
                oid = json.loads(f.read_text()).get("id")
            except Exception:
                continue
            out.append({"opportunity_id": oid,
                        "per_dimension": {"pain_severity": 6}, "weighted_total": 6.0,
                        "penalties_applied": [], "total": 6.0,
                        "recommended_stage": "validate",
                        "rationale": "Dry-run synthetic score.", "notes": ""})
        return f"```json\n{json.dumps(out)}\n```"

    if agent == "daily_summary":
        return f"# Daily Summary — {_idt_date()} (IDT)\n\n## State of the Factory\nDry-run synthetic report.\n"

    return f"[dry-run] No synthetic output defined for agent '{agent}'."


# ---------------------------------------------------------------------------
# Structured output processors -> return list of written repo-relative paths
# ---------------------------------------------------------------------------

def _process_market_radar(text: str, errors: list[dict]) -> list[str]:
    payload = _parse_json_payload(text)
    if isinstance(payload, dict):  # e.g. shabbat_readonly status object
        return []
    if not isinstance(payload, list):
        errors.append({"code": "BAD_OUTPUT", "message": "market_radar output was not a JSON array"})
        return []

    import jsonschema
    schema = _opportunity_schema()
    opp_dir = REPO_ROOT / "opportunities"
    opp_dir.mkdir(parents=True, exist_ok=True)
    seen_path = opp_dir / "_seen.jsonl"
    written = []
    for item in payload:
        if not isinstance(item, dict):
            continue
        oid = item.get("id") if _ULID_RE.match(str(item.get("id", ""))) else _ulid()
        opp = {
            "id": oid,
            "discovered_at": _idt_now().isoformat(timespec="seconds"),
            "source": item.get("source"),
            "problem_statement": item.get("problem_statement"),
            "target_segment": item.get("target_segment"),
            "geo": item.get("geo"),
            "signal_strength": item.get("signal_strength"),
            "keywords": item.get("keywords"),
            "notes": item.get("notes", ""),
            "status": "candidate",
        }
        opp = {k: v for k, v in opp.items() if v is not None}
        try:
            jsonschema.validate(instance=opp, schema=schema)
        except jsonschema.ValidationError as exc:
            errors.append({"code": "SCHEMA_INVALID", "message": exc.message})
            continue
        rel = f"opportunities/{oid}.opportunity.json"
        (REPO_ROOT / rel).write_text(json.dumps(opp, indent=2), encoding="utf-8")
        written.append(rel)
        url = (opp.get("source") or {}).get("url", "")
        if url:
            with open(seen_path, "a", encoding="utf-8") as fh:
                fh.write(json.dumps({"id": oid, "url": url}) + "\n")
    return written


def _process_opportunity_scoring(text: str, model: str, errors: list[dict]) -> list[str]:
    payload = _parse_json_payload(text)
    if isinstance(payload, dict):
        payload = [payload]
    if not isinstance(payload, list):
        errors.append({"code": "BAD_OUTPUT", "message": "opportunity_scoring output was not a JSON array"})
        return []
    opp_dir = REPO_ROOT / "opportunities"
    written = []
    for s in payload:
        if not isinstance(s, dict):
            continue
        oid = s.get("opportunity_id")
        if not oid:
            continue
        s.setdefault("scored_at", _idt_now().isoformat(timespec="seconds"))
        s.setdefault("model_version", model)
        rel = f"opportunities/{oid}.scoring.json"
        (REPO_ROOT / rel).write_text(json.dumps(s, indent=2), encoding="utf-8")
        written.append(rel)
    return written


def _process_pain_validation(text: str, errors: list[dict]) -> list[str]:
    payload = _parse_json_payload(text)
    if isinstance(payload, dict):
        payload = [payload]
    if not isinstance(payload, list):
        errors.append({"code": "BAD_OUTPUT", "message": "pain_validation output was not a JSON array"})
        return []
    opp_dir = REPO_ROOT / "opportunities"
    written = []
    for v in payload:
        if not isinstance(v, dict):
            continue
        oid = v.get("opportunity_id")
        if not oid:
            continue
        evidence_md = v.pop("market_evidence_md", "")
        v.setdefault("evaluated_at", _idt_now().isoformat(timespec="seconds"))
        verdict_rel = f"opportunities/{oid}.verdict.json"
        (REPO_ROOT / verdict_rel).write_text(json.dumps(v, indent=2), encoding="utf-8")
        written.append(verdict_rel)
        if evidence_md:
            ev_rel = f"opportunities/{oid}.market_evidence.md"
            (REPO_ROOT / ev_rel).write_text(evidence_md, encoding="utf-8")
            written.append(ev_rel)
    return written


def _process_daily_summary(text: str, errors: list[dict]) -> list[str]:
    m = re.search(r"```(?:markdown)?\s*\n(.*?)\n```", text, re.DOTALL)
    md = m.group(1) if m else text
    md = md.strip() + "\n"
    out_dir = REPO_ROOT / "reports" / "daily"
    out_dir.mkdir(parents=True, exist_ok=True)
    rel = f"reports/daily/{_idt_date()}.md"
    target = REPO_ROOT / rel
    if target.exists():
        rel = f"reports/daily/{_idt_date()}_rerun_{_idt_now().strftime('%H%M')}.md"
        target = REPO_ROOT / rel
    target.write_text(md, encoding="utf-8")
    return [rel]


# ---------------------------------------------------------------------------
# Spend
# ---------------------------------------------------------------------------

def _check_spend(policy: dict, conn) -> bool:
    cap = policy.get("caps", {}).get("per_day_external_api_usd", 25.0)
    row = conn.execute(
        "SELECT COALESCE(SUM(cost_usd), 0.0) FROM spend_ledger WHERE date=?",
        (_idt_date(),),
    ).fetchone()
    return float(row[0]) < cap


def _record_spend(agent: str, model: str, tin: int, tout: int, cost: float, run_id: str, conn) -> None:
    conn.execute(
        "INSERT INTO spend_ledger (id, agent, date, cost_usd, run_id, created_at, model, tokens_in, tokens_out) "
        "VALUES (?,?,?,?,?,?,?,?,?)",
        (_ulid(), agent, _idt_date(), cost, run_id, datetime.now(timezone.utc).isoformat(),
         model, tin, tout),
    )
    conn.commit()


def _cost_usd(model: str, tin: int, tout: int) -> float:
    pin, pout = MODEL_PRICES.get(model, _DEFAULT_PRICE)
    return (tin * pin + tout * pout) / 1_000_000


# ---------------------------------------------------------------------------
# Finalize
# ---------------------------------------------------------------------------

def _finalize(run_id, agent, started_at, status, tokens_in, tokens_out, cost_usd,
              outputs, approval_requests, errors, conn) -> None:
    ended_at = datetime.now(timezone.utc)
    duration_ms = int((ended_at - started_at).total_seconds() * 1000)
    conn.execute(
        """UPDATE runs SET ended_at=?, status=?, tokens_in=?, tokens_out=?,
               cost_usd_estimate=?, outputs=?, approval_requests=?, errors=? WHERE id=?""",
        (ended_at.isoformat(), status, tokens_in, tokens_out, cost_usd,
         json.dumps(outputs), json.dumps(approval_requests), json.dumps(errors), run_id),
    )
    conn.commit()
    conn.close()

    log_entry = {
        "schema_version": 1,
        "event_id": _ulid(),
        "agent": agent,
        "action_type": "agent_run",
        "status": status,
        "started_at": started_at.isoformat(),
        "finished_at": ended_at.isoformat(),
        "duration_ms": duration_ms,
        "inputs_summary": f"--agent {agent}",
        "outputs_summary": f"{len(outputs)} file(s) written, {len(approval_requests)} approval request(s)",
        "cost_usd_estimate": cost_usd,
        "tool_calls": [],
        "errors": errors,
        "correlation_id": run_id,
        "parent_event_id": None,
        "approval_queue_ref": approval_requests[0] if approval_requests else None,
        "run_id": run_id,
        "tokens_in": tokens_in,
        "tokens_out": tokens_out,
        "outputs": outputs,
        "approval_requests": approval_requests,
    }
    emit_log(log_entry, agent)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser(description="Venture Factory agent runner")
    ap.add_argument("--agent", required=True)
    ap.add_argument("--input", dest="input_path")
    ap.add_argument("--dry-run", action="store_true", help="Simulate run without calling the API")
    args = ap.parse_args()

    agent = args.agent
    dry_run = args.dry_run
    policy = load_policy()

    agent_md_path = REPO_ROOT / "factory" / "agents" / agent / "AGENT.md"
    if not agent_md_path.exists():
        print(f"ERROR: No AGENT.md found for agent '{agent}' at {agent_md_path}", file=sys.stderr)
        return 1

    frontmatter, body = parse_frontmatter(agent_md_path.read_text(encoding="utf-8"))
    system_prompt = body + _PROTOCOL + _runtime_contract(agent)

    import db as _db
    _db.apply_migrations()
    conn = _db.get_connection()

    run_id = _ulid()
    started_at = datetime.now(timezone.utc)
    conn.execute("INSERT INTO runs (id, agent, started_at, status) VALUES (?,?,?,?)",
                 (run_id, agent, started_at.isoformat(), "running"))
    conn.commit()

    outputs: list[str] = []
    approval_requests: list[str] = []
    errors: list[dict] = []
    tokens_in = tokens_out = 0
    cost_usd = 0.0
    status = "succeeded"

    fixture_path: Path | None = None
    if args.input_path:
        fixture_path = (REPO_ROOT / args.input_path).resolve()
        if not validate_repo_path(fixture_path):
            print(f"ERROR: --input path escapes the repo: {args.input_path}", file=sys.stderr)
            conn.close()
            return 1

    try:
        if dry_run:
            model_output = _dry_run_output(agent, fixture_path)
            model = "dry-run"
            print(f"[dry-run] Generated synthetic output for agent '{agent}'")
        else:
            api_key = os.environ.get("ANTHROPIC_API_KEY", "")
            if not api_key:
                print("ERROR: ANTHROPIC_API_KEY not set in environment / .env", file=sys.stderr)
                conn.close()
                return 1
            if not _check_spend(policy, conn):
                err = "Per-day external API spend cap reached"
                errors.append({"code": "SPEND_CAP_EXCEEDED", "message": err})
                _finalize(run_id, agent, started_at, "failed", tokens_in, tokens_out,
                          cost_usd, outputs, approval_requests, errors, conn)
                print(f"ERROR: {err}", file=sys.stderr)
                return 1

            model, max_tokens = model_for(agent)
            user_msg = build_inputs(agent, frontmatter, fixture_path)

            import anthropic
            client = anthropic.Anthropic(api_key=api_key)
            resp = client.messages.create(
                model=model,
                max_tokens=max_tokens,
                system=system_prompt,
                messages=[{"role": "user", "content": user_msg}],
            )
            model_output = resp.content[0].text if resp.content else ""
            tokens_in = resp.usage.input_tokens
            tokens_out = resp.usage.output_tokens
            cost_usd = _cost_usd(model, tokens_in, tokens_out)
            _record_spend(agent, model, tokens_in, tokens_out, cost_usd, run_id, conn)

        # Process output.
        if agent == "market_radar":
            outputs += _process_market_radar(model_output, errors)
        elif agent == "opportunity_scoring":
            outputs += _process_opportunity_scoring(model_output, model, errors)
        elif agent == "pain_validation":
            outputs += _process_pain_validation(model_output, errors)
        elif agent == "daily_summary":
            outputs += _process_daily_summary(model_output, errors)
        else:
            action_blocks, file_writes = _parse_action_write_blocks(model_output)
            for action in action_blocks:
                req_id = write_approval_request(action, agent)
                approval_requests.append(req_id)
                print(f"Queued for approval: {req_id}")
            for rel_path, content in file_writes:
                abs_path = (REPO_ROOT / rel_path).resolve()
                if not validate_repo_path(abs_path):
                    msg = f"Rejected write outside repo: {rel_path}"
                    print(f"WARN: {msg}", file=sys.stderr)
                    errors.append({"code": "PATH_OUTSIDE_REPO", "message": msg})
                    continue
                abs_path.parent.mkdir(parents=True, exist_ok=True)
                abs_path.write_text(content, encoding="utf-8")
                outputs.append(rel_path)

        for o in outputs:
            print(f"Wrote: {o}")

    except Exception as exc:
        errors.append({"code": "RUNTIME_ERROR", "message": str(exc)})
        status = "failed"
        print(f"ERROR: {exc}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)

    if errors and status == "succeeded" and not outputs:
        status = "failed"

    _finalize(run_id, agent, started_at, status, tokens_in, tokens_out,
              cost_usd, outputs, approval_requests, errors, conn)
    return 0 if status == "succeeded" else 1


def _parse_action_write_blocks(text: str) -> tuple[list[dict], list[tuple[str, str]]]:
    actions: list[dict] = []
    writes: list[tuple[str, str]] = []
    for m in re.finditer(r"```action\s*\n(.*?)\n```", text, re.DOTALL):
        raw = m.group(1).strip()
        try:
            obj = json.loads(raw)
        except json.JSONDecodeError:
            try:
                obj = yaml.safe_load(raw)
            except Exception:
                obj = {"raw": raw}
        if isinstance(obj, dict):
            actions.append(obj)
    for m in re.finditer(r"```write:([^\n]+)\n(.*?)\n```", text, re.DOTALL):
        writes.append((m.group(1).strip(), m.group(2)))
    return actions, writes


if __name__ == "__main__":
    sys.exit(main())
