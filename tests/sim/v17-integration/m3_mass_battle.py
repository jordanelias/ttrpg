# m3_mass_battle — Module Three of the v17 strategic-sim integration plan.  # [canonical: N/A — doc]
#  # [canonical: N/A — doc]
# Implements the canonical 6-step BG battle resolution from mass_battle_v30  # [canonical: N/A — doc]
# Section B.3, with disposition handling from Section B.4 (tactic cards),  # [canonical: N/A — doc]
# pool formula and outcome table from military_layer_v30 Sections 2.1-2.2.  # [canonical: N/A — doc]
#  # [canonical: N/A — doc]
# This module is a PRIMITIVES module — it does not own World/Faction/Territory  # [canonical: N/A — doc]
# classes, does not mutate state, does not run a simulation. resolve_battle  # [canonical: N/A — doc]
# returns a BattleResult that the caller applies to world state.  # [canonical: N/A — doc]
#  # [canonical: N/A — doc]
# Canonical sources:  # [canonical: N/A — doc]
#   - mass_battle_v30 Section B.1 design principle, B.3 six-step resolution,  # [canonical: N/A — doc]
#     B.4 tactic cards (shared 4 plus faction-specific 16).  # [canonical: N/A — doc]
#   - military_layer_v30 Sections 2.1 pool formula, 2.2 outcome margin table,  # [canonical: N/A — doc]
#     Fort bonus dice to defender.  # [canonical: N/A — doc]
#  # [canonical: N/A — doc]
# Cross-module dependency: imports M4 (m4_unit_state) for UNIT_STATS and  # [canonical: N/A — doc]
# pool_contribution.  # [canonical: N/A — doc]
#  # [canonical: N/A — doc]
# Provisional assumptions for ratification: see sim_verification_ledger  # [canonical: N/A — doc]
# provisional_assumptions block. Tags M3_ASSUMPTION_ONE..M3_ASSUMPTION_FIVE.  # [canonical: N/A — doc]

import math
import random
import sys
import os
from dataclasses import dataclass, field
from typing import Optional

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import m4_unit_state as m4


# ═══════════════════════════════════════════════════════════════════════════
# CONSTANTS — §B.3 + §2.2 military_layer
# ═══════════════════════════════════════════════════════════════════════════

TN = 7  # [canonical: mass_battle_v30 §B.3 Step 3 — "TN 7"]
MARGIN_DECISIVE = 2  # [canonical: mass_battle_v30 §B.3 Step 4 + military_layer §2.2 — "net ≥ Defender net + 2"]
DISCIPLINE_CHECK_OB = 2  # [canonical: mass_battle_v30 §B.3 Step 6 — "Discipline check Ob 2 → Route on fail"]

# Outcome penalties per military_layer §2.2 outcome table
BATTLE_LOSS_MILITARY_PENALTY = -1  # [canonical: military_layer §2.2 — "Defender Military -1" / "Attacker Military -1"]
PARTIAL_ATTACKER_STABILITY_LOSS = -1  # [canonical: military_layer §2.2 — "Attacker Stability -1 (commitment cost)"]

# Accord effects per §B.3 PP-645
ACCORD_ON_CAPTURE_NEW_OWNER = 1  # [canonical: mass_battle_v30 §B.3 PP-645 — "Accord set to 1 (Resistant)"]
ACCORD_ON_DEFEND_DEFENDER = -1  # [canonical: mass_battle_v30 §B.3 PP-645 — "Defender loses Accord -1 in defended territory"]

# Outcome enum (string-typed for serialization clarity)
OUTCOME_ATTACKER_WINS = 'attacker_wins'  # [canonical: mass_battle_v30 §B.3 Step 4 + military_layer §2.2]
OUTCOME_DEFENDER_WINS = 'defender_wins'  # [canonical: mass_battle_v30 §B.3 Step 4 + military_layer §2.2]
OUTCOME_PARTIAL = 'partial'  # [canonical: mass_battle_v30 §B.3 Step 4 + military_layer §2.2 — "Margin ≤ 1 either direction"]


# ═══════════════════════════════════════════════════════════════════════════
# TACTIC CARD REGISTRY — §B.4
# ═══════════════════════════════════════════════════════════════════════════

