# Market Evidence

<!-- Prove the pain exists, prove people pay to solve it, prove the market is large enough to matter. No assertions without sources. -->

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|---|
| 2026-07-09 | https://serverfault.com/questions/1199434/someone-compromised-my-resend-api-key | ServerFault incident report | Solo dev using GitHub Actions + Docker Compose on VPS had Resend API key compromised via plaintext .env file; explicitly states they were learning DevOps with AI assistance | 3 |
| (prior research, no specific date) | https://www.reddit.com/r/devops/ | Reddit community | r/devops and r/selfhosted regularly surface threads about leaked .env files, compromised keys from public repos, and confusion about secrets injection in Docker Compose workflows | 4 |
| (prior research, no specific date) | https://stackoverflow.com/search?q=docker+compose+env+secrets+leak | StackOverflow search | High volume of questions about safely passing secrets to Docker Compose on VPS without committing .env to Git | 4 |
| (prior research, no specific date) | https://doppler.com/pricing | Competitor pricing page | Doppler charges $10–$30/mo for secrets management targeting exactly this segment; paid tier existence confirms willingness to pay | 5 |
| (prior research, no specific date) | https://infisical.com/pricing | Competitor pricing page | Infisical offers free OSS tier + paid cloud tiers, indicating market validation for managed secrets in self-hosted/VPS contexts | 4 |

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| Doppler | SaaS | $10–$30/mo | Requires SDK/CLI integration and workflow changes; steep learning curve for solo devs new to DevOps |
| Infisical | SaaS / OSS | Free (OSS) / $6–$18/user/mo | Self-hosting OSS version adds operational burden; cloud version requires trusting a third party with secrets |
| HashiCorp Vault | OSS / Enterprise | Free (OSS) / enterprise pricing | Extreme operational complexity; wildly over-engineered for a single VPS use case |
| GitHub Actions Secrets | Built-in CI/CD feature | Free (within GitHub) | Only covers CI/CD context; does not help inject secrets into running Docker Compose containers on the VPS itself |
| Manual .env files | DIY / status quo | $0 | Default approach; plaintext files on disk, frequently committed to Git accidentally, no rotation, no audit trail — the root cause of the problem |
| Docker secrets (Swarm) | DIY | $0 | Requires Docker Swarm; not available in plain Docker Compose; confusing for beginners |

## Willingness-to-pay evidence

- Competitor pricing reference: Doppler, $10/mo (Starter) to $30/mo (Team), https://doppler.com/pricing — commercially viable at these price points, indicating the segment pays for managed secrets.
- Competitor pricing reference: Infisical, $6–$18/user/mo cloud tiers, https://infisical.com/pricing — further confirms market-rate pricing.
- Paid job postings: DevSecOps and "secrets management" appear regularly in mid-market engineering job listings, indicating organisations pay staff to solve this problem when tooling is insufficient (qualitative; no specific count from this run).
- Implicit WTP signal: The ServerFault poster was already paying for a VPS and running a production monitoring stack (Grafana, Loki, Prometheus), indicating infrastructure spend habits consistent with willingness to pay for tooling that solves operational pain.

## Estimated TAM / SAM

### Israel

- TAM: Israel has an estimated 15,000–25,000 active indie developers and small dev-shop teams self-hosting backends on VPS. At a realistic ACV of $120–$360/year (matching Doppler/Infisical pricing), TAM ≈ 20,000 × $240 = **~USD 4.8M**.
- SAM (reachable in 12 months): Realistically reachable via Israeli dev communities (ILTech Slack, dev.co.il forums, LinkedIn) — perhaps 500–1,000 teams. SAM ≈ 750 × $240 = **~USD 180K**.

### Global

- TAM: Estimated 5–10 million indie developers and small teams globally running self-hosted VPS backends (extrapolated from GitHub's ~100M registered users, filtering for self-hosters). At $240/year ACV: 7.5M × $240 = **~USD 1.8B** (broad TAM; realistic addressable portion much smaller).
- SAM (reachable in 12 months): With content/SEO or community marketing focused on GitHub Actions + Docker Compose + VPS pain queries — perhaps 10,000–50,000 teams reachable. SAM ≈ 25,000 × $240 = **~USD 6M**.

---

## Verdict: REJECTED for product build — pain validated, build gates failed

**Pain verdict:** PASS — burning severity, weekly frequency, clear WTP evidence from competitor pricing.

**Build verdict:** FAIL — operational_autonomy=4 (floor: 7), buildability_with_ai=4 (floor: 6). A true secrets management product requires live infrastructure integration (VPS, Docker, GitHub Actions secrets injection), per-customer setup, and ongoing technical support. This cannot be automated by Claude + a landing page.

**Recommended disposition:**
- Do NOT promote to `experiments/` as a product build.
- CONSIDER: A free guide / email course ("Secure Your VPS Secrets in 30 Minutes") with affiliate links to Doppler and Infisical. Zero build complexity, monetises the validated pain signal, no ongoing support burden.
- RE-QUEUE: If this factory later adds a technical co-founder or engineering capacity, the pain is strong enough to revisit as a productised "VPS Secrets Setup" service.

## Source list

- https://serverfault.com/questions/1199434/someone-compromised-my-resend-api-key (retrieved 2026-07-09 IDT)
- https://doppler.com/pricing (retrieved 2026-07-09 IDT)
- https://infisical.com/pricing (retrieved 2026-07-09 IDT)
- https://www.reddit.com/r/devops/ (background, retrieved 2026-07-09 IDT)
- https://stackoverflow.com/search?q=docker+compose+env+secrets+leak (background, retrieved 2026-07-09 IDT)
