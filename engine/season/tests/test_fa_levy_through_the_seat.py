"""B21.59 (`06_FA_levy_through_the_seat_B`): MEN ARE LEVIED THROUGH A SEAT -- who may mint a faction's army, raise a cohort into it
and send men home, asked of the real fold on `build_realm(0)` (the realm is the fixture: the hand-planted worlds of the older army
tests never had a seat that reaches a cohort).

The rule (`state/gate.py::may_levy`, `loop/effects_army.py`, `loop/effects_information.py::_army_mintable`): `recruit` and
`discharge_troops` are exercised through a seat (`Act.via`) whose grant carries the muster act (`dispatch`), whose faction is the
army's, and whose purview reaches where the cohort lives; the faction must also be one that may raise that cohort
(`world_q.raisable_by`); the army is minted by a holder of such a seat (`gate.may_wage`). A-22: a cohort that itself holds a seat
is levied through another's only if that seat commands him (sworn to it, or a holder of a seat it may revoke).

Each refusal is paired with the one-change control that executes, so a refusal here is the rule and not a broken fixture.
"""
from __future__ import annotations

import pytest

from engine.season.boot.realm import build_realm
from engine.season.harness import army_presets as AP
from engine.season.harness import military_menu as MM
from engine.season.loop.driver import SeasonDriver, mint_token
from engine.season.data.matrix import Step, WriteClass
from engine.season.queries import world_q
from engine.season.state import gate
from engine.season.state.carriers import Office, Tenure

pytestmark = pytest.mark.flat_fold          # the fold's eligibility, not the task draw: a levy's turnout is B22's draw

VARFELL, HAFEN, CROWN = "fac_varfell", "fac_hafenmark", "fac_valorsmark"
DUKE, DUKE_SEAT, UNSEATED = "p_npc_052", "off_duke_varfell", "p_npc_002"
KING, KING_SEAT = "p_npc_020", "off_king"


def _fold(w, *acts) -> list:
    d = SeasonDriver(w)
    w.step, w.frozen = Step.RESOLVE, False
    ev = d.resolve(mint_token(w, WriteClass.ACTS), list(acts), 2)
    w.log.extend(ev)
    return [e.kind for e in ev]


def _cohorts(w, faction):
    res = world_q.residence_of(w)
    return sorted(p for p, x in w.persons.items()
                  if x.is_cohort and x.weight > 1 and world_q.holder_faction_of(w, res[p]) == faction)


def _duke_with_army():
    w = build_realm(0)
    assert "record.created" in _fold(w, MM.act_for(w, DUKE, "create_record"))
    return w


_N = [0]


def _recruit(w, who, cohort, via=None, n=10):
    """One `recruit` through the menu's act (its `via` stamped), or through `via` where a test names a seat; the act id is unique, since the
    id is derived from the payload and two seats' acts of one payload are two acts."""
    act = MM.act_for(w, who, "recruit", cohort=cohort, troop_type="levy", count=n)
    _N[0] += 1
    return _fold(w, type(act)(id=f"lv{_N[0]}", actor=act.actor, verb=act.verb, payload=act.payload, via=via or act.via))


def test_an_unseated_member_cannot_mint_the_army():
    w = build_realm(0)
    assert world_q.faction_holding(w, UNSEATED) == VARFELL and not w.seat_holds(UNSEATED), "fixture: a Varfell member who sits in no seat"
    assert not MM.menu(w, UNSEATED).mint, "the menu offers him no mint"
    assert "create_record.refused" in _fold(w, MM.act_for(w, UNSEATED, "create_record")) and world_q.army_of(w, VARFELL) is None
    # CONTROL, one change: the Duke of Varfell, who sits in a muster seat of the faction, mints it
    assert MM.menu(w, DUKE).mint
    assert "record.created" in _fold(w, MM.act_for(w, DUKE, "create_record")) and world_q.army_of(w, VARFELL) is not None


def test_the_duke_through_his_seat_mints_and_recruits_in_his_territory():
    w = _duke_with_army()
    cohort = MM.cohorts_raisable(w, DUKE)[0][0]
    assert world_q.holder_faction_of(w, world_q.residence_of(w)[cohort]) == VARFELL, "fixture: a cohort on Varfell-held ground"
    act = MM.act_for(w, DUKE, "recruit", cohort=cohort, troop_type="levy", count=10)
    assert act.via == DUKE_SEAT, "the menu stamps the seat that grants the muster act"
    assert "army.recruited" in _fold(w, act)
    assert world_q.army_of(w, VARFELL) and w.records[world_q.army_of(w, VARFELL)].subject_matter["trained"] == ((cohort, "levy", 10),)
    # the same act with no seat named is refused: a levy is the seat's exercise, not the Record-holder's
    bare = MM.act_for(w, DUKE, "recruit", cohort=cohort, troop_type="levy", count=5)
    assert "recruit.refused" in _fold(w, type(bare)(id="bare", actor=DUKE, verb="recruit", payload=bare.payload))
    # and sending men home runs through the seat too
    assert "army.discharged" in _fold(w, MM.act_for(w, DUKE, "discharge_troops", cohort=cohort, troop_type="levy", count=10))
    assert "army.recruited" in _recruit(w, DUKE, cohort)
    sent = MM.act_for(w, DUKE, "discharge_troops", cohort=cohort, troop_type="levy", count=10)
    assert "discharge_troops.refused" in _fold(w, type(sent)(id="d2", actor=DUKE, verb="discharge_troops", payload=sent.payload))


