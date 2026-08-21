# Market Evidence

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|---|
| 2026-08-13 | https://salesforce.stackexchange.com/questions/439751/ampscript-createsobject-error-field-integrity-exception-required-field-is-m | Stack Exchange question | Developer blocked by opaque FIELD_INTEGRITY_EXCEPTION in AMPscript CreateSObject call; no actionable error message | 2 |
| 2026-08-14 | https://salesforce.stackexchange.com/questions/439751/ampscript-createsobject-error-field-integrity-exception-required-field-is-m | Stack Exchange question (second signal in same source) | Developer unable to wire Apex class reference into Prompt Builder pre-filter; runtime failure with no guidance | 2 |

**Evidence gap note:** Only two question signals, both from the same discovery source URL, both low-upvote/low-answer threads. The scoring notes confirm signal_strength was capped at 2. No Reddit threads, HN discussions, Trailblazer Community complaint volumes, or Twitter/LinkedIn corroboration was located in the source data. No competitor pricing pages or paid-tool evidence was surfaced.

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| Salesforce Trailblazer Community | Free forum / community | Free | Answers are crowdsourced and slow; no guaranteed resolution time; requires developer to self-diagnose from responses |
| Salesforce Stack Exchange | Free Q&A | Free | Same as above; highly effective for common errors, meaning AI diagnostic may not outperform for standard cases |
| Salesforce Premier / Signature Support | Official vendor support | Bundled with enterprise licenses (~$20–50k+/yr) | Slow response for developer-tier questions; not designed for real-time debugging |
| Independent Salesforce consulting agencies | Human consulting | $100–250/hr | Expensive; overkill for single-error debugging; already the default fallback |
| ChatGPT / Claude direct prompting | DIY AI | Free–$20/mo | Developer can already paste error + code into a general LLM for free; directly undercuts the report-based product proposition |

**Critical gap:** The largest alternative — free direct LLM prompting — is effectively the same product the opportunity proposes, without the Stripe paywall. A developer who encounters a Salesforce AMPscript error can paste it into Claude.ai at no cost today. The proposed product must either deliver materially better output (fine-tuned on Salesforce error patterns, with curated fix libraries) or provide workflow convenience (integrated intake, formatted deliverable) that developers value enough to pay for over the free baseline.

## Willingness-to-pay evidence

- **Quote:** None located. No forum posts, Slack messages, or community threads contain language like "I'd pay for this" or "is there a tool that diagnoses AMPscript errors?" in the source data.
- **Competitor pricing reference:** No dedicated Salesforce cross-cloud diagnostic SaaS was identified with a public pricing page. Salesforce consulting agencies charge $100–250/hr (market rate, not a direct product analog).
- **Paid job postings:** Not assessed from source data. Salesforce developer roles routinely command $80–150k/yr salaries, confirming employer willingness to pay for Salesforce expertise in aggregate — but this does not demonstrate willingness to pay for a per-report diagnostic tool.

**Verdict on WTP:** Absent. The scoring assigned willingness_to_pay = 6 based on the general consultant billing rate inference, but no direct signal (someone paying a workaround, a competitor charging money for this specific service, or a "is there a tool" question) was present in the source material. The pain_validation.yaml threshold requires at least 1 willingness-to-pay signal; this candidate does not meet it.

## Estimated TAM / SAM

### Israel
- TAM: Salesforce has approximately 150,000+ customers globally; Israel has a significant enterprise SaaS ecosystem. Rough estimate: ~500–1,500 Israeli companies running Salesforce Marketing Cloud + Sales Cloud integrations. At $149/mo subscription = ~$1,800/yr ACV → TAM ≈ USD 900k–2.7M.
- SAM (reachable in 12 months): Salesforce developers visible on Israeli LinkedIn + Trailblazer Community → ~100–200 reachable contacts → USD 180k–360k.

### Global
- TAM: Salesforce reports ~150,000 customers; Marketing Cloud + Sales Cloud combined users estimated at 20,000–40,000 organizations. At $1,800/yr ACV → TAM ≈ USD 36M–72M.
- SAM (reachable in 12 months): Salesforce Stack Exchange has ~50,000 registered users; Trailblazer Community has millions of members but relevant cross-cloud developers number in the tens of thousands. Realistically reachable via outreach in 12 months: ~2,000–5,000 contacts → USD 3.6M–9M.

**Caveat:** These are top-down estimates. The actual addressable market for a paid report-based diagnostic (vs. free LLM alternatives) is likely a fraction of this — developers who lack LLM access or who need a polished deliverable for internal sign-off.

## Source list

- https://salesforce.stackexchange.com/questions/439751/ampscript-createsobject-error-field-integrity-exception-required-field-is-m (retrieved 2026-08-15 IDT)

---

## Validation verdict: REJECTED

**Reason:** Fails the minimum evidence bar on two counts:
1. **Fewer than 5 distinct pain quotes** — only 2 signals located, both from a single source URL.
2. **No willingness-to-pay signal** — no competitor charging for this specific service, no "is there a tool" requests, no stated willingness to pay for a workaround.

Additionally, the free LLM alternative (Claude.ai, ChatGPT) directly cannibalizes the proposed product's value proposition at zero cost to the buyer. The opportunity should be re-queued for Market Radar only if corroborating signals emerge: a Trailblazer Community thread with 20+ upvotes requesting a diagnostic tool, a paid Salesforce AppExchange listing in this space, or a Reddit/HN thread where developers explicitly ask "is there a paid service for this."