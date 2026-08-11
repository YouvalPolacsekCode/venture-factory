# Market Evidence

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|---|
| 2026-08-06 | https://news.ycombinator.com/item?id=27249443 | HN comment | Single practitioner expresses desire for semantic query analysis beyond timing metrics | 2 |

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| pganalyze | SaaS | $99–$399/mo | Focuses on performance metrics, not semantic intent |
| Datadog APM | SaaS | $200+/mo | Query timing and tracing, no semantic explanation layer |
| ChatGPT / Claude direct | DIY | $0–$20/mo | Free for most developers; no dedicated Postgres context but covers the core use case |
| GitHub Copilot Chat | DIY / SaaS | $10–$19/mo | Explains SQL inline in IDE; direct free substitute |

## Willingness-to-pay evidence

- Quote: "I use it frequently — but I wish there was a tool which went into the semantics somewhat." — HN commenter, 2026-08-06 (expresses desire, not payment intent)
- Competitor pricing reference: pganalyze, $99–$399/mo, https://pganalyze.com/pricing (pays for performance analytics, not semantic explanation)
- Paid job postings: No postings found for Postgres semantic analysis tooling specifically.

**Assessment:** Zero direct willingness-to-pay signals for a standalone semantic query analyzer. The single quote expresses a wish, not a purchase intent. Free substitutes (ChatGPT, Copilot) already satisfy this need at zero marginal cost for most developers. No competitor charges specifically for query semantic explanation — the nearest paid tools bundle it with monitoring.

## Estimated TAM / SAM

### Israel
- TAM: ~2,000 Israeli software companies running Postgres in production × $228/year (assumed low-friction $19/mo) = **USD 456K** — too small for a standalone product.
- SAM (reachable in 12 months): ~400 companies reachable via developer communities.

### Global
- TAM: ~500,000 companies running Postgres globally × $228/year = **USD 114M** theoretical, but free substitute availability compresses realistic SAM to a fraction.
- SAM (reachable in 12 months): Unknown — no evidence of a distinct, unserved buyer segment willing to pay over free LLM access.

## Source list

- https://news.ycombinator.com/item?id=27249443 (retrieved 2026-08-06 IDT)
- https://pganalyze.com/pricing (reference only)

## Verdict: REJECTED

**Reason:** Fails the minimum 5 distinct pain quotes threshold (only 1 found). Zero willingness-to-pay signals for a dedicated tool. Free LLM alternatives directly substitute the proposed value proposition. Do not advance.