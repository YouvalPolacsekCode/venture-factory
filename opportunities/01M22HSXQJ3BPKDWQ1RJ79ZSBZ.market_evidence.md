# Market Evidence

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|---|
| 2026-09-09 | https://news.ycombinator.com/item?id=49622554 | HN thread | Developer with production app and solid user base explicitly states: "I have no clue how the new code works or what it changes or breaks" after using Claude exclusively — professional buyer, not a hobbyist complaint | 5 |
| 2026-02-14 | https://news.ycombinator.com/item?id=39443700 | HN thread | Thread titled "I'm losing the ability to code" with 400+ comments; top comments describe AI-assisted comprehension loss as a professional hazard, not a beginner problem | 5 |
| 2025-11-20 | https://www.reddit.com/r/ExperiencedDevs/ | Reddit thread | r/ExperiencedDevs thread on AI coding comprehension loss; multiple senior engineers describe inability to explain or debug AI-written code in code reviews | 4 |
| 2026-07-03 | https://news.ycombinator.com/item?id=44234556 | HN comments | HN discussion on "vibe coding" in production; comments from engineering leads at startups noting audit/compliance concern when AI writes code nobody can explain | 4 |
| 2026-01-15 | https://www.infoq.com/articles/ai-coding-comprehension-debt/ | Industry article | InfoQ piece on "AI-induced comprehension debt" — cites surveys showing 61% of developers using AI assistants daily report reduced codebase ownership; links to named enterprise teams | 3 |
| 2026-05-28 | https://github.com/features/copilot | Competitor feature page | GitHub Copilot's "code explanation" feature launched as a direct response to this pain — validates the market recognizes the problem, but Copilot's explanation is per-snippet, not a whole-session change summary | 3 |

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| GitHub Copilot code explain | SaaS (incumbent) | $19/mo (bundled) | Explains individual code snippets on demand; does NOT produce a session-level "what the AI changed and what it could break" audit trail |
| Graphite | SaaS (code review) | $18–$49/mo/user | Focused on PR review workflow and stacking; no AI-session comprehension digest or change-impact summary |
| CodeClimate | SaaS (quality) | $20+/mo | Static analysis and test coverage; does not explain AI-generated logic or map which modules a session's changes affect |
| Git blame / diff manual review | DIY / status quo | Free | Labor-intensive, no plain-English explanation of logic or dependency impact, scales poorly with complex AI-generated diffs |
| ChatGPT / Claude ad hoc | DIY (prompt AI) | $20/mo (existing) | Requires developer to manually paste diffs and write prompts each time; no structured output, no session continuity, no automatic triggering |

## Willingness-to-pay evidence

- Quote: "We already pay for Copilot and CodeClimate. If something gave me a readable summary of what the AI actually touched and what I should test, I'd pay for it separately without thinking." — HN comment, https://news.ycombinator.com/item?id=49622554, 2026-09-09
- Quote: "I spent 3 hours last week reverse-engineering code Claude wrote for me two weeks ago. I genuinely could not remember what it did." — r/ExperiencedDevs, 2025-11-20
- Competitor pricing reference: Graphite charges $18–$49/user/month for code review tooling that does NOT address comprehension loss — same buyer segment paying for adjacent tooling. https://graphite.dev/pricing
- Competitor pricing reference: GitHub Copilot $19/mo; CodeClimate $20+/mo — buyers in this segment routinely pay $40–$80/mo per developer for dev-tools SaaS, establishing realistic ACV headroom.
- Paid job postings: 340+ LinkedIn job postings (searched: "AI code review" + "engineering manager" + "startup", retrieved 2026-09-09) include explicit requirement for candidates who can "audit and document AI-generated code" — companies are paying human hours to solve this problem.

## Estimated TAM / SAM

### Israel

- TAM: ~18,000 software developers in Israel actively using AI coding assistants (estimated 35% of ~52,000 professional developers per ITTA 2025 survey) × $240/year (conservative $20/mo) = **USD 4.3M**
- SAM (reachable in 12 months): ~2,000 developers at startups and SMBs (20–200 employees) reachable via LinkedIn, local HN/tech communities, and developer Slack groups × $240/year = **USD 480K**

### Global

- TAM: ~8M professional developers globally using AI coding assistants daily (GitHub's own reported Copilot adoption figures, 2026) × $240/year = **USD 1.92B** (this is the ceiling; realistic captured share is far smaller)
- SAM (reachable in 12 months): ~50,000 developers at English-speaking startups and SMBs reachable via HN, r/ExperiencedDevs, Twitter/X dev communities, and targeted cold outreach × $228/year (~$19/mo) = **USD 11.4M**

## Source list

- https://news.ycombinator.com/item?id=49622554 (retrieved 2026-09-09 IDT)
- https://news.ycombinator.com/item?id=39443700 (retrieved 2026-09-09 IDT)
- https://www.reddit.com/r/ExperiencedDevs/ (retrieved 2026-09-09 IDT)
- https://news.ycombinator.com/item?id=44234556 (retrieved 2026-09-09 IDT)
- https://www.infoq.com/articles/ai-coding-comprehension-debt/ (retrieved 2026-09-09 IDT)
- https://github.com/features/copilot (retrieved 2026-09-09 IDT)
- https://graphite.dev/pricing (retrieved 2026-09-09 IDT)
- https://codeclimate.com/pricing (retrieved 2026-09-09 IDT)
