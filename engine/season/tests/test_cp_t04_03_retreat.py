"""CP-T04-03 (B10-12): retreat in good order. A standing order's `retreat_at` (`none`, `0.5`, `0.25`) becomes, per subunit,
an `own_strength:FRAC` Order whose action is the `retreat` stance; a side every one of whose subunits has retreated or
routed has CONCEDED (`hierarchy/units.py::unit_conceded`, the one predicate): `run_battle` stops for it as a rout stops it,
without rout's facing flip, and `_grade` never calls it the winner. No new band; the `MB_YIELD_*` yield is untouched.
This file is the item's own; nothing here is a shared pin.

THE FIELD is `test_cp_t04_02_marshal.py`'s (its helpers are reused, not re-invented): the Crown's two marchers against the
Church's six at `SCALE` 30 on an open field, the record `field_input`'s own, and the order a real `marshal` act folded
through the driver (`marshal` ships WITHHELD, so the act is hand-minted). Both sides name the role `Screen`, whose one
instruction is wired to no primitive, so the order changes the field by its `retreat_at` alone (the control below checks
that `Screen`/`none` is the field as it was).

FALSIFIER (the entry's): paired seeds (`random.Random(0..199)` in both arms), an attacker with `retreat_at 0.5` against an
equal defender loses fewer troops than with `none`, and is graded the winner in ZERO seeds where its retreat fired.
PLANTED FAILURES, each judged by the very predicate the real arm is: the order not read (`_retreat_orders` returns nothing)
and the order read but the battle not stopped (`run_battle`'s stop test blind to it) leave the loss where `none` has it;
`_grade` blind to a concession grades a retreating side that is ahead on size the winner.
HONEST LIMIT: on the natural fold no fired retreat is ever ahead on size (a retreat fires at <= half strength, and the
other side is then ahead), so `_grade`'s concession rule cannot be observed by a fold; it is observed on hand-set units
(`test_grade_*`). CONTROLS: no order, and `none` on both sides, are the field as it was, seed for seed."""
from __future__ import annotations

import random
from dataclasses import replace
from functools import lru_cache
from types import SimpleNamespace

import pytest

from engine.season.tests import test_cp_t04_02_marshal as M
from engine.season.tests.test_march import _fold_one

SEEDS, PERSON_SEEDS = range(200), range(100)
ROLE = "Screen"            # a role with no wired primitive: the order is its `retreat_at` and nothing else


def _mb():
    return M._mb()


def _bl():
    return M._mod("battle_loop")


def _units():
    return M._mod("hierarchy.units")


def _world(att="none", dfn=None):
    """`test_cp_t04_02_marshal._world` with each order's `retreat_at` carried: a real `marshal` act per side that is given
    one (`att`/`dfn` are `retreat_at` values or None for no order), folded through the driver."""
    w = M._world()
    w.tick = 3
    for retreat, actor, via, place, aid in ((att, M.KING, M.KING_SEAT, M.HOME, "rt_att"),
                                            (dfn, M.CARDINAL, M.CARDINAL_SEAT, M.TARGET, "rt_def")):
        if retreat is not None:
            kinds = [e.kind for e in _fold_one(w, M._marshal(actor, via, place, ROLE, retreat, aid))]
            assert "order.marshaled" in kinds, kinds
    return w


def _fold(inp, seeds):
    """`[(graded, attacker conceded, defender conceded)]` per seed. The concession is read at grading time, off the units
    the module fought, so the record's return is exactly the module's; `_grade` is wrapped, never changed."""
    mb, units = _mb(), _units()
    seen, orig = [], mb._grade

    def spy(unit_a, unit_b, by_troops=False):
        seen.append((units.unit_conceded(unit_a), units.unit_conceded(unit_b)))
        return orig(unit_a, unit_b, by_troops)

    mb._grade = spy
    try:
        out = []
        for s in seeds:
            g = mb.resolve_field(inp, random.Random(s))
            out.append((g, *seen[-1]))
        return out
    finally:
        mb._grade = orig


@lru_cache(maxsize=None)
def _arm(att, dfn=None, arm="side", n=len(SEEDS)):
    inp = replace(M._record(_world(att, dfn)), subunits=arm)
    return inp.orders, _fold(inp, range(n))


def _mean_loss(rows):
    return sum(1.0 - g["attacker_size_pct"] for g, *_ in rows) / len(rows)


def _fewer_losses(rows_retreat, rows_none, margin=0.01):
    """THE FALSIFIER'S FIRST PREDICATE (one function): the retreating attacker's mean loss share, over paired seeds, is
    lower than the same attacker's with `none` by more than `margin`."""
    return _mean_loss(rows_retreat) < _mean_loss(rows_none) - margin


def _fired_wins(rows):
    """THE FALSIFIER'S SECOND PREDICATE: (seeds where the attacker's retreat fired, of those graded a win)."""
    fired = [g for g, a_conceded, _ in rows if a_conceded]
    return len(fired), sum(g["attacker_wins"] for g in fired)


