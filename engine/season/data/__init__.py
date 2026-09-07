"""`season.data` — where the package's inputs are resolved.

`files` is the single path anchor for the whole package (see `files.py`). `rosters` and `matrix`
are the loaders that read those paths; `shape.py` imports them directly, and `matrix` imports
`rosters.load_yaml`, so the load order is fixed by the data dependency and needs no help here.

⚠ THIS MODULE DELIBERATELY DOES NOT IMPORT THE LOADERS. It did, for one commit, to make the
sentence "importing `season.data` loads every registry" true. Two independent adversarial passes
found what that cost, and the second MEASURED it:

  * Seven modules import `files` for PATHS ONLY — `harness/{delta,register,report,corpus_run,
    exercises,run_cases}.py` and `combat_seam.py`. Eager loading made every one of them parse two
    YAML registries at import and able to `SystemExit`. `delta.py` is a git+JSON differ. And
    `combat_seam.py` exists to DEGRADE to a named gap, which an exit at import defeats.
  * It removed the loaders' last external patch point, silently and FAIL-OPEN. Before:
    setting `files.WRITE_MATRIX_YAML` to a bad path then importing raised
    `SystemExit: write_matrix.yaml not found at ...`. After: the import succeeded and read the
    REAL file, because `matrix` had already bound the name at its own scope. The idiom this test
    suite already uses (`mock.patch.object(S, "VERB_TABLE_YAML")`) would have silently done
    nothing and PASSED.

To exercise a loader's path resolution, patch the module that READS it — `matrix.WRITE_MATRIX_YAML`
or `rosters.ROSTERS_YAML` — and re-call its loader. That is the only patch point, and it works.

The "ONE loader" of `04_CODE_ARCHITECTURE.md:131` is NOT satisfied by an import shim, and this
module no longer claims it is: that doctrine names twelve cross-registry validations (§B.13), and
they live in the loaders themselves, where they still fire.
"""

from . import files  # noqa: F401  -- the anchor, and its import-time self-check
