## key_type_registry.gd — the valid Key types + per-type payload schema (AUTOLOAD).
##
## Loaded from data/key_types/*.tres at boot (one Resource per type). Adding a new
## Key type is a new .tres + a registry entry — ZERO core edits. Mirrors
## designs/architecture/key_type_registry_v30.md (44 types, 7 families).
extends Node

## type_id -> { family, required_payload_fields:Array, optional_payload_fields:Array,
##              default_scale_signature:Array, default_permanence, default_time_horizon,
##              emitting_systems:Array, consuming_systems:Array, cls }
var types: Dictionary = {}


func register_type(type_id: String, spec: Dictionary) -> void:
	types[type_id] = spec


func is_registered(type_id: String) -> bool:
	return types.has(type_id)


## Per-type payload validation (universal invariants live on the Key itself).
func validate(key: Key) -> bool:
	if not types.has(key.type):
		push_error("KeyTypeRegistry: unregistered type '%s'" % key.type)
		return false
	var spec: Dictionary = types[key.type]
	for field in spec.get("required_payload_fields", []):
		if not key.payload.has(field):
			push_error("KeyTypeRegistry: %s missing required payload field '%s'" % [key.type, field])
			return false
	return true


## Load all type Resources from a directory at boot.
func load_from_dir(dir_path: String) -> void:
	var dir := DirAccess.open(dir_path)
	if dir == null:
		return
	for file in dir.get_files():
		if file.ends_with(".tres"):
			var res := load(dir_path.path_join(file))
			if res and res.has_method("to_spec"):
				register_type(res.type_id, res.to_spec())
