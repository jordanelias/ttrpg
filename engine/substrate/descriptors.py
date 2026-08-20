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

WHAT IT DOES NOT DO. It does not clamp anything yet. `Faction.adjust`
(`engine/autoload/game_state.py:127-131`) still applies a blanket floor 0.5 / ceiling 7.0 to every
stat, while the registry's PER-STAT floors were ratified 2026-07-08 (ED-IN-0029) — Influence at 1,
the rest at 0. Wiring `adjust` to `faction_bounds()` moves the seeded campaign goldens, so it is a
separate, MEASURED commit rather than a side effect of introducing this reader. The gap is recorded
in the export's `unimplemented` block and surfaced by `assert_faction_roster_is_covered()` below.
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
FACTION_STATS = _DATA['faction_stats']
SETTLEMENT_STATS = _DATA['settlement_stats']
PRACTITIONER_STATS = _DATA['practitioner_stats']
TERRITORY_STATS = _DATA['territory_stats']

#: {registry key -> the field name engine.autoload.game_state.Faction actually uses}.
FACTION_FIELD_MAP = _DATA['faction_field_map']
_FIELD_TO_KEY = {v: k for k, v in FACTION_FIELD_MAP.items()}

#: Ratified decisions the executable model has not implemented. Each names what it needs.
UNIMPLEMENTED = _DATA['unimplemented']


def faction_bounds(field):
    """(floor, ceiling) the REGISTRY declares for a Faction dataclass field, or None if it declares
    none. Returns None for `L` — Legitimacy/Mandate is written by 32 call sites and is declared
    nowhere in the registry, which is the 5-vs-6 half of the faction-stats packet awaiting a ruling.
    Callers must handle None rather than substituting a default, so the gap stays visible."""
    key = _FIELD_TO_KEY.get(field)
    if key is None:
        return None
    row = FACTION_STATS.get(key)
    if row is None:
        return None
    return row['floor'], row['ceiling']


def assert_faction_roster_is_covered(implemented_fields):
    """Raise if the registry declares a faction stat the code has no field for.

    THIS IS THE POINT OF THE MODULE: it makes `references/descriptor_registry.yaml` load-bearing at
    RUNTIME rather than by convention. Add a stat to the registry without adding its field and the
    engine stops importing, instead of silently running on a roster that no longer matches canon.

    The check runs one way ONLY. Code fields with no registry entry are NOT an error here, because
    exactly one exists — `L` — and whether it is a base descriptor or derived like Mandate is an
    open ruling. Failing on it would force this session to answer a question that is Jordan's.
    """
    have = set(implemented_fields)
    missing = sorted(k for k, f in FACTION_FIELD_MAP.items() if f not in have)
    if missing:
        raise RuntimeError(
            'descriptor_registry.yaml declares faction stat(s) the executable model does not '
            'implement: ' + ', '.join(missing) + '. Add the field to '
            'engine/autoload/game_state.py:Faction (and a MULTS entry if it is adjustable), or '
            'retire the registry entry — do not silence this check.'
        )
    return len(FACTION_FIELD_MAP)
