"""A7 (ED-MB-0067 Part A / ED-780, ED-MB-0074) — terrain, battle-wide, from the strategic map.

`mass_battle_v30.md` §A.9 ENVIRONMENTAL MODIFIERS names six canonical rows; its Phase-3 (ED-780)
extension says a battle's terrain should be found by "querying the geography at battle coordinates
... no separate declaration required". The engagement's own province tid IS that query key —
`systems.mass_battle.sim.terrain.terrain_row_for_territory` reads
`systems/settlements/valoria_geography_v30.yaml` directly (its `provinces:` and `terrain:` keys;
canon's own citation, `designs/territory/...::terrain_polygons`, is stale in both path and key).

Two things this file does NOT claim: (1) "dominant polygon by area weight" (ED-780's own wording) —
this implementation point-tests each province's `anchor` against terrain polygons rather than
computing true intersection area; disclosed in `terrain.py`'s own docstring, not re-litigated here.
(2) full A.9 mechanical coverage — only FOREST_BROKEN's speed half ("Cavalry -> Standard") and WALLS'
defender DR (plan position `20-iv`) are wired into `massbattle.py::_run_and_grade`; UPHILL/NARROW_PASS/
RIVER_CROSSING are identified by the lookup but not yet mechanically applied (see `_run_and_grade`'s own
docstring for why each is deferred, not silently dropped).

[CORRECTED, adversarial review 2026-09-27] `terrain_row_for_territory` no longer reads fortification
from the geography YAML — it takes the live `fort_level` as a caller-supplied argument (see its own
docstring for why: the YAML's authored copy and the engine's live, garrison-derived value disagree for
real territories, and reading the authored copy forked a single-owned fact). Every call below that
cares about fortification now passes `fort_level` explicitly rather than reading it off the fixture.
"""
import pytest

from systems.mass_battle.sim.terrain import (
    terrain_row_for_territory, _point_in_polygon, _load_geography, _TYPE_TO_ROW,
    NARROW_PASS, UPHILL, FOREST_BROKEN, WALLS, OPEN_FLAT,
)


# ─── the point-in-polygon primitive ──────────────────────────────────────────

def test_point_in_polygon_basic_square():
    square = [[0, 0], [10, 0], [10, 10], [0, 10]]
    assert _point_in_polygon((5, 5), square)
    assert not _point_in_polygon((15, 5), square)
    assert not _point_in_polygon((-1, 5), square)


def test_point_in_polygon_against_a_real_geography_entry():
    """Not a synthetic square — one of the actual polygons this lookup will be tested against."""
    geo = _load_geography()
    entry = next(e for e in geo['terrain'] if e['id'] == 'terrain-pass-lowenskyst')
    xs = [p[0] for p in entry['polygon']]
    ys = [p[1] for p in entry['polygon']]
    center = (sum(xs) / len(xs), sum(ys) / len(ys))
    assert _point_in_polygon(center, entry['polygon']), \
        "a polygon's own centroid must test as inside it"
    far_outside = (xs[0] - 100000, ys[0] - 100000)
    assert not _point_in_polygon(far_outside, entry['polygon'])


# ─── the geography lookup, against the REAL committed file ──────────────────

def test_every_real_province_resolves_to_one_of_the_six_rows():
    """No province should fall through to something outside A.9's closed set -- a NULL-result alarm,
    not a claim that every row actually occurs (RIVER_CROSSING never does; see terrain.py). Called at
    fort_level=0 uniformly: fortification is a separate, already-isolated concern (the tests below),
    and this test is specifically about the polygon lookup's own closed-set property."""
    geo = _load_geography()
    valid = {NARROW_PASS, UPHILL, FOREST_BROKEN, WALLS, OPEN_FLAT,
             'river_crossing'}  # not currently reachable, but still a valid A.9 row name
    seen = set()
    for tid in geo['provinces']:
        row = terrain_row_for_territory(tid, fort_level=0)
        assert row in valid, f"{tid} resolved to {row!r}, outside A.9's six rows"
        seen.add(row)
    assert len(seen) >= 2, "a lookup that always returns the same row for every province is not measuring anything"


