"""[ED-MB-0052 / plan v2 §5 C1] Every casualty is attributed to a source and a tick, and the parts sum to the whole.

Before this, the engine could not explain why a battle ended as it did. Every diagnosis in the last
two audits needed a bespoke probe and there are now 23 of them — that cost IS the finding. C1 makes
the two questions the lane keeps asking answerable without a new probe each time:

  * **the inverted causal shape** — the engine kills the loser and *then* breaks him, where history
    breaks him and then kills him. Answering that needs loss split by SOURCE, per tick;
  * **"this change is a no-op"** — A2's sigma snap, B1c's re-key. Aggregate hp is far too coarse to
    check that claim; per-source attribution is not.

CONSERVATION IS THE GATE. Attribution that does not sum to the measured hp delta is worse than none:
it reads as an explanation while being a fiction. So the load-bearing test is not "events were
emitted" but "Σ attributed == the hp that actually moved", asserted exactly, with a non-vacuity
counter so an empty battle cannot pass.

Two subtleties the assertions encode rather than assume:
  * loss is attributed from the CLAMPED movement (`before - after`), not the nominal damage. The two
    differ on the killing blow, and a conservation claim stated in nominal damage fails on every
    battle that ends in annihilation — which is most of them at this engine's casualty levels;
  * the split between melee and volley is proportional to their nominal share of that clamped total,
    so the parts sum to the whole even when the clamp bites.
"""
import os
import random
import sys

import pytest

_SIM = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'sim'))
if _SIM not in sys.path:
    sys.path.insert(0, _SIM)

import mass_battle.orchestration as O                                   # noqa: E402
from mass_battle.resolution import start_trace, get_trace               # noqa: E402
from mass_battle.engine import build_unit, run_battle                   # noqa: E402

_ANCHOR = 9


def _battle(seed, a_kw=None, b_kw=None):
    """One traced battle. Returns (events, {'A': measured_delta, 'B': measured_delta})."""
    random.seed(seed)
    ua = build_unit('Line', 3, 'A', 'A', _ANCHOR, **(a_kw or {}))
    ub = build_unit('Line', 3, 'B', 'B', _ANCHOR, **(b_kw or {}))
    a0, b0 = ua.hp, ub.hp
    start_trace(True)
    try:
        run_battle(ua, ub)
        events = [e for e in get_trace() if e.get('cat') == 'casualty']
    finally:
        start_trace(False)
    return events, {'A': a0 - ua.hp, 'B': b0 - ub.hp}


def _attributed(events):
    out = {}
    for e in events:
        out[e['unit']] = out.get(e['unit'], 0.0) + e['delta']
    return out


def test_attributed_losses_conserve_exactly_across_many_seeds():
    """THE GATE. Σ attributed == the hp that actually moved, per side, per battle.

    Exact equality, not `approx`: the attribution is computed from the same two floats the engine
    wrote, so any drift means a path is unattributed or double-counted — a real defect, not rounding.
    `pytest.approx` on an exactness claim is not a weak test, it is an absent one (§0.1 #2).
    """
    checked = 0
    for seed in range(20):
        events, measured = _battle(1000 + seed)
        attributed = _attributed(events)
        for side in ('A', 'B'):
            if measured[side] <= 0:
                continue
            checked += 1
            assert attributed.get(side, 0.0) == measured[side], (
                f"seed {seed} side {side}: attributed {attributed.get(side, 0.0)!r} != "
                f"measured {measured[side]!r} — a casualty path is untagged or double-counted")
    assert checked >= 20, (
        f"non-vacuity: only {checked} side-battles took any casualties; a conservation claim over "
        f"an empty set proves nothing")


def test_every_event_carries_source_and_tick():
    """Attribution without a tick cannot answer the causal-shape question it exists for."""
    events, _ = _battle(2024)
    assert events, "precondition: the battery matchup must produce casualties"
    for e in events:
        assert e['source'] in ('melee', 'volley', 'pursuit', 'freed_attacker'), e
        assert e['delta'] > 0, e
        if e['source'] in ('melee', 'volley'):
            assert isinstance(e['t'], int) and e['t'] >= 1, e


def test_volley_is_attributed_separately_from_melee():
    """Non-vacuity for the SPLIT, not just for the total.

    A conservation test alone passes happily if every loss is filed under one label. This asserts
    the ranged path produces its own `volley` rows, so the melee/volley separation — the thing that
    makes the causal-shape question answerable — is actually live and not a dead branch.
    """
    seen = set()
    volley_total = 0.0
    for seed in range(12):
        events, _ = _battle(3000 + seed,
                            a_kw={'unit_type': 'ranged'}, b_kw={'unit_type': 'melee'})
        for e in events:
            seen.add(e['source'])
            if e['source'] == 'volley':
                volley_total += e['delta']
    assert 'volley' in seen, f"ranged matchup produced no volley attribution; sources seen: {seen}"
    assert volley_total > 0.0


def test_attribution_is_inert_when_tracing_is_off():
    """The seam's own precondition: nothing is recorded, and nothing is computed, with tracing off.

    This is what lets the four goldens stay byte-exact. Verified here at the seam AND, in CI, by
    `bat.py --check` across all four modes.
    """
    random.seed(77)
    ua = build_unit('Line', 3, 'A', 'A', _ANCHOR)
    ub = build_unit('Line', 3, 'B', 'B', _ANCHOR)
    start_trace(False)
    run_battle(ua, ub)
    assert [e for e in get_trace() if e.get('cat') == 'casualty'] == []


def test_conservation_fails_when_one_path_is_untagged(monkeypatch):
    """MUTATION, in the suite rather than in a commit message.

    The plan's verifier gate is "conservation, mutation-verified by untagging one path". Rather than
    describe that, do it: silence `attribute_hp_loss` for the melee source and assert the
    conservation check then FAILS. Without this, a conservation test that only ever saw a correct
    engine could not distinguish "everything is attributed" from "the assertion never bites".
    """
    real = O.attribute_hp_loss

    def untagged_melee(unit, before, after, source, t=None, phase=None):
        if source == 'melee':
            return                      # the planted defect: one path stops reporting
        return real(unit, before, after, source, t=t, phase=phase)

    monkeypatch.setattr(O, 'attribute_hp_loss', untagged_melee)
    events, measured = _battle(1000)
    attributed = _attributed(events)
    assert any(measured[s] > 0 for s in ('A', 'B')), "precondition: casualties must occur"
    assert any(attributed.get(s, 0.0) != measured[s]
               for s in ('A', 'B') if measured[s] > 0), (
        "conservation still held with the melee path untagged — the check cannot observe the "
        "failure it exists to exclude")
