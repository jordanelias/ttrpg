"""REM-42: within engine/dice_engine/ the per-die mean and sigma are defined once, in `dice_engine.py`;
`sigma_leverage.py` reads them. (`modules/mass_battle/` keeps values of its own and is not asserted.)

Before this, `sigma_leverage.py` kept its own `PER_DIE = {7: (0.40, 0.800)}`, `MU_PER_DIE = 0.40`
and `SD_PER_DIE = 0.80` beside the owner's pair: equal in value, so no test could tell a copy from an
alias, and changing the owner would have left the layer on top of it silently stale. These tests can
tell: the mutation test changes the owner in a fresh interpreter and asserts the layer follows (it
catches a copy in any spelling), and the source scan fails if a numeric literal is assigned to one of
the three names directly (a tuple-unpacking spelling is the mutation test's to catch).

`SIGMA_N_COEFF` (0.8) is a different quantity (the sigma_n coefficient) and is not asserted here.
"""
from __future__ import annotations

import ast
import pathlib
import subprocess
import sys

import pytest

from engine.dice_engine import dice_engine as de
from engine.dice_engine import sigma_leverage as sl

REPO = pathlib.Path(__file__).resolve().parents[2]
SL_SOURCE = REPO / "engine" / "dice_engine" / "sigma_leverage.py"
_ALIASED = ("PER_DIE", "MU_PER_DIE", "SD_PER_DIE")


def test_per_die_is_the_owners_pair():
    assert sl.PER_DIE[7] == (de.MU_PER_DIE, de.SIGMA_PER_DIE)
    assert sl.MU_PER_DIE == de.MU_PER_DIE
    assert sl.SD_PER_DIE == de.SIGMA_PER_DIE


def test_the_public_owner_names_are_the_private_pair():
    assert de.MU_PER_DIE == de._MU_PER_DIE
    assert de.SIGMA_PER_DIE == de._SIGMA_PER_DIE


@pytest.mark.parametrize("stray_tn", [6, 8, 0, -1])
def test_per_die_stays_keyed_by_tn_so_a_stray_tn_raises(stray_tn):
    assert set(sl.PER_DIE) == {7}
    with pytest.raises(KeyError):
        sl.PER_DIE[stray_tn]


def _literal_copies(source: str) -> list[str]:
    """Names in _ALIASED whose assigned value contains a numeric literal (a second copy)."""
    found = []
    for node in ast.walk(ast.parse(source)):
        if isinstance(node, ast.Assign):
            names = [t.id for t in node.targets if isinstance(t, ast.Name)]
        elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
            names = [node.target.id]
        else:
            continue
        if node.value is None:
            continue
        has_number = any(isinstance(n, ast.Constant) and isinstance(n.value, (int, float))
                         and not isinstance(n.value, bool) for n in ast.walk(node.value))
        # the TN key 7 is an int literal in PER_DIE's dict keys; only a float is a copy of a value
        has_float = any(isinstance(n, ast.Constant) and isinstance(n.value, float)
                        for n in ast.walk(node.value))
        if has_number and has_float:
            found.extend(n for n in names if n in _ALIASED)
    return found


def test_sigma_leverage_holds_no_float_literal_for_the_pair():
    assert _literal_copies(SL_SOURCE.read_text()) == []


def test_the_literal_scan_can_see_a_planted_copy():
    planted = SL_SOURCE.read_text() + "\nMU_PER_DIE = 0.40\n"
    assert _literal_copies(planted) == ["MU_PER_DIE"]
    planted_dict = SL_SOURCE.read_text() + "\nPER_DIE = {7: (0.40, 0.800)}\n"
    assert _literal_copies(planted_dict) == ["PER_DIE"]


def test_changing_the_owner_moves_sigma_leverage():
    """MUTATION: set the owner's pair to different values in a fresh interpreter, then import
    sigma_leverage; every alias must carry the new values. A copy would still print 0.4 / 0.8."""
    code = (
        "from engine.dice_engine import dice_engine as de\n"
        "de.MU_PER_DIE = 0.55\n"
        "de.SIGMA_PER_DIE = 0.91\n"
        "from engine.dice_engine import sigma_leverage as sl\n"
        "print(sl.PER_DIE[7], sl.MU_PER_DIE, sl.SD_PER_DIE)\n"
    )
    out = subprocess.run([sys.executable, "-c", code], cwd=REPO, check=True,
                         capture_output=True, text=True).stdout.strip()
    assert out == "(0.55, 0.91) 0.55 0.91"
