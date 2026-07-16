# Market Evidence

<!-- Opportunity: 01KXJ3MCM7W1SQRRTQ7MMSXXGP -->
<!-- Verdict: FAIL — build gate failure + insufficient distinct pain signals -->

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|
|---|
| 2026-07-15 | https://softwarerecs.stackexchange.com/questions/95481/http-proxy-like-software-between-browser-and-internet-that-can-manipulate-the-do | Forum question | Technical user (web archivist / developer) explicitly needs HTTPS-intercepting proxy with on-the-fly DOM rewriting; calls out TamperMonkey/GreaseMonkey as insufficient | 2 |

**Evidence gap:** Pass threshold requires ≥5 distinct pain quotes from distinct sources. Only 1 signal was surfaced by Market Radar. The signal_strength of the source post is itself rated 2/5, indicating low community engagement or corroboration at time of discovery.

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| Charles Proxy | Desktop SaaS / installable | ~USD 50 one-time | Traffic inspection and basic rewriting, but no GUI rule engine for DOM attribute manipulation; scripting required |
| Proxyman | Desktop installable (macOS-first) | ~USD 100 one-time | Excellent TLS interception UI; scripting via JavaScript hooks but not a visual DOM rewriting rule builder |
| Burp Suite Professional | Desktop security tool | USD 449/year | Powerful but security-focused; steep learning curve; not designed for QA/archiving DOM rewriting workflows |
| mitmproxy | Open-source CLI | Free | Full power but requires Python scripting; no GUI; no non-technical user path |
| TamperMonkey / GreaseMonkey | Browser extension | Free | Extension-layer only; cannot intercept at network layer; does not work when extension context is unavailable |

**Gap identified:** None of the above offer a no-code/low-code GUI rule builder for DOM rewriting layered on top of a working MITM proxy. The gap is real but may be a niche within a niche.

## Willingness-to-pay evidence

- Competitor pricing reference: Charles Proxy, ~USD 50 one-time, https://www.charlesproxy.com/buy/ — confirms developer willingness to pay for local proxy tooling.
- Competitor pricing reference: Proxyman, ~USD 100 one-time (standard license), https://proxyman.io/pricing — confirms macOS developer segment pays for polished proxy UIs.
- Competitor pricing reference: Burp Suite Professional, USD 449/year, https://portswigger.net/buy/pro — confirms security/QA segment pays significantly for proxy tooling with scripting.
- Direct quote from source: *"I am currently in need of a software… [TamperMonkey and GreaseMonkey] are obviously not appropriate for the task"* — implies active search and frustration, but no explicit price anchor or purchase intent stated.
- **Gap:** No quotes from additional distinct users expressing payment intent for a DOM-rewriting proxy specifically. Competitor pricing validates the adjacent market, not this exact product variant.

## Estimated TAM / SAM

### Israel

- TAM: Rough proxy — Israel has ~30,000 active web/QA developers (based on general tech workforce estimates). Assuming 5% need proxy tooling regularly → ~1,500 potential buyers × USD 99/year = **USD 148,500/year**. Too small to justify standalone build.
- SAM (reachable in 12 months): Developer communities (local Slack groups, Israeli dev forums, LinkedIn) could reach ~300–500 of these. SAM ≈ USD 30,000–50,000/year.

### Global

- TAM: ~5 million web developers globally (Stack Overflow survey proxy). Assuming 3% need dedicated proxy tooling → 150,000 × USD 99/year = **USD 14.85M/year**. More meaningful at global scale.
- SAM (reachable in 12 months): HN, Reddit r/webdev, r/QualityAssurance, devtools newsletters could reach 5,000–10,000 qualified developers. SAM ≈ USD 500,000–1,000,000/year at a realistic conversion.
- **Caveat:** The DOM-rewriting niche within proxy tooling is a subset of this; actual addressable market for this specific feature set is likely 10–20% of the proxy TAM, reducing global SAM to USD 50,000–200,000/year — marginal for a standalone build.

## Verdict

**FAIL — Do not promote to Lead Research.**

Two independent failure modes:

1. **Evidence threshold not met:** Only 1 distinct pain signal found (pass requires ≥5). Willingness-to-pay evidence is inferred from adjacent competitor markets, not direct quotes from users seeking this specific product.
2. **Build gate failure:** Buildability-with-AI scored 3/10 against a minimum threshold of 6. This product requires compiled network-layer software, TLS certificate authority management, OS-level trust store integration, and cross-platform testing — none of which is achievable via Claude prompts + standard factory tooling without a technical co-founder or contractor.

**Recommendation:** Kill this candidate in its current form. If the team later secures a technical co-founder or identifies an acqui-hire/OSS-fork path for an existing mitmproxy-based codebase, the demand validation (landing page + HN post) may be worth revisiting as a cheap pre-build signal test. Any such outreach requires approval before execution.

## Source list

- https://softwarerecs.stackexchange.com/questions/95481/http-proxy-like-software-between-browser-and-internet-that-can-manipulate-the-do (retrieved 2026-07-15 IDT)
- https://www.charlesproxy.com/buy/ (pricing reference, retrieved 2026-07-15 IDT)
- https://proxyman.io/pricing (pricing reference, retrieved 2026-07-15 IDT)
- https://portswigger.net/buy/pro (pricing reference, retrieved 2026-07-15 IDT)
