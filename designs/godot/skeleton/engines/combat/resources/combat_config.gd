## combat_config.gd — CombatConfig Resource: the personal-combat Class-C tunables, in ONE
## editor-tunable place (data, not code). Ported from designs/scene/combat_engine_v1/config.py.
##
## WHY A RESOURCE: the Python engine had TWO scales — core.py's live DMG_SCALE=1.55 and a DEAD
## config.py DAMAGE_SCALE=4.0 that damage() ignored (audit finding: editing it changed nothing).
## Folding the tunables into one .tres makes the live value the ONLY value — the dead duplicate
## cannot exist. Designers tune `data/combat_config.tres` in the inspector; the modules read it.
##
## Canon model: combat_engine_v1 (ED-900/904; docket ED-1029). D_SIGMA sigma-leverage resolution,
## additive-coupled damage, bilateral-Ob wounds (ED-1041). NOT the v30 (Agi×2 / TN-7 / mult-STR) model.
class_name CombatConfig
extends Resource

# ── resolution (r1_sigma_resolution / m1_dice_sigma_core) ──
@export var decisive_ob: float = 3.0          # base Ob, FIXED; sigma-leverage boosts the ROLL, not the Ob (mu-shift)
@export var tn_standard: int = 7              # PER_DIE[7] = (mu 0.40, sigma 0.800)
@export var pool_base: int = 6                # pool = max(pool_floor, History + pool_base)
@export var pool_floor: int = 5
@export var m_max: float = 1.5               # soft-cap ceiling (sigma units): soft_cap(x)=M·tanh(x/M)
@export var sigma_n_coeff: float = 0.8       # σ_N = 0.8·√pool

# ── damage (core.py — LINEAR: (Str+heft)·coupling·quality·scale, NO tanh cap) ──
@export var damage_scale: float = 1.55       # core.DMG_SCALE — the LIVE value (config.py's 4.0 was DEAD; removed)
@export var heft_light: float = 0.0          # HEFT[wt]; blunt heft is continuous from percussion (below)
@export var heft_heavy: float = 3.0
## QUALITY[degree] — base quality factor (overwhelming gets a sigma-leverage tail in StrikeModule)
@export var qual: Dictionary = {"graze": 0.25, "partial": 0.5, "success": 1.0, "overwhelming": 1.5}
## DELIVERY[head] — head-shape delivery coefficient
@export var delivery: Dictionary = {
	"blunt": 1.6, "point": 1.45, "cut_thrust": 1.35,
	"straight_cut": 1.5, "curved_cut": 1.5, "cut": 1.5,
}
## RESIST[material][mode] — material resistance per damage mode, in [0,1]
@export var resist: Dictionary = {
	"none":  {"percussion": 0.0,  "shear": 0.0,  "puncture": 0.0},
	"cloth": {"percussion": 0.10, "shear": 0.35, "puncture": 0.15},
	"mail":  {"percussion": 0.20, "shear": 0.80, "puncture": 0.45},
	"plate": {"percussion": 0.30, "shear": 0.95, "puncture": 0.70},
}
@export var tier_to_material: Dictionary = {"none": "none", "light": "cloth", "medium": "mail", "heavy": "plate"}
@export var coverage_gap: Dictionary = {"full": 0.15, "partial": 0.5}

# ── bilateral wound Obstacle (ED-1041 — REPLACES the superseded −1D aggressor-only pool penalty) ──
# Wounds impair BOTH offence (+atk Ob) AND defence (+def Ob) as a sigma channel; the pool is never docked.
@export var wound_atk_ob: float = 0.15       # per aggressor wound: raises the aggressor's Obstacle
@export var wound_def_ob: float = 0.25       # per defender wound: the defender's impairment (no pool to dock → Ob channel)

# ── armour-defeat (systems.armor_defeat_sigma) ──
@export var adef_w: Dictionary = {"none": 0.0, "light": 0.4, "medium": 1.0, "heavy": 1.7}
@export var adef_blunt: float = 1.3
@export var adef_point: float = 1.2   # re-exported from config.py (the adef-consistency lever, ED-1080): a gap-thrust's armour-defeat CONTROL matches its damage
@export var adef_cut: float = -0.9
## ADEF_THRESHOLD — per-armour difficulty bar, RE-EXPORTED FROM THE ORACLE config.py (ED-1050 resolved,
## Jordan 2026-06-30): the Python canon was re-swept to a MONOTONE {light:0.30, medium:0.45, heavy:0.72}
## (a gambeson is soft/easily defeated, mail harder, plate hardest). This RETIRES the port's earlier private
## [AUDIT-FIX] in-place correction (CLAUDE.md §6 — the port must never correct its oracle; fix canon, re-export).
## (Fuller re-export of RESIST / GAP_EXPOSURE / the gap-game logic to weapon_resource.gd + strike_module.gd is
## the deferred module port; combat_config.gd remains a non-compilable skeleton, Key-log parity known-red.)
@export var adef_threshold: Dictionary = {"none": 0.0, "light": 0.30, "medium": 0.45, "heavy": 0.72}

# ── standing reach advantage (systems.reach_sigma) ──
@export var reach_frac: float = 0.82
@export var reach_w: Dictionary = {"none": 0.62, "light": 0.50, "medium": 0.34, "heavy": 0.20}

# ── net_sigma assembly (wrapper.py) ──
@export var commit_sigma: float = 0.18        # COMMIT_SIGMA·(commit−3)
@export var init_k: float = 0.045             # initiative tempo per Δagi
@export var init_reading_k: float = 0.03      # initiative per Δreading
@export var init_history_k: float = 0.02      # initiative per ΔHistory
@export var attacker_bias: float = 0.12       # small first-mover/Vor edge (mirror stays 50 — role alternates)
@export var read_history_k: float = 0.2       # reading = (2·Cog+Att)/3 + read_history_k·(History−3)

# ── 95% videogame cap ──
@export var upset_floor: float = 0.05         # no decided matchup reads 100/0


## blunt percussion authority → continuous heft. p_auth derives from weapon mass × point-of-balance
## (core.p_auth): min(8, 9.5·(√mass · pob_frac)^0.30). mass/pob_frac are LIVE inputs for blunt heads
## (audit: not "dead" — consumed here), categorical weight-heft for edged heads.
func heft_for(weapon: WeaponResource) -> float:
	if weapon.head == "blunt":
		return 3.0 * (weapon.percussion_authority() / 8.0)
	return heft_heavy if weapon.weight == "heavy" else heft_light


## soft_cap(net_sigma) = M·tanh(net/M) — smooth saturating, no hard ceiling/dead-zone (m1.soft_cap).
func soft_cap(net_sigma: float) -> float:
	return m_max * tanh(net_sigma / m_max)


## σ_N(pool) = 0.8·√pool — outcome-distribution width (m1.sigma_n).
func sigma_n(pool: int) -> float:
	return sigma_n_coeff * sqrt(float(max(1, pool)))
