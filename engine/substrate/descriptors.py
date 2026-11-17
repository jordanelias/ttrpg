"""engine.substrate.descriptors — the SOLE runtime reader of the descriptor registry.

Status: [live, 2026-08-20]

WHY THIS EXISTS. `systems/` stems from `engine/` and `references/` (Jordan, 2026-08-20). A
registry nothing executes is a document, not a root; this module is the reader that makes
`references/descriptor_registry.yaml` a root. It loads the COOKED artifact
`engine/engine_params/descriptors.json` (written by `tools/export_descriptors.py`, blocking
`--check`), never the YAML: the authored surface stays reviewable, code reads the cooked one, and
one exporter owns the parse.

IT IS A LEAF, DELIBERATELY. stdlib only, no `engine.*` or `systems.*` imports, so anything may
depend on it without creating a cycle. It reads the file once, at import.

There is no faction block (`ID-13`: a declared field that reaches no reader is not declared).
"""
from __future__ import annotations

import json
import os
from dataclasses import dataclass
from types import MappingProxyType
from typing import Mapping, Optional, Tuple

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

#: Character attribute roster, in registry order. Jordan ruled 2026-08-14 that this is ten and named
#: them in ED-IN-0328 (CR-84). `ATTRIBUTES_PENDING_TENTH` is None at ten; it is non-None whenever the
#: registry ships fewer, so a reader cannot mistake a short roster for a closed one.
ATTRIBUTES = tuple(_DATA['attributes']['roster'])
ATTRIBUTES_PENDING_TENTH = _DATA['attributes'].get('pending_tenth')
ATTRIBUTE_FLOOR = _DATA['attributes']['scale']['floor']
ATTRIBUTE_CEILING = _DATA['attributes']['scale']['ceiling']
#: `{lowercased name | alias | key: key}` over the ten (CR-20), cooked by the exporter from the registry's
#: resolver: the cast's legacy spellings (`cognition`) resolves here. A retired attribute's names are absent.
ATTRIBUTE_NAMES = _DATA['attributes']['names']


def attribute_key(name):
    """The roster key a name, alias or key spells, or `None` if it is none of the ten (a retired attribute's
    names included). Case-insensitive. A READ: the caller decides whether `None` refuses."""
    return ATTRIBUTE_NAMES.get(str(name).strip().lower())

#: `{attribute key: one-sentence gloss}` over the ten (B04.02, DEF Edit 1), cooked by the exporter, which refuses an empty one.
ATTRIBUTE_GLOSSES = dict(_DATA['attributes']['glosses'])


# ---------------------------------------------------------------------------
# THE TWO FACTOR FORMS OF THE USES TABLE (B04.06; U1 §3, `capability_roles`) -- a closed set of two, each implemented here once.
# A third form is a code change. The decision layer reads a row of `rosters.yaml: tables.capability_uses` and calls one of these;
# it names no attribute, no scale and no arithmetic of its own.
# ---------------------------------------------------------------------------
def scale_of(key):
    """`(floor, ceiling)` of the scale a held value at `key` lives on: the attribute scale for an attribute key, the
    registered bounds for a practitioner stat (`None` where the registry leaves that end open: `about_mid` on it raises). Raises
    ValueError for any other key."""
    if key in ATTRIBUTES:
        return ATTRIBUTE_FLOOR, ATTRIBUTE_CEILING
    stat = PRACTITIONER_STATS.get(key)
    if stat is not None:
        return stat['floor'], stat['ceiling']
    raise ValueError(f"no scale for {key!r}: it is neither an attribute nor a practitioner stat")


def about_mid(value, floor, ceiling, gain):
    """ROLE `judgement`: `1 + gain * (value - mid) / (mid - floor)`, `mid = (floor + ceiling) / 2`. Exactly 1 at the mid-point
    (and at `gain` 0), monotone in `value`, unbounded above: a caller that wants a cap applies its own."""
    mid = (floor + ceiling) / 2
    return 1.0 + gain * (value - mid) / (mid - floor)


