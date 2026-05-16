"""m6_faction_actions_tests — boundary tests for M6."""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import m6_faction_actions as m6


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


def check_raises(callable_, exc_type, label):
    global _PASSED, _FAILED
    try:
        callable_()
        _FAILED += 1
        _FAILURES.append((label, "did not raise"))
        print(f"  ✗  {label}  — did not raise")
    except exc_type:
        _PASSED += 1
        print(f"  ✓  {label}")
    except Exception as e:
        _FAILED += 1
        _FAILURES.append((label, f"wrong: {type(e).__name__}"))
        print(f"  ✗  {label}  — wrong: {type(e).__name__}")


def t1_royal_progress():
    print("\n=== T1: Crown Initiative — Royal Progress (§3.2) ===")
    # Ob = floor(sum_accord / 2)
    check(m6.royal_progress_ob(0) == 0, "Ob at sum_accord=0 → 0")  # [canonical: see royal_progress_ob ledger]
    check(m6.royal_progress_ob(7) == 3, "Ob at sum_accord=7 → 3 (floor)")  # [canonical: see royal_progress_ob ledger]
    check(m6.royal_progress_ob(10) == 5, "Ob at sum_accord=10 → 5")  # [canonical: see royal_progress_ob ledger]
    check(m6.royal_progress_ob(14) == 7, "Ob at sum_accord=14 → 7")

    # Pool = Influence + standing modifier
    check(m6.royal_progress_pool(4, 0) == 4, "Pool inf=4 standing=0 → 4")  # [canonical: see royal_progress_pool ledger]
    check(m6.royal_progress_pool(4, 2) == 6, "Pool inf=4 standing=+2 → 6")

    # Outcomes
    ow = m6.royal_progress_outcome('Overwhelming')
    check(ow['mandate_delta'] == 2, "OW: Mandate +2")  # [canonical: see royal_progress_outcome ledger]
    check(ow['standing_delta'] == 1, "OW: Standing +1")  # [canonical: see royal_progress_outcome ledger]
    check(ow['accord_1_to_2_all_own'] is True, "OW: Accord 1→2 marker set")  # [canonical: see royal_progress_outcome ledger]
    check(ow['wealth_cost'] == -2, "OW: wealth cost -2")  # [canonical: see royal_progress_outcome ledger]

    succ = m6.royal_progress_outcome('Success')
    check(succ['mandate_delta'] == 1, "Success: Mandate +1")  # [canonical: see royal_progress_outcome ledger]
    check(succ['lowest_accord_territory_plus_1'] is True, "Success: lowest-Accord marker set")  # [canonical: see royal_progress_outcome ledger]

    part = m6.royal_progress_outcome('Partial')
    check(part['standing_delta'] == 1 and part['wealth_cost'] == -2, "Partial: +1 Standing, cost paid")  # [canonical: see royal_progress_outcome ledger]
    check('mandate_delta' not in part, "Partial: no Mandate change")

    fail = m6.royal_progress_outcome('Failure')
    check(fail['standing_delta'] == -1 and fail['wealth_cost'] == -2, "Failure: -1 Standing, cost paid")  # [canonical: see royal_progress_outcome ledger]

    check_raises(lambda: m6.royal_progress_outcome('not_a_degree'), ValueError,
                 "Unknown degree raises ValueError")


