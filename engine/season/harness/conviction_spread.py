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

import json
import math
import sys
from typing import Optional

from ..data.rosters import PURSUIT_AXES
from ..data.verbs import PURSUIT_PROJECTION, PROJECTION_DEFAULT_CELL


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
    """Descending eigenvalues of a small SYMMETRIC matrix, by CYCLIC Jacobi sweeps.

    ⚠⚠ **REWRITTEN 2026-09-16 AFTER THE FIRST VERSION WAS FOUND WRONG, AND THE WAY IT WAS WRONG
    IS THE POINT.** It ran 100 SINGLE rotations, not sweeps, and vouched for itself with a TRACE
    identity. An orthogonal similarity preserves the trace whether or not the sweep has
    converged, so the check could not observe the failure it excluded — `CLAUDE.md` §0.1 pt 2
    exactly, shipped inside a docstring that claimed the opposite ("a solver that has gone wrong
    cannot satisfy this"). MEASURED on this tree, 200 random symmetric matrices per size:

        k= 4   off-diagonal residual 1.7e-12   non-converged   0/200
        k= 8   off-diagonal residual 3.5e-10   non-converged   0/200
        k=12   off-diagonal residual 2.1e-01   non-converged 200/200
        k=16   off-diagonal residual 1.3e+00   non-converged 200/200

    — and `abs(sum(ev) - trace)` stayed at ~9e-15 in EVERY one of those failures. The four-axis
    control was never affected, which is why it went unnoticed: the parameterisation exists to
    score a candidate basis of any width, and a twelve-axis candidate would have printed a
    participation ratio computed from wrong eigenvalues, silently.

    **THE CHECK IS NOW THE RESIDUAL, WHICH IS THE QUANTITY THAT CAN FAIL.** A converged Jacobi
    leaves the off-diagonal norm at machine precision; a truncated one does not. The trace
    identity is kept as a second, independent check — it catches a different error class (a
    rotation that is not a similarity) — but it is no longer claimed as the falsifier for
    convergence, because it is blind to it."""
    m = len(a)
    w = [row[:] for row in a]

    def off_norm(x):
        return math.sqrt(sum(x[i][j] ** 2 for i in range(m) for j in range(m) if i != j))

    # [JUSTIFIED: float64 convergence tolerance and sweep budget — arithmetic, not a game value]
    tol, max_sweeps = 1e-12, 60
    for _ in range(max_sweeps):
        if off_norm(w) < tol:
            break
        # A CYCLIC sweep annihilates every off-diagonal pair once. The previous version picked
        # the largest pair and did that 100 times total, which is not even two sweeps at k=12.
        for p_ in range(m):
            for q_ in range(p_ + 1, m):
                if abs(w[p_][q_]) < tol:
                    continue
                th = (math.pi / 4 if w[p_][p_] == w[q_][q_]
                      else 0.5 * math.atan2(2 * w[p_][q_], w[p_][p_] - w[q_][q_]))
                c, s_ = math.cos(th), math.sin(th)
                for r in range(m):
                    wp, wq = w[p_][r], w[q_][r]
                    w[p_][r], w[q_][r] = c * wp + s_ * wq, -s_ * wp + c * wq
                for r in range(m):
                    wp, wq = w[r][p_], w[r][q_]
                    w[r][p_], w[r][q_] = c * wp + s_ * wq, -s_ * wp + c * wq
    residual = off_norm(w)
    # [JUSTIFIED: float64 residual ceiling — arithmetic, not a game value]
    if residual > 1e-8:
        raise AssertionError(
            f"Jacobi did not converge on a {m}x{m} matrix: off-diagonal residual {residual!r}. "
            f"The eigenvalues would be wrong and the trace identity would NOT have caught it.")
    return sorted((w[i][i] for i in range(m)), reverse=True)


