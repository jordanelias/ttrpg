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
# The PRECISE edge types traversed by default. `produces`/`reads` are COARSE
# module-granularity cross-scale bridges: `reads` links every input a module
# consumes to the module and `produces` links the module to every output it
# computes, ignoring which input actually feeds which output — so including them
# by default smears a per-derivation dependency into a module-wide over-approximation
# (measured ~6× downstream over-report). They stay in the graph and are opt-in via
# an explicit `layers` slice for cross-scale queries, but never pollute the default
# "what does a change here affect" answer.
DEFAULT_LAYERS = ('emits_consumes', 'derives')
_BRIDGE_TYPES = ('produces', 'reads')
_BRIDGE_LAYER = 'ripple.bridge'


def _nid(kind, name):
    """Kind-qualified node id — modules and quantities never share an id, so a
    quantity named identically to a module can't silently merge onto it."""
    return f'{kind}:{name}'


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
    _UNSET = object()

    def _node(kind, name, notional=_UNSET, scales=None, doc=None):
        """Get-or-create a kind-qualified node. `notional` is STICKY-TRUE: it is only
        ever raised to True by an explicit True; a bare re-reference (notional unset)
        never clears it, so a doc:null / [ASSUMPTION] module keeps its tag no matter
        how many load-bearing edges also touch it."""
        nid = _nid(kind, name)
        n = nodes.get(nid)
        if n is None:
            n = nodes[nid] = {'kind': kind, 'name': name,
                              'notional': bool(notional) if notional is not _UNSET else False,
                              'scales': scales or [], 'doc': doc}
        else:
            if notional is not _UNSET and notional:
                n['notional'] = True
            if scales and not n['scales']:
                n['scales'] = scales
            if doc and not n.get('doc'):
                n['doc'] = doc
        return nid

    # ---- L2: module -> module (emits_consumes), provenance = Key type ----
    g_l2, meta, edges_meta, findings, _assump = sa.build_l2(root)
    for mod, m in meta.items():
        _node('module', mod, notional=m.get('notional', False),
              scales=m.get('scales') or [], doc=m.get('doc'))
    for e in edges_meta:
        src, dst, ktype = e.get('src'), e.get('dst'), e.get('type')
        if not src or not dst or src == dst:
            # self-consume (a module reading a Key it also emits) is a real contract
            # pattern but a NO-OP for cross-node ripple — it only inflates hub degree.
            continue
        sid, did = _node('module', src), _node('module', dst)
        notional = nodes[sid]['notional'] or nodes[did]['notional']
        edges.append({'src': sid, 'dst': did, 'type': 'emits_consumes',
                      'provenance': f'Key::{ktype}', 'notional': notional})

    # ---- L1: quantity -> quantity (derives) + module<->quantity bridges ----
    contracts = _load_contracts(root)
    fa_edges, _definitions = fa.build_contract_edges(contracts)
    for e in fa_edges:
        in_raw, out_raw = e.get('src'), e.get('dst')
        if not in_raw or not out_raw:
            continue
        mod = e.get('module')
        notional = bool(e.get('notional'))
        formula = e.get('formula')
        source = e.get('source')
        prov = f'formula::{formula}' if formula else (f'source::{source}' if source else 'derivation')
        in_id = _node('quantity', in_raw, notional=notional)
        out_id = _node('quantity', out_raw, notional=notional)
        if in_id != out_id:  # a quantity derived from itself is a no-op for ripple
            edges.append({'src': in_id, 'dst': out_id, 'type': 'derives',
                          'provenance': prov, 'notional': notional, 'module': mod})
        # COARSE cross-scale bridges (opt-in; excluded from DEFAULT_LAYERS — see note
        # on _BRIDGE_TYPES). module PRODUCES the output; module READS the input.
        if mod:
            mid = _node('module', mod)
            edges.append({'src': mid, 'dst': out_id, 'type': 'produces',
                          'provenance': f'{_BRIDGE_LAYER}::{mod} derivation', 'notional': notional})
            edges.append({'src': in_id, 'dst': mid, 'type': 'reads',
                          'provenance': f'{_BRIDGE_LAYER}::{mod} derivation', 'notional': notional})

    adj = defaultdict(list)
    radj = defaultdict(list)
    for i, e in enumerate(edges):
        adj[e['src']].append(i)
        radj[e['dst']].append(i)

    return {'nodes': nodes, 'edges': edges, 'adj': dict(adj), 'radj': dict(radj),
            'l2_findings': findings}


