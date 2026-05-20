"""
sim/thread/threadcut.py — Threadcut beings (P-06)

Canon source: designs/threadwork/threadwork_v30.md Part 6

Implements:
  - is_threadcut: registry check
  - resolve_threadcut_interaction: §6.2 observer-dependent rendering +
    §6.3 mechanical distinctions (no Coherence track, +1 Rendering Strain
    per external operation, Wounds cost sustained Thread work) + §6.4
    De-Actualisation trigger.

[ASSUMPTION: §6.1 Ontological Status canon body is empty in the doc —
 only the heading exists. §6.2-§6.4 mechanical body is implementable.
 Threadcut flag stored in module-level registry pending schema migration.]

[ASSUMPTION: Rendering Threshold = Health / 2 per §6.4 — but Health-vs-
 Wounds semantics depend on the actor's wound system. Caller supplies
 .wounds (count) and .max_wounds; Rendering Threshold = max_wounds / 2.]

Dependencies:
  - sim/thread/operations
  - sim/thread/coherence (NOT used — threadcut beings have no Coherence track per §6.3)

Entry points:
  - is_threadcut(being_id: str, world) -> bool
  - mark_threadcut(being_id: str, world) -> None
  - resolve_threadcut_interaction(actor, threadcut_target, op_type, world) -> dict
"""
from __future__ import annotations

from dataclasses import dataclass, field


# §6.2 Observer-dependent rendering bands
# [canonical: §6.2 — Observer Thread Sensitivity table]
PERCEPTION_BANDS = [
    (10, 'nothing or vague unease'),
    (30, 'a presence; unstable image; details shift'),
    (50, 'coherent figure but features approximate'),
    (70, 'stable perception; self-rendering visible as hum'),
    (101, 'full perception; self-rendering effort perceived'),
]

# §6.2 Rendering Beyond Observer Capacity
# [canonical: §6.2 — "Each scene of beyond-ceiling rendering: +1 Rendering Strain"]
RENDERING_STRAIN_PER_BEYOND_SCENE = 1

# §6.3 External operation cost
# [canonical: §6.3 — "each external Thread operation adds +1 Rendering Strain"]
RENDERING_STRAIN_PER_EXTERNAL_OP = 1

# §6.4 De-Actualisation Round 1/2 Ob penalties
# [canonical: §6.4 — Round 1 "All operations +2 Ob"; Round 2 "Operations +4 Ob"]
DEACTUALISATION_R1_OB = 2
DEACTUALISATION_R2_OB = 4


# Module-level threadcut registry: being_id → ThreadcutState
_threadcut_registry: dict = {}


def _store(world):
    """Threadcut store: world.threadcut_beings if world supplied,
    else module-level fallback."""
    if world is not None and hasattr(world, 'threadcut_beings'):
        return world.threadcut_beings
    return _threadcut_registry


