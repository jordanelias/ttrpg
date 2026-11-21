"""G1a -- the act store, the receipt mint, and the two things the log refuses.

These are the unit's FALSIFIERS, and each is written to go red if the mechanism is decorative
rather than working. The plan states two by name:

  OBSERVABLE  "A hand-built receipt in an Event fails `append`; the same Event with a
              gate-minted receipt passes."
  FALSIFIER   "An act-caused Event appended while the act store is EMPTY must fail; if it
              passes, the assertion is not reading the store."

Both are below, plus the controls that stop each from passing vacuously.
"""
import pytest

from engine.season.gaps import Forbidden, Unspecified
from engine.season.state.acts import ActStore
from engine.season.state.carriers import Act, Event, Receipt, StateChange
from engine.season.state.gate import Gate
from engine.season.state.ids import ROOT
from engine.season.state.log import EventLog


# B03.57: the log refuses a kind no column declares, so this file's one kind is declared to each bare
# `EventLog` it builds, through the roster parameter (`kinds`) a `World` hands in.
TEST_KINDS = frozenset({"test.kind"})


def _ev(eid, causes, changes=None):
    return Event(id=eid, kind="test.kind", changes=changes or [],
                 causes=list(causes), emitted_at=1)


# -- the act store ----------------------------------------------------------------------

def test_the_act_store_is_append_only_and_refuses_a_duplicate_id():
    s = ActStore()
    a = Act(id="a1", actor="p1", verb="speak")
    s.append(a)
    assert "a1" in s and len(s) == 1 and s.get("a1") is a

    with pytest.raises(Unspecified):
        s.append(Act(id="a1", actor="p2", verb="tell"))
    # the refusal did not half-apply: the first act is still the one on the id
    assert s.get("a1") is a and len(s) == 1


def test_iterating_the_act_store_cannot_reach_its_backing_list():
    """`list(store)` must be a COPY. If it aliases the store, append-only is spellable around
    in one line, and the property is a comment rather than a mechanism."""
    s = ActStore()
    s.append(Act(id="a1", actor="p1", verb="speak"))
    got = list(s)
    got.append(Act(id="forged", actor="x", verb="y"))
    assert len(s) == 1 and "forged" not in s


def test_the_act_store_refuses_a_non_act():
    with pytest.raises(Unspecified):
        ActStore().append(_ev("e1", [ROOT]))


# -- the mint ---------------------------------------------------------------------------

def test_the_gate_refuses_to_mint_with_no_write_open():
    """A receipt asserts THE GATE WROTE THIS. With no write open there is nothing to assert."""
    g = Gate()
    assert not g.is_open
    with pytest.raises(Forbidden):
        g.mint("subj", "set", "ACTS", "field")


def test_a_minted_receipt_is_issued_and_a_hand_built_one_is_not():
    g = Gate()
    g.opening("Person", "body", "MATTER", 1)
    real = g.mint("p1", "set", "MATTER", "body")
    assert g.issued(real)

    # the unminted sentinel
    assert not g.issued(Receipt("p1", "set", "MATTER", "body"))
    # ⚠ AND A FORGERY CARRYING A REAL SERIAL. This is the assertion that makes `issued` an
    # IDENTITY check rather than an equality one: the forgery below is `==` to `real` on every
    # field, so an `==`-based check would admit it.
    forged = Receipt("p1", "set", "MATTER", "body", serial=real.serial)
    assert forged == real
    assert not g.issued(forged)


def test_closing_the_window_stops_the_mint():
    g = Gate()
    g.opening("Person", "body", "MATTER", 1)
    g.mint("p1", "set", "MATTER", "body")
    g.close()
    with pytest.raises(Forbidden):
        g.mint("p1", "set", "MATTER", "body")


# -- the log: OBSERVABLE ------------------------------------------------------------------

def test_a_hand_built_receipt_fails_append_and_a_minted_one_passes():
    """The plan's OBSERVABLE, both arms, on one log."""
    g = Gate()
    log = EventLog(g, TEST_KINDS)

    with pytest.raises(Forbidden):
        log.append(_ev("e1", [ROOT], [Receipt("p1", "set", "MATTER", "body")]))
    assert len(log) == 0

    g.opening("Person", "body", "MATTER", 1)
    log.append(_ev("e1", [ROOT], [g.mint("p1", "set", "MATTER", "body")]))
    assert len(log) == 1


