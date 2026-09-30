"""Plan position 16 (≡ `15a`) -- `give`, THE `H-84` VERB, AND THE GATE'S SIXTH BASIS, `handover`.

What each block proves, and the control that stops it passing vacuously:

  1. THE ROW. `give` is a verb with a registered predicate and an effect, so `resolvable_verbs()`
     carries it; the derived opener map sees it open `hold`; its refusal kind is its own.
  2. THE OBSERVABLE, THROUGH THE REAL FOLD. A `give` between two co-located people closes the
     giver's `hold` and opens the receiver's in ONE write -- the tenure store's diff is exactly
     those two edges -- and `hold_force` (the plan's `holder_of`) moves. The previous holder's
     `document_key` channel stops firing for the Record and the receiver's starts; control: the
     same question asked before the handover answers the other way round.
  3. THE PLAN'S FALSIFIER (*the receiver's claim about the Record predates the transfer -- the
     witness read the old holder*). The receiver's `content:<kind>` claim is minted in the season
     of the handover, with the giver's exact value, and did not exist the season before. Control:
     with WITNESS's deposit trigger reading receipts as they stand (not through the `hold`), the
     receiver learns nothing -- so the trigger's widening is what delivers it.
  4. r2 `05:1246`'s CONTROL, CONSTRUCTED AT THE GATE rather than trusted to the effect's own
     close-then-open: a write that opens the receiver's `hold` WITHOUT the release is `NotYours` and
     put back (and, planted around the gate, two live holders make `hold_force` raise); the same
     write WITH the release is admitted under `handover`; a release in an EARLIER write licenses
     nothing; one release hands on ONE edge; a seat cannot be handed over; and a closure that is
     not the actor's own licenses nothing.
  5. THE PRECONDITION. A non-co-located `give` is refused (control: the co-located one executes);
     so is a give to oneself, of something not held, and one naming no receiver.
  6. NO PERSON FORMS A GIFT WITH NO RECEIVER. The row is untyped, so no Candidate can carry `to`,
     and its `counterparty: to` makes `opening_set` form none. Control: with the column cleared the
     receiver-less Candidates form -- the scene tax measured before the column (3 in `headless`,
     41 in `populated`, all refused). The loader still refuses a counterparty that is no operand.
"""
import dataclasses

import pytest

from engine.season.data import verbs as _verbs
from engine.season.data.matrix import Step, WriteClass
from engine.season.data.rosters import RECORD_CONTENT
from engine.season.data.verbs import _OPENERS_FROM_EFFECTS, VERB_TABLE
from engine.season.decision.options import opening_set
from engine.season.epistemic import CHANNEL_PREDICATES
from engine.season.gaps import Forbidden
from engine.season.harness import probes as P
from engine.season.loop import witness as _witness
from engine.season.loop.driver import SeasonDriver, mint_token, resolvable_verbs
from engine.season.loop.predicates import REQUIRES_PREDICATES
from engine.season.queries.world_q import hold_force
from engine.season.state import gate as G
from engine.season.state.carriers import Act, Question, Tenure, View
from engine.season.state.gate import HANDOVER, T_M, Change, NotYours, Subject

_CONTENT = RECORD_CONTENT["predicate"]
GIVER, RECEIVER, FAR = "p_low", "p_mid", "p_high"      # `tiny_world`: p_low, p_mid in Hh; p_high in S


def _content_claims(w, pid, rid):
    return [c for c in w.persons[pid].ledger
            if c.subject == rid and str(c.predicate).startswith(f"{_CONTENT}:")]


def _at_resolve(events=None):
    """`tiny_world` at a RESOLVE barrier, with `p_low` holding a fresh `petition` Record (content
    `{terms, to, from}`) minted through the real fold. Returns `(w, d, rid)`; the filing's Events
    are appended to `events` when a list is passed (`_fold` returns them, it does not log them)."""
    w = P.tiny_world()
    d = SeasonDriver(w)
    d.matter(mint_token(w, WriteClass.MATTER), [])
    w.step = Step.RESOLVE
    out = d._fold(w, mint_token(w, WriteClass.ACTS),
                  Act(id="pet", actor=GIVER, verb="petition",
                      payload={"record": "rec_pet", "subject": RECEIVER, "to": RECEIVER,
                               "from": "Hh"}))
    assert [e.kind for e in out] == ["petition.filed"], [e.kind for e in out]
    assert hold_force(w, "rec_pet").subject == GIVER, "fixture: the petitioner does not hold it"
    if events is not None:
        events.extend(out)
    return w, d, "rec_pet"


