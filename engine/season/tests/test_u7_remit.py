"""Plan position `19` -- U7-remit. `workplans/2026-09-18-governance-settlement-behaviour-plan_part2.md`,
*"19 — INSTRUCTION. The five remit verbs; each gains a predicate reading `via.scope` and an effect on the
G4 contract"* -- four built here (`levy`, `open_case`, `determine`, `issue`; `establish` is `13f`'s).
COMPLIANCE: `04:120` AX-1 (*"a seat enters through `Act.via`"*) and `04:330` (purview asked of the seat,
never the actor). OBSERVABLE (`21_RECONCILIATION.md:575`, the antagonist-corrected one): *"a
determination opens the disposal Tenure on its subject via the seat; below quorum, `determine.refused`"*,
and *"a `levy` executes with `Act.via` set"*.

What the position built, each asked of the real fold, the real loader and the real gate:
  * §F.24a form 7, `basis` -- *"a basis lookup on the exercised seat"* -- given its implementation
    (`data/requires.py::Basis`); the seat rides the binding structurally, as the actor does.
  * the keyed `emits_on_refusal:` schema -- `04 §B.13` invariant 4's per-conjunct half, F7 -- with its
    load-time check (`data/verbs.py`) and the fold reading `row.refusal_for(clause)` (`04 §C.4`).
  * the `docket` reader branch (`exists:DocketItem`), and `open_case` putting a matter on the docket.
  * the write gate's EIGHTH basis, `determination` (`state/gate.py::may_determine`).
  * `levy`'s effect (a conserved move into the seat's treasury), `open_case`'s, `determine`'s; `issue`'s
    (`15`'s) precondition.

THE FALSIFIERS, each with the control one clause away:
  * the plan's own: ANY OF THE FOUR EXECUTING WITH `via=None` -- run twice, through the fold as shipped
    (eligibility refuses) and with eligibility forced open (the `basis` conjunct refuses on its own).
  * the plan's added one: TWO `levy`s ON ONE LARDER IN ONE FOLD -- the second refuses (§27.1).
  * below quorum, `determine.refused` -- swept across the fixture's three points, the shipped one the
    control.
  * the gate: a bare opening of the disposal edge is refused (`NotYours`, store put back) whenever one
    clause of `may_determine` fails, and admitted as `determination` when none does.
  * the loader: a keyed row missing a clause's kind, keying a clause it does not have, or naming a
    conjunct it keys nothing to, fails the load naming what.

The fixture is `probes.tiny_world`: `R` > `D` > `S` > `Hh`. `p_high` holds `off_duke` (post `Duke`,
rung and so `scope_rung` `D`, grant `issue determine confer dispatch convene`) and lives in `S`.
`p_low`, `p_mid`, `p_other` live in `Hh`; `p_king` lives in `R`, outside the duchy, and holds nothing.
"""

from __future__ import annotations

import pytest

from ..data import verbs as _verbs
from ..data.fixtures import DEFAULT_FIXTURES
from ..data.matrix import Step, WriteClass
from ..data.requires import UNKNOWN, binding_from_act, evaluate
from ..data.verbs import ELIGIBILITY_CLAUSE, VERB_TABLE, WRITE_CLAUSE
from ..epistemic import belief_contradicts
from ..harness import probes as P
from ..loop import resolve as _resolve
from ..loop.driver import SeasonDriver, mint_token, resolvable_verbs
from ..queries import world_q
from ..queries.world_q import WorldReader
from ..state import gate as G
from ..state.carriers import Act, Claim, Tenure, Term
from ..state.gate import DETERMINATION, NotYours

SEAT, DUKE, TREASURY = "off_duke", "p_high", "D"
PARTY, OUTSIDER = "p_mid", "p_king"          # inside the duchy (Hh) / outside it (R)
REMIT = ("levy", "open_case", "determine", "issue")


def _world(**fx):
    """`tiny_world` at the given fixture arms, one MATTER barrier run (tick 0)."""
    fixtures = DEFAULT_FIXTURES
    for name, value in fx.items():
        fixtures = fixtures.sweep(name, value)
    w = P.tiny_world(fixtures)
    d = SeasonDriver(w)
    d.matter(mint_token(w, WriteClass.MATTER), [])
    return w, d


