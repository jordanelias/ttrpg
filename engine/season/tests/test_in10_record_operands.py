"""Plan position IN-10 (`workplans/valoria_master_workplan_v9_part5.md`), #453 §10.1 -- THE HELD-RECORD
OPERAND CHANNEL (`rosters.yaml: record_sourced_operands`), the enabler.

⚠ THE CHANNEL IS A PROPERTY, NOT A REALM COUNT. Every test here drives it on a HAND-BUILT world
through the real formation (`opening_set`/`operand_bags`), the real packer (`pack_scenes`, which
names `Act.via`) and the real fold (`SeasonDriver.resolve`, `.witness`), the cause controlled and a
named mutation reddening each. NO TEST HERE ASSERTS THAT ANY VERB EXECUTED IN THE SEED-0 REALM (v9
§0.5, RULED 2026-10-13 *"Relax exit rules"*): whether the authored world ever hands a seated person
a commission is authored data, not this wiring.

What each block proves, and the control that stops it passing vacuously:

  1. THE GATE: a held dispensation's `terms` answers `subject` in `_derive_operand` (`held=`), its
     addressee `to`; `from` is on no kind. Controls: no held source -> the referent; a QUESTION
     about the same document keeps the Record as `subject` (`15c`'s channel, unmoved).
  2. `held_record_claims` reads the person's OWN live `hold`s of mapped kinds only.
  3. `issue` JOINS THE KNOWN-PERSON FAN FOR `to`: one writ per executor known, `terms` the
     referent, keyed `subject>to`; the fold mints a writ whose `terms` is not its executor, THROUGH
     THE SEAT (`Act.via`); seatless it is refused. The new `terms` conjunct refuses a writ whose
     issuer holds no claim on its terms.
  4. THE FAN OVER HELD RECORDS: a held commission naming a seat and a person forms a `confer` of
     that seat on that person, unknown to the conferrer; a commission about another seat adds
     nothing; the act carries `Act.via` and executes. FALSIFIER (the entry's): no `Act.via` on an
     execution the channel forms.
  5. H-71's LEAK: the channel's `confer` onto a HELD office displaces the incumbent, and no witness
     is deposited a claim about the outgoing holder's Tenure (its opaque id).

MUTATIONS, run at the build 2026-10-16 (each RED, then restored byte-exact and GREEN):
  * `operand_bags`' held-Record loop emptied (`for c in records:` -> `for c in ():`) -> block 4's
    two tests and block 5 RED (no `confer` on the commission's addressee).
  * `_derive_operand`'s `held` branch disabled -> block 1's two tests RED, and NOTHING ELSE (re-run
    at the B-K close: 2 failed, 10 passed). Block 4 stays GREEN: `confer` is untyped, so `_operands`
    returns `dict(given)` without calling `_derive_operand`, and in production `operand_bags` skips
    any Record whose `_content_answer(c, 'subject') != subject`, so `held=` can answer only the
    referent it was already handed. THE `held=` SUBJECT BRANCH IS THEREFORE EXERCISED ONLY BY DIRECT
    CALLS (block 1); production `subject` delivery is via the classed stamps (`seats_named`,
    `places_named`, `larders_in_purview`, `writs_held`). The hook is kept, not observed in play.
  * `decision/choose.py::pack_scenes` minting `via=None` -> block 3's fold test, block 4's second
    and block 5 RED: the entry's `Act.via` falsifier observes it.
  * `epistemic._hold_tenure_ends` returning `(subject,)` unexpanded -> block 5 RED (H-71's leak).
  * `issue`'s `terms` conjunct (and its refusal key) deleted from `verb_table.yaml` -> block 3's
    three tests RED (no fan: `to` is the referent again).
"""

from __future__ import annotations

from ..data.fixtures import DEFAULT_FIXTURES
from ..data.matrix import WriteClass
from ..data.rosters import RECORD_CONTENT
from ..data.verbs import VERB_TABLE, act_key
from ..decision import assemble
from ..decision.choose import pack_scenes
from ..decision.options import _derive_operand, held_record_claims, opening_set
from ..harness import probes as P
from ..loop.driver import SeasonDriver, mint_token
from ..loop.witness import content_value
from ..queries import world_q
from ..state.carriers import Act, Claim, Question, Record, Tenure
from ..state.ids import H

from .test_g3_not_yours import _gov_world, _hold

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


def _knows(p, *who):
    for i, x in enumerate(who):
        p.ledger.append(Claim(f"k{p.id}{i}", p.id, x, "exists:Person", 1, 0, "firsthand", 100, "own"))


def _formed(w, pid, q):
    p = w.persons[pid]
    return opening_set(p, assemble(p, q, 12), q, w.fixtures)


