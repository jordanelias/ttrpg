"""Plan position `15` -- THE RECORD-KIND FOLD. `Petition` and `Dispensation` are kinds of `Record`
(`04_CODE_ARCHITECTURE.md` §B.5's synthesis call, PART A row 11), not two plain dicts on `World`.

What each block proves, and the control that stops it passing vacuously:

  1. THE SHARPENED FALSIFIER. `World` carries NO `petitions` and NO `dispensations` attribute --
     gone, not empty -- and a `hold` on a dispensation lands on a `Record` the invariant sweep
     recognises (the plan's first falsifier: *a `hold` on a dispensation refused because the store
     still has a second home*).
  2. ⊕L35 (r2 `05:671`). A Record whose `subject_matter` keys are not its kind's is refused, in both
     directions, and so is a kind `record_kinds` does not list. Control: the exact key set, and a
     `text` Record with `None` content, both construct.
  3. REACHABILITY, MEASURED RATHER THAN CLAIMED. `petition` is resolvable; `issue` is NOT (its
     `requires:` is prose -- position `19`'s) even though it now has an effect; `carry`'s
     precondition reaches a petition Record and the verb itself still has no effect (`H-63`).
  4. THE DEPOSIT RULE, IN A SEEDED SEASON. A filed petition deposits `content:petition` in the
     petitioner's own ledger, verbatim and frozen (hashable, `epistemic.Seen`'s precedent). Control: a `create_record` of kind `text` deposits NO
     content claim. The `dispensation` artifact (r2 `05:1245`) runs through the fold with a
     STAND-IN precondition for `issue`, and the control is that without it the fold refuses to
     evaluate the prose cell at all.
  5. TWO-SIDED (`ED-IN-0210` ruling 2). No Candidate is formed addressing a petition to its own
     petitioner (control: with the row's `counterparty:` cleared, one is); a hand-built
     self-addressed petition is refused and mints nothing; the loader refuses a counterparty the
     typed cell does not bind.
"""
import dataclasses

import pytest

from engine.season.data import verbs as _verbs
from engine.season.data.matrix import Step, WriteClass
from engine.season.data.rosters import RECORD_CONTENT, RECORD_KIND_KEYS
from engine.season.data.verbs import _OPENERS_FROM_EFFECTS, VERB_TABLE
from engine.season.decision.options import opening_set
from engine.season.gaps import Forbidden
from engine.season.harness import invariants as I
from engine.season.harness import probes as P
from engine.season.loop.driver import SeasonDriver, mint_token, resolvable_verbs
from engine.season.loop.effects import EFFECTS
from engine.season.loop.witness import content_value
from engine.season.queries.world_q import WorldReader, hold_force
from engine.season.state.carriers import Question, Record, View
from engine.season.state.world import World

_CONTENT = RECORD_CONTENT["predicate"]


def _mint(w, act):
    """Apply `act`'s effect through the gate at a synthetic RESOLVE barrier -- the probes' shape
    (`harness/probes.py::f5`), for a verb whose precondition the fold cannot yet evaluate."""
    w.step = Step.RESOLVE
    return w.write("exists", mint_token(w, WriteClass.ACTS), None, record_kind="Record",
                   fieldname="exists", driver="Act", actor=act.actor, via=act.via,
                   change=EFFECTS[act.verb](w, act))


def _content_claims(p, rid):
    return [c for c in p.ledger if c.subject == rid and str(c.predicate).startswith(f"{_CONTENT}:")]


# ======================================================================================
# 1 -- THE SHARPENED FALSIFIER: THE SECOND HOMES ARE GONE, AND A HOLD LANDS ON A RECORD
# ======================================================================================

def test_world_carries_no_petitions_and_no_dispensations_store():
    w = World(world_seed=0)
    assert not hasattr(w, "petitions") and not hasattr(w, "dispensations"), (
        "a second home for a document survives the fold")
    assert "petitions" not in World._STATE_COLLECTIONS
    assert "dispensations" not in World._STATE_COLLECTIONS
    assert "records" in World._STATE_COLLECTIONS


def test_a_hold_on_a_dispensation_lands_on_a_record_the_sweep_recognises():
    w = P.tiny_world()
    act = P.Act_(w, w.persons["p_high"], "issue",
                 payload={"subject": "prop_x", "to": ["p_low", "p_mid"]}, via="off_duke")
    _mint(w, act)
    rid = f"rec:{act.id}"
    rec = w.records[rid]
    assert rec.kind == "dispensation"
    h = hold_force(w, rid)
    assert h is not None and h.subject == "p_high" and h.live, "the issuer does not hold the writ"
    assert rid in I._entities(w), "the sweep's entity set cannot see the writ"
    assert not I.tenure_referent(w), I.tenure_referent(w)
    # WHERE IT IS DRAWN UP: the issuer's seat's rung, off `Act.via` (r2 `03` §A.10).
    assert rec.rung == w.offices["off_duke"].rung == "D", rec.rung


