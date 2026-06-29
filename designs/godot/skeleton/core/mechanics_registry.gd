## mechanics_registry.gd — manifest-driven engine/module discovery (AUTOLOAD).
##
## Requirement (1) support + requirement (3) extensibility. Reads the engine and
## module manifests (data/engines/*.tres, mirroring references/module_contracts.yaml
## + canon/mechanics_index.yaml) and yields the set of engines, their modules, and
## their Key subscriptions. The Kernel builds the world from THIS — so a new engine
## or module is registered by data, with zero edits to core.
extends Node

## engine_id -> { script:String, scale:String, modules:Array[String],
##                gd_constraints:Array, accounting_phase:Array }
var engine_specs: Dictionary = {}


func load_manifests(dir_path: String) -> void:
	var dir := DirAccess.open(dir_path)
	if dir == null:
		return
	for sub in dir.get_directories():
		var manifest_path := dir_path.path_join(sub).path_join("%s.tres" % sub)
		if FileAccess.file_exists(manifest_path):
			var m := load(manifest_path)
			if m and m.has_method("to_spec"):
				engine_specs[m.engine_id] = m.to_spec()


## Instantiate every registered engine with its modules, ready for Kernel.setup().
func build_engines() -> Array[BaseEngine]:
	var engines: Array[BaseEngine] = []
	for engine_id in engine_specs.keys():
		var spec: Dictionary = engine_specs[engine_id]
		var engine: BaseEngine = load(spec["script"]).new()
		engine.engine_id = engine_id
		engine.scale = spec.get("scale", "")
		engine.accounting_phase.assign(spec.get("accounting_phase", []))
		var module_resources: Array[EngineModule] = []
		for mpath in spec.get("modules", []):
			module_resources.append(load(mpath))
		engine.setup(module_resources)
		engines.append(engine)
	return engines


func engines_at_scale(s: String) -> Array:
	return engine_specs.keys().filter(func(eid): return engine_specs[eid].get("scale", "") == s)
