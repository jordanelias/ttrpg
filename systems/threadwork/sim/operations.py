"""
systems/threadwork/sim/operations.py — Thread operations: Leap, Weaving, Pulling, Past-Pulling, Locking, Dissolution, Mending

Canon source: systems/threadwork/reference/threadwork_v30.md Part 2 (§2.3-§2.6)
Params source: params/threadwork.md (TN modifiers, Three-Axis Ob, Thread Pool formula)

Implements 7 operation entry points + the Three-Axis Ob lookup (Depth + Breadth
+ Distance per params §Three-Axis Ob System). Each operation:
  - Constructs pool per PP-616/618/619 canonical pool formula
  - Looks up TN per §TN Modifiers
  - Resolves degree (Overwhelming/Success/Partial/Failure)
  - Applies Coherence delta via systems/threadwork/sim/coherence (already landed)
  - Returns OperationResult with degree + side-effects

[ASSUMPTION: practitioner stats sourced from caller — basis: actor parameter
 is a duck-typed object with .spirit, .focus, .ts (Thread Sensitivity), and
 optionally .history dict. World has no practitioner stat schema yet.
 When practitioner state is added to World, signature accepts actor_id +
 looks up. Until then, caller supplies a Practitioner-like object.]

Dependencies:
  - sim/autoload/dice_engine
  - systems/threadwork/sim/coherence (apply_coherence_delta; recover + get_state for Mending's
    restorative feedback)
  - sim/cross_scale/handoff_rules (TS-banded coherence cost for mass-battle context)

Entry points:
  - attempt_leap(actor, target_state, world) -> OperationResult
  - attempt_weaving(actor, target, world) -> OperationResult
  - attempt_pulling(actor, target, world) -> OperationResult
  - attempt_past_pulling(actor, target_moment, world) -> OperationResult
  - attempt_locking(actor, target, world) -> OperationResult
  - attempt_dissolution(actor, target, world) -> OperationResult
  - attempt_mending(actor, target, world, *, environment_in_equilibrium=False) -> OperationResult
    (keyword-only; defaults to False, so a caller that states no environment gets no restorative term)
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional, Any

from engine.dice_engine import dice_engine
from engine.dice_engine.dice_engine import roll_pool
from systems.threadwork.sim.coherence import apply_coherence_delta, get_state, recover


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

# §Three-Axis Ob System — Depth Ob (Fibonacci)
# [canonical: params/threadwork.md §Depth Ob]
DEPTH_OB = {
    "Object":       1,
    "Personal":     2,
    "Relational":   3,
    "Field":        5,
    "Structural":   8,
    "Foundational": 13,
}

# §Three-Axis Ob — Mending Ob (different scale per Mending)
MENDING_OB = {
    "Relational":   2,
    "Field":        4,
    "Structural":   7,
    "Foundational": 12,
}

# §Three-Axis Ob — TS minimums per Depth
DEPTH_TS_MINIMUM = {
    "Object":       30,
    "Personal":     30,
    "Relational":   50,
    "Field":        50,
    "Structural":   70,
    "Foundational": 90,
}

# §Three-Axis Ob — Breadth Ob
BREADTH_OB = {
    "Single":      0,
    "Small group": 1,
    "Formation":   2,
    "Battlefield": 3,
    "Regional":    4,
}

# §Three-Axis Ob — Distance Ob
DISTANCE_OB = {
    "Contact/Close": 0,
    "Near":          1,
    "Distant":       2,
    "Far":           3,
}

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

# P-25 "Scale-based Mending Stability" — the SCALE TERM on Mending Stability, authored here because
# ED-WR-0008's superseding row (2026-09-15, registers/editorial_ledger_wr_archive.jsonl) says so:
# the P-25 override table was truncated at authoring to its header plus the label `Object`, NOTHING
# READ IT, and "the scale term is authored IN CODE with its citation when position 27 runs, and the
# doc follows" (ED-WR-0010's ruled row, consequence 3). Position 27 is this change.
# THE OVERRIDE IS A FORMULA ON `COHERENCE_COST_BY_SCALE`, NOT A SECOND TABLE. A hand-kept
# `MS_COST_BY_SCALE_BAND` literal was tried first; its own test proved every one of its 14 cells
# equalled `Partial = COHERENCE_COST_BY_SCALE[scale]`, `Failure = Partial - 1` with zero exceptions
# across all seven scales — a second hand-kept copy of one fact (CLAUDE.md §8 "every rule lives
# once"; found by an adversarial /simplify pass on this position).
# ⚠ THE MAGNITUDES ARE NOT NEW, BUT PRICING MENDING STABILITY OFF COHERENCE'S TABLE IS ITS OWN
# UNCITED CHOICE (found by the Phase-3 terminal critique on this position). `COHERENCE_COST_BY_SCALE`
# is cited to §3.2 "Coherence Reduction" — a practitioner-Coherence price, not a Mending-Stability
# one — and nothing in `RULINGS.md`/`07_drift.md` says the two are the same quantity. `opposing.py`
# makes the identical move and names it what it is: "use scale cost as proxy". This override does the
# same, reusing already-invented numbers rather than inventing new ones, but the REUSE is the
# invention. A nearer, unused precedent exists in the quarantined reference
# (`.designs/systems/threadwork/reference/threadwork_v30.md:589-595`): MS -1..-5 over P-25's own five
# bands, a steeper ladder than this proxy — which ladder to run is a design call for Jordan, not
# settled here.
# THE SHAPE: the override replaces the degree table's Partial/Failure values where the degree table
# applies (Weaving/Pulling) and leaves Locking/Dissolution's flat binding cost (`ms_delta = -1` in
# `_resolve_operation` below) untouched — that flat cost PREDATES this position and is itself a
# divergence from threadwork_v30.md's own Locking/Dissolution degree tables (`:398-403`'s Partial/
# Failure -2/-3, `:433-438`'s -6/-8), out of ED-WR-0008's scope to correct here. At the
# Relational/Territorial tier the formula reproduces the old degree-only table (-1/-2) EXACTLY, so
# the term moves only the ends. See the P-25 branch in `_resolve_operation` below for the formula
# itself — and HANDOFF_WR.md for the fact that nothing yet reads its result.


@dataclass
class OperationResult:
    """Result of a single Thread operation."""
    operation: str             # 'Leap' / 'Weaving' / 'Pulling' / etc.
    actor: str                 # Actor id
    degree: str                # 'Overwhelming' / 'Success' / 'Partial' / 'Failure'
    net_successes: int
    pool: int
    tn: int
    ob: int
    coherence_delta: int       # the STRESS applied to the actor's Coherence (<= 0; coherence.py)
    # MS impact. REPORTED, written nowhere: the world MS clock it once fed has no season analogue
    # (plan position `29a`; struck at position 27 in co_movement.py and opposing.py alike).
    mending_stability_delta: int = 0
    # The elastic displacement a restorative working actually RETURNED to the mender (>= 0): what
    # `coherence.recover` moved, not what was offered to it. Only Mending sets it; see
    # `attempt_mending`.
    coherence_restored: int = 0
    notes: list[str] = field(default_factory=list)


def _compute_degree(net_successes: int | float, ob: int | float) -> str:
    """Map net_successes vs Ob to a degree label. Adapter over the owner, not a second ladder.

    This module's own `ob + 3` Overwhelming bar was already the ruled margin rule; what changed
    with the 2026-08-14 ruling is the Partial band, which was `0 < net < Ob` and is now the
    met-but-not-exceeded window. See `dice_engine.degree_from_net`.
    """
    return dice_engine.degree_label(net_successes, ob)


def _actor_pool(actor) -> int:
    """Compute (Spirit × 2) + relevant History bonus + TPS per PP-616.

    actor must expose: .spirit (1-7), .ts (Thread Sensitivity 0-100),
    and optionally .history (relevant points; +3 constant per PP-624).
    """
    spirit = getattr(actor, 'spirit', 4)
    ts = getattr(actor, 'ts', 30)
    history = getattr(actor, 'history', 0)  # Points; constant +3 already in pool baseline
    tps = ts // 10
    # PP-624: (Spirit × 2) + (History + 3 constant, capped +3D from level) + TPS
    history_contrib = min(3, history + 3)
    return (spirit * 2) + history_contrib + tps


def _resolve_operation(operation: str, actor, ob: int, tn: int,
                       coherence_delta: int, world=None,
                       rng=None, scale: str = "Object") -> OperationResult:
    """Shared resolution path for all Thread operations.

    Rolls actor's pool, computes degree, applies Coherence delta.
    `scale` is read only by the P-25 Mending Stability override (Weaving/Pulling); its default is
    the same Object fallback attempt_weaving/attempt_pulling apply to a target with no scale.
    Returns OperationResult.
    """
    pool = _actor_pool(actor)
    actor_id = getattr(actor, 'actor_id', getattr(actor, 'name', 'unknown'))

    # Roll
    rng = rng if rng is not None else (world.rng if world is not None and hasattr(world, 'rng') else None)
    if rng is None:
        import random
        rng = random.Random()
    net_successes = roll_pool(pool, tn=tn, rng=rng).net if pool > 0 else 0

    degree = _compute_degree(net_successes, ob)

    # Apply Coherence delta — modulated by degree per §3.2
    # Failure on certain ops produces additional -1 Coherence (e.g. Pull failure
    # per §2.4 Pulling table); Partial often -1 additional. For Tier 1 first
    # pass, apply base coherence_delta + extra -1 on Partial/Failure.
    # ED-871 exception: Mending is a restorative operation and costs 0 Coherence
    # at EVERY degree, so it is exempt from the blanket Partial/Failure penalty
    # (else Partial/Failure Mending would net -1, against canon). The broader
    # C-TW-3 defect — this blanket penalty also mis-hits Leap against its own
    # docstring — is NOT fixed here (separate item, ED-WR-0005 Stratum-B tail).
    effective_coh = coherence_delta
    if degree in ("Partial", "Failure") and operation != "Mending":
        effective_coh -= 1

    if effective_coh != 0:
        apply_coherence_delta(actor_id, effective_coh, f"{operation} {degree}", world=world)

    # Mending Stability impact. Weaving/Pulling: the degree table's Partial/Failure values,
    # OVERRIDDEN by scale per P-25 (ED-WR-0008, see the comment above): Partial = the scale's
    # own Coherence cost, Failure = Partial - 1. The retired degree-only form was Partial -1 /
    # Failure -2 at every scale.
    ms_delta = 0
    if operation in ("Weaving", "Pulling") and degree in ("Partial", "Failure"):
        base = COHERENCE_COST_BY_SCALE.get(scale, 0)
        ms_delta = base if degree == "Partial" else base - 1
    elif operation in ("Locking", "Dissolution"):
        ms_delta = -1  # Binding ops always cost MS

    return OperationResult(
        operation=operation,
        actor=actor_id,
        degree=degree,
        net_successes=net_successes,
        pool=pool,
        tn=tn,
        ob=ob,
        coherence_delta=effective_coh,
        mending_stability_delta=ms_delta,
    )


def attempt_leap(actor, target_state: dict, world=None, rng=None) -> OperationResult:
    """§2.3 The Leap — Suspending Rendering.

    target_state: dict with optional 'ts_minimum' (default 30) for eligibility check.
    Returns OperationResult. Failure does NOT cost Coherence per §3.2 (Leap
    is the rendering-suspension act, not yet an operation).
    """
    ts = getattr(actor, 'ts', 0)
    # Eligibility: TS 30+
    if ts < 30:
        return OperationResult(
            operation="Leap", actor=getattr(actor, 'actor_id', 'unknown'),
            degree="Failure", net_successes=0, pool=0, tn=TN_STANDARD, ob=0,
            coherence_delta=0,
            notes=["Eligibility failure: TS < 30 (§2.3 Eligibility)"]
        )

    # Leap Ob per TS band
    ob = LEAP_OB_TS_LOW if ts < 50 else LEAP_OB_TS_HIGH
    # Leap itself has no Coherence cost (operations during contact do)
    return _resolve_operation("Leap", actor, ob, TN_STANDARD,
                              coherence_delta=0, world=world, rng=rng)


def attempt_weaving(actor, target: dict, world=None, rng=None) -> OperationResult:
    """§2.4 Weaving — Things Cohere.

    target: dict with 'scale' (Object/Personal/Relational/Field/Structural),
            optional 'breadth', 'distance'.
    """
    scale = target.get('scale', 'Object')
    ob = DEPTH_OB.get(scale, 1)
    coh = COHERENCE_COST_BY_SCALE.get(scale, 0)
    return _resolve_operation("Weaving", actor, ob, TN_STANDARD,
                              coherence_delta=coh, world=world, rng=rng, scale=scale)


def attempt_pulling(actor, target: dict, world=None, rng=None) -> OperationResult:
    """§2.4 Pulling — Things Open."""
    scale = target.get('scale', 'Object')
    ob = DEPTH_OB.get(scale, 1)
    coh = COHERENCE_COST_BY_SCALE.get(scale, 0)
    return _resolve_operation("Pulling", actor, ob, TN_STANDARD,
                              coherence_delta=coh, world=world, rng=rng, scale=scale)


def attempt_past_pulling(actor, target_moment: dict, world=None, rng=None) -> OperationResult:
    """§2.4 Past-Oriented Pulling. TN 7 (ED-IN-0196; PP-619's TN 8 is superseded).

    target_moment: dict with 'recency' ('same_scene' / '1-2_seasons' / etc) and 'scale'.
    Per §3.2: POP costs −1 Coherence ADDITIONAL on top of standard Pulling cost.
    """
    scale = target_moment.get('scale', 'Object')
    # POP Ob lookup by recency
    recency = target_moment.get('recency', 'same_scene')
    pop_recency_ob = {'same_scene': 3, '1-2_seasons': 4, '3-5_seasons': 5,
                      '6-10_seasons': 6, '10+_seasons': 7}
    ob = pop_recency_ob.get(recency, 3)
    coh = COHERENCE_COST_BY_SCALE.get(scale, 0) - 1  # POP adds -1 per §3.2
    # Per-op cap per TW-05 (POP Coherence -1 additional IS subject to per-op cap)
    # Total POP Coherence cost capped at -1 max regardless of scale
    coh = max(-1, coh) if scale in ("Object", "Personal") else coh
    return _resolve_operation("Past-Oriented Pulling", actor, ob, TN_STANDARD,
                              coherence_delta=coh, world=world, rng=rng)


def attempt_locking(actor, target: dict, world=None, rng=None) -> OperationResult:
    """§2.4 Locking — Unable to Become. TN 7 (ED-IN-0196; PP-619's TN 8 is superseded). FR surcharge per PP-196.

    Coherence cost: scale + FR surcharge (cap-exempt). Per §3.2:
      Object/Personal scale: -1 total (FR surcharge only; scale cost = 0)
      Relational: -2 total (-1 scale + -1 FR)
      Territorial: -2 total
      Structural: -3 total (-2 scale + -1 FR)
    """
    scale = target.get('scale', 'Object')
    scale_cost = COHERENCE_COST_BY_SCALE.get(scale, 0)
    # FR surcharge is cap-exempt per PP-196
    coh = scale_cost + FR_SURCHARGE
    return _resolve_operation("Locking", actor, DEPTH_OB.get(scale, 1), TN_STANDARD,
                              coherence_delta=coh, world=world, rng=rng)


def attempt_dissolution(actor, target: dict, world=None, rng=None) -> OperationResult:
    """§2.4 Dissolution — Unable to Be. TN 7 (ED-IN-0196; PP-619's TN 8 is superseded). FR surcharge per PP-196."""
    scale = target.get('scale', 'Object')
    scale_cost = COHERENCE_COST_BY_SCALE.get(scale, 0)
    coh = scale_cost + FR_SURCHARGE
    return _resolve_operation("Dissolution", actor, DEPTH_OB.get(scale, 1), TN_STANDARD,
                              coherence_delta=coh, world=world, rng=rng)


def attempt_mending(actor, target: dict, world=None, rng=None, *,
                    environment_in_equilibrium: bool = False) -> OperationResult:
    """§2.4 Mending — Repairing the Substrate.

    Mending uses MENDING_OB (different scale than Depth Ob). Per ED-871
    (2026-05-31) + canon/02 Amendment 3: Mending is a RESTORATIVE operation
    type and costs 0 Coherence at every degree — operation type, not scale,
    determines Coherence risk. (Was -1, the pre-ED-871 value; the doc side was
    propagated to threadwork_v30 §3.2 + params/threadwork.md on 2026-07-07, and
    the sim is closed here.)

    THE RESTORATIVE FEEDBACK (plan position 27). C-1 (RULINGS.md Batch 9, 2026-09-08): restorative
    operations "do not merely cost nothing; they move the practitioner toward their own
    equilibrium" — and `canon/philosophy/06_operations.md` §6.8 "The restorative direction": Mending
    another "reliably moves the mender's present displacement — you recover faster for having done
    it". So a Mending that TOOK (any degree but Failure) hands the mender a restorative term, through
    `coherence.recover`'s `mending` parameter — E-1's "mending accelerates", which is that term's
    whole meaning. It is not re-implemented here: `recover` is the one owner of elastic return, of
    E-1's environment gate, and of "never past the resting point". ED-871's zero STRESS is untouched
    (`coherence_delta` stays 0); the feedback is a separate, opposite-signed event.
      - THE MAGNITUDE is the working's own type x scale term read backwards: the stress the same-
        scale manipulation would cost (`COHERENCE_COST_BY_SCALE`, negated). §6.8 grounds the
        direction ("the operational channel read backwards ... one channel, one imbrication,
        opposite relations to the equilibrium"); the REUSE of the §3.2 table as its size is this
        position's choice, as `opposing.py`'s and the P-25 term's reuse of it is theirs. A scale
        MENDING_OB does not price falls back to Relational for both the Ob and the term, so the two
        cannot disagree about which scale was worked.
      - FAILURE RETURNS NOTHING: the feedback is being joined to "a configuration that is being
        returned to the attractor" (§6.8), and a failed Mending returns nothing to it.
      - `environment_in_equilibrium` is E-1's CONDITION ("so long as you are in an environment where
        things are in equilibrium"), a fact about where the MENDER stands that only the caller can
        know. It defaults to False because the condition is a positive fact: unstated is not
        established, and a default of True would hand recovery to a mender standing in a Locked
        Zone — Mending's ordinary workplace. `recover` is still called, so the gate stays its.
    ⚠ NOT ROUTED HERE: Mending aimed at the mender's OWN configuration, which is what moves a resting
    point (`coherence.mend_resting_point`; §6.8's aim distinction, itself flagged derived). The
    target dict names no whose-configuration field to route on, and adding one is a design call.
    """
    scale = target.get('scale', 'Relational')
    priced = scale if scale in MENDING_OB else 'Relational'
    ob = MENDING_OB[priced]
    # ED-871: Mending Coherence cost = 0 (restorative-operation exception).
    coh = 0
    result = _resolve_operation("Mending", actor, ob, TN_STANDARD,
                                coherence_delta=coh, world=world, rng=rng)
    if result.degree != "Failure":
        restorative = -COHERENCE_COST_BY_SCALE[priced]
        prior = get_state(result.actor, world=world)
        elastic_before = prior.elastic_displacement if prior is not None else 0
        state = recover(result.actor, seasons=0,
                        environment_in_equilibrium=environment_in_equilibrium,
                        source=f"Mending {result.degree} at {priced}: restorative feedback",
                        mending=restorative, world=world)
        result.coherence_restored = elastic_before - state.elastic_displacement
    # Mending never produces Scars per conviction §3 Mending exception;
    # caller responsible for skipping Scar attribution
    return result
