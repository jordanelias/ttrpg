"""
sim/thread/collective.py — Collective Thread operations (multi-practitioner)

Canon source: designs/threadwork/threadwork_v30.md §2.5 Collective Operations

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
  - sim/thread/operations
  - sim/thread/coherence (apply_coherence_delta per-practitioner)

Entry points:
  - attempt_collective_operation(actors, op_type, target, world) -> CollectiveResult
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from sim.thread.operations import (
    attempt_weaving, attempt_pulling, attempt_locking, attempt_dissolution,
    attempt_mending, attempt_past_pulling, attempt_leap,
    DEPTH_OB, MENDING_OB, TN_STANDARD, TN_BINDING, TN_POP,
    _actor_pool, _resolve_operation, OperationResult,
)
from sim.autoload.dice_engine import roll_pool


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


def _helper_contribution(actor) -> int:
    """§2.5 — floor(Cognition / 2) bonus dice."""
    cog = getattr(actor, 'cognition', None)
    if cog is None:
        # Fallback to spirit if no cognition attribute (practitioner-only context)
        cog = getattr(actor, 'spirit', 3)
    return max(0, cog // 2)


def attempt_collective_operation(actors: list, op_type: str, target: dict,
                                 world=None, rng=None) -> CollectiveResult:
    """§2.5 — multi-practitioner operation.

    actors: list of practitioner objects; ranked by .ts descending,
            highest = Anchor, rest = Helpers.
    op_type: 'Weaving' / 'Pulling' / 'Locking' / 'Dissolution' / 'POP' /
             'Mending'.
    target: same shape as single-op target dict.
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

    # §2.5 — All practitioners Leap independently in same round
    leap_results = {}
    for a in [anchor] + helpers:
        leap_res = attempt_leap(a, target, world=world, rng=rng)
        actor_id = getattr(a, 'actor_id', getattr(a, 'name', 'unknown'))
        leap_results[actor_id] = leap_res.degree not in ("Failure",)

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
    scale = target.get('scale', 'Object')
    if op_type == 'Mending':
        ob = MENDING_OB.get(scale, MENDING_OB['Relational'])
        tn = TN_STANDARD
    elif op_type in ('Locking', 'Dissolution'):
        ob = DEPTH_OB.get(scale, 1)
        tn = TN_BINDING
    elif op_type == 'POP':
        ob = DEPTH_OB.get(scale, 1)
        tn = TN_POP
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

    if net >= ob + 3:
        degree = 'Overwhelming'
    elif net >= ob:
        degree = 'Success'
    elif net >= 1:
        degree = 'Partial'
    else:
        degree = 'Failure'

    # Apply Coherence cost to each successful Leap participant per §3.2 + §2.5
    # ("Co-Movement / Coherence fires per-practitioner per §3.2 — each
    # suspended their own layer 2")
    from sim.thread.coherence import apply_coherence_delta
    coh_delta = -1 if scale in ("Relational", "Field", "Territorial") else -2 if scale in ("Structural", "Foundational") else 0
    if degree in ("Partial", "Failure"):
        coh_delta -= 1

    for pid, ok in leap_results.items():
        if ok and coh_delta != 0:
            apply_coherence_delta(pid, coh_delta, f"Collective {op_type} {degree}", world=world)

    op_result = OperationResult(
        operation=f"Collective {op_type}",
        actor=anchor_id, degree=degree,
        net_successes=net, pool=total_pool, tn=tn, ob=ob,
        coherence_delta=coh_delta,
        mending_stability_delta=0,
        notes=[f"collective {len(actors)} actors; expected_pool={expected_pool} actual={total_pool}"
               + ("; lattice fractured (+1 Ob)" if lattice_fractured else "")],
    )

    return CollectiveResult(
        op_type=op_type, anchor=anchor_id, helpers=helper_ids,
        leap_results=leap_results, lattice_formed=True,
        lattice_fractured=lattice_fractured, operation_result=op_result,
    )
