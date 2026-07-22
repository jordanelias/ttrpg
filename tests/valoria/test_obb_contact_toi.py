"""Spatial-model v2 Stage B+C acceptance: the CIRCLE->BOX contact + BODY-stop shape swap.

Stage B (core.contact._find_contacts_standoff) fires contact on obb_front_reach_overlap -- the boxed
engagement surface (unit body grown by weapon reach on the front face) -- instead of the isotropic
circle math.hypot(Δ) <= standoff_from_reach. Stage C (hierarchy.units.resolve_toi_and_commit) halts
each cell's Euclidean advance at the BODY-vs-BODY touch surface (unit squares, reach 0) -- NOT the
reach-extended surface. The two are DELIBERATELY different: reach is a weapon envelope that engages
ACROSS a gap (contact fires on the reach box), while the hard geometric stop is the body (two squares
that cannot interpenetrate). Bodies collide; weapons reach across the closing gap. Stopping on the
reach surface instead parked cells on the obb_front_reach_overlap TOUCH boundary, where the strict
contact predicate returns False -> a permanent zero-casualty standoff (the bug this fixes). Both apply
on the FIELD_MOVEMENT path only; the grid oracle (FIELD_MOVEMENT=0) must not see the new code at all.

This file is the R1 probe the plan (spatial_model_v2_plan.md §1 R1, Stage C) demands:
  (a) head-on contact fires at OBB reach-touch, not before;
  (b) after every committed tick, opposing cell BODIES never interpenetrate (unit-square bodies stay
      disjoint-or-touching; the reach engagement surfaces MAY overlap -- that overlap IS the melee
      engagement, not a drive-through);
  (c) a closing head-on pair AND a cavalry charge both REACH contact (no permanent stall) and the
      battle resolves (casualties exchanged);
  (d) the FIELD_MOVEMENT=0 grid path never touches the OBB code (guarded by poisoning the primitive);
  (e) troop conservation (I1: Sum cell_troops == hp per live unit) holds across a short battle.

Deterministic + seeded. Process-global movement toggles are saved/restored in finally (the same
discipline test_mass_battle_maneuvers.py documents) so node/grid state never leaks between tests.
"""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'sim'))  # tests/sim on path

import pytest  # noqa: E402

import mass_battle.hierarchy.units as _hu  # noqa: E402
import mass_battle.orchestration as _orch  # noqa: E402
import mass_battle.core.contact as _contact  # noqa: E402
import mass_battle.geometry as _geo  # noqa: E402
from mass_battle.geometry import cellbox_from, obb_overlap  # noqa: E402
from mass_battle.engine import build_unit  # noqa: E402
from mass_battle import validators as _val  # noqa: E402


# ─── helpers ─────────────────────────────────────────────────────────────────

@pytest.fixture
def field_path():
    """Force the live coordinate-field path (FIELD_MOVEMENT=1, PC_NODE_COHESION=1) for the test body,
    then restore whatever was ambient. Units built inside the `with`/fixture run on the node path."""
    saved = [(m, m.FIELD_MOVEMENT, m.PC_NODE_COHESION) for m in (_hu, _orch)]
    _val._set_movement_path('node')
    try:
        yield
    finally:
        for m, fm, nc in saved:
            m.FIELD_MOVEMENT = fm
            m.PC_NODE_COHESION = nc


@pytest.fixture
def grid_path():
    """Force the frozen grid oracle (FIELD_MOVEMENT=0, PC_NODE_COHESION=0), restore after."""
    saved = [(m, m.FIELD_MOVEMENT, m.PC_NODE_COHESION) for m in (_hu, _orch)]
    _val._set_movement_path('grid')
    try:
        yield
    finally:
        for m, fm, nc in saved:
            m.FIELD_MOVEMENT = fm
            m.PC_NODE_COHESION = nc


def _cross_side_boxes(unit_a, unit_b):
    """Every (boxA, boxB) cross-side cell-box pair, built exactly as Stage B/C build them (unit square,
    front reach = reach_for(troop_type), heading = cell facing)."""
    a_boxes = []
    for atom in unit_a.subunits:
        a_boxes.extend(_hu.cell_boxes_for(atom, _hu.reach_for(atom.troop_type)))
    b_boxes = []
    for atom in unit_b.subunits:
        b_boxes.extend(_hu.cell_boxes_for(atom, _hu.reach_for(atom.troop_type)))
    for ba in a_boxes:
        for bb in b_boxes:
            yield ba, bb


