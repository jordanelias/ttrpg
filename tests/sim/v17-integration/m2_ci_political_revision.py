# m2_ci_political_revision — Module Two of the v17 strategic-sim integration plan.  # [canonical: N/A — doc]
#  # [canonical: N/A — doc]
# CI cap mechanics, milestone effects, political legitimacy modifiers (Bonus  # [canonical: N/A — doc]
# Dice and Obstacle Modifier), and the Unification simultaneous-seizure  # [canonical: N/A — doc]
# target-list generator.  # [canonical: N/A — doc]
#  # [canonical: N/A — doc]
# This module is PURE PRIMITIVES — it does not own World/Faction/Territory  # [canonical: N/A — doc]
# classes, does not run a simulation, does not classify which CI deltas are  # [canonical: N/A — doc]
# "Domain Action" vs "generated" (caller responsibility). The integration  # [canonical: N/A — doc]
# module wires these primitives into the next-version sim.  # [canonical: N/A — doc]
#  # [canonical: N/A — doc]
# Canonical sources (force_full reads required to validate this module):  # [canonical: N/A — doc]
#   - ci_political_v30 Sections §2 (CI 0-100 mechanics), §3 (CI as Political  # [canonical: N/A — doc]
#     Legitimacy), §4.1 (How Stats Change), §7.1 (CI Cap audit).  # [canonical: N/A — doc]
#   - victory_v30 Section §3.2 (Church Mass Seizure, Hafenmark suppress).  # [canonical: N/A — doc]
#  # [canonical: N/A — doc]
# Cross-module dependency: imports M1 (m1_church_infrastructure) for the  # [canonical: N/A — doc]
# settlement registry, has_any_church_building check, Spiritual Weight table,  # [canonical: N/A — doc]
# and PLAYABLE_TERRITORIES set. The CI=100 Unification target-list generator  # [canonical: N/A — doc]
# queries M1's per-settlement infrastructure state.  # [canonical: N/A — doc]
#  # [canonical: N/A — doc]
# Provisional assumptions for ratification: see sim_verification_ledger  # [canonical: N/A — doc]
# provisional_assumptions block. Tags ASSUMPTION_ONE through ASSUMPTION_FIVE.  # [canonical: N/A — doc]

import math
import sys
import os

# Import M1 primitives. The integration module will resolve the path; for
# module-level tests run from /home/claude, sys.path is preconfigured by the
# test runner.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import m1_church_infrastructure as m1


# ═══════════════════════════════════════════════════════════════════════════
# CONSTANTS — CI mechanics
# ═══════════════════════════════════════════════════════════════════════════

# CI starting value
CI_STARTING_VALUE = 28  # [canonical: ci_political_v30 §2.3 — P-32]

# CI hard bounds
CI_MIN = 0  # [canonical: ci_political_v30 §2.1 — runs 0 to 100, no freeze]
CI_MAX = 100  # [canonical: ci_political_v30 §2.1 — runs 0 to 100, no freeze]

# Seasonal delta caps
CI_SEASONAL_CAP_MAGNITUDE = 5  # [canonical: ci_political_v30 §2.4 — PP-504, ±5/season from all sources]
CI_DOMAIN_ACTION_SUBCAP = 3  # [canonical: ci_political_v30 §2.4 — ±3 from player Domain Actions]


# ═══════════════════════════════════════════════════════════════════════════
# CONSTANTS — CI milestones (§2.1 table)
# ═══════════════════════════════════════════════════════════════════════════

CI_MILESTONE_ASSERTIVE = 40       # [canonical: ci_political_v30 §2.1 — Church Assertive]
CI_MILESTONE_INSTITUTIONAL = 55   # [canonical: ci_political_v30 §2.1 — Institutional Reach]
CI_MILESTONE_DOMINANT = 65        # [canonical: ci_political_v30 §2.1 — Church Dominant]
CI_MILESTONE_ASCENDANT = 80       # [canonical: ci_political_v30 §2.1 — Church Ascendant; redeclared from M1]
CI_MILESTONE_UNIFICATION = 100    # [canonical: ci_political_v30 §2.2 — Unification; redeclared from M1]