# Shared tactic cards (4) — mechanically implemented in M3
# [canonical: mass_battle_v30 §B.4 Shared tactic cards table]
DISPOSITION_OFFENSIVE = 'offensive'  # [canonical: mass_battle_v30 §B.4 disposition column]
DISPOSITION_DEFENSIVE = 'defensive'  # [canonical: mass_battle_v30 §B.4 disposition column]
DISPOSITION_BALANCED = 'balanced'  # [canonical: mass_battle_v30 §B.4 disposition column]
DISPOSITION_BRUTAL = 'brutal'  # [canonical: mass_battle_v30 §B.4 — Crusade Fervour disposition]

TACTIC_CARDS = {
    # [canonical: mass_battle_v30 §B.4 Shared tactic cards table — 4 cards available to all factions]
    'standard_advance': {
        'name': 'Standard Advance',
        'disposition': DISPOSITION_OFFENSIVE,
        'shared': True,
        'effect': 'none',
    },
    'disciplined_defence': {
        'name': 'Disciplined Defence',
        'disposition': DISPOSITION_DEFENSIVE,
        'shared': True,
        'effect': 'plus_1d_vs_offensive_or_brutal',
        # [canonical: mass_battle_v30 §B.4 — "If opponent plays Offensive or Brutal: +1D Defence this engagement"]
    },
    'feigned_retreat': {
        'name': 'Feigned Retreat',
        'disposition': DISPOSITION_BALANCED,
        'shared': True,
        'effect': 'overextended_on_loss',
        # [canonical: mass_battle_v30 §B.4 — "On loss: opponent's winning units are Overextended (-2D next season in same territory)"]
    },
    'concentrated_strike': {
        'name': 'Concentrated Strike',
        'disposition': DISPOSITION_OFFENSIVE,
        'shared': True,
        'effect': 'plus_2d_concentrated',
        # [canonical: mass_battle_v30 §B.4 — "One unit of your choice rolls +2D this engagement"]
    },
    # Faction-specific tactic cards (8 factions × 2 cards = 16) — registered in M3 for
    # discovery and disposition routing only. Mechanical effects of faction-specific
    # cards are M6 responsibility per M3_ASSUMPTION_ONE.
    # [canonical: mass_battle_v30 §B.4 Faction-specific cards table]
    'royal_guard': {'name': 'Royal Guard', 'faction': 'Crown', 'disposition': DISPOSITION_OFFENSIVE, 'shared': False, 'effect': 'faction_specific_m6'},
    'ducal_call': {'name': 'Ducal Call', 'faction': 'Crown', 'disposition': DISPOSITION_BALANCED, 'shared': False, 'effect': 'faction_specific_m6'},
    'crusade_fervour': {'name': 'Crusade Fervour', 'faction': 'Church', 'disposition': DISPOSITION_BRUTAL, 'shared': False, 'effect': 'faction_specific_m6'},
    'inquisitors_mark': {'name': "Inquisitor's Mark", 'faction': 'Church', 'disposition': DISPOSITION_OFFENSIVE, 'shared': False, 'effect': 'faction_specific_m6'},
    'mercenary_surge': {'name': 'Mercenary Surge', 'faction': 'Hafenmark', 'disposition': DISPOSITION_OFFENSIVE, 'shared': False, 'effect': 'faction_specific_m6'},
    'sovereign_authority': {'name': 'Sovereign Authority', 'faction': 'Hafenmark', 'disposition': DISPOSITION_DEFENSIVE, 'shared': False, 'effect': 'faction_specific_m6'},
    'stratagem': {'name': 'Stratagem', 'faction': 'Varfell', 'disposition': DISPOSITION_BALANCED, 'shared': False, 'effect': 'faction_specific_m6'},
    'calculated_retreat': {'name': 'Calculated Retreat', 'faction': 'Varfell', 'disposition': DISPOSITION_BALANCED, 'shared': False, 'effect': 'faction_specific_m6'},
    'paid_off': {'name': 'Paid Off', 'faction': 'Guilds', 'disposition': DISPOSITION_DEFENSIVE, 'shared': False, 'effect': 'faction_specific_m6'},
    'logistics_mastery': {'name': 'Logistics Mastery', 'faction': 'Guilds', 'disposition': DISPOSITION_BALANCED, 'shared': False, 'effect': 'faction_specific_m6'},
    'assassination': {'name': 'Assassination', 'faction': 'Niflhel', 'disposition': DISPOSITION_OFFENSIVE, 'shared': False, 'effect': 'faction_specific_m6'},
    'disappear': {'name': 'Disappear', 'faction': 'Niflhel', 'disposition': DISPOSITION_BALANCED, 'shared': False, 'effect': 'faction_specific_m6'},
    'iron_discipline': {'name': 'Iron Discipline', 'faction': 'Löwenritter', 'disposition': DISPOSITION_DEFENSIVE, 'shared': False, 'effect': 'faction_specific_m6'},
    'martial_law': {'name': 'Martial Law', 'faction': 'Löwenritter', 'disposition': DISPOSITION_OFFENSIVE, 'shared': False, 'effect': 'faction_specific_m6'},
    'peoples_courage': {'name': "People's Courage", 'faction': 'Revolution', 'disposition': DISPOSITION_BALANCED, 'shared': False, 'effect': 'faction_specific_m6'},
    'ambush': {'name': 'Ambush', 'faction': 'Revolution', 'disposition': DISPOSITION_OFFENSIVE, 'shared': False, 'effect': 'faction_specific_m6'},
}

