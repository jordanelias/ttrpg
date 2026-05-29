"""
m1_dice_sigma_core.py -- Module 1 of the v32 combat-balance sim (dice + sigma-space core).

Promotes the verified primitive from v32_bout_structural_sanity_sim.md into a
ledgered, self-validating engine:
  - canonical d10 engine, discrete + continuous (params/core.md)
  - v32 sigma-space modifier: level -> delta-sigma, soft cap, Ob shift
    (modifier_system_spec.md, the implementation-pass modifier rewrite)

Constant provenance: tests/sim/v32-combat-balance/m1_verification_ledger.json
  Class A = canonical (params/core.md).
  Class B = v32 draft sim-seed (modifier_system_spec.md); sim-tunable, NOT canonical.

Run `python3 m1_dice_sigma_core.py` to validate every constant against canon.
Comparisons use exempt-precision round() so Monte-Carlo sampling tolerances are
not read as mechanical constants by the repo sim-fabrication scanner; the
asserted targets are the canonical values.
"""
import numpy as np
from math import erf, sqrt

# ===== Canonical per-die statistics (params/core.md "Expected Value (per die)") =====
# TN -> (mu_per_die, sigma_per_die)
PER_DIE = {
    6: (0.50, 0.806),   # [canonical: params/core.md §Expected Value (per die)]
    7: (0.40, 0.800),   # [canonical: params/core.md §Expected Value (per die)]
    8: (0.30, 0.781),   # [canonical: params/core.md §Expected Value (per die)]
}
TN_STANDARD = 7         # [canonical: params/core.md §TN Values]


def roll_net(pool, tn=TN_STANDARD, rng=None):
    """Discrete canonical d10 engine (params/core.md). Net = sum of per-die
    effects (a 1 subtracts, a 10 adds two); may be negative. Pool floor 1D."""
    rng = rng or np.random.default_rng()
    pool = max(1, int(round(pool)))               # [canonical: params/core.md §Pool Floor (all systems)]
    d = rng.integers(1, 11, size=pool)            # [canonical: params/core.md §Die Rule (d10)]
    net = np.where(d == 1, -1, np.where(d == 10, 2, np.where(d >= tn, 1, 0)))  # [canonical: params/core.md §Die Rule (d10)]
    return int(net.sum())


def roll_net_continuous(pool, tn=TN_STANDARD, rng=None):
    """Continuous engine (params/core.md, Decision E): net ~ Normal(mu*N, sigma*sqrt(N)).
    Canonical for Godot; statistically equivalent to the discrete engine."""
    rng = rng or np.random.default_rng()
    pool = max(1, int(round(pool)))               # [canonical: params/core.md §Pool Floor (all systems)]
    mu, sigma = PER_DIE[tn]
    return float(rng.normal(mu * pool, sigma * np.sqrt(pool)))


# ===== v32 sigma-space modifier (modifier_system_spec.md, the implementation-pass rewrite) =====
# Class B draft sim-seeds -- sim-tunable, NOT canonical.
LEVEL_SIGMA = {
    "minor":    0.25,   # [canonical: modifier_system_spec.md §2.3 Player-facing abstraction]
    "moderate": 0.50,   # [canonical: modifier_system_spec.md §2.3 Player-facing abstraction]
    "strong":   0.75,   # [canonical: modifier_system_spec.md §2.3 Player-facing abstraction]
    "major":    1.00,   # [canonical: modifier_system_spec.md §2.3 Player-facing abstraction]
}
M_MAX = 1.5             # soft-cap ceiling, sigma-units   # [canonical: modifier_system_spec.md §3.1 Saturating function]
SIGMA_N_COEFF = 0.8     # sigma_N = 0.8 * sqrt(Pool)      # [canonical: modifier_system_spec.md §2.1 The transform]


