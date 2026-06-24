## key_type_resource.gd — one registrable Key type (data). KeyTypeRegistry.load_from_dir reads these
## from data/key_types/*.tres and calls to_spec(); adding a Key type is a new .tres + ZERO core edits.
##
## Resolves audit finding F3 ("no outcome Key type in scene_outcome family for personal combat —
## registry §7 had contest/battle/investigation only"): the combat family (scene.combat_action.strike,
## scene.combat_hit, scene.combat_resolved, scene.combat_felled) registers as data here.
class_name KeyTypeResource
extends Resource

@export var type_id: String = ""                       # registered family.subtype
@export var family: String = ""                        # scene | state | da | env | mechanical | meta
@export var required_payload_fields: Array[String] = []
@export var optional_payload_fields: Array[String] = []
@export var default_scale_signature: Array[String] = ["personal"]
@export var default_permanence: String = "persistent"
@export var default_time_horizon: String = "near"
@export var emitting_systems: Array[String] = []
@export var consuming_systems: Array[String] = []


func to_spec() -> Dictionary:
	return {
		"family": family,
		"required_payload_fields": required_payload_fields,
		"optional_payload_fields": optional_payload_fields,
		"default_scale_signature": default_scale_signature,
		"default_permanence": default_permanence,
		"default_time_horizon": default_time_horizon,
		"emitting_systems": emitting_systems,
		"consuming_systems": consuming_systems,
	}
