#!/usr/bin/env python3
"""
Daily agent loop runner (Phase 1).

Runs the discovery + scoring core in the order from ARCHITECTURE.md section 9:

    market_radar -> pain_validation -> opportunity_scoring
                 -> cost_gain (stub) -> build_decisions (stub) -> daily_summary

Each step runs in its own try/except so one failure does not stop the rest.
Preconditions are file-based (sibling .opportunity/.scoring/.verdict files).
Respects the Friday 18:00 IDT - Saturday 20:00 IDT read-only window (none of
the Phase-1 agents send externally, so the window is informational here; P3
hardens enforcement).
"""
import json
import os
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import yaml
from dotenv import load_dotenv

REPO_ROOT = Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(REPO_ROOT / "scripts"))

load_dotenv(REPO_ROOT / ".env")

# Action types that must not fire during the Shabbat read-only window.
SHABBAT_BLOCKED_ACTIONS = {
    "send_outreach_email", "send_outreach_sms", "create_payment_link",
    "charge_customer", "deploy_public_domain", "send_customer_message",
}

# (slot_label, agent_slug, external_send)
DAILY_SEQUENCE = [
    ("06:00", "market_radar",        False),
    ("07:00", "pain_validation",     False),
    ("09:30", "opportunity_scoring", False),
    ("14:00", "cost_gain",           False),
    ("16:00", "build_decisions",     False),
    ("22:00", "daily_summary",       False),
]

# Agents not yet implemented for Phase 1 — logged as NOT_IMPLEMENTED, no API call.
STUB_AGENTS = {"cost_gain", "build_decisions"}

OPP_DIR = REPO_ROOT / "opportunities"


def _idt_now() -> datetime:
    return datetime.now(timezone(timedelta(hours=3)))


def _scoring_threshold() -> float:
    p = REPO_ROOT / "config" / "scoring_model.yaml"
    try:
        sm = yaml.safe_load(p.read_text()) or {}
        return float((sm.get("thresholds", {}) or {}).get("min_total_to_validate", 5.5))
    except Exception:
        return 5.5


def _opportunity_scoring_has_work() -> bool:
    for f in OPP_DIR.glob("*.opportunity.json"):
        base = f.name[: -len(".opportunity.json")]
        if not (OPP_DIR / f"{base}.scoring.json").exists():
            return True
    return False


def _pain_validation_has_work() -> bool:
    threshold = _scoring_threshold()
    for sf in OPP_DIR.glob("*.scoring.json"):
        base = sf.name[: -len(".scoring.json")]
        if (OPP_DIR / f"{base}.verdict.json").exists():
            continue
        try:
            total = float(json.loads(sf.read_text()).get("total", 0))
        except Exception:
            continue
        if total >= threshold and (OPP_DIR / f"{base}.opportunity.json").exists():
            return True
    return False


PRECONDITIONS = {
    "market_radar": lambda: True,
    "pain_validation": _pain_validation_has_work,
    "opportunity_scoring": _opportunity_scoring_has_work,
    "daily_summary": lambda: True,
}


def _is_shabbat_window() -> bool:
    now = _idt_now()
    weekday = now.weekday()  # Mon=0 .. Sun=6
    if weekday == 4 and now.hour >= 18:      # Friday from 18:00
        return True
    if weekday == 5 and now.hour < 20:       # Saturday until 20:00
        return True
    return False


def _load_policy_or_die() -> dict:
    """Fail closed: missing/unparseable approval policy halts the loop."""
    p = REPO_ROOT / "config" / "approval_policy.yaml"
    if not p.exists():
        print("FATAL: fail-closed: approval policy unreadable", file=sys.stderr)
        sys.exit(1)
    try:
        data = yaml.safe_load(p.read_text())
        if not isinstance(data, dict):
            raise ValueError("not a mapping")
        return data
    except Exception:
        print("FATAL: fail-closed: approval policy unreadable", file=sys.stderr)
        sys.exit(1)


