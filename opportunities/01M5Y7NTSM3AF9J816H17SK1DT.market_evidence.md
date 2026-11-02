# Market Evidence

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|---|
| 2026-10-27 | https://github.com/TabularisDB/tabularis/issues/1292 | GitHub feature request | Engineer explicitly describes schema drift between dev/staging/prod as a workflow failure with production risk; requests built-in diff tooling | 3 |

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| Redgate SQL Compare | SaaS / desktop | $595–$1,995/year | Windows-centric, expensive for small teams, not integrated into DB GUI workflows |
| Bytebase | SaaS | $0–custom | Full platform requiring adoption of entire migration workflow; overkill for teams already using other tooling |
| Liquibase Pro | SaaS | $5,000+/year | Enterprise-priced, requires CLI adoption, steep learning curve |
| Manual inspection / scripts | DIY | $0 | Time-consuming, error-prone, no visibility into out-of-band changes |

## Willingness-to-pay evidence

- Competitor pricing reference: Redgate SQL Compare, $595–$1,995/year per license, https://www.red-gate.com/products/sql-development/sql-compare/
- Competitor pricing reference: Bytebase Team plan, $19/user/month, https://www.bytebase.com/pricing
- Competitor pricing reference: Liquibase Pro, $5,000+/year, https://www.liquibase.com/pricing
- Note: No direct "I would pay for this" quote found in the available signal; WTP is inferred from competitor revenues.

## Estimated TAM / SAM

### Israel
- TAM: ~500 product teams managing multi-environment PostgreSQL/MySQL deployments × $300/year = ~$150K (very small)
- SAM (reachable in 12 months): ~100 teams reachable via GitHub + dev communities

### Global
- TAM: ~200,000 product engineering teams globally × $300/year = ~$60M (paid tooling captures a fraction)
- SAM (reachable in 12 months): ~5,000 teams reachable via GitHub issues, dev.to, r/devops outreach

## Verdict: FAIL

**Evidence count:** 1 distinct pain source (below threshold of 5). **Build gates:** both `buildability_with_ai` (5) and `operational_autonomy` (5) are below floor values (6 and 7 respectively). The simplified paste-and-compare MVP does not deliver the core value the market pays for (live environment comparison). Recommend kill at this stage; re-queue only if Market Radar surfaces 4+ additional distinct pain signals from independent sources.

## Source list

- https://github.com/TabularisDB/tabularis/issues/1292 (retrieved 2026-10-27 IDT)
- https://www.red-gate.com/products/sql-development/sql-compare/ (referenced from opportunity notes)
- https://www.bytebase.com/pricing (referenced from opportunity notes)
- https://www.liquibase.com/pricing (referenced from opportunity notes)
