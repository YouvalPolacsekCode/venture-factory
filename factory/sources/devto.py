"""DEV (dev.to / Forem) source fetcher. Public articles API, no auth required.

Returns a flat array of articles. Tag-filtered feeds (e.g. tag=saas, startup,
productivity) surface maker/founder problems and tool gaps. Lower raw pain
density than Q&A sources, so pair it with a reaction threshold.
"""
import httpx

from . import _filters

_TIMEOUT = 20.0
_USER_AGENT = "venture-factory/0.1 by youval"
_MIN_REACTIONS = 5


def fetch(source_config: dict, stats: dict | None = None) -> list[dict]:
    """Fetch a dev.to /api/articles listing, normalize and prefilter.

    Honors an optional `min_reactions` override in the source config.
    Returns the shared item shape. On any error, returns []."""
    url = source_config.get("url_template") or source_config.get("url")
    if not url:
        return []

    min_reactions = source_config.get("min_reactions", _MIN_REACTIONS)

    try:
        resp = httpx.get(url, headers={"User-Agent": _USER_AGENT}, timeout=_TIMEOUT)
        resp.raise_for_status()
        data = resp.json()
    except (httpx.HTTPError, ValueError):
        return []

    articles = data if isinstance(data, list) else data.get("articles", [])
    fetched = len(articles)
    seen = _filters.load_seen_urls()
    items: list[dict] = []
    for a in articles:
        if not isinstance(a, dict):
            continue
        link = a.get("url") or a.get("canonical_url") or ""
        title = a.get("title") or ""
        body = a.get("description") or title
        user = a.get("user") or {}
        author = user.get("username", "") if isinstance(user, dict) else ""
        reactions = a.get("positive_reactions_count") or 0

        if link in seen:
            continue
        if _filters.is_deleted(body):
            continue
        if _filters.is_bot(author):
            continue
        try:
            if int(reactions) < int(min_reactions):
                continue
        except (TypeError, ValueError):
            pass

        tags = a.get("tag_list") or a.get("tags") or []
        items.append({
            "url": link,
            "title": title,
            "author": author,
            "captured_at": a.get("published_at") or a.get("created_at", ""),
            "body_text": _filters.truncate_body(body),
            "score": reactions,
            "num_comments": a.get("comments_count") or 0,
            "tags": tags if isinstance(tags, list) else [],
        })

    if stats is not None:
        stats.update({"fetched": fetched, "dropped_by_rule": fetched - len(items), "kept": len(items)})
    return items
