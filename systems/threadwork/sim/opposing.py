"""
systems/threadwork/sim/opposing.py — Opposing Thread operations + Knot Strain interaction

Canon source: systems/threadwork/threadwork_v30.md §2.6

Implements:
  - resolve_opposing_operations: §2.6 6-row resolution table (Meets/Partial/
    Failure × Meets/Partial/Failure) + Opposing Engagement Ob modifier +
    Knot Strain table.

§2.6 Opposing Engagement Modifier: each practitioner's Ob increased by
floor(opponent TPS / 2), minimum +1.

§2.6 Knot Strain: when a Knot partner participates in opposing ops, both
sides accrue strain on the Knot per the canon table.

[ASSUMPTION: op_a and op_b are pre-resolved OperationResults — basis:
 caller is expected to have already invoked operations.attempt_* with the
 opposing Ob modifier applied externally OR to call resolve_opposing_ops
 with raw actor objects + target. Both shapes supported via op_a being a
 dict with .actor + .op_type + .target, or an OperationResult-like obj.]

Dependencies:
  - systems/threadwork/sim/operations
  - sim/personal/knots (for Knot strain accumulation via late-import)

Entry points:
  - resolve_opposing_operations(actor_a, actor_b, op_type, target, world) -> OpposingResult
  - opposing_engagement_modifier(opponent_tps) -> int
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from engine.autoload.dice_engine import roll_pool
from systems.threadwork.sim.operations import (
    DEPTH_OB, MENDING_OB, TN_STANDARD, TN_BINDING, TN_POP,
    _actor_pool, COHERENCE_COST_BY_SCALE, FR_SURCHARGE, OperationResult,
)
from systems.threadwork.sim.coherence import apply_coherence_delta


# §2.6 Opposing Engagement Modifier
# [canonical: §2.6 — "each practitioner's Ob is increased by +floor(opponent's
#  Thread Pool Score ÷ 2), minimum +1"]
OPPOSING_OB_MODIFIER_MIN = 1

# §2.6 Knot Strain
# [canonical: §2.6 Knot Strain table — Standard losing/tied: +1 Ob next op
#  this scene, 2 Composure. FR losing/tied: +2 Ob, 4 Composure. FR + Diss
#  winner: +1 Wound to loser (no armour). Both meet Ob: both +1 Ob/2 Comp.]
KNOT_STRAIN_STANDARD_LOSER = 1
KNOT_STRAIN_FR_LOSER = 2
KNOT_COMPOSURE_STANDARD_LOSER = 2
KNOT_COMPOSURE_FR_LOSER = 4
KNOT_COMPOSURE_STANDARD_WINNER = 1
KNOT_COMPOSURE_FR_WINNER = 2
KNOT_DISSOLUTION_WOUND = 1


@dataclass
class OpposingResult:
    """§2.6 opposing operation resolution."""
    actor_a: str
    actor_b: str
    op_type: str
    a_net: int
    b_net: int
    a_degree: str                 # 'Meets' / 'Partial' / 'Failure'
    b_degree: str
    outcome: str                  # description of thread outcome
    ms_delta: int
    a_consequences: dict
    b_consequences: dict
    notes: list[str] = field(default_factory=list)


def opposing_engagement_modifier(opponent_tps: int) -> int:
    """§2.6 — Ob increase from opposing practitioner's TPS.

    Returns floor(opponent_tps / 2), minimum +1.
    """
    return max(OPPOSING_OB_MODIFIER_MIN, opponent_tps // 2)


def _degree_label(net: int, ob: int) -> str:
    """§2.6 uses 3-degree shorthand: Meets / Partial / Failure."""
    if net >= ob:
        return 'Meets'
    if net >= 1:
        return 'Partial'
    return 'Failure'


def resolve_opposing_operations(actor_a, actor_b, op_type: str, target: dict,
                                world=None, rng=None,
                                a_knot_id: Optional[str] = None,
                                b_knot_id: Optional[str] = None) -> OpposingResult:
    """§2.6 Resolve contested operation between two practitioners.

    actor_a / actor_b: practitioner objects (with .spirit, .ts, .history,
                     .actor_id).
    op_type: 'Weaving' / 'Pulling' / 'Locking' / 'Dissolution' / 'POP' / 'Mending'.
    target: dict with 'scale' and optional 'breadth'/'distance'/'recency'.
    a_knot_id / b_knot_id: optional Knot ids — if present, both parties
                            accrue strain to that Knot per §2.6.
    """
    actor_a_id = getattr(actor_a, 'actor_id', getattr(actor_a, 'name', 'A'))
    actor_b_id = getattr(actor_b, 'actor_id', getattr(actor_b, 'name', 'B'))

    # §2.6 Opposing Engagement Modifier
    a_tps = getattr(actor_a, 'ts', 30) // 10
    b_tps = getattr(actor_b, 'ts', 30) // 10
    a_ob_mod = opposing_engagement_modifier(b_tps)
    b_ob_mod = opposing_engagement_modifier(a_tps)

    scale = target.get('scale', 'Object')
    if op_type == 'Mending':
        base_ob = MENDING_OB.get(scale, MENDING_OB['Relational'])
        tn = TN_STANDARD
    elif op_type in ('Locking', 'Dissolution'):
        base_ob = DEPTH_OB.get(scale, 1)
        tn = TN_BINDING
    elif op_type == 'POP':
        base_ob = DEPTH_OB.get(scale, 1)
        tn = TN_POP
    else:
        base_ob = DEPTH_OB.get(scale, 1)
        tn = TN_STANDARD

    a_ob = base_ob + a_ob_mod
    b_ob = base_ob + b_ob_mod

    rng = rng if rng is not None else (world.rng if world is not None and hasattr(world, 'rng') else None)
    if rng is None:
        import random as _r
        rng = _r.Random()

    # Roll both pools
    a_pool = _actor_pool(actor_a)
    b_pool = _actor_pool(actor_b)
    a_roll = roll_pool(a_pool, tn=tn, rng=rng).net if a_pool > 0 else 0
    b_roll = roll_pool(b_pool, tn=tn, rng=rng).net if b_pool > 0 else 0

    a_deg = _degree_label(a_roll, a_ob)
    b_deg = _degree_label(b_roll, b_ob)

    # §2.6 Resolution Table
    # [canonical: §2.6 table — 6 rows × A degree × B degree]
    is_fr = op_type in ('Locking', 'Dissolution')

    if a_deg == 'Meets' and b_deg == 'Meets':
        outcome = "Shifting Object at target's scale (both meet Ob)"
        # MS = "Worst single degree-table Mending Stability cost + 1"
        # For Weaving Partial: -1. Worst we have between two Meets: degree-table is Success cost = 0 each
        # The canon says "worst single degree-table MS cost + 1" — minimum -1.
        ms_delta = -1
        a_cons = {'coherence_delta': COHERENCE_COST_BY_SCALE.get(scale, 0),
                  'composure': KNOT_COMPOSURE_FR_LOSER if is_fr else KNOT_COMPOSURE_STANDARD_LOSER,
                  'knot_ob_penalty': KNOT_STRAIN_FR_LOSER if is_fr else KNOT_STRAIN_STANDARD_LOSER}
        b_cons = dict(a_cons)
    elif a_deg == 'Meets' and b_deg == 'Partial':
        outcome = "A resolves (Overwhelming → Success; Success unchanged)"
        ms_delta = COHERENCE_COST_BY_SCALE.get(scale, 0)  # use scale cost as proxy; canon says "A's degree-table MS cost +1"
        ms_delta = ms_delta if ms_delta < 0 else -1
        a_cons = {'coherence_delta': COHERENCE_COST_BY_SCALE.get(scale, 0),
                  'composure': KNOT_COMPOSURE_STANDARD_WINNER}
        b_cons = {'coherence_delta': COHERENCE_COST_BY_SCALE.get(scale, 0) - 1,
                  'composure': KNOT_COMPOSURE_FR_LOSER if is_fr else KNOT_COMPOSURE_STANDARD_LOSER,
                  'knot_ob_penalty': KNOT_STRAIN_FR_LOSER if is_fr else KNOT_STRAIN_STANDARD_LOSER}
    elif a_deg == 'Meets' and b_deg == 'Failure':
        outcome = "A resolves at achieved degree (no contest)"
        ms_delta = COHERENCE_COST_BY_SCALE.get(scale, 0)
        ms_delta = ms_delta if ms_delta < 0 else 0
        a_cons = {'coherence_delta': COHERENCE_COST_BY_SCALE.get(scale, 0)}
        b_cons = {'coherence_delta': -1, 'composure': 0}  # standard Failure per degree table
    elif a_deg == 'Partial' and b_deg == 'Meets':
        # Symmetric to A=Meets, B=Partial
        outcome = "B resolves (Overwhelming → Success; Success unchanged)"
        ms_delta = COHERENCE_COST_BY_SCALE.get(scale, 0)
        ms_delta = ms_delta if ms_delta < 0 else -1
        b_cons = {'coherence_delta': COHERENCE_COST_BY_SCALE.get(scale, 0),
                  'composure': KNOT_COMPOSURE_STANDARD_WINNER}
        a_cons = {'coherence_delta': COHERENCE_COST_BY_SCALE.get(scale, 0) - 1,
                  'composure': KNOT_COMPOSURE_FR_LOSER if is_fr else KNOT_COMPOSURE_STANDARD_LOSER,
                  'knot_ob_penalty': KNOT_STRAIN_FR_LOSER if is_fr else KNOT_STRAIN_STANDARD_LOSER}
    elif a_deg == 'Partial' and b_deg == 'Partial':
        # Weak oscillation — d6 1-2 = Shifting Object one scale below, 3-6 = none
        shift_roll = rng.randint(1, 6)
        outcome = f"Weak oscillation; d6={shift_roll} → " + ("Shifting Object one scale below" if shift_roll <= 2 else "no effect")
        ms_delta = -1
        a_cons = {'coherence_delta': COHERENCE_COST_BY_SCALE.get(scale, 0) - 1,
                  'composure': KNOT_COMPOSURE_FR_LOSER if is_fr else KNOT_COMPOSURE_STANDARD_LOSER,
                  'knot_ob_penalty': KNOT_STRAIN_FR_LOSER if is_fr else KNOT_STRAIN_STANDARD_LOSER}
        b_cons = dict(a_cons)
    elif a_deg == 'Partial' and b_deg == 'Failure':
        outcome = "A's Partial resolves"
        ms_delta = COHERENCE_COST_BY_SCALE.get(scale, 0) - 1
        a_cons = {'coherence_delta': COHERENCE_COST_BY_SCALE.get(scale, 0) - 1, 'composure': 0}
        b_cons = {'coherence_delta': -1, 'composure': 0}
    elif a_deg == 'Failure' and b_deg == 'Meets':
        outcome = "B resolves at achieved degree (no contest)"
        ms_delta = COHERENCE_COST_BY_SCALE.get(scale, 0)
        ms_delta = ms_delta if ms_delta < 0 else 0
        b_cons = {'coherence_delta': COHERENCE_COST_BY_SCALE.get(scale, 0)}
        a_cons = {'coherence_delta': -1, 'composure': 0}
    elif a_deg == 'Failure' and b_deg == 'Partial':
        outcome = "B's Partial resolves"
        ms_delta = COHERENCE_COST_BY_SCALE.get(scale, 0) - 1
        b_cons = {'coherence_delta': COHERENCE_COST_BY_SCALE.get(scale, 0) - 1, 'composure': 0}
        a_cons = {'coherence_delta': -1, 'composure': 0}
    else:  # Failure + Failure
        outcome = "Nothing resolves"
        ms_delta = -1
        a_cons = {'coherence_delta': -1, 'composure': 1}
        b_cons = dict(a_cons)

    # Apply Coherence deltas
    if a_cons.get('coherence_delta', 0) != 0:
        apply_coherence_delta(actor_a_id, a_cons['coherence_delta'],
                              f"Opposing {op_type} A:{a_deg}/B:{b_deg}", world=world)
    if b_cons.get('coherence_delta', 0) != 0:
        apply_coherence_delta(actor_b_id, b_cons['coherence_delta'],
                              f"Opposing {op_type} A:{a_deg}/B:{b_deg}", world=world)

    # Apply MS delta
    if world is not None and 'MS' in world.clocks and ms_delta != 0:
        # [2026-05-20 migration] route through ms_track.apply_ms_delta — single
        # canonical surface for MS arithmetic per PP-255. Was: inline clamp.
        from sim.peninsular.ms_track import apply_ms_delta
        apply_ms_delta(ms_delta, source=f"opposing {op_type}", world=world)

    # Apply Knot strain if Knots specified
    notes = []
    if a_knot_id or b_knot_id:
        try:
            from sim.personal.knots import sustain_knot
            # FR + winner Dissolved: loser takes +1 Wound (handled by caller)
            knot_strain_delta = KNOT_STRAIN_FR_LOSER if is_fr else KNOT_STRAIN_STANDARD_LOSER
            if a_knot_id:
                sustain_knot(a_knot_id, strain_delta=knot_strain_delta,
                             source=f"opposing {op_type}", world=world)
            if b_knot_id and b_knot_id != a_knot_id:
                sustain_knot(b_knot_id, strain_delta=knot_strain_delta,
                             source=f"opposing {op_type}", world=world)
            notes.append(f"Knot strain +{knot_strain_delta} applied")
        except (ImportError, AttributeError):
            pass

    return OpposingResult(
        actor_a=actor_a_id, actor_b=actor_b_id, op_type=op_type,
        a_net=a_roll, b_net=b_roll,
        a_degree=a_deg, b_degree=b_deg,
        outcome=outcome, ms_delta=ms_delta,
        a_consequences=a_cons, b_consequences=b_cons,
        notes=notes,
    )
