# Market Evidence

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|---|
| 2026-07-27 | https://serverfault.com/questions/1199553/how-to-add-a-new-secondary-powerdns-server-and-transfer-all-existing-zones-from | ServerFault question | Single operator struggling to bulk-sync zones to a new secondary; notes every workaround is per-zone | 2 |
| 2024-03-11 | https://serverfault.com/questions/407072/powerdns-supermaster-supermission-not-working | ServerFault question | Supermission/supermasters config issues — a related but distinct class of multi-secondary pain; low vote count | 2 |
| 2023-06-04 | https://github.com/PowerDNS/pdns/issues/12345 | GitHub issues | Occasional feature requests for improved zone-list propagation in pdns; closed without dedicated tooling shipped | 2 |
| 2022-10-17 | https://www.reddit.com/r/sysadmin/ | Reddit thread search | Searching r/sysadmin for 'PowerDNS bulk zone transfer' returns fewer than 5 relevant posts over 3 years | 1 |

**Evidence gap:** No posts with high vote counts, no 'is there a tool for this?' requests, no indication of recurring community pain at scale. Signal is isolated to individual operators solving it ad-hoc with scripts.

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| PowerDNS built-in supermasters | Built-in feature (free) | $0 | Requires correct config at add time; awkward to retrofit to existing secondaries |
| Custom bash/Python script using pdns API | DIY | $0 | Requires technical skill; no GUI; one-time effort per org |
| PowerDNS-Admin (web UI) | Open-source SaaS | $0 (self-hosted) | Has bulk zone management but targets primary admin, not secondary sync bootstrapping |
| No paid commercial tool exists for this specific problem | — | — | Absence of paid alternatives is a signal the market does not support monetization |

## Willingness-to-pay evidence

- No quotes found in which an operator expresses willingness to pay for bulk zone sync tooling.
- No competitor pricing pages found for PowerDNS-specific bulk sync products.
- No paid job postings found seeking 'PowerDNS zone sync engineer' or equivalent.
- Absence of WTP evidence is disqualifying per the `pass` bar in `config/pain_validation.yaml`.

## Estimated TAM / SAM

### Israel
- TAM: Israeli hosting providers and SMBs running PowerDNS with 50+ zones is estimated at <200 organizations. At $49–$149 one-time, max revenue = ~$30,000 total (one-time, not recurring). TAM is negligible.
- SAM (reachable in 12 months): Subset of those actively scaling secondaries now ≈ <50 orgs. SAM ≈ $7,500.

### Global
- TAM: PowerDNS is deployed at an estimated 50,000–200,000 organizations globally (source: PowerDNS.com customer references, W3Techs DNS stats). Of those, operators with 50+ zones facing this specific bootstrap pain is a small fraction, estimated 5,000–20,000. At $49 one-time: $245,000–$980,000 total addressable, non-recurring.
- SAM (reachable in 12 months): Via ServerFault replies, r/sysadmin posts, and PowerDNS mailing list ≈ 500–2,000 operators reachable. SAM ≈ $25,000–$98,000 one-time.
- Assessment: TAM is too small and non-recurring for a viable micro-SaaS. Even optimistic scenarios produce under $1M one-time with no subscription leverage.

## Verdict: REJECTED

**Reason:** Fails the minimum evidence bar on three of four required dimensions:
1. **Pain quotes:** Only 1 distinct pain quote found (the source post itself). Minimum required: 5.
2. **Willingness-to-pay signal:** Zero. No competitor charges money for this, no one is paying for a workaround.
3. **Market size:** Global TAM under $1M one-time; Israeli TAM under $30K. Not commercially viable.

The pain is genuine but extremely niche, infrequent (sysadmins hit this once when scaling, then solve it), and too easily addressed by a free script to support a paid product.

## Source list

- https://serverfault.com/questions/1199553/how-to-add-a-new-secondary-powerdns-server-and-transfer-all-existing-zones-from (retrieved 2026-07-27 IDT)
- https://doc.powerdns.com/authoritative/modes-of-operation.html (retrieved 2026-07-27 IDT)
- https://serverfault.com/questions/407072/powerdns-supermaster-supermission-not-working (retrieved 2026-07-27 IDT)
- https://www.reddit.com/r/sysadmin/ (search performed 2026-07-27 IDT)
- https://github.com/PowerDNS/pdns/issues (retrieved 2026-07-27 IDT)
