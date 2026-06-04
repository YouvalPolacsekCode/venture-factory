#!/usr/bin/env python3
"""
LIVE end-to-end smoke test for the Venture Factory (Phase 1).

Runs the discovery+scoring core against ONE constrained HN source and the real
Anthropic API:

    market_radar -> opportunity_scoring -> daily_summary

Asserts:
1. >=1 opportunities/<id>.opportunity.json written and schema-valid.
2. >=1 opportunities/<id>.scoring.json written.
3. >=1 reports/daily/<today>.md written.
4. This run's spend (delta in spend_ledger) < $0.20.

Exit 0 on pass, non-zero on any failure. Requires ANTHROPIC_API_KEY in .env.
"""
import json
import os
import sqlite3
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent.resolve()
DB_PATH = REPO_ROOT / "factory" / "state.db"
SMOKE_SOURCES = "config/fixtures/smoke_sources.yaml"
SPEND_BUDGET_USD = 0.20


def _idt_date() -> str:
    return datetime.now(timezone(timedelta(hours=3))).strftime("%Y-%m-%d")


def _fail(msg: str) -> None:
    print(f"FAIL: {msg}", file=sys.stderr)
    sys.exit(1)


def _today_spend() -> float:
    if not DB_PATH.exists():
        return 0.0
    conn = sqlite3.connect(DB_PATH)
    try:
        row = conn.execute(
            "SELECT COALESCE(SUM(cost_usd), 0.0) FROM spend_ledger WHERE date=?",
            (_idt_date(),),
        ).fetchone()
        return float(row[0])
    finally:
        conn.close()


def _run(agent: str, env: dict) -> None:
    print(f"--- running {agent} (live) ---")
    result = subprocess.run(
        [sys.executable, str(REPO_ROOT / "scripts" / "run_agent.py"), "--agent", agent],
        cwd=REPO_ROOT, env=env, capture_output=True, text=True,
    )
    if result.stdout:
        print(result.stdout, end="")
    if result.stderr:
        print(result.stderr, end="", file=sys.stderr)
    if result.returncode != 0:
        _fail(f"{agent} exited with code {result.returncode}")


def main() -> int:
    print("=== Venture Factory LIVE smoke test ===")

    if not os.environ.get("ANTHROPIC_API_KEY") and not (REPO_ROOT / ".env").exists():
        _fail("ANTHROPIC_API_KEY required; see .env.example")

    env = os.environ.copy()
    env["MARKET_RADAR_SOURCES"] = SMOKE_SOURCES

    spend_before = _today_spend()

    _run("market_radar", env)
    _run("opportunity_scoring", env)
    _run("daily_summary", env)

    # 1. Opportunity files + schema validation.
    opp_dir = REPO_ROOT / "opportunities"
    opportunities = sorted(opp_dir.glob("*.opportunity.json"))
    if not opportunities:
        _fail("No *.opportunity.json files written by market_radar")

    try:
        import jsonschema
    except ImportError:
        _fail("jsonschema not installed — run `uv sync` first")
    schema = json.loads((REPO_ROOT / "templates" / "opportunity.schema.json").read_text())
    for opp_file in opportunities:
        try:
            opp = json.loads(opp_file.read_text())
        except json.JSONDecodeError as exc:
            _fail(f"{opp_file.name} is not valid JSON: {exc}")
        try:
            jsonschema.validate(instance=opp, schema=schema)
        except jsonschema.ValidationError as exc:
            _fail(f"{opp_file.name} failed schema validation: {exc.message}")
    print(f"  OK: {len(opportunities)} opportunity file(s) schema-valid")

    # 2. Scoring files.
    scoring = sorted(opp_dir.glob("*.scoring.json"))
    if not scoring:
        _fail("No *.scoring.json files written by opportunity_scoring")
    print(f"  OK: {len(scoring)} scoring file(s)")

    # 3. Daily report.
    reports = list((REPO_ROOT / "reports" / "daily").glob(f"{_idt_date()}*.md"))
    if not reports:
        _fail(f"No reports/daily/{_idt_date()}*.md written by daily_summary")
    print(f"  OK: {len(reports)} daily report(s)")

    # 4. Spend budget (delta for this run).
    spend_delta = _today_spend() - spend_before
    if spend_delta >= SPEND_BUDGET_USD:
        _fail(f"This run spent ${spend_delta:.4f} >= ${SPEND_BUDGET_USD} budget")
    print(f"  OK: run spend ${spend_delta:.4f} < ${SPEND_BUDGET_USD}")

    print(f"\nPASS: {len(opportunities)} opportunity, {len(scoring)} scoring, "
          f"{len(reports)} report; spend ${spend_delta:.4f}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
