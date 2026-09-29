"""G3 -- `NotYours` at the gate, `Act.via`, purview through `via.scope`. Plan position 6.

`04 §C.2` F3 / AX-4 clause 2: *"kind is Tenure => one of: actor == subject(id) -- T-m / cause is
this Tenure's declared term maturation -- T-n / via is a Seat whose revocation basis reaches it --
T-o, and via MUST be present / cause is an existence change this same act caused -- destroy's
cascade / otherwise raise NotYours"*, plus the fifth clause `04_VERBS.md` found missing -- the
conferral-basis opener. And `04:332`: *"purview is asked of the seat exercised, not the actor --
`Act.via : SeatId?`; every purview walk uses `via.scope`."*

What each block proves, and the control that stops it passing vacuously:

  1. THE PLAN'S FALSIFIER. A T-o write whose `via` names a seat whose basis does NOT reach the edge
     is refused -- by an actor who ALSO holds a seat that would reach it, so a basis walk still
     reading the actor (any seat he holds) admits it and this goes red. Control: the reaching seat.
  2. ONE REFUSAL PER LIVE VIOLATION, COUNTED. `revoke`, `confer` and `fight` (renamed from
     `kill / wound`, plan `FIGHT-RENAME`) each wrote another person's edge under the old gate;
     each unlawful twin is refused (`>= 3`, and the SET of verbs refused is asserted), and each
     lawful twin is admitted.
  3. THE FIFTH CLAUSE, BOTH ARMS. A conferral-basis opener is admitted through a seat with purview
     over a seat declaring a basis, and refused without `via`, through a seat without purview, on a
     seat with no basis, and through the seat being conferred.
  4. A `revoke` WITH `via=None` IS REFUSED AT THE GATE -- asserted with every earlier check
     bypassed, so the refusal can only be the gate's; and the store is as it was.
  5. `release` IS T-m; `establish`'s re-stamp needs the conferral basis; an edge's ends cannot be
     rewritten; purview is ruling (4)'s walk; and the chooser sets `via` from the same grant the
     person-side eligibility admitted on.
"""
import pytest

from engine.season.data.matrix import Step, WriteClass
from engine.season.data.requires import UNKNOWN, Verdict
from engine.season.data.rosters import FELLED
from engine.season.data.verbs import VERB_TABLE
from engine.season.decision import person_side_eligible
from engine.season.decision.choose import pack_scenes
from engine.season.decision.options import exercised_seat
from engine.season.gaps import Forbidden
from engine.season.harness import probes as P
from engine.season.loop import predicates as _preds
from engine.season.loop.driver import SeasonDriver, mint_token
from engine.season.seam import Resolution
from engine.season.state.carriers import Act, Candidate, Office, Rung, Tenure
from engine.season.state.gate import (
    CASCADE, CONFERRAL, HANDOVER, T_M, T_O, NotYours, may_fill, may_revoke, purview_reaches,
    seat_hold)
from engine.season.state.ids import H

_RUNG_ABOVE = "rung_above_same_faction"


def _seat_on(w, pid, oid, post, rung, faction="Crown", remit=("confer", "revoke")):
    """A new office, constructed BEFORE its holder is seated, so the grant is correct at seating."""
    w.offices[oid] = Office(oid, post, rung, list(remit), faction=faction, conferral="appointed",
                            revocation=_RUNG_ABOVE)
    w.add_tenure(Tenure(f"t_{oid}", pid, oid, "hold", 0))


def _gov_world():
    """`tiny_world` (R ⊃ D ⊃ S ⊃ Hh; `p_high` holds `off_duke`, a Crown Duke at `D`), plus:

      * `off_crown` -- a Crown King at `R`, held by `p_king`: the seat ON THE RUNG ABOVE the duke,
        and a seat whose purview reaches everything in the realm;
      * `off_mayor` -- a Crown Mayor at `S`, held by THE SAME `p_king`: below the duchy, so it
        neither sits on the rung above the duke nor has purview over `D`. The King holding BOTH is
        what lets a test tell "the seat exercised" from "any seat the actor holds";
      * `D2`, a sibling duchy under `R`, and `off_duke2`, a Crown Duke there held by `p_other`: a
        seat whose purview reaches nothing under `D`;
      * `off_reeve` -- an UNHELD Crown seat at `S` declaring `appointed`, to be conferred.

    The duke's own seat declares both ruled bases (`ED-IN-0256` (2), (3))."""
    w = P.tiny_world()
    w.rungs["D2"] = Rung("D2", "duchy")
    w.add_tenure(Tenure("t_d2_in_r", "D2", "R", "contain", 0))
    duke = w.offices["off_duke"]
    duke.conferral, duke.revocation = "appointed", _RUNG_ABOVE
    _seat_on(w, "p_king", "off_crown", "King", "R")
    _seat_on(w, "p_king", "off_mayor", "Mayor", "S")
    _seat_on(w, "p_other", "off_duke2", "Duke", "D2")
    w.offices["off_reeve"] = Office("off_reeve", "Reeve", "S", ["issue"], faction="Crown",
                                    conferral="appointed", revocation=_RUNG_ABOVE)
    d = SeasonDriver(w)
    d.matter(mint_token(d.w, WriteClass.MATTER), [])
    w.step = Step.RESOLVE
    return w, d


