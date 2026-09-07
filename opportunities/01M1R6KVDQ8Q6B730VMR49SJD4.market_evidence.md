# Market Evidence

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|
| 2026-09-05 | https://salesforce.stackexchange.com/questions/439811/integrating-sf-messaging-into-custom-chat-application | Forum question | Team exploring BYOB vs Enhanced Chat API for chatbot-to-human handover; unclear tradeoffs for external clients | 2 |

**Evidence gap:** A broader search for corroborating signals across Salesforce Stack Exchange, Trailblazer Community, GitHub issues on Salesforce SDKs, and developer Reddit surfaces no volume of similar complaints. The specific intersection of custom chatbot + SF Service Cloud + handover is documented in Salesforce's own developer blog and partner ecosystem, but without buyer-complaint volume.

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| Salesforce official BYOB documentation | DIY / free docs | $0 | Poorly organized; tradeoffs between API paths are not clearly explained |
| Salesforce Consulting Partners (SI partners) | Agency | $150–$350/hr consulting | Expensive; overkill for teams that just need the decision clarified |
| Salesforce Trailblazer Community posts | DIY / community | $0 | Fragmented; no authoritative decision guide exists |

## Willingness-to-pay evidence

- **No direct quotes found** indicating a team or individual paid for a solution to this specific integration question.
- **No competitor product** targeting this exact BYOB vs Enhanced Chat API decision layer was identified; nearest adjacents are general Salesforce consulting engagements.
- **No paid job postings** found specifically for this integration work at volume.
- The single source post uses "we're exploring" language — research phase, not active purchase intent.

## Estimated TAM / SAM

### Israel
- TAM: Israeli companies using Salesforce Service Cloud with custom chatbot deployments is estimated at <100 organizations (Salesforce has ~500 enterprise/mid-market customers in Israel per public partner data; subset with custom chatbot + handover use case is likely <20%). 100 × $500 one-time guide = $50K — insufficient.
- SAM (reachable in 12 months): ~20–40 teams; not commercially meaningful.

### Global
- TAM: Globally, Salesforce has ~150,000 Service Cloud customers. Custom chatbot deployments requiring handover wiring estimated at 1–3% = 1,500–4,500 teams. At $99–$299 one-time purchase: $150K–$1.3M gross potential — marginal for a product investment.
- SAM (reachable in 12 months): Organic Trailblazer Community and Stack Exchange reach might touch 200–500 teams; revenue ceiling ~$50K–$150K.

## Verdict

**REJECTED — Fail**

- Evidence count: 1 signal (minimum 5 distinct pain quotes required)
- Willingness-to-pay signals: 0 (minimum 1 required)
- Frequency assessment: rare (the intersection of custom chatbot + SF Service Cloud + handover is a niche within a niche)
- TAM is too thin to sustain a product; pain is real but incidental engineering friction, not a persistent burning problem
- Recommend: archive this candidate; if Market Radar surfaces 4+ additional corroborating signals in future scans, re-evaluate

## Source list

- https://salesforce.stackexchange.com/questions/439811/integrating-sf-messaging-into-custom-chat-application (retrieved 2026-09-05 IDT)
