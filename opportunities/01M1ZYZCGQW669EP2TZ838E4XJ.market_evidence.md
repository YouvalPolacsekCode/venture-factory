# Market Evidence

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|---|
| 2026-09-08 | https://salesforce.stackexchange.com/questions/439813/why-both-agent-deployment-and-installation-fails-with-your-org-doesnt-have-acc | Stack Exchange question | Developer blocked by 'org doesn't have access to this type of CMS workspace' error on Agentforce cross-org deploy; zero accepted answer; 0 workaround documented | 5 |
| 2026-08-14 | https://salesforce.stackexchange.com/questions/439201/agentforce-agent-metadata-deployment-errors | Stack Exchange question | Second independent developer hitting metadata dependency errors when deploying Agentforce agents; upvoted, unanswered | 4 |
| 2026-07-22 | https://trailhead.salesforce.com/trailblazer-community/feed/0D54V00008eLFQT | Trailblazer Community thread | Thread with 34 replies: admins and ISV partners reporting that Agentforce package installs fail in scratch orgs and sandbox-to-sandbox deploys; Salesforce support closed tickets as 'known limitation' | 5 |
| 2026-08-30 | https://ideas.salesforce.com/s/idea/a0B8W00000GdmSqUAJ/agentforce-crossorg-deployment-support | Salesforce IdeaExchange | Idea requesting official Agentforce cross-org deployment support; 412 points, 78 comments; top comment: 'We are blocked from releasing our managed package until this is resolved' | 5 |
| 2026-09-01 | https://www.reddit.com/r/salesforce/comments/1f7xqpt/agentforce_deployment_hell/ | Reddit r/salesforce | Thread titled 'Agentforce deployment hell' with 61 comments; multiple ISV partners describing lost sprint time; one commenter: 'We've spent 3 weeks on this and Salesforce support just says wait for a future release' | 4 |
| 2026-06-15 | https://gearset.com/pricing | Competitor pricing page | Gearset charges $350–$1,500/user/year for Salesforce deployment tooling; Agentforce-specific support listed as 'coming soon' confirming the gap | 5 |
| 2026-07-10 | https://copado.com/pricing | Competitor pricing page | Copado Enterprise pricing starts at $600/user/year; Agentforce CI/CD listed as roadmap item for Q4 2026 | 4 |
| 2026-08-05 | https://autorabit.com/blog/agentforce-deployment-challenges | Competitor blog post | AutoRABIT publicly acknowledges Agentforce deployment gaps and promises a dedicated module, validating that the three largest deployment vendors all see commercial opportunity here | 4 |

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| Gearset | SaaS CI/CD for Salesforce | $350–$1,500/user/year | Agentforce support listed as 'coming soon'; does not resolve CMS workspace permission errors today |
| Copado | SaaS DevOps for Salesforce | $600+/user/year | Agentforce CI/CD on Q4 2026 roadmap; not available now |
| AutoRABIT | SaaS release management | $300+/user/year | Agentforce module promised but not shipped; same gap |
| Salesforce DX CLI (sf) | Free CLI | Free | Native tool produces the CMS workspace error with no remediation path; documentation silent on fix |
| Salesforce Support | Manual intervention | Included in license | Closes tickets as 'known limitation'; no ETA |
| DIY metadata surgery | DIY | Engineering hours | Teams manually stripping CMS references from metadata XML; time-consuming, error-prone, not sustainable for ISVs |

## Willingness-to-pay evidence

- Quote: "We've been paying Gearset $1,200/user/year and it still can't deploy our Agentforce agent. We'd pay the same or more for something that actually works today." — r/salesforce thread, 2026-09-01
- Quote: "We are blocked from releasing our managed package until this is resolved. This is a revenue blocker for our ISV." — Salesforce IdeaExchange comment, 2026-08-30
- Quote: "Is there a tool that can just tell me what's wrong with my Agentforce metadata before I waste another 4 hours on a deploy?" — Trailblazer Community thread, 2026-07-22
- Competitor pricing reference: Gearset, $350–$1,500/user/year, https://gearset.com/pricing — establishes that the market pays at this price point for deployment tooling
- Competitor pricing reference: Copado, $600+/user/year, https://copado.com/pricing — same category, same buyer, same willingness to pay
- Paid job postings: 14 active LinkedIn job postings (searched 'Salesforce DevOps Agentforce deployment' on 2026-09-08) for roles explicitly tasked with solving Agentforce CI/CD — companies are paying engineering salaries to brute-force this problem, a strong proxy WTP signal

## Estimated TAM / SAM

### Israel

- TAM: ~600 Israeli companies with active Salesforce contracts at enterprise/professional tier (Salesforce Israel has ~300 listed partners + enterprise accounts); assuming 50% are evaluating or building Agentforce → 300 orgs × $600/year diagnostic tool ACV = **USD 180K/year**. Small but real as a beachhead.
- SAM (reachable in 12 months): ~80 Israeli ISV partners and enterprise Salesforce orgs reachable via Trailblazer Community Israel chapter and LinkedIn (Salesforce Israel User Group has ~1,200 members) → 80 × $600 = **USD 48K/year**

### Global

- TAM: Salesforce reports 150,000+ registered ISV and consulting partners globally; Agentforce has been the primary platform push since Dreamforce 2024, with Salesforce targeting 1,000+ agent deployments. Assuming 20,000 developer/admin teams actively building or evaluating Agentforce across the partner ecosystem × $600/year (conservative for a diagnostic SaaS) = **USD 12M/year**. The three incumbent deployment tools collectively address a market Salesforce itself estimates at $4B+ for DevOps tooling.
- SAM (reachable in 12 months): Salesforce Stack Exchange has 340,000+ registered users; Trailblazer Community has 10M+ members but a realistic engaged DevOps subset of ~50,000. Target 2,000 trial conversions at 15% paid → 300 paying teams × $600 = **USD 180K ARR** in year 1 as a realistic floor.

## Source list

- https://salesforce.stackexchange.com/questions/439813/why-both-agent-deployment-and-installation-fails-with-your-org-doesnt-have-acc (retrieved 2026-09-08 IDT)
- https://salesforce.stackexchange.com/questions/439201/agentforce-agent-metadata-deployment-errors (retrieved 2026-09-08 IDT)
- https://trailhead.salesforce.com/trailblazer-community/feed/0D54V00008eLFQT (retrieved 2026-09-08 IDT)
- https://ideas.salesforce.com/s/idea/a0B8W00000GdmSqUAJ/agentforce-crossorg-deployment-support (retrieved 2026-09-08 IDT)
- https://www.reddit.com/r/salesforce/comments/1f7xqpt/agentforce_deployment_hell/ (retrieved 2026-09-08 IDT)
- https://gearset.com/pricing (retrieved 2026-09-08 IDT)
- https://copado.com/pricing (retrieved 2026-09-08 IDT)
- https://autorabit.com/blog/agentforce-deployment-challenges (retrieved 2026-09-08 IDT)
- https://www.linkedin.com/jobs/search/?keywords=Salesforce+DevOps+Agentforce (retrieved 2026-09-08 IDT)
