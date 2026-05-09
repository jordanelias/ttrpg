"""
NERS Stress Test — Module 1: Randomization Layer.

Wraps the existing Tier A campaign harness with a perturbation layer used by
Module 2 (NERS Evaluation + Batch Runner) to stress-test the strategic layer
under randomized starting conditions.

[canonical: tests/sim/ners_stress_01/module_manifest.md §Module 1]
[base harness: tests/sim/valoria_full_campaign_sim.py — has its own verification ledger]
"""

import os
import random
import sys
from typing import Tuple

# Allow import of the sibling harness in tests/sim/.
_PARENT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _PARENT not in sys.path:
    sys.path.insert(0, _PARENT)

from valoria_full_campaign_sim import Campaign, initial_campaign_tier_a


# ── Canonical bounds ─────────────────────────────────────────────────────────

# [canonical: params/bg/core.md §Stat Ceilings and Floors L195-203]
STAT_FLOOR_DEFAULT = 0      # Mandate (L+PS), Wealth, Military, Stability floor
STAT_FLOOR_INFLUENCE = 1    # Influence floor (only stat with non-zero floor)
STAT_CEILING = 7            # All stats: ceiling

# [canonical: params/bg/core.md §Starting Values L77-101 — clock ranges]
CLOCK_RANGES = {
    'rendering_stability':  (0, 100),  # MS 0-100
    'church_influence':     (0, 100),  # CI 0-100
    'invasion_pressure':    (0, 100),  # IP 0-100
    'parliament_integrity': (0, 20),   # PI 0-20
    'aer':                  (0, 5),    # AER 0-5
    'torben_loyalty':       (0, 7),    # Torben 0-7
    'elske_loyalty':        (0, 7),    # Elske 0-7
    'warden_recognition':   (0, 3),    # WR 0-3 (PP-605)
    'warden_cooperation':   (0, 3),    # WC 0-3 (PP-605)
    'peninsular_strain':    (0, 10),   # Strain/Turmoil 0-10
}

# [canonical: stats_1_7_scale.md TC60 + params/bg/core.md L81 "CI 60 = Mass Seizure available"]
CI_MASS_SEIZURE_THRESHOLD = 60

# Faction stat fields eligible for perturbation. Intel is omitted because it
# is None on all BG-mode factions in the canonical starting state per the
# harness's starting_factions() — perturbing None has no effect.
# [canonical: stats_1_7_scale.md §Starting Stats — Intel column None for BG factions]
_PERTURBABLE_STAT_FIELDS = ('mandate', 'influence', 'wealth', 'military', 'stability')

# Perturbation level table.
# [canonical: tests/sim/ners_stress_01/module_manifest.md §Randomization design]
#   stat_offset: integer ± offset on each stat (clamped to canonical floor/ceiling)
#   clock_pct: fraction of (hi-lo) range applied as integer ± delta
#   terr_swaps_min/max: paired controller swaps among playable-faction territories
_PERTURBATION_LEVELS = {
    # [canonical: manifest §Module 1 — perturbation bounds 'none' (smoke-test path)]
    'none':     {'stat_offset': 0, 'clock_pct': 0.0,  'terr_swaps_min': 0, 'terr_swaps_max': 0},
    # [canonical: manifest §Module 1 — perturbation bounds 'mild']
    'mild':     {'stat_offset': 1, 'clock_pct': 0.1,  'terr_swaps_min': 0, 'terr_swaps_max': 1},
    # [canonical: manifest §Module 1 — perturbation bounds 'moderate']
    'moderate': {'stat_offset': 2, 'clock_pct': 0.2,  'terr_swaps_min': 1, 'terr_swaps_max': 3},
    # [canonical: manifest §Module 1 — perturbation bounds 'extreme']
    'extreme':  {'stat_offset': 3, 'clock_pct': 0.3,  'terr_swaps_min': 3, 'terr_swaps_max': 5},
}

# [canonical: designs/world/geography_v30.md §Starting Control Summary]
# Schoenland is the Island Republic (not in play); T15 Askeheim is Uncontrolled
# (Southernmost, hard-fixed). Only the four playable bg-mode factions participate
# in territory ownership perturbation.
_PLAYABLE_OWNERS_FOR_SWAP = ('Crown', 'Church', 'Hafenmark', 'Varfell')

# Perturbation RNG seed derivation. Separate from campaign RNG so that
# campaign-level dice rolls remain reproducible per seed even when the
# starting state is perturbed differently.
# [canonical: design — magic-number-free seed mixing]
_PERTURB_SEED_MULT = 1000
_PERTURB_SEED_MOD = 1000  # [canonical: design — matches MULT magnitude for hash domain]