def _fold(w, d, *acts):
    """One RESOLVE pass over `acts`, its Events logged as `SeasonDriver.season` logs them."""
    out = d.resolve(mint_token(w, WriteClass.ACTS), list(acts),
                    contest_max_depth=w.fixtures.get("contest_max_depth"))
    w.log.extend(out)
    return out


def _kinds(events):
    return [e.kind for e in events]


def _act(key, verb, via=SEAT, actor=DUKE, **payload):
    return Act(id=key, actor=actor, verb=verb, via=via, payload=payload)


def _levy(key, subject="S", amount=5, **kw):
    return _act(key, "levy", subject=subject, kind="grain", amount=amount, **kw)


def _open(key, subject=PARTY, **kw):
    return _act(key, "open_case", subject=subject, **kw)


def _determine(key, subject=PARTY, **kw):
    return _act(key, "determine", subject=subject, **kw)


def _issue(key, to=PARTY, **kw):
    return _act(key, "issue", subject=to, to=to, **kw)


# A well-formed act of each verb, on a world where it would EXECUTE through the seat -- the base the
# via=None falsifier strips the seat from. `determine` needs its matter docketed first.
_WELL_FORMED = {"levy": _levy, "open_case": _open, "determine": _determine, "issue": _issue}


def _ready(verb, **fx):
    w, d = _world(**fx)
    if verb == "determine":
        assert _kinds(_fold(w, d, _open("setup"))) == ["case.opened"]
    return w, d


def _obliges(w, who=PARTY, seat=SEAT):
    return [t for t in w.tenures if t.kind == "oblige" and t.subject == who and t.object == seat]


# ======================================================================================
# 0 -- THE ROWS: RESOLVABLE, TYPED, KEYED
# ======================================================================================

def test_19_the_four_are_resolvable_typed_and_key_every_failable_clause():
    """All four enter `resolvable_verbs()` -- they were `★`'s *"formed by 17/19/19/17 holders and never
    offered"* -- each by a TYPED cell carrying a `basis` conjunct (the seat) and a keyed refusal for
    exactly its failable clauses: eligibility (all four are `remit:`), each named conjunct, and the
    write (all four write)."""
    rv = resolvable_verbs()
    for verb in REMIT:
        row = VERB_TABLE[verb]
        assert verb in rv, f"{verb} is not resolvable"
        assert row.requires_typed is not None, f"{verb}'s precondition is not typed"
        assert any(getattr(c, "_form", "") == "basis"
                   for c in getattr(row.requires_typed.requirement, "clauses",
                                    (row.requires_typed.requirement,))), f"{verb} reads no seat"
        expected = {ELIGIBILITY_CLAUSE, WRITE_CLAUSE} | set(row.requires_typed.conjuncts())
        assert set(row.refusals_by_clause) == expected, (verb, sorted(row.refusals_by_clause))
        assert set(row.emits_on_refusal) == {k for v in row.refusals_by_clause.values() for k in v}


def test_19_a_flat_row_refuses_exactly_as_before():
    """THE SCHEMA'S CONTROL. A row that did not opt in answers `refusal_for(<anything>)` with its flat
    tuple -- so no refusal outside the four moved by a byte."""
    flat = [r for r in VERB_TABLE.values() if not r.refusals_by_clause]
    assert len(flat) >= 30, len(flat)
    for row in flat:
        for clause in (None, ELIGIBILITY_CLAUSE, WRITE_CLAUSE, "anything"):
            assert row.refusal_for(clause) == row.emits_on_refusal, row.verb


# ======================================================================================
# 1 -- THE PLAN'S FALSIFIER: NONE OF THE FOUR EXECUTES WITH `via=None`
# ======================================================================================

@pytest.mark.parametrize("verb", REMIT)
def test_19_none_of_the_four_executes_with_via_none(verb):
    """The same well-formed act, seated and seatless. Through the seat it EXECUTES (the control);
    with `via=None` it is refused at eligibility -- `remit:` admits only through the seat the act
    names (`_eligible`, `seat_hold`) -- and the refusal is the row's `unauthorized` kind, keyed to the
    eligibility clause."""
    w, d = _ready(verb)
    seated = _fold(w, d, _WELL_FORMED[verb]("seated"))
    assert _kinds(seated) == list(VERB_TABLE[verb].emits), (verb, _kinds(seated))
    w, d = _ready(verb)
    bare = _fold(w, d, _WELL_FORMED[verb]("bare", via=None))
    assert _kinds(bare) == list(VERB_TABLE[verb].refusal_for(ELIGIBILITY_CLAUSE)), _kinds(bare)
    assert not set(_kinds(bare)) & set(VERB_TABLE[verb].emits)


