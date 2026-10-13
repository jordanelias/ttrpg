"""IN-10 (a) (H-203, DECISION 2026-10-13 [ASSUMPTION; medium; Jordan to correct]) -- `oblige`
FORMABLE: a person forms an `oblige` on a seat he has been TOLD OF, and on no other.

#453 `:524`: *"type clause 1 once a seat can be a referent -- from a held Record's `terms` (the
enabler) or a `tenure.opened` deposit (K-25)"*; `:1389-1391`: the row is unchanged. Built as
`referent_class: Office` on the untyped row (IN-53 D1's partition), fed by
`queries/world_q.py::seats_named` (a ledger claim about the seat, or a held document whose `terms`
names it), spliced onto the question the person answers in `questions_for`, and the seat carried on
`subject` by `decision/options.py::_operands` so both counterparty clauses see it.

  (1) `seats_named`: nothing for a person told of nothing; the seat for a deposit about it and for a
      held document whose `terms` names it; NOT for a document naming it only as its addressee;
  (2) `questions_for` carries the named seat as an `Office` referent on its first question, and with
      no claim the questions are unchanged (the control);
  (3) the Candidate formed from that question folds to `duty.taken` -- the edge `establishment_of`
      reads -- and a person told of no seat forms none;
  (4) THE FALSIFIER IN COMPUTED PLAY (`build_realm(0)`, 4 seasons, the real chooser): every `oblige`
      act any person attempted names a seat his own ledger was told of.

MUTATIONS, run at the build: `seats_named` returning every office (the seat no longer named by a
deposit or a Record) reddens (1) and (2) -- formation still holds, because `referent_named` asks the
same owner (`person_q.ledger_names`) person-side; deleting that decline in `opening_set` reddens
`test_in10a_a_conferrers_vacancy_is_not_a_seat_he_was_told_of` and `test_obligees.py::test_17a_...`.
"""
from collections import Counter

import pytest

from engine.season.data.matrix import WriteClass
from engine.season.decision import assemble
from engine.season.decision.choose import _payload_of
from engine.season.decision.options import opening_set
from engine.season.harness import probes as P
from engine.season.loop.driver import SeasonDriver, mint_token
from engine.season.queries import world_q
from engine.season.state.carriers import Act, Claim

# One `realm_4s` build per run: every test of this file goes to one xdist worker with the other two
# realm files' under CI's `--dist loadgroup` (`conftest.py::realm_4s`).
pytestmark = pytest.mark.xdist_group("realm_4s")

SEAT = "off_duke"


def _world():
    w = P.tiny_world()
    d = SeasonDriver(w)
    d.matter(mint_token(w, WriteClass.MATTER), [])
    return w, d


def _told(w, pid, subject, predicate="tenure.opened", value=True, n=0):
    w.persons[pid].ledger.append(Claim(f"c_told_{pid}_{n}", pid, subject, predicate, value, 0,
                                       "firsthand", 100, "own"))


def _oblige_formed(w, pid):
    p = w.persons[pid]
    qs = world_q.questions_for(w, p)
    if not qs:
        return []
    return [c for c in opening_set(p, assemble(p, qs[0], 12), qs[0], w.fixtures)
            if c.verb == "oblige"]


# (1) ----------------------------------------------------------------------------------------------

def test_in10a_seats_named_reads_deposits_and_a_held_documents_terms_only():
    w, _ = _world()
    p = w.persons["p_mid"]
    assert world_q.seats_named(w, p) == ()
    _told(w, "p_mid", SEAT)
    assert world_q.seats_named(w, p) == (SEAT,)
    w2, _ = _world()
    _told(w2, "p_mid", "rec_w", "content:dispensation",
          (("terms", SEAT), ("to", ("p_mid",)), ("at", None)))
    assert world_q.seats_named(w2, w2.persons["p_mid"]) == (SEAT,)
    w3, _ = _world()
    _told(w3, "p_mid", "rec_w", "content:dispensation",
          (("terms", "p_low"), ("to", (SEAT,)), ("at", None)))
    assert world_q.seats_named(w3, w3.persons["p_mid"]) == (), "an addressee is not what it is about"


# (2) ----------------------------------------------------------------------------------------------

def test_in10a_questions_carry_a_named_seat_as_an_office_and_nothing_otherwise():
    w, _ = _world()
    p = w.persons["p_mid"]
    before = world_q.questions_for(w, p)
    assert all(not q.classes for q in before)
    _told(w, "p_mid", SEAT)
    after = world_q.questions_for(w, p)
    assert after and (SEAT, "Office") in after[0].classes, after[:1]
    assert all(not q.classes for q in after[1:])
    # the plain referents, id and source of the question he answers are not touched (the partition)
    if before:
        assert (after[0].id, after[0].source) == (before[0].id, before[0].source)


# (3) ----------------------------------------------------------------------------------------------

def test_in10a_a_seat_he_was_told_of_forms_an_oblige_that_executes():
    w, d = _world()
    assert _oblige_formed(w, "p_mid") == [], "an `oblige` formed with no seat named"
    _told(w, "p_mid", SEAT)
    got = _oblige_formed(w, "p_mid")
    assert [(c.subject, c.operands) for c in got] == [(SEAT, {"subject": SEAT})], got
    a = Act(id="ob_in10a", actor="p_mid", verb="oblige", payload=_payload_of(got[0]))
    out = d.resolve(mint_token(w, WriteClass.ACTS), [a],
                    contest_max_depth=w.fixtures.get("contest_max_depth"))
    assert [e.kind for e in out] == ["duty.taken"], [e.kind for e in out]
    assert "p_mid" in world_q.establishment_of(w, SEAT)


