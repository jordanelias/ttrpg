"""v9 IN-48 -- `H-108`'s DELEGATION HALF: A SEAT EXERCISED BY SOMEONE WHO DOES NOT HOLD IT.

The carrier is a `tenure_kinds` member, `delegate : Person -> Office` (`data/rosters.py::DELEGATE_KIND`),
opened by the seat's sitting holder through that same seat -- a hand-built `confer` whose `office` is its
own `via`, naming the delegate on `to` -- and admitted at the write gate under the `delegation` basis
(`state/gate.py::may_delegate`). `seat_hold` returns it as a second way to sit in a seat, but only while
the seat has a live `hold` (dormancy; the holder's own `hold` preferred). `purview_reaches` never reads it
(`sworn_to` filters on `oblige`), so it is never vassalage. Design and its decisions:
`proposals/2026-10-14-in48-delegation-carrier.md` (reference, `CLAUDE.md` §0.05; its §5 is this file).

THE FALSIFIERS, numbered as the design's §5, each asked of the real fold, the real MATTER barrier and the
real gate:
   1. a delegate's act `via` the seat is admitted, and after the edge closes it is refused, at the fold and
      at the gate -- three arms: the term at MATTER, the delegate's `release`, the holder's `revoke` with `to`;
   2. a person with neither a `hold` nor a `delegate` on the seat is refused through it (control: with the
      edge he is admitted);
   3. opening a delegation leaves the principal's `hold` live, same id, and names no `tenure.closed`;
      revoking it closes no `hold`; a `revoke` with `office == via` and no `to` refuses as before;
   4. no self-delegation (`NotYours`); the holder's write through the seat is admitted under `delegation`;
   5. no delegation by a delegate, and no dismissal of a co-delegate by one;
   6. not vassalage: a delegate holding ground outside the seat brings none of it under the seat;
   7. a declared `acts` subset, bounded by the live remit at opening and snapshot after it;
   8. dormant: the principal's death leaves the edge live and unread; a later holder revives and revokes it;
   9. a `confer` seating the delegate in the same seat closes his `delegate` edge on it under `conferral`;
  10. no bench seat: a delegate is not in `judging_set` and may not `determine`;
  11. the DECLINE: no computed `confer` reaches `_req_confer` with `office == via` (an entry count over four
      seeded seasons, `checked >= N` asserted first), and `opening_set` forms none on a told-of own seat;
  12. the load and the ends: `release.domain` must carry `delegate`, the derived openers are `{confer}`,
      `add_tenure` refuses a `delegate` edge that is not `Person -> Office`;
  13. THE EXIT: in `build_realm(0)` plus one build-placed `delegate` edge, the delegate's COMPUTED act
      executes `via` the seat while the principal holds it, and after the holder's hand-built `revoke` the
      same act refuses.
"""

from __future__ import annotations

import pytest

from ..data import verbs as _verbs
from ..data.matrix import Step, WriteClass
from ..decision import assemble
from ..decision.choose import pack_scenes
from ..decision.options import opening_set
from ..gaps import Forbidden
from ..harness import populated as POP
from ..loop import predicates as _preds
from ..loop.driver import SeasonDriver, mint_token
from ..queries import world_q
from ..state import gate as G
from ..state.carriers import Act, Claim, Office, Question, Tenure
from ..state.gate import NotYours, purview_reaches, seat_hold
from ..state.ids import H, ROOT

from .test_g3_not_yours import _gov_world, _hold

KIND = "delegate"          # the roster member, spelled as the data spells it
BASIS = "delegation"       # the gate basis's name
_RUNG_ABOVE = "rung_above_same_faction"


# ------------------------------------------------------------------------------------------------
# fixture: `_gov_world` -- `p_king` holds `off_crown` (King, R) and `off_mayor` (Mayor, S), both granting
# confer/revoke; `p_high` holds `off_duke` (Duke, D; issue/determine/confer/dispatch/convene); `p_other`
# holds `off_duke2` (D2, outside D); `off_reeve` is vacant at S. Plus a second vacant seat, `off_reeve2`.
# ------------------------------------------------------------------------------------------------