@pytest.mark.parametrize("verb", REMIT)
def test_19_the_basis_conjunct_refuses_via_none_even_past_eligibility(verb, monkeypatch):
    """THE STRUCTURAL HALF, WHICH IS WHAT MAKES THE FALSIFIER THE FORM'S AND NOT ONLY ELIGIBILITY'S.
    Eligibility forced OPEN (`levy`'s `presence:<rung>` alternative is the live case: the day it
    admits, eligibility no longer implies a seat). The `basis` conjunct binds no `via`, reads UNKNOWN,
    and the fold refuses on it -- so the act still does not execute, and the refusal names the SEAT
    (`unauthorized`) through that conjunct's key."""
    monkeypatch.setattr(_resolve, "_eligible", lambda self, w, a, row: True)
    w, d = _ready(verb)
    out = _fold(w, d, _WELL_FORMED[verb]("bare", via=None))
    row = VERB_TABLE[verb]
    assert not set(_kinds(out)) & set(row.emits), (verb, _kinds(out))
    basis = [n for n, c in zip(row.requires_typed.names,
                               getattr(row.requires_typed.requirement, "clauses",
                                       (row.requires_typed.requirement,)))
             if getattr(c, "_form", "") == "basis"][0]
    assert _kinds(out) == list(row.refusal_for(basis)), (verb, _kinds(out))
    # THE VERDICT ITSELF, asked directly: UNKNOWN (never False -- the seat is not known to lack
    # authority, it is absent), and the conjunct that decided it is the `basis` one.
    verdict = evaluate(row.requires_typed, WorldReader(w, DUKE),
                       binding_from_act(_WELL_FORMED[verb]("probe", via=None)))
    assert verdict.value is UNKNOWN and verdict.failed == basis, (verb, verdict)


# ======================================================================================
# 2 -- LEVY: THROUGH THE SEAT, CONSERVED, SCARCE
# ======================================================================================

def test_19_a_levy_executes_with_via_set_and_moves_matter_into_the_seats_treasury():
    """THE OBSERVABLE, *"a `levy` executes with `Act.via` set"* -- and where the matter goes: out of
    the levied rung and into the treasury of the seat exercised (`off_duke`'s rung, `D`), the same
    amount on both sides (the W3 audit's conservation), both rungs named on the success Event."""
    w, d = _world()
    before = {r: dict(w.rungs[r].stores or {}) for r in ("S", TREASURY)}
    act = _levy("lv")
    out = _fold(w, d, act)
    assert _kinds(out) == ["levy.taken"] and act.via == SEAT
    after = {r: dict(w.rungs[r].stores or {}) for r in ("S", TREASURY)}
    assert after["S"]["grain"] == before["S"]["grain"] - 5
    assert after[TREASURY].get("grain", 0) == before[TREASURY].get("grain", 0) + 5
    assert sorted(c.subject for c in out[0].changes) == sorted(["S", TREASURY])


def test_19_two_levies_on_one_larder_in_one_fold_the_second_refuses():
    """THE PLAN'S ADDED FALSIFIER (§27.1, `test_lb3a_two_eaters_cannot_spend_the_same_unit`'s shape):
    a larder holding exactly one levy's worth, two levies in ONE fold -- the first takes it, the second
    reads the world the first left, finds it short, and gets a DIFFERENT Event, keyed to the `stores`
    conjunct, carrying the read that refused it."""
    w, d = _world()
    w.rungs["Hh"].stores = {"grain": 5}
    out = _fold(w, d, _levy("lv1", subject="Hh"), _levy("lv2", subject="Hh"))
    assert sorted(_kinds(out)) == ["levy.refused", "levy.taken"], _kinds(out)
    refused = [e for e in out if e.kind == "levy.refused"][0]
    assert list(VERB_TABLE["levy"].refusal_for("stores")) == ["levy.refused"]
    assert ("stores:grain", 0) in [(o.predicate, o.value) for o in refused.observed], refused.observed
    assert w.rungs["Hh"].stores["grain"] == 0 and w.rungs[TREASURY].stores["grain"] == 5


