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
(2) full A.9 mechanical coverage — `massbattle.py::_run_and_grade` applies FOREST_BROKEN's speed half
("Cavalry -> Standard"), WALLS' defender DR (plan position `20-iv`), and, since MB-05, UPHILL's and
RIVER_CROSSING's dice (plus the crossing's speed step); NARROW_PASS is identified and not applied, and
`_run_and_grade`'s own docstring says why that changes nothing on a one-subunit field. RIVER_CROSSING
comes only from the caller's `river_crossing` signal, which no season caller derives yet.

[CORRECTED, adversarial review 2026-09-27] `terrain_row_for_territory` no longer reads fortification
from the geography YAML — it takes the live `fort_level` as a caller-supplied argument (see its own
docstring for why: the YAML's authored copy and the engine's live, garrison-derived value disagree for
real territories, and reading the authored copy forked a single-owned fact). Every call below that
cares about fortification now passes `fort_level` explicitly rather than reading it off the fixture.
"""
import pytest

from systems.mass_battle.sim.terrain import (
    terrain_row_for_territory, _point_in_polygon, _load_geography, _TYPE_TO_ROW,
    NARROW_PASS, UPHILL, FOREST_BROKEN, WALLS, OPEN_FLAT, RIVER_CROSSING,
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


def test_river_crossing_comes_only_from_the_callers_signal_and_walls_outrank_it():
    """MB-05: RIVER_CROSSING has no polygon route, so the caller's `river_crossing` is its only source.
    T1 resolves OPEN_FLAT by polygon; the signal turns it into the crossing, a positive fortification
    still wins (the module's WALLS > RIVER_CROSSING > polygon assumption), an unknown territory stays the
    no-modifier fallback, and the default (`False`) leaves every territory's polygon row unchanged --
    the half that keeps every season field, none of which passes the signal, where it was."""
    assert terrain_row_for_territory('T1', fort_level=0) == OPEN_FLAT, "T1's polygon row moved"
    assert terrain_row_for_territory('T1', fort_level=0, river_crossing=True) == RIVER_CROSSING
    assert terrain_row_for_territory('T4', fort_level=0, river_crossing=True) == RIVER_CROSSING
    assert terrain_row_for_territory('T1', fort_level=1.0, river_crossing=True) == WALLS
    assert terrain_row_for_territory('T-does-not-exist', fort_level=0, river_crossing=True) == OPEN_FLAT
    geo = _load_geography()
    for tid in geo['provinces']:
        assert (terrain_row_for_territory(tid, fort_level=0, river_crossing=False)
                == terrain_row_for_territory(tid, fort_level=0)), f"{tid}: the default signal moved the row"


# ─── real committed provinces, pinned to their actual row (not just "some valid row") ────────────
# [adversarial review 2026-09-27] the tests above establish the mechanism; these pin actual results
# for actual data, so a regression in the polygon/type-mapping logic (e.g. forest silently resolving
# to OPEN_FLAT) does not pass silently just because OPEN_FLAT is also a valid member of the closed set.

@pytest.mark.parametrize('tid,expected', [
    ('T4', UPHILL),          # terrain-highland-grauwald; anchor [1090,1430] inside [970-1170]x[1300-1480]
    ('T7', FOREST_BROKEN),   # terrain-forest-rendstad; anchor [720,800] inside [420-970]x[700-1000]
    ('T6', FOREST_BROKEN),   # terrain-marsh-stillhelm (marsh -> FOREST_BROKEN); anchor [1180,2300]
    # MB-05: the territory of `set_s_036`, the target `engine/season/tests/test_mass_battle_provider.py`'s
    # uphill test fights over -- that file may not import this lookup, so the row it relies on is pinned here.
    ('T9', UPHILL),
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


# ─── MB-05: the two dice rows, UPHILL and RIVER_CROSSING ─────────────────────────────────────────

def _terrain_dice(u):
    return (u.terrain_off_d, u.terrain_def_d)


@pytest.mark.parametrize('row,attacker,defender', [
    (UPHILL, (-1, 0), (0, 1)),            # A.9: "Defender +1D Def; attacker −1D Off"
    (RIVER_CROSSING, (-1, 0), (0, 0)),    # A.9: "−1D Off", on the crossing side (the attacker)
    (OPEN_FLAT, (0, 0), (0, 0)),          # the control: "No modifiers"
    (WALLS, (0, 0), (0, 0)),              # walls move DR, never dice
])
def test_each_row_puts_its_a9_dice_on_the_right_side_once(row, attacker, defender):
    """Which unit takes which die, and that it lands once -- the stochastic tests below cannot tell the
    sides apart. Spelled as A.9's own numbers, so a constant moved off canon's die count fails here."""
    from systems.mass_battle.sim.massbattle import _run_and_grade

    a, b = _units()
    assert _terrain_dice(a) == _terrain_dice(b) == (0, 0), "a fresh unit already carries terrain dice"
    _run_and_grade(a, b, row, None)
    assert _terrain_dice(a) == attacker and _terrain_dice(b) == defender, (row, _terrain_dice(a), _terrain_dice(b))


@pytest.mark.parametrize('before,after', [('Fast', 'Standard'), ('Standard', 'Slow'), ('Slow', 'Slow')])
def test_river_crossing_steps_the_crosser_one_speed_tier_slower(before, after):
    """A.9: "River crossing | −1 Speed tier" -- the crosser only, floored at Slow. Inert on the season
    path, like forest's speed half (`run_battle` never reads `.speed`); pinned so the write is right
    the day a reader exists."""
    from systems.mass_battle.sim.massbattle import _run_and_grade

    a, b = _units()
    a.speed = before
    _run_and_grade(a, b, RIVER_CROSSING, None)
    assert (a.speed, b.speed) == (after, 'Standard')


@pytest.mark.parametrize('row,zeroed', [
    (UPHILL, ('UPHILL_ATTACKER_OFF_D', 'UPHILL_DEFENDER_DEF_D')),
    (RIVER_CROSSING, ('RIVER_CROSSING_OFF_D',)),
])
def test_a_dice_row_resolves_differently_from_open_flat_and_identically_with_its_dice_zeroed(
        monkeypatch, row, zeroed):
    """MB-05's falsifier, both arms in one run. The same two units and seeds fought on the row and on
    OPEN_FLAT: with the row's A.9 dice zeroed (the pre-MB-05 world, where the row was identified and not
    applied) the two are EQUAL on every seed; with canon's dice they DIFFER on at least one, and the
    defender never ends with fewer survivors. Measured 2026-10-08 (Python 3.11): 0/16 differ before
    MB-05, 3/16 after, for both rows at these weights -- one-off figures, not asserted. RIVER_CROSSING's
    speed step is inert here (see the test above), so the zeroed arm is equal for it too."""
    import random
    from systems.mass_battle.sim import massbattle as MB

    def fight(r, seed):
        a, b = _units()
        return MB._run_and_grade(a, b, r, random.Random(seed))

    checked = differs = 0
    for seed in range(16):
        on_row, flat = fight(row, seed), fight(OPEN_FLAT, seed)
        assert on_row['defender_size_pct'] >= flat['defender_size_pct'], (
            f"{row} seed {seed}: the row left the defender FEWER survivors: {on_row} vs {flat}")
        differs += on_row != flat
        with monkeypatch.context() as m:
            for name in zeroed:
                m.setattr(MB, name, 0)
            assert fight(row, seed) == flat, f"{row} seed {seed}: with its dice zeroed it still differs"
        checked += 1
    assert checked == 16
    assert differs >= 1, f"{row} resolved identically to OPEN_FLAT on every seed"


def test_resolve_field_carries_the_river_crossing_signal_to_the_engine():
    """MB-05: RIVER_CROSSING's season-side test, at `resolve_field` -- the season provider cannot pass
    the signal (it is handed the target rung, not the march's origin), so a provider test could only
    observe `False`. The provider's own fixture sides (the 2-man Crown army mustered at `set_s_014`
    against the Church at `set_s_036`), fought over T1 (OPEN_FLAT by polygon) with and without the
    signal: they differ on at least one of 16 seeds (3, measured 2026-10-08, not asserted), and the
    defenders never end with fewer survivors."""
    import random
    from engine.season.harness.populated import build_realm
    from engine.season.queries import world_q
    from systems.mass_battle.sim.massbattle import resolve_field

    w = build_realm(0)
    att = world_q.mustered(w, 'set_s_014', 'fac_crown')
    dfn = world_q.mustered(w, 'set_s_036', 'fac_church_of_solmund')
    assert att and dfn, "the provider's fixture sides no longer muster"
    checked = differs = 0
    for seed in range(16):
        crossed = resolve_field(w, att, dfn, territory='T1', river_crossing=True, rng=random.Random(seed))
        dry = resolve_field(w, att, dfn, territory='T1', rng=random.Random(seed))
        assert crossed['defender_size_pct'] >= dry['defender_size_pct'], (seed, crossed, dry)
        differs += crossed != dry
        checked += 1
    assert checked == 16
    assert differs >= 1, "the river_crossing signal never reached the engine"
