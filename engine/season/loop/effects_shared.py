"""`season.loop.effects_shared` -- the primitives more than one domain file in the split needs.

Holds `EFFECTS` itself and its `effect_for` decorator, the one operand reader
(`_operand`), the shared §10-ladder refusal (`_decline_ascent`, used by `move`/`migrate`/`found`),
the oblige-term pair (`_oblige_term`/`_new_oblige_term`, used by `oblige`/`determine`/`_renewals`),
and the treasury-move trio (`_shift`/`_debit`/`_exercised_office`: `_shift` is used by `transfer`/`requisition`/`found`,
`_debit` by `_shift` and `build`, `_exercised_office` by `requisition`/`_renewals`).
Every domain file imports what it needs from here rather than re-declaring its own copy (CLAUDE.md
§8: the rule lives once) -- see `effects.py`'s own docstring for why THIS file, alone among the
seven, is still eagerly imported whole by the aggregator rather than left to import on demand.
"""

from __future__ import annotations

from typing import Optional

from ..data.rosters import MARCH_TARGET_KINDS, SUBTREE_OCCUPATION_KINDS, is_season_count, task_share
from ..gaps import Forbidden, InstrumentDefect
from ..queries.world_q import holder_faction_of, occupies, seat_people_at
from ..state.carriers import Term
from ..state.gate import NO_CHANGE, seat_faction
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


def _share(res: "Resolution | None"):
    """B07.02: THE FRACTION OF ITS EFFECT THE ACT'S BAND LETS LAND -- `task_share` read off `res.degree`, the one table; a `res` of
    `None` (the arm `off`, a flat un-routed act, a bookkeeping row) is the full effect. No effect names a band."""
    return task_share(None if res is None else res.degree)


def _scaled(n: int, res: "Resolution | None") -> int:
    """B07.02: `n` of a magnitude, as much of it as the band lets land, floored (`n * share`, whole units). Share 1 returns `n`
    itself, so an act with no band, or a full band, writes what it always wrote."""
    f = _share(res)
    return n if f == 1 else (n * f.numerator) // f.denominator


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

    ⚠ IT IS THE OWNER OF THE RULE (§8): an effect that defaulted a missing operand (`from`/`to` to
    `""`, `kind` to `"grain"`, `amount` to `1`; `to` to the actor, which would confer an office on
    whoever happened to be acting when the act named nobody) would answer *the same situation*
    differently from one that raised."""
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
    Callers still build their own message, since what "not up
    the ladder" names differs (a destination for `move`/`migrate`, a parent rung for `found`)."""
    TRACE.decision(msg, "S10/E3", chose="change nothing, so the fold emits the refusal",
                   alternatives=["write the edge anyway (add_tenure raises and the season "
                                 "dies)", "let the precondition admit it and crash later"])
    return NO_CHANGE


def _fixture_seasons(w: "World", key: str) -> Optional[int]:
    """A TERM LENGTH A FIXTURE DECLARES, IN SEASONS, with its refusal in one place. `None` is the control arm: no term at all. Anything
    else must be a whole number of seasons, at least one: a term of `0` would mature in the season that declared it (MATTER has already
    run when RESOLVE opens the edge, so it lapses at the next barrier with no window to pay), and a renewal by `0` moves no clock and
    would be refused as no renewal at all -- a number that looks like a setting and behaves like a defect."""
    n = w.fixtures.get(key)
    if n is not None and not is_season_count(n):
        raise Forbidden(
            f"fixture {key} is {n!r}", "T-n",
            needs="None (no term: the control arm) or a whole number of seasons >= 1",
            law="04 §B.8 `term?` / T-n -- the opening act declares a term that MATTER matures at a "
                "later barrier; a term that cannot outlive its own season is not one")
    return n


def _oblige_term(w: "World") -> Optional[int]:
    """THE LENGTH, IN SEASONS, OF THE TERM AN `oblige` IS DECLARED FOR -- and that a paying act winds
    it on by -- read ONCE for both of its readers (`_eff_oblige`, `_renewals`), through `_fixture_seasons`.
    `None` is `H-159`'s control arm: no term at all."""
    return _fixture_seasons(w, "oblige_term")


def _new_oblige_term(w: "World", a: "Act") -> Optional["Term"]:
    """The `Term` an `oblige` edge OPENS with, for the two writers that mint one from scratch
    (`_eff_oblige`, `_eff_determine`) -- one owner for the `None if n is None else Term(...)`
    ternary rather than a second hand-copy of it. `_renewals`
    winds an EXISTING term rather than minting one and is not one of these two."""
    n = _oblige_term(w)
    return None if n is None else Term(w.tick + n, a.id)


def _provisional_term(w: "World", a: "Act") -> Optional["Term"]:
    """The `Term` a PARTIAL's hold OPENS with -- the one constructor of it (`H-611`, `14_VERBS_BINDING_C` commit C1), in
    `_new_oblige_term`'s shape: matured at the MATTER barrier of tick `w.tick + n`, citing this act (AX-5). `None` is the CONTROL: an
    untermed hold, exactly what a Success opens, so a Partial reads as a Success there; the fixture SHIPS at 2 (B21.73). Anything else
    must be a whole number of seasons, at least one, refused as `_oblige_term` refuses it (a `0` would lapse at the very next
    barrier). Callers (B21.14): `_eff_confer` and `_eff_succeed` at a Partial band; a Partial `revoke` opens no hold."""
    n = _fixture_seasons(w, "provisional_term")
    if n is None:
        return None
    return Term(w.tick + n, a.id)


