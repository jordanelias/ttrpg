"""
engine/dice_engine/sigma_leverage.py — σ-leverage advantage layer atop the d10 dice engine.
(The header read `sim/autoload/...` until 2026-08-27; that tree was retired 2026-07-21.)

Canon source: modifier_system_spec.md (the implementation-pass rewrite)
Params source: params/core.md, modifier_system_spec.md
Game Design constraints applicable: none — σ-space resolution math (GD-1..3 govern game-layer mechanics, not dice math)
Rationale:    D0-2 (audit/2026-06-30-contest-stage0-reconciliation/DECISIONS.md)
Status:       [CANONICAL — Stage 1a port 2026-06-30]

Purpose
-------
Single-source the σ-leverage modifier layer for BOTH combat and social-contest, retiring:
  • the test-dir dependency (tests/sim/v32-combat-balance/m1_dice_sigma_core.py)
  • the numpy dependency that file carried
  • the combat sys.path.insert hack (formerly systems/combat/combat_engine_v1/core.py:3; the file is now modules/combat/core.py)
  • the distillation report's "two σ-kernels" debt

Separation of concerns (D0-2):
  dice_engine  = pool / degree primitive (stdlib root, no deps)
  sigma_leverage = advantage→μ-shift layer atop it (this module)

Dependencies: stdlib only (math, random) + engine.dice_engine.dice_engine.
              numpy is NOT imported — stdlib math.tanh / math.sqrt are used throughout.

Porting notes
-------------
All numerical behaviour is byte-identical to m1_dice_sigma_core.py:
  • tanh via math.tanh (CPython delegates to libm, same IEEE-754 result)
  • sqrt via math.sqrt (same)
  • roll_net / roll_net_continuous delegate to dice_engine (no new die-roll path)
  • PER_DIE / MU_PER_DIE / SD_PER_DIE are read from the owner dice_engine (one copy of the pair)
  • LEVEL_SIGMA / M_MAX / SIGMA_N_COEFF copied verbatim with provenance tags

Functions NOT ported from m1_dice_sigma_core:
  • _phi — reproduced here from the original's math.erf path (was already stdlib)
  • roll_net — delegates to dice_engine.roll_pool (integer net)
  • roll_net_continuous — delegates to dice_engine.continuous_engine_sample

Functions added (contest surface, audit/2026-06-03-contest-groundup/engine.py):
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
  - band_odds(pool: float, ob: float, boost: float = 0.0) -> (F, P, S, O)  (exact odds of the discrete roll, CP-T01-03)
  - settle_margin(raw_net: int, boost: float, ob: float, uniform) -> int  (the fraction of a margin, CP-T01-04)
  - record_odds(pool, ob, leverage) -> (F, P, S, O) and settle_record(net, leverage, pool, ob, uniform) -> int
    (the same two, over a contest record's fields, so a host names no boost arithmetic)
  - roll_net(pool: float, tn: int = TN_STANDARD, rng: random.Random | None = None) -> int
  - roll_net_continuous(pool: float, tn: int = TN_STANDARD, rng: random.Random | None = None) -> float
"""
from __future__ import annotations

import functools
import math
import random
from fractions import Fraction
from typing import Sequence

from engine.dice_engine import dice_engine

# ---------------------------------------------------------------------------
# Canonical per-die statistics (params/core.md "Expected Value (per die)")
# TN → (mu_per_die, sigma_per_die)
# [canonical: params/core.md §Expected Value (per die)]
# ---------------------------------------------------------------------------
# Kept as a dict keyed by TN, deliberately: `net_boost` and `p_success` index PER_DIE[tn], so a
# stray non-7 tn now fails LOUDLY with a KeyError instead of silently resolving to a TN 6 or TN 8
# row. The TN 6/8 rows are deleted under the ruling below.
PER_DIE: dict[int, tuple[float, float]] = {
    7: (dice_engine.MU_PER_DIE, dice_engine.SIGMA_PER_DIE),   # [canonical: params/core.md §Expected Value (per die)]; read from the owner, never copied
}

