#!/usr/bin/env python3
"""SessionStart hook: install the test dependencies CLAUDE.md §8 documents, and SAY NOTHING.

TERM, defined at the call site (CLAUDE.md §4): **provision** means "make the container able to
run the gates this repo already documents". It is not orientation, not a status report, and not a
banner. The distinction is load-bearing, because §0.3 retired the SessionStart *banner* — a
GENERATED CONTEXT SURFACE that defined a session's work — and that ban was then read as a ban on
the hook KEY. The two are different objects: a banner spends context and steers a session; this
writes zero bytes to stdout and steers nothing. Re-adding a hook that PRINTS is the T1 regression
§0.3 names; this one is silent by construction, which is why it is allowed to exist.

WHY IT EARNS ITS PLACE: §0.4 makes `python -m pytest tests/valoria -q -n auto` the close step of
every commit, and §8 documents `pip install pyyaml pytest numpy pytest-xdist` as the one-time
setup. A fresh remote container has pyyaml only. So the documented close gate was unrunnable on
arrival, and a session either skipped its own shipping gate or spent its first minutes on pip.
MEASURED 2026-09-18 on this container: pytest, numpy and pytest-xdist all absent.

This is NOT a guard and not apparatus under §0.1 pt 5 — it asserts nothing, gates nothing and has
no verdict. It installs up to four packages, or does nothing.
"""
import importlib.util
import subprocess
import sys

# import name -> pip name. Exactly the set CLAUDE.md §8 documents; keep the two in step.
REQUIRED = {
    'yaml': 'pyyaml',
    'pytest': 'pytest',
    'numpy': 'numpy',
    'xdist': 'pytest-xdist',   # `-n auto`, which is what CI runs and what §0.4 measures
}


def missing():
    return [pip for mod, pip in REQUIRED.items() if importlib.util.find_spec(mod) is None]


def main():
    need = missing()
    if not need:
        return 0
    try:
        subprocess.run(
            [sys.executable, '-m', 'pip', 'install', '--quiet',
             '--disable-pip-version-check', *need],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=300, check=False)
    except Exception:
        # A container with no network, an absent pip, a proxy that refuses: none of these are the
        # session's problem to announce at startup. The close gate fails loudly and honestly if
        # the deps are still missing, which is the right place to find out.
        pass
    return 0


if __name__ == '__main__':
    # Never print, never fail: stdout from a SessionStart hook enters the session's context (that
    # is what made the old banner expensive) and a nonzero exit blocks the session.
    sys.exit(main())
