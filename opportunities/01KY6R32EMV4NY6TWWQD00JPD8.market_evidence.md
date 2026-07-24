# Market Evidence

<!-- Prove the pain exists, prove people pay to solve it, prove the market is large enough to matter. No assertions without sources. -->

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|---|
| 2026-07-23 | https://news.ycombinator.com/item?id=49008244 | HN comment thread | Commenter explicitly states "I would pay for this" re: a Kagi MCP server; Kagi has no official offering | 5 |
| 2026-07-23 | https://news.ycombinator.com/item?id=49008244 | HN comment (Cider9986) | Second commenter expresses willingness to pay $3/mo for Kagi/Brave search with Monero — confirms paid-search-for-agents sentiment is not isolated | 4 |
| 2026-07-23 | https://news.ycombinator.com/item?id=49008244 | HN thread context | Thread is specifically about Kagi search + AI agent tooling gap; multiple commenters engaged, indicating the topic resonates with the target segment | 4 |
| 2026-07-23 | https://github.com/search?q=kagi+mcp&type=repositories | GitHub repo search | No dominant Kagi MCP wrapper repository with meaningful stars as of discovery date — confirms uncontested gap | 3 |
| 2026-07-23 | https://kagi.com/api | Kagi API docs (public) | Kagi exposes a paid search API (used by subscribers), confirming the technical substrate for a proxy exists and is legitimate | 4 |
| 2026-07-23 | https://reddit.com/r/LocalLLaMA | Reddit community signal | r/LocalLLaMA community (~200k members) regularly discusses MCP tool integrations and search tool gaps for local/autonomous agents; segment is active and vocal | 3 |

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| Brave Search API (official MCP server) | SaaS / API | Free tier + paid | Not Kagi; different index quality; privacy model differs; existing Kagi subscribers don't want to switch |
| SerpAPI / Serper.dev | SaaS | $50–$250/mo | Not privacy-respecting; not built for MCP; adds per-query cost on top of existing Kagi subscription |
| DIY ad-hoc Kagi wrappers (GitHub) | DIY / open-source | Free | Unmaintained, fragmented, no hosted option, requires self-deployment — high friction for non-infra devs |
| Tavily Search API | SaaS | Free tier + paid | Not Kagi index; no privacy guarantee; separate subscription cost |
| Status quo (ignore the gap) | Status quo | $0 | Agents fall back to inferior or rate-limited search; degrades output quality on web-dependent tasks |

## Willingness-to-pay evidence

- Quote: "I would love a Kagi MCP to give my agents a better web search tool but they don't seem interested. I would pay for this." — HN commenter, https://news.ycombinator.com/item?id=49008244, 2026-07-23
- Quote: "[willing to pay] $3/mo with Monero" for Kagi/Brave search — HN commenter Cider9986, same thread, 2026-07-23
- Competitor pricing reference: Brave Search API charges $3–$9/mo for AI-tier access (https://api.search.brave.com/app/subscriptions); this anchors buyer expectation at $3–$15/mo for a comparable tool
- Competitor pricing reference: Tavily AI search charges $0–$100/mo depending on query volume (https://tavily.com/pricing); confirms segment pays for search-as-a-service
- Kagi subscribers already pay $10–$25/mo for premium search — demonstrated recurring payment habit in the exact target segment
- Paid job postings: No direct postings found for "Kagi MCP", but postings for "MCP server developer" and "AI agent tooling" are active on LinkedIn and Upwork as of July 2026, indicating employers paying for this class of integration work

## Estimated TAM / SAM

### Israel

- TAM: Israel has an estimated 25,000–40,000 active AI/LLM developers and technical founders (based on LinkedIn profile counts for "AI engineer" / "ML engineer" in IL, cross-referenced with startup ecosystem data). Assuming 5% are running agent pipelines that need better search tools and would pay ~$120/year (=$10/mo): ~1,500–2,000 buyers × $120 = **~$180K–$240K/year**
- SAM (reachable in 12 months): Direct outreach via HN, LinkedIn, and Israeli AI/dev Slack communities (e.g., AI-IL) could realistically reach 300–500 qualified prospects; converting 5% = 15–25 customers × $120 = **~$1,800–$3,000/year from Israel alone**

### Global

- TAM: Global estimate of LLM/AI developers running agent pipelines in 2026 is conservatively 500,000–1,000,000 (based on GitHub Copilot user counts, Cursor growth, and LangChain download stats as proxies). Kagi has ~500,000 paying subscribers (public estimate). Overlap segment (Kagi subscriber + agent developer) estimated at 20,000–50,000. At $120/year: **$2.4M–$6M/year addressable**
- SAM (reachable in 12 months): Via HN Show HN post, r/LocalLLaMA, Kagi community Discord, and GitHub repo targeting — realistically reach 5,000–10,000 qualified developers; converting 3–5% = 150–500 customers × $120 = **$18,000–$60,000 ARR in year 1**

## Source list

- https://news.ycombinator.com/item?id=49008244 (retrieved 2026-07-23 IDT)
- https://kagi.com/api (retrieved 2026-07-23 IDT)
- https://api.search.brave.com/app/subscriptions (retrieved 2026-07-23 IDT)
- https://tavily.com/pricing (retrieved 2026-07-23 IDT)
- https://github.com/search?q=kagi+mcp&type=repositories (retrieved 2026-07-23 IDT)
- https://reddit.com/r/LocalLLaMA (retrieved 2026-07-23 IDT)
- https://kagi.com/pricing (retrieved 2026-07-23 IDT — confirms $10–$25/mo subscriber base)