# ======================================================================================
# 2 -- ⊕L35: THE KEYS ARE THE KIND'S, EXACTLY, AND THE KIND IS A ROSTER MEMBER
# ======================================================================================

def test_l35_refuses_a_missing_key_an_extra_key_an_unknown_kind_and_a_non_mapping():
    keys = RECORD_KIND_KEYS["dispensation"]
    assert keys, "the dispensation kind declares no keys -- the refusal below would be vacuous"
    exact = {k: None for k in keys}
    missing = dict(list(exact.items())[:-1])
    extra = {**exact, "effect": "a bare effect field"}
    for bad in (missing, extra):
        with pytest.raises(Forbidden, match="subject_matter keys"):
            Record("r_bad", "S", "dispensation", subject_matter=bad)
    with pytest.raises(Forbidden, match="not a member of `record_kinds`"):
        Record("r_writ", "S", "writ")
    with pytest.raises(Forbidden, match="subject_matter of type"):
        Record("r_str", "S", "dispensation", subject_matter="levy the grain")
    # CONTROL: the exact key set constructs, and so does a keyless kind with no content.
    assert Record("r_ok", "S", "dispensation", subject_matter=exact).kind == "dispensation"
    assert Record("r_text", "S", "text").subject_matter is None
    assert Record("r_text2", "S", "text", subject_matter={}).kind == "text"
    with pytest.raises(Forbidden, match="subject_matter keys"):
        Record("r_text3", "S", "text", subject_matter={"terms": "x"})


# ======================================================================================
# 3 -- WHAT IS REACHABLE, MEASURED
# ======================================================================================

def test_petition_and_issue_are_resolvable_and_carry_is_not():
    """⚠ RENAMED AT PLAN POSITION `19` from `..._and_issue_and_carry_are_not`: this position gave
    `issue`'s prose cell its evaluable form (`verb_table.yaml`, `executors` + `authority`), so the
    effect `15` built is reachable through RESOLVE -- the flip `15`'s own assertion anticipated."""
    rv = resolvable_verbs()
    assert "petition" in rv, "petition has a typed precondition and an effect and is not resolvable"
    assert "issue" in EFFECTS, "issue lost its effect"
    assert "issue" in rv, "`issue` has a typed precondition (position `19`) and an effect (`15`)"
    assert VERB_TABLE["issue"].requires_typed is not None
    assert "carry" not in rv, "`carry` writes `(DocketItem, matter)` and has no effect (`H-63`)"
    for verb in ("issue", "petition"):
        assert VERB_TABLE[verb].writes == ("Record.exists",), VERB_TABLE[verb].writes
    # The derived opener map still sees the mint through the shared helper.
    assert {"confer", "create_record", "issue", "petition"} <= set(_OPENERS_FROM_EFFECTS["hold"])


def test_carrys_precondition_reaches_a_petition_record_and_only_a_petition():
    w = P.tiny_world()
    act = P.Act_(w, w.persons["p_low"], "petition",
                 payload={"record": "pet1", "subject": "p_mid", "to": "p_mid", "from": "Hh"})
    _mint(w, act)
    w.records["txt1"] = Record("txt1", "Hh", "text")
    rd = WorldReader(w, "p_mid")
    assert rd.read("pet1", "exists:petition") == 1
    assert rd.read("txt1", "exists:petition") == 0, "a text Record reads as a petition"
    assert rd.read("nothing", "exists:petition") == 0
    cell = VERB_TABLE["carry"].requires_typed
    assert cell is not None and "petition" in repr(cell), cell


# ======================================================================================
# 4 -- THE DEPOSIT RULE, IN A SEEDED SEASON
# ======================================================================================

def test_a_filed_petition_deposits_its_content_in_the_petitioners_own_ledger():
    w = P.tiny_world()

    def choose(p, v, s, ask_budget):
        if p.id == "p_low":
            return [P.Act_(w, p, "petition",
                           payload={"subject": "p_mid", "to": "p_mid", "from": "Hh"})]
        if p.id == "p_other":
            return [P.Act_(w, p, "create_record")]
        return []
    d = P._run_d(w, choose)
    kinds = [e.kind for e in w.log]
    assert "petition.filed" in kinds, kinds
    pets = [r for r in w.records.values() if r.kind == "petition"]
    assert len(pets) == 1, pets
    rec = pets[0]
    assert rec.subject_matter == {"terms": "p_mid", "to": ["p_mid"], "from": "Hh"}, rec
    assert rec.rung == "Hh", "a petition is drawn up where it rises from"
    assert hold_force(w, rec.id).subject == "p_low"
    got = _content_claims(w.persons["p_low"], rec.id)
    assert len(got) == 1, got
    assert got[0].predicate == f"{_CONTENT}:petition"
    assert got[0].value == content_value(rec.subject_matter), got[0].value
    assert dict(got[0].value) == {"terms": "p_mid", "to": ("p_mid",), "from": "Hh"}
    hash(got[0].value)   # frozen, on `epistemic.Seen`'s precedent: the harness sets it
    # nobody else learns what the document says -- only its holder
    assert not [c for pid, p in w.persons.items() if pid != "p_low"
                for c in _content_claims(p, rec.id)]
    # CONTROL: a `text` Record says nothing, and nothing is deposited for it.
    texts = [r for r in w.records.values() if r.kind == "text"]
    assert texts, "the control minted no text Record, so it observed nothing"
    assert not _content_claims(w.persons["p_other"], texts[0].id)
    assert d.resolved, "no act reached RESOLVE"


