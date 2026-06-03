"""mass_battle.config — module-level tunables/constants (behaviour-frozen P-A extract). Canonical comments preserved."""
import os
import os as _os
import os as _sigma_os
import math

__all__ = ['BATTLEFIELD_SIZE', 'UNIT_GRID_SIZE', 'BUFFER_CELLS', 'SIDE_A_START_ROW', 'SIDE_B_START_ROW', 'POOL_VARIANT', 'TIP_SUPPORT_ENABLED', 'TIP_SUPPORT_GAP', 'TROOPS_PER_TIER', 'TROOPS_PER_SIZE', 'ENCIRCLEMENT_PENALTY', 'SUPPORT_STACK_ENABLED', 'SUPPORT_WEIGHTS', 'SUPPORT_WEIGHT_FLOOR', 'PUNCTURE_ENABLED', 'PUNCTURE_CAP', 'CASCADING_ENABLED', 'MAX_SUB_PHASES', 'TICKS_PER_PHASE', 'BLOCK_SIZE', 'CASUALTY_SCALE', 'STAMINA_MAX', 'STAMINA_DRAIN_PER_CONTACT_CELL', 'STAMINA_RECOVERY_PER_RESERVE_RANK', 'STAMINA_POOL_THRESHOLDS', 'STAMINA_EXHAUSTED_POOL_PENALTY', 'ROUT_FLOOR_LOSS_PCT', 'ROUT_EXHAUSTION_MORALE_HIT', 'MORALE_PHASE_CAP', 'DISCIPLINE_LOSS_THRESHOLD', 'VOLLEY_ENABLED', 'VOLLEY_TN', 'RANGED_DR_DEFAULT', 'VOLLEY_MIN_RANGE', 'VOLLEY_MAX_RANGE', 'MIN_DISCIPLINE', 'ANGLE_DEF_MOD', 'STANCE_SPEED_MOD', 'DAMAGE_BY_DEGREE', 'SIGMA_HEAD_ENABLED', 'SIGMA_PER_D', 'RANGED_MELEE_SIGMA', 'MORALE_FIX', 'MORALE_EROSION_DAMP', 'MORALE_SIGMA_SCALE', 'PER_CELL', 'PC_STAMINA_DRAIN', 'PC_STAMINA_REST', 'PC_ROTATE_FLOOR', 'PC_STAM_SIGMA', 'PC_DEPTH_ROTATE', 'PC_FRONTAGE_BLEND', 'PC_FRONTAGE_REF', 'PC_FLANK_CAP', 'PC_REFILL_FLOOR', 'PC_FLANK_DEPTH_RESIST', 'PC_FRONT_RANKS', 'PC_ENVELOP_SIGMA', 'PC_CHARGE_SIGMA', 'PC_SHOCK_FRONT', 'PC_SHOCK_REAR', 'PC_SHOCK_BRACE_FLOOR', 'PC_SHOCK_HOLD_BRACE', 'PC_SHOCK_DISC_FULL', 'PC_SHOCK_DEPTH_FULL', 'PC_SHOCK_DEPTH_REF', 'PC_SHOCK_SHAKEN_GAIN', 'PC_CAVALRY_SPEED_MULT', 'PC_WHEEL', 'REAR_BLIND_DEG', 'FOV_HALF_DEG', 'PC_PIN_REACH', 'PC_REFUSE', 'PC_ENVELOP_MOD', 'PC_ENVELOP_DEPTH_RESIST', 'PC_POCKET_MOD', 'PC_POCKET_REACH', 'LANCHESTER_ENABLED', 'K_LINEAR', 'K_SQUARE', 'LANCHESTER_STRENGTH_REF', 'COMMAND_SIGMA_ENABLED', 'COMMAND_POOL_MULT', 'CMD_CHA_WEIGHT', 'CMD_COG_WEIGHT', 'TROOP_TYPE_ROLES', 'ROLE_SPEC']

