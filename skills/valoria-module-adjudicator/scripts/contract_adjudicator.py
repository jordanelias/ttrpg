#!/usr/bin/env python3
"""contract_adjudicator.py — module-contract assessor for the Valoria engine.

Checks A1-A9 over references/module_contracts.yaml against the canonical
Key Type Registry and canonical_sources declarations. Violations exit 1;
warnings alone exit 0. Importable for future hook wiring:

    from contract_adjudicator import adjudicate
    violations, warnings = adjudicate(contracts, registry_md, sources_yaml)

Design constraints (SKILL.md is normative):
- Family derives from the type_id PREFIX, never the registry section a type
  is housed under (registry §8 houses Class-B types outside their families).
- The 'scene.' prefix legitimately spans two families (scene_event,
  scene_outcome): A9 therefore compares TOTAL declared vs parsed counts and
  reports per-prefix tallies informationally; it does not claim per-family
  resolution it cannot ground.
- Unknown scale/resolver enum members are WARNINGS (enums are
  [ASSUMPTION]-grade pending Jordan ratification) so a wrong enum cannot
  false-halt work.
- Stubs (status: stub) must carry no edges; edges on a stub are violations.
"""
import argparse
import re
import sys

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("contract_adjudicator requires PyYAML")

SCALES = {"personal", "scene", "settlement", "territory", "provincial",
          "peninsula", "thread"}
RESOLVERS = {"dice_pool", "d_sigma", "deterministic_accounting",
             "clock_advance", "armature_dot_product", "state_reader",
             "manifest"}
BUCKETS = {"pool", "derived_value", "track", "clock"}
TYPE_RE = re.compile(r"^###\s+([a-z_]+\.[a-z_]+)\s*$", re.M)


# ── canon parsing ──────────────────────────────────────────────────────────

def parse_registry_types(registry_md: str) -> set:
    """Registered type_ids = all '### family.subtype' headings."""
    return set(TYPE_RE.findall(registry_md))


def parse_declared_total(registry_md: str):
    """Declared total from the §9 summary table's **Total** row; None if absent."""
    m = re.search(r"\|\s*\*\*Total\*\*\s*\|\s*\*\*(\d+)\*\*", registry_md)
    return int(m.group(1)) if m else None


# ── wildcard semantics ─────────────────────────────────────────────────────
# Contracts mirror canon's family-level statements: "da.*" (family wildcard)
# and "*" (universal, engine-stream readers). Three distinct questions:
#   registry closure  -> _wild_registered (does the pattern land on ≥1 type?)
#   producer wiring   -> _pat_overlap     (symbolic; independent of registry,
#                        so one fault yields one finding, not two)
#   orphan detection  -> _pat_overlap, with global "*" subscriptions EXCLUDED
#                        (a universal reader must never silence A4)

def _wild_registered(pattern: str, registered: set) -> bool:
    if pattern == "*":
        return bool(registered)
    if pattern.endswith(".*"):
        pre = pattern[:-1]                      # keep the dot: 'da.'
        return any(t.startswith(pre) for t in registered)
    return pattern in registered


def _pat_overlap(a: str, b: str) -> bool:
    """Can pattern a and pattern b denote at least one common type? Symbolic."""
    if not a or not b:
        return False
    if a == "*" or b == "*":
        return True
    aw, bw = a.endswith(".*"), b.endswith(".*")
    if aw and bw:
        return a[:-1] == b[:-1]
    if aw:
        return b.startswith(a[:-1])
    if bw:
        return a.startswith(b[:-1])
    return a == b


# ── checks ─────────────────────────────────────────────────────────────────

