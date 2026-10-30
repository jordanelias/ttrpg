"""Mechanism probe for the lopsided outcomes the social-contest stress test found (kernel, not adopted).

The stress test measured WHAT is lopsided (weaker side's share of decided contests, share of contests
that end in a side at all, church_tribunal's seat asymmetry). This probe asks WHY, by decomposing the
kernel's own quantities and by changing ONE mechanism at a time:

  A  geometry   per proceeding, equal sides and faculty 1 v 4: the distribution of the advantage gap
                (advA - advB) at the close, set against the gap the win-condition needs.
  B  seat       church_tribunal with its track start at 6.0 (canonical) and at the neutral 5.0.
  C  exchanges  the exchange-majority venue (casual_dispute's) at 1, 2, 3, 5 and 8 exchanges.
  D  policy     formal/grand contest under each side-building policy, not only 'logos'.
  E  gap        formal_contest as side B's faculty moves 1..7 against A's 4.
  F  degree     the reception degree distribution by faculty, the quantity everything above is built on.

NO CHOSEN COUNT, same rule as social_contest_stress.py: each cell samples until its slice of --budget-s
runs out and logs n. Every cell is one JSONL line (flushed, fsync'd) so the run can be audited and a
killed run still leaves its finished cells.

Usage (repo root):  python proposals/2026-10-29-parliament-and-debate/lopsided_mechanism.py \\
                      --budget-s 360 --log OUT.jsonl
"""
import argparse, dataclasses, math, os, random, sys, time
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, ROOT)
sys.path.insert(0, HERE)
from stress_probe import Log, git

import systems.social_contest.sim.contest as sc
from systems.social_contest.sim.contest.contract import A, B, Adjudicator
from systems.social_contest.sim.contest.resolver import (Bout, Contestant, Venue, PersuasionTrack,
                                                         TallyAtClose, VoteAtClose)


def side(band):
    if band in ('a', 'A_decisive', 'A_total'):
        return 'A'
    if band in ('b', 'B_decisive', 'B_total'):
        return 'B'
    return band  # 'draw' | 'committee' | anything unexpected stays visible under its own name


def wilson(k, n, z=1.96):
    if n == 0:
        return (0.0, 1.0)
    p = k / n
    d = 1 + z * z / n
    c = p + z * z / (2 * n)
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return (round((c - h) / d, 4), round((c + h) / d, 4))


def _fac(s):
    """A side spec's faculty: the int itself, or the dict's 'faculty'."""
    return s['faculty'] if isinstance(s, dict) else s


def win_geometry(win):
    """What the win-condition needs, in units of the advantage gap (advA - advB)."""
    if isinstance(win, PersuasionTrack):
        return {'kind': 'PersuasionTrack', 'start': win.start, 'scale': win.scale,
                'gap_for_A_decisive': (7 - win.start) / win.scale,
                'gap_for_B_decisive': (3 - win.start) / win.scale,
                'gap_for_A_total': (9 - win.start) / win.scale,
                'gap_for_B_total': (1 - win.start) / win.scale}
    if isinstance(win, TallyAtClose):
        return {'kind': 'TallyAtClose', 'gap_for_A': 0.0, 'gap_for_B': 0.0}
    if isinstance(win, VoteAtClose):
        return {'kind': 'VoteAtClose', 'sharpness': win.k, 'noise': win.noise, 'aggregation': win.aggregation}
    return {'kind': type(win).__name__}


def cell(log, name, seconds, proc, fa, fb, pa='logos', pb='logos', mutate=None, tag=None):
    """Sample one matchup for `seconds`; log outcome counts, the gap distribution and the move mix."""
    rnd = random.Random(hash((name, proc, repr(fa), repr(fb), pa, pb, tag)) & 0xffffffff)
    n = 0
    out = Counter()
    s_gap = s_gap2 = s_a = s_b = 0.0
    moves = Counter()
    gain_sum = Counter()
    geom = None
    end = time.time() + seconds
    while time.time() < end:
        for _ in range(20):
            random.seed(rnd.randrange(2 ** 31))
            c = sc.build_contest(fa, fb, venue=proc)
            if mutate:
                c.venue = mutate(c.venue)
            geom = geom or win_geometry(c.venue.win)
            (band, _r), bout = sc.resolve_contest(c, policy_a=pa, policy_b=pb, record=True)
            out[side(band)] += 1
            gap = bout.state.adv[A] - bout.state.adv[B]
            s_gap += gap; s_gap2 += gap * gap
            s_a += bout.state.adv[A]; s_b += bout.state.adv[B]
            for beat in bout.log:
                moves[(beat['side'], beat['kind'])] += 1
                if beat['kind'] == 'advance':
                    gain_sum[beat['side']] += beat['gain']
            n += 1
    mean = s_gap / n
    sd = math.sqrt(max(0.0, s_gap2 / n - mean * mean))
    dA, dB = out['A'], out['B']
    row = {'cell': name, 'tag': tag, 'proceeding': proc, 'faculty_A': fa, 'faculty_B': fb,
           'policy_A': pa, 'policy_B': pb, 'n': n, 'outcomes': dict(out),
           'decided_share': round((dA + dB) / n, 4),
           'A_share_of_decided': round(dA / (dA + dB), 4) if dA + dB else None,
           'A_share_ci95': wilson(dA, dA + dB),
           'weaker_share_of_decided': (round((dA if _fac(fa) < _fac(fb) else dB) / (dA + dB), 4)
                                       if (dA + dB) and _fac(fa) != _fac(fb) else None),
           'gap_mean': round(mean, 4), 'gap_sd': round(sd, 4),
           'advA_mean': round(s_a / n, 4), 'advB_mean': round(s_b / n, 4),
           'mean_gain_per_advance': {s: (round(gain_sum[s] / moves[(s, 'advance')], 4) if moves[(s, 'advance')] else None)
                                     for s in (A, B)},
           'moves_per_contest': {f'{s}:{k}': round(v / n, 3) for (s, k), v in sorted(moves.items())},
           'geometry': geom}
    if geom and geom.get('kind') == 'PersuasionTrack' and sd > 0:
        row['A_decisive_threshold_in_sd'] = round((geom['gap_for_A_decisive'] - mean) / sd, 3)
        row['B_decisive_threshold_in_sd'] = round((mean - geom['gap_for_B_decisive']) / sd, 3)
    log.w('cell', **row)
    return row


