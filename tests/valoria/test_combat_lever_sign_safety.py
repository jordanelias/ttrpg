"""SIGN-SAFETY probes for the seven levers the GENERIC calibration abilities fill (PC-17, ED-PC-0059).

One probe per (lever, consuming site, side), run for EVERY ability on that lever, so each (lever, tier) generic is
checked at every site its factor reaches. The levers: visual, precommit, tactile, tempo, balance, edge_read,
choke_control. Each probe returns GOODNESS FOR THE INVESTING OWNER on that site's channel, so the property is the
same everywhere: investing more never makes the owner worse, at levels 0, 0.5, 1, 2, 4, 8. ONE EXCEPTION: the
counter_select probe returns the SELECTION probability of a counter (a frequency), not the owner's benefit from it (a
failed counter leaves the defender undefended); the benefit was measured once, by duel, and is in ED-PC-0059.

WHAT A PROBE CAN SEE. A multiplicative lever is sign-safe when it scales a NON-NEGATIVE own-side quantity (a
reading, a balance, a probability) or enters as `lever_log_edge`; it is sign-BLIND when it scales a SIGNED
differential (the ED-PC-0045 defect, still present at `init_emphasis_sigma` until PC-17 rewrote it). So every
probe that has a signed differential beside its lever is built with the owner BEHIND on it (a computed premise,
asserted against a mirrored reference): a sign-blind form would then show as a worsening, where in an advantaged
configuration it would not.

SITE CONDITIONS (asserted as premises, so a probe that stops meeting them fails loudly):
  · edge_read acts only where the owner's weapon has cut-line entropy (`edge_lines` > 0: a double edge reads 1.0);
    on an edgeless weapon the factor is exactly inert.
  · choke_control acts only on a pole gathered above grip 0 (`choke_counterbalance` > 0); at grip 0 it is inert.
    It is a MITIGATOR: its site adds to the read the OPPONENT takes, so a factor below 1 helps its owner.
  · balance probes include an Agility 1 / Strength 1 owner, where `balance_eff` is exactly 0 (attributes are not
    clamped): the owner's own term vanishes, so a correct own-side product is exactly inert there, while a form that
    scaled the signed footwork differential would worsen the owner. That boundary probe has no liveness half.
  · tactile and the two read levers (visual, precommit) are own-side positive products.

THE VACUITY TRAP (ED-PC-0028). A technique equipped outside the fighter's known tradition is INERT, so a probe that
forgot to set the teaching tradition would pass on broken code. Every probe sets the ability's own tradition, and
`test_probe_is_live_and_tradition_gated` asserts both halves: taught, the probe MOVES at level 1; untaught
(`tradition='none'`), it is exactly inert.

MUTATION RECORD (CLAUDE.md §0.1 pt 2: each probe must be able to observe the failure it excludes). Run at PC-17's
build, 2026-11-06: each sign-broken variant applied to the site, this file run, the site restored. Every variant was
killed, and only at the site it broke:
  · the factor INVERTED (`*f` -> `/f`) at each own-side site: read_contest's aggressor visual, reopen_prob (both
    sides), disengage_clean_p (both sides), bind_sigma's tactile read (both sides), init_steal_factor (bind and
    open), counter_select, tempo_pressure (both sides), reach_sigma's and pursuit_sigma's footwork (each side) ->
    3 failed each; read_contest's DEFENDER visual and DEFENDER precommit -> 6 failed each (the own-site probe's 3 and
    the 3 cross-lever cases below, which call the same function); legibility's edge_read -> 7 and choke_control -> 6
    (seen at legibility and through read_contest); init_overcommit_loss `/f` -> `*f`: 3 failed
  · init_emphasis_sigma restored to its pre-PC-17 form (signed sum x the aggressor's tempo factor): 6 failed (the
    owner-behind aggressor worsens; the defender's factor is not read at all); lever_log_edge's arguments swapped: 6
  · the footwork factor moved onto the SIGNED differential (ratio form, ED-PC-0045's defect) in reach_sigma or
    pursuit_sigma: 12 failed each, the Agility 1 / Strength 1 probes among them
  · the tradition gate deleted from ability_primitives._invested: 75 failed at the build, 76 after the close (every live
    probe's untaught half, and the placement test's wrong-tradition case)
  · edge_read's refined tier put back at the plan's x1.50 (it ships REVISED to x1.40, ability_primitives.
    GENERIC_LEVERS' edge_read row), WITH the floor in combat_systems.legibility removed: the single-generic cross-lever probe fails
    on its legibility half (a spear thrust at level 8 reads -0.225) and, with that half disabled, on its read half
    (keen_eye_basic lowers p_read 0.0273 -> 0.0266 -> ... against a spear at level 8); at x1.40 it passes
  · the floor `max(0.0, legib)` in combat_systems.legibility removed, tier at x1.40: the STACKED probe fails on its
    floor assertion (refined L8 + practiced L8 on a thrust reads below 0). The tier back at x1.50 WITH the floor: the
    single-generic probe fails (`legib > 0.0`: at the floor)
  · COUNTS re-measured after the close added the stacked and placement tests (182 cases in all): the tradition gate
    deleted fails 76 (the placement test fails with it); edge_read inverted at legibility fails 7, choke_control 6
"""
import os
import sys
from collections import namedtuple

