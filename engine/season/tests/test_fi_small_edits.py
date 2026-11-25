"""B11.12 (`08_FI_04` §1, A-81): a refused inquiry and a failed one are two kinds, and a failed one teaches its actor.

`inquiry.refused` is the kind of an inquiry the fold would not admit (the six inquiry rows' `emits_on_refusal`); `finding.none` is
the kind of one that was admitted, rolled, and found nothing (the `Failure` band). B11.61 (CP-T06-04): both are `undeposited_kinds`, so WITNESS
makes no event-kind claim of either and deposits the Event's other claims as for any Event (`finding_none_deposit`, shipped `actor`;
`none` is the whole-Event skip, kept as the control).

Both tests are game-state tests in the `season_loop` lane: each resolves a planted act through the real driver and witnesses its Event.
"""

from __future__ import annotations

import dataclasses

import pytest

from ..data.fixtures import DEFAULT_FIXTURES
from ..data.matrix import Step, WriteClass
from ..data.rosters import UNDEPOSITED_KINDS
from ..data.verbs import EVENT_KINDS, VERB_TABLE
from ..harness import probes as P
from ..loop.driver import SeasonDriver, mint_token
from ..state.carriers import Act, Claim, Record
from .test_fi03_trail import FORGER, INVESTIGATOR, forged_event, trail_world

INQUIRIES = ("examine", "interview", "research", "surveil", "thread_read", "reconstruct")
REC, ACTOR = "rec_b1112", "p_low"


def _world(arm: str | None = None):
    w = P.tiny_world()
    w.records[REC] = Record(REC, "Hh", "text")
    if arm is not None:
        w.fixtures = w.fixtures.sweep("finding_none_deposit", arm)
    return w, SeasonDriver(w)


def _act_witnessed(w, d, act):
    """Resolve `act` through the real driver, witness its Event(s); returns the Events."""
    w.step = Step.RESOLVE
    out = d.resolve(mint_token(w, WriteClass.ACTS), [act], contest_max_depth=w.fixtures.get("contest_max_depth"))
    w.log.extend(out)
    w.step = Step.WITNESS
    d.witness(mint_token(w, WriteClass.INTERIOR), out)
    return out


def _holders(w, kind: str) -> set:
    return {pid for pid, p in w.persons.items() if any(c.predicate == kind for c in p.ledger)}


def _failed_research(arm: str | None):
    """`research` of the planted Record at act ids swept until one draws `Failure`: (world, driver, Events)."""
    for n in range(60):
        w, d = _world(arm)
        out = _act_witnessed(w, d, Act(id=f"a_b1112_research_{n}", actor=ACTOR, verb="research", payload={"subject": REC}))
        if len(out) == 1 and out[0].kind == "finding.none" and out[0].degree == "Failure":
            return w, d, out
    raise AssertionError("60 act ids drew no `Failure` research")


def test_inquiry_refused_is_split_from_finding_none():
    from ..epistemic import observers_for

    checked = 0
    for verb in INQUIRIES:
        row = VERB_TABLE[verb]
        assert set(row.emits_on_refusal) == {"inquiry.refused"}, (verb, row.emits_on_refusal)   # the refusal union, no `draw` kind
        checked += 1
        if row.emits_by_degree:                      # the graded rows keep their `Failure` kind
            assert row.emits_at("Failure") == ("finding.none",), verb
            checked += 1
    assert checked >= 9 and {"inquiry.refused", "finding.none"} <= set(EVENT_KINDS) and "inquiry.refused" in UNDEPOSITED_KINDS

    # A refused `research` (no such Record) emits the new kind, and nobody holds an event-kind claim of it -- the actor included.
    w, d = _world()
    out = _act_witnessed(w, d, Act(id="a_b1112_gone", actor=ACTOR, verb="research", payload={"subject": "rec_none"}))
    assert [(e.kind, e.degree) for e in out] == [("inquiry.refused", None)], [(e.kind, e.degree) for e in out]
    assert not _holders(w, "inquiry.refused") and not _holders(w, "finding.none")
    # ... and the fan WOULD have reached somebody besides the actor, so the empty ledgers are the kind's skip, not an empty room.
    reach = {pid for pid, _ in observers_for(w, out[0], w.fixtures.get("fan_out_mode"), list(w.persons))}
    assert reach - {ACTOR}, reach


