# Market Evidence

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|---|
| 2026-09-29 | https://news.ycombinator.com/item?id=49886890 | HN thread | Tell HN post reporting Firebase server-side change causing iOS crashes across multiple production apps; 7 points, limited comments | 2 |
| 2026-09-29 | https://github.com/firebase/firebase-ios-sdk/issues/16728 | GitHub issue | Confirmed widespread impact on production apps from a Firebase SDK regression; multiple reporters | 3 |

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| Firebase Crashlytics | SaaS (Google) | Free (bundled) | Reports crashes after they hit users; no early-warning or canary layer; no SDK-health trend view |
| Sentry / Bugsnag | SaaS | $26–$80/month | General crash monitoring; no Firebase-SDK-specific regression detection or upstream health signal |
| PagerDuty / OpsGenie | SaaS | $19–$59/user/month | Alert routing only; no Firebase-aware monitoring data source |
| Status pages (Firebase Status Dashboard) | DIY / manual check | Free | Reactive, no push alerting, no per-app impact scoping |

## Willingness-to-pay evidence

- Quote: No direct willingness-to-pay quotes found in source material. The HN post and GitHub issue contain technical frustration but no 'I would pay for X' statements.
- Competitor pricing reference: Crashlytics is free and bundled with Firebase; Sentry charges $26+/month for crash monitoring but is not Firebase-specific. No direct competitor exists in the Firebase-SDK canary alerting niche—absence of competitors may reflect absence of market rather than a gap.
- Paid job postings: No job postings found for 'Firebase SDK monitoring' or 'mobile dependency health' roles that would signal employers paying for this work to be done manually.

## Estimated TAM / SAM

### Israel

- TAM: Approximately 1,500–2,500 Israeli mobile app studios and product companies using Firebase (estimated from AppStore developer registrations and local startup ecosystem counts) × USD 400/year = USD 600K–1M. Market is too small domestically to anchor a product.
- SAM (reachable in 12 months): ~300 teams actively building iOS apps on Firebase, reachable via Firebase Slack Israel channel and local tech communities.

### Global

- TAM: Firebase reports ~3.9M monthly active apps (2024 Google I/O data); subset using Firebase on iOS estimated at ~800K apps, but the pain is specifically acute for teams with paying users and high crash sensitivity—roughly 50,000 professional/commercial teams × USD 400/year = USD 20M theoretical TAM.
- SAM (reachable in 12 months): ~5,000 teams reachable via Firebase GitHub issues, r/iOSProgramming, and Firebase Slack communities. USD 2M SAM at best, but frequency of the triggering event (Firebase regression) is low—estimated once or twice per year—undermining recurring subscription logic.

## Verdict: REJECTED

**Reason 1 — Frequency does not support subscription:** Firebase server-side regressions severe enough to cause widespread app crashes appear to occur a few times per year at most. A team would pay a monthly subscription to protect against an event that happens twice annually. The value proposition weakens sharply when the triggering event is rare.

**Reason 2 — No willingness-to-pay signal:** Zero quotes, zero competitor pricing in this niche, zero paid workarounds documented. Indirect signals (teams pay Firebase bills and developer salaries) are too weak to justify advancing.

**Reason 3 — Build gates fail:** `buildability_with_ai = 5` (floor: 6) and `operational_autonomy = 5` (floor: 7) both fail minimum thresholds. The monitoring layer requires per-customer instrumentation that cannot be delivered autonomously by this factory without a technical co-builder. Even a strong validate result cannot lead to a build under current constraints.

**Recommendation:** Archive. If Firebase regression frequency increases (e.g., multiple incidents per quarter become a pattern), re-surface via Market Radar with updated frequency evidence.

## Source list

- https://news.ycombinator.com/item?id=49886890 (retrieved 2026-09-29 IDT)
- https://github.com/firebase/firebase-ios-sdk/issues/16728 (retrieved 2026-09-29 IDT)
