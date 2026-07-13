#!/usr/bin/env python3
"""
structure_audit.py — the Structural Observatory's ARCHITECTURE layers (WS0b core).

Companion to scripts/vector_audit.py (the L0 prose layer). This builds the code /
module / wiring layers of the observatory — deterministic, working-tree only, and
depending on nothing beyond the Python standard library + PyYAML (so it runs in CI
where only pyyaml is installed). No numpy/sklearn/networkx: the graph algorithms
(Tarjan SCC, articulation points) are implemented here.

Layers built (per the plan's WS0 layer stack):
  * G_code — AST import graph over sim/ + tools/ (real `import`/`from`, not regex).
      Finds import cycles (SCC), cut-vertices (single points of failure), orphans.
  * L2 — module/subsystem wiring graph from references/module_contracts.yaml:
      producer -> consumer edges (from `consumes[].from`), Key emit/consume CLOSURE
      checks (dangling non-terminal emits; phantom producers — a consume whose named
      source does not actually emit that Key type), scale grouping, and cross-scale
      locality (does the wiring cluster by scale, per NS3?).

GOVERNANCE (the anti-fabrication discipline at graph scale — plan §WS0):
  * Working tree only; deterministic; no network.
  * PROVENANCE TAGS: module_contracts is ~37% notional (doc:null / [ASSUMPTION]-grade
      resolvers). Every L2 module carries a `notional` flag; findings on notional
      modules are reported in a separate, lower-confidence bucket. This tool MEASURES;
      it never gates a merge (pytest + import-smoke do).
  * Output reduces to a prioritized register + a scorecard.

CLI:
    python3 structure_audit.py --repo-root . --output-dir <run>
"""
import argparse
import ast
import json
import os
import re
import sys
from collections import defaultdict, deque
from pathlib import Path

try:
    import yaml
except Exception:  # pragma: no cover
    sys.exit("structure_audit requires PyYAML")


# ──────────────────────────── GRAPH ALGORITHMS (stdlib) ──────────────────────

def tarjan_scc(adj):
    """Strongly-connected components of a digraph {node: iterable(node)}.
    Iterative Tarjan (recursion-safe on large graphs). Returns list of components
    (each a list of nodes); components of size >1 (or self-loops) are cycles."""
    index = {}
    low = {}
    on_stack = {}
    stack = []
    result = []
    counter = [0]
    nodes = list(adj.keys())

    for root in nodes:
        if root in index:
            continue
        work = [(root, iter(adj.get(root, ())))]
        while work:
            node, it = work[-1]
            if node not in index:
                index[node] = low[node] = counter[0]
                counter[0] += 1
                stack.append(node)
                on_stack[node] = True
            advanced = False
            for succ in it:
                if succ not in index:
                    work.append((succ, iter(adj.get(succ, ()))))
                    advanced = True
                    break
                elif on_stack.get(succ):
                    low[node] = min(low[node], index[succ])
            if advanced:
                continue
            if low[node] == index[node]:
                comp = []
                while True:
                    w = stack.pop()
                    on_stack[w] = False
                    comp.append(w)
                    if w == node:
                        break
                result.append(comp)
            work.pop()
            if work:
                parent = work[-1][0]
                low[parent] = min(low[parent], low[node])
    return result


