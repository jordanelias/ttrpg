"""
m2_ci_political_revision_tests — boundary tests for M2.
"""  # [canonical: N/A — module docstring (triple-quoted, single-line ok)]
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import m2_ci_political_revision as m2
import m1_church_infrastructure as m1


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


def t1_constants():
    print("\n=== T1: canonical constants ===")
    check(m2.CI_STARTING_VALUE == 28, "CI_STARTING_VALUE matches canon",      # [canonical: see CI_STARTING_VALUE ledger entry]
          detail=f"got {m2.CI_STARTING_VALUE}")
    check(m2.CI_SEASONAL_CAP_MAGNITUDE == 5, "Seasonal cap matches canon",     # [canonical: see CI_SEASONAL_CAP_MAGNITUDE ledger]
          detail=f"got {m2.CI_SEASONAL_CAP_MAGNITUDE}")
    check(m2.CI_DOMAIN_ACTION_SUBCAP == 3, "DA sub-cap matches canon",         # [canonical: see CI_DOMAIN_ACTION_SUBCAP ledger]
          detail=f"got {m2.CI_DOMAIN_ACTION_SUBCAP}")
    check(m2.CI_MILESTONE_ASSERTIVE == 40, "Assertive milestone")              # [canonical: see CI_MILESTONE_ASSERTIVE ledger]
    check(m2.CI_MILESTONE_INSTITUTIONAL == 55, "Institutional Reach milestone")  # [canonical: see CI_MILESTONE_INSTITUTIONAL ledger]
    check(m2.CI_MILESTONE_DOMINANT == 65, "Dominant milestone")                # [canonical: see CI_MILESTONE_DOMINANT ledger]
    check(m2.CI_MILESTONE_ASCENDANT == 80, "Ascendant milestone")              # [canonical: see CI_MILESTONE_ASCENDANT ledger]
    check(m2.CI_MILESTONE_UNIFICATION == 100, "Unification milestone")         # [canonical: see CI_MILESTONE_UNIFICATION ledger]
    check(m2.CI_BONUS_DICE_DIVISOR == 20, "Bonus dice divisor")                # [canonical: see CI_BONUS_DICE_DIVISOR ledger]
    check(m2.CI_OBSTACLE_DIVISOR == 30, "Obstacle divisor")                    # [canonical: see CI_OBSTACLE_DIVISOR ledger]
    check(m2.HAFENMARK_CI_SUPPRESS_THRESHOLD == 4.0, "Hafenmark threshold")    # [canonical: see HAFENMARK_CI_SUPPRESS_THRESHOLD ledger]


def t2_seasonal_cap():
    print("\n=== T2: seasonal ±5 total cap ===")
    # Single +7 from generated → clamped to +5
    r = m2.apply_ci_delta(50, [{'name': 'piety', 'kind': 'generated', 'delta': 7.0}])  # [canonical: derived test boundary — see ledger entries + module constants]
    check(r['applied_total'] == 5.0, "+7 generated → +5 (cap)", detail=f"got {r['applied_total']}")  # [canonical: see CI_SEASONAL_CAP_MAGNITUDE]
    check(r['new_ci'] == 55, "CI 50 → 55 after capped delta", detail=f"got {r['new_ci']}")

    # Multiple gen sources summing to +12 → clamped to +5
    r = m2.apply_ci_delta(28, [
        {'name': 'piety', 'kind': 'generated', 'delta': 5.0},
        {'name': 'templars', 'kind': 'generated', 'delta': 4.0},  # [canonical: derived test boundary — see ledger entries + module constants]
        {'name': 'extra', 'kind': 'generated', 'delta': 3.0},
    ])
    check(r['applied_total'] == 5.0, "+12 generated → +5 (cap)", detail=f"got {r['applied_total']}")  # [canonical: see CI_SEASONAL_CAP_MAGNITUDE]

    # Negative cap: -8 generated → -5
    r = m2.apply_ci_delta(50, [{'name': 'haf', 'kind': 'generated', 'delta': -8.0}])  # [canonical: derived test boundary — see ledger entries + module constants]
    check(r['applied_total'] == -5.0, "-8 generated → -5 (cap)", detail=f"got {r['applied_total']}")  # [canonical: see CI_SEASONAL_CAP_MAGNITUDE]


