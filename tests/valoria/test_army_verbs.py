"""ED-IN-0305 phase 2 -- THE ARMY RECORD AND THE FOUR VERBS THAT CHANGE IT, asked of the real fold and gate.

What the position built: a faction's army is a `Record` of kind `army` (`rosters.yaml: record_kinds`), minted by the
`create_record` that already ran and changed afterwards by `recruit`, `form_unit`, `assign_troops` and `order_unit`
(`loop/effects_army.py`), the one Record kind with a `(Record, subject_matter)` write. The record's content and the
recruiting limit are `modules/mass_battle/armyrecord.py`'s (tested without a world in
`tests/valoria/test_mass_battle_army_record.py`); THIS file asks what only the season can: that a verb reaches the
module through the composition row, that the gate admits the write, that the holder's standing and the army kind
are enforced, and that each refusal leaves the record exactly as it was.

Fixture: `probes.tiny_world` plus a faction Proposition `fac_crown`, a cohort `c1` (weight 12, so 120 may be under
arms) living at `Hh` and committed to it, and a full barracks at `Hh`. `p_high` mints and so holds the army.
"""

from __future__ import annotations

from engine.season.data.fixtures import DEFAULT_FIXTURES
from engine.season.data.matrix import WriteClass
from engine.season.harness import probes as P
from engine.season.loop.driver import SeasonDriver, mint_token
from engine.season.queries import world_q
from engine.season.state.carriers import Act, Proposition, Site, Tenure

FACTION, COHORT, HOME, COMMANDER = "fac_crown", "c1", "Hh", "p_high"


def _world():
    w = P.tiny_world(DEFAULT_FIXTURES)
    w.propositions[FACTION] = Proposition(FACTION, "HOLDS", "Crown", "is a faction of this world", True, 0)
    P.plant_cohort(w, COHORT, HOME, weight=12)
    w.add_tenure(Tenure("t_c1_commit", COHORT, FACTION, "commit", since=0))
    w.add_tenure(Tenure("t_cmd_commit", COMMANDER, FACTION, "commit", since=0))     # the commander is of the faction
    scale = w.fixtures.get("condition_scale")
    w.sites["site_barracks"] = Site("site_barracks", HOME, "barracks", condition=scale)
    d = SeasonDriver(w)
    d.matter(mint_token(w, WriteClass.MATTER), [])
    return w, d


def _fold(w, d, *acts):
    out = d.resolve(mint_token(w, WriteClass.ACTS), list(acts), contest_max_depth=w.fixtures.get("contest_max_depth"))
    w.log.extend(out)
    return out


def _kinds(events):
    return [e.kind for e in events]


def _mint(w, d, key="army1", faction=FACTION, content=None, actor=COMMANDER):
    from modules.mass_battle import armyrecord as A
    return _fold(w, d, Act(id=f"mint_{key}", actor=actor, verb="create_record",
                           payload={"record": key, "kind": "army", "rung": "S",
                                    "subject_matter": A.new(faction) if content is None else content}))


def _do(w, d, verb, act_id, actor=COMMANDER, subject="army1", **payload):
    return _fold(w, d, Act(id=act_id, actor=actor, verb=verb, payload={"subject": subject, **payload}))


def _army(w, key="army1"):
    return w.records[key].subject_matter


def _armed(w, d):
    _mint(w, d)
    return w, d


# ---------------------------------------------------------------------------------------------------- the mint
def test_an_army_is_minted_whole_one_per_faction_and_held_by_its_maker():
    w, d = _world()
    out = _mint(w, d)
    assert _kinds(out) == ["record.created"], _kinds(out)
    assert w.records["army1"].kind == "army" and _army(w)["faction"] == FACTION
    assert world_q.hold_force(w, "army1").subject == COMMANDER and world_q.army_of(w, FACTION) == "army1"
    # CONTROLS, each the same act changed in one thing: a second army for the faction, an unknown faction, and a
    # record that is not well formed (an unknown strategy) are all declined and mint nothing.
    again = _mint(w, d, key="army2")
    assert _kinds(again) == ["act.refused"] and "army2" not in w.records, _kinds(again)
    stranger = _mint(w, d, key="army3", faction="fac_nobody")
    assert _kinds(stranger) == ["act.refused"] and "army3" not in w.records
    bad = _mint(w, d, key="army4", faction=FACTION, content={**_army(w), "strategy": "rout"})
    assert _kinds(bad) == ["act.refused"] and "army4" not in w.records


