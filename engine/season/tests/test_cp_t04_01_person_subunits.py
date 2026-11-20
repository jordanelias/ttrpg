"""CP-T04-01 (`H-359`): a side is its persons -- `field_units: person` builds one subunit per commanding person and
`_eff_march` scales each loser's body by HIS subunit's survivor ratio; `side`, shipped, is the field as it was.

THE FIELD IS HAND-BUILT, NOT NATURAL. One season of the shipped realm fights almost no field (seed 0: `field.unopposed`
3, `march.declared` 6; seed 1: unopposed 2, declared 3; seed 2: `field.lost` 1), so the falsifier runs on a real fold of
`set_s_014` marching on `set_s_036` with the Crown's two marchers at `Person.weight` `WEIGHT` and the Church's six at
`DEFENDER_WEIGHT`. A weight is 30 troops (`under_arms_cap`, B17.01's one scale), so a weight-1 person is 30 troops, under
`UNIT_ROUT_FLOOR = 80`, and every subunit of the shipped realm routs on tick 1 (a `Drawn` field nobody is hurt in); a marcher
of weight 3 is 90. The realm at `SEED` loses the field with ONE marcher's subunit routed and the other's untouched (the preconditions
are asserted below, so a moved fixture reads as a precondition, not a pass). RE-PICKED by B17.01 (the scale, the placement
by `orderofbattle._place` and the three-way grade moved every fight): of a grid of marcher weights 3 to 8, defender weights 3
to 10 and seeds 0 to 13, the case the claims need (the first marcher untouched at his full body, the second cut and named
by the band Event) is read at marcher weight 3 only: (3, 7, seed 3), (3, 8, seed 7), (3, 10, seeds 4 and 7). Seed and weights
are the helper's own knobs; the claims below are unchanged.

The cases: the falsifier (different bodies under `person`, identical under `side`), its planted failure (the side's ratio
fed to every person: the same check reddens), the control (`side` writes today's bodies and carries no per-person
key), the cause (the Event names the loser whose subunit broke first, and `run_battle`'s own order of breaking records it, B17.03), and the
shape of the `person` arm (one subunit per member, sized by his own weight, the provisioned troops spread by weight)."""
from __future__ import annotations

import importlib
from engine.dice_engine import draw

import pytest

from engine.season.boot.realm import build_realm
from engine.season.queries import world_q
from engine.season.queries.inputs import MassBattleInput
from engine.season.tests.test_march import _fold_one, _march_act, _weigh
from engine.season.tests._field_outcomes import SCALE

# B17.01 RE-PICKED (see the docstring): was seed 7, weight 1, scale 200 (B05.99: seed 8 before it).
# Seed re-picked again at the B06/B17 merge: the keyed draw changed the stream (was 3: p_npc_033 cut to 870, both marchers cut). Weights
# (3, 7) kept; seeds 0..99 scanned for the case (p_npc_033 untouched, p_npc_035 cut, `broke` Event naming him): seed 81 is the first (1000 / 90).
SEED, WEIGHT, DEFENDER_WEIGHT = 81, 3, 7      # the hand-built fold's three knobs
MARCHERS = ("p_npc_033", "p_npc_035")


def _mb():
    """`engine/` names no `modules/` import at module level; the module is loaded on first use."""
    return importlib.import_module("modules.mass_battle.massbattle")


def _fold(arm=None, *, seed=SEED):
    """The hand-built field: the Crown's two marchers (each of weight `WEIGHT`) on the Church's six at `set_s_036`.
    `arm=None` leaves the shipped fixture untouched. Returns `(world, events, bodies after, bodies before)`."""
    w = build_realm(seed)
    _weigh(w, MARCHERS, WEIGHT)
    _weigh(w, world_q.mustered(w, "set_s_036", "fac_church_of_solmund"), DEFENDER_WEIGHT)
    if arm is not None:
        w.fixtures = w.fixtures.sweep("field_units", arm)
    assert world_q.mustered(w, "set_s_014", "fac_valorsmark") == list(MARCHERS), "fixture moved: re-read it"
    before = {pid: w.persons[pid].body for pid in MARCHERS}
    events = _fold_one(w, _march_act(MARCHERS[0], "set_s_036", "off_spymaster"), contest_max_depth=2)
    return w, events, {pid: w.persons[pid].body for pid in MARCHERS}, before


