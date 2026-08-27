"""
engine/autoload/sigma_leverage.py — σ-leverage advantage layer atop the d10 dice engine.
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
  • the combat sys.path.insert hack (systems/combat/combat_engine_v1/core.py:3)
  • the distillation report's "two σ-kernels" debt

Separation of concerns (D0-2):
  dice_engine  = pool / degree primitive (stdlib root, no deps)
  sigma_leverage = advantage→μ-shift layer atop it (this module)

Dependencies: stdlib only (math, random) + engine.autoload.dice_engine.
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
  - roll_net(pool: float, tn: int = TN_STANDARD, rng: random.Random | None = None) -> int
  - roll_net_continuous(pool: float, tn: int = TN_STANDARD, rng: random.Random | None = None) -> float
  - degree(net: float, ob: float, pool: float | None = None) -> int  (the owner's ladder + one extension)
"""
from __future__ import annotations

import math
import random
from typing import Sequence

from engine.autoload import dice_engine

# ---------------------------------------------------------------------------
# Canonical per-die statistics (params/core.md "Expected Value (per die)")
# TN → (mu_per_die, sigma_per_die)
# [canonical: params/core.md §Expected Value (per die)]
# ---------------------------------------------------------------------------
# Kept as a dict keyed by TN, deliberately: `net_boost` and `p_success` index PER_DIE[tn], so a
# stray non-7 tn now fails LOUDLY with a KeyError instead of silently resolving to a TN 6 or TN 8
# row. The TN 6/8 rows are deleted under the ruling below.
PER_DIE: dict[int, tuple[float, float]] = {
    7: (0.40, 0.800),   # [canonical: params/core.md §Expected Value (per die)]
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

# Contest-surface per-die stats (params/core.md §Expected Value): TN7 μ/σ per die.
# The contest degree() Overwhelming bar is pool-aware (see degree() below).
MU_PER_DIE = 0.40       # [canonical: params/core.md §Expected Value (per die), TN7]
SD_PER_DIE = 0.80       # [canonical: params/core.md §Expected Value (per die), TN7]
# De-saturation bar (contest diagnostic Lesson 2, groundup engine.py): live degree-3 bar
# = pool mean + OVERWHELM_SIGMA·σ, holding the Overwhelming rate ~uniform across pool sizes.
OVERWHELM_SIGMA = 0.85  # [canonical: audit/2026-06-03-contest-groundup/engine.py §degree]


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
    m1_dice_sigma_core can switch to engine.autoload.sigma_leverage without a call-site
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
      * personal combat, via `systems/combat/combat_engine_v1/core.py:56` — 749 calls driven
        through `workbench.balance.winrate` at n=120, **749 integral, 0 fractional**, because
        `core.resolution_pool()` returns `max(POOL_FLOOR, int(round(history)) + BASE_POOL)` and no
        call site modifies it. `int(round(n)) == n` for integral n, so combat is value-identical
        and its byte-exact goldens are the CONTROL: if they move, this change did something it
        was not meant to.
    """
    effective_pool = max(1.0, float(pool))          # [canonical: params/core.md §Pool Floor (all systems)]
    return dice_engine.continuous_engine_sample(pool=effective_pool, tn=tn, rng=rng)


# ---------------------------------------------------------------------------
# Contest-surface degree (pool-aware integer bands)
# ---------------------------------------------------------------------------

# Read off the owner rather than written as literals, so the two encodings cannot drift.
_SUCCESS = dice_engine.DEGREE_ORDINAL[dice_engine.Degree.SUCCESS]
_OVERWHELMING = dice_engine.DEGREE_ORDINAL[dice_engine.Degree.OVERWHELMING]


def overwhelm_bar(pool: float) -> float:
    """The contest extension's de-saturation bar at a pool size. ONE definition.

    Exposed rather than inlined in `degree` because three tests and `tools/balance_oracle.py`
    need it, and each of them re-deriving `MU_PER_DIE*pool + OVERWHELM_SIGMA*SD_PER_DIE*sqrt(...)`
    is how a guard drifts from the thing it guards (CLAUDE.md §8).

    `max(1, pool)` floors only the sqrt term, not the mean term — carried over verbatim from the
    retired implementation. It makes no difference for any reachable pool (the live floor is
    `Pool.size`, which is >= 5) and is kept rather than silently "fixed", since changing it would
    be a behaviour change wearing a tidy-up's clothes.
    """
    return MU_PER_DIE * pool + OVERWHELM_SIGMA * SD_PER_DIE * math.sqrt(max(1, pool))


def crossover_pool(ob: float, limit: int = 200) -> int | None:
    """Smallest integer pool at which the extension can demote, for this `ob`. None if never.

    The extension bites exactly when its bar exceeds the owner's Overwhelming bar `ob + 3`, so
    the crossover MOVES WITH THE OBSTACLE: ob 1.0 -> 6, ob 2.0 -> 8, ob 3.0 -> 10. Tests used to
    hard-code 8, which was a measurement of `resolver.py`'s default ob presented as a contract.
    """
    owner_bar = ob + _OVERWHELMING_MARGIN
    for pool in range(1, limit + 1):
        if overwhelm_bar(pool) > owner_bar:
            return pool
    return None


#: The owner's Overwhelming margin, DERIVED rather than typed: the smallest whole margin
#: `degree_from_net` bands Overwhelming. Reading it off the owner means a future change to the
#: ladder moves this with it instead of leaving a stale literal in a helper.
_OVERWHELMING_MARGIN = next(
    m / 4 for m in range(0, 41)
    if dice_engine.degree_from_net(m / 4, 0.0) is dice_engine.Degree.OVERWHELMING
)


def degree(net: float, ob: float, pool: float | None = None) -> int:
    """Contest-surface degree: the OWNER'S ladder, plus one declared extension (ED-SC-0031).

    MIGRATED 2026-08-27. This was the ninth ladder — and the one the 2026-08-12 degree-vocabulary
    census missed entirely, despite it sitting in the same package as the owner. It returned its
    own bands from its own `if` chain, and two of its three lower boundaries contradicted the
    2026-08-14 ruling outright: `net == ob` returned Success where the ruling says Partial, and
    `0 < net < ob` returned Partial where it says Failure.

    WHAT AUTHORISES THE SHAPE BELOW, quoted rather than inferred. Jordan, 2026-08-15:

        "systems should not need different degree bands. it should be consistent in application.
         if a system does require any modification or extension, then the wrapper needs to inject
         the engine in such a manner that it can be modified cleanly."

    So the BANDS are `dice_engine.degree_from_net`'s, with no local re-decision — and the contest's
    pool-aware requirement survives as an EXPLICIT, NAMED EXTENSION over that result rather than as
    a private re-banding. The extension can only ever DEMOTE Overwhelming to Success; it cannot
    promote, cannot move any other boundary, and cannot be reached at all when `pool` is None. That
    is the narrowest form the extension can take and still do its job, which is why it is the one
    chosen: an extension that could move a lower boundary would be the old ladder wearing a
    different name.

    WHY THE EXTENSION EXISTS AND IS NOT DELETED WITH THE REST. The bar is
    `MU_PER_DIE*pool + OVERWHELM_SIGMA*SD_PER_DIE*sqrt(pool)` — roughly "beat your own pool's mean
    by 0.85 sigma". Without it the Overwhelming rate SATURATES as pools grow: a large pool clears a
    fixed margin almost every roll, so at high pool nearly every contest resolves Overwhelming and
    the band stops discriminating. The contest kernel uses the degree as a numeric magnitude in
    `resolver._advance`, so a saturating top band collapses the whole track.

    WHERE IT BINDS IS A FUNCTION OF `ob`, NOT THE CONSTANT "pool 8" AN EARLIER DRAFT CLAIMED.
    The extension is inert exactly while `bar(pool) <= ob + 3`, so the crossover moves with the
    obstacle: ob 1.0 -> binds from pool 6, ob 2.0 -> pool 8, ob 3.0 -> pool 10. The tests measured
    ob 2.0 and the docstring generalised from one obstacle; `crossover_pool()` below computes it
    instead, and the tests now sweep several. It happens to be pool 8 in the live campaign only
    because `resolver.py:155` declares `base_ob: float = 2.0` and passes it unmodified — a
    coincidence of one default, and `sigma_leverage.OB_MIN` is 1, which is reachable through
    `eff_ob`'s floor.

    ⚠ A GAME-FACING COST OF THE RULING, recorded because it is real and runs against the stated
    design goal. The bar was chosen (groundup "diagnostic Lesson 2") to hold the Overwhelming rate
    ~uniform ACROSS POOL SIZES. Under the owner's ladder that uniformity now holds only where the
    extension binds. Below the crossover the owner's fixed margin bar governs, and at ob 2.0 the
    rate across pools 2-7 is .000 .010 .038 .084 .140 .203 — monotone rather than flat, and A
    POOL-2 CONTEST CAN NEVER RESOLVE OVERWHELMING AT ALL (it would need net >= 5 from two dice,
    whose maximum is 4). Under the retired private ladder those same pools ran ~.07 .17 .29 .20
    .14 .21. This is a consequence of Jordan's one-ladder ruling, not a choice made here, and it
    is not papered over: uniformity across small pools got WORSE, and that is a disclosed cost
    rather than the "division of labour" an earlier draft of this docstring called it.

    THE POOL-LESS LEGACY BAR IS GONE, not carried across. It was `net >= 2*ob and net >= 3` — an
    Ob-scaled Overwhelming, which is the first thing the 2026-08-14 ruling struck by name
    ("Overwhelming no longer depends on difficulty"). Its own comment said "legacy, pool-less unit
    tests only". Pool-less callers now get the owner's ladder unmodified, which is the correct
    answer for a caller that has declined to supply the context the extension needs.

    ⚠ WHAT THIS IS NOT, stated because the ruling's second clause is NOT satisfied by it.
    Jordan asked that an extension be injected BY THE WRAPPER "in such a manner that it can be
    modified cleanly". This is not injection: `dice_engine.degree_from_net` exposes no hook, takes
    no policy argument, and does not know an extension exists. What is below is a hard-coded
    post-filter inside the subsystem module, whose constants (`MU_PER_DIE`, `SD_PER_DIE`,
    `OVERWHELM_SIGMA`) are still subsystem-owned. The demote-only constraint is a real discipline
    and it makes the surface auditable — it does not make it composable, and nothing here would
    stop a second subsystem bolting on a differently-shaped filter. The first clause of the ruling
    ("systems should not need different degree bands") IS satisfied: the bands are the owner's,
    verified cell-for-cell. The second is open, and belongs with the subsystem-wrapper work rather
    than being closed by this commit's wording.

    Returns the ordinal 0 Failure / 1 Partial / 2 Success / 3 Overwhelming — the encoding is
    `dice_engine.DEGREE_ORDINAL`, so even the numbering is not re-decided here.
    """
    base = dice_engine.DEGREE_ORDINAL[dice_engine.degree_from_net(net, ob)]
    if pool is None or base < _OVERWHELMING:
        return base
    # The one declared extension: a de-saturation bar on the top band only.
    return _OVERWHELMING if net >= overwhelm_bar(pool) else _SUCCESS
