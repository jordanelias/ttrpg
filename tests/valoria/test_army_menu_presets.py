"""ED-IN-0306 phase 5b and 5c -- THE HEADLESS MILITARY MENU AND THE PRESET ORDERS OF BATTLE.

The menu (`engine/season/harness/military_menu.py`) lists what a commander may ask of an army; the presets
(`harness/army_presets.py`, `modules/mass_battle/troop_types/presets.py`) raise one for a faction nobody plays. Neither adds a
rule, and this file's central claim is that: a bound the menu lists is the bound the fold enforces (accepted at the bound,
refused one past it), and a preset is a sequence of commands the verbs accept. The realm is the fixture, on purpose
(`test_army_phase5.py`'s reason); training Sites are planted where the shipped realm seats none, as a faction that had
built them would have.
"""

from __future__ import annotations

import random
import re
from pathlib import Path
from types import SimpleNamespace

import pytest

from engine.season.harness import army_presets as AP
from engine.season.harness import military_menu as MM
from engine.season.harness.play_surface import dispatching_chooser
from engine.season.harness.populated import build_realm
from engine.season.manifest.registrar import MODULE_ENTRIES
from engine.season.queries import world_q
from engine.season.queries.inputs import ArmyOptionsQuery, ArmyPresetQuery
from engine.season.seam.wrappers import mass_battle as MB
from engine.season.state.carriers import Site
from modules.mass_battle import armyrecord as A
from modules.mass_battle.config import BLOCK_SIZE, SUBUNIT_ROUT_FLOOR
from modules.mass_battle.troop_types import presets as PR
from modules.mass_battle.troop_types import recruitment as R
from modules.mass_battle.troop_types.registry import roles_for

from tests.valoria.test_army_phase5 import CHURCH, CROWN, DEFENDED_TERR, HAFEN, _fold, _governed_cohorts

_IMPORTS_PRESETS = re.compile(r"import .*army_presets|army_presets .*import|army_presets\.install")
FULL = 1000.0                                 # an arbitrary condition scale for the pure-module tests


def _sites(w, faction, kinds=("barracks", "archery_range", "stable")):
    """One full Site of each kind in every cohort of `faction`, as a faction that had built them would have."""
    res, full = world_q.residence_of(w), w.fixtures.get("condition_scale")
    for c in _governed_cohorts(w, faction):
        for k in kinds:
            w.sites[f"s_{k}_{c}"] = Site(f"s_{k}_{c}", res[c], k, condition=full)


def _commander(w, faction):
    return AP._commander(w, faction)


def _mint(w, who):
    return _fold(w, MM.act_for(w, who, "create_record"))


# ----------------------------------------------------------------------------------------- the module's `options`
def _opts(record, cohorts, others=()):
    return A.options(ArmyOptionsQuery(record, tuple(cohorts), FULL, tuple(others)))


def test_options_bound_is_the_bound_apply_enforces():
    """The falsifier of 'the menu adds no rule': for every listed (cohort, type, room), `apply` accepts `room` and refuses
    `room + 1`. A control row, a type with no Site, is absent from the list and refused at 1."""
    cohorts = (("c1", 12, {"barracks": FULL}), ("c2", 12, {"barracks": FULL / 2, "stable": FULL}))
    rec = A.new("fac_x")
    rows = _opts(rec, cohorts)["raise"]
    assert len(rows) >= 8, rows
    weight = {c: (w, s) for c, w, s in cohorts}
    for cohort, t, room in rows:
        w_, s_ = weight[cohort]
        args = {"cohort": cohort, "troop_type": t, "weight": w_, "sites": s_, "full": FULL}
        ok = A.apply(SimpleNamespace(record=rec, op="recruit", args={**args, "count": room}))
        assert A.by_type(ok)[t] == room
        with pytest.raises(ValueError):
            A.apply(SimpleNamespace(record=rec, op="recruit", args={**args, "count": room + 1}))
    listed = {(c, t) for c, t, _n in rows}
    assert ("c1", "archers") not in listed, "control: c1 has no archery range"
    with pytest.raises(ValueError):
        A.apply(SimpleNamespace(record=rec, op="recruit", args={"cohort": "c1", "troop_type": "archers", "weight": 12,
                                                                  "sites": {"barracks": FULL}, "full": FULL, "count": 1}))


