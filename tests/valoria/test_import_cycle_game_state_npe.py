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


def test_exactly_four_cycles_remain_and_they_are_the_expected_families():
    """FOUR since 2026-09-07, and the two new ones are NOT NEW CYCLES — they are two cycles this
    detector could not see until `engine/season/` was decomposed (ED-IN-0203).

    ⚠ THE CLAIM THAT THEY PRE-EXIST IS MEASURED, NOT ASSERTED, because the whole value of this
    count is that a rise means a real regression. Run against the tree at `2f13271` — the
    commit immediately before the decomposition — this file's own `_real_cycles()` returns
    **2 cycles and ZERO season cycles**, while `engine/season/combat_seam.py` already carried
    `import shape as S` and `shape.py` already carried `import combat_seam` at what is now
    `:6741`. The relationships were identical; the SPELLING was a bare name, which
    `_resolve_internal` cannot bind to an internal module, so the edge was dropped. The
    decomposition converted every intra-package import to a relative one, and the edges appeared.
    **A deferred or bare-named import hides a cycle from an instrument; it does not remove it**
    (`CLAUDE.md` §3 says the same thing about the interpreter, one level down).

    Both are SHRINK-ONLY, on the `PATH_SEAM_ALLOWED` discipline: each carries its reason and the
    point at which it goes, and removing one means deleting its entry in the same commit.

      * `engine.season.combat_seam` <-> `engine.season.shape` — A REAL DEFERRED CYCLE. Both edges
        are function-local (`combat_seam:122,137`, `shape`'s `contest` fallback). It dissolves at
        step 8 of the decomposition plan, where `body_band_penalty` lands below the seam and the
        seam stops needing `shape` at all. Not fixed here because doing step 8 out of order to
        green a gate is how a split loses its ordering.

      * `engine.season.harness.exercises` <-> `engine.season.harness.run_cases` — **NOT A RUNTIME
        CYCLE AT ALL, and this entry exists to say so rather than to excuse it.** `run_cases`
        imports `exercises` at module level; the return edge is one import inside
        `exercises.py`'s `if __name__ == "__main__":` block, which cannot execute while anything
        is importing it. `build_g_code` walks the whole AST, and the `__main__`-guard predicate
        this repository already single-owns (`ci_common.has_main_guard`, OI-52a) is used only for
        orphan/CLI classification, never for edge construction. ⚠ **That is a real available
        consolidation and it is NOT taken here**: measured 2026-09-07, TEN modules repo-wide carry
        `__main__`-guarded imports (`engine.season.harness.{exercises,report}`, five under
        `combat_engine_v1`, two under `mass_battle.sim`, `tools.compliance_check`), so the rule
        change would move edges — and possibly orphan/CLI verdicts — well outside this lane. It
        belongs in its own change, with its own before/after.

    THE ORIGINAL NOTE, unchanged — TWO, not three: the mass-battle port DELETED one, which is
    worth stating as a result.

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
    assert len(cycles) == 4, (
        f"expected exactly 4 remaining cycles (contest + the canon MB family + the two declared "
        f"engine.season ones), got {len(cycles)}: {cycles}"
    )

    def _matches(cyc, prefix):
        return all(m.startswith(prefix) for m in cyc)

    contest = [c for c in cycles if _matches(c, 'systems.social_contest.sim.contest')]
    mb_canon = [c for c in cycles if _matches(c, 'systems.mass_battle.sim')]
    # The two declared season cycles, matched by their EXACT member sets rather than by a prefix.
    # A prefix match would silently absorb a THIRD season cycle a later carving step introduces,
    # which is the one thing this count exists to catch.
    seam_shape = [c for c in cycles
                  if set(c) == {'engine.season.combat_seam', 'engine.season.shape'}]
    harness_main = [c for c in cycles
                    if set(c) == {'engine.season.harness.exercises',
                                  'engine.season.harness.run_cases'}]
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
        ('engine.season combat_seam<->shape', seam_shape),
        ('engine.season harness __main__ edge', harness_main),
    ):
        checked += 1
        assert len(family) == 1, f"{family_name}: expected exactly one cycle, found {family}"
    # assert-that-asserted (CLAUDE.md §0.1 point 2): confirm every named family was actually
    # looked up, not skipped by an early return.
    assert checked == 4

    # No family is a partial/renamed match of another — the union covers every cycle found, so a
    # fifth cycle cannot hide behind a family that matched two.
    accounted = contest + mb_canon + seam_shape + harness_main
    assert len(accounted) == len(cycles) == 4
