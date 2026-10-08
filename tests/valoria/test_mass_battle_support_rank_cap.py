"""MB-07, J-18 (A): cap the depth support stack at the ranks a troop type's weapon reaches.

The uncapped stack counts every rank behind the contact rank — 1.0, 0.7, 0.5, then 0.3 at EVERY depth
with no cutoff — so of two forces of EQUAL troops the deeper one keeps adding pool from ranks its weapons
could never bring to bear. `config.support_weight` is the single owner of a rank's weight; with
`MB_SUPPORT_RANK_CAP` ON, a rank past `support_ranks_for(troop_type)` weighs 0.

SHIPPED OFF (config.py at the flag): ON stalls the bat.py battery (mirror/cav_shaken/ranged at
MAX_TURNS=20 in every probed seed, ~2.8x slower, cell_field_mor0 688.7s) until casualty/pool magnitudes
are recalibrated. So every cap-ON assertion here sets the flag explicitly, and one test pins that the
shipped default reproduces the uncapped stack to the last float digit.

The forces: a tier-4 Line (7 files x 5 ranks) and a tier-4 Column (5 files x 7 ranks) — 35 cells and the
same 800 troops each, so the only difference is depth. Contact is each force's front rank (orig row 0).
"""
import math
import os

import pytest

import systems.mass_battle.sim.config as C
from systems.mass_battle.sim.core.exchange import _pair_engaged_troops
from systems.mass_battle.sim.geometry import _oriented_abs_map
from systems.mass_battle.sim.hierarchy.units import Subunit

from .test_reach_weapon_class import _charge_vs_brace, field_path  # noqa: F401  (fixture re-export)
import systems.mass_battle.sim.orchestration as _orch
from systems.mass_battle.sim.engine import build_unit

_TYPES = ('infantry', 'heavy_infantry', 'pike', 'cavalry')
_SHAPES = ('Line', 'Column')

# Measured on the pre-MB-07 tree (HEAD bec707aa, Python 3.11.17): full engaged troops and the share
# carried by ranks past each type's cap. Identical for every type uncapped (troop_type was not read).
_UNCAPPED_FULL = {'Line': 560.0000000000002, 'Column': 468.5714285714283}
_UNCAPPED_BEYOND = {
    ('infantry', 'Line'): 240.00000000000028, ('infantry', 'Column'): 239.99999999999974,
    ('heavy_infantry', 'Line'): 128.00000000000028, ('heavy_infantry', 'Column'): 159.99999999999977,
    ('pike', 'Line'): 48.00000000000023, ('pike', 'Column'): 102.85714285714266,
    ('cavalry', 'Line'): 128.00000000000028, ('cavalry', 'Column'): 159.99999999999977,
}


def _force(troop_type, shape):
    """A fresh tier-4 subunit and its front-rank contact cells (absolute coords)."""
    atom = Subunit.of_type(troop_type, shape, 4, (10, 20))
    amap = _oriented_abs_map(atom)
    front = {ab for ab, orig in amap.items() if orig[0] == 0}
    assert front, f"{troop_type}/{shape}: no front-rank contact cells resolved"
    return atom, front


def _cap(troop_type):
    return C.support_ranks_for(troop_type)


def _pool(troop_type, shape):
    """(full engaged troops, the share carried by ranks past the cap, troops removed to measure it)."""
    atom, front = _force(troop_type, shape)
    full = _pair_engaged_troops(atom, front)
    removed = 0.0
    for pid in list(atom.cell_troops):
        if pid[0] > _cap(troop_type):           # depth behind contact rank 0 == orig row
            removed += atom.cell_troops[pid]
            atom.cell_troops[pid] = 0.0
    return full, full - _pair_engaged_troops(atom, front), removed


@pytest.fixture
def capped(monkeypatch):
    """The cap ON. Read at call time by config.support_weight, so no module reload."""
    monkeypatch.setattr(C, 'MB_SUPPORT_RANK_CAP', True)


