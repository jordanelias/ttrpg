"""B09.02 -- A REFUSAL ONE REMEMBERS: THE READER (`person_q.refused_before`), AND THE THREE TESTS OF ITS CALLER.

A person refused an opportunity holds a firsthand claim `(subject, <the verb row's refusal kind>, doer = himself)`
that nothing in `decision/` read. `refused_before(p, kinds, subject)` is the one reader of it: the present
confidence of his NEWEST such claim, or 0 when there is none or when he holds ANY newer claim about the subject.
Its caller is `decision/choose.py::admission_weight` (B09.03, the factor at the control `refusal_memory = 0.0`).

TWO OF THE FIVE ARE GREEN HERE AND THREE ARE RED UNTIL B09.03, BY DESIGN (the plan's EXPECTED RED, `[skip ci]`):

  green  test_newer_claim_about_subject_supersedes_the_memory
  green  test_reader_takes_the_person_not_a_ledger
  red    test_control_value_zero_leaves_hash_equal        -- no `refusal_memory` fixture, no `admission_weight`
  red    test_factor_never_reaches_zero_below_one          -- no `admission_weight`
  red    test_unwired_verb_has_factor_one                  -- no `admission_weight`

The reader has no caller until B09.03, so the realm content hash is today's (the batch's control reading, quoted in
the commit body); the red hash test is the equality B09.03 makes true by the factor being exactly 1.0 at the control.
"""
from __future__ import annotations

import inspect

import pytest

from ..data.fixtures import DEFAULT_FIXTURES
from ..data.verbs import VERB_TABLE
from ..decision import choose as CH
from ..queries import person_q
from ..state.carriers import Candidate, Claim, Person

KINDS = ("give.refused",)
SUBJECT = "p_other"
ME, HIM = "p_me", "p_him"
FULL = DEFAULT_FIXTURES.get("confidence_default")


def _claim(i: int, holder: str, subject: str, predicate: str, when: int, lap: int = 0, *, doer=None,
           confidence: int = FULL, source: str = "firsthand", chain: tuple = ()) -> Claim:
    return Claim(f"c{i}", holder, subject, predicate, True, when, source, confidence, "own", lap,
                 chain=chain, doer=doer)


def _refused(i: int, when: int, lap: int = 0, *, subject: str = SUBJECT, holder: str = ME, doer=ME, **kw) -> Claim:
    return _claim(i, holder, subject, KINDS[0], when, lap, doer=doer, **kw)


def _person(pid: str, *claims: Claim) -> Person:
    return Person(pid, ledger=list(claims))


