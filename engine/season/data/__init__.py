"""`season.data` — where the package's inputs are resolved.

`files` is the single path anchor for the whole package (see `files.py`). `rosters` and `matrix`
are the loaders that read those paths; `shape.py` imports them directly, and `matrix` imports
`rosters.load_yaml`, so the load order is fixed by the data dependency and needs no help here.

⚠ THIS MODULE DELIBERATELY DOES NOT IMPORT THE LOADERS. It did, for one commit, to make the
sentence "importing `season.data` loads every registry" true. Two independent adversarial passes
found what that cost, and the second MEASURED it:

  * Seven modules import `files` for PATHS ONLY — `harness/{delta,register,report,corpus_run,
    exercises,run_cases}.py` and `seam/wrappers/combat.py`. Eager loading made every one of them parse two
    YAML registries at import and able to `SystemExit`. `delta.py` is a git+JSON differ. And
    `seam/wrappers/combat.py` exists to DEGRADE to a named gap, which an exit at import defeats.
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

WHAT "ONE ENTRY" IS, SINCE v9 SC-02 `23`: `load_all()` below -- a CALL, not an import, so the seven
path-only importers above keep importing `files` for paths and nothing else. It discovers every module
in this package (`pkgutil`, never a list: `files.py`'s own lesson, `package_modules`), imports each, and
calls the `load()` a lazy loader exports (`goals`, `geography`, `cast`) so its file is read NOW. A
loader's refusal -- a `SystemExit` naming its row -- is therefore reachable from one place, and
`loop/driver.py::SeasonDriver.__init__`, the one place every run passes, makes that call first.
"""

from . import files  # noqa: F401  -- the anchor, and its import-time self-check


def load_all() -> tuple:
    """THE ONE ENTRY TO THE `data/` LOADERS: import every module of this package, force each lazy file,
    and return the names loaded, in import order. Idempotent -- a module imports once and a lazy loader
    keeps its cache -- so calling it from every driver construction costs one directory listing
    (`pkgutil.iter_modules`) and a dict lookup per module; no measurement is claimed beyond that.

    A loader that fails raises ITS OWN refusal naming its row (`SystemExit` at import for the table
    loaders, `Unspecified` for a missing lazy file); nothing here catches, wraps or reorders it.
    `files` is skipped (paths only, loaded already). Discovery is by `pkgutil`, so a loader added tomorrow
    is reached by existing; a caller that scans the result must also pin a FLOOR on its length
    (`CLAUDE.md` §0.1 pt 2) -- a discovery that stops matching passes by finding nothing."""
    import importlib
    import pkgutil
    loaded = []
    for info in sorted(pkgutil.iter_modules(__path__), key=lambda i: i.name):
        if info.name == "files":
            continue
        mod = importlib.import_module(f"{__name__}.{info.name}")
        force = getattr(mod, "load", None)
        if callable(force):
            force()
        loaded.append(info.name)
    return tuple(loaded)