def test_options_count_what_other_armies_already_hold():
    cohorts = (("c1", 12, {}),)
    cap = R.under_arms_cap(12)
    other = A.raised(A.new("fac_y"), "c1", "levy", cap)
    assert dict((c, n) for c, t, n in _opts(A.new("fac_x"), cohorts)["raise"] if t == "levy")["c1"] == cap
    assert not _opts(A.new("fac_x"), cohorts, others=(other,))["raise"], "the cohort was already raised in full elsewhere"


def test_advisories_name_the_routs():
    rec = A.form(A.new("fac_x"), "tiny", "spearmen")
    rec = A.raised(rec, "c1", "spearmen", 50)
    rec = A.assign(rec, "tiny", "c1", 50)
    kinds = {a[0]: a for a in _opts(rec, ())["advisories"]}
    assert kinds["subformation_routs"][1:] == ("tiny", 50, SUBUNIT_ROUT_FLOOR)
    assert kinds["army_routs"][2:] == (50, BLOCK_SIZE)
    # CONTROL, one change: a body the size of a unit has neither warning
    rec2 = A.assign(A.form(A.raised(A.new("fac_x"), "c1", "spearmen", 400), "line", "spearmen"), "line", "c1", 400)
    assert not {a[0] for a in _opts(rec2, ())["advisories"]} & {"subformation_routs", "army_routs"}
    rec3 = A.form(A.raised(A.new("fac_x"), "c1", "levy", 90), "pool", "levy")
    assert "unassigned" in {a[0] for a in _opts(rec3, ())["advisories"]}


# ---------------------------------------------------------------------------------------- the menu on the realm
def test_menu_follows_the_army_through_mint_and_command():
    w = build_realm(0)
    who = _commander(w, CROWN)
    assert who and MM.menu(w, who).mint and not MM.menu(w, who).commands
    assert MM.menu(w, "no_such_person") == MM.MilitaryMenu("no_such_person", None, None, False, False)
    assert "army.recruited" not in _mint(w, who) and world_q.army_of(w, CROWN)
    m = MM.menu(w, who)
    assert m.commands and not m.mint and m.army == world_q.army_of(w, CROWN)
    other = next(p for p in world_q.members(w, CROWN) if p != who)
    assert not MM.menu(w, other).commands and not MM.menu(w, other).raise_, "a member who does not hold the army"
    assert who in MM.describe(m)


def _fresh():
    w = build_realm(0)
    _sites(w, CROWN)
    who = _commander(w, CROWN)
    _mint(w, who)
    return w, who


def test_every_listed_raise_bound_is_the_fold_s_bound():
    """For a sample of the realm's rows: the menu's `room` is accepted by the real fold and `room + 1` is refused by it, in
    a world that differs only in that count."""
    w0, who = _fresh()
    rows = MM.menu(w0, who).raise_
    assert {t for _c, t, _n in rows} >= {"levy", "spearmen", "archers", "cavalry"}, "fixture: Sites unlock their types"
    checked = 0
    for cohort, t, room in rows[::9]:
        for count, kind in ((room, "army.recruited"), (room + 1, "recruit.refused")):
            w, who = _fresh()
            assert kind in _fold(w, MM.act_for(w, who, "recruit", cohort=cohort, troop_type=t, count=count)), (cohort, t, count)
            checked += 1
    assert checked >= 6


