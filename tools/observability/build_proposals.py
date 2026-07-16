#!/usr/bin/env python3
"""
tools/observability/build_proposals.py — Valoria unified proposals / open-work register.

ONE deduplicated, lane-partitioned view of every piece of UNRATIFIED WORK in flight —
the thing that was scattered across a chain of stale hand-authored decision-queue
snapshots, a 9-file designs/proposals/ folder invisible to the dashboard, ~200 open
editorial-ledger items, the audit registry, and workplan §5. Sibling of
build_decisions.py; both are generated every audit-refresh so they cannot rot.

Scope vs DECISIONS.md: DECISIONS.md is marker-level decision *debt* (TODO/GAP/OPEN
sweep). THIS is whole unratified *work items awaiting sign-off*. Complementary,
cross-linked, both lane-partitioned. (CLAUDE.md §8; ED-IN-0068.)

Detect-not-author: this surfaces items and LINKS OUT to the human-authored ranked
queue and workplan §5 — it never invents its own ranking or ratifies anything.

Sources (all structured, via tools/observability/obs_core.py — every rule lives once):
  • canon/editorial_ledger*.jsonl  open items, split by needs_jordan
  • references/audit_registry.jsonl  PARTIAL / OPEN verdicts
  • designs/proposals/*.md          detected BY LOCATION (surfaces the 8 without a Status line)
  • designs/**/*.md                 first `## Status:` = PROPOSED / PROVISIONAL / DRAFT

Output: proposals.json, proposals_data.js (window.VALORIA_PROPOSALS), PROPOSALS.md
Run:    python3 tools/observability/build_proposals.py
"""
from __future__ import annotations
import json, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
# obs_core (not "core"): a distinct top-level module name, so it can't collide in
# sys.modules with designs/scene/combat_engine_v1/core.py (also imported bare).
import obs_core as core  # noqa: E402

# the current human-authored ranked queue + tiered register (LINKED, not parsed)
RANKED_QUEUE = "designs/audit/2026-07-14-scale-chain-and-decision-surface-map/decision_queue_delta_v1.md"
WORKPLAN_TIERS = "designs/workplans/valoria_master_workplan_v6.md"  # §5 T0/T1/T2

# audit-registry subsystem -> ED lane
AUDIT_SUBSYS_LANE = {
    "personal_combat": "PC", "social_contest": "SC", "settlement_territory": "SE",
    "mass_battle": "MB", "faction_political": "FA", "fieldwork_investigation": "FI",
    "architecture": "IN", "threadwork": "WR", "cross_cutting": "IN", "corpus_wide": "IN",
}
KIND_LABELS = {
    "proposal_doc": "Proposal docs (designs/proposals/)",
    "provisional_status_doc": "Provisional / draft design docs",
    "ledger_needs_jordan": "Editorial ledger — needs your decision",
    "ledger_actionable": "Editorial ledger — actionable (no ruling needed)",
    "audit_partial": "Audit verdicts — PARTIAL / OPEN",
}
KIND_ORDER = ["proposal_doc", "provisional_status_doc", "ledger_needs_jordan",
              "ledger_actionable", "audit_partial"]
PER_GROUP_CAP = 40  # MD render cap per (lane) — full set stays in proposals.json


def _rd(text: str) -> str:
    return core.redact_forbidden_names(text or "")


def _doc_head(path: Path, n: int = 4000) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")[:n]
    except OSError:
        return ""


def collect() -> list[dict]:
    items: list[dict] = []
    seen: set[tuple] = set()

    def add(kind, source, ident, title, lane, needs_jordan=False, status=None, links=None):
        key = (kind, source, ident)          # dedup on raw values (pre-redaction)
        if key in seen:
            return
        seen.add(key)
        # Redact EVERY text field written to the .md/.json — id/source/links can be
        # file paths or audit-folder names, so a legacy token there would otherwise
        # leak into the committed output and trip ci_naming_check (finding #4).
        items.append({
            "kind": kind, "source": _rd(source), "id": _rd(ident),
            "title": _rd(title)[:240], "lane": lane or "unassigned",
            "needs_jordan": bool(needs_jordan),
            "status": _rd(status) if status else None,
            "links": [_rd(x) for x in (links or [])],
        })

    # 1 + 2. design docs: designs/proposals/ BY LOCATION; else by unratified Status line
    for path in sorted((REPO / "designs").rglob("*.md")):
        rel = str(path.relative_to(REPO))
        if any(seg in rel for seg in ("/deprecated/", "/archives/", "/archive/")):
            continue
        in_proposals_dir = rel.startswith("designs/proposals/")
        head = _doc_head(path)
        status = core.first_status(head)
        # design-doc kinds previously could NOT carry needs_jordan (they never passed
        # the flag) — detect a pending-Jordan disposition from the doc's own Status +
        # head so a "HELD FOR JORDAN" doc is counted as needing your decision.
        nj = core.text_needs_jordan((status or "") + "\n" + head)
        if in_proposals_dir:
            add("proposal_doc", rel, rel,
                title=path.stem.replace("_", " "),
                lane=core.infer_lane(rel), needs_jordan=nj,
                status=status or "(no Status line — designs/proposals/)")
        elif core.is_unratified_status(status):
            add("provisional_status_doc", rel, rel,
                title=path.stem.replace("_", " "),
                lane=core.infer_lane(rel), needs_jordan=nj, status=status)

    # 3. editorial ledger open items, split by needs_jordan
    for e in core.open_ledger_entries():
        kind = "ledger_needs_jordan" if e["needs_jordan"] else "ledger_actionable"
        add(kind, "canon/editorial_ledger", e["id"],
            title=e["description"] or e["id"], lane=e["lane"],
            needs_jordan=e["needs_jordan"], status="open")

    # 4. audit registry PARTIAL / OPEN
    reg = REPO / "references" / "audit_registry.jsonl"
    if reg.exists():
        for line in reg.read_text(encoding="utf-8", errors="replace").splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                r = json.loads(line)
            except json.JSONDecodeError:
                continue
            if r.get("verdict") not in ("PARTIAL", "OPEN"):
                continue
            lane = AUDIT_SUBSYS_LANE.get(r.get("subsystem", ""), "IN")
            # id is shared across subsystem rows of one audit run — key on id+subsystem+folder
            ident = f"{r.get('id', '?')}:{r.get('subsystem', '')}:{(r.get('folder') or '').rstrip('/').split('/')[-1]}"
            add("audit_partial", "references/audit_registry.jsonl", ident,
                title=f"[{r.get('verdict')}] {r.get('audit_type')} / {r.get('subsystem')}: "
                      f"{(r.get('verdict_detail') or '')}",
                lane=lane, needs_jordan=(r.get("verdict") == "OPEN"),
                status=r.get("verdict"),
                links=[r.get("folder")] if r.get("folder") else [])
    return items


