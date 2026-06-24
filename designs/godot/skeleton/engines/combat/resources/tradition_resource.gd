## tradition_resource.gd — a martial tradition as a COGNITIVE-MODE bias-vector over the shared
## substrate (combat_engine_v1 / tradition.py). A tradition does NOT add rules; it re-weights HOW
## its fighter reads/selects (channel weights, neutral = 1.0) and how well it reads an UNFAMILIAR
## opponent (familiarity). Channel abilities multiply a channel via `eff_cw` (now fully wired —
## audit: the "18/23, channels inert" claim was stale; routing is complete).
class_name TraditionResource
extends Resource

@export var tradition_id: String = "none"
@export var set_name: String = ""             # bridge named-set (Bind Fighter / Thrust Duelist / …)
@export var mode: String = ""                 # cognitive mode label

# channel weights (neutral 1.0). >1 emphasises, <1 de-emphasises.
@export var visual: float = 1.0               # pre-contact anticipation (Cog/Att)
@export var tactile: float = 1.0              # in-bind feeling (Fühlen / ting jin)
@export var precommit: float = 1.0            # pre-commitment intent-read (sen-sen-no-sen)
@export var leverage: float = 1.0             # bind leverage (Stärke-Schwäche)
@export var tempo: float = 1.0                # commitment-window exploitation
@export var measure: float = 1.0              # distance control (misura / maai / círculo)
@export var balance: float = 1.0              # geometric position (compás / FoV)

## equipped ability channel modifiers: {channel: factor} multiplied into eff_cw. Default empty.
@export var channel_modifiers: Dictionary = {}

const FAMILIARITY_DEFAULT := 0.85
const FAMILIARITY_ADJACENT := 0.93


## Effective channel weight = base × equipped-ability channel modifier (tradition.eff_cw).
func eff_cw(channel: String) -> float:
	var base: float = get(channel) if channel in self else 1.0
	return base * float(channel_modifiers.get(channel, 1.0))


## How well THIS tradition reads `opponent_id`. 1.0 if same or either is "none" (no style to misread).
## `adjacent` lists traditions this one cross-pollinated with (reads better). tradition.familiarity.
func familiarity(opponent_id: String, adjacent: Array = []) -> float:
	if opponent_id == tradition_id or tradition_id == "none" or opponent_id == "none":
		return 1.0
	if adjacent.has(opponent_id):
		return FAMILIARITY_ADJACENT
	return FAMILIARITY_DEFAULT
