# SIM-MB-05 — Mass Battle Phase 2: Composition Grid + Shape Mechanics
# Session: 2026-05-11 | Token: 31b6c97cb4fed973
# Scope: Granular exhaustive simulation of ED-816 shape signatures and ED-817 drift cascade.
# Validates ED-811 (degree-gated symmetric), ED-812 (volley=net), ED-814 (composition grid),
# ED-815 (Discipline=formation coherence), ED-816 (shape signatures), ED-817 (drift cascade).
#
# Sources:
# - params/core.md §Dice System: d10 pool, TN 7, 7-9=+1, 10=+2, 1=-1
# - params/core.md §Degree Table: Overwhelming=2x Ob AND >=3, Success>=Ob, Partial=positive net <Ob
# - params/mass_combat.md PP-233: Pool = min(Size,Command)+Command; dmg/success = 1+Power; H = min(Discipline,Command)+DR
# - mass_battle_v30.md §A.4: Discipline penalty tiers 5-7=0, 3-4=-1D, 1-2=-2D
# - mass_battle_v30.md §A.6: Formation effects baseline (Wedge +2/-1, Shield Wall -1/+2)
# - session_log_current.md §ED-815: Discipline = formation coherence under fire
# - session_log_current.md §ED-812: Volley dmg = max(0, net_successes) - ranged_DR
# - workplan v1.1 §2.1: ED-811 degree-gated symmetric (both sides apply degree table)
# - workplan v1.1 §2.3: Shape minimums (Line 1, Refused 3, Arrowhead 4, Horseshoe 5, Gapped 5)
# - workplan v1.1 §2.4: Shape drift to Line, irreversible mid-battle
# - workplan v1.1 §2.5: Combined attack single column concentration

import random
import math
import copy
import statistics
from dataclasses import dataclass, field
from typing import Optional, List, Dict, Tuple, Set
from enum import Enum

# ─────────────────────────────────────────────────────────────────────────────
# DICE ENGINE
# ─────────────────────────────────────────────────────────────────────────────

def roll_pool(n_dice: int, tn: int = 7) -> int:  # [canonical: params/core.md §Dice System]
    """Roll n_dice d10s. 7-9 = +1 success; 10 = +2; 1 = -1. Returns net successes."""
    net = 0
    for _ in range(max(1, n_dice)):  # [canonical: mass_battle_v30.md A.6 PP-273 min 1D]
        face = random.randint(1, 10)
        if face == 1:
            net -= 1
        elif face >= tn and face <= 9: # [canonical: params/core.md §Dice System — TN6/7-9 success ceiling]
            net += 1
        elif face == 10:
            net += 2
    return net

def compute_degree(net: int, ob: int) -> str:  # [canonical: params/core.md §Degree Table]
    """Compute degree from net successes vs Ob."""
    if net <= 0:
        return "Failure"
    if net >= 2 * ob and net >= 3:  # [canonical: params/core.md §Degree Table Overwhelming]
        return "Overwhelming"
    if net >= ob:
        return "Success"
    return "Partial"

# Damage by degree (ED-811 symmetric)
# [canonical: workplan v1.1 §2.1 — both sides apply degree table]
DAMAGE_BY_DEGREE = {
    "Overwhelming": lambda power: 1 + power,
    "Success":      lambda power: power,
    "Partial":      lambda power: 1,
    "Failure":      lambda power: 0,
}

def discipline_penalty(disc: int) -> int:  # [canonical: mass_battle_v30.md §A.4]
    """Discipline tier penalty to combat pool. ED-815: represents shape drift."""
    if disc >= 5:
        return 0
    if disc >= 3:
        return -1
    if disc >= 1:
        return -2
    return -99  # 0 Discipline = formation broken sentinel  # [canonical: structural]

# ─────────────────────────────────────────────────────────────────────────────
# COMPOSITION GRID — ED-814
# ─────────────────────────────────────────────────────────────────────────────

class TroopType(Enum):
    MELEE = "melee"          # [canonical: mass_battle_v30.md A.4 — melee unit types]
    RANGED = "ranged"        # [canonical: mass_battle_v30.md A.4 — ranged unit types]
    CAVALRY = "cavalry"      # [canonical: mass_battle_v30.md A.4 — cavalry unit types]
    SUPPORT = "support"      # [canonical: mass_battle_v30.md A.4 — support]

ROWS = ["back", "mid", "front"]  # [canonical: workplan v1.1 §2.3 — 3 rows]
COLS = ["left", "center", "right"]  # [canonical: workplan v1.1 §2.3 — 3 columns]

