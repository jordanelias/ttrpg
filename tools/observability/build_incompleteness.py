#!/usr/bin/env python3
"""
build_incompleteness.py — the Incompleteness Ledger.

The vectorization/observability apparatus exists to SURFACE WHAT IS MISSING. This generator is
the absorb-everything surface: it scans the WHOLE repo and records every stub / null / missing /
excluded / unverified thing it can find — marked AND unmarked — into one lane-partitioned register.

It deliberately captures the STRUCTURAL incompleteness that prose-marker scans (the decisions
digest) cannot see: empty-I/O module contracts, doc:null contracts, [ASSUMPTION] resolvers,
orphan/unemitted Keys, NotImplementedError sim stubs, the vector-audit's own culled/denied
systems, unverified integrity pins, and quarantined registers. It also folds in a rollup of the
prose-marker gap/assumption/stub/todo counts (from decisions.json) so the two views cross-check.

Nothing here is culled to stay "signal-heavy": a rarely-cited null is the point, not noise.

Outputs (deterministic — no timestamps, so the committed copy does not churn):
  tools/observability/incompleteness.json        — the machine-readable ledger
  tools/observability/INCOMPLETENESS.md          — human-readable, lane-partitioned
  tools/observability/incompleteness_data.js     — window.VALORIA_INCOMPLETENESS (dashboard feed)

Usage:
  python3 tools/observability/build_incompleteness.py
  python3 tools/observability/build_incompleteness.py --check   # exit 1 if the committed files are stale
"""
from __future__ import annotations

import json
import os
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML required: pip install pyyaml", file=sys.stderr)
    sys.exit(1)

HERE = Path(__file__).resolve()
OBS_DIR = HERE.parent
REPO = OBS_DIR.parents[1]

# lane inference — reuse the single resolver (build_decisions.infer_lane), same as the other feeds
sys.path.insert(0, str(OBS_DIR))
try:
    import build_decisions as _bd
    def infer_lane(p):
        return _bd.infer_lane(p) or "unassigned"
    LANE_ORDER = list(_bd.LANE_ORDER) + ["unassigned"]
except Exception:
    def infer_lane(p):
        return "unassigned"
    LANE_ORDER = ["MB", "PC", "FI", "SC", "FA", "WR", "IN", "GO", "SE", "unassigned"]

# the vector-audit's own cull manifest — surface what IT excludes, too
sys.path.insert(0, str(REPO / "skills" / "valoria-vector-audit" / "scripts"))
try:
    import vector_audit as _va
except Exception:
    _va = None


def _load_yaml(rel):
    p = REPO / rel
    if not p.exists():
        return None
    try:
        return yaml.safe_load(p.read_text(encoding="utf-8"))
    except Exception:
        return None


def _load_json(rel):
    p = REPO / rel
    if not p.exists():
        return None
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return None


# ── each finding: {category, id, title, detail, lane, path} — uniform across categories ──
def finding(cat, ident, title, detail, path=None, lane=None):
    return {"category": cat, "id": ident, "title": title, "detail": detail,
            "path": path or "", "lane": lane or infer_lane(path or "")}


def scan_module_contracts():
    """Structural nulls in the module IN/OUT contracts — the modularity gaps."""
    out = []
    mc = _load_yaml("references/module_contracts.yaml") or {}
    for m in (mc.get("modules") or []):
        if not isinstance(m, dict):
            continue
        mod = m.get("module")
        if not mod:
            continue
        doc = m.get("doc")
        path = doc if doc else ""
        emits = m.get("emits") or []
        consumes = m.get("consumes") or []
        resolver = m.get("resolver") or ""
        # doc:null — no home design doc
        if not doc:
            out.append(finding("contract_doc_null", mod, mod,
                               "module has no home design doc (doc: null) — contract unauthored", path=""))
        # empty-I/O island — untraceable in the propagation graph
        if not emits and not consumes:
            out.append(finding("contract_island", mod, mod,
                               "module declares NO emits AND NO consumes — an untraceable island in the graph",
                               path=path))
        # missing resolver
        if not resolver:
            out.append(finding("contract_no_resolver", mod, mod,
                               "module declares no resolver", path=path))
        # [ASSUMPTION]/[STUB]-grade markers anywhere in the entry text
        blob = json.dumps(m)
        for mark in ("[ASSUMPTION]", "[STUB]", "[PLACEHOLDER]", "[TODO]"):
            if mark in blob:
                out.append(finding("contract_assumption", mod, mod,
                                   f"contract carries {mark} — provisional/assumed, not a firm spec",
                                   path=path))
                break
    return out


