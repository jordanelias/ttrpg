# m6_faction_actions — Module Six of the v17 strategic-sim integration plan.  # [canonical: N/A — doc]
#  # [canonical: N/A — doc]
# Faction-unique action expansion. Implements Crown Initiative 3 modes (Royal  # [canonical: N/A — doc]
# Progress / Great Work / Coronation Renewal), the faction analogues from  # [canonical: N/A — doc]
# Part 10 (Church Synod, Hafenmark Charter, Varfell's Hall), Church  # [canonical: N/A — doc]
# Excommunication and Absolution, RM Cultural Uprising of T9, and  # [canonical: N/A — doc]
# parametric faction-specific tactic-card pool modifiers (deferred from M3).  # [canonical: N/A — doc]
#  # [canonical: N/A — doc]
# This module is PURE PRIMITIVES — it computes pool/Ob/effect tables and  # [canonical: N/A — doc]
# returns structured outcome dicts. It does not mutate world state. Caller  # [canonical: N/A — doc]
# (the M7 integration runner) applies outcomes.  # [canonical: N/A — doc]
#  # [canonical: N/A — doc]
# Canonical sources:  # [canonical: N/A — doc]
#   - part10_crown_initiative_design_2026-05-14 Sections 3.1-3.7 (Crown  # [canonical: N/A — doc]
#     Initiative metadata + 3 modes); Section 5 (faction analogues).  # [canonical: N/A — doc]
#   - faction_canon_v30 Section 8.2 (Recovery paths — Church Absolution),  # [canonical: N/A — doc]
#     Section 9 (Unique Action Overview), Church sheet Section "Tactic /  # [canonical: N/A — doc]
#     Unique Actions" (Excommunication degree table).  # [canonical: N/A — doc]
#   - victory_v30 Sections 3.1 (Crown Peninsula Sovereignty), 3.2 (Church  # [canonical: N/A — doc]
#     Mass Seizure), 3.5 Phase 2 (RM Cultural Uprising of T9), 8 (RM  # [canonical: N/A — doc]
#     Founding Mechanic prerequisites).  # [canonical: N/A — doc]
#   - mass_battle_v30 Section B.4 (faction-specific tactic cards — disposition  # [canonical: N/A — doc]
#     routing already in M3; M6 adds parametric pool modifiers).  # [canonical: N/A — doc]
#  # [canonical: N/A — doc]
# Cross-module dependencies: imports M1 for SETTLEMENT_REGISTRY (Phase 1  # [canonical: N/A — doc]
# enumerations), M2 for CI milestone queries (Coronation Renewal interactions),  # [canonical: N/A — doc]
# M3 for TACTIC_CARDS registry (parametric pool-modifier extension).  # [canonical: N/A — doc]
#  # [canonical: N/A — doc]
# Provisional assumptions: see sim_verification_ledger provisional_assumptions  # [canonical: N/A — doc]
# block. Tags M6_ASSUMPTION_ONE..M6_ASSUMPTION_FIVE.  # [canonical: N/A — doc]

import math
import sys
import os
from typing import Optional

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import m1_church_infrastructure as m1
import m2_ci_political_revision as m2
import m3_mass_battle as m3


# ═══════════════════════════════════════════════════════════════════════════
# CONSTANTS — Outcome degree enum
# ═══════════════════════════════════════════════════════════════════════════

# [canonical: mc_v15 + victory_v30 outcome tables — degrees]
DEGREE_OVERWHELMING = 'Overwhelming'
DEGREE_SUCCESS = 'Success'
DEGREE_PARTIAL = 'Partial'
DEGREE_FAILURE = 'Failure'
DEGREES = (DEGREE_OVERWHELMING, DEGREE_SUCCESS, DEGREE_PARTIAL, DEGREE_FAILURE)


# ═══════════════════════════════════════════════════════════════════════════
# CROWN INITIATIVE — Card metadata (§3.1)
# ═══════════════════════════════════════════════════════════════════════════

CROWN_INITIATIVE_FACTION = 'Crown'  # [canonical: part10 §3.1 — Faction column]
CROWN_INITIATIVE_SLOT = 'Senator Inward'  # [canonical: part10 §3.1 — Slot column]
CROWN_INITIATIVE_MODES = ('royal_progress', 'great_work', 'coronation_renewal')  # [canonical: part10 §3.1 — Modes column]


# ═══════════════════════════════════════════════════════════════════════════
# CROWN INITIATIVE — Mode I Royal Progress (§3.2)
# ═══════════════════════════════════════════════════════════════════════════

