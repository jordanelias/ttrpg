"""
Valoria combat simulator — Session A
=====================================
Round phase machine + Strike, Full Guard, Take a Breath.

Godot-shaped: each phase is a discrete function. The state machine processes
phases in order each round. Designed for direct port to GDScript scene tree.

Canonical sources (every value cited inline or via ledger):
  params/combat.md — Pool Formula, Damage Formula, Initiative, Stamina, Actions
  designs/scene/derived_stats_v30.md sections on Health and Stamina
  designs/scene/combat_v30.md sections on Round Structure, Initiative, Actions

No mechanics outside canon. No 'arena' parameter (sim scaffolding only).
No invented actions. PP-revert in effect (canonical pool/MW/crit restored).
"""
import numpy as np
from dataclasses import dataclass, field
from enum import Enum


# ============================================================
# CANONICAL CONSTANTS — every value cited
# ============================================================

# Pool formula  [canonical: params/combat.md L14 §Pool Formula]
def combat_pool(agi: int, hist: int) -> int:
    """(Agility × 2) + Relevant History + 3, minimum 5."""
    # [canonical: params/combat.md L14 §Pool Formula]
    return max(5, agi * 2 + hist + 3)


# Health derivation  [canonical: derived_stats_v30.md §4.1]
def max_wounds(end: int) -> int:
    """floor(Endurance/2) + 1. No cap."""
    # [canonical: derived_stats_v30.md §4.1 row 'Max Wounds']
    return end // 2 + 1


def wound_interval(end: int) -> int:
    """WI = Endurance + 6."""
    # [canonical: derived_stats_v30.md §4.1 row 'Wound Interval']
    return end + 6


def max_health(end: int) -> int:
    """Health = WI × (MW+1)."""
    # [canonical: derived_stats_v30.md §4.1 row 'Formula']
    return wound_interval(end) * (max_wounds(end) + 1)


# Stamina  [canonical: params/combat.md L177 §Stamina ED-694]
def max_stamina(end: int) -> int:
    """Stamina = Endurance × 5. Range 5-35."""
    # [canonical: params/combat.md L177 §Stamina ED-694; derived_stats §4.2]
    return end * 5


def breath_recovery(end: int, hist: int) -> int:
    """Take a Breath restores (End + History) × 2."""
    # [canonical: derived_stats_v30.md §4.2 row 'Recovery']
    return (end + hist) * 2


# Action costs  [canonical: derived_stats_v30.md §4.2 'Variable action costs']
ACTION_COST = {
    'strike': 5,        # [canonical: derived_stats §4.2 'Standard attack']
    'full_guard': 3,    # [canonical: derived_stats §4.2 'Defensive stance']
    'breath': 0,        # [canonical: derived_stats §4.2 — no cost, recovers]
}

# Wound penalty  [canonical: params/combat.md L21, derived_stats §4.1]
WOUND_PENALTY_PER_WOUND = 1  # -1D per wound, ALL pools
POOL_FLOOR = 5  # [canonical: params/combat.md §Pool Formula 'minimum 5' / ED-203]

# Crit threshold  [canonical: params/combat.md §Damage Formula L90]
CRIT_NET_HITS = 3  # net hits >= 3 doubles weapon modifier

# Out of Breath  [canonical: derived_stats §4.2 row 'Depleted at']
OOB_PENALTY = 2  # -2D all combat rolls at Stamina 0


# ============================================================
# Weapon system — three-axis  [canonical: params/combat.md §Weapon System]
# ============================================================

# Final TN = 7 + reach + weight + type modifiers
# Reach: Short -1, Long +0
# Weight: Light -1, Heavy +0
# Type: Blade +0, Blunt +1

WEAPONS = {
    # [canonical: params/combat.md §Weapon System example table]
    'dagger':       {'tn': 5, 'reach': 'Short', 'weight': 'Light', 'type': 'Blade', 'min_str': 1},  # [canonical: params/combat.md §Weapon System Short Light combinations]
    'arming_sword': {'tn': 6, 'reach': 'Short', 'weight': 'Heavy', 'type': 'Blade', 'min_str': 2},  # [canonical: params/combat.md §Weapon System STR minimum table]
    'spear':        {'tn': 6, 'reach': 'Long',  'weight': 'Light', 'type': 'Blade', 'min_str': 2},  # [canonical: params/combat.md §Weapon System STR minimum]
    'mace':         {'tn': 7, 'reach': 'Short', 'weight': 'Heavy', 'type': 'Blunt', 'min_str': 3},  # [canonical: params/combat.md §Weapon System STR minimum]
    'longsword':    {'tn': 7, 'reach': 'Long',  'weight': 'Heavy', 'type': 'Blade', 'min_str': 3},  # [canonical: params/combat.md §Weapon System Long Heavy STR 3]
    'staff':        {'tn': 7, 'reach': 'Long',  'weight': 'Light', 'type': 'Blunt', 'min_str': 2},  # [canonical: params/combat.md §Weapon System]
    'warhammer':    {'tn': 8, 'reach': 'Long',  'weight': 'Heavy', 'type': 'Blunt', 'min_str': 4},  # [canonical: params/combat.md §Weapon System Long Heavy Blunt STR 4]
    'unarmed':      {'tn': 8, 'reach': 'Short', 'weight': 'Light', 'type': 'Blunt', 'min_str': 1},  # [canonical: params/combat.md §Weapon System Unarmed TN 8]
}

