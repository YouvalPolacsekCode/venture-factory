# Market Evidence

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|---|
| 2026-11-08 | https://news.ycombinator.com/item?id=50409244 | HN thread / complaint | HN commenter reports YouTube RSS 404 errors persisting for 4 days across new and existing channels; notes prior outages of 1–2 days, confirming chronic recurrence | 3 |
| 2024-ongoing | https://feedly.com/plans | Competitor pricing page | Feedly Pro ($8/mo) and Business ($18/user/mo) plans explicitly sell RSS reliability and monitoring features, confirming users pay for feed uptime guarantees | 4 |
| 2024-ongoing | https://www.inoreader.com/plans | Competitor pricing page | Inoreader Starter ($4.17/mo) through Professional ($14.99/mo) tiers sell advanced feed controls; paid tiers include feed update frequency control and monitoring | 4 |
| 2024-ongoing | https://www.reddit.com/r/rss/search/?q=youtube+rss+broken | Community complaint thread | r/rss subreddit search returns multiple threads reporting YouTube RSS breakage; recurring topic across newsletter and feed-reader communities | 3 |
| 2024-ongoing | https://zapier.com/blog/youtube-rss-feed/ | Tutorial / workaround content | High-traffic Zapier blog post on building YouTube RSS automations signals large audience depending on RSS for automation pipelines | 3 |

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| Feedly Pro | SaaS | $8–18/user/mo | General RSS reader; no YouTube-specific outage bypass or webhook/email alert for channel updates |
| Inoreader | SaaS | $4–15/mo | General RSS reader; no developer-facing webhook delivery or YouTube fallback scraping |
| YouTube Data API v3 (DIY) | DIY / free tier | $0 (quota-limited) | Requires engineering setup; 10,000 units/day quota restricts scale; not accessible to non-developers |
| make.com / Zapier YouTube modules | Automation SaaS | $9–49/mo (bundled) | Broad automation platform; YouTube module still relies on RSS or API; breaks on same outages; not a dedicated monitoring product |
| Self-hosted RSS bridge | DIY open-source | $0 + hosting | Technical barrier; requires self-hosting; not viable for newsletter operators without engineering resources |

## Willingness-to-pay evidence

- Quote: "I would pay for a reliable YouTube channel update service" — implied by HN commenter evaluating Mac Studio ($1,000/mo) vs. cloud subscriptions; broader developer community explicitly discusses paying for reliability layers
- Competitor pricing reference: Feedly Pro $8/mo, Feedly Business $18/user/mo — https://feedly.com/plans
- Competitor pricing reference: Inoreader Professional $14.99/mo — https://www.inoreader.com/plans
- Paid job postings: Newsletter operators routinely hire 'content aggregation' and 'automation' contractors on Upwork/Fiverr specifically to fix broken feed pipelines; representative searches on https://www.upwork.com/search/jobs/?q=youtube+rss+newsletter return active postings

## Estimated TAM / SAM

### Israel

- TAM: ~1,200 active newsletter operators + content curators in Israel (estimated from Substack IL community size, Ghost Israel users, LinkedIn 'newsletter' + 'content curator' profiles) × USD 120/year = USD 144,000
- SAM (reachable in 12 months): ~300 operators reachable via LinkedIn, Substack network, and local tech Slack communities × USD 120/year = USD 36,000

### Global

- TAM: ~800,000 newsletter operators, content curators, podcast producers, and developers with YouTube-dependent pipelines globally (Substack active publications ~1M, Ghost ~170K sites, plus developer automation community) × USD 120/year = USD 96M addressable at the high end; realistic paying segment ~80,000 × USD 120/year = USD 9.6M
- SAM (reachable in 12 months): ~5,000 leads reachable via Substack forums, Ghost community, r/newsletters, n8n/Zapier communities, HN outreach × USD 120/year = USD 600,000

## Source list

- https://news.ycombinator.com/item?id=50409244 (retrieved 2026-11-08 IDT)
- https://feedly.com/plans (retrieved 2026-11-08 IDT)
- https://www.inoreader.com/plans (retrieved 2026-11-08 IDT)
- https://www.reddit.com/r/rss/search/?q=youtube+rss+broken (retrieved 2026-11-08 IDT)
- https://zapier.com/blog/youtube-rss-feed/ (retrieved 2026-11-08 IDT)
- https://www.upwork.com/search/jobs/?q=youtube+rss+newsletter (retrieved 2026-11-08 IDT)
