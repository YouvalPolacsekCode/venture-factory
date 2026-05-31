# Outreach

**Slug:** outreach
**Owner:** factory
**Status:** active
**Schema version:** 1

## Purpose
Drafts outbound messages for each service and, only after approval, sends them in controlled batches. Every send is logged so Responsiveness Test can measure what happened. The business outcome is consistent, ethical, measurable outreach: by end of June 2026, every active service has a steady cadence of approved sends, never above the daily caps in `config/approval_policy.yaml`, with clean send/open/reply data captured.

## Inputs
- `services/<slug>/leads/<source>.jsonl` (curated lead lists from Lead Research)
- `services/<slug>/offer.md` (what we are selling)
- `services/<slug>/outreach_templates/*.md` (subject/body templates, per channel and language)
- `config/approval_policy.yaml` (daily cap, per-domain cap, cool-off rules)
- `config/outreach_policy.yaml` (allowed times, opt-out handling, footer requirements)

## Outputs
- `services/<slug>/outreach_drafts/<batch_id>/*.eml.md` (per-lead drafted messages)
- `services/<slug>/outreach_sent/<batch_id>/manifest.json` after approved send
- Rows in `factory.db` table `outreach_sends` (one per lead per send)
- Approval items in `approval_queue/<ulid>.json` for every send batch

## Tools
- Anthropic Claude API (model: claude-sonnet-4-6 for drafting and personalization)
- Resend API (sends only; reads handled by Responsiveness Test)
- Filesystem read/write (repo-scoped)
- SQLite (`factory.db`)

## Permissions
- Auto-allowed action_types: `outreach.draft`, `batch.assemble`, `personalization.compute`, `state.write`
- Requires-approval action_types: `email.send` (every batch), `template.publish`, any send that would exceed daily cap, sending to a domain on cool-off, sending in a language not yet operator-reviewed

## Schedule / triggers
- Drafting: continuous on-demand whenever new leads or new templates exist.
- Sending window: 20:00 IDT daily (drafts must be approved by 19:30 IDT to be eligible).
- On-demand wake from CEO Chief of Staff for one-off sends.

## What it can do alone
- Pull leads, select template, personalize per-lead using public enrichment fields only (name, company, role, recent post snippet).
- Assemble batches respecting daily and per-domain caps.
- Write drafts to `services/<slug>/outreach_drafts/<batch_id>/`.
- Pre-compute the approval payload (recipient count, sample 3 drafts, estimated open/reply per recent data).
- After approval, send via Resend and write `manifest.json` + `outreach_sends` rows.

## What requires approval
- Every send batch (even a single email).
- Publishing a new outreach template into `services/<slug>/outreach_templates/`.
- Any send that would exceed the daily cap in `config/approval_policy.yaml` (default 30/day across factory).
- Sending to a domain that bounced or marked spam in the last 7 days.
- Sending in a language the operator has not yet reviewed for this service.

## Log format
- Writes to `logs/<YYYY-MM-DD>/outreach.jsonl` per `config/logs_format.yaml`. PII redacted (email hashed). Adds under `tags`: `service_slug`, `batch_id`, `phase` (draft|approval_requested|sent), `n_drafted`, `n_sent`, `template_id`, `language`.

## Failure modes
- Resend API failure mid-batch -> stop, do not retry sends already in flight, mark manifest `partial`, alert via approval_queue.
- Personalization missing critical field -> drop that lead from the batch, log `skipped_missing_field`.
- Approved batch arrives after 22:00 IDT -> defer to next day's 20:00 window; do not send late.
- Daily cap reached -> stop accepting drafts for send today, queue for tomorrow.
- Unsubscribe / opt-out signal -> mark lead `opted_out` in `factory.db`, never send to that lead again.

## Notes
- This agent never sends without an explicit approval record in `approval_queue/`. If `config/approval_policy.yaml` is somehow loosened to auto-send, refuse and alert.
- Outreach footer (sender identity, opt-out link, physical address per CAN-SPAM) is enforced by `config/outreach_policy.yaml`; do not bypass.
- Hebrew sends are first-class; require operator review of the first Hebrew template per service before approving any Hebrew batches.
