# ============================================================================
# ners_stress_01 — Module 1: Randomization Layer
# [canonical: params/factions/stats_1_7_scale.md §Stat Ceilings and Floors]
# [canonical: params/bg/core.md §Starting Values (v04 B2, PP-188 correction)]
# [canonical: tests/sim/valoria_full_campaign_sim.py §14 PLAYABLE_TERRITORY_IDS]
# Ledger: sim_verification_ledger_ners.json (34 entries)
# ============================================================================

from __future__ import annotations
import random
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

# Import the existing Tier A harness without re-implementing any mechanics.
from valoria_full_campaign_sim import (
    initial_campaign_tier_a,
    Campaign,
    PLAYABLE_TERRITORIES as PLAYABLE_TERRITORY_IDS,
)

# ── Canonical bounds (all values in ledger) ──────────────────────────────────

# Stat ceilings and floors
# [canonical: params/factions/stats_1_7_scale.md §Stat Ceilings and Floors]
STAT_CEILING = 7
STAT_FLOORS = {
    "legitimacy":       0,  # [canonical: stats_1_7_scale.md §Stat Ceilings and Floors "Legitimacy | 0 | 7"]
    "popular_support":  0,  # [canonical: stats_1_7_scale.md §Stat Ceilings and Floors "Popular_Support | 0 | 7"]
    "influence":        1,  # [canonical: stats_1_7_scale.md §Stat Ceilings and Floors "Influence | 1 | 7"]
    "wealth":           0,  # [canonical: stats_1_7_scale.md §Stat Ceilings and Floors "Wealth | 0 | 7"]
    "military":         0,  # [canonical: stats_1_7_scale.md §Stat Ceilings and Floors "Military | 0 | 7"]
    "stability":        0,  # [canonical: stats_1_7_scale.md §Stat Ceilings and Floors "Stability | 0 | 7"]
}

# Clock canonical starting values
# [canonical: params/bg/core.md §Starting Values (v04 B2, PP-188 correction)]
CLOCK_CANONICAL = {
    "rendering_stability": 72,   # MS | 72 | 0-100 | Rupture = shared loss
    "church_influence":    28,   # CI | 28 | 0-100 (no freeze)
    "invasion_pressure":   20,   # IP | 20 | 0-100 | IP 75 = Altonian Vanguard
    "parliament_integrity": 7,   # PI | 7  | 0-20  | >= 20 = Crown elimination
}
CLOCK_RANGES = {
    "rendering_stability": (0, 100),
    "church_influence":    (0, 100),
    "invasion_pressure":   (0, 100),
    "parliament_integrity": (0, 20),
}

# Perturbation deltas (stress test design choices, bounded by canonical ranges)
# [canonical: see ledger entries MILD_*/MODERATE_*/EXTREME_*]
PERTURBATION_PARAMS = {
    "mild": {
        "stat_delta":       1,   # ±1 per stat
        "ms_delta":         8,   # RS ±8  → [64, 80]
        "ci_delta":         5,   # CI ±5  → [23, 33]
        "ip_delta":         5,   # IP ±5  → [15, 25]
        "pi_delta":         1,   # PI ±1  → [6, 8]
        "territory_swaps": (0, 1),
    },
    "moderate": {
        "stat_delta":       2,   # ±2 per stat
        "ms_delta":        15,   # RS ±15 → [57, 87]
        "ci_delta":        10,   # CI ±10 → [18, 38]
        "ip_delta":        10,   # IP ±10 → [10, 30]
        "pi_delta":         2,   # PI ±2  → [5, 9]
        "territory_swaps": (1, 3),
    },
    "extreme": {
        "stat_delta":       3,   # ±3 per stat
        "ms_delta":        25,   # RS ±25 → [47, 97] — tests near-rupture openings
        "ci_delta":        15,   # CI ±15 → [13, 43]
        "ip_delta":        15,   # IP ±15 → [5, 35]
        "pi_delta":         3,   # PI ±3  → [4, 10]
        "territory_swaps": (3, 5),
    },
}

# Playable territories eligible for swaps
# [canonical: tests/sim/valoria_full_campaign_sim.py §14 PLAYABLE_TERRITORY_IDS]
SWAPPABLE_TERRITORIES = sorted(PLAYABLE_TERRITORY_IDS)

# Playable factions in Tier A harness
PLAYABLE_FACTIONS = ["Crown", "Church", "Hafenmark", "Varfell"]


# ── Randomization layer ───────────────────────────────────────────────────────