# ------------------------------------------------------------------------------------------ recruit and refuse
def test_recruit_raises_troops_up_to_the_limit_the_population_and_the_barracks_allow():
    w, d = _armed(*_world())
    from modules.mass_battle.troop_types.recruitment import under_arms_cap
    cap = under_arms_cap(12)                         # the cohort's weight, at the ruled scale
    out = _do(w, d, "recruit", "r1", cohort=COHORT, troop_type="heavy_infantry", count=100)
    assert "army.recruited" in _kinds(out), _kinds(out)
    assert _army(w)["trained"] == ((COHORT, "heavy_infantry", 100),)
    # the rest of the cap fits, one more does not (and the refusal leaves the record as it was)
    before = _army(w)
    over = _do(w, d, "recruit", "r2", cohort=COHORT, troop_type="heavy_infantry", count=cap - 100 + 1)
    assert "recruit.refused" in _kinds(over) and _army(w) == before, _kinds(over)
    ok = _do(w, d, "recruit", "r3", cohort=COHORT, troop_type="heavy_infantry", count=cap - 100)
    assert "army.recruited" in _kinds(ok) and _army(w)["trained"] == ((COHORT, "heavy_infantry", cap),)


def test_a_troop_type_needs_its_own_kind_of_training_site():
    w, d = _armed(*_world())
    refused = _do(w, d, "recruit", "r1", cohort=COHORT, troop_type="archers", count=10)
    assert "recruit.refused" in _kinds(refused) and _army(w)["trained"] == (), "a barracks must not train archers"
    scale = w.fixtures.get("condition_scale")
    w.sites["site_range"] = Site("site_range", HOME, "archery_range", condition=scale)
    ok = _do(w, d, "recruit", "r2", cohort=COHORT, troop_type="archers", count=10)
    assert "army.recruited" in _kinds(ok) and _army(w)["trained"] == ((COHORT, "archers", 10),)
    # levy is the control: it needs no site at all
    levy = _do(w, d, "recruit", "r3", cohort=COHORT, troop_type="levy", count=5)
    assert "army.recruited" in _kinds(levy)


def test_recruit_refuses_what_is_not_a_cohort_of_the_armys_faction():
    w, d = _armed(*_world())
    w.add_tenure(Tenure("t_low_commit", "p_low", FACTION, "commit", since=0))      # a member, so only weight 1 refuses
    for who, why in (("p_low", "an individual (weight 1)"), ("p_nobody", "no such person")):
        out = _do(w, d, "recruit", f"r_{who}", cohort=who, troop_type="levy", count=1)
        assert "recruit.refused" in _kinds(out), (why, _kinds(out))
    P.plant_cohort(w, "c_other", HOME, weight=12)             # a cohort that never committed to the faction
    out = _do(w, d, "recruit", "r_other", cohort="c_other", troop_type="levy", count=1)
    assert "recruit.refused" in _kinds(out) and _army(w)["trained"] == ()


def test_the_holder_alone_commands_and_only_an_army_is_commanded():
    w, d = _armed(*_world())
    out = _do(w, d, "recruit", "r1", actor="p_mid", cohort=COHORT, troop_type="levy", count=5)
    assert "recruit.refused" in _kinds(out) and _army(w)["trained"] == (), "p_mid does not hold the army"
    _fold(w, d, Act(id="mk_text", actor=COMMANDER, verb="create_record",
                    payload={"record": "doc", "kind": "text", "subject_matter": None, "rung": "S"}))
    out = _do(w, d, "recruit", "r2", subject="doc", cohort=COHORT, troop_type="levy", count=5)
    assert "recruit.refused" in _kinds(out) and w.records["doc"].subject_matter is None


