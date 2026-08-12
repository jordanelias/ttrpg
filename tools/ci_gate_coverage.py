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

# Primitives (repo root, lane roster, token estimate, ids, Status reader) are
# owned by tools/ci_common.py — plan G7, ED-IN-0159 §8.3. See its module docstring;
# the two lines below are the bootstrap, anchored on THIS file's directory.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ci_common  # noqa: E402

ROOT = ci_common.REPO
WORKFLOW = os.path.join(ROOT, '.github', 'workflows', 'valoria-ci.yml')

JOB_RE = re.compile(r'^  ([a-z0-9][a-z0-9-]*):\n(.*?)(?=^  [a-z0-9][a-z0-9-]*:\n|\Z)', re.M | re.S)
# A pytest target that looks like a repo path (drops flags like `-q` and pip args like `numpy`).
PYTEST_TARGET_RE = re.compile(r'pytest\s+((?:[\w./-]+\s*)+)')


# A validator invocation inside a job's `run:` block. Captures the tool and its args so a
# consumer can re-run EXACTLY what CI runs. Args stop at the line end or a shell operator,
# because a swallowed `&&` would turn one command into a mis-parsed two.
TOOL_CMD_RE = re.compile(
    r'python3?\s+(?:-\w+\s+)*(tools/[\w/]+\.py)([^\n|&;>]*)'
)


def jobs() -> list[dict]:
    """Parse job id, display name, blocking-ness, pytest roots and tool commands.

    SINGLE OWNER OF WORKFLOW PARSING (ED-IN-0112). This is the only function in the tree
    that reads `.github/workflows/valoria-ci.yml` structurally. `valoria_local.py --ci`
    consumes `tool_commands` from here rather than carrying its own copy of "what CI
    runs" — a second list would be a second owner of the same rule and would drift the
    moment a job was added, which is the exact §8 violation this repo keeps finding.
    """
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

        # COMMENT LINES ARE NOT INVOCATIONS. Found the hard way: valoria-ci.yml:813 is a
        # prose comment reading "bulk refresh: python3 tools/freshness_gate.py --update)."
        # Matching it would have made `--ci` run freshness_gate WITH --update — a flag that
        # REWRITES the canonical_sha pins. A read-only gate that silently mutates state is
        # strictly worse than no gate, so this filter is load-bearing, not cosmetic.
        runnable = '\n'.join(
            ln for ln in body.splitlines() if not ln.lstrip().startswith('#')
        )

        # The syntax-check job COMPILES every tool (py_compile) rather than running any.
        # Treating those as invocations would make `--ci` "run" 33 tools it never runs —
        # the compile-vs-execute confusion that makes a naive duplication count wrong.
        #
        # COMPUTED FROM `runnable`, NOT `body` — it read the raw text until 2026-08-01, so a job
        # whose COMMENT merely mentioned py_compile was classified compiles-only and had its
        # entire command list discarded. Adding three validators to validators-report with a
        # comment explaining that valoria_local is only py_compile'd took that job from 10
        # parsed commands to 0, silently: `--ci` would have stopped running ten validators and
        # reported success, and the workflow itself was unchanged in any way that mattered.
        # Exactly the "prose about a call read as a call" mistake the filter above already
        # corrects for commands; the two must be derived from the same text or they disagree.
        compiles_only = 'py_compile' in runnable
        cmds = []
        if not compiles_only:
            seen = set()
            for cm in TOOL_CMD_RE.finditer(runnable):
                script, args = cm.group(1), cm.group(2).strip()
                if not os.path.isfile(os.path.join(ROOT, script)):
                    continue
                # Strip a trailing shell line-continuation; keep real flags.
                argv = [a for a in args.split() if a != '\\']
                dedup = (script, tuple(argv))
                if dedup in seen:
                    continue
                seen.add(dedup)
                cmds.append({'script': script, 'args': argv})

        out.append({
            'id': jid,
            'name': nm.group(1).strip() if nm else jid,
            'blocking': 'continue-on-error' not in body,
            'pytest_roots': sorted(roots),
            'tool_commands': cmds,
            'compiles_only': compiles_only,
            # The job's runnable text (comments stripped). Exposed so a caller can ask "does this
            # job reference X at all?" for invocations TOOL_CMD_RE cannot parse — notably
            # `python3 -m pkg.module`, which lanchester-signature uses. Without it, "no parsed
            # commands" is indistinguishable from "covers nothing", and every pytest-only job
            # becomes a silent safe harbor for a false coverage claim (ED-IN-0119).
            'runnable': runnable,
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
