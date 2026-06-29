## conviction_axis.gd — the 4-axis ethical vector space + projection (PP-684/687).
##
## This is the "vectorized" core. Every Key carries a position in this space
## (symbolic_dimensions) and a per-target effect (impact_vector). An observer
## interprets a Key through its OWN armature position, which is why the same event
## is a betrayal to one NPC and a triumph to another.
##
## Canon: designs/architecture/key_substrate_v30.md §2.4/§2.5;
##        designs/personal/conviction_axis_matrix_v30.md (the 13×4 matrix).
class_name ConvictionAxis
extends RefCounted

## The canonical 4-axis set (invariant — axis names are validated against this).
const AXES: Array[String] = ["hierarchical", "sacred", "instrumental", "traditional"]

## CONVICTION_AXIS_MATRIX[conviction][axis] — the 13×4 projection matrix.
## Loaded from data/conviction_axis_matrix.tres at boot; placeholder shape here.
static var MATRIX: Dictionary = {}


## armature_position = Σ over convictions: personal_convictions[c] × MATRIX[c][axis]
static func armature_position(personal_convictions: Dictionary) -> Dictionary:
	var pos := {}
	for axis in AXES:
		var acc := 0.0
		for c in personal_convictions.keys():
			var row: Dictionary = MATRIX.get(c, {})
			acc += float(personal_convictions[c]) * float(row.get(axis, 0.0))
		pos[axis] = acc
	return pos


## interpretation(observer, key) = Σ axis: armature[axis] × symbolic[axis] × impact[axis]
## A scalar that drives Concern salience, Disposition shift, Memory salience.
static func interpret(armature: Dictionary, symbolic: Dictionary, impact: Dictionary) -> float:
	var total := 0.0
	for axis in AXES:
		total += float(armature.get(axis, 0.0)) \
			* float(symbolic.get(axis, 0.0)) \
			* float(impact.get(axis, 0.0))
	return total


## Memory salience from interpretation magnitude + time horizon (substrate §4.5).
static func salience(interpretation: float, time_horizon: String) -> float:
	var horizon_factor := {"immediate": 1.5, "near": 1.0, "far": 0.5}.get(time_horizon, 1.0)
	return clampf(absf(interpretation) * horizon_factor, 0.0, 3.0)
