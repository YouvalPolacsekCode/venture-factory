# Launch Checklist

<!-- The gate between "building" and "launched". Every box must be checked, with the verifying agent name and timestamp (IDT) noted in the log at the bottom. Operator gives final go. -->

## Pre-launch gates

- [ ] **1. Offer signed off.** `offer.md` is fully populated, operator has read and approved. No EXAMPLE ONLY content remaining.
- [ ] **2. Landing page approved and published.** `landing_page_copy.md` finalised, page deployed at production URL, mobile + desktop verified, all CTAs route to the correct destinations.
- [ ] **3. Payment path tested with a 1-USD test charge.** Real card put through Stripe end-to-end: form -> Payment Link -> charge -> receipt -> webhook fires -> operator audit trail row written. Test charge refunded.
- [ ] **4. Support email live.** Inbox monitored by Support agent, autoresponder confirms receipt, escalation rules from `support_policy.md` configured.
- [ ] **5. QA checklist green on a dry-run delivery.** One synthetic customer pushed through the full delivery workflow; all 11 items in `qa_checklist.md` pass.
- [ ] **6. Analytics events firing.** Every funnel-stage event from `metrics.md` confirmed in the analytics tool: impressions, clicks, form starts, form completions, paid, delivered.
- [ ] **7. Approval policy entries added if new action types.** Any new action types introduced by this service have been added to `config/approval_policy.yaml` and signed off by the operator.
- [ ] **8. Kill-thresholds in `config/cost_gain_model.yaml` confirmed.** This service's kill conditions (cost > X, gain < Y, time-to-first-paid > Z days) are entered and the Reporting agent will trip them.
- [ ] **9. Daily summary picks up this service.** Reporting agent's daily 18:00 IDT digest includes this service's funnel + spend in tomorrow's run. Verified by viewing the next scheduled summary preview.
- [ ] **10. First outreach batch approved.** Cohort selected per `responsiveness_test.md`, message variants reviewed, batch queued and approved by operator per `automation_plan.md`.

## Launch log

<!-- One row per gate-check pass. Append-only. -->

| Item # | Verifier agent | Timestamp (IDT) | Pass | Notes / link to evidence |
|---|---|---|---|---|
| <!-- 1 --> | <!-- Builder agent --> | <!-- YYYY-MM-DD HH:MM --> | <!-- yes --> | <!-- e.g., commit hash, screenshot path --> |

## Go / no-go

- Operator final approval: <!-- yes / no -->
- Approval timestamp (IDT): <!-- YYYY-MM-DD HH:MM -->
- Launch date (IDT): <!-- YYYY-MM-DD -->
