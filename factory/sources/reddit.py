"""Reddit source fetcher (public listing JSON). No auth; respects 429."""
import time
from datetime import datetime, timezone

import httpx

from . import _filters

_TIMEOUT = 20.0
_USER_AGENT = "venture-factory/0.1 by youval"
_MAX_RETRIES = 3
_MIN_SCORE = 2


def fetch(source_config: dict, stats: dict | None = None) -> list[dict]:
    """Fetch a public Reddit listing (e.g. new.json), normalize and prefilter.

    Returns [{url, title, author, captured_at, body_text, score, num_comments}].
    Populates `stats` with fetched / dropped_by_rule / kept counts when provided.
    Retries 429 with exponential backoff (max 3); returns [] on persistent error."""
    url = source_config.get("url_template") or source_config.get("url")
    if not url:
        return []

    data = None
    for attempt in range(_MAX_RETRIES):
        try:
            resp = httpx.get(url, headers={"User-Agent": _USER_AGENT}, timeout=_TIMEOUT)
            if resp.status_code == 429:
                time.sleep(2 ** attempt)  # 1s, 2s, 4s
                continue
            resp.raise_for_status()
            data = resp.json()
            break
        except (httpx.HTTPError, ValueError):
            if attempt == _MAX_RETRIES - 1:
                return []
            time.sleep(2 ** attempt)

    if not data:
        return []

    seen = _filters.load_seen_urls()
    children = data.get("data", {}).get("children", [])
    fetched = len(children)
    items: list[dict] = []
    for child in children:
        d = child.get("data", {})
        permalink = d.get("permalink", "")
        full_url = ("https://www.reddit.com" + permalink) if permalink else d.get("url", "")
        body = d.get("selftext") or d.get("title") or ""
        author = d.get("author", "")
        score = d.get("score") or 0

        if full_url in seen:
            continue
        if _filters.is_deleted(body):
            continue
        if _filters.is_bot(author):
            continue
        if score < _MIN_SCORE:
            continue

        created = d.get("created_utc")
        captured_at = (
            datetime.fromtimestamp(created, tz=timezone.utc).isoformat()
            if isinstance(created, (int, float)) else ""
        )
        items.append({
            "url": full_url,
            "title": d.get("title", ""),
            "author": author,
            "captured_at": captured_at,
            "body_text": _filters.truncate_body(body),
            "score": score,
            "num_comments": d.get("num_comments") or 0,
        })

    if stats is not None:
        stats.update({"fetched": fetched, "dropped_by_rule": fetched - len(items), "kept": len(items)})
    return items
