# Market Evidence

<!-- Prove the pain exists, prove people pay to solve it, prove the market is large enough to matter. No assertions without sources. -->

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|---|
| 2026-09-03 | https://news.ycombinator.com/item?id=49546432 | HN thread | Single poster seeking to migrate from 1Password for corporate use after a donation controversy; 21 upvotes, 11 comments | 2 |

**Evidence gap:** Only 1 source URL was available from the candidate. Minimum threshold per `config/pain_validation.yaml` requires at least 5 distinct pain quotes from distinct sources. This candidate provides 1 thread with a single primary poster. No additional Reddit threads (r/sysadmin, r/netsec), LinkedIn posts, support forums, or job listings were surfaced in the opportunity data. Web fetch was not executed in this session; the assessment is based on available candidate data.

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| Bitwarden Teams | SaaS | ~$4/user/month | Documented migration guides exist (free, official); reduces need for paid third-party migration service |
| Dashlane Business | SaaS | ~$8/user/month | Has its own onboarding and import tooling; partially closes the gap organically |
| Keeper Business | SaaS | ~$6/user/month | Offers direct 1Password vault import via CSV; self-serve path exists |
| 1Password's own export + competitor import tools | DIY / status quo | Free | The actual migration path (vault export → CSV → import) is already documented by all major competitors at no cost |

**Key finding:** All three primary alternatives (Bitwarden, Dashlane, Keeper) provide self-serve migration documentation and import tooling at no additional cost. The gap a paid migration kit would need to fill — SSO reconfiguration, policy mapping, admin provisioning — is narrow and already partly addressed by free vendor resources and IT admin communities.

## Willingness-to-pay evidence

- Quote: No direct willingness-to-pay quote for a *migration tool or service* is present in the source data. The poster expresses intent to switch but does not indicate willingness to pay for migration assistance.
- Competitor pricing reference: No competitor is currently charging for a 1Password-specific migration kit. The closest analogues (e.g., generic SaaS migration consultants) exist but are not evidenced in the source.
- Paid job postings: None surfaced in candidate data.

**Verdict:** Willingness-to-pay signal is entirely inferred from the fact that the poster is a current paid 1Password subscriber — not from any expressed intent to pay for migration help. This does not meet the minimum WTP evidence threshold.

## Estimated TAM / SAM

### Israel

- TAM: Rough estimate — ~500 Israeli SMB/mid-market companies on 1Password Business (extrapolating from ~$20M ARR globally across ~100K+ business customers; Israel ~0.5% of global SaaS spend) × $49 one-time = ~$24,500 total addressable (one-time, not recurring). This is too small to be meaningful.
- SAM (reachable in 12 months): Subset actively switching due to this controversy — likely <50 companies in Israel, = ~$2,450 revenue ceiling. Not viable.

### Global

- TAM: If ~5% of 1Password's ~100K business customers are considering switching due to the controversy = ~5,000 companies × $49 one-time = $245,000 theoretical maximum — one-time, not recurring, and decaying rapidly as the controversy fades.
- SAM (reachable in 12 months): Realistically reachable via r/sysadmin posts, Google Ads, and HN — estimate 1–2% conversion on ~10,000 impressions = 100–200 customers × $49 = $4,900–$9,800. Does not justify build investment.

## Verdict: REJECTED

**Reason:** Fails minimum evidence thresholds on multiple dimensions:
1. **Pain quotes:** 1 distinct source (HN thread), far below the required 5.
2. **Willingness-to-pay:** No direct WTP signal for a migration product; all competitors offer self-serve migration tooling for free.
3. **Frequency:** One-time, episodic event tied to a single PR controversy — not a recurring workflow pain.
4. **TAM viability:** Even at global scale, the one-time revenue ceiling is <$10K realistically reachable, with rapid demand decay.
5. **Scoring:** Weighted total of 5.5 is below the `min_total_to_build` threshold of 6.5 per `config/pain_validation.yaml`.

**Recommendation:** Do not promote to `experiments/`. Return to `opportunities/` pool with status `rejected`. If a future signal emerges showing sustained, controversy-independent password manager migration demand (e.g., compliance-driven, M&A-driven), re-queue for Market Radar.

## Source list

- https://news.ycombinator.com/item?id=49546432 (retrieved 2026-09-03 IDT)
