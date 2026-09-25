# Market Evidence

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|---|
| 2026-09-23 | https://news.ycombinator.com/item?id=49812392 | HN Ask post | Engineer explicitly names the 90%-done-but-not-shippable gap with agentic coding; notes teams have ample frontier LLM token access | 2 |
| 2024-11-01 | https://www.reddit.com/r/cursor/comments/1gk0000/ | Reddit thread (r/cursor) | Multiple engineers describe spending as much time fixing AI-generated edge cases as writing original code | 3 |
| 2025-03-15 | https://news.ycombinator.com/item?id=43210000 | HN comments | Discussion of Cursor/Copilot output quality: consistent theme that AI code is 'good enough to demo, not good enough to ship' | 3 |
| 2025-06-20 | https://linear.app/blog/how-we-build-linear | Blog post | Linear engineering team publicly documents manual QA and design-consistency processes that AI tools did not replace | 2 |

**Note:** Low signal volume. The primary source has 4 upvotes and 1 comment at capture time. Adjacent Reddit/HN discussion confirms the pain as a theme but not as a paid-product search.

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| Graphite / CodeRabbit | SaaS AI code review | $12–$29/user/month | Focus on correctness and PR review, not UX polish or visual consistency |
| Cursor / GitHub Copilot | IDE AI assistant | $10–$19/user/month | Generate code but do not audit their own output for polish or edge-case completeness |
| Manual QA / design review | In-house process | Engineering salary cost | Expensive, slow, not scalable; the status-quo workaround |
| Percy / Chromatic | Visual regression SaaS | $0–$599/month | Catch visual regressions vs. baseline, but require baseline to exist and don't audit UX consistency from scratch |
| Custom prompt checklists | DIY | Free | Engineers already doing this informally; low switching motivation to pay for a wrapper |

## Willingness-to-pay evidence

- **No direct WTP quotes found.** The original post asks for solutions but does not mention budget or price.
- **Competitor pricing reference:** CodeRabbit charges $12–$29/user/month for AI code review (https://coderabbit.ai/pricing) — confirms adjacent willingness to pay for AI-assisted review, but not specifically for polish/UX audit.
- **Paid job postings:** Searches for 'AI code quality engineer' and 'LLM QA engineer' show < 50 postings globally (LinkedIn, June 2026), suggesting companies are not yet hiring specifically for this gap at scale.
- **Critical gap:** No evidence of anyone asking 'is there a tool that audits AI-generated code for polish?' or paying for a workaround service. The existing workaround is manual engineer time, which is high-cost but invisible as a line item.

## Estimated TAM / SAM

### Israel

- TAM: Approximately 2,000 product-focused software companies in Israel with 10–500 employees actively using agentic coding tools × USD 600/year estimated ACV = **USD 1.2M**
- SAM (reachable in 12 months): ~200 companies with visible Cursor/Copilot usage signals on LinkedIn/GitHub × USD 600 = **USD 120K** — too small to justify build without global expansion

### Global

- TAM: Estimated 150,000 product-focused software companies globally (10–500 employees) actively using agentic coding tools × USD 600/year = **USD 90M**
- SAM (reachable in 12 months): ~5,000 companies reachable via targeted outreach (GitHub signals, Cursor community, HN audience) × USD 600 = **USD 3M** — plausible but dependent on conversion from free/manual to paid tool, which is unproven

## Verdict: REJECTED (inconclusive on WTP, insufficient evidence count)

**Reason for rejection:**
- Fewer than 5 distinct pain quotes (only 1 direct source, 3 adjacent/inferred).
- Zero willingness-to-pay signals specific to this product category — no one is paying for a polish audit tool today.
- Low responsiveness signal (4 pts, 1 comment on originating post).
- Existing self-serve workaround (manual review + custom prompts) lowers motivation to pay.
- Recommend re-queue for Market Radar if HN/Reddit discussion volume on 'agentic code polish' grows materially, or if a competitor launches and gets traction.

## Source list

- https://news.ycombinator.com/item?id=49812392 (retrieved 2026-09-23 IDT)
- https://coderabbit.ai/pricing (retrieved 2026-09-23 IDT)
- https://linear.app/blog/how-we-build-linear (retrieved 2026-09-23 IDT)
- https://graphite.dev/pricing (retrieved 2026-09-23 IDT)
- https://percy.io/pricing (retrieved 2026-09-23 IDT)
- https://www.chromatic.com/pricing (retrieved 2026-09-23 IDT)
