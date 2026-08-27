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


def _pre_ruling_bounds_arm(pre: bool):
    """Patch `faction_bounds` back to its PRE-2026-08-23 answers, or leave the ruled ones. Undo.

    Two Jordan rulings landed that day and both change this clamp, so the arms compare the pair
    rather than one at a time — separating them would need a third arm and would compare against a
    state that never shipped:
      * "Influence can be 0"  — Influence floored at 1 before (ED-IN-0029/OPT-AV-14).
      * "Legitimacy is a base" — `L` was undeclared before, so it fell back to 0.5/7.0.

    It patches the BOUNDS LOOKUP rather than the registry data, so both arms read one cooked
    artifact and the only difference is the answer `adjust` gets.
    """
    from engine.autoload import game_state as gs
    from engine.substrate import descriptors as d

    original = d.faction_bounds
    _PRE = {'I': (1, 7), 'L': None}

    def patched(field):
        if field in _PRE:
            return _PRE[field]
        return original(field)

    if pre:
        d.faction_bounds = patched
        gs.descriptors.faction_bounds = patched
    return lambda: (setattr(d, 'faction_bounds', original),
                    setattr(gs.descriptors, 'faction_bounds', original))


def _floor_arm(blanket: bool):
    """Patch `Faction.adjust` to the pre-S5d blanket 0.5/7.0 bounds, or leave the registry-declared
    per-stat bounds in place (ED-IN-0029). Returns undo.

    The `blanket` arm reproduces the OLD behaviour by forcing the fallback bounds for every stat,
    which is exactly what the method did before `descriptors.faction_bounds()` was wired. It patches
    the METHOD rather than the descriptor data so both arms read the same registry — the point of
    running them in one process is that the mechanic is the only difference.
    """
    from engine.autoload import game_state as gs

    original = gs.Faction.adjust

    def patched(self, stat, granular_delta, floor=None, ceiling=None):
        return original(self, stat, granular_delta,
                        floor=gs.Faction.UNDECLARED_FLOOR if floor is None else floor,
                        ceiling=gs.Faction.UNDECLARED_CEILING if ceiling is None else ceiling)

    if blanket:
        gs.Faction.adjust = patched
    return lambda: setattr(gs.Faction, 'adjust', original)