def test_a_menu_driven_army_reaches_the_battle():
    """The menu is a surface for the real chain: acts it builds raise, organise and order an army the battle reads."""
    w = build_realm(0)
    who = _commander(w, CROWN)
    _mint(w, who)
    cohorts = _governed_cohorts(w, CROWN)
    cap = R.under_arms_cap(2)
    for c in cohorts:
        assert "army.recruited" in _fold(w, MM.act_for(w, who, "recruit", cohort=c, troop_type="levy", count=cap))
    assert "army.formed" in _fold(w, MM.act_for(w, who, "form_unit", name="host", troop_type="levy"))
    m = MM.menu(w, who)
    assert sum(n for _s, _c, n in m.assign) == len(cohorts) * cap
    sf0, c0, n0 = m.assign[0]
    assert "assign_troops.refused" in _fold(w, MM.act_for(w, who, "assign_troops", name=sf0, cohort=c0, count=n0 + 1))
    for sf, c, n in m.assign:
        assert "army.assigned" in _fold(w, MM.act_for(w, who, "assign_troops", name=sf, cohort=c, count=n))
    m = MM.menu(w, who)
    assert "assign_troops.refused" in _fold(w, MM.act_for(w, who, "assign_troops", name=sf0, cohort=c0, count=-(n0 + 1)))
    assert not m.assign and sum(n for _s, _c, n in m.release) == len(cohorts) * cap and m.orders == (("host", ("Support", "Reserve")),)
    assert "army.ordered" in _fold(w, MM.act_for(w, who, "order_unit", strategy="defend"))
    assert "levy_never_closes" in {a[0] for a in MM.menu(w, who).advisories}
    # and it can be undone, which is what makes a wrong choice recoverable
    assert "army.disbanded" in _fold(w, MM.act_for(w, who, "disband_unit", name="host"))
    m = MM.menu(w, who)
    assert not m.disband and sum(n for _c, _t, n in m.discharge) == len(cohorts) * cap
    assert "army.discharged" in _fold(w, MM.act_for(w, who, "discharge_troops", cohort=cohorts[0], troop_type="levy", count=cap))


def test_act_for_refuses_what_is_not_an_army_command():
    w = build_realm(0)
    who = _commander(w, CROWN)
    with pytest.raises(ValueError):
        MM.act_for(w, who, "march", subject="x")
    with pytest.raises(ValueError, match="no army"):
        MM.act_for(w, who, "recruit", cohort="c", troop_type="levy", count=1)
    _mint(w, who)
    a1 = MM.act_for(w, who, "disband_unit", name="a")
    assert a1.id == MM.act_for(w, who, "disband_unit", name="a").id != MM.act_for(w, who, "disband_unit", name="b").id


def test_callback_hands_the_menu_to_the_client_and_returns_its_acts():
    w = build_realm(0)
    who = _commander(w, CROWN)
    seen = []

    def select(m):
        seen.append(m)
        return [MM.act_for(w, m.actor, "create_record")] if m.mint else []
    choose = dispatching_chooser(lambda p, v, s, b: ["AUTO"], {who: MM.callback(w, select)})
    got = choose(SimpleNamespace(id=who), None, None, lambda: 3)
    assert len(got) == 1 and got[0].verb == "create_record" and seen[0].mint
    assert choose(SimpleNamespace(id="someone_else"), None, None, lambda: 3) == ["AUTO"], "control: nobody else is overridden"
    assert "record.created" in _fold(w, got[0])
    many = dispatching_chooser(lambda *a: [], {who: MM.callback(w, lambda m: [MM.act_for(w, who, "create_record")] * 5)})
    assert len(many(SimpleNamespace(id=who), None, None, lambda: 2)) == 2, "DELIBERATE raises on a return over the budget"
    assert len(many(SimpleNamespace(id=who), None, None, lambda: 9)) == 5, "control: within budget, all of it"


# -------------------------------------------------------------------------------------------------- the presets
def _cohorts(n, weight=12, sites=None):
    return tuple((f"c{i:02d}", weight, dict(sites or {})) for i in range(n))


def _plan(cohorts, others=()):
    return PR.plan(ArmyPresetQuery("fac_x", tuple(cohorts), FULL, tuple(others)))


def test_plan_is_pure_and_ordered():
    cohorts = _cohorts(10, sites={"barracks": FULL, "archery_range": FULL, "stable": FULL})
    p1, p2 = _plan(cohorts), _plan(reversed(cohorts))
    assert p1 == p2 and p1, "the same facts, the same army, in whatever order the cohorts arrive"
    verbs = [v for v, _ in p1]
    assert verbs == sorted(verbs, key={"recruit": 0, "form_unit": 1, "assign_troops": 2}.get), "recruit, then form, then assign"
    forms = {c["name"]: c for v, c in p1 if v == "form_unit"}
    assert {"heavy_infantry", "crossbow", "cavalry", "levy"} <= set(forms)
    assert forms["cavalry"]["role"] == "Flanker" and forms["levy"]["role"] == "Reserve" and "role" not in forms["heavy_infantry"]


