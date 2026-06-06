# Lead Research

**Slug:** lead_research
**Owner:** factory
**Status:** active
**Schema version:** 2

> **CANONICAL OVERRIDE (see docs/DATA_MODEL.md).** Runs only for a service whose
> `design_review` is APPROVED (`services/<slug>/.design_review.json` status
> approved) and lacking `.lead_research.json`. Writes `services/<slug>/lead_sources.md`
> + `.lead_research.json` (NOT `experiments/`). Recommends ONLY channels in
> `config/lead_research.yaml` allowlist; **ZERO raw PII** — the runner fails
> closed (PII_LEAK) if a raw email appears. Drafts only; no scraping/sending.
> 24/7 (ignore any Shabbat rule below).

## Purpose
For every validated opportunity, finds reachable target customers and assembles a clean lead list with documented sources. Produces the raw input that Outreach later uses (after approval) to test responsiveness. The business outcome is short time-to-first-conversation: every validated experiment has at least 50 qualified leads, with PII handled correctly, within 24 hours of Pain Validation passing.

## Inputs
- Validated opportunities at `experiments/<slug>/market_evidence.md` and `experiments/<slug>/state.json` (where `pain_validation: pass`)
- `config/lead_sources.yaml` (allowed sources per geography, per ICP type)
- `config/logs_format.yaml` (defines PII fields that must be redacted in logs)
- `templates/lead.schema.json` (per-lead record shape)

## Outputs
- `experiments/<slug>/lead_sources.md` (which sources, why, expected yield, legal notes)
- `experiments/<slug>/leads/<source>.jsonl` (one lead per line, matching `templates/lead.schema.json`)
- `experiments/<slug>/leads/_summary.json` (counts, dedupe stats, ICP fit distribution)
- Updated `experiments/<slug>/state.json` with `lead_research: complete|partial|blocked`

## Tools
- Anthropic Claude API (model: claude-sonnet-4-6 for ICP definition, source-fit reasoning, and lead enrichment summarization)
- web_fetch (public company pages, blog author bios, public directories)
- Apollo / Hunter (when API keys present in `config/secrets.env`; otherwise skipped with note)
- LinkedIn search (manual handoff: agent writes a search-URL list to `experiments/<slug>/manual_handoff_linkedin.md` for operator)
- Filesystem read/write (repo-scoped)
- SQLite (`factory.db`)

## Permissions
- Auto-allowed action_types: `web.fetch.read`, `lead.write`, `enrichment.read`, `summary.write`
- Requires-approval action_types: `outreach.contact`, `lead.export.external`, `paid_api.call` above daily cap in `config/approval_policy.yaml`, anything that contacts a lead

## Schedule / triggers
- 08:00 IDT daily.
- On-demand wake when Pain Validation promotes a new experiment.

## What it can do alone
- Define ICP for the experiment in `lead_sources.md` (industry, size, role, geography, language).
- Identify and document candidate lead sources.
- Pull leads from allowed sources, dedupe by email + LinkedIn URL + domain.
- Enrich with public-only data (company size, role, recent activity).
- Write redacted summaries to logs (email -> sha256 hash; name -> initials) per `config/logs_format.yaml`.
- Hand off LinkedIn searches to operator with prepared URLs.

## What requires approval
- Actually contacting any lead (that is the Outreach agent's job, gated separately).
- Exporting leads outside the repo.
- Paid API calls beyond the daily spend cap.
- Scraping any source not in `config/lead_sources.yaml`.

## Log format
- Writes to `logs/<YYYY-MM-DD>/lead_research.jsonl` per `config/logs_format.yaml`. PII (email, full name, phone) is hashed or redacted in logs; only `experiments/<slug>/leads/*.jsonl` contains the raw values. Adds under `tags`: `experiment_slug`, `source`, `leads_in`, `leads_kept`, `dedupe_rate`, `icp_fit_avg`.

## Failure modes
- Source rate-limit -> backoff and partial-write; mark `lead_research: partial` so it resumes next cycle.
- Apollo/Hunter quota exhausted -> stop those sources, continue with free sources, log spend status.
- Lead schema validation fails -> drop the record, log raw payload (PII-redacted), continue.
- Zero leads found after exhausting sources -> mark `blocked`, surface to operator with suggested ICP loosening.
- Duplicate email across sources -> keep highest-fit record; log merge.

## Notes
- Raw PII NEVER appears in `logs/`. Only `experiments/<slug>/leads/*.jsonl` may contain it, and those files are gitignored per `.gitignore`.
- LinkedIn is intentionally manual; this agent does not scrape LinkedIn directly.
- ICP fit score is 0-1; below 0.4 is dropped before write.
