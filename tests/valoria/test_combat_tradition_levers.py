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

import random  # noqa: E402
import ability_primitives as ABIL  # noqa: E402
import combat_systems as S  # noqa: E402
import contact as CT  # noqa: E402
import tradition as TR  # noqa: E402
import wrapper as W  # noqa: E402
from combatant import Combatant  # noqa: E402
from config import CFG  # noqa: E402


def test_surface_exists_and_is_inert_by_default():
    """Every lever channel is reachable via ability_factor, and with NO ability equipped every channel is exactly 1.0
    (the levers stay pure physics until a tradition attaches) — so the surface is inert-safe."""
    plain = Combatant('x', weapon='arming')
    for ch in ('edge_read', 'spine_press', 'edge_grab', 'choke_control', 'facing_regime'):
        assert ABIL.ability_factor(plain, ch) == 1.0, ch


def test_every_ability_targets_a_live_consumed_lever():
    """No ability targets a typo'd/dead lever. Every ability's lever must be one actually CONSUMED in the engine —
    the five morphology channels OR a live tradition channel/counter lever. (ED-PC-0026: after the adversarial HEMA
    regrounding, the morphology-lever abilities are exactly shinogi->spine_press and ringen_am_schwert->edge_grab;
    zwerchhau re-homed to counter_select, guardia removed — edge_read/choke_control/facing_regime are BARE levers,
    fired by weapon geometry, awaiting grounded content.)"""
    morphology = {'edge_read', 'spine_press', 'edge_grab', 'choke_control', 'facing_regime'}
    channels = {'measure', 'tempo', 'visual', 'precommit', 'leverage', 'tactile', 'balance',
                'counter_success', 'counter_select', 'anti_overcommit'}
    live = morphology | channels
    for name, a in ABIL.ABILITIES.items():
        assert a['lever'] in live, f"{name} targets unknown/dead lever {a['lever']!r}"
    # the two morphology-lever abilities whose HEMA grounding held
    assert ABIL.ABILITIES['shinogi']['lever'] == 'spine_press'
    assert ABIL.ABILITIES['ringen_am_schwert']['lever'] == 'edge_grab'
    # the regrounded ones landed on their corrected homes; guardia is gone
    assert ABIL.ABILITIES['zwerchhau']['lever'] == 'counter_select'
    assert ABIL.ABILITIES['atajo']['lever'] == 'leverage'
    assert 'guardia' not in ABIL.ABILITIES


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


def test_facing_regime_lever_live_from_weapon_class():
    """facing_regime is a BARE morphology lever (ED-PC-0026: the guardia ability was REMOVED — "guardia stretta"
    names a close-MEASURE guard, not body-FACING, a winden-class misattribution per the adversarial HEMA critic).
    The lever still fires from weapon geometry: a ONE-handed weapon fights bladed/PROFILE (facing_pref +) and a
    TWO-handed weapon squares up (facing_pref −), so facing_target carries opposite-signed regimes for a 1H vs a 2H
    weapon — live from WP.facing_pref, no ability. Isolated by toggling FACING_REGIME_K so there is no cross-weapon
    confound in the null direction."""
    off = dict(CFG); off['FACING_REGIME_K'] = 0.0
    oneH = Combatant('a', weapon='sabre'); oneH.grip_position = 0.5           # 1H: facing_pref > 0
    twoH = Combatant('a', weapon='longsword'); twoH.grip_position = 0.5       # 2H: facing_pref < 0
    # the lever moves facing_target off its lever-off baseline, in opposite directions for 1H vs 2H
    assert S.facing_target(oneH, True, CFG) != S.facing_target(oneH, True, off)
    assert (S.facing_target(oneH, True, CFG) - S.facing_target(oneH, True, off)) \
         * (S.facing_target(twoH, True, CFG) - S.facing_target(twoH, True, off)) < 0, \
        "the facing_regime lever should push a 1H (profile) and a 2H (square) weapon in opposite directions"


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


