"""S33 -- DETERMINISM. The mint (`H`) and its sentinel (`ROOT`), extracted from `shape.py`
(step 1 of the shape.py decomposition, ED-IN-0202) with no behaviour change. `shape.py`
re-exports both, so `from ..shape import H, ROOT` and `S.H(...)` keep resolving exactly as
before. Living here, on their own, makes "the mint lives once" a one-file, one-`grep`
property (`grep -rln "def H(" season/` must print exactly this file)."""

from __future__ import annotations

import hashlib


def H(world_seed: int, tick: int, subject_id: str, purpose: str) -> str:
    """S33/S49: an OWNED, VERSIONED mix -- never a language built-in hash(), whose value is not
    a cross-version contract. `purpose` must be unique per DRAW, not per operation."""
    return hashlib.blake2b(f"v1|{world_seed}|{tick}|{subject_id}|{purpose}".encode(),
                           digest_size=8).hexdigest()


ROOT = "ROOT"
