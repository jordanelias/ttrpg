"""v10 REM-21 (B10-05; rem-02 §2.3 REM-21 as repaired by `-08` AM-A-06) -- the question's own referents
stamp as their class, through ONE more term of `questions_for`'s splice and ONE dedup at the stamp site.
The file later formation items append to (REM-22 to REM-2C, and B10-06's REM-27).

The pieces, each of which can fail here: `queries/world_q.py::own_referents_of_class` (the plain
referents of the question the person answers whose `World.class_of` is in the classes it is handed),
its call as the last term of the `added` splice with `data/verbs.py::DECLARED_CLASSES` less
`rosters.yaml: occasion_only_classes` (no registry, no class literal at the stamp site), `_stamped`'s
dedup (one `(id, class)` pair per question, the first), and the three classes `rosters.yaml:
referent_classes` gains (`Site`, `Proposition`, `Person`).

  (a) the term returns exactly the question's own referents of the classes it is handed, in order;
      planted as a declared class, it stamps the answered question's own referents of that class and
      nothing the person merely knows of (no standing occasion), leaving every other field as it was.
  (b) while no row declares a class outside `occasion_only_classes` -- REM-21's table as built -- the
      questions are byte-identical to the term stubbed out, over a world whose questions DO carry
      referents of the three new classes. The realm-level equality is a reading, not a test here
      (`test_season_weather.py::BASE_HASHES`, `test_go07_canonical_digest.py::BASE` and `aperture 1 s`
      on the base commit). And the splice's term order, pinned here because the realm cannot see it
      (only `places_named` names an id there).
  (c) the dedup: the stamp site keeps one pair per question, the first; two terms emitting one Rung,
      and a question's own referent beside a standing occasion's stamp, are carried once and refused
      by nothing.
  (d) the loader still refuses an undeclared class, and takes each of the three new ones (a row
      declaring one puts it in `DECLARED_CLASSES`, the term's domain).

REM-22 (`restore`, `work` and `examine` declare `referent_class: Site`; the first positive test of the
term): the formation (a person and a Site, the verb on the Site only), the DONE tests (a person present
at a worn Site executes `restore`, reaches `examine`'s graded route, advances a works by `work`, each
through the real fold). REM-23 (`commit` declares `referent_class: Proposition`) follows the same two
tests for a person and a Proposition, and REM-24 (`petition` declares `referent_class: Person`) for a
rung and a person, with what a person's own `person`-kind rung reads as. REM-25 (`carry`, `found` and
`build` declare `Record`; the `Record` term widens from `writs_held` to `writs_held` plus
`records_held_for_holding_rows`, the Records on a person's live `hold` edges whose kind a `Record` row
asking `held_by` of `subject` asks `existence` of): the stamper, the formation (a person holding a
petition forms `carry` on it and the fold executes it; a person holding none forms none), the works rows
through the real fold, and the cost the shared class creates (measured, pinned). CP-T05-04 (`argue`
declares `Proposition`, `open_case` declares `Person`, and `world_q.docket_question` asks the witness of
a docketing about the matter docketed): the two formations and their done tests, the docket question's
asking (the claim in his own ledger, found through the act, and no stranger), the home's two
limits, and the one place the HR-9 control below does not hold (`open_case`'s class removes formations
the fold admits). REM-2C (`research` declares `Record`, and `Record` leaves `rosters.yaml:
occasion_only_classes`, so the own-referent term stamps the question's own Records): the formation (a
person and a Record, `research` on the Record only), the DONE test (a researcher holding a claim on a
Record is asked about it and reaches FI-01's graded route through the real fold), the dedup where a
standing occasion and the question both name one Record, and the second mutation (`Record` back in the
list). The last section is the batch's control (3), written over the rows
that declare `Site`, `Proposition` or `Person`, and the `Record` rows whose cell asks the actor to hold
the subject or asks `existence` of the class itself, so a later item adds its row by its column and not by
a copy.

MUTATIONS, run at the build: `_stamped`'s `dict.fromkeys` dropped (the bare concatenation) reddens the
three (c) tests on `Question`'s refusal (and `test_in53_vacancy_need.py`'s told-of-seat fingerprint
test); the term's domain widened from `DECLARED_CLASSES` to every referent class reddens (b)'s
byte-identity and (a)'s bare control; `vacancies`/`seats_named` swapped, and `places_named`/
`larders_in_purview` swapped, each redden (b)'s order test and leave the seeded realm hash
(`build_realm(0)`, one season seed 0) unmoved -- the realm reading cannot observe a reorder.
"""
import collections
import dataclasses
from unittest import mock

import pytest

from engine.season.data import verbs as _verbs
from engine.season.data.matrix import WriteClass
from engine.season.data.requires import UNKNOWN, AllOf, Existence
from engine.season.data.rosters import OCCASION_ONLY_CLASSES, PURSUITS, REFERENT_CLASSES
from engine.season.data.verbs import DECLARED_CLASSES, HOLDING_RECORD_KINDS, RECORD_REFERENT_KINDS, VERB_TABLE
from engine.season.decision import options as _options
from engine.season.decision.choose import _payload_of
from engine.season.decision.options import seat_of
from engine.season.gaps import Forbidden
from engine.season.harness import probes as P
from engine.season.loop import predicates as _preds
from engine.season.loop.driver import mint_token
from engine.season.queries import world_q
from engine.season.state.carriers import Act, Claim, Proposition, Question, Record, Tenure, View
from engine.season.trace_log import TRACE

from .test_g3_not_yours import _gov_world, _hold
from .test_h134_candidate_per_seat import _with_office
from .test_in09_dispensation_answer import HOLDER, WRIT, _with_writ
from .test_in45_carry import PARTY as CARRY_PARTY
from .test_in45_carry import PETITIONER as CARRY_PETITIONER
from .test_in45_carry import _carry, _filed
from .test_in53_vacancy_need import _ambition, _formed, _know, _planted
from .test_sc01_fired_slot import _sitting
from .test_u7_remit import DUKE, SEAT
from .test_u7_remit import PARTY as CASE_PARTY
from .test_u7_remit import _open
from .test_u7_remit import _world as _u7_world
from .test_works_founding import (
    ABSENT, HARBOUR, HEARTH, PRESENT, SETTLEMENT, _declare, _fold, _kinds, _ripen, _stock,
)
from .test_works_founding import _world as _works_world

#: The classes REM-21 adds to `rosters.yaml: referent_classes`. A test expectation, not a roster: it
#: duplicates no `values:` list (`test_jordan_no_definition_is_hardcoded_in_a_body`'s corpus rule), and
#: it stays these three when a later item releases a class from `occasion_only_classes`.
NEW_CLASSES = frozenset({"Site", "Proposition", "Person"})


def test_rem21_the_three_classes_are_declared_and_no_standing_occasion_holds_them_back():
    """The three are referent classes outside the exclusion; the exclusion names declared classes;
    and `DECLARED_CLASSES` is exactly the classes the rows declare -- no more (a derivation off the
    roster instead of the rows would stamp a class no row forms on), no fewer."""
    assert NEW_CLASSES <= REFERENT_CLASSES and not NEW_CLASSES & OCCASION_ONLY_CLASSES
    assert OCCASION_ONLY_CLASSES <= REFERENT_CLASSES
    assert DECLARED_CLASSES == {r.referent_class for r in VERB_TABLE.values() if r.referent_class}


def _proposition(w, pid, subject="S"):
    w.propositions[pid] = Proposition(pid, "OUGHT", subject, f"{pid} holds", True, 0)


# ======================================================================================
# (a) THE TERM: THE QUESTION'S OWN REFERENTS OF A DECLARED CLASS, AND NO STANDING OCCASION
# ======================================================================================

def test_rem21_a_the_term_returns_the_questions_own_referents_of_the_classes_it_is_handed():
    """A hand-built world holding one id of each kind, and a question about all of them plus an id
    the world does not hold: the term returns the referents whose collection is in `classes`, in the
    question's order. `p_mid` is also a `person`-kind rung and reads `Person`, never `Rung`."""
    w = P.tiny_world()
    _proposition(w, "prop_x")
    refs = ("site_harbour", "p_mid", "S", "off_duke", "prop_x", "nobody", "site_seam", "p_low")
    q = Question("q:claim:x", "claim_landed", refs, "x")
    own = world_q.own_referents_of_class
    assert NEW_CLASSES == {w.class_of(r) for r in ("site_harbour", "p_mid", "prop_x")}, NEW_CLASSES
    assert own(w, q, frozenset({"Site"})) == ("site_harbour", "site_seam")
    assert own(w, q, frozenset({"Person", "Proposition"})) == ("p_mid", "prop_x", "p_low")
    assert own(w, q, frozenset({"Rung"})) == ("S",)
    assert own(w, q, NEW_CLASSES) == ("site_harbour", "p_mid", "prop_x", "site_seam", "p_low")
    assert own(w, q, REFERENT_CLASSES) == tuple(r for r in refs if r != "nobody")
    assert own(w, q, frozenset()) == ()
    assert own(w, Question("q:need:y", "need", (), "y"), REFERENT_CLASSES) == ()


def test_rem21_a_a_declared_class_stamps_the_answered_questions_own_referents_and_nothing_known(
        monkeypatch):
    """`p_mid` knows the four other people and holds two ambitions, one about a Site and one about a
    person. With `Site` and `Person` planted as declared classes, the question he answers (`out[0]`)
    carries exactly its own referents of those classes, in order; the other question carries none;
    and no person he merely knows of is stamped (a person who knows fifty people forms fifty
    petitions only if the term were a standing occasion). Ids, sources and plain referents are those
    of the run with no new class declared, which stamps nothing (`p_mid` holds no seat, writ, place
    or larder)."""
    w, _ = _gov_world()
    pid = "p_mid"
    p = w.persons[pid]
    known = [o for o in w.persons if o != pid]
    _know(w, pid, *known)
    _ambition(w, pid, "prop_b", "site_harbour")
    _ambition(w, pid, "prop_a", "p_low")
    none_new = DECLARED_CLASSES & OCCASION_ONLY_CLASSES
    monkeypatch.setattr(world_q, "DECLARED_CLASSES", none_new)
    bare = world_q.questions_for(w, p)
    assert len(bare) >= 2 and all(q.classes == () for q in bare), bare
    planted = frozenset({"Site", "Person"})
    monkeypatch.setattr(world_q, "DECLARED_CLASSES", none_new | planted)
    qs = world_q.questions_for(w, p)
    assert [(q.id, q.source, q.referents, q.about) for q in qs] == [
        (q.id, q.source, q.referents, q.about) for q in bare], (qs, bare)
    head = qs[0]
    want = tuple((r, w.class_of(r)) for r in dict.fromkeys(head.referents) if w.class_of(r) in planted)
    assert want and head.classes == want, (head, want)
    assert all(q.classes == () for q in qs[1:]), qs
    stamped = {r for r, _ in head.classes}
    unasked = set(known) - set(head.referents)
    assert unasked and not unasked & stamped, (unasked, stamped)


# ======================================================================================
# (b) WHILE NO ROW DECLARES A NEW CLASS, THE QUESTIONS ARE BYTE-IDENTICAL; THE SPLICE ORDER
# ======================================================================================

def test_rem21_b_while_no_row_declares_a_new_class_the_questions_are_byte_identical(monkeypatch):
    """Every person holds an ambition about a Site, a Proposition or a person, and `off_duke2` is
    vacant (so `p_king`'s question carries a standing occasion's stamp and `_stamped` runs). With the
    declared classes held to those `occasion_only_classes` keeps back -- REM-21's table as built
    (`test_in53_vacancy_need.py::test_in53v_c_the_declarations_as_built`), so the hold is a no-op
    there -- the questions equal, field for field and in `repr`, what `questions_for` returns with
    the term stubbed to `()`."""
    monkeypatch.setattr(world_q, "DECLARED_CLASSES", DECLARED_CLASSES & OCCASION_ONLY_CLASSES)
    w, _ = _gov_world()
    _hold(w, "off_duke2").until = w.tick
    _proposition(w, "prop_x")
    subjects = ("site_harbour", "prop_x", "p_low", "site_seam", "p_mid")
    for (pid, subject) in zip(sorted(w.persons), subjects):
        _ambition(w, pid, f"prop_{pid}", subject)
    real = {pid: world_q.questions_for(w, p) for pid, p in w.persons.items()}
    exposed = sum(any(w.class_of(r) in NEW_CLASSES for r in qs[0].referents)
                  for qs in real.values() if qs)
    assert exposed >= 4, exposed
    assert any(qs and qs[0].classes for qs in real.values()), real
    monkeypatch.setattr(world_q, "own_referents_of_class", lambda *a, **k: ())
    stub = {pid: world_q.questions_for(w, p) for pid, p in w.persons.items()}
    assert real == stub and repr(real) == repr(stub)


def test_rem21_b_the_splice_stamps_in_its_term_order_and_the_own_referents_last(monkeypatch):
    """THE SPLICE ORDER, WHICH THE REALM CANNOT OBSERVE: in the seeded realm only `places_named` ever
    names an id (measured at the build, 1 and 2 seasons, seed 0), so a reordering of two terms moves no
    hash. Here every standing occasion names one id of its own and `Site` is planted as declared: the
    classes read in the splice's order -- `vacancies`, `seats_named`, `writs_held`,
    `records_held_for_holding_rows` (v10 REM-25: the second half of the `Record` term, directly after the
    writs), `places_named`, `larders_in_purview` -- and the question's own referent last. Swapping any two
    terms reddens it."""
    w, _ = _with_writ()
    w.records["rec_held"] = Record("rec_held", "Hh", "text")
    _ambition(w, HOLDER, "prop_a", "site_harbour")
    for name, out in (("vacancies", ("off_duke",)), ("seats_named", ("off_dicastery",)),
                      ("writs_held", (WRIT,)), ("records_held_for_holding_rows", ("rec_held",)),
                      ("places_named", ("D",)), ("larders_in_purview", ("S",))):
        monkeypatch.setattr(world_q, name, lambda *a, _out=out, **k: _out)
    monkeypatch.setattr(world_q, "DECLARED_CLASSES", DECLARED_CLASSES | {"Site"})
    (q,) = world_q.questions_for(w, w.persons[HOLDER])
    assert q.referents == ("site_harbour",), q
    assert q.classes == (("off_duke", "Office"), ("off_dicastery", "Office"), (WRIT, "Record"),
                         ("rec_held", "Record"), ("D", "Rung"), ("S", "Rung"), ("site_harbour", "Site")), q


# ======================================================================================
# (c) ONE PAIR PER QUESTION, THE FIRST: THE DEDUP AT THE ONE STAMP SITE
# ======================================================================================

def test_rem21_c_the_stamp_site_keeps_one_pair_per_question_the_first():
    """A question already carrying `S` as a Rung, stamped with ids that repeat it and each other:
    each pair once, at its first position, and nothing else about the question moves. The same pair
    carried twice is what `Question` refuses (the control)."""
    w, _ = _gov_world()
    q = Question("q:need:x", "need", ("S",), "x", (("S", "Rung"),))
    got = world_q._stamped(q, ("off_reeve", "S", "D", "off_reeve", "D"), w)
    assert got.classes == (("S", "Rung"), ("off_reeve", "Office"), ("D", "Rung")), got
    assert (got.id, got.source, got.referents, got.about) == (q.id, q.source, q.referents, q.about)
    with pytest.raises(Forbidden, match="twice"):
        dataclasses.replace(q, classes=q.classes + (("S", "Rung"),))


def test_rem21_c_two_terms_emitting_one_rung_stamp_one_pair_and_no_refusal(monkeypatch):
    """`places_named` and `larders_in_purview` both name `D` for one question (the rem-02 (iv-b)
    case: two terms of one class): the question carries `D` once, at the first term's position."""
    w, _ = _gov_world()
    _ambition(w, "p_mid", "prop_a", "S")
    monkeypatch.setattr(world_q, "places_named", lambda w, p, named=None: ("D",))
    monkeypatch.setattr(world_q, "larders_in_purview", lambda w, p, named=None: ("D", "S"))
    (q,) = world_q.questions_for(w, w.persons["p_mid"])
    assert q.classes == (("D", "Rung"), ("S", "Rung")), q