def _acts(w, pid, cands):
    mint = lambda who, verb, subj: H(w.world_seed, w.tick, who, f"act:{verb}:{subj}")
    return [a for s in pack_scenes(w.persons[pid], cands, 99, w.fixtures, mint) for a in s.acts]


def _resolve(w, d, *acts):
    out = d.resolve(mint_token(w, WriteClass.ACTS), list(acts),
                    contest_max_depth=w.fixtures.get("contest_max_depth"))
    w.log.extend(out)
    return out


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
# 2 -- HELD MEANS THE PERSON'S OWN LIVE HOLD, OF A KIND THE MAP CARRIES
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


def test_in10_what_a_document_is_about_has_one_owner_per_kind():
    """B-K close (ARC 5): `person_q.ABOUT_KEYS` is DERIVED from `rosters.yaml:
    record_sourced_operands`' `subject:` per kind, so `ledger_names` reads a writ's `terms` and a
    sheet's `proposition` -- never an addressee (`to`, a sheet's `head`). MUTATION (seen red,
    2026-10-16): every kind mapped to `terms` -- the old `record_kinds.content.read_from`
    derivation's effect, which had no `faction_sheet` row -> RED (the sheet's `proposition` unnamed)."""
    from ..data.requires import RECORD_SOURCED_OPERANDS
    from ..queries.person_q import ABOUT_KEYS, ledger_names
    assert ABOUT_KEYS == {k: m["subject"] for k, m in RECORD_SOURCED_OPERANDS.items()
                          if "subject" in m}
    w = P.tiny_world()
    p = w.persons[DUKE]
    writ = _content_claim("c_w", p.id, "rec_w", "dispensation",
                          {"terms": "off_reeve", "to": ["p_low"], "at": None})
    sheet = _content_claim("c_s", p.id, "rec_s", "faction_sheet",
                           {"proposition": "prop_crown", "members": ["p_mid"], "holdings": [],
                            "seats": [], "head": "p_other"})
    names = ledger_names([writ, sheet])
    assert {"off_reeve", "prop_crown"} <= names, names
    assert not {"p_low", "p_other"} & names, names


def test_in10_held_record_claims_picks_by_the_ledger_readers_comparator():
    """B-K close (LOG 6): the newest content claim per held Record is `LedgerReader._best`'s pick --
    most recent, then most confident, strict `>` -- not a second ladder. Two claims on one Record at
    the SAME tick: the more confident wins although it was deposited first. MUTATION (seen red,
    2026-10-16): the old `c.when >= best.when` pick restored -> the later, less confident claim."""
    w = P.tiny_world()
    p = w.persons[DUKE]
    sm = {"terms": "p_mid", "to": ["p_low"], "at": None}
    sure = _hold_document(w, p, "dispensation", sm, rec_id="rec_two")
    unsure = _content_claim("c_rec_two_b", p.id, "rec_two", "dispensation", sm)
    unsure.confidence = 50
    p.ledger.append(unsure)
    assert sure.when == unsure.when and sure.confidence > unsure.confidence   # anti-vacuity
    assert held_record_claims(p) == [sure]


# ======================================================================================
# 3 -- `issue` JOINS THE KNOWN-PERSON FAN
# ======================================================================================

def _issue_world():
    w = P.tiny_world(DEFAULT_FIXTURES)
    d = SeasonDriver(w)
    d.matter(mint_token(w, WriteClass.MATTER), [])
    return w, d


def test_in10_issue_fans_over_known_persons_so_terms_and_executor_separate():
    w, _ = _issue_world()
    p = w.persons[DUKE]
    _knows(p, "p_mid", "p_low")
    p.ledger.append(Claim("c_s", p.id, "S", "stores:grain", 8, 0, "firsthand", 100, "own"))
    q = Question("q:s", "claim_landed", ("S",), None)
    got = [c for c in _formed(w, DUKE, q) if c.verb == "issue"]
    assert sorted(c.operands["to"] for c in got) == ["p_low", "p_mid"], got
    assert all(c.subject == c.operands["subject"] == "S" for c in got)
    assert {act_key("issue", c.subject, c.operands) for c in got} == {"S>p_low", "S>p_mid"}
    assert VERB_TABLE["issue"].known_person_operands() == ("to",)
    # CONTROLS: knowing nobody forms no writ (an act with a hole); knowing them but holding
    # nothing on the terms forms none either (the `terms` conjunct's `said`).
    for mk in (lambda x: x.ledger.append(Claim("c_s", x.id, "S", "stores:grain", 8, 0, "firsthand",
                                               100, "own")),
               lambda x: _knows(x, "p_mid", "p_low")):
        w2, _ = _issue_world()
        mk(w2.persons[DUKE])
        assert not [c for c in _formed(w2, DUKE, q) if c.verb == "issue"]


