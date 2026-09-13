#!/usr/bin/env python3
"""FALSIFIER for the 2026-09-13 handoff split (ED-IN-0221). Re-derives every number that entry
states, and re-proves the split lossless, from the tree and git.

    python tools/verify_handoff_split.py            # verify against the split's parent commit
    python tools/verify_handoff_split.py --before <ref>

WHAT IT PROVES, per lane: the line MULTISET of `HANDOFF_<LANE>.md` plus `HANDOFF_<LANE>_closed.md`
CONTAINS the pre-split file's multiset with nothing missing. That is the whole safety claim of the
split — closed narrative was MOVED, never pruned — and it is the claim ED-IN-0221 would be wrong
about if this exits non-zero.

⚠ THIS IS A ONE-SHOT FALSIFIER, NOT A GATE, AND IT MUST NOT BECOME ONE. It is wired to no CI job
and no hook deliberately. Its subject is this repository's PROCESS, which is exactly what
`CLAUDE.md` §0.1 pt 5's predicate excludes from earning a guard: *"A pattern defect in an artifact
that is load-bearing only on this repository's process is not evidence the artifact needs a guard."*
It exists because two OTHER rules require it and they are narrower than that exclusion:
§0.1 pt 3 ("a result claim carries, in the same commit, the test that would have shown it wrong")
and `ED-PC-0040`'s claim-provenance gate, which refuses a ledger entry stating measured numbers
unless it names a re-runnable instrument that is in the tree. Adding it to a CI job would convert a
falsifier into the apparatus the predicate forbids. Delete it once the split is old news.
"""
import subprocess, sys, os
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ci_common

LANES = ('IN', 'MB', 'PC', 'SC')
SPLIT_ED = 'ED-IN-0221'


def _git(*args):
    r = subprocess.run(('git',) + args, capture_output=True, text=True,
                       cwd=ci_common.REPO)
    return r.stdout if r.returncode == 0 else None


def _before_ref(explicit=None):
    """The commit whose tree still holds the un-split handoffs."""
    if explicit:
        return explicit
    # ⚠ TWO CASES, AND THE FIRST VERSION OF THIS GOT THE SECOND ONE WRONG — it always returned
    # `HEAD^`, which on an uncommitted split reads one commit too far back and silently compared
    # against a pre-split file that was itself a revision out of date. Caught by the numbers not
    # matching the split's own measurement.
    #   * split already committed -> `before` is the parent of the commit that ADDED the closed file
    #   * split still uncommitted  -> `before` is HEAD, because the un-split file IS what HEAD holds
    out = _git('log', '--diff-filter=A', '--format=%H', '-1',
               '--', 'registers/handoffs/HANDOFF_IN_closed.md')
    if out and out.strip():
        return out.strip() + '^'
    return 'HEAD'


def main(argv):
    before = _before_ref(argv[1] if len(argv) > 2 and argv[1] == '--before' else None)
    if len(argv) > 2 and argv[1] == '--before':
        before = argv[2]
    root = ci_common.REPO
    print(f'[verify-handoff-split] {SPLIT_ED} · before = {before}\n')
    print(f'{"lane":<6}{"before":>10}{"live":>10}{"closed":>10}{"lines lost":>12}  verdict')
    bad = 0
    total_moved = 0
    for lane in LANES:
        live_p = f'registers/handoffs/HANDOFF_{lane}.md'
        clos_p = f'registers/handoffs/HANDOFF_{lane}_closed.md'
        orig = _git('show', f'{before}:{live_p}')
        if orig is None:
            print(f'{lane:<6}{"—":>10}  cannot read {live_p} at {before} — pass --before <ref>')
            bad += 1
            continue
        live = open(os.path.join(root, live_p), encoding='utf-8').read()
        clos = open(os.path.join(root, clos_p), encoding='utf-8').read()
        lost = Counter(orig.split('\n')) - (Counter(live.split('\n')) + Counter(clos.split('\n')))
        n_lost = sum(lost.values())
        ok = n_lost == 0
        bad += 0 if ok else 1
        total_moved += ci_common.tokens(clos)
        print(f'{lane:<6}{ci_common.tokens(orig):>10,}{ci_common.tokens(live):>10,}'
              f'{ci_common.tokens(clos):>10,}{n_lost:>12}  {"LOSSLESS" if ok else "*** LOST CONTENT ***"}')
        for line, c in list(lost.items())[:5]:
            print(f'        lost x{c}: {line[:100]!r}')
    print(f'\nclosed narrative moved out of the orientation surfaces: {total_moved:,} tokens')
    print('[verify-handoff-split] ' + ('OK — every pre-split line is still in the tree'
                                       if not bad else f'FAILED on {bad} lane(s)'))
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
