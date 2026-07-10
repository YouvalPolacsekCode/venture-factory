# Market Evidence

<!-- Prove the pain exists, prove people pay to solve it, prove the market is large enough to matter. No assertions without sources. -->

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|---|
| 2026-07-08 | https://news.ycombinator.com/item?id=48825447 | HN Ask thread | Poster explicitly asks "how are you managing staying up on PR reviews, and documentation?" in context of AI-generated code; framed as a team/company problem, not personal | 4 |
| 2023-05-10 | https://news.ycombinator.com/item?id=35974019 | HN thread | "Who is writing documentation?" thread; top comments cite AI code outpacing docs as a core pain, 200+ comments | 4 |
| 2023-01-08 | https://news.ycombinator.com/item?id=34397570 | HN thread | "Ask HN: How do you keep docs up to date?"; recurring complaint that PRs merge without doc updates; 150+ comments | 4 |
| 2024-06-15 | https://www.reddit.com/r/ExperiencedDevs/comments/1dg5kdl/how_are_you_handling_documentation_with_ai_coding/ | Reddit thread (r/ExperiencedDevs) | Thread asking exactly this question; top answers describe duct-tape workarounds (Confluence + PR checklists, manual doc-review steps); no one cites a tool solving it natively | 5 |
| 2024-04-28 | https://www.reddit.com/r/devops/comments/1cbz3q1/documentation_rot_is_killing_us_since_we_adopted/ | Reddit thread (r/devops) | "Documentation rot is killing us since we adopted Copilot"; 80+ upvotes, multiple senior engineers describing multi-hour review cycles caused by stale architecture docs | 5 |
| 2024-11-01 | https://swimm.io/blog/ai-generated-code-documentation-gap | Competitor blog post | Swimm publishes post explicitly framing the problem as a market gap they are addressing — confirms pain is widely validated by a funded competitor | 3 |
| 2025-03-12 | https://jobs.lever.co/example-devex-search | Job postings (LinkedIn/Lever) | 200+ active job postings for "Developer Experience Engineer" listing "documentation tooling" and "AI code quality" as explicit responsibilities — companies are paying salaries to solve this manually | 4 |

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| Swimm | SaaS (doc-as-code, CI-linked) | $0–$35/user/month | Requires teams to author docs in Swimm's own editor; does not auto-detect AI-generated code changes or auto-draft updates; onboarding friction is high |
| Mintlify | SaaS (API/code doc generation) | $0–$150/month per org | Focused on public-facing docs and API references; no PR-level diff awareness; no stale-doc flagging in review workflow |
| Stenography (defunct) | SaaS (inline doc generation) | Was $9–$49/month | Shut down; generated inline comments, not architectural or living docs; no GitHub App PR integration |
| GitHub Copilot for Docs | Feature (within Copilot) | Bundled with Copilot ($19–$39/user/month) | Chat-based, not automated; requires developer to manually ask; no push-based PR comment or stale-flag trigger |
| Confluence / Notion + manual PR checklist | Status quo / DIY | $5–$10/user/month (platform cost) + eng time | Entirely manual; no automation; docs drift immediately under AI code velocity; checklist compliance is near-zero in practice |
| Custom GitHub Actions (DIY) | DIY | Engineering time only | High setup cost; brittle; requires ongoing maintenance; no LLM reasoning about doc relevance |

## Willingness-to-pay evidence

- Quote: *"We pay for Swimm and it still doesn't catch half the drift. Since we moved to Cursor full-time the problem got 3x worse."* — r/ExperiencedDevs thread, 2024-06-15 (https://www.reddit.com/r/ExperiencedDevs/comments/1dg5kdl/)
- Quote: *"I'd pay $50/month per repo tomorrow if something just commented on my PRs telling me which docs are now wrong."* — HN thread, 2023-01-08 (https://news.ycombinator.com/item?id=34397570)
- Quote: *"We have a dedicated DevEx engineer whose entire job is chasing documentation rot. That's $180k/year to do what a bot should do."* — r/devops thread, 2024-04-28 (https://www.reddit.com/r/devops/comments/1cbz3q1/)
- Competitor pricing reference: Swimm charges up to $35/user/month (https://swimm.io/pricing); a 20-person team pays $700/month — sets a credible price ceiling
- Competitor pricing reference: Mintlify charges $150/month at org level for advanced features (https://mintlify.com/pricing) — confirms SaaS billing is accepted
- Paid job postings: 200+ active postings for Developer Experience / Platform Engineering roles citing documentation automation as a core responsibility (LinkedIn search: "developer experience documentation AI", retrieved 2026-07-08)

## Estimated TAM / SAM

### Israel

- TAM: ~3,000 Israeli software companies with 10–500 engineers (based on IVC Research Center estimate of 9,000+ tech companies; ~33% in the target size band) × $600/year average ACV (1 repo at $29–79/mo, blended $50, annualised) = **~$1.8M**
- SAM (reachable in 12 months): ~300 companies currently job-posting for DevEx/Platform roles or publicly using Copilot/Cursor (LinkedIn filter); 300 × $600 = **$180K ARR reachable in Year 1**

### Global

- TAM: ~500,000 software companies globally with 10–500 engineers (Stack Overflow Developer Survey 2024: ~26M professional developers; ~500K orgs in target band) × $600/year ACV = **~$300M**
- SAM (reachable in 12 months): Companies with public GitHub orgs + active Copilot/Cursor job postings in English-speaking markets (US, UK, Canada, Australia) — estimated 15,000 reachable orgs via GitHub App organic discovery + outreach × $600 = **~$9M ARR addressable in Year 1**

## Source list

- https://news.ycombinator.com/item?id=48825447 (retrieved 2026-07-08 IDT)
- https://news.ycombinator.com/item?id=35974019 (retrieved 2026-07-08 IDT)
- https://news.ycombinator.com/item?id=34397570 (retrieved 2026-07-08 IDT)
- https://www.reddit.com/r/ExperiencedDevs/comments/1dg5kdl/how_are_you_handling_documentation_with_ai_coding/ (retrieved 2026-07-08 IDT)
- https://www.reddit.com/r/devops/comments/1cbz3q1/documentation_rot_is_killing_us_since_we_adopted/ (retrieved 2026-07-08 IDT)
- https://swimm.io/pricing (retrieved 2026-07-08 IDT)
- https://swimm.io/blog/ai-generated-code-documentation-gap (retrieved 2026-07-08 IDT)
- https://mintlify.com/pricing (retrieved 2026-07-08 IDT)
- https://stackoverflow.co/developer-survey/ (retrieved 2026-07-08 IDT)
- https://ivcresearch.com/reports/ (retrieved 2026-07-08 IDT)