def _world():
    w, d = _gov_world()
    w.offices["off_reeve2"] = Office("off_reeve2", "Reeve", "S", ["issue"], faction="Crown",
                                     conferral="appointed", revocation=_RUNG_ABOVE)
    return w, d


def _fold(w, d, *acts):
    w.step = Step.RESOLVE
    out = d.resolve(mint_token(w, WriteClass.ACTS), list(acts),
                    contest_max_depth=w.fixtures.get("contest_max_depth"))
    w.log.extend(out)
    return [e.kind for e in out]


def _delegate(w, d, holder, seat, to, aid="dl", **extra):
    return _fold(w, d, Act(id=aid, actor=holder, verb="confer", via=seat,
                           payload={"office": seat, "to": to, **extra}))


def _confer(w, d, actor, via, office, to, aid):
    return _fold(w, d, Act(id=aid, actor=actor, verb="confer", via=via,
                           payload={"office": office, "to": to}))


def _revoke(w, d, actor, via, office, aid="rv", **extra):
    return _fold(w, d, Act(id=aid, actor=actor, verb="revoke", via=via,
                           payload={"office": office, **extra}))


def _edge(w, who, seat):
    return next((t for t in w.tenures
                 if t.kind == KIND and t.subject == who and t.object == seat and t.live), None)


def _refused(kinds):
    return "tenure.opened" not in kinds and any(k.endswith(".refused") for k in kinds)


def _gate_open(w, actor, via, owner, seat, kind="hold"):
    """A bare gate write opening `owner`'s `kind` edge on `seat`, as `actor` through `via`."""
    nt = Tenure(H(w.world_seed, w.tick, owner, f"gate:{kind}:{seat}:{actor}"), owner, seat, kind, w.tick)
    w.step = Step.RESOLVE
    w.write("Tenure", mint_token(w, WriteClass.ACTS), lambda: w.add_tenure(nt),
            record_kind="Tenure", fieldname="until", driver="Act", actor=actor, via=via)
    return nt


def _season(w, d):
    w.tick += 1
    d.matter(mint_token(w, WriteClass.MATTER), [])
    w.step = Step.RESOLVE


# ================================================================================================
# 1 -- ADMITTED WHILE THE EDGE LIVES, REFUSED AFTER IT ENDS: TERM, RELEASE, REVOKE
# ================================================================================================

@pytest.mark.parametrize("arm", ["term", "release", "revoke"])
def test_in48_1_a_delegate_is_admitted_while_the_edge_lives_and_refused_after_it_ends(arm):
    w, d = _world()
    extra = {"term": 1} if arm == "term" else {}
    kinds = _delegate(w, d, "p_king", "off_crown", "p_mid", **extra)
    assert "tenure.opened" in kinds, kinds
    e = _edge(w, "p_mid", "off_crown")
    assert e is not None and seat_hold(w, "p_mid", "off_crown") is e
    # the delegate's act through the seat: admitted at the fold, the gate admitting its write
    kinds = _confer(w, d, "p_mid", "off_crown", "off_reeve", "p_low", "a_live")
    assert "tenure.opened" in kinds and _hold(w, "off_reeve").subject == "p_low", kinds
    if arm == "term":
        _season(w, d)
    elif arm == "release":
        assert _fold(w, d, Act(id="rl", actor="p_mid", verb="release",
                               payload={"subject": "off_crown"})) == ["tenure.closed"]
    else:
        assert "tenure.closed" in _revoke(w, d, "p_king", "off_crown", "off_crown", to="p_mid")
    assert not e.live, f"{arm}: the delegate edge did not close"
    assert seat_hold(w, "p_mid", "off_crown") is None
    assert _hold(w, "off_crown").subject == "p_king", f"{arm}: the principal's hold moved"
    kinds = _confer(w, d, "p_mid", "off_crown", "off_reeve2", "p_low", "a_after")
    assert _refused(kinds) and _hold(w, "off_reeve2") is None, (arm, kinds)
    with pytest.raises(NotYours):
        _gate_open(w, "p_mid", "off_crown", "p_low", "off_reeve2")


