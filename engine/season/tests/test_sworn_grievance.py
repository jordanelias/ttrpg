"""B09.22 -- A SEAT CLOSED BY A DEATH NAMES ITS HOLDER (IN-58's carrier; lane D4).

THE GAP (v11 IN-58, NARROWED): a witness of a seat-holder's death held `(seat, tenure.closed, True)` and, on its own
channel, `(victim, person.died, True)`, and nothing that PAIRED the two -- `queries/person_q.py::deeds_judged` says it in
words, "what is missing is the PAIRING, not the edge". `state/gate.py::Subject.seat` now carries one Observation
`(seat, "hold", <the holder whose hold closed>)` on CP-T03-02's existing `Subject.observed` channel, so the Event the
seat earns (`tenure.closed`) carries it and WITNESS deposits it by its shipped `observation_deposit_mode`. No Claim,
Event or World field is added; no reader is added (B09.20 is the reader).

WHICH WITNESS HOLDS IT is WITNESS's mode, not a filter here: at the shipped `actor` the deposit is the actor's own
(the killer's), at `total` every witness of the Event holds it (`loop/witness.py`'s observation block).

The method is `test_cp_t02_01_death_names_seats`: a constructed `Felled` resolution through the real fold and the real
WITNESS barrier on `tiny_world` (`p_high` holds `off_duke`).

  (a) FALSIFIER: a witness who holds the seat's `tenure.closed` claim and none naming the holder with the seat. Run as
      the test's own assertion on the dead holder's name, and as a mutation (the Observation off) which turns it red.
  (b) A claim naming a holder whose `hold` did NOT close in that write: a WOUNDED seat-holder leaves no `hold` claim in
      any ledger, and every `hold` claim a felling leaves names a seat the dead man held, with him as the value.
  (c) CONTROL: the death of a person who holds no seat leaves no `hold` claim in any ledger and the same Event kinds.
"""
from __future__ import annotations

import pytest

from ..data.fixtures import DEFAULT_FIXTURES
from ..data.matrix import Step, WriteClass
from ..harness import probes as P
from ..loop.driver import SeasonDriver, mint_token
from ..queries import world_q
from ..seam.contest import Resolution
from ..state import gate
from ..state.carriers import Act, Person, Rung, Tenure
from ._scar_helpers import party_state, wounded

HOLDER, OFFICE, KILLER = "p_high", "off_duke", "p_near"
HOLD = "hold"
CLOSED = "tenure.closed"


def _tiny(mode=None):
    """`tiny_world` plus `p_near`, who stands at `S` with p_high (so a `fight` between them is admitted). `mode`
    sweeps `observation_deposit_mode` (None: the shipped `actor`)."""
    fx = DEFAULT_FIXTURES if mode is None else DEFAULT_FIXTURES.sweep("observation_deposit_mode", mode)
    w = P.tiny_world(fx)
    w.persons[KILLER] = Person(KILLER, "a neighbour")
    w.rungs[KILLER] = Rung(KILLER, "person")
    w.add_tenure(Tenure("t_near_in", KILLER, "S", "contain", 0))
    w.add_tenure(Tenure("t_near_home", KILLER, "S", world_q.RESIDE_KIND, 0))
    return w


def _fight(w, actor, victim, res, aid="b0922_fight"):
    """`actor` fights `victim`, the scene resolving as `res`, through the real fold and gate at RESOLVE; the Events
    are logged as the barrier logs them, then WITNESS runs. Returns `(Events, the driver)`."""
    d = SeasonDriver(w)
    w.step = Step.RESOLVE
    w.frozen = False
    out = d._fold(w, mint_token(w, WriteClass.ACTS),
                  Act(id=aid, actor=actor, verb="fight", payload={"subject": victim}), res)
    for e in out:
        w.log.append(e)
    w.step = Step.WITNESS
    d.witness(mint_token(w, WriteClass.INTERIOR), out)
    return out, d


def _felled(victim, actor):
    return Resolution("Felled", {"wound_state": {victim: party_state(felled=True, left=0),
                                                 actor: party_state()}})


def _about(w, pid, subject, predicate):
    return [c for c in w.persons[pid].ledger if c.subject == subject and c.predicate == predicate]


def _kill_the_holder(mode=None):
    w = _tiny(mode)
    assert [t.object for t in w.seat_holds(HOLDER)] == [OFFICE], "fixture: p_high does not hold off_duke"
    out, _ = _fight(w, KILLER, HOLDER, _felled(HOLDER, KILLER))
    assert HOLDER not in w.persons, "fixture: the planted death did not happen"
    assert CLOSED in [e.kind for e in out], "fixture: the death emitted no tenure.closed"
    return w, out


