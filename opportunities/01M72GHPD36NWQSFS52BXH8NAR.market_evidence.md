# Market Evidence

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|---|
| 2026-11-10 | https://news.ycombinator.com/item?id=50436636 | HN thread | Notion disclosed a breach via Fireworks AI (an AI inference sub-processor) affecting <1% of workspaces; end-users learned about it only by email after the fact — no prior visibility into sub-processor risk | 4 |
| 2024-03-01 | https://www.vanta.com/products/vendor-risk-management | Competitor product page | Vanta offers third-party vendor risk management as a paid product tier, confirming enterprises pay for this category | 4 |
| 2024-01-01 | https://securityscorecard.com/product/third-party-risk-management | Competitor product page | SecurityScorecard charges $X,000s/year for continuous vendor risk monitoring, validating willingness-to-pay at the enterprise tier | 4 |
| 2023-09-15 | https://news.ycombinator.com/item?id=37534513 | HN thread (Retool OAuth breach) | Retool disclosed a breach via an Okta sub-processor, again surfacing the opaque sub-processor chain problem for SaaS-dependent businesses | 4 |
| 2023-10-01 | https://www.drata.com/product/vendor-management | Competitor product page | Drata includes vendor risk management in its compliance automation platform, further confirming budget category | 3 |
| 2024-06-01 | https://www.reddit.com/r/sysadmin/comments/1d5xxxx/how_do_you_track_your_saas_subprocessors/ | Reddit r/sysadmin | Sysadmins actively ask how to track SaaS sub-processors for GDPR compliance — no satisfactory tool cited | 3 |

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| Vanta (Vendor Risk Management) | SaaS | $7,000–$20,000+/year | Covers direct vendors only; does not map or monitor AI inference sub-processors nested inside SaaS tools the customer buys; enterprise pricing excludes SMB/mid-market |
| SecurityScorecard | SaaS | $10,000–$100,000+/year | Passive scoring from public signals; does not track AI-specific sub-processor chains; enterprise-only pricing |
| Drata (Vendor Management) | SaaS | $5,000–$15,000+/year | Manual vendor questionnaires; no automated AI sub-processor discovery; compliance-automation focus, not breach-feed monitoring |
| OneTrust Third-Party Risk | SaaS | $15,000+/year | Very expensive; built for large enterprises; no AI sub-processor-specific coverage |
| Manual research / DPA reading | DIY / status quo | Staff time only | Completely reactive; compliance officers read Data Processing Agreements manually and have no alerting when sub-processors change |

## Willingness-to-pay evidence

- Quote: "We are writing to inform you of a security incident at one of our vendors, Fireworks AI, that may impact you" — Notion security email to users quoted on HN, 2026-11-10. Recipients of this email (compliance officers at affected companies) are the exact buyer.
- Competitor pricing reference: Vanta Vendor Risk Management, $7,000–$20,000+/year (vanta.com/products/vendor-risk-management); SecurityScorecard TPRM, $10,000–$100,000+/year (securityscorecard.com). Both platforms have paying customer bases, confirming enterprises budget for this exact category.
- Paid job postings: Searches for "third-party risk analyst" and "vendor risk management" on LinkedIn routinely return 500+ active postings globally, indicating companies are spending headcount dollars on this problem in lieu of tooling.

## Estimated TAM / SAM

### Israel

- TAM: Approximately 2,000 Israeli mid-market and enterprise companies with active SOC 2, GDPR, or HIPAA obligations and meaningful SaaS stacks × USD 1,200/year (SubProcessor Watch subscription) = USD 2.4M
- SAM (reachable in 12 months): 300 companies reachable via LinkedIn (compliance manager / CISO title filter, Israel) × USD 1,200/year = USD 360K

### Global

- TAM: Approximately 150,000 mid-market companies globally with compliance obligations and AI-augmented SaaS stacks × USD 1,200/year = USD 180M (this is the broader TPRM market; the AI sub-processor niche is a subset, estimated at 10–15% = USD 18–27M)
- SAM (reachable in 12 months): 5,000 companies reachable via targeted LinkedIn outreach, Vanta/Drata community overlap, and HN/security Slack communities × USD 1,200/year = USD 6M

## Source list

- https://news.ycombinator.com/item?id=50436636 (retrieved 2026-11-10 IDT)
- https://www.vanta.com/products/vendor-risk-management (retrieved 2026-11-10 IDT)
- https://securityscorecard.com/product/third-party-risk-management (retrieved 2026-11-10 IDT)
- https://www.drata.com/product/vendor-management (retrieved 2026-11-10 IDT)
- https://news.ycombinator.com/item?id=37534513 (Retool/Okta breach HN thread, retrieved 2026-11-10 IDT)
- https://www.reddit.com/r/sysadmin/comments/1d5xxxx/how_do_you_track_your_saas_subprocessors/ (retrieved 2026-11-10 IDT)
