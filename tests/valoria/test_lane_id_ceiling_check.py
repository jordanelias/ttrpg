"""The per-lane ID-ceiling check must be able to FIRE (ED-IN-0121).

`currency_consistency_check.check_lane_id_ceilings` guards ID allocation across nine concurrent
lanes — the exact hazard the `ED-<LANE>-NNNN` namespace was created for after two same-session
collisions (CLAUDE.md §3). It could never fire.

`_ledger_lane_max()` read only `registers/editorial_ledger.jsonl`. That file contains ZERO
lane-tagged ids: every `ED-<LANE>-NNNN` entry lives in `registers/editorial_ledger_<lane>.jsonl`
after the 2026-07-08 split. So it returned `{}`, the check hit `if not lane_max: return`, and
nothing was ever compared — while its docstring explained the no-op as "no lane-tagged IDs exist
yet". Measured at repair: 0 lanes checked before, 8 after, 0 new findings. It agreed by luck.

A blind check and a passing check look identical from outside. These tests make the difference
observable.
"""
import importlib.util
import os
import sys

import pytest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
TOOLS = os.path.join(ROOT, 'tools')


@pytest.fixture()
def ccc():
    if TOOLS not in sys.path:
        sys.path.insert(0, TOOLS)
    spec = importlib.util.spec_from_file_location(
        'currency_consistency_check', os.path.join(TOOLS, 'currency_consistency_check.py'))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_the_lane_reader_actually_finds_lanes(ccc):
    """THE REGRESSION. An empty dict here is not 'no drift', it is 'no check'."""
    lanes = ccc._ledger_lane_max()
    assert lanes, ('_ledger_lane_max() returned {} — check_lane_id_ceilings will no-op and the '
                   'per-lane ID ceiling is unguarded across all nine lanes')
    assert len(lanes) >= 7, f'only {len(lanes)} lane(s) seen: {sorted(lanes)}'
    assert all(code in ccc.LANE_CODES for code in lanes)


def test_the_reader_is_not_cwd_dependent(ccc, monkeypatch, tmp_path):
    """A relative glob would silently return {} — restoring the blindness — whenever the tool runs
    from anywhere but the repo root. Pre-existing precedent in this repo: two guards that passed
    only because of the directory they happened to be invoked from."""
    monkeypatch.chdir(tmp_path)
    assert ccc._ledger_lane_max(), 'the lane reader depends on the current working directory'


def test_drift_is_reported_when_next_free_is_behind(ccc, monkeypatch):
    """THE FALSIFIER the old implementation could not produce. Plant a lane whose ledger max has
    overrun next_free and assert the message fires."""
    monkeypatch.setattr(ccc, '_ledger_lane_max', lambda: {'MB': 9999})
    drift = []
    ccc.check_lane_id_ceilings(drift)
    assert any('next_free' in d and 'MB' in d for d in drift), drift


def test_no_drift_is_reported_on_the_live_tree(ccc):
    """Both directions: the repaired check must not invent findings. Measured 0 at repair."""
    drift = []
    ccc.check_lane_id_ceilings(drift)
    assert drift == [], f'unexpected lane-ceiling drift: {drift}'


def test_archived_allocations_still_count(ccc):
    """An archived ED consumed its id. Excluding archives would under-report the maximum and
    re-open the collision this check exists to prevent."""
    import glob as _g
    archives = _g.glob(os.path.join(ROOT, 'registers', 'editorial_ledger_*_archive.jsonl'))
    assert archives, 'no lane archives present — this test would be vacuous'
    assert ccc._ledger_lane_max().get('IN', 0) >= 58, \
        'IN maximum looks too low — archived allocations may have been dropped'
