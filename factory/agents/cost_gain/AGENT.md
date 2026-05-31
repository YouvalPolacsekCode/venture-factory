# Cost/Gain

**Slug:** cost_gain
**Owner:** factory
**Status:** active
**Schema version:** 1

## Purpose
Estimates how much it will cost to stand up and run each opportunity vs the expected gain, using the canonical model in `config/cost_gain_model.yaml`. Produces a single `cost_gain.json` per experiment that Build Decision consumes. The business outcome is rational capital allocation: the operator does not green-light an experiment whose expected gain is below a clear break-even at realistic conversion rates.

## Inputs
- Scored opportunities: `experiments/_candidates/<ulid>.score.json` and `experiments/<slug>/score.json`
- `experiments/<slug>/market_evidence.md` (for unit economics inputs: competitor pricing, willingness-to-pay anchors)
- `experiments/<slug>/responsiveness_test.md` (when available)
- `config/cost_gain_model.yaml` (cost categories, gain assumptions, ranges)
- Current portfolio: list of active `services/<slug>/` and their measured unit costs

## Outputs
- `experiments/<slug>/cost_gain.json` (build_cost_eur, monthly_run_cost_eur, expected_arpu_eur, expected_conversion_rate, break_even_customers, ev_eur_90d, ev_eur_12m, sensitivity_band)
- `experiments/_candidates/<ulid>.cost_gain.json` for pre-promotion candidates (lighter version, ranges only)
- Rows in `factory.db` table `cost_gain_runs`
- Update to `experiments/<slug>/state.json` with `cost_gain: complete|partial`

## Tools
- Anthropic Claude API (model: claude-sonnet-4-6 for extracting price anchors and competitor-cost reasoning from evidence)
- Filesystem read/write (repo-scoped)
- SQLite (`factory.db`)
- web_fetch (limited, only to refresh public competitor pricing pages when stale)

## Permissions
- Auto-allowed action_types: `cost_gain.compute`, `cost_gain.write`, `state.write`, `web.fetch.read` (pricing pages only)
- Requires-approval action_types: `cost_gain_model.config.edit`, `cost_gain.override`, any paid data lookup

## Schedule / triggers
- 14:00 IDT daily.
- On-demand wake from CEO Chief of Staff when a new experiment is promoted by Pain Validation or when Responsiveness Test publishes new data (conversion rates change the EV).

## What it can do alone
- Compute build_cost_eur from category sums (Claude tokens, hosting, third-party APIs, design assets, operator hours at the rate in the model).
- Compute monthly_run_cost_eur from steady-state assumptions.
- Compute expected_arpu_eur and expected_conversion_rate using anchors from market_evidence and (if present) measured responsiveness.
- Produce sensitivity bands (pessimistic, base, optimistic).
- Update state.json and write the per-experiment cost_gain.json.

## What requires approval
- Editing `config/cost_gain_model.yaml`.
- Manual override of any cost or gain figure.
- Spending on paid data sources to refine estimates.
- Triggering re-evaluation that would invalidate an already-issued Build Decision.

## Log format
- Writes to `logs/<YYYY-MM-DD>/cost_gain.jsonl` per `config/logs_format.yaml`. Adds under `tags`: `experiment_slug_or_ulid`, `build_cost_eur`, `monthly_run_cost_eur`, `ev_90d`, `ev_12m`, `confidence` (low|med|high).

## Failure modes
- Missing score input -> request Opportunity Scoring run via CEO Chief of Staff, mark `partial`.
- Competitor pricing page unreachable -> use last cached value, log `stale_pricing=true`.
- Model produces negative EV across all sensitivity bands -> still write the file; this is signal, not failure.
- Model config invalid -> abort, alert via approval_queue, do not overwrite prior outputs.
- Claude extraction disagrees with cached anchor by >50% -> log a `pricing_anchor_conflict` event for operator review.

## Notes
- All figures are in EUR. Convert ILS via the rate in `config/cost_gain_model.yaml`; do not call live FX APIs.
- Operator-hour cost is fixed in the model; this agent does not estimate operator hours, only multiplies.
- `ev_90d` is the headline number Build Decision uses; `ev_12m` is informational only at this stage.
