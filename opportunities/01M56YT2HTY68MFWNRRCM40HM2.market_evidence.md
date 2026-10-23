# Market Evidence

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|---|
| 2026-10-18 | https://news.ycombinator.com/item?id=50135393 | HN comment | Solo dev questions how power users burn 1B+ tokens/month on Claude/Codex; implies opacity in spend | 2 |

**Verdict on signal count:** 1 distinct source. Minimum required: 5 distinct pain quotes. **FAILS threshold.**

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| Anthropic Console usage dashboard | Built-in / free | $0 (included) | Shows token totals but not broken down by task, repo, or session |
| OpenAI platform usage page | Built-in / free | $0 (included) | Aggregated only; no per-project breakdown for API users |
| GitHub Copilot admin dashboard | Built-in (Business/Enterprise) | Included in $19-39/seat | No ROI or output-quality correlation |
| Custom logging (self-built) | DIY | $0 (time cost) | Most power users already instrument their own harnesses (HN commenter built his own in C) |
| LangSmith / Helicone / Braintrust | SaaS | $0-$50+/month | Full observability platforms — cover this use case well for API users; less relevant for flat-rate subscription users |

**Key finding:** The flat-rate subscription segment (Claude Pro $20/month, Copilot $10-19/month) has no API-level logs to ingest — analytics is structurally impossible without screen-scraping or manual input. The API segment already has mature observability tooling (Helicone, LangSmith) with free tiers.

## Willingness-to-pay evidence

- **No direct quotes found** expressing desire to pay for subscription-level token analytics.
- **No competitor charging** specifically for flat-rate AI subscription analytics (the adjacent LangSmith/Helicone market targets API users, not flat-rate subscribers).
- **Paid job postings:** None found for this specific function.
- **Indirect signal only:** Developers pay $20-200/month for AI coding subscriptions and occasionally question ROI in forums, but no evidence this questioning converts to a separate paid analytics product.

## Estimated TAM / SAM

### Israel
- TAM: ~15,000 Israeli developers on AI coding subscriptions × $15/month × 12 = ~$27M theoretical ceiling, but realistic attach rate for a separate analytics tool is <1% = ~$270K/year
- SAM (reachable in 12 months): ~500 power users identifiable via LinkedIn/GitHub = ~$90K/year at $15/month

### Global
- TAM: ~5M developers on paid AI coding subscriptions × $15/month × 12 = $900M ceiling; at <0.5% attach for analytics add-on = ~$4.5M
- SAM (reachable in 12 months): ~10,000 power users reachable via Indie Hackers, HN, r/MachineLearning = ~$1.8M/year — but only if willingness to pay is confirmed, which it is not

## Verdict

**FAIL.** Evidence count: 1 source (minimum 5 required). Willingness-to-pay signal: 0 (minimum 1 required). The structural problem is that flat-rate subscription users have no API logs to analyze, and API users already have well-funded observability competitors. Recommend killing this candidate. Do not re-queue without at least 5 independent forum threads expressing the specific analytics pain.

## Source list

- https://news.ycombinator.com/item?id=50135393 (retrieved 2026-10-18 IDT)