def test_rem21_c_an_own_referent_beside_a_standing_occasions_stamp_is_carried_once(monkeypatch):
    """`p_king`'s question is about `off_reeve`, a seat he may fill (`vacancies`). With `Office`
    released from `occasion_only_classes`, the own-referent term names it too: it is carried once, at
    the vacancy's position, so the classes are exactly the vacancies'."""
    w, _ = _gov_world()
    p = w.persons["p_king"]
    vac = world_q.vacancies(w, p)
    assert "off_reeve" in vac, vac
    _ambition(w, "p_king", "prop_a", "off_reeve")
    monkeypatch.setattr(world_q, "OCCASION_ONLY_CLASSES", OCCASION_ONLY_CLASSES - {"Office"})
    assert world_q.own_referents_of_class(w, world_q.questions_for(w, p)[0], frozenset({"Office"})) \
        == ("off_reeve",)
    (q,) = world_q.questions_for(w, p)
    assert q.referents == ("off_reeve",) and q.classes == tuple((o, "Office") for o in vac), q


# ======================================================================================
# (d) THE CLASSES ARE CLOSED: THE LOADER REFUSES AN UNDECLARED ONE AND TAKES THE THREE NEW ONES
# ======================================================================================

def test_rem21_d_the_loader_still_refuses_an_undeclared_class(monkeypatch):
    _planted(monkeypatch, "restore", "referent_class", "Sight")
    with pytest.raises(SystemExit, match="not a declared class"):
        _verbs._load_verb_table()
    with pytest.raises(Forbidden, match="no declared class"):
        Question("q:bad", "need", ("site_harbour",), "", (("site_harbour", "Sight"),))


@pytest.mark.parametrize("cls", sorted(NEW_CLASSES))
def test_rem21_d_a_row_declaring_a_new_class_loads_and_enters_the_terms_domain(monkeypatch, cls):
    """Each new class is a declared one: a row naming it loads, `DECLARED_CLASSES` (re-derived off the
    planted table) then holds it outside `occasion_only_classes` -- the term's domain -- and gains
    nothing else, and a Question may carry it."""
    assert "restore" in VERB_TABLE
    _planted(monkeypatch, "restore", "referent_class", cls)
    table = _verbs._load_verb_table()
    assert table["restore"].referent_class == cls
    monkeypatch.setattr(_verbs, "VERB_TABLE", table)
    declared = _verbs._derive_declared_classes()
    assert cls in declared - OCCASION_ONLY_CLASSES and declared - {cls} <= DECLARED_CLASSES, declared
    assert Question("q:ok", "need", (), "", (("x", cls),)).classes == (("x", cls),)


# ======================================================================================
# REM-22 (B10-05; rem-02 §2.3 REM-22, limit `-08` AM-A-07): `restore`, `work` AND `examine` FORM ON
# A SITE ONLY. The first positive test of REM-21's term: the data edit is three `referent_class: Site`
# columns, and the term is what makes them stamp.
# ======================================================================================

SITE_ROWS = ("restore", "examine", "work")
#: A question about a person, a place, a stated thing and a settlement: one referent of each kind the
#: new classes name, plus a rung (`S`), so a class's removals are visible against every other kind.
MIXED = ("p_low", "site_harbour", "prop_x", "S")
GRADED_DEGREES = frozenset({"Overwhelming", "Success", "Partial", "Failure"})


def _ask(monkeypatch, w, pid, refs=MIXED):
    """The question `pid` answers when his one ambition is about `refs`, delivered through the real
    `questions_for` (the splice, the term, `_stamped`). `goal_referents` is the one owner of what an
    ambition is about and ships no producer of a person AND a place in one question, so it is stood
    in for HERE, once, for this ambition alone; the question is otherwise the producer's."""
    prop = f"prop_ask_{pid}"
    _proposition(w, "prop_x", "S")
    _ambition(w, pid, prop, refs[0])
    real = world_q.goal_referents
    monkeypatch.setattr(world_q, "goal_referents",
                        lambda w_, p_, pr: refs if pr.id == prop else real(w_, p_, pr))
    q = world_q.questions_for(w, w.persons[pid])[0]
    assert q.id == f"q:need:{prop}" and q.referents == refs, q
    return q


def _act_of(c, p, actor=None):
    """The act the chooser mints from Candidate `c` (`decision/choose.py::pack_scenes`: `_payload_of`
    and `seat_of`), optionally in another actor's hands."""
    return Act(f"a_{c.verb}_{actor or p.id}", actor or p.id, c.verb, payload=_payload_of(c),
               via=seat_of(p, c))


def _formed_without_class(w, pid, q, verb):
    """The Candidates `verb` forms on `q` if its row declared no class: the base table's formation.
    `opening_set` reads the module's `VERB_TABLE`, so one row's copy is swapped in for the call."""
    row = VERB_TABLE[verb]
    table = {**VERB_TABLE, verb: dataclasses.replace(row, referent_class="")}
    with mock.patch.object(_options, "VERB_TABLE", table):
        return [c for c in _formed(w, pid, q) if c.verb == verb]


# --- (a) THE FORMATION: THE VERB FORMS ON THE SITE AND ON NOTHING ELSE ------------------------

@pytest.mark.parametrize("verb", SITE_ROWS)
def test_rem22_a_a_question_about_a_person_and_a_site_forms_the_verb_on_the_site_only(monkeypatch, verb):
    """THE FIRST ASSERTION, which deleting the column reddens (`test_rem22_a_mutation_...` below runs
    that deletion): `p_high` answers a question about `p_low`, the harbour, a Proposition and a rung;
    the term stamps the one Site, and `verb` forms on it and on nothing else. THE CONTROL: the person
    still forms rows that declare no class on every one of the four, so the class removed the verb's
    formations and not the person's."""
    w, _ = _works_world()
    q = _ask(monkeypatch, w, PRESENT)
    # REM-23: the question's Proposition (`prop_x`) now stamps too, as `commit` declares its class; REM-24:
    # so does its person (`p_low`, first in the question's order), as `petition` declares `Person`. The
    # Site is the same one and this verb's formation is unchanged by either.
    assert q.classes == (("p_low", "Person"), ("site_harbour", "Site"), ("prop_x", "Proposition")), q
    formed = _formed(w, PRESENT, q)
    assert [c.subject for c in formed if c.verb == verb] == ["site_harbour"], (verb, formed)
    plain = {c.subject for c in formed if not VERB_TABLE[c.verb].referent_class}
    assert set(MIXED) <= plain, plain


def test_rem22_a_every_candidate_respects_the_partition_a_classed_row_the_class_a_plain_row_the_plain(
        monkeypatch):
    """Over everything `p_high` forms from the mixed question: a row declaring a class forms only on an
    id the question carries as that class, a row declaring none only on its plain referents -- and the
    loop asserts it compared (`CLAUDE.md` §0.1 pt 2): the three Site rows, REM-23's `commit` and REM-24's
    `petition` among the classed, and the plain rows on all four referents."""
    w, _ = _works_world()
    q = _ask(monkeypatch, w, PRESENT)
    classed, plain = collections.Counter(), collections.Counter()
    for c in _formed(w, PRESENT, q):
        row = VERB_TABLE[c.verb]
        if row.referent_class:
            assert (c.subject, row.referent_class) in q.classes, (c, q.classes)
            classed[c.verb] += 1
        else:
            assert c.subject in q.referents, (c, q.referents)
            plain[c.subject] += 1
    both = SITE_ROWS + PROPOSITION_ROWS + PERSON_ROWS
    assert set(both) <= set(classed) and all(classed[v] == 1 for v in both), classed
    assert set(plain) == set(MIXED), plain


@pytest.mark.parametrize("verb", SITE_ROWS)
def test_rem22_a_mutation_without_its_column_the_row_forms_on_every_referent(monkeypatch, verb):
    """THE MUTATION, EXECUTED: the column deleted (the row copied with no class) and the assertion
    above has something to see -- the verb forms on all four referents, the person, the Proposition and
    the rung among them. The unclassed formation is the base reading's: `restore` 6/21/15 and `examine`
    29/34/22 refused at admission, on exactly such referents (`aperture 1 s`, B10-05 base)."""
    w, _ = _works_world()
    q = _ask(monkeypatch, w, PRESENT)
    assert [c.subject for c in _formed_without_class(w, PRESENT, q, verb)] == list(MIXED)
    assert [c.subject for c in _formed(w, PRESENT, q) if c.verb == verb] == ["site_harbour"]


# --- (b) THE DONE TESTS: A PERSON AT A SITE, THROUGH THE REAL FOLD (P9) -----------------------

def test_rem22_b_a_person_present_at_a_worn_site_executes_restore_through_the_fold(monkeypatch):
    """`p_high` stands at the harbour (it lies on his rung `S`) and it is worn. The Candidate his
    question forms is minted as the chooser mints it and folded by the real driver: `site.restored`,
    the fabric up. THE CONTROL, the same Candidate in the hands of `p_low`, who is not there: the
    admission refuses it on `present_at`, and the fold emits `restore.refused` and moves nothing."""
    w, d = _works_world()
    harbour = w.sites[HARBOUR]
    worn = harbour.condition
    assert worn < w.fixtures.get("condition_scale")
    q = _ask(monkeypatch, w, PRESENT)
    (c,) = [c for c in _formed(w, PRESENT, q) if c.verb == "restore"]
    ok, _kinds_, verdict = d._admits(w, _act_of(c, w.persons[PRESENT], ABSENT), VERB_TABLE["restore"])
    assert not ok and any(o.predicate.startswith("present_at") and o.value is False
                          for o in verdict.observed), verdict
    assert _kinds(_fold(w, d, _act_of(c, w.persons[PRESENT], ABSENT))) == ["restore.refused"]
    assert harbour.condition == worn
    out = _fold(w, d, _act_of(c, w.persons[PRESENT]))
    assert _kinds(out) == ["site.restored"] and harbour.condition > worn, (_kinds(out), harbour.condition)


def test_rem22_b_a_person_present_at_a_site_reaches_the_graded_route_of_examine(monkeypatch):
    """The same pair for `examine`: `p_high`'s Candidate on the harbour folds through FI-01's graded
    route -- a `finding.made` or a `finding.none` carrying a degree of the four bands, the roll having
    been thrown. THE CONTROL, `p_low` (not there): refused at admission, `finding.none` with NO degree,
    which is the refusal and not a lost roll."""
    w, d = _works_world()
    q = _ask(monkeypatch, w, PRESENT)
    (c,) = [c for c in _formed(w, PRESENT, q) if c.verb == "examine"]
    (away,) = _fold(w, d, _act_of(c, w.persons[PRESENT], ABSENT))
    assert (away.kind, away.degree) == ("finding.none", None), (away.kind, away.degree)
    (here,) = _fold(w, d, _act_of(c, w.persons[PRESENT]))
    assert here.kind in ("finding.made", "finding.none") and here.degree in GRADED_DEGREES, (
        here.kind, here.degree)


@pytest.mark.parametrize("kind", [world_q.WORKS_KIND, "text"])
def test_rem22_b_work_formed_on_a_site_advances_a_works_and_only_a_works(monkeypatch, kind):
    """ED-IN-0297 UNTOUCHED: `p_low` (the maker) forms `work` on the harbour from his question and the
    fold admits it (the cell passes: the Site is a Site). With a works planned at the harbour the
    fabric rises to its ceiling, `site.worked`; the same Candidate over a Record that is no works
    stages nothing -- `work.unavailable`, the harbour where it was."""
    w, d = _works_world()
    _declare(w, d, "rec", "harbour", SETTLEMENT, kind=kind)
    _ripen(w, d, 2)
    harbour = w.sites[HARBOUR]
    harbour.condition = 500
    q = _ask(monkeypatch, w, ABSENT)
    (c,) = [c for c in _formed(w, ABSENT, q) if c.verb == "work"]
    assert c.subject == HARBOUR and d._admits(w, _act_of(c, w.persons[ABSENT]), VERB_TABLE["work"])[0]
    out = _fold(w, d, _act_of(c, w.persons[ABSENT]))
    if kind == world_q.WORKS_KIND:
        assert _kinds(out) == ["site.worked"] and harbour.condition == 666, (_kinds(out), harbour.condition)
    else:
        assert _kinds(out) == ["work.unavailable"] and harbour.condition == 500, _kinds(out)


# ======================================================================================
# REM-23 (B10-05; rem-02 §2.3 REM-23, limit `-08` AM-A-08): `commit` FORMS ON A PROPOSITION ONLY.
# One more `referent_class:` column, the same term (`own_referents_of_class`) stamping it. THE CLASS
# REMOVES WRONG-KIND FORMATIONS ONLY: it does not answer IN-57's own-act screen (ED-IN-0296 (3), B10-09's
# CR-10) -- a person may still form `commit` on a Proposition he is already committed to.
# ======================================================================================

#: The rows declaring `Proposition`, named so that control (3) below asserts it walked each of them.
#: A later item that declares the class on a row (CP-T05-04's `argue`) is under control (3) by its column
#: whether or not it is listed here; listing it only adds the row's formation assertions to this item's.
PROPOSITION_ROWS = ("commit",)


@pytest.mark.parametrize("verb", PROPOSITION_ROWS)
def test_rem23_a_a_question_about_a_person_and_a_proposition_forms_the_verb_on_the_proposition_only(
        monkeypatch, verb):
    """THE FIRST ASSERTION, which deleting the column reddens (`test_rem23_a_mutation_...` below runs that
    deletion, and the build ran it against the YAML itself): `p_high` answers a question about `p_low`, the
    harbour, a Proposition and a rung; the term stamps the Proposition, and `commit` forms on it and on
    nothing else. THE CONTROL: the person still forms the plain rows on all four referents, so the class
    removed this verb's formations and not the person's."""
    w, _ = _works_world()
    q = _ask(monkeypatch, w, PRESENT)
    assert ("prop_x", "Proposition") in q.classes, q
    formed = _formed(w, PRESENT, q)
    assert [c.subject for c in formed if c.verb == verb] == ["prop_x"], (verb, formed)
    plain = {c.subject for c in formed if not VERB_TABLE[c.verb].referent_class}
    assert set(MIXED) <= plain, plain


@pytest.mark.parametrize("verb", PROPOSITION_ROWS)
def test_rem23_a_mutation_without_its_column_the_row_forms_on_every_referent(monkeypatch, verb):
    """THE MUTATION, EXECUTED: the column deleted (the row copied with no class) and the assertion above
    has something to see -- `commit` forms on all four referents, the person, the Site and the rung among
    them. The unclassed formation is the base reading's: `commit` attempted 38/33/34 and refused
    36/32/33 at admission on `exists:Proposition=0` (`aperture 1 s`, REM-22 tree)."""
    w, _ = _works_world()
    q = _ask(monkeypatch, w, PRESENT)
    assert [c.subject for c in _formed_without_class(w, PRESENT, q, verb)] == list(MIXED)
    assert [c.subject for c in _formed(w, PRESENT, q) if c.verb == verb] == ["prop_x"]


def test_rem23_b_a_person_committing_to_a_proposition_executes_through_the_fold(monkeypatch):
    """THE DONE TEST (P9): the Candidate `p_high`'s question forms on the Proposition is minted as the
    chooser mints it and folded by the real driver: `commitment.made`, and a live `commit` edge from him to
    it. THE CONTROL, the Candidate the unclassed row would also have formed on the person `p_low`: the
    admission refuses it (`exists:Proposition` = 0), the fold emits `commitment.refused`, and no edge
    opens. The class claims no more than that: it is the wrong-kind formation that is gone, and the
    committer's own-act screen (ED-IN-0296 (3), CR-10) is not here."""
    w, d = _works_world()
    q = _ask(monkeypatch, w, PRESENT)
    p = w.persons[PRESENT]
    (c,) = [c for c in _formed(w, PRESENT, q) if c.verb == "commit"]
    assert c.subject == "prop_x"

    def live():
        return sorted(t.object for t in p.tenures if t.kind == "commit" and t.live)

    held = live()
    assert "prop_x" not in held, held
    (wrong,) = [c for c in _formed_without_class(w, PRESENT, q, "commit") if c.subject == "p_low"]
    refused = dataclasses.replace(_act_of(wrong, p), id="a_commit_wrong_kind")
    assert _kinds(_fold(w, d, refused)) == ["commitment.refused"]
    assert live() == held, live()
    assert _kinds(_fold(w, d, _act_of(c, p))) == ["commitment.made"]
    assert live() == sorted(held + ["prop_x"]), live()


