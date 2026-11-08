"""CP-T04-05: graded walls -- `field_input` hands the engine `int(field_walls_dr * fort_level)` (floor), `None` (shipped)
staying `None`, so a worn garrison's walls armour the defender less. This file is the item's own; nothing here is a
shared pin.

THE FIELD IS HAND-BUILT, NOT NATURAL. One season of the shipped realm fights almost no field (seed 0: unopposed 3;
seed 1: unopposed 2; seed 2: lost 1), so the falsifier runs on a hand fold of `set_s_014` (the Crown's two marchers,
made cohorts of `WEIGHT`) on `set_s_036` (the Church's six), the weight -> troops scale at `SCALE` (a value of THIS
TEST, as `test_cp_t04_01_person_subunits.py`'s). The record is `field_input`'s own, so the line under test is the one
that builds `walls_dr`; two fields of it are this test's, as `tests/valoria/test_mass_battle_terrain.py` does: the place
(`territory='T3'`, an OPEN_FLAT polygon, so fort 0 is a plain field and a fort above 0 is WALLS) and no origin (no river
crossing to confound the steps).

The cases: the falsifier (defender win share falls as the garrison's condition steps 1.0 -> 0.67 -> 0.33 -> 0 under
paired seeds, `field_walls_dr = 3`), its planted failure (a flat `walls_dr` reaches the engine: the same predicate
reddens), the control (shipped `None` is flat across the same steps and `3` at full condition is the same field as
`None`, through `field_input` and through the real driver), and the floor (`int`, never `round`)."""
from __future__ import annotations

import importlib
import random
from dataclasses import replace
from functools import lru_cache

import pytest

from engine.season.harness.populated import build_realm
from engine.season.queries import world_q
from engine.season.seam.wrappers import mass_battle as wrapper
from engine.season.tests.test_march import _fold_one, _march_act

#: RE-PICKED by MB-07r (the depth support cap ON, `POOL_QUALITY_SCALE` 0.5 -> 0.8): at the old fold (weight 8, scale 100)
#: the defender's shares read {1.0: 0.54, 0.67: 0.465, 0.33: 0.42, 0.0: 0.42}, a 4.5-point second step under the +-7
#: band the entry names. At (10, 60) they read {1.0: 0.49, 0.67: 0.385, 0.33: 0.285, 0.0: 0.285}: base inside the 45-56 %
#: shape, both steps ~10 points, the 0.33 -> 0 plateau exact (`int(3 * 0.33)` is 0). The predicate and n are unchanged.
WEIGHT, SCALE, SEEDS = 10, 60, range(200)
MARCHERS = ("p_npc_033", "p_npc_035")
LEVELS = (1.0, 0.67, 0.33, 0.0)
TARGET, HOME = "set_s_036", "set_s_014"
NOISE = 0.07            # the entry's band: +-7 points at a 45 % share


def _mb():
    """`engine/` names no `modules/` import at module level; the module is loaded on first use."""
    return importlib.import_module("modules.mass_battle.massbattle")


def _world(walls_dr, level):
    w = build_realm(0)
    for pid in MARCHERS:
        w.persons[pid].weight = WEIGHT
    w.fixtures = w.fixtures.sweep("field_troops_per_weight", SCALE).sweep("field_walls_dr", walls_dr)
    full = w.fixtures.get("condition_scale")
    garrisons = [s for s in w.sites.values() if s.kind == "garrison" and s.rung == TARGET]
    assert garrisons, "fixture moved: set_s_036 holds no garrison Site"
    for s in garrisons:
        s.condition = level * full
    assert world_q.mustered(w, HOME, "fac_valorsmark") == list(MARCHERS), "fixture moved: re-read it"
    return w


def _record(w):
    att = world_q.mustered(w, HOME, "fac_valorsmark")
    dfn = world_q.mustered(w, TARGET, "fac_church_of_solmund")
    return replace(wrapper.field_input(w, att, dfn, TARGET), origin=None, territory="T3")


def _share(walls_dr, level, builder=None):
    """The defender's win share over the paired seeds, and the `walls_dr` the record carried."""
    w = _world(walls_dr, level)
    inp = _record(w) if builder is None else builder(w)
    wins = sum(not _mb().resolve_field(inp, random.Random(s))["attacker_wins"] for s in SEEDS)
    return wins / len(SEEDS), inp.walls_dr


def _shares(walls_dr, builder=None):
    return {lv: _share(walls_dr, lv, builder) for lv in LEVELS}


