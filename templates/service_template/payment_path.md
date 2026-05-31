# Payment Path

<!-- The end-to-end money flow. The Payment / Ops agent owns this file. -->

## Pricing reference

See `pricing.md` for tiers, currencies, VAT treatment, and Stripe IDs.

## Payment method

<!-- Pick exactly one. Default to Stripe Payment Link for simplicity in Phase 1.5. -->

- Method: <!-- Stripe Payment Link | Stripe Checkout | manual invoice -->
- Reason: <!-- e.g., Payment Link — zero code, hosted page, supports ILS + USD -->
- Link(s): <!-- per-tier Payment Link URLs, filled after creation -->

## Trigger

<!-- When the charge is initiated in the customer journey. -->

- Trigger point: <!-- post-form | post-call | post-trial | pre-delivery -->
- Rationale: <!-- e.g., post-form because the deliverable is fully automated and customer expectation is "pay then receive" -->

## Refund policy

<!-- Customer-visible policy. Must match what's promised in offer.md risk reversal and on the landing page. -->

- Window: <!-- e.g., 14 days from delivery -->
- Conditions: <!-- e.g., no questions asked / requires evidence of issue -->
- Processing time: <!-- e.g., refund issued within 5 business days, lands in 5-10 banking days -->
- Cap: <!-- e.g., full refund | partial pro-rata for subscription -->

## Failure path

<!-- What happens when a charge fails or a customer drops off without paying. -->

| Failure | Detection | Action | Owner |
|---|---|---|---|
| Card declined at checkout | Stripe webhook `payment_intent.payment_failed` | Send retry email with new link, max 3 attempts | Payment agent |
| Customer abandons checkout | No `checkout.session.completed` within 24h | Single reminder email, then drop | Outreach agent |
| Chargeback / dispute | Stripe webhook `charge.dispute.created` | Pause delivery; ping operator | Support agent |
| Currency mismatch | Manual catch | Refund + reissue correct-currency link | Payment agent |

## Receipts

<!-- Israeli law requires a tax invoice (חשבונית מס) for sales to Israeli customers. -->

- Stripe receipt: enabled by default for all customers (email).
- Israeli tax invoice (חשבונית מס): generated via <!-- e.g., Greeninvoice, Hashavshevet, or manual --> for ILS-billed customers; sent within 7 days of payment.
- Receipt language: matches customer billing currency (USD -> English, ILS -> Hebrew).
- VAT line item: 17% explicitly shown on Israeli invoices.

## Operator audit trail

<!-- Every payment event written to a per-customer folder so we can reconstruct any dispute. -->

- Path: `payments/<customer_email_hash>/`
- Files written per customer:
  - `events.jsonl` — every Stripe webhook event, append-only
  - `invoices/` — PDF receipts and tax invoices
  - `notes.md` — operator notes (refunds, disputes, manual overrides)
- Retention: 7 years (Israeli tax record retention requirement).
