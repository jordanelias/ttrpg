"""Tradition-modulation surface for the morphology levers — U10 / ED-PC-0022.

audit/2026-07-04-weapon-morphology-granularity/u10_activation_v1.md.

The U9 capstone left the six U3/U5/U7 morphology levers wired but at K=0, and found no lever robustly moves
AGGREGATE field winrate. That finding is correct but incomplete: flat physics cancels in a mirror-ish field, and —
more to the point — the levers had NO tradition-modulation surface, so they were pure rote physics equal for every
fighter. U10 (a) re-homes the mis-parked choke-thrust cost (keeping the D2 force-invariant), (b) activates the
levers to small grounded baselines, and (c) — the infrastructure fix — routes each lever through
ability_primitives.ability_factor(c, <channel>) so a school that specialises in a lever amplifies it.

HONESTY (ED-PC-0023 adversarial review): the ability layer's AGGREGATE win-rate edge is ~0 once isolated from
tradition membership (the earlier "+2.8pp specialist edge" was a CONFOUND — it compared german+ability vs
none+empty, mixing the tradition switch with the ability). The abilities produce a real PER-EVENT effect (a bind
won, a grab de-hazarded) that aggregate winrate cannot see — the situational nature U9 identified. These tests pin
the SURFACE (every lever site reaches ability_factor; default 1.0 = inert-safe) and the PER-EVENT effect — NOT an
aggregate edge, which the review showed the abilities do not robustly confer.
"""
import os
import sys

import pytest

ENGINE = os.path.join(os.path.dirname(__file__), '..', '..', 'systems', 'combat', 'combat_engine_v1')
sys.path.insert(0, ENGINE)
pytest.importorskip("numpy")

import ability_primitives as ABIL  # noqa: E402
import combat_systems as S  # noqa: E402
import contact as CT  # noqa: E402
import tradition as TR  # noqa: E402
from combatant import Combatant  # noqa: E402
from config import CFG  # noqa: E402


def test_surface_exists_and_is_inert_by_default():
    """Every lever channel is reachable via ability_factor, and with NO ability equipped every channel is exactly 1.0
    (the levers stay pure physics until a tradition attaches) — so the surface is inert-safe."""
    plain = Combatant('x', weapon='arming')
    for ch in ('edge_read', 'spine_press', 'edge_grab', 'choke_control', 'facing_regime'):
        assert ABIL.ability_factor(plain, ch) == 1.0, ch


def test_every_new_ability_targets_a_live_channel():
    """The four U10 abilities each target one of the five morphology-lever channels (no typo'd/dead lever)."""
    live = {'edge_read', 'spine_press', 'edge_grab', 'choke_control', 'facing_regime'}
    for name in ('shinogi', 'zwerchhau', 'ringen_am_schwert', 'guardia'):
        assert ABIL.ABILITIES[name]['lever'] in live, name


def test_shinogi_amplifies_the_bind_PER_EVENT_not_aggregate():
    """The HONEST deliverable, on the genuinely correct (PER-EVENT) instrument. A spine-press specialist (shinogi,
    on a single-edged katana that actually HAS a spine) wins MORE of the specific event the lever governs — the bind —
    measured directly as a higher bind_sigma, deterministically.

    NOTE (ED-PC-0023 adversarial review): the ability's AGGREGATE win-rate edge is ~0 once isolated from tradition
    membership — binds are too rare to move a full-fight tally, exactly the situational nature U9 identified. An
    earlier version of this test asserted an aggregate win-share >0.51 for `german+winden` vs `none+empty`; that was
    a CONFOUND (it measured the pre-existing german tradition-membership baseline, not the ability) and is removed.
    This test deliberately measures the per-event effect, which is real, and makes NO aggregate claim."""
    plain = Combatant('A', weapon='katana')                              # single-edge: spine > 0
    spec = Combatant('A', weapon='katana', tradition='japanese', equipped=['shinogi'])
    defr = Combatant('B', weapon='arming')                               # double-edged: spine 0
    assert S.bind_sigma(spec, defr, CFG, TR) > S.bind_sigma(plain, defr, CFG, TR)


