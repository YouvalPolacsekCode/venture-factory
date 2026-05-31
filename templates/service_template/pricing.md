# Pricing

<!-- Full pricing structure. The headline number lives in offer.md; everything else lives here. -->

## Pricing model

<!-- Pick one and justify. -->
- Model: <!-- one-off | subscription | usage -->
- Rationale: <!-- why this model fits the service shape and buyer behaviour -->

## Price points and rationale

<!-- Anchor + main + premium where applicable. State the value-based logic behind each number, not "what feels right". -->

| Tier | Price (USD) | Price (ILS) | What's included | Target buyer |
|---|---|---|---|---|
| <!-- Starter --> | <!-- 99 --> | <!-- 360 --> | <!-- scope --> | <!-- who buys this --> |
| <!-- Standard --> | <!-- 199 --> | <!-- 720 --> | <!-- scope --> | <!-- ... --> |
| <!-- Premium (optional) --> | <!-- 499 --> | <!-- 1,800 --> | <!-- scope --> | <!-- ... --> |

<!-- EXAMPLE ONLY pricing logic: "Standard tier at USD 199 sits at ~10% of the manual-labour cost the buyer would otherwise pay an accountant (USD ~2,000)." -->

## Discounts and launch offers

<!-- Time-boxed promotions. Each one must have an expiry. -->

- Launch offer: <!-- e.g., first 10 customers get 30% off, expires YYYY-MM-DD IDT -->
- Referral discount: <!-- e.g., 15% off for both parties -->
- Bulk / multi-seat: <!-- ... -->

## Israel VAT note

<!-- Israeli VAT (Ma'am / מע"מ) is 17% as of 2025. -->
- For Israeli customers (ILS billing): prices shown ARE inclusive / EXCLUSIVE of 17% VAT. <!-- pick one and be consistent across the landing page and invoices -->
- For non-Israeli customers (USD billing): VAT not applicable; reverse-charge or B2C rules per jurisdiction.
- Tax invoice (חשבונית מס) must be issued for Israeli sales — see `payment_path.md` for the receipt flow.

## Currency

- Default for international customers: USD
- For Israeli customers: ILS
- Conversion reference rate source: <!-- e.g., daily Bank of Israel representative rate -->
- Display logic on landing page: <!-- IP-based, language toggle, or explicit selector -->

## Stripe product / price IDs

<!-- Filled in by the Payment / Ops agent after creating the products in Stripe. Do NOT hand-edit once set; recreate via Stripe dashboard if needed. -->

| Tier | Stripe product ID | Stripe price ID (USD) | Stripe price ID (ILS) |
|---|---|---|---|
| <!-- Starter --> | <!-- prod_... --> | <!-- price_... --> | <!-- price_... --> |
| <!-- Standard --> | <!-- prod_... --> | <!-- price_... --> | <!-- price_... --> |
| <!-- Premium --> | <!-- prod_... --> | <!-- price_... --> | <!-- price_... --> |
