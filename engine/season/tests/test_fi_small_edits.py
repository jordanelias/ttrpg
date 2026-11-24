"""B11.12 (`08_FI_04` §1, A-81): a refused inquiry and a failed one are two kinds, and a failed one leaves its actor's own claim.

`inquiry.refused` is the kind of an inquiry the fold would not admit (the six inquiry rows' `emits_on_refusal`); `finding.none` is
the kind of one that was admitted, rolled, and found nothing (the `Failure` band). WITNESS deposits the second to its own doer and to
nobody else (`rosters.yaml: undeposited_actor_kinds`, behind `finding_none_deposit`); the first stays skipped for everyone until the
refusal card CP-T06-04 lands.

Both tests are game-state tests in the `season_loop` lane: each resolves a planted act through the real driver and witnesses its Event.
"""

from __future__ import annotations

from ..data.fixtures import DEFAULT_FIXTURES
from ..data.matrix import Step, WriteClass
from ..data.rosters import UNDEPOSITED_KINDS
from ..data.verbs import EVENT_KINDS, VERB_TABLE
from ..harness import probes as P
from ..loop.driver import SeasonDriver, mint_token
from ..state.carriers import Act, Record

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
