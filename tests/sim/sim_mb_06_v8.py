# SIM-MB-06 v8 — Tension F implementation: cell support + puncture
# Session: 2026-05-12 | v7 + F-i (cell support stack) + F-ii (puncture/momentum)
#
# v8 changes over v7:
#   F-i: support_stack_frac() — cells behind contact zone contribute weighted engage_frac
#        weights: depth 1→1.0, 2→0.7, 3→0.5, 4→0.3; capped at 1.0
#        [canonical: tests/sim/sim_mb_06_handoff_2026-05-12.md §F-i]
#   F-ii: puncture_bonus() — attacker speed differential adds pool dice, cap +3D
#        last_turn_speed tracked per cell in Atom; halted cells = 0
#        [canonical: tests/sim/sim_mb_06_handoff_2026-05-12.md §F-ii]
#
# Control flags: F_SUPPORT_ENABLED, F_PUNCTURE_ENABLED — can toggle independently

import random, math, statistics, time
from dataclasses import dataclass, field
from typing import List, Tuple, Optional, Dict, Set

BATTLEFIELD_SIZE = 25     # [canonical: tests/sim/sim_mb_06_v7_manifest.md — 25×25 battlefield]
UNIT_GRID_SIZE = 15       # [canonical: tests/sim/sim_mb_06_v7_manifest.md — 15×15 unit grids]
BUFFER_CELLS = 5          # [canonical: tests/sim/sim_mb_06_v7_manifest.md — 5-cell buffer]
SIDE_A_START_ROW = 15     # [canonical: tests/sim/sim_mb_06_v7_manifest.md — Side A rows 15-19]
SIDE_B_START_ROW = 5      # [canonical: tests/sim/sim_mb_06_v7_manifest.md — Side B rows 5-9]

POOL_VARIANT = "C-ii"     # [canonical: tests/sim/sim_mb_06_v7_manifest.md — Phase C exploration]
TIP_SUPPORT_ENABLED = True # [canonical: tests/sim/sim_mb_06_v7_manifest.md — Phase E exploration]
TIP_SUPPORT_GAP = 2        # [canonical: tests/sim/sim_mb_06_v7_manifest.md — X=2 default]

# v8 control flags
F_SUPPORT_ENABLED = True   # F-i: cell support stack [canonical: handoff §F-i]
F_PUNCTURE_ENABLED = True  # F-ii: puncture/momentum [canonical: handoff §F-ii]

# F-i weights by depth behind contact row
# [canonical: tests/sim/sim_mb_06_handoff_2026-05-12.md — row weights 1.0/0.7/0.5/0.3]
SUPPORT_WEIGHTS = {1: 1.0, 2: 0.7, 3: 0.5, 4: 0.3}

# F-ii: puncture bonus per speed differential unit; cap
# [canonical: tests/sim/sim_mb_06_handoff_2026-05-12.md — +1D/speed-unit, cap +3D]
PUNCTURE_BONUS_PER_SPEED_UNIT = 1
PUNCTURE_CAP = 3           # [canonical: tests/sim/sim_mb_06_handoff_2026-05-12.md]

TROOPS_PER_TIER = {1: 100, 2: 200, 3: 400, 4: 800}  # [canonical: tests/sim/sim_mb_06_v7_manifest.md]
TROOPS_PER_SIZE = 100
ENCIRCLEMENT_PENALTY = 1   # [canonical: tests/sim/sim_mb_06_v7_manifest.md — reduced from 2 per v4]

SHAPE_OFF_MOD = {
    "Line":        lambda role: 0,
    "Arrowhead":   lambda role: 2 if role == "tip" else -1,  # [canonical: tests/sim/sim_mb_06_v7_manifest.md — structural shape off-mods]
    "Horseshoe":   lambda role: -2 if role == "center" else (2 if role == "flank_engaged" else 0),  # [canonical: tests/sim/sim_mb_06_v7_manifest.md — structural]
    "GappedLine":  lambda role: -99 if role == "gap" else (2 if role == "flank_engaged" else 0),  # [canonical: tests/sim/sim_mb_06_v7_manifest.md — structural sentinel -99 = disengaged gap]
    "RefusedFlank":lambda role: -2 if role == "refused" else 1,  # [canonical: tests/sim/sim_mb_06_v7_manifest.md — structural]
}
SHAPE_DEF_MOD = {"Line": lambda r: 0, "Arrowhead": lambda r: 0,  # [canonical: tests/sim/sim_mb_06_v7_manifest.md — structural def mods]
                  "Horseshoe": lambda r: 1 if r == "center" else 0,
                  "GappedLine": lambda r: 0, "RefusedFlank": lambda r: 0}
