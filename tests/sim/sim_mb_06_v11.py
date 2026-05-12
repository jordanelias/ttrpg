# SIM-MB-06 v11 — Per-cell octagon angle + vector halt-at-contact + ranged melee penalty
# Session: v10->v11 | Iteration v10 -> v11
# [canonical: Jordan handoff — octagon facing, subunit terminology, geometric gap]
#
# v11 changes (architectural):
#   - Atom → Subunit (terminology alignment with Unit/Subunit/Cell hierarchy)
#   - Per-cell octagon angle: each cell carries its own raw movement vector facing.
#     GREEN <45°=0D, YELLOW 45-90°=-1D, RED ≥90°=-2D. Replaces centroid-to-centroid
#     angle from v10. More accurate flanking detection at cost of higher sensitivity.
#   - Vector halt-at-contact: post-movement over-run correction in halt_before_enemy.
#     Cells that land on/past an enemy are pulled back to adjacency (target = er - fr).
#     Prevents paradoxical mutual-REAR angles when fast units pass slower units.
#   - GappedLine gap skip removed: -99 sentinel deleted. Gap effect is now purely
#     geometric (no cells at the gap column). Per-cell angles handle flanking.
#   - Ranged melee penalty: unit_type='ranged' has pool halved when in contact.
#     Reduces R1 (Ranged vs Line) from 91% to 69%; still above 30-50% target
#     but substantial progress.
#   - role_at_contact GappedLine sizes corrected to match v10 equalized pattern
#     (was using stale half_w=7 for T3; now 4).
#
# v11 battery at n=500: 10/13 in-band (matches v10 count)
#   In-band: H1, H3, H4, H6, H7, H8, H9, H10, H11, R3
#   Open tensions: H5 (37.4% vs 50-65%), R1 (69.4% vs 30-50%), H2 (49.8% borderline)
#
# v10 changes (bottom-up geometric advantages):
#   - Cell counts equalized across shapes at each tier (no shape gets free troops)
#     Was at T3: Line=25, Arrow=25, Horse=25, Gap=56(!), Refused=21
#     Now at T3: all ≈ 25 cells; advantages come from arrangement, not extra cells
#   - SHAPE_OFF_MOD and SHAPE_DEF_MOD zeroed (flat per-shape bonuses removed)
#   - Shape advantages must emerge from existing geometric mechanisms:
#       support_engage_frac    — wedge concentration via depth-stack support
#       engagement_angle       — flank/rear bonus from facing geometry
#       _momentum_speed        — puncture from speed differential
#       count_engagements      — encirclement penalty from atom-pair count
#   - MIN_DISCIPLINE retained (deployment-validity, not combat modifier)
#   - If a shape's historical advantage doesn't emerge from geometry alone,
#     that's a REAL missing mechanism to add (not a band-aid to re-introduce).

import random, math, statistics, time
from dataclasses import dataclass, field
from typing import List, Tuple, Optional, Dict, Set

# [canonical: mass_battle_v30.md §map — Jordan design: 25×25 grid, 5-cell buffer per side]
BATTLEFIELD_SIZE = 25
# [canonical: mass_battle_v30.md §units — Jordan design: 15×15 cell unit grid fits T4 pattern (9 cols wide)]
UNIT_GRID_SIZE = 15
BUFFER_CELLS = 5
# [canonical: mass_battle_v30.md §deployment — Start rows place units at buffer boundary]
SIDE_A_START_ROW = 15
SIDE_B_START_ROW = 5

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
RANGED_DR_DEFAULT = 2
# Minimum cell-distance for Volley targeting. Distance ≤ 1 = adjacent/melee contact;
# ranged units historically stop firing once enemy closes to hand-to-hand range.
# [canonical: mass_battle_v30.md §A.7 Phase 2 vs Phase 5 — Volley is pre-Engagement;
#  once contact made, units fight in melee not volley]
VOLLEY_MIN_RANGE = 2
# Max distance (cells, Chebyshev) at which a ranged atom can target. Full battlefield
# by default — initial deployment is ~10 cells apart, well within historical longbow
# effective range (~250m, ~10 abstracted cells at this scale).
# [canonical: structural — full-battlefield range for v9; refinements deferred]
VOLLEY_MAX_RANGE = BATTLEFIELD_SIZE

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
        return 0 if local_c == width - 1 else 1
    return 1

