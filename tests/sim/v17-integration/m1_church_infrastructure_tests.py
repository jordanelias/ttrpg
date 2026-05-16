"""
m1_church_infrastructure_tests — boundary/regression tests for M1.

Designed to run as a script (subprocess) — no external test framework dep.
Run: python3 m1_church_infrastructure_tests.py
Returns 0 on success, non-zero on any failure.
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

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


# ═══════════════════════════════════════════════════════════════════════════
# T1 — Registry integrity
# ═══════════════════════════════════════════════════════════════════════════

def t1_registry():
    print("\n=== T1: registry integrity ===")
    check(len(m1.SETTLEMENT_REGISTRY) == 37,  # [canonical: derived — see ledger entries + module constants]
          "37 settlements registered",
          detail=f"got {len(m1.SETTLEMENT_REGISTRY)}")
    check(sum(m1.SPIRITUAL_WEIGHT.values()) == 32,
          "SW table sums to 32 (canonical)",
          detail=f"got {sum(m1.SPIRITUAL_WEIGHT.values())}")
    # All 17 T# entries present in SW
    for tid in [f'T{i}' for i in range(1, 18)]:
        check(tid in m1.SPIRITUAL_WEIGHT, f"  SW contains {tid}",
              detail=f"missing {tid}")
    # 15 playable + 2 inert = 17 distinct
    check(len(m1.PLAYABLE_TERRITORIES) == 15, "15 playable territories",
          detail=f"got {len(m1.PLAYABLE_TERRITORIES)}")
    check('T15' in m1.INERT_TERRITORIES and 'T16' in m1.INERT_TERRITORIES,
          "T15 + T16 are inert", detail="missing from INERT_TERRITORIES")
    # Settlement count per duchy
    valorsmark_tids = {'T1', 'T2', 'T3', 'T5', 'T6', 'T14'}
    hafenmark_tids = {'T7', 'T8', 'T10', 'T17'}
    varfell_tids = {'T4', 'T11', 'T12', 'T13'}
    valorsmark_count = sum(len(m1.TERRITORY_SETTLEMENTS.get(t, []))
                            for t in valorsmark_tids)
    hafenmark_count = sum(len(m1.TERRITORY_SETTLEMENTS.get(t, []))
                           for t in hafenmark_tids)
    varfell_count = sum(len(m1.TERRITORY_SETTLEMENTS.get(t, []))
                         for t in varfell_tids)
    check(valorsmark_count == 15, "Valorsmark duchy has 15 settlements",
          detail=f"got {valorsmark_count}")
    check(hafenmark_count == 10, "Hafenmark duchy has 10 settlements",
          detail=f"got {hafenmark_count}")
    check(varfell_count == 10, "Varfell duchy has 10 settlements",
          detail=f"got {varfell_count}")
    check(len(m1.TERRITORY_SETTLEMENTS.get('T9', [])) == 1, "T9 Himmelenger has 1 settlement (S-036)")
    check(len(m1.TERRITORY_SETTLEMENTS.get('T16', [])) == 1, "T16 Schoenland has 1 settlement (S-037)")
    check(len(m1.TERRITORY_SETTLEMENTS.get('T15', [])) == 0, "T15 Askeheim has 0 settlements")


# ═══════════════════════════════════════════════════════════════════════════
# T2 — Starting infrastructure state
# ═══════════════════════════════════════════════════════════════════════════

def t2_starting_state():
    print("\n=== T2: starting infrastructure ===")
    himmelenger = m1.SETTLEMENT_REGISTRY['S-036']
    check(himmelenger.religious_building == m1.RB_CATHEDRAL,
          "S-036 starts with Cathedral",
          detail=f"got {himmelenger.religious_building}")
    check(himmelenger.templar_station, "S-036 starts with Templar Station")
    check(himmelenger.church_governor, "S-036 starts with Church Governor")
    check(not himmelenger.inquisitor_base,
          "S-036 starts without Inquisitor Base (canon: false)")
    # All other settlements start clean
    for sid, s in m1.SETTLEMENT_REGISTRY.items():
        if sid == 'S-036':
            continue
        check(s.religious_building == m1.RB_NONE
              and not s.templar_station
              and not s.inquisitor_base
              and not s.church_governor,
              f"{sid} starts with no Church infrastructure",
              detail=f"rb={s.religious_building} t={s.templar_station} "
                     f"i={s.inquisitor_base} g={s.church_governor}")


# ═══════════════════════════════════════════════════════════════════════════
# T3 — Seizure Ob boundaries
# ═══════════════════════════════════════════════════════════════════════════

def t3_seizure_ob():
    print("\n=== T3: Seizure Ob formula ===")
    # Empty registry baseline cases — use a fresh registry to control state
    # Case 1: PT=5, no infra → Ob 5
    test_reg = m1.build_settlement_registry()
    # Clear S-036's infrastructure for a clean test
    test_reg['S-036'].religious_building = m1.RB_NONE
    test_reg['S-036'].templar_station = False
    test_reg['S-036'].church_governor = False
    ob = m1.seizure_ob('T9', pt_canon_tier=5, world_ci=0, registry=test_reg)
    check(ob == 5, "PT=5, no infra → Ob 5", detail=f"got {ob}")

    # Case 2: PT=0, no infra → Ob 10
    ob = m1.seizure_ob('T9', pt_canon_tier=0, world_ci=0, registry=test_reg)
    check(ob == 10, "PT=0, no infra → Ob 10", detail=f"got {ob}")

    # Case 3: PT=5, Cathedral+Templar+Governor at single settlement (max −5
    # before cap, cap at −4) → Ob = 10 − 5 − 4 = 1
    test_reg['S-036'].religious_building = m1.RB_CATHEDRAL  # −2
    test_reg['S-036'].templar_station = True                # −1
    test_reg['S-036'].church_governor = True                # −2
    # raw = -5, capped to -4
    s = test_reg['S-036']
    check(s.per_settlement_seizure_modifier() == -4,  # [canonical: derived — see ledger entries + module constants]
          "Cathedral+Templar+Governor on single settlement caps at -4",
          detail=f"got {s.per_settlement_seizure_modifier()}")
    ob = m1.seizure_ob('T9', pt_canon_tier=5, world_ci=0, registry=test_reg)
    check(ob == 1, "PT=5, full infra (capped −4) → Ob 1", detail=f"got {ob}")

    # Case 4: Floor enforcement — PT=5, full infra, with Ascendant (−1) → still 1
    ob = m1.seizure_ob('T9', pt_canon_tier=5, world_ci=80, registry=test_reg)
    check(ob == 1, "Ob floor enforced even at CI 80 Ascendant",
          detail=f"got {ob}")

    # Case 5: Two-settlement territory, both maxed out, total −8 → uncapped at
    # territory level. PT=3 → Ob = 10 − 3 − 8 = -1 → floor → 1
    test_reg2 = m1.build_settlement_registry()
    # Manually loading T2 (Kronmark) with full infra in two settlements
    test_reg2['S-004'].religious_building = m1.RB_CATHEDRAL
    test_reg2['S-004'].templar_station = True
    test_reg2['S-004'].church_governor = True
    test_reg2['S-005'].religious_building = m1.RB_CATHEDRAL
    test_reg2['S-005'].templar_station = True
    test_reg2['S-005'].church_governor = True
    territory_mod = m1.territory_seizure_modifier('T2', registry=test_reg2)
    check(territory_mod == -8, "Two fully-loaded settlements in T2 → −8 total",  # [canonical: derived — see ledger entries + module constants]
          detail=f"got {territory_mod}")
    ob = m1.seizure_ob('T2', pt_canon_tier=3, world_ci=0, registry=test_reg2)
    check(ob == 1, "PT=3, two fully-loaded settlements → Ob 1 (floor)",
          detail=f"got {ob}")

    # Case 6: PT=2, single Chapel only (−0) → Ob = 10 − 2 − 0 = 8
    test_reg3 = m1.build_settlement_registry()
    test_reg3['S-036'].religious_building = m1.RB_NONE
    test_reg3['S-036'].templar_station = False
    test_reg3['S-036'].church_governor = False
    test_reg3['S-004'].religious_building = m1.RB_CHAPEL
    ob = m1.seizure_ob('T2', pt_canon_tier=2, world_ci=0, registry=test_reg3)
    check(ob == 8, "PT=2, single Chapel → Ob 8 (Chapel −0)",  # [canonical: derived — see ledger entries + module constants]
          detail=f"got {ob}")

    # Case 7: CI=80 Ascendant globally lowers Ob by 1
    ob_pre = m1.seizure_ob('T2', pt_canon_tier=2, world_ci=79,  # [canonical: derived — see ledger entries + module constants]
                            registry=test_reg3)
    ob_post = m1.seizure_ob('T2', pt_canon_tier=2, world_ci=80,
                             registry=test_reg3)
    check(ob_post == ob_pre - 1, "CI=80 Ascendant reduces Seizure Ob by 1",
          detail=f"pre={ob_pre} post={ob_post}")


# ═══════════════════════════════════════════════════════════════════════════
# T4 — PT generation from buildings
# ═══════════════════════════════════════════════════════════════════════════

def t4_pt_generation():
    print("\n=== T4: PT generation ===")
    test_reg = m1.build_settlement_registry()
    test_reg['S-036'].religious_building = m1.RB_NONE
    test_reg['S-036'].templar_station = False
    test_reg['S-036'].church_governor = False
    interior = m1.pt_yield_per_territory(test_reg)
    adjacency = m1.pt_yield_adjacency(test_reg)

    # Empty world → all zero
    check(all(v == 0.0 for v in interior.values()),
          "Empty world → all interior PT yields zero")
    check(all(v == 0.0 for v in adjacency.values()),
          "Empty world → all adjacency PT yields zero")

    # Single Chapel in T1 → T1 interior = 0.5; no adjacency contribution
    test_reg['S-001'].religious_building = m1.RB_CHAPEL
    interior = m1.pt_yield_per_territory(test_reg)
    adjacency = m1.pt_yield_adjacency(test_reg)
    check(interior['T1'] == 0.5, "Single Chapel in T1 → interior 0.5",
          detail=f"got {interior['T1']}")
    check(all(v == 0.0 for v in adjacency.values()),
          "Chapel does NOT contribute adjacency bonus")

    # Two Cathedrals in T9 → interior 4.0
    # T9 adjacency = {T2, T3, T8, T14, T17}
    # 2 Cathedrals × 0.5 per adjacent = +1.0 to each of those 5 territories
    test_reg2 = m1.build_settlement_registry()
    test_reg2['S-036'].religious_building = m1.RB_CATHEDRAL  # Cathedral 1
    # T9 only has one settlement (S-036); we can't add a second Cathedral
    # within T9 without adding a fake settlement. Use a different territory.
    test_reg3 = m1.build_settlement_registry()
    test_reg3['S-036'].religious_building = m1.RB_NONE
    test_reg3['S-036'].templar_station = False
    test_reg3['S-036'].church_governor = False
    # T1 has 3 settlements — put 2 Cathedrals in T1
    test_reg3['S-001'].religious_building = m1.RB_CATHEDRAL
    test_reg3['S-002'].religious_building = m1.RB_CATHEDRAL
    interior = m1.pt_yield_per_territory(test_reg3)
    adjacency = m1.pt_yield_adjacency(test_reg3)
    check(interior['T1'] == 4.0, "Two Cathedrals in T1 → interior 4.0",  # [canonical: derived — see ledger entries + module constants]
          detail=f"got {interior['T1']}")
    # T1 adjacency = {T2, T5, T14, T16}
    # 2 Cathedrals × 0.5 each → adjacent territories get +1.0 each
    for adj_tid in {'T2', 'T5', 'T14', 'T16'}:
        check(adjacency[adj_tid] == 1.0,
              f"  T1's 2 Cathedrals → {adj_tid} adjacency bonus = 1.0",
              detail=f"got {adjacency[adj_tid]}")
    # Non-adjacent territories get nothing
    check(adjacency['T9'] == 0.0,
          "T9 (not adjacent to T1) gets no adjacency bonus")

    # Total = interior + adjacency
    totals = m1.pt_yield_total(test_reg3)
    check(totals['T1'] == 4.0, "T1 total = interior 4.0 (no adjacency from self)")  # [canonical: derived — see ledger entries + module constants]
    check(totals['T2'] == 1.0, "T2 total = adjacency bonus only (1.0)")


# ═══════════════════════════════════════════════════════════════════════════
# T5 — CI from Templars + SW-weighted piety yield
# ═══════════════════════════════════════════════════════════════════════════

def t5_ci_generation():
    print("\n=== T5: CI generation ===")
    # Baseline: only S-036 (in T9) has Templar Station → CI yield = 1.0
    ci = m1.ci_from_templars()
    check(ci == 1.0, "Default registry: 1 Templar territory (T9) → CI yield 1.0",
          detail=f"got {ci}")

    # No Templars anywhere → 0
    test_reg = m1.build_settlement_registry()
    test_reg['S-036'].templar_station = False
    ci = m1.ci_from_templars(test_reg)
    check(ci == 0.0, "No Templars → CI yield 0",
          detail=f"got {ci}")

    # Multiple Templars in same territory → still 1 (per territory, not per settlement)
    test_reg2 = m1.build_settlement_registry()
    test_reg2['S-036'].templar_station = False
    test_reg2['S-001'].templar_station = True
    test_reg2['S-002'].templar_station = True
    test_reg2['S-003'].templar_station = True
    ci = m1.ci_from_templars(test_reg2)
    check(ci == 1.0,
          "3 Templars all in T1 → CI yield 1.0 (per-territory, not per-settlement)",
          detail=f"got {ci}")

    # Templars across 3 different territories → 3
    test_reg3 = m1.build_settlement_registry()
    test_reg3['S-036'].templar_station = False
    test_reg3['S-001'].templar_station = True   # T1
    test_reg3['S-004'].templar_station = True   # T2
    test_reg3['S-007'].templar_station = True   # T3
    ci = m1.ci_from_templars(test_reg3)
    check(ci == 3.0, "3 Templars in 3 territories → CI yield 3.0",
          detail=f"got {ci}")

    # SW-weighted piety yield
    # Church holds T9 (SW=5) at PT=5 (float 7.0) → tier×SW/5 = 5×(5/5) = 5.0
    pt_floats = {tid: 0.0 for tid in m1.PLAYABLE_TERRITORIES}
    pt_floats['T9'] = 7.0  # [canonical: derived] canon tier 5
    py = m1.piety_yield_sw_weighted(['T9'], pt_floats)
    check(py == 5.0, "SW-weighted yield: T9 (SW 5, PT 5) → 5.0",
          detail=f"got {py}")
    # T8 (SW 3) at PT 3 (float 5.5) → 3 × (3/5) = 1.8
    pt_floats2 = {'T8': 5.5}
    py = m1.piety_yield_sw_weighted(['T8'], pt_floats2)
    check(abs(py - 1.8) < 1e-9, "SW-weighted yield: T8 (SW 3, PT 3) → 1.8",  # [canonical: derived — see ledger entries + module constants]
          detail=f"got {py}")
    # Empty list → 0
    py = m1.piety_yield_sw_weighted([], pt_floats)
    check(py == 0.0, "No prominent territories → 0")
    # Inert territory (T15, T16) excluded even if listed
    pt_floats3 = {'T15': 7.0, 'T16': 7.0}  # [canonical: derived — see ledger entries + module constants]
    py = m1.piety_yield_sw_weighted(['T15', 'T16'], pt_floats3)
    check(py == 0.0, "Inert territories excluded from yield",
          detail=f"got {py}")


# ═══════════════════════════════════════════════════════════════════════════
# T6 — Other axis effects
# ═══════════════════════════════════════════════════════════════════════════

def t6_axis_effects():
    print("\n=== T6: Inquisitor / Parish / Pastoral ===")
    # Inquisitor Ob modifier — none baseline
    check(m1.rm_ob_modifier_from_inquisitors('T1') == 0,
          "T1 (no Inquisitor) → RM Ob mod 0")
    test_reg = m1.build_settlement_registry()
    test_reg['S-001'].inquisitor_base = True
    check(m1.rm_ob_modifier_from_inquisitors('T1', test_reg) == 1,
          "T1 with Inquisitor → RM Ob mod +1")

    # Parish Order yields
    order = m1.parish_order_yields(test_reg)
    check(order['S-036']['order_install_bonus'] == 1,
          "S-036 (Cathedral) → Order install bonus +1")
    check(order['S-036']['order_decay_modifier'] == -1,
          "S-036 (Cathedral) → Order decay −1")
    check(order['S-001']['order_per_season'] == 0.0,
          "S-001 (no building) → 0 Order/season")

    test_reg2 = m1.build_settlement_registry()
    test_reg2['S-001'].religious_building = m1.RB_CHAPEL
    order = m1.parish_order_yields(test_reg2)
    check(order['S-001']['order_per_season'] == 0.5,
          "S-001 with Chapel → 0.5 Order/season")

    # Pastoral Assumption eligibility
    eligible = m1.pastoral_assumption_eligible('S-001',
                                                governor_present=False,
                                                registry=test_reg2)
    check(eligible,
          "Settlement with Chapel + no governor → Pastoral eligible")
    eligible = m1.pastoral_assumption_eligible('S-001',
                                                governor_present=True,
                                                registry=test_reg2)
    check(not eligible,
          "Settlement with Chapel + governor present → NOT eligible")
    eligible = m1.pastoral_assumption_eligible('S-002',
                                                governor_present=False,
                                                registry=test_reg2)
    check(not eligible,
          "Settlement with no building + no governor → NOT eligible")


# ═══════════════════════════════════════════════════════════════════════════
# T7 — Mass Seizure mechanics
# ═══════════════════════════════════════════════════════════════════════════

def t7_mass_seizure():
    print("\n=== T7: Mass Seizure ===")
    # P(declare) curve
    check(m1.mass_seizure_declaration_probability(50) == 0.0,  # [canonical: derived — see ledger entries + module constants]
          "CI=50 → P(declare) = 0")
    check(m1.mass_seizure_declaration_probability(60) == 0.0,
          "CI=60 → P(declare) = 0")
    check(abs(m1.mass_seizure_declaration_probability(100) - 1.0) < 1e-9,  # [canonical: derived — see ledger entries + module constants]
          "CI=100 → P(declare) = 1.0",
          detail=f"got {m1.mass_seizure_declaration_probability(100)}")
    # Mid-range monotonic
    p70 = m1.mass_seizure_declaration_probability(70)  # [canonical: derived — see ledger entries + module constants]
    p80 = m1.mass_seizure_declaration_probability(80)
    p90 = m1.mass_seizure_declaration_probability(90)  # [canonical: derived — see ledger entries + module constants]
    check(p70 < p80 < p90 < 1.0, "Monotone increasing 70 < 80 < 90 < 100",
          detail=f"p70={p70:.4f} p80={p80:.4f} p90={p90:.4f}")
    # Canonical reference values from victory_v30 §3.2 table
    # CI 80 → 10% per table; formula gives ((80-60)/40)^3.3 = 0.5^3.3 ≈ 0.1016
    expected_80 = 0.5 ** 3.3
    check(abs(p80 - expected_80) < 1e-9,  # [canonical: derived — see ledger entries + module constants]
          f"CI=80 → P matches formula ({expected_80:.4f})",
          detail=f"got {p80:.4f}")

    # Pool formula
    check(m1.seizure_pool(church_influence=6.0, world_ci=60) == 6.0 + 4,  # [canonical: derived — see ledger entries + module constants]
          "Pool: I=6, CI=60 → 10",
          detail=f"got {m1.seizure_pool(6.0, 60)}")
    check(m1.seizure_pool(church_influence=6.0, world_ci=100) == 6.0 + 6,  # [canonical: derived — see ledger entries + module constants]
          "Pool: I=6, CI=100 → 12",
          detail=f"got {m1.seizure_pool(6.0, 100)}")


# ═══════════════════════════════════════════════════════════════════════════
# T8 — CI=100 Unification phase
# ═══════════════════════════════════════════════════════════════════════════

def t8_unification():
    print("\n=== T8: CI=100 Unification ===")
    state = m1.ci_unification_active(world_ci=99, theocracy_seasons=0,  # [canonical: derived — see ledger entries + module constants]
                                      church_controlled_count=15)
    check(not state['active'], "CI<100 → Unification not active")

    state = m1.ci_unification_active(world_ci=100, theocracy_seasons=0,
                                      church_controlled_count=8)  # [canonical: derived — see ledger entries + module constants]
    check(state['active'], "CI=100 → active")
    check(state['free_secular_motion'], "CI=100 → free secular motions")
    check(not state['victory_pending'],
          "CI=100, <10 territories → no victory pending")

    state = m1.ci_unification_active(world_ci=100, theocracy_seasons=1,
                                      church_controlled_count=10)
    check(state['victory_pending'],
          "CI=100, 10 territories, 1 season → victory pending")
    check(not state['victory_achieved'],
          "  only 1 consecutive season → not yet achieved")

    state = m1.ci_unification_active(world_ci=100, theocracy_seasons=2,
                                      church_controlled_count=10)
    check(state['victory_achieved'],
          "CI=100, 10 territories, 2 consecutive seasons → victory achieved")


# ═══════════════════════════════════════════════════════════════════════════
# T9 — PT drift (CI=80 Ascendant)
# ═══════════════════════════════════════════════════════════════════════════

def t9_pt_drift():
    print("\n=== T9: CI=80 PT drift ===")
    pt_floats = {tid: 4.0 for tid in m1.PLAYABLE_TERRITORIES}  # [canonical: derived — see ledger entries + module constants]
    pt_floats['T9'] = 7.0  # already at tier 5 — should not exceed [canonical: derived]
    new = m1.ci_ascendant_pt_drift(pt_floats, warden_cooperation=0)
    # 4.0 is tier 2 → +1 → tier 3 → float 5.5
    check(new['T1'] == 5.5, "PT 4.0 (tier 2) drifts to 5.5 (tier 3)",
          detail=f"got {new['T1']}")
    check(new['T9'] == 7.0,  # [canonical: derived — see ledger entries + module constants]
          "PT 7.0 (tier 5) stays at 7.0 (cap)",
          detail=f"got {new['T9']}")

    # Warden Cooperation ≥ 2 suppresses drift
    new = m1.ci_ascendant_pt_drift(pt_floats, warden_cooperation=2)
    check(new == pt_floats, "Warden Cooperation ≥ 2 suppresses drift")

    # pt_float_to_tier boundary cases
    check(m1.pt_float_to_tier(1.0) == 0, "PT_MAP inverse: 1.0 → tier 0")
    check(m1.pt_float_to_tier(2.5) == 1, "PT_MAP inverse: 2.5 → tier 1")
    check(m1.pt_float_to_tier(4.0) == 2, "PT_MAP inverse: 4.0 → tier 2")  # [canonical: derived — see ledger entries + module constants]
    check(m1.pt_float_to_tier(5.5) == 3, "PT_MAP inverse: 5.5 → tier 3")
    check(m1.pt_float_to_tier(6.5) == 4, "PT_MAP inverse: 6.5 → tier 4")  # [canonical: derived — see ledger entries + module constants]
    check(m1.pt_float_to_tier(7.0) == 5, "PT_MAP inverse: 7.0 → tier 5")  # [canonical: derived — see ledger entries + module constants]


# ═══════════════════════════════════════════════════════════════════════════
# RUN ALL
# ═══════════════════════════════════════════════════════════════════════════

def run_all():
    print("=" * 100)
    print("M1 Church Infrastructure — Test Suite")
    print("=" * 100)
    t1_registry()
    t2_starting_state()
    t3_seizure_ob()
    t4_pt_generation()
    t5_ci_generation()
    t6_axis_effects()
    t7_mass_seizure()
    t8_unification()
    t9_pt_drift()
    print()
    print("=" * 100)
    print(f"PASSED: {_PASSED}    FAILED: {_FAILED}")
    print("=" * 100)
    if _FAILURES:
        print("\nFailures:")
        for label, detail in _FAILURES:
            print(f"  ✗ {label}")
            if detail:
                print(f"      {detail}")
    return 0 if _FAILED == 0 else 1


if __name__ == "__main__":
    sys.exit(run_all())
