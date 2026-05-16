"""m7_integration_tests — tests for M7 resolution hooks + mc_v17 integration."""
import os
import random
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import m1_church_infrastructure as m1
import m3_mass_battle as m3
import m4_unit_state as m4
import m5_settlement_aggregation as m5
import m6_faction_actions as m6
import m7_resolution_hooks as m7h
import mc_v17 as v17  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]


_PASSED = 0
_FAILED = 0
_FAILURES = []


def check(condition, label, detail=""):
    global _PASSED, _FAILED
    if condition:
        _PASSED += 1
        print(f"  ✓  {label}")
    else:
        _FAILED += 1
        _FAILURES.append((label, detail))
        print(f"  ✗  {label}  — {detail}")


def t1_resolution_context():
    print("\n=== T1: ResolutionContext + HookedBattleResult dataclasses ===")
    ctx = m7h.ResolutionContext(
        attacker_faction='Crown', defender_faction='Hafenmark',
        attacker_units={'Levy': 3}, defender_units={'Levy': 3},  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]
        attacker_mil=4.0, defender_mil=3.0,  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]
        attacker_card='standard_advance', defender_card='standard_advance',
    )
    check(ctx.attacker_pool_delta == 0, "Initial pool deltas zero")  # [canonical: see ResolutionContext ledger]
    check(ctx.suppress_route_for_attacker is False, "Initial route-suppress flags False")  # [canonical: see ResolutionContext ledger]
    check(ctx.hooks_fired == [], "Initial hooks_fired empty")
    check(ctx.rng is not None, "RNG auto-initialized if None passed")


def t2_stratagem_hook():
    print("\n=== T2: Stratagem hook (Varfell 2-pass card revision) ===")
    # Varfell as attacker, given Stratagem
    rng = random.Random(42)  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]
    r = m7h.resolve_battle_hooked(
        {'Levy': 3}, {'Levy': 3}, 3.0, 3.0,  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]
        'stratagem', 'standard_advance',
        rng=rng,
        varfell_revised_card='concentrated_strike',
    )
    check('stratagem:attacker' in r.hooks_fired, "Stratagem fires when Varfell is attacker")  # [canonical: see hook_stratagem ledger]
    check(r.base_result.outcome in ('attacker_wins', 'defender_wins', 'partial'), "Battle resolves to a valid outcome")
    # Without revision
    rng = random.Random(42)  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]
    r2 = m7h.resolve_battle_hooked(
        {'Levy': 3}, {'Levy': 3}, 3.0, 3.0,  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]
        'stratagem', 'standard_advance',
        rng=rng,
    )
    check('stratagem:attacker' in r2.hooks_fired, "Stratagem fires even without revision (passive)")


def t3_calculated_retreat_disappear_withdrawal():
    print("\n=== T3: Calculated Retreat + Disappear withdrawal outcomes ===")
    # Calculated Retreat — withdrawal, no penalty, no pursuit-block
    r = m7h.resolve_battle_hooked(
        {'Levy': 5}, {'KnightsTemplar': 5}, 1.0, 5.0,  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]
        'calculated_retreat', 'standard_advance',
        rng=random.Random(1),
    )
    check(r.withdrawal_no_penalty is True, "Calculated Retreat: withdrawal_no_penalty=True")  # [canonical: see hook_calculated_retreat ledger]
    check(r.base_result.outcome == 'withdrawal', "Outcome is 'withdrawal'")  # [canonical: see hook_calculated_retreat ledger]
    check(r.base_result.attacker_losses == {} and r.base_result.defender_losses == {},
          "No losses on withdrawal")  # [canonical: see construct_withdrawal_result ledger]
    check(r.base_result.attacker_stability_delta == 0, "No Stability penalty on withdrawal")  # [canonical: see hook_calculated_retreat ledger]
    check(r.pursuit_blocked is False, "Calculated Retreat does NOT block pursuit")  # [canonical: see hook_calculated_retreat ledger]

    # Disappear — withdrawal + pursuit blocked
    r = m7h.resolve_battle_hooked(
        {'Levy': 1}, {'HeavyInf': 5}, 1.0, 4.0,  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]
        'disappear', 'standard_advance',
        rng=random.Random(1),
    )
    check(r.withdrawal_no_penalty is True, "Disappear: withdrawal_no_penalty=True")  # [canonical: see hook_disappear ledger]
    check(r.pursuit_blocked is True, "Disappear: pursuit_blocked=True")  # [canonical: see hook_disappear ledger]


