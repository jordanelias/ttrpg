"""`season.state.gate` -- THE RECEIPT MINT. The one place a `Receipt` comes from.

`04:1024` step 3 names *"the gate · the four tokens · the receipt mint · the log"* as one unit of
the critical path, and this is the mint half of it.

WHAT THIS FILE OWNS AND WHAT IT DOES NOT. It owns **the authority to say a write happened**. It
does NOT own the matrix check, the step check, the emission rule or the `(kind, field)` keying --
those are still `World.write`, which is ~160 lines of Layer-2 policy welded to `World`'s own
state, and moving them is `G2`'s signature rewrite across 33 call sites, not this unit's. The
split is deliberate and is stated here so the next reader does not conclude the relocation was
forgotten: **G1a makes the receipt unforgeable; G2 moves the call.**

⚠ THE AUTHORIZATION WINDOW, AND WHY IT IS NOT A PER-CALL RETURN VALUE. The obvious design is
`write() -> Receipt`, and it does not fit the one caller that matters. `loop/resolve.py`'s
`_apply_write` cannot know WHAT it changed until the effect has run: the effect reports touched
ids from inside the `apply()` closure, so the subjects of the receipts are discovered DURING the
write and read AFTER it returns. A mint that closed at `return` would therefore be unusable by
the fold -- which is every act in the game -- and the fold would go on hand-building changes,
leaving this file a decoration.

So the window opens when a gate write begins and stays open until the NEXT gate write opens its
own, or the step barrier closes it. `mint()` outside a window raises. The property that buys:
**you cannot mint a receipt without having just performed a real gate write**, which is the whole
of what `changes[]` needs to mean something. What it does not buy: a second receipt minted after
an unrelated later write would be attributed to that write. That is a narrower guarantee than
"one receipt per write" and it is the honest one -- stating it is cheaper than a guard that
implies it.
"""
from typing import Any, Optional

from ..gaps import Forbidden
from .carriers import Receipt


class _Window:
    """The write currently authorized to mint. Not a token in `04:199`'s sense -- that is `G2`."""

    # roster-exempt: MECHANISM -- `__slots__` names THIS CLASS'S OWN ATTRIBUTES, as on
    # `carriers.Sensation` and `View`. It is a Python language construct, not a definition of
    # anything in the game, and moving it to `rosters.yaml` would make the attribute list of a
    # private helper into game data.
    __slots__ = ("record_kind", "fieldname", "wclass", "tick")

    def __init__(self, record_kind: str, fieldname: str, wclass: str, tick: int) -> None:
        self.record_kind, self.fieldname = record_kind, fieldname
        self.wclass, self.tick = wclass, tick

    def __repr__(self) -> str:
        return f"({self.record_kind}, {self.fieldname}) {self.wclass} @t{self.tick}"


class Gate:
    """Mints receipts, and remembers which ones it minted."""

    # roster-exempt: MECHANISM -- as above; these are the gate's own private attributes.
    __slots__ = ("_serial", "_minted", "_open")

    def __init__(self) -> None:
        self._serial = 0
        # serial -> the EXACT object handed out. The log checks identity against this, so a
        # forged receipt carrying a real serial is a different object and does not match.
        self._minted: dict[int, Receipt] = {}
        self._open: Optional[_Window] = None

    # -- the window -----------------------------------------------------------------------
    def opening(self, record_kind: str, fieldname: str, wclass: str, tick: int) -> None:
        """Called by `World.write` as it begins an authorized write."""
        self._open = _Window(record_kind, fieldname, wclass, tick)

    def close(self) -> None:
        """Called at a step barrier. A window left open across a barrier would let the next
        step's first hand-built change mint against the previous step's write."""
        self._open = None

    @property
    def is_open(self) -> bool:
        return self._open is not None

    # -- the mint -------------------------------------------------------------------------
    def mint(self, subject: str, mode: str, driver: str,
             field: Optional[str] = None, delta: Any = None, spec: Any = None) -> Receipt:
        """Issue a receipt for the write currently open. Raises outside a window."""
        if self._open is None:
            raise Forbidden(
                f"no gate write is open, so there is nothing to issue a receipt for "
                f"(subject {subject!r}, field {field!r})", "S16",
                needs="a `World.write(...)` that has begun",
                law="a Receipt asserts THE GATE WROTE THIS. Minting one with no write behind it "
                    "is the ID-9 fabrication the type exists to prevent, committed at the mint")
        self._serial += 1
        r = Receipt(subject, mode, driver, field, delta, spec, serial=self._serial)
        self._minted[self._serial] = r
        return r

    def issued(self, change: Any) -> bool:
        """True only for a receipt THIS gate handed out -- identity, never equality.

        ⚠ `is`, NOT `==`. `Receipt` is a dataclass, so `==` compares the six fields, and a forged
        receipt copying a real one's serial and values would compare equal to it. The object is
        the credential; a copy of a credential is not one.
        """
        if not isinstance(change, Receipt):
            return False
        return self._minted.get(change.serial) is change

    def __repr__(self) -> str:
        return f"Gate({self._serial} minted, window={self._open!r})"
