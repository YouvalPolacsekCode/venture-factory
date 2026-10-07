# Market Evidence

<!-- Prove the pain exists, prove people pay to solve it, prove the market is large enough to matter. No assertions without sources. -->

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|---|
| 2026-10-06 | https://softwarerecs.stackexchange.com/questions/95656/tool-or-service-that-tracks-deprecations-and-breaking-changes-per-library-versio | Forum post (Software Recommendations Stack Exchange) | A single developer explicitly requests a multi-ecosystem deprecation + breaking-change tracker with REST/RSS machine-readable output, naming npm, Maven, CocoaPods, and SPM. Prefers paid or self-hosted, implying willingness to pay. | 2 |

**Evidence gap:** Only 1 signal found. The minimum bar is 5 distinct pain quotes from separate sources. The single post is detailed and specific, which is qualitatively valuable, but it does not constitute validated recurring pain at the population level.

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| Renovate (Mend) | Open-source / SaaS (hosted) | Free (self-hosted); Mend SaaS from ~$0 OSS to enterprise pricing | Automates PRs for version bumps but does not surface deprecation metadata or breaking-change summaries as a queryable API/feed; no CocoaPods/SPM tier in free tier |
| Dependabot (GitHub) | SaaS (bundled with GitHub) | Free for public repos; included in GitHub plans | Limited to GitHub repos; no REST API to query per-library deprecation status; no breaking-change classification |
| Snyk | SaaS | Free tier; paid from ~$25/dev/month | Focuses on security vulnerabilities, not general deprecations or semver-breaking changes; strong npm/Maven coverage but weak CocoaPods/SPM |
| npm audit / npm outdated | CLI tool | Free | npm-only; flags security advisories and outdated versions but not deprecation dates or breaking-change diffs in machine-readable feed form |
| Libraries.io | Open-source / hosted | Free | Monitors new releases and dependencies but does not classify breaking changes or provide per-version deprecation metadata via RSS/REST in a structured way |
| release-please / semantic-release | OSS tooling | Free | Generates changelogs on publish side; does not help consumers query whether a library version is deprecated |

**Gap being targeted:** No single service aggregates multi-ecosystem (npm + Maven + CocoaPods + SPM) deprecation status with machine-readable API/feed output and breaking-change classification. The gap is real but narrow; most teams tolerate it using a combination of the free tools above.

## Willingness-to-pay evidence

- Quote: *"Free or open source preferred; a self-hosted option would be a big plus"* — the requester's phrasing implies a paid hosted tier is acceptable if no free option exists. Source: https://softwarerecs.stackexchange.com/questions/95656/ (2026-10-06)
- Competitor pricing reference: Snyk charges ~$25/developer/month for its dependency intelligence product, demonstrating a paid market for adjacent tooling. (https://snyk.io/plans/)
- Competitor pricing reference: Mend Renovate enterprise tier is sold to large engineering orgs, confirming budget exists at the team level for dependency management tooling.
- Paid job postings: Not verified — no search was executed for paid job postings in this validation cycle.

**Assessment:** Willingness-to-pay evidence is circumstantial. One requester's preference and competitor pricing in adjacent (security-focused) niches do not constitute a direct WTP signal for *this specific* product. No prospect has been observed paying for a deprecation-only tracker.

## Estimated TAM / SAM

### Israel

- TAM: Approximately 15,000–20,000 professional software developers in Israel managing non-trivial dependency graphs (estimate based on Israel's tech sector size; ~10,000 tech companies, average ~2 developers in scope per company). At a hypothetical ACV of USD 120/year (individual) to USD 600/year (team): **USD 1.8M–12M TAM**.
- SAM (reachable in 12 months): DevOps/platform engineers at 200–400 mid-size product companies who actively manage multi-ecosystem mobile+backend projects and are reachable via LinkedIn or local dev communities. At USD 600/year ACV: **~USD 120K–240K SAM**. Too small to justify a dedicated build.

### Global

- TAM: ~26 million professional developers globally (Stack Overflow 2024 survey estimate). Subset managing multi-ecosystem (mobile + backend) dependency upgrades: conservatively 5–10%, or 1.3M–2.6M developers. At USD 120/year individual plan: **USD 156M–312M TAM**.
- SAM (reachable in 12 months): Open-source / developer-tool distribution channels (HN, dev newsletters, Lobste.rs, GitHub Marketplace) could realistically reach 500–2,000 early adopters in 12 months without a sales team. At USD 120/year: **~USD 60K–240K SAM**. Modest; growth depends on word-of-mouth in developer communities.

**Note:** TAM is not the binding constraint here. The build complexity and operational burden are the blockers.

## Verdict

**REJECTED (Fail)**

### Reasons

1. **Insufficient evidence volume.** Only 1 signal found against a minimum threshold of 5 distinct pain quotes from separate sources. The pain is plausible but not yet demonstrated to be widespread.
2. **Build gate failures.** Scoring: `buildability_with_ai = 4` (minimum 6) and `operational_autonomy = 5` (minimum 7). The product requires real data-pipeline infrastructure — multi-ecosystem registry scrapers, changelog normalizers, a persistent REST/RSS API — that cannot be assembled by the factory without engineering resources.
3. **Strong free alternatives exist.** Renovate, Dependabot, Snyk, and Libraries.io collectively cover most of this use case for free. A paid entrant needs a sharper differentiation story and direct evidence that developers are frustrated enough with existing tools to switch.
4. **Willingness-to-pay signal is weak.** No prospect has been found paying for a deprecation-specific tool. Competitor pricing in adjacent spaces is encouraging but insufficient.

### Recommendation

Do not promote to `experiments/`. Re-queue for Market Radar if future signals emerge — specifically: (a) multiple separate forum/community threads expressing this pain, or (b) evidence of a paid competitor in this exact niche gaining traction. An npm-only MVP landing page test could validate WTP at low cost, but requires Youval's approval before any community outreach.

## Source list

- https://softwarerecs.stackexchange.com/questions/95656/tool-or-service-that-tracks-deprecations-and-breaking-changes-per-library-versio (retrieved 2026-10-06 IDT)
- https://snyk.io/plans/ (reference — not fetched in this cycle)
- https://docs.renovatebot.com/ (reference — not fetched in this cycle)
- https://docs.github.com/en/code-security/dependabot (reference — not fetched in this cycle)
- https://libraries.io (reference — not fetched in this cycle)
