"""
engine/dice_engine/sigma_leverage.py — σ-leverage advantage layer atop the d10 dice engine.

The σ-space layer of the one dice chain: the soft cap, the net boost, the level table and `band_odds`, the closed
form of the one sampler. The code is the source; the numbers are exported to `engine/engine_params/` by
`tools/export_sim_params.py`. (`params/core.md` and `modifier_system_spec.md`, once named here, are retired.)
Rationale:    D0-2 (the one σ-kernel for combat and social contest, which this module is)
Status:       the ruled owner, read by every provider; the code is the mechanism, this text is reference.

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
  • roll_net_continuous delegates to dice_engine (no new die-roll path)
  • PER_DIE / MU_PER_DIE / SD_PER_DIE are read from the owner dice_engine (one copy of the pair)
  • LEVEL_SIGMA / M_MAX / SIGMA_N_COEFF copied verbatim with provenance tags

Functions NOT ported from m1_dice_sigma_core:
  • _phi — reproduced here from the original's math.erf path (was already stdlib)
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
  - band_odds(pool: float, ob: float, boost: float = 0.0) -> (F, P, S, O)  (the Normal closed form of the one sampler, graded on BAND_FLOORS)
  - record_odds(pool, ob, leverage) -> (F, P, S, O)  (the same, over a contest record's fields, so a host names no boost arithmetic)
  - roll_net_continuous(pool: float, tn: int = TN_STANDARD, rng: random.Random | None = None) -> float
"""
from __future__ import annotations

import math
import random
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
# A situational TN scale ("Controlled 6 / Standard 7 / Desperate 8") is dead canon, and "all weapons
# are TN7" is subsumed: not just weapons, everything. A varying difficulty is an Ob, never a TN.
# See ED-IN-0196 and registers/supersession_register.yaml.
TN_STANDARD = 7         # [canonical: params/core.md §TN Values -- FORK: c451bcb]

# ---------------------------------------------------------------------------
# v32 σ-space modifier seeds (modifier_system_spec.md)
# Class B draft sim-seeds — sim-tunable, NOT canonical.
# ---------------------------------------------------------------------------
LEVEL_SIGMA = {
    "minor":    0.25,   # [canonical: modifier_system_spec.md §2.3 Player-facing abstraction]
    "moderate": 0.50,   # [canonical: modifier_system_spec.md §2.3 Player-facing abstraction]
    "strong":   0.75,   # [canonical: modifier_system_spec.md §2.3 Player-facing abstraction]
    "major":    1.00,   # [canonical: modifier_system_spec.md §2.3 Player-facing abstraction]
}

M_MAX = 1.5             # soft-cap ceiling, sigma-units   # [canonical: modifier_system_spec.md §3.1 Saturating function]
SIGMA_N_COEFF = 0.8     # sigma_N = 0.8 * sqrt(Pool)      # [canonical: modifier_system_spec.md §2.1 The transform]

# Contest engine surface constants (audit/2026-06-03-contest-groundup/engine.py)
OB_MIN = 1              # the floor a favourable modifier may not push an obstacle below (`eff_ob`; not an "Ob minimum" of a roll)

# Per-die stats (params/core.md §Expected Value): TN7 μ/σ per die. GENERAL, not contest-specific
# — the contest's de-saturation extension reads them from here (ED-SC-0032).
MU_PER_DIE = dice_engine.MU_PER_DIE        # alias of the owner (engine/dice_engine/dice_engine.py)
SD_PER_DIE = dice_engine.SIGMA_PER_DIE     # alias of the owner; the owner's name is SIGMA_PER_DIE
# OVERWHELM_SIGMA lives in systems/social_contest/sim/contest/degree_extension.py (ED-SC-0032): it
# is a contest constant and belongs with the extension that reads it.


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


def saturate(x: float, m: float) -> float:
    """`m * tanh(x / m)`: nearly `x` for small `x`, approaching `m` for large; no hard ceiling and no
    dead-zone. The one saturating function: `soft_cap` is it at `M_MAX`, and the social obstacle's
    bound is it over the span between the fixed ceiling and the pool's cap."""
    return m * math.tanh(x / m)


def soft_cap(net_sigma: float) -> float:
    """Smooth saturating cap: M*tanh(net/M).

    Small sums apply nearly fully; large sums saturate toward ±M_MAX;
    no hard ceiling and no dead-zone.
    [canonical: modifier_system_spec.md §3.1 Saturating function]
    """
    return saturate(net_sigma, M_MAX)     # [canonical: modifier_system_spec.md §3.1 Saturating function]


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
    return eff * sigma * math.sqrt(max(0.0, pool))  # [canonical: params/core.md §Continuous Engine] the pool as it is: one rule below one die (DOE §1 row 5)


