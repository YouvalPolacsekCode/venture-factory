#!/usr/bin/env python3
"""
Safety suite (Phase 3). Verifies the factory cannot blow the budget or leak the
key, and that it runs 24/7 (no read-only window).

Run with `uv run safety` (wraps pytest) or `uv run python -m pytest scripts/test_safety.py`.

None of these tests make a live Anthropic API call: the spend/key/policy guards
all short-circuit before any network or API request.
"""
import json
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(REPO_ROOT / "scripts"))

RUN_AGENT = REPO_ROOT / "scripts" / "run_agent.py"
RUN_LOOP = REPO_ROOT / "scripts" / "run_daily_loop.py"
POLICY = REPO_ROOT / "config" / "approval_policy.yaml"
APPROVAL_DIR = REPO_ROOT / "approval_queue"


def _idt_date() -> str:
    return datetime.now(timezone(timedelta(hours=3))).strftime("%Y-%m-%d")


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def test_missing_key():
    """Blank ANTHROPIC_API_KEY -> run_agent.py exits 1 with the fail-closed message."""
    import os
    env = os.environ.copy()
    env["ANTHROPIC_API_KEY"] = ""  # present-but-empty so load_dotenv won't override it
    r = subprocess.run([sys.executable, str(RUN_AGENT), "--agent", "market_radar"],
                       cwd=REPO_ROOT, env=env, capture_output=True, text=True)
    assert r.returncode == 1, r.stderr
    assert "ANTHROPIC_API_KEY required; see .env.example" in r.stderr


def test_spend_cap():
    """Seed spend_ledger above the cap, run market_radar, assert a
    spend_above_daily_cap approval is queued and NO API call was made."""
    import os
    import db

    db.apply_migrations()
    seed_id = "test-spendcap-row"
    conn = db.get_connection()
    conn.execute("DELETE FROM spend_ledger WHERE id=?", (seed_id,))
    conn.execute(
        "INSERT INTO spend_ledger (id, agent, date, cost_usd, run_id, created_at) "
        "VALUES (?,?,?,?,?,?)",
        (seed_id, "test", _idt_date(), 1000.0, "test", _utc_now()),
    )
    conn.commit()
    conn.close()

    before = {p.name for p in APPROVAL_DIR.glob("*.json")} if APPROVAL_DIR.exists() else set()
    marker = _utc_now()
    new_files: list[Path] = []
    try:
        env = os.environ.copy()  # real key from .env stays available
        r = subprocess.run([sys.executable, str(RUN_AGENT), "--agent", "market_radar"],
                           cwd=REPO_ROOT, env=env, capture_output=True, text=True)
        assert r.returncode == 0, r.stderr

        after = {p.name for p in APPROVAL_DIR.glob("*.json")}
        new_files = [APPROVAL_DIR / n for n in (after - before)]
        action_types = []
        for f in new_files:
            try:
                action_types.append(json.loads(f.read_text()).get("action_type"))
            except Exception:
                pass
        assert "spend_above_daily_cap" in action_types, f"approvals seen: {action_types}"

        # No API call: no market_radar spend rows recorded after the marker.
        conn = db.get_connection()
        n = conn.execute(
            "SELECT COUNT(*) FROM spend_ledger WHERE agent='market_radar' AND created_at >= ?",
            (marker,),
        ).fetchone()[0]
        conn.close()
        assert n == 0, f"expected no market_radar API spend, found {n} rows"
    finally:
        conn = db.get_connection()
        conn.execute("DELETE FROM spend_ledger WHERE id=?", (seed_id,))
        conn.commit()
        conn.close()
        for f in new_files:
            f.unlink(missing_ok=True)


def test_runs_24_7_no_shabbat_window():
    """The factory runs 24/7: there is no read-only / time-of-week gating left in
    the loop (the old Shabbat window was removed)."""
    import run_daily_loop as loop

    assert not hasattr(loop, "_is_shabbat_window")
    assert not hasattr(loop, "_shabbat_blocks")
    assert not hasattr(loop, "SHABBAT_BLOCKED_ACTIONS")


def test_build_now_requires_scoring_gate():
    """build_decisions may NOT promote an idea to build_now if it fails the
    scoring-v2 build_gates — the runner downgrades to defer_1_week in code and
    queues NO promote_to_build approval, even when the LLM said build_now."""
    import run_agent as R

    opp = REPO_ROOT / "opportunities"
    pid = "01TESTSAFEPASS000000000000"
    fid = "01TESTSAFEFAIL000000000000"
    (opp / f"{pid}.scoring.json").write_text(json.dumps({
        "opportunity_id": pid, "total": 7.0, "recommended_stage": "build",
        "per_dimension": {"operational_autonomy": 8, "buildability_with_ai": 7,
                          "buyer_clarity": 7, "willingness_to_pay": 6}}))
    (opp / f"{fid}.scoring.json").write_text(json.dumps({
        "opportunity_id": fid, "total": 7.0, "recommended_stage": "build",
        "per_dimension": {"operational_autonomy": 5, "buildability_with_ai": 7,
                          "buyer_clarity": 7, "willingness_to_pay": 6}}))
    arr = [
        {"opportunity_id": pid, "decision": "build_now", "confidence_pct": 80,
         "proposed_slug": "safe-pass", "why_now_memo": "x"},
        {"opportunity_id": fid, "decision": "build_now", "confidence_pct": 80,
         "proposed_slug": "safe-fail", "why_now_memo": "x"},
    ]
    text = "```json\n" + json.dumps(arr) + "\n```"
    appr: list = []
    created = []
    try:
        R._process_build_decisions(text, [], appr)
        pdec = json.loads((opp / f"{pid}.build_decision.json").read_text())
        fdec = json.loads((opp / f"{fid}.build_decision.json").read_text())
        assert pdec["decision"] == "build_now", "idea clearing gates may build_now"
        assert fdec["decision"] == "defer_1_week", "idea failing a gate MUST be downgraded"
        # Exactly one promote_to_build approval, for the passing idea only.
        promos = []
        for a in appr:
            p = APPROVAL_DIR / f"{a}.json"
            created.append(p)
            obj = json.loads(p.read_text())
            if obj.get("action_type") == "promote_to_build":
                promos.append(obj["payload"]["opportunity_id"])
        assert promos == [pid], f"only the gate-passing idea queues promote_to_build, got {promos}"
    finally:
        for x in (pid, fid):
            (opp / f"{x}.scoring.json").unlink(missing_ok=True)
            (opp / f"{x}.build_decision.json").unlink(missing_ok=True)
        for p in created:
            p.unlink(missing_ok=True)


def test_policy_unreadable():
    """Missing approval_policy.yaml -> run_daily_loop.py fails closed (exit 1)."""
    backup = POLICY.with_name("approval_policy.yaml.bak")
    POLICY.rename(backup)
    try:
        r = subprocess.run([sys.executable, str(RUN_LOOP)], cwd=REPO_ROOT,
                           capture_output=True, text=True)
        assert r.returncode == 1, r.stdout + r.stderr
        assert "fail-closed: approval policy unreadable" in r.stderr
    finally:
        backup.rename(POLICY)


def _run():
    """Entry point for `uv run safety`."""
    import pytest
    raise SystemExit(pytest.main(["-q", str(Path(__file__).resolve())]))


if __name__ == "__main__":
    _run()
