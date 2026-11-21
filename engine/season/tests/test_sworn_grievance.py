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


# ======================================================================================================================
# B09.20 -- THE SWORN-TO HALF OF GRIEVANCE AT READ (IN-58's reader; lane D4; `sworn_bond`, H-459)
#
# `queries/person_q.py::_bond` is the judge's allegiance to a deed's PATIENT. A judge who holds a live, un-`imposed`
# `oblige` to a seat S AND whose own ledger holds B09.22's claim `(S, hold, patient)` is sworn to the patient: at
# `sworn_bond` b the allegiance `a` gains b before its clamp, and `deeds_judged`'s paired-deed term (`lean * bond`) moves.
# PERSON-SIDE: the tests below build a `Person` and read `regard` -- no World is read (AX-2).
# ======================================================================================================================
from ..data.rosters import PURSUITS, SEEN_PREDICATE      # noqa: E402
from ..data.pursuits import to_axes                       # noqa: E402
from ..epistemic import Seen                              # noqa: E402
from ..queries import person_q as PQ                      # noqa: E402
from ..state.carriers import Claim                        # noqa: E402

V_SEAT = OFFICE                       # the victim's seat S
VICTIM, DOER = HOLDER, KILLER         # the patient and the hand `deed_doer` pairs to the death


def _condemning_pursuit(kind="person.died"):
    """A pursuit whose lean on `kind` is NEGATIVE, so the patient's allegiance (`_bond` = 1 + a) moves the term."""
    for e in sorted(PURSUITS):
        if PQ._lean(to_axes({e: 1.0}), kind) < 0:
            return e
    raise AssertionError(f"no pursuit condemns {kind!r}: allegiance could not be shown to matter")


def _judge(pid, *, oath=False, imposed=False, closed=False, hold_claim=True, hold_value=VICTIM, hold_seat=V_SEAT,
           oath_seat=V_SEAT, stance=()):
    """A judge with the death's two ordinary claims -- `(victim, person.died, True)` and the sighting naming the killer
    (so `deed_doer` pairs it) -- and, where asked: the `oblige` Tenure sworn to `oath_seat` (`imposed`: a sentence;
    `closed`: no longer live), B09.22's claim `(hold_seat, hold, hold_value)`. Pursuits and stance are the same for
    every judge built here, whatever else differs."""
    p = Person(pid, pid)
    p.pursuits = {_condemning_pursuit(): 1.0}
    p.stance = list(stance)
    p.ledger = [
        Claim(f"c_died_{pid}", pid, VICTIM, "person.died", True, 0, "firsthand", 100, "own", 0),
        Claim(f"c_seen_{pid}", pid, VICTIM, SEEN_PREDICATE,
              Seen(stratum="contested_physical", marks=(), who=DOER), 0, "firsthand", 100, "own", 0),
        # the seat's own `tenure.closed`, deposited at the same `when` and `lap` as the death: a pairing nobody may guess
        Claim(f"c_closed_{pid}", pid, V_SEAT, "tenure.closed", True, 0, "firsthand", 100, "own", 0),
    ]
    if hold_claim:
        p.ledger.append(Claim(f"c_hold_{pid}", pid, hold_seat, HOLD, hold_value, 0, "firsthand", 100, "own", 0))
    if oath:
        t = Tenure(f"t_oath_{pid}", pid, oath_seat, "oblige", 0)
        if imposed:
            t.payload = {"determined_by": "a_determination"}
        if closed:
            t.until = 1
        p.tenures.append(t)
    return p


def _regard_of_the_killer(p, b):
    fx = DEFAULT_FIXTURES.sweep("sworn_bond", b)
    return PQ.regard(p, DOER, fx)


