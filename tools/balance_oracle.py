#!/usr/bin/env python3
"""balance_oracle.py — the n>=100 controlled balance comparison this repo has been missing.

WHY THIS EXISTS. `engine/tests/test_f7_smoke_oracle.py:8` has asked for an n>=100 balance oracle
since it was written, and `CLAUDE.md` §7 records the two gaps that follow from its absence:

  1. the seeded goldens run at n=2 and n=8, where ONE campaign flipping is 50pp and 12.5pp, so
     they "cannot distinguish a balance regression from noise once someone legitimately re-pins";
  2. "the re-pin path is uncontrolled: nothing verifies a golden regeneration was intended."

This closes (1) and gives (2) something to point at. It is NOT a CI gate and must not become one —
240 campaigns take roughly 13 minutes, and a gate that slow gets skipped, which is worse than a
tool that gets run.

WHAT IT DOES. Runs the same seeds twice IN ONE PROCESS, once with a mechanic patched to its old
behaviour and once with the new, so the ONLY difference between arms is the mechanic. Reports the
per-faction win-share delta and a two-proportion z. That is the control CLAUDE.md §0.1 pt 4 demands:
"a number without a control is not a measurement -- in either direction."

FIRST USE, 2026-08-21 (M1 juncture 1, fractional dice pools). Six seeded goldens moved and the
question was whether the mechanic had shifted BALANCE or merely diverged the RNG stream. Result at
n=120 per arm:

    faction      rounded   fractional   delta pp        z
    Church        10.8%       10.0%       -0.8       -0.21
    Crown         36.7%       39.2%       +2.5       +0.40
    Hafenmark      8.3%       10.0%       +1.7       +0.45
    Varfell       44.2%       40.8%       -3.3       -0.52

Nothing significant (threshold |z| > 1.96). The goldens were re-recorded on that basis.

HOW TO ADD AN ARM. `ARMS` maps a name to a function that patches the engine into that behaviour and
returns an undo. Keep both arms in one process — running them as two invocations reintroduces every
between-process difference the control exists to remove.

Usage:
    python3 tools/balance_oracle.py                 # default: fractional-pool comparison, n=120
    python3 tools/balance_oracle.py --n 200
    python3 tools/balance_oracle.py --seed 20260819
"""
from __future__ import annotations

import argparse
import collections
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from engine.autoload import dice_engine, sigma_leverage as SL  # noqa: E402
from engine import mc_v18  # noqa: E402

Z_THRESHOLD = 1.96          # two-sided 5%


def _pool_arm(round_pool: bool):
    """Patch `roll_net_continuous` to round (the pre-2026-08-21 behaviour) or not. Returns undo."""
    original = SL.roll_net_continuous

    def patched(pool, tn=SL.TN_STANDARD, rng=None):
        p = max(1, int(round(pool))) if round_pool else max(1.0, float(pool))
        return dice_engine.continuous_engine_sample(pool=float(p), tn=tn, rng=rng)

    SL.roll_net_continuous = patched
    return lambda: setattr(SL, 'roll_net_continuous', original)


ARMS = {
    'rounded':    lambda: _pool_arm(True),
    'fractional': lambda: _pool_arm(False),
}


def run_arm(setup, n, base_seed):
    undo = setup()
    wins = collections.Counter()
    try:
        for i in range(n):
            r = mc_v18.run_campaign(seed=base_seed + i, max_seasons=50)
            wins[r.winner or 'none'] += 1
    finally:
        undo()
    return wins


def two_proportion_z(a_wins, b_wins, n):
    """Pooled two-proportion z. Returns 0.0 when the pooled rate is degenerate (0 or 1)."""
    pooled = (a_wins + b_wins) / (2 * n)
    if pooled <= 0 or pooled >= 1:
        return 0.0
    se = math.sqrt(2 * pooled * (1 - pooled) / n)
    return ((b_wins / n) - (a_wins / n)) / se


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument('--n', type=int, default=120, help='campaigns PER ARM (default 120)')
    ap.add_argument('--seed', type=int, default=20260819, help='base seed (default 20260819)')
    args = ap.parse_args(argv)

    if args.n < 100:
        print(f'[balance-oracle] WARNING: n={args.n} is below the 100 this tool exists to provide. '
              f'At small n a single campaign flip dominates and the z values below mean nothing.')

    results = {name: run_arm(setup, args.n, args.seed) for name, setup in ARMS.items()}
    names = list(ARMS)
    a, b = results[names[0]], results[names[1]]
    factions = sorted(set(a) | set(b))

    print(f'\nn={args.n} campaigns per arm, seeds {args.seed}..{args.seed + args.n - 1}\n')
    print(f'{"faction":<12}{names[0]:>11}{names[1]:>13}{"delta pp":>11}{"z":>9}')
    significant = []
    for f in factions:
        pa, pb = 100 * a[f] / args.n, 100 * b[f] / args.n
        z = two_proportion_z(a[f], b[f], args.n)
        flag = '  SIGNIFICANT' if abs(z) > Z_THRESHOLD else ''
        if flag:
            significant.append(f)
        print(f'{str(f):<12}{pa:>10.1f}%{pb:>12.1f}%{pb - pa:>+10.1f}{z:>+9.2f}{flag}')

    print()
    if significant:
        print(f'[balance-oracle] {len(significant)} faction(s) shifted significantly: '
              f'{", ".join(map(str, significant))}. The mechanic MOVED BALANCE — say so in the '
              f'commit and do not describe the golden re-record as "RNG divergence".')
    else:
        print(f'[balance-oracle] no faction shifted significantly (|z| <= {Z_THRESHOLD}). Consistent '
              f'with the mechanic diverging the RNG stream without moving balance. That is a '
              f'CONTROL, not proof of no effect — it bounds the effect, it does not exclude one.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
