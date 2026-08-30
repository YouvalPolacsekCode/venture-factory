# Market Evidence

<!-- Prove the pain exists, prove people pay to solve it, prove the market is large enough to matter. No assertions without sources. -->

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|
| 2026-08-28 | https://webmasters.stackexchange.com/questions/148877/how-can-i-get-my-domain-into-google-postmaster-tools | Forum post | Solo operator unable to add sending subdomain to Google Postmaster Tools despite correct DNS records; reports consistent multi-day failure with no support path | 2 |

**Evidence gap:** Only 1 source found. Validation threshold requires ≥5 distinct pain quotes from independent sources. No additional corroborating threads, Reddit posts, HN discussions, or job listings were available in the opportunity data. Web fetch of adjacent sources would be required before this could pass, and even then the one-time-fix nature of most GPT onboarding issues limits recurrence evidence.

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| GlockApps | SaaS deliverability monitor | $9–$99/mo | Does not specifically help with GPT domain verification failures; focuses on inbox placement testing |
| MxToolbox | SaaS / freemium DNS & email diagnostics | Free–$129/mo | Generic DNS checker; no GPT-specific onboarding guidance |
| Postmark / SendGrid | Managed email sending | $10–$300+/mo | Solves sending infrastructure but does not resolve GPT setup for custom domains; often still requires GPT verification |
| Email deliverability consultants (freelance) | Agency / freelance | $50–$200/hr | Exist on Upwork/Fiverr; indicates some willingness to pay but also that supply already meets demand for one-time fixes |
| Status quo: Google's own docs + trial and error | DIY | $0 | No cost but high time cost; GPT UI is notoriously opaque for subdomain verification |

## Willingness-to-pay evidence

- **Quote:** No direct willingness-to-pay quotes found in available evidence. The source post does not mention budget or prior spend on this problem.
- **Competitor pricing reference:** Freelance deliverability consultants on Upwork charge $50–200/hr for email setup work (general knowledge; no specific URL in candidate data). This suggests some operators pay for help, but it is not specific to GPT onboarding.
- **Paid job postings:** None identified in candidate data.

**Assessment:** Willingness-to-pay evidence is circumstantial at best. The existence of freelance deliverability work is weak proxy evidence. No direct quote, no competitor pricing page specific to GPT setup services, and no job listing targeting this problem were available.

## Estimated TAM / SAM

### Israel
- TAM: ~15,000 Israeli SaaS founders and small-business operators managing own email infrastructure × $99/yr (one-time setup fee amortized) ≈ **USD 1.5M** — but this is speculative; GPT setup is a one-time event for most operators, not recurring.
- SAM (reachable in 12 months): ~1,500 operators actively experiencing deliverability issues and searching for help ≈ **USD 150K** theoretical, likely much less given the infrequency of the specific GPT subdomain failure.

### Global
- TAM: ~2M self-hosted / self-managed email senders globally × $99 one-time ≈ **USD 198M** addressable in theory — but again, GPT setup is a one-time fix for most; recurring revenue opportunity is very limited without pivoting to ongoing monitoring.
- SAM (reachable in 12 months): ~20,000 operators actively hitting GPT verification failures and willing to pay ≈ **USD 2M** one-time, or ~5,000 operators on a $19/mo monitoring plan ≈ **USD 1.1M ARR** — optimistic given thin evidence of recurrence demand.

## Source list

- https://webmasters.stackexchange.com/questions/148877/how-can-i-get-my-domain-into-google-postmaster-tools (retrieved 2026-08-28 IDT)

---

## Verdict: **FAIL**

**Reason:** Evidence does not meet the pass bar. Required: ≥5 distinct pain quotes from independent sources, ≥1 clear willingness-to-pay signal. Found: 1 source, 0 direct WTP signals. The pain is real but the market signal is too thin to justify promotion. Additionally, the one-time-fix nature of GPT onboarding undermines recurring revenue potential, which was already flagged in scoring.

**Recommendation:** Re-queue for Market Radar with broader search query targeting Reddit (r/email, r/selfhosted, r/emailmarketing), HN, and IndieHackers threads mentioning Google Postmaster Tools failures. If ≥5 corroborating sources are found in the next cycle, re-score willingness-to-pay before promoting.
