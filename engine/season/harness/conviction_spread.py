"""HOW FAR APART THE THIRTEEN CONVICTIONS ACTUALLY ARE, in the four-axis basis.

`ED-IN-0214`'s instrument. That row escalates one question — whether
`conviction_axis_matrix_v30.md`'s 13x4 should be re-centred — and every number in it is produced
here, because a ledger entry stating measured numbers must name a re-runnable instrument
(`ED-PC-0040`, and `CLAUDE.md` §0.1 pt 3 for the same reason one layer up).

    python -m engine.season.harness.conviction_spread

TWO QUANTITIES, AND THE SECOND ONE ASKS A DIFFERENT QUESTION FROM THE FIRST.

  1. **How far is each conviction from the common direction** — the cosine table. It answers
     *are the thirteen thirteen characters, or five?*
  2. **How many independent directions the four-axis basis actually carries** — the covariance
     spectrum over the same thirteen rows. It answers *are the four axes four?* A basis whose
     columns co-vary is a smaller basis wearing a larger one's coordinates, and no re-weighting of
     a person's convictions can recover a direction the MATRIX does not span.

The second was added 2026-09-16 because `conviction_axis_matrix_v30.md` §2.2 reasons in the
opposite direction — it asks whether a FIFTH axis is needed, on the ground that Community and
Identity score alike — and the spectrum is the measurement that question needs before it can be
answered either way.

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


def _covariance(rows: dict, axes: list) -> list:
    """The `len(axes)` x `len(axes)` covariance of the matrix's COLUMNS, over its rows.

    The rows are the thirteen convictions and the columns are the four axes, so this asks how far
    the axes move together ACROSS the authored set — not how far the convictions move apart, which
    is what the cosine table above already answers. Sample covariance (`n - 1`), because the
    thirteen are the whole authored population but the question is about the shape they describe.
    """
    k = len(axes)
    m = [[float(v[i]) for i in range(k)] for v in rows.values()]
    n = len(m)
    if n < 2:
        return [[0.0] * k for _ in range(k)]
    mu = [sum(r[i] for r in m) / n for i in range(k)]
    return [[sum((r[i] - mu[i]) * (r[j] - mu[j]) for r in m) / (n - 1)
             for j in range(k)] for i in range(k)]


def _eigenvalues(a: list) -> list:
    """Descending eigenvalues of a small SYMMETRIC matrix, by cyclic Jacobi rotation.

    ⚠ HAND-ROLLED BECAUSE `numpy` IS NOT A DEPENDENCY OF THIS PACKAGE, and that is a reason to
    self-check rather than to trust the arithmetic. A symmetric rotation preserves the trace
    exactly, so `sum(eigenvalues) == trace(input)` is a property this routine cannot satisfy by
    accident — `spread()` asserts it, which is the falsifier `CLAUDE.md` §0.1 pt 3 asks for on a
    number this instrument prints. Without it a silently wrong solver would report a plausible
    effective-dimension figure and nothing would contradict it."""
    m = len(a)
    w = [row[:] for row in a]
    for _ in range(100):
        off = max(((abs(w[i][j]), i, j) for i in range(m) for j in range(i + 1, m)),
                  default=(0.0, 0, 0))
        # A Jacobi sweep on a 4x4 reaches machine precision in a handful of rotations, so this
        # is the convergence floor. No canonical source governs it and none should.
        # [JUSTIFIED: float64 convergence tolerance — arithmetic, not a game value]
        if off[0] < 1e-12:
            break
        _, p_, q_ = off
        th = (math.pi / 4 if w[p_][p_] == w[q_][q_]
              else 0.5 * math.atan2(2 * w[p_][q_], w[p_][p_] - w[q_][q_]))
        c, s = math.cos(th), math.sin(th)
        for r in range(m):
            wp, wq = w[p_][r], w[q_][r]
            w[p_][r], w[q_][r] = c * wp + s * wq, -s * wp + c * wq
        for r in range(m):
            wp, wq = w[r][p_], w[r][q_]
            w[r][p_], w[r][q_] = c * wp + s * wq, -s * wp + c * wq
    return sorted((w[i][i] for i in range(m)), reverse=True)


def spread() -> dict:
    """`{mean, magnitude, cosines, per_axis_signs, within_60deg, spectrum}` over the matrix."""
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
    cov = _covariance(rows, axes)
    ev = _eigenvalues(cov)
    trace = sum(cov[i][i] for i in range(len(axes)))
    # THE SELF-CHECK, not decoration: a Jacobi sweep preserves the trace exactly, so a solver
    # that has gone wrong cannot satisfy this. `_eigenvalues`' docstring says why a hand-rolled
    # routine needs one.
    # The trace identity is exact in real arithmetic, so this bounds accumulated rounding only.
    # Three orders looser than the convergence floor above — the direction that keeps the
    # self-check from firing on noise rather than on a wrong solver.
    # [JUSTIFIED: float64 residual tolerance — arithmetic, not a game value]
    if abs(sum(ev) - trace) > 1e-9:
        raise AssertionError(
            f"eigenvalues sum to {sum(ev)!r}, covariance trace is {trace!r} — the solver is wrong")
    # CORRELATION IS THE SAME MATRIX, NORMALISED — reported because the eigenvalues say *how many*
    # directions there are and the pairwise r says *which axes are saying the same thing*, and a
    # document citing the second must be able to re-run it rather than quote a session.
    corr = {}
    for i, a in enumerate(axes):
        for j, b in enumerate(axes):
            if j <= i:
                continue
            den = math.sqrt(cov[i][i] * cov[j][j])
            corr[(a, b)] = (cov[i][j] / den) if den else 0.0
    tot = sum(ev) or 1.0
    # PARTICIPATION RATIO — `(Σλ)² / Σλ²`, the standard read of *how many directions are actually
    # carrying variance*. It is `k` when the k axes carry equal variance and 1 when one axis
    # carries all of it, so it is directly comparable against the declared axis count.
    pr = (tot * tot) / (sum(x * x for x in ev) or 1.0)
    return dict(axes=axes, mean=dict(zip(axes, mean)), magnitude=mag, cosines=cos,
                per_axis_signs=signs,
                within_60deg=sum(1 for x in cos.values() if x > 0.5), total=n,
                spectrum=dict(eigenvalues=ev, share=[x / tot for x in ev],
                              trace=trace, effective_axes=pr, correlations=corr))


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
    sp = s["spectrum"]
    print(f"\n  HOW MANY DIRECTIONS THE {len(s['axes'])}-AXIS BASIS ACTUALLY CARRIES")
    print("  (covariance of the axis COLUMNS across the thirteen rows):")
    cum = 0.0
    for i, (v, share) in enumerate(zip(sp["eigenvalues"], sp["share"]), 1):
        cum += share
        print(f"    direction {i}   {v:.4f}   {100 * share:5.1f}%   cumulative {100 * cum:5.1f}%")
    print(f"    effective axes (participation ratio)  {sp['effective_axes']:.2f} "
          f"of {len(s['axes'])}")
    print("\n  pairwise correlation between the axes (which axes say the same thing):")
    for (a, b), r in sorted(sp["correlations"].items(), key=lambda kv: -abs(kv[1])):
        print(f"    {a:14} x {b:14} r = {r:+.3f}")
    # ⚠ NO VERDICT. Whether this spread is right is `ED-IN-0214`'s question and Jordan's to answer;
    # printing a pass/fail here would be this instrument deciding it.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