@pytest.fixture
def uncapped(monkeypatch):
    monkeypatch.setattr(C, 'MB_SUPPORT_RANK_CAP', False)


# ── the shipped default ───────────────────────────────────────────────────────────────────────────

def test_shipped_default_is_off_and_is_todays_stack_exactly():
    if 'MB_SUPPORT_RANK_CAP' not in os.environ:
        assert C.MB_SUPPORT_RANK_CAP is False, "the cap ships OFF until magnitudes are recalibrated"
    if C.MB_SUPPORT_RANK_CAP:
        pytest.skip("ambient MB_SUPPORT_RANK_CAP=1 — the shipped-default arm cannot be observed here")
    for tt in _TYPES + (None, 'no_such_type'):
        for d in range(1, 12):
            assert C.support_weight(d, tt) == C.SUPPORT_WEIGHTS.get(d, C.SUPPORT_WEIGHT_FLOOR), (tt, d)
    checked = 0
    for tt in _TYPES:
        for shape in _SHAPES:
            full, beyond, _ = _pool(tt, shape)
            assert full == _UNCAPPED_FULL[shape], (tt, shape, repr(full))
            assert beyond == _UNCAPPED_BEYOND[(tt, shape)], (tt, shape, repr(beyond))
            checked += 1
    assert checked == 8


# ── the falsifier ─────────────────────────────────────────────────────────────────────────────────

def test_equal_forces_have_equal_troops_and_differ_only_in_depth():
    for tt in _TYPES:
        line, _ = _force(tt, 'Line')
        col, _ = _force(tt, 'Column')
        assert line.cur_troops == col.cur_troops, tt
        assert len({p[0] for p in line.cell_troops}) == 5
        assert len({p[0] for p in col.cell_troops}) == 7


def test_control_deep_and_shallow_differ_beyond_the_cap(uncapped):
    """RED premise: uncapped, the ranks past the weapon DO add pool, and depth alone decides how much."""
    differ = 0
    for tt in _TYPES:
        line = _pool(tt, 'Line')[1]
        col = _pool(tt, 'Column')[1]
        assert line > 0.0 and col > 0.0, f"{tt}: uncapped stack added nothing past the cap"
        if abs(col - line) > 1e-6:
            differ += 1
    # infantry (cap 1) ties up to float rounding: 7 files x (0.7+0.5+0.3) == 5 files x (0.7+0.5+0.3x3)
    assert differ == 3, f"{differ} troop types differ beyond the cap uncapped, expected 3"


def test_capped_ranks_past_the_cap_add_nothing_to_the_pool(capped):
    """GREEN with the cap ON. Planted: remove every rank past the weapon's reach; the pool is unchanged."""
    checked = 0
    for tt in _TYPES:
        for shape in _SHAPES:
            _, beyond, removed = _pool(tt, shape)
            assert removed > 0, f"{tt}/{shape}: nothing past cap {_cap(tt)} to remove — vacuous"
            assert beyond == 0.0, f"{tt}/{shape}: ranks past cap {_cap(tt)} still add {beyond} to the pool"
            checked += 1
    assert checked == len(_TYPES) * len(_SHAPES)


def test_capped_deep_and_shallow_no_longer_differ_beyond_the_cap(capped):
    for tt in _TYPES:
        assert _pool(tt, 'Column')[1] == _pool(tt, 'Line')[1] == 0.0, tt


def test_capped_ranks_within_the_cap_still_count(capped):
    for tt in _TYPES:
        cap = _cap(tt)
        assert cap >= 1
        for d in range(1, cap + 1):
            assert C.support_weight(d, tt) == C.SUPPORT_WEIGHTS.get(d, C.SUPPORT_WEIGHT_FLOOR), (tt, d)
        assert C.support_weight(cap + 1, tt) == 0.0, tt


