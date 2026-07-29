"""
sim/cross_scale/articulation.py — Articulation Layer — Tier 1 UI Lens, Tier 2 Triggers, Tier 3 Chronicle

Canon source: designs/articulation/articulation_layer_v30.md (PP-688)
Status: [PROVISIONAL — Pass 2l armature stub 2026-05-17]

Dependencies:
  - sim/autoload/game_state
  - sim/personal/knots
  - sim/personal/beliefs

Entry points:
  - render_protagonist_lens(actor_id: str, world: GameState) -> LensState
  - evaluate_articulation_triggers(world: GameState) -> list[Trigger]
  - generate_chronicle_entry(event, world: GameState) -> ChronicleEntry

"""
from __future__ import annotations

from engine.substrate import stubwire

# [PROVISIONAL — Pass 2l armature stub; implementation pending against canonical source]
#
# OI-17 (ED-IN-0091 plan §2.2/§3 Wave 1): converted from an unconditional
# `raise NotImplementedError` to the single-owner stub-wire primitive (engine/substrate/stubwire.py,
# plan §2.1) — a typed no-op instead of a crash, visible to structure_audit's `stub_wired`
# attribute and review_core's `stubs.count` ratchet by construction (greppable import, no second
# registry). `io_contract` below cites this module's own docstring "Entry points" declaration.
#
# SELF-FLAG ONLY (plan §3 Wave 1 task A scope note): this converts the unconditional raises to
# stub-wire calls and stops there. The minimal bus subscriber is Wave 2 item 6 (OI-08); the render
# layer stays ED-IN-0073's docket. Do not build either here.


def render_protagonist_lens(actor_id: str, world: GameState):
    return stubwire.stub_resolve(
        'engine.cross_scale.articulation',
        'render_protagonist_lens(actor_id: str, world: GameState) -> LensState',
        reason='Pass 2l armature stub, implementation pending against canonical source '
               '(designs/articulation/articulation_layer_v30.md, PP-688); OI-17, ED-IN-0091 plan §2.2; '
               'render layer stays ED-IN-0073 docket')


def evaluate_articulation_triggers(world: GameState):
    return stubwire.stub_resolve(
        'engine.cross_scale.articulation',
        'evaluate_articulation_triggers(world: GameState) -> list[Trigger]',
        reason='Pass 2l armature stub, implementation pending against canonical source '
               '(designs/articulation/articulation_layer_v30.md, PP-688); OI-17, ED-IN-0091 plan §2.2; '
               'minimal subscriber is Wave 2 item 6 (OI-08)')


def generate_chronicle_entry(event, world: GameState):
    return stubwire.stub_resolve(
        'engine.cross_scale.articulation',
        'generate_chronicle_entry(event, world: GameState) -> ChronicleEntry',
        reason='Pass 2l armature stub, implementation pending against canonical source '
               '(designs/articulation/articulation_layer_v30.md, PP-688); OI-17, ED-IN-0091 plan §2.2; '
               'render layer stays ED-IN-0073 docket')


