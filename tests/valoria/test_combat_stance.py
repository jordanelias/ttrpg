"""CI-tier: the grip/stance writer (The Approach — footwork & stance factors).

systems.adopt_stance writes the grip: a long pole that closes_poorly gathers in (chokes up) once the measure is
closed; otherwise grounded. The lunge is set at the attack (a deep thrust extends the body). These tests pin the
stance policy and that lunge raises / choke lowers irrecoverability (the recoverability_factor grip terms)."""
import os
import sys

ENGINE = os.path.join(os.path.dirname(__file__), '..', '..', 'designs', 'scene', 'combat_engine_v1')
sys.path.insert(0, ENGINE)

import systems as S  # noqa: E402
from combatant import Combatant  # noqa: E402
from config import CFG  # noqa: E402


def test_closing_pole_chokes_up():
    assert S.adopt_stance(Combatant('x', weapon='spear'), True, CFG) == 'choke'
    assert S.adopt_stance(Combatant('x', weapon='staff'), True, CFG) == 'choke'


def test_open_or_non_pole_is_grounded():
    assert S.adopt_stance(Combatant('x', weapon='spear'), False, CFG) == 'normal'   # open measure: not gathered yet
    assert S.adopt_stance(Combatant('x', weapon='arming'), True, CFG) == 'normal'   # not a pole


def test_lunge_quality_is_weapon_derived_nonlinear():
    q = lambda w: S.lunge_quality(Combatant('x', weapon=w), CFG)
    assert q('rapier') == 1.0                        # light, hand-balanced, one-handed thruster: lunges freely
    assert q('greatsword') == 0.0                    # a cutter cannot lunge a thrust at all
    assert q('staff') == 0.0                         # blunt: no thrust
    assert 0.0 < q('longsword') < q('rapier')        # two-handed thruster lunges, but nothing like a rapier
    assert q('spear') < q('longsword')               # heavy two-hander lunges rarely (non-linear in weight)


def test_rapier_cannot_choke_but_pole_can():
    assert S.can_choke(Combatant('x', weapon='staff'), CFG)
    assert S.can_choke(Combatant('x', weapon='spear'), CFG)
    assert not S.can_choke(Combatant('x', weapon='rapier'), CFG)   # long reach, short hilt -> can't gather in, suffers close
    assert not S.can_choke(Combatant('x', weapon='arming'), CFG)


def test_lunge_raises_choke_lowers_irrecoverability():
    c = Combatant('x', weapon='longsword')
    base = S.recoverability_factor(c, CFG)
    c.grip = 'lunge'
    assert S.recoverability_factor(c, CFG) > base    # extended body = harder to recover
    c.grip = 'choke'
    assert S.recoverability_factor(c, CFG) < base    # gathered in = more recoverable
