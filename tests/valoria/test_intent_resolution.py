"""ED-MB-0029 — intent as an offence/defence resolution axis (Jordan directive 2026-07-23:
"a subunit trying to hold ground and defend versus a subunit trying to rout the other resolve
differently — intent makes a big difference").

Verifies: default gated off (byte-exact), the stance-commitment signs, the delta-sigma arithmetic
(hold blunts the enemy's offence + eases its own; aggressive presses + exposes), and the emergent
battle effect (a holding pin takes fewer casualties / survives a pressing foe).
"""
import os
import random
import statistics
import sys

import pytest

_SIM = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'sim'))
if _SIM not in sys.path:
    sys.path.insert(0, _SIM)

import mass_battle.config as C  # noqa: E402
import mass_battle.orchestration as O  # noqa: E402
from mass_battle.engine import build_army, resolve_battle, SIDE_A_START_ROW, SIDE_B_START_ROW  # noqa: E402


def test_default_gated_off():
    assert C.PC_INTENT_RESOLUTION is False, "intent-resolution must default OFF (byte-exact)"


def test_stance_commitment_signs():
    m = C.STANCE_COMMITMENT
    assert m["aggressive"] == 1
    assert m["balanced"] == 0
    assert m["hold"] == -1 and m["retreat"] == -1


def test_defence_outweighs_offence():
    # the canon asymmetry (Disciplined Defence +1D; Standard Advance no effect) -> DEF > OFF
    assert C.INTENT_DEFENSE_D > C.INTENT_OFFENSE_D


def _ns_delta(stance_self, stance_enemy):
    """The ED-MB-0029 net-successes delta a subunit gains from its own + the enemy's stance."""
    cS = C.STANCE_COMMITMENT[stance_self]
    cE = C.STANCE_COMMITMENT[stance_enemy]
    return (cS * C.INTENT_OFFENSE_D + cE * C.INTENT_DEFENSE_D) * C.SIGMA_PER_D


def test_hold_blunts_enemy_offence():
    # a holder facing a balanced foe: the ENEMY's offence net against the holder drops (holder shielded)
    enemy_vs_holder = _ns_delta('balanced', 'hold')
    assert enemy_vs_holder < 0, "a defensive stance must blunt the enemy's offence"


def test_aggression_exposes():
    # an aggressor facing a balanced foe: the ENEMY's offence net against the aggressor rises (exposed)
    enemy_vs_aggressor = _ns_delta('balanced', 'aggressive')
    assert enemy_vs_aggressor > 0, "an aggressive stance must expose (raise enemy offence)"


def test_holder_own_offence_eased():
    own = _ns_delta('hold', 'balanced')
    assert own < 0, "a holding stance eases its OWN offence (cannot win alone)"


def _unit(name, faction, stance):
    sr = SIDE_A_START_ROW if faction == 'A' else SIDE_B_START_ROW
    return build_army([{'shape': 'Line', 'troop_type': 'infantry', 'unit_type': 'melee', 'stance': stance,
                        'width': 6, 'depth': 2, 'troops': 1200, 'starting_position': (sr, 25)}],
                      name, faction, stance=stance)


def _mean_holder_casualties(intent_on, n=16):
    prev_flag = O.PC_INTENT_RESOLUTION
    O.PC_INTENT_RESOLUTION = intent_on
    try:
        cas = []
        for s in range(n):
            random.seed(2_000_000 + s)
            ua = _unit('A', 'A', 'hold')       # the holding pin
            ub = _unit('B', 'B', 'aggressive')  # the pressing foe
            a0 = ua.hp_max
            resolve_battle(ua, ub, 'Line', 'Line', {}, kind='multi', max_battle_turns=40)
            cas.append(100 * (a0 - ua.hp) / a0 if a0 else 0)
        return statistics.mean(cas)
    finally:
        O.PC_INTENT_RESOLUTION = prev_flag


def test_holder_survives_better_with_intent():
    """A holding pin against a pressing foe takes fewer casualties with intent ON than OFF."""
    off = _mean_holder_casualties(False)
    on = _mean_holder_casualties(True)
    assert on < off - 2.0, f"holder should survive better with intent on (off={off:.1f} on={on:.1f})"


def test_battle_runs_with_intent_on():
    """Smoke: a full battle resolves without error under intent, and conserves the winner field."""
    prev = O.PC_INTENT_RESOLUTION
    O.PC_INTENT_RESOLUTION = True
    try:
        random.seed(2_000_123)
        r = resolve_battle(_unit('A', 'A', 'aggressive'), _unit('B', 'B', 'hold'),
                           'Line', 'Line', {}, kind='multi', max_battle_turns=40)
        assert r.get('winner') in ('A', 'B', 'draw')
    finally:
        O.PC_INTENT_RESOLUTION = prev
