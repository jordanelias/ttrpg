"""`decision/` -- the `questions` member of `04_CODE_ARCHITECTURE.md` §A.2:133.

`assemble` builds the season's `Question[]` for one person, `aggregate_questions` folds several
into the one the `QUESTION_AGGREGATION` rule selects, and `view_ids` bounds what a `View` may
carry. Moved here whole from `decision.py` by unit L1 of
`workplans/2026-09-09-layer1-conformance-plan.md`; see `__init__.py` for why the package exists
and for the import-list record this file's imports are derived from.

AX-2 binds every file under `decision/`: no `World`, as an import, a name, an attribute or a
string. Enforced BY PATH over this directory -- `04:1046` -- by
`tests/valoria`'s sibling in `engine/season/tests/test_season_shape.py`.
"""

from __future__ import annotations

from typing import Any
from ..data.rosters import QUESTION_AGGREGATION, VIEW_BUILDER_RULES
from ..gaps import InstrumentDefect, Unspecified
from ..state.carriers import Person, Question, View


def assemble(p: Person, question: Any, k: int, rule: str = "recent") -> View:
    # ⚠ W5 REMOVED A `NoProducer` HERE, AND THE REMOVAL IS THE DISCHARGE OF §61, NOT A
    # SOFTENING OF IT. It read: "`assemble(person, question)` and `view(person, question)`
    # are UNSATISFIABLE; DELIBERATE HAS NO DECLARED ENTRY POINT." That was TRUE while nothing
    # produced `q`. `questions_for()` produces it from four sources, so `question is None` no
    # longer means "the design has no producer" -- it means THIS PERSON HAS NO QUESTION THIS
    # SEASON, which is an ordinary state (a quiet season, nothing due, no standing commit) and
    # not a hole. Such a person forms no candidates and does nothing, which is correct.
    # A WRONG TYPE STILL RAISES, below: silently accepting one would let a caller's leftover
    # string sit where a Question belongs and read as "no question", which is how a discharged
    # hole comes back as a silent no-op.
    if question is not None and not isinstance(question, Question):
        # `InstrumentDefect`, not `Forbidden`: a caller passing the wrong TYPE is a bug in the
        # caller, not a hole in #353, and filing it as a GAP would put it in the column that
        # measures the design. Same lesson as `_TenureView`.
        raise InstrumentDefect(
            f"assemble() was given a {type(question).__name__}, not a Question. Pass a "
            "Question from questions_for(), or None for a person with no question this "
            "season. §F1's `q` has a producer now (`H-04`); accepting any object here would "
            "make a stale injected fixture indistinguishable from an absent question.")
    return View(p.id, view_ids(p, question, k, rule), k, question)


def aggregate_questions(qs: list, rule: str):
    """`H-54`: how many of a person's questions reach `assemble` in one season.

    #353 says NOTHING about this and the instrument answered it silently as `qs[0]` for four
    revisions. `first` preserves that answer as a declared, swept default; `all` and
    `one_per_source` are the alternatives the sweep compares it against. Returns ONE question,
    because `assemble(person, question)` takes one -- the rules differ in WHICH, and in how many
    are folded into it, which is exactly what is open."""
    if rule not in QUESTION_AGGREGATION:
        raise Unspecified(
            f"question-aggregation rule {rule!r} is not in the roster", "H-54",
            needs=f"one of {list(QUESTION_AGGREGATION)}",
            law="H-54 -- nothing in #353 says how many questions a person forms per season, so a "
                "rule outside the roster is a fourth answer nobody declared")
    if not qs:
        return None
    if rule == "first":
        return qs[0]
    if rule == "one_per_source":
        seen, keep = set(), []
        for q in qs:
            if q.source not in seen:
                seen.add(q.source); keep.append(q)
        qs = keep
    # `all` and `one_per_source` widen the REFERENTS rather than the question count, because
    # `assemble` takes one question. The person brings everything they are being asked about.
    refs = tuple(sorted({r for q in qs for r in q.referents}))
    return Question(f"q:agg:{rule}:{qs[0].id}", qs[0].source, refs, qs[0].about)


def view_ids(p: Person, q: Any, k: int, rule: str) -> list:
    """§18's "at most K claim ids from the holder's OWN ledger -- BUILT, not filtered". `H-53`.

    ⚠ #353 SUPPLIES K AND NEVER SUPPLIES WHICH K, and "built, not filtered" says what a View is
    NOT. `H-09` gives `K = 12`; nothing in the chain says which twelve of a 200-claim ledger a
    person brings to a question, and taking the last k -- which every revision before `W5` did
    silently -- is an invention. The rules are `rosters.yaml: view_builder_rules`, `recent` is the
    default because it is the incumbent and a sweep needs an honest control, NOT because it is
    argued for.

    PERSON-SIDE: it reads `p.ledger` and the question's own referents. No World."""
    if rule not in VIEW_BUILDER_RULES:
        raise Unspecified(
            f"view-builder rule {rule!r} is not in the view_builder_rules roster", "H-53",
            needs=f"one of {sorted(VIEW_BUILDER_RULES)}",
            law="§18 -- 'at most K ids ... BUILT, not filtered'. WHICH K is `H-53` and is open; "
                "a rule not on the roster is a fourth answer nobody declared")
    if rule == "highest_confidence":
        ranked = sorted(p.ledger, key=lambda c: (-c.confidence, c.id))
        return [c.id for c in ranked[:k]]
    if rule == "question_relevant":
        refs = set(getattr(q, "referents", ()) or ())
        near = [c for c in p.ledger if c.subject in refs]
        rest = [c for c in p.ledger if c.subject not in refs]
        # Relevant first, then the incumbent order for the remainder -- a person brings what the
        # question is about AND whatever else is freshest, rather than only the former.
        return [c.id for c in near[-k:]] + [c.id for c in rest[-(k - min(len(near), k)):]] \
            if k > len(near) else [c.id for c in near[-k:]]
    return [c.id for c in p.ledger][-k:]
