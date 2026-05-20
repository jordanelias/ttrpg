"""
sim/peninsular/ci_track.py — Church Influence (CI) world-track

Canon source: designs/scene/conviction_track_v30.md §3 (PP-412)
(Note: 'conviction_track_v30.md' is the Piety Track + CI redesign doc;
distinct from designs/personal/conviction_track_v1.md which is the
personal-scale Conviction Scar mechanic.)

Implements PP-412 5-step Seasonal CI Calculation:
  Step 1: Institutional Momentum +1 (passive)
  Step 2: Conviction Yield from prominent territories by PT
  Step 3: Assert (optional Church action) — caller-driven
  Step 4: Suppress (optional opposing action) — caller-driven
  Step 5: Hafenmark Structural Suppression (-1 if Baralta Mandate ≥ 4)

Plus apply_ci_delta for non-seasonal mutations (Excommunication +4, etc).

[DRIFT: accounting._ci_generation (sim/peninsular/accounting.py L23-32)
 implements a simplified version (+2 per Church-held territory). That
 predates the Pass 2l ci_track stub. This module is the canonical surface
 per PP-412; accounting's inline is legacy. Migration deferred (same
 pattern as ms_track / season — out of stub-infill scope to touch
 implemented module).]

Dependencies:
  - sim/autoload/game_state
  - sim/territory/infrastructure (for Templar Station CI gain integration)

Entry points:
  - compute_seasonal_ci_delta(world: GameState) -> dict
  - apply_ci_delta(delta: float, source: str, world: GameState) -> float
"""
from __future__ import annotations

import math
from typing import Optional


# PP-412 Step 1: Institutional Momentum
# [canonical: §3 Step 1 — "CI +1. (Unchanged from PP-402.)"]
CI_INSTITUTIONAL_MOMENTUM = 1

# PP-412 Step 2: Conviction Yield per territory PT
# [canonical: §3 Step 2 — PT yield table]
CI_YIELD_BY_PT = {
    5: 1.0,    # PT 5: +1
    4: 0.5,    # PT 4: +0.5
    3: 0.0, 2: 0.0, 1: 0.0, 0: 0.0,
}

# PP-412 Step 5: Hafenmark Structural Suppression
# [canonical: §3 Step 5 — "While Baralta's Mandate ≥ 4: CI -1/season"]
HAFENMARK_BARALTA_THRESHOLD_MANDATE = 4
HAFENMARK_SUPPRESS_PER_SEASON = -1

# PP-412 starting + phase transition
# [canonical: §3 — "Starting CI: 28 (canonical BG). Phase transition: CI 75."]
CI_STARTING = 28
CI_PHASE_TRANSITION = 75

# PP-412 floor / ceiling
CI_FLOOR = 0
CI_CEILING = 100


def _church_is_prominent(world, territory_id: str) -> bool:
    """A territory is 'Church prominent' iff Church Mandate > controlling
    faction's Mandate. Per §3 Step 2 definition."""
    if territory_id not in world.territories:
        return False
    t = world.territories[territory_id]
    if t.owner is None:
        return False
    if 'Church' not in world.factions:
        return False
    church_mandate = world.factions['Church'].L
    controller_mandate = world.factions[t.owner].L if t.owner in world.factions else 0
    return church_mandate > controller_mandate


def compute_seasonal_ci_delta(world,
                              assert_attempted: bool = False,
                              assert_success: bool = False,
                              suppress_attempted: bool = False,
                              suppress_success: bool = False) -> dict:
    """Compute the PP-412 5-step seasonal CI delta.

    Caller drives Step 3 (Assert) and Step 4 (Suppress) — these are
    optional faction actions, not automatic. assert_success / suppress_success
    are determined by caller-rolled rolls (Church Influence vs Ob 2 for
    Assert; Mandate vs Church Mandate Ob for Suppress).

    Returns dict with breakdown: step1, step2_yield, step3_assert, step4_suppress,
    step5_hafenmark, total_delta, conviction_yield_per_territory.
    """
    breakdown = {
        'step1_momentum': CI_INSTITUTIONAL_MOMENTUM,
        'step2_yield': 0,
        'step3_assert': 0,
        'step4_suppress': 0,
        'step5_hafenmark': 0,
        'conviction_yield_per_territory': {},
    }

    # Step 2: Conviction Yield
    raw_yield = 0.0
    for tid, t in world.territories.items():
        if not _church_is_prominent(world, tid):
            continue
        pt_int = max(0, min(5, int(t.pt)))
        contribution = CI_YIELD_BY_PT.get(pt_int, 0.0)
        if contribution > 0:
            breakdown['conviction_yield_per_territory'][tid] = contribution
            raw_yield += contribution
    # [canonical: §3 Step 2 — "Total Conviction Yield = floor(Σ yield across
    #  all prominent territories)"]
    breakdown['step2_yield'] = math.floor(raw_yield)

    # Step 3: Assert (caller-driven; outcome supplied)
    if assert_attempted:
        # [canonical: §3 Step 3 — "Success: CI +1. Failure: no additional CI;
        #  Stability -1"]
        breakdown['step3_assert'] = 1 if assert_success else 0

    # Step 4: Suppress (caller-driven; outcome supplied)
    if suppress_attempted and suppress_success:
        # [canonical: §3 Step 4 — "Success: negate Step 1 passive +1 for this
        #  season only."]
        breakdown['step4_suppress'] = -breakdown['step1_momentum']

    # Step 5: Hafenmark Structural Suppression
    # [canonical: §3 Step 5 — "While Baralta's Mandate ≥ 4: CI -1/season"]
    # Approximate: Hafenmark faction Mandate >= threshold triggers suppression
    if 'Hafenmark' in world.factions:
        hafenmark_mandate = world.factions['Hafenmark'].L
        if hafenmark_mandate >= HAFENMARK_BARALTA_THRESHOLD_MANDATE:
            breakdown['step5_hafenmark'] = HAFENMARK_SUPPRESS_PER_SEASON

    total = (breakdown['step1_momentum'] + breakdown['step2_yield'] +
             breakdown['step3_assert'] + breakdown['step4_suppress'] +
             breakdown['step5_hafenmark'])
    breakdown['total_delta'] = total

    return breakdown


def apply_ci_delta(delta: float, source: str, world) -> float:
    """Apply an arbitrary CI delta (Excommunication +4, ad-hoc adjustments).

    Returns the new CI value clamped to [CI_FLOOR, CI_CEILING].
    """
    current = world.clocks.get('CI', CI_STARTING)
    new_value = max(CI_FLOOR, min(CI_CEILING, current + delta))
    world.clocks['CI'] = new_value
    return new_value


def apply_seasonal_ci(world, **kwargs) -> dict:
    """Compute + apply the seasonal CI delta in one call.

    Returns the breakdown dict with 'new_ci' key added.
    """
    breakdown = compute_seasonal_ci_delta(world, **kwargs)
    new_ci = apply_ci_delta(breakdown['total_delta'], 'seasonal PP-412', world)
    breakdown['new_ci'] = new_ci
    return breakdown