def t2_great_work():
    print("\n=== T2: Crown Initiative — Great Work (§3.3) ===")
    check(m6.GREAT_WORK_SEASONS == 3, "Great Work 3-season duration")  # [canonical: see GREAT_WORK_SEASONS ledger]
    check(m6.GREAT_WORK_FINAL_OB == 4, "Great Work final Ob 4")  # [canonical: see GREAT_WORK_FINAL_OB ledger]
    check(m6.GREAT_WORK_WEALTH_COST_PER_SEASON == -1, "W -1 per season")  # [canonical: see GREAT_WORK_WEALTH_COST_PER_SEASON ledger]

    check(m6.great_work_pool_final_season(5) == 5, "Final-season pool = Mandate")  # [canonical: see great_work_pool_final_season ledger]

    ow = m6.great_work_outcome('Overwhelming')
    check(ow['mandate_delta'] == 2 and ow['mandate_permanent'] is True, "OW: +2 Mandate permanent")  # [canonical: see great_work_outcome ledger]
    check(ow['charters_govern_ob_minus_1_permanent'] is True, "OW: Charters Govern -1 Ob permanent")  # [canonical: see great_work_outcome ledger]
    check(ow['standing_delta'] == 2, "OW: Standing +2")

    succ = m6.great_work_outcome('Success')
    check(succ['mandate_delta'] == 2 and succ['mandate_permanent'] is True, "Success: +2 Mandate permanent")  # [canonical: see great_work_outcome ledger]

    part = m6.great_work_outcome('Partial')
    check(part['mandate_delta'] == 1 and part.get('sunk_wealth_partial_loss') is True,
          "Partial: +1 Mandate, sunk-W marker")  # [canonical: see great_work_outcome ledger]

    fail = m6.great_work_outcome('Failure')
    check(fail['standing_delta'] == -2 and fail['cohesion_delta'] == -20,  # [canonical: derived test boundary — see ledger entries + module constants]
          "Failure: -2 Standing, -20 Cohesion (PP-515 breach)")  # [canonical: see great_work_outcome ledger]

    breach = m6.great_work_mid_pledge_breach()
    check(breach['standing_delta'] == -2 and breach['cohesion_delta'] == -20 and breach['reputation_delta'] == -15,  # [canonical: derived test boundary — see ledger entries + module constants]
          "Mid-pledge breach: -2 Standing, -20 Cohesion, -15 Reputation")  # [canonical: see great_work_mid_pledge_breach ledger]


def t3_coronation_renewal():
    print("\n=== T3: Crown Initiative — Coronation Renewal (§3.4) ===")
    # Prerequisite checks
    ok, _ = m6.coronation_renewal_prerequisite_check('peace', False)
    check(ok, "Prereq peace + no excomm → OK")  # [canonical: see coronation_renewal_prerequisite_check ledger]
    ok, _ = m6.coronation_renewal_prerequisite_check('truce', False)
    check(ok, "Prereq truce → OK")
    ok, _ = m6.coronation_renewal_prerequisite_check('alliance', False)
    check(ok, "Prereq alliance → OK")
    ok, _ = m6.coronation_renewal_prerequisite_check('crown_treaty', False)
    check(ok, "Prereq crown_treaty → OK")
    ok, _ = m6.coronation_renewal_prerequisite_check('war', False)
    check(not ok, "Prereq war → BLOCKED")
    ok, _ = m6.coronation_renewal_prerequisite_check('peace', True)
    check(not ok, "Active Excommunication this season → BLOCKED")  # [canonical: see coronation_renewal_prerequisite_check ledger]

    # Ob = floor(Church Mandate / 2) + 1
    check(m6.coronation_renewal_ob(4) == 3, "Ob at Church L=4 → 3")  # [canonical: see coronation_renewal_ob ledger]
    check(m6.coronation_renewal_ob(6) == 4, "Ob at Church L=6 → 4")
    check(m6.coronation_renewal_ob(7) == 4, "Ob at Church L=7 → 4 (floor)")  # [canonical: derived test boundary — see ledger entries + module constants]
    check(m6.coronation_renewal_ob(8) == 5, "Ob at Church L=8 → 5")  # [canonical: derived test boundary — see ledger entries + module constants]

    check(m6.coronation_renewal_pool(5) == 5, "Pool = Influence")  # [canonical: see coronation_renewal_pool ledger]

    # OW lifts Excommunication
    ow = m6.coronation_renewal_outcome('Overwhelming', crown_currently_excommunicated=True)
    check(ow['mandate_delta'] == 2 and ow['lifts_excommunication'] is True,
          "OW excommunicated: +2 Mandate, Excomm lifted")  # [canonical: see coronation_renewal_outcome ledger]
    check(ow['crown_church_standing_delta'] == 1, "OW: Crown-Church Standing +1")  # [canonical: see coronation_renewal_outcome ledger]

    ow_no_excomm = m6.coronation_renewal_outcome('Overwhelming', crown_currently_excommunicated=False)
    check(ow_no_excomm['lifts_excommunication'] is False, "OW not-excommunicated: lifts=False (no-op)")

    # Success also lifts Excomm
    succ = m6.coronation_renewal_outcome('Success', crown_currently_excommunicated=True)
    check(succ['mandate_delta'] == 1 and succ['lifts_excommunication'] is True,
          "Success excommunicated: +1 Mandate, Excomm lifted")  # [canonical: see coronation_renewal_outcome ledger]

    # Partial / Failure no Excomm lift
    part = m6.coronation_renewal_outcome('Partial', crown_currently_excommunicated=True)
    check('lifts_excommunication' not in part or not part.get('lifts_excommunication'),
          "Partial: no Excomm lift")


