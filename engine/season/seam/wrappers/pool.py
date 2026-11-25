"""`seam/wrappers/pool.py` -- THE ONE POOL READER (CP-T01-01).

`faculty` is read by the social contest (`sigma.py`, `contest_input` and `odds_of`); combat reads `score`, `addends_of` and `pool_pair`
(`combat.py::combat_input`, CR-85) and builds its own pool in the module. `combat.py` imports `sigma.py` (`ADVANTAGE_SOURCES`, `WOUNDS`) and `sigma.py` no longer imports `combat.py` at module
level, so the edge runs one way; the pool reader still lives here, a leaf both adapters import and neither is imported
by: ONE OWNER, no copy.
`sigma.py` re-exports the names it imports from here; a test that REPLACES
`POOL_ADDENDS` patches THIS module (the list `faculty` reads), not `sigma`'s binding of it.
"""
from __future__ import annotations

from typing import Any

from engine.dice_engine.sigma_leverage import governing_mean, pool_of
from engine.substrate import descriptors

from ...data.rosters import capability_rows, require_use_site
from ...data.verbs import VERB_CAPABILITY, VERB_TABLE
from ...gaps import Forbidden, Unspecified
from ...queries.world_q import practice


def _capability(entity: Any, verb: str):
    """What `entity` brings to `verb`'s capability key, or `None` if it brings nothing.

    ⚠ ONE READ, TWO CALLERS. `faculty` and `_opposition_of` each map the verb through
    `VERB_CAPABILITY`, guard a missing key, and guard a missing entry — the same three steps,
    differing only in WHOSE dict they read and what default they fall to. Those differences are the
    callers'; the read is not. Returning `None` rather than a default is what keeps it that way:
    the pool falls to `pool_default`, and the opposition's `None` reaches the module, which falls
    to `opposed_ob(pool_default)`; neither is this function's to know."""
    key = VERB_CAPABILITY.get(verb)
    if not key:
        return None
    return (getattr(entity, "capability", None) or {}).get(key)


# THE POOL'S ADDENDS (CP-T01-01): each `(w, person, verb) -> int` is summed into `faculty`, the one pool
# reader. Holds the practice addend (CP-T01-02, the first reader of `w.log`, registered below `register_pool_addend`);
# this is the place addends land, so none grows its own pool rule. An addend reads
# only what it is handed (`w`, the actor, the verb) and returns whole dice; it never replaces the
# capability read, it adds to it.
POOL_ADDENDS: list = []


def register_pool_addend(fn: Any) -> None:
    """Add `fn(w, person, verb) -> int` to what `faculty` sums. Registered once, at import of its owner; a
    second registration of the same function is a no-op (an addend counts once however often its owner registers it)."""
    if fn not in POOL_ADDENDS:
        POOL_ADDENDS.append(fn)


# THE PRACTICE ADDEND (CP-T01-02), `faculty`'s first reader of `w.log`: registered here, the one door into the
# pool, and called from nowhere else. Its reader is `queries/world_q.py::practice`; the arm ships live (CR-18);
# `practice_cap` 0 is the control and answers 0 without reading the log.
register_pool_addend(practice)


def _held_attribute(entity: Any, attr):
    """The score `entity` holds on attribute `attr` (`Person.attributes`), or `None` where `attr` is none, he holds
    none, or the entity is no person. The one read `governing_attribute` and `governing_score` end in."""
    return (getattr(entity, "attributes", None) or {}).get(attr) if attr else None


def governing_attribute(entity: Any, verb: str):
    """(B05.25) The FIRST of `verb`'s `governing:` attributes (`verb_table.yaml`) AS HELD (`Person.attributes`), else `None` --
    `None` where he holds none, the row names none (a brute or a subsystem row) or the entity is no person. A READ, never a
    default (B05.16): `None` is an unheld value, which the opposition reads as the mid-point (`opposing_attribute`) and the pool, through
    `governing_score`, as the untrained score."""
    row = VERB_TABLE.get(verb)
    return _held_attribute(entity, row.governing[0] if row is not None and row.governing else None)




