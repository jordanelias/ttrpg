#!/usr/bin/env python3
"""measure_colocation.py — the standing measurement behind ED-MB-0056 / ED-MB-0059.

Jordan, 2026-07-29: "i don't want cells between subunits mixing with each other. the surface of
battle between units is the boundary between their cells — if we accept co-location, everything
becomes a disaster codewise." And the design steer that followed: "we are using a field system so
there shouldn't even be any assignment issues so long as cell boundaries are respected."

TWO METRICS, and the difference between them matters. The field path is CONTINUOUS, so "these two
cells occupy the same integer square" is a proxy that rounds two bodies 0.6 apart into a collision
that never happened. The metric the exclusion pass actually enforces is BODY-BOX INTERPENETRATION,
and this probe reports it using `geometry.obb_overlap` — the engine's existing single owner of "these
two bodies overlap" — rather than inventing a third definition of the same fact:

  squares  — legacy ED-MB-0056 metric: placements rounded to an integer square, then counted.
             Kept only so the original number stays comparable. It over-counts.
  bodies   — obb_overlap on the two oriented unit squares: a strict SAT boolean.
  DEEP     — obb_overlap AND penetration depth >= COLOC_MIN_DEPTH (default 0.1 lattice units).
             THIS IS THE ONE TO READ, and the reason it exists is measured, not stylistic.

⚠ A RAW OVERLAP BOOLEAN IS NOT A MEASUREMENT OF CO-LOCATION HERE. The formation lattice has pitch
1.0 and the bodies are 1.0 x 1.0, so neighbouring cells sit EXACTLY ON the touch boundary by
construction — `_sat_separated` documents that centre-distance exactly 1.0 counts as separated, i.e.
the lattice is tangent to the predicate's own boundary. Any sub-millimetre jitter therefore flips a
neighbour pair to "overlapping" while nothing has visibly moved. Measured at t=4 over the 20
historical rows: of 16,847 overlapping same-subunit pairs the MEDIAN penetration depth is 0.0029
lattice units and 88.5% are below 0.1; only ~295 pairs (1.8%) exceed 0.5. Reporting the boolean
count as "co-location" over-states the defect by roughly an order of magnitude, in the same way the
rounded-square metric over-states it in the other direction. Depth is the discriminator.

Both are split by the three classes that have DIFFERENT meanings:

  same subunit            — a body's own cells stacked; the grid-era `resolve_internal_collisions`
                            discipline roll is the primitive built for this one (still unwired).
  different subunit, same side  — two of my own formations interpenetrating. This is the class
                            ED-MB-0059's same-side exclusion pass exists to drive to zero.
  opposing sides          — two armies occupying one square; the cross-side TOI pass has always
                            covered this, so a nonzero count here is a regression in that pass.

Run it with PC_CELL_EXCLUSION=0 and =1 to get the before/after; the pass is a no-op on the grid
path, so PER_CELL=1 FIELD_MOVEMENT=1 is required for the numbers to mean anything.

    PER_CELL=1 FIELD_MOVEMENT=1 PC_NODE_COHESION=1 VIZ_SCALE=historical \\
        PC_CELL_EXCLUSION=0 python3 audit/2026-07-29-scenario-visualization/measure_colocation.py
"""
import collections
import math
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))), 'tests', 'sim'))

import render_scenarios as R            # noqa: E402  (owns scenarios()/snapshot(); never re-derived)
import mass_battle.hierarchy.units as U  # noqa: E402
from mass_battle.geometry import cellbox_from, obb_overlap  # noqa: E402
from mass_battle.hierarchy.units import CELL_RADIUS  # noqa: E402  (single owner of the body radius)

TICKS = tuple(int(t) for t in os.environ.get('COLOC_TICKS', '0,4,8,12,16,20,24').split(','))
MIN_DEPTH = float(os.environ.get('COLOC_MIN_DEPTH', '0.1'))


def _bodies(unit, side):
    """(side, subunit_idx, square, CellBox, pos, axes) per live cell — the SAME (id, position,
    facing) pairing resolve_toi_and_commit._flat uses, so the probe measures the boxes the engine
    actually solves. `axes` is the box's own (depth, width) unit frame, for the depth measure."""
    out = []
    for idx, atom in enumerate(unit.subunits):
        ids = [(o_r, o_c) for o_r, o_c, _a, _b in U._oriented(atom)]
        default = getattr(atom, '_node_facing', None) or (atom.advance_dir, 0)
        for cid, (r, c) in zip(ids, atom.cells_float()):
            facing = atom.cell_facing_vec.get(cid, default)
            n = math.hypot(facing[0], facing[1]) or 1.0
            u1 = (facing[0] / n, facing[1] / n)
            out.append((side, idx, (int(round(r)), int(round(c))),
                        cellbox_from(r, c, facing, w=1.0, d=1.0, reach_front=0.0),
                        (r, c), (u1, (-u1[1], u1[0]))))
    return out


