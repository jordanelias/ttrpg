"""v9 IN-34 -- FORCE-BODIES: ageing and illness through the bodies motion (#457 D2).

#457 D2, answered [medium; Jordan to correct]: ageing and illness are in scope, a HAZARD READER only,
rates swept. What the position built, each asked of the real builder, the real MATTER barrier and the
real Queries:
  * ONE FIELD, `Person.born` (`state/carriers.py`), defaulting to `-age_at_build`; age is READ OFF THE
    CLOCK (`world_q.age_of`), never stored; its two readers are `age_of` and, through it,
    `world_q.body_hazard` (ID-13);
  * THE HAZARD AS ITS READER, `world_q.body_hazard`: `illness_rate + age_step * age`, capped at 1,
    none for a cohort;
  * ONE BODIES WRITE AT MATTER (`loop/matter.py`'s bodies pass): a keyed draw per living person, and a
    hit is `(Person, exists)` through `World.remove_person`, emitting `person.died` chained to that
    person's own prior emission.
SHIPPED DARK: `age_step` and `illness_rate` ship at 0 and `age_at_build` at 0. NONE of the three is
chosen here -- they are Jordan's (#457 D2's gate) -- so every arm below is a TEST arm, swept, ruling
nothing.

THE FALSIFIERS, each with the failure it would show:
  * CONTROL (event level): at the shipped rates the ordered (kind, id) sequence of `build_realm(0)`'s
    log after one season and after two EQUALS the pre-IN-34 base's (pinned below: count and digest, taken
    on d47077d5 before the field existed). `test_season_weather.py`'s three hash pins are re-recorded for
    the schema move this field causes, and THIS is the proof that the move is schema alone: the hash
    folds `repr(Person)`, which gained a field; the events did not move. A hazard that fired at step 0
    changes the sequence;
  * SECOND FALSIFIER, stated as what the tree delivers: a seat-holder's death by age deposits CLAIMS
    NAMING THE DEAD HOLDER on the persons at his place and none on persons out of reach, and the same
    arm at step 0 deposits none. It does NOT claim vacancy claims about the OFFICE or the closed
    HOLD: those are H-206's NOT DONE (`claim_subjects` does not expand a departed person's holds);
  * READER (ID-13): two individuals at one arm, one old and one new -- the old one dies and the new one
    lives, so `born` is read; an `age_of` that ignored it kills nobody;
  * CHAIN: a `person.died` at MATTER cites the person's own prior `person.died` when there is one.
"""

from __future__ import annotations

import hashlib
import math

import pytest

from ..data.matrix import Step, WriteClass
from ..harness import populated as POP
from ..harness import probes as P
from ..loop import census
from ..loop.driver import SeasonDriver, mint_token
from ..queries import world_q
from ..state.ids import ROOT

# TEST ARMS, not game values: nothing here is the number the game ships (those are Jordan's). Each is
# chosen so the test can reach a certainty or a visible fraction, nothing more.
# [JUSTIFIED: test arms -- an `age_step` where a person is certain to die within a century of seasons, and one where a few seasons of age do it]
AGE_ARMS = (0.01, 0.25)
# [JUSTIFIED: test arms -- an age-free chance a draw can miss, and certainty]
ILL_ARMS = (0.05, 1.0)

# The pre-IN-34 base (d47077d5), `build_realm(0)` driven by `POP.run`, seed 0: the whole log's event
# count and the sha256 of its ordered `kind|id` lines after one season and after two.
BASE_EVENTS = {1: (7526, "e56f8652be7f7cd52352bdf07ef17dcc555daf83e267a37b0eecafc096ec82e7"),
               2: (21508, "dc3c440ad533b0548d69bfdc8b092e3ccc03ff622baa9a5167a92c839c2b42f4")}


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


def _died(evs) -> list:
    return [c.subject for e in evs if e.kind == "person.died" for c in e.changes]