# -------------------------------------------------------------------------- form, assign, order: the whole menu
def test_form_assign_and_order_build_the_order_of_battle_and_conserve_every_trooper():
    from modules.mass_battle import armyrecord as A
    w, d = _armed(*_world())
    _do(w, d, "recruit", "r1", cohort=COHORT, troop_type="heavy_infantry", count=60)
    formed = _do(w, d, "form_unit", "f1", name="wall", troop_type="heavy_infantry", role="ShieldWall")
    assert "army.formed" in _kinds(formed), _kinds(formed)
    moved = _do(w, d, "assign_troops", "a1", name="wall", cohort=COHORT, count=45)
    assert "army.assigned" in _kinds(moved) and A.by_type(_army(w)) == {"heavy_infantry": 60}
    assert A.unassigned(_army(w), COHORT, "heavy_infantry") == 15
    released = _do(w, d, "assign_troops", "a2", name="wall", cohort=COHORT, count=-5)
    assert "army.assigned" in _kinds(released) and A.unassigned(_army(w), COHORT, "heavy_infantry") == 20
    ordered = _do(w, d, "order_unit", "o1", name="wall", stance="hold", fall_back_at=0.4)
    assert "army.ordered" in _kinds(ordered)
    sf = _army(w)["subformations"][0]
    assert (sf["stance"], sf["fall_back_at"], sf["role"], sf["assigned"]) == ("hold", 0.4, "ShieldWall", ((COHORT, 40),))
    strat = _do(w, d, "order_unit", "o2", strategy="advance")
    assert "army.ordered" in _kinds(strat) and _army(w)["strategy"] == "advance"
    A.validate(_army(w))
    oob = A.to_order_of_battle(_army(w))                       # the record the season holds is the battle's input
    assert [s.name for s in oob.subformations] == ["wall"] and oob.strategy == "advance"


def test_each_menu_refusal_leaves_the_record_as_it_was():
    w, d = _armed(*_world())
    _do(w, d, "recruit", "r1", cohort=COHORT, troop_type="heavy_infantry", count=30)
    _do(w, d, "form_unit", "f1", name="wall", troop_type="heavy_infantry")
    before = _army(w)
    cases = (("form_unit", dict(name="wall", troop_type="levy")),                        # duplicate name
             ("form_unit", dict(name="x", troop_type="dragons")),                        # unknown type
             ("form_unit", dict(name="x", troop_type="heavy_infantry", role="Kite")),    # role outside the menu
             ("assign_troops", dict(name="wall", cohort=COHORT, count=31)),              # more than trained
             ("assign_troops", dict(name="nobody", cohort=COHORT, count=1)),             # no such subformation
             ("assign_troops", dict(name="wall", cohort=COHORT, count=-1)),              # releases what is not held
             ("order_unit", dict(name="wall", stance="retreat")),                        # stance outside the roster
             ("order_unit", dict(name="wall", fall_back_at=1.5)),
             ("order_unit", dict(name="wall")),                                          # an order that sets nothing
             ("order_unit", dict(strategy="rout")))
    for i, (verb, payload) in enumerate(cases):
        out = _do(w, d, verb, f"bad{i}", **payload)
        assert f"{verb}.refused" in _kinds(out), (verb, payload, _kinds(out))
        assert _army(w) == before, (verb, payload)


def test_the_army_verbs_are_withheld_from_formation_so_no_person_forms_them():
    """The command is the act's payload, which no Candidate carries: a computed act could not bind it."""
    from engine.season.data.rosters import ARMY_VERBS
    from engine.season.data.verbs import VERB_TABLE
    assert len(ARMY_VERBS) == 6 and set(ARMY_VERBS) <= set(VERB_TABLE), "vacuous unless six real verbs"
    assert set(ARMY_VERBS) <= set(DEFAULT_FIXTURES.get("withheld_verbs"))


# ----------------------------------------------------------------- the close's findings: mint, payload, holder
def test_an_army_is_minted_empty_so_the_recruiting_rule_cannot_be_skipped():
    from modules.mass_battle import armyrecord as A
    w, d = _world()
    full = A.raised(A.new(FACTION), COHORT, "knights_templar", 100000)             # no cap, no stable
    out = _mint(w, d, key="army_full", content=full)
    assert _kinds(out) == ["act.refused"] and "army_full" not in w.records, _kinds(out)
    formed = A.form(A.new(FACTION), "wall", "levy")
    assert _kinds(_mint(w, d, key="army_sf", content=formed)) == ["act.refused"]
    assert _kinds(_mint(w, d, key="army_ok")) == ["record.created"], "control: the same mint, empty, is admitted"


