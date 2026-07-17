"""
systems/threadwork/sim/operations.py — Thread operations: Leap, Weaving, Pulling, Past-Pulling, Locking, Dissolution, Mending

Canon source: systems/threadwork/threadwork_v30.md Part 2 (§2.3-§2.6)
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
  - systems/threadwork/sim/coherence (apply_coherence_delta)
  - sim/cross_scale/handoff_rules (TS-banded coherence cost for mass-battle context)

Entry points:
  - attempt_leap(actor, target_state, world) -> OperationResult
  - attempt_weaving(actor, target, world) -> OperationResult
  - attempt_pulling(actor, target, world) -> OperationResult
  - attempt_past_pulling(actor, target_moment, world) -> OperationResult
  - attempt_locking(actor, target, world) -> OperationResult
  - attempt_dissolution(actor, target, world) -> OperationResult
  - attempt_mending(actor, target, world) -> OperationResult
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional, Any

from engine.autoload.dice_engine import roll_pool
from systems.threadwork.sim.coherence import apply_coherence_delta


# §TN Modifiers (PP-619 — canonical)
# [canonical: params/threadwork.md §TN Modifiers]
TN_STANDARD = 7    # Weave, Pull, Mend, Leap, Community Weave
TN_BINDING = 8     # Lock, Dissolution
TN_POP = 8         # Past-Oriented Pulling
TN_POP_BINDING = 9  # POP Lock or Dissolution

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
    coherence_delta: int       # Applied to actor's coherence track
    mending_stability_delta: int = 0  # MS impact (clamped externally by ms_track)
    notes: list[str] = field(default_factory=list)


def _compute_degree(net_successes: int, ob: int) -> str:
    """Map net_successes vs Ob to a degree label per standard dice-engine semantics."""
    if net_successes <= 0:
        return "Failure"
    if net_successes < ob:
        return "Partial"
    if net_successes >= ob + 3:
        return "Overwhelming"
    return "Success"


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
                       rng=None) -> OperationResult:
    """Shared resolution path for all Thread operations.

    Rolls actor's pool, computes degree, applies Coherence delta.
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

    # Mending Stability impact per §2.4 tables (degree-driven for non-Mending ops)
    ms_delta = 0
    if operation == "Weaving":
        if degree == "Partial":
            ms_delta = -1
        elif degree == "Failure":
            ms_delta = -2
    elif operation == "Pulling":
        if degree == "Partial":
            ms_delta = -1
        elif degree == "Failure":
            ms_delta = -2
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
                              coherence_delta=coh, world=world, rng=rng)


def attempt_pulling(actor, target: dict, world=None, rng=None) -> OperationResult:
    """§2.4 Pulling — Things Open."""
    scale = target.get('scale', 'Object')
    ob = DEPTH_OB.get(scale, 1)
    coh = COHERENCE_COST_BY_SCALE.get(scale, 0)
    return _resolve_operation("Pulling", actor, ob, TN_STANDARD,
                              coherence_delta=coh, world=world, rng=rng)


def attempt_past_pulling(actor, target_moment: dict, world=None, rng=None) -> OperationResult:
    """§2.4 Past-Oriented Pulling. TN 8.

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
    return _resolve_operation("Past-Oriented Pulling", actor, ob, TN_POP,
                              coherence_delta=coh, world=world, rng=rng)


def attempt_locking(actor, target: dict, world=None, rng=None) -> OperationResult:
    """§2.4 Locking — Unable to Become. TN 8. FR surcharge per PP-196.

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
    return _resolve_operation("Locking", actor, DEPTH_OB.get(scale, 1), TN_BINDING,
                              coherence_delta=coh, world=world, rng=rng)


def attempt_dissolution(actor, target: dict, world=None, rng=None) -> OperationResult:
    """§2.4 Dissolution — Unable to Be. TN 8. FR surcharge per PP-196."""
    scale = target.get('scale', 'Object')
    scale_cost = COHERENCE_COST_BY_SCALE.get(scale, 0)
    coh = scale_cost + FR_SURCHARGE
    return _resolve_operation("Dissolution", actor, DEPTH_OB.get(scale, 1), TN_BINDING,
                              coherence_delta=coh, world=world, rng=rng)


def attempt_mending(actor, target: dict, world=None, rng=None) -> OperationResult:
    """§2.4 Mending — Repairing the Substrate.

    Mending uses MENDING_OB (different scale than Depth Ob). Per ED-871
    (2026-05-31) + canon/02 Amendment 3: Mending is a RESTORATIVE operation
    type and costs 0 Coherence at every degree — operation type, not scale,
    determines Coherence risk. (Was -1, the pre-ED-871 value; the doc side was
    propagated to threadwork_v30 §3.2 + params/threadwork.md on 2026-07-07, and
    the sim is closed here.)
    """
    scale = target.get('scale', 'Relational')
    ob = MENDING_OB.get(scale, MENDING_OB['Relational'])
    # ED-871: Mending Coherence cost = 0 (restorative-operation exception).
    coh = 0
    result = _resolve_operation("Mending", actor, ob, TN_STANDARD,
                                coherence_delta=coh, world=world, rng=rng)
    # Mending never produces Scars per conviction §3 Mending exception;
    # caller responsible for skipping Scar attribution
    return result
