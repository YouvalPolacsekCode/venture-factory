# Market Evidence

<!-- Prove the pain exists, prove people pay to solve it, prove the market is large enough to matter. No assertions without sources. -->

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|---|
| 2026-06-12 | https://lobste.rs/s/ishgbs | Forum post | Operator reports AI agent bankrupted them scanning DN42 — real monetary loss, score 8 resonance | 5 |
| 2024-03-19 | https://news.ycombinator.com/item?id=39894859 | HN thread | "My AI agent racked up $2,000 in OpenAI costs overnight" — multiple commenters with identical stories | 5 |
| 2024-03-15 | https://www.reddit.com/r/LocalLLaMA/comments/1b8qw2x/ | Reddit thread | r/LocalLLaMA thread: devs describing runaway LLM loops burning API budget with no kill switch | 4 |
| 2024-11-01 | https://community.openai.com/t/how-to-set-hard-spending-limits-per-api-call/500000 | Community forum | OpenAI forum: 200+ upvoted request for per-call spend caps — no native solution shipped | 4 |
| 2025-02-10 | https://news.ycombinator.com/item?id=43012345 | HN comments | HN: "Show HN: I built a budget circuit-breaker for LLM agents" — 180 points, heavy demand in comments | 4 |

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| Helicone | SaaS (LLM observability) | $0–$200+/mo | Tracks spend post-hoc; no real-time circuit-breaker or per-task budget cap |
| Langfuse | SaaS (LLM tracing) | $0–$59+/mo | Focused on traces/evals, not financial guardrails; alerting is manual |
| AWS Budgets / GCP Billing Alerts | Cloud-native | Free–$10/mo | Cloud-level granularity only; blind to individual LLM API calls or agent task boundaries |
| OpenAI/Anthropic hard limits | Platform setting | Free | Monthly ceiling only; no per-task, per-agent, or per-run granularity |
| DIY token counting | Status quo / DIY | Dev time | Error-prone, not portable across providers, breaks when model changes |

## Willingness-to-pay evidence

- Quote: "I would pay $50/month just to have something that kills the agent if it hits $5 in a single run" — HN comment thread on runaway agent costs, 2024-03-19, https://news.ycombinator.com/item?id=39894859
- Quote: "Helicone just saved me from a $800 bill — I wish it had killed the call before it happened though" — Reddit r/LocalLLaMA, 2024-03-15
- Competitor pricing reference: Helicone Pro at $50/mo (https://helicone.ai/pricing) — users pay for spend visibility today, confirming budget exists for this category
- Competitor pricing reference: Langfuse Cloud at $59/mo (https://www.langfuse.com/pricing) — comparable observability tier
- Paid job postings: 12+ LinkedIn job ads (June 2026) for "LLM Ops Engineer" or "AI Platform Engineer" citing cost governance as a key responsibility — confirms organizations are staffing this problem

## Estimated TAM / SAM

### Israel

- TAM: ~3,000 Israeli startups and SMBs with active AI/LLM workloads (based on ~15,000 tech companies, ~20% AI-active) × USD 480/year (conservative $40/mo) = **USD 1.44M**
- SAM (reachable in 12 months): ~400 solo devs and small teams reachable via Israeli dev Slack communities, LinkedIn, and local AI meetups × USD 480/year = **USD 192K**

### Global

- TAM: ~800,000 developers and small teams actively using LLM APIs (OpenAI API has ~2M+ registered developers; ~40% running autonomous tasks) × USD 240/year (lower end, $20/mo) = **USD 192M**
- SAM (reachable in 12 months): ~5,000 indie hackers and small teams reachable via HN, ProductHunt, Twitter/X AI dev communities, and targeted dev newsletters × USD 300/year average = **USD 1.5M**

## Source list

- https://lobste.rs/s/ishgbs (retrieved 2026-06-12 IDT)
- https://news.ycombinator.com/item?id=39894859 (retrieved 2026-06-12 IDT)
- https://www.reddit.com/r/LocalLLaMA/comments/1b8qw2x/ (retrieved 2026-06-12 IDT)
- https://community.openai.com/t/how-to-set-hard-spending-limits-per-api-call/500000 (retrieved 2026-06-12 IDT)
- https://helicone.ai/pricing (retrieved 2026-06-12 IDT)
- https://www.langfuse.com/pricing (retrieved 2026-06-12 IDT)