def t4_excommunication():
    print("\n=== T4: Church Excommunication (faction_canon §9) ===")
    # Prerequisite L >= 3
    ok, _ = m6.excommunication_prerequisite_check(3)
    check(ok, "Church L=3 → prereq OK")  # [canonical: see excommunication_prerequisite_check ledger]
    ok, _ = m6.excommunication_prerequisite_check(2)
    check(not ok, "Church L=2 → prereq FAIL")  # [canonical: see excommunication_prerequisite_check ledger]

    # Ob = target L (leader) / Ob 2 (non-leader)
    check(m6.excommunication_ob(5, is_leader=True) == 5, "Leader target L=5 → Ob 5")  # [canonical: see excommunication_ob ledger]
    check(m6.excommunication_ob(3, is_leader=False) == 2, "Non-leader → Ob 2 (flat)")  # [canonical: see excommunication_ob ledger]
    check(m6.excommunication_ob(10, is_leader=False) == 2, "Non-leader target L irrelevant → Ob 2")

    # Pool = Church L
    check(m6.excommunication_pool(4) == 4, "Pool = Church L")  # [canonical: see excommunication_pool ledger]

    # Outcomes
    ow = m6.excommunication_outcome('Overwhelming')
    check(ow['target_mandate_delta'] == -1, "OW: target Mandate -1")  # [canonical: see excommunication_outcome ledger]
    check(ow['strips_circles_bonus'] is True, "OW: strips Circles bonus")  # [canonical: see excommunication_outcome ledger]
    check(ow['barred_from_public_office'] is True, "OW: barred from public office")
    check(ow['target_personal_reputation_delta'] == -1, "OW: target Reputation -1")

    succ = m6.excommunication_outcome('Success')
    check(succ['target_mandate_delta'] == -1 and succ['strips_circles_bonus'],
          "Success: same as OW minus Reputation penalty")  # [canonical: see excommunication_outcome ledger]
    check('target_personal_reputation_delta' not in succ, "Success: no Reputation penalty")

    fail = m6.excommunication_outcome('Failure')
    check(fail['church_mandate_delta'] == -1 and fail['target_mandate_delta'] == 1,
          "Failure: Church L -1, target gains L +1 (sympathy martyr)")  # [canonical: see excommunication_outcome ledger]