def _give(w, d, rid, to, actor=GIVER, key="g"):
    return d._fold(w, mint_token(w, WriteClass.ACTS),
                   Act(id=f"give_{key}", actor=actor, verb="give",
                       payload={"subject": rid, **({"to": to} if to is not None else {})}))


def _holds_on(w, rid):
    return [t for t in w.tenures if t.kind == "hold" and t.object == rid]


# ======================================================================================
# 1 -- THE ROW
# ======================================================================================

def test_give_is_a_resolvable_verb_that_opens_hold_and_refuses_as_itself():
    row = VERB_TABLE["give"]
    assert row.eligibility == ("own", "hold:<record>"), row.eligibility
    assert row.writes == ("Tenure.until", "Tenure.since"), row.writes
    assert row.emits == ("record.given",) and row.emits_on_refusal == ("give.refused",)
    assert row.requires_typed is None and "give" in REQUIRES_PREDICATES, (
        "`give` must take `release`'s route: an untyped cell read by a registered predicate")
    assert "give" in resolvable_verbs()
    assert "give" in _OPENERS_FROM_EFFECTS["hold"], _OPENERS_FROM_EFFECTS["hold"]
    # NOT A KIND ANY BROADCAST CHANNEL READS: `chronicle` keys on `binding_decision` rows and
    # `post_remit` on `remit:` rows, by the kinds those rows emit.
    assert row.stratum != "binding_decision"
    assert not any("record.given" in r.emits for v, r in VERB_TABLE.items() if v != "give")


# ======================================================================================
# 2 -- THE OBSERVABLE: THE HOLD MOVES, IN ONE WRITE, AND THE CHANNEL FOLLOWS IT
# ======================================================================================

def test_a_give_closes_the_givers_hold_and_opens_the_receivers_in_one_write():
    w, d, rid = _at_resolve()
    snap = w._tenure_snapshot()
    out = _give(w, d, rid, RECEIVER)
    assert [e.kind for e in out] == ["record.given"], [e.kind for e in out]
    diff = w._tenure_changes(snap)
    closed = [(t.subject, t.object) for t, was in diff if was is not None]
    opened = [(t.subject, t.object) for t, was in diff if was is None]
    assert closed == [(GIVER, rid)] and opened == [(RECEIVER, rid)], diff
    assert hold_force(w, rid).subject == RECEIVER, "`holder_of(record)` did not move"
    giver_edge = next(t for t in _holds_on(w, rid) if t.subject == GIVER)
    assert giver_edge.until == w.tick, "the giver's hold was not closed AT the handover"
    assert sum(t.live for t in _holds_on(w, rid)) == 1, "two live holders after a give"
    # the receipts name the two EDGES, never the Record (`_eff_confer`'s rule on receipts)
    assert {c.subject for c in out[0].changes} == {t.id for t, _ in diff}, out[0].changes


def test_the_previous_holders_document_key_stops_firing_and_the_receivers_starts():
    events = []
    w, d, rid = _at_resolve(events)
    filed = events[0]
    assert rid in {c.subject for c in filed.changes}, "the filing Event does not name the Record"
    doc = CHANNEL_PREDICATES["document_key"]
    # CONTROL: before the handover the channel is the giver's and not the receiver's
    assert doc(w, filed, GIVER) and not doc(w, filed, RECEIVER)
    _give(w, d, rid, RECEIVER)
    assert not doc(w, filed, GIVER), "the previous holder's channel still fires for the Record"
    assert doc(w, filed, RECEIVER), "the new holder's channel does not fire for the Record"