def test_the_dispensation_artifact_runs_through_the_real_precondition(monkeypatch):
    """r2 `05:1245`'s artifact -- *a season log showing a `content:dispensation` claim in the
    issuer's ledger*. ⚠ PLAN POSITION `19` RETIRED THE STAND-IN THIS TEST PLANTED (an always-true
    `REQUIRES_PREDICATES["issue"]`, *"for this test only"*, while the cell was prose) and renamed it
    from `..._with_a_stand_in_precondition_and_not_without`: the shipped cell now runs -- the
    executor is a person and `off_duke`'s purview reaches his home -- and everything after it is the
    shipped fold, effect and WITNESS, as before. THE CONTROL moved with it: the unpatched run used
    to refuse to EVALUATE the prose cell (`Unspecified`); now the same writ through NO seat is
    evaluated and refused (`issue.unauthorized`), and mints nothing. ⚠ `to` IS ONE ID, NOT A LIST:
    the cell's `existence` conjunct asks about one executor (the row's `requires_typed_note`); the
    mint still stores the addressee as a list, which the assertions below read."""
    def choose_for(w, via="off_duke"):
        def choose(p, v, s, ask_budget):
            if p.id == "p_high":
                return [P.Act_(w, p, "issue", via=via,
                               payload={"subject": "prop_x", "to": "p_low"})]
            return []
        return choose

    w = P.tiny_world()
    P._run_d(w, choose_for(w, via=None))
    assert "issue.unauthorized" in [e.kind for e in w.log], [e.kind for e in w.log]
    assert not [r for r in w.records.values() if r.kind == "dispensation"]

    w = P.tiny_world()
    P._run_d(w, choose_for(w))
    assert "dispensation.issued" in [e.kind for e in w.log]
    writs = [r for r in w.records.values() if r.kind == "dispensation"]
    assert len(writs) == 1, writs
    writ = writs[0]
    assert writ.subject_matter == {"terms": "prop_x", "to": ["p_low"], "at": None}, writ
    assert writ.rung == "D"
    got = _content_claims(w.persons["p_high"], writ.id)
    assert [c.predicate for c in got] == [f"{_CONTENT}:dispensation"], got
    assert dict(got[0].value) == {"terms": "prop_x", "to": ("p_low",), "at": None}, got[0].value
    assert got[0].source.startswith("firsthand")


# ======================================================================================
# 5 -- TWO-SIDED: A PETITION NEEDS A SECOND SIDE
# ======================================================================================

def _petition_candidates(w, pid):
    p = w.persons[pid]
    q = Question("q:fold", "need", ("p_low", "p_mid"))
    return [c for c in opening_set(p, View(pid, [], w.fixtures.get("view_k")), q, w.fixtures)
            if c.verb == "petition"]


def test_no_candidate_addresses_a_petition_to_its_own_petitioner(monkeypatch):
    w = P.tiny_world()
    got = _petition_candidates(w, "p_low")
    assert [c.operands.get("to") for c in got] == ["p_mid"], got
    assert got[0].operands.get("from") == "Hh", got[0].operands
    # CONTROL: clear the row's `counterparty:` and the self-addressed Candidate forms -- so the
    # column, not some other filter, is what declined it.
    monkeypatch.setitem(VERB_TABLE, "petition",
                        dataclasses.replace(VERB_TABLE["petition"], counterparty=""))
    assert sorted(c.operands.get("to") for c in _petition_candidates(w, "p_low")) == [
        "p_low", "p_mid"]


def test_a_hand_built_self_addressed_petition_is_refused_and_mints_nothing():
    w = P.tiny_world()
    before = dict(w.records)

    def choose(p, v, s, ask_budget):
        if p.id == "p_low":
            return [P.Act_(w, p, "petition",
                           payload={"subject": "p_low", "to": "p_low", "from": "Hh"})]
        return []
    P._run_d(w, choose)
    kinds = [e.kind for e in w.log]
    assert "petition.refused" in kinds and "petition.filed" not in kinds, kinds
    assert w.records == before, "a refused petition left a Record behind"


def test_the_loader_refuses_a_counterparty_the_typed_cell_does_not_bind(monkeypatch):
    real = _verbs.load_yaml

    def planted(text):
        doc = real(text)
        if isinstance(doc, dict) and "verbs" in doc:
            for r in doc["verbs"]:
                if r.get("verb") == "petition":
                    r["counterparty"] = "site"
        return doc
    monkeypatch.setattr(_verbs, "load_yaml", planted)
    with pytest.raises(SystemExit, match="does not bind"):
        _verbs._load_verb_table()
