"""Ledger-integrity guards added with ED-IN-0086.

Two separate things, both surfaced while widening the claim-provenance gate to the IN lane.

1. **The `confidence` vocabulary is closed for NEW entries.** ED-IN-0085 measured the field across
   1,075 entries and found `med` (27) and `medium` (11) coexisting as unvalidated spellings of one
   value, with nothing enforcing a set.

   ⚠️ **This corrects the proposal that led here.** ED-IN-0085's P6 said to "collapse `med` →
   `medium`". Measurement says don't: every `med` lives in `editorial_ledger.jsonl` (21) and
   `editorial_ledger_archive.jsonl` (6) — both **pre-cutover flat-ID registers**, which CLAUDE.md §3
   freezes ("no retrofit of pre-cutover entries") and which are append-only. Rewriting them to
   satisfy a linter is exactly the mass-edit-an-append-only-ledger move that
   `ci_claim_provenance_check.py` rejected when it chose an ID cutover over a date one. So the
   vocabulary is enforced going FORWARD, on the lane ledgers where new entries actually land, and
   history is left legible rather than laundered.

2. **The gate's cutover comparison must survive a lane with more than one id shape.** See
   `_is_pre_cutover` — the string comparison it replaced silently dragged every
   `ED-IN-REMEDIATION-NNNN` entry into scope.
"""
import glob
import importlib.util
import json
import os
import sys

import pytest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

# Closed set for NEW entries. `med` is deliberately absent: it is legal history, not a legal value.
ALLOWED_CONFIDENCE = {'high', 'medium', 'low'}

# Frozen pre-cutover registers (CLAUDE.md §3/§4). Grandfathered, never rewritten.
GRANDFATHERED = {
    'registers/editorial_ledger.jsonl',
    'registers/editorial_ledger_archive.jsonl',
}


def _lane_ledgers():
    out = []
    for full in sorted(glob.glob(os.path.join(ROOT, 'registers', 'editorial_ledger_*.jsonl'))):
        rel = os.path.relpath(full, ROOT).replace(os.sep, '/')
        if rel in GRANDFATHERED:
            continue
        out.append(rel)
    return out


def _entries(rel):
    with open(os.path.join(ROOT, rel), encoding='utf-8') as fh:
        for i, line in enumerate(fh, 1):
            line = line.strip()
            if not line:
                continue
            try:
                yield i, json.loads(line)
            except ValueError:
                pytest.fail(f"{rel}:{i} is not valid JSON — the ledger must stay machine-readable")


def test_there_are_lane_ledgers_to_check():
    """Guard the guard: if the glob stops matching, every assertion below passes vacuously."""
    assert _lane_ledgers(), "no lane ledgers found — this test would silently check nothing"


def test_new_entries_use_the_closed_confidence_vocabulary():
    bad = []
    for rel in _lane_ledgers():
        for lineno, entry in _entries(rel):
            conf = entry.get('confidence')
            if conf is not None and conf not in ALLOWED_CONFIDENCE:
                bad.append(f"{rel}:{lineno} id={entry.get('id')} confidence={conf!r}")
    assert not bad, (
        "lane-ledger entries use a confidence value outside "
        f"{sorted(ALLOWED_CONFIDENCE)}: {bad}. `med` is the historical drift ED-IN-0085 measured; "
        "write `medium`. Pre-cutover flat registers are grandfathered and not covered here.")


def test_grandfathered_registers_are_left_alone():
    """The frozen registers must keep their history — including the `med` spellings.

    This is the inverse assertion, and it is the point: if some future pass 'cleans up' the flat
    ledgers to make the vocabulary uniform, that is a retrofit of an append-only pre-cutover
    register and this test says so.
    """
    seen = 0
    for rel in sorted(GRANDFATHERED):
        full = os.path.join(ROOT, rel)
        if not os.path.exists(full):
            continue
        with open(full, encoding='utf-8') as fh:
            seen += sum(1 for line in fh if '"confidence": "med"' in line)
    assert seen > 0, (
        "no `med` confidence values remain in the frozen pre-cutover registers. If they were "
        "rewritten to `medium`, that retrofits an append-only register CLAUDE.md §3 freezes — "
        "revert it. If the registers were legitimately restructured, update GRANDFATHERED here.")


# --------------------------------------------------------------- claim-provenance cutover

def _gate():
    path = os.path.join(ROOT, 'tools', 'ci_claim_provenance_check.py')
    spec = importlib.util.spec_from_file_location('_cp_under_test', path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules['_cp_under_test'] = mod
    try:
        spec.loader.exec_module(mod)
    except SystemExit:
        pass
    return mod


@pytest.mark.parametrize('entry_id,cutover,expected,why', [
    ('ED-IN-0085', 'ED-IN-0086', True,  'earlier in the same lane is grandfathered'),
    ('ED-IN-0086', 'ED-IN-0086', False, 'the cutover entry is held to its own rule'),
    ('ED-IN-0087', 'ED-IN-0086', False, 'later in the same lane is in scope'),
    ('ED-IN-0100', 'ED-IN-0086', False, 'numeric, not lexical: 0100 > 0086'),
    ('ED-IN-REMEDIATION-0064', 'ED-IN-0086', True,
     "a different id scheme in the same file — the bug this replaced ('R' > '0')"),
    ('ED-PC-0041', 'ED-IN-0086', True,  'a different lane is not in this cutover sequence'),
    ('ED-PC-0040', 'ED-PC-0040', False, 'the PC precedent must not shift'),
    ('ED-PC-0039', 'ED-PC-0040', True,  'the PC precedent must not shift'),
])
def test_cutover_compares_lane_and_sequence_not_raw_string(entry_id, cutover, expected, why):
    assert _gate()._is_pre_cutover(entry_id, cutover) is expected, why
