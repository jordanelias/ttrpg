## engine_module.gd — the plug-in contract (requirement 3b).
##
## A module is ONE pluggable behaviour an engine hosts, in the canonical contract
## shape from references/module_contracts.yaml:
##
##     IN (consumed Key types) → resolver → OUT (emitted Key types)
##                               owns: declared scalars (bucket-classified)
##                               crosses scales only via declared transitions
##
## New modules are added as data (a .tres manifest + a .gd extending this) with ZERO
## edits to the kernel/bus/base-engine. Two modules coexist in one engine because each
## declares the Key types it handles; the engine dispatches by type.
class_name EngineModule
extends Resource

enum Resolver { DICE_POOL, D_SIGMA, DETERMINISTIC_ACCOUNTING, CLOCK_ADVANCE,
	ARMATURE_DOT_PRODUCT, STATE_READER, MANIFEST }

@export var module_id: String = ""
@export var resolver: Resolver = Resolver.STATE_READER
@export var consumes: Array[String] = []           # Key types this module handles
@export var emits: Array[String] = []              # Key types this module produces
## owned scalars: Array of { name:String, bucket:String, writable:bool }
## bucket ∈ {pool, derived_value, track, clock}; derived_value is write-protected (F1).
@export var owned_scalars: Array[Dictionary] = []
@export var transitions: Array[String] = []        # scale_transitions handoffs used

var engine: BaseEngine                              # set on register


func register(host: BaseEngine) -> void:
	engine = host


## Does this module handle the given Key type?
func handles(key_type: String) -> bool:
	return consumes.has(key_type)


## Resolve one consumed Key. Override in concrete modules. The base does nothing.
## Concrete modules read inputs, run their resolver, and call `produce()` for outputs.
func resolve(_key: Key) -> void:
	pass


## Helper: emit an outcome Key through the bus (never a private channel).
func produce(key: Key) -> void:
	if not emits.has(key.type):
		push_warning("Module %s emitted undeclared type %s" % [module_id, key.type])
	KeyBus.emit_key(key)