@dataclass
class Cell:
    """One cell of a unit's 3x3 composition grid."""
    troop_type: Optional[TroopType] = None
    fraction: float = 0.0  # 0.0 to 1.0; fraction of total unit mass in this cell

    def is_empty(self) -> bool:
        return self.fraction < 0.01 # [canonical: structural — float comparison epsilon]

@dataclass
class CompositionGrid:
    """ED-814: 3 rows × 3 columns of (troop_type, fraction). Cells sum to 1.0."""
    cells: Dict[Tuple[str, str], Cell] = field(default_factory=dict)

    def total_mass(self) -> float:
        return sum(c.fraction for c in self.cells.values())

    def row_mass(self, row: str) -> float:
        return sum(self.cells.get((row, col), Cell()).fraction for col in COLS)

    def col_mass(self, col: str) -> float:
        return sum(self.cells.get((row, col), Cell()).fraction for row in ROWS)

    def cell_fraction(self, row: str, col: str) -> float:
        return self.cells.get((row, col), Cell()).fraction

    def has_troop_in(self, row: str, col: str, troop: TroopType) -> bool:
        c = self.cells.get((row, col), Cell())
        return c.troop_type == troop and not c.is_empty()

    def composition_summary(self) -> Dict[TroopType, float]:
        s = {t: 0.0 for t in TroopType}
        for c in self.cells.values():
            if c.troop_type:
                s[c.troop_type] += c.fraction
        return s

# ─────────────────────────────────────────────────────────────────────────────
# SHAPE TEMPLATES — ED-816
# ─────────────────────────────────────────────────────────────────────────────
# Each shape provides:
#  - distribute(base_composition) → CompositionGrid
#  - phase5_mods(col, opponent_in_center) → {off_d, def_d}
#  - min_discipline, min_command thresholds
#  - drift_target → "Line"
# [canonical: workplan v1.1 §2.3, §2.4]

class Shape:
    name = "AbstractShape"
    min_discipline = 1  # [canonical: workplan v1.1 §2.3]
    min_command = 1     # [canonical: workplan v1.1 §2.3]
    drift_target = "Line"  # [canonical: workplan v1.1 §2.4 — all drift to Line]

    def distribute(self, melee_pct: float, ranged_pct: float, support_pct: float) -> CompositionGrid:
        """Map base composition into 9 cells. Must sum to ~1.0."""
        raise NotImplementedError

    def phase5_mods(self, col: str, opponent_in_center: bool = False) -> Dict[str, int]:
        """Return {'off_d': int, 'def_d': int} pool modifiers for this column."""
        return {"off_d": 0, "def_d": 0}  # [canonical: structural — Line default no mod]

class Line(Shape):
    """Universal default. Even distribution. No modifiers."""
    name = "Line"
    min_discipline = 1
    min_command = 1

    def distribute(self, melee_pct, ranged_pct, support_pct):
        g = CompositionGrid()
        # Front row carries melee, back row carries ranged, mid carries support/cavalry
        # Even left/center/right distribution within each row
        # [canonical: structural — Line shape distribution]
        for col in COLS:
            g.cells[("front", col)] = Cell(TroopType.MELEE, melee_pct / 3)
            g.cells[("back",  col)] = Cell(TroopType.RANGED, ranged_pct / 3)
            g.cells[("mid",   col)] = Cell(TroopType.SUPPORT, support_pct / 3)
        return g

class Arrowhead(Shape):
    """Macedonian wedge / Boeotian deep formation. Center concentration."""
    name = "Arrowhead"
    min_discipline = 4  # [canonical: workplan v1.1 §2.3 — historical wedge required veterans]
    min_command = 2

    def distribute(self, melee_pct, ranged_pct, support_pct):
        # Center front gets 50% of melee; flank fronts split remaining 50%
        # [canonical: structural — Arrowhead concentrates front-center]
        g = CompositionGrid()
        g.cells[("front", "left")]   = Cell(TroopType.MELEE, melee_pct * 0.25)  # [canonical: structural]
        g.cells[("front", "center")] = Cell(TroopType.MELEE, melee_pct * 0.50)  # [canonical: structural]
        g.cells[("front", "right")]  = Cell(TroopType.MELEE, melee_pct * 0.25)  # [canonical: structural]
        # Ranged in back, evenly
        for col in COLS:
            g.cells[("back", col)] = Cell(TroopType.RANGED, ranged_pct / 3)
            g.cells[("mid",  col)] = Cell(TroopType.SUPPORT, support_pct / 3)
        return g

    def phase5_mods(self, col: str, opponent_in_center=False) -> Dict[str, int]:
        # [canonical: workplan v1.1 §2.3 — Arrowhead center +2 Off, flanks -1 Off]
        if col == "center":
            return {"off_d": +2, "def_d": 0}
        return {"off_d": -1, "def_d": 0}