def build() -> dict:
    items = collect()
    by_lane: dict[str, dict] = {}
    by_kind: dict[str, int] = {}
    nj = 0
    for it in items:
        lane = it["lane"]
        by_lane.setdefault(lane, {"total": 0, "needs_jordan": 0, "items": []})
        by_lane[lane]["total"] += 1
        by_lane[lane]["items"].append(it)
        if it["needs_jordan"]:
            by_lane[lane]["needs_jordan"] += 1
            nj += 1
        by_kind[it["kind"]] = by_kind.get(it["kind"], 0) + 1
    return {
        "schema_version": 1,
        "generator": "tools/observability/build_proposals.py",
        "note": "GENERATED — do not hand-edit; re-run the generator (audit-refresh.yml). "
                "One deduplicated, lane-partitioned view of unratified work in flight. "
                "Complementary to DECISIONS.md (marker-level decision debt).",
        "ranked_view": RANKED_QUEUE,          # link, not a re-ranking (detect-not-author)
        "workplan_tiers": WORKPLAN_TIERS,
        "counts": {"total": len(items), "needs_jordan": nj,
                   "by_kind": by_kind,
                   "by_lane": {k: {"total": v["total"], "needs_jordan": v["needs_jordan"]}
                               for k, v in sorted(by_lane.items())}},
        "by_lane": by_lane,
        "items": items,
    }


def render_md(reg: dict) -> str:
    c = reg["counts"]
    L = ["# Proposals & open-work register",
         "",
         "> GENERATED by `tools/observability/build_proposals.py` — do not hand-edit; re-run it.",
         "> One deduplicated, lane-partitioned view of every unratified work item in flight.",
         "> Companion to [`DECISIONS.md`](DECISIONS.md) (marker-level decision *debt*); this is",
         "> whole *work* awaiting sign-off. Detect-not-author: nothing here ratifies on merge.",
         "",
         f"**{c['total']} open work items** · **{c['needs_jordan']} need your decision**.",
         "",
         f"Ranked view (human-authored): [`{reg['ranked_view']}`]({reg['ranked_view']}) · "
         f"tiered register: [`{reg['workplan_tiers']}` §5]({reg['workplan_tiers']})",
         "",
         "By kind: " + ", ".join(f"{KIND_LABELS.get(k, k)} — {v}"
                                 for k, v in sorted(c["by_kind"].items())),
         ""]
    lane_order = list(core.LANE_CODES) + ["unassigned"]
    for lane in lane_order:
        blk = reg["by_lane"].get(lane)
        if not blk:
            continue
        name = core.LANE_NAMES.get(lane, lane.title() if lane != "unassigned" else "Unassigned / cross-lane")
        L += [f"## {lane} — {name}  ({blk['total']} items, {blk['needs_jordan']} need decision)", ""]
        # order items within a lane by kind, needs_jordan first
        rows = sorted(blk["items"],
                      key=lambda it: (KIND_ORDER.index(it["kind"]) if it["kind"] in KIND_ORDER else 99,
                                      not it["needs_jordan"], it["id"]))
        shown = rows[:PER_GROUP_CAP]
        for it in shown:
            flag = "🔸 " if it["needs_jordan"] else ""
            src = it["id"] if it["id"] != it["source"] else it["source"]
            L.append(f"- {flag}`{src}` — {it['title']}"
                     + (f"  _({it['status']})_" if it["status"] else ""))
        if len(rows) > PER_GROUP_CAP:
            L.append(f"- …and {len(rows) - PER_GROUP_CAP} more (see `proposals.json`).")
        L.append("")
    return "\n".join(L) + "\n"


def main() -> int:
    reg = build()
    (HERE / "proposals.json").write_text(json.dumps(reg, indent=2, ensure_ascii=False),
                                         encoding="utf-8")
    core.write_js_bundle(HERE / "proposals_data.js", "VALORIA_PROPOSALS", reg)
    (HERE / "PROPOSALS.md").write_text(render_md(reg), encoding="utf-8")
    c = reg["counts"]
    print("Valoria proposals register built:")
    print(f"  total={c['total']}  needs_jordan={c['needs_jordan']}")
    print(f"  by_kind={c['by_kind']}")
    print(f"  by_lane={c['by_lane']}")
    print(f"  -> {HERE/'PROPOSALS.md'}  /  proposals.json  /  proposals_data.js")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
