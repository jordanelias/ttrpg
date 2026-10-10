"""v9 IN-34 -- FORCE-BODIES: ageing and illness through the bodies motion (`H-206`, `H-207`).

#457 D2, answered [medium; Jordan to correct]: ageing and illness are in scope, a HAZARD READER only,
rates swept. What the position built, each asked of the real builder, the real MATTER barrier and the
real Queries:
  * ONE FIELD, `Person.born` (`state/carriers.py`), defaulting to `-age_at_build`; age is READ OFF THE
    CLOCK (`world_q.age_of`), never stored;
  * THE HAZARD AS ITS READER, `world_q.body_hazard` (ID-13: a Query over the field, never a stored
    value): `illness_rate + age_step * age`, capped at 1, none for a cohort;
  * ONE BODIES WRITE AT MATTER (`loop/matter.py`'s bodies pass): a keyed draw per living person, and a
    hit is `(Person, exists)` through `World.remove_person`, emitting `person.died` chained to that
    person's own prior emission.

THE FALSIFIERS, each with the failure it would show:
  * CONTROL: at the shipped rates (both `0`, each row's control arm) a realm whose every individual is
    made ancient loses nobody and MATTER emits exactly what it emits for the untouched realm -- a
    hazard that did not read the rates, or that floored above 0, would kill here. The SEASON-level
    control is `test_season_weather.py`'s three pinned hashes, re-recorded for the schema move this
    field causes (`H-206`'s cite: event kinds and counts over one and two seasons equal B-F's base);
  * THE VACANCY HALF THAT HOLDS: at each live `age_step` arm a seat-holder old enough to die certainly
    dies at MATTER, alone, and his seat is left with no live holder, through the one death cascade;
  * EXTREMES: at `illness_rate` 1 every individual dies and no cohort does, and the same seed gives the
    same deaths twice.
NOT HELD, MEASURED: *"a seat-holder's death by age raises vacancy claims for those in reach"* -- a
MATTER-emitted `person.died` reaches no ledger under the shipped fan-out (`H-206`'s cite). No xfail.
"""

from __future__ import annotations

import math

import pytest

from ..data.matrix import Step, WriteClass
from ..harness import populated as POP
from ..harness import probes as P
from ..harness import register as REG
from ..loop.driver import SeasonDriver, mint_token
from ..queries import world_q
from ..state.ids import ROOT

ROWS = {r["id"]: r for r in REG.load()["rows"] if r["id"] in ("H-206", "H-207")}
AGE_CONTROL = P.DEFAULT_FIXTURES.get("age_step")
ILL_CONTROL = P.DEFAULT_FIXTURES.get("illness_rate")
AGE_ARMS = [a for a in ROWS["H-206"]["sweep"] if a != AGE_CONTROL]
ILL_ARMS = [a for a in ROWS["H-207"]["sweep"] if a != ILL_CONTROL]


def _matter(w):
    """MATTER alone, through the real barrier and a real MATTER token (the `24f` tests' helper)."""
    d = SeasonDriver(w)
    w.step = Step.MATTER
    return d.matter(mint_token(w, WriteClass.MATTER), [])


def _individuals(w) -> list:
    return sorted(pid for pid, p in w.persons.items() if not p.is_cohort)


def _seats(w) -> list:
    """`(holder, office)` for every live `hold` on an Office, sorted."""
    return sorted((t.subject, t.object) for t in w.tenures
                  if t.kind == "hold" and t.live and t.object in w.offices)


def test_in34_the_sweeps_have_a_control_and_live_arms():
    """The parametrizations below cannot be vacuous: both rows declare the shipped default as their
    control arm and at least one live arm, each a chance."""
    assert AGE_CONTROL == 0 and ILL_CONTROL == 0, "a shipped rate is no longer the control arm"
    assert AGE_CONTROL in ROWS["H-206"]["sweep"] and ILL_CONTROL in ROWS["H-207"]["sweep"]
    for arms in (AGE_ARMS, ILL_ARMS):
        assert arms and all(0 < a <= 1 for a in arms), arms


def test_in34_age_is_read_off_the_clock_and_the_hazard_is_a_query_over_it():
    """No write ages anyone: advancing `tick` alone moves `age_of`, and `body_hazard` is the declared
    sum over it. A cohort has no hazard; a rate outside [0, 1] refuses."""
    w = P.tiny_world()
    assert w.persons, "the fixture holds nobody; nothing below observes anything"
    pid = sorted(w.persons)[0]
    p = w.persons[pid]
    assert p.born == -P.DEFAULT_FIXTURES.get("age_at_build"), "`born` is not the declared default"
    p.born = -3
    w.tick = 2
    assert world_q.age_of(w, pid) == 5
    assert world_q.body_hazard(w, pid) == 0.0, "the shipped rates read a hazard"
    age_step, ill = AGE_ARMS[0], ILL_ARMS[0]
    w.fixtures = w.fixtures.sweep("age_step", age_step).sweep("illness_rate", ill)
    assert world_q.body_hazard(w, pid) == ill + age_step * 5
    w.tick = 3
    assert world_q.body_hazard(w, pid) == ill + age_step * 6, (
        "the hazard did not move with the clock -- age is being stored, not read")
    p.weight = 2
    assert world_q.body_hazard(w, pid) == 0.0, "a cohort read an individual's hazard"
    for bad in (-0.1, 1.5, float("nan")):
        w.fixtures = w.fixtures.sweep("age_step", bad)
        with pytest.raises(ValueError):
            world_q.body_hazard(w, pid)


