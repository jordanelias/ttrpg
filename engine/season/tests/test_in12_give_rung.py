"""v9 IN-12 `give` + Rung (#453 §9.6) -- a CESSION: a rung `hold` changes hands by `give`.

The entry's falsifier, verbatim: *"a rung `hold` changes hands by `give`"*. Every test drives the act
through the REAL fold (`SeasonDriver._fold`, the gate, the Event log) on a HAND-BUILT world
(`probes.tiny_world`, a settlement `S` the giver is made the holder of). Each claim has a control one
change away, so the cause is the widened object and nothing else:

  * the cession executes: the donor's `hold` on the rung closes, the receiver's opens, in ONE write, and
    the Event is `rung.ceded` (never `record.given`, which a handed Record still earns);
  * what is NOT the actor's to cede is refused (`give.refused`, nothing moves): a rung somebody else
    holds, a rung nobody holds, a seat (the gate's `handover` is for non-seat holds), a receiver who is
    not present;
  * the loosened cell still forms only on what a person holds (`own_hold_declines`).
"""
import pytest

from engine.season.data.matrix import Step, WriteClass
from engine.season.data.verbs import OWN_HOLD_DECLINES, VERB_TABLE
from engine.season.harness import probes as P
from engine.season.loop.driver import SeasonDriver, mint_token
from engine.season.queries.world_q import hold_force
from engine.season.state.carriers import Act, Tenure

GIVER, RECEIVER, FAR, OTHER = "p_low", "p_mid", "p_high", "p_other"
RUNG = "S"                       # `tiny_world`'s settlement; p_high lives there, p_low and p_mid in `Hh`


def _world(holder=GIVER):
    """`tiny_world` at a RESOLVE barrier, `holder` the live holder of the settlement `S` (a seeded
    `hold` on a rung, as the realm's territories are held)."""
    w = P.tiny_world()
    d = SeasonDriver(w)
    d.matter(mint_token(w, WriteClass.MATTER), [])
    w.step = Step.RESOLVE
    if holder is not None:
        w.add_tenure(Tenure("hold_S", holder, RUNG, "hold", since=0))
    return w, d


def _give(w, d, obj, to, actor=GIVER, key="g"):
    return d._fold(w, mint_token(w, WriteClass.ACTS),
                   Act(id=f"give_{key}", actor=actor, verb="give", payload={"subject": obj, "to": to}))


def test_a_rung_hold_changes_hands_by_give_and_the_event_is_named():
    """THE ENTRY'S FALSIFIER: the receiver holds the rung, the donor's edge is closed AT the cession, and
    the diff is exactly those two edges."""
    w, d = _world()
    assert hold_force(w, RUNG).subject == GIVER, "fixture: the giver does not hold the rung"
    snap = w._tenure_snapshot()
    out = _give(w, d, RUNG, RECEIVER)
    assert [e.kind for e in out] == ["rung.ceded"], [e.kind for e in out]
    assert hold_force(w, RUNG).subject == RECEIVER, "the rung `hold` did not change hands"
    donor = next(t for t in w.tenures if t.id == "hold_S")
    assert donor.until == w.tick and not donor.live, "the donor's hold was not closed at the cession"
    diff = w._tenure_changes(snap)
    closed = [(t.subject, t.object) for t, was in diff if was is not None]
    opened = [(t.subject, t.object) for t, was in diff if was is None]
    assert closed == [(GIVER, RUNG)] and opened == [(RECEIVER, RUNG)], diff
    assert sum(1 for t in w.tenures if t.kind == "hold" and t.object == RUNG and t.live) == 1, (
        "two live holders: the cession was not one write")
    # the Event names the Rung's tenures, and a handed RECORD still earns the other kind
    ev = [e for e in w.log if e.kind == "rung.ceded"] or out
    assert all(e.kind != "record.given" for e in out)
    assert ev


def test_control_the_giver_who_does_not_hold_the_rung_cedes_nothing():
    """One change from the cession: somebody else holds the rung. Refused, nothing moves."""
    w, d = _world(holder=OTHER)
    snap = w._tenure_snapshot()
    assert [e.kind for e in _give(w, d, RUNG, RECEIVER)] == ["give.refused"]
    assert hold_force(w, RUNG).subject == OTHER and not w._tenure_changes(snap)


def test_control_a_rung_nobody_holds_is_not_ceded():
    w, d = _world(holder=None)
    assert hold_force(w, RUNG) is None, "fixture: the rung is held"
    assert [e.kind for e in _give(w, d, RUNG, RECEIVER)] == ["give.refused"]
    assert hold_force(w, RUNG) is None


def test_control_a_receiver_who_is_not_present_is_refused():
    """The row's `with` conjunct is unchanged by the widening: `p_high` stands in `S`, not in `Hh`."""
    w, d = _world()
    assert [e.kind for e in _give(w, d, RUNG, FAR)] == ["give.refused"]
    assert hold_force(w, RUNG).subject == GIVER


def test_a_seat_is_still_not_ceded_by_give():
    """The object's kind is the effect's now: a seat is neither a Record nor a Rung. `p_high` holds
    `off_duke`; a `give` of it to a person standing with him is refused and the seat does not move."""
    w, d = _world()
    for t in w.tenures:                                                     # OTHER moves to stand with p_high
        if t.kind == "contain" and t.subject == OTHER and t.live:
            t.until = w.tick
    w.add_tenure(Tenure("t_close", OTHER, "S", "contain", since=0))
    holder = hold_force(w, "off_duke").subject
    assert holder == FAR
    out = _give(w, d, "off_duke", OTHER, actor=FAR, key="seat")
    assert [e.kind for e in out] == ["give.refused"], [e.kind for e in out]
    assert hold_force(w, "off_duke").subject == FAR


def test_a_handed_record_still_earns_record_given_not_rung_ceded():
    """The widening does not move the Record half: the same verb on a Record is `record.given`."""
    from engine.season.tests.test_give import GIVER as G0, RECEIVER as R0, _at_resolve, _give as _g
    w, d, rid = _at_resolve()
    assert [e.kind for e in _g(w, d, rid, R0)] == ["record.given"]
    assert hold_force(w, rid).subject == R0 and G0 != R0


def test_the_loosened_cell_forms_only_on_what_a_person_holds():
    """The cell no longer asks the object's kind, so the person-side `held_by` reading
    (`own_hold_declines`) is what keeps a gift of an unheld referent from forming. Control: the cell
    still binds `held_by` of `subject` (the loader refuses the roster member otherwise)."""
    assert "give" in OWN_HOLD_DECLINES
    row = VERB_TABLE["give"]
    assert row.emits == ("record.given", "rung.ceded"), row.emits
    assert row.requires_typed.known_person_operands() == ("to",)