def articulation_points(adj):
    """Cut-vertices of the UNDIRECTED projection of {node: iterable(node)}.
    A node whose removal increases the number of connected components — a single
    point of failure in the dependency structure. Iterative DFS (Tarjan)."""
    undirected = defaultdict(set)
    for u, nbrs in adj.items():
        undirected.setdefault(u, set())
        for v in nbrs:
            if v == u:
                continue
            undirected[u].add(v)
            undirected[v].add(u)
    visited = {}
    disc = {}
    low = {}
    parent = {}
    ap = set()
    timer = [0]
    for start in list(undirected.keys()):
        if start in visited:
            continue
        root_children = 0
        stack = [(start, iter(sorted(undirected[start])))]
        visited[start] = True
        disc[start] = low[start] = timer[0]
        timer[0] += 1
        parent[start] = None
        while stack:
            node, it = stack[-1]
            advanced = False
            for nb in it:
                if nb not in visited:
                    parent[nb] = node
                    if node == start:
                        root_children += 1
                    visited[nb] = True
                    disc[nb] = low[nb] = timer[0]
                    timer[0] += 1
                    stack.append((nb, iter(sorted(undirected[nb]))))
                    advanced = True
                    break
                elif nb != parent.get(node):
                    low[node] = min(low[node], disc[nb])
            if advanced:
                continue
            stack.pop()
            if stack:
                par = stack[-1][0]
                low[par] = min(low[par], low[node])
                if parent.get(par) is not None and low[node] >= disc[par]:
                    ap.add(par)
        if root_children > 1:
            ap.add(start)
    return ap


def degrees(adj, nodes):
    out = {n: len(set(adj.get(n, ()))) for n in nodes}
    indeg = defaultdict(int)
    for u, nbrs in adj.items():
        for v in set(nbrs):
            indeg[v] += 1
    return {n: {'in': indeg.get(n, 0), 'out': out.get(n, 0)} for n in nodes}


# ──────────────────────────── G_CODE — AST IMPORT GRAPH ──────────────────────

CODE_ROOTS = ('sim', 'tools')
SKIP_DIR_PARTS = {'__pycache__', 'tests', 'test', 'deprecated', 'archives'}


def _module_name(rel_path):
    """sim/provincial/faction_action.py -> sim.provincial.faction_action;
    .../__init__.py -> the package name."""
    p = rel_path[:-3] if rel_path.endswith('.py') else rel_path
    parts = p.split('/')
    if parts and parts[-1] == '__init__':
        parts = parts[:-1]
    return '.'.join(parts)


def collect_py_modules(root):
    """{dotted_module: relpath} for every internal .py under the code roots
    (skipping caches/tests/deprecated/archives)."""
    mods = {}
    for base in CODE_ROOTS:
        for dirpath, dirnames, filenames in os.walk(root / base):
            rel_dir = os.path.relpath(dirpath, root).replace(os.sep, '/')
            if any(part in SKIP_DIR_PARTS for part in rel_dir.split('/')):
                continue
            dirnames[:] = [d for d in dirnames if d not in SKIP_DIR_PARTS]
            for fn in filenames:
                if fn.endswith('.py'):
                    rel = os.path.relpath(os.path.join(dirpath, fn), root).replace(os.sep, '/')
                    mods[_module_name(rel)] = rel
    return mods


def _resolve_internal(target, known):
    """Map an imported dotted name to the known internal module it (or its nearest
    package prefix) denotes, else None."""
    if target in known:
        return target
    parts = target.split('.')
    while parts:
        cand = '.'.join(parts)
        if cand in known:
            return cand
        parts = parts[:-1]
    return None


def build_g_code(root, modules):
    """Directed import graph over internal modules. Edge A -> B iff A imports B."""
    known = set(modules)
    g = defaultdict(set)
    parse_errors = []
    for mod, rel in modules.items():
        g.setdefault(mod, set())
        try:
            tree = ast.parse((root / rel).read_text(encoding='utf-8', errors='replace'), filename=rel)
        except SyntaxError as e:
            parse_errors.append(f'{rel}: {e}')
            continue
        pkg = mod.rsplit('.', 1)[0] if '.' in mod else mod
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    tgt = _resolve_internal(alias.name, known)
                    if tgt and tgt != mod:
                        g[mod].add(tgt)
            elif isinstance(node, ast.ImportFrom):
                base = node.module or ''
                if node.level:  # relative import — resolve against this file's package
                    base = pkg + ('.' + base if base else '')
                # try the module, then module.name for `from pkg import submod`
                cands = [base] + [f'{base}.{a.name}' for a in node.names if base]
                for c in cands:
                    tgt = _resolve_internal(c, known)
                    if tgt and tgt != mod:
                        g[mod].add(tgt)
    return g, parse_errors


# ──────────────────────────── L2 — MODULE WIRING GRAPH ───────────────────────

