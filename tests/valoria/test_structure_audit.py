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


from . import _structure_audit  # the single owner of the loader


def _load():
    return _structure_audit.load()


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


# ── OI-54 (ED-IN-0097, 2026-07-29-code-shape-open-items plan §3 Wave 4 item 4): the
# JOIN-VERIFIED contract↔code correspondence check, superseding l2_contract_without_code()
# as run()'s primary correspondence signal. Falsifier per the wave's own item 4: a fictional
# contract entry with a bogus sim_module: must be reported unresolvable — a fixture, not a
# claim about the live corpus (which could drift). The live corpus is separately re-checked
# by test_module_contracts_sim_module_join_is_exact below (§0.1 #2: assert it asserted).

def _l2_meta(entries):
    """{name: {'sim_module': v}} — the minimal build_l2()-shaped meta dict l2_contract_code_join
    actually reads (it only touches the 'sim_module' key)."""
    return {name: {'sim_module': sm} for name, sm in entries.items()}


def test_join_reports_bogus_sim_module_as_unresolvable():
    # THE falsifier: a fictional contract entry naming a file that does not exist anywhere in
    # G_code must land in 'unresolvable', never silently pass as 'joined'.
    meta = _l2_meta({
        'faction_state': 'engine/autoload/game_state.py',   # real file
        'totally_fictional_module': 'systems/nowhere/does_not_exist.py',   # bogus
    })
    modules = {'engine.autoload.game_state': 'engine/autoload/game_state.py',
               'systems.factions.sim.faction_action': 'systems/factions/sim/faction_action.py'}
    join = sa.l2_contract_code_join(meta, modules)
    assert join['unresolvable'] == ['totally_fictional_module']
    assert join['joined'] == ['faction_state']


def test_join_resolves_directory_prefix_and_exact_file():
    meta = _l2_meta({
        'personal_combat': 'systems/combat/combat_engine_v1/',   # directory, trailing slash
        'victory': 'engine/autoload/victory.py',                 # exact file
        'mass_battle': None,                                     # undeclared (no field at all)
        'ci_political': 'none',                                  # explicit disclosed absence
    })
    modules = {
        'systems.combat.combat_engine_v1.wrapper': 'systems/combat/combat_engine_v1/wrapper.py',
        'engine.autoload.victory': 'engine/autoload/victory.py',
    }
    join = sa.l2_contract_code_join(meta, modules)
    assert join['joined'] == ['personal_combat', 'victory']
    assert join['none'] == ['ci_political']
    assert join['undeclared'] == ['mass_battle']
    assert join['unresolvable'] == []


def test_join_directory_without_trailing_slash_still_resolves():
    # a directory path given without the trailing slash (easy to typo in hand-authored YAML)
    # must not be misread as a bogus exact-file match.
    meta = _l2_meta({'social_contest': 'systems/social_contest/sim/contest'})
    modules = {'systems.social_contest.sim.contest.wrapper':
               'systems/social_contest/sim/contest/wrapper.py'}
    join = sa.l2_contract_code_join(meta, modules)
    assert join['joined'] == ['social_contest']


def test_join_accounts_for_every_module_exactly_once():
    # §0.1 #2: the loop asserts it asserted — every module lands in exactly one bucket, no
    # module silently disappears or double-counts.
    meta = _l2_meta({'a': 'x/y.py', 'b': 'none', 'c': None, 'd': 'nowhere/bogus.py'})
    modules = {'x.y': 'x/y.py'}
    join = sa.l2_contract_code_join(meta, modules)
    all_named = join['joined'] + join['none'] + join['unresolvable'] + join['undeclared']
    assert sorted(all_named) == ['a', 'b', 'c', 'd']
    checked = sum(len(v) for v in join.values())
    assert checked == 4, 'every fixture module must be accounted for exactly once'


