"""Coherence is a distance held as two quantities, elastic then plastic (position 27, WR-SCOPE).

WHY THIS EXISTS. `systems/threadwork/sim/coherence.py` implemented a 10 -> 0 depleting track until
2026-09-29, and NO test observed its behaviour — only a P-range citation string. The replacement
model's rulings (canon/philosophy/07_drift.md §7.1, §7.4; RULINGS.md Batch 8 E-1..E-4, Batch 9 C-1,
C-2) are each a claim a plausible-looking implementation could get wrong silently, so each gets a
test that runs the arithmetic and would fail under the rival reading:

  * per-event yield (stretch never stacking) fails `test_increments_accumulate_without_rest`;
  * a recovery that reaches the resting point fails `test_recovery_is_elastic_only`;
  * work hardening / brittleness fails `test_elastic_range_is_constant_after_set`;
  * creep, or a stack that never empties, fails `test_rest_between_workings_takes_no_set`;
  * a restore-to-human path past the crossing fails `test_crossing_is_reported_once_and_irreversible`.

The magnitudes in coherence.py are invented (its own header says so); what is NOT invented is the
set of orderings §7.1 fixes, and `test_canon_orderings_hold` pins those so a re-tune cannot break
them. The ED-WR-0008 Mending Stability scale term rides the same position and is tested at the end,
followed by the position's remainder: Mending's restorative feedback to the mender (C-1, §6.8), which
a Mending that stayed inert — the state until position 27's remainder — fails
`test_mending_calls_recover_and_its_term_is_positive`.
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


@pytest.fixture
def w():
    return _World()


def _stress(actor, k, w):
    return coh.apply_coherence_delta(actor, -k, f"stress {k}", world=w)


def _rest_fully(actor, w):
    return coh.recover(actor, seasons=10, environment_in_equilibrium=True, source="long rest", world=w)


def test_canon_orderings_hold():
    """§7.1's fixed orderings over the invented magnitudes."""
    # A novice at rest pushed to the end of their range reads Fractured; a veteran resting at
    # Dissonant pushed as far reads deeper (§7.1 "arrives deeper into Fractured").
    assert coh.RESTING_POINT_START + coh.ELASTIC_RANGE >= coh.DISPLACEMENT_FRACTURED_LOW
    # Someone can REST at Dissonant without having crossed.
    assert coh.DISPLACEMENT_DISSONANT_LOW <= coh.HUMAN_BAND_LIMIT
    # The human band has extent (derived "band, not point").
    assert coh.HUMAN_BAND_LIMIT > coh.RESTING_POINT_START
    assert (0 < coh.DISPLACEMENT_DISSONANT_LOW < coh.DISPLACEMENT_FRAGMENTED_LOW
            < coh.DISPLACEMENT_FRACTURED_LOW)


def test_below_range_is_elastic(w):
    s = _stress("a", coh.ELASTIC_RANGE, w)            # exactly the range: still elastic
    assert (s.resting_point, s.elastic_displacement) == (0, coh.ELASTIC_RANGE)
    s = _rest_fully("a", w)
    assert (s.resting_point, s.present_displacement) == (0, 0)


def test_excess_over_range_is_permanent_set_exactly(w):
    _stress("a", 4, w)
    s = _stress("a", 5, w)                              # stack 9 against a range of 6
    assert s.resting_point == 9 - coh.ELASTIC_RANGE
    assert s.elastic_displacement == coh.ELASTIC_RANGE
    assert s.log[-1].resting_after - s.log[-1].resting_before == 3


def test_increments_accumulate_without_rest(w):
    """C-2: "build up in increments". Small workings with no recuperation must eventually deform."""
    for _ in range(coh.ELASTIC_RANGE + 3):
        s = _stress("a", 1, w)
    assert s.resting_point == 3, "stretch did not stack across events — the per-event rival reading"


