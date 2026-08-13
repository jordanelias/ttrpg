#!/usr/bin/env python3
"""A document header may not cite an `ED-<LANE>-NNNN` that was never allocated (ED-IN-0174).

WHY THIS EXISTS. `audit/2026-08-12-alias-index-consolidation/00_plan.md` shipped with
`ED-IN-0173` in its header while `references/id_reservations.yaml` still read
`IN: next_free: 173`. The ID was cited but never allocated, so the register would have handed
0173 to the next unrelated allocation — the collision the `ED-<LANE>-NNNN` namespace exists to
make impossible by construction (CLAUDE.md §4). It was the second such slip in four commits.

WHY THE BLOCKING GATE DID NOT CATCH IT, stated precisely, because the obvious answer is wrong.
`tools/validate_ed_citations.py` is the anti-fabrication gate and it is BLOCKING. The natural
reading is that it excludes audits "by mandate" via `WORKING_PREFIXES` (:103) — audits PROPOSE
and TRACK EDs rather than assert canon, so they are deliberately out of its mandate. **That is
not what happened, and a fix aimed at it would have changed nothing.** `SCAN_PREFIXES` (:120) is
`('canon/', 'designs/', 'systems/', 'references/')`; live `audit/` is never SELECTED, so the
mandate exclusion never gets the chance to apply. Measured: the gate prints
`Scanning 285 doc(s)` and not one is under `audit/`.

WHY NOT JUST WIDEN `SCAN_PREFIXES`. Because the mandate is right on its merits. An audit citing
an *open* ED is normal and must not red a blocking gate; widening scope trades a blind spot for
a flood of false positives. This guard instead checks the one property that is ALWAYS wrong
regardless of status: citing a number nobody allocated. It is orthogonal to that gate, not a
widening of it.

WHY HEADERS AND NOT FULL TEXT — measured, not assumed. A full-text sweep of 1,143 files
reported five violations and **all five were artifacts**:

  · `registers/handoffs/HANDOFF_IN.md:667` reads "**ED-WR-0010 NOT allocated**" — the sweep
    flagged the very sentence documenting the non-allocation.
  · `tools/sim_harness/README.md:145` uses `ED-FA-9999` as a placeholder inside a code example.
  · three `tests/valoria/` files use `ED-IN-9999` / `ED-IN-0999` / `ED-GO-0001` as fixtures.

That is the corpus's own recurring lesson — co-occurrence of a token on a line is not an
assertion (the provenance-census "conflict" bucket, ED-IN-0135) — and no amount of sharpening
the heuristic fixes it. A `## Date:` header line, by contrast, is a STRUCTURED claim that this
document is filed under this ID. So the scope is deliberately narrow, and the narrowness is
evidenced rather than asserted.

THE FALSIFIER (CLAUDE.md §0.1 point 3). `test_the_checker_reproduces_the_ED_IN_0173_defect`
replays the exact pre-fix header against the exact pre-fix `next_free` and asserts it reds. A
guard that cannot observe the failure it excludes is absent, not weak (§0.1 point 2).
"""
from __future__ import annotations

import os
import re

import pytest
import yaml

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# The lane roster comes from the ALLOCATION AUTHORITY itself, not from a second copy. Any other
# source would be a roster that can drift from the register this check is about.
RESERVATIONS = os.path.join(REPO, 'references', 'id_reservations.yaml')

# Doc trees whose headers file work under an ED. `tests/` and `deprecated/` are excluded on
# purpose: fixtures and frozen history, per the measurement in the module docstring.
DOC_ROOTS = ('audit', 'proposals', 'workplans', 'godot', 'registers/handoffs',
             'canon', 'systems', 'references')

# HEADER_LINES was 8 and that MISSED THE PLAN OF RECORD (ED-IN-0177, adversarial review).
# `audit/2026-08-11-code-leanness/01_plan.md` carries its `## Date:` at line 37 — pushed down by an
# execution-state block — so the guard covered ZERO of that document's ID claims while appearing to
# cover the corpus. And the realistic recurrence is exactly that: a plan doc grows a preamble. The
# floors below could not notice, because they count docs that ARE in scope, never one that slid out.
#
# 60 is not a guess: measured over the corpus, the deepest live `## Date:` sits at line 37, so 60
# carries headroom for another preamble without reaching into body prose (the body-mention class the
# module docstring measures as 100% false-positive).
HEADER_LINES = 60
DATE_HEADER_RE = re.compile(r'^##\s*Date:.*$', re.M)
LANE_ID_RE = re.compile(r'\bED-([A-Z]{2})-(\d{3,4})\b')

