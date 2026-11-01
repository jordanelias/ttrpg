"""v10 IN-12 steps 5 and 5a, their remainder (`workplans/valoria_master_workplan_v10_part4.md` IN-12; H-226
route (a), H-227) -- `interrogate` and the charge.

⚠ A PROPERTY ON A HAND-BUILT WORLD, NOT A REALM COUNT (P9). Formation through the real `questions_for` and
`opening_set`; resolution through the real fold (`SeasonDriver.resolve`). The realm reading is the batch's:
at the build, `build_realm(s)` + two seasons read the base hashes at seeds 0-2 with `interrogation.refused`
0 and `commitment.refused` 0 (the row is never attempted while no live `detain` exists).

What each block proves, and the control that stops it passing vacuously:

  1. THE ROW: untyped, contested, `counterparty: subject`, the `Detainee` class, `[]` at every band, ONE
     KIND PER BAND, `uncelled:`, resolvable. PLANTED FAILURE: the row's ground for the driver's gate clause
     (its `counterparty: subject`) withdrawn -> it leaves `resolvable_verbs()` while its precondition and
     effect gates still pass, so the clause is what admits it.
  2. THE FALSIFIER: the Duke holds `off_duke` (grants `determine`), the clerk is detained to it, and a
     docketed petition names him -> the clerk is stamped `Detainee` on the Duke's question, the Duke forms
     `interrogate(clerk)`, and the fold's contest emits one `confession.*` kind at its band (one draw).
     PLANTED FAILURE: the stamper switched off -> nothing is formed.
  3. THE CONTROL: no custody -> nothing stamped, nothing formed; and a hand-built act (force-admitted) is
     refused `interrogation.refused` BEFORE ANY DRAW (the draw count is 0). The same for custody without a
     charge, and for custody at a seat the Duke does not hold (not offered).
  4. STEP 5a: a witness addressed by a petition he holds forms `commit` on the charge its `terms` names,
     and the commit executes. CONTROL: the petitioner holding his own petition (not its addressee) forms
     none on it.
"""

from __future__ import annotations

import dataclasses
from unittest import mock

from ..data.rosters import PURSUIT_AXES, table, table_meta
from ..data.verbs import DETAINEE_CLASS, TERMS_SOURCED, VERB_TABLE
from ..loop import driver as D
from ..loop import resolve as R
from ..loop.driver import resolvable_verbs
from ..queries import world_q
from ..state.carriers import Question, Tenure
from .test_in10_record_operands import _acts, _formed, _hold_document
from .test_in12_arrest import DUKE, FAR, PRISONER, SEAT, WATCH, WATCHMAN, _act, _fold, _kinds, _world

BANDS = ("Overwhelming", "Success", "Partial", "Failure")
PETITION = "rec:pt_charge"


def _custody(w, who=PRISONER, seat=SEAT):
    w.add_tenure(Tenure(f"t_det_{who}", who, seat, "detain", since=w.tick))


def _charge(w, accused=PRISONER, holder=FAR, rid=PETITION):
    """A petition naming `accused` (its `terms`), held by `holder`, docketed with him -- what `carry`
    leaves behind (`_eff_carry`: the matter is the petition's `terms`, the item names the petition)."""
    _hold_document(w, w.persons[holder], "petition", {"terms": accused, "to": [SEAT], "from": "S"},
                   rec_id=rid)
    w.docket.append({"date": None, "matter": accused, world_q.DOCKET_ARRANGEMENT: None,
                     world_q.DOCKET_PETITION: rid})


def _duke_question(w):
    qs = world_q.questions_for(w, w.persons[DUKE])
    return qs[0] if qs else None


def _interrogations(w, q, who=DUKE):
    return [c for c in _formed(w, who, q) if c.verb == "interrogate"] if q is not None else []


class _Draws:
    """Counts every RNG the fold derives (`loop/resolve.py`'s `draw_factory`): a contest's roll is one."""
    def __init__(self):
        self.n = 0
        self._real = R.draw_factory

    def __call__(self, seed, tick):
        f = self._real(seed, tick)

        def g(*a):
            self.n += 1
            return f(*a)
        return g


def _fold_counting(w, d, act):
    spy = _Draws()
    with mock.patch.object(R, "draw_factory", spy):
        out = _fold(w, d, act)
    return out, spy.n


# ======================================================================================
# 1 -- THE ROW, AND THE DRIVER'S GATE CLAUSE
# ======================================================================================

def test_in12_interrogate_row_is_untyped_contested_one_kind_per_band_and_resolvable():
    row = VERB_TABLE["interrogate"]
    assert row.requires_typed is None and row.contests == "a proposition"
    assert row.counterparty == "subject" and row.referent_class == DETAINEE_CLASS == "Detainee"
    assert row.eligibility == ("remit:determine",)
    assert all(row.writes_at(b) == () for b in BANDS)
    kinds = [tuple(row.emits_by_degree[b]) for b in BANDS]
    assert all(len(k) == 1 for k in kinds) and len({k[0] for k in kinds}) == 4, kinds
    assert ("confession.made",) in kinds and ("confession.withheld",) in kinds
    assert row.emits_on_refusal == ("interrogation.refused",)
    assert "interrogate" in resolvable_verbs()
    cells, uncelled = table("alignment"), table_meta("alignment")["uncelled"]
    assert "interrogate" in uncelled and not [ax for ax in PURSUIT_AXES if "interrogate" in cells[ax]]


