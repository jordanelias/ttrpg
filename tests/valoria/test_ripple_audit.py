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

def test_bidirectionality_is_consistent():
    """If B is reachable downstream of A over an allowed edge type, then A must be
    reachable upstream of B — the up/down views are the same graph, reversed."""
    g = ra.build_graph(_ROOT)
    # pick a node that actually has out-edges
    src = next(n for n in g['nodes'] if g['adj'].get(n))
    down = ra.ripple(g, src, direction='down')
    assert 'down' in down
    for hop in down['down'][:20]:
        back = ra.ripple(g, hop['node'], direction='up')
        assert any(h['node'] == src for h in back['up']), (src, hop['node'])


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
