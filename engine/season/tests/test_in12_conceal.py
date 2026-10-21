"""Plan position IN-12 step 10 (`workplans/valoria_master_workplan_v9_part5.md`), #453 §10.4 step 10 --
`conceal`: a person mints a `cover` Record whose `terms` is himself (#453 §9.3, K-19), and while he holds
it and a stage is unmatured, `state/attribution.py::anchor_of` answers the cover's id for his acts.

⚠ A PROPERTY, NOT A REALM COUNT. Every test drives a HAND-BUILT world (`tiny_world`) through the real fold
(`SeasonDriver.resolve`), the real WITNESS (`SeasonDriver.witness`, the shipped `all_five` fan and `both`
deposit rule), the real MATTER (which ripens the cover's stages) and the real formation (`questions_for`
-> `opening_set`); NO TEST HERE ASSERTS THAT `conceal` EXECUTED IN THE SEED-0 REALM (v9 §0.5, RULED
2026-10-13 *"Relax exit rules"*).

What each block proves, and the control that stops it passing vacuously:

  1. THE ROW: resolvable, `own`, no precondition and an empty refusal column, mints through the shared
     mint (so it opens the maker's `hold`), declared `uncelled:` with its reason.
  2. THE MINT, THROUGH THE REAL FOLD: `cover.assumed`, and a `cover` whose `terms` is the ACTOR whatever
     the act's `subject`, held by him alone, with stages wound.
  3. THE FALSIFIER (#453 §10.4 step 10, verbatim: *"an Event anchors on a `cover` id, and a chronicle
     deposit about it names the alias; `seen.who` still names the actor"*): the Duke conceals, then
     convenes (a `binding_decision` row, so `chronicle` admits a witness nowhere near); the convening
     anchors on the cover id; the King, at the realm, holds a `chronicle`-sourced (`told_by`) claim about
     it whose subject is the alias and none about the Duke; the stranger standing beside the Duke holds a
     `seen` claim whose `who` is the Duke. CONTROL: the same convening with no cover anchors on the Duke
     and the King's deposit names him. MUTATION, run in-test: the cover read removed
     (`attribution.live_cover` answering `None`) and the falsifier goes red.
  4. `_ch_witness_key` CHANGES WITH IT: a knot-partner of the Duke witnesses his `utter` by key; with a
     live cover he does not (the cover id is no person and no knot names it), and the stranger beside
     him still does, `co_located`.
  5. THE COVER LAPSES: after MATTER ripens every stage the Duke's acts anchor on him again; with one
     stage still unmatured they do not. A covered Event already LOGGED keeps the alias after the lapse
     (`World._covers_logged`; `World._on_logged`'s invariant). And a cover he does not hold, or one
     naming someone else, hides nothing.
  6. THE PERSON-SIDE DECLINE (`rosters.yaml: held_document_declines`): before the cover, the Duke forms
     `conceal`; once he holds it (and WITNESS has deposited its content to him) he forms none. The
     loader refuses a line naming no verb or no record kind.

  7. THE ALIAS READS THAT BATCH-CLOSE FOUND (B-Q Phase 1, reproduced red first): (a) CENSUS individuates
     a person demanded by a dead covered actor's `dispatch` at the actor's place and raises no `KeyError`
     (`world_q.event_place` places an act-caused Event by its ACTOR, not by its cover); (b) a covered
     `move`'s deposit names the alias alone, not the mover (`epistemic.claim_subjects`); (c) a covered
     mover's `travel.ended` chains to his `travel.moved` (`loop/matter.py`, `written=True`). Each has its
     uncovered control.

MUTATIONS, run at the build 2026-10-21 (each RED, then restored and GREEN):
  * `state/attribution.py::anchor_of`'s tier-1 line returning `who` (the cover read deleted) -> block 3's
    falsifier, block 4 and block 5's logged-alias test RED (block 3 also runs it in-test, through
    `live_cover`).
  * `state/attribution.py::_cover_for` re-reading a LOGGED Event's cover live -> block 5's logged-alias
    test RED.
  * `loop/effects_information.py::_eff_conceal` writing the act's `subject` as `terms` -> block 2 RED, and
    block 3's falsifier RED (the cover then names the convening's referent, not the Duke).
  * `decision/options.py::opening_set`'s `held_document_declines` decline deleted -> block 6 RED.
"""

from __future__ import annotations

import pytest

