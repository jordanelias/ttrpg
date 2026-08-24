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
    the 5-module systems.mass_battle.sim.* cycle) — routed to the MB session's own plan
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


def test_exactly_two_cycles_remain_and_they_are_the_expected_families():
    """TWO, not three — the mass-battle port DELETED one, which is worth stating as a result.

    Through 2026-08-23 there were three: the social_contest family, the canon mass-battle family,
    and `systems.mass_battle.sim.massbattle <-> systems.mass_battle.sim.units`. That third one was
    the OLD engine's late-binding twin — `units.py` reached back into `massbattle.py`'s namespace
    for constants and helpers, and `massbattle.py` re-exported the dataclasses `units.py` defined.
    Jordan's port replaced both files: `units.py` is gone, and `massbattle.py` is now a thin
    strategic adapter that imports the canon engine one way and is imported by nothing. The cycle
    had nowhere left to close.

    Recorded here rather than silently re-pinned, because a cycle count going DOWN is the kind of
    result this repository usually only claims in prose.
    """
    cycles = _real_cycles()
    assert len(cycles) == 2, (
        f"expected exactly 2 remaining cycles (contest + the canon MB family), got "
        f"{len(cycles)}: {cycles}"
    )

    def _matches(cyc, prefix):
        return all(m.startswith(prefix) for m in cyc)

    contest = [c for c in cycles if _matches(c, 'systems.social_contest.sim.contest')]
    mb_canon = [c for c in cycles if _matches(c, 'systems.mass_battle.sim')]
    # The massbattle<->units family is DELETED, not merely absent — asserted so a future edit that
    # reintroduces it fails here rather than quietly restoring a cycle the port removed.
    reintroduced = [c for c in cycles
                    if set(c) == {'systems.mass_battle.sim.massbattle', 'systems.mass_battle.sim.units'}]
    assert not reintroduced, (
        f"the massbattle<->units cycle is back: {reintroduced}. It died with the 2026-08-24 port "
        f"(units.py deleted, massbattle.py reduced to a strategic adapter). Reintroducing it means "
        f"the adapter has grown a late-binding twin again.")

    checked = 0
    for family_name, family in (
        ('social_contest.contest', contest),
        ('systems.mass_battle.sim', mb_canon),
    ):
        checked += 1
        assert len(family) == 1, f"{family_name}: expected exactly one cycle, found {family}"
    # assert-that-asserted (CLAUDE.md §0.1 point 2): confirm every named family was actually
    # looked up, not skipped by an early return.
    assert checked == 2

    # Neither family is a partial/renamed match of the other — the union covers both cycles found.
    accounted = contest + mb_canon
    assert len(accounted) == len(cycles) == 2
