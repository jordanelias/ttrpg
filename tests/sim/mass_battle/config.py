"""mass_battle.config — module-level tunables/constants (behaviour-frozen P-A extract). Canonical comments preserved."""
import os
import os as _os
import os as _sigma_os
import math

__all__ = ['BATTLEFIELD_SIZE', 'UNIT_GRID_SIZE', 'BUFFER_CELLS', 'SIDE_A_START_ROW', 'SIDE_B_START_ROW', 'POOL_VARIANT', 'TIP_SUPPORT_ENABLED', 'TIP_SUPPORT_GAP', 'TROOPS_PER_TIER', 'TROOPS_PER_SIZE', 'CELL_FLOOR', 'CELL_CAP', 'SUBUNIT_ROUT_FLOOR', 'MAX_TROOPS_PER_UNIT', 'LINE_ASPECT', 'ENCIRCLEMENT_PENALTY', 'SUPPORT_STACK_ENABLED', 'SUPPORT_WEIGHTS', 'SUPPORT_WEIGHT_FLOOR', 'PUNCTURE_ENABLED', 'PUNCTURE_CAP', 'CASCADING_ENABLED', 'MAX_SUB_PHASES', 'TICKS_PER_PHASE', 'BLOCK_SIZE', 'CASUALTY_SCALE', 'STAMINA_MAX', 'STAMINA_DRAIN_PER_CONTACT_CELL', 'STAMINA_RECOVERY_PER_RESERVE_RANK', 'STAMINA_POOL_THRESHOLDS', 'STAMINA_EXHAUSTED_POOL_PENALTY', 'ROUT_FLOOR_LOSS_PCT', 'ROUT_EXHAUSTION_MORALE_HIT', 'MORALE_PHASE_CAP', 'DISCIPLINE_LOSS_THRESHOLD', 'VOLLEY_ENABLED', 'VOLLEY_TN', 'RANGED_DR_DEFAULT', 'VOLLEY_MIN_RANGE', 'VOLLEY_MAX_RANGE', 'PC_VOLLEY_DENSITY_ENABLED', 'PC_VOLLEY_DENSITY_REF', 'PC_VOLLEY_DENSITY_FLOOR', 'PC_VOLLEY_DENSITY_CAP', 'MIN_DISCIPLINE', 'ANGLE_DEF_MOD', 'STANCE_SPEED_MOD', 'DAMAGE_BY_DEGREE', 'SIGMA_HEAD_ENABLED', 'SIGMA_PER_D', 'RANGED_MELEE_SIGMA', 'MORALE_FIX', 'MORALE_EROSION_DAMP', 'MORALE_SIGMA_SCALE', 'PER_CELL', 'PC_STAMINA_DRAIN', 'PC_STAMINA_REST', 'PC_ROTATE_FLOOR', 'PC_STAM_SIGMA', 'PC_DEPTH_ROTATE', 'PC_FRONTAGE_BLEND', 'PC_FRONTAGE_REF', 'PC_FLANK_CAP', 'PC_REFILL_FLOOR', 'PC_FLANK_DEPTH_RESIST', 'PC_FRONT_RANKS', 'PC_ENVELOP_SIGMA', 'PC_CHARGE_SIGMA', 'PC_SHOCK_FRONT', 'PC_SHOCK_REAR', 'PC_SHOCK_BRACE_FLOOR', 'PC_SHOCK_HOLD_BRACE', 'PC_SHOCK_DISC_FULL', 'PC_SHOCK_DEPTH_FULL', 'PC_SHOCK_DEPTH_REF', 'PC_SHOCK_SHAKEN_GAIN', 'PC_CAVALRY_SPEED_MULT', 'PC_BRACE_ENABLED', 'PC_RECOIL_FRONTAL', 'PC_CHARGE_RECOIL', 'PC_BRACE_SETUP_DELAY', 'PC_RECOIL_CHARGER_GATE', 'PC_WHEEL', 'REAR_BLIND_DEG', 'FOV_HALF_DEG', 'PC_PIN_REACH', 'PC_REFUSE', 'PC_ENVELOP_MOD', 'PC_ENVELOP_DEPTH_RESIST', 'PC_POCKET_MOD', 'PC_POCKET_REACH', 'LANCHESTER_ENABLED', 'K_LINEAR', 'K_SQUARE', 'LANCHESTER_STRENGTH_REF', 'LANCHESTER_DENSITY_REF', 'COMMAND_SIGMA_ENABLED', 'COMMAND_POOL_MULT', 'CMD_CHA_WEIGHT', 'CMD_COG_WEIGHT', 'TROOP_TYPE_ROLES', 'ROLE_SPEC', 'PC_KITE_ENABLED', 'PC_KITE_STANDOFF', 'PC_NODE_COHESION']

