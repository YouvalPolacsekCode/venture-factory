-- Initial schema for Venture Factory state.db

CREATE TABLE IF NOT EXISTS runs (
    id TEXT PRIMARY KEY,
    agent TEXT NOT NULL,
    started_at TEXT NOT NULL,
    ended_at TEXT,
    status TEXT NOT NULL DEFAULT 'running',
    tokens_in INTEGER NOT NULL DEFAULT 0,
    tokens_out INTEGER NOT NULL DEFAULT 0,
    cost_usd_estimate REAL NOT NULL DEFAULT 0.0,
    outputs TEXT NOT NULL DEFAULT '[]',
    approval_requests TEXT NOT NULL DEFAULT '[]',
    errors TEXT NOT NULL DEFAULT '[]'
);

CREATE TABLE IF NOT EXISTS signals (
    id TEXT PRIMARY KEY,
    agent TEXT NOT NULL,
    source_type TEXT,
    source_url TEXT,
    content_hash TEXT,
    seen_at TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_signals_hash ON signals(content_hash);
CREATE INDEX IF NOT EXISTS idx_signals_url ON signals(source_url);

CREATE TABLE IF NOT EXISTS spend_ledger (
    id TEXT PRIMARY KEY,
    agent TEXT NOT NULL,
    date TEXT NOT NULL,
    cost_usd REAL NOT NULL DEFAULT 0.0,
    run_id TEXT,
    created_at TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_spend_date ON spend_ledger(date);

CREATE TABLE IF NOT EXISTS experiments (
    id TEXT PRIMARY KEY,
    opportunity_ulid TEXT,
    service_slug TEXT,
    status TEXT NOT NULL,
    started_at TEXT NOT NULL,
    decision_log TEXT NOT NULL DEFAULT '[]'
);