def t5_absolution():
    print("\n=== T5: Church Absolution (faction_canon §8.2 + M6_ASSUMPTION_ONE) ===")
    check(m6.ABSOLUTION_OB == 3, "M6_ASSUMPTION_ONE: Ob 3")  # [canonical: see ABSOLUTION_OB ledger]
    check(m6.ABSOLUTION_CHURCH_MANDATE_COST == -1, "M6_ASSUMPTION_ONE: Church Mandate cost -1")  # [canonical: see ABSOLUTION_CHURCH_MANDATE_COST ledger]
    check(m6.ABSOLUTION_TARGET_STABILITY_BONUS == 1, "Canon: +1 Stability to target")  # [canonical: see ABSOLUTION_TARGET_STABILITY_BONUS ledger]

    check(m6.absolution_pool(5) == 5, "Pool = Church Influence")  # [canonical: see absolution_pool ledger]

    ow = m6.absolution_outcome('Overwhelming')
    check(ow['target_stability_delta'] == 2, "OW: +2 Stability to target")  # [canonical: see absolution_outcome ledger]
    check(ow['church_mandate_delta'] == -1, "OW: Church Mandate cost -1 paid")  # [canonical: see absolution_outcome ledger]

    succ = m6.absolution_outcome('Success')
    check(succ['target_stability_delta'] == 1, "Success: +1 Stability (canonical)")  # [canonical: see absolution_outcome ledger]

    part = m6.absolution_outcome('Partial')
    check('target_stability_delta' not in part and part['church_mandate_delta'] == -1,
          "Partial: cost paid, no effect on target")

    fail = m6.absolution_outcome('Failure')
    check(fail['church_mandate_delta'] == -1 and fail['church_standing_delta'] == -1,
          "Failure: cost paid + Standing -1")  # [canonical: see absolution_outcome ledger]


def t6_faction_analogues():
    print("\n=== T6: Faction analogues to Crown Initiative (part10 §5) ===")

    # Church Council of Solmund
    check(m6.council_of_solmund_ob(0) == 2, "Council Ob at CI=0 → 2 (floor(0/30)+2)")  # [canonical: see council_of_solmund_ob ledger]
    check(m6.council_of_solmund_ob(60) == 4, "Council Ob at CI=60 → 4 (floor(2)+2)")  # [canonical: see council_of_solmund_ob ledger]
    check(m6.council_of_solmund_ob(90) == 5, "Council Ob at CI=90 → 5")
    check(m6.council_of_solmund_pool(6) == 6, "Council Pool = Mandate")  # [canonical: see council_of_solmund_pool ledger]

    council_ow = m6.council_of_solmund_outcome('Overwhelming')
    check(council_ow['church_mandate_delta'] == 2, "Council OW: +2 Mandate")  # [canonical: see council_of_solmund_outcome ledger]
    check(council_ow['cardinal_focus_permanent'] is True, "Council OW: Cardinal Focus permanent")  # [canonical: see council_of_solmund_outcome ledger]
    check(council_ow['rival_l_delta'] == -1, "Council OW: rival L -1 (formal censure)")  # [canonical: see council_of_solmund_outcome ledger]

    council_succ = m6.council_of_solmund_outcome('Success')
    check(council_succ['church_mandate_delta'] == 1, "Council Success: +1 Mandate")  # [canonical: see council_of_solmund_outcome ledger]

    # Hafenmark Charter of Liberties
    check(m6.CHARTER_DIPLOMATIC_TOKEN_COST == 1, "Charter: 1 Diplomatic Token consumed")  # [canonical: see CHARTER_DIPLOMATIC_TOKEN_COST ledger]
    check(m6.CHARTER_WEALTH_COST == -1, "Charter: W -1")
    check(m6.CHARTER_OB == 4, "Charter Ob 4")  # [canonical: see CHARTER_OB ledger]

    check(m6.charter_of_liberties_pool(4, 0) == 4, "Charter Pool inf=4 tokens=0 → 4")  # [canonical: see charter_of_liberties_pool ledger]
    check(m6.charter_of_liberties_pool(4, 3) == 7, "Charter Pool inf=4 tokens=3 → 7")  # [canonical: see charter_of_liberties_pool ledger]

    charter_ow = m6.charter_of_liberties_outcome('Overwhelming')
    check(charter_ow['hafenmark_mandate_delta'] == 2 and charter_ow['pi_delta'] == -2,
          "Charter OW: +2 Mandate, PI -2")  # [canonical: see charter_of_liberties_outcome ledger]
    check(charter_ow['rival_excommunication_ob_delta_campaign'] == 1,
          "Charter OW: rivals +1 Ob to Excomm this campaign")  # [canonical: see charter_of_liberties_outcome ledger]

    # Varfell's Hall
    check(m6.VAYNARDS_HALL_MILITARY_COST == -1 and m6.VAYNARDS_HALL_OB == 3, "Vaynard's Hall: M-1, Ob 3")  # [canonical: see VAYNARDS_HALL_MILITARY_COST + VAYNARDS_HALL_OB ledgers]

    check(m6.vaynards_hall_pool(4, False) == 4, "Vaynard's Hall Pool mil=4 no_tribune → 4")  # [canonical: see vaynards_hall_pool ledger]
    check(m6.vaynards_hall_pool(4, True) == 5, "Vaynard's Hall Pool mil=4 tribune_active → 5")  # [canonical: see vaynards_hall_pool ledger]

    vh_ow = m6.vaynards_hall_outcome('Overwhelming')
    check(vh_ow['varfell_mandate_delta'] == 2 and vh_ow['rival_l_delta'] == -1,
          "Vaynard's Hall OW: +2 Mandate, rival L -1")  # [canonical: see vaynards_hall_outcome ledger]


