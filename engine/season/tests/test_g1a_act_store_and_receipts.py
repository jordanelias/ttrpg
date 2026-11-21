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


# -- the receipt carries the value the gate saw (B09.10) ------------------------------------

def _write_one(w, subject, perform, *, field="body", kind="Person", **kw):
    """One `Change` through `World.write` with an ACTS token, returning its `(subject, receipt)` pairs."""
    from engine.season.data.matrix import WriteClass
    from engine.season.loop.driver import mint_token
    from engine.season.state.gate import Change
    return w.write(field, mint_token(w, WriteClass.ACTS), None, record_kind=kind, fieldname=field,
                   driver="Act", actor="p_low", change=Change((subject,), perform), **kw)


def test_receipt_delta_decodes_before_after_for_fields_subject():
    """B09.10, the planted 940 -> 1000 case: a `Change` raising one person's `body` from 940 to 1000
    gives a receipt whose `delta` is the (before, after) the gate read, each side decoded from the
    canonical reading `World.state_of` takes (`(True, <body>)`, `(False,)` for an absent entity).
    Falsifier: a fields-naming receipt with `delta is None`, which is what the gate minted before.
    Controls: the receipt still names the field and mode `set`; a whole-entity subject's delta stays
    `None` (no named attribute to decode); and the delta is encodable, so the Event carrying it
    folds into `content_hash` (the first reading of the delta was bytes, which `_canonical` refuses)."""
    from engine.season.data.matrix import Step
    from engine.season.data.verbs import EVENT_KINDS
    from engine.season.harness import probes as P
    from engine.season.state.gate import Subject
    w = P.tiny_world()
    w.step = Step.RESOLVE
    p = w.persons["p_mid"]
    p.body = 940

    def raise_it():
        p.body = 1000

    (subj, r), = _write_one(w, Subject.entity("persons", "p_mid", fields=("body",)), raise_it)
    assert isinstance(r, Receipt) and w.gate.issued(r)
    assert (r.subject, r.mode, r.driver, r.field) == ("p_mid", "set", "Act", "body")
    assert r.delta is not None, "a fields-naming receipt minted with no delta"
    before, after = r.delta
    assert (before, after) == ((True, 940), (True, 1000))

    # the control: a whole-entity subject names no attribute, so its delta is None (its mode is the next test's)
    (_, whole), = _write_one(w, Subject.entity("persons", "p_mid"), lambda: setattr(p, "body", 5))
    assert whole.mode == "set" and whole.delta is None

    # encodable: the receipt rides an Event and the world still hashes (it raised on a bytes delta)
    h0 = w.content_hash()
    w.log.append(Event(id="e_d", kind=sorted(EVENT_KINDS)[0], changes=[r], causes=[ROOT], emitted_at=w.tick))
    assert w.content_hash() != h0


def test_a_whole_entity_receipt_names_its_mode_and_a_fields_receipt_stays_set():
    """B09.10, `mode` told honestly for a whole-entity digest subject: `create` when it was absent,
    `delete` when it is absent after, else `set`. A subject naming `fields` keeps `set` even across
    a creation, its delta carrying the `(False,)` reading instead. Each arm is planted, so a
    constant `set` fails three of the four assertions."""
    from engine.season.data.matrix import Step, WriteClass
    from engine.season.harness import probes as P
    from engine.season.loop.driver import mint_token
    from engine.season.state.carriers import Rung
    from engine.season.state.gate import Change, Subject
    w = P.tiny_world()
    w.step = Step.MATTER

    def at_matter(subject, perform):
        return w.write("stores", mint_token(w, WriteClass.MATTER), None, record_kind="Rung",
                       fieldname="stores", driver="MATTER", change=Change((subject,), perform),
                       emits="stores.changed", subject="r_new", causes=[ROOT])

    def make():
        w.rungs["r_new"] = Rung("r_new", "settlement", stores={"grain": 1})

    def unmake():
        del w.rungs["r_new"]

    def regrain():
        w.rungs["r_new"].stores = {"grain": 2}

    whole = Subject.entity("rungs", "r_new", earns="stores.changed")
    (_, created), = at_matter(whole, make)
    assert (created.mode, created.delta) == ("create", None)
    (_, set_), = at_matter(whole, regrain)
    assert (set_.mode, set_.delta) == ("set", None)
    (_, deleted), = at_matter(whole, unmake)
    assert (deleted.mode, deleted.delta) == ("delete", None)

    named = Subject.entity("rungs", "r_new", earns="stores.changed", fields=("stores",))
    (_, born), = at_matter(named, make)
    assert born.mode == "set" and born.delta[0] == (False,) and born.delta[1][0] is True


def test_every_minted_receipt_is_in_an_event(monkeypatch):
    """B09.10 (red until B09.11 BY DESIGN): every receipt the world's gate minted sits in some Event of
    the log. The scene is `test_h11_affiliation_scar`'s -- a fight observed by persons whose
    holdings the rebound engagement table says it violates -- and its `(Person, scar)` write mints a
    receipt per scarred observer with NO `emits`, so they land in no Event (the `_scar_witnesses`
    docstring says "Nothing is emitted"). The fold's Events are appended as the driver does
    (`loop/driver.py`, S19.5). It can observe what it excludes: the scar receipts are asserted
    minted first, and the control is that every OTHER minted receipt is logged."""
    from engine.season.data import affiliations as A
    from engine.season.data.matrix import Step
    from engine.season.data.rosters import AFFILIATIONS
    from engine.season.harness import probes as P
    from engine.season.state.carriers import Tenure
    from engine.substrate.descriptors import AFFILIATION_CEILING
    from ._scar_helpers import fight, rebound
    holding = {a: AFFILIATION_CEILING for a in sorted(AFFILIATIONS)[:2]}
    monkeypatch.setattr(A, "ENGAGEMENT", rebound(**{A.SHARED_COLUMN: {"fight": -0.3}}))
    w = P.tiny_world()
    for q in w.persons.values():
        q.pursuits = {}
        q.conviction = dict(holding)
    w.add_tenure(Tenure("t_g1a_knot", "p_low", "p_high", "knot", since=0))
    w.step = Step.RESOLVE
    w.acts.append(Act(id="g1a_fight", actor="p_low", verb="fight", payload={"subject": "p_mid"}))
    for e in fight(w, "g1a_fight"):
        w.log.append(e)
    minted = list(w.gate._minted.values())
    scar = [r for r in minted if r.field == "scar"]
    assert scar, "no scar receipt was minted, so the assertion below would be vacuous"
    logged = {id(c) for e in w.log for c in e.changes}
    unlogged = [r for r in minted if id(r) not in logged]
    assert {r.field for r in minted} - {"scar"}, "the control has nothing but scar receipts in it"
    assert not [r for r in unlogged if r.field != "scar"], "a non-scar receipt is in no Event too"
    assert not unlogged, (f"{len(unlogged)} of {len(minted)} minted receipts are in no Event: "
                          f"{sorted({(r.field, r.subject) for r in unlogged})}")


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
