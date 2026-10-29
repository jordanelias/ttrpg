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
tests for a person and a Proposition. The last section is the batch's control (3), written over the rows
that declare `Site`, `Proposition` or `Person` so a later item adds its row by its column and not by a
copy.

CR-28 (`world_q.propositions_named`, the sixth standing occasion: the Propositions a person's own ledger names and
the goals he is committed to stamp as `Proposition`, so `commit` forms on an `utter` he heard and a goal he holds):
the formation through the real `questions_for`/`opening_set`/fold for each of the two sources, the byte-identity of a
world whose ledgers name no Proposition (and the control that the equality can fail), the bound (his own ledger and
edges, never the store), the dedup beside the question's own referent, the no-motive rule (a goal that names no one is
not offered, IN-67), the gate on the declaration, and the mutation (the term returning `()` reproduces REM-23's reading).
Run at the build: the term's body replaced by `return ()` reddens every `test_cr28_*` first assertion (and the REM-21
`c` pair, REM-22 `a`, REM-23 `a`, `test_in53_vacancy_need` `a` that now see a goal stamped); the term spliced after the
own-referent term reddens the splice-order test and the dedup order test; `questions_for` passing every ambition and not
the ones that formed a question reddens `test_cr28_c_a_goal_that_names_no_one...` and three IN-67 tests.

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
from engine.season.data.rosters import OCCASION_ONLY_CLASSES, REFERENT_CLASSES
from engine.season.data.verbs import DECLARED_CLASSES, VERB_TABLE
from engine.season.decision import options as _options
from engine.season.decision.choose import _payload_of
from engine.season.decision.options import seat_of
from engine.season.gaps import Forbidden
from engine.season.harness import probes as P
from engine.season.loop.driver import mint_token
from engine.season.queries import world_q
from engine.season.state.carriers import Act, Claim, Proposition, Question, Tenure

from .test_g3_not_yours import _gov_world, _hold
from .test_in09_dispensation_answer import HOLDER, WRIT, _with_writ
from .test_in53_vacancy_need import _ambition, _formed, _know, _planted
from .test_works_founding import ABSENT, HARBOUR, PRESENT, SETTLEMENT, _declare, _fold, _kinds, _ripen
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
    classes read in the splice's order -- `vacancies`, `seats_named`, `writs_held`, `places_named`,
    `larders_in_purview`, and (v10 CR-28) `propositions_named` -- and the question's own referent last.
    Swapping any two terms reddens it."""
    w, _ = _with_writ()
    _ambition(w, HOLDER, "prop_a", "site_harbour")
    _proposition(w, "prop_n")
    for name, out in (("vacancies", ("off_duke",)), ("seats_named", ("off_dicastery",)),
                      ("writs_held", (WRIT,)), ("places_named", ("D",)),
                      ("larders_in_purview", ("S",)), ("propositions_named", ("prop_n",))):
        monkeypatch.setattr(world_q, name, lambda *a, _out=out, **k: _out)
    monkeypatch.setattr(world_q, "DECLARED_CLASSES", DECLARED_CLASSES | {"Site"})
    (q,) = world_q.questions_for(w, w.persons[HOLDER])
    assert q.referents == ("site_harbour",), q
    assert q.classes == (("off_duke", "Office"), ("off_dicastery", "Office"), (WRIT, "Record"),
                         ("D", "Rung"), ("S", "Rung"), ("prop_n", "Proposition"),
                         ("site_harbour", "Site")), q


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
    # v10 CR-28: and the goal he holds (`prop_a`) rides after them, as a `Proposition`.
    assert q.classes == (("D", "Rung"), ("S", "Rung"), ("prop_a", "Proposition")), q


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
    # v10 CR-28: the Offices are exactly the vacancies, each once; the goal he holds follows them.
    assert q.referents == ("off_reeve",) and q.classes == tuple((o, "Office") for o in vac) + (
        ("prop_a", "Proposition"),), q


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


def _goal_of(pid):
    """The id of the one goal `_ask` plants for `pid`, whose `need` question is the one he answers."""
    return f"prop_ask_{pid}"


def _ask(monkeypatch, w, pid, refs=MIXED):
    """The question `pid` answers when his one ambition is about `refs`, delivered through the real
    `questions_for` (the splice, the term, `_stamped`). `goal_referents` is the one owner of what an
    ambition is about and ships no producer of a person AND a place in one question, so it is stood
    in for HERE, once, for this ambition alone; the question is otherwise the producer's."""
    prop = _goal_of(pid)
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
    # REM-23: the question's Proposition (`prop_x`) now stamps too, as `commit` declares its class; the
    # Site is the same one, first in the question's order, and this verb's formation is unchanged by it.
    # v10 CR-28: and the goal he is answering (`_goal_of`), a standing occasion, ahead of both.
    assert q.classes == ((_goal_of(PRESENT), "Proposition"), ("site_harbour", "Site"),
                         ("prop_x", "Proposition")), q
    formed = _formed(w, PRESENT, q)
    assert [c.subject for c in formed if c.verb == verb] == ["site_harbour"], (verb, formed)
    plain = {c.subject for c in formed if not VERB_TABLE[c.verb].referent_class}
    assert set(MIXED) <= plain, plain


