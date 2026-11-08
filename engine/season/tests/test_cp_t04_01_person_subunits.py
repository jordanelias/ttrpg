"""CP-T04-01 (`H-359`): a side is its persons -- `field_subunits: person` builds one subunit per commanding person and
`_eff_march` scales each loser's body by HIS subunit's survivor ratio; `side`, shipped, is the field as it was.

THE FIELD IS HAND-BUILT, NOT NATURAL. One season of the shipped realm fights almost no field (seed 0: `field.unopposed`
3, `march.declared` 6; seed 1: unopposed 2, declared 3; seed 2: `field.lost` 1), so the falsifier runs on a real fold of
`set_s_014` marching on `set_s_036` with the Crown's two marchers made cohorts (`Person.weight` 2) and the weight ->
troops scale at 100 (REM-32's `field_troops_per_weight`; a value of THIS TEST, not Jordan's answer to JQ-4). At that
scale a weight-1 subunit is 100 troops, at or above `SUBUNIT_ROUT_FLOOR = 80`, and a side is above the 100-troop line,
so a subunit does not rout on tick 1. Realm seed 0 loses the field with ONE marcher's subunit routed and the other's
not (the preconditions are asserted below, so a moved fixture reads as a precondition, not a pass).

The cases: the falsifier (different bodies under `person`, identical under `side`), its planted failure (the side's ratio
fed to every person: the same check reddens), the control (`side` writes today's bodies and carries no per-person
key), the cause (the Event names the loser whose subunit broke first, and `_PersonSubunit` logs it in order), and the
shape of the `person` arm (one subunit per member, sized by his own weight, the provisioned troops spread by weight)."""
from __future__ import annotations

import importlib
import random

import pytest

from engine.season.harness.populated import build_realm
from engine.season.queries import world_q
from engine.season.queries.inputs import MassBattleInput
from engine.season.tests.test_march import _fold_one, _march_act

SEED, WEIGHT, SCALE = 0, 2, 100
MARCHERS = ("p_npc_033", "p_npc_035")


def _mb():
    """`engine/` names no `modules/` import at module level; the module is loaded on first use."""
    return importlib.import_module("modules.mass_battle.massbattle")


def _fold(arm=None, *, seed=SEED):
    """The hand-built field: the Crown's two marchers (cohorts of `WEIGHT`) on the Church's six at `set_s_036`.
    `arm=None` leaves the shipped fixture untouched. Returns `(world, events, bodies after, bodies before)`."""
    w = build_realm(seed)
    for pid in MARCHERS:
        w.persons[pid].weight = WEIGHT
    w.fixtures = w.fixtures.sweep("field_troops_per_weight", SCALE)
    if arm is not None:
        w.fixtures = w.fixtures.sweep("field_subunits", arm)
    assert world_q.mustered(w, "set_s_014", "fac_valorsmark") == list(MARCHERS), "fixture moved: re-read it"
    before = {pid: w.persons[pid].body for pid in MARCHERS}
    events = _fold_one(w, _march_act(MARCHERS[0], "set_s_036", "off_spymaster"), contest_max_depth=2)
    return w, events, {pid: w.persons[pid].body for pid in MARCHERS}, before


def _broke(events):
    return [(e.kind, o.subject) for e in events for o in e.observed if o.predicate == "broke"]


def test_shipped_arm_is_side():
    assert build_realm(0).fixtures.get("field_subunits") == "side"


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
    real = _mb()._person_report

    def side_ratio_for_all(units, members, logs):
        rep = real(units, members, logs)
        for unit, pids in zip(units, members):
            side = unit.hp / max(1.0, unit.hp_max)
            for pid in pids:
                rep['subunits'][pid] = (side, rep['subunits'][pid][1])
        return rep

    monkeypatch.setattr(_mb(), "_person_report", side_ratio_for_all)
    _w, _events, after, _before = _fold("person")
    assert after[MARCHERS[0]] == after[MARCHERS[1]], "the mutant still wrote two different bodies"
    with pytest.raises(AssertionError):
        assert after[MARCHERS[0]] != after[MARCHERS[1]], "the falsifier's person-arm check"