def test_failed_inquiry_makes_no_event_kind_claim_and_teaches_its_actor():
    from ..epistemic import observers_for

    # THE SHIPPED ARM (B11.61): nobody holds a `finding.none` claim, and the Event is deposited otherwise, so a ledger moved.
    assert DEFAULT_FIXTURES.get("finding_none_deposit") == "actor"
    w, d, out = _failed_research(None)
    assert not _holders(w, "finding.none"), _holders(w, "finding.none")
    deposited = {e.changes[0].subject for e in w.log if e.kind == "claim.deposited" and out[0].id in e.causes}
    assert deposited, "the failed inquiry deposited nothing: a null scene"
    assert any(c.id in deposited and c.doer == ACTOR for c in w.persons[ACTOR].ledger), "the actor holds nothing of his own act"
    reach = {pid for pid, _ in observers_for(w, out[0], w.fixtures.get("fan_out_mode"), list(w.persons))}
    assert reach - {ACTOR}, "no bystander could have been reached; the absence above would be an empty room"

    # CONTROL: the whole-Event skip (`none`) leaves the same failed inquiry no write at all.
    w, d, out = _failed_research("none")
    assert not _holders(w, "finding.none")
    assert not [e for e in w.log if e.kind == "claim.deposited" and out[0].id in e.causes]


# ---- B11.13 (`08_FI_04` §2, first bullet): `research` needs presence ----------------------------------------------------


def _research_kinds(actor: str, n: int = 40):
    """`n` `research` acts of the planted Record by `actor`, each resolved on a fresh world: the Events' kinds."""
    kinds = []
    for i in range(n):
        w, d = _world()
        out = _act_witnessed(w, d, Act(id=f"a_b1113_research_{i}", actor=actor, verb="research", payload={"subject": REC}))
        kinds.append([e.kind for e in out])
    return kinds


def test_research_from_elsewhere_is_refused():
    # The Record is at `Hh` (its holder's place, `world_q.place_of`); `p_low` lives at `Hh`, `p_high` at `S`.
    present = _research_kinds(ACTOR)
    elsewhere = _research_kinds("p_high")
    # H-319's reading: someone elsewhere is refused 40 of 40.
    assert elsewhere == [["inquiry.refused"]] * 40, [k for k in elsewhere if k != ["inquiry.refused"]][:3]
    # CONTROL: the person present still executes -- no refusal, and the finding kinds the row emits.
    assert not [k for k in present if "inquiry.refused" in k], present
    assert {k for ks in present for k in ks} & {"finding.made", "finding.none"}, present


# ---- B11.14 (`08_FI_04` §2, second bullet): a repeated ungraded finding deposits nothing --------------------------------


def _claims_of(w, kind: str) -> list:
    return [(pid, c) for pid, p in w.persons.items() for c in p.ledger if c.predicate == kind]


def test_ten_repeated_interviews_leave_one_claim():
    # Ten `interview` acts of one person by one actor in one world: each holder keeps ONE `(subject, finding.made, True)`, not ten (H-320).
    w, d = _world()
    for i in range(10):
        out = _act_witnessed(w, d, Act(id=f"a_b1114_interview_{i}", actor=ACTOR, verb="interview", payload={"subject": "p_mid"}))
        assert [e.kind for e in out] == ["finding.made"], [e.kind for e in out]
    held = _claims_of(w, "finding.made")
    holders = {pid for pid, _ in held}
    assert ACTOR in holders and len(holders) >= 2, holders        # the fan reached a bystander too: the one claim is the skip's doing
    assert len(held) == len(holders), f"{len(held)} claims for {len(holders)} holders"
    assert all(c.value is True and c.source == "firsthand" for _, c in held), held

    # CONTROL: a graded inquiry's repeated finding still deposits per band -- ten `research` acts leave several claims on one holder.
    w, d = _world()
    kinds = []
    for i in range(10):
        kinds += [e.kind for e in _act_witnessed(w, d, Act(id=f"a_b1114_research_{i}", actor=ACTOR, verb="research", payload={"subject": REC}))]
    assert kinds.count("finding.made") >= 3, kinds
    assert len([c for pid, c in _claims_of(w, "finding.made") if pid == ACTOR]) > 1


# ---- B11.15 (`08_FI_04` §2, third bullet): a forgotten trail claim stops closing its trail ---------------------------------


