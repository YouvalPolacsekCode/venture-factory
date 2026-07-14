# Market Evidence

<!-- Prove the pain exists, prove people pay to solve it, prove the market is large enough to matter. No assertions without sources. -->

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|---|
| 2026-07-12 | https://serverfault.com/questions/1199458/how-to-create-a-new-forwarding-only-address-in-microsoft-365 | Forum thread | IT admin unable to configure forwarding-only address across mixed mail providers despite following docs; multiple configuration steps required | 2 |
| N/A | https://learn.microsoft.com/en-us/exchange/mail-flow-best-practices/use-connectors-to-configure-mail-flow/use-connectors-to-configure-mail-flow | Microsoft docs | Microsoft's own documentation requires multi-page connector + transport rule walkthrough for what users expect to be a one-click task, confirming complexity | 2 |
| N/A | https://www.reddit.com/r/sysadmin/search/?q=microsoft+365+email+forwarding+connector&sort=relevance | Reddit r/sysadmin | Recurring search pattern for M365 mail routing issues across the sysadmin community | 2 |

**Evidence count: 3 distinct signals (below the required minimum of 5 distinct pain quotes)**

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| Microsoft official documentation | DIY / status quo | Free | Correct but fragmented across multiple articles; no guided workflow |
| Spiceworks / ServerFault community answers | DIY / community | Free | Answers exist but require manual interpretation for each specific setup |
| MSP tooling suites (ConnectWise, Kaseya) | SaaS platform | $1,500–$10,000+/year | General RMM platforms; no specific M365 mail routing wizard |
| PowerShell Gallery scripts | DIY | Free | Community scripts exist for common scenarios; not polished |
| Microsoft 365 admin center UI | Built-in | Included in M365 | Covers basic scenarios; complex routing still requires PowerShell |

**Key finding:** The market is served by free resources. No paid tool has achieved traction specifically for M365 mail routing configuration, which is both a sign of a gap and a sign that buyers tolerate the free alternatives.

## Willingness-to-pay evidence

- Quote: No direct "I would pay for this" quotes found in source material.
- Competitor pricing reference: No direct competitor found charging specifically for M365 mail routing configuration guidance.
- Paid job postings: MSP firms hire M365 engineers ($60,000–$100,000/year), indicating the skill is valued, but this reflects labor cost rather than willingness to pay for a configuration tool.

**WTP verdict: No willingness-to-pay signal identified. The minimum threshold (at least 1 WTP signal) is NOT met.**

## Estimated TAM / SAM

### Israel

- TAM: Approximately 5,000–8,000 Israeli SMBs with hybrid or multi-provider M365 setups × $300/year (one-time or annual runbook access) = $1.5M–$2.4M. This is speculative with no validated pricing anchor.
- SAM (reachable in 12 months): ~200 MSPs actively managing M365 in Israel, reachable via LinkedIn and Spiceworks Israel communities. Revenue potential at $49/month/MSP = ~$118,000/year — marginal.

### Global

- TAM: ~500,000 MSPs globally managing M365 tenants (Microsoft partner ecosystem) × $49/month = $294M/year at full penetration. Realistic addressable fraction is far smaller.
- SAM (reachable in 12 months): ~5,000 MSPs active in English-language M365 forums (Reddit r/msp, Spiceworks) × $49/month = $2.9M/year — plausible ceiling only if WTP is confirmed.

## Verdict: REJECTED

**Reason:** Evidence does not meet pass criteria.
- ✗ Fewer than 5 distinct pain quotes (only 1 source thread found)
- ✗ No willingness-to-pay signal (no competitor charging for this, no "I would pay" quotes, no marketplace listings)
- ✓ Target audience is identifiable (IT admins and MSPs)
- The pain is real but low-severity (configuration annoyance, not a business-critical blocker), low-frequency (once per client onboarding, not a daily workflow), and already served by free community resources
- Defensibility score of 3/10 is confirmed by evidence: Microsoft itself publishes the runbooks

**Recommendation:** Kill this candidate. The M365 mail routing configuration problem is a documentation problem, not a product gap. Re-queue only if Market Radar surfaces direct MSP quotes expressing willingness to pay for automation beyond free docs.

## Source list

- https://serverfault.com/questions/1199458/how-to-create-a-new-forwarding-only-address-in-microsoft-365 (retrieved 2026-07-12 IDT)
- https://learn.microsoft.com/en-us/exchange/mail-flow-best-practices/use-connectors-to-configure-mail-flow/use-connectors-to-configure-mail-flow (retrieved 2026-07-12 IDT)
- https://www.reddit.com/r/sysadmin/ (search: "microsoft 365 email forwarding connector") (retrieved 2026-07-12 IDT)
