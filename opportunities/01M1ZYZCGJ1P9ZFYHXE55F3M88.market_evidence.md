# Market Evidence

<!-- Prove the pain exists, prove people pay to solve it, prove the market is large enough to matter. No assertions without sources. -->

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|---|
| 2026-09-08 | https://serverfault.com/questions/1199790/azure-entra-id-password-writeback-fails | ServerFault thread | IT admin describes SSPR writeback silently failing: config toggle disappears, audit log shows nothing on failure, users cannot self-reset — must escalate to helpdesk | 3 |

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| Cayosoft Guardian | SaaS — AD management & monitoring | $3,000–$15,000+/year (est.) | Broad AD scope; no SSPR-specific writeback health dashboard |
| Semperis Directory Services Protector | SaaS — AD security & recovery | $10,000+/year (enterprise) | Security and recovery focus; not a writeback diagnostics tool |
| AvePoint | SaaS — Microsoft 365 management | $5,000+/year (enterprise) | Data governance focus; SSPR not a primary feature |
| Microsoft Entra audit logs (native) | Built-in | Included in Entra P1/P2 licence | Logs exist but provide no writeback-specific health alerting or root-cause diagnosis |
| Status quo: helpdesk escalation | Manual | IT labour cost ($25–$60/ticket est.) | No self-service resolution; each failed SSPR generates a manual ticket |

## Willingness-to-pay evidence

- Quote: _(No direct willingness-to-pay quote retrieved from the single source thread. No "is there a tool that..." phrasing or competitor pricing reference found in the source post.)_
- Competitor pricing reference: Cayosoft, Semperis, AvePoint charge $3,000–$15,000+/year for adjacent AD management tooling — confirms enterprise budget exists for this category, but not specifically for SSPR/writeback diagnostics.
- Paid job postings: Not retrieved in this validation cycle.

**Assessment:** Indirect willingness-to-pay signal only (adjacent category spend). No direct quote, no specific tool request, no marketplace listing for this exact pain. Does not meet the single-signal threshold required for `pass`.

## Estimated TAM / SAM

### Israel

- TAM: Approximately 2,000–4,000 Israeli mid-market enterprises running hybrid AD + Entra ID × USD 600/year = USD 1.2M–2.4M (rough estimate; no primary source retrieved)
- SAM (reachable in 12 months): ~200–400 IT admins reachable via LinkedIn + local IT communities

### Global

- TAM: Estimated 300,000–500,000 mid-market enterprises globally running hybrid AD × USD 600/year = USD 180M–300M (category-level estimate; Entra ID has 700M+ MAU but mid-market hybrid subset is smaller)
- SAM (reachable in 12 months): ~5,000–10,000 IT admins reachable via ServerFault, r/sysadmin, r/azure, LinkedIn in first 12 months

## Verdict

**REJECTED — Insufficient evidence volume + operational autonomy constraint**

Evidence count: 1 source thread (floor: 5 distinct pain quotes). Willingness-to-pay signal: indirect only (adjacent competitor pricing). Build constraint: per-tenant SSPR diagnostics require live Azure Graph API access; a log-upload-only MVP provides insufficient diagnostic value and is unlikely to retain paying customers. Operational autonomy cannot reach the required floor (7) without agent-level Entra integration that exceeds solo-founder buildability.

Recommend: Market Radar re-scan targeting r/sysadmin, r/azure, Microsoft Tech Community, and Entra feedback forums for corroborating volume before re-queuing.

## Source list

- https://serverfault.com/questions/1199790/azure-entra-id-password-writeback-fails (retrieved 2026-09-08 IDT)