def test_rem22_a_every_candidate_respects_the_partition_a_classed_row_the_class_a_plain_row_the_plain(
        monkeypatch):
    """Over everything `p_high` forms from the mixed question: a row declaring a class forms only on an
    id the question carries as that class, a row declaring none only on its plain referents -- and the
    loop asserts it compared (`CLAUDE.md` §0.1 pt 2): the three Site rows and REM-23's `commit` among the
    classed, and the plain rows on all four referents."""
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
    both = SITE_ROWS + PROPOSITION_ROWS
    # v10 CR-28: once per id the question carries as the row's class -- the one harbour for the Site rows,
    # and for `commit` the Proposition the question names AND the goal he holds -- which is the property
    # the count of 1 stood for.
    assert set(both) <= set(classed), classed
    assert all(classed[v] == sum(k == VERB_TABLE[v].referent_class for _, k in q.classes) for v in both), (
        classed, q.classes)
    assert [classed[v] for v in SITE_ROWS] == [1] * len(SITE_ROWS), classed
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
    # v10 CR-28: the Propositions are the question's own (`prop_x`) and the goal he holds (`_goal_of`); the
    # person, the harbour and the rung are still not formed on -- the class removes the wrong kinds only.
    assert [c.subject for c in formed if c.verb == verb] == [_goal_of(PRESENT), "prop_x"], (verb, formed)
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
    assert [c.subject for c in _formed(w, PRESENT, q) if c.verb == verb] == [_goal_of(PRESENT), "prop_x"]


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
    (c,) = [c for c in _formed(w, PRESENT, q) if c.verb == "commit" and c.subject == "prop_x"]

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
# CR-28 (B10-05; register G-04 (a), H-156 option (b)): THE PROPOSITIONS A PERSON'S OWN STATE NAMES STAMP AS
# `Proposition`, SO `commit` FORMS ON AN `utter` HE HEARD AND A GOAL HE HOLDS -- not only on a Proposition
# the question he answers happens to name (REM-23's reading: `commit` formed for 6/2/1 persons at
# `aperture 1 s`, and on no goal). ONE standing occasion beside `seats_named` and `writs_held`
# (`world_q.propositions_named`), composed on REM-21's one stamp site and its dedup; no registry.
# ======================================================================================

SPEAKER, HEARER, STRANGER = "p_low", "p_mid", "p_high"    # the first two share the hearth `Hh`; `p_high` is at `S`


