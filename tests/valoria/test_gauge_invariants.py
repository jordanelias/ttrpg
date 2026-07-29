"""[ED-MB-0041] The two gauge invariants that need no band: side symmetry, and casualty realism.

The win-share gauge asks "how often does A beat B". It cannot tell a double envelopment from two lines
colliding, because both can produce the same number — which is how the reachability sweep found a
configuration that passes the Cannae row with envelopment pathing switched OFF. These two properties
close that gap from opposite directions:

  SIDE SYMMETRY — `decA(X vs Y) + decA(Y vs X) == 100`. Which army occupies the engine's "side A" slot
  is bookkeeping, not physics. No history, no band, no judgement call. A global constant enters both
  sides identically, so it moves the halves in opposite directions and leaves the sum pinned at 100:
  the sum is an invariant OF the constants, and a deviation localises a side-dependent mechanism.

  CASUALTY REALISM — what the battle cost, which is what the sources actually constrain. Bands are
  in-repo or logical consequences of in-repo values; see `gauge_mb.LOSER_CAS_BAND` for the provenance.

**Both are currently RED, and are marked xfail rather than skipped.** They describe properties the
engine does not yet have (measured: H3/H10 asymmetry +4.5 sigma, H4/H11 -5.3 sigma; mirror H1 kills
~85% of the loser and ~26% of the winner against a 15-30% / <15% expectation). xfail is the honest
encoding: the assertion runs every time, its failure is expected and does not redden CI, and it flips
to XPASS — which pytest reports loudly — the moment the mechanism is fixed. Skipping would let the
invariant rot; asserting would redden CI for a known-open design gap.

**These are TRACKING tests, not gates, and the sample size is why.** They run in the ordinary unit
suite, so n is far below the gauge's own 60. Reporting the symmetry deviation in sigma keeps low n from
manufacturing a false *positive* — the error bar widens with the noise — but it cannot buy statistical
POWER: a real defect can still go undetected because the point estimate wandered. Observed directly at
n=24: H3/H10, a +4.5 sigma defect at n=60, XPASSed. So an XPASS here is a prompt to re-measure, **not
evidence of a fix** — confirm with `reverse_pair_symmetry.py --n 60`, which is the authoritative run.
N is set to 40 below, enough to detect the two known defects most of the time without making the unit
suite unusable.

The casualty checks are not affected the same way: the current values miss their bands by 3-5x, which
no plausible sampling wobble closes.
"""
import os
import sys

import pytest

_SIM = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'sim'))
if _SIM not in sys.path:
    sys.path.insert(0, _SIM)
_AUDIT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..',
                                      'audit', '2026-07-22-mass-battle-stress-test'))
if _AUDIT not in sys.path:
    sys.path.insert(0, _AUDIT)

import gauge_mb as G
from reverse_pair_symmetry import symmetry, SIGMA_GATE

N = 40   # unit-suite budget; see the module docstring on the power limitation this carries


def _row(rid):
    for t in (G.TESTS + G.CAV_TESTS):
        if t[0] == rid:
            return t
    raise KeyError(rid)


# ─── side symmetry ───────────────────────────────────────────────────────────

@pytest.mark.xfail(reason="known-open: a side-dependent mechanism exists in the envelopment rows "
                          "(measured +4.5 sigma on H3/H10, -5.3 sigma on H4/H11 at n=60). H2/H9 is "
                          "NOT among them (+1.6 sigma — consistent with noise) and is parametrized "
                          "here as the negative control. XPASS is a prompt to re-measure at n=60, "
                          "not evidence of a fix.",
                   strict=False)
@pytest.mark.slow
@pytest.mark.parametrize('rid', ['H2', 'H3', 'H4'])
def test_reverse_pair_symmetry(rid):
    """Swapping which army is 'side A' must invert the result, not change it."""
    _tid, _label, sa, sb, ka, kb, *_ = _row(rid)
    s = symmetry(sa, sb, ka, kb, mode='multi', n=N)
    assert s['sigma'] is not None, (
        f"{rid}: no decisive results in one orientation — symmetry is undefined, which is a "
        f"broken instrument rather than a pass")
    assert abs(s['sigma']) < SIGMA_GATE, (
        f"{rid}: decA forward {s['fwd']:.1f} + reverse {s['rev']:.1f} = {s['total']:.1f}, "
        f"deviation {s['dev']:+.1f}pp = {s['sigma']:+.1f} sigma. The sum must be 100: which side "
        f"a body is deployed on is bookkeeping, not physics.")


def test_symmetry_is_measured_in_sigma_not_raw_points():
    """Guard the guard: the test above must stay noise-aware.

    A fixed percentage-point threshold would either flake at small n or miss a real defect at large n.
    The deviation is only meaningful relative to its own standard error, so `symmetry()` must keep
    returning one computed on the DECISIVE counts.
    """
    _tid, _label, sa, sb, ka, kb, *_ = _row('H1')
    s = symmetry(sa, sb, ka, kb, mode='multi', n=8)
    assert s['se'] is not None and s['se'] > 0, "standard error must be computed, not assumed"
    assert s['dec_fwd'] > 0 and s['dec_rev'] > 0
    # SE must shrink as evidence grows — otherwise it is not a real error bar.
    s_big = symmetry(sa, sb, ka, kb, mode='multi', n=32)
    assert s_big['se'] < s['se'], "standard error must fall with more decisive trials"


# ─── casualty realism ────────────────────────────────────────────────────────

@pytest.mark.xfail(reason="known-open: battles are far too lethal — the mirror kills ~85% of the "
                          "loser and ~26% of the winner against a 15-30% / <15% expectation. "
                          "XPASS here means the lethality model has been brought into band.",
                   strict=False)
@pytest.mark.parametrize('rid', ['H1', 'H2'])
def test_casualty_realism(rid):
    """The loser should break at its break-point, and the winner should not be gutted winning."""
    _tid, _label, sa, sb, ka, kb, *_ = _row(rid)
    r = G.matchup(sa, sb, ka, kb, 'multi', n=N)
    ok, flag, why = G.casualty_verdict(r)
    assert ok, f"{rid}: {flag} — {why} (winner {r['win_cas']}, loser {r['lose_cas']})"


def test_casualty_verdict_treats_an_absent_measurement_as_a_failure():
    """An unresolved row must never pass the cost checks by defaulting its casualties to zero.

    This is the R3 shape: 100% draws, so there is no winner and no loser. Reading that as "the winner
    lost 0%, which is below the cap" would turn the engine's most broken row into its cleanest pass.
    """
    unresolved = dict(win_cas=None, lose_cas=None, capped=100.0, t=20.0)
    ok, flag, _why = G.casualty_verdict(unresolved)
    assert not ok and flag == 'UNMEASURED'


def test_casualty_bands_are_self_consistent():
    """The winner cap is the contrapositive of the loser band's floor, so it must track it.

    If someone widens the rout band downward without moving the winner cap, the two stop describing
    the same underlying claim and the provenance note becomes false.
    """
    assert G.WINNER_CAS_MAX <= G.LOSER_CAS_BAND[0], (
        "the winner did not break, so its losses must sit below the break band's floor; "
        f"got winner-cap {G.WINNER_CAS_MAX} vs loser-floor {G.LOSER_CAS_BAND[0]}")