def t3_da_subcap():
    print("\n=== T3: Domain-Action ±3 sub-cap ===")
    # +4 from DA alone → clamped to +3 by sub-cap
    r = m2.apply_ci_delta(50, [{'name': 'sermon', 'kind': 'domain_action', 'delta': 4.0}])  # [canonical: derived test boundary — see ledger entries + module constants]
    check(r['da_applied'] == 3.0, "+4 DA → +3 (sub-cap)", detail=f"got {r['da_applied']}")           # [canonical: see CI_DOMAIN_ACTION_SUBCAP]
    check(r['applied_total'] == 3.0, "total = +3 (room remains under total cap)", detail=f"got {r['applied_total']}")  # [canonical: see CI_DOMAIN_ACTION_SUBCAP]

    # +5 from DA, +0 from gen → DA clamps to +3
    r = m2.apply_ci_delta(50, [{'name': 'sermon', 'kind': 'domain_action', 'delta': 5.0}])  # [canonical: derived test boundary — see ledger entries + module constants]
    check(r['da_applied'] == 3.0, "+5 DA → +3 (sub-cap clamps before total)", detail=f"got {r['da_applied']}")  # [canonical: see CI_DOMAIN_ACTION_SUBCAP]
    check(r['applied_total'] == 3.0, "total = +3", detail=f"got {r['applied_total']}")

    # Negative DA: -4 → -3
    r = m2.apply_ci_delta(50, [{'name': 'parl_motion', 'kind': 'domain_action', 'delta': -4.0}])  # [canonical: derived test boundary — see ledger entries + module constants]
    check(r['da_applied'] == -3.0, "-4 DA → -3 (sub-cap)", detail=f"got {r['da_applied']}")           # [canonical: see CI_DOMAIN_ACTION_SUBCAP]


def t4_mixed_sources():
    print("\n=== T4: mixed DA + generated, both cap-aware ===")
    # DA +3, gen +4 → DA stays at +3, gen would push total to +7, total clamps to +5
    # → gen reduces to +2
    r = m2.apply_ci_delta(50, [  # [canonical: derived test boundary — see ledger entries + module constants]
        {'name': 'sermon', 'kind': 'domain_action', 'delta': 3.0},
        {'name': 'piety', 'kind': 'generated', 'delta': 4.0},  # [canonical: derived test boundary — see ledger entries + module constants]
    ])
    check(r['da_applied'] == 3.0, "DA share preserved at +3", detail=f"got {r['da_applied']}")           # [canonical: see CI_DOMAIN_ACTION_SUBCAP]
    check(r['applied_total'] == 5.0, "total clamped to +5", detail=f"got {r['applied_total']}")          # [canonical: see CI_SEASONAL_CAP_MAGNITUDE]
    # Generated absorbed the residual
    check(r['gen_applied'] == 2.0, "generated absorbed cap residual (gen=4 → +2)", detail=f"got {r['gen_applied']}")  # [canonical: see CI_SEASONAL_CAP_MAGNITUDE]

    # DA +4 (clamps to +3), gen +1 → total = +4 (no total clamp needed)
    r = m2.apply_ci_delta(50, [  # [canonical: derived test boundary — see ledger entries + module constants]
        {'name': 'sermon', 'kind': 'domain_action', 'delta': 4.0},  # [canonical: derived test boundary — see ledger entries + module constants]
        {'name': 'piety', 'kind': 'generated', 'delta': 1.0},
    ])
    check(r['da_applied'] == 3.0, "DA over-cap → +3", detail=f"got {r['da_applied']}")                   # [canonical: see CI_DOMAIN_ACTION_SUBCAP]
    check(r['gen_applied'] == 1.0, "Generated unaffected → +1", detail=f"got {r['gen_applied']}")
    check(r['applied_total'] == 4.0, "Total = +4 (no total clamp)", detail=f"got {r['applied_total']}")  # [canonical: derived test boundary — see ledger entries + module constants]

    # All zero — sanity
    r = m2.apply_ci_delta(50, [])  # [canonical: derived test boundary — see ledger entries + module constants]
    check(r['applied_total'] == 0.0, "Empty deltas → 0", detail=f"got {r['applied_total']}")
    check(r['new_ci'] == 50, "CI unchanged at 50")  # [canonical: derived test boundary — see ledger entries + module constants]


