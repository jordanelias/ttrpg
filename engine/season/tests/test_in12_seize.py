"""Plan position IN-12 step 6 (`workplans/valoria_master_workplan_v9_part5.md`), #453 §10.4 step 6 --
`seize`, THE RECORD HALF, AND THE GATE'S ELEVENTH BASIS, `seizure`. (Its Rung half is IN-13's.)

⚠ A PROPERTY, NOT A REALM COUNT. Every test drives `seize` on a HAND-BUILT world through the real
formation (`opening_set`), the real packer (`pack_scenes`, which names `Act.via`) and the real fold
(`SeasonDriver.resolve`), the cause controlled and a named mutation reddening each. NO TEST HERE
ASSERTS THAT `seize` EXECUTED IN THE SEED-0 REALM (v9 §0.5, RULED 2026-10-13 *"Relax exit rules"*).

What each block proves, and the control that stops it passing vacuously:

  1. THE ROW: resolvable, opens `hold`, celled on IN-08's seven axes (not `uncelled:`), keyed refusals.
  2. THE OBSERVABLE (the entry's falsifier), THROUGH THE REAL FOLD: a `seize` over a held warrant
     naming a Record writes `record.seized` into `w.log`, the previous holder's `hold` closes and the
     seat-holder's opens in one write, one live holder after. CONTROLS, each ONE change: no warrant
     held; the warrant names another Record; the Record is already the actor's.
  3. A SEAT CANNOT BE SEIZED (the entry's falsifier, `test_give.py`'s style): a warrant naming a SEAT is
     refused by the fold (since v9 IN-13 at the `authority` conjunct -- an Office has no place -- and by
     the effect past it; the `existence` conjunct went with the Rung half); and PLANTED AROUND THE
     PRECONDITION at the gate, closing
     a seat's `hold` through the exercised seat is `NotYours` where the same write on a Record is
     admitted under `seizure` (control).
  4. THE SEAT'S AUTHORITY, at the fold and at the gate: no seat exercised, a seat granting no `issue`,
     and a seat whose purview does not reach the dispossessed each refuse (control: the seat that does).
  5. FORMATION, person-side: a held warrant is the Candidate's source -- `seize` forms on a referent
     the warrant names and on no other, and the formed act carries `Act.via` and executes.

MUTATIONS, run at the build 2026-10-16 (each RED, then restored and GREEN) -- outcomes recorded in the
commit message of the step that landed this file, and re-run by anyone who edits the four sites:
  * `loop/effects_information.py::_held_warrant_names` returning True -> block 2's no-warrant and
    wrong-record controls RED.
  * `state/gate.py`'s `SEIZURE` clause deleted -> block 2's observable and block 3's gate control RED
    (the close is `NotYours`).
  * the gate clause's `seat is None` conjunct is REDUNDANT with its object test (`t.object in w.records
    or t.object in w.rungs` already excludes an Office), so dropping it is an EQUIVALENT mutant: block
    3's seat-at-the-gate test stays GREEN (measured), and no RED is claimed for it.
  * `decision/options.py`'s `warranted` filter dropped -> block 5's two negative controls RED.
"""

from __future__ import annotations

import pytest

from ..data.matrix import Step, WriteClass
from ..data.rosters import PURSUIT_AXES, table_meta, table
from ..data.verbs import _OPENERS_FROM_EFFECTS, VERB_TABLE
from ..harness import probes as P
from ..loop.driver import SeasonDriver, mint_token, resolvable_verbs
from ..loop.effects import EFFECTS
from ..queries.world_q import hold_force
from ..state import gate as G
from ..state.carriers import Act, Office, Question, Tenure
from ..state.gate import SEIZURE, T_M, Change, NotYours, Subject
from .test_in10_record_operands import _acts, _formed, _hold_document, _resolve

SEAT, DUKE = "off_duke", "p_high"
HOLDER, FAR = "p_low", "p_king"            # in the duchy (Hh) / outside it (R)
_PET = {"terms": "p_mid", "to": ["p_mid"], "from": "Hh"}


def _warrant(terms):
    return {"terms": terms, "to": ["p_mid"], "at": None}


def _world(warrant_names="rec_pet"):
    """`tiny_world` at a MATTER barrier: `p_low` holds a petition `rec_pet`; the Duke (`off_duke`, grant
    `issue`, purview `D` over `Hh`) holds a warrant `rec_w` naming `warrant_names` (None = no warrant)."""
    w = P.tiny_world()
    _hold_document(w, w.persons[HOLDER], "petition", _PET, rec_id="rec_pet")
    if warrant_names is not None:
        _hold_document(w, w.persons[DUKE], "dispensation", _warrant(warrant_names),
                       rec_id="rec_w")
    d = SeasonDriver(w)
    d.matter(mint_token(w, WriteClass.MATTER), [])
    return w, d