def test_the_doctrine_names_only_roles_each_type_has():
    seen = 0
    for _cls, _share, types in PR.ARM_SHARES:
        for t in types:
            assert PR.ROLE_OF[t] is None or PR.ROLE_OF[t] in roles_for(t), t
            seen += 1
    assert PR.ROLE_OF["levy"] in roles_for("levy") and seen == 11


def test_plan_without_sites_is_levy_alone_and_without_people_is_empty():
    p = _plan(_cohorts(10))
    assert {c["troop_type"] for v, c in p if v == "recruit"} == {"levy"}, "no Site, no trained troops"
    assert _plan(()) == () and _plan(_cohorts(1, weight=1)) == ()
    assert _plan(_cohorts(1, weight=3)) == (), "90 troops clear a subformation's floor but not a unit's block: it would rout at once"
    assert _plan(_cohorts(1, weight=4))[0][0] == "recruit", "control: 120 troops clear the block"


def test_plan_drops_a_group_that_would_rout_and_gives_its_room_to_the_levy():
    # six cohorts of weight 10, a stable in one only: its horse is one cohort's fifth of its cap, under the floor
    share = dict((c, s) for c, s, _t in PR.ARM_SHARES)["mounted"]
    horse = int(R.under_arms_cap(10) * share)
    assert horse < SUBUNIT_ROUT_FLOOR <= 2 * horse, "fixture: one cohort's horse routs, two cohorts' do not"
    one = _cohorts(5, 10) + (("c99", 10, {"barracks": FULL, "stable": FULL}),)
    types = {c["troop_type"] for v, c in _plan(one) if v == "recruit"}
    assert "cavalry" not in types and "heavy_infantry" in types
    # CONTROL, one change: a second stable brings the horse over the floor
    two = _cohorts(4, 10) + (("c98", 10, {"stable": FULL}), ("c99", 10, {"barracks": FULL, "stable": FULL}))
    assert "cavalry" in {c["troop_type"] for v, c in _plan(two) if v == "recruit"}


def test_plan_counts_the_claims_of_other_armies():
    cohorts = _cohorts(8, sites={"barracks": FULL})
    free = _plan(cohorts)
    held = tuple(A.raised(A.new("fac_y"), c, "levy", R.under_arms_cap(w)) for c, w, _s in cohorts)
    assert free and _plan(cohorts, others=held) == (), "every cohort is already raised in full by another army"


def _realm_crown_army(strategy="line", sites=True):
    w = build_realm(0)
    if sites:
        _sites(w, CROWN)
    return w, AP.install(w, [CROWN], strategy=strategy)


def test_install_raises_a_whole_organised_army_through_the_real_fold():
    w, got = _realm_crown_army("advance")
    kinds = got[CROWN]
    assert kinds[0] == "record.created" and not [k for k in kinds if k.endswith(".refused")], kinds
    rec = w.records[world_q.army_of(w, CROWN)].subject_matter
    assert rec["strategy"] == "advance" and not rec["trained"], "everything raised is in a subformation"
    sizes = {sf["name"]: sum(n for _c, n in sf["assigned"]) for sf in rec["subformations"]}
    assert set(sizes) == {"heavy_infantry", "crossbow", "cavalry", "levy"}, sizes
    assert min(sizes.values()) >= SUBUNIT_ROUT_FLOOR and sum(sizes.values()) == 15 * R.under_arms_cap(2) == 900
    for c in _governed_cohorts(w, CROWN):
        assert sum(A.by_type(rec, c).values()) <= R.under_arms_cap(2), "no cohort over its cap"
    # the menu agrees: nothing left to raise, and the army is sound
    cmd = next(t.subject for t in w.tenures if t.kind == "hold" and t.live and t.object == world_q.army_of(w, CROWN))
    m = MM.menu(w, cmd)
    assert m.commands and not m.raise_ and not {a[0] for a in m.advisories} & {"subformation_routs", "army_routs", "unassigned"}


