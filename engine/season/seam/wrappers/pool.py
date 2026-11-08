"""`seam/wrappers/pool.py` -- THE ONE POOL READER (CP-T01-01, moved out of `sigma.py` at B10-11).

`faculty` is read by the social contest (`sigma.py`, `contest_input` and `odds_of`) and, since CR-85, by combat
(`combat.py::combat_input`). `sigma.py` imports `combat.py` at module level (`fight_estimate`, `record_of`), so
`combat.py` importing `faculty` from `sigma.py` closed a two-module import cycle (`test_import_cycle_game_state_npe`
counts it). The reader lives here instead, a leaf both adapters import and neither is imported by: ONE OWNER, no copy.
`sigma.py` re-exports every name it moved, so a caller reaches `sigma.faculty` as before; a test that REPLACES
`POOL_ADDENDS` patches THIS module (the list `faculty` reads), not `sigma`'s binding of it.
"""
from __future__ import annotations

from typing import Any

from ...data.rosters import VERB_CAPABILITY, VOCATION_ATTRIBUTE, VOCATION_OPPOSED_BY
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
# reader. Holds the practice addend (CP-T01-02, the first reader of `w.log`, registered below `register_pool_addend`)
# and takes T07's; this is the place they land, so none grows its own pool rule. An addend reads
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
# `practice_cap` 0 is the control and answers 0 without reading the log, every pool then what it was before it was registered.
register_pool_addend(practice)


def _authored_attribute(entity: Any, verb: str):
    """The score `entity` HOLDS on the attribute the verb's vocation starts from (`rosters.yaml:
    vocation_attribute`; `Person.attributes`), or `None` where he holds none, the verb draws on no
    capability, or the entity is no person. The attribute's twin of `_capability`: a READ, never a default."""
    attr = VOCATION_ATTRIBUTE.get(VERB_CAPABILITY.get(verb))
    return (getattr(entity, "attributes", None) or {}).get(attr) if attr else None


def _opposing_attribute(entity: Any, verb: str):
    """The score `entity` HOLDS on the attribute that OPPOSES the verb's vocation (v10 CR-96, AR-44): the row's
    `opposed_by` where it has one, else the row's own attribute (so every row shipped absent reads as CR-20 landed
    it, and `_authored_attribute` is its twin). `None` where he holds none. The opposition's read only: `faculty`
    keeps the row's own attribute for the pool."""
    voc = VERB_CAPABILITY.get(verb)
    attr = VOCATION_OPPOSED_BY.get(voc) or VOCATION_ATTRIBUTE.get(voc)
    return (getattr(entity, "attributes", None) or {}).get(attr) if attr else None


def faculty(w: Any, p: Any, verb: str) -> int:
    """Dice, from what the actor genuinely has: THE ONE POOL READER. `03 §A.2` -- *"Rank supplies dice and
    gates nothing"*. Reached by `contest_input` (the dealt record) and by `odds_of` (the believer's own
    pool, which is known to him; `believed_input` takes it as an argument and has no World).

    `VERB_CAPABILITY` maps a verb to the capability key it draws on; `Person.capability` is the
    person's own dict, written by a `cast:` overlay and (v9 IN-12 step 9) `train`, which raises a key
    only a person already holds. v10 CR-20: WHERE HE HOLDS THE VOCATION'S ATTRIBUTE (`VOCATION_ATTRIBUTE`,
    `Person.attributes`) that score is the pool's base, and the pool is the LARGER of it and the capability
    key he holds (practice raises a key; it never takes dice from an attribute). WHERE HE HOLDS NONE the held
    key stands alone and `pool_default` is the fallback, exactly as before the carrier -- so a held 0 is still
    a person under one die (`test_odds_of.py`, `test_sc01_speak.py` pin it) and an all-absent realm rolls what
    it rolled. Then the registered addends (`POOL_ADDENDS`) are summed on.
    ⚠ `08 §3` GIVES THE POLARITY: an `assumption` grade means *inject the default, declare the site,
    sweep three points* -- never refuse the whole corpus for a missing key. `absent` is the grade
    that refuses, and this is not one."""
    have = _capability(p, verb)
    attr = _authored_attribute(p, verb)
    if attr is not None:
        base = int(attr) if have is None else max(int(attr), int(have))
    else:
        base = int(have if have is not None else w.fixtures.get("pool_default"))
    return base + sum(int(add(w, p, verb)) for add in POOL_ADDENDS)
