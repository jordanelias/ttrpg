"""engine.substrate.descriptors — the SOLE runtime reader of the descriptor registry.

Status: [live, 2026-08-20]

WHY THIS EXISTS. `systems/` stems from `engine/` and `references/` (Jordan, 2026-08-20). Measured
the same day, `references/` was load-bearing on tools and prose ONLY: no module under `engine/` or
`systems/` loaded `references/descriptor_registry.yaml` — every runtime hit across both trees was a
comment or a docstring — while the rosters the code actually runs on were hardcoded twins in
`engine/autoload/game_state.py`. A registry nothing executes is a document, not a root.

This module is the reader that makes it a root. It loads the COOKED artifact
`engine/engine_params/descriptors.json` (written by `tools/export_descriptors.py`, blocking
`--check`), never the YAML: the same discipline as `keys.py` vs `key_types.json` — the authored
surface stays reviewable, code reads the cooked one, and one exporter owns the parse.

IT IS A LEAF, DELIBERATELY. stdlib only, no `engine.*` or `systems.*` imports, so anything may
depend on it without creating a cycle. It reads the file once, at import.

THE FACTION BLOCK WAS RETIRED AT PLAN POSITION `29b` (2026-10-01). This module used to expose
`FACTION_STATS`, `FACTION_FIELD_MAP`, `faction_bounds()` (the clamp `Faction.adjust` read) and
`assert_faction_roster_is_covered()` (the import-time check in `game_state.py`). Their only reader,
`engine/autoload/game_state.py::Faction`, is deleted, and the six `fac.*` rows left the registry with
it (`ID-13`: a declared field that reaches no reader is not declared). The rulings that shaped them are
in git at `5c5d8ec6:references/descriptor_registry.yaml`.
"""
from __future__ import annotations

import json
import os

_HERE = os.path.dirname(os.path.abspath(__file__))
_PATH = os.path.normpath(os.path.join(_HERE, '..', 'engine_params', 'descriptors.json'))


def _load():
    with open(_PATH) as fh:
        return json.load(fh)


_DATA = _load()

#: Registry version/date the loaded artifact was cooked from — carried so a caller can report
#: provenance without re-reading the YAML.
REGISTRY_VERSION = _DATA.get('registry_version', '')
REGISTRY_RATIFIED = _DATA.get('registry_ratified', '')

#: Character attribute roster, in registry order. NOTE: Jordan ruled 2026-08-14 that this WILL BE
#: ten; the registry ships nine and the tenth is unnamed. `ATTRIBUTES_PENDING_TENTH` is non-None
#: while that is true, so a reader cannot mistake the current roster for a closed one.
ATTRIBUTES = tuple(_DATA['attributes']['roster'])
ATTRIBUTES_PENDING_TENTH = _DATA['attributes'].get('pending_tenth')
ATTRIBUTE_FLOOR = _DATA['attributes']['scale']['floor']
ATTRIBUTE_CEILING = _DATA['attributes']['scale']['ceiling']

#: {registry key -> {name, floor, ceiling}} for each declared domain.
SETTLEMENT_STATS = _DATA['settlement_stats']
PRACTITIONER_STATS = _DATA['practitioner_stats']
TERRITORY_STATS = _DATA['territory_stats']

#: Ratified decisions the executable model has not implemented. Each names what it needs.
UNIMPLEMENTED = _DATA['unimplemented']


def block(name: str) -> dict:
    """One registry block by name, e.g. `block('pursuit_roster')`. THE PUBLIC WAY IN.

    ⚠ `engine/season/data/rosters.py`'s `from_descriptor:` pointer reached `_DATA` directly, via
    `getattr(_desc, "_DATA", {})`. Two things were wrong with that. `_DATA` is underscore-private
    and carries no compatibility contract, so renaming or wrapping it is a legal refactor here --
    and the `{}` default turned that refactor into a LIE: every pointed-at roster would raise
    *"points at descriptor block 'pursuit_roster', which is absent or has no `names`"*, sending
    the next session to edit `references/descriptor_registry.yaml`, which would be perfectly
    correct and completely unrelated to the actual cause.

    Returning `{}` for an unknown name is deliberate and is NOT that default: the caller's own
    refusal reads better than one raised from here, because it names the roster that pointed and
    the exporter to re-run. What this removes is the silent-`{}`-on-RENAME, not the empty answer
    for a name nobody declared.
    """
    return _DATA.get(name) or {}


# ---------------------------------------------------------------------------
# PURSUITS — added 2026-08-24. THIS IS THE ONLY PURSUIT ROSTER IN THE ENGINE.
# ---------------------------------------------------------------------------
# ⚠ THE FIFTEEN (IN-08's cells commit, ED-IN-0261): the roster this leaf reads is
# `references/descriptor_registry.yaml: pursuit_roster`. What follows is the history of why there is
# one roster at all, and it holds for the fifteen exactly as it held for the thirteen it replaced.
# Before this, three incompatible rosters shipped: nine names in
# `systems/characters/sim/conviction.py`, eight in `systems/world/sim/npe.py` (overlapping the
# first in three), and thirteen registered `by_reference` in `references/descriptor_registry.yaml`
# with a 13x4 axis map bound to them. The two CODE rosters were nearly disjoint, and the gap was
# not cosmetic: `systems/fieldwork/sim/knots.py` scarred `conviction='Loyalty'` — a name only npe
# knew — so ED-912 §6.1's Close-Knot-break Scar hit an unknown-name branch and returned
# magnitude=0 forever while the caller reported `consequences['conviction_scar'] = 1`.
#
# The registry wins, and not by preference: it is the surface the axis matrix, the contest styles
# and the cultural-background templates already resolve `conv.*` through, so any other choice
# would have left the 13x4 matrix keyed on names no code could produce. Its thirteen are now
# ENUMERATED there (they were registered by reference only) and cooked into the artifact, so the
# names exist in one place and every consumer reads THEM.
#
# ⚠ THIS TUPLE IS NOT A SUPERSET OF WHAT IT REPLACED. Three of conviction.py's nine (Reason,
# Autonomy, Continuity) and five of npe's eight (Justice, Survival, Loyalty, Truth, Power) are not
# canonical names. `CONVICTION_ALIASES` below carries the two that have an unambiguous canonical
# twin; the rest are gone, and a caller passing one now raises instead of silently scoring zero.
PURSUITS = tuple(_DATA['pursuit_roster']['names'])