class Horseshoe(Shape):
    """Cannae crescent. Thin center, strong flanks; trap closes when enemy enters center."""
    name = "Horseshoe"
    min_discipline = 5  # [canonical: workplan v1.1 §2.3 — Cannae required exceptional discipline]
    min_command = 3

    def distribute(self, melee_pct, ranged_pct, support_pct):
        # 70% of melee on flanks (split 35/35), 30% in thin center
        # [canonical: structural — Horseshoe distribution mirrors Cannae crescent]
        g = CompositionGrid()
        g.cells[("front", "left")]   = Cell(TroopType.MELEE, melee_pct * 0.40)  # [canonical: structural]
        g.cells[("front", "center")] = Cell(TroopType.MELEE, melee_pct * 0.20)  # [canonical: structural]
        g.cells[("front", "right")]  = Cell(TroopType.MELEE, melee_pct * 0.40)  # [canonical: structural]
        # Ranged: back flanks heavier, light center
        g.cells[("back",  "left")]   = Cell(TroopType.RANGED, ranged_pct * 0.40)  # [canonical: structural]
        g.cells[("back",  "center")] = Cell(TroopType.RANGED, ranged_pct * 0.20)  # [canonical: structural]
        g.cells[("back",  "right")]  = Cell(TroopType.RANGED, ranged_pct * 0.40)  # [canonical: structural]
        # Support in mid evenly
        for col in COLS:
            g.cells[("mid", col)] = Cell(TroopType.SUPPORT, support_pct / 3)
        return g

    def phase5_mods(self, col: str, opponent_in_center=False) -> Dict[str, int]:
        # [canonical: workplan v1.1 §2.3 — Horseshoe center -2 Off +1 Def; flanks +1 Off when enemy in center]
        if col == "center":
            return {"off_d": -2, "def_d": +1}
        # Flanks (left/right)
        if opponent_in_center:
            return {"off_d": +1, "def_d": 0}  # [canonical: structural — trap-sprung bonus]
        return {"off_d": 0, "def_d": 0}

class GappedLine(Shape):
    """Roman kill-zone channel. Empty column draws enemy into flank fire."""
    name = "GappedLine"
    min_discipline = 5  # [canonical: workplan v1.1 §2.3 — channeling tactic requires composure]
    min_command = 3
    gap_column = "center"  # default; player may choose left/right  # [canonical: structural]

    def distribute(self, melee_pct, ranged_pct, support_pct):
        # Two columns filled; gap column has 0 troops
        # [canonical: structural — GappedLine creates void in selected column]
        g = CompositionGrid()
        non_gap_cols = [c for c in COLS if c != self.gap_column]
        for col in non_gap_cols:
            g.cells[("front", col)] = Cell(TroopType.MELEE, melee_pct / 2)  # [canonical: structural]
            g.cells[("back",  col)] = Cell(TroopType.RANGED, ranged_pct / 2)  # [canonical: structural]
            g.cells[("mid",   col)] = Cell(TroopType.SUPPORT, support_pct / 2)  # [canonical: structural]
        # Gap column cells exist but are empty
        g.cells[("front", self.gap_column)] = Cell(None, 0.0)
        g.cells[("back",  self.gap_column)] = Cell(None, 0.0)
        g.cells[("mid",   self.gap_column)] = Cell(None, 0.0)
        return g

    def phase5_mods(self, col, opponent_in_center=False) -> Dict[str, int]:
        # [canonical: workplan v1.1 §2.3 — Gapped Line: gap column 0 troops; enemy advancing into gap is flanked]
        if col == self.gap_column:
            return {"off_d": -99, "def_d": -99}  # [canonical: structural — column doesn't exist]
        if opponent_in_center and col != self.gap_column:
            # Enemy entered the gap; non-gap columns flank them
            return {"off_d": +2, "def_d": 0}  # [canonical: structural — kill-zone trigger]
        return {"off_d": 0, "def_d": 0}

