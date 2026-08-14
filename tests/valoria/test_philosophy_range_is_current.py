#!/usr/bin/env python3
"""The stated philosophy range must match what canon actually defines (ED-IN-0184).

WHY THIS EXISTS, and it is the worst kind of defect: a SILENT one in the governing document.

`canon/02_canon_constraints.md` has defined **P-15** since 2026-04-02 — three-layer
being-persistence, the Leap vulnerability window, Coherence-0 TS branching — and it carries a real
FAIL test ("Does any mechanic allow Coherence 0 with no consequence, or allow a Leap without a
vulnerability window?"). `systems/threadwork/sim/coherence.py` implements it by name, and four
skills scope themselves to P-01–P-15.

CLAUDE.md said **P-01..P-14** in three places, including §9's routing row for `valoria-canon-guard`
— the skill whose entire job is philosophy compliance.

**The failure mode is silence.** A compliance pass scoped by §9 audits fourteen constraints,
never looks at P-15, and reports "all principles checked". Nothing errors. The certification is
simply wrong about the constraint governing Coherence 0 and Leap mechanics.

Found 2026-08-14 by a read-only contradiction hunt; CLAUDE.md §3 defers world/design truth to
`canon/`, so canon wins and the governing doc was stale by four months.
"""
from __future__ import annotations

import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CONSTRAINTS = os.path.join(ROOT, 'canon', '02_canon_constraints.md')
RANGE_RE = re.compile(r'P-01\s*(?:\.\.|–|-|through\s+)\s*P-(\d{2})')


def canon_max_p() -> int:
    """Highest P-NN with a row in the constraint table — the register of record."""
    text = open(CONSTRAINTS, encoding='utf-8').read()
    ids = [int(m) for m in re.findall(r'^\|\s*P-(\d{2})\s*\|', text, re.M)]
    assert ids, f'no P-NN rows parsed from {CONSTRAINTS} — the table format changed'
    return max(ids)


def test_canon_defines_at_least_fifteen():
    """Assert that it asserted: a parse returning a low number would make the check vacuous."""
    assert canon_max_p() >= 15, (
        f'canon/02_canon_constraints.md parses a max of P-{canon_max_p():02d}. P-15 has existed '
        f'since 2026-04-02; if the table shrank, that is a canon change needing its own record.')


def test_no_doc_understates_the_philosophy_range():
    """Any `P-01..P-NN` range string must not stop below what canon defines.

    Scans the surfaces a session actually reads to scope a compliance pass. Overstating is a
    different defect (a range naming a P that does not exist) and is caught by the same compare.
    """
    top = canon_max_p()
    # LIVE surfaces only. Ledgers and dated audit units are HISTORICAL RECORDS of what was
    # believed at the time — rewriting them would violate the same no-retrofit posture the
    # ED-<LANE>-NNNN cutover and the flat-ED freeze both take (CLAUDE.md §4). Measured
    # 2026-08-14: 13 understating occurrences existed, 9 on live surfaces (fixed) and 4 in
    # records (registers/editorial_ledger*.jsonl ×3, audit/2026-08-06-vector-audit/00_index.md).
    roots = ['CLAUDE.md', 'CURRENT.md', 'canon', 'skills', 'systems', 'references', 'tools',
             'engine', 'workplans', 'godot']
    bad = []
    for rel in roots:
        path = os.path.join(ROOT, rel)
        files = []
        if os.path.isfile(path):
            files = [path]
        else:
            for dirpath, dirnames, filenames in os.walk(path):
                dirnames[:] = [d for d in dirnames if d != '__pycache__']
                files += [os.path.join(dirpath, f) for f in filenames
                          if f.endswith(('.md', '.yaml', '.py'))]
        files = [f for f in files if '/audit/' not in f.replace(os.sep, '/')]
        for f in files:
            try:
                text = open(f, encoding='utf-8', errors='ignore').read()
            except OSError:
                continue
            for stated in RANGE_RE.findall(text):
                if int(stated) != top:
                    bad.append(f'{os.path.relpath(f, ROOT)}: says P-01..P-{stated}, canon defines P-01..P-{top:02d}')
    assert not bad, (
        f'{len(bad)} stated philosophy range(s) disagree with canon:\n  ' + '\n  '.join(sorted(bad))
        + '\n\nCanon is the register of record (CLAUDE.md §3 defers world/design truth to canon/). '
          'A range that stops short makes a compliance pass skip a constraint and still report '
          '"all principles checked" — the failure is silent.')
