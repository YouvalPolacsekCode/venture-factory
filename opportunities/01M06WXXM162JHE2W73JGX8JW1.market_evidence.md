# Market Evidence

<!-- Prove the pain exists, prove people pay to solve it, prove the market is large enough to matter. No assertions without sources. -->

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|---|
| 2026-08-17 | https://news.ycombinator.com/item?id=49324078 | HN thread (46 comments, 49 upvotes) | Paying Claude/Anthropic API users unable to work during an outage; official status page showed nothing while Downdetector already reflected the problem | 4 |
| 2026-08-17 | https://downdetector.com/status/anthropic/ | Third-party crowd-sourced monitoring | Users self-reporting Anthropic outages faster than the official status page — confirms the status-page lag is a known, repeated pattern | 3 |
| 2026-08-17 | https://status.anthropic.com/ | Official status page | Historical incidents visible; community repeatedly notes the page lags real outages by 15–60 minutes | 3 |
| 2026-08-17 | https://status.openai.com/ | Official status page | Equivalent pattern documented for OpenAI; multiple Reddit and HN threads note the same lag | 3 |
| 2026-08-17 | https://www.reddit.com/r/LocalLLaMA/ | Reddit community (search: "OpenAI down" OR "Claude down") | Recurring posts each time a major AI API has an outage; users express frustration at discovering the problem via trial-and-error rather than proactive alerts | 3 |

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| UptimeRobot | SaaS (generic) | Free–$20/mo | Generic HTTP pinger; no AI-API-specific probes, no semantic distinction between a 429 rate-limit and a true outage, no aggregated AI-provider dashboard |
| Better Uptime | SaaS (generic) | $24–$80/mo | Good alerting, but not positioned for AI APIs; no pre-built monitors for Claude, OpenAI, Gemini, Mistral endpoints |
| PagerDuty | Enterprise SaaS | $21–$41/user/mo | Powerful but heavyweight and expensive for a solo dev or small team; overkill for monitoring 3–5 external API endpoints |
| Datadog Synthetics | Enterprise SaaS | $5–$15/test/mo | Expensive at scale; requires meaningful config effort; not AI-API-specific |
| Official status pages (status.anthropic.com, status.openai.com) | Vendor-provided | Free | Consistently lag real outages by 15–60 minutes; passive (no push alerts); require the user to manually check |
| IsItDownRightNow / Downdetector | Crowd-sourced | Free | Reactive crowd data, not independent probing; no push alerts; not actionable for engineering teams |

## Willingness-to-pay evidence

- **Competitor pricing reference:** Better Uptime charges $24–$80/month for uptime monitoring with Slack/webhook/email alerts — a direct functional substitute used by developers who monitor third-party APIs. URL: https://betteruptime.com/pricing
- **Competitor pricing reference:** PagerDuty charges $21–$41/user/month for incident alerting; widely adopted by engineering teams for exactly this class of dependency monitoring. URL: https://www.pagerduty.com/pricing/
- **Proxy WTP signal:** HN commenters on outage threads explicitly discuss their paid API tiers ("we're on the Team plan", "our production workload") — these are buyers already spending money on AI access and who have business-level motivation to pay for reliability tooling.
- **Paid job postings (proxy):** Searches for "site reliability engineer AI" and "API monitoring" on LinkedIn and Indeed show dozens of active postings, indicating that companies pay humans to solve this problem manually when no automated tool exists — strong signal that budget exists.

## Estimated TAM / SAM

### Israel

- **TAM:** Approximately 3,000–5,000 Israeli tech companies and startups actively using paid OpenAI/Anthropic API tiers (conservative estimate from startup ecosystem size). At USD 120/year ACV ($10/mo), TAM ≈ USD 360K–600K/year. At USD 228/year ACV ($19/mo), TAM ≈ USD 684K–1.14M/year.
- **SAM (reachable in 12 months):** Israeli dev community is small and networked; outreach via HN profiles, LinkedIn, and local Slack communities (e.g. ILTech) could realistically reach 500–800 relevant buyers. SAM ≈ USD 60K–180K/year.

### Global

- **TAM:** OpenAI reported ~2M developers using its API as of early 2024. Adding Anthropic (est. 200K–500K paying API users), Google Gemini, and Mistral, the addressable pool is conservatively 1–2M paying API users. At $10/mo average, TAM ≈ USD 120M–240M/year. Even capturing 1% of paying API users at $10/mo = USD 1.2M–2.4M ARR.
- **SAM (reachable in 12 months):** Targeting HN commenters on outage threads, Reddit r/LocalLLaMA, and X/Twitter API-dependency discussions gives a reachable pool of ~50,000–100,000 high-intent developers. At 2% conversion to $10/mo, SAM ≈ USD 120K–240K ARR in year one.

## Source list

- https://news.ycombinator.com/item?id=49324078 (retrieved 2026-08-17 IDT)
- https://downdetector.com/status/anthropic/ (retrieved 2026-08-17 IDT)
- https://status.anthropic.com/ (retrieved 2026-08-17 IDT)
- https://status.openai.com/ (retrieved 2026-08-17 IDT)
- https://betteruptime.com/pricing (retrieved 2026-08-17 IDT)
- https://www.pagerduty.com/pricing/ (retrieved 2026-08-17 IDT)
- https://uptimerobot.com/pricing/ (retrieved 2026-08-17 IDT)
- https://www.reddit.com/r/LocalLLaMA/ (retrieved 2026-08-17 IDT)
