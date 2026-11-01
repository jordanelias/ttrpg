"""Spatial-model acceptance: contact fires on the reach body, and the collision step stops on the BODY (a circle).

Contact (core.contact._find_contacts_standoff) fires on geometry.reach_reaches -- the body grown forward by
weapon reach. The collision step (hierarchy.units.resolve_toi_and_commit) stops each cell's advance at the
BODY-vs-BODY touch (two circles one pitch across, reach 0) -- NOT at the reach-extended surface. The two are
DELIBERATELY different: reach is a weapon envelope that engages ACROSS a gap, while the hard geometric stop is
the body (two bodies that cannot interpenetrate). Bodies collide; weapons reach across the closing gap.
Stopping on the reach surface instead parked cells on the reach touch boundary, where the strict contact
predicate returns False -> a permanent zero-casualty standoff. Both apply on the FIELD_MOVEMENT path only;
the grid oracle (FIELD_MOVEMENT=0) must not see the new code at all.

This file is the R1 probe the plan (spatial_model_v2_plan.md §1 R1, Stage C) demands:
  (a) head-on contact fires at reach touch, not before;
  (b) after every committed tick, opposing cell BODIES never interpenetrate (circular bodies stay
      disjoint-or-touching; the reach bodies MAY overlap -- that overlap IS the melee
      engagement, not a drive-through);
  (c) a closing head-on pair AND a cavalry charge both REACH contact (no permanent stall) and the
      battle resolves (casualties exchanged);
  (d) the FIELD_MOVEMENT=0 grid path never touches the body code (guarded by poisoning the primitive);
  (e) troop conservation (I1: Sum cell_troops == hp per unit) holds across a short battle.

Deterministic + seeded. Process-global movement toggles are saved/restored in finally (the same
discipline test_mass_battle_maneuvers.py documents) so node/grid state never leaks between tests.
"""
import math
import os
import sys


import pytest  # noqa: E402

import modules.mass_battle.hierarchy.units as _hu  # noqa: E402
import modules.mass_battle.orchestration as _orch  # noqa: E402
import modules.mass_battle.core.contact as _contact  # noqa: E402
import modules.mass_battle.geometry as _geo  # noqa: E402
from modules.mass_battle.geometry import body_depth, cellbody_from  # noqa: E402
from systems.mass_battle.sim.engine import build_unit  # noqa: E402
from systems.mass_battle.sim import validators as _val  # noqa: E402

from ._conservation import assert_troop_conservation  # noqa: E402


# ─── helpers ─────────────────────────────────────────────────────────────────

@pytest.fixture
def field_path():
    """Force the live coordinate-field path (FIELD_MOVEMENT=1, MB_NODE_COHESION=1) for the test body,
    then restore whatever was ambient. Units built inside the `with`/fixture run on the node path."""
    saved = [(m, m.FIELD_MOVEMENT, m.MB_NODE_COHESION) for m in (_hu, _orch)]
    _val._set_movement_path('node')
    try:
        yield
    finally:
        for m, fm, nc in saved:
            m.FIELD_MOVEMENT = fm
            m.MB_NODE_COHESION = nc


@pytest.fixture
def grid_path():
    """Force the frozen grid oracle (FIELD_MOVEMENT=0, MB_NODE_COHESION=0), restore after."""
    saved = [(m, m.FIELD_MOVEMENT, m.MB_NODE_COHESION) for m in (_hu, _orch)]
    _val._set_movement_path('grid')
    try:
        yield
    finally:
        for m, fm, nc in saved:
            m.FIELD_MOVEMENT = fm
            m.MB_NODE_COHESION = nc


_PENETRATION_TOL = 1e-6   # lattice units: below this a pair is tangent, not interpenetrating (float noise on a distance)


def _cross_side_bodies(unit_a, unit_b):
    """Every (bodyA, bodyB) cross-side cell-body pair, built exactly as contact and the collision step build them
    (circle, front reach = reach_for(troop_type), heading = cell facing)."""
    a_bodies = []
    for atom in unit_a.subunits:
        a_bodies.extend(_hu.cell_bodies_for(atom, _hu.reach_for(atom.troop_type)))
    b_bodies = []
    for atom in unit_b.subunits:
        b_bodies.extend(_hu.cell_bodies_for(atom, _hu.reach_for(atom.troop_type)))
    for ba in a_bodies:
        for bb in b_bodies:
            yield ba, bb