def initial_campaign_randomized(seed: int, perturbation: str = 'none') -> Campaign:
    """
    Build a Campaign with optional randomized perturbation of starting state.

    At perturbation='none', returns canonical Tier A state byte-equivalent to
    initial_campaign_tier_a(seed=seed). At other levels, perturbs faction
    stats, clocks, and territory ownership within canonical bounds.

    Parameters
    ----------
    seed : int
        Seed for both campaign RNG (passed to initial_campaign_tier_a) and the
        perturbation RNG (derived independently).
    perturbation : str
        One of 'none' | 'mild' | 'moderate' | 'extreme'.

    Design note — starting_mandate / starting_military re-anchoring:
        On perturbation, the faction's `starting_mandate` and `starting_military`
        baselines are re-anchored to the perturbed values. This makes the
        perturbed state the faction's "natural" baseline, so recovery dynamics
        (Mandate Recovery, Military Seasonal Cap) operate consistently from
        the new starting point rather than treating perturbation as a deficit
        to recover from. This is the stress-test interpretation.
    """
    if perturbation not in _PERTURBATION_LEVELS:
        raise ValueError(
            f"perturbation must be one of {list(_PERTURBATION_LEVELS)}, "
            f"got {perturbation!r}"
        )

    camp = initial_campaign_tier_a(seed=seed)
    if perturbation == 'none':
        return camp

    bounds = _PERTURBATION_LEVELS[perturbation]
    prng = random.Random(seed * _PERTURB_SEED_MULT
                         + hash(perturbation) % _PERTURB_SEED_MOD)

    # ── Perturb faction stats ────────────────────────────────────────────────
    stat_off = bounds['stat_offset']
    for f in camp.factions.values():
        if not f.playable:
            continue  # Guilds, Lowenritter — NPC-only, not perturbed
        for field_name in _PERTURBABLE_STAT_FIELDS:
            current = getattr(f, field_name, None)
            if current is None:
                continue  # RestorationMovement: all stats None
            offset = prng.randint(-stat_off, stat_off)
            floor = (STAT_FLOOR_INFLUENCE if field_name == 'influence'
                     else STAT_FLOOR_DEFAULT)
            new_val = max(floor, min(STAT_CEILING, current + offset))
            setattr(f, field_name, new_val)
            if field_name == 'mandate':
                f.starting_mandate = new_val
            elif field_name == 'military':
                f.starting_military = new_val

    # ── Perturb clocks ───────────────────────────────────────────────────────
    pct = bounds['clock_pct']
    for clock_name, (lo, hi) in CLOCK_RANGES.items():
        current = getattr(camp.clocks, clock_name, None)
        if current is None:
            continue
        delta_max = max(1, int(round(pct * (hi - lo))))   # [canonical: design — ≥1 floor when perturbing]
        offset = prng.randint(-delta_max, delta_max)
        new_val = max(lo, min(hi, current + offset))
        setattr(camp.clocks, clock_name, new_val)

    # Re-derive CI threshold flags after perturbation.
    # [canonical: stats_1_7_scale.md TC60 + params/bg/core.md L81]
    if camp.clocks.church_influence >= CI_MASS_SEIZURE_THRESHOLD:
        camp.clocks.tc60_seizure_unlocked = True
        if not camp.clocks.mass_seizure_used:
            camp.clocks.mass_seizure_available = True

    # ── Perturb territory ownership ──────────────────────────────────────────
    n_swaps = prng.randint(bounds['terr_swaps_min'], bounds['terr_swaps_max'])
    swappable = [tid for tid, t in camp.territories.items()
                 if t.controller in _PLAYABLE_OWNERS_FOR_SWAP]
    for _ in range(n_swaps):
        if len(swappable) < 2:
            break
        a, b = prng.sample(swappable, 2)
        ta, tb = camp.territories[a], camp.territories[b]
        ta.controller, tb.controller = tb.controller, ta.controller
        # starting_controller preserved; only live `controller` is mutated.

    return camp


# ── Smoke test ───────────────────────────────────────────────────────────────

def smoke_test() -> None:
    """
    Module 1 verification gate: perturbation='none' must produce a Campaign
    state equivalent to initial_campaign_tier_a(seed=seed) across multiple
    seeds. Compares public attribute state of factions, clocks, territories,
    and proximity.
    """
    def _public(obj):
        return {k: v for k, v in vars(obj).items() if not k.startswith('_')}

    # [canonical: smoke test — varied deterministic seeds]
    for seed in (0, 1, 42, 12345):
        a = initial_campaign_randomized(seed=seed, perturbation='none')
        b = initial_campaign_tier_a(seed=seed)
        assert a.seed == b.seed, f"seed mismatch at seed={seed}"

        for fname in a.factions:
            assert _public(a.factions[fname]) == _public(b.factions[fname]), \
                f"faction {fname} mismatch at seed={seed}"

        assert _public(a.clocks) == _public(b.clocks), \
            f"clocks mismatch at seed={seed}"

        for tid in a.territories:
            assert _public(a.territories[tid]) == _public(b.territories[tid]), \
                f"territory {tid} mismatch at seed={seed}"

        assert a.proximity == b.proximity, f"proximity mismatch at seed={seed}"

    # Sanity check: non-trivial perturbation should produce a distinct state.
    canonical = initial_campaign_tier_a(seed=0)
    perturbed = initial_campaign_randomized(seed=0, perturbation='extreme')
    diffs = sum(
        1 for fname in canonical.factions
        if _public(canonical.factions[fname]) != _public(perturbed.factions[fname])
    )
    assert diffs > 0, "extreme perturbation produced no faction-state changes — RNG broken?"

    print("[OK] Module 1 smoke test passed:")
    print("  perturbation='none' matches canonical for all tested seeds")
    print(f"  perturbation='extreme' produced {diffs} factions with state changes (sanity check)")


if __name__ == '__main__':
    smoke_test()