def _broke(events):
    return [(e.kind, o.subject) for e in events for o in e.observed if o.predicate == "broke"]


def test_shipped_arm_is_person():
    assert build_realm(0).fixtures.get("field_units") == "person"


def test_falsifier_two_losers_one_routed_one_not_end_with_different_bodies_under_person_and_identical_under_side():
    """The entry's falsifier. Under `person` the marcher whose subunit broke is cut and the other is not; under `side`
    both take the side's one ratio. If the two were equal under `person` the per-person ratio would not be reaching the
    write."""
    w, events, after, before = _fold("person")
    kinds = [e.kind for e in events]
    assert "field.lost" in kinds, f"precondition: the field is lost by the attacker ({kinds})"
    assert after[MARCHERS[0]] != after[MARCHERS[1]], "person arm: the two losers ended with the same body"
    assert after[MARCHERS[0]] == before[MARCHERS[0]] and after[MARCHERS[1]] < before[MARCHERS[1]], (
        "person arm: the unrouted marcher should be untouched and the routed one cut")

    _w, events_s, after_s, before_s = _fold("side")
    assert "field.lost" in [e.kind for e in events_s]
    assert after_s[MARCHERS[0]] == after_s[MARCHERS[1]], "side arm: the two losers ended with different bodies"
    assert after_s[MARCHERS[0]] < before_s[MARCHERS[0]], "side arm: the loss cut nobody (the control saw no loss)"


def test_planted_failure_the_sides_ratio_fed_to_every_person_reddens_the_falsifier(monkeypatch):
    """MUTATION: every person's ratio is the side's. The falsifier's `person`-arm check (the two bodies differ) must
    then fail -- were it to pass, the test could not observe the failure it excludes."""
    from engine.season.queries.inputs import PartOutcome
    mb = _mb()
    real = mb._person_namer

    def side_share_for_all(members):
        namer = real(members)

        def name(army, scale):
            parts, credit = namer(army, scale)
            side = mb._share(army.hp, army.hp_max, scale)
            return tuple(PartOutcome(part.id, side, part.routed) for part in parts), credit
        return name

    monkeypatch.setattr(mb, "_person_namer", side_share_for_all)
    _w, _events, after, _before = _fold("person")
    assert after[MARCHERS[0]] == after[MARCHERS[1]], "the mutant still wrote two different bodies"
    with pytest.raises(AssertionError):
        assert after[MARCHERS[0]] != after[MARCHERS[1]], "the falsifier's person-arm check"


def test_the_shipped_arm_is_the_person_arm_and_side_is_the_control_that_carries_no_per_person_record():
    """The unswept fold is the `person` fold (the shipped arm), same bodies and hash; `field_units: side` is the control: the
    module's outcome names no part and no breaker, and no Event names one."""
    w_ship, ev_ship, after_ship, _ = _fold(None)
    w_person, ev_person, after_person, _ = _fold("person")
    assert after_ship == after_person
    assert [(e.kind, e.degree) for e in ev_ship] == [(e.kind, e.degree) for e in ev_person]
    assert w_ship.content_hash() == w_person.content_hash()
    _w, ev_side, _after, _ = _fold("side")
    assert _broke(ev_side) == []

    inp = MassBattleInput(weights=((2, 2), (6,)), territory=None, fort_level=0.0, stances=(0.0, 0.0), walls_dr=None,
                          origin=None, loyalties=(0.0, 0.0), loyalty_gain=0, geography={}, condition_scale=SCALE,
                          members=(("a0", "a1"), ("b0",)), units="side")
    record = _mb().resolve_field(inp, draw.seeded(draw.H2("test_cp_t04_01_person_subunits", 0)))
    assert all(side.parts == () and side.broke_first is None for side in (record.attacker, record.defender))


