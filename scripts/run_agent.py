#!/usr/bin/env python3
"""
Venture Factory agent runner.

Usage:
  run_agent.py --agent <slug> [--input <path>] [--dry-run]

Loads factory/agents/<slug>/AGENT.md as the system prompt, calls the
Anthropic API, intercepts action blocks for the approval queue, and
writes file-write blocks directly into the repo.
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

load_dotenv(REPO_ROOT / ".env")

# Appended to the AGENT.md body so every model knows the I/O protocol.
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
# Helpers
# ---------------------------------------------------------------------------

def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Return (frontmatter_dict, body_text). Body excludes the --- delimiters."""
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


def _ulid() -> str:
    from ulid import ULID
    return str(ULID())


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


def parse_output_blocks(text: str) -> tuple[list[dict], list[tuple[str, str]]]:
    """
    Scan model output for action and write blocks.
    Returns (action_dicts, [(rel_path, content), ...]).
    """
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


def write_approval_request(action: dict, agent: str) -> str:
    """Write approval_queue/<ulid>.json. Returns the ULID."""
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


def emit_log(entry: dict, agent: str) -> None:
    log_dir = REPO_ROOT / "logs" / "runs" / _idt_date()
    log_dir.mkdir(parents=True, exist_ok=True)
    with open(log_dir / f"{agent}.jsonl", "a", encoding="utf-8") as fh:
        fh.write(json.dumps(entry) + "\n")


# ---------------------------------------------------------------------------
# Dry-run synthetic output
# ---------------------------------------------------------------------------

def _dry_run_output(agent: str, fixture_path: Path | None) -> str:
    fixture: dict = {}
    if fixture_path and fixture_path.exists():
        with open(fixture_path, encoding="utf-8") as fh:
            fixture = json.load(fh)

    if agent == "market_radar":
        opp_id = _ulid()
        sources = fixture.get("sources", [])
        src = sources[0] if sources else {
            "type": "other",
            "url": "https://example.com/dry-run-signal",
            "content": "Dry-run signal with no fixture provided.",
        }
        snippet = (src.get("content") or src.get("snippet") or "No content available.")[:2000]
        opp = {
            "id": opp_id,
            "discovered_at": _idt_now().isoformat(),
            "source": {
                "type": src.get("type", "other"),
                "url": src.get("url", "https://example.com"),
                "snippet": snippet,
            },
            "problem_statement": (
                "Freelancers and small businesses spend 2-3 hours monthly reconciling "
                "invoices with bank transactions manually, with accountants charging extra "
                "for the resulting cleanup work."
            ),
            "target_segment": (
                "Freelancers and small business owners processing 20-200 monthly transactions"
            ),
            "geo": "GLOBAL",
            "signal_strength": 3,
            "keywords": ["invoicing", "reconciliation", "bookkeeping", "freelance"],
            "notes": "Dry-run synthetic opportunity generated by market_radar smoke test.",
            "status": "candidate",
        }
        return f"```write:opportunities/{opp_id}.json\n{json.dumps(opp, indent=2)}\n```"

    return f"[dry-run] No synthetic output defined for agent '{agent}'."


# ---------------------------------------------------------------------------
# User message construction (for real API calls)
# ---------------------------------------------------------------------------

def _build_user_message(frontmatter: dict, fixture_path: Path | None) -> str:
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
        parts.append(
            "No input files found. Proceed based on your agent instructions, "
            "scanning any sources you are configured to use."
        )

    return "\n\n".join(parts)


# ---------------------------------------------------------------------------
# Spend cap enforcement
# ---------------------------------------------------------------------------

def _check_spend(policy: dict, conn) -> bool:
    cap = policy.get("caps", {}).get("per_day_external_api_usd", 25.0)
    today = _idt_date()
    row = conn.execute(
        "SELECT COALESCE(SUM(cost_usd), 0.0) FROM spend_ledger WHERE date=?",
        (today,),
    ).fetchone()
    return float(row[0]) < cap


def _record_spend(agent: str, cost: float, run_id: str, conn) -> None:
    conn.execute(
        "INSERT INTO spend_ledger (id, agent, date, cost_usd, run_id, created_at) "
        "VALUES (?,?,?,?,?,?)",
        (_ulid(), agent, _idt_date(), cost, run_id, datetime.now(timezone.utc).isoformat()),
    )
    conn.commit()


# ---------------------------------------------------------------------------
# Finalize: update DB + emit log line
# ---------------------------------------------------------------------------

