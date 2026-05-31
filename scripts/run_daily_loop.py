#!/usr/bin/env python3
"""
Daily agent loop runner.

Runs agents in the order defined in ARCHITECTURE.md section 9,
skipping those whose preconditions are unmet. Respects the Friday
18:00 IDT – Saturday 20:00 IDT read-only window.
"""
import json
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(REPO_ROOT / "scripts"))

# Agent schedule from ARCHITECTURE.md section 9.
# Each entry: (slot_label, agent_slug, external_send)
# external_send=True means the agent may send to the outside world and is
# blocked during the Shabbat read-only window.
DAILY_SCHEDULE = [
    ("05:55", "ceo_chief_of_staff", False),
    ("06:00", "market_radar",       False),
    ("07:00", "pain_validation",    False),
    ("08:00", "lead_research",      False),
    ("09:30", "opportunity_scoring",False),
    ("10:00", "daily_summary",      False),   # interim morning brief
    ("14:00", "cost_gain",          False),
    ("16:00", "build_decisions",    False),
    ("17:00", "service_builder",    False),
    ("17:30", "product_design",     False),
    ("17:30", "outreach",           True),    # drafts only at this slot
    ("19:00", "qa",                 False),
    ("20:00", "responsiveness_test",True),    # sends only if approved
    ("21:30", "analytics",          False),
    ("22:00", "daily_summary",      False),
]

# Precondition checkers: return True if agent may run.
def _has_opportunities(status: str | None = None) -> bool:
    opp_dir = REPO_ROOT / "opportunities"
    if not opp_dir.exists():
        return False
    for f in opp_dir.glob("*.json"):
        if status is None:
            return True
        try:
            data = json.loads(f.read_text())
            if data.get("status") == status:
                return True
        except Exception:
            continue
    return False


PRECONDITIONS: dict[str, callable] = {
    "pain_validation":     lambda: _has_opportunities("candidate"),
    "lead_research":       lambda: _has_opportunities("validated"),
    "opportunity_scoring": lambda: _has_opportunities(),
    "cost_gain":           lambda: _has_opportunities(),
    "build_decisions":     lambda: _has_opportunities("scored") or _has_opportunities("validated"),
    "service_builder":     lambda: any(
        (REPO_ROOT / "experiments").rglob("decision.json")
    ),
    "product_design":      lambda: any(
        (REPO_ROOT / "services").iterdir()
        if (REPO_ROOT / "services").exists() else []
    ),
    "outreach":            lambda: any(
        (REPO_ROOT / "services").rglob("outreach")
        if (REPO_ROOT / "services").exists() else []
    ),
    "responsiveness_test": lambda: any(
        (REPO_ROOT / "approval_queue").glob("*.approved.json")
    ),
    "qa":                  lambda: any(
        (REPO_ROOT / "approval_queue").glob("*.json")
        if (REPO_ROOT / "approval_queue").exists() else []
    ),
    "analytics":           lambda: any(
        (REPO_ROOT / "logs" / "runs").rglob("*.jsonl")
        if (REPO_ROOT / "logs" / "runs").exists() else []
    ),
}


def _idt_now() -> datetime:
    return datetime.now(timezone(timedelta(hours=3)))


def _is_shabbat_window() -> bool:
    now = _idt_now()
    weekday = now.weekday()  # Monday=0 … Sunday=6
    hour = now.hour
    minute = now.minute

    # Friday 18:00 – Saturday 20:00 IDT
    if weekday == 4 and (hour > 18 or (hour == 18 and minute >= 0)):
        return True
    if weekday == 5 and (hour < 20):
        return True
    return False


def _log_skip(agent: str, reason: str) -> None:
    print(f"[SKIP] {agent}: {reason}")
    # Write a skip log line so the daily summary can surface it.
    from datetime import timezone as tz
    import json as j
    date_str = _idt_now().strftime("%Y-%m-%d")
    log_dir = REPO_ROOT / "logs" / "runs" / date_str
    log_dir.mkdir(parents=True, exist_ok=True)
    with open(log_dir / f"{agent}.jsonl", "a", encoding="utf-8") as fh:
        fh.write(j.dumps({
            "schema_version": 1,
            "event_id": _new_ulid(),
            "agent": agent,
            "action_type": "agent_run",
            "status": "skipped",
            "started_at": _idt_now().isoformat(),
            "finished_at": _idt_now().isoformat(),
            "duration_ms": 0,
            "inputs_summary": "precondition not met",
            "outputs_summary": reason,
            "cost_usd_estimate": 0.0,
            "tool_calls": [],
            "errors": [],
            "correlation_id": _new_ulid(),
            "parent_event_id": None,
            "approval_queue_ref": None,
        }) + "\n")


def _new_ulid() -> str:
    from ulid import ULID
    return str(ULID())


def run_agent_subprocess(agent: str) -> int:
    result = subprocess.run(
        [sys.executable, str(REPO_ROOT / "scripts" / "run_agent.py"), "--agent", agent],
        cwd=REPO_ROOT,
    )
    return result.returncode


def main() -> int:
    shabbat = _is_shabbat_window()
    if shabbat:
        print("[INFO] Shabbat read-only window active. External-send agents will be skipped.")

    import db as _db
    _db.apply_migrations()

    exit_code = 0
    for slot, agent, is_external_send in DAILY_SCHEDULE:
        if shabbat and is_external_send:
            _log_skip(agent, "Shabbat read-only window — external send blocked")
            continue

        precond = PRECONDITIONS.get(agent)
        if precond is not None:
            try:
                ok = precond()
            except Exception as exc:
                ok = False
                print(f"[WARN] Precondition check for {agent} raised: {exc}", file=sys.stderr)
            if not ok:
                _log_skip(agent, "precondition not met")
                continue

        print(f"[RUN ] {slot} — {agent}")
        rc = run_agent_subprocess(agent)
        if rc != 0:
            print(f"[WARN] {agent} exited with code {rc}", file=sys.stderr)
            exit_code = rc  # continue remaining agents; record failure

    return exit_code


if __name__ == "__main__":
    sys.exit(main())
