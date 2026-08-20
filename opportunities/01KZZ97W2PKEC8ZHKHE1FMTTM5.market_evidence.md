# Market Evidence

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|---|
| 2026-08-14 | https://news.ycombinator.com/item?id=49290713 | HN thread | Users publicly listing monthly AI subscription costs (Claude, GPT, Gemini, Perplexity); 22 comments, 8 points | 2 |

**Notes:** Only one primary source was identified. The thread documents spend awareness, not spend frustration or active tool-seeking. No comments request a tracker product. Volume (8 points) is below the threshold for strong community signal on HN (typically 50+). No Reddit, Indie Hackers, or Product Hunt threads independently corroborate demand for a paid AI spend tracker aimed at individual developers.

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| Manual spreadsheet | DIY | $0 | Requires discipline; no automatic sync — but this is the status quo and most devs tolerate it |
| Ramp / Brex expense dashboards | SaaS (corporate cards) | Free–$12/user/mo | Only captures card spend; many AI subs are personal cards |
| Copilot Money / Monarch Money | SaaS (personal finance) | $8–$14/mo | Already tracks all subscriptions including AI tools; not developer-specific but functionally solves the problem |
| Notion / Airtable templates (public) | DIY template | $0 | Dozens of free "SaaS tracker" templates exist; zero switching cost |
| Privacy.com virtual cards per service | DIY | $0 | Allows per-subscription spend caps and visibility without a new tool |

**Gap analysis:** The gaps are narrow. The only defensible wedge would be AI-model-specific recommendations ("switch from GPT-4 to Claude for coding because your usage pattern shows X"), but this requires account-level usage data that providers do not expose via public API at the individual tier. Without that data, the product reduces to a manual input tracker competing with free alternatives.

## Willingness-to-pay evidence

- Quote: No quotes found in source thread requesting a paid tracker tool. Comments are descriptive ("I pay $X for Y") rather than pain-expressing ("I can't manage this, I need help").
- Competitor pricing reference: No direct competitor charging for individual AI subscription tracking was identified. Closest analogues (Truebill/Rocket Money) target broader subscription management at $3–$12/mo but have not launched AI-specific tiers.
- Paid job postings: Zero job postings found for "AI subscription manager" or equivalent role.

**Verdict:** No willingness-to-pay signal identified. The bar requires at least 1 WTP signal; this opportunity provides none from available evidence.

## Estimated TAM / SAM

### Israel
- TAM: ~15,000 Israeli software developers and freelancers actively using multiple AI subscriptions × $60/year = ~$900K. Speculative; no Israel-specific data.
- SAM (reachable in 12 months): ~1,500 (active on LinkedIn/HN/local dev communities) × $60/year = ~$90K. Too small to justify build investment.

### Global
- TAM: ~2M developers globally paying for 2+ AI subscriptions × $60/year = ~$120M. Market size is real.
- SAM (reachable in 12 months): Conversion against free alternatives and low pain severity make realistic SAM ~0.05% = ~$60K ARR in year one — below the threshold for a standalone product.

## Source list

- https://news.ycombinator.com/item?id=49290713 (retrieved 2026-08-14 IDT)

---

## Verdict: REJECTED

**Reason:** Fails the minimum evidence bar. Only 1 distinct source identified (vs. minimum 5 distinct pain signals required). Zero willingness-to-pay signal found. Free alternatives (personal finance apps, spreadsheets) already absorb the pain with zero friction. The thread demonstrates spend awareness, not spend frustration requiring a paid solution. Recommend Market Radar re-scan in 90 days if a competitor launches and gains traction.