def test_in10_a_fanned_issue_folds_through_its_seat_to_a_writ_whose_terms_is_not_its_executor():
    w, d = _issue_world()
    duke = w.persons[DUKE]
    _knows(duke, "p_mid")
    duke.ledger.append(Claim("c_s", DUKE, "S", "stores:grain", 8, 0, "firsthand", 100, "own"))
    q = Question("q:s", "claim_landed", ("S",), None)
    (a,) = [a for a in _acts(w, DUKE, _formed(w, DUKE, q)) if a.verb == "issue"]
    assert a.via == SEAT, a                                       # the falsifier's `Act.via`
    # CONTROL, FIRST and one change (B-K close, LOG 9): the same act with no seat, folded before the
    # treatment so it shares nothing with it, is refused on the eligibility clause -- the seat is
    # load-bearing. Exact, as block 4's `confer.refused` control is.
    bare = Act(id="is_bare", actor=DUKE, verb="issue", via=None, payload=dict(a.payload))
    assert [e.kind for e in _resolve(w, d, bare)] == ["issue.unauthorized"]
    assert not [r for r in w.records.values() if r.kind == "dispensation"]
    kinds = [e.kind for e in _resolve(w, d, a)]
    assert kinds == ["dispensation.issued"], kinds
    (rec,) = [r for r in w.records.values() if r.kind == "dispensation"]
    assert rec.subject_matter["terms"] == "S" and rec.subject_matter["to"] == ["p_mid"], rec


def test_in10_the_terms_conjunct_refuses_a_writ_whose_issuer_holds_nothing_on_it():
    w, d = _issue_world()
    unknown = Act(id="is_unknown", actor=DUKE, verb="issue", via=SEAT,
                  payload={"subject": "prop_x", "to": "p_mid"})
    assert [e.kind for e in _resolve(w, d, unknown)] == list(VERB_TABLE["issue"].refusal_for("terms"))
    # CONTROL: once he holds a claim on its terms -- a Proposition, which has no place, so a purview
    # clause on the terms would have refused it -- the same writ is issued.
    w.persons[DUKE].ledger.append(Claim("c_px", DUKE, "prop_x", "exists:Proposition", 1, 0,
                                        "firsthand", 100, "own"))
    known = Act(id="is_known", actor=DUKE, verb="issue", via=SEAT,
                payload={"subject": "prop_x", "to": "p_mid"})
    assert [e.kind for e in _resolve(w, d, known)] == ["dispensation.issued"]


# ======================================================================================
# 4 -- THE FAN OVER HELD RECORDS: A COMMISSION IS A `confer` OF ITS SEAT ON ITS ADDRESSEE
# ======================================================================================

def _commission(w, pid, seat, to, rec_id="rec_cm"):
    """`pid` holds (and has read) a dispensation whose `terms` is `seat`, addressed to `to`."""
    return _hold_document(w, w.persons[pid], "dispensation", {"terms": seat, "to": [to], "at": None},
                          rec_id=rec_id)


def _confers_on(w, pid, seat):
    (q, *_) = world_q.questions_for(w, w.persons[pid])
    return q, [c for c in _formed(w, pid, q) if c.verb == "confer" and c.subject == seat]


def test_in10_a_held_commission_forms_a_confer_of_its_seat_on_its_addressee():
    """`p_king` knows nobody, so before IN-10 he could confer the vacant `off_reeve` on himself alone
    (IN-53 D2). Holding a commission naming `off_reeve` and `p_low`, he forms the `confer` onto
    `p_low` too -- a person he knows only through the document. CONTROLS: without the commission,
    himself alone; with a commission about ANOTHER seat (`off_duke2`, terms != referent), nothing on
    `off_reeve` is added -- the referent is never re-aimed (§F1 clause 3)."""
    w, _ = _gov_world()
    _, ctl = _confers_on(w, "p_king", "off_reeve")
    assert {c.operands.get("to") for c in ctl} == {"p_king"}, ctl
    w2, _ = _gov_world()
    _commission(w2, "p_king", "off_duke2", "p_low")
    _, other = _confers_on(w2, "p_king", "off_reeve")
    assert {c.operands.get("to") for c in other} == {"p_king"}, other
    w3, _ = _gov_world()
    _commission(w3, "p_king", "off_reeve", "p_low")
    _, got = _confers_on(w3, "p_king", "off_reeve")
    assert {c.operands.get("to") for c in got} == {"p_king", "p_low"}, got
    # He holds two seats granting `confer` (H-134: one Candidate per seat), so the id carries both
    # the addressee and the seat -- the held bag keys as a known-person bag for `p_low` would.
    assert {act_key("confer", c.subject, c.operands) for c in got if c.operands["to"] == "p_low"} \
        == {"off_reeve>p_low@off_crown", "off_reeve>p_low@off_mayor"}, got


