#!/usr/bin/env python3
"""Build dashboard/data.json — a sanitized, read-only snapshot of the factory.

Aggregates the on-disk data model into ONE JSON file that the static page
(dashboard/index.html) renders client-side. Read-only over the repo and
factory/state.db; writes ONLY to dashboard/.

NEVER reads .env, customers/, payments/, security/, or leads/*.jsonl. Free-text
is email-redacted to `email#<sha256[:12]>` before emission, and a final
self-check greps the produced JSON for secret-shaped tokens / raw emails and
aborts loudly if any survive. Hard-fail beats ever shipping a secret or PII.

On-disk model (authoritative; not the aspirational AGENT.md paths):
  opportunities/<id>.opportunity.json  + sibling .scoring.json / .verdict.json
                                         / .decision.json / .cost_gain.json
  reports/daily/<date>.md
  approval_queue/<ulid>.json   (exclude *.approved.json / *.rejected.json)
  services/<slug>/status.md
  factory/state.db -> spend_ledger
  logs/runs/<date>/<agent>.jsonl
  dashboards/*.json (+ dashboards/data/*.json) -> analytics (optional)
"""
import hashlib
import json
import re
import sqlite3
import sys
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent.resolve()
OPP_DIR = REPO_ROOT / "opportunities"
REPORTS_DIR = REPO_ROOT / "reports" / "daily"
QUEUE_DIR = REPO_ROOT / "approval_queue"
SERVICES_DIR = REPO_ROOT / "services"
LOGS_DIR = REPO_ROOT / "logs" / "runs"
ANALYTICS_DIR = REPO_ROOT / "dashboards"          # plural: analytics agent funnel JSON
STATE_DB = REPO_ROOT / "factory" / "state.db"

OUT_DIR = REPO_ROOT / "dashboard"                 # singular: the published page
OUT_FILE = OUT_DIR / "data.json"

UTC = timezone.utc
IDT = timezone(timedelta(hours=3))

STAGE_WORDS = {"validating", "building", "launched", "scaling", "killed", "paused"}
LAUNCHED_STAGES = {"launched", "scaling"}

EMAIL_RE = re.compile(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}")


# ---------------------------------------------------------------------------
# Sanitization helpers
# ---------------------------------------------------------------------------

