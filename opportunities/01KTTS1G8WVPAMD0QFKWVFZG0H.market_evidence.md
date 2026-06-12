# Market Evidence

<!-- Prove the pain exists, prove people pay to solve it, prove the market is large enough to matter. No assertions without sources. -->

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|
| 2026-06-11 | https://dev.to/thegdsks/the-portfolio-math-when-30-small-apps-beat-1-big-one-41ai | Dev.to article | Author argues a portfolio of 30 small apps beats 1 big one; low engagement (score 22, 3 comments) suggests limited community resonance. No comments specifically request a unified dashboard tool. | 2 |

**Evidence gap:** The bar for `pass` requires ≥5 distinct pain quotes from ≥2 independent sources. Only 1 source was available at validation time. web_fetch of the dev.to thread confirmed the low comment count; no adjacent HN, Reddit r/indiehackers, or IndieHackers.com threads with high-engagement complaints about multi-product dashboard fragmentation were surfaced during this cycle.

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|
| Makerlog | Community / activity tracker | Free / $0 | No revenue aggregation; task-log focus only; not a metrics dashboard |
| IndieHackers product pages | Community profile | Free | Manual self-reporting; no live Stripe/Paddle data pull |
| Baremetrics / ChartMogul | SaaS analytics | $50–$300/mo per Stripe account | Designed for single-product; multi-account view is enterprise-tier or unsupported |
| Personal spreadsheet (Excel/Notion) | DIY | $0–$15/mo | Friction to maintain; no automation; no cross-promotion scheduling |
| Pirsch / Plausible | Web analytics | $10–$19/mo per site | Traffic only; no revenue layer; no cross-product view |

**Observation:** Existing alternatives are either community-social (Makerlog, IH) or single-product analytics (Baremetrics, Plausible). The multi-product aggregation gap is real, but no competitor has yet charged and won customers specifically on this pitch—which could mean the market doesn't value it enough to pay, or the opportunity is early.

## Willingness-to-pay evidence

- Quote: **None found.** No direct quotes from indie hackers expressing intent to pay for a unified portfolio dashboard were located in the single available source or adjacent public threads reachable without authentication.
- Competitor pricing reference: Baremetrics charges ~$129/mo for a single Stripe account; no competitor specifically targets the multi-product indie-hacker segment at a discovered price point.
- Paid job postings: 0 confirmed. No job ads requesting "indie hacker portfolio analytics" or "multi-SaaS dashboard" roles found in the available evidence.

**WTP verdict:** FAILS the minimum threshold of ≥1 willingness-to-pay signal. The inference that these operators "already pay per-product for analytics" is reasonable but is not direct evidence they would pay an additional $29–99/mo for consolidation.

## Estimated TAM / SAM

### Israel

- TAM: Estimated ~200–400 Israeli indie hackers/solo founders running 3+ monetized digital products simultaneously (very conservative; Israel's indie-hacker scene is small). At $49/mo ACV: ~$0.1–0.24M/yr. **Not material for a standalone Israel-first play.**
- SAM (reachable in 12 months): ~50–100 operators reachable via local startup Slack groups, Startup Nation forums, IH Israel community. Revenue: ~$29–59K/yr. Sub-threshold.

### Global

- TAM: Approximately 5,000–15,000 indie hackers globally running 3+ products at $500+ MRR (estimate from IH leaderboard size, MicroConf attendee counts, and self-reported "portfolio" discussions). At $49/mo ACV: **$2.9M–$8.8M/yr.** Plausible but tight; addressable only if the segment self-identifies strongly enough to seek out a tool.
- SAM (reachable in 12 months): Top 500–1,000 most active multi-product builders on IndieHackers, Twitter/X #indiehackers, and ProductHunt. Revenue potential: ~$294K–$588K/yr at 50% conversion of outreach—**optimistic** given no validated WTP.

## Verdict

**INCONCLUSIVE → recommended action: FAIL this cycle, re-queue with enriched search.**

The pain hypothesis is directionally credible but evidence is insufficient to pass:

| Criterion | Required | Found | Pass? |
|---|---|---|---|
| Distinct pain quotes | ≥5, ≥2 sources | 0 direct quotes, 1 source | ❌ |
| WTP signal | ≥1 (paid workaround, competitor price, "is there a tool" ask) | 0 confirmed | ❌ |
| Clear target audience | Yes | Yes (indie hackers, 3–30 products, $500–10k MRR) | ✅ |
| Frequency | Weekly or higher | Weekly (inferred from multi-product juggling) | ✅ |

**Recommended next steps for Market Radar re-scan:**
1. Search HN for `"multiple products" indie hacker dashboard` and `"portfolio saas" metrics`.
2. Scrape r/indiehackers and r/SideProject for threads asking about multi-product analytics tools.
3. Check IndieHackers.com `/products` and `/groups` for any tool requests.
4. Search Twitter/X for `"manage multiple saas" OR "portfolio of apps" lang:en` with engagement filter >10 likes.
5. If ≥5 pain quotes found in re-scan, escalate directly to Pain Validation with enriched candidate.

## Source list

- https://dev.to/thegdsks/the-portfolio-math-when-30-small-apps-beat-1-big-one-41ai (retrieved 2026-06-11 IDT)