def t5_hard_bounds():
    print("\n=== T5: hard 0-100 bounds ===")
    # CI 98 + 5 → clamped to 100
    r = m2.apply_ci_delta(98, [{'name': 'piety', 'kind': 'generated', 'delta': 5.0}])  # [canonical: derived test boundary — see ledger entries + module constants]
    check(r['new_ci'] == 100, "CI 98 + 5 → 100 (hard bound)", detail=f"got {r['new_ci']}")               # [canonical: see CI_MAX]
    check(r['applied_total'] == 2.0, "Applied total reflects bound clip", detail=f"got {r['applied_total']}")

    # CI 2 - 5 → clamped to 0
    r = m2.apply_ci_delta(2, [{'name': 'haf', 'kind': 'generated', 'delta': -5.0}])
    check(r['new_ci'] == 0, "CI 2 - 5 → 0 (hard bound)", detail=f"got {r['new_ci']}")                    # [canonical: see CI_MIN]


def t6_bonus_dice_and_obstacle():
    print("\n=== T6: §3.2 Bonus Dice + §3.3 Obstacle Modifier ===")
    # Bonus dice table (CI 28 → +1D, 40 → +2D, 60 → +3D, 80 → +4D, 100 → +5D)
    check(m2.ci_bonus_dice(28) == 1, "CI 28 → +1D bonus")                                                 # [canonical: see CI_BONUS_DICE_DIVISOR]
    check(m2.ci_bonus_dice(40) == 2, "CI 40 → +2D bonus")
    check(m2.ci_bonus_dice(60) == 3, "CI 60 → +3D bonus")  # [canonical: derived test boundary — see ledger entries + module constants]
    check(m2.ci_bonus_dice(80) == 4, "CI 80 → +4D bonus")  # [canonical: derived test boundary — see ledger entries + module constants]
    check(m2.ci_bonus_dice(100) == 5, "CI 100 → +5D bonus")
    check(m2.ci_bonus_dice(0) == 0, "CI 0 → +0D")
    check(m2.ci_bonus_dice(19) == 0, "CI 19 → +0D (below first threshold)")  # [canonical: derived test boundary — see ledger entries + module constants]

    # Obstacle modifier (CI 0-29 → 0, 30-59 → -1, 60-89 → -2, 90+ → -3)
    check(m2.ci_obstacle_modifier(0) == 0, "CI 0 → 0 obstacle")                                           # [canonical: see CI_OBSTACLE_DIVISOR]
    check(m2.ci_obstacle_modifier(29) == 0, "CI 29 → 0 obstacle (below threshold)")                       # [canonical: see CI_OBSTACLE_DIVISOR]
    check(m2.ci_obstacle_modifier(30) == -1, "CI 30 → -1 obstacle")                                       # [canonical: see CI_OBSTACLE_DIVISOR]
    check(m2.ci_obstacle_modifier(59) == -1, "CI 59 → -1 obstacle")                                       # [canonical: see CI_OBSTACLE_DIVISOR]
    check(m2.ci_obstacle_modifier(60) == -2, "CI 60 → -2 obstacle")                                       # [canonical: see CI_OBSTACLE_DIVISOR]
    check(m2.ci_obstacle_modifier(89) == -2, "CI 89 → -2 obstacle")                                       # [canonical: see CI_OBSTACLE_DIVISOR]
    check(m2.ci_obstacle_modifier(90) == -3, "CI 90 → -3 obstacle")                                       # [canonical: see CI_OBSTACLE_DIVISOR]
    check(m2.ci_obstacle_modifier(100) == -3, "CI 100 → -3 obstacle")                                     # [canonical: see CI_OBSTACLE_DIVISOR]


