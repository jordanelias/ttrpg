"""CI-tier: the weapon-morphology affordance gates stay synced with the live engine (WS-2 / req 5).

capabilities.py declares the true hard gates (half-sword / gap-thrust / percussive-blow) as pure predicates.
These tests assert each predicate still matches the engine's actual physics, so the registry can never drift
from what the engine enforces.
"""
import os
import sys

ENGINE = os.path.join(os.path.dirname(__file__), '..', '..', 'designs', 'scene', 'combat_engine_v1')
sys.path.insert(0, ENGINE)

import pytest  # noqa: E402
pytest.importorskip("numpy")  # engine import chain needs numpy + the sim modules; skip in the lightweight validator job

import capabilities as C  # noqa: E402
import systems as S  # noqa: E402
import core  # noqa: E402
from combatant import WEAPONS, Combatant  # noqa: E402

NAMES = [n for n in WEAPONS if n != 'longsword_halfsword']


def test_halfsword_matches_engine_form_switch():
    for n in NAMES:
        c = Combatant('x', weapon=n)
        switches = S.halfsword_target(c, True, 'heavy') != n
        assert switches == C.allowed('halfsword', n), n


def test_gap_thrust_matches_puncture_path():
    for n in NAMES:
        head = WEAPONS[n]['head']
        puncture = (core.HEAD_MODE.get(head) == 'puncture') or head == 'cut_thrust' or 'point' in S.afforded_heads(WEAPONS[n])
        assert puncture == C.allowed('gap_thrust', n), n


def test_percussive_blow_matches_percussion_mode():
    for n in NAMES:
        head = WEAPONS[n]['head']
        percussion = core.HEAD_MODE.get(head) == 'percussion'
        assert percussion == C.allowed('percussive_blow', n), n


def test_table_covers_full_roster():
    tbl = C.capability_table()
    assert set(tbl) == set(NAMES)
    for n, row in tbl.items():
        assert set(row) == set(C.CAPABILITIES)


def test_pure_cutters_have_no_gates():
    """A pure-cut weapon (greatsword / sabre) can neither half-sword, gap-thrust, nor deliver percussion."""
    for n in ('greatsword', 'sabre'):
        assert not any(C.capability_table()[n].values()), n
