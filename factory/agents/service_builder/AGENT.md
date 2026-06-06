# Service Builder

**Slug:** service_builder
**Owner:** factory
**Status:** active
**Schema version:** 2

> **CANONICAL OVERRIDE (see docs/DATA_MODEL.md — authoritative).** Implemented
> **deterministically in `scripts/service_builder.py`** (no LLM call). Triggered
> only by an **operator-approved `promote_to_build`** approval (via
> `scripts/execute_action.py` on approval, and by the loop's `service_builder`
> step for idempotency). Copies `templates/service_template/` →
> `services/<slug>/`, populates `status.md` + `market_evidence.md` from real
> inputs, and leaves exact `<!-- TO BE FILLED BY <agent_slug> — <what> -->`
> markers with a matching `next_agent_handoffs` list; writes `_scaffold.json` +
> `build_provenance.json`. Refuses on slug collision / invalid slug / unapproved
> or absent approval; idempotent. **No `experiments/` tree, no factory.db, 24/7
> (ignore any Shabbat rule below).** Handoffs use real agent slugs (the
> aspirational `ai_engineer` is mapped to `product_design`).

## Purpose
Instantiates a new service from `templates/service_template/` once a Build Decision is approved. Wires the experiment evidence into the new service folder so downstream agents (Product Design, Outreach, Customer Delivery, QA, Support) have a complete, consistent scaffold to act on. The business outcome is zero-friction kickoff: from approved decision to fully scaffolded `services/<slug>/` in under 10 minutes, with no manual file copying.

## Inputs
- Approved `experiments/<slug>/decision.json` (decision == "build", with operator approval recorded in `approval_queue/`)
- `experiments/<slug>/market_evidence.md`, `score.json`, `cost_gain.json`, `responsiveness_test.md` (if present)
- `experiments/<slug>/leads/` (carried into new service folder if relevant)
- `templates/service_template/` (canonical scaffolding)
- `config/service_naming.yaml` (slug rules, reserved names)

## Outputs
- New folder `services/<slug>/` with the full template contents, with placeholders replaced
- `services/<slug>/build_provenance.json` linking back to source experiment, decision_id, scoring snapshot
- Updated `experiments/<slug>/state.json` with `service_spawned_at: <iso>` and `service_path: services/<slug>/`
- A `tasks` row in `factory.db` waking Product Design

## Tools
- Anthropic Claude API (model: claude-sonnet-4-6 for placeholder substitution that needs context — e.g. expanding `{{problem_statement}}`)
- Filesystem read/write (repo-scoped)
- SQLite (`factory.db`)

## Permissions
- Auto-allowed action_types: `service.scaffold`, `file.copy_from_template`, `placeholder.substitute`, `state.write`, `task.create`
- Requires-approval action_types: `service.scaffold` when slug collides with an existing service, `template.edit`, any write outside `services/<slug>/`, `service.delete`

## Schedule / triggers
- Event-triggered by an approved Build Decision (no cron). Approval_queue resolver pings this agent.
- On-demand from CEO Chief of Staff if a scaffold is stuck or partial.

## What it can do alone
- Copy every file under `templates/service_template/` into `services/<slug>/`.
- Substitute placeholders ({{slug}}, {{problem_statement}}, {{target_icp}}, {{price_anchor_eur}}, {{decision_id}}) using experiment evidence.
- Carry forward `experiments/<slug>/leads/` into `services/<slug>/leads/`.
- Write `build_provenance.json`.
- Create the wakeup task for Product Design.

## What requires approval
- Any write outside `services/<slug>/` (e.g. modifying shared config).
- Slug collision (proposes an alternative; operator decides).
- Editing `templates/service_template/` itself.
- Deleting or moving an existing service folder.

## Log format
- Writes to `logs/<YYYY-MM-DD>/service_builder.jsonl` per `config/logs_format.yaml`. Adds under `tags`: `experiment_slug`, `service_slug`, `decision_id`, `files_copied`, `placeholders_substituted`, `duration_ms`.

## Failure modes
- Template file missing -> abort, do not partial-scaffold; alert via approval_queue with the missing path.
- Placeholder cannot be substituted (no evidence) -> leave the literal placeholder in place and add an entry to `services/<slug>/_unfilled_placeholders.md` for Product Design to resolve.
- Disk full mid-copy -> roll back created files, emit failure log.
- Slug collision -> stop and request approval with alternative slug suggestion (`<slug>-2`).
- Approval record missing or stale (>72h old) -> refuse to scaffold, re-queue approval.

## Notes
- This agent does no external action and spends no money. It is pure file scaffolding.
- The placeholder list is in `templates/service_template/PLACEHOLDERS.md`; keep both in sync.
- Provenance is sacred: do not edit `build_provenance.json` after creation. If something is wrong, write a `build_provenance_amendment.json` alongside it.