# ---------------------------------------------------------------------------
# CAPABILITIES (SKILLS) -- B04.02. THE ONLY SKILL DEFINITION IN THE ENGINE.
# ---------------------------------------------------------------------------
# `references/descriptor_registry.yaml: capabilities`, validated by the exporter's `_capability_roster` and read here:
# one kind (`skill`, A-98 (4)); the attributes and the traits are defined elsewhere and not re-defined here.
@dataclass(frozen=True)
class CapabilityRow:
    """One skill's definition. `base` is the attribute key its pool starts from; `opposed_by` is an attribute key,
    `'none'` or `None` (absent: the opposition reads `base`; `'none'` currently reads as absent too [ASSUMPTION] until the
    obstacle's one form lands, B05, OBS section 2); `floor`/`ceiling` bound the held rank;
    `untrained` is what a non-holder brings (`default` or `none`); `grows_by` is the rules that may raise it."""
    kind: str
    gloss: str
    base: str
    opposed_by: Optional[str]
    floor: int
    ceiling: int
    untrained: str
    grows_by: Tuple[str, ...]


CAPABILITIES: Mapping[str, CapabilityRow] = MappingProxyType({
    name: CapabilityRow(r['kind'], r['gloss'], r['base'], r['opposed_by'], r['floor'], r['ceiling'],
                        r['untrained'], tuple(r['grows_by']))
    for name, r in _DATA['capabilities']['rows'].items()})


def capability(name) -> CapabilityRow:
    """The definition row of skill `name`; raises ValueError naming the roster, as `resolve_pursuit` does."""
    try:
        return CAPABILITIES[name]
    except (KeyError, TypeError):
        raise ValueError(
            f'unknown capability {name!r}. The roster is owned by references/descriptor_registry.yaml:capabilities '
            f'and read here; the defined skills are: ' + ', '.join(CAPABILITIES) + '. A skill is defined there once, '
            'then exported (tools/export_descriptors.py); do not add one anywhere else.') from None


# ---------------------------------------------------------------------------
# TRAITS -- B04.07 (U1 §2a, A-107). A SEPARATE ROSTER FROM THE SKILLS: a trait is held or not and never gives dice.
# ---------------------------------------------------------------------------
# `references/descriptor_registry.yaml: traits`, validated by the exporter's `_trait_roster`. `seated_by` is the one
# lowercase `resonant_style` value that seats the trait (`data/cast.py::traits_of`); held on `Person.traits`.
@dataclass(frozen=True)
class TraitRow:
    """One trait's definition: its `id`, a one-sentence `gloss`, and the `resonant_style` value that seats it."""
    id: str
    gloss: str
    seated_by: str


TRAITS: Mapping[str, TraitRow] = MappingProxyType({
    name: TraitRow(name, r['gloss'], r['seated_by']) for name, r in _DATA['traits']['rows'].items()})


def trait(id) -> TraitRow:
    """The definition row of trait `id`; raises ValueError naming the roster, as `capability` does."""
    try:
        return TRAITS[id]
    except (KeyError, TypeError):
        raise ValueError(
            f'unknown trait {id!r}. The roster is owned by references/descriptor_registry.yaml:traits and read here; '
            f'the defined traits are: ' + ', '.join(TRAITS) + '. A trait is defined there once, then exported '
            '(tools/export_descriptors.py); do not add one anywhere else.') from None


#: {registry key -> {name, floor, ceiling}} for each declared domain.
SETTLEMENT_STATS = _DATA['settlement_stats']
PRACTITIONER_STATS = _DATA['practitioner_stats']
TERRITORY_STATS = _DATA['territory_stats']

#: Ratified decisions the executable model has not implemented. Each names what it needs.
UNIMPLEMENTED = _DATA['unimplemented']


def block(name: str) -> dict:
    """One registry block by name, e.g. `block('pursuit_roster')`. THE PUBLIC WAY IN.

    ⚠ `engine/season/data/rosters.py`'s `from_descriptor:` pointer reads through here, never
    `_DATA`, which is underscore-private and carries no compatibility contract: a `getattr(...,
    "_DATA", {})` would turn a legal rename into a LIE (every pointed-at roster would raise *"absent
    or has no `names`"*, sending the next session to edit the registry, which is correct and
    unrelated).

    Returning `{}` for an unknown name is deliberate: the caller's own refusal reads better than
    one raised from here, because it names the roster that pointed and the exporter to re-run.
    """
    return _DATA.get(name) or {}


