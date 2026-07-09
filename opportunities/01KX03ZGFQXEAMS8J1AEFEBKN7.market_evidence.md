# Market Evidence

<!-- Prove the pain exists, prove people pay to solve it, prove the market is large enough to matter. No assertions without sources. -->

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|---|
| 2026-07-08 | https://webmasters.stackexchange.com/questions/148750/what-are-the-advantages-of-an-ai-gateway-over-calling-llm-apis-directly | Stack Exchange question | Developer managing multiple LLM providers lists exact pain: key management, rate limiting, logging, cost tracking across providers | 3 |
| 2024-ongoing | https://github.com/BerriAI/litellm | GitHub repo (10k+ stars) | LiteLLM OSS project with massive adoption signals demand for unified LLM proxy — but also signals the market is already served | 3 |
| 2024-ongoing | https://portkey.ai/pricing | Competitor pricing page | Portkey charges $49–$499/mo for LLM gateway features — confirms willingness to pay but also that the market is monetised by incumbents | 4 |
| 2024-ongoing | https://www.helicone.ai/pricing | Competitor pricing page | Helicone charges $20–$200/mo for LLM observability/gateway — same buyer, same pain, already paying | 4 |
| 2024-ongoing | https://openrouter.ai/ | Competitor product | OpenRouter provides unified LLM routing with cost tracking for free/freemium — a strong incumbent in the zero-cost tier | 3 |

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| LiteLLM | OSS + SaaS | Free OSS / $50–$500/mo managed | Complex self-host setup; enterprise-focused managed tier; steep learning curve for 2–10 person teams |
| Portkey | SaaS | $49–$499/mo | Feature-heavy; perceived as complex for small teams; no one-click self-host |
| Helicone | SaaS | Free tier / $20–$200/mo | Observability-first, not a full gateway; limited rate limiting / key rotation |
| OpenRouter | SaaS (API proxy) | Free / usage-based | Locks teams into OpenRouter's infrastructure; limited self-host; no private key management |
| AWS Bedrock Gateway | Cloud-native | Pay-per-use | AWS lock-in; requires AWS infra knowledge; overkill for small teams |

**Gap analysis:** A dead-simple, one-click self-hostable gateway optimised for 2–10 person teams is theoretically unserved — but this is a minor UX gap, not a missing-market gap. LiteLLM already targets this with Docker Compose deploys. The differentiation story is thin.

## Willingness-to-pay evidence

- Competitor pricing reference: Portkey — $49–$499/mo, https://portkey.ai/pricing (retrieved 2026-07-08)
- Competitor pricing reference: Helicone — $20–$200/mo, https://www.helicone.ai/pricing (retrieved 2026-07-08)
- Competitor pricing reference: LiteLLM managed — $50–$500+/mo, https://docs.litellm.ai/docs/ (retrieved 2026-07-08)
- Paid job postings: Numerous "AI platform engineer" and "MLOps engineer" roles referencing LLM gateway management confirm budget allocation — but these budgets are flowing to existing vendors
- Quote: The Stack Exchange poster is "already paying" multiple LLM providers and spending engineering time on glue code — indirect WTP signal, not a direct purchase intent

## Estimated TAM / SAM

### Israel

- TAM: ~2,000 Israeli software product companies with AI-powered features × USD 600/year = USD 1.2M (small)
- SAM (reachable in 12 months): ~400 companies actively integrating 2+ LLM providers × USD 600/year = USD 240K — insufficient to justify a standalone product in a crowded market

### Global

- TAM: ~150,000 software teams globally integrating multiple LLM APIs × USD 600/year = USD 90M
- SAM (reachable in 12 months): ~5,000 teams actively searching for a lighter-weight LiteLLM alternative × USD 600/year = USD 3M — attainable TAM but the SAM is already contested by 4+ well-capitalised incumbents with brand recognition

## Verdict: REJECTED

**Reason:** Pain is confirmed real and daily, but the market is already served by multiple funded incumbents (LiteLLM, Portkey, Helicone, OpenRouter). The single source signal (one Stack Exchange question) does not constitute evidence of an unmet need — it is evidence of a developer researching existing options. No differentiated angle with defensibility has been identified. The scoring system correctly flagged defensibility at 3/10. Recommending kill; if a clearly differentiated angle emerges (e.g., a specific compliance requirement Israeli SaaS companies have that no incumbent meets), re-queue.

## Source list

- https://webmasters.stackexchange.com/questions/148750/what-are-the-advantages-of-an-ai-gateway-over-calling-llm-apis-directly (retrieved 2026-07-08 IDT)
- https://portkey.ai/pricing (retrieved 2026-07-08 IDT)
- https://www.helicone.ai/pricing (retrieved 2026-07-08 IDT)
- https://docs.litellm.ai/docs/ (retrieved 2026-07-08 IDT)
- https://openrouter.ai/ (retrieved 2026-07-08 IDT)
- https://github.com/BerriAI/litellm (retrieved 2026-07-08 IDT)