def adjudicate(contracts: dict, registry_md: str, sources_text: str):
    violations, warnings = [], []
    V, W = violations.append, warnings.append

    modules = contracts.get("modules", [])
    if not isinstance(modules, list) or not modules:
        V("A1: contracts file has no 'modules' list")
        return violations, warnings

    registered = parse_registry_types(registry_md)
    by_name = {}

    # A1 — schema validity (+ stub edge ban, enum warnings)
    for m in modules:
        name = m.get("module")
        if not name:
            V("A1: module record missing 'module' name")
            continue
        if name in by_name:
            V(f"A1: duplicate module record '{name}'")
        by_name[name] = m
        status = m.get("status")
        if status not in ("extracted", "stub"):
            V(f"A1 [{name}]: status must be extracted|stub, got {status!r}")
        if status == "stub" and (m.get("emits") or m.get("consumes")):
            V(f"A1 [{name}]: stub carries edges — stubs must be empty")
        for s in m.get("scales", []) or []:
            if s not in SCALES:
                W(f"A1 [{name}]: unknown scale '{s}' (enum is ASSUMPTION-grade)")
        r = m.get("resolver")
        if status == "extracted" and r and r not in RESOLVERS:
            W(f"A1 [{name}]: unknown resolver '{r}' (enum is ASSUMPTION-grade)")
        for st in m.get("state", []) or []:
            if st.get("bucket") not in BUCKETS:
                V(f"A1 [{name}]: state '{st.get('name')}' bucket "
                  f"{st.get('bucket')!r} not in {sorted(BUCKETS)}")

    emitters = {}            # emitted pattern -> [module names]
    consume_pats = []        # (pattern, module) — global '*' EXCLUDED (A4)
    global_readers = []      # modules consuming '*' (reported, never silencing)
    for m in modules:
        name = m.get("module", "?")
        for e in m.get("emits", []) or []:
            emitters.setdefault(e.get("type"), []).append(name)
        for c in m.get("consumes", []) or []:
            t = c.get("type")
            if t == "*":
                global_readers.append(name)
            else:
                consume_pats.append((t, name))

    # A2 — emit-closure (family wildcards pass iff the family is inhabited)
    for t, who in sorted(emitters.items()):
        if not t:
            V(f"A2: emission with empty type (emitters: {', '.join(who)})")
        elif not _wild_registered(t, registered):
            kind = ("family wildcard lands on zero registered types"
                    if t.endswith(".*") else "not in Key Type Registry")
            V(f"A2: emitted type '{t}' {kind} "
              f"(emitters: {', '.join(who)}) — registry §10 extension required")

    # A3 — consume-closure
    for m in modules:
        name = m.get("module", "?")
        for c in m.get("consumes", []) or []:
            t, frm = c.get("type"), c.get("from", [])
            if not t:
                V(f"A3 [{name}]: consume entry with empty type")
                continue
            if not _wild_registered(t, registered):
                kind = ("family wildcard lands on zero registered types"
                        if t.endswith(".*") else "not in Key Type Registry")
                V(f"A3 [{name}]: consumed type '{t}' {kind}")
            if frm == "engine" or frm == ["engine"]:
                continue
            declared = [p for p in (frm or []) if p in by_name]
            if not frm:
                V(f"A3 [{name}]: consume '{t}' declares no producer "
                  f"(use from: [modules] or engine)")
            elif not declared:
                V(f"A3 [{name}]: consume '{t}' producers {frm} not in contracts")
            else:
                for p in declared:
                    ppats = [e.get("type")
                             for e in by_name[p].get("emits", []) or []]
                    if not any(_pat_overlap(t, ep) for ep in ppats):
                        V(f"A3 [{name}]: declared producer '{p}' of '{t}' "
                          f"does not emit it")

    # A4 — orphan emissions + W-GAP notes
    # Family-wildcard subscriptions (e.g. 'scene.*') are real declared edges
    # and count as consumption; global '*' subscriptions are universal readers
    # (articulation, fieldwork Memory Query) and are deliberately excluded so
    # they cannot silence orphan detection.
    for m in modules:
        name = m.get("module", "?")
        for e in m.get("emits", []) or []:
            t = e.get("type")
            if e.get("terminal") or not t:
                continue
            if not any(_pat_overlap(t, cp) for cp, _ in consume_pats):
                gr = (f" (universal readers {sorted(set(global_readers))} "
                      f"see it but do not count)" if global_readers else "")
                W(f"A4 [{name}]: non-terminal emission '{t}' has no "
                  f"declared consumer{gr}")
        for gnote in m.get("gap_notes", []) or []:
            W(f"W-GAP [{name}]: {gnote}")

    # A5 — derived-value write guard
    for m in modules:
        name = m.get("module", "?")
        for st in m.get("state", []) or []:
            if st.get("bucket") == "derived_value" and st.get("writable"):
                V(f"A5 [{name}]: derived value '{st.get('name')}' marked "
                  f"writable — route the delta to its substrate "
                  f"(derived_stats §11)")

    # A6 — cross-scale edges require a transition
    for m in modules:
        name = m.get("module", "?")
        cscales = set(m.get("scales", []) or [])
        has_trans = bool(m.get("transitions"))
        for c in m.get("consumes", []) or []:
            frm = c.get("from", [])
            if frm in ("engine", ["engine"]):
                continue
            for p in frm or []:
                pm = by_name.get(p)
                if not pm:
                    continue
                pscales = set(pm.get("scales", []) or [])
                if cscales and pscales and not (cscales & pscales):
                    if not (has_trans or pm.get("transitions")):
                        V(f"A6 [{name}←{p}]: edge '{c.get('type')}' crosses "
                          f"scales {sorted(pscales)}→{sorted(cscales)} with no "
                          f"transitions entry on either side "
                          f"(scale_transitions §3/§5)")

    # A7 — cycles must carry loop annotations
    graph = {m.get("module"): set() for m in modules}
    for m in modules:
        for c in m.get("consumes", []) or []:
            frm = c.get("from", [])
            if frm in ("engine", ["engine"]):
                continue
            for p in frm or []:
                if isinstance(p, str) and p in graph:
                    graph[p].add(m.get("module"))   # producer -> consumer
    for scc in _sccs(graph):
        if len(scc) < 2 and not (len(scc) == 1 and
                                 next(iter(scc)) in graph[next(iter(scc))]):
            continue
        annotated = False
        for n in scc:
            for lp in by_name.get(n, {}).get("loops", []) or []:
                if lp.get("open") or lp.get("with") in scc:
                    annotated = True
        if not annotated:
            V(f"A7: cycle {sorted(scc)} carries no loops[] damper/cap "
              f"annotation (Lesson 5)")

    # A8 — doc anchored in canonical_sources
    for m in modules:
        name, doc = m.get("module", "?"), m.get("doc")
        if m.get("status") != "extracted":
            continue
        if not doc:
            W(f"W-DOC [{name}]: extracted module with no located home doc "
              f"(edges grounded in sources[]: "
              f"{'; '.join(m.get('sources', []) or ['NONE'])})")
            if not m.get("sources"):
                V(f"A8 [{name}]: extracted, no doc AND no sources — ungrounded")
        elif doc not in sources_text:
            V(f"A8 [{name}]: doc '{doc}' not declared in canonical_sources")

    # A9 — registry self-check
    declared = parse_declared_total(registry_md)
    if declared is not None and declared != len(registered):
        W(f"A9: registry §9 declares {declared} types; parsed "
          f"{len(registered)} '###' type headings — registry-internal drift")
    prefixes = {}
    for t in registered:
        prefixes[t.split('.')[0]] = prefixes.get(t.split('.')[0], 0) + 1
    W(f"A9-info: parsed prefix tally {dict(sorted(prefixes.items()))} "
      f"(scene.* spans scene_event + scene_outcome by design)")

    return violations, warnings


