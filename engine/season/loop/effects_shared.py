"""`season.loop.effects_shared` -- the primitives more than one domain file in the split needs.

EXTRACTED from `effects.py` at the per-subsystem split (Phase 4 of the decomposition, CLAUDE.md's
settled requirement that each subsystem be its own module -- per-subsystem files, human-readable,
self-contained). Holds `EFFECTS` itself and its `effect_for` decorator, the one operand reader
(`_operand`), the shared §10-ladder refusal (`_decline_ascent`, used by `move`/`migrate`/`found`),
the oblige-term pair (`_oblige_term`/`_new_oblige_term`, used by `oblige`/`determine`/`_renewals`),
and the treasury-move pair (`_shift`/`_exercised_office`, used by `transfer`/`levy`/`_renewals`).
Every domain file imports what it needs from here rather than re-declaring its own copy (CLAUDE.md
§8: the rule lives once) -- see `effects.py`'s own docstring for why THIS file, alone among the
seven, is still eagerly imported whole by the aggregator rather than left to import on demand.
"""

from __future__ import annotations

from typing import Optional

from ..gaps import Forbidden, InstrumentDefect
from ..state.carriers import Term
from ..state.gate import NO_CHANGE
from ..trace_log import TRACE

# ---------------------------------------------------------------------------
# THE EFFECTS. One per verb, OWNED BY THE RESOLVER.
#
# ⚠ PART E's `writes:` COLUMN NAMES THE CELL AND NEVER THE VALUE. `transfer` writes
# `(Rung, stores)` -- it does not say BY HOW MUCH, or that the giver's store goes DOWN. Without
# that the fold checks a precondition, emits, and changes nothing, so `transfer` twice from a
# one-unit larder succeeds twice: the scarcity §27.1 rests on never happens.
#
# THE DISTINCTION FROM THE `effect` PARAMETER W3 REMOVED IS THE WHOLE POINT, and it is §27.2's.
# A CALLER-supplied lambda is a second resolver: every caller may disagree about what a verb does,
# and each probe did. A VERB-KEYED effect registered here is the resolver's BODY -- one
# implementation, the same for every caller, and a verb with a `writes:` and no effect REFUSES
# rather than silently writing nothing.
#
# This gap is register row H-63.
# ---------------------------------------------------------------------------
EFFECTS: dict = {}


def effect_for(verb: str):
    def deco(fn):
        EFFECTS[verb] = fn
        return fn
    return deco


def _operand(a: "Act", name: str):
    """THE FOLD'S ONE READ OF A CARRIED OPERAND. A missing one RAISES.

    ⚠ AN ABSENT OPERAND AT RESOLVE IS AN `InstrumentDefect`, NOT A REFUSAL, AND THE DISTINCTION
    IS THE WHOLE OF `W-C`'s SECOND HALF. A refusal says *the world would not permit this*; a
    caller minting a `transfer` that names no receiver is saying nothing about the world at all.
    Filing it as a refusal would emit `emits_on_refusal`, `W-B` would deposit that at WITNESS, and
    every witness would end the season holding a belief about a granary the act never named --
    the instrument's own gap, laundered into the game as evidence. `operands_for` is what makes
    this unreachable from a COMPUTED act: a Candidate whose operands cannot be derived is never
    formed, so an act arriving here without one came from a hand-written call site.

    ⚠ IT IS THE OWNER OF THE RULE, AND THREE EFFECTS HAD THEIR OWN COPY. `_eff_move` raised on a
    missing `to` and `_eff_work` on a missing `site` -- both correct, both written twice -- while
    `_eff_transfer` DEFAULTED four operands (`from`/`to` to `""`, `kind` to `"grain"`, `amount` to
    `1`) and `_eff_confer` defaulted `to` to the actor, i.e. conferred an office on whoever
    happened to be acting when the act named nobody. Same situation, four verbs, three answers.
    §8: the rule lives once."""
    d = a.payload if isinstance(getattr(a, "payload", None), dict) else {}
    if d.get(name) is None:
        raise InstrumentDefect(
            f"a {a.verb!r} reached its effect with no {name!r} operand. The fold binds operands "
            f"from the act's payload and `operands_for` forms NO Candidate whose operands it "
            f"cannot derive, so an act minted without one is a CALLER defect and not a design "
            f"gap -- and fabricating a value here would name a thing nobody chose. Payload: "
            f"{sorted(d)}")
    return d[name]


