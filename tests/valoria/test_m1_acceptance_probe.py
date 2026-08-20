"""Behaviour pins for the S2 acceptance-oracle probe rows (return_to_game_queue.yaml S2,
ED-IN-0112, tools/m1_acceptance.py).

WHAT THESE TESTS ARE FOR. Before S2, `row_stub_invocations` and `row_determinism` were
unconditionally `blocked` — the module docstring said the "headless season run" that would
unblock them "does not exist". S2 pointed both rows at `engine.mc_v18.run_campaign`, which
already existed. These tests pin that the two rows are now genuinely `measured` (not merely
returning a plausible-looking dict), and that the measurement is REPRODUCIBLE under the tool's
own fixed probe seed — CLAUDE.md §0.1 point 4 ("a number without a control is not a
measurement"): the control here is running the SAME seed twice and requiring the SAME answer,
which is exactly what `row_determinism` itself measures and what
`test_stub_invocations_reproducible_under_the_fixed_probe_seed` below re-checks independently
for the other row.

Deliberately NOT pinned: the literal stub-call count. `row_stub_invocations()['value'] == 2`
is true today and would be a maintenance tax that teaches nothing if the season path's stub
sites change count (see engine/mc_v18.py's OI-05/OI-07 stub_resolve calls). What must never
change is that the row is MEASURED (not blocked) and that repeated probes under the same seed
AGREE — the relation, not the number (mirrors test_scope_ratchet.py's stated policy).
"""
import os
import sys

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
TOOLS = os.path.join(REPO_ROOT, 'tools')
sys.path.insert(0, TOOLS)
sys.path.insert(0, REPO_ROOT)

import m1_acceptance as m1  # noqa: E402


def test_engine_probe_import_succeeded():
    """Falsifier for every test below: if engine.mc_v18 failed to import, both rows would
    silently read as `blocked` again (a real green from a real run vs. a defensive fallback
    are otherwise indistinguishable from the outside) -- this asserts the live path was taken."""
    assert m1._mc_v18 is not None, (
        f'engine.mc_v18 import failed: {m1._ENGINE_IMPORT_ERROR!r} -- rows 1-2 fell back to '
        f'blocked; the tests below would be validating the fallback, not the S2 measurement'
    )


def test_stub_invocations_row_is_measured_not_blocked():
    row = m1.row_stub_invocations()
    assert row['state'] == 'measured', row
    assert row['unblocked_by'] is None
    assert isinstance(row['value'], int)
    assert row['value'] >= 0
    # `passes` must be DERIVED from `value`, not an independent guess.
    assert row['passes'] == (row['value'] == 0)


def test_determinism_row_is_measured_and_passes():
    row = m1.row_determinism()
    assert row['state'] == 'measured', row
    assert row['unblocked_by'] is None
    # The whole point of the row: identical seed -> identical KeyLog.content_hash().
    assert row['passes'] is True, row['detail']
    # Falsifier for a vacuous pass (both sides empty would satisfy h1 == h2 too):
    assert row['value'] != '(empty)', row['detail']
    assert '<empty>' not in row['detail'], row['detail']


def test_stub_invocations_reproducible_under_the_fixed_probe_seed():
    """Same fixed seed, measured twice, independently -> same stub-call count. This is
    row_stub_invocations' OWN control: if two probes under the tool's fixed M1_PROBE_SEED
    disagreed, the row would not be a measurement at all (CLAUDE.md §0.1 point 4)."""
    a = m1.row_stub_invocations()
    b = m1.row_stub_invocations()
    assert a['value'] == b['value']
    assert a['passes'] == b['passes']


def test_probe_season_hash_matches_across_independent_helper_calls():
    """Exercises _run_probe_season directly (row_determinism already does this internally;
    this pins the primitive it composes on, per CLAUDE.md §8 -- compose on one owner, and
    test that owner directly rather than only through one caller)."""
    r1 = m1._run_probe_season(m1.M1_PROBE_SEED)
    r2 = m1._run_probe_season(m1.M1_PROBE_SEED)
    assert r1.key_log_hash == r2.key_log_hash
    assert r1.key_log_hash != ''
    assert r1.stub_hits == r2.stub_hits


def test_a_different_seed_can_diverge_from_the_probe_seed():
    """Falsifier for 'the hash is a constant string regardless of input' -- content_hash()
    must actually be sensitive to the campaign, not a fixed value the row would trivially
    match against itself no matter what ran."""
    fixed = m1._run_probe_season(m1.M1_PROBE_SEED)
    other = m1._run_probe_season(m1.M1_PROBE_SEED + 1)
    # Not asserting inequality unconditionally would be too strong a claim to make blind, but
    # BOTH producing the exact same hash as the fixed-seed probe while differing by only the
    # seed would mean content_hash() is not keyed on campaign content -- assert that did NOT
    # happen, which is the property this row's whole design depends on.
    assert (fixed.key_log_hash, fixed.stub_hits) != (other.key_log_hash, other.stub_hits) or \
        fixed.keys_emitted == 0, (
        'seed 20260819 and 20260820 produced identical (hash, stub_hits) -- either both '
        'campaigns are no-ops (keys_emitted == 0, checked above) or content_hash() is not '
        'actually sensitive to what the campaign did, which would make row_determinism vacuous'
    )


def test_collect_reports_at_least_four_of_five_rows_measured_or_partial():
    """The step's own gate (return_to_game_queue.yaml S2 `observable`)."""
    result = m1.collect()
    non_blocked = [r['row'] for r in result['rows'] if r['state'] in ('measured', 'partial')]
    assert len(non_blocked) >= 4, (non_blocked, [r['row'] for r in result['rows']])


def test_check_exit_code_tracks_a_real_measured_failure():
    """--check's exit code must be DERIVED from collect()['failed'], never a constant --
    the S2 gate's 'exit code is now meaningful' claim, checked directly against main()."""
    result = m1.collect()
    rc = m1.main(['--check'])
    assert rc == (1 if result['failed'] else 0), (rc, result['failed'])