def t7_milestone_effects():
    print("\n=== T7: milestone effect queries ===")
    # Threshold-inclusive boundary tests
    check(m2.church_assertive_bonus_dice(39) == 0, "CI 39 → no Assertive bonus")                          # [canonical: see CI_MILESTONE_ASSERTIVE]
    check(m2.church_assertive_bonus_dice(40) == 1, "CI 40 → +1D Assertive")                               # [canonical: see CI_MILESTONE_ASSERTIVE]
    check(m2.church_assertive_bonus_dice(80) == 1, "CI 80 → still +1D Assertive (single bonus, not cumulative)")  # [canonical: see ASSERTIVE_BONUS_DICE]

    check(m2.anti_church_ob_modifier(54) == 0, "CI 54 → no Institutional Reach")                          # [canonical: see CI_MILESTONE_INSTITUTIONAL]
    check(m2.anti_church_ob_modifier(55) == 1, "CI 55 → +1 Ob to anti-Church actions")                    # [canonical: see CI_MILESTONE_INSTITUTIONAL]

    check(m2.secular_anti_church_slot_cost(64) == 1, "CI 64 → 1-slot anti-Church motion")                 # [canonical: see CI_MILESTONE_DOMINANT]
    check(m2.secular_anti_church_slot_cost(65) == 2, "CI 65 → 2-slot anti-Church motion")                 # [canonical: see CI_MILESTONE_DOMINANT]

    check(not m2.is_ascendant(79), "CI 79 → not Ascendant")  # [canonical: derived test boundary — see ledger entries + module constants]
    check(m2.is_ascendant(80), "CI 80 → Ascendant")

    check(not m2.is_unification_active(99), "CI 99 → not Unification")  # [canonical: derived test boundary — see ledger entries + module constants]
    check(m2.is_unification_active(100), "CI 100 → Unification")

    # Active milestone set composition
    check(m2.active_milestones(28) == set(), "CI 28 → no milestones active")                              # [canonical: see CI_STARTING_VALUE]
    check(m2.active_milestones(40) == {'assertive'}, "CI 40 → {assertive}")                               # [canonical: see CI_MILESTONE_ASSERTIVE]
    check(m2.active_milestones(55) == {'assertive', 'institutional_reach'}, "CI 55 → assertive + IR")     # [canonical: see CI_MILESTONE_INSTITUTIONAL]
    check(m2.active_milestones(65) == {'assertive', 'institutional_reach', 'dominant'}, "CI 65 → +dominant")  # [canonical: see CI_MILESTONE_DOMINANT]
    check(m2.active_milestones(80) == {'assertive', 'institutional_reach', 'dominant', 'ascendant'},
          "CI 80 → +ascendant")                                                                            # [canonical: see CI_MILESTONE_ASCENDANT]
    check(m2.active_milestones(100) == {'assertive', 'institutional_reach', 'dominant', 'ascendant', 'unification'},
          "CI 100 → all five")                                                                              # [canonical: see CI_MILESTONE_UNIFICATION]


def t8_hafenmark_and_unification_targets():
    print("\n=== T8: Hafenmark suppress + Unification targets ===")
    # Hafenmark threshold tests
    check(m2.hafenmark_ci_suppress(3.9) == 0.0, "Haf.L 3.9 → 0 suppress")                                 # [canonical: see HAFENMARK_CI_SUPPRESS_THRESHOLD]
    check(m2.hafenmark_ci_suppress(4.0) == -1.0, "Haf.L 4.0 → -1 suppress")                               # [canonical: see HAFENMARK_CI_SUPPRESS_THRESHOLD]
    check(m2.hafenmark_ci_suppress(5.0) == -1.0, "Haf.L 5.0 → -1 suppress (flat, not scaled)")            # [canonical: see HAFENMARK_CI_SUPPRESS_MAGNITUDE]
    check(m2.hafenmark_ci_suppress(0.0) == 0.0, "Haf.L 0 → 0 suppress")                                    # [canonical: see HAFENMARK_CI_SUPPRESS_THRESHOLD]

    # Unification target list — default M1 registry: only S-036 has Church infrastructure (T9)
    # Church owns T9 → T9 is in target list (re-affirms control)
    # No other territory has Church buildings → no other targets
    owners = {tid: None for tid in m1.PLAYABLE_TERRITORIES}
    owners['T9'] = 'Church'
    targets = m2.mass_seizure_unification_targets(owners, church_mandate=5.0,
                                                   faction_mandates={'Crown': 5.0, 'Hafenmark': 4.0, 'Varfell': 3.0})  # [canonical: derived test boundary — see ledger entries + module constants]
    check(targets == ['T9'], "Default registry: only T9 has Church building → target = [T9]",
          detail=f"got {targets}")                                                                          # [canonical: see registry default infrastructure]

    # Add Chapel to T1 (S-001) → T1 becomes targetable if Church prominent
    test_reg = m1.build_settlement_registry()
    test_reg['S-001'].religious_building = m1.RB_CHAPEL
    # Crown owns T1, Church Mandate 5 vs Crown Mandate 4 → Church Prominent
    targets = m2.mass_seizure_unification_targets(
        territory_owners={**owners, 'T1': 'Crown'},
        church_mandate=5.0,
        faction_mandates={'Crown': 4.0, 'Hafenmark': 4.0, 'Varfell': 3.0},  # [canonical: derived test boundary — see ledger entries + module constants]
        registry=test_reg,
    )
    check('T1' in targets, "Chapel in T1 + Church Prominent → T1 in targets",
          detail=f"got {targets}")                                                                          # [canonical: see ASSUMPTION_FIVE — Prominence + Chapel+ gates targeting]
    check('T9' in targets, "T9 still in targets")

    # Same setup but Crown Mandate 6 vs Church 5 → Church NOT Prominent in T1
    targets = m2.mass_seizure_unification_targets(
        territory_owners={**owners, 'T1': 'Crown'},
        church_mandate=5.0,
        faction_mandates={'Crown': 6.0, 'Hafenmark': 4.0, 'Varfell': 3.0},  # [canonical: derived test boundary — see ledger entries + module constants]
        registry=test_reg,
    )
    check('T1' not in targets, "Chapel in T1 + Church NOT Prominent → T1 excluded",
          detail=f"got {targets}")                                                                          # [canonical: see ASSUMPTION_FIVE — Prominence required]

    # Inert territories never included
    test_reg2 = m1.build_settlement_registry()
    # S-037 is in T16 (inert); even if Church Prominent there, T16 excluded
    test_reg2['S-037'].religious_building = m1.RB_CATHEDRAL
    owners2 = {tid: None for tid in m1.PLAYABLE_TERRITORIES}
    owners2['T9'] = 'Church'
    targets = m2.mass_seizure_unification_targets(owners2, church_mandate=5.0,
                                                   faction_mandates={},
                                                   registry=test_reg2)
    check('T16' not in targets, "Inert T16 excluded even with Cathedral",
          detail=f"got {targets}")                                                                          # [canonical: see m1.PLAYABLE_TERRITORIES]


