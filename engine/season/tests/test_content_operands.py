"""Plan position `15c` -- CONTENT OPERANDS. r2 `01_ATTENTION_AND_REACH.md` §A.5.3/§A.5.4 (Q2's
clause 3) and `02_THE_WRIT_AND_THE_WORD.md` §A.13 (`_derive_operand` reading a held writ). GATE:
`15`, `16` -- the Record-kind fold and `give`, both landed, are what give clause 3 and the
operand reader a producer: a `content:<kind>` claim now carries the Record's real
`subject_matter`, frozen, instead of `True`.

What each block proves, and the control that stops it passing vacuously:

  1. `named(c)` -- the CLAUSE 3 READER. Reads the addressee id set off a `content:<kind>` claim's
     value, through `record_kinds`'s own `addressee` key, never off the value's strings. `()` for
     a non-`content:` claim, a `None` value, or a kind with no addressee key.
  2. THE FALSIFIER (r2 `01` AR-5, `05:1247`). A `content:dispensation` claim naming a person, that
     person holds nothing and is nowhere near the rung, is ASKED (Q2 clause 3). Control: the same
     claim, same world, held by a person the writ does NOT name -- not asked.
  3. `_from_content_claim` -- THE OPERAND READER. `to` resolves off a held/witnessed writ, ahead of
     the referent copy and the fixture; `kind`/`amount` decline every time today, because neither
     live schema (`dispensation`, `petition`) carries either key, and fall through to the
     UNCHANGED fixture/referent behaviour. `from` is never asked (r2's own ruling: the writ may not
     name where the actor stands), and `at` is never asked either -- it is not, and must not
     become, a `requires_operands` member, so `_derive_operand` is never called with that name.
  4. THE SINGLETON RULE, FOUND BY RUNNING THE POPULATED CORPUS (`CLAUDE.md` §0.1 pt 3). A writ's
     addressee key is a LIST; every operand this vocabulary carries is a SCALAR. Exactly one
     addressee collapses to that id; more than one, or none, declines -- naming which of several a
     scalar operand means is a choice nobody has ruled, on `floor`'s own precedent.
  5. THE OBSERVABLE (r2 `05:1247`): `Candidates with writ-derived operands > 0`, measured on the
     real populated corpus, not a hand-built fixture -- and every one of them resolves to a real,
     live entity, not a value the fold can only ever refuse.
  6. NOTHING WIDENS THAT DID NOT NEED TO. `requires_operands` stays at eight names (`at` does not
     join it -- r2's own ruling, *"I do not coin a ninth operand"*); `question_sources` stays at
     two (clause 3 is not a fourth source -- r2 §A.5.4, *"one `Question` shape, one `source`
     string"*). Both are regression guards on a design choice this position made, not a fact this
     position discovered.
"""

from __future__ import annotations

import pytest

from ..data.requires import REQUIRES_OPERANDS, WRIT_SOURCED_OPERANDS, _check_writ_sourced_subset
from ..data.rosters import QUESTION_SOURCES, RECORD_CONTENT, RECORD_KIND_KEYS
from ..data.verbs import VERB_TABLE
from ..decision.options import _derive_operand, _from_content_claim, opening_set
from ..gaps import Forbidden, Unspecified
from ..harness import populated
from ..harness import probes as P
from ..loop.witness import content_value
from ..queries.world_q import named, questions_for
from ..state.carriers import Claim, Question, Record, Tenure, View

_CONTENT = RECORD_CONTENT["predicate"]


def _content_claim(cid, holder, rec_id, kind, subject_matter, when=0):
    return Claim(cid, holder, rec_id, f"{_CONTENT}:{kind}", content_value(subject_matter),
                 when, "firsthand", 100, "own")


# ======================================================================================
# 1 -- `named(c)`: THE CLAUSE 3 READER
# ======================================================================================

def test_named_reads_the_addressee_key_record_kinds_declares():
    sm = {"terms": "prop_x", "to": ["p_a", "p_b"], "at": None}
    c = _content_claim("c1", "holder", "rec1", "dispensation", sm)
    assert named(c) == ("p_a", "p_b")


def test_named_is_empty_for_a_non_content_claim_a_none_value_and_a_bare_predicate():
    ordinary = Claim("c2", "holder", "p_x", "office", "duke", 0, "told_by", 100, "own")
    assert named(ordinary) == ()
    bare = Claim("c3", "holder", "p_x", _CONTENT, True, 0, "firsthand", 100, "own")
    assert named(bare) == (), "a predicate that is `content` with no `:kind` names nobody"
    none_valued = Claim("c4", "holder", "rec1", f"{_CONTENT}:text", None, 0, "firsthand", 100,
                        "own")
    assert named(none_valued) == ()


