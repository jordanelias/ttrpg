"""[ED-MB-0041] Reverse-pair symmetry — the cheapest invariant the gauge has, and it fails today.

**Distinct from `symmetry_probe.py`** in this directory, which tests MIRROR symmetry: identical armies
must split 50/50, measuring pure slot bias. That one passes (gauge H1 reads 50.0, C3 50.8). This one
tests the other half — the INTERACTION — by running an *asymmetric* matchup in both orientations. That
is where the failure lives, and a mirror probe is structurally blind to it.

**The invariant.** A matchup is a physical question: *does this army beat that one?* Which of the two
occupies the engine's "side A" slot is bookkeeping. So for any matchup,

    decA(X vs Y)  +  decA(Y vs X)  ==  100

up to sampling error. No history, no band, no judgement call — the engine either has this property or
it does not. Three of the gauge's own row pairs are exactly this construction (H2/H9, H3/H10, H4/H11)
and their bands were independently authored as exact complements (48-62/38-52, 55-72/28-45,
45-62/38-55), so both halves of a pair can only pass if the engine satisfies it.

**Why this outranks a band.** A global constant enters both sides' resolution identically, so under a
symmetric engine it moves the two halves in opposite directions and leaves the sum pinned at 100. The
sum is therefore an *invariant of the symmetric constants*: no amount of tuning changes it, and any
deviation localises the fault to a mechanism that treats the sides differently — deployment geometry,
resolution order — rather than to a number. This is why the reachability sweep found H10 unreachable by
any of the 85 configurations it tried: it was never a calibration problem.

**Statistics — why this reports sigma and not a raw gap.** The two halves are independent binomial
proportions, so the deviation `sum - 100` carries a standard error of about
`100 * sqrt(p_f(1-p_f)/k_f + p_r(1-p_r)/k_r)` on the DECISIVE counts. At the gauge's n=60 that is
roughly 9pp, so a deviation must clear ~18pp to be 2-sigma real. Reporting the deviation in units of
its own standard error is what stops a noisy near-miss being recorded as a defect (and vice versa) —
the same failure mode that made the first reachability sweep report 76 phantom in-band hits at n=16.

Usage:
    python audit/2026-07-22-mass-battle-stress-test/reverse_pair_symmetry.py [--n 60] [--mode multi]
"""
import argparse
import math
import os
import sys

_SIM = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'tests', 'sim'))
if _SIM not in sys.path:
    sys.path.insert(0, _SIM)

import gauge_mb as G

SIGMA_GATE = 2.0   # |sigma| below this is consistent with a symmetric engine at the sample size used


def row(rid):
    for t in (G.TESTS + G.CAV_TESTS):
        if t[0] == rid:
            return t
    raise KeyError(rid)


def symmetry(sa, sb, ka, kb, mode='multi', n=60, seed_base=1_000_000):
    """Run a matchup both ways; report the deviation from the 100-sum invariant, in sigma.

    Returns {fwd, rev, total, dev, se, sigma, dec_fwd, dec_rev}. Judge on `sigma`: |sigma| < 2 is
    consistent with symmetry at this sample size; a large |sigma| means a side-dependent mechanism.
    `sigma is None` means at least one orientation produced NO decisive results, in which case the
    matchup carries no information about symmetry at all — not a pass.
    """
    f = G.matchup(sa, sb, ka, kb, mode, n=n, seed_base=seed_base)
    r = G.matchup(sb, sa, kb, ka, mode, n=n, seed_base=seed_base)
    total = f['decA'] + r['decA']
    dev = total - 100.0

    def _se(res):
        # On the DECISIVE count, not n: a draw-heavy row has fewer informative trials and a
        # correspondingly wider error bar. An all-draw orientation has none.
        k = res['dec_n']
        if k <= 0:
            return None
        p = res['decA'] / 100.0
        return 100.0 * math.sqrt(max(p * (1 - p), 1e-9) / k)

    se_f, se_r = _se(f), _se(r)
    se = None if (se_f is None or se_r is None) else math.sqrt(se_f ** 2 + se_r ** 2)
    sigma = None if not se else dev / se
    return dict(fwd=f['decA'], rev=r['decA'], total=total, dev=dev, se=se, sigma=sigma,
                dec_fwd=f['dec_n'], dec_rev=r['dec_n'])


# The gauge's own reverse pairs: matchups that already exist in both orientations, so the invariant is
# checked against rows whose complementary bands were authored independently of this probe.
PAIRS = [('H2/H9', 'H2'), ('H3/H10', 'H3'), ('H4/H11', 'H4')]


def report(n=60, mode='multi'):
    print(f'--- reverse-pair symmetry: decA(X vs Y) + decA(Y vs X) must be 100 '
          f'(mode={mode}, n={n}) ---')
    print(f'  {"pair":9} {"fwd":>6} {"rev":>6} {"sum":>7} {"dev":>7} {"se":>6} {"sigma":>7}  verdict')
    worst, results = 0.0, {}
    for label, ida in PAIRS:
        _tid, _lab, sa, sb, ka, kb, *_ = row(ida)
        s = symmetry(sa, sb, ka, kb, mode=mode, n=n)
        results[label] = s
        if s['sigma'] is None:
            print(f'  {label:9} {"-":>6} {"-":>6} {"-":>7} {"-":>7} {"-":>6} {"-":>7}  '
                  f'NO DECISIVE RESULTS (symmetry undefined, not a pass)')
            continue
        worst = max(worst, abs(s['sigma']))
        print(f'  {label:9} {s["fwd"]:6.1f} {s["rev"]:6.1f} {s["total"]:7.1f} {s["dev"]:+7.1f} '
              f'{s["se"]:6.1f} {s["sigma"]:+7.1f}  '
              f'{"OK" if abs(s["sigma"]) < SIGMA_GATE else "ASYMMETRIC"}')
    print(f'\n  worst deviation: {worst:.1f} sigma — '
          f'{"consistent with symmetry" if worst < SIGMA_GATE else "a side-dependent mechanism exists"}')
    return results


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--n', type=int, default=60)
    ap.add_argument('--mode', default='multi')
    a = ap.parse_args()
    report(n=a.n, mode=a.mode)
