# Market Evidence

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|---|
| 2026-10-17 | https://serverfault.com/questions/1200039/self-hosted-mail-server-not-reaching-some-recipients | Forum thread | Operator running Postfix+Dovecot for years still hits UCEPROTECT L3 blocklist despite clean DMARC/DKIM/SPF/rDNS | 2 |

**Evidence gap:** Only one primary source was available. The required minimum of 5 distinct pain quotes from separate sources was not met. Adjacent evidence (UCEPROTECT complaints across Reddit r/selfhosted, ServerFault, Hacker News) is widely known to exist anecdotally, but no additional URLs were surfaced in the candidate data and web_fetch was not invoked in this run.

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| MXToolbox | Free SaaS / paid tiers | $0–$129/mo | Covers blocklist lookup but no remediation guidance; free tier widely used by this segment |
| mail-tester.com | Free tool | $0 | Spam-score snapshot only; no monitoring or ongoing alerts |
| UCEPROTECT express delisting | Paid remediation | $299 one-time | Operator pays directly to UCEPROTECT; outside any third-party tool's control |
| Mailgun / SendGrid / Postmark | Managed SMTP SaaS | $15–$90+/mo | Full deliverability outsourcing; the self-hosting segment explicitly avoids these for cost/privacy reasons |
| GlockApps | Paid monitoring SaaS | $9–$79/mo | Covers inbox placement and blocklists; closest existing competitor |

## Willingness-to-pay evidence

- **Structural contradiction:** The self-hosting segment chose self-hosting to *avoid* paying for managed email. This creates a ceiling on price tolerance for any third-party tool targeting this audience.
- **Competitor pricing reference:** GlockApps charges $9–$79/mo for deliverability monitoring — market evidence that *some* operators pay, but GlockApps targets marketers and high-volume senders, not the niche self-hoster segment.
- **UCEPROTECT L3 remediation:** The only actionable remediation path (ISP-level IP range reputation improvement or $299 express delisting paid to UCEPROTECT) is outside the scope of any monitoring product, limiting the product's value proposition to diagnosis only.
- **No direct willingness-to-pay quotes** found in the available source material.

## Estimated TAM / SAM

### Israel
- TAM: Small — Israel has an estimated 2,000–5,000 VPS/dedicated server operators running self-hosted mail; at a realistic $9/mo ACV that is a ~$220K–$540K annual ceiling.
- SAM (reachable in 12 months): <500 active self-hosters reachable via local tech forums and LinkedIn; ~$54K/yr.

### Global
- TAM: Estimated 200,000–500,000 active self-hosted mail server operators globally (Postfix/Dovecot install base proxies) × $9/mo = ~$21M–$54M/yr ceiling, but realistic conversion rate among a cost-sensitive, free-tools-preferring segment is very low (<1%).
- SAM (reachable in 12 months): ~5,000 operators reachable via ServerFault, r/selfhosted, HN; ~$540K/yr at 1% conversion.

## Source list

- https://serverfault.com/questions/1200039/self-hosted-mail-server-not-reaching-some-recipients (retrieved 2026-10-17 IDT)

---

**Verdict: REJECTED.** Evidence count below threshold (1 source, 0 direct WTP quotes). Structural willingness-to-pay contradiction: the audience self-selects against paying for managed services. Actual remediation (the high-value action) is outside product control. Recommend killing this candidate; do not re-queue unless Market Radar surfaces at least 5 independent threads with explicit WTP signals.