def test_rest_between_workings_takes_no_set(w):
    """E-4 / C-2 "answerable": recuperating between workings leaves nothing, however many there are."""
    for _ in range(50):
        _stress("a", coh.ELASTIC_RANGE - 1, w)
        s = _rest_fully("a", w)
    assert (s.resting_point, s.elastic_displacement) == (0, 0)
    assert len(s.log) == 100


def test_recovery_is_elastic_only(w):
    _stress("a", coh.ELASTIC_RANGE + 2, w)
    s = coh.recover("a", seasons=100, mending=100, environment_in_equilibrium=True,
                    source="everything", world=w)
    assert s.resting_point == 2
    assert s.present_displacement == s.resting_point, "recovery went past the resting point"


def test_environment_gates_recovery(w):
    _stress("a", 4, w)
    s = coh.recover("a", seasons=4, mending=3, environment_in_equilibrium=False,
                    source="beside a Gap", world=w)
    assert s.elastic_displacement == 4
    s = coh.recover("a", seasons=1 / 3, environment_in_equilibrium=True, source="a month", world=w)
    assert s.elastic_displacement == 4 - int(coh.ELASTIC_RETURN_PER_SEASON / 3)


def test_a_no_op_recover_logs_nothing(w):
    """A season tick that changes nothing must not grow `state.log` -- found missing by an
    adversarial /simplify pass: the guard's arithmetic was traced correct by hand, but nothing
    asserted the log stayed flat, which is exactly the claim ('an inactive practitioner would
    otherwise grow the log every season forever') the guard exists to make true. The guard itself
    later moved into `CoherenceState._log` (one owner for all three mutators, CLAUDE.md §8); this
    test still exercises it through `recover()`'s own contract."""
    _stress("a", 4, w)
    before = len(coh.get_state("a", w).log)
    # environment not in equilibrium: `offered` computes to nonzero but is gated to 0 -- no change.
    s = coh.recover("a", seasons=4, mending=3, environment_in_equilibrium=False,
                    source="beside a Gap", world=w)
    assert len(s.log) == before, "a gated (environment=False) recover still logged an entry"
    # environment in equilibrium but nothing left to recover: elastic_displacement is already 0.
    s = coh.recover("a", seasons=100, environment_in_equilibrium=True, source="fully rested", world=w)
    assert s.elastic_displacement == 0
    before2 = len(s.log)
    s = coh.recover("a", seasons=1, environment_in_equilibrium=True, source="already at rest", world=w)
    assert len(s.log) == before2, "a recover with nothing left to reduce still logged an entry"


def test_elastic_range_is_constant_after_set(w):
    """E-3: no work hardening, no brittleness. A veteran stretches exactly as far, from further out."""
    _stress("vet", coh.ELASTIC_RANGE + 2, w)
    _rest_fully("vet", w)
    s = _stress("vet", coh.ELASTIC_RANGE, w)
    assert s.resting_point == 2, "a full-range stretch took set after a prior set — range narrowed"
    s = _stress("vet", 1, w)
    assert s.resting_point == 3, "one past the range took no set — range widened"
    # Same load, veteran reads worse by exactly their set (§7.1).
    novice = _stress("nov", 4, w)
    _stress("vet2", coh.ELASTIC_RANGE + 2, w)
    _rest_fully("vet2", w)
    veteran = _stress("vet2", 4, w)
    assert veteran.present_displacement - novice.present_displacement == 2


def test_bands_read_present_except_failure(w):
    _stress("a", coh.ELASTIC_RANGE + coh.DISPLACEMENT_DISSONANT_LOW, w)
    s = coh.get_state("a", world=w)
    assert s.band == coh.BAND_FRACTURED and s.resting_band == coh.BAND_DISSONANT
    s = _rest_fully("a", w)
    assert s.band == coh.BAND_DISSONANT == s.resting_band      # "the band someone comes to rest in"
    _stress("b", coh.ELASTIC_RANGE + coh.HUMAN_BAND_LIMIT + 1, w)
    s = _rest_fully("b", w)
    assert s.elastic_displacement == 0 and s.band == coh.BAND_FAILURE


