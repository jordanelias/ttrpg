"""
systems/threadwork/sim/params.py -- THE ONE OWNER of the threadwork oracle's tables and magnitudes.

`operations.py`, `collective.py` and `opposing.py` import these names from here and hold no literal copy of
any. `tools/export_engine_params.py` collects every uppercase JSON-typeable constant of this module into
`engine/engine_params/threadwork_params.json` (its `--check` re-derives and diffs it), so a table value a Godot
port reads is this file's, never a transcription: change a value HERE and regenerate; never edit the JSON.

This module imports nothing, so the exporter's auto-collection sees only constants defined here (a name
imported from another module would be exported as that module's).
"""
from __future__ import annotations


# §TN — TN IS 7. ALWAYS.
# [Jordan, 2026-08-25: "TN7 always. Never change TN anywhere ever."]
# PP-619's TN differential (Lock/Dissolution 8, Past-Oriented Pulling 8, POP-binding 9) is
# SUPERSEDED; TN_BINDING/TN_POP/TN_POP_BINDING are deleted. See ED-IN-0196 and
# registers/supersession_register.yaml.
#
# This is ROLL-NEUTRAL — precisely, and the precision matters. Every threadwork roll goes
# through engine/dice_engine/dice_engine.roll_pool, which has never read `tn` for any die, so
# the differential was inert from the day it was written: Locking, Dissolution and POP have
# always rolled at the same difficulty as Weaving. No die, draw or outcome moves.
# ONE OBSERVABLE DOES CHANGE, and it is not a roll: OperationResult.tn is a returned field,
# and it now reports 7 where it used to report 8 for the binding/POP operations. That is a
# report value catching up with what the engine was already doing, not a behaviour change —
# but 'byte-neutral' would be the wrong word for it, so it is not used.
#
# If binding operations SHOULD be harder, that is an Ob question under the ruling (the
# Three-Axis Ob system below is where it belongs), and it is a threadwork design decision
# — deliberately not smuggled in here.
# [canonical: params/threadwork.md §TN Modifiers]
#   ^ RETAINED and still true: 7 is that section's standard TN and that is what this constant
#     is. What is superseded is the section's DIFFERENTIAL (binding 8, POP 8, POP-binding 9).
# [canonical: Jordan ruling 2026-08-25 "TN7 always. Never change TN anywhere ever." — ED-IN-0196]
TN_STANDARD = 7    # every threadwork operation

# §Three-Axis Ob System — Depth Ob (Fibonacci). One line each, under its tag: the provenance gate reads a
# constant's own line and the line above it. The three tables are the Ob, Mending Ob and TS minimum
# columns of one table at the cited section (FORK:c451bcb: engine/params/threadwork.md, the file at the fork).
# [canonical: FORK:c451bcb:engine/params/threadwork.md §Depth Ob — the "Ob" column]
DEPTH_OB = {"Object": 1, "Personal": 2, "Relational": 3, "Field": 5, "Structural": 8, "Foundational": 13}

# §Three-Axis Ob — Mending Ob (different scale per Mending)
# [canonical: FORK:c451bcb:engine/params/threadwork.md §Depth Ob — the "Mending Ob" column (Object and Personal: n/a)]
MENDING_OB = {"Relational": 2, "Field": 4, "Structural": 7, "Foundational": 12}

# §Three-Axis Ob — TS minimums per Depth
# [canonical: FORK:c451bcb:engine/params/threadwork.md §Depth Ob — the "TS minimum" column (30+, 30+, 50+, 50+, 70+, 90+)]
DEPTH_TS_MINIMUM = {"Object": 30, "Personal": 30, "Relational": 50, "Field": 50, "Structural": 70, "Foundational": 90}  # read by nothing until CR-13 (B35)

# §Leap Ob by Thread Sensitivity
# [canonical: threadwork_v30 §2.3 — "Thread Sensitivity 30-49 = 2 · Thread Sensitivity 50+ = 1"]
LEAP_OB_TS_LOW = 2     # TS 30-49
LEAP_OB_TS_HIGH = 1    # TS 50+

