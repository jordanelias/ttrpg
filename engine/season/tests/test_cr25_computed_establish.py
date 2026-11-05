"""v11 CR-25 -- A COMPUTED `establish` FOUNDS AN OFFICE OVER A HOLDING (CR-11's design; M8's H-132 (b), H-144 (b)).

THE HAND-BUILT SET the card names, each through the shipped fold (`SeasonDriver.resolve`), with its control in
the same world where one is needed so neither half can pass for the other's reason:

  1. a King holding a territory inside his purview founds `Lord` there, and `w.offices` gains the derived row;
  2. a founding on a territory he does not hold refuses -- and with conjunct (i) dropped (PLANTED FAILURE) the
     same act executes, so the refusal is (i)'s;
  3. a founding at equal rank refuses: the Confessor at `terr_T9` in `build_realm(0)`. ⚠ Under
     `seated_on_the_rung_above_structure` conjuncts (ii) and (iii) follow from (iv) (CR-11's design, 'card and
     tree differ'), so this test refuses at (iii) and at (iv) alike and CANNOT TELL THE TWO APART; it asserts
     both are false and (i), (ii) true;
  4. a re-remit of a VACANT office outside purview refuses (H-144 (b)); control: the seat with purview executes;
  5. a reduction of a `revocation: None` seat's grant refuses (H-132 (b)); controls: the same seat's grant
     WIDENED executes, and a reduction of a seat whose basis admits the exercised seat executes;
  6. the founder revokes the founded Lord through the seat that holds `revoke`, and it executes.

Plus the stamper (`holdings_to_found`) on the realm, and the derivation the effect reads being the
precondition's."""
from __future__ import annotations

import pytest

from ..data.rosters import TITLE_DOMAINS
from ..data.matrix import WriteClass
from ..harness import probes as P
from ..harness.populated import build_realm
from ..loop import predicates as _preds
from ..loop.driver import SeasonDriver, mint_token
from ..queries import world_q
from ..state.carriers import Act, Office, Rung, Tenure


def _world():
    """`tiny_world` plus what test 1 needs and the realm cannot give it (CR-11's design: in `build_realm` no
    realm seat meets (iv) on a territory it holds): a King's seat `off_king` on the realm `R`, held by
    `p_king`, granting `confer` and `revoke`; two territories DIRECTLY UNDER THE REALM, `T` (held by `p_king`)
    and `T2` (held by nobody); and a second duchy `D2` under `R` with a duke `p_other` in `off_duke2`, whose
    purview does not reach `S` (under `D`)."""
    w = P.tiny_world()
    for rid in ("T", "T2"):
        w.rungs[rid] = Rung(rid, "territory")
    w.rungs["D2"] = Rung("D2", "duchy")
    w.offices["off_king"] = Office("off_king", "King", "R", ["issue", "confer", "revoke", "convene"],
                                   faction="Crown")
    w.offices["off_duke2"] = Office("off_duke2", "Duke", "D2", ["issue", "confer", "dispatch"],
                                    faction="Crown")
    for i, (sub, obj, kind) in enumerate((("T", "R", "contain"), ("T2", "R", "contain"),
                                          ("D2", "R", "contain"), ("p_king", "off_king", "hold"),
                                          ("p_king", "T", "hold"), ("p_other", "off_duke2", "hold"))):
        w.add_tenure(Tenure(f"t_cr25_{i}", sub, obj, kind, 0))
    d = SeasonDriver(w)
    d.matter(mint_token(d.w, WriteClass.MATTER), [])
    return w, d


def _act(w, d, aid, actor, via, payload):
    return d.resolve(mint_token(d.w, WriteClass.ACTS),
                     [Act(id=aid, actor=actor, verb="establish", payload=payload, via=via)],
                     contest_max_depth=w.fixtures.get("contest_max_depth"))


def _kinds(out):
    return [e.kind for e in out]


