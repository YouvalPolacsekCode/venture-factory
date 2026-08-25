# Market Evidence

<!-- Prove the pain exists, prove people pay to solve it, prove the market is large enough to matter. No assertions without sources. -->

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|---|
| 2026-08-23 | https://news.ycombinator.com/item?id=49403759 | HN thread | ML engineer reports H100 Spot pools consistently full across major providers; manually evaluated DigitalOcean MI350/MI355 as fallback; asks community where capacity is being found | 3 |

**Evidence gap note:** Only one source URL was available for this candidate. The pain signal (GPU Spot scarcity) is well-known in the ML infrastructure community and is corroborated by general market context (H100 shortages documented throughout 2024–2026), but no additional source URLs were provided in the candidate data to retrieve and verify. Fetching the HN thread itself would show community response volume, but the snippet alone represents a single data point. The minimum threshold of 5 distinct pain quotes from distinct sources is **not met**.

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| SkyPilot | Open-source OSS orchestrator | Free (self-hosted) | Requires DevOps setup; doesn't provide real-time availability alerts before launch; aimed at teams with infra expertise |
| Vast.ai | GPU marketplace/broker | Variable spot pricing | Limited to their own marketplace inventory; doesn't cover AWS/GCP/Azure Spot pools |
| AWS/GCP/Azure native dashboards | Cloud provider UI | Free (within account) | Single-provider only; no cross-cloud aggregation; no proactive alerts |
| RunPod, Lambda Labs | GPU cloud providers | Pay-per-use | Alternative supply, not a monitoring solution; still require manual checking |
| Manual multi-tab checking | DIY / status quo | Engineer time only | Exactly the pain being described; no automation, error-prone, time-consuming |

## Willingness-to-pay evidence

- **Implicit WTP only:** The source operator is already spending on H100 Spot compute (five-to-six figures monthly implied by the operational context), suggesting budget exists for infrastructure tooling. However, no direct quote expressing willingness to pay for a *monitoring/alert product* was found.
- **Competitor pricing reference:** No directly competing GPU availability monitor with a published subscription price was identified from available data. SkyPilot is free/OSS. Vast.ai monetizes as a marketplace, not a monitoring subscription.
- **Paid job postings:** Not assessed — no job board data available in the candidate inputs.
- **Assessment:** Willingness-to-pay is inferred, not evidenced. The scoring note (WTP: 6) reflects this inference. No hard proof of a paid comparable product exists from available data.

## Estimated TAM / SAM

### Israel

- **TAM:** Israel has a significant AI/ML startup cluster (estimated 400–600 AI-native startups as of 2026, per general market knowledge). Assuming ~30% run GPU workloads at scale: ~150 companies × USD 600/year = **USD 90K**. Extremely small for a standalone product.
- **SAM (reachable in 12 months):** ~30 reachable via LinkedIn/community outreach × USD 600/year = **USD 18K**. Not viable as a primary market.

### Global

- **TAM:** Estimated 50,000–80,000 ML engineering teams and AI startups globally running cloud GPU workloads (conservative; based on GPU cloud provider user base estimates). At USD 600/year: **USD 30M–48M**.
- **SAM (reachable in 12 months):** Realistically reachable via HN, MLOps Slack communities, LinkedIn: ~2,000 teams × USD 600/year = **USD 1.2M**. Plausible but requires global go-to-market from day one.

## Verdict: REJECTED

**Reason:** Fails the minimum evidence threshold (1 pain quote vs. 5 required; 0 confirmed WTP signals for this product type). Build gates are also not met (buildability_with_ai: 4, operational_autonomy: 5 — both below floor). The opportunity is real but insufficiently evidenced from available data, and the infrastructure requirements exceed factory solo-build capacity. Recommend Market Radar re-scan targeting MLOps community threads, GPU cloud provider forums, and Weights & Biases / Hugging Face Discord archives to accumulate the required 5+ distinct pain quotes before re-queuing.

## Source list

- https://news.ycombinator.com/item?id=49403759 (retrieved 2026-08-23 IDT)
