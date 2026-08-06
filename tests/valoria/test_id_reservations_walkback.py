"""Walk-back safety guard for references/id_reservations.yaml (ED-IN-0098).

WHY THIS EXISTS. The W5 capstone's job is to "release unused reserved IDs with a documented
walk-back" — i.e. to LOWER `next_free` back onto the highest id a lane actually consumed. That
operation is only safe if the new `next_free` is strictly greater than every id already in that
lane's ledger. Lower it one step too far and the next session re-issues a LIVE id, which is the
same-lane collision class the `ED-<LANE>-NNNN` namespace was created to eliminate (see this
file's own history: 0074/0075/0083/0086/0087 each renumbered at merge).

The walk-back was done by hand on 2026-07-30 across four lanes. A hand-computed pointer is
exactly the kind of claim §0.1 #3 says must ship with its falsifier, so: this is the falsifier.

It also pins the ONE deliberate exception. IN's `next_free` is 112 while its highest allocated id
is 103, leaving 0098-0102 unreleased. That is not sloppiness — the 0092-0111 block is
sub-partitioned with `audit/2026-07-29-centralization-single-owner/` holding 0103-0111, and a
single integer pointer cannot represent a hole. The test asserts the SAFE direction only
(`next_free > max_allocated`), so a deliberately-conservative pointer passes and only an
UNSAFE one fails — the asymmetry is the point.
"""
import glob
import json
import os
import re

import pytest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
RESERVATIONS = os.path.join(ROOT, 'references', 'id_reservations.yaml')

LANES = ('MB', 'PC', 'FI', 'SC', 'FA', 'WR', 'IN', 'GO', 'SE')

# Lanes whose pointer is intentionally ahead of max-allocated, with the reason. A lane listed
# here still gets the safety assertion; this only documents why the gap is not reclaimable.
DELIBERATE_GAPS = {
    'IN': 'block 0092-0111 is sub-partitioned; CSO holds 0103-0111 (its §0.1 row 6), so '
          '0098-0102 cannot be reached by a single next_free pointer without handing out a '
          'live reservation. Reclaim when CSO completes.',
}


def _next_free():
    """Parse `LANE: { name: ..., next_free: N }` without a YAML dependency."""
    out = {}
    with open(RESERVATIONS, encoding='utf-8', errors='replace') as f:
        for line in f:
            m = re.match(r'\s{4}([A-Z]{2}): \{ name: "[^"]*",\s*next_free: (\d+)\s*\}', line)
            if m and m.group(1) in LANES:
                out[m.group(1)] = int(m.group(2))
    return out


def _max_allocated():
    """Highest ED-<LANE>-NNNN actually present, across live AND archive lane ledgers.

    Archives count: an archived id is still permanently valid for citation, so re-issuing it
    would be just as much a collision as re-issuing a live one.
    """
    out = {lane: 0 for lane in LANES}
    for path in glob.glob(os.path.join(ROOT, 'registers', 'editorial_ledger_*.jsonl')):
        for line in open(path, encoding='utf-8', errors='replace'):
            line = line.strip()
            if not line:
                continue
            try:
                entry = json.loads(line)
            except json.JSONDecodeError:
                continue
            m = re.match(r'ED-([A-Z]{2})-(\d+)$', str(entry.get('id', '')))
            if m and m.group(1) in out:
                out[m.group(1)] = max(out[m.group(1)], int(m.group(2)))
    return out


def _allocated_ids(lane):
    """Every ED number actually present for `lane`, live AND archive.

    Same sources and same archive rationale as `_max_allocated`; this returns the whole
    set rather than its maximum, so a hole in the middle of a lane's range is visible.
    """
    found = set()
    for path in glob.glob(os.path.join(ROOT, 'registers', 'editorial_ledger_*.jsonl')):
        for line in open(path, encoding='utf-8', errors='replace'):
            line = line.strip()
            if not line:
                continue
            try:
                entry = json.loads(line)
            except json.JSONDecodeError:
                continue
            m = re.match(r'ED-([A-Z]{2})-(\d+)$', str(entry.get('id', '')))
            if m and m.group(1) == lane:
                found.add(int(m.group(2)))
    return found


def test_reservations_file_is_parseable_and_covers_every_lane():
    nf = _next_free()
    missing = [lane for lane in LANES if lane not in nf]
    assert not missing, f'lane(s) absent from id_reservations.yaml next_free table: {missing}'


@pytest.mark.parametrize('lane', LANES)
def test_next_free_never_re_issues_a_live_id(lane):
    """The walk-back invariant: next_free must be strictly past every allocated id."""
    nf, mx = _next_free(), _max_allocated()
    assert nf[lane] > mx[lane], (
        f'ED-{lane}-{nf[lane]:04d} would be issued next, but ED-{lane}-{mx[lane]:04d} already '
        f'exists in a lane ledger — next_free was walked back too far and the next allocation '
        f'is a collision. Set next_free to at least {mx[lane] + 1}.'
        + (f' (Deliberate gap on record: {DELIBERATE_GAPS[lane]})' if lane in DELIBERATE_GAPS else ''))