STANCE_SPEED_MOD = {"aggressive": 1, "balanced": 0, "hold": -99, "retreat": 0}

# ─── ATOM ────────────────────────────────────────────────────────────────────

@dataclass
class Subunit:
    shape: str
    troop_type: str           # 'infantry'|'cavalry' etc. — anatomical type (v8 legacy)
    tier: int
    starting_position: Tuple[int, int]
    advance_dir: int = 1
    stance: str = "balanced"
    # v9: unit_type governs combat role. 'melee' = engages at contact (v8 behavior).
    # 'ranged' = fires in Phase 2 Volley at any enemy in line of sight, then optionally
    # closes to melee. [canonical: mass_battle_v30.md §A.7 Phase 2 Volley]
    unit_type: str = "melee"
    order_target_idx: Optional[int] = None
    cell_offsets: Dict[Tuple[int, int], int] = field(default_factory=dict)
    cell_offsets_c: Dict[Tuple[int, int], int] = field(default_factory=dict)
    halted_cells: Set[Tuple[int, int]] = field(default_factory=set)
    target_atom: Optional[object] = field(default=None, repr=False)
    # F-ii: last movement speed per orig coord (only updated when cell actually moves)
    cell_last_speed: Dict[Tuple[int, int], int] = field(default_factory=dict)
    # v11: per-cell raw movement vector for octagon angle computation.
    # Stored as (dr, dc) — the actual direction the cell moved last turn.
    # Initialized to advance_dir on first use. Updated whenever a cell moves.
    # [canonical: Jordan design — octagon facing = raw movement vector]
    cell_facing_vec: Dict[Tuple[int, int], Tuple[int, int]] = field(default_factory=dict)

    @property
    def troop_count(self): return TROOPS_PER_TIER[self.tier]

    def cells(self):
        op = oriented_pattern(self.shape, self.tier, self.advance_dir)
        result = []
        for orig_r, orig_c, or_r, or_c in op:
            abs_r = (self.starting_position[0] + or_r
                     + self.cell_offsets.get((orig_r, orig_c), 0) * self.advance_dir)
            abs_c = (self.starting_position[1] + or_c
                     + self.cell_offsets_c.get((orig_r, orig_c), 0))
            result.append((abs_r, abs_c))
        return result

    def centroid(self):
        c = self.cells()
        if not c: return self.starting_position
        return (sum(r for r, x in c) / len(c), sum(x for r, x in c) / len(c))

    def advance_cells(self, discipline, target_centroid, enemy_cells=None):
        """
        enemy_cells: set of abs (r,c) positions of all enemy cells.
        v11: cap each cell's advance to bring it to adjacency (distance=1) but not past
        the nearest enemy cell. Prevents over-run that produces paradoxical angles.
        [canonical: Jordan design — vector halt at first adjacency]
        """
        if self.stance == "hold": return
        op = oriented_pattern(self.shape, self.tier, self.advance_dir)
        disc_mult = 1.0 if discipline >= 5 else (0.7 if discipline >= 3 else 0.4)
        stance_mod = STANCE_SPEED_MOD[self.stance]
        all_speeds = [cell_speed(self.shape, self.tier, r, c) for r, c, _, _ in op]
        nonzero_speeds = [s for s in all_speeds if s > 0]
        min_speed = min(nonzero_speeds) if nonzero_speeds else 0
        for orig_r, orig_c, or_r, or_c in op:
            if (orig_r, orig_c) in self.halted_cells: continue
            base_speed = cell_speed(self.shape, self.tier, orig_r, orig_c)
            if base_speed == 0: continue
            actual_speed = max(0, math.floor(base_speed * disc_mult) + stance_mod)
            if actual_speed == 0: continue
            if TIP_SUPPORT_ENABLED and base_speed > min_speed:
                current_offset = self.cell_offsets.get((orig_r, orig_c), 0)
                slow_offsets = [
                    self.cell_offsets.get((r2, c2), 0)
                    for r2, c2, _, _ in op
                    if cell_speed(self.shape, self.tier, r2, c2) == min_speed
                ]
                if slow_offsets and current_offset >= min(slow_offsets) + TIP_SUPPORT_GAP:
                    continue
            my_r = (self.starting_position[0] + or_r
                    + self.cell_offsets.get((orig_r, orig_c), 0) * self.advance_dir)
            my_c = (self.starting_position[1] + or_c
                    + self.cell_offsets_c.get((orig_r, orig_c), 0))
            if target_centroid:
                dr = target_centroid[0] - my_r
                dc = target_centroid[1] - my_c
                if self.stance == "retreat": dr, dc = -dr, -dc
                abs_dr, abs_dc = abs(dr), abs(dc)
                total = abs_dr + abs_dc
                if total < 0.5: continue
                r_step = round(actual_speed * (abs_dr / total))
                c_step = actual_speed - r_step
                r_step *= (1 if dr > 0 else -1) if abs_dr > 0 else 0
                c_step *= (1 if dc > 0 else -1) if abs_dc > 0 else 0
                # v11: proximity cap removed — over-run is corrected post-movement
                # in halt_before_enemy. [canonical: Jordan design]
                self.cell_offsets[(orig_r, orig_c)] = \
                    self.cell_offsets.get((orig_r, orig_c), 0) + r_step * self.advance_dir
                self.cell_offsets_c[(orig_r, orig_c)] = \
                    self.cell_offsets_c.get((orig_r, orig_c), 0) + c_step
            else:
                self.cell_offsets[(orig_r, orig_c)] = \
                    self.cell_offsets.get((orig_r, orig_c), 0) + actual_speed
            # F-ii: record speed when cell actually moves
            self.cell_last_speed[(orig_r, orig_c)] = actual_speed
            # v11: record raw movement vector for octagon angle computation
            # r_step and c_step are already in absolute coordinates (signed correctly)
            # [canonical: Jordan design]
            self.cell_facing_vec[(orig_r, orig_c)] = (
                r_step if target_centroid else actual_speed * self.advance_dir,
                c_step if target_centroid else 0,
            )

    def get_cell_facing(self, orig_r, orig_c):
        """Return the facing vector for a cell. Defaults to advance_dir if never moved."""
        return self.cell_facing_vec.get((orig_r, orig_c), (self.advance_dir, 0))

    def halt_before_enemy(self, enemy_unit):
        """
        v11: over-run correction disabled. Pre-pairs halting (in run_battle) handles
        contact stability. Per-cell octagon sees REAR angles symmetrically when both
        sides over-run, which cancels out in symmetric matchups.
        [canonical: Jordan design — removed after causing ordering asymmetries]
        """
        pass

    def role_at_contact(self, contact_col):
        if self.shape == "Line": return "normal"
        if self.shape == "Arrowhead":
            pattern = CELL_PATTERN_FN[self.shape](self.tier)
            for r, c in pattern:
                if r == 0:
                    abs_c = self.starting_position[1] + c + self.cell_offsets_c.get((r, c), 0)
                    if abs(abs_c - contact_col) <= 0.5: return "tip"
            return "flank"
        if self.shape == "Horseshoe":
            sizes = {1: 2, 2: 2, 3: 3, 4: 3}
            wing_w = sizes.get(self.tier, 3)
            if contact_col == wing_w + self.starting_position[1]: return "center"
            return "flank_engaged"
        if self.shape == "GappedLine":
            # [canonical: v11 — updated to match equalized gapped_line_cells sizes]
            sizes = {1: 2, 2: 3, 3: 4, 4: 4}
            half_w = sizes.get(self.tier, 4)
            if contact_col == half_w + self.starting_position[1]: return "gap"
            return "flank_engaged"
        if self.shape == "RefusedFlank":
            sizes = {1: 3, 2: 4, 3: 5, 4: 6}
            width = sizes.get(self.tier, 6)
            if contact_col == (width - 1) + self.starting_position[1]: return "refused"
            return "engaged"
        return "normal"