def _contest_ladder_arm(pre: bool):
    """Patch the CONTEST's degree path back to its PRE-ED-SC-0031 private ladder. Returns undo.

    THE MECHANIC. Until 2026-08-27 the social-contest surface carried its own degree bands — the
    ninth ladder, and the one the 2026-08-12 census missed. Two of its three lower boundaries
    contradicted Jordan's 2026-08-14 ruling (`net == ob` -> Success where the ruling says Partial;
    `0 < net < ob` -> Partial where it says Failure) and its pool-less top band was the Ob-scaled
    `net >= 2*ob` bar the ruling struck by name. It now resolves through
    `dice_engine.degree_from_net` with a declared, injected extension (ED-SC-0032).

    The `pre` arm below is a VERBATIM copy of the retired implementation, kept here as the record
    of what it did — same convention as `_pool_arm` and `_floor_arm` above.

    ⚠ THIS ARM WAS BROKEN FOR THE LENGTH OF ONE COMMIT, and the repair is the interesting part.
    It read `original = SL.degree` and `SL.OVERWHELM_SIGMA`; ED-SC-0032 moved both out of the
    engine into the subsystem that owns them, so `python3 tools/balance_oracle.py` — the
    documented default invocation, and the instrument CLAUDE.md §7 names as THE campaign-level
    balance control — raised AttributeError on its first arm. Found by an adversarial pass, not by
    a test, because NOTHING EXECUTES THIS FILE: it is deliberately not a CI gate (240 campaigns,
    ~13 minutes), so it has no freshness relationship to the code it measures. The instrument that
    produced ED-SC-0031's control was disabled by ED-SC-0031's own successor commit.
    `tests/valoria/test_balance_oracle_arms.py` now constructs both arms, which is cheap and
    catches exactly this.

    SCOPE, which the repair also had to get right. Post-ED-SC-0032 the contest reaches the ladder
    through `resolver`'s module-level `degree_from_net` binding plus the contest's own `degree`
    adapter. Patching `dice_engine.degree_from_net` globally would re-band the WHOLE GAME — mass
    battle, threadwork, faction actions — which is a different experiment from the one this arm
    exists to run. Only the contest's two bindings are patched.
    """
    from engine.autoload.dice_engine import Degree
    from systems.social_contest.sim.contest import degree_extension as CD
    from systems.social_contest.sim.contest import resolver as _res

    _ORDINAL_TO_DEGREE = {0: Degree.FAILURE, 1: Degree.PARTIAL,
                          2: Degree.SUCCESS, 3: Degree.OVERWHELMING}

    def pre_ruling_ordinal(net, ob, pool=None):
        if net <= 0:                       return 0
        if net < ob:                       return 1
        if pool is not None:
            thresh = (SL.MU_PER_DIE * pool
                      + CD.OVERWHELM_SIGMA * SL.SD_PER_DIE * math.sqrt(max(1, pool)))
            if net >= thresh and net >= max(3, ob): return 3
            return 2
        if net >= 2 * ob and net >= 3:     return 3
        return 2

    def pre_ruling_degree_from_net(net, ob, extension=None, pool=None, **context):
        """The shape `resolver._reception` calls. `extension` is IGNORED by construction: the
        pre-ruling ladder had no seam, and honouring one here would measure a hybrid that never
        shipped."""
        return _ORDINAL_TO_DEGREE[pre_ruling_ordinal(net, ob, pool)]

    if not pre:
        return lambda: None

    originals = [(_res, 'degree_from_net', _res.degree_from_net),
                 (CD, 'degree', CD.degree)]
    # Assert the sites are what we think they are BEFORE patching. A binding that has moved makes
    # this arm silently half-fake — two nearly-identical arms and a meaningless z — which is the
    # confound §0.1 pt 4 exists for, and is precisely how this function broke.
    assert _res.degree_from_net.__name__ == 'degree_from_net', (
        'resolver no longer binds degree_from_net at module level; this arm would not reach the '
        'live campaign call site and the comparison would be fake')
    assert CD.degree.__module__.endswith('degree_extension'), (
        'the contest degree adapter has moved; re-derive this arm before trusting a result')

    setattr(_res, 'degree_from_net', pre_ruling_degree_from_net)
    setattr(CD, 'degree', lambda net, ob, pool=None: pre_ruling_ordinal(net, ob, pool))
    return lambda: [setattr(m, a, orig) for m, a, orig in originals]


#: The comparison this invocation runs. Swap in the pair you are measuring; keep exactly two arms,
#: keep them in one process, and leave the retired pairs above as worked examples rather than
#: deleting the function that documents what the old behaviour WAS.
ARMS = {
    'private_ladder': lambda: _contest_ladder_arm(True),
    'owner_ladder':   lambda: _contest_ladder_arm(False),
}

#: Retired comparison (ED-IN-0029 / the 2026-08-23 Influence + Legitimacy rulings). Restore into
#: ARMS to re-run it.
_ARMS_BOUNDS = {
    'pre_ruling': lambda: _pre_ruling_bounds_arm(True),
    'ruled':      lambda: _pre_ruling_bounds_arm(False),
}

#: Retired comparison from plan S5d, kept as the record of what `adjust` did before the registry
#: owned its bounds. Restore into ARMS to re-run it.
_ARMS_FLOOR = {
    'blanket_0.5': lambda: _floor_arm(True),
    'per_stat':    lambda: _floor_arm(False),
}

#: Retired comparison, kept because `_pool_arm` is the record of what `roll_net_continuous` did
#: before M1 juncture 1 half A. Restore into ARMS to re-run it.
_ARMS_POOL = {
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
    """Pooled two-proportion z. Returns 0.0 when the pooled rate is degenerate (0 or 1).

    ⚠ IT TREATS THE TWO ARMS AS INDEPENDENT SAMPLES, AND THEY ARE NOT. Both arms run the SAME seed
    sequence (`base_seed + i`), which is the point — it removes between-sample variance so the
    mechanic is the only difference. But a two-proportion z assumes independence, so on paired,
    highly-correlated arms it OVERSTATES the standard error and therefore UNDER-DETECTS a real
    shift. Read a non-significant result as "no shift large enough for an independence-assuming
    test to see", not as "no shift". A paired test (McNemar over per-seed win/loss flips) would be
    the right statistic and needs per-seed winners retained rather than counted; recorded here
    rather than swapped in, because changing the statistic under a result already reported to
    Jordan would be worse than naming its limitation.

    The bias runs toward the null, which is the safe direction for a CONTROL — it makes "the goldens
    moved from RNG divergence, not balance" harder to claim, not easier."""
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