# ======================================================================================
# REM-24 (B10-05; rem-02 §2.3 REM-24, limit `-08` AM-A-09): `petition` FORMS ON A PERSON ONLY.
# One more `referent_class:` column, the same term stamping it. The counterparty `to` is the referent the
# row's cell binds (a cell that binds no `subject`), so the class binds `to`. THE CLASS REMOVES
# WRONG-KIND FORMATIONS ONLY: the cell, the eligibility and the person-side self-address decline stand.
# The home's STOPPING RULE (a fall in executions that petitions reaching a person another way do not
# explain reverts the column) is a reading of `aperture 1 s` in the commit body, never an assertion here.
# ======================================================================================

#: The rows declaring `Person`; control (3) below asserts it walked each of them.
PERSON_ROWS = ("petition",)
#: A question about a rung and a person: the pair the class tells apart.
RUNG_AND_PERSON = ("S", "p_low")


@pytest.mark.parametrize("verb", PERSON_ROWS)
def test_rem24_a_a_question_about_a_rung_and_a_person_forms_the_verb_to_the_person_only(monkeypatch, verb):
    """THE FIRST ASSERTION, which deleting the column reddens (`test_rem24_a_mutation_...` below runs that
    deletion, and the build ran it against the YAML itself): `p_high` answers a question about the
    settlement rung `S` and the person `p_low`; the term stamps the person, and `petition` forms on him
    and on nothing else, `to` bound to him. THE CONTROL: the person still forms the plain rows on both
    referents, so the class removed this verb's formations and not the person's."""
    w, _ = _works_world()
    q = _ask(monkeypatch, w, PRESENT, RUNG_AND_PERSON)
    assert q.classes == (("p_low", "Person"),), q
    formed = _formed(w, PRESENT, q)
    mine = [c for c in formed if c.verb == verb]
    assert [(c.subject, c.operands["to"]) for c in mine] == [("p_low", "p_low")], (verb, formed)
    plain = {c.subject for c in formed if not VERB_TABLE[c.verb].referent_class}
    assert set(RUNG_AND_PERSON) <= plain, plain


@pytest.mark.parametrize("verb", PERSON_ROWS)
def test_rem24_a_mutation_without_its_column_the_row_forms_on_the_rung_too(monkeypatch, verb):
    """THE MUTATION, EXECUTED: the column deleted (the row copied with no class) and the assertion above
    has something to see -- `petition` forms on the rung `S` as well as the person, the formation the
    fold refused on `exists:Person=0` (`aperture 1 s`, REM-23 tree, `petition` refused 9/13/12 of 19/17/20
    attempts, every one on that read)."""
    w, _ = _works_world()
    q = _ask(monkeypatch, w, PRESENT, RUNG_AND_PERSON)
    assert [c.subject for c in _formed_without_class(w, PRESENT, q, verb)] == list(RUNG_AND_PERSON)
    assert [c.subject for c in _formed(w, PRESENT, q) if c.verb == verb] == ["p_low"]


def test_rem24_a_a_persons_own_rung_is_a_person_and_a_settlement_is_not():
    """THE INTERACTION WITH `person`-KIND RUNGS (`rosters.yaml: referent_classes`' `Person` note): a person's
    own rung shares his id and `World.class_of` asks `persons` before `rungs`, so such a referent is a
    `Person` and never a `Rung`; a settlement is a `Rung`. The term therefore keeps a `petition` to a
    person named by his rung's id, and removes the one to a settlement."""
    w, _ = _works_world()
    assert w.rungs["p_mid"].kind == "person" and "p_mid" in w.persons and w.class_of("p_mid") == "Person"
    assert w.rungs["S"].kind == "settlement" and "S" not in w.persons and w.class_of("S") == "Rung"
    q = Question("q:claim:x", "claim_landed", ("S", "p_mid"), "x")
    assert world_q.own_referents_of_class(w, q, frozenset({"Person"})) == ("p_mid",)
    assert world_q.own_referents_of_class(w, q, frozenset({"Rung"})) == ("S",)


@pytest.mark.parametrize("referents", [RUNG_AND_PERSON, MIXED])
def test_rem24_a_the_stamp_reaches_the_delivered_question_whatever_else_it_names(monkeypatch, referents):
    """The splice, not the helper: through the real `questions_for`, the delivered question carries the
    person among its classes whether it names a rung beside him or also a Site and a Proposition, and the
    rung is not carried as anything (`Rung` is held back from the own-referent term)."""
    w, _ = _works_world()
    q = _ask(monkeypatch, w, PRESENT, referents)
    assert ("p_low", "Person") in q.classes and not any(k == "Rung" for _, k in q.classes), q


@pytest.mark.parametrize("verb", PERSON_ROWS)
def test_rem24_b_a_person_petitioning_a_person_executes_through_the_fold(monkeypatch, verb):
    """THE DONE TEST (P9): the Candidate `p_high`'s question forms on the person is minted as the chooser
    mints it and folded by the real driver: `petition.filed`, and a Record of kind `petition` addressed to
    `p_low`, held by the petitioner, who rises from `S`. THE CONTROL, the Candidate the unclassed row would
    also have formed on the rung `S`: the admission refuses it (`exists:Person` = 0), the fold emits
    `petition.refused`, and no Record is minted. The class claims no more than that: it is the
    wrong-kind formation that is gone, and what the filed petition does next is not here."""
    w, d = _works_world()
    q = _ask(monkeypatch, w, PRESENT, RUNG_AND_PERSON)
    p = w.persons[PRESENT]
    (c,) = [c for c in _formed(w, PRESENT, q) if c.verb == verb]
    assert (c.subject, c.operands["to"], c.operands["from"]) == ("p_low", "p_low", "S"), c
    (wrong,) = [c for c in _formed_without_class(w, PRESENT, q, verb) if c.subject == "S"]
    held = set(w.records)
    refused = dataclasses.replace(_act_of(wrong, p), id="a_petition_wrong_kind")
    assert _kinds(_fold(w, d, refused)) == ["petition.refused"]
    assert set(w.records) == held, set(w.records) - held
    assert _kinds(_fold(w, d, _act_of(c, p))) == ["petition.filed"]
    (rec,) = [w.records[r] for r in set(w.records) - held]
    assert rec.kind == "petition" and rec.subject_matter["to"] == ["p_low"] and rec.rung == "S", rec
    assert [t.live for t in p.tenures if t.kind == "hold" and t.object == rec.id] == [True]


# ======================================================================================
# REM-25 (B10-05; rem-02 §2.3 REM-25, limit `-08` AM-A-10): `carry`, `found` AND `build` FORM ON A
# `Record` THE PERSON HOLDS. Three `referent_class: Record` columns, and the `Record` term widened from
# `writs_held` (comply's: a dispensation naming him) to `writs_held` plus `records_held_for_holding_rows`
# (the Records on his live `hold` edges whose kind a `Record` row asking `held_by` of `subject` asks
# `existence` of, `data/verbs.py::HOLDING_RECORD_KINDS`, derived off the cells with no verb name).
# THE CLASS REMOVES WRONG-COLLECTION FORMATIONS AND IS SHARED: one class cannot tell a petition from a
# works, so the three rows form on every held Record of either kind and the fold disposes (pinned below).
# DECLARED SIDEWAYS MOVE: `found` and `build` leave always-refused for (nearly) never-attempted, because
# no computed act declares a works until ED-IN-0297 is answered; the readings are `aperture 1 s`'s, in
# the commit body, never an assertion here.
# ======================================================================================

#: The rows declaring `Record` whose cell asks the actor to hold the subject; control (3) below walks them.
HOLDING_ROWS = ("carry", "found", "build")
#: The rows declaring `Record` on a writ (REM-2B restored the two beside `comply`): no `held_by`, `writs_held`'s occasion.
WRIT_ROWS = ("comply", "evade / defy", "construe")
PETITION_ID = "pet_rem25"
#: The rows' independent statement of the data the derivation reads, spelt without `data/verbs.py`.
HOLDING_KINDS = frozenset({"petition", "works"})


def _file_petition(w, d, pid=PRESENT, key=PETITION_ID):
    """`pid` files a petition about `p_low` to him through the real `petition` fold: a Record of kind
    `petition` minted into the petitioner's hand (`_mint_document`'s maker's `hold`), who is not its
    addressee."""
    out = _fold(w, d, Act(id=f"file_{key}", actor=pid, verb="petition",
                          payload={"record": key, "subject": "p_low", "to": "p_low", "from": "S"}))
    assert _kinds(out) == ["petition.filed"], _kinds(out)
    assert w.records[key].kind == "petition" and world_q.hold_force(w, key).subject == pid
    return key


def test_rem25_the_two_record_terms_are_told_apart_by_the_cell_and_derived_from_it():
    """The `Record` rows split by whether their cell asks `held_by` of `subject`: the writ row's kinds are
    `RECORD_REFERENT_KINDS` (stamped with the addressee test), the holding rows' are `HOLDING_RECORD_KINDS`
    (stamped by the holding alone); the two sets are disjoint and each is exactly the `existence` kinds of
    its rows' cells. THE ANTI-VACUITY: both sets are non-empty and the holding rows are the three columns.

    RE-RECORDED AT v10 REM-2C (B10-05; control: the CP-T05-04 tree `ea6f1dba`, where `research` declared no
    class): the rows asking no `held_by` were `{comply}` and are `{comply, research}`, and their `existence`
    kinds were `{dispensation}` and are `{dispensation, Record}`. WHAT THIS TEST MEANT -- `writs_held`
    stamps the dispensation alone -- holds unchanged, and is asserted on the SUB-kinds: `research` asks
    `existence` of the collection itself (`kind: Record`, any document), which `_record_subkinds_answered`
    keeps out of both sets, so neither set moved (`RECORD_REFERENT_KINDS` {dispensation},
    `HOLDING_RECORD_KINDS` {petition, works}, the same on both trees).

    RE-RECORDED AT v10 REM-2B (B10-06; control: the REM-2A tree `f23194871`, where the two rows were untyped):
    `evade / defy` and `construe` declare `Record` on `comply`'s cell (no `held_by`), so the rows asking no
    `held_by` were `{comply, research}` and are `{comply, evade / defy, construe, research}`; their `existence`
    kinds are still `{dispensation, Record}`, and neither set moved. `construe` asks no `held_by` ON PURPOSE:
    the checkpoint's third conjunct would move `dispensation` into `HOLDING_RECORD_KINDS` (`holding` would gain
    `construe` and the two sets stop being disjoint), which this test reddens, and its formation consequence is
    `test_in09_dispensation_answer.py::test_in09_a_custodian_who_is_not_the_addressee_is_offered_none_of_the_three`."""
    rows = {v: r for v, r in VERB_TABLE.items() if r.referent_class == "Record"}
    holding = {v for v, r in rows.items() if _verbs._asks_subject_held(r)}
    assert holding == set(HOLDING_ROWS) and set(rows) - holding == set(WRIT_ROWS) | set(COLLECTION_ROWS), (
        sorted(rows), sorted(holding))
    kinds = lambda vs: frozenset().union(*(_existence_kinds(rows[v].requires_typed.requirement) for v in vs))
    assert kinds(COLLECTION_ROWS) == {"Record"}
    assert HOLDING_RECORD_KINDS == kinds(holding) == HOLDING_KINDS
    assert RECORD_REFERENT_KINDS == kinds(set(rows) - holding) - {"Record"} == {"dispensation"}
    assert not HOLDING_RECORD_KINDS & RECORD_REFERENT_KINDS


def test_rem25_a_the_stamper_returns_the_live_holds_of_a_holding_kind_and_nothing_else():
    """`records_held_for_holding_rows`: the Records on the person's own live `hold` edges of a holding kind,
    sorted. NOT the addressee test (the petitioner holds his petition and is not its addressee: `writs_held`
    stamps him nothing), NOT a text, NOT a hold that has ended, NOT the person the petition names (he holds
    nothing). The anti-vacuity: the first call returns the petition."""
    w, d = _works_world()
    pet = _file_petition(w, d)
    w.records["txt_rem25"] = Record("txt_rem25", "S", "text")
    w.add_tenure(Tenure("hold:txt_rem25", PRESENT, "txt_rem25", "hold", since=w.tick))
    p = w.persons[PRESENT]
    assert world_q.records_held_for_holding_rows(w, p) == (pet,)
    assert world_q.writs_held(w, p) == (), "a petition is no writ: the addressee test stamps it nothing"
    assert world_q.records_held_for_holding_rows(w, w.persons["p_low"]) == ()
    world_q.hold_force(w, pet).until = w.tick
    assert world_q.records_held_for_holding_rows(w, p) == ()


def test_rem25_a_a_writ_is_stamped_by_its_own_term_and_not_by_the_holding_term():
    """The other half of the split: a held dispensation naming its holder is `writs_held`'s and the holding
    term returns nothing for it (a dispensation is no holding row's kind), so `comply`'s addressee test is
    unchanged. The anti-vacuity: `writs_held` stamps the writ."""
    w, _ = _with_writ()
    p = w.persons[HOLDER]
    assert world_q.writs_held(w, p) == (WRIT,)
    assert world_q.records_held_for_holding_rows(w, p) == ()


@pytest.mark.parametrize("verb", HOLDING_ROWS)
def test_rem25_a_a_person_holding_a_petition_forms_the_verb_on_it_and_one_holding_none_forms_none(
        monkeypatch, verb):
    """THE FIRST ASSERTION, which dropping the `held_by` derivation reddens (the build ran that mutation
    against `_derive_holding_record_kinds` itself): `p_high` files a petition and answers a question about
    `p_low`, the harbour, a Proposition and a rung; the holding term stamps the petition as a `Record`, and
    `verb` forms on it and on nothing else. THE CONTROL: he still forms the plain rows on all four referents
    (the class removed this verb's formations and not his), and `p_low`, who holds nothing, is stamped no
    Record and forms none of the three."""
    w, d = _works_world()
    pet = _file_petition(w, d)
    q = _ask(monkeypatch, w, PRESENT)
    assert (pet, "Record") in q.classes, q
    formed = _formed(w, PRESENT, q)
    assert [c.subject for c in formed if c.verb == verb] == [pet], (verb, formed)
    plain = {c.subject for c in formed if not VERB_TABLE[c.verb].referent_class}
    assert set(MIXED) <= plain, plain
    none = _ask(monkeypatch, w, ABSENT)
    assert not [r for r, k in none.classes if k == "Record"], none
    assert not [c for c in _formed(w, ABSENT, none) if c.verb in HOLDING_ROWS]


@pytest.mark.parametrize("verb", HOLDING_ROWS)
def test_rem25_a_mutation_without_its_column_the_row_forms_on_every_referent_and_never_on_the_record(
        monkeypatch, verb):
    """THE MUTATION, EXECUTED: the column deleted (the row copied with no class) and the assertion above
    has something to see -- `verb` forms on all four plain referents, the person, the Site and the rung among
    them, and NEVER on the petition (a classless row reads the plain referents only). The unclassed
    formation is the base reading's: `carry` 15/18/12, `found` 11/14/21 and `build` 12/13/12 attempted and
    refused at admission (`aperture 1 s`, REM-24 tree)."""
    w, d = _works_world()
    pet = _file_petition(w, d)
    q = _ask(monkeypatch, w, PRESENT)
    assert [c.subject for c in _formed_without_class(w, PRESENT, q, verb)] == list(MIXED)
    assert [c.subject for c in _formed(w, PRESENT, q) if c.verb == verb] == [pet]


def test_rem25_a_dropping_the_holding_derivation_stamps_nothing(monkeypatch):
    """THE DERIVATION MUTATION, IN-PROCESS: with `HOLDING_RECORD_KINDS` empty (what dropping the `held_by`
    derivation yields) the petition is stamped nothing, and no holding row forms for its holder -- the
    first assertion of the formation test above would red. The CONTROL is that test: same world, shipped set."""
    w, d = _works_world()
    pet = _file_petition(w, d)
    monkeypatch.setattr(world_q, "HOLDING_RECORD_KINDS", frozenset())
    q = _ask(monkeypatch, w, PRESENT)
    assert (pet, "Record") not in q.classes and not [r for r, k in q.classes if k == "Record"], q
    assert not [c for c in _formed(w, PRESENT, q) if c.verb in HOLDING_ROWS]


