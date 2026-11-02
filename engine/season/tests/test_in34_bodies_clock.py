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
  * CONTROL (event level): lives in `test_season_weather.py` (`BASE_EVENTS`, beside the hash pins it
    proves a schema move for): at the shipped rates the ordered (kind, id) sequence of `build_realm(0)`'s
    log after one season and after two EQUALS the pre-IN-34 base's. A hazard that fired at step 0
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

import math

import pytest

from ..data.matrix import Step, WriteClass
from ..harness import populated as POP
from ..harness import probes as P
from ..loop import census
from ..loop.driver import SeasonDriver, mint_token
from ..queries import world_q
from ..state.attribution import causing_act
from ..state.carriers import Act, Person, Rung, Tenure
from ..state.ids import ROOT
from ..state.world import World
from ._scar_helpers import wounded

# TEST ARMS, not game values: nothing here is the number the game ships (those are Jordan's). Each is
# chosen so the test can reach a certainty or a visible fraction, nothing more.
# [JUSTIFIED: test arms -- an `age_step` where a person is certain to die within a century of seasons, and one where a few seasons of age do it]
AGE_ARMS = (0.01, 0.25)
# [JUSTIFIED: test arms -- an age-free chance a draw misses about half the time, and certainty]
ILL_ARMS = (0.5, 1.0)


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


def _age_to_certain(w, pid, arm):
    """Age `pid` to a hazard of exactly 1 at `age_step = arm` -- a season past where it reaches 1, so
    float rounding cannot leave it short. Only `born` moves; the world's own rates are left as they are."""
    w.persons[pid].born = w.tick - (math.ceil(1 / arm) + 1)
    fixtures = w.fixtures
    w.fixtures = fixtures.sweep("age_step", arm)
    try:
        assert world_q.body_hazard(w, pid) == 1.0
    finally:
        w.fixtures = fixtures


def _realm_with_an_old_holder(arm):
    """`build_realm(0)` with its first seat-holder who has company (found by the realm, not named) aged
    to certain death at `age_step = arm`; the world's `age_step` is left at the shipped control."""
    w = POP.build_realm(0)
    seats = _seats(w)
    assert seats, "nobody is seated on the realm; the falsifier is vacuous"
    home = world_q.home_of(w)
    holder, office = next((h, o) for h, o in seats
                          if sum(1 for p in w.persons if p != h and home.get(p) == home.get(h)) >= 2)
    _age_to_certain(w, holder, arm)
    return w, holder, office, home.get(holder), home


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


@pytest.mark.parametrize("arm", AGE_ARMS[1:])    # `AGE_ARMS[0]` sets the same hazard (1.0) for the holder
def test_in34_a_seat_holders_death_by_age_deposits_claims_naming_him_where_he_stood(arm):
    """THE SECOND FALSIFIER, as the tree delivers it (H-206's holder half): one seat-holder is made
    exactly old enough that the hazard is 1, one FULL season runs on the built realm.
      * MATTER writes `person.died` for him alone, chained to ROOT (no prior), placed where he stood;
      * the persons at his place hold claims `person.died` naming him (floor >= 1 such persons);
      * no person elsewhere holds any claim naming him (floor >= 1 such persons checked).
    The step-0 control is the next test. NOT CLAIMED: vacancy claims about his OFFICE or the closed
    HOLD -- H-206's NOT DONE, a different fan-out. The holder is the first seat-holder with company,
    found by the realm and not named."""
    def named(w, holder, who, only=None):
        return {p: [c for c in w.persons[p].ledger if c.subject == holder
                    and (only is None or c.predicate == only)] for p in who if p in w.persons}

    w, holder, office, place, home = _realm_with_an_old_holder(arm)
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
    assert died[0].causes == [ROOT] and causing_act(w, died[0]) is None
    assert holder not in w.persons
    on_here = {p: cs for p, cs in named(w, holder, here, "person.died").items() if cs}
    assert len(on_here) >= 1, (
        f"no one at {place} holds a `person.died` claim naming the dead holder: the death reached "
        "nobody (H-206 not holding)")
    on_away = {p: cs for p, cs in named(w, holder, away).items() if cs}
    assert not on_away, f"{len(on_away)} persons out of reach hold a claim naming him: {sorted(on_away)}"
    assert world_q.event_place(w, died[0]) == place, "the death is not placed where he stood"


def test_in34_control_the_same_holder_as_old_at_step_0_lives_and_deposits_no_death_claim():
    """THE CONTROL ARM of the test above, run once: the holder aged to certain death at an `age_step`
    arm, but the world's rates left at the shipped 0. No `person.died` for him, no `person.died` claim."""
    c, holder, _office, _place, _home = _realm_with_an_old_holder(AGE_ARMS[1])
    assert c.fixtures.get("age_step") == 0 and c.fixtures.get("illness_rate") == 0
    POP.run(seasons=1, seed=0, w=c)
    assert holder in c.persons
    assert not [e for e in c.log if e.kind == "person.died"
                and any(ch.subject == holder for ch in e.changes)]
    assert not [cl for p in c.persons.values() for cl in p.ledger
                if cl.subject == holder and cl.predicate == "person.died"], (
        "the control deposited a death claim about a man who lives")


@pytest.mark.parametrize("arm", AGE_ARMS[1:])    # `AGE_ARMS[0]` sets the same hazard (1.0) for the holder
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
    _age_to_certain(w, holder, arm)
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
    pid = _individuals(w)[0]
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


