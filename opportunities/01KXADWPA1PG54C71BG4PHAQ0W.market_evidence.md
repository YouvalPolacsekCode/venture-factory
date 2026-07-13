# Market Evidence

<!-- Opportunity: 01KXADWPA1PG54C71BG4PHAQ0W -->
<!-- Verdict: FAIL — insufficient distinct pain signals and no WTP evidence from primary sources -->

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|---|
| 2026-07-12 | https://salesforce.stackexchange.com/questions/439629/deploying-a-profile-via-metadata-api-with-debug-apex-enabled-but-modify-all-data | Forum question | Admin asking whether Metadata API enforces the same permission cascade as Setup UI — describes real compliance risk when deploying Profiles with Debug Apex enabled | 2 |

**Evidence gap:** Only 1 distinct source reached the validation pipeline. The pain_validation threshold requires ≥5 distinct pain quotes from ≥2 sources. No competitor pricing pages, no paid-workaround signals, no community upvotes or reply count data were available from the supplied inputs.

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| Strongpoint (now part of Fastpath) | SaaS governance tool | ~$15,000–$50,000/year enterprise | Broad Salesforce audit suite; permission dependency graph is a subset feature, not purpose-built |
| OwnBackup / OwnData | SaaS backup + governance | ~$10,000+/year | Focuses on data backup and change tracking, not pre-deployment permission cascade simulation |
| Manual XML diff + Salesforce CLI | DIY | Free (labor cost) | Requires deep Metadata API expertise; error-prone; no automated cascade modeling |
| Copado / Gearset | DevOps SaaS | $1,500–$6,000+/year | CI/CD pipeline management; permission cascade validation is not a primary feature |

**Note:** Gap analysis is based on known market participants as of mid-2026. No pricing pages were fetched in this cycle due to single-source input.

## Willingness-to-pay evidence

- Quote: *(None retrieved — the sole source is an unanswered forum question with no community engagement data provided.)*
- Competitor pricing reference: Strongpoint/Fastpath and OwnBackup operate at enterprise price points ($10k–$50k/year), indicating willingness to pay exists at the category level — but this is indirect inference, not primary WTP evidence for this specific pain point.
- Paid job postings: *(Not retrieved in this cycle.)*

**WTP verdict:** Category-level inference only. No direct quote, no "is there a tool that does X" signal, no paid workaround evidence surfaced from available inputs. Does not satisfy the ≥1 WTP signal threshold.

## Estimated TAM / SAM

### Israel

- TAM: Estimated ~500–800 Israeli companies running Salesforce at enterprise scale (50+ users, compliance-sensitive). At a hypothetical $600/year audit tool: ~$300k–$480k TAM. Too small to justify standalone investment without global rollout.
- SAM (reachable in 12 months): ~50–100 reachable via Trailblazer Community + LinkedIn outreach (requires approval before any contact).

### Global

- TAM: Salesforce reports ~150,000 enterprise customers globally. Subset with DevOps/CI-CD workflows and compliance requirements estimated at ~15,000–25,000. At $600/year: ~$9M–$15M TAM for a focused permission audit tool.
- SAM (reachable in 12 months): ~500–1,000 via Salesforce Stack Exchange, Trailblazer Community, and LinkedIn DevOps/admin groups — all outreach requires operator approval.

## Verdict

**FAIL — Do not promote to experiments/ this cycle.**

Reasons:
1. Only 1 distinct pain source (threshold: ≥5 quotes from distinct sources).
2. Zero primary willingness-to-pay signals (threshold: ≥1).
3. Responsiveness signal = 1 — no evidence of community engagement with the problem.
4. Build gate not met: operational_autonomy=6 is below the floor of 7; Salesforce Metadata API integration requires freelance developer work.

**Recommended next action:** Re-queue for Market Radar with expanded search — Trailblazer Community, r/salesforce, Salesforce release notes discussions, job postings for "Salesforce DevOps" or "Salesforce security admin", and competitor review sites (G2, Capterra) for Strongpoint/Gearset.

## Source list

- https://salesforce.stackexchange.com/questions/439629/deploying-a-profile-via-metadata-api-with-debug-apex-enabled-but-modify-all-data (retrieved 2026-07-12 IDT)
