# Market Evidence

<!-- Prove the pain exists, prove people pay to solve it, prove the market is large enough to matter. No assertions without sources. -->

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|---|
| 2026-08-29 | https://salesforce.stackexchange.com/questions/439789/custom-fields-deployed-successfully-to-scratch-org-but-missing-from-runtime-sche | Stack Exchange Q&A | Developer documents a reproducible bug where deployed custom fields appear in metadata APIs but are absent from runtime schema, causing Apex compilation failures; manually-created fields work fine | 3 |

**Evidence gap:** The pass bar requires ≥5 distinct pain quotes from separate sources. Only one source was available for this cycle. Four additional corroborating threads (Trailblazer Community, Salesforce Developer Slack archives, GitHub issues on salesforce/cli or CumulusCI, or additional Stack Exchange/Stack Overflow threads) are needed before this opportunity can be promoted.

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| Gearset | SaaS CI/CD for Salesforce | USD 175–500/mo per user | Full deployment pipeline tool; does not specifically surface runtime schema mismatches post-deploy with plain-language diagnosis |
| Copado | SaaS DevOps platform | USD 300–600/mo per user | Enterprise-focused; expensive for small agencies/ISVs; same gap on runtime vs metadata reconciliation |
| Salesforce CLI (sf deploy validate) | CLI / open-source | Free | Validates metadata structure but does not compare deployed state against EntityParticle/runtime schema |
| Manual debugging (Setup UI, Workbench, SOQL on EntityParticle) | DIY | Developer time ($100–200/hr) | No automation; requires developer expertise to know which APIs to compare |

## Willingness-to-pay evidence

- **Competitor pricing reference:** Gearset charges USD 175–500/user/month and has raised significant venture funding, demonstrating the Salesforce developer tooling market does pay for deployment automation — but this is a market-level signal, not pain-specific. URL: https://gearset.com/pricing (not directly fetched this cycle).
- **Competitor pricing reference:** Copado charges USD 300–600/user/month for enterprise DevOps pipelines. URL: https://copado.com/pricing (not directly fetched this cycle).
- **Direct quote (from source):** *"A field created manually through Setup → New Field appears immediately"* — implies the developer spent meaningful time isolating the bug and would value a tool that surfaces it instantly.
- **Gap:** No direct quote of the form "I would pay for a tool that catches this" or "is there a product that..." was found. Paid job postings for this specific workflow were not located. This is the critical missing willingness-to-pay signal.

## Estimated TAM / SAM

### Israel

- **TAM:** Salesforce has ~200,000 certified developers worldwide (Salesforce Trailhead data); Israel accounts for roughly 0.5–1% of the global Salesforce developer population, suggesting ~1,000–2,000 Israeli Salesforce developers and a smaller number of ISV/agency shops. At USD 49–99/mo per seat: 500 addressable Israeli devs × USD 600/yr = **~USD 300K**.
- **SAM (reachable in 12 months):** Israeli Salesforce User Group attendees + LinkedIn Salesforce developers in IL = ~150 contacts × USD 600/yr = **~USD 90K**. Too small to be a primary market; Israel is a validation sandbox, not the revenue story.

### Global

- **TAM:** ~200,000 Salesforce developers globally × 15% using scratch orgs regularly (DX adoption estimate) = 30,000 potential users × USD 600/yr = **~USD 18M**.
- **SAM (reachable in 12 months):** Salesforce Stack Exchange active users (~8,000) + Trailblazer Community DevOps groups + Ohana Slack members reachable via approved outreach = ~2,000 contacts × 5% conversion × USD 600/yr = **~USD 60K ARR in year 1** — modest but meaningful as a wedge.

**Note:** TAM math is plausible but rests on scratch-org adoption estimates that are unverified. A single survey of the Trailblazer Community (requires approval) could sharpen this significantly.

## Verdict

**REJECTED (inconclusive — insufficient evidence, re-queue)**

The pain is mechanically credible and the buyer is well-defined, but the evidence base fails the minimum threshold:
- ✗ Distinct pain quotes from ≥5 separate users: **1 found, 4 needed**
- ✗ Willingness-to-pay signal specific to this problem: **0 found** (adjacent market spend only)
- ✓ Clear target audience: Salesforce developers and ISV partners on DX/scratch orgs
- ✓ Competitor market exists (Gearset, Copado) proving the broader tooling market pays

**Recommended next action:** Re-queue for Market Radar to find corroborating threads on Trailblazer Community, GitHub salesforce/cli issues, and Salesforce Stack Overflow. If 4+ additional pain quotes surface, re-run Pain Validation.

## Source list

- https://salesforce.stackexchange.com/questions/439789/custom-fields-deployed-successfully-to-scratch-org-but-missing-from-runtime-sche (retrieved 2026-08-29 IDT)