def test_a_witness_of_a_seat_holders_death_holds_the_seat_and_its_holder():
    """THE ITEM'S TEST. At `total` every living witness of the Event holds BOTH claims about the seat, `(seat,
    tenure.closed, True)` and `(seat, hold, victim)`, deposited at the same `when` and `lap`; at the shipped `actor` the
    killer does (the observation is the actor's own there). The assertion is made over a checked count, never over an
    empty loop."""
    w, out = _kill_the_holder(mode="total")
    living = list(w.persons)
    checked = 0
    for pid in living:
        closed = _about(w, pid, OFFICE, CLOSED)
        held = _about(w, pid, OFFICE, HOLD)
        assert closed, f"{pid} holds no `tenure.closed` claim about {OFFICE}: the fixture reaches nothing"
        assert [c.value for c in held] == [HOLDER], (
            f"{pid} holds {[(c.predicate, c.value) for c in held]} for {OFFICE}, not the holder whose `hold` closed")
        assert (closed[0].when, closed[0].lap) == (held[0].when, held[0].lap), (
            f"{pid}: the two claims about the seat were deposited at different times")
        checked += 1
    assert checked >= 3, f"fixture: only {checked} living witnesses, so 'every' means little"
    # and the Event carries it on the channel that exists: `Event.observed`, not a field
    e = next(e for e in out if e.kind == CLOSED)
    assert [(o.subject, o.predicate, o.value) for o in e.observed
            if o.predicate == HOLD] == [(OFFICE, HOLD, HOLDER)]


def test_at_the_shipped_mode_the_killer_holds_the_seat_and_its_holder():
    """The shipped `actor` mode: the deposit is the actor's own, so the killer holds the pairing and a bystander
    holds the seat's `tenure.closed` claim alone -- WITNESS's mode, unchanged by this item."""
    w, _ = _kill_the_holder()
    assert [c.value for c in _about(w, KILLER, OFFICE, HOLD)] == [HOLDER]
    bystander = "p_low"
    assert _about(w, bystander, OFFICE, CLOSED), "fixture: the bystander was not told of the seat"
    assert not _about(w, bystander, OFFICE, HOLD), "a non-actor holds the pairing at the shipped `actor` mode"


def test_mutation_the_seat_without_its_observation_leaves_no_pairing(monkeypatch):
    """THE FALSIFIER (a), RUN: `Subject.seat` stripped of its Observation is the pre-item world -- a witness holds
    `tenure.closed` and no claim naming the holder with the seat. The item's own test must go red on it."""
    seat = gate.Subject.seat.__func__

    def bare(cls, t):
        s = seat(cls, t)
        return type(s)(s.id, s.ref, s.earns)

    monkeypatch.setattr(gate.Subject, "seat", classmethod(bare))
    w = _tiny("total")
    out, _ = _fight(w, KILLER, HOLDER, _felled(HOLDER, KILLER))
    assert HOLDER not in w.persons and CLOSED in [e.kind for e in out]
    checked = 0
    for pid in w.persons:
        assert _about(w, pid, OFFICE, CLOSED)
        assert not _about(w, pid, OFFICE, HOLD), "the pairing exists with the Observation off"
        checked += 1
    assert checked >= 3


def test_a_hold_that_did_not_close_names_no_holder():
    """(b): a WOUNDED seat-holder keeps his seat -- no `tenure.closed`, and no `hold` claim in any ledger. And a
    felling's `hold` claims name only seats the dead man held, each with him as the value."""
    w = _tiny("total")
    out, _ = _fight(w, KILLER, HOLDER, wounded(victim=HOLDER, actor=KILLER))
    assert HOLDER in w.persons and w.seat_holds(HOLDER), "fixture: the wounded holder lost his seat"
    assert CLOSED not in [e.kind for e in out]
    checked = 0
    for pid in w.persons:
        assert not [c for c in w.persons[pid].ledger if c.predicate == HOLD], f"{pid} holds a `hold` claim"
        checked += 1
    assert checked >= 3

    w2, _ = _kill_the_holder("total")
    checked = 0
    for pid in w2.persons:
        for c in w2.persons[pid].ledger:
            if c.predicate == HOLD:
                assert c.subject == OFFICE and c.value == HOLDER, (c.subject, c.value)
                checked += 1
    assert checked >= 3


def test_control_a_death_with_no_seat_leaves_no_pairing():
    """(c): `p_near` holds no seat. His felling emits `person.died` and no `tenure.closed`, and no ledger gains a
    `hold` claim -- the tallies of everything but the seat's pairing are the death's own."""
    w = _tiny("total")
    assert not w.seat_holds(KILLER)
    out, _ = _fight(w, HOLDER, KILLER, _felled(KILLER, HOLDER))
    assert KILLER not in w.persons, "fixture: the planted death did not happen"
    kinds = [e.kind for e in out]
    assert "person.died" in kinds and CLOSED not in kinds, kinds
    checked = 0
    for pid in w.persons:
        assert not [c for c in w.persons[pid].ledger if c.predicate == HOLD]
        checked += 1
    assert checked >= 3
