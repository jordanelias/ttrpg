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


# A malformed registry that parses to None is the WORST possible cull — the scanner would report
# the layer as complete precisely when it is most broken. So parse failures are RECORDED (F1) and
# surfaced as their own findings, never swallowed to silence.
PARSE_FAILURES = []


def _load_yaml(rel):
    p = REPO / rel
    if not p.exists():
        return None
    try:
        return yaml.safe_load(p.read_text(encoding="utf-8"))
    except Exception as e:
        PARSE_FAILURES.append((rel, f"YAML parse error: {e}"))
        return None


def _load_json(rel):
    p = REPO / rel
    if not p.exists():
        return None
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception as e:
        PARSE_FAILURES.append((rel, f"JSON parse error: {e}"))
        return None


def scan_parse_failures():
    """Surface any registry/data file that failed to parse (recorded by the loaders above)."""
    return [finding("parse_failure", rel, f"UNPARSEABLE: {rel}", msg, path=rel)
            for rel, msg in PARSE_FAILURES]


# ── each finding: {category, id, title, detail, lane, path} — uniform across categories ──
# Severity per category (fix #4, 2026-07-23 — the ledger had no ranking; every finding read equal,
# so a port-blocking isolated `victory` contract sat level with a sparse token in an arc doc).
# high = engine-spine / a concept with no home; med = a real gap needing authoring; low = hygiene.
SEVERITY = {
    "contract_missing_entirely": "high", "contract_no_resolver": "high", "contract_doc_null": "high",
    "key_orphan_emit": "high", "key_unemitted_consume": "high", "audit_isolate": "high",
    "audit_schema_mismatch": "high", "register_quarantined": "high", "register_phantom_source": "high",
    "parse_failure": "high",
    "contract_island": "med", "contract_assumption": "med", "contract_doc_dead": "med",
    "audit_implied_missing": "med", "audit_throughline_orphan": "med",
    # sim_not_implemented kept MED (an adversarial pass argued high — a NotImplementedError in the
    # port's ORACLE, CLAUDE.md §7, is a port-blocker): kept med deliberately so the HIGH tier stays
    # the tight "drop-everything" triage set (39 sim stubs would swamp it); a known stub is incomplete,
    # not necessarily blocking a module the port hasn't reached. Judgment call, documented.
    "sim_not_implemented": "med", "status_noncurrent": "med", "stale_retired_pointer": "med",
    "integrity_unverified_pin": "med",
    "prose_marker": "low", "code_marker": "low", "unregistered_term": "low", "audit_notional": "low",
    "audit_sparse": "low", "audit_vocab_debt": "low", "audit_excluded_system": "low",
    "apparatus_orphan": "low",
    # audit_cascade_sink is LOW, not med: it's an UNVERIFIED LEAD (the return-path search is
    # cap-limited and trips heavily on a dense corpus — see coverage_gaps), not a confirmed gap.
    "audit_cascade_sink": "low",
}
DEFAULT_SEVERITY = "med"
SEVERITY_RANK = {"high": 0, "med": 1, "low": 2}


def finding(cat, ident, title, detail, path=None, lane=None):
    return {"category": cat, "id": ident, "title": title, "detail": detail,
            "path": path or "", "lane": lane or infer_lane(path or ""),
            "severity": SEVERITY.get(cat, DEFAULT_SEVERITY)}


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
        # best-effort lane for a doc:null module: guess from a systems/<...>/<module> glob (F9)
        guess_lane = infer_lane(doc) if doc else None
        if not guess_lane or guess_lane == "unassigned":
            hit = next(iter((REPO / "systems").glob(f"*/{mod}*")), None) or \
                  next(iter((REPO / "systems").glob(f"*/*{mod}*")), None)
            if hit:
                guess_lane = infer_lane(str(hit.relative_to(REPO)))
        # doc:null — no home design doc
        if not doc:
            out.append(finding("contract_doc_null", mod, mod,
                               "module has no home design doc (doc: null) — contract unauthored",
                               path="", lane=guess_lane))
        # doc points at a file that DOES NOT EXIST — more incomplete than doc:null (F2)
        elif not (REPO / doc).exists():
            out.append(finding("contract_doc_dead", mod, mod,
                               f"module doc points at a NON-EXISTENT file (dead path): {doc}",
                               path=doc, lane=guess_lane))
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
        island = " (and it is an island: no emits/consumes)" if (
            not s.get("emits") and not s.get("consumes") and not s.get("full_stream")) else ""
        # one node = one finding — missing_entirely subsumes island, so we don't double-book (F10)
        out.append(finding("contract_missing_entirely", sid, sid,
                           "module appears in the propagation graph (referenced by Keys) but has NO "
                           "module_contracts entry — no authored IN/OUT contract at all" + island, path=""))
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