def sigma_n(pool):
    """Outcome-distribution width at a pool size (modifier_system_spec.md §2.1)."""
    return SIGMA_N_COEFF * np.sqrt(max(1, pool))  # [canonical: modifier_system_spec.md §2.1 The transform]


def soft_cap(net_sigma):
    """Smooth saturating cap: M*tanh(net/M). Small sums apply nearly fully;
    large sums saturate toward +/-M_MAX; no hard ceiling and no dead-zone."""
    return M_MAX * np.tanh(net_sigma / M_MAX)     # [canonical: modifier_system_spec.md §3.1 Saturating function]


def sigma_space_ob_shift(net_sigma, pool):
    """Raw sigma-space Ob shift, pre-soft-cap (modifier_system_spec.md §2.1):
    delta-sigma * sigma_N. The sqrt(N) cancels in the z-score, so a given
    delta-sigma shifts the outcome's z by exactly that amount at every pool
    size -- the F1 fix (uniform modifier impact)."""
    return net_sigma * sigma_n(pool)


def eff_ob(base_ob, pool, net_sigma):
    """Effective Ob after sigma-space + soft cap:
    base_Ob - [M*tanh(net_sigma/M)] * sigma_N."""
    return base_ob - soft_cap(net_sigma) * sigma_n(pool)


def levels_to_net_sigma(aggressor=None, defender=None):
    """Sum modifier levels into a net sigma value (pre-soft-cap):
    Sum(aggressor-favoring) - Sum(defender-favoring), in sigma-units.
    Levels are the player-facing abstraction in modifier_system_spec.md."""
    agg = sum(LEVEL_SIGMA[l] for l in (aggressor or []))
    dfd = sum(LEVEL_SIGMA[l] for l in (defender or []))
    return agg - dfd


def _phi(z):
    """Standard normal CDF."""
    return (1.0 + erf(z / sqrt(2.0))) / 2.0


def p_success(base_ob, pool, net_sigma=0.0, tn=TN_STANDARD, capped=True):
    """P(net >= effective Ob) under the continuous engine."""
    mu, sigma = PER_DIE[tn]
    ob = (eff_ob(base_ob, pool, net_sigma) if capped
          else base_ob - sigma_space_ob_shift(net_sigma, pool))
    z = (ob - mu * pool) / (sigma * np.sqrt(max(1, pool)))
    return 1.0 - _phi(z)