# §3.2 Coherence cost by scale
# [canonical: threadwork_v30 §3.2 Coherence Reduction table]
COHERENCE_COST_BY_SCALE = {
    "Object":       0,
    "Personal":     0,
    "Relational":   -1,
    "Field":        -1,
    "Territorial":  -1,
    "Structural":   -2,
    "Foundational": -2,
}

# FR (Forced Resolution) surcharge per PP-196 (Lock or Dissolution)
# [canonical: §3.2 — "FR surcharge cap exemption (PP-196)"]
FR_SURCHARGE = -1

# R-14 — THE PRACTITIONER-SIDE TERM ON A WORKING'S COHERENCE COST (WR-01).
# canon/philosophy/06_operations.md "How large the cost is, and what resists it" (ruled 2026-09-09):
# "What determines their ability to prevent that cost is how resilient their spirit is — which is how
# strongly configured they are." Canon says it is NOT thread sensitivity, NOT imbrication, NOT size. `operations.py`
# derives it from nothing: it reads one duck-typed slot (`actor.resilience`, a non-negative int,
# absent = 0). The slot's NAME and what fills it (Spirit is a candidate input, GO-01 / J-9 in the plan) are
# unruled, and the builder's `resilience` is a placeholder until they are. It "sits alongside" D-5's type
# x scale and §6.6's direction test:
# those still form the working's cost; this term only RESISTS it (`resist_coherence_cost` below).
# THE ARITHMETIC IS UNRULED (RULINGS.md Batch 13 retracted C-3's "no toughness term" without ruling a
# shape), so it ships as a SWEPT FIXTURE on H-94's precedent (engine/season/hole_register.yaml,
# `sweep: [0, 1, 3]`): the gain is whole Coherence units resisted per point of resilience, and the
# shipped value 0 is THE CONTROL — today's behaviour, byte-for-byte. Arms 1 and 3 are the builder's.
# The sweep is a tuple here, not a comment (tests/valoria/test_threadwork_resilience.py ran it; retired).
RESILIENCE_GAIN_SWEEP = (0, 1, 3)  # [JUSTIFIED: R-14 ruled 2026-09-09 sources the mechanism (resilience resists the cost); magnitude unruled — swept fixture on H-94's precedent, arms are the builder's]
RESILIENCE_GAIN = 0                # [JUSTIFIED: R-14 ruled 2026-09-09 sources the mechanism; magnitude unruled — shipped arm RESILIENCE_GAIN_SWEEP[0], the control = pre-R-14 behaviour]

# WR-02 — WHAT A MENDING AIMED AT THE MENDER'S OWN CONFIGURATION ACHIEVES ON THE RESTING POINT, by
# degree: the `amount` handed to `coherence.mend_resting_point` (see `attempt_mending`). The floor
# moves only when the working clearly took, so Partial and Failure move nothing. One owner; tests read it
# rather than restate it. ⚠ [GAP] C-1 calls moving the floor "extremely difficult to do but possible",
# and the difficulty belongs in the caller's Ob (coherence.mend_resting_point). It is NOT modelled here:
# an own-aim Mending rolls the ordinary MENDING_OB (a target with no scale prices Relational, Ob 2), so a
# Success is roughly 0.6 likely at pool 8 and 0.85 at pool 14 (hand estimate, normal approximation, not a
# measurement), and an attempt costs nothing (ED-871), so repeated casts can walk a permanent set to 0.
# A cost, a cadence or a harder Ob is a design call, carried in HANDOFF_WR.md.
RESTING_POINT_MEND_BY_DEGREE = {"Overwhelming": 1, "Success": 1, "Partial": 0, "Failure": 0}  # [JUSTIFIED: RULINGS.md C-1 (floor movable, "extremely difficult") + canon/philosophy/06_operations.md §6.8 aim distinction (derived) source the mechanism; magnitude invented]
