# m7_resolution_hooks — Resolution-time hook implementations for the 6  # [canonical: N/A — doc]
# faction-specific tactic cards deferred from M3/M6.  # [canonical: N/A — doc]
#  # [canonical: N/A — doc]
# Each hook wraps a phase of M3's resolve_battle to apply faction-specific  # [canonical: N/A — doc]
# semantics that the primitives layer cannot express:  # [canonical: N/A — doc]
#  # [canonical: N/A — doc]
#   1. Stratagem (Varfell) — 2-pass init inversion: read opposing card,  # [canonical: N/A — doc]
#      allow revision of own card, then resolve normally.  # [canonical: N/A — doc]
#   2. Crusade Fervour (Church) — Discipline-check-exempt: suppress route  # [canonical: N/A — doc]
#      checks for the Church side this engagement (acts as Brutal disposition).  # [canonical: N/A — doc]
#   3. Inquisitor's Mark (Church) — per-unit -2D targeting: subtract 2 from  # [canonical: N/A — doc]
#      opponent pool (aggregate-count approximation of per-unit targeting).  # [canonical: N/A — doc]
#   4. Calculated Retreat (Varfell) — withdraw without Overextended: outcome  # [canonical: N/A — doc]
#      override to withdrawal_no_penalty state.  # [canonical: N/A — doc]
#   5. Disappear (Niflhel) — withdraw all units; opponent cannot pursue: same  # [canonical: N/A — doc]
#      as Calculated Retreat plus pursuit_blocked flag.  # [canonical: N/A — doc]
#   6. Ducal Call (Crown) — summon 1 unit from adjacent territory before  # [canonical: N/A — doc]
#      resolution; pre-resolution state mutation on UnitRoster.  # [canonical: N/A — doc]
#  # [canonical: N/A — doc]
# Architecture: ResolutionContext dataclass wraps M3's resolve_battle inputs +  # [canonical: N/A — doc]
# intermediate state. Each hook is a function (context) -> patched context.  # [canonical: N/A — doc]
# Hooks fire in known order:  # [canonical: N/A — doc]
#   pre_tactic_resolution:  stratagem  # [canonical: N/A — doc]
#   pre_pool_compute:       ducal_call  # [canonical: N/A — doc]
#   pre_roll:               inquisitors_mark  # [canonical: N/A — doc]
#   post_outcome:           calculated_retreat, disappear, crusade_fervour  # [canonical: N/A — doc]
#  # [canonical: N/A — doc]
# Canonical sources:  # [canonical: N/A — doc]
#   - mass_battle_v30 §B.4 Faction-specific tactic cards table (effect column)  # [canonical: N/A — doc]
#   - M6 TACTIC_CARDS_REQUIRING_HOOKS frozenset (architectural deferral list)  # [canonical: N/A — doc]
#  # [canonical: N/A — doc]
# Provisional assumptions: see sim_verification_ledger.  # [canonical: N/A — doc]
# Tags M7_ASSUMPTION_ONE..M7_ASSUMPTION_FIVE.  # [canonical: N/A — doc]

import sys
import os
import random
from dataclasses import dataclass, field
from typing import Optional, Callable

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import m3_mass_battle as m3
import m4_unit_state as m4
import m6_faction_actions as m6


# ═══════════════════════════════════════════════════════════════════════════
# RESOLUTION CONTEXT
# ═══════════════════════════════════════════════════════════════════════════

@dataclass
class ResolutionContext:
    # [canonical: M7_ASSUMPTION_ONE — wraps M3 resolve_battle inputs + intermediate state for hooks]
    attacker_faction: str
    defender_faction: str
    attacker_units: dict      # {unit_class: count}
    defender_units: dict
    attacker_mil: float
    defender_mil: float
    attacker_card: str
    defender_card: str
    fort_level: int = 0
    rng: Optional[random.Random] = None
    # Phase-specific mutable state:
    attacker_pool_delta: int = 0          # set by ducal_call, inquisitors_mark
    defender_pool_delta: int = 0
    suppress_route_for_attacker: bool = False  # set by crusade_fervour
    suppress_route_for_defender: bool = False
    pursuit_blocked: bool = False         # set by disappear
    withdrawal_no_penalty: bool = False   # set by calculated_retreat / disappear
    # Stratagem state:
    stratagem_used: bool = False
    # Logging:
    hooks_fired: list = field(default_factory=list)

    def __post_init__(self):
        if self.rng is None:
            self.rng = random.Random()


