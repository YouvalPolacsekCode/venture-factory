# Metrics

<!-- What we measure for this service. The Reporting agent reads this file to build the daily and weekly summaries. -->

## Funnel metrics

<!-- Top-of-funnel to repeat. Each metric has a definition that anyone on the team would compute the same way. -->

| Stage | Metric | Definition | Source |
|---|---|---|---|
| Awareness | Impressions | Landing page views (unique sessions) | <!-- e.g., Plausible / GA --> |
| Interest | Clicks | Primary CTA clicks | <!-- analytics --> |
| Intent | Form starts | Onboarding form first-field interaction | <!-- form tool --> |
| Action | Form completions | Onboarding form submitted | <!-- form tool / webhook log --> |
| Revenue | Paid | `payment_intent.succeeded` count | Stripe |
| Fulfilment | Delivered | Final deliverable sent and not bounced | Delivery agent log |
| Retention | Repeat | Same customer purchases again within 90 days | Stripe customer ID match |

Funnel conversion rates to track weekly:
- Impressions -> Clicks
- Clicks -> Form starts
- Form starts -> Form completions
- Form completions -> Paid
- Paid -> Delivered (should be ~100%; deviations are operational issues)
- Delivered -> Repeat

## Quality metrics

<!-- How well we're serving the customers we do get. -->

| Metric | Definition | Target | Source |
|---|---|---|---|
| NPS proxy | Post-delivery 1-question survey: "Would you recommend this to a colleague? 0-10" | >= 7 average | <!-- survey tool --> |
| Refund rate | Refunds / Paid in trailing 30 days | <= 5% | Stripe |
| Complaint count | Distinct customers who raised a complaint (any channel) per week | trend; investigate any week > prior 4-week avg + 2 | Support log |
| On-time delivery rate | Deliveries within SLA / total deliveries | >= 95% | Delivery agent log |

## Unit economics

<!-- Honest math. Update monthly. -->

| Metric | Definition | Current | Target |
|---|---|---|---|
| CAC | (Outreach cost + paid ads + lead provider cost + agent compute attributable) / Paid customers in period | <!-- USD --> | <!-- < gross margin per customer --> |
| Gross margin per customer | (Price paid - delivery cost: compute + tools + any human time costed at operator's rate) / Price paid | <!-- % --> | <!-- >= 70% target for pure-agent services --> |
| Payback period | Months until cumulative gross margin from a customer cohort covers their CAC | <!-- months --> | <!-- <= 3 months --> |
| LTV (proxy) | Gross margin per customer x estimated purchase count over 12 months | <!-- USD --> | <!-- >= 3x CAC --> |

## Data sources

<!-- Where the Reporting agent reads from. -->

- Funnel dashboard: `dashboards/funnel_<slug>.json`
- Stripe events: `payments/<customer>/events.jsonl` + Stripe API
- Support log: `services/<slug>/support/log.jsonl`
- Delivery log: `services/<slug>/work/_log.jsonl`
- Survey responses: <!-- e.g., `services/<slug>/surveys/responses.csv` -->
- Cost ledger: `dashboards/costs_<slug>.json` (compute, tool fees, lead costs)
