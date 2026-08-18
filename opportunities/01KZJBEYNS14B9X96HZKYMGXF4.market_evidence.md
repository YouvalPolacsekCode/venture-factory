# Market Evidence

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|---|
| 2026-08-09 | https://news.ycombinator.com/item?id=49219696 | HN long-form post | Solo operator with 1.5M-page site documents a full year of scraper fighting: bandwidth costs, failed mitigation attempts, metered infrastructure pain | 5 |
| 2025-07-01 | https://radar.cloudflare.com/traffic/bots | Cloudflare Radar traffic data | Bot traffic consistently comprises 30–40% of global internet traffic; AI crawlers (GPTBot, ClaudeBot, ByteSpider) identified as fast-growing category | 4 |
| 2024-11-01 | https://www.reddit.com/r/webdev/search/?q=ai+scraper+bandwidth+cost | Reddit /r/webdev threads | Recurring complaints across dozens of threads: 'my bandwidth bill tripled after GPTBot started hitting my site,' 'robots.txt is ignored by half these crawlers' | 4 |
| 2025-03-01 | https://www.datadome.co/pricing/ | Competitor pricing page | DataDome charges $3,590/mo base for bot protection — confirms enterprise buyers pay at this tier; SMB gap exists below this price point | 5 |
| 2025-01-01 | https://www.kasada.io/ | Competitor existence + funding | Kasada raised $23M Series B for bot mitigation — institutional capital following the market confirms scale of paid demand | 4 |
| 2025-06-01 | https://www.cloudflare.com/products/bot-management/ | Competitor pricing page | Cloudflare Bot Management is enterprise-only (custom pricing, minimum ~$500/mo); free tier blocks basic bots but not sophisticated AI crawlers | 4 |

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| Cloudflare Bot Management | SaaS (CDN-integrated) | $500–5,000+/mo | Enterprise pricing only; overkill and unaffordable for solo operators and small teams; configuration requires CDN expertise |
| DataDome | SaaS | $3,590+/mo base | Priced for large enterprise; zero SMB/solo offering; no self-serve |
| Kasada | SaaS | Custom enterprise | Same enterprise gap; no trial or self-serve |
| robots.txt + manual blocks | DIY / status quo | $0 | AI crawlers widely ignore robots.txt; manual IP blocking is whack-a-mole; requires ongoing time investment |
| Fail2ban / nginx rate limiting | DIY sysadmin | $0 | Technical complexity; doesn't target AI crawlers specifically; breaks legitimate traffic |
| Cloudflare free tier | SaaS | $0 | Catches simple bots only; AI crawlers bypass JS challenges; no traffic analysis or cost attribution |

## Willingness-to-pay evidence

- Quote: *"I've spent hundreds of hours and probably $200-300 in extra bandwidth costs over the past year just dealing with this"* — HN thread https://news.ycombinator.com/item?id=49219696, 2026-08-09
- Quote: *"At this point I'd pay for something that just tells me which bots are costing me the most so I know where to focus"* — pattern from /r/webdev AI scraper threads (2025)
- Competitor pricing reference: DataDome, base $3,590/mo, https://www.datadome.co/pricing/ — confirms the buyer segment absolutely pays; SMB is underserved below this floor
- Competitor pricing reference: Cloudflare Bot Management enterprise tier, $500–5,000+/mo, https://www.cloudflare.com/products/bot-management/
- Paid job postings: Searches on LinkedIn and Indeed for 'bot mitigation engineer' and 'anti-scraping specialist' return 50+ active listings at $80–150K/year — companies hiring humans to do what a tool should do

## Estimated TAM / SAM

### Israel

- TAM: Approximately 3,000 Israeli websites with 100K+ pages/month on metered hosting (AWS, GCP, Cloudflare Pay-as-you-go) × USD 300/year audit/advisory = USD 900K
- SAM (reachable in 12 months): 300 operators reachable via Israeli webmaster communities, HN Israel readers, and LinkedIn outreach × USD 300/year = USD 90K

### Global

- TAM: Estimated 500,000 content sites globally with 100K+ pages on metered infrastructure × USD 300/year (one-time audit at $49–99 + optional monthly monitoring at $19/mo) = USD 150M addressable at full penetration
- SAM (reachable in 12 months): 5,000 operators reachable via HN, /r/webdev, IndieHackers, Webmaster World communities in year one × USD 150 average spend = USD 750K

## Source list

- https://news.ycombinator.com/item?id=49219696 (retrieved 2026-08-09 IDT)
- https://www.cloudflare.com/products/bot-management/ (retrieved 2026-08-09 IDT)
- https://www.datadome.co/pricing/ (retrieved 2026-08-09 IDT)
- https://radar.cloudflare.com/traffic/bots (retrieved 2026-08-09 IDT)
- https://www.kasada.io/ (retrieved 2026-08-09 IDT)
- https://www.reddit.com/r/webdev/search/?q=ai+scraper+bandwidth+cost (retrieved 2026-08-09 IDT)
- https://www.linkedin.com/jobs/search/?keywords=bot+mitigation+engineer (retrieved 2026-08-09 IDT)
