"""[ED-MB-0041 phase 1] The cell is the primitive for MORALE.

Jordan, 2026-07-25: *"the cell needs to be the primitive for morale, discipline, quality, stamina,
route, health, armour, facing, damage, troops count, etc"*, and earlier: *"cells get modulated /
disciplined / harnessed by subunit holistic scoring/behaviour, but the cells themselves are what
aggregate into those subunit holistic scorings in the first place, so a cell should be able to have
worse morale than another cell in same subunit."*

Before this, the cell was the primitive for GEOMETRY only — position, facing, contact, casualty
placement. Every piece of state (morale, discipline, quality, stamina, rout, hp, armour) was a subunit
scalar, so that last sentence was literally not representable: a rear cell being cut down and a front
cell holding shared one number.

The model is a two-way loop, not a broadcast:
  AGGREGATE UP     the subunit's morale is the troop-weighted mean of its cells — derived, not stored.
  MODULATE DOWN    that holistic value pulls its own cells back toward it, discipline-gated (du Picq:
                   men hold because the men beside them hold).

Gated behind `PC_CELL_MORALE`, default OFF, so an unseeded subunit takes the scalar path verbatim.
"""
import os
import sys

import pytest

_SIM = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'sim'))
if _SIM not in sys.path:
    sys.path.insert(0, _SIM)

import mass_battle.config as C
from mass_battle.engine import build_army, SIDE_A_START_ROW
from mass_battle.percell import _apply_with_spill


def _atom(troops=300.0, conc=100.0):
    u = build_army([{'shape': 'Line', 'troop_type': 'infantry', 'troops': troops,
                     'concentration': conc, 'starting_position': (SIDE_A_START_ROW, 20)}], 'A', 'A')
    return u.subunits[0]


def _seeded():
    a = _atom()
    a.seed_cell_morale()
    return a


# ─── the directive itself ────────────────────────────────────────────────────

def test_a_cell_can_have_worse_morale_than_its_sibling():
    """Jordan's test case, stated verbatim as a requirement. It was previously unrepresentable."""
    a = _seeded()
    cids = list(a.cell_troops)
    assert len(cids) >= 2, "need at least two cells for the claim to mean anything"
    _apply_with_spill([(a, cids[0], 1.0)], a.cell_troops[cids[0]] * 0.6)
    assert a.cell_morale[cids[0]] < a.cell_morale[cids[1]], \
        "a cell that was cut down must hold worse morale than an untouched sibling"


def test_seeding_leaves_the_aggregate_identical_to_the_scalar():
    """At t=0 the two models must agree exactly — divergence has to be EARNED, not injected at birth."""
    a = _atom()
    before = a.eff_morale
    a.seed_cell_morale()
    assert a.eff_morale == pytest.approx(float(before))


def test_unseeded_is_the_scalar_path_verbatim():
    """The shipped default. No cell morale -> the old expression, untouched."""
    a = _atom()
    assert not a.cell_morale
    assert a.eff_morale == (a.morale if a.morale is not None else a._u().morale)


# ─── aggregate up ────────────────────────────────────────────────────────────

def test_aggregate_is_troop_weighted_not_a_flat_mean():
    """A nearly-empty shattered cell must not drag the body as hard as a full one.

    Flat-meaning the cells would let a cell holding three men count as much as one holding a hundred,
    so a body would read as broken while almost all of its strength was still steady.
    """
    a = _seeded()
    cids = list(a.cell_troops)
    big, small = cids[0], cids[1]
    a.cell_troops[small] = 1.0            # this cell is nearly gone
    a.cell_morale[small] = 0.0            # ...and shattered
    a.cell_morale[big] = 6.0
    for c in cids[2:]:
        a.cell_morale[c] = 6.0
    assert a.eff_morale > 5.0, \
        "a one-man shattered cell must not pull the body down as if it were a full one"


def test_local_damage_moves_the_aggregate():
    """Aggregate-up has to be live: hurting a cell must be felt by the body."""
    a = _seeded()
    before = a.eff_morale
    cid = list(a.cell_troops)[0]
    _apply_with_spill([(a, cid, 1.0)], a.cell_troops[cid] * 0.5)
    assert a.eff_morale < before


# ─── modulate down ───────────────────────────────────────────────────────────

def test_cohesion_pulls_a_shaken_cell_back_toward_the_body():
    a = _seeded()
    cid = list(a.cell_troops)[0]
    a.cell_morale[cid] = 1.0
    before = a.cell_morale[cid]
    a.cohere_cells()
    assert a.cell_morale[cid] > before, "a steady body must steady its shaky corner"


def test_cohesion_drags_a_firm_cell_down_in_a_disintegrating_body():
    """The pull is signed, not a floor — the loop must run both ways or it is just a rally bonus."""
    a = _seeded()
    cids = list(a.cell_troops)
    for c in cids[1:]:
        a.cell_morale[c] = 0.5           # the body is coming apart
    a.cell_morale[cids[0]] = 6.0         # one corner still firm
    a.cohere_cells()
    assert a.cell_morale[cids[0]] < 6.0, "a collapsing body must drag its firm corner down"


def test_cohesion_conserves_the_aggregate():
    """Cohesion REDISTRIBUTES morale; it must not create or destroy any.

    new_m = m + r*(agg - m), so the troop-weighted mean of new_m is agg + r*(agg - agg) = agg. If this
    ever fails, cohesion has become a free morale source and a body could steady itself indefinitely.
    """
    a = _seeded()
    cids = list(a.cell_troops)
    a.cell_morale[cids[0]] = 1.0
    a.cell_morale[cids[-1]] = 6.0
    before = a.eff_morale
    for _ in range(5):
        a.cohere_cells()
    assert a.eff_morale == pytest.approx(before), "cohesion must conserve the body's total morale"


def test_cohesion_is_discipline_gated():
    """Closing ranks around a wavering cell is what discipline names; a levy should do it worse."""
    hi, lo = _seeded(), _seeded()
    hi.discipline, lo.discipline = 6, 1
    cid_h, cid_l = list(hi.cell_troops)[0], list(lo.cell_troops)[0]
    hi.cell_morale[cid_h] = 1.0
    lo.cell_morale[cid_l] = 1.0
    hi.cohere_cells(); lo.cohere_cells()
    assert (hi.cell_morale[cid_h] - 1.0) > (lo.cell_morale[cid_l] - 1.0), \
        "a disciplined body must close ranks harder than a levy"


# ─── erosion shape ───────────────────────────────────────────────────────────

def test_erosion_scales_by_fraction_of_the_cell_not_absolute_count():
    """Losing 20 of 100 beside you is the same shock at any body size.

    An absolute scale would make DENSE cells look braver purely for being dense — the same class of
    error as weighting a collapse by live rather than starting strength.
    """
    thin, dense = _atom(troops=150.0, conc=50.0), _atom(troops=600.0, conc=200.0)
    thin.seed_cell_morale(); dense.seed_cell_morale()
    tc, dc = list(thin.cell_troops)[0], list(dense.cell_troops)[0]
    _apply_with_spill([(thin, tc, 1.0)], thin.cell_troops[tc] * 0.5)
    _apply_with_spill([(dense, dc, 1.0)], dense.cell_troops[dc] * 0.5)
    assert thin.cell_morale[tc] == pytest.approx(dense.cell_morale[dc]), \
        "equal FRACTIONAL loss must cost equal morale regardless of cell density"


def test_default_is_gated_off():
    assert C.PC_CELL_MORALE is False, "phase 1 ships gated OFF until measured on both scoreboards"