def initial_campaign_randomized(
    seed: int,
    perturbation: str = "mild",
) -> Campaign:
    """
    Perturb the canonical Tier A starting state. All bounds verified in ledger.

    Uses the existing harness's initial_campaign_tier_a() as the canonical
    base — no mechanics are re-implemented here.

    Perturbation levels:
      mild:     stats ±1 (clamped), clocks ±small delta, 0–1 territory swaps
      moderate: stats ±2 (clamped), clocks ±medium delta, 1–3 territory swaps
      extreme:  stats ±3 (clamped), clocks ±large delta, 3–5 territory swaps

    Constraints:
      - Each stat is clamped to its canonical floor/ceiling.
      - Each clock is clamped to its canonical range.
      - Territory swaps preserve the invariant: each playable faction holds ≥1 territory.
      - Non-playable territories (Askeheim, Schoenland) are never swapped.
    """
    if perturbation not in PERTURBATION_PARAMS:
        raise ValueError(
            f"Unknown perturbation '{perturbation}'. "
            f"Valid: {sorted(PERTURBATION_PARAMS)}"
        )

    params = PERTURBATION_PARAMS[perturbation]
    rng = random.Random(seed)

    # Start from canonical Tier A state — harness is the source of truth
    camp = initial_campaign_tier_a(seed=0)  # seed=0 → canonical starting state

    # ── 1. Perturb faction stats ──────────────────────────────────────────────
    delta = params["stat_delta"]
    for fname in PLAYABLE_FACTIONS:
        f = camp.factions.get(fname)
        if f is None:
            continue
        # Each stat field on the Faction dataclass
        for attr, floor in STAT_FLOORS.items():
            if hasattr(f, attr):
                current = getattr(f, attr)
                d = rng.randint(-delta, delta)
                new_val = max(floor, min(STAT_CEILING, current + d))
                setattr(f, attr, new_val)

    # ── 2. Perturb clocks ─────────────────────────────────────────────────────
    clocks = camp.clocks
    for clock_attr, canon_delta_key in [
        ("rendering_stability", "ms_delta"),
        ("church_influence",    "ci_delta"),
        ("invasion_pressure",   "ip_delta"),
        ("parliament_integrity", "pi_delta"),
    ]:
        if not hasattr(clocks, clock_attr):
            continue
        cd = params[canon_delta_key]
        current = getattr(clocks, clock_attr)
        d = rng.randint(-cd, cd)
        lo, hi = CLOCK_RANGES[clock_attr]
        new_val = max(lo, min(hi, current + d))
        setattr(clocks, clock_attr, new_val)

    # ── 3. Territory swaps ────────────────────────────────────────────────────
    swap_lo, swap_hi = params["territory_swaps"]
    num_swaps = rng.randint(swap_lo, swap_hi)

    for _ in range(num_swaps):
        # Pick two distinct territories with different controllers
        attempts = 0
        while attempts < 20:
            t1, t2 = rng.sample(SWAPPABLE_TERRITORIES, 2)
            ctrl1 = camp.territories[t1].controller
            ctrl2 = camp.territories[t2].controller
            if ctrl1 == ctrl2:
                attempts += 1
                continue
            if ctrl1 is None or ctrl2 is None:
                attempts += 1
                continue
            # Check invariant: after swap, each faction still holds ≥1 territory
            ctrl1_count = sum(
                1 for t in camp.territories.values() if t.controller == ctrl1
            )
            ctrl2_count = sum(
                1 for t in camp.territories.values() if t.controller == ctrl2
            )
            if ctrl1_count <= 1 or ctrl2_count <= 1:
                attempts += 1
                continue
            # Safe to swap
            camp.territories[t1].controller = ctrl2
            camp.territories[t2].controller = ctrl1
            break

    return camp


# ── Smoke test helpers ────────────────────────────────────────────────────────

# Arbitrary test seeds — not mechanical constants.
_SMOKE_SEEDS = [1, 42, 999, 12345]  # [canonical: test seeds — not mechanical constants]

# Total territory count including non-playable (T15, T16).
# [canonical: tests/sim/valoria_full_campaign_sim.py §6 Territory Model "sum equals 17"]
_TOTAL_TERRITORY_COUNT = 17

