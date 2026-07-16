#!/usr/bin/env python3
"""
ci_supersession_check.py
Ports valoria_hooks.supersession_check into a standalone CI validator.

WARN-ONLY churn / downstream-consequence guard. Reads registers/supersession_register.yaml
from the working tree and the current git changeset (via ci_common), then emits a
WARNING for every register entry whose 'files_to_recheck' list overlaps the changed
paths. A propagating change legitimately re-touches these files, so this NEVER blocks
the build — it always exits 0. The warning is a prompt to verify the change does not
regress whatever superseded authority the entry tracks.

Original lived at valoria_hooks.supersession_check(additions); it took an in-memory
`additions` list and read the register from the GitHub-ops session cache. This version
takes the changeset from git and reads the register from disk.
"""
import os
import sys

try:
    import ci_common
except ImportError:
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import ci_common

REGISTER_PATH = 'registers/supersession_register.yaml'


def find_matches(entries: list, changed_paths: set) -> list:
    """
    Pure core. Given the register's `entries` list and a set of changed repo-relative
    paths, return a list of match dicts (one per entry whose 'files_to_recheck' overlaps
    the changed set):

        {'id': <superseded_id or '?'>,
         'scope': <scope, truncated to 80 chars>,
         'replacement': <replacement, truncated to 120 chars>,
         'touched': <sorted list of overlapping paths>}

    No I/O. Mirrors the original supersession_check match structure exactly.
    """
    if not entries:
        return []

    matches = []
    for e in entries:
        if not isinstance(e, dict):
            continue
        recheck = e.get('files_to_recheck', []) or []
        if not isinstance(recheck, list):
            continue
        overlap = set(changed_paths) & set(recheck)
        if overlap:
            matches.append({
                'id': e.get('superseded_id', '?'),
                'scope': str(e.get('scope', ''))[:80],
                'replacement': str(e.get('replacement', ''))[:120],
                'touched': sorted(overlap),
            })
    return matches


def main(argv) -> int:
    """
    Load the register from disk, compute the changeset via ci_common, run find_matches,
    print advisories, and ALWAYS return 0 (WARN-ONLY).
    """
    mode = 'ci'
    if '--staged' in argv:
        mode = 'staged'
    elif '--local' in argv:
        mode = 'local'

    # Load the register from the working tree.
    content = ci_common.read_text(REGISTER_PATH)
    if content is None:
        print(f"[SUPERSESSION SKIP] {REGISTER_PATH} not present — skipping (non-blocking).")
        return 0

    try:
        import yaml
    except ImportError:
        print("[SUPERSESSION SKIP] PyYAML not available — skipping (non-blocking).")
        return 0

    try:
        data = yaml.safe_load(content) or {}
    except Exception as exc:
        print(f"[SUPERSESSION SKIP] {REGISTER_PATH} malformed ({exc}) — skipping (non-blocking).")
        return 0

    entries = data.get('entries', []) if isinstance(data, dict) else []
    if not entries:
        print(f"[SUPERSESSION INFO] no entries in {REGISTER_PATH} — nothing to check.")
        return 0

    changed = ci_common.get_changed_files(mode)
    if not changed:
        print("[SUPERSESSION INFO] no changed files detected — nothing to check.")
        return 0

    matches = find_matches(entries, changed)
    if not matches:
        print(f"[SUPERSESSION INFO] no supersession entries overlap the changeset "
              f"({len(changed)} changed file(s) checked against {len(entries)} entries).")
        return 0

    print(f"[SUPERSESSION WARN] {len(matches)} match(es) in {REGISTER_PATH} "
          f"(non-blocking — verify the change does not regress superseded authority):")
    for m in matches:
        print(f"[SUPERSESSION WARN]   - {m['id']}: {m['scope']}")
        print(f"[SUPERSESSION WARN]     Current canonical: {m['replacement']}")
        print(f"[SUPERSESSION WARN]     Touched in this change: {', '.join(m['touched'])}")
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