MIN_DISCIPLINE = {"Line": 1, "Arrowhead": 4, "Horseshoe": 5, "GappedLine": 5, "RefusedFlank": 3}  # [canonical: tests/sim/sim_mb_06_v7_manifest.md — structural]

# [canonical: tests/sim/sim_mb_06_handoff_2026-05-12.md — ANGLE_DEF_MOD]
ANGLE_DEF_MOD = {"FRONT": 0, "FLANK": -1, "REAR": -2}

# ─────────────────────────────────────────────────────────────────────────────
# CELL PATTERNS
# ─────────────────────────────────────────────────────────────────────────────

def arrowhead_cells(tier):
    cells = []
    for r in range(tier + 2):  # [canonical: tests/sim/sim_mb_06_v7_manifest.md — structural arrowhead row formula: row r has width 2r+1]
        width = 2 * r + 1
        center_col = tier + 1
        start = center_col - r
        for c in range(start, start + width):
            cells.append((r, c))
    return cells

def line_cells(tier):
    sizes = {1: (3, 3), 2: (5, 3), 3: (5, 5), 4: (7, 5)}  # [canonical: tests/sim/sim_mb_06_v7_manifest.md — structural line dims]
    width, depth = sizes.get(tier, (7, 5))  # [canonical: tests/sim/sim_mb_06_v7_manifest.md — structural]
    return [(r, c) for r in range(depth) for c in range(width)]

def horseshoe_cells(tier):
    sizes = {1: (2, 2), 2: (2, 3), 3: (3, 3), 4: (3, 4)}  # [canonical: tests/sim/sim_mb_06_v7_manifest.md — structural horseshoe dims]
    wing_w, depth = sizes.get(tier, (3, 4))  # [canonical: tests/sim/sim_mb_06_v7_manifest.md — structural]
    full_width = wing_w * 2 + 1
    cells = []
    for r in range(depth):
        for c in range(wing_w):
            cells.append((r, c))
        for c in range(wing_w + 1, full_width):  # [canonical: tests/sim/sim_mb_06_v7_manifest.md — structural horseshoe gap at wing_w]
            cells.append((r, c))
    for c in range(full_width):
        cells.append((depth, c))
    return cells

def gapped_line_cells(tier):
    sizes = {1: (3, 2), 2: (5, 3), 3: (7, 4), 4: (9, 5)}  # [canonical: tests/sim/sim_mb_06_v7_manifest.md — structural gappedline dims]
    half_w, depth = sizes.get(tier, (9, 5))  # [canonical: tests/sim/sim_mb_06_v7_manifest.md — structural]
    cells = []
    for r in range(depth):
        for c in range(half_w):
            cells.append((r, c))
        for c in range(half_w + 1, 2 * half_w + 1):  # [canonical: tests/sim/sim_mb_06_v7_manifest.md — structural gappedline gap at half_w]
            cells.append((r, c))
    return cells

def refused_flank_cells(tier):
    sizes = {1: (3, 3), 2: (4, 3), 3: (5, 4), 4: (6, 5)}  # [canonical: tests/sim/sim_mb_06_v7_manifest.md — structural refusedflank dims]
    width, depth = sizes.get(tier, (6, 5))  # [canonical: tests/sim/sim_mb_06_v7_manifest.md — structural]
    cells = []
    for r in range(depth):
        for c in range(width - 1):  # [canonical: tests/sim/sim_mb_06_v7_manifest.md — structural refusedflank refused col = width-1]
            cells.append((r, c))
    for r in range(depth + 1):
        cells.append((r, width - 1))
    return cells

CELL_PATTERN_FN = {
    "Line": line_cells, "Arrowhead": arrowhead_cells,
    "Horseshoe": horseshoe_cells, "GappedLine": gapped_line_cells,
    "RefusedFlank": refused_flank_cells,
}

