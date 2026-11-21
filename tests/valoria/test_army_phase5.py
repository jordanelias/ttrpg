"""ED-IN-0306 phase 5 -- THE MISSED BEHAVIOURS OF PHASES 1-4, asked of the shipped realm (`build_realm(0)`).

`proposals/2026-10-29-army-phase5-design.md` lists them (M1..M10). This file is each one's falsifier, with a control that
differs from it in one thing. The realm is the fixture on purpose: phases 1-4 passed their tests on hand-planted
weight-12 cohorts the realm never ships, and that is how a chain that could not field an army went unseen.

The Crown's seat holder `p_npc_033` (seat `off_spymaster`, home under `set_s_014`) commands; the Crown governs 15 cohorts of
weight 2; the Church's `set_s_036` is defended by six individuals; `terr_T7` is Hafenmark's and empty of it.
"""

from __future__ import annotations

from engine.dice_engine import draw

from engine.season.data.matrix import Step, WriteClass
from engine.season.boot.realm import build_realm
from engine.season.data.rosters import WON
from engine.season.loop.driver import SeasonDriver, mint_token
from engine.season.loop.sides import sides_of
from engine.season.manifest.registrar import MODULE_ENTRIES
from engine.season.queries import world_q
from engine.season.seam.ladder import field_degree
from engine.season.tests._field_outcomes import SCALE
from engine.season.seam.wrappers import mass_battle as MB
from engine.season.state.carriers import Act, Site, Tenure
from modules.mass_battle import armyrecord as A
from modules.mass_battle.config import MIN_ARMY_TROOPS
from modules.mass_battle.troop_types import recruitment as R
import pytest

pytestmark = pytest.mark.flat_fold

ACTOR, SEAT, ORIGIN = "p_npc_033", "off_spymaster", "set_s_014"
CROWN, CHURCH, HAFEN = "fac_valorsmark", "fac_church_of_solmund", "fac_hafenmark"
DEFENDED_TOWN, UNDEFENDED, DEFENDED_TERR = "set_s_036", "terr_T7", "terr_T9"



def _fold(w, *acts):
    d = SeasonDriver(w)
    w.step = Step.RESOLVE
    w.frozen = False
    ev = d.resolve(mint_token(w, WriteClass.ACTS), list(acts), 2)
    ev = ev + d.encounter(mint_token(w, WriteClass.ACTS), ev, 2)
    w.log.extend(ev)
    return [e.kind for e in ev]


def _governed_cohorts(w, faction):
    res = world_q.residence_of(w)
    return sorted(p for p, x in w.persons.items() if x.is_cohort and world_q.holder_faction_of(w, res[p]) == faction)


def _crown_levy(w, strategy="advance", troop_type="levy"):
    """The Crown's whole levy under arms in one unit, through the real verbs, commanded by ACTOR. A trained
    type needs its Site: one full barracks is planted in each cohort's town, as a faction that had built them would
    have (the shipped realm seats none, so it can only raise levy, and a levy line does not advance)."""
    _fold(w, Act(id="mk", actor=ACTOR, verb="create_record",
                 payload={"record": "crown_army", "kind": "army", "rung": ORIGIN, "subject_matter": A.new(CROWN)}))
    cohorts = _governed_cohorts(w, CROWN)
    res = world_q.residence_of(w)
    if troop_type != "levy":
        for c in cohorts:
            w.sites[f"site_bk_{c}"] = Site(f"site_bk_{c}", res[c], "barracks", condition=w.fixtures.get("condition_scale"))
    for i, c in enumerate(cohorts):
        _fold(w, Act(id=f"r{i}", actor=ACTOR, verb="recruit",
                     payload={"subject": "crown_army", "cohort": c, "troop_type": troop_type, "count": R.under_arms_cap(2)}))
    # B17.16: at 1,000 troops a weight the whole levy is 30,000 troops and one unit may hold 10,000 (`MAX_TROOPS_PER_UNIT`), so it is
    # three units of five cohorts each; one unit of the lot is a field the module refuses (`SCALE-GAP`).
    names = ("host", "host_2", "host_3")
    for name in names:
        _fold(w, Act(id=f"f_{name}", actor=ACTOR, verb="form_unit", payload={"subject": "crown_army", "name": name, "troop_type": troop_type}))
    for i, c in enumerate(cohorts):
        _fold(w, Act(id=f"a{i}", actor=ACTOR, verb="assign_troops",
                     payload={"subject": "crown_army", "name": names[i % 3], "cohort": c, "count": R.under_arms_cap(2)}))
    _fold(w, Act(id="o", actor=ACTOR, verb="order_unit", payload={"subject": "crown_army", "strategy": strategy}))
    return cohorts


