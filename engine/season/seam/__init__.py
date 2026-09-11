"""`season.seam` -- THE CONTEST SEAM. **A PACKAGE, per `04_CODE_ARCHITECTURE.md` §A.2 (`04:135`):
`seam/  contest() · ladder · one wrapper per deferred subsystem`**, and the §A.2 table gives each of
the three its own row: `seam/contest` dispatches and returns Events + degree or a typed refusal,
`seam/ladder` owns nothing and answers `degree(margin, veto?) -> Degree`, and `seam/wrappers/*`
own *"nothing, ever"* and return a `Margin`.

    contest.py            contest() · contest_subsystem() · ContestError · Resolution
    ladder.py             degree_of() · combat_degree() · degree_ladder() · ladder_error()
    wrappers/combat.py    the IN-side of the personal-combat call

⚠ **`_LADDER` AND `_LADDER_ERROR` ARE NOT RE-EXPORTED HERE.** `degree_ladder()` rebinds both through
`global`, so a name bound in this namespace would be a snapshot that is permanently stale the moment
the first call fires. A caller that reads or writes the raw attribute -- a test swapping the ladder
-- must name **`seam.ladder._LADDER`**. Step 8 established this for the flat module and it holds one
directory down. The two non-rebinding readers, `ladder_error()` and `degree_of()`, ARE re-exported
and work from here: a function is one object regardless of which module holds a name pointing at it,
so `seam.ladder_error()` runs the same code and reads `ladder`'s own globals.

⚠ **`combat_seam.py` MOVED, AND THE CLAIM THAT IT WOULD NOT IS THE DEFECT THIS UNIT REPAIRS.** The
flat `seam.py`'s docstring said it *"does NOT move here and is not renamed ... per
`PATH_SEAM_ALLOWED`"*, inheriting that premise from
`workplans/2026-09-09-shape-decomposition-plan-v2.md` §3. That is the R-execution plan's **D5
inverted** -- the cost read as the reason. D5 prices the same edit as *"a rename inside a
shrink-only set, not a widening"*, and it was on `main` five hours before step 8 merged. The wrapper
is `seam/wrappers/combat.py` now, with the `PATH_SEAM_ALLOWED` member and `files.COMBAT_SEAM_PY`
renamed in the same commit. **The yield is not zero, which is why the premise was wrong twice
over:** `04:1046`'s by-path scan is the enforcement mechanism for AX-2, and `04:135` puts a wrapper
under `wrappers/`; a flat file at the package root cannot be either.

⚠ **AND THE SET MUST NOT LOSE A MEMBER EITHER.**
`test_engine_does_not_import_systems.py`'s `_relative_module_files` follows **relative imports only**
-- it skips any `ImportFrom` with `level == 0`. Write the wrapper's imports absolute and the scan
stops seeing the seam at all: `offenders` shrinks and the exact-equality assertion reddens with a
message inviting deletion of the entry. The repair for that is restoring the relative import, never
deleting the declaration.

Filed as **ED-IN-0206**; this is unit **L2** of
`workplans/2026-09-09-layer1-conformance-plan.md`.
"""

# ---------------------------------------------------------------------------
# THE PACKAGE SURFACE. Everything the fold, the harness and the suite import from `..seam`,
# re-exported from its owning member -- EXCEPT `_LADDER` and `_LADDER_ERROR`, per the docstring.
# `dir(seam)` must keep containing `contest`: `harness/probes.py`'s A17 probe asks this surface
# whether the loop has one resolver, and a package that hid it would make that probe read PASS over
# an empty list.
# ---------------------------------------------------------------------------
# ⚠⚠ **IMPORTING `wrappers` IS WHAT REGISTERS THE PROVIDERS, AND LEAVING IT OUT IS A SILENT
# WRONG ANSWER RATHER THAN AN ERROR.** The wrapper modules carry `@provider(role, module)`; nothing
# runs those decorators unless the package is imported. `manifest.has(...)` then answers False,
# `resolvable_verbs()`'s third gate drops every contesting verb, and the season runs a smaller verb
# set with no exception anywhere. MEASURED while making this cut: with the import missing,
# `resolvable_verbs()` returned 17 instead of 18 and `tell` executed ZERO times in `tiny_world`
# where it had executed 32 — no error, no refusal, no `news.untold`, just a verb quietly gone.
# `tests/valoria/test_season_providers_are_registered.py` is the falsifier.
from . import wrappers as _wrappers   # noqa: F401
from .contest import ContestError, Resolution, contest, contest_subsystem
from .ladder import combat_degree, degree_ladder, degree_of, ladder_error

# ⚠ DERIVED, NOT LISTED -- Jordan 2026-09-02, definitions are not hardcoded, and
# `test_jordan_no_definition_is_hardcoded_in_a_body` reads a written-out name list in a model module
# as a literal roster. The predicate keeps only what a member DEFINED, which is what makes the two
# exclusions structural rather than remembered: `_LADDER` is a tuple with no `__module__` and would
# be excluded even if the underscore rule were dropped.
__all__ = sorted(
    _n for _n, _v in list(globals().items())
    if not _n.startswith("_") and getattr(_v, "__module__", "").startswith(__name__)
)