def _as_list(v):
    """module_contracts `from:` is sometimes a bare string, sometimes a list — a
    real data hazard (iterating the string yields characters). Normalize."""
    if v is None:
        return []
    if isinstance(v, str):
        return [v]
    if isinstance(v, list):
        return [x for x in v if isinstance(x, str)]
    return []


def build_l2(root):
    """L2 module graph + closure findings from references/module_contracts.yaml.
    Returns (graph, modules_meta, findings)."""
    path = root / 'references' / 'module_contracts.yaml'
    raw = path.read_text(encoding='utf-8', errors='replace')
    data = yaml.safe_load(raw) or {}
    mods = data.get('modules', []) or []
    names = {m.get('module') for m in mods if isinstance(m, dict)}

    meta = {}
    emit_index = defaultdict(set)   # key_type -> {modules that emit it}
    emit_terminal = {}              # (module, type) -> terminal?
    for m in mods:
        if not isinstance(m, dict):
            continue
        name = m.get('module')
        doc = m.get('doc')
        resolver = m.get('resolver')
        notional = (not doc) or (resolver in (None, 'None'))
        meta[name] = {
            'scales': m.get('scales') or [], 'resolver': resolver,
            'doc': doc, 'status': m.get('status'),
            'notional': bool(notional),
        }
        for e in (m.get('emits') or []):
            if isinstance(e, dict) and e.get('type'):
                emit_index[e['type']].add(name)
                emit_terminal[(name, e['type'])] = bool(e.get('terminal'))

    g = defaultdict(set)
    for n in names:
        g.setdefault(n, set())
    consume_index = defaultdict(set)  # key_type -> {consumers}
    edges_meta = []
    findings = {'phantom_producer': [], 'dangling_emit': [], 'doc_null': [],
                'unconsumed_terminal_ok': 0}

    for m in mods:
        if not isinstance(m, dict):
            continue
        dst = m.get('module')
        for c in (m.get('consumes') or []):
            if not isinstance(c, dict):
                continue
            ktype = c.get('type')
            if not ktype or ktype == '*':      # wildcard consume — skip closure logic
                continue
            for src in _as_list(c.get('from')):
                if src in names:
                    g[src].add(dst)
                    edges_meta.append({'src': src, 'dst': dst, 'type': ktype})
                consume_index[ktype].add(dst)
                # phantom producer: src named as a source but does not emit ktype
                if src in names and src not in emit_index.get(ktype, set()):
                    findings['phantom_producer'].append(
                        {'consumer': dst, 'named_source': src, 'type': ktype,
                         'src_notional': meta.get(src, {}).get('notional', False)})

    # dangling emit: a non-terminal emit that nobody consumes
    for (mod, ktype), terminal in emit_terminal.items():
        if ktype not in consume_index:
            if terminal:
                findings['unconsumed_terminal_ok'] += 1
            else:
                findings['dangling_emit'].append(
                    {'emitter': mod, 'type': ktype,
                     'notional': meta.get(mod, {}).get('notional', False)})

    for name, mm in meta.items():
        if not mm['doc']:
            findings['doc_null'].append(name)

    assumption_count = raw.count('[ASSUMPTION]')
    return g, meta, edges_meta, findings, assumption_count


def cross_scale_locality(g, meta):
    """Per NS3: what fraction of L2 edges stay within a scale vs cross scales.
    High cross-scale fraction = the wiring does not cluster by scale."""
    intra = cross = 0
    per_module = {}
    for src, dsts in g.items():
        s_scales = set(meta.get(src, {}).get('scales', []))
        sm_intra = sm_cross = 0
        for dst in dsts:
            d_scales = set(meta.get(dst, {}).get('scales', []))
            if s_scales & d_scales:
                intra += 1; sm_intra += 1
            else:
                cross += 1; sm_cross += 1
        if sm_intra + sm_cross:
            per_module[src] = {'intra': sm_intra, 'cross': sm_cross}
    total = intra + cross
    return {'intra': intra, 'cross': cross,
            'cross_fraction': round(cross / total, 3) if total else 0.0,
            'per_module': per_module}