def test_install_is_deterministic_idempotent_and_leaves_other_factions_alone():
    w1, g1 = _realm_crown_army()
    w2, g2 = _realm_crown_army()
    assert g1 == g2 and w1.records[world_q.army_of(w1, CROWN)].subject_matter == w2.records[world_q.army_of(w2, CROWN)].subject_matter
    assert AP.install(w1, [CROWN]) == {}, "a faction that has an army is not given a second"
    assert world_q.army_of(w1, HAFEN) is None and world_q.army_of(w1, CHURCH) is None
    assert AP.install(w1, ["fac_no_such_faction"]) == {}
    # the step and freeze it borrowed are put back
    w3 = build_realm(0)
    step, frozen = w3.step, w3.frozen
    assert AP.install(w3, [HAFEN])[HAFEN][0] == "record.created", "control: it did act"
    assert (w3.step, w3.frozen) == (step, frozen)


def test_a_realm_without_sites_gets_a_levy_army_that_holds_and_does_not_press():
    """The shipped realm seats no barracks, range or stable, so its preset army is levy alone: 900 troops, one subformation.
    A NAMED LIMIT, not a hidden one: the menu says the levy does not close, and the doctrine is what unlocks the rest."""
    w, got = _realm_crown_army(sites=False)
    rec = w.records[world_q.army_of(w, CROWN)].subject_matter
    assert [sf["troop_type"] for sf in rec["subformations"]] == ["levy"]
    cmd = next(t.subject for t in w.tenures if t.kind == "hold" and t.live and t.object == world_q.army_of(w, CROWN))
    assert "levy_never_closes" in {a[0] for a in MM.menu(w, cmd).advisories}


def _wins_vs_the_churchs_territory(sites):
    w, got = _realm_crown_army("advance", sites=sites)
    cmd = next(t.subject for t in w.tenures if t.kind == "hold" and t.live and t.object == world_q.army_of(w, CROWN))
    origin = next(r for r in world_q.ancestry(w, world_q.home_of(w)[cmd]) if w.rungs[r].kind == "settlement")
    att = world_q.mustered(w, origin, CROWN)
    assert cmd in att, "fixture: the army's commander is mustered where the army is"
    inp = MB.field_input(w, att, world_q.mustered(w, DEFENDED_TERR, CHURCH), DEFENDED_TERR, factions=(CROWN, CHURCH))
    oob = inp.orders_of_battle[0]
    assert oob is not None and sum(s.troops for s in oob.subformations) == 900
    fn = MODULE_ENTRIES["mass_battle.resolve_field"].fn
    return sum(bool(fn(inp, random.Random(s))["attacker_wins"]) for s in range(1, 9))


def test_a_preset_army_with_sites_beats_a_town_s_levy_and_the_sites_are_why():
    with_sites, levy_only = _wins_vs_the_churchs_territory(True), _wins_vs_the_churchs_territory(False)
    assert with_sites >= 5, with_sites
    assert with_sites > levy_only, ("CONTROL: the same 900 troops as levy alone", with_sites, levy_only)


def test_the_presets_are_off_by_construction():
    """Nothing in the season loop, the seam, the decision layer or the harness runners reaches `install`: a seeded run does
    not move because this exists. The falsifier is the scan itself (`checked` is asserted), and the control is that the
    one file that should mention it does."""
    root = Path(__file__).resolve().parents[2] / "engine" / "season"
    me = {"army_presets.py", "military_menu.py"}
    checked, hits = 0, []
    for p in root.rglob("*.py"):
        if "tests" in p.parts or p.name in me:
            continue
        checked += 1
        if _IMPORTS_PRESETS.search(p.read_text(encoding="utf-8", errors="replace")):
            hits.append(p.name)
    assert checked > 60 and not hits, hits
    assert re.search(r"def install", (root / "harness" / "army_presets.py").read_text(encoding="utf-8")), "control"
    probe = "from ..harness.army_presets import install"
    assert _IMPORTS_PRESETS.search(probe), "the pattern sees an import"