def test_module_contracts_sim_module_join_is_exact():
    """Live-corpus check (companion to the bogus-fixture falsifier above): every one of the
    27 references/module_contracts.yaml modules is accounted for in exactly one join bucket,
    and — the one currently-known, DELIBERATE exception (mass_battle, MB-owned rows per the
    2026-07-29-code-shape-open-items plan's shared-file single-writer table) aside — the
    unresolvable bucket is empty. A regression here (a NEW unresolvable or undeclared module)
    is a real defect, not a fixture artifact."""
    root = sa.Path(_ROOT)
    modules = sa.collect_py_modules(root)
    g_l2, meta, edges_meta, findings, assumption_count = sa.build_l2(root)
    join = sa.l2_contract_code_join(meta, modules)
    checked = len(join['joined']) + len(join['none']) + len(join['unresolvable']) + len(join['undeclared'])
    assert checked == len(meta) == 27, f'expected all 27 module_contracts.yaml rows accounted, got {checked}'
    assert join['unresolvable'] == [], f"unresolvable (fictional/stale sim_module:) rows: {join['unresolvable']}"
    # SUBSET, not equality, and deliberately so. `mass_battle` is undeclared because the row is
    # MB-lane-owned and this (IN-owned) wave may not edit it — but module_contracts.yaml:552
    # explicitly invites the MB session to add its `sim_module:`, and mechanics_index already
    # carries the path. An `== ['mass_battle']` pin would go RED the moment MB lands its own row,
    # forcing MB to edit an IN-owned test file to ship in-lane work — a foreseeable cross-lane
    # break, which is the failure this phrasing exists to avoid. What must hold is the invariant:
    # nothing OUTSIDE the known MB exception may be undeclared.
    assert set(join['undeclared']) <= {'mass_battle'}, (
        f"only the MB-owned mass_battle row may be undeclared, got: {join['undeclared']}")


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
    assert sa._module_name('systems/factions/sim/faction_action.py') == 'systems.factions.sim.faction_action'
    assert sa._module_name('sim/personal/__init__.py') == 'sim.personal'


# ── L2 regression against PR #131 hand-caught defects ───────────────────────

@pytest.fixture(scope='module')
def l2():
    from pathlib import Path
    g, meta, edges, findings, assumption_count = sa.build_l2(Path(_ROOT))
    return {'g': g, 'meta': meta, 'edges': edges, 'findings': findings,
            'assumption_count': assumption_count}


def test_l2_massbattle_fabricated_emit_stays_deleted(l2):
    # ED-MB-0010 RESOLVED 2026-07-29 (plan-v2 E1): scene_outcome.battle_concluded was the
    # FAMILY name of scene.battle_concluded fabricated into mass_battle.emits, deleted at
    # the source. This test used the defect as its known answer; it is now the recurrence
    # guard — if the family-name emit ever reappears, it surfaces as a dangling emit again
    # and this fails. (Mutation-verified: re-adding the module_contracts row flips this red.)
    dangling = {(d['emitter'], d['type']) for d in l2['findings']['dangling_emit']}
    assert ('mass_battle', 'scene_outcome.battle_concluded') not in dangling
    # Setup guard (G6 — the absence above must be observable): mass_battle itself must still
    # be parsed into the graph, or the 'not in' passes vacuously because the whole module
    # vanished (e.g. a YAML fat-finger in the deleting edit).
    assert 'mass_battle' in l2['meta']


def test_l2_personal_combat_dead_emits_now_consumed(l2):
    # PR #131 §2.3 / module_adjudicator A4: scene.combat_felled / scene.combat_resolved
    # were declared personal_combat emits with zero wired consumers.
    # CLOSED 2026-07-29 (W3 item 5, OI-22a/OI-24): npc_behavior + faction_state consumes:[]
    # now declare both types (module_contracts.yaml, per the registry's pre-existing
    # consuming_systems: [npc_behavior, faction_layer, articulation] declaration for both
    # types) — declared intent, runtime gated on those modules being built. No longer dangling.
    dangling = {(d['emitter'], d['type']) for d in l2['findings']['dangling_emit']}
    assert ('personal_combat', 'scene.combat_felled') not in dangling
    assert ('personal_combat', 'scene.combat_resolved') not in dangling


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