def test_levels_of_investment_grade_technique_efficacy():
    """LEVELS OF INVESTMENT (ED-PC-0023): a technique's efficacy scales with how much the fighter INVESTED, not
    tradition membership. `equipped` supports a graded dict {name: level}. Pins: (1) BACK-COMPAT — a list is
    level 1.0, byte-identical to the dict at level 1; (2) level 0 is fully INERT (1.0); (3) an AMPLIFIER grows
    monotonically with level; (4) a MITIGATOR shrinks monotonically toward 0 and never goes negative/crosses sign;
    (5) the additive path scales value*level."""
    class _C:  # minimal stub — ability_factor/bonus read only c.equipped
        def __init__(self, eq): self.equipped = eq
    # (1) back-compat: list == dict at level 1.0
    assert ABIL.ability_factor(_C(['shinogi']), 'spine_press') == ABIL.ability_factor(_C({'shinogi': 1.0}), 'spine_press')
    assert ABIL.ability_factor(_C(['shinogi']), 'spine_press') == ABIL.ABILITIES['shinogi']['value']
    # (2) level 0 inert
    assert ABIL.ability_factor(_C({'shinogi': 0.0}), 'spine_press') == 1.0
    # (3) amplifier monotone increasing in level
    amp = [ABIL.ability_factor(_C({'shinogi': L}), 'spine_press') for L in (0.0, 0.5, 1.0, 2.0)]
    assert amp == sorted(amp) and amp[0] == 1.0 and amp[-1] > amp[2] > 1.0
    # (4) mitigator monotone DECREASING, stays in (0,1], never negative
    mit = [ABIL.ability_factor(_C({'ringen_am_schwert': L}), 'edge_grab') for L in (0.0, 1.0, 2.0, 3.0)]
    assert mit == sorted(mit, reverse=True) and all(0.0 < m <= 1.0 for m in mit) and mit[-1] < mit[1]
    # (5) additive path scales with level (indes is an existing '+' ability on counter_success)
    b1 = ABIL.ability_bonus(_C({'indes': 1.0}), 'counter_success')
    b2 = ABIL.ability_bonus(_C({'indes': 2.0}), 'counter_success')
    assert b1 == pytest.approx(ABIL.ABILITIES['indes']['value']) and b2 == pytest.approx(2 * b1)


def test_investment_is_bounded_no_overflow_crash():
    """ED-PC-0024 adversarial-review fix: an unbounded value**level overflowed the downstream 1/(1+exp(-x)) sigmoids
    and CRASHED fight resolution at a plausible deep-investment level (~15-22). Pins: (1) the level is capped at
    MAX_INVESTMENT_LEVEL; (2) the composed factor is bounded [FLOOR, CEIL], finite, never 0/negative — even at an
    absurd level and with several abilities stacked on one lever; (3) a real fight with an extreme-investment fighter
    RESOLVES (no OverflowError)."""
    import math
    class _C:
        def __init__(self, eq): self.equipped = eq
    # level clamped, factor finite/bounded even at absurd level
    for L in (8.0, 30.0, 1000.0):
        fac = ABIL.ability_factor(_C({'shinogi': L}), 'spine_press')
        assert math.isfinite(fac) and ABIL.ABIL_FACTOR_FLOOR <= fac <= ABIL.ABIL_FACTOR_CEIL, (L, fac)
    # a mitigator never underflows to exactly 0 or crosses sign, even absurdly deep
    mit = ABIL.ability_factor(_C({'ringen_am_schwert': 1000.0}), 'edge_grab')
    assert 0.0 < mit <= 1.0
    # levels above the cap saturate (level 30 == level MAX)
    assert ABIL.ability_factor(_C({'shinogi': 30.0}), 'spine_press') == ABIL.ability_factor(_C({'shinogi': ABIL.MAX_INVESTMENT_LEVEL}), 'spine_press')
    # a real fight with an extreme-investment fighter must RESOLVE, not crash
    import random as _r
    a = Combatant('A', weapon='katana', tradition='japanese', equipped={'shinogi': 999})
    b = Combatant('B', weapon='arming', tradition='german', equipped={'zwerchhau': 999, 'ringen_am_schwert': 999})
    W.fight(a, b, CFG, _r.Random(3))   # no OverflowError


def test_investment_level_moves_the_per_event_effect():
    """Deeper investment in a technique produces a LARGER per-event effect — emergent expertise, not a flat grant.
    A level-2 shinogi katana out-binds a level-1 one (bind_sigma), which out-binds an uninvested one."""
    defr = Combatant('B', weapon='arming')
    b0 = S.bind_sigma(Combatant('A', weapon='katana'), defr, CFG, TR)
    b1 = S.bind_sigma(Combatant('A', weapon='katana', tradition='japanese', equipped={'shinogi': 1.0}), defr, CFG, TR)
    b2 = S.bind_sigma(Combatant('A', weapon='katana', tradition='japanese', equipped={'shinogi': 2.0}), defr, CFG, TR)
    assert b2 > b1 > b0


def test_ability_inert_when_weapon_lacks_the_feature():
    """A tradition ability modulates a PHYSICAL lever — it does nothing when the weapon has no such feature: shinogi on
    a double-edged (spineless) arming sword adds no spine bind edge (spine==0)."""
    spineless = Combatant('A', weapon='arming', tradition='japanese', equipped=['shinogi'])
    spineless0 = Combatant('A', weapon='arming')
    defr = Combatant('B', weapon='longsword')
    assert S.bind_sigma(spineless, defr, CFG, TR) == S.bind_sigma(spineless0, defr, CFG, TR)