def test_every_geography_terrain_type_has_a_row_mapping():
    """[adversarial review 2026-09-27] `_TYPE_TO_ROW.get(best_type, OPEN_FLAT)` silently falls back to
    OPEN_FLAT for any `type:` this dict does not cover -- indistinguishable from a genuine open-flat
    result. If the geography file ever gains a terrain type this module has not been told about, that
    silent fallback is a real, unflagged mechanical error, not a documented gap like RIVER_CROSSING is
    (which is absent from the FUNCTION'S REACHABLE SET, not from the file's own type vocabulary)."""
    geo = _load_geography()
    real_types = {entry['type'] for entry in geo['terrain']}
    uncovered = real_types - set(_TYPE_TO_ROW)
    assert not uncovered, f"geography terrain type(s) {uncovered} have no _TYPE_TO_ROW entry"


@pytest.mark.parametrize('tid', ['T2', 'T4', 'T7'])
def test_a_positive_fort_level_resolves_to_walls_regardless_of_terrain(tid):
    """ED-780: fortification dominates whatever polygon surrounds it -- and, per this function's own
    contract, `fort_level` is now the CALLER's value, not something read off this `tid` in the
    geography file. T2/T4/T7 are real, known provinces with different terrain (see the pinned-row
    tests below for what T4/T7 resolve to at fort_level=0); a positive fort_level must win regardless
    of which terrain a `tid` would otherwise resolve to. NOT tested here: an UNKNOWN `tid` -- the
    province-existence check runs first and returns OPEN_FLAT before `fort_level` is even looked at
    (see `test_unknown_territory_falls_back_to_open_flat`), which is fine since every real caller's
    `tid` already names a `world.territories` entry by construction."""
    assert terrain_row_for_territory(tid, fort_level=2) == WALLS


def test_zero_fort_level_falls_through_to_the_polygon_lookup():
    """Companion boundary to the test above: fort_level=0 must NOT force WALLS -- confirms the
    dominance check is a real `> 0` gate, not e.g. a falsy/None check that WALLS-locks a passed-but-
    zero value too."""
    assert terrain_row_for_territory('T4', fort_level=0) == UPHILL


def test_unknown_territory_falls_back_to_open_flat():
    assert terrain_row_for_territory('T-does-not-exist', fort_level=0) == OPEN_FLAT


# ─── real committed provinces, pinned to their actual row (not just "some valid row") ────────────
# [adversarial review 2026-09-27] the tests above establish the mechanism; these pin actual results
# for actual data, so a regression in the polygon/type-mapping logic (e.g. forest silently resolving
# to OPEN_FLAT) does not pass silently just because OPEN_FLAT is also a valid member of the closed set.

@pytest.mark.parametrize('tid,expected', [
    ('T4', UPHILL),          # terrain-highland-grauwald; anchor [1090,1430] inside [970-1170]x[1300-1480]
    ('T7', FOREST_BROKEN),   # terrain-forest-rendstad; anchor [720,800] inside [420-970]x[700-1000]
    ('T6', FOREST_BROKEN),   # terrain-marsh-stillhelm (marsh -> FOREST_BROKEN); anchor [1180,2300]
])
def test_real_unfortified_provinces_pin_to_their_actual_terrain_row(tid, expected):
    assert terrain_row_for_territory(tid, fort_level=0) == expected