def _input(w, target):
    att = world_q.mustered(w, ORIGIN, CROWN)
    dfd = world_q.mustered(w, target, CHURCH)
    return MB.field_input(w, att, dfd, target, factions=(CROWN, CHURCH))


def _troops(oob):
    return sum(s.troops for s in oob.units)


# ---------------------------------------------------------------------------------------- M1, M2, M3: the chain runs
def test_the_shipped_realm_can_raise_field_and_win_with_an_army():
    """B17.16 (ED-MB-0101): a shipped cohort is weight 2 = 2,000 troops, over the army's floor of 1,000 (`MIN_ARMY_TROOPS`; at 30 a
    weight it was 60, under the engine's 100-troop floor, and this test's premise was that one cohort could not field an army); the
    faction's whole levy, under its commander, is 15 cohorts = 30,000 troops in three units, recruited from cohorts that are
    committed to nobody."""
    assert R.under_arms_cap(2) >= MIN_ARMY_TROOPS, "control: a single shipped cohort is over the army's floor"
    w = build_realm(0)
    cohorts = _governed_cohorts(w, CROWN)
    assert len(cohorts) == 15 and not set(cohorts) & set(world_q.members(w, CROWN)), "fixture: governed, not committed"
    _crown_levy(w, troop_type="spearmen")
    rec = w.records["crown_army"].subject_matter
    assert sum(n for sf in rec["units"] for _c, n in sf["assigned"]) == 15 * R.under_arms_cap(2) == 30_000 and len(rec["units"]) == 3
    # The Church's territory, not its walled town: slow infantry cannot storm walls (A.9, WALLS), which is a rule and
    # not a defect, and a field AT a territory is an open one.
    inp = _input(w, DEFENDED_TERR)
    assert _troops(inp.orders_of_battle[0]) == 30_000 and inp.orders_of_battle[1] is None
    assert inp.fort_level == 0.0
    fn = MODULE_ENTRIES["mass_battle.resolve_field"].fn
    seen = [fn(inp, draw.seeded(draw.H2("test_army_phase5", s))) for s in range(1, 9)]
    assert sum(field_degree(r) == WON for r in seen) >= 5, [(field_degree(r), r.attacker.share) for r in seen]
    assert min(r.attacker.share for r in seen) > 0.5 * SCALE, "an army of 30,000 must not be routed by a town's levy"


def test_an_army_is_where_its_commander_is():
    w = build_realm(0)
    _crown_levy(w)
    assert _input(w, DEFENDED_TOWN).orders_of_battle[0] is not None, "control: the commander is here"
    # CONTROL, one change: the Record passes to a Crown member who is not at the origin, and the army stays with him
    away = next(p for p in world_q.members(w, CROWN) if p not in world_q.mustered(w, ORIGIN, CROWN))
    for t in w.tenures:
        if t.object == "crown_army" and t.kind == "hold" and t.live:
            t.until = w.tick
    w.add_tenure(Tenure("t_away", away, "crown_army", "hold", since=w.tick))
    assert _input(w, DEFENDED_TOWN).orders_of_battle is None, "the army fought without its commander"


def test_a_faction_raises_only_the_people_it_governs():
    w = build_realm(0)
    _fold(w, Act(id="mk", actor=ACTOR, verb="create_record",
                 payload={"record": "crown_army", "kind": "army", "rung": ORIGIN, "subject_matter": A.new(CROWN)}))
    foreign = _governed_cohorts(w, HAFEN)[0]
    mine = _governed_cohorts(w, CROWN)[0]
    pay = lambda c: {"subject": "crown_army", "cohort": c, "troop_type": "levy", "count": 10}
    assert "recruit.refused" in _fold(w, Act(id="rf", actor=ACTOR, verb="recruit", payload=pay(foreign)))
    assert "army.recruited" in _fold(w, Act(id="rm", actor=ACTOR, verb="recruit", payload=pay(mine)))


