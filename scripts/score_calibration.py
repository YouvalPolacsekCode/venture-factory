#!/usr/bin/env python3
"""Scoring calibration benchmark (prompt D, Workstream 2).

Scores the hand-crafted fixtures in config/fixtures/scoring_calibration/ with the
REAL opportunity_scoring model + contract, and checks that a genuinely strong,
solo-viable idea CAN reach the unchanged build bar (min_total_to_build, 6.5) AND
clear build_gates — verifying the 0-10 range is usable and the strict bar is
reachable by construction. Makes one cheap API call (cache on).

Usage:  uv run python scripts/score_calibration.py   (or `uv run score-calibration`)
Exit 0 if at least one STRONG fixture reaches >=6.5 AND passes build_gates.
"""
import json
import os
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import run_agent as R  # noqa: E402
import yaml  # noqa: E402
from dotenv import load_dotenv  # noqa: E402

FIX_DIR = REPO_ROOT / "config" / "fixtures" / "scoring_calibration"


def main() -> int:
    load_dotenv(REPO_ROOT / ".env")
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("ERROR: ANTHROPIC_API_KEY required (see .env.example)", file=sys.stderr)
        return 2

    fixtures = [json.loads(p.read_text()) for p in sorted(FIX_DIR.glob("*.json"))]
    names = [p.name for p in sorted(FIX_DIR.glob("*.json"))]
    if not fixtures:
        print("No fixtures found.", file=sys.stderr)
        return 2

    model_cfg = yaml.safe_load((REPO_ROOT / "config" / "scoring_model.yaml").read_text())
    min_build = float(model_cfg["thresholds"]["min_total_to_build"])

    # Build the SAME system prompt + contract the live opportunity_scoring uses.
    agent = "opportunity_scoring"
    body = R.parse_frontmatter((REPO_ROOT / "factory" / "agents" / agent / "AGENT.md").read_text())[1]
    system_blocks = R.build_system_blocks(agent, body)
    user = R._section("date_iso_idt", R._idt_date()) + "\n\n" + \
        R._section("opportunities", "```json\n" + json.dumps(fixtures, indent=2) + "\n```")

    import anthropic
    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    resp = client.messages.create(
        model="claude-sonnet-4-6", max_tokens=8192,
        system=system_blocks, messages=[{"role": "user", "content": user}],
    )
    text = resp.content[0].text if resp.content else ""
    scored = R._parse_json_payload(text)
    if isinstance(scored, dict):
        scored = [scored]
    by_id = {s.get("opportunity_id"): s for s in (scored or []) if isinstance(s, dict)}

    print(f"\n{'fixture':32} {'total':>6} {'stage':10} {'gate':6} {'autonomy':>8} {'buyer':>6} {'wtp':>5}")
    print("-" * 80)
    strong_reaching = []
    control_ok = True
    for name, fx in zip(names, fixtures):
        s = by_id.get(fx["id"], {})
        total = s.get("total")
        pd = s.get("per_dimension", {}) or {}
        gate_pass, _ = R._scoring_gate_pass(s, model_cfg) if s else (False, [])
        print(f"{name:32} {str(total):>6} {str(s.get('recommended_stage')):10} "
              f"{'PASS' if gate_pass else 'fail':6} {str(pd.get('operational_autonomy')):>8} "
              f"{str(pd.get('buyer_clarity')):>6} {str(pd.get('willingness_to_pay')):>5}")
        try:
            t = float(total)
        except (TypeError, ValueError):
            t = 0.0
        if name.startswith("strong_") and t >= min_build and gate_pass:
            strong_reaching.append(name)
        if name.startswith("control_") and t >= 5.5:
            control_ok = False

    print("-" * 80)
    print(f"build bar (min_total_to_build) = {min_build}")
    print(f"STRONG fixtures reaching >= {min_build} AND passing build_gates: "
          f"{len(strong_reaching)}/{sum(1 for n in names if n.startswith('strong_'))} "
          f"-> {strong_reaching}")
    print(f"negative control stayed < 5.5: {control_ok}")

    if strong_reaching and control_ok:
        print("\nCONCLUSION: the 6.5 build bar is REACHABLE by a genuinely strong, "
              "solo-viable idea. The rubric uses the full range; the empty pipeline "
              "is a SUPPLY problem (need more/better real ideas + time), not a "
              "calibration one.")
        return 0
    print("\nCONCLUSION: a clearly-excellent idea did NOT reach 6.5 — the rubric is "
          "COMPRESSED. Recalibrate anchors/weights (NOT the threshold) and re-run.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
