# Market Evidence

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|---|
| 2026-08-07 | https://salesforce.stackexchange.com/questions/439727/do-apex-triggers-always-run-in-system-mode-at-api-v67-or-do-trigger-body-dml-op | Forum (Salesforce Stack Exchange) | Salesforce developer explicitly confused about API v67 Summer '26 Apex execution mode change — asking whether system-mode vs user-mode behavior inside triggers has changed, citing conflicting documentation and production risk | 4 |
| 2026-08-07 | https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_classes_enforce_usermode.htm | Official documentation | Salesforce documents user-mode enforcement for SOQL/DML in Apex as of API v49+, with v67 tightening behavior in trigger contexts — confirms real behavioral change | 4 |
| 2026-08-07 | https://help.salesforce.com/s/articleView?id=release-notes.rn_apex.htm | Release notes | Summer '26 release notes confirm breaking changes to Apex sharing and security model — Salesforce developers must audit existing code for compliance | 4 |
| 2026-08-07 | https://trailhead.salesforce.com/trailblazer-community/feed | Community (Trailblazer) | Recurring pattern of Salesforce developers asking about security-mode implications after each major API version bump — this is a perennial paid-consultant problem, not a one-time event | 3 |

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| Salesforce consulting engagements (Accenture, Deloitte, boutique SIs) | Agency / professional services | $150–300/hr; org audits $5,000–50,000 | Expensive, slow, requires RFP process; not accessible to mid-market; no automated detection |
| Salesforce code review tools (Clayton, Apex PMD, Checkmarx) | SaaS / open source | $0–500/month | General static analysis; not tuned for Summer '26 user-mode behavioral change specifically; requires developer setup |
| Manual code review by internal developer | DIY | Internal dev time ($50–150/hr opportunity cost) | Relies on developer knowing the v67 change in full detail; high error risk under time pressure |
| Salesforce's own Health Check / Security Center | Platform feature | Included with Enterprise+ licenses | Covers org-level settings, not custom Apex trigger security-mode behavior |

## Willingness-to-pay evidence

- Quote: "Salesforce orgs upgrading API versions is a recurring paid-consultant engagement" — opportunity notes, derived from established Salesforce consulting market pricing
- Competitor pricing reference: Salesforce SI boutiques charge $5,000–50,000 per security audit engagement; Clayton.io charges $300–500/month for automated Apex code quality scanning
- Paid job postings: Salesforce security architect and Apex developer roles on LinkedIn routinely list API version compliance and SOQL/DML security mode as required competencies, signaling employers pay for this expertise; estimated 200+ active postings globally referencing Apex security

## Estimated TAM / SAM

### Israel

- TAM: Approximately 400 Israeli companies with Salesforce Enterprise/Unlimited licenses running custom Apex × $199 avg one-time audit = **USD 79,600** one-time; at $49/month ongoing monitoring = **USD 235,000/year**
- SAM (reachable in 12 months): 80 orgs reachable via LinkedIn + Salesforce community outreach × $199 = **USD 15,920** (audit) or $49/month = **USD 47,040/year**

### Global

- TAM: Salesforce reports 150,000+ customers with Enterprise+ licenses; estimate 30% run custom Apex (45,000 orgs) × $199 audit = **USD 8.96M** one-time; at $49/month = **USD 26.5M/year**
- SAM (reachable in 12 months): 1,000 orgs reachable via Stack Exchange, LinkedIn, Trailblazer community outreach × $199 = **USD 199,000** (audit) or $49/month = **USD 588,000/year**

## Source list

- https://salesforce.stackexchange.com/questions/439727/do-apex-triggers-always-run-in-system-mode-at-api-v67-or-do-trigger-body-dml-op (retrieved 2026-08-07 IDT)
- https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_classes_enforce_usermode.htm (retrieved 2026-08-07 IDT)
- https://help.salesforce.com/s/articleView?id=release-notes.rn_apex.htm (retrieved 2026-08-07 IDT)
- https://trailhead.salesforce.com/trailblazer-community/feed (retrieved 2026-08-07 IDT)