# NotImplementedError is a hard RUNTIME stub; the rest are comment-marked gaps. Kept as separate
# categories (F8) so a runtime failure is not conflated with a TODO note. Broad idiom set (F11).
NIE_PATTERN = re.compile(r"raise\s+NotImplementedError")
MARKER_PATTERNS = [
    (re.compile(r"#\s*TODO", re.I), "TODO"),
    (re.compile(r"#\s*FIXME", re.I), "FIXME"),
    (re.compile(r"#\s*XXX"), "XXX"),
    (re.compile(r"#\s*HACK", re.I), "HACK"),
    (re.compile(r"#\s*TBD", re.I), "TBD"),
    (re.compile(r"#\s*STUB", re.I), "STUB"),
    (re.compile(r"#\s*PLACEHOLDER", re.I), "PLACEHOLDER"),
]
# Python trees scanned for stubs — the WHOLE executable surface, not just the port oracle (F3):
# systems/ + engine/ (the sim reference) AND tools/ + skills/ (the apparatus itself). tests/ is
# INCLUDED but tagged, so a stubbed test is surfaced, not hidden.
PY_STUB_ROOTS = ["systems", "engine", "tools", "skills"]


def scan_sim_stubs():
    """Runtime stubs (NotImplementedError) + comment-marked gaps (TODO/FIXME/…) across every
    Python tree in the apparatus. NotImplementedError -> category 'sim_not_implemented' (hard);
    markers -> 'code_marker' (soft). Scope is surfaced in each finding (incl. whether in tests)."""
    out = []
    for root in PY_STUB_ROOTS:
        base = REPO / root
        if not base.exists():
            continue
        for py in base.rglob("*.py"):
            if "__pycache__" in py.parts:
                continue
            rel = str(py.relative_to(REPO))
            in_tests = "/tests/" in ("/" + rel) or rel.split("/")[0] == "tests"
            try:
                lines = py.read_text(encoding="utf-8").splitlines()
            except Exception:
                continue
            for i, line in enumerate(lines, 1):
                tag = " [in tests]" if in_tests else ""
                if NIE_PATTERN.search(line):
                    out.append(finding("sim_not_implemented", f"{rel}:{i}",
                                       f"NotImplementedError @ {rel}:{i}{tag}", line.strip()[:160], path=rel))
                    continue
                for rx, kind in MARKER_PATTERNS:
                    if rx.search(line):
                        out.append(finding("code_marker", f"{rel}:{i}",
                                           f"{kind} @ {rel}:{i}{tag}", line.strip()[:160], path=rel))
                        break
    return out


PROSE_MARKER = re.compile(r"\b(TODO|FIXME|TBD|XXX|HACK|WIP|\?\?\?)\b")


