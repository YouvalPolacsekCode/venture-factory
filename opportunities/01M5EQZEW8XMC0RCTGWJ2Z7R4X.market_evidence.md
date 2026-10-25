# Market Evidence

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|---|
| 2026-10-21 | https://news.ycombinator.com/item?id=50164771 | HN comment | Single operator calculating $35/hr net per GPU card against $30k hardware cost, estimating 35-day break-even | 2 |

**Evidence count: 1 — below the required minimum of 5 distinct pain quotes. Verdict: FAIL.**

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| Excel / Google Sheets | DIY | Free | Requires manual setup but fully capable for this calculation; no gap severe enough to drive paid adoption |
| RunPod / Lambda Labs pricing pages | Status quo / vendor tools | Free | Vendor-provided, not operator-controlled; no peak/off-peak blended modelling |
| Generic ROI calculator templates | DIY / free tools | Free | Not LLM-inference-specific but close enough for most operators |

## Willingness-to-pay evidence

- Quote: "At $35/hour in net cash generation per card, a $30,000 GPU would pay for itself entirely in about 850 hours" — HN comment, 2026-10-21 (implies operator is doing this math manually, not that they'd pay for a tool to do it)
- Competitor pricing reference: None identified — no paid GPU ROI calculator product found
- Paid job postings: None identified for this specific function

**Assessment:** The commenter is doing the math in a forum post with arithmetic — the free substitution (back-of-envelope calculation) is already working for them. No signal that they would pay for a dedicated tool.

## Estimated TAM / SAM

### Israel
- TAM: Estimated <50 serious on-premise LLM inference operators in Israel × $200/year (one-time tool) = ~$10,000 — not material
- SAM (reachable in 12 months): <20 operators

### Global
- TAM: Estimated 500–2,000 serious operators globally × $49 one-time = $25k–$98k total addressable — insufficient for a sustainable micro-SaaS
- SAM (reachable in 12 months): ~200 operators via HN/r/LocalLLaMA outreach

## Source list

- https://news.ycombinator.com/item?id=50164771 (retrieved 2026-10-21 IDT)

---
**Verdict: REJECTED.** Single data point, no corroborating pain evidence, free substitutes fully capable, market too small. Recommend killing — do not re-queue unless Market Radar surfaces a cluster of 5+ independent signals.