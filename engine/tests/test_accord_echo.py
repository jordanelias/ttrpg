"""
engine/tests/test_accord_echo.py — §5.5 Accord Domain Echo wiring oracle (OI-03,
ED-IN-0091 plan §3 Wave 2).

`domain_echo.compute_accord_echo` had zero callers before this change (grep-verified
2026-07-29, `engine/tests/test_pipeline_reach.py`'s `accord-echo-leg` xfail row). This suite
pins the caller path: `echo_transport.classify_scene_outcome` (the §5.5 outcome classification
step) + `echo_transport.emit_scene_echo`'s call into `compute_accord_echo` + `_apply_accord_echo`'s
write onto `Settlement.order`/RS.

WAVE-2 REWRITE (orchestrator-adjudicated fix batch, 2026-07-29, OI-03 fixes 1-4):
  1. classify_scene_outcome no longer infers an outcome from `scene_type` alone (the prior
     `{"combat": "violence"}` fallback is deleted) — only an explicit caller-declared
     `echo['scene_outcome']` is trusted. `test_classify_combat_maps_to_violence` is REPLACED by
     `test_classify_requires_explicit_declared_outcome_even_for_combat` below.
  2. `_apply_accord_echo` targets the SETTLEMENT where the scene occurred (AUD-SET-02,
     scale_transitions_v30.md:215), never Territory.accord directly — echo_ctx uses
     `target_settlement`, not `target_territory`.
  3. The write applies in canonical-index space directly to `Settlement.order` (the settlement's
     own native 0-5 scale, settlement_layer_v30.md §1.3) — no MULTS/ACCORD_MAP conversion.
  4. The returned key is `accord_applied` (not `accord_changes`), matching the corrected
     zoom_in_out.zoom_out contract (immediate application, not queued).

Known-answer rows per scale_transitions_v30.md §5.5 (lines 208-221):
  - governance, Success -> settlement Order +1 on the named settlement.
  - violence -> RS -1 (immediate, via the rs_track stub) + settlement Order -1 on the named
    settlement.
  - an unmappable (scene_type, degree) / declared-outcome pair -> nothing applied, recorded.

NOT touching engine/tests/test_pipeline_reach.py (Oracle-stage owned) — the manifest-row flip
this change causes is filed via oracle_requests, not edited here.
"""
from engine.autoload import game_state
from engine.cross_scale import domain_echo, echo_transport
from engine.substrate import stubwire
from systems.settlements.sim import registry as settlement_registry


def _world_with_scheduler(seed=42):
    world = game_state.create_world(seed=seed)
    world.echo_scheduler = echo_transport.make_scheduler()
    world.key_log = world.echo_scheduler.log
    world._echo_key_seq = 0
    return world


def _first_settlement_id(world):
    return next(iter(world.settlements))


# ── 1. classify_scene_outcome — pure classification, no world/state effects ──────────────────

def test_classify_requires_explicit_declared_outcome_even_for_combat():
    """WAVE-2 (OI-03 fix 1): the prior `{"combat": "violence"}` scene_type fallback is deleted —
    a combat scene with no declared `echo['scene_outcome']` classifies to None, never guessed
    from scene_type alone (see echo_transport.classify_scene_outcome's docstring for why: a
    resolved combat scene is not the same claim as "a PC publicly initiated territorial-scale
    violence")."""
    assert echo_transport.classify_scene_outcome("combat", "Success", {}) is None
    assert echo_transport.classify_scene_outcome("combat", "Overwhelming", None) is None
    # Even with an echo block present, absent a declared scene_outcome it stays unmapped.
    assert echo_transport.classify_scene_outcome(
        "combat", "Success", {"actor_faction": "Crown", "most_relevant_stat": "Mil"}) is None


def test_classify_contest_is_unmapped_without_a_declared_outcome():
    """No live contest stakes kind (emergency_council) matches a §5.5 row — never guessed."""
    assert echo_transport.classify_scene_outcome("contest", "Success", {}) is None
    assert echo_transport.classify_scene_outcome(
        "contest", "Success", {"actor_faction": "Crown", "most_relevant_stat": "L"}) is None