def test_cr25_1_a_king_founds_lord_over_a_held_territory_and_the_office_is_the_derived_row():
    w, d = _world()
    lord = _preds.founded_office_id("T", "Lord")
    assert lord not in w.offices, "fixture: the office exists before the founding"
    out = _act(w, d, "e_found", "p_king", "off_king", {"subject": "T"})
    assert _kinds(out) == ["office.established"], _kinds(out)
    off = w.offices[lord]
    assert (off.post, off.rung, off.faction, off.body) == ("Lord", "T", "Valorsmark", None), off
    assert off.remit_acts == ["issue", "convene"], f"remit is the seat's less confer and revoke: {off.remit_acts}"
    assert (off.conferral, off.revocation) == ("appointed", "rung_above_in_holdings"), off
    # The post is read from `titles.domains` as data: the first post in authored order whose kind is the rung's.
    assert off.post == next(p for p, k in TITLE_DOMAINS.items() if k == "territory")


def test_cr25_2_a_founding_on_an_unheld_territory_refuses():
    w, d = _world()
    out = _act(w, d, "e_unheld", "p_king", "off_king", {"subject": "T2"})
    assert _kinds(out) == ["establish.refused"], _kinds(out)
    assert _preds.founded_office_id("T2", "Lord") not in w.offices


def test_cr25_2_planted_failure_conjunct_i_dropped_founds_on_the_unheld_territory(monkeypatch):
    """THE PLANTED FAILURE: `in_holdings` (conjunct (i)) answering True turns test 2's refusal into a
    founding -- so test 2 is red without (i), and its refusal is (i)'s and no other conjunct's."""
    monkeypatch.setattr(world_q, "in_holdings", lambda w, actor, rung: True)
    w, d = _world()
    out = _act(w, d, "e_unheld", "p_king", "off_king", {"subject": "T2"})
    assert _kinds(out) == ["office.established"], _kinds(out)


def test_cr25_3_a_founding_at_equal_rank_refuses_the_confessor_at_terr_t9():
    w = build_realm(0)
    seat = w.offices["off_confessor"]
    [holder] = [t.subject for t in w.tenures if t.kind == "hold" and t.live and t.object == "off_confessor"]
    assert seat.rung == "terr_T9" and w.rungs["terr_T9"].kind == "territory", "fixture moved"
    assert "confer" in seat.remit_acts, "fixture: the Confessor's seat grants no `confer`"
    assert world_q.in_holdings(w, holder, "terr_T9"), "fixture: (i) false, so the test would not reach rank"
    assert world_q.purview_reaches(w, seat, "terr_T9"), "(ii) is reflexive on the rung"
    assert not world_q.rung_kind_ascends("territory", w.rungs[seat.rung].kind), "(iii)"
    assert not world_q.seat_on_parent_of(w, seat, "terr_T9"), "(iv)"
    a = Act(id="e_eq", actor=holder, verb="establish", payload={"subject": "terr_T9"}, via="off_confessor")
    # `None` and NO RAISE: had the conjuncts passed, the seat's `body` would have the constructor refuse the
    # titled post (`Forbidden`), so a quiet `None` is the conjuncts' refusal, not the body's.
    assert _preds.office_founded_by(w, a) is None
    assert not _preds._req_establish(w, a)


def test_cr25_4_a_re_remit_of_a_vacant_office_outside_purview_refuses():
    w, d = _world()
    w.offices["off_reeve"] = Office("off_reeve", "Reeve", "S", ["issue"], conferral="appointed", faction="Crown")
    payload = dict(office="off_reeve", post="Reeve", rung="S", remit=["issue", "dispatch"], faction="Crown",
                   conferral="appointed")
    assert not any(t.kind == "hold" and t.object == "off_reeve" and t.live for t in w.tenures), "fixture: held"
    out = _act(w, d, "e_far", "p_other", "off_duke2", payload)
    assert _kinds(out) == ["establish.refused"], _kinds(out)
    assert w.offices["off_reeve"].remit_acts == ["issue"]
    out = _act(w, d, "e_near", "p_high", "off_duke", payload)            # control: the seat whose purview reaches S
    assert _kinds(out) == ["remit.changed"], _kinds(out)


def _seated_reeve(w, revocation):
    w.offices["off_reeve"] = Office("off_reeve", "Reeve", "S", ["issue", "dispatch"], conferral="appointed",
                                    revocation=revocation, faction="Crown")
    w.add_tenure(Tenure("t_reeve", "p_mid", "off_reeve", "hold", 0))
    return dict(office="off_reeve", post="Reeve", rung="S", faction="Crown", conferral="appointed",
                revocation=revocation)


