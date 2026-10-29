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
through the real fold, and the cost the shared class creates (measured, pinned). The last section is the
batch's control (3), written over the rows
that declare `Site`, `Proposition` or `Person`, and the `Record` rows whose cell asks the actor to hold
the subject, so a later item adds its row by its column and not by a copy.

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
from engine.season.data.requires import UNKNOWN, AllOf, Existence
from engine.season.data.rosters import OCCASION_ONLY_CLASSES, REFERENT_CLASSES
from engine.season.data.verbs import DECLARED_CLASSES, HOLDING_RECORD_KINDS, RECORD_REFERENT_KINDS, VERB_TABLE
from engine.season.decision import options as _options
from engine.season.decision.choose import _payload_of
from engine.season.decision.options import seat_of
from engine.season.gaps import Forbidden
from engine.season.harness import probes as P
from engine.season.queries import world_q
from engine.season.state.carriers import Act, Claim, Proposition, Question, Record, Tenure

from .test_g3_not_yours import _gov_world, _hold
from .test_in09_dispensation_answer import HOLDER, WRIT, _with_writ
from .test_in53_vacancy_need import _ambition, _formed, _know, _planted
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
    monkeypatch.setattr(world_q, "own_referents_of_class", lambda w, q, classes: ())
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
    its rows' cells. THE ANTI-VACUITY: both sets are non-empty and the holding rows are the three columns."""
    rows = {v: r for v, r in VERB_TABLE.items() if r.referent_class == "Record"}
    holding = {v for v, r in rows.items() if _verbs._asks_subject_held(r)}
    assert holding == set(HOLDING_ROWS) and set(rows) - holding == {"comply"}, (sorted(rows), sorted(holding))
    kinds = lambda vs: frozenset().union(*(_existence_kinds(rows[v].requires_typed.requirement) for v in vs))
    assert HOLDING_RECORD_KINDS == kinds(holding) == HOLDING_KINDS
    assert RECORD_REFERENT_KINDS == kinds(set(rows) - holding) == {"dispensation"}
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


# --- (c) CONTROL (3) OF B10-05's HR-9: A CLASS REMOVES REFUSALS AND NOTHING ELSE --------------

#: The classes whose rows control (3) walks. The ROWS are read off the table, so a later item that
#: declares `Proposition` or `Person` on a row is under the control the moment its column lands: nothing
#: here names a verb but `SITE_ROWS`, `PROPOSITION_ROWS` and `PERSON_ROWS` (the rows whose extra
#: assertions are stated), and a row is added by its data and never by a copy.
CONTROL3_CLASSES = frozenset({"Site", "Proposition", "Person"})


def _control3_rows() -> dict:
    """The classed rows control (3) walks: every row declaring one of `CONTROL3_CLASSES`, plus (v10 REM-25)
    the `Record` rows whose cell asks the actor to HOLD the subject -- read off the cell, not a verb name.
    `comply`, the other `Record` row, forms on a writ its own ledger names (`referent_named`) and keeps its
    addressee test; it is held to `test_in09_dispensation_answer.py`'s formation tests."""
    return {v: r for v, r in VERB_TABLE.items()
            if r.referent_class in CONTROL3_CLASSES
            or (r.referent_class == "Record" and _verbs._asks_subject_held(r))}


def _existence_kinds(req) -> frozenset:
    """The `kind` of every `existence` clause in a typed cell (`AllOf` nested or not)."""
    if isinstance(req, Existence):
        return frozenset({req.kind})
    if isinstance(req, AllOf):
        return frozenset().union(*(_existence_kinds(x) for x in req.clauses))
    return frozenset()


def _refuses_on_the_rows_kind(row, verdict, c):
    """The refusal is the row's own kind test: where the cell asks `existence` of a kind, an
    `exists:<kind>` read came back 0; where it asks none (`work`'s threshold), the read of the referent
    came back UNKNOWN and the verdict is not True. Anything else is a refusal for another reason, and
    a class that removed it would be removing a refusal that was not about kind. A cell asking several
    kinds (REM-24's `petition`: its person AND the rung it rises from) is held to the one the class
    names, so a formation refused only on its OTHER side would not pass for a wrong-kind one."""
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
    asserts exactly those on a Record of the row's own kind are admitted, and that there is at least one."""
    w, d = _works_world()
    pet = _file_petition(w, d)
    _declare(w, d, "wk_c3", "hearth", SETTLEMENT, actor=PRESENT)
    q = _ask(monkeypatch, w, PRESENT)
    p = w.persons[PRESENT]
    rows = _control3_rows()
    assert set(SITE_ROWS + PROPOSITION_ROWS + PERSON_ROWS + HOLDING_ROWS) <= set(rows), sorted(rows)
    formed = _formed(w, PRESENT, q)
    kept = {c.verb: c for c in formed}
    checked = collections.Counter()
    for verb, row in sorted(rows.items()):
        own = {r for r, k in q.classes if k == row.referent_class}
        removed = [c for c in _formed_without_class(w, PRESENT, q, verb) if c.subject not in own]
        for c in removed:
            ok, _kinds_, verdict = d._admits(w, _act_of(c, p), row)
            assert not ok, (verb, c)
            _refuses_on_the_rows_kind(row, verdict, c)
            checked[verb] += 1
        if verb in SITE_ROWS + PROPOSITION_ROWS + PERSON_ROWS:
            assert {c.subject for c in removed} == set(MIXED) - own, (verb, removed)
            assert d._admits(w, _act_of(kept[verb], p), row)[0], (verb, kept[verb])
        if row.referent_class == "Record":
            mine = [c for c in formed if c.verb == verb]
            assert own == {pet, "wk_c3"} and {c.subject for c in mine} == own, (verb, own, mine)
            kinds = _existence_kinds(row.requires_typed.requirement)
            admitted = {c.subject for c in mine if d._admits(w, _act_of(c, p), row)[0]}
            assert admitted == {r for r in own if w.records[r].kind in kinds} and admitted, (verb, admitted)
            assert {c.subject for c in removed} == set(MIXED), (verb, removed)
    assert set(checked) == set(rows) and min(checked.values()) >= 1, (sorted(rows), checked)
