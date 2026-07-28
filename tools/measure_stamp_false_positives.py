#!/usr/bin/env python3
"""Measure how often CURRENT.md's staleness stamp trips on apparatus alone (ED-IN-0089).

THE INSTRUMENT FOR A CLAIM, not a gate. `ci_claim_provenance_check.py` requires a ledger entry
that states measured numbers to name a script that reproduces them; this is that script for
ED-IN-0089's "12 of 51 stamp-tripping commits moved no canonical head".

WHY THE CLAIM NEEDED MEASURING AT ALL. The report that prompted the change said the stamp trips on
"essentially every infrastructure PR". That is the stronger claim, and it is not what the history
says — a quarter, not nearly all. Both numbers argue for the same narrowing, but shipping the
stronger one because it was handed to me is exactly the failure CLAUDE.md §0.1 point 4 describes:
a number with no control is not a measurement, in either direction, and a favourable framing is not
a reason to skip the check.

WHAT IT COUNTS. For each commit in the window, whether it touched a path CURRENT.md tracks, split by
whether that path is a canonical head (systems/, engine/, canon/, references/, params/, designs/,
sim/) or apparatus (tools/, tests/). A commit that touched apparatus and NO canonical head is a pure
false positive: it could not have staled a canon index, but it demanded a stamp bump anyway.

LIMIT, stated plainly: this counts what WOULD trip the check, from the file list alone. It does not
know whether the stamp was actually stale at that moment, so it measures the false-positive SURFACE
rather than observed failures. That is the honest ceiling of a retrospective sweep, and it is why
the number is reported as "would trip" throughout.

Usage:  python tools/measure_stamp_false_positives.py [--since 2026-06-28]
"""
import argparse
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))

import currency_consistency_check as C  # noqa: E402


def commits_since(since):
    out = subprocess.run(
        ['git', 'log', f'--since={since}', '--name-only', '--pretty=format:@@%H'],
        cwd=ROOT, capture_output=True, text=True, check=True).stdout
    commits, cur = [], None
    for line in out.splitlines():
        if line.startswith('@@'):
            cur = []
            commits.append(cur)
        elif line.strip() and cur is not None:
            cur.append(line.strip())
    return commits


def _hits(files, group):
    return any(f == t.rstrip('/') or f.startswith(t if t.endswith('/') else t + '/')
               for f in files for t in group)


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument('--since', default='2026-06-28',
                    help='git --since window (default: the 2026-06-28 CURRENT.md reconciliation)')
    a = ap.parse_args(argv)

    with open(os.path.join(ROOT, 'CURRENT.md'), encoding='utf-8') as fh:
        text = fh.read()
    tracked = C._current_md_paths(text)
    canon = set(C._canonical_head_paths(text))
    apparatus = set(tracked) - canon

    commits = commits_since(a.since)
    only_app = both = only_canon = 0
    for files in commits:
        ha, hc = _hits(files, apparatus), _hits(files, canon)
        only_app += ha and not hc
        both += ha and hc
        only_canon += hc and not ha
    tripping = only_app + both + only_canon

    print(f"window: commits since {a.since}")
    print(f"  CURRENT.md tracks {len(tracked)} path(s): {len(canon)} canonical-head, "
          f"{len(apparatus)} apparatus (tools/, tests/)")
    print(f"  commits in window:                                {len(commits)}")
    print(f"  would trip the stamp at all:                      {tripping}")
    print(f"    · via APPARATUS ONLY — no canonical head moved: {only_app}"
          + (f"  ({100 * only_app / tripping:.0f}% of trips)" if tripping else ""))
    print(f"    · via a canonical head as well:                 {both}")
    print(f"    · via a canonical head only:                    {only_canon}")
    print(f"  would not trip:                                   {len(commits) - tripping}")
    print("\n  The apparatus-only count is the false-positive surface ED-IN-0089 removes by scoping")
    print("  the STALENESS half to CANONICAL_HEAD_TREES. The existence half still covers every path.")
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