@dataclass
class HookedBattleResult:
    # [canonical: extends M3.BattleResult with hook-specific outcome flags]
    base_result: m3.BattleResult
    pursuit_blocked: bool = False
    withdrawal_no_penalty: bool = False
    hooks_fired: list = field(default_factory=list)

    def to_dict(self):
        d = self.base_result.to_dict()
        d['pursuit_blocked'] = self.pursuit_blocked
        d['withdrawal_no_penalty'] = self.withdrawal_no_penalty
        d['hooks_fired'] = list(self.hooks_fired)
        return d


# ═══════════════════════════════════════════════════════════════════════════
# HOOK 1 — STRATAGEM (Varfell) — pre_tactic_resolution
# ═══════════════════════════════════════════════════════════════════════════

def hook_stratagem(context, varfell_revised_card=None):
    # [canonical: mass_battle_v30 §B.4 — "Stratagem (read opponent's tactic card before locking yours)"]
    # [canonical: mass_battle_v30 §B.4 Stratagem resolution PP-690 — "initiative inversion at the tactic-card layer"]
    # [M7_ASSUMPTION_TWO: caller decides whether Varfell revises their card after reading opponent;
    #  if varfell_revised_card is provided, swap; otherwise leave unchanged]
    if context.stratagem_used:
        return context  # idempotent

    if context.attacker_card == 'stratagem':
        # Varfell is attacker — defender's card already revealed by context construction
        if varfell_revised_card is not None and varfell_revised_card in m3.TACTIC_CARDS:
            context.attacker_card = varfell_revised_card
        context.hooks_fired.append('stratagem:attacker')
    elif context.defender_card == 'stratagem':
        # Varfell is defender — attacker's card already revealed
        if varfell_revised_card is not None and varfell_revised_card in m3.TACTIC_CARDS:
            context.defender_card = varfell_revised_card
        context.hooks_fired.append('stratagem:defender')

    context.stratagem_used = True
    return context


# ═══════════════════════════════════════════════════════════════════════════
# HOOK 2 — CRUSADE FERVOUR (Church) — sets disposition + route-suppress flag
# ═══════════════════════════════════════════════════════════════════════════

def hook_crusade_fervour(context):
    # [canonical: mass_battle_v30 §B.4 — "Crusade Fervour (Brutal + Discipline check exempt this turn)"]
    # Disposition routing (Brutal) is already handled by M3.apply_tactic_cards because Crusade Fervour
    # is registered there with disposition=brutal. Hook only handles the route-suppression side effect.
    if context.attacker_card == 'crusade_fervour':
        context.suppress_route_for_attacker = True
        context.hooks_fired.append('crusade_fervour:attacker')
    if context.defender_card == 'crusade_fervour':
        context.suppress_route_for_defender = True
        context.hooks_fired.append('crusade_fervour:defender')
    return context


# ═══════════════════════════════════════════════════════════════════════════
# HOOK 3 — INQUISITOR'S MARK (Church) — opponent pool -2
# ═══════════════════════════════════════════════════════════════════════════

