# Market Evidence

<!-- Prove the pain exists, prove people pay to solve it, prove the market is large enough to matter. No assertions without sources. -->

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|---|
| 2026-06-25 | https://news.ycombinator.com/item?id=48669496 | HN practitioner thread | Engineers discuss that token savings in the first 25% of a 40-turn loop produce disproportionate gains; multiple commenters corroborate the difficulty of measuring per-phase spend | 3 |
| 2026-06-25 | https://dev.to/arpitstack/we-had-6-features-2-were-eating-our-budget-2bph | Dev blog post | Startup burning $4,200/month with no visibility into which features or loop phases drove cost; built internal tooling to fix it | 4 |

**Verdict note:** Only 2 distinct sources located. Minimum threshold is 5 distinct pain quotes. Signal count is insufficient for a `pass` verdict.

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| Helicone | SaaS LLM proxy/observability | Free–$200/month | Tracks request-level token counts but does not model multi-turn loop phases or attribute cost to loop stage | 
| LangSmith (LangChain) | SaaS tracing | Free–$49/month | Traces chain steps but no cost-per-phase budgeting or early-exit recommendations |
| Langfuse | Open-source / SaaS | Free–$59/month | Similar to LangSmith; no agentic loop phase profiling |
| Manual logging | DIY | Engineering time only | What the dev.to author did; high setup cost, not generalized |
| Status quo (no measurement) | Status quo | $0 tool cost, unknown waste | Most teams; burn is invisible until it's painful |

## Willingness-to-pay evidence

- Quote: "Turns saved in first 25% of an otherwise 40 turn loop can produce significant gains" — HN commenter, 2026-06-25, https://news.ycombinator.com/item?id=48669496 (practitioner insight, not a direct WTP signal)
- Quote: "Twelve months ago we were burning $4,200/month on AI infrastructure and could not tell you which features were responsible" — dev.to author, 2026-06-25 (built internal tooling = implicit WTP, but not a paid external tool)
- Competitor pricing reference: Helicone Pro $200/month (observability category validated), https://helicone.ai/pricing
- Competitor pricing reference: LangSmith $49/month, https://smith.langchain.com/pricing
- Paid job postings: Not located for this specific problem slice (loop-phase profiling is too narrow to appear as a distinct job category)

**Gap:** No direct quote of someone paying for a loop-phase-specific tool, no "is there a tool that profiles my agentic loop turns?" request found, no marketplace listing for this. One WTP anchor found (competitor category pricing), which is below the minimum of 1 credible WTP signal referencing this specific problem.

## Estimated TAM / SAM

### Israel

- TAM: Approximately 400 Israeli AI-native startups with active LLM API spend (estimate based on Start-Up Nation Central database size) × USD 600/year = USD 240K — too small to justify a standalone product at Israeli scale
- SAM (reachable in 12 months): ~80 startups running production agentic loops × USD 600/year = USD 48K

### Global

- TAM: ~50,000 teams globally running production agentic workflows on LLM APIs × USD 600/year = USD 30M — plausible but the loop-phase profiling slice is a subset of the broader LLM observability market (estimated $500M+ TAM), meaning addressable share is much smaller
- SAM (reachable in 12 months): ~2,000 AI-native startups reachable via HN/Slack communities × USD 600/year = USD 1.2M

## Source list

- https://news.ycombinator.com/item?id=48669496 (retrieved 2026-06-25 IDT)
- https://dev.to/arpitstack/we-had-6-features-2-were-eating-our-budget-2bph (retrieved 2026-06-25 IDT)
- https://helicone.ai/pricing (retrieved 2026-06-25 IDT)
- https://smith.langchain.com/pricing (retrieved 2026-06-25 IDT)
- https://langfuse.com/pricing (retrieved 2026-06-25 IDT)

---

## Verdict: REJECTED

**Reason:** Evidence count below threshold (2 sources vs. minimum 5 distinct pain quotes). Single willingness-to-pay signal is categorical (competitor pricing), not specific to loop-phase profiling. Integration complexity confirmed by scoring (buildability 5/10, below build gate floor of 6). Recommend re-queuing for Market Radar with a broader search query targeting "agentic loop cost" and "AI agent budget control" to see if a larger evidence base surfaces. If it does, re-evaluate as a feature of the broader cost-attribution opportunity (01KVYR5SFSS1ZS0GVNHJ0DCQZB) rather than a standalone product.
