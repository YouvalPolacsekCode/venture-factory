"""Shared prefilter helpers for source fetchers (Phase 1.5).

Drops low-signal items before they reach the LLM:
- deleted/removed bodies
- known-bot authors
- items below an upvote/score threshold
- URLs already seen (opportunities/_seen.jsonl)
And truncates body_text to keep prompt size (and cost) bounded.
"""
import html
import json
import re
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
SEEN_LEDGER = REPO_ROOT / "opportunities" / "_seen.jsonl"

BODY_TRUNC = 500

_TAG_RE = re.compile(r"<[^>]+>")
_WS_RE = re.compile(r"\s+")

# Known-bot author patterns (case-insensitive substring / suffix matches).
BOT_PATTERNS = [
    re.compile(r"bot$", re.IGNORECASE),
    re.compile(r"^auto", re.IGNORECASE),
    re.compile(r"automoderator", re.IGNORECASE),
    re.compile(r"-bot", re.IGNORECASE),
    re.compile(r"_bot", re.IGNORECASE),
]


def load_seen_urls() -> set[str]:
    seen: set[str] = set()
    if SEEN_LEDGER.exists():
        for line in SEEN_LEDGER.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            try:
                url = json.loads(line).get("url")
            except json.JSONDecodeError:
                continue
            if url:
                seen.add(url)
    return seen


def is_bot(author: str) -> bool:
    a = (author or "").strip()
    return any(p.search(a) for p in BOT_PATTERNS)


def is_deleted(body: str) -> bool:
    b = (body or "").strip().lower()
    return b in ("[deleted]", "[removed]", "")


def truncate_body(body: str) -> str:
    return (body or "")[:BODY_TRUNC]


def strip_html(text: str) -> str:
    """Flatten HTML/markdown-ish body to plain text (StackExchange / GitHub
    bodies arrive as HTML or Markdown). Best-effort, stdlib-only."""
    if not text:
        return ""
    return _WS_RE.sub(" ", html.unescape(_TAG_RE.sub(" ", text))).strip()


def epoch_to_iso(epoch) -> str:
    """Unix seconds (StackExchange `creation_date`) -> ISO-8601 UTC string."""
    try:
        return datetime.fromtimestamp(int(epoch), tz=timezone.utc).isoformat()
    except (TypeError, ValueError, OSError):
        return ""
