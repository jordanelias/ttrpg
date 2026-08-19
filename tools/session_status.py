#!/usr/bin/env python3
"""
session_status.py — Claude Code SessionStart hook.

WHAT A SESSION SEES. This is T1 (CLAUDE.md §0.3): the attention surface. It is the
first thing every session reads and it therefore decides what every session works on.

AMENDED 2026-08-19 (Act 4 / Act 3, Jordan-directed: "I need to break out of the
infrastructure loop in the repository").

Until today this banner printed ~389 named units of pending work — 242 open EDs, 24 lane
items, 6 stale audit families, a stale board, an uncomputed repo-state grade — and **none
of them concerned the game**. The single game line, `M1 0/7 junctures done`, carried no
imperative verb and sat above six `⚠` warnings. The only imperative in the whole banner
was `run python tools/review_core.py --json`. It worked exactly as built: it was designed
to make process debt unmissable, and it did, so process debt is what got done.

So the banner now prints ONE thing: the game, and the next concrete increment on it.

THIS IS ALSO THE CHEAPEST FALSIFIABLE TEST OF THE WHOLE DIAGNOSIS (§0.3). Change nothing
else, print the juncture line, and watch one session. If it still writes apparatus, the
ordering in `proposals/2026-08-18-breaking-the-recursion.md` is wrong and that document
should be attacked accordingly. That is the experiment; do not quietly re-add lines to the
banner while it is running, or it measures nothing.

NOTHING WAS DELETED. `session_open_work.py`, `review_core.py`, `currency_consistency_check.py`
and `workplan_status.py` all still exist and still run in CI. They are no longer *pushed* at
a session that did not ask. One pointer line below says how to get them, so the data is one
command away rather than unmissable. Reverting Act 3 is `git revert` of this file.
"""
import os
import subprocess
import sys


def sh(args):
    r = subprocess.run(['git'] + args, capture_output=True, text=True)
    return r.stdout.strip() if r.returncode == 0 else ''


def game_lines():
    """The one thing a session sees: the milestone deliverable and its next increment.

    Reads the progress board for the first M1 juncture that is not done, and — when the
    acceptance oracle can run — the EXECUTION verdict, which is the referent CLAUDE.md
    §0.2 binds `done` to. Never allowed to break session start.
    """
    out = []
    juncture = None
    try:
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        import ci_common
        # load_yaml is the INTENDED owner of YAML register load (ci_common.py:445) — composing
        # on it rather than adding another bare loader, which is both §8 and what
        # test_the_bare_yaml_load_residual_can_only_shrink pins. (That test counts the literal
        # string, so do not name the bare call here — the mention alone trips it.)
        board = ci_common.load_yaml('workplans/workplan_v6_progress.yaml', default={})
        js = board['milestones']['M1']['junctures']
        done = sum(1 for j in js if j.get('state') == 'done')
        for i, j in enumerate(js, 1):
            if j.get('state') != 'done':
                juncture = (i, len(js), done, j)
                break
        if juncture:
            i, n, done, j = juncture
            title = str(j.get('label') or j.get('title') or f'juncture {i}')
            owns = ' '.join(str(j.get('owner_deliverable') or '').split())
            nxt = ' '.join(str(j.get('next') or '—').split())
            out.append(f"▶ THE GAME — M1 juncture {i}/{n} ({done}/{n} done) · {title}"
                       + (f" [{j['owner']}]" if j.get('owner') else ''))
            if owns:
                out.append(f"  deliverable: {owns[:140]}")
            out.append(f"  board says next: {nxt[:140]}")
            if j.get('blocked_on') and str(j['blocked_on']) not in ('None', 'null', ''):
                out.append(f"  blocked_on: {str(j['blocked_on'])[:110]}")
    except Exception:
        pass

    # The execution referent. `done` means the behaviour RUNS (CLAUDE.md §0.2), and this is
    # the instrument that says whether it does. It refuses to guess, which is why it is here.
    try:
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        import m1_acceptance
        res = m1_acceptance.collect()
        rows = res.get('rows') or []
        measured = sum(1 for r in rows if r.get('state') in ('measured', 'partial'))
        failed = [r['row'] for r in rows if r.get('passes') is False]
        out.append(f"  DOES IT RUN? {res.get('verdict', '?')} — {measured}/{len(rows)} rows measured"
                   + (f", failing: {', '.join(failed)}" if failed else ''))
        out.append("  (that is the referent `done` binds to — CLAUDE.md §0.2; "
                   "detail: python tools/m1_acceptance.py --summary)")
    except Exception:
        pass

    if not out:
        out.append("▶ THE GAME — board unreadable; open workplans/workplan_v6_progress.yaml")
    return out


def main():
    print("=== Valoria ===")
    branch = sh(['rev-parse', '--abbrev-ref', 'HEAD'])
    if branch:
        print(f"branch:      {branch}")
    last = sh(['log', '-1', '--oneline'])
    if last:
        print(f"last commit: {last}")
    status = sh(['status', '--porcelain'])
    print(f"working tree: {len(status.splitlines())} uncommitted change(s)" if status
          else "working tree: clean")

    print()
    for ln in game_lines():
        print(ln)

    # ── The apparatus is available, not advertised. ────────────────────────────────────
    # One line replaces ~389. Act 4's §0 amendment means a finding here is fixed in the
    # commit or dropped, so a session that pulls this up has to DO something with it.
    print()
    print("process/apparatus state is no longer printed here (Act 3, 2026-08-19). On demand:")
    print("  python tools/session_open_work.py   # lane items, editorial debt, stale audits")
    print("  python tools/review_core.py --summary")

    if os.path.exists('HANDOFF.md'):
        try:
            with open('HANDOFF.md', encoding='utf-8', errors='replace') as f:
                lines = f.read().splitlines()
        except OSError:
            lines = []
        out, grab = [], False
        for ln in lines:
            if ln.strip().lower().startswith('## next'):
                grab = True
                out.append(ln)
                continue
            if grab and ln.startswith('## '):
                break
            if grab:
                out.append(ln)
        if out:
            print()
            print('\n'.join(out[:12]))
    else:
        print("(no HANDOFF.md yet — create one to capture next actions)")

    sys.exit(0)


if __name__ == '__main__':
    main()
