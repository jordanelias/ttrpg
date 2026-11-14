"""v10 CP-T05-02 parts (ii) and (iii) (batch B10-13; home T05 §2 CP-T05-02, `-08` AM-D-02): THE ACCUSED ANSWERS.

Part (i) (`hearing`, `hearing_step`) is HELD on SC-02's design and is not built or tested here.

  * (ii) THE GUARD -- `seam/wrappers/sigma.py::contest_input` reads NO opposition when the subject IS the actor
    (nobody opposes himself), so the self-plea's obstacle carries no opposition term at any capability he holds: on the
    shipped `task` arm (B11 lane A) it is the task's difficulty alone (`speak`'s, `rosters.yaml: task_difficulty`), on
    the `stand_in` control arm `obstacle_default`.
    FALSIFIER: a pleader with `speak`'s capability seeded at 3 rolls the self-plea at the same obstacle as with
    capability 0. CONTROL: the same person as someone ELSE's subject opposes at his capability (the guard does not
    swallow the opposed case). PLANTED FAILURE (run 2026-11-08, reverted): the guard's condition made `False` (the
    score read for a self-subject) -> the capability-3 pleader's `opposition` reads 3.0 and the first test reds.
  * (iii) THE SELF-PLEA -- the row column `subject_may_be_self` on `speak` ALONE waives `opening_set`'s self-subject
    decline for the row declaring it: a person docketed, holding the docketing claim, forms `speak {subject: himself}`
    and forms none with the column removed. PLANTED FAILURE (run 2026-11-08, reverted): the waiver
    `and not row.subject_may_be_self` dropped from `opening_set` -> the formation test reds.
  * THE LOADER admits the column only on a row contested against its subject (`VerbRow.opponent_operand() ==
    "subject"`); `confer`'s `counterparty_may_be_self` is a different column and is untouched.
"""
from __future__ import annotations

import dataclasses
import importlib

import pytest

from engine.substrate import composition

from ..data import verbs as _verbs
from ..data.matrix import WriteClass
from ..data.rosters import VERB_CAPABILITY
from ..data.verbs import VERB_TABLE
from ..decision import assemble
from ..decision.options import opening_set, subject_is_opponent
from ..loop.driver import mint_token
from ..queries import world_q
from ..seam.wrappers import sigma
from .test_sc01_speak import PARTY, SPEAKER, _docket, _speak
from .test_u7_remit import _fold, _kinds, _plant, _world

KEY = VERB_CAPABILITY["speak"]


def revert_cp_t05_02(monkeypatch):
    """The self-plea OFF, in process: `speak` declares no `subject_may_be_self`, so `opening_set` declines the docketed
    party's own matter as before. (The guard, (ii), is hash-neutral and needs no revert.) Other tests that pin a
    pre-item trajectory call it."""
    monkeypatch.setitem(VERB_TABLE, "speak", dataclasses.replace(VERB_TABLE["speak"], subject_may_be_self=False))


def _obstacle(w, claimants, subject):
    roll = importlib.import_module(composition.require("social_contest.roll").__module__)
    inp = sigma.contest_input(w, claimants, verb="speak", subject=subject)
    return inp, roll.obstacle(inp)


# ---------------------------------------------------------------------------------------------
# (ii) THE GUARD
# ---------------------------------------------------------------------------------------------

def test_a_self_plea_rolls_at_the_same_obstacle_at_any_capability_the_pleader_holds():
    seen = {}
    for score in (0, 3):
        w, _ = _world()
        w.persons[SPEAKER].capability = {KEY: score}
        inp, ob = _obstacle(w, [SPEAKER], SPEAKER)
        assert inp.opposition is None, (score, inp.opposition)
        seen[score] = (inp.obstacle_default, ob)
    assert seen[0] == seen[3], seen            # no opposition term (the task's difficulty alone, shipped), the same either way
    assert len(seen) == 2


def test_the_control_the_same_person_as_anothers_subject_still_opposes_at_his_capability():
    w, _ = _world()
    w.persons[SPEAKER].capability = {KEY: 3}
    inp, _ob = _obstacle(w, [PARTY], SPEAKER)      # SPEAKER is another's subject: the score IS read
    assert inp.opposition == 3.0, inp.opposition
    inp0, _ = _obstacle(w, [SPEAKER], SPEAKER)     # and his own subject: it is not
    assert inp0.opposition is None


# ---------------------------------------------------------------------------------------------
# (iii) THE SELF-PLEA
# ---------------------------------------------------------------------------------------------