# IDs inside a lane's DELIBERATE RESERVATION GAP are not allocated either (ED-IN-0177).
# `references/id_reservations.yaml:234` records that IN holds 0103–0111 for
# `audit/2026-07-29-centralization-single-owner/`. Those numbers are below `next_free`, so a bare
# `num >= next_free` test calls them allocated. The stated property is "citing a number nobody
# allocated", and a held-but-unissued number is exactly that. Parsed from the register rather than
# hardcoded, so walking the hold back does not silently strand this rule.
_GAP_RE = re.compile(r'CSO holds\s+(\d{3,4})-(\d{3,4})')

# Measured at write time: 67 header-bearing docs, 12 of them carrying an ED id. The floor guards
# against this test silently becoming vacuous if the header convention or DOC_ROOTS drift — a
# loop that asserts conditionally must assert that it asserted (CLAUDE.md §0.1 point 2).
MIN_HEADER_DOCS = 40
MIN_DOCS_WITH_IDS = 8


def lane_next_free() -> dict[str, int]:
    with open(RESERVATIONS, encoding='utf-8') as fh:
        data = yaml.safe_load(fh)
    return {lane: row['next_free'] for lane, row in data['lane_ids']['lanes'].items()}


def reserved_gaps() -> dict[str, set[int]]:
    """Lane -> ID numbers held but not issued. See _GAP_RE's note."""
    raw = open(RESERVATIONS, encoding='utf-8').read()
    gaps: dict[str, set[int]] = {}
    for line in raw.splitlines():
        m = _GAP_RE.search(line)
        if not m:
            continue
        lane_m = re.match(r'\s*([A-Z]{2}):', line)
        if lane_m:
            lo, hi = int(m.group(1)), int(m.group(2))
            gaps.setdefault(lane_m.group(1), set()).update(range(lo, hi + 1))
    return gaps


def header_ed_ids(text: str) -> list[tuple[str, int]]:
    """Lane ids claimed by a document's `## Date:` header line, if it has one."""
    head = ''.join(text.splitlines(keepends=True)[:HEADER_LINES])
    m = DATE_HEADER_RE.search(head)
    if not m:
        return []
    return [(lane, int(num)) for lane, num in LANE_ID_RE.findall(m.group(0))]


def check_header(text: str, next_free: dict[str, int], gaps: dict[str, set[int]] | None = None) -> list[str]:
    """Ids in this header that no lane has allocated. Empty list means clean."""
    gaps = gaps or {}
    bad = []
    for lane, num in header_ed_ids(text):
        if lane not in next_free:
            bad.append(f'ED-{lane}-{num:04d} names lane {lane!r}, absent from the lane roster')
        elif num >= next_free[lane]:
            bad.append(
                f'ED-{lane}-{num:04d} is NOT ALLOCATED — {lane} next_free is {next_free[lane]}. '
                f'Allocate it in references/id_reservations.yaml (read next_free, bump, write the '
                f'ledger row, co-commit) rather than citing max+1 (CLAUDE.md §4).')
        elif num in gaps.get(lane, ()):
            bad.append(
                f'ED-{lane}-{num:04d} sits in {lane}\'s RESERVED GAP — the number is held for '
                f'another owner and has not been issued. Below next_free is not the same as '
                f'allocated (ED-IN-0177).')
    return bad


def _iter_docs():
    for root_name in DOC_ROOTS:
        root_abs = os.path.join(REPO, root_name)
        if not os.path.isdir(root_abs):
            continue
        for dirpath, dirnames, filenames in os.walk(root_abs):
            dirnames[:] = [d for d in dirnames if d != '__pycache__']
            for fn in filenames:
                if not fn.endswith('.md'):
                    continue
                abspath = os.path.join(dirpath, fn)
                with open(abspath, encoding='utf-8', errors='replace') as fh:
                    yield os.path.relpath(abspath, REPO), fh.read()