# ================================================================================================
# 2 -- NEITHER A HOLD NOR THE CARRIER: REFUSED; WITH THE CARRIER: ADMITTED
# ================================================================================================

def test_in48_2_a_person_with_neither_a_hold_nor_a_delegation_is_refused_through_the_seat():
    w, d = _world()
    kinds = _confer(w, d, "p_other", "off_crown", "off_reeve", "p_low", "x1")
    assert _refused(kinds) and _hold(w, "off_reeve") is None, kinds
    with pytest.raises(NotYours):
        _gate_open(w, "p_other", "off_crown", "p_low", "off_reeve")
    # control: the same person, delegated, is admitted through the same seat
    assert "tenure.opened" in _delegate(w, d, "p_king", "off_crown", "p_other")
    kinds = _confer(w, d, "p_other", "off_crown", "off_reeve", "p_low", "x2")
    assert "tenure.opened" in kinds and _hold(w, "off_reeve").subject == "p_low", kinds


# ================================================================================================
# 3 -- A DELEGATION NEVER TOUCHES THE PRINCIPAL'S HOLD
# ================================================================================================

def test_in48_3_opening_and_revoking_a_delegation_leave_the_principals_hold_alone():
    w, d = _world()
    h = _hold(w, "off_crown")
    hid = h.id
    kinds = _delegate(w, d, "p_king", "off_crown", "p_mid")
    assert kinds == ["tenure.opened"], kinds
    assert _hold(w, "off_crown") is h and h.live and h.id == hid
    e = _edge(w, "p_mid", "off_crown")
    kinds = _revoke(w, d, "p_king", "off_crown", "off_crown", to="p_mid")
    assert kinds == ["tenure.closed"] and not e.live, kinds
    assert _hold(w, "off_crown") is h and h.live
    # a `revoke` of the seat it is exercised through, naming no `to`: refused, exactly as before
    kinds = _revoke(w, d, "p_king", "off_crown", "off_crown", aid="rv_no_to")
    assert _refused(kinds) and h.live, kinds


# ================================================================================================
# 4 -- NO SELF-DELEGATION; THE HOLDER'S WRITE IS ADMITTED UNDER `delegation`
# ================================================================================================

@pytest.mark.parametrize("via", [None, "off_crown"])
def test_in48_4_a_person_opening_his_own_delegation_is_not_yours(via):
    w, _ = _world()
    with pytest.raises(NotYours):
        _gate_open(w, "p_mid", via, "p_mid", "off_crown", kind=KIND)
    assert _edge(w, "p_mid", "off_crown") is None


def test_in48_4_the_holders_write_through_the_seat_is_admitted_under_delegation():
    w, _ = _world()
    probe = Tenure("t_probe", "p_mid", "off_crown", KIND, w.tick)
    assert G.tenure_write_basis(w, probe, None, "p_king", "off_crown", frozenset()) == BASIS
    assert G.tenure_write_basis(w, probe, None, "p_king", "off_mayor", frozenset()) is None
    nt = _gate_open(w, "p_king", "off_crown", "p_mid", "off_crown", kind=KIND)
    assert nt.live and seat_hold(w, "p_mid", "off_crown") is nt


# ================================================================================================
# 5 -- A DELEGATE CANNOT DELEGATE FURTHER, NOR DISMISS A CO-DELEGATE
# ================================================================================================

