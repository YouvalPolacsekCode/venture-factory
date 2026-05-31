# Opportunity Scoring

**Slug:** opportunity_scoring
**Owner:** factory
**Status:** active
**Schema version:** 1

## Purpose
Applies the canonical scoring model in `config/scoring_model.yaml` to every candidate opportunity and to every active experiment, producing a single comparable score. This is what makes the daily ranking deterministic and auditable instead of a vibe. The business outcome is a defensible top-5 list each morning: the operator sees the same numbers the agents see, with the inputs traceable.

## Inputs
- All `experiments/_candidates/<ulid>.opportunity.json`
- All active `experiments/<slug>/state.json` and `experiments/<slug>/market_evidence.md`
- `config/scoring_model.yaml` (weights, normalization, must-pass gates)
- `factory.db` table `historical_scores` (for drift detection)

## Outputs
- `experiments/_candidates/<ulid>.score.json` per candidate
- `experiments/<slug>/score.json` per active experiment (replaced each run, prior versions kept in `experiments/<slug>/.score_history/`)
- Ranked list embedded in `reports/daily/<YYYY-MM-DD>.md`
- Rows in `factory.db` table `scores`

## Tools
- Anthropic Claude API (model: claude-sonnet-4-6 only for natural-language inputs that need numeric extraction; pure math is in code)
- Filesystem read/write (repo-scoped)
- SQLite (`factory.db`)

## Permissions
- Auto-allowed action_types: `score.compute`, `score.write`, `rank.publish`
- Requires-approval action_types: `scoring_model.config.edit`, `score.override` (manual operator-set scores), `historical_scores.purge`

## Schedule / triggers
- 09:30 IDT daily (after Market Radar 06:00, Pain Validation 07:00, Lead Research 08:00).
- On-demand wake whenever `config/scoring_model.yaml` is edited (re-score everything).
- On-demand wake when Cost/Gain finishes (some weights depend on cost_gain output).

## What it can do alone
- Read every candidate and active experiment.
- Compute each dimension (pain_severity, market_size, accessibility, ICP_clarity, willingness_to_pay, build_cost_proxy) per the model.
- Apply must-pass gates and drop disqualified items.
- Write `.score.json` files and the ranked list.
- Detect score drift vs `historical_scores` and flag in logs when >25% on the same item.

## What requires approval
- Editing `config/scoring_model.yaml`.
- Manual override of any score.
- Purging or rewriting `historical_scores`.
- Disabling the must-pass gates for any single experiment.

## Log format
- Writes to `logs/<YYYY-MM-DD>/opportunity_scoring.jsonl` per `config/logs_format.yaml`. Adds under `tags`: `target_ulid_or_slug`, `score_total`, `dimension_scores` (compact dict), `gates_passed`, `drift_pct_vs_last`.

## Notes the operator should know — see Failure modes below.

## Failure modes
- `config/scoring_model.yaml` invalid -> abort run, do NOT overwrite existing scores, emit failure log, alert via approval_queue.
- Missing input dimensions on a candidate -> use defaults from the model with `imputed=true` flag in `.score.json`; never silently zero.
- Claude extraction returns low confidence -> retain prior numeric value if one exists; otherwise mark dimension `unknown` and let gates handle it.
- Score drift > 25% -> log explicitly so Daily Summary can call it out.
- SQLite write fails -> retry 3x then write a sidecar `.pending.jsonl` for next run to flush.

## Notes
- All math is in code; Claude is used only to turn prose evidence into numbers. This keeps the model auditable.
- Score history (`.score_history/`) is the audit trail; do not delete.
- Weights are intentionally biased toward `willingness_to_pay` until we have 3 live services to calibrate against.