# ──────────────────────────── RIPPLE TRAVERSAL ──────────────────────────────

def resolve_node(graph, ref):
    """Accept a kind-qualified id (`module:faction_state`) OR a bare name
    (`faction_state`); return the canonical node id, preferring a module on a
    bare-name tie. None if unknown."""
    if ref in graph['nodes']:
        return ref
    for kind in ('module', 'quantity'):
        nid = _nid(kind, ref)
        if nid in graph['nodes']:
            return nid
    return None


def ripple(graph, start, direction='both', depth=None, layers=None):
    """Bidirectional depth-limited reachability from `start` (a node id or bare name).

    direction: 'down' (forward src->dst = what a change affects),
               'up'   (backward dst->src = provenance / dependencies),
               'both'.
    depth:     hop limit (None = unbounded, cycle-safe).
    layers:    iterable of edge types to traverse. None = DEFAULT_LAYERS (the PRECISE
               emits_consumes+derives; the coarse produces/reads bridges are opt-in) —
               this is the SLICE. Pass EDGE_TYPES explicitly for the full cross-scale view.

    Returns {'node','kind','down':[hop,...],'up':[hop,...]} where each hop is
      {'node','name','kind','via_edge':{type,provenance,notional},'from','depth'}.
    Order is BFS (nearest first); each node reported once per direction (shortest hop).
    """
    start = resolve_node(graph, start)
    if start is None:
        return {'error': 'unknown node', 'down': [], 'up': []}
    allow = set(layers) if layers else set(DEFAULT_LAYERS)
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
                nn = graph['nodes'].get(nxt, {})
                out.append({'node': nxt, 'name': nn.get('name', nxt), 'kind': nn.get('kind'),
                            'via_edge': {'type': e['type'], 'provenance': e['provenance'],
                                         'notional': e['notional']},
                            'from': cur, 'from_name': graph['nodes'].get(cur, {}).get('name', cur),
                            'depth': d + 1})
                q.append((nxt, d + 1))
        return out

    res = {'node': start, 'kind': graph['nodes'][start]['kind']}
    if direction in ('down', 'both'):
        res['down'] = walk(graph['adj'], 'dst')
    if direction in ('up', 'both'):
        res['up'] = walk(graph['radj'], 'src')
    return res


# ─────────────── FULL-TOKEN IMPACT QUERY (vector G_cite + metadata) ──────────
# "Tug anything, see what moves." Unifies the vector audit's QUANTIZED full-token graph
# (all 276 tokens: mechanics, Keys, primitives, actions, places, …) with ripple's directional
# reachability, so a change to A can be traced to distant/surprising j,q — not just neighbours.

