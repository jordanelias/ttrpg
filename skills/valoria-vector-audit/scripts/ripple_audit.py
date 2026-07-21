#!/usr/bin/env python3
"""
ripple_audit.py — Valoria cross-scale RIPPLE / propagation methodology (observatory L3)

The QUALITATIVE complement to vector_audit.py's QUANTITATIVE (vectorized) map: where
vector_audit gives every token numeric coordinates (cite/tl/mu/pp degrees), this makes
the typed dependency CHAINS explicit and traversable in ALL directions and at multiple
scales, and answers the operational question the other observatory layers don't:

    "If I change X, what ripples — downstream (what a change here affects) AND upstream
     (what X actually depends on / its provenance) — and WHY does each hop exist?"

It is a COMPOSITION, not a new parser (CLAUDE.md §8 — never re-derive a rule). It unifies
two already-present observatory graphs into one typed, directed, cross-scale graph:

  * L2 module wiring  — structure_audit.build_l2(): producer -> consumer edges carrying the
      Key type that couples them (the MECHANIC / module scale).
  * L1 formula DAG    — formula_audit.build_contract_edges(): input -> output derivation edges
      carrying the formula/source (the VALUE / quantity scale).

and BRIDGES the two scales so a chain can cross them:

  quantity --reads--> module --emits_consumes(Key)--> module --produces--> quantity

Node kinds: `module` (a subsystem/mechanic) and `quantity` (a value/derived stat/Key output).
Edge types (all oriented src -> dst = "flows into / affects"):
  * emits_consumes  (L2)     module -> module, provenance = Key type
  * derives         (L1)     quantity -> quantity, provenance = formula / source / module
  * produces        (bridge) module -> quantity it computes as a derivation output
  * reads           (bridge) quantity -> module that consumes it as a derivation input

Directions:
  * downstream (forward,  src->dst): a change to X propagates INTO these — the ripple.
  * upstream   (backward, dst->src): X's provenance — what it is computed / built from.

QUANTIZED overlay (optional): pass --vector-run <dir> pointing at a vector_audit run's
`data/degrees.json`; matching module/quantity name-nodes are annotated with their cite/tl/mu/pp
degrees, so the qualitative chain and the quantized coordinate travel together on one node.

Working-tree only (no GitHub fetch). Stdlib + PyYAML only; numpy/sklearn NOT required.
Deterministic. MEASURES, never gates (pytest + the CI gates remain the enforcement boundary).
The graph is PROVENANCE-TAGGED: edges from notional / doc:null / [ASSUMPTION]-grade contract
modules are marked `notional=true` so a ripple through un-authored canon is never mistaken for
a load-bearing one.

Usage:
    # write the full register + machine-hookable graph:
    python3 ripple_audit.py --repo-root . --output-dir <run>
    # ad-hoc query a single node's chains:
    python3 ripple_audit.py --repo-root . --node "faction_state" --direction both --depth 4
    # slice to one scale:
    python3 ripple_audit.py --repo-root . --node "Combat Pool" --layers derives,produces,reads

Outputs (to <output-dir>):
    ripple_register.md          human-visible: counts, hubs, orphans/sinks, a worked WHAT/HOW/WHY
    data/ripple_graph.json      machine-hookable: {nodes, edges} — the surface other tooling hooks into

VERSION: v1 (2026-07-21). Extension points (documented, not yet built): fold in vector_audit's
L0 doc citation graph (design scale), pointer_audit's G_pointer (identifier->key resolution), and
gen_audit's G_generation (supersedes) as additional edge types on the same node namespace.
"""

import sys
import os
import re
import json
import argparse
from collections import defaultdict, deque

import yaml  # noqa: F401  (used transitively by the reused builders; kept explicit for clarity)

# Reuse the sibling observatory layers as THE builders (CLAUDE.md §8). Same scripts/ dir.
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
if _SCRIPT_DIR not in sys.path:
    sys.path.insert(0, _SCRIPT_DIR)
_TOOLS_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(_SCRIPT_DIR))), 'tools')
if _TOOLS_DIR not in sys.path:
    sys.path.insert(0, _TOOLS_DIR)