def test_ringen_mitigates_the_grab_self_hazard():
    """Ringen am Schwert (the 'edge_grab' mitigator) lets a grappler seize a live double edge with less self-injury:
    grab_sigma vs an edged opponent is HIGHER (less negative) with Ringen equipped."""
    grabber = Combatant('A', weapon='dagger')
    grappler = Combatant('A', weapon='dagger', tradition='german', equipped=['ringen_am_schwert'])
    opp = Combatant('B', weapon='arming')                       # double-edged, grab_hazard 1.0
    assert CT.grab_sigma(grappler, opp, CFG) > CT.grab_sigma(grabber, opp, CFG)


def test_guardia_amplifies_facing_regime():
    """The Italian single-time profile (guardia) commits the facing regime harder — a larger facing_target for the
    same stance/grip/weapon."""
    plain = Combatant('a', weapon='sabre'); plain.grip_position = 0.5
    ital = Combatant('a', weapon='sabre', tradition='italian', equipped=['guardia']); ital.grip_position = 0.5
    assert abs(S.facing_target(ital, True, CFG)) > abs(S.facing_target(plain, True, CFG))


def test_levers_add_texture_without_shifting_balance():
    """THE CORRECT INSTRUMENT for a situational lever (ED-PC-0023 review + Jordan's reframe): not aggregate win-rate
    (which U9 and the first U10 write-up both wrongly used), but EVENT-DIVERGENCE WITH OUTCOME-PRESERVATION. For a
    no-GM narrative-resolving engine the value of the edge/spine/grab/choke/facing levers is the PER-FIGHT TEXTURE
    they create — different binds won, grabs that self-injure on a live edge, reads that land or don't — and the
    hook-surface those moments give abilities. A good situational lever makes many fights PLAY OUT differently while
    rarely flipping the winner. This test pins exactly that: at identical seeds, levers-on vs levers-off diverge in
    their event sequence for a meaningful fraction of fights (texture is real), yet the decided outcome changes only
    rarely (balance is preserved). Measured (observed ~16-28% divergence / ~3-8% flip); bounds are generous so this
    guards the PROPERTY, not a point value."""
    import os as _os
    _wb = _os.path.join(ENGINE, 'workbench'); sys.path.insert(0, _wb)
    from trace import run_traced_fight  # noqa: E402
    OFF = dict(CFG, LEGIB_EDGELINE_K=0, BIND_SPINE_K=0, GRAB_EDGE_K=0, CHOKE_ACCURACY_K=0, FACING_REGIME_K=0)

    def _sig(ev):
        o = []
        for e in ev:
            k = e['kind']
            if k == 'outcome':
                o.append(('H' if e['hit'] > 0 else '.') + ('B' if e['bind'] else '') + ('R' if e['riposte'] else ''))
            elif k == 'contact':
                o.append('G:' + e['outcome'])
            elif k == 'separation':
                o.append('sep:' + e['reason'])
        return tuple(o)

    for wa, wb in (('katana', 'arming'), ('dagger', 'arming')):
        n, diverged, flipped = 60, 0, 0
        for s in range(n):
            r_on, ev_on = run_traced_fight(Combatant('A', weapon=wa), Combatant('B', weapon=wb), cfg=CFG, seed=s)
            r_off, ev_off = run_traced_fight(Combatant('A', weapon=wa), Combatant('B', weapon=wb), cfg=OFF, seed=s)
            if _sig(ev_on) != _sig(ev_off):
                diverged += 1
            if r_on != r_off:
                flipped += 1
        assert diverged >= 4, f"{wa} vs {wb}: levers produced almost no per-fight texture ({diverged}/{n} diverged)"
        assert flipped <= n * 0.20, f"{wa} vs {wb}: levers shifted the OUTCOME too often ({flipped}/{n}) — not balance-neutral"


def test_ability_inert_when_weapon_lacks_the_feature():
    """A tradition ability modulates a PHYSICAL lever — it does nothing when the weapon has no such feature: shinogi on
    a double-edged (spineless) arming sword adds no spine bind edge (spine==0)."""
    spineless = Combatant('A', weapon='arming', tradition='japanese', equipped=['shinogi'])
    spineless0 = Combatant('A', weapon='arming')
    defr = Combatant('B', weapon='longsword')
    assert S.bind_sigma(spineless, defr, CFG, TR) == S.bind_sigma(spineless0, defr, CFG, TR)