def scan_prose_markers():
    """TODO/FIXME/TBD/??? in .md prose across the design tree (F5) — the scanner previously only
    read .py. Scans the canonical doc surfaces; skips deprecated/ (frozen history)."""
    out = []
    roots = ["systems", "engine", "godot", "canon", "references", "registers", "proposals", "workplans"]
    for root in roots:
        base = REPO / root
        if not base.exists():
            continue
        for md in base.rglob("*.md"):
            rel = str(md.relative_to(REPO))
            if rel.startswith("deprecated/"):
                continue
            try:
                text = md.read_text(encoding="utf-8")
            except Exception:
                continue
            hits = PROSE_MARKER.findall(text)
            if hits:
                c = Counter(hits)
                out.append(finding("prose_marker", rel, rel,
                                   "prose gap markers: " + ", ".join(f"{k}×{v}" for k, v in c.items()),
                                   path=rel))
    return out


NONCURRENT_STATUS = re.compile(
    r"^\s*#{0,4}\s*Status\s*:\s*.*?\b(PROPOSED|PROVISIONAL|DRAFT|STALE|SUPERSEDED|DEPRECATED|WIP|TODO)\b",
    re.I | re.M)


def scan_status_headers():
    """Docs whose `## Status:` line is not a current/ratified state (F5) — the currency signal
    CLAUDE.md leans on. Skips deprecated/ (frozen)."""
    out = []
    roots = ["systems", "engine", "godot", "canon", "references", "proposals"]
    for root in roots:
        base = REPO / root
        if not base.exists():
            continue
        for md in base.rglob("*.md"):
            rel = str(md.relative_to(REPO))
            if rel.startswith("deprecated/"):
                continue
            try:
                text = md.read_text(encoding="utf-8")
            except Exception:
                continue
            m = NONCURRENT_STATUS.search(text)
            if m:
                out.append(finding("status_noncurrent", rel, rel,
                                   f"doc Status is not current: {m.group(1).upper()}", path=rel))
    return out


RETIRED_TREES = ("designs/",)  # designs/ was retired 2026-07-19 (ED-IN-0071 P4/P5)


def scan_retired_tree_pointers():
    """Machine-read registries that still reference the RETIRED designs/ tree (F/critic follow-up).
    These resolve only via the restructure_ledger alias map — i.e. they are stale pointers hiding
    behind the alias, invisible until now. The alias map itself and append-only ledgers legitimately
    carry the old paths, so they are excluded."""
    out = []
    EXCLUDE = ("restructure_ledger",)  # the alias map: designs/ paths are its KEYS, legitimate
    rel_re = re.compile(r"designs/[A-Za-z0-9_./\-]+\.md")
    for sub in ("references", "registers"):
        base = REPO / sub
        if not base.exists():
            continue
        for f in list(base.glob("*.yaml")) + list(base.glob("*.md")):
            rel = str(f.relative_to(REPO))
            if any(x in rel for x in EXCLUDE):
                continue
            try:
                text = f.read_text(encoding="utf-8")
            except Exception:
                continue
            hits = rel_re.findall(text)
            if hits:
                uniq = sorted(set(hits))
                out.append(finding("stale_retired_pointer", rel, rel,
                                   f"{len(hits)} reference(s) to the retired designs/ tree "
                                   f"(alias-resolved, not live): e.g. {', '.join(uniq[:3])}"
                                   + (f" (+{len(uniq)-3} more)" if len(uniq) > 3 else ""),
                                   path=rel, lane="IN"))
    return out