def test_in10_a_held_commission_saying_nothing_of_the_referent_forms_no_bag():
    """B-K close (COR 1 / LOG 2): a held dispensation whose `terms` is absent (`None`: the kind's
    keys are closed, ⊕L35, so the key is present and empty) is about nothing, so it adds no bag on
    `off_reeve` -- `operand_bags` compares the Record's own answer for `subject` with the referent,
    and `None` skips. MUTATION (seen red, 2026-10-16): the old
    `_derive_operand(..., held=c) != subject` check restored -> the missing `terms` falls through to
    the referent and a `confer` onto `p_low` forms. CONTROL: `test_in10_a_held_commission_forms_a_
    confer_of_its_seat_on_its_addressee`, the same commission WITH `terms`."""
    w, _ = _gov_world()
    _hold_document(w, w.persons["p_king"], "dispensation",
                   {"terms": None, "to": ["p_low"], "at": None}, rec_id="rec_cm")
    _, got = _confers_on(w, "p_king", "off_reeve")
    assert {c.operands.get("to") for c in got} == {"p_king"}, got


def test_in10_the_channels_confer_carries_its_seat_and_executes():
    """THE ENTRY'S FALSIFIER, FIRST HALF: an execution the channel forms carries `Act.via`. The act
    `pack_scenes` mints from the commission's Candidate names the seat it is exercised through and
    folds to `tenure.opened`, seating the addressee. CONTROL: the same act stripped of its seat is
    refused, so the `via` is what admitted it."""
    w, d = _gov_world()
    _commission(w, "p_king", "off_reeve", "p_low")
    q, got = _confers_on(w, "p_king", "off_reeve")
    acts = [a for a in _acts(w, "p_king", got) if a.payload.get("to") == "p_low"]
    # One per seat granting `confer` (H-134); EVERY ONE carries the seat it is exercised through.
    assert sorted(a.via for a in acts) == ["off_crown", "off_mayor"], acts
    (a,) = [a for a in acts if a.via == "off_crown"]
    bare = Act(id="cf_bare", actor=a.actor, verb="confer", via=None,
               payload={k: v for k, v in a.payload.items() if k != "via"})
    assert [e.kind for e in _resolve(w, d, bare)] == ["confer.refused"]
    assert "tenure.opened" in [e.kind for e in _resolve(w, d, a)]
    assert _hold(w, "off_reeve").subject == "p_low"


# ======================================================================================
# 5 -- H-71's LEAK: RE-SEATING DEPOSITS NO CLAIM ABOUT THE OUTGOING HOLDER'S TENURE
# ======================================================================================

def test_in10_a_channel_confer_onto_a_held_office_deposits_no_claim_about_the_outgoing_tenure():
    """THE ENTRY'S FALSIFIER, SECOND HALF. `off_reeve` is held by `p_mid` (no live commit). The duke,
    whose seat sits on `D` (S's parent, same faction: he may fill AND revoke the reeve), holds a
    commission naming `off_reeve` and `p_low`, and is told of the seat by it alone (`seats_named`).
    The channel's `confer` displaces `p_mid` and seats `p_low`; after WITNESS no ledger holds a claim
    whose subject is `p_mid`'s closed Tenure -- the opaque edge id H-71's reader expands into who and
    what. CONTROL (non-vacuous): somebody IS deposited a claim about the seat or the outgoing
    holder."""
    w, d = _gov_world()
    w.add_tenure(Tenure("t_reeve_mid", "p_mid", "off_reeve", "hold", since=0))
    _commission(w, DUKE, "off_reeve", "p_low")
    assert "off_reeve" in world_q.seats_named(w, w.persons[DUKE])
    q, got = _confers_on(w, DUKE, "off_reeve")
    acts = [a for a in _acts(w, DUKE, got) if a.payload.get("to") == "p_low"]
    assert len(acts) == 1, (got, acts)
    (a,) = acts
    assert a.via == SEAT, a
    out = _resolve(w, d, a)
    kinds = [e.kind for e in out]
    assert {"tenure.opened", "tenure.closed"} <= set(kinds), kinds
    assert _hold(w, "off_reeve").subject == "p_low"
    d.witness(mint_token(w, WriteClass.INTERIOR), out)
    leaked = [(pid, c.predicate) for pid, p in w.persons.items() for c in p.ledger
              if c.subject == "t_reeve_mid"]
    assert leaked == [], leaked
    about = {c.subject for p in w.persons.values() for c in p.ledger
             if c.subject in ("off_reeve", "p_mid") and c.predicate.startswith("tenure.")}
    assert about, "nobody was deposited a `tenure.*` claim about the re-seating: vacuous"
