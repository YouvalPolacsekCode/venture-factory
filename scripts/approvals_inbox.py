#!/usr/bin/env python3
"""
Operator approvals inbox.

Lists pending approval_queue/*.json items (ulid, agent, action_type, age_hours,
cost_estimate_usd, summary), newest first. Supports bulk approve/reject by
action_type glob.

Usage:
  approvals_inbox.py                                  # list all pending
  approvals_inbox.py --expiring                       # only items expiring within 6h
  approvals_inbox.py --bulk-approve 'spend_*'         # approve all matching action_types
  approvals_inbox.py --bulk-reject 'send_*' --reason "out of scope"
"""
import argparse
import fnmatch
import json
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent.resolve()
QUEUE = REPO_ROOT / "approval_queue"
EXPIRING_WINDOW_H = 6


def _idt_now() -> datetime:
    return datetime.now(timezone(timedelta(hours=3)))


def _parse_dt(s: str):
    try:
        return datetime.fromisoformat(s)
    except (TypeError, ValueError):
        return None


def _pending() -> list[dict]:
    items = []
    if not QUEUE.exists():
        return items
    now = _idt_now()
    for f in QUEUE.glob("*.json"):
        if f.name.endswith((".approved.json", ".rejected.json")):
            continue
        try:
            obj = json.loads(f.read_text())
        except json.JSONDecodeError:
            continue
        created = _parse_dt(obj.get("created_at", ""))
        expires = _parse_dt(obj.get("expires_at", ""))
        age_h = round((now - created).total_seconds() / 3600, 1) if created else None
        h_to_exp = round((expires - now).total_seconds() / 3600, 1) if expires else None
        items.append({
            "ulid": obj.get("ulid", f.stem),
            "agent": obj.get("agent", "?"),
            "action_type": obj.get("action_type", "?"),
            "age_hours": age_h,
            "hours_to_expiry": h_to_exp,
            "cost_estimate_usd": obj.get("cost_estimate_usd", 0.0),
            "summary": (obj.get("summary", "") or "")[:80],
            "created_at": obj.get("created_at", ""),
        })
    items.sort(key=lambda x: x["created_at"], reverse=True)
    return items


def _print_table(items: list[dict]) -> None:
    if not items:
        print("Approval queue is empty — nothing waiting on you.")
        return
    hdr = f"{'ulid':<28}{'agent':<18}{'action_type':<24}{'age_h':>7}{'exp_h':>7}{'USD':>8}  summary"
    print(hdr)
    print("-" * len(hdr))
    for it in items:
        age = f"{it['age_hours']}" if it['age_hours'] is not None else "-"
        exp = f"{it['hours_to_expiry']}" if it['hours_to_expiry'] is not None else "-"
        print(f"{it['ulid']:<28}{it['agent']:<18}{it['action_type']:<24}"
              f"{age:>7}{exp:>7}{it['cost_estimate_usd']:>8.4f}  {it['summary']}")
    print(f"\n{len(items)} pending.")


def _bulk(items: list[dict], glob: str, reject_reason: str | None) -> int:
    matched = [it for it in items if fnmatch.fnmatch(it["action_type"], glob)]
    if not matched:
        print(f"No pending items match action_type glob '{glob}'.")
        return 0
    rc_total = 0
    for it in matched:
        if reject_reason is None:
            cmd = [sys.executable, str(REPO_ROOT / "scripts" / "approve.py"), it["ulid"]]
        else:
            cmd = [sys.executable, str(REPO_ROOT / "scripts" / "reject.py"),
                   it["ulid"], "--reason", reject_reason]
        r = subprocess.run(cmd, cwd=REPO_ROOT, capture_output=True, text=True)
        verb = "reject" if reject_reason is not None else "approve"
        status = "OK" if r.returncode == 0 else f"FAILED rc={r.returncode}"
        print(f"  [{verb}] {it['ulid']} ({it['action_type']}): {status}")
        if r.returncode != 0:
            rc_total = 1
            if r.stderr.strip():
                print(f"        {r.stderr.strip()}", file=sys.stderr)
    return rc_total


def main() -> int:
    ap = argparse.ArgumentParser(description="Venture Factory approvals inbox")
    ap.add_argument("--expiring", action="store_true", help="only items expiring within 6h")
    ap.add_argument("--bulk-approve", metavar="ACTION_GLOB", help="approve all matching action_types")
    ap.add_argument("--bulk-reject", metavar="ACTION_GLOB", help="reject all matching action_types")
    ap.add_argument("--reason", help="rejection reason (required with --bulk-reject)")
    args = ap.parse_args()

    items = _pending()

    if args.expiring:
        items = [it for it in items
                 if it["hours_to_expiry"] is not None and it["hours_to_expiry"] < EXPIRING_WINDOW_H]

    if args.bulk_approve:
        return _bulk(items, args.bulk_approve, None)
    if args.bulk_reject:
        if not args.reason:
            print("ERROR: --bulk-reject requires --reason", file=sys.stderr)
            return 1
        return _bulk(items, args.bulk_reject, args.reason)

    if args.expiring:
        print(f"Approvals expiring within {EXPIRING_WINDOW_H}h:")
    _print_table(items)
    return 0


if __name__ == "__main__":
    sys.exit(main())
