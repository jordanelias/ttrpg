#!/usr/bin/env python3
"""ci_program_claim_check.py — warn when a change touches a path a LIVE program has claimed.

ED-IN-0098, 2026-07-30. REPORT-ONLY.

THE INCIDENT THIS EXISTS FOR
----------------------------
W4 (ED-IN-0097) retired `tools/registry.py` on a correct zero-consumer grep. It was reversed at
the gate, because `audit/2026-07-29-centralization-single-owner/` had claimed that exact file —
its §0.1 row 1 is *titled* "`tools/registry.py` retirement race" and it predicted the outcome
verbatim: the grep-then-move precedent finds no consumers *precisely because its W1 has not run*.

The interlock's declared executable form was "a `[CSO]` blocking row in `04_execution_ledger.md`".
That row was never written. So the prediction was correct, recorded, and inert — prose does not
execute. This tool is the missing executable form, generalised.

WHY NOT A LANE CHECK (an idea considered and rejected on evidence)
-----------------------------------------------------------------
The obvious design is a lane-ownership gate keyed on `build_decisions.infer_lane`. It would NOT
have caught this: `infer_lane('tools/registry.py')` returns `IN`, and W4 *was* the IN session. The
collision was between two concurrent programs INSIDE one lane, which lane inference cannot see.
What distinguishes them is the program, so the claim — not the lane — is the right key.

WHERE CLAIMS COME FROM
----------------------
`workplans/POINTER_*.md`, the existing pointer convention — no new register (CLAUDE.md §8). A
pointer declares `**liveness:**` and `**scope:**`; this reads the backtick-quoted repo paths out
of the scope/target lines of every pointer whose liveness is LIVE (incl. LIVE-PARTIAL). CSO's
pointer says: "WS1 completion (`tools/registry.py` made real)" — which is exactly the signal.

HONEST LIMITS (do not overstate this tool)
------------------------------------------
* Claims are only as good as the prose. A program that never names a file in its pointer's scope
  line is invisible here. This narrows the blind spot; it does not close it.
* It cannot tell "I am the claiming program" from "I am a different program" automatically —
  so it reports the claim and names the claimant, and the human/agent decides. Use
  `--self <pointer-substring>` to suppress your own program's claims.
* REPORT-ONLY by design. A claim is a coordination signal, not a proof of wrongness; several
  legitimate changes touch claimed files. Promoting this to blocking needs Jordan's call.

USAGE
    python3 tools/ci_program_claim_check.py --staged
    python3 tools/ci_program_claim_check.py --base origin/main
    python3 tools/ci_program_claim_check.py --staged --self code_shape
"""
from __future__ import annotations

import argparse
import glob
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
POINTER_GLOB = os.path.join(ROOT, 'workplans', 'POINTER_*.md')

# Top-level trees a claimed path can start with — mirrors ci_claude_workflow_paths.TREES so a
# backticked prose word like `resolve()` is not mistaken for a file.
TREES = (
    'designs', 'sim', 'systems', 'engine', 'references', 'params', 'tests', 'registers', 'canon',
    'audit', 'arcs', 'godot', 'tools', 'skills', 'proposals', 'workplans', 'deprecated', 'dashboard',
)
LIVE_RE = re.compile(r'^\*\*liveness:\*\*\s*(.+)$', re.M | re.I)
SCOPE_RE = re.compile(r'^\*\*(?:scope|target):\*\*\s*(.+?)(?=^\*\*|\Z)', re.M | re.I | re.S)
BACKTICK_RE = re.compile(r'`([^`]+)`')


def _is_live(text: str) -> tuple[bool, str]:
    m = LIVE_RE.search(text)
    if not m:
        return False, 'no liveness line'
    verdict = m.group(1).strip()
    return bool(re.match(r'\**\s*LIVE', verdict, re.I)), verdict


def _claimed_paths(text: str) -> set[str]:
    """Repo paths named in backticks inside the scope/target blocks."""
    out: set[str] = set()
    for block in SCOPE_RE.findall(text):
        for tok in BACKTICK_RE.findall(block):
            tok = tok.strip().split()[0] if tok.strip() else ''
            tok = tok.rstrip(',.;:)').replace('\\', '/')
            if not tok or tok.startswith('#'):
                continue
            if tok.split('/', 1)[0] in TREES:
                out.add(tok)
    return out


def load_claims(self_filter: str | None = None) -> dict[str, set[str]]:
    """{pointer basename: {claimed path, ...}} for every LIVE pointer."""
    claims: dict[str, set[str]] = {}
    for path in sorted(glob.glob(POINTER_GLOB)):
        name = os.path.basename(path)
        if self_filter and self_filter in name:
            continue
        text = open(path, encoding='utf-8', errors='replace').read()
        live, _verdict = _is_live(text)
        if not live:
            continue
        paths = _claimed_paths(text)
        if paths:
            claims[name] = paths
    return claims


def changed_files(staged: bool, base: str | None) -> list[str]:
    if staged:
        cmd = ['git', 'diff', '--cached', '--name-only']
    elif base:
        cmd = ['git', 'diff', '--name-only', f'{base}...HEAD']
    else:
        cmd = ['git', 'diff', '--name-only', 'HEAD']
    out = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    return [ln.strip() for ln in out.stdout.splitlines() if ln.strip()]


def overlaps(changed: list[str], claims: dict[str, set[str]]) -> list[tuple[str, str, str]]:
    """(changed file, claimant pointer, claimed path). A claim on a DIRECTORY covers its files."""
    hits = []
    for f in changed:
        for pointer, paths in claims.items():
            for claimed in paths:
                if f == claimed or (claimed.endswith('/') and f.startswith(claimed)) \
                        or f.startswith(claimed.rstrip('/') + '/'):
                    hits.append((f, pointer, claimed))
    return hits


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--staged', action='store_true', help='check staged files (pre-commit)')
    ap.add_argument('--base', help='check files changed vs this ref (e.g. origin/main)')
    ap.add_argument('--self', dest='self_filter',
                    help='substring of YOUR program pointer, to suppress your own claims')
    args = ap.parse_args(argv)

    claims = load_claims(args.self_filter)
    changed = changed_files(args.staged, args.base)
    print(f'[program-claims] {len(claims)} LIVE pointer(s) declaring paths; '
          f'{len(changed)} changed file(s)')
    if not changed:
        print('[program-claims ✓] nothing to check')
        return 0

    hits = overlaps(changed, claims)
    if not hits:
        print('[program-claims ✓] no changed file is claimed by a LIVE program pointer')
        return 0

    by_pointer: dict[str, list[tuple[str, str]]] = {}
    for f, pointer, claimed in hits:
        by_pointer.setdefault(pointer, []).append((f, claimed))
    print(f'\n[program-claims ⚠] {len(hits)} overlap(s) with {len(by_pointer)} LIVE program(s).')
    print('REPORT-ONLY. A claim is a coordination signal, not proof of wrongness — but if you are')
    print('about to DELETE or RETIRE one of these, read the claiming plan first (W4/ED-IN-0097).')
    for pointer, rows in sorted(by_pointer.items()):
        print(f'\n  claimant: workplans/{pointer}')
        for f, claimed in sorted(set(rows)):
            via = '' if f == claimed else f'   (via claim on `{claimed}`)'
            print(f'    {f}{via}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