def test_no_doc_header_cites_an_unallocated_ed():
    next_free = lane_next_free()
    gaps = reserved_gaps()
    header_docs = 0
    docs_with_ids = 0
    failures = []
    for rel, text in _iter_docs():
        ids = header_ed_ids(text)
        head = ''.join(text.splitlines(keepends=True)[:HEADER_LINES])
        if DATE_HEADER_RE.search(head):
            header_docs += 1
        if ids:
            docs_with_ids += 1
        for msg in check_header(text, next_free, gaps):
            failures.append(f'{rel}: {msg}')

    # Assert that it asserted.
    assert header_docs >= MIN_HEADER_DOCS, (
        f'only {header_docs} docs carry a `## Date:` header (expected >= {MIN_HEADER_DOCS}). '
        f'Either the header convention changed or DOC_ROOTS has gone stale — this check is '
        f'measuring almost nothing.')
    assert docs_with_ids >= MIN_DOCS_WITH_IDS, (
        f'only {docs_with_ids} headers carry an ED id (expected >= {MIN_DOCS_WITH_IDS}); '
        f'the id convention may have moved out of the header line.')

    assert not failures, (
        'document header(s) cite an ED id that was never allocated:\n  '
        + '\n  '.join(failures))


def test_the_checker_reproduces_the_ED_IN_0173_defect():
    """THE FALSIFIER. The exact pre-fix header against the exact pre-fix register state."""
    pre_fix_header = (
        '# Path-alias finding aid — consolidation plan\n'
        '\n'
        '## Status: PROPOSED — RATIFIES NOTHING. No parser moved, no row rewritten.\n'
        '## Date: 2026-08-12 · Lane: IN (cross-cutting) · ED-IN-0173\n'
    )
    pre_fix_next_free = {'IN': 173}
    bad = check_header(pre_fix_header, pre_fix_next_free)
    assert len(bad) == 1 and 'ED-IN-0173' in bad[0] and 'NOT ALLOCATED' in bad[0], (
        f'the guard cannot see the defect it was written for: {bad}')

    # …and it must go quiet once the ID is actually allocated. A one-sided control proves the
    # check fires, never that it fires SELECTIVELY (ED-IN-0139 F3).
    assert check_header(pre_fix_header, {'IN': 176}) == []


@pytest.mark.parametrize('header,expect_bad', [
    ('## Date: 2026-08-13 · Lane: MB · ED-MB-9999\n', True),      # far future
    ('## Date: 2026-08-13 · Lane: XX · ED-XX-0001\n', True),      # unknown lane
    ('## Date: 2026-08-13 · Lane: MB · ED-MB-0001\n', False),     # long allocated
    ('## Date: 2026-08-13 · no id here\n', False),                # header, no claim
    ('some prose mentioning ED-MB-9999 outside any header\n', False),  # not a claim
])
def test_positive_and_negative_controls(header, expect_bad):
    next_free = lane_next_free()
    assert bool(check_header(header, next_free)) is expect_bad


def test_body_mentions_are_deliberately_out_of_scope():
    """The measured false-positive class — see the module docstring. Not an oversight."""
    doc = (
        '## Date: 2026-08-13 · Lane: IN\n'
        '\n'
        'Later in the body: **ED-WR-0010 NOT allocated** — and `ED-FA-9999` as a placeholder.\n'
    )
    assert check_header(doc, lane_next_free()) == []


def test_the_reserved_gap_is_actually_parsed():
    """Assert that it asserted: if the gap parse silently returns nothing, the gap rule is off."""
    gaps = reserved_gaps()
    assert gaps.get('IN'), (
        'no reserved gap parsed for IN. references/id_reservations.yaml:234 records "CSO holds '
        '0103-0111"; if that wording changed, this rule went quiet without failing.')
    assert 105 in gaps['IN'] and 112 not in gaps['IN']


def test_a_gap_id_is_reported_even_though_it_is_below_next_free():
    """The blind spot ED-IN-0177 closed. ED-IN-0105 < next_free, and is still nobody's."""
    hdr = '## Date: 2026-08-13 · Lane: IN · ED-IN-0105\n'
    bad = check_header(hdr, lane_next_free(), reserved_gaps())
    assert len(bad) == 1 and 'RESERVED GAP' in bad[0], bad
    # …and the same id passes when the gap is not declared — the rule is the gap, not the number.
    assert check_header(hdr, lane_next_free(), {}) == []


def test_the_plan_of_record_is_actually_in_scope():
    """HEADER_LINES=8 covered ZERO of this document's id claims. Pin that it is now reachable."""
    rel = 'audit/2026-08-11-code-leanness/01_plan.md'
    text = open(os.path.join(REPO, rel), encoding='utf-8').read()
    head = ''.join(text.splitlines(keepends=True)[:HEADER_LINES])
    assert DATE_HEADER_RE.search(head), (
        f'{rel} has a `## Date:` header the guard cannot reach. HEADER_LINES={HEADER_LINES} is '
        f'too small again — the exact regression ED-IN-0177 fixed.')
