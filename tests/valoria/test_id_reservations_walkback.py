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
    released = {'SC': 17, 'FA': 37, 'WR': 10, 'SE': 50}
    checked = 0
    for lane, expected in released.items():
        assert nf[lane] == expected, (
            f'{lane} next_free is {nf[lane]}, expected {expected} from the 2026-07-30 walk-back '
            f'(ED-IN-0098). If a later allocation legitimately advanced it, update this pin in '
            f'the same commit and say so.')
        checked += 1
    assert checked == len(released) == 4, f'expected 4 walked-back lanes, checked {checked}'


def test_in_lane_gap_is_documented_not_accidental():
    """IN's pointer is 9 past its max-allocated. That must be explained IN THE FILE, not just here."""
    nf, mx = _next_free(), _max_allocated()
    assert nf['IN'] - mx['IN'] > 1, 'IN no longer carries a gap — drop this test and the DELIBERATE_GAPS row'
    text = open(RESERVATIONS, encoding='utf-8', errors='replace').read()
    assert '0103-0111' in text, (
        "IN's next_free is deliberately ahead of max-allocated because CSO holds 0103-0111, but "
        "the file no longer says so — an undocumented gap is indistinguishable from an error.")