class _CommitProbe:
    """Wraps separate_all_bodies, the end-of-tick guarantee: after each REAL call, records whether any two opposing
    cell BODIES interpenetrate. The body is the circle (reach 0) -- the hard stop surface -- so two bodies may TOUCH
    but never overlap. The reach bodies are NOT checked here: their overlap is the intended melee engagement
    (contact fires across the closing gap), not a violation. (Movement itself, resolve_toi_and_commit, is only
    approximately clear while a tick is in progress; this pass is what makes the end of every tick exact.)"""
    def __init__(self):
        self.body_interpenetration = False
        self.commits = 0
        self._real = _hu.separate_all_bodies

    def __enter__(self):
        def wrapped(unit_a, unit_b):
            moved = self._real(unit_a, unit_b)
            self.commits += 1
            for ba, bb in _cross_side_bodies(unit_a, unit_b):
                if body_depth(cellbody_from(ba.cr, ba.cc, ba.heading), cellbody_from(bb.cr, bb.cc, bb.heading)) > _PENETRATION_TOL:
                    self.body_interpenetration = True
            return moved
        _orch.separate_all_bodies = wrapped
        return self

    def __exit__(self, *exc):
        _orch.separate_all_bodies = self._real
        return False


# ─── (a) head-on contact fires at reach touch ─────────────────────────────────

def test_head_on_contact_fires_at_reach_touch(field_path):
    """Two head-on cells: contact fires strictly inside the OBB touch distance and NOT beyond it.
    The touch distance is BODY + reach envelope = 2*CELL_RADIUS + reach (one weapon reaching the other's
    body across the gap) -- reach-DERIVED so this stays correct as weapon-class reach changes (v2 Stage E
    moved the default melee reach from 0.5 to reach_for('infantry')=0.1, so the threshold moved 1.5->1.1;
    pinning it to the live reach keeps the test a real geometry check, not a frozen constant)."""
    from modules.mass_battle.core.contact import find_contacts
    thr = 2 * _hu.CELL_RADIUS + _hu.reach_for('infantry')   # the reach-touch centre-gap
    # place B just closer than reach touch -> contact; and just beyond -> none. Build via a small helper.
    a = build_unit('Line', 3, 'A', 'A', 9)
    for gap, want in [(thr - 0.02, True), (thr + 0.02, False), (thr + 0.4, False)]:
        b = build_unit('Line', 3, 'B', 'B', 9)
        # pin both single cells head-on `gap` apart on the same column (node path floats).
        a_cid = next(iter(a.subunits[0]._node_pos))
        b_cid = next(iter(b.subunits[0]._node_pos))
        a.subunits[0]._node_pos[a_cid] = (0.0, 0.0)
        b.subunits[0]._node_pos[b_cid] = (gap, 0.0)
        a.subunits[0].cell_facing_vec[a_cid] = (1.0, 0.0)   # A faces +row toward B
        b.subunits[0].cell_facing_vec[b_cid] = (-1.0, 0.0)  # B faces -row toward A
        pairs = find_contacts(a, b)
        fired = len(pairs) > 0
        assert fired == want, f"gap={gap}: contact fired={fired}, expected {want}"


# ─── (b)+(c) head-on: no interpenetration, no stall, resolves ───────────────

def test_head_on_no_interpenetration_no_stall(field_path):
    """A head-on Line-vs-Line closes to contact, exchanges casualties (no stall), and at no committed
    tick do opposing cell BODIES interpenetrate (circular bodies stay disjoint-or-touching; the
    reach bodies MAY overlap -- that is the engagement, checked by the casualties below)."""
    import random
    random.seed(4242)
    a = build_unit('Line', 3, 'A', 'A', 9)
    b = build_unit('Line', 3, 'B', 'B', 9)
    hp_a0, hp_b0 = a.hp, b.hp
    with _CommitProbe() as probe:
        _orch.run_battle(a, b, max_turns=18)
    assert probe.commits > 0, "the end-of-tick pass never ran -> not on the field path"
    assert not probe.body_interpenetration, "opposing cell BODIES interpenetrated after a commit"
    # no stall: contact was reached and combat resolved -> at least one side lost troops.
    assert (a.hp < hp_a0) or (b.hp < hp_b0), "no casualties -> cells stalled short of contact"