def test_classify_honors_an_explicit_caller_declared_outcome():
    """A future SC/PC-lane bridge can declare `echo['scene_outcome']` directly; validated
    against the closed §5.5 vocabulary before being trusted."""
    echo = {"scene_outcome": "governance"}
    assert echo_transport.classify_scene_outcome("contest", "Success", echo) == "governance"
    # combat now has NO cited fallback to override -- an explicit declared value is the ONLY way
    # combat ever classifies, and this is it.
    echo2 = {"scene_outcome": "destabilisation"}
    assert echo_transport.classify_scene_outcome("combat", "Success", echo2) == "destabilisation"
    echo3 = {"scene_outcome": "violence"}
    assert echo_transport.classify_scene_outcome("combat", "Success", echo3) == "violence"


def test_classify_rejects_an_out_of_vocabulary_declared_outcome():
    """A bogus `scene_outcome` string is not silently trusted -- falls through to None, never
    passed through unvalidated (WAVE-2: there is no cited fallback left to fall through to)."""
    echo = {"scene_outcome": "not-a-real-row"}
    assert echo_transport.classify_scene_outcome("combat", "Success", echo) is None
    assert echo_transport.classify_scene_outcome("contest", "Success", echo) is None


def test_classify_unknown_scene_type_is_unmapped():
    assert echo_transport.classify_scene_outcome("fieldwork", "Success", {}) is None


# ── 2. emit_scene_echo wiring — known-answer per §5.5 row, assert-that-asserted ──────────────

def test_governance_success_moves_settlement_order_plus_one_on_the_right_settlement():
    world = _world_with_scheduler()
    fid = next(iter(world.factions))
    sid = _first_settlement_id(world)
    world.settlements[sid].order = 2   # mid-range headroom so a +1 clamp never masks the assert
    before = world.settlements[sid].order
    # Snapshot every OTHER settlement's Order BEFORE the call -- comparing against a snapshot
    # taken after the call would be a tautology (comparing state to itself), the exact class of
    # decorative assert this suite's own docstring warns against (CLAUDE.md §0.1 point 2).
    other_sids = [s for s in world.settlements if s != sid]
    assert other_sids, "fixture needs >=2 settlements for this assertion to mean anything"
    other_orders_before = {s: world.settlements[s].order for s in other_sids}

    ctx = {"echo": {"actor_faction": fid, "target_faction": fid, "most_relevant_stat": "L",
                    "degree": "Success", "scene_outcome": "governance",
                    "target_settlement": sid}}
    out = echo_transport.emit_scene_echo("contest", {"winner": "A"}, ctx, world)
    changes = out.get("accord_applied")
    assert changes and len(changes) == 1, f"expected exactly one accord_applied row, got: {out}"
    row = changes[0]
    assert row["applied"] is True and row["target_settlement"] == sid
    assert row["accord_delta"] == 1
    assert world.settlements[sid].order == before + 1, (
        f"settlement Order did not move +1: {before} -> {world.settlements[sid].order}")
    # Wrong settlement is untouched -- assert-that-asserted the loop actually checked something.
    checked = 0
    for other in other_sids:
        assert world.settlements[other].order == other_orders_before[other], (
            f"unrelated settlement {other} moved")
        checked += 1
    assert checked >= 1


def test_violence_moves_rs_and_settlement_order_on_the_right_settlement():
    world = _world_with_scheduler()
    fid = next(iter(world.factions))
    sid = _first_settlement_id(world)
    world.settlements[sid].order = 3   # headroom for a -1 move
    before = world.settlements[sid].order
    stubwire.reset_invocations()
    ctx = {"echo": {"actor_faction": fid, "target_faction": fid, "most_relevant_stat": "Mil",
                    "degree": "Success", "scene_outcome": "violence",
                    "target_settlement": sid}}
    out = echo_transport.emit_scene_echo("combat", {"result": 1}, ctx, world)
    changes = out.get("accord_applied")
    assert changes and len(changes) == 1
    row = changes[0]
    assert row["scene_outcome"] == "violence"
    assert row["accord_delta"] == -1 and row["rs_delta"] == -1
    assert row["applied"] is True
    assert world.settlements[sid].order == before - 1, (
        f"settlement Order did not move -1: {before} -> {world.settlements[sid].order}")
    # RS has no live store yet (OI-17 stub) -- the write routes through rs_track's own declared
    # entry point and self-flags as a typed no-op, not silently dropped.
    assert stubwire.invocations >= 1, "rs_delta must route through rs_track.apply_rs_delta"