import structure_audit as sa            # noqa: E402  (the ONE L2 module-wiring builder)
import formula_audit as fa              # noqa: E402  (the ONE L1 derivation-DAG builder)


# ──────────────────────────── GRAPH CONSTRUCTION ────────────────────────────

EDGE_TYPES = ('emits_consumes', 'derives', 'produces', 'reads')
_BRIDGE_LAYER = 'ripple.bridge'


def _load_contracts(root):
    """The single module_contracts.yaml read, handed to formula_audit's builder verbatim."""
    path = os.path.join(str(root), 'references', 'module_contracts.yaml')
    with open(path, encoding='utf-8', errors='replace') as fh:
        return yaml.safe_load(fh) or {}


def build_graph(root):
    """Compose L2 (module wiring) + L1 (formula DAG) into one typed directed graph.

    Returns a dict:
      nodes: {node_id: {'kind': 'module'|'quantity', 'notional': bool, 'scales': [...],
                        'doc': str|None}}
      edges: [ {'src', 'dst', 'type', 'provenance', 'notional', 'module'?} ]
      adj:   {node_id: [edge_index, ...]}   (out-edges)
      radj:  {node_id: [edge_index, ...]}   (in-edges)
    """
    from pathlib import Path
    root = Path(root)

    nodes = {}
    edges = []

    def _node(nid, kind, **attrs):
        n = nodes.get(nid)
        if n is None:
            nodes[nid] = {'kind': kind, 'notional': attrs.get('notional', False),
                          'scales': attrs.get('scales', []), 'doc': attrs.get('doc')}
        else:
            # a node seen as both module and quantity keeps 'module' (the coarser scale);
            # notional is sticky-false (any load-bearing appearance clears the flag).
            if kind == 'module':
                n['kind'] = 'module'
            if not attrs.get('notional', False):
                n['notional'] = False
            if attrs.get('scales'):
                n['scales'] = attrs['scales'] or n['scales']
            if attrs.get('doc') and not n.get('doc'):
                n['doc'] = attrs['doc']
        return nid

    # ---- L2: module -> module (emits_consumes), provenance = Key type ----
    g_l2, meta, edges_meta, findings, _assump = sa.build_l2(root)
    for mod, m in meta.items():
        _node(mod, 'module', notional=m.get('notional', False),
              scales=m.get('scales') or [], doc=m.get('doc'))
    for e in edges_meta:
        src, dst, ktype = e.get('src'), e.get('dst'), e.get('type')
        if not src or not dst or src == dst:
            # self-consume (a module reading a Key it also emits) is a real contract
            # pattern but a NO-OP for cross-node ripple — it only inflates hub degree.
            continue
        notional = nodes.get(src, {}).get('notional', False) or nodes.get(dst, {}).get('notional', False)
        edges.append({'src': _node(src, 'module'), 'dst': _node(dst, 'module'),
                      'type': 'emits_consumes',
                      'provenance': f'Key::{ktype}', 'notional': notional})

    # ---- L1: quantity -> quantity (derives) + module<->quantity bridges ----
    contracts = _load_contracts(root)
    fa_edges, _definitions = fa.build_contract_edges(contracts)
    for e in fa_edges:
        in_node, out_node = e.get('src'), e.get('dst')
        if not in_node or not out_node:
            continue
        mod = e.get('module')
        notional = bool(e.get('notional'))
        formula = e.get('formula')
        source = e.get('source')
        prov = f'formula::{formula}' if formula else (f'source::{source}' if source else 'derivation')
        _node(in_node, 'quantity', notional=notional)
        _node(out_node, 'quantity', notional=notional)
        if in_node != out_node:  # a quantity derived from itself is a no-op for ripple
            edges.append({'src': in_node, 'dst': out_node, 'type': 'derives',
                          'provenance': prov, 'notional': notional, 'module': mod})
        # cross-scale bridges: the owning module PRODUCES the output and READS the input.
        if mod:
            _node(mod, 'module')
            if mod != out_node:
                edges.append({'src': mod, 'dst': out_node, 'type': 'produces',
                              'provenance': f'{_BRIDGE_LAYER}::{mod} derivation', 'notional': notional})
            if in_node != mod:
                edges.append({'src': in_node, 'dst': mod, 'type': 'reads',
                              'provenance': f'{_BRIDGE_LAYER}::{mod} derivation', 'notional': notional})

    adj = defaultdict(list)
    radj = defaultdict(list)
    for i, e in enumerate(edges):
        adj[e['src']].append(i)
        radj[e['dst']].append(i)

    return {'nodes': nodes, 'edges': edges, 'adj': dict(adj), 'radj': dict(radj),
            'l2_findings': findings}


