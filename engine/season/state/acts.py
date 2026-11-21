"""`season.state.acts` -- THE ACT STORE. Append-only, and the store `causes[]` resolves against.

`04:1024` step 3 names it among the things the critical path builds at step 3: *"the stores with
private setters · the gate · the four tokens · the receipt mint · the log · the ledgers · the act
store · `World`"*.

WHAT IT IS FOR, and it is one thing. `loop/resolve.py` folds an Act into Events carrying
`causes=[a.id]` -- and without this store **nothing in the world would hold that act**, so the id on
the most load-bearing field in the model would resolve against nothing. #353 §19.4 calls `causes[]` *"the
substrate of the entire emergent-narrative claim"*; `hole_register.yaml`'s `H-80` row records the
consequence in its own words: *"a log walker drops an unresolvable `[a.id]` exactly as it drops
`[ROOT]`"*. An unresolvable cause and an absent cause are the same object to every reader. This
store is what makes them different.

⚠ IT IS NOT A LOG OF EVENTS AND IT IS NOT A LEDGER. The log holds what OCCURRED (`Event`); this
holds what was ATTEMPTED and resolved (`Act`). An act that was refused is still in here -- the
refusal Event names it as its cause (`loop/resolve.py`), so a store that admitted only successful
acts would make every refusal chain unresolvable, which is the defect one level along.

APPEND-ONLY IS ENFORCED, NOT ASKED. The list is private and there is no remove, no clear, no
setter and no mutable accessor: `__iter__` yields from a tuple copy so a caller holding the
result cannot reach the backing list.

⚠ RE-APPENDING AN ID IS IDEMPOTENT WHEN THE ACT IS EQUAL AND REFUSED WHEN IT DIFFERS. Read
`append`'s own note for why -- the short version is that a DIFFERING act on a live id makes every
`causes[]` naming it ambiguous with both readings available, while an EQUAL one changes no
reading, and a real id collision in the tree (`W17`'s control arm) makes the distinction load-
bearing rather than theoretical.
"""
from typing import Iterator, Optional

from .carriers import Act, Scene
from ..gaps import Unspecified


class ActStore:
    """The acts this world has resolved, in resolution order. Append-only."""

    __slots__ = ("_acts", "_by_id", "_scenes")

    def __init__(self) -> None:
        self._acts: list[Act] = []
        self._by_id: dict[str, Act] = {}
        self._scenes: dict[str, Scene] = {}

    def append(self, act: Act) -> Act:
        """Record `act`. Returns it, so a caller can append inline in the fold.

        ⚠ NEVER OVERWRITES. A DIFFERING act on a live id is REFUSED; an EQUAL one is a no-op.
        `resolve()` sorts one global array and folds each member once, so a second append of one
        id means either the same act reached the store twice by two entry points (harmless, and
        deliberate -- see the note below) or two acts were minted onto one id. The second is
        reachable: `H(seed, tick, actor, "act:verb:key")` carries no draw ordinal, so two acts by
        one actor on one verb with one key in one tick collide. Taking the last writer would hide
        it, because `causes[]` would then resolve to a real act that is not the one that caused
        the Event -- silently, with nothing to notice.
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
        # ⚠ THE TEST IS EQUALITY, NOT IDENTITY, AND A REAL COLLISION IS WHY. With `interactions_per_scene`
        # set to `unbounded` (`W17`'s control arm), one scene folds four `speak` acts by `p_king`, and the
        # act mint `H(seed, tick, actor, "act:verb:key")` carries NO DRAW ORDINAL -- so two of them are
        # distinct objects on one id. That collision is REAL: the Event ids derived from `a.id` collide with
        # it, which is the same defect `W4` found in the emission id and fixed there with `new_draw()` (see
        # `World.write`). It is NOT fixed here: the act mint feeds every Event id, so changing it moves
        # every golden.
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

    def add_scene(self, sc: Scene) -> None:
        """Keep the Scene an act was released in, beside the acts (B09.16, `01_CORE_reason_trail_in_the_act_store`).

        APPEND-ONLY, AND A REPEATED ID IS REFUSED, as `append` refuses a differing act: two Scenes on one id make
        `scene_of` ambiguous with both readings available. Unlike `append`, an EQUAL repeat is refused too -- a Scene
        is stored once, by RESOLVE, before the acts it carries, so a second store of one is a second writer.

        WRITTEN BY RESOLVE ONLY, as `append` is: this store has no token of its own, the discipline is where it is
        reached from (`loop/resolve.py::resolve`, the ACTS step) and that `loop/deliberate.py` holds none and stores
        nothing (`test_g2_token.py::test_g2_deliberate_mutates_no_store_by_any_route` measures the world around it).
        NOT IN THE CONTENT HASH (`World.content_hash`'s frames name `acts`, not this): the port carries it as data."""
        if not isinstance(sc, Scene):
            raise Unspecified(
                f"the scene store holds Scene, not {type(sc).__name__}", "S27",
                needs="a Scene",
                law="the store holds the question an act answered; an Act goes in `append`")
        if sc.id in self._scenes:
            raise Unspecified(
                f"scene id {sc.id!r} is already in the store", "S27",
                needs="one Scene per id",
                law="two Scenes on one id make `scene_of` ambiguous, and the ambiguity is silent")
        self._scenes[sc.id] = sc

    def scene_of(self, act_id: str) -> Optional[Scene]:
        """The Scene a STORED act was released in -- through the act's own `scene` id -- or `None`: an act the store
        never held, an act with no scene (a hand-built act, the pre-`W17` bare `Act`), or one naming a Scene not stored.
        Never raises: an absent question is the honest answer for those, and `loop/resolve.py::_occasion_ids` keeps
        `[a.id]` alone for it."""
        act = self._by_id.get(act_id)
        if act is None:
            return None
        sid = getattr(act, "scene", None)
        return self._scenes.get(sid) if sid else None

    def scenes(self) -> tuple:
        """Every Scene stored, in release order. A tuple copy: the caller cannot reach the backing map."""
        return tuple(self._scenes.values())

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