def test_in48_5_no_delegation_and_no_dismissal_by_a_delegate():
    w, d = _world()
    assert "tenure.opened" in _delegate(w, d, "p_king", "off_crown", "p_mid")
    kinds = _delegate(w, d, "p_mid", "off_crown", "p_low", aid="dl_sub")
    assert _refused(kinds) and _edge(w, "p_low", "off_crown") is None, kinds
    with pytest.raises(NotYours):
        _gate_open(w, "p_mid", "off_crown", "p_low", "off_crown", kind=KIND)
    assert "tenure.opened" in _delegate(w, d, "p_king", "off_crown", "p_low", aid="dl_co")
    co = _edge(w, "p_low", "off_crown")
    kinds = _revoke(w, d, "p_mid", "off_crown", "off_crown", to="p_low")
    assert _refused(kinds) and co.live, kinds


# ================================================================================================
# 6 -- NOT VASSALAGE
# ================================================================================================

def test_in48_6_a_delegate_brings_none_of_his_own_ground_under_the_delegated_seat():
    w, d = _world()
    duke = w.offices["off_duke"]
    assert not purview_reaches(w, duke, "D2"), "fixture: the duke reaches D2 already"
    assert "tenure.opened" in _delegate(w, d, "p_high", "off_duke", "p_other")
    assert _edge(w, "p_other", "off_duke") is not None
    assert not purview_reaches(w, duke, "D2"), "a delegation was read as vassalage"
    # control: his live `oblige` to the same seat IS vassalage (IN-40's clause)
    kinds = _fold(w, d, Act(id="ob", actor="p_other", verb="oblige", payload={"subject": "off_duke"}))
    assert kinds == ["duty.taken"], kinds
    assert purview_reaches(w, duke, "D2")


# ================================================================================================
# 7 -- A DECLARED SUBSET, BOUNDED BY THE LIVE REMIT AT OPENING, SNAPSHOT AFTER
# ================================================================================================

def test_in48_7_a_declared_subset_is_bounded_at_opening_and_kept_after():
    w, d = _world()
    # `off_mayor` grants confer/revoke; `dispatch` is not in its remit, so the intersection drops it
    kinds = _delegate(w, d, "p_king", "off_mayor", "p_mid", acts=["revoke", "dispatch"])
    assert "tenure.opened" in kinds, kinds
    e = _edge(w, "p_mid", "off_mayor")
    assert e.granted_acts == ("revoke",), e.granted_acts
    assert e.seat_rung == "S"
    # an act outside the subset is refused through the seat
    kinds = _confer(w, d, "p_mid", "off_mayor", "off_reeve", "p_low", "sub_out")
    assert _refused(kinds) and _hold(w, "off_reeve") is None, kinds
    # a later `establish` narrowing the seat's remit re-stamps the holder, never the delegate
    kinds = _fold(w, d, Act(id="est", actor="p_high", verb="establish", via="off_duke",
                            payload=dict(office="off_mayor", post="Mayor", rung="S", remit=["confer"],
                                         faction="Crown", conferral="appointed",
                                         revocation=_RUNG_ABOVE)))
    assert "remit.changed" in kinds, kinds
    assert _hold(w, "off_mayor").granted_acts == ("confer",)
    assert e.granted_acts == ("revoke",), "the bound held only at opening: the delegate was re-stamped"


# ================================================================================================
# 8 -- DORMANT WHILE THE SEAT IS VACANT; A LATER HOLDER REVIVES AND REVOKES IT
# ================================================================================================