# ──────────────────────────── RIPPLE TRAVERSAL ──────────────────────────────

def ripple(graph, start, direction='both', depth=None, layers=None):
    """Bidirectional depth-limited reachability from `start`.

    direction: 'down' (forward src->dst = what a change affects),
               'up'   (backward dst->src = provenance / dependencies),
               'both'.
    depth:     hop limit (None = unbounded, cycle-safe).
    layers:    iterable of edge types to traverse (None = all EDGE_TYPES) — this is the SLICE.

    Returns {'down': [hop, ...], 'up': [hop, ...]} where each hop is
      {'node', 'kind', 'via_edge': {type, provenance, notional}, 'from', 'depth'}.
    Order is BFS (nearest first); each node reported once per direction (shortest hop).
    """
    if start not in graph['nodes']:
        return {'error': f'unknown node: {start!r}', 'down': [], 'up': []}
    allow = set(layers) if layers else set(EDGE_TYPES)
    edges = graph['edges']

    def walk(index_map, endpoint):
        seen = {start}
        out = []
        q = deque([(start, 0)])
        while q:
            cur, d = q.popleft()
            if depth is not None and d >= depth:
                continue
            for ei in index_map.get(cur, ()):
                e = edges[ei]
                if e['type'] not in allow:
                    continue
                nxt = e[endpoint]
                if nxt in seen:
                    continue
                seen.add(nxt)
                out.append({'node': nxt, 'kind': graph['nodes'].get(nxt, {}).get('kind'),
                            'via_edge': {'type': e['type'], 'provenance': e['provenance'],
                                         'notional': e['notional']},
                            'from': cur, 'depth': d + 1})
                q.append((nxt, d + 1))
        return out

    res = {'node': start, 'kind': graph['nodes'][start]['kind']}
    if direction in ('down', 'both'):
        res['down'] = walk(graph['adj'], 'dst')
    if direction in ('up', 'both'):
        res['up'] = walk(graph['radj'], 'src')
    return res


# ──────────────────────────── QUANTIZED OVERLAY ─────────────────────────────

def attach_vector_degrees(graph, vector_run_dir):
    """Annotate name-matching nodes with a vector_audit run's quantized coordinates
    (cite/tl/mu/pp degrees), so the qualitative node carries its quantized measure.
    Best-effort: matches on exact node id, else a normalized (lower/underscore) form."""
    path = os.path.join(vector_run_dir, 'data', 'degrees.json')
    if not os.path.isfile(path):
        return 0
    with open(path, encoding='utf-8', errors='replace') as fh:
        degs = json.load(fh)

    def norm(s):
        return re.sub(r'[^a-z0-9]+', '', str(s).lower())
    by_norm = {}
    # degrees.json shape: {'cite': {token: n}, 'tl': {...}, 'mu': {...}, 'pp': {...}} OR
    # {token: {cite,tl,mu,pp}} — support both.
    coords = defaultdict(dict)
    if degs and all(k in ('cite', 'tl', 'mu', 'pp') for k in degs):
        for axis, m in degs.items():
            for tok, v in (m or {}).items():
                coords[tok][axis] = v
    else:
        for tok, m in (degs or {}).items():
            if isinstance(m, dict):
                coords[tok] = {k: m.get(k) for k in ('cite', 'tl', 'mu', 'pp') if k in m}
    for tok, c in coords.items():
        by_norm[norm(tok)] = c
    hits = 0
    for nid, n in graph['nodes'].items():
        c = coords.get(nid) or by_norm.get(norm(nid))
        if c:
            n['quantized'] = c
            hits += 1
    return hits