def test_mountain_pass_polygon_maps_to_narrow_pass_directly(monkeypatch):
    """THE 'DONE WHEN' CRITERION (Part A, A7): a battle placed in a mountain_pass polygon resolves
    under A.9's narrow-pass row. [CORRECTED, adversarial review 2026-09-27] No real province pins
    this today -- NOT because both mountain-pass provinces (T3, T10) are fortified (fortification is
    orthogonal, tested separately above), but because each one's own `anchor` sits in ITS OWN
    territory polygon, south of and geometrically DISJOINT from the pass polygon it "gates"
    (`altonian_passes` in the geography file): T3's anchor is at y=380, its pass polygon spans
    y=[80,290]; T10's anchor is at y=380, its pass polygon spans y=[80,290] too. Neither anchor is
    a near-miss inside the pass -- it is entirely outside its y-range. So this pins the polygon->row
    mapping directly with a synthetic province placed at the pass polygon's own centroid, isolating
    the claim in question from that unrelated (and, for T3/T10, unrelated-twice-over) gap."""
    geo = _load_geography()
    pass_entry = next(e for e in geo['terrain'] if e['type'] == 'mountain_pass')
    xs = [p[0] for p in pass_entry['polygon']]
    ys = [p[1] for p in pass_entry['polygon']]
    synthetic = dict(geo)
    synthetic['provinces'] = dict(geo['provinces'])
    synthetic['provinces']['T-synthetic-pass'] = {
        'anchor': [sum(xs) / len(xs), sum(ys) / len(ys)],
    }
    import systems.mass_battle.sim.terrain as T
    monkeypatch.setattr(T, '_cache', synthetic)
    assert terrain_row_for_territory('T-synthetic-pass', fort_level=0) == NARROW_PASS


def test_open_ground_resolves_unmodified(monkeypatch):
    """The other half of the 'Done when' criterion: open ground resolves unmodified (OPEN_FLAT)."""
    geo = _load_geography()
    plains_entry = next(e for e in geo['terrain'] if e['type'] == 'plains')
    xs = [p[0] for p in plains_entry['polygon']]
    ys = [p[1] for p in plains_entry['polygon']]
    synthetic = dict(geo)
    synthetic['provinces'] = dict(geo['provinces'])
    synthetic['provinces']['T-synthetic-plains'] = {
        'anchor': [sum(xs) / len(xs), sum(ys) / len(ys)],
    }
    import systems.mass_battle.sim.terrain as T
    monkeypatch.setattr(T, '_cache', synthetic)
    assert terrain_row_for_territory('T-synthetic-plains', fort_level=0) == OPEN_FLAT


# ─── the mechanical effects wired so far: forest -> cavalry Standard speed; walls -> defender DR ─
# RE-POINTED at plan position `29b` (2026-10-01). These three tests drove `resolve_mass_battle` with
# faction-shaped stubs and patched `_faction_to_unit`; both were deleted with `game_state.Faction` and
# `systems/factions/`. The behaviour they pinned lives on in `_run_and_grade`, the function `resolve_field`
# (the season's entry point) and the deleted adapter both called, so they now drive that directly with
# units built by `_weighted_unit`.

def _units():
    from systems.mass_battle.sim.massbattle import _weighted_unit
    return _weighted_unit('side_a', 10), _weighted_unit('side_b', 10)


def test_run_and_grade_accepts_every_row_without_crashing():
    """`_run_and_grade`'s `terrain` parameter went from always-None (a [GAP], silently discarded)
    to a real value -- every row this lookup can produce must be a safe, non-crashing input, even the
    ones with no mechanical effect wired yet."""
    from systems.mass_battle.sim.massbattle import _run_and_grade

    for row in (NARROW_PASS, UPHILL, FOREST_BROKEN, WALLS, OPEN_FLAT, 'river_crossing', None):
        a, b = _units()
        r = _run_and_grade(a, b, row, None)
        assert 'attacker_wins' in r