# Milestone 40 — Church Assertive
ASSERTIVE_BONUS_DICE = 1  # [canonical: ci_political_v30 §2.1 — "+1D on all Assert and Seizure rolls"]

# Milestone 55 — Institutional Reach
INSTITUTIONAL_REACH_OB_PENALTY = 1  # [canonical: ci_political_v30 §2.1 — "Ob +1 to actions directly opposing Church"]

# Milestone 65 — Church Dominant
DOMINANT_BASE_SLOT_COST = 1  # [canonical: faction_layer_v30 §5 default — Parliamentary motion = 1 card slot]
DOMINANT_EXTRA_SLOT_COST = 2  # [canonical: ci_political_v30 §2.1 — "two slots not one"]


# ═══════════════════════════════════════════════════════════════════════════
# CONSTANTS — CI Political Legitimacy (§3)
# ═══════════════════════════════════════════════════════════════════════════

CI_BONUS_DICE_DIVISOR = 20  # [canonical: ci_political_v30 §3.2 — floor(CI/20)]
CI_OBSTACLE_DIVISOR = 30  # [canonical: ci_political_v30 §3.3 — floor(CI/30)]


# ═══════════════════════════════════════════════════════════════════════════
# CONSTANTS — Hafenmark suppress (§7.1 / victory_v30 §3.2)
# ═══════════════════════════════════════════════════════════════════════════

HAFENMARK_CI_SUPPRESS_THRESHOLD = 4.0  # [canonical: victory_v30 §3.2 — Haf.L ≥ 4 triggers suppress]
HAFENMARK_CI_SUPPRESS_MAGNITUDE = -1.0  # [canonical: victory_v30 §3.2 — flat -1 per ED-110]


# ═══════════════════════════════════════════════════════════════════════════
# CI BOUNDS AND DELTA APPLICATION
# ═══════════════════════════════════════════════════════════════════════════

def clamp_ci(value):
    # [canonical: ci_political_v30 §2.1 — CI runs 0 to 100, no freeze]
    return max(CI_MIN, min(CI_MAX, value))