# STR multiplier  [canonical: params/combat.md §Damage Formula L84]
# Canonical examples at STR 4: Dagger=4, Arming sword=8, Mace=6, Warhammer=12.
# Text reads "Light×1, Heavy×2, Blade×1, Blunt×1.5. Heavy Blunt = ×3" but
# the mace=6 example (mult 1.5, not 3) shows that "Heavy Blunt = ×3" applies
# only to LONG Heavy Blunt (warhammer), not Short Heavy Blunt (mace).
# [EDITORIAL: params/combat.md L84 — multiplier text ambiguous, examples authoritative.]
STR_MULT_BY_WEAPON = {
    # [canonical: params/combat.md L85 example values]
    'dagger': 1.0,        # Light Blade
    'arming_sword': 2.0,  # Heavy Blade
    'spear': 1.0,         # Light Blade
    'mace': 1.5,          # Short Heavy Blunt → Blunt mult only (per example)
    'longsword': 2.0,     # Heavy Blade
    'staff': 1.5,         # Light Blunt
    'warhammer': 3.0,     # Long Heavy Blunt → full Heavy×Blunt
    'unarmed': 1.0,       # Light Blunt baseline
}

def str_multiplier(weapon: str) -> float:
    """Per-weapon canonical multiplier.  [canonical: params/combat.md L85 examples]"""
    return STR_MULT_BY_WEAPON[weapon]


# Weapon modifier vs armour  [canonical: params/combat.md §Damage Formula L93]
def weapon_class(weapon: str) -> str:
    """Returns LB/HB/LN/HN class code."""
    # [canonical: params/combat.md §Damage Formula classes]
    w = WEAPONS[weapon]
    weight_code = 'H' if w['weight'] == 'Heavy' else 'L'
    type_code = 'B' if w['type'] == 'Blade' else 'N'
    return weight_code + type_code


WMOD = {
    # [canonical: params/combat.md L93-98 §Damage Formula]
    'LB': {'None': 3, 'Light': 2, 'Medium': 1, 'Heavy': 0},  # [canonical: params/combat.md §Damage Formula Light Blade row]
    'HB': {'None': 6, 'Light': 4, 'Medium': 2, 'Heavy': 0},  # [canonical: params/combat.md §Damage Formula Heavy Blade row]
    'LN': {'None': 3, 'Light': 3, 'Medium': 3, 'Heavy': 3},  # [canonical: params/combat.md §Damage Formula Light Blunt row]
    'HN': {'None': 5, 'Light': 5, 'Medium': 5, 'Heavy': 5},  # [canonical: params/combat.md §Damage Formula Heavy Blunt row]
}


def weapon_mod(weapon: str, armour: str) -> int:
    """Damage modifier from weapon class vs armour tier."""
    return WMOD[weapon_class(weapon)][armour]


# Armour stamina drain  [canonical: params/combat.md §Armour L152]
ARMOUR_STAMINA_MOD = {
    # [canonical: params/combat.md §Armour table]
    'None': 0,
    'Light': 0,
    'Medium': -1,
    'Heavy': -2,
}


# ============================================================
# Dice engine  [canonical: params/core.md §dice engine]
# ============================================================

def roll(rng: np.random.Generator, n: int, tn: int) -> int:
    """
    Roll n d10s vs TN. Return net hits.
    1s subtract a hit. 10s chain (roll again, add if >= TN).
    [canonical: params/core.md §dice engine]
    """
    if n <= 0:
        return 0
    dice = rng.integers(1, 11, size=n)  # [canonical: params/core.md §dice engine d10]
    hits = int(np.sum(dice >= tn))
    hits -= int(np.sum(dice == 1))  # 1s subtract
    # Chain 10s  [canonical: params/core.md §dice engine — chains on 10]
    tens = int(np.sum(dice == 10))
    while tens > 0:
        chain = rng.integers(1, 11, size=tens)  # [canonical: params/core.md §dice engine chain on 10]
        hits += int(np.sum(chain >= tn))
        tens = int(np.sum(chain == 10))
    return max(0, hits)