def t9_accord():
    print("\n=== T9: Accord on Seizure success ===")
    # Accord formula: max(floor(PT/2)+1, 2), clamped to [3, 7]
    # PT 0 (float 1.0): floor(0.5)+1 = 1 → max(1,2) = 2 → clamped to 3 (floor)
    check(m2.accord_on_seizure_success(1.0) == 3.0, "PT 1.0 → Accord 3 (floor)")                          # [canonical: see accord_on_seizure_success ledger]
    # PT 4.0: floor(2)+1 = 3 → clamped to [3,7] = 3
    check(m2.accord_on_seizure_success(4.0) == 3.0, "PT 4.0 → Accord 3")                                  # [canonical: see accord_on_seizure_success ledger]
    # PT 5.5: floor(2.75)+1 = 3
    check(m2.accord_on_seizure_success(5.5) == 3.0, "PT 5.5 → Accord 3")                                  # [canonical: see accord_on_seizure_success ledger]
    # PT 6.5: floor(3.25)+1 = 4
    check(m2.accord_on_seizure_success(6.5) == 4.0, "PT 6.5 → Accord 4")                                  # [canonical: see accord_on_seizure_success ledger]
    # PT 7.0: floor(3.5)+1 = 4
    check(m2.accord_on_seizure_success(7.0) == 4.0, "PT 7.0 → Accord 4")                                  # [canonical: see accord_on_seizure_success ledger]
    # PT 99 (hypothetical max): floor(49.5)+1 = 50 → clamped to 7 (ceiling)
    check(m2.accord_on_seizure_success(99.0) == 7.0, "PT 99 → Accord 7 (ceiling)")                        # [canonical: see accord_on_seizure_success ledger]


def run_all():
    print("=" * 100)                                                                                       # [canonical: N/A — display formatting]
    print("M2 CI Political Revision — Test Suite")
    print("=" * 100)                                                                                       # [canonical: N/A — display formatting]
    t1_constants()
    t2_seasonal_cap()
    t3_da_subcap()
    t4_mixed_sources()
    t5_hard_bounds()
    t6_bonus_dice_and_obstacle()
    t7_milestone_effects()
    t8_hafenmark_and_unification_targets()
    t9_accord()
    print()
    print("=" * 100)                                                                                       # [canonical: N/A — display formatting]
    print(f"PASSED: {_PASSED}    FAILED: {_FAILED}")
    print("=" * 100)                                                                                       # [canonical: N/A — display formatting]
    if _FAILURES:
        print("\nFailures:")
        for label, detail in _FAILURES:
            print(f"  ✗ {label}")
            if detail:
                print(f"      {detail}")
    return 0 if _FAILED == 0 else 1


if __name__ == "__main__":
    sys.exit(run_all())
