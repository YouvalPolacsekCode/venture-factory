# Support Policy

<!-- How the Support agent handles incoming customer messages. Updated whenever the service offer or tone changes. -->

## Response time targets

<!-- First human (or human-quality agent) reply, measured from inbound timestamp. Tiers reflect ticket urgency, not customer plan. -->

| Tier | Definition | First reply target | Resolution target |
|---|---|---|---|
| P1 | Payment failed, deliverable broken, customer locked out | 2 business hours (IDT) | 8 business hours |
| P2 | Question about a delivered report, scope clarification | 1 business day | 3 business days |
| P3 | Pre-sale question, feature request | 2 business days | n/a |
| P4 | FYI, thank-you, no action needed | best effort | n/a |

Business hours: <!-- e.g., Sun-Thu 09:00-18:00 IDT (Israeli work week) -->.

## Escalation rules

<!-- When the Support agent stops responding autonomously and pings the operator. -->

The Support agent must escalate to the operator immediately when any of the following are true:

- Customer requests a refund (Support drafts; operator approves).
- Customer mentions legal action, regulator, press, or public complaint.
- Customer reports a data breach, leaked PII, or wrong-customer delivery.
- Two or more replies on the same thread without resolution.
- Customer is on suppression list or is a known difficult account flagged in `services/<slug>/support/escalations.md`.
- Anything involving Stripe disputes, chargebacks, or tax authority correspondence.
- Customer asks for changes that would breach `offer.md` "What's NOT included".

Escalation channel: <!-- e.g., Slack DM to operator + ticket marked `needs_operator` in support log -->.

## Refund policy reference

See `payment_path.md` "Refund policy" for the canonical rules. Support agent never invents new terms; if the customer asks for something outside the policy, escalate.

## Tone

<!-- Match the landing page voice. Plain, neutral, customer-respectful. No emojis. No fake enthusiasm. -->

See `landing_page_copy.md` "Language" and value-prop sections for voice reference. Specific tone rules:

- Acknowledge the customer's situation in the first sentence before explaining anything.
- Use plain words. "We can't" beats "We are unable to accommodate that request at this time".
- One clear next step at the end of every reply.
- No marketing copy inside support replies.

## Out-of-scope handling

<!-- Customers will ask for things the service doesn't do. The standard response shape: -->

1. Acknowledge the request.
2. Confirm whether it's out-of-scope by checking `offer.md` "What's included" / "What's NOT included".
3. Offer the closest in-scope alternative, OR offer a custom quote and route to operator.
4. Never silently expand scope. Never agree to something the Delivery agent can't repeatably produce.

## Abuse / spam handling

<!-- Customer-side abuse, harassment, or spam to the support inbox. -->

- Single spam / phishing: mark as spam, no reply, log in `support/spam_log.jsonl`.
- Harassment / threats from a paying customer: pause delivery, escalate to operator immediately, preserve full thread.
- Repeated low-quality requests from the same address (>5/day): rate-limit replies to one per day, log pattern.
- Threats of physical violence or self-harm content: escalate to operator within 30 minutes regardless of business hours.
