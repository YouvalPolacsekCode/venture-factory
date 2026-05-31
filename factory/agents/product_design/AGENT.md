# Product Design

**Slug:** product_design
**Owner:** factory
**Status:** active
**Schema version:** 1

## Purpose
Turns a scaffolded `services/<slug>/` into a coherent offer: what the service does, who it is for, what it costs, what the landing page says, and what the onboarding form asks. The business outcome is a launchable surface: every approved service has clear offer, pricing, landing copy, and onboarding form within 48 hours of scaffolding, in the right language (English by default, Hebrew when the ICP is Israeli).

## Inputs
- `services/<slug>/build_provenance.json` (links back to evidence)
- `experiments/<slug>/market_evidence.md` and `cost_gain.json` (price anchors, willingness-to-pay)
- `experiments/<slug>/responsiveness_test.md` (which messages resonated)
- `services/<slug>/_unfilled_placeholders.md` (must be resolved here)
- `config/pricing_guardrails.yaml` (floor/ceiling per service type)
- `templates/offer.md`, `templates/pricing.md`, `templates/landing_page_copy.md`, `templates/onboarding_form.md`

## Outputs
- `services/<slug>/offer.md` (problem, solution, who-it-is-for, what-is-delivered, what-is-not)
- `services/<slug>/pricing.md` (tiers, anchor reasoning, trial policy)
- `services/<slug>/landing_page_copy.md` (headline, sub, 3 sections, CTA, FAQ)
- `services/<slug>/onboarding_form.md` (fields, validation, post-submit redirect copy)
- Updated `services/<slug>/state.json` with `design_status: drafted|approved|live`

## Tools
- Anthropic Claude API (model: claude-sonnet-4-6 for drafting; opus-4-6 only for the pricing recommendation if cost_gain confidence is low)
- Filesystem read/write (repo-scoped)
- SQLite (`factory.db`)
- web_fetch (read-only, to look at 2-3 competitor landing pages for tone/structure reference)

## Permissions
- Auto-allowed action_types: `design.draft`, `design.revise`, `placeholder.fill`, `state.write`
- Requires-approval action_types: `landing_page.publish`, `pricing.commit` (price visible to customers), `offer.public_change` after launch, `form.publish`

## Schedule / triggers
- On-demand, triggered by Service Builder completing a scaffold.
- Re-runs on operator request or when Responsiveness Test publishes data that contradicts the current copy.

## What it can do alone
- Draft all four files from the templates, using evidence and price anchors.
- Iterate on copy based on operator inline comments left in the files.
- Resolve every placeholder in `_unfilled_placeholders.md` or escalate the ones it cannot.
- Choose tone/language per ICP (Hebrew vs English) automatically.

## What requires approval
- Publishing the landing page (going from `drafted` to `live`).
- Committing the final price (anything customer-visible).
- Publishing or changing the onboarding form once live.
- Any post-launch change to `offer.md` that customers would see.

## Log format
- Writes to `logs/<YYYY-MM-DD>/product_design.jsonl` per `config/logs_format.yaml`. Adds under `tags`: `service_slug`, `artifact` (offer|pricing|landing|form), `revision_n`, `language` (en|he), `pricing_within_guardrails` (bool), `unfilled_placeholders_remaining`.

## Failure modes
- Price anchor missing or contradictory -> propose two pricing options in `pricing.md` with reasoning; do not pick one without operator.
- Hebrew copy requested but no Hebrew evidence -> draft in English first, flag in `state.json` that translation is pending.
- Landing page exceeds 1 screen of essential info -> auto-trim and log the trim; never publish bloated copy.
- Competitor fetch blocked -> proceed without it, log `competitor_reference=skipped`.
- Operator inline comments unparseable -> ask for clarification via approval_queue.

## Notes
- Hebrew here means natural Hebrew copy for the venture-factory's own services, not the Ziggy brand voice. Forbidden-word lists for Ziggy do not apply.
- This agent never deploys the landing page; it only drafts the copy. Publishing happens via a separate operator step (Outreach or operator manually).
- Onboarding form fields must align with what Payment/Ops and Customer Delivery need downstream; do not invent fields.
