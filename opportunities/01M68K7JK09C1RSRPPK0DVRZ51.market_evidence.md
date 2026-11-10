# Market Evidence

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|---|
| 2026-10-31 | https://serverfault.com/questions/1200165/what-does-free-for-up-to-100-000-requests-when-created-as-an-ai-gateway-in-azur | Forum question | A single production Azure customer unable to interpret AI Gateway billing footnotes before committing to a tier | 2 |

**Evidence gap:** No additional ServerFault, Stack Overflow, Reddit (r/AZURE, r/cloudcomputing), or Microsoft Tech Community threads found expressing the same confusion about AI Gateway vs. API Management tier pricing. The question has no upvotes or accepted answer recorded in the source snippet, indicating low community resonance.

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| Azure Pricing Calculator (official) | Free tool | $0 | Does not decode footnote logic or explain tier interactions in plain English |
| Infracost | Open-source / SaaS | Free–$50/mo | Does not cover Azure API Management or AI Foundry gateway tiers |
| Azure Cost Management | Built-in | $0 | Retrospective only; no pre-commitment estimator for new services |
| CloudHealth / Apptio Cloudability | Enterprise SaaS | $500+/mo | Overkill for single-service pricing question; no AI-gateway-specific coverage |

**Gap exists** but is narrow: no tool explains Azure AI Gateway footnotes in plain English. The gap is likely to be closed by Microsoft itself (documentation update) rather than a sustainable third-party product.

## Willingness-to-pay evidence

- Quote: *"I'm considering enabling AI Gateway… mainly to enforce monthly token quotas"* — ServerFault, 2026-10-31. Implied commercial context, not an explicit WTP statement.
- Competitor pricing reference: Infracost Cloud charges $0–$50/mo for IaC cost estimation; no Azure AI Gateway coverage confirmed.
- Paid job postings: 0 found for roles specifically managing Azure AI Gateway cost estimation.

**Verdict:** No hard WTP signal. No quote expressing willingness to pay a third party for pricing clarity. No competitor charging money for this specific service.

## Estimated TAM / SAM

### Israel
- TAM: Azure AI Foundry is in early adoption in Israel. Estimated <200 teams actively evaluating AI Gateway tiers × $200/year (one-time explainer or annual subscription) = **~USD 40K**. Not material.
- SAM (reachable in 12 months): ~50 teams actively in evaluation phase at any moment = **~USD 10K**.

### Global
- TAM: Rough estimate of 5,000 enterprise and mid-market teams globally actively evaluating Azure AI Gateway in 2026 × $200/year = **~USD 1M**. This ceiling is small and shrinks as Microsoft improves its own documentation.
- SAM (reachable in 12 months): Engineers actively in the Azure AI evaluation phase are timing-sensitive leads, not a stable directory-searchable audience. Reachable SAM is likely **<USD 200K** in year one.

## Source list

- https://serverfault.com/questions/1200165/what-does-free-for-up-to-100-000-requests-when-created-as-an-ai-gateway-in-azur (retrieved 2026-10-31 IDT)

---

**Verdict: FAIL.** Does not meet the minimum 5 distinct pain quotes. Zero hard WTP signal. TAM is too small and inherently self-correcting (Microsoft will update its docs). Recommend killing this candidate.