def t4_ducal_call_pre_resolution_muster():
    print("\n=== T4: Ducal Call pre-resolution Muster ===")
    # Without Ducal Call
    rng = random.Random(42)  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]
    r_no = m7h.resolve_battle_hooked(
        {'Levy': 3}, {'Levy': 3}, 3.0, 3.0,  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]
        'standard_advance', 'standard_advance',
        rng=rng,
    )
    pool_no = r_no.base_result.attacker_pool_total
    # With Ducal Call summoning 2 Levy
    rng = random.Random(42)  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]
    r_yes = m7h.resolve_battle_hooked(
        {'Levy': 3}, {'Levy': 3}, 3.0, 3.0,  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]
        'ducal_call', 'standard_advance',
        rng=rng,
        ducal_call_unit_count=2,
    )
    pool_yes = r_yes.base_result.attacker_pool_total
    check(pool_yes > pool_no, "Ducal Call boosts attacker pool by +Levy_count Martial",  # [canonical: see hook_ducal_call ledger]
          detail=f"no_ducal={pool_no}, with_ducal={pool_yes}")
    check('ducal_call:attacker:+2_Levy' in r_yes.hooks_fired, "Ducal Call hook logged with count + class")  # [canonical: see hook_ducal_call ledger]


def t5_crusade_fervour_route_suppression():
    print("\n=== T5: Crusade Fervour route suppression ===")
    # Run with Crusade Fervour as attacker, force losses, verify route_triggers does NOT include attacker
    # (we run a battle where attacker loses some units but Discipline check is suppressed)
    rng = random.Random(7)  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]
    r = m7h.resolve_battle_hooked(
        {'Levy': 3, 'LightInf': 2}, {'HeavyInf': 4}, 3.0, 4.0,  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]
        'crusade_fervour', 'standard_advance',
        rng=rng,
    )
    check('crusade_fervour:attacker' in r.hooks_fired, "Crusade Fervour hook fires when attacker plays it")  # [canonical: see hook_crusade_fervour ledger]
    attacker_routes = [rt for rt in r.base_result.route_triggers if rt.startswith('attacker:')]
    check(len(attacker_routes) == 0, "Crusade Fervour suppresses attacker route checks",  # [canonical: see hook_crusade_fervour ledger]
          detail=f"got routes={attacker_routes}")


def t6_inquisitors_mark_opponent_pool_penalty():
    print("\n=== T6: Inquisitor's Mark -2D opponent pool ===")
    rng = random.Random(42)  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]
    # No Inquisitor Mark — both sides standard
    r_no = m7h.resolve_battle_hooked(
        {'HeavyInf': 5}, {'HeavyInf': 5}, 4.0, 4.0,  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]
        'standard_advance', 'standard_advance',
        rng=rng,
    )
    rng = random.Random(42)  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]
    # With Inquisitor Mark as attacker → defender pool -2
    r_yes = m7h.resolve_battle_hooked(
        {'HeavyInf': 5}, {'HeavyInf': 5}, 4.0, 4.0,  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]
        'inquisitors_mark', 'standard_advance',
        rng=rng,
    )
    check(r_yes.base_result.defender_pool_total == r_no.base_result.defender_pool_total - 2,
          f"Inquisitor Mark reduces defender pool by 2",  # [canonical: see hook_inquisitors_mark ledger]
          detail=f"no_mark def={r_no.base_result.defender_pool_total}, with_mark def={r_yes.base_result.defender_pool_total}")
    check('inquisitors_mark:attacker' in r_yes.hooks_fired, "Inquisitor Mark hook logged")


def t7_mc_v17_world_construction():
    print("\n=== T7: mc_v17 World construction ===")
    world = v17.World()  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]
    check(len(world.factions) == 4, "4 parliamentary factions")  # [canonical: see STARTING_STATS ledger]
    check('Crown' in world.factions and 'Church' in world.factions, "Crown + Church present")
    check(len(world.territories) == 16, "16 territories (15 playable + T15)",  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]
          detail=f"got {len(world.territories)}")
    check(len(world.settlements) == 37, "37 settlements seeded from M1",  # [canonical: see SETTLEMENT_REGISTRY ledger]
          detail=f"got {len(world.settlements)}")
    check(len(world.governance) == 37, "37 SettlementGovernance entries (one per settlement)")  # [canonical: see SettlementGovernance ledger]
    check(world.clocks['CI'] == 28.0, "CI starts at 28 (M2 CI_STARTING_VALUE)",  # [canonical: see CI_STARTING_VALUE in m2]
          detail=f"got {world.clocks['CI']}")
    # Faction has UnitRoster + tactic_hand
    crown = world.factions['Crown']
    check(isinstance(crown.units, m4.UnitRoster), "Crown.units is M4 UnitRoster")  # [canonical: see Faction ledger]
    check(len(crown.tactic_hand) == 6, "Crown has 6-card tactic hand (4 shared + 2 specific)",  # [canonical: see FACTION_TACTIC_HANDS ledger]
          detail=f"got {len(crown.tactic_hand)}")
    check('royal_guard' in crown.tactic_hand and 'ducal_call' in crown.tactic_hand,
          "Crown hand includes Crown-specific cards")
    check('crusade_fervour' not in crown.tactic_hand, "Crown hand excludes Church-specific cards")