def load_vector_graph(run_dir):
    """Build a ripple-style graph from a vector_audit run's exported data/*.json:
    nodes = every token (kind = its scale), edges = the citation graph (`cites`) + the three
    metadata layers (`throughline`/`mu`/`pp`). Node ids are the bare token names."""
    data = os.path.join(run_dir, 'data')
    with open(os.path.join(data, 'g_cite.json'), encoding='utf-8') as fh:
        g_cite = json.load(fh)
    try:
        with open(os.path.join(data, 'g_metadata.json'), encoding='utf-8') as fh:
            g_meta = json.load(fh)
    except OSError:
        g_meta = {}
    try:
        with open(os.path.join(data, 'tokens.json'), encoding='utf-8') as fh:
            toks = json.load(fh).get('tokens', {})
    except OSError:
        toks = {}
    nodes = {}

    def _n(name):
        if name not in nodes:
            nodes[name] = {'kind': (toks.get(name) or {}).get('scale', '?'), 'name': name}
        return name

    edges = []
    for a, nbrs in g_cite.items():
        for b, w in (nbrs or {}).items():
            edges.append({'src': _n(a), 'dst': _n(b), 'type': 'cites',
                          'provenance': f'cite×{w}', 'notional': False, 'weight': w})
    for layer in ('throughline', 'mu', 'pp'):
        for a, nbrs in (g_meta.get(layer) or {}).items():
            for b, w in (nbrs or {}).items():
                edges.append({'src': _n(a), 'dst': _n(b), 'type': layer,
                              'provenance': f'{layer}×{w}', 'notional': False})
    adj, radj = defaultdict(list), defaultdict(list)
    for i, e in enumerate(edges):
        adj[e['src']].append(i)
        radj[e['dst']].append(i)
    return {'nodes': nodes, 'edges': edges, 'adj': dict(adj), 'radj': dict(radj)}


def impact_query(graph, start, depth=6, top=40):
    """UNDIRECTED transitive reachability from `start` over the full token graph — "what
    moves if I tug this". Returns every reachable token with its shortest graph distance,
    the path, and a SURPRISE flag: reachable but in a DIFFERENT scale/subsystem AND ≥3 hops
    away (a far, cross-subsystem link no one would predict), or reached only through a single
    non-obvious intermediary."""
    start = resolve_node(graph, start)
    if start is None:
        return {'error': 'unknown token'}
    edges = graph['edges']
    seen = {start: (0, None, None)}  # node -> (dist, parent, via_edge_type)
    q = deque([start])
    while q:
        cur = q.popleft()
        d = seen[cur][0]
        if d >= depth:
            continue
        # undirected: both out-edges and in-edges
        for ei in graph['adj'].get(cur, ()):
            nxt = edges[ei]['dst']
            if nxt not in seen:
                seen[nxt] = (d + 1, cur, edges[ei]['type'])
                q.append(nxt)
        for ei in graph['radj'].get(cur, ()):
            nxt = edges[ei]['src']
            if nxt not in seen:
                seen[nxt] = (d + 1, cur, edges[ei]['type'])
                q.append(nxt)

    def _path(n):
        out = []
        while n is not None:
            out.append(n)
            n = seen[n][1]
        return list(reversed(out))

    src_scale = graph['nodes'][start]['kind']
    reached = []
    for n, (dist, _parent, via) in seen.items():
        if n == start:
            continue
        scale = graph['nodes'][n]['kind']
        cross = scale != src_scale
        reached.append({'node': n, 'scale': scale, 'dist': dist, 'via': via,
                        'cross_scale': cross, 'surprising': cross and dist >= 3,
                        'path': _path(n)})
    reached.sort(key=lambda r: (not r['surprising'], -r['dist'], r['node']))
    surprising = [r for r in reached if r['surprising']]
    return {'start': start, 'scale': src_scale, 'reached_total': len(reached),
            'surprising_total': len(surprising), 'surprising': surprising[:top],
            'nearest': sorted(reached, key=lambda r: (r['dist'], r['node']))[:12]}


# ──────────────────────────── QUANTIZED OVERLAY ─────────────────────────────

