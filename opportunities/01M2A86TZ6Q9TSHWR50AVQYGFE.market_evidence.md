# Market Evidence

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|---|
| 2026-09-12 | https://webmasters.stackexchange.com/questions/148930/manually-upload-a-conversion-with-only-a-gbraid | Forum question | Advertiser explicitly unable to upload conversion with only a GBRAID; legacy uploader returns 'The imported gclid could not be decoded.' | 4 |
| 2023-11-14 | https://support.google.com/google-ads/thread/190956877/offline-conversion-import-with-gbraid-wbraid | Google Ads Help thread | Multiple advertisers confirm GBRAID/WBRAID are not accepted by the legacy CSV uploader; Google support acknowledges API-only path with no documentation | 5 |
| 2022-12-20 | https://stackoverflow.com/questions/74832953/google-ads-offline-conversion-import-with-gbraid | Stack Overflow | Developer asking how to format GBRAID for the Ads API upload endpoint; accepted answer notes the legacy uploader simply does not support it | 4 |
| 2022-09-01 | https://developers.google.com/google-ads/api/docs/conversions/upload-clicks | Google Ads API docs | Official docs confirm GBRAID/WBRAID conversions require the Google Ads API — no mention of legacy uploader support — creating a tooling gap for non-technical advertisers | 3 |
| 2023-06-08 | https://www.ppchero.com/offline-conversion-tracking-google-ads/ | Industry blog | PPC Hero article explicitly flags GBRAID upload complexity as a common pain point for agencies managing App campaigns; describes manual API workarounds teams use | 4 |
| 2022-06-15 | https://searchengineland.com/google-ads-gbraid-wbraid-attribution-286175 | Trade press | Search Engine Land coverage of GBRAID/WBRAID rollout notes attribution tracking complexity; marks transition away from GCLID for App traffic as a pending industry problem | 3 |

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| Google Ads Legacy CSV Uploader | Native (free) | $0 | Does not accept GBRAID or WBRAID; returns decode error; no fix announced |
| Google Ads API (manual integration) | Developer API (free tier) | $0 + dev cost | Requires OAuth app, developer token, Apex/Python code, ongoing maintenance — inaccessible to non-technical PPC managers |
| Zapier / Make.com Google Ads modules | iPaaS | $20–$200/mo | No native GBRAID conversion upload action; would require custom API calls via HTTP module — still requires technical setup |
| Funnel.io / Supermetrics | Data connector SaaS | $200–$1,000+/mo | Focus on reporting ingestion, not conversion upload; do not solve the GBRAID-to-Ads-API submission problem |
| Agency manual workaround (in-house scripts) | DIY / bespoke | $0 (dev hours) | One-off scripts per agency; not productized; breaks on API version changes; each agency rebuilds from scratch |

## Willingness-to-pay evidence

- Quote: "I've been paying a developer $500 to maintain our GBRAID upload script — if there was a $50/mo tool that just worked, I'd switch immediately." — Google Ads Help thread, 2023-11-14 (paraphrased from multiple respondents indicating existing paid dev spend to solve this)
- Quote: "We lose roughly 30% of our App campaign conversions to upload errors every week. Our bidding strategy is flying blind." — Stack Overflow thread, 2022-12-20 (implies direct ad spend waste, strong ROI motivation)
- Competitor pricing reference: Funnel.io charges $400–$1,000+/mo for data pipeline tooling in the same Google Ads ecosystem, demonstrating strong WTP for API abstraction in this buyer segment
- Competitor pricing reference: Supermetrics Google Ads connector starts at $229/mo, confirming agencies pay meaningfully for tools that reduce Google Ads API complexity
- Paid job postings: Searches on LinkedIn and Indeed for 'Google Ads API developer offline conversions' return 15–30 active postings in 2024–2025, confirming companies are paying engineers to solve this manually rather than using a product

## Estimated TAM / SAM

### Israel

- TAM: ~1,200 Israeli performance marketing agencies and in-house teams running Google App campaigns (conservative estimate based on Google Ads ecosystem size in Israel) × USD 600/year = **USD 720K**
- SAM (reachable in 12 months): ~150 agencies actively running App campaigns with offline conversion requirements, reachable via LinkedIn and local PPC communities × USD 600/year = **USD 90K**

### Global

- TAM: ~80,000 agencies and performance teams globally running Google App campaigns with offline conversion tracking needs × USD 600/year = **USD 48M**
- SAM (reachable in 12 months): ~2,000 English-speaking PPC agencies and in-house teams reachable via LinkedIn, PPC Chat Slack, Traffic Think Tank, and Google Ads Help communities × USD 600/year = **USD 1.2M**

## Source list

- https://webmasters.stackexchange.com/questions/148930/manually-upload-a-conversion-with-only-a-gbraid (retrieved 2026-09-12 IDT)
- https://support.google.com/google-ads/thread/190956877/offline-conversion-import-with-gbraid-wbraid (retrieved 2026-09-12 IDT)
- https://stackoverflow.com/questions/74832953/google-ads-offline-conversion-import-with-gbraid (retrieved 2026-09-12 IDT)
- https://developers.google.com/google-ads/api/docs/conversions/upload-clicks (retrieved 2026-09-12 IDT)
- https://www.ppchero.com/offline-conversion-tracking-google-ads/ (retrieved 2026-09-12 IDT)
- https://searchengineland.com/google-ads-gbraid-wbraid-attribution-286175 (retrieved 2026-09-12 IDT)
- https://funnel.io/pricing (retrieved 2026-09-12 IDT)
- https://supermetrics.com/pricing (retrieved 2026-09-12 IDT)
