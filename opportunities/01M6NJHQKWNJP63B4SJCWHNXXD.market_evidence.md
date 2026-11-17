# Market Evidence

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|---|
| 2026-11-05 | https://news.ycombinator.com/item?id=50355278 | HN comment | One commenter compared monthly GitHub Actions cost vs. M4 Mac mini price and bought hardware | 2 |

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| Manual spreadsheet | DIY | Free | Exists but takes time; not shareable or updatable |
| GitHub's own cost estimator (Actions billing page) | Built-in | Free | Shows spend but no hardware ROI projection |
| Blog posts (e.g., "self-hosted runners cost analysis") | Content | Free | Generic, not personalized to team's actual minute usage |
| Actuated.dev | SaaS (managed runners) | ~$0.04/min | Sells alternative runners, not a decision tool |

## Willingness-to-pay evidence

- Quote: "I looked at our GitHub Actions monthly expenses, then at the price of a M4 Mac mini… and decided to buy one as it would pay for itself in less than a year." — HN, 2026-11-05 (commenter paid for hardware, not a tool)
- Competitor pricing reference: No competitor found charging money specifically for a CI break-even calculator. Actuated.dev sells alternative runners but not the decision layer.
- Paid job postings: No job postings found specifically for CI cost analysis tooling.

## Estimated TAM / SAM

### Israel
- TAM: Approximately 500 Israeli software companies running macOS CI (conservative estimate of 10% of ~5,000 tech companies) × USD 29 one-time = USD 14,500. Negligible.
- SAM (reachable in 12 months): ~100 companies actively evaluating self-hosted runners × USD 29 = USD 2,900.

### Global
- TAM: ~50,000 teams globally running macOS CI on GitHub Actions × USD 29 one-time = USD 1.45M (ceiling, one-time purchase, not recurring).
- SAM (reachable in 12 months): ~5,000 teams actively evaluating this decision × USD 29 = USD 145,000.

## Verdict: FAIL

**Evidence count:** 1 pain quote (threshold: 5). **WTP signals:** 0 direct (threshold: 1). The pain is a one-time calculation, not a recurring workflow; free spreadsheets and blog posts already serve it. TAM is too small and one-time to support a sustainable micro-SaaS.

## Source list

- https://news.ycombinator.com/item?id=50355278 (retrieved 2026-11-05 IDT)