def _seize(subject="rec_pet", actor=DUKE, via=SEAT, key="s1"):
    return Act(id=key, actor=actor, verb="seize", via=via, payload={"subject": subject})


def _kinds(events):
    return [e.kind for e in events]


def _holds_on(w, rid):
    return [t for t in w.tenures if t.kind == "hold" and t.object == rid]


def _gate_write(w, actor, via, apply, subjects):
    """A bare gate write carrying a hand-built `Change` -- nothing but the gate is asked."""
    w.step = Step.RESOLVE
    return w.write("Tenure", mint_token(w, WriteClass.ACTS), None, record_kind="Tenure",
                   fieldname="until", driver="Act", actor=actor, via=via,
                   change=Change(tuple(subjects), apply))


# ======================================================================================
# 1 -- THE ROW
# ======================================================================================

def test_seize_is_a_resolvable_celled_verb_that_opens_hold():
    row = VERB_TABLE["seize"]
    assert row.eligibility == ("remit:issue",) and row.beneficiary == "none" and not row.counterparty
    # RE-PINNED AT v9 IN-13: the Rung half adds `rung.seized` and drops the `object` conjunct (a
    # Record-typed existence the Rung half cannot pass; 'Record or Rung' is no grammar form).
    assert row.writes == ("Tenure.until", "Tenure.since")
    assert row.emits == ("record.seized", "rung.seized")
    assert set(row.refusals_by_clause) == {"eligibility", "authority", "write"}
    assert "seize" in resolvable_verbs()
    assert "seize" in _OPENERS_FROM_EFFECTS["hold"], _OPENERS_FROM_EFFECTS["hold"]
    # IN-08: celled on EVERY axis (a number or an explicit null), not declared `uncelled:`
    cells, uncelled = table("alignment"), table_meta("alignment")["uncelled"]
    assert "seize" not in uncelled
    assert [ax for ax in PURSUIT_AXES if "seize" in cells[ax]] == list(PURSUIT_AXES)
    assert cells["hierarchical_equal"]["seize"] < 0, "the one non-null cell is the rank reading"


# ======================================================================================
# 2 -- THE OBSERVABLE, THROUGH THE REAL FOLD
# ======================================================================================

def test_a_seize_over_a_held_warrant_writes_record_seized_and_moves_the_hold(monkeypatch):
    w, d = _world()
    assert hold_force(w, "rec_pet").subject == HOLDER, "fixture: the petitioner does not hold it"
    bases = {}
    real = G.tenure_write_basis

    def spy(*a, **k):
        b = real(*a, **k)
        bases[a[1].id] = b
        return b
    monkeypatch.setattr(G, "tenure_write_basis", spy)
    snap = w._tenure_snapshot()
    out = _resolve(w, d, _seize())
    assert _kinds(out) == ["record.seized"], _kinds(out)
    assert [e for e in w.log if e.kind == "record.seized"], "record.seized never reached w.log"
    diff = w._tenure_changes(snap)
    closed = [(t.subject, t.object) for t, was in diff if was is not None]
    opened = [(t.subject, t.object) for t, was in diff if was is None]
    assert closed == [(HOLDER, "rec_pet")] and opened == [(DUKE, "rec_pet")], diff
    assert hold_force(w, "rec_pet").subject == DUKE, "`holder_of(record)` did not move"
    assert sum(t.live for t in _holds_on(w, "rec_pet")) == 1, "two live holders after a seizure"
    taken = next(t for t in _holds_on(w, "rec_pet") if t.subject == HOLDER)
    assert taken.until == w.tick, "the dispossessed holder's hold was not closed AT the seizure"
    assert {c.subject for c in out[0].changes} == {t.id for t, _ in diff}, out[0].changes
    # the gate's verdicts: the CLOSE is the new basis, the OPEN is the seizer's own `T-m`
    assert bases[taken.id] == SEIZURE and bases[hold_force(w, "rec_pet").id] == T_M, bases


def test_control_no_held_warrant_is_a_refusal_and_nothing_moves():
    w, d = _world(warrant_names=None)
    out = _resolve(w, d, _seize())
    assert _kinds(out) == ["seize.refused"], _kinds(out)
    assert hold_force(w, "rec_pet").subject == HOLDER
    assert not [e for e in w.log if e.kind == "record.seized"]


