# Market Evidence

<!-- Prove the pain exists, prove people pay to solve it, prove the market is large enough to matter. No assertions without sources. -->

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|---|
| 2026-11-12 | https://webmasters.stackexchange.com/questions/150079/is-a-temporary-sitemap-of-410-urls-a-legitimate-way-to-get-googlebot-to-recrawl | Forum question | Single SEO manager asking how to accelerate bulk de-indexing of legacy spam URLs via temporary 410 sitemap | 2 |
| 2026-11-12 | https://webmasters.stackexchange.com/questions/tagged/sitemaps+410 | Tag cluster | Approximately 12–18 related questions on SE over 5+ years; collectively modest volume, no sign of unmet paid need | 1 |
| 2026-11-12 | https://developers.google.com/search/docs/crawling-indexing/remove-information | Official docs | Google provides free URL Removal tool in Search Console for exactly this workflow; documented step-by-step | 1 |
| 2026-11-12 | https://www.searchenginejournal.com/google-index-removal-tools/ | Industry editorial | SEJ article covers the standard free GSC workflow as the accepted solution; no mention of paid tooling gap | 1 |
| 2026-11-12 | https://reddit.com/r/TechSEO/ | Community scan | r/TechSEO (120k+ members) has scattered threads on bulk de-indexing; no recurring paid-tool request observed | 2 |

**Evidence count: 5 sources, all strength ≤ 2. Minimum threshold for `pass` requires ≥ 5 distinct pain quotes AND ≥ 1 willingness-to-pay signal. Neither bar is met.**

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| Google Search Console URL Removal Tool | Free (native) | $0 | Requires manual entry per URL batch (max 1,000/submission); tedious but functional for most cases |
| Google's Crawl Budget docs + 410 sitemap method | Free (DIY / tutorial) | $0 | Requires technical knowledge to implement; gap is purely knowledge, not tooling |
| Screaming Frog SEO Spider | Desktop SaaS | $259/year | Crawls and identifies URLs but does not automate GSC submission or sitemap generation for removal |
| Ahrefs / Semrush Site Audit | SaaS suite | $129–$499/month | Surface-level index health metrics; no bulk de-index workflow; overkill pricing for this single problem |
| IndexNow protocol | Free (standard) | $0 | Accelerates indexing of new content; not designed for de-indexing junk URLs |
| Manual developer scripting (Python + GSC API) | DIY | $0 (dev time) | Full solution via GSC Indexing API + sitemap submission; free but requires coding skill |

**Key finding:** The gap is a knowledge/friction gap, not a tooling gap. The free GSC URL Removal Tool handles up to 1,000 URLs per submission and is the documented canonical solution. For agencies handling thousands of URLs, a GSC API Python script is freely available on GitHub and well-documented. No paid product occupies this niche profitably because the free alternatives are genuinely adequate.

## Willingness-to-pay evidence

- Quote: No direct WTP quotes found. The source thread's author is seeking free advice, not expressing intent to purchase tooling. — webmasters.stackexchange.com, 2026-11-12
- Competitor pricing reference: No competitor product found that is specifically sold for bulk de-indexing acceleration. Adjacent SEO suites (Screaming Frog, Ahrefs) are purchased for broad SEO management, not this workflow.
- Paid job postings: Searches for "bulk de-indexing tool", "index cleanup SEO", and "Google index removal automation" on LinkedIn Jobs and Indeed return 0 dedicated tool-specific job listings. Technical SEO specialist roles mention GSC management generically.
- Marketplace listings: No Gumroad, AppSumo, or Product Hunt listings found for a dedicated bulk de-index tool (search conducted 2026-11-12).

**WTP verdict: No signal. Zero evidence of anyone paying for this specific workflow.**

## Estimated TAM / SAM

### Israel

- TAM: Approximately 400–600 technical SEO agencies/specialists in Israel who handle site migrations or legacy domain cleanups. At a one-time fee of $39/job and assuming 1–2 cleanup jobs per agency per year: 500 agencies × 1.5 jobs × $39 = **~$29,250/year**. This is below any viable product threshold.
- SAM (reachable in 12 months): ~100–150 agency leads via LinkedIn outreach; estimated conversion rate for a niche one-time tool with free alternatives: <5%. Expected revenue: **<$3,000**.

### Global

- TAM: Approximately 50,000–80,000 agencies/technical SEO specialists globally who might face this problem at least once. At $39/job, 1 job/year: 65,000 × $39 = **~$2.5M/year theoretical max**. However, annual recurrence is very low (domain cleanups are one-time events), and free alternatives cap real addressable share at <2%.
- SAM (reachable in 12 months): Via content SEO, r/TechSEO presence, and cold outreach: ~500–1,000 leads realistically engaged. At <3% conversion: **<$1,200 revenue in year 1**.

**TAM/SAM conclusion:** Even under optimistic assumptions, the revenue potential is negligible. The event is episodic (not recurring), the free solution is fully adequate, and no evidence of segment willingness to pay exists.

## Verdict: REJECT

**Fail reasons:**
1. **Insufficient pain signals**: Only 1 original signal (single forum post). The 5-source minimum is met in count but all are strength ≤ 2 and none are distinct pain quotes.
2. **Zero willingness-to-pay signal**: No competitor pricing for this specific problem, no marketplace listings, no job postings, no quotes expressing purchase intent.
3. **Free canonical solution exists**: Google Search Console URL Removal Tool and GSC API scripts solve this problem without payment. The gap is a knowledge gap, addressable by a free tutorial, not a paid tool.
4. **Episodic, non-recurring demand**: Domain cleanup is a one-time project event, not a recurring workflow — eliminates SaaS pricing model and makes customer acquisition cost economics very unfavorable.
5. **TAM too small**: Even global TAM under realistic conversion assumptions yields <$3,000 revenue in year 1.

**Recommendation:** Kill. Do not re-queue. If the SEO agency tooling space is of interest, redirect Market Radar to scan for recurring technical SEO pain (e.g., ongoing index health monitoring, schema markup automation, or Core Web Vitals reporting for agencies) where WTP evidence and recurring billing are documented.

## Source list

- https://webmasters.stackexchange.com/questions/150079/is-a-temporary-sitemap-of-410-urls-a-legitimate-way-to-get-googlebot-to-recrawl (retrieved 2026-11-12 IDT)
- https://webmasters.stackexchange.com/questions/tagged/sitemaps+410 (retrieved 2026-11-12 IDT)
- https://developers.google.com/search/docs/crawling-indexing/remove-information (retrieved 2026-11-12 IDT)
- https://support.google.com/webmasters/answer/9689846 (retrieved 2026-11-12 IDT)
- https://www.searchenginejournal.com/google-index-removal-tools/ (retrieved 2026-11-12 IDT)
- https://reddit.com/r/TechSEO/ (retrieved 2026-11-12 IDT)
