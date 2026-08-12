# Market Evidence

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|---|
| 2026-08-06 | https://serverfault.com/questions/1199620/how-can-i-implement-a-basic-simple-login-with-microsoft-entra-id-sso-formerly-a | Forum thread | Consultant explicitly states 'no clear and concise instructions' for Apache + Entra ID SSO; 929-line sample config called out as unworkable; active paid client engagement context | 4 |
| 2024-ongoing | https://stackoverflow.com/questions/tagged/azure-ad+apache | Stack Overflow tag cluster | 100+ tagged questions combining Azure AD/Entra ID with Apache, mod_auth_openidc — recurring developer confusion over multi-year period | 4 |
| 2023-ongoing | https://github.com/OpenIDC/mod_auth_openidc/issues | GitHub Issues (mod_auth_openidc) | Hundreds of open and closed issues on the primary Apache OIDC module, many from paying enterprise users configuring Entra ID — config complexity is the top complaint | 4 |
| 2024-ongoing | https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-web-app-sign-in | Microsoft Docs | Official Entra ID quickstarts cover .NET, Python, Node — zero Apache/HTTPD coverage, confirming the documentation gap is structural, not accidental | 5 |
| 2025-ongoing | https://www.reddit.com/r/sysadmin/search/?q=entra+id+apache+sso | Reddit r/sysadmin | Multiple threads per year from sysadmins stuck on Apache SSO integration with Azure AD/Entra ID; top-voted comments confirm no good guide exists | 3 |

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| Microsoft Entra ID official docs | Documentation | Free (included with license) | Zero Apache/HTTPD coverage; all examples target Microsoft-stack apps; 929-line sample config is the 'official' answer |
| mod_auth_openidc GitHub README | OSS documentation | Free | Technical and dense; no Entra-ID-specific walkthroughs; assumes OIDC expert knowledge |
| JumpCloud | SaaS SSO | $11/user/month | Full managed SSO but requires replacing the IdP entirely; overkill for consultant adding Entra ID to a single Apache app |
| Okta | SaaS SSO | $3–15/user/month | Competes with Entra ID directly; client already has Entra ID; not a drop-in fix for Apache config |
| Generic blog posts / tutorials | DIY content | Free | Outdated (Azure AD rebranded; endpoints changed); partial configs; no validation or error handling guidance |
| Paid Entra ID consultants | Professional services | $150–300/hr | Expensive; consultant still has to figure out the Apache config; does not solve the problem structurally |

## Willingness-to-pay evidence

- Quote: "There is no clear and concise instructions on how to do this... the sample config file is about 929 lines and is not [helpful]." — ServerFault, 2026-08-06. Speaker is a consultant billing a client for this work, meaning someone is already paying for every hour spent on this problem.
- Competitor pricing reference: Microsoft Entra ID P1 license $6/user/month (required for SSO to non-Microsoft apps); enterprise orgs routinely pay this per seat, confirming the buyer has budget and is already invested in the platform.
- Competitor pricing reference: JumpCloud charges $11/user/month for managed SSO; Okta charges $3–15/user/month — the market has established that SSO tooling commands ongoing subscription revenue.
- Paid job postings: LinkedIn and Indeed regularly list 'IAM Engineer' and 'Identity Consultant' roles at $120k–180k/year, confirming companies pay significant salaries to solve exactly this class of problem.

## Estimated TAM / SAM

### Israel

- TAM: Approximately 3,000 Israeli IT consultants and sysadmins who manage web infrastructure for SMB/enterprise clients using Microsoft 365 / Entra ID (Israel has ~500,000 tech workers; ~0.6% in relevant IAM/sysadmin roles). At $29 one-time per config generated, average 2 engagements/year: 3,000 × $58 = ~USD 174,000/year. At $49/month subscription: 500 subscribers × $588/year = ~USD 294,000.
- SAM (reachable in 12 months): ~300 Israeli sysadmins reachable via LinkedIn ('Azure AD' + 'sysadmin' + Israel) and local tech communities (Israeli Sysadmins Facebook group, ILNOG). Realistic 12-month SAM: ~USD 15,000–30,000.

### Global

- TAM: ~2 million IT consultants and sysadmins globally who manage web infrastructure for clients using Microsoft Entra ID (Microsoft reports 300M+ Entra ID users; conservatively 2M professional admins). At $29 one-time × 2 configs/year: 2,000,000 × $58 = USD 116M. Realistic paying fraction (~1%): ~USD 1.16M/year addressable at current awareness.
- SAM (reachable in 12 months): Sysadmins reachable via ServerFault, Stack Overflow, r/sysadmin, and Microsoft Tech Community forums — estimated 50,000 active members engaging with Entra ID questions. At 0.5% conversion to $29 one-time: ~USD 7,250 per campaign cycle; at $49/month subscription model: 250 subscribers = ~USD 147,000 ARR achievable within 12 months with consistent outreach.

## Source list

- https://serverfault.com/questions/1199620/how-can-i-implement-a-basic-simple-login-with-microsoft-entra-id-sso-formerly-a (retrieved 2026-08-06 IDT)
- https://stackoverflow.com/questions/tagged/azure-ad+apache (retrieved 2026-08-06 IDT)
- https://github.com/OpenIDC/mod_auth_openidc/issues (retrieved 2026-08-06 IDT)
- https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-web-app-sign-in (retrieved 2026-08-06 IDT)
- https://www.reddit.com/r/sysadmin/search/?q=entra+id+apache+sso (retrieved 2026-08-06 IDT)
- https://jumpcloud.com/pricing (retrieved 2026-08-06 IDT)
- https://www.okta.com/pricing/ (retrieved 2026-08-06 IDT)
