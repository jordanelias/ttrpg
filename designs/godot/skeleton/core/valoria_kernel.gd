## valoria_kernel.gd — THE WRAPPER (requirement 1) (AUTOLOAD).
##
## A thin orchestrator that holds no game logic. It boots the registries, instantiates
## every engine, drives the season loop, manages the zoom stack of scene containers,
## and owns save/load. Engines never reference the Kernel or each other — they speak
## only Keys through the KeyBus.
extends Node

signal phase_changed(phase: String)
signal scene_pushed(scene_id: String)
signal scene_popped(scene_id: String)

enum Phase { BRIEFING, PERSONAL, STRATEGIC, ACCOUNTING }
const PHASE_NAMES: Array[String] = ["briefing", "personal", "strategic", "accounting"]

var engines: Array[BaseEngine] = []
var current_phase: Phase = Phase.BRIEFING
var zoom_stack: Array[String] = []                  # scene container ids (max depth 2)
const MAX_ZOOM_DEPTH := 2


func _ready() -> void:
	_boot()


func _boot() -> void:
	# 1. deterministic RNG + data
	GameState.seed_rng(_initial_seed())
	KeyTypeRegistry.load_from_dir("res://data/key_types")
	ConvictionAxis.MATRIX = load("res://data/conviction_axis_matrix.tres").matrix \
		if ResourceLoader.exists("res://data/conviction_axis_matrix.tres") else {}

	# 2. discover + instantiate engines from manifests; they self-subscribe on the bus
	MechanicsRegistry.load_manifests("res://data/engines")
	engines = MechanicsRegistry.build_engines()

	# 3. assert the hard constraints (GD-1 etc.) before the game runs
	_assert_constraints()


## Drive the season state machine. Boundaries emit mechanical.* Keys so every
## subscribing engine ticks through the same substrate.
func advance_phase() -> void:
	current_phase = ((current_phase + 1) % PHASE_NAMES.size()) as Phase
	var phase_name := PHASE_NAMES[current_phase]
	for e in engines:
		e.season_tick(phase_name)
	if current_phase == Phase.ACCOUNTING:
		_emit_engine_key("mechanical.accounting", ["peninsula"])
	elif current_phase == Phase.BRIEFING:
		_emit_engine_key("mechanical.season_change", ["peninsula"])
	phase_changed.emit(phase_name)


# --- Zoom stack: push/pop scene containers (the "containers" of the design) ---
func push_scene(scene_id: String) -> bool:
	if zoom_stack.size() >= MAX_ZOOM_DEPTH:
		push_warning("Kernel: max zoom depth reached; resolving %s abstractly" % scene_id)
		return false
	zoom_stack.append(scene_id)
	_emit_engine_key("mechanical.scene_entered", ["scene"], {"scene_id": scene_id,
		"stack_depth_after": zoom_stack.size()})
	scene_pushed.emit(scene_id)
	return true


func pop_scene() -> void:
	if zoom_stack.is_empty():
		return
	var scene_id: String = zoom_stack.pop_back()
	_emit_engine_key("mechanical.scene_exited", ["scene"], {"scene_id": scene_id})
	scene_popped.emit(scene_id)


# --- Save / load: save = initial_state + Key log (deterministic replay) ---
func save_game(path: String) -> void:
	var data := {
		"initial_state": GameState.initial_snapshot,
		"world": GameState.snapshot(),
		"key_log": GameState.serialize_keys(KeyBus.key_log),
		"seed": GameState.rng_seed,
	}
	FileAccess.open(path, FileAccess.WRITE).store_var(data)


func load_game(path: String) -> void:
	var data: Dictionary = FileAccess.open(path, FileAccess.READ).get_var()
	GameState.restore(data["world"])
	# replay is optional: re-run the log through KeyBus for verification.


# --- internals ---
func _emit_engine_key(type: String, scales: Array, payload: Dictionary = {}) -> void:
	var k := Key.new()
	k.id = GameState.new_key_id()
	k.type = type
	k.scale_signature.assign(scales)
	k.public = true
	k.permanence = "indelible"
	k.time_horizon = "immediate"
	k.payload = payload
	k.season_index = GameState.season_index
	KeyBus.emit_key(k)


func _assert_constraints() -> void:
	# GD-1: peninsula-only victory — exactly one engine may produce a game-end trigger.
	var victory_engines := engines.filter(func(e): return e.has_method("can_end_game"))
	assert(victory_engines.size() <= 1, "GD-1: more than one engine can end the game")


func _initial_seed() -> int:
	return 0  # injected from the save / new-game screen; 0 = fixed for dev determinism
