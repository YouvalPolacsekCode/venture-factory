# venture-factory

An autonomous AI Venture Factory: a closed loop of 18 specialized agents that discover, validate, build, and operate real micro-service businesses with a single human operator in the loop.

**Mission:** Stand up three live revenue experiments by end of June 2026 with no more than ~60 minutes of operator attention per day.

## Status

Phase 0 scaffold complete on 2026-05-31. Folders, configs, runbook, and templates in place. Agent code and the daily loop are next.

## Read these first

- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) — system design, the 18 agents, data substrate, control flow.
- [RUNBOOK.md](RUNBOOK.md) — how the operator runs the factory day-to-day.

## Quick start

Read `docs/ARCHITECTURE.md` end-to-end, then open Claude Code at the repo root and run the bootstrap prompt in section 13 of that document. That prompt builds out the agents from this scaffold.

## First-time setup

The Cowork scaffold left a half-initialized `.git/` because of a Windows mount permissions artifact. Run one of these from a normal shell (NOT inside the Cowork sandbox) to reset git and commit Phase 0:

```powershell
powershell -ExecutionPolicy Bypass -File scripts\setup_git.ps1
```

or, from Git Bash / WSL:

```
bash scripts/setup_git.sh
```

Also: `approval_queue/test.txt` is a stray empty file created during sandbox bootstrap. Safe to delete with `del approval_queue\test.txt` (PowerShell) before the first commit.

## Reality check

All slugs, names, prices, and example experiments anywhere in this repo are **EXAMPLE ONLY**. The factory chooses real services after running. Do not treat `experiments/example_*` folders or sample outputs as commitments — they are placeholder shapes for the agents to overwrite.