def test_named_is_empty_for_a_kind_with_no_addressee_key():
    # `text` carries no `to` key at all (`record_kinds`); a generic reader must not invent one.
    c = _content_claim("c5", "holder", "rec1", "text", {})
    assert named(c) == ()


# ======================================================================================
# 2 -- THE FALSIFIER (AR-5): NAMED, AND ONLY NAMED
# ======================================================================================

def test_ar5_a_writ_names_you_into_a_question_and_the_control_does_not():
    w = P.tiny_world()
    named_person = w.persons["p_low"]
    other = w.persons["p_other"]
    sm = {"terms": "prop_x", "to": ["p_low"], "at": None}
    # `rec:elsewhere` is not in `w.records`, `w.persons`, `w.sites`, `w.dates` or `w.rungs` --
    # `place_of` returns `None` for it and clause 2 cannot fire; it is also not in either
    # person's `reach()`, so clause 1 cannot fire either. Only clause 3 can admit this claim.
    claim = _content_claim("c_writ", named_person.id, "rec:elsewhere", "dispensation", sm)
    named_person.ledger.append(claim)
    qs = questions_for(w, named_person)
    assert any(q.about == claim.id for q in qs), (
        f"clause 3 did not admit a claim naming {named_person.id!r}: {[q.about for q in qs]}")

    # CONTROL: the identical claim, same world, held by a person the writ does NOT name.
    control_claim = _content_claim("c_writ2", other.id, "rec:elsewhere", "dispensation", sm)
    other.ledger.append(control_claim)
    qs2 = questions_for(w, other)
    assert not any(q.about == control_claim.id for q in qs2), (
        f"a person NOT named in the writ was asked about it: {[q.about for q in qs2]}")


def test_named_alone_is_not_enough_without_reach_of_the_addressee_id_itself():
    """Clause 3 is `any(x in R for x in named(c))` -- it is the ADDRESSEE's presence in the
    READER's OWN reach that admits, not membership in the writ alone. A person who reads their
    OWN id off the writ always has it in their own `reach()` (`{p.id}` is its first member), so
    this is the same fact as the falsifier above, checked from the reach side instead."""
    w = P.tiny_world()
    p = w.persons["p_mid"]
    from ..queries.world_q import reach
    R = reach(w, p)
    assert p.id in R, "a person's own reach always contains their own id -- clause 3 rests on it"


# ======================================================================================
# 3 -- `_from_content_claim` / `_derive_operand`: THE OPERAND READER
# ======================================================================================

def _held_writ_question(w, p, kind, sm, rec_id="rec_writ"):
    rec = Record(rec_id, "S", kind, subject_matter=sm)
    w.records[rec.id] = rec
    w.add_tenure(Tenure(f"t_{rec_id}", p.id, rec.id, "hold", since=0))
    claim = _content_claim(f"c_{rec_id}", p.id, rec.id, kind, sm)
    p.ledger.append(claim)
    return rec, Question(f"q:claim:{claim.id}", "claim_landed", (rec.id,), claim.id)


def test_to_is_read_off_a_held_dispensation_ahead_of_the_referent():
    w = P.tiny_world()
    p = w.persons["p_low"]
    sm = {"terms": "prop_x", "to": ["p_mid"], "at": "S"}
    rec, q = _held_writ_question(w, p, "dispensation", sm)
    assert _from_content_claim(p, q, "to") == "p_mid"
    assert _derive_operand(p, "to", q, rec.id, w.fixtures) == "p_mid", (
        "the writ must answer before the referent-copy branch (`return subject`)")


def test_to_is_read_off_a_held_petition_too():
    w = P.tiny_world()
    p = w.persons["p_mid"]
    sm = {"terms": "prop_x", "to": ["p_low"], "from": "Hh"}
    rec, q = _held_writ_question(w, p, "petition", sm)
    assert _from_content_claim(p, q, "to") == "p_low"