def _digest(w) -> tuple:
    seq = [f"{e.kind}|{e.id}" for e in w.log]
    return len(seq), hashlib.sha256("\n".join(seq).encode()).hexdigest()


def test_in34_the_shipped_rates_are_the_control_and_the_test_arms_are_live():
    """The parametrizations below cannot be vacuous, and the shipped values are the control."""
    for key in ("age_step", "illness_rate", "age_at_build"):
        assert P.DEFAULT_FIXTURES.get(key) == 0, f"shipped `{key}` is no longer the control arm"
    assert all(0 < a <= 1 for a in AGE_ARMS + ILL_ARMS)


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


def test_in34_a_person_minted_at_census_is_age_at_build_old_when_minted():
    """`loop/census.py::_individuate` mints from the `Person` defaults, whose `born` is `-age_at_build`
    -- age `age_at_build` at tick 0 and older by every season since. The mint passes its own `born`."""
    w = POP.build_realm(0)
    at = sorted(r for r, x in w.rungs.items() if x.kind == "settlement")[0]
    w.fixtures = w.fixtures.sweep("age_at_build", 7)
    w.tick = 3
    census._individuate(w, "p_minted_probe", at)
    assert world_q.age_of(w, "p_minted_probe") == 7, (
        "a person minted at tick 3 is not `age_at_build` old: the mint took the bare default")


def test_in34_control_at_the_shipped_rates_nobody_dies_however_old():
    """THE CONTROL AT MATTER: the realm with every individual a thousand years old, at the shipped
    rates, runs the same MATTER barrier as the untouched realm -- the same events, in the same order --
    and loses nobody. A hazard that fired at step 0 would kill every one of them here."""
    base = POP.build_realm(0)
    old = POP.build_realm(0)
    people = _individuals(old)
    assert len(people) >= 10, "the realm seats too few individuals for the control to observe anything"
    for pid in people:
        old.persons[pid].born = -4000
    assert old.fixtures.get("age_step") == 0 and old.fixtures.get("illness_rate") == 0
    want = [(e.kind, e.id) for e in _matter(base)]
    got = [(e.kind, e.id) for e in _matter(old)]
    assert len(want) >= 100, f"MATTER emitted {len(want)} events on the realm; the comparison is thin"
    assert got == want, "the shipped rates moved MATTER's output"
    assert set(old.persons) == set(base.persons)
    assert not [e for e in got if e[0] == "person.died"]


def test_in34_control_the_event_sequence_over_one_and_two_seasons_equals_the_base():
    """THE EVENT-LEVEL CONTROL (the plan's restated control): `age_step` 0 reproduces the base's ordered
    (kind, id) sequence after one season and after two -- the proof that the re-pinned
    `test_season_weather.BASE_HASHES` moved by the `Person` schema alone. ~2 minutes (the realm, two
    real seasons)."""
    w = POP.build_realm(0)
    assert w.fixtures.get("age_step") == 0 and w.fixtures.get("illness_rate") == 0
    got = {}
    for n in (1, 2):
        POP.run(seasons=1, seed=0, w=w)
        got[n] = _digest(w)
    assert got[1][0] >= 5000 and got[2][0] >= 15000, f"the seasons emitted too little to observe: {got}"
    assert got == BASE_EVENTS, f"age_step 0 moved the event sequence: {got}"