def _heard_utter(w, d, key="u1"):
    """The real `utter` by SPEAKER, folded, and the real WITNESS pass over it: the hearth's ledgers (the
    hearer's, not the stranger's at `S`) hold the `proposition.uttered` claim about the new Proposition.
    Returns its id."""
    out = _fold(w, d, Act(id=key, actor=SPEAKER, verb="utter"))
    assert _kinds(out) == ["proposition.uttered"], _kinds(out)
    d.witness(mint_token(w, WriteClass.INTERIOR), out)
    return f"prop:{key}"


def _commits_on(w, pid):
    """`(the subjects `commit` forms on, the delivered question)` for `pid`: the real `questions_for`, the
    first question (the `first` rule delivers it), the real `opening_set`. `([], None)` when no question."""
    qs = world_q.questions_for(w, w.persons[pid])
    if not qs:
        return [], None
    return [c.subject for c in _formed(w, pid, qs[0]) if c.verb == "commit"], qs[0]


def _live_commits(w, pid):
    return sorted(t.object for t in w.persons[pid].tenures if t.kind == "commit" and t.live)


def test_cr28_a_a_person_who_heard_an_utter_forms_commit_on_its_proposition():
    """THE FIRST ASSERTION, which the term returning `()` reddens (`test_cr28_mutation_...` runs that, and the
    build ran it against the source): `p_mid` heard `p_low` utter. The question he answers is a claim landing,
    about the speaker -- a person, which REM-23's class keeps `commit` off -- and the term carries the
    Proposition his ledger names beside it, so `commit` forms on that Proposition and on nothing else, and the
    fold executes it. THE CONTROLS: the plain rows still form on the speaker (the stamp added a formation and
    took none); `p_high` at `S` heard nothing, holds no goal, and is offered nothing."""
    w, d = _works_world()
    prop = _heard_utter(w, d)
    hearer = w.persons[HEARER]
    assert {c.predicate for c in hearer.ledger if c.subject == prop} >= {"proposition.uttered"}
    assert not [c for c in w.persons[STRANGER].ledger if c.subject == prop]
    on, q = _commits_on(w, HEARER)
    assert q.referents == (SPEAKER,) and q.classes == ((prop, "Proposition"),), q
    assert on == [prop], on
    formed = _formed(w, HEARER, q)
    assert SPEAKER in {c.subject for c in formed if not VERB_TABLE[c.verb].referent_class}, formed
    assert _commits_on(w, STRANGER) == ([], None)
    (c,) = [c for c in formed if c.verb == "commit"]
    assert prop not in _live_commits(w, HEARER)
    assert _kinds(_fold(w, d, _act_of(c, hearer))) == ["commitment.made"]
    assert _live_commits(w, HEARER) == [prop]


def test_cr28_a_a_person_committed_to_a_goal_forms_commit_on_it_and_it_executes_once_more():
    """`p_mid` holds a goal about the harbour (an OUGHT Proposition he is committed to). His `need` question's
    referent is the Site -- the goal itself was never among the referents a question carries (REM-23's note) --
    and the term carries the goal beside it: `commit` forms on the goal and on nothing else, and the fold
    opens a second live edge to it. THE CONTROL: `ambitions`, the one owner of what a goal is, still reads
    ONE ambition (two live edges to one Proposition are one ambition), so the term did not make a second."""
    w, d = _works_world()
    _ambition(w, HEARER, "prop_goal", HARBOUR)
    hearer = w.persons[HEARER]
    on, q = _commits_on(w, HEARER)
    assert (q.id, q.referents) == ("q:need:prop_goal", (HARBOUR,)), q
    assert q.classes == (("prop_goal", "Proposition"), (HARBOUR, "Site")), q
    assert on == ["prop_goal"], on
    (c,) = [c for c in _formed(w, HEARER, q) if c.verb == "commit"]
    assert _live_commits(w, HEARER) == ["prop_goal"] and world_q.ambitions(w, hearer) == ["prop_goal"]
    assert _kinds(_fold(w, d, _act_of(c, hearer))) == ["commitment.made"]
    assert _live_commits(w, HEARER) == ["prop_goal", "prop_goal"], _live_commits(w, HEARER)
    assert world_q.ambitions(w, hearer) == ["prop_goal"]


