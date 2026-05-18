"""
sim/provincial/massbattle.py — Mass-battle resolution engine (multi-turn, multi-unit,
freed-attacker, morale cascade, rout contagion, cavalry pursuit, simultaneous resolution)

Canon source: designs/provincial/mass_battle_v30.md (canonical, approved 2026-04-17);
              designs/provincial/mass_battle_integration_v30.md §4.1 Step 1 (bare port spec);
              designs/architecture/complete_systems_reference.md Part 6 (MASS COMBAT)
Params source: params/mass_combat.md; params/core.md
Game Design constraints applicable: GD-1 (mass-battle resolution produces faction stat /
                                          territorial-control deltas only — no
                                          mass_battle_outcome → game_victory triggers)
Status: [CANONICAL — Phase 7 bare port from tests/sim/sim_mb_06_v22.py 2026-05-18.
         Scope C2 narrow: canon §4.1 Step 1 (bare port) + §4.10 sub-step 3
         (faction_action wiring). Steps 2–9 deferred to later Phase 7 follow-ons.]

Bare-port source: tests/sim/sim_mb_06_v22.py (2143 lines, validated_n1000 in v17 sweep).
Per `mass_battle_integration_v30.md §4.1 Step 1`:
  1. Copy v22 → sim/provincial/massbattle.py  ← THIS FILE
  2. Extract Unit / Subunit dataclasses → sim/provincial/units.py
  3. Extract FACTION_TACTIC_CARD_POOL_MODIFIERS → sim/provincial/tactic_cards.py
       [not present in v22 — canonical-named empty stub; BLOCKED on contamination audit
        per integration_plan_v18 §1.4]
  4. Module docstring per CONVENTIONS  ← THIS HEADER

Dataclasses Subunit + Unit live in `sim.provincial.units` (split per step 2).
This module imports them at file tail (after all module-level constants and
helper functions are defined) — units.py late-binds back to `_mb` for those
names. See units.py docstring for the circular-import resolution pattern.

Dependencies:
  - sim/provincial/units — Subunit, Unit dataclasses (imported at file tail)
  - sim/provincial/tactic_cards — FACTION_TACTIC_CARD_POOL_MODIFIERS (stub)

Entry points:
  - resolve_mass_battle(faction_a, faction_b, terrain, world) -> dict
       Strategic-layer adapter: constructs minimal Unit forces from faction.Mil,
       invokes run_multi_unit_battle, maps result → degree-shaped outcome.
       [GAP: faction→unit construction has no canonical spec; uses minimum-viable
        defaults — shape=Line, tier=2, single subunit per faction, command=4,
        discipline=5, morale=5, power=int(faction.Mil). Phase 7 Step 10 sub-steps
        1-2 (domain_echo / accounting) deferred — will introduce richer mapping.]
  - run_multi_unit_battle(side_a, side_b, pairings, shapes_a, shapes_b, ...) -> dict
       v22 multi-unit orchestrator — full feature surface preserved.
  - run_multi_turn_battle(unit_a, unit_b, shape_a, shape_b, anchor_map, ...) -> dict
       v22 multi-turn loop with phase-boundary hooks.
  - run_battle(unit_a, unit_b, max_turns=18) -> dict
       v22 single-encounter resolver.
"""
import random, math, statistics, time
from dataclasses import dataclass, field
from typing import List, Tuple, Optional, Dict, Set

# [canonical: designs/provincial/mass_battle_v30.md §map — 25×25 grid, 5-cell buffer per side]
BATTLEFIELD_SIZE = 25
# [canonical: designs/provincial/mass_battle_v30.md §units — 15×15 cell unit grid fits T4 pattern]
UNIT_GRID_SIZE = 15
BUFFER_CELLS = 5
# v20 fix: symmetric deployment. Both sides 7 rows from center (row 12).
# [canonical: designs/provincial/mass_battle_v30.md §deployment]
SIDE_A_START_ROW = 16  # symmetric: 4 from center
SIDE_B_START_ROW = 8   # symmetric: 4 from center

POOL_VARIANT = "C-ii"

TIP_SUPPORT_ENABLED = True
TIP_SUPPORT_GAP = 2

# [canonical: mass_battle_v30.md §Scale — T1=100(1 size), T2=200(2), T3=400(4), T4=800(8), base 100]
TROOPS_PER_TIER = {1: 100, 2: 200, 3: 400, 4: 800}
TROOPS_PER_SIZE = 100
ENCIRCLEMENT_PENALTY = 1

# F-i: Cell support stacking [canonical: Jordan handoff §(1)]
SUPPORT_STACK_ENABLED = True
# [canonical: Jordan handoff §(1) — depth-1: full, depth-2: 0.7, depth-3: 0.5, floor 0.3]
SUPPORT_WEIGHTS = {1: 1.0, 2: 0.7, 3: 0.5}
SUPPORT_WEIGHT_FLOOR = 0.3

# F-ii: Puncture mechanism [canonical: Jordan handoff §(2)]
PUNCTURE_ENABLED = True
PUNCTURE_CAP = 3

# F-iii: Cascading resolution [canonical: Jordan handoff §(3)]
CASCADING_ENABLED = True
MAX_SUB_PHASES = 5

# ─── v14: PHASE / TICK STRUCTURE ────────────────────────────────────────────
# A "tick" is one resolution cycle (volley + advance + engagement). A "phase"
# is a block of TICKS_PER_PHASE ticks corresponding to one cavalry charge-and-
# return cycle (approach + gallop + impact + contact + disengage/reform).
# A pre-modern battle is then ~3-6 phases, matching the 30-90 minutes of
# active fighting found in hoplite, medieval, and early-modern accounts.
# [canonical: Jordan design — phase = gallop and charge cycle, ~5-6 ticks per
#  Operational Studies Group's "three-hex charge would take about 5 minutes",
#  with reform-to-position adding 1-2 ticks; hoplite phalanx fighting bounded
#  ~10-15 minutes by exhaustion before rotation/withdrawal]
TICKS_PER_PHASE = 6

# ─── TROOP COUNT / BLOCK SIZE (bottom-up lethality) ─────────────────────────
# [canonical: designs/provincial/mass_battle_v30.md §A.3 — "1 Size = block_size soldiers"]
# [canonical: derived_stats architecture (2026-04-19) — "TroopCount = Size × block_size"]
# HP = TroopCount = Size × BLOCK_SIZE. Damage from combat = soldier casualties.
# No LETHALITY_SCALE — casualty rates emerge from pool/TN/DR mechanics directly.
# At Company scale: Size 4 unit = 400 soldiers = 400 HP. Pool=8, ~3 successes/tick
# = ~3 soldiers killed/tick = 0.75%/tick = ~13% per 3-phase turn. Emergent.
BLOCK_SIZE = 100  # [canonical: designs/provincial/mass_battle_v30.md §A.3 — Company scale]

# ─── MORALE EROSION (v20 — fully emergent) ───────────────────────────────────
# [canonical: designs/provincial/mass_battle_v30.md §A.4 morale triggers]
# v20: morale eroded by damage_taken / (discipline × command) each tick.
# NO thresholds. Rout point emerges from unit stats:
#   morale 6, damage ~3/tick, disc=5, cmd=4: erosion 3/20 = 0.15/tick
#   morale 6 → 0 in 40 ticks × 0.75%/tick = ~30% casualties to rout.
#   cmd=6: 45% to rout. cmd=2: 15%. Generalship dominance (T1) is structural.
# Morale is now float (accumulates fractional erosion). Rout at morale ≤ 0.
# No morale floor — general's contribution is in the denominator.
# [canonical: designs/provincial/mass_battle_v30.md §A.4 — "Generalship dominates"]

# ─── STAMINA CONSTANTS (G-1) ────────────────────────────────────────────────
# [ASSUMPTION: stamina constants are tuning parameters — basis: no canonical
#  source specifies stamina values; audit G-1 identifies the mechanism gap
#  without prescribing numbers. Validated against battery.]
STAMINA_MAX = 100
STAMINA_DRAIN_PER_CONTACT_CELL = 1   # drain per cell in contact per tick
# v20: stamina drain proportional to cells in contact — emergent from formation.
# v20 fix: 1/cell gives ~8 drain/tick at 8 contact cells → 12.5 ticks to exhaust.
# Historical: front-rank rotation every 2-3 phases (12-18 ticks).
# [ASSUMPTION: drain per contact cell is a tuning parameter]
# Recovery at phase boundary: per reserve rank (rows behind front row).
# Net drain/phase (6 contact ticks × 16 = 96):
#   RF (6 reserve × 8 = 48): net −48/phase. Exhausts mid-phase 3.
#   Line (4 reserve × 8 = 32): net −64/phase. Exhausts early phase 2.
#   HS (3 reserve × 8 = 24): net −72/phase. Exhausts late phase 1.
#   GL (2 reserve × 8 = 16): net −80/phase. Exhausts mid phase 1.
STAMINA_RECOVERY_PER_RESERVE_RANK = 8
# Pool penalty: only at exhaustion. The differentiation comes from WHEN each
# formation exhausts, not how much worse they get. -1 die when exhausted =
# small but persistent disadvantage that compounds across many ticks.
# Deeper formations recover more → exhaust later → fight at full pool longer.
STAMINA_POOL_THRESHOLDS = [(1, 0)]  # no penalty while stamina > 0
STAMINA_EXHAUSTED_POOL_PENALTY = -1  # stamina == 0: -1 die
# G-2 rout-at-threshold constants (phase-boundary morale check for exhausted units)
# [canonical: mass_battle_v30.md §A.4 — morale floor = 1 while general present;
#  G-2 overrides this for exhausted+damaged units at phase boundary]
ROUT_FLOOR_LOSS_PCT = 0.20          # casualty% at which exhausted unit loses morale floor
ROUT_EXHAUSTION_MORALE_HIT = 1      # morale loss per phase boundary when exhausted
# [canonical: mass_battle_v30.md §A.4 — cap −3 per Cascade Phase for non-general morale loss]
MORALE_PHASE_CAP = 3

# ─── DISCIPLINE DEGRADATION WITH CONTINUOUS EFFECTIVE_SIZE (D-6) ─────────
# [canonical: params/mass_combat.md §Discipline Degradation —
#  "Discipline degrades when Size lost > Discipline AND asymmetric"]
# Reinterpreted for continuous: check cumulative HP loss as fraction of
# h_per_size at each phase boundary. Fires when cumulative_loss in eff_size
# terms exceeds 1.0 AND loss is asymmetric. Each time it fires, threshold
# resets (so it can fire again after another 1.0 eff_size loss).
# [ASSUMPTION: threshold 1.0 eff_size maps to "Size lost > 1" in original]
DISCIPLINE_LOSS_THRESHOLD = 1.0  # [canonical: params/mass_combat.md §Discipline Degradation]

# ─── PHASE-BOUNDARY HOOKS ───────────────────────────────────────────────────
# Called once per phase boundary. Order is canonical:
# stamina → morale → rout → rally → reform → threadwork.
# v15 populates stamina_check, morale_check_phase, rout_resolution.
# rally_check, reform_check, threadwork_check remain empty (future cycles).


def _formation_depth(unit):
    """Max row count across all subunits = number of distinct ranks.
    Deeper formations have more reserve ranks for stamina rotation.
    [canonical: audit_sim_mb_06_v14.md §G-1 — depth permits rotation]"""
    max_depth = 1
    for sub in unit.subunits:
        pattern = CELL_PATTERN_FN[sub.shape](sub.tier)
        if pattern:
            rows = max(r for r, c in pattern) + 1
            if rows > max_depth:
                max_depth = rows
    return max_depth