import pytest

ENGINE = os.path.join(os.path.dirname(__file__), '..', '..', 'modules', 'combat')
sys.path.insert(0, ENGINE)

import ability_primitives as ABIL  # noqa: E402
import combat_systems as S  # noqa: E402
import tradition as TR  # noqa: E402
import weapon_physics as WP  # noqa: E402
from combatant import Combatant  # noqa: E402
from config import CFG  # noqa: E402

LEVELS = (0.0, 0.5, 1.0, 2.0, 4.0, 8.0)
LEVERS = ('visual', 'precommit', 'tactile', 'tempo', 'balance', 'edge_read', 'choke_control')

# a fighter who is BEHIND on reading and footwork, and one who is AHEAD (attributes only; weapons per probe)
# CR-85 (ED-IN-0330) deleted `history` from every sigma term and renamed the input `faculty`, which feeds only the pool
# and the Ob; no probe here reads a pool or an Ob, so the builds carry none.
WEAK = dict(att=1, agi=2, strength=2)
STRONG = dict(att=5, agi=6, strength=6)
FLOOR_BAL = dict(att=1, agi=1, strength=1)   # balance_eff is exactly 0 here


def _own(ability, tradition, level, **kw):
    """The investing owner. Level 0 is the UNEQUIPPED baseline; the tradition is always the one passed in."""
    return Combatant('own', tradition=tradition, equipped=({} if level <= 0.0 else {ability: level}), **kw)


def _opp(**kw):
    return Combatant('opp', **kw)


class _FixedRng:
    """Fixed-uniform stand-in: the probes read probabilities, never the draw's outcome."""

    def __init__(self, u):
        self._u = u

    def random(self):
        return self._u

    def randrange(self, n):
        return 0


def _p_read(aggressor, defender):
    return S.read_contest(aggressor, defender, 3.0, 0.0, 0.0, 0.0, CFG, _FixedRng(0.5), TR)['p_read']


def _counter_p(defender):
    """The exact selection probability behind `counter_select`'s single draw, by bisection (no sampling)."""
    lo, hi = 0.0, 1.0
    for _ in range(64):
        mid = (lo + hi) / 2.0
        if S.counter_select(defender, CFG, _FixedRng(mid), TR):
            lo = mid
        else:
            hi = mid
    return lo


def _reach(aggressor, defender):
    er = {aggressor: S.reach_base(aggressor, CFG), defender: S.reach_base(defender, CFG)}
    return S.reach_sigma(aggressor, defender, er, 0.0, 0.0, CFG, TR)


def _gathered(c, grip=1.0):
    c.grip_position = grip
    return c


# ── the probes: goodness FOR THE OWNER at one site ─────────────────────────────────────────────────────
# visual / precommit — read_contest (p_read = logistic(read_d - read_a)), reopen_prob, disengage_clean_p
def _read_as_defender(ab, tr, lv):
    return _p_read(_opp(weapon='spear', **STRONG), _own(ab, tr, lv, weapon='arming', **WEAK))


def _read_as_defender_ref():
    return _p_read(_opp(weapon='spear', **STRONG), _opp(weapon='arming', **STRONG))


def _read_as_aggressor(ab, tr, lv):
    return 1.0 - _p_read(_own(ab, tr, lv, weapon='arming', **WEAK), _opp(weapon='spear', **STRONG))


def _read_as_aggressor_ref():
    return 1.0 - _p_read(_opp(weapon='arming', **STRONG), _opp(weapon='spear', **STRONG))


def _reopen_as_longer(ab, tr, lv):
    return S.reopen_prob(_own(ab, tr, lv, weapon='spear', **WEAK), _opp(weapon='dagger', armor='none', **STRONG),
                         0.5, 0.0, False, CFG, TR)


def _reopen_as_longer_ref():
    return S.reopen_prob(_opp(weapon='spear', **STRONG), _opp(weapon='dagger', armor='none', **STRONG),
                         0.5, 0.0, False, CFG, TR)


