"""CP-T03-02 -- THE BAND'S EVENT SAYS HOW THE FIGHT ENDED, AND WHAT THE BODY NOW IS.

(i) Every success Event of a fight's Felled/Wounded band carries `Event.ending`: `(pid, felled | yielded |
undecided)` per party, read off the scene's lifted `wound_state` and `surrender`
(`loop/effects_combat.py::fight_ending`). (ii) Each wounded party's `body.changed` carries the Observation
`(pid, "body", v)`, `v` the body the write LEAVES him with, on `Event.observed` -- deposited by WITNESS's
shipped `observation_deposit_mode` (`actor`), no new channel.
[ASSUMPTION; medium; Jordan to correct; revert: the field and the Observation]

  FALSIFIER: after a Wounded band, the observer the shipped mode deposits to (the act's ACTOR) holds
  `(subject, "body", v)` with `v` the WRITTEN body, and a non-witness holds none.
  MUTATION (executed below, not by hand): build the Observation off the body read before the write and
  `v` is the pre-fight body -- the falsifier's check goes red.
  ⚠ STATED LIMIT: under `actor` mode only the act's actor holds the body Observation; a bystander who saw
  the fight holds `body.changed` (the event-kind claim) but not the value. CP-T03-08's bystander input is
  not widened here.
"""
from __future__ import annotations

import pytest

from ..data.matrix import Step, WriteClass
from ..data.rosters import FELLED, UNTOUCHED, WOUNDED
from ..harness import probes as P
from ..harness.populated import build_realm, run
from ..loop import effects_combat
from ..loop.driver import SeasonDriver, mint_token
from ..seam import Resolution, degree_of
from ..state.carriers import Act
from ._scar_helpers import party_state
from .test_cr85_faculty_replaces_history import revert_cr85
from .test_cp_t03_04_arms import revert_cp_t03_04
from .test_cp_t03_07_body_ceiling import revert_cp_t03_07

ACTOR, SUBJECT = "p_low", "p_mid"      # `tiny_world`: co-located, so a `fight` between them is admitted

_BAND_STATE = {FELLED: dict(felled=True, wounds=2, left=0),
               WOUNDED: dict(wounds=1, left=5),
               UNTOUCHED: dict()}


def _fight(actor_band, subject_band, yielder=None, fan=None, aid="cp302"):
    """`ACTOR` fights `SUBJECT` through the real fold and gate at RESOLVE, the band minted by `degree_of`
    as `resolve()`'s seam branch mints it; then WITNESS at the given `fan_out_mode` (the shipped one when
    `None`)."""
    w = P.tiny_world()
    if fan is not None:
        w.fixtures = w.fixtures.sweep("fan_out_mode", fan)
    before = {pid: w.persons[pid].body for pid in (ACTOR, SUBJECT)}
    d = SeasonDriver(w)
    w.step = Step.RESOLVE
    w.frozen = False
    raw = {"wound_state": {SUBJECT: party_state(**_BAND_STATE[subject_band]),
                           ACTOR: party_state(**_BAND_STATE[actor_band])}}
    if yielder is not None:
        raw["surrender"] = {"by": yielder, "turn": 1, "accepted": True}
    res = Resolution(degree_of(raw, SUBJECT, w.fixtures), raw)
    act = Act(id=aid, actor=ACTOR, verb="fight", payload={"subject": SUBJECT})
    out = d._fold(w, mint_token(w, WriteClass.ACTS), act, res)
    for e in out:
        w.log.append(e)
        d.act_of[e.id] = act
    w.step = Step.WITNESS
    d.witness(mint_token(w, WriteClass.INTERIOR), out)
    return w, out, before


def _body_claims(w, pid) -> dict:
    """Each person's held `(subject, "body", v)` values about `pid`."""
    return {p.id: [c.value for c in p.ledger if c.subject == pid and c.predicate == "body"]
            for p in w.persons.values()}


def _falsifier_holds(w, before) -> list:
    """The home's falsifier as a check; returns its failures (empty = it holds)."""
    bad = []
    written = w.persons[SUBJECT].body
    if written == before[SUBJECT]:
        bad.append("setup: the subject was not bled")
    held = _body_claims(w, SUBJECT)
    if held.get(ACTOR) != [written]:
        bad.append(f"the actor holds {held.get(ACTOR)} for the subject's body, written {written}")
    witnesses = {p.id for p in w.persons.values()
                 if any(c.predicate == "body.changed" and c.subject == SUBJECT for c in p.ledger)}
    non = [pid for pid in w.persons if pid not in witnesses and pid != ACTOR]
    if not non:
        bad.append("setup: everyone witnessed, so the non-witness clause is vacuous")
    bad += [f"non-witness {pid} holds {held[pid]}" for pid in non if held[pid]]
    return bad


def test_falsifier_the_actor_holds_the_written_body_and_a_non_witness_holds_none():
    w, out, before = _fight(UNTOUCHED, WOUNDED)
    assert [e.kind for e in out] == ["body.changed"], [e.kind for e in out]
    assert _falsifier_holds(w, before) == []
    [e] = out
    assert any(o.subject == SUBJECT and o.predicate == "body" and o.value == w.persons[SUBJECT].body
               for o in e.observed), e.observed