def test_19_a_levy_outside_the_seats_purview_is_unauthorized_and_says_whose():
    """`04:330`: purview is asked of the SEAT. `R` is above the duchy -- a Duke has no purview upward --
    so the levy refuses on the `authority` conjunct, and the read it carries names the seat."""
    w, d = _world()
    w.rungs["R"].stores = {"grain": 50}
    out = _fold(w, d, _levy("lv", subject="R"))
    assert _kinds(out) == ["levy.unauthorized"]
    assert (f"purview:{SEAT}", False) in [(o.predicate, o.value) for o in out[0].observed]
    assert w.rungs["R"].stores["grain"] == 50, "an unauthorized levy moved matter"


# ======================================================================================
# 3 -- OPEN_CASE: THE DOCKET, AND THE READER BRANCH
# ======================================================================================

def test_19_open_case_puts_the_matter_on_the_docket_and_the_reader_now_sees_it():
    """`21_RECONCILIATION.md` PHASE 2 step 10, whose falsifier is *"the cell still returns UNKNOWN"*.
    Before the act the docket reader answers 0 -- not UNKNOWN -- and after it 1; the case file is drawn
    up at the seat's rung; a second opening of the same matter is refused (it is already before the
    room); a matter outside the seat's purview is `case.unauthorized`."""
    w, d = _world()
    reader = WorldReader(w, DUKE)
    assert reader.read(PARTY, "exists:DocketItem") == 0
    out = _fold(w, d, _open("oc"))
    assert _kinds(out) == ["case.opened"]
    assert reader.read(PARTY, "exists:DocketItem") == 1
    assert world_q.docketed(w, PARTY) == [{"date": None, "matter": PARTY}]
    case = w.records[out[0].changes[0].subject]
    assert case.rung == TREASURY and case.kind == "text" and case.stages, case
    assert _kinds(_fold(w, d, _open("oc2"))) == ["case.refused"]
    assert len(world_q.docketed(w, PARTY)) == 1
    assert _kinds(_fold(w, d, _open("oc3", subject=OUTSIDER))) == ["case.unauthorized"]
    assert world_q.docketed(w, OUTSIDER) == []


def test_19_the_docket_reader_counts_matters_and_never_an_empty_slot():
    """CALENDAR's slot is `{"date": <id>, "matter": None}`. A `None` subject is not docketed, so an empty
    slot is never read as a matter before the room."""
    w, _ = _world()
    w.docket.append({"date": "d_x", "matter": None})
    assert world_q.docketed(w, None) == [] and WorldReader(w, DUKE).read(None, "exists:DocketItem") == 0


# ======================================================================================
# 4 -- DETERMINE: THE DISPOSAL, THE DOCKET, THE QUORUM
# ======================================================================================

def test_19_a_determination_opens_the_disposal_tenure_on_its_subject_via_the_seat(monkeypatch):
    """THE OBSERVABLE, *"a determination opens the disposal Tenure on its subject via the seat"*. The
    edge is an `oblige` OWNED BY THE PARTY on the seat exercised, carrying the term the determination
    declared (T-n; `declared_by` the act), admitted at the gate as `determination` and as nothing else
    -- observed through the real `tenure_write_basis`. The party joins the seat's establishment, and
    the matter leaves the docket."""
    seen = []
    real = G.tenure_write_basis

    def spy(*a, **k):
        b = real(*a, **k)
        seen.append(b)
        return b
    monkeypatch.setattr(G, "tenure_write_basis", spy)
    w, d = _world()
    _fold(w, d, _open("oc"))
    seen.clear()
    out = _fold(w, d, _determine("dt"))
    assert _kinds(out) == ["matter.determined"], _kinds(out)
    edge, = _obliges(w)
    assert (edge.subject, edge.object, edge.live) == (PARTY, SEAT, True)
    assert edge.term == Term(w.tick + w.fixtures.get("oblige_term"), "dt"), edge.term
    assert DETERMINATION in seen, seen
    assert PARTY in world_q.establishment_of(w, SEAT)
    assert world_q.docketed(w, PARTY) == [] and w.docket == [{"date": None, "matter": None}]


def test_19_two_determinations_of_one_matter_in_one_fold_the_second_refuses():
    """The docket's scarcity: the first determination takes the matter off it, so the second reads 0
    on the `docket` conjunct -- one edge, not two."""
    w, d = _world()
    _fold(w, d, _open("oc"))
    out = _fold(w, d, _determine("dt1"), _determine("dt2"))
    assert sorted(_kinds(out)) == ["determine.refused", "matter.determined"], _kinds(out)
    assert len(_obliges(w)) == 1


