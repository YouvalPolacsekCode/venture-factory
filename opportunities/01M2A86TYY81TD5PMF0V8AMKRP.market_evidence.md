# Market Evidence

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|---|
| 2026-09-12 | https://salesforce.stackexchange.com/questions/439830/what-is-the-1ps-key-prefix-partitionlevelscheme-and-can-it-be-managed-throug | Forum question | Single developer hit an undocumented `1ps` key prefix while automating sandbox management; notes that regular SOQL fails and Anonymous Apex is needed as a workaround | 2 |

**Evidence gap:** Only one distinct signal located. The bar requires ≥5 distinct pain quotes. No corroborating Reddit threads, Salesforce Trailblazer Community posts, HN threads, or AppExchange reviews referencing this specific pain were found in the candidate data or source metadata.

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| Salesforce official docs / Tooling API reference | Free documentation | $0 | Omits undocumented/internal key prefixes by design |
| Community key-prefix lists (GitHub gists, blog posts) | DIY / community | $0 | Manually maintained, frequently stale, no API access |
| Salesforce Inspector (Chrome extension) | Free tool | $0 | Surfaces object metadata interactively but does not maintain a queryable registry or alert on undocumented changes |
| Metazoa Snapshot / Org Surgeon | SaaS | ~$75–$300/mo | Org comparison and metadata backup; not focused on key-prefix documentation |

## Willingness-to-pay evidence

- **No direct WTP signal found.** The source question relies on free community workarounds (Anonymous Apex). No competitor charges specifically for a key-prefix reference layer.
- **Indirect signal only:** Teams managing multiple sandboxes are on enterprise Salesforce licenses (≥$150/user/mo), implying budget exists, but no evidence they would pay a third party for this specific reference versus tolerating occasional debugging.
- Paid job postings: none found for this specific skill/tool requirement.

## Estimated TAM / SAM

### Israel
- TAM: Salesforce enterprise orgs in Israel ≈ 200–400 companies × $600/year = $120K–$240K (too small to matter as a standalone product)
- SAM (reachable in 12 months): ~50–100 Salesforce DevOps engineers; ACV too low to justify independent validation effort

### Global
- TAM: ~50,000 Salesforce orgs with active DevOps/sandbox automation practices × $600/year = ~$30M (theoretical ceiling)
- SAM (reachable in 12 months): Realistically reachable via Trailblazer Community and SFDC Slack, but niche within a niche — developers hit this specific pain only occasionally, reducing effective conversion rates sharply

## Verdict

**REJECTED — insufficient evidence.** Only 1 pain signal located vs. the 5-quote minimum. No willingness-to-pay signal. Free workarounds are adequate for the infrequent occurrence of this pain. Recommend Market Radar re-scan focused on broader Salesforce DevOps tooling pain (sandbox refresh time, metadata deployment failures) where corroborated signal exists.

## Source list

- https://salesforce.stackexchange.com/questions/439830/what-is-the-1ps-key-prefix-partitionlevelscheme-and-can-it-be-managed-throug (retrieved 2026-09-12 IDT)
