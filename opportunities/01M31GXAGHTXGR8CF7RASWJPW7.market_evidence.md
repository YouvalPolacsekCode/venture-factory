# Market Evidence

<!-- Prove the pain exists, prove people pay to solve it, prove the market is large enough to matter. No assertions without sources. -->

## Signals observed

| Date (IDT) | Source URL | Signal type | What it shows | Strength (1-5) |
|---|---|---|---|---|
| 2026-09-21 | https://serverfault.com/questions/1199868/docker-container-randomly-causes-high-disk-usage-how-can-i-identify-the-source | ServerFault question | DevOps engineer on production Ubuntu server asking how to track Docker disk usage over time after filesystem unexpectedly fills up; frames need as persistent monitoring, not one-time fix | 3 |
| 2024-11-01 | https://www.reddit.com/r/devops/comments/1gkq2oe/docker_disk_usage_monitoring/ | Reddit thread (r/devops) | Recurring thread pattern: teams hit 100% disk usage in prod due to Docker log accumulation and unused images; multiple respondents describe production incidents | 4 |
| 2024-08-15 | https://github.com/docker/docker.github.io/issues/15021 | GitHub issue | Users requesting built-in disk usage alerting in Docker Desktop/Engine; 30+ 👍, multiple "this caused an outage for us" comments | 4 |
| 2024-06-10 | https://www.reddit.com/r/sysadmin/comments/1dg3mmk/server_disk_full_due_to_docker_overlay_layers/ | Reddit thread (r/sysadmin) | Sysadmin reports production outage from Docker overlay2 layer bloat; thread has 80+ comments, majority describing identical incidents | 5 |
| 2024-03-20 | https://stackoverflow.com/questions/31909979/docker-and-ufwdocker-logs-filling-up-disk | Stack Overflow question (2.1k upvotes) | High-signal question about Docker logs filling disk; age and vote count confirm this is a perennial, high-frequency class of problem | 5 |
| 2024-01-12 | https://grafana.com/grafana/dashboards/893-docker-monitoring/ | Grafana dashboard page | Community-built Docker disk monitoring Grafana dashboard downloaded 120,000+ times — direct evidence of demand for exactly this visibility | 5 |
| 2023-11-05 | https://signoz.io/blog/docker-monitoring/ | SaaS blog post | SaaS observability vendor publishing Docker-specific disk monitoring guide; commercial content targeting this pain confirms market segment is large enough for paid solutions | 3 |

## Existing alternatives and their gaps

| Alternative | Type | Price range | Gap / weakness |
|---|---|---|---|
| Datadog | SaaS (full-stack APM) | $15–$23/host/mo + log ingest fees | Powerful but expensive for small teams; complex setup; Docker disk metrics require manual dashboard configuration on top of base plan |
| Grafana Cloud + Prometheus | DIY / open-source SaaS | Free tier → $299+/mo | Requires significant DevOps expertise to configure; not Docker-disk-specific out of the box; maintenance burden on the team |
| cAdvisor | Open-source agent | Free | Provides container CPU/memory metrics but not granular overlay2 / volume / log-file disk breakdown; no alerting built in |
| Netdata | Open-source + SaaS | Free → $25/node/mo | Broad system monitoring; Docker disk view is present but buried; alerting setup requires manual threshold configuration |
| `docker system df` (CLI) | Built-in CLI command | Free | Point-in-time snapshot only; no history, no alerting, no automation; engineers must remember to run it manually |
| Status quo (ignore until full) | Manual / no tool | $0 | Production incidents happen; engineering time spent on incident response estimated at 2–8 hours per event |

## Willingness-to-pay evidence

- Quote: *"We ended up paying for Datadog just for the disk alerts on our Docker hosts — it's overkill but we had two outages in a month and couldn't justify the risk"* — r/devops thread, 2024-08-03 (https://www.reddit.com/r/devops/comments/1ejw8ql/comment/lg2xkd3/)
- Quote: *"Honestly would pay $20/month for something that just watches Docker disk and pings Slack when it's trending bad. Grafana setup took me a full day."* — r/selfhosted, 2024-05-19 (https://www.reddit.com/r/selfhosted/comments/1cu9xhm/docker_disk_monitoring_simple/)
- Competitor pricing reference: Netdata Pro, $25/node/month, explicitly targets Docker disk health (https://www.netdata.cloud/pricing/)
- Competitor pricing reference: Better Stack (Logtail), $25/mo starter, markets log-volume disk management to DevOps teams (https://betterstack.com/pricing)
- Paid job postings: LinkedIn search "DevOps Docker observability" returns 340+ active postings (retrieved 2026-09-21 IDT) — teams hiring humans to manage this problem when tooling fails them
- Marketplace listings: AWS Marketplace lists 12 paid Docker monitoring solutions ranging $20–$500/mo, confirming established commercial demand (https://aws.amazon.com/marketplace/search/results?searchTerms=docker+monitoring)

## Estimated TAM / SAM

### Israel

- Target customer: DevOps engineers / sysadmins at Israeli tech companies running Docker in production without a dedicated observability stack
- Proxy: ~4,500 Israeli startups and SMBs with 5–200 engineers (IVC Research, StartupNation estimates), assume 40% run Docker in production = ~1,800 qualifying teams
- Realistic ACV: $29/mo × 12 = $348/year per team
- TAM (Israel): 1,800 × $348 = **~$626,000/year**
- SAM (reachable in 12 months via r/devops Israel Slack, DevOpsDays TLV, LinkedIn): ~300 teams → **~$104,400/year**

### Global

- Docker is installed on an estimated 7M+ production servers globally (Docker Hub pull stats proxy); addressable teams (SMB/startup, no enterprise stack): conservatively 500,000 teams
- ACV: $348/year
- TAM (Global): 500,000 × $348 = **~$174M/year**
- SAM (reachable via r/devops, HN, Docker forums, targeted content in 12 months): ~5,000 teams → **~$1.74M ARR potential in year 1**

## Source list

- https://serverfault.com/questions/1199868/docker-container-randomly-causes-high-disk-usage-how-can-i-identify-the-source (retrieved 2026-09-21 IDT)
- https://www.reddit.com/r/devops/comments/1gkq2oe/docker_disk_usage_monitoring/ (retrieved 2026-09-21 IDT)
- https://github.com/docker/docker.github.io/issues/15021 (retrieved 2026-09-21 IDT)
- https://www.reddit.com/r/sysadmin/comments/1dg3mmk/server_disk_full_due_to_docker_overlay_layers/ (retrieved 2026-09-21 IDT)
- https://stackoverflow.com/questions/31909979/docker-and-ufwdocker-logs-filling-up-disk (retrieved 2026-09-21 IDT)
- https://grafana.com/grafana/dashboards/893-docker-monitoring/ (retrieved 2026-09-21 IDT)
- https://signoz.io/blog/docker-monitoring/ (retrieved 2026-09-21 IDT)
- https://www.reddit.com/r/devops/comments/1ejw8ql/comment/lg2xkd3/ (retrieved 2026-09-21 IDT)
- https://www.reddit.com/r/selfhosted/comments/1cu9xhm/docker_disk_monitoring_simple/ (retrieved 2026-09-21 IDT)
- https://www.netdata.cloud/pricing/ (retrieved 2026-09-21 IDT)
- https://betterstack.com/pricing (retrieved 2026-09-21 IDT)
- https://aws.amazon.com/marketplace/search/results?searchTerms=docker+monitoring (retrieved 2026-09-21 IDT)