def _stamina_pool_penalty(stamina):
    """Return pool penalty (negative int) based on current stamina level."""
    if stamina <= 0:
        return STAMINA_EXHAUSTED_POOL_PENALTY
    for threshold, penalty in STAMINA_POOL_THRESHOLDS:
        if stamina >= threshold:
            return penalty
    return STAMINA_EXHAUSTED_POOL_PENALTY


def stamina_check(unit_a, unit_b, phase_idx):  # noqa: ARG001
    """G-1: at phase boundary, recover stamina proportional to formation depth.
    Drain happens per-tick in run_battle; this hook handles rotation recovery.
    [canonical: audit_sim_mb_06_v14.md §G-1 — depth permits front-rank rotation]"""
    for u in [unit_a, unit_b]:
        if u.routed or u.broken:
            continue
        depth = _formation_depth(u)
        reserve_ranks = max(0, depth - 1)
        recovery = STAMINA_RECOVERY_PER_RESERVE_RANK * reserve_ranks
        u.stamina = min(u.stamina_max, u.stamina + recovery)


def morale_check_phase(unit_a, unit_b, phase_idx):  # noqa: ARG001
    """v17: phase-boundary morale = exhaustion pressure ONLY (D-7 fix).
    Per-tick morale handles casualty-based triggers separately.
    Exhausted units lose -1 morale at phase boundary (within cap).
    Floor is NOT overridden here — that's the per-tick trigger's job.
    [canonical: designs/provincial/mass_battle_v30.md §A.4 — morale floor 1 while general present;
     §A.4 — cap −3 non-general morale loss per Cascade Phase]"""
    for u in [unit_a, unit_b]:
        if u.routed or u.broken:
            continue
        if u.stamina > 0:
            continue  # only exhausted units feel phase-boundary pressure
        # v20: exhaustion accelerates morale erosion at phase boundary.
        # Additional erosion = 1.0 / (discipline * command). Small but compounds.
        if u.discipline > 0 and u.command > 0:
            exhaustion_erosion = 1.0 / (u.discipline * u.command)
            u.morale -= exhaustion_erosion


def rout_resolution(unit_a, unit_b, phase_idx):  # noqa: ARG001
    """Units with morale ≤ 0 rout.
    [canonical: designs/provincial/mass_battle_v30.md §A.12 —
     "Routing: Slow/Standard cannot fight back."
     "Pursuit: Fast units only. Routing unit loses Size equal to pursuer net
      Offence successes (no Defence) each turn. Recall: Command Ob 2."]
    v19: Standard infantry cannot pursue. Pursuit is a level-2 mechanic
    that fires at the battle-map level when a Fast unit is adjacent.
    Morale Cascade (§A.12): friendly units in same engagement make
    Discipline check Ob 1 on rout — modeled when multi-unit engagements exist."""
    for u, opponent in [(unit_a, unit_b), (unit_b, unit_a)]:
        if u.routed or u.broken:
            continue
        if u.morale <= 0:
            u.routed = True
            # No pursuit damage from Standard infantry (canonical: Fast only).
            # Pursuit damage will be handled at the battle-map level (level 2)
            # when cavalry (G-11) and multi-unit engagements (D-3) are implemented.


def discipline_check_phase(unit_a, unit_b, phase_idx):  # noqa: ARG001
    """v18 (D-6): discipline degradation at phase boundary using cumulative loss.
    [canonical: params/mass_combat.md §Discipline Degradation —
     deterministic, fires when effective_size loss > threshold AND asymmetric]"""
    a_loss = (unit_a.hp_max - unit_a.hp) / BLOCK_SIZE if BLOCK_SIZE else 0
    b_loss = (unit_b.hp_max - unit_b.hp) / BLOCK_SIZE if BLOCK_SIZE else 0
    for u, my_loss, their_loss in [(unit_a, a_loss, b_loss), (unit_b, b_loss, a_loss)]:
        if u.routed or u.broken:
            continue
        # How many full thresholds of loss have we crossed?
        disc_hits = int(my_loss / DISCIPLINE_LOSS_THRESHOLD)
        # How many have we already applied? Track via discipline_start - discipline
        already_applied = u.discipline_start - u.discipline
        if disc_hits > already_applied and my_loss > their_loss:
            u.discipline = max(0, u.discipline - 1)
            u.check_drift()


def rally_check(unit_a, unit_b, phase_idx):  # noqa: ARG001
    """Empty hook — rally lands in a future cycle (G-7)."""
    pass

def reform_check(unit_a, unit_b, phase_idx):  # noqa: ARG001
    """Empty hook — reform lands in a future cycle (G-8)."""
    pass

def threadwork_check(unit_a, unit_b, phase_idx):  # noqa: ARG001
    """Empty hook — threadwork lands in a future cycle (G-9)."""
    pass

def phase_boundary(unit_a, unit_b, phase_idx):
    """Run the phase-boundary hook sequence in canonical order.
    Called every TICKS_PER_PHASE ticks within run_battle."""
    stamina_check(unit_a, unit_b, phase_idx)
    discipline_check_phase(unit_a, unit_b, phase_idx)
    morale_check_phase(unit_a, unit_b, phase_idx)
    rout_resolution(unit_a, unit_b, phase_idx)
    rally_check(unit_a, unit_b, phase_idx)
    reform_check(unit_a, unit_b, phase_idx)
    threadwork_check(unit_a, unit_b, phase_idx)

# v9 Volley (Phase 2 ranged fire) [canonical: mass_battle_v30.md §A.7 Phase 2; PP-503]
VOLLEY_ENABLED = True
# TN for Volley success rolls. Standard d10: TN 6 success rate ≈ 0.5/die.
# [canonical: mass_battle_v30.md §A.7 PP-503 — "TN 6 [PROVISIONAL]"]
VOLLEY_TN = 6
# [canonical: mass_battle_v30.md §A.7 PP-503 — "Roll [Power stat] dice"]
# Volley pool = Power dice; not the engagement pool formula.
# Ranged DR table [canonical: params/mass_combat.md §Ranged DR Table — Volley Phase, PP-188]
# Keys: (armour_class) → DR vs Piercing. Sim default: Light armour (DR 1).
# Ranged_DR_None=0, Light=1, Medium=2, Heavy=3 (Piercing column).
# Default DR vs Piercing (ranged) applied to ALL volley targets. Medium-armoured
# infantry (typical Veteran/Professional tier) = DR 2 vs Piercing. Configurable via
# Atom.armour_class in future iterations.
# [canonical: params/mass_combat.md §Ranged DR Table — Medium vs Piercing = 2]
# [canonical: params/mass_combat.md §Ranged DR Table — default DR vs piercing 2]
RANGED_DR_DEFAULT = 2
# Minimum cell-distance for Volley targeting. Distance ≤ 1 = adjacent/melee contact;
# ranged units historically stop firing once enemy closes to hand-to-hand range.
# [canonical: mass_battle_v30.md §A.7 Phase 2 vs Phase 5 — Volley is pre-Engagement;
#  once contact made, units fight in melee not volley]
VOLLEY_MIN_RANGE = 2
# v12: VOLLEY_MAX_RANGE reduced from BATTLEFIELD_SIZE (25) to 8.
# Initial deployment is row 5 vs row 15 = 10 cells apart. Range 8 means ranged
# units must close 1-2 cells (or wait for enemy to approach) before volley begins.
# Historical longbow at Crécy/Agincourt: effective fire began ~100 paces (~5 cells)
# but harassment fire extended further. Range 8 captures both regimes.
# Reduces R1 (Ranged vs Line) by ~25% by removing 4-5 turns of free volley.
# [canonical: references/historical/precedents_warfare.md — effective volleys at
#  100-200 paces; killing zone was the final approach to contact]
VOLLEY_MAX_RANGE = 8

# [canonical: mass_battle_v30.md §ED-816 shape mods; -99 = structural sentinel (−∞ pool)]
# [canonical: v11 — gap=-99 removed for GappedLine. Gap effect is geometric:
#  no cells at the gap column means no engagement there. Per-cell angles handle
#  the flanking naturally. Structural sentinel only retained where cell is absent.]
SHAPE_OFF_MOD = {
    "Line":        lambda role: 0,
    "Arrowhead":   lambda role: 0,
    "Horseshoe":   lambda role: 0,
    "GappedLine":  lambda role: 0,
    "RefusedFlank":lambda role: 0,
}
SHAPE_DEF_MOD = {"Line": lambda r: 0, "Arrowhead": lambda r: 0,
                  "Horseshoe": lambda r: 0,
                  "GappedLine": lambda r: 0, "RefusedFlank": lambda r: 0}
MIN_DISCIPLINE = {
    # [canonical: mass_battle_v30.md §ED-815 shape discipline — min disc required by shape]
    "Line": 1, "Arrowhead": 4, "Horseshoe": 5, "GappedLine": 5, "RefusedFlank": 3
}

# ─── CELL PATTERNS ───────────────────────────────────────────────────────────
# [canonical: mass_battle_v30.md §Shapes — per-tier cell grid dimensions, Jordan design]

def arrowhead_cells(tier):
    cells = []
    for r in range(tier + 2):
        width = 2 * r + 1
        center_col = tier + 1
        start = center_col - r
        for c in range(start, start + width):
            cells.append((r, c))
    return cells

def line_cells(tier):
    sizes = {1: (3, 3), 2: (5, 3), 3: (5, 5), 4: (7, 5)}
    width, depth = sizes.get(tier, (7, 5))
    return [(r, c) for r in range(depth) for c in range(width)]

def horseshoe_cells(tier):
    sizes = {1: (2, 2), 2: (2, 3), 3: (3, 3), 4: (3, 4)}
    wing_w, depth = sizes.get(tier, (3, 4))
    full_width = wing_w * 2 + 1
    cells = []
    for r in range(depth):
        for c in range(wing_w):
            cells.append((r, c))
        for c in range(wing_w + 1, full_width):
            cells.append((r, c))
    for c in range(full_width):
        cells.append((depth, c))
    return cells

def gapped_line_cells(tier):
    # [canonical: v10 — sized to match Line cell count at each tier so advantage
    #  emerges from arrangement (the gap), not extra troops. Was 56 cells T3, now 24.]
    sizes = {1: (2, 2), 2: (3, 3), 3: (4, 3), 4: (4, 4)}
    half_w, depth = sizes.get(tier, (4, 4))
    cells = []
    for r in range(depth):
        for c in range(half_w):
            cells.append((r, c))
        for c in range(half_w + 1, 2 * half_w + 1):
            cells.append((r, c))
    return cells

def refused_flank_cells(tier):
    # [canonical: v10 — sized to match Line cell count at each tier. Engaging-side
    #  block is (width-1) × depth, plus 1 cell at front of refused column.
    #  The refused side withdraws troops from contact (geometric concentration on engaging side),
    #  not from total. Was 21 cells T3, now 25.]
    sizes = {1: (3, 4), 2: (4, 5), 3: (5, 6), 4: (6, 7)}
    width, depth = sizes.get(tier, (6, 7))
    cells = []
    for r in range(depth):
        for c in range(width - 1):
            cells.append((r, c))
    # One forward cell in the refused column at the front row
    cells.append((depth, width - 1))
    return cells

