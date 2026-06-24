# Market Evidence

<!-- Prove the pain exists, prove people pay to solve it, prove the market is large enough to matter. No assertions without sources. -->

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|---|
| 2026-06-22 | https://news.ycombinator.com/item?id=48624574 | HN thread | OSS org had all GitHub Actions (including self-hosted runners) silently disabled due to drive-by contributor crypto-mining; GitHub support unresponsive | 3 |

**Evidence gap summary:** Only one primary signal source was available. A broader web search for adjacent complaints (GitHub Actions disabled, OSS org banned, contributor abuse CI) did not surface additional distinct pain threads, forum posts, or job listings confirming this as a recurring, widespread pattern rather than an isolated incident. The single HN post garnered only 7 points and the thread is low-volume, indicating limited community resonance at time of discovery.

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| GitHub's built-in Actions permissions (fork PR approval settings) | Platform feature (free) | $0 | Requires manual configuration; does not score contributor risk proactively; does not prevent the platform-level ban trigger |
| Allstar (OpenSSF) | Open-source GitHub App | Free | Security posture hardening, not contributor abuse/mining detection |
| Manual org admin review | DIY / status quo | Staff time cost | Does not scale; no automated signal scoring |

**Note:** No paid SaaS product was found that specifically addresses contributor vetting to prevent Actions abuse bans. Absence of a paid competitor is not a positive signal here — it more likely indicates the market is too small or the problem is too narrow/rare to sustain a standalone product.

## Willingness-to-pay evidence

- Quote: No direct quotes from maintainers expressing willingness to pay for a contributor vetting solution were found in the source thread or adjacent searches.
- Competitor pricing reference: No direct competitor charging for this specific use case identified.
- Paid job postings: No job listings found requesting contributor risk management or CI abuse prevention roles.

**WTP verdict: FAIL.** The minimum threshold of 1 willingness-to-pay signal is not met.

## Estimated TAM / SAM

### Israel

- TAM: Israel has a meaningful open-source developer community, but OSS org maintainers at companies with paid GitHub accounts who would proactively pay for contributor vetting is an extremely narrow slice. Rough estimate: ~200 qualifying orgs × $360/year ($30/mo) = ~$72K. Too small to be meaningful.
- SAM (reachable in 12 months): <50 orgs realistically reachable.

### Global

- TAM: GitHub reports ~4M public organizations. Active OSS orgs with >50 contributors who have experienced or fear Actions abuse bans: conservatively ~10,000 orgs × $360/year = ~$3.6M. However, willingness-to-pay pre-incident is unproven — most maintainers will not purchase insurance for a rare event they haven't experienced.
- SAM (reachable in 12 months): ~1,000 orgs via GitHub search + devops community outreach = ~$360K at full conversion (unrealistic without WTP evidence).

## Verdict

**FAIL — Do not promote.**

Reasons:
1. **Insufficient pain breadth:** Only 1 distinct signal source. Minimum bar is 5 distinct pain quotes from independent sources.
2. **No willingness-to-pay signal:** No competitor charging for this, no quotes asking for a paid solution, no job postings.
3. **Frequency too low:** This is a catastrophic-but-rare event; pre-emptive purchasing motivation is unproven.
4. **Platform dependency risk:** GitHub could resolve this with a policy change, eliminating the market overnight.
5. **TAM too small:** Even optimistic global TAM is ~$3.6M, and realistic SAM is negligible.

**Recommended next action:** Mark as `fail`. If GitHub Actions abuse bans become a more widely-reported pattern (5+ distinct HN/Reddit/devops forum threads within a 30-day window), re-queue for Market Radar re-scan.

## Source list

- https://news.ycombinator.com/item?id=48624574 (retrieved 2026-06-22 IDT)
- https://github.com/ossf/allstar (retrieved 2026-06-22 IDT — reviewed as existing alternative)
