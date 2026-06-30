"""mass_battle.core.exchange — combat-pool assembly primitives.
Stage-1 behaviour-frozen extract from orchestration.py (derive_command, command_base_pool,
subunit_combat_pool, _stamina_pool_penalty). Pure: depends on config + math + duck-typed
unit/atom attributes only; imports nothing from orchestration (no cycle). Re-imported by
orchestration via `from mass_battle.core.exchange import *` so every call site is unchanged.
[canonical: mass_battle_v30.md §A.4 Effective Combat Pool; ED-899 Command-only base]"""
import math
from mass_battle.config import *

__all__ = ['_stamina_pool_penalty', 'derive_command', 'command_base_pool', 'subunit_combat_pool']


def _stamina_pool_penalty(stamina):
    """Return pool penalty (negative int) based on current stamina level."""
    if stamina <= 0:
        return STAMINA_EXHAUSTED_POOL_PENALTY
    for threshold, penalty in STAMINA_POOL_THRESHOLDS:
        if stamina >= threshold:
            return penalty
    return STAMINA_EXHAUSTED_POOL_PENALTY


def derive_command(charisma, cognition):
    """Command DERIVED from Charisma (primary weight) + Cognition (secondary weight).
    [canonical: Jordan canon-structure directive] Command = leadership leverage:
    Charisma primary (inspire/hold the line), Cognition secondary (tactical read).
    Weighted mean on the 1-7 scale, rounded and clamped to 1-7 (derived_stats weighting convention).
    """
    w = CMD_CHA_WEIGHT + CMD_COG_WEIGHT
    val = round((CMD_CHA_WEIGHT * charisma + CMD_COG_WEIGHT * cognition) / w)
    # [canonical: params/factions/stats_1_7_scale.md — attributes on the 1-7 scale; Command clamped to it]
    return max(1, min(7, int(val)))


def command_base_pool(command, pen, stam_pen):
    """Command-only base exchange pool (the COMMAND_SIGMA branch): MULT×Command + pool advantages.
    Module-level so the MECHANICS 'command_sigma_base' entry resolves to a real callable rather than
    a bare constant. [canonical: Jordan canon-structure directive — base driven SOLELY by
    Command; Size enters outcomes only via the Lanchester frontage term; MULT=2 matches
    min(Size,Cmd)+Cmd at Size≥Cmd.]"""
    return COMMAND_POOL_MULT * command + pen + stam_pen


def subunit_combat_pool(unit, atom):
    """Per-subunit combat pool (Jordan directive): SHARED Command (the general),
    per-subunit Discipline + cohesion + stamina. Mirrors Unit.base_combat_pool EXACTLY for a
    single-subunit unit (atom.cohesion fast-paths to unit.hp/hp_max; eff_discipline inherits unit) ->
    byte-exact for the homogeneous gauge; differentiates per subunit for mixed units.
    [canonical: mass_battle_v30.md §A.4 Effective Combat Pool; the (5.0-disc)*0.5 discipline penalty
     mirrors Unit.discipline_penalty 'fix discipline'; size-decoupled cohesion form]"""
    if unit.routed or unit.broken or atom.routed or atom.broken:
        return 0
    disc = atom.eff_discipline
    if disc <= 0:
        # Per-subunit broken state (ED-1020 fix): this SUBUNIT's formation is gone (Discipline 0,
        # §A.4 "Formation broken; cannot attack") -> it contributes 0. The UNIT is broken only when
        # EVERY subunit is broken (the whole formation is gone); a single broken section must NOT zero
        # its healthy siblings' pools -- that was an unintended intra-unit break cascade, contradicting
        # §A.12's inter-unit-only cascade decision and the per-subunit "siblings fight on" model.
        # Single-subunit: the lone subunit broken => all() true => unit.broken set exactly as before
        # (byte-exact for the homogeneous gauge).
        atom.broken = True
        if all(s.broken for s in unit.subunits):
            unit.broken = True
        return 0
    pen = -max(0.0, min(2.0, (5.0 - disc) * 0.5))
    stam_pen = _stamina_pool_penalty(atom.eff_stamina)
    if COMMAND_SIGMA_ENABLED:
        raw = unit.command * (1.0 + atom.cohesion) + pen + stam_pen
    else:
        raw = min(atom.eff_size, unit.command) + unit.command + pen + stam_pen
    return max(1, math.floor(raw))
