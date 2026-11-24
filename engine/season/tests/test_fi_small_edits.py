"""B11.12 (`08_FI_04` §1, A-81): a refused inquiry and a failed one are two kinds, and a failed one leaves its actor's own claim.

`inquiry.refused` is the kind of an inquiry the fold would not admit (the six inquiry rows' `emits_on_refusal`); `finding.none` is
the kind of one that was admitted, rolled, and found nothing (the `Failure` band). WITNESS deposits the second to its own doer and to
nobody else (`rosters.yaml: undeposited_actor_kinds`, behind `finding_none_deposit`); the first stays skipped for everyone until the
refusal card CP-T06-04 lands.

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
from .test_fi03_trail import INVESTIGATOR, forged_event, trail_world

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

    # A refused `research` (no such Record) emits the new kind, and it deposits to nobody -- the actor included.
    w, d = _world()
    out = _act_witnessed(w, d, Act(id="a_b1112_gone", actor=ACTOR, verb="research", payload={"subject": "rec_none"}))
    assert [(e.kind, e.degree) for e in out] == [("inquiry.refused", None)], [(e.kind, e.degree) for e in out]
    assert not _holders(w, "inquiry.refused") and not _holders(w, "finding.none")
    # ... and the fan WOULD have reached somebody besides the actor, so the empty ledgers are the skip's doing.
    reach = {pid for pid, _ in observers_for(w, out[0], w.fixtures.get("fan_out_mode"), list(w.persons))}
    assert reach - {ACTOR}, reach


def test_failed_inquiry_leaves_the_actors_own_claim():
    from ..epistemic import observers_for

    # THE SHIPPED ROSTER: the failed inquiry is held by its actor, firsthand, and by nobody else.
    assert DEFAULT_FIXTURES.get("finding_none_deposit") == "actor"
    w, d, out = _failed_research(None)
    assert _holders(w, "finding.none") == {ACTOR}, _holders(w, "finding.none")
    (claim,) = [c for c in w.persons[ACTOR].ledger if c.predicate == "finding.none"]
    assert claim.doer == ACTOR and claim.source == "firsthand", claim
    assert [e for e in w.log if e.kind == "claim.deposited" and out[0].id in e.causes], "the deposit did not emit"
    reach = {pid for pid, _ in observers_for(w, out[0], w.fixtures.get("fan_out_mode"), list(w.persons))}
    assert reach - {ACTOR}, "no bystander could have been reached; the absence above would be an empty room"

    # CONTROL: the roster as it stood (`finding.none` skipped for everyone) leaves the same failed inquiry no write at all.
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
    held = Claim("c_held", INVESTIGATOR, rid, "record.forged", True, e.emitted_at, "inferred", decay, "own")
    w.persons[INVESTIGATOR].ledger.append(held)

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
# Build-verification, `season_loop` lane -- run once to read red then green; the scan is the item's named test, kept at its instruction.