def test_in48_8_the_principals_death_leaves_the_delegation_live_and_dormant():
    w, d = _world()
    assert "tenure.opened" in _delegate(w, d, "p_king", "off_crown", "p_mid")
    e = _edge(w, "p_mid", "off_crown")
    # A4, the seat's knowledge goes with its exercise: a live delegate is among the seat's governors
    assert "p_mid" in world_q.governors_of(w, "D"), world_q.governors_of(w, "D")
    w.step = Step.MATTER
    w.write("Tenure", mint_token(w, WriteClass.MATTER), lambda: w.remove_person("p_king"),
            record_kind="Tenure", fieldname="until", driver="Event",
            caused_person_exists="p_king", emits="tenure.closed", subject="p_king",
            causes=[ROOT])
    assert _hold(w, "off_crown") is None and e.live, "the edge closed with the principal"
    assert seat_hold(w, "p_mid", "off_crown") is None, "a dormant delegation seated its delegate"
    assert "p_mid" not in world_q.governors_of(w, "D"), "a dormant delegate still governs"
    kinds = _confer(w, d, "p_mid", "off_crown", "off_reeve", "p_low", "dormant")
    assert _refused(kinds) and _hold(w, "off_reeve") is None, kinds
    # a later holder revives it, and may revoke it
    w.add_tenure(Tenure("t_new_king", "p_high", "off_crown", "hold", w.tick))
    assert seat_hold(w, "p_mid", "off_crown") is e
    kinds = _revoke(w, d, "p_high", "off_crown", "off_crown", to="p_mid")
    assert kinds == ["tenure.closed"] and not e.live, kinds
    assert _hold(w, "off_crown").subject == "p_high"


def test_in48_8_the_holders_own_hold_is_preferred():
    w, d = _world()
    nt = Tenure("t_both", "p_king", "off_crown", KIND, w.tick)
    w.add_tenure(nt)                           # an edge no act could open, planted to ask the order
    assert seat_hold(w, "p_king", "off_crown") is _hold(w, "off_crown")
    _hold(w, "off_crown").until = w.tick       # and with the hold gone, the seat is vacant: dormant
    assert seat_hold(w, "p_king", "off_crown") is None


# ================================================================================================
# 9 -- SEATING THE DELEGATE IN THE SAME SEAT CLOSES HIS DELEGATION ON IT, UNDER `conferral`
# ================================================================================================

def test_in48_9_a_confer_seating_the_delegate_closes_his_delegation_on_that_seat_only():
    w, d = _world()
    assert "tenure.opened" in _delegate(w, d, "p_high", "off_duke", "p_mid")
    assert "tenure.opened" in _delegate(w, d, "p_king", "off_crown", "p_mid", aid="dl2")
    on_duke, on_crown = _edge(w, "p_mid", "off_duke"), _edge(w, "p_mid", "off_crown")
    kinds = _confer(w, d, "p_king", "off_crown", "off_duke", "p_mid", "seat_mid")
    assert "tenure.opened" in kinds and _hold(w, "off_duke").subject == "p_mid", kinds
    assert not on_duke.live, "the conferee kept a delegation on the seat he now holds"
    assert on_crown.live, "a delegation on another seat closed"
    was = Tenure(on_duke.id, on_duke.subject, on_duke.object, KIND, on_duke.since,
                 payload=on_duke.payload)
    assert G.tenure_write_basis(w, on_duke, was, "p_king", "off_crown", frozenset()) == G.CONFERRAL


# ================================================================================================
# 10 -- NO BENCH SEAT FOR A DELEGATE
# ================================================================================================

def test_in48_10_a_delegate_is_not_on_the_bench_and_may_not_determine():
    w, d = _world()
    assert "determine" in _hold(w, "off_duke").granted_acts
    assert "tenure.opened" in _delegate(w, d, "p_high", "off_duke", "p_mid")
    e = _edge(w, "p_mid", "off_duke")
    assert "determine" in e.granted_acts and seat_hold(w, "p_mid", "off_duke") is e
    bench = world_q.judging_set(w, "S")
    assert "p_high" in bench and "p_mid" not in bench, bench
    assert G.may_determine(w, "p_high", "off_duke", "p_low"), "control: the holder may determine"
    assert not G.may_determine(w, "p_mid", "off_duke", "p_low"), "a delegate sat in judgment"


# ================================================================================================
# 11 -- THE DECLINE: NO COMPUTED DECISION OPENS A DELEGATION
# ================================================================================================

