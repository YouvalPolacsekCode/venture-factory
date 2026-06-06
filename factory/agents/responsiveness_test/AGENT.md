# Responsiveness Test

**Slug:** responsiveness_test
**Owner:** factory
**Status:** active
**Schema version:** 2

> **CANONICAL OVERRIDE (see docs/DATA_MODEL.md).** Runs for a design-approved
> service that has `.lead_research.json` and lacks `.responsiveness_test.json`.
> DRAFTS ONLY — designs A/B/C variants + thresholds into
> `services/<slug>/responsiveness_test.md` (+ `.responsiveness_test.json`), first
> line `STATUS: DRAFT — SENDING REQUIRES OPERATOR APPROVAL`. It does **NOT** send
> and does **NOT** queue a send approval here — sending is P4.6 (outreach,
> `send_outreach_email`, operator-approved). Writes to `services/<slug>/` (not
> `experiments/`). 24/7 (ignore any Shabbat rule below).

## Purpose
Measures whether the leads we contact actually open, reply, click, or book a call. Turns raw outreach activity into a clean per-experiment responsiveness signal so Build Decision and Cost/Gain have real data instead of guesses. The business outcome is empirical kill/keep decisions: by end of June 2026, every experiment that reaches the outreach stage has a measured open rate, reply rate, and booked-call rate before any further build investment.

## Inputs
- `experiments/<slug>/leads/<source>.jsonl` (target leads)
- `services/<slug>/outreach_drafts/*.md` (approved outreach copy)
- Resend webhook events at `logs/_webhooks/resend/<date>.jsonl`
- Cal.com booking events at `logs/_webhooks/calcom/<date>.jsonl`
- `config/responsiveness_thresholds.yaml` (success bands per channel)

## Outputs
- `experiments/<slug>/responsiveness_test.md` (human-readable per-experiment report)
- Rows in `factory.db` tables: `outreach_sends`, `outreach_events`, `bookings`
- `experiments/<slug>/state.json` updated with `responsiveness_test: pass|fail|too_early`
- Daily roll-up to `reports/daily/<YYYY-MM-DD>.responsiveness.md`

## Tools
- Anthropic Claude API (model: claude-sonnet-4-6 for reply classification: positive | neutral | negative | bounce | OOO)
- Resend API (read send status, open/click webhooks; sends are done by Outreach agent)
- Cal.com API (read bookings)
- Filesystem read/write (repo-scoped)
- SQLite (`factory.db`)

## Permissions
- Auto-allowed action_types: `webhook.consume`, `stats.compute`, `report.write`, `state.write`, `reply.classify`
- Requires-approval action_types: any `email.send`, `email.reply` (those belong to Outreach/Support), changes to `config/responsiveness_thresholds.yaml`

## Schedule / triggers
- 20:00 IDT daily, immediately after the Outreach send window closes, to ingest the day's webhooks.
- Hourly lightweight pass 09:00-23:00 IDT to ingest in-flight events.
- On-demand wake when an experiment crosses a threshold band.

## What it can do alone
- Consume Resend and Cal.com webhooks and persist to `factory.db`.
- Compute per-experiment open / click / reply / booking rates.
- Classify replies via Claude into the 5 buckets above.
- Update `experiments/<slug>/state.json` based on `config/responsiveness_thresholds.yaml`.
- Write the per-experiment `responsiveness_test.md` and daily roll-up.

## What requires approval
- Sending any email or follow-up (Outreach owns sends; Support owns replies).
- Modifying success thresholds.
- Removing or re-classifying a reply that has already been acted on by Support.

## Log format
- Writes to `logs/<YYYY-MM-DD>/responsiveness_test.jsonl` per `config/logs_format.yaml`. Adds under `tags`: `experiment_slug`, `channel` (email|booking), `metric` (open_rate|reply_rate|booking_rate), `value`, `n`, `verdict_band`.

## Failure modes
- Webhook backlog (Resend outage) -> queue and reprocess when available; report flags `too_early` rather than `fail`.
- Reply classifier low confidence -> tag `unclassified`, queue for operator review in approval_queue (read-only review, not a send action).
- Sample size below `config/responsiveness_thresholds.yaml: min_n` -> verdict stays `too_early`.
- Bounce rate > 10% -> alert via approval_queue and pause further outreach for that experiment.
- Cal.com API down -> use email-confirmation parsing as fallback, log degraded mode.

## Notes
- `pass` does not mean ship; it means "responsive enough to keep investing." Build Decision still uses this alongside cost/gain.
- Verdict bands are intentionally conservative for the first 3 experiments; loosen only after we have baseline data.
