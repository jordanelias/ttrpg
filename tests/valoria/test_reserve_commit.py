"""Reserve formation Phase-3-commit rule (PP-MB-04 / PP-499 / mass_battle_v30.md §A.6) — ED-MB-0023.

A unit held in Reserve "cannot engage" its first turn; it COMMITS at Phase 3 of the NEXT battle-turn
(RESERVE_COMMIT_TURN=2) and may engage from Phase 5 of that same turn (declare Reserve turn N -> commit
Phase 3 turn N+1 -> engage Phase 5 turn N+1; NOT delayed to N+2). Modeled at battle-turn granularity in
run_multi_unit_battle: a reserve pair is benched turn 1 and re-activates at the commit turn.

GATED behind PC_RESERVE_COMMIT (default OFF): the `reserve` instruction stays inert and every pair is
active from turn 1 (byte-exact; run_multi_unit_battle is not in the bat.py golden battery anyway)."""
import importlib
import os
import random
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'sim'))

import pytest  # noqa: E402


def _reload(on):
    os.environ['PC_RESERVE_COMMIT'] = '1' if on else '0'
    import mass_battle.config as C
    importlib.reload(C)
    import mass_battle.resolution as R
    importlib.reload(R)
    import mass_battle.hierarchy.units as U
    importlib.reload(U)
    import mass_battle.engine as E
    importlib.reload(E)
    import mass_battle.orchestration as O
    importlib.reload(O)
    return C, E, O


def _pair(on, a_instructions=(), b_instructions=()):
    """Build a single-pair multi-unit battle: A vs B. Returns (config, log)."""
    C, E, O = _reload(on)
    random.seed(77)
    ua = E.build_unit('Line', 3, 'A0', 'A', 20, instructions=a_instructions)
    ub = E.build_unit('Line', 3, 'B0', 'B', 20, instructions=b_instructions)
    anchor_map = {('Line', 3): 20}
    res = O.run_multi_unit_battle([ua], [ub], [(0, 0)], {0: 'Line'}, {0: 'Line'},
                                  anchor_map, max_battle_turns=6)
    return C, O, res


def test_unit_in_reserve_predicate():
    _, _, O = _reload(on=True), None, None  # noqa: F841
    import mass_battle.orchestration as O2
    import mass_battle.engine as E2
    reserve = E2.build_unit('Line', 3, 'R', 'A', 20, instructions=('reserve',))
    normal = E2.build_unit('Line', 3, 'N', 'A', 20, instructions=('hold',))
    assert O2.unit_in_reserve(reserve) is True
    assert O2.unit_in_reserve(normal) is False


def test_gate_on_reserve_benched_then_commits_turn_two():
    """ON: a reserve unit's pair does not engage turn 1; it commits (re-activates) at turn 2."""
    C, O, res = _pair(on=True, b_instructions=('reserve',))
    log = res['log']
    turn1 = log[0]
    # No engagement for the (only) pair on turn 1 — the reserve unit is benched.
    assert turn1['turn'] == 1
    assert not turn1['engagements'], "turn 1 must have no engagement (reserve benched)"
    assert 'reserve_commits' not in turn1, "reserve commits at turn 2, not turn 1"
    # Turn 2 records the commitment and engages.
    turn2 = log[1]
    assert turn2.get('reserve_commits'), "reserve must commit at turn 2 (RESERVE_COMMIT_TURN)"
    assert turn2['reserve_commits'][0]['pair'] == 0
    assert turn2['engagements'], "committed reserve engages from Phase 5 of its commit turn"


def test_gate_off_reserve_is_inert():
    """OFF (default): the reserve instruction is inert — the pair engages from turn 1, no reserve_commits."""
    C, O, res = _pair(on=False, b_instructions=('reserve',))
    turn1 = res['log'][0]
    assert turn1['engagements'], "OFF: reserve instruction must be inert -> pair engages turn 1"
    assert 'reserve_commits' not in turn1


def test_no_reserve_units_unaffected():
    """A battle with no reserve units behaves identically whether the gate is on or off (engages turn 1)."""
    _, _, res_on = _pair(on=True)
    _, _, res_off = _pair(on=False)
    assert res_on['log'][0]['engagements'], "no-reserve battle still engages turn 1 (gate ON)"
    assert res_off['log'][0]['engagements'], "no-reserve battle still engages turn 1 (gate OFF)"
    assert 'reserve_commits' not in res_on['log'][0]


def teardown_module(module):
    os.environ.pop('PC_RESERVE_COMMIT', None)
    _reload(on=False)
