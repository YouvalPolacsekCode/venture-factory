# Market Evidence

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|---|
| 2026-08-06 | https://salesforce.stackexchange.com/questions/439731/change-data-capture-changeeventheader-changedfields-doesnt-contain-fields-that | Stack Exchange question | Single developer hitting undocumented CDC permission-leakage behavior causing silent field omission in change events | 2 |

**Evidence gap:** No additional corroborating threads found via discovery. No Reddit, HN, or Trailblazer Community discussions surfaced on this specific CDC edge case. No competitor product exists targeting this issue specifically.

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| Salesforce Official Docs | Free documentation | $0 | Underdocumented edge case; the question itself reveals docs are silent on commitUser permission interaction |
| Stack Overflow / SFSE community answers | DIY / free | $0 | Partial answers exist but no authoritative resolution confirmed |
| Salesforce consultants | Agency | $150–$300/hr | Overkill for a one-time debug; no recurring engagement |

## Willingness-to-pay evidence

- Quote: No direct WTP quotes found. The single source is a question, not a complaint about cost or a request for a paid tool.
- Competitor pricing reference: No competitors found targeting Salesforce CDC permission-leakage diagnostics specifically.
- Paid job postings: Zero postings found referencing this specific CDC behavior.

## Estimated TAM / SAM

### Israel
- TAM: Salesforce Enterprise/Unlimited customers in Israel ≈ ~500–800 orgs (estimate based on Salesforce Israel market presence). Of those, the subset running CDC-based integrations who hit this specific edge case is estimated at <50 developers at any given time. At a one-time $49 guide price: ~$2,450 total. Not viable.
- SAM (reachable in 12 months): <20 developers; effectively zero recurring revenue.

### Global
- TAM: Globally, Salesforce has ~150,000 enterprise customers. CDC users are a subset; CDC users hitting this specific permission edge case are a further subset estimated at <1,000 developers globally in any 12-month window. At $49 one-time: ~$49,000 total addressable — thin for a standalone product.
- SAM (reachable in 12 months): ~200–500 developers discoverable via Stack Exchange, Trailblazer Community, and LinkedIn. One-time purchase ceiling ~$10,000–$25,000 with no recurring layer.

## Verdict: FAIL

Does not meet the minimum evidence bar (5 distinct pain quotes: **0 found**; willingness-to-pay signal: **none**; clear recurring buyer: **no**). Problem is real but narrow, episodic, and commercially thin. Recommend leaving in `opportunities/` as dropped. No promotion to experiments.

## Source list

- https://salesforce.stackexchange.com/questions/439731/change-data-capture-changeeventheader-changedfields-doesnt-contain-fields-that (retrieved 2026-08-06 IDT)
