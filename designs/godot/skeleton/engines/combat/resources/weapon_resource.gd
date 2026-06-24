## weapon_resource.gd — canonical weapon vector (combat_engine_v1 / combatant.py WEAPONS + GEOMETRY).
##
## SUPERSEDES the v30 `WeaponData` in data_serialization_spec.md (3-axis reach/weight/damage_type,
## TN 5-8, dmg_vs_none/light/medium/heavy) — that is the deprecated model. The canonical weapon is a
## continuous vector: head-shape + lever-arm (grip/head length) + guards + gap-precision + percussion,
## with mass + point-of-balance feeding blunt percussion authority.
class_name WeaponResource
extends Resource

@export var weapon_name: String = ""
@export_enum("short", "long") var reach: String = "long"
@export_enum("light", "heavy") var weight: String = "light"
@export var hands: int = 1
@export_enum("point", "cut_thrust", "straight_cut", "curved_cut", "blunt") var head: String = "cut_thrust"
@export var spd: float = 1.5
@export_enum("Forgiving", "Standard", "Demanding") var handling: String = "Standard"

# lever-arm (leverage / bind / reach)
@export var grip_len: float = 0.8
@export var head_len: float = 2.4
@export var reach_adj: float = 0.0

# guards: hand_guard = passive hand protection (commit/parry safely); blade_guard = active blade-catch/wind
@export_range(0.0, 1.0) var hand_guard: float = 0.40
@export_range(0.0, 1.0) var blade_guard: float = 0.55

# gap-thrust precision vs armour (geometry-baked in Python; carried as data here)
@export_range(0.0, 1.0) var gap: float = 0.65

# blunt/percussion physics inputs (LIVE for blunt heads via percussion_authority — audit: not "dead data")
@export var mass: float = 1.2          # kg
@export_range(0.0, 1.0) var pob_frac: float = 0.12   # point of balance, fraction of length


## HEAD_MODE — the damage mode a head fights in.
const HEAD_MODE := {
	"blunt": "percussion", "point": "puncture", "cut_thrust": "shear",
	"straight_cut": "shear", "curved_cut": "shear", "cut": "shear",
}


## Percussion authority P_auth = min(8, 9.5·(√mass · pob_frac)^0.30) — core.p_auth.
## Replaces the old hand-set `percussion`; mass & pob_frac are its LIVE inputs (for blunt heads).
func percussion_authority() -> float:
	return minf(8.0, 9.5 * pow(sqrt(maxf(0.0, mass)) * pob_frac, 0.30))


## Coupling = DELIVERY[head] · transmit(mode, material, coverage). cut_thrust is VERSATILE —
## takes the better of its edge (shear) or a half-sword thrust (puncture/gaps) at each armour level.
## Ported from core.coupling / core._transmit.
func coupling(armor_tier: String, cfg: CombatConfig, coverage: String = "full") -> float:
	var mat: String = cfg.tier_to_material.get(armor_tier, "none")
	if head == "cut_thrust":
		return maxf(
			cfg.delivery["cut_thrust"] * _transmit("shear", mat, coverage, cfg),
			cfg.delivery["point"] * _transmit("puncture", mat, coverage, cfg))
	var mode: String = HEAD_MODE.get(head, "shear")
	return float(cfg.delivery.get(head, 1.5)) * _transmit(mode, mat, coverage, cfg)


func _transmit(mode: String, mat: String, coverage: String, cfg: CombatConfig) -> float:
	var t: float = 1.0 - float(cfg.resist[mat][mode])
	if mode == "puncture":
		return maxf(t, float(cfg.coverage_gap[coverage]))   # thrust takes through-material OR the gap
	if mat != "none":
		var g: float = float(cfg.coverage_gap[coverage])
		return t * (1.0 - g) + 1.0 * g                      # some blows reach a bare zone
	return t
