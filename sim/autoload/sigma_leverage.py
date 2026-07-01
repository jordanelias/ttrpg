"""
sim/autoload/sigma_leverage.py — σ-leverage advantage layer atop the d10 dice engine.

Canon source: modifier_system_spec.md (the implementation-pass rewrite)
Params source: params/core.md, modifier_system_spec.md
Game Design constraints applicable: none — σ-space resolution math (GD-1..3 govern game-layer mechanics, not dice math)
Rationale:    D0-2 (designs/audit/2026-06-30-contest-stage0-reconciliation/DECISIONS.md)
Status:       [CANONICAL — Stage 1a port 2026-06-30]

Purpose
-------
Single-source the σ-leverage modifier layer for BOTH combat and social-contest, retiring:
  • the test-dir dependency (tests/sim/v32-combat-balance/m1_dice_sigma_core.py)
  • the numpy dependency that file carried
  • the combat sys.path.insert hack (designs/scene/combat_engine_v1/core.py:3)
  • the distillation report's "two σ-kernels" debt

Separation of concerns (D0-2):
  dice_engine  = pool / degree primitive (stdlib root, no deps)
  sigma_leverage = advantage→μ-shift layer atop it (this module)

Dependencies: stdlib only (math, random) + sim.autoload.dice_engine.
              numpy is NOT imported — stdlib math.tanh / math.sqrt are used throughout.

Porting notes
-------------
All numerical behaviour is byte-identical to m1_dice_sigma_core.py:
  • tanh via math.tanh (CPython delegates to libm, same IEEE-754 result)
  • sqrt via math.sqrt (same)
  • roll_net / roll_net_continuous delegate to dice_engine (no new die-roll path)
  • PER_DIE constants copied verbatim with their [canonical: ...] provenance tags
  • LEVEL_SIGMA / M_MAX / SIGMA_N_COEFF copied verbatim with provenance tags

Functions NOT ported from m1_dice_sigma_core:
  • _phi — reproduced here from the original's math.erf path (was already stdlib)
  • roll_net — delegates to dice_engine.roll_pool (integer net)
  • roll_net_continuous — delegates to dice_engine.continuous_engine_sample

Functions added (contest surface, designs/audit/2026-06-03-contest-groundup/engine.py):
  • sigma_N (alias: contest engine names it sigma_N not sigma_n)
  • eff_sigma (alias for soft_cap, with contest naming)
  • effective_ob (display-only Ob shift, per contest engine's signature)
  • level (single modifier-level → σ lookup; engine.py:21 `def level(name): return LEVEL[name]`)

Entry points:
  - sigma_n(pool: float) -> float
  - sigma_N(pool: float) -> float  (contest alias of sigma_n)
  - soft_cap(net_sigma: float) -> float
  - eff_sigma(net_sigma: float) -> float  (contest alias of soft_cap)
  - sigma_space_ob_shift(net_sigma: float, pool: float) -> float
  - eff_ob(base_ob: float, pool: float, net_sigma: float) -> float
  - effective_ob(base_ob: float, net_dsigma: float, pool: float) -> float  (contest arg-order alias of eff_ob)
  - net_boost(net_sigma: float, pool: float, tn: int = TN_STANDARD, capped: bool = True) -> float
  - level(name: str) -> float  (contest modifier-level → σ lookup)
  - levels_to_net_sigma(aggressor: Sequence[str] | None = None, defender: Sequence[str] | None = None) -> float
  - p_success(base_ob: float, pool: float, net_sigma: float = 0.0, tn: int = TN_STANDARD, capped: bool = True) -> float
  - roll_net(pool: float, tn: int = TN_STANDARD, rng: random.Random | None = None) -> int
  - roll_net_continuous(pool: float, tn: int = TN_STANDARD, rng: random.Random | None = None) -> float
"""
from __future__ import annotations

import math
import random
from typing import Sequence

from sim.autoload import dice_engine

# ---------------------------------------------------------------------------
# Canonical per-die statistics (params/core.md "Expected Value (per die)")
# TN → (mu_per_die, sigma_per_die)
# [canonical: params/core.md §Expected Value (per die)]
# ---------------------------------------------------------------------------
PER_DIE: dict[int, tuple[float, float]] = {
    6: (0.50, 0.806),   # [canonical: params/core.md §Expected Value (per die)]
    7: (0.40, 0.800),   # [canonical: params/core.md §Expected Value (per die)]
    8: (0.30, 0.781),   # [canonical: params/core.md §Expected Value (per die)]
}

TN_STANDARD = 7         # [canonical: params/core.md §TN Values]