def test_rem25_b_a_person_carrying_his_held_petition_executes_through_the_fold(monkeypatch):
    """THE DONE TEST (P9): the Candidate `p_high`'s question forms on his petition is minted as the chooser
    mints it and folded by the real driver: `petition.carried`, and a docket item naming the petition.
    THE CONTROLS, each one clause from the executing carry: the Candidate the unclassed row would also have
    formed on the person `p_low` (the admission refuses it, `exists:petition` = 0), and the executing
    Candidate in the hands of `p_low`, who does not hold the petition (`held_by`); each is `carry.refused`
    and moves the docket nowhere. The class claims no more than that: it is the wrong-kind formation that is
    gone."""
    w, d = _works_world()
    pet = _file_petition(w, d)
    q = _ask(monkeypatch, w, PRESENT)
    p = w.persons[PRESENT]
    (c,) = [c for c in _formed(w, PRESENT, q) if c.verb == "carry"]
    assert c.subject == pet
    before = list(w.docket)
    (wrong,) = [c for c in _formed_without_class(w, PRESENT, q, "carry") if c.subject == "p_low"]
    refused = dataclasses.replace(_act_of(wrong, p), id="a_carry_wrong_kind")
    assert _kinds(_fold(w, d, refused)) == ["carry.refused"] and w.docket == before
    not_held = dataclasses.replace(_act_of(c, p, ABSENT), id="a_carry_not_held")
    assert _kinds(_fold(w, d, not_held)) == ["carry.refused"] and w.docket == before
    assert _kinds(_fold(w, d, _act_of(c, p))) == ["petition.carried"]
    (item,) = [i for i in w.docket if i not in before]
    assert item[world_q.DOCKET_PETITION] == pet, item


@pytest.mark.parametrize("verb, plan, at, done, stocked", [
    ("found", "hearth", SETTLEMENT, "rung.founded", None),
    ("build", "harbour", HEARTH, "site.built", HEARTH),
])
def test_rem25_b_a_maker_holding_a_works_executes_found_and_build_through_the_fold(
        monkeypatch, verb, plan, at, done, stocked):
    """THE DONE TEST for the works rows (P9), on a hand-built world only: no computed act declares a works
    (ED-IN-0297), so the realm never reaches this. The maker `p_low` declares a works through the real
    `create_record`, holds it, is asked a question, and the holding term stamps it; `verb` forms on it and
    the real fold executes it (`rung.founded`: a hearth at `S`; `site.built`: a harbour at `Hh`). THE
    CONTROL: the same body with the Record declared `text` -- the term stamps it nothing and the row forms
    nothing; and a `p_mid` who holds no works forms none."""
    w, d = _works_world()
    _declare(w, d, "wk", plan, at)
    if stocked:                             # the plan's timber (v9 IN-28); `S` stocks the hearth's stake
        _stock(w, stocked, plan)
    q = _ask(monkeypatch, w, ABSENT)
    assert ("wk", "Record") in q.classes, q
    (c,) = [c for c in _formed(w, ABSENT, q) if c.verb == verb]
    assert c.subject == "wk"
    assert _kinds(_fold(w, d, _act_of(c, w.persons[ABSENT]))) == [done]
    wt, dt = _works_world()
    _declare(wt, dt, "wk", plan, at, kind="text")
    qt = _ask(monkeypatch, wt, ABSENT)
    assert not [r for r, k in qt.classes if k == "Record"], qt
    assert not [c for c in _formed(wt, ABSENT, qt) if c.verb in HOLDING_ROWS]


def test_rem25_c_the_class_is_shared_so_the_rows_form_on_each_others_records_and_the_fold_refuses(
        monkeypatch):
    """THE COST THE CLASS SHARING CREATES, MEASURED AND PINNED (the H-163 precedent; rem-02 REM-25): one
    `Record` class cannot tell a petition from a works from a writ. (1) A held PETITION is a `Record` for
    `found` and `build` too, and each, force-admitted, is refused on `exists:works` = 0 (the carry on it is
    admitted); (2) a `comply` formed on it (once his ledger names it) is refused on `exists:dispensation`;
    (3) a held WRIT is a `Record` for `carry`, refused on `exists:petition` = 0. Each is a wrong-SUB-kind
    refusal where the base had wrong-COLLECTION ones: a Record is the right collection."""
    w, d = _works_world()
    pet = _file_petition(w, d)
    q = _ask(monkeypatch, w, PRESENT)
    p = w.persons[PRESENT]
    # AFTER the question is delivered (a claim in his ledger would raise a question of its own that sorts
    # first): his own ledger now names the petition, which is what lets `comply` (`referent_named`) form.
    p.ledger.append(Claim("c_names_pet", PRESENT, pet, "record.created", True, w.tick, "firsthand", 100, "own"))
    formed = {c.verb: c for c in _formed(w, PRESENT, q) if c.subject == pet}
    assert {"carry", "found", "build", "comply"} <= set(formed), sorted(formed)

    def refusals(world, driver, person, cand, verb):
        ok, _k, verdict = driver._admits(world, _act_of(cand, person), VERB_TABLE[verb])
        return ok, [o.predicate for o in verdict.observed if o.value in (0, False)]

    assert refusals(w, d, p, formed["carry"], "carry")[0]
    for verb, wanted in (("found", "exists:works"), ("build", "exists:works"), ("comply", "exists:dispensation")):
        ok, reads = refusals(w, d, p, formed[verb], verb)
        assert not ok and wanted in reads, (verb, reads)
    ww, wd = _with_writ()
    holder = ww.persons[HOLDER]
    writ_q = world_q.questions_for(ww, holder)[0]
    (carry_on_writ,) = [c for c in _formed(ww, HOLDER, writ_q) if c.verb == "carry"]
    assert carry_on_writ.subject == WRIT
    ok, reads = refusals(ww, wd, holder, carry_on_writ, "carry")
    assert not ok and "exists:petition" in reads, reads


# ======================================================================================
# CP-T05-04 (B10-05; home T05 §2 CP-T05-04, limits `-08` AM-D-05): THE PROCEEDINGS VERBS' FORMATION.
# TWO COLUMNS -- `argue` declares `Proposition` (the arguer's own uttered Propositions reach his question
# through the maker's hold), `open_case` declares `Person` -- AND ONE QUESTION, `world_q.docket_question`,
# the sitting question's sibling: the docketed matters whose docketing Event his OWN ledger holds a claim
# of, as PLAIN referents of a `claim_landed` question. `speak` and `determine` get NO class (a class is
# the referent's own type), so both keep forming on plain referents and the sitting route stays. The
# readings (formed, attempted, executed per verb; the unclassed rows that newly form on a docketed
# person) are `aperture 1 s`'s, in the commit body, never an assertion here.
# ======================================================================================

#: The rows CP-T05-04 gives a class; control (3) below walks them by their column, these add each row's
#: own formation assertions (`argue` forms one Candidate per hearer it knows, so it is not `PROPOSITION_ROWS`').
ARGUE_ROWS = ("argue",)
OPEN_CASE_ROWS = ("open_case",)
PROCEEDINGS_ROWS = ARGUE_ROWS + OPEN_CASE_ROWS
HEARER = "p_hearer"
#: The Event kinds that put a matter before a room, spelt without `world_q.DOCKETING_KINDS`.
DOCKETING_EVENT_KINDS = frozenset({"case.opened", "petition.carried"})


def _hearer_world():
    """`_works_world` with a hearer at the arguer's place (`argue`'s `with` conjunct) whom the arguer KNOWS
    exists (`known_persons`, the fan `argue`'s `to` ranges over). The claim is dated before the landing
    floor so it raises no question of its own and `_ask`'s question stays the first."""
    w, d = _works_world()
    P.plant_cohort(w, HEARER, SETTLEMENT)
    w.persons[PRESENT].ledger.append(Claim(f"c_knows_{HEARER}", PRESENT, HEARER, "exists:Person", 1, -2,
                                           "firsthand", 100, "own"))
    return w, d


def test_cp_t05_04_the_docketing_kinds_are_derived_off_the_rows_that_write_the_docket_item():
    """`DOCKETING_KINDS` is the success kinds of the rows writing a docket item's `petition` key, and it is
    exactly the two the home names -- not `determine`'s, which clears a matter and writes `DocketItem.matter`
    alone. THE ANTI-VACUITY: the two writers are `open_case` and `carry` and the set is not empty."""
    writers = {v for v, r in VERB_TABLE.items() if "DocketItem.petition" in r.writes}
    assert writers == {"open_case", "carry"}, writers
    assert world_q.DOCKETING_KINDS == DOCKETING_EVENT_KINDS
    assert "DocketItem.matter" in VERB_TABLE["determine"].writes and "determine" not in writers


# --- (a) THE FORMATION: argue FORMS ON THE PROPOSITION, open_case ON THE PERSON ---------------

def test_cp_t05_04_a_a_question_about_a_person_and_a_proposition_forms_argue_on_the_proposition_only(
        monkeypatch):
    """THE FIRST ASSERTION, which deleting the column reddens (`test_cp_t05_04_a_mutation_...` below runs
    that deletion, and the build ran it against the YAML itself): `p_high` knows a hearer and answers a
    question about `p_low`, the harbour, a Proposition and a rung; the term stamps the Proposition, and
    `argue` forms on it, to the hearer, and on nothing else. THE CONTROL: the person still forms the plain
    rows on all four referents, so the class removed this verb's formations and not the person's."""
    w, _ = _hearer_world()
    q = _ask(monkeypatch, w, PRESENT)
    assert ("prop_x", "Proposition") in q.classes, q
    formed = _formed(w, PRESENT, q)
    assert [(c.subject, c.operands["to"]) for c in formed if c.verb == "argue"] == [("prop_x", HEARER)], formed
    plain = {c.subject for c in formed if not VERB_TABLE[c.verb].referent_class}
    assert set(MIXED) <= plain, plain


def test_cp_t05_04_a_a_question_about_a_rung_and_a_person_forms_open_case_on_the_person_only(monkeypatch):
    """THE FIRST ASSERTION for the second column: `p_high`, who sits the Duke's seat (`remit:determine`),
    answers a question about the settlement rung `S` and the person `p_low`; the term stamps the person, and
    `open_case` forms on him and on nothing else. THE CONTROL: the plain rows still form on both."""
    w, _ = _works_world()
    q = _ask(monkeypatch, w, PRESENT, RUNG_AND_PERSON)
    assert q.classes == (("p_low", "Person"),), q
    formed = _formed(w, PRESENT, q)
    assert [c.subject for c in formed if c.verb == "open_case"] == ["p_low"], formed
    plain = {c.subject for c in formed if not VERB_TABLE[c.verb].referent_class}
    assert set(RUNG_AND_PERSON) <= plain, plain


def test_cp_t05_04_a_mutation_without_its_column_the_row_forms_on_every_referent(monkeypatch):
    """THE MUTATION, EXECUTED for both columns (the row copied with no class): `argue` forms on all four
    referents, the person, the Site and the rung among them -- the unclassed formation `aperture 1 s` read
    refused 8/10/5 on `exists:Proposition=0` -- and `open_case` forms on the rung as well as the person."""
    w, _ = _hearer_world()
    q = _ask(monkeypatch, w, PRESENT)
    assert [c.subject for c in _formed_without_class(w, PRESENT, q, "argue")] == list(MIXED)
    assert [c.subject for c in _formed(w, PRESENT, q) if c.verb == "argue"] == ["prop_x"]
    w, _ = _works_world()
    q = _ask(monkeypatch, w, PRESENT, RUNG_AND_PERSON)
    assert [c.subject for c in _formed_without_class(w, PRESENT, q, "open_case")] == list(RUNG_AND_PERSON)
    assert [c.subject for c in _formed(w, PRESENT, q) if c.verb == "open_case"] == ["p_low"]


# --- (b) THE DONE TESTS (P9): THE FORMED CANDIDATE RUNS THROUGH THE REAL FOLD -------------------

def test_cp_t05_04_b_a_person_arguing_a_proposition_to_a_hearer_executes_through_the_fold(monkeypatch):
    """The Candidate `p_high`'s question forms on the Proposition is minted as the chooser mints it and
    folded by the real driver: a contested `argue` whose band is the seed's, and in every band a kind the
    row emits for a lawful argument (`argument.won`, `argument.lost`) -- never `argument.refused`. The
    two hold different pursuits so a won argument has something to move (a won argument that moves nothing
    is refused at its write). THE CONTROL, the Candidate the unclassed row would also have formed on the
    person `p_low`: the admission refuses it (`exists:Proposition` = 0) and the fold emits
    `argument.refused`. The class claims no more than that: it is the wrong-kind formation that is gone, and
    whether an arguer's question ever carries a Proposition in a season is `aperture`'s reading."""
    w, d = _hearer_world()
    a, b = sorted(PURSUITS)[:2]
    w.persons[PRESENT].pursuits = {a: 0.9, b: 0.1}
    w.persons[HEARER].pursuits = {a: 0.1, b: 0.9}
    q = _ask(monkeypatch, w, PRESENT)
    p = w.persons[PRESENT]
    (c,) = [c for c in _formed(w, PRESENT, q) if c.verb == "argue"]
    assert (c.subject, c.operands["to"]) == ("prop_x", HEARER)
    wrong = [c for c in _formed_without_class(w, PRESENT, q, "argue") if c.subject == "p_low"]
    assert [x.operands["to"] for x in wrong] == [HEARER]
    refused = dataclasses.replace(_act_of(wrong[0], p), id="a_argue_wrong_kind")
    assert _kinds(_fold(w, d, refused)) == ["argument.refused"]
    assert _kinds(_fold(w, d, _act_of(c, p)))[0] in ("argument.won", "argument.lost")


def test_cp_t05_04_b_a_seat_opening_a_case_on_a_person_executes_and_the_rung_it_no_longer_forms_on_would_too(
        monkeypatch):
    """`p_high`'s Candidate on the person is minted as the chooser mints it (the seat riding as `Act.via`)
    and folded: `case.opened`, and the person is on the docket. THE CONTROL IS THE CLOSED ROUTE, kept
    evaluated with the class blanked in-process (`_formed_without_class`): the Candidate the unclassed row
    also formed on the settlement rung `S` is ADMITTED by the same fold -- `open_case` is a remit verb
    whose cell asks the seat's purview over the matter's place, not its kind -- and docketing a rung is a
    case `determine` can never take off (its `party` conjunct needs a person: `determine.refused`). That is
    what the class removes (the home, D:#75), and it is an EXECUTING formation, not a refusal: the shipped
    row no longer forms it, and a hand-built act still may."""
    w, d = _works_world()
    q = _ask(monkeypatch, w, PRESENT, RUNG_AND_PERSON)
    p = w.persons[PRESENT]
    (c,) = [c for c in _formed(w, PRESENT, q) if c.verb == "open_case"]
    (rung,) = [c for c in _formed_without_class(w, PRESENT, q, "open_case") if c.subject == "S"]
    assert world_q.docketed(w, "p_low") == [] and world_q.docketed(w, "S") == []
    assert _kinds(_fold(w, d, _act_of(c, p))) == ["case.opened"]
    assert [i["matter"] for i in world_q.docketed(w, "p_low")] == ["p_low"]
    assert _kinds(_fold(w, d, dataclasses.replace(_act_of(rung, p), id="a_open_case_rung"))) == ["case.opened"]
    assert [i["matter"] for i in world_q.docketed(w, "S")] == ["S"]
    undeterminable = Act("a_determine_rung", PRESENT, "determine", payload={"subject": "S"}, via=SEAT)
    assert _kinds(_fold(w, d, undeterminable)) == ["determine.refused"]
    assert [i["matter"] for i in world_q.docketed(w, "S")] == ["S"], "the rung stays docketed for ever"


# --- (c) THE DOCKET QUESTION: THE WITNESS OF A DOCKETING IS ASKED ABOUT THE MATTER ---------------

def _docketed_case():
    """The Duke (`p_high`) opens a case on `p_mid` through the real fold and the season's WITNESS deposits
    it: a dateless docket item, and the claims of `case.opened` in the ledgers of whoever stood at `S`."""
    w, d = _u7_world()
    out = _fold(w, d, _open("oc"))
    assert [e.kind for e in out] == ["case.opened"]
    d.witness(mint_token(w, WriteClass.INTERIOR), out)
    (item,) = w.docket
    assert item["date"] is None and item["matter"] == CASE_PARTY
    return w, d