def scan_orphan_tools():
    """Tools/skills/hooks the apparatus registry flags as orphaned (no importer/invoker) (F5)."""
    out = []
    ar = _load_yaml("references/apparatus_registry.yaml")
    entries = ar if isinstance(ar, list) else ((ar or {}).get("entries") if isinstance(ar, dict) else None)
    for e in (entries or []):
        if isinstance(e, dict) and e.get("orphaned"):
            p = e.get("path", "")
            out.append(finding("apparatus_orphan", p or e.get("stem", "?"), p or e.get("stem", "?"),
                               "apparatus registry flags this as orphaned (no importer/invoker)", path=p))
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
    """Registers CLAUDE.md marks as quarantined/stale, PLUS the per-item phantom rows inside them
    (F6): values_master entries that index a NON-EXISTENT source file are enumerated, not collapsed."""
    out = []
    vm_rel = "references/values_master.yaml"
    vm = REPO / vm_rel
    if not vm.exists():
        return out
    out.append(finding("register_quarantined", vm_rel, "values_master.yaml",
                       "quarantined-stale (CLAUDE.md §7): free-text formulas, indexes a nonexistent "
                       "combat.md, pulls from a superseded threadwork doc — do not lift as canonical",
                       path=vm_rel, lane="IN"))
    vm_data = _load_yaml(vm_rel)
    # enumerate rows whose declared source does not exist on disk — the ~70 phantom combat.md rows.
    # In values_master the source is the MAPPING KEY (e.g. "engine/params/combat.md": {…}) as well as
    # any source-like field VALUE; count nested entries under a phantom key.
    phantom = Counter()
    def is_dead_md(s):
        if not (isinstance(s, str) and s.endswith(".md")):
            return None
        cand = s.split(":")[0].split("#")[0].strip()
        return cand if (cand and "/" in cand and not (REPO / cand).exists()) else None
    def walk(node):
        if isinstance(node, dict):
            for k, v in node.items():
                dead = is_dead_md(k)  # source path used as a mapping key
                if dead:
                    phantom[dead] += (len(v) if isinstance(v, (dict, list)) else 1)
                    continue
                if isinstance(k, str) and k in ("source", "source_file", "file", "doc", "canonical_source"):
                    dv = is_dead_md(v)
                    if dv:
                        phantom[dv] += 1
                        continue
                walk(v)
        elif isinstance(node, list):
            for it in node:
                walk(it)
    walk(vm_data)
    for src, n in sorted(phantom.items()):
        out.append(finding("register_phantom_source", f"values_master::{src}",
                           f"{n} entries index a NON-EXISTENT source: {src}",
                           f"values_master.yaml has {n} entries whose source file {src} does not exist on "
                           f"disk — phantom index rows (CLAUDE.md §5)", path=vm_rel, lane="IN"))
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


