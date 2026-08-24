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

WHAT IT NOW DOES, corrected 2026-08-22 (plan S5d — this paragraph described the opposite until
then) and again 2026-08-23. `faction_bounds()` IS the clamp: `Faction.adjust` reads it instead of
applying a blanket floor 0.5 / ceiling 7.0 to every stat. ED-IN-0029's per-stat floors reached the
executable model on 2026-08-22; Jordan then ruled three times on 2026-08-23 — "Legitimacy is a
base" (so `fac.legitimacy` is declared and the roster is SIX), "Influence can be 0" (superseding
that docket's Influence floor of 1), and "floor ruling 0" for Legitimacy itself. All six declared
faction stats floor at 0 and ceiling at 7, and every one of those bounds is now RULED rather than
inferred — the Legitimacy floor shipped on 2026-08-22 as a session's inference and the third ruling
CONFIRMED it, so no golden moved for it. The two re-records that DID move goldens measured their
delta against an n=240-per-arm control first.

FIVE OF THE SIX FLOORS ARE REACHABLE. `fac.intel` is not: `MULTS` carries no `intel` key, so
`adjust('intel', …)` raises `KeyError` before any bound is consulted, and the (0, 7) this returns
for it is unreachable. Recorded rather than papered over — wiring it needs a multiplier nobody has
stated.
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
    none.

    ⚠ IT NO LONGER RETURNS None FOR ANY DECLARED FACTION STAT. Until 2026-08-23 it returned None for
    `L`, the one Faction field the registry did not declare — the "5-vs-6" gap in the faction-stats
    packet, now closed. Jordan ruled that day that Legitimacy IS a base descriptor, so `fac.legitimacy` is
    declared and bound to `L`, and the roster is six. Callers must STILL handle None, because a
    caller may pass a stat that is not a faction descriptor at all (`MULTS` carries `accord` and
    `pt`, which are Territory fields) — the contract is unchanged even though the L case is gone."""
    key = _FIELD_TO_KEY.get(field)
    if key is None:
        return None
    row = FACTION_STATS.get(key)
    if row is None:
        return None
    return row['floor'], row['ceiling']


def assert_faction_roster_is_covered(implemented_fields):
    """Raise if the REGISTRY declares a faction stat the executable model does not implement.

    THIS IS THE POINT OF THE MODULE: it makes `references/descriptor_registry.yaml` load-bearing at
    RUNTIME rather than by convention. Add a stat to the registry without adding its field and the
    engine stops importing, instead of silently running on a roster that no longer matches canon.

    IT ITERATES `FACTION_STATS`, WHICH IS THE REGISTRY-DERIVED HALF OF THE ARTIFACT, AND THAT IS THE
    WHOLE CORRECTNESS ARGUMENT. Until 2026-08-21 it iterated `FACTION_FIELD_MAP` instead — the
    hand-maintained `FACTION_KEY_TO_FIELD` dict in `tools/export_descriptors.py`. A registry edit
    does not touch that dict, so the claim in this docstring was FALSE as shipped: adding
    `fac.zeal` to the registry, re-cooking, and calling this function returned `covered=5` and the
    engine imported fine. The two-stage check below is what the claim actually requires:

      stage 1 — every registry key is BOUND to a field name by the export's `faction_field_map`;
      stage 2 — every bound field name is IMPLEMENTED by the dataclass.

    A new registry stat fails stage 1 (nobody has said which field it is). A registry stat whose
    field was deleted fails stage 2. Both stop the import, which is what "load-bearing" means.

    THE CHECK RUNS ONE WAY ONLY, and as of 2026-08-23 that direction protects nothing that exists —
    which is exactly when it is worth stating why it is kept. A code field with no registry entry is
    not an error here. Until that date one such field existed (`L`), and failing on it would have
    forced a session to answer a question that was Jordan's; he answered it, `fac.legitimacy` is
    declared, and the count of unregistered Faction fields is now zero.

    The direction stays anyway, because the reason was never "there is currently one" — it was that
    a NEW field appearing in the dataclass is a design act whose registry status is a ruling, and a
    check that halts the engine over it would make this file the arbiter of canon. The property is
    structural rather than a special case: this function never enumerates `implemented_fields`, only
    registry keys, so an unregistered field cannot reach either stage.
    """
    have = set(implemented_fields)

    unbound = sorted(k for k in FACTION_STATS if k not in FACTION_FIELD_MAP)
    if unbound:
        raise RuntimeError(
            'descriptor_registry.yaml declares faction stat(s) that nothing binds to a field of '
            'engine/autoload/game_state.py:Faction: ' + ', '.join(unbound) + '. Add the field to '
            'Faction, then add the key -> field row to FACTION_KEY_TO_FIELD in '
            'tools/export_descriptors.py and re-run it — or retire the registry entry. Do not '
            'silence this check: a stat canon declares and the engine cannot name is exactly the '
            'drift this module exists to stop.'
        )

    unimplemented = sorted(k for k in FACTION_STATS if FACTION_FIELD_MAP[k] not in have)
    if unimplemented:
        raise RuntimeError(
            'descriptor_registry.yaml declares faction stat(s) the executable model does not '
            'implement: ' + ', '.join(f'{k} -> {FACTION_FIELD_MAP[k]}' for k in unimplemented) +
            '. Add the field to engine/autoload/game_state.py:Faction (and a MULTS entry if it is '
            'adjustable), or retire the registry entry — do not silence this check.'
        )

    return len(FACTION_STATS)


# ---------------------------------------------------------------------------
# CONVICTIONS — added 2026-08-24. THIS IS THE ONLY CONVICTION ROSTER IN THE ENGINE.
# ---------------------------------------------------------------------------
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
CONVICTIONS = tuple(_DATA['conviction_roster']['names'])

#: Retired roster names -> the canonical name they resolve to. Kept SMALL and only where the
#: mapping is a rename rather than a design call: Reason and Scholastic are the same conviction
#: under two labels, as are Autonomy and Liberty. Nothing else is aliased — mapping `Survival` or
#: `Power` onto a canonical name would be inventing canon, so those simply fail.
CONVICTION_ALIASES = {
    'Reason': 'Scholastic',
    'Autonomy': 'Liberty',
}


def resolve_conviction(name):
    """Canonical Conviction name for `name`, or raise ValueError.

    THE RAISE IS THE POINT. The bug this module closes was a *silent* one — an unknown name scored
    magnitude=0 and no caller could tell the difference between "this Scar was capped" and "this
    Conviction does not exist". A wrong name is a defect in the caller, so it is loud here.
    """
    if name in CONVICTIONS:
        return name
    alias = CONVICTION_ALIASES.get(name)
    if alias is not None:
        return alias
    raise ValueError(
        f'unknown Conviction {name!r}. The roster is owned by '
        'references/descriptor_registry.yaml:conviction_roster and read here; the canonical '
        f'{len(CONVICTIONS)} are: ' + ', '.join(CONVICTIONS) + '. Do not add a name to a local '
        'tuple to make this pass — add it to the registry and re-run tools/export_descriptors.py, '
        'or fix the caller.'
    )
