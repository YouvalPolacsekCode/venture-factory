# Responsiveness Test

<!-- The structured test that decides whether to keep building this service or kill it. Run before scaling outreach. -->

## Hypothesis

<!-- One sentence in the form: "If we send <message> to <cohort> via <channel>, we expect <metric> >= <threshold> within <window>." -->
<!-- EXAMPLE ONLY: "If we send a personalized 80-word LinkedIn DM to 50 Israeli SaaS finance managers, we expect a reply rate >= 15% within 7 days." -->

## Cohort definition

<!-- Exact criteria for who is in the test. Pull from lead_sources.md. -->

- ICP filter: <!-- role, industry, size, geo -->
- Exclusion: <!-- existing customers, suppression list, anyone contacted in last 90 days -->
- Sourcing: <!-- which channel from lead_sources.md -->

## Sample size

<!-- Be honest about statistical power. For early-stage validation, 30-100 per variant is usually enough to see a strong signal, not enough to confirm a weak one. -->

- N per variant: <!-- e.g., 50 -->
- Variants: <!-- e.g., 2 -->
- Total N: <!-- e.g., 100 -->
- Rationale: <!-- why this size is enough to inform a kill/continue decision -->

## Channels tested

<!-- One channel per test ideally. If multi-channel, log channel per send. -->

- Primary: <!-- e.g., LinkedIn DM -->
- Secondary (if any): <!-- e.g., follow-up email after 4 days -->

## Message variants (A/B)

### Variant A

<!-- Full copy. Personalization tokens in {curly_braces}. -->
- Subject / hook: <!-- ... -->
- Body: <!-- ... -->
- CTA: <!-- ... -->

### Variant B

- Subject / hook: <!-- ... -->
- Body: <!-- ... -->
- CTA: <!-- ... -->

## Metrics tracked

<!-- Capture every step of the funnel. Map each metric to where it's logged. -->

| Metric | Definition | Logged in |
|---|---|---|
| Sent | Successful delivery (not bounced) | <!-- outreach log path --> |
| Opened | First open (email only) | <!-- ... --> |
| Replied | Any human reply, positive or negative | <!-- ... --> |
| Positive reply | Indicates interest | <!-- ... --> |
| Booked | Form submitted or call booked | <!-- ... --> |
| Paid | Charge succeeded | <!-- ... --> |

## Success threshold

<!-- Maps to the responsiveness_signal scale in `config/scoring_model.yaml`. A test below the kill threshold triggers a kill recommendation in the next weekly review. -->

- Kill threshold: <!-- reply rate < X% AND booked = 0 -->
- Continue threshold: <!-- reply rate >= X% OR booked >= Y -->
- Scale threshold: <!-- paid >= Z within test window -->

See `config/scoring_model.yaml` -> `responsiveness_signal` for the scale definition.

## Test window

- Start: <!-- YYYY-MM-DD IDT -->
- End: <!-- YYYY-MM-DD IDT -->
- Duration: <!-- e.g., 7 days from first send -->

## Results log

<!-- Append-only. Each row = one cohort run. -->

| Run ID | Start (IDT) | End (IDT) | Variant | N sent | Replied | Positive | Booked | Paid | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| <!-- run-001 --> | <!-- ... --> | <!-- ... --> | <!-- A --> | <!-- ... --> | <!-- ... --> | <!-- ... --> | <!-- ... --> | <!-- ... --> | <!-- kill / continue / scale --> |
