# Market Evidence

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|---|
| 2026-07-29 | https://salesforce.stackexchange.com/questions/439706/server-side-validation-of-uploaded-files | StackExchange question | ISV developer explicitly states no established patterns exist for Apex server-side file validation on guest-user endpoints | 3 |
| N/A | https://appexchange.salesforce.com/appxStore | AppExchange directory | No dedicated security-validation toolkit listed for managed-package file upload hardening as of retrieval date | 2 |
| N/A | https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_classes_restful_http_rest.htm | Official docs | Salesforce Apex REST documentation contains no prescriptive file-upload validation patterns, confirming the documented gap | 2 |

**Evidence count: 3 distinct signals (minimum required for pass: 5). Bar not met.**

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| Salesforce Security Review consultants | Agency / consulting | USD 5,000–20,000 per engagement | Expensive, bespoke, no reusable code artefact; focuses on full Security Review submission not isolated file-validation |
| OWASP File Upload Cheat Sheet | DIY / documentation | Free | Generic guidance not Apex-specific; requires developer to translate manually |
| Salesforce Partner Community forums | DIY / peer advice | Free | Fragmented, no authoritative pattern; the candidate question itself shows the gap |

## Willingness-to-pay evidence

- **Competitor pricing reference:** Salesforce Security Review consulting firms (e.g., Appirio, Wipro Salesforce practice) charge USD 5,000–20,000 for full Security Review prep — but this covers the entire submission, not file-upload hardening specifically. No discrete pricing for file-validation tooling was found.
- **Quote:** No direct "I would pay for this" quote found in source material.
- **Paid job postings:** Zero job postings found specifically requesting Apex file-upload security expertise as a discrete deliverable.

**Willingness-to-pay signal: inferred only (cost avoidance of consultant engagement). No direct WTP evidence found. Bar not met.**

## Estimated TAM / SAM

### Israel
- Estimated Israeli Salesforce ISV / AppExchange partner firms: ~15–30 (based on Salesforce partner directory filtering)
- Realistic ACV for a code-template / audit pack: USD 149–499 one-time
- TAM Israel: ~25 orgs × USD 300 avg = **USD 7,500** — too small to matter
- SAM (reachable in 12 months): ~10 firms × USD 300 = **USD 3,000**

### Global
- Active AppExchange managed-package ISVs (those with guest-user file upload use cases): estimated ~200–500 globally (conservative, based on AppExchange directory scale and ISV partner programme size)
- TAM Global: 350 orgs × USD 300 = **USD 105,000**
- SAM (reachable in 12 months via Salesforce Partner Community, Trailblazer forums, ISV Slack): ~100 orgs × USD 300 = **USD 30,000**

**TAM is too small to justify a dedicated experiment. Even at optimistic conversion, annual revenue ceiling is under USD 50K.**

## Verdict

**REJECTED — FAIL**

Reasons:
1. Only 1 primary pain signal discovered; minimum threshold is 5 distinct quotes/signals.
2. No direct willingness-to-pay evidence — inferred cost avoidance only.
3. Global TAM estimated at ~USD 100K; addressable in 12 months ~USD 30K. Not a viable standalone business.
4. Founder-fit score of 3/10 (lowest dimension) further reduces expected execution quality.

Recommendation: Do not promote to experiments/. If Salesforce security emerges as a recurring theme across multiple candidate cycles with stronger signal volume, revisit as a content/SEO play rather than a productised service.

## Source list

- https://salesforce.stackexchange.com/questions/439706/server-side-validation-of-uploaded-files (retrieved 2026-07-29 IDT)
- https://appexchange.salesforce.com/appxStore (retrieved 2026-07-29 IDT)
- https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_classes_restful_http_rest.htm (retrieved 2026-07-29 IDT)
- https://owasp.org/www-community/vulnerabilities/Unrestricted_File_Upload (background reading, retrieved 2026-07-29 IDT)
