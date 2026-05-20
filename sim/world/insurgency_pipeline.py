"""
sim/world/insurgency_pipeline.py — Revolt → Insurgency → Faction emergence pipeline (GD-3)

Canon source: canon/02_canon_constraints.md §B GD-3

PARTIAL IMPLEMENTATION:
  - check_insurgency_triggers: implemented against GD-3 (a)-(b) — detects
    2+ contiguous Uncontrolled territories sustained 2 consecutive seasons.
  - check_insurgency_promotion: implemented against GD-3 (c)-(e) — promotes
    at L≥3, 2+ territories, Accord≥4 averaged, sustained 2 seasons; PT<3
    average → RM variant (extra-parliamentary); PT≥3 → parliamentary candidate.

[ASSUMPTION: insurgency registry on World — basis: insurgencies are
 world-level emergent entities. game_state.World has no insurgencies field.
 Stored at module level keyed by world_token + insurgency_id, with
 reset_for_world helper. Schema migration to World pending.]

[CANON-GATED]: designs/world/insurgency_pipeline_v30.md cited but not yet
authored (Pass 2i pending). This module implements GD-3's mechanical
constraints; richer behavior (specific Conviction generation per emergence,
NPC seeding for new faction's leadership) awaits Pass 2i.

Dependencies:
  - sim/autoload/game_state
  - sim/territory/adjacency

Entry points:
  - check_insurgency_triggers(world: GameState) -> list[InsurgencyEvent]
  - check_insurgency_promotion(insurgency_id: str, world: GameState) -> PromotionResult
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


# GD-3 trigger thresholds
# [canonical: canon/02_canon_constraints.md §B GD-3]
INSURGENCY_TRIGGER_MIN_TERRITORIES = 2
INSURGENCY_TRIGGER_SUSTAINED_SEASONS = 2
INSURGENCY_STARTING_L = 1.0

# GD-3 promotion thresholds
INSURGENCY_PROMOTE_MIN_L = 3
INSURGENCY_PROMOTE_MIN_TERRITORIES = 2
INSURGENCY_PROMOTE_MIN_ACCORD = 4
INSURGENCY_PROMOTE_SUSTAINED_SEASONS = 2
INSURGENCY_RM_PT_THRESHOLD = 3  # PT < 3 → RM variant; PT >= 3 → parliamentary

# Module-level insurgency state — fallback when world is None
# Post-2026-05-19 schema migration: when world is supplied, state lives on
# world.insurgencies and world.uncontrolled_streaks.
_insurgencies: dict[str, "InsurgencyRecord"] = {}
_uncontrolled_streaks: dict[frozenset, int] = {}  # contiguous-group → consecutive seasons


def _ins_store(world):
    if world is not None and hasattr(world, 'insurgencies'):
        return world.insurgencies
    return _insurgencies


def _streak_store(world):
    if world is not None and hasattr(world, 'uncontrolled_streaks'):
        return world.uncontrolled_streaks
    return _uncontrolled_streaks


@dataclass
class InsurgencyRecord:
    insurgency_id: str
    territory_ids: list[str]
    L: float = INSURGENCY_STARTING_L
    formed_season: int = 0
    promoted: bool = False
    parliamentary_status: Optional[str] = None  # 'parliamentary' / 'extra-parliamentary' / None

    def to_dict(self) -> dict:
        return {'insurgency_id': self.insurgency_id,
                'territory_ids': list(self.territory_ids),
                'L': self.L, 'formed_season': self.formed_season,
                'promoted': self.promoted,
                'parliamentary_status': self.parliamentary_status}

    @classmethod
    def from_dict(cls, d: dict) -> "InsurgencyRecord":
        return cls(insurgency_id=d['insurgency_id'],
                   territory_ids=list(d['territory_ids']),
                   L=d.get('L', INSURGENCY_STARTING_L),
                   formed_season=d.get('formed_season', 0),
                   promoted=d.get('promoted', False),
                   parliamentary_status=d.get('parliamentary_status'))


@dataclass
class InsurgencyEvent:
    event_type: str          # 'formation' / 'streak_extended'
    territory_ids: list[str]
    season: int


@dataclass
class PromotionResult:
    promoted: bool
    insurgency_id: str
    new_status: Optional[str]   # 'parliamentary' / 'extra-parliamentary' (RM variant)
    reason: str


def _contiguous_uncontrolled_groups(world) -> list[list[str]]:
    """Find groups of adjacent territories all in Uncontrolled state.

    Uses sim/territory/adjacency for neighbor lookup. Returns list of
    territory-id lists, one per connected component of Uncontrolled.
    """
    from sim.territory.adjacency import ADJACENCY
    uncontrolled = [tid for tid, t in world.territories.items() if t.is_uncontrolled()]
    visited = set()
    groups = []
    for tid in uncontrolled:
        if tid in visited:
            continue
        # BFS from tid
        group = []
        queue = [tid]
        while queue:
            cur = queue.pop(0)
            if cur in visited:
                continue
            visited.add(cur)
            group.append(cur)
            for other in uncontrolled:
                if other not in visited and other in ADJACENCY.get(cur, set()):
                    queue.append(other)
        groups.append(group)
    return groups


def check_insurgency_triggers(world) -> list[InsurgencyEvent]:
    """Check GD-3 (a)-(b) Insurgency formation triggers.

    Detects groups of 2+ contiguous Uncontrolled territories. Tracks
    consecutive-season streaks; when a group sustains 2+ seasons, fires
    an Insurgency formation event.
    """
    events = []
    groups = _contiguous_uncontrolled_groups(world)
    insurgencies = _ins_store(world)
    streaks = _streak_store(world)

    # Update streaks
    seen_now = set()
    for g in groups:
        if len(g) < INSURGENCY_TRIGGER_MIN_TERRITORIES:
            continue
        key = frozenset(g)
        seen_now.add(key)
        streaks[key] = streaks.get(key, 0) + 1

        if streaks[key] >= INSURGENCY_TRIGGER_SUSTAINED_SEASONS:
            # Check if already-formed insurgency exists for this group
            existing = any(
                set(rec.territory_ids) == set(g) and not rec.promoted
                for rec in insurgencies.values()
            )
            if not existing:
                ins_id = f"INS-{world.season:04d}-{len(insurgencies)+1:03d}"
                insurgencies[ins_id] = InsurgencyRecord(
                    insurgency_id=ins_id,
                    territory_ids=list(g),
                    formed_season=world.season,
                )
                events.append(InsurgencyEvent(
                    event_type='formation',
                    territory_ids=list(g),
                    season=world.season,
                ))
            else:
                events.append(InsurgencyEvent(
                    event_type='streak_extended',
                    territory_ids=list(g),
                    season=world.season,
                ))
        else:
            events.append(InsurgencyEvent(
                event_type='streak_extended',
                territory_ids=list(g),
                season=world.season,
            ))

    # Reset streaks for groups that broke up
    for key in list(streaks.keys()):
        if key not in seen_now:
            del streaks[key]

    return events


def check_insurgency_promotion(insurgency_id: str, world) -> PromotionResult:
    """Check GD-3 (c)-(e) Insurgency → Faction promotion.

    Promotes if: L ≥ 3, 2+ territories held, Accord ≥ 4 averaged across
    holdings, sustained 2 consecutive seasons. PT < 3 average → RM variant
    (extra-parliamentary); PT ≥ 3 → parliamentary candidate.
    """
    insurgencies = _ins_store(world)
    if insurgency_id not in insurgencies:
        return PromotionResult(promoted=False, insurgency_id=insurgency_id,
                               new_status=None, reason="insurgency not found")

    rec = insurgencies[insurgency_id]
    if rec.promoted:
        return PromotionResult(promoted=False, insurgency_id=insurgency_id,
                               new_status=rec.parliamentary_status,
                               reason="already promoted")

    # GD-3 (c) thresholds
    if rec.L < INSURGENCY_PROMOTE_MIN_L:
        return PromotionResult(promoted=False, insurgency_id=insurgency_id,
                               new_status=None,
                               reason=f"L={rec.L} < {INSURGENCY_PROMOTE_MIN_L}")

    if len(rec.territory_ids) < INSURGENCY_PROMOTE_MIN_TERRITORIES:
        return PromotionResult(promoted=False, insurgency_id=insurgency_id,
                               new_status=None,
                               reason=f"only {len(rec.territory_ids)} territories")

    accords = [world.territories[tid].accord for tid in rec.territory_ids
               if tid in world.territories]
    avg_accord = sum(accords) / len(accords) if accords else 0
    if avg_accord < INSURGENCY_PROMOTE_MIN_ACCORD:
        return PromotionResult(promoted=False, insurgency_id=insurgency_id,
                               new_status=None,
                               reason=f"avg Accord {avg_accord:.1f} < {INSURGENCY_PROMOTE_MIN_ACCORD}")

    # GD-3 (d) / (e) — RM vs parliamentary based on PT
    pts = [world.territories[tid].pt for tid in rec.territory_ids
           if tid in world.territories]
    avg_pt = sum(pts) / len(pts) if pts else 0

    # [canonical: GD-3 (d) — "PT < 3 average across held territories → faction
    #  emerges as Restoration Movement variant (anti-Church identity,
    #  extra-parliamentary status)"]
    # [canonical: GD-3 (e) — "PT ≥ 3 average → generic new Parliamentary candidate"]
    new_status = 'extra-parliamentary' if avg_pt < INSURGENCY_RM_PT_THRESHOLD else 'parliamentary'

    rec.promoted = True
    rec.parliamentary_status = new_status

    return PromotionResult(
        promoted=True,
        insurgency_id=insurgency_id,
        new_status=new_status,
        reason=f"L={rec.L} territories={len(rec.territory_ids)} avg_accord={avg_accord:.1f} avg_pt={avg_pt:.1f}",
    )


def get_insurgencies(world=None) -> dict[str, InsurgencyRecord]:
    """Inspection helper."""
    return dict(_ins_store(world))


def reset_for_world(world=None):
    """Test helper — clear insurgency state."""
    _ins_store(world).clear()
    _streak_store(world).clear()
