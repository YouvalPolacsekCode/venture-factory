#!/usr/bin/env bash
# Run from a normal shell at the repo root (NOT inside the Cowork mount).
# Resets a partially-initialized .git and starts fresh.
# Usage: bash scripts/setup_git.sh

set -euo pipefail

repo="$(pwd)"
echo "Resetting git at $repo"

rm -rf .git
git init -b main
git config user.email "silentyouval@gmail.com"
git config user.name "Youval"
git add -A
git commit -m "Phase 0: scaffold AI Venture Factory MVP"

echo "Git initialized and Phase 0 committed."
git log --oneline | head -3
