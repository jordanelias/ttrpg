"""B17.01's ONE SCALE (REM-32's `troops_per_weight` fixture is gone), observed where it is applied: `modules/mass_battle/massbattle.py`
`resolve_field` sizes a HEADCOUNT side by `under_arms_cap(weight)`, applies it to BOTH headcount sides and to fed troops
(`troops_a`/`troops_b`, which stand in the weight's place), and gives a side with an order of battle its own headcounts and the
headcount side facing one the same `under_arms_cap` (`_oob_unit`).

The battle itself is replaced by a recorder (`_run_and_grade`): this file reads the units the scale produced, and nothing is
resolved."""
from __future__ import annotations

import importlib
from types import SimpleNamespace as NS

from ..queries.inputs import MassBattleInput
from ._field_outcomes import SCALE


def _mb():
    """`engine/` names no `modules/` import at module level (`tests/valoria/test_engine_does_not_import_systems.py`
    walks `engine/season/tests/` too and imports every module it finds): the module is loaded on first use."""
    return importlib.import_module("modules.mass_battle.massbattle")


def _recruit():
    return importlib.import_module("modules.mass_battle.troop_types.recruitment")


def under_arms_cap(weight):
    return _recruit().under_arms_cap(weight)


def _field(**kw):
    base = dict(weights=((10.0, 5.0), (6.0,)), territory=None, fort_level=0.0, stances=(0.0, 0.0),
                walls_dr=None, origin=None, loyalties=(0.0, 0.0), loyalty_gain=0, geography=None, condition_scale=SCALE)
    base.update(kw)
    return MassBattleInput(**base)


def _units(monkeypatch, inp, **kw):
    """The two Armies `resolve_field` built, with the battle, the terrain and the crossing stubbed out."""
    seen = {}
    monkeypatch.setattr(_mb(), "river_crossed", lambda *a, **k: False)
    monkeypatch.setattr(_mb(), "terrain_row_for_territory", lambda *a, **k: None)
    monkeypatch.setattr(_mb(), "_run_and_grade", lambda a, b, *r, **k: seen.update(a=a, b=b, k=k) or NS())
    _mb().resolve_field(inp, None, **kw)
    return seen["a"], seen["b"], seen["k"]


def test_the_cap_sizes_both_headcount_sides(monkeypatch):
    a, b, _ = _units(monkeypatch, _field(units="side"))
    assert (a.total_troops(), b.total_troops()) == (float(under_arms_cap(15.0)), float(under_arms_cap(6.0)))
    assert (a.total_troops(), b.total_troops()) == (15000.0, 6000.0)     # 15 * 1,000 and 6 * 1,000 (B17.16: a weight is 1,000 troops)
    assert (a.faction, b.faction) == ("A", "B")                          # the engine's deployment convention, as an army's


def test_the_cap_applies_after_the_provisioning_bound(monkeypatch):
    """Fed troops (`troops_a`) stand in the weight's place and are then capped: the bound is in weight units."""
    a, b, _ = _units(monkeypatch, _field(units="side"), troops_a=4.0)
    assert (a.total_troops(), b.total_troops()) == (float(under_arms_cap(4.0)), 6000.0)
    a, _, _ = _units(monkeypatch, _field(units="side"), troops_a=0.0)
    assert a.total_troops() == 1.0                                       # the crash floor still applies


def test_a_person_side_is_the_same_cap_person_by_person(monkeypatch):
    """The `person` arm sizes each person by `under_arms_cap` of his own weight, so the side's total is the side arm's (B17.16: a
    side is at least three units, `massbattle._cut`: two persons make three units, the larger person's 10,000 cut in two of 5,000, and
    one person of 6,000 makes three of 2,000)."""
    a, b, _ = _units(monkeypatch, _field(units="person", members=(("a0", "a1"), ("b0",))))
    assert [s.troops for s in a.units] == [5000.0, 5000.0, 5000.0] and [s.troops for s in b.units] == [2000.0, 2000.0, 2000.0]
    assert sum(s.troops for s in a.units) == under_arms_cap(10.0) + under_arms_cap(5.0) and sum(s.troops for s in b.units) == under_arms_cap(6.0)


def test_a_side_with_an_order_of_battle_and_the_headcount_side_facing_it_are_sized_by_the_same_owner(monkeypatch):
    """With one side armied the whole field is sized by `_oob_unit`: the armied side by its own headcounts, the other by
    `under_arms_cap(weight)`, the cap the headcount path now takes too; `_weighted_unit` is not reached."""
    called = []
    monkeypatch.setattr(_mb(), "_weighted_unit", lambda *a, **k: called.append((a, k)) or (_ for _ in ()).throw(
        AssertionError("the headcount path ran on an armied field")))
    sized = []

    def spy(oob, weight, side, morale_start):
        sized.append((side, oob, weight))
        size = float(under_arms_cap(weight)) if oob is None else 99.0
        return NS(total_troops=lambda: size, units=[NS(_start_troops=size)])     # `_refusal` (B17.04) reads each Army's units

    monkeypatch.setattr(_mb(), "_oob_unit", spy)
    inp = _field(orders_of_battle=(object(), None))
    a, b, kw = _units(monkeypatch, inp)
    assert not called
    assert [(s, o is None, w) for s, o, w in sized] == [("A", False, 15.0), ("B", True, 6.0)]   # weights unscaled
    assert b.total_troops() == float(under_arms_cap(6.0)), "the headcount side facing an army is under_arms_cap's"
