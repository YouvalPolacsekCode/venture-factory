# Market Evidence

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|---|
| 2026-08-13 | https://news.ycombinator.com/item?id=49281152 | HN thread | Users reporting 10/10 Claude API requests failing with HTTP 529; explicit paying-user context | 2 |

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| LiteLLM | Open-source / hosted SaaS | Free–$99+/mo | Requires self-hosting setup; feature-heavy for simple failover use case |
| Portkey | SaaS | $49–$499/mo | Targets enterprise; overkill for solo devs; pricing opaque |
| OpenRouter | API gateway | Usage-based | Not a true circuit-breaker; no alerting; limited fallback configurability |

## Willingness-to-pay evidence

- No direct quotes from users willing to pay for a failover proxy extracted from this thread.
- Competitor pricing reference: Portkey charges $49–$499/mo for multi-provider routing (portkey.ai/pricing); LiteLLM Cloud exists as a paid tier.
- Paid job postings: Not assessed — insufficient distinct evidence from a single thread.

## Estimated TAM / SAM

### Israel
- TAM: Estimated ~500 Israeli startups with Claude API in production × USD 300/year = USD 150K — too small to be primary market.
- SAM (reachable in 12 months): ~100 (via HN, AngelList Israel, local dev communities).

### Global
- TAM: ~50,000 companies with LLM API in production × USD 300/year = USD 15M (conservative; proxy/reliability tooling tier).
- SAM (reachable in 12 months): ~2,000 active HN/Reddit LLM developers reachable via public threads.

## Verdict

**REJECTED.** Single-source evidence (signal_strength 2), direct overlap with stronger candidate 01M06WXXM162JHE2W73JGX8JW1, and a saturated competitive landscape with well-funded incumbents. The narrower monitoring angle is better pursued under the dedicated monitoring candidate. Re-queue only if Market Radar surfaces 5+ independent corroborating signals.

## Source list

- https://news.ycombinator.com/item?id=49281152 (retrieved 2026-08-13 IDT)
