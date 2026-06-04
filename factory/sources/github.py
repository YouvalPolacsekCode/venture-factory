"""GitHub source fetcher (Issues search API). No auth required (low rate).

Open issues labelled as feature requests / pain ("FR:", "would be great if…")
across public repos are concrete, sourced demand signals. Unauthenticated
search is rate-limited (~10 req/min), which is fine for one query per daily run.
Issue bodies are Markdown.
"""
import httpx

from . import _filters

_TIMEOUT = 20.0
_USER_AGENT = "venture-factory/0.1 by youval"
_ACCEPT = "application/vnd.github+json"


def fetch(source_config: dict, stats: dict | None = None) -> list[dict]:
    """Run a GitHub Issues search from `url_template`, normalize and prefilter.

    The url_template should already exclude PRs (e.g. `+is:issue`).
    Returns the shared item shape. On any error, returns []."""
    url = source_config.get("url_template") or source_config.get("url")
    if not url:
        return []

    try:
        resp = httpx.get(
            url,
            headers={"User-Agent": _USER_AGENT, "Accept": _ACCEPT},
            timeout=_TIMEOUT,
        )
        resp.raise_for_status()
        data = resp.json()
    except (httpx.HTTPError, ValueError):
        return []

    issues = data.get("items", []) if isinstance(data, dict) else []
    fetched = len(issues)
    seen = _filters.load_seen_urls()
    items: list[dict] = []
    for it in issues:
        if not isinstance(it, dict):
            continue
        if "pull_request" in it:  # safety: never treat a PR as a signal
            continue
        link = it.get("html_url", "")
        title = it.get("title") or ""
        body = _filters.strip_html(it.get("body") or "") or title
        user = it.get("user") or {}
        author = user.get("login", "") if isinstance(user, dict) else ""
        reactions = (it.get("reactions") or {}).get("total_count", 0)

        if link in seen:
            continue
        if _filters.is_deleted(body):
            continue
        if _filters.is_bot(author):
            continue

        items.append({
            "url": link,
            "title": title,
            "author": author,
            "captured_at": it.get("created_at", ""),
            "body_text": _filters.truncate_body(body),
            "score": reactions or 0,
            "num_comments": it.get("comments") or 0,
            "tags": [lbl.get("name") for lbl in (it.get("labels") or [])
                     if isinstance(lbl, dict) and lbl.get("name")],
        })

    if stats is not None:
        stats.update({"fetched": fetched, "dropped_by_rule": fetched - len(items), "kept": len(items)})
    return items
