"""
sim/thread/coherence.py — Coherence 10-0 track per Foundations P-10, P-15

Canon source: designs/threadwork/threadwork_v30.md Part 3; canon/02_canon_constraints.md §A P-10 / P-15

Implements the per-practitioner Coherence track per §3.1-§3.6:
  - 10 -> 0 integer track, starting 10 (§3.1)
  - Deltas from operations / FR / Residue / Resonance / Flashback / proximity (§3.2)
  - Threshold bands trigger fallout / penalty states (§3.3)
  - Recovery via non-practice / Anchoring Scene / Einhir technique (§3.5)
  - Rendering Crisis at 0 (§3.3 row 0 / §3.7 PROVISIONAL)

[ASSUMPTION: practitioner registry stored at module level rather than on
 game_state.World — basis: World currently has no practitioner/knot schema;
 modifying World is a separate commit out of Tier 0 scope. Module exposes
 get_state(actor) for inspection and apply/check functions for mutation.
 When World gains a practitioner registry, this module's state-store moves
 onto World; the entry-point signatures stay.]

Dependencies:
  - sim/autoload/game_state

Entry points:
  - apply_coherence_delta(actor: str, delta: int, source: str, world: GameState) -> CoherenceState
  - check_coherence_zero_transition(actor: str, world: GameState) -> ZeroTransitionResult
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


# Coherence track bounds per §3.1
# [canonical: designs/threadwork/threadwork_v30.md §3.1 — "Range: 10 (fully
#  coherent) -> 0 (rendering crisis). Starting value: 10 (all practitioners)."]
COHERENCE_MAX = 10
COHERENCE_MIN = 0
COHERENCE_START = 10

# §3.3 threshold band boundaries — inclusive low ends
# [canonical: §3.3 Coherence Thresholds]
COHERENCE_STABLE_LOW = 8       # 10-8 = Stable
COHERENCE_DISSONANT_LOW = 5    # 7-5 = Dissonant
COHERENCE_FRAGMENTED_LOW = 3   # 4-3 = Fragmented
COHERENCE_FRACTURED = 2        # 2 = Fractured
COHERENCE_SEVERED = 1          # 1 = Severed
COHERENCE_CRISIS = 0           # 0 = Rendering Crisis

# Module-level practitioner state store
# Key: actor id (str); Value: CoherenceState
_practitioner_state: dict[str, "CoherenceState"] = {}


@dataclass
class CoherenceLogEntry:
    """Single delta application — used for audit trail per §3.6 fallout rolls."""
    delta: int
    source: str
    before: int
    after: int


@dataclass
class CoherenceState:
    """Per-practitioner coherence track state per §3.1."""
    actor: str
    coherence: int = COHERENCE_START
    band: str = "Stable"
    log: list[CoherenceLogEntry] = field(default_factory=list)
    crisis_active: bool = False


@dataclass
class ZeroTransitionResult:
    """Result of checking for Rendering Crisis transition per §3.3 row 0 / §3.7."""
    actor: str
    crisis: bool                    # True if currently at 0
    just_transitioned: bool         # True iff this check is the moment of entry
    band: str
    coherence: int


def _band_for(c: int) -> str:
    """Map coherence integer to §3.3 band label."""
    # [canonical: §3.3 Coherence Thresholds — band labels]
    if c >= COHERENCE_STABLE_LOW:
        return "Stable"
    if c >= COHERENCE_DISSONANT_LOW:
        return "Dissonant"
    if c >= COHERENCE_FRAGMENTED_LOW:
        return "Fragmented"
    if c == COHERENCE_FRACTURED:
        return "Fractured"
    if c == COHERENCE_SEVERED:
        return "Severed"
    return "Rendering Crisis"


def _get_or_create(actor: str) -> CoherenceState:
    """Initialise a practitioner's track at the §3.1 starting value if first seen."""
    if actor not in _practitioner_state:
        _practitioner_state[actor] = CoherenceState(actor=actor, coherence=COHERENCE_START, band="Stable")
    return _practitioner_state[actor]


def apply_coherence_delta(actor: str, delta: int, source: str, world=None) -> CoherenceState:
    """Apply a Coherence change per §3.2 / §3.5.

    delta: signed int. Negative = reduction (operation, FR, residue, etc).
           Positive = recovery (non-practice season, Anchoring Scene, Einhir).
    source: free-text describing the cause for log purposes (e.g.
            "Weave Relational", "FR Lock Territorial", "Anchoring Scene").
    world: GameState — currently unused (state is module-level); preserved in
           signature for forward compatibility when state moves onto World.

    Returns the updated CoherenceState.
    """
    state = _get_or_create(actor)
    before = state.coherence
    # Clamp to [0, 10] per §3.5 "Cannot exceed 10" and §3.1 "0 (rendering crisis)" floor
    # [canonical: §3.5 "Cannot exceed 10" + §3.1 range 10->0]
    new_value = max(COHERENCE_MIN, min(COHERENCE_MAX, before + delta))
    state.coherence = new_value
    state.band = _band_for(new_value)
    state.log.append(CoherenceLogEntry(delta=delta, source=source, before=before, after=new_value))
    return state


def check_coherence_zero_transition(actor: str, world=None) -> ZeroTransitionResult:
    """Check whether actor has just entered or is currently in Rendering Crisis.

    Per §3.3 row 0 / §3.7: at Coherence 0, the practitioner enters Rendering
    Crisis (campaign event). This function marks crisis_active=True the first
    time it observes coherence==0, and reports just_transitioned=True only
    for that first observation.
    """
    state = _get_or_create(actor)
    crisis_now = (state.coherence == COHERENCE_CRISIS)
    just_transitioned = crisis_now and not state.crisis_active
    if crisis_now:
        state.crisis_active = True
    elif state.coherence > COHERENCE_CRISIS:
        # Per §3.7: crisis resolves when coherence rises again
        state.crisis_active = False
    return ZeroTransitionResult(
        actor=actor,
        crisis=crisis_now,
        just_transitioned=just_transitioned,
        band=state.band,
        coherence=state.coherence,
    )


def get_state(actor: str) -> Optional[CoherenceState]:
    """Inspection helper — returns the practitioner's current state, or None
    if the practitioner has never had a coherence delta applied."""
    return _practitioner_state.get(actor)


def reset_all():
    """Test helper — clear the module-level store. Not for production use."""
    _practitioner_state.clear()