# --- OI-08 (ED-IN-0091 plan §3 Wave 2 item 6) ------------------------------------------------
# The minimal Key-bus subscriber. TickScheduler.subscribe (engine/substrate/keys.py:447) has
# ZERO callers anywhere in the corpus prior to this — articulation is the first. Kills the
# zero-subscriber state without inventing the render layer: each callback below is a
# per-invocation stub-wire flag that observes the emitted Key and returns, storing nothing and
# rendering nothing. The render layer stays ED-IN-0073's docket (Q1-Q4 qualitative-rendering
# fork, unbuilt) — do not build it here.
#
# Trigger roster: systems/articulation/articulation_layer_v30.md §3.1 (the 13-row table,
# rows 1-10 at lines 77-92, rows #11/#12 added W3 item 1 (combat pair) and row #13 added W3
# item 1 (scene.accord_echo, OI-03) immediately below the table).
#
# G12 CORRECTION (2026-07-29, verified against the working tree — not executed as written):
# both the register (OI-27, 00_open_items_register.md) and this wave's own preflight/header
# comment describe `meta.cascade_cluster_event` as "UNREGISTERED in the key-type registry" (OI-27b,
# §5 fork 11) and instruct subscribing to only the other 9, recording the 10th as held-on-fork.
# That premise is STALE: ED-IN-0022 (2026-07-07, C-KEY-8) already registered it in
# systems/_architecture/key_type_registry_v30.md ("### meta.cascade_cluster_event", ~line 862,
# with a full required_payload_fields yaml block whose own notes say "RETROACTIVE registration
# ... closes the dangling-type defect"). Verified by loading the live registry through the actual
# runtime parser: `'meta.cascade_cluster_event' in TypeRegistry.load(
# 'systems/_architecture/key_type_registry_v30.md').types` is True, alongside all other 9 §3.1
# type_ids. No new key type is registered by this module (that stays Wave 3/J territory per the
# task's own constraint) — the type already existed in the working tree; this module only calls
# the existing `TickScheduler.subscribe` on it, exactly as it does for the other 9. All 10 §3.1
# type_ids are therefore subscribed; none is held back.
#
# W3 ADDITION (2026-07-29, OI-22a / ED-IN-0004 execution, ED-IN-0091 plan §3 Wave 3 item 1):
# systems/articulation/articulation_layer_v30.md §3.1 gained trigger rows #11
# (`scene.combat_resolved`) and #12 (`scene.combat_felled`) in the same change — closing the
# combat-pair dangling-emit half of OI-22 for the one declared consuming_systems member
# (key_type_registry_v30.md:899-915/953-966 — re-derived line numbers, see the round-2
# stale-citation correction below) that has runtime: articulation. `npc_behavior` and
# `faction_layer` are also declared consumers there but have zero runtime (systems/npcs/ has no
# .py files; faction_state's consumer wiring is fork-9-gated) — their contract-level `consumes:`
# entries are the L-contracts lane's job this wave (oracle_requests), not this module's; this
# module only ever subscribes for the ONE consumer that can actually run a callback.
#
# STALE-CITATION CORRECTION, ROUND 2 (2026-07-29, re-critic fix round 2, orchestrator-adjudicated):
# the prior correction below (W3 item 5) re-derived the range to :873-889/:927-940 — itself already
# stale by the time it landed, because the registry kept growing mid-wave (the drift root cause
# named by this round's own task: re-deriving citation ranges before the file has finished
# changing). Re-derived a SECOND time, LAST, only after every other edit in this batch to
# key_type_registry_v30.md had landed: `scene.combat_resolved` is at :899-915 (header
# `### scene.combat_resolved` through the closing yaml fence), `scene.combat_felled` is at
# :953-966 (same span shape). Superseded citation: :873-889/:927-940 (round 1, now stale).
#
# W3 ADDITION 2 (2026-07-29, OI-03 execution, ED-IN-0091 plan §3 Wave 3 item 1): row #13
# (`scene.accord_echo`, key_type_registry_v30.md:969-1006 — re-derived round 2, was :943-977) closes
# the same class of gap for the §5.5 Accord Echo leg — `_apply_accord_echo` now builds a real Key
# of this type (echo_transport.py) and the registry already names articulation a consuming_systems
# member; this module is the one consumer with runtime, same discipline as rows #11/#12 above.
# LIVE-but-organically-dormant (see articulation_layer_v30.md §3.1 trigger #13's own note for why
# it fires zero times today).
_TRIGGER_TYPE_IDS = (
    'state.scar_acquired',
    'state.coup_attempted',
    'state.succession',
    'mechanical.mission_shift',
    'da.covert_betrayal',
    'meta.knot_formed',
    'meta.knot_ruptured',
    'env.peninsular_strain_shock',
    'meta.cascade_cluster_event',  # G12-corrected: registered (ED-IN-0022), see note above.
    'state.belief_revised',
    'scene.combat_resolved',       # W3 addition: articulation_layer_v30.md §3.1 row #11, ED-IN-0004.
    'scene.combat_felled',         # W3 addition: articulation_layer_v30.md §3.1 row #12, ED-IN-0004.
    'scene.accord_echo',           # W3 addition: articulation_layer_v30.md §3.1 row #13, OI-03.
)


def _make_trigger_callback(type_id: str):
    """Build the stub-wire callback for one §3.1 trigger type_id.

    The closure captures only `type_id` (a str) — no Key/world state is retained across
    invocations, matching the "stores nothing" contract.
    """

    def _on_key(key, scheduler):
        return stubwire.stub_resolve(
            'engine.cross_scale.articulation',
            f"Tier-2 trigger callback for {type_id!r} "
            "(Key -> Trigger, articulation_layer_v30.md §3.1)",
            reason='OI-08, ED-IN-0091 plan §3 Wave 2 item 6: minimal bus subscriber observes the '
                   'emitted Key at the §3.1 trigger condition and stops — the Tier 2 cut-scene '
                   'render layer stays ED-IN-0073 docket (Q1-Q4 qualitative-rendering fork).')

    return _on_key


def subscribe_all(scheduler) -> int:
    """Register one stub-wire callback per §3.1 trigger type_id on `scheduler`.

    `scheduler` is an `engine.substrate.keys.TickScheduler` (duck-typed here: only
    `.subscribe(type_id, callback)` is used, so a test double satisfies the contract too).

    Returns the number of type_ids subscribed (13 — the full §3.1 roster; see the module-level
    G12 correction note for why none is held back on the cascade_cluster_event fork, the W3
    addition note for the combat-pair rows #11/#12, and W3 addition 2 for row #13
    (scene.accord_echo)).

    Idempotency note: `TickScheduler.subscribe` is purely additive (keys.py:447-448 appends to a
    list) — calling `subscribe_all` twice on the same scheduler registers duplicate callbacks
    (each firing, each incrementing the stub-wire counter once). Callers own calling this exactly
    once per scheduler lifetime; nothing here is idempotent by construction.
    """
    for type_id in _TRIGGER_TYPE_IDS:
        scheduler.subscribe(type_id, _make_trigger_callback(type_id))
    return len(_TRIGGER_TYPE_IDS)
