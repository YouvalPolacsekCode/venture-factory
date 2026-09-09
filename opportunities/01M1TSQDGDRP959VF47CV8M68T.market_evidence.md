# Market Evidence

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|---|
| 2026-09-06 | https://serverfault.com/questions/1199776/how-to-get-user-read-all-permissions-in-microsoft-graph-to-be-seen-on-the-pc-end | ServerFault thread | Developer blocked on app-vs-delegated permission distinction for Teams Graph integration; multi-step failed attempts documented | 2 |
| N/A | https://stackoverflow.com/questions/tagged/microsoft-graph+permissions | SO tag search | ~12,000 questions tagged microsoft-graph+permissions on Stack Overflow, many concerning app-vs-delegated confusion | 3 |
| N/A | https://learn.microsoft.com/en-us/graph/permissions-overview | Microsoft Docs | Official docs run to thousands of words and distinguish 40+ permission scopes — complexity is structural and not resolved by docs alone | 2 |

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| Microsoft Graph Explorer | Free tool (Microsoft) | $0 | Shows permissions but does not explain which to use for a given goal or app-vs-delegated tradeoff |
| Microsoft Docs / Learn | Documentation | $0 | Comprehensive but dense; does not validate a specific configuration or generate a checklist |
| GitHub Copilot / ChatGPT | AI assistant | $10–$20/mo (general) | General-purpose; no Graph-specific validation or step-by-step checklist |
| Workato / Power Automate | Workflow automation SaaS | $200–$2,000+/mo | Abstracts the problem but does not educate or explain; overkill for a single integration task |

## Willingness-to-pay evidence

- No direct quote found of a developer willing to pay for a Graph permissions configurator as a standalone tool.
- Competitor pricing reference: No identified SaaS charges specifically for Microsoft Graph permission configuration advice. Adjacent tools (Workato, Postman) charge for broader API workflow automation, not permission scoping.
- Paid job postings: Microsoft Graph API integration roles appear regularly on LinkedIn and Indeed, confirming organizational spend on this work — but spend is on developer time, not a dedicated tool.

## Estimated TAM / SAM

### Israel

- TAM: ~2,000 Israeli companies using M365 with active developer/IT integration projects × USD 300/year = USD 600K (speculative; no Israel-specific data).
- SAM (reachable in 12 months): ~200 companies reachable via LinkedIn and developer community targeting.

### Global

- TAM: ~500,000 companies globally running M365 with custom Graph integrations × USD 300/year = USD 150M addressable in theory — but realistic capture is a fraction, and free alternatives suppress monetization.
- SAM (reachable in 12 months): Developer community (StackOverflow, ServerFault) reachable via answer-seeding; realistic paying conversion rate is very low given free alternatives.

## Source list

- https://serverfault.com/questions/1199776/how-to-get-user-read-all-permissions-in-microsoft-graph-to-be-seen-on-the-pc-end (retrieved 2026-09-06 IDT)
- https://stackoverflow.com/questions/tagged/microsoft-graph+permissions (retrieved 2026-09-06 IDT)
- https://learn.microsoft.com/en-us/graph/permissions-overview (retrieved 2026-09-06 IDT)

## Verdict

**REJECTED.** Pain exists and is frequent, but willingness-to-pay for a standalone configurator is unconfirmed. Free alternatives (Microsoft Docs, Graph Explorer, general AI assistants) address the same need without charging. No paid competitor validates the price point. Score 6.0 is below the 6.5 build threshold and WTP is at the floor (5). Do not promote. Re-queue if a paid competitor or direct WTP signal emerges.