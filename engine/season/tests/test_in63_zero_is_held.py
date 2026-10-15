"""IN-63 (`workplans/valoria_master_workplan_v9_part5.md`, ED-IN-0293 (2)) -- A ZERO IS A HELD
POSITION: `conviction_map` keeps an explicit 0 (a considered rejection, the bottom of
`affiliation_roster`'s 0-5 scale) and every reader of `Person.conviction` counts a position HELD only
above 0.

THE PLAN'S FALSIFIER, each an executed test: a hand-built `{solmund_orthodoxy: 5, einhir_restoration:
0}` (an incompatible pair, the 5 held and the 0 rejected)
  * reads confliction 0 (control: the same pair at 1 reads 1);
  * takes no scar on `einhir_restoration` from an act violating it (control: held at 1 it is scarred);
  * is not folded into `einhir_restoration` by a crisis on `solmund_orthodoxy`, person-side and
    through the real fold (control: held at 1 it IS folded into);
  * `-1` and `6` still refuse; a bool and a float still refuse.
The MUTATION (count 0 as held in `conviction_after_crisis`) turns the crisis tests red; it was run and
reverted when this file was written, and the tests below assert the facts it would break.
The hash-EQUAL exit held on IN-63's base, where no affiliation was authored; v9 IN-64 authored them.
"""
from __future__ import annotations

import pytest

from engine.season.data import affiliations as A
from engine.season.data.matrix import Step
from engine.season.data.rosters import AFFILIATIONS
from engine.season.epistemic import observers_for
from engine.season.gaps import Unspecified
from engine.season.harness import probes as P
from engine.season.queries.person_q import (SCAR_CRISIS_AT, broken_by, confliction,
                                            conviction_after_crisis, elements_violated_by,
                                            violated_affiliations)
from engine.season.state.carriers import Person, Tenure
from engine.substrate.descriptors import AFFILIATION_CEILING, AFFILIATION_FLOOR

from ._scar_helpers import compatible_pairs, fight
from ._scar_helpers import rebound as _rebound

HELD, REJECTED = "solmund_orthodoxy", "einhir_restoration"


def test_in63_the_pair_is_rostered_and_incompatible():
    """The falsifier's two names are real: rostered, and a strained pair, so the zero is what
    separates the readings below and not an accident of the pair."""
    assert {HELD, REJECTED} <= AFFILIATIONS
    assert frozenset((HELD, REJECTED)) in A.INCOMPATIBLE


# ------------------------------------------------------------------------------ the loader

def test_in63_conviction_map_keeps_an_explicit_zero_and_still_refuses_outside_the_spine():
    a = sorted(AFFILIATIONS)[0]
    assert AFFILIATION_FLOOR == 0 and AFFILIATION_CEILING == 5
    assert A.conviction_map({a: 0}) == {a: 0}
    assert A.conviction_map({HELD: 5, REJECTED: 0}) == {REJECTED: 0, HELD: 5}
    assert list(A.conviction_map({HELD: 5, REJECTED: 0})) == sorted([HELD, REJECTED]), "keys sorted"
    assert A.conviction_map(None) == {} and A.conviction_map({}) == {}
    refused = 0
    for bad in (-1, AFFILIATION_CEILING + 1, 6, 2.5, 0.0, True, False, "0"):
        with pytest.raises(Unspecified):
            A.conviction_map({a: bad})
        refused += 1
    assert refused == 8
    with pytest.raises(Unspecified):
        A.conviction_map({"threadwork": 0})        # a zero does not excuse an unrostered name


# The EXIT's precondition test (no row carried `affiliations:` on IN-63's base, so keeping a zero
# moved no stored value; two-season hash `2eedf7b0...` before and after) was retired at v9 IN-64,
# which authors every cast row's affiliations and stores the opponents' zeros
# (`test_in64_cast_integration.py`). Its subject died with that base.


# ------------------------------------------------------------------------------ confliction

def test_in63_a_rejected_pole_strains_nothing():
    zero = Person("p_zero", conviction=A.conviction_map({HELD: 5, REJECTED: 0}))
    assert zero.conviction == {REJECTED: 0, HELD: 5}, "the zero must be stored for this to test it"
    assert confliction(zero) == 0
    control = Person("p_one", conviction=A.conviction_map({HELD: 5, REJECTED: 1}))
    assert confliction(control) == 1, "control: the same pair held at 1 strains at the weaker holding"
    both_zero = Person("p_none", conviction=A.conviction_map({HELD: 0, REJECTED: 0}))
    assert confliction(both_zero) == 0


# ------------------------------------------------------------------------------ the scar

def _violating_verb() -> str:
    """A verb the SHIPPED engagement table violates every affiliation on (the shared column's first
    negative cell that `elements_violated_by` reads as violating all of them)."""
    for verb, val in sorted(A.ENGAGEMENT[A.SHARED_COLUMN].items()):
        if val < 0 and elements_violated_by(verb)[1] == AFFILIATIONS:
            return verb
    raise AssertionError("no shipped verb violates every affiliation; the scar arm has nothing to read")


