## key.gd — the universal event substrate record (PP-687 §2.1).
##
## Every consequential event in Valoria — a duel result, a debate outcome, a decree,
## a battle, a season tick — is one Key. One result type for everything, so a single
## delivery rule can carry it all, in every direction, to every scale.
##
## Canon: designs/architecture/key_substrate_v30.md §2 (schema), §2.4/§2.5 (vectors).
class_name Key
extends Resource

# --- Identity ---
@export var id: String = ""                        # globally unique (uuid)
@export var type: String = ""                      # registered family.subtype

# --- Causation ---
@export var source_actor: String = ""              # proximate cause; "" = environmental
@export var season_index: int = 0                  # ordered season position
@export var sub_step_index: int = 0                # ordered position within the season
@export var causes: Array[String] = []             # provenance: Key ids that led to this

# --- Targets & impact (each target carries the 4-axis impact vector + raw deltas) ---
## targets is an Array of Dictionaries:
##   { actor_id:String, role:String, impact_vector:Dictionary, stat_deltas:Dictionary }
## role ∈ {subject, object, witness, beneficiary, bystander}
## impact_vector keys ∈ ConvictionAxis.AXES (signed magnitude of effect on that actor)
@export var targets: Array[Dictionary] = []

# --- Scale & symbolic content (the "vectorized" part) ---
@export var scale_signature: Array[String] = []    # scales the event runs at
@export var symbolic_dimensions: Dictionary = {}   # event's position in 4-axis space

# --- Visibility (who can observe → who can form Memory) ---
@export var public: bool = false
@export var semi_public_observers: Array[String] = []
@export var private_observers: Array[String] = []

# --- Temporal ---
@export var time_horizon: String = "near"          # immediate | near | far
@export var permanence: String = "persistent"      # transient | persistent | indelible

# --- Type-specific payload + determinism metadata ---
@export var payload: Dictionary = {}
@export var rng_seed: int = 0                       # per-Key seed for replay determinism

# Awareness (PP-688): bumped when a later Key cites this one as a cause.
var awareness: float = 0.0


## Validate against the universal invariants (substrate §2.3). Type-specific
## payload validation is delegated to the KeyTypeRegistry.
func validate_universal() -> bool:
	if id.is_empty() or type.is_empty():
		return false
	if scale_signature.is_empty():
		return false
	# exactly one visibility mode
	var modes := 0
	if public: modes += 1
	if not semi_public_observers.is_empty(): modes += 1
	if not private_observers.is_empty(): modes += 1
	if modes != 1:
		return false
	# axis names must be canonical
	for d in symbolic_dimensions.keys():
		if not ConvictionAxis.AXES.has(d):
			return false
	return true


func is_ordered_after(other: Key) -> bool:
	if season_index != other.season_index:
		return season_index >= other.season_index
	return sub_step_index >= other.sub_step_index
