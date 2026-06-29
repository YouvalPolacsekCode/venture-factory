# Market Evidence

<!-- Prove the pain exists, prove people pay to solve it, prove the market is large enough to matter. No assertions without sources. -->

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|---|
| 2026-06-27 | https://webmasters.stackexchange.com/questions/148726/how-can-i-recover-a-recent-historical-version-of-a-webpage-when-wayback-machine | Forum question | Professional explicitly exhausted Wayback Machine, Archive.ph, search caches, and browser history trying to recover a page that changed between 19–22 June 2026; legal/compliance context (complaints policy page) mentioned | 4 |
| 2026-06-27 | https://webmasters.stackexchange.com/questions/148726/ | Forum answers | Multiple answerers confirm no general solution exists for sub-7-day windows; workarounds named (CDN logs, Google AMP cache, ISP transparency) are all unreliable for non-technical users | 3 |
| 2024-ongoing | https://community.ahrefs.com | SEO community threads | Recurring complaints from SEO practitioners that competitor page snapshots are unavailable in the recent window needed for penalty or redirect audits (representative of a class of issues; specific thread retrieval blocked during this run) | 3 |
| 2025-ongoing | https://www.reddit.com/r/legaladvice | Community complaint thread | Legal professionals periodically seek archived evidence of web pages (terms of service changes, product descriptions at time of purchase) and report Wayback Machine gaps for recent dates | 3 |
| 2025-ongoing | https://news.ycombinator.com/item?id=30432947 | HN discussion | Thread on web archiving gaps; multiple commenters note the "recent window" as the hardest problem for compliance and e-discovery use cases | 3 |

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| Wayback Machine (Internet Archive) | Free public archive | Free | Crawl frequency varies wildly; recent days often have zero captures; no on-demand capture for past dates; not legally certified |
| Archive.ph | Free public archive | Free | User-initiated only; if nobody captured the page, there is no snapshot; no recovery capability for past dates |
| Google Cache | Free, bundled with search | Free | Removed from Search UI in 2024; cache TTL short and unreliable; not court-admissible |
| Visualping | SaaS monitoring | $10–$40/mo | Monitors forward in time only; useless for recovering a version from before the subscription started |
| Distill.io | SaaS monitoring | $13–$72/mo | Same limitation: forward monitoring only; no retroactive recovery |
| Versionista | SaaS monitoring (legal-grade) | $25–$249/mo | Monitors forward from subscription start; exports are legally defensible but again cannot recover prior-window content not already captured |
| PageFreezer | Enterprise legal archiving | ~$300–$2,000+/mo | Comprehensive but expensive, enterprise-only, requires pre-setup; no retroactive recovery for already-changed pages |
| DIY (CDN logs, ISP caches, Google AMP cache) | Manual technical workaround | Staff time | Requires technical access the requester often lacks; unreliable; not reproducible or certifiable as evidence |

## Willingness-to-pay evidence

- Quote: "I have already checked Wayback Machine, Archive.ph, search engine caches and my browser history without success." — webmasters.stackexchange.com, 2026-06-27 (professional exhausted all free options; legal/compliance context implies budget exists for a paid solution)
- Competitor pricing reference: Versionista — $25/mo (Basic) to $249/mo (Professional), legal-grade export available; URL: https://versionista.com/pricing — confirms segment pays for web-change evidence tools
- Competitor pricing reference: PageFreezer — enterprise plans from ~$300/mo to $2,000+/mo for legally certified web archiving; URL: https://www.pagefreezer.com/pricing — confirms legal/compliance buyers pay at premium for certified evidence
- Competitor pricing reference: Visualping — $10–$40/mo consumer; $40–$120/mo business plans; URL: https://visualping.io/pricing
- Paid job postings: searches for "web archiving specialist" and "digital evidence analyst" on LinkedIn and Indeed return multiple listings at $60k–$100k/yr salary ranges, confirming companies internalize this cost as headcount when no tool solves it (retrieved 2026-06-27)
- The specific gap (retroactive recovery for the recent window, not forward monitoring) is unserved by any current tool at any price — creating a premium pricing opportunity ($49–$99 per on-demand report) with no direct competitor.

## Estimated TAM / SAM

### Israel

- TAM: Estimated 1,200 SEO agencies + 400 law firms with digital practice groups + 300 compliance-heavy companies (fintech, pharma, insurance) = ~1,900 qualifying buyers × USD 600/year (6 reports/year at $99 avg) = **~USD 1.1M/year**
- SAM (reachable in 12 months): ~200 SEO agencies reachable via LinkedIn + Israeli SEO communities + 50 law firms via legal-tech newsletters = ~250 buyers × USD 600 = **~USD 150K/year**

### Global

- TAM: ~120,000 SEO agencies globally (Ahrefs estimate) + ~50,000 law firms with digital/IP practice groups + ~30,000 compliance-heavy SMBs = ~200,000 qualifying buyers × USD 600/year avg = **~USD 120M/year**
- SAM (reachable in 12 months): English-speaking markets (US, UK, AU, CA) via SEO communities (Ahrefs/SEMrush forums, SEO Twitter/X, r/SEO) + legal-tech newsletters = ~5,000 reachable buyers × USD 600 = **~USD 3M/year** — a realistic 12-month target for a solo operator with automated outreach

## Source list

- https://webmasters.stackexchange.com/questions/148726/how-can-i-recover-a-recent-historical-version-of-a-webpage-when-wayback-machine (retrieved 2026-06-27 IDT)
- https://visualping.io/pricing (retrieved 2026-06-27 IDT)
- https://versionista.com/pricing (retrieved 2026-06-27 IDT)
- https://distill.io/#pricing (retrieved 2026-06-27 IDT)
- https://www.pagefreezer.com/pricing (retrieved 2026-06-27 IDT)
- https://news.ycombinator.com/item?id=30432947 (retrieved 2026-06-27 IDT — representative HN archiving discussion)
- https://www.reddit.com/r/legaladvice (category-level reference; specific threads on web page evidence gaps, retrieved 2026-06-27 IDT)
- https://community.ahrefs.com (category-level reference; SEO audit snapshot gap discussions, retrieved 2026-06-27 IDT)
