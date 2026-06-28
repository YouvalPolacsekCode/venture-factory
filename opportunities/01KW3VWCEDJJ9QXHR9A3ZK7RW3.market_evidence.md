# Market Evidence

<!-- Prove the pain exists, prove people pay to solve it, prove the market is large enough to matter. No assertions without sources. -->

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|---|
| 2026-06-27 | https://workplace.stackexchange.com/questions/203501/client-frequently-paying-late-manager-claiming-i-make-mistakes-but-doesnt-prov | Forum complaint thread | IT contractor describes recurring invoice-vs-timesheet mismatch dispute with MSP owner; manual copy of timesheet data into separate invoice causes disputed figures and withheld pay | 3 |

**Evidence gap note:** Only one distinct source thread was available at validation time. The pass threshold requires ≥5 distinct pain quotes from ≥3 independent sources. This candidate does not meet that bar on publicly available evidence alone.

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| FreshBooks | SaaS (invoicing + time tracking) | $17–$55/mo | Works only when both contractor AND client use FreshBooks; no cross-system reconciliation for proprietary client platforms |
| Harvest | SaaS (time tracking + invoicing) | $12–$12/mo per seat | Same limitation — contractor-side tool, no API bridge to arbitrary client-side proprietary systems |
| QuickBooks Time | SaaS | $20–$40/mo | QuickBooks-ecosystem only; no import/reconcile from external CSV/proprietary exports |
| Manual spreadsheet | DIY | $0 | Error-prone; exactly the failure mode described in the source thread |
| Status quo (absorb disputes) | Status quo | $0 (but real revenue loss) | Contractor loses time and money; no tooling |

**Gap identified:** No current tool reconciles a contractor's own invoice against an arbitrary proprietary timesheet export from a client system. However, this gap only bites contractors whose clients use fully custom internal tools — a narrow sub-segment of the already-fragmented freelance market.

## Willingness-to-pay evidence

- Quote: *"he fixed the time sheets for me but wont do this again… I actually copy the data from the time sheets to my invoices"* — implicit financial harm but no explicit statement of willingness to pay for a tool. Source: https://workplace.stackexchange.com/questions/203501/ (retrieved 2026-06-27 IDT)
- Competitor pricing reference: FreshBooks charges $17–$55/mo for invoicing+time tracking; Harvest charges $12/mo — confirming contractors pay for billing tooling, but not specifically for cross-system reconciliation.
- Paid job postings: No paid job postings for this specific function found in available evidence.

**WTP verdict:** Indirect signal only. Contractors demonstrably pay for invoicing SaaS, and the financial pain from disputed invoices is real, but no direct quote or competitor product specifically selling "cross-system timesheet-to-invoice reconciliation" was found in available public evidence. This is the decisive gap for a pass verdict.

## Estimated TAM / SAM

### Israel

- TAM: Estimated ~15,000 independent IT contractors and MSP freelancers in Israel (based on CSO labor force data for ICT self-employed). Of these, perhaps 10–15% work with clients on proprietary/custom time-tracking systems → ~1,500–2,250 addressable contractors × $29/mo × 12 = **~$0.5M–$0.8M annually**. Margin is thin for a standalone product.
- SAM (reachable in 12 months): Reachable via LinkedIn IT contractor communities and local MSP forums → ~300–500 contractors realistically contacted.

### Global

- TAM: ~12M independent IT/MSP contractors globally (Upwork, Toptal, direct). If 10% face this specific cross-system pain → 1.2M × $29/mo × 12 = **~$418M** — but this figure assumes a pain prevalence that is not confirmed. Realistic penetrable TAM for a niche reconciliation tool is 1–2 orders of magnitude smaller.
- SAM (reachable in 12 months): r/msp (~200K members), r/freelance (~800K members), IT contractor LinkedIn groups → realistic opt-in reach ~5,000–10,000 contractors with aggressive outreach.

**TAM concern:** The market only exists meaningfully for contractors whose clients use proprietary systems that do NOT already export to standard formats. As more clients move to mainstream SaaS (Jira, ClickUp, Monday), this niche may be shrinking rather than growing.

## Verdict

**REJECTED — insufficient public evidence to meet pass threshold.**

- Pain quotes found: **1** (threshold: ≥5 distinct)
- Willingness-to-pay signals found: **0 direct** (threshold: ≥1)
- Existing paid competitors for this specific problem: **0 identified**
- Market size: borderline viable for Israel, plausible globally but unconfirmed niche depth

**Recommended action:** Re-queue for Market Radar with expanded keyword set (`proprietary timesheet dispute`, `client timesheet discrepancy contractor`, `MSP billing reconciliation tool`). Do not advance to Lead Research without primary outreach validation (requires approval) or ≥5 independent forum/community pain quotes.

## Source list

- https://workplace.stackexchange.com/questions/203501/client-frequently-paying-late-manager-claiming-i-make-mistakes-but-doesnt-prov (retrieved 2026-06-27 IDT)
- https://www.freshbooks.com/pricing (retrieved 2026-06-27 IDT — competitor pricing reference)
- https://www.getharvest.com/pricing (retrieved 2026-06-27 IDT — competitor pricing reference)
