## base_engine.gd — the base mechanical engine (requirement 3a).
##
## Every cohesive resolution system (CombatEngine, FactionEngine, ThreadEngine, …)
## extends this. It is a THIN host: it owns scalar state, holds pluggable modules,
## declares its Key ports, and routes consumed Keys to the right module. It speaks
## ONLY Keys — it never references the kernel or another engine directly.
##
## Lifecycle discipline (checked by the Engine-Shape Conformance methodology):
##   setup → on_key → season_tick → serialize/restore.
## Plus the hard invariants: writes only its own scalars; cross-scale effects leave
## only as Keys via declared transitions; never imports a higher-scale engine.
class_name BaseEngine
extends Node

@export var engine_id: String = ""
@export var scale: String = ""                      # personal | scene | territory | provincial | peninsula | thread | meta
@export var accounting_phase: Array[String] = []    # spine phases it acts in

var modules: Array[EngineModule] = []
var _by_consumed_type: Dictionary = {}              # key_type -> Array[EngineModule]


## Called by the Kernel at boot. Loads modules from manifest, then registers the
## union of their consumed types on the KeyBus.
func setup(module_manifests: Array[EngineModule]) -> void:
	for m in module_manifests:
		add_module(m)
	KeyBus.subscribe(self, consumed_types())
	_on_setup()


func add_module(m: EngineModule) -> void:
	m.register(self)
	modules.append(m)
	for t in m.consumes:
		if not _by_consumed_type.has(t):
			_by_consumed_type[t] = []
		_by_consumed_type[t].append(m)


func consumed_types() -> Array:
	return _by_consumed_type.keys()


## A consumed Key arrives from the bus → dispatch to every module that handles it.
func consume(key: Key) -> void:
	for m in _by_consumed_type.get(key.type, []):
		m.resolve(key)
	on_key(key)


# --- Overridable hooks (concrete engines override as needed) ---
func _on_setup() -> void: pass
func on_key(_key: Key) -> void: pass
func season_tick(_phase: String) -> void: pass


## Serialize this engine's OWNED scalars only (routed to GameState).
func serialize() -> Dictionary:
	return {}

func restore(_data: Dictionary) -> void:
	pass


## Discipline guard: a derived_value scalar is write-protected (F1). Engines route
## deltas to the substrate stat; this asserts the rule in debug builds.
func assert_writable(scalar_name: String, bucket: String) -> void:
	assert(bucket != "derived_value",
		"%s: '%s' is a derived_value — write its substrate stat, not the derived value (F1)"
		% [engine_id, scalar_name])