def test_the_band_event_names_the_loser_whose_subunit_broke_first():
    """The cause (D_T04 #61-#62): `field.lost` carries `(pid, "broke", True)` for exactly one loser, the one whose
    subunit broke -- here the marcher who ended cut."""
    _w, events, after, before = _fold("person")
    cut = [pid for pid in MARCHERS if after[pid] < before[pid]]
    named = _broke(events)
    assert cut == [MARCHERS[1]] and named == [("field.lost", MARCHERS[1])], (named, after)


def test_the_engines_order_of_breaking_names_each_unit_once_and_not_a_unit_swept_with_its_army():
    """B17.03: `run_battle` returns `broke`, `(side, unit index)` in the order units broke on their own account while their army
    stood (`_PersonSubunit`'s setter that logged a person is deleted). Three-person sides of weight 3 (90 troops a unit, above
    `UNIT_ROUT_FLOOR`) are fought over seeds 0 to 7: every name is `A` or `B` and a unit of that army, none is named twice, and
    the fields that broke a unit are most of them (the loop asserts that it asserted). CONTROL, the same fight with weight 1 (30
    troops, under the floor): the army routs whole, every unit is swept with it and NOBODY is named, which is what keeps a swept
    unit from being credited with a break it did not make."""
    mb = _mb()
    rngsource = importlib.import_module("modules.mass_battle.rngsource")
    run_battle = importlib.import_module("modules.mass_battle.battle_loop").run_battle     # by string: `engine/` imports no module code

    def fight(weight, seed):
        a = mb._person_unit("side_a", (weight,) * 3, ("a0", "a1", "a2"), "A", 5)
        b = mb._person_unit("side_b", (weight,) * 3, ("b0", "b1", "b2"), "B", 5)
        with rngsource.using(draw.seeded(draw.H2("test_cp_t04_01_person_subunits", seed))):
            return run_battle(a, b, max_ticks=18)["broke"], a, b

    named = 0
    for seed in range(8):
        got, a, b = fight(3, seed)
        assert len(set(got)) == len(got) and all(side in "AB" and 0 <= i < 3 for side, i in got), got
        named += bool(got)
    assert named >= 6, named
    for seed in range(8):
        got, a, b = fight(1, seed)
        assert got == [] and a.routed and b.routed, (seed, got)


def test_the_person_arm_builds_one_subunit_per_member_sized_by_his_own_weight():
    mb = _mb()
    unit = mb._person_unit("side_x", (1, 3, 2), ("p0", "p1", "p2"), "A", 5)
    assert [s.troops for s in unit.units] == [30.0, 90.0, 60.0]     # `under_arms_cap`: 30 troops a weight
    assert unit.total_troops() == 180.0
    side = mb._weighted_unit("side_x", 6, "A", 5)
    assert side.total_troops() == unit.total_troops()    # the side's total is the same either way
    fed = mb._person_unit("side_x", (1, 3), ("p0", "p1"), "A", 5, fed=2.0)
    assert [s.troops for s in fed.units] == [15.0, 45.0]      # provisioned troops spread by weight, then capped


def test_an_unknown_arm_is_refused():
    inp = MassBattleInput(weights=((2,), (2,)), territory=None, fort_level=0.0, stances=(0.0, 0.0), walls_dr=None,
                          origin=None, loyalties=(0.0, 0.0), loyalty_gain=0, geography={}, condition_scale=SCALE, units="squad")
    with pytest.raises(ValueError):
        _mb().resolve_field(inp, draw.seeded(draw.H2("test_cp_t04_01_person_subunits", 0)))


def test_field_input_hands_the_members_beside_the_weights_and_the_fixture():
    from engine.season.seam.wrappers.mass_battle import field_input
    w = build_realm(0)
    w.fixtures = w.fixtures.sweep("field_units", "person")
    claimants = list(MARCHERS) + ["p_not_in_the_world"]
    other = world_q.mustered(w, "set_s_036", "fac_church_of_solmund")
    inp = field_input(w, claimants, other, "set_s_036")
    assert inp.units == "person"
    assert inp.members == (MARCHERS, tuple(other))
    assert tuple(len(m) for m in inp.members) == tuple(len(x) for x in inp.weights)