def test_crossing_is_reported_once_and_irreversible(w):
    s = _stress("a", coh.ELASTIC_RANGE + coh.HUMAN_BAND_LIMIT, w)
    assert not s.crossed
    r = coh.check_coherence_failure_transition("a", world=w)
    assert not r.failed and not r.just_transitioned
    _stress("a", 1, w)
    first = coh.check_coherence_failure_transition("a", world=w)
    second = coh.check_coherence_failure_transition("a", world=w)
    assert first.failed and first.just_transitioned
    assert second.failed and not second.just_transitioned
    _rest_fully("a", w)
    assert coh.get_state("a", world=w).crossed
    with pytest.raises(ValueError, match="manipulation"):
        coh.mend_resting_point("a", 5, "bring them back", world=w)


def test_mend_moves_resting_point_before_crossing(w):
    _stress("a", coh.ELASTIC_RANGE + 3, w)
    s = coh.mend_resting_point("a", 2, "self-mending", world=w)
    assert s.resting_point == 1 and s.elastic_displacement == coh.ELASTIC_RANGE
    s = coh.mend_resting_point("a", 99, "self-mending", world=w)
    assert s.resting_point == coh.RESTING_POINT_START


def test_a_no_op_mend_logs_nothing(w):
    """A Mending working that achieves nothing (amount=0, e.g. a Partial/Failure roll) must not
    grow `state.log` -- the same shared `CoherenceState._log` guard `recover()` exercises above,
    found missing here by /code-review on this position, then centralized into the one owner by
    an adversarial /simplify pass rather than duplicated a second time."""
    _stress("a", 3, w)
    before = len(coh.get_state("a", w).log)
    s = coh.mend_resting_point("a", 0, "a Failure roll achieved nothing", world=w)
    assert len(s.log) == before, "a no-op (amount=0) mend still logged an entry"
    assert s.resting_point == 0


def test_a_no_op_apply_coherence_delta_logs_nothing(w):
    """A zero-magnitude stress event (delta=0, legal per `apply_coherence_delta`'s own contract --
    'zero or NEGATIVE') must not grow `state.log` either -- the gap an adversarial /simplify pass
    found this mutator alone left open before the guard moved into the shared `_log` sink."""
    _stress("a", 3, w)
    before = len(coh.get_state("a", w).log)
    s = coh.apply_coherence_delta("a", 0, "a Success roll costs nothing", world=w)
    assert len(s.log) == before, "a no-op (delta=0) apply_coherence_delta still logged an entry"
    assert s.elastic_displacement == 3


def test_positive_delta_is_refused(w):
    with pytest.raises(ValueError, match="recover"):
        coh.apply_coherence_delta("a", 1, "old-style recovery", world=w)


def test_state_round_trips_and_retired_shape_is_refused(w):
    _stress("a", coh.ELASTIC_RANGE + 1, w)
    d = coh.get_state("a", world=w).to_dict()
    assert coh.CoherenceState.from_dict(d).to_dict() == d
    with pytest.raises(ValueError, match="retired"):
        coh.CoherenceState.from_dict({'actor': 'x', 'coherence': 7, 'band': 'Dissonant',
                                      'crisis_active': False, 'log': []})


# ─── ED-WR-0008: the P-25 scale term on Mending Stability ─────────────────────────────────────────

class _Practitioner:
    def __init__(self):
        self.actor_id, self.spirit, self.ts, self.history = "prac", 1, 30, 0


def _ms_by_degree(op, scale, seeds=400):
    # `op(...)` is called with no `world=`, so its Coherence write lands in the module-level
    # fallback store (`_store(None)`) under the shared actor id "prac" -- also used by
    # `engine/tests/test_thread_mending_ed871.py`. `mending_stability_delta` and `degree` don't
    # read accumulated Coherence state, so this has never affected an assertion, but nothing
    # should depend on run order to stay that way. Found by the Phase-3 terminal critique.
    coh.reset_all()
    seen = {}
    for seed in range(seeds):
        r = op(_Practitioner(), {"scale": scale}, rng=random.Random(seed))
        seen.setdefault(r.degree, set()).add(r.mending_stability_delta)
    return seen