def _hold(w, office):
    return next((t for t in w.tenures if t.kind == "hold" and t.object == office and t.live), None)


def _close(w, t, actor, via):
    """A bare gate write closing `t`, as `actor` through `via` -- nothing but the gate is asked."""
    return w.write("Tenure", mint_token(w, WriteClass.ACTS), lambda: setattr(t, "until", w.tick),
                   record_kind="Tenure", fieldname="until", driver="Act", actor=actor, via=via)


@pytest.fixture
def gate_only(monkeypatch):
    """EVERY CHECK BEFORE THE GATE, BYPASSED: `_admits` (eligibility AND `requires`) admits all.
    What is refused under this fixture can only have been refused by the write gate."""
    monkeypatch.setattr(SeasonDriver, "_admits",
                        lambda self, w, a, row: (True, (), Verdict(UNKNOWN, ())))


# ======================================================================================
# 1 -- THE PLAN'S FALSIFIER: THE BASIS IS ASKED OF `via`, NOT OF THE ACTOR
# ======================================================================================

def test_g3_a_revocation_through_a_seat_whose_basis_does_not_reach_is_refused():
    """`p_king` holds `off_crown` (on the rung above the duke, same faction: ruling (3) admits it)
    AND `off_mayor` (below the duchy: ruling (3) refuses it). Revoking the duke THROUGH `off_mayor`
    must raise -- if it passes, the basis walk is reading the actor's seats, not `via`'s. Control:
    the same write through `off_crown` is admitted. Asserted at the gate, at the precondition that
    asks the gate's own predicate, and on the store after the refusal."""
    w, _ = _gov_world()
    t = _hold(w, "off_duke")
    assert seat_hold(w, "p_king", "off_crown") and seat_hold(w, "p_king", "off_mayor"), "fixture"
    assert not may_revoke(w, "p_king", "off_mayor", w.offices["off_duke"])
    assert may_revoke(w, "p_king", "off_crown", w.offices["off_duke"]), "control: no seat reaches"
    act = lambda via: Act(id=f"rv_{via}", actor="p_king", verb="revoke",
                          payload={"office": "off_duke"}, via=via)
    assert not _preds._req_revoke(w, act("off_mayor")), "the precondition read the actor's seats"
    assert _preds._req_revoke(w, act("off_crown")), "control: the precondition refused the King"

    with pytest.raises(NotYours) as refused:
        _close(w, t, "p_king", "off_mayor")
    assert refused.value.where == "F3", refused.value.where
    assert t.live, "the gate refused the revocation and the duke's hold is closed anyway"
    _close(w, t, "p_king", "off_crown")
    assert not t.live, "control: the revocation through the seat above was not applied"


# ======================================================================================
# 2 -- ONE REFUSAL PER LIVE VIOLATION, COUNTED, EACH WITH ITS LAWFUL TWIN
# ======================================================================================

def _felled(victim):
    return Resolution(FELLED, {"wound_state": {victim: {}}})


