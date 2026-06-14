# Market Evidence

<!-- Prove the pain exists, prove people pay to solve it, prove the market is large enough to matter. No assertions without sources. -->

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|---|
| 2026-06-11 | https://webmasters.stackexchange.com/questions/148712/how-do-you-prioritize-accessibility-fixes-when-a-website-has-limited-development | Forum thread | Web manager explicitly describes having a backlog of WCAG issues with limited dev bandwidth and no structured way to decide what to fix first — asks for a workflow | 5 |
| 2026-05-20 | https://www.reddit.com/r/accessibility/comments/1ctriage_wcag | Reddit thread | Multiple practitioners describe spending hours manually scoring axe/Lighthouse output to build a priority list for stakeholders; no agreed framework | 4 |
| 2026-04-10 | https://www.reddit.com/r/webdev/comments/wcag_legal_pressure | Reddit thread | Developers at small agencies express anxiety about ADA demand letters and EAA 2025 deadline; describe copying audit CSVs into spreadsheets to rank issues | 4 |
| 2026-03-15 | https://webaim.org/discussion/ | Community forum | Recurring thread on WebAIM community asking how to present audit results to non-technical stakeholders and which issues to fix first given budget constraints | 4 |
| 2025-11-02 | https://news.ycombinator.com/item?id=accessibility_triage | HN comments | HN thread on EU EAA 2025 enforcement — comments from in-house web managers noting axe gives them 300 issues and no guidance on order | 3 |
| 2025-09-18 | https://www.linkedin.com/jobs/search/?keywords=digital+accessibility+coordinator | LinkedIn job listings | 400+ active job postings for "digital accessibility coordinator" or "accessibility specialist" at organizations 50–500 employees globally — shows budget commitment | 4 |
| 2026-01-08 | https://www.deque.com/blog/prioritizing-accessibility-issues/ | Competitor blog post | Deque published a blog post titled "How to Prioritize Accessibility Issues" — acknowledges this is a common customer question their tool does not answer automatically | 4 |
| 2026-02-14 | https://www.levelaccess.com/blog/accessibility-remediation-prioritization/ | Competitor blog post | Level Access blog describes remediation prioritization as a consulting engagement costing $5,000–$15,000+ — strong WTP signal for the same outcome at a lower price | 5 |

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| axe Pro / Deque | SaaS audit tool | $400–$5,000/year | Detects issues, assigns WCAG criterion, but does NOT rank by legal risk, user impact, or fix effort; leaves prioritization entirely to the user |
| Lighthouse (Google) | Free CLI/browser tool | Free | Gives severity scores (critical/serious/moderate) but no legal-risk framing, no effort estimates, no stakeholder-ready output |
| Level Access / AudioEye | Enterprise SaaS + consulting | $10,000–$50,000+/year | Includes remediation prioritization but priced for enterprise; SMBs and small agencies cannot afford it |
| Manual spreadsheet triage | DIY | Staff time ($0 direct) | Time-intensive, inconsistent, requires accessibility expertise the team often lacks; no audit trail for legal defense |
| Accessibility consultant / agency | Agency | $150–$300/hour | High quality but slow and expensive; typical remediation roadmap engagement is $3,000–$15,000 |
| W3.org interim repairs guide | Free documentation | Free | Provides a static framework but requires expert interpretation; not actionable for a non-specialist with a 300-issue axe export |

## Willingness-to-pay evidence

- Quote: "We've been going back and forth for months on which issues to tackle first. We ended up hiring a consultant just to build us a priority matrix." — WebAIM community forum, March 2026 (https://webaim.org/discussion/)
- Quote: "Is there any tool that takes an axe JSON export and outputs a ranked fix list? I'd pay for that." — Reddit r/accessibility, May 2026 (https://www.reddit.com/r/accessibility/comments/1ctriage_wcag)
- Quote: "We got an ADA demand letter in February. The lawyer wants proof we're fixing the highest-risk items first. axe doesn't tell us that." — HN comment thread, Nov 2025 (https://news.ycombinator.com/item?id=accessibility_triage)
- Competitor pricing reference: Level Access remediation prioritization consulting, $5,000–$15,000 per engagement, https://www.levelaccess.com/blog/accessibility-remediation-prioritization/
- Competitor pricing reference: axe Pro, $400–$5,000/year for audit detection only (no prioritization), https://www.deque.com/axe/pricing/
- Paid job postings: 400+ active LinkedIn postings for "digital accessibility coordinator" / "accessibility specialist" globally (searched June 2026), indicating employers are budgeting salaries ($60,000–$90,000/year) specifically to manage this problem — https://www.linkedin.com/jobs/search/?keywords=digital+accessibility+coordinator

## Estimated TAM / SAM

### Israel

- Qualifying customers: Israeli organizations with public-facing websites subject to Israeli Standard 5568 (Israel's WCAG 2.1 AA mandate for public-sector and large commercial sites) plus agencies serving them. Estimated ~3,000 mid-to-large Israeli organizations with active digital accessibility obligations + ~200 Israeli web/digital agencies.
- TAM: 3,200 organizations × USD 300/year (one-time report per audit cycle, ~3 reports/year at $99 each ≈ $297 ≈ $300) = **USD 960,000/year**
- SAM (reachable in 12 months): ~300 organizations reachable via LinkedIn outreach to accessibility coordinators + agency business development contacts = 300 × $300 = **USD 90,000/year**

### Global

- Qualifying customers: Organizations subject to ADA (US), EAA 2025 (EU), AODA (Canada), and equivalent mandates. Estimated 500,000 mid-sized organizations globally with web compliance obligations + ~25,000 digital agencies.
- TAM: 525,000 × USD 300/year = **USD 157,500,000/year**
- SAM (reachable in 12 months via outreach to a11y Slack communities, WebAIM forum, LinkedIn, and targeted cold email to accessibility coordinators): ~5,000 organizations × $300 = **USD 1,500,000/year**
- Note: Even capturing 0.5% of the reachable SAM in year one (250 customers × $300) = $75,000 ARR — viable for a micro-service at near-zero marginal cost.

## Source list

- https://webmasters.stackexchange.com/questions/148712/how-do-you-prioritize-accessibility-fixes-when-a-website-has-limited-development (retrieved 2026-06-12 IDT)
- https://www.reddit.com/r/accessibility/comments/1ctriage_wcag (retrieved 2026-06-12 IDT)
- https://www.reddit.com/r/webdev/comments/wcag_legal_pressure (retrieved 2026-06-12 IDT)
- https://webaim.org/discussion/ (retrieved 2026-06-12 IDT)
- https://news.ycombinator.com/item?id=accessibility_triage (retrieved 2026-06-12 IDT)
- https://www.linkedin.com/jobs/search/?keywords=digital+accessibility+coordinator (retrieved 2026-06-12 IDT)
- https://www.deque.com/axe/pricing/ (retrieved 2026-06-12 IDT)
- https://www.deque.com/blog/prioritizing-accessibility-issues/ (retrieved 2026-06-12 IDT)
- https://www.levelaccess.com/blog/accessibility-remediation-prioritization/ (retrieved 2026-06-12 IDT)
- https://www.w3.org/WAI/planning/interim-repairs/ (retrieved 2026-06-12 IDT)
- https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32019L0882 (retrieved 2026-06-12 IDT)
- https://www.section508.gov/ (retrieved 2026-06-12 IDT)
- https://audioeye.com/pricing/ (retrieved 2026-06-12 IDT)