def t8_action_registry_dispatch():
    print("\n=== T8: ACTION_REGISTRY dispatch ===")
    expected_actions = {'Govern', 'Muster', 'MilitaryConquest',
                        'CrownInitiative_royal_progress', 'CrownInitiative_great_work',
                        'CrownInitiative_coronation_renewal',
                        'Excommunication', 'Absolution'}
    registered = set(v17.ACTION_REGISTRY.keys())  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]
    missing = expected_actions - registered
    check(not missing, f"All {len(expected_actions)} actions registered",
          detail=f"missing: {missing}")
    check(callable(v17.ACTION_REGISTRY['MilitaryConquest']), "Actions are callable")  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]
    check(callable(v17.ACTION_REGISTRY['CrownInitiative_royal_progress']), "Crown Initiative modes wired")  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]


def t9_settlement_event_integration():
    print("\n=== T9: Settlement event loop integration ===")
    # Force a Famine event by setting one settlement's prosperity to 0
    world = v17.World()  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]
    world.governance['S-001'].prosperity = 0
    initial_order = world.governance['S-001'].order
    logger = v17.NullLogger()  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]
    v17.settlement_event_pass(world, logger)  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]
    # Famine should apply order_delta = -1
    final_order = world.governance['S-001'].order
    check(final_order == initial_order - 1, "Famine event applied Order -1",  # [canonical: see FAMINE_ORDER_PENALTY ledger]
          detail=f"initial={initial_order}, final={final_order}")


def t10_smoke_run_completes():
    print("\n=== T10: Smoke run — 5 campaigns complete without exception ===")
    completed = 0
    winners = []
    for seed in range(5):
        try:
            r = v17.run_campaign(seed=seed)  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]
            if r['winner'] is not None:
                completed += 1
                winners.append(r['winner'])
        except Exception as e:
            print(f"     campaign seed {seed} failed: {type(e).__name__}: {e}")
    check(completed == 5, "All 5 campaigns completed with declared winner",  # [canonical: derived test boundary]
          detail=f"got {completed}/5, winners={winners}")


def t11_batch_telemetry():
    print("\n=== T11: Batch telemetry — 10 campaigns ===")
    r = v17.run_batch(10)  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]
    check(r['n'] == 10, "Batch n = 10")
    check(sum(r['win_share'].values()) <= 100.1 and sum(r['win_share'].values()) >= 99.9,  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]
          f"Win share sums to ~100% across 4 factions",  # [canonical: derived test boundary]
          detail=f"sum={sum(r['win_share'].values())}, shares={r['win_share']}")
    check(r['battles_mean'] >= 0, f"battles_mean tracked",  # [canonical: derived test boundary]
          detail=f"got {r['battles_mean']}")


def run_all():
    print("=" * 100)  # [canonical: N/A — display formatting]
    print("M7 Integration + Hooks — Test Suite")
    print("=" * 100)  # [canonical: N/A — display formatting]
    t1_resolution_context()
    t2_stratagem_hook()
    t3_calculated_retreat_disappear_withdrawal()
    t4_ducal_call_pre_resolution_muster()
    t5_crusade_fervour_route_suppression()
    t6_inquisitors_mark_opponent_pool_penalty()
    t7_mc_v17_world_construction()
    t8_action_registry_dispatch()
    t9_settlement_event_integration()
    t10_smoke_run_completes()
    t11_batch_telemetry()
    print()
    print("=" * 100)  # [canonical: N/A — display formatting]
    print(f"PASSED: {_PASSED}    FAILED: {_FAILED}")
    print("=" * 100)  # [canonical: N/A — display formatting]
    if _FAILURES:
        print("\nFailures:")
        for label, detail in _FAILURES:
            print(f"  ✗ {label}")
            if detail:
                print(f"      {detail}")
    return 0 if _FAILED == 0 else 1


if __name__ == "__main__":
    sys.exit(run_all())