def governing_score(w: Any, p: Any, verb: str) -> float:
    """(B05.25; B05.24's rule, Jordan 2026-11-13) HIS GOVERNING SCORE FOR `verb`: the mean (`sigma_leverage.governing_mean`: to
    the nearest tenth, a half up, a FRACTIONAL number) of his scores in the verb's one to three `governing:` attributes, an
    attribute he does not hold counting at the untrained score (`untrained`). Refused (`Forbidden`) for a brute verb and for a verb that
    proceeds (B24p.19: `faculty` reads this, so the pool reader refuses it naming the verb), and (`Unspecified`) for a row naming no
    attribute: none of the three is pooled here."""
    row = VERB_TABLE.get(verb)
    if row is not None and row.brute:
        raise Forbidden(f"{verb!r} is a brute verb (`brute: {row.brute}`) and never rolls; it has no governing score",
                        "seam/wrappers/pool.py", needs="a verb row with `governing:`",
                        law="B05.24 -- a brute function is authorised, gated or recorded and does not roll at all")
    if row is not None and row.proceeds:
        raise Forbidden(f"{verb!r} proceeds (`proceeds:`, B24p.16) and is never pooled here: its dice are the proceeding's own, drawn by "
                        f"`social_contest.proceeding` from the six attributes of the room",
                        "seam/wrappers/pool.py", needs="a verb row with `governing:`",
                        law="B24p.19, RD §D.3 -- a verb that opens a proceeding names no governing attribute; the pool reader is the single roll's")
    if row is None or not row.governing:
        raise Unspecified(f"{verb!r} names no `governing:` attribute; its act is a subsystem's (`person_inputs: own`) or the verb is no row",
                          "seam/wrappers/pool.py", needs="a verb row with `governing:`",
                          law="B05.24 -- a verb that hands its act to a subsystem names none and the subsystem reads him by its own rule")
    default = untrained(w.fixtures)
    return governing_mean([default if (held := _held_attribute(p, a)) is None else held for a in row.governing])


def attribute_midpoint() -> float:
    """THE ATTRIBUTE SCALE'S MID-POINT, `(ATTRIBUTE_FLOOR + ATTRIBUTE_CEILING) / 2` (4 on 1-7): what the OPPOSITION reads for an
    attribute a person holds no value on (B05.16; U1 §4). Neither above nor below it: zero levels either way. Derived, never stored."""
    return (descriptors.ATTRIBUTE_FLOOR + descriptors.ATTRIBUTE_CEILING) / 2


def opposing_attribute(fx: Any, p: Any, verb: str):
    """(B05.14, B05.16; A-79, A-137) THE ATTRIBUTE A PERSON RESISTS `verb` WITH, AS HE HOLDS IT: his score in the verb row's `opposed_attribute:`,
    read at the scale's MID-POINT (`attribute_midpoint`) where he holds none (`_held_attribute` is `None`: a hand-built world's person; every
    realm person holds all ten after B01a), and `None` where the row names none (an inquiry nobody resists by a trait). So an authored
    character is easier to oppose than an unauthored one only by being authored low. The one read the obstacle's `opposition` member
    adds to his skill score (`score`); the pool reads his OWN attributes through `governing_score`, where an unheld one counts at the
    untrained score (`untrained`), never this. `fx` is kept for the caller's signature."""
    row = VERB_TABLE.get(verb)
    key = row.opposed_attribute if row is not None else None
    if key is None:
        return None
    held = _held_attribute(p, key)
    return attribute_midpoint() if held is None else held


def rank(p: Any, verb: str) -> int:
    """(B05.25) HIS HELD RANK in `verb`'s skill (`_capability`), `0` where he holds none or the row names no skill: an untrained
    man rolls on his attributes alone, and a first rank always adds a die."""
    have = _capability(p, verb)
    return 0 if have is None else have


