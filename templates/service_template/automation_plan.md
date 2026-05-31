# Automation Plan

<!-- What runs without humans, what waits for approval, what stays manual. Updated whenever a step moves between categories. -->

## Fully automated steps

<!-- Agent runs these without operator approval. Errors raise an alert but don't block other steps. -->

| Step | Owner agent | Trigger | Failure handling |
|---|---|---|---|
| Lead enrichment from public sources | Research agent | New lead added to `leads/inbox/` | Skip enrichment, flag lead for manual review |
| Outreach send (cohort already approved) | Outreach agent | Daily 09:00 IDT cron | Pause channel if bounce rate > 5% |
| Intake form -> Stripe Payment Link issuance | Payment agent | Form webhook | Retry 3x, then alert operator |
| Stripe receipt forwarding | Payment agent | `payment_intent.succeeded` webhook | Retry from Stripe event log |
| Delivery agent draft generation | Delivery agent | Payment confirmed + intake validated | Pause, write to `work/<customer>/blockers.md` |
| QA agent automated checks (links, file naming, PII regex) | QA agent | Draft ready | Block send, route back to Delivery |
| Daily summary to operator | Reporting agent | Daily 18:00 IDT cron | Retry; if fails twice, send minimal email |

## Approval-gated steps

<!-- Require operator approval per `config/approval_policy.yaml`. Agent prepares and queues; operator clicks approve. -->

| Step | Owner agent | Approval policy entry | Why gated |
|---|---|---|---|
| New cohort outreach launch (>20 recipients) | Outreach agent | `outreach.new_cohort` | Reputation + compliance risk |
| Send final deliverable to customer | Delivery agent | `delivery.send_final` | First-time per service; can be auto-graduated after N clean sends |
| Issue refund | Payment agent | `payment.refund` | Money out |
| Publish new landing page or change pricing | Builder agent | `web.publish` | Public-facing change |
| Add a new agent action type | Builder agent | `meta.new_action_type` | Governance |

## Manual-only steps

<!-- Operator does these in person. -->

- Sign-off on Build Decision for a new experiment.
- Quarterly review of suppression list and consent records.
- Direct customer call when a P1 escalation needs a human voice.
- Filing of Israeli tax returns and VAT reports (accountant + operator, never an agent).
- Hiring or firing a tool / vendor.

## Cutover plan

<!-- Timeline to move steps from manual -> approval-gated -> fully automated. Each cutover requires N consecutive clean runs at the prior stage. -->

| Step | Current | Target | Gate criteria | Target date |
|---|---|---|---|---|
| <!-- Send final deliverable --> | <!-- approval-gated --> | <!-- fully automated --> | <!-- 10 consecutive QA-clean sends with zero customer complaints --> | <!-- YYYY-MM-DD IDT --> |
| <!-- ... --> | <!-- ... --> | <!-- ... --> | <!-- ... --> | <!-- ... --> |

## Risks of over-automation

<!-- Document the failure modes so we don't sleepwalk into them. -->

- **Silent quality drift.** Auto-send hides slow degradation. Mitigation: sample 10% of auto-sent deliverables for weekly human review.
- **Compliance blast radius.** A single bad cohort can email thousands before anyone notices. Mitigation: hard rate-limit per channel per day; pause on bounce-rate spike.
- **Refund cascades.** Auto-refund logic can drain funds if abused. Mitigation: keep `payment.refund` approval-gated; cap auto-refundable amount per day.
- **Wrong-customer delivery.** Auto-routing on a malformed intake can send Customer A's report to Customer B. Mitigation: QA agent must match intake-id to deliverable-id on every send.
- **Loss of learning.** Over-automation removes the operator's exposure to real customer friction. Mitigation: operator reads 5 random support threads per week even when none are escalated.