ROYAL_PROGRESS_WEALTH_COST = -2  # [canonical: part10 §3.2 — "Wealth -2 (treasury for entertainment, gifts to hosts)"]


def royal_progress_ob(sum_own_territories_accord):
    # [canonical: part10 §3.2 — "Ob | floor(sum of own territories Accord / 2)"]
    return math.floor(sum_own_territories_accord / 2)


def royal_progress_pool(influence, standing_modifier):
    # [canonical: part10 §3.2 — "Pool | Influence + Standing modifier"]
    return influence + standing_modifier


def royal_progress_outcome(degree):
    # [canonical: part10 §3.2 outcome table]
    if degree == DEGREE_OVERWHELMING:
        return {
            'mandate_delta': 2,                                     # [canonical: part10 §3.2 Overwhelming row]
            'standing_delta': 1,                                    # [canonical: part10 §3.2 Overwhelming row]
            'accord_1_to_2_all_own': True,                          # [canonical: part10 §3.2 — "all own territories at Accord 1 → Accord 2"]
            'wealth_cost': ROYAL_PROGRESS_WEALTH_COST,
        }
    elif degree == DEGREE_SUCCESS:
        return {
            'mandate_delta': 1,                                     # [canonical: part10 §3.2 Success row]
            'lowest_accord_territory_plus_1': True,                 # [canonical: part10 §3.2 — "one own territory of choice (lowest Accord) +1 Accord"]
            'wealth_cost': ROYAL_PROGRESS_WEALTH_COST,
        }
    elif degree == DEGREE_PARTIAL:
        return {
            'standing_delta': 1,                                    # [canonical: part10 §3.2 Partial row]
            'wealth_cost': ROYAL_PROGRESS_WEALTH_COST,              # [canonical: part10 §3.2 — "cost still paid"]
        }
    elif degree == DEGREE_FAILURE:
        return {
            'standing_delta': -1,                                   # [canonical: part10 §3.2 Failure row]
            'wealth_cost': ROYAL_PROGRESS_WEALTH_COST,              # [canonical: part10 §3.2 — "cost paid"]
        }
    else:
        raise ValueError(f"Unknown degree: {degree}")


# ═══════════════════════════════════════════════════════════════════════════
# CROWN INITIATIVE — Mode II Great Work (§3.3)
# ═══════════════════════════════════════════════════════════════════════════

GREAT_WORK_WEALTH_COST_PER_SEASON = -1  # [canonical: part10 §3.3 — "Wealth -1 per season for 3 seasons"]
GREAT_WORK_SEASONS = 3  # [canonical: part10 §3.3 — "3 seasons"]
GREAT_WORK_FINAL_OB = 4  # [canonical: part10 §3.3 — "Ob (final season) | 4 — challenging; major project"]


def great_work_pool_final_season(mandate):
    # [canonical: part10 §3.3 — "Pool (final season) | Mandate (the institutional weight backing the project)"]
    return mandate


def great_work_outcome(degree):
    # [canonical: part10 §3.3 outcome table]
    if degree == DEGREE_OVERWHELMING:
        return {
            'mandate_delta': 2,                                     # [canonical: part10 §3.3 Overwhelming — "Mandate +2 permanent"]
            'mandate_permanent': True,                              # [canonical: part10 §3.3 — "permanent"]
            'charters_govern_ob_minus_1_permanent': True,           # [canonical: part10 §3.3 — "all own Charters gain Govern -1 Ob (permanent)"]
            'standing_delta': 2,                                    # [canonical: part10 §3.3 Overwhelming — "Standing +2"]
        }
    elif degree == DEGREE_SUCCESS:
        return {
            'mandate_delta': 2,                                     # [canonical: part10 §3.3 Success — "Mandate +2 permanent"]
            'mandate_permanent': True,                              # [canonical: part10 §3.3 — "permanent"]
        }
    elif degree == DEGREE_PARTIAL:
        return {
            'mandate_delta': 1,                                     # [canonical: part10 §3.3 Partial — "Mandate +1; sunk W cost partial loss"]
            'sunk_wealth_partial_loss': True,                       # [canonical: part10 §3.3 Partial — "sunk W cost partial loss"]
        }
    elif degree == DEGREE_FAILURE:
        return {
            'standing_delta': -2,                                   # [canonical: part10 §3.3 Failure — "Standing -2"]
            'cohesion_delta': -20,                                  # [canonical: part10 §3.3 Failure — "Cohesion -20 (per PP-515 breach penalties)"]
        }
    else:
        raise ValueError(f"Unknown degree: {degree}")