def test_g3_every_live_violation_is_refused_without_its_basis_and_admitted_with_it(gate_only):
    """`04 §C.2`'s F3 note names the three: *"`revoke` ... and `confer` ... both writing
    `Tenure.until` on an edge whose subject is somebody else, and `kill / wound` writing
    `Tenure.until` on the victim's edges. Under the first gate all three are lawful."* Each is
    driven through the REAL effect in the fold, with every check before the gate bypassed:

      * `revoke` of the duke's seat with NO seat exercised;
      * `confer` of the unheld reeve's seat onto `p_mid` with NO seat exercised;
      * `fight` (renamed from `kill / wound`) whose victim's edges close while the victim DOES
        NOT cease to exist -- `remove_person` stubbed to close and not remove -- the cascade
        claimed, not caused.

    COUNTED, and the set is asserted, so a gate that refuses one and admits two cannot pass. Then
    each lawful twin -- the King's seat, the duke's seat, a real death -- is admitted."""
    refused = []

    w, d = _gov_world()
    with pytest.raises(NotYours):
        d._fold(w, mint_token(w, WriteClass.ACTS),
                Act(id="rv0", actor="p_king", verb="revoke", payload={"office": "off_duke"}))
    assert _hold(w, "off_duke") is not None, "the refused revocation closed the hold"
    refused.append("revoke")

    w, d = _gov_world()
    with pytest.raises(NotYours):
        d._fold(w, mint_token(w, WriteClass.ACTS),
                Act(id="cf0", actor="p_high", verb="confer",
                    payload={"office": "off_reeve", "to": "p_mid"}))
    assert _hold(w, "off_reeve") is None, "the refused conferral left a hold on the seat"
    refused.append("confer")

    w, d = _gov_world()
    victim_edges = [t for t in w.tenures if t.subject == "p_mid" and t.live]
    assert victim_edges, "fixture: the victim owns no live edge"

    def close_without_removing(who):                 # the claim of a cascade, with no death
        for t in w.tenures:
            if (t.subject == who or t.object == who) and t.live:
                t.until = w.tick
        return [who]
    w.remove_person = close_without_removing
    with pytest.raises(NotYours):
        d._fold(w, mint_token(w, WriteClass.ACTS),
                Act(id="kw0", actor="p_low", verb="fight", payload={"subject": "p_mid"}),
                _felled("p_mid"))
    assert all(t.live for t in victim_edges), "the refused cascade left the victim's edges closed"
    refused.append("fight")

    assert len(refused) >= 3 and set(refused) == {"revoke", "confer", "fight"}, refused

    # THE LAWFUL TWINS -- the same three effects, each with its basis present.
    w, d = _gov_world()
    out = d._fold(w, mint_token(w, WriteClass.ACTS),
                  Act(id="rv1", actor="p_king", verb="revoke", payload={"office": "off_duke"},
                      via="off_crown"))
    assert "tenure.closed" in {e.kind for e in out} and _hold(w, "off_duke") is None     # T-o
    w, d = _gov_world()
    out = d._fold(w, mint_token(w, WriteClass.ACTS),
                  Act(id="cf1", actor="p_high", verb="confer",
                      payload={"office": "off_reeve", "to": "p_mid"}, via="off_duke"))
    assert _hold(w, "off_reeve").subject == "p_mid"                                     # conferral
    w, d = _gov_world()
    victim_edges = [t for t in w.tenures if t.subject == "p_mid" and t.live]
    out = d._fold(w, mint_token(w, WriteClass.ACTS),
                  Act(id="kw1", actor="p_low", verb="fight", payload={"subject": "p_mid"}),
                  _felled("p_mid"))
    assert "p_mid" not in w.persons and victim_edges and not any(t.live for t in victim_edges)


# ======================================================================================
# 3 -- THE FIFTH CLAUSE: THE CONFERRAL-BASIS OPENER, BOTH ARMS
# ======================================================================================