def test_cp_t05_04_c_a_person_holding_case_opened_of_a_dateless_matter_is_asked_and_forms_speak_on_it():
    """THE HOME'S FALSIFIER: the opener holds `case.opened` of a dateless docketed matter, so the docket
    question names it (one question, plain referents, the `claim_landed` source, `about` a claim he holds
    of the Event), it is among the questions `questions_for` returns, and `speak` forms on the matter from
    it. THE CONTROLS: nobody who holds no such claim is asked (the copyist, the clerk and the stranger live
    below the Duke's seat and saw nothing; the King stands outside it), and before the case is opened no
    one is asked."""
    w, d = _u7_world()
    assert all(world_q.docket_question(w, p) is None for p in w.persons.values())
    out = _fold(w, d, _open("oc"))
    d.witness(mint_token(w, WriteClass.INTERIOR), out)
    duke = w.persons[DUKE]
    dq = world_q.docket_question(w, duke)
    assert (dq.id, dq.source, dq.referents, dq.classes) == (f"q:docket:{CASE_PARTY}", "claim_landed",
                                                            (CASE_PARTY,), ())
    assert dq.about in {c.id for c in duke.ledger if c.predicate == "case.opened"}
    assert dq in world_q.questions_for(w, duke)
    assert [c.subject for c in _formed(w, DUKE, dq) if c.verb == "speak"] == [CASE_PARTY]
    for pid in sorted(set(w.persons) - {DUKE}):
        assert world_q.docket_question(w, w.persons[pid]) is None, pid
        assert not [q for q in world_q.questions_for(w, w.persons[pid]) if q.id.startswith("q:docket:")], pid


def test_cp_t05_04_c_the_claim_is_of_the_event_and_names_the_actor_and_the_file_never_the_matter():
    """WHY THE LINK IS THE ACT AND NOT THE CLAIM'S SUBJECT (the ledger test `sittings_before` makes reads a
    firing's own subject, a venue): no claim a `case.opened` leaves names the matter -- they name its actor
    and the case file -- so the docket question finds the matter through the act the Event's cause is
    (`docketed_by`). Mutation: asking the claim's subject finds nothing, and the person is asked no more."""
    w, _ = _docketed_case()
    duke = w.persons[DUKE]
    held = [c for c in duke.ledger if c.predicate == "case.opened"]
    assert held and CASE_PARTY not in {c.subject for c in held}, [(c.subject, c.predicate) for c in held]
    assert {c.subject for c in held} == {DUKE, "rec:oc"}
    assert all(world_q.docketed_by(w, c) == (CASE_PARTY,) for c in held)
    other = [c for c in duke.ledger if c.predicate != "case.opened"]
    assert other and all(world_q.docketed_by(w, c) == () for c in other)


def test_cp_t05_04_c_a_matter_taken_off_the_docket_or_never_witnessed_is_not_asked():
    """CONTROLS, each one clause from the asked question: a matter a determination has cleared (written back
    to `None`, the slot kept) names nothing and the Duke is asked no more; and a second case docketed but
    never witnessed (no deposit) does not widen his question -- his claims are of the first Event only."""
    w, d = _docketed_case()
    duke = w.persons[DUKE]
    assert [_fold(w, d, _open("oc2", subject="p_low"))[0].kind] == ["case.opened"]
    assert [i["matter"] for i in w.docket] == [CASE_PARTY, "p_low"]
    assert world_q.docket_question(w, duke).referents == (CASE_PARTY,)
    w.docket[0]["matter"] = None
    assert world_q.docket_question(w, duke) is None


def test_cp_t05_04_c_the_carry_route_asks_the_petitioner_about_the_matter_the_petition_names():
    """`petition.carried` is the other docketing Event: the carried petition's terms are docketed, the item
    names the petition, and the witnesses of the carriage -- the petitioner and whoever stood with him at
    `Hh` -- are asked about the matter, found through the act's subject (the petition) and the item's
    `petition` key. THE CONTROLS: the King stands at the realm and saw nothing; and before the carriage
    (the petition filed and held, nothing docketed) no one is asked."""
    w, d = _filed()
    assert all(world_q.docket_question(w, p) is None for p in w.persons.values())
    out = _fold(w, d, _carry("c1"))
    assert [e.kind for e in out] == ["petition.carried"]
    d.witness(mint_token(w, WriteClass.INTERIOR), out)
    low = w.persons[CARRY_PETITIONER]
    dq = world_q.docket_question(w, low)
    assert (dq.id, dq.referents) == (f"q:docket:{CARRY_PARTY}", (CARRY_PARTY,))
    assert next(c.predicate for c in low.ledger if c.id == dq.about) == "petition.carried"
    assert world_q.docket_question(w, w.persons["p_other"]).referents == (CARRY_PARTY,)
    assert world_q.docket_question(w, w.persons["p_king"]) is None


def test_cp_t05_04_c_a_judge_holding_date_fired_and_no_docketing_claim_still_forms_determine_from_the_sitting():
    """THE HOME'S LAST FALSIFIER, and why `determine` gets no class: the sitting route is untouched. A
    sitting fires at `S`, a case is opened on `p_mid` for its slot, and the Duke -- on the bench, holding
    the firing's `date.fired` claim -- has his `case.opened` claims taken out of his ledger. He is asked by
    the sitting question and by no docket question, and `determine` forms on the matter from it. THE
    CONTROL: with his docketing claims back he is asked by both, and `determine` forms from either."""
    w, d = _u7_world(pool_default=30)
    duke = w.persons[DUKE]
    did = _sitting(w, d)
    out = _fold(w, d, _open("oc"))
    d.witness(mint_token(w, WriteClass.INTERIOR), out)
    sitting = f"q:sitting:{did}:{CASE_PARTY}"
    kept = list(duke.ledger)
    duke.ledger[:] = [c for c in kept if c.predicate not in DOCKETING_EVENT_KINDS]
    ids = [q.id for q in world_q.questions_for(w, duke)]
    assert sitting in ids and not [i for i in ids if i.startswith("q:docket:")], ids
    (sq,) = [q for q in world_q.questions_for(w, duke) if q.id == sitting]
    assert [c.subject for c in _formed(w, DUKE, sq) if c.verb == "determine"] == [CASE_PARTY]
    duke.ledger[:] = kept
    qs = {q.id: q for q in world_q.questions_for(w, duke)}
    assert sitting in qs and f"q:docket:{CASE_PARTY}" in qs
    assert all([c.subject for c in _formed(w, DUKE, q) if c.verb == "determine"] == [CASE_PARTY]
               for q in (qs[sitting], qs[f"q:docket:{CASE_PARTY}"]))


# --- (d) THE TWO LIMITS OF `-08` AM-D-05, AS THEY STAND ON A HAND-BUILT WORLD ---------------------

def test_cp_t05_04_d_limit_1_the_docket_question_is_delivered_only_where_it_sorts_first():
    """LIMIT (1): `question_aggregation_rule` is `first` (`data/fixtures.py`), so a person answers `out[0]`
    alone and the docket question reaches him only when it sorts first by `attention_key`. The Duke has
    just witnessed the opening, so the claims it landed raise questions of their own that sort ahead and
    the docket question is asked but not delivered; a season later those claims are no longer new, nothing
    sorts ahead of the standing question, and it is delivered. So the formed `speak`/`determine` counts at
    the exit are a lower bound, and the reading is the formed counts, not the question's existence."""
    w, _ = _docketed_case()
    duke = w.persons[DUKE]
    assert w.fixtures.get("question_aggregation_rule") == "first"
    ids = [q.id for q in world_q.questions_for(w, duke)]
    assert f"q:docket:{CASE_PARTY}" in ids and ids[0] != f"q:docket:{CASE_PARTY}", ids
    w.tick += 3
    ids = [q.id for q in world_q.questions_for(w, duke)]
    assert f"q:docket:{CASE_PARTY}" in ids and ids[0] == f"q:docket:{CASE_PARTY}", ids


def test_cp_t05_04_d_limit_2_a_docketed_person_is_a_plain_referent_of_every_unclassed_row():
    """LIMIT (2): the docket question carries the docketed person as a PLAIN referent, so every row with no
    `referent_class` forms on him; a classed row forms only on what the splice stamps for the question
    (`petition` and `open_case` on the person, `Person`), never on the plain referent as such. The exit
    lists the unclassed rows that newly form (`aperture`'s reading); here the property, on the question as
    the person is delivered it (a season on, when it sorts first): every unclassed row's subjects are the
    docketed person, and every classed row's are inside what the question carries as that class."""
    w, _ = _docketed_case()
    w.tick += 3
    duke = w.persons[DUKE]
    q = world_q.questions_for(w, duke)[0]
    assert q.id == f"q:docket:{CASE_PARTY}" and q.referents == (CASE_PARTY,), q
    assert (CASE_PARTY, "Person") in q.classes, q
    formed = _formed(w, DUKE, q)
    plain = {c.verb for c in formed if not VERB_TABLE[c.verb].referent_class}
    assert {"speak", "determine"} <= plain and len(plain) > 2, sorted(plain)
    for verb in sorted({c.verb for c in formed}):
        row = VERB_TABLE[verb]
        subjects = {c.subject for c in formed if c.verb == verb}
        if not row.referent_class:
            assert subjects == {CASE_PARTY}, (verb, subjects)
        else:
            assert subjects <= {i for i, k in q.classes if k == row.referent_class}, (verb, subjects)


def test_cp_t05_04_d_limit_3_open_case_forms_on_the_docketed_person_and_the_fold_refuses_it():
    """LIMIT (3), found at the B10-05 close (the exit read the unclassed rows only, limit 2): the docket
    question's referents are matters still on the docket, `Person` is a class `open_case` declares, so the
    seat-holder it is delivered to forms `open_case` on the docketed person -- and `_eff_open_case`'s
    `docketed` decline refuses it. PINNED, not fixed: the realm's `case.refused` over `aperture 2 --seeds 0 1 2
    3 4` is 9 of 44 `open_case` attempts at the batch base, 7 of 33 after CP-T05-04 and 7 of 31 at the close,
    so the docket question added none the base lacked; and a person-side decline would need the docket, which
    only the world reads (AX-2). If that realm count ever rises above the base's, revert the docket question's
    call in `questions_for` (the two `referent_class` columns stay)."""
    w, d = _docketed_case()
    w.tick += 3
    duke = w.persons[DUKE]
    q = world_q.questions_for(w, duke)[0]
    assert q.id == f"q:docket:{CASE_PARTY}", q
    assert [i["matter"] for i in world_q.docketed(w, CASE_PARTY)] == [CASE_PARTY], "fixture: not docketed"
    oc = [c for c in _formed(w, DUKE, q) if c.verb == "open_case"]
    assert [c.subject for c in oc] == [CASE_PARTY], [(c.verb, c.subject) for c in oc]
    assert [e.kind for e in _fold(w, d, _act_of(oc[0], duke))] == ["case.refused"]


# ======================================================================================
# REM-2C (B10-05; rem-02 §2.3 REM-2C, limit `-08` AM-A-11): `research` FORMS ONLY ON A RECORD THE
# QUESTION IS ABOUT. One `referent_class: Record` column, and the one-value edit that takes `Record` out of
# `rosters.yaml: occasion_only_classes`, so REM-21's own-referent term stamps the question's own Records --
# NOT the stamp rem-02 rejected (every Record the person has heard of): the term reads the question, never
# the ledger. `research`'s cell asks `existence` of the collection itself (any document), so it adds no
# sub-kind to the two standing occasions' sets (`data/verbs.py::_record_subkinds_answered`). THE CLASS
# REMOVES WRONG-KIND FORMATIONS ONLY, AND IS SHARED: `research` also forms on the Records the standing
# occasions stamp, and the four other `Record` rows on the question's own Records, the fold disposing
# (pinned below). The readings (`research`'s `finding.none` admission refusals and executions, the five
# Record rows' wrong-kind refusals) are `aperture 1 s`'s, in the commit body, never an assertion here.
# ======================================================================================

#: The `Record` rows whose cell asks `existence` of the class itself (any document); control (3) walks them.
COLLECTION_ROWS = ("research",)
DOCUMENT = "doc_rem2c"


def _document(w, key=DOCUMENT, rung=SETTLEMENT):
    """A `text` Record lying at `rung` (the settlement `p_high` lives at), held by nobody: a document a
    question may be about. `text` is a sub-kind neither standing occasion stamps, so only the own-referent
    term can carry it as a `Record`."""
    w.records[key] = Record(key, rung, "text")
    return key


def _knows_of(w, pid, key, cid=None):
    """`pid`'s own ledger holds a firsthand claim on Record `key` (its making, `record.created`)."""
    w.persons[pid].ledger.append(Claim(cid or f"c_{pid}_{key}", pid, key, "record.created", True, w.tick,
                                       "firsthand", 100, "own"))


# --- (a) THE FORMATION: research FORMS ON THE RECORD AND ON NOTHING ELSE ----------------------

def test_rem2c_a_a_question_about_a_person_and_a_record_forms_research_on_the_record_only(monkeypatch):
    """THE FIRST ASSERTION, which deleting the column reddens (the mutation below runs that deletion
    in-process; the build ran it on the table too): `p_high` answers a question about `p_low` and a
    document; the own-referent term stamps the document as a `Record` (and `p_low` as a `Person`, REM-24's
    class), and `research` forms on the document and on nothing else. THE CONTROL: rows declaring no class
    still form on both, so the class removed `research`'s formation on the person and not the person's."""
    w, _ = _works_world()
    doc = _document(w)
    q = _ask(monkeypatch, w, PRESENT, refs=("p_low", doc))
    assert q.classes == (("p_low", "Person"), (doc, "Record")), q
    formed = _formed(w, PRESENT, q)
    assert [c.subject for c in formed if c.verb == "research"] == [doc], formed
    plain = {c.subject for c in formed if not VERB_TABLE[c.verb].referent_class}
    assert {"p_low", doc} <= plain, plain


def test_rem2c_a_mutation_without_its_column_research_forms_on_the_person_too(monkeypatch):
    """THE MUTATION, EXECUTED: the column deleted (the row copied with no class) and the assertion above has
    something to see -- `research` forms on both plain referents, the person first. The unclassed formation
    is the base reading's: formed for 83 of 83 persons, refused at admission on `exists:Record=0` 67/62/53
    (`aperture 1 s`, s = 0/1/2, the CP-T05-04 tree `ea6f1dba`)."""
    w, _ = _works_world()
    doc = _document(w)
    q = _ask(monkeypatch, w, PRESENT, refs=("p_low", doc))
    assert [c.subject for c in _formed_without_class(w, PRESENT, q, "research")] == ["p_low", doc]
    assert [c.subject for c in _formed(w, PRESENT, q) if c.verb == "research"] == [doc]


# --- (b) THE DONE TEST (P9): A RESEARCHER HOLDING A CLAIM ON A RECORD, THROUGH THE REAL FOLD -------

def test_rem2c_b_a_researcher_holding_a_claim_on_a_record_reaches_the_graded_route_through_the_fold():
    """THE DONE TEST, and the home's `[UNVERIFIED]` observed. `p_high` holds a firsthand claim on each of two
    documents lying at his own rung; each claim raises a `claim_landed` question about its document (the
    real `questions_for`, no stand-in). The question he answers carries ITS document as a `Record` and the
    other question carries no class (the term reads the question answered, never the ledger: a document he
    merely knows of is not stamped), and `research` forms on that document alone. Minted as the chooser
    mints it and folded by the real driver, it reaches FI-01's graded route -- a `finding.made` or a
    `finding.none` carrying a degree of the four bands, the roll thrown -- so the eligibility admitted the act
    on the classed `subject`: `own` admits first, and `presence:<site>` is never reached and binds no operand
    (the cell binds `subject` alone, and the payload carries no `site`). THE CONTROL, the same act on the
    person `p_low` (the formation the class removes): refused at admission, `finding.none` with NO degree,
    on `exists:Record` = 0."""
    w, d = _works_world()
    docs = (_document(w, "doc_a"), _document(w, "doc_b"))
    for doc in docs:
        _knows_of(w, PRESENT, doc)
    p = w.persons[PRESENT]
    head, *rest = world_q.questions_for(w, p)
    assert head.source == "claim_landed" and len(head.referents) == 1 and head.referents[0] in docs, head
    (doc,) = head.referents
    assert head.classes == ((doc, "Record"),), head
    assert rest and all(q.classes == () for q in rest) and {q.referents for q in rest} == {
        (o,) for o in docs if o != doc}, rest
    (c,) = [c for c in _formed(w, PRESENT, head) if c.verb == "research"]
    assert c.subject == doc
    act = _act_of(c, p)
    assert "site" not in act.payload, act.payload
    wrong = dataclasses.replace(act, id="a_research_on_a_person", payload={**act.payload, "subject": "p_low"})
    ok, _kinds_, verdict = d._admits(w, wrong, VERB_TABLE["research"])
    assert not ok and ("exists:Record", 0) in [(o.predicate, o.value) for o in verdict.observed], verdict
    (away,) = _fold(w, d, wrong)
    assert (away.kind, away.degree) == ("finding.none", None), (away.kind, away.degree)
    (here,) = _fold(w, d, act)
    assert here.kind in ("finding.made", "finding.none") and here.degree in GRADED_DEGREES, (
        here.kind, here.degree)


