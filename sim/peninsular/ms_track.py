"""
sim/peninsular/ms_track.py — Mass Suspension (MS) world-track

Canon source: params/core.md §MS Baseline Decay (PP-255)

Implements the MS clock: floor 0 (Rupture), ceiling 100, baseline drift
of −1 per in-game year applied at Year-End Accounting. Thread operations
and Restoration sources adjust beyond baseline via apply_ms_delta.

MS lives at world.clocks['MS'] per game_state schema. Initial value set
at world creation (currently 80; canon defaults: TTRPG 60, BG 72 — see
ASSUMPTION below).

[ASSUMPTION: starting-value reconciliation deferred — basis: game_state
 currently initialises MS=80 which does not match canon's TTRPG 60 / BG 72
 defaults. This is pre-existing schema state and out of Tier 0 scope.
 ms_track operates on whatever value world.clocks['MS'] holds; corrections
 to starting state belong in a separate game_state commit.]

[DRIFT: accounting._ms_decay (sim/peninsular/accounting.py L36-39) ALSO
 implements PP-255 baseline decay inline. This module is the canonical
 surface for MS arithmetic per the Pass 2l module-decomposition plan; the
 accounting inline copy predates the stub. Migration (accounting calls
 apply_ms_baseline_decay instead of inlining) is out of Tier 0 scope —
 it touches an implemented module. Until migration: both code paths
 produce identical output (MS_FLOOR=0, MS_CEILING=100, delta=-1/year).]

Dependencies:
  - sim/autoload/game_state

Entry points:
  - apply_ms_baseline_decay(world: GameState) -> int
  - apply_ms_delta(delta: int, source: str, world: GameState) -> int
"""
from __future__ import annotations


# §MS Baseline Decay (PP-255) constants
# [canonical: params/core.md §MS Baseline Decay — "MS floor: 0 (Rupture).
#  MS ceiling: 100."]
MS_FLOOR = 0          # Rupture
MS_CEILING = 100

# [canonical: §MS Baseline Decay — "−1 per in-game year from baseline drift alone"]
MS_BASELINE_DECAY_PER_YEAR = -1

# [canonical: §MS Baseline Decay — "TTRPG: −1 MS per 4-season year, applied at
#  Year-End Accounting."]
SEASONS_PER_YEAR = 4

# [canonical: §MS Baseline Decay — starting values by mode]
MS_START_TTRPG = 60
MS_START_BOARD_GAME = 72


def _clamp(value: float) -> int:
    """Clamp MS to [floor, ceiling] per canon."""
    return int(max(MS_FLOOR, min(MS_CEILING, value)))


def apply_ms_baseline_decay(world) -> int:
    """Apply −1 MS per in-game year per PP-255.

    Should be invoked at Year-End Accounting (every SEASONS_PER_YEAR seasons).
    Caller is responsible for the seasonal cadence; this function applies
    one year's decay unconditionally when called. Returns the new MS value.
    """
    # [canonical: §MS Baseline Decay (PP-255)]
    current = world.clocks.get('MS', MS_START_TTRPG)
    new_value = _clamp(current + MS_BASELINE_DECAY_PER_YEAR)
    world.clocks['MS'] = new_value
    return new_value


def apply_ms_delta(delta: int, source: str, world) -> int:
    """Apply a non-baseline MS change (Thread operation, Restoration source).

    delta: signed int. Negative = MS reduction (Thread ops, ruptures).
           Positive = MS gain (Restoration sources, Mending).
    source: free-text describing cause for downstream logging / audit.
    Returns the clamped new MS value.

    Per PP-255: "Restoration sources can offset but not reverse baseline decay."
    This module does not enforce that policy — it applies arbitrary deltas;
    the "cannot reverse baseline decay" semantic is a caller-side rule about
    when to allow restoration vs when baseline has already taken effect.
    """
    # [canonical: §MS Baseline Decay (PP-255) — "Thread operations accelerate
    #  this. Restoration sources can offset but not reverse baseline decay."]
    current = world.clocks.get('MS', MS_START_TTRPG)
    new_value = _clamp(current + delta)
    world.clocks['MS'] = new_value
    return new_value
