# Market Evidence

<!-- Opportunity: 01KY9A92AD5KPTAXDKSECC8XW3 — Salesforce managed package release-state CI/CD gate -->
<!-- Verdict: FAIL — insufficient distinct pain signals, no willingness-to-pay evidence, market too narrow -->

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|---|
| 2026-07-23 | https://salesforce.stackexchange.com/questions/439686/is-there-any-api-available-to-quickly-find-out-if-installed-package-version-is-r | Forum question | Developer building CI/CD pipeline needs runtime check of whether installed managed package version is released vs beta; calls Tooling API workaround "inefficient" | 3 |

**Evidence gap:** Only 1 distinct pain signal found. Pass threshold requires ≥5 distinct pain quotes from separate sources. Searches across Salesforce Stack Exchange, Trailblazer Community, GitHub Issues for sfdx/sf CLI, and HN produced no additional threads expressing this specific frustration with meaningful engagement.

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| Salesforce Tooling API (native) | Platform API / DIY | Free (included with org) | Requires iterating full released-version list; no single endpoint returns release state for an installed version ID; slow for CI/CD hot path |
| sfdx/sf CLI package commands | CLI / DIY | Free | No built-in flag to check release state of an installed version at pipeline runtime |
| CumulusCI | Open-source DevOps framework | Free (OSS) | General Salesforce CI/CD orchestration; does not expose a specific release-state gate check |
| Gearset / Copado | SaaS DevOps | $150–$500+/mo per user | Broad Salesforce deployment tooling; release-state gating for managed packages is not a documented feature |

## Willingness-to-pay evidence

- Quote: No public quotes found of anyone paying or expressing intent to pay for this specific capability.
- Competitor pricing reference: Gearset and Copado charge for broad Salesforce DevOps but do not market this feature; no niche tool found charging specifically for package release-state checks.
- Paid job postings: No job postings found requiring or describing this capability as a paid deliverable.

**WTP verdict:** Zero direct willingness-to-pay signals found. The adjacent market (Salesforce DevOps SaaS) does show spend, but it cannot be attributed to this specific sub-problem.

## Estimated TAM / SAM

### Israel

- TAM: Salesforce ISV companies based in Israel doing 2GP managed package development — estimated 20–40 companies (Salesforce Israel partner ecosystem is small). At $29–$49/mo per team = ~$35/mo avg × 30 teams × 12 = ~USD 12,600/year. Immaterial.
- SAM (reachable in 12 months): Likely ≤15 teams; revenue negligible.

### Global

- TAM: Salesforce AppExchange has ~7,000 listed apps; a subset (~1,500–2,000) are managed packages actively maintained by ISVs with CI/CD pipelines. Of those, perhaps 20–30% use 2GP (the context where this pain is acute) = ~400–600 teams. At $35/mo avg = 500 teams × $420/yr = ~USD 210,000/year maximum addressable.
- SAM (reachable in 12 months): 100–150 teams via Salesforce developer community outreach = ~USD 50,000–63,000/year.

**TAM is sub-$250K globally. Does not meet minimum bar for a standalone product.**

## Source list

- https://salesforce.stackexchange.com/questions/439686/is-there-any-api-available-to-quickly-find-out-if-installed-package-version-is-r (retrieved 2026-07-24 IDT)
- https://developer.salesforce.com/docs/atlas.en-us.sfdx_dev.meta/sfdx_dev/sfdx_dev_dev2gp.htm (Salesforce 2GP documentation — context only, retrieved 2026-07-24 IDT)
- https://appexchange.salesforce.com/appxStore?type=App (AppExchange browse — used for TAM estimation, retrieved 2026-07-24 IDT)

---
**Verdict: FAIL**
Does not meet evidence thresholds: 1/5 required pain quotes, 0/1 required willingness-to-pay signals, TAM <$250K globally. Recommend killing this candidate. Do not re-queue unless Market Radar surfaces ≥4 additional corroborating signals from separate sources.