def test_a_sworn_judge_reads_the_killer_differently():
    """THE ENTRY'S FALSIFIER: two judges with EQUAL stance and pursuits, one sworn to the victim's seat (a live oblige
    on S, and the ledger claim `(S, hold, victim)`), read DIFFERENT regard for the killer at `sworn_bond` 0.5 -- and the
    oath weighs as the victim's ally does: a condemned death condemns the killer the more."""
    sworn, unsworn = _judge("j_sworn", oath=True), _judge("j_free")
    assert sworn.pursuits == unsworn.pursuits and sworn.stance == unsworn.stance
    for b in (0.5, 1.0):
        s, u = _regard_of_the_killer(sworn, b), _regard_of_the_killer(unsworn, b)
        assert s < u < 0, (b, s, u)
    # the oath is a sum before the clamp: 0.5 then 1.0 move it further, and 1.0 doubles the condemnation (a = 1)
    r0, r5, r10 = (_regard_of_the_killer(sworn, b) for b in (0.0, 0.5, 1.0))
    assert r10 < r5 < r0
    # and the same claims, unsworn, are what the control reads: the oath is what moved it
    assert _regard_of_the_killer(unsworn, 0.5) == r0


def test_sworn_bond_zero_is_todays_regard():
    """The CONTROL: at the shipped `sworn_bond` (0.0, "it ships OFF") the sworn judge reads exactly what the unsworn
    one reads, and exactly what the same judge reads with the oath and the claim removed -- `_bond` adds nothing."""
    assert DEFAULT_FIXTURES.get("sworn_bond") == 0.0
    sworn, unsworn = _judge("j_sworn", oath=True), _judge("j_free")
    bare = _judge("j_bare", hold_claim=False)
    fx = DEFAULT_FIXTURES
    assert PQ.regard(sworn, DOER, fx) == PQ.regard(unsworn, DOER, fx) == PQ.regard(bare, DOER, fx) != 0.0
    assert PQ.deeds_judged(sworn, DOER) == PQ.deeds_judged(sworn, DOER, sworn_bond=0.0) == PQ.deeds_judged(bare, DOER)
    assert PQ.deeds_judged(sworn, DOER, sworn_bond=0.5) != PQ.deeds_judged(sworn, DOER)


def test_a_sworn_judge_with_no_claim_naming_the_victim_in_the_seat_does_not_move():
    """THE ITEM'S FALSIFIER: the pairing is the CLAIM `(S, hold, victim)`, never a shared `when`/`lap` (`deed_doer` does
    not guess). Every judge below holds the death, the sighting and the seat's `tenure.closed` at one `when` and `lap`,
    and each lacks one of the sworn arm's conditions; each must read what an unsworn judge reads at `sworn_bond` 1.0."""
    control = _regard_of_the_killer(_judge("j_free"), 1.0)
    assert control == _regard_of_the_killer(_judge("j_free"), 0.0), "fixture: the control must not read the arm"
    cases = {
        "no hold claim at all":                      _judge("a", oath=True, hold_claim=False),
        "a hold claim in another seat":              _judge("b", oath=True, hold_seat="off_other"),
        "a hold claim naming another holder":        _judge("c", oath=True, hold_value="p_someone_else"),
        "an oath to another seat":                   _judge("d", oath=True, oath_seat="off_other"),
        "an imposed oblige (a sentence, no oath)":   _judge("e", oath=True, imposed=True),
        "an oath no longer live":                    _judge("f", oath=True, closed=True),
        "the claim and no oath":                     _judge("g", oath=False),
    }
    checked = 0
    for name, judge in cases.items():
        assert _regard_of_the_killer(judge, 1.0) == control, f"{name}: the sworn arm read without its conditions"
        checked += 1
    assert checked == len(cases)
    # and the case that satisfies them moves, so the loop above could have failed
    assert _regard_of_the_killer(_judge("h", oath=True), 1.0) != control


def test_the_oath_scales_only_the_paired_term_and_never_the_stored_stance():
    """The entry's LIMITS: the arm only scales a paired deed -- a judge whose pursuits do not lean on the death has no
    term for it to scale -- and the stored stance half is untouched at any `sworn_bond`."""
    inert = _judge("j_inert", oath=True, stance=[(VICTIM, 3, 2)])
    inert.pursuits = {}
    assert PQ.deeds_judged(inert, DOER, sworn_bond=1.0) == (0.0, 0.0)
    assert PQ.stance_toward(inert, VICTIM) == 6.0
    sworn = _judge("j_sworn", oath=True)
    assert PQ.stance_toward(sworn, DOER) == 0.0
    assert PQ.stance_toward(sworn, VICTIM) == 0.0
