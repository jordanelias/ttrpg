"""systems.mass_battle.sim.terrain — A7 (ED-MB-0067 Part A / ED-780): geography-derived battle terrain.

[canonical: mass_battle_v30.md §A.9 ENVIRONMENTAL MODIFIERS + its Phase-3 (ED-780) extension — "When a
mass battle resolves at engagement coordinates that intersect
designs/territory/valoria_geography_v30.yaml::terrain_polygons, the Terrain row is determined by
querying the geography at battle coordinates rather than declaratively assigned... Polygon
intersections producing multiple terrains use the dominant polygon (by area weight) at the engagement
hex... no separate declaration required." Quarantined, cited by bare filename per CLAUDE.md §1 — do
not point at its `.designs/` path.]

⚠ CORRECTION TO CANON'S OWN TEXT, already flagged in
proposals/2026-09-25-squad-engagement-synthesis.md (A7): the data lives at
`systems/settlements/valoria_geography_v30.yaml`, key `terrain:` (typed polygons) — NOT
`designs/territory/...::terrain_polygons`, stale in both path and key. This module reads the file's
`provinces:` and `terrain:` keys directly through its own `_GEOGRAPHY_YAML`; it shares that loader with
no other module since plan position `29c` deleted `systems/settlements/sim/registry.py` (the settlement
population loader, which had a second `_GEOGRAPHY_YAML` for the same file). `engine/season/harness/
populated.py` reads the same file by its own path (`GEOGRAPHY`).
**Fortification is NOT read from this file** — see `terrain_row_for_territory`'s own docstring for why.

SIMPLIFICATION, disclosed rather than hidden: "dominant polygon by area weight" would need true
polygon-intersection-AREA computation between the target province's own footprint and every
overlapping terrain polygon. This implementation instead point-tests the province's own `anchor`
(`provinces.<tid>.anchor` — already the geography file's own representative coordinate for the
province) against each terrain polygon — simpler, no new geometry dependency (no shapely; this
repo's provisioner installs pyyaml/pytest/numpy only), and correct whenever a province's anchor sits
inside its own dominant terrain, which held for every province sampled while building this. A
genuinely split province whose anchor lands in a minority polygon is a known gap, not silently
claimed as solved by "dominant... by area weight" — a real area-weighted version is follow-up work,
not this pass's. **A known instance of this exact gap, found by adversarial review (2026-09-27):**
T3 and T10 each "gate" a mountain pass (`altonian_passes`, geography YAML) but their own `anchor`
sits inside their OWN territory polygon, south of and outside the pass polygon's y-range entirely —
not a near-miss, a disjoint region — so neither can resolve to NARROW_PASS via this point-test
regardless of fortification. `test_mass_battle_terrain.py` covers the "Done when" criterion with a
synthetic province rather than a real one for exactly this reason.

RIVER_CROSSING is not reachable from the polygon lookup: `_TYPE_TO_ROW` has no entry producing it and
nothing here reads the geography file's `water:`/`bridges:` keys. It is reached only through the
CALLER'S signal, `terrain_row_for_territory(..., river_crossing=True)` (MB-05); no season caller
derives that signal yet (the provider is handed the target rung, not the march's origin, and whether a
bridge on the route cancels the crossing is unruled) — see that function's own docstring.
"""
import os

import yaml

_REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
_GEOGRAPHY_YAML = os.path.join(_REPO_ROOT, 'systems', 'settlements', 'valoria_geography_v30.yaml')

# A.9's six canonical rows (mass_battle_v30.md §A.9, a closed table — this module invents no seventh).
NARROW_PASS = 'narrow_pass'
UPHILL = 'uphill'
FOREST_BROKEN = 'forest_broken'
WALLS = 'walls'
RIVER_CROSSING = 'river_crossing'  # reached only by the caller's `river_crossing` signal — see the module docstring
OPEN_FLAT = 'open_flat'

# [ASSUMPTION: geography `type:` values with no direct A.9 analogue mapped to the closest existing
# row rather than inventing a seventh — basis: A.9 is closed/canonical, and CLAUDE.md Sec.4's
# idempotent-vocabulary rule ("coin nothing a plain word already covers") argues against a new row
# for a case no ruling has asked for. 'mountain'/'highland' -> UPHILL: the only A.9 row describing
# elevated ground; neither name is a literal match, only the closest available. 'coast' -> OPEN_FLAT:
# adjacency to open sea is not itself obstructive to a land battle (the actual crossing case, a RIVER,
# is not yet reachable from this lookup at all — see the module docstring). 'fjord_coast' ->
# FOREST_BROKEN, not OPEN_FLAT: [CORRECTED, adversarial review 2026-09-27] the geography file's own
# `terrain_cost_matrix` names it "broken inlet land terrain" at cost 2.5 — higher than forest's 1.5 or
# marsh's 2.0, and using A.9's own word "broken" — so OPEN_FLAT's "no modifiers" was the wrong read of
# this repo's own data, not a defensible simplification. 'marsh' -> FOREST_BROKEN: boggy/difficult
# ground is closest, of the six, to forest/broken's own character (restricts formation, not open
# terrain).]
_TYPE_TO_ROW = {
    'mountain_pass': NARROW_PASS,
    'mountain': UPHILL,
    'highland': UPHILL,
    'forest': FOREST_BROKEN,
    'marsh': FOREST_BROKEN,
    'coast': OPEN_FLAT,
    'fjord_coast': FOREST_BROKEN,
    'plains': OPEN_FLAT,
}

