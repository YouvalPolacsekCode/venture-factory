# Market Evidence

<!-- Opportunity: 01KWXMPWX4RPDZ0BMAVNFSGBN9 -->
<!-- Problem: Engineering teams paying for AI coding agents cannot measure real-world session-level performance. -->
<!-- Verdict: REJECTED (inconclusive evidence base — re-queue next cycle) -->

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|---|
| 2026-07-07 | https://news.ycombinator.com/item?id=48810964 | HN thread (original post) | Author actively building a real-session benchmark tool for Claude Code / Codex; identifies that existing benchmarks (one-shot, clean harnesses) don't reflect messy multi-step sessions with cache TTL expiry and context growth; demonstrates felt need strong enough to self-build | 3 |
| — | — | Adjacent HN / forum threads | No corroborating multi-source threads found in available evidence; pain exists but has not surfaced at scale in public forums beyond this post | 1 |
| — | — | Competitor product pages | No dedicated SaaS product found that specifically tracks multi-session AI coding agent cost + quality at team level (as of evidence sweep date) | 2 |

**Evidence gap:** The pass threshold requires ≥ 5 distinct pain quotes from ≥ 3 separate sources. Current evidence provides 1 primary source with 1 articulate pain expression. The pain is credible but not yet multi-source documented.

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| Anthropic Console usage dashboard | Built-in / free | $0 (included with API) | Shows token spend and call counts but has no session grouping, no quality signal, no cross-engineer aggregation, no benchmark comparison |
| GitHub Copilot Business analytics | Built-in / free | Included with Copilot Business (~$19/seat/month) | Tracks acceptance rate and suggestion counts; no cost-per-task, no multi-step session replay, specific to Copilot only |
| LangSmith (LangChain) | SaaS | Free tier; Team ~$39/month | Designed for LLM app developers instrumenting their own pipelines; not built for end-user dev-tool sessions (Claude Code, Codex); requires manual SDK instrumentation |
| Helicone | SaaS | Free tier; Growth from ~$100/month | Proxy-based API logging and cost tracking; covers raw API calls but not session-level semantics or quality scoring for coding tasks |
| DIY scripts / spreadsheets | DIY | $0 | High friction, no standardisation, not scalable across teams |

**Gap we would exploit:** None of the above products model a *session* as a unit of work (start → multi-step → stop, with context growth and cache effects), none score *quality* of output for coding tasks at session level, and none produce a cross-team benchmark comparable across engineers or over time.

## Willingness-to-pay evidence

- **Existing tool spend as proxy:** Target buyers already pay $20–$100+/seat/month for Claude Code or Copilot Business, establishing that this segment has AI tooling budget and ROI pressure. This is an indirect WTP signal, not direct.
- **Direct quote (WTP):** None found. No "how much would you pay for this", no pre-purchase requests, no waitlist with pricing signal in available evidence.
- **Competitor pricing reference:** No direct competitor product charging for session-level AI coding analytics found. Closest proxies: LangSmith Team ~$39/month, Helicone Growth ~$100/month — but neither is the same product.
- **Paid job postings:** No job postings specifically for "AI coding agent analytics" or "developer productivity instrumentation" found in evidence sweep.
- **Self-build signal:** The HN author building their own tool implies strong personal felt need, but does not constitute organisational willingness to pay for a purchased product.

**WTP verdict:** No direct willingness-to-pay signal. Fails the mandatory pass criterion.

## Estimated TAM / SAM

### Israel

- **Qualifying customers:** Israeli software companies with ≥ 5 engineers using Claude Code or GitHub Copilot. Estimate ~400–600 companies at Series A and above (based on IVC / Start-Up Nation Central data ranges for Israeli tech companies with engineering headcount at that scale).
- **Realistic ACV:** $600–$1,200/year per company for a team-level analytics subscription (analogous to mid-tier SaaS tooling).
- **TAM (Israel):** 500 companies × $900/year = **~$450K/year**.
- **SAM (12 months):** Realistically contactable via LinkedIn + HN + local engineering communities: ~50–80 companies → **~$45K–$72K/year**. Below meaningful threshold for a standalone product; viable only as part of a broader platform.

### Global

- **Qualifying customers:** Software companies globally with ≥ 5 engineers on AI coding agent subscriptions. Conservative estimate: 25,000–50,000 companies (extrapolating from Anthropic's and GitHub's disclosed enterprise customer ranges and Copilot Business seat counts).
- **Realistic ACV:** $600–$2,400/year depending on team size and tier.
- **TAM (Global):** 35,000 companies × $1,200/year = **~$42M/year**.
- **SAM (12 months):** Early-adopter segment (engineering-led, AI-forward, public on HN/LinkedIn): ~500–1,000 companies → **~$600K–$1.2M/year reachable**.
- **Note:** TAM is plausible but not large; the space will likely be absorbed by the platform vendors themselves (Anthropic, GitHub, OpenAI) as a free dashboard feature within 12–18 months, compressing the independent product window.

## Verdict

**REJECTED — Inconclusive evidence; re-queue for next Market Radar cycle.**

| Criterion | Threshold | Actual | Pass? |
|---|---|---|---|
| Distinct pain quotes | ≥ 5 | 1 | ❌ |
| Separate sources | ≥ 3 | 1 | ❌ |
| Willingness-to-pay signal | ≥ 1 direct | 0 direct | ❌ |
| Clear target audience | Yes | Yes (eng managers, platform engineers) | ✅ |
| Existing spend in category | Yes | Yes (Claude Code / Copilot subscriptions) | ✅ |

**Recommended next action:** Re-queue. Market Radar should watch for: (1) follow-up posts by the HN author or ProductHunt launch; (2) new HN / Reddit threads on AI coding ROI measurement; (3) any competitor announcing session-level analytics. If 3+ corroborating sources emerge, re-score and re-run Pain Validation. Do not advance to Lead Research or commit any build resources at this stage.

## Source list

- https://news.ycombinator.com/item?id=48810964 (retrieved 2026-07-07 IDT)