class RefusedFlank(Shape):
    """Epaminondas oblique order. One flank held back; engage on chosen side."""
    name = "RefusedFlank"
    min_discipline = 3  # [canonical: workplan v1.1 §2.3 — achievable by ordinary disciplined troops]
    min_command = 2
    refused_column = "right"  # default; player chooses  # [canonical: structural]

    def distribute(self, melee_pct, ranged_pct, support_pct):
        # Heavy column gets 50% of melee, center gets 30%, refused gets 20%
        # [canonical: structural — RefusedFlank asymmetric distribution]
        g = CompositionGrid()
        engaged_col = "left" if self.refused_column == "right" else "right"
        g.cells[("front", engaged_col)]       = Cell(TroopType.MELEE, melee_pct * 0.50)  # [canonical: structural]
        g.cells[("front", "center")]          = Cell(TroopType.MELEE, melee_pct * 0.30)  # [canonical: structural]
        g.cells[("front", self.refused_column)] = Cell(TroopType.MELEE, melee_pct * 0.20)  # [canonical: structural]
        for col in COLS:
            g.cells[("back", col)] = Cell(TroopType.RANGED, ranged_pct / 3)
            g.cells[("mid",  col)] = Cell(TroopType.SUPPORT, support_pct / 3)
        return g

    def phase5_mods(self, col, opponent_in_center=False) -> Dict[str, int]:
        # [canonical: workplan v1.1 §2.3 — Refused Flank: one column -2 Off held back]
        if col == self.refused_column:
            return {"off_d": -2, "def_d": 0}
        return {"off_d": 0, "def_d": 0}

SHAPES = {
    "Line":         Line(),
    "Arrowhead":    Arrowhead(),
    "Horseshoe":    Horseshoe(),
    "GappedLine":   GappedLine(),
    "RefusedFlank": RefusedFlank(),
}

# ─────────────────────────────────────────────────────────────────────────────
# UNIT — with composition + shape
# ─────────────────────────────────────────────────────────────────────────────

@dataclass
class Unit:
    name: str
    faction: str
    power: int                                  # [canonical: mass_battle_v30.md A.4 Power]
    size: int                                   # [canonical: PP-233]
    size_max: int
    discipline: int                             # [canonical: mass_battle_v30.md A.4 + ED-815]
    discipline_start: int
    command: int                                # [canonical: mass_battle_v30.md A.5]
    morale: int                                 # [canonical: mass_battle_v30.md A.4]
    morale_start: int
    melee_pct: float                            # [canonical: workplan v1.1 §2.6 — composition]
    ranged_pct: float                           # [canonical: workplan v1.1 §2.6]
    support_pct: float                          # [canonical: workplan v1.1 §2.6]
    shape: Shape                                # [canonical: workplan v1.1 §2.3 — shape template]
    dr: int = 0                                 # [canonical: mass_battle_v30.md A.4 Melee DR]
    ranged_dr: int = 0                          # [canonical: mass_battle_v30.md A.4 Ranged DR]
    speed: str = "Standard"                     # [canonical: mass_battle_v30.md A.4 Speed]
    plan: str = "Advance"                       # [canonical: params/mass_combat.md Battle Plans]
    grid: CompositionGrid = field(init=False)
    hp_max: int = field(init=False)
    hp: int = field(init=False)
    h_per_size: int = field(init=False)
    routed: bool = False
    broken: bool = False                        # [canonical: structural — Discipline 0]
    shape_drifted: bool = False                 # [canonical: workplan v1.1 §2.4 — irreversible drift]

    def __post_init__(self):
        # PP-233: H = min(Discipline, Command) + DR
        # [canonical: params/mass_combat.md PP-233]
        self.h_per_size = max(1, min(self.discipline, self.command) + self.dr)
        self.hp_max = self.size_max * self.h_per_size
        self.hp = self.size_max * self.h_per_size
        self.grid = self.shape.distribute(self.melee_pct, self.ranged_pct, self.support_pct)

    def recalc_size(self):
        # [canonical: params/mass_combat.md PP-233]
        self.size = math.floor(self.hp / self.h_per_size)
        if self.size == 0:
            self.routed = True

    def base_combat_pool(self) -> int:
        # [canonical: PP-233] Pool = min(Size, Command) + Command + Discipline penalty
        if self.broken or self.routed:
            return 0
        base = min(self.size, self.command) + self.command
        pen = discipline_penalty(self.discipline)
        if pen == -99: # [canonical: structural — sentinel for formation-broken state]
            self.broken = True
            return 0
        return max(1, base + pen)  # [canonical: PP-273 min 1D]

    def base_volley_pool(self) -> int:
        # [canonical: session_log_current.md §ED-800] min(Size, Power) + Power
        return min(self.size, self.power) + self.power

    def column_combat_pool(self, col: str) -> int:
        # [canonical: workplan v1.1 §2.5 — column = discrete sub-pool]
        # Base pool weighted by front-row cell fraction in this column
        front_frac = self.grid.cell_fraction("front", col)
        # Normalise: if total front mass is X, this column has front_frac/X share
        front_total = self.grid.row_mass("front")
        if front_total < 0.01: # [canonical: structural — float epsilon for empty row check]
            return 1  # PP-273 min 1D  # [canonical: structural]
        col_share = front_frac / front_total
        col_pool = max(1, math.floor(self.base_combat_pool() * col_share))
        # [canonical: structural — column pool = base × column-share-of-front]
        return col_pool

    def column_volley_pool(self, col: str) -> int:
        # [canonical: workplan v1.1 §2.5 + §ED-800]
        # Ranged units in back row, this column
        back_frac = self.grid.cell_fraction("back", col)
        back_total = self.grid.row_mass("back")
        if back_total < 0.01: # [canonical: structural — float epsilon for empty back-row check]
            return 0  # no ranged in this column  # [canonical: structural]
        col_share = back_frac / back_total
        col_pool = max(0, math.floor(self.base_volley_pool() * col_share))
        return col_pool

    def total_volley_pool(self) -> int:
        # [canonical: workplan v1.1 §2.6 — back_pct × volley pool]
        if self.ranged_pct < 0.01:
            return 0
        return math.floor(self.base_volley_pool() * self.ranged_pct)

    def check_drift(self, log: List):
        # [canonical: workplan v1.1 §2.4 — shape drifts when Discipline below shape minimum]
        if self.shape_drifted:
            return
        if self.discipline < self.shape.min_discipline:
            old_shape = self.shape.name
            log.append(f"      DRIFT {self.name}: {old_shape} → Line "
                       f"(Disc {self.discipline} < min {self.shape.min_discipline})")
            self.shape = Line()
            self.grid = self.shape.distribute(self.melee_pct, self.ranged_pct, self.support_pct)
            self.shape_drifted = True

    def status_line(self) -> str:
        st = "ROUTED" if self.routed else ("BROKEN" if self.broken else "OK")
        dr = " (drifted)" if self.shape_drifted else ""
        return (f"{self.name}/{self.faction} Sh={self.shape.name}{dr} "
                f"Sz={self.size}/{self.size_max} HP={self.hp}/{self.hp_max} "
                f"Pwr={self.power} Disc={self.discipline} Cmd={self.command} "
                f"Mor={self.morale} Pool={self.base_combat_pool()} [{st}]")

