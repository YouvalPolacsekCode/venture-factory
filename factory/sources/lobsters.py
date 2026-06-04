"""Lobsters source fetcher (lobste.rs JSON). No auth required.

Lobsters is a focused computing/tech community; its newest/hottest JSON feeds
return a flat array of stories. Good for developer-tooling friction signals.
"""
import httpx

from . import _filters

_TIMEOUT = 20.0
_USER_AGENT = "venture-factory/0.1 by youval"


def fetch(source_config: dict, stats: dict | None = None) -> list[dict]:
    """Fetch a Lobsters listing (e.g. newest.json / hottest.json), normalize
    and prefilter. Returns the shared item shape. On any error, returns []."""
    url = source_config.get("url_template") or source_config.get("url")
    if not url:
        return []

    try:
        resp = httpx.get(url, headers={"User-Agent": _USER_AGENT}, timeout=_TIMEOUT)
        resp.raise_for_status()
        data = resp.json()
    except (httpx.HTTPError, ValueError):
        return []

    stories = data if isinstance(data, list) else data.get("stories", [])
    fetched = len(stories)
    seen = _filters.load_seen_urls()
    items: list[dict] = []
    for s in stories:
        if not isinstance(s, dict):
            continue
        # Use the Lobsters discussion permalink as the stable id (always present);
        # the submitted external link goes in the body for context.
        permalink = s.get("short_id_url") or s.get("comments_url") or s.get("url", "")
        title = s.get("title") or ""
        link = s.get("url") or ""
        desc = s.get("description_plain") or s.get("description") or ""
        body = desc or title
        if link and link != permalink:
            body = f"{body}\n(link: {link})"
        author = s.get("submitter_user") or ""
        if isinstance(author, dict):  # older API returned a user object
            author = author.get("username", "")

        if permalink in seen:
            continue
        if _filters.is_deleted(body):
            continue
        if _filters.is_bot(author):
            continue

        tags = s.get("tags") or []
        items.append({
            "url": permalink,
            "title": title,
            "author": author,
            "captured_at": s.get("created_at", ""),
            "body_text": _filters.truncate_body(body),
            "score": s.get("score") or 0,
            "num_comments": s.get("comment_count") or 0,
            "tags": tags if isinstance(tags, list) else [],
        })

    if stats is not None:
        stats.update({"fetched": fetched, "dropped_by_rule": fetched - len(items), "kept": len(items)})
    return items
