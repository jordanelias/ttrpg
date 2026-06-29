## strike_module.gd — the canonical combat exchange (an EngineModule).
##
## CANON: combat_engine_v1 (ED-900/904; docket ED-1029). This REPLACES the earlier placeholder that
## used the DEPRECATED v30 model (pool=Agi×2, TN-7, damage=net_hits+STR) — the same superseded model
## the audit flagged in sim/personal/combat.py and mechanics_index.yaml. The canonical model is:
##   • resolver D_SIGMA (sigma-leverage): pool = max(5, History+6); base Ob FIXED at 3; advantage
##     boosts the ROLL (mu-shift), never the Ob.   [r1_sigma_resolution / m1_dice_sigma_core]
##   • damage LINEAR: (Strength + heft) · coupling(head,armour) · quality · 1.55 — no tanh cap.  [core.py]
##   • wounds BILATERAL Obstacle (ED-1041): defender wounds raise the attacker's net, aggressor wounds
##     lower it — wounds impair offence AND defence; the pool is never docked.
##   • the wound rides the substrate as a write-protected `health` stat_delta (F1), never a direct write.
##
## SCOPE (slice): the core exchange net_sigma + resolution + damage. The defensive-mode selection
## (parry/dodge/wind), feint, bind/winding, initiative-state (Vor/Nach), and poise/kuzushi are their
## own modules in the contract (references/module_contracts.yaml personal_combat) — a later port pass.
##
## Expected Actor API (duck-typed, mirrors the skeleton's GameState actor):
##   actor.stat(name:String)->float   for history/agility/cognition/attunement/strength
##   actor.get("weapon")->WeaponResource, actor.get("armor")->String, actor.get("wounds")->int
class_name StrikeModule
extends EngineModule

@export var config: CombatConfig          # set by the module .tres (ExtResource); fallback below


func _init() -> void:
	module_id = "combat.strike"
	resolver = Resolver.D_SIGMA
	consumes = ["scene.combat_strike"]
	emits = ["scene.combat_hit"]
	# Health is the CombatEngine's derived_value (F1) — this module never owns/writes it; it routes
	# the wound as a stat_delta on the emitted Key. It owns no scalar of its own.
	owned_scalars = []


func resolve(key: Key) -> void:
	var cfg: CombatConfig = config if config != null else CombatConfig.new()
	var atk = GameState.get_actor(key.payload.get("attacker", ""))
	var dfn = GameState.get_actor(key.payload.get("defender", ""))
	if atk == null or dfn == null:
		return
	var aw: WeaponResource = atk.get("weapon")
	var dw: WeaponResource = dfn.get("weapon")
	if aw == null or dw == null:
		return
	var d_armor: String = String(dfn.get("armor")) if dfn.get("armor") != null else "none"
	var a_wounds: int = int(atk.get("wounds")) if atk.get("wounds") != null else 0
	var d_wounds: int = int(dfn.get("wounds")) if dfn.get("wounds") != null else 0
	var commit: int = int(key.payload.get("commit", 3))   # 2–5 (disposition-skewed in the full engine)

	# ── net_sigma (aggressor-favouring positive). wrapper.py net_sigma assembly, core terms. ──
	var init_sig: float = (
		cfg.init_k * (atk.stat("agility") - dfn.stat("agility"))
		+ cfg.init_reading_k * (_reading(atk, cfg) - _reading(dfn, cfg))
		+ cfg.init_history_k * (atk.stat("history") - dfn.stat("history")))
	var atk_sig: float = cfg.commit_sigma * (commit - 3) + init_sig
	var reach_pen: float = _reach_sigma(aw, dw, d_armor, cfg)              # defender reach lowers attacker net
	var adef: float = _armor_defeat_sigma(aw, d_armor, cfg)               # armour-defeat capability
	var wound_ob: float = cfg.wound_def_ob * d_wounds - cfg.wound_atk_ob * a_wounds   # ED-1041 bilateral
	var net_sigma: float = atk_sig - reach_pen + adef + wound_ob + cfg.attacker_bias

	# ── resolution: pool = max(5, History+6); net = roll + mu-shift boost; canonical degree band. ──
	var pool: int = maxi(cfg.pool_floor, int(round(atk.stat("history"))) + cfg.pool_base)
	GameState.rng.seed = key.rng_seed                                     # per-Key seed → replay-deterministic
	var net: float = _roll_net_continuous(pool, cfg) + cfg.soft_cap(net_sigma) * cfg.sigma_n(pool)
	var deg: String = _degree(net, cfg.decisive_ob)
	if deg == "failure":
		return                                                            # miss (riposte/counter = later module)

	# ── damage: LINEAR (Str + heft) · coupling · quality · scale. ──
	var quality: String = "graze" if deg == "partial" else deg
	var qf: float = float(cfg.qual[quality])
	if deg == "overwhelming":                                             # sigma-leverage tail (M-QUAL)
		var z: float = maxf(0.0, (net - 2.0 * cfg.decisive_ob) / cfg.sigma_n(pool))
		qf = 1.5 + (2.5 - 1.5) * tanh(z / 1.5)
	var impact: float = atk.stat("strength") + cfg.heft_for(aw)
	var damage: int = maxi(0, int(round(impact * aw.coupling(d_armor, cfg) * qf * cfg.damage_scale)))
	if damage <= 0:
		return

	# ── emit: the wound rides the substrate as a write-protected health stat_delta (F1). ──
	var hit := Key.new()
	hit.id = GameState.new_key_id()
	hit.type = "scene.combat_hit"
	hit.source_actor = String(key.payload.get("attacker", ""))
	hit.scale_signature = ["personal"]
	hit.season_index = GameState.season_index
	hit.causes = [key.id]
	hit.targets = [{
		"actor_id": String(key.payload.get("defender", "")), "role": "subject",
		"impact_vector": {}, "stat_deltas": {"health": -damage},
	}]
	hit.private_observers = [String(key.payload.get("attacker", "")), String(key.payload.get("defender", ""))]
	hit.payload = {"degree": deg, "net": net, "damage": damage}
	hit.rng_seed = key.rng_seed
	produce(hit)