def whole_amount(amount) -> bool:
    """A store move's amount: a whole number of units, at least one. `bool` is refused (YAML `yes`).
    The one reading of it (H-306, A-81): an effect that moves stores returns `NO_CHANGE` when it is false,
    before it builds its `Change` (the fold then emits the row's own refusal), and `_debit`/`_shift` raise on
    it, so a caller that skipped the check fails loudly rather than moving matter."""
    return isinstance(amount, int) and not isinstance(amount, bool) and amount >= 1


def _decline_amount(verb: str, amount) -> Change:
    """The refusal of a store move whose amount is not a whole positive number: one `TRACE.decision` line
    naming the amount, then `NO_CHANGE` so the fold emits the row's own refusal. The backstop, not the path:
    formation excludes such an amount first (`whole_amount`'s docstring)."""
    TRACE.decision(f"{verb} carries an amount of {amount!r}, which is not a whole number of units, at least one",
                   "H-306/A-81", chose="change nothing, so the fold emits the refusal",
                   alternatives=["move the stores anyway (a negative amount reverses the move, a fraction splits a unit)"])
    return NO_CHANGE


def _debit(rung, kind: str, amount) -> None:
    """`rung`'s stores down by `amount` of `kind`: copied before it is written, as `_eff_transfer`
    always did, so no other holder of the old dict sees it change. The one body of the debit side of
    `_shift` and of `build`'s one-sided consumption (the cost goes into the fabric). A non-whole amount
    is an `InstrumentDefect` (`whole_amount`): the effect declines it before it gets here."""
    if not whole_amount(amount):
        raise InstrumentDefect(f"a store move of {amount!r} of {kind!r} reached `_debit`: an amount is a whole "
                               f"number of units, at least one, and the calling effect should have declined it "
                               f"(`whole_amount`)")
    rung.stores = dict(rung.stores or {})
    rung.stores[kind] = rung.stores.get(kind, 0) - amount


def _shift(src, dst, kind: str, amount) -> None:
    """MATTER MOVES FROM ONE RUNG'S STORES TO ANOTHER'S, CONSERVED: `src` down by `amount` of `kind`,
    `dst` up by the same. The one body of every act that moves stores between two rungs -- `transfer`
    and, since plan position `19`, `requisition` -- factored so the W3 audit's lesson is written once:
    *"six grain left the world and arrived nowhere"* was a transfer that decremented one side and
    forgot the other. Each store is copied before it is written, as `_eff_transfer` always did, so
    no other holder of the old dict sees it change. Called only from inside a `Change.apply`: the
    gate reads both rungs either side of it (G4). A non-whole amount raises in `_debit`, before either
    side is written."""
    _debit(src, kind, amount)
    dst.stores = dict(dst.stores or {})
    dst.stores[kind] = dst.stores.get(kind, 0) + amount


def _exercised_office(w: "World", a: "Act") -> Optional["Office"]:
    """The Office an act's `via` names, or `None` -- the one-line resolution `_eff_requisition` and
    `_renewals` both read. NOT `_seat_rung`: that helper's
    fallback (a document's `payload.rung`, else the actor) is for a Record write, not for either of
    these two, which have their own reasons to want the bare Office or nothing."""
    return w.offices.get(a.via) if a.via else None


def occupying_faction(w: "World", via: str, rid: str, unheld: bool = False) -> Optional[str]:
    """THE LICENCE OF OCCUPATION (#453 §10.4 steps 8 and 11), the one reading `seize` (a Rung) and `raze` share:
    the faction of the exercised seat `via`, when it OCCUPIES the place `rid` (`world_q.occupies`, the one
    reading of that: mustered under a settlement, arrived at a territory, and a taken territory's settlements
    with it) and the place is held by ANOTHER faction (`holder_faction_of`).
    `unheld=True` (`seize`'s Rung half; `09_WR_world_motion` edit 2) also passes a place NOBODY holds, on the same
    occupation: the rule for held land is the rule for unheld land. `raze` leaves it `False` and keeps its decline.
    `None` -- the licence fails -- for a subject that is no Rung or no `march_target_kinds` kind, a seat with
    no faction, a place nobody holds (H-166: who holds an unheld place is unruled; passed when `unheld`) or the seat's own
    faction holds, or a faction that does not occupy it. A defended territory therefore stays its holder's AGAINST A
    MARCH: one that lost never arrived, so nothing occupies and nothing is seized. Occupation is PRESENCE (R-6, ruled
    for settlements at #453), so people placed on a territory by other means (a `move`) occupy it as well; that is the
    settlement rule's own weakness carried to the larger prize, named in `HANDOFF_MB.md`, not closed here. Every
    decline is a `NO_CHANGE` at the effect, so the order of these tests is not observable; a caller adds its own declines (`seize`: the actor must be
    committed to the seat's faction, and `may_seize` over the hold it replaces)."""
    rung = w.rungs.get(rid)
    mine = seat_faction(w, via)
    if rung is None or rung.kind not in MARCH_TARGET_KINDS or mine is None:
        return None
    holder = holder_faction_of(w, rid)
    if holder == mine or (holder is None and not unheld):
        return None
    # B21.79 (CP-T09-07 (b)): the seat's sworn men present at a settlement are presence as its faction's members are
    # (`world_q.seat_people_at`); a territory is occupied by standing AT it, which the union does not widen.
    if not (occupies(w, rid, mine)
            or (rung.kind in SUBTREE_OCCUPATION_KINDS and seat_people_at(w, via, rid))):
        return None
    return mine
