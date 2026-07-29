"""Falsifier tests for engine/cross_scale/articulation.py's `subscribe_all` (OI-08, ED-IN-0091
plan `audit/2026-07-29-code-shape-open-items/01_orchestration_plan_v1.md` §3 Wave 2 item 6).

`TickScheduler.subscribe` (engine/substrate/keys.py:447) had ZERO callers anywhere in the corpus
before this. `subscribe_all` is the first — it registers a per-invocation stub-wire callback for
every §3.1 trigger type_id (systems/articulation/articulation_layer_v30.md §3.1, lines 77-92) and
renders nothing (the render layer stays ED-IN-0073's docket).

Two claims, each with an assert-that-asserted loop (CLAUDE.md §0.1 point 2 — a loop that asserts
conditionally must assert that it asserted):
  1. `subscribe_all` registers >= 9 of the §3.1 roster's type_ids on the scheduler (the task
     floor). This suite additionally pins the exact count at 10 and documents why: the register's
     claim that `meta.cascade_cluster_event` is unregistered (OI-27b, §5 fork 11) is STALE against
     the working tree — ED-IN-0022 (2026-07-07, C-KEY-8) already registered it in
     key_type_registry_v30.md. `test_all_ten_type_ids_are_registry_valid` is the falsifier for
     that correction: if the registry ever drops the type, this test fails loudly instead of the
     correction silently rotting.
  2. An emitted Key of a subscribed type increments `stubwire.invocations`, end-to-end through a
     real `TickScheduler` (not a mock of the callback) — for every one of the 10 type_ids, each
     with a registry-valid payload built from key_type_registry_v30.md's own
     required_payload_fields, so the test also incidentally proves every payload this module's
     docstring claims is emittable actually validates.
"""
from __future__ import annotations

import pytest

from engine.cross_scale import articulation
from engine.substrate import stubwire
from engine.substrate.keys import (
    EmittedAt,
    Key,
    KeyLog,
    TickScheduler,
    TypeRegistry,
    Visibility,
)

REGISTRY_PATH = "systems/_architecture/key_type_registry_v30.md"

# The §3.1 roster (articulation_layer_v30.md lines 77-92), same order as
# articulation._TRIGGER_TYPE_IDS. Each entry supplies a registry-valid payload built from that
# type's required_payload_fields in key_type_registry_v30.md, plus an EXPLICIT scale_signature
# (never relying on apply_defaults' default_scale_signature — meta.cascade_cluster_event's default
# entry parses as a mis-shaped multi-word string, not a clean list, a pre-existing registry-prose
# defect this test sidesteps rather than silently depends on; out of OI-08's scope to fix).
_PAYLOADS = {
    "state.scar_acquired": dict(
        payload={
            "npc_id": "npc_a", "conviction": "hierarchical",
            "scar_count_before": 0, "scar_count_after": 1,
            "triggering_event_key": "seed_key",
        },
        scale_signature=["personal"],
    ),
    "state.coup_attempted": dict(
        payload={
            "faction_id": "faction_a", "challenger_id": "npc_b",
            "incumbent_id": "npc_a", "outcome": "failure",
        },
        scale_signature=["territory"],
    ),
    "state.succession": dict(
        payload={
            "faction_id": "faction_a", "prior_leader_id": "npc_a",
            "new_leader_id": "npc_b", "succession_mode": "contested",
        },
        scale_signature=["territory"],
    ),
    "mechanical.mission_shift": dict(
        payload={
            "faction_id": "faction_a", "prior_mission": "hold",
            "new_mission": "expand", "trigger": "authored",
        },
        scale_signature=["territory"],
    ),
    "da.covert_betrayal": dict(
        payload={
            "faction_id": "faction_a", "target_actor": "npc_b",
            "target_faction": None, "exposed": True,
        },
        scale_signature=["territory"],
    ),
    "meta.knot_formed": dict(
        payload={"participants": ["npc_a", "npc_b"], "tier": "Medium"},
        scale_signature=["personal"],
    ),
    "meta.knot_ruptured": dict(
        payload={
            "knot_id": "knot_1", "participants": ["npc_a", "npc_b"],
            "cause": "betrayal",
        },
        scale_signature=["personal"],
    ),
    "env.peninsular_strain_shock": dict(
        payload={
            "strain_delta": 3, "causes": [], "affected_territories": ["territory_a"],
        },
        scale_signature=["peninsula"],
    ),
    "meta.cascade_cluster_event": dict(
        payload={
            "cluster_pair": ["faction_a", "faction_b"], "similarity": 0.62,
            "cluster_type": "aligned", "sustained_seasons": 4,
        },
        scale_signature=["territory"],
    ),
    "state.belief_revised": dict(
        payload={
            "npc_id": "npc_a", "prior_belief": "the_crown_is_just",
            "new_belief": "the_crown_is_corrupt",
        },
        scale_signature=["personal"],
    ),
}


@pytest.fixture(scope="module")
def registry():
    return TypeRegistry.load(REGISTRY_PATH)


def _sched(registry):
    return TickScheduler(KeyLog(registry), cascade_depth_max=3, emissions_per_tick_max=50)