def spread(candidate: Optional[tuple] = None) -> dict:
    """`{mean, magnitude, cosines, per_axis_signs, within_60deg, spectrum}` over a matrix.

    ⚠ **PARAMETERISED 2026-09-16, AND THE REASON IS THAT THE UNPARAMETERISED VERSION COULD ONLY
    EVER CONDEMN.** It measured the live table and nothing else, so a session proposing a DIFFERENT
    basis could measure the thing it wanted to replace and not the thing it wanted to replace it
    with — which is `CLAUDE.md` §0.1 pt 4's asymmetric skepticism, built into an instrument. A
    proposal scored by no instrument while its target is scored by one is not a comparison.

    `candidate` is `(axes, rows)` — a list of axis names and `{conviction: {axis: value}}`. Passing
    `None` measures the LIVE table and is the control: it must reproduce the figures `ED-IN-0214`
    cites, and `main()` prints both when a candidate is given so the two are never reported alone.

    ⚠ IT SCORES WHAT IT IS HANDED AND JUDGES NOTHING. A candidate basis scoring better here is not
    thereby right — the spectrum says how many directions a matrix spans, never whether they are
    the directions the game needs. That question is `ED-IN-0214`'s and Jordan's."""
    if candidate is not None:
        axes, raw = candidate
        axes = list(axes)
        rows = {c: [float(raw[c].get(a, PROJECTION_DEFAULT_CELL)) for a in axes] for c in raw}
    else:
        axes = list(PURSUIT_AXES)
        # The DECLARED sparse default, not a literal — `decision.project` reads the same constant,
        # and an instrument that hard-codes `0.0` stops agreeing with the thing it measures the day
        # the row's `default_cell` moves.
        rows = {c: [PURSUIT_PROJECTION[c].get(a, PROJECTION_DEFAULT_CELL) for a in axes]
                for c in PURSUIT_PROJECTION}
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


def _report(s: dict, tag: str) -> None:
    """One basis, printed. Factored out of `main` so the control and a candidate render
    IDENTICALLY -- two printers would let the two halves of a comparison diverge in format, and
    a comparison whose sides are formatted differently invites reading a difference that is not
    in the numbers."""
    print(f"\n=== {tag} — {s['total']} convictions over {len(s['axes'])} axes ===")
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


def main(argv: Optional[list] = None) -> int:
    """`python -m engine.season.harness.conviction_spread [--candidate FILE.json]`.

    ⚠ **THE `--candidate` FLAG EXISTS BECAUSE THE PARAMETER WITHOUT IT WAS A DECLARED-BUT-UNREAD
    ROW.** `spread(candidate=...)` shipped on 2026-09-16 with no caller anywhere in the tree —
    the one measurement it was built for was run from an ad-hoc shell script that left nothing
    behind, so the branch was unreachable by any command and the result was unreproducible. That
    is `01_AXIOMS.md` ID-13's own prohibition, and this same package's guards exist to prevent it
    for other artifacts.

    FILE.json is `{"axes": [...], "rows": {"<Conviction>": {"<axis>": value, ...}, ...}}`.

    ⚠ **THE CONTROL IS ALWAYS PRINTED FIRST.** A candidate reported alone is the asymmetry §0.1
    pt 4 names: the replacement graded while the incumbent is not. The flag cannot suppress it."""
    argv = list(sys.argv[1:] if argv is None else argv)
    cand_path = None
    if "--candidate" in argv:
        i = argv.index("--candidate")
        if i + 1 >= len(argv):
            print("--candidate needs a path to a JSON file", file=sys.stderr)
            return 2
        cand_path = argv[i + 1]

    _report(spread(), "CONTROL: the live basis")
    if cand_path:
        with open(cand_path, encoding="utf-8") as fh:
            doc = json.load(fh)
        _report(spread((doc["axes"], doc["rows"])), f"CANDIDATE: {cand_path}")
        print("\n⚠ The instrument does not choose between these. It reports how many independent "
              "directions each\n  basis spans; whether they are the directions the game needs is "
              "ED-IN-0214's question.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