@pytest.mark.parametrize("scale", list(ops.COHERENCE_COST_BY_SCALE))
def test_mending_stability_is_scale_keyed(scale):
    """P-25's override (ED-WR-0008): Partial = the scale's own Coherence cost, Failure =
    Partial - 1 -- a formula on `COHERENCE_COST_BY_SCALE`, not a second hand-kept table."""
    seen = _ms_by_degree(ops.attempt_weaving, scale)
    base = ops.COHERENCE_COST_BY_SCALE[scale]
    expected = {"Partial": base, "Failure": base - 1}
    checked = 0
    for degree in ("Partial", "Failure"):
        if degree in seen:
            assert seen[degree] == {expected[degree]}, (scale, degree, seen)
            checked += 1
    assert checked >= 1, f"no Partial/Failure rolled at {scale} — the assertion observed nothing"
    for degree in ("Success", "Overwhelming"):
        assert seen.get(degree, {0}) == {0}


def test_relational_tier_reproduces_the_retired_degree_table():
    """The override moves only the ends; at Relational it is the old -1/-2 exactly."""
    assert ops.COHERENCE_COST_BY_SCALE["Relational"] == -1  # Partial; Failure = Partial - 1 = -2
    assert (ops.COHERENCE_COST_BY_SCALE["Structural"] - 1) < (ops.COHERENCE_COST_BY_SCALE["Object"] - 1)


def test_binding_ops_keep_their_flat_cost():
    seen = _ms_by_degree(ops.attempt_locking, "Structural", seeds=60)
    assert set().union(*seen.values()) == {-1}


# ─── Position 27 remainder: Mending's restorative feedback (C-1; 06_operations.md §6.8) ──────────
# Read as: `attempt_mending` calls `recover()` and the restorative term > 0 (`coherence_delta` stays 0,
# ED-871) — the plan's wording is "cost > 0", and a literal cost contradicts ED-871's zero STRESS, so
# the term is what is asserted. The two rulings are asserted together.

DEGREES = ("Overwhelming", "Success", "Partial", "Failure")


def _spy_recover(monkeypatch):
    """Wrap the REAL `recover` that `operations` calls, recording each call's keywords. Wrapped,
    not replaced: the state assertions below then observe the owner's own arithmetic."""
    calls = []
    real = ops.recover

    def spy(*args, **kwargs):
        calls.append(kwargs)
        return real(*args, **kwargs)
    monkeypatch.setattr(ops, "recover", spy)
    return calls


def _mend_at(w, scale, degree, monkeypatch, *, env, pre_stress=coh.ELASTIC_RANGE):
    """One Mending by "prac", stretched by `pre_stress` first, with the degree FORCED — the rolled
    path is exercised separately below; this pins the per-degree contract at every scale."""
    monkeypatch.setattr(ops, "_compute_degree", lambda net, ob: degree)
    if pre_stress:
        _stress("prac", pre_stress, w)
    return ops.attempt_mending(_Practitioner(), {"scale": scale}, world=w, rng=random.Random(0),
                               environment_in_equilibrium=env)