def test_territorial_transfer_sets_settlement_order_to_canonical_two():
    world = _world_with_scheduler()
    fid = next(iter(world.factions))
    sid = _first_settlement_id(world)
    world.settlements[sid].order = 4   # deliberately NOT 2, so the assert proves a real move
    ctx = {"echo": {"actor_faction": fid, "target_faction": fid, "most_relevant_stat": "L",
                    "degree": "Success", "scene_outcome": "territorial_transfer",
                    "target_settlement": sid}}
    echo_transport.emit_scene_echo("contest", {"winner": "A"}, ctx, world)
    assert world.settlements[sid].order == 2


def test_settlement_order_never_leaves_the_canonical_0_5_index_bound():
    """OI-03 fix 3 falsifier: a settlement already at STAT_MAX must clamp, not overshoot -- the
    canonical-index bound (registry.STAT_MIN/STAT_MAX) is respected exactly like every other
    settlement.order writer in the tree."""
    world = _world_with_scheduler()
    fid = next(iter(world.factions))
    sid = _first_settlement_id(world)
    world.settlements[sid].order = settlement_registry.STAT_MAX
    ctx = {"echo": {"actor_faction": fid, "target_faction": fid, "most_relevant_stat": "L",
                    "degree": "Success", "scene_outcome": "governance",
                    "target_settlement": sid}}
    echo_transport.emit_scene_echo("contest", {"winner": "A"}, ctx, world)
    assert world.settlements[sid].order == settlement_registry.STAT_MAX


def test_unmappable_pair_fires_false_and_is_recorded_not_guessed():
    """An unmapped scene_type/degree combo -> compute_accord_echo itself returns fires=False;
    nothing is applied and nothing is added to the returned dict for this leg."""
    world = _world_with_scheduler()
    fid = next(iter(world.factions))
    sid = _first_settlement_id(world)
    before = world.settlements[sid].order
    # 'destabilisation' only fires on degree=='Success' per §5.5 -- Overwhelming is an
    # unmappable pair for this row.
    ctx = {"echo": {"actor_faction": fid, "target_faction": fid, "most_relevant_stat": "L",
                    "degree": "Overwhelming", "scene_outcome": "destabilisation",
                    "target_settlement": sid}}
    out = echo_transport.emit_scene_echo("contest", {"winner": "A", "total_victory": True}, ctx, world)
    ar = domain_echo.compute_accord_echo("destabilisation", "Overwhelming", world)
    assert ar.fires is False, "fixture assumption: destabilisation+Overwhelming must not fire"
    assert "accord_applied" not in out, f"unmappable pair must not write Order: {out}"
    assert world.settlements[sid].order == before


def test_no_target_settlement_is_computed_but_not_applied():
    """§5.5 fires, but with no resolvable settlement the write is recorded, never guessed at."""
    world = _world_with_scheduler()
    fid = next(iter(world.factions))
    before = {sid: s.order for sid, s in world.settlements.items()}
    ctx = {"echo": {"actor_faction": fid, "target_faction": fid, "most_relevant_stat": "L",
                    "degree": "Success", "scene_outcome": "governance"}}
    out = echo_transport.emit_scene_echo("contest", {"winner": "A"}, ctx, world)
    changes = out.get("accord_applied")
    assert changes and len(changes) == 1
    assert changes[0]["applied"] is False
    checked = 0
    for sid, s in world.settlements.items():
        assert s.order == before[sid]
        checked += 1
    assert checked >= 1


def test_no_scope_met_suppresses_accord_echo_too():
    """Sufficient Scope (§7) gates §5.5 the same way it gates the §5.2 core (scale_transitions_
    v30.md:55) -- scope_met=False must suppress both, not just the domain-echo leg."""
    world = _world_with_scheduler()
    fid = next(iter(world.factions))
    sid = _first_settlement_id(world)
    before = world.settlements[sid].order
    ctx = {"echo": {"actor_faction": fid, "target_faction": fid, "most_relevant_stat": "L",
                    "degree": "Success", "scene_outcome": "governance",
                    "target_settlement": sid, "scope_met": False}}
    out = echo_transport.emit_scene_echo("contest", {"winner": "A"}, ctx, world)
    assert "accord_applied" not in out
    assert world.settlements[sid].order == before
