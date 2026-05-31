# QA Checklist

<!-- Run by the QA agent on every deliverable before send. Every box must be checked. A single fail means the deliverable goes back to the Delivery agent with the failing item logged. -->

## Pre-send checks

- [ ] **1. No PII leak.** No customer's internal data, credentials, API keys, employee names, or other identifying information appears in the deliverable except where the customer explicitly provided it for inclusion. No data from other customers appears anywhere.
- [ ] **2. No hallucinated facts.** Every external claim (number, quote, statistic, name, date, URL) is traceable to either the customer's inputs or a cited source. Spot-check 5 random claims by clicking through to the source.
- [ ] **3. All customer-provided inputs reflected back.** Every field collected via the onboarding form that's relevant to the deliverable is actually used or explicitly acknowledged as out-of-scope. Nothing the customer gave us is silently dropped.
- [ ] **4. Links work.** Every hyperlink in the deliverable returns HTTP 200 (or the expected non-200 for paywalled sources). Tested via automated link checker or manual sample of 100% if N < 20, 20% if N >= 20.
- [ ] **5. Brand voice consistent.** Tone matches `landing_page_copy.md` voice notes. No marketing fluff inside the deliverable. No words from the operator's forbidden list if one exists.
- [ ] **6. Pricing accurate.** Any pricing mentioned in the deliverable matches `pricing.md` exactly. No stale numbers, no rounding errors, correct currency and VAT treatment.
- [ ] **7. No off-topic content.** Nothing outside the scope defined in `offer.md` "What's included". No upsells embedded in the body. (One closing line referencing other services is acceptable in the cover-letter email, not in the deliverable itself.)
- [ ] **8. File naming convention followed.** Filenames match the pattern defined in `delivery_workflow.md` (e.g., `<slug>_<customer>_<YYYY-MM-DD>.pdf`). No spaces, no special characters, lowercase.
- [ ] **9. Deliverable matches `report_template.md` shape.** All required sections present and non-empty: Cover, Executive summary, Findings, Recommendations, Next steps, About this report. No placeholder text remains.
- [ ] **10. Time-to-deliver within SLA.** Elapsed time from payment confirmation to ready-to-send is within the SLA defined in `delivery_workflow.md`. If late, escalate per `support_policy.md`.
- [ ] **11. Payment confirmed before send.** Stripe shows `payment_intent.succeeded` for this customer's charge. No send without confirmed payment (unless the offer is post-delivery payment, in which case the invoice must be queued and noted here).

## QA log

<!-- One row per QA run. Append-only. -->

| Run ID | Date (IDT) | Reviewer agent | Pass | Failed items | Notes |
|---|---|---|---|---|---|
| <!-- qa-001 --> | <!-- YYYY-MM-DD HH:MM --> | <!-- QA agent --> | <!-- yes/no --> | <!-- list item numbers if any --> | <!-- ... --> |
