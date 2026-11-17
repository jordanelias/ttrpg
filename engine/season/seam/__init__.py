"""`season.seam` -- THE CONTEST SEAM. **A PACKAGE, per `04_CODE_ARCHITECTURE.md` §A.2 (`04:135`):
`seam/  contest() · ladder · one wrapper per deferred subsystem`**, and the §A.2 table gives each of
the three its own row: `seam/contest` dispatches and returns Events + degree or a typed refusal,
`seam/ladder` owns nothing and answers `degree(margin, veto?) -> Degree`, and `seam/wrappers/*`
own *"nothing, ever"* and return a `Margin`.

    contest.py            contest() · grade() · find_trail() · contest_subsystem() · ContestError · ContestRefused · Resolution
    ladder.py             degree_of() · combat_degree() · party_degree() · degree_ladder() · ladder_error()
    wrappers/combat.py    the IN-side of the personal-combat call
    wrappers/fieldwork.py the `inquiry` role's provider (v9 FI-02 + FI-03), called by find_trail()

⚠ **`_LADDER` IS NOT RE-EXPORTED HERE.** `degree_ladder()` reads it as `ladder`'s own global, so a name
bound in this namespace would be a snapshot that goes stale the moment a test swaps the ladder. A caller
that reads or writes the raw attribute -- a test swapping the ladder -- must name **`seam.ladder._LADDER`**.
The readers `degree_ladder()`,
`ladder_error()` and `degree_of()`, ARE re-exported and work from here: a function is one object regardless
of which module holds a name pointing at it, so `seam.degree_ladder()` runs the same code and reads
`ladder`'s own globals.

⚠ **THE PERSONAL-COMBAT WRAPPER IS `seam/wrappers/combat.py`; it reaches `modules/combat` by the composition rows
`combat.fight` and `combat.duel_terms` only.** `PATH_SEAM_ALLOWED` is empty (CI-09) and stays so: a `sys.path`
insert here naming a code root is a new seam, and `04` §E.1's by-path scan is the enforcement mechanism for AX-2.
`04` §A.2's adapter row puts a wrapper under `wrappers/`.

Governed by **ED-IN-0206**.
"""

# ---------------------------------------------------------------------------
# THE PACKAGE SURFACE. Everything the fold, the harness and the suite import from `..seam`,
# re-exported from its owning member -- EXCEPT `_LADDER`, per the docstring.
# `dir(seam)` must keep containing `contest`: `harness/probes.py`'s A17 probe asks this surface
# whether the loop has one resolver, and a package that hid it would make that probe read PASS over
# an empty list.
# ---------------------------------------------------------------------------
# ⚠⚠ **IMPORTING `wrappers` IS WHAT REGISTERS THE PROVIDERS, AND LEAVING IT OUT IS A SILENT
# WRONG ANSWER RATHER THAN AN ERROR.** The wrapper modules carry `@provider(role, module)`; nothing
# runs those decorators unless the package is imported.
# `manifest.check_contest_prizes()` refuses an unregistered prize provider at `SeasonDriver`
# construction, naming the prize. The import is what fills the table.
# `tests/valoria/test_season_providers_are_registered.py` is the falsifier.
from . import wrappers as _wrappers   # noqa: F401
from .contest import (ContestError, ContestRefused, Resolution, contest, contest_subsystem,
                      find_trail, grade)
from .ladder import combat_degree, degree_ladder, degree_of, ladder_error, party_degree

# ⚠ DERIVED, NOT LISTED -- Jordan 2026-09-02, definitions are not hardcoded, and
# `test_jordan_no_definition_is_hardcoded_in_a_body` reads a written-out name list in a model module
# as a literal roster. The predicate keeps only what a member DEFINED, which is what makes the
# exclusion structural rather than remembered: `_LADDER` is a tuple with no `__module__` and would
# be excluded even if the underscore rule were dropped.
__all__ = sorted(
    _n for _n, _v in list(globals().items())
    if not _n.startswith("_") and getattr(_v, "__module__", "").startswith(__name__)
)
