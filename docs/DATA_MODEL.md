# Canonical Data Model (P4.0)

This document is **authoritative**. Where `ARCHITECTURE.md`, `prompts/*.md`, or
`factory/agents/*/AGENT.md` disagree with it, this wins. It was written to
reconcile three drifting conventions found in the repo (implemented code,
prompt contracts, and aspirational AGENT.md files).

## 1. One opportunity → one service

A venture moves through **two** on-disk homes — there is **no `experiments/`
tree** (rejected; see §6):

### Discovery → decision: `opportunities/<id>.*.json`

`<id>` is a ULID. Sibling files accrete as an opportunity advances; each agent
reads the siblings present and writes its own:

| File | Written by | Key fields |
|---|---|---|
| `<id>.opportunity.json` | market_radar | `id`, `discovered_at`, `source{type,url,snippet}`, `problem_statement`, `target_segment`, `geo`, `signal_strength`, `keywords`, `status` |
| `<id>.scoring.json` | opportunity_scoring | `per_dimension{...}`, `total`, `recommended_stage` (drop/validate/build/scale), `penalties_applied`, `rationale`, `solution_plan`, `scored_at`, `model_version` |
| `<id>.verdict.json` | pain_validation | `status` (validated/rejected), `severity`, `frequency`, `rationale`, `sources` |
| `<id>.market_evidence.md` | pain_validation | evidence narrative |
| `<id>.cost_gain.json` | **cost_gain (P4.1)** | see §3 |
| `<id>.build_decision.json` | **build_decisions (P4.2)** | see §4 |

> **Naming fix:** older code/`should_run` referred to `<id>.decision.json`.
> Canonical is **`<id>.build_decision.json`** (matches `prompts/build_decision.md`).

### Built service: `services/<slug>/`

Created by **service_builder (P4.3)** only after an operator-approved
`build_now`. It is a copy of the 17-file `templates/service_template/` scaffold
plus runtime artifacts. **All in-flight test + build artifacts live here**, not
in a separate tree:

```
services/<slug>/
  service.yaml, offer.md, pricing.md, landing_page_copy.md, onboarding_form.md,
  lead_sources.md, responsiveness_test.md, delivery_workflow.md,
  claude_delivery_prompts.md, metrics.md, status.md, support_policy.md,
  qa_checklist.md, launch_checklist.md, market_evidence.md, payment_path.md,
  report_template.md            # the 17-file template
  _scaffold.json                # service_builder provenance (slug, opp id, approval ulid, ts)
  build_provenance.json         # which inputs filled which sections
  .lead_research.json           # lead_research structured output
  .responsiveness_test.json     # responsiveness_test structured output (DRAFT)
  outreach_drafts/<batch_id>/   # outreach agent drafts (pre-approval)
  outreach_sent/<batch_id>/manifest.json   # post-approved-send record (hashed emails)
  site/index.html               # built landing page (P4.7)
  claude_delivery_prompts/      # delivery engine prompt chain (P4.7)
```

`services/<slug>/status.md` carries the live stage (`validating | building |
launched | scaling | killed | paused`) and the live URL once published.

### Customers & payments (P5)

```
payments/<customer_hash>/...     # payment_ops artifacts (Stripe link/invoice refs; NO raw cards)
customers/<customer_hash>/deliveries/<date>/draft/   # customer_delivery + qa
```

`<customer_hash>` = `sha256(email)[:12]`. **No raw PII** is ever written to disk
or logs — emails/handles are always hashed.

## 2. State, logs, approvals

- **Database: `factory/state.db`** (SQLite). Never `factory.db` (that name is a
  doc artifact only). Tables: `runs`, `signals`, `spend_ledger`, `experiments`,
  `source_rate_limit`, `smoke_baseline`, plus P4/P5 additions
  (`outreach_sends`). Migrations in `scripts/migrations/`.
- **Logs:** `logs/runs/<YYYY-MM-DD>/<agent>.jsonl` (IDT date). `execute_action`
  logs to `logs/runs/<date>/execute_action.jsonl`.