def faculty(w: Any, p: Any, verb: str) -> float:
    """Dice, from what the actor genuinely has: THE ONE POOL READER. `03 §A.2` -- *"Rank supplies dice and
    gates nothing"*. Reached by `contest_input` (the dealt record) and by `odds_of` (the believer's own
    pool, which is known to him; `believed_input` takes it as an argument and has no World).

    THE POOL IS `pool_of` (A-6, D-U1-08, B05.25): `pool_of(governing_score + rank, addends, pool_add, pool_floor)`, the one rule
    of how the verb's governing score (the mean of his scores in its `governing:` attributes, FRACTIONAL: 2.5, not 3), his rank in
    the verb's skill, the registered addends (`POOL_ADDENDS`, whole dice) and the base and floor the `social_roll` `dice` row names
    (`add: pool_add`, `floor: pool_floor`, B05.10; each 0 at control) make a pool. A first rank adds a die; a person holding no attribute and no rank rolls
    `pool_default`. The opposition does not read this: it reads the opponent's skill score (`score`, B05.11) plus his opposing
    attribute (`opposing_attribute`, B05.14), which `sigma.py::OBSTACLE_TERMS["opposition"]` adds and `roll.py::obstacle` reads at
    `opposed_ob` (A-137).
    A brute verb never reaches here (`Forbidden`), nor does a row naming no attribute (`Unspecified`): a (c) row reaches its
    module, which reads `score` and `addends` as two numbers (`seam/wrappers/combat.py::combat_input`, B05.57).
    ⚠ `08 §3` GIVES THE POLARITY: an `assumption` grade means *inject the default, declare the site,
    sweep three points* -- never refuse the whole corpus for a missing key. `absent` is the grade
    that refuses, and this is not one."""
    add, floor = pool_pair(w.fixtures)
    return pool_of(governing_score(w, p, verb) + rank(p, verb), addends_of(w, p, verb), add, floor)


#: `rosters.yaml: capability_use_sites`' site whose `dice` row names the pool's base and floor (B05.10, MAP §G edit 4).
_DICE_SITE = require_use_site("social_roll")


#: The fight's own `dice` row names the same pair (`rosters.yaml: capability_uses`); `combat.py::combat_input` reads it through `pool_pair`.
FIGHT_DICE_SITE = require_use_site("fight")


def pool_pair(fx: Any, site: str = _DICE_SITE) -> tuple:
    """`(pool_add, pool_floor)` as `site`'s (the `social_roll` site's, unless given) `dice` row names them (`add:`, `floor:`: Fixture NAMES, read from `fx`),
    so swapping the names in the row swaps what the pool reads, with no code edit. A row naming neither (or no `dice` row) reads
    `(0, 0)`: the control, where the pool is `governing score + rank + addends`. Read by `faculty` and, for the
    obstacle's `even` term, by `sigma.py::OBSTACLE_TERMS` -- the base that makes the pool is the base whose line the obstacle starts at."""
    row = next((r for r in capability_rows(site) if r.role == "dice"), None)
    return (0 if row is None or row.add is None else fx.get(row.add),
            0 if row is None or row.floor is None else fx.get(row.floor))


def addends_of(w: Any, p: Any, verb: str) -> int:
    """The registered addends (`POOL_ADDENDS`) summed, whole dice: the one sum, read by `faculty` and by `combat_input` (which
    carries it beside the skill score as `PersonalCombatInput.addends`; the module applies its own row's two operands, MAP §G edit 4)."""
    return sum(int(add(w, p, verb)) for add in POOL_ADDENDS)


def score(w: Any, p: Any, verb: str) -> "int | None":
    """(W3-1, A-7, 7b-6) WHAT `p` IS TRAINED IN FOR `verb`'s SKILL: the held rank, never below the untrained score
    `pool_default` (CORE Edit 9: a first rank is never a loss), else the untrained score. `None` where the row says
    `untrained: none` and he holds no rank. No attribute (the governing attribute enters the dice through `governing_score`,
    B05.25; the attribute is a level, not a score, A-7; B05.11 deleted the opposition's `attribute=` read) and no addend
    (practice raises a pool, never an opposition). The score an opponent's `opposed_ob` reads (`sigma.py::_opposition_of`),
    and the rank `faculty` reads through `rank`."""
    have = _capability(p, verb)
    default = untrained(w.fixtures)
    if have is not None:
        return max(default, int(have))
    row = descriptors.CAPABILITIES.get(VERB_CAPABILITY.get(verb))
    return None if row is not None and row.untrained == "none" else default


def untrained(fx: Any) -> int:
    """THE UNTRAINED SCORE: what a person brings to a vocation he holds nothing on, `Fixtures pool_default` (H-126) --
    `score`'s fallback, read here once. On a verb that names NO vocation (no `verb_capability` row: `lie`) nobody can hold
    a key or an attribute for it, so this is EVERY person's score there, and a believer knows it without asking anyone
    (`sigma.believed_input` reads it for a person he opposes on such a verb, so the odds he weighs are the odds dealt)."""
    return int(fx.get("pool_default"))