def _finalize(
    run_id: str,
    agent: str,
    started_at: datetime,
    status: str,
    tokens_in: int,
    tokens_out: int,
    cost_usd: float,
    outputs: list[str],
    approval_requests: list[str],
    errors: list[dict],
    conn,
) -> None:
    ended_at = datetime.now(timezone.utc)
    duration_ms = int((ended_at - started_at).total_seconds() * 1000)

    conn.execute(
        """UPDATE runs
           SET ended_at=?, status=?, tokens_in=?, tokens_out=?,
               cost_usd_estimate=?, outputs=?, approval_requests=?, errors=?
           WHERE id=?""",
        (
            ended_at.isoformat(),
            status,
            tokens_in,
            tokens_out,
            cost_usd,
            json.dumps(outputs),
            json.dumps(approval_requests),
            json.dumps(errors),
            run_id,
        ),
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
        "outputs_summary": (
            f"{len(outputs)} file(s) written, {len(approval_requests)} approval request(s)"
        ),
        "cost_usd_estimate": cost_usd,
        "tool_calls": [],
        "errors": errors,
        "correlation_id": run_id,
        "parent_event_id": None,
        "approval_queue_ref": approval_requests[0] if approval_requests else None,
        # runner-specific extensions
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
    ap.add_argument("--agent", required=True, help="Agent slug (directory name under factory/agents/)")
    ap.add_argument("--input", dest="input_path", help="Input file path relative to repo root")
    ap.add_argument("--dry-run", action="store_true", help="Simulate run without calling the API")
    args = ap.parse_args()

    agent: str = args.agent
    input_path_rel: str | None = args.input_path
    dry_run: bool = args.dry_run

    policy = load_policy()

    # logs_format.yaml is referenced for schema_version; load for info only.
    logs_fmt_path = REPO_ROOT / "config" / "logs_format.yaml"
    if logs_fmt_path.exists():
        try:
            yaml.safe_load(logs_fmt_path.read_text())
        except Exception:
            pass

    agent_md_path = REPO_ROOT / "factory" / "agents" / agent / "AGENT.md"
    if not agent_md_path.exists():
        print(f"ERROR: No AGENT.md found for agent '{agent}' at {agent_md_path}", file=sys.stderr)
        return 1

    frontmatter, body = parse_frontmatter(agent_md_path.read_text(encoding="utf-8"))
    system_prompt = body + _PROTOCOL

    import db as _db  # scripts/db.py — importable because REPO_ROOT/scripts is on sys.path
    _db.apply_migrations()
    conn = _db.get_connection()

    run_id = _ulid()
    started_at = datetime.now(timezone.utc)

    conn.execute(
        "INSERT INTO runs (id, agent, started_at, status) VALUES (?,?,?,?)",
        (run_id, agent, started_at.isoformat(), "running"),
    )
    conn.commit()

    outputs: list[str] = []
    approval_requests: list[str] = []
    errors: list[dict] = []
    tokens_in = tokens_out = 0
    cost_usd = 0.0
    status = "succeeded"

    fixture_path: Path | None = None
    if input_path_rel:
        fixture_path = (REPO_ROOT / input_path_rel).resolve()
        if not validate_repo_path(fixture_path):
            print(f"ERROR: --input path escapes the repo: {input_path_rel}", file=sys.stderr)
            conn.close()
            return 1

    try:
        if dry_run:
            model_output = _dry_run_output(agent, fixture_path)
            print(f"[dry-run] Generated synthetic output for agent '{agent}'")
        else:
            api_key = os.environ.get("ANTHROPIC_API_KEY", "")
            if not api_key:
                print("ERROR: ANTHROPIC_API_KEY not set in environment / .env", file=sys.stderr)
                return 1

            if not _check_spend(policy, conn):
                err = "Per-day external API spend cap reached"
                errors.append({"code": "SPEND_CAP_EXCEEDED", "message": err})
                status = "failed"
                _finalize(run_id, agent, started_at, status, tokens_in, tokens_out,
                          cost_usd, outputs, approval_requests, errors, conn)
                print(f"ERROR: {err}", file=sys.stderr)
                return 1

            import anthropic
            client = anthropic.Anthropic(api_key=api_key)
            user_msg = _build_user_message(frontmatter, fixture_path)
            resp = client.messages.create(
                model="claude-opus-4-5",
                max_tokens=4096,
                system=system_prompt,
                messages=[{"role": "user", "content": user_msg}],
            )
            model_output = resp.content[0].text
            tokens_in = resp.usage.input_tokens
            tokens_out = resp.usage.output_tokens
            # Rough cost: claude-opus-4-5 pricing estimate ($15/Mtok in, $75/Mtok out)
            cost_usd = (tokens_in * 15 + tokens_out * 75) / 1_000_000
            _record_spend(agent, cost_usd, run_id, conn)

        action_blocks, file_writes = parse_output_blocks(model_output)

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
            print(f"Wrote: {rel_path}")

    except Exception as exc:
        errors.append({"code": "RUNTIME_ERROR", "message": str(exc)})
        status = "failed"
        print(f"ERROR: {exc}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)

    _finalize(run_id, agent, started_at, status, tokens_in, tokens_out,
              cost_usd, outputs, approval_requests, errors, conn)

    return 0 if status == "succeeded" else 1


if __name__ == "__main__":
    sys.exit(main())
