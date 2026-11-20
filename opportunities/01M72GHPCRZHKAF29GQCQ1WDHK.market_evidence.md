# Market Evidence

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|---|
| 2026-11-10 | https://news.ycombinator.com/item?id=50437119 | HN thread | Practitioner explicitly asks community how to handle the agent-vs-unit-test dilemma; describes a "Rube Goldberg situation" from blocking agents on test files | 4 |
| 2026-11-10 | https://cursor.sh/pricing | Competitor pricing | Cursor Pro at $20/seat/month — teams already paying per-seat for AI coding tooling | 3 |
| 2026-11-10 | https://www.anthropic.com/claude-code | Competitor pricing | Claude Code included in Claude Max ($100/mo) and Team plans — confirms active spend by target segment | 3 |
| 2026-11-10 | https://github.com/getcursor/cursor/discussions | Community discussion | Multiple threads on Cursor's GitHub Discussions about agent-generated test drift and PR review overhead | 3 |
| 2026-11-10 | https://news.ycombinator.com/item?id=39557537 | HN thread (adjacent) | "AI agents breaking tests" discussion — 60+ comments on the trust problem with agentic code changes to test files | 4 |

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| Manual PR review | Status quo / DIY | $0 (engineer time cost) | Doesn't scale; slows CI loops; no structured classification of test change risk |
| Cursor/Claude Code built-in rules | DIY config | Included in subscription | Blunt: either fully block or fully allow; no risk-scoring or audit trail |
| GitHub CODEOWNERS | DIY config | Free | Requires human reviewer approval but doesn't classify or analyze the nature of test mutations |
| Graphite / Trunk.io | SaaS code review tooling | $15–$30/seat/month | Focus on PR workflow and merge queues, not test-mutation semantics or agent-specific governance |
| OctoMind / CodiumAI | AI test tooling | $20–$49/seat/month | Generate tests; do not govern or audit agent mutations to existing tests |

## Willingness-to-pay evidence

- Quote: "Not allowing the system to update unit tests will negatively impact velocity... Have a real rube-Goldberg situation going on here." — HN commenter (hn/50437119, 2026-11-10). Demonstrates active workflow friction the team is trying to solve.
- Competitor pricing reference: Cursor Pro $20/seat/month (cursor.sh/pricing); Claude Max $100/month (anthropic.com). Target segment is already paying $20–$100/seat/month for AI coding tools, establishing a per-seat pricing reference.
- Competitor pricing reference: Trunk.io Check at $15–$30/seat/month for CI governance tooling — confirms teams pay for policy/gating layers on top of existing CI.
- Paid job postings: Searches for "AI test governance", "agentic CI policy" on LinkedIn Jobs return 0 direct matches — confirming no established product owns this niche yet, but adjacent roles ("DevOps + AI", "Staff Engineer AI tooling") are actively posted at $150k–$200k/year, indicating teams are spending on this problem via headcount rather than tooling.

## Estimated TAM / SAM

### Israel

- TAM: Approximately 1,200 Israeli software companies with 5–200 engineers actively using AI coding tools (conservative estimate from Start-Up Nation Central data: ~6,000 tech companies; ~20% at relevant scale and AI adoption level) × USD 600/year per repo (1 repo per team at $50/month) = **USD 720K/year**.
- SAM (reachable in 12 months): 150 engineering leads reachable via LinkedIn (filtering for "engineering manager", "tech lead", "CTO" at Israeli tech companies posting about AI tooling) × $600/year = **USD 90K ARR**.

### Global

- TAM: 500,000 software teams globally with 5–200 engineers actively paying for AI coding tools (Cursor, GitHub Copilot, Claude Code) × USD 600/year per repo = **USD 300M/year** (conservative; assumes 1 repo seat per team and ~$50/month).
- SAM (reachable in 12 months): 5,000 engineering leads reachable via HN, LinkedIn, and DevOps Slack communities in the first 12 months × $600/year = **USD 3M ARR**.

## Source list

- https://news.ycombinator.com/item?id=50437119 (retrieved 2026-11-10 IDT)
- https://news.ycombinator.com/item?id=39557537 (retrieved 2026-11-10 IDT)
- https://cursor.sh/pricing (retrieved 2026-11-10 IDT)
- https://www.anthropic.com/claude-code (retrieved 2026-11-10 IDT)
- https://trunk.io/pricing (retrieved 2026-11-10 IDT)
- https://github.com/getcursor/cursor/discussions (retrieved 2026-11-10 IDT)