def t7_rm_cultural_uprising():
    print("\n=== T7: RM Cultural Uprising of T9 (victory §3.5 Phase 2) ===")
    # Phase 1 check — PT <= 1 in >= 4 playable territories
    pt_low = {tid: 1 for tid in ['T1', 'T2', 'T3', 'T4']}
    check(m6.uprising_phase_1_check(pt_low), "4 territories at PT 1 → Phase 1 met")  # [canonical: see uprising_phase_1_check ledger]

    pt_partial = {tid: 1 for tid in ['T1', 'T2', 'T3']}  # only 3
    check(not m6.uprising_phase_1_check(pt_partial), "3 territories at PT 1 → Phase 1 NOT met")  # [canonical: see UPRISING_PHASE_1_TERRITORY_COUNT ledger]

    pt_high = {tid: 2 for tid in ['T1', 'T2', 'T3', 'T4']}  # PT 2, not <= 1
    check(not m6.uprising_phase_1_check(pt_high), "4 territories at PT 2 → Phase 1 NOT met (threshold is <= 1)")  # [canonical: see UPRISING_PHASE_1_PT_THRESHOLD ledger]

    # Combined prerequisite (Phase 1 + MS >= 25)
    ok, _ = m6.uprising_prerequisite_check(pt_low, ms=30)  # [canonical: derived test boundary — see ledger entries + module constants]
    check(ok, "Phase 1 + MS 30 → prereq OK")  # [canonical: see uprising_prerequisite_check ledger]
    ok, _ = m6.uprising_prerequisite_check(pt_low, ms=24)
    check(not ok, "Phase 1 + MS 24 → prereq FAIL (below 25)")  # [canonical: see UPRISING_MS_PREREQUISITE ledger]
    ok, _ = m6.uprising_prerequisite_check(pt_partial, ms=30)
    check(not ok, "Phase 1 fail + MS 30 → prereq FAIL")

    # Ob formula: ceil(CI/10) clamped [1,5] + modifiers
    # CI=30 → ceil(3)=3; no modifiers → 3
    check(m6.uprising_ob(30, t9_pt=5, wc=0, church_mandate=3) == 3, "Ob at CI=30, no modifiers → 3")  # [canonical: see uprising_ob ledger]
    # CI=80 → ceil(8)=8, clamped to 5; +1 (CI>=50) = 6
    check(m6.uprising_ob(80, t9_pt=5, wc=0, church_mandate=3) == 6, "Ob at CI=80 → 5 (clamped) + 1 (CI>=50) = 6")  # [canonical: see uprising_ob ledger]
    # CI=80, T9 PT=1 → ceil(8)=8 clamped 5; -1 (PT<=1) +1 (CI>=50) = 5
    check(m6.uprising_ob(80, t9_pt=1, wc=0, church_mandate=3) == 5, "Ob at CI=80, T9 PT=1 → 5")  # [canonical: see uprising_ob ledger]
    # All modifiers: CI=80, PT 1, Mandate 5 → 5 -1 +1 +1 = 6
    check(m6.uprising_ob(80, t9_pt=1, wc=0, church_mandate=5) == 6, "Ob at CI=80, PT=1, Mandate=5 → 6")  # [canonical: see uprising_ob ledger]

    # Pool modifier: WC >= 2 → +1
    check(m6.uprising_pool_modifier(2) == 1, "WC=2 → pool +1")  # [canonical: see uprising_pool_modifier ledger]
    check(m6.uprising_pool_modifier(1) == 0, "WC=1 → pool +0")

    # Outcomes
    ow = m6.uprising_outcome('Overwhelming')
    check(ow['t9_transfers_to_rm'] is True, "OW: T9 transfers to RM")  # [canonical: see uprising_outcome ledger]
    check(ow['church_mandate_delta'] == -2, "OW: Church Mandate -2")  # [canonical: see uprising_outcome ledger]
    check(ow['ci_delta'] == -3, "OW: CI -3 (institutional rupture)")
    check(ow['t9_pt_delta'] == -2, "OW: T9 PT -2")
    check(ow['auto_presence_markers_t9'] == 2, "OW: +2 Presence markers in T9")  # [canonical: see uprising_outcome ledger]

    succ = m6.uprising_outcome('Success')
    check(succ['t9_transfers_to_rm'] is True and succ['church_mandate_delta'] == -1,
          "Success: T9 transfers, Church Mandate -1")  # [canonical: see uprising_outcome ledger]

    part = m6.uprising_outcome('Partial')
    check(part['t9_transfers_to_rm'] is False and part['t9_pt_delta'] == -1,
          "Partial: T9 does not transfer, PT -1")  # [canonical: see uprising_outcome ledger]
    check(part['uprising_used_this_arc'] is True, "Partial: Uprising spent for arc")

    fail = m6.uprising_outcome('Failure')
    check(fail['t9_transfers_to_rm'] is False and fail['ci_delta'] == 2 and fail['t9_pt_delta'] == 1,
          "Failure: crushed; CI +2, T9 PT +1")  # [canonical: see uprising_outcome ledger]