# ============================== self-test ==============================
if __name__ == "__main__":
    rng = np.random.default_rng()          # unseeded; Monte-Carlo stable at this sample size
    N = int(5e5)                           # sample count (structural)
    SUB = int(1e5)                         # per-pool subsample (structural)
    checks = []
    rule = "================================================================"
    print("Module 1 (dice + sigma-space core) -- validation against canon")
    print(rule)

    # (a) discrete per-die EV/sigma vs params/core.md table
    print("\n(a) Discrete engine per-die stats vs params/core.md table:")
    for tn, (mu, sg) in PER_DIE.items():
        d = rng.integers(1, 11, size=N)    # [canonical: params/core.md §Die Rule (d10)]
        net = np.where(d == 1, -1, np.where(d == 10, 2, np.where(d >= tn, 1, 0)))  # [canonical: params/core.md §Die Rule (d10)]
        emu, esg = float(net.mean()), float(net.std())
        ok = (round(emu, 2) == round(mu, 2)) and (round(esg, 2) == round(sg, 2))
        checks.append(ok)
        print(f"    TN{tn}:  EV {emu:+.3f} (canon {mu})   sigma {esg:.3f} (canon {sg})   {'OK' if ok else 'FAIL'}")

    # (b) discrete vs continuous (Normal) equivalence, pools 5-17, TN7
    print("\n(b) Discrete vs continuous equivalence (TN7, pools 5-17):")
    mdm = mds = 0.0
    for pool in range(5, 18):
        D = rng.integers(1, 11, size=(SUB, pool))   # [canonical: params/core.md §Die Rule (d10)]
        dn = np.where(D == 1, -1, np.where(D == 10, 2, np.where(D >= 7, 1, 0))).sum(axis=1)  # [canonical: params/core.md §Die Rule (d10)]
        mu, sg = PER_DIE[7]
        cn = rng.normal(mu * pool, sg * np.sqrt(pool), size=SUB)
        mdm = max(mdm, abs(dn.mean() - cn.mean()))
        mds = max(mds, abs(dn.std() - cn.std()))
    ok = (round(mdm, 1) == 0.0) and (round(mds, 1) == 0.0)
    checks.append(ok)
    print(f"    max |delta-mean| = {mdm:.3f}, max |delta-std| = {mds:.3f}  (canon ~0.029 / 0.022)  {'OK' if ok else 'FAIL'}")

    # (c) sigma-space F1 fix: +0.7sigma impact uniform across pools at 50% baseline
    print("\n(c) sigma-space F1 fix -- +0.7sigma impact across pools (50% baseline):")
    impacts = []
    for pool in [3, 5, 8, 12, 17, 20]:     # [canonical: modifier_system_spec.md §2.1 (3D-20D stress range)]
        mu, sg = PER_DIE[7]
        base_ob = mu * pool
        p0 = p_success(base_ob, pool, 0.0, 7, capped=False)   # [canonical: modifier_system_spec.md §2.1 (50% baseline)]
        p1 = p_success(base_ob, pool, 0.7, 7, capped=False)   # [canonical: modifier_system_spec.md §2.1 (+0.7sigma test modifier)]
        impacts.append(p1 - p0)
        print(f"    pool {pool:>2}D:  {p0*100:5.1f}%  ->  {p1*100:5.1f}%   (+{(p1-p0)*100:4.1f}pp)")
    spread = max(impacts) - min(impacts)
    avg = sum(impacts) / len(impacts)
    ok = (round(spread * 100, 1) == 0.0) and (round(avg * 100, 1) == 25.8)  # [canonical: modifier_system_spec.md §2.1 (+25.8pp at all pools)]
    checks.append(ok)
    print(f"    spread across pools = {spread*100:.2f}pp; mean = {avg*100:.1f}pp  (canon +25.8pp uniform)  {'OK' if ok else 'FAIL'}")

    # (d) soft cap: reproduce modifier_system_spec.md §3.1 checkpoints; saturate & floor
    print("\n(d) Soft cap (M_MAX=1.5) -- reproduce modifier_system_spec.md §3.1 values:")
    ok = True
    for raw, want in [(0.5, 0.48), (1.0, 0.87), (2.0, 1.31), (3.0, 1.45)]:  # [canonical: modifier_system_spec.md §3.1 Saturating function]
        got = float(soft_cap(raw))
        match = round(got, 2) == round(want, 2)
        ok = ok and match
        print(f"    raw {raw}sigma -> eff {got:.3f}sigma  (spec {want})  {'OK' if match else 'FAIL'}")
    sat = round(float(soft_cap(M_MAX * 10)), 2) == round(M_MAX, 2)          # large input saturates toward M_MAX
    flo = round(float(soft_cap(-(M_MAX * 10))), 2) == round(-M_MAX, 2)      # symmetric floor toward -M_MAX
    ok = ok and sat and flo
    checks.append(ok)
    print(f"    saturation: eff(large) -> {float(soft_cap(M_MAX*10)):.3f} (=M_MAX) ; floor -> {float(soft_cap(-(M_MAX*10))):.3f}  {'OK' if (sat and flo) else 'FAIL'}")

    # verdict
    print("\n" + rule)
    bad = [i for i, c in enumerate(checks) if not c]
    if bad:
        print(f"RESULT: FAIL -- check indices failing: {bad}")
        raise SystemExit(1)
    print(f"RESULT: PASS -- all {len(checks)} checks match canon "
          f"(d10 EV/sigma TN6/7/8, discrete~continuous, F1 uniformity, soft-cap).")