def great_work_mid_pledge_breach():
    # [canonical: part10 §3.3 — "Mid-pledge breach | Standing -2, Cohesion -20, Reputation -15 (PP-515)"]
    return {
        'standing_delta': -2,
        'cohesion_delta': -20,  # [canonical: see great_work_outcome Failure + mid_pledge_breach ledger — PP-515 breach magnitudes]
        'reputation_delta': -15,  # [canonical: see great_work_outcome Failure + mid_pledge_breach ledger — PP-515 breach magnitudes]
    }


# ═══════════════════════════════════════════════════════════════════════════
# CROWN INITIATIVE — Mode III Coronation Renewal (§3.4)
# ═══════════════════════════════════════════════════════════════════════════

CORONATION_WEALTH_COST = -2  # [canonical: part10 §3.4 — "Wealth -2 (ceremony, gifts to Church, hosting clergy)"]


def coronation_renewal_prerequisite_check(crown_church_relation, excommunication_active_this_season):
    # [canonical: part10 §3.4 — "Crown-Church active Truce, Peace, Alliance, or Crown Treaty; Church is not actively prosecuting an Excommunication against Crown this season"]
    valid_relations = ('truce', 'peace', 'alliance', 'crown_treaty')
    if crown_church_relation not in valid_relations:
        return False, f"Required relation in {valid_relations}; got '{crown_church_relation}'"
    if excommunication_active_this_season:
        return False, "Church is actively prosecuting Excommunication against Crown this season"
    return True, "ok"


def coronation_renewal_ob(church_mandate):
    # [canonical: part10 §3.4 — "Ob | floor(Church Mandate / 2) + 1"]
    return math.floor(church_mandate / 2) + 1


def coronation_renewal_pool(influence):
    # [canonical: part10 §3.4 — "Pool | Influence"]
    return influence


def coronation_renewal_outcome(degree, crown_currently_excommunicated):
    # [canonical: part10 §3.4 outcome table]
    if degree == DEGREE_OVERWHELMING:
        return {
            'mandate_delta': 2,                                     # [canonical: part10 §3.4 Overwhelming — "Mandate +2"]
            'lifts_excommunication': crown_currently_excommunicated,  # [canonical: part10 §3.4 — "if Crown currently Excommunicated, Excommunication lifted"]
            'standing_delta': 1,                                    # [canonical: part10 §3.4 Overwhelming — "Standing +1"]
            'crown_church_standing_delta': 1,                       # [canonical: part10 §3.4 Overwhelming — "Crown-Church Standing +1"]
            'wealth_cost': CORONATION_WEALTH_COST,
        }
    elif degree == DEGREE_SUCCESS:
        return {
            'mandate_delta': 1,                                     # [canonical: part10 §3.4 Success — "Mandate +1"]
            'lifts_excommunication': crown_currently_excommunicated,  # [canonical: part10 §3.4 — "Excommunication lifted if currently active"]
            'wealth_cost': CORONATION_WEALTH_COST,
        }
    elif degree == DEGREE_PARTIAL:
        return {
            'standing_delta': 1,                                    # [canonical: part10 §3.4 Partial — "Standing +1"]
            'wealth_cost': CORONATION_WEALTH_COST,                  # [canonical: part10 §3.4 — "no L change"]
        }
    elif degree == DEGREE_FAILURE:
        return {
            'standing_delta': -1,                                   # [canonical: part10 §3.4 Failure — "Standing -1"]
            'wealth_cost': CORONATION_WEALTH_COST,                  # [canonical: part10 §3.4 — "cost paid"]
        }
    else:
        raise ValueError(f"Unknown degree: {degree}")


# ═══════════════════════════════════════════════════════════════════════════
# CHURCH EXCOMMUNICATION — faction_canon §9 + Church sheet
# ═══════════════════════════════════════════════════════════════════════════

EXCOMMUNICATION_PREREQUISITE_CHURCH_L = 3  # [canonical: faction_canon Church sheet — "Requires Church L >= 3"]
EXCOMMUNICATION_OB_NON_LEADER = 2  # [canonical: faction_canon §9 — "Ob 2 (non-leader)"]