def test_a_bare_statechange_is_refused_and_the_event_is_not_logged():
    """B09.09 (H-145): THE SEAM THIS TEST USED TO PIN OPEN IS CLOSED. It asserted a bare
    `StateChange` was ADMITTED, and said it would go red when the log refused one; it is inverted
    here. The assertion can fail: were a bare change accepted, `pytest.raises` would not see a
    `Forbidden` and `len(log) == 0` would read 1. Controls: the same Event with a minted receipt is
    admitted, and a bare change AFTER a good receipt in one Event is refused too, so the check
    reads every change and not the first."""
    g = Gate()
    log = EventLog(g, TEST_KINDS)

    with pytest.raises(Forbidden) as bare:
        log.append(_ev("e1", [ROOT], [StateChange("p1", "set", "MATTER", "body")]))
    assert "bare" in str(bare.value)
    assert len(log) == 0

    g.opening("Person", "body", "MATTER", 1)
    good = g.mint("p1", "set", "MATTER", "body")
    with pytest.raises(Forbidden):
        log.append(_ev("e2", [ROOT], [good, StateChange("p1", "set", "MATTER", "body")]))
    assert len(log) == 0

    log.append(_ev("e3", [ROOT], [good]))                  # control: the minted receipt passes
    assert len(log) == 1


def test_the_probes_apparatus_changes_are_receipts_the_world_gate_issued():
    """The probes' one source of a hand-built change (`about`, and `apparatus_receipt` for the
    `alter` an act declares) mints on the world's own gate, closes its window, and the log admits it;
    a bare change of the same shape is refused on the same world."""
    from engine.season.data.verbs import EVENT_KINDS
    from engine.season.harness import probes as P
    kind = sorted(EVENT_KINDS)[0]
    w = P.tiny_world()
    r = P.about(w, "p_low")
    assert isinstance(r, Receipt) and w.gate.issued(r) and not w.gate.is_open
    assert (r.subject, r.mode, r.driver, r.field, r.delta) == ("p_low", "set", "Event", None, None)
    w.log.append(Event(id="e_ap", kind=kind, changes=[r], causes=[ROOT], emitted_at=w.tick))
    assert len(w.log) == 1
    with pytest.raises(Forbidden):
        w.log.append(Event(id="e_bare", kind=kind, changes=[StateChange("p_low", "set", "Event")],
                           causes=[ROOT], emitted_at=w.tick))
    assert len(w.log) == 1


# -- the log: FALSIFIER -------------------------------------------------------------------

def test_an_act_caused_event_fails_while_the_act_store_is_empty():
    """The plan's FALSIFIER. 'If it passes, the assertion is not reading the store.'"""
    store = ActStore()
    log = EventLog(Gate(), TEST_KINDS, lambda: store.ids())

    with pytest.raises(Forbidden):
        log.append(_ev("e1", ["act_1"]))
    assert len(log) == 0

    # and the SAME event passes once the act is in the store -- the control that stops the
    # assertion above from passing for any reason other than the one claimed
    store.append(Act(id="act_1", actor="p1", verb="speak"))
    log.append(_ev("e1", ["act_1"]))
    assert len(log) == 1


def test_a_cause_naming_a_prior_event_resolves_and_an_invented_one_does_not():
    log = EventLog(Gate(), TEST_KINDS)
    log.append(_ev("e1", [ROOT]))
    log.append(_ev("e2", ["e1"]))
    with pytest.raises(Forbidden):
        log.append(_ev("e3", ["e_never_happened"]))
    assert len(log) == 2


def test_root_always_resolves():
    log = EventLog(Gate(), TEST_KINDS, lambda: frozenset())
    log.append(_ev("e1", [ROOT]))
    assert len(log) == 1


# -- the list surface the tree already depends on -------------------------------------------

def test_the_log_is_reversible_indexable_and_sized():
    """`world.py:625` does `reversed(self.log)` and `content_hash` folds it positionally. A
    log with only `__iter__` raises on `reversed`, and it would raise at RUNTIME in the clock
    chain rather than here."""
    log = EventLog(Gate(), TEST_KINDS)
    log.append(_ev("e1", [ROOT]))
    log.append(_ev("e2", ["e1"]))
    assert len(log) == 2
    assert [e.id for e in reversed(log)] == ["e2", "e1"]
    assert log[0].id == "e1" and log[-1].id == "e2"
    assert bool(log) is True and bool(EventLog(Gate(), TEST_KINDS)) is False
