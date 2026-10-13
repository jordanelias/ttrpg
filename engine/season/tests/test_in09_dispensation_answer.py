"""v9 IN-09 (`19b`, U7-disp; H-203, DECISION 2026-10-13 [ASSUMPTION; medium; Jordan to correct]) --
`comply`, the act that answers a dispensation, typed on THE HELD WRIT (J-2 arm A) and formed only on a
writ the person holds. `evade / defy` and `construe` were typed beside it and REVERTED to their base
rows (each executed 0 times through the real chooser; H-203's IN-09 OUTCOME and AMENDED, checkpoints
`a1c83e62`, `60073e75`).

The cell: `existence` of `subject` kind `dispensation` + `own_ledger` of `subject`. Formation:
`queries/world_q.py::writs_held` stamps the dispensations on a person's live `hold` edges onto the
question he answers as `Record` (IN-53 D1's partition), and the row declares `referent_class: Record`
+ `referent_named: true` (IN-10 (a)'s column), so a Candidate forms only on a held writ his own ledger
names.

  (1) THE ROW: typed, resolvable, emission-only (no effect the fold would never call);
  (2) THE CARRIED FALSIFIER, through the real fold: `comply` for a person whose ledger holds no claim
      of the terms -> `compliance.impossible`; the control, his content claim in hand -> executed;
  (3) a claim on a person, or on a text, answers no writ (the `existence` conjunct);
  (4) the cell does not ask for the writ in hand: a reader of its terms complies;
  (5) FORMATION: `writs_held`/`questions_for` stamp a held writ and nothing else; `comply` forms on it
      only once his ledger names it; with no writ held the questions are unchanged (the control);
  (6) THE CROWD-OUT CONTROL AT FORMATION (`test_in53v_a_the_partition_moves_no_other_rows_formations`'
      form): every row declaring no `referent_class:` forms exactly what the question forms stripped;
  (7) THE FALSIFIER AND THE EXIT IN COMPUTED PLAY (`conftest.py::realm_4s`: `build_realm(0)`, 4
      seasons, the real chooser): every attempted `comply` answers a writ its actor held and the fold
      admitted, and `comply` EXECUTES >= 1.

MUTATIONS, run at the build on the unit tests (the realm half not re-run under them): `writs_held`
returning `()` reddens (5) twice and (6); the `own_ledger` conjunct deleted from `comply` reddens (2);
`referent_named` dropped reddens (1) and (5)'s 'not before his ledger names it'.
"""
from collections import Counter
import dataclasses

import pytest

from engine.season.data.matrix import Step, WriteClass
from engine.season.data.rosters import RECORD_CONTENT
from engine.season.data.verbs import RECORD_REFERENT_KINDS, VERB_TABLE
from engine.season.decision import assemble
from engine.season.decision.options import opening_set
from engine.season.harness import probes as P
from engine.season.loop.driver import SeasonDriver, mint_token, resolvable_verbs
from engine.season.loop.effects import EFFECTS
from engine.season.loop.witness import content_value
from engine.season.queries import world_q
from engine.season.queries.world_q import hold_force
from engine.season.state.carriers import Act, Claim

# One `realm_4s` build per run: every test of this file goes to one xdist worker with the other two
# realm files' under CI's `--dist loadgroup` (`conftest.py::realm_4s`).
pytestmark = pytest.mark.xdist_group("realm_4s")

VERB, GIVEN, REFUSED = "comply", "compliance.given", "compliance.impossible"
HOLDER, OTHER = "p_low", "p_mid"                  # `tiny_world`: both in Hh
WRIT = "rec_writ"
_CONTENT = RECORD_CONTENT["predicate"]
TERMS = {"terms": OTHER, "to": [HOLDER], "at": None}


def _with_writ(kind="dispensation"):
    """`tiny_world` at a RESOLVE barrier, `HOLDER` holding a Record of `kind` minted through the real
    fold (`create_record` declaring the kind: the one mint `issue` shares). No claim on it is in
    anyone's ledger yet -- WITNESS has not run."""
    w = P.tiny_world()
    d = SeasonDriver(w)
    d.matter(mint_token(w, WriteClass.MATTER), [])
    w.step = Step.RESOLVE
    sm = TERMS if kind == "dispensation" else None
    out = d._fold(w, mint_token(w, WriteClass.ACTS),
                  Act(id="mk", actor=HOLDER, verb="create_record",
                      payload={"record": WRIT, "kind": kind, "subject_matter": sm}))
    assert [e.kind for e in out] == ["record.created"], [e.kind for e in out]
    assert w.records[WRIT].kind == kind
    assert hold_force(w, WRIT).subject == HOLDER, "fixture: the maker does not hold the writ"
    return w, d


