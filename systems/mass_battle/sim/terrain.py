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
`designs/territory/...::terrain_polygons`, stale in both path and key. `systems/settlements/sim/
registry.py`'s `_GEOGRAPHY_YAML` is the existing, single-owner loader for this same file (settlement
population); this module reads the same file's `provinces:` and `terrain:` keys directly rather than
routing through that settlement-shaped API, since neither key it needs is exposed there.
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

RIVER_CROSSING is not yet reachable from this lookup at all: `_TYPE_TO_ROW` has no entry that
produces it, and no code path here reads the geography file's `water:`/`bridges:` keys (the crossing
data ED-780's extension implies exists). Adding it needs a caller-side signal (does the engagement
cross a mapped river edge between two provinces) that this province-interior point-test cannot derive
by itself — follow-up work, not this pass's.
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
RIVER_CROSSING = 'river_crossing'  # not yet reachable from this lookup — see the module docstring's own gap note
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


def terrain_row_for_territory(tid, fort_level=0):
    """The A.9 row (one of this module's six constants) for a battle fought over province `tid`.

    `fort_level`: the LIVE value from `world.territories[tid].fort_level` — pass it, do not omit it,
    for any campaign-reachable call. [CORRECTED, adversarial review 2026-09-27] This function does NOT
    read the geography YAML's own `provinces.<tid>.fort_level` key for this check, though that key
    exists in the file and an earlier version of this function read it. `engine/autoload/
    game_state.py`'s `Territory` dataclass derives `fort_level` from `garrison` at world-build time and
    says so directly: "fort_level stays DERIVED from garrison rather than authored: it is a rule, not
    data, and authoring it would give one number two owners" (`game_state.py:322-323`). The geography
    YAML's copy is that second owner — authored, static, and already disagreeing with the live value
    for real territories (e.g. T2: YAML `fort_level: 1`, live `fort_level: 0` since `garrison: false`
    in `references/world_initial_state.yaml`). Reading the YAML copy here silently forked a
    single-owned fact (CLAUDE.md §0.05 clause 3) and was latent only because nothing yet applies a
    WALLS effect — it would have surfaced the moment one did. The caller (`faction_action._try_conquest`)
    already holds the live `Territory` in scope; passing its `fort_level` costs nothing.

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