def _sha12(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()[:12]


def _redact(text: str | None) -> str:
    """Replace any raw email with a stable truncated hash. Applied to every
    free-text string before it enters the export."""
    if not text:
        return ""
    return EMAIL_RE.sub(lambda m: f"email#{_sha12(m.group(0))}", text)


def _trunc(text: str | None, limit: int) -> str:
    s = _redact((text or "").strip())
    if len(s) <= limit:
        return s
    return s[: max(0, limit - 1)].rstrip() + "…"


def _read_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None


# ---------------------------------------------------------------------------
# Opportunity aggregation (funnel + top list)
# ---------------------------------------------------------------------------

def _collect_opportunities():
    """Returns (joined rows, funnel counts). One row per *.opportunity.json,
    joined with whatever sibling files happen to exist."""
    rows = []
    for opp_file in sorted(OPP_DIR.glob("*.opportunity.json")):
        base = opp_file.name[: -len(".opportunity.json")]
        opp = _read_json(opp_file)
        if not isinstance(opp, dict):
            continue
        scoring = _read_json(OPP_DIR / f"{base}.scoring.json")
        verdict = _read_json(OPP_DIR / f"{base}.verdict.json")
        # build decision lives as <base>.decision.json on disk; tolerate the
        # alternate .build_decision.json name too.
        decision = _read_json(OPP_DIR / f"{base}.decision.json") or _read_json(
            OPP_DIR / f"{base}.build_decision.json"
        )
        cost_gain = _read_json(OPP_DIR / f"{base}.cost_gain.json")
        rows.append({
            "base": base,
            "opp": opp,
            "scoring": scoring if isinstance(scoring, dict) else None,
            "verdict": verdict if isinstance(verdict, dict) else None,
            "decision": decision if isinstance(decision, dict) else None,
            "cost_gain": cost_gain if isinstance(cost_gain, dict) else None,
        })
    return rows


def _decision_type(decision: dict) -> str | None:
    """Normalize a build-decision record to build_now / defer / kill.
    The on-disk shape is not finalized, so probe a few likely fields."""
    if not decision:
        return None
    for key in ("decision", "recommended_action", "action", "verdict", "outcome"):
        val = decision.get(key)
        if isinstance(val, str) and val.strip():
            v = val.strip().lower().replace("-", "_").replace(" ", "_")
            if v in ("build", "build_now", "go"):
                return "build_now"
            if v in ("defer", "hold", "wait", "later"):
                return "defer"
            if v in ("kill", "drop", "no_go", "reject"):
                return "kill"
            return v  # surface unknown values rather than hide them
    return None


def _funnel(rows, services):
    by_decision = defaultdict(int)
    for r in rows:
        dt = _decision_type(r["decision"])
        if dt:
            by_decision[dt] += 1
    scaffolded = len(services)
    launched = sum(1 for s in services if (s.get("current_stage") or "") in LAUNCHED_STAGES)
    return {
        "candidates": len(rows),
        "scored": sum(1 for r in rows if r["scoring"]),
        "validated": sum(
            1 for r in rows if r["verdict"] and r["verdict"].get("status") == "validated"
        ),
        "build_decisions": dict(by_decision),
        "build_now": by_decision.get("build_now", 0),
        "services_scaffolded": scaffolded,
        "services_launched": launched,
    }


def _top_opportunities(rows, limit=25):
    scored = [r for r in rows if r["scoring"] and r["scoring"].get("total") is not None]

    def total_of(r):
        try:
            return float(r["scoring"].get("total", 0))
        except (TypeError, ValueError):
            return 0.0

    scored.sort(key=total_of, reverse=True)
    # Surface the dimensions the operator cares about most, in plain-language keys.
    DIM_LABELS = {
        "buyer_clarity": "Who pays",
        "operational_autonomy": "Runs alone",
        "willingness_to_pay": "Will pay",
        "buildability_with_ai": "Buildable",
        "pain_severity": "Pain",
    }
    out = []
    for r in scored[:limit]:
        opp, sc, vr = r["opp"], r["scoring"], r["verdict"]
        src = opp.get("source") or {}
        per_dim = sc.get("per_dimension") or {}
        scores = {}
        for key, label in DIM_LABELS.items():
            if isinstance(per_dim.get(key), (int, float)):
                scores[label] = per_dim[key]
        out.append({
            "id": opp.get("id", r["base"]),
            # Full problem text — the schema caps it at 500 chars, so show it all.
            "problem_statement": _trunc(opp.get("problem_statement"), 520),
            "target_segment": _trunc(opp.get("target_segment"), 240),
            "total": round(total_of(r), 1),
            "recommended_stage": sc.get("recommended_stage"),
            # Plain-language "why this score / who pays / can it run alone".
            "rationale": _trunc(sc.get("rationale"), 500),
            "scores": scores,           # {"Who pays": 8, "Runs alone": 7, ...}
            "verdict": vr.get("status") if vr else None,
            "source_type": src.get("type"),
            "source_url": src.get("url"),  # public links are fine
            "discovered_at": opp.get("discovered_at"),
        })
    return out


# ---------------------------------------------------------------------------
# Approvals — the operator's to-do list
# ---------------------------------------------------------------------------

def _approvals(now_idt):
    out = []
    if not QUEUE_DIR.exists():
        return out
    for qf in sorted(QUEUE_DIR.glob("*.json")):
        if qf.name.endswith((".approved.json", ".rejected.json")):
            continue
        obj = _read_json(qf)
        if not isinstance(obj, dict):
            continue
        age_h = None
        created = obj.get("created_at", "")
        try:
            age_h = round((now_idt - datetime.fromisoformat(created)).total_seconds() / 3600, 1)
        except Exception:
            pass
        cost = obj.get("cost_estimate_usd")
        if cost is None:
            cost = obj.get("projected_call_usd")
        out.append({
            "ulid": obj.get("ulid") or qf.stem,
            "agent": obj.get("agent"),
            "action_type": obj.get("action_type"),
            "summary": _trunc(obj.get("summary"), 120),
            "age_hours": age_h,
            "expires_at": obj.get("expires_at"),
            "cost_estimate_usd": cost,
        })
    # Most urgent (oldest) first.
    out.sort(key=lambda a: (a["age_hours"] is None, -(a["age_hours"] or 0)))
    return out


# ---------------------------------------------------------------------------
# Services
# ---------------------------------------------------------------------------

def _parse_status_md(text: str):
    stage = None
    m = re.search(r"Current stage:\s*`?([A-Za-z]+)`?", text)
    if m and m.group(1).lower() in STAGE_WORDS:
        stage = m.group(1).lower()
    if stage is None:  # fall back to first known stage word in the doc body
        for w in re.findall(r"[A-Za-z]+", text):
            if w.lower() in STAGE_WORDS:
                stage = w.lower()
                break
    started = None
    m = re.search(r"(?:Created at|Stage entered at)[^\n]*\n+[^\n]*?"
                  r"(\d{4}-\d{2}-\d{2}(?:[ T]\d{2}:\d{2})?)", text)
    if m:
        started = m.group(1)
    # last signal = last non-comment, non-example data row of a markdown table
    last_signal = None
    for line in reversed(text.splitlines()):
        s = line.strip()
        if s.startswith("|") and "---" not in s and "<!--" not in s and "EXAMPLE" not in s:
            cells = [c.strip() for c in s.strip("|").split("|")]
            if cells and cells[0] and not cells[0].lower().startswith("date"):
                last_signal = _trunc(" / ".join(c for c in cells if c), 120)
                break
    return stage, started, last_signal


def _services():
    out = []
    if not SERVICES_DIR.exists():
        return out
    for status_md in sorted(SERVICES_DIR.glob("*/status.md")):
        slug = status_md.parent.name
        try:
            text = status_md.read_text(encoding="utf-8")
        except Exception:
            text = ""
        stage, started, last_signal = _parse_status_md(text)
        out.append({
            "slug": slug,
            "current_stage": stage,
            "started_at": started,
            "last_signal": last_signal,
        })
    return out


# ---------------------------------------------------------------------------
# Spend (read-only query over spend_ledger)
# ---------------------------------------------------------------------------

def _spend(today_idt_date: str):
    empty = {"today_usd": 0.0, "last_7_days_usd": 0.0, "all_time_usd": 0.0,
             "by_day": [], "by_agent": []}
    if not STATE_DB.exists():
        return empty
    try:
        con = sqlite3.connect(f"file:{STATE_DB}?mode=ro", uri=True)
    except sqlite3.Error:
        return empty
    try:
        cur = con.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='spend_ledger'")
        if not cur.fetchone():
            return empty
        all_time = cur.execute("SELECT COALESCE(SUM(cost_usd),0) FROM spend_ledger").fetchone()[0] or 0.0
        by_day_rows = cur.execute(
            "SELECT date, ROUND(SUM(cost_usd),4) FROM spend_ledger "
            "GROUP BY date ORDER BY date DESC LIMIT 7"
        ).fetchall()
        by_day = [{"date": d, "usd": float(v or 0)} for d, v in reversed(by_day_rows)]
        recent_dates = [d for d, _ in by_day_rows]
        by_agent = []
        if recent_dates:
            placeholders = ",".join("?" * len(recent_dates))
            rows = cur.execute(
                f"SELECT agent, ROUND(SUM(cost_usd),4) FROM spend_ledger "
                f"WHERE date IN ({placeholders}) GROUP BY agent ORDER BY 2 DESC",
                recent_dates,
            ).fetchall()
            by_agent = [{"agent": a, "usd": float(v or 0)} for a, v in rows]
        last7 = sum(d["usd"] for d in by_day)
        today = cur.execute(
            "SELECT COALESCE(SUM(cost_usd),0) FROM spend_ledger WHERE date=?",
            (today_idt_date,),
        ).fetchone()[0] or 0.0
        return {
            "today_usd": round(float(today), 4),
            "last_7_days_usd": round(float(last7), 4),
            "all_time_usd": round(float(all_time), 4),
            "by_day": by_day,
            "by_agent": by_agent,
        }
    except sqlite3.Error:
        return empty
    finally:
        con.close()


# ---------------------------------------------------------------------------
# Activity heatmap (last 7 days of run logs)
# ---------------------------------------------------------------------------

def _activity(today_idt):
    days = [(today_idt - timedelta(days=i)).strftime("%Y-%m-%d") for i in range(6, -1, -1)]
    out = []
    for day in days:
        day_dir = LOGS_DIR / day
        per_agent: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
        if day_dir.exists():
            for jf in sorted(day_dir.glob("*.jsonl")):
                for line in jf.read_text(encoding="utf-8").splitlines():
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        e = json.loads(line)
                    except Exception:
                        continue
                    agent = e.get("agent", jf.stem)
                    status = e.get("status", "unknown")
                    per_agent[agent][status] += 1
        out.append({
            "date": day,
            "agents": {a: dict(s) for a, s in sorted(per_agent.items())},
        })
    return out


# ---------------------------------------------------------------------------
# Latest daily report excerpt
# ---------------------------------------------------------------------------

def _latest_report_excerpt(max_lines=40):
    if not REPORTS_DIR.exists():
        return None
    md_files = list(REPORTS_DIR.glob("*.md"))
    if not md_files:
        return None

    def sort_key(p: Path):
        m = re.match(r"(\d{4}-\d{2}-\d{2})", p.name)
        return (m.group(1) if m else "0000-00-00", p.name)

    latest = max(md_files, key=sort_key)
    try:
        lines = latest.read_text(encoding="utf-8").splitlines()
    except Exception:
        return None
    excerpt = "\n".join(lines[:max_lines])
    return {
        "file": f"reports/daily/{latest.name}",
        "date": sort_key(latest)[0],
        "text": _redact(excerpt),
        "truncated": len(lines) > max_lines,
    }


# ---------------------------------------------------------------------------
# Optional analytics fold-in (created later by prompt C)
# ---------------------------------------------------------------------------

def _analytics():
    if not ANALYTICS_DIR.exists():
        return None
    found = {}
    for jf in sorted(list(ANALYTICS_DIR.glob("*.json")) + list(ANALYTICS_DIR.glob("data/*.json"))):
        data = _read_json(jf)
        if data is not None:
            found[jf.relative_to(ANALYTICS_DIR).as_posix()] = data
    return found or None


# ---------------------------------------------------------------------------
# Leak self-check (backstop after redaction)
# ---------------------------------------------------------------------------
# NOTE on interpretation: a naive substring scan for "sk-", "STRIPE", or "@"
# would false-positive on ordinary text ("task-", "risk-", the company name
# "Stripe", "5 items @ $3"), which would block the dashboard on legitimate
# data. We instead scan for *secret-shaped* occurrences: real key prefixes,
# env-var assignments/names, and RFC-shaped emails. Emails are already redacted
# upstream; this is the backstop.
LEAK_PATTERNS = [
    ("anthropic_api_key", re.compile(r"sk-ant-[A-Za-z0-9\-_]{8,}")),
    ("openai_style_key", re.compile(r"sk-(?:proj-)?[A-Za-z0-9]{20,}")),
    ("stripe_secret_key", re.compile(r"\b[rs]k_(?:live|test)_[A-Za-z0-9]{8,}")),
    ("resend_api_key", re.compile(r"\bre_[A-Za-z0-9]{16,}")),
    ("env_secret_assignment",
     re.compile(r"(?:ANTHROPIC|RESEND|STRIPE|CLOUDFLARE)[A-Z0-9_]*\s*=\s*\S")),
    ("env_secret_name",
     re.compile(r"\b(?:ANTHROPIC_API_KEY|RESEND_API_KEY|STRIPE_API_KEY|"
                r"CLOUDFLARE_API_TOKEN)\b")),
    ("raw_email", EMAIL_RE),
]


def _mask(s: str) -> str:
    if len(s) <= 6:
        return "*" * len(s)
    return s[:2] + "*" * (len(s) - 4) + s[-2:]


def _self_check(serialized: str) -> None:
    hits = []
    for label, pat in LEAK_PATTERNS:
        for m in pat.finditer(serialized):
            hits.append((label, _mask(m.group(0))))
    if hits:
        print("FATAL: dashboard export aborted — potential secret/PII leak detected:",
              file=sys.stderr)
        for label, masked in hits[:20]:
            print(f"  - {label}: {masked}", file=sys.stderr)
        raise SystemExit(2)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    now_idt = datetime.now(IDT)
    now_utc = datetime.now(UTC)
    today_idt_date = now_idt.strftime("%Y-%m-%d")

    rows = _collect_opportunities()
    services = _services()

    data = {
        "generated_at": {
            "utc": now_utc.replace(microsecond=0).isoformat(),
            "idt": now_idt.replace(microsecond=0).isoformat(),
        },
        "funnel": _funnel(rows, services),
        "top_opportunities": _top_opportunities(rows),
        "approvals": _approvals(now_idt),
        "services": services,
        "spend": _spend(today_idt_date),
        "activity": _activity(now_idt),
        "latest_report_excerpt": _latest_report_excerpt(),
        "analytics": _analytics(),
    }

    serialized = json.dumps(data, indent=2, ensure_ascii=False)
    _self_check(serialized)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_FILE.write_text(serialized + "\n", encoding="utf-8")

    f = data["funnel"]
    print(f"Wrote {OUT_FILE.relative_to(REPO_ROOT)} "
          f"({len(serialized)} bytes): {f['candidates']} candidates, "
          f"{f['scored']} scored, {f['validated']} validated, "
          f"{len(data['approvals'])} pending approvals, "
          f"{len(services)} service(s); leak self-check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
