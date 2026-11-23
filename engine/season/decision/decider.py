"""`decision/decider.py` -- ONE DECIDER FOR A CHOICE INSIDE A CONTEST (B10.57; `IS-B2-CHAR-02` steps 1-5).

"Decider" is the ordinary word: the one who decides. `make_decider` is a person deciding among the `legal` values a module's view offers him (a duel
round's approach, a commander's order, a hearing's response), by the alignment cells `data/verbs.py::align_choice` reads for `(key, value)` and his own axis
weights -- the `pursuit` term of `choose.score_terms`, for the values of one key. It is the chooser's own arithmetic over a value instead of a verb, and
it adds no term the chooser does not have: no stance, no fit, no aim, no risk, no refusal memory.

The pick is `choose.sample_order` over those scores -- a DRAW whose odds his interior sets (`choice_temperature` and his own `temper`), never the top
score; at temperature 0 it is the top, ties by the value's spelling, which is the chooser's own control. One owner of the pick: a module's `decide=`
(the duel round's `approach_of`, the field's commander, the hearing's window) is this function bound to its view, not a second pick routine.

AX-2 binds this directory: no store of the world in scope, as an import, a name, an attribute or a string. A person-side reader over the person, his
fixtures, a view and the draw he is handed.
"""

from __future__ import annotations

from typing import Any, Callable, Optional

from engine.dice_engine.fmath import ltr_sum
from ..data.pursuits import _AXES   # the sorted axis order: a sum over the frozenset would add in PYTHONHASHSEED's order
from ..data.verbs import align_choice
from ..state.carriers import Candidate, Person
from .choose import _AXIS_W, _DAMP, deliberation_memo, sample_order, score_order, weigh_by_chance

# The names of a value's terms, in the tuple `watch` is handed: its alignment cells' pull (`score_terms`' `pursuit`, for a choice value) and the caller's `bias`.
TERM_NAMES = ("pursuit", "bias")


def decides_for(fx: "Fixtures", role: str, host_plays: bool) -> bool:
    """Does a wrapper of composition role `role` pass `make_decider`'s pick as its module's `decide=`? Only for a role `Fixtures npc_decider_roles` names and a
    party the host does not play (`host_plays` false); for any other the module runs its interim policy as it does today. `()`, the control, names none."""
    return not host_plays and role in fx.get("npc_decider_roles")


def make_decider(p: Person, fx: "Fixtures", draw: Callable[[str, str], Any], *, key: str,
                 odds: Optional[Callable[[Any, Any], Optional[float]]] = None,
                 bias: Optional[Callable[[Any, Any], float]] = None,
                 watch: Optional[Callable[..., None]] = None) -> Callable[[Any], Any]:
    """`decide(view) -> value`: one of `view.legal`, drawn. `view` is any frozen dataclass with a `legal: tuple` field.

      * `key` -- the choice key (`data/verbs.py`'s `CHOICE_RANGES` names the shipped ones); a value's score is
        `damp * Σ_axis axis_w[axis] * align_choice(key, value, axis)`, `axis_w` and `damp` the chooser's own (`deliberation_memo`), then times the factor
        `choose.weigh_by_chance` gives the believed chance `odds(view, value)` where the caller hands an `odds` (the module's pure estimate: `p_carried` for a
        hearing, `fight_estimate` for a fight), exactly as it prices a candidate; no `odds`, the arm `none` and an answer of `None` read 1.0. A value whose
        score is exactly 0.0 is not asked the query, as `score_terms` does not ask it;
      * `bias` -- an optional `(view, value) -> float`, added to the value's score after the pricing (`None` adds nothing: `IS-MB-03`'s window decider is its one
        caller, with its `window_responses` weights);
      * `draw` -- `(person id, purpose) -> Random`, `state/ids.py::draw_factory`'s product, ALREADY BOUND to the wrapper's scope (`role:scene id:n`): the
        pick draws `choice:<key>:<value>` on it, one stream per value as the chooser keys one per candidate, so a value's noise belongs to the value;
      * `watch` -- an observer, as `make_chooser`'s (B09.13): `watch(p, view, ranked, terms, sampled)` once per decision among two or more values, `ranked` the
        values in score order, `terms` the parallel `(pursuit, bias)` tuples (`TERM_NAMES`), `sampled` the order drawn; copies, and its return is ignored.

    A view with one legal value returns it and takes no draw (and calls no `watch`: nothing was decided); an empty `legal` is refused. The person is read when
    the decider is called, not when it is made."""
    def decide(view: Any) -> Any:
        legal = tuple(view.legal)
        if not legal:
            raise ValueError(f"a decider for {key!r} was handed a view with no legal value")
        if len(legal) == 1:
            return legal[0]
        memo = deliberation_memo(p, fx)
        axis_w, damp = memo[_AXIS_W], memo[_DAMP]
        cands = [Candidate(key, str(v)) for v in legal]         # the value's spelling is its candidate's subject: what the sampler keys its stream by
        value_of = {id(c): v for c, v in zip(cands, legal)}
        terms_of, scores = {}, {}
        for c, v in zip(cands, legal):
            pursuit = damp * ltr_sum(axis_w[ax] * align_choice(key, v, ax) for ax in _AXES)
            pursuit *= weigh_by_chance(fx, None if odds is None or pursuit == 0.0 else (lambda v=v: odds(view, v)))
            extra = 0.0 if bias is None else float(bias(view, v))
            terms_of[id(c)], scores[id(c)] = (pursuit, extra), pursuit + extra if extra else pursuit
        ranked = score_order(cands, scores)
        sampled = sample_order(ranked, lambda c: scores[id(c)], p, fx, draw)
        if watch is not None:
            watch(p, view, [value_of[id(c)] for c in ranked], [terms_of[id(c)] for c in ranked], [value_of[id(c)] for c in sampled])
        return value_of[id(sampled[0])]
    return decide