# ── code-root liveness guard (ED-MB-0044) ───────────────────────────────────
#
# THE PATTERN THIS GUARDS (CLAUDE.md §0.1 #5): a tool hardcodes a path root; the tree moves
# underneath it; the tool then scans NOTHING and reports that emptiness as a clean result.
# `CODE_ROOTS` read ('sim', 'tools') for five days after `sim/` was deleted on 2026-07-21
# (ED-IN-0071 P4 continuation). G_code covered 88 `tools/` modules and zero simulation code;
# every G_code finding — cycles, cut-vertices, orphans — was scoped to a corpus that excluded
# the entire engine, and the register's own prose described 88 as "real code modules".
#
# A missing root is unobservable from the outputs (an empty scan and a healthy scan both
# produce no findings), so it must be asserted on the CONFIGURATION, not the result.

def test_code_roots_all_exist():
    """Every configured code root must exist on disk. A missing root means G_code is silently
    under-scanning — the failure mode is an absent finding, which no output assertion can see."""
    missing = sa.missing_code_roots(_ROOT)
    assert missing == [], (
        f"configured code root(s) do not exist: {missing}. G_code is scanning a deleted tree and "
        "will report emptiness as health. Update CODE_ROOTS/EXTRA_CODE_ROOTS to the live homes."
    )


def test_g_code_covers_simulation_code_not_just_tools():
    """The observable half of the same guard: the import graph must actually contain simulation
    modules. This is what a reader of the register believes when it says 'real code modules'."""
    mods = sa.collect_py_modules(sa.Path(_ROOT))
    prefixes = {m.split('.')[0] for m in mods}
    assert 'tools' in prefixes
    assert 'systems' in prefixes, "no systems/*/sim modules in G_code — per-subsystem sims invisible"
    assert 'engine' in prefixes, "no engine/ modules in G_code — the engine core is invisible"
    # The live mass-battle engine sits under tests/ and is reachable only via EXTRA_CODE_ROOTS.
    assert any(m.startswith('tests.sim.mass_battle') for m in mods), (
        "the live mass-battle engine (tests/sim/mass_battle/, ~10.5k LOC) is not in G_code"
    )


def test_sys_path_alias_resolves_live_mass_battle_internal_edges():
    """`tests/sim/mass_battle/` puts `tests/sim` on sys.path and imports itself as top-level
    `mass_battle.*`. Without sys_path_aliases every internal edge fails to resolve and the
    package lands in G_code as 28 EDGELESS nodes — reported as orphans. Visible-but-edgeless is
    strictly worse than unscanned: it reads as a measured emptiness. (Mutation guard: dropping
    the `aliases` argument from _resolve_internal drives this count to 0.)"""
    root = sa.Path(_ROOT)
    mods = sa.collect_py_modules(root)
    aliases = sa.sys_path_aliases(mods)
    assert aliases.get('mass_battle.engine') == 'tests.sim.mass_battle.engine'
    g, _ = sa.build_g_code(root, mods)
    internal = sum(
        1 for m in g if m.startswith('tests.sim.mass_battle')
        for t in g[m] if t.startswith('tests.sim.mass_battle')
    )
    assert internal >= 20, f"live mass-battle engine resolved only {internal} internal edges"


# ── CLI entry-point detection (OI-55 open half, ED-IN-0092) ─────────────────
#
# code_orphans previously excluded only `.__main__` suffixes and leading-`_` private
# names, so a real CLI tool with zero internal importers (any `tools/ci_*.py` invoked
# only from a workflow YAML or a git hook) read as an orphan. Detection is a single
# AST predicate plus a single split function (`split_orphans_and_cli_entries`) — both
# known-answer-tested here over a synthetic tree, per §0.1's "conditional assertions
# assert they asserted" discipline: each of (a)-(d) below is a positive, direct
# assertion, not a loop that could silently match zero rows.
#
# The AST predicate itself moved to `tools/ci_common.has_main_guard` (OI-52a/OI-54,
# ED-IN-0097, 2026-07-29-code-shape-open-items plan §3 Wave 4) — single-owner, adopted
# here via the sys.path idiom (module-level `sa.ci_common`, same pattern as
# tools/build_apparatus_registry.py and tests/valoria/test_retired_tree_apparatus.py).
# `tests/valoria/test_ci_common.py` carries the exhaustive known-answer suite
# (conventional/reversed/comment-false-positive/string-false-positive/non-dunder); this
# test now asserts ONLY that structure_audit genuinely delegates to that one owner
# (mutation check: perturb ci_common.has_main_guard and BOTH this test and
# test_ci_common.py's fail — no second, silently-divergent copy).

