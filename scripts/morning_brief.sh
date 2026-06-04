#!/usr/bin/env bash
#
# Operator morning brief (run ~08:30 IDT). Opens today's daily report and shows
# expiring approvals. Run directly (./scripts/morning_brief.sh) or via `uv run brief`.
#
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO"

TODAY="$(python3 -c "from datetime import datetime,timezone,timedelta; print(datetime.now(timezone(timedelta(hours=3))).strftime('%Y-%m-%d'))")"
YESTERDAY="$(python3 -c "from datetime import datetime,timezone,timedelta; print((datetime.now(timezone(timedelta(hours=3)))-timedelta(days=1)).strftime('%Y-%m-%d'))")"

REPORT="reports/daily/${TODAY}.md"
if [ ! -f "$REPORT" ]; then
    REPORT="reports/daily/${YESTERDAY}.md"
fi

if [ -f "$REPORT" ]; then
    echo "Opening $REPORT"
    open "$REPORT"
else
    echo "No daily report found for ${TODAY} or ${YESTERDAY} (has the loop run yet?)."
fi

echo
echo "=== Approvals expiring soon ==="
uv run python scripts/approvals_inbox.py --expiring

echo
echo "Full inbox: uv run python scripts/approvals_inbox.py"
