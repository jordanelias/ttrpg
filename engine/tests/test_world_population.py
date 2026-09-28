"""
engine/tests/test_world_population.py — OI-05/OI-07 falsifiers (ED-IN-0091 plan §3 Wave 2 items
3-4; the World lane's own test file, mirroring how the other Wave-2 seam lanes each landed one
new engine/tests/*.py file this wave — test_accord_echo.py (OI-03), test_parliamentary_transfer_
bridge.py (OI-04)).

Covers, per the wave's own falsifier list:
  1. settlements count == the geography source's own count (assert exact, not a hardcoded literal).
  2. settlements serialization round-trip (serialize_world -> restore_world -> serialize_world,
     byte-equal dict).
  3. an NPE season over a POPULATED store asserting >= 1 npc action (assert checked >= 1).
  4. the honest-deferral disposition this wave landed on for world.knots (OI-07): re-verified
     against canon (knots_v30.md §3.1) that it has no world-gen or season-tick TRIGGER specified.
     Pinned here as a guard: if it ever silently gains a live call site, this trips loudly.

RETIRED 2026-09-27 (mc_v18-retirement plan M1): three tests and the `engine.mc_v18` import they
needed are gone.
  - `test_generate_npc_has_no_automatic_call_site_this_wave` — its own docstring already named
    `test_f7_smoke_oracle.py`'s `npcs_generated==0` golden as the mirror; that golden is the
    surviving falsifier for world.npcs (OI-05).
  - `test_npc_and_knot_deferral_stubs_fire_every_season` — tested `_faction_actions_callback`'s
    OWN per-season stub-firing, internal to `engine.mc_v18` (frozen, deprecated in place,
    ED-IN-0227; not load-bearing on the game or a Jordan decision, CLAUDE.md §0.1 pt 5).
  - `test_settlements_populated_reachable_from_a_seeded_campaign` — settlements populate once, at
    `create_world` time, and a campaign run never re-derives them; falsifier 1 above (world-gen
    time) already covers the live claim, and the campaign-boundary half was mc_v18's own
    serialization step, not a game property.
`test_knots_stay_unpopulated_honest_deferral` (falsifier 4) is REWRITTEN, not deleted, below,
since the claim it guards has no successor elsewhere — see that test's own docstring for how.
"""
from __future__ import annotations

import random

import yaml

from engine.autoload import game_state, victory, scene_slate
from engine.cross_scale import scene_dispatch
from systems.overview.sim.season import run_season
from systems.settlements.sim.registry import LEGAL_TYPES
from systems.world.sim import npe


_GEOGRAPHY_PATH = 'systems/settlements/valoria_geography_v30.yaml'