def test_a_cohort_resident_in_another_factions_territory_is_refused():
    w = _duke_with_army()
    foreign = _cohorts(w, HAFEN)[0]
    assert not world_q.raisable_by(w, foreign, VARFELL)
    assert foreign not in {c for c, _w, _s in MM.cohorts_raisable(w, DUKE)}, "the menu lists no cohort the fold refuses"
    assert "recruit.refused" in _recruit(w, DUKE, foreign)
    # the seat's own reach, apart from the faction's: a Hafenmark cohort that has committed to Varfell is one it may raise, and still lies
    # outside the Duke's ground, so the seat refuses it (`purview_reaches`) where `raisable_by` does not
    w.add_tenure(Tenure("t_sworn_over", foreign, VARFELL, "commit", since=w.tick))
    assert world_q.raisable_by(w, foreign, VARFELL) and not gate.purview_reaches(w, w.offices[DUKE_SEAT], world_q.residence_of(w)[foreign])
    assert "recruit.refused" in _recruit(w, DUKE, foreign)
    # CONTROL, one change: a cohort on the Duke's own ground
    assert "army.recruited" in _recruit(w, DUKE, _cohorts(w, VARFELL)[0])
    # the seat's faction, apart from its reach: the King's seat reaches every cohort of the realm, and raises only the Crown's army
    mine = _cohorts(w, VARFELL)[0]
    assert gate.may_levy(w, KING, KING_SEAT, mine, CROWN), "control: the King's seat reaches a Varfell cohort"
    assert not gate.may_levy(w, KING, KING_SEAT, mine, VARFELL), "a Crown seat raised a Varfell army"


def test_a_seat_without_the_muster_act_is_refused():
    w = _duke_with_army()
    w.offices["off_varfell_reeve"] = Office("off_varfell_reeve", "Reeve", "duchy_varfell", ["issue"], faction="Varfell")
    w.add_tenure(Tenure("t_reeve", DUKE, "off_varfell_reeve", "hold", since=w.tick))
    cohort = _cohorts(w, VARFELL)[0]
    assert gate.MUSTER_ACT not in next(t for t in w.seat_holds(DUKE) if t.object == "off_varfell_reeve").granted_acts
    assert "recruit.refused" in _recruit(w, DUKE, cohort, via="off_varfell_reeve")
    # CONTROL, one change: the same man, the same cohort, through the seat whose grant carries the act
    assert "army.recruited" in _recruit(w, DUKE, cohort, via=DUKE_SEAT)


def test_army_presets_mint_three_armies_by_seated_leaders():
    w = build_realm(0)
    got = AP.install(w)
    armies, counts = {f: world_q.army_of(w, f) for f in (HAFEN, CROWN, VARFELL)}, {}
    assert all(armies.values()) and {f for f in got} >= set(armies), got
    for f, rid in armies.items():
        rec = w.records[rid].subject_matter
        commander = next(t.subject for t in w.tenures if t.kind == "hold" and t.live and t.object == rid)
        assert gate.may_wage(w, commander, f), (f, commander, "minted by a man who sits in no muster seat of the faction")
        raised = {c for c, _t, _n in rec["trained"]} | {c for sf in rec["units"] for c, _n in sf["assigned"]}
        assert {t for _c, t, _n in rec["trained"]} | {sf["troop_type"] for sf in rec["units"]} == {"levy"}, "the shipped realm has no Sites: all levy"
        # the MB audit's three armies (Hafenmark 600, Valorsmark 900, Varfell 600, all levy) are 10, 15 and 10 cohorts at its scale: every cohort
        # the faction may raise is raised, so none lies outside the commander's seat (a difference would be reported by cohort name here)
        every = sorted(c for c, x in w.persons.items() if x.is_cohort and x.weight > 1 and world_q.raisable_by(w, c, f))
        assert sorted(raised) == every, (f, commander, sorted(set(every) - raised))
        counts[f] = len(raised)
    # B21b.02 (the guards ship on): the three guard cohorts are governed by the Crown's holdings, 15 -> 18 (`_governed_cohorts`' reading)
    assert counts == {HAFEN: 10, CROWN: 18, VARFELL: 10}, counts


def test_a_seated_resident_is_not_levied_unless_sworn_or_revocable():
    w = _duke_with_army()
    cohort = _cohorts(w, VARFELL)[0]
    assert gate.may_levy(w, DUKE, DUKE_SEAT, cohort, VARFELL), "control: an unseated resident is levied through the seat whose land he lives on"
    # he comes to hold a seat of his own, on the same ground: living there is no longer enough
    w.offices["off_hall_warden"] = Office("off_hall_warden", "Warden", "terr_T12", [], faction="Varfell")
    w.add_tenure(Tenure("t_warden", cohort, "off_hall_warden", "hold", since=w.tick))
    assert w.seat_holds(cohort) and not gate.may_levy(w, DUKE, DUKE_SEAT, cohort, VARFELL)
    assert "recruit.refused" in _recruit(w, DUKE, cohort)
    # sworn to the levying seat: levied (the oath is the tie)
    oath = Tenure("t_oath", cohort, DUKE_SEAT, "oblige", since=w.tick)
    w.add_tenure(oath)
    assert gate.may_levy(w, DUKE, DUKE_SEAT, cohort, VARFELL) and "army.recruited" in _recruit(w, DUKE, cohort)
    oath.until = w.tick
    assert not gate.may_levy(w, DUKE, DUKE_SEAT, cohort, VARFELL), "control: the oath ended"
    # or the holder of a seat the levying seat may revoke
    w.offices["off_hall_warden"].revocation = "rung_above_same_faction"
    assert gate.may_revoke(w, DUKE, DUKE_SEAT, w.offices["off_hall_warden"]), "fixture: the Duke may revoke the warden's seat"
    assert gate.may_levy(w, DUKE, DUKE_SEAT, cohort, VARFELL)