def test_rem2c_b_the_investigator_researches_the_held_forgery_where_his_answered_question_names_it():
    """FI-03's TRAIL ROUTE AT THE SHIPPED TABLE (`test_fi03_trail.py::chooser_research` walks it with the class
    blanked, a route the class closes). In FI-03's trail world at tick 2 the investigator holds the forged Record
    (a `faction_sheet`, given him at tick 1) and is asked about it three times, but the question he ANSWERS is about
    the forger: `research` forms on the Record from NONE of his questions -- the class stamps the answered question's
    own Records alone, and no standing occasion stamps a held sheet (pinned: the closed route). THE SHIPPED ROUTE:
    with an ambition of his about the Record, the question he answers names it (it now sorts first under
    `attention_key`) and carries it as a `Record`; `research` forms on it and on nothing
    else, its Candidate the blanked route's but for `to`, an operand its cell does not read (pinned below), and the
    act -- the id FI-03's own sweep found for a hand band -- resolved and witnessed through the driver draws a hand
    band and deposits the forger's deed: the find lands through the shipped class."""
    from . import test_fi03_trail as F
    w, d, rid = F.trail_world()
    p = w.persons[F.INVESTIGATOR]
    view = View(F.INVESTIGATOR, [], w.fixtures.get("view_k"))
    qs = world_q.questions_for(w, p)
    naming = [i for i, q in enumerate(qs) if rid in q.referents]
    assert len(naming) >= 1 and 0 not in naming, (naming, qs[0])
    assert not [c for q in qs for c in _options.opening_set(p, view, q, w.fixtures)
                if c.verb == "research" and c.subject == rid], "the closed route formed `research` on the sheet"
    blanked = F.chooser_research(w, rid)
    assert blanked is not None and blanked.subject == rid
    _ambition(w, F.INVESTIGATOR, "prop_rem2c_sheet", rid)
    head = world_q.questions_for(w, p)[0]
    assert rid in head.referents and (rid, "Record") in head.classes, head
    (cand,) = [c for c in _options.opening_set(p, view, head, w.fixtures) if c.verb == "research"]
    # The two Candidates differ in ONE carried operand the cell does not read: `to`. A CLASSED row skips the
    # document-content reader (`decision/options.py::_derive_operand`, `on_referent` False, B-K close COR 4), so `to`
    # binds the referent (the sheet); the blanked row read it off the sheet's content (the forger). `research`'s cell
    # binds `subject` alone, and no `site` is carried by either (`_REFERENT_OPERANDS`): `presence:<site>` binds nothing.
    assert VERB_TABLE["research"].requires_typed.operands() == ("subject",)
    assert (cand.subject, cand.operands) == (rid, {"subject": rid, "to": rid}), cand
    assert (blanked.subject, blanked.operands) == (rid, {"subject": rid, "to": F.FORGER}), blanked
    n, _blanked = F.find_band(F.HAND_BANDS)
    (finding,) = F.step(w, d, F.research(n, cand))
    assert finding.kind == "finding.made" and finding.degree in F.HAND_BANDS, (finding.kind, finding.degree)
    held = {(c.subject, c.source, c.value) for c in F.forged_claims(w, F.INVESTIGATOR)}
    assert held == {(F.FORGER, "inferred", True), (rid, "inferred", True)}, held


# --- (c) THE DEDUP, AND THE COST THE SHARED CLASS CREATES ---------------------------------------

def test_rem2c_c_a_record_a_standing_occasion_and_the_question_both_name_is_carried_once(monkeypatch):
    """THE DEDUP (`_stamped`, REM-21 (iv-b)), now that both kinds of term can name one Record. A standing
    occasion stamps it -- the petition `p_high` filed and holds (`records_held_for_holding_rows`) -- and the
    question he answers is about it too (the own-referent term names it). The question carries ONE
    `(id, Record)` pair, at the standing occasion's position (first in splice order), `Question` raises no
    `Forbidden`, and `research` forms on it once. THE CONTROL, the dedup dropped in-process (the bare
    concatenation it replaced): the same call is refused on the pair carried twice. (A writ is NOT this
    case since the B10-05 close: the own-referent term skips it, so `writs_held` alone carries it, below.)"""
    w, d = _works_world()
    pid, rec = PRESENT, _file_petition(w, d)
    assert world_q.records_held_for_holding_rows(w, w.persons[pid]) == (rec,)
    q = _ask(monkeypatch, w, pid, refs=("p_low", rec))
    assert world_q.own_referents_of_class(w, q)[-1] == rec, q
    assert [k for r, k in q.classes if r == rec] == ["Record"] and q.classes[0] == (rec, "Record"), q
    assert [c.subject for c in _formed(w, pid, q) if c.verb == "research"] == [rec]
    monkeypatch.setattr(world_q, "_stamped", lambda q_, added, w_: dataclasses.replace(
        q_, classes=q_.classes + tuple((o, w_.class_of(o)) for o in added)))
    with pytest.raises(Forbidden, match="twice"):
        world_q.questions_for(w, w.persons[pid])


def test_b10_05_close_a_writ_the_holder_and_the_question_both_name_is_carried_by_writs_held_alone():
    """The writ's side of the dedup, after the B10-05 close: the own-referent term skips a Record of a writ
    kind (`RECORD_REFERENT_KINDS`), so the writ's addressee-holder, whose question names it, carries ONE
    `(WRIT, Record)` pair, stamped by `writs_held`, and the own term adds nothing -- there is no second pair
    to dedup. `research` still forms on it once (the shared class)."""
    w, _ = _with_writ()
    _knows_of(w, HOLDER, WRIT)
    assert world_q.writs_held(w, w.persons[HOLDER]) == (WRIT,)
    q = world_q.questions_for(w, w.persons[HOLDER])[0]
    assert q.referents == (WRIT,), q
    assert world_q.own_referents_of_class(w, q) == ()
    assert [k for r, k in q.classes if r == WRIT] == ["Record"], q.classes
    assert [c.subject for c in _formed(w, HOLDER, q) if c.verb == "research"] == [WRIT]


def test_rem2c_c_the_class_is_shared_so_the_record_rows_form_on_each_others_records_and_the_fold_refuses(
        monkeypatch):
    """THE COST THE CLASS SHARING CREATES, MEASURED AND PINNED (the H-163 precedent; rem-02 REM-2C, *"the
    shared-class cost, measured"*). (1) `research` forms on a Record a standing occasion stamps as well as on
    the question's own: `p_high` holds his petition and is asked about `p_low` and a document, and `research`
    forms on both Records, each admitted (any document answers its cell). (2) The four other `Record` rows
    form on the question's own document, and each, force-admitted, is refused on its own sub-kind (`carry`
    `exists:petition` = 0, `found` and `build` `exists:works` = 0, `comply`, once his ledger names the
    document, `exists:dispensation` = 0): a wrong-SUB-kind refusal, the realm's `record_subkind` column."""
    w, d = _works_world()
    pet = _file_petition(w, d)
    doc = _document(w)
    q = _ask(monkeypatch, w, PRESENT, refs=("p_low", doc))
    p = w.persons[PRESENT]
    assert q.classes == ((pet, "Record"), ("p_low", "Person"), (doc, "Record")), q
    _knows_of(w, PRESENT, doc)                 # after the question: `comply` forms on what his ledger names
    formed = collections.defaultdict(list)
    for c in _formed(w, PRESENT, q):
        formed[c.verb].append(c)
    assert [c.subject for c in formed["research"]] == [pet, doc], formed["research"]
    for c in formed["research"]:
        assert d._admits(w, _act_of(c, p), VERB_TABLE["research"])[0], c
    for verb, wanted in (("carry", "exists:petition"), ("found", "exists:works"), ("build", "exists:works"),
                         ("comply", "exists:dispensation")):
        (c,) = [c for c in formed[verb] if c.subject == doc]
        ok, _k, verdict = d._admits(w, _act_of(c, p), VERB_TABLE[verb])
        assert not ok and (wanted, 0) in [(o.predicate, o.value) for o in verdict.observed], (verb, verdict)


# --- (d) THE SECOND MUTATION: `Record` BACK IN `occasion_only_classes` ----------------------------

def test_rem2c_d_with_record_back_in_the_list_research_forms_only_on_a_record_he_holds(monkeypatch):
    """THE ROSTER HALF REVERTED ALONE, IN-PROCESS (`Record` put back in `occasion_only_classes`; the build ran
    the same edit on `rosters.yaml` itself): the question's own document is no longer stamped, so `research`
    forms on nothing from the formation test's question; and, the class being shared, it then forms ONLY on
    a Record a standing occasion stamps -- the petition he holds. The column without the roster edit makes
    `research` a held-Record verb, which is not the act rem-02 asked for (the document the question is
    about). THE CONTROL is the formation test: same world, the shipped list."""
    monkeypatch.setattr(world_q, "OCCASION_ONLY_CLASSES", OCCASION_ONLY_CLASSES | {"Record"})
    w, d = _works_world()
    doc = _document(w)
    q = _ask(monkeypatch, w, PRESENT, refs=("p_low", doc))
    assert q.classes == (("p_low", "Person"),), q
    assert not [c for c in _formed(w, PRESENT, q) if c.verb == "research"]
    pet = _file_petition(w, d)
    q = world_q.questions_for(w, w.persons[PRESENT])[0]
    assert [r for r, k in q.classes if k == "Record"] == [pet], q
    assert [c.subject for c in _formed(w, PRESENT, q) if c.verb == "research"] == [pet]


# --- (c) CONTROL (3) OF B10-05's HR-9: A CLASS REMOVES REFUSALS AND NOTHING ELSE --------------

#: The classes whose rows control (3) walks. The ROWS are read off the table, so a later item that
#: declares `Proposition` or `Person` on a row is under the control the moment its column lands: nothing
#: here names a verb but `SITE_ROWS`, `PROPOSITION_ROWS` and `PERSON_ROWS` (the rows whose extra
#: assertions are stated), and a row is added by its data and never by a copy.
CONTROL3_CLASSES = frozenset({"Site", "Proposition", "Person"})

#: THE ONE PLACE THE PROOF DOES NOT HOLD (CP-T05-04): `open_case`'s `Person` class removes formations the
#: fold ADMITS, because the row is a `remit:` verb whose cell asks the seat's purview over the matter's
#: PLACE and no kind (`basis: purview`), so the Site and the settlement rung of the question are matters
#: the Duke's seat reaches and the fold opens a case on. The home states it as the point (D:#75: stop
#: docketing Rungs `determine` can never take off), so the loop does not assert `not ok` for this row; it
#: pins the removed Candidates' admitted subjects exactly (`{verb: subjects}`), so the exemption is
#: observed and cannot go stale, and the Proposition (no place: `purview` False) is still held to a
#: refusal. Every other classed row is held to the unconditional `not ok`. (v10 REM-2C: `research` enters the
#: loop by its cell and is NOT here -- every Candidate its class removes is refused on `exists:Record` = 0, a
#: removal of refusals only, which the exact equality below observes.)
REMOVES_ADMITTED = {"open_case": frozenset({"site_harbour", "S"})}


def _control3_rows() -> dict:
    """The classed rows control (3) walks: every row declaring one of `CONTROL3_CLASSES`, plus (v10 REM-25)
    the `Record` rows whose cell asks the actor to HOLD the subject and (v10 REM-2C) those whose cell asks
    `existence` of the class itself (any document) -- read off the cell, not a verb name. `comply`, the
    other `Record` row, forms on a writ its own ledger names (`referent_named`) and keeps its addressee test;
    it is held to `test_in09_dispensation_answer.py`'s formation tests."""
    return {v: r for v, r in VERB_TABLE.items()
            if r.referent_class in CONTROL3_CLASSES
            or (r.referent_class == "Record" and (
                _verbs._asks_subject_held(r)
                or r.referent_class in _existence_kinds(r.requires_typed.requirement)))}


def _existence_kinds(req) -> frozenset:
    """The `kind` of every `existence` clause in a typed cell (`AllOf` nested or not)."""
    if isinstance(req, Existence):
        return frozenset({req.kind})
    if isinstance(req, AllOf):
        return frozenset().union(*(_existence_kinds(x) for x in req.clauses))
    return frozenset()


#: v10 REM-28: the kind clause an UNTYPED PREDICATE row refuses a wrong-kind referent on -- the text of REM-14's
#: `_refuse` trace row (`loop/predicates.py`), the one read such a row leaves, since a predicate records no `observed`
#: and its Verdict is `UNKNOWN` with none (`dispatch`: `_req_dispatch`, 'names no person the world holds').
PREDICATE_KIND_CLAUSES = {"dispatch": "names no person the world holds"}


def _refusal_clauses(call):
    """`(call's answer, the clause of every DECISION refusal row the call appended to the trace)`: `test_rem14_...`'s
    reader, the cluster key `harness/report.py` groups a predicate's refusals by."""
    first = len(TRACE.rows)
    out = call()
    return out, [r.what.split(" -> ")[0] for r in TRACE.rows[first:]
                 if r.channel == "DECISION" and r.detail.get("chose") == "refuse"]


def _refuses_on_the_rows_kind(row, verdict, c, clauses=()):
    """The refusal is the row's own kind test: where the cell asks `existence` of a kind, an
    `exists:<kind>` read came back 0; where it asks none (`work`'s threshold), the read of the referent
    came back UNKNOWN and the verdict is not True. Anything else is a refusal for another reason, and
    a class that removed it would be removing a refusal that was not about kind. A cell asking several
    kinds (REM-24's `petition`: its person AND the rung it rises from) is held to the one the class
    names, so a formation refused only on its OTHER side would not pass for a wrong-kind one.
    v10 REM-28: a row with NO typed cell (`dispatch`, a registered predicate) leaves no read, so the verdict
    cannot show the kind; its refusal clause (`clauses`, from `_refusal_clauses`) is held to
    `PREDICATE_KIND_CLAUSES` instead, and a refusal for another reason (eligibility, a different clause)
    leaves no such clause and fails here."""
    if row.requires_typed is None:
        assert any(PREDICATE_KIND_CLAUSES[row.verb] in cl for cl in clauses), (row.verb, c, clauses)
        return
    kinds = _existence_kinds(row.requires_typed.requirement) if row.requires_typed is not None else frozenset()
    if kinds:
        asked = kinds & {row.referent_class} or kinds
        assert any(o.predicate == f"exists:{k}" and o.value in (0, False)
                   for k in asked for o in verdict.observed), (row.verb, c, verdict)
    else:
        assert verdict.value is UNKNOWN and any(o.value is UNKNOWN for o in verdict.observed), (
            row.verb, c, verdict)