def oriented_pattern(shape, tier, advance_dir):
    """Returns list of (orig_r, orig_c, oriented_r, oriented_c) tuples.
    Side B (advance_dir=+1) gets vertical mirror so leading edge faces enemy.
    [canonical: tests/sim/sim_mb_06_v7_manifest.md — side-mirror]"""
    pattern = CELL_PATTERN_FN[shape](tier)
    if advance_dir == -1:  # [canonical: tests/sim/sim_mb_06_v7_manifest.md — structural side A = -1, side B = +1]
        return [(r, c, r, c) for r, c in pattern]
    max_r = max(r for r, c in pattern)
    return [(r, c, max_r - r, c) for r, c in pattern]

def cell_facing(advance_dir):
    """Uniform facing for all cells in formation. [canonical: v7 structural]"""
    return (advance_dir, 0)

def engagement_angle(defender_pos, defender_facing, attacker_pos):
    """FRONT/FLANK/REAR classification. [canonical: v7 structural]"""
    dr_to = attacker_pos[0] - defender_pos[0]
    dc_to = attacker_pos[1] - defender_pos[1]
    fr, fc = defender_facing
    dot = dr_to * fr + dc_to * fc
    mag = max(1e-9, (dr_to*dr_to + dc_to*dc_to) ** 0.5)  # [canonical: tests/sim/sim_mb_06_v7_manifest.md — structural precision floor]
    proj = dot / mag
    if proj > 0.5: return "FRONT"  # [canonical: tests/sim/sim_mb_06_v7_manifest.md — structural ~60° cone]
    if proj < -0.5: return "REAR"  # [canonical: tests/sim/sim_mb_06_v7_manifest.md — structural ~60° rear cone]
    return "FLANK"

def atom_max_width(shape, tier):
    pattern = CELL_PATTERN_FN[shape](tier)
    by_row = {}
    for r, c in pattern:
        by_row.setdefault(r, []).append(c)
    return max(len(v) for v in by_row.values())

# ─────────────────────────────────────────────────────────────────────────────
# F-i: CELL SUPPORT STACK
# [canonical: tests/sim/sim_mb_06_handoff_2026-05-12.md §(1) Cell support]
# ─────────────────────────────────────────────────────────────────────────────

def support_stack_frac(atom, contact_orig_coords, max_width):
    """Compute effective engage_frac with support from cells behind the contact zone.

    "Behind" = higher oriented_r (further from enemy) in both advance directions,
    because oriented_pattern mirrors Side B so that or_r always increases away from
    the enemy's direction.

    For each contact cell's oriented_r, find the minimum (most forward) contact row.
    Rows at depth d (1 = immediately behind) contribute: count × SUPPORT_WEIGHTS[d].
    Total = |contact_cells| + sum(weighted_supporters).
    engage_frac = min(1.0, total / max_width).
    (canonical: handoff §F-i)
    """
    if not F_SUPPORT_ENABLED:
        return len(contact_orig_coords) / max_width

    op = oriented_pattern(atom.shape, atom.tier, atom.advance_dir)
    orig_to_or_r = {(orig_r, orig_c): or_r for orig_r, orig_c, or_r, or_c in op}
    all_cells_by_or_r = {}
    for orig_r, orig_c, or_r, or_c in op:
        all_cells_by_or_r.setdefault(or_r, []).append((orig_r, orig_c))

    contact_set = set(contact_orig_coords)
    contact_or_rows = set()
    for coord in contact_set:
        if coord in orig_to_or_r:
            contact_or_rows.add(orig_to_or_r[coord])

    if not contact_or_rows:
        return len(contact_orig_coords) / max_width

    # Most forward contact row (smallest or_r = closest to enemy)
    front_or_r = min(contact_or_rows)
    # Count cells at each support depth behind the front contact row
    supporter_sum = 0.0
    for depth, weight in SUPPORT_WEIGHTS.items():
        support_or_r = front_or_r + depth  # behind = higher or_r
        supporters = all_cells_by_or_r.get(support_or_r, [])
        supporter_sum += len(supporters) * weight

    total_effective = len(contact_orig_coords) + supporter_sum
    return min(1.0, total_effective / max_width)  # [canonical: tests/sim/sim_mb_06_handoff_2026-05-12.md — cap at 1.0]


# ─────────────────────────────────────────────────────────────────────────────
# F-ii: PUNCTURE / MOMENTUM
# [canonical: tests/sim/sim_mb_06_handoff_2026-05-12.md §(2) Puncture mechanism]
# ─────────────────────────────────────────────────────────────────────────────