def test_control_a_warrant_naming_another_record_licenses_nothing():
    w, d = _world(warrant_names="rec_other")
    out = _resolve(w, d, _seize())
    assert _kinds(out) == ["seize.refused"], _kinds(out)
    assert hold_force(w, "rec_pet").subject == HOLDER


def test_control_a_warrant_the_actor_does_not_hold_licenses_nothing():
    """The warrant exists and names the Record, but a THIRD person holds it: the licence is the
    seizer's own held warrant, not any warrant in the world."""
    w, d = _world(warrant_names=None)
    _hold_document(w, w.persons["p_other"], "dispensation", _warrant("rec_pet"), rec_id="rec_w")
    out = _resolve(w, d, _seize())
    assert _kinds(out) == ["seize.refused"], _kinds(out)
    assert hold_force(w, "rec_pet").subject == HOLDER


def test_control_a_record_the_actor_already_holds_moves_nothing():
    w, d = _world(warrant_names="rec_w")             # the warrant names ITSELF: a Record the Duke holds
    assert hold_force(w, "rec_w").subject == DUKE
    assert _kinds(_resolve(w, d, _seize(subject="rec_w"))) == ["seize.refused"]
    assert sum(t.live for t in _holds_on(w, "rec_w")) == 1


# ======================================================================================
# 3 -- A SEAT CANNOT BE SEIZED
# ======================================================================================

def _seated(warrant_names):
    """The Duke's world with a second seat, `off_steward`, held by `p_low` inside his duchy."""
    w, d = _world(warrant_names=None)
    w.offices["off_steward"] = Office("off_steward", "Steward", "Hh", ["issue"], faction="Crown")
    w.add_tenure(Tenure("t_steward", HOLDER, "off_steward", "hold", since=0))
    _hold_document(w, w.persons[DUKE], "dispensation", _warrant(warrant_names), rec_id="rec_w")
    return w, d


def test_a_warrant_naming_a_seat_does_not_seize_it():
    """The cause controlled: the Duke holds a warrant naming `off_steward` and his seat reaches the
    steward's ground, so the only thing refusing is that the subject is a SEAT, not a Record."""
    w, d = _seated("off_steward")
    assert hold_force(w, "off_steward").subject == HOLDER
    out = _resolve(w, d, _seize(subject="off_steward"))
    # RE-PINNED AT v9 IN-13: the `object` conjunct went with the Rung half, and a seat now refuses at
    # `authority` -- an Office has no place, so no seat's purview reaches it. Still refused, earlier.
    assert _kinds(out) == ["seize.unauthorized"], _kinds(out)
    assert hold_force(w, "off_steward").subject == HOLDER, "a seat was taken"
    assert not [e for e in w.log if e.kind in ("record.seized", "rung.seized")]
    # AND PAST THE PRECONDITION: the effect itself declines a seat (neither a Record nor a settlement).
    assert EFFECTS["seize"](w, _seize(subject="off_steward")) is G.NO_CHANGE


def test_a_seat_cannot_be_seized_at_the_gate_either():
    """PLANTED AROUND THE PRECONDITION (`test_give.py`'s `test_a_seat_cannot_be_handed_over` style): the
    Duke, exercising `off_duke`, closes the steward's `hold` on his seat. A seat passes by its conferral
    basis and by `T-o`, never by seizure: `NotYours`, store put back -- the CLOSURE ALONE, because the
    opening of a seat's `hold` is refused under every basis but `conferral` and would pass the test
    for the wrong reason. (The clause's `seat is None` conjunct is redundant with its object test, so
    no mutation of it turns this test RED -- see the module docstring.)
    CONTROL: the same write over a Record is admitted."""
    w, _d = _seated("off_steward")
    seat = hold_force(w, "off_steward")
    assert G.may_seize(w, DUKE, SEAT, HOLDER), "fixture: the seat must otherwise be able to seize"
    with pytest.raises(NotYours):
        _gate_write(w, DUKE, SEAT, lambda: setattr(seat, "until", w.tick), [Subject.edge(seat)])
    assert seat.live, "the store was not put back"
    nt = Tenure("t_seat_taken", DUKE, "off_steward", "hold", since=w.tick)

    def take_seat():
        seat.until = w.tick
        w.add_tenure(nt)
    with pytest.raises(NotYours):
        _gate_write(w, DUKE, SEAT, take_seat, [Subject.edge(nt), Subject.edge(seat)])
    assert seat.live and nt not in w.tenures, "the store was not put back"
    # control: identical write shape over a Record, same actor, same seat
    rec = hold_force(w, "rec_pet")
    nr = Tenure("t_rec_taken", DUKE, "rec_pet", "hold", since=w.tick)

    def take_record():
        rec.until = w.tick
        w.add_tenure(nr)
    _gate_write(w, DUKE, SEAT, take_record, [Subject.edge(nr), Subject.edge(rec)])
    assert hold_force(w, "rec_pet") is nr, "control: the Record could not be seized at the gate"


