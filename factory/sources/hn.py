"""Hacker News source fetcher (Algolia HN Search API). No auth required."""
import httpx

from . import _filters

_TIMEOUT = 20.0
_USER_AGENT = "venture-factory/0.1 by youval"
_MIN_POINTS = 3


def fetch(source_config: dict, stats: dict | None = None) -> list[dict]:
    """Run the Algolia HN search in `url_template`, normalize and prefilter.

    Returns [{url, title, author, captured_at, body_text, points, num_comments}].
    Populates `stats` with fetched / dropped_by_rule / kept counts when provided.
    On any HTTP/parse error, returns [] (caller skips this source)."""
    url = source_config.get("url_template") or source_config.get("url")
    if not url:
        return []

    try:
        resp = httpx.get(url, headers={"User-Agent": _USER_AGENT}, timeout=_TIMEOUT)
        resp.raise_for_status()
        data = resp.json()
    except (httpx.HTTPError, ValueError):
        return []

    seen = _filters.load_seen_urls()
    hits = data.get("hits", [])
    fetched = len(hits)
    items: list[dict] = []
    for hit in hits:
        object_id = hit.get("objectID", "")
        permalink = hit.get("url") or f"https://news.ycombinator.com/item?id={object_id}"
        body = hit.get("story_text") or hit.get("comment_text") or hit.get("title") or ""
        points_raw = hit.get("points")  # None for comments (no upvote count)
        points = points_raw or 0

        if permalink in seen:
            continue
        if _filters.is_deleted(body):
            continue
        if _filters.is_bot(hit.get("author", "")):
            continue
        if points_raw is not None and points_raw < _MIN_POINTS:
            continue

        items.append({
            "url": permalink,
            "title": hit.get("title") or hit.get("story_title") or "",
            "author": hit.get("author", ""),
            "captured_at": hit.get("created_at", ""),
            "body_text": _filters.truncate_body(body),
            "points": points,
            "num_comments": hit.get("num_comments") or 0,
        })

    if stats is not None:
        stats.update({"fetched": fetched, "dropped_by_rule": fetched - len(items), "kept": len(items)})
    return items