def apply_ci_delta(current_ci, source_deltas):
    # [canonical: ci_political_v30 §2.4 — ±5/season total, ±3 from Domain Actions]
    # [ASSUMPTION_ONE: caller labels each delta source via 'kind' field — either
    #   'domain_action' or 'generated'. M2 enforces caps; M2 does not classify.]
    # [ASSUMPTION_TWO: when both caps would clamp, the Domain-Action sub-cap is
    #   applied first; the remaining DA-clamped DA total plus non-DA total is
    #   then clamped against the seasonal total cap.]
    #
    # source_deltas: list of dicts, each:
    #   {'name': str, 'kind': 'domain_action' | 'generated', 'delta': float}
    #
    # Returns:
    #   {'new_ci': float, 'applied_total': float, 'da_applied': float,
    #    'gen_applied': float, 'sources': [{name, kind, requested, applied}]}
    da_requested = sum(d['delta'] for d in source_deltas if d.get('kind') == 'domain_action')
    gen_requested = sum(d['delta'] for d in source_deltas if d.get('kind') == 'generated')

    # Step 1: clamp DA portion to ±3
    da_cap = float(CI_DOMAIN_ACTION_SUBCAP)
    da_applied = max(-da_cap, min(da_cap, da_requested))

    # Step 2: clamp total (DA_applied + gen_requested) to ±5
    total_cap = float(CI_SEASONAL_CAP_MAGNITUDE)
    raw_total = da_applied + gen_requested
    total_applied = max(-total_cap, min(total_cap, raw_total))

    # Step 3: distribute the total_cap clamp back onto gen_requested (DA stays at da_applied)
    # If total_applied differs from raw_total, the difference comes from clipping
    # the generated portion (DA already clipped in step 1).
    if total_applied != raw_total:
        # Generated absorbs the difference
        gen_applied = total_applied - da_applied
    else:
        gen_applied = gen_requested

    # Build per-source applied amounts proportionally within their kind
    sources_report = []
    if da_requested != 0:
        da_scale = da_applied / da_requested if da_requested else 1.0
    else:
        da_scale = 1.0
    if gen_requested != 0:
        gen_scale = gen_applied / gen_requested if gen_requested else 1.0
    else:
        gen_scale = 1.0
    for d in source_deltas:
        kind = d.get('kind')
        requested = d['delta']
        if kind == 'domain_action':
            applied = requested * da_scale
        elif kind == 'generated':
            applied = requested * gen_scale
        else:
            # Unknown kind — pass through unscaled but still subject to the hard CI bounds at step 4
            applied = requested
        sources_report.append({
            'name': d.get('name', '?'),
            'kind': kind,
            'requested': requested,
            'applied': applied,
        })

    # Step 4: hard CI bound clamp
    new_ci_raw = current_ci + total_applied
    new_ci = clamp_ci(new_ci_raw)

    # If hard bounds clipped further, reflect the residual back into total_applied
    # so the returned total_applied honours the bounds.
    if new_ci != new_ci_raw:
        total_applied = new_ci - current_ci

    return {
        'new_ci': new_ci,
        'applied_total': total_applied,
        'da_applied': da_applied,
        'gen_applied': gen_applied,
        'sources': sources_report,
    }


# ═══════════════════════════════════════════════════════════════════════════
# CI POLITICAL LEGITIMACY — Bonus Dice and Obstacle Modifier
# ═══════════════════════════════════════════════════════════════════════════

def ci_bonus_dice(ci):
    # [canonical: ci_political_v30 §3.2 — Church adds floor(CI / divisor) bonus dice
    #  in Parliamentary motions, Treaty rolls, Diplomacy vs PLAYABLE]
    return math.floor(ci / CI_BONUS_DICE_DIVISOR)


def ci_obstacle_modifier(ci):
    # [canonical: ci_political_v30 §3.3 — secular factions voting against Church
    #  reduce effective Mandate by floor(CI / divisor); returned as a negative integer]
    return -math.floor(ci / CI_OBSTACLE_DIVISOR)


# ═══════════════════════════════════════════════════════════════════════════
# HAFENMARK SUPPRESS
# ═══════════════════════════════════════════════════════════════════════════

def hafenmark_ci_suppress(hafenmark_legitimacy):
    # [canonical: victory_v30 §3.2 — Hafenmark flat -1 CI/season when L >= threshold]
    if hafenmark_legitimacy >= HAFENMARK_CI_SUPPRESS_THRESHOLD:
        return HAFENMARK_CI_SUPPRESS_MAGNITUDE
    return 0.0


# ═══════════════════════════════════════════════════════════════════════════
# MILESTONE EFFECT QUERIES
# ═══════════════════════════════════════════════════════════════════════════

def church_assertive_bonus_dice(ci):
    # [canonical: ci_political_v30 §2.1 milestone 40 — Church Assertive
    #  threshold-inclusive (ASSUMPTION_THREE)]
    if ci >= CI_MILESTONE_ASSERTIVE:
        return ASSERTIVE_BONUS_DICE
    return 0


def anti_church_ob_modifier(ci):
    # [canonical: ci_political_v30 §2.1 milestone 55 — Institutional Reach
    #  threshold-inclusive (ASSUMPTION_THREE); ASSUMPTION_FOUR — caller classifies actions]
    if ci >= CI_MILESTONE_INSTITUTIONAL:
        return INSTITUTIONAL_REACH_OB_PENALTY
    return 0


