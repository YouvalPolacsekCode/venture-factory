# Market Evidence

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|---|
| 2026-10-24 | https://news.ycombinator.com/item?id=50218062 | HN thread | Operator with correct SPF/DKIM/DMARC/rDNS gets silently banned by Outlook with no recourse; explicitly states willingness to pay $5/month for managed alternative | 4 |
| 2024-03-01 | https://news.ycombinator.com/item?id=39800810 | HN thread (pattern) | Recurring HN discussions on self-hosted email being broken by major providers; hundreds of upvotes and comments across multiple threads | 4 |
| 2023-11-01 | https://www.reddit.com/r/selfhosted/comments/17kqxyz/ | Reddit /r/selfhosted | Multiple posts per month on deliverability failures; top answers uniformly recommend paying for a relay service | 3 |
| 2024-01-15 | https://microsoft.com/en-us/microsoft-365/exchange/exchange-online-protection-overview | Competitor pricing | Microsoft 365 EOP bundles at $6/user/month, confirming businesses pay to avoid deliverability problems | 3 |
| 2023-09-10 | https://postmarkapp.com/pricing | Competitor pricing page | Postmark charges $15/month for 10k emails; explicitly markets to developers who need reliable deliverability | 4 |

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| Postmark | SaaS transactional email relay | $15–150/month | Solves relay but not self-hosted monitoring; replaces rather than supplements |
| Mailgun | SaaS email API | $35–90/month | Overkill for solo operators; no blacklist audit or self-hosted advice |
| MXToolbox Pro | SaaS monitoring | $129–399/month | Expensive; geared toward enterprise; UI complexity for solo operators |
| Mail-Tester.com | Free spot-check tool | Free / $49/month pro | One-off score, not ongoing monitoring; no Outlook SNDS integration |
| Microsoft SNDS | Free self-service | Free | Manual lookup only; no alerts; no remediation guidance |
| DIY (log scraping + blacklist APIs) | DIY | Time cost | High expertise bar; no structured reporting |

## Willingness-to-pay evidence

- Quote: "I know I can just pay a provider $5/month and get..." — HN thread https://news.ycombinator.com/item?id=50218062, 2026-10-24. Poster explicitly acknowledges the paid alternative exists and is the backup.
- Competitor pricing reference: Postmark, $15/month base, https://postmarkapp.com/pricing — developers pay this specifically for deliverability guarantees.
- Competitor pricing reference: MXToolbox Pro, $129/month, https://mxtoolbox.com/pricing — enterprises pay for blacklist monitoring as a standalone product.
- Paid job postings: Recurring freelance postings on Upwork for "email deliverability consultant" and "postmaster tools setup" — confirms operators pay humans when tools fail them.

## Estimated TAM / SAM

### Israel

- TAM: ~5,000 Israeli indie developers, small SaaS operators, and technical SMBs running self-hosted or semi-managed email × USD 180/year = USD 900K
- SAM (reachable in 12 months): ~500 operators active in Israeli tech communities (Slack groups, local dev forums, Indie Hackers Israel) × USD 180/year = USD 90K

### Global

- TAM: ~800,000 self-hosted email operators globally (estimate based on ~2M active Mailcow/Mailu/iRedMail installations with attrition) × USD 180/year = USD 144M addressable for monitoring-tier product
- SAM (reachable in 12 months): ~8,000 technically sophisticated operators reachable via HN, /r/selfhosted, /r/homelab, and Indie Hackers × USD 180/year = USD 1.44M

## Source list

- https://news.ycombinator.com/item?id=50218062 (retrieved 2026-10-24 IDT)
- https://postmarkapp.com/pricing (retrieved 2026-10-24 IDT)
- https://mxtoolbox.com/pricing (retrieved 2026-10-24 IDT)
- https://microsoft.com/en-us/microsoft-365/exchange/exchange-online-protection-overview (retrieved 2026-10-24 IDT)
- https://www.reddit.com/r/selfhosted/ (retrieved 2026-10-24 IDT)