def scan_audit_structural():
    """Surface ALL EIGHT of the vector-audit's diagnostic modes from its committed feed
    (audit_findings.json, refreshed by --emit-findings): B implied-missing, C notional, D
    cascade-sinks, E sparse-context, F throughline-orphans, G vocabulary-debt, H isolates (A hubs are
    context). This is how the two observatories TALK — the audit's full structural analysis lands in
    the unified ledger, not just ¼ of it. Reads a committed snapshot (fast) — the 70s audit run
    happens in audit-refresh / the dashboard deploy, not per ledger build."""
    d = _load_json("tools/observability/audit_findings.json")
    if not d:
        return []
    # SCHEMA HANDSHAKE: the two observatories agree on schema_version 2 (all-eight-modes feed). If the
    # emit side bumps it, degrade LOUDLY to a self-surfacing marker rather than silently emitting
    # empty/partial rows via all-optional .get() — the ledger's job is to never hide a break.
    sv = d.get("schema_version")
    if sv != 2:
        return [finding("audit_schema_mismatch", "audit_findings_schema",
                        f"audit_findings.json schema_version {sv!r} ≠ expected 2",
                        f"the vector-audit feed changed its schema (got {sv!r}, expected 2) — "
                        f"scan_audit_structural in build_incompleteness.py must be updated to match "
                        f"before its findings can be trusted",
                        path="tools/observability/audit_findings.json", lane="IN")]
    # SNAPSHOT disclosure: these rows are read from a weekly-committed feed, not recomputed here
    # (the 70s audit runs in audit-refresh). audit_staleness.py watches the feed for drift.
    snap = "snapshot (audit_findings.json, refreshed weekly by audit-refresh)"
    out = []
    for r in d.get("implied_missing", []):
        # SURFACE-NEVER-CULL: the feed retains every finding; the ledger's high-signal Missing face
        # consumes only the UNfiltered rows (hub×hub pairs are flagged in the feed, not here). A
        # reader wanting the full set reads audit_findings.json directly.
        if r.get("filtered"):
            continue
        a, b = r.get("a"), r.get("b")
        # navigability: carry the tokens' primary_doc(s) as the finding path. Prefer a's doc.
        p = r.get("a_doc") or r.get("b_doc") or ""
        out.append(finding("audit_implied_missing", f"impl::{a}||{b}",
                           f"{a} ⋯ {b} — implied but never cited",
                           f"“{a}” and “{b}” are linked in {r.get('meta_links','?')} metadata graphs "
                           f"(throughline/mu/pp) but are NEVER cited together — a missing connection the "
                           f"design should make explicit or is a real gap (vector-audit Mode B; {snap})",
                           path=p, lane="IN"))
    for r in d.get("isolates", []):
        if r.get("filtered"):
            continue
        t = r.get("token")
        # (M2) Do NOT soften this — a Mode-H isolate is one of the strongest gap signals. Be exact
        # about HOW isolated (the feed carries max_deg + doc so we don't assume): a token with a home
        # doc but max-degree ≤1 is structurally marooned; a token with NO home doc is a registered
        # term with no design-prose home at all — the strongest case. (L1) path links to the doc if
        # there is one, else to the REGISTRY that defines it (where you'd author a doc or de-register).
        doc = r.get("doc")
        reg = r.get("registry") or ""
        md = r.get("max_deg", 0)
        if doc:
            title = f"{t} — structurally marooned"
            body = (f"“{t}” appears in {doc} but has max degree {md} (≤1) across ALL FIVE structural "
                    f"graphs (cite/throughline/mu/pp + the engine Key-propagation graph) — disconnected "
                    f"from the rest of the design AND the engine wiring; make its connections explicit "
                    f"or confirm it is genuinely standalone")
            path = doc
        else:
            title = f"{t} — no design-prose home"
            # Report the STRUCTURAL fact only; do NOT assert a mechanism the ledger can't verify. A
            # degree-≤1 Key token can be an orphan EMIT (emitted, unconsumed — e.g. mass_battle's
            # scene_outcome.battle_concluded, ED-MB-0010), a Key consumed-but-unemitted, or a
            # cross-module flow declared only in `derivations:` (which the Key graph does not read) —
            # the register is where you investigate which. (Corrected after an adversarial pass caught
            # the text mislabeling an orphan-emit as "no module emits or consumes".)
            body = (f"“{t}” has max degree {md} (≤1) across ALL FIVE structural graphs "
                    f"(cite/throughline/mu/pp + engine Key-propagation) AND has no primary design doc "
                    f"— a registered term with no home the graphs can see (a strong incompleteness "
                    f"signal). If it is a Key type, check the register for the mechanism: an orphan "
                    f"emit (emitted, unconsumed), an unemitted/unconsumed Key, or a cross-module "
                    f"`derivations` flow the Key graph does not read; registered via {reg or '?'}")
            path = reg
        out.append(finding("audit_isolate", f"iso::{t}", title,
                           f"{body}. vector-audit Mode H; status {r.get('status','?')} ({snap})",
                           path=path, lane="IN"))

    # ── Modes C–G (added 2026-07-23 — the feed used to surface only B + H) ────────────────────────
    # C — notional citations (cited but content-empty): high volume (~14k), so a SINGLE summary row
    # carrying the TRUE total + top examples (SURFACE-NEVER-CULL: total shown, not silently capped).
    nt = d.get("notional_total", 0)
    if nt:
        top = d.get("notional", [])
        egs = "; ".join(f"{r.get('source')}→{r.get('target')} (w{r.get('cite_weight')})" for r in top[:5])
        out.append(finding("audit_notional", "notional::rollup",
                           f"{nt} notional citations — cited but content-empty",
                           f"{nt} token pairs are cited together but share NO metadata-graph support "
                           f"(throughline/mu/pp/key) — a citation with nothing structural behind it "
                           f"(vector-audit Mode C). Top by weight: {egs or '—'}. The feed carries a "
                           f"top-100 sample (not all {nt}); the full ranked list is reproducible by "
                           f"re-running the deterministic audit ({snap})", path="", lane="IN"))
    # D — cascade sinks (flowed into, never back out): few (<=15 shown); emit each + truncation caveat.
    trunc = d.get("cascade_truncated_calls", 0)
    dtot = d.get("cascade_sinks_total", 0)
    # QUANTITATIVE honesty (fix #6): the return-path search is capped (5000 steps / 200 nodes). In a
    # dense corpus that cap trips often, and a capped 'no-return' can be a FALSE sink. Print the actual
    # trip count so the reader knows HOW unreliable — "some" understates a 5-figure number.
    cav = (f" ⚠ UNVERIFIED LEAD: the return-path search hit its traversal cap {trunc:,} times this "
           f"run, so this 'no-return' may be a cap artifact, not a real sink — verify by hand"
           if trunc else "")
    for r in d.get("cascade_sinks", []):
        term = r.get("terminal")
        out.append(finding("audit_cascade_sink", f"sink::{term}",
                           f"{term} — cascade sink ({r.get('chains')} chains)",
                           f"“{term}” is reached by {r.get('chains')} citation chains (len≥3) but never "
                           f"cites back — a concept things flow INTO but nothing flows back from "
                           f"(vector-audit Mode D; {dtot} sinks total). Terminal-by-design or a broken "
                           f"feedback loop.{cav} ({snap})", path=r.get("doc") or "", lane="IN"))
    # E — sparse-context tokens (bottom decile in paragraphs AND cite-degree): emit each (bounded).
    for r in d.get("sparse_context", []):
        t = r.get("token")
        out.append(finding("audit_sparse", f"sparse::{t}",
                           f"{t} — thinly developed",
                           f"“{t}” is in the bottom decile of BOTH prose volume ({r.get('paragraphs')} "
                           f"paragraphs) and citation degree ({r.get('cite_deg')}) — an under-developed "
                           f"concept (vector-audit Mode E); status {r.get('status','?')} ({snap})",
                           path=r.get("doc") or "", lane="IN"))
    # F — throughline orphans (<=2 substantiating paragraphs): emit each.
    for r in d.get("throughline_orphans", []):
        tid = r.get("throughline")
        systems = ", ".join((r.get("systems") or [])[:5])
        out.append(finding("audit_throughline_orphan", f"tl_orphan::{tid}",
                           f"{tid} — throughline barely substantiated",
                           f"throughline {tid} has only {r.get('substantiating')} paragraph(s) where ≥2 "
                           f"of its systems ({systems}) co-appear — a narrative chain the prose barely "
                           f"grounds (vector-audit Mode F; {snap})", path="", lane="IN"))
    # G — vocabulary debt (struck/deprecated terms still in use): emit each.
    for r in d.get("vocab_debt", []):
        term = r.get("term")
        out.append(finding("audit_vocab_debt", f"vocab::{term}",
                           f"“{term}” — struck term still in use",
                           f"the struck/deprecated term “{term}” still appears {r.get('total')}× across "
                           f"{r.get('docs')} doc(s) (vector-audit Mode G) — vocabulary debt to sweep; "
                           f"e.g. {r.get('top_doc','')} ({snap})", path=r.get("top_doc") or "", lane="IN"))
    return out