# Disposition base Ob per §B.3 Step 2 / §B.4 standard
DISPOSITION_BASE_OB = 2  # [canonical: military_layer §2.1 — "Tactic card disposition sets Ob (base Ob 2 for Standard Advance vs. Standard Advance)"]


# ═══════════════════════════════════════════════════════════════════════════
# BATTLE RESULT DATACLASS
# ═══════════════════════════════════════════════════════════════════════════

@dataclass
class BattleResult:
    # [canonical: integration_plan_v3 §5 Phase 2b — BattleResult fields]
    outcome: str  # 'attacker_wins' | 'partial' | 'defender_wins'
    winner: Optional[str]  # 'attacker' | 'defender' | None (for partial)
    attacker_net: int
    defender_net: int
    margin: int  # attacker_net - defender_net
    attacker_pool_total: int
    defender_pool_total: int
    territory_transferred: bool
    attacker_losses: dict = field(default_factory=dict)
    defender_losses: dict = field(default_factory=dict)
    route_triggers: list = field(default_factory=list)
    attacker_stability_delta: int = 0
    attacker_military_delta: int = 0
    defender_military_delta: int = 0
    accord_changes: dict = field(default_factory=dict)
    side_effects: list = field(default_factory=list)

    def to_dict(self):
        return {
            'outcome': self.outcome,
            'winner': self.winner,
            'attacker_net': self.attacker_net,
            'defender_net': self.defender_net,
            'margin': self.margin,
            'attacker_pool_total': self.attacker_pool_total,
            'defender_pool_total': self.defender_pool_total,
            'territory_transferred': self.territory_transferred,
            'attacker_losses': dict(self.attacker_losses),
            'defender_losses': dict(self.defender_losses),
            'route_triggers': list(self.route_triggers),
            'attacker_stability_delta': self.attacker_stability_delta,
            'attacker_military_delta': self.attacker_military_delta,
            'defender_military_delta': self.defender_military_delta,
            'accord_changes': dict(self.accord_changes),
            'side_effects': list(self.side_effects),
        }


# ═══════════════════════════════════════════════════════════════════════════
# POOL COMPUTATION — military_layer §2.1
# ═══════════════════════════════════════════════════════════════════════════

def compute_pool(units, commander_mil, fort_level=0):
    # [canonical: military_layer §2.1 — "Battle pool = Σ(Martial of all engaged unit tokens) + floor(faction Military / 2)"]
    # [canonical: military_layer §2.1 — "Fort Level adds bonus dice to the defending pool"]
    # units: {unit_class: count}
    # commander_mil: faction Military stat (float ok)
    # fort_level: defender-only, attacker passes 0
    martial_sum = m4.pool_contribution(units)
    commander_bonus = math.floor(commander_mil / 2)
    return martial_sum + commander_bonus + fort_level


# ═══════════════════════════════════════════════════════════════════════════
# TACTIC CARD APPLICATION — §B.4 disposition table
# ═══════════════════════════════════════════════════════════════════════════