def test_rem22_c_every_candidate_a_class_removes_force_admitted_refuses_on_the_rows_kind(monkeypatch):
    """HR-9 CONTROL (3), for every row declaring `Site`, `Proposition` or `Person`: the Candidates its
    class removes -- those the row would form on the question's referents of any other class were it
    classless -- are force-admitted through the fold's own `_admits` (the Candidate minted as the chooser
    mints it) and each is refused on the row's kind. A PROOF, NOT A COUNT: the class removes refusals and
    nothing else. The loop asserts that it checked at least one removed Candidate for EVERY classed row,
    and the Site rows', the Proposition row's and the Person row's own Candidate (the one the class keeps)
    is admitted by the same call, so a refusal here is not the fold refusing everything. REM-23's `commit`
    and REM-24's `petition` entered this loop by their column alone: `rows` is read off the table.

    REM-25: `carry`, `found` and `build` enter by their column and their cell (`_control3_rows`: a `Record`
    row whose cell asks `held_by` of `subject`), in a world where `p_high` HOLDS a petition and a works, so
    the question carries two Records. A `Record` row's class keeps every held Record (one class cannot tell
    a petition from a works), so for these rows the kept Candidates are one per held Record and the loop
    asserts exactly those on a Record of the row's own kind are admitted, and that there is at least one.

    CP-T05-04: `argue` (`Proposition`) and `open_case` (`Person`) enter by their column, in a world that also
    holds a hearer the arguer knows at his own place (`_hearer_world`: `argue` forms one Candidate per known
    hearer, and its kept Candidate must be one the fold admits, which needs the hearer WITH him).
    ⚠ THE PROOF FAILS FOR `open_case` AND THE LOOP SAYS SO RATHER THAN BENDING: its class removes
    formations on the Site and the rung that the fold ADMITS (`REMOVES_ADMITTED`), pinned exactly, with the
    Proposition still refused (on `purview`, a Proposition has no place).

    REM-2C: `research` enters by its column and its cell (`_control3_rows`: a `Record` row whose cell asks
    `existence` of the class itself). Its class keeps the two held Records (a standing occasion's stamp; the
    class is shared) and both are admitted, any document answering its cell; every Candidate it removes -- the
    question's person, Site, Proposition and rung -- is refused on `exists:Record` = 0, so it is held to the
    unconditional `not ok` and is no `REMOVES_ADMITTED` row.

    REM-28: `dispatch` (`Person`) enters by its column. It is an UNTYPED predicate row, so its removed Candidates
    leave no `exists:` read to observe; each is held to the refusal clause `_req_dispatch` traces
    (`PREDICATE_KIND_CLAUSES`), and its kept Candidate is admitted by `test_rem28_c_...` below."""
    w, d = _hearer_world()
    pet = _file_petition(w, d)
    _declare(w, d, "wk_c3", "hearth", SETTLEMENT, actor=PRESENT)
    q = _ask(monkeypatch, w, PRESENT)
    p = w.persons[PRESENT]
    rows = _control3_rows()
    assert set(SITE_ROWS + PROPOSITION_ROWS + PERSON_ROWS + HOLDING_ROWS + PROCEEDINGS_ROWS
               + COLLECTION_ROWS) <= set(rows), sorted(rows)
    formed = _formed(w, PRESENT, q)
    kept = {c.verb: c for c in formed}
    checked = collections.Counter()
    admitted_removed = collections.defaultdict(set)
    for verb, row in sorted(rows.items()):
        own = {r for r, k in q.classes if k == row.referent_class}
        removed = [c for c in _formed_without_class(w, PRESENT, q, verb) if c.subject not in own]
        for c in removed:
            (ok, _kinds_, verdict), clauses = _refusal_clauses(lambda: d._admits(w, _act_of(c, p), row))
            checked[verb] += 1
            if verb in REMOVES_ADMITTED:
                if ok:
                    admitted_removed[verb].add(c.subject)
                else:
                    assert any(o.predicate.startswith("purview:") and o.value is False for o in verdict.observed), (
                        verb, c, verdict)
                continue
            assert not ok, (verb, c)
            _refuses_on_the_rows_kind(row, verdict, c, clauses)
        if verb in SITE_ROWS + PROPOSITION_ROWS + PERSON_ROWS + PROCEEDINGS_ROWS:
            assert {c.subject for c in removed} == set(MIXED) - own, (verb, removed)
            assert d._admits(w, _act_of(kept[verb], p), row)[0], (verb, kept[verb])
        if row.referent_class == "Record":
            mine = [c for c in formed if c.verb == verb]
            assert own == {pet, "wk_c3"} and {c.subject for c in mine} == own, (verb, own, mine)
            kinds = _existence_kinds(row.requires_typed.requirement)
            admitted = {c.subject for c in mine if d._admits(w, _act_of(c, p), row)[0]}
            # REM-2C: a cell asking `existence` of the class itself is answered by a Record of any kind.
            assert admitted == {r for r in own if row.referent_class in kinds or w.records[r].kind in kinds} \
                and admitted, (verb, admitted)
            assert {c.subject for c in removed} == set(MIXED), (verb, removed)
    assert set(checked) == set(rows) and min(checked.values()) >= 1, (sorted(rows), checked)
    assert {v: frozenset(s) for v, s in admitted_removed.items()} == REMOVES_ADMITTED, dict(admitted_removed)


# ======================================================================================
# v10 REM-27 (B10-06, AM-A-13 limit): `march` DECLARES `Rung`; THE STANDING `Rung` STAMP CARRIES THE FIELD
# ======================================================================================
# THE CLAIM: a seated marcher told of a defended settlement of another faction forms `march` on it, and
# the act, minted as the chooser mints it, is folded by the real driver through RESOLVE and ENCOUNTER to a
# fought field (`Won` or `Lost`), writing `Person.stance` on the losing side (`_eff_march`). The reading is
# "reaches a field", never "contests one" (`massbattle.py::_weighted_unit`, `troops=weight`). The field
# is stamped by `world_q.places_named`, the `Rung` occasion already in the splice: a `fields_named` term
# was built beside it and measured unearned (stubbed to `()`, the march still formed on this field), so
# it is not in the tree. MUTATION, executed below in REM-22's shape: the column deleted, and the march no
# longer forms on the field.

MARCHER, MARCHER_SEAT, ORIGIN, FIELD = "p_npc_033", "off_npc_033", "set_s_014", "set_s_036"


def _told_of_field():
    """`build_realm(0)` with `MARCHER` (Crown, a seat granting `dispatch`) told of `FIELD` (Church of
    Solmund, defended): one claim about the settlement in his own ledger, the shape any deposit about
    the place leaves (`person_q.ledger_names` reads its subject). Before it, nothing stamps him the field
    and it is not what his question is about."""
    from engine.season.harness.populated import build_realm
    w = build_realm(0)
    p = w.persons[MARCHER]
    q0 = world_q.questions_for(w, p)
    assert FIELD not in world_q.places_named(w, p), "fixture: the marcher already knows of the field"
    assert not q0 or (FIELD, "Rung") not in q0[0].classes, q0
    p.ledger.append(Claim("c_rem27_field", MARCHER, FIELD, "exists:Rung", 1, 0, "firsthand", 100, "own"))
    return w, p


def test_rem27_a_the_row_declares_rung_and_the_remit_acts_widen_to_dispatch_by_derivation():
    """The column, and the derived widening it brings, named: `RUNG_REMIT_ACTS` is read off every `Rung`
    row's `remit:` alternatives, so `march`'s `remit:dispatch` joins `requisition`'s `issue`. v10 REM-28
    (B10-06): `convene` declares `Rung` too, so its `remit:convene` joins the set (`{issue, dispatch}` to
    `{issue, dispatch, convene}`). The set is derived off the rows; this pins its value so the widening is
    named, not silent."""
    assert VERB_TABLE["march"].referent_class == "Rung"
    assert _verbs.RUNG_REMIT_ACTS == frozenset({"issue", "dispatch", "convene"}), _verbs.RUNG_REMIT_ACTS


def test_rem27_a_a_seated_marcher_told_of_a_defended_field_marches_on_it_and_fights_it():
    """THE FALSIFIER (P9 DONE, through the real fold): the `Rung` occasion stamps `FIELD`, `march` forms on
    it, the chooser's act exercises the dispatch seat, and RESOLVE then ENCOUNTER fight a field whose
    losing side gains a `Person.stance` row. THE CONTROL beside it: the settlement is another faction's
    and defended (`world_q.mustered` names its defenders), so the field is not `Unopposed`."""
    from .test_march import _fold_one
    w, p = _told_of_field()
    assert FIELD in world_q.places_named(w, p)
    attacker_f = world_q.faction_of(w, MARCHER)
    holder_f = world_q.holder_faction_of(w, FIELD)
    assert holder_f and holder_f != attacker_f, (attacker_f, holder_f)
    defenders = world_q.mustered(w, FIELD, holder_f)
    attackers = world_q.mustered(w, ORIGIN, attacker_f)
    assert defenders and attackers, (defenders, attackers)
    q = world_q.questions_for(w, p)[0]
    assert (FIELD, "Rung") in q.classes, q
    marches = {c.subject: c for c in _formed(w, MARCHER, q) if c.verb == "march"}
    assert FIELD in marches, sorted(marches)
    act = _act_of(marches[FIELD], p)
    assert act.via == MARCHER_SEAT and act.payload.get("subject") == FIELD, act
    before = {pid: list(w.persons[pid].stance or []) for pid in attackers + defenders}
    kinds = [(e.kind, e.degree) for e in _fold_one(w, act)]
    assert ("march.declared", "Declared") in kinds, kinds
    fought = {deg for k, deg in kinds if k in ("field.won", "field.lost")}
    assert fought in ({"Won"}, {"Lost"}), kinds
    losers = defenders if fought == {"Won"} else attackers
    grew = [pid for pid in losers if len(w.persons[pid].stance or []) > len(before[pid])]
    assert grew and len(grew) == len(losers), (fought, losers, grew)


def test_rem27_a_mutation_without_the_column_the_march_no_longer_forms_on_the_field():
    """THE MUTATION, EXECUTED in REM-22's shape: `march`'s `referent_class` deleted (the base table's
    formation, `_formed_without_class`), the same marcher on the same question no longer forms `march` on
    `FIELD` -- the row forms on the question's single plain referent, which is not the field. The column
    restored, the same question forms it (so the mutation had something to see)."""
    w, p = _told_of_field()
    q = world_q.questions_for(w, p)[0]
    assert FIELD not in q.referents, q
    unclassed = _formed_without_class(w, MARCHER, q, "march")
    assert unclassed and FIELD not in {c.subject for c in unclassed}, unclassed
    assert any(c.verb == "march" and c.subject == FIELD for c in _formed(w, MARCHER, q))


# ======================================================================================
# v10 REM-28 (B10-06): `convene` DECLARES `Rung`; THE STANDING `Rung` STAMP IS THE ONLY PLACE IT FORMS
# ======================================================================================
# THE CLAIM: a seated convener answering a question about a person, a Proposition and a place he has been
# told of forms `convene` on the place and on nothing else. The person (a `person`-kind rung is "an address,
# not a place": `_req_convene`'s ordinal floor) and the Proposition (no rung the world holds) are the
# formations the class removes, and the fold refuses each; the place it keeps is admitted and folds to a
# scheduled sitting held by the seat that convened it. MUTATION, executed below in REM-22's shape
# (`_formed_without_class`): the column deleted, and the verb forms on all three again. The reading behind
# it is `aperture 1 s` (`verb_table.yaml`'s `convene` note): 9 of the 11 pooled attempts were refused on
# exactly those two kinds.

CONVENE_REFS = ("p_low", "prop_x", HEARTH)


def _convener_told_of_the_hearth(monkeypatch):
    """`_works_world` (`p_high` sits `off_duke`, whose grant carries `convene`, and lives at `S`) with the hearth
    `Hh` -- below `S`, not a rung he lives under -- named by a firsthand claim in his own ledger, dated before the
    landing floor so it raises no question of its own; he then answers a question about a person, a Proposition
    and that hearth. The hearth is the one thing `world_q.places_named` stamps as a `Rung` (the question's own
    Rung referent is not: `Rung` is `occasion_only`)."""
    w, d = _works_world()
    p = w.persons[PRESENT]
    p.ledger.append(Claim(f"c_rem28_{HEARTH}", PRESENT, HEARTH, "exists:Rung", 1, -2, "firsthand", 100, "own"))
    assert world_q.places_named(w, p) == (HEARTH,), world_q.places_named(w, p)
    return w, d, _ask(monkeypatch, w, PRESENT, CONVENE_REFS)


def test_rem28_a_a_question_about_a_person_a_proposition_and_a_told_of_place_forms_convene_on_the_place_only(
        monkeypatch):
    """THE FIRST ASSERTION, which deleting the column reddens (`test_rem28_a_mutation_...` below runs that
    deletion): the three referents are carried as their three classes, and `convene` forms on the `Rung` and
    on nothing else. THE CONTROL: the person still forms the plain rows on all three, so the class removed
    this verb's formations and not the person's."""
    w, _, q = _convener_told_of_the_hearth(monkeypatch)
    assert VERB_TABLE["convene"].referent_class == "Rung"
    assert set(q.classes) == {(HEARTH, "Rung"), ("p_low", "Person"), ("prop_x", "Proposition")}, q
    formed = _formed(w, PRESENT, q)
    assert [c.subject for c in formed if c.verb == "convene"] == [HEARTH], formed
    plain = {c.subject for c in formed if not VERB_TABLE[c.verb].referent_class}
    assert set(CONVENE_REFS) <= plain, plain


def test_rem28_a_every_candidate_the_class_removes_is_refused_by_the_fold_and_the_one_it_keeps_is_admitted(
        monkeypatch):
    """A PROOF, NOT A COUNT (REM-22's control (3), for a predicate row): the Candidates the class removes --
    the person and the Proposition, which the classless row forms -- are force-admitted through the fold's own
    `_admits` and each is refused, and the one it keeps is admitted by the same call, so a refusal here is not
    the fold refusing everything. The loop asserts it checked both removed kinds."""
    w, d, q = _convener_told_of_the_hearth(monkeypatch)
    p, row = w.persons[PRESENT], VERB_TABLE["convene"]
    removed = [c for c in _formed_without_class(w, PRESENT, q, "convene") if c.subject != HEARTH]
    assert {c.subject for c in removed} == {"p_low", "prop_x"}, removed
    for c in removed:
        assert not d._admits(w, _act_of(c, p), row)[0], c
    (kept,) = [c for c in _formed(w, PRESENT, q) if c.verb == "convene"]
    assert d._admits(w, _act_of(kept, p), row)[0], kept


def test_rem28_a_mutation_without_its_column_the_row_forms_on_the_person_and_the_proposition_too(monkeypatch):
    """THE MUTATION, EXECUTED: the column deleted (the row copied with no class) and the assertion above has
    something to see -- `convene` forms on all three plain referents, the person (a person-rung) and the
    Proposition among them. The unclassed formation is the base reading's: 9 of 11 attempts refused, 8 on a
    person-rung and 1 on a Proposition (`aperture 1 s`, s = 0/1/2, realm and spine, the REM-27 tree)."""
    w, _, q = _convener_told_of_the_hearth(monkeypatch)
    assert [c.subject for c in _formed_without_class(w, PRESENT, q, "convene")] == list(CONVENE_REFS)
    assert [c.subject for c in _formed(w, PRESENT, q) if c.verb == "convene"] == [HEARTH]


def test_rem28_b_a_convener_convening_at_a_told_of_place_executes_through_the_fold(monkeypatch):
    """THE DONE TEST (P9): the Candidate the question forms on the hearth is minted as the chooser mints it and
    folded by the real driver: `date.scheduled`, and a Date at the hearth held by the SEAT that convened it
    (`Act.via`, the convened-slot step: CALENDAR forms a docket slot only for a date with a holder). THE
    CONTROL, the Candidate the unclassed row forms on the person: the fold emits `convene.refused` and
    schedules nothing."""
    w, d, q = _convener_told_of_the_hearth(monkeypatch)
    p = w.persons[PRESENT]
    (person_c,) = [c for c in _formed_without_class(w, PRESENT, q, "convene") if c.subject == "p_low"]
    refused = dataclasses.replace(_act_of(person_c, p), id="a_rem28_convene_on_the_person")   # one act per id
    assert _kinds(_fold(w, d, refused)) == ["convene.refused"] and not w.dates, w.dates
    (kept,) = [c for c in _formed(w, PRESENT, q) if c.verb == "convene"]
    act = _act_of(kept, p)
    assert _kinds(_fold(w, d, act)) == ["date.scheduled"]
    (date,) = w.dates.values()
    assert date["venue"] == HEARTH and date["holder"] == act.via == "off_duke" and date["convening_attached"], date


# ======================================================================================
# v10 REM-28 (B10-06): `dispatch` DECLARES `Person`; THE QUESTION'S OWN PERSON IS THE ONLY NAME IT FORMS ON
# ======================================================================================
# THE CLAIM: a seat granting `dispatch` answering a question about a settlement, a harbour, a document and a
# person forms `dispatch` on the person and on nothing else. The settlement, the Site and the Record are what
# `_req_dispatch` refuses ('names no person the world holds'): 16 of 33 pooled attempts at `aperture 1 s`, all
# one clause, a Rung 14, a Record 1, a Site 1. `dispatch` is an UNTYPED predicate row, so the refusal leaves no
# `observed` read: the fold proof below reads REM-14's refusal clause instead (`_refusal_clauses`). MUTATION,
# executed below in REM-22's shape (`_formed_without_class`): the column deleted, and the verb forms on all four.

DISPATCH_REFS = (SETTLEMENT, HARBOUR, DOCUMENT, "p_low")


def _dispatcher_asked_about_a_person_and_three_things(monkeypatch):
    """`_works_world` (`p_high` sits `off_duke`, whose grant carries `dispatch`; the settlement `S` is his home)
    with a document lying at `S`, asked about the settlement, the harbour on it, the document and `p_low`. The
    own-referent term carries the Site, the Record and the Person as their classes; the settlement is carried as
    nothing (`Rung` is `occasion_only`, and `S` is where he lives)."""
    w, d = _works_world()
    _document(w)
    return w, d, _ask(monkeypatch, w, PRESENT, DISPATCH_REFS)


