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
