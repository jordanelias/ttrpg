"""`season` — the season-loop tracer, as a package.

⚠ NO `sys.path` INSERT HERE, DELIBERATELY. A package that repairs its own import path works from
anywhere and therefore hides where it is being imported from; the four `sys.path` mutations this
package still performs are DECLARED SEAMS reaching OUT of it (the flat personal-combat module set,
the repo root for `engine.autoload`, the degree sweep), each inside a function body and each with
its reason at the site. Import this package the ordinary way, with
`proposals/2026-09-01-season-loop-tests/` on the path -- which is what pytest's rootdir insertion
and `python -m season.harness.<name>` both already do.

Entry points are modules, not scripts:

    python -m season.harness.headless --case NPC-088 --seasons 2 --seed 0
    python -m season.harness.run_cases
    python -m season.harness.report          # the SOLE emitter of runs/ (W15, guardrail G7)
    python -m season.harness.corpus_run
    python -m season.harness.register --counts
    python -m season.harness.delta HEAD

Every path the package derives is named once in `season.data.files`, which is the only module here
allowed to anchor itself on its own module location. That is checkable rather than aspirational:
`grep -rln "__f" + "ile__" season/` must print exactly that one file.
"""