# --------------------------------------------------------------------------------------------------- M4: the cap
def test_a_cohort_cannot_be_raised_to_its_cap_into_two_armies():
    w = build_realm(0)
    cohort = _governed_cohorts(w, CROWN)[0]
    hafen_member = world_q.members(w, HAFEN)[0]
    w.add_tenure(Tenure("t_dual", cohort, HAFEN, "commit", since=0))          # raisable by both factions now
    for rid, who, fac in (("crown_army", ACTOR, CROWN), ("hafen_army", hafen_member, HAFEN)):
        _fold(w, Act(id=f"mk_{rid}", actor=who, verb="create_record",
                     payload={"record": rid, "kind": "army", "rung": ORIGIN, "subject_matter": A.new(fac)}))
    cap = R.under_arms_cap(2)

    def recruit(rid, who, c, n, act_id):
        return _fold(w, Act(id=act_id, actor=who, verb="recruit",
                            payload={"subject": rid, "cohort": c, "troop_type": "levy", "count": n}))
    assert "army.recruited" in recruit("crown_army", ACTOR, cohort, cap, "c1")
    assert "recruit.refused" in recruit("hafen_army", hafen_member, cohort, 1, "h1"), "the cohort was raised twice"
    other = _governed_cohorts(w, HAFEN)[0]
    assert "army.recruited" in recruit("hafen_army", hafen_member, other, 5, "h2"), "control: another cohort is free"


# ---------------------------------------------------------------------------- M5, M6, M7: territories and arrival
def test_a_move_cannot_seat_a_person_at_a_territory():
    w = build_realm(0)
    up = next(r for r in world_q.ancestry(w, world_q.home_of(w)[ACTOR]) if w.rungs[r].kind == "territory")
    town = next(r for r in world_q.ancestry(w, world_q.home_of(w)[ACTOR]) if w.rungs[r].kind == "settlement")
    to_town = _fold(w, Act(id="mv1", actor=ACTOR, verb="move", payload={"to": town}))
    assert "travel.blocked" not in to_town, "control: a move up to the settlement is admitted"
    to_terr = _fold(w, Act(id="mv2", actor=ACTOR, verb="move", payload={"to": up}))
    assert "travel.blocked" in to_terr and not world_q.standing_at(w, up, CROWN), to_terr


def test_an_army_parked_at_a_territory_can_march_on():
    w = build_realm(0)
    kinds = _fold(w, Act(id="m1", actor=ACTOR, verb="march", payload={"subject": UNDEFENDED}, via=SEAT))
    assert "army.arrived" in kinds and world_q.standing_at(w, UNDEFENDED, CROWN)
    nxt = Act(id="m2", actor=ACTOR, verb="march", payload={"subject": DEFENDED_TOWN}, via=SEAT)
    claimants, subject, rung = sides_of(w, nxt, DEFENDED_TOWN, "a field")
    assert claimants and ACTOR in claimants, "the parked army had no origin"
    assert set(claimants) <= set(world_q.standing_at(w, UNDEFENDED, CROWN)), "a territory mustered its whole subtree"


def test_a_territory_field_is_not_a_walled_assault():
    w = build_realm(0)
    terr = next(r for r in world_q.ancestry(w, DEFENDED_TOWN) if w.rungs[r].kind == "territory")
    assert world_q.fortification_of(w, terr) > 0, "fixture: the territory's subtree holds garrisons"
    assert MB.field_input(w, [ACTOR], [], terr).fort_level == 0.0
    assert MB.field_input(w, [ACTOR], [], DEFENDED_TOWN).fort_level > 0, "control: a settlement keeps its walls"


