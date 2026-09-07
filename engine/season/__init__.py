"""`engine.season` — the season loop, as a package. The adopted game code (ED-IN-0202, Jordan
2026-09-05, *"adopt in full"*), decomposed into modules (ED-IN-0203).

⚠ NO `sys.path` INSERT HERE, AND THE ABSENCE IS THE POINT — THIS FILE USED TO BE ONE. At adoption
the modules imported each other by BARE NAME (`import shape`, `import probes`), a flat convention
carried in from the instrument they came from, and this file inserted its own directory to make
that work under `tests/valoria/test_engine_does_not_import_systems.py`, which walks every
`engine/**/*.py` and imports it by dotted path. That insert bought a real repair and charged a real
price, which the file it replaced named honestly: a module could be reached as `shape` AND as
`engine.season.shape`, two module objects with two sets of module-level state in one process — the
same second-identity hazard `CLAUDE.md` §3 records for `combat_engine_v1`.

The decomposition pays that price off rather than carrying it. Every import inside this package is
now relative, so there is exactly one identity per module and no path repair to perform. A package
that repairs its own import path works from anywhere and therefore hides where it is being imported
from; the `sys.path` mutations that remain are DECLARED SEAMS reaching OUT of this package — the
flat personal-combat module set, the repo root for `engine.autoload`, the degree sweep — each
inside a function body, each with its reason at the site.

Entry points are modules, not scripts:

    python -m engine.season.harness.headless --case NPC-088 --seasons 2 --seed 0
    python -m engine.season.harness.run_cases
    python -m engine.season.harness.report      # the SOLE emitter of runs/ (W15, guardrail G7)
    python -m engine.season.harness.corpus_run
    python -m engine.season.harness.register --counts
    python -m engine.season.harness.delta HEAD

⚠ `report` BEFORE `delta`, ALWAYS. `delta` compares a committed revision's `runs/results.json`
against the WORKING TREE's copy and regenerates nothing, so running it alone compares a file with
itself and prints `PROBE FLIPS 0` no matter what changed. That number was quoted as a control in
five commit messages before an independent verifier caught it.

Every path this package derives is named once in `engine.season.data.files`, the only module here
allowed to anchor itself on its own module location. That is checkable rather than aspirational:
grepping the dunder-file spelling across `engine/season/` must print exactly that one file.
"""