def scan_unregistered_terms():
    """MISSING REGISTRATIONS — authored design terms that appear across many docs but that NO
    registered token matches, so the vector-audit is structurally blind to them (the token universe
    is registry-derived). This is the audit's token-discovery TALKING to the ledger: a frequent
    unregistered term is a gap in the central registers. Leads, not verdicts."""
    if _va is None:
        return []
    try:
        # min_docs=12 (not a hard top-N cap): the floor is the only cutoff, so a boundary tie can't
        # reshuffle the committed slice (churn-proof). Name-level ontology match keeps it high-signal.
        cands = _va.discover_unregistered_candidates(REPO, min_docs=12)
    except Exception:
        return []
    out = []
    for c in cands:
        top = (c.get('top_docs') or [])
        back = (" — e.g. " + ", ".join(top)) if top else ""
        out.append(finding("unregistered_term", f"term::{c['term']}",
                           f"“{c['term']}” — in {c['docs']} docs, unregistered",
                           f"appears in {c['docs']} design docs ({c['total']} mentions) but the central "
                           f"ontology (tokens/modules/descriptors/graph nodes) has no match — a candidate "
                           f"missing registration; register it or confirm it is not canonical{back}",
                           path=(top[0] if top else ""), lane="IN"))
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
    findings += scan_prose_markers()
    findings += scan_status_headers()
    findings += scan_retired_tree_pointers()
    findings += scan_orphan_tools()
    findings += scan_audit_structural()
    findings += scan_unregistered_terms()
    findings += scan_integrity_pins()
    findings += scan_quarantine()
    findings += scan_audit_exclusions()
    findings += scan_parse_failures()  # last: after every _load_* has run
    # stable order: category, then id — deterministic (no timestamps anywhere)
    findings.sort(key=lambda f: (f["category"], f["id"]))

    # stable within-category order is already set; now also rank by severity for consumers that want
    # a triaged view (fix #4). Keep the canonical `findings` in (category,id) order for determinism;
    # expose the severity rollup in totals so the dashboard can sort/filter without re-deriving it.
    by_cat = Counter(f["category"] for f in findings)
    by_sev = Counter(f.get("severity", DEFAULT_SEVERITY) for f in findings)
    by_lane = defaultdict(lambda: defaultdict(int))
    for f in findings:
        by_lane[f["lane"]]["total"] += 1
        by_lane[f["lane"]][f["category"]] += 1

    payload = {
        "schema_version": 2,
        "generator": "tools/observability/build_incompleteness.py",
        "note": "GENERATED — the Incompleteness Ledger. Surfaces incompleteness across a BOUNDED, "
                "GROWING set of categories (see totals.by_category), each carrying a `severity` "
                "(high/med/low, see totals.by_severity). It is deliberately NOT claimed exhaustive: "
                "known coverage gaps are listed in `coverage_gaps` so the ledger surfaces its OWN "
                "incompleteness. Nothing within a covered category is culled to stay 'signal-heavy'.",
        "totals": {"findings": len(findings), "by_category": dict(sorted(by_cat.items())),
                   "by_severity": {s: by_sev.get(s, 0) for s in ("high", "med", "low")}},
        "by_lane": {ln: dict(by_lane[ln]) for ln in LANE_ORDER if ln in by_lane},
        "prose_marker_rollup": prose_marker_rollup(),
        "coverage_gaps": COVERAGE_GAPS,
        "findings": findings,
    }
    return payload