CELL_PATTERN_FN = {
    "Line": line_cells, "Arrowhead": arrowhead_cells,
    "Horseshoe": horseshoe_cells, "GappedLine": gapped_line_cells,
    "RefusedFlank": refused_flank_cells,
}

def oriented_pattern(shape, tier, advance_dir):
    pattern = CELL_PATTERN_FN[shape](tier)
    if advance_dir == -1:
        return [(r, c, r, c) for r, c in pattern]
    max_r = max(r for r, c in pattern)
    return [(r, c, max_r - r, c) for r, c in pattern]

def cell_facing(advance_dir):
    # [canonical: v11 — legacy centroid facing, kept for fallback only]
    return (advance_dir, 0)

# v11: Per-cell octagon angle model
# [canonical: Jordan design — octagon, 2 GREEN faces = 90°, 2 YELLOW = 45°+45°, 4 RED = 180°]
# Facing = raw movement vector per cell (not snapped). Octagon rotates to facing direction.
# Angle between attack vector and defender facing:
#   GREEN  |diff| < 45°  → 0 modifier   (attacker in defender's front arc)
#   YELLOW 45° ≤ |diff| < 90° → -1D     (attacker at defender's flank)
#   RED    |diff| ≥ 90° → -2D           (attacker in defender's rear 180°)

def octagon_angle(attacker_pos, defender_pos, defender_facing_vec):
    """
    Compute octagon zone (GREEN/YELLOW/RED) for an attack on defender.
    defender_facing_vec: raw (dr, dc) movement vector of the defender cell.
    Returns zone string and angle in degrees.
    """
    fr, fc = defender_facing_vec
    fmag = max(1e-9, (fr*fr + fc*fc) ** 0.5)
    # Vector from defender to attacker
    dr = attacker_pos[0] - defender_pos[0]
    dc = attacker_pos[1] - defender_pos[1]
    amag = max(1e-9, (dr*dr + dc*dc) ** 0.5)
    # Cosine of angle between defender facing and direction-to-attacker
    cos_a = (dr * fr + dc * fc) / (amag * fmag)
    cos_a = max(-1.0, min(1.0, cos_a))
    angle_deg = math.degrees(math.acos(cos_a))
    # [canonical: Jordan design — octagon: GREEN<45deg, YELLOW 45-90deg, RED>=90deg]
    # 45.0 = half of GREEN 90deg face; 90.0 = boundary of rear hemisphere
    if angle_deg < 45.0:   return "GREEN",  angle_deg
    if angle_deg < 90.0:   return "YELLOW", angle_deg  # [canonical: designs/provincial/mass_battle_v30.md §octagon]
    return "RED", angle_deg

ANGLE_DEF_MOD = {
    # v11: per-cell octagon. GREEN < 45° = 0D; YELLOW 45-90° = -1D; RED ≥ 90° = -2D.
    # [canonical: Jordan design]
    "GREEN": 0, "YELLOW": -1, "RED": -2,
    "FRONT": 0, "FLANK": -1, "REAR": -2,  # legacy aliases
}

def atom_max_width(shape, tier):
    pattern = CELL_PATTERN_FN[shape](tier)
    by_row = {}
    for r, c in pattern:
        by_row.setdefault(r, []).append(c)
    return max(len(v) for v in by_row.values())

# ─── F-i: CELL SUPPORT STACKING ──────────────────────────────────────────────

def cells_to_orig_coords(atom, abs_cells):
    op = oriented_pattern(atom.shape, atom.tier, atom.advance_dir)
    orig_coords = []
    for abs_r, abs_c in abs_cells:
        for orig_r, orig_c, or_r, or_c in op:
            comp_r = (atom.starting_position[0] + or_r
                      + atom.cell_offsets.get((orig_r, orig_c), 0) * atom.advance_dir)
            comp_c = (atom.starting_position[1] + or_c
                      + atom.cell_offsets_c.get((orig_r, orig_c), 0))
            if (comp_r, comp_c) == (abs_r, abs_c):
                orig_coords.append((orig_r, orig_c))
                break
    return orig_coords

def support_engage_frac(atom, contact_abs_cells):
    """F-i: support-stack-adjusted engage_frac.
    Cells behind the contact zone contribute weighted support.
    [canonical: Jordan handoff §(1)]"""
    max_w = atom_max_width(atom.shape, atom.tier)
    if not SUPPORT_STACK_ENABLED:
        return len(set(contact_abs_cells)) / max_w

    pattern = CELL_PATTERN_FN[atom.shape](atom.tier)
    contact_orig = cells_to_orig_coords(atom, set(contact_abs_cells))

    if not contact_orig:
        return len(set(contact_abs_cells)) / max_w

    contact_orig_set = set(contact_orig)
    front_r = min(r for r, c in contact_orig)

    supporter_total = 0.0
    for orig_r, orig_c in pattern:
        if (orig_r, orig_c) in contact_orig_set:
            continue
        if orig_r <= front_r:
            continue
        depth = orig_r - front_r
        w = SUPPORT_WEIGHTS.get(depth, SUPPORT_WEIGHT_FLOOR)
        supporter_total += w

    effective_engaged = len(contact_orig) + supporter_total
    return min(1.0, effective_engaged / max_w)

# ─── F-iii: FACING HELPERS ───────────────────────────────────────────────────

def _cell_facing_key(atom, orig_r, orig_c):
    return (id(atom), orig_r, orig_c)

def _rotate_defender_facing(defender_atom, defender_abs_cells, attacker_abs_cells,
                             dynamic_facings):
    """Rotate engaged defender cells toward attacker (Rule A: full pivot).
    [canonical: Jordan handoff §(3a)]"""
    if not attacker_abs_cells or not defender_abs_cells:
        return
    att_r = sum(c[0] for c in attacker_abs_cells) / len(attacker_abs_cells)
    att_c = sum(c[1] for c in attacker_abs_cells) / len(attacker_abs_cells)
    op = oriented_pattern(defender_atom.shape, defender_atom.tier, defender_atom.advance_dir)
    for abs_r, abs_c in defender_abs_cells:
        for orig_r, orig_c, or_r, or_c in op:
            comp_r = (defender_atom.starting_position[0] + or_r
                      + defender_atom.cell_offsets.get((orig_r, orig_c), 0) * defender_atom.advance_dir)
            comp_c = (defender_atom.starting_position[1] + or_c
                      + defender_atom.cell_offsets_c.get((orig_r, orig_c), 0))
            if (comp_r, comp_c) == (abs_r, abs_c):
                dr = att_r - abs_r
                dc = att_c - abs_c
                mag = max(1e-9, (dr*dr + dc*dc)**0.5)
                dynamic_facings[_cell_facing_key(defender_atom, orig_r, orig_c)] = \
                    (round(dr / mag), round(dc / mag))
                break

def _init_dynamic_facings(unit_a, unit_b):
    df = {}
    for u in [unit_a, unit_b]:
        for atom in u.subunits:
            op = oriented_pattern(atom.shape, atom.tier, atom.advance_dir)
            for orig_r, orig_c, _, _ in op:
                df[_cell_facing_key(atom, orig_r, orig_c)] = cell_facing(atom.advance_dir)
    return df

def _atom_avg_facing(atom, contact_abs_cells, dynamic_facings):
    """Compute average facing for an atom's contact cells from dynamic_facings."""
    op = oriented_pattern(atom.shape, atom.tier, atom.advance_dir)
    facings = []
    for abs_r, abs_c in contact_abs_cells:
        for orig_r, orig_c, or_r, or_c in op:
            comp_r = (atom.starting_position[0] + or_r
                      + atom.cell_offsets.get((orig_r, orig_c), 0) * atom.advance_dir)
            comp_c = (atom.starting_position[1] + or_c
                      + atom.cell_offsets_c.get((orig_r, orig_c), 0))
            if (comp_r, comp_c) == (abs_r, abs_c):
                key = _cell_facing_key(atom, orig_r, orig_c)
                facings.append(dynamic_facings.get(key, cell_facing(atom.advance_dir)))
                break
    if not facings:
        return cell_facing(atom.advance_dir)
    return (sum(f[0] for f in facings) / len(facings),
            sum(f[1] for f in facings) / len(facings))

# ─── PER-CELL SPEED ──────────────────────────────────────────────────────────

def cell_speed(shape, tier, local_r, local_c):
    if shape == "Line":    return 1
    if shape == "Arrowhead": return 2 if local_r == 0 else 1
    if shape == "Horseshoe":
        sizes = {1: 2, 2: 2, 3: 3, 4: 3}
        wing_w = sizes.get(tier, 3)
        depth_sizes = {1: 2, 2: 3, 3: 3, 4: 4}
        depth = depth_sizes.get(tier, 4)
        if local_r == depth:    return 0
        elif local_c != wing_w: return 2
        return 1
    if shape == "GappedLine": return 1
    if shape == "RefusedFlank":
        sizes = {1: 3, 2: 4, 3: 5, 4: 6}
        width = sizes.get(tier, 6)
        # v12: front row of engaged side at speed 2 (oblique-order charge).
        # The "phalanx push" was led by the front rank at battle pace, with
        # deeper ranks following at marching pace. Whole-column speed 2 over-tunes
        # vs Line (H6); front-2-rows still over-tunes; front-row-only is the
        # partial momentum bonus that helps against wide formations (HS) without
        # dominating same-width opposition (Line).
        # Refused cell at width-1 holds at speed 0.
        # [canonical: references/historical/precedents_warfare.md — Leuctra 371 BC,
        #  Theban front rank advanced at battle pace; depth followed]
        if local_c == width - 1: return 0
        if local_r == 0: return 2
        return 1
    return 1

STANCE_SPEED_MOD = {"aggressive": 1, "balanced": 0, "hold": -99, "retreat": 0}

# ─── ATOM ────────────────────────────────────────────────────────────────────


# ─── DICE ────────────────────────────────────────────────────────────────────

def roll_pool(n, tn=7):
    net = 0
    for _ in range(max(1, n)):
        f = random.randint(1, 10)
        if f == 1:         net -= 1
        elif tn <= f <= 9: net += 1
        elif f == 10:      net += 2
    return net

def compute_degree(net, ob):
    if net <= 0:                    return "Failure"
    if net >= 2 * ob and net >= 3:  return "Overwhelming"
    if net >= ob:                   return "Success"
    return "Partial"

DAMAGE_BY_DEGREE = {"Overwhelming": lambda p: 1+p, "Success": lambda p: p,
                     "Partial": lambda p: 1,        "Failure": lambda p: 0}

# ─── TARGETING ───────────────────────────────────────────────────────────────

def assign_targets(unit_a, unit_b):
    for atom in unit_a.subunits:
        if not unit_b.subunits: atom.target_atom = None; continue
        if atom.order_target_idx is not None and atom.order_target_idx < len(unit_b.subunits):
            atom.target_atom = unit_b.subunits[atom.order_target_idx]
        else:
            my = atom.centroid()
            atom.target_atom = min(unit_b.subunits,
                key=lambda e: math.hypot(my[0]-e.centroid()[0], my[1]-e.centroid()[1]))
    for atom in unit_b.subunits:
        if not unit_a.subunits: atom.target_atom = None; continue
        if atom.order_target_idx is not None and atom.order_target_idx < len(unit_a.subunits):
            atom.target_atom = unit_a.subunits[atom.order_target_idx]
        else:
            my = atom.centroid()
            atom.target_atom = min(unit_a.subunits,
                key=lambda e: math.hypot(my[0]-e.centroid()[0], my[1]-e.centroid()[1]))