# TN 7 MEANS "A FACE OF 7 OR HIGHER SUCCEEDS" — equivalently, "roll above 6". Both readings are
# the same rule and both are in circulation; RULED 2026-08-15 (Jordan: "TN7, roll of 7 or higher is
# success") so the ambiguity stops here rather than being re-derived. The die rule it indexes:
# face 1 = -1 success, 2-6 = 0, 7-9 = +1, 10 = +2.
# ⚠ TN IS 7. ALWAYS. THERE IS NO OTHER TN.
# [Jordan, 2026-08-25, verbatim: "TN7 always. Never change TN anywhere ever."]
# This SUPERSEDES the 2026-08-15 situational scale that stood here — "Controlled 6 / Standard 7 /
# Desperate 8, selected by SITUATION" — which is now dead canon. The earlier half of that same
# ruling ("all weapons are TN7") is subsumed: not just weapons, everything. A varying difficulty
# is an Ob, never a TN. See ED-IN-0196 and registers/supersession_register.yaml.
TN_STANDARD = 7         # [canonical: params/core.md §TN Values -- FORK: c451bcb]

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

# Contest engine surface constants (audit/2026-06-03-contest-groundup/engine.py)
OB_MIN = 1              # [canonical: params/core.md §Obstacle Scale]

# Per-die stats (params/core.md §Expected Value): TN7 μ/σ per die. GENERAL, not contest-specific
# — the contest's de-saturation extension reads them from here (ED-SC-0032).
MU_PER_DIE = dice_engine.MU_PER_DIE        # alias of the owner (engine/dice_engine/dice_engine.py)
SD_PER_DIE = dice_engine.SIGMA_PER_DIE     # alias of the owner; the owner's name is SIGMA_PER_DIE
# OVERWHELM_SIGMA MOVED 2026-08-27 (ED-SC-0032) to
# systems/social_contest/sim/contest/degree_extension.py. It is a contest constant — its own
# citation is the contest groundup engine — and it belongs with the extension that reads it.


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

    audit/2026-06-03-contest-groundup/engine.py names this sigma_N;
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

    audit/2026-06-03-contest-groundup/engine.py names this eff_sigma;
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

    audit/2026-06-03-contest-groundup/engine.py calls
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
    """σ-value for a named modifier level (minor/moderate/strong/major) — contest surface.

    Ported from audit/2026-06-03-contest-groundup/engine.py:21
    (`def level(name): return LEVEL[name]`); that engine's LEVEL dict is this module's
    LEVEL_SIGMA (byte-identical: minor 0.25 / moderate 0.50 / strong 0.75 / major 1.00).
    Single-sources LEVEL_SIGMA so combat (levels_to_net_sigma) and contest
    (Leverage.ONGROUND = level("moderate"), groundup primitives.py:9 at import time)
    share one table. Stage-1a finding 1a: this accessor was missing from the port.
    [canonical: modifier_system_spec.md §2.3 Player-facing abstraction]
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

    THE POOL FLOOR APPLIES TO THE MEAN AS WELL AS THE VARIANCE (Jordan, 2026-09-04: "1D is
    floor"). This line read `mu * pool` against `sqrt(max(1, pool))` — flooring the SPREAD but
    not the LOCATION, so below 1D the closed form drifted away from the sampler that
    `roll_net_continuous` actually draws from, which floors both via
    `effective_pool = max(1.0, float(pool))`. Two flooring conventions in one module.
    Measured before the fix, base_Ob 1.0, net_sigma 0, 200k draws, seed 7:
        pool 0.25 -> p_success 0.1303 vs sampled 0.2275   (9.7 pp apart)
        pool 0.50 -> p_success 0.1587 vs sampled 0.2275   (6.9 pp apart)
        pool 1.00 -> p_success 0.2266 vs sampled 0.2275   (Monte-Carlo noise)
    CONTROL: no golden row carries a sub-1D pool (p_success pools are 1/5/10/26), and
    max(1.0, pool) == pool for every one of them, so this is VALUE-IDENTICAL at and above 1D
    and the byte-exact parity goldens are what proves it. The bug was inherited verbatim from
    m1_dice_sigma_core.p_success, which the Stage-1a port copied byte-for-byte; that copy is
    fixed in the same commit so the two stay byte-identical.
    [canonical: params/core.md §Pool Floor (all systems)]
    """
    mu, sigma = PER_DIE[tn]
    effective_pool = max(1.0, float(pool))          # [canonical: params/core.md §Pool Floor (all systems)]
    shifted_mean = mu * effective_pool + net_boost(net_sigma, effective_pool, tn, capped)
    z = (base_ob - shifted_mean) / (sigma * math.sqrt(effective_pool))   # [canonical: params/core.md §Continuous Engine]
    return 1.0 - _phi(z)