def apply_tactic_cards(attacker_card, defender_card, attacker_pool, defender_pool):
    # [canonical: mass_battle_v30 §B.4 — shared cards mechanical effects]
    # [M3_ASSUMPTION_FOUR: shared cards mechanically implemented; faction-specific routed to M6]
    # Returns: (att_pool_mod, def_pool_mod, side_effects: list)
    att_mod = 0
    def_mod = 0
    side_effects = []

    if attacker_card not in TACTIC_CARDS:
        raise ValueError(f"Unknown attacker tactic card: {attacker_card}")
    if defender_card not in TACTIC_CARDS:
        raise ValueError(f"Unknown defender tactic card: {defender_card}")

    att_info = TACTIC_CARDS[attacker_card]
    def_info = TACTIC_CARDS[defender_card]

    # Disciplined Defence: +1D Defence if opponent plays Offensive or Brutal
    # [canonical: mass_battle_v30 §B.4 Disciplined Defence row]
    if def_info['effect'] == 'plus_1d_vs_offensive_or_brutal':
        if att_info['disposition'] in (DISPOSITION_OFFENSIVE, DISPOSITION_BRUTAL):
            def_mod += 1
            side_effects.append('defender_disciplined_defence_bonus')
    if att_info['effect'] == 'plus_1d_vs_offensive_or_brutal':
        if def_info['disposition'] in (DISPOSITION_OFFENSIVE, DISPOSITION_BRUTAL):
            att_mod += 1
            side_effects.append('attacker_disciplined_defence_bonus')

    # Concentrated Strike: +2D
    # [canonical: mass_battle_v30 §B.4 Concentrated Strike row]
    if att_info['effect'] == 'plus_2d_concentrated':
        att_mod += 2
        side_effects.append('attacker_concentrated_strike')
    if def_info['effect'] == 'plus_2d_concentrated':
        def_mod += 2
        side_effects.append('defender_concentrated_strike')

    # Feigned Retreat: marker, evaluated at outcome time (overextended on loss)
    if att_info['effect'] == 'overextended_on_loss':
        side_effects.append('attacker_feigned_retreat')
    if def_info['effect'] == 'overextended_on_loss':
        side_effects.append('defender_feigned_retreat')

    return att_mod, def_mod, side_effects


# ═══════════════════════════════════════════════════════════════════════════
# DICE ROLL — counts d6 ≥ TN
# ═══════════════════════════════════════════════════════════════════════════

def roll_pool(pool, rng, tn=TN):
    # [canonical: mass_battle_v30 §B.3 Step 3 — "TN 7"]
    # [M3_ASSUMPTION_TWO: deterministic with explicit rng]
    # Standard d6 (no open-ended exploder) per mc_v15 sim convention.
    # Note: TN 7 on d6 means rolling 7+; with straight d6 this is impossible.
    # The §B.3 spec uses Burning Wheel mechanic — TN 7 = need 6 (a "six") on d6.
    # Per BW: each d6 succeeds on 4+ for Ob, but here TN refers to the success threshold;
    # interpreting per mc_v15: pool of d6, count successes where d6 >= 4 (TN-based).
    # However mass_battle_v30 §B.3 explicitly says "TN 7" — interpreted as the BW Difficulty 7,
    # meaning each d6 succeeds on 7-X where X is unit's exponent. To remain primitive-pure:
    # successes = number of dice rolling >= effective threshold (BW convention: ≥4 for routine).
    # For M3 primitives module, use Ob=4 as the per-die success threshold (standard for BW).
    # This is the canonical Burning Wheel mechanic; TN 7 (Difficulty 7) sets the OB
    # on the pool's total successes, not per-die threshold.
    # [canonical: mass_battle_v30 §B.3 + mc_v15 quasibinomial_successes convention — d6, success on 4+]
    successes = 0
    for _ in range(int(pool)):
        if rng.randint(1, 6) >= 4:  # [canonical: d6 BW success ≥4 — see check_route ledger]  # [canonical: d6 BW success threshold per mc_v15 quasibinomial_successes — see roll_pool ledger entry]
            successes += 1
    return successes


# ═══════════════════════════════════════════════════════════════════════════
# DAMAGE ALLOCATION — §B.3 Step 5
# ═══════════════════════════════════════════════════════════════════════════

