#!/usr/bin/env python3
"""
Execute an approved action.

Usage: execute_action.py <ulid>

Dispatches on action_type. In Phase 0 every action_type writes a
simulated_execution.json next to the approved file and logs it.

Extension point: add a real adapter function to ADAPTERS below and
remove the TODO comment for that action_type.
"""
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


# ---------------------------------------------------------------------------
# Adapters
# Each adapter receives (request_dict, approved_dict) and returns a result dict.
# Phase 0: all adapters are stubs that write simulated_execution.json.
# ---------------------------------------------------------------------------

def _stub_adapter(request: dict, approved: dict) -> dict:
    """Phase 0 stub — simulates execution without calling any external service."""
    action_type = request.get("action_type", "unknown")
    return {
        "simulated": True,
        "action_type": action_type,
        "note": (
            f"Phase 0 stub. Real adapter for '{action_type}' not yet implemented. "
            "Replace this function in ADAPTERS when ready."
        ),
        "executed_at": _idt_now().isoformat(),
    }


def _promote_to_build_adapter(request: dict, approved: dict) -> dict:
    """P4.3 — an approved promote_to_build scaffolds the service (internal-only,
    no external call). Idempotent: a slug already built is skipped."""
    import service_builder
    payload = approved.get("payload") or request.get("payload") or {}
    oid = payload.get("opportunity_id")
    slug = (payload.get("proposed_slug") or "").strip().lower()
    approved_at = approved.get("operator_ts")
    if not oid or not slug:
        return {"ok": False, "reason": "missing opportunity_id/proposed_slug in approval payload"}
    res = service_builder.scaffold_service(
        oid, slug, approved_at, payload.get("confidence_pct"), payload.get("why_now_memo", ""))
    return res


# TODO: replace each stub with a real adapter when the relevant service is wired up.
# Adapter signature: (request: dict, approved: dict) -> dict
ADAPTERS: dict[str, callable] = {
    # Outreach — TODO: wire Resend API (see services/resend_adapter.py when created)
    "send_outreach_email": _stub_adapter,
    "send_outreach_sms":   _stub_adapter,
    "send_outreach_dm":    _stub_adapter,

    # Hosting — TODO: wire `wrangler pages deploy` (see scripts/adapters/cloudflare.py)
    "publish_landing_page":   _stub_adapter,
    "deploy_public_domain":   _stub_adapter,

    # Payments — TODO: wire Stripe API (see scripts/adapters/stripe.py)
    "create_payment_link": _stub_adapter,
    "charge_customer":     _stub_adapter,
    "refund_customer":     _stub_adapter,

    # Customer comms — TODO: wire send channel
    "send_customer_message": _stub_adapter,

    # Accounts
    "register_external_account": _stub_adapter,

    # Destructive
    "delete_repo_file": _stub_adapter,

    # Cap overrides
    "spend_above_daily_cap":   _stub_adapter,
    "call_paid_api_above_cap": _stub_adapter,

    # Build promotion — scaffolds the service folder (internal-only).
    "promote_to_build": _promote_to_build_adapter,
}

_DEFAULT_ADAPTER = _stub_adapter


def _emit_execution_log(ulid: str, action_type: str, result: dict, ok: bool) -> None:
    log_dir = REPO_ROOT / "logs" / "runs" / _idt_date()
    log_dir.mkdir(parents=True, exist_ok=True)
    with open(log_dir / "execute_action.jsonl", "a", encoding="utf-8") as fh:
        fh.write(json.dumps({
            "schema_version": 1,
            "event_id": _new_ulid(),
            "agent": "execute_action",
            "action_type": action_type,
            "status": "succeeded" if ok else "failed",
            "approval_ulid": ulid,
            "result": result,
            "executed_at": _idt_now().isoformat(),
        }) + "\n")


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: execute_action.py <ulid>", file=sys.stderr)
        return 1

    ulid = sys.argv[1].strip()
    queue_dir = REPO_ROOT / "approval_queue"

    approved_path = queue_dir / f"{ulid}.approved.json"
    request_path = queue_dir / f"{ulid}.json"

    if not approved_path.exists():
        print(f"ERROR: {ulid}.approved.json not found — was approve.py run first?", file=sys.stderr)
        return 1

    if not request_path.exists():
        print(f"ERROR: {ulid}.json (original request) not found", file=sys.stderr)
        return 1

    try:
        request = json.loads(request_path.read_text(encoding="utf-8"))
        approved = json.loads(approved_path.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"ERROR: Could not parse approval files: {exc}", file=sys.stderr)
        return 1

    action_type = request.get("action_type", "unknown")
    adapter = ADAPTERS.get(action_type, _DEFAULT_ADAPTER)

    try:
        result = adapter(request, approved)
        ok = True
    except Exception as exc:
        result = {"error": str(exc)}
        ok = False
        print(f"ERROR: Adapter for '{action_type}' raised: {exc}", file=sys.stderr)

    # Write simulated_execution.json alongside the approved file
    sim_path = queue_dir / f"{ulid}.simulated_execution.json"
    sim_path.write_text(json.dumps({
        "ulid": ulid,
        "action_type": action_type,
        "executed_at": _idt_now().isoformat(),
        "ok": ok,
        "result": result,
    }, indent=2), encoding="utf-8")

    _emit_execution_log(ulid, action_type, result, ok)
    print(f"Executed ({action_type}): {ulid} — ok={ok}")

    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