def test_forest_broken_forces_a_fast_side_to_standard_speed():
    """A.9: 'Forest / broken: Cavalry -> Standard' -- the one branch this pass wires inside
    `_run_and_grade`. [CORRECTED, adversarial review 2026-09-27] This proves the FIELD WRITE
    happens through the real function, not just in isolation -- it does NOT prove the write has any
    downstream effect. It does not: `run_battle` (what this function actually calls) never reads
    `.speed` at all, so this branch is inert on its own terms. See `_run_and_grade`'s own docstring."""
    from systems.mass_battle.sim.massbattle import _run_and_grade

    a, b = _units()
    # The pre-condition this test depends on: `_weighted_unit`'s armies are never Fast by
    # construction, so a Fast side is patched in after construction to actually exercise the branch.
    assert a.speed != 'Fast', \
        "if this ever changes, the FOREST_BROKEN branch stops being vacuous on the season path " \
        "and the patching below becomes unnecessary -- not a failure, but worth noticing"
    a.speed = 'Fast'
    _run_and_grade(a, b, FOREST_BROKEN, None)
    assert a.speed == 'Standard', "a Fast side must be forced to Standard when terrain is forest_broken"


def test_walls_raise_the_defenders_dr_and_only_the_defenders_dr():
    """A.9: 'Walls / fortifications | Defender +3 DR' (plan position `20-iv`). Pins WHICH unit takes the
    bonus and that it lands once: the defender is `unit_b` (`march` is the only verb contesting a field,
    and its target side is `other`). The control is the same pair on OPEN_FLAT, whose DR must not move.
    The stochastic 8-seed test in `test_mass_battle_provider.py` cannot tell the sides apart."""
    from systems.mass_battle.sim.massbattle import _run_and_grade
    from systems.mass_battle.sim.terrain import WALLS_DEFENDER_DR

    a, b = _units()
    a0, b0 = a.dr, b.dr
    _run_and_grade(a, b, WALLS, None)
    assert b.dr == b0 + WALLS_DEFENDER_DR, "the defender (unit_b) must take A.9's walls bonus, once"
    assert a.dr == a0, "the attacker (unit_a) must not take the walls bonus"

    a, b = _units()
    a0, b0 = a.dr, b.dr
    _run_and_grade(a, b, OPEN_FLAT, None)
    assert (a.dr, b.dr) == (a0, b0), "OPEN_FLAT must not touch DR (control)"


def test_walls_dr_override_replaces_a9s_number_only_on_a_walls_field():
    """Plan position `20-v` (`H-150`): `walls_dr` is what the season's `field_walls_dr` fixture hands
    in. An int REPLACES `WALLS_DEFENDER_DR` on the defender (0 = the control, 1, and A.9's own number
    spelled out must equal the `None` default), and on a field that is not WALLS it is inert -- the
    control that stops the parameter reading as a general DR knob."""
    from systems.mass_battle.sim.massbattle import _run_and_grade
    from systems.mass_battle.sim.terrain import WALLS_DEFENDER_DR

    seen = {}
    for label, walls_dr in (('none', None), ('a9', WALLS_DEFENDER_DR), ('zero', 0), ('one', 1)):
        a, b = _units()
        a0, b0 = a.dr, b.dr
        _run_and_grade(a, b, WALLS, None, walls_dr=walls_dr)
        seen[label] = b.dr - b0
        assert a.dr == a0, f"{label}: the attacker must never take the walls bonus"
    assert seen == {'none': WALLS_DEFENDER_DR, 'a9': WALLS_DEFENDER_DR, 'zero': 0, 'one': 1}, seen

    a, b = _units()
    a0, b0 = a.dr, b.dr
    _run_and_grade(a, b, OPEN_FLAT, None, walls_dr=1)
    assert (a.dr, b.dr) == (a0, b0), "walls_dr must be inert off a WALLS field (control)"


def test_open_flat_does_not_touch_speed():
    """Control: the same Fast side, OPEN_FLAT terrain, must stay Fast (no modifier is A.9's own
    definition of the open-flat row)."""
    from systems.mass_battle.sim.massbattle import _run_and_grade

    a, b = _units()
    a.speed = 'Fast'
    _run_and_grade(a, b, OPEN_FLAT, None)
    assert a.speed == 'Fast', "OPEN_FLAT must not touch speed (control)"