BATTLEFIELD_SIZE = 50  # [canonical: designs/provincial/mass_battle_v30.md §A.3b — "engine rescaled; config.py is leading canon" for battlefield geometry]
UNIT_GRID_SIZE = 30  # [canonical: designs/provincial/mass_battle_v30.md §A.3b — "engine rescaled; config.py is leading canon" for battlefield geometry]
BUFFER_CELLS = 10
SIDE_A_START_ROW = 34  # step-2 rescale to fit 10k (50-grid)  # [canonical: designs/provincial/mass_battle_v30.md §A.3b — SIDE_A_START_ROW=34/SIDE_B_START_ROW=15 named explicitly in the rescale note]
SIDE_B_START_ROW = 15  # step-2 rescale to fit 10k (50-grid)  # [canonical: designs/provincial/mass_battle_v30.md §A.3b — SIDE_A_START_ROW=34/SIDE_B_START_ROW=15 named explicitly in the rescale note]
POOL_VARIANT = "C-ii"
TIP_SUPPORT_ENABLED = True
TIP_SUPPORT_GAP = 2
# [canonical: sim_verification_ledger.json — CALIBRATED, engine's own tier-generator doubling progression (100/200/400/800), not independently historically cited]
TROOPS_PER_TIER = {1: 100, 2: 200, 3: 400, 4: 800}
TROOPS_PER_SIZE = 100
# ─── CONTINUOUS-SCALE CELL MODEL (Jordan directive 2026-06-03) ───
# Units carry a continuous troop count (no discrete tiers). A cell holds CELL_FLOOR..CELL_CAP
# fighting troops; user-set concentration trades cells for density (denser = fewer cells). A
# subunit routs below SUBUNIT_ROUT_FLOOR total. All-fight: every troop in a contacting cell
# contributes to the exchange (bounded-square, capped at CELL_CAP).
CELL_FLOOR = 40             # min troops/cell; below this a cell merges into a neighbour (lifecycle)  # [canonical: tests/coverage_matrix_archive.md §"2026-06-03 continuous-scale rework - step 1a" — footprint generator constants CELL_FLOOR=40/CELL_CAP=200/SUBUNIT_ROUT_FLOOR=80/MAX_TROOPS_PER_UNIT=10000]
CELL_CAP = 200              # max troops/cell that fight; beyond this, troops overflow to new cells  # [canonical: tests/coverage_matrix_archive.md §"2026-06-03 continuous-scale rework - step 1a" — footprint generator constants CELL_FLOOR=40/CELL_CAP=200/SUBUNIT_ROUT_FLOOR=80/MAX_TROOPS_PER_UNIT=10000]
SUBUNIT_ROUT_FLOOR = 80     # a subunit routs when its aggregate total falls below this  # [canonical: tests/coverage_matrix_archive.md §"2026-06-03 continuous-scale rework - step 1a" — footprint generator constants CELL_FLOOR=40/CELL_CAP=200/SUBUNIT_ROUT_FLOOR=80/MAX_TROOPS_PER_UNIT=10000]
MAX_TROOPS_PER_UNIT = 10000 # design ceiling on a single unit's troop count  # [canonical: tests/coverage_matrix_archive.md §"2026-06-03 continuous-scale rework - step 1a" — footprint generator constants CELL_FLOOR=40/CELL_CAP=200/SUBUNIT_ROUT_FLOOR=80/MAX_TROOPS_PER_UNIT=10000]
LINE_ASPECT = 1.4           # generator: Line width:depth ratio (from the per-tier tables' progression)  # [canonical: sim_verification_ledger.json — CALIBRATED, engine generator ratio (coverage_matrix_archive.md "Line=1.4xdepth"), not independently historically cited]
ENCIRCLEMENT_PENALTY = 1
SUPPORT_STACK_ENABLED = True
# [canonical: sim_verification_ledger.json — CALIBRATED, cell-support-stacking taper (F-i), not independently historically cited]
SUPPORT_WEIGHTS = {1: 1.0, 2: 0.7, 3: 0.5}
SUPPORT_WEIGHT_FLOOR = 0.3  # [canonical: sim_verification_ledger.json — CALIBRATED, cell-support-stacking floor (F-i), not independently historically cited]
PUNCTURE_ENABLED = True
PUNCTURE_CAP = 3
CASCADING_ENABLED = True
MAX_SUB_PHASES = 5  # [canonical: sim_verification_ledger.json — CALIBRATED, cascading sub-phase resolution bound (F-iii), not independently historically cited]
TICKS_PER_PHASE = 6  # [canonical: sim_verification_ledger.json — CALIBRATED, engine tick-resolution granularity, not independently historically cited]
BLOCK_SIZE = 100  # [canonical: designs/provincial/mass_battle_v30.md §A.3 — Company scale]
CASUALTY_SCALE = float(_os.environ.get('CASUALTY_SCALE','4'))  # D-B: per-tick lethality. Default 4 = even units take ~3 turns to resolve (playable). TUNING.
STAMINA_MAX = 100
STAMINA_DRAIN_PER_CONTACT_CELL = 1   # drain per cell in contact per tick
STAMINA_RECOVERY_PER_RESERVE_RANK = 8  # [canonical: sim_verification_ledger.json — CALIBRATED, per-subunit fatigue-chain recovery rate (ED-1017), not independently historically cited]
STAMINA_POOL_THRESHOLDS = [(1, 0)]  # no penalty while stamina > 0
STAMINA_EXHAUSTED_POOL_PENALTY = -1  # stamina == 0: -1 die
ROUT_FLOOR_LOSS_PCT = 0.20          # casualty% at which exhausted unit loses morale floor  # [canonical: sim_verification_ledger.json — CALIBRATED, exhaustion/rout-floor threshold, not independently historically cited]
ROUT_EXHAUSTION_MORALE_HIT = 1      # morale loss per phase boundary when exhausted
MORALE_PHASE_CAP = 3  # [canonical: sim_verification_ledger.json — CALIBRATED, per-phase morale-loss bound, not independently historically cited]
DISCIPLINE_LOSS_THRESHOLD = 1.0  # [canonical: params/mass_combat.md §Discipline Degradation]
VOLLEY_ENABLED = True
VOLLEY_TN = 6  # [canonical: params/mass_combat.md §Volley TN (ED-037 resolved — provisional) — "Volley phase uses TN 6 (not TN 7)"]
RANGED_DR_DEFAULT = 2
VOLLEY_MIN_RANGE = 2
VOLLEY_MAX_RANGE = 8  # [canonical: sim_verification_ledger.json — CALIBRATED, engine volley-band ceiling paired with VOLLEY_MIN_RANGE, not independently historically cited]
PC_VOLLEY_DENSITY_ENABLED = _sigma_os.environ.get('PC_VOLLEY_DENSITY_ENABLED', '1') == '1'  # [class-B] volley casualties scale with TARGET formation density (packed/deep -> more hits); ranged-only path so the melee gauge stays byte-exact
PC_VOLLEY_DENSITY_REF = float(_sigma_os.environ.get('PC_VOLLEY_DENSITY_REF', '80'))  # [class-B sim-tunable] reference column density (a standard line) at which the multiplier is 1.0
PC_VOLLEY_DENSITY_FLOOR = float(_sigma_os.environ.get('PC_VOLLEY_DENSITY_FLOOR', '0.5'))  # [class-B sim-tunable] a dispersed/skirmish-order target bleeds at least this fraction
PC_VOLLEY_DENSITY_CAP = float(_sigma_os.environ.get('PC_VOLLEY_DENSITY_CAP', '2.0'))  # [class-B sim-tunable] a packed deep column bleeds at most this multiple (Carrhae/Agincourt/Crécy)
# SHAPE_OFF_MOD / SHAPE_DEF_MOD RETIRED 2026-06-02 (Jordan design principle): formations grant
# NO flat per-shape bonuses. All formation effects emerge from geometry — frontage (Lanchester),
# depth-damping, support vectors, facing/angle. A formation template is a SHAPE, not a bonus carrier.
MIN_DISCIPLINE = {
    # [canonical: mass_battle_v30.md §ED-815 shape discipline — min disc required by shape]
    # [LC-8, ED-909, Jordan-approved 2026-07-02] Horseshoe/RefusedFlank entries retired along with
    # the shapes themselves (geometry.CELL_PATTERN_FN's note) -- they are now Unit-level, multi-body
    # emergent compositions, not a single Subunit.shape this per-shape table can key on.
    "Line": 1, "Arrowhead": 4, "GappedLine": 5, "Column": 3
}
ANGLE_DEF_MOD = {
    # v11: per-cell octagon. GREEN < 45° = 0D; YELLOW 45-90° = -1D; RED ≥ 90° = -2D.
    # [canonical: Jordan design]
    "GREEN": 0, "YELLOW": -1, "RED": -2,
    "FRONT": 0, "FLANK": -1, "REAR": -2,  # legacy aliases
}
# [canonical: sim_verification_ledger.json — CALIBRATED, -99 is a structural sentinel (effectively-zero speed for 'hold'), not a magnitude independently historically cited]
STANCE_SPEED_MOD = {"aggressive": 1, "balanced": 0, "hold": -99, "retreat": 0}
DAMAGE_BY_DEGREE = {"Overwhelming": lambda p: 1+p, "Success": lambda p: p,
                     "Partial": lambda p: 1,        "Failure": lambda p: 0}