BATTLEFIELD_SIZE = 25
UNIT_GRID_SIZE = 15
BUFFER_CELLS = 5
SIDE_A_START_ROW = 16  # symmetric: 4 from center
SIDE_B_START_ROW = 8   # symmetric: 4 from center
POOL_VARIANT = "C-ii"
TIP_SUPPORT_ENABLED = True
TIP_SUPPORT_GAP = 2
TROOPS_PER_TIER = {1: 100, 2: 200, 3: 400, 4: 800}
TROOPS_PER_SIZE = 100
ENCIRCLEMENT_PENALTY = 1
SUPPORT_STACK_ENABLED = True
SUPPORT_WEIGHTS = {1: 1.0, 2: 0.7, 3: 0.5}
SUPPORT_WEIGHT_FLOOR = 0.3
PUNCTURE_ENABLED = True
PUNCTURE_CAP = 3
CASCADING_ENABLED = True
MAX_SUB_PHASES = 5
TICKS_PER_PHASE = 6
BLOCK_SIZE = 100  # [canonical: designs/provincial/mass_battle_v30.md §A.3 — Company scale]
CASUALTY_SCALE = float(_os.environ.get('CASUALTY_SCALE','4'))  # D-B: per-tick lethality. Default 4 = even units take ~3 turns to resolve (playable). TUNING.
STAMINA_MAX = 100
STAMINA_DRAIN_PER_CONTACT_CELL = 1   # drain per cell in contact per tick
STAMINA_RECOVERY_PER_RESERVE_RANK = 8
STAMINA_POOL_THRESHOLDS = [(1, 0)]  # no penalty while stamina > 0
STAMINA_EXHAUSTED_POOL_PENALTY = -1  # stamina == 0: -1 die
ROUT_FLOOR_LOSS_PCT = 0.20          # casualty% at which exhausted unit loses morale floor
ROUT_EXHAUSTION_MORALE_HIT = 1      # morale loss per phase boundary when exhausted
MORALE_PHASE_CAP = 3
DISCIPLINE_LOSS_THRESHOLD = 1.0  # [canonical: params/mass_combat.md §Discipline Degradation]
VOLLEY_ENABLED = True
VOLLEY_TN = 6
RANGED_DR_DEFAULT = 2
VOLLEY_MIN_RANGE = 2
VOLLEY_MAX_RANGE = 8
# SHAPE_OFF_MOD / SHAPE_DEF_MOD RETIRED 2026-06-02 (Jordan design principle): formations grant
# NO flat per-shape bonuses. All formation effects emerge from geometry — frontage (Lanchester),
# depth-damping, support vectors, facing/angle. A formation template is a SHAPE, not a bonus carrier.
MIN_DISCIPLINE = {
    # [canonical: mass_battle_v30.md §ED-815 shape discipline — min disc required by shape]
    "Line": 1, "Arrowhead": 4, "Horseshoe": 5, "GappedLine": 5, "RefusedFlank": 3
}
ANGLE_DEF_MOD = {
    # v11: per-cell octagon. GREEN < 45° = 0D; YELLOW 45-90° = -1D; RED ≥ 90° = -2D.
    # [canonical: Jordan design]
    "GREEN": 0, "YELLOW": -1, "RED": -2,
    "FRONT": 0, "FLANK": -1, "REAR": -2,  # legacy aliases
}
STANCE_SPEED_MOD = {"aggressive": 1, "balanced": 0, "hold": -99, "retreat": 0}
DAMAGE_BY_DEGREE = {"Overwhelming": lambda p: 1+p, "Success": lambda p: p,
                     "Partial": lambda p: 1,        "Failure": lambda p: 0}
