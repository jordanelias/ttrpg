"""S33 -- DETERMINISM. The mint (`H`) and its sentinel (`ROOT`), extracted from `shape.py`
(step 1 of the shape.py decomposition, ED-IN-0203) with no behaviour change. Importers name
this module directly (`from ..state.ids import H, ROOT`); the `shape.py` facade that used to
re-export them was deleted at step 10. Living here, on their own, makes "the mint lives once" CHECKABLE in one grep
(`grep -rln "def H(" season/` prints exactly this file today). ⚠ That is a CONVENTION,
not an enforcement -- no test asserts it. Said plainly per S47: "a false claim of
enforcement is worse than none, because it stops the next reader from checking."
The property is also narrower than "hashing lives once": it covers the id MINT, not
hashing generally -- `World.content_hash` hashes too, and correctly."""

from __future__ import annotations

import hashlib


def H(world_seed: int, tick: int, subject_id: str, purpose: str) -> str:
    """S33/S49: an OWNED, VERSIONED mix -- never a language built-in hash(), whose value is not
    a cross-version contract. `purpose` must be unique per DRAW, not per operation."""
    return hashlib.blake2b(f"v1|{world_seed}|{tick}|{subject_id}|{purpose}".encode(),
                           # [JUSTIFIED: a HASH WIDTH, not a game value -- 8 bytes is 16 hex characters of id; nothing in the model reads it as a quantity]
                           digest_size=8).hexdigest()


ROOT = "ROOT"