class _CommitProbe:
    """Wraps resolve_toi_and_commit: after each REAL commit, records whether any two opposing cell
    BODIES strictly interpenetrate. The body is the unit square (reach 0) -- the hard stop surface --
    so two bodies may TOUCH (SAT is strict: touching == separated) but never overlap. The reach-
    extended surfaces are NOT checked here: their overlap is the intended melee engagement (contact
    fires across the closing gap), not a violation."""
    def __init__(self):
        self.body_interpenetration = False
        self.commits = 0
        self._real = _hu.resolve_toi_and_commit

    def __enter__(self):
        def wrapped(a_subs, b_subs):
            self._real(a_subs, b_subs)
            self.commits += 1
            # rebuild a Unit-like shim view: cell_boxes_for takes an atom, and _cross_side_boxes takes
            # units, so pass lightweight holders exposing .subunits.
            ua = type('U', (), {'subunits': a_subs})()
            ub = type('U', (), {'subunits': b_subs})()
            for ba, bb in _cross_side_boxes(ua, ub):
                body_a = cellbox_from(ba.cr, ba.cc, ba.heading, reach_front=0.0)
                body_b = cellbox_from(bb.cr, bb.cc, bb.heading, reach_front=0.0)
                if obb_overlap(body_a, body_b):
                    self.body_interpenetration = True
        _orch.resolve_toi_and_commit = wrapped
        return self

    def __exit__(self, *exc):
        _orch.resolve_toi_and_commit = self._real
        return False


def _unit_troops(unit):
    return sum(sum(su.cell_troops.values()) for su in unit.subunits)


# ─── (a) head-on contact fires at OBB touch ─────────────────────────────────

def test_head_on_contact_fires_at_obb_touch(field_path):
    """Two head-on short-reach cells: contact fires strictly inside OBB touch distance (centre gap <
    1.5 = 2*(0.5 body-half + 0.5 reach) - 0.5... i.e. reach envelope meets body), and NOT at a gap the
    old circle test (standoff 2.0) would have fired. Exercises the real _find_contacts_standoff."""
    from mass_battle.core.contact import find_contacts
    # place B just closer than OBB touch -> contact; and just beyond -> none. Build via a small helper.
    a = build_unit('Line', 3, 'A', 'A', 9)
    for gap, want in [(1.49, True), (1.51, False), (1.9, False)]:
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
    tick do opposing cell BODIES interpenetrate (unit-square bodies stay disjoint-or-touching; the
    reach surfaces MAY overlap -- that is the engagement, checked by the casualties below)."""
    import random
    random.seed(4242)
    a = build_unit('Line', 3, 'A', 'A', 9)
    b = build_unit('Line', 3, 'B', 'B', 9)
    hp_a0, hp_b0 = a.hp, b.hp
    with _CommitProbe() as probe:
        _orch.run_battle(a, b, max_turns=18)
    assert probe.commits > 0, "TOI never ran -> not on the field path"
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


# ─── (d) grid oracle never touches the OBB code ─────────────────────────────

def test_grid_path_never_calls_obb(grid_path, monkeypatch):
    """FIELD_MOVEMENT=0: the frozen grid path must not run any OBB code. Poison the primitive so ANY
    call raises, then run a full grid battle -- it must complete untouched (proves the box swap is
    entirely field-gated; complements the byte-exact digest gate)."""
    import random

    def _poison(*a, **k):
        raise AssertionError("OBB primitive called on the FIELD_MOVEMENT=0 grid path")

    # poison every module that could reach the primitive by name
    monkeypatch.setattr(_geo, 'obb_front_reach_overlap', _poison)
    monkeypatch.setattr(_contact, 'obb_front_reach_overlap', _poison, raising=False)
    monkeypatch.setattr(_hu, 'obb_front_reach_overlap', _poison, raising=False)
    monkeypatch.setattr(_hu, 'cell_boxes_for', _poison)
    random.seed(1)
    a = build_unit('Line', 3, 'A', 'A', 9)
    b = build_unit('Line', 3, 'B', 'B', 9)
    res = _orch.run_battle(a, b, max_turns=18)  # must NOT raise
    assert res['winner'] in ('A', 'B', 'draw')


# ─── (e) conservation (I1) over a short field battle ────────────────────────

def test_conservation_over_short_battle(field_path):
    """I1: Sum cell_troops == hp for every non-routed/broken unit, at battle end (the geometry swap
    touches no troop bookkeeping, so this must hold with only float slop)."""
    import random
    random.seed(2026)
    a = build_unit('Line', 3, 'A', 'A', 9)
    b = build_unit('Line', 3, 'B', 'B', 9)
    _orch.run_battle(a, b, max_turns=18)
    for unit in (a, b):
        if unit.routed or unit.broken:
            continue
        assert math.isclose(_unit_troops(unit), unit.hp, rel_tol=1e-6, abs_tol=1e-3), \
            f"{unit.name}: Sum cell_troops={_unit_troops(unit)} != hp={unit.hp}"


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
