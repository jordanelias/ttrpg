"""REM-32's scale, observed where it is applied (the Phase 1 close of B10-10): `modules/mass_battle/massbattle.py`
`resolve_field` sizes a HEADCOUNT side by `weight * troops_per_weight`, applies the scale to BOTH headcount sides and
to fed troops (`troops_a`/`troops_b`, which stand in the weight's place), and does NOT apply it to a side with an
order of battle or to the headcount side facing one (that side is sized by `under_arms_cap`).

Until now `troops_per_weight` was exercised only through `test_march.py`'s real fold, which cannot say which side
the scale reached. The battle itself is replaced by a recorder (`_run_and_grade`): this file reads the units the
scale produced, and nothing is resolved."""
from __future__ import annotations

from types import SimpleNamespace as NS

from modules.mass_battle import massbattle as MB
from modules.mass_battle.troop_types.recruitment import under_arms_cap

from ..queries.inputs import MassBattleInput


def _field(**kw):
    base = dict(weights=((10.0, 5.0), (6.0,)), territory=None, fort_level=0.0, stances=(0.0, 0.0),
                walls_dr=None, origin=None, loyalties=(0.0, 0.0), loyalty_gain=0, geography=None)
    base.update(kw)
    return MassBattleInput(**base)


def _units(monkeypatch, inp, **kw):
    """The two Units `resolve_field` built, with the battle, the terrain and the crossing stubbed out."""
    seen = {}
    monkeypatch.setattr(MB, "river_crossed", lambda *a, **k: False)
    monkeypatch.setattr(MB, "terrain_row_for_territory", lambda *a, **k: None)
    monkeypatch.setattr(MB, "_run_and_grade", lambda a, b, *r, **k: seen.update(a=a, b=b, k=k) or NS())
    MB.resolve_field(inp, None, **kw)
    return seen["a"], seen["b"], seen["k"]


def test_the_scale_sizes_both_headcount_sides(monkeypatch):
    a, b, _ = _units(monkeypatch, _field(troops_per_weight=3))
    assert (a.total_troops(), b.total_troops()) == (45.0, 18.0)          # 15 * 3 and 6 * 3
    a1, b1, _ = _units(monkeypatch, _field(troops_per_weight=1))
    assert (a1.total_troops(), b1.total_troops()) == (15.0, 6.0)         # the identity: the weight sum, as before


def test_the_scale_applies_after_the_provisioning_bound(monkeypatch):
    """Fed troops (`troops_a`) stand in the weight's place and are then scaled: the bound is in weight units."""
    a, b, _ = _units(monkeypatch, _field(troops_per_weight=3), troops_a=4.0)
    assert (a.total_troops(), b.total_troops()) == (12.0, 18.0)
    a, _, _ = _units(monkeypatch, _field(troops_per_weight=3), troops_a=0.0)
    assert a.total_troops() == 1.0                                       # the crash floor still applies


def test_a_side_with_an_order_of_battle_and_the_headcount_side_facing_it_are_not_scaled(monkeypatch):
    """With one side armied the whole field is sized by `_oob_unit`: the armied side by its own headcounts, the other by
    `under_arms_cap(weight)`; `_weighted_unit` is not reached, so the scale touches neither (D5 of the Phase 1 close:
    the knob reaches only fields where NEITHER side holds an order of battle)."""
    called = []
    monkeypatch.setattr(MB, "_weighted_unit", lambda *a, **k: called.append((a, k)) or (_ for _ in ()).throw(
        AssertionError("the headcount path ran on an armied field")))
    sized = []

    def spy(oob, weight, side, morale_start):
        sized.append((side, oob, weight))
        return NS(total_troops=lambda: float(under_arms_cap(weight)) if oob is None else 99.0)

    monkeypatch.setattr(MB, "_oob_unit", spy)
    inp = _field(troops_per_weight=3, orders_of_battle=(object(), None))
    a, b, kw = _units(monkeypatch, inp)
    assert not called and kw.get("by_troops") is True
    assert [(s, o is None, w) for s, o, w in sized] == [("A", False, 15.0), ("B", True, 6.0)]   # weights unscaled
    assert b.total_troops() == float(under_arms_cap(6.0)), "the headcount side facing an army is under_arms_cap's"