def _reopen_as_shorter(ab, tr, lv):
    return -S.reopen_prob(_opp(weapon='spear', **STRONG), _own(ab, tr, lv, weapon='dagger', armor='none', **WEAK),
                          0.5, 0.0, False, CFG, TR)


def _reopen_as_shorter_ref():
    return -S.reopen_prob(_opp(weapon='spear', **STRONG), _opp(weapon='dagger', armor='none', **STRONG),
                          0.5, 0.0, False, CFG, TR)


def _clean_as_longer(ab, tr, lv):
    return S.disengage_clean_p(_own(ab, tr, lv, weapon='spear', **WEAK), _opp(weapon='dagger', **STRONG), CFG, TR)


def _clean_as_longer_ref():
    return S.disengage_clean_p(_opp(weapon='spear', **STRONG), _opp(weapon='dagger', **STRONG), CFG, TR)


def _clean_as_shorter(ab, tr, lv):
    return -S.disengage_clean_p(_opp(weapon='spear', **STRONG), _own(ab, tr, lv, weapon='dagger', **WEAK), CFG, TR)


def _clean_as_shorter_ref():
    return -S.disengage_clean_p(_opp(weapon='spear', **STRONG), _opp(weapon='dagger', **STRONG), CFG, TR)


# tactile — bind_sigma's tactile read (+ve favours the bind aggressor) and the bind initiative steal
def _bind_as_aggressor(ab, tr, lv):
    return S.bind_sigma(_own(ab, tr, lv, weapon='dagger', **WEAK), _opp(weapon='poleaxe', **STRONG), CFG, TR)


def _bind_as_aggressor_ref():
    return S.bind_sigma(_opp(weapon='poleaxe', **STRONG), _opp(weapon='poleaxe', **STRONG), CFG, TR)


def _bind_as_defender(ab, tr, lv):
    return -S.bind_sigma(_opp(weapon='poleaxe', **STRONG), _own(ab, tr, lv, weapon='dagger', **WEAK), CFG, TR)


def _bind_as_defender_ref():
    return -S.bind_sigma(_opp(weapon='poleaxe', **STRONG), _opp(weapon='poleaxe', **STRONG), CFG, TR)


def _steal_in_bind(ab, tr, lv):
    return S.init_steal_factor(_own(ab, tr, lv, weapon='arming', **WEAK), True, CFG, TR)


# tempo — init_emphasis_sigma (signed; the PC-17 rewrite), counter_select, the open steal, overcommit loss,
# tempo_pressure's read term
def _emphasis_as_aggressor(ab, tr, lv):
    return S.init_emphasis_sigma(_own(ab, tr, lv, weapon='arming', **WEAK), _opp(weapon='arming', **STRONG), CFG, TR)


def _emphasis_as_aggressor_ref():
    return S.init_emphasis_sigma(_opp(weapon='arming', **STRONG), _opp(weapon='arming', **STRONG), CFG, TR)


def _emphasis_as_defender(ab, tr, lv):
    return -S.init_emphasis_sigma(_opp(weapon='arming', **STRONG), _own(ab, tr, lv, weapon='arming', **WEAK), CFG, TR)


def _emphasis_as_defender_ref():
    return -S.init_emphasis_sigma(_opp(weapon='arming', **STRONG), _opp(weapon='arming', **STRONG), CFG, TR)


def _counter(ab, tr, lv):
    return _counter_p(_own(ab, tr, lv, weapon='arming', disp=6, **WEAK))


def _steal_in_open(ab, tr, lv):
    return S.init_steal_factor(_own(ab, tr, lv, weapon='arming', **WEAK), False, CFG, TR)


def _overcommit_loss(ab, tr, lv):
    return -S.init_overcommit_loss(_own(ab, tr, lv, weapon='arming', **WEAK), 0.5, CFG, TR)


def _tempo_pressure_own(ab, tr, lv):
    return S.tempo_pressure(_own(ab, tr, lv, weapon='arming', **WEAK), _opp(weapon='arming', **STRONG), CFG, TR)


def _tempo_pressure_own_ref():
    return S.tempo_pressure(_opp(weapon='arming', **STRONG), _opp(weapon='arming', **STRONG), CFG, TR)


def _tempo_pressure_opp(ab, tr, lv):
    return -S.tempo_pressure(_opp(weapon='arming', **STRONG), _own(ab, tr, lv, weapon='arming', **WEAK), CFG, TR)


def _tempo_pressure_opp_ref():
    return -S.tempo_pressure(_opp(weapon='arming', **STRONG), _opp(weapon='arming', **STRONG), CFG, TR)