# ── helpers (ported from core.py / systems.py) ──

func _reading(c, cfg: CombatConfig) -> float:
	return (2.0 * c.stat("cognition") + c.stat("attunement")) / 3.0 + cfg.read_history_k * (c.stat("history") - 3.0)


func _reach_base(w: WeaponResource) -> float:
	var head_reach := {"point": 1.0, "straight_cut": 0.5, "curved_cut": 0.5, "cut_thrust": 0.5, "blunt": 0.0}
	return 4.0 + 2.0 * float(w.reach == "long") + 0.8 * float(w.hands == 2) + float(head_reach.get(w.head, 0.0)) + w.reach_adj


func _reach_sigma(aw: WeaponResource, dw: WeaponResource, d_armor: String, cfg: CombatConfig) -> float:
	var gap: float = _reach_base(dw) - _reach_base(aw)
	return float(cfg.reach_w[d_armor]) * gap * cfg.reach_frac


## armour-defeat: the weapon that CAN defeat the armour controls the armoured exchange. core/systems.
func _armor_defeat_sigma(aw: WeaponResource, d_armor: String, cfg: CombatConfig) -> float:
	var a: float = float(cfg.adef_w[d_armor])
	if a == 0.0:
		return 0.0
	var cap: float
	match aw.head:
		"blunt":
			cap = cfg.adef_blunt * (aw.percussion_authority() / 8.0)
		"point":
			cap = cfg.adef_point * aw.gap
		"cut_thrust":
			cap = maxf(cfg.adef_cut, cfg.adef_point * aw.gap)   # cut OR half-sword gap-thrust
		_:
			cap = cfg.adef_cut
	return a * (cap - float(cfg.adef_threshold[d_armor]))


## net ~ Normal(mu·N, sigma·√N) at TN7: PER_DIE[7] = (0.40, 0.800). m1.roll_net_continuous.
func _roll_net_continuous(pool: int, cfg: CombatConfig) -> float:
	return GameState.rng.randfn(0.40 * pool, 0.800 * sqrt(float(maxi(1, pool))))


## degree band WITH the ER-2 continuity correction — band on net-(ob-0.5), matching core.py
## degree() (commit 793f1a62). Without the -0.5 shifts the Godot port ran ~5-9pp low on success
## vs the discrete/Python engine below ~5D (the personal-combat 5-13D band) — verification RU-1.
func _degree(net: float, ob: float) -> String:
	if net < 0.5:
		return "failure"
	if net >= 2.0 * ob - 0.5 and net >= 2.5:
		return "overwhelming"
	if net >= ob - 0.5:
		return "success"
	return "partial"
