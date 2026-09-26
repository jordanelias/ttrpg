"""engine.substrate.names — canonical naming, read from references/. One owner for a TERM.

Status: [live, 2026-09-16]

WHY. `references/names_index.yaml` has called itself *"the one place a definition's name lives"*
since 2026-06-28, and for executable code it was not. MEASURED: one arrow reached runtime --
`engine/season/data/cast.py`, which opened the YAML itself and built a private alias map over
`token_class: faction` rows. `alias_registry`'s two apparent reads in `descriptors.py` are a
COMMENT and a DOCSTRING. Nothing under `systems/` read any naming register at all, which is why a
ruling could land in `references/` and never arrive: `systems/world/sim/npe.py` was still minting
NPCs affiliated to `'Church'` after Jordan ruled the name is `Church of Solmund`.

`tools/export_names.py` cooks the index into `engine/engine_params/names.json` behind a blocking
`--check`; this is its single runtime reader. Same shape as `descriptors.py`, `composition.py`
and `world_initial_state.py`.

IT IS A LEAF. This MODULE imports stdlib only -- `json`, `os` -- exactly as
`world_initial_state.py` does, verified by AST rather than asserted. That is what lets BOTH trees
read it without either naming the other: a name propagates in one direction, from the authored
index outward, and a subsystem wanting the canonical spelling asks instead of spelling it.

⚠ THE PACKAGE `__init__.py` USED TO NOT BE A LEAF, AND THE DISTINCTION MATTERED WHILE IT LASTED.
Until 2026-09-16 it imported `keys.py` and re-exported it, so `import engine.substrate.names`
pulled `keys` and `descriptors` in with it. `keys.py` retired under ED-IN-0232 and the re-export
went with it -- `engine/substrate/__init__.py` now imports nothing. `from engine.substrate.names
import FACTIONS` costs exactly what it names; it is not a hidden dependency edge.

⚠ AMBIGUOUS NAMES RAISE. They are not resolved to whichever row was met first. Two display strings
are claimed twice in the index and both collisions are real quantities, not typos:

    Order      -- `conv.order` (a Conviction) and `set.order` (a settlement stat)
    Stability  -- `fac.stability` (a 0-7 faction stat) and `mech.stability` (a mechanic)

`canonical_for()` refuses both and names the claimants. The index's `context:` field disambiguates
these for PROSE matching (the §3.5 gate `vector_audit` reads) but says nothing about which row owns
the string, so there is no answer to give a caller -- and inventing one is the silent-wrong-value
this module exists to stop. Pass the KEY (`'set.order'`) when you mean a specific one.
"""
from __future__ import annotations

import json
import os

_HERE = os.path.dirname(os.path.abspath(__file__))
_PATH = os.path.normpath(os.path.join(_HERE, '..', 'engine_params', 'names.json'))

with open(_PATH, encoding='utf-8') as _fh:
    _DATA = json.load(_fh)

#: {key -> canonical display string}, e.g. `'fac.influence' -> 'Influence'`.
CANONICAL = _DATA['canonical']

#: {alias -> canonical}. An alias is an ALLOWED equivalent phrasing, never a deprecation.
ALIASES = _DATA['aliases']

#: {legacy tag -> canonical}. A legacy tag must NOT appear in active docs; it is here so a reader
#: meeting one can find out what replaced it, not so it keeps resolving.
LEGACY = _DATA['legacy']

#: {token_class -> (canonical, ...)}. `FACTIONS = BY_CLASS['faction']` is the roster
#: `engine/season/rosters.yaml: factions` derives from rather than copying.
BY_CLASS = {k: tuple(v) for k, v in _DATA['by_class'].items()}

#: Display strings more than one entry claims. See the module docstring.
AMBIGUOUS = _DATA['ambiguous']

#: The faction roster. Read this instead of spelling a faction name.
#: ⚠ ITS SIZE IS NOT AN INVARIANT and no caller may assume one (RULED by Jordan, 2026-09-19:
#: *"faction count should not be pinned"*). It grows when the world does, and it carries test
#: fixtures — `faction x`, the generic governance ladder's — alongside canon. Membership is the
#: question to ask it; a length is not.
FACTIONS = BY_CLASS.get('faction', ())


def canonical_for(name: str) -> str:
    """`name` resolved to its canonical spelling, whether it arrives canonical or as an alias.

    RAISES rather than guessing, in three cases, and each raise is a defect in the caller:
      · an ambiguous display string -- two rows claim it, so there is no answer;
      · a legacy tag -- it names what replaced it, because resolving a deprecation silently is how
        a rename never finishes;
      · an unknown name -- the same polarity `descriptors.resolve_conviction` uses, and for its
        reason: a silent pass-through made a wrong name indistinguishable from a right one.
    """
    if name in AMBIGUOUS:
        raise ValueError(
            f'{name!r} is claimed by more than one entry ({", ".join(AMBIGUOUS[name])}), so it '
            f'does not resolve to one definition. Pass the KEY of the one you mean.')
    if name in ALIASES:
        return ALIASES[name]
    if name in LEGACY:
        raise ValueError(
            f'{name!r} is a LEGACY name, replaced by {LEGACY[name]!r}. It is carried here so the '
            f'rename can be finished, not so it keeps resolving -- use the replacement.')
    if name in CANONICAL:            # a key was passed
        return CANONICAL[name]
    if name in set(CANONICAL.values()):
        return name                  # already canonical
    raise ValueError(
        f'unknown name {name!r}. The owner is references/names_index.yaml, cooked by '
        f'tools/export_names.py and read here. If this is a new term, add the row; do not add a '
        f'local alias, which gives the name a second owner.')


def of_class(token_class: str) -> tuple:
    """Every canonical name carrying `token_class`, as a tuple. Unknown class -> empty tuple, which
    is deliberate: asking for a class nobody declared is not an error, it is an empty roster."""
    return BY_CLASS.get(token_class, ())