def _claim(w, pid, subject, predicate, value, cid):
    w.persons[pid].ledger.append(
        Claim(cid, pid, subject, predicate, value, w.tick, "firsthand", 100, "own"))


def _read_terms(w, pid):
    """The `content:dispensation` claim -- the deposit WITNESS makes for a new holder."""
    _claim(w, pid, WRIT, f"{_CONTENT}:dispensation", content_value(w.records[WRIT].subject_matter),
           f"c_terms_{pid}")


def _fold(w, d, actor, verb, subject, key):
    return [e.kind for e in d._fold(w, mint_token(w, WriteClass.ACTS),
                                    Act(id=key, actor=actor, verb=verb,
                                        payload={"subject": subject}))]


def _formed(w, pid, q):
    p = w.persons[pid]
    return opening_set(p, assemble(p, q, 12), q, w.fixtures)


def _sig(cs):
    return sorted(repr((c.verb, c.subject, sorted(c.operands.items()))) for c in cs)


# (1) ----------------------------------------------------------------------------------------------

def test_in09_the_row_is_typed_resolvable_classed_and_emission_only():
    row = VERB_TABLE[VERB]
    assert row.requires_typed is not None, "the cell is still untyped"
    assert not row.requires_decline_note, "a stale `requires_decline_note:`"
    assert VERB in resolvable_verbs(), "the fold still cannot carry it"
    assert row.writes == (), f"declares writes {row.writes} -- not emission-only"
    assert VERB not in EFFECTS, "an effect the fold never calls (`ID-13`)"
    assert (row.referent_class, row.referent_named) == ("Record", True)


def test_in09_the_record_class_is_declared_by_comply_alone_and_answers_dispensations():
    assert {v for v, r in VERB_TABLE.items() if r.referent_class == "Record"} == {VERB}
    assert RECORD_REFERENT_KINDS == frozenset({"dispensation"})


# (2) THE CARRIED FALSIFIER -------------------------------------------------------------------------

def test_in09_falsifier_no_claim_of_the_terms_refuses_and_holding_one_admits():
    """*`comply` evaluable for a person whose ledger holds no claim of the terms -> fail*. The actor
    holds the writ and it IS a dispensation, so the one conjunct left to refuse is the ledger's."""
    w, d = _with_writ()
    assert not [c for c in w.persons[HOLDER].ledger if c.subject == WRIT], "fixture: a claim held"
    assert _fold(w, d, HOLDER, VERB, WRIT, "a1") == [REFUSED], (
        "`comply` admitted for a person whose ledger holds no claim of the terms")
    _read_terms(w, HOLDER)
    assert _fold(w, d, HOLDER, VERB, WRIT, "a2") == [GIVEN]


# (3) THE WRIT CONJUNCT -----------------------------------------------------------------------------

def test_in09_a_claim_on_a_person_or_a_text_answers_no_writ():
    w, d = _with_writ()
    _claim(w, HOLDER, OTHER, "exists:Person", 1, "c_person")
    assert _fold(w, d, HOLDER, VERB, OTHER, "p1") == [REFUSED]
    w2, d2 = _with_writ(kind="text")
    _claim(w2, HOLDER, WRIT, "record.created", True, "c_text")
    assert _fold(w2, d2, HOLDER, VERB, WRIT, "p2") == [REFUSED]


# (4) THE CELL DOES NOT ASK FOR THE WRIT IN HAND ----------------------------------------------------

def test_in09_a_reader_of_the_terms_who_does_not_hold_the_writ_complies():
    """A claim of its terms is the whole cell (§E3 `:430`); formation (5) is what offers it to the
    holder alone in computed play."""
    w, d = _with_writ()
    _read_terms(w, OTHER)
    assert _fold(w, d, OTHER, VERB, WRIT, "c3") == [GIVEN]


# (5) FORMATION -------------------------------------------------------------------------------------

def test_in09_writs_held_stamps_a_held_dispensation_and_nothing_else():
    w, _ = _with_writ()
    assert world_q.writs_held(w, w.persons[HOLDER]) == (WRIT,)
    assert world_q.writs_held(w, w.persons[OTHER]) == ()
    wt, _ = _with_writ(kind="text")
    assert world_q.writs_held(wt, wt.persons[HOLDER]) == (), "a held text is no writ"
    hold_force(w, WRIT).until = w.tick            # given away / ended: no longer his
    assert world_q.writs_held(w, w.persons[HOLDER]) == ()