def test_cr28_b_a_world_whose_ledgers_name_no_proposition_is_byte_identical(monkeypatch):
    """THE BYTE-IDENTITY CONTROL: with no ledger naming a Proposition and nobody holding a goal, every person's
    questions equal, field for field and in `repr`, what `questions_for` returns with the term stubbed to
    `()`. Everyone knows everyone (so there are questions to compare) and `off_duke2` is vacant (so
    `p_king`'s question carries a standing occasion's stamp and `_stamped` runs). THE CONTROL OF THE CONTROL:
    one ledger gains a claim naming a Proposition and exactly that person's questions differ."""
    w, _ = _gov_world()
    _hold(w, "off_duke2").until = w.tick
    ids = sorted(w.persons)
    for pid in ids:
        _know(w, pid, *[o for o in ids if o != pid])
    assert not [c for p in w.persons.values() for c in p.ledger if c.subject in w.propositions]
    real = {pid: world_q.questions_for(w, p) for pid, p in w.persons.items()}
    assert sum(bool(qs) for qs in real.values()) >= 4 and any(qs[0].classes for qs in real.values() if qs), real
    monkeypatch.setattr(world_q, "propositions_named", lambda *a, **k: ())
    stub = {pid: world_q.questions_for(w, p) for pid, p in w.persons.items()}
    assert real == stub and repr(real) == repr(stub)
    monkeypatch.undo()
    _proposition(w, "prop_x")
    w.persons[HEARER].ledger.append(Claim("c_named", HEARER, "prop_x", "proposition.uttered", True, 0,
                                          "firsthand", 100, "own"))
    named = {pid: world_q.questions_for(w, p) for pid, p in w.persons.items()}
    assert [pid for pid in ids if named[pid] != real[pid]] == [HEARER], named
    assert ("prop_x", "Proposition") in named[HEARER][0].classes


def test_cr28_c_a_person_is_offered_the_propositions_he_names_and_holds_and_no_others():
    """THE BOUND, the precedents' (`seats_named` reads his ledger, `writs_held` his edges; neither reads the
    store): the world holds twelve Propositions, `p_mid`'s ledger names three, he holds one OUGHT goal and is
    committed to one HOLDS creed, and a neighbour heard a fourth. He is offered exactly the three he heard and
    the goal -- not the other eight, not the neighbour's, not a creed that is no goal (`ambitions` reads an OUGHT
    only) -- and `commit` forms on exactly those four."""
    w, _ = _works_world()
    for i in range(12):
        _proposition(w, f"prop_w{i:02d}")
    heard = ("prop_w03", "prop_w07", "prop_w10")
    for i, prop in enumerate(heard):
        w.persons[HEARER].ledger.append(Claim(f"c_heard{i}", HEARER, prop, "proposition.uttered", True, 0,
                                              "firsthand", 100, "own"))
    w.persons[SPEAKER].ledger.append(Claim("c_other", SPEAKER, "prop_w05", "proposition.uttered", True, 0,
                                           "firsthand", 100, "own"))
    w.propositions["prop_creed"] = Proposition("prop_creed", "HOLDS", "S", "prop_creed holds", True, 0)
    w.add_tenure(Tenure("tc_creed", HEARER, "prop_creed", "commit", since=0))
    _ambition(w, HEARER, "prop_goal", HARBOUR)
    p = w.persons[HEARER]
    assert world_q.ambitions(w, p) == ["prop_goal"] and len(w.propositions) >= 14
    want = tuple(sorted(heard + ("prop_goal",)))
    assert world_q.propositions_named(w, p) == want
    on, q = _commits_on(w, HEARER)
    assert q.classes[:len(want)] == tuple((x, "Proposition") for x in want), q
    assert sorted(on) == list(want) and len(on) == 4, on
    assert world_q.propositions_named(w, w.persons[SPEAKER]) == ("prop_w05",)


