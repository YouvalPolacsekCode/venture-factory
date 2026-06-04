"""Hacker News source fetcher (Algolia HN Search API). No auth required."""
import httpx

_TIMEOUT = 20.0
_USER_AGENT = "venture-factory/0.1 by youval"


def fetch(source_config: dict) -> list[dict]:
    """Run the Algolia HN search in `url_template` and normalize the hits.

    Returns [{url, title, author, captured_at, body_text, points, num_comments}].
    On any HTTP/parse error, returns [] (the caller skips this source)."""
    url = source_config.get("url_template") or source_config.get("url")
    if not url:
        return []

    try:
        resp = httpx.get(url, headers={"User-Agent": _USER_AGENT}, timeout=_TIMEOUT)
        resp.raise_for_status()
        data = resp.json()
    except (httpx.HTTPError, ValueError):
        return []

    items: list[dict] = []
    for hit in data.get("hits", []):
        object_id = hit.get("objectID", "")
        permalink = hit.get("url") or f"https://news.ycombinator.com/item?id={object_id}"
        body = hit.get("story_text") or hit.get("comment_text") or hit.get("title") or ""
        items.append({
            "url": permalink,
            "title": hit.get("title") or hit.get("story_title") or "",
            "author": hit.get("author", ""),
            "captured_at": hit.get("created_at", ""),
            "body_text": body,
            "points": hit.get("points") or 0,
            "num_comments": hit.get("num_comments") or 0,
        })
    return items
