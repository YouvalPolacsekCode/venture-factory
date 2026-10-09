# Market Evidence

<!-- Prove the pain exists, prove people pay to solve it, prove the market is large enough to matter. No assertions without sources. -->

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|---|
| 2026-10-07 | https://salesforce.stackexchange.com/questions/439905/how-can-i-report-on-billable-flex-credit-consumption-per-user-for-agentforce-in | Stack Exchange question | Salesforce admin in sandbox evaluation cannot map token counts from GenAIGatewayRequest to Flex Credits for per-user cost forecasting before rollout | 3 |

**Evidence gap:** Only one primary source was available. The candidate was discovered on 2026-10-07 and the source URL is the sole signal. No corroborating Trailblazer Community threads, Reddit r/salesforce posts, LinkedIn complaints, or Salesforce IdeaExchange entries were identified through available context. Additional web_fetch calls to the following would be required to complete validation:
- https://trailhead.salesforce.com/trailblazer-community/feed (search: "Flex Credits" OR "Agentforce cost" OR "credit consumption reporting")
- https://ideas.salesforce.com (search: "Agentforce usage report" OR "Flex Credit dashboard")
- https://www.reddit.com/r/salesforce (search: "agentforce flex credits cost")
- https://news.ycombinator.com (search: "Agentforce credits")

These fetches were not executed in this cycle. Verdict is accordingly limited.

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| Salesforce native Lightning Reports (GenAIGatewayRequest object) | DIY / built-in | Included in Salesforce licensing | Does not expose usage_type, credit units, or a token-to-credit conversion; raw token counts only — confirmed by the source thread |
| Salesforce AI Agent Generation Log | DIY / built-in | Included in Salesforce licensing | Unclear whether it surfaces credit-level data; the source author was unsure if this is the right object — no definitive answer found |
| Generic BI tools (Tableau, Einstein Analytics) | SaaS | USD 70–3,000/user/year | Can query Salesforce objects but still depend on the same underlying data gap; do not know the token-to-credit mapping |
| Salesforce ISV managed packages (e.g., CloudKettle, Ceptive) | Managed package / agency | Unknown; typically USD 500–5,000+/year | No confirmed product found specifically addressing Agentforce Flex Credit per-user forecasting as of the candidate discovery date |
| Manual spreadsheet + Salesforce Support | DIY / status quo | Staff time only | Requires periodic exports and manual credit-rate application; not scalable for rollout forecasting |

**Gap exploited:** None of the above provides an automated, per-user, token-to-credit-translated consumption dashboard that finance and procurement can act on prior to a wider Agentforce rollout.

## Willingness-to-pay evidence

- **Quote:** No direct WTP quotes found in available evidence. The source author's context implies budget authority ("evaluating before wider rollout") but does not state they would pay for a third-party tool.
- **Competitor pricing reference:** No directly competing paid product was identified that prices this specific capability.
- **Paid job postings:** Not checked in this cycle (would require web_fetch to LinkedIn/Indeed with query "Salesforce Agentforce reporting" OR "Flex Credit dashboard").

**Assessment:** Willingness-to-pay evidence is **absent**. The scoring model awarded WTP a 6/10 based on inference (enterprise Salesforce orgs already pay for add-ons), but no hard proof — competitor pricing page, direct quote, or marketplace listing — was found. This is the single most critical missing signal. Per `config/pain_validation.yaml` requirements, at least one WTP signal is mandatory for a `pass` verdict.

## Estimated TAM / SAM

### Israel

- **TAM:** Salesforce's Israeli customer base is estimated at roughly 400–600 mid-to-large enterprise orgs (based on Salesforce's public EMEA market disclosures and Israel tech-sector density; no primary source verified in this cycle). If 20% evaluate or run Agentforce in the next 12 months ≈ 100 orgs × USD 600/year = **USD 60,000/year** (very small).
- **SAM (reachable in 12 months):** Perhaps 20–30 orgs reachable via Trailblazer Community Israel group or LinkedIn Salesforce Admin Israel network ≈ **USD 12,000–18,000/year**.

### Global

- **TAM:** Salesforce reports ~150,000 customers globally. Assuming 5% are mid-to-large enterprises evaluating Agentforce in the next 12 months ≈ 7,500 orgs × USD 600/year = **USD 4.5M/year**. (This is speculative; Agentforce adoption rate is early-stage as of 2026-10.)
- **SAM (reachable in 12 months):** Trailblazer Community has ~10M members; a realistic direct-reachable segment via community posts and Stack Exchange presence might be 500–1,000 orgs ≈ **USD 300,000–600,000/year**.

**Note:** TAM/SAM figures are illustrative estimates, not validated. The Israel SAM is below the threshold that would justify a standalone build.

## Verdict

**REJECTED (recommended: inconclusive → re-queue)**

This opportunity fails validation on two independent grounds:

1. **Insufficient pain evidence:** Only one primary source. The minimum threshold per `config/pain_validation.yaml` is 5 distinct pain quotes from independent sources. Current count: 1.
2. **No willingness-to-pay signal:** Zero competitor pricing references, zero direct quotes about paying for a solution, zero paid job postings verified.
3. **Build gate failure (non-evidence reason):** Even if pain were validated, the opportunity scores buildability_with_ai: 4 and operational_autonomy: 5 against floors of 6 and 7 respectively. Advancing would require contracting a Salesforce developer and ongoing maintenance tied to Salesforce's internal pricing table changes.

**Recommended next action:** Re-queue for Market Radar to surface additional Trailblazer Community and Reddit threads. If 4+ additional corroborating pain quotes are found in the next cycle, re-run Pain Validation with a web_fetch-heavy pass against Trailblazer Community, IdeaExchange, and Reddit. Do not advance to Lead Research until WTP signal and build-gate scores are resolved.

## Source list

- https://salesforce.stackexchange.com/questions/439905/how-can-i-report-on-billable-flex-credit-consumption-per-user-for-agentforce-in (retrieved 2026-10-07 IDT)