SIGMA_HEAD_ENABLED = _sigma_os.environ.get('SIGMA_HEAD', '1') == '1'   # toggle via SIGMA_HEAD env; default ON
SIGMA_PER_D = 0.2            # [class-B sim-tunable] sigma-units per die-equivalent of a legacy pool modifier  # [canonical: sim_verification_ledger.json — CALIBRATED, sigma-head/pool-modifier conversion rate, not independently historically cited]
RANGED_MELEE_SIGMA = -1.0    # [class-B sim-tunable] ranged-in-melee disadvantage as delta-sigma (replaces pool//3)
MORALE_FIX = _sigma_os.environ.get('MORALE_FIX', '1') == '1'   # toggle; OFF reproduces the pre-fix sigma prototype exactly
MORALE_EROSION_DAMP = 0.7    # [class-B] <1 slows morale erosion -> longer, more attritional battles  # [canonical: sim_verification_ledger.json — CALIBRATED, morale-erosion damping factor, not independently historically cited]
MORALE_SIGMA_SCALE  = 0.8    # [class-B] morale->effectiveness: falling morale lowers a unit's sigma-leverage  # [canonical: sim_verification_ledger.json — CALIBRATED, morale-to-sigma-leverage scaling, not independently historically cited]
PER_CELL = _sigma_os.environ.get('PER_CELL', '1') == '1'   # per-column density/depth/fatigue/charge layer. [movement/pathing audit gate 4, ED-MB-0001, Jordan-ratified 2026-07-02: "yes, all options/modules must be turned on."] DEFAULT FLIPPED 0 -> 1, same ED-1089 precedent as FIELD_MOVEMENT/PC_NODE_COHESION: unlocks charge shock, brace recoil, cavalry speed, fatigue, and the ED-1091/ED-1095 gates in the default/visualized configuration; grid oracle = explicit '0' pin (bat.py/test_mass_battle_byte_exact.py already pin both PER_CELL=0 and PER_CELL=1 explicitly per mode, not via ambient default, so no CI-pin gap here)
PC_NODE_COHESION = _sigma_os.environ.get('PC_NODE_COHESION', '1') == '1'   # step 2: node-relational cohesion (cells=nodes at live positions, held by relational offsets). [ED-1089, Jordan-ratified 2026-07-02] DEFAULT FLIPPED 0 -> 1 together with FIELD_MOVEMENT (units.py) — the field toggle requires the node float path (run_battle asserts FIELD_MOVEMENT => PC_NODE_COHESION); grid oracle = both pinned '0'
PC_STAMINA_DRAIN   = 12     # front-column stamina lost per clash it fights  # [canonical: sim_verification_ledger.json — CALIBRATED, per-column fatigue chain (ED-1017), not independently historically cited]
PC_STAMINA_REST    = 5      # a non-engaged (reserve-fed) column recovers this per tick  # [canonical: sim_verification_ledger.json — CALIBRATED, per-column fatigue chain (ED-1017), not independently historically cited]
PC_ROTATE_FLOOR    = 50     # below this a fatigued front rotates if a fresher reserve rank exists  # [canonical: sim_verification_ledger.json — CALIBRATED, per-column fatigue chain (ED-1017), not independently historically cited]
PC_STAM_SIGMA      = 1.5    # fatigue -> delta-sigma (a winded front fights worse; thin lines can't rotate)  # [canonical: sim_verification_ledger.json — CALIBRATED, per-column fatigue chain (ED-1017), not independently historically cited]
PC_DEPTH_ROTATE    = 1.0    # depth fatigue-damping: effective drain = PC_STAMINA_DRAIN/(1+PC_DEPTH_ROTATE*(depth-1))
PC_FRONTAGE_BLEND  = 0.0    # Incr4 contact-fraction: 0=pure width (more cols=more men), 1=pure frontage (depth-neutral)
PC_FRONTAGE_REF    = 7.0    # reference frontage (columns) for the width term normalization  # [canonical: tests/coverage_matrix_archive.md §"PER_CELL Increment 4" — depth-aware contact-fraction width-term normalization; CALIBRATED, not independently historically cited]
PC_FLANK_CAP       = 3      # max overhang columns that count toward envelopment  # [canonical: sim_verification_ledger.json — CALIBRATED, M3 envelopment overhang bound, not independently historically cited]
PC_REFILL_FLOOR    = 0.60   # column pulls a rear rank forward below this fraction of its start density  # [canonical: sim_verification_ledger.json — CALIBRATED, rear-rank refill trigger, not independently historically cited]
PC_FLANK_DEPTH_RESIST = 0.6 # depth blunts flank/overhang delta-sigma  # [canonical: sim_verification_ledger.json — CALIBRATED, M3 envelopment depth-resistance, not independently historically cited]
PC_FRONT_RANKS     = 2      # ranks a column must hold on its front; deeper ranks are free to reform to a flank
PC_ENVELOP_SIGMA   = 0.0    # DISABLED: depth-aware contact fraction (Incr4) already captures the width/envelopment
PC_CHARGE_SIGMA    = 0.55   # MAX defender moral-shock delta-sigma on a charge impact (du Picq: cavalry's  # [canonical: designs/audit/2026-06-01-massbattle-stub-wiring/cavalry_shock_design.md §5 (PART 5 — CONSTANTS)]
                            # weapon is the MORAL impulse, not physical collision). This is a CAP reached only
