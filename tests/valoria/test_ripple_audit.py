"""Unit + integration tests for the cross-scale ripple methodology
(skills/valoria-vector-audit/scripts/ripple_audit.py).

Governance mirror of the sibling observatory layers: assert §8 reuse-by-identity
(it must COMPOSE structure_audit.build_l2 + formula_audit.build_contract_edges,
never re-derive them), plus traversal correctness (bidirectionality, cycle-safety,
depth + slice semantics) on the real working-tree graph.
"""
import importlib.util
import os

_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
_SCRIPTS = os.path.join(_ROOT, 'skills', 'valoria-vector-audit', 'scripts')


def _load(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(_SCRIPTS, name + '.py'))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


ra = _load('ripple_audit')


# ── §8 reuse-by-identity: it must import the real builders, not clone them ──

def test_reuses_sibling_builders_by_identity():
    import structure_audit as sa
    import formula_audit as fa
    assert ra.sa.build_l2 is sa.build_l2
    assert ra.fa.build_contract_edges is fa.build_contract_edges


# ── graph construction on the real working tree ─────────────────────────────

def test_build_graph_nonempty_and_typed():
    g = ra.build_graph(_ROOT)
    assert g['nodes'] and g['edges']
    kinds = {n['kind'] for n in g['nodes'].values()}
    assert kinds <= {'module', 'quantity'}
    assert 'module' in kinds  # module_contracts always yields modules
    types = {e['type'] for e in g['edges']}
    assert types <= set(ra.EDGE_TYPES)
    # every edge endpoint is a registered node (no dangling references)
    for e in g['edges']:
        assert e['src'] in g['nodes'] and e['dst'] in g['nodes']


# ── traversal correctness ───────────────────────────────────────────────────

def _node_with_precise_outedge(g):
    precise = set(ra.DEFAULT_LAYERS)
    for n in g['nodes']:
        if any(g['edges'][ei]['type'] in precise for ei in g['adj'].get(n, ())):
            return n
    raise AssertionError('no node with a precise out-edge')


def test_bidirectionality_is_consistent():
    """If B is reachable downstream of A over an allowed edge type, then A must be
    reachable upstream of B — the up/down views are the same graph, reversed."""
    g = ra.build_graph(_ROOT)
    src = _node_with_precise_outedge(g)
    down = ra.ripple(g, src, direction='down')
    assert down['down'], 'chosen node should have a precise downstream'
    for hop in down['down'][:20]:
        back = ra.ripple(g, hop['node'], direction='up')
        assert any(h['node'] == src for h in back['up']), (src, hop['node'])


# ── regression pins for the 2026-07-21 adversarial-review fixes ─────────────

def test_notional_flag_is_sticky_true():
    """A doc:null/[ASSUMPTION] module must KEEP its notional tag no matter how many
    load-bearing edges also touch it (critic finding #1: bare re-refs were clearing it)."""
    import structure_audit as sa
    from pathlib import Path
    _g, meta, _e, _f, _a = sa.build_l2(Path(_ROOT))
    meta_notional = {m for m, v in meta.items() if v.get('notional')}
    assert meta_notional, 'fixture expects at least one notional module in contracts'
    g = ra.build_graph(_ROOT)
    for m in meta_notional:
        n = g['nodes'].get(ra._nid('module', m))
        assert n and n['notional'] is True, f'{m} lost its notional tag'


def test_kind_namespacing_prevents_merge():
    """module and quantity ids live in disjoint namespaces (critic finding #2)."""
    g = ra.build_graph(_ROOT)
    for nid, n in g['nodes'].items():
        assert nid == ra._nid(n['kind'], n['name'])
    mods = {nid for nid in g['nodes'] if nid.startswith('module:')}
    qtys = {nid for nid in g['nodes'] if nid.startswith('quantity:')}
    assert mods and qtys and not (mods & qtys)


def test_coarse_bridges_excluded_from_default():
    """The coarse produces/reads bridges must NOT inflate the default ripple
    (critic finding #3: ~6x downstream over-report). Full-layer reach >= default,
    and strictly greater for at least one node that has bridge edges."""
    g = ra.build_graph(_ROOT)
    assert set(ra.DEFAULT_LAYERS) == {'emits_consumes', 'derives'}
    bigger = False
    for n in list(g['nodes'])[:200]:
        d_default = len(ra.ripple(g, n, direction='down')['down'])
        d_all = len(ra.ripple(g, n, direction='down', layers=ra.EDGE_TYPES)['down'])
        assert d_all >= d_default
        bigger = bigger or d_all > d_default
    assert bigger, 'expected the bridges to add reach somewhere (else the test is vacuous)'


def test_depth_limits_and_slice():
    g = ra.build_graph(_ROOT)
    src = next(n for n in g['nodes'] if g['adj'].get(n))
    d1 = ra.ripple(g, src, direction='down', depth=1)['down']
    dmax = ra.ripple(g, src, direction='down', depth=None)['down']
    assert all(h['depth'] == 1 for h in d1)                 # depth=1 → only first hop
    assert len(d1) <= len(dmax)                             # deeper reaches at least as far
    # a slice to a single edge type never reaches MORE than the unsliced traversal
    one = ra.ripple(g, src, direction='down', layers=('derives',))['down']
    assert len(one) <= len(dmax)


def test_unknown_node_is_graceful():
    g = ra.build_graph(_ROOT)
    r = ra.ripple(g, 'definitely-not-a-real-node-xyz', direction='both')
    assert 'error' in r and r['down'] == [] and r['up'] == []


def test_cycle_safety():
    """A hand-built 2-cycle must terminate and report each other node once."""
    g = {'nodes': {'A': {'kind': 'module'}, 'B': {'kind': 'module'}},
         'edges': [{'src': 'A', 'dst': 'B', 'type': 'emits_consumes', 'provenance': 'x', 'notional': False},
                   {'src': 'B', 'dst': 'A', 'type': 'emits_consumes', 'provenance': 'y', 'notional': False}],
         'adj': {'A': [0], 'B': [1]}, 'radj': {'B': [0], 'A': [1]}}
    r = ra.ripple(g, 'A', direction='down', depth=None)
    assert [h['node'] for h in r['down']] == ['B']         # B once, no infinite loop
