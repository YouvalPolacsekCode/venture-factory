# Delivery Workflow

<!-- The repeatable, agent-runnable steps that produce one customer deliverable. The Delivery agent reads this file. -->

## Steps

<!-- Numbered, atomic. Each step has one owner agent and a hard time estimate. If a step takes more than 30 minutes, split it. -->

| # | Step | Owner agent | Est. time | Output |
|---|---|---|---|---|
| 1 | Validate intake (all required fields present, payment confirmed) | Payment agent | 5 min | `intake/<customer>/validated.json` |
| 2 | Pull customer-supplied inputs into working folder | Delivery agent | 5 min | `work/<customer>/inputs/` |
| 3 | Run analysis / generation prompts (see `claude_delivery_prompts.md`) | Delivery agent | <!-- e.g., 20 min --> | `work/<customer>/draft.md` |
| 4 | Self-check against quality bars | Delivery agent | 5 min | `work/<customer>/self_check.md` |
| 5 | QA review (see `qa_checklist.md`) | QA agent | 10 min | `work/<customer>/qa.md` |
| 6 | Render to final format (PDF / Notion / Loom) | Delivery agent | 10 min | `work/<customer>/final/` |
| 7 | Send to customer + log delivery | Delivery agent | 5 min | `work/<customer>/sent.json` |
| 8 | Trigger follow-up sequence | Outreach agent | n/a (scheduled) | scheduled emails |

## Tools used

<!-- Be explicit. The Builder agent uses this to provision per-experiment access. -->

- Claude (model: <!-- e.g., claude-opus-4-7 -->) for generation
- <!-- e.g., Python + pandas for data prep -->
- <!-- e.g., Playwright for any web scraping during delivery -->
- <!-- e.g., Pandoc or weasyprint for PDF rendering -->

## Inputs from customer

<!-- Every field the onboarding form collects that's needed for delivery. Mirrors onboarding_form.md. -->

- <!-- field name --> — <!-- how it's used in the workflow -->

## Outputs to customer

<!-- The artifacts the customer actually receives. Must match offer.md "What's included". -->

- <!-- e.g., 1x PDF report (~6 pages), filename pattern `<slug>_<customer>_<YYYY-MM-DD>.pdf` -->
- <!-- e.g., 1x Loom walkthrough, 5-7 minutes -->

## SLA

<!-- Turnaround time from payment to delivery. Must match offer.md "Delivery promise". -->

- Standard SLA: <!-- e.g., 48 hours from payment confirmation, business days IDT -->
- Rush option (if offered): <!-- e.g., 12 hours, +50% price, see pricing.md -->

## Re-do policy

<!-- When a customer asks for a revision. -->

- Free re-do conditions: <!-- e.g., factual error, missing requested scope item -->
- Paid revision: <!-- e.g., new direction or expanded scope -> quote new fee -->
- Maximum re-do rounds: <!-- e.g., 2 free re-dos within 14 days of delivery -->

## Reference

See `claude_delivery_prompts.md` for the system prompt, step prompts, and guardrails the Delivery agent runs inside this workflow.