def test_in48_11_opening_set_forms_no_confer_on_a_told_of_own_seat():
    w, d = _world()
    p = w.persons["p_king"]
    p.ledger.append(Claim("c_k_mid", "p_king", "p_mid", "exists:Person", 1, 0, "firsthand", 100, "own"))
    q = Question("q:need:own", "need", (), "off_crown", (("off_crown", "Office"), ("off_reeve", "Office")))
    formed = opening_set(p, assemble(p, q, 12), q, w.fixtures)
    confers = [c for c in formed if c.verb == "confer"]
    assert any(c.subject == "off_reeve" for c in confers), "control: no confer formed at all"
    own = [c for c in confers if c.subject == (c.operands or {}).get("via", "off_crown")
           and c.subject in {"off_crown", "off_mayor"}]
    assert not own, [(c.subject, c.operands) for c in own]


SEASONS = 4


def _entry_count(monkeypatch, decline: bool) -> tuple:
    """The entry instrument (design §4.1): `POP.run` (the real chooser, the real fold) for `SEASONS`
    seasons on the fixture world, the King TOLD of both his own seats (H-207 C4: a told-of own seat
    rides the `Office` class), every `_req_confer` entry counted and every one naming its own `via`.
    `decline=False` empties the derived opener set `opening_set` declines on -- the CONTROL arm."""
    from ..decision import options as _options
    real = _preds.REQUIRES_PREDICATES["confer"]
    seen = {"checked": 0, "own": 0}

    def counted(w, a):
        seen["checked"] += 1
        if a.via is not None and _preds.office_named_by(a) == a.via:
            seen["own"] += 1
        return real(w, a)
    monkeypatch.setitem(_preds.REQUIRES_PREDICATES, "confer", counted)
    if not decline:
        monkeypatch.setattr(_options, "_DELEGATE_OPENERS", frozenset())
    w, _ = _world()
    p = w.persons["p_king"]
    for i, o in enumerate(("p_mid", "p_low")):
        p.ledger.append(Claim(f"c_k{i}", "p_king", o, "exists:Person", 1, 0, "firsthand", 100, "own"))
    for i, s in enumerate(("off_crown", "off_mayor")):
        p.ledger.append(Claim(f"c_s{i}", "p_king", s, "exists:Office", 1, 0, "firsthand", 100, "own"))
    POP.run(seasons=SEASONS, seed=0, w=w)
    return seen["checked"], seen["own"], sum(1 for t in w.tenures if t.kind == KIND)


def test_in48_11_no_computed_confer_reaches_req_confer_naming_its_own_seat(monkeypatch):
    """`checked >= N` is asserted BEFORE the zero: a run that never entered `_req_confer` is a failed
    measurement, not a pass. THE CONTROL shows the instrument can see what it excludes: with the
    DECLINE off, computed `confer`s naming their own seat DO reach `_req_confer` and open delegations.
    (`build_realm(0)` over four seasons is the design's instrument; it runs far past tens of seconds,
    so it was run once and its numbers are in the IN-48 receipt, not here.)"""
    checked, own, opened = _entry_count(monkeypatch, decline=False)
    assert checked >= 1, f"control: _req_confer never entered ({checked})"
    assert own >= 1 and opened >= 1, f"control: the instrument observed no own-seat confer ({own}, {opened})"
    monkeypatch.undo()
    checked, own, opened = _entry_count(monkeypatch, decline=True)
    assert checked >= 10, f"_req_confer was entered {checked} times: the measurement observed too little"
    assert own == 0 and opened == 0, (checked, own, opened)


# ================================================================================================
# 12 -- THE LOAD AND THE ENDS
# ================================================================================================

