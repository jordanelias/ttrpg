"""Plan position `19` -- U7-remit. `workplans/2026-09-18-governance-settlement-behaviour-plan_part2.md`,
*"19 — INSTRUCTION. The five remit verbs; each gains a predicate reading `via.scope` and an effect on the
G4 contract"* -- four built here (`requisition`, `open_case`, `determine`, `issue`; `establish` is `13f`'s).
COMPLIANCE: `04:120` AX-1 (*"a seat enters through `Act.via`"*) and `04:330` (purview asked of the seat,
never the actor). OBSERVABLE (`21_RECONCILIATION.md:575`, the antagonist-corrected one): *"a
determination opens the disposal Tenure on its subject via the seat; below quorum, `determine.refused`"*,
and *"a `requisition` executes with `Act.via` set"*.

What the position built, each asked of the real fold, the real loader and the real gate:
  * §F.24a form 7, `basis` -- *"a basis lookup on the exercised seat"* -- given its implementation
    (`data/requires.py::Basis`); the seat rides the binding structurally, as the actor does.
  * the keyed `emits_on_refusal:` schema -- `04 §B.13` invariant 4's per-conjunct half, F7 -- with its
    load-time check (`data/verbs.py`) and the fold reading `row.refusal_for(clause)` (`04 §C.4`).
  * the `docket` reader branch (`exists:DocketItem`), and `open_case` putting a matter on the docket.
  * the write gate's EIGHTH basis, `determination` (`state/gate.py::may_determine`).
  * `requisition`'s effect (a conserved move into the seat's treasury), `open_case`'s, `determine`'s; `issue`'s
    (`15`'s) precondition.

THE FALSIFIERS, each with the control one clause away:
  * the plan's own: ANY OF THE FOUR EXECUTING WITH `via=None` -- run twice, through the fold as shipped
    (eligibility refuses) and with eligibility forced open (the `basis` conjunct refuses on its own).
  * the plan's added one: TWO `requisition`s ON ONE LARDER IN ONE FOLD -- the second refuses (§27.1).
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
from ..data.verbs import COUNTERPARTY_CLAUSE, ELIGIBILITY_CLAUSE, VERB_TABLE, WRITE_CLAUSE
from ..epistemic import belief_contradicts
from ..harness import probes as P
from ..loop import resolve as _resolve
from ..loop.driver import SeasonDriver, mint_token, resolvable_verbs
from ..loop.effects_information import PURSUIT_MOVED
from ..queries import world_q
from ..queries.world_q import WorldReader
from ..state import gate as G
from ..state.carriers import Act, Claim, Tenure, Term
from ..state.gate import DETERMINATION, NotYours

SEAT, DUKE, TREASURY = "off_duke", "p_high", "D"
PARTY, OUTSIDER = "p_mid", "p_king"          # inside the duchy (Hh) / outside it (R)
REMIT = ("requisition", "open_case", "determine", "issue")
# v9 SC-03b: `determine` is a CONTESTED act (`contests: a proposition`), so a determination executes at the
# band the judge's roll decides. At the shipped `pool_default` (2) against the shipped obstacle (2) most
# rolls are `Failure` (`matter.undetermined`, nothing opens), and WHICH act id lands where is the seed's
# business. The tests below that need the disposal to OPEN take a STRONG JUDGE -- `pool_default` 30 against
# the same obstacle -- and each such test ASSERTS the band it landed on (`_sentenced`, the `OPENS` checks), so a
# fixture that stopped being strong fails here and does not quietly turn an executes-test into a refusal-test.
JUDGE = {"pool_default": 30}
OPENS = ("Overwhelming", "Success")


def _world(**fx):
    """`tiny_world` at the given fixture arms, one MATTER barrier run (tick 0)."""
    fixtures = DEFAULT_FIXTURES
    for name, value in fx.items():
        fixtures = fixtures.sweep(name, value)
    w = P.tiny_world(fixtures)
    # ⚠ RE-RECORDED AT PLAN POSITION IN-10: `issue`'s cell gained a `terms` conjunct -- the issuer
    # holds a claim on what the writ is about (`own_ledger` of `subject`, `verb_table.yaml`) -- so the
    # Duke knows the two parties these writs name. Nothing else here reads an `exists:Person` claim.
    for who in (PARTY, OUTSIDER):
        w.persons[DUKE].ledger.append(Claim(f"c_knows_{who}", DUKE, who, "exists:Person", 1, 0,
                                            "firsthand", 100, "own"))
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


def _requisition(key, subject="S", amount=5, **kw):
    return _act(key, "requisition", subject=subject, kind="grain", amount=amount, **kw)


def _open(key, subject=PARTY, **kw):
    return _act(key, "open_case", subject=subject, **kw)


def _determine(key, subject=PARTY, **kw):
    return _act(key, "determine", subject=subject, **kw)


def _issue(key, to=PARTY, **kw):
    return _act(key, "issue", subject=to, to=to, **kw)


# A well-formed act of each verb, on a world where it would EXECUTE through the seat -- the base the
# via=None falsifier strips the seat from. `determine` needs its matter docketed first.
_WELL_FORMED = {"requisition": _requisition, "open_case": _open, "determine": _determine, "issue": _issue}


def _ready(verb, **fx):
    if verb == "determine":
        fx = {**JUDGE, **fx}
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
        # PLAN POSITION `14`: a row naming a second party keys the fold's `counterparty` clause too
        # (`determine`'s party, `issue`'s executor).
        if row.counterparty:
            expected.add(COUNTERPARTY_CLAUSE)
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
    row = VERB_TABLE[verb]
    # A contested row's success kinds are its BAND's (`emits_at`): the strong judge lands on a band that
    # opens, and the control asserts which, so it cannot pass on a `Failure`. v9 SC-02 `22b` step 24: the
    # band also declares `pursuit.moved`, EARNED only when the judge's own pursuits move -- `tiny_world`'s
    # Duke holds none, so it is not published (asserted, so the subtraction cannot hide a move).
    want = list(row.emits_at(seated[0].degree)) if row.contests else list(row.emits)
    if verb == "determine":
        assert not w.persons[DUKE].pursuits, w.persons[DUKE].pursuits
        want = [k for k in want if k != PURSUIT_MOVED]
    assert _kinds(seated) == want, (verb, _kinds(seated))
    assert not row.contests or seated[0].degree in OPENS, (verb, seated[0].degree)
    w, d = _ready(verb)
    bare = _fold(w, d, _WELL_FORMED[verb]("bare", via=None))
    assert _kinds(bare) == list(VERB_TABLE[verb].refusal_for(ELIGIBILITY_CLAUSE)), _kinds(bare)
    assert not set(_kinds(bare)) & set(VERB_TABLE[verb].emits)


@pytest.mark.parametrize("verb", REMIT)
def test_19_the_basis_conjunct_refuses_via_none_even_past_eligibility(verb, monkeypatch):
    """THE STRUCTURAL HALF, WHICH IS WHAT MAKES THE FALSIFIER THE FORM'S AND NOT ONLY ELIGIBILITY'S.
    Eligibility forced OPEN (`requisition`'s `presence:<rung>` alternative is the live case: the day it
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
# 2 -- REQUISITION: THROUGH THE SEAT, CONSERVED, SCARCE
# ======================================================================================

def test_19_a_requisition_executes_with_via_set_and_moves_matter_into_the_seats_treasury():
    """THE OBSERVABLE, *"a `requisition` executes with `Act.via` set"* -- and where the matter goes: out of
    the requisitioned rung and into the treasury of the seat exercised (`off_duke`'s rung, `D`), the same
    amount on both sides (the W3 audit's conservation), both rungs named on the success Event."""
    w, d = _world()
    before = {r: dict(w.rungs[r].stores or {}) for r in ("S", TREASURY)}
    act = _requisition("rq")
    out = _fold(w, d, act)
    assert _kinds(out) == ["requisition.taken"] and act.via == SEAT
    after = {r: dict(w.rungs[r].stores or {}) for r in ("S", TREASURY)}
    assert after["S"]["grain"] == before["S"]["grain"] - 5
    assert after[TREASURY].get("grain", 0) == before[TREASURY].get("grain", 0) + 5
    assert sorted(c.subject for c in out[0].changes) == sorted(["S", TREASURY])


def test_19_two_requisitions_on_one_larder_in_one_fold_the_second_refuses():
    """THE PLAN'S ADDED FALSIFIER (§27.1, `test_lb3a_two_eaters_cannot_spend_the_same_unit`'s shape):
    a larder holding exactly one requisition's worth, two requisitions in ONE fold -- the first takes it, the second
    reads the world the first left, finds it short, and gets a DIFFERENT Event, keyed to the `stores`
    conjunct, carrying the read that refused it."""
    w, d = _world()
    w.rungs["Hh"].stores = {"grain": 5}
    out = _fold(w, d, _requisition("rq1", subject="Hh"), _requisition("rq2", subject="Hh"))
    assert sorted(_kinds(out)) == ["requisition.refused", "requisition.taken"], _kinds(out)
    refused = [e for e in out if e.kind == "requisition.refused"][0]
    assert list(VERB_TABLE["requisition"].refusal_for("stores")) == ["requisition.refused"]
    assert ("stores:grain", 0) in [(o.predicate, o.value) for o in refused.observed], refused.observed
    assert w.rungs["Hh"].stores["grain"] == 0 and w.rungs[TREASURY].stores["grain"] == 5


def test_19_a_requisition_outside_the_seats_purview_is_unauthorized_and_says_whose():
    """`04:330`: purview is asked of the SEAT. `R` is above the duchy -- a Duke has no purview upward --
    so the requisition refuses on the `authority` conjunct, and the read it carries names the seat."""
    w, d = _world()
    w.rungs["R"].stores = {"grain": 50}
    out = _fold(w, d, _requisition("rq", subject="R"))
    assert _kinds(out) == ["requisition.unauthorized"]
    assert (f"purview:{SEAT}", False) in [(o.predicate, o.value) for o in out[0].observed]
    assert w.rungs["R"].stores["grain"] == 50, "an unauthorized requisition moved matter"


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
    # v9 SC-03a: the item names its arrangement and petition -- `None` for an act declaring neither.
    assert world_q.docketed(w, PARTY) == [{"date": None, "matter": PARTY,
                                           world_q.DOCKET_ARRANGEMENT: None,
                                           world_q.DOCKET_PETITION: None}]
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
    w, d = _world(**JUDGE)
    _fold(w, d, _open("oc"))
    seen.clear()
    out = _fold(w, d, _determine("dt"))
    assert _kinds(out) == ["matter.determined"], _kinds(out)
    edge, = _obliges(w)
    assert (edge.subject, edge.object, edge.live) == (PARTY, SEAT, True)
    # v9 SC-03b: the edge carries the band the contest decided (H-162's producer), the Event's own.
    assert edge.degree == out[0].degree and edge.degree in OPENS, (edge.degree, out[0].degree)
    assert edge.term == Term(w.tick + w.fixtures.get("oblige_term"), "dt"), edge.term
    assert DETERMINATION in seen, seen
    assert PARTY in world_q.establishment_of(w, SEAT)
    assert world_q.docketed(w, PARTY) == [] and w.docket == [{"date": None, "matter": None,
                                                              world_q.DOCKET_ARRANGEMENT: None,
                                                              world_q.DOCKET_PETITION: None}]


def test_19_two_determinations_of_one_matter_in_one_fold_the_second_refuses():
    """The docket's scarcity: the first determination takes the matter off it, so the second reads 0
    on the `docket` conjunct -- one edge, not two."""
    w, d = _world(**JUDGE)
    _fold(w, d, _open("oc"))
    out = _fold(w, d, _determine("dt1"), _determine("dt2"))
    assert sorted(_kinds(out)) == ["determine.refused", "matter.determined"], _kinds(out)
    assert len(_obliges(w)) == 1
    # AND IT IS THE DOCKET THAT REFUSED, NOT THE EFFECT'S ONE-EDGE-PER-PAIR DECLINE (which would also
    # refuse a second binding): the refusal's last read -- the conjunct that decided it -- is the
    # docket, now empty.
    refused, = [e for e in out if e.kind == "determine.refused"]
    assert (refused.observed[-1].predicate, refused.observed[-1].value) == ("exists:DocketItem", 0)


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
    conjunct refuses as the SEAT (`determine.refused` since SC-03b flattened the kind). A matter that is no person: `party` refuses."""
    w, d = _world()
    assert _kinds(_fold(w, d, _determine("dt0"))) == ["determine.refused"]
    w.docket.append({"date": None, "matter": OUTSIDER})
    # v9 SC-03b: the seat's refusal answers in the row's one kind now; the READ that refused it is the
    # `bench` conjunct's, which is what tells it from the docket's (observed, not the kind).
    out = _fold(w, d, _determine("dt1", subject=OUTSIDER))
    assert _kinds(out) == ["determine.refused"]
    assert (out[0].observed[-1].predicate, out[0].observed[-1].value) == (f"bench:{SEAT}", False), out[0].observed
    w.docket.append({"date": None, "matter": "S"})
    assert _kinds(_fold(w, d, _determine("dt2", subject="S"))) == ["determine.refused"]
    assert not [t for t in w.tenures if t.kind == "oblige"]


def test_19_the_disposal_declines_a_party_already_bound_to_the_seat():
    """One `oblige` per person and seat (`_req_oblige`'s clause 4, one step over): a party who already
    serves the seat is not bound twice. The precondition cannot spell the negation, so the effect
    declines, keyed to the `write` clause."""
    w, d = _world(**JUDGE)
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


def test_19_determination_opens_only_a_disposed_kind_and_closes_only_a_restraint():
    """(Named for the basis as it stands since v9 SC-03a, which widened it from "an opening only": it
    OPENS a disposed kind and CLOSES a `detain`/`ban`, and re-grades nothing. The assertions below are
    the re-grade half, unchanged; `test_sc03a_the_determination_basis_*` are the widened halves.)
    AUTHORITY TO BIND IS NOT AUTHORITY TO RE-GRADE: an EXISTING `oblige` on the seat, owned by the
    party, RE-GRADED (its `degree` changed) through the judge's seat, meets no basis --
    `determination` asks `opened` first. ⚠ NARROWED FROM "changed in any field" (found by the
    second sub-batch's layer-conformance critic, 2026-09-30): a `term` pushed later on this same
    edge through this same seat IS admitted, under `renewal` (`gate.py::may_renew`) -- a different
    basis, not this one, and this test does not exercise it."""
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
    # occupant does not serve his own seat is `_req_oblige`'s refusal and, for `determine`, the
    # `bench` conjunct's (`may_determine`, `determine.refused`) -- the fold's `counterparty`
    # clause names the same case but is never reached on that row, and `_eff_determine`'s own
    # self-check was already dead -- not the gate's (the gate admits any owner's opening of his own
    # non-seat edge).
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
    holding `(R, purview:off_duke, False)` -- what a witnessed `requisition.unauthorized` deposits -- finds
    his requisition of `R` KNOWN-FALSE through that seat; with no seat the conjunct is UNKNOWN and
    contradicts nothing (the control)."""
    w, _ = _world()
    p = w.persons[DUKE]
    p.ledger.append(Claim("c1", DUKE, "R", f"purview:{SEAT}", False, w.tick, "firsthand", 90,
                          "own"))
    row = VERB_TABLE["requisition"]
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
    ("twice", r"no two alike"),
    ("nested", r"inside a nested `all:`"),
])
def test_19_the_loader_refuses_a_keyed_row_that_does_not_key_exactly_its_clauses(monkeypatch, defect,
                                                                                    match):
    """Each defect planted on `requisition`'s row, and the load fails naming it. The control is the table
    itself, which loaded to run this file."""
    def mutate(r):
        ref, cell = r["emits_on_refusal"], r["requires_typed"]["all"]
        if defect == "missing":
            ref.pop("stores")
        elif defect == "extra":
            ref["bribe"] = ["requisition.refused"]
        elif defect == "unnamed":
            cell[1].pop("conjunct")
            ref.pop("stores")
        elif defect == "flat named":
            r["emits_on_refusal"] = ["requisition.refused"]
        elif defect == "twice":
            cell[1]["conjunct"] = cell[0]["conjunct"]
        elif defect == "nested":
            inner = {k: v for k, v in cell[0].items() if k != "conjunct"}
            cell[0] = {"all": [dict(inner, conjunct="inner"),
                               {"form": "existence", "of": "subject", "kind": "Rung"}],
                       "conjunct": "authority"}
        else:
            ref["stores"] = []
    _plant(monkeypatch, "requisition", mutate)
    with pytest.raises(SystemExit, match=match):
        _verbs._load_verb_table()


def test_19_the_fold_raises_rather_than_emit_an_undeclared_clauses_kind():
    """`refusal_for` on a keyed row and a clause it does not key RAISES -- the loader guaranteed every
    failable clause a kind, so an unkeyed one is a refusal point the fold invented. Emitting the union
    instead would publish kinds for conjuncts that did not fail."""
    from ..gaps import InstrumentDefect
    with pytest.raises(InstrumentDefect):
        VERB_TABLE["requisition"].refusal_for("bribe")


# ======================================================================================
# 9 -- v9 SC-03a (#453 §10.4 steps 2b/3, K-53/K-55): THE DOCKET NAMES ITS ARRANGEMENT;
#      `detain` AND `ban`, THEIR READERS, AND THE WIDENED `determination` BASIS
# ======================================================================================
# The rows are picked BY WHAT THEY DISPOSE, never by name: which of the four seeded rows disposes
# `detain` and which `ban` is SC-03a's [ASSUMPTION] (`arrangements.yaml`'s own comments), and these
# tests observe the mechanism, whichever row carries the kind.

from ..data.arrangements import ARRANGEMENTS                      # noqa: E402
from ..data.rosters import BAN_KIND, DETAIN_KIND, RESTRAINT_KINDS  # noqa: E402
from ..loop import sides as _sides                                # noqa: E402
from ..state.carriers import Office, Record                       # noqa: E402

PETITION = "rec_petition"


def _row_disposing(kind):
    return next(name for name, row in sorted(ARRANGEMENTS.items()) if row["disposes"] == kind)


def _petition(w, rid=PETITION, kind="petition"):
    """A petition Record the matter rose from -- planted, as the docket tests plant their items: what
    is under test is what `open_case` writes, not how a petition reaches the bench."""
    w.records[rid] = Record(rid, "Hh", kind,
                            subject_matter={"terms": PARTY, "to": DUKE, "from": "Hh"}
                            if kind == "petition" else None)
    return rid


def _edges(w, kind, who=PARTY, seat=SEAT):
    return [t for t in w.tenures if t.kind == kind and t.subject == who and t.object == seat]


def _sentenced(kind):
    """A world where `PARTY` is docketed under the row that disposes `kind` and then determined."""
    w, d = _world(**JUDGE)
    row = _row_disposing(kind)
    assert _kinds(_fold(w, d, _open("oc", arrangement=row, petition=_petition(w)))) == ["case.opened"]
    out = _fold(w, d, _determine("dt"))
    assert _kinds(out) == ["matter.determined"] and out[0].degree in OPENS, out   # the judge is still strong
    return w, d


def test_sc03a_an_open_case_under_a_seeded_arrangement_names_that_row_and_the_petition():
    """#453 §10.4 step 2b's observable: the docket item names the arrangement row it is heard under
    and the petition it rose from. Controls, each one clause away: an act naming no arrangement (every
    computed `open_case`) dockets both as `None`; an arrangement no row carries, or a "petition" that
    is a Record of another kind, is refused before anything is docketed (`case.refused`)."""
    row = _row_disposing(BAN_KIND)
    w, d = _world()
    out = _fold(w, d, _open("oc", arrangement=row, petition=_petition(w)))
    assert _kinds(out) == ["case.opened"], _kinds(out)
    item, = world_q.docketed(w, PARTY)
    assert item[world_q.DOCKET_ARRANGEMENT] == row and item[world_q.DOCKET_PETITION] == PETITION, item
    assert world_q.docketed_under(w, PARTY) == {row}
    w, d = _world()
    assert _kinds(_fold(w, d, _open("oc"))) == ["case.opened"]
    item, = world_q.docketed(w, PARTY)
    assert item[world_q.DOCKET_ARRANGEMENT] is None and item[world_q.DOCKET_PETITION] is None, item
    w, d = _world()
    assert _kinds(_fold(w, d, _open("oc", arrangement="no_such_row"))) == ["case.refused"]
    assert _kinds(_fold(w, d, _open("oc2", arrangement=row,
                                    petition=_petition(w, "rec_text", "text")))) == ["case.refused"]
    assert world_q.docketed(w, PARTY) == []


def test_sc03a_open_case_declines_an_arrangement_it_cannot_dispose_and_a_malformed_operand():
    """COR2/COR6: a docket item naming a row whose `disposes:` is not a Tenure kind (a `Record`, or
    `none`) would wedge the matter -- `determine` declines it forever and `docketed` blocks a second
    `open_case`. So `open_case` DECLINES it up front (`case.refused`), and the matter stays openable
    (CONTROL: the same matter opened with no arrangement executes). A list-valued arrangement or a
    dict-valued petition (unhashable) is declined, never raised.
    Mutation: drop the `disposes` test in `_eff_open_case` (red: the Record row dockets); drop the
    `isinstance` guards (red: `TypeError` out of the fold)."""
    w, d = _world()
    record_rows = [n for n, r in sorted(ARRANGEMENTS.items()) if r["disposes"] not in G.DISPOSABLE_KINDS]
    assert record_rows, "fixture: no seeded row disposes a non-Tenure kind"
    for i, row in enumerate(record_rows):
        assert _kinds(_fold(w, d, _open(f"oc{i}", arrangement=row))) == ["case.refused"], row
        assert world_q.docketed(w, PARTY) == [], row
    assert _kinds(_fold(w, d, _open("oc_list", arrangement=["x"]))) == ["case.refused"]
    assert _kinds(_fold(w, d, _open("oc_dict", petition={"a": 1}))) == ["case.refused"]
    assert world_q.docketed(w, PARTY) == []
    assert _kinds(_fold(w, d, _open("oc_ok"))) == ["case.opened"], "the matter was wedged"


def test_sc03a_a_determination_under_disposes_ban_opens_a_ban_and_release_is_refused_on_it():
    """#453 §10.4 step 3's observable, and §8.3's reason for the kind: the bench opens the kind the
    docketed row `disposes:` -- a `ban`, owned by the party, on the seat exercised, and no `oblige` --
    and the party's own `release` of it is refused (`RELEASABLE_KINDS` excludes it). CONTROL: the same
    party's `release` of an `oblige` (the undeclared disposal) closes it -- the convict's price C-1
    ruled -- so the refusal is the kind's and not the actor's."""
    w, d = _sentenced(BAN_KIND)
    ban, = _edges(w, BAN_KIND)
    assert ban.live and not _edges(w, "oblige"), w.tenures
    assert ban.degree in OPENS, ban     # the grade rides the `ban` literal (`_disposal`)
    out = _fold(w, d, Act(id="rl", actor=PARTY, verb="release", payload={"subject": SEAT}))
    assert _kinds(out) == ["release.refused"], _kinds(out)
    assert ban.live
    w, d = _ready("determine")
    assert _kinds(_fold(w, d, _determine("dt"))) == ["matter.determined"]
    assert _kinds(_fold(w, d, Act(id="rl", actor=PARTY, verb="release",
                                  payload={"subject": SEAT}))) == ["tenure.closed"]


def test_sc03a_move_is_refused_while_a_detain_is_live():
    """#453 §10.4 step 3's second observable: a person holding a live `detain` does not travel
    (`move` -> `travel.blocked`) and does not settle (`migrate` -> its `write` refusal). CONTROL: the
    same journey by the same person, in a world where he was not sentenced, executes."""
    w, d = _world()
    assert _kinds(_fold(w, d, Act(id="mv0", actor=PARTY, verb="move",
                                  payload={"to": "S"}))) == ["travel.moved"]
    w, d = _sentenced(DETAIN_KIND)
    detain, = _edges(w, DETAIN_KIND)
    assert detain.live and detain.degree in OPENS, detain   # the grade rides the `detain` literal
    legs = [t for t in w.tenures if t.subject == PARTY and t.kind == "contain" and t.live]
    assert _kinds(_fold(w, d, Act(id="mv", actor=PARTY, verb="move",
                                  payload={"to": "S"}))) == ["travel.blocked"]
    assert _kinds(_fold(w, d, Act(id="mg", actor=PARTY, verb="migrate", payload={"to": "S"}))) \
        == list(VERB_TABLE["migrate"].refusal_for(WRITE_CLAUSE))
    assert [t for t in w.tenures if t.subject == PARTY and t.kind == "contain" and t.live] == legs


def test_sc03a_a_ban_does_not_stop_travel_and_a_second_sentence_of_one_kind_is_declined():
    """Two claims the `detain` test above cannot make, each with its mutation. (a) A `ban` holder
    TRAVELS (`travel.moved`): `restrained` is asked of one kind, so the custody refusal is `detain`'s
    and not any restraint's. Mutation: `world_q.restrained` matches `t.kind in RESTRAINT_KINDS`, any restraint (red here). (b) A second
    `open_case` + `determine` under the SAME `ban` row on the same seat and party is declined on the
    `write` clause: the effect's one-live-edge-per-kind test reads the DISPOSED kind, not `oblige`.
    Mutation: `_eff_determine`'s `t.kind == kind` back to `t.kind == "oblige"` (red: a second ban
    opens, `matter.determined`)."""
    w, d = _sentenced(BAN_KIND)
    assert _kinds(_fold(w, d, Act(id="mv", actor=PARTY, verb="move",
                                  payload={"to": "S"}))) == ["travel.moved"]
    row = _row_disposing(BAN_KIND)
    assert _kinds(_fold(w, d, _open("oc2", arrangement=row, petition=_petition(w)))) == ["case.opened"]
    assert _kinds(_fold(w, d, _determine("dt2"))) == list(VERB_TABLE["determine"].refusal_for(WRITE_CLAUSE))
    assert len(_edges(w, BAN_KIND)) == 1 and not _edges(w, "oblige")


def test_sc03a_the_determination_basis_closes_a_restraint_and_nothing_else():
    """THE POSITION'S FALSIFIER, at the gate. A determination may CLOSE a `detain` or a `ban` on the
    judging seat (the control) -- and a planted closure of a `hold` through the same seat by the same
    judge is REFUSED (`NotYours`, store put back), as is a closure of an `oblige` (the obligee-side
    closer D-5 refused). And a NON-JUDGING actor through the same seat is refused both ways
    (`may_determine`)."""
    w, _ = _world()
    w.step = Step.RESOLVE
    checked = 0
    for kind in sorted(RESTRAINT_KINDS):
        t = Tenure(f"t_{kind}", PARTY, SEAT, kind, since=w.tick)
        w.add_tenure(t)
        was = Tenure(f"t_{kind}", PARTY, SEAT, kind, since=w.tick)
        t.until = w.tick
        assert G.tenure_write_basis(w, t, was, DUKE, SEAT, frozenset()) == DETERMINATION, kind
        assert G.tenure_write_basis(w, t, was, "p_other", SEAT, frozenset()) is None, kind
        t.until = None
        checked += 1
    assert checked == 2
    # The planted `hold` is ON THE JUDGING SEAT ITSELF -- the one object the clause's `t.object == via`
    # test lets through, so it is the closure only the KIND test can refuse (a hold elsewhere would be
    # refused by the object test and observe nothing about the kind).
    # RE-RECORDED (v9 IN-12 step 6, `seize`): a closure of another person's `hold` on a RECORD is no longer
    # refused by the gate -- it is admitted under the new `seizure` basis, by this same seat (granted
    # `issue`, purview over the holder's home), and the warrant that licenses it is the effect's to read.
    # So the planted Record hold leaves the `NotYours` loop and the test asserts the basis that admits it:
    # `seizure`, never `determination` (a bench closes a restraint and nothing else), and not for a
    # non-seated actor.
    _petition(w, "rec_held")
    held = Tenure("t_held", PARTY, "rec_held", "hold", since=w.tick)
    w.add_tenure(held)
    was_held = Tenure("t_held", PARTY, "rec_held", "hold", since=w.tick)
    held.until = w.tick
    assert G.tenure_write_basis(w, held, was_held, DUKE, SEAT, frozenset()) == G.SEIZURE
    assert G.tenure_write_basis(w, held, was_held, "p_other", SEAT, frozenset()) is None
    held.until = None
    seated = Tenure("t_seated", PARTY, SEAT, "hold", since=w.tick)
    owed = Tenure("t_owed", PARTY, SEAT, "oblige", since=w.tick)
    for t in (seated, owed):
        w.add_tenure(t)
        with pytest.raises(NotYours):
            w.write("Tenure", mint_token(w, WriteClass.ACTS),
                    lambda t=t: setattr(t, "until", w.tick), record_kind="Tenure",
                    fieldname="until", driver="Act", actor=DUKE, via=SEAT)
        assert t.live, f"the refused closure of the {t.kind} was not put back"
    assert not G.may_determine(w, "p_other", SEAT, PARTY)
    with pytest.raises(NotYours):
        _bare_open(w, actor="p_other", via=SEAT, key="t_x")


def test_sc03a_the_determination_basis_opens_each_disposed_kind_and_no_other():
    """The OPENING side: every Tenure kind an arrangement row disposes (`DISPOSABLE_KINDS`) is admitted
    as `determination` through the judging seat; a kind no row disposes (`commit`) is not. The C-1
    report stays empty: `_eff_determine` constructs each disposed kind literally."""
    from ..data.arrangements import arrangements_without_a_disposal_opener
    w, _ = _world()
    assert RESTRAINT_KINDS | {G.UNDECLARED_DISPOSAL} <= G.DISPOSABLE_KINDS
    for kind in sorted(G.DISPOSABLE_KINDS):
        fresh = Tenure(f"t_{kind}", PARTY, SEAT, kind, since=w.tick)
        assert G.tenure_write_basis(w, fresh, None, DUKE, SEAT, frozenset()) == DETERMINATION, kind
        assert "determine" in _verbs._OPENERS_FROM_EFFECTS[kind], kind
    assert G.tenure_write_basis(w, Tenure("t_c", PARTY, SEAT, "commit", since=w.tick), None,
                                DUKE, SEAT, frozenset()) is None
    assert arrangements_without_a_disposal_opener() == []


def test_sc03a_the_warrant_basis_opens_a_detain_for_a_seat_granted_dispatch_over_the_prisoner():
    """K-52's `warrant` basis, at the gate (its producer, `arrest`, is #453 step 5's): a `detain` on a
    seat, opened by a seated holder whose grant carries `dispatch`, for a person the seat's purview
    reaches, is admitted as `warrant`. Each conjunct has its refused twin: no `dispatch` in the grant,
    a prisoner outside the purview, an unseated actor, an object that is not a seat."""
    w, _ = _world()

    def basis(actor=DUKE, via=SEAT, prisoner=PARTY, obj="off_dicastery", kind=DETAIN_KIND):
        return G.tenure_write_basis(w, Tenure("t_w", prisoner, obj, kind, since=w.tick),
                                    None, actor, via, frozenset())
    assert basis() == G.WARRANT
    assert basis(prisoner=OUTSIDER) is None
    assert basis(actor="p_other") is None
    assert basis(obj="Hh") is None
    # Each of these is a mutation's twin (run red once locally, SC-03a fix pass):
    #   a warrant opens a `detain` and no other kind -- drop `t.kind == "detain"` and an `oblige` on a
    #   prisoner in purview is admitted as `warrant`;
    assert basis(kind="oblige") is None
    #   a warrant is an OPENING -- drop `opened` and a closure of a live detain is admitted;
    live = Tenure("t_live", PARTY, "off_dicastery", DETAIN_KIND, since=w.tick)
    shut = Tenure("t_live", PARTY, "off_dicastery", DETAIN_KIND, since=w.tick, until=w.tick)
    assert G.tenure_write_basis(w, shut, live, DUKE, SEAT, frozenset()) is None
    #   and a man does not arrest himself -- the owner (T-m) is refused a restraint of his own
    #   (COR4), and `may_warrant` refuses the prisoner who is the actor.
    assert basis(prisoner=DUKE) is None
    G.seat_hold(w, DUKE, SEAT).payload = {"remit_acts": ("issue", "determine")}
    assert basis() is None


def test_sc03a_an_owner_can_neither_open_nor_close_his_own_restraint_at_the_gate():
    """COR4: `T-m` (the owner's discretion) does not reach a `detain` or a `ban`. A prisoner closing his
    own custody or opening one for himself through `World.write` is refused (`NotYours`, store put
    back), by any `via` -- and the judging seat's closure of the same edge still passes (the control).
    Mutation: drop `t.kind not in RESTRAINT_KINDS` from `T-m` (red: the owner's own closure admitted)."""
    w, _ = _world()
    w.step = Step.RESOLVE
    checked = 0
    for kind in sorted(RESTRAINT_KINDS):
        t = Tenure(f"t_{kind}", PARTY, SEAT, kind, since=w.tick)
        w.add_tenure(t)
        for via in (None, SEAT):
            with pytest.raises(NotYours):
                w.write("Tenure", mint_token(w, WriteClass.ACTS),
                        lambda t=t: setattr(t, "until", w.tick), record_kind="Tenure",
                        fieldname="until", driver="Act", actor=PARTY, via=via)
            assert t.live, f"the owner's own closure of his {kind} was not put back"
            mine = Tenure(f"t_mine_{kind}_{via}", PARTY, SEAT, kind, since=w.tick)
            with pytest.raises(NotYours):
                w.write("Tenure", mint_token(w, WriteClass.ACTS), lambda m=mine: w.add_tenure(m),
                        record_kind="Tenure", fieldname="since", driver="Act", actor=PARTY, via=via)
            assert mine not in w.tenures, f"the owner's own opening of a {kind} was not put back"
        w.write("Tenure", mint_token(w, WriteClass.ACTS), lambda t=t: setattr(t, "until", w.tick),
                record_kind="Tenure", fieldname="until", driver="Act", actor=DUKE, via=SEAT)
        assert not t.live, f"control: the judging seat's closure of the {kind} was refused"
        checked += 1
    assert checked == 2


def test_sc03a_a_ban_holder_is_refused_service_and_seating():
    """The `ban`'s two readers: `oblige` refuses its holder service (`duty.refused`), and `confer`
    declines to seat him (`confer`'s refusal). CONTROLS: the same two acts for an unbanned party
    execute."""
    def world(banned):
        w, d = _world()
        w.offices["off_reeve"] = Office("off_reeve", "Reeve", "S", ["issue"], faction="Crown",
                                        conferral="appointed", revocation="rung_above_same_faction")
        if banned:
            w.add_tenure(Tenure("t_ban", PARTY, "off_dicastery", BAN_KIND, since=w.tick))
        return w, d
    confer = Act(id="cf", actor=DUKE, verb="confer", payload={"office": "off_reeve", "to": PARTY},
                 via=SEAT)
    oblige = Act(id="ob", actor=PARTY, verb="oblige", payload={"subject": SEAT})
    w, d = world(banned=False)
    assert "tenure.opened" in _kinds(_fold(w, d, confer))
    w, d = world(banned=False)
    assert _kinds(_fold(w, d, oblige)) == ["duty.taken"]
    w, d = world(banned=True)
    out = _kinds(_fold(w, d, confer))
    assert "tenure.opened" not in out and set(out) <= set(VERB_TABLE["confer"].emits_on_refusal), out
    assert not [t for t in w.tenures if t.object == "off_reeve" and t.live]
    w, d = world(banned=True)
    assert _kinds(_fold(w, d, oblige)) == ["duty.refused"]


def test_sc03a_a_mustered_army_excludes_a_person_held_in_custody(monkeypatch):
    """The `detain`'s third reader: `sides_of`'s army is the muster at the actor's settlement less
    every person in custody. `mustered` is stubbed to a known list so the read under test is the
    exclusion alone; CONTROL: with nobody detained the list passes through unchanged."""
    w, _ = _world()
    monkeypatch.setattr(_sides, "mustered", lambda *a, **k: [DUKE, PARTY, "p_low"])
    march = Act(id="mr", actor=DUKE, verb="march", payload={"subject": "S"}, via=SEAT)
    claimants, _, _ = _sides.sides_of(w, march, "S", "a field")
    assert claimants == [DUKE, PARTY, "p_low"], claimants
    w.add_tenure(Tenure("t_det", PARTY, "off_dicastery", DETAIN_KIND, since=w.tick))
    claimants, _, _ = _sides.sides_of(w, march, "S", "a field")
    assert claimants == [DUKE, "p_low"], claimants


# ======================================================================================
# 9 -- v9 IN-49 `requisition`: THE REQUISITIONED RUNG (H-163 limit 3), THROUGH THE REAL FORMATION
# ======================================================================================
# `subject` bound the question's single referent, so a computed `requisition` aimed at whatever the seat
# holder was asked about -- a person, a Record, a rung his seat does not reach, an empty larder --
# and was refused there (H-163 limit 3). The channel is `queries/world_q.py::larders_in_purview`:
# the Rungs his OWN ledger names, holding the fixtures' requisition of their matter, inside the purview of a
# seat of his granting the remit act (`data/verbs.py::RUNG_REMIT_ACTS`), stamped on the question he
# answers as `Rung`; `requisition` declares `referent_class: Rung`. Every act below is COMPUTED --
# `questions_for`, the real `opening_set`, the real `pack_scenes` -- and folded by the real RESOLVE.
# Hand-built worlds only; nothing here asserts anything about the seed-0 realm (v9 §0.5).
# The common setup stocks `R` (the realm, outside the Duke's purview) as well as `S`, so the three
# controls differ from the executing world by the rung he was told of (`R` for `S`; `D` for `S`,
# which control 3 also stocks -- two changes), or by `S`'s grain (emptied).
# MUTATIONS, run at the build 2026-10-16. Each went RED, then was restored byte-exact and went GREEN:
#   * `larders_in_purview`'s `held > 0 and held >= amount and` deleted (the stores condition) -> the
#     empty-larder control RED (a computed requisition forms on the empty larder);
#   * `larders_in_purview`'s `any(purview_reaches(...))` replaced by `True` -> the outside-purview
#     control RED (the realm is stamped as a larder he may requisition);
#   * `larders_in_purview`'s `r != s.rung and` deleted (the treasury clause) -> the own-treasury
#     control RED (a computed requisition forms on `D`, the seat's own rung);
#   * `requisition`'s `referent_class: Rung` deleted from `verb_table.yaml` -> the plain-referent test RED
#     (a requisition forms on the clerk he was asked about) and the executing test RED (no `Rung` row is
#     exercised through a seat, so nothing is stamped);
#   * `_derive_operand`'s `and on_referent` dropped from the shortfall branch -> the operand test RED
#     (the requisition of `S` carries the realm's salt dearth).

from ..decision import assemble as _assemble
from ..decision import options as _options
from ..decision.choose import pack_scenes as _pack
from ..state.carriers import Question as _Question
from ..state.ids import H as _H

STOCK = 40


def _larder_world(told_of="S", grain_at_s=STOCK):
    """`tiny_world` with the realm `R` stocked too (outside `off_duke`'s purview, which is `D`'s
    subtree), `S`'s grain set to `grain_at_s`, and the Duke told of `told_of` by the deposit a
    witnessed `stores.changed` leaves (planted, so the cause is controlled)."""
    w, d = _world()
    w.rungs["R"].stores = {"grain": STOCK}
    w.rungs["S"].stores["grain"] = grain_at_s
    w.persons[DUKE].ledger.append(Claim(f"c_told_{told_of}", DUKE, told_of, "stores.changed",
                                        True, w.tick, "firsthand", 100, "own"))
    return w, d


def _computed_requisitions(w, q=None):
    """The `requisition` acts the Duke forms -- on `q`, by default the question he answers first, which
    the classed referents ride -- through the real `opening_set`, packed by the real `pack_scenes`."""
    p = w.persons[DUKE]
    if q is None:
        qs = world_q.questions_for(w, p, since=(w.tick, 0))
        if not qs:
            return []
        q = qs[0]
    cands = [c for c in _options.opening_set(p, _assemble(p, q, 12), q, w.fixtures)
             if c.verb == "requisition"]
    mint = lambda who, verb, subj: _H(w.world_seed, w.tick, who, f"act:{verb}:{subj}")
    return [a for s in _pack(p, cands, 99, w.fixtures, mint) for a in s.acts]


def test_in49_a_computed_requisition_of_a_larder_his_seat_reaches_executes_with_via_set():
    """THE OBSERVABLE U9 NAMED, *"a `requisition` executes with `Act.via` set"*, FROM A COMPUTED ACT. The
    Duke is told of `S` (his own town, inside `D`): `larders_in_purview` offers exactly `S`, the
    computed `requisition` carries `subject = S` and `via = off_duke`, and the real fold executes it --
    `requisition.taken` in `w.log`, the fixtures' amount out of `S` and into the seat's treasury `D`."""
    w, d = _larder_world()
    assert world_q.larders_in_purview(w, w.persons[DUKE]) == ("S",)
    (lv,) = _computed_requisitions(w)
    assert lv.payload.get("subject") == "S" and lv.via == SEAT, (lv.payload, lv.via)
    amount = w.fixtures.get("default_transfer_amount")
    assert lv.payload.get("kind") == w.fixtures.get("default_store_kind") == "grain"
    assert lv.payload.get("amount") == amount and amount > 0
    before_s, before_d = w.rungs["S"].stores["grain"], (w.rungs["D"].stores or {}).get("grain", 0)
    assert _kinds(_fold(w, d, lv)) == ["requisition.taken"]
    assert [e for e in w.log if e.kind == "requisition.taken"], "requisition.taken never reached w.log"
    assert w.rungs["S"].stores["grain"] == before_s - amount
    assert w.rungs["D"].stores["grain"] == before_d + amount


def test_in49_a_rung_outside_the_seats_purview_raises_no_requisition():
    """CONTROL 1, ONE CHANGE: told of the stocked realm `R` instead of `S`. No seat of his reaches
    `R` (a Duke has no purview over the realm above him), so it is no larder he may requisition, nothing
    is stamped, and no `requisition` forms -- asserted on the formed acts AND by folding whatever forms."""
    w, d = _larder_world(told_of="R")
    assert w.rungs["R"].stores["grain"] == STOCK          # anti-vacuity: the larder is full
    assert world_q.larders_in_purview(w, w.persons[DUKE]) == ()
    acts = _computed_requisitions(w)
    assert [a.payload.get("subject") for a in acts] == [], acts


def test_in49_the_seats_own_treasury_raises_no_requisition():
    """CONTROL 3, ONE CHANGE: told of `D`, the seat's own rung, stocked. Purview is reflexive, but
    `D` is the treasury a requisition pays INTO, and a requisition of it into itself moves nothing (`_eff_requisition`'s
    G4 `NoOpReceipt`, `requisition.refused` on the `write` clause -- every computed corpus requisition before the
    clause). So it is no larder he may requisition and no `requisition` forms on it."""
    w, d = _larder_world(told_of=TREASURY)
    w.rungs[TREASURY].stores = {"grain": STOCK}
    assert G.purview_reaches(w, w.offices[SEAT], TREASURY)   # anti-vacuity: inside the purview
    acts = _computed_requisitions(w)
    assert [a.payload.get("subject") for a in acts] == [], acts
    assert world_q.larders_in_purview(w, w.persons[DUKE]) == ()


def test_in49_an_empty_larder_raises_no_requisition():
    """CONTROL 2, ONE CHANGE: `S` holds no grain. An empty larder is an occasion for nothing --
    the `requisition.refused` H-163 limit 3 measured -- so nothing is stamped and no `requisition` forms."""
    w, d = _larder_world(grain_at_s=0)
    acts = _computed_requisitions(w)
    assert [a.payload.get("subject") for a in acts] == [], acts
    assert world_q.larders_in_purview(w, w.persons[DUKE]) == ()


def test_in49_a_requisition_never_forms_on_a_plain_referent():
    """THE PARTITION: a question whose plain referent is the clerk (`p_mid`), with nothing stamped,
    forms no `requisition` -- before the class it formed one on him and the fold refused it. CONTROL: the
    same question with `S` riding it as a `Rung` forms the requisition on `S` and nowhere else."""
    w, _ = _world()
    plain = _Question("q:claim:c_knows_p_mid", "claim_landed", (PARTY,), f"c_knows_{PARTY}")
    assert _computed_requisitions(w, q=plain) == []
    classed = _Question(plain.id, plain.source, plain.referents, plain.about,
                        classes=(("S", "Rung"),))
    assert [a.payload.get("subject") for a in _computed_requisitions(w, q=classed)] == ["S"]


def test_in49_a_claim_the_question_is_about_does_not_set_a_classed_levys_matter():
    """THE OPERAND RULE, ONE PARTITION OVER (IN-45's document gate, extended to the shortfall and
    stores readers). The question he answers is about a `shortfall:salt` claim of 5 on `R`, and `S`
    rides it as a `Rung`: the requisition of `S` carries the fixtures' grain and amount -- what
    `larders_in_purview` stocked it by -- not the realm's salt dearth. AND ON THE OVERLAP (B-K close,
    COR 4 / LOG 1): a question about `S` itself, `S` riding it as a `Rung` too, still gives the requisition
    the fixtures' values -- the row is classed, so the claim does not re-aim it (this assertion read
    `("salt", 5)` before, pinning the mismatch)."""
    w, _ = _world()
    p = w.persons[DUKE]
    p.ledger.append(Claim("c_short_R", DUKE, "R", "shortfall:salt", 5, w.tick, "firsthand", 100,
                          "own"))
    p.ledger.append(Claim("c_short_S", DUKE, "S", "shortfall:salt", 5, w.tick, "firsthand", 100,
                          "own"))
    q = _Question("q:claim:c_short_R", "claim_landed", ("R",), "c_short_R",
                  classes=(("S", "Rung"),))
    (lv,) = _computed_requisitions(w, q=q)
    assert (lv.payload.get("kind"), lv.payload.get("amount")) == (
        w.fixtures.get("default_store_kind"), w.fixtures.get("default_transfer_amount")), lv.payload
    own = _Question("q:claim:c_short_S", "claim_landed", ("S",), "c_short_S",
                    classes=(("S", "Rung"),))
    assert [(a.payload.get("kind"), a.payload.get("amount"))
            for a in _computed_requisitions(w, q=own)] == [
        (w.fixtures.get("default_store_kind"), w.fixtures.get("default_transfer_amount"))]


def _formed(w, verb, q):
    """The operands of the `verb` Candidates the Duke forms on `q` (the real `opening_set`)."""
    p = w.persons[DUKE]
    return [c.operands for c in _options.opening_set(p, _assemble(p, q, 12), q, w.fixtures)
            if c.verb == verb]


def test_in49_a_claim_about_the_stamped_rung_itself_does_not_set_the_levys_matter():
    """THE OVERLAP (B-K close, COR 4 / LOG 1): the head question is about a `shortfall:salt` claim of
    5 on `S`, and `S` is ALSO stamped `Rung` -- the common case, since the claim about the larder
    ranks first. The classed `requisition` of `S` carries the fixtures' grain and amount, what the stamp
    checked. CONTROL, one change of ROW: the plain-row `transfer` on the same question and the same
    rung still reads the claim (19d's `salt`, 5) -- so the rule is the row's class, not the id's.
    MUTATION (seen red, 2026-10-16): `on_referent = q is None or subject in q.referents` restored in
    `_derive_operand` -> the requisition reads `("salt", 5)`."""
    w, _ = _world()
    w.persons[DUKE].ledger.append(Claim("c_short_S", DUKE, "S", "shortfall:salt", 5, w.tick,
                                        "firsthand", 100, "own"))
    q = _Question("q:claim:c_short_S", "claim_landed", ("S",), "c_short_S",
                  classes=(("S", "Rung"),))
    fx = (w.fixtures.get("default_store_kind"), w.fixtures.get("default_transfer_amount"))
    assert fx != ("salt", 5)                                     # anti-vacuity
    assert [(o.get("kind"), o.get("amount")) for o in _formed(w, "requisition", q)] == [fx]
    assert ("salt", 5) in [(o.get("kind"), o.get("amount")) for o in _formed(w, "transfer", q)
                           if o.get("to") == "S"]


def test_in49_a_stores_claim_about_the_stamped_rung_does_not_set_the_levys_kind():
    """`store_kind_of`'s guard made falsifiable: the head question is about a `stores:salt` level on
    `S`, `S` stamped `Rung`. The classed `requisition` carries the fixtures' kind; CONTROL, one change of
    row: the plain `transfer` on the same question reads `salt`. MUTATION (seen red, 2026-10-16):
    `if on_referent` dropped from `_derive_operand`'s `kind` branch -> the requisition carries `salt`."""
    w, _ = _world()
    w.persons[DUKE].ledger.append(Claim("c_st_S", DUKE, "S", "stores:salt", 30, w.tick,
                                        "firsthand", 100, "own"))
    q = _Question("q:claim:c_st_S", "claim_landed", ("S",), "c_st_S", classes=(("S", "Rung"),))
    assert w.fixtures.get("default_store_kind") != "salt"        # anti-vacuity
    assert [o.get("kind") for o in _formed(w, "requisition", q)] == [w.fixtures.get("default_store_kind")]
    assert "salt" in [o.get("kind") for o in _formed(w, "transfer", q) if o.get("to") == "S"]


# ======================================================================================
# 10 -- v9 SC-03b (#453 §10.4 step 4): `determine` IS A CONTESTED ACT; `Tenure.degree` GAINS ITS WRITER
# ======================================================================================
# Two observations, kept apart (CLAUDE.md §0.1 pt 3). STATIC: what the loader reads of the DECLARED
# `writes:` (the row, the matrix cell, invariant 2 in both directions) -- it shows no producer. RUNTIME:
# a seeded contested determination actually leaves `Tenure.degree` on the opened edge, at the band the
# contest decided, and at `Failure` opens nothing.

import dataclasses                                                # noqa: E402
from ..data.arrangements import DEGREE_BANDS as BANDS             # noqa: E402
from ..data.matrix import matrix_row                              # noqa: E402
from ..manifest import resolve as _manifest_resolve               # noqa: E402


def test_sc03b_determine_is_a_contested_row_keyed_on_the_four_ladder_bands():
    row = VERB_TABLE["determine"]
    assert row.contests == "a proposition", row.contests
    prize = _manifest_resolve("contest", "a proposition")
    assert prize is not None and prize["provider"] == "social_contest", prize
    assert prize["module_entry"] == "social_contest.roll", prize
    assert set(row.writes_by_degree) == set(row.emits_by_degree) == BANDS
    # THE FALSIFIER'S DECLARED HALVES, literal: Failure writes nothing; Partial declares what the effect does,
    # the opening graded `Partial` -- the same three pairs as Success (`writes_note`; the gate admits a degree
    # only on an edge the write opens, so `Tenure.degree` alone at Partial was unbuildable).
    # v9 SC-02 `22b` step 24: the two MOVING bands add the determiner's own `Person.pursuits` (and its
    # `pursuit.moved`) after the three disposal pairs; `Partial`, the held matter, moves nothing.
    assert row.writes_at("Failure") == () and row.writes_at("Partial") == tuple(
        p for p in row.writes_at("Success") if p != "Person.pursuits")
    assert row.writes_at("Success")[-1] == row.writes_at("Overwhelming")[-1] == "Person.pursuits"
    assert "Tenure.degree" in row.writes_at("Success") and "Tenure.degree" in row.writes_at("Overwhelming")
    assert row.writes_at("Success")[0] == "Tenure.since"        # the opening is the first pair, the effect's
    assert row.emits_at("Failure") == ("matter.undetermined",)
    assert row.emits_at("Partial") == ("matter.determined",)
    assert all(row.emits_at(b) == ("matter.determined", PURSUIT_MOVED) for b in ("Overwhelming", "Success"))
    # ONE refusal kind, because a contested row may key only one (the party-gap refusal emits the union).
    assert row.emits_on_refusal == ("determine.refused",), row.emits_on_refusal
    assert {k for v in row.refusals_by_clause.values() for k in v} == {"determine.refused"}
    assert "determine" in resolvable_verbs()


def test_sc03b_static_the_matrix_cell_has_no_unproduced_declaration_and_the_loader_enforces_both_ways(
        monkeypatch):
    """STATIC. The shipped cell carries no `unproduced:` (the verb declares the write). Each direction of
    invariant 2 is then PLANTED and the load refuses: the stale declaration kept after a verb writes the
    cell, and the orphan -- the verb stops declaring the write and the cell has no declaration. That the
    load is green shows the DECLARED writes agree; it does not show a producer (the runtime test does)."""
    cell = matrix_row("Tenure", "degree")
    assert not cell.unproduced, cell.unproduced
    monkeypatch.setitem(_verbs.MATRIX, ("Tenure", "degree"),
                        dataclasses.replace(cell, unproduced="H-162: kept after the verb declares it"))
    with pytest.raises(SystemExit, match=r"declares `unproduced:` and a verb writes it"):
        _verbs._load_verb_table()
    monkeypatch.undo()

    def drop(r):
        r["writes"] = {b: [p for p in ps if p != "Tenure.degree"] for b, ps in r["writes"].items()}
    _plant(monkeypatch, "determine", drop)
    with pytest.raises(SystemExit, match=r"\(Tenure, degree\) is written at RES and no verb writes it"):
        _verbs._load_verb_table()


def _determined(w, d, key):
    """One `determine` act folded; the Event it made and the party's disposal edges after it."""
    out = _fold(w, d, _determine(key, subject=PARTY))
    assert len(out) == 1, _kinds(out)
    return out[0], _obliges(w)


def test_sc03b_runtime_a_seeded_contested_determination_leaves_the_degree_on_the_opened_edge():
    """RUNTIME. Swept over two judges (the shipped `pool_default` and a strong one) and forty act ids each,
    every band of the ladder occurs, and each is observed against what the row declares for it:
      * Overwhelming / Success -- the edge is opened, owned by the party on the seat, and carries
        `degree == the band == the Event's degree`; the matter leaves the docket; `matter.determined`.
      * Partial -- `matter.determined` and the edge carries `degree == Partial` (the row declares the same
        three pairs as Success, `writes_note`: the gate admits a degree only on an edge the write opens).
      * Failure -- `matter.undetermined`, NO edge, the matter still docketed, no change on the Event.
    CONTROL (assert-that-asserted): all four bands were seen, and the counts add up to the folds made."""
    seen: dict = {}
    for pool in (2, 12):
        for i in range(40):
            w, d = _ready("determine", pool_default=pool)
            ev, edges = _determined(w, d, f"sc03b_{pool}_{i}")
            band = ev.degree
            assert band in BANDS, band
            seen[band] = seen.get(band, 0) + 1
            if band == "Failure":
                assert ev.kind == "matter.undetermined" and not edges and not ev.changes, (ev.kind, edges)
                assert len(world_q.docketed(w, PARTY)) == 1
                assert not [t for t in w.tenures if t.degree is not None]
            else:
                assert ev.kind == "matter.determined", (band, ev.kind)
                edge, = edges
                assert edge.degree == band and edge.live, (band, edge)
                assert world_q.docketed(w, PARTY) == []
    assert sum(seen.values()) == 80, seen
    assert set(seen) == BANDS, seen          # all four occurred, so no band's branch went unobserved


def test_sc03b_runtime_an_undetermined_matter_can_be_heard_again():
    """The Failure band opens nothing, so the matter is not lost: the same bench determines it again on a
    later act (a different draw) and the disposal opens then. Control: an act id that lands on `Failure`
    at the shipped judge is found first, so the second fold is a real re-hearing, not a first one."""
    for i in range(200):
        w, d = _ready("determine", pool_default=2)
        ev, edges = _determined(w, d, f"sc03b_again_{i}")
        if ev.degree == "Failure":
            break
    else:
        pytest.fail("fixture: no Failure draw in 200 act ids")
    assert not edges and len(world_q.docketed(w, PARTY)) == 1
    reheard = 0
    for j in range(200):
        ev2, edges2 = _determined(w, d, f"sc03b_again_{i}_retry{j}")
        if ev2.degree != "Failure":
            edge, = edges2
            assert edge.degree == ev2.degree and world_q.docketed(w, PARTY) == []
            reheard += 1
            break
    assert reheard == 1, "the matter was never disposed of on a re-hearing"


def test_sc03b_a_judge_under_one_die_is_refused_not_a_crash_and_opens_nothing():
    """S27.4 (`Ob > 2 x Pool`) reached by a contested `determine`: a judge whose pool is under 1D comes
    back as the row's one refusal kind with NO degree -- never an aborted season -- exactly as `speak`'s
    does (`test_sc01_speak.py`), and the matter stays docketed. CONTROL: pool 1 resolves to a band."""
    for pool, refused in ((0, True), (1, False)):  # `_pool_of` int()s the pool, so 0.5 would be the 0 arm
        w, d = _ready("determine", pool_default=pool)
        out = _fold(w, d, _determine(f"zpool{pool}"))
        assert bool(out) and (_kinds(out) == ["determine.refused"]) is refused, (pool, _kinds(out))
        if refused:
            assert out[0].degree is None and not _obliges(w) and len(world_q.docketed(w, PARTY)) == 1
        else:
            assert out[0].degree in BANDS