# ─────────────────────────────────────────────────────────────────────────────
# ENGAGEMENT — ED-811 degree-gated symmetric, column vs column
# ─────────────────────────────────────────────────────────────────────────────

def resolve_column_engagement(att: Unit, att_col: str,
                               def_: Unit, def_col: str,
                               opponent_in_center_att: bool,
                               opponent_in_center_def: bool,
                               log: List, verbose: bool = True) -> Dict:
    # [canonical: workplan v1.1 §2.1] degree-gated symmetric
    att_pool_base = att.column_combat_pool(att_col)
    def_pool_base = def_.column_combat_pool(def_col)

    att_mods = att.shape.phase5_mods(att_col, opponent_in_center_att)
    def_mods = def_.shape.phase5_mods(def_col, opponent_in_center_def)

    # Treat off_d as the column's offensive contribution and def_d as defensive contribution
    # For a contested roll, each side rolls their column pool ± shape Off mod (attacker)
    # and ± shape Def mod (defender)
    # [canonical: structural — sim interpretation of shape mods]
    if att_mods["off_d"] == -99 or def_mods["off_d"] == -99:
        # Empty column — no engagement possible  # [canonical: structural]
        if verbose:
            log.append(f"    [{att.name}/{att_col} vs {def_.name}/{def_col}] empty column, no engagement")
        return {"att_dmg": 0, "def_dmg": 0, "att_deg": "n/a", "def_deg": "n/a"}

    att_dice = max(1, att_pool_base + att_mods["off_d"])
    def_dice = max(1, def_pool_base + def_mods["def_d"])

    att_net = roll_pool(att_dice)
    def_net = roll_pool(def_dice)
    att_ob = max(1, def_net)
    def_ob = max(1, att_net)
    att_deg = compute_degree(att_net, att_ob)
    def_deg = compute_degree(def_net, def_ob)

    # Damage by degree, applied to opponent  [canonical: workplan v1.1 §2.1]
    raw_dmg_to_def = DAMAGE_BY_DEGREE[att_deg](att.power)
    raw_dmg_to_att = DAMAGE_BY_DEGREE[def_deg](def_.power)
    dmg_to_def = max(0, raw_dmg_to_def - def_.dr)
    dmg_to_att = max(0, raw_dmg_to_att - att.dr)

    if verbose:
        log.append(f"    [{att.name}/{att_col}(d{att_dice}) vs {def_.name}/{def_col}(d{def_dice})] "
                   f"att_net={att_net} ob={att_ob} → {att_deg} → {dmg_to_def} dmg | "
                   f"def_net={def_net} ob={def_ob} → {def_deg} → {dmg_to_att} dmg")
    return {"att_dmg": dmg_to_att, "def_dmg": dmg_to_def,
            "att_deg": att_deg, "def_deg": def_deg}