def hook_inquisitors_mark(context):
    # [canonical: mass_battle_v30 §B.4 — "Inquisitor's Mark (target unit -2D, any opponent)"]
    # [M7_ASSUMPTION_THREE: aggregate-count approximation — canon "target unit -2D" is per-unit;
    #  M4's aggregate-count schema cannot express per-unit modifiers, so M7 applies as -2 opponent pool]
    INQUISITORS_MARK_OPPONENT_POOL_DELTA = -2  # [canonical: see hook_inquisitors_mark ledger — -2D aggregate]
    if context.attacker_card == 'inquisitors_mark':
        context.defender_pool_delta += INQUISITORS_MARK_OPPONENT_POOL_DELTA
        context.hooks_fired.append("inquisitors_mark:attacker")
    if context.defender_card == 'inquisitors_mark':
        context.attacker_pool_delta += INQUISITORS_MARK_OPPONENT_POOL_DELTA
        context.hooks_fired.append("inquisitors_mark:defender")
    return context


# ═══════════════════════════════════════════════════════════════════════════
# HOOK 4 — CALCULATED RETREAT (Varfell) — withdrawal, no Overextended
# ═══════════════════════════════════════════════════════════════════════════

def hook_calculated_retreat(context):
    # [canonical: mass_battle_v30 §B.4 — "Calculated Retreat (withdraw without Overextended penalty)"]
    if context.attacker_card == 'calculated_retreat':
        context.withdrawal_no_penalty = True
        context.hooks_fired.append("calculated_retreat:attacker")
    if context.defender_card == 'calculated_retreat':
        context.withdrawal_no_penalty = True
        context.hooks_fired.append("calculated_retreat:defender")
    return context


# ═══════════════════════════════════════════════════════════════════════════
# HOOK 5 — DISAPPEAR (Niflhel) — withdraw + opponent cannot pursue
# ═══════════════════════════════════════════════════════════════════════════

def hook_disappear(context):
    # [canonical: mass_battle_v30 §B.4 — "Disappear (withdraw all units; opponent cannot pursue this season)"]
    if context.attacker_card == 'disappear':
        context.withdrawal_no_penalty = True
        context.pursuit_blocked = True
        context.hooks_fired.append("disappear:attacker")
    if context.defender_card == 'disappear':
        context.withdrawal_no_penalty = True
        context.pursuit_blocked = True
        context.hooks_fired.append("disappear:defender")
    return context


# ═══════════════════════════════════════════════════════════════════════════
# HOOK 6 — DUCAL CALL (Crown) — pre-resolution Muster-from-adjacent
# ═══════════════════════════════════════════════════════════════════════════

def hook_ducal_call(context, adjacent_unit_class='Levy', adjacent_unit_count=1):
    # [canonical: mass_battle_v30 §B.4 — "Ducal Call (summon 1 unit from adjacent territory)"]
    # [M7_ASSUMPTION_FOUR: caller specifies which class to summon; default Levy per MUSTER_DEFAULT_CLASS]
    DUCAL_CALL_UNIT_DEFAULT_COUNT = 1  # [canonical: mass_battle_v30 §B.4 — "summon 1 unit"]
    if context.attacker_card == 'ducal_call':
        existing = context.attacker_units.get(adjacent_unit_class, 0)
        context.attacker_units[adjacent_unit_class] = existing + adjacent_unit_count
        context.hooks_fired.append(f"ducal_call:attacker:+{adjacent_unit_count}_{adjacent_unit_class}")
    if context.defender_card == 'ducal_call':
        existing = context.defender_units.get(adjacent_unit_class, 0)
        context.defender_units[adjacent_unit_class] = existing + adjacent_unit_count
        context.hooks_fired.append(f"ducal_call:defender:+{adjacent_unit_count}_{adjacent_unit_class}")
    return context


# ═══════════════════════════════════════════════════════════════════════════
# HOOK ORCHESTRATION — apply all hooks in known order
# ═══════════════════════════════════════════════════════════════════════════

HOOK_ORDER = [
    # [canonical: M7_ASSUMPTION_FIVE — hook firing order]
    ('stratagem', hook_stratagem),
    ('ducal_call', hook_ducal_call),
    ('crusade_fervour', hook_crusade_fervour),
    ('inquisitors_mark', hook_inquisitors_mark),
    ('calculated_retreat', hook_calculated_retreat),
    ('disappear', hook_disappear),
]