@pytest.mark.parametrize("arm", AGE_ARMS)
def test_in34_a_seat_holders_death_by_age_deposits_claims_naming_him_where_he_stood(arm):
    """THE SECOND FALSIFIER, as the tree delivers it (H-206's holder half): one seat-holder is made
    exactly old enough that the hazard is 1, one FULL season runs on the built realm.
      * MATTER writes `person.died` for him alone, chained to ROOT (no prior), placed where he stood;
      * the persons at his place hold claims `person.died` naming him (floor >= 1 such persons);
      * no person elsewhere holds any claim naming him (floor >= 1 such persons checked);
      * the same arm at step 0, the same holder just as old: no `person.died` for him and no
        `person.died` claim anywhere.
    NOT CLAIMED: vacancy claims about his OFFICE or the closed HOLD -- H-206's NOT DONE, a different
    fan-out. The holder is the first seat-holder with company, found by the realm and not named."""
    def build():
        w = POP.build_realm(0)
        seats = _seats(w)
        assert seats, "nobody is seated on the realm; the falsifier is vacuous"
        home = world_q.home_of(w)
        holder, office = next((h, o) for h, o in seats
                              if sum(1 for p in w.persons if p != h and home.get(p) == home.get(h)) >= 2)
        # a season past where the hazard reaches 1, so float rounding cannot leave it short
        w.persons[holder].born = w.tick - (math.ceil(1 / arm) + 1)
        return w, holder, office, home.get(holder), home

    def named(w, holder, who, only=None):
        return {p: [c for c in w.persons[p].ledger if c.subject == holder
                    and (only is None or c.predicate == only)] for p in who if p in w.persons}

    # -- the killed arm ----------------------------------------------------------------------
    w, holder, office, place, home = build()
    w.fixtures = w.fixtures.sweep("age_step", arm)
    here = {p for p in w.persons if p != holder and home.get(p) == place}
    away = {p for p in w.persons if p != holder and home.get(p) != place}
    assert len(here) >= 1 and len(away) >= 1
    assert world_q.body_hazard(w, holder) == 1.0
    others_hazard = [world_q.body_hazard(w, p) for p in w.persons if p != holder]
    assert not any(others_hazard), "someone else is old enough to die; the arm is not about one holder"

    POP.run(seasons=1, seed=0, w=w)

    died = [e for e in w.log if e.kind == "person.died" and any(c.subject == holder for c in e.changes)]
    assert len(died) == 1, f"{len(died)} `person.died` events name the holder"
    assert died[0].causes == [ROOT] and world_q.causing_act(w, died[0]) is None
    assert holder not in w.persons
    on_here = {p: cs for p, cs in named(w, holder, here, "person.died").items() if cs}
    assert len(on_here) >= 1, (
        f"no one at {place} holds a `person.died` claim naming the dead holder: the death reached "
        "nobody (H-206 not holding)")
    on_away = {p: cs for p, cs in named(w, holder, away).items() if cs}
    assert not on_away, f"{len(on_away)} persons out of reach hold a claim naming him: {sorted(on_away)}"
    assert world_q.event_place(w, died[0]) == place, "the death is not placed where he stood"

    # -- the control arm: the same holder, as old, step 0 ------------------------------------------
    c, holder_c, _o, _p, _h = build()
    assert holder_c == holder and c.fixtures.get("age_step") == 0
    POP.run(seasons=1, seed=0, w=c)
    assert holder in c.persons
    assert not [e for e in c.log if e.kind == "person.died"
                and any(ch.subject == holder for ch in e.changes)]
    assert not [cl for p in c.persons.values() for cl in p.ledger
                if cl.subject == holder and cl.predicate == "person.died"], (
        "the control deposited a death claim about a man who lives")