def test_the_2026_07_30_walkback_actually_moved_something():
    """Counted assertion (§0.1 #2): a release that released nothing is a no-op mislabelled as work.

    Pins the four lanes whose blocks were walked back, so a silent revert to the frozen
    pointers is caught rather than passing as 'nothing to do'.
    """
    nf = _next_free()
    # PIN UPDATED 2026-08-06: SC 17 -> 23. ED-SC-0017..0022 were legitimately allocated by the
    # three-lens social-contest audit (audit/2026-08-06-social-contest-three-lens-audit/), and all
    # six entries exist in registers/editorial_ledger_sc.jsonl. This is the update-the-pin-and-say-so
    # path the assertion message below prescribes, not a revert of the walk-back: the frozen
    # pre-walk-back SC pointer was 21, so 23 cannot be reached by reverting ED-IN-0098.
    released = {'SC': 23, 'FA': 37, 'WR': 10, 'SE': 50}
    checked = 0
    for lane, expected in released.items():
        assert nf[lane] == expected, (
            f'{lane} next_free is {nf[lane]}, expected {expected} from the 2026-07-30 walk-back '
            f'(ED-IN-0098). If a later allocation legitimately advanced it, update this pin in '
            f'the same commit and say so.')
        checked += 1
    assert checked == len(released) == 4, f'expected 4 walked-back lanes, checked {checked}'


def _unallocated_below_next_free(lane):
    """Ids strictly below `next_free` that no ledger entry claims — the real hole.

    MEASURE CORRECTED 2026-07-31 (ED-IN-0112). The original form asserted
    `next_free - max_allocated > 1`, which is only equivalent to "a hole exists" while
    every allocation sits BELOW the held block. The allocation protocol requires the
    opposite — read `next_free`, allocate THERE, bump — so the first legitimate IN
    allocation after this guard landed (ED-IN-0112 at 112, bumping to 113) drove
    `next_free - max_allocated` to 1 and tripped the guard, while the hole it exists to
    document (0098-0102 unreleased, 0103-0111 held by CSO) was entirely untouched.

    A guard that fails on the operation it was written to protect is measuring the wrong
    quantity. Counting unallocated ids below the pointer is invariant to allocations at
    the top, so it tracks the hole itself rather than a proxy that the protocol destroys.
    """
    nf = _next_free()[lane]
    allocated = _allocated_ids(lane)
    if not allocated:
        return []
    return [n for n in range(min(allocated), nf) if n not in allocated]


def test_in_lane_gap_is_documented_not_accidental():
    """IN carries unallocated ids below its pointer. That must be explained IN THE FILE."""
    hole = _unallocated_below_next_free('IN')
    assert hole, ('IN no longer carries a hole below next_free — every id is allocated, so the '
                  'deliberate-gap exception is spent. Drop this test and the DELIBERATE_GAPS row.')
    text = open(RESERVATIONS, encoding='utf-8', errors='replace').read()
    assert '0103-0111' in text, (
        "IN's next_free is deliberately ahead of its unallocated ids because CSO holds 0103-0111, "
        "but the file no longer says so — an undocumented gap is indistinguishable from an error.")


# ── State/history separation (ED-MB-0063 follow-on, 2026-08-01) ───────────────

HISTORY = os.path.join(ROOT, 'references', 'id_reservations_history.md')

# A lane row plus a one-line summary and pointer fits comfortably; the narratives that were
# moved out ran 2,461-10,734 chars. 600 is well clear of legitimate rows (longest today: 1,579,
# in the header prose, which is why the cap below applies to LANE ROWS, not every line) and far
# under anything that counts as a migrated narrative.
MAX_LANE_ROW_CHARS = 600


def test_narrative_does_not_creep_back_into_the_state_file():
    """id_reservations.yaml is STATE. Long-form history belongs in the companion.

    THE PATTERN THIS GUARDS (§0.1 #5 — a pattern fix without a guard is not understood).
    This file is read on EVERY ED allocation by EVERY lane, and it is size-capped by a BLOCKING
    CI gate. It had accreted ~9,000 tokens of trailing `#` narrative and reached 14,263 of its
    15,000-token cap — about two allocations from failing the whole repo's allocation path.
    Nothing reported it until the approaching-cap WARN was added, because the cap check was
    binary OK/FAIL.

    Unbounded append-only history inside a hot, capped, machine-read state file WILL hit the cap
    again; the only question is when. So the fix is not "we trimmed it once", it is this: a lane
    row may carry a short summary and a pointer, and nothing more.

    Scoped to LANE ROWS (`XX: { ... }`) rather than every line on purpose — the file header
    legitimately carries multi-line prose about the allocation protocol, and a blanket
    line-length cap would either fail on that or be set so high it never fires.
    """
    offenders = []
    for i, line in enumerate(open(RESERVATIONS, encoding='utf-8', errors='replace'), 1):
        line = line.rstrip('\n')
        if not re.match(r'\s*[A-Z]{1,2}:\s*\{', line):
            continue
        if len(line) > MAX_LANE_ROW_CHARS:
            offenders.append((i, len(line), line[:90]))
    assert not offenders, (
        'lane row(s) in id_reservations.yaml exceed '
        f'{MAX_LANE_ROW_CHARS} chars — narrative is creeping back into the state file:\n' +
        '\n'.join(f'  line {i}: {n} chars — {t}...' for i, n, t in offenders) +
        '\n\nPut the narrative in references/id_reservations_history.md (or the lane ledger) and '
        'leave a one-line summary plus a pointer.')


def test_the_history_companion_exists_and_is_referenced():
    """The pointer must resolve, or the split silently becomes a deletion.

    Both directions are asserted deliberately. A test that only checked the companion EXISTS
    would pass just as happily if the YAML stopped pointing at it, which is how a moved
    narrative becomes unreachable history nobody knows to look for.
    """
    assert os.path.exists(HISTORY), (
        'references/id_reservations_history.md is missing — the YAML points at it for every '
        'lane narrative, so deleting it destroys provenance that exists nowhere else '
        '(checked: the ED-IN-0064 ledger entry is about a DIFFERENT item).')
    yaml_text = open(RESERVATIONS, encoding='utf-8', errors='replace').read()
    assert 'id_reservations_history.md' in yaml_text, (
        'id_reservations.yaml no longer points at its history companion — a reader hitting a '
        'one-line summary has no way to find the detail it summarises.')