# ======================================================================================
# 3 -- THE PLAN'S FALSIFIER: THE RECEIVER LEARNS THE DOCUMENT AT THE HANDOVER, NOT BEFORE
# ======================================================================================

def _two_seasons(w):
    """Season 1: `p_low` petitions `p_mid` (a Record with content, held by `p_low`). Season 2:
    `p_low` gives it to `p_mid`, who stands in the same hearth. Returns `(rid, t_mint, t_give,
    receiver's content claims after season 1)`."""
    seen = {}

    def choose(p, v, s, ask_budget):
        if p.id != GIVER:
            return []
        if w.tick == seen.setdefault("t_mint", w.tick):
            # ⚠ ONE STAGE, DUE FAR AWAY: the default stage clock matures a term the season after
            # the mint, and `term.matured` names the Record in `changes[]` -- which would hand the
            # new holder the content through the Record's own id and let the control below pass
            # without observing the handover's receipts at all (found by that control failing).
            return [P.Act_(w, p, "petition",
                           payload={"record": "rec_s", "subject": RECEIVER, "to": RECEIVER,
                                    "from": "Hh", "stages": [(w.tick + 50, "stage1", "t")]})]
        seen["t_give"] = w.tick
        return [P.Act_(w, p, "give", payload={"subject": "rec_s", "to": RECEIVER})]
    d = SeasonDriver(w)
    d.season(choose, question=None, subsistence=P.SUBSIST)
    before = list(_content_claims(w, RECEIVER, "rec_s"))
    d.season(choose, question=None, subsistence=P.SUBSIST)
    return "rec_s", seen["t_mint"], seen["t_give"], before


def test_the_receivers_content_claim_is_minted_at_the_handover_and_not_before():
    w = P.tiny_world()
    rid, t_mint, t_give, before = _two_seasons(w)
    assert t_give > t_mint, (t_mint, t_give)
    assert "record.given" in [e.kind for e in w.log], [e.kind for e in w.log][-20:]
    assert not before, f"the receiver held the document's content before it was given: {before}"
    got = _content_claims(w, RECEIVER, rid)
    assert len(got) == 1, got
    assert got[0].when == t_give, (
        f"the receiver's content claim is dated {got[0].when}, the handover was {t_give} -- a claim "
        "that predates the transfer means the witness read the OLD holder")
    giver = _content_claims(w, GIVER, rid)
    assert len(giver) == 1 and giver[0].when == t_mint, giver
    assert got[0].value == giver[0].value and got[0].predicate == giver[0].predicate, (
        "the receiver does not hold the giver's exact reading of the document")
    assert got[0].source.startswith("firsthand"), got[0].source


def test_control_without_reading_through_the_hold_the_receiver_learns_nothing(monkeypatch):
    """The deposit trigger read `changes[]` as Record ids before this position; `give`'s receipts
    name the two custody edges. Undo the widening and the receiver's belief never forms -- so the
    test above observes the widening and not some other path."""
    monkeypatch.setattr(_witness, "_hold_tenure_ends", lambda w, subject: (subject,))
    w = P.tiny_world()
    rid, _t_mint, _t_give, _before = _two_seasons(w)
    assert hold_force(w, rid).subject == RECEIVER, "the handover itself did not happen"
    assert not _content_claims(w, RECEIVER, rid)


# ======================================================================================
# 4 -- THE GATE: RELEASE-BEFORE-MINT IS ITS CONDITION, CONSTRUCTED RATHER THAN TRUSTED
# ======================================================================================

def _gate_write(w, actor, apply, subjects=()):
    """A bare gate write carrying a hand-built `Change` -- nothing but the gate is asked."""
    return w.write("Tenure", mint_token(w, WriteClass.ACTS), None, record_kind="Tenure",
                   fieldname="until", driver="Act", actor=actor, via=None,
                   change=Change(tuple(subjects), apply))


def _new_hold(w, who, rid, tag):
    return Tenure(f"t_{tag}", who, rid, "hold", since=w.tick)