def test_in48_12_release_must_carry_delegate_or_the_load_fails(monkeypatch):
    real = _verbs.load_yaml

    def planted(text):
        doc = real(text)
        if isinstance(doc, dict) and "verbs" in doc:
            for r in doc["verbs"]:
                if r.get("verb") == "release":
                    r["domain"] = [k for k in r["domain"] if k != KIND]
        return doc
    monkeypatch.setattr(_verbs, "load_yaml", planted)
    with pytest.raises(SystemExit, match="release"):
        _verbs._load_verb_table()


def test_in48_12_the_derived_opener_set_of_delegate_is_confer():
    assert _verbs._derive_openers_from_effects().get(KIND) == ["confer"]
    assert KIND not in _verbs.tenure_kinds_without_an_opener()


def test_in48_12_add_tenure_refuses_a_delegate_that_is_not_person_to_office():
    w, _ = _world()
    w.add_tenure(Tenure("t_ok", "p_mid", "off_crown", KIND, 0))             # control: Person -> Office
    with pytest.raises(Forbidden):
        w.add_tenure(Tenure("t_rung", "p_mid", "S", KIND, 0))               # object a Rung
    with pytest.raises(Forbidden):
        w.add_tenure(Tenure("t_sub", "off_mayor", "off_crown", KIND, 0))    # subject an Office


# ================================================================================================
# 13 -- THE EXIT: A COMPUTED ACT, IN THE SEEDED REALM, THROUGH A DELEGATED SEAT
# ================================================================================================

EXIT_SEAT = "off_npc_021"          # a seat of `build_realm(0)` whose remit grants `revoke` (and more)


def _computed_acts_via(w, pid, seat):
    """Every act `pid`'s own decision machinery forms THROUGH `seat` this tick: `questions_for`,
    `opening_set`, `pack_scenes` -- no act hand-built."""
    p = w.persons[pid]
    acts = []
    for q in world_q.questions_for(w, p):
        cands = opening_set(p, assemble(p, q, 12), q, w.fixtures)
        mint = lambda who, verb, subj, q=q: H(w.world_seed, w.tick, who, f"act:{verb}:{subj}:{q.id}")
        for s in pack_scenes(p, cands, 99, w.fixtures, mint):
            acts.extend(a for a in s.acts if a.via == seat)
    return acts


def test_in48_13_exit_a_delegates_computed_act_executes_via_the_seat_then_refuses_after_revoke():
    w = POP.build_realm(0)
    d = SeasonDriver(w)
    d.matter(mint_token(w, WriteClass.MATTER), [])
    principal = _hold(w, EXIT_SEAT).subject
    delegate = next(pid for pid in sorted(w.persons)
                    if pid.startswith("p_npc") and not any(t.kind == "hold" and t.live
                                                          for t in w.persons[pid].tenures))
    w.add_tenure(Tenure("t_exit_delegate", delegate, EXIT_SEAT, KIND, w.tick))   # build-placed
    e = _edge(w, delegate, EXIT_SEAT)
    assert e is not None and _hold(w, EXIT_SEAT).subject == principal
    assert seat_hold(w, delegate, EXIT_SEAT) is e
    acts = _computed_acts_via(w, delegate, EXIT_SEAT)
    assert acts, f"{delegate} formed no act through the delegated seat"
    executed = None
    for a in acts:
        kinds = _fold(w, d, a)
        if kinds and not any(k.endswith(".refused") for k in kinds):
            executed = (a, kinds)
            break
    assert executed is not None, [(a.verb, a.payload) for a in acts]
    a, kinds = executed
    assert _hold(w, EXIT_SEAT).subject == principal, "the principal lost his hold"
    assert "tenure.closed" in _revoke(w, d, principal, EXIT_SEAT, EXIT_SEAT, to=delegate)
    assert not e.live and _hold(w, EXIT_SEAT).subject == principal
    again = Act(id=a.id + ":again", actor=a.actor, verb=a.verb, via=a.via, payload=a.payload)
    kinds = _fold(w, d, again)
    assert any(k.endswith(".refused") for k in kinds), (a.verb, kinds)