def scan_graph_gaps(contract_mods):
    """Graph nodes with NO module_contracts entry at all (build_graph synthesizes them from the
    Key registry) — a module referenced by the wiring but never given a contract: the deepest
    modularity gap. Plus island/doc:null status for those synthesized nodes (missed by the
    contract scan). Deduped against contract_mods (module ids already scanned from the contracts)."""
    out = []
    g = _load_json("tools/observability/graph.json")
    if not g:
        return out
    for s in g.get("systems", []):
        sid = s.get("id")
        if not sid or sid in contract_mods:
            continue  # already covered by scan_module_contracts
        out.append(finding("contract_missing_entirely", sid, sid,
                           "module appears in the propagation graph (referenced by Keys) but has NO "
                           "module_contracts entry — no authored IN/OUT contract at all", path=""))
        if not s.get("emits") and not s.get("consumes") and not s.get("full_stream"):
            out.append(finding("contract_island", sid, sid,
                               "synthesized graph node with no emits/consumes — untraceable island", path=""))
    return out


def scan_key_closure():
    """Orphan/unemitted Keys — dead-ends in the propagation graph (from graph.json if present)."""
    out = []
    g = _load_json("tools/observability/graph.json")
    if not g:
        return out
    stats = (g.get("meta") or {}).get("stats") or {}
    for kid in stats.get("orphan_emits", []) or []:
        out.append(finding("key_orphan_emit", kid, kid,
                           "Key is emitted but has NO consumer — downstream dead-end", path=""))
    for kid in stats.get("unemitted_consumes", []) or []:
        out.append(finding("key_unemitted_consume", kid, kid,
                           "Key is consumed but NEVER emitted — upstream dead-end", path=""))
    return out


STUB_PATTERNS = [
    (re.compile(r"raise\s+NotImplementedError"), "NotImplementedError"),
    (re.compile(r"#\s*TODO", re.I), "TODO"),
    (re.compile(r"#\s*FIXME", re.I), "FIXME"),
    (re.compile(r"#\s*XXX"), "XXX"),
    (re.compile(r"#\s*STUB", re.I), "STUB-comment"),
]


def scan_sim_stubs():
    """NotImplementedError / TODO / FIXME in the executable sim reference + engine (the port oracle)."""
    out = []
    roots = [REPO / "systems", REPO / "engine"]
    for base in roots:
        if not base.exists():
            continue
        for py in base.rglob("*.py"):
            if "__pycache__" in py.parts or "/tests/" in str(py):
                continue
            rel = str(py.relative_to(REPO))
            try:
                lines = py.read_text(encoding="utf-8").splitlines()
            except Exception:
                continue
            for i, line in enumerate(lines, 1):
                for rx, kind in STUB_PATTERNS:
                    if rx.search(line):
                        out.append(finding("sim_stub", f"{rel}:{i}", f"{kind} @ {rel}:{i}",
                                           line.strip()[:160], path=rel))
                        break
    return out


