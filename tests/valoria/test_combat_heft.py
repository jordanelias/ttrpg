"""CI-tier: continuous weapon heft (WS-2 / req 4) — binary no-op invariant + within-class mass ordering.

core.heft_resp replaces the binary wt='heavy' booleans with a continuous response. These tests pin the two
properties that matter: HEFT_MODE='binary' reproduces the exact booleans (so it is a true no-op), and under
'continuous' a heavier weapon in the same class reads heavier (greatsword 2.7kg > longsword 1.4kg)."""
import os
import sys

ENGINE = os.path.join(os.path.dirname(__file__), '..', '..', 'designs', 'scene', 'combat_engine_v1')
sys.path.insert(0, ENGINE)

import pytest  # noqa: E402
pytest.importorskip("numpy")  # engine import chain needs numpy + the sim modules; skip in the lightweight validator job

import core  # noqa: E402
from combatant import WEAPONS  # noqa: E402

CFG_BIN = {'HEFT_MODE': 'binary'}
CFG_CONT = {'HEFT_MODE': 'continuous', 'HEFT_MASS_K': 0.15}


def test_binary_mode_reproduces_booleans():
    """binary heft_resp == exactly 1.0 (heavy) / 0.0 (light) for every weapon — a true no-op."""
    for n, w in WEAPONS.items():
        expected = 1.0 if w['wt'] == 'heavy' else 0.0
        assert core.heft_resp(w, CFG_BIN) == expected, n


def test_continuous_greatsword_heavier_than_longsword():
    """The headline req-4 case: a 2.7kg greatsword reads heavier than a 1.4kg longsword."""
    assert core.heft_resp(WEAPONS['greatsword'], CFG_CONT) > core.heft_resp(WEAPONS['longsword'], CFG_CONT)


def test_continuous_orders_within_heavy_class_by_mass():
    """Within the heavy class, heft is monotone in mass (longsword anchor = 1.0)."""
    h = lambda n: core.heft_resp(WEAPONS[n], CFG_CONT)
    assert h('greatsword') > h('poleaxe') > h('longsword') > h('mace')  # 2.7 > 2.5 > 1.4 > 1.2 kg
    assert abs(h('longsword') - 1.0) < 1e-9


def test_continuous_never_negative():
    """The heft response is clamped non-negative (penalty sites cannot go below the light baseline)."""
    for w in WEAPONS.values():
        assert core.heft_resp(w, CFG_CONT) >= 0.0
