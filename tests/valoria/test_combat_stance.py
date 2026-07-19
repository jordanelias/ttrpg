"""CI-tier: the grip/stance writer (The Approach — footwork & stance factors).

systems.adopt_stance writes the grip: a long pole that closes_poorly gathers in (chokes up) once the measure is
closed; otherwise grounded. The lunge is set at the attack (a deep thrust extends the body). These tests pin the
stance policy and that lunge raises / choke lowers irrecoverability (the recoverability_factor grip terms)."""
import os
import sys

ENGINE = os.path.join(os.path.dirname(__file__), '..', '..', 'systems', 'combat', 'combat_engine_v1')
sys.path.insert(0, ENGINE)

import pytest  # noqa: E402
pytest.importorskip("numpy")  # engine import chain needs numpy + the sim modules; skip in the lightweight validator job

import combat_systems as S  # noqa: E402
from combatant import Combatant  # noqa: E402
from config import CFG  # noqa: E402


def test_closing_pole_gathers_in():
    # A BUTT-gripped reach pole (spear: head_len >> grip_len) is unwieldy in the close, so it GATHERS IN —
    # grip_target rises above 0 (it regrips up the haft toward balance). Phase-3 Stage-2: CONTINUOUS grip-position.
    assert S.grip_target(Combatant('x', weapon='spear'), True, CFG) > 0.0
    # A CENTRE-gripped pole (staff: head_len == grip_len) is ALREADY close-capable (derived reach < CLOSE_REACH_REF),
    # so close_unwieldiness == 0 -> it does NOT need to gather (grip_target 0).
    assert S.grip_target(Combatant('x', weapon='staff'), True, CFG) == 0.0


def test_open_or_non_pole_does_not_gather():
    assert S.grip_target(Combatant('x', weapon='spear'), False, CFG) == 0.0   # open measure: full reach, no gather
    assert S.grip_target(Combatant('x', weapon='arming'), True, CFG) == 0.0   # short hilt: grip_choke_max 0, cannot gather


def test_lunge_quality_is_weapon_derived_continuous():
    # [PHASE-C FLAG, 2026-07-02] morphology-rearch Phase B's real rapier pommel/guard/grip positions shift
    # PoB_frac slightly (hand-balance term), so q('rapier') now reads 0.963, just under the 1.0 cap — a Phase-C
    # re-tune item (MOMENT_MASS_EXP / the cap floor), not a regression; the ordering below is unaffected.
    # [RE-ANNOTATED, 2026-07-03, I8 capstone] R2 (I0->I8) is complete and did not touch MOMENT_MASS_EXP or the
    # cap floor; still correctly deferred to Phase C — see the closing-distance-redesign folder's
    # i8_capstone_audit.md item 7.
    q = lambda w: S.lunge_quality(Combatant('x', weapon=w), CFG)
    assert q('rapier') == 1.0                        # light, hand-balanced, one-handed, point-concentrated: lunges freely (capped)
    assert q('greatsword') < 0.25                    # heavy forward cutter: a poor lunge (LOW via mass+balance, not a hard-0 head gate)
    assert q('staff') < 0.1                          # blunt (point_concentration ~0): barely lunges
    assert 0.0 < q('longsword') < q('rapier')        # two-handed thruster lunges, but nothing like a rapier
    assert q('spear') < q('longsword')               # forward-balanced reach pole: poor lunge recovery


def test_rapier_cannot_choke_but_pole_can():
    assert S.can_choke(Combatant('x', weapon='staff'), CFG)
    assert S.can_choke(Combatant('x', weapon='spear'), CFG)
    assert not S.can_choke(Combatant('x', weapon='rapier'), CFG)   # long reach, short hilt -> can't gather in, suffers close
    assert not S.can_choke(Combatant('x', weapon='arming'), CFG)


def test_lunge_raises_gather_lowers_irrecoverability():
    # extended body (lunge) = harder to recover
    c = Combatant('x', weapon='longsword')
    base = S.recoverability_factor(c, CFG)
    c.lunge_depth = 1.0
    assert S.recoverability_factor(c, CFG) > base
    # GATHERING IN lowers it — for a pole that CAN gather (the spear gathers to its working balance)
    s = Combatant('x', weapon='spear')
    s_open = S.recoverability_factor(s, CFG)
    s.grip_position = 1.0
    assert S.recoverability_factor(s, CFG) < s_open
