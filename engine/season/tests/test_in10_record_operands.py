"""Plan position IN-10 (`workplans/valoria_master_workplan_v9_part5.md`), #453 §10.1 -- THE HELD-RECORD
OPERAND CHANNEL, the enabler only.

What each block proves, and the control that stops it passing vacuously:

  1. THE GATE: a held dispensation's `terms` answers `subject` in `_derive_operand` (its `held=`
     source, read through `rosters.yaml: record_sourced_operands`), and its addressee answers `to`.
     Controls: the same person with no held source answers the referent; a QUESTION about the same
     document keeps the Record as `subject` (the act is about the document) while its `to` still
     comes off the document -- `15c`'s channel, unmoved.
  2. `held_record_claims` reads the person's OWN live `hold`s only: a released hold, a document
     merely witnessed and a kind the map does not carry each answer nothing.
  3. `issue` JOINS THE KNOWN-PERSON FAN FOR `to`: an issuer forms one `issue` per person he knows,
     `subject` the referent (the writ's `terms`) and `to` a known person, so `terms` and the executor
     separate; each act's id carries `>to`. The fold mints a writ whose `terms` is not its addressee,
     through the seat (`Act.via`); the new `terms` conjunct refuses a writ whose issuer holds no
     claim on its terms (`issue.refused`), and its control -- a Proposition's terms -- executes.
"""

from __future__ import annotations

from ..data.fixtures import DEFAULT_FIXTURES
from ..data.matrix import WriteClass
from ..data.rosters import RECORD_CONTENT
from ..data.verbs import VERB_TABLE, act_key
from ..decision.options import _derive_operand, held_record_claims, opening_set
from ..harness import probes as P
from ..loop.driver import SeasonDriver, mint_token
from ..loop.witness import content_value
from ..state.carriers import Act, Claim, Question, Record, Tenure, View

SEAT, DUKE = "off_duke", "p_high"
_CONTENT = RECORD_CONTENT["predicate"]


def _content_claim(cid, holder, rec_id, kind, sm, when=0):
    return Claim(cid, holder, rec_id, f"{_CONTENT}:{kind}", content_value(sm), when, "firsthand",
                 100, "own")


def _hold_document(w, p, kind, sm, rec_id="rec_w", held=True):
    """A Record of `kind` saying `sm`, its content claim in `p`'s ledger, and (if `held`) `p`'s live
    `hold` on it -- what `_mint_document` and the content deposit leave behind."""
    w.records[rec_id] = Record(rec_id, "S", kind, subject_matter=sm)
    if held:
        w.add_tenure(Tenure(f"t_{rec_id}", p.id, rec_id, "hold", since=0))
    c = _content_claim(f"c_{rec_id}", p.id, rec_id, kind, sm)
    p.ledger.append(c)
    return c


# ======================================================================================
# 1 -- THE GATE
# ======================================================================================

def test_in10_a_held_dispensations_terms_answers_subject_in_derive_operand():
    w = P.tiny_world()
    p = w.persons[DUKE]
    c = _hold_document(w, p, "dispensation", {"terms": "off_dicastery", "to": ["p_mid"], "at": None})
    (held,) = held_record_claims(p)
    assert held is c
    q = Question("q:other", "claim_landed", ("S",), None)        # a question about something else
    assert _derive_operand(p, "subject", q, "S", w.fixtures, held=held) == "off_dicastery"
    assert _derive_operand(p, "to", q, "S", w.fixtures, held=held) == "p_mid"
    # CONTROL 1: no held source -- the referent, as before IN-10.
    assert _derive_operand(p, "subject", q, "S", w.fixtures) == "S"
    assert _derive_operand(p, "to", q, "S", w.fixtures) == "S"
    # CONTROL 2: a QUESTION about the document -- the act is about the document itself, so
    # `subject` stays the Record; `to` still comes off the document (`15c`, unmoved).
    qd = Question(f"q:claim:{c.id}", "claim_landed", ("rec_w",), c.id)
    assert _derive_operand(p, "subject", qd, "rec_w", w.fixtures) == "rec_w"
    assert _derive_operand(p, "to", qd, "rec_w", w.fixtures) == "p_mid"


def test_in10_a_held_petition_answers_too_and_never_from():
    w = P.tiny_world()
    p = w.persons["p_mid"]
    _hold_document(w, p, "petition", {"terms": "p_low", "to": ["p_high"], "from": "D"})
    (held,) = held_record_claims(p)
    q = Question("q:other", "claim_landed", ("S",), None)
    assert _derive_operand(p, "subject", q, "S", w.fixtures, held=held) == "p_low"
    assert _derive_operand(p, "to", q, "S", w.fixtures, held=held) == "p_high"
    # `from` is on no kind (r2's ruling): the actor's own containing rung, not the petition's `D`.
    assert _derive_operand(p, "from", q, "S", w.fixtures, held=held) == "Hh"


