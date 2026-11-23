"""B10.14 -- the crisis reader's one composed signature, `queries/person_q.py::conviction_after_crisis(p, among, band, shared, reading)`.
Hand-built persons with planted creeds and scar counts; every expected conviction is stated here, not re-derived from the reader.

FALSIFIER: at the shared column the stronger creed is still the one folded, or `band=None` is no longer today's function.
"""
from __future__ import annotations

from engine.dice_engine.dice_engine import DEGREE_LABEL, Degree

from ..data import affiliations as A
from ..data.fixtures import DEFAULT_FIXTURES
from ..data.matrix import Step
from ..harness import probes as P
from ..loop import resolve as R
from ..queries import person_q as PQ
from ..queries import world_q
from ..state.carriers import Act, Event, Person
from ..state.ids import H
from ._scar_helpers import compatible_pairs, fight, incompatible_pairs, rebound

MOVED = "conviction.moved"
LEVEL = "demanding"              # [ASSUMPTION; the test reads a direction, not the calibrated value]


def _drawn(fixtures=DEFAULT_FIXTURES):
    return fixtures.sweep("crisis_arm", "drawn").sweep("crisis_obstacle", LEVEL)


def _person(conviction: dict, scar: dict) -> Person:
    return Person(id="p_crisis", conviction=dict(conviction), scar=dict(scar))


def test_off_reproduces_conviction_after_crisis():
    """`band=None`, `shared=False`, `reading="any"` is today's function on each of its branches, and its `scar_delta` is empty."""
    a, b = incompatible_pairs()[0]
    c, d = compatible_pairs()[0]
    checked = 0
    # FOLD: the stronger of two incompatible creeds in crisis is the one taken (today's `max`), its intensity going to the other, clamped.
    after, delta = PQ.conviction_after_crisis(_person({a: 4, b: 2}, {a: 3, b: 3}))
    assert (after, delta) == ({b: 5}, {})
    checked += 1
    # DESTROYED: nothing else is held.
    assert PQ.conviction_after_crisis(_person({a: 3}, {a: 3})) == ({}, {})
    checked += 1
    # RESTABILISE is not built: a compatible creed held beside it leaves the vector as it was.
    held = {c: 3, d: 2}
    assert PQ.conviction_after_crisis(_person(held, {c: 3})) == (held, {})
    checked += 1
    # `among` bounds the crisis to the creeds the act just scarred: a creed at the threshold that was not scarred is not in crisis.
    assert PQ.conviction_after_crisis(_person({a: 4, b: 2}, {a: 3}), among=frozenset({b})) == ({a: 4, b: 2}, {})
    checked += 1
    assert checked >= 4


def test_lowest_intensity_creed_is_the_one_in_crisis_for_shared_column():
    """Where the shared column scars every held creed alike, the lowest-intensity creed is the one in crisis and folds into the stronger."""
    a, b = incompatible_pairs()[0]
    held, scar = {a: 4, b: 2}, {a: 3, b: 3}
    shared, _ = PQ.conviction_after_crisis(_person(held, scar), shared=True)
    assert shared == {a: 5}, "the weaker creed must be the one that drops"
    # the control: a per-affiliation cell keeps the draft's direction (the stronger creed in crisis), the same person
    cell, _ = PQ.conviction_after_crisis(_person(held, scar), shared=False)
    assert cell == {b: 5}
    # a tie on intensity goes to the first by name under either selector
    tied, _ = PQ.conviction_after_crisis(_person({a: 3, b: 3}, {a: 3, b: 3}), shared=True)
    assert tied == {b: 5} and a < b


def test_each_band_writes_what_its_table_row_says():
    """`band=` reads `tables.crisis_bands`: the Overwhelming, Success, Partial and Failure rows each leave the creed in crisis, and its count, as written."""
    c, d = compatible_pairs()[0]
    a, b = incompatible_pairs()[0]
    held, scar = {c: 3, d: 2}, {c: 4}                    # a count of 4: `zero` (-4) and `threshold_less_one` (-2) differ
    got = {band: PQ.conviction_after_crisis(_person(held, scar), band=band) for band in PQ.CRISIS_BANDS}
    BAND = {name: name for name in PQ.CRISIS_BANDS}      # the table's own names: a bare band literal here reads as a second degree ladder
    assert got["Overwhelming"] == ({c: 4, d: 2}, {c: -4})
    assert got["Success"] == (held, {c: -2})
    assert got["Partial"] == ({c: 2, d: 2}, {})
    assert got["Failure"] == ({c: 1, d: 2}, {})          # nothing incompatible held, something else held: -2
    assert PQ.conviction_after_crisis(_person({c: 5, d: 2}, scar), band=BAND["Overwhelming"])[0] == {c: 5, d: 2}, "clamped at the ceiling"
    assert PQ.conviction_after_crisis(_person({c: 1, d: 2}, scar), band=BAND["Partial"])[0] == {c: 0, d: 2}, "a held rejection, not a drop"
    assert PQ.conviction_after_crisis(_person({c: 1, d: 2}, scar), band=BAND["Failure"])[0] == {c: 0, d: 2}, "floored at 0"
    assert PQ.conviction_after_crisis(_person({a: 3, b: 2}, {a: 3, b: 3}), band=BAND["Failure"]) == ({b: 5}, {}), "Failure folds first"
    assert PQ.conviction_after_crisis(_person({c: 3}, {c: 3}), band=BAND["Failure"]) == ({}, {}), "Failure destroys where nothing else is held"