# ─── CONTACTS ────────────────────────────────────────────────────────────────

# [canonical: Jordan design — speed-priority cell contention; historical: Crécy/Agincourt timing, Leuctra oblique order, hoplite equal-speed combat resolution]
def resolve_cross_side_contention(unit_a, unit_b):
    """v13: cross-side cell contention — strict speed-differential resolution.

    Historical model (per Jordan design this session, confirmed against precedent):

    The default v11/v12 sim allowed cells from opposing sides to magically
    co-locate at the same abs position (a contact zone where both sides exist
    on the same square). Per Jordan: "if they were to occupy the same cell,
    then the troop with higher speed gets priority for taking up that adjacent
    cell while the other remains in place."

    Historical precedents for the resolution model:

      Crécy and Agincourt (Hundred Years' War): English archers reached their
      defensive positions BEFORE French cavalry could close. The speed
      advantage (defenders pre-positioned, attackers slowed by terrain) meant
      the English took the ground; French had to halt and assault from
      disadvantaged position. Loser of the timing race stays in place.

      Leuctra (Epaminondas's oblique order, classical Greek): the strong left
      wing advanced FASTER than the weakened right. Strong wing reached enemy
      first, hit Spartan elite before Spartan right could engage the
      weakened Theban right. Speed advantage = first-engagement priority.

      Phalanx-meets-phalanx (Greek hoplite era, Roman vs Roman): two
      equally-fast disciplined formations meeting at the contact line.
      Neither side gains ground via movement alone — the push (othismos)
      decides via combat. Resolution-by-movement only fires on CLEAR speed
      differential; equal-speed meetings stay at the magical-co-location
      contact zone where combat resolves the outcome.

    Implementation:

      For each contested abs position (cells from BOTH sides):
        - Skip if both sides have only static cells (stale contention)
        - If a_speed > b_speed: A wins, B loser-cells that moved this turn
          revert to their pre-move snapshot (didn't advance into A's space)
        - If b_speed > a_speed: symmetric
        - Tied speed: NO MOVEMENT-BASED RESOLUTION. Cells stay at contested
          position; combat resolves via find_contacts + engagement damage.
          This is the historically-correct behavior for equal-speed meetings.

      Size and random tiebreakers from Jordan's spec are NOT applied. Per
      historical precedent, equal-speed equal-size meetings don't resolve
      by movement priority — they resolve by combat. Applying random
      tiebreakers per contested position per turn introduces battery noise
      that doesn't model anything historical. Reserved for cavalry charge-
      through cases (where size and morale do matter for penetration depth).

    Charge-through (cavalry past static infantry) and end-of-phase
    displacement: deferred — no cavalry in current battery, and the
    framework is in place to add it via speed/power/facing inputs when
    cavalry units enter the test suite.

    Citation: see preceding canonical comment.
    """
    def collect(unit):
        """abs_pos -> [(subunit, orig_coord, contention_speed)]"""
        result = {}
        for su in unit.subunits:
            op = oriented_pattern(su.shape, su.tier, su.advance_dir)
            for orig_r, orig_c, or_r, or_c in op:
                ar = (su.starting_position[0] + or_r
                      + su.cell_offsets.get((orig_r, orig_c), 0) * su.advance_dir)
                ac = (su.starting_position[1] + or_c
                      + su.cell_offsets_c.get((orig_r, orig_c), 0))
                # Contention speed: only counts if cell moved this turn
                speed = (su.cell_last_speed.get((orig_r, orig_c), 0)
                         if (orig_r, orig_c) in su._moved_this_turn
                         else 0)
                result.setdefault((ar, ac), []).append((su, (orig_r, orig_c), speed))
        return result

    a_pos = collect(unit_a)
    b_pos = collect(unit_b)
    contested = set(a_pos.keys()) & set(b_pos.keys())
    n_resolved = 0
    for pos in contested:
        a_cells = a_pos[pos]
        b_cells = b_pos[pos]
        # Each side's representative speed is its highest at this position
        a_speed = max(sp for _, _, sp in a_cells)
        b_speed = max(sp for _, _, sp in b_cells)
        # Skip stale contention — neither moved into this position this turn
        if a_speed == 0 and b_speed == 0:
            continue
        # Strict speed differential only. Equal-speed meetings stay co-located
        # (combat resolves via engagement, not movement priority).
        if a_speed > b_speed:
            winner = 'A'
        elif b_speed > a_speed:
            winner = 'B'
        else:
            continue  # tied speed → combat resolves, no movement adjustment
        losers = b_cells if winner == 'A' else a_cells
        for su, oc, _ in losers:
            if oc in su._moved_this_turn:
                # Loser moved this turn → revert to pre-move snapshot.
                # Historical: "the other remains in place" — slower cell
                # didn't actually advance to the contested cell; it stays at
                # the position it held at the start of the turn.
                su.cell_offsets[oc] = su._prev_offsets.get(oc, 0)
                su.cell_offsets_c[oc] = su._prev_offsets_c.get(oc, 0)
                su.cell_facing_vec[oc] = su._prev_facings.get(oc, (su.advance_dir, 0))
                n_resolved += 1
            # Loser that didn't move: nothing to revert. The mover (winner) is
            # already at this position; both cells now occupy it. This is the
            # cavalry-charge-through case (handled separately when implemented).
    return n_resolved