@dataclass
class ThreadcutState:
    being_id: str
    rendering_strain: int = 0
    deactualisation_round: int = 0   # 0 = not started; 1/2/3 per §6.4
    notes: list[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {'being_id': self.being_id,
                'rendering_strain': self.rendering_strain,
                'deactualisation_round': self.deactualisation_round,
                'notes': list(self.notes)}

    @classmethod
    def from_dict(cls, d: dict) -> "ThreadcutState":
        return cls(being_id=d['being_id'],
                   rendering_strain=d.get('rendering_strain', 0),
                   deactualisation_round=d.get('deactualisation_round', 0),
                   notes=list(d.get('notes', [])))


def mark_threadcut(being_id: str, world=None) -> ThreadcutState:
    """Register a being as threadcut (P-06). Idempotent."""
    store = _store(world)
    if being_id not in store:
        store[being_id] = ThreadcutState(being_id=being_id)
    return store[being_id]


def is_threadcut(being_id: str, world=None) -> bool:
    """§Part 6 — is this being threadcut (continuous self-rendering, no Leap required)?"""
    return being_id in _store(world)


def perception_band(observer_ts: int) -> str:
    """§6.2 — Observer's perception of a threadcut being given their TS."""
    # [canonical: §6.2 perception table]
    for threshold, label in PERCEPTION_BANDS:
        if observer_ts < threshold:
            return label
    return 'full perception'


def resolve_threadcut_interaction(actor, threadcut_target_id: str,
                                  op_type: str,
                                  rendering_threshold: int = None,
                                  world=None) -> dict:
    """§6.3 — A threadcut being performs an external Thread operation OR
    an external practitioner targets a threadcut being.

    For the threadcut-as-actor case: caller passes the threadcut being as
    `actor` (must have being_id matching is_threadcut). Adds +1 Rendering
    Strain to its registry entry.

    For the practitioner-targeting-threadcut case: caller passes the
    practitioner as `actor` and threadcut_target_id as the target's id.
    No special Coherence routing needed.

    Returns dict with consequences: rendering_strain_after,
    deactualisation_triggered, notes.
    """
    actor_id = getattr(actor, 'actor_id', getattr(actor, 'name', 'unknown'))
    is_actor_threadcut = is_threadcut(actor_id, world=world)

    if not is_actor_threadcut and not is_threadcut(threadcut_target_id, world=world):
        return {
            'error': 'neither actor nor target is threadcut',
            'actor_id': actor_id,
            'target_id': threadcut_target_id,
        }

    consequences = {
        'actor_id': actor_id,
        'target_id': threadcut_target_id,
        'op_type': op_type,
        'rendering_strain_delta': 0,
        'rendering_strain_after': 0,
        'deactualisation_round': 0,
        'deactualisation_triggered': False,
        'notes': [],
    }

    if is_actor_threadcut:
        # §6.3 — external operation adds +1 Rendering Strain to the threadcut being
        state = _store(world)[actor_id]
        state.rendering_strain += RENDERING_STRAIN_PER_EXTERNAL_OP
        consequences['rendering_strain_delta'] = RENDERING_STRAIN_PER_EXTERNAL_OP
        consequences['rendering_strain_after'] = state.rendering_strain

        # §6.4 — De-Actualisation trigger: Rendering Strain == Health OR
        # Wounds reach Rendering Threshold (Health / 2)
        # rendering_threshold supplied by caller (typically max_wounds / 2)
        # If not supplied, fall back to attribute on actor
        if rendering_threshold is None:
            rendering_threshold = getattr(actor, 'max_wounds', 6) // 2
        # Use Health = max_wounds as proxy for canonical Health
        health = getattr(actor, 'max_wounds', 6)
        wounds = getattr(actor, 'wounds', 0)

        if state.rendering_strain >= health or wounds >= rendering_threshold:
            if state.deactualisation_round == 0:
                state.deactualisation_round = 1
                consequences['deactualisation_triggered'] = True
                consequences['notes'].append(
                    f'§6.4 De-Actualisation Round 1 triggered '
                    f'(rendering_strain={state.rendering_strain} health={health} '
                    f'wounds={wounds} threshold={rendering_threshold}); '
                    f'all operations +{DEACTUALISATION_R1_OB} Ob'
                )
            elif state.deactualisation_round < 3:
                state.deactualisation_round += 1
                consequences['notes'].append(
                    f'§6.4 De-Actualisation Round {state.deactualisation_round} '
                    f'progresses; ops +{DEACTUALISATION_R2_OB if state.deactualisation_round == 2 else "terminal"} Ob'
                )

        consequences['deactualisation_round'] = state.deactualisation_round

    # If practitioner is targeting threadcut (Mending interaction per P-17):
    # +Ob = threadcut's TS / 20 (round up), max +4 — see operations.py for
    # Mending-specific Ob adjustment when target is threadcut.
    # Not applied here; this function returns the state info, caller
    # invokes operations.attempt_mending with the adjusted Ob.

    return consequences


def reset_threadcut(world=None):
    """Test helper."""
    _store(world).clear()