_cache = None


def _load_geography():
    global _cache
    if _cache is None:
        with open(_GEOGRAPHY_YAML, 'r', encoding='utf-8') as f:
            _cache = yaml.safe_load(f)
    return _cache


def _point_in_polygon(pt, polygon):
    """Standard ray-casting point-in-polygon test. `polygon`: a list of [x, y] pairs. A point exactly
    on a polygon edge is treated inconsistently (a known limitation of the raw algorithm) — not
    load-bearing here, since a province's `anchor` is placed well inside its own territory in every
    entry sampled, never on a terrain-polygon boundary."""
    x, y = pt
    inside = False
    n = len(polygon)
    x1, y1 = polygon[-1]
    for i in range(n):
        x2, y2 = polygon[i]
        if (y1 > y) != (y2 > y):
            x_intersect = (x2 - x1) * (y - y1) / (y2 - y1) + x1
            if x < x_intersect:
                inside = not inside
        x1, y1 = x2, y2
    return inside


def _polygon_area(polygon):
    """Shoelace formula. Used only to break ties among OVERLAPPING terrain polygons (below) — not a
    claim about the true intersection-area computation this module's docstring already discloses as
    a simplification."""
    n = len(polygon)
    total = 0.0
    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % n]
        total += x1 * y2 - x2 * y1
    return abs(total) / 2.0


def terrain_row_for_territory(tid, fort_level=0, river_crossing=False):
    """The A.9 row (one of this module's six constants) for a battle fought over province `tid`.

    `river_crossing` (MB-05): the CALLER's fact that the attacker fights its way across a river to
    reach the field -- the only way RIVER_CROSSING is ever returned (the module docstring says why the
    polygon lookup cannot produce it). Default `False` is every caller today, so no live field moves.
    `[ASSUMPTION: priority WALLS > RIVER_CROSSING > polygon -- the same one-row-of-six shape that forced
    the fortification rule below forces one here; a crossing outranks the surrounding polygon because it
    is what happens AT the engagement, and walls outrank the crossing by that rule's own reasoning.]`
    Like fortification, it is read only for a KNOWN `tid`.

    `fort_level`: the LIVE fortification of the place fought over — pass it, do not omit it, for any
    season-reachable call. Since plan position `20-iv` the one production caller is
    `massbattle.resolve_field`,
    fed by `engine/season/seam/wrappers/mass_battle.py` with `queries/world_q.py::fortification_of`
    at the march target (a garrison Site's `condition`, Jordan's ruling on what garrison strength IS),
    a float in `[0.0, 1.0]`; only `> 0` is read here. [CORRECTED, adversarial review 2026-09-27] This
    function does NOT read the geography YAML's own `provinces.<tid>.fort_level` key for this check,
    though that key exists in the file and an earlier version of this function read it: the YAML's
    copy is authored and static, a second owner of a fact the world holds live, and it already
    disagreed with the live value for real territories (T2: YAML `fort_level: 1`, while the
    since-deleted `Territory` derived 0 from `garrison: false`). Reading it would silently fork a
    single-owned fact (CLAUDE.md §0.05 clause 3). The 2026-09-27 caller this paragraph first named,
    `faction_action._try_conquest`, and the `game_state.Territory` it read were deleted at plan
    position `29b`.

    [ED-780] FORTIFICATION DOMINATES: a fielded `fort_level > 0` resolves as WALLS regardless of the
    surrounding terrain polygon — a walled city's defining battle character is its walls, not whatever
    geography surrounds it. `[ASSUMPTION: this priority rule — fortification checked before, and
    overriding, the polygon lookup — is this module's own inference, not ED-780's text, which says only
    that "the Terrain row is determined by querying the geography" and is silent on fortification
    entirely. Basis: A.9's own table lists "Walls / fortifications" and the five geography-derived rows
    as ONE row picked among six, never combined, so some priority rule between "walled" and "whatever
    polygon the anchor sits in" is required by the table's own shape; fortification winning is the more
    defensible default absent a ruling, since a fortified anchor point still physically sits somewhere,
    but an un-fortified point cannot retroactively acquire walls.]`

    SMALLEST-AREA MATCH WINS among overlapping terrain polygons — found empirically, not assumed: the
    geography file nests smaller features inside larger ones on purpose (its own description: the
    Northern Mountains polygon has "Two passes embedded"), so a point can legitimately test inside
    BOTH `terrain-mountain-north` (type mountain) and `terrain-pass-lowenskyst` (type mountain_pass)
    at once. Taking the first list match arbitrarily picked whichever was written first in the file
    (the enclosing mountain, wrongly) rather than the more specific feature actually at that point —
    caught by this module's own test (`test_mountain_pass_polygon_maps_to_narrow_pass_directly`)
    failing on the naive version, not assumed correct without checking. Smallest-area-wins matches the
    geography file's own framing of the pass as embedded IN the mountain (`terrain_cost_matrix`'s
    comment: "Mountain interior is impassable except via embedded mountain_pass polygons") — the
    embedded feature is what's actually underfoot, not "standard GIS convention" (no such external
    standard is cited or needed here) — and needs no per-type special case (CLAUDE.md's own guardrail
    against special-casing an entity or outcome).

    Falls back to OPEN_FLAT — the safe, no-modifier default — if `tid` is unknown to the geography
    file, its `anchor` is missing, or the anchor lands inside no terrain polygon at all."""
    geo = _load_geography()
    province = geo.get('provinces', {}).get(tid)
    if province is None:
        return OPEN_FLAT
    if fort_level > 0:
        return WALLS
    if river_crossing:
        return RIVER_CROSSING
    anchor = province.get('anchor')
    if anchor is None:
        return OPEN_FLAT
    best_type, best_area = None, None
    for entry in geo.get('terrain', []):
        if not _point_in_polygon(anchor, entry['polygon']):
            continue
        area = _polygon_area(entry['polygon'])
        if best_area is None or area < best_area:
            best_type, best_area = entry['type'], area
    if best_type is None:
        return OPEN_FLAT
    return _TYPE_TO_ROW.get(best_type, OPEN_FLAT)