@pytest.mark.flat_fold
def test_a_claim_decayed_to_zero_no_longer_closes_the_trail():
    # H-341's trail arm: the investigator's `(rid, record.forged, True)` claim closes the Event's trail while he still holds it, and stops
    # closing it once it has faded to 0 (`present_confidence`), whether the fade is the stored floor or the seasons since `when`.
    from ..epistemic import holds_trail, trail_of
    from ..state.ledgers import present_confidence

    w, d, rid = trail_world()
    e = forged_event(w)
    decay = w.fixtures.claim_decay()
    assert decay > 0 and trail_of(w, rid, INVESTIGATOR) != [], "the world offers no trail to close, or claims do not fade"
    # B11.61: the trail is closed by the thing AND the hand, both held and fading at one rate.
    hand = Claim("c_hand", INVESTIGATOR, FORGER, "record.forged", True, e.emitted_at, "inferred", decay, "own")
    held = Claim("c_held", INVESTIGATOR, rid, "record.forged", True, e.emitted_at, "inferred", decay, "own")
    w.persons[INVESTIGATOR].ledger.extend([hand, held])

    # CONTROL: confidence 5 at its own tick still closes the trail.
    w.tick = e.emitted_at
    assert present_confidence(held.confidence, held.when, w.tick, decay) > 0
    assert holds_trail(w, w.persons[INVESTIGATOR], e, w.fixtures.get("claim_subject_rule")) and trail_of(w, rid, INVESTIGATOR) == []

    # The same claim one season on has faded to 0: it no longer closes the trail.
    w.tick = e.emitted_at + 1
    assert present_confidence(held.confidence, held.when, w.tick, decay) == 0
    assert trail_of(w, rid, INVESTIGATOR) != [], "a claim faded to 0 still closed its trail"

    # A claim deposited at 0 does not close it either, and a fresh one beside it does.
    w.tick = e.emitted_at
    w.persons[INVESTIGATOR].ledger[-1] = dataclasses.replace(held, id="c_zero", confidence=0)
    assert trail_of(w, rid, INVESTIGATOR) != [], "a claim held at 0 closed its trail"
    w.persons[INVESTIGATOR].ledger.append(held)
    assert trail_of(w, rid, INVESTIGATOR) == []


@pytest.mark.flat_fold
def test_a_trail_found_again_after_its_claims_faded_deposits_again():
    # Close fix F-A1: `_found_claims`' exact-triple guard counts only a held copy that is still LIVE (`present_confidence` > 0, the reading `holds_trail`
    # takes), so a finder whose claims faded to 0 is offered the trail by `trail_of` AND the deposit lands. FALSIFIER: with the guard reading the raw
    # ledger the faded copy blocks it, the find deposits nothing and `trail_of` offers the same trail for ever.
    from ..epistemic import trail_of
    from ..state.ledgers import present_confidence
    from .test_fi03_trail import HAND_BANDS, find_band, forged_claims, found_deposits, research, step, step_until

    n, cand = find_band(HAND_BANDS)
    w, d, rid = trail_world()
    step(w, d, research(n, cand))
    decay = w.fixtures.claim_decay()
    held = forged_claims(w, INVESTIGATOR)
    assert decay > 0 and len(held) == 2 and trail_of(w, rid, INVESTIGATOR) == [], "the first find did not close the trail"
    for _ in range(1000):
        if all(present_confidence(c.confidence, c.when, w.tick, decay) == 0 for c in held):
            break
        w.tick += 1
    else:
        raise AssertionError("the held claims never faded to 0")
    assert trail_of(w, rid, INVESTIGATOR) != [], "a faded claim still closed the trail"
    out = step_until(w, d, cand, "faded", HAND_BANDS.__contains__)
    assert found_deposits(w, out[0].id), "the find deposited nothing: the faded copy blocked it"
    assert any(present_confidence(c.confidence, c.when, w.tick, decay) > 0 for c in forged_claims(w, INVESTIGATOR))


# ---- B11.17 (`08_FI_04` §4 with `17_CENSUS_REST_1` D2): the `ttl` field deleted; a writ ends when its last stage matures ----
# Both are game-state tests in the `season_loop` lane: the first resolves `comply` through the real fold and MATTER's
# maturing; the second writes a declared row through the real gate.

def test_a_writ_stops_admitting_comply_after_its_last_stage():
    from .test_in09_dispensation_answer import HOLDER, WRIT, _fold, _read_terms, _with_writ

    w, d = _with_writ()
    w.records[WRIT].stages = [(w.tick + 1, "last", "mk")]     # a writ whose last stage matures at the next barrier
    _read_terms(w, HOLDER)
    assert _fold(w, d, HOLDER, "comply", WRIT, "c_before") == ["compliance.given"], "an open writ refused `comply`"

    w.tick += 1
    w.step = Step.MATTER
    d.matter(mint_token(w, WriteClass.MATTER), [])
    assert w.records[WRIT].matured, "its last stage did not mature"
    w.step = Step.RESOLVE
    assert _fold(w, d, HOLDER, "comply", WRIT, "c_after") == ["compliance.impossible"], "a lapsed writ still admitted `comply`"


def test_a_declared_row_with_no_emission_still_raises_d22():
    from ..state.gate import Forbidden

    w = P.tiny_world()
    rec = Record("rec_d22", "Hh", "text")
    w.records[rec.id] = rec
    w.step = Step.MATTER
    with pytest.raises(Forbidden, match="D22|emitted nothing"):
        w.write("matured", mint_token(w, WriteClass.MATTER), lambda: setattr(rec, "matured", True),
                record_kind="Record", fieldname="matured", driver="Event")
    assert rec.matured is False, "the refused write applied"


# B11.21 (`08_FI_04` §6, D-74): the witness step reads a holder's own ledger through `queries/person_q.py`, never through `decision/`.
# (A statement of the layering this edit kept, not a test: no test in this file scans `loop/witness.py`'s imports.)