# ============================================================
# Combatant state  — Godot-shaped (will become Resource in GDScript)
# ============================================================

@dataclass
class Combatant:
    """Single fighter. Maps to Godot CharacterResource."""
    name: str
    agi: int
    str_: int
    end: int
    hist: int
    att: int = 4  # [canonical: params/combat.md PP-239 default median Attunement]
    weapon: str = 'arming_sword'
    armour: str = 'None'
    
    # Mutable state
    health: int = 0
    stamina: int = 0
    wounds: int = 0
    damage_total: int = 0
    out_of_breath: bool = False
    
    def __post_init__(self):
        self.health = max_health(self.end)
        self.stamina = max_stamina(self.end)
    
    @property
    def max_pool(self) -> int:
        """Effective Combat Pool after wound and OOB penalties."""
        # [canonical: params/combat.md L14 + L21 wound -1D + derived_stats §4.2 OOB -2D]
        base = combat_pool(self.agi, self.hist)
        penalty = self.wounds * WOUND_PENALTY_PER_WOUND
        if self.out_of_breath:
            penalty += OOB_PENALTY
        return max(POOL_FLOOR, base - penalty)  # [canonical: PP-203 floor 5]
    
    @property
    def weapon_tn(self) -> int:
        return WEAPONS[self.weapon]['tn']
    
    @property
    def stamina_drain_per_action(self) -> int:
        """Armour adds to drain per action.  [canonical: derived_stats §4.2]"""
        return -ARMOUR_STAMINA_MOD[self.armour]  # +2 for Heavy
    
    def is_incapacitated(self) -> bool:
        """Health reached 0.  [canonical: params/combat.md L132]"""
        return self.health <= 0


# ============================================================
# Round phases — combat_v30.md §2 mapping
# ============================================================

class Phase(Enum):
    """Round phases.  [canonical: combat_v30.md §2 Round Structure]"""
    MOVEMENT = 1       # [canonical: combat_v30.md §2 phase one]
    RANGE = 2          # [canonical: combat_v30.md §2 phase two]
    DECLARATION = 3    # [canonical: combat_v30.md §2 phase three]
    RESOLUTION = 4     # [canonical: combat_v30.md §2 phase four]
    DAMAGE = 5         # [canonical: combat_v30.md §2 phase five]
    TRACKING = 6       # [canonical: combat_v30.md §2 phase six]


# Action priority  [canonical: params/combat.md L194 PP-247]
ACTION_PRIORITY = {
    'strike': 1,
    'full_guard': 99,   # [canonical: combat_v30.md §4 Reactive — sentinel only]
    'breath': 99,       # [canonical: combat_v30.md §4 Reactive — sentinel only]
}


def initiative_holder(a: Combatant, b: Combatant, rng: np.random.Generator,
                       prev_holder: str | None = None) -> str:
    """
    Determine initiative.
    Exchange 1: higher Attunement; tie -> higher Agility; tie -> random.  # [canonical: params/combat.md PP-239]
    Subsequent rounds: transfers to exchange winner (passed as prev_holder).
    [canonical: params/combat.md §Initiative]
    """
    if prev_holder is not None:
        return prev_holder
    if a.att > b.att: return a.name
    if b.att > a.att: return b.name
    if a.agi > b.agi: return a.name
    if b.agi > a.agi: return b.name
    return a.name if rng.integers(0, 2) == 0 else b.name


# Pool split  — Player decides offence/defence allocation
def pool_split_strike(pool: int, offence_fraction: float) -> tuple[int, int]:
    """For Strike: split pool between offence and defence.
    [canonical: combat_v30.md §3 'declare Offence/Defence split']"""
    offence = max(1, int(pool * offence_fraction))
    defence = pool - offence
    return offence, defence


def pool_split_guard(pool: int) -> tuple[int, int]:
    """Full Guard: all to defence.
    [canonical: combat_v30.md Actions section, Full Guard rule]"""
    return 0, pool


# ============================================================
# Action resolution
# ============================================================

