"""Reddit source fetcher (public listing JSON). No auth; respects 429."""
import time
from datetime import datetime, timezone

import httpx

_TIMEOUT = 20.0
_USER_AGENT = "venture-factory/0.1 by youval"
_MAX_RETRIES = 3


def fetch(source_config: dict) -> list[dict]:
    """Fetch a public Reddit listing (e.g. new.json) and normalize children.

    Returns [{url, title, author, captured_at, body_text, score, num_comments}].
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

    items: list[dict] = []
    for child in data.get("data", {}).get("children", []):
        d = child.get("data", {})
        permalink = d.get("permalink", "")
        full_url = ("https://www.reddit.com" + permalink) if permalink else d.get("url", "")
        created = d.get("created_utc")
        captured_at = (
            datetime.fromtimestamp(created, tz=timezone.utc).isoformat()
            if isinstance(created, (int, float)) else ""
        )
        items.append({
            "url": full_url,
            "title": d.get("title", ""),
            "author": d.get("author", ""),
            "captured_at": captured_at,
            "body_text": d.get("selftext") or d.get("title") or "",
            "score": d.get("score") or 0,
            "num_comments": d.get("num_comments") or 0,
        })
    return items
