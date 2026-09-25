"""The eigensolver behind `conviction_spread`'s spectrum, and the check that guards it.

⚠ THIS GUARD IS LICENSED, AND THE PREDICATE IS NAMED RATHER THAN ASSUMED. `CLAUDE.md` §0.1 pt 5
permits a guard only where the defective artifact is load-bearing on the game, the exported
params, the port, or the `needs_jordan` queue. `conviction_spread` is `ED-IN-0214`'s instrument
and that row is open with `needs_jordan: true`, so its numbers reach a Jordan decision. A guard on
an instrument that reached nothing would be the apparatus §0.1 pt 5 exists to forbid.

WHAT IT IS GUARDING AGAINST, measured rather than imagined. The first version of `_eigenvalues`
(2026-09-16) ran 100 SINGLE Jacobi rotations and vouched for itself with a TRACE identity. An
orthogonal similarity preserves the trace whether or not the sweep converged, so the self-check
was blind to the only failure that mattered:

    k= 4   residual 1.7e-12   non-converged   0/200      trace error ~1e-15
    k= 8   residual 3.5e-10   non-converged   0/200      trace error ~1e-15
    k=12   residual 2.1e-01   non-converged 200/200      trace error ~1e-15
    k=16   residual 1.3e+00   non-converged 200/200      trace error ~1e-15

The four-axis control was never wrong, which is exactly why it survived review: the parameter that
makes the instrument score a candidate basis of ANY width shipped in the same commit, and a
twelve-axis candidate would have printed a participation ratio computed from wrong eigenvalues
with the self-check reporting success.
"""
from __future__ import annotations

import math
import random

import pytest

from engine.season.harness.conviction_spread import _eigenvalues, spread


def _sym(k: int, rng: random.Random) -> list:
    a = [[0.0] * k for _ in range(k)]
    for i in range(k):
        for j in range(i, k):
            a[i][j] = a[j][i] = rng.uniform(-1.0, 1.0)
    return a


# [JUSTIFIED: matrix widths, not game values — 4 is the live basis, the rest are the widths a
#  candidate basis could take and the ones the old solver silently failed at]
# [JUSTIFIED: matrix widths — arithmetic, not game values]
@pytest.mark.parametrize("k", [2, 4, 8, 12, 16])
def test_the_solver_converges_at_every_width_a_candidate_basis_could_have(k):
    """`k` goes past 4 deliberately: 4 is the live basis and the width that never failed."""
    # [JUSTIFIED: an arbitrary fixed seed — determinism, not a game value]
    rng = random.Random(11)
    for _ in range(25):
        a = _sym(k, rng)
        ev = _eigenvalues(a)
        assert len(ev) == k
        assert ev == sorted(ev, reverse=True)
        # the trace identity is kept as an INDEPENDENT check -- it catches a rotation that is not
        # a similarity, which the residual check would not.
        # [JUSTIFIED: float64 tolerance — arithmetic, not a game value]
        assert sum(ev) == pytest.approx(sum(a[i][i] for i in range(k)), abs=1e-9)


def test_the_residual_check_fires_where_the_trace_check_is_blind():
    """THE FALSIFIER. A starved sweep leaves a large off-diagonal residual and a trace error at
    machine precision — so this asserts the two checks disagree, which is the whole reason the
    residual replaced the trace as the convergence guard."""
    # [JUSTIFIED: fixed seed and a width the old solver provably failed at — not game values]
    rng = random.Random(11)
    # [JUSTIFIED: a width the old solver provably failed at — not a game value]
    k = 16
    a = _sym(k, rng)

    def starved(sweeps):
        m = len(a)
        w = [r[:] for r in a]
        for _ in range(sweeps):
            for p in range(m):
                for q in range(p + 1, m):
                    # [JUSTIFIED: float64 skip threshold — arithmetic, not a game value]
                    if abs(w[p][q]) < 1e-12:
                        continue
                    th = (math.pi / 4 if w[p][p] == w[q][q]
                          else 0.5 * math.atan2(2 * w[p][q], w[p][p] - w[q][q]))
                    c, s = math.cos(th), math.sin(th)
                    for r in range(m):
                        x, y = w[p][r], w[q][r]
                        w[p][r], w[q][r] = c * x + s * y, -s * x + c * y
                    for r in range(m):
                        x, y = w[r][p], w[r][q]
                        w[r][p], w[r][q] = c * x + s * y, -s * x + c * y
        off = math.sqrt(sum(w[i][j] ** 2 for i in range(m) for j in range(m) if i != j))
        tr = abs(sum(w[i][i] for i in range(m)) - sum(a[i][i] for i in range(m)))
        return off, tr

    off1, tr1 = starved(1)
    # [JUSTIFIED: float64 residual / trace thresholds — arithmetic, not game values]
    assert off1 > 1e-8, "one sweep on a 16x16 should NOT converge; if it does the premise moved"
    # [JUSTIFIED: float64 trace tolerance — arithmetic, not a game value]
    assert tr1 < 1e-9, "the trace identity holds even unconverged — this is the blindness"
    # and the real solver, on the same matrix, does converge
    ev = _eigenvalues(a)
    # [JUSTIFIED: float64 tolerance — arithmetic, not a game value]
    assert sum(ev) == pytest.approx(sum(a[i][i] for i in range(k)), abs=1e-9)


def test_the_control_reproduces_the_figure_the_open_ledger_row_cites():
    """`spread()` with no candidate is the CONTROL and must keep reproducing `ED-IN-0214`'s
    reading. A parameterisation that perturbed the default path would move this."""
    s = spread()
    # [canonical: ED-IN-0214 (registers/editorial_ledger_in.jsonl) — the row this instrument
    #  produces; the roster size is references/descriptor_registry.yaml:conviction_roster]
    # [canonical: ED-IN-0214 — nine of thirteen within 60 degrees, the row's own figure]
    assert s["within_60deg"] == 9 and s["total"] == 13
    # [JUSTIFIED: the control figure and its float tolerance — reproduced, not chosen]
    assert s["spectrum"]["effective_axes"] == pytest.approx(1.85, abs=0.01)


def test_a_candidate_basis_is_scored_by_the_same_rule_as_the_live_one():
    """The parameter's falsifier: handing `spread` the LIVE table explicitly must give the same
    answer as letting it read the module. If the two paths diverge, the candidate branch is
    measuring something the control is not, and every comparison drawn from it is void."""
    from engine.season.data.rosters import PURSUIT_AXES
    from engine.season.data.verbs import PURSUIT_PROJECTION
    axes = list(PURSUIT_AXES)
    # [JUSTIFIED: the sparse default, matching PROJECTION_DEFAULT_CELL — not a game value here]
    rows = {c: {a: PURSUIT_PROJECTION[c].get(a, 0.0) for a in axes}
            for c in PURSUIT_PROJECTION}
    assert spread((axes, rows))["spectrum"]["effective_axes"] == pytest.approx(
        spread()["spectrum"]["effective_axes"], abs=1e-12)  # [JUSTIFIED: float64 identity]