def excommunication_prerequisite_check(church_l):
    # [canonical: faction_canon Church sheet — "Requires Church L >= 3"]
    if church_l < EXCOMMUNICATION_PREREQUISITE_CHURCH_L:
        return False, f"Church L {church_l} below threshold {EXCOMMUNICATION_PREREQUISITE_CHURCH_L}"
    return True, "ok"


def excommunication_ob(target_l, is_leader):
    # [canonical: faction_canon §9 — "L vs target L (leader) / Ob 2 (non-leader)"]
    if is_leader:
        return target_l
    return EXCOMMUNICATION_OB_NON_LEADER


def excommunication_pool(church_l):
    # [canonical: faction_canon §9 — "L" (Church L)]
    return church_l


def excommunication_outcome(degree):
    # [canonical: faction_canon Church sheet Excommunication degree table]
    if degree == DEGREE_OVERWHELMING:
        return {
            'target_mandate_delta': -1,                             # [canonical: faction_canon Church — "target faction L -1"]
            'strips_circles_bonus': True,                           # [canonical: faction_canon Church — "Strips target's Circles bonus with Church contacts"]
            'barred_from_public_office': True,                      # [canonical: faction_canon Church — "target barred from public office and Church-loyal command"]
            'target_personal_reputation_delta': -1,                 # [canonical: faction_canon Church — "personal Reputation -1 with all factions"]
        }
    elif degree == DEGREE_SUCCESS:
        return {
            'target_mandate_delta': -1,                             # [canonical: faction_canon Church — "As Overwhelming minus the personal Reputation penalty"]
            'strips_circles_bonus': True,
            'barred_from_public_office': True,
        }
    elif degree == DEGREE_PARTIAL:
        # Canon doesn't define Partial for Excommunication explicitly.
        # Outcome table only lists Overwhelming/Success/Failure.
        # M6 defaults Partial to "no effect, cost paid" — caller still spent a card slot.
        return {}
    elif degree == DEGREE_FAILURE:
        return {
            'church_mandate_delta': -1,                             # [canonical: faction_canon Church — "Church L -1"]
            'target_mandate_delta': 1,                              # [canonical: faction_canon Church — "target gains L +1 (sympathy martyr)"]
        }
    else:
        raise ValueError(f"Unknown degree: {degree}")


# ═══════════════════════════════════════════════════════════════════════════
# CHURCH ABSOLUTION — faction_canon §8.2 (M6_ASSUMPTION_ONE)
# ═══════════════════════════════════════════════════════════════════════════

# [canonical: faction_canon §8.2 — "Church Absolution (Church unique action): +1 to target"]
# [M6_ASSUMPTION_ONE: canon specifies the +1 Stability effect but not Pool/Ob/cost.
#  M6 declares Pool=Influence, Ob=3, cost=Mandate-1 (Church spends institutional capital).
#  Frequency: 1/season. Surface for ratification.]
ABSOLUTION_OB = 3
ABSOLUTION_CHURCH_MANDATE_COST = -1
ABSOLUTION_TARGET_STABILITY_BONUS = 1


def absolution_pool(church_influence):
    # [canonical: faction_canon §8.2 — "Church Absolution (Church unique action)"]
    # [M6_ASSUMPTION_ONE: Pool = Influence]
    return church_influence


def absolution_outcome(degree):
    # [canonical: faction_canon §8.2 — "+1 to target"]
    # [M6_ASSUMPTION_ONE: degree-graded effects on +1 Stability base]
    if degree == DEGREE_OVERWHELMING:
        return {
            'target_stability_delta': 2,                            # [canonical: see ABSOLUTION_TARGET_STABILITY_BONUS — OW doubles]
            'church_mandate_delta': ABSOLUTION_CHURCH_MANDATE_COST,
        }
    elif degree == DEGREE_SUCCESS:
        return {
            'target_stability_delta': ABSOLUTION_TARGET_STABILITY_BONUS,
            'church_mandate_delta': ABSOLUTION_CHURCH_MANDATE_COST,
        }
    elif degree == DEGREE_PARTIAL:
        return {
            'church_mandate_delta': ABSOLUTION_CHURCH_MANDATE_COST,  # cost paid, no target effect
        }
    elif degree == DEGREE_FAILURE:
        return {
            'church_mandate_delta': ABSOLUTION_CHURCH_MANDATE_COST,  # cost paid
            'church_standing_delta': -1,                              # public ceremony failed
        }
    else:
        raise ValueError(f"Unknown degree: {degree}")


