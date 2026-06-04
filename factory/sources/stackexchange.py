"""Stack Exchange source fetcher (api.stackexchange.com). No auth required.

Unauthenticated access has a generous daily quota (~300 calls). Question feeds
from sites like softwarerecs / webapps are dense with explicit unmet-need and
willingness-to-pay language ("I need a tool that…", "is there an app for…"),
which is exactly the signal Market Radar wants. Bodies arrive as HTML.
"""
import httpx

from . import _filters

_TIMEOUT = 20.0
_USER_AGENT = "venture-factory/0.1 by youval"


def fetch(source_config: dict, stats: dict | None = None) -> list[dict]:
    """Fetch a Stack Exchange /questions listing, normalize and prefilter.

    The url_template should include `site=<site>` and `filter=withbody`.
    Returns the shared item shape. On any error, returns []."""
    url = source_config.get("url_template") or source_config.get("url")
    if not url:
        return []

    try:
        resp = httpx.get(url, headers={"User-Agent": _USER_AGENT}, timeout=_TIMEOUT)
        resp.raise_for_status()
        data = resp.json()
    except (httpx.HTTPError, ValueError):
        return []

    questions = data.get("items", []) if isinstance(data, dict) else []
    fetched = len(questions)
    seen = _filters.load_seen_urls()
    items: list[dict] = []
    for q in questions:
        if not isinstance(q, dict):
            continue
        link = q.get("link", "")
        title = _filters.strip_html(q.get("title") or "")
        body = _filters.strip_html(q.get("body") or "") or title
        owner = q.get("owner") or {}
        author = owner.get("display_name", "") if isinstance(owner, dict) else ""

        if link in seen:
            continue
        if _filters.is_deleted(body):
            continue
        if _filters.is_bot(author):
            continue

        tags = q.get("tags") or []
        items.append({
            "url": link,
            "title": title,
            "author": author,
            "captured_at": _filters.epoch_to_iso(q.get("creation_date")),
            "body_text": _filters.truncate_body(body),
            "score": q.get("score") or 0,
            "num_comments": q.get("answer_count") or 0,
            "tags": tags if isinstance(tags, list) else [],
        })

    if stats is not None:
        stats.update({"fetched": fetched, "dropped_by_rule": fetched - len(items), "kept": len(items)})
    return items
