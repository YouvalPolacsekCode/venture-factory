# Handover to Claude Code on Mac

Single-doc context transfer for resuming the venture-factory build from a Mac.

---

## You (Claude Code on the Mac) — read this first

You are picking up a project mid-stream. The operator (Youval, Tel Aviv, IDT/UTC+3) started the venture-factory build inside Cowork on Windows + Claude Code on Windows. They are now moving the same repo to a Mac and want to continue from there. The repo is the source of truth. `docs/ARCHITECTURE.md` is the spec — read it before touching anything.

**Mission.** This repo is an AI Venture Factory: a closed loop of 18 specialized agents that discover, validate, build, and operate real micro-service businesses with a single human operator in the loop. End-of-June 2026 goal: 3 live service experiments produced *by the factory*, not pre-picked by the operator or by you.

**Hard constraints (don't violate, ever).**

- Do NOT choose the 3 final service businesses. The factory selects them after running.
- Any service named anywhere in this repo is EXAMPLE ONLY.
- Auto-allowed actions per `config/approval_policy.yaml` can be done freely; anything that touches the outside world (publishing, outreach, money, deploys, customer messages) goes through `approval_queue/` and must wait for the operator.
- Default response length: short. Long-form only when explicitly asked.
- When in doubt, ask 1–3 clarifying questions before doing destructive or high-cost work.

---

## State at handover

Phase 0 (scaffold) and Phase 1 core wiring (P1) are complete and committed via Claude Code on Windows. Pending work that runs on the Mac: **P1.5 (cost optimization), P2 (scheduler + operator inbox), P3 (safety hardening)**.

What's in the repo right now (commit topology, Windows side):

1. Initial Phase 0 commit — full scaffold (folders, configs, 18 AGENT.md, 17 service template files, 3 JSON schemas, 8 prompts, README, RUNBOOK, ARCHITECTURE).
2. Drift-reconciliation commit — three fixes:
   - `config/logs_format.yaml` path_template → `logs/runs/<YYYY-MM-DD>/<agent>.jsonl`
   - `docs/ARCHITECTURE.md` §7 Opportunity snippet updated to match the on-disk schema (`id`, `discovered_at`, `problem_statement`).
   - Global rename `experiments/_candidates/` → `opportunities/` across agents, prompts, and `config/market_radar_sources.yaml` (also fixed a YAML quoting bug on that file).
3. Phase 1 core wiring (P1) commit — live Anthropic API in `scripts/run_agent.py`, real HN/Reddit fetchers in `factory/sources/`, the scoring chain (`opportunity_scoring`, `pain_validation`), daily summary writer, updated `scripts/smoke_test.py`. `uv run smoke` was green on Windows.

What still needs doing, in order:

- **P1.5** — prompt caching + batching + source prefilter + model routing + skip-no-work. Cuts API cost ~70% with zero capability loss. Sequential — must commit before P3.
- **P2** — scheduler + operator inbox + morning brief. **Windows-specific as originally written; adapt to macOS launchd for the Mac.** Can run in parallel with P3 after P1.5.
- **P3** — safety hardening: per-day USD cap enforcement, fail-closed startup, Shabbat read-only window, pytest safety suite. Touches `scripts/run_agent.py`, so must come after P1.5.

---

## Transfer & first-time Mac setup

Before running any prompt below, confirm the repo arrived intact and the toolchain works on the Mac.

1. **Get the repo to the Mac.** Cleanest path: push from Windows, clone on Mac.
   - On Windows (PowerShell, in the repo): `git remote add origin <your-private-repo-url>` then `git push -u origin main`.
   - On Mac: `cd ~/Documents && git clone <your-private-repo-url> venture-factory && cd venture-factory`.
   - If you skipped GitHub: rsync/zip the folder over, but make sure the `.git/` directory transferred and that file permissions are sane (`chmod -R u+rw .` after copy).
2. **Recreate `.env`** (it was gitignored and didn't transfer):
   ```
   echo "ANTHROPIC_API_KEY=sk-ant-YOUR-KEY-HERE" > .env
   chmod 600 .env
   ```
3. **Install uv** (Python package + script runner):
   ```
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```
   Open a new terminal so PATH refreshes. Confirm with `uv --version`.
4. **Sync dependencies** from the committed `uv.lock`:
   ```
   uv sync
   ```
5. **Validate the transfer**: run the existing smoke test against the live API. This is the equivalence check — if it passes on the Mac, you have the same working environment as Windows.
   ```
   uv run smoke
   ```
   If smoke fails, do NOT proceed to P1.5/P2/P3 yet. Diagnose first: most likely culprits are missing env var, missing Python 3.11, or stale `factory/state.db` carrying Windows paths. Wipe `factory/state.db` and re-run smoke — migrations recreate it from `scripts/migrations/`.
6. **Git identity** (if it wasn't set on the Mac):
   ```
   git config user.email "silentyouval@gmail.com"
   git config user.name "Youval"
   ```

---

## How to run the pending prompts on Mac

The operator runs each prompt below in a separate Claude Code session at the repo root:

```
cd ~/Documents/venture-factory
claude
```

Then paste the prompt's `text` block. Sequence:

1. **P1.5** alone → wait for green smoke + commit.
2. After P1.5: open two Claude Code sessions. Paste **P2** in one, **P3** in the other. They touch disjoint files.

P2 was originally drafted for Windows Task Scheduler. On Mac, translate the scheduling step to **launchd** (a `~/Library/LaunchAgents/com.youval.venturefactory.daily.plist` file + `launchctl load`). The rest of P2 (operator inbox, morning brief, RUNBOOK section) ports directly — just rewrite the `.ps1` morning brief as a `.sh` or `.zsh` and use `open` instead of `start-process` to launch the editor.

---

## The five prompts, verbatim

Below are all five Claude Code prompts created during the Windows session, in execution order. P0 and P1 already ran on Windows and are committed to the repo — they are included here for reference / re-runnability. P1.5, P2, P3 are pending and will run on the Mac.

---

### P0 — Build the Python agent runner MVP (already executed on Windows)

This is the verbatim prompt from `docs/ARCHITECTURE.md` §13. It was the bootstrap that turned the scaffold into a working factory.

```text
You are Claude Code. Working directory: ~/Documents/venture-factory. The repo scaffold already exists (config/, factory/agents/, templates/, scripts/, approval_queue/, logs/, opportunities/, leads/, experiments/, services/, customers/, payments/, support/, reports/, dashboards/, security/, prompts/, docs/). Read docs/ARCHITECTURE.md before doing anything else and treat it as the spec.

Goal: build the Python agent runner MVP for the Venture Factory. Stay minimal. No frameworks. Boring code wins.

Tasks, in order:

1. Set up the Python project with uv (Python 3.11). Create pyproject.toml with dependencies: anthropic, jsonschema, pyyaml, python-ulid, httpx, python-dotenv. Generate uv.lock. Add .python-version pinned to 3.11.

2. Implement scripts/run_agent.py with this contract:
   - CLI: `run_agent.py --agent <slug> [--input <path>] [--dry-run]`.
   - Loads factory/agents/<slug>/AGENT.md as the system prompt.
   - Loads config/approval_policy.yaml and config/logs_format.yaml at startup.
   - Reads inputs declared in the AGENT.md frontmatter (a YAML block at the top between --- markers, with keys: inputs (list of globs), outputs (list of paths or path templates), schedule, permissions).
   - Calls the Anthropic Claude API (model: claude-opus-4-5 or the latest available; read ANTHROPIC_API_KEY from .env). Use the messages API. Stream optional.
   - Parses the model output. If the output contains an action block of the form ```action ... ``` (a YAML or JSON block describing an outside-world action), do not execute it. Instead write approval_queue/<ulid>.json conforming to the shape in section 6 of ARCHITECTURE.md. Print the ulid.
   - For any file write the model proposes inside the repo (and only the repo), perform the write directly. Reject writes outside the repo root.
   - Emit exactly one structured log line per run to logs/runs/<YYYY-MM-DD>/<agent>.jsonl following config/logs_format.yaml (run_id, agent, started_at, ended_at, status, tokens_in, tokens_out, cost_usd_estimate, outputs[], approval_requests[], errors[]).
   - Enforce per-day USD caps from approval_policy.yaml using a small counter persisted in factory/state.db (table: spend_ledger).

3. Implement scripts/run_daily_loop.py that invokes agents in the order from section 9 of ARCHITECTURE.md, skipping any agent whose preconditions are not met (log a SKIP). Respect Friday 18:00 IDT to Saturday 20:00 IDT read-only window (block agents whose permissions include external send).

4. Implement scripts/approve.py and scripts/reject.py:
   - approve.py <ulid>: validate the approval JSON, write approval_queue/<ulid>.approved.json with operator_ts, then invoke scripts/execute_action.py <ulid>.
   - reject.py <ulid> --reason "<text>": write approval_queue/<ulid>.rejected.json, append to logs/denied/<date>.jsonl.

5. Implement scripts/execute_action.py as a dispatcher keyed on action_type. For Phase 0, stub every action_type to write a `simulated_execution.json` next to the approved file and log it. Real adapters (Resend, Stripe, wrangler) come later — leave a TODO and a clear extension point.

6. Initialise factory/state.db with sqlite3 stdlib. Tables: runs, signals, spend_ledger, experiments. Migrations live in scripts/migrations/ as numbered .sql files. Apply on first run.

7. Add scripts/smoke_test.py:
   - Runs `run_agent.py --agent market_radar --dry-run` against a fixture source list (config/fixtures/market_radar_fixture.json).
   - Asserts at least one opportunities/<ulid>.json is written and validates against templates/opportunity.schema.json.
   - Asserts one log line exists.
   - Exits non-zero on any failure.

8. Wire `uv run smoke` via a pyproject.toml [tool.uv] scripts entry (or a Makefile target if simpler).

Constraints:
- No outside-world calls during Phase 0 unless behind the approval queue.
- All file paths inside the repo. Reject anything else.
- Reads ANTHROPIC_API_KEY from .env via python-dotenv. Never log the key.
- If config/approval_policy.yaml is missing or unparseable, fail closed: block every external action and exit 1.

Deliverable: a green `uv run smoke` and a one-paragraph CHANGES.md entry summarising what you built and any deviations from this prompt.
```

---

### P1 — Live API + real sources + scoring chain (already executed on Windows)

```text
You are Claude Code. Working directory: ~/Documents/venture-factory. Phase 0 is complete and committed. ARCHITECTURE.md is the spec — read it before touching anything.

Goal: take the factory live for Phase 1. The W23 (Jun 1–7) gate is ≥30 scored candidate opportunities. That requires real Anthropic API calls and real signal-source pulls, not dry-run fixtures.

Tasks, in order:

1. Ensure .env.example exists with `ANTHROPIC_API_KEY=` and a comment linking to https://console.anthropic.com/. Confirm .env is in .gitignore.

2. Add real source fetchers under factory/sources/:
   - factory/sources/__init__.py — exposes `fetch(source_config) -> list[dict]` keyed on source.type.
   - factory/sources/hn.py — Algolia HN search via the url_template in config/market_radar_sources.yaml. Returns [{url, title, author, captured_at, body_text}].
   - factory/sources/reddit.py — fetches new.json with User-Agent "venture-factory/0.1 by youval"; handles 429 with exponential backoff (max 3 retries).
   - factory/sources/ph.py — raises NotImplementedError unless enabled (placeholder).
   Each fetcher respects rate_limit_rpm from source config. Persist last-call timestamps in factory/state.db (table: source_rate_limit).

3. Update scripts/run_agent.py:
   - --dry-run becomes opt-in. Default behavior: real Anthropic API.
   - Read ANTHROPIC_API_KEY from .env at startup; exit 1 with clear message if missing/empty.
   - Default model: claude-sonnet-4-6; override to claude-opus-4-6 for build_decisions. Read overrides from a new config/agent_models.yaml shipped with defaults.
   - When invoking market_radar, pre-fetch each enabled source via factory.sources.fetch and inject raw items into the prompt as {pre_fetched_items}.
   - Update prompts/market_radar.md so the model deduplicates/structures {pre_fetched_items} rather than fetching.

4. Wire the scoring chain (each agent's runner branch):
   - opportunity_scoring: scan opportunities/*.opportunity.json with no sibling .scoring.json; score via API; write opportunities/<id>.scoring.json.
   - pain_validation: scan opportunities/*.scoring.json with total >= scoring_model.yaml min_total_to_validate AND no sibling .verdict.json; write opportunities/<id>.market_evidence.md + opportunities/<id>.verdict.json.

5. Wire daily_summary: aggregate logs/runs/<today>/*.jsonl + opportunities/* counts by status + approval_queue/* with age + every services/<slug>/status.md, apply prompts/daily_summary.md, write reports/daily/<YYYY-MM-DD>.md per templates/daily_summary.md shape. Tag sample values EXAMPLE ONLY.

6. Update scripts/run_daily_loop.py to run: market_radar → pain_validation → opportunity_scoring → cost_gain (stub, log NOT_IMPLEMENTED) → build_decisions (stub) → daily_summary. Each in its own try/except so one failure doesn't stop the rest.

7. Update scripts/smoke_test.py to do a LIVE end-to-end smoke against a single HN source with rate_limit_rpm=1. Assert: ≥1 opportunity file, ≥1 scoring file, ≥1 daily report, total spend in spend_ledger < $0.20. Exit non-zero on any failure.

8. Run `uv run smoke` yourself. Must pass. Then commit: "Phase 1: live API + real sources + scoring chain". If smoke fails, write the failure summary to CHANGES.md and stop before commit.

Constraints:
- Stay minimal. No new frameworks.
- No outside-world send (email/sms/payment/deploy). Those still route through approval_queue/.
- Every API call writes to factory/state.db spend_ledger (date, agent, model, tokens_in, tokens_out, cost_usd).
- Every agent run emits one log line to logs/runs/<today>/<agent>.jsonl per config/logs_format.yaml.
- All paths repo-relative.
- If ARCHITECTURE.md and config/* conflict, ARCHITECTURE.md wins; note divergence in CHANGES.md.
```

---

### P1.5 — Cost optimization (PENDING — run first on Mac)

```text
You are Claude Code. Working directory: ~/Documents/venture-factory. Phase 1 core wiring (P1) is complete and committed. ARCHITECTURE.md is the spec.

Goal: collapse API spend by ~70% with zero capability loss. Five levers, baked into the existing runner — no new agents, no new frameworks.

Tasks, in order:

1. **Prompt caching** in scripts/run_agent.py:
   - Restructure the Anthropic call so `system` is a LIST of blocks, not a string. Stable blocks get `cache_control: {"type": "ephemeral"}`. Variable per-call content stays uncached.
   - Cacheable: the AGENT.md content, injected schema files (templates/*.schema.json), and injected config (config/scoring_model.yaml, config/cost_gain_model.yaml, etc.).
   - Uncacheable: per-call inputs (pre-fetched items, current opportunity payload, today's date, correlation_id).
   - Cache lifetime: ephemeral (5 min) is fine — the daily loop runs all agents within minutes of each other and any single agent's batched calls hit the cache within seconds.
   - Update spend_ledger to record `cache_creation_input_tokens` and `cache_read_input_tokens` separately, priced correctly (cache write = base × 1.25; cache read = base × 0.10).

2. **Batched scoring & validation**:
   - opportunity_scoring branch: instead of one API call per opportunity, batch N=15 opportunities per call (configurable in config/agent_models.yaml as `batch_size`). Returns an array of scoring objects. The system prompt is loaded once per batch — cache amortization kicks in across batches within the same run.
   - pain_validation already accepts an array ({top_candidate_opportunities}); confirm the runner batches up to 10 candidates per call.
   - Update prompts/opportunity_scoring.md so the Inputs section accepts `{opportunities}` (array) instead of `{opportunity}` (singular), and the Output contract is an array. Keep the per-item scoring logic identical.

3. **Pre-filter source inputs** in factory/sources/hn.py and factory/sources/reddit.py:
   - Drop items where: body is `[deleted]`/`[removed]`, author matches a known-bot pattern (configurable list in source module), upvotes < threshold (HN points >= 3, Reddit score >= 2), URL already in opportunities/_seen.jsonl.
   - Truncate body_text to first 500 chars before returning.
   - Log per-source counts: fetched, dropped_by_rule, kept. Add as `tags` on the market_radar log entry.

4. **Model routing** via config/agent_models.yaml (ship populated):
   ```yaml
   schema_version: 1
   defaults:
     model: claude-sonnet-4-6
     max_tokens: 2048
   agents:
     market_radar:        { model: claude-sonnet-4-6, max_tokens: 4096 }
     pain_validation:     { model: claude-sonnet-4-6, max_tokens: 3072, batch_size: 10 }
     opportunity_scoring: { model: claude-sonnet-4-6, max_tokens: 4096, batch_size: 15 }
     cost_gain:           { model: claude-sonnet-4-6, max_tokens: 1024 }
     build_decisions:     { model: claude-opus-4-6,   max_tokens: 2048 }
     service_builder:     { model: claude-sonnet-4-6, max_tokens: 4096 }
     product_design:      { model: claude-sonnet-4-6, max_tokens: 3072 }
     outreach:            { model: claude-sonnet-4-6, max_tokens: 1024 }
     support:             { model: claude-sonnet-4-6, max_tokens: 1024 }
     daily_summary:       { model: claude-haiku-4-5-20251001, max_tokens: 2048 }
   ```
   Runner reads this at startup; agent's `model` and `max_tokens` come from here. If the file is missing, fall back to defaults and log a warning.

5. **Skip-when-no-work** preconditions in scripts/run_agent.py:
   - Add a per-agent precondition function `should_run(agent: str) -> tuple[bool, str]`:
     - opportunity_scoring: True iff any opportunities/*.opportunity.json lacks a sibling .scoring.json.
     - pain_validation: True iff any *.scoring.json with `total >= config/scoring_model.yaml min_total_to_validate` lacks a sibling .verdict.json.
     - cost_gain: True iff any verdict=validated lacks a sibling .cost_gain.json.
     - build_decisions: True iff any .cost_gain.json lacks a sibling .decision.json.
     - market_radar, daily_summary: always True.
   - If False, write a log entry with `status=no_op`, `outputs_summary=<reason>`, zero spend, and exit that agent branch before any API call.

6. **Cost report**:
   - New scripts/cost_report.py: prints today's spend grouped by agent, separating cache_write / cache_read / standard input tokens / output tokens, and the actual USD spent vs cap. Flag `--since YYYY-MM-DD` to span a date range.
   - Add `cost-report` to [project.scripts] in pyproject.toml.

7. **Smoke regression**:
   - Update scripts/smoke_test.py so the second consecutive run (with no new sources) hits ZERO non-cached input tokens on opportunity_scoring's second batch (cache hit on system prompt). Assert spend_ledger today's total is below P1's smoke baseline — record the baseline once on first run and persist it in factory/state.db (table: smoke_baseline).

8. Run `uv run smoke` (must pass). Run `uv run cost-report` and paste its output into CHANGES.md under a new "Phase 1.5 baseline" heading. Commit: "Phase 1.5: prompt caching + batching + prefilter + model routing + skip-no-work".

Constraints:
- Stay minimal. No new pip deps beyond what's already declared.
- Do NOT change agent capabilities or output contracts — only how/when calls are made.
- Caching is transparent to the agent; the LLM still sees the same effective prompt.
- Cost ceilings from config/approval_policy.yaml still apply (P3 will enforce them; for now, runner just records).
- If Anthropic SDK version doesn't support cache_control blocks, bump it in pyproject.toml and update uv.lock.
- ARCHITECTURE.md remains authoritative. Note any divergence in CHANGES.md.
```

---

### P2 — Scheduler + operator inbox + morning brief (PENDING — adapt for macOS)

This was originally written for Windows (Task Scheduler + PowerShell). On Mac, swap the scheduler implementation to **launchd** and rewrite the morning brief as a shell script. Everything else (approvals inbox, RUNBOOK section, project.scripts entries) ports without change.

```text
You are Claude Code. Working directory: ~/Documents/venture-factory. Phase 1 core wiring is complete and committed. ARCHITECTURE.md is the spec.

PLATFORM NOTE: this is being run on macOS. The original prompt referenced Windows Task Scheduler and PowerShell. Replace those with launchd + zsh. Keep all other tasks identical.

Goal: scheduling + operator daily UX so Youval runs the factory in ~15 minutes a day.

Tasks:

1. scripts/com.youval.venturefactory.daily.plist — launchd LaunchAgent plist that runs scripts/run_daily_loop.py daily at 06:00 Asia/Jerusalem. Use the absolute path to `uv` (resolve from `which uv`) and the `daily-loop` entry from [project.scripts]. WorkingDirectory must be the repo path. Set RunAtLoad=false, StartCalendarInterval to 06:00 IDT (translate to local clock if needed using zoneinfo at install time), and StandardOutPath/StandardErrorPath to logs/launchd/daily.{out,err}.log.

2. scripts/install_schedule.sh — idempotent installer:
   - Copies the plist into ~/Library/LaunchAgents/
   - Runs `launchctl unload` on any existing version, then `launchctl load -w` on the new one
   - Prints next-fire time via `launchctl list | grep venturefactory`
   - Detects whether ~/Library/LaunchAgents exists and creates it if not.

3. scripts/approvals_inbox.py — CLI listing every approval_queue/*.json with: ulid, agent, action_type, age_hours, cost_estimate_usd, summary[:80]. Sort by created_at desc. Flags:
   - --expiring: only items within 6h of expires_at
   - --bulk-approve <action_type_glob>: call scripts/approve.py for each match, print results
   - --bulk-reject <action_type_glob> --reason "<text>": same for reject
   - default (no flags): list and exit.

4. scripts/morning_brief.sh — Youval runs this at 08:30 IDT each morning:
   - Resolves today's reports/daily/<date>.md (or yesterday's if today's hasn't generated yet)
   - Opens it via `open` (so it lands in the default Markdown editor)
   - Runs `uv run python scripts/approvals_inbox.py --expiring`
   - Prints: "Full inbox: uv run python scripts/approvals_inbox.py"
   Make it executable (chmod +x).

5. Append a "Schedule operations" section to RUNBOOK.md: install_schedule.sh, `launchctl list | grep venturefactory` to check status, unload/load to disable/re-enable, and morning_brief.sh usage. Append as a new section at the end — do not rewrite existing content.

6. Add `daily-loop`, `inbox`, `brief` entries to [project.scripts] in pyproject.toml mapping to the right modules/scripts.

7. Commit: "Phase 1: launchd scheduler + operator inbox + morning brief".

Constraints:
- All new scripts must be runnable as `uv run python scripts/<name>.py` or directly (`./scripts/<name>.sh`).
- No new pip dependencies.
- Use stdlib zoneinfo for any time math; assume Asia/Jerusalem.
- Do NOT touch scripts/run_agent.py or scripts/run_daily_loop.py. If a surgical edit is unavoidable, note it in CHANGES.md.
```

---

### P3 — Safety hardening (PENDING — run after P1.5; can be parallel with P2)

```text
You are Claude Code. Working directory: ~/Documents/venture-factory. Phase 1 core wiring is complete and committed. ARCHITECTURE.md is the spec.

Goal: safety hardening so the factory cannot blow the budget, leak secrets, or send outreach during Shabbat.

Tasks:

1. Per-day USD cap enforcement in scripts/run_agent.py:
   - Before each Anthropic call, sum today's spend_ledger rows. If projected next call (estimated tokens × model price) would exceed config/approval_policy.yaml caps.per_day_external_api_usd, do NOT call.
   - Instead, emit approval_queue/<ulid>.json with action_type=spend_above_daily_cap (summary, current_spend, requested_overage, expires_at = now + 24h) and exit with a log entry status=awaiting_approval.
   - Per-action ceiling: never exceed caps.per_action_usd_hard_ceiling on a single call. Same emit-and-stop pattern.
   - Hardcode current Sonnet/Opus/Haiku per-million-token prices with a "// update from anthropic pricing page" comment.

2. Fail-closed startup in run_agent.py and run_daily_loop.py:
   - Missing/empty ANTHROPIC_API_KEY → exit 1, message "ANTHROPIC_API_KEY required; see .env.example".
   - Missing/unparseable config/approval_policy.yaml → exit 1, message "fail-closed: approval policy unreadable".
   - Never log the key value. Redact from any error trace.

3. Shabbat block in scripts/run_daily_loop.py:
   - Compute now in Asia/Jerusalem.
   - If within Fri 18:00 → Sat 20:00 IDT, set RUN_MODE=read_only.
   - In read_only, skip any agent whose AGENT.md permissions include any of: send_outreach_email, send_outreach_sms, create_payment_link, charge_customer, deploy_public_domain, send_customer_message. Log SKIP with reason="shabbat_read_only".
   - market_radar, opportunity_scoring, pain_validation, cost_gain, daily_summary still run.

4. scripts/test_safety.py (pytest):
   - test_missing_key: blank ANTHROPIC_API_KEY env, assert run_agent.py exits 1 with the expected message.
   - test_spend_cap: seed spend_ledger near cap, run market_radar, assert one approval_queue/*.json with action_type=spend_above_daily_cap exists and no API call was made.
   - test_shabbat_block: monkeypatch the loop's "now" to Friday 19:00 IDT, run loop, assert read_only is active and outreach-capable agents skipped.
   - test_policy_unreadable: temporarily rename approval_policy.yaml, assert run_daily_loop.py exits 1.
   Add pytest to dev deps in pyproject.toml if not present.

5. Wire `uv run safety` in [project.scripts] to invoke pytest on scripts/test_safety.py.

6. Run `uv run safety` (must pass) then `uv run smoke` (must still pass). Commit: "Phase 1: budget cap + fail-closed + Shabbat read-only".

Constraints:
- Do NOT touch files P2 created (scripts/com.youval.venturefactory.daily.plist, scripts/install_schedule.sh, scripts/approvals_inbox.py, scripts/morning_brief.sh). If your tests need to reference the inbox, mock it.
- If RUNBOOK.md was edited by P2, append your Shabbat/safety notes as a separate new section at the end — don't rewrite their additions.
- Token-cost estimation must be conservative: assume max tokens, not actual.
```

---

## After all three commit

1. Register the schedule: `bash scripts/install_schedule.sh`.
2. Kick off a manual seed run so `opportunities/` starts filling: `uv run daily-loop`.
3. Tomorrow 08:30 IDT: `bash scripts/morning_brief.sh`.

Phase 1 (W23 gate) is met when `uv run cost-report` shows healthy spend, `opportunities/` has ≥30 scored entries, and `reports/daily/<date>.md` confirms it.

Phase 2 (W24 Jun 8–14): top 3 candidates promoted via Build Decision, Service Builder scaffolds them, landing pages drafted. **You (Claude) do not pick them — the agents do.**

Phase 3 (W25–W26): approval cycle, landing pages published, outreach round 1, responsiveness data, kill/continue/scale call — three experiments live by Jun 28–30.

---

## Pointers

- Spec: `docs/ARCHITECTURE.md` (15 sections, authoritative).
- Daily operations: `RUNBOOK.md`.
- Original Cowork build summary: ask Youval for the Cowork chat log if anything in the repo is unclear.
- All examples in this repo are EXAMPLE ONLY. The factory picks real services. You do not.