def puncture_bonus(attacker_atom, contact_orig_coords):
    """Compute puncture bonus dice for attacker.
    Average speed of attacker contact cells vs defender (0 if halted = in contact).
    +1D per speed-unit differential, cap PUNCTURE_CAP.
    (canonical: handoff §F-ii)
    """
    if not F_PUNCTURE_ENABLED:
        return 0
    speeds = []
    for coord in contact_orig_coords:
        spd = attacker_atom.last_turn_speed.get(coord, 0)
        speeds.append(spd)
    if not speeds:
        return 0
    avg_attacker_speed = sum(speeds) / len(speeds)
    # Defender contact cells: speed 0 (they were halted at contact row)
    defender_speed = 0
    diff = avg_attacker_speed - defender_speed
    if diff <= 0:
        return 0
    return min(PUNCTURE_CAP, math.floor(diff * PUNCTURE_BONUS_PER_SPEED_UNIT))


# ─────────────────────────────────────────────────────────────────────────────
# PER-CELL SPEED
# ─────────────────────────────────────────────────────────────────────────────

def cell_speed(shape, tier, local_r, local_c):
    """Speed of an individual cell at Disc 5 + Balanced.
    [canonical: tests/sim/sim_mb_06_v7_manifest.md — per-cell deformation Eiii]"""
    if shape == "Line":
        return 1
    if shape == "Arrowhead":
        return 2 if local_r == 0 else 1
    if shape == "Horseshoe":
        sizes = {1: 2, 2: 2, 3: 3, 4: 3}  # [canonical: tests/sim/sim_mb_06_v7_manifest.md — structural horseshoe wing widths]
        wing_w = sizes.get(tier, 3)
        depth_sizes = {1: 2, 2: 3, 3: 3, 4: 4}  # [canonical: tests/sim/sim_mb_06_v7_manifest.md — structural horseshoe depths]
        depth = depth_sizes.get(tier, 4)
        if local_r == depth:
            return 0
        elif local_c != wing_w:
            return 2
        return 1
    if shape == "GappedLine":
        return 1
    if shape == "RefusedFlank":
        sizes = {1: 3, 2: 4, 3: 5, 4: 6}  # [canonical: tests/sim/sim_mb_06_v7_manifest.md — structural refusedflank widths]
        width = sizes.get(tier, 6)
        if local_c == width - 1:
            return 0
        return 1
    return 1

STANCE_SPEED_MOD = {"aggressive": 1, "balanced": 0, "hold": -99, "retreat": 0}  # [canonical: tests/sim/sim_mb_06_v7_manifest.md — structural sentinel -99=unable to advance]


# ─────────────────────────────────────────────────────────────────────────────
# ATOM — now tracks last_turn_speed per cell for F-ii
# ─────────────────────────────────────────────────────────────────────────────