# balance — reach_sigma's footwork term (reach_sigma is the DEFENDER's goodness) and pursuit_sigma's
def _reach_as_defender(ab, tr, lv, attrs=WEAK):
    return _reach(_opp(weapon='spear', armor='none', **STRONG), _own(ab, tr, lv, weapon='dagger', armor='none', **attrs))


def _reach_as_defender_ref():
    return _reach(_opp(weapon='spear', armor='none', **STRONG), _opp(weapon='spear', armor='none', **STRONG))


def _reach_as_aggressor(ab, tr, lv, attrs=WEAK):
    return -_reach(_own(ab, tr, lv, weapon='dagger', armor='none', **attrs), _opp(weapon='spear', armor='none', **STRONG))


def _reach_as_aggressor_ref():
    return -_reach(_opp(weapon='spear', armor='none', **STRONG), _opp(weapon='spear', armor='none', **STRONG))


def _pursuit_as_pursuer(ab, tr, lv, attrs=WEAK):
    return S.pursuit_sigma(_own(ab, tr, lv, weapon='dagger', armor='none', **attrs),
                           _opp(weapon='spear', armor='none', **STRONG), 0.0, 0.0, CFG, TR)


def _pursuit_as_pursuer_ref():
    return S.pursuit_sigma(_opp(weapon='spear', armor='none', **STRONG),
                           _opp(weapon='spear', armor='none', **STRONG), 0.0, 0.0, CFG, TR)


def _pursuit_as_withdrawer(ab, tr, lv, attrs=WEAK):
    return -S.pursuit_sigma(_opp(weapon='dagger', armor='none', **STRONG),
                            _own(ab, tr, lv, weapon='spear', armor='none', **attrs), 0.0, 0.0, CFG, TR)


def _pursuit_as_withdrawer_ref():
    return -S.pursuit_sigma(_opp(weapon='dagger', armor='none', **STRONG),
                            _opp(weapon='spear', armor='none', **STRONG), 0.0, 0.0, CFG, TR)


def _floor(probe):
    """The Agility 1 / Strength 1 variant of a balance probe: the owner's balance_eff is exactly 0."""
    return lambda ab, tr, lv: probe(ab, tr, lv, attrs=FLOOR_BAL)


# edge_read / choke_control — legibility (the read the OPPONENT takes of the owner's attack: lower is better for
# the owner), and the same site through read_contest, where the owner is the aggressor
def _legib_edge(ab, tr, lv):
    return -S.legibility(_own(ab, tr, lv, weapon='arming', **WEAK), 3.0, CFG)


def _legib_edge_read_contest(ab, tr, lv):
    return 1.0 - _p_read(_own(ab, tr, lv, weapon='arming', **WEAK), _opp(weapon='spear', **STRONG))


def _legib_choke(ab, tr, lv):
    return -S.legibility(_gathered(_own(ab, tr, lv, weapon='poleaxe', **WEAK)), 3.0, CFG)


def _legib_choke_read_contest(ab, tr, lv):
    return 1.0 - _p_read(_gathered(_own(ab, tr, lv, weapon='poleaxe', **WEAK)), _opp(weapon='spear', **STRONG))


# `live`: the site must MOVE for a taught level-1 owner (False only for the balance floor, where the owner's own term
# is 0 by construction and the factor is exactly inert — the property checked there is that it stays inert).
Probe = namedtuple('Probe', 'label site probe reference live')
_P = Probe