# ---------------------------------------------------------------------------
# v32 σ-space modifier seeds (modifier_system_spec.md)
# Class B draft sim-seeds — sim-tunable, NOT canonical.
# ---------------------------------------------------------------------------
LEVEL_SIGMA: dict[str, float] = {
    "minor":    0.25,   # [canonical: modifier_system_spec.md §2.3 Player-facing abstraction]
    "moderate": 0.50,   # [canonical: modifier_system_spec.md §2.3 Player-facing abstraction]
    "strong":   0.75,   # [canonical: modifier_system_spec.md §2.3 Player-facing abstraction]
    "major":    1.00,   # [canonical: modifier_system_spec.md §2.3 Player-facing abstraction]
}

M_MAX = 1.5             # soft-cap ceiling, sigma-units   # [canonical: modifier_system_spec.md §3.1 Saturating function]
SIGMA_N_COEFF = 0.8     # sigma_N = 0.8 * sqrt(Pool)      # [canonical: modifier_system_spec.md §2.1 The transform]

# Contest engine surface constants (designs/audit/2026-06-03-contest-groundup/engine.py)
OB_MIN = 1              # [canonical: params/core.md §Obstacle Scale]


# ---------------------------------------------------------------------------
# Core σ-leverage primitives
# ---------------------------------------------------------------------------

def sigma_n(pool: float) -> float:
    """Outcome-distribution width at a pool size (modifier_system_spec.md §2.1).

    Named sigma_n (combat surface). See sigma_N for the contest-surface alias.
    """
    # [canonical: modifier_system_spec.md §2.1 The transform]
    return SIGMA_N_COEFF * math.sqrt(max(1, pool))


def sigma_N(pool: float) -> float:
    """Contest-surface alias for sigma_n.

    designs/audit/2026-06-03-contest-groundup/engine.py names this sigma_N;
    combat surface uses sigma_n. Identical computation.
    """
    return sigma_n(pool)


def soft_cap(net_sigma: float) -> float:
    """Smooth saturating cap: M*tanh(net/M).

    Small sums apply nearly fully; large sums saturate toward ±M_MAX;
    no hard ceiling and no dead-zone.
    [canonical: modifier_system_spec.md §3.1 Saturating function]
    """
    return M_MAX * math.tanh(net_sigma / M_MAX)     # [canonical: modifier_system_spec.md §3.1 Saturating function]


def eff_sigma(net_sigma: float) -> float:
    """Contest-surface alias for soft_cap.

    designs/audit/2026-06-03-contest-groundup/engine.py names this eff_sigma;
    combat surface uses soft_cap. Identical computation.
    """
    return soft_cap(net_sigma)


def sigma_space_ob_shift(net_sigma: float, pool: float) -> float:
    """Raw σ-space Ob shift, pre-soft-cap (modifier_system_spec.md §2.1):
    delta-sigma * sigma_N.  The sqrt(N) cancels in the z-score, so a given
    delta-sigma shifts the outcome's z by exactly that amount at every pool
    size — the F1 fix (uniform modifier impact).
    """
    return net_sigma * sigma_n(pool)


def eff_ob(base_ob: float, pool: float, net_sigma: float) -> float:
    """DISPLAY ONLY (not the resolution value): an 'effective difficulty' a UI may surface.
    Floored at the canonical Ob minimum.

    Resolution uses p_success (the mu-shift), which leaves base_Ob untouched and boosts
    the roll instead (post ED-884 / ED-934 ruling).
    """
    raw = base_ob - soft_cap(net_sigma) * sigma_n(pool)
    return max(float(OB_MIN), float(raw))           # [canonical: params/core.md §Obstacle Scale]


def effective_ob(base_ob: float, net_dsigma: float, pool: float) -> float:
    """Contest-surface signature for eff_ob.

    designs/audit/2026-06-03-contest-groundup/engine.py calls
    effective_ob(base_ob, net_dsigma, pool) — argument order differs from the
    combat eff_ob(base_ob, pool, net_sigma). This wrapper normalises the call.
    """
    return eff_ob(base_ob, pool, net_dsigma)


def net_boost(net_sigma: float, pool: float, tn: int = TN_STANDARD, capped: bool = True) -> float:
    """Advantage as an additive boost to the expected net (the μ-shift):
    eff_sigma * sigma_per_die[TN] * sqrt(N).

    The σ cancels in the z-score, so the modifier shifts the outcome's z by exactly
    eff_sigma at every pool size and every TN (uniform impact, TN-exact). This is the
    resolution-path modifier. [canonical: params/core.md §Continuous Engine]

    When tn=TN_STANDARD=7 (contest default, D0-3), the TN-independence of sigma_n
    and net_boost coincide (sigma_per_die[7] = 0.800 = SIGMA_N_COEFF = 0.8).
    """
    _, sigma = PER_DIE[tn]
    eff = soft_cap(net_sigma) if capped else net_sigma
    return eff * sigma * math.sqrt(max(1, pool))    # [canonical: params/core.md §Continuous Engine]


