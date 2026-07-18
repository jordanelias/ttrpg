"""
sim/personal/conviction.py — Conviction Scar tracking + crisis detection

Canon source: designs/personal/conviction_track_v1.md §2-§3
(PP-718 per-Conviction Scar accumulation under PP-684 13-Conviction structured concentration)

Implements:
  §2 Scar Accumulation — per-Conviction (not aggregate) thresholds 0/1/2/3+,
     with crisis firing at 3+ Scars on any individual Conviction.
  §3 Thread Operation → Conviction Scar matrix (which Conviction gets Scarred
     for which witnessed Thread event).

Cyclic dependency with sim/personal/beliefs (§5.5 Belief revision triggered
by Conviction-engaging social wins). Both modules co-defined in single
commit per stub_infill_plan cyclic-pair protocol.

[ASSUMPTION: per-actor conviction state stored at module level — basis:
 World has no actor/practitioner conviction registry; pattern matches
 coherence.py's pre-schema-migration shape. _store(world) router pattern
 prepared for future schema migration.]

[ASSUMPTION: cycle resolution — beliefs.revise_belief calls into
 conviction.check_conviction_threshold for actor state; conviction.
 apply_conviction_scar references beliefs by string id, not by importing
 the Belief class. This breaks the literal import cycle while preserving
 the conceptual coupling per canon §2 row-2 "NPC enters arc transition
 state if X was the highest-weighted primary".]

Dependencies:
  - sim/personal/beliefs (string references only; no class import)

Entry points:
  - apply_conviction_scar(actor, source: str, magnitude: int, world=None) -> ScarRecord
  - check_conviction_threshold(actor, world=None) -> ConvictionState
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


# Canonical 13-Conviction set per PP-684 (taxonomy_v30); legacy 9-Conviction
# from conviction_track_v1 §1 superseded by taxonomy_v30 per file header.
# We list the canonical names used in §3 Thread Operation matrix.
# [canonical: conviction_track_v1 §1 + taxonomy_v30 §4 weights]
CONVICTIONS = (
    "Faith", "Order", "Reason", "Equity", "Precedent",
    "Autonomy", "Continuity", "Community", "Warden",
)

# §2 Per-Conviction Scar thresholds
# [canonical: §2 Per-Conviction Scar table]
SCAR_DESTABILISE = 1     # Scar 1: Conviction X destabilises
SCAR_SHIFT = 2           # Scar 2: weight may shift; Resonant Style activates
SCAR_CRISIS = 3          # Scar 3+: Conviction crisis on X

# §3 Conditions
# [canonical: §3 — "Season cap: Max 1 Scar per season from Thread witnessing per NPC"]
SCAR_SEASON_CAP_THREAD = 1

# §3 Truth scaling (the axis was renamed Certainty -> Truth per ED-IN-0075; the internal
#     identifier CERTAINTY_SCALING / the `certainty` param below are retained to avoid churning
#     frozen tests/sim callers, and denote the 0-5 Truth value)
# [canonical: §3 — "C5: +1 Scar severity. C0: -1 Scar severity. C2-3: standard."]
CERTAINTY_SCALING = {
    0: -1, 1: -1, 2: 0, 3: 0, 4: 0, 5: +1,
}


# Module-level actor state
# Key: actor_id (str); Value: ConvictionState
_conviction_state: dict[str, "ConvictionState"] = {}


def _store(world):
    """Return the conviction store: world.convictions if world supplied,
    else module-level fallback."""
    if world is not None and hasattr(world, 'convictions'):
        return world.convictions
    return _conviction_state


@dataclass
class ScarRecord:
    """Single Scar event on a named Conviction per §2."""
    actor: str
    conviction: str            # Which Conviction is Scarred
    source: str                # Free-text describing cause
    magnitude: int             # Effective Scar magnitude after Certainty scaling
    season: int                # When applied
    before: int                # Scar count on this Conviction before
    after: int                 # Scar count after

    def to_dict(self) -> dict:
        return {'actor': self.actor, 'conviction': self.conviction,
                'source': self.source, 'magnitude': self.magnitude,
                'season': self.season,
                'before': self.before, 'after': self.after}

    @classmethod
    def from_dict(cls, d: dict) -> "ScarRecord":
        return cls(actor=d['actor'], conviction=d['conviction'],
                   source=d['source'], magnitude=d['magnitude'],
                   season=d['season'],
                   before=d['before'], after=d['after'])


@dataclass
class ConvictionState:
    """Per-actor conviction-track state per §2."""
    actor: str
    # Per-Conviction Scar counts — keyed by Conviction name
    scars: dict[str, int] = field(default_factory=dict)
    # Resonant Style activations (one per Conviction once 2+ Scars)
    resonant_active: set[str] = field(default_factory=set)
    # Crisis state per Conviction (3+ Scars)
    in_crisis: set[str] = field(default_factory=set)
    # Belief revision opportunities (string ids of beliefs marked for revision)
    pending_belief_revisions: list[str] = field(default_factory=list)
    # Last-Scar-event season tracker per Conviction (for season cap enforcement)
    last_scar_season: dict[str, int] = field(default_factory=dict)
    # Log of all Scar events
    log: list[ScarRecord] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            'actor': self.actor,
            'scars': dict(self.scars),
            'resonant_active': sorted(self.resonant_active),
            'in_crisis': sorted(self.in_crisis),
            'pending_belief_revisions': list(self.pending_belief_revisions),
            'last_scar_season': dict(self.last_scar_season),
            'log': [r.to_dict() for r in self.log],
        }

    @classmethod
    def from_dict(cls, d: dict) -> "ConvictionState":
        return cls(
            actor=d['actor'],
            scars=dict(d.get('scars', {})),
            resonant_active=set(d.get('resonant_active', [])),
            in_crisis=set(d.get('in_crisis', [])),
            pending_belief_revisions=list(d.get('pending_belief_revisions', [])),
            last_scar_season=dict(d.get('last_scar_season', {})),
            log=[ScarRecord.from_dict(r) for r in d.get('log', [])],
        )


@dataclass
class ConvictionThresholdState:
    """Return value of check_conviction_threshold — summarises actor's state."""
    actor: str
    scar_counts: dict[str, int]
    destabilised: list[str]    # Convictions at 1 Scar
    shifted: list[str]         # Convictions at 2 Scars
    in_crisis: list[str]       # Convictions at 3+ Scars
    any_crisis: bool


