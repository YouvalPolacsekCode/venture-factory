# Status

<!-- Living status doc for this service experiment. Reporting agent updates the 7-day signal table daily; operator updates decisions log on review days. Never delete history — append. -->

## Slug

`<service-slug>`  <!-- kebab-case, matches folder name under services/ -->

## Created at (IDT)

<!-- YYYY-MM-DD HH:MM IDT -->

## Current stage

<!-- One of: validating | building | launched | scaling | killed | paused -->
<!-- Stage definitions:
     - validating: collecting market evidence + running responsiveness test, no paid customers yet
     - building: validation passed, building offer + landing + payment + delivery workflow
     - launched: live, accepting paid customers, in measurement window
     - scaling: hit scale threshold; increasing spend / cohort size
     - killed: failed kill threshold; experiment closed; learnings captured
     - paused: temporary stop (operator vacation, dependency missing); not killed
-->

Current stage: <!-- one of the above -->
Stage entered at (IDT): <!-- YYYY-MM-DD HH:MM -->

## Last 7-day signal

<!-- Reporting agent appends one row per material event. Cap visible window at 7 days; older rows roll to `status_archive.md`. -->

| Date (IDT) | Agent | Event | Value |
|---|---|---|---|
| <!-- YYYY-MM-DD HH:MM --> | <!-- e.g., Outreach agent --> | <!-- e.g., cohort_sent --> | <!-- e.g., 50 sent, 7 replied --> |
| <!-- EXAMPLE ONLY: 2026-05-30 14:00 --> | <!-- EXAMPLE ONLY: Payment agent --> | <!-- EXAMPLE ONLY: first_paid --> | <!-- EXAMPLE ONLY: USD 199, customer hash a7c... --> |

## Open blockers

<!-- Anything stopping forward motion. Each blocker has an owner and an age. Anything > 7 days old auto-escalates in the weekly review. -->

| Opened (IDT) | Blocker | Owner | Age (days) | Status |
|---|---|---|---|---|
| <!-- YYYY-MM-DD --> | <!-- description --> | <!-- agent or operator --> | <!-- N --> | <!-- open / in-progress / resolved --> |

## Operator decisions log

<!-- Append-only. One row per material decision. -->

| Date (IDT) | Decision | Rationale |
|---|---|---|
| <!-- YYYY-MM-DD --> | <!-- e.g., Approved Build Decision --> | <!-- 1-2 sentence reasoning --> |

## Kill / continue / scale recommendation from last weekly review

- Reviewed on (IDT): <!-- YYYY-MM-DD -->
- Reviewer agent: <!-- e.g., Reporting agent -->
- Recommendation: <!-- kill | continue | scale | pause -->
- Rationale (link to inputs): <!-- references metrics.md numbers, responsiveness_test.md results, cost_gain ratio -->
- Operator decision: <!-- accepted | overridden -->

## Next milestone

- Milestone: <!-- e.g., 10 paid customers, OR launch date, OR responsiveness test complete -->
- Target date (IDT): <!-- YYYY-MM-DD -->
- Owner agent: <!-- ... -->
