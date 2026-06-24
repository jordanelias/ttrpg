"""
sim/personal/combat.py — Personal combat resolution

[DEPRECATED 2026-06-23 — superseded by combat_engine_v1 (ED-900/904; docket ED-1029).]
This module implements the v30 model (Combat Pool = Agility×2 + History + 3; TN-7 weapon matrix;
MULTIPLICATIVE STR damage). The CANONICAL personal-combat resolver is designs/scene/combat_engine_v1/
(sigma-leverage d_sigma resolution; pool = max(5, History+6); additive-coupled damage ×1.55; ED-1041
bilateral-Ob wounds). The Godot port lives at designs/godot/skeleton/engines/combat/ + the
references/module_contracts.yaml personal_combat entry. Retained for reference/history only — do NOT
wire new game code through this file. (Surfaced by the 2026-06-22 personal-combat audit; see also
mechanics_index.yaml, now repointed to the canonical engine.)

Canon source: designs/scene/combat_v30.md §1-§7  [DEPRECATED — see banner above]

Implements personal-scale combat resolution: Combat Pool (§1), round
structure (§2), action resolution per priority order (§4), weapon TN
matrix (§5 PP-232), damage formula (§5 PP-232).

Per Tier 1 scope: single-action resolution + round skeleton. Multi-action
choreography (Feint→Strike chain, Rescue interception, Tie Up consequences)
is Tier 2+ — bounded here to Strike, Full Guard, Dodge, Establish Distance,
Take a Breath as core action set.

[ASSUMPTION: actor object is duck-typed — basis: World has no character
 schema yet. Caller supplies CombatActor with .actor_id, .agility,
 .strength, .endurance, .history, .wounds, .stamina_out_of_breath,
 .weapon (dict with str/heavy/light/blade/blunt/reach attrs).]

Dependencies:
  - sim/autoload/dice_engine
  - sim/cross_scale/handoff_rules (Mass → Personal General Duel per §3.7)

Entry points:
  - resolve_combat_round(participants, scene) -> RoundResult
  - resolve_action(actor, target, action_type, scene=None) -> ActionResult
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from sim.autoload.dice_engine import roll_pool


# §1 Combat Pool formula constants
# [canonical: combat_v30 §1 — "Combat Pool = (Agility × 2) + Relevant History + 3 (minimum 5)"]
COMBAT_POOL_MIN = 5
COMBAT_POOL_HISTORY_CONSTANT = 3

# §1 Pool modifiers
WOUND_PENALTY_PER = -1                  # "Wounds: -1D per wound (cumulative)"
OUT_OF_BREATH_PENALTY = -2              # "Stamina Out of Breath: -2D to all rolls"

# §5 Weapon TN matrix base
# [canonical: §5 — "Weapons are defined by three binary axes. Base TN = 7."]
WEAPON_TN_BASE = 7
WEAPON_TN_MOD = {
    'reach_short': -1, 'reach_long': 0,
    'weight_light': -1, 'weight_heavy': 0,
    'type_blade': 0, 'type_blunt': +1,
}

# §5 Damage formula constants (PP-232)
# [canonical: §5 — "STR multiplier: Light×1, Heavy×2, Blade×1, Blunt×1.5. Multiplicative (Heavy Blunt=×3)"]
STR_MULT_LIGHT = 1.0
STR_MULT_HEAVY = 2.0
STR_MULT_BLADE = 1.0
STR_MULT_BLUNT = 1.5

# Critical hit threshold (PP-211)
# [canonical: §5 — "Critical Hit: net hits ≥ 3 → weapon modifier doubled"]
CRIT_NET_HITS_THRESHOLD = 3

# §5 Weapon modifier vs armour tier
# [canonical: §5 Weapon modifier vs armour tier table]
WEAPON_MOD_VS_ARMOR = {
    ('Light Blade', 'None'):   +3, ('Light Blade', 'Light'):  +2,
    ('Light Blade', 'Medium'): +1, ('Light Blade', 'Heavy'):  +0,
    ('Heavy Blade', 'None'):   +6, ('Heavy Blade', 'Light'):  +4,
    ('Heavy Blade', 'Medium'): +2, ('Heavy Blade', 'Heavy'):  +0,
    ('Light Blunt', 'None'):   +3, ('Light Blunt', 'Light'):  +3,
    ('Light Blunt', 'Medium'): +3, ('Light Blunt', 'Heavy'):  +3,
    ('Heavy Blunt', 'None'):   +5, ('Heavy Blunt', 'Light'):  +5,
    ('Heavy Blunt', 'Medium'): +5, ('Heavy Blunt', 'Heavy'):  +5,
}

# §4 Action resolution order (PP-247)
# [canonical: §4 Action resolution order table]
ACTION_RESOLUTION_ORDER = {
    'Strike': 1, 'Feint': 2,
    'Disarm': 3, 'Tie Up': 3, 'Retrieve': 3,
    'Establish Distance': 4, 'Escape': 4,
    'Leap': 5,
    # Reactive — resolve when trigger fires
    'Full Guard': 99, 'Take a Breath': 99, 'Dodge': 99, 'Rescue': 99,
}


@dataclass
class ActionResult:
    """Result of a single combat action resolution."""
    actor_id: str
    action_type: str
    target_id: Optional[str]
    success: bool
    net_hits: int
    damage_dealt: int
    degree: str               # 'Overwhelming' / 'Success' / 'Partial' / 'Failure'
    notes: list[str] = field(default_factory=list)


@dataclass
class RoundResult:
    """Result of a complete combat round."""
    round_number: int
    actions: list[ActionResult]
    incapacitated: list[str]    # actor_ids that hit Stage 1 this round


def _combat_pool(actor) -> int:
    """§1 Combat Pool = (Agi × 2) + History + 3 (min 5), modified by wounds + Out of Breath."""
    agi = getattr(actor, 'agility', 3)
    history = getattr(actor, 'history', 0)
    wounds = getattr(actor, 'wounds', 0)
    out_of_breath = getattr(actor, 'stamina_out_of_breath', False)

    pool = (agi * 2) + history + COMBAT_POOL_HISTORY_CONSTANT
    pool = max(COMBAT_POOL_MIN, pool)
    pool += wounds * WOUND_PENALTY_PER
    if out_of_breath:
        pool += OUT_OF_BREATH_PENALTY
    return max(1, pool)


def _weapon_tn(weapon: dict) -> int:
    """§5 Weapon TN from 3 binary axes."""
    tn = WEAPON_TN_BASE
    if weapon.get('reach') == 'short':
        tn += WEAPON_TN_MOD['reach_short']
    if weapon.get('weight') == 'light':
        tn += WEAPON_TN_MOD['weight_light']
    if weapon.get('type') == 'blunt':
        tn += WEAPON_TN_MOD['type_blunt']
    return tn


def _weapon_class(weapon: dict) -> str:
    """Map weapon to a string class for damage lookup."""
    weight = 'Heavy' if weapon.get('weight') == 'heavy' else 'Light'
    type_ = 'Blunt' if weapon.get('type') == 'blunt' else 'Blade'
    return f"{weight} {type_}"


def _str_multiplier(weapon: dict) -> float:
    """§5 STR multiplier: Light×1, Heavy×2, Blade×1, Blunt×1.5. Multiplicative."""
    wm = STR_MULT_HEAVY if weapon.get('weight') == 'heavy' else STR_MULT_LIGHT
    tm = STR_MULT_BLUNT if weapon.get('type') == 'blunt' else STR_MULT_BLADE
    return wm * tm


def _degree(net: int) -> str:
    """§5 Degree Table."""
    if net <= 0:
        return "Failure"
    if net == 1:
        return "Partial"
    if net >= 3:
        return "Overwhelming"
    return "Success"


def _damage(net_hits: int, actor, weapon: dict, target_armor: str = 'None') -> int:
    """§5 Damage = net_hits + (STR × mult) + weapon_mod_vs_armor.

    Critical hit (net ≥ 3): weapon modifier doubled before armour reduction.
    """
    if net_hits <= 0:
        return 0
    str_score = getattr(actor, 'strength', 3)
    str_mult = _str_multiplier(weapon)
    weapon_class = _weapon_class(weapon)
    weapon_mod = WEAPON_MOD_VS_ARMOR.get((weapon_class, target_armor), 0)
    if net_hits >= CRIT_NET_HITS_THRESHOLD:
        # [canonical: §5 PP-211 Critical Hit — "weapon modifier doubled"]
        weapon_mod *= 2
    return int(net_hits + (str_score * str_mult) + weapon_mod)


def resolve_action(actor, target, action_type: str, scene=None, rng=None) -> ActionResult:
    """Resolve a single combat action.

    Implemented action types: Strike, Full Guard, Dodge, Establish Distance,
    Take a Breath. Others return Failure with explanatory note (Tier 2+).
    """
    actor_id = getattr(actor, 'actor_id', getattr(actor, 'name', 'unknown'))
    target_id = getattr(target, 'actor_id', getattr(target, 'name', 'unknown')) if target else None

    rng = rng if rng is not None else (scene.rng if scene and hasattr(scene, 'rng') else None)
    if rng is None:
        import random
        rng = random.Random()

    if action_type == 'Strike':
        pool = _combat_pool(actor)
        weapon = getattr(actor, 'weapon', {'reach': 'short', 'weight': 'light', 'type': 'blade'})
        tn = _weapon_tn(weapon)
        # Offence pool — for simple round, allocate full pool to offence (caller
        # supplies the split for advanced Feint/Tie Up etc).
        offense_pool = getattr(actor, 'offense_dice', pool)
        defense_pool_target = getattr(target, 'defense_dice', _combat_pool(target) if target else 0)

        off_roll = roll_pool(offense_pool, tn=tn, rng=rng).net if offense_pool > 0 else 0
        def_tn = _weapon_tn(getattr(target, 'weapon', {})) if target else 7
        def_roll = roll_pool(defense_pool_target, tn=def_tn, rng=rng).net if defense_pool_target > 0 else 0

        net_hits = max(0, off_roll - def_roll)
        target_armor = getattr(target, 'armor_tier', 'None')
        damage = _damage(net_hits, actor, weapon, target_armor)
        degree = _degree(net_hits)

        return ActionResult(
            actor_id=actor_id, action_type='Strike', target_id=target_id,
            success=(net_hits > 0), net_hits=net_hits,
            damage_dealt=damage, degree=degree,
            notes=[f"weapon TN {tn}; offense {off_roll} vs defense {def_roll}; net {net_hits}; armor {target_armor}"]
        )

    if action_type == 'Full Guard':
        return ActionResult(
            actor_id=actor_id, action_type='Full Guard', target_id=None,
            success=True, net_hits=0, damage_dealt=0, degree='Success',
            notes=["All Combat Pool dice to Defence per §4"]
        )

    if action_type == 'Take a Breath':
        # Recovers Stamina by Endurance score per §4
        end = getattr(actor, 'endurance', 3)
        return ActionResult(
            actor_id=actor_id, action_type='Take a Breath', target_id=None,
            success=True, net_hits=0, damage_dealt=0, degree='Success',
            notes=[f"Recovered {end} Stamina; cannot be in immediate melee contact (§4)"]
        )

    if action_type == 'Dodge':
        # Ranged-only; forfeit offence
        return ActionResult(
            actor_id=actor_id, action_type='Dodge', target_id=None,
            success=True, net_hits=0, damage_dealt=0, degree='Success',
            notes=["Ranged-attack-only; full pool to passive Defence (§4 PP-215)"]
        )

    if action_type == 'Establish Distance':
        # Contested Agility if opposed; for Tier 1 single-action we resolve unopposed
        return ActionResult(
            actor_id=actor_id, action_type='Establish Distance', target_id=target_id,
            success=True, net_hits=0, damage_dealt=0, degree='Success',
            notes=["Move to preferred range (§4)"]
        )

    # Action not implemented this tier
    return ActionResult(
        actor_id=actor_id, action_type=action_type, target_id=target_id,
        success=False, net_hits=0, damage_dealt=0, degree='Failure',
        notes=[f"Action '{action_type}' not implemented at Tier 1; deferred to Tier 2+"],
    )


def resolve_combat_round(participants: list, scene=None, rng=None) -> RoundResult:
    """Resolve one round of combat per §2 priority order + §4 resolution.

    Each participant must have a declared action (participant.declared_action)
    and optional target (participant.declared_target). Resolved in §4
    resolution-order; reactive actions resolve at end-of-round.
    """
    round_num = getattr(scene, 'round_number', 1) if scene else 1
    actions: list[ActionResult] = []

    # Sort by §4 resolution order
    ordered = sorted(participants,
                     key=lambda p: ACTION_RESOLUTION_ORDER.get(
                         getattr(p, 'declared_action', 'Strike'), 99))

    incapacitated = []
    for p in ordered:
        # Skip if already incapacitated this round
        if getattr(p, 'actor_id', 'unknown') in incapacitated:
            continue
        action = getattr(p, 'declared_action', 'Strike')
        target = getattr(p, 'declared_target', None)
        # Skip target if target was incapacitated this round
        if target and getattr(target, 'actor_id', None) in incapacitated:
            continue
        result = resolve_action(p, target, action, scene=scene, rng=rng)
        actions.append(result)
        # Track damage on target — if damage_dealt brings target to 0 wounds, mark incap
        if result.damage_dealt > 0 and target is not None:
            current_wounds = getattr(target, 'wounds', 0)
            # Simple wound mapping — each damage increment = 1 wound for Tier 1
            new_wounds = current_wounds + 1
            target.wounds = new_wounds
            max_wounds = getattr(target, 'max_wounds', 3)
            if new_wounds >= max_wounds:
                incapacitated.append(getattr(target, 'actor_id', 'unknown'))

    return RoundResult(round_number=round_num, actions=actions, incapacitated=incapacitated)
