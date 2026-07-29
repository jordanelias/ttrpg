"""Falsifier tests for engine/cross_scale/articulation.py's `subscribe_all` (OI-08, ED-IN-0091
plan `audit/2026-07-29-code-shape-open-items/01_orchestration_plan_v1.md` §3 Wave 2 item 6;
extended to 12 type_ids by OI-22a, plan §3 Wave 3 item 1, then to 13 by OI-03, plan §3 Wave 3
item 1 (scene.accord_echo)).

`TickScheduler.subscribe` (engine/substrate/keys.py:447) had ZERO callers anywhere in the corpus
before this. `subscribe_all` is the first — it registers a per-invocation stub-wire callback for
every §3.1 trigger type_id (systems/articulation/articulation_layer_v30.md §3.1: the original
10-row table at lines 77-92, rows #11/#12 added Wave 3 ED-IN-0004, row #13 added Wave 3 OI-03) and
renders nothing (the render layer stays ED-IN-0073's docket).

Three claims, each with an assert-that-asserted loop (CLAUDE.md §0.1 point 2 — a loop that asserts
conditionally must assert that it asserted):
  1. The roster `articulation._TRIGGER_TYPE_IDS` matches the design doc's §3.1 table FOR REAL (W3
     item 6, critic HIGH repair): `test_trigger_roster_matches_articulation_layer_v30_section_3_1`
     below now genuinely PARSES the table out of `articulation_layer_v30.md` (each row's `Trigger
     condition` cell opens with the type_id in backticks) instead of comparing against a second,
     independently-hardcoded `expected` set — a doc edit that adds/removes/renames a row now
     actually fails this test instead of both copies silently drifting together.
  2. `subscribe_all` registers >= 9 of the §3.1 roster's type_ids on the scheduler (the task
     floor). This suite additionally pins the exact count at 13 and documents why: the register's
     claim that `meta.cascade_cluster_event` is unregistered (OI-27b, §5 fork 11) is STALE against
     the working tree — ED-IN-0022 (2026-07-07, C-KEY-8) already registered it in
     key_type_registry_v30.md. `test_all_thirteen_type_ids_are_registry_valid` is the falsifier for
     that correction: if the registry ever drops a type, this test fails loudly instead of the
     correction silently rotting. Wave 3 added `scene.combat_resolved`/`scene.combat_felled` (OI-22a
     — the combat-pair dangling-emit closure for articulation, the one declared `consuming_systems`
     member of that pair with runtime) and `scene.accord_echo` (OI-03 — the §5.5 Accord Echo leg's
     equivalent closure).
  3. An emitted Key of a subscribed type increments `stubwire.invocations`, end-to-end through a
     real `TickScheduler` (not a mock of the callback) — for every one of the 13 type_ids, each
     with a registry-valid payload built from key_type_registry_v30.md's own
     required_payload_fields, so the test also incidentally proves every payload this module's
     docstring claims is emittable actually validates.
"""
from __future__ import annotations