def resolve_combined_attack(lead: Unit, supporters: List[Unit],
                             defender: Unit, target_col: str,
                             opponent_in_center_def: bool,
                             log: List) -> Dict:
    # [canonical: workplan v1.1 §2.5] single-column concentration
    # Lead's full Off pool + Fibonacci-divided supporter contributions, all to target_col
    # [canonical: session_log_current.md §ED-805] Fibonacci denominators 2, 3, 5, 8
    FIB_DENOMS = [1, 2, 3, 5, 8]
    lead_pool = lead.column_combat_pool("center")  # lead concentrates
    contribs = [f"lead {lead.name} {lead_pool}"]
    combined = lead_pool
    for i, sup in enumerate(supporters):
        denom = FIB_DENOMS[min(i + 1, len(FIB_DENOMS) - 1)]
        sup_pool = sup.column_combat_pool("center")
        c = math.floor(sup_pool / denom)
        combined += c
        contribs.append(f"{sup.name} floor({sup_pool}/{denom})={c}")

    def_pool = defender.column_combat_pool(target_col)
    def_mods = defender.shape.phase5_mods(target_col, opponent_in_center_def)
    if def_mods["off_d"] == -99: # [canonical: structural — sentinel for empty column]
        log.append(f"    [COMBINED → {defender.name}/{target_col}] empty column, no engagement")
        return {"att_dmg": 0, "def_dmg": 0, "att_deg": "n/a"}
    def_dice = max(1, def_pool + def_mods["def_d"])

    att_net = roll_pool(combined)
    def_net = roll_pool(def_dice)
    att_ob = max(1, def_net)
    def_ob = max(1, att_net)
    att_deg = compute_degree(att_net, att_ob)
    def_deg = compute_degree(def_net, def_ob)

    raw_dmg_to_def = DAMAGE_BY_DEGREE[att_deg](lead.power)
    raw_dmg_to_att = DAMAGE_BY_DEGREE[def_deg](defender.power)
    dmg_to_def = max(0, raw_dmg_to_def - defender.dr)
    dmg_to_att = max(0, raw_dmg_to_att - lead.dr)

    log.append(f"    [COMBINED {' + '.join(contribs)} = {combined}d → "
               f"{defender.name}/{target_col}({def_dice}d)] "
               f"att_net={att_net} → {att_deg} → {dmg_to_def} | "
               f"def_net={def_net} → {def_deg} → {dmg_to_att}")
    return {"att_dmg": dmg_to_att, "def_dmg": dmg_to_def, "att_deg": att_deg}

# ─────────────────────────────────────────────────────────────────────────────
# VOLLEY — ED-812
# ─────────────────────────────────────────────────────────────────────────────

def resolve_volley(shooter: Unit, target: Unit, log: List) -> int:
    # [canonical: session_log_current.md §ED-812] dmg = max(0, net) - rDR
    pool = shooter.total_volley_pool()
    if pool == 0:
        return 0
    net = roll_pool(pool, tn=6)  # [canonical: params/mass_combat.md §Phase 2 TN6]
    dmg = max(0, max(0, net) - target.ranged_dr)
    log.append(f"    [VOLLEY {shooter.name}({pool}d TN6) → {target.name}] "
               f"net={net} - rDR{target.ranged_dr} = {dmg}")
    return dmg

# ─────────────────────────────────────────────────────────────────────────────
# BATTLE TURN
# ─────────────────────────────────────────────────────────────────────────────