def test_in34_one_persons_missing_draw_moves_nobody_elses_the_draws_are_keyed_not_a_shared_stream():
    """THE FALSIFIER FOR "ONE KEYED DRAW PER PERSON, NO OTHER STREAM MOVES". Every individual has a
    hazard of one half at `age_step` 0.05 and age ten, so the draws are live. The same one-season arm
    is run twice; the second time ONE individual is aged 0 (`born = w.tick`, hazard 0), so no draw is
    taken for him. The deaths must equal the base deaths minus him. A pass that consumed one shared
    stream in sorted-pid order would hand every later person the draw of the one before, and the sets
    would differ. He is chosen so that a death in the base sorts after him -- the one the shift reaches."""
    def run(skip):
        w = POP.build_realm(0)
        w.fixtures = w.fixtures.sweep("age_step", 0.05)
        for pid in _individuals(w):
            w.persons[pid].born = w.tick - 10
        if skip is not None:
            w.persons[skip].born = w.tick
            assert world_q.body_hazard(w, skip) == 0.0
        return _individuals(w), _died(_matter(w))

    people, base = run(None)
    assert 0 < len(base) < len(people), f"{len(base)} of {len(people)} died; the draws are not observed"
    after_him = [p for p in people if any(d > p for d in base)]
    assert after_him, "no death in the base arm sorts after any individual; the shift cannot be seen"
    skipped = after_him[0]
    _people, without = run(skipped)
    assert without == [d for d in base if d != skipped], (
        f"skipping {skipped}'s draw moved other people's: base {base}, without {without}")


# -- v10 REM-52 (B10-05): H-129's `body.changed` half, reachable the day `body_step` ships off 0 -----------

TOWN_129, HIT, HURT = "set_h129", "p_h129_hit", "p_h129_hurt"


def _two_cohorts_in_a_dearth() -> World:
    """realm > territory > settlement holding NOTHING with no Site (no yield), and two cohorts housed there,
    so each is short by its whole want at the first MATTER barrier. Fixtures are the SHIPPED ones."""
    w = World(0)
    for rid, kind in (("r_realm", "realm"), ("terr_h129", "territory"), (TOWN_129, "settlement")):
        w.rungs[rid] = Rung(rid, kind)
    w.add_tenure(Tenure("t_in_0", "terr_h129", "r_realm", "contain", 0))
    w.add_tenure(Tenure("t_in_1", TOWN_129, "terr_h129", "contain", 0))
    for pid in (HIT, HURT):
        w.persons[pid] = Person(pid, pid, weight=2)
        w.rungs[pid] = Rung(pid, "person")
        w.add_tenure(Tenure(f"t_{pid}_in", pid, TOWN_129, "contain", 0))
        w.add_tenure(Tenure(f"t_{pid}_home", pid, TOWN_129, world_q.RESIDE_KIND, 0))
    return w


def test_h129_a_wounded_then_starved_person_chains_to_the_wound_that_wrote_him_and_the_wounder_does_not():
    """H-129, THE `body.changed` HALF (REM-52 passes `written=True` at the bodies pass of `matter`, in the
    same commit that ships `body_step` off 0). The fold's `body.changed` for a wound is caused by the ACT, so
    it ANCHORS on the wounder (tier 1) and `last_emission_of("body.changed", pid)` by anchor answered for
    the wrong person: the victim's own later starvation write chained to `[ROOT]` (the wound that wrote his
    body was missed), and the WOUNDER's starvation write chained to the wound he had inflicted on somebody
    else. Both ends are asserted at the SHIPPED step, the real fold (`fight`, a `Wounded` scene result) then
    the real MATTER barrier:
      * `HURT` (wounded by `HIT`, then starved) chains to the wound Event that wrote HIS body;
      * `HIT` (the wounder, starved, never wounded) chains to `[ROOT]`, not to the wound he dealt.
    MUTATION, run at REM-52 (`written=True` taken back off the read in `loop/matter.py`): both assertions
    red -- `HURT` cites `[ROOT]`, `HIT` cites the wound -- and with it on, both pass."""
    w = _two_cohorts_in_a_dearth()
    assert w.fixtures.get("body_step") > 0, "this test reads the SHIPPED live arm; the control would be vacuous"
    act = Act(id="h129_wound", actor=HIT, verb="fight", payload={"subject": HURT})
    w.step = Step.RESOLVE
    evs = SeasonDriver(w)._fold(w, mint_token(w, WriteClass.ACTS), act, wounded(HURT, full=10, left=5, actor=HIT))
    for ev in evs:                      # the fold returns the Events; the barrier logs them
        w.log.append(ev)
    (wound,) = [e for e in evs if e.kind == "body.changed" and any(c.subject == HURT for c in e.changes)]
    assert causing_act(w, wound) is not None and wound.causes[0] == act.id, "fixture: the wound is not act-caused"
    assert w.persons[HURT].body < w.fixtures.get("condition_scale") and w.persons[HIT].body == (
        w.fixtures.get("condition_scale")), "fixture: the wound did not land on the victim alone"
    assert w.last_emission_of("body.changed", HURT) is None, "fixture: the anchor read already finds the wound"
    assert w.last_emission_of("body.changed", HURT, written=True) == wound.id

    w.tick += 1
    starved = [e for e in _matter(w) if e.kind == "body.changed"]
    mine = {pid: [e for e in starved if any(c.subject == pid for c in e.changes)] for pid in (HIT, HURT)}
    assert all(len(v) == 1 for v in mine.values()), {k: len(v) for k, v in mine.items()}
    got = {HURT: mine[HURT][0].causes, HIT: mine[HIT][0].causes}
    assert got == {HURT: [wound.id], HIT: [ROOT]}, (
        f"the starvation writes cite {got}: the wounded-then-starved person's must be the wound {wound.id} "
        f"that wrote his body, and the wounder's (never wounded) must be [ROOT], not the wound he dealt")