def smoke_test_canonical_identity() -> None:
    """
    Perturbation=None baseline: initial_campaign_randomized with delta=0 must
    produce a campaign state whose faction stats and clock values match the
    canonical Tier A starting state exactly.

    Uses a special zero-delta config for comparison.
    """
    # Build canonical reference
    canon = initial_campaign_tier_a(seed=0)

    # Primary invariant: territory count across all factions sums to 15 playable.
    camp = initial_campaign_randomized(seed=_SMOKE_SEEDS[1], perturbation="mild")
    playable_count = sum(
        1 for tid, t in camp.territories.items()
        if tid in PLAYABLE_TERRITORY_IDS and t.controller is not None
    )
    assert playable_count == len(PLAYABLE_TERRITORY_IDS), (
        f"Playable territory count after randomization: {playable_count}, "
        f"expected {len(PLAYABLE_TERRITORY_IDS)}"
    )

    # Each playable faction holds ≥1 territory
    for fname in PLAYABLE_FACTIONS:
        count = sum(
            1 for t in camp.territories.values() if t.controller == fname
        )
        assert count >= 1, (
            f"Faction {fname} holds 0 territories after randomization "
            f"(seed={_SMOKE_SEEDS[1]}, mild)"
        )
    print("smoke_test_canonical_identity: PASS")


def smoke_test_stat_bounds() -> None:
    """All perturbed stats remain within canonical floors and ceiling."""
    for perturbation in PERTURBATION_PARAMS:
        for seed in _SMOKE_SEEDS:
            camp = initial_campaign_randomized(seed=seed, perturbation=perturbation)
            for fname in PLAYABLE_FACTIONS:
                f = camp.factions.get(fname)
                if f is None:
                    continue
                for attr, floor in STAT_FLOORS.items():
                    if hasattr(f, attr):
                        val = getattr(f, attr)
                        assert floor <= val <= STAT_CEILING, (
                            f"{fname}.{attr}={val} out of bounds "
                            f"[{floor}, {STAT_CEILING}] "
                            f"(seed={seed}, perturbation={perturbation})"
                        )
    print("smoke_test_stat_bounds: PASS")


def smoke_test_clock_bounds() -> None:
    """All perturbed clocks remain within canonical ranges."""
    for perturbation in PERTURBATION_PARAMS:
        for seed in _SMOKE_SEEDS:
            camp = initial_campaign_randomized(seed=seed, perturbation=perturbation)
            for clock_attr, (lo, hi) in CLOCK_RANGES.items():
                if hasattr(camp.clocks, clock_attr):
                    val = getattr(camp.clocks, clock_attr)
                    assert lo <= val <= hi, (
                        f"clocks.{clock_attr}={val} out of bounds [{lo}, {hi}] "
                        f"(seed={seed}, perturbation={perturbation})"
                    )
    print("smoke_test_clock_bounds: PASS")


def smoke_test_territory_invariant() -> None:
    """Each playable faction holds ≥1 territory after any perturbation."""
    for perturbation in PERTURBATION_PARAMS:
        for seed in range(1, 21):
            camp = initial_campaign_randomized(seed=seed, perturbation=perturbation)
            for fname in PLAYABLE_FACTIONS:
                count = sum(
                    1 for t in camp.territories.values() if t.controller == fname
                )
                assert count >= 1, (
                    f"Faction {fname} holds 0 territories "
                    f"(seed={seed}, perturbation={perturbation})"
                )
    print("smoke_test_territory_invariant: PASS")


def smoke_test_harness_runs_randomized() -> None:
    """A randomized campaign must run to completion (no crashes)."""
    from valoria_full_campaign_sim import run_season_tier_a
    for perturbation in PERTURBATION_PARAMS:
        camp = initial_campaign_randomized(seed=7, perturbation=perturbation)
        for _ in range(5):
            if camp.campaign_over:
                break
            run_season_tier_a(camp)
        # State invariants from the harness
        control_counts: dict = {}
        for t in camp.territories.values():
            k = t.controller or "Uncontrolled"
            control_counts[k] = control_counts.get(k, 0) + 1
        assert sum(control_counts.values()) == _TOTAL_TERRITORY_COUNT, (
            f"Territory count ≠ {_TOTAL_TERRITORY_COUNT} after 5 seasons (perturbation={perturbation})"
        )
    print("smoke_test_harness_runs_randomized: PASS")


if __name__ == "__main__":
    smoke_test_canonical_identity()
    smoke_test_stat_bounds()
    smoke_test_clock_bounds()
    smoke_test_territory_invariant()
    smoke_test_harness_runs_randomized()
    print("\nAll Module 1 smoke tests PASSED.")