def test_in09_comply_forms_on_the_held_writ_once_his_ledger_names_it():
    w, _ = _with_writ()
    p = w.persons[HOLDER]
    qs = world_q.questions_for(w, p)
    assert qs and (WRIT, "Record") in qs[0].classes, qs[:1]
    assert all((WRIT, "Record") not in q.classes for q in qs[1:])
    assert not [c for c in _formed(w, HOLDER, qs[0]) if c.verb == VERB], (
        "formed on a writ his own ledger does not name")
    _read_terms(w, HOLDER)
    qs = world_q.questions_for(w, p)
    got = {(c.verb, c.subject) for c in _formed(w, HOLDER, qs[0]) if c.verb == VERB}
    assert got == {(VERB, WRIT)}, sorted(got)


def test_in09_with_no_writ_held_the_questions_are_unchanged():
    """The control: the non-holder's questions carry no `Record` class, and a held writ's ending
    returns the holder's to what they were before he held one."""
    w, _ = _with_writ()
    assert all(not [c for c in q.classes if c[1] == "Record"]
               for q in world_q.questions_for(w, w.persons[OTHER]))
    held = world_q.questions_for(w, w.persons[HOLDER])
    hold_force(w, WRIT).until = w.tick
    after = world_q.questions_for(w, w.persons[HOLDER])
    assert all(not [c for c in q.classes if c[1] == "Record"] for q in after)
    assert [(q.id, q.source, q.referents) for q in after] == \
        [(q.id, q.source, q.referents) for q in held if q.source != "need" or q.referents], (held, after)


# (6) THE CROWD-OUT CONTROL AT FORMATION ------------------------------------------------------------

def test_in09_the_partition_moves_no_other_rows_formations():
    """Every person holds a writ his ledger names, and is told of a person: every row declaring no
    `referent_class:` forms exactly what the same question forms with its classed referents
    stripped, and stripped, `comply` forms nothing."""
    classed_rows = {v for v, r in VERB_TABLE.items() if r.referent_class}
    w, d = _with_writ()
    for i, pid in enumerate(sorted(w.persons)):
        rid = WRIT if pid == HOLDER else f"rec_w{i}"
        if pid != HOLDER:
            out = d._fold(w, mint_token(w, WriteClass.ACTS),
                          Act(id=f"mk{i}", actor=pid, verb="create_record",
                              payload={"record": rid, "kind": "dispensation",
                                       "subject_matter": {"terms": pid, "to": [pid], "at": None}}))
            assert [e.kind for e in out] == ["record.created"]
        _claim(w, pid, rid, f"{_CONTENT}:dispensation", content_value(w.records[rid].subject_matter),
               f"c_t{i}")
    checked = 0
    for pid in w.persons:
        for q in world_q.questions_for(w, w.persons[pid]):
            got = _formed(w, pid, q)
            bare = _formed(w, pid, dataclasses.replace(q, classes=()))
            assert _sig(c for c in got if c.verb not in classed_rows) == _sig(bare), (pid, q.id)
            assert not [c for c in bare if c.verb == VERB], (pid, q.id)
            checked += sum(c.verb == VERB for c in got)
    assert checked >= len(w.persons), checked


# (7) THE FALSIFIER AND THE EXIT IN COMPUTED PLAY: `build_realm(0)`, 4 SEASONS, THE REAL CHOOSER -----
#
# The 4-season run is `conftest.py::realm_4s` (one shared run; `aperture 4 0` is the plan's
# instrument, this its unit form). Formation-time conditions are (5)'s; here the observable is the
# ACT: every attempted `comply` names a dispensation its actor held, and the fold admitted it (no
# `compliance.impossible`: his own ledger held a claim on it).


def test_in09_falsifier_every_attempt_answers_a_writ_its_actor_holds_and_is_not_refused(realm_4s):
    # Batch B-I close (L4): the refusal is read from the row's THIRD element (the refusal kinds the
    # log holds for the act); `made` never carries one, so `REFUSED not in made` could not fail. The
    # hold is the LIVE one at the end of the run (a writ given away or a holder dead reads red here
    # for that reason, not for this falsifier's).
    w, _, rows, _ = realm_4s
    tried = [(a, refused) for a, _, refused in rows if a.verb == VERB]
    assert tried, "no `comply` was attempted, so the falsifier observed nothing"
    for a, refused in tried:
        rid = a.payload["subject"]
        assert any(t.kind == "hold" and t.live and t.subject == a.actor and t.object == rid
                   for t in w.tenures), (a.actor, rid, "does not hold the writ")
        assert REFUSED not in refused, (a.actor, rid, refused)


def test_in09_exit_comply_executes_in_computed_play(realm_4s):
    w, _, rows, _ = realm_4s
    done = [a for a, made, _ in rows if a.verb == VERB and GIVEN in made]
    assert done, sorted(Counter(a.verb for a, made, _ in rows if made).items())
    assert all(w.records[a.payload["subject"]].kind == "dispensation" for a in done)
