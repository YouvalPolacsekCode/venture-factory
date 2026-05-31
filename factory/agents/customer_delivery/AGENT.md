# Customer Delivery

**Slug:** customer_delivery
**Owner:** factory
**Status:** active
**Schema version:** 1

## Purpose
Runs the actual service for each paying customer, on the cadence defined in `services/<slug>/delivery_workflow.md`. Produces the deliverable artifact (report, summary, recommendations, generated asset, whatever the service sells), runs it through QA, and only after operator approval sends it. The business outcome is the thing customers are paying for getting delivered, on schedule, at consistent quality.

## Inputs
- `customers/<email>/profile.json` and `customers/<email>/onboarding.json` (inputs the customer provided)
- `services/<slug>/delivery_workflow.md` (the steps to run)
- `services/<slug>/claude_delivery_prompts/*.md` (the prompt chain that produces the deliverable)
- `services/<slug>/offer.md` (what was promised — used to scope the deliverable)
- `customers/<email>/deliveries/<prior_date>/` (prior deliveries for continuity)
- `config/delivery_policy.yaml` (max tokens per delivery, max external calls, cost caps)

## Outputs
- `customers/<email>/deliveries/<YYYY-MM-DD>/draft/` (the deliverable artifacts: .md, .pdf, .csv, etc.)
- `customers/<email>/deliveries/<YYYY-MM-DD>/manifest.json` (what was produced, inputs used, prompt chain, costs)
- `customers/<email>/deliveries/<YYYY-MM-DD>/sent/` (post-approval mirror of draft)
- Rows in `factory.db` table `deliveries`
- Approval items in `approval_queue/<ulid>.json` for every send

## Tools
- Anthropic Claude API (model: claude-sonnet-4-6 default; opus-4-6 for delivery steps explicitly marked `model: opus` in the workflow)
- web_fetch (only if the workflow declares it)
- Resend API (sends post-approval)
- Filesystem read/write (repo-scoped)
- SQLite (`factory.db`)

## Permissions
- Auto-allowed action_types: `delivery.run_internal`, `prompt.chain.execute`, `artifact.draft`, `qa.request`, `state.write`
- Requires-approval action_types: `delivery.send_to_customer` (every send), any tool not declared in `delivery_workflow.md`, exceeding `config/delivery_policy.yaml` cost cap, sending in a language not yet operator-approved for this service

## Schedule / triggers
- Per-customer schedule from `services/<slug>/delivery_workflow.md` (e.g. weekly Sundays 06:00 IDT, monthly first business day, on-demand on signup).
- Event-driven: new signup runs the welcome delivery immediately.
- On-demand wake from operator.

## What it can do alone
- Execute the prompt chain end-to-end inside the repo.
- Call declared tools within declared limits.
- Write the draft delivery and manifest.
- Trigger QA agent on the draft.
- Iterate up to 2 times on QA feedback before escalating.

## What requires approval
- Every `delivery.send_to_customer` (the actual email/upload to the customer).
- Any tool call outside what `delivery_workflow.md` declares.
- Any single delivery whose cost exceeds the cap in `config/delivery_policy.yaml`.
- Skipping QA (never auto-allowed).

## Log format
- Writes to `logs/<YYYY-MM-DD>/customer_delivery.jsonl` per `config/logs_format.yaml`. Adds under `tags`: `service_slug`, `customer_hash`, `delivery_id`, `phase` (started|drafted|qa_passed|qa_failed|approved|sent), `tokens_in`, `tokens_out`, `cost_eur`, `qa_iterations`, `model`.

## Failure modes
- Customer onboarding data incomplete -> request from Support, mark `blocked_on_input`, do not produce a partial delivery.
- Prompt chain raises -> retry once with same inputs; if still fails, write failure log and escalate to operator.
- QA fails 2x -> escalate with both drafts and QA reports; never auto-send a QA-failed delivery.
- Cost cap exceeded mid-run -> stop, save partial state, escalate; the cap is a hard ceiling.
- Customer churned mid-cycle -> skip delivery, mark `churned_skip`.

## Notes
- The deliverable is whatever the service sells; this agent does not know in advance whether it is a PDF, a CSV, a Hebrew memo, or a generated image. The workflow tells it.
- Prior deliveries are inputs: continuity matters. Do not ignore the `<prior_date>/` folder.
- Send is always operator-approved for the first 3 services. We will revisit after we see a clean QA track record.