def test_in34_control_at_the_shipped_rates_nobody_dies_however_old():
    """THE CONTROL: the realm with every individual a thousand years old, at the shipped rates, runs
    the same MATTER barrier as the untouched realm -- the same events, in the same order -- and loses
    nobody. A hazard that ignored the rates would kill every one of them here."""
    base = POP.build_realm(0)
    old = POP.build_realm(0)
    for pid in _individuals(old):
        old.persons[pid].born = -4000
    assert old.fixtures.get("age_step") == 0 and old.fixtures.get("illness_rate") == 0
    want = [(e.kind, e.id) for e in _matter(base)]
    got = [(e.kind, e.id) for e in _matter(old)]
    assert want, "MATTER emitted nothing on the realm; the comparison observes nothing"
    assert got == want, "the shipped rates moved MATTER's output"
    assert set(old.persons) == set(base.persons)
    assert not [e for e in got if e[0] == "person.died"]


@pytest.mark.parametrize("arm", AGE_ARMS)
def test_in34_a_seat_holder_old_enough_dies_at_matter_and_his_seat_falls_vacant(arm):
    """THE VACANCY HALF THAT HOLDS, at each live `age_step` arm, on the BUILT realm. One seat-holder
    is made exactly old enough that the hazard is 1; everyone else is the age the realm builds (0, so
    no hazard at an `age_step`-only arm). MATTER kills him and only him, once, at ROOT (he has no
    prior `person.died`), and the death goes through the one cascade: his `hold` closes, so the
    office has no live holder. A write that removed the person without the cascade leaves the seat
    held by a dead man."""
    w = POP.build_realm(0)
    w.fixtures = w.fixtures.sweep("age_step", arm)
    seats = _seats(w)
    assert seats, "nobody is seated on the realm; the falsifier is vacuous"
    holder, office = seats[0]
    (hold,) = [t for t in w.tenures if t.kind == "hold" and t.live
               and t.subject == holder and t.object == office]
    assert world_q.body_hazard(w, holder) == 0.0
    # one season past the age where the hazard reaches 1, so float rounding cannot leave it short
    w.persons[holder].born = w.tick - (math.ceil(1 / arm) + 1)
    assert world_q.body_hazard(w, holder) == 1.0
    others = set(w.persons) - {holder}

    evs = _matter(w)

    died = [e for e in evs if e.kind == "person.died"]
    assert [c.subject for e in died for c in e.changes] == [holder], (
        f"the deaths at arm {arm} are {[c.subject for e in died for c in e.changes]}, not the one "
        "seat-holder whose hazard is 1")
    assert died[0].causes == [ROOT]
    assert holder not in w.persons and others <= set(w.persons)
    assert not [h for h, o in _seats(w) if o == office], f"{office} is still held after its holder died"
    # ⚠ THE EDGE ITSELF, NOT THE VIEW: `w.tenures` reads the living's own lists, so a death that only
    # popped the person would drop the seat from the view while the `hold` stayed open (MUTATION-
    # CHECKED: `w.persons.pop` in place of `remove_person` passes the line above and fails this one).
    assert not hold.live and hold.until == w.tick, (
        f"{hold.id} is still open after its holder died -- the death skipped the cascade")


def test_in34_at_certain_illness_every_individual_dies_no_cohort_does_and_it_is_keyed():
    """THE EXTREME: `illness_rate` 1 is a chance every individual meets. Each dies exactly once and
    no cohort dies (a population's bound is E-1's, not this hazard). The same seed twice gives the
    same deaths (the control on the same seed is `..._control_at_the_shipped_rates_...` above)."""
    def run(rate):
        w = POP.build_realm(0)
        w.fixtures = w.fixtures.sweep("illness_rate", rate)
        people = _individuals(w)
        evs = _matter(w)
        return people, [c.subject for e in evs if e.kind == "person.died" for c in e.changes], w

    people, dead, w = run(1.0)
    assert people and sorted(dead) == people and len(dead) == len(set(dead)), (
        f"{len(people)} individuals, {len(dead)} deaths at certain illness")
    assert all(p.is_cohort for p in w.persons.values()) and w.persons, "a cohort died, or one lived"
    arm = ILL_ARMS[-1]
    once = run(arm)[1]
    assert once, f"nobody died at the illness arm {arm} on the realm; the keyed check observes nothing"
    assert run(arm)[1] == once, "the same seed gave two sets of deaths"
