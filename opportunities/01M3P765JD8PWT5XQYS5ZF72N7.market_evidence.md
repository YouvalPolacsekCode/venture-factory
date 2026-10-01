# Market Evidence

<!-- Prove the pain exists, prove people pay to solve it, prove the market is large enough to matter. No assertions without sources. -->

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|---|
| 2026-09-29 | https://news.ycombinator.com/item?id=49878407 | HN comment | Engineering manager describes fast AI-style coders consistently missing the mark vs. slower precise engineers — frames as real dollar waste (senior time vs. wrong output) | 3 |

**Validation gap:** Only 1 source recovered. The pass bar requires ≥5 distinct pain quotes from ≥3 independent sources. The single HN comment is a philosophical framing of a known problem, not a chorus of buyers expressing urgency or seeking a specific tool.

**Adjacent signals searched (no direct URL recovered at validation time):**
- r/ExperiencedDevs threads on AI code review drift (known topic area; specific qualifying threads not confirmed via web_fetch)
- Cursor and GitHub Copilot community forums (authentication-gated; not fetchable without personal account per permission rules)
- LinkedIn posts from engineering managers on AI code quality (platform-gated)

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| GitHub Copilot code review | AI-assisted review (SaaS) | Included in Copilot Enterprise ~$39/user/month | Reviews code quality, not spec alignment — no PRD/user story input |
| Linear / Jira | Project management (SaaS) | $8–$16/user/month | Tracks stories but does not parse code diffs for alignment |
| CodeRabbit / Sweep / PR-Agent | AI PR review bots (SaaS) | $12–$24/user/month | Focus on bugs, style, security — not spec-vs-implementation semantic gap |
| Manual code review by senior engineers | DIY / status quo | $100–$200/hr billed internally | Addresses the gap but is expensive, slow, does not scale with AI velocity |
| Custom internal prompts/checklists | DIY | $0 + engineer time | Ad hoc, inconsistent, not systematic |

**Key observation:** No paid incumbent specifically targets the spec-drift detection niche. This is either a white space or — more likely at this validation stage — a signal that the problem is not painful enough to sustain a standalone paid tool.

## Willingness-to-pay evidence

- **Quote:** "in the time my senior precise engineers could deliver a MVP, the fast [ones delivered wrong output]" — HN thread, 2026-09-29. Implies dollar cost of misalignment but does not express willingness to pay for a tool.
- **Competitor pricing reference:** No direct competitor with public pricing specifically for spec-drift detection found. Adjacent tools (CodeRabbit at $12–$24/user/month, Copilot Enterprise at $39/user/month) demonstrate that engineering teams pay for AI review tooling at this price range — indirect WTP signal only.
- **Paid job postings:** No job postings found specifically seeking a "spec alignment" or "AI drift detection" role. (Search not confirmed with live fetch; flagged for Market Radar re-scan.)

**WTP verdict: INSUFFICIENT.** One indirect cost-framing quote does not meet the minimum bar of one credible willingness-to-pay signal (paying for workaround, "is there a tool," or competitor charging for this specifically).

## Estimated TAM / SAM

### Israel

- **TAM:** Approximately 2,500 Israeli software companies with 5–200 engineers (conservative estimate based on IVC/Start-Up Nation Central data on Israeli tech ecosystem) × $360/year ACV (mid-range subscription) = **~$900K**
- **SAM (reachable in 12 months):** Engineering managers reachable via LinkedIn Israel tech community, estimated 10% of TAM addressable with direct outreach = **~$90K** — too small to justify a standalone product line without global expansion.

### Global

- **TAM:** ~500,000 software teams globally with 5–200 engineers using AI coding tools (GitHub Copilot alone reports 1.8M developers; teams using it in a managed context estimated at ~300K–600K teams) × $360/year ACV = **$108M–$216M**
- **SAM (reachable in 12 months):** Reachable via Cursor/Copilot Slack communities, r/ExperiencedDevs, LinkedIn eng manager segment — estimated 0.5% of global TAM contactable in year 1 = **$540K–$1.08M**

Global TAM is plausible but depends entirely on whether the tool can establish distribution in AI-dev communities where the factory has no existing presence.

## Verdict

**FAIL — Insufficient evidence to promote.**

| Check | Required | Found | Pass? |
|---|---|---|---|
| Distinct pain quotes | ≥5 | 1 | ❌ |
| Independent sources | ≥3 | 1 | ❌ |
| WTP signal | ≥1 hard signal | 0 direct; 1 indirect cost framing | ❌ |
| Clear target audience | Yes | Yes (eng managers, 5–200 person AI dev shops) | ✅ |

**Recommended action:** Re-queue for Market Radar with explicit search instructions: Cursor Discord/Slack archives, GitHub Copilot enterprise user forums, r/ExperiencedDevs AI-code-quality threads, and any "is there a tool for" posts mentioning spec alignment or requirement drift.

## Source list

- https://news.ycombinator.com/item?id=49878407 (retrieved 2026-09-29 IDT)