# ---------------------------------------------------------------------------
# Exact band odds of the DISCRETE roll (CP-T01-03)
# ---------------------------------------------------------------------------

@functools.lru_cache(maxsize=None)
def _net_counts(dice: int) -> tuple:
    """How many of the 10**dice face combinations deal each net, as sorted (net, count) pairs.

    The per-die net comes from the owner's face table, `dice_engine._die_result`, called once per
    face; the d10 is `roll_pool`'s own `rng.randint(1, 10)`. The pool's net is the sum over dice, so
    the counts are an integer convolution -- exact, and no floating error enters until the division."""
    per_die = [dice_engine._die_result(face) for face in range(1, 11)]      # roll_pool deals 1..10
    counts = {0: 1}
    for _ in range(dice):
        step: dict[int, int] = {}
        for net, n in counts.items():
            for r in per_die:
                step[net + r] = step.get(net + r, 0) + n
        counts = step
    return tuple(sorted(counts.items()))


def _split_margin(boost: float, ob: float) -> tuple:
    """`(whole, fraction)` of `boost - ob`: its floor and what is left (`0.0 <= fraction < 1.0`).
    The one place the rule's two parts are cut, read by `settle_margin` and by `band_odds`."""
    q = boost - ob
    whole = math.floor(q)
    return whole, q - whole


def settle_margin(raw_net: int, boost: float, ob: float, uniform) -> int:
    """THE FRACTION OF A MARGIN IS WORTH ITS FRACTION (CP-T01-04): the whole margin the ladder reads.

    `raw_net` is the roll's own integer net (`roll_net`), `boost` the mu-shift it was given
    (`net_boost`), `ob` the composed obstacle, and `uniform` the act's OWN generator's `random`, a
    zero-argument callable. With `q = boost - ob` the settled margin is
        raw_net + floor(q) + [u < frac(q)]
    an integer, so the ladder reads it against a zero obstacle (`degree_from_net(m, 0)`). Expected margin
    is `raw_net + q`, unrounded: advantage stays a mu-shift in expectation, and two obstacles a fraction
    apart (or two boosts) differ in their odds, which whole dice alone collapse.

    `uniform` IS CALLED ONLY WHEN `frac(q) > 0`. A whole margin (every whole-Ob roll with no boost, which
    is the whole realm) draws nothing, so the act's stream, and every hash behind it, is unmoved; the
    rule is then the identity, `raw_net + q`. Base Ob and TN are never modified: the obstacle is only the
    fraction's source. Pure but for that one call."""
    whole, fraction = _split_margin(boost, ob)
    if fraction > 0.0 and uniform() < fraction:
        whole += 1
    return int(raw_net) + whole