@pytest.mark.parametrize("quorum", [1, 2, 3])
def test_19_below_quorum_the_determination_is_refused(quorum):
    """THE OBSERVABLE'S SECOND HALF, *"below quorum, `determine.refused`"*, across `H-161`'s sweep.
    `tiny_world`'s bench for `Hh` is ONE person (`p_high`); at the shipped `1` he meets it (the
    control), at `2` and `3` he does not, and the refusal is keyed to the `quorum` conjunct, carrying
    both sides of the comparison. Nothing is stored: the size is read off the live holds."""
    w, d = _ready("determine", bench_quorum=quorum)
    out = _fold(w, d, _determine("dt"))
    if quorum <= 1:
        assert _kinds(out) == ["matter.determined"]
        return
    assert _kinds(out) == list(VERB_TABLE["determine"].refusal_for("quorum")) == ["determine.refused"]
    reads = {o.predicate: o.value for o in out[0].observed}
    assert reads["bench.size"] == 1 and reads["quorum"] == quorum, reads
    assert _obliges(w) == [] and len(world_q.docketed(w, PARTY)) == 1


def test_19_a_determination_needs_a_docketed_person_inside_the_benchs_ground():
    """The other three conjuncts, each against its own refusal. Nothing docketed: `docket` refuses.
    A party outside the duchy (docketed by hand, since no Duke could open that case): the `bench`
    conjunct refuses as the SEAT (`unauthorized`). A matter that is no person: `party` refuses."""
    w, d = _world()
    assert _kinds(_fold(w, d, _determine("dt0"))) == ["determine.refused"]
    w.docket.append({"date": None, "matter": OUTSIDER})
    assert _kinds(_fold(w, d, _determine("dt1", subject=OUTSIDER))) == ["determine.unauthorized"]
    w.docket.append({"date": None, "matter": "S"})
    assert _kinds(_fold(w, d, _determine("dt2", subject="S"))) == ["determine.refused"]
    assert not [t for t in w.tenures if t.kind == "oblige"]


def test_19_the_disposal_declines_a_party_already_bound_to_the_seat():
    """One `oblige` per person and seat (`_req_oblige`'s clause 4, one step over): a party who already
    serves the seat is not bound twice. The precondition cannot spell the negation, so the effect
    declines, keyed to the `write` clause."""
    w, d = _world()
    assert _kinds(_fold(w, d, Act(id="ob", actor=PARTY, verb="oblige",
                                  payload={"subject": SEAT}))) == ["duty.taken"]
    _fold(w, d, _open("oc"))
    out = _fold(w, d, _determine("dt"))
    assert _kinds(out) == list(VERB_TABLE["determine"].refusal_for(WRITE_CLAUSE))
    assert len(_obliges(w)) == 1 and len(world_q.docketed(w, PARTY)) == 1


def test_19_the_disposal_opener_closes_c1s_report():
    """`21_RECONCILIATION.md` C-1's load check, REPORTED by `data/arrangements.py`: *"every row's
    `disposes` kind must name `determine` in `ID-14`'s opener map"*. `arbitration` disposes `oblige` and
    was the report's one entry; `_eff_determine`'s `Tenure(..., "oblige", ...)` is read by the derived
    opener map, so the report is now empty."""
    from ..data.arrangements import arrangements_without_a_disposal_opener
    assert "determine" in _verbs._OPENERS_FROM_EFFECTS["oblige"]
    assert arrangements_without_a_disposal_opener() == []


# ======================================================================================
# 5 -- THE GATE'S EIGHTH BASIS: `determination`
# ======================================================================================

def _bare_open(w, actor, via, party=PARTY, seat=SEAT, key="t_disposal"):
    """A BARE GATE WRITE opening an `oblige` owned by `party` on `seat` -- `_admits` never asked, so
    what refuses is the gate alone."""
    t = Tenure(key, party, seat, "oblige", since=w.tick)
    w.step = Step.RESOLVE                       # `(Tenure, since)` is written at RES only
    return w.write("Tenure", mint_token(w, WriteClass.ACTS), lambda: w.add_tenure(t),
                   record_kind="Tenure", fieldname="since", driver="Act", actor=actor, via=via)


@pytest.mark.parametrize("case", ["no seat", "outside the ground", "no bench grant",
                                  "another seat", "not seated"])