@pytest.mark.parametrize("scale", list(ops.MENDING_OB))
@pytest.mark.parametrize("degree", DEGREES)
def test_mending_calls_recover_and_its_term_is_positive(scale, degree, monkeypatch):
    w = _World()
    calls = _spy_recover(monkeypatch)
    r = _mend_at(w, scale, degree, monkeypatch, env=True)
    s = coh.get_state("prac", world=w)
    assert r.coherence_delta == 0, "ED-871: Mending's STRESS is 0 at every degree"
    if degree == "Failure":
        assert calls == [] and r.coherence_restored == 0, (
            f"a FAILED Mending returned {r.coherence_restored} — it returned nothing to the "
            "attractor, so nothing is drawn along with it (§6.8)")
        assert s.elastic_displacement == coh.ELASTIC_RANGE
        return
    term = -ops.COHERENCE_COST_BY_SCALE[scale]
    assert len(calls) == 1, f"recover() called {len(calls)} times by a Mending that took"
    assert calls[0]["mending"] == term > 0, (scale, degree, calls[0])
    assert calls[0]["seasons"] == 0, "Mending is an event, not time: it must not pass seasons"
    assert r.coherence_restored == term == coh.ELASTIC_RANGE - s.elastic_displacement
    assert s.resting_point == coh.RESTING_POINT_START


def test_mending_feedback_is_gated_by_the_menders_environment(monkeypatch):
    """E-1's condition, owned by `recover`: Mending in disharmony still CALLS it (the gate stays
    one owner's) and returns nothing. Unstated is not established — the default is False."""
    w = _World()
    calls = _spy_recover(monkeypatch)
    monkeypatch.setattr(ops, "_compute_degree", lambda net, ob: "Success")
    _stress("prac", 4, w)
    log_before = len(coh.get_state("prac", world=w).log)
    r = ops.attempt_mending(_Practitioner(), {"scale": "Structural"}, world=w,
                            rng=random.Random(0))             # environment not stated
    assert len(calls) == 1 and calls[0]["environment_in_equilibrium"] is False
    assert calls[0]["mending"] > 0
    s = coh.get_state("prac", world=w)
    assert r.coherence_restored == 0 and s.elastic_displacement == 4
    assert len(s.log) == log_before, "a gated Mending feedback logged an event that moved nothing"


def test_mending_feedback_never_reaches_the_resting_point(monkeypatch):
    """C-1's feedback to a mender drawn along by ANOTHER's configuration is elastic only: a
    permanent set stays however many Mendings follow (moving it is `mend_resting_point`'s)."""
    w = _World()
    monkeypatch.setattr(ops, "_compute_degree", lambda net, ob: "Overwhelming")
    _stress("prac", coh.ELASTIC_RANGE + 2, w)
    for _ in range(coh.ELASTIC_RANGE + 2):
        ops.attempt_mending(_Practitioner(), {"scale": "Foundational"}, world=w,
                            rng=random.Random(0), environment_in_equilibrium=True)
    s = coh.get_state("prac", world=w)
    assert (s.resting_point, s.elastic_displacement) == (2, 0)


def test_an_unpriced_scale_falls_back_to_relational_for_ob_and_term_alike(monkeypatch):
    w = _World()
    calls = _spy_recover(monkeypatch)
    r = _mend_at(w, "Object", "Success", monkeypatch, env=True)
    assert r.ob == ops.MENDING_OB["Relational"]
    assert calls[0]["mending"] == -ops.COHERENCE_COST_BY_SCALE["Relational"]


def test_rolled_mending_executes_both_branches(monkeypatch):
    """The unforced path: real dice, so `_compute_degree` and `_resolve_operation` are the
    production ones. Asserts it asserted (CLAUDE.md §0.1 pt 2): both a Mending that took and one
    that failed must occur, or the per-branch checks observed nothing."""
    calls = _spy_recover(monkeypatch)
    took = failed = 0
    for seed in range(300):
        w = _World()
        _stress("prac", coh.ELASTIC_RANGE, w)
        n = len(calls)
        r = ops.attempt_mending(_Practitioner(), {"scale": "Relational"}, world=w,
                                rng=random.Random(seed), environment_in_equilibrium=True)
        assert r.coherence_delta == 0
        if r.degree == "Failure":
            failed += 1
            assert len(calls) == n and r.coherence_restored == 0
        else:
            took += 1
            assert len(calls) == n + 1 and r.coherence_restored == 1
    assert took >= 1 and failed >= 1, f"took={took} failed={failed}: a branch never executed"