# The ledger surfaces its OWN incompleteness — categories not yet scanned (honesty over overclaim).
# Add a scanner and delete the line; never let this list quietly imply the ledger is exhaustive.
COVERAGE_GAPS = [
    "null/empty REQUIRED fields in registries other than module_contracts (id_reservations, "
    "descriptor_registry 'IN FLUX' roster, names_index, …) are not yet structurally scanned",
    "co-file _index/_infill pairing gaps are owned by ci_co_file_checker and not yet absorbed here",
    "retired designs/-tree pointers in references/ & registers/ ARE now surfaced "
    "(stale_retired_pointer); pointers in docs/comments and non-designs/ dead paths are not yet validated",
    "which of the canonical_sha pins are actually STALE (vs merely advisory) is delegated to "
    "freshness_gate.py --update, not enumerated here",
    "the alias(<4)/paragraph(<50)/citation(<2) audit floors are recorded as COUNTS by "
    "vector_audit.audit_exclusions, not enumerated per-item",
    "prose/status scans cover the canonical doc roots only; audit/ and workplans/ working docs are "
    "intentionally out of scope (they PROPOSE, not assert)",
    "the vector-audit sees the design CITATION/registry structure, NOT the sim .py behaviour, the "
    "typed engine/params VALUES, or actual runtime — a wrong number or a broken simulation is "
    "invisible to it (sim stubs ARE surfaced via sim_not_implemented, but only the stubs, not logic)",
    "vector-audit Mode D (cascade sinks) uses a capped return-path search; in this dense corpus the "
    "cap trips heavily, so Mode-D findings are UNVERIFIED LEADS (each carries the trip count) — the "
    "cap is not yet raised/replaced with an SCC decomposition",
]