def test_a_give_without_the_release_is_notyours_and_put_back():
    w, _d, rid = _at_resolve()
    nt = _new_hold(w, RECEIVER, rid, "norelease")
    with pytest.raises(NotYours) as refused:
        _gate_write(w, GIVER, lambda: w.add_tenure(nt), [Subject.edge(nt)])
    assert refused.value.where == "F3", refused.value.where
    assert nt not in w.tenures, "the refused edge was left standing"
    assert hold_force(w, rid).subject == GIVER, "the giver lost the Record to a refused write"
    # THE HALF THE GATE PREVENTS, PLANTED AROUND IT: two live holders and the owner of *who holds
    # this* refuses to choose. This is what a gate without the basis's condition would ship.
    w.add_tenure(_new_hold(w, RECEIVER, rid, "planted"))
    with pytest.raises(Forbidden, match="2 live `hold` Tenures"):
        hold_force(w, rid)


def test_control_the_same_write_with_the_release_is_admitted_under_handover(monkeypatch):
    w, _d, rid = _at_resolve()
    old = hold_force(w, rid)
    nt = _new_hold(w, RECEIVER, rid, "withrelease")
    bases = []
    real = G.tenure_write_basis

    def spy(*a, **k):
        b = real(*a, **k)
        bases.append((a[1].id, b))
        return b
    monkeypatch.setattr(G, "tenure_write_basis", spy)

    def apply():
        old.until = w.tick
        w.add_tenure(nt)
    _gate_write(w, GIVER, apply, [Subject.edge(nt), Subject.edge(old)])
    assert hold_force(w, rid) is nt
    final = dict(bases)                      # the LAST verdict per edge id is the one that stood
    assert final[old.id] == T_M and final[nt.id] == HANDOVER, bases


def test_a_release_in_an_earlier_write_licenses_nothing_in_a_later_one():
    w, _d, rid = _at_resolve()
    old = hold_force(w, rid)
    _gate_write(w, GIVER, lambda: setattr(old, "until", w.tick), [Subject.edge(old)])
    assert hold_force(w, rid) is None, "control: the release itself was not applied"
    nt = _new_hold(w, RECEIVER, rid, "later")
    with pytest.raises(NotYours):
        _gate_write(w, GIVER, lambda: w.add_tenure(nt), [Subject.edge(nt)])
    assert nt not in w.tenures


def test_one_release_hands_on_one_edge():
    w, _d, rid = _at_resolve()
    old = hold_force(w, rid)
    a, b = _new_hold(w, RECEIVER, rid, "a"), _new_hold(w, "p_other", rid, "b")

    def apply():
        old.until = w.tick
        w.add_tenure(a)
        w.add_tenure(b)
    with pytest.raises(NotYours) as refused:
        _gate_write(w, GIVER, apply, [Subject.edge(a), Subject.edge(b), Subject.edge(old)])
    msg = str(refused.value)
    # exactly ONE of the two openings is refused -- whichever the diff lists second
    assert ("t_a (" in msg) != ("t_b (" in msg), msg
    assert old.live and a not in w.tenures and b not in w.tenures, "the store was not put back"


def test_a_seat_cannot_be_handed_over():
    """`p_high` holds `off_duke`. Ending his own seat and opening `p_mid`'s in one write, with no
    seat exercised, is refused: a seat passes by its conferral basis, never by its holder. Control:
    the resignation alone is `T-m` and is admitted."""
    w, _d, _rid = _at_resolve()
    seat = hold_force(w, "off_duke")
    assert seat.subject == FAR, "fixture"
    nt = _new_hold(w, RECEIVER, "off_duke", "seat")

    def apply():
        seat.until = w.tick
        w.add_tenure(nt)
    with pytest.raises(NotYours):
        _gate_write(w, FAR, apply, [Subject.edge(nt), Subject.edge(seat)])
    assert seat.live and nt not in w.tenures
    _gate_write(w, FAR, lambda: setattr(seat, "until", w.tick), [Subject.edge(seat)])
    assert not seat.live, "control: the holder could not resign his own seat"


