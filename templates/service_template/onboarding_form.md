# Onboarding Form

<!-- The form a customer fills out to start the service. Keep it short — every extra field drops conversion. -->

## Form purpose

<!-- One sentence: what we collect, why we need it, and what happens immediately after submit. -->
<!-- EXAMPLE ONLY: "Collect the minimum inputs needed for the Delivery agent to produce the report, plus contact details for follow-up." -->

## Fields

<!-- Required only if the Delivery agent literally cannot start without it. Each field's helper text is what the user sees under the input. -->

| Field | Type | Required | Validation | Helper text |
|---|---|---|---|---|
| Full name | text | yes | 2-80 chars | <!-- e.g., "As it should appear on the report" --> |
| Work email | email | yes | RFC 5322, no free providers if B2B | <!-- "We'll send your deliverable here" --> |
| Company | text | yes | 2-80 chars | <!-- ... --> |
| <!-- service-specific field --> | <!-- text / select / file --> | <!-- yes/no --> | <!-- ... --> | <!-- ... --> |
| Consent to email | checkbox | yes | must be true | <!-- "I agree to receive my deliverable and follow-ups by email" --> |

## Submit destination

<!-- Pick exactly one based on the service shape. -->

- Tool: <!-- Cal.com | Tally | Google Forms | custom -->
- Reason: <!-- e.g., "Tally — supports payment-on-submit and webhooks to Make.com" -->
- Webhook target: <!-- e.g., Make.com scenario URL or n8n endpoint -->
- Submission storage: <!-- e.g., `services/<slug>/intake/submissions.jsonl` -->

## Post-submit flow

<!-- Step-by-step what happens within 5 minutes of submission. The customer must never wonder if the form went through. -->

1. Immediate on-screen confirmation: <!-- copy, e.g., "Got it — check your inbox in 2 minutes." -->
2. Confirmation email sent (from: <!-- ... -->, subject: <!-- ... -->), with: order summary + next steps + payment link if not yet paid.
3. Payment link issued via Stripe (see `payment_path.md`).
4. Internal alert to operator: <!-- channel + format, e.g., Slack #factory-intake -->
5. Delivery agent triggered: <!-- automated or queued for next operator approval -->

## Data handling note

<!-- Where the data goes, how long it stays, who can access it. The user-facing version of this lives in the privacy policy. -->

- Storage location: <!-- e.g., encrypted in `services/<slug>/intake/` + Stripe for payment data -->
- Retention: <!-- e.g., 24 months from last interaction, then deletion -->
- Access: <!-- which agents and which humans can read it -->
- Cross-border: <!-- e.g., data may transit US (Stripe), EU (Make.com) -->
- Deletion request handling: <!-- response SLA, contact -->