# ──────────────────────────── REPORTING ─────────────────────────────────────

def _degree(graph):
    out = {n: 0 for n in graph['nodes']}
    inn = {n: 0 for n in graph['nodes']}
    for e in graph['edges']:
        out[e['src']] = out.get(e['src'], 0) + 1
        inn[e['dst']] = inn.get(e['dst'], 0) + 1
    return inn, out


def _fmt_hop(h):
    tag = ' ⚠notional' if h['via_edge']['notional'] else ''
    return (f"{h['from']} --{h['via_edge']['type']}[{h['via_edge']['provenance']}]--> "
            f"{h['node']} ({h['kind']}){tag}")


def write_register(graph, out_dir, vector_hits=0):
    from pathlib import Path
    out = Path(out_dir)
    (out / 'data').mkdir(parents=True, exist_ok=True)

    nodes, edges = graph['nodes'], graph['edges']
    inn, outd = _degree(graph)
    n_mod = sum(1 for n in nodes.values() if n['kind'] == 'module')
    n_qty = sum(1 for n in nodes.values() if n['kind'] == 'quantity')
    by_type = defaultdict(int)
    notional_edges = 0
    for e in edges:
        by_type[e['type']] += 1
        notional_edges += bool(e['notional'])
    total_deg = {n: inn[n] + outd[n] for n in nodes}
    hubs = sorted(nodes, key=lambda n: -total_deg[n])[:12]
    orphans = sorted(n for n in nodes if inn.get(n, 0) == 0 and outd.get(n, 0) > 0)   # pure sources
    sinks = sorted(n for n in nodes if outd.get(n, 0) == 0 and inn.get(n, 0) > 0)     # pure sinks
    isolated = sorted(n for n in nodes if inn.get(n, 0) == 0 and outd.get(n, 0) == 0)

    L = []
    L.append('# Ripple register — cross-scale propagation map (observatory L3, v1)')
    L.append('')
    L.append('QUALITATIVE complement to the vector audit\'s quantized map. Composed from '
             'structure_audit L2 (module wiring) + formula_audit L1 (derivation DAG), '
             'bridged across scales. MEASURES, never gates. Provenance-tagged — a `⚠notional` '
             'hop runs through a doc:null / [ASSUMPTION]-grade contract module.')
    L.append('')
    L.append(f'**Nodes:** {len(nodes)} ({n_mod} module · {n_qty} quantity)  ·  '
             f'**Edges:** {len(edges)} ({notional_edges} notional)')
    L.append('**Edge types:** ' + ', '.join(f'{t}={by_type.get(t, 0)}' for t in EDGE_TYPES))
    if vector_hits:
        L.append(f'**Quantized overlay:** {vector_hits} node(s) annotated with vector-audit degrees.')
    L.append('')
    L.append('## What / How / Why')
    L.append('- **WHAT** a node is: its `kind` (module = mechanic/subsystem; quantity = value/derived stat/Key output).')
    L.append('- **HOW** two nodes couple: the edge `type` — `emits_consumes` (a Key flows module→module), '
             '`derives` (a value is computed from another), `produces`/`reads` (a module writes/consumes a value).')
    L.append('- **WHY** the coupling exists: the edge `provenance` — the Key type, formula, or contract source '
             'that established it (never synthesized; read from module_contracts / descriptor_registry).')
    L.append('')
    L.append('## Highest change-impact nodes (by total degree — a change here ripples furthest)')
    for h in hubs:
        q = nodes[h].get('quantized')
        qs = f'  ·  quantized={q}' if q else ''
        L.append(f'- **{h}** ({nodes[h]["kind"]}) — downstream {outd[h]} · upstream {inn[h]}{qs}')
    L.append('')
    # a worked example on the top hub
    if hubs:
        top = hubs[0]
        r = ripple(graph, top, direction='both', depth=2)
        L.append(f'### Worked ripple — `{top}` (depth ≤2)')
        L.append('**Downstream (a change here affects):**')
        for h in r.get('down', [])[:12]:
            L.append(f'- {_fmt_hop(h)}')
        if not r.get('down'):
            L.append('- (nothing downstream — terminal)')
        L.append('**Upstream (this is built from):**')
        for h in r.get('up', [])[:12]:
            L.append(f'- {_fmt_hop(h)}')
        if not r.get('up'):
            L.append('- (nothing upstream — a root/primitive)')
        L.append('')
    L.append('## Structural leads')
    L.append(f'- **Pure sources** (produce, never derived — candidate primitives/inputs): {len(orphans)}')
    L.append('  ' + (', '.join(orphans[:25]) + (' …' if len(orphans) > 25 else '')) if orphans else '  (none)')
    L.append(f'- **Pure sinks** (consumed by nothing — candidate terminal outputs or dead ends): {len(sinks)}')
    L.append('  ' + (', '.join(sinks[:25]) + (' …' if len(sinks) > 25 else '')) if sinks else '  (none)')
    L.append(f'- **Isolated** (in the contracts but wired to nothing): {len(isolated)}')
    L.append('  ' + (', '.join(isolated[:25]) + (' …' if len(isolated) > 25 else '')) if isolated else '  (none)')
    L.append('')
    L.append('_Leads, not verdicts — pure sinks/sources are often correct by design (terminal Keys, '
             'primitive inputs); triage against the contract before acting._')

    (out / 'ripple_register.md').write_text('\n'.join(L), encoding='utf-8')

    # machine-hookable graph
    payload = {
        'schema_version': 1,
        'node_count': len(nodes), 'edge_count': len(edges),
        'edge_types': {t: by_type.get(t, 0) for t in EDGE_TYPES},
        'nodes': nodes,
        'edges': edges,
    }
    (out / 'data' / 'ripple_graph.json').write_text(
        json.dumps(payload, indent=1, sort_keys=True), encoding='utf-8')
    return out / 'ripple_register.md'


