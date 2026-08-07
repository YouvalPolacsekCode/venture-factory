# Market Evidence

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|---|
| 2026-08-04 | https://salesforce.stackexchange.com/questions/439721/prevent-email-to-case-from-creating-multiple-cases-when-an-email-lists-several-r | StackExchange question | Salesforce admin with production Email-to-Case setup hit duplicate-case creation from a single multi-address email; requested three distinct mitigation options | 3 |

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| Native Salesforce Flow | DIY (no-code) | Free (included in SF license) | Cannot natively detect cross-queue duplicate cases triggered by the same inbound message-ID |
| Apex trigger (custom code) | DIY (custom dev) | $0 + dev time | Requires Salesforce developer; no packaged solution; per-org maintenance burden |
| AppExchange dedup tools (e.g. DemandTools, Cloudingo) | SaaS | $600–$2,400+/yr | Focused on contact/lead deduplication, not Email-to-Case routing dedup at ingest time |
| Manual queue review | Status quo | Staff time (~15–30 min/incident) | Entirely manual; agents must identify and close duplicates case-by-case |

## Willingness-to-pay evidence

- Quote: No explicit "I would pay" quote found in source material.
- Competitor pricing reference: AppExchange deduplication tools (DemandTools by CRMFusion) list at ~$1,200–$2,400/yr for org-wide dedup; indicates ecosystem WTP for dedup tooling generally.
- Paid job postings: Salesforce admin/developer roles routinely list Email-to-Case configuration as a required skill, implying ongoing organizational investment, but no specific job posts for this sub-problem found.

## Estimated TAM / SAM

### Israel

- TAM: Estimated 400–600 Israeli companies running Salesforce Service Cloud (enterprise/mid-market) × ~$600/yr for a point AppExchange solution = ~$240K–$360K
- SAM (reachable in 12 months): ~100 Salesforce admins reachable via LinkedIn + Salesforce Israel community × $600/yr = ~$60K

### Global

- TAM: ~150,000 Salesforce Service Cloud orgs globally × $600/yr = ~$90M (theoretical ceiling; realistic share is a small fraction)
- SAM (reachable in 12 months): AppExchange listing + targeted Trailblazer Community outreach could reach ~2,000–5,000 orgs in year 1 × $600/yr = ~$1.2M–$3M

## Source list

- https://salesforce.stackexchange.com/questions/439721/prevent-email-to-case-from-creating-multiple-cases-when-an-email-lists-several-r (retrieved 2026-08-04 IDT)

---

**Verdict: REJECTED**

Evidence count is insufficient (1 distinct pain source vs. 5 required). No explicit willingness-to-pay quote found. Critically, both build gates fail: solution requires Salesforce Apex/Flow/managed-package engineering and per-org deployment that is outside factory tooling capabilities. Recommend parking until a Salesforce ISV technical co-builder is identified and additional pain signals (≥5 distinct sources) are gathered.