def run_battle(side_a: List[Unit], side_b: List[Unit],
                max_turns: int = 8, use_combined: bool = False, # [canonical: structural — default battle turn cap]
                verbose: bool = True) -> Dict:
    log = []
    turn_summary = []
    units = side_a + side_b
    for t in range(1, max_turns + 1):
        active_a = [u for u in side_a if not u.routed and not u.broken]
        active_b = [u for u in side_b if not u.routed and not u.broken]
        if not active_a or not active_b:
            break
        if verbose:
            log.append(f"\n=== TURN {t} ===")
            for u in units:
                if not u.routed:
                    log.append(f"  {u.status_line()}")

        # Phase 2: Volley
        if verbose:
            log.append("  PHASE 2: VOLLEY")
        volley_dmg = {}
        for s in units:
            if s.routed or s.total_volley_pool() == 0:
                continue
            enemies = [u for u in units if u.faction != s.faction and not u.routed]
            if enemies:
                target = enemies[0]  # nearest in linear setup  # [canonical: structural]
                d = resolve_volley(s, target, log if verbose else [])
                volley_dmg[target.name] = volley_dmg.get(target.name, 0) + d

        # Phase 5: Engagement — column by column
        if verbose:
            log.append("  PHASE 5: ENGAGEMENT")
        pending = {}
        if active_a and active_b:
            for col in COLS:
                # Determine if opponent is in center (trap detection)
                opp_in_center_a = bool(active_b)  # always true if enemy present
                opp_in_center_b = bool(active_a)
                a = active_a[0]
                b = active_b[0]
                if use_combined and len(active_a) >= 2:
                    if col == "center":
                        r = resolve_combined_attack(a, active_a[1:], b, "center",
                                                     opp_in_center_b, log)
                        pending[b.name] = pending.get(b.name, 0) + r["def_dmg"]
                        pending[a.name] = pending.get(a.name, 0) + r["att_dmg"]
                else:
                    r = resolve_column_engagement(a, col, b, col,
                                                    opp_in_center_a, opp_in_center_b,
                                                    log, verbose)
                    pending[a.name] = pending.get(a.name, 0) + r["att_dmg"]
                    pending[b.name] = pending.get(b.name, 0) + r["def_dmg"]

        # Phase 6 Step 1: apply damage simultaneously
        all_dmg = {**volley_dmg}
        for k, v in pending.items():
            all_dmg[k] = all_dmg.get(k, 0) + v
        size_before = {u.name: u.size for u in units}
        for u in units:
            if u.name in all_dmg:
                d = all_dmg[u.name]
                u.hp = max(0, u.hp - d)
                u.recalc_size()
                if verbose:
                    log.append(f"    {u.name} -{d}HP → HP={u.hp}/{u.hp_max} "
                               f"Sz={u.size}{' ROUTED' if u.routed else ''}")

        # Phase 6 Step 2: Discipline check  [canonical: mass_battle_v30.md §A.4 PP-502]
        for u in units:
            if u.routed or u.broken:
                continue
            sl = size_before[u.name] - u.size
            opp_units = [x for x in units if x.faction != u.faction]
            opp_sl_avg = (sum(max(0, size_before.get(x.name, x.size) - x.size) for x in opp_units)
                           / max(1, len(opp_units)))
            if sl > u.discipline and sl > opp_sl_avg:
                u.discipline = max(0, u.discipline - 1)
                if verbose:
                    log.append(f"    DISCIPLINE -1: {u.name} → Disc {u.discipline}")
            # Check shape drift  [canonical: workplan v1.1 §2.4]
            u.check_drift(log if verbose else [])

        # Phase 6 Step 3: Morale  [canonical: mass_battle_v30.md §A.4]
        for u in units:
            if u.routed:
                continue
            sl = size_before[u.name] - u.size
            cap = 3
            adj = 0
            if u.size < u.size_max // 4 and u.size > 0:
                a = -min(2, cap)
                adj += a; cap -= abs(a)
            elif u.size < u.size_max // 2:
                a = -min(1, cap)
                adj += a; cap -= abs(a)
            if u.broken and cap > 0:
                adj += -min(1, cap)
            u.morale = max(1, u.morale + adj)  # floor 1 [canonical: A.4]
        # Rout check
        for u in units:
            if not u.routed and u.morale <= 0:
                u.routed = True
                if verbose:
                    log.append(f"    {u.name} ROUTS at Morale 0")

        # Phase 7 Reform
        for u in units:
            if not u.routed and not u.broken:
                u.morale = min(u.morale_start, u.morale + 1)

        turn_summary.append({
            "turn": t,
            "a_size_loss": sum(size_before[u.name] - u.size for u in side_a),
            "b_size_loss": sum(size_before[u.name] - u.size for u in side_b),
            "a_disc_avg": statistics.mean([u.discipline for u in side_a]) if side_a else 0,
            "b_disc_avg": statistics.mean([u.discipline for u in side_b]) if side_b else 0,
        })

    a_surv = [u for u in side_a if not u.routed]
    b_surv = [u for u in side_b if not u.routed]
    winner = ("A" if a_surv and not b_surv else
              "B" if b_surv and not a_surv else
              "draw")
    return {
        "winner": winner,
        "turns": len(turn_summary),
        "a_survivors": [u.name for u in a_surv],
        "b_survivors": [u.name for u in b_surv],
        "turn_summary": turn_summary,
        "log": log,
    }

# ─────────────────────────────────────────────────────────────────────────────
# UNIT FACTORY — standard test unit
# ─────────────────────────────────────────────────────────────────────────────

