"""CI-tier: the grip/stance writer (The Approach — footwork & stance factors).

systems.adopt_stance writes the grip: a long pole that closes_poorly gathers in (chokes up) once the measure is
closed; otherwise grounded. The lunge is set at the attack (a deep thrust extends the body). These tests pin the
stance policy and that lunge raises / choke lowers irrecoverability (the recoverability_factor grip terms)."""
import os
import sys

ENGINE = os.path.join(os.path.dirname(__file__), '..', '..', 'systems', 'combat', 'combat_engine_v1')
sys.path.insert(0, ENGINE)

import combat_systems as S  # noqa: E402
from combatant import Combatant  # noqa: E402
from config import CFG  # noqa: E402


def test_closing_pole_gathers_in():
    # A BUTT-gripped reach pole (spear: head_len >> grip_len) is unwieldy in the close, so it GATHERS IN —
    # grip_target rises above 0 (it regrips up the haft toward balance). Phase-3 Stage-2: CONTINUOUS grip-position.
    assert S.grip_target(Combatant('x', weapon='spear'), True, CFG) > 0.0
    # [ED-PC-0053, 2026-07-29] THE STAFF ASSERTION IS RETIRED, and how it failed is the clearest single argument for
    # the change that retired it. It read `== 0.0`, justified as "derived reach < CLOSE_REACH_REF, so
    # close_unwieldiness == 0". But the staff's forward extent is 1.176 m and that fiat threshold sat at 1.18 m — so
    # a **4 mm** margin was deciding whether a two-metre quarterstaff gathers its grip in a press AT ALL. With the
    # gate replaced by the derived overhang past the body's close measure, the staff gathers (g* 0.484), which is
    # also the physically right answer: 1.18 m of shaft forward of the hand is awkward at grappling measure however
    # the staff is gripped. What the test now pins is the ORDERING that actually carries meaning — a butt-gripped
    # spear is more compromised in the close than a centre-gripped staff.
    staff = S.grip_target(Combatant('x', weapon='staff'), True, CFG)
    spear = S.grip_target(Combatant('x', weapon='spear'), True, CFG)
    assert 0.0 < staff < spear, (staff, spear)


def test_open_or_non_pole_does_not_gather():
    assert S.grip_target(Combatant('x', weapon='spear'), False, CFG) == 0.0   # open measure: full reach, no gather
    assert S.grip_target(Combatant('x', weapon='arming'), True, CFG) == 0.0   # short hilt: grip_choke_max 0, cannot gather


def test_lunge_quality_is_weapon_derived_continuous():
    # [RESOLVED, U1 / ED-PC-0010, 2026-07-08 — comment corrected 2026-07-29] The 2026-07-02 PHASE-C FLAG here
    # recorded that Phase B's real rapier pommel/guard/grip positions had pushed q('rapier') down to 0.963, just
    # under the 1.0 cap, pending a Phase-C MOMENT_MASS_EXP / cap-floor re-tune. U1's PoB recalibration closed that:
    # q('rapier') reads EXACTLY 1.0 again (measured 2026-07-29), which is what the assertion below has always
    # required — so the comment had been contradicting its own passing test for three weeks. No Phase-C item
    # remains for the rapier lunge cap.
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
