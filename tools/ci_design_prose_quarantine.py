#!/usr/bin/env python3
"""
ci_design_prose_quarantine.py — the game trees hold code, not prose.

RULE
    No tracked `.md` may live under `systems/**` or `engine/**`,
    with one exemption: `engine/season/**`, which is live game code and
    whose run reports and case briefs belong beside it.

WHY THIS EXISTS (2026-09-16, ED-IN-0231 — Jordan)
    Verbatim: *"game code keeps getting poisoned by these stray .md files that
    you are unable to consistently avoid as you are AI, so we have to quarantine
    them somehow so you stop pulling them into your sweeps or read them as
    canon."*

    The failure is not that the prose is wrong. It is that an agent sweeping
    `systems/` for a term ingests forty superseded design documents alongside
    the code and treats them as authority — which CLAUDE.md §0.05 forbids
    outright: *code is the mechanism, prose is reference*. 230 documents were
    moved to `.designs/` (hidden, so ripgrep and `glob.glob` skip it). This gate
    is what stops the tree refilling: measured over PRs #337–#404, prose was
    written back into `systems/` in ten separate pull requests, 2,364 lines,
    accelerating rather than decaying — #403 landed 15 such files and #404
    proposes 10 more.

    It earns its existence under CLAUDE.md §0.1 pt 5: the defective artifact is
    load-bearing on THE GAME. Prose in the code trees is what a session reads
    when it resolves a mechanic, so a defect here reaches the engine. This is
    not a guard on a guard.

WHERE THE PROSE GOES INSTEAD
    * new design work            -> `proposals/`
    * superseded design prose    -> `.designs/` (+ a row in
                                    `references/restructure_ledger.md`)
    * anything the engine READS  -> a typed artifact under
                                    `engine/engine_params/` (§0.05)

    A run report or case brief produced BY `engine/season/` stays with it.

ZERO IS THE INVARIANT, NOT A RATCHET. There is nothing to grandfather: the
count was driven to 0 in the same commit that added this file. A ratchet would
encode a tolerance that does not exist.

CLI:
    python tools/ci_design_prose_quarantine.py            # whole tree (CI)
    python tools/ci_design_prose_quarantine.py --staged   # the git index (pre-commit)

Exit 0 = clean, 1 = prose found in a game tree.
"""
import subprocess
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ci_common  # noqa: E402

# ONE OWNER for the repo root (plan G7, ED-IN-0159 §8.1) — never re-derive it.
REPO = ci_common.REPO

# Trees that hold the game. Prose in them is the defect this gate names.
GAME_TREES = ('systems/', 'engine/')

# `engine/season/` is Layer 2 — the live season loop. Its own run reports,
# case briefs and decision logs are execution artifacts, not design prose, and
# Jordan exempted the tree by name. Keep this tuple SHORT: every entry is a
# place prose may accumulate unobserved.
EXEMPT = ('engine/season/',)

ARCHIVE = '.designs/'


def _tracked_md(staged=False):
    if staged:
        args = ['git', '-C', REPO, 'diff', '--cached', '--name-only', '--diff-filter=ACMR']
    else:
        args = ['git', '-C', REPO, 'ls-files']
    out = subprocess.run(args, capture_output=True, text=True).stdout
    return [p for p in out.split('\n') if p.endswith('.md')]


def offenders(staged=False):
    """Every tracked .md sitting in a game tree without an exemption."""
    bad = []
    for path in _tracked_md(staged=staged):
        if not path.startswith(GAME_TREES):
            continue
        if path.startswith(EXEMPT):
            continue
        bad.append(path)
    return sorted(bad)


def main():
    staged = '--staged' in sys.argv
    bad = offenders(staged=staged)
    scope = 'staged changes' if staged else 'the working tree'
    if not bad:
        trees = ', '.join(GAME_TREES)
        print(f'[QUARANTINE OK] no design prose under {trees} across {scope} '
              f'(exempt: {", ".join(EXEMPT)}).')
        return 0
    print(f'[QUARANTINE FAILED] {len(bad)} markdown file(s) in a game tree:\n')
    for p in bad:
        print(f'  {p}')
    print(
        '\nThe game trees hold code. Move design prose to `proposals/` if it is new,\n'
        f'or to `{ARCHIVE}` if it is superseded — and add a row to\n'
        'references/restructure_ledger.md so the old path still resolves.\n'
        'A value the engine READS belongs in engine/engine_params/ (CLAUDE.md §0.05).\n'
        f'Exempt by ruling: {", ".join(EXEMPT)}'
    )
    return 1


if __name__ == '__main__':
    sys.exit(main())