# ======================================================================================
# 2 -- HELD MEANS THE PERSON'S OWN LIVE HOLD
# ======================================================================================

def test_in10_held_record_claims_reads_only_live_holds_of_mapped_kinds():
    w = P.tiny_world()
    p = w.persons[DUKE]
    sm = {"terms": "p_mid", "to": ["p_low"], "at": None}
    _hold_document(w, p, "dispensation", sm, rec_id="rec_seen", held=False)   # witnessed only
    _hold_document(w, p, "text", {}, rec_id="rec_text")                        # kind not mapped
    assert held_record_claims(p) == []
    c = _hold_document(w, p, "dispensation", sm, rec_id="rec_live")
    assert held_record_claims(p) == [c]
    next(t for t in p.tenures if t.object == "rec_live").until = 1           # handed on / released
    assert held_record_claims(p) == []


# ======================================================================================
# 3 -- `issue` JOINS THE KNOWN-PERSON FAN
# ======================================================================================

def _knows(p, *who):
    for i, x in enumerate(who):
        p.ledger.append(Claim(f"k{i}", p.id, x, "exists:Person", 1, 0, "firsthand", 100, "own"))


def test_in10_issue_fans_over_known_persons_so_terms_and_executor_separate():
    w = P.tiny_world()
    p = w.persons[DUKE]
    _knows(p, "p_mid", "p_low")
    p.ledger.append(Claim("c_s", p.id, "S", "stores:grain", 8, 0, "firsthand", 100, "own"))
    q = Question("q:s", "claim_landed", ("S",), None)
    got = [c for c in opening_set(p, View(p.id, [], w.fixtures.get("view_k"), q), q, w.fixtures)
           if c.verb == "issue"]
    assert sorted(c.operands["to"] for c in got) == ["p_low", "p_mid"], got
    assert all(c.subject == c.operands["subject"] == "S" for c in got)
    keys = {act_key("issue", c.subject, c.operands) for c in got}
    assert keys == {"S>p_low", "S>p_mid"}
    assert VERB_TABLE["issue"].requires_typed.known_person_operands() == ("to",)
    # CONTROLS: a person who knows nobody forms no `issue` -- a writ to nobody is an act with a
    # hole; and one who knows them but holds nothing on the terms forms none either (`terms`).
    for mk in (lambda x: x.ledger.append(Claim("c_s", x.id, "S", "stores:grain", 8, 0, "firsthand",
                                               100, "own")),
               lambda x: _knows(x, "p_mid", "p_low")):
        w2 = P.tiny_world()
        p2 = w2.persons[DUKE]
        mk(p2)
        assert not [c for c in opening_set(p2, View(p2.id, [], w2.fixtures.get("view_k"), q), q,
                                           w2.fixtures) if c.verb == "issue"]


def _world():
    w = P.tiny_world(DEFAULT_FIXTURES)
    d = SeasonDriver(w)
    d.matter(mint_token(w, WriteClass.MATTER), [])
    return w, d


def _fold(w, d, act):
    out = d.resolve(mint_token(w, WriteClass.ACTS), [act],
                    contest_max_depth=w.fixtures.get("contest_max_depth"))
    w.log.extend(out)
    return [e.kind for e in out], out


def test_in10_a_computed_shaped_issue_mints_a_writ_whose_terms_is_not_its_executor():
    w, d = _world()
    duke = w.persons[DUKE]
    # THE NEW CONJUNCT, FIRST WITH NOTHING HELD: the issuer holds no claim on `prop_x` -- refused,
    # keyed `terms` (`issue.refused`), with an executor the seat DOES reach.
    unknown = Act(id="is_unknown", actor=DUKE, verb="issue", via=SEAT,
                  payload={"subject": "prop_x", "to": "p_mid"})
    assert _fold(w, d, unknown)[0] == list(VERB_TABLE["issue"].refusal_for("terms"))
    # CONTROL: the same writ once he holds a claim on its terms -- a Proposition, which has no place,
    # so a purview clause on the terms would have refused it (the row's note: a covenant's terms).
    duke.ledger.append(Claim("c_px", DUKE, "prop_x", "exists:Proposition", 1, 0, "firsthand", 100,
                             "own"))
    kinds, out = _fold(w, d, Act(id="is_sep", actor=DUKE, verb="issue", via=SEAT,
                                 payload={"subject": "prop_x", "to": "p_mid"}))
    assert kinds == ["dispensation.issued"]
    rec = w.records[out[0].changes[0].subject]
    assert rec.subject_matter["terms"] == "prop_x" and rec.subject_matter["to"] == ["p_mid"]
    # and no seat: the purview conjunct reads UNKNOWN and refuses (the `Act.via` falsifier).
    bare = Act(id="is_bare", actor=DUKE, verb="issue", via=None,
               payload={"subject": "prop_x", "to": "p_mid"})
    assert _fold(w, d, bare)[0] != ["dispensation.issued"]
