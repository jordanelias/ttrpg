#!/usr/bin/env python3
"""FALSIFIER for the 2026-09-13 handoff split (ED-IN-0221). Re-derives every number that entry
states, and re-proves the split lossless, from the tree and git.

    python tools/verify_handoff_split.py            # verify against the split's parent commit
    python tools/verify_handoff_split.py --before <ref>

WHAT IT PROVES, per lane: the line MULTISET of `HANDOFF_<LANE>.md` plus `HANDOFF_<LANE>_closed.md`
plus `HANDOFF_<LANE>_history.md` (where that exists) CONTAINS the pre-split file's multiset with
nothing missing.

⚠ THE `_history.md` SIBLING WAS ADDED 2026-09-17 (`ED-IN-0240`, Jordan: *"TRIM THE HANDOFFS"*), and
this tool had to learn about it or it would have reported a FALSE ALARM on the IN lane — 65k tokens
of narrative left the live file for a destination this summation did not know. A falsifier that
cries wolf gets ignored, which is worse than not having one. `_closed` holds what the marker
predicate proved FINISHED; `_history` holds dated narrative regardless of markers, with every marker
it carries indexed verbatim in the live file. That is the whole safety claim of the
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
import re, subprocess, sys, os
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


# ── Structural invariant: a heading's PARENT does not change (ED-IN-0241) ─────
#
# ⚠ THIS EXISTS BECAUSE THE SAME DEFECT FIRED THREE TIMES IN ONE SESSION, and each time it was
# patched with a hard-coded list of section names instead of a rule. Jordan: *"stop hard coding"*.
#
# THE DEFECT: a splitter that slices a section as "this heading to the next heading of ANY level"
# moves a `##` head and LEAVES ITS `###` CHILDREN BEHIND. The children then sit under whatever
# section happens to precede them, which reads as though someone filed them there deliberately.
# It happened to `## Next actions`'s ruling records, to `## ⚠ WAS CURRENT — 2026-08-27`'s five
# subsections, and a heading inserted on "the first `###` in the file" landed inside the ratified
# work order, briefly filing it under "RULINGS AND STANDING STATE".
#
# THE RULE, which needs no names: A HEADING BELONGS TO ITS NEAREST PRECEDING HEADING OF A HIGHER
# LEVEL. So a unit is a SUBTREE, not a slice, and moving a parent moves its children. What this
# function checks is the observable consequence: for every heading that is STILL IN THE SAME FILE
# after the edit, its parent heading must be the one it had before. A heading that moved to another
# file legitimately gets a new parent there, so it is excluded — the invariant is about what STAYED.


def _parents(text):
    """{heading: parent heading or None}, structurally, fence-aware."""
    out, stack, fence = {}, {}, None
    for ln in text.split('\n'):
        f = re.match(r'^\s*(`{3,}|~{3,})', ln)
        if f:
            tok = f.group(1)[0]
            fence = None if fence == tok else (fence or tok)
            continue
        if fence:
            continue
        m = re.match(r'^(#{1,6}) (.+)$', ln)
        if not m:
            continue
        lvl, head = len(m.group(1)), m.group(2).strip()
        out[head] = next((stack[l] for l in range(lvl - 1, 0, -1) if l in stack), None)
        stack[lvl] = head
        for l in [l for l in stack if l > lvl]:
            del stack[l]
    return out


def check_structure(before, paths):
    """REPORT-ONLY. Prints every heading that stayed in its file under a DIFFERENT parent.

    Report-only rather than blocking, and that is a ruling rather than a preference: a reparent is
    sometimes deliberate — moving a `##` out legitimately leaves its surviving children needing a
    new home — so a failing verdict here would halt on a heuristic, which Jordan ruled against
    (`CLAUDE.md` §10: *"a breaker halting a large audit on a heuristic costs more than the defect
    it caught"*). It always returns 0. READ ITS OUTPUT; it cannot decide for you.
    """
    bad = 0
    print(f'\n{"file":<46}{"headings":>10}{"reparented":>12}  verdict')
    for rel in paths:
        old = _git('show', f'{before}:{rel}')
        if old is None:
            continue
        pb, pa = _parents(old), _parents(open(os.path.join(ci_common.REPO, rel),
                                              encoding='utf-8').read())
        moved = [h for h in pb if h in pa and pb[h] != pa[h]]
        bad += len(moved)
        print(f'{rel:<46}{len(pa):>10}{len(moved):>12}  '
              f'{"OK" if not moved else "*** REPARENTED ***"}')
        for h in moved[:5]:
            print(f'      {h[:68]!r}\n        was under {pb[h]!r}\n        now under {pa[h]!r}')
    if bad:
        print(f'  {bad} heading(s) reparented — REPORT-ONLY. Judge each: a `##` moved out leaves '
              'its surviving children needing a parent, which is legitimate. An UNINTENDED one '
              'reads as though someone filed a section somewhere deliberately.')
    return 0


def main(argv):
    before = _before_ref(argv[1] if len(argv) > 2 and argv[1] == '--before' else None)
    if len(argv) > 2 and argv[1] == '--before':
        before = argv[2]
    root = ci_common.REPO
    print(f'[verify-handoff-split] {SPLIT_ED} · before = {before}\n')
    print(f'{"lane":<6}{"before":>10}{"live":>10}{"closed":>10}{"history":>10}'
          f'{"lines lost":>12}  verdict')
    bad = 0
    total_moved = 0
    for lane in LANES:
        live_p = f'registers/handoffs/HANDOFF_{lane}.md'
        clos_p = f'registers/handoffs/HANDOFF_{lane}_closed.md'
        hist_p = f'registers/handoffs/HANDOFF_{lane}_history.md'
        orig = _git('show', f'{before}:{live_p}')
        if orig is None:
            print(f'{lane:<6}{"—":>10}  cannot read {live_p} at {before} — pass --before <ref>')
            bad += 1
            continue
        live = open(os.path.join(root, live_p), encoding='utf-8').read()
        clos = open(os.path.join(root, clos_p), encoding='utf-8').read()
        hist_abs = os.path.join(root, hist_p)
        hist = open(hist_abs, encoding='utf-8').read() if os.path.exists(hist_abs) else ''
        lost = Counter(orig.split('\n')) - (Counter(live.split('\n')) + Counter(clos.split('\n'))
                                            + Counter(hist.split('\n')))
        n_lost = sum(lost.values())
        ok = n_lost == 0
        bad += 0 if ok else 1
        total_moved += ci_common.tokens(clos) + ci_common.tokens(hist)
        print(f'{lane:<6}{ci_common.tokens(orig):>10,}{ci_common.tokens(live):>10,}'
              f'{ci_common.tokens(clos):>10,}{ci_common.tokens(hist):>10,}{n_lost:>12}  '
              f'{"LOSSLESS" if ok else "*** LOST CONTENT ***"}')
        for line, c in list(lost.items())[:5]:
            print(f'        lost x{c}: {line[:100]!r}')
    print(f'\nclosed narrative moved out of the orientation surfaces: {total_moved:,} tokens')

    # Losslessness is only half the claim; the other half is that what STAYED still reads as the
    # document it was. Derived from the tree, never from a list of section names.
    watched = ['HANDOFF.md'] + [f'registers/handoffs/HANDOFF_{l}.md' for l in LANES]
    bad += check_structure(before, watched)

    print('[verify-handoff-split] ' + ('OK — every pre-split line is still in the tree; heading '
                                       'reparenting above is report-only'
                                       if not bad else f'FAILED on {bad} check(s)'))
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
