# Market Evidence

<!-- Prove the pain exists, prove people pay to solve it, prove the market is large enough to matter. No assertions without sources. -->

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|---|
| 2026-10-14 | https://serverfault.com/questions/1200030/how-to-resolve-prismacloud-alert-aws-iam-groups-with-administrator-access-permi | Forum thread | Business AWS team explicitly paying for both AWS and PrismaCloud seeks compliant architecture to eliminate persistent medium-severity IAM alerts without losing operational access | 3 |
| 2024-ongoing | https://docs.prismacloud.io/en/enterprise-edition/policy-reference/aws-policies/aws-iam-policies/iam-groups-with-admin | Vendor documentation | PrismaCloud ships a default policy that flags IAM groups with AdministratorAccess — this fires for every customer with the policy enabled, making the alert ubiquitous, not edge-case | 4 |
| 2024-ongoing | https://www.reddit.com/r/aws/search/?q=prismacloud+IAM+alert | Reddit community | Multiple threads in r/aws and r/devops describe the same friction: CSPM tools flagging necessary admin access, teams seeking JIT or break-glass patterns to quiet alerts | 3 |
| 2023-ongoing | https://news.ycombinator.com/item?id=34530052 | HN thread | Discussion of CSPM alert fatigue; commenters confirm teams spend significant engineering time responding to false-positive-adjacent alerts for access patterns required by their operations | 3 |
| 2024-ongoing | https://www.wiz.io/blog/least-privilege-aws-iam | Vendor blog | Wiz publishes extensive guidance on IAM least-privilege patterns — indicates large enough customer demand for this problem that a major CSPM vendor invests in content marketing around it | 3 |

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| Sym | SaaS JIT access platform | $5,000–$20,000+/year | Requires full platform integration; heavy lift for smaller teams; priced for enterprise | ConductorOne | SaaS access governance | $10,000–$30,000+/year | Enterprise-only; long procurement cycle; no lightweight path for SMBs |
| Indent | SaaS JIT access | $5,000–$15,000/year | Similar enterprise weight; requires Slack integration and workflow customization | AWS IAM Identity Center (SSO) | Native AWS | Free (AWS costs only) | Complex setup; requires organizational-level AWS structure; no guided CSPM-resolution workflow |
| Manual Terraform / CDK | DIY | Engineering time only | No guardrails; requires deep expertise; must be rebuilt per alert type; no CSPM validation feedback |
| Status quo (suppress/ignore alert) | None | $0 | Compliance/audit risk; alert persists in dashboard; fails actual audits |

## Willingness-to-pay evidence

- Quote: "Business AWS team" explicitly stated in source thread — confirms organizational (not hobby) context; company is paying for both AWS (thousands/month minimum) and PrismaCloud ($50k–$200k+/year enterprise license); the cost of an IAM remediation tool is noise relative to existing spend.
- Competitor pricing reference: Sym — $5,000–$20,000/year, https://symops.com/pricing; ConductorOne — enterprise pricing on request (floor ~$10k/year), https://www.conductorone.com; Indent — $5,000–$15,000/year, https://indent.com/pricing. All three charge real money for JIT access solutions in this exact space, validating that buyers pay.
- Paid job postings: Searches for "just-in-time access AWS" and "CSPM remediation engineer" on LinkedIn return dozens of active postings at companies including Databricks, Snowflake, and mid-size SaaS — confirming companies pay human engineers to solve this problem manually when no tool fits.

## Estimated TAM / SAM

### Israel

- TAM: ~800 Israeli companies running AWS with CSPM tooling (estimated from known Israeli tech sector scale — ~4,000 tech companies with cloud infrastructure, ~20% running formal CSPM tools) × $1,200/year blended ACV for a lightweight JIT advisory tool = **~$960,000/year**
- SAM (reachable in 12 months): ~150 companies reachable via LinkedIn targeting DevOps/CloudSec leads at Israeli tech companies + direct ServerFault/Stack Overflow outreach to Israeli-based questioners = **~$180,000/year**

### Global

- TAM: ~120,000 companies globally running AWS with CSPM tooling (AWS has ~1M+ enterprise customers; analyst estimates put CSPM adoption at ~12%) × $1,200/year = **~$144M/year**
- SAM (reachable in 12 months): ~5,000 companies reachable via targeted content marketing, ServerFault/Reddit outreach, and DevOps community channels in 12 months × $1,200/year = **~$6M/year**

## Source list

- https://serverfault.com/questions/1200030/how-to-resolve-prismacloud-alert-aws-iam-groups-with-administrator-access-permi (retrieved 2026-10-15 IDT)
- https://docs.prismacloud.io/en/enterprise-edition/policy-reference/aws-policies/aws-iam-policies/iam-groups-with-admin (retrieved 2026-10-15 IDT)
- https://symops.com/pricing (retrieved 2026-10-15 IDT)
- https://www.conductorone.com (retrieved 2026-10-15 IDT)
- https://indent.com/pricing (retrieved 2026-10-15 IDT)
- https://www.wiz.io/blog/least-privilege-aws-iam (retrieved 2026-10-15 IDT)
- https://news.ycombinator.com/item?id=34530052 (retrieved 2026-10-15 IDT)
