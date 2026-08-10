# Market Evidence

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|---|
| 2026-08-05 | https://salesforce.stackexchange.com/questions/439723/creating-a-pde-with-an-orgs-metadata | Forum question | ISV developer blocked by dependency errors when migrating managed package metadata to a PDE; describes manually resolving component sequencing | 2 |

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| Gearset | SaaS deployment tool | ~$150+/user/month | Handles CI/CD and metadata deployment diffs but does not specifically solve namespace-boundary dependency sequencing for managed package migrations |
| Salesforce CLI (sf) | Free tool | $0 | No automated dependency detection or sequencing; errors are surfaced only at deploy time with cryptic messages |
| Manual process | DIY / status quo | Dev time only | Error-prone, hours wasted per migration; no tooling assistance |

## Willingness-to-pay evidence

- Competitor pricing reference: Gearset charges ~$150+/user/month for Salesforce metadata deployment tooling, confirming this buyer segment pays for developer tooling — but no direct WTP signal for this specific migration sub-problem exists.
- Paid job postings: No job postings found specifically for managed package migration tooling expertise.
- Direct quotes: No quotes found expressing desire to pay for a solution to this specific problem.

## Estimated TAM / SAM

### Israel
- TAM: Estimated <50 Israeli Salesforce ISVs on AppExchange × $600–1,200/year = ~$30K–60K — insufficient to matter.
- SAM (reachable in 12 months): <20 qualifying companies.

### Global
- TAM: ~10,000 AppExchange partners globally × assumed 20% facing this migration problem × $600/year = ~$1.2M. Very narrow.
- SAM (reachable in 12 months): ~500–1,000 ISVs who have migrated or are migrating; reachable via Salesforce Partner Community and SFDC forums.

## Source list

- https://salesforce.stackexchange.com/questions/439723/creating-a-pde-with-an-orgs-metadata (retrieved 2026-08-05 IDT)

---
**Verdict: FAIL** — Only 1 pain signal found (minimum 5 required). No direct willingness-to-pay evidence for this specific problem. TAM too narrow for a standalone product. Recommend dropping this candidate; revisit only if Market Radar surfaces 4+ additional corroborating threads.