@pytest.mark.parametrize("arm", AGE_ARMS)
def test_in34_a_seat_holder_old_enough_dies_at_matter_and_his_seat_falls_vacant(arm):
    """THE CASCADE, at each live `age_step` arm, on the BUILT realm: MATTER kills the one old
    seat-holder and only him, once, and the death goes through the one cascade -- his `hold` closes, so
    the office has no live holder. A write that removed the person without the cascade leaves the seat
    held by a dead man."""
    w = POP.build_realm(0)
    w.fixtures = w.fixtures.sweep("age_step", arm)
    seats = _seats(w)
    assert seats, "nobody is seated on the realm; the falsifier is vacuous"
    holder, office = seats[0]
    (hold,) = [t for t in w.tenures if t.kind == "hold" and t.live
               and t.subject == holder and t.object == office]
    assert world_q.body_hazard(w, holder) == 0.0
    w.persons[holder].born = w.tick - (math.ceil(1 / arm) + 1)
    assert world_q.body_hazard(w, holder) == 1.0
    others = set(w.persons) - {holder}

    evs = _matter(w)

    assert _died(evs) == [holder], f"the deaths at arm {arm} are {_died(evs)}, not the one holder"
    assert holder not in w.persons and others <= set(w.persons)
    assert not [h for h, o in _seats(w) if o == office], f"{office} is still held after its holder died"
    # THE EDGE ITSELF, NOT THE VIEW: `w.tenures` reads the living's own lists, so a death that only
    # popped the person would drop the seat from the view while the `hold` stayed open.
    assert not hold.live and hold.until == w.tick, (
        f"{hold.id} is still open after its holder died -- the death skipped the cascade")


def test_in34_born_has_a_reader_the_older_person_dies_and_the_younger_lives():
    """ID-13: no field without a reader. Two individuals at one `age_step` arm; only `born` differs.
    The old one is certain to die, the new one has no hazard. An `age_of` that ignored `born` (the
    field dead) gives both the same hazard, so either both live or both die -- red."""
    w = POP.build_realm(0)
    old, new = _individuals(w)[:2]
    arm = AGE_ARMS[1]
    w.fixtures = w.fixtures.sweep("age_step", arm)
    w.persons[old].born = w.tick - 10
    w.persons[new].born = w.tick
    assert world_q.body_hazard(w, old) == 1.0 and world_q.body_hazard(w, new) == 0.0
    assert _died(_matter(w)) == [old]
    assert new in w.persons


def test_in34_a_second_person_died_at_matter_cites_the_first_it_chains_to():
    """`person.died` is chained to ITS OWN PRIOR EMISSION (`last_emission_of`): an id that died, was
    individuated again (`census._individuate`) and died again cites its first death, not ROOT. The
    first death has no antecedent and cites ROOT."""
    w = POP.build_realm(0)
    w.fixtures = w.fixtures.sweep("illness_rate", 1.0)
    (pid,) = [_individuals(w)[0]]
    first = [e for e in _matter(w) if e.kind == "person.died"
             and any(c.subject == pid for c in e.changes)]
    assert len(first) == 1 and first[0].causes == [ROOT]
    at = sorted(r for r, x in w.rungs.items() if x.kind == "settlement")[0]
    w.tick += 1
    census._individuate(w, pid, at)
    assert pid in w.persons
    second = [e for e in _matter(w) if e.kind == "person.died"
              and any(c.subject == pid for c in e.changes)]
    assert len(second) == 1
    assert second[0].causes == [first[0].id], (
        f"the second death cites {second[0].causes}, not its own prior emission {first[0].id}")


def test_in34_at_certain_illness_every_individual_dies_no_cohort_does_and_it_is_keyed():
    """THE EXTREME: `illness_rate` 1 is a chance every individual meets. Each dies exactly once and
    no cohort dies (a population's bound is E-1's, not this hazard). The same seed twice gives the
    same deaths, at an arm a draw can miss."""
    def run(rate):
        w = POP.build_realm(0)
        w.fixtures = w.fixtures.sweep("illness_rate", rate)
        people = _individuals(w)
        return people, _died(_matter(w)), w

    people, dead, w = run(1.0)
    assert people and sorted(dead) == people and len(dead) == len(set(dead)), (
        f"{len(people)} individuals, {len(dead)} deaths at certain illness")
    assert w.persons and all(p.is_cohort for p in w.persons.values()), "a cohort died, or one lived"
    arm = ILL_ARMS[0]
    people, once, _w = run(arm)
    assert 0 < len(once) < len(people), f"{len(once)} of {len(people)} died at {arm}; no draw is observed"
    assert run(arm)[1] == once, "the same seed gave two sets of deaths"
