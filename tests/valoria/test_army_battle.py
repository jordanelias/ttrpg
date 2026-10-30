"""ED-IN-0306 phase 3 -- THE ARMY RECORD FIGHTS: `field_input` reads each side's army Record into the battle.

What the position built: a side whose faction holds an `army` Record fights as that Record's order of battle
(`seam/wrappers/mass_battle.py::_order_of_battle`, through the `mass_battle.army_order` composition row), the
cohorts present on the field at their body fraction. Casualties need no write of their own: `march` already scales a
losing side's bodies, so the next field is smaller by exactly that. THIS file asks what only the season can: who is
on the field, how fit, which side's faction, and that a field with no army Record is the field it always was.

Fixture: `test_levy_feed.py`'s realm (`build_realm(0)`), the Crown marching `set_s_014` -> `set_s_036` where the
Church of Solmund stands, plus one cohort of weight 12 planted on each side and committed to its faction, and an
army Record for each whose one subformation holds that cohort's whole 120.
"""

from __future__ import annotations

import random
from types import SimpleNamespace

import pytest

from engine.season.data.matrix import Step, WriteClass
from engine.season.harness import probes as P
from engine.season.harness.populated import build_realm
from engine.season.loop.driver import SeasonDriver, mint_token
from engine.season.manifest.registrar import MODULE_ENTRIES
from engine.season.queries import world_q
from engine.season.seam.wrappers.mass_battle import field_input, resolve
from engine.season.state.carriers import Act, Record, Tenure

ACTOR, SEAT, ORIGIN, TARGET = "p_npc_033", "off_npc_033", "set_s_014", "set_s_036"
ATTACKER, DEFENDER = "fac_crown", "fac_church_of_solmund"
CA, CD = "c_att", "c_def"


@pytest.fixture(autouse=True, scope="module")
def _module_entries_registered():
    SeasonDriver(build_realm(0))


def _army(faction, cohort, troop_type="heavy_infantry", n=120, role=None, **order):
    from modules.mass_battle import armyrecord as A
    r = A.raised(A.new(faction), cohort, troop_type, n)
    r = A.assign(A.form(r, "wall", troop_type, role=role), "wall", cohort, n)
    return A.order(r, "wall", **order) if order else r


def _world(attacker_army=True, defender_army=True, defender_role="ShieldWall"):
    w = build_realm(0)
    for cid, rung, fac in ((CA, ORIGIN, ATTACKER), (CD, TARGET, DEFENDER)):
        P.plant_cohort(w, cid, rung, weight=12)
        w.add_tenure(Tenure(f"t_{cid}_commit", cid, fac, "commit", since=0))
    scale = w.fixtures.get("condition_scale")
    assert world_q.mustered(w, ORIGIN, ATTACKER).count(CA) == 1 and CD in world_q.mustered(w, TARGET, DEFENDER)
    for flag, rid, fac, cid in ((attacker_army, "army_a", ATTACKER, CA), (defender_army, "army_d", DEFENDER, CD)):
        if flag:
            w.records[rid] = Record(rid, TARGET, "army", subject_matter=_army(fac, cid, role=None if fac == ATTACKER else defender_role))
            # an army is its faction's only while somebody holds it (`world_q.army_of`)
            w.add_tenure(Tenure(f"t_{rid}_hold", world_q.members(w, fac)[0], rid, "hold", since=0))
    return w, scale


def _input(w):
    attackers = world_q.mustered(w, ORIGIN, ATTACKER)
    defenders = world_q.mustered(w, TARGET, DEFENDER)
    return field_input(w, attackers, defenders, TARGET, factions=(ATTACKER, DEFENDER))


def _troops(oob):
    return sum(sf.troops for sf in oob.subformations)


# --------------------------------------------------------------------------------------------- who fights as what
def test_a_world_with_no_army_record_builds_the_field_it_always_did():
    w, _ = _world(attacker_army=False, defender_army=False)
    assert _input(w).orders_of_battle is None, "no army Record anywhere must leave the record exactly as it was"
    assert world_q.army_of(w, ATTACKER) is None and world_q.army_of(w, DEFENDER) is None


def test_each_side_with_an_army_record_fights_as_that_records_order_of_battle():
    w, _ = _world()
    oob_a, oob_d = _input(w).orders_of_battle
    assert [s.name for s in oob_a.subformations] == ["wall"] and [s.name for s in oob_d.subformations] == ["wall"]
    assert (_troops(oob_a), _troops(oob_d)) == (120, 120)
    # the defender holds its ground behind a shield wall and the attacker does not: two held lines never close
    assert oob_a.subformations[0].role is None and oob_d.subformations[0].role == "ShieldWall"
    assert oob_a.subformations[0].troop_type == "heavy_infantry"


def test_a_side_without_an_army_record_is_none_while_the_other_fights_its_own():
    w, _ = _world(defender_army=False)
    oob_a, oob_d = _input(w).orders_of_battle
    assert oob_a is not None and oob_d is None
    # the control: the same world with the attacker's Record gone is the old field (both None -> record None)
    w2, _ = _world(attacker_army=False, defender_army=False)
    assert _input(w2).orders_of_battle is None


def test_the_orders_a_faction_sets_reach_the_battle():
    from modules.mass_battle import armyrecord as A
    w, _ = _world()
    base = _input(w).orders_of_battle[0]
    rec = w.records["army_a"]
    rec.subject_matter = A.set_strategy(A.order(rec.subject_matter, "wall", stance="hold", fall_back_at=0.4), "advance")
    oob = _input(w).orders_of_battle[0]
    sf = oob.subformations[0]
    assert (oob.strategy, sf.stance, sf.fall_back_at) == ("advance", "hold", 0.4)
    assert (base.strategy, base.subformations[0].stance) == ("line", None), "vacuous if the base already had the orders"