SIGMA_HEAD_ENABLED = _sigma_os.environ.get('SIGMA_HEAD', '1') == '1'   # toggle via SIGMA_HEAD env; default ON
SIGMA_PER_D = 0.2            # [class-B sim-tunable] sigma-units per die-equivalent of a legacy pool modifier
RANGED_MELEE_SIGMA = -1.0    # [class-B sim-tunable] ranged-in-melee disadvantage as delta-sigma (replaces pool//3)
MORALE_FIX = _sigma_os.environ.get('MORALE_FIX', '1') == '1'   # toggle; OFF reproduces the pre-fix sigma prototype exactly
MORALE_EROSION_DAMP = 0.7    # [class-B] <1 slows morale erosion -> longer, more attritional battles
MORALE_SIGMA_SCALE  = 0.8    # [class-B] morale->effectiveness: falling morale lowers a unit's sigma-leverage
PER_CELL = _sigma_os.environ.get('PER_CELL', '0') == '1'   # default OFF; ON enables per-column density/depth/fatigue/charge
PC_STAMINA_DRAIN   = 12     # front-column stamina lost per clash it fights
PC_STAMINA_REST    = 5      # a non-engaged (reserve-fed) column recovers this per tick
PC_ROTATE_FLOOR    = 50     # below this a fatigued front rotates if a fresher reserve rank exists
PC_STAM_SIGMA      = 1.5    # fatigue -> delta-sigma (a winded front fights worse; thin lines can't rotate)
PC_DEPTH_ROTATE    = 1.0    # depth fatigue-damping: effective drain = PC_STAMINA_DRAIN/(1+PC_DEPTH_ROTATE*(depth-1))
PC_FRONTAGE_BLEND  = 0.0    # Incr4 contact-fraction: 0=pure width (more cols=more men), 1=pure frontage (depth-neutral)
PC_FRONTAGE_REF    = 7.0    # reference frontage (columns) for the width term normalization
PC_FLANK_CAP       = 3      # max overhang columns that count toward envelopment
PC_REFILL_FLOOR    = 0.60   # column pulls a rear rank forward below this fraction of its start density
PC_FLANK_DEPTH_RESIST = 0.6 # depth blunts flank/overhang delta-sigma
PC_FRONT_RANKS     = 2      # ranks a column must hold on its front; deeper ranks are free to reform to a flank
PC_ENVELOP_SIGMA   = 0.0    # DISABLED: depth-aware contact fraction (Incr4) already captures the width/envelopment
PC_CHARGE_SIGMA    = 0.55   # MAX defender moral-shock delta-sigma on a charge impact (du Picq: cavalry's
                            # weapon is the MORAL impulse, not physical collision). This is a CAP reached only