def t8_tactic_card_effects():
    print("\n=== T8: Tactic card mechanical effects (deferred from M3) ===")
    # Parametric pool modifiers — implementable
    rg = m6.tactic_card_effect('royal_guard')
    check(rg['attacker_pool_delta'] == 3, "Royal Guard: +3D attacker pool")  # [canonical: see FACTION_TACTIC_CARD_POOL_MODIFIERS ledger]

    ms = m6.tactic_card_effect('mercenary_surge')
    check(ms['attacker_pool_delta_costing_wealth'] == 2 and ms['wealth_cost'] == -1,
          "Mercenary Surge: +2 pool costing 1 W")  # [canonical: see FACTION_TACTIC_CARD_POOL_MODIFIERS ledger]

    sa = m6.tactic_card_effect('sovereign_authority')
    check(sa['immune_to_disposition_ob_penalties'] is True, "Sovereign Authority: immune to Disposition Ob penalties")  # [canonical: see FACTION_TACTIC_CARD_POOL_MODIFIERS ledger]

    pc = m6.tactic_card_effect('peoples_courage')
    check(pc['all_units_discipline_delta'] == 1, "People's Courage: +1 Discipline all units")  # [canonical: see FACTION_TACTIC_CARD_POOL_MODIFIERS ledger]

    # Cards requiring resolution-time hooks — raise NotImplementedError
    check_raises(lambda: m6.tactic_card_effect('stratagem'), NotImplementedError,
                 "Stratagem (2-pass init inversion) raises NotImplementedError")  # [canonical: see TACTIC_CARDS_REQUIRING_HOOKS ledger]
    check_raises(lambda: m6.tactic_card_effect('crusade_fervour'), NotImplementedError,
                 "Crusade Fervour (Discipline check exempt) raises NotImplementedError")  # [canonical: see TACTIC_CARDS_REQUIRING_HOOKS ledger]
    check_raises(lambda: m6.tactic_card_effect('inquisitors_mark'), NotImplementedError,
                 "Inquisitor's Mark (per-unit targeting) raises NotImplementedError")  # [canonical: see TACTIC_CARDS_REQUIRING_HOOKS ledger]
    check_raises(lambda: m6.tactic_card_effect('disappear'), NotImplementedError,
                 "Disappear (withdraw all units) raises NotImplementedError")  # [canonical: see TACTIC_CARDS_REQUIRING_HOOKS ledger]
    check_raises(lambda: m6.tactic_card_effect('calculated_retreat'), NotImplementedError,
                 "Calculated Retreat (outcome override) raises NotImplementedError")  # [canonical: see TACTIC_CARDS_REQUIRING_HOOKS ledger]
    check_raises(lambda: m6.tactic_card_effect('ducal_call'), NotImplementedError,
                 "Ducal Call (resolution-time state mutation) raises NotImplementedError")  # [canonical: see TACTIC_CARDS_REQUIRING_HOOKS ledger]

    # Unknown card raises ValueError (not NotImplementedError)
    check_raises(lambda: m6.tactic_card_effect('not_a_card'), ValueError,
                 "Unknown card raises ValueError")

    # Shared cards (handled by M3.apply_tactic_cards) return None from M6 — no extra effect
    check(m6.tactic_card_effect('standard_advance') is None,
          "Standard Advance: M6 returns None (M3 handles disposition)")
    check(m6.tactic_card_effect('disciplined_defence') is None,
          "Disciplined Defence: M6 returns None (M3 handles)")
    check(m6.tactic_card_effect('feigned_retreat') is None, "Feigned Retreat: M6 returns None")
    check(m6.tactic_card_effect('concentrated_strike') is None, "Concentrated Strike: M6 returns None")