def _get_or_create(actor: str, world=None) -> ConvictionState:
    store = _store(world)
    if actor not in store:
        store[actor] = ConvictionState(actor=actor)
    return store[actor]


def apply_conviction_scar(actor: str, source: str, magnitude: int,
                          conviction: Optional[str] = None,
                          certainty: int = 3,
                          season: int = 0,
                          world=None) -> ScarRecord:
    """Apply a Scar on a specific Conviction.

    conviction: which Conviction is Scarred. Required per PP-718 (per-
                Conviction not aggregate). Caller determines from §3 matrix
                given the witnessed Thread event.
    certainty: 0-5 cosmological Certainty Track value; modulates severity
               per §3 Certainty scaling.
    season: current world season for cap enforcement.
    magnitude: base Scar count (typically 1; the §3 matrix marks Scar/No-Scar).

    Returns the ScarRecord (which may report magnitude=0 if season cap
    suppressed the event).
    """
    if conviction is None:
        # Caller didn't pass a Conviction; treat as a no-op per PP-718
        # (Scars are per-Conviction not aggregate; we don't infer)
        return ScarRecord(actor=actor, conviction="(none)", source=source,
                          magnitude=0, season=season, before=0, after=0)

    if conviction not in CONVICTIONS:
        return ScarRecord(actor=actor, conviction=conviction, source=source,
                          magnitude=0, season=season, before=0, after=0)

    state = _get_or_create(actor, world)
    before = state.scars.get(conviction, 0)

    # Season cap per §3 for Thread-witnessing sources
    # [canonical: §3 — "Max 1 Scar per season from Thread witnessing per NPC"]
    is_thread_source = source.lower().startswith('thread') or 'witness' in source.lower()
    if is_thread_source:
        last_season = state.last_scar_season.get(conviction, -999)
        if season == last_season:
            # Already Scarred this season on this Conviction from Thread source
            return ScarRecord(actor=actor, conviction=conviction, source=source,
                              magnitude=0, season=season, before=before, after=before)

    # Apply Certainty scaling per §3
    scaling = CERTAINTY_SCALING.get(certainty, 0)
    effective_magnitude = max(0, magnitude + scaling)

    after = before + effective_magnitude
    state.scars[conviction] = after
    state.last_scar_season[conviction] = season

    # §2 thresholds
    if after >= SCAR_SHIFT and conviction not in state.resonant_active:
        state.resonant_active.add(conviction)
    if after >= SCAR_CRISIS and conviction not in state.in_crisis:
        state.in_crisis.add(conviction)

    record = ScarRecord(
        actor=actor, conviction=conviction, source=source,
        magnitude=effective_magnitude, season=season,
        before=before, after=after,
    )
    state.log.append(record)
    return record


def check_conviction_threshold(actor: str, world=None) -> ConvictionThresholdState:
    """Summarise actor's per-Conviction Scar state per §2 thresholds.

    Returns:
      destabilised: Convictions at exactly 1 Scar
      shifted: Convictions at 2 Scars
      in_crisis: Convictions at 3+ Scars
      any_crisis: True if any Conviction has 3+ Scars
    """
    state = _get_or_create(actor, world)
    destabilised = [c for c, s in state.scars.items() if s == SCAR_DESTABILISE]
    shifted = [c for c, s in state.scars.items() if s == SCAR_SHIFT]
    in_crisis = [c for c, s in state.scars.items() if s >= SCAR_CRISIS]
    return ConvictionThresholdState(
        actor=actor,
        scar_counts=dict(state.scars),
        destabilised=destabilised,
        shifted=shifted,
        in_crisis=in_crisis,
        any_crisis=bool(in_crisis),
    )


def mark_belief_revision_pending(actor: str, belief_id: str, world=None):
    """Called by beliefs.revise_belief when a Conviction-engaging Belief is
    flagged for revision per fieldwork §5.5 'Belief-challenging social
    success' or §9.5 narrative pressure. Stores belief_id by string only
    to avoid import cycle."""
    state = _get_or_create(actor, world)
    if belief_id not in state.pending_belief_revisions:
        state.pending_belief_revisions.append(belief_id)


def get_state(actor: str, world=None) -> Optional[ConvictionState]:
    return _store(world).get(actor)


def reset_all(world=None):
    """Test helper."""
    _store(world).clear()
