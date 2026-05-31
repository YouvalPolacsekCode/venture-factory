# Daily Summary

**Slug:** daily_summary
**Owner:** factory
**Status:** active
**Schema version:** 1

## Purpose
Assembles the operator's daily report from every other agent's logs, the approval queue, and current experiment/service status, using `templates/daily_summary.md` as the shape. The business outcome is a single file the operator opens each morning that answers: what shipped, what is waiting on me, what changed in the funnel, what to do today.

## Inputs
- Today's `logs/<YYYY-MM-DD>/*.jsonl` from every agent
- `approval_queue/` (pending items, with age)
- `experiments/*/state.json` (active and recently-changed)
- `services/*/state.json`
- `dashboards/funnel_*.json` and `dashboards/factory_overview.json` (latest snapshots from Analytics)
- `reports/daily/<YYYY-MM-DD>.md` (the seed file written by CEO Chief of Staff at 05:55 IDT)
- `templates/daily_summary.md` (canonical section order and headings)

## Outputs
- `reports/daily/<YYYY-MM-DD>.md` (completed, replacing the morning seed)
- `reports/daily/<YYYY-MM-DD>.attachments/` (optional charts, ranked lists, JSON appendices)
- Updated row in `factory.db` table `daily_reports`

## Tools
- Anthropic Claude API (model: claude-sonnet-4-6 for synthesis and prose; never opus — this is daily routine)
- Filesystem read/write (repo-scoped)
- SQLite (`factory.db`)

## Permissions
- Auto-allowed action_types: `report.write`, `report.attach`, `state.read`
- Requires-approval action_types: `daily_summary_template.edit`, `report.republish` (rewriting a prior day's report), `report.delete`

## Schedule / triggers
- 10:00 IDT daily (after morning agents 06:00-09:30 have produced their outputs).
- On-demand wake from operator (e.g. "regenerate today's report including the 14:00 cost_gain run").

## What it can do alone
- Read every input listed above.
- Synthesize the day's narrative per `templates/daily_summary.md` sections: top-of-mind (operator decisions waiting), what shipped, funnel delta, experiments moved, approvals pending with age, anomalies, recommended next 3 actions for today.
- Attach ranked lists and the latest dashboard snapshots.
- Replace the 05:55 IDT seed file with the completed report.
- Write the row in `daily_reports`.

## What requires approval
- Editing `templates/daily_summary.md`.
- Republishing a prior day's report (overwriting historical record).
- Deleting any report.
- Including any raw PII in the report (it should always be hashed/initialized).

## Log format
- Writes to `logs/<YYYY-MM-DD>/daily_summary.jsonl` per `config/logs_format.yaml`. Adds under `tags`: `sections_filled` (list), `inputs_missing` (list, e.g. analytics_overview), `pending_approvals_count`, `oldest_pending_approval_age_h`, `word_count`.

## Failure modes
- Analytics has not run yet today -> proceed without funnel delta section, mark `inputs_missing: [analytics]`, generate report anyway. Operator gets partial signal beats no signal.
- Approval queue empty -> still write the report; "no decisions waiting" is itself a useful signal.
- Template file invalid -> fall back to a minimal hard-coded section list and log a template_invalid event.
- Word count exceeds template guidance -> auto-trim less critical sections (anomalies, attachments index) before truncating the operator-decisions section.
- Report write conflict (operator was editing the seed) -> save as `<date>.agent.md` next to the seed, alert operator to merge.

## Notes
- Operator decisions go at the top. Always. Even when nothing is waiting (then it says "Nothing waiting on you — here is the day's plan").
- The seed file written at 05:55 by CEO Chief of Staff contains the day's plan; this agent layers in the results. If the seed is missing, write the whole thing from scratch.
- Hebrew is not used in the daily report; operator (Youval) reads it in English.