def scan_integrity_pins():
    """Unverified canonical_sha pins — CLAUDE.md §1 flags the WHOLE pin layer as advisory (not
    verified against the working tree). Reported as ONE systemic finding carrying the total count
    (surfacing the magnitude, not hiding it) — per-pin detail + the stale subset come from
    `tools/freshness_gate.py --update`, the owner of that granularity (one rule, one place)."""
    cs = _load_yaml("references/canonical_sources.yaml") or {}
    n = 0
    def walk(node):
        nonlocal n
        if isinstance(node, dict):
            for k, v in node.items():
                if isinstance(k, str) and k.startswith("canonical_sha"):
                    n += 1
                else:
                    walk(v)
        elif isinstance(node, list):
            for it in node:
                walk(it)
    walk(cs)
    if not n:
        return []
    return [finding("integrity_unverified_pin", "canonical_sha_layer",
                    f"{n} canonical_sha pins — all advisory",
                    f"CLAUDE.md §1: the entire canonical_sha pin layer ({n} pins) is NOT verified against "
                    f"the working tree — treat as advisory, not an integrity signal. Stale subset via "
                    f"freshness_gate.py --update.", path="references/canonical_sources.yaml", lane="IN")]


def scan_quarantine():
    """Registers CLAUDE.md marks as quarantined/stale (surface them as known-incomplete data)."""
    out = []
    vm = REPO / "references" / "values_master.yaml"
    if vm.exists():
        out.append(finding("register_quarantined", "references/values_master.yaml",
                           "values_master.yaml",
                           "quarantined-stale (CLAUDE.md §7): free-text formulas, indexes a nonexistent "
                           "combat.md, pulls from a superseded threadwork doc — do not lift as canonical",
                           path="references/values_master.yaml", lane="IN"))
    return out


def scan_audit_exclusions():
    """The vector-audit's OWN culls — surface what the tokenizer denylists/floors drop."""
    out = []
    if _va is None:
        return out
    try:
        ex = _va.audit_exclusions(REPO)
    except Exception:
        return out
    for s in ex.get("skip_systems", []):
        if not s.get("present_in_canonical_sources"):
            continue
        out.append(finding("audit_excluded_system", s["system"], s.get("would_be_label") or s["system"],
                           f"vector-audit denylists this system: {s.get('reason','')}",
                           path=f"canonical_sources:{s['system']}", lane="IN"))
    return out


def prose_marker_rollup():
    """Cross-reference the decisions digest's prose gap/assumption/stub/todo counts (not re-scanned)."""
    d = _load_json("tools/observability/decisions.json")
    if not d:
        return {}
    by_cat = (d.get("meta") or {}).get("by_category") or {}
    return {k: by_cat.get(k, 0) for k in ("gap", "assumption", "stub", "todo") if k in by_cat}


def build():
    findings = []
    findings += scan_module_contracts()
    mc = _load_yaml("references/module_contracts.yaml") or {}
    contract_mods = {m.get("module") for m in (mc.get("modules") or []) if isinstance(m, dict)}
    findings += scan_graph_gaps(contract_mods)
    findings += scan_key_closure()
    findings += scan_sim_stubs()
    findings += scan_integrity_pins()
    findings += scan_quarantine()
    findings += scan_audit_exclusions()
    # stable order: category, then id — deterministic (no timestamps anywhere)
    findings.sort(key=lambda f: (f["category"], f["id"]))

    by_cat = Counter(f["category"] for f in findings)
    by_lane = defaultdict(lambda: defaultdict(int))
    for f in findings:
        by_lane[f["lane"]]["total"] += 1
        by_lane[f["lane"]][f["category"]] += 1

    payload = {
        "schema_version": 1,
        "generator": "tools/observability/build_incompleteness.py",
        "note": "GENERATED — the absorb-everything Incompleteness Ledger. Surfaces every stub / null / "
                "missing / excluded / unverified thing across the tree. Nothing culled to stay 'signal-heavy'.",
        "totals": {"findings": len(findings), "by_category": dict(sorted(by_cat.items()))},
        "by_lane": {ln: dict(by_lane[ln]) for ln in LANE_ORDER if ln in by_lane},
        "prose_marker_rollup": prose_marker_rollup(),
        "findings": findings,
    }
    return payload