def test_g3_the_conferral_opener_is_admitted_only_through_a_seat_with_purview(gate_only):
    """`04_VERBS.md`, the `determine` row's correction ⑴: *"a conferral-basis opener matches none of
    the four. So does `confer`, today"*. ADMITTED: the duke, through his seat at `D`, opens
    `p_mid`'s hold on the reeve's seat at `S`, which declares `appointed`. REFUSED at the gate,
    each on a fresh world and each leaving no hold behind, one per conjunct of the clause:"""
    cases = {
        "no seat exercised": dict(actor="p_high", via=None),
        "a seat with no purview over S (the sibling duchy)": dict(actor="p_other", via="off_duke2"),
        "a seat the actor does not occupy": dict(actor="p_low", via="off_duke"),
        "the seat being conferred": dict(actor="p_high", via="off_reeve", seat_self=True),
        "a seat declaring no conferral basis": dict(actor="p_high", via="off_duke", no_basis=True),
    }
    checked = 0
    for why, c in cases.items():
        w, d = _gov_world()
        if c.get("seat_self"):
            # SEATED, LIVE, on the seat he names -- so `seat_hold` passes and the seat's purview
            # (its own rung, `S`, reflexively) DOES reach the seat: the only conjunct left to
            # refuse is `via` being the seat filled. His own hold's closure is `T-m` and admitted.
            w.add_tenure(Tenure("t_self", "p_high", "off_reeve", "hold", 0))
            assert purview_reaches(w, w.offices["off_reeve"], "S"), "fixture: not reflexive"
        if c.get("no_basis"):
            w.offices["off_reeve"].conferral = None
        with pytest.raises(NotYours):
            d._fold(w, mint_token(w, WriteClass.ACTS),
                    Act(id="cf", actor=c["actor"], verb="confer",
                        payload={"office": "off_reeve", "to": "p_mid"}, via=c["via"]))
        assert not [t for t in w.tenures if t.object == "off_reeve" and t.subject == "p_mid"], (
            f"{why}: the refused opener left the conferee a hold")
        if c.get("seat_self"):
            assert _hold(w, "off_reeve").subject == "p_high", "the refusal left his own hold closed"
            # ⚠ TWO REASONS REFUSE THIS CASE IN THE FOLD, AND ONLY THE PREDICATE SEPARATES THEM.
            # Conferring the seat CLOSES every live hold on it -- his own too -- and the gate judges
            # the world the write leaves, so he no longer sits in `via` by the time it asks. The
            # exclusive-on-the-seat conjunct is asked here, of the world before the act, where he
            # is still seated: it must refuse on `via == the seat filled` alone (`M9` kills this).
            assert seat_hold(w, "p_high", "off_reeve") is not None
            assert not may_fill(w, "p_high", "off_reeve", w.offices["off_reeve"]), (
                "a seat was admitted as the authority to fill ITSELF")
        checked += 1
    assert checked == len(cases) >= 5, checked

    w, d = _gov_world()
    kinds = [e.kind for e in d._fold(w, mint_token(w, WriteClass.ACTS),
                                     Act(id="cf", actor="p_high", verb="confer",
                                         payload={"office": "off_reeve", "to": "p_mid"},
                                         via="off_duke"))]
    assert "tenure.opened" in kinds and _hold(w, "off_reeve").subject == "p_mid", kinds


def test_g3_confer_refuses_at_the_precondition_what_the_gate_would_refuse():
    """The SHIPPED fold: `_req_confer` asks the gate's own `may_fill` (and, on a held seat,
    `may_revoke`), so an opener without a basis EMITS `confer.refused` and never reaches the gate
    to raise. Both arms through `resolve`, the real path; plus the displacement arm -- a held seat
    is conferred only through a seat whose REVOCATION basis also reaches the incumbent."""
    w, d = _gov_world()
    run = lambda aid, actor, via, to="p_mid": [e.kind for e in d.resolve(
        mint_token(w, WriteClass.ACTS),
        [Act(id=aid, actor=actor, verb="confer", payload={"office": "off_reeve", "to": to},
             via=via)], contest_max_depth=w.fixtures.get("contest_max_depth"))]
    assert run("c0", "p_other", "off_duke2") == ["confer.refused"], "no purview, and admitted"
    assert _hold(w, "off_reeve") is None
    assert "tenure.opened" in run("c1", "p_high", "off_duke")
    # DISPLACEMENT: the reeve's seat is now held (by `p_mid`, no live commit). The King has
    # purview over S, but R is not S's PARENT, so his seat has no revocation authority over the
    # reeve: refused, the reeve still seated. The duke's seat is on D, S's parent, same faction:
    # admitted, and the incumbent's edge closes as the conferee's opens.
    assert may_fill(w, "p_king", "off_crown", w.offices["off_reeve"])
    assert not may_revoke(w, "p_king", "off_crown", w.offices["off_reeve"])
    assert run("c2", "p_king", "off_crown", to="p_low") == ["confer.refused"], (
        "the King displaced a sitting reeve he has no revocation authority over")
    assert _hold(w, "off_reeve").subject == "p_mid"
    kinds = run("c3", "p_high", "off_duke", to="p_low")
    assert {"tenure.opened", "tenure.closed"} <= set(kinds), kinds
    assert _hold(w, "off_reeve").subject == "p_low"


# ======================================================================================
# 4 -- A `revoke` WITH NO SEAT IS REFUSED AT THE GATE
# ======================================================================================