def apply_pre_resolution_hooks(context, varfell_revised_card=None,
                                ducal_call_unit_class='Levy', ducal_call_unit_count=1):
    # [canonical: M7_ASSUMPTION_FIVE — orchestrates all 6 hooks; only fires hooks for cards actually in play]
    cards_in_play = {context.attacker_card, context.defender_card}
    for card_id, hook_fn in HOOK_ORDER:
        if card_id not in cards_in_play:
            continue
        if card_id == 'stratagem':
            context = hook_fn(context, varfell_revised_card=varfell_revised_card)
        elif card_id == 'ducal_call':
            context = hook_fn(context, adjacent_unit_class=ducal_call_unit_class,
                              adjacent_unit_count=ducal_call_unit_count)
        else:
            context = hook_fn(context)
    return context


# ═══════════════════════════════════════════════════════════════════════════
# WITHDRAWAL OUTCOME CONSTRUCTOR
# ═══════════════════════════════════════════════════════════════════════════

def construct_withdrawal_result(context):
    # [canonical: M7_ASSUMPTION_FIVE — when withdrawal_no_penalty fires, return special outcome]
    # No territory transfer, no losses, no Stability penalty, no Accord change.
    return m3.BattleResult(
        outcome='withdrawal',                                       # [canonical: M7-only outcome class — not in M3 OUTCOME_*]
        winner=None,
        attacker_net=0,
        defender_net=0,
        margin=0,
        attacker_pool_total=0,
        defender_pool_total=0,
        territory_transferred=False,
        attacker_losses={},
        defender_losses={},
        route_triggers=[],
        attacker_stability_delta=0,
        attacker_military_delta=0,
        defender_military_delta=0,
        accord_changes={},
        side_effects=['withdrawal_no_penalty'],
    )


# ═══════════════════════════════════════════════════════════════════════════
# RESOLVE_BATTLE_HOOKED — full pipeline with hooks
# ═══════════════════════════════════════════════════════════════════════════

