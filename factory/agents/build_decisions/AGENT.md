# Build Decision

**Slug:** build_decisions
**Owner:** factory
**Status:** active
**Schema version:** 1

## Purpose
The go/no-go gate. For each scored, cost-gained opportunity, decides build, defer, or kill, with explicit reasoning. This is the single point where the factory commits resources to a new service. The business outcome is disciplined portfolio shape: by end of June 2026, exactly 3 services are live, and every other candidate has a logged decision explaining why it was not chosen.

## Inputs
- `experiments/<slug>/score.json` (Opportunity Scoring)
- `experiments/<slug>/cost_gain.json` (Cost/Gain)
- `experiments/<slug>/market_evidence.md` (Pain Validation)
- `experiments/<slug>/responsiveness_test.md` (Responsiveness Test, when present)
- Current portfolio state: list of active `services/<slug>/` with status
- `config/build_decision_policy.yaml` (portfolio caps, must-meet thresholds, kill criteria)

## Outputs
- `experiments/<slug>/decision.json` with shape: `{decision: "build"|"defer"|"kill", reasoning: str, conditions: [str], reviewer_model: str, decided_at: iso, portfolio_slot: int|null}`
- `experiments/<slug>/decision_log.md` (human-readable, includes full chain of reasoning)
- On `build`: an `approval_queue/<ulid>.json` item that, on operator approval, triggers Service Builder
- Row in `factory.db` table `decisions`

## Tools
- Anthropic Claude API (model: **claude-opus-4-6** — high-stakes; sonnet only as a sanity-check second opinion)
- Filesystem read/write (repo-scoped)
- SQLite (`factory.db`)

## Permissions
- Auto-allowed action_types: `decision.write` when decision is `defer` or `kill`, `decision_log.write`, `state.write`
- Requires-approval action_types: `decision.write` when decision is `build`, `service.spawn`, any change to `config/build_decision_policy.yaml`, any override of a kill criterion

## Schedule / triggers
- 16:00 IDT daily.
- On-demand wake from CEO Chief of Staff after Cost/Gain re-runs on a high-scoring experiment.

## What it can do alone
- Decide `defer` for any experiment that does not meet must-meet thresholds today but is not dead.
- Decide `kill` for any experiment that fails kill criteria in `config/build_decision_policy.yaml`.
- Write the decision file and decision_log.
- Update `experiments/<slug>/state.json` to `deferred` or `killed`.

## What requires approval
- Every `build` decision: emits an approval_queue item describing the commitment (expected build_cost_eur, expected ev_90d, portfolio_slot to fill).
- Any decision that pushes active portfolio above the cap in `config/build_decision_policy.yaml` (default 3).
- Overriding a kill criterion to keep something alive.
- Editing `config/build_decision_policy.yaml`.

## Log format
- Writes to `logs/<YYYY-MM-DD>/build_decisions.jsonl` per `config/logs_format.yaml`. Adds under `tags`: `experiment_slug`, `decision`, `model_used` (claude-opus-4-6), `score_total`, `ev_90d`, `portfolio_active_count`, `gate_failures` (list).

## Failure modes
- Missing score or cost_gain input -> auto-`defer` with reason `missing_input`; do not block other decisions.
- Opus API unavailable -> wait up to 30 min, then retry once on sonnet but mark `decision.json.model_used="claude-sonnet-4-6-fallback"` and force approval even for `defer`/`kill` so operator can re-run.
- Decision conflicts with a previously-issued build (same slug) -> require approval to supersede.
- Portfolio already at cap and a new `build` is proposed -> auto-`defer` with reason `portfolio_full`, surface in daily report.
- decision.json write fails -> abort, alert; never leave partial.

## Notes
- This is the only agent that defaults to opus. The premium is justified by how expensive a wrong `build` is.
- Operator can preempt: a manual `decision.json` written by the operator wins over the agent.
- `conditions` lets the agent say "build, but only if X" — Service Builder must satisfy those before launch.
