# Market Evidence

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|---|
| 2026-09-12 | https://news.ycombinator.com/item?id=49677232 | HN post | Single poster notes Namecheap hosting incident is at least the second in ~30 days; 4 points, no visible comment thread | 2 |

**Assessment:** Only one primary source retrieved. The HN post scored 4 points with no corroborating comment thread visible at crawl time. The problem narrative (budget shared-hosting unreliability) is broadly credible but is represented here by a single signal. The minimum evidence bar of 5 distinct pain quotes is not met.

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| UptimeRobot | SaaS (freemium) | $0–$20/mo | Monitoring only; no automated failover or DNS redirect |
| Better Uptime | SaaS | $0–$80/mo | Monitoring + on-call; failover requires manual DNS change |
| StatusCake | SaaS | $0–$40/mo | Monitoring only; no CDN fallback integration |
| Cloudflare (free/pro) | CDN + proxy | $0–$200/mo | Full failover possible but requires technical setup; not zero-config |
| Namecheap/host-level SLA | Status quo | Included | SLA credits rarely compensate lost revenue; no proactive failover |

**Gap the opportunity targets:** Zero-config, one-click CDN/DNS failover triggered automatically when a budget host goes down — not just alerting. This gap exists but is narrow and technically demanding to make truly zero-config.

## Willingness-to-pay evidence

- Quote: *None found.* No direct quote from a user expressing willingness to pay specifically for a failover add-on.
- Competitor pricing reference: UptimeRobot paid plans ($7–$20/mo) and Better Uptime ($25–$80/mo) confirm that monitoring has a paying market, but these are monitoring products, not failover. No competitor charging specifically for automated DNS/CDN failover for shared-hosting customers was identified.
- Paid job postings: Not searched (would require an approval action). No marketplace listings for this specific service found via public web data.

**Verdict on WTP:** Implicit only. Buyers already pay for hosting; there is no documented case of a user paying for a shared-hosting failover overlay product specifically.

## Estimated TAM / SAM

### Israel

- TAM: Estimated ~15,000 Israeli freelancers and micro-SMBs on budget shared hosting × USD 120/year (low-end monitoring/failover tier) = **USD 1.8M**. Market is small domestically.
- SAM (reachable in 12 months): Freelancer communities (Facebook groups, LinkedIn, local dev Slack) could yield ~500 reachable leads = **USD 60K**.

### Global

- TAM: ~50M websites on shared hosting globally (W3Techs data, approximate); assuming 5% are operated by buyers willing to pay a separate failover fee × USD 120/year = **USD 300M** (upper bound, highly optimistic).
- SAM (reachable in 12 months): Organic HN/Reddit/Indie Hackers reach for a new entrant without paid acquisition = ~2,000 trial users × 10% conversion × USD 120/year = **USD 24K ARR**. Not compelling at early stage without a clear moat.

## Source list

- https://news.ycombinator.com/item?id=49677232 (retrieved 2026-09-13 IDT)

---

## Verdict: REJECTED

**Reason:** Fails minimum evidence thresholds. Only 1 source, 0 distinct pain quotes meeting the 5-quote bar, and 0 explicit willingness-to-pay signals for a failover product specifically. Competitive market is well-served at the free tier. Recommend Market Radar re-scan if hosting-outage complaint volume increases or if a corroborated thread with ≥20 comments surfaces.