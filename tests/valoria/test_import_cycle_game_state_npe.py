"""
OI-52a cycle-gone regression (ED-IN-0097,
audit/2026-07-29-code-shape-open-items/01_orchestration_plan_v1.md §3 Wave 4 item 2).

Loads skills/valoria-vector-audit/scripts/structure_audit.py the SAME way
engine/tests/test_pipeline_reach.py and tests/valoria/test_retired_tree_apparatus.py do
(importlib.util, since scripts/ is not a package) — reused, not re-implemented — and runs the
REAL cycle detection (tarjan_scc + _cycles) over the REAL repo tree.

Deliberately a NEW file rather than an addition to tests/valoria/test_structure_audit.py: this
wave's join lane (a parallel, file-disjoint worktree) owns structure_audit.py itself and its
existing test file this same wave (the __main__-guard predicate consolidation), so this test only
READS structure_audit.py's already-existing graph functions and does not touch either file.

Before this fix: `engine.autoload.game_state ↔ systems.world.sim.npe` was a 2-node cycle
(game_state.py:370 lazily imports npe.NPC; npe.py:184 lazily imported
game_state.canonical_accord) — both edges lazy, so no runtime import-time deadlock, but
structure_audit's AST-only g_code graph does not distinguish lazy from eager imports, so it
counted as a real cycle. canonical_accord moved to engine/substrate/canon_buckets.py (a no-deps
leaf both modules import at top level now), which deletes the npe -> game_state edge outright.

Two other cycle families are OUT OF SCOPE and must NOT move:
  - the 9-module systems.social_contest.sim.contest.* cycle (documented intentional-during-rebuild)
  - the 2 mass-battle cycles (systems.mass_battle.sim.massbattle <-> .units;
    the 5-module tests.sim.mass_battle.* cycle) — routed to the MB session's own plan
"""
import importlib.util
import os
from . import _structure_audit  # noqa: E402  the single owner of the loader

_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
_SCRIPT = os.path.join(_ROOT, 'skills', 'valoria-vector-audit', 'scripts', 'structure_audit.py')




def _real_cycles():
    sa = _structure_audit.load()
    root = sa.Path(_ROOT)
    modules = sa.collect_py_modules(root)
    g_code, parse_errors = sa.build_g_code(root, modules)
    assert not parse_errors, f"structure_audit failed to parse: {parse_errors}"
    scc = sa.tarjan_scc(g_code)
    return sa._cycles(scc, g_code)


def test_game_state_npe_cycle_is_gone():
    cycles = _real_cycles()
    for cyc in cycles:
        members = set(cyc)
        assert not ({'engine.autoload.game_state', 'systems.world.sim.npe'} <= members), (
            f"game_state <-> npe cycle still present: {cyc}"
        )


def test_exactly_three_cycles_remain_and_they_are_the_expected_families():
    cycles = _real_cycles()
    assert len(cycles) == 3, (
        f"expected exactly 3 remaining cycles (contest + 2 MB families), got "
        f"{len(cycles)}: {cycles}"
    )

    def _matches(cyc, prefix):
        return all(m.startswith(prefix) for m in cyc)

    contest = [c for c in cycles if _matches(c, 'systems.social_contest.sim.contest')]
    mb_massbattle = [c for c in cycles
                      if set(c) == {'systems.mass_battle.sim.massbattle', 'systems.mass_battle.sim.units'}]
    mb_tests = [c for c in cycles if _matches(c, 'tests.sim.mass_battle')]

    checked = 0
    for family_name, family in (
        ('social_contest.contest', contest),
        ('mass_battle.massbattle<->units', mb_massbattle),
        ('tests.sim.mass_battle', mb_tests),
    ):
        checked += 1
        assert len(family) == 1, f"{family_name}: expected exactly one cycle, found {family}"
    # assert-that-asserted (CLAUDE.md §0.1 point 2): confirm every named family was actually
    # looked up, not skipped by an early return.
    assert checked == 3

    # No family is a partial/renamed match of the other two — union covers all 3 cycles found.
    accounted = contest + mb_massbattle + mb_tests
    assert len(accounted) == len(cycles) == 3
