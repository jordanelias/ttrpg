"""
sim/personal/beliefs.py — Belief tracking and revision

Canon source: systems/fieldwork/fieldwork_v30.md §5.5 Socializing and Beliefs;
              systems/social_contest/social_contest_v30.md §9.5 Beliefs Integration

Implements:
  - Belief-aligned social success: +1 Momentum (cap 4) per §5.5
  - Belief-challenging social success: marks belief for revision (no Momentum)
  - §9.5 contest Belief alignment: +1 Momentum on belief-aligned exchange win
  - Belief revision protocol: revise_belief produces a RevisionResult, may
    trigger Conviction state notification via mark_belief_revision_pending

Cyclic dependency with sim/personal/conviction (Scar accumulation can shift
underlying Conviction; Belief revision can be triggered by Conviction
crisis per Coherence Fractured band §3.3 row "Belief Co-Authorship begins").
Both modules co-defined in single commit per stub_infill_plan cyclic-pair
protocol. Cycle broken by string-id references (no class-level imports
between modules).

[ASSUMPTION: Belief storage at module level — basis: World has no actor
 belief registry. _store(world) router pattern prepared for future
 schema migration. Beliefs are owned per-actor (PC or NPC); each Belief
 has a string id used for both lookup and cross-module references.]

Dependencies:
  - sim/personal/conviction (string references only via mark_belief_revision_pending)

Entry points:
  - revise_belief(actor, belief_id, new_position, evidence, world) -> RevisionResult
  - get_active_beliefs(actor, world) -> list[Belief]
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional, Any


# Momentum cap per fieldwork_v30 §5.5
# [canonical: fieldwork_v30 §5.5 — "+1 Momentum (if below cap 4)"]
MOMENTUM_CAP = 4

# §9.5 cap on Belief-alignment momentum per contest
# [canonical: social_contest_v30 §9.5 — "Max 1 Momentum per contest from
#  Belief alignment"]
BELIEF_MOMENTUM_PER_CONTEST_CAP = 1


@dataclass
class Belief:
    """A single Belief held by an actor."""
    belief_id: str
    actor: str
    statement: str             # Free-text canonical statement
    position: str              # Current orientation ('strong' / 'wavering' / 'revised')
    underlying_convictions: list[str] = field(default_factory=list)  # Conviction names from taxonomy
    revision_pressure: int = 0  # Accumulated 'challenging' social wins; triggers revision opportunity
    history: list[dict] = field(default_factory=list)  # Revision events

    def to_dict(self) -> dict:
        # history entries may contain non-serializable 'evidence' fields;
        # coerce to string for storage safety
        safe_history = []
        for h in self.history:
            entry = {k: v for k, v in h.items() if k != 'evidence'}
            ev = h.get('evidence')
            entry['evidence'] = None if ev is None else (
                ev if isinstance(ev, (str, int, float, bool, list, dict)) else str(ev))
            safe_history.append(entry)
        return {
            'belief_id': self.belief_id, 'actor': self.actor,
            'statement': self.statement, 'position': self.position,
            'underlying_convictions': list(self.underlying_convictions),
            'revision_pressure': self.revision_pressure,
            'history': safe_history,
        }

    @classmethod
    def from_dict(cls, d: dict) -> "Belief":
        return cls(
            belief_id=d['belief_id'], actor=d['actor'],
            statement=d['statement'], position=d['position'],
            underlying_convictions=list(d.get('underlying_convictions', [])),
            revision_pressure=d.get('revision_pressure', 0),
            history=list(d.get('history', [])),
        )


@dataclass
class RevisionResult:
    actor: str
    belief_id: str
    accepted: bool             # True if revision applied
    old_position: str
    new_position: str
    momentum_delta: int        # +1 if aligned win, 0 if challenging or rejected
    notification_sent: bool    # True if conviction module was notified
    reason: str


# Module-level belief store keyed by actor → list[Belief]
_beliefs_by_actor: dict[str, list[Belief]] = {}


def _store(world):
    """Return the belief store: world.beliefs if world supplied,
    else module-level fallback."""
    if world is not None and hasattr(world, 'beliefs'):
        return world.beliefs
    return _beliefs_by_actor


def _find_belief(actor: str, belief_id: str, world=None) -> Optional[Belief]:
    store = _store(world)
    for b in store.get(actor, []):
        if b.belief_id == belief_id:
            return b
    return None


def add_belief(actor: str, belief_id: str, statement: str,
               position: str = 'strong',
               underlying_convictions: Optional[list] = None,
               world=None) -> Belief:
    """Add a new Belief to an actor's belief set. Used for scaffolding
    (character creation, scene setup). Returns the new Belief."""
    store = _store(world)
    if _find_belief(actor, belief_id, world):
        # Already exists — return existing
        return _find_belief(actor, belief_id, world)
    b = Belief(
        belief_id=belief_id, actor=actor, statement=statement,
        position=position,
        underlying_convictions=list(underlying_convictions or []),
    )
    store.setdefault(actor, []).append(b)
    return b


def revise_belief(actor: str, belief_id: str, new_position: str,
                  evidence: Any = None,
                  world=None) -> RevisionResult:
    """Revise a Belief in response to evidence / social pressure / Conviction shift.

    new_position: 'strong' / 'wavering' / 'revised'. Determines whether the
                  revision is a strengthening or weakening change.
    evidence: opaque object describing why (free-form; passed through to log).

    If the actor has a Conviction Scar related to the belief's underlying
    Convictions, this revision may notify the conviction module.
    """
    belief = _find_belief(actor, belief_id, world)
    if belief is None:
        return RevisionResult(
            actor=actor, belief_id=belief_id, accepted=False,
            old_position='', new_position=new_position,
            momentum_delta=0, notification_sent=False,
            reason=f"belief_id '{belief_id}' not found for actor '{actor}'",
        )

    old_position = belief.position
    belief.position = new_position
    belief.history.append({
        'old_position': old_position,
        'new_position': new_position,
        'evidence': evidence,
    })

    # Notify conviction module if revision involves Conviction-linked beliefs
    # [canonical: fieldwork §5.5 "creates narrative pressure to re-examine
    #  the Belief"; conviction_track §2 row 1 "Decision Forks increase
    #  when X is salient"]
    notified = False
    if belief.underlying_convictions:
        # Late-import to break the cycle at module-import time
        from systems.characters.sim.conviction import mark_belief_revision_pending
        mark_belief_revision_pending(actor, belief_id, world)
        notified = True

    return RevisionResult(
        actor=actor, belief_id=belief_id, accepted=True,
        old_position=old_position, new_position=new_position,
        momentum_delta=0,  # caller invokes social-success path separately
        notification_sent=notified,
        reason=f"revised: '{old_position}' -> '{new_position}'",
    )


def social_success(actor: str, belief_id: str, aligned: bool,
                   current_momentum: int = 0,
                   world=None) -> RevisionResult:
    """Apply §5.5 / §9.5 belief-aligned vs belief-challenging social win.

    aligned=True: belief-aligned win → +1 Momentum (up to cap 4)
    aligned=False: belief-challenging win → marks revision opportunity (no Momentum)

    current_momentum: caller's current momentum value; used for cap enforcement.
    Returns RevisionResult with momentum_delta and (for challenging case)
    notification_sent=True.
    """
    belief = _find_belief(actor, belief_id, world)
    if belief is None:
        return RevisionResult(
            actor=actor, belief_id=belief_id, accepted=False,
            old_position='', new_position='',
            momentum_delta=0, notification_sent=False,
            reason=f"belief_id '{belief_id}' not found",
        )

    if aligned:
        # [canonical: fieldwork §5.5 — "+1 Momentum (if below cap 4).
        #  Counts as Belief achievement per core engine."]
        delta = 1 if current_momentum < MOMENTUM_CAP else 0
        return RevisionResult(
            actor=actor, belief_id=belief_id, accepted=True,
            old_position=belief.position, new_position=belief.position,
            momentum_delta=delta, notification_sent=False,
            reason="§5.5 belief-aligned social success" + (" (Momentum capped)" if delta == 0 else ""),
        )

    # Challenging — mark revision pressure
    # [canonical: fieldwork §5.5 — "No Momentum, but the success creates
    #  narrative pressure to re-examine the Belief. GM marks as potential
    #  Belief revision opportunity."]
    belief.revision_pressure += 1
    # Notify conviction module
    from systems.characters.sim.conviction import mark_belief_revision_pending
    mark_belief_revision_pending(actor, belief_id, world)
    return RevisionResult(
        actor=actor, belief_id=belief_id, accepted=True,
        old_position=belief.position, new_position=belief.position,
        momentum_delta=0, notification_sent=True,
        reason="§5.5 belief-challenging success: revision opportunity marked",
    )


def get_active_beliefs(actor: str, world=None) -> list[Belief]:
    """Return the actor's active (non-revised) Beliefs."""
    store = _store(world)
    return [b for b in store.get(actor, []) if b.position != 'revised']


def reset_all(world=None):
    """Test helper."""
    _store(world).clear()