def test_19_the_determination_basis_refuses_each_clause_it_needs(case):
    """EVERY CLAUSE OF `may_determine` HAS A REFUSED TWIN, and the store is put back each time. The
    control (the last line) is the same opening through a seated judge over a party in his ground."""
    w, _ = _world()
    if case == "no seat":
        args = dict(actor=DUKE, via=None)
    elif case == "outside the ground":
        args = dict(actor=DUKE, via=SEAT, party=OUTSIDER)
    elif case == "no bench grant":
        hold = G.seat_hold(w, DUKE, SEAT)
        hold.payload = {"remit_acts": ("issue",)}
        args = dict(actor=DUKE, via=SEAT)
    elif case == "another seat":
        args = dict(actor=DUKE, via=SEAT, seat="off_dicastery")
    else:
        args = dict(actor="p_other", via=SEAT)
    with pytest.raises(NotYours):
        _bare_open(w, **args)
    assert not [t for t in w.tenures if t.id == "t_disposal"], "the refused edge was not put back"
    w2, _ = _world()
    _bare_open(w2, actor=DUKE, via=SEAT)
    assert [t for t in w2.tenures if t.id == "t_disposal"], "control: the lawful disposal was refused"


def test_19_determination_admits_an_opening_only():
    """AUTHORITY TO BIND IS NOT AUTHORITY TO RE-GRADE: an EXISTING `oblige` on the seat, owned by the
    party, changed in any field through the judge's seat, meets no basis -- `determination` asks
    `opened` first."""
    w, _ = _world()
    t = Tenure("t_old", PARTY, SEAT, "oblige", since=w.tick)
    w.add_tenure(t)
    was = Tenure("t_old", PARTY, SEAT, "oblige", since=w.tick)
    t.degree = "Success"
    assert G.tenure_write_basis(w, t, was, DUKE, SEAT, frozenset()) is None
    fresh = Tenure("t_new", PARTY, SEAT, "oblige", since=w.tick)
    assert G.tenure_write_basis(w, fresh, None, DUKE, SEAT, frozenset()) == DETERMINATION
    # A JUDGE DOES NOT BIND HIMSELF -- `may_determine` refuses it, and an `oblige` a man opens on his
    # own behalf is his own act (`T-m`), whatever seat he names: never `determination`. That the
    # occupant does not serve his own seat is `_req_oblige`'s and `_eff_determine`'s refusal, not the
    # gate's (the gate admits any owner's opening of his own non-seat edge).
    own = Tenure("t_own", DUKE, SEAT, "oblige", since=w.tick)
    assert not G.may_determine(w, DUKE, SEAT, DUKE)
    assert G.tenure_write_basis(w, own, None, DUKE, SEAT, frozenset()) == G.T_M


def test_19_judging_set_and_the_gate_read_one_bench():
    """`sits_over` is the one containment test: the persons `judging_set` lists for the party's home
    are exactly the judges `may_determine` admits for that party, over every person in the world."""
    w, _ = _world()
    homes = world_q.home_of(w)
    checked = 0
    for party in sorted(w.persons):
        bench = set(world_q.judging_set(w, homes.get(party), party))
        admitted = {p for p in w.persons for t in w.tenures
                    if t.kind == "hold" and t.subject == p and t.live and t.object in w.offices
                    and G.may_determine(w, p, t.object, party)}
        assert admitted <= bench, (party, admitted, bench)
        assert bench - {party} <= admitted, (party, admitted, bench)
        checked += 1
    assert checked == len(w.persons) >= 5


# ======================================================================================
# 6 -- ISSUE: THE PRECONDITION `15`'s EFFECT WAITED FOR
# ======================================================================================

def test_19_issue_mints_the_dispensation_at_the_seats_rung_for_an_executor_in_its_purview():
    """`15`'s effect, reached: a `dispensation` Record at the issuing seat's rung, addressed to the
    executor. Outside the seat's purview: `issue.unauthorized`. Addressed to a PLACE: `issue.refused`
    on `executors` -- *"scope enumerates executors, not places"*."""
    w, d = _world()
    out = _fold(w, d, _issue("is"))
    assert _kinds(out) == ["dispensation.issued"]
    rec = w.records[out[0].changes[0].subject]
    assert (rec.kind, rec.rung) == ("dispensation", TREASURY)
    assert rec.subject_matter["to"] == [PARTY]
    assert _kinds(_fold(w, d, _issue("is2", to=OUTSIDER))) == ["issue.unauthorized"]
    assert _kinds(_fold(w, d, _issue("is3", to="S"))) == ["issue.refused"]