def _key(kid, type_id, season=0):
    spec = _PAYLOADS[type_id]
    return Key(
        id=kid,
        type=type_id,
        emitted_at=EmittedAt(season_index=season),
        scale_signature=list(spec["scale_signature"]),
        visibility=Visibility(public=True),
        payload=dict(spec["payload"]),
    )


# -- claim 1: the roster is registered ----------------------------------------------------------

def test_trigger_roster_matches_articulation_layer_v30_section_3_1():
    # Pin the exact roster against the design doc's own 10 type_ids (order-independent), so a
    # future doc edit that adds/removes a trigger row is caught here rather than silently
    # diverging from the module's hardcoded tuple.
    expected = {
        "state.scar_acquired", "state.coup_attempted", "state.succession",
        "mechanical.mission_shift", "da.covert_betrayal", "meta.knot_formed",
        "meta.knot_ruptured", "env.peninsular_strain_shock",
        "meta.cascade_cluster_event", "state.belief_revised",
    }
    assert set(articulation._TRIGGER_TYPE_IDS) == expected
    assert len(articulation._TRIGGER_TYPE_IDS) == 10


def test_all_ten_type_ids_are_registry_valid(registry):
    # The G12 correction's falsifier: if meta.cascade_cluster_event (or any other §3.1 type_id)
    # is ever dropped from key_type_registry_v30.md, this fails loudly instead of subscribe_all
    # silently registering a type the runtime substrate would reject on first emission.
    checked = 0
    for type_id in articulation._TRIGGER_TYPE_IDS:
        assert type_id in registry.types, type_id
        checked += 1
    assert checked == 10  # assert-that-asserted (CLAUDE.md §0.1 point 2)


def test_subscribe_all_registers_at_least_nine(registry):
    s = _sched(registry)
    count = articulation.subscribe_all(s)
    assert count >= 9  # the task's own floor
    assert count == 10  # this module's actual, corrected roster (see class docstring)


def test_subscribe_all_registers_one_callback_per_type_id(registry):
    s = _sched(registry)
    articulation.subscribe_all(s)
    checked = 0
    for type_id in articulation._TRIGGER_TYPE_IDS:
        assert type_id in s.subscriptions, type_id
        assert len(s.subscriptions[type_id]) == 1, type_id
        checked += 1
    assert checked == 10


def test_subscribe_all_touches_no_other_type(registry):
    # A subscriber for a §3.1 type must not accidentally register on an unrelated bus type
    # (declared I/O only — ED-1083 guardrail: no interface dialect beyond what §3.1 declares).
    s = _sched(registry)
    articulation.subscribe_all(s)
    assert set(s.subscriptions.keys()) == set(articulation._TRIGGER_TYPE_IDS)


# -- claim 2: an emitted Key of a subscribed type fires the stub end-to-end ----------------------

def test_emitted_key_increments_stubwire_counter_for_every_trigger_type(registry):
    s = _sched(registry)
    articulation.subscribe_all(s)
    checked = 0
    for i, type_id in enumerate(articulation._TRIGGER_TYPE_IDS):
        stubwire.reset_invocations()
        assert stubwire.invocations == 0
        s.emit(_key(f"k{i}", type_id))
        assert stubwire.invocations == 1, type_id  # exactly one callback fired, once
        checked += 1
    assert checked == 10  # assert-that-asserted


def test_unsubscribed_type_does_not_fire_the_stub(registry):
    # scene.dialogue is registered in key_type_registry_v30.md but is NOT one of §3.1's 10
    # triggers — subscribe_all must not have opted articulation into it.
    s = _sched(registry)
    articulation.subscribe_all(s)
    stubwire.reset_invocations()
    s.emit(Key(
        id="k_dialogue",
        type="scene.dialogue",
        emitted_at=EmittedAt(season_index=0),
        scale_signature=["personal"],
        visibility=Visibility(public=True),
        payload={"exchange_count": 1, "initiator_id": "npc_a", "topic": "harvest"},
    ))
    assert stubwire.invocations == 0


def test_callback_return_is_a_typed_stub_that_stores_nothing(registry):
    # The callback itself: call it directly (as TickScheduler would) and check the shape — no
    # invented state, no rendering, `stub=True` by construction (StubResult.__init__ forbids the
    # caller from setting stub=False, per stubwire.py's own contract).
    s = _sched(registry)
    articulation.subscribe_all(s)
    callback = s.subscriptions["state.belief_revised"][0]
    key = _key("k_direct", "state.belief_revised")
    result = callback(key, s)
    assert result.stub is True
    assert result.module == "engine.cross_scale.articulation"
    assert "ED-IN-0073" in result.reason


def test_subscribe_all_called_twice_double_registers_and_double_fires(registry):
    # Documented (non-idempotent) behavior per subscribe_all's own docstring: TickScheduler.subscribe
    # is purely additive. This test pins that contract so a future accidental double-call at a
    # production call site is visible as "2 fires per Key", not silently swallowed.
    s = _sched(registry)
    articulation.subscribe_all(s)
    articulation.subscribe_all(s)
    assert len(s.subscriptions["state.scar_acquired"]) == 2
    stubwire.reset_invocations()
    s.emit(_key("k_double", "state.scar_acquired"))
    assert stubwire.invocations == 2