PC_SHOCK_FRONT       = 0.15  # GREEN (faced) charge: mostly absorbed by the formation (square holds frontally)
PC_SHOCK_REAR        = 1.6   # RED (rear) charge: bracing bypassed (Cannae/Adrianople — cannot face the rear)
PC_SHOCK_BRACE_FLOOR = 0.05  # [canonical: Stage-4 calibration vs Waterloo-square bands] braced+disciplined+deep -> shock ~0 (the square Ney could not break)
PC_SHOCK_HOLD_BRACE  = 0.35  # 'hold' stance (Shield Wall, cannot advance) alone cuts shock to ~1/3
PC_SHOCK_DISC_FULL   = 0.35  # discipline>=5 (steady troops hold formation) cuts shock to ~1/3
PC_SHOCK_DEPTH_FULL  = 0.5   # deep (>=PC_SHOCK_DEPTH_REF ranks) halves shock (mass absorbs)
PC_SHOCK_DEPTH_REF   = 4.0   # rank depth treated as fully "deep"
PC_SHOCK_SHAKEN_GAIN = 1.0   # already-shaken defender (morale<<start) takes up to 2x shock (Hastings-post-feint)
PC_CAVALRY_SPEED_MULT = 2.0  # cavalry velocity primitive: cavalry closes this much faster (PER_CELL), triggering the charge
PC_WHEEL = _sigma_os.environ.get('PC_WHEEL', '1') == '1'   # envelopment wheel: overhang cells wheel toward the enemy flank (PER_CELL); A/B via env
REAR_BLIND_DEG = 150.0                                     # [grounded; Class-B tunable] rear arc a cell cannot perceive
FOV_HALF_DEG = 180.0 - REAR_BLIND_DEG / 2.0                # visible if angle-from-facing <= this (105deg)
PC_PIN_REACH = 1.5                                         # an attacker within this distance in the front arc PINS the cell
PC_REFUSE = _sigma_os.environ.get('PC_REFUSE', '1') == '1' # M3 envelopment (wheel+perception+refusal+wrap+pocket); ACTIVE in the per-cell path (PER_CELL=1). PER_CELL itself still gates the whole layer.
PC_ENVELOP_MOD = float(_sigma_os.environ.get('PC_ENVELOP_MOD', '-1.0'))  # rear-wrap penalty magnitude (M3); tunable
PC_ENVELOP_DEPTH_RESIST = float(_sigma_os.environ.get('PC_ENVELOP_DEPTH_RESIST', '0.3'))  # defender column depth resists the wrap (Clausewitz reserves)
PC_POCKET_MOD = float(_sigma_os.environ.get('PC_POCKET_MOD', '-1.0'))   # surround penalty magnitude
PC_POCKET_REACH = int(_sigma_os.environ.get('PC_POCKET_REACH', '2'))    # lateral column reach to count a flanker

# ─── P-L LANCHESTER ATTRITION SUBSTRATE (D-D; spec designs/audit/2026-06-01-massbattle-stub-wiring/mb_lanchester_design.md 81ea569d) ───
# Linear Law = ancient/melee (casualty rate ∝ enemy strength IN CONTACT, frontage-capped);
# Square Law = ranged/volley (effectiveness ∝ shooter count, cap lifted). Feeds the morale/
# rout system; does NOT replace it (battles still end by rout ~30%, not annihilation).
# OFF reproduces the pre-P-L flat-scale term EXACTLY (A/B). All coefficients class-B sim-tunable, Jordan-vetoable.
LANCHESTER_ENABLED = _sigma_os.environ.get('LANCHESTER_ENABLED', '1') == '1'   # default ON post-validation; OFF = pre-P-L flat scale
K_LINEAR  = float(_sigma_os.environ.get('K_LINEAR', '4'))   # [canonical: mb_lanchester_design.md §3a/§5 — melee linear coeff, rescopes CASUALTY_SCALE; class-B]
K_SQUARE  = float(_sigma_os.environ.get('K_SQUARE', '0.25')) # [canonical: mb_lanchester_design.md §3b/§5 — volley square-law coeff; class-B]
LANCHESTER_STRENGTH_REF = float(_sigma_os.environ.get('LANCHESTER_STRENGTH_REF', '4'))  # [canonical: mb_lanchester_design.md §3a — reference engaged frontage (cols) normalizing the linear factor to ~1 at the mirror; class-B]