PROBES = {
    'visual': [
        _P('defender reads a spear attack, behind on reading', 'combat_systems.read_contest',
           _read_as_defender, _read_as_defender_ref, True),
        _P('aggressor is read by a spear defender, behind on reading', 'combat_systems.read_contest',
           _read_as_aggressor, _read_as_aggressor_ref, True),
        _P('longer weapon reopens distance, behind on reading', 'combat_systems.reopen_prob',
           _reopen_as_longer, _reopen_as_longer_ref, True),
        _P('shorter weapon denies the reopening, behind on reading', 'combat_systems.reopen_prob',
           _reopen_as_shorter, _reopen_as_shorter_ref, True),
        _P('longer weapon breaks clean, behind on reading', 'combat_systems.disengage_clean_p',
           _clean_as_longer, _clean_as_longer_ref, True),
        _P('shorter weapon reads the break, behind on reading', 'combat_systems.disengage_clean_p',
           _clean_as_shorter, _clean_as_shorter_ref, True),
    ],
    'precommit': [
        _P('defender reads a spear attack, behind on reading', 'combat_systems.read_contest',
           _read_as_defender, _read_as_defender_ref, True),
    ],
    'tactile': [
        _P('dagger binds poleaxe as AGGRESSOR, behind on reading', 'combat_systems.bind_sigma',
           _bind_as_aggressor, _bind_as_aggressor_ref, True),
        _P('dagger binds poleaxe as DEFENDER, behind on reading', 'combat_systems.bind_sigma',
           _bind_as_defender, _bind_as_defender_ref, True),
        _P('initiative steal in the bind', 'combat_systems.init_steal_factor', _steal_in_bind, None, True),
    ],
    'tempo': [
        _P('initiative emphasis as AGGRESSOR, behind on agility and reading',
           'combat_systems.init_emphasis_sigma', _emphasis_as_aggressor, _emphasis_as_aggressor_ref, True),
        _P('initiative emphasis as DEFENDER, behind on agility and reading',
           'combat_systems.init_emphasis_sigma', _emphasis_as_defender, _emphasis_as_defender_ref, True),
        _P('aggressive disposition bleeds the counter selection', 'combat_systems.counter_select',
           _counter, None, True),
        _P('initiative steal in the open', 'combat_systems.init_steal_factor', _steal_in_open, None, True),
        _P('initiative lost to over-commitment', 'combat_systems.init_overcommit_loss', _overcommit_loss, None, True),
        _P('tempo pressure, owner acting, behind on reading', 'combat_systems.tempo_pressure',
           _tempo_pressure_own, _tempo_pressure_own_ref, True),
        _P('tempo pressure, owner as the opponent, behind on reading', 'combat_systems.tempo_pressure',
           _tempo_pressure_opp, _tempo_pressure_opp_ref, True),
    ],
    'balance': [
        _P('out-reached dagger DEFENDER, behind on footwork', 'combat_systems.reach_sigma',
           _reach_as_defender, _reach_as_defender_ref, True),
        _P('dagger AGGRESSOR closing on a spear, behind on footwork', 'combat_systems.reach_sigma',
           _reach_as_aggressor, _reach_as_aggressor_ref, True),
        _P('PURSUER of a withdrawing spear, behind on footwork', 'combat_systems.pursuit_sigma',
           _pursuit_as_pursuer, _pursuit_as_pursuer_ref, True),
        _P('WITHDRAWER from a dagger pursuit, behind on footwork', 'combat_systems.pursuit_sigma',
           _pursuit_as_withdrawer, _pursuit_as_withdrawer_ref, True),
        _P('out-reached DEFENDER at Agility 1 / Strength 1 (balance_eff 0)', 'combat_systems.reach_sigma',
           _floor(_reach_as_defender), _reach_as_defender_ref, False),
        _P('AGGRESSOR at Agility 1 / Strength 1 (balance_eff 0)', 'combat_systems.reach_sigma',
           _floor(_reach_as_aggressor), _reach_as_aggressor_ref, False),
        _P('PURSUER at Agility 1 / Strength 1 (balance_eff 0)', 'combat_systems.pursuit_sigma',
           _floor(_pursuit_as_pursuer), _pursuit_as_pursuer_ref, False),
        _P('WITHDRAWER at Agility 1 / Strength 1 (balance_eff 0)', 'combat_systems.pursuit_sigma',
           _floor(_pursuit_as_withdrawer), _pursuit_as_withdrawer_ref, False),
    ],
    'edge_read': [
        _P('double-edged arming sword attacks', 'combat_systems.legibility', _legib_edge, None, True),
        _P('double-edged arming sword attacks, read by a spear defender', 'combat_systems.read_contest',
           _legib_edge_read_contest, None, True),
    ],
    'choke_control': [
        _P('poleaxe gathered to grip 1.0 attacks', 'combat_systems.legibility', _legib_choke, None, True),
        _P('poleaxe gathered to grip 1.0 attacks, read by a spear defender', 'combat_systems.read_contest',
           _legib_choke_read_contest, None, True),
    ],
}

GENERICS = tuple(sorted((n, a['lever'], a['tradition']) for n, a in ABIL.ABILITIES.items()
                        if a['grade'] == 'GENERIC'))
CASES = [(n, lever, trad, p) for n, lever, trad in GENERICS for p in PROBES[lever]]
IDS = [f'{n}-{p.site.split(".")[-1]}-{p.label}' for n, _l, _t, p in CASES]


def test_the_probe_set_covers_every_generic_at_every_site():
    """21 generics, 7 levers x 3 tiers, each reached by every probe its lever has; no lever without a probe."""
    assert len(GENERICS) == 21, GENERICS
    assert {lever for _n, lever, _t in GENERICS} == set(LEVERS) == set(PROBES)
    assert all(a['op'] == '*' for n, a in ABIL.ABILITIES.items() if a['grade'] == 'GENERIC')
    assert len(CASES) == sum(3 * len(PROBES[lever]) for lever in LEVERS), len(CASES)