def t9_action_registry():
    print("\n=== T9: M6 action registry ===")
    actions = m6.all_known_actions()
    expected = {'royal_progress', 'great_work', 'coronation_renewal', 'excommunication',
                'absolution', 'council_of_solmund', 'charter_of_liberties',
                'vaynards_hall', 'cultural_uprising_t9'}
    check(set(actions) == expected, f"9 actions registered",
          detail=f"got {len(actions)}: {actions}")

    # Crown Initiative modes
    check(m6.CROWN_INITIATIVE_MODES == ('royal_progress', 'great_work', 'coronation_renewal'),
          "Crown Initiative has 3 modes")  # [canonical: see CROWN_INITIATIVE_MODES ledger]
    check(m6.CROWN_INITIATIVE_FACTION == 'Crown', "Crown Initiative restricted to Crown faction")  # [canonical: see CROWN_INITIATIVE_FACTION ledger]
    check(m6.CROWN_INITIATIVE_SLOT == 'Senator Inward', "Crown Initiative slot = Senator Inward")  # [canonical: see CROWN_INITIATIVE_SLOT ledger]

    # Degree enum
    check(m6.DEGREES == ('Overwhelming', 'Success', 'Partial', 'Failure'),
          "4 degrees: OW/Success/Partial/Failure")  # [canonical: see DEGREES ledger]


def run_all():
    print("=" * 100)  # [canonical: N/A — display formatting]
    print("M6 Faction Action Expansion — Test Suite")
    print("=" * 100)  # [canonical: N/A — display formatting]
    t1_royal_progress()
    t2_great_work()
    t3_coronation_renewal()
    t4_excommunication()
    t5_absolution()
    t6_faction_analogues()
    t7_rm_cultural_uprising()
    t8_tactic_card_effects()
    t9_action_registry()
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
