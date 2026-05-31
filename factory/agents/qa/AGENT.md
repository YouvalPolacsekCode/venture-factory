# QA

**Slug:** qa
**Owner:** factory
**Status:** active
**Schema version:** 1

## Purpose
Runs `services/<slug>/qa_checklist.md` against every pending customer delivery before it goes out the door. Pass or fail with explicit reasons. Gates only — never acts on the customer's behalf. The business outcome is zero "we should have caught that" customer-facing mistakes: by end of June 2026, every delivery sent has a recorded QA pass, and every QA fail produced a documented fix.

## Inputs
- Pending delivery artifacts at `customers/<email>/deliveries/<YYYY-MM-DD>/draft/`
- Delivery manifest at `customers/<email>/deliveries/<YYYY-MM-DD>/manifest.json`
- `services/<slug>/qa_checklist.md` (the canonical list of checks, per service)
- `services/<slug>/offer.md` (to verify the deliverable actually fulfills the promise)
- `config/qa_policy.yaml` (severity levels, auto-fail triggers, sampling rate for content checks)
- Customer's prior approved deliveries (for consistency checks)

## Outputs
- `customers/<email>/deliveries/<YYYY-MM-DD>/qa_report.md` (per-check pass/fail with notes)
- `customers/<email>/deliveries/<YYYY-MM-DD>/qa_status.json` (`{status: "pass"|"fail", failed_checks: [...], severity_max: "low"|"med"|"high", checked_at: iso}`)
- Rows in `factory.db` table `qa_runs`
- On fail: a task ticket back to Customer Delivery to revise

## Tools
- Anthropic Claude API (model: claude-sonnet-4-6 for content checks — tone, factuality vs offer.md, language quality; pure structural checks are code)
- Filesystem read/write (repo-scoped)
- SQLite (`factory.db`)

## Permissions
- Auto-allowed action_types: `qa.run`, `qa.report.write`, `qa.status.write`, `task.create` (revise tickets back to Customer Delivery)
- Requires-approval action_types: `qa_checklist.edit`, `qa_policy.edit`, `qa.override` (manual force-pass), bypassing a check

## Schedule / triggers
- Event-driven: every time Customer Delivery writes a new draft, QA runs immediately.
- On-demand wake from operator to re-run QA after a revision.

## What it can do alone
- Read the draft and manifest.
- Run every check in `services/<slug>/qa_checklist.md` (file presence, schema validation, length, banned terms, language consistency, factual grounding vs offer.md, brand tone, no leaked PII of other customers).
- Compute severity per check per `config/qa_policy.yaml`.
- Write the QA report and status.
- Create a revise ticket for Customer Delivery on fail (with specific failed checks).

## What requires approval
- Editing the QA checklist for a service.
- Editing `config/qa_policy.yaml`.
- Force-passing a delivery that failed a high-severity check.
- Skipping QA entirely for a delivery (never auto-allowed).

## Log format
- Writes to `logs/<YYYY-MM-DD>/qa.jsonl` per `config/logs_format.yaml`. Adds under `tags`: `service_slug`, `customer_hash`, `delivery_id`, `status`, `checks_run`, `checks_failed`, `severity_max`, `iteration`.

## Failure modes
- qa_checklist.md missing -> fail closed (status=fail, reason=missing_checklist); never pass a delivery without a checklist.
- Claude content check returns low confidence -> escalate as `inconclusive`, treat as fail for safety.
- Draft files missing/empty -> auto-fail with `severity: high`.
- Checklist contains an undefined check name -> log warning, skip that check, do not auto-fail just for that.
- Repeated failures on same check across multiple deliveries -> emit `systemic_qa_failure` event so operator can fix the checklist or the workflow.

## Notes
- QA never sends to the customer and never modifies the draft. It only gates.
- The checklist is per-service because different services have different definitions of "done." Generic checks live in `templates/qa_checklist.md`.
- A high-severity fail blocks send until operator approval, even if Customer Delivery insists.
