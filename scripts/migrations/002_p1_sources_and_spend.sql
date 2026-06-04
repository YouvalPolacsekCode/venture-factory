-- Phase 1: per-call model/token accounting on spend_ledger, and a
-- persisted rate-limit ledger for external source fetchers.

ALTER TABLE spend_ledger ADD COLUMN model TEXT;
ALTER TABLE spend_ledger ADD COLUMN tokens_in INTEGER NOT NULL DEFAULT 0;
ALTER TABLE spend_ledger ADD COLUMN tokens_out INTEGER NOT NULL DEFAULT 0;

CREATE TABLE IF NOT EXISTS source_rate_limit (
    source_id TEXT PRIMARY KEY,
    last_called_at TEXT NOT NULL
);