import os
import re

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
ARTICULATION_DOC_PATH = "systems/articulation/articulation_layer_v30.md"
_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def _parse_section_3_1_trigger_type_ids() -> set[str]:
    """Parse the §3.1 table's type_ids directly out of the design doc (W3 item 6, critic HIGH —
    doc<->code drift falsifier). Every §3.1 table row's `Trigger condition` cell opens with the
    type_id in backticks (`` `family.name` `` — verified against all 13 rows 2026-07-29); this
    extracts that token per row, order-independent. CORRECTED (item 7, small/LOW, re-critic pass):
    the actual window is NOT "to the §3.2 boundary" -- there is no `---` rule between §3.1's own
    header and §4's (the next `\n---` after §3.1's start lands at the §3/§4 boundary, past
    §3.2-§3.5). The window genuinely spans §3.1 through §3.5, to the §4 rule. That is safe rather
    than a latent over-capture: §3.2 (Significance function), §3.3 (Accumulated narrative weight),
    §3.4 (Cut scene rendering), and §3.5 (Belief/Inspiration/Knot engagement) contain no numbered
    pipe-table rows opening with a backtick-delimited `family.name` token (verified by direct
    read, 2026-07-29) -- the regex below has nothing to spuriously match in that extra span, so
    the wider window is inert, not a bug. §6's Class-B-extension prose (which DOES also mention
    these type_ids in backticks, in a different shape) still sits safely past the real §4 rule and
    can never leak in and mask a real drift."""
    doc_path = os.path.join(_REPO_ROOT, ARTICULATION_DOC_PATH)
    text = open(doc_path, encoding="utf-8").read()
    start = text.index("### §3.1 Trigger ruleset")
    end = text.index("\n---", start)
    section = text[start:end]
    rx = re.compile(r"^\|\s*\d+\s*\|\s*`([a-z_]+\.[a-z_]+)`", re.MULTILINE)
    return set(rx.findall(section))

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
    # W3 additions (OI-22a, ED-IN-0004): §3.1 rows #11/#12. Required payload fields per
    # key_type_registry_v30.md:899-915 (scene.combat_resolved) / :953-966 (scene.combat_felled)
    # (re-derived round 2, fix-round-2 — was :873-889/:927-940, itself already stale by the time
    # it landed; see articulation.py's ROUND 2 stale-citation correction comment).
    "scene.combat_resolved": dict(
        payload={
            "scene_id": "combat_1", "outcome": "attacker_win",
            "participants": ["npc_a", "npc_b"],
        },
        scale_signature=["personal"],
    ),
    "scene.combat_felled": dict(
        payload={"actor_id": "npc_b"},
        scale_signature=["personal"],
    ),
    # W3 addition (OI-03): §3.1 row #13. Required payload fields per
    # key_type_registry_v30.md:969-1006 (scene.accord_echo) (re-derived round 2 — was :943-977).
    "scene.accord_echo": dict(
        payload={
            "scene_outcome": "governance", "target_settlement": "settlement_a",
            "accord_delta": 1,
        },
        scale_signature=["settlement"],
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
    # W3 item 6 (critic HIGH): genuinely PARSE the §3.1 table out of the doc instead of comparing
    # against a second, independently-hardcoded set — a doc edit that adds/removes/renames a row
    # now actually fails this test, both directions (doc has something code doesn't, and vice
    # versa), instead of two copies silently drifting together.
    doc_type_ids = _parse_section_3_1_trigger_type_ids()
    assert doc_type_ids, "§3.1 table parse returned zero type_ids — parser or doc structure broke"
    assert set(articulation._TRIGGER_TYPE_IDS) == doc_type_ids, (
        f"articulation._TRIGGER_TYPE_IDS drifted from articulation_layer_v30.md §3.1: "
        f"code-only={set(articulation._TRIGGER_TYPE_IDS) - doc_type_ids}, "
        f"doc-only={doc_type_ids - set(articulation._TRIGGER_TYPE_IDS)}")
    assert len(articulation._TRIGGER_TYPE_IDS) == 13


def test_all_thirteen_type_ids_are_registry_valid(registry):
    # The G12 correction's falsifier: if meta.cascade_cluster_event (or any other §3.1 type_id)
    # is ever dropped from key_type_registry_v30.md, this fails loudly instead of subscribe_all
    # silently registering a type the runtime substrate would reject on first emission.
    checked = 0
    for type_id in articulation._TRIGGER_TYPE_IDS:
        assert type_id in registry.types, type_id
        checked += 1
    assert checked == 13  # assert-that-asserted (CLAUDE.md §0.1 point 2)


def test_subscribe_all_registers_at_least_nine(registry):
    s = _sched(registry)
    count = articulation.subscribe_all(s)
    assert count >= 9  # the task's own floor
    assert count == 13  # this module's actual, corrected roster (see class docstring)


def test_subscribe_all_registers_one_callback_per_type_id(registry):
    s = _sched(registry)
    articulation.subscribe_all(s)
    checked = 0
    for type_id in articulation._TRIGGER_TYPE_IDS:
        assert type_id in s.subscriptions, type_id
        assert len(s.subscriptions[type_id]) == 1, type_id
        checked += 1
    assert checked == 13


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
    assert checked == 13  # assert-that-asserted


def test_unsubscribed_type_does_not_fire_the_stub(registry):
    # scene.dialogue is registered in key_type_registry_v30.md but is NOT one of §3.1's 13
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


# -- OI-22a (W3): the combat-pair dangling-emit closure, isolated ------------------------------

def test_combat_pair_reaches_the_articulation_subscriber(registry):
    """OI-22a falsifier: `scene.combat_resolved`/`scene.combat_felled` are the two dangling
    combat-pair emits (key_type_registry_v30.md:899-915/953-966, re-derived round 2 — was
    :873-889/:927-940 — declares articulation a consuming_systems member of both). This is the
    direct, isolated proof that articulation's
    subscription actually receives each — not just that it's present in `_TRIGGER_TYPE_IDS`
    (test_trigger_roster_matches... already checks that) but that a REAL emitted Key of each
    type reaches a REAL callback through a REAL TickScheduler, exactly the "≥1 consumed
    scene.combat_resolved" claim the wave's exit criterion names."""
    s = _sched(registry)
    articulation.subscribe_all(s)
    checked = 0
    for i, type_id in enumerate(("scene.combat_resolved", "scene.combat_felled")):
        stubwire.reset_invocations()
        s.emit(_key(f"kcombat{i}", type_id))
        assert stubwire.invocations == 1, type_id
        checked += 1
    assert checked == 2  # assert-that-asserted
