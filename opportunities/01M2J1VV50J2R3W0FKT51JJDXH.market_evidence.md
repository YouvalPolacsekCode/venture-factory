# Market Evidence

<!-- Prove the pain exists, prove people pay to solve it, prove the market is large enough to matter. No assertions without sources. -->

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|---|
| 2026-09-15 | https://salesforce.stackexchange.com/questions/439837/how-to-make-comments-mandatory-in-approval-process-upon-rejection | Forum question | Salesforce admin unable to enforce mandatory rejection comments despite trying documented Flow workaround; describes a business compliance requirement, not a hobbyist experiment | 2 |

**Evidence gap note:** Only one corroborating source was available at validation time. No Salesforce Trailblazer Community threads, AppExchange product reviews, or Reddit r/salesforce posts were located that independently confirm frequency or breadth of this problem.

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| Custom Salesforce Flow workaround | DIY / no-code | $0 (developer time only) | Brittle — breaks across Salesforce releases; requires Apex or Flow expertise; documented in the source post as not working reliably |
| Salesforce AppExchange compliance packages (e.g., Nintex, Conga) | SaaS | $3,000–$30,000/year | Full-suite overkill for a single mandatory-comment requirement; enterprise pricing excludes smaller orgs |
| Salesforce Professional Services / SI partners | Agency | $150–$300/hr | Works but expensive; ongoing maintenance not included |

## Willingness-to-pay evidence

- **Quote:** *(None located)* — The single source post describes the problem but contains no explicit statement of willingness to pay for a solution.
- **Competitor pricing reference:** No AppExchange product specifically targeting mandatory approval comments was identified. Broader compliance packages (Nintex, Conga) exist at $3,000–$30,000/year but are not direct comparables.
- **Paid job postings:** Not searched (requires approval action). Cannot confirm demand via this signal without outreach.

**Verdict:** Willingness-to-pay evidence does not meet the pass threshold (minimum 1 confirmed WTP signal required). The pain is plausible and the buyer has budget, but no hard WTP signal was found.

## Estimated TAM / SAM

### Israel
- TAM: Salesforce customer count in Israel is not publicly available. Estimated ~300–600 Israeli mid-market/enterprise Salesforce orgs using approval workflows × $500–$1,200/year for a narrow AppExchange micro-app = **~$150K–$720K**. Arithmetic is speculative without confirmed customer counts.
- SAM (reachable in 12 months): ~50–100 orgs reachable via Trailblazer Community and LinkedIn targeting.

### Global
- TAM: Salesforce reports ~150,000 customers globally; a subset using approval workflows in compliance-sensitive industries (procurement, HR, legal) estimated at 20,000–40,000 orgs × $600/year = **$12M–$24M** (highly speculative).
- SAM (reachable in 12 months): AppExchange listing discovery + targeted Trailblazer Community posts could reach 500–2,000 admins.

## Verdict

**REJECTED.** Evidence count: 1 (threshold: 5 distinct pain quotes). Willingness-to-pay signals: 0 (threshold: 1). Build gates fail: `buildability_with_ai = 3` (floor: 6), `operational_autonomy = 4` (floor: 7). The opportunity is not ready to promote. Recommend: re-queue Market Radar to scan Salesforce Trailblazer Community, AppExchange reviews, and r/salesforce for corroborating threads before reconsidering.

## Source list

- https://salesforce.stackexchange.com/questions/439837/how-to-make-comments-mandatory-in-approval-process-upon-rejection (retrieved 2026-09-15 IDT)