# ──────────────────────────── CLI ───────────────────────────────────────────

def _print_query(graph, node, direction, depth, layers):
    r = ripple(graph, node, direction=direction, depth=depth, layers=layers)
    if 'error' in r:
        print(r['error'])
        # offer near-matches
        nl = node.lower()
        near = [n for n in graph['nodes'] if nl in n.lower()][:10]
        if near:
            print('did you mean:', ', '.join(near))
        return 1
    print(f'# ripple({node!r}, direction={direction}, depth={depth}, '
          f'layers={sorted(layers) if layers else "all"})')
    if 'down' in r:
        print(f'\n## downstream — a change to {node!r} affects ({len(r["down"])}):')
        for h in r['down']:
            print('  ' + _fmt_hop(h))
    if 'up' in r:
        print(f'\n## upstream — {node!r} is built from ({len(r["up"])}):')
        for h in r['up']:
            print('  ' + _fmt_hop(h))
    return 0


def main():
    ap = argparse.ArgumentParser(description='Cross-scale ripple / propagation map (observatory L3).')
    ap.add_argument('--repo-root', default='.')
    ap.add_argument('--output-dir', default=None,
                    help='write ripple_register.md + data/ripple_graph.json here')
    ap.add_argument('--node', default=None, help='ad-hoc: query one node and print its chains')
    ap.add_argument('--direction', default='both', choices=('down', 'up', 'both'))
    ap.add_argument('--depth', type=int, default=None)
    ap.add_argument('--layers', default=None,
                    help='comma-separated edge-type slice, e.g. derives,produces,reads')
    ap.add_argument('--vector-run', default=None,
                    help='a vector_audit run dir to overlay quantized degrees from')
    args = ap.parse_args()

    graph = build_graph(args.repo_root)
    layers = tuple(s.strip() for s in args.layers.split(',')) if args.layers else None
    vector_hits = attach_vector_degrees(graph, args.vector_run) if args.vector_run else 0

    if args.node:
        return _print_query(graph, args.node, args.direction, args.depth, layers)
    if args.output_dir:
        p = write_register(graph, args.output_dir, vector_hits=vector_hits)
        print(f'[ripple] {len(graph["nodes"])} nodes, {len(graph["edges"])} edges -> {p}')
        return 0
    ap.error('give --node for an ad-hoc query, or --output-dir to write the register')


if __name__ == '__main__':
    sys.exit(main())