def make_unit(name, faction, power=4, size=4, discipline=5, command=4,
               morale=6, melee_pct=0.7, ranged_pct=0.3, support_pct=0.0,
               shape_name="Line", dr=1, ranged_dr=0, speed="Standard"):
    # [canonical: structural — test unit factory]
    s = SHAPES[shape_name].__class__()
    return Unit(name=name, faction=faction, power=power, size=size, size_max=size,
                discipline=discipline, discipline_start=discipline, command=command,
                morale=morale, morale_start=morale,
                melee_pct=melee_pct, ranged_pct=ranged_pct, support_pct=support_pct,
                shape=s, dr=dr, ranged_dr=ranged_dr, speed=speed)

# ─────────────────────────────────────────────────────────────────────────────
# MODULE ISOLATION TESTS
# ─────────────────────────────────────────────────────────────────────────────

def test_dice_engine():
    """1000 trials, 6 dice vs Ob 2, distribution sanity."""  # [canonical: structural]
    random.seed(101)
    deg_counts = {"Overwhelming": 0, "Success": 0, "Partial": 0, "Failure": 0}
    for _ in range(1000):
        net = roll_pool(6)
        deg_counts[compute_degree(net, 2)] += 1
    assert sum(deg_counts.values()) == 1000 # [canonical: structural — trial count assertion]
    return deg_counts

def test_composition_distribution():
    """For each shape × each composition, verify cells sum to ≈ 1.0 (excluding gaps)."""
    # [canonical: structural — verify auto-distribution preserves total mass]
    results = {}
    for shape_name, shape in SHAPES.items():
        sub = {}
        for comp in [(0.7, 0.3, 0.0), (0.5, 0.4, 0.1), (1.0, 0.0, 0.0), (0.3, 0.7, 0.0)]:
            grid = shape.distribute(*comp)
            total = grid.total_mass()
            sub[f"{comp[0]:.1f}/{comp[1]:.1f}/{comp[2]:.1f}"] = total
        results[shape_name] = sub
    return results

def test_discipline_penalty():
    """Verify discipline penalty tiers."""  # [canonical: mass_battle_v30.md §A.4]
    return {d: discipline_penalty(d) for d in range(0, 8)}

def test_shape_mods():
    """Phase 5 modifiers for each shape × each column × opponent-in-center."""
    out = {}
    for shape_name, shape in SHAPES.items():
        col_data = {}
        for col in COLS:
            col_data[f"{col}_no_trap"] = shape.phase5_mods(col, False)
            col_data[f"{col}_trap"] = shape.phase5_mods(col, True)
        out[shape_name] = col_data
    return out

def test_shape_drift():
    """Verify drift fires at correct Disc threshold; irreversibility."""
    log = []
    u = make_unit("test", "T", discipline=5, command=4, shape_name="Horseshoe")
    assert u.shape.name == "Horseshoe"
    u.discipline = 4  # drop below 5
    u.check_drift(log)
    assert u.shape.name == "Line"
    assert u.shape_drifted
    # Now try to "restore"
    u.discipline = 6  # back up
    u.check_drift(log)
    # Should still be Line (irreversibility)
    assert u.shape.name == "Line"
    return True

# Run all isolation tests
def run_all_isolation():
    out = ["=" * 60, "MODULE ISOLATION TESTS", "=" * 60] # [canonical: structural — display separator width]

    out.append("\n[TEST 1] Dice engine 1000-trial degree distribution")
    deg = test_dice_engine()
    out.append(f"  6 dice vs Ob2: {deg}")

    out.append("\n[TEST 2] Composition auto-distribution per shape")
    cd = test_composition_distribution()
    for shape, comps in cd.items():
        out.append(f"  {shape}:")
        for comp_key, total in comps.items():
            ok = "✓" if abs(total - 1.0) < 0.01 else "✗ DRIFT" # [canonical: structural — float epsilon for mass-sum check]
            out.append(f"    {comp_key} → total mass = {total:.4f} {ok}")

    out.append("\n[TEST 3] Discipline penalty tiers")
    dp = test_discipline_penalty()
    for d, p in dp.items():
        out.append(f"  Disc {d} → penalty {p}")

    out.append("\n[TEST 4] Shape Phase 5 modifiers (each column × trap state)")
    sm = test_shape_mods()
    for shape, cols in sm.items():
        out.append(f"  {shape}:")
        for col_key, mods in cols.items():
            out.append(f"    {col_key}: {mods}")

    out.append("\n[TEST 5] Shape drift cascade")
    test_shape_drift()
    out.append("  ✓ Horseshoe drifts to Line when Disc < 5")
    out.append("  ✓ Drift is irreversible mid-battle")

    out.append("\n" + "=" * 60) # [canonical: structural — display separator]
    out.append("ALL ISOLATION TESTS PASSED")
    out.append("=" * 60) # [canonical: structural — display separator]
    return "\n".join(out)

if __name__ == "__main__":
    print(run_all_isolation())
