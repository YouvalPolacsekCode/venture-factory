# Market Evidence

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|---|
| 2026-10-31 | https://salesforce.stackexchange.com/questions/439960/signuprequest-with-connectedappconsumerkey-always-ends-in-status-error-errorcod | Forum post | Single ISV developer building a GitHub Actions org-provisioning workflow hitting opaque C-1016 error with no Salesforce documentation to resolve it | 2 |

**Evidence count: 1 distinct pain source. Minimum required: 5. FAIL.**

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| Gearset | SaaS (Salesforce DevOps) | ~$150–$450/user/month | Focused on metadata deployment, not org provisioning/SignupRequest API debugging |
| Copado | SaaS (Salesforce DevOps) | ~$200–$800/user/month | Enterprise CI/CD for Salesforce metadata, not SignupRequest/Trialforce headless auth flows |
| Salesforce Partner Community / docs | DIY / status quo | Free | Sparse, non-actionable documentation for Trialforce API error codes |

## Willingness-to-pay evidence

- Quote: No direct quote found expressing willingness to pay for a SignupRequest diagnostic tool.
- Competitor pricing reference: Gearset ($150–$450/user/month), Copado ($200–$800/user/month) — these address adjacent Salesforce DevOps pain, not this specific API error class.
- Paid job postings: No job postings found specifically for Salesforce org-provisioning API expertise.

**WTP signal: inferred only from adjacent market. No direct signal. FAIL.**

## Estimated TAM / SAM

### Israel
- TAM: Salesforce ISV partners in Israel is estimated at <200 companies (Salesforce AppExchange lists ~6,500 ISVs globally; Israel's tech sector ~3% of global SaaS = ~200 ISVs). Of those, the subset automating org provisioning via SignupRequest API is likely <50. At $29–79/month: USD 17K–47K/year. Sub-material.
- SAM (reachable in 12 months): ~20–40 ISV engineers reachable via Salesforce Partner Community Israel chapter.

### Global
- TAM: ~6,500 Salesforce AppExchange ISVs globally; subset automating org provisioning estimated at 5–10% = ~500 teams. At $49/month average: USD 294K/year. Very small.
- SAM (reachable in 12 months): ~200 ISV engineers active in Salesforce Partner Community forums and Stack Exchange.

## Source list

- https://salesforce.stackexchange.com/questions/439960/signuprequest-with-connectedappconsumerkey-always-ends-in-status-error-errorcod (retrieved 2026-10-31 IDT)

---
**Verdict: REJECTED.** Evidence count (1) is far below the minimum threshold of 5 distinct pain quotes. No direct WTP signal found. TAM is sub-material at global scale. The pain is real but the addressable population is too small and too thinly documented to justify advancing. Not recommended for re-queue — recommend Market Radar monitor for signal volume growth over 90 days before reconsidering.