def test_g3_a_revoke_with_no_seat_is_refused_at_the_gate_itself(gate_only):
    """`04 §C.2`: *"a revocation with no seat in `Act.via` is refused at the gate, so 'a superior may
    revoke' cannot degrade into 'anyone with a remit string'"*. Three observations:

      (a) the gate ALONE -- a bare write, actor present, `via=None` -> `NotYours`;
      (b) the fold with eligibility AND `requires` bypassed (`gate_only`) -> `NotYours`, so the gate
          is what refuses when nothing before it does;
      (c) after either, the duke's hold is LIVE and the mint window is SHUT -- a refused write
          cannot issue a receipt after it. (G4 moved the fold's mint INSIDE `World.write`, so
          `_apply_write` no longer mints after the write returns; the shut window is still what
          stops any caller minting against a refused one.)"""
    w, d = _gov_world()
    t = _hold(w, "off_duke")
    with pytest.raises(NotYours):
        _close(w, t, "p_king", None)
    assert t.live, "(a) the gate refused and the hold closed anyway"
    with pytest.raises(Forbidden):
        w.gate.mint(t.id, "set", "Act", "until")
    with pytest.raises(NotYours):
        d._fold(w, mint_token(w, WriteClass.ACTS),
                Act(id="rv_none", actor="p_king", verb="revoke", payload={"office": "off_duke"}))
    assert t.live, "(b) the fold's refused write closed the hold"


def test_g3_the_shipped_fold_refuses_a_seatless_revoke_before_the_gate():
    """(c)'s complement, DEFENCE IN DEPTH: through the shipped fold a `via=None` remit act is not
    eligible at all -- `_eligible`'s `remit:` branch asks the seat exercised, and there is none --
    so it EMITS `revoke.refused` and raises nothing. And naming a seat the actor does not occupy is
    the same as naming none (`seat_hold`)."""
    w, d = _gov_world()
    row = VERB_TABLE["revoke"]
    mk = lambda via, actor="p_king": Act(id=f"rv_{via}_{actor}", actor=actor, verb="revoke",
                                         payload={"office": "off_duke"}, via=via)
    assert not d._eligible(w, mk(None), row)
    assert not d._eligible(w, mk("off_crown", actor="p_low"), row), "a borrowed seat was admitted"
    assert d._eligible(w, mk("off_crown"), row), "control: the King's own seat is not eligible"
    out = d.resolve(mint_token(w, WriteClass.ACTS), [mk(None)],
                    contest_max_depth=w.fixtures.get("contest_max_depth"))
    assert [e.kind for e in out] == ["revoke.refused"], [e.kind for e in out]
    assert _hold(w, "off_duke") is not None


# ======================================================================================
# 5 -- THE REST OF THE CLAUSE: T-m, THE RE-STAMP, THE ENDS, PURVIEW, AND THE MINT
# ======================================================================================

def test_g3_release_is_the_owners_discretion_and_the_owners_only():
    """`_eff_release` is T-m BY CONSTRUCTION (`t.subject == a.actor`) -- confirmed, not assumed:
    the shipped fold releases `p_low`'s own `tie` with NO seat, and the gate admits it; a write by
    `p_low` closing an edge `p_mid` owns is refused, and the edge stays live."""
    w, d = _gov_world()
    tie = next(t for t in w.tenures if t.kind == "tie" and t.subject == "p_low" and t.live)
    out = d.resolve(mint_token(w, WriteClass.ACTS),
                    [Act(id="rel", actor="p_low", verb="release", payload={"subject": tie.object})],
                    contest_max_depth=w.fixtures.get("contest_max_depth"))
    assert "tenure.closed" in {e.kind for e in out} and not tie.live, [e.kind for e in out]
    theirs = next(t for t in w.tenures if t.subject == "p_mid" and t.kind == "contain" and t.live)
    with pytest.raises(NotYours):
        _close(w, theirs, "p_low", None)
    assert theirs.live


