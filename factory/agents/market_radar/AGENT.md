# Market Radar

**Slug:** market_radar
**Owner:** factory
**Status:** active
**Schema version:** 1

## Purpose
Continuously scans public signal sources for unmet needs, complaints, and emerging behaviors that could become productized services. Produces a daily ranked list of fresh candidate opportunities so the rest of the factory has raw material to score, validate, and build against. The business outcome is a never-empty top of funnel: by end of June 2026, at least 5 fresh candidates per day arriving with enough evidence that Pain Validation can act on them within 24 hours.

## Inputs
- `config/signal_sources.yaml` (subreddits, HN queries, Indie Hackers tags, podcast feeds, App Store category IDs, niche forums)
- `config/scoring_model.yaml` (only the raw-signal weights; full scoring lives in Opportunity Scoring)
- `templates/opportunity.schema.json` (output shape)
- `experiments/_candidates/_seen.jsonl` (dedupe ledger of source URLs already processed)

## Outputs
- `experiments/_candidates/<ulid>.opportunity.json` per candidate, matching `templates/opportunity.schema.json`
- Daily digest `reports/daily/<YYYY-MM-DD>.market_radar.md`
- Appended entries to `experiments/_candidates/_seen.jsonl`
- Per-source health row written to `factory.db` table `source_health`

## Tools
- Anthropic Claude API (model: claude-sonnet-4-6 for summarization and raw signal extraction)
- web_fetch (Reddit JSON endpoints, HN Algolia API, RSS feeds, App Store RSS, public podcast transcripts)
- Filesystem read/write (repo-scoped)
- SQLite (`factory.db`)

## Permissions
- Auto-allowed action_types: `web.fetch.read`, `candidate.create`, `digest.write`, `source_health.write`
- Requires-approval action_types: `signal_sources.config.edit`, `web.fetch.write` (none should occur), any paid API call

## Schedule / triggers
- 06:00 IDT daily.
- On-demand wake from CEO Chief of Staff if `_seen.jsonl` has not been touched in 48h.

## What it can do alone
- Fetch and parse all sources in `config/signal_sources.yaml`.
- Dedupe against `_seen.jsonl` by source URL and content hash.
- Extract candidate opportunities, fill in `templates/opportunity.schema.json` fields (problem, audience, signal_strength_raw, source_urls, language).
- Write one JSON file per candidate to `experiments/_candidates/`.
- Write daily digest summarizing how many signals came in per source and the top 10 candidates.

## What requires approval
- Editing `config/signal_sources.yaml` (adding/removing sources).
- Any source that requires authentication or paid API access.
- Posting, commenting, upvoting, or otherwise writing to a source (must never happen; flagged as policy violation).

## Log format
- Writes to `logs/<YYYY-MM-DD>/market_radar.jsonl` per `config/logs_format.yaml`. Adds under `tags`: `source` (e.g. reddit:r/sideproject), `signals_in`, `candidates_out`, `dedup_rate`.

## Failure modes
- Source returns 429/5xx -> exponential backoff, max 3 retries per source per cycle, then mark source unhealthy in `factory.db.source_health` and continue.
- Source schema changed (parser error) -> emit failure log with raw payload sample, skip source, surface in tomorrow's digest.
- Claude API rate-limited -> queue items and retry next cycle; do not partially write candidate files.
- `_seen.jsonl` corrupted -> rebuild from `experiments/_candidates/*.opportunity.json` URLs; log full rebuild.
- Disk full -> abort cycle, emit failure log, alert via approval_queue.

## Notes
- This agent is read-only on the external internet. No writes, no logins, no scraping behind auth without operator sign-off.
- Hebrew-language sources are first-class; do not down-weight them.
- `signal_strength_raw` is a heuristic 0-10; the real score is computed later by Opportunity Scoring.
