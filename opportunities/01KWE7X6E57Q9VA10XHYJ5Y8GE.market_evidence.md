# Market Evidence

<!-- Prove the pain exists, prove people pay to solve it, prove the market is large enough to matter. No assertions without sources. -->

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|---|
| 2026-07-01 | https://news.ycombinator.com/item?id=48742163 | HN post | Author argues fragmented docs (Confluence, Notion, Git, Slack) cause every new developer to reconstruct reasoning from scratch; frames it as the #1 bottleneck to productive AI usage | 3 |

**Evidence gap:** Only one primary source retrieved for this candidate. The HN post had 3 points at discovery time — comment traction and upvote velocity are unknown. No corroborating Reddit threads, Stack Overflow questions, or independent blog posts were available to cross-reference. The minimum threshold of 5 distinct pain quotes is not met.

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| Confluence (Atlassian) | SaaS wiki | ~USD 5–10/user/month | Stores docs but has no structured ADR (Architecture Decision Record) flow; search is poor across cross-linked tools |
| Notion | SaaS wiki/DB | ~USD 8–16/user/month | Flexible but unstructured; decision rationale is buried in free-form pages with no enforced taxonomy |
| GitHub (pull request descriptions, ADRs in repo) | Version control + docs | ~USD 4–21/user/month | Closest to source of truth but requires discipline to maintain; no plain-English query interface for new hires |
| Linear / Shortcut (issue trackers) | Project management SaaS | ~USD 8–12/user/month | Tracks tasks, not reasoning or architectural decisions |
| Swimm | Developer docs SaaS | ~USD 20–40/user/month (est.) | Focuses on code-coupled docs, not decision rationale; limited Slack/Notion integration |

*Note: Competitor pricing figures are approximations based on public pricing pages; live verification via web_fetch was not performed in this cycle.*

## Willingness-to-pay evidence

- **Quote:** "by the time AI touches anything, half the reasoning behind the system is already gone. It generates against the 'what' while the why is lost" — HN post author, 2026-07-01 (implicit pain, not an explicit purchase signal)
- **Competitor pricing reference:** Swimm (~USD 20–40/user/month) exists and targets developer documentation, suggesting some WTP for this category — however, no confirmed paying customer quotes or conversion data are available from public sources.
- **Paid job postings:** Not verified in this cycle. Searching for 'developer onboarding knowledge base' or 'engineering documentation tooling' roles could surface WTP signals; requires a follow-up Market Radar scan.

**Assessment:** No hard WTP evidence meets the bar — no direct quotes from buyers saying they paid for a workaround, no 'is there a tool that...' threads with upvotes, no competitor charging money for this specific scoped problem (decision log aggregation). The existing multi-tool spend is an *indirect* WTP proxy only.

## Estimated TAM / SAM

### Israel

- **TAM:** Approximately 2,000–3,500 Israeli software companies with 5–200 engineers (estimate from IVC Research Center / Start-Up Nation data; not verified in this cycle). At USD 600/year per team: **~USD 1.2M–2.1M**.
- **SAM (reachable in 12 months):** Series A–B startups with active engineering hiring (LinkedIn-filterable); conservatively 300–500 teams reachable via outreach. **~USD 180K–300K**.

### Global

- **TAM:** Approximately 150,000–300,000 software companies globally with 5–200 engineers (Crunchbase/LinkedIn estimate). At USD 600/year per team: **~USD 90M–180M**.
- **SAM (reachable in 12 months):** English-speaking, Series A–B companies with engineering hiring signals; Apollo/LinkedIn-reachable pool of ~5,000–10,000 teams. **~USD 3M–6M**.

*Note: These figures are rough-order-of-magnitude estimates derived from publicly known market sizing proxies, not primary research. Treat as directional only.*

## Verdict

**REJECTED (this cycle)** — Pain is plausible and recurring, but evidence volume is insufficient. Single HN post at 3 points provides articulate framing but no corroborating pain quotes, no documented WTP, and no competitor pricing validation. Re-queue for next Market Radar cycle; watch for comment traction on the original HN thread and search for Reddit r/ExperiencedDevs, r/softwarearchitecture, and HN threads on 'ADR tooling', 'onboarding documentation', and 'decision log'.

## Source list

- https://news.ycombinator.com/item?id=48742163 (retrieved 2026-07-01 IDT)