# ──────────────────────────── OUTPUT ─────────────────────────────────────────

def _cycles(scc):
    return [sorted(c) for c in scc if len(c) > 1]


def run(root, out):
    root, out = Path(root), Path(out)
    (out / 'data').mkdir(parents=True, exist_ok=True)

    print('[G_code] parsing sim/ + tools/ imports (AST)...')
    modules = collect_py_modules(root)
    g_code, parse_errors = build_g_code(root, modules)
    code_nodes = list(modules)
    code_scc = tarjan_scc(g_code)
    code_cycles = _cycles(code_scc)
    code_cuts = articulation_points(g_code)
    code_deg = degrees(g_code, code_nodes)
    code_orphans = sorted(n for n in code_nodes
                          if code_deg[n]['in'] == 0
                          and not n.endswith('.__main__')
                          and not n.split('.')[-1].startswith('_'))
    print(f'         {len(code_nodes)} modules, '
          f'{sum(len(v) for v in g_code.values())} import edges, '
          f'{len(code_cycles)} cycle(s), {len(code_cuts)} cut-vertex(es)')

    print('[L2] building module_contracts wiring graph...')
    g_l2, meta, edges_meta, findings, assumption_count = build_l2(root)
    l2_nodes = list(meta)
    l2_scc = tarjan_scc(g_l2)
    l2_cycles = _cycles(l2_scc)  # cross-check against the contracts' own `loops` field
    l2_deg = degrees(g_l2, l2_nodes)
    l2_cuts = articulation_points(g_l2)
    locality = cross_scale_locality(g_l2, meta)
    print(f'     {len(l2_nodes)} modules, {len(edges_meta)} wiring edges, '
          f'{len(findings["phantom_producer"])} phantom-producer, '
          f'{len(findings["dangling_emit"])} dangling-emit, '
          f'{len(findings["doc_null"])} doc:null')

    # ---- JSON ----
    def dump(name, obj):
        (out / 'data' / name).write_text(json.dumps(obj, indent=1, sort_keys=True), encoding='utf-8')
    dump('g_code.json', {k: sorted(v) for k, v in g_code.items()})
    dump('g_l2.json', {k: sorted(v) for k, v in g_l2.items()})
    dump('structure_metrics.json', {
        'code': {'nodes': len(code_nodes), 'edges': sum(len(v) for v in g_code.values()),
                 'cycles': code_cycles, 'cut_vertices': sorted(code_cuts),
                 'orphans': code_orphans, 'parse_errors': parse_errors},
        'l2': {'nodes': len(l2_nodes), 'edges': len(edges_meta), 'cycles': l2_cycles,
               'cut_vertices': sorted(l2_cuts), 'locality': locality,
               'assumption_markers': assumption_count},
        'findings': findings,
    })

    # ---- register (primary deliverable) ----
    top_code_hubs = sorted(code_nodes, key=lambda n: -(code_deg[n]['in'] + code_deg[n]['out']))[:12]
    top_l2_hubs = sorted(l2_nodes, key=lambda n: -(l2_deg[n]['in'] + l2_deg[n]['out']))[:12]
    real_phantoms = [p for p in findings['phantom_producer'] if not p['src_notional']]
    notional_phantoms = [p for p in findings['phantom_producer'] if p['src_notional']]
    real_dangling = [d for d in findings['dangling_emit'] if not d['notional']]

    L = []
    L.append('# Structure register — architecture layers (G_code + L2)')
    L.append('')
    L.append('Deterministic, working-tree only. **Measures; does not gate** (pytest + import-smoke gate). '
             'Provenance: L2 is built on `module_contracts.yaml`, which carries '
             f'{assumption_count} `[ASSUMPTION]` markers and {len(findings["doc_null"])} `doc:null` modules — '
             'findings on those are bucketed as lower-confidence.')
    L.append('')
    L.append(f'**Scorecard:** code-modules={len(code_nodes)}, import-edges={sum(len(v) for v in g_code.values())}, '
             f'import-cycles={len(code_cycles)}, code-cut-vertices={len(code_cuts)}, code-orphans={len(code_orphans)}; '
             f'l2-modules={len(l2_nodes)}, wiring-edges={len(edges_meta)}, l2-cycles={len(l2_cycles)}, '
             f'phantom-producers={len(real_phantoms)}(+{len(notional_phantoms)} notional), '
             f'dangling-emits={len(real_dangling)}, cross-scale-fraction={locality["cross_fraction"]}.')
    L.append('')

    def section(title, rows, fmt, empty='(none)'):
        L.append(f'## {title}')
        L.append(empty if not rows else '')
        for r in rows[:20]:
            L.append('- ' + fmt(r))
        L.append('')

    section('L2 phantom producers — a consume names a source that does NOT emit that Key '
            '(canon-grade; the mass_battle `scene_outcome.battle_concluded` class)',
            real_phantoms,
            lambda p: f"`{p['consumer']}` consumes `{p['type']}` from `{p['named_source']}`, "
                      f"which emits no such Key")
    section('L2 dangling emits — a non-terminal Key emitted but consumed nowhere (canon-grade)',
            real_dangling, lambda d: f"`{d['emitter']}` emits `{d['type']}` — no consumer")
    section('Import cycles (SCC > 1) in sim/ + tools/', code_cycles,
            lambda c: ' ↔ '.join(c[:6]) + (' …' if len(c) > 6 else ''))
    section('Code cut-vertices — single points of failure (removal disconnects the import graph)',
            sorted(code_cuts, key=lambda n: -(code_deg[n]['in'] + code_deg[n]['out'])),
            lambda n: f"`{n}` (in {code_deg[n]['in']}, out {code_deg[n]['out']})")
    section('L2 module cut-vertices — wiring fragility points',
            sorted(l2_cuts, key=lambda n: -(l2_deg[n]['in'] + l2_deg[n]['out'])),
            lambda n: f"`{n}` (in {l2_deg[n]['in']}, out {l2_deg[n]['out']}, "
                      f"{'notional' if meta[n]['notional'] else 'canon'})")
    section('doc:null modules — registered contract, no home design doc (unimplementable spec)',
            sorted(findings['doc_null']), lambda n: f"`{n}`")
    section('Import orphans — internal module nothing imports (dead-ish; verify before removal)',
            code_orphans, lambda n: f"`{n}`")
    section('Code import hubs (highest total degree — change-impact)', top_code_hubs,
            lambda n: f"`{n}` (in {code_deg[n]['in']}, out {code_deg[n]['out']})")
    section('L2 wiring hubs (highest total degree)', top_l2_hubs,
            lambda n: f"`{n}` (in {l2_deg[n]['in']}, out {l2_deg[n]['out']})")
    L.append('## Cross-scale locality (NS3 — does the wiring cluster by scale?)')
    L.append(f"{locality['intra']} intra-scale vs {locality['cross']} cross-scale edges "
             f"({locality['cross_fraction']:.0%} cross). Lower is better-clustered.")
    L.append('')
    if notional_phantoms:
        L.append('## Lower-confidence (findings on notional/[ASSUMPTION] modules)')
        for p in notional_phantoms[:15]:
            L.append(f"- `{p['consumer']}` ← `{p['named_source']}` `{p['type']}` (source notional)")
        L.append('')

    (out / 'structure_register.md').write_text('\n'.join(L), encoding='utf-8')
    print(f'[done] {out}/structure_register.md')
    return findings


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[1])
    ap.add_argument('--repo-root', default='.', help='repo root (working tree)')
    ap.add_argument('--output-dir', required=True, help='audit output folder')
    a = ap.parse_args()
    root = Path(a.repo_root)
    if not (root / 'references' / 'module_contracts.yaml').exists():
        sys.exit(f"not a Valoria repo root (no references/module_contracts.yaml): {root}")
    print(f'[structure_audit] repo root (working tree): {root.resolve()}')
    run(root, a.output_dir)


if __name__ == '__main__':
    main()