# --------------------------------------------------------------------------------------------------------------- falsifier

def test_falsifier_an_attacker_who_retreats_at_half_loses_fewer_troops_and_never_wins_a_fired_retreat():
    (o_none, none), (o_half, half) = _arm("none"), _arm("0.5")
    assert o_none[0].retreat_at == "none" and o_half[0].retreat_at == "0.5" and o_half[1] is None
    fired, fired_wins = _fired_wins(half)
    assert fired >= 20, fired                                     # the loop asserted: the retreat fired in a real share of seeds
    assert _fewer_losses(half, none), (_mean_loss(half), _mean_loss(none))
    assert fired_wins == 0, fired_wins                            # a win with a fired retreat is a grading defect
    # the saving is the retreat's, seed for seed: every seed where the two arms differ is a seed the retreat fired in, and
    # in each the retreating attacker ends with more of its troops (the orderly retreat stopped the fight for it)
    differ = [i for i, ((gh, *_), (gn, *_)) in enumerate(zip(half, none)) if gh != gn]
    assert len(differ) >= 20 and all(half[i][1] for i in differ)
    assert all(half[i][0]["attacker_size_pct"] > none[i][0]["attacker_size_pct"] for i in differ)
    # a fired retreat is the attacker's concession, never the rout it spares
    assert all(not half[i][0]["attacker_wins"] and half[i][0]["degree"] in ("Partial", "Failure") for i in differ)


def test_falsifier_on_the_person_arm_a_side_concedes_when_every_subunit_has_retreated_or_routed():
    none, half = _arm("none", arm="person", n=len(PERSON_SEEDS))[1], _arm("0.5", arm="person", n=len(PERSON_SEEDS))[1]
    fired, fired_wins = _fired_wins(half)
    assert fired >= 5, fired
    assert fired_wins == 0, fired_wins
    assert not _fired_wins(none)[0]
    assert _mean_loss(half) <= _mean_loss(none) + 1e-9           # (a smaller effect on six small subunits, but never a rise)


def test_a_defender_who_retreats_leaves_the_field_to_the_attacker():
    rows = _arm("none", "0.5")[1]
    d_fired = [g for g, _, d_conceded in rows if d_conceded]
    assert len(d_fired) >= 20
    assert all(g["attacker_wins"] for g in d_fired)                # the defender gave the field up; the attacker holds it
    assert not any(a for _, a, _ in rows)


def test_a_retreat_at_a_quarter_is_the_same_primitive_and_a_side_this_thin_has_routed_before_it():
    inp = replace(M._record(_world("0.25")), subunits="side")
    assert inp.orders[0].retreat_at == "0.25"
    (sub,) = _mb()._weighted_unit("a", 20, 5, M.SCALE, None, "0.25").subunits
    (order,) = sub.orders
    assert (order.trigger, order.behavior) == ("own_strength:0.25", {"stance": "retreat", "conceded": True})
    # on a single-subunit side the SUBUNIT_ROUT_FLOOR / morale rout comes first, so it fires in no seed (a limit, not a defect)
    assert _fired_wins(_arm("0.25")[1])[1] == 0


# ----------------------------------------------------------------------------------------------------- planted failures

def test_planted_failure_an_order_not_read_reddens_the_falsifier(monkeypatch):
    monkeypatch.setattr(_mb(), "_retreat_orders", lambda retreat_at: ())
    inp = replace(M._record(_world("0.5")), subunits="side")
    mutant = _fold(inp, SEEDS)
    assert not _fewer_losses(mutant, _arm("none")[1])
    assert _fired_wins(mutant)[0] == 0                              # (and nothing fired: the order is not there)
    with pytest.raises(AssertionError):
        assert _fewer_losses(mutant, _arm("none")[1])


def test_planted_failure_a_battle_that_does_not_stop_for_a_concession_reddens_the_falsifier(monkeypatch):
    """The order is read and the retreat fires (its stance is written), but `run_battle` goes on to the end, so the side
    loses what `none` loses: the stance alone saves nothing."""
    monkeypatch.setattr(_bl(), "unit_conceded", lambda unit: False)
    inp = replace(M._record(_world("0.5")), subunits="side")
    mutant = _fold(inp, SEEDS)
    assert not _fewer_losses(mutant, _arm("none")[1])


def _fake_unit(share, stance="balanced", routed=False):
    """A unit as `_grade` and `unit_conceded` read it: one subunit, `share` of its size left."""
    return SimpleNamespace(routed=routed, effective_size=10 * share, size_max=10, hp=100 * share, hp_max=100,
                           subunits=[SimpleNamespace(routed=routed, eff_stance=stance, conceded=stance == "retreat")])


