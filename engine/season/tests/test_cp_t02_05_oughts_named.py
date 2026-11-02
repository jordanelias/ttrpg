"""v10 CP-T02-05 (B10-09; `-08` AM-B-11) -- the causes a person has heard of are ambitions on offer: the
stamper `world_q.oughts_named` is one more named term of `questions_for`'s `added` splice, so the OUGHT
Propositions among `person_q.ledger_names(p.ledger)` ride the question he answers as `Proposition`, and the
rows declaring that class (`commit`, `argue`) form on them. `release` declares no class and is not among them.

THE CUT CONDITION this item stood on (the home's own falsifier): REM-21 (iv)'s `own_referents_of_class`
already carries a heard-of Proposition only where the question is ABOUT it, which a witnessed
`proposition.uttered` claim is not (its subject is the actor, and the Proposition is outside the witness's
`reach`). Test (a)'s `before` assertion is that falsifier: with the term stubbed out, the witness's question
carries no Proposition. It does not hold, so the item is built.

  (a) A person who witnessed one `utter` of an OUGHT forms `commit` on it at his next deliberation and the act
      EXECUTES through the real fold -- a Proposition the actor did not utter. Mutation: remove the splice term
      and this is red (the stubbed arm below observes exactly that).
  (b) A person who heard of none forms none; and one who heard only of a Proposition of another mood forms
      none (the term is the OUGHTs among what he has heard, not every Proposition).
  (c) `release` is not among the rows that form on a heard-of Proposition; `argue` is, beside `commit`.

The seeded realm's reading (commit executions on a Proposition the actor did not utter, seeds 0-2, two
seasons, off against on) is a reading in the commit body, not an assertion here.
"""
import dataclasses

from engine.season.data.matrix import WriteClass
from engine.season.data.verbs import VERB_TABLE
from engine.season.harness import probes as P
from engine.season.loop.driver import SeasonDriver, mint_token
from engine.season.queries import person_q, world_q
from engine.season.state.carriers import Act

from .test_in53_vacancy_need import _formed
from .test_referent_class_stamps import _act_of

WITNESS = "p_mid"
UTTERER = "p_low"
STRANGER = "p_high"          # present in the world, witnessed nothing


def _fold(w, d, act):
    out = d.resolve(mint_token(w, WriteClass.ACTS), [act], contest_max_depth=w.fixtures.get("contest_max_depth"))
    w.log.extend(out)
    return out


def _heard(mood="OUGHT"):
    """`UTTERER` utters a Proposition of `mood`; the round's WITNESS deposits it in the ledgers of those with
    him (`WITNESS` among them, `STRANGER` not). Returns (world, driver, proposition id)."""
    w = P.tiny_world()
    d = SeasonDriver(w)
    d.matter(mint_token(d.w, WriteClass.MATTER), [])
    act = Act(id="t0205_u", actor=UTTERER, verb="utter", payload={"mood": mood})
    out = _fold(w, d, act)
    assert [e.kind for e in out] == ["proposition.uttered"]
    d.witness(mint_token(d.w, WriteClass.INTERIOR), out)
    pid = f"prop:{act.id}"
    assert w.propositions[pid].mood == mood
    return w, d, pid


def _classes(w, pid):
    qs = world_q.questions_for(w, w.persons[pid])
    return qs, {c for q in qs for c in q.classes}


def _commits_on(w, pid, prop):
    """The `commit` Candidates the person's delivered question forms on `prop`."""
    (q, *_) = world_q.questions_for(w, w.persons[pid])
    return [c for c in _formed(w, pid, q) if c.verb == "commit" and c.subject == prop]


def test_cp_t02_05_a_a_witness_of_an_utter_forms_commit_on_it_and_the_act_executes():
    w, d, prop = _heard()
    p = w.persons[WITNESS]
    # The witness heard of it and did not utter it: the Proposition is outside his reach (the cut condition's
    # route, REM-21 (iv), cannot carry it) and the term is what names it.
    assert prop in person_q.ledger_names(p.ledger)
    assert prop not in world_q.reach(w, p)
    assert world_q.oughts_named(w, p) == (prop,)
    qs, classes = _classes(w, WITNESS)
    assert (prop, "Proposition") in classes, qs
    (c,) = _commits_on(w, WITNESS, prop)
    assert not [t for t in p.tenures if t.object == prop], "he held nothing on it before"
    out = _fold(w, d, dataclasses.replace(_act_of(c, p), id="t0205_commit"))
    assert [e.kind for e in out] == ["commitment.made"]
    assert [t.kind for t in p.tenures if t.object == prop and t.live] == ["commit"]
    # Not a Proposition he uttered: the utterer's own hold is another person's edge.
    assert not [t for t in p.tenures if t.object == prop and t.kind == "hold"]