CATEGORY_LABEL = {
    "contract_doc_null": "Module contracts with no home doc (doc:null)",
    "contract_island": "Island modules (no emits AND no consumes — untraceable)",
    "contract_no_resolver": "Modules with no resolver",
    "contract_assumption": "Contracts carrying [ASSUMPTION]/[STUB] markers",
    "contract_missing_entirely": "Modules in the graph with NO contract entry at all",
    "key_orphan_emit": "Orphan-emit Keys (emitted, no consumer)",
    "key_unemitted_consume": "Unemitted-consume Keys (consumed, never emitted)",
    "sim_stub": "Sim/engine stubs (NotImplementedError/TODO/FIXME)",
    "integrity_unverified_pin": "Unverified integrity pins (canonical_sha)",
    "register_quarantined": "Quarantined/stale registers",
    "audit_excluded_system": "Systems the vector-audit denylists",
}


def to_markdown(p):
    lines = ["# Incompleteness Ledger", "",
             "_GENERATED by `tools/observability/build_incompleteness.py` — do not hand-edit._", "",
             "The absorb-everything surface: every stub / null / missing / excluded / unverified thing "
             "the apparatus can find, across the whole tree. This is the point of the vectorization tool — "
             "to surface what is missing — so nothing here is culled to stay 'signal-heavy'.", "",
             f"**{p['totals']['findings']} findings** across {len(p['totals']['by_category'])} categories.", ""]
    lines.append("## By category")
    lines.append("")
    lines.append("| Category | Count |")
    lines.append("|---|---|")
    for cat, n in p["totals"]["by_category"].items():
        lines.append(f"| {CATEGORY_LABEL.get(cat, cat)} | {n} |")
    lines.append("")
    if p["prose_marker_rollup"]:
        pr = p["prose_marker_rollup"]
        lines.append("_Cross-reference — prose markers in the decisions digest: "
                     + ", ".join(f"{k} {v}" for k, v in pr.items()) + "._")
        lines.append("")
    lines.append("## By lane")
    lines.append("")
    lines.append("| Lane | Total |")
    lines.append("|---|---|")
    for ln, d in p["by_lane"].items():
        lines.append(f"| {ln} | {d.get('total', 0)} |")
    lines.append("")
    lines.append("## Findings")
    lines.append("")
    cur = None
    for f in p["findings"]:
        if f["category"] != cur:
            cur = f["category"]
            lines.append("")
            lines.append(f"### {CATEGORY_LABEL.get(cur, cur)}")
            lines.append("")
        loc = f" — `{f['path']}`" if f["path"] else ""
        lines.append(f"- **{f['title']}** ({f['lane']}){loc}: {f['detail']}")
    lines.append("")
    return "\n".join(lines)


def main(argv):
    payload = build()
    js = "window.VALORIA_INCOMPLETENESS = " + json.dumps(payload, separators=(",", ":")) + ";\n"
    md = to_markdown(payload)
    pj = OBS_DIR / "incompleteness.json"
    pjs = OBS_DIR / "incompleteness_data.js"
    pmd = OBS_DIR / "INCOMPLETENESS.md"
    new_json = json.dumps(payload, indent=2) + "\n"
    if "--check" in argv:
        stale = []
        for path, want in ((pj, new_json), (pjs, js), (pmd, md)):
            if not path.exists() or path.read_text(encoding="utf-8") != want:
                stale.append(path.name)
        if stale:
            print("Incompleteness Ledger STALE (re-run build_incompleteness.py): " + ", ".join(stale))
            return 1
        print(f"Incompleteness Ledger current: {payload['totals']['findings']} findings.")
        return 0
    pj.write_text(new_json, encoding="utf-8")
    pjs.write_text(js, encoding="utf-8")
    pmd.write_text(md, encoding="utf-8")
    print(f"Incompleteness Ledger built: {payload['totals']['findings']} findings across "
          f"{len(payload['totals']['by_category'])} categories.")
    for cat, n in payload["totals"]["by_category"].items():
        print(f"  {cat}: {n}")
    print(f"  -> {pj}\n  -> {pjs}\n  -> {pmd}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