def test_kind_and_amount_decline_today_and_fall_back_unchanged():
    """Neither live schema carries `kind` or `amount` (`RECORD_KIND_KEYS`), so the writ answers
    `None` for both and the caller's PRE-EXISTING fallback runs -- unchanged from before this
    position, which this pins."""
    w = P.tiny_world()
    p = w.persons["p_low"]
    sm = {"terms": "prop_x", "to": ["p_mid"], "at": "S"}
    rec, q = _held_writ_question(w, p, "dispensation", sm)
    assert "kind" not in RECORD_KIND_KEYS["dispensation"]
    assert "amount" not in RECORD_KIND_KEYS["dispensation"]
    assert _from_content_claim(p, q, "kind") is None
    assert _from_content_claim(p, q, "amount") is None
    assert (_derive_operand(p, "kind", q, rec.id, w.fixtures)
            == w.fixtures.get("default_store_kind"))
    assert (_derive_operand(p, "amount", q, rec.id, w.fixtures)
            == w.fixtures.get("default_transfer_amount"))


def test_from_is_never_read_off_the_writ_even_though_petition_declares_one():
    """r2's own ruling: `from` stays `containing_rung_of(p)` -- a writ that could name it would
    let a Duke's document reach into a larder the executor is not standing in. `petition`'s own
    schema DOES carry a `from` key (r2 `02_THE_WRIT_AND_THE_WORD.md` §A.5); the point of this test
    is that `_derive_operand` never asks `_from_content_claim` for it regardless."""
    w = P.tiny_world()
    p = w.persons["p_mid"]
    sm = {"terms": "prop_x", "to": ["p_low"], "from": "D"}   # a rung the actor is NOT standing in
    rec, q = _held_writ_question(w, p, "petition", sm)
    # The writ's own `from` key resolves fine through the generic reader...
    assert _from_content_claim(p, q, "from") == "D"
    # ...but `_derive_operand` never reaches it for that name: the actor's OWN containing rung
    # answers instead, which for `p_mid` in `tiny_world` is `Hh`, not the writ's `D`.
    assert _derive_operand(p, "from", q, rec.id, w.fixtures) == "Hh"


def test_at_is_not_a_requires_operands_member_and_derive_operand_is_never_asked_for_it():
    assert "at" not in REQUIRES_OPERANDS
    # A COUNT PIN, NOT THE ROSTER'S CONTENT RESTATED -- BATCH-CLOSE FINDING (methodology-close
    # Phase 1, CODE ARCHITECTURE lens): the prior version spelled all eight names out again,
    # which `test_jordan_no_definition_is_hardcoded_in_a_body` catches in the corpus as "the same
    # closed set written out again". The closure's actual content is `rosters.yaml:
    # requires_operands`'s own job to declare; this test's job is only to catch it growing (or
    # shrinking) without `at` in particular joining it, which the length plus the membership
    # check above both do without a second copy of the names.
    assert len(REQUIRES_OPERANDS) == 8, (
        "the eight-name closure moved -- `at` joining it is a ruling this position did not make")
    # No typed cell can ever declare `at`, so `operands_for` can never pass it to
    # `_derive_operand`; the function itself still declines it if asked directly, honestly --
    # there is no branch, and an operand with no branch declines (`ID-13`).
    w = P.tiny_world()
    p = w.persons["p_low"]
    sm = {"terms": "prop_x", "to": ["p_mid"], "at": "S"}
    rec, q = _held_writ_question(w, p, "dispensation", sm)
    assert _derive_operand(p, "at", q, rec.id, w.fixtures) is None


# ======================================================================================
# 4 -- THE SINGLETON RULE
# ======================================================================================

def test_two_addressees_decline_rather_than_guess_which_one():
    w = P.tiny_world()
    p = w.persons["p_low"]
    sm = {"terms": "prop_x", "to": ["p_mid", "p_other"], "at": "S"}
    rec, q = _held_writ_question(w, p, "dispensation", sm)
    assert _from_content_claim(p, q, "to") is None, (
        "two addressees must not silently pick one -- that is a choice nobody has ruled")


def test_zero_addressees_decline():
    w = P.tiny_world()
    p = w.persons["p_low"]
    sm = {"terms": "prop_x", "to": [], "at": "S"}
    rec, q = _held_writ_question(w, p, "dispensation", sm)
    assert _from_content_claim(p, q, "to") is None


# ======================================================================================
# 5 -- THE OBSERVABLE, ON THE REAL POPULATED CORPUS
# ======================================================================================

