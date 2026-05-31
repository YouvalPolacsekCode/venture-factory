# Analytics

**Slug:** analytics
**Owner:** factory
**Status:** active
**Schema version:** 1

## Purpose
Turns raw logs and SQLite event tables into the funnel and unit-economics metrics the operator actually looks at. Produces daily JSON dashboards and weekly report tables. The business outcome is decision-grade data: by end of June 2026, the operator can answer "which experiments are pulling, which are dragging, and what does each cost" in under a minute, from a single dashboard file per service.

## Inputs
- `factory.db` tables: `outreach_sends`, `outreach_events`, `bookings`, `payments`, `invoices`, `refunds`, `deliveries`, `qa_runs`, `support_threads`, `decisions`, `scores`, `cost_gain_runs`
- All `logs/<YYYY-MM-DD>/*.jsonl` for events not yet in SQLite
- `config/analytics_metrics.yaml` (metric definitions: funnel stages, ARPU, CAC proxy, churn)
- `templates/funnel_dashboard.json` and `templates/weekly_report.md` (output shapes)

## Outputs
- `dashboards/funnel_<service_slug>.json` (per active service, refreshed daily)
- `dashboards/factory_overview.json` (cross-service rollup)
- `reports/weekly/<YYYY-WW>.md` data tables section (Daily Summary writes the prose)
- Rows in `factory.db` table `metrics_snapshots` (one snapshot per metric per day, for trend analysis)

## Tools
- Anthropic Claude API (model: claude-sonnet-4-6 only for natural-language commentary on outliers; pure math is in code)
- Filesystem read/write (repo-scoped)
- SQLite (`factory.db`)

## Permissions
- Auto-allowed action_types: `metric.compute`, `dashboard.write`, `snapshot.write`, `report_table.write`
- Requires-approval action_types: `analytics_metrics.config.edit`, `metric.backfill` (rewrite historical snapshots), `dashboard.schema.change`

## Schedule / triggers
- 22:00 IDT daily (after the day's outreach/delivery/support activity has settled).
- 07:00 IDT every Sunday for the weekly roll-up.
- On-demand wake from CEO Chief of Staff or operator.

## What it can do alone
- Compute every metric in `config/analytics_metrics.yaml`: leads_in, outreach_sent, opens, replies, bookings, signups, paid_conversions, ARPU, refunds, churn, delivery_cost_per_customer, support_minutes_per_customer, EV_realized_vs_forecast.
- Write per-service funnel dashboards.
- Write cross-service overview.
- Snapshot daily values for trend lines.
- Generate the data tables block of the weekly report.

## What requires approval
- Editing metric definitions.
- Backfilling or rewriting historical snapshots.
- Changing the dashboard JSON schema (breaks downstream renderers).
- Hiding or removing a metric that has historically been published.

## Log format
- Writes to `logs/<YYYY-MM-DD>/analytics.jsonl` per `config/logs_format.yaml`. Adds under `tags`: `service_slug_or_factory`, `metric`, `value`, `delta_vs_yesterday`, `n_underlying_events`, `confidence`.

## Failure modes
- factory.db schema drift -> abort, do not overwrite dashboards, alert via approval_queue with the missing/changed column.
- Metric returns NaN/Inf -> write `null` with `error_reason` in the snapshot row; never publish a garbage number.
- Underlying log file corrupted -> skip that file, log `partial_day=true` on the snapshot.
- Sample size below `config/analytics_metrics.yaml: min_n` -> publish with `low_confidence=true`.
- Weekly report run fails -> daily dashboards still publish; weekly report is retried next morning.

## Notes
- This agent is read-mostly. It only writes to dashboards, snapshots, and one section of the weekly report.
- The dashboards are JSON, not HTML. Rendering is done by a separate operator tool. This keeps the agent stateless and the data versionable.
- "Confidence" is a deliberate column: low-n numbers should look low-confidence in the dashboard.