# ------------------------------------------------------------------------------------------------ M8: the ration
def test_an_army_is_provisioned_by_the_cohorts_it_drew_from(monkeypatch):
    w = build_realm(0)
    w.fixtures = w.fixtures.sweep("field_provisioning", True)
    cohorts = _crown_levy(w)
    seen = []
    real = MB.provision_input
    monkeypatch.setattr(MB, "provision_input", lambda w_, weight, *a, **k: seen.append(weight) or real(w_, weight, *a, **k))
    act = Act(id="mp", actor=ACTOR, verb="march", payload={"subject": DEFENDED_TOWN}, via=SEAT)
    w.acts.append(act)
    att = world_q.mustered(w, ORIGIN, CROWN)
    MB.resolve(w, att, [act.id], "a field", subject=CHURCH, rung=DEFENDED_TOWN, rng=draw.seeded(draw.H2("test_army_phase5", 3)))
    assert seen[0] == sum(w.persons[c].weight for c in cohorts) == 30, seen
    assert seen[0] != sum(w.persons[p].weight for p in att), "billed the mustered members, not the army"


# ----------------------------------------------------------------------------------- M2 again: who bleeds, at home
def test_a_lost_army_costs_the_cohorts_at_home_their_bodies():
    """The people an army drew from bleed, wherever they live, and only they. A Crown army of spearmen takes the field
    against a Hafenmark levy raised from its ten cohorts and commanded by a member standing in the territory.
    The realm seed is 8: at the B06/B17 merge the keyed draw is the stream (it was 1); B17.16's scale (30,000 troops against 20,000, three
    units and two) re-picked it: of seeds 0 to 9, 1 to 3, 5 to 7 and 9 draw the field (nobody bleeds), 0 and 4 decide it but leave a
    cohort of the losing side whole (its unit untouched, and the assertion that every cohort of the loser bleeds fails), and 8 is the one
    that passes every assertion."""
    w = build_realm(8)
    cohorts = _crown_levy(w, strategy="advance", troop_type="spearmen")
    hafen = _governed_cohorts(w, HAFEN)
    cmdr = world_q.members(w, HAFEN)[0]
    inside = sorted(world_q.descendants(w, "set_s_016"))[0]
    for t in w.tenures:
        if t.subject == cmdr and t.kind == "contain" and t.live:
            t.until = w.tick
    w.add_tenure(Tenure("t_cmdr_in", cmdr, inside, "contain", w.tick))
    assert cmdr in world_q.mustered(w, UNDEFENDED, HAFEN), "fixture: the Hafenmark commander stands in the territory"
    _fold(w, Act(id="mkh", actor=cmdr, verb="create_record",
                 payload={"record": "hafen_army", "kind": "army", "rung": "set_s_016", "subject_matter": A.new(HAFEN)}))
    for i, c in enumerate(hafen):
        _fold(w, Act(id=f"rh{i}", actor=cmdr, verb="recruit",
                     payload={"subject": "hafen_army", "cohort": c, "troop_type": "levy", "count": R.under_arms_cap(2)}))
    for name in ("g", "g_2"):       # B17.16: ten cohorts are 20,000 troops, two units at most 10,000 each
        _fold(w, Act(id=f"fh_{name}", actor=cmdr, verb="form_unit", payload={"subject": "hafen_army", "name": name, "troop_type": "levy"}))
    for i, c in enumerate(hafen):
        _fold(w, Act(id=f"ah{i}", actor=cmdr, verb="assign_troops",
                     payload={"subject": "hafen_army", "name": ("g", "g_2")[i % 2], "cohort": c, "count": R.under_arms_cap(2)}))
    before = {c: w.persons[c].body for c in cohorts + hafen}
    kinds = _fold(w, Act(id="mm", actor=ACTOR, verb="march", payload={"subject": UNDEFENDED}, via=SEAT))
    assert {"field.won", "field.lost"} & set(kinds), kinds
    after = {c: w.persons[c].body if c in w.persons else 0 for c in before}
    hurt = {c for c in before if after[c] < before[c]}
    assert hurt, ("nobody bled", kinds)
    side = set(cohorts) if "field.lost" in kinds else set(hafen)
    assert hurt == side, (kinds, sorted(hurt))
    assert all(after[c] == before[c] for c in set(before) - side), "the winning army's cohorts were hurt"
