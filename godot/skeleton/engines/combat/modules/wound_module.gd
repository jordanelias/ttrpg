## wound_module.gd — the canonical wound model (an EngineModule).
##
## CANON: combat_engine_v1 wound tracker (r2_consequence_wounds) + ED-1041 bilateral-Ob wiring.
## Consumes scene.combat_hit (the health delta a StrikeModule routed onto the substrate) and converts
## cumulative damage into the wound state:
##   WI       = round(Endurance + 4 + 0.4·Spirit)                          [r2.wound_interval]
##   MaxWounds= min(⌊End/2⌋ + 1, 3)                                        [r2.max_wounds, PP-717 cap]
##   Health   = round(WI·(MaxWounds+1) + 0.25·Strength·Endurance)          [r2.health_full]
##   Wounds   = min(⌊cumulative_damage / WI⌋, MaxWounds+1)   (a hit > WI crosses gates at once)
##   felled   ⇔ cumulative_damage ≥ Health                                 [r2.felled — Health depletion]
##
## F1 GUARD: `health` is a DERIVED_VALUE (read-only) = Health − cumulative_damage; this module writes
## the SUBSTRATE track (cumulative_damage) and the Wounds track, never the derived Health directly.
## The Wounds track it maintains is exactly what StrikeModule reads for the bilateral-Ob term — so the
## wound impairs BOTH fighters' future exchanges (offence via wound_atk_ob, defence via wound_def_ob).
##
## SUPERSEDES the −1D aggressor-only pool penalty (the model the stale docs still describe): there is
## no pool dock here at all — impairment is the Obstacle channel StrikeModule applies.
class_name WoundModule
extends EngineModule


func _init() -> void:
	module_id = "combat.wound"
	resolver = Resolver.STATE_READER
	consumes = ["scene.combat_hit"]
	emits = ["scene.combat_felled"]
	owned_scalars = [
		{"name": "cumulative_damage", "bucket": "track", "writable": true},
		{"name": "wounds", "bucket": "track", "writable": true},
		{"name": "health", "bucket": "derived_value", "writable": false},   # F1 — derived from the track
	]


func resolve(key: Key) -> void:
	for t in key.targets:
		var dmg: float = -float(t.get("stat_deltas", {}).get("health", 0.0))
		if dmg <= 0.0:
			continue
		var actor = GameState.get_actor(t.get("actor_id", ""))
		if actor == null:
			continue
		var end_v: float = actor.stat("endurance")
		var spi: float = actor.stat("spirit")
		var strn: float = actor.stat("strength")
		var wi: float = roundf(end_v + 4.0 + 0.4 * spi)
		var max_w: int = mini(int(end_v / 2.0) + 1, 3)
		var health_full: float = roundf(wi * (max_w + 1) + 0.25 * strn * end_v)

		# write the SUBSTRATE track (not the derived Health) — F1
		var cum: float = float(actor.get("cumulative_damage")) if actor.get("cumulative_damage") != null else 0.0
		cum += dmg
		actor.set("cumulative_damage", cum)
		actor.set("wounds", mini(int(cum / wi), max_w + 1))          # the Wounds track → bilateral-Ob source
		actor.set("health", maxf(0.0, health_full - cum))            # derived display value (read-only)

		if cum >= health_full:
			_emit_felled(t.get("actor_id", ""), key.id)


func _emit_felled(actor_id: String, cause_id: String) -> void:
	var k := Key.new()
	k.id = GameState.new_key_id()
	k.type = "scene.combat_felled"
	k.scale_signature = ["personal"]
	k.season_index = GameState.season_index
	k.causes = [cause_id]
	k.targets = [{"actor_id": actor_id, "role": "subject", "impact_vector": {}, "stat_deltas": {}}]
	k.public = true                                                 # a felling is witnessable (ripples up/sideways)
	k.payload = {"actor_id": actor_id}
	produce(k)