def _docketed_party():
    """The Duke opens a case on PARTY; PARTY holds the docketing claim (the Duke's own `case.opened` claim, the
    deposit `docket_question` reads, copied into PARTY's ledger -- the witness reaches the opener alone here)."""
    w, d = _world()
    _docket(w, d)
    d.witness(mint_token(w, WriteClass.INTERIOR), [e for e in w.log if e.kind == "case.opened"])
    claim = next(c for c in w.persons["p_high"].ledger if c.predicate == "case.opened")
    w.persons[PARTY].ledger.append(dataclasses.replace(claim, holder=PARTY))
    return w, d


def _speak_formed(w, pid=PARTY):
    p = w.persons[pid]
    q = world_q.docket_question(w, p)
    assert q is not None and pid in q.referents, q
    return [(c.verb, c.subject) for c in opening_set(p, assemble(p, q, 12), q, w.fixtures) if c.verb == "speak"]


def test_a_docketed_party_forms_the_self_plea_under_the_column_and_none_without_it(monkeypatch):
    w, _ = _docketed_party()
    assert VERB_TABLE["speak"].subject_may_be_self is True
    assert _speak_formed(w) == [("speak", PARTY)]
    revert_cp_t05_02(monkeypatch)
    assert _speak_formed(w) == []                  # the decline is the revert: the column


def test_the_column_is_on_speak_alone_and_confers_own_column_is_another():
    assert [v for v, r in VERB_TABLE.items() if r.subject_may_be_self] == ["speak"]
    assert [v for v, r in VERB_TABLE.items() if r.counterparty_may_be_self] == ["confer"]


def test_the_self_plea_executes_through_the_fold_at_a_band():
    w, d = _docketed_party()
    out = _fold(w, d, _speak("selfplea", actor=PARTY, subject=PARTY))
    bands = {k for ks in VERB_TABLE["speak"].emits_by_degree.values() for k in ks}
    assert len(out) == 1 and out[0].kind in bands, _kinds(out)


@pytest.mark.parametrize("verb,mutate,match", [
    ("tell", lambda r: r.__setitem__("subject_may_be_self", True), "subject_may_be_self, but its act is not contested"),
    ("speak", lambda r: r.__setitem__("subject_may_be_self", "true"), "declares subject_may_be_self 'true'"),
])
def test_the_loader_refuses_the_column_off_a_row_contested_against_its_subject(monkeypatch, verb, mutate, match):
    _plant(monkeypatch, verb, mutate)
    with pytest.raises(SystemExit, match=match):
        _verbs._load_verb_table()


def test_the_loader_admits_the_column_on_a_row_contested_against_its_subject(monkeypatch):
    """`determine` names `counterparty: subject` (CR-16): the same rule admits it. Control for the refusals above."""
    row = VERB_TABLE["determine"]
    assert subject_is_opponent(row) and row.opponent_operand() == "subject"
    _plant(monkeypatch, "determine", lambda r: r.__setitem__("subject_may_be_self", True))
    assert _verbs._load_verb_table()["determine"].subject_may_be_self is True


# ---------------------------------------------------------------------------------------------
# THE STANCE SIGN (Phase 1 of the B10-13 close: A1)
# ---------------------------------------------------------------------------------------------

def test_a_self_plea_is_scored_for_himself_and_an_accusation_against_another(monkeypatch):
    """`_stance_arm` negates `regard` on a row contested against its subject (the `declared` polarity, CR-16: an act
    AGAINST somebody you like scores down). `subject_is_opponent` encodes 'a person is not his own adversary', so a
    self-plea (`speak` on himself) is not that act and reads `+regard`. FALSIFIER: with a held regard of -3 the
    self-plea reads -3.0 and `speak` on another reads +3.0; PLANTED FAILURE (run 2026-11-08, reverted): the guard
    `subject != p.id` dropped -> the self-plea reads +3.0 and this test reds. CONTROL: the `regard` arm reads the
    same -3.0 for both."""
    from ..decision import choose as CH
    from ..data.fixtures import DEFAULT_FIXTURES
    from ..state.carriers import Candidate
    w = _world()[0]
    p = next(iter(w.persons.values()))
    monkeypatch.setattr(CH, "regard", lambda person, subject, fx: -3.0)
    declared = DEFAULT_FIXTURES.sweep("stance_polarity", "declared")
    regard_arm = DEFAULT_FIXTURES.sweep("stance_polarity", "regard")
    assert subject_is_opponent(VERB_TABLE["speak"])
    own, other = Candidate("speak", p.id), Candidate("speak", "p_someone_else")
    assert CH._stance_arm(p, own, declared, {}) == -3.0
    assert CH._stance_arm(p, other, declared, {}) == 3.0
    assert CH._stance_arm(p, own, regard_arm, {}) == CH._stance_arm(p, other, regard_arm, {}) == -3.0
