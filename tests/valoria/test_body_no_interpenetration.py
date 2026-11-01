"""No two bodies interpenetrate, at battle scale, whatever step writes a position.

Jordan, 2026-11-01: "troops have geometry. they cannot overlap." The body is a circle one pitch across
(geometry.CellBody). Two things keep it so: movement (hierarchy.units._separate_bodies, inside
resolve_toi_and_commit: a cell slides along a body it presses on instead of entering it) and an end-of-tick
guarantee over every body of both sides (hierarchy.units.separate_all_bodies), because position is also written by
steps that know nothing of other bodies: the reshape of a Column or Arrowhead that loses its discipline (check_drift),
the closing of ranks behind casualties, contention reverts, and the builder's deployment.

THE CHECK RUNS THE BATTLE, not a fixture of two cells: armies of at least 5,000 troops a side from
systems/mass_battle/sim/stress_scenarios.json (the harness's own scenarios, shipped flags), measured from the
harness's end-of-tick snapshots. Two ways this test could pass without testing anything are closed: it asserts it
CHECKED battles and ticks, and it asserts the armies actually MOVED AND FOUGHT (contact reached, casualties taken,
few idle subunits), because freezing every formation also leaves no overlap (the ED-MB-0059 deadlock). A second test
switches both mechanisms off and requires the same instrument to SEE interpenetration, so the first cannot be
vacuous.

The harness records positions to `round_digits` places, so its overlap floor is 10**-round_digits per body; the
tolerance below is twice that, and the in-engine pass keeps bodies apart to 1e-9.
"""
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))

import pytest  # noqa: E402

from systems.mass_battle.sim import stress  # noqa: E402

SCENARIOS = ('S01_mirror_lines', 'S03_cannae_double_envelopment', 'S06_missile_against_foot', 'S07_season_path_mirror')
SEEDS = (1, 2)
CAP = 40


@pytest.fixture(scope='module')
def params():
    with open(stress.PARAMS, encoding='utf-8') as f:
        return json.load(f)


@pytest.fixture(scope='module')
def loaded(params):
    stress._load({}, None)          # the flags as shipped; the grid as shipped
    return stress.M['cfg'].BATTLEFIELD_SIZE


def _tolerance(params):
    return 2 * 10 ** -params['round_digits']


def _fight(params, field, sid, seed):
    row = stress.fight_one((sid, seed, CAP, params, field))
    assert 'error' not in row, row.get('error')
    return row


def test_no_two_bodies_interpenetrate_and_the_armies_fight(params, loaded):
    tol = _tolerance(params)
    battles = ticks = 0
    for sid in SCENARIOS:
        for seed in SEEDS:
            row = _fight(params, loaded, sid, seed)
            battles += 1
            ticks += row['result']['turns']
            depth = row['max_depth']
            assert max(depth.values()) <= tol, (sid, seed, depth)
            # the armies moved and fought: freezing them would also leave no overlap
            assert row['first_contact_tick'] is not None, (sid, seed, 'never reached contact')
            assert min(row['result']['a_hp_pct'], row['result']['b_hp_pct']) < 100.0, (sid, seed, 'no casualties')
            assert row['idle_subunit_ticks'] <= 0.25 * max(1, row['live_subunit_ticks']), (sid, seed, 'formations froze')
    assert battles == len(SCENARIOS) * len(SEEDS) and ticks >= 4 * battles


def test_the_check_sees_overlap_when_the_mechanisms_are_off(params, loaded, monkeypatch):
    """Mutation control: with movement separation reduced to the bare per-cell caps and the end-of-tick pass removed,
    the same instrument must read interpenetration, or the test above proves nothing."""
    import modules.mass_battle.hierarchy.units as hu
    import modules.mass_battle.orchestration as orch

    def bare_caps(cells_a, cells_b, same_side):
        return {id(e): (e.sr + e.best_t * (e.pr - e.sr), e.sc + e.best_t * (e.pc - e.sc))
                for e in cells_a + cells_b if e.movable and e.cid not in e.atom.halted_cells}

    monkeypatch.setattr(hu, '_separate_bodies', bare_caps)
    monkeypatch.setattr(orch, 'separate_all_bodies', lambda a, b: 0)
    worst = 0.0
    for sid in ('S01_mirror_lines', 'S06_missile_against_foot'):
        worst = max(worst, max(_fight(params, loaded, sid, 1)['max_depth'].values()))
    assert worst > 10 * _tolerance(params), worst