def degree_cell(log, seconds, faculties):
    """Reception degree by faculty (A's roll against base_ob 2.0): the quantity the advantage is built on."""
    per = seconds / len(faculties)
    for f in faculties:
        random.seed(f)
        b = Bout(Contestant(f), Contestant(4), Venue(), Adjudicator())
        c = Counter(); n = 0
        end = time.time() + per
        while time.time() < end:
            for _ in range(50):
                c[b._reception(A)] += 1; n += 1
        pool = sc.primitives.Pool.size(f)
        lev = sc.primitives.Leverage.net(f, on_ground=True)
        log.w('cell', cell='F_degree', faculty=f, pool=pool, leverage_sigma=round(lev, 4), n=n,
              degree_share={str(k): round(c[k] / n, 4) for k in (0, 1, 2, 3)},
              mean_degree=round(sum(k * v for k, v in c.items()) / n, 4))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--budget-s', type=float, required=True)
    ap.add_argument('--log', required=True)
    args = ap.parse_args()
    log = Log(args.log)
    log.w('manifest', head=git('rev-parse', 'HEAD'), branch=git('rev-parse', '--abbrev-ref', 'HEAD'),
          dirty=git('status', '--porcelain'), python=sys.version, budget_s=args.budget_s,
          argv=sys.argv, note='mechanism probe; kernel is evaluated, not adopted (SC-05)')

    procs = sorted(sc.PROCEEDINGS)
    # cells: A = procs x 2 matchups; B = 2 x 2; C = 5 x 2; D = 2 procs x 4 policies x 2; E = 7; F = 7 (degree)
    n_cells = len(procs) * 2 + 4 + 10 + 16 + 7 + 7
    per = args.budget_s / n_cells
    log.w('plan', cells=n_cells, per_cell_s=round(per, 2),
          note='no chosen trial count: each cell samples until its time slice ends and logs n')

    # A  geometry
    for p in procs:
        cell(log, 'A_geometry', per, p, 4, 4)
        cell(log, 'A_geometry', per, p, 1, 4)

    # B  seat: church_tribunal at the canonical start (6.0) and at the neutral start (5.0)
    def neutral_start(v):
        return dataclasses.replace(v, win=PersuasionTrack(start=5.0))
    for fa, fb in ((4, 4), (1, 4)):
        cell(log, 'B_seat', per, 'church_tribunal', fa, fb, tag='start=6.0 (canonical)')
        cell(log, 'B_seat', per, 'church_tribunal', fa, fb, mutate=neutral_start, tag='start=5.0 (neutral)')

    # C  exchanges: casual_dispute's exchange-majority venue at different exchange counts
    for n_ex in (1, 2, 3, 5, 8):
        def with_budget(v, n_ex=n_ex):
            return dataclasses.replace(v, budget=n_ex)
        for fa, fb in ((4, 4), (1, 4)):
            cell(log, 'C_exchanges', per, 'casual_dispute', fa, fb, mutate=with_budget, tag=f'exchanges={n_ex}')

    # D  policy: does building ethos/pathos (readiness) change the shape?
    for p in ('formal_contest', 'grand_contest'):
        for pol in ('logos', 'build_then_close', 'exploiter', 'demagogue'):
            for fa, fb in ((4, 4), (1, 4)):
                cell(log, 'D_policy', per, p, fa, fb, pa=pol, pb=pol, tag=f'both={pol}')

    # E  gap: formal_contest, B's faculty 1..7 against A's 4
    for fb in range(1, 8):
        cell(log, 'E_gap', per, 'formal_contest', 4, fb)

    # F  degree distribution by faculty
    degree_cell(log, per * 7, list(range(1, 8)))
    log.w('done', cells=n_cells)


if __name__ == '__main__':
    main()