def _record(seen: list, draw, pid: str, purpose: str):
    seen.append((pid, purpose, draw.key))
    return draw


def test_two_crises_of_one_person_in_one_tick_have_two_keys(monkeypatch):
    """The key of a crisis roll is `H(seed, tick, person, "crisis:" + act.id)`: a person scarred past the threshold by two acts of one tick is drawn twice,
    once under each act's key. Planted: the shipped table rebound so `fight` wounds every holding alike, three fights folded through the real fold."""
    monkeypatch.setattr(A, "ENGAGEMENT", rebound(**{A.SHARED_COLUMN: {"fight": -0.3}}))
    seen = []
    real = R.draw_factory
    monkeypatch.setattr(R, "draw_factory", lambda seed, tick_of: (lambda pid, purpose: _record(seen, real(seed, tick_of)(pid, purpose), pid, purpose)))
    a, b = compatible_pairs()[0]
    w = P.tiny_world(_drawn(DEFAULT_FIXTURES.sweep("fan_out_mode", "total")))
    for p in w.persons.values():
        p.pursuits, p.conviction, p.scar = {}, {a: 5, b: 5}, {a: 2, b: 2}
    w.step = Step.RESOLVE
    acts = ("c_fight_1", "c_fight_2", "c_fight_3")
    before = {pid: dict(p.conviction) for pid, p in w.persons.items()}
    events = [e for act in acts for e in fight(w, act)]
    by_person: dict = {}
    for pid, purpose, key in seen:
        if purpose.startswith("crisis:"):
            by_person.setdefault(pid, []).append((purpose, key))
    # Every conviction a crisis moved is TOLD: one `conviction.moved` Event naming him, graded on the ladder, with the act that scarred him in `causes`.
    told = {c.subject for e in events if e.kind == MOVED for c in e.changes}
    moved = {pid for pid, p in w.persons.items() if p.conviction != before[pid]}
    assert moved and moved <= told, f"a conviction write went untold: moved {moved}, told {told}"
    for e in (e for e in events if e.kind == MOVED):
        (change,) = e.changes
        assert change.field == "conviction" and change.subject in w.persons and e.degree in DEGREE_LABEL.values()
        assert any(act in acts for act in e.causes), f"{e.id} names none of the acts that scarred {change.subject}"
    twice = {pid: drawn for pid, drawn in by_person.items() if len(drawn) >= 2}
    assert twice, f"no person was drawn twice in one tick: {by_person}"
    for pid, drawn in twice.items():
        purposes = [p for p, _k in drawn]
        assert len(set(purposes)) == len(purposes) and set(purposes) <= {"crisis:" + act for act in acts}, (pid, purposes)
        assert len({k for _p, k in drawn}) == len(drawn), f"{pid}: two crises shared a key"
        assert all(k == H(w.world_seed, w.tick, pid, p) for p, k in drawn), f"{pid}: a key is not H(seed, tick, person, purpose)"


def test_an_observers_crisis_band_does_not_practise_the_actor_who_scarred_him():
    """A `conviction.moved` Event names the scarring act in `causes` and carries the OBSERVER'S band: an observer's Overwhelming crisis must not credit the actor's
    practice in that act's key. Planted: `p_low`'s one `fight` resolved at Failure, then a crisis Event at Overwhelming caused by it; a `body.changed` Event at
    Overwhelming caused by it is the control that the reader does count a good result of his own act."""
    w = P.tiny_world(DEFAULT_FIXTURES.sweep("practice_step", 1))
    w.acts.append(Act(id="a_fight", actor="p_low", verb="fight", payload={"subject": "p_mid"}))
    w.log.append(Event("ev_own", "body.changed", [P.apparatus_receipt(w, "p_mid", "set", "Person")], ["a_fight"], 0, DEGREE_LABEL[Degree.FAILURE]))
    w.log.append(Event("ev_crisis", MOVED, [P.apparatus_receipt(w, "p_other", "set", "Person")], ["a_fight"], 0, DEGREE_LABEL[Degree.OVERWHELMING]))
    w.tick = 1
    assert world_q.practice(w, w.persons["p_low"], "fight") == 0, "an observer's crisis band credited the actor who scarred him"
    w.log.append(Event("ev_good", "body.changed", [P.apparatus_receipt(w, "p_mid", "set", "Person")], ["a_fight"], 0, DEGREE_LABEL[Degree.OVERWHELMING]))
    assert world_q.practice(w, w.persons["p_low"], "fight") == 1, "the reader no longer counts his own act's good result"
