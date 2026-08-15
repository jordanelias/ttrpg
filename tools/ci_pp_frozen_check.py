#!/usr/bin/env python3
"""PP is FROZEN HISTORICAL VOCABULARY — this gate is what makes that true rather than stated.

JORDAN RULING, 2026-08-14 (ED-IN-0185 Q4, executed as ED-IN-0190): of the PP-NNN patch numbers
cited across the live tree, all but six point at registers that left `main` in the 2026-08-05
evacuation. Blanket-mark them historical, resolving at the fork, and have the checker verify
only the format — not resolution.

WHAT "VERIFY ONLY THE FORMAT" HAD TO BECOME, AND WHY IT IS NOT WHAT IT SOUNDS LIKE.
Read literally, a format check over `PP-\\d+` matches for the pattern `PP-\\d+` and can never
fail. That is a vacuous gate, and this repo has paid for those twice already (ED-IN-0177's
allowlist that passed because its corpus emptied; ED-IN-0182's generator that ran and discarded
its output). So the ruling's INTENT — PP is frozen vocabulary, and its provenance resolves at a
named ref — is discharged as two things that can actually fail:

  R1  Every archive pointer in the active register's header names a fork ref. Four of the six
      pointed at `deprecated/archives/patches/*` paths that DO NOT EXIST on `main`; a reader
      following one got nothing and no explanation. Delete a `FORK:` annotation and this fails.

  R2  No PP id above the frozen ceiling appears anywhere live. Frozen means frozen: allocate
      PP-727 and this fails. The ceiling is the max id actually cited (726), not the header's
      aspirational "Next PP number: 727" — a next-free pointer is a plan, and freezing must bind
      what the tree really contains.

THE PATTERN CARRIES A LEFT BOUNDARY, and that is load-bearing rather than tidiness. `ci_common`'s
`PP_ID_PAT` is bare `PP-\\d+`, which is safe at its two call sites ONLY because both anchor it in
YAML (`-\\s+id:\\s+` + pattern). Used for a corpus scan it matches inside `OPP-03`: measured
2026-08-14, the bare pattern reported 48 malformed PP tokens, 34 of which were substrings of
`EVT-OPP-0N` in one proposals document. A gate built on the owner's pattern would have opened
with 34 fabricated findings. The owner is not changed here — its call sites are correct and
migrating them is not this ruling's business — but the difference is recorded at both ends.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ci_common  # noqa: E402

# The repo root has ONE owner (plan G7, ED-IN-0159 §8.1). Deriving it locally is the exact
# single-ownership violation this gate's own subject is about, and the guard caught it here.
REPO_ROOT = ci_common.REPO

REGISTER = 'registers/patch_register_active.yaml'
FORK_REF = 'c451bcb'

# Frozen ceiling: the highest PP id cited anywhere live as of the 2026-08-14 ruling.
# Raising this is not a maintenance action — it un-freezes a frozen vocabulary and needs its
# own ED plus a Jordan ruling, the same posture as the flat ED-NNNN freeze (CLAUDE.md §4).
PP_FROZEN_CEILING = 726

# Left boundary excludes OPP-/APP-/etc.; right boundary stops PP-72 matching inside PP-726.
PP_CITATION_RE = re.compile(r'(?<![A-Za-z0-9])PP-(\d+)\b')

SCAN_ROOTS = ('canon/', 'systems/', 'references/', 'registers/', 'workplans/',
              'godot/', 'engine/', 'proposals/', 'tools/')
SCAN_EXTS = ('.md', '.yaml', '.jsonl', '.py', '.json')

ARCHIVE_POINTER_RE = re.compile(r'(deprecated/archives/patches/[A-Za-z0-9_.]+\.yaml)')


# THE INSTRUMENT MUST NOT COUNT ITSELF. On its first run this gate reported a violation against
# its own docstring, which names `PP-727` as the example of an id that would breach the ceiling.
# That is ED-IN-0159 §2.4 ("the instrument counted itself") recurring VERBATIM in a new instrument
# written by someone who had read the finding — which is the argument for running a new gate before
# believing it. Excluding this one file is the narrowest fix that keeps the example readable; the
# alternative, never writing an out-of-range id in the prose, makes the rule harder to explain.
SELF = os.path.relpath(os.path.abspath(__file__), REPO_ROOT)


def _iter_live_files():
    for root in SCAN_ROOTS:
        base = os.path.join(REPO_ROOT, root)
        if not os.path.isdir(base):
            continue
        for dirpath, dirnames, filenames in os.walk(base):
            dirnames[:] = [d for d in dirnames if d != 'deprecated']
            for fn in filenames:
                if not fn.endswith(SCAN_EXTS):
                    continue
                full = os.path.join(dirpath, fn)
                if os.path.relpath(full, REPO_ROOT) == SELF:
                    continue
                yield full


def check_archive_pointers_name_the_fork(violations):
    """R1 — a pointer at an evacuated register must say where it went."""
    path = os.path.join(REPO_ROOT, REGISTER)
    try:
        with open(path, encoding='utf-8') as fh:
            lines = fh.read().splitlines()
    except OSError as exc:
        violations.append(f'{REGISTER}: unreadable ({exc})')
        return
    for i, line in enumerate(lines, 1):
        for pointer in ARCHIVE_POINTER_RE.findall(line):
            if os.path.exists(os.path.join(REPO_ROOT, pointer)):
                continue                      # still on main: nothing to annotate
            if FORK_REF not in line:
                violations.append(
                    f'{REGISTER}:{i}: points at {pointer}, which does not exist on main, '
                    f'and the line names no fork ref — add `FORK: {FORK_REF}`')


def check_pp_is_frozen(violations):
    """R2 — no id above the ceiling; PP allocates nothing new."""
    for path in _iter_live_files():
        try:
            with open(path, encoding='utf-8', errors='replace') as fh:
                text = fh.read()
        except OSError:
            continue
        rel = os.path.relpath(path, REPO_ROOT)
        for match in PP_CITATION_RE.finditer(text):
            num = int(match.group(1))
            if num > PP_FROZEN_CEILING:
                violations.append(
                    f'{rel}: {match.group(0)} exceeds the frozen ceiling PP-{PP_FROZEN_CEILING}. '
                    f'PP is frozen historical vocabulary (Jordan, 2026-08-14) — new work takes an '
                    f'ED-<LANE>-NNNN id, not a patch number')


def run_checks():
    violations = []
    check_archive_pointers_name_the_fork(violations)
    check_pp_is_frozen(violations)
    return violations


def main(argv):
    violations = run_checks()
    if violations:
        print(f'[pp-frozen ✗] {len(violations)} violation(s):')
        for v in violations:
            print(f'  {v}')
        return 1
    print(f'[pp-frozen ✓] archive pointers name the fork; no PP above the frozen '
          f'ceiling PP-{PP_FROZEN_CEILING}')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
