"""REM-42: within engine/dice_engine/ the per-die mean and sigma are defined once, in `dice_engine.py`;
`sigma_leverage.py` reads them. (`modules/mass_battle/` keeps values of its own and is not asserted.)

Before this, `sigma_leverage.py` kept its own `PER_DIE = {7: (0.40, 0.800)}`, `MU_PER_DIE = 0.40`
and `SD_PER_DIE = 0.80` beside the owner's pair: equal in value, so no test could tell a copy from an
alias, and changing the owner would have left the layer on top of it silently stale. These tests can
tell: the mutation test changes the owner in a fresh interpreter and asserts the layer follows, which
a copy in any spelling would fail.

`SIGMA_N_COEFF` (0.8) is a different quantity (the sigma_n coefficient) and is not asserted here;
`PER_DIE` staying keyed by TN (a stray TN raises) is pinned in `test_tn7_always.py`.
"""
from __future__ import annotations

import pathlib
import subprocess
import sys

from engine.dice_engine import dice_engine as de
from engine.dice_engine import sigma_leverage as sl

REPO = pathlib.Path(__file__).resolve().parents[2]


def test_per_die_is_the_owners_pair():
    assert sl.PER_DIE[7] == (de.MU_PER_DIE, de.SIGMA_PER_DIE)
    assert sl.MU_PER_DIE == de.MU_PER_DIE
    assert sl.SD_PER_DIE == de.SIGMA_PER_DIE


def test_the_public_owner_names_are_the_private_pair():
    assert de.MU_PER_DIE == de._MU_PER_DIE
    assert de.SIGMA_PER_DIE == de._SIGMA_PER_DIE


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
