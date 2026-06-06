#!/usr/bin/env python3
"""Service Builder (P4.3) — scaffold services/<slug>/ from an APPROVED build.

Deterministic, internal-only (no LLM, no external calls). Triggered by an
operator-approved `promote_to_build` approval (see prompts/service_builder.md +
docs/DATA_MODEL.md). Copies the 17-file templates/service_template/ scaffold,
pre-populates only what is known from real inputs (NO fabrication), and leaves
exact `<!-- TO BE FILLED BY <agent_slug> — <what> -->` markers with a matching
`next_agent_handoffs` list. Refuses on slug collision or unapproved/absent
approval; idempotent (skips a slug already built).
"""
import json
import re
from datetime import datetime, timedelta, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent.resolve()
TEMPLATE_DIR = REPO_ROOT / "templates" / "service_template"
SERVICES_DIR = REPO_ROOT / "services"
OPP_DIR = REPO_ROOT / "opportunities"
QUEUE_DIR = REPO_ROOT / "approval_queue"

SLUG_RE = re.compile(r"^[a-z0-9]([a-z0-9-]{0,30}[a-z0-9])?$")
NEW_BUILDS_PER_DAY = 1  # hard ceiling; weekly cap lives in build_decisions

# file -> (owner_agent_slug, what_to_fill). market_evidence/status handled specially.
OWNERSHIP = {
    "offer.md": ("product_design", "one-line pitch, what's included/excluded, delivery promise, differentiation, guarantee"),
    "pricing.md": ("product_design", "price model + tiers within config/product_design.yaml guardrails + competitor anchor"),
    "landing_page_copy.md": ("product_design", "hook, three benefits, CTA, FAQ (language per geo)"),
    "onboarding_form.md": ("product_design", "final field list, validation rules, language labels"),
    "claude_delivery_prompts.md": ("product_design", "the delivery system prompt + input/output schema (language per geo)"),
    "delivery_workflow.md": ("product_design", "step-by-step delivery automation (trigger=form, end=deliverable+payment)"),
    "automation_plan.md": ("product_design", "tool list (Python + Claude; no Zapier)"),
    "lead_sources.md": ("lead_research", "ranked, compliant outreach channels; NO raw PII (hash handles)"),
    "responsiveness_test.md": ("responsiveness_test", "A/B/C outreach variants + success thresholds — DRAFT, sending requires approval"),
    "payment_path.md": ("payment_ops", "Stripe payment-link/invoice flow; IL VAT 17% if geo=IL"),
    "metrics.md": ("analytics", "funnel targets and the first-signal checkpoint"),
    "report_template.md": ("analytics", "per-week numbers section"),
    "support_policy.md": ("support", "support hours, response SLA, language"),
    "qa_checklist.md": ("qa", "service-specific QA items (disclaimer, opt-out, no PII, language)"),
    "launch_checklist.md": ("product_design", "gate names and the approval each requires per config/approval_policy.yaml"),
}


def _idt_now() -> datetime:
    return datetime.now(timezone(timedelta(hours=3)))


def _read_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None


def _scaffold_header(owner: str, what: str, facts: dict) -> str:
    fact_lines = "\n".join(f"{k}: {v}" for k, v in facts.items() if v not in (None, ""))
    return (
        f"<!-- TO BE FILLED BY {owner} — {what} -->\n"
        "<!-- Scaffold context (auto-filled by service_builder; do not fabricate "
        "beyond these known facts):\n"
        f"{fact_lines}\n-->\n\n"
    )


def find_pending_builds() -> list[dict]:
    """Approved promote_to_build items whose services/<slug>/ doesn't exist yet."""
    out: list[dict] = []
    if not QUEUE_DIR.exists():
        return out
    for ap in sorted(QUEUE_DIR.glob("*.approved.json")):
        obj = _read_json(ap)
        if not isinstance(obj, dict) or obj.get("action_type") != "promote_to_build":
            continue
        payload = obj.get("payload") or {}
        oid = payload.get("opportunity_id")
        slug = (payload.get("proposed_slug") or "").strip().lower()
        if not oid or not slug:
            continue
        if (SERVICES_DIR / slug).exists():
            continue
        out.append({
            "ulid": obj.get("ulid"),
            "opportunity_id": oid,
            "slug": slug,
            "approved_at": obj.get("operator_ts"),
            "confidence_pct": payload.get("confidence_pct"),
            "why_now_memo": payload.get("why_now_memo", ""),
        })
    return out


def _builds_today() -> int:
    today = _idt_now().strftime("%Y-%m-%d")
    n = 0
    if SERVICES_DIR.exists():
        for sd in SERVICES_DIR.iterdir():
            sc = _read_json(sd / "_scaffold.json") if sd.is_dir() else None
            if sc and (sc.get("scaffolded_at") or "")[:10] == today:
                n += 1
    return n