def test_cr28_c_a_proposition_named_and_the_questions_own_referent_is_carried_once():
    """The dedup (REM-21's `_stamped`, the one stamp site): a goal about itself (`prop_b`) is both the
    question's own plain referent (`own_referents_of_class`) and the Proposition he holds
    (`propositions_named`), and he has heard a second (`prop_a`, sorting first). The question carries each pair
    once, in the standing occasion's order and ahead of the own-referent term -- `Question` refuses a pair
    carried twice, so the bare concatenation reddens it, and the own-referent term first would put `prop_b`
    ahead."""
    w, _ = _works_world()
    _proposition(w, "prop_a")
    w.persons[HEARER].ledger.append(Claim("c_heard", HEARER, "prop_a", "proposition.uttered", True, 0,
                                          "firsthand", 100, "own"))
    _ambition(w, HEARER, "prop_b", "prop_b")
    (q,) = world_q.questions_for(w, w.persons[HEARER])
    assert q.referents == ("prop_b",) and q.classes == (("prop_a", "Proposition"),
                                                        ("prop_b", "Proposition")), q


def test_cr28_c_a_goal_that_names_no_one_is_no_motive_and_is_not_offered(monkeypatch):
    """IN-67's rule (*"an OUGHT about nobody is not a motive"*, `goal_referents` reading `()` forms no question) holds
    for the stamp too: offering such a goal would carry it onto a `need` question the rule refuses (`questions_for`
    creates one for a person who has a stamp and no question). `p_mid` holds only a goal `goal_referents` names
    no one for: no question, nothing offered, and `commit` forms nowhere. THE CONTROL: with a second goal that
    does name someone, he is offered that goal and not the first. (The mutation, offering every ambition, reddens the
    first assertion; `test_in67_goal_referents.py` holds the same rule at the question.)"""
    w, _ = _works_world()
    real = world_q.goal_referents
    monkeypatch.setattr(world_q, "goal_referents",
                        lambda w_, p_, pr: () if pr.id == "prop_nobody" else real(w_, p_, pr))
    _ambition(w, HEARER, "prop_nobody", HARBOUR)
    p = w.persons[HEARER]
    assert world_q.ambitions(w, p) == ["prop_nobody"]
    assert world_q.propositions_named(w, p) == () and world_q.questions_for(w, p) == []
    _ambition(w, HEARER, "prop_goal", HARBOUR)
    assert world_q.propositions_named(w, p) == ("prop_goal",)
    on, q = _commits_on(w, HEARER)
    assert q.classes[0] == ("prop_goal", "Proposition") and on == ["prop_goal"], (q, on)
    assert "prop_nobody" not in {r for r, _ in q.classes}, q


def test_cr28_d_the_term_is_gated_on_the_declaration(monkeypatch):
    """`larders_in_purview`' and `writs_held`' way: while no verb row declares `Proposition` the term names
    nothing and the question carries no class, so dropping `commit`'s column (M19's per-row revert) leaves
    nothing stamped for nobody to read. THE CONTROL: declared, the same ledger stamps it."""
    w, d = _works_world()
    prop = _heard_utter(w, d)
    hearer = w.persons[HEARER]
    assert world_q.propositions_named(w, hearer) == (prop,)
    monkeypatch.setattr(world_q, "DECLARED_CLASSES", DECLARED_CLASSES - {"Proposition"})
    assert world_q.propositions_named(w, hearer) == ()
    assert [q.classes for q in world_q.questions_for(w, hearer)] == [()]