# ------------------------------------------------------------------------------------- who is there, and how fit
def test_a_cohort_not_on_the_field_fights_with_nobody():
    w, _ = _world()
    # the cohort is not among those mustered at the origin (it marched elsewhere): the side is everybody else
    attackers = [p for p in world_q.mustered(w, ORIGIN, ATTACKER) if p != CA]
    assert attackers, "vacuous without other attackers"
    inp = field_input(w, attackers, world_q.mustered(w, TARGET, DEFENDER), TARGET, factions=(ATTACKER, DEFENDER))
    oob_a, oob_d = inp.orders_of_battle
    assert oob_a is None and oob_d is not None, "an army with nobody present must read as absent, not crash"


def test_troops_on_the_field_are_the_cohorts_body_fraction_of_its_assignment():
    w, scale = _world()
    full = _troops(_input(w).orders_of_battle[0])
    w.persons[CA].body = scale // 2
    half = _troops(_input(w).orders_of_battle[0])
    assert full == 120 and half == 60, (full, half)
    w.persons[CA].body = 0
    assert _input(w).orders_of_battle[0] is None, "a cohort with no body left fights with nobody"


# -------------------------------------------------------------------------------------------- the scale of the rest
def test_a_side_without_an_order_of_battle_is_scaled_to_the_troops_it_could_raise():
    """A headcount side meeting an order of battle counts households against troops unless scaled: weight 12 must
    field what a weight-12 cohort can put under arms, not twelve."""
    from modules.mass_battle import massbattle as MBT
    from modules.mass_battle.troop_types.recruitment import under_arms_cap
    unit = MBT._oob_unit(None, 12, "B", 5)
    assert unit.total_troops() == under_arms_cap(12) > 12, unit.total_troops()
    assert MBT._oob_unit(None, 0, "B", 5).total_troops() >= 1, "an empty side keeps the crash floor"


# ----------------------------------------------------------------------------------------- the provider, end to end
def _march_act(act_id="m1"):
    return Act(id=act_id, actor=ACTOR, verb="march", payload={"subject": TARGET}, via=SEAT)


def test_the_provider_names_each_sides_faction_and_the_entry_receives_both_orders(monkeypatch):
    from engine.season.seam.wrappers import mass_battle as MB
    seen = []
    real = MODULE_ENTRIES["mass_battle.resolve_field"]

    def fn(inp, rng, **kw):
        seen.append(inp.orders_of_battle)
        return real.fn(inp, rng, **kw)
    monkeypatch.setattr(MB, "entry_for", lambda prize, module: (SimpleNamespace(fn=fn), None))
    w, _ = _world()
    act = _march_act()
    w.acts.append(act)
    attackers = world_q.mustered(w, ORIGIN, ATTACKER)
    r = resolve(w, attackers, [act.id], "a field", subject=DEFENDER, rung=TARGET, rng=random.Random(11))
    assert r["status"] == "RESOLVED" and r["unopposed"] is False, r
    (oobs,) = seen
    assert oobs[0] is not None and oobs[1] is not None, "the provider did not find both factions' armies"
    assert (_troops(oobs[0]), _troops(oobs[1])) == (120, 120)


def _fold(w, *acts):
    d = SeasonDriver(w)
    w.step = Step.RESOLVE
    w.frozen = False
    events = d.resolve(mint_token(w, WriteClass.ACTS), list(acts), 2)
    events = events + d.encounter(mint_token(w, WriteClass.ACTS), events, 2)
    w.log.extend(events)
    return events


def test_a_fought_field_costs_the_loser_its_bodies_and_so_its_next_army():
    """THE CASUALTY LOOP, through the real fold: no write of the army Record, yet the side that lost fields fewer
    troops next time, by exactly its cohort's body fraction. The winner's cohort is untouched."""
    # two plain lines: a held shield wall against a balanced line can end with nobody having closed (no casualties)
    w, scale = _world(defender_role=None)
    others = {p: w.persons[p].body for p in set(world_q.mustered(w, ORIGIN, ATTACKER) + world_q.mustered(w, TARGET, DEFENDER))
              if p not in (CA, CD)}
    assert len(others) >= 3, "vacuous without bystanders mustered beside the two cohorts"
    events = _fold(w, _march_act())
    kinds = {e.kind for e in events}
    assert kinds & {"field.won", "field.lost"}, sorted(kinds)
    bodies = {CA: w.persons[CA].body if CA in w.persons else 0, CD: w.persons[CD].body if CD in w.persons else 0}
    hurt = [c for c, b in bodies.items() if b < scale]
    assert len(hurt) == 1, ("exactly one side loses", bodies)
    loser, rid = (CA, "army_a") if hurt == [CA] else (CD, "army_d")
    assert w.records[rid].subject_matter == _army(ATTACKER if loser == CA else DEFENDER, loser,
                                                         role=None), (
        "the fight must not rewrite the Record")
    if bodies[loser] > 0:
        oob = _input(w).orders_of_battle[0 if loser == CA else 1]
        assert abs(_troops(oob) - 120 * bodies[loser] / scale) < 1e-6, (_troops(oob), bodies)
    else:
        assert _input(w).orders_of_battle[0 if loser == CA else 1] is None

    # WHO BLEEDS IS WHO FOUGHT: the people mustered beside the cohorts, in neither army, are not scaled by a fight
    # they were not in. (They were, before `parties["fielded"]`: the headcount path writes every mustered loser.)
    assert {p: w.persons[p].body for p in others if p in w.persons} == others, "a bystander was hurt by the fight"
