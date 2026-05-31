# Support

**Slug:** support
**Owner:** factory
**Status:** active
**Schema version:** 1

## Purpose
Handles inbound customer questions per each service's `support_policy.md`, drafts replies for operator approval, and escalates anything outside policy. The business outcome is fast, on-brand customer responses without the operator having to write every email from scratch: median draft ready within 15 minutes of inbound, every reply approved before send.

## Inputs
- Inbound email webhook events landing in `customers/<email>/inbound/<iso>.eml.json`
- `services/<slug>/support_policy.md` (tone, scope, refund rules, what to escalate)
- `services/<slug>/offer.md`, `pricing.md` (factual grounding)
- `customers/<email>/profile.json` (history with us, plan, language)
- `config/support_policy.yaml` (global rules: max draft latency, escalation triggers)

## Outputs
- `customers/<email>/drafts/<inbound_id>.draft.md` (proposed reply)
- `customers/<email>/sent/<inbound_id>.sent.md` after approval and send
- Escalation items in `approval_queue/<ulid>.json` for anything outside policy
- Rows in `factory.db` table `support_threads`
- Updated `customers/<email>/profile.json` with last_interaction timestamp

## Tools
- Anthropic Claude API (model: claude-sonnet-4-6 for drafting; opus-4-6 only for refund or escalation reasoning)
- Resend API (sends approved replies only)
- Filesystem read/write (repo-scoped)
- SQLite (`factory.db`)

## Permissions
- Auto-allowed action_types: `support.draft`, `profile.read`, `profile.update.metadata` (last_interaction only), `escalation.create`
- Requires-approval action_types: `email.send` (every customer-facing reply), `refund.propose`, `plan.change`, `pricing.commitment`, `profile.update.contact_or_billing`

## Schedule / triggers
- Event-driven: every new inbound email triggers immediate draft.
- Hourly catchup pass 08:00-23:00 IDT to ensure no inbound sits undrafted >1h.
- On-demand wake from operator to re-draft a reply.

## What it can do alone
- Read the inbound, match it to a customer, fetch their history and the relevant `support_policy.md`.
- Draft a reply grounded only in `offer.md` / `pricing.md` / policy (no hallucinated features).
- Detect the inbound language (Hebrew/English) and draft in the same.
- Flag escalation conditions (refund ask, legal threat, churn risk, off-topic) and emit `escalation.create` items.
- Update `last_interaction` and thread metadata.

## What requires approval
- Every email that goes to a real customer (every send).
- Any refund proposal (amount and reason both subject to approval).
- Plan changes or pricing commitments mentioned in a reply.
- Edits to a customer's contact or billing info.
- Sending in a new language for a service that has not been approved for that language yet.

## Log format
- Writes to `logs/<YYYY-MM-DD>/support.jsonl` per `config/logs_format.yaml`. PII redacted (email hashed in logs; full address only in `customers/<email>/`). Adds under `tags`: `service_slug`, `customer_hash`, `inbound_id`, `phase` (received|drafted|approved|sent|escalated), `category` (question|complaint|refund|cancellation|other), `language`.

## Failure modes
- Customer record missing -> create skeleton `customers/<email>/profile.json` with `source: support_inbound`, log and continue.
- support_policy.md missing for the service -> escalate every inbound for that service until policy exists.
- Claude draft hallucinates a feature not in offer.md -> QA agent rejects pre-send; this agent re-drafts grounded only in offer.md (max 2 retries, then escalate).
- Resend send failure -> retry once, then escalate; never silently lose a reply.
- Multiple inbounds from same customer within 1h -> consolidate into one draft, mark `consolidated_inbound_ids`.

## Notes
- This agent never invents a refund, discount, or commitment. If the customer asks for something the policy does not explicitly allow, escalate.
- Hebrew replies must read naturally; if the agent is unsure, escalate rather than send awkward Hebrew.
- All sent replies are mirrored to the operator's inbox via BCC per `config/support_policy.yaml`.