def resolve_strike(attacker: Combatant, defender: Combatant,
                    atk_offence: int, def_defence: int,
                    rng: np.random.Generator) -> dict:
    """
    Strike resolution. Attacker rolls offence at their weapon TN;
    defender rolls defence at their weapon TN.
    Damage = net + (STR × multiplier) + weapon_mod_vs_armour.
    Crit at net >= 3 doubles weapon_mod.
    [canonical: params/combat.md §Damage Formula]
    """
    atk_hits = roll(rng, atk_offence, attacker.weapon_tn)
    def_hits = roll(rng, def_defence, defender.weapon_tn)
    net = atk_hits - def_hits
    
    if net <= 0:
        return {'hit': False, 'net': net, 'damage': 0, 'crit': False}
    
    # [canonical: params/combat.md L84 STR multiplier]
    str_dmg = int(attacker.str_ * str_multiplier(attacker.weapon))
    # [canonical: params/combat.md L93 weapon mod vs armour]
    wmod = weapon_mod(attacker.weapon, defender.armour)
    crit = net >= CRIT_NET_HITS
    if crit:
        wmod *= 2  # [canonical: params/combat.md L90 critical doubles weapon mod]
    
    damage = net + str_dmg + wmod
    return {'hit': True, 'net': net, 'damage': damage, 'crit': crit}


def apply_damage(target: Combatant, damage: int) -> None:
    """Apply damage, accrue wounds.
    [canonical: params/combat.md Wounds/Incapacitation, wounds accrue as floor of cumulative_damage divided by WI]"""
    target.health = max(0, target.health - damage)
    target.damage_total += damage
    new_wounds = min(max_wounds(target.end), target.damage_total // wound_interval(target.end))
    target.wounds = new_wounds


# ============================================================
# Round runner
# ============================================================

def run_round(a: Combatant, b: Combatant,
              a_action: str, a_offence_split: float,
              b_action: str, b_offence_split: float,
              prev_init: str | None,
              rng: np.random.Generator) -> dict:
    """
    Execute one complete round through all 6 phases.
    Returns log with damage dealt, init winner, OOB status.
    """
    log = {'round_init': '', 'a_dmg': 0, 'b_dmg': 0, 'a_action': a_action, 'b_action': b_action}
    
    # Phase 1: Movement (Session A: not modeled, no positions)
    # Phase 2: Range (Session A: assume same range)
    
    # Phase 3: Action declarations
    init = initiative_holder(a, b, rng, prev_init)
    log['round_init'] = init
    
    # Determine pool splits based on action
    Pa = a.max_pool
    Pb = b.max_pool
    if a_action == 'full_guard':
        oa, da = pool_split_guard(Pa)
    elif a_action == 'strike':
        oa, da = pool_split_strike(Pa, a_offence_split)
    else:  # breath
        oa, da = 0, 0
    if b_action == 'full_guard':
        ob, db = pool_split_guard(Pb)
    elif b_action == 'strike':
        ob, db = pool_split_strike(Pb, b_offence_split)
    else:
        ob, db = 0, 0
    
    # Phase 4 & 5: Resolution + Damage (Strike priority 1)
    if a_action == 'strike':
        r = resolve_strike(a, b, oa, db, rng)
        if r['hit']:
            apply_damage(b, r['damage'])
            log['a_dmg'] = r['damage']
            log['a_crit'] = r['crit']
    if b_action == 'strike':
        r = resolve_strike(b, a, ob, da, rng)
        if r['hit']:
            apply_damage(a, r['damage'])
            log['b_dmg'] = r['damage']
            log['b_crit'] = r['crit']
    
    # Phase 6: Stamina/wound tracking
    # Stamina costs  [canonical: derived_stats §4.2]
    if a_action == 'strike':
        a.stamina = max(0, a.stamina - (ACTION_COST['strike'] + a.stamina_drain_per_action))
    elif a_action == 'full_guard':
        a.stamina = max(0, a.stamina - (ACTION_COST['full_guard'] + a.stamina_drain_per_action))
    elif a_action == 'breath':
        a.stamina = min(max_stamina(a.end), a.stamina + breath_recovery(a.end, a.hist))
    if b_action == 'strike':
        b.stamina = max(0, b.stamina - (ACTION_COST['strike'] + b.stamina_drain_per_action))
    elif b_action == 'full_guard':
        b.stamina = max(0, b.stamina - (ACTION_COST['full_guard'] + b.stamina_drain_per_action))
    elif b_action == 'breath':
        b.stamina = min(max_stamina(b.end), b.stamina + breath_recovery(b.end, b.hist))
    
    # OOB check
    a.out_of_breath = (a.stamina <= 0)
    b.out_of_breath = (b.stamina <= 0)
    
    # Initiative transfer  [canonical: combat_v30.md §3 'transfers to exchange winner']
    if log['a_dmg'] > log['b_dmg']: log['next_init'] = a.name
    elif log['b_dmg'] > log['a_dmg']: log['next_init'] = b.name
    else: log['next_init'] = init  # stays with current holder (PP-232 tie)
    
    return log
