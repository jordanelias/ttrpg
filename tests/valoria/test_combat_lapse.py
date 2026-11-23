"""PC-19, ED-IN-0347: Focus between the read and the response. `mode_sigma` adds `LAPSE_K * consistency(defender)` before
the mode's affinity cap. `consistency` is `FOCUS_CONSISTENCY_K*(conc/5 - 3)`: 0 at a full default reserve (3F+2S = 15),
negative once the reserve is drained, so the term lowers a DRAINED defender's response and leaves a fresh one's alone.

Falsifier (CLAUDE.md §0.1 pt 3), run at the build: the `sig += LAPSE_K*consistency(...)` line deleted from mode_sigma
reddens `test_a_drained_defender_chooses_the_same_mode_with_a_worse_sigma` and `test_the_shipped_lapse_separates_a_drained_defender`
(the sigmas come out equal); with it present and K = 0 the control tests stay green (`test_k_zero_is_the_pre_item_tree`, retired since)."""

import pytest


from modules.combat import combat_systems as S  # noqa: E402
from modules.combat import tradition as TR  # noqa: E402
from modules.combat.combatant import Combatant  # noqa: E402
from modules.combat.config import CFG  # noqa: E402

SCRATCH_K = 0.2


class _WinRng:
    """A read that is won (random() < p_read for any p_read > 0); the guess branch is never reached."""

    def random(self):
        return 0.0

    def below(self, n):
        raise AssertionError('a won read must not guess')


def _full(c):
    """A fight's start: the reserve at its maximum (wrapper._init_live; a fresh Combatant holds 0 until a fight starts)."""
    c.conc = c.conc_max
    return c


def _drained(c, hits=3):
    """The reserve after `hits` hits, by the wrapper's own drain (`conc = max(0, conc - CONC_DRAIN_HIT)`)."""
    _full(c)
    for _ in range(hits):
        c.conc = max(0, c.conc - CFG['CONC_DRAIN_HIT'])
    return c


def _pair(weapon='arming'):
    return _full(Combatant('fresh', weapon=weapon)), _drained(Combatant('drained', weapon=weapon))


def _choose(aggressor, defender, cfg):
    return S.read_contest(aggressor, defender, 3.0, 0.0, 0.0, 0.0, cfg, _WinRng(), TR)


def test_full_reserve_is_zero_and_a_drained_one_is_negative():
    fresh, drained = _pair()
    assert fresh.conc == fresh.conc_max == 15.0
    assert S.consistency(fresh, CFG) == 0.0
    assert S.consistency(drained, CFG) < 0.0
    assert drained.conc == 15.0 - 3 * CFG['CONC_DRAIN_HIT']


def test_a_drained_defender_chooses_the_same_mode_with_a_worse_sigma():
    cfg = dict(CFG, LAPSE_K=SCRATCH_K)
    checked = 0
    for weapon in ('arming', 'spear', 'rapier', 'longsword'):
        agg = Combatant('a', weapon='arming')
        fresh, drained = _pair(weapon)
        rf, rd = _choose(agg, fresh, cfg), _choose(agg, drained, cfg)
        assert rf['read_win'] and rd['read_win'] and rf['read_d'] == rd['read_d']      # the same read
        assert rf['mode'] == rd['mode'], weapon                                         # the same mode chosen
        m = rf['mode']
        assert rd['msig'][m] < rf['msig'][m], (weapon, m)                               # a worse response
        cap = S.WP.defense_affinities(fresh.w)[m]
        assert rf['msig'][m] - rd['msig'][m] == pytest.approx(
            -SCRATCH_K * S.consistency(drained, cfg) * cap, abs=1e-12)
        checked += 1
    assert checked == 4


def test_the_shipped_lapse_separates_a_drained_defender():
    """PC-19 (2): at the shipped K a defender drained by three hits and one at full reserve, the same read, choose the
    same mode and differ in its sigma by exactly -K*consistency*cap; at K = 0 they are equal."""
    k = CFG['LAPSE_K']
    assert k > 0.0, k
    checked = 0
    for weapon in ('arming', 'spear', 'rapier', 'longsword', 'mace'):
        agg = Combatant('a', weapon='arming')
        fresh, drained = _pair(weapon)
        rf, rd = _choose(agg, fresh, CFG), _choose(agg, drained, CFG)
        assert rf['mode'] == rd['mode'], weapon
        m = rf['mode']
        assert rd['msig'][m] < rf['msig'][m], (weapon, m)
        cap = S.WP.defense_affinities(fresh.w)[m]
        assert rf['msig'][m] - rd['msig'][m] == pytest.approx(-k * S.consistency(drained, CFG) * cap, abs=1e-12)
        off = dict(CFG, LAPSE_K=0.0)
        zf, zd = _choose(agg, fresh, off), _choose(agg, drained, off)
        assert zf['mode'] == zd['mode'] == m and zf['msig'][m] == zd['msig'][m], weapon
        checked += 1
    assert checked == 5


def test_the_lapse_falls_with_each_further_hit():
    """The drain is monotone in the response: each further hit lowers the chosen mode's sigma at the shipped K."""
    agg = Combatant('a', weapon='arming')
    seen = []
    for hits in range(0, 8):
        d = _drained(Combatant('d', weapon='arming'), hits)
        seen.append(_choose(agg, d, CFG)['msig']['parry'])
    assert seen[0] > seen[1] > seen[2] > seen[3] > seen[4] > seen[5] > seen[6] > seen[7]   # conc 15, 13, ... 1
    assert len(seen) == 8