def resolve_battle_hooked(attacker_units, defender_units,
                          attacker_mil, defender_mil,
                          attacker_card, defender_card,
                          fort_level=0, rng=None,
                          varfell_revised_card=None,
                          ducal_call_unit_class='Levy',
                          ducal_call_unit_count=1):
    # [canonical: M3.resolve_battle wrapped with M7 hook orchestration]
    # Builds context, applies pre-resolution hooks, then runs M3 + post-resolution patches.
    if rng is None:
        rng = random.Random()

    # Copy units dicts so hooks mutating them don't surprise the caller
    att_units_copy = dict(attacker_units)
    def_units_copy = dict(defender_units)

    context = ResolutionContext(
        attacker_faction='',  # not currently used by hooks
        defender_faction='',
        attacker_units=att_units_copy,
        defender_units=def_units_copy,
        attacker_mil=attacker_mil,
        defender_mil=defender_mil,
        attacker_card=attacker_card,
        defender_card=defender_card,
        fort_level=fort_level,
        rng=rng,
    )

    # Pre-resolution hook pass
    context = apply_pre_resolution_hooks(
        context,
        varfell_revised_card=varfell_revised_card,
        ducal_call_unit_class=ducal_call_unit_class,
        ducal_call_unit_count=ducal_call_unit_count,
    )

    # Check for withdrawal short-circuit (Calculated Retreat / Disappear)
    if context.withdrawal_no_penalty:
        result = construct_withdrawal_result(context)
        return HookedBattleResult(
            base_result=result,
            pursuit_blocked=context.pursuit_blocked,
            withdrawal_no_penalty=True,
            hooks_fired=list(context.hooks_fired),
        )

    # Normal M3 resolution — but with pool deltas applied via composite faux-card pattern
    # [M7_ASSUMPTION_THREE: pool deltas from Inquisitor's Mark applied by augmenting commander_mil
    #  proxy. Specifically: Inquisitor's Mark -2D opponent translates to +4 commander_mil reduction
    #  (since pool uses floor(mil/2), -4 mil = -2 pool). Hacky but preserves M3 surface.]
    # Cleaner: call M3 internals to compute pool, then add deltas before roll.
    import math
    att_pool_base = m3.compute_pool(context.attacker_units, context.attacker_mil, fort_level=0)
    def_pool_base = m3.compute_pool(context.defender_units, context.defender_mil, fort_level=context.fort_level)
    att_mod, def_mod, m3_side_effects = m3.apply_tactic_cards(
        context.attacker_card, context.defender_card, 0, 0
    )
    att_pool_total = att_pool_base + att_mod + context.attacker_pool_delta
    def_pool_total = def_pool_base + def_mod + context.defender_pool_delta

    att_net = m3.roll_pool(max(0, att_pool_total), rng)
    def_net = m3.roll_pool(max(0, def_pool_total), rng)
    margin = att_net - def_net

    if margin >= m3.MARGIN_DECISIVE:
        outcome = m3.OUTCOME_ATTACKER_WINS
        winner = 'attacker'
        territory_transferred = True
    elif margin <= -m3.MARGIN_DECISIVE:
        outcome = m3.OUTCOME_DEFENDER_WINS
        winner = 'defender'
        territory_transferred = False
    else:
        outcome = m3.OUTCOME_PARTIAL
        winner = None
        territory_transferred = False

    att_dmg_mod = m3._avg_dmg_mod(context.attacker_units)
    def_dmg_mod = m3._avg_dmg_mod(context.defender_units)
    attacker_losses = m3.apply_damage_lowest_martial_first(def_net, context.attacker_units, def_dmg_mod)
    defender_losses = m3.apply_damage_lowest_martial_first(att_net, context.defender_units, att_dmg_mod)

    # Morale checks — but suppress for crusade_fervour side
    route_triggers = []
    for unit_class, lost in attacker_losses.items():
        if lost > 0:
            remaining = context.attacker_units.get(unit_class, 0) - lost
            if remaining > 0 and not context.suppress_route_for_attacker:
                if m3.check_route(unit_class, rng):
                    route_triggers.append(f'attacker:{unit_class}')
    for unit_class, lost in defender_losses.items():
        if lost > 0:
            remaining = context.defender_units.get(unit_class, 0) - lost
            if remaining > 0 and not context.suppress_route_for_defender:
                if m3.check_route(unit_class, rng):
                    route_triggers.append(f'defender:{unit_class}')

    # Outcome deltas
    att_stab_delta = 0
    att_mil_delta = 0
    def_mil_delta = 0
    accord_changes = {}
    if outcome == m3.OUTCOME_ATTACKER_WINS:
        def_mil_delta = m3.BATTLE_LOSS_MILITARY_PENALTY
        accord_changes['new_owner'] = m3.ACCORD_ON_CAPTURE_NEW_OWNER
    elif outcome == m3.OUTCOME_DEFENDER_WINS:
        att_mil_delta = m3.BATTLE_LOSS_MILITARY_PENALTY
        accord_changes['defender_territory'] = m3.ACCORD_ON_DEFEND_DEFENDER
    elif outcome == m3.OUTCOME_PARTIAL:
        att_stab_delta = m3.PARTIAL_ATTACKER_STABILITY_LOSS

    side_effects = list(m3_side_effects)
    if 'attacker_feigned_retreat' in side_effects and outcome == m3.OUTCOME_DEFENDER_WINS:
        side_effects.append('defender_units_overextended_next_season')
    if 'defender_feigned_retreat' in side_effects and outcome == m3.OUTCOME_ATTACKER_WINS:
        side_effects.append('attacker_units_overextended_next_season')

    base = m3.BattleResult(
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
        attacker_stability_delta=att_stab_delta,
        attacker_military_delta=att_mil_delta,
        defender_military_delta=def_mil_delta,
        accord_changes=accord_changes,
        side_effects=side_effects,
    )

    return HookedBattleResult(
        base_result=base,
        pursuit_blocked=context.pursuit_blocked,
        withdrawal_no_penalty=False,
        hooks_fired=list(context.hooks_fired),
    )