@pytest.mark.parametrize('ability,lever,tradition,probe', CASES, ids=IDS)
def test_investing_never_worsens_its_owner(ability, lever, tradition, probe):
    """THE PROPERTY: goodness for the owner is non-decreasing in the invested level, at every site the lever
    reaches; where a mirrored reference exists the owner is asserted BEHIND first, so a sign-blind form (one that
    scales a signed differential) would show here as a worsening."""
    base = probe.probe(ability, tradition, 0.0)
    if probe.reference is not None:
        ref = probe.reference()
        assert base < ref, (
            f'{probe.label!r} is no longer DISADVANTAGED for the owner ({base!r} >= reference {ref!r}): a '
            f'non-worsening assertion in an advantaged configuration cannot see a sign-blind lever; re-pick the builds')
    vals = [probe.probe(ability, tradition, lv) for lv in LEVELS]
    assert vals == sorted(vals), (
        f'SIGN-BLIND or NON-MONOTONE lever at {probe.site}: investing in {ability!r} (lever {lever!r}) moves its '
        f'owner {vals!r} over levels {LEVELS} [{probe.label}]')


@pytest.mark.parametrize('ability,lever,tradition,probe', CASES, ids=IDS)
def test_probe_is_live_and_tradition_gated(ability, lever, tradition, probe):
    """THE ANTI-VACUITY HALF (ED-PC-0028): untaught, exactly inert; taught, the probe MOVES (or, for the balance
    floor, stays exactly inert because the owner's own term is 0)."""
    assert probe.probe(ability, 'none', 1.0) == probe.probe(ability, 'none', 0.0), (
        f'{ability!r} is not tradition-gated at {probe.site}')
    off, on = probe.probe(ability, tradition, 0.0), probe.probe(ability, tradition, 1.0)
    if probe.live:
        assert on != off, (
            f'VACUOUS PROBE: {ability!r} (lever {lever!r}, tradition {tradition!r}) does not move {probe.site} '
            f'[{probe.label}] — it cannot observe the failure it excludes (CLAUDE.md §0.1 pt 2)')
    else:
        assert on == off, f'{ability!r} moved {probe.site} for an owner whose own term is 0 [{probe.label}]'


def test_site_conditions_hold():
    """The premises the probes stand on, measured rather than assumed."""
    weak_bal = Combatant('x', **FLOOR_BAL)
    assert S.balance_eff(weak_bal, 0.0, CFG) == 0.0
    arming, mace = Combatant('a', weapon='arming'), Combatant('m', weapon='mace')
    assert WP.edge_lines(arming.w) == 1.0 and WP.edge_lines(mace.w) == 0.0
    pole = Combatant('p', weapon='poleaxe')
    assert S.choke_counterbalance(pole, CFG) == 0.0
    assert S.choke_counterbalance(_gathered(Combatant('p', weapon='poleaxe')), CFG) > 0.0
    checked = 0
    for lever, weapon in (('edge_read', 'mace'), ('choke_control', 'poleaxe')):
        for n, lv, trad in GENERICS:
            if lv != lever:
                continue
            # edge_read on an edgeless weapon, choke_control on a pole held at grip 0: exactly inert
            plain = Combatant('o', weapon=weapon, tradition=trad)
            invested = Combatant('o', weapon=weapon, tradition=trad, equipped={n: 8.0})
            assert S.legibility(invested, 3.0, CFG) == S.legibility(plain, 3.0, CFG), (n, weapon)
            checked += 1
    assert checked == 6, checked


EDGE_READ_GENERICS = tuple((n, t) for n, lever, t in GENERICS if lever == 'edge_read')
READ_GENERICS = tuple((n, t) for n, lever, t in GENERICS if lever in ('visual', 'precommit'))
# thrusting double edges: spear and rapier, and the jian, whose ornament (distraction) makes it the roster's worst case
THRUSTING_DOUBLE_EDGES = ('spear', 'rapier', 'jian')


def _thrusting(c):
    c.sel_dmg = 'puncture'          # legibility's LOWEST base (LEGIB_THRUST): the worst case for this bound
    return c


