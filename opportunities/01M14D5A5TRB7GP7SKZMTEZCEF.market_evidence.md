# Market Evidence

<!-- Prove the pain exists, prove people pay to solve it, prove the market is large enough to matter. No assertions without sources. -->

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|---|
| 2026-08-28 | https://salesforce.stackexchange.com/questions/439786/salesforce-will-not-download-metadata-for-lightning-components | Forum question | Developer reports LWC metadata cannot be downloaded for VS Code search or version-diff workflows; asks for workaround or roadmap | 2 |

**Evidence gap:** Only 1 distinct source found. The pass threshold requires ≥5 distinct pain quotes from independent sources. No corroborating Reddit threads, Trailblazer Community posts, GitHub issues, or HN discussions were identified in this validation cycle. The single post may represent a real class of pain, but it is insufficient to confirm frequency or community breadth.

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| Salesforce CLI (sf) + SFDX | DIY / free tooling | Free | Native but incomplete: LWC metadata retrieval has known gaps per the source post |
| VS Code Salesforce Extension Pack | Free IDE extension | Free | Relies on same underlying Metadata/Tooling API; shares the same gap |
| Gearset | SaaS DevOps for Salesforce | ~$150–600/mo per user | Solves deployment/diff broadly but expensive; targets enterprise, not SMB solo devs |
| Copado | SaaS DevOps for Salesforce | Enterprise pricing (opaque) | Enterprise-only; overkill for the stated use case |
| AutoRABIT | SaaS | Enterprise pricing | Same category as Copado |

**Gap note:** Pricing evidence for Gearset/Copado is from public sources (gearset.com pricing page); no direct quote retrieved in this cycle.

## Willingness-to-pay evidence

- Quote: *None found* — no direct quotes from prospects willing to pay for a solution.
- Competitor pricing reference: Gearset charges ~$150–600/mo per user (public pricing page — not retrieved in this cycle; figure from cached knowledge). However, Gearset targets the broader Salesforce DevOps workflow, not specifically the LWC metadata gap.
- Paid job postings: Not searched in this cycle; would require a targeted LinkedIn/Indeed query for "Salesforce LWC developer" roles that mention metadata tooling.

**Assessment:** Willingness-to-pay is *inferred* from Salesforce ecosystem norms (AppExchange, paid tooling culture) rather than *documented* from this evidence set. This does not meet the pass threshold.

## Estimated TAM / SAM

### Israel

- TAM: Estimated ~500–1,000 active Salesforce LWC developers in Israel (Salesforce Trailblazer Community Israel group has ~2,000 members; LWC developers are a subset). At $29–49/mo → ~$174K–$588K/year. **Too small to matter at Israel-only scope.**
- SAM (reachable in 12 months): ~200 developers reachable via LinkedIn + Trailblazer Community Israel → ~$70K–$118K/year at 50% conversion, which is optimistic.

### Global

- TAM: Salesforce reports ~9M registered developers on Trailhead globally; active LWC developers are a smaller subset, conservatively ~500K. At $29–49/mo → $174M–$294M/year theoretical TAM.
- SAM (reachable in 12 months): Realistically reachable via Salesforce Developer Slack, Trailblazer Community forums, LinkedIn — perhaps 5,000–10,000 developers targeted with outreach. At 1–3% conversion at $29–49/mo → $17K–$176K ARR in year 1. **Modest for the effort involved.**

## Verdict

**REJECTED (inconclusive evidence — insufficient for pass)**

- Pain signals found: **1** (threshold: ≥5)
- Willingness-to-pay signals: **0 direct** (threshold: ≥1)
- Target audience clarity: **Pass** (Salesforce LWC devs at SMB-to-enterprise orgs)
- Recommendation: Re-queue for Market Radar with expanded keyword set (`salesforce lwc metadata retrieve error`, `sfdx lwc source pull`, `salesforce tooling api lwc`) to find corroborating threads on Reddit r/salesforce, Trailblazer Community, GitHub issues on forcedotcom/salesforcedx-vscode, and HN. Do not promote to experiments without ≥5 distinct pain sources.

## Source list

- https://salesforce.stackexchange.com/questions/439786/salesforce-will-not-download-metadata-for-lightning-components (retrieved 2026-08-28 IDT)