def secular_anti_church_slot_cost(ci):
    # [canonical: ci_political_v30 §2.1 milestone 65 — Church Dominant
    #  threshold-inclusive (ASSUMPTION_THREE)]
    if ci >= CI_MILESTONE_DOMINANT:
        return DOMINANT_EXTRA_SLOT_COST
    return DOMINANT_BASE_SLOT_COST


def is_ascendant(ci):
    # [canonical: ci_political_v30 §2.1 milestone 80 — Church Ascendant]
    return ci >= CI_MILESTONE_ASCENDANT


def is_unification_active(ci):
    # [canonical: ci_political_v30 §2.2 — Unification at threshold]
    return ci >= CI_MILESTONE_UNIFICATION


# ═══════════════════════════════════════════════════════════════════════════
# UNIFICATION SIMULTANEOUS SEIZURE — target-list generator
# ═══════════════════════════════════════════════════════════════════════════

def mass_seizure_unification_targets(territory_owners, church_mandate,
                                      faction_mandates, registry=None):
    # [canonical: ci_political_v30 §2.2 — Church declares simultaneous seizure
    #  on all territories with Church buildings]
    # [ASSUMPTION_FIVE: target set = territories where (a) Church has a building
    #  (Chapel+) per the M1 has_any_church_building check, AND (b) Church has
    #  Prominence per the §1 definition (controls the territory OR Church Mandate
    #  exceeds the controlling faction's Mandate). Church-controlled territories
    #  are included (re-affirms control during Unification per §2.2).]
    #
    # territory_owners: {tid: faction_name | None}
    # church_mandate: float — Church.L
    # faction_mandates: {faction_name: float} — for Prominence comparison
    # registry: dict of Settlement objects; defaults to M1 SETTLEMENT_REGISTRY
    reg = registry if registry is not None else m1.SETTLEMENT_REGISTRY
    targets = []
    for tid in sorted(m1.PLAYABLE_TERRITORIES):  # [canonical: M1 PLAYABLE_TERRITORIES — inert territories excluded]
        # (a) at least one Church building in this territory?
        settlements = m1.territory_settlements(tid, reg)
        has_building = any(s.has_any_church_building() for s in settlements)
        if not has_building:
            continue
        # (b) Church Prominent?
        owner = territory_owners.get(tid)
        if owner == 'Church':
            prominent = True
        elif owner is None:
            prominent = True  # [canonical: ci_political §1 — no controlling faction means Church Mandate trivially highest]
        else:
            controlling_mandate = faction_mandates.get(owner, 0.0)
            prominent = church_mandate > controlling_mandate
        if prominent:
            targets.append(tid)
    return targets


# ═══════════════════════════════════════════════════════════════════════════
# SEIZURE ACCORD OUTCOME
# ═══════════════════════════════════════════════════════════════════════════

def accord_on_seizure_success(pt_float):
    # [canonical: victory_v30 §3.2 + mc_v15 inline — Accord = max(floor(PT/2)+1, 2),
    #  clamped to [3, 7]]
    raw = max(math.floor(pt_float / 2) + 1, 2)
    return float(max(3, min(7, raw)))  # [canonical: see accord_on_seizure_success formula ledger]


# ═══════════════════════════════════════════════════════════════════════════
# CONVENIENCE — milestone summary for a given CI
# ═══════════════════════════════════════════════════════════════════════════

def active_milestones(ci):
    # [canonical: ci_political_v30 §2.1 milestone table — returns set of active milestone identifiers]
    out = set()
    if ci >= CI_MILESTONE_ASSERTIVE:
        out.add('assertive')
    if ci >= CI_MILESTONE_INSTITUTIONAL:
        out.add('institutional_reach')
    if ci >= CI_MILESTONE_DOMINANT:
        out.add('dominant')
    if ci >= CI_MILESTONE_ASCENDANT:
        out.add('ascendant')
    if ci >= CI_MILESTONE_UNIFICATION:
        out.add('unification')
    return out