- **Approvals:** every outward / resource-committing action writes
  `approval_queue/<ulid>.json`; the operator runs `scripts/approve.py <ulid>`
  (→ `<ulid>.approved.json`) or `scripts/reject.py`. `scripts/execute_action.py`
  refuses to act without `<ulid>.approved.json`. `action_type` values come from
  **`config/approval_policy.yaml`** (see §5).

## 3. cost_gain output (`<id>.cost_gain.json`) — P4.1, deterministic

Computed in code from `config/cost_gain_model.yaml` + the opportunity's scoring
(no LLM call; matches ARCHITECTURE "all math in code"). USD throughout.

```
opportunity_id, computed_at, model_version,
build_cost_usd, monthly_run_cost_usd,
expected_arpu_usd, expected_conversion_rate, break_even_customers,
cost_to_first_paid_usd, expected_gain_30d_usd, expected_gain_90d_usd,
cost_to_gain_ratio,                 # projected_4w_cost / projected_4w_gain
sensitivity{pessimistic,base,optimistic},  # ratio under conversion bands
assumptions[]                       # human-readable list of every figure used
```

## 4. build_decision output (`<id>.build_decision.json`) — P4.2

Decision ∈ `{build_now, defer_1_week, kill}`. **`build_now` is only legal when
the scoring-v2 bar is cleared** (enforced in code, not trusted to the LLM):

> `build_now` requires: scoring `recommended_stage` ∈ {build, scale} **AND**
> `total ≥ min_total_to_build` (6.5) **AND** every `build_gates.required_gates`
> dimension ≥ its `_min` floor. Otherwise the max decision is `defer_1_week`
> (or `kill`). Plus portfolio cap (≤3 active builds) and daily cap (≤5
> decisions/day). On `build_now`, an `approval_queue/<ulid>.json` with
> `action_type: promote_to_build` is written; **service_builder runs only after
> the operator approves it.**

Fields: `opportunity_id`, `decided_at`, `decision`, `confidence_pct` (≤95),
`model_used`, `gates_checked{...}`, `reasoning_summary`, `why_now_memo`
(iff build_now, ≤120 words), `proposed_slug`, `estimated_first_signal_days`,
`suggested_first_outreach_channel`.

## 5. Config files (only what code consumes)

| Config | Consumed by | Added in |
|---|---|---|
| `config/scoring_model.yaml` | opportunity_scoring, **build_decisions** (build_gates + thresholds) | existing; P4.0 adds `build_gates.required_gates` |
| `config/cost_gain_model.yaml` | **cost_gain**, build_decisions | existing |
| `config/approval_policy.yaml` | runner, execute_action; P4.0+ adds action_types `promote_to_build`, `design_review`, `implementation_review` | existing |
| `config/agent_models.yaml` | runner (model/tokens/batch) | existing |
| `config/product_design.yaml` | product_design (price guardrails) | **P4.4** |
| `config/hosting.yaml` | publish adapter (cloudflare\|github_pages) | **P4.7** |

No `build_decision_policy.yaml`, `service_naming.yaml`, `outreach_policy.yaml`,
`responsiveness_thresholds.yaml`, `delivery_policy.yaml`, `payment_policy.yaml`,
`qa_policy.yaml`, `analytics_metrics.yaml` — those AGENT.md references are
**dropped**; their settings are folded into the configs above or into code
defaults documented here. New config is created only in the phase that reads it.

## 6. Decisions / rationale

- **`services/<slug>/` over `experiments/<slug>/`:** one folder per venture from
  scaffold onward avoids a parallel tree and a rename at promotion. The 17-file
  template already contains `responsiveness_test.md`, `market_evidence.md`,
  `metrics.md`, so in-flight test artifacts have a natural home. Pre-scaffold,
  everything is the `opportunities/<id>.*` sibling set.
- **`build_now`/`defer_1_week`/`kill`** (not `build`/`defer`) — matches the more
  specific `prompts/build_decision.md` contract.
- **USD** everywhere (cost_gain_model is USD); AGENT.md "EUR" is dropped.
- **24/7** — no Shabbat / read-only / time-of-week gating anywhere (removed
  earlier; `test_runs_24_7_no_shabbat_window` guards it). AGENT.md / prompt
  "Shabbat rule" lines are obsolete and ignored.
