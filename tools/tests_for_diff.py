#!/usr/bin/env python3
"""tests_for_diff.py -- which test suites a session's edits call for, and (with --run) run them.

An INNER-LOOP ACCELERATOR, not a gate: CI runs everything and is the full-suite tier (`CLAUDE.md` section 8).
It reads the files this session changed (committed since the branch left `origin/main`, staged, unstaged,
untracked) and prints the narrowest honest command. A test belongs to the SEASON LOOP (`engine/season/tests/`, and
the `tests/valoria` files that name `engine.season`) or to ONE SUBSYSTEM (combat, mass battle, social contest:
the file-name markers `conftest.py` owns); a change runs its own group and no other:

  * a test file edited                                    ->  that file alone;
  * `engine/season/` edited (the loop, its data, its test helpers)  ->  the season suite and the `tests/valoria`
    files that run it, and NOT the subsystem suites (they execute `modules/` and the dice engine, nothing in
    `engine/season/`);
  * `modules/<s>/` or `systems/<s>/` edited               ->  `pytest -m <s>` over all three test trees;
  * anything else (engine/dice_engine/, engine/substrate/, exporters, registries, tools/)  ->  no narrowing: it
    prints the full-gate commands of `CLAUDE.md` section 0.4, because every suite reaches it;
  * only prose changed (.md and the like)                 ->  nothing to run beyond the validators.

WHAT THE NARROW ANSWER DOES NOT COVER, said here because it is the cost of skipping: the season suite builds a whole
realm, so its tests execute the combat, mass-battle and contest modules too (measured 2026-11-04: a `modules/combat/`
edit is reached by tests costing about three quarters of the suite). A subsystem edit that changes what a realm
does shows up there, and in the realm-hash goldens, only when the full season suite runs; with this tool that is
CI's run. If your edit could change a realm (a module's output the season loop reads), run the season suite as well.

Usage:  python tools/tests_for_diff.py [--base REF] [--run]
"""
import argparse
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# source directory -> marker. The marker names and the test-file patterns have ONE owner: the root conftest.py.
SOURCE_PREFIXES = {
    "modules/combat/": "combat", "systems/combat/": "combat",
    "modules/mass_battle/": "mass_battle", "systems/mass_battle/": "mass_battle",
    "modules/social_contest/": "social_contest", "systems/social_contest/": "social_contest",
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


SEASON_PREFIX = "engine/season/"
SEASON_TESTS = "engine/season/tests/"


def _is_test_file(f):
    return f.endswith(".py") and os.path.basename(f).startswith("test_")


def classify(files):
    """-> (markers touched, season loop touched, test files edited, files that forbid narrowing, prose-only files).

    Groups, in the order a file is tried: a subsystem source tree (`SOURCE_PREFIXES`) -> its marker; a test file ->
    that file alone; anything under `engine/season/` (the season loop and its data; its test helpers too) -> the
    season loop; prose -> nothing; everything else (dice engine, substrate, exporters, registries, tools) reaches
    every suite and is wide."""
    markers, season, tests, wide, prose = set(), False, [], [], []
    for f in files:
        hit = next((m for p, m in SOURCE_PREFIXES.items() if f.startswith(p)), None)
        if hit:
            markers.add(hit)
        elif _is_test_file(f) and (f.startswith(SEASON_TESTS) or f.startswith("tests/valoria/") or f.startswith("engine/tests/")):
            tests.append(f)
        elif f.startswith(SEASON_PREFIX):
            season = True
        elif f.endswith(PROSE_SUFFIXES):
            prose.append(f)
        else:
            wide.append(f)
    return sorted(markers), season, sorted(tests), wide, prose


def _valoria_files_that_run_the_season():
    """The `tests/valoria` files that import or name `engine.season`: the only ones a season-loop edit can reach (the
    combat and mass-battle files there execute `modules/` and the dice engine and nothing in `engine/season/`,
    `conftest.py`'s measurement of 2026-11-04). Found by grep at call time, so a new file is picked up."""
    out = []
    d = os.path.join(ROOT, "tests", "valoria")
    for name in sorted(os.listdir(d)):
        if name.startswith("test_") and name.endswith(".py"):
            with open(os.path.join(d, name), errors="ignore") as fh:
                if "engine.season" in fh.read():
                    out.append(f"tests/valoria/{name}")
    return out


def commands(markers, season, tests, wide):
    # `--durations=30` is the reading a `--timeout=<budget>` is a multiple of; the budget itself is a reading, not a
    # constant, so the caller adds `--timeout` (`.claude/commands/close.md` step 4).
    if wide:
        return [f"python -m pytest {' '.join(TREES[:1])} -q -n auto --durations=30",
                "python -m pytest engine/season/tests -q -n auto --dist worksteal --durations=30",
                "python -m pytest engine/tests -q --durations=30"]
    cmds = []
    if season:
        # A season-loop edit: the season suite and the `tests/valoria` files that run it. Not the subsystem suites.
        cmds.append("python -m pytest engine/season/tests " + " ".join(_valoria_files_that_run_the_season())
                    + " -q -n auto --dist worksteal --durations=30")
        tests = [t for t in tests if not t.startswith(SEASON_TESTS)]
    cmds += [f"python -m pytest {' '.join(TREES)} -m {m} -q -n auto --dist worksteal --durations=30" for m in markers]
    if tests:
        cmds.append("python -m pytest " + " ".join(tests) + " -q --durations=30")
    return cmds


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--base", default="origin/main")
    ap.add_argument("--run", action="store_true",
                    help="run every command and report each one's verdict (exit 1 if any is red)")
    a = ap.parse_args(argv)
    files = changed_files(a.base)
    markers, season, tests, wide, prose = classify(files)
    print(f"changed files: {len(files)}  | subsystems touched: {markers or 'none'}  | season loop: "
          f"{'yes' if season else 'no'}  | test files: {len(tests)}  | wide: {len(wide)}  | prose only: {len(prose)}")
    if wide:
        print("no narrowing, because of: " + ", ".join(wide[:6]) + (" ..." if len(wide) > 6 else ""))
    cmds = commands(markers, season, tests, wide)
    if not cmds:
        print("nothing to run beyond the validators (`python tools/valoria_local.py --staged`).")
        return 0
    for c in cmds:
        print("  " + c)
    if a.run:
        # Every tree runs and reports, so a red in the first does not hide the others' verdicts.
        verdicts = [(c, subprocess.run(c.split(), cwd=ROOT).returncode) for c in cmds]
        for c, rc in verdicts:
            print(("green        " if rc == 0 else f"RED (exit {rc})  ") + c)
        return 1 if any(rc for _, rc in verdicts) else 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