def test_g3_t_m_never_admits_self_seating_on_an_unrelated_seat(gate_only):
    """FOUND BY AN ANTAGONIST PASS, 2026-09-26: T-m read `owner` from the WRITE ITSELF for an
    OPENED edge (`t.subject`), so "the actor is the owner" was self-fulfilling for anyone who
    named themselves the new holder -- an UNRELATED actor, `via=None`, no purview anywhere, could
    open a `hold` on ANY seat naming himself its subject. `04:330` -- purview is asked of the SEAT
    exercised, never the actor. A bare gate write, `_admits` bypassed, so what refuses is the
    gate's own T-m boundary and nothing upstream of it."""
    w, _ = _gov_world()
    assert w.offices["off_reeve"].conferral == "appointed" and not _hold(w, "off_reeve"), "fixture"

    def open_reeve():
        w.add_tenure(Tenure("t_self_seat", "p_other", "off_reeve", "hold", w.tick,
                            payload={"remit_acts": ("issue",)}))

    with pytest.raises(NotYours) as refused:
        w.write("Tenure", mint_token(w, WriteClass.ACTS), open_reeve,
                record_kind="Tenure", fieldname="until", driver="Act",
                actor="p_other", via=None)
    assert refused.value.where == "F3", refused.value.where
    assert _hold(w, "off_reeve") is None, "the self-seating was refused and the seat stayed empty"

    # CONTROL: the same open, through a seat with real purview over off_reeve (the King's), admits.
    w.write("Tenure", mint_token(w, WriteClass.ACTS), open_reeve,
           record_kind="Tenure", fieldname="until", driver="Act",
           actor="p_king", via="off_crown")
    assert _hold(w, "off_reeve") is not None, "control: a purview-holding seat could not seat p_king"


def test_g3_t_m_never_admits_re_stamping_ones_own_seat_without_a_superiors_basis(gate_only):
    """THE PAYLOAD-SIDE TWIN. `off_duke` has exactly one holder, `p_high`, and `establish`'s own
    re-stamp mechanism (`World._grant_remit`) writes ONLY his `hold`'s `payload` -- so `owner ==
    actor` on every re-stamp of his own seat, and pre-fix T-m admitted it with no seat at all.
    Refused with `via=None` and reflexively through `off_duke` itself (`may_fill` refuses
    `via == off.id`); admitted through `off_crown`, the seat directly above in the same faction."""
    w, _ = _gov_world()
    t = _hold(w, "off_duke")
    assert t.subject == "p_high" and t.granted_acts == ("issue", "determine", "confer",
                                                         "dispatch", "convene"), "fixture"

    def restamp():
        t.payload = dict(t.payload)
        t.payload["remit_acts"] = t.payload["remit_acts"] + ("revoke",)

    for via in (None, "off_duke"):
        before = t.payload
        with pytest.raises(NotYours) as refused:
            w.write("Tenure", mint_token(w, WriteClass.ACTS), restamp,
                    record_kind="Tenure", fieldname="payload", driver="Act",
                    actor="p_high", via=via)
        assert refused.value.where == "F3", (via, refused.value.where)
        assert t.payload == before, f"via={via!r}: the refused self-re-stamp reached the grant"

    w.write("Tenure", mint_token(w, WriteClass.ACTS), restamp,
           record_kind="Tenure", fieldname="payload", driver="Act",
           actor="p_king", via="off_crown")
    assert "revoke" in t.granted_acts, "control: the King's own seat could not re-stamp the duke"


def test_g3_t_m_still_admits_a_sole_holders_own_resignation():
    """THE CONTROL FOR BOTH TESTS ABOVE: closing one's own seat -- not opening or re-granting it --
    is still T-m, because giving up a seat is not an exercise of the seat's authority. `release` on
    `off_duke2`'s sole holder, no `via`, admitted and the hold closes."""
    w, d = _gov_world()
    t = _hold(w, "off_duke2")
    assert t.subject == "p_other", "fixture"
    out = d.resolve(mint_token(w, WriteClass.ACTS),
                    [Act(id="rel_seat", actor="p_other", verb="release",
                         payload={"subject": "off_duke2"})],
                    contest_max_depth=w.fixtures.get("contest_max_depth"))
    assert "tenure.closed" in {e.kind for e in out} and not t.live, [e.kind for e in out]


# The reeve's seat restated in full with one more remit act -- clause 4's only admitted change.
_RESTAMP = dict(office="off_reeve", post="Reeve", rung="S", remit=["issue", "dispatch"],
                faction="Crown", conferral="appointed", revocation=_RUNG_ABOVE)