def band_odds(pool: float, ob: float, boost: float = 0.0) -> tuple:
    """`(F, P, S, O)`: the exact chance of each of the four bands -- in the owner's order, the
    ordinals of `dice_engine.DEGREE_ORDINAL` -- for one roll of `pool` d10s against `ob`, the roll
    shifted by `boost`, its margin settled by `settle_margin`.

    AN ENUMERATION OF THE DEALT ROLL, NOT A MODEL OF IT. The net of the pool is enumerated over
    `dice_engine._die_result`'s own faces; each net is settled by THE SAME RULE `settle_margin` deals
    (`_split_margin`: the whole part with certainty, one more with probability `frac`) and graded by
    `dice_engine.degree_from_net`, the one ladder. Neither the faces, the ladder nor the rule is copied
    here, so a change to any of them moves this tuple with the roll (the tests swap a band edge, and
    walk the face table through `settle_margin` itself). The boost is the mu-shift and the obstacle is
    untouched -- never an Ob reduction.

    `pool` is rounded and floored as `roll_net` deals it (`max(1, int(round(pool)))` whole dice), so
    the odds are for the dice dealt. `p_success` stays the Gaussian closed form combat reads; on these
    dice it is 10-15 points off, which is why this exists. Pure and read-only; the result is a tuple of
    floats (a count over 10**dice, a whole margin weighing exactly 1), so
    `band_odds(2, 2) == (0.74, 0.19, 0.07, 0.0)` exactly."""
    dice = max(1, int(round(pool)))                 # [canonical: params/core.md §Pool Floor (all systems)]
    whole, fraction = _split_margin(boost, ob)
    pays = Fraction(fraction)                       # exact, so the four bands sum to 1 and none exceeds it
    tally = [Fraction(0)] * 4
    for net, n in _net_counts(dice):
        if fraction > 0.0:
            tally[dice_engine.DEGREE_ORDINAL[dice_engine.degree_from_net(net + whole, 0)]] += n * (1 - pays)
            tally[dice_engine.DEGREE_ORDINAL[dice_engine.degree_from_net(net + whole + 1, 0)]] += n * pays
        else:
            tally[dice_engine.DEGREE_ORDINAL[dice_engine.degree_from_net(net + whole, 0)]] += n
    total = 10 ** dice
    return tuple(float(n / total) for n in tally)


def record_odds(pool: float, ob: float, leverage: float) -> tuple:
    """`band_odds` for a contest RECORD's own fields: its pool, its composed obstacle and its leverage
    (net sigma), the boost being the roll's own `net_boost(leverage, pool)`. The host reads a record and
    names no arithmetic: the boost the roll adds is derived HERE, by the owner of `net_boost`, so the
    odds shown are the odds of the roll dealt (`band_odds` is the one enumeration)."""
    return band_odds(pool, ob, net_boost(leverage, pool))


def settle_record(net: float, leverage: float, pool: float, ob: float, uniform) -> int:
    """`settle_margin` for the net an entry RETURNED: `net` is the integer roll plus the boost it was
    given (`net_boost(leverage, pool)`), so the roll is that net less the boost, rounded back to the
    whole it is. The host passes the record's fields and the act's `uniform`; the boost and the roll
    are derived here, by the owner, and the fraction rule stays `settle_margin`'s alone."""
    boost = net_boost(leverage, pool)
    return settle_margin(round(net - boost), boost, ob, uniform)


# ---------------------------------------------------------------------------
# Rolling entry points (delegate to dice_engine — NO new die-roll path)
# ---------------------------------------------------------------------------

def roll_net(pool: float, tn: int = TN_STANDARD, rng: random.Random | None = None) -> int:
    """Discrete canonical d10 engine roll, delegating to dice_engine.roll_pool.

    Pool floored at 1D. [canonical: params/core.md §Die Rule (d10)]
    This sigma_leverage wrapper exists so callers that previously imported from
    m1_dice_sigma_core can switch to engine.dice_engine.sigma_leverage without a call-site
    change. The authoritative implementation is dice_engine.roll_pool.
    """
    effective_pool = max(1, int(round(pool)))       # [canonical: params/core.md §Pool Floor (all systems)]
    result = dice_engine.roll_pool(pool_size=effective_pool, tn=tn, rng=rng)
    return result.net


