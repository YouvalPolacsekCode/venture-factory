# Market Evidence

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|---|
| 2026-09-19 | https://salesforce.stackexchange.com/questions/439858/how-to-override-the-default-standard-email-field-matching-to-use-custom-email-ad | Stack Exchange question | Single admin stuck on EAC custom email-field matching override; no accepted answer, low vote count | 2 |

**Evidence gap summary:** One signal. The Pain Validation threshold requires ≥5 distinct pain quotes from distinct sources. No Reddit threads, no Trailblazer Community posts, no AppExchange reviews, no LinkedIn complaints, and no Salesforce IdeaExchange votes were found for this specific configuration problem. The broader EAC dissatisfaction space has more signal, but that is a different (and already-saturated) problem.

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| Salesforce SI / consulting partner | Agency | $150–$300/hr | Solves it but expensive; most orgs just escalate to their partner | 
| Salesforce Trailblazer Community / Stack Exchange | DIY / status quo | Free | No working implementation exists yet; community has not produced an answer | 
| Salesforce Support (Premier) | Vendor support | Included in Enterprise/Unlimited | Slow; Salesforce often deflects EAC configuration issues as "working as designed" | 

## Willingness-to-pay evidence

- Quote: None found. No prospect has asked "is there a paid guide for this?" or offered to pay for a solution in any thread discovered.
- Competitor pricing reference: No competitor product or paid guide targeting EAC custom email-field matching was found on Gumroad, AppExchange, or Udemy.
- Paid job postings: Zero job postings found that list EAC custom email-field matching as a required or desired skill.

**Verdict on WTP:** Fails. Zero willingness-to-pay signals found. The Salesforce ecosystem does support paid implementation guides (e.g., Gumroad guides, AppExchange mini-apps), but none exist for this problem — which is more likely evidence of insufficient demand than an untapped gap.

## Estimated TAM / SAM

### Israel

- TAM: Salesforce enterprise orgs in Israel using EAC ≈ ~200–400 companies (Salesforce has ~1,500 Israeli customers total; EAC adoption rate among Enterprise/Unlimited tiers ≈ 20–30%). Of those, orgs with custom email address fields needing the override ≈ ~50–100. At $49–99 one-time: **TAM ≈ USD 2,500–9,900**. Below any viable threshold.
- SAM (reachable in 12 months): ~20–40 admins who could be reached via LinkedIn or Trailblazer Community. **SAM ≈ USD 1,000–4,000**.

### Global

- TAM: ~150,000 Salesforce Enterprise/Unlimited orgs globally; EAC active users ≈ ~30,000; orgs with custom email field override need ≈ ~3,000–5,000. At $49–99 one-time: **TAM ≈ USD 147K–495K** (ceiling, one-time, no recurrence).
- SAM (reachable in 12 months): Via Stack Exchange, Trailblazer Community, r/salesforce organic posts ≈ ~300–500 reachable leads. **SAM ≈ USD 14,700–49,500**.

Neither figure justifies investment. The one-time nature of the purchase and the trivial copyability of a written guide make the economics unattractive.

## Source list

- https://salesforce.stackexchange.com/questions/439858/how-to-override-the-default-standard-email-field-matching-to-use-custom-email-ad (retrieved 2026-09-19 IDT)

---

**Verdict: REJECTED**

Fails the minimum evidence threshold (1 pain quote vs. required 5), fails the willingness-to-pay check (0 signals), and TAM arithmetic does not support investment even in a best-case scenario. Recommend closing this candidate. If the Market Radar repeatedly surfaces EAC dissatisfaction signals at broader scope (e.g., EAC sync reliability, data hygiene across all EAC-matched records), that wider problem may warrant a fresh candidate.