def _decline_ascent(msg: str) -> Change:
    """The shared §10-ladder refusal: `move`, `migrate` and `found` each require their
    destination/parent to ascend the containment ladder and decline identically when it does not
    -- one owner for the `chose`/`alternatives` pair rather than a third hand-copy of it
    (`/simplify`, BATCH-CLOSE Phase 2). Callers still build their own message, since what "not up
    the ladder" names differs (a destination for `move`/`migrate`, a parent rung for `found`)."""
    TRACE.decision(msg, "S10/E3", chose="change nothing, so the fold emits the refusal",
                   alternatives=["write the edge anyway (add_tenure raises and the season "
                                 "dies)", "let the precondition admit it and crash later"])
    return NO_CHANGE


def _oblige_term(w: "World") -> Optional[int]:
    """THE LENGTH, IN SEASONS, OF THE TERM AN `oblige` IS DECLARED FOR -- and that a paying act winds
    it on by -- read ONCE for both of its readers (`_eff_oblige`, `_renewals`), with the refusal
    in the same place. `None` is `H-159`'s control arm: no term at all. Anything else must be a
    whole number of seasons, at least one: a term of `0` would mature in the season that declared
    it (MATTER has already run when RESOLVE opens the edge, so it lapses at the next barrier with
    no window to pay), and a renewal by `0` moves no clock and would be refused as no renewal at
    all -- a number that looks like a setting and behaves like a defect."""
    n = w.fixtures.get("oblige_term")
    if n is not None and (isinstance(n, bool) or not isinstance(n, int) or n < 1):
        raise Forbidden(
            f"fixture oblige_term is {n!r}", "T-n",
            needs="None (no term: H-159's control) or a whole number of seasons >= 1",
            law="04 §B.8 `term?` / T-n -- the opening act declares a term that MATTER matures at a "
                "later barrier; a term that cannot outlive its own season is not one")
    return n


def _new_oblige_term(w: "World", a: "Act") -> Optional["Term"]:
    """The `Term` an `oblige` edge OPENS with, for the two writers that mint one from scratch
    (`_eff_oblige`, `_eff_determine`) -- one owner for the `None if n is None else Term(...)`
    ternary rather than a second hand-copy of it (`/simplify`, BATCH-CLOSE Phase 2). `_renewals`
    winds an EXISTING term rather than minting one and is not one of these two."""
    n = _oblige_term(w)
    return None if n is None else Term(w.tick + n, a.id)


def _shift(src, dst, kind: str, amount) -> None:
    """MATTER MOVES FROM ONE RUNG'S STORES TO ANOTHER'S, CONSERVED: `src` down by `amount` of `kind`,
    `dst` up by the same. The one body of every act that moves stores between two rungs -- `transfer`
    and, since plan position `19`, `levy` -- factored so the W3 audit's lesson is written once:
    *"six grain left the world and arrived nowhere"* was a transfer that decremented one side and
    forgot the other. Each store is copied before it is written, as `_eff_transfer` always did, so
    no other holder of the old dict sees it change. Called only from inside a `Change.apply`: the
    gate reads both rungs either side of it (G4)."""
    src.stores = dict(src.stores or {})
    src.stores[kind] = src.stores.get(kind, 0) - amount
    dst.stores = dict(dst.stores or {})
    dst.stores[kind] = dst.stores.get(kind, 0) + amount


def _exercised_office(w: "World", a: "Act") -> Optional["Office"]:
    """The Office an act's `via` names, or `None` -- the one-line resolution `_eff_levy` and
    `_renewals` both did inline (`/simplify`, BATCH-CLOSE Phase 2). NOT `_seat_rung`: that helper's
    fallback (a document's `payload.rung`, else the actor) is for a Record write, not for either of
    these two, which have their own reasons to want the bare Office or nothing."""
    return w.offices.get(a.via) if a.via else None