@pytest.mark.parametrize('ability,tradition', EDGE_READ_GENERICS, ids=[n for n, _t in EDGE_READ_GENERICS])
def test_edge_read_keeps_legibility_non_negative_and_the_read_levers_sign_safe(ability, tradition):
    """The CROSS-LEVER case (PC-17's tier revision). edge_read SUBTRACTS from the aggressor's legibility, which
    multiplies the defender's read_d; were it driven below 0, the defender's own visual / precommit factors would
    scale a NEGATIVE read and make investing worse. combat_systems.legibility is floored at 0 (the stacking case, below),
    but a SINGLE generic must not reach that floor at all: at x1.50 for the refined tier it would (jian, spear and
    rapier at level 8), so the tier was revised to x1.40. Every edge_read generic at every level, on every thrusting
    double edge: legibility > 0, and the defender's visual / precommit generics never lower p_read as their level rises."""
    checked = 0
    for weapon in THRUSTING_DOUBLE_EDGES:
        assert WP.edge_lines(Combatant('w', weapon=weapon).w) == 1.0, weapon
        for lv in LEVELS:
            agg = _thrusting(_own(ability, tradition, lv, weapon=weapon))
            legib = S.legibility(agg, 3.0, CFG)
            # strictly positive: a single generic must stay OFF combat_systems.legibility's floor at every level, so the
            # tier revision (x1.40) is observed here and not hidden by the floor
            assert legib > 0.0, (
                f'{ability!r} at level {lv} drives the legibility of a {weapon} thrust to {legib!r}: at the floor, '
                f"the defender's read levers go inert (revise the tier, PC-17)")
            for d_ability, d_tradition in READ_GENERICS:
                ps = [_p_read(_thrusting(_own(ability, tradition, lv, weapon=weapon)),
                              Combatant('d', weapon='arming', tradition=d_tradition,
                                        equipped=({} if dl <= 0.0 else {d_ability: dl})))
                      for dl in LEVELS]
                assert ps == sorted(ps), (
                    f"defender's {d_ability!r} lowers p_read against {ability!r} L{lv} on a {weapon}: {ps!r}")
                checked += 1
    assert checked == len(THRUSTING_DOUBLE_EDGES) * len(LEVELS) * len(READ_GENERICS) == 108, checked


def _stacked(weapon, levels):
    """A cross-trained fighter: several edge_read generics from three traditions, factors multiplying."""
    eq = {n: lv for (n, _t), lv in zip(EDGE_READ_GENERICS, levels)}
    c = Combatant('stack', weapon=weapon, tradition='none', equipped=eq)
    c.known_traditions = tuple(t for _n, t in EDGE_READ_GENERICS)   # set after construction, as build_levers does
    return _thrusting(c)


def test_stacked_edge_read_generics_are_floored_at_zero():
    """STACKING (a review finding, PC-17 close six): factors multiply, so two edge_read generics (refined L8 with
    practiced L1 is already past the jian's root at a total factor of 17.7; refined L8 with practiced L8, used here,
    is past the spear's and rapier's 20 as well) would drive legibility below 0, and read_contest multiplies the
    defender's read by it, so the defender's visual / precommit generics would then lower p_read as they rise.
    combat_systems.legibility is floored at 0: the stacked build sits ON the floor. That the defender's read levers
    then stay sign-safe follows from read_d being a product with a zero factor; a p_read monotonicity assertion here
    would be vacuous (every p_read equal), so it is not made."""
    checked = 0
    for weapon in THRUSTING_DOUBLE_EDGES:
        levels = [8.0 if n.endswith(('refined', 'practiced')) else 0.0 for n, _t in EDGE_READ_GENERICS]
        agg = _stacked(weapon, levels)
        # the premise this probe licenses: the stack really is past the root (otherwise the floor is never exercised)
        unfloored = (CFG['LEGIB_THRUST'] - CFG['LEGIB_DISTRACT_K'] * WP.distraction(agg.w)
                     - CFG['LEGIB_EDGELINE_K'] * WP.edge_lines(agg.w) * ABIL.ability_factor(agg, 'edge_read'))
        assert unfloored < 0.0, (weapon, unfloored)
        assert S.legibility(agg, 3.0, CFG) == 0.0, (weapon, S.legibility(agg, 3.0, CFG))
        checked += 1
    assert checked == len(THRUSTING_DOUBLE_EDGES) == 3, checked


