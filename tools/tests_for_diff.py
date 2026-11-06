#!/usr/bin/env python3
"""tests_for_diff.py -- which test suites a session's edits call for, and (with --run) run them.

An INNER-LOOP ACCELERATOR, not a gate: CI runs everything and is the full-suite tier (`CLAUDE.md` section 8).
It reads the files this session changed (committed since the branch left `origin/main`, staged, unstaged,
untracked) and prints the narrowest honest command:

  * every changed file is inside one subsystem (`modules/<s>/`, `systems/<s>/`, or a test file whose name the
    root `conftest.py` assigns to <s>)  ->  `pytest -m <s>` over all three test trees, for each subsystem touched;
  * a changed file outside every subsystem (engine/season/, engine/dice_engine/, engine/substrate/, tools/, the
    registries ...)  ->  no narrowing: it prints the full-gate commands of `CLAUDE.md` section 0.4;
  * only prose changed (.md and the like)  ->  nothing to run beyond the validators.

WHAT THE NARROW ANSWER DOES NOT COVER, said here because it is the cost of skipping: the season suite builds a whole
realm, so its tests execute the combat, mass-battle and contest modules too (measured 2026-11-04: a `modules/combat/`
edit is reached by tests costing about three quarters of the suite). A subsystem edit that changes what a realm
does shows up there, and in the realm-hash goldens, only when the full season suite runs; with this tool that is
CI's run. If your edit could change a realm (a module's output the season loop reads), run the season suite as well.

Usage:  python tools/tests_for_diff.py [--base REF] [--run]
"""
import argparse
import importlib.util
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


def _conftest():
    spec = importlib.util.spec_from_file_location("valoria_root_conftest", os.path.join(ROOT, "conftest.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def classify(files):
    """-> (markers touched, files that forbid narrowing, prose-only files)."""
    patterns = _conftest().SUBSYSTEM_FILES
    markers, wide, prose = set(), [], []
    for f in files:
        hit = next((m for p, m in SOURCE_PREFIXES.items() if f.startswith(p)), None)
        if hit is None and "/test_" in f and f.endswith(".py"):
            base = os.path.basename(f)[:-3]
            hit = next((m for m, pat in patterns.items() if pat.match(base)), None)
        if hit:
            markers.add(hit)
        elif f.endswith(PROSE_SUFFIXES):
            prose.append(f)
        else:
            wide.append(f)
    return sorted(markers), wide, prose


def commands(markers, wide):
    if wide:
        return [f"python -m pytest {' '.join(TREES[:1])} -q -n auto",
                "python -m pytest engine/season/tests -q -n auto --dist worksteal",
                "python -m pytest engine/tests -q"]
    return [f"python -m pytest {' '.join(TREES)} -m {m} -q -n auto --dist worksteal" for m in markers]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--base", default="origin/main")
    ap.add_argument("--run", action="store_true", help="run the commands (stops at the first failure)")
    a = ap.parse_args(argv)
    files = changed_files(a.base)
    markers, wide, prose = classify(files)
    print(f"changed files: {len(files)}  | subsystems touched: {markers or 'none'}  | outside every subsystem: "
          f"{len(wide)}  | prose only: {len(prose)}")
    if wide:
        print("no narrowing, because of: " + ", ".join(wide[:6]) + (" ..." if len(wide) > 6 else ""))
    cmds = commands(markers, wide)
    if not cmds:
        print("nothing to run beyond the validators (`python tools/valoria_local.py --staged`).")
        return 0
    for c in cmds:
        print("  " + c)
    if a.run:
        for c in cmds:
            if subprocess.run(c.split(), cwd=ROOT).returncode:
                return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
