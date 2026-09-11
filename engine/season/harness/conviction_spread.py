"""HOW FAR APART THE THIRTEEN CONVICTIONS ACTUALLY ARE, in the four-axis basis.

`ED-IN-0214`'s instrument. That row escalates one question — whether
`conviction_axis_matrix_v30.md`'s 13x4 should be re-centred — and every number in it is produced
here, because a ledger entry stating measured numbers must name a re-runnable instrument
(`ED-PC-0040`, and `CLAUDE.md` §0.1 pt 3 for the same reason one layer up).

    python -m engine.season.harness.conviction_spread

WHAT IT MEASURES AND WHY THAT QUANTITY. `U3` made a person's convictions reach a verb through
`Σ_conv conviction[conv] · projection[conv][axis]`, so two people differ in their rankings exactly
as far as their PROJECTED VECTORS differ. If most convictions project to nearly the same direction,
then a person's convictions discriminate well among their own options and badly between people —
which is what the corpus showed (ranking discrimination 7..11 -> 16..22 of 28 while distinct
executed sets fell 40 -> 27). The cosine against the mean vector is the direct read of that: a
conviction at +0.95 is a variation on the common theme, one at -0.90 is a genuine dissent.

⚠ IT MEASURES THE TABLE, NOT A RUN, AND THAT IS THE POINT. No world is built and no season is
played, so the figures cannot move with a fixture, a seed or an act mix — they move only when the
matrix does. The run-dependent half of `ED-IN-0214` (the discrimination range and the executed-set
count) comes from `corpus_run.py`'s own `RANKING DISCRIMINATION` line and is not duplicated here.
"""
from __future__ import annotations

import math

from ..data.rosters import CONVICTION_AXES
from ..data.verbs import CONVICTION_PROJECTION, PROJECTION_DEFAULT_CELL


def spread() -> dict:
    """`{mean, magnitude, cosines, per_axis_signs, within_60deg}` over the declared matrix."""
    axes = list(CONVICTION_AXES)
    # The DECLARED sparse default, not a literal — `decision.project` reads the same constant,
    # and an instrument that hard-codes `0.0` stops agreeing with the thing it measures the day
    # the row's `default_cell` moves.
    rows = {c: [CONVICTION_PROJECTION[c].get(a, PROJECTION_DEFAULT_CELL) for a in axes]
            for c in CONVICTION_PROJECTION}
    n = len(rows) or 1
    mean = [sum(v[i] for v in rows.values()) / n for i in range(len(axes))]
    mag = math.sqrt(sum(m * m for m in mean))
    cos = {}
    for c, v in rows.items():
        vn = math.sqrt(sum(x * x for x in v))
        cos[c] = (sum(a * b for a, b in zip(v, mean)) / (vn * mag)) if vn and mag else 0.0
    signs = {a: (sum(1 for v in rows.values() if v[i] > 0),
                 sum(1 for v in rows.values() if v[i] < 0))
             for i, a in enumerate(axes)}
    return dict(axes=axes, mean=dict(zip(axes, mean)), magnitude=mag, cosines=cos,
                per_axis_signs=signs,
                within_60deg=sum(1 for x in cos.values() if x > 0.5), total=n)


def main() -> int:
    s = spread()
    print(f"CONVICTION SPREAD — {s['total']} convictions over {len(s['axes'])} axes")
    print("  mean vector   " + "  ".join(f"{a} {s['mean'][a]:+.3f}" for a in s["axes"]))
    print(f"  magnitude     {s['magnitude']:.3f}")
    print("\n  cosine with the mean direction (a variation on the common theme vs a dissent):")
    for c, x in sorted(s["cosines"].items(), key=lambda kv: -kv[1]):
        print(f"    {c:12} {x:+.3f}")
    print(f"\n  {s['within_60deg']} of {s['total']} convictions lie within 60 degrees of the mean")
    print("  per axis (positive / negative):")
    for a, (pos, neg) in s["per_axis_signs"].items():
        print(f"    {a:14} {pos:2} / {neg:2}")
    # ⚠ NO VERDICT. Whether this spread is right is `ED-IN-0214`'s question and Jordan's to answer;
    # printing a pass/fail here would be this instrument deciding it.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