def find_contacts(unit_a, unit_b):
    pairs = []
    a_cells = {id(a): set(a.cells()) for a in unit_a.subunits}
    b_cells = {id(b): set(b.cells()) for b in unit_b.subunits}
    for atom_a in unit_a.subunits:
        for atom_b in unit_b.subunits:
            ca = a_cells[id(atom_a)]
            cb = b_cells[id(atom_b)]
            contact_cells_a, contact_cells_b, contact_cols = [], [], set()
            for (ra, c) in ca:
                for (rb, cb_) in cb:
                    if abs(ra-rb) <= 1 and abs(c-cb_) <= 1:
                        contact_cells_a.append((ra, c))
                        contact_cells_b.append((rb, cb_))
                        contact_cols.add((c + cb_) // 2)
            if contact_cols:
                pairs.append({"atom_a": atom_a, "atom_b": atom_b,
                               "a_cells": contact_cells_a, "b_cells": contact_cells_b,
                               "cols": list(contact_cols)})
    return pairs

def count_engagements_per_atom(pairs):
    counts = {}
    for p in pairs:
        counts[id(p["atom_a"])] = counts.get(id(p["atom_a"]), 0) + 1
        counts[id(p["atom_b"])] = counts.get(id(p["atom_b"]), 0) + 1
    return counts

def _momentum_speed(atom, contact_abs_cells):
    """F-ii: mean cell_last_speed for contact cells.
    [canonical: Jordan handoff §(2)]"""
    if not contact_abs_cells: return 0.0
    speeds = []
    op = oriented_pattern(atom.shape, atom.tier, atom.advance_dir)
    for abs_r, abs_c in contact_abs_cells:
        for orig_r, orig_c, or_r, or_c in op:
            comp_r = (atom.starting_position[0] + or_r
                      + atom.cell_offsets.get((orig_r, orig_c), 0) * atom.advance_dir)
            comp_c = (atom.starting_position[1] + or_c
                      + atom.cell_offsets_c.get((orig_r, orig_c), 0))
            if (comp_r, comp_c) == (abs_r, abs_c):
                speeds.append(atom.cell_last_speed.get((orig_r, orig_c), 0))
                break
    return sum(speeds) / len(speeds) if speeds else 0.0

def _cascade_depth_key(pair):
    """Sub-phase ordering: foremost attacker resolves first.
    [canonical: Jordan handoff §(3) — tip arrives first]"""
    atom_a = pair["atom_a"]
    a_cells = pair["a_cells"]
    if not a_cells: return 999
    if atom_a.advance_dir == -1:
        return min(r for r, c in a_cells)
    return -max(r for r, c in a_cells)

def resolve_engagements(unit_a, unit_b, pairs, dynamic_facings=None):
    """Resolve all contact pairs.
    F-i: support_engage_frac replaces bare engage_frac.
    F-ii: puncture bonus from momentum differential.
    dynamic_facings: per-cell facing dict for F-iii (None -> default advance_dir)."""
    dmg_a, dmg_b = 0, 0
    eng_counts = count_engagements_per_atom(pairs)
    for p in pairs:
        atom_a, atom_b = p["atom_a"], p["atom_b"]
        cols = p["cols"]
        primary_col = sorted(cols)[len(cols)//2]
        role_a = atom_a.role_at_contact(primary_col)
        role_b = atom_b.role_at_contact(primary_col)
        off_a = SHAPE_OFF_MOD[atom_a.shape](role_a)
        off_b = SHAPE_OFF_MOD[atom_b.shape](role_b)
        if off_a == -99 or off_b == -99: continue

        a_troops_frac = atom_a.troop_count / unit_a.total_troops()
        b_troops_frac = atom_b.troop_count / unit_b.total_troops()
        a_base = unit_a.base_combat_pool()
        b_base = unit_b.base_combat_pool()

        # F-i: support-stack-adjusted engage_frac
        a_engage_frac = support_engage_frac(atom_a, p["a_cells"])
        b_engage_frac = support_engage_frac(atom_b, p["b_cells"])

        if POOL_VARIANT == "baseline":
            a_pool_raw = a_base * a_troops_frac * a_engage_frac
            b_pool_raw = b_base * b_troops_frac * b_engage_frac
        elif POOL_VARIANT == "C-i":
            a_pool_raw = a_base * a_engage_frac
            b_pool_raw = b_base * b_engage_frac
        elif POOL_VARIANT == "C-ii":
            a_pool_raw = max(a_base * a_engage_frac * 0.5,
                             a_base * a_troops_frac * a_engage_frac)
            b_pool_raw = max(b_base * b_engage_frac * 0.5,
                             b_base * b_troops_frac * b_engage_frac)
        else:
            raise ValueError(f"Unknown POOL_VARIANT: {POOL_VARIANT}")

        a_pool = max(1, math.floor(a_pool_raw) + off_a)
        b_pool = max(1, math.floor(b_pool_raw) + off_b)

        # v11: Per-cell octagon angle — replace centroid-to-centroid with per-cell raw vectors
        # [canonical: Jordan design — octagon, GREEN<45°, YELLOW 45-90°, RED≥90°]
        # For each contact cell-pair, compute angle using defender's per-cell facing vector.
        # Average the modifier across all contact cell-pairs per side.
        def _per_cell_angle_mod(defender_subunit, defender_cells, attacker_cells):
            if not defender_cells or not attacker_cells: return 0
            # Use attacker CENTROID rather than nearest-cell to avoid non-determinism
            # when a defender cell is equidistant between attacker cells (e.g. Arrowhead tip
            # embedded between two Line rows). [canonical: Jordan design]
            atk_cr = sum(r for r,c in attacker_cells) / len(attacker_cells)
            atk_cc = sum(c for r,c in attacker_cells) / len(attacker_cells)
            atk_centroid = (atk_cr, atk_cc)
            mods = []
            op = oriented_pattern(defender_subunit.shape, defender_subunit.tier,
                                   defender_subunit.advance_dir)
            abs_to_orig = {}
            for orig_r, orig_c, or_r, or_c in op:
                abs_r = (defender_subunit.starting_position[0] + or_r
                         + defender_subunit.cell_offsets.get((orig_r, orig_c), 0)
                         * defender_subunit.advance_dir)
                abs_c = (defender_subunit.starting_position[1] + or_c
                         + defender_subunit.cell_offsets_c.get((orig_r, orig_c), 0))
                abs_to_orig[(abs_r, abs_c)] = (orig_r, orig_c)
            seen = set()
            for d_pos in defender_cells:
                if d_pos in seen: continue
                seen.add(d_pos)
                orig = abs_to_orig.get(d_pos)
                facing = (defender_subunit.get_cell_facing(*orig)
                          if orig else (defender_subunit.advance_dir, 0))
                zone, _ = octagon_angle(atk_centroid, d_pos, facing)
                mods.append(ANGLE_DEF_MOD[zone])
            return sum(mods) / len(mods) if mods else 0

        a_angle_mod = _per_cell_angle_mod(atom_a, list(set(p["a_cells"])),
                                           list(set(p["b_cells"])))
        b_angle_mod = _per_cell_angle_mod(atom_b, list(set(p["b_cells"])),
                                           list(set(p["a_cells"])))
        a_pool = max(1, a_pool + round(a_angle_mod))
        b_pool = max(1, b_pool + round(b_angle_mod))

        # F-ii: puncture bonus from speed differential
        if PUNCTURE_ENABLED:
            a_mom = _momentum_speed(atom_a, p["a_cells"])
            b_mom = _momentum_speed(atom_b, p["b_cells"])
            if a_mom > b_mom:
                a_pool += min(PUNCTURE_CAP, int(a_mom - b_mom))
            elif b_mom > a_mom:
                b_pool += min(PUNCTURE_CAP, int(b_mom - a_mom))

        # Encirclement
        if eng_counts.get(id(atom_a), 0) >= 2: a_pool = max(1, a_pool - ENCIRCLEMENT_PENALTY)
        if eng_counts.get(id(atom_b), 0) >= 2: b_pool = max(1, b_pool - ENCIRCLEMENT_PENALTY)

        # v11: Ranged melee penalty — ranged units at contact fight with halved pool.
        # Historical: archers in hand-to-hand use secondary weapons, significantly less
        # effective than dedicated infantry. [canonical: Jordan design]
        # v12: Ranged melee penalty strengthened from pool//2 to pool//3.
        # Historical: archers in hand-to-hand were near-useless. At Agincourt, the
        # English archers played minor role in melee; their decisive contribution was
        # ranged. Heavy melee infantry (men-at-arms) decided close combat.
        # [canonical: references/historical/precedents_warfare.md — Agincourt 1415,
        #  Crécy 1346: archer melee performance documented as marginal]
        if atom_a.unit_type == 'ranged': a_pool = max(1, a_pool // 3)
        if atom_b.unit_type == 'ranged': b_pool = max(1, b_pool // 3)

        a_net = roll_pool(a_pool)
        b_net = roll_pool(b_pool)
        a_deg = compute_degree(a_net, max(1, b_net))
        b_deg = compute_degree(b_net, max(1, a_net))
        dmg_a += max(0, DAMAGE_BY_DEGREE[b_deg](unit_b.power) - unit_a.dr)
        dmg_b += max(0, DAMAGE_BY_DEGREE[a_deg](unit_a.power) - unit_b.dr)
    return {"dmg_a": dmg_a, "dmg_b": dmg_b, "engagements": len(pairs)}

def resolve_engagements_cascading(unit_a, unit_b, pairs):
    """F-iii: cascading sub-phase resolution with facing rotation.
    [canonical: Jordan handoff §(3)]

    Contacts sorted by attacker depth (tip first). Each sub-phase resolves
    one depth group, then rotates engaged cells' facings toward their attacker.
    Later sub-phases see FLANK/REAR angles on already-rotated cells.
    Effect requires tight formation (TIP_SUPPORT_GAP=1 or 2) so multiple
    Arrowhead rows are simultaneously adjacent to Line cells."""
    if not CASCADING_ENABLED:
        return resolve_engagements(unit_a, unit_b, pairs)

    dynamic_facings = _init_dynamic_facings(unit_a, unit_b)
    total_dmg_a = total_dmg_b = 0
    resolved_keys = set()

    # Sort by attacker depth; group into sub-phases by proximity (1-row buckets)
    sorted_pairs = sorted(pairs, key=_cascade_depth_key)
    if not sorted_pairs:
        return {"dmg_a": 0, "dmg_b": 0, "engagements": 0}

    groups = []
    cur_group = [sorted_pairs[0]]
    cur_depth = _cascade_depth_key(sorted_pairs[0])
    for p in sorted_pairs[1:]:
        d = _cascade_depth_key(p)
        if abs(d - cur_depth) <= 1:
            cur_group.append(p)
        else:
            groups.append(cur_group)
            cur_group = [p]
            cur_depth = d
    groups.append(cur_group)

    total_engagements = 0
    for sub_idx, group in enumerate(groups):
        if sub_idx >= MAX_SUB_PHASES:
            break
        active = [p for p in group
                  if (id(p["atom_a"]), id(p["atom_b"])) not in resolved_keys]
        if not active:
            continue
        result = resolve_engagements(unit_a, unit_b, active, dynamic_facings)
        total_dmg_a += result["dmg_a"]
        total_dmg_b += result["dmg_b"]
        total_engagements += result["engagements"]
        for p in active:
            resolved_keys.add((id(p["atom_a"]), id(p["atom_b"])))
            # Rotate engaged cells toward their opponents
            _rotate_defender_facing(p["atom_b"], p["b_cells"], p["a_cells"], dynamic_facings)
            _rotate_defender_facing(p["atom_a"], p["a_cells"], p["b_cells"], dynamic_facings)

    return {"dmg_a": total_dmg_a, "dmg_b": total_dmg_b, "engagements": total_engagements}

# ─── VOLLEY (Phase 2 — ranged fire at distance) ──────────────────────────────
# [canonical: mass_battle_v30.md §A.7 Phase 2 — Volley fires before Manoeuvre.
#  PP-503: Volley pool = Power dice vs TN 6. Net successes − ranged DR = Size loss.
#  Damage recorded in Phase 2 but APPLIED at Phase 6 Step 1 (simultaneous with engagement).]

def _atom_distance(atom_a, atom_b):
    """Chebyshev (king-move) distance between nearest cells of two atoms."""
    cells_a = atom_a.cells()
    cells_b = atom_b.cells()
    if not cells_a or not cells_b:
        return float('inf')
    best = float('inf')
    for (ra, ca) in cells_a:
        for (rb, cb) in cells_b:
            d = max(abs(ra - rb), abs(ca - cb))
            if d < best:
                best = d
                if best == 0:
                    return 0
    return best


def _roll_volley_pool(power_dice):
    """Roll power_dice d10s vs TN=VOLLEY_TN. Returns net successes (count of d>=TN)
    with the standard fumble/crit: 1 = -1 net, 10 = +2 net.
    [canonical: mass_battle_v30.md §A.1 dice engine — TN-based successes, 1=-1, 10=+2]
    """
    if power_dice <= 0:
        return 0
    net = 0
    for _ in range(power_dice):
        roll = random.randint(1, 10)
        if roll == 1:
            net -= 1
        elif roll == 10:
            net += 2
        elif roll >= VOLLEY_TN:
            net += 1
    return max(0, net)  # floor at 0; PP-273 minimum pool is for engagement, not volley result


def volley_phase(unit_a, unit_b):
    """Phase 2 Volley. Each ranged atom selects nearest in-range enemy atom and fires.
    Returns dict of total Size-loss to each side (applied simultaneously at end of turn).
    Pool = Power; TN = VOLLEY_TN; ranged DR subtracts from net successes.
    [canonical: mass_battle_v30.md §A.7 Phase 2 Volley; params/mass_combat.md §Ranged DR Table]
    """
    if not VOLLEY_ENABLED:
        return {"loss_a": 0, "loss_b": 0, "shots": 0}

    loss_a = loss_b = 0
    shots = 0

    def fire(shooter_atom, shooter_unit, target_atoms):
        """Pick nearest in-range target atom, roll Power vs TN, return Size loss inflicted."""
        if shooter_atom.unit_type != "ranged":
            return 0, None
        best_target = None
        best_dist = float('inf')
        for t in target_atoms:
            d = _atom_distance(shooter_atom, t)
            if VOLLEY_MIN_RANGE <= d <= VOLLEY_MAX_RANGE and d < best_dist:
                best_dist = d
                best_target = t
        if best_target is None:
            return 0, None
        # Pool = unit Power dice (PP-503). Discipline penalty applies (per §A.4).
        pool = max(1, shooter_unit.power - shooter_unit.discipline_penalty_volley())
        net = _roll_volley_pool(pool)
        # DR subtracts from net successes (Ranged DR Table)
        net_after_dr = max(0, net - RANGED_DR_DEFAULT)
        return net_after_dr, best_target

    for atom in unit_a.subunits:
        dmg, tgt = fire(atom, unit_a, unit_b.subunits)
        if tgt is not None:
            loss_b += dmg
            shots += 1
    for atom in unit_b.subunits:
        dmg, tgt = fire(atom, unit_b, unit_a.subunits)
        if tgt is not None:
            loss_a += dmg
            shots += 1

    return {"loss_a": loss_a, "loss_b": loss_b, "shots": shots}


# ─── BATTLE ──────────────────────────────────────────────────────────────────

def run_battle(unit_a, unit_b, max_turns=18):
    """Run one engagement turn (up to 3 phases = 18 ticks).
    v16: max_turns=18 = one battle turn's engagement cap (3 phases).
    Multi-turn battles call this repeatedly with persistent unit state.
    [canonical: Jordan direction — "limit of three phases per simultaneous
     engagement per turn"]

    Returns:
      {"winner": "A"|"B"|"draw", "turns": int, "phases": int, "tick_in_phase": int}
    """
    turns = 0
    current_phase = 0
    for t in range(1, max_turns + 1):
        turns = t
        if unit_a.routed or unit_b.routed: break
        # Phase 2 — Volley. Ranged atoms fire at range BEFORE movement.
        # Damage accumulated here, applied with Phase 5 damage at end of turn.
        # [canonical: mass_battle_v30.md §A.7 Phase 2; PP-503]
        vol = volley_phase(unit_a, unit_b)
        volley_dmg_a = vol["loss_a"]
        volley_dmg_b = vol["loss_b"]
        # Pre-movement contacts -> halt
        pre_pairs = find_contacts(unit_a, unit_b)
        for atom in unit_a.subunits + unit_b.subunits:
            atom.halted_cells = set()
        for p in pre_pairs:
            op_a = oriented_pattern(p["atom_a"].shape, p["atom_a"].tier, p["atom_a"].advance_dir)
            for cell in p["a_cells"]:
                for orig_r, orig_c, or_r, or_c in op_a:
                    abs_r = (p["atom_a"].starting_position[0] + or_r
                             + p["atom_a"].cell_offsets.get((orig_r,orig_c), 0) * p["atom_a"].advance_dir)
                    abs_c = (p["atom_a"].starting_position[1] + or_c
                             + p["atom_a"].cell_offsets_c.get((orig_r,orig_c), 0))
                    if (abs_r, abs_c) == cell:
                        p["atom_a"].halted_cells.add((orig_r, orig_c)); break
            op_b = oriented_pattern(p["atom_b"].shape, p["atom_b"].tier, p["atom_b"].advance_dir)
            for cell in p["b_cells"]:
                for orig_r, orig_c, or_r, or_c in op_b:
                    abs_r = (p["atom_b"].starting_position[0] + or_r
                             + p["atom_b"].cell_offsets.get((orig_r,orig_c), 0) * p["atom_b"].advance_dir)
                    abs_c = (p["atom_b"].starting_position[1] + or_c
                             + p["atom_b"].cell_offsets_c.get((orig_r,orig_c), 0))
                    if (abs_r, abs_c) == cell:
                        p["atom_b"].halted_cells.add((orig_r, orig_c)); break
        assign_targets(unit_a, unit_b)
        b_cells_set = set(c for sub in unit_b.subunits for c in sub.cells())
        a_cells_set = set(c for sub in unit_a.subunits for c in sub.cells())
        # v21: SIMULTANEOUS RESOLUTION — cache all target centroids BEFORE any
        # atom moves. Without this, unit_a advances toward unit_b's pre-move
        # centroid, but unit_b advances toward unit_a's POST-move centroid,
        # creating ~10% first-arg bias. With caching, both sides see each
        # other's pre-move positions symmetrically.
        # [canonical: params/mass_combat.md PP-233 — "Damage is simultaneous"]
        cached_centroids = {}
        for atom in unit_a.subunits + unit_b.subunits:
            if atom.target_atom:
                cached_centroids[id(atom)] = atom.target_atom.centroid()
        for atom in unit_a.subunits:
            if atom.target_atom:
                atom.advance_cells(unit_a.discipline, cached_centroids[id(atom)],
                                   enemy_cells=b_cells_set)
        for atom in unit_b.subunits:
            if atom.target_atom:
                atom.advance_cells(unit_b.discipline, cached_centroids[id(atom)],
                                   enemy_cells=a_cells_set)
        # v11: vector halt-at-contact — prevent over-run that creates paradoxical angles
        for atom in unit_a.subunits: atom.halt_before_enemy(unit_b)
        for atom in unit_b.subunits: atom.halt_before_enemy(unit_a)
        # v13: cross-side cell contention (speed → size → random priority).
        # After both sides have advanced, cells from opposing sides may occupy the
        # same abs position. Resolve per Jordan design 2026-05-12: higher-speed
        # cell wins; tie → greater size; tie → random. Losers that moved this turn
        # revert; static losers shift back 1 step ("end-of-phase displacement").
        # [canonical: Jordan design 2026-05-12 — same-cell contention rules]
        resolve_cross_side_contention(unit_a, unit_b)
        # v13: within-side discipline-gated formation hold (Subunit method
        # resolve_internal_collisions) is implemented but not invoked here —
        # it over-tuned battery (12/13 -> 9/13). Left available for future use
        # when paired with a proper bad-facing trigger.
        pairs = find_contacts(unit_a, unit_b)
        # v20: stamina drain proportional to cells in contact (bottom-up).
        # More front-line cells fighting = more exhaustion. Emergent from formation.
        if pairs:
            for u in [unit_a, unit_b]:
                if u.routed:
                    continue
                cells_in_contact = 0
                for p in pairs:
                    if p.get('atom_a') in u.subunits:
                        cells_in_contact += len(p.get('a_cells', []))
                    elif p.get('atom_b') in u.subunits:
                        cells_in_contact += len(p.get('b_cells', []))
                drain = max(1, cells_in_contact) * STAMINA_DRAIN_PER_CONTACT_CELL
                u.stamina = max(0, u.stamina - drain)
        result = (resolve_engagements_cascading(unit_a, unit_b, pairs)
                  if CASCADING_ENABLED
                  else resolve_engagements(unit_a, unit_b, pairs))
        sz_a, sz_b = unit_a.size, unit_b.size
        # Apply Phase 2 Volley + Phase 5 Engagement damage simultaneously at Phase 6 Step 1
        # [canonical: mass_battle_v30.md §A.7 — Volley/Thread/Engagement damage applied together]
        total_dmg_a_turn = result["dmg_a"] + volley_dmg_a
        total_dmg_b_turn = result["dmg_b"] + volley_dmg_b
        # v12: Volley size-loss → hp uses ceil(h_per_size / 2), not full h_per_size.
        # Bottom-up rationale: a ranged "size loss" represents arrows finding targets in
        # the formation; many hits glance off shields/armor. Melee size loss represents
        # men killed in close combat, where wounds are decisive. Halving the conversion
        # captures that volley size loss is less lethal per unit than melee size loss.
        # Reduces R1 (Ranged vs Line) without breaking R3 (mirror — same scaling on both sides).
        # [canonical: Jordan design 2026-05-12 — volley hp scaling tuned for historical match]
        volley_hp_scale = lambda u: max(1, (u.h_per_size + 1) // 2)
        # v20: scale engagement damage by contact fraction.
        # More cells in contact = more soldiers fighting = more damage dealt.
        # Bottom-up: the envelopment advantage EMERGES from having more cells engaged.
        # contact_fraction = cells_in_contact / total_cells. Capped at 1.0.
        if pairs:
            for u, dmg_key in [(unit_a, "dmg_a"), (unit_b, "dmg_b")]:
                cells_in_contact = set()
                total_cells = 0
                for sub in u.subunits:
                    total_cells += len(list(sub.cells()))
                    for p in pairs:
                        if p.get('atom_a') is sub:
                            cells_in_contact.update(p.get('a_cells', []))
                        elif p.get('atom_b') is sub:
                            cells_in_contact.update(p.get('b_cells', []))
                # The OPPONENT's contact fraction scales their damage against us
                # More of the opponent's troops fighting = more damage TO us
                opp = unit_b if u is unit_a else unit_a
                opp_cells_contact = set()
                opp_total = 0
                for sub in opp.subunits:
                    opp_total += len(list(sub.cells()))
                    for p in pairs:
                        if p.get('atom_a') is sub:
                            opp_cells_contact.update(p.get('a_cells', []))
                        elif p.get('atom_b') is sub:
                            opp_cells_contact.update(p.get('b_cells', []))
                # Scale damage: opponent's contact fraction → damage to us
                opp_frac = len(opp_cells_contact) / max(1, opp_total)
                result[dmg_key] = result[dmg_key] * max(0.2, opp_frac)
        # v21: SIMULTANEOUS HP — apply damage to both units, THEN recalc_size
        # for both. Prevents size recalc of unit_a from affecting anything
        # before unit_b's damage is applied.
        # [canonical: params/mass_combat.md PP-233 — "Damage is simultaneous.
        #  Both sides deal and receive damage before Size is recalculated."]
        unit_a.hp = max(0, unit_a.hp - result["dmg_a"] - volley_dmg_a * volley_hp_scale(unit_a))
        unit_b.hp = max(0, unit_b.hp - result["dmg_b"] - volley_dmg_b * volley_hp_scale(unit_b))
        unit_a.recalc_size()
        unit_b.recalc_size()
        # v18: discipline degradation moved to phase_boundary (D-6).
        # Per-tick integer Size changes are rare at TroopCount HP scale.
        # check_drift still runs per-tick for formation coherence.
        for u in [unit_a, unit_b]:
            if not u.routed and not u.broken:
                u.check_drift()
        # v21: SIMULTANEOUS MORALE — compute erosion for both units, then
        # check rout for both. Prevents ordering from affecting which unit
        # routs first within a single tick.
        # [canonical: designs/provincial/mass_battle_v30.md §A.4 — generalship]
        total_dmg_a_morale = result.get("dmg_a", 0) + volley_dmg_a * volley_hp_scale(unit_a)
        total_dmg_b_morale = result.get("dmg_b", 0) + volley_dmg_b * volley_hp_scale(unit_b)
        for u, total_dmg in [(unit_a, total_dmg_a_morale), (unit_b, total_dmg_b_morale)]:
            if u.routed: continue
            # General death: Command=0 → instant rout (M1: general IS the army)
            # [canonical: designs/provincial/mass_battle_v30.md §A.4 — "General killed: Morale −2 (uncapped)"]
            if u.command <= 0:
                u.morale = 0.0
                continue  # rout check below
            if total_dmg > 0 and u.discipline > 0:
                erosion = total_dmg / (u.discipline * u.command)
                u.morale -= erosion
        # Rout check AFTER both erosions applied
        for u in [unit_a, unit_b]:
            if not u.routed and u.morale <= 0:
                u.routed = True
        # v15: phase boundary — stamina_check, morale_check_phase, rout_resolution
        # are now populated (G-1 + G-2). rally/reform/threadwork remain empty.
        if t % TICKS_PER_PHASE == 0:
            current_phase += 1
            phase_boundary(unit_a, unit_b, current_phase)
    winner = ("A" if not unit_a.routed and unit_b.routed else
              "B" if not unit_b.routed and unit_a.routed else "draw")
    tick_in_phase = turns % TICKS_PER_PHASE if turns else 0
    return {"winner": winner, "turns": turns,
            "phases": current_phase, "tick_in_phase": tick_in_phase,
            "a_stamina": unit_a.stamina, "b_stamina": unit_b.stamina,
            "a_hp_pct": round(unit_a.hp / unit_a.hp_max * 100, 1) if unit_a.hp_max else 0,
            "b_hp_pct": round(unit_b.hp / unit_b.hp_max * 100, 1) if unit_b.hp_max else 0,
            "a_morale": unit_a.morale, "b_morale": unit_b.morale}

# ─── MULTI-TURN BATTLE ORCHESTRATOR (D-1, D-9) ─────────────────────────────
# Models a multi-turn battle: each turn = one 3-phase engagement (run_battle).
# Between turns: units disengage, partial stamina recovery, state persists.
# [canonical: Jordan direction — "we have a bunch of turns throughout the mass
#  battle system. 5 turns in a row attacking. limit of 3 phases per engagement"]

# Between-turn recovery rules (D-9):
# [ASSUMPTION: between-turn recovery constants are tuning parameters —
#  basis: no canonical source specifies inter-turn recovery rates]
# [canonical: params/mass_combat.md §PP-712 — "Discipline persists between battles"]
BETWEEN_TURN_STAMINA_RECOVERY = 30  # partial rest during disengagement
BETWEEN_TURN_MORALE_RECOVERY = 0    # morale does NOT recover between turns
# HP does NOT recover between turns (casualties are permanent within a battle)
# Discipline persists (canonical PP-712)
# [canonical: designs/provincial/mass_battle_v30.md §A.4 — "Morale reset between battles"]


def between_turn_recovery(unit):
    """Apply between-turn state changes. Called after each engagement turn.
    [canonical: params/mass_combat.md §PP-712 — discipline persists]"""
    if unit.routed or unit.broken:
        return
    unit.stamina = min(unit.stamina_max, unit.stamina + BETWEEN_TURN_STAMINA_RECOVERY)
    unit.morale = min(unit.morale_start, unit.morale + BETWEEN_TURN_MORALE_RECOVERY)


def reset_positions(unit, shape, anchor_map):
    """Reset subunit positions for re-engagement after disengagement.
    Units return to their starting rows for fresh approach."""
    start_row = SIDE_A_START_ROW if unit.faction == 'A' else SIDE_B_START_ROW
    anchor_col = anchor_map.get((shape, unit.subunits[0].tier), 10)
    for atom in unit.subunits:
        atom.starting_position = (start_row, anchor_col)
        atom.cell_offsets = {}
        atom.cell_offsets_c = {}


def run_multi_turn_battle(unit_a, unit_b, shape_a, shape_b, anchor_map,
                          max_battle_turns=8):
    """Run a multi-turn battle. Each turn = 3 phases of engagement.
    Returns list of per-turn result dicts + final outcome.
    [canonical: Jordan direction — 5-8 turns per battle, 3 phases per turn]"""
    log = []
    for battle_turn in range(1, max_battle_turns + 1):
        hp_a_before = unit_a.hp
        hp_b_before = unit_b.hp

        # Reset positions for re-engagement
        reset_positions(unit_a, shape_a, anchor_map)
        reset_positions(unit_b, shape_b, anchor_map)

        # Run one engagement turn (3 phases max)
        # v21: alternating swap removed — simultaneous resolution makes
        # run_battle symmetric regardless of argument order.
        r = run_battle(unit_a, unit_b)

        a_loss_turn = (hp_a_before - unit_a.hp) / unit_a.hp_max if unit_a.hp_max else 0
        b_loss_turn = (hp_b_before - unit_b.hp) / unit_b.hp_max if unit_b.hp_max else 0
        a_loss_cum = 1.0 - (unit_a.hp / unit_a.hp_max) if unit_a.hp_max else 1.0
        b_loss_cum = 1.0 - (unit_b.hp / unit_b.hp_max) if unit_b.hp_max else 1.0

        log.append({
            'turn': battle_turn,
            'a_loss_turn': a_loss_turn, 'b_loss_turn': b_loss_turn,
            'a_loss_cum': a_loss_cum, 'b_loss_cum': b_loss_cum,
            'a_pool': unit_a.base_combat_pool(), 'b_pool': unit_b.base_combat_pool(),
            'a_eff_size': unit_a.effective_size, 'b_eff_size': unit_b.effective_size,
            'a_morale': unit_a.morale, 'b_morale': unit_b.morale,
            'a_stamina': unit_a.stamina, 'b_stamina': unit_b.stamina,
            'a_routed': unit_a.routed, 'b_routed': unit_b.routed,
            'ticks': r['turns'], 'phases': r['phases'],
        })

        if unit_a.routed or unit_b.routed:
            break

        # Between-turn recovery
        between_turn_recovery(unit_a)
        between_turn_recovery(unit_b)

    # Determine winner
    if unit_a.routed and not unit_b.routed:
        winner = 'B'
    elif unit_b.routed and not unit_a.routed:
        winner = 'A'
    else:
        winner = 'draw'

    return {
        'winner': winner,
        'battle_turns': len(log),
        'log': log,
        'a_loss_final': 1.0 - (unit_a.hp / unit_a.hp_max) if unit_a.hp_max else 1.0,
        'b_loss_final': 1.0 - (unit_b.hp / unit_b.hp_max) if unit_b.hp_max else 1.0,
    }


# ─── PURSUIT (G-11, v22) ─────────────────────────────────────────────────────
# [canonical: designs/provincial/mass_battle_v30.md §A.12-514]
# "Pursuit: Fast units only. Routing unit loses Size equal to pursuer net
#  Offence successes (no Defence) each turn. Recall: Command Ob 2."
# "Routing: Slow/Standard cannot fight back. Fast may rearguard at −2D Off."
REARGUARD_PENALTY = 2  # [canonical: §A.12 — "Fast may rearguard at −2D Off"]
RECALL_OB = 2  # [canonical: §A.12 — "Recall: Command Ob 2"]


def pursuit_damage(pursuer, routing_unit):
    """Fast pursuer attacks routing unit. Routing unit has no defence
    unless it is also Fast (rearguard at -2D Off).
    Returns HP damage dealt.
    [canonical: designs/provincial/mass_battle_v30.md §A.12]"""
    if pursuer.speed != "Fast":
        return 0  # Only Fast units can pursue
    if pursuer.routed or pursuer.broken:
        return 0
    if not routing_unit.routed:
        return 0

    # [canonical: params/mass_combat.md PP-233 — Pool = min(Size,Cmd)+Cmd]
    a_pool = pursuer.base_combat_pool()
    a_net = roll_pool(a_pool)

    # Fast routing unit may rearguard at -2D Off
    # [canonical: §A.12 — "Fast may rearguard at −2D Off"]
    if routing_unit.speed == "Fast":
        rg_pool = max(1, routing_unit.base_combat_pool() - REARGUARD_PENALTY)
        rg_net = roll_pool(rg_pool)
        # Rearguard acts as partial defence — reduce pursuer net
        a_net = max(0, a_net - max(0, rg_net))

    # No defence roll for Slow/Standard routing units
    # [canonical: §A.12 — "Slow/Standard cannot fight back"]

    # Damage = net successes × (1 + Power), minus DR
    # [canonical: params/mass_combat.md PP-233]
    if a_net <= 0:
        return 0
    raw_dmg = a_net * (1 + pursuer.power)
    dmg = max(0, raw_dmg - routing_unit.dr)
    return dmg


def recall_check(pursuer):
    """General attempts to recall pursuing unit. Command Ob 2.
    Returns True if recalled (pursuit stops).
    [canonical: designs/provincial/mass_battle_v30.md §A.12]"""
    net = roll_pool(pursuer.command)
    return net >= RECALL_OB


# ─── MULTI-UNIT BATTLE ORCHESTRATOR (D-3, D-5, v22) ──────────────────────────
# Models battles with multiple units per side. Each engagement pair runs through
# run_battle (1v1). After all pairs resolve: morale cascade, rout contagion,
# freed-attacker flanking. Between turns: recovery.
# [canonical: designs/provincial/mass_battle_v30.md §A.12 — Morale Cascade,
#  Rout contagion brake, pursuit rules]

# v22: Morale cascade discipline check — Ob 1, fires at Phase 6 Step 3
# [canonical: §A.12 — "all friendly units in the same engagement make a
#  Discipline check (Ob 1). Failure: Morale −1"]
MORALE_CASCADE_OB = 1  # [canonical: designs/provincial/mass_battle_v30.md §A.12]
ROUT_CONTAGION_MORALE_HIT = 1  # [canonical: designs/provincial/mass_battle_v30.md L167]
FREED_ATTACKER_FLANK_PENALTY = 1  # [canonical: §A.4 octagon YELLOW = -1D]


def discipline_check_cascade(unit):
    """Discipline check Ob 1 for morale cascade.
    Returns True if unit PASSES (resists cascade).
    [canonical: designs/provincial/mass_battle_v30.md §A.12 — Ob 1 check]"""
    # [canonical: params/mass_combat.md — roll_pool uses TN 7 default]
    net = roll_pool(unit.discipline)
    return net >= MORALE_CASCADE_OB


def freed_attacker_damage(freed_unit, target_unit):
    """Freed unit attacks target from the flank.
    The freed unit rolls its full pool. Target defends at -1D (flank).
    Returns damage dealt to target.
    [canonical: designs/provincial/mass_battle_v30.md §A.12 — implied by
     rout freeing the victor to attack adjacent enemies]"""
    if freed_unit.routed or freed_unit.broken:
        return 0
    if target_unit.routed or target_unit.broken:
        return 0
    # [canonical: params/mass_combat.md PP-233 — Pool = min(Size,Cmd)+Cmd]
    a_pool = freed_unit.base_combat_pool()
    # [canonical: designs/provincial/mass_battle_v30.md §A.4 — YELLOW zone -1D]
    b_pool = max(1, target_unit.base_combat_pool() - FREED_ATTACKER_FLANK_PENALTY)
    a_net = roll_pool(a_pool)
    b_net = roll_pool(b_pool)
    a_deg = compute_degree(a_net, max(1, b_net))
    # [canonical: params/mass_combat.md PP-233 — Damage = successes × (1+Power)]
    dmg = max(0, DAMAGE_BY_DEGREE[a_deg](freed_unit.power) - target_unit.dr)
    return dmg


def run_multi_unit_battle(side_a, side_b, pairings, shapes_a, shapes_b,
                          anchor_map, max_battle_turns=8):
    """Run a multi-unit battle with morale cascade and freed-attacker.

    Args:
        side_a: list of Unit objects for side A
        side_b: list of Unit objects for side B
        pairings: list of (a_idx, b_idx) — initial engagement pairings.
            Indices into side_a / side_b. Pairs are ordered spatially
            (adjacent pairs = adjacent on battlefield).
        shapes_a, shapes_b: dicts {unit_idx: shape_name}
        anchor_map: position anchor mapping for reset_positions
        max_battle_turns: turn cap

    Returns: dict with winner ('A'|'B'|'draw'), per-turn log, casualties.
    [canonical: designs/provincial/mass_battle_v30.md §A.12 — Morale Cascade,
     Rout contagion brake; Phase 6 Steps 1-3]
    """
    log = []
    # Track active pairings and freed units
    active_pairs = list(range(len(pairings)))
    freed_units = []  # (unit, owner_side, source_pair_idx)
    pursuing_units = []  # (pursuer, routing_unit, pursuer_side, source_pair_idx)

    for battle_turn in range(1, max_battle_turns + 1):
        turn_log = {
            'turn': battle_turn,
            'engagements': [],
            'cascades': [],
            'freed_attacks': [],
            'pursuits': [],
            'routs_this_turn': [],
        }

        # ── Pursuit phase: Fast units pursuing routing enemies ──
        # [canonical: §A.12 L513 — "Routing unit loses Size equal to pursuer
        #  net Offence successes (no Defence) each turn."]
        for pursuer, routing, p_side, p_pair in list(pursuing_units):
            if routing.hp <= 0:
                # Routing unit destroyed — pursuer becomes freed
                pursuing_units.remove((pursuer, routing, p_side, p_pair))
                freed_units.append((pursuer, p_side, p_pair))
                continue
            # Recall check — general tries to pull unit back
            # [canonical: §A.12 — "Recall: Command Ob 2"]
            if recall_check(pursuer):
                pursuing_units.remove((pursuer, routing, p_side, p_pair))
                freed_units.append((pursuer, p_side, p_pair))
                turn_log['pursuits'].append({
                    'pursuer': pursuer.name, 'target': routing.name,
                    'damage': 0, 'recalled': True,
                })
                continue
            # Pursuit damage
            dmg = pursuit_damage(pursuer, routing)
            if dmg > 0:
                routing.hp = max(0, routing.hp - dmg)
                routing.recalc_size()
            turn_log['pursuits'].append({
                'pursuer': pursuer.name, 'target': routing.name,
                'damage': dmg, 'recalled': False,
            })
            if routing.hp <= 0:
                pursuing_units.remove((pursuer, routing, p_side, p_pair))
                freed_units.append((pursuer, p_side, p_pair))

        # ── Phase: run each active engagement ──
        # [canonical: designs/provincial/mass_battle_v30.md — Phase 2-5 per pair]
        for pair_idx in list(active_pairs):
            a_idx, b_idx = pairings[pair_idx]
            ua, ub = side_a[a_idx], side_b[b_idx]
            if ua.routed or ub.routed:
                continue

            # Reset positions for this turn's engagement
            reset_positions(ua, shapes_a[a_idx], anchor_map)
            reset_positions(ub, shapes_b[b_idx], anchor_map)

            # Run 3-phase engagement
            r = run_battle(ua, ub)
            turn_log['engagements'].append({
                'pair': pair_idx, 'a_idx': a_idx, 'b_idx': b_idx,
                'result': r['winner'], 'ticks': r['turns'],
            })

        # ── Freed-attacker bonus damage (from PREVIOUS turn's freed units) ──
        # [canonical: §A.12 — freed unit attacks adjacent enemy from flank]
        for freed_unit, owner_side, source_pair in list(freed_units):
            if freed_unit.routed or freed_unit.broken:
                freed_units.remove((freed_unit, owner_side, source_pair))
                continue
            # Find adjacent active engagement with an enemy to flank
            target = None
            for adj_offset in [-1, 1]:
                adj_pair = source_pair + adj_offset
                if adj_pair not in active_pairs:
                    continue
                a_idx, b_idx = pairings[adj_pair]
                if owner_side == 'A':
                    # Freed A unit flanks the B unit in adjacent pair
                    enemy = side_b[b_idx]
                else:
                    # Freed B unit flanks the A unit in adjacent pair
                    enemy = side_a[a_idx]
                if not enemy.routed and not enemy.broken:
                    target = enemy
                    break

            if target:
                dmg = freed_attacker_damage(freed_unit, target)
                if dmg > 0:
                    # [canonical: params/mass_combat.md PP-233 — simultaneous damage]
                    target.hp = max(0, target.hp - dmg)
                    target.recalc_size()
                    # Morale erosion from flanking damage
                    # [canonical: designs/provincial/mass_battle_v30.md §A.4]
                    if target.discipline > 0 and target.command > 0:
                        erosion = dmg / (target.discipline * target.command)
                        target.morale -= erosion
                    if target.morale <= 0:
                        target.routed = True
                    turn_log['freed_attacks'].append({
                        'freed': freed_unit.name, 'target': target.name,
                        'damage': dmg,
                    })

        # ── Check for new routs ──
        newly_routed = []
        for pair_idx in active_pairs:
            a_idx, b_idx = pairings[pair_idx]
            ua, ub = side_a[a_idx], side_b[b_idx]
            if ua.routed:
                newly_routed.append(('A', a_idx, pair_idx))
            if ub.routed:
                newly_routed.append(('B', b_idx, pair_idx))
        turn_log['routs_this_turn'] = [(s, i) for s, i, _ in newly_routed]

        # ── Phase 6 Step 3: Morale Cascade ──
        # [canonical: designs/provincial/mass_battle_v30.md §A.12]
        for routed_side, routed_idx, pair_idx in newly_routed:
            # All friendly units in the SAME engagement check Discipline Ob 1
            a_idx, b_idx = pairings[pair_idx]
            if routed_side == 'A':
                # Check other A units in this pair (for future 2v1 support)
                # For now, same-engagement only has one unit per side
                pass
            else:
                pass
            # Adjacent friendly units: rout contagion (-1, braked)
            # [canonical: designs/provincial/mass_battle_v30.md L167]
            for adj_offset in [-1, 1]:
                adj_pair = pair_idx + adj_offset
                if adj_pair < 0 or adj_pair >= len(pairings):
                    continue
                if adj_pair not in active_pairs:
                    continue
                adj_a, adj_b = pairings[adj_pair]
                if routed_side == 'A':
                    friend = side_a[adj_a]
                else:
                    friend = side_b[adj_b]
                if friend.routed:
                    continue
                # Morale cascade: Discipline check Ob 1
                if not discipline_check_cascade(friend):
                    friend.morale -= 1
                    turn_log['cascades'].append({
                        'unit': friend.name, 'trigger': f'{routed_side}{routed_idx} routed',
                        'result': 'failed — morale -1',
                    })
                else:
                    turn_log['cascades'].append({
                        'unit': friend.name, 'trigger': f'{routed_side}{routed_idx} routed',
                        'result': 'passed',
                    })
                # Rout contagion: additional -1, braked
                # [canonical: L167 — "Rout causes −1 Morale to adjacent units"]
                friend.morale -= ROUT_CONTAGION_MORALE_HIT
                # Brake: this morale loss cannot cause rout this turn
                # (rout check deferred to next turn's engagement resolution)

        # ── Freed-attacker: victor from resolved pair becomes free ──
        # v22/G-11: Fast victors PURSUE routing unit (§A.12). Non-Fast join adjacent.
        for routed_side, routed_idx, pair_idx in newly_routed:
            a_idx, b_idx = pairings[pair_idx]
            victor = None
            routing = None
            if routed_side == 'A' and not side_b[b_idx].routed:
                victor = side_b[b_idx]
                routing = side_a[a_idx]
                victor_side = 'B'
            elif routed_side == 'B' and not side_a[a_idx].routed:
                victor = side_a[a_idx]
                routing = side_b[b_idx]
                victor_side = 'A'

            if victor:
                if victor.speed == "Fast" and routing.hp > 0:
                    # Fast unit pursues — track for ongoing pursuit
                    # [canonical: §A.12 L513 — "Pursuit: Fast units only"]
                    pursuing_units.append((victor, routing, victor_side, pair_idx))
                else:
                    # Non-Fast: freed attacker joins adjacent engagement
                    freed_units.append((victor, victor_side, pair_idx))

        # ── Remove resolved pairs ──
        active_pairs = [p for p in active_pairs
                        if not (side_a[pairings[p][0]].routed or
                                side_b[pairings[p][1]].routed)]

        # ── Log state ──
        turn_log['active_pairs'] = len(active_pairs)
        turn_log['freed_count'] = len(freed_units)
        turn_log['pursuing_count'] = len(pursuing_units)
        for side, units in [('A', side_a), ('B', side_b)]:
            for i, u in enumerate(units):
                turn_log[f'{side}{i}_hp'] = round(u.hp / u.hp_max * 100, 1) if u.hp_max else 0
                turn_log[f'{side}{i}_morale'] = round(u.morale, 3)
                turn_log[f'{side}{i}_routed'] = u.routed
        log.append(turn_log)

        # ── Check termination ──
        # [canonical: §A.12 — pursuit continues until recall or routing unit destroyed]
        # Battle ends when: both sides fully routed, OR no activity remains
        # (no active pairs, no pursuit, no freed attackers with targets)
        a_all_routed = all(u.routed for u in side_a)
        b_all_routed = all(u.routed for u in side_b)
        if a_all_routed and b_all_routed:
            break  # mutual rout — no one left to pursue
        if not active_pairs and not pursuing_units:
            # No engagements and no pursuit — freed attackers can't do anything
            break

        # ── Between-turn recovery ──
        for u in side_a + side_b:
            if not u.routed:
                between_turn_recovery(u)

    # ── Determine winner ──
    a_surviving = sum(1 for u in side_a if not u.routed)
    b_surviving = sum(1 for u in side_b if not u.routed)
    if a_surviving > b_surviving:
        winner = 'A'
    elif b_surviving > a_surviving:
        winner = 'B'
    else:
        winner = 'draw'

    return {
        'winner': winner,
        'battle_turns': len(log),
        'log': log,
        'a_surviving': a_surviving,
        'b_surviving': b_surviving,
        'a_casualties': {i: 1.0 - (u.hp / u.hp_max) if u.hp_max else 1.0
                         for i, u in enumerate(side_a)},
        'b_casualties': {i: 1.0 - (u.hp / u.hp_max) if u.hp_max else 1.0
                         for i, u in enumerate(side_b)},
    }



# ─── PHASE 7 STEP §4.10.3 — STRATEGIC ADAPTER ────────────────────────────────


def resolve_mass_battle(faction_a, faction_b, terrain, world):
    """Strategic-layer entry point for Military Conquest resolution.

    Replaces the v17 single-roll path in `faction_action._try_conquest`. Per
    `mass_battle_integration_v30.md §4.10 sub-step 3` and `canon/02_canon_constraints.md`
    §B GD-1: produces faction stat / territorial-control deltas only — no
    mass_battle_outcome → game_victory triggers.

    Args:
        faction_a: attacker faction (has .name, .Mil)
        faction_b: defender faction OR None (target uncontrolled)
        terrain:   placeholder for terrain modifiers (deferred to Phase 7 follow-ons)
        world:     strategic world state (battle_count increment site)

    Returns:
        dict with keys:
          - 'attacker_wins': bool
          - 'degree': 'Overwhelming' | 'Success' | 'Partial' | 'Failure'
          - 'attacker_size_pct': float (remaining size / starting size)
          - 'defender_size_pct': float

    [GAP: faction→unit construction lacks canonical spec — minimum-viable defaults
     used. Phase 7 Step 10 sub-steps 1-2 (domain_echo + accounting) will introduce
     richer faction-state → unit-roster mapping.]
    """
    # GD-1: no victory short-circuit; only deltas
    unit_a = _faction_to_unit(faction_a)
    if faction_b is None:
        # Uncontrolled-territory case: light garrison. Mirrors v17 Ob 2 vs Ob 4 spread.
        unit_b = _faction_to_unit(_GarrisonStub(name='Uncontrolled', Mil=1.5))
    else:
        unit_b = _faction_to_unit(faction_b)

    # Single-encounter run — multi-unit orchestrator overkill for C2 scope.
    # Phase 7 Step 10 sub-steps 1-2 will route through run_multi_unit_battle.
    result = run_battle(unit_a, unit_b, max_turns=18)

    # Map v22 result → degree shape that faction_action expects
    a_size_pct = unit_a.effective_size / max(1, unit_a.size_max)
    b_size_pct = unit_b.effective_size / max(1, unit_b.size_max)
    attacker_wins = (not unit_a.routed) and (unit_b.routed or a_size_pct > b_size_pct)

    if attacker_wins and a_size_pct >= 0.75 and b_size_pct <= 0.25:
        degree = 'Overwhelming'
    elif attacker_wins:
        degree = 'Success'
    elif not unit_a.routed and a_size_pct >= 0.50:
        degree = 'Partial'
    else:
        degree = 'Failure'

    return {
        'attacker_wins': attacker_wins,
        'degree': degree,
        'attacker_size_pct': a_size_pct,
        'defender_size_pct': b_size_pct,
    }


class _GarrisonStub:
    """Minimal faction-shaped stub for uncontrolled-territory garrison.

    [GAP: defenderless-territory garrison strength lacks canonical spec; using
     Mil=1.5 to roughly match v17 Ob 2 vs Ob 4 single-roll spread. Phase 7
     follow-ons or integration_plan §4.10 sub-step 2 (accounting) will replace.]
    """
    def __init__(self, name, Mil):
        self.name = name
        self.Mil = Mil


def _faction_to_unit(faction):
    """Construct a v22 Unit from a strategic-layer faction object.

    [GAP: no canonical spec for faction.Mil → Unit construction. Defaults:
     shape='Line', tier=2 (200 troops), single subunit, command=4, discipline=5,
     morale=5, power=int(faction.Mil). Phase 7 Step 10 sub-steps 1-2 will
     introduce richer mapping via sim/cross_scale/domain_echo.py.]
    """
    power = max(1, int(round(faction.Mil)))
    sub = Subunit(
        shape='Line',
        troop_type='infantry',
        tier=2,
        starting_position=(8, 12),
        advance_dir=1,
        stance='balanced',
        unit_type='melee',
    )
    return Unit(
        name=f'{faction.name}_force',
        faction=faction.name,
        power=power,
        command=4,
        discipline=5,
        discipline_start=5,
        morale=5,
        morale_start=5,
        subunits=[sub],
    )


# ─── DATACLASS RE-EXPORT (must come AFTER all module-level constants/functions) ──
# Subunit + Unit are defined in sim.provincial.units; that module late-binds back
# to this module's namespace (`_mb` alias) for constants like TROOPS_PER_TIER and
# helpers like oriented_pattern, cell_speed, _stamina_pool_penalty. Python's import
# machinery resolves the circular path because all those names are already bound
# in this module by the time the from-import below executes.

from sim.provincial.units import Subunit, Unit  # noqa: E402
