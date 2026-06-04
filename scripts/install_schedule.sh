#!/usr/bin/env bash
#
# Idempotent installer for the Venture Factory daily-loop launchd agent.
# Resolves the absolute uv path, translates 06:00 Asia/Jerusalem to the local
# clock, fills the plist template, and (re)loads it into launchd.
#
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LABEL="com.youval.venturefactory.daily"
TEMPLATE="$REPO/scripts/$LABEL.plist"
AGENTS_DIR="$HOME/Library/LaunchAgents"
TARGET="$AGENTS_DIR/$LABEL.plist"

# 1. Resolve uv.
UV="$(command -v uv || true)"
if [ -z "$UV" ]; then
    echo "ERROR: uv not found on PATH. Install uv and re-run." >&2
    exit 1
fi

# 2. Translate 06:00 Asia/Jerusalem to the local wall clock (DST-aware, at install time).
read -r HOUR MINUTE <<EOF
$(python3 - <<'PY'
from datetime import datetime
from zoneinfo import ZoneInfo
now = datetime.now(ZoneInfo("Asia/Jerusalem"))
target = now.replace(hour=6, minute=0, second=0, microsecond=0)
local = target.astimezone()
print(local.hour, local.minute)
PY
)
EOF

# 3. Ensure dirs exist.
mkdir -p "$AGENTS_DIR"
mkdir -p "$REPO/logs/launchd"

OUT="$REPO/logs/launchd/daily.out.log"
ERR="$REPO/logs/launchd/daily.err.log"
LAUNCH_PATH="$(dirname "$UV"):/usr/local/bin:/usr/bin:/bin"

# 4. Fill the template.
sed -e "s|__UV__|$UV|g" \
    -e "s|__WORKDIR__|$REPO|g" \
    -e "s|__HOUR__|$HOUR|g" \
    -e "s|__MINUTE__|$MINUTE|g" \
    -e "s|__OUT__|$OUT|g" \
    -e "s|__ERR__|$ERR|g" \
    -e "s|__PATH__|$LAUNCH_PATH|g" \
    "$TEMPLATE" > "$TARGET"

# 5. Reload idempotently.
launchctl unload "$TARGET" 2>/dev/null || true
launchctl load -w "$TARGET"

echo "Installed $TARGET"
echo "Scheduled daily at local ${HOUR}:$(printf '%02d' "$MINUTE") (= 06:00 Asia/Jerusalem at install time)."
echo "Status:"
launchctl list | grep venturefactory || echo "  (not yet listed — give launchd a moment)"