def test_has_main_guard_detects_conventional_and_reversed_forms():
    import ast
    # IDENTITY + absence-of-copy, not `is not None`: a module-level function is never None, so the
    # old assertion was vacuous (§0.1 #2 — an assertion must be able to observe the failure it
    # excludes) and would have passed even if structure_audit re-copied a local predicate
    # alongside the import. NB structure_audit imports plain `ci_common` via the sys.path idiom
    # (structure_audit.py:51-57), NOT `tools.ci_common` — importing the latter here would build a
    # SECOND module object and fail this assertion spuriously.
    import ci_common as ci_common_owner
    assert sa.ci_common.has_main_guard is ci_common_owner.has_main_guard
    # ...and structure_audit carries no module-level copy of its own — the failure "imported the
    # owner AND kept a local predicate" is what makes the identity check above insufficient alone.
    assert not hasattr(sa, 'has_main_guard'), 'structure_audit re-copied the predicate locally'
    guarded = ast.parse("if __name__ == '__main__':\n    pass\n")
    assert sa.ci_common.has_main_guard(guarded) is True
    reversed_guarded = ast.parse("if '__main__' == __name__:\n    pass\n")
    assert sa.ci_common.has_main_guard(reversed_guarded) is True
    unguarded = ast.parse("X = 1\nif X == 2:\n    pass\n")
    assert sa.ci_common.has_main_guard(unguarded) is False
    empty = ast.parse("")
    assert sa.ci_common.has_main_guard(empty) is False


def test_collect_cli_entry_modules_over_synthetic_tree(tmp_path):
    # (a)/(c)/(d) fixture: a plain orphan, a real CLI entry (guard + zero importers),
    # and a guarded-but-imported module — built as one synthetic tree so the split
    # logic is exercised the same way run() exercises it.
    root, modules = _write_pkg(tmp_path, {
        'pkg/__init__.py': '',
        # (a) a fake orphan: no importers, no guard.
        'pkg/dead_mod.py': 'X = 1\n',
        # (b) a fake import cycle: two modules import each other.
        'pkg/cyc_a.py': 'import pkg.cyc_b\n',
        'pkg/cyc_b.py': 'import pkg.cyc_a\n',
        # (c) a real CLI entry: __main__ guard, zero importers.
        'pkg/cli_tool.py': "def main():\n    pass\n\nif __name__ == '__main__':\n    main()\n",
        # (d) a __main__-guarded module that IS imported elsewhere — never an orphan
        # candidate at all, so it must land in neither list.
        'pkg/cli_used.py': "if __name__ == '__main__':\n    pass\n",
        'pkg/user_of_cli_used.py': 'import pkg.cli_used\n',
    })
    g, errs = sa.build_g_code(root, modules)
    assert errs == []
    code_nodes = list(modules)
    deg = sa.degrees(g, code_nodes)
    main_guard_modules = sa.collect_cli_entry_modules(root, modules)
    code_orphans, cli_entries = sa.split_orphans_and_cli_entries(code_nodes, deg, main_guard_modules)

    # (a) the fake orphan MUST be reported.
    assert 'pkg.dead_mod' in code_orphans

    # (b) the fake import cycle MUST be reported.
    cycles = sa._cycles(sa.tarjan_scc(g), g)
    assert ['pkg.cyc_a', 'pkg.cyc_b'] in cycles

    # (c) the guarded, zero-importer module MUST appear in cli_entries and MUST NOT
    # appear in code_orphans.
    assert 'pkg.cli_tool' in cli_entries
    assert 'pkg.cli_tool' not in code_orphans

    # (d) the guarded-but-imported module was never an orphan candidate (it has an
    # importer), so it must appear in NEITHER list — asserted both ways, not inferred.
    assert 'pkg.cli_used' not in cli_entries
    assert 'pkg.cli_used' not in code_orphans
    # and its importer is unaffected — sanity check the fixture wiring itself.
    assert 'pkg.cli_used' in g['pkg.user_of_cli_used']


