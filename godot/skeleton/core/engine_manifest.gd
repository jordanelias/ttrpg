## engine_manifest.gd — one engine's discovery manifest (data). MechanicsRegistry.load_manifests
## reads data/engines/<id>/<id>.tres, calls to_spec(), and the Kernel builds the engine from it —
## a new engine is registered by DATA, with zero edits to Kernel/Bus/BaseEngine. Mirrors the
## references/module_contracts.yaml entry for the engine.
class_name EngineManifest
extends Resource

@export var engine_id: String = ""
@export_file("*.gd") var engine_script: String = ""        # the BaseEngine subclass
@export var scale: String = ""
@export var modules: Array[String] = []                    # res:// paths to the module .tres manifests
@export var accounting_phase: Array[String] = []


func to_spec() -> Dictionary:
	return {
		"script": engine_script,
		"scale": scale,
		"modules": modules,
		"accounting_phase": accounting_phase,
	}
