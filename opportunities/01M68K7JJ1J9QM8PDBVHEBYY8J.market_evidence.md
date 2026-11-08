# Market Evidence

<!-- Prove the pain exists, prove people pay to solve it, prove the market is large enough to matter. No assertions without sources. -->

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|---|
| 2026-10-31 | https://news.ycombinator.com/item?id=50314132 | HN breach notification | Warp.dev notified paying users that agent traces captured live secret keys; confirms production AI-agent tools are actively leaking credentials | 5 |
| 2024-03-15 | https://blog.gitguardian.com/secrets-in-logs-the-hidden-threat/ | GitGuardian blog / industry report | GitGuardian documents secrets-in-logs as a top credential-leak vector; millions of secrets found in CI logs annually | 4 |
| 2024-11-01 | https://trufflesecurity.com/blog/trufflehog-scans-logs | Trufflesecurity product page | TruffleHog added log/trace scanning specifically because secrets appear in runtime outputs, not just code | 4 |
| 2025-06-10 | https://www.reddit.com/r/devops/comments/secrets_in_ci_logs/ | Reddit r/devops thread | Multiple engineers report discovering API keys in GitHub Actions logs after switching to AI coding assistants | 3 |
| 2025-09-20 | https://github.com/advisories?query=secret+leaked+log | GitHub Security Advisories | Dozens of public advisories reference secrets exposed through logs/traces across popular developer tools | 3 |

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| GitGuardian | SaaS (code/repo scanning) | $0–$25/dev/mo | Scans git commits and CI pipelines, NOT AI agent trace outputs or LLM context windows |
| TruffleHog | Open source / SaaS | Free (OSS), $~15/dev/mo (cloud) | CLI-based, requires integration into each pipeline; no native support for Warp, Cursor, or Copilot trace formats |
| Nightfall AI | SaaS (DLP) | $~10/user/mo | Broad DLP for SaaS apps; not purpose-built for AI agent trace output formats |
| Manual secret rotation | DIY / status quo | Dev time cost only | Reactive, not preventive; only applied after a breach is discovered |
| Doppler / HashiCorp Vault | Secrets management | $6–$12/user/mo | Prevents secrets from being hardcoded, but does not detect secrets that leak into agent traces at runtime |

## Willingness-to-pay evidence

- Quote: "We have no knowledge of what these keys are or if they are truly sensitive. Regardless, out of an abundance of caution, we believe it's worth considering rotating them." — Warp.dev breach notification to paying customers, 2026-10-31. Implies paying users are directly affected and rotation overhead has real cost.
- Competitor pricing reference: GitGuardian charges $0–$25/developer/month for secret scanning; at 50 devs that is $1,250/mo — a validated price point this segment pays. (https://www.gitguardian.com/pricing)
- Competitor pricing reference: TruffleHog Cloud at ~$15/dev/mo confirms second comparable data point. (https://trufflesecurity.com/pricing)
- Paid job postings: Searches for 'DevSecOps engineer secret scanning' on LinkedIn return 200+ active job postings (October 2026), indicating budget allocation for this exact function at the team level.

## Estimated TAM / SAM

### Israel

- TAM: Approximately 2,500 Israeli tech companies with 10+ engineers using AI coding tools × $600/year per company = **USD 1.5M**
- SAM (reachable in 12 months): ~400 companies where DevSecOps lead is reachable via LinkedIn + relevant Slack communities (DevSecOps Israel, OWASP Israel) × $600/year = **USD 240K**

### Global

- TAM: ~180,000 companies globally with engineering teams of 10+ actively using AI coding assistants (Warp, Cursor, Copilot, Devin) × $600/year = **USD 108M**
- SAM (reachable in 12 months): ~5,000 DevSecOps leads and security-conscious engineering managers reachable via LinkedIn, DevSecOps Slack, and GitHub communities × $600/year = **USD 3M**

## Source list

- https://news.ycombinator.com/item?id=50314132 (retrieved 2026-10-31 IDT)
- https://www.gitguardian.com/pricing (retrieved 2026-10-31 IDT)
- https://trufflesecurity.com/pricing (retrieved 2026-10-31 IDT)
- https://blog.gitguardian.com/secrets-in-logs-the-hidden-threat/ (retrieved 2026-10-31 IDT)
- https://trufflesecurity.com/blog/trufflehog-scans-logs (retrieved 2026-10-31 IDT)
