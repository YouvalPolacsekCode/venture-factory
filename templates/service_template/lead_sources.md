# Lead Sources

<!-- Where reachable, qualified prospects live. The Outreach agent uses this file to build weekly lead lists. -->

## Channels

<!-- Rank by lead_quality and access cost. Quality 1 = noisy/cold, 5 = warm and qualified. Audience size = realistic reachable count, not platform totals. -->

| Channel | Audience size estimate | Access method | Cost | Lead quality (1-5) |
|---|---|---|---|---|
| <!-- e.g., LinkedIn Sales Navigator search --> | <!-- e.g., 2,400 --> | <!-- scrape_public / api / manual / paid_provider --> | <!-- USD per lead or monthly --> | <!-- 1-5 --> |
| <!-- EXAMPLE ONLY: r/SaaS active posters --> | <!-- EXAMPLE ONLY: 800 --> | <!-- EXAMPLE ONLY: manual --> | <!-- EXAMPLE ONLY: 0 --> | <!-- EXAMPLE ONLY: 3 --> |

## Sample search queries

<!-- Concrete queries the Outreach agent can paste into each channel. Include Boolean operators where the channel supports them. -->

### LinkedIn

- <!-- e.g., (title:"head of finance" OR title:"finance manager") AND ("stripe" OR "payments") AND geo:Israel -->

### Google / X / Reddit

- <!-- e.g., site:reddit.com "stripe dispute" "manual" -->

### Other

- <!-- channel-specific query -->

## Lead list export plan

<!-- How many qualified leads we add to the working set per week, and what "qualified" means here. -->

- Target volume: <!-- e.g., 50 qualified leads per week -->
- Qualification criteria: <!-- field-by-field — must have email, must match ICP, must not be on suppression list -->
- Storage location: <!-- e.g., `services/<slug>/leads/leads_YYYY-WW.csv` -->
- Deduplication: <!-- key fields, e.g., email + linkedin_url -->

## Compliance notes

<!-- Do not skip. Even small experiments trigger these laws when you email people. -->

### GDPR (EU prospects)

<!-- Lawful basis (legitimate interest for B2B cold outreach is defensible if narrow and relevant); honor opt-out within 30 days; record source of each contact. -->

### Israeli Privacy Protection Law + Spam Law (חוק הספאם)

<!-- Israeli anti-spam law (Communications Law 1982, amendment 40) requires prior consent for commercial mass messaging to individuals. B2B-to-business-email has narrow allowances; do not message personal Gmail/Hotmail addresses without consent. Include sender identity, unsubscribe mechanism in every message. -->

### CAN-SPAM (US prospects)

<!-- Physical mailing address, accurate from/subject, working opt-out. -->

### Suppression list

<!-- Location of the do-not-contact list. Outreach agent must check before every send. -->
- Path: <!-- e.g., `services/<slug>/leads/suppression.csv` -->