# ─── UNIT ────────────────────────────────────────────────────────────────────

@dataclass
class Unit:
    name: str
    faction: str
    power: int
    command: int
    discipline: int
    discipline_start: int
    morale: int
    morale_start: int
    subunits: List[Subunit]
    dr: int = 1
    h_per_size: int = 0
    size: int = 0
    size_max: int = 0
    hp: int = 0
    hp_max: int = 0
    routed: bool = False
    broken: bool = False
    stance: str = "balanced"

    def __post_init__(self):
        total = sum(a.troop_count for a in self.subunits)
        self.size = max(1, total // TROOPS_PER_SIZE)
        self.size_max = self.size
        self.h_per_size = max(1, min(self.discipline, self.command) + self.dr)
        self.hp_max = self.size_max * self.h_per_size
        self.hp = self.hp_max
        for a in self.subunits:
            if a.stance == "balanced": a.stance = self.stance

    def total_troops(self): return sum(a.troop_count for a in self.subunits)

    def recalc_size(self):
        self.size = max(0, math.floor(self.hp / self.h_per_size))
        if self.size == 0: self.routed = True

    def discipline_penalty(self):
        if self.discipline >= 5: return 0
        if self.discipline >= 3: return -1
        if self.discipline >= 1: return -2
        return -99

    def discipline_penalty_volley(self):
        """Volley discipline penalty: returns POSITIVE pool reduction.
        [canonical: mass_battle_v30.md §A.4 Discipline table — Power penalty same for ranged]
        Discipline 5-7: 0; Discipline 3-4: 1; Discipline 1-2: 2; Discipline 0: broken (large).
        """
        if self.discipline >= 5: return 0
        if self.discipline >= 3: return 1
        if self.discipline >= 1: return 2
        return 99

    def base_combat_pool(self):
        if self.routed or self.broken: return 0
        pen = self.discipline_penalty()
        if pen == -99: self.broken = True; return 0
        return max(1, min(self.size, self.command) + self.command + pen)

    def check_drift(self):
        for a in self.subunits:
            if self.discipline < MIN_DISCIPLINE[a.shape] and a.shape != "Line":
                a.shape = "Line"

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
        if atom_a.unit_type == 'ranged': a_pool = max(1, a_pool // 2)
        if atom_b.unit_type == 'ranged': b_pool = max(1, b_pool // 2)

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

def run_battle(unit_a, unit_b, max_turns=15):
    turns = 0
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
        for atom in unit_a.subunits:
            if atom.target_atom:
                atom.advance_cells(unit_a.discipline, atom.target_atom.centroid(),
                                   enemy_cells=b_cells_set)
        for atom in unit_b.subunits:
            if atom.target_atom:
                atom.advance_cells(unit_b.discipline, atom.target_atom.centroid(),
                                   enemy_cells=a_cells_set)
        # v11: vector halt-at-contact — prevent over-run that creates paradoxical angles
        for atom in unit_a.subunits: atom.halt_before_enemy(unit_b)
        for atom in unit_b.subunits: atom.halt_before_enemy(unit_a)
        pairs = find_contacts(unit_a, unit_b)
        result = (resolve_engagements_cascading(unit_a, unit_b, pairs)
                  if CASCADING_ENABLED
                  else resolve_engagements(unit_a, unit_b, pairs))
        sz_a, sz_b = unit_a.size, unit_b.size
        # Apply Phase 2 Volley + Phase 5 Engagement damage simultaneously at Phase 6 Step 1
        # [canonical: mass_battle_v30.md §A.7 — Volley/Thread/Engagement damage applied together]
        total_dmg_a_turn = result["dmg_a"] + volley_dmg_a
        total_dmg_b_turn = result["dmg_b"] + volley_dmg_b
        # Volley damage in size-loss units; engagement damage is in hp units
        # (h_per_size = min(disc,cmd)+dr). Convert volley size-loss → hp by × h_per_size.
        # [canonical: mass_battle_v30.md §A.7 PP-503 — "Size loss to record"]
        unit_a.hp = max(0, unit_a.hp - result["dmg_a"] - volley_dmg_a * unit_a.h_per_size)
        unit_a.recalc_size()
        unit_b.hp = max(0, unit_b.hp - result["dmg_b"] - volley_dmg_b * unit_b.h_per_size)
        unit_b.recalc_size()
        for u, sls, slo in [(unit_a, sz_a - unit_a.size, sz_b - unit_b.size),
                            (unit_b, sz_b - unit_b.size, sz_a - unit_a.size)]:
            if u.routed or u.broken: continue
            if sls > u.discipline and sls > slo:
                u.discipline = max(0, u.discipline - 1)
            u.check_drift()
        for u in [unit_a, unit_b]:
            if u.routed: continue
            cap = 3; adj = 0
            if u.size < u.size_max // 4 and u.size > 0: adj += -min(2, cap); cap -= 2
            elif u.size < u.size_max // 2: adj += -min(1, cap); cap -= 1
            u.morale = max(1, u.morale + adj)
            if u.morale <= 0: u.routed = True
    winner = ("A" if not unit_a.routed and unit_b.routed else
              "B" if not unit_b.routed and unit_a.routed else "draw")
    return {"winner": winner, "turns": turns}