from ..data import verbs as VERBS
from ..data.matrix import WriteClass
from ..data.rosters import PURSUIT_AXES, SEEN_PREDICATE, table, table_meta
from ..data.verbs import _OPENERS_FROM_EFFECTS, VERB_TABLE
from ..decision import assemble
from ..decision.options import opening_set
from ..gaps import Forbidden
from ..harness import probes as P
from ..loop.driver import SeasonDriver, mint_token, resolvable_verbs
from ..queries.world_q import event_place, hold_force, questions_for
from ..state import attribution
from ..state.attribution import anchor_of, live_cover, matured_terms
from ..state.carriers import Act, Question, Tenure
from ..epistemic import _ch_witness_key
from .test_in10_record_operands import _resolve

DUKE, SEAT = "p_high", "off_duke"          # seated at S; the seat grants `convene`
WATCHER = "p_other"                        # moved to S: present at the Duke's acts
FAR = "p_king"                             # at R: never present at S
COVER = "rec:cc"


def _kinds(events):
    return [e.kind for e in events]


def _world(knot: bool = False):
    """`tiny_world` at a MATTER barrier, the stranger standing where the Duke stands (S) -- the one edit to
    the fixture, made on his own edges; `knot=True` also knots the King to the Duke (block 4)."""
    w = P.tiny_world()
    for t in w.persons[WATCHER].tenures:
        if t.live and t.kind in ("contain", "reside"):
            t.object = "S"
    if knot:
        w.add_tenure(Tenure("t_knot", FAR, DUKE, "knot", since=0))
    d = SeasonDriver(w)
    d.matter(mint_token(w, WriteClass.MATTER), [])
    return w, d


def _conceal(w, d, subject=DUKE, key="cc"):
    out = _resolve(w, d, Act(id=key, actor=DUKE, verb="conceal", payload={"subject": subject}))
    assert _kinds(out) == ["cover.assumed"], _kinds(out)
    return out


def _convene(w, d, key="cv"):
    out = _resolve(w, d, Act(id=key, actor=DUKE, verb="convene", via=SEAT, payload={"subject": "S"}))
    (e,) = [e for e in out if e.kind == "date.scheduled"]
    return out, e


def _witness(w, d, events):
    d.witness(mint_token(w, WriteClass.INTERIOR), events)


def _about(w, pid, e):
    """`pid`'s event-kind claims deposited from `e` (predicate `e.kind`), as (subject, source) pairs."""
    return sorted((c.subject, c.source) for c in w.persons[pid].ledger if c.predicate == e.kind)


def _seen_who(w, pid, e):
    """The `who` of every `seen` claim `pid` holds from this tick's Events (one Event witnessed here)."""
    return [c.value.who for c in w.persons[pid].ledger if c.predicate == SEEN_PREDICATE]


# ======================================================================================
# 1 -- THE ROW
# ======================================================================================

def test_conceal_is_a_resolvable_own_verb_that_opens_hold_and_is_declared_uncelled():
    row = VERB_TABLE["conceal"]
    assert row.eligibility == ("own",)
    assert row.beneficiary == "actor" and not row.counterparty
    assert row.stratum == "social", "a `binding_decision` row's kinds are chronicled by kind"
    assert row.writes == ("Record.exists",)
    assert row.emits == ("cover.assumed",) and tuple(row.emits_on_refusal) == ()
    assert row.requires_typed is None, "no precondition (#453 §9.3)"
    assert "conceal" in resolvable_verbs()
    assert "conceal" in _OPENERS_FROM_EFFECTS["hold"], _OPENERS_FROM_EFFECTS["hold"]
    cells, uncelled = table("alignment"), table_meta("alignment")["uncelled"]
    assert str(uncelled.get("conceal") or "").strip()
    assert not [ax for ax in PURSUIT_AXES if "conceal" in cells[ax]]


# ======================================================================================
# 2 -- THE MINT, THROUGH THE REAL FOLD
# ======================================================================================

def test_a_conceal_mints_a_cover_naming_the_actor_whatever_its_subject_held_by_him_alone():
    w, d = _world()
    _conceal(w, d, subject="S")                         # the referent is a rung; the cover is about him
    rec = w.records[COVER]
    assert rec.kind == "cover"
    assert rec.subject_matter == {"terms": DUKE}, rec.subject_matter
    assert rec.stages, "the mint winds the stages (H-80's default for an act declaring none)"
    assert hold_force(w, COVER).subject == DUKE
    assert live_cover(w, DUKE) == COVER


# ======================================================================================
# 3 -- THE FALSIFIER
# ======================================================================================

def _falsifier_reading(w, d):
    """Conceal, convene, witness: (the convening's anchor, the King's deposits from it, the stranger's
    `seen` whos). The conceal is formed on a referent that is not the Duke (`S`), as a computed act's
    subject is its question's referent: the cover must still name HIM."""
    _witness(w, d, _conceal(w, d, subject="S"))
    out, e = _convene(w, d)
    _witness(w, d, out)
    return anchor_of(w, e), _about(w, FAR, e), _seen_who(w, WATCHER, e), e


