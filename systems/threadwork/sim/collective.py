"""
systems/threadwork/sim/collective.py — Collective Thread operations (multi-practitioner)

Canon source: systems/threadwork/reference/threadwork_v30.md §2.5 Collective Operations

Implements:
  - attempt_collective_operation: §2.5 procedure. All practitioners Leap
    independently in same round (Priority 5). Anchor = highest-TS practitioner;
    Helpers contribute floor(Cognition / 2) bonus dice. Lattice fractures
    if helper Leap drops total below half Anchor's solo pool.

[ASSUMPTION: Cognition attribute optional on actor object — basis: canon
 §2.5 says "Each assisting practitioner contributes floor(Cognition / 2)".
 Cognition is per faction_canon §5.1 7-stat lineup. Actor objects expose
 .cognition when set; default to .spirit for practitioner-only contexts.]

Dependencies:
  - systems/threadwork/sim/operations
  - systems/threadwork/sim/operations.charge_working (resist + apply per-practitioner)

Entry points:
  - attempt_collective_operation(actors, op_type, target, world) -> CollectiveResult
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from systems.threadwork.sim.operations import (
    attempt_leap,
    COHERENCE_COST_BY_SCALE, DEPTH_OB, MENDING_OB, TN_STANDARD,
    _actor_pool, OperationResult,
    aims_at_own_configuration, apply_mending_feedback, charge_working, mending_priced_scale,
    price_mending,
)
from engine.dice_engine import dice_engine
from engine.dice_engine.dice_engine import roll_pool


# §2.5 lattice fracture threshold
# [canonical: §2.5 — "if remaining pool drops below half the Anchor's solo
#  pool, apply +1 Ob (lattice fracture)"]
LATTICE_FRACTURE_OB_PENALTY = 1


@dataclass
class CollectiveResult:
    """§2.5 collective operation result."""
    op_type: str
    anchor: str                    # actor_id of the Anchor
    helpers: list                  # list of helper actor_ids
    leap_results: dict             # actor_id → bool (success/fail)
    lattice_formed: bool
    lattice_fractured: bool        # +1 Ob penalty applied
    operation_result: Optional[OperationResult]
    notes: list[str] = field(default_factory=list)
    # Mending only (WR-03): actor_id -> elastic displacement the restorative term actually returned
    # to that participant (`operations.apply_mending_feedback`). Empty for every other op_type.
    coherence_restored: dict = field(default_factory=dict)


def _helper_contribution(actor) -> int:
    """§2.5 — floor(Cognition / 2) bonus dice."""
    cog = getattr(actor, 'cognition', None)
    if cog is None:
        # Fallback to spirit if no cognition attribute (practitioner-only context)
        cog = getattr(actor, 'spirit', 3)
    return max(0, cog // 2)


def attempt_collective_operation(actors: list, op_type: str, target: dict,
                                 world=None, rng=None, *,
                                 environment_in_equilibrium: bool = False) -> CollectiveResult:
    """§2.5 — multi-practitioner operation.

    actors: list of practitioner objects; ranked by .ts descending,
            highest = Anchor, rest = Helpers.
    op_type: 'Weaving' / 'Pulling' / 'Locking' / 'Dissolution' / 'POP' /
             'Mending'.
    target: same shape as single-op target dict.
    environment_in_equilibrium: E-1's condition on the restorative term a Mending hands each
             participant; a fact about where they stand that only the caller knows. Defaults to
             False (unstated is not established), as `operations.attempt_mending` does.

    COHERENCE (R-14, WR-03). Every participant whose Leap succeeded pays the working's cost, each
    resisted by their OWN resilience through `operations.charge_working` (identity at the
    shipped gain 0); the reported `coherence_delta` is the Anchor's. A Mending is priced by
    `operations.price_mending` on `operations.mending_priced_scale(target)` — 0 cost at every degree
    (ED-871), the owner's Mending Stability delta, and the restorative term handed to every such
    participant through `operations.apply_mending_feedback` — as a single Mending aimed at ANOTHER's
    configuration is. Own-configuration aim (`target['configuration_of']`, WR-02) is routed by
    `operations.attempt_mending` ONLY: here it is refused with a ValueError, not silently given the
    elastic path.
    """
    if not actors:
        return CollectiveResult(op_type=op_type, anchor='', helpers=[],
                                leap_results={}, lattice_formed=False,
                                lattice_fractured=False, operation_result=None,
                                notes=['no actors provided'])

    # Rank by TS descending — Anchor first
    ranked = sorted(actors, key=lambda a: getattr(a, 'ts', 0), reverse=True)
    anchor = ranked[0]
    helpers = ranked[1:]
    anchor_id = getattr(anchor, 'actor_id', getattr(anchor, 'name', 'anchor'))
    helper_ids = [getattr(h, 'actor_id', getattr(h, 'name', f'helper{i}'))
                  for i, h in enumerate(helpers)]
    if op_type == 'Mending' and any(aims_at_own_configuration(target, pid) for pid in [anchor_id] + helper_ids):
        raise ValueError("attempt_collective_operation: Mending aimed at a participant's OWN configuration "
                         "(target['configuration_of']) is routed by operations.attempt_mending only")

    # §2.5 — All practitioners Leap independently in same round
    leap_results = {}
    participants = {}              # actor_id -> actor, keyed exactly as leap_results is
    for a in [anchor] + helpers:
        leap_res = attempt_leap(a, target, world=world, rng=rng)
        actor_id = getattr(a, 'actor_id', getattr(a, 'name', 'unknown'))
        leap_results[actor_id] = leap_res.degree not in ("Failure",)
        participants[actor_id] = a

    # §2.5 — If the Anchor fails: collective lattice does not form
    if not leap_results.get(anchor_id, False):
        return CollectiveResult(
            op_type=op_type, anchor=anchor_id, helpers=helper_ids,
            leap_results=leap_results, lattice_formed=False,
            lattice_fractured=False, operation_result=None,
            notes=['Anchor Leap failed — no collective lattice (§2.5)']
        )

    # §2.5 — If the Anchor succeeds but helpers fail: subtract their
    # contributed dice; if remaining pool drops below half the Anchor's
    # solo pool, apply +1 Ob (lattice fracture)
    anchor_solo_pool = _actor_pool(anchor)
    helper_contributions = sum(
        _helper_contribution(h) for h, hid in zip(helpers, helper_ids)
        if leap_results.get(hid, False)
    )
    total_pool = anchor_solo_pool + helper_contributions

    lattice_fractured = total_pool < (anchor_solo_pool // 2 + anchor_solo_pool)
    # Wait — re-read canon: "if remaining pool drops below half the Anchor's solo pool"
    # That means total_pool < anchor_solo_pool / 2 is the fracture condition
    # The total_pool starts at anchor_solo_pool + helper_contributions and
    # only loses helper contributions when helpers fail. So "remaining pool"
    # = anchor_solo_pool + (succeeded helpers' contributions). If all helpers
    # failed: total = anchor_solo_pool alone → still ≥ half. So fracture
    # only triggers if somehow the calculation is anchor-relative. Re-checking:
    # The "remaining pool" phrase refers to AFTER subtracting failed-helper
    # dice, but the Anchor's solo pool is never subtracted. So fracture
    # would only happen if the formula counted helper contributions as
    # NEGATIVE when failed. That doesn't match the canon language.
    # Cleaner read: fracture = total ops pool < half(anchor_solo). Since
    # anchor_solo ≤ total, this never fires unless something else reduces.
    # The actual semantic is: helpers committed dice expecting them to add;
    # if they fail, those dice are subtracted from the EXPECTED total pool
    # the Anchor was relying on. Expected = solo + sum(all helper contribs).
    # Remaining after failures = solo + sum(successful helper contribs).
    # Fracture: remaining < expected / 2.
    expected_pool = anchor_solo_pool + sum(_helper_contribution(h) for h in helpers)
    lattice_fractured = total_pool < (expected_pool / 2)

    # Resolve the operation with the pooled dice
    # Map op_type to depth-Ob lookup
    is_mending = op_type == 'Mending'
    # A Mending works the owner's priced scale (WR-03), so its Ob and its price read one answer.
    scale = mending_priced_scale(target) if is_mending else target.get('scale', 'Object')
    # TN7 always (ED-IN-0196) — the op_type only selects the Ob now.
    if is_mending:
        ob = MENDING_OB[scale]
    else:
        ob = DEPTH_OB.get(scale, 1)
    tn = TN_STANDARD

    if lattice_fractured:
        ob += LATTICE_FRACTURE_OB_PENALTY

    rng = rng if rng is not None else (world.rng if world is not None and hasattr(world, 'rng') else None)
    if rng is None:
        import random as _r
        rng = _r.Random()

    # Anchor's operation uses pooled dice
    roll = roll_pool(total_pool, tn=tn, rng=rng)
    net = roll.net

    degree = dice_engine.degree_label(net, ob)  # owner's ladder (Jordan ruling 2026-08-14)

    # Apply Coherence cost to each successful Leap participant per §3.2 + §2.5
    # ("Co-Movement / Coherence fires per-practitioner per §3.2 — each
    # suspended their own layer 2")
    if is_mending:
        price = price_mending(scale, degree)
        coh_delta = price.coherence_cost
        ms_delta = price.mending_stability_delta
    else:
        coh_delta = COHERENCE_COST_BY_SCALE.get(scale, 0)
        if degree in ("Partial", "Failure"):
            coh_delta -= 1
        ms_delta = 0

    applied = {}                   # actor_id -> the cost that participant actually took (R-14)
    restored = {}
    for pid, ok in leap_results.items():
        if not ok:
            continue
        applied[pid] = charge_working(participants[pid], pid, coh_delta,
                                      f"Collective {op_type} {degree}", world=world)
        if is_mending:
            restored[pid] = apply_mending_feedback(
                pid, price, environment_in_equilibrium=environment_in_equilibrium,
                source=f"Collective Mending {degree} at {scale}: restorative feedback", world=world)

    op_result = OperationResult(
        operation=f"Collective {op_type}",
        actor=anchor_id, degree=degree,
        net_successes=net, pool=total_pool, tn=tn, ob=ob,
        coherence_delta=applied[anchor_id],
        mending_stability_delta=ms_delta,
        coherence_restored=restored.get(anchor_id, 0),
        notes=[f"collective {len(actors)} actors; expected_pool={expected_pool} actual={total_pool}"
               + ("; lattice fractured (+1 Ob)" if lattice_fractured else "")],
    )

    return CollectiveResult(
        op_type=op_type, anchor=anchor_id, helpers=helper_ids,
        leap_results=leap_results, lattice_formed=True,
        lattice_fractured=lattice_fractured, operation_result=op_result,
        coherence_restored=restored,
    )
