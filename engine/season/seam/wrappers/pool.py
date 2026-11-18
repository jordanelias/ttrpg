"""`seam/wrappers/pool.py` -- THE ONE POOL READER (CP-T01-01).

`faculty` is read by the social contest (`sigma.py`, `contest_input` and `odds_of`) and, CR-85, by combat
(`combat.py::combat_input`). `sigma.py` imports `combat.py` at module level (`fight_estimate`, `record_of`), so
`combat.py` importing `faculty` from `sigma.py` would close a two-module import cycle (`test_import_cycle_game_state_npe`
counts it). The reader lives here, a leaf both adapters import and neither is imported by: ONE OWNER, no copy.
`sigma.py` re-exports the names it imports from here; a test that REPLACES
`POOL_ADDENDS` patches THIS module (the list `faculty` reads), not `sigma`'s binding of it.
"""
from __future__ import annotations

from typing import Any

from engine.dice_engine.sigma_leverage import pool_of
from engine.substrate import descriptors

from ...data.verbs import VERB_CAPABILITY, VOCATION_ATTRIBUTE, VOCATION_OPPOSED_BY
from ...queries.world_q import practice


def _capability(entity: Any, verb: str):
    """What `entity` brings to `verb`'s capability key, or `None` if it brings nothing.

    ⚠ ONE READ, TWO CALLERS. `faculty` and `_opposition_of` each map the verb through
    `VERB_CAPABILITY`, guard a missing key, and guard a missing entry — the same three steps,
    differing only in WHOSE dict they read and what default they fall to. Those differences are the
    callers'; the read is not. Returning `None` rather than a default is what keeps it that way:
    the pool falls to `pool_default`, and the opposition's `None` reaches the module, which falls
    to `obstacle_default`; neither is this function's to know."""
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
    none, or the entity is no person. The one read `_authored_attribute` and `_opposing_attribute` end in."""
    return (getattr(entity, "attributes", None) or {}).get(attr) if attr else None


def governing_attribute(entity: Any, verb: str):
    """(CAP B1, U1 §4) The governing attribute of `verb`'s skill AS HELD (`rosters.yaml: vocation_attribute`;
    `Person.attributes`), else `None` -- read as the scale's mid-point where a reader needs a number
    (`(descriptors.ATTRIBUTE_FLOOR + descriptors.ATTRIBUTE_CEILING) / 2`, derived, never stored). `None` too where the verb
    draws on no skill or the entity is no person. The attribute's twin of `_capability`: a READ, never a default. The pool no
    longer reads it (the skill score has no attribute in it, A-7); the opposition does, through `_opposing_attribute`."""
    attr = VOCATION_ATTRIBUTE.get(VERB_CAPABILITY.get(verb))
    return _held_attribute(entity, attr)


_authored_attribute = governing_attribute   # B05.09: the name its remaining readers (tests, `sigma.py`'s re-export) still use


def _opposing_attribute(entity: Any, verb: str):
    """The score `entity` HOLDS on the attribute that OPPOSES the verb's vocation (v10 CR-96, AR-44): the row's
    `opposed_by` where it has one, else the row's own attribute (so every row shipped absent reads as CR-20 landed
    it, and `_authored_attribute` is its twin). `None` where he holds none. The opposition's read only: `faculty`
    keeps the row's own attribute for the pool."""
    voc = VERB_CAPABILITY.get(verb)
    attr = VOCATION_OPPOSED_BY.get(voc) or VOCATION_ATTRIBUTE.get(voc)
    return _held_attribute(entity, attr)


def faculty(w: Any, p: Any, verb: str) -> int:
    """Dice, from what the actor genuinely has: THE ONE POOL READER. `03 §A.2` -- *"Rank supplies dice and
    gates nothing"*. Reached by `contest_input` (the dealt record) and by `odds_of` (the believer's own
    pool, which is known to him; `believed_input` takes it as an argument and has no World).

    THE POOL IS `pool_of` (A-6, D-U1-08, B05.09): `pool_of(score, addends, pool_add, pool_floor)`, the one rule of how a skill
    score, the registered addends (`POOL_ADDENDS`, whole dice) and the row's base and floor (`Fixtures pool_add`, `pool_floor`,
    each 0 at control) make a pool. `score` has no attribute in it (A-7): the governing attribute enters the dice through
    `governing_score` (B05.25), and the opposing attribute enters the opposition beside the skill score,
    `opposed_ob(opposing attribute + skill score)` (B05.14, A-137). A held 0 is no longer a person under one die: the score is
    `max(untrained score, rank)`, so a first rank never lowers a pool.
    A skill whose row says `untrained: none` gives a non-holder NO score (`score` is `None`): his pool is 0, the roll refused as
    a held 0 was (S27.4); no floor lifts a refusal.
    ⚠ `08 §3` GIVES THE POLARITY: an `assumption` grade means *inject the default, declare the site,
    sweep three points* -- never refuse the whole corpus for a missing key. `absent` is the grade
    that refuses, and this is not one."""
    base = score(w, p, verb)
    if base is None:
        return 0
    return pool_of(base, addends_of(w, p, verb), w.fixtures.get("pool_add"), w.fixtures.get("pool_floor"))


def addends_of(w: Any, p: Any, verb: str) -> int:
    """The registered addends (`POOL_ADDENDS`) summed, whole dice: the one sum, read by `faculty` and by `combat_input` (which
    applies its own row's two operands and receives `score + addends`, MAP §G edit 4)."""
    return sum(int(add(w, p, verb)) for add in POOL_ADDENDS)


def score(w: Any, p: Any, verb: str, attribute: Any = None) -> "int | None":
    """(W3-1, A-7, 7b-6) WHAT `p` IS TRAINED IN FOR `verb`'s SKILL: the held rank, never below the untrained score
    `pool_default` (CORE Edit 9: a first rank is never a loss), else the untrained score. `None` where the row says
    `untrained: none` and he holds no rank. No attribute (the governing attribute enters the dice through `governing_score`,
    B05.25) and no addend (practice raises a pool, never an opposition). The base of his pool AND the score an opponent's
    `opposed_ob` reads (`sigma.py::_opposition_of`). `attribute` (B01's parameter, kept until B05.11): the opposition's read
    only -- `_opposing_attribute` (v10 CR-96), the larger of that attribute and the rank, as B01 shipped it; the pool passes
    none and reads no attribute."""
    have = _capability(p, verb)
    if attribute is not None and (attr := attribute(p, verb)) is not None:
        return int(attr) if have is None else max(int(attr), int(have))
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