#: A.9's Walls row, the one number it gives: the DEFENDER's damage reduction rises by this much. It
#: lands on the engine's own `Unit.dr`, the quantity melee already subtracts from damage
#: (`orchestration.py`: `DAMAGE_BY_DEGREE[deg](power) - eff_dr`). Applying A.9's +3 1:1 to that unit
#: is an ASSUMPTION (`H-150`), not a measurement. The row's other two clauses ("no flanking; Slow cannot
#: advance") are NOT applied -- `massbattle.py::_run_and_grade`'s docstring says why. Kept below the
#: lookup, not beside the row constants, so the lookup's line stays where the mass-battle flow
#: skeleton's line anchor cites it (`tests/valoria/test_flow_skeletons.py`). Applied since `20-iv`.
WALLS_DEFENDER_DR = 3  # [canonical: mass_battle_v30.md §A.9 ENVIRONMENTAL MODIFIERS — "Walls / fortifications | Defender +3 DR"]

#: MB-05. A.9's two dice rows, as DICE -- A.6's currency (`Off dice | Def dice`). They land on
#: `Unit.terrain_off_d`/`terrain_def_d` (`massbattle._run_and_grade`), and the engine turns a die into
#: sigma only through `config.SIGMA_PER_D`, a CALIBRATED-DEBT conversion (its own line says so): the dice
#: counts are canon's, the size of their effect on a fight is that constant's. Def dice are spent the
#: way the engine already spends a defensive commitment (`INTENT_DEFENSE_D`): they blunt the enemy's
#: offence, so on an uphill field the attacker's offence falls by both rows together.
UPHILL_ATTACKER_OFF_D = -1  # [canonical: mass_battle_v30.md §A.9 ENVIRONMENTAL MODIFIERS — "Uphill | Defender +1D Def; attacker −1D Off"]
UPHILL_DEFENDER_DEF_D = 1  # [canonical: mass_battle_v30.md §A.9 ENVIRONMENTAL MODIFIERS — "Uphill | Defender +1D Def; attacker −1D Off"]
#: River crossing's dice row, on the CROSSING side -- the attacker, `unit_a` (`[ASSUMPTION: A.9 does
#: not say who crosses; the side that marched to the field is the one that can have crossed to reach
#: it]`). The row's other clauses: "−1 Speed tier" is applied by `SPEED_TIERS` below (inert on the
#: season path, as forest's speed half is); "Discipline check (treat Size lost = 1)" is NOT coded,
#: because under §A.4's deterministic check (PP-502: degrade when Size lost > current Discipline AND
#: exceeds the enemy's loss) a Size loss of 1 degrades no unit with Discipline >= 1 -- a no-op by canon's
#: own arithmetic, so code for it would observe nothing.
RIVER_CROSSING_OFF_D = -1  # [canonical: mass_battle_v30.md §A.9 ENVIRONMENTAL MODIFIERS — "River crossing | −1 Speed tier; −1D Off; Discipline check"]
SPEED_TIERS = ('Slow', 'Standard', 'Fast')  # [canonical: mass_battle_v30.md §A.4 — "Speed — Slow / Standard / Fast (3 tiers)", in that order]