# ─── COMMAND-ONLY SIGMA-LEVERAGE BASE (Jordan canon-structure directive 2026-06-02) ───
# The canonical Size-based pool (min(Size,Command)+Command, derived_stats §L276 / PP-233) is
# SET ASIDE: it made per-capita effectiveness size-dependent (degrades below Command), which
# layered super-linearity on the Lanchester linear melee term (measured emergent exponent
# p≈1.7 instead of the linear law's p≈1). Replacement: the base exchange pool is driven SOLELY
# by Command (quality/leverage); numbers (Size) enter outcomes ONLY through the Lanchester
# frontage term. Advantages remain delta-sigma leverage on the sigma head (unchanged).
# OFF reproduces the canonical Size-based pool EXACTLY (A/B). Command becomes DERIVED from
# Charisma (primary weight) + Cognition (secondary weight). All class-B sim-tunable, Jordan-vetoable.
COMMAND_SIGMA_ENABLED = _sigma_os.environ.get('COMMAND_SIGMA_ENABLED', '1') == '1'  # default ON per directive; OFF = canonical Size-based pool
COMMAND_POOL_MULT = float(_sigma_os.environ.get('COMMAND_POOL_MULT', '2'))  # [canonical: Jordan directive 2026-06-02 — Command-only base = MULT×Command; =2 matches min(Size,Command)+Command at Size≥Command; class-B]
CMD_CHA_WEIGHT = float(_sigma_os.environ.get('CMD_CHA_WEIGHT', '2'))  # [canonical: Jordan directive 2026-06-02 — Charisma PRIMARY weight in derived Command; class-B]
CMD_COG_WEIGHT = float(_sigma_os.environ.get('CMD_COG_WEIGHT', '1'))  # [canonical: Jordan directive 2026-06-02 — Cognition SECONDARY weight in derived Command; class-B]

# ─── P-C COMPOSITIONAL-FORMATION ROLES (SCAFFOLD — data only; INERT until the instruction→
# primitive modulation lands, which is behaviour-cascading; see pc_formation_design.md §3.5/§9.1).
# Troop type gates the role menu (the FM "position"→role model). This is a STARTING POINT for the
# historical troop-type/role research — expect the taxonomy and per-type role lists to be revised.
TROOP_TYPE_ROLES = {
    # taxonomy grounded in the historical troop-roles research (Research_Report.md) + design §3.5
    "heavy_infantry":  ["ShieldWall", "Hold", "Anvil", "Push"],
    "light_infantry":  ["Skirmish", "Screen", "Pursue"],
    "cavalry":         ["Shock", "Flanker", "Feint", "Screen", "Pursue"],
    "archers":         ["VolleyLine", "Harass"],
    "mounted_archers": ["Kite", "Harass", "Feint"],   # report's #1 troop type; Kite blocked on the kiting primitive (gap)
    # generic fallbacks for the engine's current coarse troop_type values ('infantry'/'cavalry')
    "infantry":        ["Hold", "Push", "ShieldWall"],
    "any":             ["Support", "Reserve"],
}

# Each role = a typical shape + an instruction package (the FM "role + tactics" model). Instructions
# are the behaviour layer; they MODULATE foundational primitives (brace->density/hold, charge->momentum,
# etc.) and never add flat numbers. Behaviour wiring + calibration is the next step -- the brace mechanism
# in particular needs strengthening per the measured baseline (see pc_formation_design.md). Data only here.
ROLE_SPEC = {
    "ShieldWall": {"shape": "Line",       "instructions": ("brace", "hold")},
    "Hold":       {"shape": "Line",       "instructions": ("hold",)},
    "Anvil":      {"shape": "Line",       "instructions": ("brace", "pin")},
    "Push":       {"shape": "Line",       "instructions": ("advance",)},
    "Skirmish":   {"shape": "GappedLine", "instructions": ("loose", "harass")},
    "Screen":     {"shape": "Line",       "instructions": ("screen",)},
    "Pursue":     {"shape": "Line",       "instructions": ("pursue",)},
    "Shock":      {"shape": "Arrowhead",  "instructions": ("charge",)},
    "Flanker":    {"shape": "Line",       "instructions": ("envelop",)},   # Column shape not yet defined; Line placeholder
    "Feint":      {"shape": "Line",       "instructions": ("lure",)},
    "VolleyLine": {"shape": "Line",       "instructions": ("volley", "hold")},
    "Harass":     {"shape": "GappedLine", "instructions": ("loose", "shoot_move")},
    "Kite":       {"shape": "GappedLine", "instructions": ("kite", "shoot_move")},   # blocked on the kiting primitive
    "Support":    {"shape": "Line",       "instructions": ("reserve",)},
    "Reserve":    {"shape": "Line",       "instructions": ("reserve",)},
}