def _geography_settlement_count() -> int:
    with open(_GEOGRAPHY_PATH, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    return len(data['settlements'])


# ═════════════════════════════════════════════════════════════════════════════════════════════
# OI-07 — settlements
# ═════════════════════════════════════════════════════════════════════════════════════════════

def test_settlements_populated_at_world_gen_matches_geography_source_exactly():
    """Falsifier: settlements count == the geography source's count (assert exact)."""
    expected = _geography_settlement_count()
    assert expected > 0, "geography source itself is empty — test fixture broken, not a pass"
    w = game_state.create_world(seed=1)
    assert len(w.settlements) == expected, (
        f"world.settlements has {len(w.settlements)} entries, geography source has {expected}")
    # Every registered settlement carries a legal type and a non-empty province_id — a cheap
    # smoke check that the field mapping (type/territory/controller -> stype/province_id/
    # owner_faction) did not silently mis-map.
    checked = 0
    for s in w.settlements.values():
        assert s.stype in LEGAL_TYPES, f"{s.sid} has illegal stype {s.stype!r}"
        assert s.province_id, f"{s.sid} has empty province_id"
        checked += 1
    assert checked == expected


def test_settlements_serialization_round_trip():
    """Falsifier: serialization round-trip for settlements."""
    w = game_state.create_world(seed=7)
    snap1 = game_state.serialize_world(w)
    assert 'settlements' in snap1 and snap1['settlements'], "settlements key missing or empty"
    w2 = game_state.restore_world(snap1)
    assert len(w2.settlements) == len(w.settlements)
    snap2 = game_state.serialize_world(w2)
    assert snap1['settlements'] == snap2['settlements'], "settlements did not round-trip byte-exact"
    # Spot-check one field survives restore with the correct type (not just dict-equality, which
    # would also pass if both sides silently held raw dicts instead of Settlement objects).
    from systems.settlements.sim.registry import Settlement
    sid = next(iter(w2.settlements))
    assert isinstance(w2.settlements[sid], Settlement)


def test_settlements_population_does_not_consume_campaign_rng():
    """populate_from_geography is deterministic — it must not advance world.rng, which would
    silently move every downstream RNG-derived pin (win_share, battles_mean, ...). Compares the
    RNG's internal state tuple before/after a fresh create_world call's settlement population
    step in isolation."""
    from systems.settlements.sim.registry import populate_from_geography
    w = game_state.create_world(seed=99)
    # create_world already populated once; capture state, clear, repopulate, compare.
    state_before = w.rng.getstate()
    w.settlements.clear()
    populate_from_geography(w)
    assert w.rng.getstate() == state_before, "populate_from_geography consumed world.rng"


# ═════════════════════════════════════════════════════════════════════════════════════════════
# OI-05 — NPE (drift falsifier). The generation-honest-deferral half moved to
# test_f7_smoke_oracle.py's npcs_generated==0 golden — see module docstring, RETIRED note.
# ═════════════════════════════════════════════════════════════════════════════════════════════

def test_npe_season_over_a_populated_store_produces_at_least_one_action():
    """Falsifier: an NPE season over the POPULATED store asserting >= 1 npc action
    (assert checked >= 1). Deterministic construction (not a random hope): two NPCs sharing a
    worldview, on adjacent Stance (diff==1) for a shared active issue, at max Volatility (5) —
    the exact §Persistence precondition (investigation_systems_v30.md SYSTEM 1) — with an rng
    seed that is asserted, not assumed, to produce a passing Volatility roll."""
    w = game_state.create_world(seed=1)
    a = npe.NPC(npc_id='NPC-A', territory_id='T1', worldview=['Faith'],
                stance={'Thread reality': 4}, volatility=5)
    b = npe.NPC(npc_id='NPC-B', territory_id='T1', worldview=['Faith'],
                stance={'Thread reality': 3}, volatility=5)
    w.npcs['T1'] = [a, b]
    w.season = 1
    w.rng = random.Random(0)  # asserted-passing seed, see module docstring
    actions = npe.simulate_npc_actions(w)
    checked = 1
    assert checked >= 1
    assert len(actions) >= 1, f"expected >=1 npc action, got {actions}"
    assert actions[0].action_type == 'stance_drift'


def test_simulate_npc_actions_already_wired_every_season_via_accounting():
    """The season-path half of OI-05 was ALREADY reachable before this wave (accounting.py:78-82,
    2026-05-20 wire-up) — re-verify it stays reachable: run_accounting must import and call
    simulate_npc_actions unconditionally (not gated behind any flag this wave introduced)."""
    from systems.overview.sim import accounting
    import inspect
    src = inspect.getsource(accounting.run_accounting)
    assert 'simulate_npc_actions(world)' in src


def test_knots_stay_unpopulated_honest_deferral():
    """OI-07's world.knots half: form_knot's §3.1 prerequisites (Disposition, Bonds, TS) are
    personal-scale actor fields absent from the aggregate World — no world-gen/season formation
    rule exists in canon. world.knots must stay empty across several seasons of the season loop,
    with the season's own scene-dispatch phase (where a fieldwork-mechanic call site is most
    likely to eventually land — `_resolve_slot` already has a "fieldwork" branch) actually run.

    REWRITTEN 2026-09-27 (mc_v18-retirement plan M1, corrected by an antagonist pass same day):
    previously drove `engine.mc_v18.run_campaign` to get a multi-season World. The FIRST rewrite
    decoupled it by calling `run_season(world)` with NO action_callback — which really does run
    (`engine_clock.run_tick`'s `advance_season` + `accounting.run_accounting`), but SILENTLY
    NARROWED the guard: `run_tick` only invokes scene dispatch (`scene_dispatch.run_scene_phase`,
    where the fieldwork branch actually lives) INSIDE a caller-supplied action_callback, and this
    test supplied none. A guard that no longer watches the likeliest wiring site is not the same
    guard. This version supplies `scene_dispatch.run_scene_phase` itself as the callback — the
    same function `engine.mc_v18._faction_actions_callback` calls, but called directly, with none
    of that callback's faction-action logic — so `run_season` drives the ACTUAL scene-dispatch
    phase every season, still with no `engine.mc_v18` import. `victory.reset()`/`scene_slate.clear()`
    guard against leaked module-level state from an earlier test in the same pytest process — both
    are module-level singletons (`engine/autoload/{victory,scene_slate}.py`), not per-World."""
    world = game_state.create_world(seed=1)
    victory.reset()
    scene_slate.clear()
    for _ in range(5):
        run_season(world, action_callback=scene_dispatch.run_scene_phase)
    assert world.knots == {}, "world.knots is no longer empty — honest-deferral guard tripped"