PC_SHOCK_FRONT       = 0.15  # GREEN (faced) charge: mostly absorbed by the formation (square holds frontally)  # [canonical: designs/audit/2026-06-01-massbattle-stub-wiring/cavalry_shock_design.md §5]
PC_SHOCK_REAR        = 1.6   # RED (rear) charge: bracing bypassed (Cannae/Adrianople — cannot face the rear)  # [canonical: designs/audit/2026-06-01-massbattle-stub-wiring/cavalry_shock_design.md §5]
PC_SHOCK_BRACE_FLOOR = 0.05  # [canonical: Stage-4 calibration vs Waterloo-square bands] braced+disciplined+deep -> shock ~0 (the square Ney could not break)
PC_SHOCK_HOLD_BRACE  = 0.35  # 'hold' stance (Shield Wall, cannot advance) alone cuts shock to ~1/3
PC_SHOCK_DISC_FULL   = 0.35  # discipline>=5 (steady troops hold formation) cuts shock to ~1/3  # [canonical: designs/audit/2026-06-01-massbattle-stub-wiring/cavalry_shock_design.md §5]
PC_SHOCK_DEPTH_FULL  = 0.5   # deep (>=PC_SHOCK_DEPTH_REF ranks) halves shock (mass absorbs)
PC_SHOCK_DEPTH_REF   = 4.0   # rank depth treated as fully "deep"  # [canonical: designs/audit/2026-06-01-massbattle-stub-wiring/cavalry_shock_design.md §5]
PC_SHOCK_SHAKEN_GAIN = 1.0   # already-shaken defender (morale<<start) takes up to 2x shock (Hastings-post-feint)
PC_CAVALRY_SPEED_MULT = 2.0  # cavalry velocity primitive: cavalry closes this much faster (PER_CELL), triggering the charge
PC_KITE_ENABLED = True  # §13 kiting primitive: ranged units with the 'kite' instruction maintain the volley band instead of closing. INERT without the instruction -> byte-exact.
PC_KITE_STANDOFF = 5  # [class-B] kiter retreat-trigger (Chebyshev distance): open the gap when nearest enemy is nearer than this; hold+volley in [this, VOLLEY_MAX_RANGE]; close when beyond. Calibrate by measurement. §13.  # [canonical: sim_verification_ledger.json — CALIBRATED, §13 kiting primitive retreat-trigger, not independently historically cited]
PC_BRACE_ENABLED = _sigma_os.environ.get('PC_BRACE_ENABLED', '1') == '1'  # [class-B] brace-instruction effects (charge-resistance + reciprocal recoil); gated on the 'brace' instruction so instruction-less scenarios stay byte-exact
PC_RECOIL_FRONTAL = _sigma_os.environ.get('PC_RECOIL_FRONTAL', '1') == '1'  # [ED-1091, Jordan-approved 2026-07-02 "c7 if it is historically valid"] the reciprocal charge-recoil fires ONLY when the braced wall FACES the charge (GREEN octagon zone) — a brace cannot repel what it cannot face; OFF reproduces the prior any-direction recoil  # [canonical: mass_battle_gauge_grounding.md §4.3 — Burkholder 2007; the flagged fix candidate "gate the recoil on the frontal (GREEN) octagon zone"]
PC_CHARGE_RECOIL = float(_sigma_os.environ.get('PC_CHARGE_RECOIL', '6'))  # [class-B sim-tunable; CALIBRATED vs Courtrai/Swiss/Waterloo pike-vs-cavalry: braced+deep+disciplined wall beats a frontal charge ~75%, cavalry takes the heavier losses; shallow/green is ridden down] net-success cost a charger suffers hitting a fully-prepared braced wall (x prep x SIGMA_PER_D)
PC_BRACE_SETUP_DELAY = _sigma_os.environ.get('PC_BRACE_SETUP_DELAY', '1') == '1'  # [ED-1095, Jordan-ruled 2026-07-02 "Bracing is not something that can be done instantaneously, but must be prepared ahead of time and intentionally set"] brace (both the charge-shock defensive benefit and the reciprocal recoil) only counts once >=1 full tick has elapsed since the 'brace' instruction was set via an Order; a subunit DEPLOYED already braced (construction-time instructions) is exempt (it had time to set up before the battle began). OFF reproduces the prior instantaneous-brace behaviour exactly, even when a tick is passed in.
PC_RECOIL_CHARGER_GATE = _sigma_os.environ.get('PC_RECOIL_CHARGER_GATE', '1') == '1'  # [ED-1095, Jordan-ruled 2026-07-02] the reciprocal charge-recoil additionally requires (a) the CHARGING atom's troop_type=='cavalry' literally (mounted_archers explicitly excluded -- they should never be closing/charging at all, see T4) and (b) the DEFENDER's reach >= the CHARGER's reach (troop_types.registry.reach_for) -- a charger with genuinely longer reach (e.g. a lance) can strike a braced wall whose weapons can't reach back, so the wall can't retaliate. Structural only: TROOP_TYPE_REACH stays empty (everyone defaults to REACH_SHORT), so (b) is a deliberate no-op today until reach assignments are separately ratified. OFF reproduces the exact pre-this-ruling recoil condition (momentum + braced + PC_RECOIL_FRONTAL only).
PC_WHEEL = _sigma_os.environ.get('PC_WHEEL', '1') == '1'   # envelopment wheel: overhang cells wheel toward the enemy flank (PER_CELL); A/B via env
REAR_BLIND_DEG = 150.0                                     # [grounded; Class-B tunable] rear arc a cell cannot perceive  # [canonical: designs/audit/2026-05-31-percell-combat/movement_model_design.md §"FOV — RESOLVED" — anatomical rear blind arc ~150deg, visible +/-105deg (human visual field ~190-210deg horizontal)]
FOV_HALF_DEG = 180.0 - REAR_BLIND_DEG / 2.0                # visible if angle-from-facing <= this (105deg)  # [canonical: designs/audit/2026-05-31-percell-combat/movement_model_design.md §"FOV — RESOLVED"]
PC_PIN_REACH = 1.5                                         # an attacker within this distance in the front arc PINS the cell  # [canonical: designs/audit/2026-05-31-percell-combat/movement_model_design.md §"FOV — RESOLVED" — is_pinned(): enemy adjacent (<=~1.5) within the front arc]
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
K_LINEAR  = float(_sigma_os.environ.get('K_LINEAR', '12'))   # [canonical: mb_lanchester_design.md §3a/§5 — melee linear coeff, rescopes CASUALTY_SCALE; class-B]
K_SQUARE  = float(_sigma_os.environ.get('K_SQUARE', '0.25')) # [canonical: mb_lanchester_design.md §3b/§5 — volley square-law coeff; class-B]
LANCHESTER_STRENGTH_REF = float(_sigma_os.environ.get('LANCHESTER_STRENGTH_REF', '4'))  # [canonical: mb_lanchester_design.md §3a — reference engaged frontage (cols) normalizing the linear factor to ~1 at the mirror; class-B]
LANCHESTER_DENSITY_REF = float(_sigma_os.environ.get('LANCHESTER_DENSITY_REF', '100'))  # [Jordan directive 2026-06-03] all-fight reference troops/cell; density factor = min(tpc,CELL_CAP)/this

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