def test_grade_a_conceded_attacker_ahead_on_size_is_not_the_winner_and_a_conceded_defender_gives_the_field():
    mb = _mb()
    ahead, behind = _fake_unit(0.8, "retreat"), _fake_unit(0.6)
    g = mb._grade(ahead, behind)
    assert not g["attacker_wins"] and g["degree"] == "Partial"       # ahead on size, but it gave the field up
    g = mb._grade(_fake_unit(0.8), _fake_unit(0.9))                  # the control: no concession, behind on size
    assert not g["attacker_wins"]
    g = mb._grade(_fake_unit(0.55), _fake_unit(0.9, "retreat"))      # behind on size, but the defender conceded
    assert g["attacker_wins"] and g["degree"] == "Success"
    g = mb._grade(_fake_unit(0.8, "retreat"), _fake_unit(0.9, "retreat"))   # both gave it up: nobody holds it
    assert not g["attacker_wins"]


def test_planted_failure_a_grade_blind_to_a_concession_grades_a_fired_retreat_a_win(monkeypatch):
    mb = _mb()
    ahead, behind = _fake_unit(0.8, "retreat"), _fake_unit(0.6)
    assert not mb._grade(ahead, behind)["attacker_wins"]
    monkeypatch.setattr(mb, "unit_conceded", lambda unit: False)
    assert mb._grade(ahead, behind)["attacker_wins"]                 # the grading defect the falsifier's second predicate names
    # ... and the second predicate sees it on a row shaped like a fold's
    assert _fired_wins([(mb._grade(ahead, behind), True, False)]) == (1, 1)


# ---------------------------------------------------------------------------------------- the stop, and no facing flip

def test_the_battle_stops_for_a_conceding_side_without_routing_it():
    mb, bl, units = _mb(), _bl(), _units()
    rngsource = M._mod("rngsource")
    stopped = checked = early = 0
    for s in range(60):
        a = mb._weighted_unit("side_a", 20, 5, M.SCALE, None, "0.5")
        b = mb._weighted_unit("side_b", 20, 5, M.SCALE)
        with rngsource.using(random.Random(s)):
            res = bl.run_battle(a, b, max_turns=18)
        checked += 1
        if units.unit_conceded(a) and not a.routed:      # (a side can retreat and rout in the same tick: that one is a rout)
            stopped += 1
            early += res["turns"] < 18                                  # ended before the 18-tick cap
            assert not any(x.routed for x in a.subunits)                # no rout, so no rout facing flip
            assert a.subunits[0].eff_stance == "retreat"
    assert checked == 60 and stopped >= 5 and early >= 1, (stopped, early)


def test_a_side_with_no_retreating_subunit_is_never_conceded_and_the_function_moved_by_name():
    mb, units = _mb(), _units()
    assert not units.unit_conceded(mb._weighted_unit("a", 20, 5, M.SCALE))
    assert not units.unit_conceded(SimpleNamespace(subunits=[SimpleNamespace(routed=True, conceded=False)]))  # routed is not conceded
    assert units.unit_conceded(SimpleNamespace(subunits=[SimpleNamespace(routed=True, conceded=False),
                                                         SimpleNamespace(routed=False, conceded=True)]))
    assert not units.unit_conceded(SimpleNamespace(subunits=[SimpleNamespace(routed=False, conceded=True),
                                                             SimpleNamespace(routed=False, conceded=False)]))
    # Keyed on the ORDER's mark, not the stance or `yielding`: a DG-2 fighting withdrawal (`yielding` + stance retreat,
    # no `conceded`) is not a concession, and an emergent `yielding` on a subunit whose `retreat_at` order fired does not
    # hide one. Real subunits, so the field's default and the order-settable set are observed too.
    wd = mb._weighted_unit("a", 20, 5, M.SCALE)
    for s_ in wd.subunits:
        s_.stance, s_.yielding = "retreat", True
    assert not units.unit_conceded(wd)
    for s_ in wd.subunits:
        s_.conceded = True
    assert units.unit_conceded(wd)                                      # conceded AND yielding: still a concession
    assert "conceded" in units._ORDER_SAFE_FIELDS
    assert M._mod("orchestration").run_battle is _bl().run_battle          # ED-1043: moved verbatim, the name re-exported


# ---------------------------------------------------------------------------------------------------------------- controls

def test_control_no_order_and_none_everywhere_are_the_field_as_it_was():
    mb = _mb()
    inp = M._record(_world(None, None))
    assert inp.orders is None
    ordered = replace(inp, orders=_arm("none", "none")[0])
    assert ordered.orders[0].retreat_at == ordered.orders[1].retreat_at == "none"
    for s in list(SEEDS)[:40]:
        assert mb.resolve_field(inp, random.Random(s)) == mb.resolve_field(ordered, random.Random(s))


def test_control_a_retreat_at_outside_the_closed_set_is_refused_and_none_is_no_order():
    mb = _mb()
    assert mb._retreat_orders(None) == mb._retreat_orders("none") == ()
    assert [o.trigger for o in mb._retreat_orders("0.5")] == ["own_strength:0.5"]
    with pytest.raises(ValueError):
        mb._retreat_orders("0.1")
    assert mb._weighted_unit("a", 20, 5, M.SCALE).subunits[0].orders == ()