@lru_cache(maxsize=None)
def _graded():
    return _shares(3)


@lru_cache(maxsize=None)
def _flat():
    return _shares(None)


def _falls(shares):
    """THE FALSIFIER'S PREDICATE (one function, so the planted failure is judged by the very check the real arm is):
    each step of armour lost costs the defender at least the noise band; 0.33 -> 0 loses no armour (the floor) and the
    field is the same open field, so it must not fall again."""
    s = {lv: shares[lv][0] for lv in LEVELS}
    return (s[1.0] - s[0.67] >= NOISE and s[0.67] - s[0.33] >= NOISE and s[0.33] == s[0.0])


def test_shipped_arm_is_none():
    assert build_realm(0).fixtures.get("field_walls_dr") is None


def test_falsifier_defender_win_share_falls_as_the_garrison_wears_under_paired_seeds():
    shares = _graded()
    assert [shares[lv][1] for lv in LEVELS] == [3, 2, 0, 0], shares        # the record carried the graded DR
    assert _falls(shares), {lv: shares[lv][0] for lv in LEVELS}
    s = [shares[lv][0] for lv in LEVELS]
    assert s[0] > s[1] > s[2], s
    # the base is a contest, not a rout either way (the entry's 45 % +- 7 shape): the steps are not a ceiling or a floor
    assert 0.2 < s[3] < s[0] < 0.8, s


def test_planted_failure_a_flat_walls_dr_reaching_the_engine_reddens_the_falsifier():
    """MUTATION: the record carries the fixture's 3 whatever the garrison's condition (the line this item replaces,
    one level up). The falsifier's predicate must then fail on the same fold."""
    def flat(w):
        return replace(_record(w), walls_dr=w.fixtures.get("field_walls_dr"))

    mutant = _shares(3, builder=flat)
    assert not _falls(mutant), {lv: mutant[lv][0] for lv in LEVELS}
    with pytest.raises(AssertionError):
        assert _falls(mutant)


def test_the_grade_is_floored_not_banker_rounded():
    """`round(3 * 0.5)` is 2 and `round(1 * 0.5)` is 0; the floor is 1 and 0. The wrapper's line is checked at 0.5
    against both, so a `round` there would be seen."""
    w = _world(3, 0.5)
    assert _record(w).walls_dr == 1 and round(3 * 0.5) == 2
    w = _world(1, 0.5)
    assert _record(w).walls_dr == 0 and int(1 * 0.5) == 0


def test_control_shipped_none_hands_none_and_is_flat_across_the_steps_that_stay_walled():
    shares = _flat()
    assert all(shares[lv][1] is None for lv in LEVELS), shares
    s = {lv: shares[lv][0] for lv in LEVELS}
    assert s[1.0] == s[0.67] == s[0.33], s                 # every fort_level above 0 is the same flat WALLS row
    assert not _falls(shares)                               # the falsifier's predicate sees no grading on `None`
    assert s[0.0] < s[1.0]                                  # ... and fort 0 is no wall, as today


def test_control_three_at_full_condition_is_the_shipped_field():
    """A.9's number times 1.0: the graded arm and the shipped arm are one field at full condition, so the flip moves
    only a worn garrison. Same record, same share, same result on every seed."""
    graded, flat = _graded()[1.0], _flat()[1.0]
    assert graded[0] == flat[0]
    assert graded[1] == 3 and flat[1] is None
    w3, wn = _world(3, 1.0), _world(None, 1.0)
    for s in SEEDS[:20]:
        assert (_mb().resolve_field(_record(w3), random.Random(s))
                == _mb().resolve_field(_record(wn), random.Random(s)))


def test_control_through_the_real_driver_three_at_full_condition_is_hash_equal_to_none():
    """The same control through `march` -> ENCOUNTER -> `resolve` -> `field_input` (the whole path, no hand record)."""
    hashes = []
    for walls_dr in (None, 3):
        w = build_realm(0)
        for pid in MARCHERS:
            w.persons[pid].weight = 2
        w.fixtures = w.fixtures.sweep("field_troops_per_weight", SCALE).sweep("field_walls_dr", walls_dr)
        events = _fold_one(w, _march_act(MARCHERS[0], TARGET, "off_spymaster"), contest_max_depth=2)
        assert any(e.kind.startswith("field.") for e in events), [e.kind for e in events]
        hashes.append(w.content_hash())
    assert hashes[0] == hashes[1]
