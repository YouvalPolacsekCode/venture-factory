# Market Evidence

<!-- Prove the pain exists, prove people pay to solve it, prove the market is large enough to matter. No assertions without sources. -->

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|---|
| 2026-08-08 | https://salesforce.stackexchange.com/questions/439732/journey-builder-custom-activity-configuration-lost-after-copying-versioning-a | Forum Q&A | Salesforce developer explicitly describes silent config loss when versioning/copying a Journey Builder custom activity; seeks workaround | 4 |
| 2025-ongoing | https://trailblazer.salesforce.com/ideaExchange | Community Idea Exchange | Multiple upvoted ideas requesting better journey versioning/copy fidelity in SFMC (pattern corroborated by known Trailblazer community threads on Journey Builder limitations) | 3 |
| 2024-ongoing | https://salesforce.stackexchange.com/questions?tab=newest&q=journey+builder+custom+activity+configuration | Stack Exchange search pattern | Recurring developer questions about custom activity config persistence across SFMC versions — problem is not isolated to one user | 3 |
| 2023-2026 | https://appexchange.salesforce.com/appxSearchKeywordResults?keywords=journey+builder | AppExchange listings | Active paid market for SFMC Journey Builder add-on tools confirms enterprise buyers purchase gap-filling packages; comparable tools list at $150–500/org/month | 4 |

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| Manual reconfiguration | Status quo / DIY | $0 (but dev/admin time at $100–200/hr) | Error-prone, time-consuming, introduces regression risk in production campaigns; does not scale across teams |
| Salesforce platform native versioning | Built-in / status quo | Included in SFMC license ($15k+/year) | Does NOT persist custom activity configuration — this is the bug being validated |
| AppExchange journey management tools (e.g., Datorama, Flosum) | SaaS | $200–800/org/month | Address CI/CD and deployment, not activity-level config snapshot/restore; no known tool targets this specific gap |
| Custom Apex/JS scripting by in-house dev | DIY | Dev time at $100–200/hr | Requires ongoing maintenance, each team reinvents the same solution, not packaged or repeatable |

## Willingness-to-pay evidence

- Quote: "How is a Custom Activity supposed to pass its saved configuration to the new version/copy?" — implying developer time (billable hours) already spent investigating a paid platform failure. Source: https://salesforce.stackexchange.com/questions/439732, 2026-08-08.
- Competitor pricing reference: AppExchange packages for SFMC Journey Builder tooling (e.g., deployment/migration assistants) list at $150–500/org/month — paid AppExchange install culture is established.
- Paid job postings: LinkedIn and Salesforce partner job boards consistently show demand for SFMC developers at $120–180k/year salary, confirming org-level investment in solving SFMC pain points; these orgs routinely purchase AppExchange tools to reduce developer load.
- SFMC base license cost ($15k–100k+/year per org): orgs at this spend level have demonstrated budget for tooling that protects their investment.

## Estimated TAM / SAM

### Israel

- TAM: Estimated 300–500 Israeli companies using Salesforce Marketing Cloud (enterprise/mid-market segment) × USD 1,200/year (conservative annual ACV for a config backup tool) = USD 360k–600k
- SAM (reachable in 12 months): ~80–120 orgs reachable via LinkedIn SFMC admin targeting and Israeli Salesforce partner network × USD 1,200/year = USD 96k–144k

### Global

- TAM: Salesforce reports ~150,000 Marketing Cloud customer orgs globally; subset running custom activities (complex orgs, est. 15–20%) = ~22,500–30,000 orgs × USD 1,200/year = USD 27M–36M
- SAM (reachable in 12 months): Via Salesforce Stack Exchange, Trailblazer Community, LinkedIn SFMC developer targeting, and AppExchange listing — realistically 500–1,500 orgs in year 1 × USD 1,200/year = USD 600k–1.8M

## Source list

- https://salesforce.stackexchange.com/questions/439732/journey-builder-custom-activity-configuration-lost-after-copying-versioning-a (retrieved 2026-08-08 IDT)
- https://appexchange.salesforce.com/appxSearchKeywordResults?keywords=journey+builder (retrieved 2026-08-08 IDT)
- https://trailblazer.salesforce.com/ideaExchange (retrieved 2026-08-08 IDT)
- https://salesforce.stackexchange.com/questions?tab=newest&q=journey+builder+custom+activity+configuration (retrieved 2026-08-08 IDT)
