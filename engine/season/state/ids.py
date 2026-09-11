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


def draw_factory(world_seed: int, tick_of):
    """A per-person, per-purpose RNG, seeded from the SAME clock the mint uses (`U4`, `H-96`).

    ⚠ IT LIVES BESIDE `H` BECAUSE IT IS THE SAME OBJECT WEARING A SECOND FACE. `make_chooser`'s
    own docstring already argues why a clock-derived callable may cross into a person-side
    function: *"`mint` IS HERE BECAUSE §F2 TYPES `choose -> Act[]` AND GIVES THE PERSON NO WAY TO
    MINT ONE … the barrier passes a minter closed over the seed and tick, which are THE CLOCK, NOT
    ANYBODY'S INTERIOR. Same shape as `fx`, and the AST proof still sees no `World`."* Every word
    of that applies here unchanged, which is why this is a factory closed over the clock rather
    than an RNG handed around: a person cannot be given a stream, only a way to derive their own.

    ⚠ DETERMINISM IS PRESERVED, AND THAT IS NOT A SIDE NOTE — `m1_acceptance.py` row 2 is
    *"same seed -> same KeyLog.content_hash()"* and would fail on a wall-clock or process-entropy
    seed. Two runs of one world draw identical streams because the seed is `(world_seed, tick,
    pid, purpose)` and nothing else. What sampling removes is the ARGMAX, not the replay.

    ⚠ `purpose` IS PER DRAW, as `H`'s own contract states. Two different decisions by one person in
    one tick must pass different purposes or they share a stream.

    ⚠⚠ `tick_of` IS A CALLABLE, AND THAT IS THE WHOLE OF THE BUG IT PREVENTS. A caller that builds
    its chooser ONCE and runs it for N seasons — `harness/corpus_run.py`'s `run_case`, where `ch` is
    built before the season loop — would otherwise freeze the clock, and `mint` survives the same
    shape only because it is a lambda reading `w.tick` at CALL time.
    ⚠ ONE WORKED EXAMPLE IN THE FIRST WRITING OF THIS PARAGRAPH WAS WRONG AND IS CORRECTED RATHER
    THAN DROPPED: it named `headless.py:129` alongside `corpus_run.py:355`. **`headless` rebuilds
    the chooser INSIDE its season loop**, so a factory closed over an integer tick would be
    re-closed each season there and would NOT freeze. `corpus_run` is the real instance; `headless`
    was not one, and citing it overstated the hazard by exactly one call site. A factory
    closed over an integer tick would freeze the season: a person would draw the identical stream
    every season and take the identical choice forever, which reads as a plausible world and is an
    artifact of the seeding. `lambda: w.tick` puts the late binding at the call site where a reader
    can see the clock advance, rather than hiding it in a closure."""
    import random

    def draw(subject_id: str, purpose: str) -> "random.Random":
        # [JUSTIFIED: a RADIX, not a game value -- `H` returns `hexdigest()`, so 16 is how that string is read back as an integer; the same non-quantity as the `digest_size` above]
        return random.Random(int(H(world_seed, tick_of(), subject_id, purpose), 16))

    return draw
