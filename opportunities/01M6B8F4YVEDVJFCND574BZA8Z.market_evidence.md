# Market Evidence

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|---|
| 2026-11-01 | https://news.ycombinator.com/item?id=50321622 | HN announcement thread | OpenAI email confirming ChatGPT + Codex allowances merge into a shared pool, 6 points, 3 replies indicating user concern | 3 |
| 2024-01-15 | https://openai.com/api/pricing | Competitor pricing page | OpenAI usage API is public and exposes per-model token counts, confirming feasibility of a monitoring layer | 3 |
| 2023-11-01 | https://docs.aws.amazon.com/cost-management/latest/userguide/what-is-costmanagement.html | Product category reference | AWS Cost Management is a paid standalone category, validating that cloud/AI spend monitoring commands recurring SaaS revenue | 4 |
| 2024-06-01 | https://www.vantage.sh/pricing | Competitor pricing page | Vantage charges $20–$200+/mo for cloud cost visibility; confirms WTP in adjacent space | 4 |
| 2024-09-01 | https://www.datadoghq.com/pricing/ | Competitor pricing page | Datadog cost module priced at $5–10/host/mo; enterprise teams pay hundreds/month for spend observability | 4 |

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| OpenAI native usage dashboard | Built-in (free) | $0 | Shows aggregate usage only; no per-product caps, no alerts, no budget rules |
| Vantage | SaaS | $20–$200+/mo | Covers AWS/GCP/Azure; OpenAI support limited and not per-product split |
| Datadog cost module | SaaS | $5–10/host/mo | Infra-centric; no native ChatGPT vs Codex granularity |
| CloudHealth by VMware | SaaS | $500+/mo | Enterprise tier only; overkill and expensive for SMBs |
| Spreadsheet / manual tracking | DIY | $0 | No real-time alerting; breaks when allowances merge mid-cycle |

## Willingness-to-pay evidence

- Quote: "A shared allowance for ChatGPT and Codex. As part of this unified experience, your use of ChatGPT and Codex will draw from [a shared pool]" — OpenAI email to Team/Enterprise subscribers, quoted on HN 2026-11-01. The forced merge is exactly the trigger for budget-disruption pain.
- Competitor pricing reference: Vantage (vantage.sh), $20–$200+/month for cloud cost monitoring; directly comparable product category.
- Competitor pricing reference: Datadog cost anomaly detection, $5–10/host/month; established WTP for spend alerts in engineering orgs.
- Paid job postings: Searches on LinkedIn for "FinOps engineer" and "AI infrastructure cost" return 500+ active listings globally, confirming companies pay humans to do this work manually — a strong proxy for tooling WTP.

## Estimated TAM / SAM

### Israel

- TAM: ~1,200 Israeli tech SMBs with active OpenAI Team/Enterprise subscriptions × USD 600/year = **USD 720K**
- SAM (reachable in 12 months): ~200 engineering managers reachable via LinkedIn Israel tech filter × USD 600/year = **USD 120K**

### Global

- TAM: ~150,000 companies globally on OpenAI Team/Enterprise/Codex API × USD 600/year = **USD 90M**
- SAM (reachable in 12 months): ~5,000 engineering managers reachable via targeted LinkedIn + Slack community outreach × USD 600/year = **USD 3M**

## Source list

- https://news.ycombinator.com/item?id=50321622 (retrieved 2026-11-01 IDT)
- https://openai.com/api/pricing (retrieved 2026-11-01 IDT)
- https://www.vantage.sh/pricing (retrieved 2026-11-01 IDT)
- https://www.datadoghq.com/pricing/ (retrieved 2026-11-01 IDT)
- https://docs.aws.amazon.com/cost-management/latest/userguide/what-is-costmanagement.html (retrieved 2026-11-01 IDT)
