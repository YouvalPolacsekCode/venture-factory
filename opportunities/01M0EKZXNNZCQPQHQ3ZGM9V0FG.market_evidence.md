# Market Evidence

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|---|
| 2026-08-20 | https://salesforce.stackexchange.com/questions/439759/external-credential-with-google-auth-provider-stops-refreshing-oauth-token-after | Stack Exchange question | Salesforce admin describes silent OAuth token expiry breaking Google Calendar integration after 1.5h–2 days, with no error or audit trail; extensive config detail suggests real production incident | 3 |

**Evidence gap:** Only one distinct signal source found. The pain_validation threshold requires ≥5 distinct pain quotes from ≥3 independent sources. This candidate has one thread, one author, and no corroborating community discussion, competitor complaints, or adjacent forum activity discovered.

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| Salesforce native debug logs | DIY / built-in | Free (included) | Do not surface silent credential failures; require manual polling and expertise to interpret |
| Datadog / Splunk log monitoring | SaaS | $15–$50/host/mo | General-purpose; no Salesforce-specific OAuth credential health awareness out of the box |
| Custom Apex scheduled jobs | DIY dev time | $150–$250/hr dev cost | Bespoke, fragile, requires Salesforce developer; not a productized solution |
| Workato / MuleSoft error handling | Integration platform | $10k–$50k+/yr | Heavy-weight; overkill for credential health monitoring; expensive |

## Willingness-to-pay evidence

- Quote: *(none found)* — No forum participant expressed desire to pay for a monitoring tool; discussion focused on configuration fixes.
- Competitor pricing reference: No direct competitor product for Salesforce OAuth credential health monitoring identified. Adjacent tools (Datadog, Splunk) address general observability but are not purpose-built for this.
- Paid job postings: No job postings found referencing Salesforce OAuth credential monitoring as a discrete responsibility.

**WTP verdict:** Zero willingness-to-pay signals found. The scoring notes that WTP requires corroboration; none exists. Buyers in this space are more likely to expect Salesforce to fix the platform bug than to pay for a workaround tool.

## Estimated TAM / SAM

### Israel

- TAM: Israeli companies running Salesforce + Google Workspace integrations using 2nd-gen External Credentials is estimated at <200 orgs (Salesforce has ~500 enterprise customers in Israel per public reports; a fraction use 2nd-gen External Credentials specifically with Google OAuth). At a hypothetical $49/mo × 200 orgs = ~$117k/yr. Insufficient.
- SAM (reachable in 12 months): ~50 orgs reachable via LinkedIn + Salesforce community filtering. Revenue potential: ~$29k/yr.

### Global

- TAM: Salesforce has ~150,000 enterprise customers globally. Orgs using 2nd-gen External Credentials (a relatively new, less-adopted feature) with Google OAuth is estimated at ~5,000–10,000. At $49/mo × 7,500 = ~$4.4M/yr theoretical ceiling.
- SAM (reachable in 12 months): Salesforce Stack Exchange has ~50k registered users; Trailblazer Community has ~3M members but the specific segment is a small fraction. Realistically reachable in 12 months: ~500 orgs via community outreach + cold email. Revenue potential: ~$294k/yr — below typical SaaS viability threshold for a standalone product.

**TAM note:** The TAM is structurally constrained by the specificity of the trigger condition (2nd-gen External Credentials + Google OAuth). If Salesforce patches the underlying bug (likely given forum visibility), the market evaporates.

## Source list

- https://salesforce.stackexchange.com/questions/439759/external-credential-with-google-auth-provider-stops-refreshing-oauth-token-after (retrieved 2026-08-20 IDT)

---

## Verdict: FAIL

**Reason:** Does not meet minimum evidence bar.
- Distinct pain quotes: 1 (requires ≥5)
- Independent sources: 1 (requires ≥3)
- Willingness-to-pay signals: 0 (requires ≥1)
- Market size: Structurally narrow; dependent on a specific Salesforce platform bug that may be patched

**Recommendation:** Re-queue for Market Radar only if corroborating signals emerge (e.g., multiple Trailblazer Community threads, a Salesforce Known Issues entry with significant votes, or competitor tools addressing this gap). Do not advance to Lead Research.
