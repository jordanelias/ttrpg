#!/usr/bin/env python3
"""ci_gate_coverage.py — derive the local gate instead of remembering it.

ED-IN-0098, 2026-07-30. REPORT-ONLY advisory, for use before commit/PR.

THE MISS THIS EXISTS FOR
------------------------
The W4 orchestrator gate (ED-IN-0097) validated `tests/valoria` plus the validators it happened to
think of, and shipped. It never ran `engine/tests`, which is a SEPARATE blocking CI job
(`sim-regression`) covering four files that wave edited — nor `tests/contracts`, which the
`unit-tests` job also runs. Both were green, so nothing broke; the point is that the gate was
complete by luck rather than by construction. Two roots forgotten in one wave, by a session that
was deliberately being careful, is a tooling problem and not an attention problem.

So: stop recalling which suites exist. Read them out of the workflow, and print the ones a
change plausibly touches alongside the full blocking-job list.

IT ALSO ANSWERS THE OTHER W4 GAP (P6)
-------------------------------------
That same gate verified the BRANCH in isolation while `main` moved underneath it — two concurrent
sessions merged during the run. CI tests the MERGE; a local suite run does not. So this also
reports how far behind `origin/main` the branch base is, because "green locally" means little if
the base is stale.

USAGE
    python3 tools/ci_gate_coverage.py                 # changed vs HEAD
    python3 tools/ci_gate_coverage.py --staged
    python3 tools/ci_gate_coverage.py --base origin/main
"""
from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORKFLOW = os.path.join(ROOT, '.github', 'workflows', 'valoria-ci.yml')

JOB_RE = re.compile(r'^  ([a-z0-9][a-z0-9-]*):\n(.*?)(?=^  [a-z0-9][a-z0-9-]*:\n|\Z)', re.M | re.S)
# A pytest target that looks like a repo path (drops flags like `-q` and pip args like `numpy`).
PYTEST_TARGET_RE = re.compile(r'pytest\s+((?:[\w./-]+\s*)+)')


def jobs() -> list[dict]:
    """Parse job id, display name, blocking-ness and pytest roots out of the CI workflow."""
    if not os.path.exists(WORKFLOW):
        return []
    text = open(WORKFLOW, encoding='utf-8', errors='replace').read()
    out = []
    for m in JOB_RE.finditer(text):
        jid, body = m.group(1), m.group(2)
        nm = re.search(r'name:\s*(.+)', body)
        roots = set()
        for tm in PYTEST_TARGET_RE.finditer(body):
            for tok in tm.group(1).split():
                tok = tok.strip()
                if tok.startswith('-') or '/' not in tok:
                    continue
                if os.path.isdir(os.path.join(ROOT, tok)) or os.path.isfile(os.path.join(ROOT, tok)):
                    roots.add(tok)
        out.append({
            'id': jid,
            'name': nm.group(1).strip() if nm else jid,
            'blocking': 'continue-on-error' not in body,
            'pytest_roots': sorted(roots),
        })
    return out


def changed_files(staged: bool, base: str | None) -> list[str]:
    if staged:
        cmd = ['git', 'diff', '--cached', '--name-only']
    elif base:
        cmd = ['git', 'diff', '--name-only', f'{base}...HEAD']
    else:
        cmd = ['git', 'diff', '--name-only', 'HEAD']
    r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    return [ln.strip() for ln in r.stdout.splitlines() if ln.strip()]


def base_distance(ref: str = 'origin/main') -> tuple[int, str] | None:
    """How many commits `ref` has that HEAD does not. None if the ref is unknown."""
    r = subprocess.run(['git', 'rev-list', '--count', f'HEAD..{ref}'],
                       cwd=ROOT, capture_output=True, text=True)
    if r.returncode != 0:
        return None
    try:
        return int(r.stdout.strip()), ref
    except ValueError:
        return None


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--staged', action='store_true')
    ap.add_argument('--base')
    args = ap.parse_args(argv)

    all_jobs = jobs()
    test_jobs = [j for j in all_jobs if j['pytest_roots']]
    blocking = [j for j in all_jobs if j['blocking']]
    changed = changed_files(args.staged, args.base)

    print(f'[gate-coverage] {len(all_jobs)} CI job(s) parsed · {len(blocking)} blocking · '
          f'{len(changed)} changed file(s)')

    # Every pytest root in CI. This is the list a local gate must not silently subset.
    roots = sorted({r for j in test_jobs for r in j['pytest_roots']})
    print(f'\nPYTEST ROOTS RUN BY CI ({len(roots)}) — a local gate must cover ALL of these:')
    for r in roots:
        owners = [j['id'] for j in test_jobs if r in j['pytest_roots']]
        touched = [f for f in changed if f.startswith(r.rstrip('/') + '/') or f == r]
        mark = f'  <-- {len(touched)} changed file(s) under it' if touched else ''
        print(f'    python -m pytest {r:22} (job: {", ".join(owners)}){mark}')

    if roots:
        print('\n  Run them all:')
        print('    python -m pytest ' + ' '.join(roots) + ' -q')

    # Which blocking non-test jobs exist — the validators a session tends to half-remember.
    other = [j for j in blocking if not j['pytest_roots']]
    print(f'\nBLOCKING NON-TEST JOBS ({len(other)}) — each is an unbypassable gate:')
    print('    ' + ', '.join(j['id'] for j in other))

    dist = base_distance()
    if dist is not None:
        n, ref = dist
        print()
        if n:
            print(f'[gate-coverage ⚠] {ref} is {n} commit(s) ahead of HEAD. CI tests the MERGE '
                  f'RESULT; a local suite run here does not.')
            print(f'    Concurrent sessions land while you work (W4 saw two). Before the final '
                  f'gate:  git merge {ref}')
        else:
            print(f'[gate-coverage ✓] HEAD is up to date with {ref} — local green matches the '
                  f'merge result.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