# ═══════════════════════════════════════════════════════════════════════════
# CHURCH COUNCIL (SYNOD) — part10 §5.1 analogue
# ═══════════════════════════════════════════════════════════════════════════

# [canonical: part10 §5.1 — "Council of Solmund - Special/Unique Power"]
COUNCIL_FREQUENCY = 'per_arc'  # [canonical: part10 §5.1 — "1x per arc (rare event)"]
COUNCIL_OB_BASE = 2  # [canonical: part10 §5.1 — "Ob | floor(CI / 30) + 2"]


def council_of_solmund_ob(ci):
    # [canonical: part10 §5.1 — "floor(CI / 30) + 2 (easier when CI is high)"]
    return math.floor(ci / 30) + COUNCIL_OB_BASE


def council_of_solmund_pool(church_mandate):
    # [canonical: part10 §5.1 — "Pool | Mandate"]
    return church_mandate


def council_of_solmund_outcome(degree):
    # [canonical: part10 §5.1 — Effects rows]
    if degree == DEGREE_OVERWHELMING:
        return {
            'church_mandate_delta': 2,                              # [canonical: part10 §5.1 OW — "Church Mandate +2"]
            'cardinal_focus_permanent': True,                       # [canonical: part10 §5.1 OW — "choose a Cardinal Focus permanent"]
            'rival_l_delta': -1,                                    # [canonical: part10 §5.1 OW — "select one rival faction's L → -1 (formal censure)"]
        }
    elif degree == DEGREE_SUCCESS:
        return {
            'church_mandate_delta': 1,                              # [canonical: part10 §5.1 Success — "Church Mandate +1"]
            'cardinal_focus_permanent': True,                       # [canonical: part10 §5.1 — "one Cardinal Focus permanent for this campaign"]
        }
    elif degree == DEGREE_PARTIAL:
        return {}  # cost paid, no effect (M6_ASSUMPTION_FIVE)
    elif degree == DEGREE_FAILURE:
        return {}  # cost paid, no effect
    else:
        raise ValueError(f"Unknown degree: {degree}")


# ═══════════════════════════════════════════════════════════════════════════
# HAFENMARK CHARTER OF LIBERTIES — part10 §5.2 analogue
# ═══════════════════════════════════════════════════════════════════════════

CHARTER_DIPLOMATIC_TOKEN_COST = 1  # [canonical: part10 §5.2 — "1 Diplomatic Token (consumed)"]
CHARTER_WEALTH_COST = -1  # [canonical: part10 §5.2 — "W -1"]
CHARTER_OB = 4  # [canonical: part10 §5.2 — "Ob | 4"]


def charter_of_liberties_pool(influence, active_tokens_on_opponents):
    # [canonical: part10 §5.2 — "Pool | Influence + (active Tokens on opponents)"]
    return influence + active_tokens_on_opponents


def charter_of_liberties_outcome(degree):
    # [canonical: part10 §5.2 — Effects rows]
    if degree == DEGREE_OVERWHELMING:
        return {
            'hafenmark_mandate_delta': 2,                           # [canonical: part10 §5.2 OW — "Hafenmark Mandate +2"]
            'pi_delta': -2,                                         # [canonical: part10 §5.2 OW — "PI -2"]
            'rival_excommunication_ob_delta_campaign': 1,           # [canonical: part10 §5.2 OW — "all rival factions face +1 Ob to Excommunication attempts this campaign"]
        }
    elif degree == DEGREE_SUCCESS:
        return {
            'hafenmark_mandate_delta': 1,                           # [canonical: part10 §5.2 Success — "Hafenmark Mandate +1"]
            'pi_delta': -1,                                         # [canonical: part10 §5.2 Success — "PI -1"]
        }
    elif degree == DEGREE_PARTIAL:
        return {}
    elif degree == DEGREE_FAILURE:
        return {}
    else:
        raise ValueError(f"Unknown degree: {degree}")


# ═══════════════════════════════════════════════════════════════════════════
# VARFELL'S HALL — part10 §5.3 analogue
# ═══════════════════════════════════════════════════════════════════════════

VAYNARDS_HALL_MILITARY_COST = -1  # [canonical: part10 §5.3 — "Military -1"]
VAYNARDS_HALL_WEALTH_COST = -1  # [canonical: part10 §5.3 — "W -1"]
VAYNARDS_HALL_OB = 3  # [canonical: part10 §5.3 — "Ob | 3"]


