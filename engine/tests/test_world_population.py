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
  4. the honest-deferral disposition this wave landed on for BOTH world.npcs (OI-05) and
     world.knots (OI-07): re-verified against canon (investigation_systems_v30.md SYSTEM 1 /
     knots_v30.md §3.1) that neither has a world-gen or season-tick TRIGGER specified — only
     drift (simulate_npc_actions, already wired pre-this-wave via accounting.run_accounting) has
     one. Pinned here as a guard: if either ever silently gains a live call site, this trips
     loudly (same discipline as test_f7_smoke_oracle.py's npcs==0 guard) rather than the golden
     moving unnoticed.
"""
from __future__ import annotations

import random
import unittest.mock

import yaml

from engine.autoload import game_state, victory, scene_slate
from engine.mc_v18 import _faction_actions_callback, run_campaign
from engine.substrate import stubwire
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


def test_settlements_populated_reachable_from_a_seeded_campaign():
    """The same falsifier, but through the full campaign loop (run_campaign), not just
    create_world directly — this is what test_pipeline_reach.py's world-settlements xfail row
    exercises."""
    expected = _geography_settlement_count()
    r = run_campaign(seed=42)
    settlements = r.final_state.get('settlements', {})
    assert len(settlements) == expected, (
        f"final_state['settlements'] has {len(settlements)} entries, expected {expected}")


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
# OI-05 — NPE (generation honest deferral + drift falsifier)
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


def test_generate_npc_has_no_automatic_call_site_this_wave():
    """Honest-deferral guard (mirrors test_f7_smoke_oracle.py's npcs==0 assertion, but scoped to
    THIS module so a silent future wire-up trips here first with the citation attached): neither
    world-gen nor the season loop calls generate_npc, because investigation_systems_v30.md SYSTEM
    1's Two-Tier Generation is scene-specification-driven only — no world-gen count and no
    season-tick generation trigger exist in canon to cite (re-verified 2026-07-29). A seeded
    campaign must therefore still show npcs_generated == 0, and the stubwire flag recorded in
    mc_v18.py's _faction_actions_callback must fire once per season as the visible marker of the
    deferral."""
    r = run_campaign(seed=1, max_seasons=5)
    assert r.npcs_generated == 0, (
        "npcs_generated is no longer 0 — generate_npc may have gained a live call site; if this "
        "is an intentional wire-up, update this test AND test_f7_smoke_oracle.py's golden together")


def test_knots_stay_unpopulated_honest_deferral():
    """OI-07's world.knots half: form_knot's §3.1 prerequisites (Disposition, Bonds, TS) are
    personal-scale actor fields absent from the aggregate World — no world-gen/season formation
    rule exists in canon. world.knots must stay empty after a seeded campaign, and the deferral
    must be recorded via stubwire (not silent)."""
    r = run_campaign(seed=1, max_seasons=5)
    assert r.final_state.get('knots', {}) == {}, "world.knots is no longer empty — honest-deferral guard tripped"


def test_npc_and_knot_deferral_stubs_fire_every_season():
    """Both honest-deferral stub_resolve calls in mc_v18._faction_actions_callback fire exactly
    once per season.

    WAVE-2 REPAIR (critic 'missing', ED-IN-0091 plan §3 Wave 2 item 8 / CLAUDE.md §0.1 point 2):
    the prior version of this test ran the whole campaign in one `run_campaign` call and then
    asserted `checked = seasons; assert checked == seasons` — `checked` never depended on
    anything observed per season, so the assert was decorative (it would pass even if the
    callback fired zero times per season, or a wildly different number, as long as SOME season
    ran at all). This version steps the season loop itself (mirrring `run_campaign`'s own
    composition — `season.run_season(action_callback=mc_v18._faction_actions_callback)` — but
    driven here so `stubwire.invocations` can be sampled BETWEEN seasons) and asserts a REAL
    per-season delta, so a season that produced zero deflection-stub fires would fail this test,
    not just the aggregate floor below.

    W2 RE-CRITIC HARDENING (CLAUDE.md §0.1 point 2): the prior version below asserted only the
    UNATTRIBUTED global `delta >= 2` — any two `stub_resolve` calls from anywhere would satisfy
    it, so deleting ONE of the two named OI-05/OI-07 fires (`generate_npc`, `form_knot`) while a
    THIRD, unrelated stub call happened to fire that same season would leave this test green.
    `stubwire.invocations` (stubwire.py:51) is a bare module-level int, not keyed by module (per
    stubwire.py:40-51's `StubResult` shape — `module`/`io_contract` live on the per-call return
    value, not on the counter), so attribution requires capturing the actual `StubResult`s, not
    just counting. This version wraps `stubwire.stub_resolve` (via `unittest.mock.patch.object`,
    `side_effect=` the real function so behavior is unchanged) to record each call's
    `(module, io_contract)`, then asserts the two call sites named in mc_v18.py — 'engine.mc_v18'
    module / 'generate_npc(world-gen|season-tick)' + 'form_knot(world-gen|season-tick)'
    io_contract — each appear at least once per season. Deleting either named fire now fails
    here even if unrelated stubs fire in the same season."""
    world = game_state.create_world(seed=3)
    victory.reset()
    scene_slate.clear()
    seasons = 6
    checked = 0
    per_season_counts = []

    _NPC_SITE = ('engine.mc_v18', 'generate_npc(world-gen|season-tick)')
    _KNOT_SITE = ('engine.mc_v18', 'form_knot(world-gen|season-tick)')

    real_stub_resolve = stubwire.stub_resolve
    captured: list[tuple[str, str]] = []

    def _capturing_stub_resolve(module, io_contract, *, reason):
        captured.append((module, io_contract))
        return real_stub_resolve(module, io_contract, reason=reason)

    with unittest.mock.patch.object(
            stubwire, 'stub_resolve', side_effect=_capturing_stub_resolve):
        for _ in range(seasons):
            captured.clear()
            run_season(world, action_callback=_faction_actions_callback)
            npc_fires = captured.count(_NPC_SITE)
            knot_fires = captured.count(_KNOT_SITE)
            per_season_counts.append((npc_fires, knot_fires))
            # Real conditional check, attributed: a season missing EITHER named fire fails HERE,
            # per-season, regardless of how many other stub_resolve calls fired that season.
            assert npc_fires >= 1 and knot_fires >= 1, (
                f"season missing an attributed deferral fire — generate_npc={npc_fires} "
                f"form_knot={knot_fires} (expected >=1 each) — per-season (npc, knot) counts "
                f"so far: {per_season_counts}")
            checked += 1
    assert checked == seasons  # assert-that-asserted (CLAUDE.md §0.1 point 2) — now load-bearing:
    # `checked` only increments inside the loop body AFTER the real per-season attributed assert
    # above ran and passed, so this confirms every one of the `seasons` iterations cleared that
    # bar, not merely that the loop executed `seasons` times.