def test_newer_claim_about_subject_supersedes_the_memory():
    checked = 0

    # CONTROL: the refusal alone is remembered, at the confidence it was deposited at.
    p = _person(ME, _refused(1, when=2, lap=1))
    assert person_q.refused_before(p, KINDS, SUBJECT) == FULL
    checked += 1

    # THE SUPERSESSION: any claim about the subject NEWER than the refusal, whatever its predicate, source or doer,
    # and whether it is newer by season or by lap within the season, clears the memory.
    for newer_when, newer_lap in ((3, 0), (2, 2), (9, 0)):
        for predicate, source, doer in (("at", "firsthand", None), (KINDS[0], "told", HIM), ("seen", "seen", None)):
            news = _claim(2, ME, SUBJECT, predicate, newer_when, newer_lap, doer=doer, source=source)
            assert person_q.refused_before(_person(ME, _refused(1, 2, 1), news), KINDS, SUBJECT) == 0, \
                (newer_when, newer_lap, predicate)
            checked += 1

    # AND NOT OTHERWISE: a claim not newer (older, or the same `(when, lap)`), or newer but about another subject,
    # leaves the memory standing.
    for claim in (_claim(2, ME, SUBJECT, "at", 1, 9),          # an older season, a later lap: older
                  _claim(2, ME, SUBJECT, "at", 2, 0),          # the same season, an earlier lap
                  _claim(2, ME, SUBJECT, "at", 2, 1),          # the same `(when, lap)`: not newer
                  _claim(2, ME, "p_third", "at", 9, 9)):       # newer, about another subject
        assert person_q.refused_before(_person(ME, _refused(1, 2, 1), claim), KINDS, SUBJECT) == FULL, claim
        checked += 1

    # THE NEWEST refusal is the one read: the older of two is superseded by the newer, not the other way about.
    older, newer = _refused(1, 1, confidence=FULL), _refused(2, 3, confidence=FULL // 2)
    assert person_q.refused_before(_person(ME, older, newer), KINDS, SUBJECT) == FULL // 2
    assert person_q.refused_before(_person(ME, newer, older), KINDS, SUBJECT) == FULL // 2
    checked += 2

    # IT IS READ AT PRESENT CONFIDENCE (`state/ledgers.py::present_confidence`), never the stored deposit: the
    # deposit less `decay` per season elapsed, 0 at the floor. Control: no `tick` and no `decay` reads the stored value.
    p = _person(ME, _refused(1, when=2))
    assert person_q.refused_before(p, KINDS, SUBJECT, tick=2, decay=5) == FULL
    assert person_q.refused_before(p, KINDS, SUBJECT, tick=4, decay=5) == FULL - 10
    assert person_q.refused_before(p, KINDS, SUBJECT, tick=2 + FULL, decay=5) == 0
    checked += 3

    assert checked == 19


def test_reader_takes_the_person_not_a_ledger():
    params = list(inspect.signature(person_q.refused_before).parameters.values())
    assert [q.name for q in params[:3]] == ["p", "kinds", "subject"]
    # nothing a caller could use to name a holder other than the asker (the own-ledger carve-out, `04` §B.2)
    assert not {"ledger", "holder", "claims", "world", "w"} & {q.name for q in params}
    assert [q.name for q in params[3:]] == ["tick", "decay"]             # the fade's two inputs, as `believed_kit` takes them

    # the asker's own ledger is what is read: a PLANTED SECOND PERSON'S ledger, holding a refusal, is not reachable.
    mine, his = _person(ME), _person(HIM, _refused(1, 2, holder=HIM, doer=HIM))
    assert person_q.refused_before(his, KINDS, SUBJECT) == FULL            # control: the same claim, asked by its holder
    assert person_q.refused_before(mine, KINDS, SUBJECT) == 0
    # a bare ledger is not a Person, and a Person is refused no matter what it holds
    with pytest.raises(AttributeError):
        person_q.refused_before(his.ledger, KINDS, SUBJECT)

    # a claim in the asker's own ledger about the asker's neighbour's refusal (not his own act) is not a memory of his
    # refusal: `doer` must be himself, and the claim firsthand (a retelling of a refusal is hearsay about another)
    for claim in (_refused(1, 2, doer=HIM), _refused(1, 2, doer=None), _refused(1, 2, source="told", chain=(HIM,))):
        assert person_q.refused_before(_person(ME, claim), KINDS, SUBJECT) == 0, claim
    assert person_q.refused_before(_person(ME, _claim(1, ME, SUBJECT, "other.refused", 2, doer=ME)), KINDS, SUBJECT) == 0


# ---------------------------------------------------------------------------------------------
# RED UNTIL B09.03: the factor, its fixture and its control.


def _fx(memory: float):
    return DEFAULT_FIXTURES.sweep("refusal_memory", memory)


def test_control_value_zero_leaves_hash_equal(monkeypatch):
    """At `refusal_memory = 0.0` the factor is exactly 1.0, so a season's content hash is the one a chooser with no
    admission factor reaches. Read two ways: the fixture is registered (cheap, and red until B09.03 builds it), and
    one season played at the control equals one played with `admission_weight` replaced by the constant 1.0."""
    from ..boot.realm import build_realm
    from ..harness import populated

    assert DEFAULT_FIXTURES.get("refusal_memory") is not None                      # registered, graded, swept
    assert hasattr(CH, "admission_weight")

    def hash_of(factor):
        w = build_realm(0)
        w.fixtures = w.fixtures.sweep("refusal_memory", 0.0)
        if factor is not None:
            monkeypatch.setattr(CH, "admission_weight", lambda p, c, fx, *a, **k: factor)
        populated.run(1, 0, w=w)
        return w.content_hash()

    assert hash_of(None) == hash_of(1.0)


def _giving_person(*claims: Claim):
    assert VERB_TABLE["give"].emits_on_refusal == KINDS
    return _person(ME, *claims), Candidate("give", SUBJECT)


def test_factor_never_reaches_zero_below_one():
    """`1 - refusal_memory * refused_before / confidence_default`: a person refused at full confidence keeps a
    positive factor at every `refusal_memory < 1`, so he is never stuck; it is 0 only at 1.0 and a full memory."""
    p, c = _giving_person(_refused(1, 0))
    checked = 0
    for memory in (0.0, 0.25, 0.5, 0.9, 0.999):
        f = CH.admission_weight(p, c, _fx(memory))
        assert 0.0 < f <= 1.0, memory
        checked += 1
    assert CH.admission_weight(p, c, _fx(0.0)) == 1.0
    assert CH.admission_weight(p, c, _fx(0.5)) == pytest.approx(0.5)               # control: the memory does act
    assert CH.admission_weight(p, c, _fx(1.0)) == 0.0
    assert checked >= 5

    # THE FACTOR IS OBSERVABLE (the hash test above plays one season and cannot see it): at `refusal_memory` 1.0 a
    # hand-built remembered refusal puts a factor strictly below 1.0, and it is read at the person's own tick and decay.
    assert CH.admission_weight(p, c, _fx(1.0)) < 1.0
    from ..state.carriers import interior_of
    decay = 5
    for tick, remembered in ((0, FULL), (4, FULL - 4 * decay), (FULL // decay, 0)):
        seen = interior_of(p, tick, decay)
        assert CH.admission_weight(seen, c, _fx(1.0)) == pytest.approx(1.0 - remembered / FULL), tick


def test_unwired_verb_has_factor_one():
    """A verb whose row declares no refusal kind, and an opportunity with no memory, are 1.0 at every setting."""
    silent = [v for v, row in VERB_TABLE.items() if not row.emits_on_refusal]
    assert silent, "no verb row without a refusal kind: the test has nothing to read"
    p = _person(ME, _refused(1, 0))                                  # holds a refusal on SUBJECT, of a kind no silent row names
    checked = 0
    for verb in silent:
        for memory in (0.0, 0.5, 1.0):
            assert CH.admission_weight(p, Candidate(verb, SUBJECT), _fx(memory)) == 1.0, (verb, memory)
            checked += 1
    # nothing remembered: a verb WITH a refusal kind is 1.0 too, on a person holding no such claim
    for memory in (0.5, 1.0):
        assert CH.admission_weight(_person(ME), Candidate("give", SUBJECT), _fx(memory)) == 1.0
        checked += 1
    assert checked >= 5


# ---------------------------------------------------------------------------------------------
# B09.04: a failed search may be remembered by the one who searched, behind the `finding_none_deposit` arm.


def _failed_search(arm: str):
    """`tiny_world` with the arm swept to `arm`; the actor's `research` of a Record that does not exist is REFUSED at the precondition,
    which emits `finding.none` with no draw (`test_fi01_graded_inquiries.py` plants the same act), resolved through the real driver and
    witnessed. Returns the world, the Event, and `(holder, claim)` for every claim of that kind any person holds."""
    from ..data.matrix import Step, WriteClass
    from ..harness import probes as P
    from ..loop.driver import SeasonDriver, mint_token
    from ..state.carriers import Act

    w = P.tiny_world()
    w.fixtures = w.fixtures.sweep("finding_none_deposit", arm)
    d = SeasonDriver(w)
    act = Act(id="a_b0904_research_gone", actor="p_low", verb="research", payload={"subject": "rec_none"})
    w.step = Step.RESOLVE
    (ev,) = d.resolve(mint_token(w, WriteClass.ACTS), [act], contest_max_depth=w.fixtures.get("contest_max_depth"))
    w.log.extend([ev])
    assert ev.kind == "finding.none", ev.kind
    w.step = Step.WITNESS
    d.witness(mint_token(w, WriteClass.INTERIOR), [ev])
    return w, ev, [(pid, c) for pid, p in w.persons.items() for c in p.ledger if c.predicate == "finding.none"]


def test_finding_none_deposits_to_its_actor_only_at_the_actor_arm():
    from ..epistemic import observers_for

    assert DEFAULT_FIXTURES.get("finding_none_deposit") == "none"                  # the shipped arm is the control

    # CONTROL ARM: nobody holds the claim -- the skip stands, the actor included.
    w, ev, held = _failed_search("none")
    assert held == [], held
    # THE CLAIM COULD HAVE REACHED A NON-ACTOR: the fan that WITNESS would have asked admits somebody besides the actor, so
    # "no non-actor holds it" below is the arm's doing and not an empty room.
    reach = {pid for pid, _ in observers_for(w, ev, w.fixtures.get("fan_out_mode"), list(w.persons))}
    assert "p_low" in reach and reach - {"p_low"}, reach

    # ACTOR ARM: the doer, and only the doer, holds one firsthand claim about the subject, stamped as his own act, and the
    # reader of a refusal one remembers finds it. (An arm wired backwards fails the control's `held == []` and this line.)
    w, ev, held = _failed_search("actor")
    assert [pid for pid, _ in held] == ["p_low"], held
    claim = held[0][1]
    assert claim.doer == "p_low" and claim.source == "firsthand", claim
    assert person_q.refused_before(w.persons["p_low"], ("finding.none",), claim.subject) == claim.confidence > 0
    assert [e for e in w.log if e.kind == "claim.deposited" and ev.id in e.causes], "the deposit did not emit"

    # AN ARM OUTSIDE THE ROSTER REFUSES, so a misspelt arm cannot read as the control.
    with pytest.raises(Exception, match="finding.none deposit arm"):
        _failed_search("actors")