# ---------------------------------------------------------------------------
# ETHICAL AXES — centralized 2026-09-14 (ED-IN-0230). THE ONLY AXIS ROSTER IN THE ENGINE.
# ---------------------------------------------------------------------------
# `keys.py::AXES` held one literal and `engine/season/rosters.yaml: conviction_axes` held another,
# and NOTHING compared them — while the roster's own note claimed "a fifth axis or a rename is one
# edit there and a loader refusal here rather than two rosters drifting apart". MEASURED by AST on
# 2026-09-14: exactly one module in the tree imports `AXES`, and it is `engine/substrate/__init__`
# re-exporting it. Nothing under `engine/season/` reads it. So the two literals could disagree in
# either direction with no refusal on either side — a fifth axis in `keys.py` alone left the season
# engine scoring on four, and one in the roster alone left `keys.py` invariant 6 rejecting every
# Key that named it.
#
# This is the PURSUITS move above, applied one level up, and it is the tree's own precedent for
# this exact object rather than a new decision. Seven bipolar names since IN-08 (ED-IN-0261);
# `AXIS_SCALE` carries the sign convention as data (negative = the first-named pole).
AXES = tuple(_DATA['axis_roster']['names'])
AXIS_SCALE = _DATA['axis_roster'].get('scale', '')

# ---------------------------------------------------------------------------
# AFFILIATIONS — IN-08 H10 (ED-IN-0251 R1/R2). THE ONLY AFFILIATION ROSTER IN THE ENGINE.
# ---------------------------------------------------------------------------
# `Person.conviction` is `{affiliation: intensity}` over these names, each intensity an int inside
# `[AFFILIATION_FLOOR, AFFILIATION_CEILING]`; the ceiling is "full intensity". The pursuits' move,
# made a third time: one roster in `references/descriptor_registry.yaml`, exported behind the
# blocking `--check` (which validates the scale), read here.
AFFILIATIONS = tuple(_DATA['affiliation_roster']['names'])
AFFILIATION_FLOOR = _DATA['affiliation_roster']['scale']['floor']
AFFILIATION_CEILING = _DATA['affiliation_roster']['scale']['ceiling']

# ⚠ THERE IS NO ALIAS MAP, AND ITS REMOVAL IS THE POINT (corrected 2026-08-24, same day it was
# added, by an adversarial pass). This module briefly carried
# `CONVICTION_ALIASES = {'Reason': 'Scholastic', 'Autonomy': 'Liberty'}`, justified in a comment as
# "a rename rather than a design call". TWO AUTHORED SURFACES EXPLICITLY REFUSE THAT MAPPING:
#
#   systems/characters/conviction_taxonomy_v30.md:282
#       | Reason (legacy tag) | composite — see PP-685 per character |
#   references/alias_registry.yaml:653-658
#       legacy: [... 'Reason (legacy tag)', 'Continuity (legacy tag)'] with NO canonical target,
#       note: "Per-character migration in PP-685 / conviction_migration_roster_v30."
#
# Reason is a COMPOSITE that migrates per character; collapsing it to Scholastic at runtime decides
# a migration the corpus deliberately left open — and only *Epistemic* Reason maps primarily to
# Scholastic, "+ (situational; some Utility)" (taxonomy_v30.md:279). `Autonomy` appears in neither
# surface at all. So the alias map was inventing exactly the canon the comment beside it claimed to
# refuse for Survival and Power, and it is gone: every non-canonical name now raises, and the error
# names the migration rather than guessing its outcome.
def resolve_pursuit(name):
    """`name` if it is a canonical pursuit, else raise ValueError. Nothing is translated.

    THE RAISE IS THE POINT. The bug this module closes was a *silent* one — an unknown name scored
    magnitude=0 and no caller could tell the difference between "this Scar was capped" and "this
    pursuit does not exist". A wrong name is a defect in the caller, so it is loud here.
    """
    if name in PURSUITS:
        return name
    raise ValueError(
        f'unknown pursuit {name!r}. The roster is owned by '
        'references/descriptor_registry.yaml:pursuit_roster and read here; the canonical '
        f'{len(PURSUITS)} are: ' + ', '.join(PURSUITS) + '. If this is a name from the retired '
        'thirteen-Conviction roster or an older LEGACY tag, it has no automatic successor: the '
        'per-character migration is authored in references/npc_registry.yaml and the role '
        'templates in engine/season/rosters.yaml. Do the migration, or fix the caller; do not add '
        'a local alias, which decides that migration by accident.'
    )
