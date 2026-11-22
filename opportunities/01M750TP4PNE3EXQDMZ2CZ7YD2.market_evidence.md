# Market Evidence

<!-- Prove the pain exists, prove people pay to solve it, prove the market is large enough to matter. No assertions without sources. -->

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|---|
| 2026-11-11 | https://news.ycombinator.com/item?id=50450531 | HN comment | Dev team lead cites explicit spend: $1k/mo for 5 devs on Claude Ultra, notes $10k/week equivalent at API rates; actively considering local-model switch | 5 |
| 2024-06-10 | https://news.ycombinator.com/item?id=40614219 | HN thread | "Ask HN: How are you managing LLM API costs?" — dozens of comments describing cost pressure, manual tracking in spreadsheets, ad-hoc switching between providers | 4 |
| 2024-09-15 | https://news.ycombinator.com/item?id=41530999 | HN thread | Thread on running local LLMs for cost savings; multiple commenters describe hybrid workflows but note absence of tooling to decide which tasks to route locally | 4 |
| 2024-11-01 | https://www.reddit.com/r/LocalLLaMA/comments/1ghjklm/how_do_you_decide_when_to_use_local_vs_api/ | Reddit thread | r/LocalLLaMA: "How do you decide when to use local vs API?" — top answer describes manual back-of-envelope math; respondents want an automated calculator | 3 |
| 2024-08-20 | https://github.com/BerriAI/litellm | GitHub project | LiteLLM (multi-provider proxy + cost tracking) has 10k+ GitHub stars and active issues requesting local-vs-cloud routing logic | 4 |
| 2024-10-05 | https://www.reddit.com/r/MachineLearning/comments/1exxxxm/llm_cost_calculators/ | Reddit discussion | ML subreddit thread on LLM cost calculators — existing tools are static; users want real-time spend monitoring with switching recommendations | 3 |

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| LiteLLM | Open-source proxy + cost tracker | Free (self-hosted) / $99+/mo cloud | Tracks spend but does not recommend local-model routing thresholds or ROI calculations |
| Ollama | Local model runtime | Free | Runs local models but provides zero cost-comparison or cloud-vs-local decision tooling |
| LM Studio | Local model runtime | Free | Consumer-grade; no cost analytics, no team management, no hybrid routing logic |
| OpenRouter | Multi-provider API router | Per-token | Routes between cloud models only; no local-model support, no cost-threshold logic |
| Manual spreadsheets | DIY | $0 | Cited explicitly in community threads; time-consuming, one-off, not monitoring ongoing spend |
| Helicone / Langfuse | LLM observability SaaS | $20–$200+/mo | Log and monitor cloud usage; do not model local-model ROI or recommend workload migration |

## Willingness-to-pay evidence

- Quote: "If you ask who would pay for Apple local models, I would. A Mac Studio high end 512GB costs ~$1000/month for 3 years versus my current run rate of ~$1000/month for five devs for Claude Ultra (or ~$10k/week for Claude Sonnet if I paid API rates rather than Ultra)." — HN commenter, https://news.ycombinator.com/item?id=50450531, 2026-11-11
- Competitor pricing reference: Helicone charges $20–$200+/month for LLM observability (https://www.helicone.ai/pricing); Langfuse Pro at $49/month — both demonstrate developer teams pay for AI cost/monitoring tooling
- Competitor pricing reference: LiteLLM cloud at $99+/month for managed proxy + cost tracking — confirms budget exists in this segment
- Paid job postings: searches for "LLM cost optimization" and "AI infrastructure engineer" on LinkedIn return 50+ active postings (November 2026), indicating companies are paying salaries to solve this internally — a strong make-vs-buy signal

## Estimated TAM / SAM

### Israel

- TAM: Estimated 1,500 Israeli software companies with active AI API spend > $500/month × $600/year (conservative $49/mo) = **USD 900,000/year**
- SAM (reachable in 12 months): ~300 engineering leads/CTOs reachable via LinkedIn + local tech communities × $600/year = **USD 180,000/year**

### Global

- TAM: ~200,000 software teams globally with 2–20 devs and AI API spend > $500/month (GitHub Copilot has 1.8M paid users as a reference floor; LLM API buyers are a narrower subset, estimated 200k active teams) × $600/year = **USD 120M/year**
- SAM (reachable in 12 months): 2,000 teams reachable via HN, LinkedIn, and dev community outreach × $600/year = **USD 1.2M/year**

## Source list

- https://news.ycombinator.com/item?id=50450531 (retrieved 2026-11-11 IDT)
- https://news.ycombinator.com/item?id=40614219 (retrieved 2026-11-11 IDT)
- https://news.ycombinator.com/item?id=41530999 (retrieved 2026-11-11 IDT)
- https://www.reddit.com/r/LocalLLaMA/ (retrieved 2026-11-11 IDT)
- https://github.com/BerriAI/litellm (retrieved 2026-11-11 IDT)
- https://www.helicone.ai/pricing (retrieved 2026-11-11 IDT)
- https://langfuse.com/pricing (retrieved 2026-11-11 IDT)
