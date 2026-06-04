#!/usr/bin/env python3
"""Thin entry point so `uv run brief` runs scripts/morning_brief.sh."""
import subprocess
import sys
from pathlib import Path


def main() -> int:
    sh = Path(__file__).parent / "morning_brief.sh"
    return subprocess.call(["bash", str(sh)])


if __name__ == "__main__":
    sys.exit(main())