def test_latin_square_placement_and_a_wrong_tradition_stays_inert():
    """Placement is asserted here, not only counted: each (lever, tier) pair exists in exactly one tradition and each
    tradition holds three generics on three DIFFERENT levers; and a fighter who knows a DIFFERENT real tradition than
    the generic's gets exactly the unequipped result (the gate admits the named tradition only, not 'any but none')."""
    pairs = {}
    per_tradition = {}
    for n, lever, t in GENERICS:
        tier = n.rsplit('_', 1)[1]
        assert (lever, tier) not in pairs, (n, pairs[(lever, tier)])
        pairs[(lever, tier)] = t
        per_tradition.setdefault(t, []).append(lever)
    assert len(pairs) == 21, len(pairs)
    assert len(per_tradition) == 7 and all(len(set(v)) == 3 == len(v) for v in per_tradition.values()), per_tradition
    checked = 0
    for n, lever, t in GENERICS:
        wrong = next(x for x in per_tradition if x != t)
        invested = Combatant('w', weapon='arming', tradition=wrong, equipped={n: 8.0})
        plain = Combatant('w', weapon='arming', tradition=wrong)
        assert ABIL.ability_factor(invested, lever) == ABIL.ability_factor(plain, lever) == 1.0, (n, wrong)
        checked += 1
    assert checked == 21, checked


def test_choke_control_generics_are_mitigators_and_the_rest_amplifiers():
    """Direction follows the site: choke_control's factor multiplies a term ADDED to the read the opponent takes."""
    checked = 0
    for n, lever, _t in GENERICS:
        v = ABIL.ABILITIES[n]['value']
        assert (v < 1.0) if lever == 'choke_control' else (v > 1.0), (n, v)
        checked += 1
    assert checked == 21


def test_the_read_is_perception_alone():
    """PC-18 (1), ED-IN-0347: `reading(c)` is `c.att` and nothing else. `cog` is gone from `Combatant`, so two defenders
    cannot differ in it (the constructor refuses the keyword, as does the attribute setter), and two defenders differing
    only in `att` read differently. Planted failure: the `cog` term back in `reading` reddens this (no `c.cog`)."""
    with pytest.raises(TypeError):
        Combatant('d', cog=5)
    with pytest.raises(TypeError):
        Combatant('d').set_attr('cog', 5)
    assert not hasattr(Combatant('d'), 'cog')
    checked = 0
    seen = []
    for att in (1, 2, 3, 4, 5):
        d = Combatant('d', att=att)
        assert S.reading(d, CFG) == att, att
        seen.append(S.reading(d, CFG))
        checked += 1
    assert len(set(seen)) == 5 and checked == 5     # differing only in att, they read differently
    assert S.reading(Combatant('d'), CFG) == 3      # the class default: the old (2*3+3)/3, so an unauthored realm is unmoved


def _read_a(aggressor, cfg, consistency_a=0.7):
    return S.read_contest(aggressor, Combatant('d', weapon='arming'), 3.0, consistency_a, 0.0, 0.0, cfg,
                          _FixedRng(0.5), TR)['read_a']


def test_the_attacks_suddenness_is_coordination():
    """PC-18 (2), ED-IN-0347: the aggressor's side of the read adds AGI_READ_K*(agi - NEUTRAL['agi']) to his reading
    value, inside the visual factor. Two aggressors differing only in agi are read differently at the shipped K and
    alike at K = 0; an aggressor at agi 4 reads exactly as the pre-item formula at every K, his visual lever invested
    or not; at the shipped K a Perception-1 / Coordination-1 aggressor's read value stays above 0, so the visual
    probes above stay live and sign-safe. Planted failure: the term dropped from read_contest makes the first equal."""
    k = CFG['AGI_READ_K']
    assert k > 0.0, k
    slow, quick = Combatant('a', agi=2), Combatant('a', agi=6)
    assert _read_a(quick, CFG) > _read_a(slow, CFG)
    assert _read_a(quick, CFG) - _read_a(slow, CFG) == pytest.approx(k * 4 * TR.eff_cw(quick, 'visual'), abs=1e-12)
    off = dict(CFG, AGI_READ_K=0.0)
    assert _read_a(quick, off) == _read_a(slow, off)
    checked = 0
    for kk in (0.0, 0.05, 0.1, 0.2, 0.3, 0.5, k):
        cfg = dict(CFG, AGI_READ_K=kk)
        for att in (1, 3, 5, 7):
            for lv in (0.0, 8.0):
                agg = Combatant('a', att=att, tradition='german',
                                equipped=({} if lv <= 0.0 else {'keen_eye_basic': lv}))
                assert agg.agi == S.NEUTRAL['agi']
                pre = S.reading(agg, cfg) * TR.eff_cw(agg, 'visual') + 0.7      # the formula before PC-18 (2)
                assert _read_a(agg, cfg) == pre, (kk, att, lv)
                checked += 1
    assert checked == 7 * 4 * 2
    floor = Combatant('a', att=1, agi=1)
    assert S.reading(floor, CFG) + k * (floor.agi - S.NEUTRAL['agi']) > 0.0
