"""R-14's practitioner-side term on a working's Coherence cost (WR-01).

canon/philosophy/06_operations.md (ruled 2026-09-09): "What determines their ability to prevent that
cost is how resilient their spirit is." The arithmetic is unruled, so it ships as a swept fixture
(`operations.RESILIENCE_GAIN`, arms `operations.RESILIENCE_GAIN_SWEEP`) whose shipped arm 0 is the
control — today's behaviour. The identity at gain 0 is observed by
engine/tests/test_thread_mending_ed871.py (Weaving's applied Coherence, CI job sim-regression) and by the
base digests in tests/valoria/test_threadwork_mending_parity.py (every op_type, collective and opposing);
test_coherence_elastic_plastic.py asserts no non-Mending cost, so it is not that control.

Falsifier: with the application line in `_resolve_operation` disabled,
`test_a_resilient_practitioner_takes_strictly_less_on_one_planted_pair` fails at every gain > 0.
"""
import os
import random
import sys

import pytest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from systems.threadwork.sim import coherence as coh  # noqa: E402
from systems.threadwork.sim import operations as ops  # noqa: E402


class _World:
    """The one field coherence reads off a World."""
    def __init__(self):
        self.practitioners = {}


class _Practitioner:
    """Same stats as the control file's stub; `resilience` is the only thing a pair varies."""
    def __init__(self, actor_id, resilience=None):
        self.actor_id, self.spirit, self.ts, self.history = actor_id, 1, 30, 0
        if resilience is not None:
            self.resilience = resilience


_SEED = 0
_WORKING = {"scale": "Structural"}   # the costliest priced scale: -2 before the degree penalty


def _displacement_taken(actor_id, w):
    """Total distance moved from the equilibrium: permanent set plus elastic stretch."""
    state = coh.get_state(actor_id, world=w)
    if state is None:
        return 0
    return (state.resting_point - coh.RESTING_POINT_START) + state.elastic_displacement


def _run_pair(resilience):
    """One planted pair: same stats, same seed, same working; only `resilience` differs."""
    w = _World()
    plain = ops.attempt_weaving(_Practitioner("plain"), _WORKING, world=w, rng=random.Random(_SEED))
    steady = ops.attempt_weaving(_Practitioner("steady", resilience), _WORKING, world=w,
                                 rng=random.Random(_SEED))
    assert plain.degree == steady.degree and plain.net_successes == steady.net_successes, \
        "resilience must not touch the roll — the pair is not planted"
    assert plain.coherence_delta < 0, "the planted working must cost something, or nothing is tested"
    return plain, steady, _displacement_taken("plain", w), _displacement_taken("steady", w)


def test_the_shipped_gain_is_the_control_arm():
    assert ops.RESILIENCE_GAIN == 0
    assert ops.RESILIENCE_GAIN_SWEEP[0] == ops.RESILIENCE_GAIN


def test_at_the_shipped_gain_resilience_changes_nothing():
    plain, steady, d_plain, d_steady = _run_pair(resilience=5)
    assert steady.coherence_delta == plain.coherence_delta
    assert d_steady == d_plain == -plain.coherence_delta


@pytest.mark.parametrize("gain", ops.RESILIENCE_GAIN_SWEEP)
def test_a_resilient_practitioner_takes_strictly_less_on_one_planted_pair(gain, monkeypatch):
    monkeypatch.setattr(ops, "RESILIENCE_GAIN", gain)
    plain, steady, d_plain, d_steady = _run_pair(resilience=1)
    if gain == 0:
        assert d_steady == d_plain
        assert steady.coherence_delta == plain.coherence_delta
    else:
        assert d_steady < d_plain
        assert steady.coherence_delta > plain.coherence_delta
        assert steady.coherence_delta == min(0, plain.coherence_delta + gain * 1)
    # The reported delta is the one applied.
    assert d_plain == -plain.coherence_delta and d_steady == -steady.coherence_delta


@pytest.mark.parametrize("gain", ops.RESILIENCE_GAIN_SWEEP)
@pytest.mark.parametrize("attempt", [ops.attempt_weaving, ops.attempt_pulling, ops.attempt_locking,
                                     ops.attempt_dissolution, ops.attempt_past_pulling])
def test_a_huge_resilience_floors_at_zero_and_never_raises(attempt, gain, monkeypatch):
    """The floor: resistance brings a cost toward 0 and stops; it is never a positive delta
    (which apply_coherence_delta would refuse) and never a negative displacement."""
    monkeypatch.setattr(ops, "RESILIENCE_GAIN", gain)
    for seed in range(20):
        w = _World()
        r = attempt(_Practitioner("titan", 10 ** 6), _WORKING, world=w, rng=random.Random(seed))
        assert r.coherence_delta <= 0
        assert _displacement_taken("titan", w) == -r.coherence_delta >= 0
        if gain > 0:
            assert r.coherence_delta == 0


def test_the_owner_leaves_zero_cost_alone_and_refuses_negative_resilience(monkeypatch):
    monkeypatch.setattr(ops, "RESILIENCE_GAIN", 3)
    assert ops.resist_coherence_cost(0, _Practitioner("m", 4)) == 0       # Mending (ED-871), Leap
    assert ops.resist_coherence_cost(-3, _Practitioner("a")) == -3        # absent attribute = 0
    assert ops.resist_coherence_cost(-7, _Practitioner("b", 2)) == -1
    for bad in (-1, 1.5, True, None):
        with pytest.raises(ValueError):
            ops.resist_coherence_cost(-1, _Practitioner("bad", bad) if bad is not None else _NoneResilience())


class _NoneResilience(_Practitioner):
    def __init__(self):
        super().__init__("none")
        self.resilience = None


@pytest.mark.parametrize("odd", [None, -1, 1.5, True, float("inf"), float("nan")])
def test_at_the_shipped_gain_the_owner_is_the_identity_whatever_resilience_holds(odd):
    """The control must hold for every actor, not only well-formed ones: at gain 0 the owner returns the
    cost before it reads the attribute, so an odd value neither raises nor leaks a float."""
    assert ops.RESILIENCE_GAIN == 0
    actor = _Practitioner("odd")
    actor.resilience = odd
    for cost in (0, -1, -2, -5):
        got = ops.resist_coherence_cost(cost, actor)
        assert got == cost and type(got) is int


def test_mending_is_unaffected_by_resilience(monkeypatch):
    """ED-871: Mending costs 0 at every degree; resistance has nothing to resist. The mender is
    pre-stressed and the environment stated, so the restorative path actually runs (a fresh mender
    with nothing to return would make the comparison 0 == 0)."""
    outcomes = {}
    for gain in (0, 3):
        monkeypatch.setattr(ops, "RESILIENCE_GAIN", gain)
        w = _World()
        coh.apply_coherence_delta("mender", -coh.ELASTIC_RANGE, "pre-stress", world=w)
        r = ops.attempt_mending(_Practitioner("mender", 5), {"scale": "Field"}, world=w,
                                rng=random.Random(_SEED), environment_in_equilibrium=True)
        outcomes[gain] = (r.degree, r.coherence_delta, r.coherence_restored,
                          _displacement_taken("mender", w))
    assert outcomes[0] == outcomes[3]
    assert outcomes[0][1] == 0
    assert outcomes[0][2] > 0, f"the restorative term never ran: {outcomes[0]}"