def test_control_side_arm_is_the_shipped_field_and_carries_no_per_person_record():
    """`field_subunits: side` reproduces the shipped bodies exactly (the unswept fold), the same hash, and the module's
    record holds no `subunits` or `broke_first`; no Event names a breaker."""
    w_ship, ev_ship, after_ship, _ = _fold(None)
    w_side, ev_side, after_side, _ = _fold("side")
    assert after_ship == after_side
    assert [(e.kind, e.degree) for e in ev_ship] == [(e.kind, e.degree) for e in ev_side]
    assert w_ship.content_hash() == w_side.content_hash()
    assert _broke(ev_side) == []

    inp = MassBattleInput(weights=((2, 2), (6,)), territory=None, fort_level=0.0, stances=(0.0, 0.0), walls_dr=None,
                          origin=None, loyalties=(0.0, 0.0), loyalty_gain=0, geography={}, troops_per_weight=SCALE,
                          members=(("a0", "a1"), ("b0",)))
    record = _mb().resolve_field(inp, random.Random(0))
    assert set(record) == {"attacker_wins", "degree", "attacker_size_pct", "defender_size_pct"}


def test_the_band_event_names_the_loser_whose_subunit_broke_first():
    """The cause (D_T04 #61-#62): `field.lost` carries `(pid, "broke", True)` for exactly one loser, the one whose
    subunit broke -- here the marcher who ended cut."""
    _w, events, after, before = _fold("person")
    cut = [pid for pid in MARCHERS if after[pid] < before[pid]]
    named = _broke(events)
    assert cut == [MARCHERS[1]] and named == [("field.lost", MARCHERS[1])], (named, after)


def test_a_subunit_logs_its_person_in_the_order_it_breaks_and_not_when_the_whole_unit_is_swept():
    mb = _mb()
    unit, log = mb._person_unit("side_x", (2, 2, 2), ("p0", "p1", "p2"), 5, SCALE)
    unit.subunits[1].routed = True
    unit.subunits[0].routed = True
    unit.subunits[0].routed = True                       # setting it again is not breaking again
    assert log == ["p1", "p0"]
    unit.routed = True                                   # the whole body routs: the sweep after it is nobody's break
    unit.subunits[2].routed = True
    assert log == ["p1", "p0"]
    assert [s.routed for s in unit.subunits] == [True, True, True]


def test_the_person_arm_builds_one_subunit_per_member_sized_by_his_own_weight():
    mb = _mb()
    unit, _log = mb._person_unit("side_x", (1, 3, 2), ("p0", "p1", "p2"), 5, SCALE)
    assert [s.troops for s in unit.subunits] == [100.0, 300.0, 200.0]
    assert [s.person for s in unit.subunits] == ["p0", "p1", "p2"]
    assert unit.total_troops() == 600.0
    side = mb._weighted_unit("side_x", 6, 5, SCALE)
    assert side.total_troops() == unit.total_troops()    # the side's total is the same either way
    fed, _ = mb._person_unit("side_x", (1, 3), ("p0", "p1"), 5, SCALE, fed=2.0)
    assert [s.troops for s in fed.subunits] == [50.0, 150.0]     # provisioned troops spread by weight


def test_an_unknown_arm_is_refused():
    inp = MassBattleInput(weights=((2,), (2,)), territory=None, fort_level=0.0, stances=(0.0, 0.0), walls_dr=None,
                          origin=None, loyalties=(0.0, 0.0), loyalty_gain=0, geography={}, subunits="squad")
    with pytest.raises(ValueError):
        _mb().resolve_field(inp, random.Random(0))


def test_field_input_hands_the_members_beside_the_weights_and_the_fixture():
    from engine.season.seam.wrappers.mass_battle import field_input
    w = build_realm(0)
    w.fixtures = w.fixtures.sweep("field_subunits", "person")
    claimants = list(MARCHERS) + ["p_not_in_the_world"]
    other = world_q.mustered(w, "set_s_036", "fac_church_of_solmund")
    inp = field_input(w, claimants, other, "set_s_036")
    assert inp.subunits == "person"
    assert inp.members == (MARCHERS, tuple(other))
    assert tuple(len(m) for m in inp.members) == tuple(len(x) for x in inp.weights)
