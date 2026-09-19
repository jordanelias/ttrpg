"""`season.state.acts` -- THE ACT STORE. Append-only, and the store `causes[]` resolves against.

`04:1024` step 3 names it among the things the critical path builds at step 3: *"the stores with
private setters · the gate · the four tokens · the receipt mint · the log · the ledgers · the act
store · `World`"*. The tree built steps 4-8 and 10 before step 3, which is why this file arrives
after the loop that needs it rather than before.

WHAT IT IS FOR, and it is one thing. `loop/resolve.py` folds an Act into Events carrying
`causes=[a.id]` -- and until now **nothing in the world held that act**, so the id on the most
load-bearing field in the model resolved against nothing. #353 §19.4 calls `causes[]` *"the
substrate of the entire emergent-narrative claim"*; `hole_register.yaml`'s `H-80` row records the
consequence in its own words: *"a log walker drops an unresolvable `[a.id]` exactly as it drops
`[ROOT]`"*. An unresolvable cause and an absent cause are the same object to every reader. This
store is what makes them different.

⚠ IT IS NOT A LOG OF EVENTS AND IT IS NOT A LEDGER. The log holds what OCCURRED (`Event`); this
holds what was ATTEMPTED and resolved (`Act`). An act that was refused is still in here -- the
refusal Event names it as its cause (`resolve.py:395`), so a store that admitted only successful
acts would make every refusal chain unresolvable, which is the defect one level along.

APPEND-ONLY IS ENFORCED, NOT ASKED. The list is private and there is no remove, no clear, no
setter and no mutable accessor: `__iter__` yields from a tuple copy so a caller holding the
result cannot reach the backing list.

⚠ RE-APPENDING AN ID IS IDEMPOTENT WHEN THE ACT IS EQUAL AND REFUSED WHEN IT DIFFERS. Read
`append`'s own note for why -- the short version is that a DIFFERING act on a live id makes every
`causes[]` naming it ambiguous with both readings available, while an EQUAL one changes no
reading, and a real id collision in the tree (`W17`'s control arm) makes the distinction load-
bearing rather than theoretical. An earlier draft of this paragraph said re-appending an id "is
refused rather than ignored" full stop; that was written against rev 1 and left standing when the
code relaxed, which is a docstring asserting a check the code does not perform -- false in the
direction that stops the next reader checking.
"""
from typing import Iterator, Optional

from .carriers import Act
from ..gaps import Unspecified


class ActStore:
    """The acts this world has resolved, in resolution order. Append-only."""

    __slots__ = ("_acts", "_by_id")

    def __init__(self) -> None:
        self._acts: list[Act] = []
        self._by_id: dict[str, Act] = {}

    def append(self, act: Act) -> Act:
        """Record `act`. Returns it, so a caller can append inline in the fold.

        ⚠ REFUSES A DUPLICATE ID RATHER THAN OVERWRITING OR IGNORING. `resolve()` sorts one
        global array and folds each member once, so a second append of one id means either the
        same act was folded twice or two acts were minted onto one id -- and `H(seed, tick,
        actor, "act:verb:key")` makes the second reachable: two acts by one actor on one verb
        with one key in one tick collide. Both are defects and neither is visible if the store
        takes the last writer, because `causes[]` then resolves to a real act that is not the
        one that caused the Event.
        """
        if not isinstance(act, Act):
            raise Unspecified(
                f"the act store holds Act, not {type(act).__name__}", "S27",
                needs="an Act",
                law="the store `causes[]` resolves against holds ACTS; an Event goes in the log")
        prior = self._by_id.get(act.id)
        # ⚠ IDEMPOTENT ON AN EQUAL ACT, REFUSING ON A DIFFERING ONE. Re-recording an act already
        # recorded asserts nothing new; recording a DIFFERENT act under a live id is the
        # ambiguity this store exists to prevent. That lets every entry point record
        # unconditionally -- `resolve()` before its refusal branches, `_fold` for the callers
        # that enter there directly -- so the invariant holds at the entry point rather than at
        # the one path someone remembered (`CLAUDE.md` §8's shape applied to a store).
        #
        # ⚠ THE TEST IS EQUALITY, NOT IDENTITY, AND A REAL COLLISION IS WHY. Rev 1 compared
        # `prior is act` and `W17`'s control arm went red on it: with `interactions_per_scene`
        # set to `unbounded`, one scene folds four `speak` acts by `p_king`, and the act mint
        # `H(seed, tick, actor, "act:verb:key")` carries NO DRAW ORDINAL -- so two of them are
        # distinct objects on one id. That collision is REAL and it PREDATES this store: the
        # Event ids derived from `a.id` collide with it, which is the same defect `W4` found in
        # the emission id and fixed there with `new_draw()` (see `World.write`). It is NOT fixed
        # here: the act mint feeds every Event id, so changing it moves every golden, and that
        # is its own change with its own re-record.
        #
        # What this store must not do is FAIL on it, because with equal content the ambiguity
        # does not arise -- `causes[]` naming that id resolves to the same act either way, which
        # is the only question this store is asked. Two acts that DIFFER on one id is the case
        # where the reading changes, and that is still refused below.
        if prior == act:
            return act
        if prior is not None:
            raise Unspecified(
                f"act id {act.id!r} is already in the store (verb {prior.verb!r} by "
                f"{prior.actor!r}); the new one is {act.verb!r} by {act.actor!r}", "S27",
                needs="one act per id",
                law="two acts on one id make every `causes[]` naming it ambiguous, and the "
                    "ambiguity is silent -- both readings resolve")
        self._acts.append(act)
        self._by_id[act.id] = act
        return act

    def __contains__(self, act_id: object) -> bool:
        return act_id in self._by_id

    def get(self, act_id: str) -> Optional[Act]:
        return self._by_id.get(act_id)

    def ids(self) -> frozenset:
        """The id set, for the log's `causes[]` check. Frozen: the checker may not mutate it."""
        return frozenset(self._by_id)

    def __iter__(self) -> Iterator[Act]:
        # A TUPLE COPY, NOT THE LIST. `iter(self._acts)` hands back an iterator over the live
        # backing list, and a caller doing `list(store)` then holds a list it can append to
        # believing it has the store. Append-only is only a property if it cannot be spelled
        # around, and the cheapest way around it is a reference.
        return iter(tuple(self._acts))

    def __len__(self) -> int:
        return len(self._acts)

    def __repr__(self) -> str:
        return f"ActStore({len(self._acts)} acts)"