def attach_vector_degrees(graph, vector_run_dir):
    """Annotate name-matching nodes with a vector_audit run's quantized coordinates
    (cite/tl/mu/pp degrees), so the qualitative node carries its quantized measure.
    Matches on the node's display NAME (ids are kind-qualified), exact then normalized.
    Returns hit count; -1 if the file is present but the wrong shape (caller can warn)."""
    path = os.path.join(vector_run_dir, 'data', 'degrees.json')
    if not os.path.isfile(path):
        return 0
    with open(path, encoding='utf-8', errors='replace') as fh:
        degs = json.load(fh)
    if not isinstance(degs, dict):          # a list / scalar degrees.json is unusable
        return -1

    def norm(s):
        return re.sub(r'[^a-z0-9]+', '', str(s).lower())
    # Axis aliases: vector_audit's degrees.json writes the throughline axis as
    # `throughline` (not `tl`) and adds a `tfidf` axis — the axis-major detector must
    # accept those or the overlay is dead on arrival against the sibling it consumes.
    _AXIS = {'cite': 'cite', 'tl': 'tl', 'throughline': 'tl', 'mu': 'mu', 'pp': 'pp'}
    # shape A (axis-major): {'cite': {token: n}, 'throughline': ...} — recognized axis
    # keys map to dicts.  shape B (token-major): {token: {cite,tl,mu,pp}}.
    coords = defaultdict(dict)
    axis_keys = [k for k in degs if k in _AXIS and isinstance(degs[k], dict)]
    if axis_keys:
        for axis in axis_keys:                       # unrecognized axes (e.g. tfidf) ignored
            for tok, v in (degs[axis] or {}).items():
                coords[tok][_AXIS[axis]] = v
    else:
        for tok, m in degs.items():
            if isinstance(m, dict):
                got = {_AXIS[k]: m.get(k) for k in m if k in _AXIS}
                if got:
                    coords[tok] = got
    if not coords:                          # parsed but no recognizable axis data
        return -1
    by_norm = {norm(tok): c for tok, c in coords.items()}
    hits = 0
    for n in graph['nodes'].values():
        name = n.get('name', '')
        c = coords.get(name) or by_norm.get(norm(name))
        if c:
            n['quantized'] = c
            hits += 1
    return hits


# ──────────────────────────── REPORTING ─────────────────────────────────────

def _degree(graph, allow=DEFAULT_LAYERS):
    """In/out degree counting only `allow` edge types — defaults to the PRECISE layers
    so hub ranking + orphan/sink analysis are not inflated by the coarse bridges."""
    allow = set(allow)
    out = {n: 0 for n in graph['nodes']}
    inn = {n: 0 for n in graph['nodes']}
    for e in graph['edges']:
        if e['type'] not in allow:
            continue
        out[e['src']] = out.get(e['src'], 0) + 1
        inn[e['dst']] = inn.get(e['dst'], 0) + 1
    return inn, out


def _fmt_hop(h):
    tag = ' ⚠notional' if h['via_edge']['notional'] else ''
    return (f"{h.get('from_name', h['from'])} --{h['via_edge']['type']}"
            f"[{h['via_edge']['provenance']}]--> {h['name']} ({h['kind']}){tag}")


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
    nm = lambda nid: nodes[nid].get('name', nid)  # noqa: E731
    hubs = sorted(nodes, key=lambda n: (-total_deg[n], n))[:12]  # explicit tiebreak (deterministic)
    orphans = sorted((nm(n) for n in nodes if inn.get(n, 0) == 0 and outd.get(n, 0) > 0))  # pure sources
    sinks = sorted((nm(n) for n in nodes if outd.get(n, 0) == 0 and inn.get(n, 0) > 0))     # pure sinks
    isolated = sorted((nm(n) for n in nodes if inn.get(n, 0) == 0 and outd.get(n, 0) == 0))

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
    L.append('**Edge types:** ' + ', '.join(f'{t}={by_type.get(t, 0)}' for t in EDGE_TYPES)
             + '  (`produces`/`reads` are COARSE module-granularity bridges — opt-in, '
               'excluded from the default precise ripple).')
    if vector_hits > 0:
        L.append(f'**Quantized overlay:** {vector_hits} node(s) annotated with vector-audit degrees.')
    elif vector_hits < 0:
        L.append('**Quantized overlay:** a degrees.json was found but had no usable cite/tl/mu/pp data.')
    L.append('')
    L.append('## What / How / Why')
    L.append('- **WHAT** a node is: its `kind` (module = mechanic/subsystem; quantity = value/derived stat/Key output).')
    L.append('- **HOW** two nodes couple: the edge `type` — `emits_consumes` (a Key flows module→module), '
             '`derives` (a value is computed from another), `produces`/`reads` (a module writes/consumes a value).')
    L.append('- **WHY** the coupling exists: the edge `provenance` — the Key type, formula, or contract source '
             'that established it (never synthesized; read from module_contracts / descriptor_registry).')
    L.append('')
    L.append('## Highest change-impact nodes (by precise degree — a change here ripples furthest)')
    for h in hubs:
        q = nodes[h].get('quantized')
        qs = f'  ·  quantized={q}' if q else ''
        L.append(f'- **{nm(h)}** ({nodes[h]["kind"]}) — downstream {outd[h]} · upstream {inn[h]}{qs}')
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