def test_a_proposition_that_is_not_a_faction_has_no_army():
    w, d = _world()
    w.propositions["prop_idea"] = Proposition("prop_idea", "HOLDS", "Idea", "is just a thought", True, 0)
    out = _mint(w, d, key="army_idea", faction="prop_idea")
    assert _kinds(out) == ["act.refused"] and "army_idea" not in w.records, _kinds(out)


def test_a_missing_or_mistyped_payload_field_is_a_refusal_not_a_crash():
    w, d = _armed(*_world())
    before = _army(w)
    cases = (("form_unit", dict(troop_type="levy")),                          # no name
             ("assign_troops", dict(name="x", cohort=COHORT)),                # no count
             ("recruit", dict(cohort=COHORT, troop_type="levy", count=None)),
             ("order_unit", dict(stance="hold")),                             # no name
             ("order_unit", dict(name="x", fall_back_at="soon")),
             ("recruit", dict(cohort=[COHORT], troop_type="levy", count=1)),  # unhashable: a dict key must not be tried
             ("form_unit", dict(name=["x"], troop_type="levy")),              # a name no string would crash the battle
             ("form_unit", dict(name=5, troop_type="levy")))
    for i, (verb, payload) in enumerate(cases):
        out = _do(w, d, verb, f"bad_pl{i}", **payload)
        assert f"{verb}.refused" in _kinds(out), (verb, payload, _kinds(out))
        assert _army(w) == before


def test_an_army_whose_faction_is_no_string_is_refused_not_a_crash():
    from modules.mass_battle import armyrecord as A
    w, d = _world()
    out = _mint(w, d, key="army_list", content={**A.new(FACTION), "faction": [FACTION]})
    assert _kinds(out) == ["act.refused"] and "army_list" not in w.records, _kinds(out)


def test_an_army_whose_holder_is_gone_frees_its_factions_slot():
    """A dead holder strands the army (every verb needs the holder). It must not also lock the faction out of ever
    minting another."""
    w, d = _armed(*_world())
    assert world_q.army_of(w, FACTION) == "army1"
    for t in w.tenures:                                  # the holder is gone: the hold on the army closed with him
        if t.object == "army1" and t.kind == "hold" and t.live:
            t.until = w.tick
    assert world_q.army_of(w, FACTION) is None, "an army nobody holds is nobody's army"
    w.add_tenure(Tenure("t_heir_commit", "p_mid", FACTION, "commit", since=w.tick))      # an heir of the same faction
    out = _mint(w, d, key="army2", actor="p_mid")
    assert _kinds(out) == ["record.created"] and world_q.army_of(w, FACTION) == "army2", _kinds(out)


def test_only_a_member_of_the_faction_raises_or_commands_its_army():
    """Otherwise a rival could mint the Church's army and lock it out, or be handed the Record and field one levy for
    it. CONTROLS: the committed commander mints and commands (every other test); here one change each."""
    w, d = _world()
    out = _mint(w, d, key="army_rival", actor="p_mid")                        # p_mid is of no faction
    assert _kinds(out) == ["act.refused"] and "army_rival" not in w.records, _kinds(out)
    _mint(w, d)
    for t in w.tenures:                                                       # the Record passes to p_mid by hand
        if t.object == "army1" and t.kind == "hold" and t.live:
            t.until = w.tick
    w.add_tenure(Tenure("t_handed", "p_mid", "army1", "hold", since=w.tick))
    refused = _do(w, d, "recruit", "r_out", actor="p_mid", cohort=COHORT, troop_type="levy", count=5)
    assert "recruit.refused" in _kinds(refused) and _army(w)["trained"] == (), "a holder who is no member commanded it"
    w.add_tenure(Tenure("t_mid_commit", "p_mid", FACTION, "commit", since=w.tick))
    ok = _do(w, d, "recruit", "r_in", actor="p_mid", cohort=COHORT, troop_type="levy", count=5)
    assert "army.recruited" in _kinds(ok), _kinds(ok)