def _depth(pa, axes_a, pb, axes_b=None):
    """Penetration depth in lattice units. 0 => tangent; 2r => fully co-located.

    ⚠ [ED-MB-0061, 2026-07-30] THE PREVIOUS FORM WAS BIASED AND ITS NUMBERS ARE RETRACTED. It read
    `min over axes_a of (1.0 - |delta . axis|)` — two independent errors for pairs whose facings
    differ, both caught by a read-only fable critic:
      1. it used B's half-extent as 0.5 on A's axes, but a rotated unit square's support radius on a
         FOREIGN axis is 0.5*(|cos t| + |sin t|), up to 0.7071 — under-stating the term by up to
         0.207, so `_depth` could return NEGATIVE for a pair `obb_overlap` had just certified as
         overlapping, silently dropping it from the DEEP count;
      2. it omitted B's own two axes, so it was not a min over the full SAT axis set and could
         over-state in the other direction.
    It was exact only for aligned/anti-aligned facings. ED-MB-0059's -48.6%/-74.4% headline was
    computed with it across differently-faced pairs and MUST BE RE-MEASURED before being cited.

    NOW MEASURED ON THE CIRCULAR BODY, per Jordan's 2026-07-30 ruling (S6): the exclusion volume is
    the r=0.5 circle, so penetration is exactly `2r - dist` — isotropic, rotation-invariant, one term,
    no axes and no frame to get wrong. This does not merely fix the bias, it retires the entire class:
    there is no foreign-axis support radius to mis-compute because a circle has the same extent in
    every direction. `axes_a`/`axes_b` are accepted and ignored, kept so call sites need not change.
    """
    dr = pa[0] - pb[0]; dc = pa[1] - pb[1]
    return 2.0 * CELL_RADIUS - math.hypot(dr, dc)


def _classify(si, gi, sj, gj):
    return 'cross_side' if si != sj else ('inter_subunit' if gi != gj else 'same_subunit')


def measure(ticks=TICKS):
    placements = 0
    sq = collections.Counter()      # legacy rounded-square metric
    bd = collections.Counter()      # body-box overlap boolean (dominated by boundary jitter)
    dp = collections.Counter()      # body-box overlap with penetration depth >= MIN_DEPTH
    worst = []
    for row in R.scenarios():
        for tk in ticks:
            _ca, _cb, ua, ub = R.snapshot(row, tk)
            bodies = _bodies(ua, 'A') + _bodies(ub, 'B')
            placements += len(bodies)
            # Rounded-square pass: bucket by square, then count colliding PAIRS within each.
            occ = collections.defaultdict(list)
            for side, idx, square, _box, _p, _ax in bodies:
                occ[square].append((side, idx))
            for _s, members in occ.items():
                for i in range(len(members)):
                    for j in range(i + 1, len(members)):
                        sq[_classify(members[i][0], members[i][1],
                                     members[j][0], members[j][1])] += 1
            # Body-box pass: exact SAT overlap. Bucketed by square first — two unit squares can only
            # overlap if their centres are within 1 square-radius, so only same/adjacent buckets can
            # collide; that is a superset, so no overlapping pair is skipped.
            row_bd = collections.Counter()
            row_dp = collections.Counter()
            by_sq = collections.defaultdict(list)
            for k, (side, idx, square, box, _p, _ax) in enumerate(bodies):
                by_sq[square].append(k)
            checked = set()
            for (r, c), ks in by_sq.items():
                near = [k for dr in (-1, 0, 1) for dc in (-1, 0, 1)
                        for k in by_sq.get((r + dr, c + dc), ())]
                for a in ks:
                    for b in near:
                        if a >= b:
                            continue
                        if (a, b) in checked:
                            continue
                        checked.add((a, b))
                        sa, ga, _sqa, ba, pa, axa = bodies[a]
                        sb, gb, _sqb, bb, pb, _axb = bodies[b]
                        if obb_overlap(ba, bb):
                            cls = _classify(sa, ga, sb, gb)
                            row_bd[cls] += 1
                            if _depth(pa, axa, pb) >= MIN_DEPTH:
                                row_dp[cls] += 1
            bd.update(row_bd)
            dp.update(row_dp)
            hot = row_dp['inter_subunit'] + row_dp['cross_side']
            if hot:
                worst.append((hot, row[0], tk, row_dp['inter_subunit'], row_dp['cross_side']))
    worst.sort(reverse=True)
    return {'placements': placements, 'min_depth': MIN_DEPTH,
            'squares': dict(sq), 'bodies': dict(bd), 'deep': dict(dp),
            'square_rate': sum(sq.values()) / max(placements, 1),
            'body_rate': sum(bd.values()) / max(placements, 1),
            'deep_rate': sum(dp.values()) / max(placements, 1),
            'worst': [{'row': w[1], 'tick': w[2], 'inter_subunit': w[3], 'cross_side': w[4]}
                      for w in worst[:8]]}


def main():
    out = measure()
    print(f"[CO-LOCATION] scale={R.SCALE} PC_CELL_EXCLUSION={U.PC_CELL_EXCLUSION} ticks={TICKS}")
    print(f"  cell placements            : {out['placements']:,}")
    for title, key, rate in (('rounded squares (legacy)', 'squares', 'square_rate'),
                             ('body boxes, any overlap', 'bodies', 'body_rate'),
                             (f'DEEP overlap (depth >= {MIN_DEPTH})', 'deep', 'deep_rate')):
        d = out[key]
        print(f"  ── {title} ──")
        print(f"     same subunit            : {d.get('same_subunit', 0):,}")
        print(f"     different subunit, mine : {d.get('inter_subunit', 0):,}")
        print(f"     opposing sides          : {d.get('cross_side', 0):,}")
        print(f"     rate                    : {100.0 * out[rate]:.2f}%")
    for w in out['worst']:
        print(f"    worst: {w['row']:>6s} t={w['tick']:<3d} inter={w['inter_subunit']:<5d} "
              f"cross={w['cross_side']}")
    if '--json' in sys.argv:
        path = sys.argv[sys.argv.index('--json') + 1]
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(out, f, indent=2, sort_keys=True)
        print(f"wrote {path}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