def test_in10a_a_conferrers_vacancy_is_not_a_seat_he_was_told_of():
    """ONE CLASS, TWO SOURCES (`referent_named`): `p_king` may fill the vacant `off_reeve`, so his
    question carries it as `Office` and `confer` forms on it -- but no deposit or held document names
    it to him, so `oblige` does not. Told of it, it does."""
    from .test_g3_not_yours import _gov_world
    w, _ = _gov_world()
    p = w.persons["p_king"]
    (q,) = world_q.questions_for(w, p)
    assert ("off_reeve", "Office") in q.classes, q
    got = opening_set(p, assemble(p, q, 12), q, w.fixtures)
    assert any(c.verb == "confer" and c.subject == "off_reeve" for c in got)
    assert not [c for c in got if c.verb == "oblige"], "an `oblige` formed on an untold vacancy"
    _told(w, "p_king", "off_reeve")
    (q,) = world_q.questions_for(w, p)
    got = opening_set(p, assemble(p, q, 12), q, w.fixtures)
    assert "off_reeve" in {c.subject for c in got if c.verb == "oblige"}


def test_in10a_the_seat_holder_is_offered_his_own_seat_and_the_fold_refuses_it():
    """The referent is a fact about what he was told, not a filter on what he may do: the duke told
    of his own seat forms the Candidate and `_req_oblige` clause 3 refuses it (`duty.refused`)."""
    w, d = _world()
    _told(w, "p_high", SEAT)
    got = _oblige_formed(w, "p_high")
    assert [c.subject for c in got] == [SEAT]
    a = Act(id="ob_in10a_self", actor="p_high", verb="oblige", payload=_payload_of(got[0]))
    out = d.resolve(mint_token(w, WriteClass.ACTS), [a],
                    contest_max_depth=w.fixtures.get("contest_max_depth"))
    assert [e.kind for e in out] == ["duty.refused"], [e.kind for e in out]


@pytest.mark.parametrize("verb,value,match", [
    ("oblige", "true", "is `true` or `false`"),
    ("give", True, "without a referent_class"),
])
def test_in10a_the_loader_refuses_a_malformed_referent_named(monkeypatch, verb, value, match):
    from engine.season.data import verbs as _verbs
    from .test_in53_vacancy_need import _planted
    _planted(monkeypatch, verb, "referent_named", value)
    with pytest.raises(SystemExit, match=match):
        _verbs._load_verb_table()


def test_in10a_the_declarations_as_built():
    from engine.season.data.verbs import VERB_TABLE
    # RE-RECORDED AT v9 IN-09: `comply` declares it too (was `{"oblige"}`).
    assert {v for v, r in VERB_TABLE.items() if r.referent_named} == {"oblige", "comply"}
    assert VERB_TABLE["oblige"].referent_class == "Office"


# (4) THE FALSIFIER AND THE EXIT IN COMPUTED PLAY: `build_realm(0)`, 4 SEASONS, THE REAL CHOOSER -----
#
# `aperture 4 0` (the plan's instrument) reads the realm row; this is its unit form, at the same
# seasons and seed. Measured at the build: the season-4 self-conferral (`p_npc_032` onto
# `off_npc_082`, IN-53) deposits `tenure.opened` claims about the seat on its witnesses, who
# re-deliberate in the same season's later rounds and oblige to it.

# The 4-season run, with the `oblige` formations recorded, is `conftest.py::realm_4s`.


def test_in10a_falsifier_no_oblige_forms_on_a_seat_nobody_told_him_of(realm_4s):
    _, _, _, formed = realm_4s
    assert formed, "no `oblige` Candidate formed, so the falsifier observed nothing"
    untold = [f for f in formed if not f[2]]
    assert not untold, untold[:5]


def test_in10a_exit_oblige_executes_in_computed_play(realm_4s):
    w, _, rows, _ = realm_4s
    taken = [a for a, made, _ in rows if a.verb == "oblige" and "duty.taken" in made]
    assert taken, sorted(Counter(a.verb for a, made, _ in rows if made).items())
    assert all(a.payload["subject"] in w.offices for a in taken)


def test_in10a_the_partition_moves_no_other_rows_formations():
    """THE CROWD-OUT CONTROL AT FORMATION, BY CONSTRUCTION (`test_in53v_a_the_partition_...`'s form,
    with every person TOLD OF every seat): every row declaring no `referent_class:` forms exactly
    what the same question forms with its classed referents stripped."""
    from engine.season.data.verbs import VERB_TABLE
    from .test_g3_not_yours import _gov_world
    import dataclasses
    classed_rows = {v for v, r in VERB_TABLE.items() if r.referent_class}
    w, _ = _gov_world()
    for i, pid in enumerate(w.persons):
        for j, o in enumerate(sorted(w.offices)):
            _told(w, pid, o, n=f"{i}_{j}")
    checked = 0
    for pid, p in w.persons.items():
        for q in world_q.questions_for(w, p):
            v = assemble(p, q, 12)
            got = opening_set(p, v, q, w.fixtures)
            bare = opening_set(p, v, dataclasses.replace(q, classes=()), w.fixtures)
            sig = lambda cs: sorted(repr((c.verb, c.subject, sorted(c.operands.items()))) for c in cs)
            assert sig(c for c in got if c.verb not in classed_rows) == sig(bare), (pid, q.id)
            checked += any(c.verb == "oblige" for c in got)
    assert checked >= 3, checked
