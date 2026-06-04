#!/usr/bin/env python3
"""
LIVE end-to-end smoke test for the Venture Factory (Phase 1.5).

Runs the discovery+scoring core against ONE constrained HN source and the real
Anthropic API:

    market_radar -> opportunity_scoring -> daily_summary

opportunity_scoring is forced to batch_size=1 (SMOKE_FORCE_BATCH_SIZE) so that,
when there are >=2 fresh opportunities, the second+ scoring calls reuse the
cached system prompt — proving prompt caching is active.

Asserts:
1. >=1 opportunities/<id>.opportunity.json written and schema-valid.
2. >=1 opportunities/<id>.scoring.json written.
3. >=1 reports/daily/<today>.md written.
4. This run's spend (delta in spend_ledger) < $0.20.
5. If >=2 scoring batches ran, their cached system prompt produced
   cache_read_input_tokens > 0 (cache hit).
6. Cost-baseline regression: first run records the baseline; later runs must
   not exceed it.

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


def _conn() -> sqlite3.Connection:
    return sqlite3.connect(DB_PATH)


def _today_spend() -> float:
    if not DB_PATH.exists():
        return 0.0
    c = _conn()
    try:
        return float(c.execute("SELECT COALESCE(SUM(cost_usd),0.0) FROM spend_ledger WHERE date=?",
                               (_idt_date(),)).fetchone()[0])
    finally:
        c.close()


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
    print("=== Venture Factory LIVE smoke test (P1.5) ===")

    if not os.environ.get("ANTHROPIC_API_KEY") and not (REPO_ROOT / ".env").exists():
        _fail("ANTHROPIC_API_KEY required; see .env.example")

    env = os.environ.copy()
    env["MARKET_RADAR_SOURCES"] = SMOKE_SOURCES
    env["SMOKE_FORCE_BATCH_SIZE"] = "1"

    spend_before = _today_spend()
    marker = datetime.now(timezone.utc).isoformat()

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

    # 4. Spend budget (this run's delta).
    spend_delta = _today_spend() - spend_before
    if spend_delta >= SPEND_BUDGET_USD:
        _fail(f"This run spent ${spend_delta:.4f} >= ${SPEND_BUDGET_USD} budget")
    print(f"  OK: run spend ${spend_delta:.4f} < ${SPEND_BUDGET_USD}")

    # 5. Cache-hit assertion (only meaningful when >=2 scoring batches ran).
    c = _conn()
    n_calls, cache_read, cache_write = c.execute(
        "SELECT COUNT(*), COALESCE(SUM(cache_read_input_tokens),0), "
        "COALESCE(SUM(cache_creation_input_tokens),0) "
        "FROM spend_ledger WHERE agent='opportunity_scoring' AND created_at >= ?",
        (marker,),
    ).fetchone()
    if n_calls >= 2:
        if cache_read <= 0:
            _fail(f"opportunity_scoring ran {n_calls} batches but cache_read_input_tokens=0 "
                  f"(prompt caching not engaged; cache_write={cache_write})")
        print(f"  OK: cache hit — {n_calls} scoring batches, cache_read={cache_read} tokens "
              f"(cache_write={cache_write})")
    else:
        print(f"  NOTE: cache assertion skipped — only {n_calls} scoring batch this run "
              f"(need >=2 fresh opportunities). cache_write={cache_write}.")

    # 6. Cost baseline regression.
    row = c.execute("SELECT value FROM smoke_baseline WHERE metric='smoke_run_usd'").fetchone()
    if row is None:
        c.execute("INSERT INTO smoke_baseline (metric, value, recorded_at) VALUES (?,?,?)",
                  ("smoke_run_usd", spend_delta, marker))
        c.commit()
        print(f"  OK: baseline recorded (smoke_run_usd=${spend_delta:.4f})")
    else:
        baseline = float(row[0])
        if spend_delta > baseline + 1e-6:
            c.close()
            _fail(f"cost regression: run ${spend_delta:.4f} > baseline ${baseline:.4f}")
        print(f"  OK: within baseline (run ${spend_delta:.4f} <= baseline ${baseline:.4f})")
    c.close()

    print(f"\nPASS: {len(opportunities)} opportunity, {len(scoring)} scoring, "
          f"{len(reports)} report; spend ${spend_delta:.4f}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
