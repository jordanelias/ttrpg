"""ED-MB-0059 guard: the same-side cell-exclusion pass must never freeze a formation.

WHY THIS EXISTS (§0.1 point 5 — "if you cannot write the guard you have not understood the pattern").
The exclusion pass shipped in its first form accepting a time-of-impact of s == 0.0, exactly as the
cross-side loop above it does. On cross-side pairs that is safe: two armies start far apart and a
pre-existing contact is caught upstream by `halted_cells`, so s == 0 is the "defensive floor"
_pair_toi_scale's docstring calls it. Same-side pairs invert every one of those assumptions. A
formation is a LATTICE at pitch 1.0 and the bodies are 1.0 x 1.0 unit squares, so every adjacent cell
in every formation is touching BY CONSTRUCTION and permanently, and no cell is ever halted against
its own neighbour. Accepting s == 0.0 therefore capped essentially the whole army to zero motion on
essentially every tick.

WHAT THAT COST, measured before the fix (cell_field battery, 2 seeds): 1,213,199 extra body-box
solves, of which 568,785 (46.9%) returned exactly 0.0, against a 9.84% zero rate on cross-side pairs.
Halted cells FELL 20,356 -> 3,300 and resolve_toi_and_commit calls ROSE 1,482 -> 11,934 — frozen
formations never close, never contact, never halt, so every battle ran to the turn cap. That 8.05x
tick inflation was the whole of the "8.2x slowdown" the pass was first blamed for, and it is why the
swept-AABB broad phase written to fix the *cost* bought nothing: it culled pairs correctly inside a
loop whose ITERATION COUNT was the actual defect.

THE INVARIANT, stated so it is checkable: capping at s == 0.0 cannot un-overlap a pre-existing
overlap — it freezes the pair where it already sits, for zero corrective benefit and total motion
cost. The pass bounds "no pair may BECOME interpenetrating during this tick", a disjoint ->
overlapping transition, which is exactly s > 0. So:

    A RIGID FORMATION TRANSLATING IN FREE SPACE MUST BE BIT-IDENTICAL WITH THE PASS ON OR OFF.

Its cells stay at constant relative offsets, so no pair ever transitions, so the pass has nothing to
say. That is the property below, and it is the one that fails the instant `s <= 0.0` stops being
skipped.

MUTATION-VERIFIED at introduction: dropping `or s <= 0.0` from the same-side filter in
hierarchy/units.resolve_toi_and_commit fails test_rigid_translation_unaffected_by_exclusion (the
formation stops dead: displacement 0.0 against the flag-off arm's full step).
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'sim'))

import pytest  # noqa: E402

import mass_battle.hierarchy.units as _hu  # noqa: E402
import mass_battle.orchestration as _orch  # noqa: E402
from mass_battle import validators as _val  # noqa: E402
from mass_battle.engine import build_unit  # noqa: E402


@pytest.fixture
def field_path():
    """The exclusion pass lives inside resolve_toi_and_commit, which only runs under FIELD_MOVEMENT;
    on the grid oracle every assertion here would pass vacuously."""
    saved = [(m, m.FIELD_MOVEMENT, m.PC_NODE_COHESION) for m in (_hu, _orch)]
    _val._set_movement_path('node')
    try:
        yield
    finally:
        for m, fm, nc in saved:
            m.FIELD_MOVEMENT = fm
            m.PC_NODE_COHESION = nc


def _mk(name, faction, col):
    return build_unit('Line', 3, name, faction, col, troop_type='infantry', unit_type='melee',
                      power=4, command=4, discipline=5, morale=6, morale_start=None,
                      stance='balanced', speed='Standard', instructions=())


def _advance_free(exclusion, ticks=6):
    """One formation advancing toward a DISTANT enemy: far enough that no cross-side pair can touch
    within `ticks`, so side A's motion is a rigid translation and no same-side pair ever transitions
    disjoint -> overlapping. Returns A's final cell positions.

    The enemy must exist at all: `_node_advance` defers to the TOI solve only when
    `enemy_cells_float` is non-empty (`toi_deferred`), so with no opponent anywhere the exclusion
    pass is never reached and the test would pass vacuously. Distance, not absence, is what makes
    this the free-translation case.
    """
    saved = _hu.PC_CELL_EXCLUSION
    _hu.PC_CELL_EXCLUSION = exclusion
    try:
        import random
        random.seed(20260729)
        ua, ub = _mk('A', 'A', 9), _mk('B', 'B', 9)
        # park B at the far edge; A advances toward it and cannot reach it in `ticks`
        for atom in ub.subunits:
            atom.starting_position = (_hu.BATTLEFIELD_SIZE - 1, atom.starting_position[1])
        # same shape orchestration's nested _cells_float_of builds; _node_advance consults it only
        # for truthiness (it is the toi_deferred signal), so building it here is not a second owner
        # of any rule — just the same list.
        b_float = [(r, c, _hu.reach_for(sub.troop_type))
                   for sub in ub.subunits for (r, c) in sub.cells_float()]
        b_set = set(c for sub in ub.subunits for c in sub.cells())
        target = (float(_hu.BATTLEFIELD_SIZE - 1), float(ua.subunits[0].starting_position[1]))
        for _ in range(ticks):
            for atom in ua.subunits:
                atom.advance_cells(atom.eff_discipline, target,
                                   enemy_cells=b_set, enemy_cells_float=b_float)
            _hu.resolve_toi_and_commit(ua.subunits, ub.subunits)
        return {cid: tuple(round(v, 12) for v in pos)
                for cid, pos in sorted(ua.subunits[0]._node_pos.items())}
    finally:
        _hu.PC_CELL_EXCLUSION = saved


def test_rigid_translation_unaffected_by_exclusion(field_path):
    """THE GUARD. A formation moving in free space must land in exactly the same place whether the
    same-side pass runs or not — it has no pair to act on. Accepting s == 0.0 breaks this because
    the lattice's own permanent tangency reads as a collision."""
    off = _advance_free(False)
    on = _advance_free(True)
    assert off, "fixture produced no cell positions — the probe, not the engine, is broken"
    assert on == off, (
        "the exclusion pass moved a rigidly-translating formation. It can only do that by capping "
        "on a pair that was ALREADY touching at tick start — the lattice's permanent tangency — "
        "which freezes the army. The same-side filter must skip s <= 0.0.")


def test_free_formation_actually_moves(field_path):
    """Anti-vacuity, §0.1 point 2: an assertion must be able to observe the failure it excludes.
    If the fixture never moved at all, the equality above would hold trivially and this guard would
    be absent rather than weak."""
    one = _advance_free(True, ticks=1)
    many = _advance_free(True, ticks=6)
    assert one and many, "fixture produced no cell positions"
    moved = sum(1 for cid, pos in many.items() if pos != one.get(cid))
    assert moved > 0, (
        "no cell moved between tick 1 and tick 6 — the equality guard above would be vacuous, "
        "which is the deadlock it exists to catch showing up as a silent pass")


def test_exclusion_flag_is_pinned_in_the_golden_gate():
    """PC_CELL_EXCLUSION is strongly digest-moving on both field modes, so an ambient flip must
    produce a NAMED red in the golden gate rather than a mystery mismatch."""
    import importlib.util
    root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    spec = importlib.util.spec_from_file_location(
        'ci_golden_modes_check', os.path.join(root, 'tools', 'ci_golden_modes_check.py'))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    assert mod.FIELD_PINS.get('PC_CELL_EXCLUSION') == '1', (
        "PC_CELL_EXCLUSION must be pinned in tools/ci_golden_modes_check.py FIELD_PINS — it moves "
        "unit_field and cell_field.")