def test_cr25_5_a_reduction_of_a_revocation_none_seats_grant_refuses():
    w, d = _world()
    payload = _seated_reeve(w, None)
    [t] = [t for t in w.tenures if t.id == "t_reeve"]
    assert t.granted_acts == ("issue", "dispatch"), t.granted_acts
    out = _act(w, d, "e_cut", "p_high", "off_duke", {**payload, "remit": ["issue"]})
    assert _kinds(out) == ["establish.refused"], _kinds(out)
    assert t.granted_acts == ("issue", "dispatch"), "the refused reduction re-stamped the grant"
    # CONTROL 1: the same seat, the same actor, a WIDENING -- the purview is there, so the refusal was the cut's.
    out = _act(w, d, "e_add", "p_high", "off_duke", {**payload, "remit": ["issue", "dispatch", "convene"]})
    assert _kinds(out) == ["remit.changed", "tenure.payload_set"], _kinds(out)


def test_cr25_5_control_a_reduction_the_seats_basis_admits_executes():
    """CONTROL 2: the reduction is refused for the BASIS, not for being a reduction -- the reeve's seat declaring
    `rung_above_same_faction`, which the duke's seat on `S`'s parent `D`, same faction, satisfies."""
    w, d = _world()
    payload = _seated_reeve(w, "rung_above_same_faction")
    out = _act(w, d, "e_cut", "p_high", "off_duke", {**payload, "remit": ["issue"]})
    assert _kinds(out) == ["remit.changed", "tenure.payload_set"], _kinds(out)


def test_cr25_6_the_founder_revokes_the_founded_lord_through_his_seat():
    w, d = _world()
    _act(w, d, "e_found", "p_king", "off_king", {"subject": "T"})
    lord = _preds.founded_office_id("T", "Lord")
    out = d.resolve(mint_token(d.w, WriteClass.ACTS),
                    [Act(id="cf", actor="p_king", verb="confer", payload={"office": lord, "to": "p_mid"},
                         via="off_king")], contest_max_depth=w.fixtures.get("contest_max_depth"))
    [h] = [t for t in w.tenures if t.kind == "hold" and t.object == lord and t.live]
    assert h.subject == "p_mid", (h, _kinds(out))
    out = d.resolve(mint_token(d.w, WriteClass.ACTS),
                    [Act(id="rv", actor="p_king", verb="revoke", payload={"office": lord}, via="off_king")],
                    contest_max_depth=w.fixtures.get("contest_max_depth"))
    assert not h.live, f"the founder's revocation did not close the Lord's hold: {_kinds(out)}"


def test_cr25_the_effect_and_the_precondition_read_one_derivation():
    """`_eff_establish` reads `office_founded_by` as `_req_establish` does: with `office_described_by` alone the
    effect would find no office on a computed act and the precondition's admission would write nothing."""
    w, _ = _world()
    a = Act(id="e", actor="p_king", verb="establish", payload={"subject": "T"}, via="off_king")
    assert _preds.office_described_by(a) is None, "a computed act carries no overlay keys"
    assert _preds._req_establish(w, a)
    from ..loop import effects_governance as G
    assert G.office_founded_by is _preds.office_founded_by


def test_cr25_holdings_to_found_on_the_realm_offers_the_dukes_their_territories():
    """The stamper on `build_realm(0)`: every holding `founds_over` admits through a `confer`-granting seat, and
    nothing for a person whose seats grant no `confer`. MEASURED at the build (14 holdings, every one a
    territory under a duchy whose duke holds it; the design's probe on the pre-CR-81 tree read 14 too)."""
    w = build_realm(0)
    found = {pid: world_q.holdings_to_found(w, p) for pid, p in w.persons.items()}
    found = {k: v for k, v in found.items() if v}
    assert sum(map(len, found.values())) == 14, found
    for pid, rungs in found.items():
        assert all(w.rungs[r].kind == "territory" and world_q.in_holdings(w, pid, r) for r in rungs), (pid, rungs)
