-- Phase 1.5: separate cache-token accounting on spend_ledger, and a small
-- table to persist the smoke-test cost baseline for regression checks.

ALTER TABLE spend_ledger ADD COLUMN cache_creation_input_tokens INTEGER NOT NULL DEFAULT 0;
ALTER TABLE spend_ledger ADD COLUMN cache_read_input_tokens INTEGER NOT NULL DEFAULT 0;

CREATE TABLE IF NOT EXISTS smoke_baseline (
    metric TEXT PRIMARY KEY,
    value REAL NOT NULL,
    recorded_at TEXT NOT NULL
);
