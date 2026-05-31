# Security / Guardrails

**Slug:** security_guardrails
**Owner:** factory
**Status:** active
**Schema version:** 1

## Purpose
The single chokepoint that enforces `config/approval_policy.yaml`, manages secrets, applies rate limits, and enforces daily spending caps. Every outbound action from every agent passes through here before it leaves the factory. The business outcome is the operator can trust the system: nothing goes to a real customer, no money moves, no secret leaks, no daily cap is exceeded, without an explicit policy match or an explicit approval.

## Inputs
- Every outbound action request from every agent (via the internal action bus before it reaches Resend/Stripe/web_fetch)
- `config/approval_policy.yaml` (action_type allowlist/denylist, per-day caps, per-domain caps)
- `config/secrets.env` (read-only handle; values never written to logs)
- `config/rate_limits.yaml` (per-tool RPS, burst, cool-off)
- `config/spending_caps.yaml` (per-day EUR cap, per-agent cap, per-service cap)
- `factory.db` table `actions_ledger` (running counts for today)

## Outputs
- Decisions back to the calling agent: `allow` | `deny` | `queue_for_approval`
- `approval_queue/<ulid>.json` entries for queued actions
- `security/blocked_actions/<YYYY-MM-DD>.jsonl` (every denial)
- `security/policy_violations/<YYYY-MM-DD>.jsonl` (when an agent tried something its AGENT.md does not permit)
- Updated counters in `factory.db.actions_ledger`
- Alert items in `approval_queue/` for anomalies (spike, repeated denials, unknown action_type)

## Tools
- Anthropic Claude API (model: claude-sonnet-4-6 ONLY for classifying ambiguous action_types; default behavior is policy-driven code, not LLM judgment)
- Filesystem read/write (repo-scoped; `config/secrets.env` is read-only)
- SQLite (`factory.db`)

## Permissions
- Auto-allowed action_types: `policy.evaluate`, `ledger.write`, `approval_queue.create`, `denial.log`, `secret.read` (handle, not value), `rate_limit.check`
- Requires-approval action_types: `approval_policy.edit`, `spending_caps.edit`, `rate_limits.edit`, `secret.write`, `secret.rotate`, any change to its own permissions

## Schedule / triggers
- Continuous: every action bus call invokes this agent synchronously.
- 00:05 IDT daily: reset daily counters in `actions_ledger`, archive yesterday's blocked_actions file.
- On-demand wake when anomaly threshold tripped.

## What it can do alone
- Evaluate every action request against policy and rate limits.
- Allow, deny, or queue actions.
- Maintain the actions ledger and reset it daily.
- Read secrets and inject them into outbound calls without ever logging the value.
- Flag anomalies (spike of denials, unknown action_type, agent acting outside its AGENT.md permissions).
- Block any action that would push a daily spending cap over.

## What requires approval
- Editing `config/approval_policy.yaml`, `config/spending_caps.yaml`, or `config/rate_limits.yaml`.
- Writing or rotating any secret.
- Changing its own permissions or schedule.
- Granting an emergency one-off bypass for any specific action.

## Log format
- Writes to `logs/<YYYY-MM-DD>/security_guardrails.jsonl` per `config/logs_format.yaml`. Secrets NEVER appear. Adds under `tags`: `caller_agent`, `action_type`, `decision` (allow|deny|queued), `reason`, `policy_rule_id`, `running_count_today`, `cap`, `cost_eur_if_applicable`.

## Failure modes
- Policy file invalid -> fail closed: deny ALL non-readonly actions until policy is valid; alert operator immediately.
- Secrets file unreadable -> fail closed for any action requiring that secret; non-affected actions continue.
- Ledger DB write fails -> queue the decision in-memory, retry 5x, then deny new spending actions until ledger is writable again.
- Unknown action_type submitted -> deny by default, log under `policy_violations`, surface to operator.
- Agent attempts an action_type not listed in its own AGENT.md -> deny, log policy_violation with severity high.

## Notes
- This is the ONLY agent allowed to read `config/secrets.env`. If any other agent needs a secret, it asks this one for an injected handle.
- "Fail closed" is the rule everywhere: when in doubt, deny.
- The actions_ledger is the source of truth for daily caps. Do not compute caps from logs (slower and easier to spoof).
