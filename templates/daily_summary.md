<!--
Daily summary template. The `daily_summary` agent writes one of these per day to
reports/daily/<YYYY-MM-DD>.md at 07:00 IDT. All values below are EXAMPLE ONLY
and exist to show the shape; the agent overwrites everything on each run.

Conventions:
- All times IDT (UTC+3).
- Counts cover the previous 24h unless stated.
- "Last-7d signal" is a free-form 1-line summary written by analytics.
- Recommendations are kill | continue | scale | none-yet.
-->

# Daily Summary — 2026-06-12 (Fri)

<!-- Date in YYYY-MM-DD followed by short weekday in parens. IDT. -->

## Top-line (last 24h)

<!-- Single line per metric. Use integers. If a metric is N/A today, write 0, not "-". -->

| Metric | Value |
|---|---|
| New opportunities surfaced | 14 |
| Opportunities validated past threshold | 3 |
| Leads collected | 87 |
| Outreach messages sent | 42 |
| Replies received | 5 |
| Approvals pending in queue | 2 |
| Blockers (agent failures, policy hits) | 1 |

## Per-experiment status

<!--
One row per folder in experiments/ that is not archived. Stage is one of:
  discovery | validation | build | live | scaling | winding-down.
Recommendation is the factory's call; the operator confirms in the weekly ritual.
-->

| Slug | Stage | Last-7d signal | Recommendation |
|---|---|---|---|
| example-invoice-chaser | validation | 4 replies / 60 sends, 1 demo booked | continue |
| example-shopify-refund-bot | build | landing page live, 18 waitlist signups | continue |
| example-hebrew-lease-summarizer | live | 2 paying customers, MRR $98 | scale |
| example-airbnb-cleanup-coordinator | discovery | low pain signal in 3 of 5 cohorts | kill |

## Approval queue digest

<!--
Each item is a one-liner: ulid (short), action_type, slug, cost, expires_at.
If queue is empty, write "Empty." and skip the table.
-->

| ULID (short) | Action | Experiment | Cost USD | Expires (IDT) |
|---|---|---|---|---|
| 01JX...4A2 | send_outreach_email | example-invoice-chaser | 0.04 | 2026-06-13 18:00 |
| 01JX...7BQ | publish_landing_page | example-shopify-refund-bot | 0.00 | 2026-06-14 09:00 |

## Agent health

<!--
List only agents that failed, retried >3 times, or hit a policy cap in the last 24h.
If all green, write "All 18 agents nominal." and skip the table.
-->

| Agent | Status | Notes |
|---|---|---|
| outreach | degraded | 1 send bounced (invalid domain); auto-suppressed |

## Tomorrow's auto-scheduled actions

<!--
What the factory plans to do in the next 24h without operator intervention.
Limit to top 5. The agents schedule themselves via schedule_internal_job.
-->

1. `market_radar` sweeps 3 new B2B SaaS subreddits for pain signals.
2. `pain_validation` runs 10 targeted DM probes on yesterday's top opportunities.
3. `outreach` sends 50 emails across active experiments (within daily cap).
4. `analytics` computes weekly cost/gain ratios for the Sunday report.
5. `qa` re-runs the responsiveness regression on `example-hebrew-lease-summarizer`.

## Operator action items

<!--
Maximum 3. Ranked by impact. If nothing requires the operator, write
"None — process the approval queue and move on." and skip the list.
-->

1. **Confirm kill on `example-airbnb-cleanup-coordinator`** — pain signal has stayed below threshold for 6 days. Run `python scripts/kill_experiment.py example-airbnb-cleanup-coordinator --reason "no pain signal"`.
2. **Approve or reject the landing page for `example-shopify-refund-bot`** — copy is in the approval payload; 60-second read.
3. **Review the bounce in `outreach`** — if the source is `lead_research`'s allowlist, prune it.