CATEGORY_LABEL = {
    "contract_doc_null": "Module contracts with no home doc (doc:null)",
    "contract_doc_dead": "Module contracts whose doc path does not exist (dead pointer)",
    "contract_island": "Island modules (no emits AND no consumes — untraceable)",
    "contract_no_resolver": "Modules with no resolver",
    "contract_assumption": "Contracts carrying [ASSUMPTION]/[STUB] markers",
    "contract_missing_entirely": "Modules in the graph with NO contract entry at all",
    "key_orphan_emit": "Orphan-emit Keys (emitted, no consumer)",
    "key_unemitted_consume": "Unemitted-consume Keys (consumed, never emitted)",
    "sim_not_implemented": "Runtime stubs (raise NotImplementedError)",
    "code_marker": "Code gap markers (TODO/FIXME/HACK/TBD/STUB in .py)",
    "prose_marker": "Prose gap markers (TODO/FIXME/TBD/??? in .md docs)",
    "status_noncurrent": "Docs whose Status is not current (PROPOSED/DRAFT/STALE/…)",
    "apparatus_orphan": "Orphaned tools/skills (no importer/invoker)",
    "stale_retired_pointer": "Registries still pointing at the retired designs/ tree (alias-hidden)",
    "unregistered_term": "Frequent authored terms with NO registered token (missing registrations)",
    "audit_implied_missing": "Implied-but-never-cited connections (vector-audit Mode B)",
    "audit_isolate": "Structurally isolated tokens (vector-audit Mode H)",
    "audit_notional": "Notional citations — cited but no metadata support (vector-audit Mode C)",
    "audit_cascade_sink": "Cascade sinks — flowed into, never back out (vector-audit Mode D)",
    "audit_sparse": "Sparse-context tokens — thinly developed (vector-audit Mode E)",
    "audit_throughline_orphan": "Throughline orphans — ≤2 substantiating paragraphs (vector-audit Mode F)",
    "audit_vocab_debt": "Vocabulary debt — struck/deprecated terms still in use (vector-audit Mode G)",
    "audit_schema_mismatch": "Audit feed schema mismatch (two-observatory handshake broke)",
    "integrity_unverified_pin": "Unverified integrity pins (canonical_sha)",
    "register_quarantined": "Quarantined/stale registers",
    "register_phantom_source": "Registry rows indexing a non-existent source file",
    "audit_excluded_system": "Systems the vector-audit denylists",
    "parse_failure": "Files that FAILED to parse (invisible to every other scanner)",
}


def to_markdown(p):
    lines = ["# Incompleteness Ledger", "",
             "_GENERATED by `tools/observability/build_incompleteness.py` — do not hand-edit._", "",
             "The point of the vectorization tool is to surface what is missing. This ledger absorbs "
             "incompleteness across a **bounded, growing** set of categories — nothing *within* a covered "
             "category is culled to stay 'signal-heavy'. It is **not** claimed exhaustive: its own known "
             "coverage gaps are listed below so the ledger surfaces its own incompleteness.", "",
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
    if p.get("coverage_gaps"):
        lines.append("## ⚠ Known coverage gaps (this ledger's OWN incompleteness)")
        lines.append("")
        lines.append("_The ledger is not exhaustive. Categories it does not yet scan:_")
        lines.append("")
        for gap in p["coverage_gaps"]:
            lines.append(f"- {gap}")
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