def test_in63_an_act_violating_a_rejected_pole_scars_nothing_on_it():
    verb = _violating_verb()
    violated = elements_violated_by(verb)
    assert {HELD, REJECTED} <= violated[1]
    zero = Person("p_zero", conviction=A.conviction_map({HELD: 5, REJECTED: 0}))
    assert broken_by(zero, violated) == (HELD,)
    assert violated_affiliations(zero, verb) == (HELD,)
    control = Person("p_one", conviction=A.conviction_map({HELD: 5, REJECTED: 1}))
    assert broken_by(control, violated) == (REJECTED, HELD), "control: held at 1, it is broken too"


# ------------------------------------------------------------------------------ the crisis

def _crisis(held: dict, scar: dict) -> dict:
    return conviction_after_crisis(Person("p_crisis", conviction=A.conviction_map(held), scar=dict(scar)))


def test_in63_a_crisis_on_the_held_pole_does_not_fold_into_the_rejected_one():
    both = {HELD: SCAR_CRISIS_AT}
    after = _crisis({HELD: 5, REJECTED: 0}, both)
    assert after.get(REJECTED, 0) == 0, f"the crisis folded into a rejected pole: {after}"
    assert HELD not in after, "the held pole in crisis drops"
    assert after == {REJECTED: 0}, "a rejection other than the crisis pole is left as it was"
    # control: the same pair with the heir held at 1 DOES fold (so the 0 is what stopped it)
    assert _crisis({HELD: 5, REJECTED: 1}, both) == {REJECTED: AFFILIATION_CEILING}
    # a zero is no heir however the scar sits: scarred to the threshold itself, it is not in crisis
    at_threshold = {HELD: SCAR_CRISIS_AT, REJECTED: SCAR_CRISIS_AT}
    assert _crisis({HELD: 5, REJECTED: 0}, at_threshold) == {REJECTED: 0}
    assert _crisis({HELD: 0, REJECTED: 0}, at_threshold) == {HELD: 0, REJECTED: 0}, \
        "nothing held, nothing in crisis: the vector is returned as it stands"
    unchanged = Person("p_rej", conviction=A.conviction_map({HELD: 0}), scar={HELD: SCAR_CRISIS_AT})
    assert conviction_after_crisis(unchanged) is unchanged.conviction


def test_in63_a_zero_is_not_something_else_held_for_the_restabilise_branch():
    """Destroyed means NOTHING ELSE IS HELD above 0: a compatible co-holding at 0 does not make the
    crisis a restabilise (which would leave the vector alone) -- the crisis pole drops."""
    pairs = compatible_pairs()
    assert pairs, "every rostered pair is incompatible; no compatible zero to plant"
    a, z = pairs[0]
    assert _crisis({a: 3, z: 0}, {a: SCAR_CRISIS_AT}) == {z: 0}
    assert _crisis({a: 3, z: 2}, {a: SCAR_CRISIS_AT}) == {z: 2, a: 3}, \
        "control: held at 2 it is restabilise (not built), the vector unchanged"


def _world(holdings: dict, count: int):
    """H13's planted world: one `knot` ties `p_low` to `p_high`; no pursuits; `holdings` on every
    person, each held affiliation at scar `count`."""
    w = P.tiny_world()
    for p in w.persons.values():
        p.pursuits = {}
        p.conviction = A.conviction_map(holdings)
        p.scar = {a: count for a, v in sorted(p.conviction.items()) if v > 0}
    w.add_tenure(Tenure("t_in63_knot", "p_low", "p_high", "knot", since=0))
    w.fixtures = w.fixtures.sweep("fan_out_mode", "presence_only")
    w.step = Step.RESOLVE
    return w


def _observers(w, events) -> set:
    w.discard_caches()
    return {pid for e in events for pid, _ch in observers_for(w, e, "presence_only", list(w.persons))}


def test_in63_through_the_real_fold_a_rejected_pole_takes_no_scar_and_no_fold(monkeypatch):
    monkeypatch.setattr(A, "ENGAGEMENT", _rebound(**{A.SHARED_COLUMN: {"fight": -0.3}}))

    w = _world({HELD: 5, REJECTED: 0}, SCAR_CRISIS_AT - 1)
    seen = _observers(w, fight(w, "in63_fight"))
    unseen = set(w.persons) - seen
    assert seen and unseen, (seen, unseen)
    checked = 0
    for pid in seen:
        p = w.persons[pid]
        assert REJECTED not in p.scar, (pid, p.scar)
        assert p.scar.get(HELD) == SCAR_CRISIS_AT, (pid, p.scar)
        assert p.conviction == {REJECTED: 0}, (pid, p.conviction)      # HELD dropped, 0 stays 0
        checked += 1
    for pid in unseen:
        assert w.persons[pid].conviction == {REJECTED: 0, HELD: 5}, pid
        assert REJECTED not in w.persons[pid].scar, pid
        checked += 1
    assert checked == len(w.persons)

    # CONTROL: the same world with the pole held at 1 -- scarred, and the crisis folds into it.
    c = _world({HELD: 5, REJECTED: 1}, SCAR_CRISIS_AT - 1)
    cseen = _observers(c, fight(c, "in63_fight"))
    assert cseen
    for pid in cseen:
        p = c.persons[pid]
        assert p.scar.get(REJECTED) == SCAR_CRISIS_AT, (pid, p.scar)
        assert p.conviction == {REJECTED: AFFILIATION_CEILING}, (pid, p.conviction)
