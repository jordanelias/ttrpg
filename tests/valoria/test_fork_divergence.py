#!/usr/bin/env python3
"""The anti-fabrication ratchet over the restructure-ledger consumers (ED-IN-0178).

The property, stated so it can fail — it is `tests/valoria/test_forked_status.py`'s property, one
layer out. That file proves `broken_dependency_checker` separates *a path that left deliberately*
(a `FORK:` row) from *a path that never existed* (no row), and calls the separation "the repo's
anti-fabrication property". It proves it for ONE consumer.

`audit/2026-08-13-fork-divergence-harness/fork_divergence.py` asked the same question of all SIX
consumers that parse the alias ledger, and the answer is worse than the alias plan's reading
suggested: the distinction survives in **5 of 18** (consumer x fork-row) pairs. Four consumers
collapse it on every row.

WHAT THIS TEST IS FOR, AND WHAT IT IS NOT. It is a RATCHET, not a conformance gate. Failing on
today's 13 collapsed pairs would fail on the state of the world the alias plan exists to fix, on
every unrelated PR, immediately — the "reds on day one" mistake ED-IN-0112 already paid for. So it
pins only the pairs that WORK, and fails when one stops working. Phase A2 makes it grow.

WHY PER-PAIR AND NOT PER-CONSUMER — a finding in its own right. `broken_dependency_checker`
returns INFO-EVACUATED for a 1-hop FORK row but BROKEN for a 2-hop chain, which is exactly what a
fabricated path returns. Its anti-fabrication property is CONDITIONAL ON HOP COUNT. A per-consumer
roster would have to record it as wholly safe or wholly broken, and both are false.
"""
from __future__ import annotations

import importlib.util
import os
import sys

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
HARNESS = os.path.join(ROOT, 'audit', '2026-08-13-fork-divergence-harness', 'fork_divergence.py')


def _load_fork_divergence_module():
    # Not `_load` — that bare name is already defined in 12 other test modules, each loading
    # something different (ED-IN-0181). A helper name that says nothing is a collision waiting
    # for the duplicate-helper gate to find it.
    spec = importlib.util.spec_from_file_location('fork_divergence', HARNESS)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


@pytest.fixture(scope='module')
def fd():
    if not os.path.exists(HARNESS):
        pytest.fail(f'the instrument is gone: {HARNESS}. A ratchet without its instrument is not '
                    f'a passing test, it is an absent one.')
    return _load_fork_divergence_module()


@pytest.fixture(scope='module')
def verdicts(fd):
    return fd.probe_all([q for q, _ in fd.PROBES])


def test_the_probe_reaches_every_consumer(verdicts, fd):
    """Assert that it asserted. An import failure inside probe_all must not read as agreement."""
    expected = {'pathres', 'broken_dependency_checker', 'ci_claude_workflow_paths',
                'vector_audit', 'workbench', 'gen_audit'}
    for q in verdicts:
        assert set(verdicts[q]) == expected, (
            f'probe for {q!r} covered {sorted(verdicts[q])}, expected {sorted(expected)} — a '
            f'consumer was renamed, moved, or silently failed to import.')


def test_the_control_is_dead_everywhere(verdicts, fd):
    """A path with NO ledger row must resolve nowhere. If this ever passes somewhere, the alias
    map has started inventing homes and the anti-fabrication property is gone outright."""
    live_shaped = {'LIVE', 'ALIASED', 'FORKED', 'INFO-EVACUATED', 'INFO-MAPPED', 'live', 'moved',
                   'remapped'}
    for consumer, verdict in verdicts[fd.CONTROL].items():
        assert verdict not in live_shaped, (
            f'{consumer} resolved the fabricated control path {fd.CONTROL!r} to {verdict!r}. '
            f'A path with no row must never resolve.')


def test_baseline_pairs_still_separate_evacuated_from_fabricated(verdicts, fd):
    """THE RATCHET. Losing a pair is an anti-fabrication regression, not a style drift."""
    keep = fd.distinguishing(verdicts)
    lost = fd.DISTINGUISHING_BASELINE - keep
    assert not lost, (
        f'{len(lost)} (consumer, path) pair(s) stopped distinguishing a FORKED path from a '
        f'fabricated one: {sorted(lost)}. Either a consumer lost its FORK handling, or a ledger '
        f'row it depended on changed shape.')


def test_the_ratchet_can_observe_a_loss(verdicts, fd):
    """Positive control: plant a regression and require the comparison to report exactly it."""
    victim = ('pathres', 'engine/params/core.md')
    assert victim in fd.DISTINGUISHING_BASELINE
    pretend = fd.distinguishing(verdicts) - {victim}
    assert fd.DISTINGUISHING_BASELINE - pretend == {victim}, (
        'the ratchet cannot see a planted regression — it would pass through a real one too.')


def test_the_baseline_is_not_vacuous(fd):
    """An empty or trivially-satisfied baseline would make the ratchet decorative."""
    assert len(fd.DISTINGUISHING_BASELINE) >= 5, (
        f'baseline holds only {len(fd.DISTINGUISHING_BASELINE)} pair(s); it was measured at 5. '
        f'Shrinking it is how a ratchet gets quietly disarmed — grow it in Phase A2 instead.')


def test_bdc_still_collapses_the_two_hop_chain_and_that_is_recorded_not_asserted(verdicts, fd):
    """The finding the plan's per-consumer framing could not express.

    This does NOT assert the collapse is acceptable — it asserts the baseline is HONEST about it.
    If someone fixes bdc's chained resolution, this test fails and points at the baseline line to
    update, which is the correct direction for a ratchet to break.
    """
    pair = ('broken_dependency_checker', 'params/core.md')
    assert pair not in fd.DISTINGUISHING_BASELINE, 'baseline claims a pair it did not measure'
    collapsed_now = pair not in fd.distinguishing(verdicts)
    assert collapsed_now, (
        "broken_dependency_checker now DISTINGUISHES the 2-hop chain params/core.md — that is a "
        "FIX, not a failure. Add the pair to DISTINGUISHING_BASELINE in fork_divergence.py in "
        "this same commit and delete this test's expectation.")
