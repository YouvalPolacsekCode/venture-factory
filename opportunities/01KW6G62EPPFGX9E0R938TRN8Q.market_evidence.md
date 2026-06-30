# Market Evidence

<!-- Prove the pain exists, prove people pay to solve it, prove the market is large enough to matter. No assertions without sources. -->

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|---|
| 2026-06-28 | https://serverfault.com/questions/1199339/how-to-trace-azure-saas-model-deployment-costs-back-to-their-azure-ai-foundry-re | Forum question | Engineer deploying multiple Azure AI Foundry endpoints cannot attribute SaaS-type spend rows to individual Foundry resources in Cost Management UI | 3 |

**Evidence gap:** Only one confirmed signal found. The pain is structural (a known Azure Cost Management limitation for SaaS-type resources), but Reddit, HN, Microsoft Tech Community, and FinOps Foundation forums did not surface additional corroborating threads in available data. Minimum threshold of 5 distinct pain quotes is **not met**.

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| Azure Cost Management (native) | Built-in / free | $0 | Does not expose Foundry resource names for SaaS-type deployments; grouping stops at resource type, not resource instance |
| Apptio Cloudability | SaaS | ~$15,000–$60,000+/yr | General cloud cost allocation; no specific Azure AI Foundry / SaaS-type resource reconciliation module |
| CloudHealth by VMware | SaaS | ~$10,000–$50,000+/yr | Same gap — no AI Foundry-aware cost attribution |
| Custom Azure Policy + tagging | DIY | Engineering hours | Requires tagging at deployment time; does not retroactively fix SaaS-type billing records |
| Azure Monitor + Log Analytics | Built-in | Per-GB ingestion | Captures inference logs but does not link back to Cost Management billing rows |

## Willingness-to-pay evidence

- Quote: *"How to trace Azure SaaS model deployment costs back to their Azure AI Foundry resource?"* — ServerFault, 2026-06-28 (implies active search for a solution, but not a payment signal)
- Competitor pricing reference: Apptio Cloudability, enterprise tier ~$15,000–$60,000/yr (URL: https://www.apptio.com/products/cloudability/) — confirms FinOps teams pay for cost attribution tooling broadly, but no evidence they are specifically paying or requesting Azure AI Foundry attribution
- Paid job postings: Not found for this specific problem
- **WTP verdict:** Inferred only. No direct quote of someone paying or offering to pay for this specific gap. Minimum one hard WTP signal is **not met**.

## Estimated TAM / SAM

### Israel

- TAM: Israeli enterprises with meaningful Azure AI spend — estimated ~150–300 companies (large tech, finance, healthcare) × USD 600–1,200/yr = USD 90K–360K. Too small to anchor a standalone product.
- SAM (reachable in 12 months): ~30–60 companies via LinkedIn FinOps / Azure community outreach = USD 18K–72K ARR potential

### Global

- TAM: ~15,000 mid-to-large enterprises globally with Azure AI Foundry deployments (conservative; Azure has ~300,000 enterprise customers, AI Foundry is a small subset) × USD 600–1,200/yr = USD 9M–18M
- SAM (reachable in 12 months): FinOps Foundation membership (~10,000 practitioners), Azure community forums — realistically 200–500 paying customers = USD 120K–600K ARR if conversion is strong
- **Note:** TAM math is highly speculative; Azure AI Foundry adoption is early-stage and SaaS-type deployment penetration is unknown.

## Source list

- https://serverfault.com/questions/1199339/how-to-trace-azure-saas-model-deployment-costs-back-to-their-azure-ai-foundry-re (retrieved 2026-06-28 IDT)
- https://www.apptio.com/products/cloudability/ (background reference — not retrieved directly)
- https://www.vmware.com/products/cloudhealth.html (background reference — not retrieved directly)

---

## Verdict: REJECTED (this cycle)

**Reason:** Evidence threshold not met.
- Distinct pain quotes found: **1** (minimum required: 5) ✗
- Willingness-to-pay signal: **0 direct** (minimum required: 1) ✗
- Clear target audience: ✓

**Recommendation:** Re-queue for Market Radar re-scan in 60 days. The problem is structurally real, but the developer community surface area is currently too small to validate. Monitor Microsoft Tech Community, FinOps Foundation Slack threads, and Azure Feedback portal for accumulating signal. If Azure AI Foundry adoption accelerates (as expected), this will become a stronger candidate by Q4 2026.
