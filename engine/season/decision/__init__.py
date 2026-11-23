"""`season.decision` -- AX-2's island: what a PERSON forms, wants and can afford, with no
`World` in scope. **A PACKAGE, and `04_CODE_ARCHITECTURE.md` §E.1 is why:** *"`decision/` is a
directory from its first commit. The isolation scan matches by path, so a `choose` drafted inside
`loop/` and moved later would have been green while violating AX-2."* A single file cannot be
scanned by path, so the directory is the enforcement mechanism and not a filing preference.

THE FOUR MEMBERS, per §A.2 (the `decision/` row) -- *"`decision/` AX-2's island: questions · opening_set · choose ·
budget.   NO World in scope."*

    questions.py   assemble · aggregate_questions · view_ids
    options.py     THE `opening_set` MEMBER -- opening_set and its operand machinery,
                   person_side_eligible, agreement, standing_of, and `project`
                   (which the `H-146` refusal gate calls; defined here so `options` never
                   imports `choose`)

⚠ `entrenchment` LEFT AT UNIT L3, to `queries/person_q.py`. It was the only one of the four symbols
`ED-IN-0206` item (2) named that `04:133` does NOT list as a `decision/` member, and it is
person-first in signature and self-declares as a person Query at its own first statement. `budget`,
`opening_set` and `assemble` stay: `04:133` names them here, so moving them would break conformance
rather than restore it.
    choose.py      make_chooser · pack_scenes · make_ranker · release
                   (`align` is `data.verbs.align`, `stance_toward` is `queries.person_q.stance_toward`)
    budget.py      budget · body_band_penalty
    sheet.py       v10 REM-30 (IN-47): the character sheet's spaces -- creation_sheet · seat ·
                   development_space · chronicle. NOT a fifth §A.2 member: §A.2's `decision/` row is silent on
                   a player's sheet (it names questions · opening_set · choose · budget and nothing about a
                   management space), so this is B4's third disposition, named here and picked: the sheet
                   lives under `decision/` so the AX-2 by-path scan covers it, `development_space` is
                   `choose`-shaped (it ranks and selects), and `creation_sheet` / `chronicle` are reads that
                   return records, not `Scene`s. Imported by module (`decision.sheet`), not re-exported here.

⚠ **`options.py`, NOT `opening_set.py`.** A module named for the function it exports makes
`decision.opening_set` ambiguous -- this file's re-export shadows the submodule -- and the rebind
surface below needs the MODULE by name. *Option set* is the tree's own phrase for what the function
returns, so the name is idiomatic rather than coined (`CLAUDE.md` §4).

⚠ **`belief_contradicts` IS NOT RE-EXPORTED HERE, AND `ALIGNMENT` IS NOT BOUND IN THIS PACKAGE AT
ALL -- THAT IS THE WHOLE OF THE REBIND CONTRACT.** Each is read BY BARE NAME inside a body -- `align`
(in `data/verbs.py`) reads the first, `opening_set` the second -- and a bare name resolves in its own
module's globals. So a test or a sweep arm that wants to substitute one must name the module the
reader lives in:

    data.verbs.ALIGNMENT                   (align reads it -- choose's score and the H-146 gate)
    decision.choose.pack_scenes            (make_chooser calls it)
    decision.options.belief_contradicts    (opening_set reads it)

Re-exporting either from here would let a reader rebind THIS namespace and silently miss the
reader, because a rebound value re-exported is a stale snapshot. The
suite and `engine/reference/degree-sweep/sweep_core.py` (moved from `proposals/2026-09-04-degree-sweep/`)
name the owning modules for this
reason; a rebind that reaches the wrong namespace does not fail loudly, it reports every branch
identical, which is the fabricated null `CLAUDE.md` §0.1 pt 4 calls the worse direction.

§A.2's typing of the module (`ED-IN-0206`) governs: *owns nothing, returns `Scene[]`, may read `PersonInterior`, `View`,
`Sensation`, `budget`, `Question[]` and the table's declarations.*
"""


# ---------------------------------------------------------------------------
# THE PACKAGE SURFACE. Every public name the rest of the tree imports from `..decision`, re-exported
# from its owning member so no importer has to know which file holds what. `ALIGNMENT` and
# `belief_contradicts` are deliberately ABSENT -- see the module docstring.
# ---------------------------------------------------------------------------
from .budget import body_band_penalty, budget
from .choose import make_chooser, pack_scenes
from .options import (
    agreement, containing_rung_of, operand_bags, operands_for, opening_set, project,
    person_side_eligible, standing_of, store_kind_of,
)
from .questions import aggregate_questions, assemble, view_ids

# ⚠ `__all__` IS DERIVED, NOT LISTED, AND JORDAN'S OWN GUARD IS WHY.
# `test_jordan_no_definition_is_hardcoded_in_a_body` (retired) reads a written-out list
# as a literal roster in a model module (Jordan, 2026-09-02: definitions are not hardcoded),
# and the fix is to derive rather than to claim a `roster-exempt:` -- an exemption is counted against
# a ceiling that "needs an argument, not a bump", and there is no argument here because the set is
# computable. The predicate is the one thing that makes the two DELIBERATE omissions structural
# instead of remembered: a name is in the surface only if it was DEFINED in a member of this
# package. `ALIGNMENT` is a dict with no `__module__` and `belief_contradicts` carries
# `engine.season.epistemic`, so neither can be re-exported here by accident.
# Prefix-matched, so a further split cannot narrow it.
__all__ = sorted(
    _n for _n, _v in list(globals().items())
    if not _n.startswith("_") and getattr(_v, "__module__", "").startswith(__name__)
)