def test_a_covered_act_anchors_on_the_cover_its_chronicle_deposit_names_the_alias_and_seen_names_the_actor():
    w, d = _world()
    anchor, far, seen, e = _falsifier_reading(w, d)
    assert anchor == COVER, f"the convening anchored on {anchor!r}, not the cover"
    assert event_place(w, e) == "S", "where it happened does not move: the cover is read at its holder"
    assert far, "the King, nowhere near, received nothing (the chronicle channel is the route)"
    assert {src for _, src in far} == {"told_by"}, far
    subjects = {s for s, _ in far}
    assert COVER in subjects, f"the chronicle deposit does not name the alias: {far}"
    assert DUKE not in subjects, f"the chronicle deposit names the actor: {far}"
    assert DUKE in seen, f"`seen.who` no longer names the actor for one present: {seen}"


def test_control_the_same_convening_without_a_cover_anchors_on_the_actor_and_names_him():
    w, d = _world()
    out, e = _convene(w, d)
    _witness(w, d, out)
    assert anchor_of(w, e) == DUKE
    assert DUKE in {s for s, _ in _about(w, FAR, e)}
    assert not [r for r in w.records.values() if r.kind == "cover"]


def test_mutation_without_the_cover_read_the_falsifier_fails(monkeypatch):
    """THE NAMED MUTATION, RUN IN-TEST: `live_cover` answering `None` (the cover read removed from tier 1)
    and the convening anchors on the Duke again, his name in the King's deposit -- the route is that read."""
    monkeypatch.setattr(attribution, "live_cover", lambda w, actor: None)
    w, d = _world()
    anchor, far, _, _ = _falsifier_reading(w, d)
    assert anchor == DUKE
    assert DUKE in {s for s, _ in far} and COVER not in {s for s, _ in far}


# ======================================================================================
# 4 -- `_ch_witness_key` CHANGES WITH IT
# ======================================================================================

def test_a_knot_partner_stops_witnessing_by_key_while_the_cover_is_live():
    w, d = _world(knot=True)
    out = _resolve(w, d, Act(id="u0", actor=DUKE, verb="utter"))
    (e0,) = [e for e in out if e.kind == "proposition.uttered"]
    w.discard_caches()
    assert _ch_witness_key(w, e0, FAR), "control: the knot-partner witnesses by key with no cover"
    _conceal(w, d)
    out = _resolve(w, d, Act(id="u1", actor=DUKE, verb="utter"))
    (e1,) = [e for e in out if e.kind == "proposition.uttered"]
    w.discard_caches()
    assert anchor_of(w, e1) == COVER
    assert not _ch_witness_key(w, e1, FAR), "the knot-partner still witnesses a covered act by key"
    _witness(w, d, out)
    assert _about(w, FAR, e1) == [], "the far knot-partner learned of the covered act"
    assert _about(w, WATCHER, e1), "the stranger present no longer witnesses (co_located)"


# ======================================================================================
# 5 -- THE COVER LAPSES, AND ONLY HIS OWN, HELD, COVER HIDES HIM
# ======================================================================================

def _season(w, d, tick):
    w.tick = tick
    w.discard_caches()
    d.matter(mint_token(w, WriteClass.MATTER), [])


def test_the_cover_lapses_when_matter_has_ripened_every_stage():
    w, d = _world()
    _conceal(w, d)
    n = len(w.records[COVER].stages)
    assert n >= 2, "the lapse needs a cover of two stages or more to show the partial state"
    for t in range(1, n):
        _season(w, d, t)
    assert 0 < matured_terms(w, COVER) < n
    assert live_cover(w, DUKE) == COVER, "a cover with a stage still unmatured is live"
    _season(w, d, n)
    assert matured_terms(w, COVER) == n
    assert live_cover(w, DUKE) is None, "a cover every stage of which has ripened still hides him"
    _, e = _convene(w, d, key="cv_late")
    assert anchor_of(w, e) == DUKE


def test_a_logged_covered_event_keeps_its_alias_after_the_cover_lapses():
    """`World._on_logged`'s invariant (an appended Event's anchor cannot change, `test_in56`'s index
    rests on it): the cover is read as the Event is logged and kept (`World._covers_logged`), so the
    lapse moves the Duke's LATER acts back onto him and leaves the earlier one on the alias -- in the
    anchor and in the last-emission index alike."""
    w, d = _world()
    _conceal(w, d)
    _, e = _convene(w, d)
    assert anchor_of(w, e) == COVER
    for t in range(1, len(w.records[COVER].stages) + 1):
        _season(w, d, t)
    assert live_cover(w, DUKE) is None, "precondition: the cover has lapsed"
    assert anchor_of(w, e) == COVER, "a logged Event's anchor moved when the cover lapsed"
    assert w.last_emission_of("date.scheduled", COVER) == e.id
    assert w.last_emission_of("date.scheduled", DUKE) is None


