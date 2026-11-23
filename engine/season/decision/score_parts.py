"""`decision/score_parts.py` -- A CHOICE READ BACK AS ITS SCORE PARTS, AND WHICH OF THEM ARE HEARD (B10.54).

`score_parts` splits `choose.score_terms`' tuple into the parts that own it -- one per held pursuit, one for the stance subject, the
conferred person, the goal and the prize -- each a `ScorePart`, which the player's surface shows as a "voice". It is an OBSERVER: it calls
`score_terms` and reads `damp` from the memo `deliberation_memo` built, asks `odds_weight` and `admission_weight` once per candidate as
`score_terms` asks them, and re-derives no factor (`CLAUDE.md` §8). `heard` is the curation rule that keeps a voice rare. Nothing here steers
a choice or is stored: a `watch` (B09.13) may call both and the realm's content hash is equal.

AX-2 binds this directory: no store of the world in scope, as an import, a name, an attribute or a string. Person-side and read at the call.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Optional

from engine.dice_engine.fmath import ltr_sum
from ..data.pursuits import _AXES, to_axes   # the sorted axis order: a sum over the frozenset would add in PYTHONHASHSEED's order
from ..data.verbs import VERB_TABLE, align, align_kind
from ..queries.person_q import crisis_weights, is_deed
from ..state.carriers import Candidate, Claim, Question
from .choose import _DAMP, TERM_NAMES, admission_weight, odds_weight, score_terms

# The terms of `score_terms`' tuple that name an owner here, in the tuple's order. A term added to `score_terms` leaves this shorter than the
# tuple and `score_parts` refuses, until the new term names its owner below. `test_voices.py` ties it to `choose.TERM_NAMES`.
ATTRIBUTED_TERMS = ("pursuit", "stance", "fit", "aim", "risk")

# The share of the total's size a dissenting part must reach to be heard. A display parameter of the surface: it changes what is shown, never what is chosen.
HEARD_FLOOR = 0.5   # [canonical: proposals/2026-11-12-subsystem-audit-suite/proposals/02_CHAR_voices_and_the_room.md §Exact edits 3 ([ASSUMPTION; medium; GO and Jordan to correct])]

DRAW = "draw"       # the kind of the voice that says the person did not take his own best (`heard`)


@dataclass(frozen=True)
class ScorePart:
    """One owned part of a candidate's score, shown on the surface as a "voice".
    `kind` is a name in `ATTRIBUTED_TERMS` (or `DRAW`); `owner` the pursuit key, the subject id, the conferred person, the goal id or the prize it
    belongs to; `pull` its signed share of the score."""
    kind: str
    owner: str
    pull: float


@dataclass(frozen=True)
class Citation:
    """The history a pursuit voice cites: that pursuit's scar count and the newest deed claim in his ledger scored on its axes (`None` if none)."""
    scar: int
    claim: Optional[Claim]


def _order(part: ScorePart) -> tuple:
    return (-abs(part.pull), part.owner, part.kind)


def _pursuit_parts(p, c: Candidate, fx, memo: dict, odds: Optional[Callable], total: float) -> list:
    """`damp * Σ_axis to_axes({e: w_e})[axis] * align(c.verb, axis) * odds_weight * admission_weight` for each held pursuit `e`, `w_e` from
    `crisis_weights(p, scar_weight_shift)`, the weights `choose.project` reads. A candidate whose pursuit term is exactly 0.0 is not asked the
    two factors (nor is `score_terms`: the odds query scans the log), so its parts carry none."""
    factor_o, factor_a = (odds_weight(p, c, fx, odds), admission_weight(p, c, fx)) if total != 0.0 else (1.0, 1.0)
    weights = crisis_weights(p, fx.get("scar_weight_shift"))
    parts = []
    for e in sorted(weights):
        axes = to_axes({e: weights[e]})
        pull = memo[_DAMP] * ltr_sum(axes[ax] * align(c.verb, ax) for ax in _AXES)
        if pull != 0.0:
            parts.append(ScorePart("pursuit", e, pull * factor_o * factor_a))
    return parts


