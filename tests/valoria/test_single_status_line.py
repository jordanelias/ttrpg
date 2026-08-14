#!/usr/bin/env python3
"""A design doc may not carry two `## Status:` lines in its head window (ED-IN-0184).

WHY THIS EXISTS, and why the failure is silent. The G8 consolidation made ONE owner for the
`## Status:` parse and it takes the **first match** in an 80-line head window. So a second Status
line is not a conflict the tooling resolves — it is a line the tooling **cannot see**. Whatever it
says is invisible to `CURRENT.md` reconciliation, the incompleteness census, and every currency
gate, while remaining perfectly visible to a human reading the file.

Found 2026-08-14 by a read-only contradiction hunt. Three of the five instances are genuine
contradictions, not duplications:

  · `systems/_architecture/derived_stats_v30.md:2,4` — `CANONICAL` and `PROPOSAL — supersedes
    prior derived_stats_v30.md`. One file, two statuses, the second self-referentially superseding
    the file it appears in. This doc is load-bearing: CURRENT.md names its §14.2 as the Truth-Track
    source of truth, and the combat wound constants resolve through its §4.1.
  · `systems/factions/faction_canon_v30.md:6,7` — `CANONICAL` and `PROVISIONAL — pending
    ratification`, where the PROVISIONAL line explicitly redirects per-faction texture authority
    back to four other documents. An ED-1094 ratify-on-merge flip that never happened; the loser is
    not a softer version of the winner, it points somewhere else entirely.
  · `systems/characters/character_generation_questionnaire_v30.md:2,4` — `CANONICAL` and
    `DESIGN DIRECTION (not yet authored — question set pending)`. Incompatible claims about whether
    canonical content exists at all.

The other two are duplications rather than conflicts (the hunt dissolved `scale_transitions_v30.md`
explicitly: its second line agrees in substance). They are pinned here anyway, because the
distinction between "duplicate" and "contradiction" is a judgment this test cannot make — what it
can do is stop the population growing while those five are dispositioned.

RATCHET, NOT CONFORMANCE GATE. Failing on the five known instances would red every unrelated PR for
a pre-existing condition — the mistake ED-IN-0112 already paid for. This pins the five and fails on
a sixth.
"""
from __future__ import annotations

import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Must match the single owner's window (G8). If that constant moves, this must move with it.
HEAD_LINES = 80
STATUS_RE = re.compile(r'^##\s*Status:', re.M)

# MEASURED 2026-08-14. Shrink this as each is dispositioned; never grow it to make a run pass.
KNOWN_MULTI_STATUS = {
    'systems/_architecture/derived_stats_v30.md',            # CONTRADICTION — CANONICAL vs self-superseding PROPOSAL
    'systems/factions/faction_canon_v30.md',                  # CONTRADICTION — CANONICAL vs PROVISIONAL (ED-1094 flip missed)
    'systems/characters/character_generation_questionnaire_v30.md',  # CONTRADICTION — CANONICAL vs "not yet authored"
    'systems/_architecture/scale_transitions_v30.md',          # duplication, dissolved on inspection
    'systems/_architecture/subsystem_flow_skeletons_v1.md',    # unassessed
}


def _multi_status_docs():
    found = {}
    root = os.path.join(ROOT, 'systems')
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d != '__pycache__']
        for fn in filenames:
            if not fn.endswith('.md'):
                continue
            abspath = os.path.join(dirpath, fn)
            with open(abspath, encoding='utf-8', errors='ignore') as fh:
                head = ''.join(fh.readlines()[:HEAD_LINES])
            n = len(STATUS_RE.findall(head))
            if n > 1:
                found[os.path.relpath(abspath, ROOT).replace(os.sep, '/')] = n
    return found


def test_the_scan_reaches_a_real_corpus():
    """Assert that it asserted — a walk finding nothing would make the ratchet vacuous."""
    count = sum(1 for _ in _iter_status_docs())
    assert count >= 100, (
        f'only {count} systems/ docs carry a `## Status:` head at all; the scan or the convention '
        f'broke, and the ratchet below is measuring nothing.')


def _iter_status_docs():
    root = os.path.join(ROOT, 'systems')
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d != '__pycache__']
        for fn in filenames:
            if not fn.endswith('.md'):
                continue
            p = os.path.join(dirpath, fn)
            with open(p, encoding='utf-8', errors='ignore') as fh:
                head = ''.join(fh.readlines()[:HEAD_LINES])
            if STATUS_RE.search(head):
                yield p


def test_no_new_doc_carries_two_status_lines():
    """THE RATCHET. A second Status line is invisible to the single owner, so it cannot be
    resolved by tooling — only by a human who happens to open the file."""
    found = set(_multi_status_docs())
    new = sorted(found - KNOWN_MULTI_STATUS)
    assert not new, (
        f'{len(new)} doc(s) gained a second `## Status:` line in the first {HEAD_LINES} lines:\n  '
        + '\n  '.join(new)
        + '\n\nThe single owner takes the FIRST match, so the second line is invisible to every '
          'currency gate while staying visible to readers. Delete one, or state plainly which is '
          'the head status and move the other out of the head window.')


def test_the_known_set_has_not_silently_shrunk_without_being_fixed():
    """If a pinned doc drops off the list it was fixed — good, and the pin must shrink with it,
    in the same commit, so the ratchet stays tight."""
    found = set(_multi_status_docs())
    fixed = sorted(KNOWN_MULTI_STATUS - found)
    assert not fixed, (
        f'{len(fixed)} pinned doc(s) no longer carry two Status lines: {fixed}. Remove them from '
        f'KNOWN_MULTI_STATUS in this same commit — a ratchet that is not tight measures nothing.')


def test_the_three_real_contradictions_are_still_the_named_ones():
    """Named explicitly so a future session does not have to re-derive which of the five matter.

    This is documentation with an assertion attached: if one of the three stops carrying two
    statuses, it was dispositioned and this test points at the record to update.
    """
    found = set(_multi_status_docs())
    for rel in ('systems/_architecture/derived_stats_v30.md',
                'systems/factions/faction_canon_v30.md',
                'systems/characters/character_generation_questionnaire_v30.md'):
        assert rel in found, (
            f'{rel} no longer carries two Status lines — if it was dispositioned, update '
            f'KNOWN_MULTI_STATUS and this test together and record the disposition.')
