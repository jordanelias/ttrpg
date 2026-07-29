"""[ED-MB-0041] Partition invariance of the convergence normalisation.

The adversarial audit found `_convergence_scale` computed `merged_base` as a troop-weighted MEAN while
`merged_troops` was a SUM, giving `factor == 1/N` exactly for N identical converging bodies — so N
subunits converging on one target dealt the damage of ONE. That fires precisely on Cannae/double-
envelopment geometry. These tests pin the invariant so it cannot regress silently.
"""
import os, sys
_SIM = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'sim'))
if _SIM not in sys.path:
    sys.path.insert(0, _SIM)

import pytest
from mass_battle.orchestration import _convergence_scale
from mass_battle.engine import build_army, SIDE_A_START_ROW, SIDE_B_START_ROW


def _army(n_sub, total=600.0, conc=100.0, faction='A', anchor=10):
    row = SIDE_A_START_ROW if faction == 'A' else SIDE_B_START_ROW
    per = total / n_sub
    specs = [{'shape': 'Line', 'troop_type': 'infantry', 'troops': per, 'concentration': conc,
              'starting_position': (row, anchor + i)} for i in range(n_sub)]
    return build_army(specs, faction, faction)


def _pairs_converging(attackers, defender_atom):
    """One pair per attacking subunit, all onto the SAME defender atom."""
    out = []
    for atk in attackers.subunits:
        cells = list(atk.cells())
        out.append({'atom_a': atk, 'atom_b': defender_atom,
                    'a_cells': cells, 'b_cells': list(defender_atom.cells())})
    return out


@pytest.mark.parametrize('n', [2, 3, 4])
def test_convergence_factor_is_unity_under_live_pool_model(n):
    """N identical bodies converging on one target must NOT be scaled down.

    Under the live POOL_QUALITY_MODEL the base is proportional to troops, so a genuinely merged atom of
    N*T troops has base ~N*B and the correction must be a no-op (factor == 1.0). Before the fix this
    returned exactly 1/N.
    """
    atk = _army(n, faction='A')
    dfn = _army(1, faction='B')
    pairs = _pairs_converging(atk, dfn.subunits[0])
    a_scale, _b_scale = _convergence_scale(atk, dfn, pairs)
    assert a_scale, "expected a convergence group for N>=2 attackers on one target"
    for key, factor in a_scale.items():
        assert factor == pytest.approx(1.0, rel=1e-6), (
            f"convergence factor {factor} != 1.0 for {n} converging bodies "
            f"(1/N == {1.0/n:.4f} would indicate the mean-vs-sum regression)")


def test_convergence_is_not_one_over_n():
    """Explicitly pin the regression signature: the factor must never equal 1/N.

    [ED-MB-0045 S12] The loop below is over `a_scale.values()`, so an EMPTY `a_scale` passed it
    vacuously — the exact shape §0.1 #2 names, and its sibling
    `test_convergence_factor_is_unity_under_live_pool_model` already guards it with `assert a_scale`.
    Pinned here on the measured reality instead of mere non-emptiness: `_convergence_scale` returns
    exactly one entry per converging body, measured len(a_scale) == 3 for n == 3 (2026-07-29).
    """
    n = 3
    atk = _army(n, faction='A')
    dfn = _army(1, faction='B')
    pairs = _pairs_converging(atk, dfn.subunits[0])
    a_scale, _ = _convergence_scale(atk, dfn, pairs)
    assert len(a_scale) == n, (
        f"expected one convergence entry per converging body ({n}), got {len(a_scale)} -- with an "
        f"empty a_scale the 1/N regression check below asserts nothing")
    for factor in a_scale.values():
        assert abs(factor - (1.0 / n)) > 1e-6, (
            "convergence factor collapsed to 1/N — the merged_base mean-vs-sum bug is back")


def test_single_pair_is_untouched():
    """A lone attacker is not a convergence group and must get no entry at all."""
    atk = _army(1, faction='A')
    dfn = _army(1, faction='B')
    pairs = _pairs_converging(atk, dfn.subunits[0])
    a_scale, b_scale = _convergence_scale(atk, dfn, pairs)
    assert not a_scale and not b_scale