def _print_impact(vg, token, depth):
    r = impact_query(vg, token, depth=depth)
    if 'error' in r:
        print(f'unknown token: {token!r}')
        nl = token.lower()
        near = sorted(n for n in vg['nodes'] if nl in n.lower())[:10]
        if near:
            print('did you mean:', ', '.join(near))
        return 1
    print(f"# impact({token!r}) over the full token graph — scale={r['scale']}; reached "
          f"{r['reached_total']} tokens, {r['surprising_total']} SURPRISING (≥3 hops + cross-subsystem)")
    print("\n## nearest — immediate blast radius:")
    for h in r['nearest']:
        print(f"  d{h['dist']}  {h['node']} ({h['scale']})  via {h['via']}")
    print(f"\n## SURPRISING — tug {token!r} and these move via a far, non-obvious path:")
    for h in r['surprising']:
        print(f"  d{h['dist']}  {h['node']} ({h['scale']})   {'  →  '.join(h['path'])}")
    if not r['surprising']:
        print("  (none — nothing distant-and-cross-subsystem within depth)")
    return 0


def _print_query(graph, node, direction, depth, layers):
    r = ripple(graph, node, direction=direction, depth=depth, layers=layers)
    if 'error' in r:
        print(f'unknown node: {node!r}')
        nl = node.lower()
        near = sorted({n.get('name', '') for n in graph['nodes'].values()
                       if nl in n.get('name', '').lower()})[:10]
        if near:
            print('did you mean:', ', '.join(near))
        return 1
    print(f'# ripple({node!r}, direction={direction}, depth={depth}, '
          f'layers={sorted(layers) if layers else list(DEFAULT_LAYERS)})')
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
                    help="comma-separated edge-type slice (default: the precise "
                         "emits_consumes,derives). Use 'all' or add produces,reads for the "
                         "coarse cross-scale bridges.")
    ap.add_argument('--vector-run', default=None,
                    help='a vector_audit run dir: overlays quantized degrees, and is the graph '
                         'source for --impact')
    ap.add_argument('--impact', default=None,
                    help='full-token change-impact query: given a token, rank every reachable '
                         'token by graph distance over the vector G_cite+metadata graph and flag '
                         'the far/cross-subsystem "surprising" ones. Requires --vector-run.')
    args = ap.parse_args()

    # --impact operates on the vector run's exported full-token graph, not the contract graph.
    if args.impact:
        if not args.vector_run:
            ap.error('--impact requires --vector-run <a vector_audit run dir> (its exported g_cite)')
        return _print_impact(load_vector_graph(args.vector_run), args.impact, args.depth or 6)

    contracts = os.path.join(args.repo_root, 'references', 'module_contracts.yaml')
    if not os.path.isfile(contracts):
        ap.error(f'not a repo root (missing {contracts}) — pass --repo-root at the checkout root')

    graph = build_graph(args.repo_root)
    if args.layers and args.layers.strip() == 'all':
        layers = EDGE_TYPES
    elif args.layers:
        layers = tuple(s.strip() for s in args.layers.split(','))
    else:
        layers = None
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