# ---------------------------------------------------------------------------
# Level lookup + aggregation
# ---------------------------------------------------------------------------

def level(name: str) -> float:
    """Single modifier-level → σ-value lookup (contest surface).

    Ported from designs/audit/2026-06-03-contest-groundup/engine.py:21
    (`def level(name): return LEVEL[name]`). That engine's LEVEL dict is this
    module's LEVEL_SIGMA (byte-identical values: minor 0.25 / moderate 0.50 /
    strong 0.75 / major 1.00), so this completes the contest surface the Stage-1a
    port began alongside sigma_N / eff_sigma / effective_ob.

    Consumer: designs/audit/2026-06-03-contest-groundup/primitives.py:9
    (`from engine import level`) evaluates `Leverage.ONGROUND = level('moderate')`
    at class-body import time; when that kernel is promoted into
    sim/personal/contest/ (Stage 1b) and re-pointed here, the name must resolve.
    """
    return LEVEL_SIGMA[name]


def levels_to_net_sigma(
    aggressor: Sequence[str] | None = None,
    defender: Sequence[str] | None = None,
) -> float:
    """Sum modifier levels into a net sigma value (pre-soft-cap):
    Sum(aggressor-favoring) - Sum(defender-favoring), in sigma-units.
    Levels are the player-facing abstraction in modifier_system_spec.md.
    """
    agg = sum(LEVEL_SIGMA[lv] for lv in (aggressor or []))
    dfd = sum(LEVEL_SIGMA[lv] for lv in (defender or []))
    return agg - dfd


# ---------------------------------------------------------------------------
# Probability helper (closed-form)
# ---------------------------------------------------------------------------

def _phi(z: float) -> float:
    """Standard normal CDF (stdlib erf path — no numpy)."""
    return (1.0 + math.erf(z / math.sqrt(2.0))) / 2.0


def p_success(
    base_ob: float,
    pool: float,
    net_sigma: float = 0.0,
    tn: int = TN_STANDARD,
    capped: bool = True,
) -> float:
    """P(net >= base_Ob) under the continuous engine, advantage applied as a μ-shift.

    The roll is boosted; base_Ob and TN are NOT modified, so the Ob floor is never
    breached:  shifted_mean = μ·N + net_boost ;  P = 1 - Φ((base_Ob - shifted_mean)/(σ·√N)).
    [canonical: params/core.md §Continuous Engine]
    """
    mu, sigma = PER_DIE[tn]
    shifted_mean = mu * pool + net_boost(net_sigma, pool, tn, capped)
    z = (base_ob - shifted_mean) / (sigma * math.sqrt(max(1, pool)))   # [canonical: params/core.md §Continuous Engine]
    return 1.0 - _phi(z)


# ---------------------------------------------------------------------------
# Rolling entry points (delegate to dice_engine — NO new die-roll path)
# ---------------------------------------------------------------------------

def roll_net(pool: float, tn: int = TN_STANDARD, rng: random.Random | None = None) -> int:
    """Discrete canonical d10 engine roll, delegating to dice_engine.roll_pool.

    Pool floored at 1D. [canonical: params/core.md §Die Rule (d10)]
    This sigma_leverage wrapper exists so callers that previously imported from
    m1_dice_sigma_core can switch to sim.autoload.sigma_leverage without a call-site
    change. The authoritative implementation is dice_engine.roll_pool.
    """
    effective_pool = max(1, int(round(pool)))       # [canonical: params/core.md §Pool Floor (all systems)]
    result = dice_engine.roll_pool(pool_size=effective_pool, tn=tn, rng=rng)
    return result.net


def roll_net_continuous(pool: float, tn: int = TN_STANDARD, rng: random.Random | None = None) -> float:
    """Continuous engine sample, delegating to dice_engine.continuous_engine_sample.

    Canonical for Godot; statistically equivalent to the discrete engine.
    [canonical: params/core.md §Continuous Engine, Decision E]
    """
    effective_pool = max(1, int(round(pool)))       # [canonical: params/core.md §Pool Floor (all systems)]
    return dice_engine.continuous_engine_sample(pool=float(effective_pool), tn=tn, rng=rng)