def test_split_orphans_and_cli_entries_pure_logic():
    # Direct unit test of the split predicate against synthetic degree data, isolated
    # from AST parsing — covers the same (a)/(c)/(d) shape with hand-built degrees so
    # the split logic itself (not the guard-detection) is pinned independently.
    code_nodes = ['orphan', 'cli_entry', 'guarded_but_imported', 'imported_normal', 'private_mod._helper']
    code_deg = {
        'orphan': {'in': 0, 'out': 0},
        'cli_entry': {'in': 0, 'out': 0},
        'guarded_but_imported': {'in': 1, 'out': 0},
        'imported_normal': {'in': 1, 'out': 0},
        'private_mod._helper': {'in': 0, 'out': 0},
    }
    main_guard_modules = {'cli_entry', 'guarded_but_imported'}
    code_orphans, cli_entries = sa.split_orphans_and_cli_entries(code_nodes, code_deg, main_guard_modules)

    assert 'orphan' in code_orphans
    assert 'cli_entry' in cli_entries
    assert 'cli_entry' not in code_orphans
    assert 'guarded_but_imported' not in cli_entries
    assert 'guarded_but_imported' not in code_orphans
    # private-name exclusion (pre-existing rule) is preserved through the split.
    assert 'private_mod._helper' not in code_orphans
    assert 'private_mod._helper' not in cli_entries


def test_run_surfaces_cli_entries_field_in_metrics_json(tmp_path):
    # Both lists must be VISIBLE in the report output, never silent (task requirement).
    # Run the real audit against the live repo and check the JSON shape directly —
    # asserting on the artifact the register/JSON actually ships, not a reimplementation.
    from pathlib import Path
    findings = sa.run(Path(_ROOT), tmp_path)
    assert findings is not None  # run() returned (didn't raise); sanity on the call itself
    import json
    metrics = json.loads((tmp_path / 'data' / 'structure_metrics.json').read_text(encoding='utf-8'))
    assert 'cli_entries' in metrics['code']
    assert isinstance(metrics['code']['cli_entries'], list)
    assert len(metrics['code']['cli_entries']) > 0, (
        "expected at least one real CLI entry point in the live tree (e.g. tools/ci_*.py) — "
        "an empty list here would mean detection silently found nothing"
    )
    # no overlap between the two lists in the live tree.
    assert not (set(metrics['code']['orphans']) & set(metrics['code']['cli_entries']))
    register_text = (tmp_path / 'structure_register.md').read_text(encoding='utf-8')
    assert 'CLI entry points' in register_text


def test_orphan_cli_split_conservation():
    # Pins CONSERVATION on the real-tree run this file already exercises (Critic F8):
    # every zero-in-degree, non-private code candidate must land in exactly one of
    # code_orphans / cli_entries — never both (already asserted above), never neither.
    # The candidate set below is derived with the IDENTICAL predicate
    # split_orphans_and_cli_entries applies internally, fed the same code_nodes/code_deg/
    # main_guard_modules run() passes it — so this fails if the split ever becomes
    # non-exhaustive (a candidate silently dropped by both lists).
    from pathlib import Path
    root = Path(_ROOT)
    modules = sa.collect_py_modules(root)
    g_code, _parse_errors = sa.build_g_code(root, modules)
    code_nodes = list(modules)
    code_deg = sa.degrees(g_code, code_nodes)
    main_guard_modules = sa.collect_cli_entry_modules(root, modules)

    candidates = {n for n in code_nodes
                  if code_deg[n]['in'] == 0
                  and not n.endswith('.__main__')
                  and not n.split('.')[-1].startswith('_')}

    code_orphans, cli_entries = sa.split_orphans_and_cli_entries(code_nodes, code_deg, main_guard_modules)
    orphans_set, cli_set = set(code_orphans), set(cli_entries)

    assert orphans_set.isdisjoint(cli_set)
    assert orphans_set | cli_set == candidates
    assert len(code_orphans) + len(cli_entries) == len(candidates)