def vaynards_hall_pool(military, tribune_network_active_flag):
    # [canonical: part10 §5.3 — "Pool | Mil + (Tribune Network active)"]
    return military + (1 if tribune_network_active_flag else 0)


def vaynards_hall_outcome(degree):
    # [canonical: part10 §5.3 — Effects rows]
    if degree == DEGREE_OVERWHELMING:
        return {
            'varfell_mandate_delta': 2,                             # [canonical: part10 §5.3 OW — "Varfell Mandate +2"]
            'rival_l_delta': -1,                                    # [canonical: part10 §5.3 OW — "one rival faction L -1 (publicly insulted)"]
        }
    elif degree == DEGREE_SUCCESS:
        return {
            'varfell_mandate_delta': 1,                             # [canonical: part10 §5.3 Success — "Varfell Mandate +1"]
            'revelation_token_sacrificed_for_standing': True,       # [canonical: part10 §5.3 Success — "one captured Revelation Token sacrificed for +1 Standing"]
        }
    elif degree == DEGREE_PARTIAL:
        return {}
    elif degree == DEGREE_FAILURE:
        return {}
    else:
        raise ValueError(f"Unknown degree: {degree}")


# ═══════════════════════════════════════════════════════════════════════════
# RM CULTURAL UPRISING OF T9 — victory_v30 §3.5 Phase 2
# ═══════════════════════════════════════════════════════════════════════════

UPRISING_PHASE_1_PT_THRESHOLD = 1  # [canonical: victory §3.5 Phase 1 — "PT <= 1"]
UPRISING_PHASE_1_TERRITORY_COUNT = 4  # [canonical: victory §3.5 Phase 1 PP-543 — ">= 4 of the 15 playable territories"]
UPRISING_MS_PREREQUISITE = 25  # [canonical: victory §3.5 Phase 2 — "MS >= 25 required"]
UPRISING_OB_DIVISOR = 10  # [canonical: victory §3.5 Phase 2 — "Ob = CI / 10 (round up)"]
UPRISING_OB_MIN = 1  # [canonical: victory §3.5 Phase 2 — "min 1"]
UPRISING_OB_MAX = 5  # [canonical: victory §3.5 Phase 2 — "max 5"]
UPRISING_T9_TARGET = 'T9'  # [canonical: victory §3.5 Phase 2 — "T9 Himmelenger"]


def uprising_phase_1_check(pt_by_territory, playable_territories=None):
    # [canonical: victory §3.5 Phase 1 — "PT <= 1 in >= 4 of the 15 playable territories"]
    if playable_territories is None:
        playable_territories = m1.PLAYABLE_TERRITORIES
    qualifying = sum(1 for tid in playable_territories if pt_by_territory.get(tid, 5) <= UPRISING_PHASE_1_PT_THRESHOLD)  # [canonical: 5 = default PT=Piety pole for unset territories per uprising_phase_1_check ledger]
    return qualifying >= UPRISING_PHASE_1_TERRITORY_COUNT


def uprising_prerequisite_check(pt_by_territory, ms, playable_territories=None):
    # [canonical: victory §3.5 Phase 2 — "Available only while Phase 1 condition is met. MS >= 25 required"]
    if not uprising_phase_1_check(pt_by_territory, playable_territories):
        return False, "Phase 1 not met (PT <= 1 in fewer than 4 playable territories)"
    if ms < UPRISING_MS_PREREQUISITE:
        return False, f"MS {ms} below threshold {UPRISING_MS_PREREQUISITE}"
    return True, "ok"


def uprising_ob(ci, t9_pt, wc, church_mandate):
    # [canonical: victory §3.5 Phase 2 — "Weaver Thread pool vs Ob = CI / 10 (round up, min 1, max 5)"]
    # [canonical: victory §3.5 Phase 2 modifiers]
    base_ob = max(UPRISING_OB_MIN, min(UPRISING_OB_MAX, math.ceil(ci / UPRISING_OB_DIVISOR)))
    # Modifiers:
    if t9_pt <= 1:
        base_ob -= 1  # [canonical: victory §3.5 — "T9 PT <= 1: Ob -1"]
    if ci >= 50:
        base_ob += 1  # [canonical: victory §3.5 — "CI >= 50 at declaration: Ob +1"]
    if church_mandate >= 5:
        base_ob += 1  # [canonical: victory §3.5 — "Church Mandate >= 5: Ob +1"]
    return base_ob


def uprising_pool_modifier(wc):
    # [canonical: victory §3.5 Phase 2 — "WC >= 2: +1D (Wardens support the Uprising)"]
    return 1 if wc >= 2 else 0