def _sccs(graph):
    """Tarjan strongly connected components (iterative)."""
    idx, low, onstk, stack, out = {}, {}, set(), [], []
    counter = [0]

    def strong(v):
        work = [(v, iter(graph.get(v, ())))]
        idx[v] = low[v] = counter[0]; counter[0] += 1
        stack.append(v); onstk.add(v)
        while work:
            node, it = work[-1]
            advanced = False
            for w in it:
                if w not in idx:
                    idx[w] = low[w] = counter[0]; counter[0] += 1
                    stack.append(w); onstk.add(w)
                    work.append((w, iter(graph.get(w, ()))))
                    advanced = True
                    break
                elif w in onstk:
                    low[node] = min(low[node], idx[w])
            if advanced:
                continue
            work.pop()
            if work:
                low[work[-1][0]] = min(low[work[-1][0]], low[node])
            if low[node] == idx[node]:
                comp = set()
                while True:
                    w = stack.pop(); onstk.discard(w); comp.add(w)
                    if w == node:
                        break
                out.append(comp)

    for v in graph:
        if v not in idx:
            strong(v)
    return out


# ── CLI ────────────────────────────────────────────────────────────────────

def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--contracts", required=True)
    ap.add_argument("--registry", required=True)
    ap.add_argument("--sources", required=True)
    a = ap.parse_args()
    contracts = yaml.safe_load(open(a.contracts))
    registry_md = open(a.registry).read()
    sources_text = open(a.sources).read()
    violations, warnings = adjudicate(contracts, registry_md, sources_text)
    print(f"== contract_adjudicator: {len(violations)} violation(s), "
          f"{len(warnings)} warning(s) ==")
    for v in violations:
        print("VIOLATION:", v)
    for w in warnings:
        print("warning:  ", w)
    sys.exit(1 if violations else 0)


if __name__ == "__main__":
    main()
