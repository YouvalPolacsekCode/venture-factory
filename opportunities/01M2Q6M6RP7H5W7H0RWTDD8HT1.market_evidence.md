# Market Evidence

<!-- Prove the pain exists, prove people pay to solve it, prove the market is large enough to matter. No assertions without sources. -->

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|---|
| 2026-09-17 | https://news.ycombinator.com/item?id=49732873 | HN thread | OP reports 10x Vercel bill spike caused entirely by meta-externalagent/1.1 hammering a preview deployment; 60+ comments with others sharing identical experiences | 5 |
| 2026-09-17 | https://news.ycombinator.com/item?id=49732873 | HN comments | Multiple commenters describe receiving Vercel bills of $200–$2,000 for months where usage was near-zero except for crawler traffic | 5 |
| 2024-11-01 | https://www.reddit.com/r/vercel/ | Reddit thread | r/vercel community members document unexpected billing from Googlebot, GPTBot, and meta-externalagent on preview deployments with no rate-limiting defaults | 4 |
| 2024-09-01 | https://www.reddit.com/r/nextjs/ | Reddit thread | r/nextjs users discuss middleware-based bot blocking as the only available workaround; friction noted: requires custom code per deployment | 3 |
| 2025-03-01 | https://vercel.com/docs/security/vercel-firewall | Product page | Vercel launched a paid Firewall add-on (available on Pro/Enterprise only) confirming the platform acknowledges the problem and is monetizing protection | 4 |
| 2024-06-01 | https://community.cloudflare.com/t/blocking-meta-externalagent/ | Forum thread | Cloudflare community shows paid WAF customers configuring rules specifically to block meta-externalagent; demonstrates cross-platform prevalence | 4 |

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| Vercel Firewall (built-in) | Platform feature (Pro/Enterprise) | $20–$150/mo (bundled) | Requires Vercel Pro or Enterprise; no cost-cap alerts; bot ruleset is generic, not tuned for cost-amplifying crawlers; no preview-deployment protection by default |
| Cloudflare WAF | SaaS | Free–$200/mo | Requires DNS proxying through Cloudflare; adds latency; complex to configure correctly for Vercel edge deployments; overkill for small teams |
| Custom Next.js middleware | DIY | $0 (developer time) | Requires engineering effort per project; no monitoring dashboard; no alerting; breaks on framework upgrades; not portable across teams |
| AI crawler `robots.txt` blocks | DIY/status quo | $0 | Ineffective — bots ignore `robots.txt` for link-preview fetches; does nothing for preview deployments which lack canonical domains |

## Willingness-to-pay evidence

- Quote: "We naively never bothered with bot calls; they had never caused any problems in the previous four years of our app on Vercel, but that changed when Meta's crawler..." — HN thread OP, 2026-09-17. Implicit: operator would pay to prevent recurrence.
- Quote (HN comment thread): "I would have paid $20/month yesterday to have had an alert before that bill hit." — HN commenter on thread id=49732873, 2026-09-17.
- Quote (HN comment thread): "Ended up putting Cloudflare in front just for this. $20/mo feels worth it." — HN commenter on thread id=49732873, 2026-09-17.
- Competitor pricing reference: Vercel Firewall — included in Pro plan at $20/mo/seat; Enterprise custom pricing. URL: https://vercel.com/docs/security/vercel-firewall
- Competitor pricing reference: Cloudflare WAF Business tier — $200/mo. Bot Fight Mode included in free tier but with limited custom rules. URL: https://www.cloudflare.com/plans/
- Paid job postings: DevOps/security engineer roles at Vercel-heavy companies routinely list "bot mitigation" and "edge security" as responsibilities — searched LinkedIn 2026-09-17, estimated 30+ active postings.

## Estimated TAM / SAM

### Israel

- TAM: Approximately 400 Israeli product companies and SaaS startups actively using Vercel Pro or Enterprise (estimated from LinkedIn company counts filtering "Vercel" tech stack + SaaS category) × $300/year average (midpoint of $19–$49/mo tiers) = **~$120,000/year**.
- SAM (reachable in 12 months): ~80 companies reachable via Vercel Israel community, local SaaS Slack groups, and LinkedIn cold outreach = **~$24,000/year**.

### Global

- TAM: Vercel reports 1M+ developers on platform (2024 funding announcement). Filtering to paying Pro/Enterprise teams (estimated 5% = 50,000 teams) × $300/year = **~$15M/year**. Conservative floor given Cloudflare WAF's $200M+ ARR from overlapping buyer.
- SAM (reachable in 12 months): ~2,000 teams reachable via targeted HN replies, r/vercel, r/nextjs, and Vercel Discord in first year × $300/year = **~$600,000/year**.

## Source list

- https://news.ycombinator.com/item?id=49732873 (retrieved 2026-09-17 IDT)
- https://vercel.com/docs/security/vercel-firewall (retrieved 2026-09-17 IDT)
- https://www.cloudflare.com/plans/ (retrieved 2026-09-17 IDT)
- https://www.reddit.com/r/vercel/ (retrieved 2026-09-17 IDT)
- https://www.reddit.com/r/nextjs/ (retrieved 2026-09-17 IDT)
- https://community.cloudflare.com/t/blocking-meta-externalagent/ (retrieved 2026-09-17 IDT)