def test_19_a_writ_naming_several_executors_refuses_rather_than_ending_the_season():
    """r2 §A.3 types the addressee as a LIST; the cell asks about ONE executor. A hand-built writ
    naming two reached `WorldReader.read` with an unhashable subject and raised `TypeError` from
    inside `_admits` -- a crash where a refusal belongs. The reader now answers UNKNOWN, and the
    fold refuses on `executors`. Control: the same writ to one of them executes."""
    w, d = _world()
    two = Act(id="is_two", actor=DUKE, verb="issue", via=SEAT,
              payload={"subject": PARTY, "to": [PARTY, "p_low"]})
    assert _kinds(_fold(w, d, two)) == list(VERB_TABLE["issue"].refusal_for("executors"))
    assert _kinds(_fold(w, d, _issue("is_one"))) == ["dispensation.issued"]


# ======================================================================================
# 7 -- PERSON-SIDE: THE SAME SEAT, ASKED OF A BELIEF
# ======================================================================================

def test_19_a_person_who_learned_the_seat_cannot_reach_stops_forming_it():
    """§F1 clause 4 asks the cell the fold asks, seat included (`exercised_seat` -> `via`). A Duke
    holding `(R, purview:off_duke, False)` -- what a witnessed `levy.unauthorized` deposits -- finds
    his levy of `R` KNOWN-FALSE through that seat; with no seat the conjunct is UNKNOWN and
    contradicts nothing (the control)."""
    w, _ = _world()
    p = w.persons[DUKE]
    p.ledger.append(Claim("c1", DUKE, "R", f"purview:{SEAT}", False, w.tick, "firsthand", 90,
                          "own"))
    row = VERB_TABLE["levy"]
    ops = {"subject": "R", "kind": "grain", "amount": 1}
    assert belief_contradicts(p, row, "R", ops, SEAT)
    assert not belief_contradicts(p, row, "R", ops, None)
    assert not belief_contradicts(p, row, "R", ops, "off_dicastery")


# ======================================================================================
# 8 -- THE LOADER: INVARIANT 4'S PER-CONJUNCT HALF
# ======================================================================================

def _plant(monkeypatch, verb, mutate):
    real = _verbs.load_yaml

    def planted(text):
        doc = real(text)
        if isinstance(doc, dict) and "verbs" in doc:
            for r in doc["verbs"]:
                if r.get("verb") == verb:
                    mutate(r)
        return doc
    monkeypatch.setattr(_verbs, "load_yaml", planted)


@pytest.mark.parametrize("defect, match", [
    ("missing", r"keys no refusal for the failable clause\(s\) \['stores'\]"),
    ("extra", r"keys refusals for \['bribe'\]"),
    ("unnamed", r"EVERY top-level conjunct named"),
    ("flat named", r"keys no refusal to them"),
    ("empty", r"keys an EMPTY refusal"),
])
def test_19_the_loader_refuses_a_keyed_row_that_does_not_key_exactly_its_clauses(monkeypatch, defect,
                                                                                    match):
    """Each defect planted on `levy`'s row, and the load fails naming it. The control is the table
    itself, which loaded to run this file."""
    def mutate(r):
        ref, cell = r["emits_on_refusal"], r["requires_typed"]["all"]
        if defect == "missing":
            ref.pop("stores")
        elif defect == "extra":
            ref["bribe"] = ["levy.refused"]
        elif defect == "unnamed":
            cell[1].pop("conjunct")
            ref.pop("stores")
        elif defect == "flat named":
            r["emits_on_refusal"] = ["levy.refused"]
        else:
            ref["stores"] = []
    _plant(monkeypatch, "levy", mutate)
    with pytest.raises(SystemExit, match=match):
        _verbs._load_verb_table()


def test_19_the_fold_raises_rather_than_emit_an_undeclared_clauses_kind():
    """`refusal_for` on a keyed row and a clause it does not key RAISES -- the loader guaranteed every
    failable clause a kind, so an unkeyed one is a refusal point the fold invented. Emitting the union
    instead would publish kinds for conjuncts that did not fail."""
    from ..gaps import InstrumentDefect
    with pytest.raises(InstrumentDefect):
        VERB_TABLE["levy"].refusal_for("bribe")
