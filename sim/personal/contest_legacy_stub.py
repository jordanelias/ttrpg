"""
sim/personal/contest_legacy_stub.py — DEPRECATED single-compare social-contest stub

⚠️ DEPRECATED (Stage 1b, 2026-06-30, designs/audit/2026-06-30-contest-stage0-reconciliation).
   SUPERSEDED BY the promoted groundup kernel package `sim/personal/contest/` (a real
   directory package). This 256-line single-compare stub is retained (deprecate-not-delete)
   ONLY as the provenance source for the public API the two live importers need:
     • run_contest / ContestResult / ExchangeResult / build_argue_pool / resolve_exchange
     • the Persuasion-Track threshold constants (PERSUASION_*)
   The new package `sim/personal/contest/__init__.py` RE-EXPORTS these from this module so
   scene_dispatch.py and parliamentary_vote.py keep resolving unchanged. Do NOT import this
   module directly in new code; import `sim.personal.contest` (the package) instead. The v30
   re-skin + build_contest/resolve_contest wrapper land in the NEXT stage.

Canon source: designs/scene/social_contest_v30.md §1-§9

Implements the contest pipeline:
  - build_argue_pool: §3 Argue Pool = (Primary Attribute × 2) + History
  - resolve_exchange: §4 exchange resolution (pool roll, margin vs resistance,
    Persuasion Track update)
  - run_contest: §2-§6 full contest orchestration (setup + exchanges + post-resolution)

[ASSUMPTION: actor is duck-typed — basis: World has no contestant character
 schema. Caller supplies object with .actor_id, .primary_attribute (int 1-7),
 .history (relevant points), .focus (int 1-7), .convictions (optional list),
 .beliefs (optional list of belief_ids), .concentration (int, default
 focus*3 per §4).]

Beliefs integration per §9.5: a Decisive win on a Belief-aligned position
grants +1 Momentum (cap 4) — calls beliefs.social_success(aligned=True).
A Belief-challenging win marks revision per §5.5. Both routed through
the cycle-pair mechanism without cyclic import (late-import inside
function body).

Conviction integration per §6.2: contests producing Decisive outcomes
may trigger Conviction Scar via post-contest hook (called via
conviction.apply_conviction_scar if a Conviction is named in stakes).

Dependencies:
  - sim/autoload/dice_engine
  - sim/personal/conviction (via late-import inside function bodies)
  - sim/personal/beliefs (via late-import)

Entry points:
  - run_contest(parties, stakes, world) -> ContestResult
  - build_argue_pool(actor, position) -> int
  - resolve_exchange(parties, exchange_n, persuasion_track, world) -> ExchangeResult
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional, Any

from sim.autoload.dice_engine import roll_pool


# §3 Argue Pool formula
# [canonical: §3 — "Argue Pool = (Primary Attribute × 2) + History bonus"]
ARGUE_POOL_TN = 7  # [canonical: §3 — "TN: 7 (Standard)"]

# §4 Concentration formula
# [canonical: §4 — "Concentration restores to max (Focus × 3)"]
CONCENTRATION_MULTIPLIER = 3

# §6 Persuasion Track resolution thresholds
# [canonical: §6 — "Persuasion Track ≥ 7 = Side A wins; ≤ 3 = Side B wins; 4–6 = compromise"]
PERSUASION_WIN_THRESHOLD = 7
PERSUASION_LOSS_THRESHOLD = 3
PERSUASION_TOTAL_VICTORY = 9  # §6 — "Persuasion Track ≥ 9 or ≤ 1"
PERSUASION_TOTAL_DEFEAT = 1
PERSUASION_TRACK_START_DEFAULT = 5  # Neutral starting position

# §2 Step 4 Audience Resistance modifiers (proceeding type matters; this is
# the table value the caller supplies, not enforced here — kept as default)
RESISTANCE_DEFAULT = 1

# §6 Contest Fatigue
# [canonical: §6 — "losing primary orator gains Contest Fatigue (-1D next
#  social roll, one instance per session, clears at next session start)"]
CONTEST_FATIGUE_PENALTY = -1


@dataclass
class ExchangeResult:
    """Result of a single exchange per §4."""
    exchange_n: int
    side_a_actor: str
    side_b_actor: str
    a_net: int
    b_net: int
    winning_side: Optional[str]   # 'A' / 'B' / None (tie)
    margin: int                   # |a_net - b_net|
    resistance: int
    track_movement: int           # Toward winner's position (signed: +A / -B)
    notes: list[str] = field(default_factory=list)


@dataclass
class ContestResult:
    """Result of a complete contest per §6."""
    parties: list
    final_persuasion_track: int
    winner: Optional[str]         # 'A' / 'B' / None (compromise)
    total_victory: bool
    exchanges: list[ExchangeResult]
    momentum_grants: dict        # actor_id → +momentum
    contest_fatigue: list         # actor_ids granted Contest Fatigue
    belief_alignments_marked: list  # (actor_id, belief_id) pairs


def build_argue_pool(actor, position: Any = None) -> int:
    """§3 Argue Pool = (Primary Attribute × 2) + History bonus.

    position: optional belief/stance the actor argues. Not currently used
    for pool math (Belief alignment is post-contest momentum per §9.5);
    kept in signature for future Belief-alignment dice bonuses.

    [canonical: §3 — base formula. Wound penalty -1D per wound (PP-716)
     applied per actor.wounds attr if present.]
    """
    primary = getattr(actor, 'primary_attribute', 3)
    history = getattr(actor, 'history', 0)
    wounds = getattr(actor, 'wounds', 0)
    fatigue_penalty = CONTEST_FATIGUE_PENALTY if getattr(actor, 'contest_fatigue', False) else 0

    pool = (primary * 2) + history + (-1 * wounds) + fatigue_penalty
    return max(1, pool)


def resolve_exchange(parties: list, exchange_n: int,
                     persuasion_track: int,
                     resistance: int = RESISTANCE_DEFAULT,
                     world=None, rng=None) -> tuple[ExchangeResult, int]:
    """§4 Resolve a single exchange between two parties.

    parties: list of exactly 2 actor objects with side labels via .side ('A' or 'B').
    persuasion_track: current track position (1-9 typical).
    resistance: §2 audience resistance.

    Returns (ExchangeResult, new_persuasion_track).
    """
    if len(parties) != 2:
        return (ExchangeResult(
            exchange_n=exchange_n, side_a_actor='?', side_b_actor='?',
            a_net=0, b_net=0, winning_side=None, margin=0,
            resistance=resistance, track_movement=0,
            notes=['parties must have exactly 2 actors']
        ), persuasion_track)

    side_a = next((p for p in parties if getattr(p, 'side', 'A') == 'A'), parties[0])
    side_b = next((p for p in parties if getattr(p, 'side', 'B') == 'B'), parties[1])

    a_pool = build_argue_pool(side_a)
    b_pool = build_argue_pool(side_b)

    rng = rng if rng is not None else (world.rng if world is not None and hasattr(world, 'rng') else None)
    if rng is None:
        import random
        rng = random.Random()

    a_net = roll_pool(a_pool, tn=ARGUE_POOL_TN, rng=rng).net
    b_net = roll_pool(b_pool, tn=ARGUE_POOL_TN, rng=rng).net

    margin = abs(a_net - b_net)
    if a_net > b_net:
        winner = 'A'
        movement = max(0, margin - resistance)
    elif b_net > a_net:
        winner = 'B'
        movement = -max(0, margin - resistance)
    else:
        # §4 — Tied exchanges: track moves +1 toward first-to-speak holder
        # [canonical: §4 — "Persuasion Track moves +1 toward first-to-speak"]
        # We treat A as first-to-speak by default; caller can swap by side label.
        winner = None
        movement = +1   # toward A by convention if no first-to-speak override

    new_track = max(0, min(10, persuasion_track + movement))

    return (ExchangeResult(
        exchange_n=exchange_n,
        side_a_actor=getattr(side_a, 'actor_id', 'A'),
        side_b_actor=getattr(side_b, 'actor_id', 'B'),
        a_net=a_net, b_net=b_net, winning_side=winner,
        margin=margin, resistance=resistance, track_movement=movement,
    ), new_track)


def run_contest(parties: list, stakes: dict, world=None, rng=None) -> ContestResult:
    """§2-§6 Run a complete contest.

    parties: list of 2 actor objects with .side ('A'/'B').
    stakes: dict with optional keys:
      'exchange_count': int (§2 Step 3, default 3)
      'resistance': int (§2 Step 4, default 1)
      'starting_track': int (§2 Step 4, default 5)
      'belief_ids': dict {actor_id → belief_id} for §9.5 alignment momentum
      'conviction_engaged': dict {actor_id → conviction_name} for §6.2 Scar
    """
    exchange_count = stakes.get('exchange_count', 3)
    resistance = stakes.get('resistance', RESISTANCE_DEFAULT)
    track = stakes.get('starting_track', PERSUASION_TRACK_START_DEFAULT)
    belief_ids = stakes.get('belief_ids', {})

    exchanges = []
    for n in range(1, exchange_count + 1):
        result, track = resolve_exchange(parties, n, track, resistance, world=world, rng=rng)
        exchanges.append(result)

    # §6 Post-contest resolution
    if track >= PERSUASION_WIN_THRESHOLD:
        winner = 'A'
    elif track <= PERSUASION_LOSS_THRESHOLD:
        winner = 'B'
    else:
        winner = None  # Compromise

    total_victory = (track >= PERSUASION_TOTAL_VICTORY or track <= PERSUASION_TOTAL_DEFEAT)

    # §9.5 Belief alignment momentum (§6 Total Victory awards +1 Momentum)
    # Plus per §9.5: alignment on the winning side counts as Belief
    # achievement (max 1 Momentum per contest from Belief alignment).
    momentum_grants = {}
    belief_alignments_marked = []
    if winner == 'A':
        winning_actor = next((p for p in parties if getattr(p, 'side', 'A') == 'A'), parties[0])
    elif winner == 'B':
        winning_actor = next((p for p in parties if getattr(p, 'side', 'B') == 'B'), parties[1])
    else:
        winning_actor = None

    if winning_actor:
        actor_id = getattr(winning_actor, 'actor_id', None)
        if actor_id and actor_id in belief_ids:
            belief_id = belief_ids[actor_id]
            # Late-import to break cycle with beliefs module
            try:
                from sim.personal.beliefs import social_success
                current_momentum = getattr(winning_actor, 'momentum', 0)
                rr = social_success(actor_id, belief_id, aligned=True,
                                    current_momentum=current_momentum, world=world)
                if rr.momentum_delta > 0:
                    momentum_grants[actor_id] = rr.momentum_delta
                    belief_alignments_marked.append((actor_id, belief_id))
            except (ImportError, AttributeError):
                pass

    # §6 Contest Fatigue for losing primary orator
    contest_fatigue = []
    if winner == 'A':
        losing = next((p for p in parties if getattr(p, 'side', None) == 'B'), parties[1])
        contest_fatigue.append(getattr(losing, 'actor_id', 'B'))
    elif winner == 'B':
        losing = next((p for p in parties if getattr(p, 'side', None) == 'A'), parties[0])
        contest_fatigue.append(getattr(losing, 'actor_id', 'A'))

    return ContestResult(
        parties=parties,
        final_persuasion_track=track,
        winner=winner,
        total_victory=total_victory,
        exchanges=exchanges,
        momentum_grants=momentum_grants,
        contest_fatigue=contest_fatigue,
        belief_alignments_marked=belief_alignments_marked,
    )
