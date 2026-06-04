#!/usr/bin/env python3
"""
Cost report for the Venture Factory.

Prints spend grouped by agent, separating standard input / cache-write /
cache-read input tokens and output tokens, plus actual USD spent vs the
per-day external-API cap from config/approval_policy.yaml.

Usage:
  cost_report.py                 # today (IDT)
  cost_report.py --since DATE    # from DATE (YYYY-MM-DD) through today, inclusive
"""
import argparse
import sqlite3
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).parent.parent.resolve()
DB_PATH = REPO_ROOT / "factory" / "state.db"


def _idt_date() -> str:
    return datetime.now(timezone(timedelta(hours=3))).strftime("%Y-%m-%d")


def _daily_cap() -> float:
    p = REPO_ROOT / "config" / "approval_policy.yaml"
    try:
        pol = yaml.safe_load(p.read_text()) or {}
        return float(pol.get("caps", {}).get("per_day_external_api_usd", 25.0))
    except Exception:
        return 25.0


def main() -> int:
    ap = argparse.ArgumentParser(description="Venture Factory cost report")
    ap.add_argument("--since", help="Start date YYYY-MM-DD (inclusive). Defaults to today.")
    args = ap.parse_args()

    today = _idt_date()
    since = args.since or today

    if not DB_PATH.exists():
        print("No state.db yet — nothing to report.")
        return 0

    conn = sqlite3.connect(DB_PATH)
    rows = conn.execute(
        """SELECT agent,
                  COUNT(*) AS calls,
                  COALESCE(SUM(tokens_in), 0),
                  COALESCE(SUM(cache_creation_input_tokens), 0),
                  COALESCE(SUM(cache_read_input_tokens), 0),
                  COALESCE(SUM(tokens_out), 0),
                  COALESCE(SUM(cost_usd), 0.0)
           FROM spend_ledger
           WHERE date >= ? AND date <= ?
           GROUP BY agent
           ORDER BY SUM(cost_usd) DESC""",
        (since, today),
    ).fetchall()
    conn.close()

    span = today if since == today else f"{since} .. {today}"
    print(f"=== Cost report ({span}, IDT) ===")
    if not rows:
        print("No spend recorded in this range.")
        return 0

    header = f"{'agent':<22}{'calls':>6}{'std_in':>10}{'cache_wr':>10}{'cache_rd':>10}{'out':>9}{'USD':>10}"
    print(header)
    print("-" * len(header))
    tot = [0, 0, 0, 0, 0, 0.0]
    for agent, calls, std_in, cwr, crd, out, cost in rows:
        print(f"{agent:<22}{calls:>6}{std_in:>10}{cwr:>10}{crd:>10}{out:>9}{cost:>10.4f}")
        tot = [tot[0] + calls, tot[1] + std_in, tot[2] + cwr, tot[3] + crd, tot[4] + out, tot[5] + cost]
    print("-" * len(header))
    print(f"{'TOTAL':<22}{tot[0]:>6}{tot[1]:>10}{tot[2]:>10}{tot[3]:>10}{tot[4]:>9}{tot[5]:>10.4f}")

    cap = _daily_cap()
    if since == today:
        pct = (tot[5] / cap * 100) if cap else 0
        print(f"\nToday: ${tot[5]:.4f} spent of ${cap:.2f} per-day cap ({pct:.1f}%).")
    else:
        print(f"\nNote: per-day cap is ${cap:.2f}; range total above spans multiple days.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