def test_g3_the_restamp_of_anothers_grant_needs_the_conferral_basis(gate_only):
    """`13f`'s `establish` re-stamps the grant on every live `hold` on the office -- a write on a
    SITTING HOLDER'S edge, the fourth live non-owner write G3's plan text did not list. Admitted
    through a seat with purview over the office (the duke's, over `S`); REFUSED through a seat
    without it (the sibling duke's), with the holder's grant as it was.

    ⚠ AND THE BOUND THE GATE STATES, PINNED: the refused act's OFFICE write (`remit_acts`) is NOT
    undone -- the gate restores the tenure store only (`World._restore_tenures`, `H-130`'s class)."""
    def world():
        w, d = _gov_world()
        w.add_tenure(Tenure("t_reeve", "p_mid", "off_reeve", "hold", 0))
        return w, d, next(t for t in w.tenures if t.id == "t_reeve")

    w, d, t = world()
    assert t.granted_acts == ("issue",), "fixture"
    with pytest.raises(NotYours):
        d._fold(w, mint_token(w, WriteClass.ACTS),
                Act(id="e0", actor="p_other", verb="establish", payload=_RESTAMP, via="off_duke2"))
    assert t.granted_acts == ("issue",), "the refused re-stamp reached the sitting holder"
    assert w.offices["off_reeve"].remit_acts == ["issue", "dispatch"], (
        "the office write was undone -- then `_restore_tenures`' stated bound is wrong")

    w, d, t = world()
    kinds = [e.kind for e in d._fold(w, mint_token(w, WriteClass.ACTS),
                                     Act(id="e1", actor="p_high", verb="establish",
                                         payload=_RESTAMP, via="off_duke"))]
    assert "tenure.payload_set" in kinds and t.granted_acts == ("issue", "dispatch"), kinds


def test_g3_the_shipped_establish_refuses_the_restamp_before_the_gate():
    """`_req_establish`'s clause 5 asks the gate's `may_fill` first, so through the SHIPPED fold
    the sibling duke's re-stamp EMITS `establish.refused`, raises nothing, and leaves the sitting
    reeve's grant -- and, because the effect never ran, the office -- as they were."""
    w, d = _gov_world()
    w.add_tenure(Tenure("t_reeve", "p_mid", "off_reeve", "hold", 0))
    t = next(x for x in w.tenures if x.id == "t_reeve")
    out = d.resolve(mint_token(w, WriteClass.ACTS),
                    [Act(id="e2", actor="p_other", verb="establish", payload=_RESTAMP,
                         via="off_duke2")],
                    contest_max_depth=w.fixtures.get("contest_max_depth"))
    assert [e.kind for e in out] == ["establish.refused"], [e.kind for e in out]
    assert t.granted_acts == ("issue",) and w.offices["off_reeve"].remit_acts == ["issue"]


def test_g3_no_basis_rewrites_an_edges_ends_not_even_the_owners():
    """A Tenure's `subject`, `object` and `kind` fix WHOSE edge it is. Rewriting `subject` hands the
    edge to another store, so `T-m` -- read off the owner BEFORE the write -- does not admit it,
    and nothing else does. The owner rewriting his own edge's subject is refused and restored."""
    w, _ = _gov_world()
    tie = next(t for t in w.tenures if t.kind == "tie" and t.subject == "p_low")
    with pytest.raises(NotYours):
        w.write("Tenure", mint_token(w, WriteClass.ACTS), lambda: setattr(tie, "subject", "p_mid"),
                record_kind="Tenure", fieldname="until", driver="Act", actor="p_low")
    assert tie.subject == "p_low"


def test_g3_an_opened_edge_is_removed_when_its_write_is_refused():
    """The rollback's other half: a refused write that OPENED a Tenure leaves no trace of it in
    any store -- the owner's list or `_unowned`."""
    w, _ = _gov_world()
    before = len(w.tenures)
    with pytest.raises(NotYours):
        w.write("Tenure", mint_token(w, WriteClass.ACTS),
                lambda: w.add_tenure(Tenure("t_forced", "p_mid", "off_reeve", "hold", w.tick)),
                record_kind="Tenure", fieldname="since", driver="Act", actor="p_low")
    assert len(w.tenures) == before and not [t for t in w.tenures if t.id == "t_forced"]


def test_g3_purview_is_ruling_four_asked_of_the_seat():
    """`ED-IN-0256` (4): *"owner of highest rung in chain of ownership, eg territory is owned by
    Duke if it's within boundaries of duchy"*. Every (seat, rung) pair in the world against the
    reading adopted in `purview_reaches`' docstring -- reflexive on the seat's rung, every rung
    inside it, the King over the duke's ground AS WELL AS the duke (reading (a)), nothing upward,
    nothing sideways, a rungless seat nowhere -- counted, so the sweep cannot pass on an empty
    world."""
    w, _ = _gov_world()
    inside = {"R": {"R", "D", "D2", "S", "Hh"}, "D": {"D", "S", "Hh"}, "D2": {"D2"},
              "S": {"S", "Hh"}}
    places = ("R", "D", "D2", "S", "Hh")
    checked = 0
    for oid in ("off_crown", "off_duke", "off_duke2", "off_mayor"):
        seat = w.offices[oid]
        for rung in places:
            assert purview_reaches(w, seat, rung) is (rung in inside[seat.rung]), (oid, rung)
            checked += 1
    rungless = w.offices["off_dicastery"]
    assert rungless.rung is None
    for rung in places:
        assert not purview_reaches(w, rungless, rung), f"a rungless seat reaches {rung}"
        checked += 1
    assert not purview_reaches(w, w.offices["off_crown"], None)
    assert checked >= 25, checked


