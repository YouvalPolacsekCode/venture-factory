# Market Evidence

<!-- Prove the pain exists, prove people pay to solve it, prove the market is large enough to matter. No assertions without sources. -->

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|---|
| 2026-10-16 | https://news.ycombinator.com/item?id=50112559 | HN complaint thread | Paying Pro subscriber reports burning 50% of 5-hour quota window in one prompt; describes subscription as "worthless" | 2 |

**Verdict on signal volume:** Only 1 distinct primary source identified. The pass bar requires ≥5 distinct pain quotes from independent sources. This candidate does not meet the threshold.

**Adjacent signals searched (not found or insufficient):**
- Reddit threads on r/ChatGPTPro, r/LocalLLaMA, r/OpenAI discussing quota burnout: recurring complaints exist but are fragmented across platform-specific subreddits with no aggregated demand signal for a third-party monitor.
- "Is there a tool that..." requests for AI quota dashboards: not located in the evidence available.
- HN threads on AI subscription ROI: scattered comments, no dedicated thread with significant upvote mass on quota-monitoring tooling specifically.

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| OpenAI usage dashboard (built-in) | Platform-native | Included in subscription | Only covers OpenAI products; no cross-platform view; no pre-burnout alerts |
| Anthropic console usage view | Platform-native | Included in subscription | API-key usage only, not consumer Pro plan quota |
| TokenCounter / prompt cost browser extensions | DIY / free extension | Free | Counts tokens per prompt but does not track session quota against plan limits; no alert logic |
| Helicone, LangSmith, Braintrust | SaaS (API observability) | Free tier + $20-200/mo | Targets API users / enterprise, not consumer Pro subscription holders; requires SDK instrumentation |

**Gap observation:** No identified product tracks consumer-plan quota (OpenAI Pro, Claude Pro, Google Gemini Advanced) in real time and fires pre-burnout alerts. However, platforms can close this gap unilaterally at any time by improving their own dashboards.

## Willingness-to-pay evidence

- Quote: No direct "I would pay for this" quote found in source material.
- Competitor pricing reference: Helicone charges $20-200/mo for API observability — confirms the adjacent market pays, but Helicone targets API/enterprise buyers, not consumer-plan subscribers.
- Paid job postings: None identified specifically for quota-monitoring tooling.
- Indirect signal: The source poster pays $20+ for a Pro subscription, confirming they buy AI tooling, but no signal they would pay an additional layer on top.

**WTP verdict:** Indirect/inferred only. Does not meet the ≥1 hard WTP signal requirement (competitor charging money for this specific layer, or explicit "is there a paid tool" request).

## Estimated TAM / SAM

### Israel

- TAM: Estimated 15,000–25,000 Israeli knowledge workers and developers on paid AI subscriptions (OpenAI Pro ~$20/mo, Claude Pro ~$18/mo, Gemini Advanced ~$22/mo) × USD 120/year monitoring add-on = USD 1.8M–3.0M. Math is speculative; no Israel-specific subscription data available.
- SAM (reachable in 12 months): ~2,000–4,000 power users identifiable via LinkedIn ("AI" + "developer") and Israeli tech communities (e.g., Geektime, local Slack groups) × USD 120/year = USD 240K–480K.

### Global

- TAM: ~50M paid AI subscription seats globally (rough estimate from OpenAI ~15M+ paid, Anthropic undisclosed, Google ~5M+ Gemini Advanced) × 10% power-user segment experiencing quota pain × USD 120/year = USD 600M theoretical ceiling. This is a very rough upper bound.
- SAM (reachable in 12 months): r/ChatGPTPro (~180K members), r/LocalLLaMA (~500K members), relevant HN audience — realistically reachable paid-conversion pool is 5,000–20,000 users × USD 120/year = USD 600K–2.4M.

## Source list

- https://news.ycombinator.com/item?id=50112559 (retrieved 2026-10-16 IDT)
- https://helicone.ai/pricing (reference for adjacent market pricing; not retrieved live)
- https://www.reddit.com/r/ChatGPTPro/ (checked for quota complaint threads; no single high-signal thread identified)
- https://www.reddit.com/r/LocalLLaMA/ (checked for quota burnout discussions; fragmented signals only)

---

## Verdict: REJECTED (Inconclusive → Fail)

**Reason:** Fewer than 5 distinct pain quotes from independent sources (only 1 primary source found). No hard willingness-to-pay signal for a quota-monitoring layer specifically. Free alternatives exist and platform-native dashboards can close the gap. Re-queue for Market Radar if forum volume on quota complaints grows or a competitor launches and gains traction.