def test_mutation_an_observation_built_before_the_write_carries_the_pre_fight_body(monkeypatch):
    """The mutation, executed: the Observation reads `w.persons[pid].body` while the `Change` is built
    (before `perform`), which is the pre-fight body -- the falsifier must go red on it."""
    real = effects_combat.Observation
    box = {}

    def pre_write(subject, predicate, _written):
        return real(subject, predicate, box["w"].persons[subject].body)

    orig = P.tiny_world

    def world():
        box["w"] = orig()
        return box["w"]

    monkeypatch.setattr(P, "tiny_world", world)
    monkeypatch.setattr(effects_combat, "Observation", pre_write)
    w, _out, before = _fight(UNTOUCHED, WOUNDED)
    bad = _falsifier_holds(w, before)
    assert any("the actor holds" in b for b in bad), bad
    assert _body_claims(w, SUBJECT)[ACTOR] == [before[SUBJECT]], "the mutation did not carry the pre-fight body"


def test_under_actor_mode_a_bystander_witness_holds_the_wound_but_not_the_value():
    """The stated limit, observed: everyone witnesses (`total`), only the actor holds the value."""
    w, _out, _b = _fight(UNTOUCHED, WOUNDED, fan="total")
    held = _body_claims(w, SUBJECT)
    bystanders = [pid for pid in w.persons if pid not in (ACTOR, SUBJECT)]
    assert bystanders
    for pid in bystanders:
        assert any(c.predicate == "body.changed" for c in w.persons[pid].ledger), f"{pid} did not witness"
        assert held[pid] == [], f"bystander {pid} holds {held[pid]}"
    assert held[ACTOR] == [w.persons[SUBJECT].body]


def test_the_ending_per_party_on_every_band_event():
    checked = 0
    for (a, s, yielder), want in {
            (UNTOUCHED, WOUNDED, None): {ACTOR: "undecided", SUBJECT: "undecided"},
            (WOUNDED, FELLED, None): {ACTOR: "undecided", SUBJECT: "felled"},
            (FELLED, WOUNDED, None): {ACTOR: "felled", SUBJECT: "undecided"},
            (UNTOUCHED, WOUNDED, SUBJECT): {ACTOR: "undecided", SUBJECT: "yielded"}}.items():
        _w, out, _b = _fight(a, s, yielder=yielder)
        assert out
        for e in out:
            assert dict(e.ending) == want, (a, s, yielder, e.kind, e.ending)
            assert [pid for pid, _ in e.ending] == [ACTOR, SUBJECT], e.ending
            checked += 1
    assert checked >= 4


def test_an_untouched_fight_carries_no_ending_and_no_body():
    _w, out, _b = _fight(UNTOUCHED, UNTOUCHED)
    assert [e.kind for e in out] == ["contest.undecided"], [e.kind for e in out]
    assert all(e.ending == () and not any(o.predicate == "body" for o in e.observed) for e in out)


def test_a_felled_party_carries_no_body_observation():
    """A felled man is removed; only the wounded party's body is observed, on `body.changed` alone."""
    _w, out, _b = _fight(WOUNDED, FELLED)
    by_kind = {e.kind: [o for o in e.observed if o.predicate == "body"] for e in out}
    assert [o.subject for o in by_kind.get("body.changed", [])] == [ACTOR], by_kind
    assert by_kind.get("person.died", []) == [], by_kind


#: The one-season realm hashes BEFORE this item (dee492f7); seed 0 forms no Felled/Wounded fight and does not move.
PRE_ITEM = {0: "20accb03c3d32f80a9fab00d80a70b21",
            1: "f4330aacb84c25069dfdb33f2a123215",
            2: "a030141a9c66a833e84a97a71404ff88"}


def revert_cp_t03_02(monkeypatch):
    """The item at its revert, in process: no ending, no body Observation."""
    monkeypatch.setattr(effects_combat, "fight_ending", lambda *_a, **_k: ())
    monkeypatch.setattr(effects_combat, "body_observed", lambda *_a, **_k: ())


@pytest.mark.parametrize("seed", [0, 1, 2])
def test_control_the_item_at_its_revert_reproduces_the_pre_item_one_season_hash(seed, monkeypatch):
    """HASH MOVER, CONTROLLED: every pin this item re-records moved by the ending and the body Observation alone --
    with both reverted in process the one-season realm reads the pre-item hash exactly; with them, seeds 1 and 2
    move (seed 0 formed no Felled/Wounded fight)."""
    # v11 CP-T03-04 (`arms` in the vocation range, a formation mover of EVERY seed, seed 0 included) is reverted on BOTH arms,
    # so `moved` still reads this item alone and `PRE_ITEM` stands.
    revert_cp_t03_04(monkeypatch)
    revert_cp_t03_07(monkeypatch)   # v11 CP-T03-07 (`body_ceiling`, a schema mover of every realm), the same way
    w = build_realm(seed)
    run(1, seed, w=w)
    moved = w.content_hash()
    revert_cp_t03_02(monkeypatch)
    # v11 CR-85 (`faculty` replaces `history`, a later mover of seed 1) is reverted too, so `PRE_ITEM` stands.
    revert_cr85(monkeypatch)
    w = build_realm(seed)
    run(1, seed, w=w)
    assert w.content_hash() == PRE_ITEM[seed]
    assert (moved != PRE_ITEM[seed]) == (seed != 0), (seed, moved)