# ---------------------------------------------------------------------------
# PURSUITS — THIS IS THE ONLY PURSUIT ROSTER IN THE ENGINE.
# ---------------------------------------------------------------------------
# ⚠ THE FIFTEEN (IN-08's cells commit, ED-IN-0261): the roster this leaf reads is
# `references/descriptor_registry.yaml: pursuit_roster`, the surface the axis matrix, the contest
# styles and the cultural-background templates resolve `conv.*` through, enumerated there and
# cooked into the artifact, so the names exist in one place and every consumer reads THEM.
#
# ⚠ A NON-CANONICAL NAME (a legacy conviction tag) RAISES instead of silently scoring zero; see
# `resolve_pursuit` below.
PURSUITS = tuple(_DATA['pursuit_roster']['names'])

# ---------------------------------------------------------------------------
# ETHICAL AXES (ED-IN-0230). THE ONLY AXIS ROSTER IN THE ENGINE.
# ---------------------------------------------------------------------------
# Two literals of the axis roster with nothing comparing them could disagree in either direction
# with no refusal on either side; this is the PURSUITS shape one level up. Seven bipolar names
# (IN-08, ED-IN-0261); `AXIS_SCALE` carries the sign convention as data (negative = the
# first-named pole).
AXES = tuple(_DATA['axis_roster']['names'])
AXIS_SCALE = _DATA['axis_roster'].get('scale', '')

# ---------------------------------------------------------------------------
# AFFILIATIONS — IN-08 H10 (ED-IN-0251 R1/R2). THE ONLY AFFILIATION ROSTER IN THE ENGINE.
# ---------------------------------------------------------------------------
# `Person.conviction` is `{affiliation: intensity}` over these names, each intensity an int inside
# `[AFFILIATION_FLOOR, AFFILIATION_CEILING]`; the ceiling is "full intensity". One roster in `references/descriptor_registry.yaml`, exported behind the
# blocking `--check` (which validates the scale), read here.
AFFILIATIONS = tuple(_DATA['affiliation_roster']['names'])
AFFILIATION_FLOOR = _DATA['affiliation_roster']['scale']['floor']
AFFILIATION_CEILING = _DATA['affiliation_roster']['scale']['ceiling']
#: `{concern: (member, ...)}` -- the Church, Einhir, Altonia, each with the members that answer it
#: (v9 IN-64, ED-IN-0293 (2)); validated by the exporter (rostered, non-empty, none filed twice).
#: `engine/season/data/cast.py::conviction_of` refuses a cast row holding no member of a concern.
#: Indexed, not `.get`: an export without the key would otherwise read as "no concern to satisfy".
AFFILIATION_CONCERNS = {c: tuple(ms) for c, ms in _DATA['affiliation_roster']['concerns'].items()}

# ---------------------------------------------------------------------------
# HERITAGE -- v10 CR-30 (ED-IN-0301). THE ONLY HERITAGE ROSTER IN THE ENGINE.
# ---------------------------------------------------------------------------
#: The descents `Person.heritage` is one of (`None` is unauthored, never a member), in registry order, and
#: `{member: concern}` -- the affiliation concern each engages (a key of `AFFILIATION_CONCERNS`; the exporter
#: refuses any other). A member absent from the mapping engages none. `engine/season/data/cast.py::heritage_of`
#: refuses a cast value that is not a member.
HERITAGES = tuple(_DATA['heritage_roster']['names'])
HERITAGE_ENGAGES = dict(_DATA['heritage_roster']['engages'])

# ⚠ THERE IS NO ALIAS MAP, DELIBERATELY: a `{'Reason': 'Scholastic', 'Autonomy': 'Liberty'}` map
# would decide a migration TWO AUTHORED SURFACES EXPLICITLY REFUSE:
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
# surface at all. So every non-canonical name raises, and the error names the migration rather than
# guessing its outcome.
def resolve_pursuit(name):
    """`name` if it is a canonical pursuit, else raise ValueError. Nothing is translated.

    THE RAISE IS THE POINT. A silent unknown name would score magnitude=0 and no caller could tell
    "this Scar was capped" from "this pursuit does not exist". A wrong name is a defect in the
    caller, so it is loud here.
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