def test_table_follows_the_weapon_classes():
    """P-DEC-1 weapon classes: non-pole 1 < pole/lance 2 < pike 3; unmapped = non-pole."""
    assert _cap('infantry') < _cap('heavy_infantry') < _cap('pike')
    assert _cap('heavy_infantry') == _cap('cavalry')
    assert _cap('no_such_type') == _cap('infantry') == 1
    # derived from the reach map, so EVERY mapped type is covered and a reach edit moves its rank
    from systems.mass_battle.sim.troop_types.registry import TROOP_TYPE_REACH
    expect = {0.1: 1, 0.2: 2, 0.3: 3}
    assert len(TROOP_TYPE_REACH) == 12
    assert {t: _cap(t) for t in TROOP_TYPE_REACH} == {t: expect[r] for t, r in TROOP_TYPE_REACH.items()}


# ── what the cap does to play (measured, Python 3.11.17) ─────────────────────────────────────────

def _standing(ta, tb, n=12):
    import random
    ha = hb = 0.0
    for s in range(n):
        random.seed(500 + s)
        a = build_unit('Line', 3, 'A', 'A', 9, troop_type=ta)
        b = build_unit('Line', 3, 'B', 'B', 9, troop_type=tb)
        h0a, h0b = a.hp, b.hp
        _orch.run_battle(a, b, max_turns=18)
        ha += a.hp / h0a; hb += b.hp / h0b
    return round(ha / n, 4), round(hb / n, 4)


@pytest.mark.slow
def test_capped_pike_out_retains_heavy_after_repelling_a_charge(field_path, monkeypatch):
    """Both pike (0.3) and heavy (0.2) clear the lance (0.2), so the recoil gate treats them alike; with
    the cap ON the melee after the repel separates them by the pike's third supported rank. Measured over
    test_reach_weapon_class's 16-seed braced-vs-charge fixture: capped pike 0.9774 > heavy 0.9665 > levy
    0.9225; uncapped pike == heavy == 0.958 (levy 0.9188).
    Re-measured at MB-04: the fixture's charger carries the 'charge' keyword, which now drives the
    aggressive stance (hierarchy.units.ROLE_INSTRUCTION_PRIMITIVES). With MB_ROLE_INSTRUCTIONS=0 the
    MB-07 readings return exactly (capped 0.9805/0.9714/0.9275, uncapped 0.9663, levy 0.9244); the
    ordering this test exists for holds under both."""
    monkeypatch.setattr(C, 'MB_SUPPORT_RANK_CAP', False)
    pike0, heavy0 = _charge_vs_brace('pike'), _charge_vs_brace('heavy_infantry')
    assert math.isclose(pike0, heavy0, abs_tol=1e-6)
    assert pike0 == pytest.approx(0.958, abs=1e-4)
    monkeypatch.setattr(C, 'MB_SUPPORT_RANK_CAP', True)
    pike, heavy, levy = (_charge_vs_brace(t) for t in ('pike', 'heavy_infantry', 'levy'))
    assert pike > heavy > levy, (pike, heavy, levy)
    assert (pike, heavy, levy) == pytest.approx((0.9774, 0.9665, 0.9225), abs=1e-4)


@pytest.mark.slow
def test_capped_pike_outfights_levy_in_standing_melee(field_path, monkeypatch):
    """With the cap ON the pike side (3 ranks) out-retains the levy side (1 rank) on either side of the
    field: pike-vs-levy (0.9646, 0.9421), levy-vs-pike (0.9296, 0.9746), levy-vs-levy (0.963, 0.9634).
    Uncapped all three read (0.9273, 0.9457): the reach VALUE alone does not change standing melee."""
    monkeypatch.setattr(C, 'MB_SUPPORT_RANK_CAP', False)
    assert _standing('pike', 'levy') == _standing('levy', 'levy') == _standing('levy', 'pike')
    monkeypatch.setattr(C, 'MB_SUPPORT_RANK_CAP', True)
    pl, lp, ll = _standing('pike', 'levy'), _standing('levy', 'pike'), _standing('levy', 'levy')
    assert pl[0] > pl[1] and lp[1] > lp[0], (pl, lp)
    assert (pl, lp, ll) == ((0.9646, 0.9421), (0.9296, 0.9746), (0.963, 0.9634))
