"""mass_battle.core.exchange — combat-pool assembly primitives.
Stage-1 behaviour-frozen extract from orchestration.py (derive_command, command_base_pool,
subunit_combat_pool, _stamina_pool_penalty). Pure: depends on config + math + duck-typed
unit/atom attributes only; imports nothing from orchestration (no cycle). Re-imported by
orchestration via `from mass_battle.core.exchange import *` so every call site is unchanged.
[canonical: mass_battle_v30.md §A.4 Effective Combat Pool; ED-899 Command-only base]"""
import math
from mass_battle.config import *
from mass_battle.geometry import cells_to_orig_coords

__all__ = ['_stamina_pool_penalty', 'derive_command', 'command_base_pool', 'subunit_combat_pool',
           'pair_pool_contribution']


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


def pair_pool_contribution(atom, contact_abs_cells, base_pool):
    """[DG-3, ED-MB-0002, Jordan: "Combat pool for a subunit is misleading. It should be based upon
    combat pool per cell as per troop type/quality/density, and the overall combat pool for a
    subunit is actually just a combat score for the subunit. This is bottom-up, and it solves
    issues with multiple engagements."]

    `subunit_combat_pool()` is unchanged and stays exactly what Jordan calls it -- the subunit's
    aggregate COMBAT SCORE (Command + discipline/stamina/cohesion). This function is the bottom-up
    piece: it redistributes that score across a SPECIFIC contact pair by the ACTUAL troop density
    (`atom.cell_troops`, per-cell troop count -- today the only real per-cell signal; troop_type/
    discipline/power are still subunit-uniform, see designs/audit/2026-07-04-mass-battle-cannae-
    gauge-audit/README.md's own confirmation that per-cell type doesn't exist yet) in the cells
    ACTUALLY engaged with the other atom in THIS pair (`contact_abs_cells`, already pair-scoped by
    `find_contacts`), plus depth-weighted support from ranks behind the contact line (reusing the
    same `SUPPORT_WEIGHTS`/`SUPPORT_WEIGHT_FLOOR` falloff `support_engage_frac` already uses).

    This replaces a flat "divide the whole subunit's pool by how many simultaneous pairs it's in"
    approximation with an exact, troop-weighted split: a subunit fighting two enemies with an uneven
    cell split (e.g. 70% of its cells facing one, 30% the other) correctly gives each pair roughly
    its actual share, not a blind 50/50 -- solving RC-1(a)'s multi-front asymmetry from the bottom up
    instead of an atom-level fudge factor.

    Known accepted residual (same discipline as Stage A's TOI multi-body approximation, designs/
    audit/2026-07-01-mass-battle-.../ (see plan file Stage A.5b, finding 3): a single cell
    simultaneously adjacent to TWO enemy atoms contributes its full troop share to BOTH pairs -- a
    genuine dogpile edge case, not solved here, not observed to be dense enough to matter in the
    gauge battery, flagged as a possible future refinement rather than blocking this fix."""
    if atom.cur_troops <= 0 or base_pool <= 0:
        return 0.0
    contact_orig = set(cells_to_orig_coords(atom, set(contact_abs_cells)))
    if not contact_orig:
        return 0.0
    front_r = min(r for r, c in contact_orig)
    weighted_troops = 0.0
    # [2026-07-04 adversarial-review fix] Iterate the atom's ACTUAL cell_troops directly, not a
    # freshly recomputed CELL_PATTERN_FN[shape](tier). A continuous-scale Subunit (troops=/
    # concentration= set) lays out its real footprint via footprint_for(shape, troops,
    # concentration) -- a different coordinate scheme than the legacy tier-keyed pattern, and tier
    # is documented as vestigial on that path. Recomputing from CELL_PATTERN_FN silently missed
    # every real cell outside the small legacy-tier rectangle, collapsing weighted_troops (and thus
    # the whole pair's pool) to 0 for any continuous-scale subunit whose footprint doesn't happen to
    # be a subset of that rectangle -- confirmed by direct repro (a tier=4 troops=8000 Line's real
    # 70-cell footprint vs. the tier's own 35-cell pattern). cell_troops is already the authoritative,
    # footprint/drift-aware source of truth (same one cells()/check_drift use), so iterate it
    # directly and use its own (orig_r, orig_c) keys instead of asking CELL_PATTERN_FN separately.
    cell_troops = getattr(atom, 'cell_troops', None) or {}
    for pid, troops in cell_troops.items():
        if troops <= 0:
            continue
        orig_r, orig_c = pid
        if pid in contact_orig:
            weighted_troops += troops
        elif SUPPORT_STACK_ENABLED and orig_r > front_r:
            depth = orig_r - front_r
            weighted_troops += troops * SUPPORT_WEIGHTS.get(depth, SUPPORT_WEIGHT_FLOOR)
    pool_per_troop = base_pool / atom.cur_troops
    return pool_per_troop * weighted_troops
