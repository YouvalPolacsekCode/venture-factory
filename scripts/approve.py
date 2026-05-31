#!/usr/bin/env python3
"""
Approve a queued action.

Usage: approve.py <ulid>

Validates approval_queue/<ulid>.json, writes
approval_queue/<ulid>.approved.json, then calls execute_action.py.
"""
import json
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(REPO_ROOT / "scripts"))


def _idt_now() -> datetime:
    return datetime.now(timezone(timedelta(hours=3)))


def _new_ulid() -> str:
    from ulid import ULID
    return str(ULID())


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: approve.py <ulid>", file=sys.stderr)
        return 1

    ulid = sys.argv[1].strip()
    queue_dir = REPO_ROOT / "approval_queue"
    request_path = queue_dir / f"{ulid}.json"

    if not request_path.exists():
        print(f"ERROR: approval_queue/{ulid}.json not found", file=sys.stderr)
        return 1

    if (queue_dir / f"{ulid}.approved.json").exists():
        print(f"WARN: {ulid} is already approved", file=sys.stderr)
        return 1

    if (queue_dir / f"{ulid}.rejected.json").exists():
        print(f"ERROR: {ulid} was already rejected", file=sys.stderr)
        return 1

    try:
        request = json.loads(request_path.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"ERROR: Could not parse {ulid}.json: {exc}", file=sys.stderr)
        return 1

    # Validate required fields
    for field in ("ulid", "action_type", "agent", "created_at"):
        if field not in request:
            print(f"ERROR: Approval request missing field '{field}'", file=sys.stderr)
            return 1

    if request["ulid"] != ulid:
        print(f"ERROR: ulid mismatch in file (got {request['ulid']!r})", file=sys.stderr)
        return 1

    approved = {
        **request,
        "operator_ts": _idt_now().isoformat(),
        "approval_event_id": _new_ulid(),
    }
    approved_path = queue_dir / f"{ulid}.approved.json"
    approved_path.write_text(json.dumps(approved, indent=2), encoding="utf-8")
    print(f"Approved: {ulid}")

    # Execute
    rc = subprocess.run(
        [sys.executable, str(REPO_ROOT / "scripts" / "execute_action.py"), ulid],
        cwd=REPO_ROOT,
    ).returncode

    if rc != 0:
        print(f"WARN: execute_action.py exited {rc} for {ulid}", file=sys.stderr)

    return rc


if __name__ == "__main__":
    sys.exit(main())