def scaffold_service(opportunity_id: str, slug: str, approved_at: str | None,
                     confidence_pct=None, why_now_memo: str = "") -> dict:
    """Scaffold one approved service. Returns a status dict (also written to
    services/<slug>/_scaffold.json on success)."""
    slug = (slug or "").strip().lower()
    if not SLUG_RE.match(slug) or len(slug) > 32:
        return {"status": "blocked", "reason": "slug_invalid", "received_slug": slug}
    if not approved_at:
        return {"status": "blocked", "reason": "build_decision_not_approved", "slug": slug}
    svc = SERVICES_DIR / slug
    if svc.exists():
        return {"status": "blocked", "reason": "slug_collision", "existing_slug": slug}

    opp = _read_json(OPP_DIR / f"{opportunity_id}.opportunity.json") or {}
    scoring = _read_json(OPP_DIR / f"{opportunity_id}.scoring.json") or {}
    facts = {
        "opportunity_id": opportunity_id,
        "slug": slug,
        "target_segment": opp.get("target_segment"),
        "problem_statement": opp.get("problem_statement"),
        "geo": opp.get("geo"),
        "keywords": ", ".join(opp.get("keywords", []) or []),
        "build_confidence_pct": confidence_pct,
        "recommended_stage": scoring.get("recommended_stage"),
        "scoring_total": scoring.get("total"),
    }

    if not TEMPLATE_DIR.exists():
        return {"status": "failed", "reason": "template_dir_missing"}

    svc.mkdir(parents=True)
    created, populated, partial, template_only, missing = [], [], [], [], []
    handoffs = []
    now_iso = _idt_now().isoformat(timespec="seconds")

    template_files = sorted(p.name for p in TEMPLATE_DIR.glob("*.md"))
    try:
        for fname in template_files:
            tmpl = (TEMPLATE_DIR / fname).read_text(encoding="utf-8")
            dest = svc / fname
            rel = f"services/{slug}/{fname}"

            if fname == "status.md":
                header = (
                    "# Status\n\n"
                    "## Slug\n\n`" + slug + "`\n\n"
                    "## Created at (IDT)\n\n" + now_iso + "\n\n"
                    "## Current stage\n\nCurrent stage: building\nStage entered at (IDT): " + now_iso + "\n\n"
                    "## Provenance\n\n"
                    f"- opportunity_id: `{opportunity_id}`\n"
                    f"- build_decision approved at: {approved_at}\n"
                    f"- build_decision confidence: {confidence_pct}%\n"
                    f"- scoring total: {scoring.get('total')} (stage {scoring.get('recommended_stage')})\n"
                    "- market evidence: `market_evidence.md`\n"
                    "- live URL: <!-- TO BE FILLED BY product_design — set on publish (P4.7) -->\n"
                    "- last_signal_at: <!-- TO BE FILLED BY responsiveness_test/analytics -->\n\n"
                    "---\n\n"
                )
                dest.write_text(header + tmpl, encoding="utf-8")
                populated.append(fname)
                created.append(rel)
                continue

            if fname == "market_evidence.md":
                ev = OPP_DIR / f"{opportunity_id}.market_evidence.md"
                if ev.exists():
                    dest.write_text(ev.read_text(encoding="utf-8"), encoding="utf-8")
                    populated.append(fname)
                else:
                    dest.write_text(_scaffold_header(
                        "pain_validation", "market evidence narrative", facts) + tmpl, encoding="utf-8")
                    partial.append(fname)
                    handoffs.append({"agent": "pain_validation", "file": rel,
                                     "what_to_fill": "validated market evidence narrative"})
                created.append(rel)
                continue

            owner, what = OWNERSHIP.get(fname, ("product_design", "complete this section"))
            dest.write_text(_scaffold_header(owner, what, facts) + tmpl, encoding="utf-8")
            partial.append(fname)
            handoffs.append({"agent": owner, "file": rel, "what_to_fill": what})
            created.append(rel)
    except OSError as exc:
        # roll back partial scaffold
        for c in created:
            (REPO_ROOT / c).unlink(missing_ok=True)
        try:
            svc.rmdir()
        except OSError:
            pass
        return {"status": "failed", "reason": str(exc)}

    summary = {
        "slug": slug,
        "scaffolded_at": now_iso,
        "opportunity_id": opportunity_id,
        "approved_build_decision_at": approved_at,
        "build_confidence_pct": confidence_pct,
        "files_created": created,
        "files_populated": populated,
        "files_partially_populated": partial,
        "files_template_only": template_only,
        "missing_template_files": missing,
        "next_agent_handoffs": handoffs,
        "design_review_done": False,
        "status": "scaffolded",
    }
    (svc / "_scaffold.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    (svc / "build_provenance.json").write_text(json.dumps({
        "slug": slug,
        "opportunity_id": opportunity_id,
        "approved_build_decision_at": approved_at,
        "scaffolded_at": now_iso,
        "inputs": {
            "opportunity": f"opportunities/{opportunity_id}.opportunity.json",
            "scoring": f"opportunities/{opportunity_id}.scoring.json",
            "cost_gain": f"opportunities/{opportunity_id}.cost_gain.json",
            "build_decision": f"opportunities/{opportunity_id}.build_decision.json",
        },
        "why_now_memo": why_now_memo,
    }, indent=2), encoding="utf-8")
    return summary


def run() -> list[dict]:
    """Scaffold all pending approved builds, up to the daily ceiling."""
    results = []
    pending = find_pending_builds()
    budget = max(0, NEW_BUILDS_PER_DAY - _builds_today())
    for p in pending:
        if budget <= 0:
            results.append({"status": "deferred", "reason": "daily_build_cap_reached", "slug": p["slug"]})
            break
        res = scaffold_service(p["opportunity_id"], p["slug"], p["approved_at"],
                               p.get("confidence_pct"), p.get("why_now_memo", ""))
        results.append(res)
        if res.get("status") == "scaffolded":
            budget -= 1
    return results


if __name__ == "__main__":
    for r in run():
        print(json.dumps(r))