def roll_net_continuous(pool: float, tn: int = TN_STANDARD, rng: random.Random | None = None) -> float:
    """Continuous engine sample, delegating to dice_engine.continuous_engine_sample.

    Canonical for Godot; statistically equivalent to the discrete engine.
    [canonical: params/core.md §Continuous Engine, Decision E]

    THE POOL IS FRACTIONAL HERE (M1 juncture 1, 2026-08-21). Jordan ruled "fractional dice" on
    2026-08-14 and only the fractional RESULT had been implemented: this line read
    `max(1, int(round(pool)))`, so a 3.5-die pool was sampled as a 4-die pool. The rounding was
    imposed by THIS CALLER ALONE — `dice_engine.continuous_engine_sample` has always accepted a
    fractional pool and says so at `dice_engine.py:92`, computing `mu*pool` and `sigma*sqrt(pool)`
    with no quantisation. ED-IN-0187 recorded the gap and it was written into the ledger without
    being applied here, which `systems/factions/sim/faction_action.py` called out as worse than an
    unimplemented feature because the call site asserted the opposite.

    THE FLOOR STAYS AT 1D and is canon, not caution — `params/core.md §Pool Floor (all systems)`.
    What goes is the rounding, not the floor.

    `roll_net` above is the DISCRETE d10 path and keeps `int(round(pool))`: whole dice are correct
    there, because it deals actual dice rather than sampling their limit distribution.

    MEASURED BLAST RADIUS, because two subsystems share this entry point (§0.1 pt 4 — a number
    without a control is not a measurement):
      * faction strategic actions — 4-season seeded campaign, 40 calls, **20 already fractional**
        (4.3, 4.6, 4.9, 5.3, 5.5, …), every one silently rounded before this change. These MOVE.
      * personal combat, via `modules/combat/core.py:56` — 749 calls driven
        through `workbench.balance.winrate` at n=120, **749 integral, 0 fractional**, because
        `core.resolution_pool()` returns `max(POOL_FLOOR, int(round(history)) + BASE_POOL)` and no
        call site modifies it. `int(round(n)) == n` for integral n, so combat is value-identical
        and its byte-exact goldens are the CONTROL: if they move, this change did something it
        was not meant to.
    """
    effective_pool = max(1.0, float(pool))          # [canonical: params/core.md §Pool Floor (all systems)]
    return dice_engine.continuous_engine_sample(pool=effective_pool, tn=tn, rng=rng)


# ---------------------------------------------------------------------------
# Contest-surface degree — RETIRED FROM THIS MODULE 2026-08-27 (ED-SC-0032)
# ---------------------------------------------------------------------------
# `degree(net, ob, pool)`, `overwhelm_bar`, `crossover_pool` and `OVERWHELM_SIGMA` lived here and
# are now at `systems/social_contest/sim/contest/degree_extension.py`. They were never general:
# the pool-aware de-saturation is ONE SUBSYSTEM'S rule, and OVERWHELM_SIGMA's own citation says
# so (`audit/2026-06-03-contest-groundup/engine.py §degree`). The engine carrying it was half of
# what made Jordan's 2026-08-15 ruling unsatisfied — the other half being that there was no seam,
# which `dice_engine.BandExtension` now is.
#
# WHAT TO CALL INSTEAD: `dice_engine.degree_from_net(net, ob, extension=..., **context)` for the
# ladder, and the contest package's own `degree()` adapter if you want the ordinal with the
# contest's extension applied. Nothing in `engine/` should reach for the second.
#
# The MU/SD per-die constants stay here: those ARE general, and the extension reads them from
# this module.