def test_the_populated_corpus_forms_candidates_with_writ_derived_operands():
    """r2 `05:1247`'s OBSERVABLE: `probes` on the corpus, `Candidates with writ-derived operands
    > 0`. Measured directly rather than trusted: every naturally-occurring `content:` holder's
    candidate set is walked, and the count of Candidates whose `to` differs from the naive
    referent copy (`c.subject`) and names a real, live person is asserted > 0 -- not merely
    nonzero-looking, and not a value the fold could only ever refuse."""
    w = populated.build_realm(0)
    # The ids that exist BEFORE the season: a writ's addressee who dies during it (a combat
    # outcome the ladder decides) leaves `w.persons` but is still a well-formed referent, which
    # is all this control asks (B-D1 PC-02: the degree-ladder migration kills `p_npc_034` here).
    seeded = set(w.persons)
    populated.run(seasons=1, seed=0, w=w)
    writ_derived = []
    for pid, p in w.persons.items():
        for q in questions_for(w, p):
            v = View(pid, [], w.fixtures.get("view_k"), q)
            for c in opening_set(p, v, q, w.fixtures):
                to = c.operands.get("to")
                if to is not None and to != c.subject and isinstance(to, str):
                    writ_derived.append((pid, c.verb, to))
    assert len(writ_derived) > 0, "no Candidate carried a writ-derived operand on the real corpus"
    # CONTROL, THE OTHER DIRECTION: every one of them names a person who actually exists (or
    # existed at the season's start), so the count above is not an artefact of a malformed value
    # -- a tuple, an id no realm ever held -- that the fold would refuse outright for a reason
    # that has nothing to do with the writ.
    unresolvable = [(pid, verb, to) for pid, verb, to in writ_derived if to not in seeded]
    assert not unresolvable, (
        f"{len(unresolvable)} writ-derived `to` values name no person the realm ever held: "
        f"{unresolvable[:5]}")


def test_no_writ_derived_operand_is_ever_a_raw_tuple():
    """THE REGRESSION THIS POSITION'S OWN ADVERSARIAL PASS FOUND (§4 above). The first writing of
    `_from_content_claim` returned the addressee list verbatim and 173 Candidates on this exact
    corpus carried it as a tuple -- a value `w.persons`/`w.rungs` can never key on, so every one
    of them was refused for a reason that was never in the design. This pins the fix."""
    w = populated.build_realm(0)
    populated.run(seasons=1, seed=0, w=w)
    for pid, p in w.persons.items():
        for q in questions_for(w, p):
            v = View(pid, [], w.fixtures.get("view_k"), q)
            for c in opening_set(p, v, q, w.fixtures):
                assert not isinstance(c.operands.get("to"), tuple), (
                    f"{pid}/{c.verb} carries a tuple `to`: {c.operands}")


# ======================================================================================
# 6 -- NOTHING WIDENS THAT DID NOT NEED TO
# ======================================================================================

def test_question_sources_stays_at_two_clause_3_is_not_a_fourth_source():
    """r2 `01` §A.5.4, RULED: *"Not a fourth source. One `Question` shape, one `source` string,
    one `occasioned_by` route."* Clause 3 widens Q2's ADMISSION test in place; it mints no new
    `Question.source` value."""
    assert set(QUESTION_SOURCES) == {"claim_landed", "need"}


def test_a_bad_source_still_raises_named_did_not_smuggle_one_in():
    with pytest.raises(Forbidden, match="question_sources"):
        Question("q:bad", "named", ("p_x",), "c1")


def test_writ_sourced_operands_refuses_a_member_outside_requires_operands():
    """BATCH-CLOSE FINDING (methodology-close Phase 1, antagonist). The load-time cross-
    validation between `writ_sourced_operands` and `requires_operands` shipped with no falsifier
    -- it never fires on today's data, so nothing observed whether it could actually raise. It
    could not: it named `Unspecified` without importing it, so a real mismatch died with
    `NameError` instead. Call the check directly with a planted mismatch, the way `data/rosters.py`
    has no equivalent test for its own sibling cross-validations either, but this one is new."""
    with pytest.raises(Unspecified, match="writ_sourced_operands"):
        _check_writ_sourced_subset(frozenset({"to", "at"}), frozenset(REQUIRES_OPERANDS))
    # THE CONTROL -- the real roster, read back through its own binding, never re-typed: a second
    # literal here would be exactly the "roster duplicated from the data file" defect this whole
    # position exists to fix (`test_jordan_no_definition_is_hardcoded_in_a_body` caught the first
    # draft doing precisely this).
    _check_writ_sourced_subset(frozenset(WRIT_SOURCED_OPERANDS), frozenset(REQUIRES_OPERANDS))