def uprising_outcome(degree):
    # [canonical: victory §3.5 Phase 2 outcome table]
    if degree == DEGREE_OVERWHELMING:
        return {
            't9_transfers_to_rm': True,                             # [canonical: victory §3.5 OW — "T9 transfers to RM administration"]
            'church_mandate_delta': -2,                             # [canonical: victory §3.5 OW — "Church Mandate -2"]
            'ci_delta': -3,                                         # [canonical: victory §3.5 OW — "CI -3 (institutional rupture)"]
            't9_pt_delta': -2,                                      # [canonical: victory §3.5 OW — "T9 PT -2"]
            'auto_presence_markers_t9': 2,                          # [canonical: victory §3.5 — "Overwhelming Uprising bonus: +2 Presence markers in T9"]
        }
    elif degree == DEGREE_SUCCESS:
        return {
            't9_transfers_to_rm': True,                             # [canonical: victory §3.5 Success — "T9 transfers to RM administration"]
            'church_mandate_delta': -1,                             # [canonical: victory §3.5 Success — "Church Mandate -1"]
        }
    elif degree == DEGREE_PARTIAL:
        return {
            't9_transfers_to_rm': False,                            # [canonical: victory §3.5 Partial — "T9 does not transfer"]
            't9_pt_delta': -1,                                      # [canonical: victory §3.5 Partial — "PT in T9 -1"]
            'uprising_used_this_arc': True,                         # [canonical: victory §3.5 Partial — "Uprising attempt used up for this arc"]
        }
    elif degree == DEGREE_FAILURE:
        return {
            't9_transfers_to_rm': False,                            # [canonical: victory §3.5 Failure — "Uprising crushed"]
            'ci_delta': 2,                                          # [canonical: victory §3.5 Failure — "CI +2 (Church authority strengthened by resistance)"]
            't9_pt_delta': 1,                                       # [canonical: victory §3.5 Failure — "T9 PT +1"]
            'uprising_used_this_arc': True,                         # [canonical: victory §3.5 Failure — "Uprising attempt used up for this arc"]
        }
    else:
        raise ValueError(f"Unknown degree: {degree}")


# ═══════════════════════════════════════════════════════════════════════════
# FACTION-SPECIFIC TACTIC CARD POOL MODIFIERS — §B.4 (deferred from M3)
# ═══════════════════════════════════════════════════════════════════════════

# Parametric pool modifiers — cards whose effect is a constant pool delta or simple condition.
# [canonical: mass_battle_v30 §B.4 faction-specific tactic cards table]
# [M6_ASSUMPTION_THREE: M6 implements constant pool-modifier cards;
#  cards requiring resolution-time hooks raise NotImplementedError]
FACTION_TACTIC_CARD_POOL_MODIFIERS = {
    # Crown
    'royal_guard': {'attacker_pool_delta': 3, 'description': 'Elite unit +3D'},
    # [canonical: mass_battle_v30 §B.4 — "Royal Guard (Elite unit +3D)"]
    # M3_ASSUMPTION_ONE note: §B.4 says "Elite unit" implying per-unit targeting;
    # M6 simplifies to +3D pool. Per-unit targeting is M7 integration concern.

    # Hafenmark
    'mercenary_surge': {'attacker_pool_delta_costing_wealth': 2, 'wealth_cost': -1, 'description': 'Pay 1 Wealth: +2 units this engagement'},
    # [canonical: mass_battle_v30 §B.4 — "Mercenary Surge (pay 1 Wealth: +2 units this engagement)"]
    'sovereign_authority': {'immune_to_disposition_ob_penalties': True, 'description': 'Immune to Disposition table Ob penalties this engagement'},
    # [canonical: mass_battle_v30 §B.4 — "Sovereign Authority (immune to Disposition table Ob penalties this engagement)"]

    # Guilds
    'paid_off': {'opponent_pool_delta': -1, 'wealth_cost': -1, 'description': 'Opponent unit -1D; costs 1 Wealth'},
    # [canonical: mass_battle_v30 §B.4 — "Paid Off (opponent unit -1D; costs 1 Wealth)"]
    'logistics_mastery': {'strained_units_at_full': True, 'description': 'Strained units fight at full this engagement'},
    # [canonical: mass_battle_v30 §B.4 — "Logistics Mastery (Strained units fight at full this engagement)"]

    # Niflhel
    'assassination': {'opponent_pool_delta_all_units': -1, 'description': 'Target opponent commander; -1D all opp. units'},
    # [canonical: mass_battle_v30 §B.4 — "Assassination (target opponent commander; -1D all opp. units)"]

    # Löwenritter
    'iron_discipline': {'immune_to_route': True, 'description': 'Immune to Route this engagement'},
    # [canonical: mass_battle_v30 §B.4 — "Iron Discipline (immune to Route this engagement)"]
    'martial_law': {'martial_law_next_season_on_win': True, 'description': 'After winning: territory gains Martial Law next season'},
    # [canonical: mass_battle_v30 §B.4 — "Martial Law (after winning: territory gains Martial Law next season)"]

    # Revolution
    'peoples_courage': {'all_units_discipline_delta': 1, 'description': "Discipline +1 all units this engagement"},
    # [canonical: mass_battle_v30 §B.4 — "People's Courage (Discipline +1 all units this engagement)"]
    'ambush': {'opponent_no_defence_roll_in_specific_territories': ('Oastad', 'Stillhelm'), 'description': 'First engagement in Oastad or Stillhelm: opponent no Defence roll'},
    # [canonical: mass_battle_v30 §B.4 — "Ambush (first engagement in Oastad or Stillhelm: opponent no Defence roll)"]
}

