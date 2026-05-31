# Pain Validation

**Slug:** pain_validation
**Owner:** factory
**Status:** active
**Schema version:** 1

## Purpose
Takes the top candidate opportunities from Market Radar and stress-tests whether a real, frequent, paid-for pain exists. Produces structured `market_evidence.md` files that either justify advancing an opportunity to Lead Research or recommend killing it. The business outcome is fewer wasted build cycles: only opportunities with documented pain and at least one credible willingness-to-pay signal proceed.

## Inputs
- Top-N candidates from `experiments/_candidates/<ulid>.opportunity.json` (N from `config/orchestration.yaml`, default 5/day)
- `experiments/_candidates/<ulid>.score.json` if Opportunity Scoring has already run
- `templates/market_evidence.md` (output skeleton)
- `config/pain_validation.yaml` (evidence thresholds, must-have vs nice-to-have checks)

## Outputs
- `experiments/<slug>/market_evidence.md` (one per promoted candidate)
- `experiments/<slug>/state.json` with `pain_validation: pass|fail|inconclusive`
- Promoted candidates moved from `experiments/_candidates/` into `experiments/<slug>/` (slug = human-readable, derived from problem statement)
- Approval items for any outreach proposals

## Tools
- Anthropic Claude API (model: claude-sonnet-4-6 for synthesis and source reading)
- web_fetch (deeper read of source threads, competitor pricing pages, public reviews)
- Filesystem read/write (repo-scoped)
- SQLite (`factory.db`)

## Permissions
- Auto-allowed action_types: `web.fetch.read`, `evidence.write`, `experiment.promote`, `state.write`
- Requires-approval action_types: `survey.post`, `outreach.contact`, `dm.send`, `community.post`, any action that contacts a real person

## Schedule / triggers
- 07:00 IDT daily.
- On-demand wake from CEO Chief of Staff when a candidate scores above the auto-promote threshold.

## What it can do alone
- Read each candidate's source URLs in depth.
- Search for adjacent threads, competitor products, and existing solutions via web_fetch + Claude reasoning.
- Score frequency, severity, and existing-spend evidence per `config/pain_validation.yaml`.
- Write `market_evidence.md` filled with quotes, source links, competitor pricing, and a verdict.
- Promote opportunity into `experiments/<slug>/` folder and update `state.json`.

## What requires approval
- Posting any survey link to a public community.
- Contacting any individual (DM, email, comment reply) to validate.
- Spending money on a paid research tool (Statista, SimilarWeb pro, etc.).
- Using any source that requires personal account authentication.

## Log format
- Writes to `logs/<YYYY-MM-DD>/pain_validation.jsonl` per `config/logs_format.yaml`. Adds under `tags`: `candidate_ulid`, `verdict` (pass|fail|inconclusive), `evidence_count`, `competitor_count`, `proposed_slug`.

## Failure modes
- Candidate JSON malformed -> skip with failure log, leave file in `_candidates/`, notify CEO Chief of Staff.
- All source URLs return 404/gone -> mark inconclusive, recommend re-scan by Market Radar.
- Claude reasoning returns low-confidence verdict -> default to `inconclusive`, never auto-promote.
- web_fetch repeatedly blocked (Cloudflare, etc.) -> log domain, fall back to cached/archive.org where allowed.
- Slug collision in `experiments/` -> append `-2`, `-3`, never overwrite.

## Notes
- The bar for `pass` is intentionally high: at least 5 distinct pain quotes, at least 1 willingness-to-pay signal (people paying for a workaround, asking "is there a tool that...", or competitor charging money), and clear target audience.
- Inconclusive verdicts are not failures; they get re-queued for the next cycle.