def test_cp_t02_05_a_a_person_with_a_live_commit_on_the_heard_of_proposition_forms_no_second_commit_and_argues_it():
    """B10-09 close one, D3 ([ASSUMPTION; medium; Jordan to correct; revert: drop `rosters.yaml: held_edge_declines`
    and restore the live-commit clause in `oughts_named`]). `_eff_commit` always opens a fresh Tenure, so a second
    `commit` on a Proposition he already commits to is a duplicate live edge: `opening_set`'s person-side decline does
    not form it. The STAMP is unnarrowed -- the cause he holds still rides his question -- so `argue` (he argues for what
    he holds right) forms on it toward the utterer he knows. The arm before it is the control (the same person, not yet
    committed, IS offered `commit`); a released commit offers it again."""
    w, d, prop = _heard()
    p = w.persons[WITNESS]
    assert world_q.oughts_named(w, p) == (prop,)                     # control: not yet committed
    (c,) = _commits_on(w, WITNESS, prop)
    assert [e.kind for e in _fold(w, d, dataclasses.replace(_act_of(c, p), id="t0205_c1"))] == ["commitment.made"]
    assert world_q.oughts_named(w, p) == (prop,), "the stamp was narrowed by his own commitment"
    qs, classes = _classes(w, WITNESS)
    assert (prop, "Proposition") in classes, qs
    formed = [c for q in qs for c in _formed(w, WITNESS, q) if c.subject == prop]
    assert not [c for c in formed if c.verb == "commit"], "a second commit on a cause he holds formed"
    argued_to = {(c.operands or {}).get("to") for c in formed if c.verb == "argue"}
    assert UTTERER in argued_to, ("he no longer argues for the cause he holds", argued_to)
    for t in p.tenures:                                               # ended: a cause he has let go is on offer again
        if t.kind == "commit" and t.object == prop:
            t.until = w.tick
    assert world_q.oughts_named(w, p) == (prop,)
    assert _commits_on(w, WITNESS, prop), "a released commit is not offered again"


def test_cp_t02_05_a_held_edge_declines_line_naming_no_verb_or_no_tenure_kind_is_refused_at_load():
    """`rosters.yaml: held_edge_declines`' one loader (`data/verbs.py::_load_held_edge_declines`), on a COPY of the
    shipped roster: the shipped line loads; a verb the table lacks, a kind `tenure_kinds` lacks, and an empty kind
    are each refused."""
    import pytest
    from engine.season.data import verbs as VERBS
    from engine.season.data.rosters import roster_map
    from engine.season.gaps import Forbidden
    shipped = dict(roster_map("held_edge_declines", "values"))
    assert VERBS._load_held_edge_declines(dict(shipped)) == VERBS.HELD_EDGE_DECLINES == {"commit": "commit"}
    for planted in ({**shipped, "no_such_verb": "commit"}, {**shipped, "commit": "no_such_kind"},
                    {**shipped, "commit": ""}):
        with pytest.raises(Forbidden, match="held_edge_declines"):
            VERBS._load_held_edge_declines(planted)


def test_cp_t02_05_a_mutation_without_the_splice_term_the_witness_is_offered_nothing(monkeypatch):
    """THE FALSIFIER (a) CAN OBSERVE ITS FAILURE: with the term stubbed out, REM-21's own-referent term does
    not carry the heard-of Proposition (the cut condition does not hold), and `commit` forms on nothing."""
    w, d, prop = _heard()
    monkeypatch.setattr(world_q, "oughts_named", lambda *a, **k: ())
    qs, classes = _classes(w, WITNESS)
    assert (prop, "Proposition") not in classes, qs
    assert all(prop not in q.referents for q in qs), qs
    assert not [c for q in qs for c in _formed(w, WITNESS, q) if c.verb == "commit"]


def test_cp_t02_05_b_a_person_who_heard_of_none_forms_none():
    w, d, prop = _heard()
    p = w.persons[STRANGER]
    assert not p.ledger and world_q.oughts_named(w, p) == ()
    qs, classes = _classes(w, STRANGER)
    assert qs == [] and classes == set()


def test_cp_t02_05_b_a_proposition_of_another_mood_is_not_a_cause_on_offer():
    w, d, prop = _heard(mood="WAR")
    p = w.persons[WITNESS]
    assert prop in person_q.ledger_names(p.ledger)          # he heard of it
    assert world_q.oughts_named(w, p) == ()                  # but it is no OUGHT
    qs, classes = _classes(w, WITNESS)
    assert (prop, "Proposition") not in classes, qs
    assert not [c for q in qs for c in _formed(w, WITNESS, q) if c.verb == "commit" and c.subject == prop]


def test_cp_t02_05_c_the_rows_that_form_on_a_heard_of_proposition_are_those_declaring_the_class():
    rows = sorted(v for v, r in VERB_TABLE.items() if r.referent_class == "Proposition")
    assert rows == ["argue", "commit"], rows
    assert VERB_TABLE["release"].referent_class == ""
    w, d, prop = _heard()
    (q, *_) = world_q.questions_for(w, w.persons[WITNESS])
    formed_on_it = {c.verb for c in _formed(w, WITNESS, q) if c.subject == prop}
    assert "commit" in formed_on_it and "release" not in formed_on_it, formed_on_it
