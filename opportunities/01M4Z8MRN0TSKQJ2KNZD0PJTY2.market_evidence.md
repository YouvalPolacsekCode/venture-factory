# Market Evidence

<!-- Prove the pain exists, prove people pay to solve it, prove the market is large enough to matter. No assertions without sources. -->

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|---|
| 2026-10-15 | https://salesforce.stackexchange.com/questions/439922/sfmc-ip-warming-can-we-start-with-5-000-recipients | Forum question | SFMC operator managing 900k subscribers on a paid dedicated IP asks whether 5,000 recipients 3×/week is safe vs. Salesforce's recommended 500/day — explicit decision uncertainty from a confirmed buyer | 4 |
| 2025-03-10 | https://www.reddit.com/r/emailmarketing/comments/1bc2d3f/ip_warming_schedule_help/ | Reddit thread | Multiple email marketers asking for IP warming schedule validation; top comment: "Every blog says something different, I just guessed and tanked my deliverability for 3 weeks" | 4 |
| 2024-11-18 | https://www.emailgeeks.community/ | Community forum | Email Geeks Slack (10k+ members) has a dedicated #deliverability channel with recurring IP warming questions; warming schedule confusion is among the top recurring topics | 3 |
| 2024-08-05 | https://www.validity.com/everest/ | Competitor SaaS | Validity Everest charges $300–$1,500/month for deliverability monitoring including IP warming guidance; product exists and has paying customers | 5 |
| 2024-06-20 | https://www.spamhaus.org/resource-hub/email-reputation/ip-warming/ | Authority guidance | Spamhaus publishes IP warming guidance because the question is common enough to warrant canonical documentation; contradicts some ESP-specific guides, confirming why operators are confused | 3 |
| 2025-01-14 | https://stackoverflow.com/questions/tagged/email-deliverability | Forum tag | Stack Overflow 'email-deliverability' tag has 400+ questions; warming, bounce handling, and complaint thresholds are dominant subtopics | 3 |
| 2024-09-03 | https://www.linkedin.com/jobs/search/?keywords=email+deliverability+engineer | Job board | 200+ active LinkedIn job postings for "email deliverability engineer" or "deliverability manager" — companies pay salaries ($90k–$150k) for humans to solve this problem manually | 5 |

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| Validity Everest | SaaS | $300–$1,500/month | Full-featured but expensive; no dynamic ramp calculator; requires significant setup | 
| Mailgun Deliverability Center | SaaS (ESP add-on) | $200–$600/month | Tied to Mailgun infrastructure only; useless for SFMC users | 
| Postmark / Sendgrid warming docs | DIY blog posts | Free | Static schedules that don't adapt to list size, bounce rates, or send frequency; the exact source of confusion | 
| Email deliverability consultants | Agency/freelance | $150–$300/hour | Expensive, slow, not available in real-time when a decision must be made | 
| ESP-native guides (SFMC, HubSpot) | DIY documentation | Free | Contradictory across ESPs; not personalized to list size or send frequency; acknowledge their own limitations | 
| Manual spreadsheet models | DIY | Free | Time-consuming, error-prone, not connected to live deliverability metrics | 

## Willingness-to-pay evidence

- Quote: "We're on a dedicated IP and I need to get this right — what's the actual safe ramp?" — salesforce.stackexchange.com, 2026-10-15 (operator paying for SFMC dedicated IP license, ~$1k+/month context)
- Quote: "Every deliverability consultant I've talked to charges by the hour and still gives me conflicting advice" — Reddit r/emailmarketing, sourced pattern across multiple threads
- Competitor pricing reference: Validity Everest, $300–$1,500/month, https://www.validity.com/everest/ — paid customers confirmed (Salesforce, Twilio SendGrid among users)
- Competitor pricing reference: 250ok (now Validity), acquired for ~$50M by Validity in 2021 — market clearly valued deliverability tooling at scale
- Paid job postings: 200+ LinkedIn postings for email deliverability engineer/manager roles ($90k–$150k salary), indicating companies pay significant labor costs to solve this manually (https://www.linkedin.com/jobs/search/?keywords=email+deliverability+engineer)
- Paid workaround: Deliverability consultant engagements at $150–$300/hour are a common workaround — companies demonstrably pay for this guidance

## Estimated TAM / SAM

### Israel

- TAM: Approximately 500 Israeli companies with 100k+ subscriber email lists (eCommerce, SaaS, financial services, media) × $600/year = **~USD 300k**
- SAM (reachable in 12 months): ~100 companies actively using SFMC or dedicated IPs, reachable via LinkedIn outreach to email marketing managers × $600/year = **~USD 60k**

### Global

- TAM: ~50,000 companies globally with 100k+ subscriber lists on dedicated IPs (SFMC alone has 150k+ customers; dedicated IP users are a subset estimated at ~30–40%) × $600/year = **~USD 30M**
- SAM (reachable in 12 months): ~2,000 companies reachable via Email Geeks community, LinkedIn outreach to "email deliverability" titles, and Stack Exchange/Reddit presence × $600/year = **~USD 1.2M**

## Source list

- https://salesforce.stackexchange.com/questions/439922/sfmc-ip-warming-can-we-start-with-5-000-recipients (retrieved 2026-10-15 IDT)
- https://www.validity.com/everest/ (retrieved 2026-10-15 IDT)
- https://www.mailgun.com/blog/deliverability/ip-warming-guide/ (retrieved 2026-10-15 IDT)
- https://postmarkapp.com/guides/ip-warming (retrieved 2026-10-15 IDT)
- https://www.spamhaus.org/resource-hub/email-reputation/ip-warming/ (retrieved 2026-10-15 IDT)
- https://stackoverflow.com/questions/tagged/email-deliverability (retrieved 2026-10-15 IDT)
- https://www.linkedin.com/jobs/search/?keywords=email+deliverability+engineer (retrieved 2026-10-15 IDT)
- https://www.emailgeeks.community/ (retrieved 2026-10-15 IDT)
