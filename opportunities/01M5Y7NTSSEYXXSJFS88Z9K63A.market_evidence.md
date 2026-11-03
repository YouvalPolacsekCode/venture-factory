# Market Evidence

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|---|
| 2026-10-27 | https://dev.to/james_anderson_h/security-changed-with-ai-and-small-teams-are-falling-behind-5ebg | Editorial article with comments | Score 30, 36 comments on dev.to; practitioner audience engaging with the speed-asymmetry framing between AI-aided attackers and small defending teams | 3 |
| 2026-10-27 | https://snyk.io/plans/ | Competitor pricing page | Snyk charges $25–$98/dev/month for vulnerability scanning; SMB tier exists confirming willingness to pay in this category | 4 |
| 2026-10-27 | https://www.wiz.io/pricing | Competitor pricing page | Wiz targets startups with a dedicated tier; confirms paid market exists for security tooling at this segment | 3 |
| 2026-10-27 | https://semgrep.dev/pricing | Competitor pricing page | Semgrep Team plan ~$40/dev/month; open-source free tier also exists, showing price sensitivity alongside willingness to pay | 3 |

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| Snyk | SaaS | $25–$98/dev/month | Full integration required; too complex for teams with no security function; requires authenticated repo access |
| Wiz | SaaS | Custom enterprise pricing | Built for cloud infrastructure; onboarding complexity is high for a 2–10 person eng team |
| Semgrep | SaaS / OSS | Free–$40/dev/month | Requires developer time to tune rules; not a managed digest/report |
| GitHub Dependabot | Built-in tool | Free | Only covers dependency vulnerabilities; no CVE feed synthesis or prioritization |
| Free CVE newsletters (e.g., SANS NewsBites) | Newsletter | Free | Generic; not stack-specific; no action items tied to your codebase |

## Willingness-to-pay evidence

- Competitor pricing reference: Snyk Team plan, $25–$98/developer/month — https://snyk.io/plans/
- Competitor pricing reference: Semgrep Team, ~$40/developer/month — https://semgrep.dev/pricing
- Paid job postings: DevSecOps and security engineering roles at startups are common on LinkedIn and AngelList, but these represent hiring budget, not tooling spend directly.
- No direct "I'd pay for X" quote is available in the discoverable snippet or surrounding context. This is a key gap for passing pain validation.

## Estimated TAM / SAM

### Israel

- TAM: ~5,000 Israeli startups and SMBs with 2–50 person eng teams × $600/year digest service = USD 3M (rough ceiling)
- SAM (reachable in 12 months): ~500 CTOs reachable via LinkedIn + AngelList outreach × $600 = USD 300K

### Global

- TAM: ~500,000 startups globally with 2–50 person eng teams × $600/year = USD 300M (addressable for full security tooling; weekly digest captures a small slice)
- SAM (reachable in 12 months): Realistically 2,000–5,000 paying customers at $49/month = USD 1.2M–$2.9M ARR ceiling for digest format

## Source list

- https://dev.to/james_anderson_h/security-changed-with-ai-and-small-teams-are-falling-behind-5ebg (retrieved 2026-10-27 IDT)
- https://snyk.io/plans/ (retrieved 2026-10-27 IDT)
- https://www.wiz.io/pricing (retrieved 2026-10-27 IDT)
- https://semgrep.dev/pricing (retrieved 2026-10-27 IDT)

## Verdict: FAIL

**Reason:** Does not meet minimum evidence bar. Fewer than 5 distinct pain quotes from independent sources. The willingness-to-pay signal is indirect (competitor pricing, not prospect quotes or workaround spend). The factory-buildable variant (weekly digest) competes directly against free alternatives (Dependabot, SANS newsletters) without a proven differentiation. Build-gate failures on buildability_with_ai (5/10) and operational_autonomy (4/10) mean the real product is out of scope. Recommend killing this candidate. If revisited, requires 5+ direct pain quotes and a demonstrated gap between free CVE tooling and what paying customers actually need at the digest format level.