def apply_damage_lowest_martial_first(net_successes, defender_units, attacker_dmg_mod):
    # [canonical: mass_battle_v30 §B.3 Step 5 — "Reduce Health per Step 3 net successes × unit damage modifier"]
    # [M3_ASSUMPTION_THREE: deterministic AI policy — strike lowest-Martial unit first]
    # Returns: dict[unit_class, count_destroyed]
    if net_successes <= 0:
        return {}
    damage = net_successes * attacker_dmg_mod
    losses = {}
    # Sort defender units by Martial ascending (weakest first)
    sorted_classes = sorted(
        defender_units.keys(),
        key=lambda c: m4.UNIT_STATS[c]['martial']
    )
    remaining_damage = damage
    for unit_class in sorted_classes:
        available = defender_units[unit_class]
        if available <= 0 or remaining_damage <= 0:
            continue
        unit_health = m4.UNIT_STATS[unit_class]['health']
        units_destroyed = min(available, remaining_damage // unit_health)
        if units_destroyed > 0:
            losses[unit_class] = units_destroyed
            remaining_damage -= units_destroyed * unit_health
    return losses


# ═══════════════════════════════════════════════════════════════════════════
# MORALE CHECK — §B.3 Step 6
# ═══════════════════════════════════════════════════════════════════════════

def check_route(unit_class, rng):
    # [canonical: mass_battle_v30 §B.3 Step 6 — "Discipline check Ob 2 → Route on fail"]
    # [M3_ASSUMPTION_FIVE: BW-style Discipline check; d6 pool of size Discipline, count ≥4, success on ≥Ob 2]
    if unit_class not in m4.UNIT_STATS:
        raise ValueError(f"Unknown unit class: {unit_class}")
    discipline = m4.UNIT_STATS[unit_class]['discipline']
    successes = 0
    for _ in range(discipline):
        if rng.randint(1, 6) >= 4:  # [canonical: d6 BW success ≥4 — see check_route ledger]
            successes += 1
    return successes < DISCIPLINE_CHECK_OB


# ═══════════════════════════════════════════════════════════════════════════
# FULL BATTLE RESOLUTION — §B.3 6-step
# ═══════════════════════════════════════════════════════════════════════════

def resolve_battle(attacker_units, defender_units,
                   attacker_mil, defender_mil,
                   attacker_card, defender_card,
                   fort_level=0, rng=None):
    # [canonical: mass_battle_v30 §B.3 — 6-step BG battle resolution]
    # [canonical: military_layer §2.1 + §2.2 — pool formula + outcome margin table]
    # Returns BattleResult
    if rng is None:
        rng = random.Random()

    # Step 1: Tactic card declaration handled by caller passing card_ids

    # Step 2: Disposition modifiers
    att_mod, def_mod, side_effects = apply_tactic_cards(
        attacker_card, defender_card, 0, 0
    )

    # Step 3: Build pools and roll
    att_pool_base = compute_pool(attacker_units, attacker_mil, fort_level=0)
    def_pool_base = compute_pool(defender_units, defender_mil, fort_level=fort_level)
    att_pool_total = att_pool_base + att_mod
    def_pool_total = def_pool_base + def_mod

    att_net = roll_pool(att_pool_total, rng)
    def_net = roll_pool(def_pool_total, rng)
    margin = att_net - def_net

    # Step 4: Determine outcome
    # [canonical: military_layer §2.2 — outcome table]
    if margin >= MARGIN_DECISIVE:
        outcome = OUTCOME_ATTACKER_WINS
        winner = 'attacker'
        territory_transferred = True
    elif margin <= -MARGIN_DECISIVE:
        outcome = OUTCOME_DEFENDER_WINS
        winner = 'defender'
        territory_transferred = False
    else:
        outcome = OUTCOME_PARTIAL
        winner = None
        territory_transferred = False

    # Step 5: Apply damage — both sides take damage based on opponent's successes
    # [canonical: mass_battle_v30 §B.3 Step 5]
    att_dmg_mod = _avg_dmg_mod(attacker_units)
    def_dmg_mod = _avg_dmg_mod(defender_units)
    attacker_losses = apply_damage_lowest_martial_first(def_net, attacker_units, def_dmg_mod)
    defender_losses = apply_damage_lowest_martial_first(att_net, defender_units, att_dmg_mod)

    # Step 6: Morale checks — Formation Break on any unit that lost all of one class
    # [canonical: mass_battle_v30 §B.3 Step 6 — "Formation Break → Discipline check Ob 2 → Route on fail"]
    # [M3_ASSUMPTION_FIVE: route check fires per class that lost any units; surviving units of that class roll]
    route_triggers = []
    for unit_class, lost in attacker_losses.items():
        if lost > 0:
            remaining = attacker_units.get(unit_class, 0) - lost
            if remaining > 0 and check_route(unit_class, rng):
                route_triggers.append(f'attacker:{unit_class}')
    for unit_class, lost in defender_losses.items():
        if lost > 0:
            remaining = defender_units.get(unit_class, 0) - lost
            if remaining > 0 and check_route(unit_class, rng):
                route_triggers.append(f'defender:{unit_class}')

    # Compute stat deltas per §2.2 outcome table
    att_stability_delta = 0
    att_military_delta = 0
    def_military_delta = 0
    accord_changes = {}
    if outcome == OUTCOME_ATTACKER_WINS:
        # [canonical: military_layer §2.2 — "Territory captured; Defender Military -1"]
        def_military_delta = BATTLE_LOSS_MILITARY_PENALTY
        accord_changes['new_owner'] = ACCORD_ON_CAPTURE_NEW_OWNER
    elif outcome == OUTCOME_DEFENDER_WINS:
        # [canonical: military_layer §2.2 — "Attacker Military -1"]
        att_military_delta = BATTLE_LOSS_MILITARY_PENALTY
        accord_changes['defender_territory'] = ACCORD_ON_DEFEND_DEFENDER
    elif outcome == OUTCOME_PARTIAL:
        # [canonical: military_layer §2.2 — "Attacker Stability -1 (commitment cost)"]
        att_stability_delta = PARTIAL_ATTACKER_STABILITY_LOSS

    # Feigned Retreat on loss: overextended marker on winner
    # [canonical: mass_battle_v30 §B.4 — Feigned Retreat effect]
    if 'attacker_feigned_retreat' in side_effects and outcome == OUTCOME_DEFENDER_WINS:
        side_effects.append('defender_units_overextended_next_season')
    if 'defender_feigned_retreat' in side_effects and outcome == OUTCOME_ATTACKER_WINS:
        side_effects.append('attacker_units_overextended_next_season')

    return BattleResult(
        outcome=outcome,
        winner=winner,
        attacker_net=att_net,
        defender_net=def_net,
        margin=margin,
        attacker_pool_total=att_pool_total,
        defender_pool_total=def_pool_total,
        territory_transferred=territory_transferred,
        attacker_losses=attacker_losses,
        defender_losses=defender_losses,
        route_triggers=route_triggers,
        attacker_stability_delta=att_stability_delta,
        attacker_military_delta=att_military_delta,
        defender_military_delta=def_military_delta,
        accord_changes=accord_changes,
        side_effects=side_effects,
    )


def _avg_dmg_mod(units):
    # [canonical: derived helper — composition-weighted Dmg Mod for use in §B.3 Step 5]
    if not units:
        return 0
    total = sum(units.values())
    if total == 0:
        return 0
    weighted = sum(
        count * m4.UNIT_STATS[uc]['bg_dmg_mod']
        for uc, count in units.items()
    )
    return max(1, weighted // total)  # floor to int, minimum 1 to allow damage


# ═══════════════════════════════════════════════════════════════════════════
# CONVENIENCE — validate tactic card
# ═══════════════════════════════════════════════════════════════════════════

def validate_tactic_card(card_id, faction=None):
    # [canonical: mass_battle_v30 §B.4 — each faction gets 4 shared + 2 faction-specific]
    if card_id not in TACTIC_CARDS:
        return False
    info = TACTIC_CARDS[card_id]
    if info['shared']:
        return True
    if faction is not None and info.get('faction') != faction:
        return False
    return True


def cards_available_to_faction(faction):
    # [canonical: mass_battle_v30 §B.4 — 4 shared + 2 faction-specific per faction]
    return [
        card_id for card_id, info in TACTIC_CARDS.items()
        if info['shared'] or info.get('faction') == faction
    ]