# Cards requiring resolution-time hooks (not implementable in M6 primitives layer)
# [canonical: mass_battle_v30 §B.4 + M3_ASSUMPTION_ONE deferred-to-M6 list]
TACTIC_CARDS_REQUIRING_HOOKS = frozenset({
    'crusade_fervour',        # Church — Discipline check exempt this turn (overrides check_route)
    # [canonical: mass_battle_v30 §B.4 — "Crusade Fervour (Brutal + Discipline check exempt this turn)"]
    'inquisitors_mark',       # Church — target unit -2D (requires per-unit targeting)
    # [canonical: mass_battle_v30 §B.4 — "Inquisitor's Mark (target unit -2D, any opponent)"]
    'stratagem',              # Varfell — 2-pass init inversion (read opposing card before locking)
    # [canonical: mass_battle_v30 §B.4 — "Stratagem (read opponent's tactic card before locking yours)"]
    'calculated_retreat',     # Varfell — withdraw without Overextended (overrides outcome)
    # [canonical: mass_battle_v30 §B.4 — "Calculated Retreat (withdraw without Overextended penalty)"]
    'disappear',              # Niflhel — withdraw all units; opponent cannot pursue (overrides outcome)
    # [canonical: mass_battle_v30 §B.4 — "Disappear (withdraw all units; opponent cannot pursue this season)"]
    'ducal_call',             # Crown — summon 1 unit from adjacent territory (resolution-time state mutation)
    # [canonical: mass_battle_v30 §B.4 — "Ducal Call (summon 1 unit from adjacent territory)"]
})


def tactic_card_effect(card_id):
    # [canonical: mass_battle_v30 §B.4 — registered card effects]
    # [M6_ASSUMPTION_THREE: M6 returns parametric effects; hooks-required cards raise]
    if card_id not in m3.TACTIC_CARDS:
        raise ValueError(f"Unknown tactic card: {card_id}")
    if card_id in TACTIC_CARDS_REQUIRING_HOOKS:
        raise NotImplementedError(
            f"Tactic card '{card_id}' requires resolution-time hooks not present in M6 primitives layer. "
            f"M7 integration must wire a post-resolution callback. See mass_battle_v30 §B.4."
        )
    if card_id in FACTION_TACTIC_CARD_POOL_MODIFIERS:
        return FACTION_TACTIC_CARD_POOL_MODIFIERS[card_id]
    # Shared cards already handled by M3.apply_tactic_cards
    return None  # parametric effect not declared by M6 (shared card or no extra effect)


# ═══════════════════════════════════════════════════════════════════════════
# CONVENIENCE — outcome envelope for caller logging
# ═══════════════════════════════════════════════════════════════════════════

def empty_outcome():
    # [canonical: derived helper — default outcome for unknown degrees / no effect]
    return {}


def all_known_actions():
    # [canonical: M6 action surface — list of all faction-unique actions implemented]
    return (
        'royal_progress',
        'great_work',
        'coronation_renewal',
        'excommunication',
        'absolution',
        'council_of_solmund',
        'charter_of_liberties',
        'vaynards_hall',
        'cultural_uprising_t9',
    )