def score_parts(p, c: Candidate, fx, memo: dict, odds: Optional[Callable] = None, q: Optional[Question] = None) -> tuple:
    """Every owned part of `score_terms(p, c, fx, memo, odds, q)`, exactly once, each with a non-zero pull, sorted by |pull| descending then owner.

    The pursuit term is split by held pursuit (`_pursuit_parts`); the stance term is one part owned by `c.subject`; `fit` one owned by the
    person the row seats (`operands["to"]`); `aim` one owned by the goal the question `q` was raised by; `risk` one owned by the prize the row
    contests. The parts sum to `score_total` of the terms within summation reorder."""
    terms = score_terms(p, c, fx, memo, odds, q)
    if len(terms) != len(ATTRIBUTED_TERMS) or TERM_NAMES != ATTRIBUTED_TERMS:
        raise ValueError(f"score_terms returns {TERM_NAMES}, but only {ATTRIBUTED_TERMS} name an owner: a new term must name its owner here")
    by = dict(zip(TERM_NAMES, terms))
    row = VERB_TABLE.get(c.verb)
    parts = _pursuit_parts(p, c, fx, memo, odds, by["pursuit"])
    for kind, owner in (("stance", c.subject or ""), ("fit", (c.operands or {}).get("to") or c.subject or ""),
                        ("aim", q.about if q is not None else ""), ("risk", row.contests if row is not None else "")):
        if by[kind] != 0.0:
            parts.append(ScorePart(kind, owner, by[kind]))
    return tuple(sorted(parts, key=_order))


def heard(chosen_parts, total: float, floor: float = HEARD_FLOOR, drew_off: Optional[float] = None) -> tuple:
    """At most two voices from `chosen_parts` (a candidate's `score_parts`): the one that CARRIED the act (the largest pull with the total's
    sign) and, only if one exists at or above `floor * |total|`, the one that DISSENTED (the largest pull against it); then, if `drew_off` is
    given, a third of kind `DRAW` saying the person did not take his own best. `drew_off` is the score he gave up (his best total less the chosen
    one, 0 or more; `None` when the draw took his best), so the draw's pull is negative: it went against the score.

    `floor` is a display parameter, not a fixture. The entry's `runner_up_parts` is not taken: nothing in the rule reads the runner-up's parts."""
    sign = -1.0 if total < 0 else 1.0
    ordered = sorted(chosen_parts, key=_order)
    out = []
    carried = next((x for x in ordered if x.pull * sign > 0), None)
    if carried is not None:
        out.append(carried)
    dissent = next((x for x in ordered if x.pull * sign < 0 and abs(x.pull) >= floor * abs(total)), None)
    if dissent is not None:
        out.append(dissent)
    if drew_off is not None:
        out.append(ScorePart(DRAW, DRAW, 0.0 - drew_off))
    return tuple(out)


def history(p, part: ScorePart) -> Optional[Citation]:
    """The history a voice cites, read at the call and stored nowhere: for a pursuit voice, `p.scar[owner]` and the newest deed claim in his
    ledger whose kind scores (`align_kind`) on an axis the pursuit projects onto -- the deed claims `deeds_judged` scores, by the pursuit's own
    axes; ties to the later in the ledger. `None` for any other voice (a stance voice's `regard` parts land with B10.55)."""
    if part.kind != "pursuit":
        return None
    axes = [ax for ax, w in to_axes({part.owner: 1.0}).items() if w]
    newest = None
    for claim in p.ledger:
        if is_deed(claim) and any(align_kind(claim.predicate, ax) for ax in axes) and (newest is None or claim.when >= newest.when):
            newest = claim
    return Citation(p.scar.get(part.owner, 0), newest)