def _agent_permissions(agent: str, policy: dict) -> set:
    """Permissions an agent holds: AGENT.md frontmatter `permissions` unioned
    with the agent's requires-approval roles in approval_policy.yaml."""
    perms: set = set()
    md = REPO_ROOT / "factory" / "agents" / agent / "AGENT.md"
    if md.exists():
        text = md.read_text()
        if text.startswith("---"):
            end = text.find("\n---", 3)
            if end != -1:
                try:
                    fm = yaml.safe_load(text[3:end]) or {}
                    perms.update(fm.get("permissions") or [])
                except yaml.YAMLError:
                    pass
    perms.update((policy.get("roles") or {}).get(agent, []) or [])
    return perms


def _shabbat_blocks(agent: str, policy: dict | None = None) -> bool:
    """True if this agent holds any action type blocked during the Shabbat window."""
    if policy is None:
        policy = _load_policy_or_die()
    return bool(_agent_permissions(agent, policy) & SHABBAT_BLOCKED_ACTIONS)


def _new_ulid() -> str:
    from ulid import ULID
    return str(ULID())


def _log_line(agent: str, status: str, reason: str) -> None:
    print(f"[{status.upper()}] {agent}: {reason}")
    date_str = _idt_now().strftime("%Y-%m-%d")
    log_dir = REPO_ROOT / "logs" / "runs" / date_str
    log_dir.mkdir(parents=True, exist_ok=True)
    now_iso = _idt_now().isoformat()
    with open(log_dir / f"{agent}.jsonl", "a", encoding="utf-8") as fh:
        fh.write(json.dumps({
            "schema_version": 1,
            "event_id": _new_ulid(),
            "agent": agent,
            "action_type": "agent_run",
            "status": status,
            "started_at": now_iso,
            "finished_at": now_iso,
            "duration_ms": 0,
            "inputs_summary": "daily loop",
            "outputs_summary": reason,
            "cost_usd_estimate": 0.0,
            "tool_calls": [],
            "errors": [],
            "correlation_id": _new_ulid(),
            "parent_event_id": None,
            "approval_queue_ref": None,
        }) + "\n")


def run_agent_subprocess(agent: str) -> int:
    return subprocess.run(
        [sys.executable, str(REPO_ROOT / "scripts" / "run_agent.py"), "--agent", agent],
        cwd=REPO_ROOT,
    ).returncode


def main() -> int:
    # Fail closed at startup.
    policy = _load_policy_or_die()
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("ERROR: ANTHROPIC_API_KEY required; see .env.example", file=sys.stderr)
        return 1

    read_only = _is_shabbat_window()
    if read_only:
        print("[INFO] RUN_MODE=read_only (Shabbat window): outreach/payment/deploy/"
              "customer-send agents will be skipped.")

    import db as _db
    _db.apply_migrations()

    exit_code = 0
    for slot, agent, _external in DAILY_SEQUENCE:
        try:
            if read_only and _shabbat_blocks(agent, policy):
                _log_line(agent, "skipped", "shabbat_read_only")
                continue

            if agent in STUB_AGENTS:
                _log_line(agent, "skipped", "NOT_IMPLEMENTED (Phase 1 stub)")
                continue

            precond = PRECONDITIONS.get(agent)
            if precond is not None and not precond():
                _log_line(agent, "skipped", "precondition not met (no work)")
                continue

            print(f"[RUN ] {slot} - {agent}")
            rc = run_agent_subprocess(agent)
            if rc != 0:
                print(f"[WARN] {agent} exited with code {rc}", file=sys.stderr)
                exit_code = rc
        except Exception as exc:  # one failure must not stop the rest
            print(f"[WARN] {agent} raised in loop: {exc}", file=sys.stderr)
            exit_code = 1

    return exit_code


if __name__ == "__main__":
    sys.exit(main())
