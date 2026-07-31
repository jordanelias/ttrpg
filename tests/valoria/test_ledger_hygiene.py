"""Ledger-integrity guards added with ED-IN-0087.

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
    ('ED-IN-0085', 'ED-IN-0087', True,  'earlier in the same lane is grandfathered'),
    ('ED-IN-0087', 'ED-IN-0087', False, 'the cutover entry is held to its own rule'),
    ('ED-IN-0087', 'ED-IN-0087', False, 'later in the same lane is in scope'),
    ('ED-IN-0100', 'ED-IN-0087', False, 'numeric, not lexical: 0100 > 0086'),
    ('ED-IN-REMEDIATION-0064', 'ED-IN-0087', True,
     "a different id scheme in the same file — the bug this replaced ('R' > '0')"),
    ('ED-PC-0041', 'ED-IN-0087', True,  'a different lane is not in this cutover sequence'),
    ('ED-PC-0040', 'ED-PC-0040', False, 'the PC precedent must not shift'),
    ('ED-PC-0039', 'ED-PC-0040', True,  'the PC precedent must not shift'),
])
def test_cutover_compares_lane_and_sequence_not_raw_string(entry_id, cutover, expected, why):
    assert _gate()._is_pre_cutover(entry_id, cutover) is expected, why


# ------------------------------------------------------- MEASURED-BY marker parsing

@pytest.mark.parametrize('blob,expected,why', [
    ('MEASURED-BY: tools/x.py', 'tools/x.py', 'the plain form'),
    ('… re-run. MEASURED-BY: tools/x.py.', 'tools/x.py',
     'a marker ENDING A SENTENCE — the trailing period is prose, not part of the filename. This is '
     'the case that failed ED-IN-0087 with "tools/x.py. does not exist" while the file sat right there.'),
    ('MEASURED-BY: tools/x.py, and see also', 'tools/x.py', 'comma already excluded'),
    ('MEASURED-BY: tools/x.py::case_3', 'tools/x.py', 'the ::selector suffix is stripped for existence'),
    ('MEASURED-BY: tools/x.py::case_3.', 'tools/x.py', 'both at once'),
])
def test_measured_by_marker_survives_ordinary_prose_punctuation(blob, expected, why):
    gate = _gate()
    found = gate.MARKER.findall(blob)
    assert found, f'marker not matched at all: {blob!r}'
    target = found[0].rstrip(gate._TRAILING_PROSE).split('::')[0]
    assert target == expected, why


def test_a_genuinely_missing_instrument_is_still_caught():
    """The inverse. Stripping trailing punctuation must not soften the actual rule — a named
    instrument that does not exist is the whole point of the marker."""
    gate = _gate()
    target = gate.MARKER.findall('MEASURED-BY: tools/does_not_exist.py.')[0] \
        .rstrip(gate._TRAILING_PROSE).split('::')[0]
    assert target == 'tools/does_not_exist.py'
    assert not os.path.exists(os.path.join(ROOT, target)), \
        'fixture path unexpectedly exists — this test no longer proves anything'


# ---------------------------------------------------------------------------
# 3. An ED's rows must not be SPLIT between a live lane ledger and its archive.
#    (ED-IN-0112, 2026-07-31 — found by CI, not by reading.)
# ---------------------------------------------------------------------------

REGISTERS_DIR = os.path.join(ROOT, 'registers')

# Ids that legitimately appear in BOTH a live ledger and its archive. Currently EMPTY, and that
# is a result rather than an omission.
#
# ED-IN-0012/0013 were listed here for exactly one commit. They are the documented 2026-07-05
# DOUBLE-ALLOCATION (PR #83's SC-audit batch vs PR #81/#82's edge-playability items — two
# different items issued one id), and they were genuinely split across live/archive at the time.
# Resolving the origin/main merge by WHOLE-ID placement moved both of their rows into the
# archive together, which ended the split without touching history: no row was edited, deleted,
# or relabelled, so CLAUDE.md §3's no-retrofit rule is intact. The exemption then went stale and
# `test_the_split_grandfather_list_is_still_load_bearing` said so on the next run — which is the
# entire reason that second test exists.
#
# If this set ever grows again: a NEW overlap is the archive-split bug this guard exists for.
# Adding an entry to silence it converts the guard into a record of its own defeats. The correct
# response is to place the id's rows in one file, not to exempt it.
_PRECUTOVER_DUP = (
    'pre-cutover flat id, byte-identical row in BOTH files (same date, same status), so the '
    'effective status is unambiguous from either — a duplicated row, not a split status. '
    'CLAUDE.md §3 freezes pre-cutover entries ("no retrofit") and both files are append-only, '
    'so the correct action is to record it, not to edit history.'
)
SPLIT_GRANDFATHERED = {
    'ED-129': _PRECUTOVER_DUP,
    'ED-131': _PRECUTOVER_DUP,
    'ED-200': _PRECUTOVER_DUP,
    'ED-295': _PRECUTOVER_DUP,
}


def _lane_ledger_pairs():
    """(live, archive) paths for every ledger that has both.

    GLOB CORRECTED 2026-07-31 (ED-IN-0112, adversarial pass). The first version globbed
    `editorial_ledger_*.jsonl` — which REQUIRES the underscore and therefore never matched
    `registers/editorial_ledger.jsonl`, the flat pre-cutover ledger and the largest live one.
    Its archive matched the glob but was then discarded by the `_archive` skip, so the flat
    pair was checked by neither test. The guard reported green over four ids that are split
    across that pair today. A guard whose population excludes the biggest member is not a
    weaker guard, it is a different one.
    """
    pairs = []
    candidates = set(glob.glob(os.path.join(REGISTERS_DIR, 'editorial_ledger*.jsonl')))
    for live in sorted(candidates):
        if live.endswith('_archive.jsonl'):
            continue
        archive = live[:-len('.jsonl')] + '_archive.jsonl'
        if os.path.exists(archive):
            pairs.append((live, archive))
    return pairs


def _ids(path):
    out = set()
    for line in open(path, encoding='utf-8', errors='replace'):
        line = line.strip()
        if not line:
            continue
        try:
            entry = json.loads(line)
        except json.JSONDecodeError:
            continue
        if entry.get('id'):
            out.add(entry['id'])
    return out


def test_no_ed_has_rows_split_between_a_live_ledger_and_its_archive():
    """Archive whole IDs, never individual rows.

    THE INCIDENT (ED-IN-0112). The IN ledger crossed its 50k size cap, so an archive
    pass moved the six oldest TERMINAL ROWS out. ED-IN-0016 had two rows — `open`
    (2026-07-05) and `resolved` (2026-07-08). Only the resolved row moved. Because the
    ledger is APPEND-ONLY, an id's effective status is its LATEST row, so removing the
    resolved one silently reverted ED-IN-0016 to `open` in the live file. That turned
    `module_contracts.yaml`'s citation of it into "a canonical surface citing an open ED
    as basis", and ED-Citation-Integrity went red on CI.

    Nothing local caught it: the size check passed, and `validate_ed_citations` had been
    run BEFORE the archive move. The row-level operation looked correct in isolation and
    was wrong only in relation to rows it left behind — the same read/write-asymmetry
    shape as §0.1 #1.

    The guard is the invariant, not the incident: an id lives entirely in the live file
    or entirely in the archive. Splitting is always a bug, whatever the reason.
    """
    pairs = _lane_ledger_pairs()
    assert pairs, 'no live/archive lane-ledger pairs found — this guard would be vacuous'

    checked = 0
    for live, archive in pairs:
        overlap = (_ids(live) & _ids(archive)) - set(SPLIT_GRANDFATHERED)
        assert not overlap, (
            f'{os.path.basename(live)} and its archive both contain {sorted(overlap)}. '
            f"An ED's rows must move together: because the ledger is append-only, a split "
            f"leaves the id's effective status set by whichever rows stayed behind."
        )
        checked += 1
    assert checked == len(pairs), f'expected to check {len(pairs)} pairs, checked {checked}'


def test_the_split_grandfather_list_is_still_load_bearing():
    """Every grandfathered id must STILL be split, or the exemption is stale.

    Without this, the exemption set is write-only: an id that stopped overlapping would sit
    here forever, quietly widening the hole for a future genuine split of the same id.
    """
    live_arch = {}
    for live, archive in _lane_ledger_pairs():
        live_arch.setdefault('live', set()).update(_ids(live))
        live_arch.setdefault('arch', set()).update(_ids(archive))
    actually_split = live_arch.get('live', set()) & live_arch.get('arch', set())

    stale = set(SPLIT_GRANDFATHERED) - actually_split
    assert not stale, (
        f'{sorted(stale)} are grandfathered as split but are no longer split — remove them '
        f'from SPLIT_GRANDFATHERED so the guard covers them again.'
    )
    # An EMPTY set is the healthy state and must stay legal: the exemption exists to be spent.
    # (An earlier version asserted the set was non-empty, which would have made "we fixed the
    # last split" a test failure — a guard that punishes its own success.)