@dataclass
class Atom:
    shape: str
    troop_type: str
    tier: int
    starting_position: Tuple[int, int]
    advance_dir: int = 1
    stance: str = "balanced"
    order_target_idx: Optional[int] = None
    cell_offsets: Dict[Tuple[int, int], int] = field(default_factory=dict)
    cell_offsets_c: Dict[Tuple[int, int], int] = field(default_factory=dict)
    halted_cells: Set[Tuple[int, int]] = field(default_factory=set)
    target_atom: Optional[object] = field(default=None, repr=False)
    last_turn_speed: Dict[Tuple[int, int], int] = field(default_factory=dict)  # F-ii

    @property
    def troop_count(self): return TROOPS_PER_TIER[self.tier]

    def cells(self) -> List[Tuple[int, int]]:
        op = oriented_pattern(self.shape, self.tier, self.advance_dir)
        result = []
        for orig_r, orig_c, or_r, or_c in op:
            offset_r = self.cell_offsets.get((orig_r, orig_c), 0)
            offset_c = self.cell_offsets_c.get((orig_r, orig_c), 0)
            abs_r = self.starting_position[0] + or_r + offset_r * self.advance_dir
            abs_c = self.starting_position[1] + or_c + offset_c
            result.append((abs_r, abs_c))
        return result

    def centroid(self) -> Tuple[float, float]:
        c = self.cells()
        if not c: return (self.starting_position[0], self.starting_position[1])
        return (sum(r for r, x in c) / len(c), sum(x for r, x in c) / len(c))

    def advance_cells(self, discipline: int, target_centroid: Optional[Tuple[float, float]]):
        """Advance per cell. Records last_turn_speed for F-ii puncture calc."""
        if self.stance == "hold":
            return
        op = oriented_pattern(self.shape, self.tier, self.advance_dir)
        disc_mult = 1.0 if discipline >= 5 else (0.7 if discipline >= 3 else 0.4)  # [canonical: tests/sim/sim_mb_06_v7_manifest.md — structural disc multipliers]
        stance_mod = STANCE_SPEED_MOD[self.stance]
        all_speeds = [cell_speed(self.shape, self.tier, r, c) for r, c, _, _ in op]
        nonzero_speeds = [s for s in all_speeds if s > 0]
        min_speed = min(nonzero_speeds) if nonzero_speeds else 0

        # Reset speed tracking for this turn
        self.last_turn_speed = {}

        for orig_r, orig_c, or_r, or_c in op:
            if (orig_r, orig_c) in self.halted_cells:
                self.last_turn_speed[(orig_r, orig_c)] = 0  # halted = speed 0
                continue
            base_speed = cell_speed(self.shape, self.tier, orig_r, orig_c)
            if base_speed == 0:
                self.last_turn_speed[(orig_r, orig_c)] = 0
                continue
            actual_speed = max(0, math.floor(base_speed * disc_mult) + stance_mod)
            if actual_speed == 0:
                self.last_turn_speed[(orig_r, orig_c)] = 0
                continue
            # Tip-support gate
            if TIP_SUPPORT_ENABLED and base_speed > min_speed:
                current_offset = self.cell_offsets.get((orig_r, orig_c), 0)
                slow_offsets = [
                    self.cell_offsets.get((r2, c2), 0)
                    for r2, c2, _, _ in op
                    if cell_speed(self.shape, self.tier, r2, c2) == min_speed
                ]
                if slow_offsets and current_offset >= min(slow_offsets) + TIP_SUPPORT_GAP:
                    self.last_turn_speed[(orig_r, orig_c)] = 0
                    continue
            # Record speed before movement
            self.last_turn_speed[(orig_r, orig_c)] = actual_speed

            my_r = self.starting_position[0] + or_r + self.cell_offsets.get((orig_r, orig_c), 0) * self.advance_dir
            my_c = self.starting_position[1] + or_c + self.cell_offsets_c.get((orig_r, orig_c), 0)
            if target_centroid:
                dr = target_centroid[0] - my_r
                dc = target_centroid[1] - my_c
                if self.stance == "retreat":
                    dr, dc = -dr, -dc
                abs_dr, abs_dc = abs(dr), abs(dc)
                total = abs_dr + abs_dc
                if total < 0.5: continue
                r_step = round(actual_speed * (abs_dr / total))
                c_step = actual_speed - r_step
                r_step *= (1 if dr > 0 else -1) if abs_dr > 0 else 0
                c_step *= (1 if dc > 0 else -1) if abs_dc > 0 else 0
                self.cell_offsets[(orig_r, orig_c)] = self.cell_offsets.get((orig_r, orig_c), 0) + r_step * self.advance_dir
                self.cell_offsets_c[(orig_r, orig_c)] = self.cell_offsets_c.get((orig_r, orig_c), 0) + c_step
            else:
                self.cell_offsets[(orig_r, orig_c)] = self.cell_offsets.get((orig_r, orig_c), 0) + actual_speed

    def role_at_contact(self, contact_col: int) -> str:
        if self.shape == "Line": return "normal"
        if self.shape == "Arrowhead":
            pattern = CELL_PATTERN_FN[self.shape](self.tier)
            for r, c in pattern:
                if r == 0:
                    abs_c = self.starting_position[1] + c + self.cell_offsets_c.get((r, c), 0)
                    if abs(abs_c - contact_col) <= 0.5:
                        return "tip"
            return "flank"
        if self.shape == "Horseshoe":
            sizes = {1: 2, 2: 2, 3: 3, 4: 3}  # [canonical: tests/sim/sim_mb_06_v7_manifest.md — structural]
            wing_w = sizes.get(self.tier, 3)
            center_col_abs = wing_w + self.starting_position[1]
            if contact_col == center_col_abs: return "center"
            return "flank_engaged"
        if self.shape == "GappedLine":
            sizes = {1: 3, 2: 5, 3: 7, 4: 9}  # [canonical: tests/sim/sim_mb_06_v7_manifest.md — structural]
            half_w = sizes.get(self.tier, 9)
            gap_col_abs = half_w + self.starting_position[1]
            if contact_col == gap_col_abs: return "gap"
            return "flank_engaged"
        if self.shape == "RefusedFlank":
            sizes = {1: 3, 2: 4, 3: 5, 4: 6}  # [canonical: tests/sim/sim_mb_06_v7_manifest.md — structural]
            width = sizes.get(self.tier, 6)
            refused_col_abs = (width - 1) + self.starting_position[1]
            if contact_col == refused_col_abs: return "refused"
            return "engaged"
        return "normal"


