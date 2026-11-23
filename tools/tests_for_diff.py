#!/usr/bin/env python3
"""tests_for_diff.py -- which test suites a session's edits call for, and (with --run) run them.

An INNER-LOOP ACCELERATOR, not a gate: CI runs everything and is the full-suite tier (`CLAUDE.md` section 8).
It reads the files this session changed (committed since the branch left `origin/main`, staged, unstaged,
untracked) and prints the narrowest honest command. Every test belongs to one LANE: the season loop, the engine, or
one subsystem (combat, mass battle, social contest, threadwork); the root `conftest.py` owns the assignment, as a
marker. A change runs its own lane and no other:

  * a test file edited                                    ->  that file alone;
  * `engine/season/` edited                               ->  `pytest -m season_loop`; no subsystem lane (their
    tests execute `modules/` and the dice engine, nothing in `engine/season/`);
  * `modules/<s>/` or `systems/<s>/` edited               ->  `pytest -m <s>`;
  * anything else (engine/dice_engine/, engine/substrate/, exporters, registries, tools/)  ->  no narrowing: it
    prints the full-gate commands of `CLAUDE.md` section 8, because every lane reaches it;
  * only prose changed (.md and the like)                 ->  nothing to run beyond the validators.

WHAT THE NARROW ANSWER DOES NOT COVER, said here because it is the cost of skipping: the season suite builds a whole
realm, so its tests execute the combat, mass-battle and contest modules too. A subsystem edit that changes what a realm
does shows up there, and in the realm-hash goldens, only when the season lane runs; with this tool that is CI's run.
If your edit could change a realm (a module's output the season loop reads), run `-m season_loop` as well.

WHO USES IT: `/close` (`.claude/commands/close.md` step 4) and the inner loop. `methodology-execute`'s BATCH-CLOSE does
not: its lanes are the ones its plan names (v12 P18).

A SUBSYSTEM'S SUITE is its lane plus its `<lane>_season` marker: the subsystem's tests that live in `engine/season/tests/` are
`season_loop` by tree, and the second marker (root `conftest.py`, `SEASON_SUITES`) selects them. `--suite` picks suites by name,
`--list` names every lane and suite, `--all` prints the full gates.

Usage:  python tools/tests_for_diff.py [--base REF] [--run] [--suite NAME[,NAME...]] [--list] [--all]
"""
import argparse
import os
import shlex
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# source directory -> lane marker. The lanes and the test-file patterns have ONE owner: the root conftest.py.
SOURCE_PREFIXES = {
    "modules/combat/": "combat or pc_season", "systems/combat/": "combat or pc_season",
    "modules/mass_battle/": "mass_battle or mb_season", "systems/mass_battle/": "mass_battle or mb_season",
    "modules/social_contest/": "social_contest or sc_season", "systems/social_contest/": "social_contest or sc_season",
    "systems/threadwork/": "threadwork",
    "engine/season/": "season_loop",
}
PROSE_SUFFIXES = (".md", ".txt", ".rst")
TREES = ["tests/valoria", "engine/season/tests", "engine/tests"]


def _git(*args):
    r = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)
    return r.stdout.split("\n") if r.returncode == 0 else []


def changed_files(base):
    names = set()
    mb = _git("merge-base", "HEAD", base)[0].strip() if _git("rev-parse", "--verify", base) else ""
    if mb:
        names.update(_git("diff", "--name-only", f"{mb}...HEAD"))
    names.update(_git("diff", "--name-only"))
    names.update(_git("diff", "--name-only", "--cached"))
    names.update(_git("ls-files", "-o", "--exclude-standard"))
    return sorted(n for n in names if n and os.path.exists(os.path.join(ROOT, n)))


def _is_test_file(f):
    return f.endswith(".py") and os.path.basename(f).startswith("test_") and (
        f.startswith("tests/valoria/") or f.startswith("engine/season/tests/") or f.startswith("engine/tests/"))


def classify(files):
    """-> (lanes touched, test files edited, files that forbid narrowing, prose-only files).

    Every test belongs to one LANE (the season loop, the engine, or one subsystem; `conftest.py` assigns it) and a
    change runs its own lane. A test file edited -> that file alone; a source tree with a lane (`SOURCE_PREFIXES`)
    -> `-m <lane>`; anything else (the dice engine, substrate, exporters, registries, tools) reaches every lane and is
    wide; prose runs nothing."""
    lanes, tests, wide, prose = set(), [], [], []
    for f in files:
        hit = next((m for p, m in SOURCE_PREFIXES.items() if f.startswith(p) and not f.startswith("engine/season/tests/")), None)
        if _is_test_file(f):
            tests.append(f)
        elif hit:
            lanes.add(hit)
        elif f.endswith(PROSE_SUFFIXES):
            prose.append(f)
        else:
            wide.append(f)
    return sorted(lanes), sorted(tests), wide, prose


def commands(lanes, tests, wide):
    # `--durations=30` is the reading a `--timeout=<budget>` is a multiple of; the budget itself is a reading, not a
    # constant, so the caller adds `--timeout` (`.claude/commands/close.md` step 4).
    if wide:
        return [f"python -m pytest {' '.join(TREES[:1])} -q -n auto --durations=30",
                "python -m pytest engine/season/tests -q -n auto --dist worksteal --durations=30",
                "python -m pytest engine/tests -q --durations=30"]
    cmds = [f"python -m pytest {' '.join(TREES)} -m {shlex.quote(m)} -q -n auto --dist worksteal --durations=30" for m in lanes]
    if tests:
        cmds.append("python -m pytest " + " ".join(tests) + " -q --durations=30")
    return cmds


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--base", default="origin/main")
    ap.add_argument("--run", action="store_true",
                    help="run every command and report each one's verdict (exit 1 if any is red)")
    ap.add_argument("--suite", help="comma-separated lane or suite names (see --list): run those across the three trees, whatever changed")
    ap.add_argument("--list", action="store_true", help="name every lane and suite (the root conftest.py owns them)")
    ap.add_argument("--all", action="store_true", help="the full gates, whatever changed")
    a = ap.parse_args(argv)
    if a.list:
        sys.path.insert(0, ROOT)
        import conftest
        print("lanes:  " + ", ".join(conftest.SUBSYSTEM_FILES))
        print("suites: " + ", ".join(conftest.SEASON_SUITES) + "  (a second marker on engine/season/tests files, never a lane)")
        return 0
    if a.suite:
        files, lanes, tests, wide, prose = [], [" or ".join(n.strip() for n in a.suite.split(",") if n.strip())], [], [], []
    elif a.all:
        files, lanes, tests, wide, prose = [], [], [], ["--all"], []
    else:
        files = changed_files(a.base)
        lanes, tests, wide, prose = classify(files)
    print(f"changed files: {len(files)}  | lanes touched: {lanes or 'none'}  | test files: {len(tests)}  | "
          f"wide: {len(wide)}  | prose only: {len(prose)}")
    if wide:
        print("no narrowing, because of: " + ", ".join(wide[:6]) + (" ..." if len(wide) > 6 else ""))
    cmds = commands(lanes, tests, wide)
    if not cmds:
        print("nothing to run beyond the validators (`python tools/valoria_local.py --staged`).")
        return 0
    for c in cmds:
        print("  " + c)
    if a.run:
        # Every tree runs and reports, so a red in the first does not hide the others' verdicts.
        verdicts = [(c, subprocess.run(shlex.split(c), cwd=ROOT).returncode) for c in cmds]
        for c, rc in verdicts:
            print(("green        " if rc == 0 else f"RED (exit {rc})  ") + c)
        return 1 if any(rc for _, rc in verdicts) else 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
