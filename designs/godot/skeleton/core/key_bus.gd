## key_bus.gd — the vectorized Key orchestration framework (AUTOLOAD).
##
## Requirement (2): the framework that orchestrates all systems and moves data in
## ALL directions via a vectorized key-system. This is the ONE substrate; no engine
## keeps a private event channel. Direction (up/down/lateral/diagonal) is emergent
## from each Key's targets[]/scale_signature/visibility — not hard-wired channels.
##
## Canon: designs/architecture/key_substrate_v30.md §4.1 (the single update rule),
##        §4.2 (observer resolution), scale_transitions_v30.md §12 (all-directions).
extends Node

signal key_emitted(key: Key)          # UI/telemetry may listen; engines subscribe by type
signal key_applied(key: Key)

var key_log: Array[Key] = []                              # the append-only save substrate
var _type_subscriptions: Dictionary = {}                 # type -> Array[BaseEngine]
var _causal_children: Dictionary = {}                    # key_id -> Array[key_id]
var _by_id: Dictionary = {}                              # key_id -> Key


## Engines register the Key types they consume (called by the Kernel at boot).
func subscribe(engine, types: Array) -> void:
	for t in types:
		if not _type_subscriptions.has(t):
			_type_subscriptions[t] = []
		if not _type_subscriptions[t].has(engine):
			_type_subscriptions[t].append(engine)


## THE SINGLE UPDATE RULE — the only path by which engine state changes.
func emit_key(key: Key) -> bool:
	# 1. validate (universal invariants + per-type payload schema)
	if not key.validate_universal() or not KeyTypeRegistry.validate(key):
		push_error("KeyBus: rejected invalid Key %s (type %s)" % [key.id, key.type])
		return false
	if _detect_cycle(key):
		push_error("KeyBus: Key %s would introduce a causal cycle" % key.id)
		return false

	# 2. append (immutable log)
	key_log.append(key)
	_by_id[key.id] = key

	# 3. resolve observers (source + targets + actors_in_scale + visibility)
	var observers := _compute_observers(key)

	# 4. each observer interprets through its OWN armature and applies
	for actor_id in observers:
		var actor = GameState.get_actor(actor_id)
		if actor == null:
			continue
		var interp := ConvictionAxis.interpret(
			actor.armature_position(), key.symbolic_dimensions,
			_impact_for(key, actor_id))
		actor.memory_record(key.id, ConvictionAxis.salience(interp, key.time_horizon))
		actor.apply_state_changes(interp, _stat_deltas_for(key, actor_id))

	# 5. cross-system propagation (the registry routing — every direction)
	for sys in _type_subscriptions.get(key.type, []):
		sys.consume(key)

	# 6. causal graph + awareness bump on cited causes
	for cause_id in key.causes:
		if not _causal_children.has(cause_id):
			_causal_children[cause_id] = []
		_causal_children[cause_id].append(key.id)
		var cause: Key = _by_id.get(cause_id)
		if cause:
			cause.awareness = clampf(cause.awareness + 0.1, 0.0, 1.0)

	key_emitted.emit(key)
	key_applied.emit(key)
	return true


## Observer set = source_actor ∪ every target ∪ (public ? actors_in_scale : witness lists).
func _compute_observers(key: Key) -> Dictionary:
	var obs := {}
	if not key.source_actor.is_empty():
		obs[key.source_actor] = true
	for t in key.targets:
		obs[t.get("actor_id", "")] = true
	if key.public:
		for a in GameState.actors_in_scale(key.scale_signature):
			obs[a] = true
	for a in key.semi_public_observers:
		obs[a] = true
	for a in key.private_observers:
		obs[a] = true
	obs.erase("")
	return obs


func _impact_for(key: Key, actor_id: String) -> Dictionary:
	for t in key.targets:
		if t.get("actor_id", "") == actor_id:
			return t.get("impact_vector", {})
	return {}


func _stat_deltas_for(key: Key, actor_id: String) -> Dictionary:
	for t in key.targets:
		if t.get("actor_id", "") == actor_id:
			return t.get("stat_deltas", {})
	return {}


## BFS cycle check over causes[] (substrate §4.6).
func _detect_cycle(key: Key) -> bool:
	var queue := key.causes.duplicate()
	var visited := {}
	while not queue.is_empty():
		var cid: String = queue.pop_front()
		if cid == key.id:
			return true
		if visited.has(cid):
			continue
		visited[cid] = true
		var c: Key = _by_id.get(cid)
		if c:
			queue.append_array(c.causes)
	return false


## Diagnostic walk: backward = the cause chain; forward = the consequence cascade.
func walk_backward(key_id: String, depth_limit: int = 10) -> Array[String]:
	return _walk(key_id, depth_limit, true)

func walk_forward(key_id: String, depth_limit: int = 10) -> Array[String]:
	return _walk(key_id, depth_limit, false)

func _walk(start: String, depth_limit: int, backward: bool) -> Array[String]:
	var visited := {}
	var queue := [[start, 0]]
	while not queue.is_empty():
		var item: Array = queue.pop_front()
		var cid: String = item[0]
		var d: int = item[1]
		if visited.has(cid) or d > depth_limit:
			continue
		visited[cid] = true
		var nexts: Array = []
		if backward:
			var k: Key = _by_id.get(cid)
			nexts = k.causes if k else []
		else:
			nexts = _causal_children.get(cid, [])
		for n in nexts:
			queue.append([n, d + 1])
	visited.erase(start)
	var out: Array[String] = []
	out.assign(visited.keys())
	return out
