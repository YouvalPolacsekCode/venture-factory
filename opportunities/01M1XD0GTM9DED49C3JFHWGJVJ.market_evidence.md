# Market Evidence

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|---|
| 2026-09-07 | https://serverfault.com/questions/1199776/how-to-send-a-teams-message-from-ms-graph-when-i-cant-get-user-read-all-and-ch | Forum post | Developer unable to send Teams messages via Graph after hours of permission debugging; describes it as 'a bit of a ride' | 2 |
| 2026-09-07 | https://stackoverflow.com/questions/tagged/microsoft-graph+teams | Stack Overflow tag | 1,400+ questions tagged microsoft-graph+teams; top questions repeatedly involve permission scope confusion (app-only vs delegated, consent flows) | 3 |
| 2026-09-07 | https://github.com/microsoftgraph/microsoft-graph-docs/issues | GitHub Issues | Recurring open issues on MS Graph docs repo flagging undocumented permission requirements for Teams chat endpoints; multiple commenters confirm same confusion | 3 |
| 2026-09-07 | https://learn.microsoft.com/en-us/graph/permissions-reference | Official docs | MS Graph permission reference is 200+ scopes with no clear 'for Teams message sending, use X' decision tree; structural gap that forces trial-and-error | 2 |
| 2026-09-07 | https://developer.microsoft.com/en-us/graph/changelog | Changelog | Permission requirement changes for Teams endpoints shipped with minimal notice in 2024–2025, repeatedly invalidating existing implementations | 2 |

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| Microsoft official docs (learn.microsoft.com) | Free documentation | Free | Comprehensive but not task-oriented; no 'I want to do X, here's the exact scope' lookup; frequently out of date on Teams-specific permissions |
| Stack Overflow / ServerFault community | Free Q&A | Free | Answers are fragmented, often version-stale, and require developer to synthesize across multiple threads |
| Microsoft Graph Explorer | Free interactive tool | Free | Good for testing calls but does not explain permission selection or consent flow decisions |
| Power Automate | SaaS automation platform | $15–$40/user/month | Solves end-to-end workflow automation, not the narrow permission-debugging pain; overkill and expensive for simple Teams notification use cases |
| Workato / Zapier | SaaS iPaaS | $300–$1,500+/month | Same as above — workflow platforms, not Graph permission reference tools; pricing far above what a permission guide would command |
| GitHub Copilot / ChatGPT | AI coding assistant | $10–$19/month | Already provides inline permission suggestions and code snippets in editor; most developers with this pain already have access to these tools |

## Willingness-to-pay evidence

- **No direct quotes found** of developers stating they would pay for a standalone Graph permission guide or troubleshooter.
- **Competitor pricing reference:** Power Automate ($15–$40/user/month) and Workato ($300+/month) are paid, but they solve a broader problem (full workflow automation) — not a validated proxy for paying for permission documentation specifically.
- **Paid job postings:** Searches for 'Microsoft Graph developer' job listings confirm the skill is in demand, but this reflects employer spend on engineers, not on tooling for this narrow pain.
- **Critical gap:** The most common resolution path observed across Stack Overflow and GitHub threads is a community answer or a free blog post — not a purchase. No evidence of developers expressing frustration that the free resources are insufficient AND that they would pay for better ones.

## Estimated TAM / SAM

### Israel

- TAM: Estimated 3,000–5,000 Israeli developers working in enterprises with Microsoft 365 + Teams environments; at $29/month, TAM ≈ USD 1.0–1.7M/year — too small to be material.
- SAM (reachable in 12 months): ~500 developers actively working on Teams automation, reachable via LinkedIn and local tech communities. At realistic conversion rates (1–3%), this is 5–15 paying customers.

### Global

- TAM: ~2M enterprise developers globally working with Microsoft 365 APIs; however, the addressable subset experiencing this specific pain and willing to pay (rather than use free resources) is likely <0.5% = ~10,000 developers x $29/month = USD 3.5M/year theoretical ceiling.
- SAM (reachable in 12 months): Developer communities (Stack Overflow, ServerFault, Dev.to) provide reach, but conversion from free-resource-seekers to paying customers for documentation tooling is historically very low (<0.1%). Realistic SAM: USD 100K–300K/year if conversion holds.

## Verdict: REJECTED

The pain is real and frequent, but the willingness-to-pay bar is not met. Free alternatives (Stack Overflow, GitHub Copilot, official docs) already address this pain at zero cost, and no evidence was found of developers paying — or expressing intent to pay — for a dedicated permission guide. The 5-distinct-pain-quote threshold is met, but the single willingness-to-pay signal requirement is not: no competitor is charging specifically for Graph permission documentation, no developers are asking 'is there a paid tool for this,' and the workaround (free community answers) is already adequate for most. Recommend killing this candidate. If the Market Radar surfaces stronger WTP signals (e.g., enterprise IT procurement teams expressing budget for MS Graph tooling beyond Power Automate), re-evaluate.

## Source list

- https://serverfault.com/questions/1199776/how-to-send-a-teams-message-from-ms-graph-when-i-cant-get-user-read-all-and-ch (retrieved 2026-09-07 IDT)
- https://stackoverflow.com/questions/tagged/microsoft-graph+teams (retrieved 2026-09-07 IDT)
- https://github.com/microsoftgraph/microsoft-graph-docs/issues (retrieved 2026-09-07 IDT)
- https://learn.microsoft.com/en-us/graph/permissions-reference (retrieved 2026-09-07 IDT)
- https://developer.microsoft.com/en-us/graph/changelog (retrieved 2026-09-07 IDT)
- https://powerautomate.microsoft.com/en-us/pricing/ (retrieved 2026-09-07 IDT)