def test_in12_interrogate_planted_failure_the_gate_clause_is_what_admits_it():
    """The row's ground for the clause withdrawn (no `counterparty: subject`): gates one and two still
    pass, and the row leaves the resolvable set -- the contested gate's new clause is what admits it."""
    row = VERB_TABLE["interrogate"]
    bare = dataclasses.replace(row, counterparty="")
    assert bare.precondition_evaluable(D.REQUIRES_PREDICATES) and bare.effect_carried(D.EFFECTS)
    with mock.patch.dict(D.VERB_TABLE, {"interrogate": bare}):
        assert "interrogate" not in D.resolvable_verbs()
    assert "interrogate" in D.resolvable_verbs()


# ======================================================================================
# 2 -- THE FALSIFIER
# ======================================================================================

def test_in12_interrogate_the_custodian_forms_it_and_the_seam_emits_a_confession_kind():
    w, d = _world(pool_default=30)
    _custody(w)
    _charge(w)
    q = _duke_question(w)
    assert (PRISONER, DETAINEE_CLASS) in q.classes, q.classes
    cands = _interrogations(w, q)
    assert [c.subject for c in cands] == [PRISONER], [c.subject for c in cands]
    (act,) = [a for a in _acts(w, DUKE, cands) if a.verb == "interrogate"]
    assert act.via == SEAT
    out, draws = _fold_counting(w, d, act)
    row = VERB_TABLE["interrogate"]
    assert len(out) == 1 and out[0].degree in BANDS, (_kinds(out), out[0].degree)
    assert _kinds(out) == list(row.emits_by_degree[out[0].degree]), _kinds(out)
    assert _kinds(out)[0].startswith("confession.") and draws == 1, (_kinds(out), draws)


def test_in12_interrogate_planted_failure_stamper_off_nothing_is_formed():
    w, _ = _world(pool_default=30)
    _custody(w)
    _charge(w)
    assert _interrogations(w, _duke_question(w)), "CONTROL: formed with the stamper on"
    with mock.patch.object(world_q, "detainees_held", lambda w, p: ()):
        assert _interrogations(w, _duke_question(w)) == []


# ======================================================================================
# 3 -- THE CONTROL
# ======================================================================================

def test_in12_interrogate_control_a_free_man_is_never_offered_and_refused_before_any_draw():
    w, d = _world(pool_default=30)
    _charge(w)                                   # charged, not detained
    assert world_q.detainees_held(w, w.persons[DUKE]) == ()
    assert _interrogations(w, _duke_question(w)) == []
    out, draws = _fold_counting(w, d, _act("i0", "interrogate", DUKE, SEAT, subject=PRISONER))
    assert _kinds(out) == ["interrogation.refused"] and out[0].degree is None and draws == 0, \
        (_kinds(out), draws)


def test_in12_interrogate_control_custody_without_a_charge_is_refused_before_any_draw():
    w, d = _world(pool_default=30)
    _custody(w)
    out, draws = _fold_counting(w, d, _act("i1", "interrogate", DUKE, SEAT, subject=PRISONER))
    assert _kinds(out) == ["interrogation.refused"] and draws == 0, (_kinds(out), draws)


def test_in12_interrogate_control_custody_at_another_seat_is_not_offered():
    w, _ = _world(pool_default=30)
    _custody(w, seat=WATCH)                      # held by the watch, not the Duke's seat
    _charge(w)
    assert world_q.detainees_held(w, w.persons[DUKE]) == ()
    assert _interrogations(w, _duke_question(w)) == []
    # the watchman's seat grants no `determine`, so his own custody is no occasion either
    assert world_q.detainees_held(w, w.persons[WATCHMAN]) == ()


# ======================================================================================
# 4 -- STEP 5a: A WITNESS'S `commit` FROM THE HELD PETITION
# ======================================================================================

def _charge_proposition(w, d):
    assert _kinds(_fold(w, d, _act("u1", "utter", DUKE, None, proposition="prop_charge", mood="HOLDS",
                                   subject=PRISONER, predicate="murdered the reeve", value=True))) \
        == ["proposition.uttered"]


def _commits(w, who, rid):
    q = Question("q:held", "claim_landed", (), None, ((rid, "Record"),))
    return [c.subject for c in _formed(w, who, q) if c.verb == "commit"]


def test_in12_5a_a_witness_addressed_by_a_held_petition_commits_to_its_charge():
    assert TERMS_SOURCED["commit"] == ("dispensation", "petition")
    w, d = _world()
    _charge_proposition(w, d)
    _hold_document(w, w.persons[WATCHMAN], "petition",
                   {"terms": "prop_charge", "to": [WATCHMAN], "from": "S"}, rec_id="rec:pt1")
    assert "prop_charge" in _commits(w, WATCHMAN, "rec:pt1")
    assert _kinds(_fold(w, d, _act("c1", "commit", WATCHMAN, None, subject="prop_charge"))) \
        == ["commitment.made"]


def test_in12_5a_control_the_petitioner_holding_his_own_petition_forms_no_commit_on_it():
    w, d = _world()
    _charge_proposition(w, d)
    _hold_document(w, w.persons[FAR], "petition",
                   {"terms": "prop_charge", "to": [WATCHMAN], "from": "S"}, rec_id="rec:pt2")
    assert "prop_charge" not in _commits(w, FAR, "rec:pt2")