def test_cr28_mutation_without_the_term_commit_forms_as_it_did_at_rem23(monkeypatch):
    """THE MUTATION, EXECUTED: the term returning `()` and `commit` forms on neither the `utter` he heard nor
    the goal he holds -- REM-23's reading, where it formed only on a Proposition the question itself named --
    so the first assertions of the two tests above have something to see."""
    w, d = _works_world()
    prop = _heard_utter(w, d)
    _ambition(w, STRANGER, "prop_goal", HARBOUR)
    with_term = (_commits_on(w, HEARER)[0], _commits_on(w, STRANGER)[0])
    assert with_term == ([prop], ["prop_goal"]), with_term
    monkeypatch.setattr(world_q, "propositions_named", lambda *a, **k: ())
    assert (_commits_on(w, HEARER)[0], _commits_on(w, STRANGER)[0]) == ([], [])


# --- (c) CONTROL (3) OF B10-05's HR-9: A CLASS REMOVES REFUSALS AND NOTHING ELSE --------------

#: The classes whose rows control (3) walks. The ROWS are read off the table, so a later item that
#: declares `Proposition` or `Person` on a row is under the control the moment its column lands: nothing
#: here names a verb but `SITE_ROWS` and `PROPOSITION_ROWS` (the rows whose extra assertions are stated),
#: and a row is added by its data and never by a copy.
CONTROL3_CLASSES = frozenset({"Site", "Proposition", "Person"})


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
    a class that removed it would be removing a refusal that was not about kind."""
    kinds = _existence_kinds(row.requires_typed.requirement) if row.requires_typed is not None else frozenset()
    if kinds:
        assert any(o.predicate == f"exists:{k}" and o.value in (0, False)
                   for k in kinds for o in verdict.observed), (row.verb, c, verdict)
    else:
        assert verdict.value is UNKNOWN and any(o.value is UNKNOWN for o in verdict.observed), (
            row.verb, c, verdict)


def test_rem22_c_every_candidate_a_class_removes_force_admitted_refuses_on_the_rows_kind(monkeypatch):
    """HR-9 CONTROL (3), for every row declaring `Site`, `Proposition` or `Person`: the Candidates its
    class removes -- those the row would form on the question's referents of any other class were it
    classless -- are force-admitted through the fold's own `_admits` (the Candidate minted as the chooser
    mints it) and each is refused on the row's kind. A PROOF, NOT A COUNT: the class removes refusals and
    nothing else. The loop asserts that it checked at least one removed Candidate for EVERY classed row,
    and the Site rows' and the Proposition row's own Candidate (the one the class keeps) is admitted by the
    same call, so a refusal here is not the fold refusing everything. REM-23's `commit` entered this loop
    by its column alone: `rows` is read off the table."""
    w, d = _works_world()
    q = _ask(monkeypatch, w, PRESENT)
    p = w.persons[PRESENT]
    rows = {v: r for v, r in VERB_TABLE.items() if r.referent_class in CONTROL3_CLASSES}
    assert set(SITE_ROWS + PROPOSITION_ROWS) <= set(rows), sorted(rows)
    kept = {c.verb: c for c in _formed(w, PRESENT, q)}
    checked = collections.Counter()
    for verb, row in sorted(rows.items()):
        own = {r for r, k in q.classes if k == row.referent_class}
        removed = [c for c in _formed_without_class(w, PRESENT, q, verb) if c.subject not in own]
        for c in removed:
            ok, _kinds_, verdict = d._admits(w, _act_of(c, p), row)
            assert not ok, (verb, c)
            _refuses_on_the_rows_kind(row, verdict, c)
            checked[verb] += 1
        if verb in SITE_ROWS + PROPOSITION_ROWS:
            assert {c.subject for c in removed} == set(MIXED) - own, (verb, removed)
            assert d._admits(w, _act_of(kept[verb], p), row)[0], (verb, kept[verb])
    assert set(checked) == set(rows) and min(checked.values()) >= 1, (sorted(rows), checked)
