"""Regression + unit tests for the Structural Observatory's architecture layers
(skills/valoria-vector-audit/scripts/structure_audit.py).

Per the observatory governance ("validate-or-label"): the graph algorithms are
unit-tested on tiny fixtures with known answers, and the L2 closure checks are
regression-pinned against defects independently caught by hand in the 2026-07-13
multi-agent audit (PR #131) — if the tool stops reproducing those, it has
regressed.
"""
import importlib.util
import os

import pytest

_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
_SCRIPT = os.path.join(_ROOT, 'skills', 'valoria-vector-audit', 'scripts', 'structure_audit.py')


def _load():
    spec = importlib.util.spec_from_file_location('structure_audit', _SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


sa = _load()


# ── graph-algorithm unit tests (known answers) ──────────────────────────────

def test_tarjan_finds_cycle_and_singletons():
    adj = {'a': ['b'], 'b': ['c'], 'c': ['a'], 'd': ['a'], 'e': []}
    comps = sa.tarjan_scc(adj)
    sizes = sorted(len(c) for c in comps)
    assert sizes == [1, 1, 3]  # {a,b,c} cycle + d + e
    cyc = [sorted(c) for c in comps if len(c) > 1]
    assert cyc == [['a', 'b', 'c']]


def test_tarjan_no_cycle():
    adj = {'a': ['b'], 'b': ['c'], 'c': []}
    assert all(len(c) == 1 for c in sa.tarjan_scc(adj))


# ── capstone reconciliation pins (ED-IN-0056) ───────────────────────────────

def test_cycles_includes_self_loops():
    # capstone #1/#2: a size-1 SCC WITH a self-edge is a real 1-node cycle. The old
    # `_cycles(scc)` filtered `len>1` and silently dropped self-loops, contradicting
    # tarjan_scc's own docstring; `_cycles` now takes the adjacency to detect them.
    adj = {'a': ['a'], 'b': ['c'], 'c': []}   # a self-loops; b->c acyclic
    assert sa._cycles(sa.tarjan_scc(adj), adj) == [['a']]


def test_cycles_multi_node_still_reported_and_dag_is_empty():
    cyc = {'x': ['y'], 'y': ['x'], 'z': []}
    assert sa._cycles(sa.tarjan_scc(cyc), cyc) == [['x', 'y']]
    dag = {'a': ['b'], 'b': ['c'], 'c': []}
    assert sa._cycles(sa.tarjan_scc(dag), dag) == []


def test_is_notional_is_the_one_provenance_predicate():
    # capstone #10: single-sourced here; doc:null OR no/literal-'None' resolver => notional.
    assert sa.is_notional(None, 'RealResolver') is True
    assert sa.is_notional('designs/x_v30.md', None) is True
    assert sa.is_notional('designs/x_v30.md', 'None') is True
    assert sa.is_notional('designs/x_v30.md', 'RealResolver') is False


def test_l2_contract_without_code_is_informational_name_gap():
    # capstone #7: returns contract names absent as a code-path segment. Informational
    # (drives the DISCLOSURE), never presented as a fabrication findings list.
    l2 = ['mass_battle', 'faction_state', 'victory']
    code = ['sim.provincial.mass_battle', 'engine.autoload.victory']   # faction_state absent
    assert sa.l2_contract_without_code(l2, code) == ['faction_state']


def test_articulation_point_on_path():
    # a - b - c : b is the cut vertex
    adj = {'a': ['b'], 'b': ['c'], 'c': []}
    assert sa.articulation_points(adj) == {'b'}


def test_articulation_none_on_triangle():
    adj = {'a': ['b', 'c'], 'b': ['c'], 'c': []}
    assert sa.articulation_points(adj) == set()


def test_as_list_handles_string_and_list():
    # the real module_contracts data hazard: `from:` is sometimes a bare string
    assert sa._as_list('engine_clock') == ['engine_clock']
    assert sa._as_list(['a', 'b']) == ['a', 'b']
    assert sa._as_list(None) == []
    assert sa._as_list([1, 'a', None]) == ['a']  # non-strings dropped


def test_module_name():
    assert sa._module_name('sim/provincial/faction_action.py') == 'sim.provincial.faction_action'
    assert sa._module_name('sim/personal/__init__.py') == 'sim.personal'


# ── L2 regression against PR #131 hand-caught defects ───────────────────────

@pytest.fixture(scope='module')
def l2():
    from pathlib import Path
    g, meta, edges, findings, assumption_count = sa.build_l2(Path(_ROOT))
    return {'g': g, 'meta': meta, 'edges': edges, 'findings': findings,
            'assumption_count': assumption_count}


def test_l2_reproduces_massbattle_fabricated_emit(l2):
    # PR #131 ED-MB-0010: mass_battle emits scene_outcome.battle_concluded with no
    # consumer (canon writes scene.battle_concluded). Must surface as a dangling emit.
    dangling = {(d['emitter'], d['type']) for d in l2['findings']['dangling_emit']}
    assert ('mass_battle', 'scene_outcome.battle_concluded') in dangling


def test_l2_reproduces_personal_combat_dead_emits(l2):
    # PR #131 §2.3 / module_adjudicator A4: scene.combat_felled / scene.combat_resolved
    # are declared personal_combat emits with zero wired consumers.
    dangling = {(d['emitter'], d['type']) for d in l2['findings']['dangling_emit']}
    assert ('personal_combat', 'scene.combat_felled') in dangling
    assert ('personal_combat', 'scene.combat_resolved') in dangling


def test_l2_flags_engine_clock_doc_null(l2):
    # engine_clock (the temporal spine) is doc:null per CLAUDE.md §6.
    assert 'engine_clock' in l2['findings']['doc_null']
    assert l2['meta']['engine_clock']['notional'] is True


def test_l2_has_wiring_edges_and_provenance(l2):
    assert len(l2['edges']) > 50            # real wiring present
    assert l2['assumption_count'] > 0        # provenance signal is live
    # every module carries a notional flag (provenance tag)
    assert all('notional' in m for m in l2['meta'].values())


# ── G_code relative-import resolution (Fable-5 finding M: build_g_code, the ──
#    AST import-graph builder, shipped untested; the batch-2 fix to package
#    __init__ / multi-dot relative resolution had no regression pin) ──────────

def _write_pkg(tmp_path, files):
    """files: {relpath: source} — write them under tmp_path and return a
    {module_name: relpath} map shaped exactly like build_g_code expects."""
    from pathlib import Path
    modules = {}
    for rel, src in files.items():
        p = tmp_path / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(src, encoding='utf-8')
        modules[sa._module_name(rel)] = rel
    return Path(tmp_path), modules


def test_g_code_relative_import_from_package_init_resolves_within_package(tmp_path):
    # The batch-2 defect: `from . import ip_track` inside sim/peninsular/__init__.py
    # must resolve to sim.peninsular.ip_track, NOT the nonexistent sim.ip_track. A
    # package __init__'s own module name IS its package, so it must not rsplit a
    # segment off before resolving `.`.
    root, modules = _write_pkg(tmp_path, {
        'pkg/__init__.py': 'from . import leaf\n',
        'pkg/leaf.py': 'X = 1\n',
    })
    g, errs = sa.build_g_code(root, modules)
    assert errs == []
    assert 'pkg.leaf' in g['pkg']              # resolved WITHIN the package
    # the one-package-too-high miss would resolve `from . import leaf` to a bare `leaf`
    # (no package prefix) instead of `pkg.leaf`; assert that mis-resolution is absent.
    assert 'leaf' not in g['pkg']              # never the unqualified (too-high) target
    assert g['pkg'] == {'pkg.leaf'}            # exactly the correct edge, nothing spurious


def test_g_code_relative_import_from_regular_module(tmp_path):
    # a regular module a.b.c: `from . import d` resolves against a.b (its package)
    root, modules = _write_pkg(tmp_path, {
        'a/__init__.py': '',
        'a/b.py': 'from . import c\n',
        'a/c.py': 'Y = 2\n',
    })
    g, errs = sa.build_g_code(root, modules)
    assert errs == []
    assert 'a.c' in g['a.b']


def test_g_code_multi_dot_relative_walks_up(tmp_path):
    # `from .. import top` inside a.sub.mod must climb two packages to a.top
    root, modules = _write_pkg(tmp_path, {
        'a/__init__.py': '',
        'a/top.py': 'Z = 3\n',
        'a/sub/__init__.py': '',
        'a/sub/mod.py': 'from .. import top\n',
    })
    g, errs = sa.build_g_code(root, modules)
    assert errs == []
    assert 'a.top' in g['a.sub.mod']


def test_g_code_captures_relative_import_cycle(tmp_path):
    # two modules importing each other relatively form a real SCC — the batch-2 fix
    # was motivated by such a cycle (systems.social_contest.sim.contest) being dropped when the
    # relative target mis-resolved. Determinism: _cycles is sorted, so the same
    # fixture yields the same list every run.
    root, modules = _write_pkg(tmp_path, {
        'p/__init__.py': '',
        'p/one.py': 'from . import two\n',
        'p/two.py': 'from . import one\n',
    })
    g, errs = sa.build_g_code(root, modules)
    assert errs == []
    cycles = sa._cycles(sa.tarjan_scc(g), g)
    assert ['p.one', 'p.two'] in cycles


def test_cycles_members_are_sorted_regardless_of_insertion_order():
    # The real determinism property _cycles provides: each cycle's MEMBERS come out
    # sorted, so the output does NOT depend on set/hash iteration order of the SCC.
    # Build two adjacencies describing the SAME 3-cycle in opposite insertion orders;
    # both must yield identically-sorted members. (Mutation guard: dropping the
    # `sorted(c)` in _cycles makes these two results differ.)
    fwd = {'a': ['b'], 'b': ['c'], 'c': ['a']}
    rev = {'c': ['a'], 'b': ['c'], 'a': ['b']}
    cf = sa._cycles(sa.tarjan_scc(fwd), fwd)
    cr = sa._cycles(sa.tarjan_scc(rev), rev)
    assert cf == [['a', 'b', 'c']]
    assert cf == cr