def test_a_cover_naming_another_or_not_held_hides_nobody():
    w, d = _world()
    _conceal(w, d)
    rec = w.records[COVER]
    rec.subject_matter = {"terms": WATCHER}             # a cover about someone else, in the Duke's hand
    assert live_cover(w, DUKE) is None
    rec.subject_matter = {"terms": DUKE}
    assert live_cover(w, DUKE) == COVER
    hold_force(w, COVER).until = w.tick                  # no longer in his hand
    assert live_cover(w, DUKE) is None


# ======================================================================================
# 6 -- THE PERSON-SIDE DECLINE
# ======================================================================================

def _conceals_formed(w, pid=DUKE):
    """The person's option set on a question about the place he stands (`tiny_world` raises no question
    of its own at tick 0, so one is handed to `opening_set` as `test_in10_record_operands` does), plus
    any question the world raises for him: the `conceal` Candidates formed."""
    p = w.persons[pid]
    qs = [Question("q:conceal", "claim_landed", ("S",), None)] + list(questions_for(w, p))
    return [c for q in qs for c in opening_set(p, assemble(p, q, 12), q, w.fixtures) if c.verb == "conceal"]


def test_a_person_holding_a_cover_forms_no_conceal():
    w, d = _world()
    assert _conceals_formed(w), "control: with no cover held the Duke forms `conceal`"
    _witness(w, d, _conceal(w, d))
    assert [c for c in w.persons[DUKE].ledger if c.subject == COVER and c.predicate == "content:cover"], (
        "precondition: WITNESS deposited the cover's content to its holder")
    assert _conceals_formed(w) == [], "a second cover formed while the first is held"


def test_a_held_document_declines_line_naming_no_verb_or_no_record_kind_is_refused_at_load():
    assert VERBS._load_held_document_declines({"conceal": "cover"}) == VERBS.HELD_DOCUMENT_DECLINES
    assert VERBS.HELD_DOCUMENT_DECLINES == {"conceal": "cover"}
    for planted in ({"conceal": "no_such_kind"}, {"no_such_verb": "cover"}, {"conceal": ""}):
        with pytest.raises(Forbidden, match="held_document_declines"):
            VERBS._load_held_document_declines(planted)


# (7) THE ALIAS READS THAT BATCH-CLOSE FOUND ------------------------------------------------------------

def test_census_places_a_dead_covered_actors_demand_where_he_acted_and_raises_nothing():
    """The Duke conceals, then a `dispatch` naming an un-individuated person emits `person.demanded`; he then
    dies. CENSUS must read the demand's place from the ACTOR (the cover's holder-place is gone with him)."""
    from ..data.matrix import Step
    from ..state.ids import ROOT
    w, d = _world()
    _resolve(w, d, Act(id="cc", actor=DUKE, verb="conceal", payload={"subject": DUKE}))
    out = _resolve(w, d, Act(id="dd", actor=DUKE, verb="dispatch", via=SEAT, payload={"subject": "p_clerk"}))
    demanded = [e for e in out if e.kind == "person.demanded"]
    assert demanded and anchor_of(w, demanded[0]) == COVER, "precondition: a covered act-caused demand"
    w.step = Step.MATTER
    w.write("exists", mint_token(w, WriteClass.MATTER), lambda: w.remove_person(DUKE), record_kind="Person",
            fieldname="exists", driver="Event", emits="person.died", subject=DUKE, causes=[ROOT])
    d.census(mint_token(w, WriteClass.MATTER))           # raised KeyError at census.py:91 before the fix


def test_a_covered_moves_deposit_names_the_alias_and_not_the_mover_and_his_travel_ends_on_his_move():
    from ..epistemic import claim_subjects
    for cover in (True, False):
        w, d = _world()
        if cover:
            _resolve(w, d, Act(id="cc", actor=WATCHER, verb="conceal", payload={"subject": WATCHER}))
        mv = _resolve(w, d, Act(id="mv", actor=WATCHER, verb="move", payload={"to": "S"}))
        (moved,) = [e for e in mv if e.kind == "travel.moved"]
        subjects = claim_subjects(w, moved, "both")
        if cover:
            assert subjects == [COVER], subjects            # the mover's id left the deposit
        else:
            assert subjects == [WATCHER], subjects          # control: uncovered, he is the subject
        w.tick += 1
        w.discard_caches()
        d.matter(mint_token(w, WriteClass.MATTER), [])
        ended = [e for e in w.log if e.kind == "travel.ended"]
        assert ended and all(e.causes == [moved.id] for e in ended), [e.causes for e in ended]
