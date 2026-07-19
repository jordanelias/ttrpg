## combat_engine.gd — the BaseEngine for personal-scale fight resolution.
##
## CANON: combat_engine_v1 (ED-900/904; docket ED-1029). Owns the combat scalars; hosts the combat-
## action modules (Strike, Wound, …Feint/Bind/Approach in the full port); emits scene.combat_resolved
## when a fight ends, which the bus delivers up to factions, sideways to witnesses, into NPC memory.
## This is the shape EVERY engine follows. Canon detail: complete_systems_reference Part 2.
##
## OWNED SCALARS (declared in the engine manifest; runtime values live per-actor in GameState):
##   Health  → derived_value (write-protected; route deltas to the wound substrate) — F1
##   Stamina → pool
##   Wounds  → track (the bilateral-Ob source — ED-1041)
class_name CombatEngine
extends BaseEngine

@export var config: CombatConfig          # the Class-C tunables (one source of truth — set by the engine .tres)

var _active_fights: Dictionary = {}       # fight_id -> {participants:Array[String], round:int}


func _on_setup() -> void:
	# Strike/Wound (and later Feint/Bind/…) are loaded from the manifest by BaseEngine.setup().
	# Inject the shared config into any module that takes one (the slice's StrikeModule).
	for m in modules:
		if "config" in m and config != null:
			m.config = config


## Drive a fight round; each action module resolves its own declared Key types via the bus dispatch.
func resolve_round(fight_id: String, declarations: Array) -> void:
	var fight: Dictionary = _active_fights.get(fight_id, {"participants": [], "round": 0})
	fight["round"] = int(fight.get("round", 0)) + 1
	_active_fights[fight_id] = fight
	for decl in declarations:
		consume(decl)                     # dispatches the action Key to the right module (Strike → hit → Wound)
	if _fight_over(fight_id):
		_emit_combat_resolved(fight_id)


## A fight ends when any participant is felled — health depleted (the WoundModule drives health to 0).
func _fight_over(fight_id: String) -> bool:
	var fight: Dictionary = _active_fights.get(fight_id, {})
	for actor_id in fight.get("participants", []):
		var a = GameState.get_actor(actor_id)
		if a != null and a.get("health") != null and float(a.get("health")) <= 0.0:
			return true
	return false


func _emit_combat_resolved(fight_id: String) -> void:
	var fight: Dictionary = _active_fights.get(fight_id, {})
	var k := Key.new()
	k.id = GameState.new_key_id()
	k.type = "scene.combat_resolved"
	k.scale_signature = ["personal"]
	k.season_index = GameState.season_index
	# a fight against an office-holder is an institutional event → the ripple reaches the strategic
	# scale because witnesses/factions observe a public outcome (down/up targeting discipline §12.3).
	k.public = true
	k.payload = {"scene_id": fight_id, "participants": fight.get("participants", [])}
	KeyBus.emit_key(k)
	_active_fights.erase(fight_id)