# ======================================================================================
# 4 -- THE SEAT'S AUTHORITY
# ======================================================================================

def _plant_far_record(w):
    _hold_document(w, w.persons[FAR], "petition", {"terms": "p_mid", "to": ["p_mid"], "from": "R"},
                   rec_id="rec_far")
    _hold_document(w, w.persons[DUKE], "dispensation", _warrant("rec_far"), rec_id="rec_w2")


def test_a_seat_whose_purview_does_not_reach_the_holder_is_unauthorized():
    w, d = _world()
    _plant_far_record(w)
    assert G.may_seize(w, DUKE, SEAT, HOLDER) and not G.may_seize(w, DUKE, SEAT, FAR)   # control
    out = _resolve(w, d, _seize(subject="rec_far"))
    assert _kinds(out) == ["seize.unauthorized"], _kinds(out)
    assert hold_force(w, "rec_far").subject == FAR


def test_the_same_reach_is_refused_at_the_gate_when_planted_around_the_precondition():
    w, _d = _world()
    _plant_far_record(w)
    far = hold_force(w, "rec_far")
    nt = Tenure("t_far_taken", DUKE, "rec_far", "hold", since=w.tick)

    def apply():
        far.until = w.tick
        w.add_tenure(nt)
    with pytest.raises(NotYours):
        _gate_write(w, DUKE, SEAT, apply, [Subject.edge(nt), Subject.edge(far)])
    assert far.live and nt not in w.tenures


def test_no_seat_exercised_and_a_seat_granting_no_issue_are_refused():
    w, d = _world()
    # `via=None`: the actor acting as himself has no remit at all -> the eligibility clause
    assert _kinds(_resolve(w, d, _seize(via=None, key="s_none"))) == ["seize.unauthorized"]
    assert hold_force(w, "rec_pet").subject == HOLDER
    # a seat whose grant lacks `issue` (`off_dicastery`-like, rung `Hh`), held by the actor
    w.offices["off_scribe"] = Office("off_scribe", "Scribe", "Hh", ["determine"], faction="Crown")
    w.add_tenure(Tenure("t_scribe", DUKE, "off_scribe", "hold", since=0))
    assert not G.may_seize(w, DUKE, "off_scribe", HOLDER)
    assert _kinds(_resolve(w, d, _seize(via="off_scribe", key="s_scribe"))) == ["seize.unauthorized"]
    assert hold_force(w, "rec_pet").subject == HOLDER
    # control: through the seat that grants it, the same act executes
    assert _kinds(_resolve(w, d, _seize(key="s_ok"))) == ["record.seized"]


def test_a_person_acting_as_himself_cannot_close_anothers_hold_at_the_gate():
    w, _d = _world()
    rec = hold_force(w, "rec_pet")
    nt = Tenure("t_taken_by_stranger", "p_other", "rec_pet", "hold", since=w.tick)

    def apply():
        rec.until = w.tick
        w.add_tenure(nt)
    with pytest.raises(NotYours):
        _gate_write(w, "p_other", None, apply, [Subject.edge(nt), Subject.edge(rec)])
    assert rec.live and nt not in w.tenures


# ======================================================================================
# 5 -- FORMATION: THE WARRANT IS THE CANDIDATE'S SOURCE
# ======================================================================================

def _seizes(w, referents):
    q = Question("q:seize", "claim_landed", tuple(referents), None)
    return [c for c in _formed(w, DUKE, q) if c.verb == "seize"]


def test_seize_forms_on_a_referent_a_held_warrant_names_and_executes_through_its_seat():
    w, d = _world()
    (cand,) = _seizes(w, ("rec_pet",))
    assert cand.subject == "rec_pet"
    (act,) = _acts(w, DUKE, [cand])
    assert act.verb == "seize" and act.via == SEAT, (act.verb, act.via)      # `Act.via`: no seatless act
    assert _kinds(_resolve(w, d, act)) == ["record.seized"]
    assert hold_force(w, "rec_pet").subject == DUKE


def test_control_seize_forms_on_no_referent_a_held_warrant_does_not_name():
    w, _d = _world(warrant_names="rec_other")
    assert _seizes(w, ("rec_pet",)) == [], "formed without a warrant naming the referent"
    w2, _d2 = _world(warrant_names=None)
    assert _seizes(w2, ("rec_pet",)) == [], "formed with no warrant held at all"
