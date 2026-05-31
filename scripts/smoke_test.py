#!/usr/bin/env python3
"""
Smoke test for the Venture Factory agent runner.

Runs market_radar in dry-run mode against the fixture, then asserts:
1. At least one opportunities/<ulid>.json was written.
2. That file validates against templates/opportunity.schema.json.
3. At least one log line exists in logs/runs/<date>/market_radar.jsonl.

Exit 0 on pass, non-zero on any failure.
"""
import json
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent.resolve()
FIXTURE = "config/fixtures/market_radar_fixture.json"


def _idt_date() -> str:
    return datetime.now(timezone(timedelta(hours=3))).strftime("%Y-%m-%d")


def _fail(msg: str) -> None:
    print(f"FAIL: {msg}", file=sys.stderr)
    sys.exit(1)


def main() -> int:
    print("=== Venture Factory smoke test ===")

    # 1. Invoke the runner
    cmd = [
        sys.executable,
        str(REPO_ROOT / "scripts" / "run_agent.py"),
        "--agent", "market_radar",
        "--input", FIXTURE,
        "--dry-run",
    ]
    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, cwd=REPO_ROOT, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout, end="")
    if result.stderr:
        print(result.stderr, end="", file=sys.stderr)

    if result.returncode != 0:
        _fail(f"run_agent.py exited with code {result.returncode}")

    # 2. Assert opportunity files
    opp_dir = REPO_ROOT / "opportunities"
    opportunities = sorted(opp_dir.glob("*.json")) if opp_dir.exists() else []
    if not opportunities:
        _fail("No *.json files found in opportunities/")

    # 3. Validate against schema
    schema_path = REPO_ROOT / "templates" / "opportunity.schema.json"
    if not schema_path.exists():
        _fail(f"Schema not found: {schema_path}")

    try:
        import jsonschema
    except ImportError:
        _fail("jsonschema not installed — run `uv sync` first")

    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    for opp_file in opportunities:
        try:
            opp = json.loads(opp_file.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            _fail(f"{opp_file.name} is not valid JSON: {exc}")

        try:
            jsonschema.validate(instance=opp, schema=schema)
        except jsonschema.ValidationError as exc:
            _fail(f"{opp_file.name} failed schema validation: {exc.message}")

        print(f"  OK: {opp_file.name} passes schema validation")

    # 4. Assert log line
    log_file = REPO_ROOT / "logs" / "runs" / _idt_date() / "market_radar.jsonl"
    if not log_file.exists():
        _fail(f"Log file not found: {log_file.relative_to(REPO_ROOT)}")

    lines = [ln for ln in log_file.read_text(encoding="utf-8").splitlines() if ln.strip()]
    if not lines:
        _fail("Log file exists but contains no lines")

    # Verify the log line is valid JSON with required fields
    try:
        log_entry = json.loads(lines[-1])
    except json.JSONDecodeError as exc:
        _fail(f"Last log line is not valid JSON: {exc}")

    for field in ("schema_version", "event_id", "agent", "status"):
        if field not in log_entry:
            _fail(f"Log entry missing required field '{field}'")

    print(f"  OK: {len(lines)} log line(s) in {log_file.relative_to(REPO_ROOT)}")
    print(f"\nPASS: {len(opportunities)} opportunity file(s) written and validated, "
          f"{len(lines)} log line(s) found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
