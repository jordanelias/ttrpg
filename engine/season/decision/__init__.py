"""`season.decision` -- AX-2's island: what a PERSON forms, wants and can afford, with no
`World` in scope. **A PACKAGE, and `04_CODE_ARCHITECTURE.md:1046` is why:** *"`decision/` is a
directory from its first commit. The isolation scan matches by path, so a `choose` drafted inside
`loop/` and moved later would have been green while violating AX-2."* A single file cannot be
scanned by path, so the directory is the enforcement mechanism and not a filing preference.

THE FOUR MEMBERS, per §A.2:133 -- *"`decision/` AX-2's island: questions · opening_set · choose ·
budget.   NO World in scope."*

    questions.py   assemble · aggregate_questions · view_ids
    options.py     THE `opening_set` MEMBER -- opening_set and its operand machinery,
                   person_side_eligible, agreement, standing_of, entrenchment
    choose.py      make_chooser · align · stance_toward · urgency · pack_scenes
    budget.py      budget · body_band_penalty

⚠ **`options.py`, NOT `opening_set.py`.** A module named for the function it exports makes
`decision.opening_set` ambiguous -- this file's re-export shadows the submodule -- and the rebind
surface below needs the MODULE by name. *Option set* is the tree's own phrase for what the function
returns, so the name is idiomatic rather than coined (`CLAUDE.md` §4).

⚠ **TWO NAMES ARE NOT RE-EXPORTED HERE, AND THAT IS THE WHOLE OF THE REBIND CONTRACT.** `ALIGNMENT`
and `belief_contradicts` are read BY BARE NAME inside a body -- `align` reads the first,
`opening_set` the second -- and a bare name resolves in its own module's globals. So a test or a
sweep arm that wants to substitute one must name the module the reader lives in:

    decision.choose.ALIGNMENT              (align reads it)
    decision.choose.pack_scenes            (make_chooser calls it)
    decision.options.belief_contradicts    (opening_set reads it)

Re-exporting either from here would let a reader rebind THIS namespace and silently miss the
reader -- step 8's `_LADDER` lesson, where a rebound value re-exported is a stale snapshot. The
suite and `proposals/2026-09-04-degree-sweep/sweep_core.py` name the owning modules for this
reason; a rebind that reaches the wrong namespace does not fail loudly, it reports every branch
identical, which is the fabricated null `CLAUDE.md` §0.1 pt 4 calls the worse direction.

HISTORY, corrected rather than carried. This module was extracted as a FLAT `decision.py` at step
7 of the decomposition (ED-IN-0203) on the strength of two claims that were already superseded on
`main`: *"Layer 10, precedent `epistemic.py`"* -- `epistemic` is not one of §A.2's nine, so it is
no precedent for a placement -- and a closing paragraph promising that `shape.py`'s re-export block
would keep `S.<name>` resolving. `shape.py` was deleted at step 10 and that paragraph was dead the
day it shipped. The gap between this package and Layer 1 is filed as **ED-IN-0206**; this split is
unit **L1** of `workplans/2026-09-09-layer1-conformance-plan.md`. §A.2's typing of the module is
unchanged and still governs: *owns nothing, returns `Scene[]`, may read `PersonInterior`, `View`,
`Sensation`, `budget`, `Question[]` and the table's declarations.*
"""


# ⚠ TWO DEVIATIONS FROM THE DECOMPOSITION PLAN'S DECLARED IMPORT LIST, BOTH FOUND BY THE AST
# VERIFICATION THE PLAN ITSELF DEMANDED, NEITHER A JUDGMENT CALL:
#
# 1. `ELIGIBILITY_KINDS` IS IN `.data.verbs`, NOT `.data.rosters` -- the plan named the wrong
#    owner. `person_side_eligible()` reads it (`if kind not in ELIGIBILITY_KINDS`), and importing
#    it from `.data.rosters` as written raises `ImportError` at module load, immediately, for
#    every caller -- the loud failure mode, not the step-5 kind that hides until a byte-compare.
#    Verified against the actual definition site, which is `engine/season/data/verbs.py`'s
#    `ELIGIBILITY_KINDS = roster("eligibility_kinds")` -- located by `rg -n "^ELIGIBILITY_KINDS"`
#    and deliberately cited WITHOUT a line number, because the first draft of this comment said
#    `:55` and the assignment is at `:68`, in a file this same commit edits (CLAUDE.md §3: "a LINE
#    citation into a file being decomposed is wrong twice over"). It is *sourced* from the rosters file's
#    `eligibility_kinds` table but the module-level NAME lives in `verbs`, because `verbs.py` is
#    what checks a verb row's `eligible:` cell against it.
#
# 2. `Claim` IS ADDED to `.state.carriers`, absent from the plan's list. `agreement()`'s signature
#    reads `list[Claim]` twice, bare (not a forward-ref string) -- the same AST pass that confirmed
#    every other name below is needed found this one unimported. This is the step-5 `Forbidden`
#    lesson again: an annotation-only reference is still a reference, and `from __future__ import
#    annotations` makes a missing one a silent hole rather than an `ImportError`, since nothing in
#    this tree currently calls `typing.get_type_hints` on a season module. Fixed anyway rather than
#    left as a known dangling annotation.
#
# `Fixtures` and `VerbRow` are the converse case and are DELIBERATELY absent (the plan is right to
# omit them): every occurrence of either in the moved bodies is a QUOTED forward-reference string
# (`"Fixtures"`, `"VerbRow"`), never a bare name, never constructed, never the subject of
# `isinstance`. That is the same quoting the moved bodies used even inside `shape.py`, where both
# names WERE already resolvable -- so the quoting was never about deferred resolution, it is how
# this file's original author marked "an opaque handle whose class identity this function does not
# need". Importing them here would add two names AST proves are dead weight.

# ---------------------------------------------------------------------------
# THE PACKAGE SURFACE. Every public name the rest of the tree imports from `..decision`, re-exported
# from its owning member so no importer has to know which file holds what. `ALIGNMENT` and
# `belief_contradicts` are deliberately ABSENT -- see the module docstring.
# ---------------------------------------------------------------------------
from .budget import body_band_penalty, budget
from .choose import align, make_chooser, pack_scenes, stance_toward, urgency
from .options import (
    agreement, containing_rung_of, entrenchment, operands_for, opening_set,
    person_side_eligible, standing_of, store_kind_of,
)
from .questions import aggregate_questions, assemble, view_ids

# ⚠ `__all__` IS DERIVED, NOT LISTED, AND JORDAN'S OWN GUARD IS WHY. A first version of this file
# wrote the eighteen names out; `test_jordan_no_definition_is_hardcoded_in_a_body` correctly read
# that as a literal roster in a model module (Jordan, 2026-09-02: definitions are not hardcoded),
# and the fix is to derive rather than to claim a `roster-exempt:` -- an exemption is counted against
# a ceiling that "needs an argument, not a bump", and there is no argument here because the set is
# computable. The predicate is the one thing that makes the two DELIBERATE omissions structural
# instead of remembered: a name is in the surface only if it was DEFINED in a member of this
# package. `ALIGNMENT` is a dict with no `__module__` and `belief_contradicts` carries
# `engine.season.epistemic`, so neither can be re-exported here by accident -- which is exactly the
# `_LADDER` property step 8 had to hold by hand. Prefix-matched, so a further split cannot narrow it.
__all__ = sorted(
    _n for _n, _v in list(globals().items())
    if not _n.startswith("_") and getattr(_v, "__module__", "").startswith(__name__)
)