def test_cavalry_charge_reaches_contact(field_path):
    """A fast cavalry cell charging a standing infantry line must REACH contact (no freeze short) and
    resolve. Cavalry = 'Fast'; the BODY stop must not halt it short of the enemy body -- it drives to
    body contact and its weapons engage across the closing gap (bodies must still never interpenetrate)."""
    import random
    random.seed(77)
    cav = build_unit('Line', 3, 'CAV', 'A', 9, troop_type='cavalry', speed='Fast')
    inf = build_unit('Line', 3, 'INF', 'B', 9, troop_type='infantry')
    hp_c0, hp_i0 = cav.hp, inf.hp
    with _CommitProbe() as probe:
        _orch.run_battle(cav, inf, max_turns=18)
    assert probe.commits > 0
    assert not probe.body_interpenetration, "charge drove bodies into interpenetration"
    assert (cav.hp < hp_c0) or (inf.hp < hp_i0), "cavalry charge stalled short of contact"


# ─── (d) grid oracle never touches the body code ─────────────────────────────

def test_grid_path_never_calls_body_code(grid_path, monkeypatch):
    """FIELD_MOVEMENT=0: the frozen grid path must not run any body code. Poison the primitive so ANY
    call raises, then run a full grid battle -- it must complete untouched (proves the body geometry is
    entirely field-gated; complements the byte-exact digest gate)."""
    import random

    def _poison(*a, **k):
        raise AssertionError("body primitive called on the FIELD_MOVEMENT=0 grid path")

    # poison every module that could reach the primitive by name
    monkeypatch.setattr(_geo, 'reach_reaches', _poison)
    monkeypatch.setattr(_contact, 'reach_reaches', _poison, raising=False)
    monkeypatch.setattr(_hu, 'reach_reaches', _poison, raising=False)
    monkeypatch.setattr(_hu, 'cell_bodies_for', _poison)
    monkeypatch.setattr(_hu, 'separate_all_bodies', _poison)
    random.seed(1)
    a = build_unit('Line', 3, 'A', 'A', 9)
    b = build_unit('Line', 3, 'B', 'B', 9)
    res = _orch.run_battle(a, b, max_turns=18)  # must NOT raise
    assert res['winner'] in ('A', 'B', 'draw')


# ─── (e) conservation (I1) over a short field battle ────────────────────────

def test_conservation_over_short_battle(field_path):
    """I1: Sum cell_troops == hp for BOTH units at battle end (the geometry swap touches no troop
    bookkeeping, so this must hold with only float slop).

    [ED-MB-0045 S6] Routed through the single owner `_conservation.assert_troop_conservation`; the
    old open-coded loop skipped routed/broken units without counting the skip, so it could assert
    nothing and still pass.
    """
    import random
    random.seed(2026)
    a = build_unit('Line', 3, 'A', 'A', 9)
    b = build_unit('Line', 3, 'B', 'B', 9)
    _orch.run_battle(a, b, max_turns=18)
    checked = assert_troop_conservation(a, b, context='body seed=2026')
    assert checked >= 2, f"conservation checked {checked} units, expected both"


# ─── determinism (I2) ────────────────────────────────────────────────────────

def test_determinism_same_seed(field_path):
    """Same seed twice -> identical public outcome (winner, turns, final hp)."""
    import random

    def _run():
        random.seed(9001)
        a = build_unit('Line', 3, 'A', 'A', 9)
        b = build_unit('Line', 3, 'B', 'B', 9)
        res = _orch.run_battle(a, b, max_turns=18)
        return (res['winner'], res['turns'], round(a.hp, 6), round(b.hp, 6))

    assert _run() == _run()
