"""PC-19, ED-IN-0347: Focus between the read and the response. `mode_sigma` adds `LAPSE_K * consistency(defender)` before
the mode's affinity cap. `consistency` is `FOCUS_CONSISTENCY_K*(conc/5 - 3)`: 0 at a full default reserve (3F+2S = 15),
negative once the reserve is drained, so the term lowers a DRAINED defender's response and leaves a fresh one's alone.

Falsifier (CLAUDE.md §0.1 pt 3), run at the build: the `sig += LAPSE_K*consistency(...)` line deleted from mode_sigma
reddens `test_a_drained_defender_chooses_the_same_mode_with_a_worse_sigma` and `test_the_shipped_lapse_separates_a_drained_defender`
(the sigmas come out equal); with it present and K = 0 the control tests stay green (`test_k_zero_is_the_pre_item_tree`)."""
import os
import sys

import pytest

ENGINE = os.path.join(os.path.dirname(__file__), '..', '..', 'modules', 'combat')
sys.path.insert(0, ENGINE)

import combat_systems as S  # noqa: E402
import tradition as TR  # noqa: E402
from combatant import Combatant  # noqa: E402
from config import CFG  # noqa: E402
import vocabulary as V  # noqa: E402

SCRATCH_K = 0.2


class _WinRng:
    """A read that is won (random() < p_read for any p_read > 0); the guess branch is never reached."""

    def random(self):
        return 0.0

    def randrange(self, n):
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


def test_k_zero_is_the_pre_item_tree():
    """K = 0 reproduces mode_sigma without the term, bitwise, for every mode and reserve."""
    off = dict(CFG, LAPSE_K=0.0)
    checked = 0
    for hits in (0, 1, 3, 7):
        agg, d = Combatant('a', weapon='arming'), _drained(Combatant('d', weapon='arming'), hits)
        for mode in V.DEFENCE_MODES:
            for win in (True, False):
                with_term = S.mode_sigma(mode, agg, d, 3.0, win, 0.0, off)
                fresh = _full(Combatant('d', weapon='arming'))                # same build, undrained
                assert with_term == S.mode_sigma(mode, agg, fresh, 3.0, win, 0.0, off), (hits, mode, win)
                checked += 1
    assert checked == 4 * 3 * 2


def test_at_full_reserve_the_term_is_zero_at_every_k():
    fresh = _full(Combatant('d', weapon='arming'))
    agg = Combatant('a', weapon='arming')
    checked = 0
    for k in (0.0, 0.05, 0.3, 1.0):
        cfg = dict(CFG, LAPSE_K=k)
        for mode in V.DEFENCE_MODES:
            assert S.mode_sigma(mode, agg, fresh, 3.0, True, 0.0, cfg) == \
                S.mode_sigma(mode, agg, fresh, 3.0, True, 0.0, dict(CFG, LAPSE_K=0.0)), (k, mode)
            checked += 1
    assert checked == 12