def opposed_ob(score: float, rate: float) -> float:
    """The opposition as an obstacle: `rate` times the opposing SKILL SCORE (floored at 0).

    The operand is a skill score, never a pool (A-26, A-71). `rate` has no default: a caller
    names the rate it opposes at, and a missing one is a TypeError, not a silent 1.0.
    """
    return float(rate) * max(0.0, float(score))


def even_line(pool_add: float) -> float:
    """The even line: the pool's expected net, `MU_PER_DIE` (the owner's mean per die) times
    the pool's base `pool_add` (A-26, A-71). An obstacle at this line is an even contest."""
    return MU_PER_DIE * float(pool_add)


def pool_of(score: float, addends: float, pool_add: float, pool_floor: int) -> float:
    """The pool rule: `max(pool_floor, score + addends + pool_add)` (A-6; D-U1-08).

    One owner for how a skill score, the rolled addends and the row's pool addition make a
    pool, floored at the row's `pool_floor`.
    """
    return max(pool_floor, score + addends + pool_add)


def governing_mean(scores) -> float:
    """A verb's GOVERNING SCORE (B05.24, `ED-IN-0379`; Jordan, 2026-11-13): *a verb names one to three attributes; his
    governing score for it is the average of his scores in them (an attribute he does not hold counts at the untrained score
    `pool_default`), rounded to the nearest tenth, a value halfway between two tenths rounding up; the result is a
    fractional number (2.5, not 3) and feeds the dice as a fractional pool, as the engine already takes one (A-5); his rank
    in the verb's skill, if the verb names one, is added (`pool.py::faculty`).*

    `(20 * sum + n) // (2 * n) / 10`: the sum is taken in exact integers (attribute scores are integers on
    `descriptors.ATTRIBUTE_FLOOR` to `ATTRIBUTE_CEILING`) and only the last division is a float, so no float noise enters
    the rounding. The result is NOT a whole number and does not use `round_half_up` (B38.55's, for integer counts).
    For `n` of 1 to 3 the mean of integers is a multiple of a third, so a true half-tenth never occurs and the half-up
    clause is vacuous at this input. [ASSUMPTION: scores stay integers; if the tree ever holds fractional attribute scores,
    hold them in tenths and sum in tenths: `(2 * sum_tenths + n) // (2 * n) / 10`.]
    Refuses `n` outside 1 to 3 and a negative score."""
    scores = list(scores)
    n = len(scores)
    if not 1 <= n <= 3:
        raise ValueError(f"governing_mean takes one to three attribute scores, got {n}")
    if any(s < 0 for s in scores):
        raise ValueError(f"governing_mean takes no negative score, got {scores}")
    # [canonical: proposals/2026-11-12-subsystem-audit-suite/proposals/2026-11-13-verb-governing-attributes.md §0 (ED-IN-0379): the tenth, taken as 20 half-tenths a point]
    return (20 * sum(scores) + n) // (2 * n) / 10


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
    share one table.
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

    THE POOL IS TAKEN AS IT IS FOR `pool > 0` (DOE §1 row 5): mean and spread both scale with the pool, as the
    sampler `roll_net_continuous` draws them, so the closed form and the draw are one rule at every size. This
    is the one-band case of `band_odds` (the band edge unquantised). CONTROL: no pool below 1D reaches it from a
    person, and at and above 1D the result is what it was, so the parity goldens (no row carries a sub-1D pool)
    are unmoved.
    """
    mu, sigma = PER_DIE[tn]
    effective_pool = float(pool)
    if effective_pool <= 0:                          # no pool rolls nothing: the net is 0 (the sampler's own)
        return 1.0 if 0.0 >= base_ob else 0.0
    shifted_mean = mu * effective_pool + net_boost(net_sigma, effective_pool, tn, capped)
    z = (base_ob - shifted_mean) / (sigma * math.sqrt(effective_pool))   # [canonical: params/core.md §Continuous Engine]
    return 1.0 - _phi(z)


# ---------------------------------------------------------------------------
# Band odds of the roll (B05.02): the closed form of the one sampler
# ---------------------------------------------------------------------------

def _at_or_above(pool: float, ob: float, boost: float, floor: int) -> float:
    """P(the roll's margin, quantised once at the ladder, reaches `floor`): the roll is the one sampler's
    Normal(MU_PER_DIE * pool, SIGMA_PER_DIE * sqrt(pool)) plus `boost`; the ladder reads
    `round(MARGIN_SCALE * (net - ob))` against the integer `floor` (`dice_engine.degree_from_net`), which is the real
    margin reaching `(floor - 0.5) / MARGIN_SCALE`. No pool at all rolls nothing: the net is the boost alone."""
    edge = (floor - 0.5) / dice_engine.MARGIN_SCALE
    if pool <= 0:
        return 1.0 if boost - ob >= edge else 0.0
    mean = dice_engine.MU_PER_DIE * pool + boost
    sd = dice_engine.SIGMA_PER_DIE * math.sqrt(pool)
    return 1.0 - _phi((ob + edge - mean) / sd)


def band_odds(pool: float, ob: float, boost: float = 0.0) -> tuple:
    """`(F, P, S, O)`: the chance of each of the four bands -- in the owner's order, the ordinals of
    `dice_engine.DEGREE_ORDINAL` -- for one roll of `pool` against `ob`, the roll shifted by `boost`.

    THE NORMAL CLOSED FORM OF THE ONE SAMPLER (A-5; DOE §1 row 2), `dice_engine.continuous_engine_sample`: mean
    `MU_PER_DIE * pool` plus the boost, spread `SIGMA_PER_DIE * sqrt(pool)`, the pool as it is for `pool > 0`.
    The band edges are `dice_engine.BAND_FLOORS`, read from the owner's table in its milli-units, so a change to
    the ladder's table moves this tuple with the roll (the test mutates it). The boost is the mu-shift and the
    obstacle is untouched -- never an Ob reduction.

    A SAMPLED CLAIM, NOT AN ENUMERATION: `engine/tests/test_band_odds.py` checks it against the sampler at a stated
    n and tolerance. Pure and read-only; the four bands sum to 1 by construction."""
    floors = dice_engine.BAND_FLOORS
    partial = _at_or_above(pool, ob, boost, floors["partial"])
    success = _at_or_above(pool, ob, boost, floors["success"])
    overwhelming = _at_or_above(pool, ob, boost, floors["overwhelming"])
    by_band = {dice_engine.Degree.FAILURE: 1.0 - partial, dice_engine.Degree.PARTIAL: partial - success,
               dice_engine.Degree.SUCCESS: success - overwhelming, dice_engine.Degree.OVERWHELMING: overwhelming}
    return tuple(by_band[d] for d, _ in sorted(dice_engine.DEGREE_ORDINAL.items(), key=lambda kv: kv[1]))


def record_odds(pool: float, ob: float, leverage: float) -> tuple:
    """`band_odds` for a contest RECORD's own fields: its pool, its composed obstacle and its leverage
    (net sigma), the boost being the roll's own `net_boost(leverage, pool)`. The host reads a record and
    names no arithmetic: the boost the roll adds is derived HERE, by the owner of `net_boost`, so the
    odds shown are the odds of the roll dealt."""
    return band_odds(pool, ob, net_boost(leverage, pool))


# ---------------------------------------------------------------------------
# Rolling entry point (delegates to dice_engine — NO new die-roll path)
# ---------------------------------------------------------------------------

def roll_net_continuous(pool: float, tn: int = TN_STANDARD, rng: random.Random | None = None) -> float:
    """The sampler every provider draws from (ED-833; Jordan, 2026-11-12). Same mean and variance as the d10
    face rule it is derived from.

    Delegates to `dice_engine.continuous_engine_sample`, which takes the pool as it is for `pool > 0` (fractional
    dice, Jordan 2026-08-14; below one die one rule, DOE §1 row 5: no floor at one die here) and rolls nothing
    for a pool of nothing. Its closed form is `band_odds`.

    BLAST RADIUS, because subsystems share this entry point (§0.1 pt 4 -- a number without a control is not a
    measurement): personal combat (`modules/combat/core.py`) draws it with pools at and above its own floor, so
    nothing moves there and its byte-exact goldens are the CONTROL; the social roll moved to it at B05.02.
    """
    return dice_engine.continuous_engine_sample(pool=float(pool), tn=tn, rng=rng)


# ---------------------------------------------------------------------------
# Contest-surface degree — NOT IN THIS MODULE (ED-SC-0032)
# ---------------------------------------------------------------------------
# `degree(net, ob, pool)`, `overwhelm_bar`, `crossover_pool` and `OVERWHELM_SIGMA` are at
# `systems/social_contest/sim/contest/degree_extension.py`: the pool-aware de-saturation is ONE
# SUBSYSTEM'S rule, injected through the seam `dice_engine.BandExtension`.
#
# WHAT TO CALL INSTEAD: `dice_engine.degree_from_net(net, ob, extension=..., **context)` for the
# ladder, and the contest package's own `degree()` adapter if you want the ordinal with the
# contest's extension applied. Nothing in `engine/` should reach for the second.
#
# The MU/SD per-die constants stay here: those ARE general, and the extension reads them from
# this module.