def test_a_closure_that_is_not_the_actors_own_licenses_nothing():
    """`p_other` ends `p_low`'s hold and opens `p_mid`'s: the closure is not `T-m` (the edge is
    somebody else's), so it licenses no `handover` -- both edges are refused, not only the one
    that had no basis of its own. (A third party is the actor so that the opened edge cannot pass
    as its opener's own: `T-m` admits a person opening a non-seat `hold` for THEMSELVES.)"""
    w, _d, rid = _at_resolve()
    old = hold_force(w, rid)
    nt = _new_hold(w, RECEIVER, rid, "taken")

    def apply():
        old.until = w.tick
        w.add_tenure(nt)
    with pytest.raises(NotYours) as refused:
        _gate_write(w, "p_other", apply, [Subject.edge(nt), Subject.edge(old)])
    msg = str(refused.value)
    assert f"{old.id} (" in msg and "t_taken (" in msg, msg
    assert old.live and hold_force(w, rid) is old


# ======================================================================================
# 5 -- THE PRECONDITION: CO-LOCATION, A SECOND PARTY, A HELD RECORD, A NAMED RECEIVER
# ======================================================================================

def test_a_non_co_located_give_is_refused_and_a_co_located_one_executes():
    w, d, rid = _at_resolve()
    assert w.persons[FAR] is not None
    out = _give(w, d, rid, FAR, key="far")
    assert [e.kind for e in out] == ["give.refused"], [e.kind for e in out]
    assert hold_force(w, rid).subject == GIVER and len(_holds_on(w, rid)) == 1
    # CONTROL: the same Record, to a person standing in the giver's hearth
    out = _give(w, d, rid, RECEIVER, key="near")
    assert [e.kind for e in out] == ["record.given"], [e.kind for e in out]


@pytest.mark.parametrize("to, actor", [
    (GIVER, GIVER),        # to oneself: no second party (ED-IN-0210 ruling 1)
    (RECEIVER, "p_other"), # by somebody who does not hold it
    (None, GIVER),         # no receiver named -- what a person-formed `give` would be until `15c`
    ("nobody", GIVER),     # a receiver who is no person
])
def test_the_precondition_refuses_what_is_not_a_give(to, actor):
    w, d, rid = _at_resolve()
    out = _give(w, d, rid, to, actor=actor, key=f"{actor}_{to}")
    assert [e.kind for e in out] == ["give.refused"], [e.kind for e in out]
    assert hold_force(w, rid).subject == GIVER and len(_holds_on(w, rid)) == 1


# ======================================================================================
# 6 -- NO PERSON FORMS A GIFT WITH NO RECEIVER
# ======================================================================================

def _give_candidates(w, pid, referents):
    p = w.persons[pid]
    q = Question("q:give", "need", tuple(referents))
    return [c for c in opening_set(p, View(pid, [], w.fixtures.get("view_k")), q, w.fixtures)
            if c.verb == "give"]


def test_no_person_forms_a_give_it_cannot_name_a_receiver_for(monkeypatch):
    w, _d, rid = _at_resolve()
    referents = (rid, RECEIVER, "Hh")
    assert VERB_TABLE["give"].counterparty == "to"
    assert not _give_candidates(w, GIVER, referents), "a receiver-less `give` was formed"
    # CONTROL: clear the column and the Candidates form -- each naming no receiver, which is the
    # act the fold refuses every time. So the column, not some other filter, is what declined them.
    monkeypatch.setitem(VERB_TABLE, "give", dataclasses.replace(VERB_TABLE["give"], counterparty=""))
    got = _give_candidates(w, GIVER, referents)
    assert got and all("to" not in c.operands for c in got), got


def test_the_loader_refuses_an_untyped_rows_counterparty_that_is_no_operand(monkeypatch):
    real = _verbs.load_yaml

    def planted(text):
        doc = real(text)
        if isinstance(doc, dict) and "verbs" in doc:
            for r in doc["verbs"]:
                if r.get("verb") == "give":
                    r["counterparty"] = "receiver"
        return doc
    monkeypatch.setattr(_verbs, "load_yaml", planted)
    with pytest.raises(SystemExit, match="does not bind"):
        _verbs._load_verb_table()