def test_rem28_c_a_question_about_a_rung_a_site_a_record_and_a_person_forms_dispatch_on_the_person_only(
        monkeypatch):
    """THE FIRST ASSERTION, which deleting the column reddens (`test_rem28_c_mutation_...` below runs that
    deletion): the four referents are carried as what they are, and `dispatch` forms on the person alone, even
    though the Record and the Site are carried as classes too (the class is `Person`, not `stamped`). THE
    CONTROL: the person still forms the plain rows on all four, so the class removed this verb's formations
    and not the person's."""
    w, _, q = _dispatcher_asked_about_a_person_and_three_things(monkeypatch)
    assert VERB_TABLE["dispatch"].referent_class == "Person"
    assert set(q.classes) == {(HARBOUR, "Site"), (DOCUMENT, "Record"), ("p_low", "Person")}, q
    formed = _formed(w, PRESENT, q)
    assert [c.subject for c in formed if c.verb == "dispatch"] == ["p_low"], formed
    plain = {c.subject for c in formed if not VERB_TABLE[c.verb].referent_class}
    assert set(DISPATCH_REFS) <= plain, plain


def test_rem28_c_every_candidate_the_class_removes_is_refused_on_the_named_person_clause_and_the_kept_one_admitted(
        monkeypatch):
    """A PROOF, NOT A COUNT (REM-22's control (3), for an untyped predicate row): the Candidates the class
    removes -- the settlement, the Site and the Record, which the classless row forms -- are force-admitted
    through the fold's own `_admits` and each is refused on `_req_dispatch`'s clause 'names no person the world
    holds' (read off the trace: the row records no `observed`), and the one it keeps is admitted by the same
    call, so a refusal here is neither the fold refusing everything nor a refusal for another reason."""
    w, d, q = _dispatcher_asked_about_a_person_and_three_things(monkeypatch)
    p, row = w.persons[PRESENT], VERB_TABLE["dispatch"]
    removed = [c for c in _formed_without_class(w, PRESENT, q, "dispatch") if c.subject != "p_low"]
    assert {c.subject for c in removed} == {SETTLEMENT, HARBOUR, DOCUMENT}, removed
    for c in removed:
        (ok, _kinds_, verdict), clauses = _refusal_clauses(lambda: d._admits(w, _act_of(c, p), row))
        assert not ok and verdict.observed == (), (c, verdict)
        _refuses_on_the_rows_kind(row, verdict, c, clauses)
    (kept,) = [c for c in _formed(w, PRESENT, q) if c.verb == "dispatch"]
    (ok, _kinds_, _v), clauses = _refusal_clauses(lambda: d._admits(w, _act_of(kept, p), row))
    assert ok and clauses == [], (kept, clauses)


def test_rem28_c_mutation_without_its_column_the_row_forms_on_the_rung_the_site_and_the_record_too(monkeypatch):
    """THE MUTATION, EXECUTED: the column deleted (the row copied with no class) and the assertion above has
    something to see -- `dispatch` forms on all four plain referents, the settlement, the harbour and the
    document among them. The unclassed formation is the base reading's: 16 of 33 attempts refused, a Rung 14,
    a Record 1, a Site 1 (`aperture 1 s`, s = 0/1/2, realm and spine, the convene commit `b8fd583b`)."""
    w, _, q = _dispatcher_asked_about_a_person_and_three_things(monkeypatch)
    assert [c.subject for c in _formed_without_class(w, PRESENT, q, "dispatch")] == list(DISPATCH_REFS)
    assert [c.subject for c in _formed(w, PRESENT, q) if c.verb == "dispatch"] == ["p_low"]


def test_rem28_d_a_dispatcher_ordering_the_named_person_executes_through_the_fold(monkeypatch):
    """THE DONE TEST (P9): the Candidate the question forms on the person is minted as the chooser mints it and
    folded by the real driver: `order.given`, the order given through the seat that issued it. THE CONTROL, the
    Candidate the unclassed row forms on the settlement: the fold emits `dispatch.refused` and no order."""
    w, d, q = _dispatcher_asked_about_a_person_and_three_things(monkeypatch)
    p = w.persons[PRESENT]
    (rung_c,) = [c for c in _formed_without_class(w, PRESENT, q, "dispatch") if c.subject == SETTLEMENT]
    refused = dataclasses.replace(_act_of(rung_c, p), id="a_rem28_dispatch_to_the_settlement")   # one act per id
    assert _kinds(_fold(w, d, refused)) == ["dispatch.refused"]
    (kept,) = [c for c in _formed(w, PRESENT, q) if c.verb == "dispatch"]
    act = _act_of(kept, p)
    assert act.payload.get("subject") == "p_low" and act.via == "off_duke", act
    assert _kinds(_fold(w, d, act)) == ["order.given"]


def test_rem28_c_the_class_moves_no_derived_set():
    """`Person` is declared already (`open_case`, `petition`) and `RUNG_REMIT_ACTS` reads the `Rung` rows alone, so
    the column moves neither derived set: both are re-derived over the table with `dispatch`'s column blanked and
    read the shipped sets. THE CONTROL, that the derivation can move: with `convene`'s `Rung` column blanked the
    remit set loses `convene`, and a table with no `Person` row at all (`dispatch`, `open_case` and `petition`
    blanked) loses `Person` from `DECLARED_CLASSES`, so neither equality is one a constant could satisfy."""
    classless = lambda *verbs: {**VERB_TABLE, **{v: dataclasses.replace(VERB_TABLE[v], referent_class="")
                                                  for v in verbs}}
    with mock.patch.object(_verbs, "VERB_TABLE", classless("dispatch")):
        assert _verbs._derive_rung_remit_acts() == _verbs.RUNG_REMIT_ACTS
        assert _verbs._derive_declared_classes() == _verbs.DECLARED_CLASSES
    with mock.patch.object(_verbs, "VERB_TABLE", classless("convene")):
        assert _verbs._derive_rung_remit_acts() == _verbs.RUNG_REMIT_ACTS - {"convene"}
    with mock.patch.object(_verbs, "VERB_TABLE", classless("dispatch", "open_case", "petition")):
        assert "Person" not in _verbs._derive_declared_classes()
    assert _verbs.RUNG_REMIT_ACTS == frozenset({"issue", "dispatch", "convene"}), _verbs.RUNG_REMIT_ACTS


# ======================================================================================
# v10 REM-28 (B10-06): `revoke` DECLARES `Office`; THE COLUMN REMOVES A FORMATION AND EXECUTES NOTHING
# ======================================================================================
# THE CLAIM, AND ITS LIMIT. A seat granting `revoke` answering a question about a person, a place and a seat it
# was told of forms `revoke` on the seats the question carries as `Office` and on nothing else. Every refusal the
# class removes is the one clause 'a revoke names no office the world holds' (18 of 18 pooled attempts at
# `aperture 1 s`: a person 8, a rung 8, a Record 1, a Site 1, an Office 0). BUT `_req_revoke` reads
# `payload['office']` and a computed act carries `subject` (`loop/predicates.py::office_named_by`: `revoke` IS NOT A
# CALLER, IN-53 D1; H-207 ruling (A)), so the formations that SURVIVE are refused on that same clause: executions
# stay 0 -> 0 by design, and the caller that would read `subject` is H-207 (A)'s, not this item's. The tests below
# hold both halves: what the class removes, and what it leaves refused. With a caller, `rem28_f` and the kept-Candidates
# loop of the second test are the ones to re-scope (they assert the computed act is refused); the formation, the
# mutation and the removed-Candidates half do not move.

REVOKER, REVOKE_TARGET = "p_king", "off_duke"
REVOKE_REFS = ("p_low", HEARTH, REVOKE_TARGET)
NO_OFFICE_CLAUSE = "a revoke names no office the world holds"


def _revoker_asked_about_a_person_a_place_and_a_seat(monkeypatch):
    """`test_g3_not_yours.py::_gov_world` (`p_king` sits `off_crown`, the King on the rung above the Duke, and
    `off_mayor`, both granting `confer` and `revoke`; the Duke's seat is held by `p_high`; `off_reeve` is a vacant
    Crown seat the King may fill) with the Duke's seat named by a firsthand claim in the King's own ledger, dated
    before the landing floor so it raises no question of its own. He then answers a question about a person, a
    hearth and that seat. The standing occasions stamp two seats as `Office` (`seats_named`: the Duke's, which he was
    told of; `vacancies`: `off_reeve`, which he may fill); the person is a `Person`; the hearth is carried as
    nothing (`Rung` is `occasion_only`, and the King knows nothing of it)."""
    w, d = _gov_world()
    w.persons[REVOKER].ledger.append(Claim(f"c_rem28_{REVOKE_TARGET}", REVOKER, REVOKE_TARGET, "exists:Office", 1, -2,
                                           "firsthand", 100, "own"))
    return w, d, _ask(monkeypatch, w, REVOKER, REVOKE_REFS)


def test_rem28_e_a_question_about_a_person_a_place_and_a_seat_forms_revoke_on_the_seats_only(monkeypatch):
    """THE FIRST ASSERTION, which deleting the column reddens (`test_rem28_e_mutation_...` below runs that deletion):
    the person and the seats are carried as their classes and `revoke` forms on the seats and on neither the person
    nor the place -- one Candidate per granting seat (H-134), two seats, so each Office twice. THE CONTROL: the
    King still forms the plain rows on all three referents, so the class removed this verb's formations and not his."""
    w, _, q = _revoker_asked_about_a_person_a_place_and_a_seat(monkeypatch)
    assert VERB_TABLE["revoke"].referent_class == "Office"
    assert set(q.classes) == {(REVOKE_TARGET, "Office"), ("off_reeve", "Office"), ("p_low", "Person")}, q
    formed = _formed(w, REVOKER, q)
    mine = [c for c in formed if c.verb == "revoke"]
    assert collections.Counter(c.subject for c in mine) == {REVOKE_TARGET: 2, "off_reeve": 2}, mine
    assert {seat_of(w.persons[REVOKER], c) for c in mine} == {"off_crown", "off_mayor"}
    plain = {c.subject for c in formed if not VERB_TABLE[c.verb].referent_class}
    assert set(REVOKE_REFS) <= plain, plain


def test_rem28_e_the_class_keeps_the_only_referents_a_revoke_can_succeed_on_and_removes_the_rest(monkeypatch):
    """A PROOF, NOT A COUNT, for an untyped predicate row whose one clause reads the payload's `office`. THE REMOVED
    Candidates (the person and the hearth, which the classless row forms): the act the chooser mints is refused on
    'names no office', and so is the same act handed the id as its `office` -- a person and a rung are no office, so
    nothing a caller could add makes them succeed, and removing them removes refusals only. THE KEPT Candidates: the
    computed act is refused on the same clause (the limit, below), and handed `office` (the shape a hand-built act
    has, `test_h134_candidate_per_seat._with_office`) exactly ONE is admitted -- the Duke's seat through `off_crown`,
    the seat on the rung above it; the vacant `off_reeve` is refused (a seat nobody holds) and `off_mayor` has no
    authority over the Duke. The loop asserts it checked both removed kinds and all four kept Candidates."""
    w, d, q = _revoker_asked_about_a_person_a_place_and_a_seat(monkeypatch)
    p = w.persons[REVOKER]
    removed = [c for c in _formed_without_class(w, REVOKER, q, "revoke") if c.subject in ("p_low", HEARTH)]
    assert {c.subject for c in removed} == {"p_low", HEARTH} and len(removed) == 4, removed
    for c in removed:
        act = _act_of(c, p)
        out, clauses = _refusal_clauses(lambda: _preds._req_revoke(w, act))
        assert out is False and clauses == [NO_OFFICE_CLAUSE], (c, clauses)
        out, clauses = _refusal_clauses(lambda: _preds._req_revoke(w, _with_office(act)))
        assert out is False and clauses == [NO_OFFICE_CLAUSE], (c, clauses)
    kept = [c for c in _formed(w, REVOKER, q) if c.verb == "revoke"]
    assert len(kept) == 4, kept
    for c in kept:
        out, clauses = _refusal_clauses(lambda: _preds._req_revoke(w, _act_of(c, p)))
        assert out is False and clauses == [NO_OFFICE_CLAUSE], (c, clauses)
    admitted = [(c.subject, seat_of(p, c)) for c in kept if _preds._req_revoke(w, _with_office(_act_of(c, p)))]
    assert admitted == [(REVOKE_TARGET, "off_crown")], admitted


def test_rem28_e_mutation_without_its_column_the_row_forms_on_the_person_and_the_place_too(monkeypatch):
    """THE MUTATION, EXECUTED: the column deleted (the row copied with no class) and the assertion above has
    something to see -- `revoke` forms on all three plain referents, the person and the hearth among them, and on no
    seat the question does not name (`off_reeve` is a classed referent only). The unclassed formation is the base
    reading's: 18 of 18 attempts refused, a person 8, a rung 8, a Record 1, a Site 1 (`aperture 1 s`, s = 0/1/2,
    realm and spine, the dispatch commit `a4c508c5`)."""
    w, _, q = _revoker_asked_about_a_person_a_place_and_a_seat(monkeypatch)
    unclassed = _formed_without_class(w, REVOKER, q, "revoke")
    assert collections.Counter(c.subject for c in unclassed) == {s: 2 for s in REVOKE_REFS}, unclassed
    assert {c.subject for c in _formed(w, REVOKER, q) if c.verb == "revoke"} == {REVOKE_TARGET, "off_reeve"}


def test_rem28_f_the_formation_that_survives_is_still_refused_by_the_fold_and_executes_nothing(monkeypatch):
    """THE STATED LIMIT, EXECUTED (the done test this item does NOT have): the Candidate the question forms on the
    Duke's seat through `off_crown`, minted as the chooser mints it and folded by the real driver, is REFUSED --
    `revoke.refused`, and the Duke's `hold` stays live. THE CONTROL, which says the refusal is the payload's key and
    not the Candidate: the same act carrying `office` closes the hold (`tenure.closed`). When a caller reads
    `subject` (H-207 ruling (A)), THIS is the test to re-scope: the first assertion then becomes the execution."""
    w, d, q = _revoker_asked_about_a_person_a_place_and_a_seat(monkeypatch)
    p = w.persons[REVOKER]
    (kept,) = [c for c in _formed(w, REVOKER, q) if c.verb == "revoke" and c.subject == REVOKE_TARGET
               and seat_of(p, c) == "off_crown"]
    act = _act_of(kept, p)
    run = lambda *acts: [e.kind for e in d.resolve(mint_token(w, WriteClass.ACTS), list(acts),
                                                   contest_max_depth=w.fixtures.get("contest_max_depth"))]
    assert run(act) == ["revoke.refused"] and _hold(w, REVOKE_TARGET) is not None
    with_office = dataclasses.replace(_with_office(act), id="a_rem28_revoke_with_office")
    assert "tenure.closed" in run(with_office) and _hold(w, REVOKE_TARGET) is None


def test_rem28_e_the_class_moves_no_derived_set():
    """`Office` is declared already (`confer`, `oblige`) and `RUNG_REMIT_ACTS` reads the `Rung` rows alone, so the
    column moves neither derived set: both are re-derived over the table with `revoke`'s column blanked and read the
    shipped sets (an INVARIANCE: the fold cannot differ, so this is the whole of what can be asserted). THE CONTROL,
    that the derivation can move: a table with no `Office` row at all (`revoke`, `confer`, `oblige` blanked) loses
    `Office` from `DECLARED_CLASSES`, so neither equality is one a constant could satisfy."""
    classless = lambda *verbs: {**VERB_TABLE, **{v: dataclasses.replace(VERB_TABLE[v], referent_class="")
                                                  for v in verbs}}
    with mock.patch.object(_verbs, "VERB_TABLE", classless("revoke")):
        assert _verbs._derive_rung_remit_acts() == _verbs.RUNG_REMIT_ACTS
        assert _verbs._derive_declared_classes() == _verbs.DECLARED_CLASSES
    with mock.patch.object(_verbs, "VERB_TABLE", classless("revoke", "confer", "oblige")):
        assert "Office" not in _verbs._derive_declared_classes()
    assert _verbs.RUNG_REMIT_ACTS == frozenset({"issue", "dispatch", "convene"}), _verbs.RUNG_REMIT_ACTS