# ─────────────────────────────────────────────────────────────────────────────
# UNIT
# ─────────────────────────────────────────────────────────────────────────────

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
    atoms: List[Atom]
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
        total = sum(a.troop_count for a in self.atoms)
        self.size = max(1, total // TROOPS_PER_SIZE)
        self.size_max = self.size
        self.h_per_size = max(1, min(self.discipline, self.command) + self.dr)  # [canonical: tests/sim/sim_mb_06_v7_manifest.md — structural HP formula]
        self.hp_max = self.size_max * self.h_per_size
        self.hp = self.hp_max
        for a in self.atoms:
            if a.stance == "balanced": a.stance = self.stance

    def total_troops(self): return sum(a.troop_count for a in self.atoms)

    def recalc_size(self):
        self.size = max(0, math.floor(self.hp / self.h_per_size))
        if self.size == 0: self.routed = True

    def discipline_penalty(self):
        if self.discipline >= 5: return 0
        if self.discipline >= 3: return -1
        if self.discipline >= 1: return -2
        return -99  # [canonical: tests/sim/sim_mb_06_v7_manifest.md — structural sentinel: broken]

    def base_combat_pool(self):
        if self.routed or self.broken: return 0
        pen = self.discipline_penalty()
        if pen == -99: self.broken = True; return 0  # [canonical: tests/sim/sim_mb_06_v7_manifest.md — structural]
        return max(1, min(self.size, self.command) + self.command + pen)

    def check_drift(self):
        for a in self.atoms:
            if self.discipline < MIN_DISCIPLINE[a.shape] and a.shape != "Line":
                a.shape = "Line"


# ─────────────────────────────────────────────────────────────────────────────
# DICE
# ─────────────────────────────────────────────────────────────────────────────

def roll_pool(n, tn=7):  # [canonical: tests/sim/sim_mb_06_v7_manifest.md — structural §Dice TN7]
    net = 0
    for _ in range(max(1, n)):
        f = random.randint(1, 10)
        if f == 1: net -= 1
        elif f >= tn and f <= 9: net += 1  # [canonical: tests/sim/sim_mb_06_v7_manifest.md — structural §Dice System]
        elif f == 10: net += 2
    return net

def compute_degree(net, ob):
    if net <= 0: return "Failure"
    if net >= 2 * ob and net >= 3: return "Overwhelming"
    if net >= ob: return "Success"
    return "Partial"

DAMAGE_BY_DEGREE = {"Overwhelming": lambda p: 1+p, "Success": lambda p: p,  # [canonical: tests/sim/sim_mb_06_v7_manifest.md — structural degree→damage]
                     "Partial": lambda p: 1, "Failure": lambda p: 0}


# ─────────────────────────────────────────────────────────────────────────────
# TARGETING
# ─────────────────────────────────────────────────────────────────────────────

def assign_targets(unit_a, unit_b):
    for atom in unit_a.atoms:
        if not unit_b.atoms: atom.target_atom = None; continue
        if atom.order_target_idx is not None and atom.order_target_idx < len(unit_b.atoms):
            atom.target_atom = unit_b.atoms[atom.order_target_idx]
        else:
            my = atom.centroid()
            atom.target_atom = min(unit_b.atoms,
                                     key=lambda e: math.hypot(my[0]-e.centroid()[0], my[1]-e.centroid()[1]))
    for atom in unit_b.atoms:
        if not unit_a.atoms: atom.target_atom = None; continue
        if atom.order_target_idx is not None and atom.order_target_idx < len(unit_a.atoms):
            atom.target_atom = unit_a.atoms[atom.order_target_idx]
        else:
            my = atom.centroid()
            atom.target_atom = min(unit_a.atoms,
                                     key=lambda e: math.hypot(my[0]-e.centroid()[0], my[1]-e.centroid()[1]))


# ─────────────────────────────────────────────────────────────────────────────
# CONTACT + ENGAGEMENT
# ─────────────────────────────────────────────────────────────────────────────

def find_contacts(unit_a, unit_b):
    pairs = []
    a_cells = {id(a): set(a.cells()) for a in unit_a.atoms}
    b_cells = {id(b): set(b.cells()) for b in unit_b.atoms}
    for atom_a in unit_a.atoms:
        for atom_b in unit_b.atoms:
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
                pairs.append({
                    "atom_a": atom_a, "atom_b": atom_b,
                    "a_cells": contact_cells_a, "b_cells": contact_cells_b,
                    "cols": list(contact_cols),
                })
    return pairs

def count_engagements_per_atom(pairs):
    counts = {}
    for p in pairs:
        counts[id(p["atom_a"])] = counts.get(id(p["atom_a"]), 0) + 1
        counts[id(p["atom_b"])] = counts.get(id(p["atom_b"]), 0) + 1
    return counts

def abs_cells_to_orig(atom, abs_contact_cells):
    """Map absolute (row,col) contact positions back to original pattern coords."""
    op = oriented_pattern(atom.shape, atom.tier, atom.advance_dir)
    result = []
    for orig_r, orig_c, or_r, or_c in op:
        abs_r = atom.starting_position[0] + or_r + atom.cell_offsets.get((orig_r, orig_c), 0) * atom.advance_dir
        abs_c = atom.starting_position[1] + or_c + atom.cell_offsets_c.get((orig_r, orig_c), 0)
        if (abs_r, abs_c) in set(abs_contact_cells):
            result.append((orig_r, orig_c))
    return result

def resolve_engagements(unit_a, unit_b, pairs):
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
        if off_a == -99 or off_b == -99: continue  # [canonical: tests/sim/sim_mb_06_v7_manifest.md — structural sentinel skip disengaged gap]

        # Map contact cells back to orig coords for support-stack calc
        a_contact_orig = abs_cells_to_orig(atom_a, p["a_cells"])
        b_contact_orig = abs_cells_to_orig(atom_b, p["b_cells"])

        a_troops_frac = atom_a.troop_count / unit_a.total_troops()
        b_troops_frac = atom_b.troop_count / unit_b.total_troops()
        a_width = atom_max_width(atom_a.shape, atom_a.tier)
        b_width = atom_max_width(atom_b.shape, atom_b.tier)
        a_base = unit_a.base_combat_pool()
        b_base = unit_b.base_combat_pool()

        # F-i: support-stack engage_frac
        # [canonical: tests/sim/sim_mb_06_handoff_2026-05-12.md §(1) Cell support]
        a_engage_frac = support_stack_frac(atom_a, a_contact_orig, a_width)
        b_engage_frac = support_stack_frac(atom_b, b_contact_orig, b_width)

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

        # Engagement angle — defender penalty
        a_contact_centroid = (sum(c[0] for c in p["a_cells"]) / len(p["a_cells"]),
                                sum(c[1] for c in p["a_cells"]) / len(p["a_cells"]))
        b_contact_centroid = (sum(c[0] for c in p["b_cells"]) / len(p["b_cells"]),
                                sum(c[1] for c in p["b_cells"]) / len(p["b_cells"]))
        a_facing = cell_facing(atom_a.advance_dir)
        b_facing = cell_facing(atom_b.advance_dir)
        a_angle = engagement_angle(a_contact_centroid, a_facing, b_contact_centroid)
        b_angle = engagement_angle(b_contact_centroid, b_facing, a_contact_centroid)
        a_pool = max(1, a_pool + ANGLE_DEF_MOD[a_angle])
        b_pool = max(1, b_pool + ANGLE_DEF_MOD[b_angle])

        # F-ii: puncture bonus for attacker
        # [canonical: tests/sim/sim_mb_06_handoff_2026-05-12.md §(2) Puncture mechanism]
        # A is attacker if it's the one advancing into B (advance_dir toward B)
        # Both are "attackers" of each other — each gets puncture for their own momentum
        a_puncture = puncture_bonus(atom_a, a_contact_orig)
        b_puncture = puncture_bonus(atom_b, b_contact_orig)
        a_pool = a_pool + a_puncture
        b_pool = b_pool + b_puncture

        # Encirclement
        if eng_counts.get(id(atom_a), 0) >= 2: a_pool = max(1, a_pool - ENCIRCLEMENT_PENALTY)
        if eng_counts.get(id(atom_b), 0) >= 2: b_pool = max(1, b_pool - ENCIRCLEMENT_PENALTY)

        a_net = roll_pool(a_pool)
        b_net = roll_pool(b_pool)
        a_deg = compute_degree(a_net, max(1, b_net))
        b_deg = compute_degree(b_net, max(1, a_net))
        dmg_a += max(0, DAMAGE_BY_DEGREE[b_deg](unit_b.power) - unit_a.dr)
        dmg_b += max(0, DAMAGE_BY_DEGREE[a_deg](unit_a.power) - unit_b.dr)
    return {"dmg_a": dmg_a, "dmg_b": dmg_b, "engagements": len(pairs)}


# ─────────────────────────────────────────────────────────────────────────────
# BATTLE
# ─────────────────────────────────────────────────────────────────────────────

def run_battle(unit_a, unit_b, max_turns=15):
    turns = 0
    for t in range(1, max_turns + 1):
        turns = t
        if unit_a.routed or unit_b.routed: break
        pre_pairs = find_contacts(unit_a, unit_b)
        for atom in unit_a.atoms + unit_b.atoms:
            atom.halted_cells = set()
        for p in pre_pairs:
            op_a = oriented_pattern(p["atom_a"].shape, p["atom_a"].tier, p["atom_a"].advance_dir)
            for cell in p["a_cells"]:
                for orig_r, orig_c, or_r, or_c in op_a:
                    abs_r = p["atom_a"].starting_position[0] + or_r + p["atom_a"].cell_offsets.get((orig_r,orig_c), 0) * p["atom_a"].advance_dir
                    abs_c = p["atom_a"].starting_position[1] + or_c + p["atom_a"].cell_offsets_c.get((orig_r,orig_c), 0)
                    if (abs_r, abs_c) == cell:
                        p["atom_a"].halted_cells.add((orig_r, orig_c))
                        break
            op_b = oriented_pattern(p["atom_b"].shape, p["atom_b"].tier, p["atom_b"].advance_dir)
            for cell in p["b_cells"]:
                for orig_r, orig_c, or_r, or_c in op_b:
                    abs_r = p["atom_b"].starting_position[0] + or_r + p["atom_b"].cell_offsets.get((orig_r,orig_c), 0) * p["atom_b"].advance_dir
                    abs_c = p["atom_b"].starting_position[1] + or_c + p["atom_b"].cell_offsets_c.get((orig_r,orig_c), 0)
                    if (abs_r, abs_c) == cell:
                        p["atom_b"].halted_cells.add((orig_r, orig_c))
                        break
        assign_targets(unit_a, unit_b)
        for atom in unit_a.atoms:
            if atom.target_atom:
                atom.advance_cells(unit_a.discipline, atom.target_atom.centroid())
        for atom in unit_b.atoms:
            if atom.target_atom:
                atom.advance_cells(unit_b.discipline, atom.target_atom.centroid())
        pairs = find_contacts(unit_a, unit_b)
        result = resolve_engagements(unit_a, unit_b, pairs)
        size_b_a, size_b_b = unit_a.size, unit_b.size
        unit_a.hp = max(0, unit_a.hp - result["dmg_a"])
        unit_a.recalc_size()
        unit_b.hp = max(0, unit_b.hp - result["dmg_b"])
        unit_b.recalc_size()
        for u, sls, slo in [(unit_a, size_b_a - unit_a.size, size_b_b - unit_b.size),
                              (unit_b, size_b_b - unit_b.size, size_b_a - unit_a.size)]:
            if u.routed or u.broken: continue
            if sls > u.discipline and sls > slo:
                u.discipline = max(0, u.discipline - 1)
            u.check_drift()
        for u in [unit_a, unit_b]:
            if u.routed: continue
            cap = 3; adj = 0
            if u.size < u.size_max // 4 and u.size > 0: adj += -min(2, cap); cap -= 2  # [canonical: tests/sim/sim_mb_06_v7_manifest.md — structural morale thresholds]
            elif u.size < u.size_max // 2: adj += -min(1, cap); cap -= 1  # [canonical: tests/sim/sim_mb_06_v7_manifest.md — structural]
            u.morale = max(1, u.morale + adj)
            if u.morale <= 0: u.routed = True
    winner = ("A" if not unit_a.routed and unit_b.routed else
               "B" if not unit_b.routed and unit_a.routed else "draw")
    return {"winner": winner, "turns": turns}
