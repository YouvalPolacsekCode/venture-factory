"""
Signal source fetchers for Market Radar.

Public API:
    fetch(source_config: dict) -> list[dict]

Each returned item is a dict with at least:
    {url, title, author, captured_at, body_text}

Dispatch is keyed on `source_config["type"]`. Rate limiting is enforced
per-source against `rate_limit_rpm`, persisted in factory/state.db
(table: source_rate_limit) so limits survive across process runs.
"""
import sqlite3
import time
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
DB_PATH = REPO_ROOT / "factory" / "state.db"


def _now_utc() -> datetime:
    return datetime.now(timezone.utc)


def _respect_rate_limit(source_id: str, rate_limit_rpm: float | int | None) -> None:
    """Block until at least 60/rpm seconds have passed since this source's
    last call, then record the new call timestamp. No-op if rpm falsy."""
    if not rate_limit_rpm or rate_limit_rpm <= 0:
        return
    min_interval = 60.0 / float(rate_limit_rpm)

    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    try:
        conn.execute(
            "CREATE TABLE IF NOT EXISTS source_rate_limit ("
            "source_id TEXT PRIMARY KEY, last_called_at TEXT NOT NULL)"
        )
        row = conn.execute(
            "SELECT last_called_at FROM source_rate_limit WHERE source_id=?",
            (source_id,),
        ).fetchone()
        if row:
            try:
                last = datetime.fromisoformat(row[0])
            except ValueError:
                last = None
            if last is not None:
                elapsed = (_now_utc() - last).total_seconds()
                if elapsed < min_interval:
                    time.sleep(min_interval - elapsed)
        conn.execute(
            "INSERT INTO source_rate_limit (source_id, last_called_at) VALUES (?,?) "
            "ON CONFLICT(source_id) DO UPDATE SET last_called_at=excluded.last_called_at",
            (source_id or "unknown", _now_utc().isoformat()),
        )
        conn.commit()
    finally:
        conn.close()


def fetch(source_config: dict, stats: dict | None = None) -> list[dict]:
    """Fetch raw signal items for one source config entry.

    When `stats` is a dict, the fetcher fills it with fetched/dropped_by_rule/kept
    counts. Returns [] for disabled sources (except `ph`, which signals explicitly)."""
    stype = (source_config or {}).get("type", "")
    source_id = source_config.get("id", stype or "unknown")

    if stype != "ph" and not source_config.get("enabled", True):
        return []

    _respect_rate_limit(source_id, source_config.get("rate_limit_rpm"))

    if stype == "hn":
        from . import hn
        return hn.fetch(source_config, stats)
    if stype == "reddit":
        from . import reddit
        return reddit.fetch(source_config, stats)
    if stype == "lobsters":
        from . import lobsters
        return lobsters.fetch(source_config, stats)
    if stype == "stackexchange":
        from . import stackexchange
        return stackexchange.fetch(source_config, stats)
    if stype == "devto":
        from . import devto
        return devto.fetch(source_config, stats)
    if stype == "github":
        from . import github
        return github.fetch(source_config, stats)
    if stype == "ph":
        from . import ph
        return ph.fetch(source_config)

    # Unknown source type — surface nothing rather than crashing the sweep.
    return []
