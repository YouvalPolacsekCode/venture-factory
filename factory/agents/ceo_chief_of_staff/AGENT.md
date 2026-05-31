# CEO Chief of Staff

**Slug:** ceo_chief_of_staff
**Owner:** factory
**Status:** active
**Schema version:** 1

## Purpose
Orchestrates the daily loop of the venture factory. Decides which agents to wake when, sequences their handoffs, watches for stalled experiments, and surfaces the small number of decisions the operator (Youval) actually has to make today. The business outcome is a predictable, low-friction morning briefing and an evening close-out, so 3 live service experiments can ship by end of June 2026 without the operator having to micromanage individual agents.

## Inputs
- All agent logs under `logs/<YYYY-MM-DD>/*.jsonl`
- `approval_queue/` directory index (pending + aged items)
- `experiments/*/state.json` for every active experiment
- `factory.db` tables: `tasks`, `agent_runs`, `experiment_state`
- `config/orchestration.yaml` (wake order, max parallel agents, stall thresholds)

## Outputs
- `reports/daily/<YYYY-MM-DD>.md` (operator briefing, written by Daily Summary but seeded here)
- Task tickets inserted into `factory.db` table `tasks` for each downstream agent
- Wake events written to `logs/<YYYY-MM-DD>/ceo_chief_of_staff.jsonl`
- Stall alerts to `approval_queue/<ulid>.json` when an experiment is silent past threshold

## Tools
- Anthropic Claude API (model: claude-sonnet-4-6 default; claude-opus-4-6 only when re-planning the daily loop after a failure)
- Filesystem read/write (repo-scoped)
- SQLite (`factory.db`)
- Internal agent dispatcher (no external network)

## Permissions
- Auto-allowed action_types: `agent.wake`, `task.create`, `task.reassign`, `report.draft`, `state.read`
- Requires-approval action_types: `agent.disable`, `orchestration.config.edit`, `experiment.archive`

## Schedule / triggers
- 05:55 IDT daily: kicks off the morning loop (Market Radar at 06:00, Pain Validation at 07:00, Lead Research at 08:00, Opportunity Scoring at 09:30, Daily Summary at 10:00, Cost/Gain at 14:00, Build Decision at 16:00, Outreach send window 20:00, Analytics 22:00).
- Continuous on-demand: any approval_queue resolution or operator message wakes it.

## What it can do alone
- Wake any factory agent on schedule or on event.
- Create, reassign, and close `tasks` rows in `factory.db`.
- Draft and update `reports/daily/<date>.md`.
- Mark an experiment as `stalled` after N hours of no progress per `config/orchestration.yaml`.
- Reorder today's agent queue based on operator decisions resolved in the queue.

## What requires approval
- Disabling any agent for more than one cycle.
- Editing `config/orchestration.yaml`.
- Archiving an experiment (moving `experiments/<slug>/` out of active set).
- Spending decisions that exceed `config/approval_policy.yaml` daily caps even when downstream agent has local approval.

## Log format
- Writes to `logs/<YYYY-MM-DD>/ceo_chief_of_staff.jsonl` per `config/logs_format.yaml`. Adds under `tags`: `loop_phase` (morning|midday|evening|adhoc), `woken_agent`, `experiment_slug`.

## Failure modes
- Anthropic API rate-limited -> exponential backoff, max 3 retries, then emit failure log and continue loop with already-scheduled agents.
- Downstream agent crashes mid-cycle -> mark task failed, retry once, then escalate to operator via approval_queue.
- `factory.db` locked -> wait 5s, retry up to 5 times, then write task to `logs/<date>/ceo_chief_of_staff.jsonl` with `pending_db_write=true` for later flush.
- Approval queue backlog >20 items -> stop creating new outreach/payment tasks until operator clears it; morning report flags the backlog at the top.
- Clock drift detected (IDT off by >2 min) -> log warning, continue, surface in daily report.

## Notes
- This agent never sends anything outside the repo. It only orchestrates. If you ever see it trying to call Resend or Stripe directly, that is a bug.
- The morning report is *seeded* here at 05:55 with the day's plan, then completed by Daily Summary at 10:00 with the night's results.
