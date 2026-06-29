## game_state.gd — the serializable world state (AUTOLOAD).
##
## Holds all mutable runtime state (factions, territories, clocks, actors) and the
## save substrate. `save = initial_state + Key log` (deterministic replay). Data
## templates live in .tres; this is the runtime mutable layer. Mirrors
## sim/autoload/game_state.py (create_world / serialize_world / restore_world).
extends Node

var season_index: int = 0
var rng_seed: int = 0
var rng := RandomNumberGenerator.new()

var factions: Dictionary = {}        # name -> FactionState
var territories: Dictionary = {}     # tid  -> TerritoryState
var clocks: Dictionary = {}          # "MS"/"CI"/"IP"/... -> float
var actors: Dictionary = {}          # actor_id -> Actor (NPC/PC; carries armature + memory)

var initial_snapshot: Dictionary = {}
var _key_counter: int = 0


func seed_rng(s: int) -> void:
	rng_seed = s
	rng.seed = s


## A deterministic, monotonic Key id (no Date/UUID randomness in the hot path).
func new_key_id() -> String:
	_key_counter += 1
	return "k%08d" % _key_counter


func get_actor(actor_id: String):
	return actors.get(actor_id)


## All actors whose state intersects any of the named scales (substrate §4.2).
func actors_in_scale(scales: Array) -> Array:
	var out: Array = []
	for id in actors.keys():
		var a = actors[id]
		for s in scales:
			if a.scales.has(s):
				out.append(id)
				break
	return out


func snapshot() -> Dictionary:
	return {
		"season_index": season_index,
		"factions": _map_to_dict(factions),
		"territories": _map_to_dict(territories),
		"clocks": clocks.duplicate(),
		"actors": _map_to_dict(actors),
	}


func restore(data: Dictionary) -> void:
	season_index = data.get("season_index", 0)
	clocks = data.get("clocks", {}).duplicate()
	# factions/territories/actors rebuilt by their owning engines' restore() — see Kernel.


func serialize_keys(log: Array) -> Array:
	var out: Array = []
	for k in log:
		out.append({"id": k.id, "type": k.type, "payload": k.payload,
			"season_index": k.season_index, "rng_seed": k.rng_seed})
	return out


func _map_to_dict(m: Dictionary) -> Dictionary:
	var out := {}
	for k in m.keys():
		out[k] = m[k].serialize() if m[k].has_method("serialize") else m[k]
	return out
