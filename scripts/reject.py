#!/usr/bin/env python3
"""
Reject a queued action.

Usage: reject.py <ulid> --reason "<text>"

Writes approval_queue/<ulid>.rejected.json and appends to
logs/denied/<date>.jsonl.
"""
import argparse
import json
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(REPO_ROOT / "scripts"))


def _idt_now() -> datetime:
    return datetime.now(timezone(timedelta(hours=3)))


def _idt_date() -> str:
    return _idt_now().strftime("%Y-%m-%d")


def _new_ulid() -> str:
    from ulid import ULID
    return str(ULID())


def main() -> int:
    ap = argparse.ArgumentParser(description="Reject a queued approval request")
    ap.add_argument("ulid", help="ULID of the approval request")
    ap.add_argument("--reason", required=True, help="Human-readable rejection reason")
    args = ap.parse_args()

    ulid = args.ulid.strip()
    reason = args.reason

    queue_dir = REPO_ROOT / "approval_queue"
    request_path = queue_dir / f"{ulid}.json"

    if not request_path.exists():
        print(f"ERROR: approval_queue/{ulid}.json not found", file=sys.stderr)
        return 1

    if (queue_dir / f"{ulid}.approved.json").exists():
        print(f"ERROR: {ulid} is already approved; cannot reject", file=sys.stderr)
        return 1

    if (queue_dir / f"{ulid}.rejected.json").exists():
        print(f"WARN: {ulid} already rejected — overwriting", file=sys.stderr)

    try:
        request = json.loads(request_path.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"ERROR: Could not parse {ulid}.json: {exc}", file=sys.stderr)
        return 1

    now_ts = _idt_now().isoformat()
    rejected = {
        **request,
        "operator_ts": now_ts,
        "rejection_reason": reason,
        "rejection_event_id": _new_ulid(),
    }

    rejected_path = queue_dir / f"{ulid}.rejected.json"
    rejected_path.write_text(json.dumps(rejected, indent=2), encoding="utf-8")

    # Append to denied log
    denied_dir = REPO_ROOT / "logs" / "denied"
    denied_dir.mkdir(parents=True, exist_ok=True)
    denied_log = denied_dir / f"{_idt_date()}.jsonl"
    with open(denied_log, "a", encoding="utf-8") as fh:
        fh.write(json.dumps({
            "schema_version": 1,
            "event_id": _new_ulid(),
            "ulid": ulid,
            "action_type": request.get("action_type", "unknown"),
            "agent": request.get("agent", "unknown"),
            "reason": reason,
            "rejected_at": now_ts,
        }) + "\n")

    print(f"Rejected: {ulid} — {reason}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