def test_g3_the_chooser_mints_via_from_the_grant_eligibility_admitted_on():
    """`decision/choose.py::pack_scenes` sets `Act.via` person-side, and the fold admits the act
    through exactly that seat. SWEPT over every verb row and every person in the world: wherever the
    person-side reading admits a verb, the resolver's `_eligible` admits the act minted with
    `exercised_seat`'s `via`; and a verb admitted ONLY through a remit is refused with `via=None`.
    Counted on both sides, so neither half can pass on zero."""
    w, d = _gov_world()
    admitted = remit_only = 0
    for pid, p in sorted(w.persons.items()):
        for verb, row in sorted(VERB_TABLE.items()):
            if not person_side_eligible(p, row):
                continue
            via = exercised_seat(p, row)
            act = Act(id=f"x_{pid}_{verb}", actor=pid, verb=verb, via=via)
            assert d._eligible(w, act, row), f"{pid}/{verb} via {via}: admitted person-side only"
            admitted += 1
            if via is not None:
                assert seat_hold(w, pid, via) is not None, f"{pid} does not sit in {via}"
                if all(alt.startswith("remit") for alt in row.eligibility):
                    assert not d._eligible(w, Act(id="n", actor=pid, verb=verb), row), (
                        f"{pid}/{verb} is eligible with NO seat -- remit read off the actor")
                    remit_only += 1
    assert admitted >= 20 and remit_only >= 5, (admitted, remit_only)

    duke = w.persons["p_high"]
    mint = lambda pid, verb, subj: H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
    scenes = pack_scenes(duke, [Candidate("dispatch", "p_low"), Candidate("speak", "p_low")],
                         2, w.fixtures, mint)
    vias = {a.verb: a.via for s in scenes for a in s.acts}
    assert vias == {"dispatch": "off_duke", "speak": None}, vias


def test_g3_every_basis_name_the_gate_can_return_is_reached_in_this_file():
    """The six bases, less the unbuilt `T-n`, each observed ADMITTING at least once through the
    real `tenure_write_basis` -- so a basis whose branch stopped being reachable cannot hide behind
    the refusal tests above, which observe only what is refused. The sixth, `handover`, arrived
    with `give` at plan position 16; its own refusals are `test_give.py`'s."""
    import engine.season.state.gate as G
    seen = set()
    real = G.tenure_write_basis

    def spy(*a, **k):
        b = real(*a, **k)
        seen.add(b)
        return b
    G.tenure_write_basis = spy
    try:
        w, d = _gov_world()
        tok = lambda: mint_token(w, WriteClass.ACTS)
        # The conferral FIRST: the revocation closes the duke's own seat, after which he no
        # longer sits in the seat he would confer through.
        d._fold(w, tok(), Act(id="b", actor="p_high", verb="confer",
                              payload={"office": "off_reeve", "to": "p_mid"}, via="off_duke"))
        d._fold(w, tok(), Act(id="a", actor="p_king", verb="revoke",
                              payload={"office": "off_duke"}, via="off_crown"))          # T-o
        # `p_low` and `p_mid` share a hearth: a Record made and handed over before the fight below
        # takes `p_mid` out of the world.
        d._fold(w, tok(), Act(id="r", actor="p_low", verb="create_record",
                              payload={"record": "rec_g"}))
        d._fold(w, tok(), Act(id="g", actor="p_low", verb="give",
                              payload={"subject": "rec_g", "to": "p_mid"}))               # handover
        d._fold(w, tok(), Act(id="c", actor="p_low", verb="release",
                              payload={"subject": "p_mid"}))                              # T-m
        d._fold(w, tok(), Act(id="k", actor="p_low", verb="fight",
                              payload={"subject": "p_mid"}), _felled("p_mid"))            # cascade
    finally:
        G.tenure_write_basis = real
    assert {T_M, T_O, CONFERRAL, CASCADE, HANDOVER} <= seen, sorted(map(str, seen))
