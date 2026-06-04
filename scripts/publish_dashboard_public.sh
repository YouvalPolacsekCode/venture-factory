#!/usr/bin/env bash
# Free fallback publisher: push ONLY the sanitized dashboard/ folder to a
# SEPARATE PUBLIC repo whose GitHub Pages is free (private-repo Pages needs a
# paid plan). The public mirror contains index.html + data.json only — no
# source code, no secrets, no raw PII (the export is already sanitized).
#
# One-time setup
#   1. Create a public repo, e.g.:  gh repo create <you>/venture-factory-dashboard --public
#   2. Enable Pages on it: Settings -> Pages -> Source: "Deploy from a branch",
#      branch = main, folder = / (root).  (Or push to a `gh-pages` branch.)
#   3. Either have `gh` authenticated, or set MIRROR_REMOTE to an authenticated
#      URL (HTTPS with a PAT, or SSH).
#
# Usage
#   scripts/publish_dashboard_public.sh <you>/venture-factory-dashboard
#   # or, with an explicit remote URL:
#   MIRROR_REMOTE=git@github.com:you/venture-factory-dashboard.git \
#       scripts/publish_dashboard_public.sh
#
# This script is read-only over the main repo: it copies dashboard/ into a temp
# clone of the mirror and pushes. It never touches this repo's git history.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DASH_DIR="$REPO_ROOT/dashboard"

if [[ ! -f "$DASH_DIR/index.html" || ! -f "$DASH_DIR/data.json" ]]; then
  echo "ERROR: $DASH_DIR/{index.html,data.json} not found. Run 'uv run build-dashboard' first." >&2
  exit 1
fi

# Resolve the mirror remote URL.
TARGET="${1:-}"
if [[ -n "${MIRROR_REMOTE:-}" ]]; then
  REMOTE="$MIRROR_REMOTE"
elif [[ -n "$TARGET" ]]; then
  REMOTE="https://github.com/${TARGET}.git"
else
  echo "ERROR: pass <owner>/<repo> or set MIRROR_REMOTE." >&2
  echo "  e.g. scripts/publish_dashboard_public.sh you/venture-factory-dashboard" >&2
  exit 1
fi

BRANCH="${MIRROR_BRANCH:-main}"

# Sanitization backstop before anything leaves the machine: refuse to publish if
# the export trips the exporter's own self-check.
echo "Re-verifying export is clean..."
uv run build-dashboard >/dev/null

TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

echo "Cloning mirror $REMOTE (branch $BRANCH)..."
if ! git clone --depth 1 --branch "$BRANCH" "$REMOTE" "$TMP/mirror" 2>/dev/null; then
  # Fresh/empty repo: init and set the remote.
  git init -q "$TMP/mirror"
  git -C "$TMP/mirror" remote add origin "$REMOTE"
  git -C "$TMP/mirror" checkout -q -b "$BRANCH"
fi

cp "$DASH_DIR/index.html" "$TMP/mirror/index.html"
cp "$DASH_DIR/data.json"  "$TMP/mirror/data.json"
# Disable Jekyll so files with leading underscores publish verbatim.
touch "$TMP/mirror/.nojekyll"

git -C "$TMP/mirror" add index.html data.json .nojekyll
if git -C "$TMP/mirror" diff --cached --quiet; then
  echo "No changes to publish."
  exit 0
fi

git -C "$TMP/mirror" -c user.name="venture-factory-bot" \
    -c user.email="actions@github.com" \
    commit -q -m "dashboard: publish $(date -u +%Y-%m-%dT%H:%MZ)"
git -C "$TMP/mirror" push -u origin "$BRANCH"

OWNER_REPO="$(echo "$REMOTE" | sed -E 's#.*[/:]([^/]+/[^/]+)\.git#\1#')"
OWNER="${OWNER_REPO%%/*}"
NAME="${OWNER_REPO##*/}"
echo "Published. Pages URL (once enabled): https://${OWNER}.github.io/${NAME}/"
