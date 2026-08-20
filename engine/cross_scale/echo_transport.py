"""
sim/cross_scale/echo_transport.py — deterministic echo-transport bridge (PR-2a, ED-IN-0028)

Un-orphans `domain_echo.py` and routes a resolved personal/scene outcome through the
executable Key substrate (`sim/substrate`) to a DEFERRED faction/territory stat write at
the accounting boundary. This is the "no more zoom_out({})" plumbing of the Key & Echo
Armature §6.2 (designs/architecture/key_echo_armature_v1.md), landed FLAG-GATED and
byte-exact by default.

Canon source: designs/architecture/scale_transitions_v30.md §5 (Domain Echo, degree-keyed
±2/±1/0/−1, Sufficient-Scope §7 gate) via sim/cross_scale/domain_echo.py; the substrate
contract is sim/substrate/keys.py (Key/KeyLog/TickScheduler, OF-7 deferred-apply).

SCOPE OF THIS SLICE (IN-lane; direction ruled, downstream deferred to owning lanes):
  - DETERMINISTIC transport only. `domain_echo` is degree-keyed and takes NO rng draw, so
    the §5.5 RNG-model-collision fork is NOT engaged here (no stochastic consumer lands).
  - The CONTEXT-DERIVATION bridge — deriving scene actors and which faction/stat is at
    stake from aggregate world-state — stays SC-lane work (ED-SC-0006/0007). This module
    fires an echo ONLY when the scene ctx already carries an explicit `echo` block
    (actor_faction / most_relevant_stat, optional target_faction / degree / scope_met).
    In the live campaign loop today every scene DEFERS (no parties are derived), so this
    path is INERT there — it is exercised by sim/tests/test_echo_transport.py, and the
    campaign's KeyLog is born empty-but-deterministic until the bridge lands.
  - parliamentary_vote-into-the-loop (the Hafenmark comeback path) is a BALANCE change
    owned by FA-lane ED-FA-0005 — NOT wired here.
  - OI-03 (ED-IN-0091 plan §3 Wave 2, 2026-07-29): `emit_scene_echo` now ALSO routes through
    §5.5 Accord Domain Echo (`domain_echo.compute_accord_echo`, previously zero callers) via
    `classify_scene_outcome` + `_apply_accord_echo` below. Same INERT-in-the-live-loop caveat
    as the §5.2 path above applies, PLUS a narrower one, TIGHTENED in the Wave-2 fix batch
    (OI-03 fix 1, 2026-07-29): classification now trusts ONLY an explicit caller-declared
    `echo['scene_outcome']` — the prior narrow `scene_type`-keyed fallback map (`'combat' ->
    'violence'`) is DELETED (see `classify_scene_outcome`'s docstring for why: a resolved combat
    scene is not the same claim as "a PC publicly initiated territorial-scale violence", and this
    boundary cannot verify the latter from `scene_type`/`degree` alone). No live producer in the
    campaign loop declares `scene_outcome` today (scene_dispatch.py's emergency_council/combat
    branches, parliamentary_bridge.py's vote ctx — none do, re-verified 2026-07-29), so this leg
    is WIRED (a real caller of `compute_accord_echo` exists) but DORMANT (organically
    unreachable) in any seeded campaign until a future SC/PC-lane bridge declares one.
  - W3 Handoff item 1 (ED-IN-0091 plan §3 Wave 3, 2026-07-29): `scene.accord_echo` is now
    registered in `key_type_registry_v30.md`, so `_apply_accord_echo`'s settlement-Order write
    routes through `sched.emit(key, apply=...)` (OF-7 deferred-apply) instead of applying
    inline — genuine queue-parity with the §5.2 leg above, closing OI-03 fix 4's contract
    collision with `zoom_in_out.zoom_out` rather than the prior wave's rename-around-it fix.
    Still DORMANT in any seeded campaign (no live producer declares `echo['scene_outcome']`),
    so no pinned golden moves.

Guardrails (holonic doctrine ED-1083 §2): implement the local rule only; declared I/O
only; never special-case an entity/outcome; never grow a scale-local dialect.
"""
from __future__ import annotations

from pathlib import Path
from typing import Optional

from engine.cross_scale import domain_echo
from engine.autoload.game_state import MULTS
from engine.substrate import EmittedAt, Key, KeyLog, Target, TickScheduler, TypeRegistry
# SEAM 1 OF 3 REMOVED 2026-08-20 (plan Act C3). This module used to import
# `systems.settlements.sim.registry` for ONE thing: STAT_MIN/STAT_MAX, the 0-5 clamp on settlement
# stats. That inverted the dependency direction — engine/ is the root and systems/ stems from it —
# to reach a bound `references/descriptor_registry.yaml` already declares as `set.order: 0-5`.
# It now reads the root. Value-identical by construction: registry.py:50 is `STAT_MIN, STAT_MAX =
# 0, 5` and the registry declares (0, 5), so the seeded campaign goldens are the control — if they
# move, this swap was wrong. They did not.
from engine.substrate import descriptors

_ORDER_FLOOR, _ORDER_CEILING = (descriptors.SETTLEMENT_STATS['set.order']['floor'],
                                descriptors.SETTLEMENT_STATS['set.order']['ceiling'])


# THE COOKED REGISTRY, not the markdown (ED-IN-0136). The markdown remains the AUTHORED surface —
# edit it, then re-run `tools/export_key_types.py` — but runtime reads typed data. Parsing prose at
# import time was defensible while the alternative was a hand-copied roster; it stopped being
# defensible once Godot (which re-implements the logic and cannot parse markdown) needed the same
# roster and got four HAND-MADE `.tres` files covering 4 of 55 types.
# The two sources are pinned identical by
# tests/valoria/test_key_substrate.py::test_json_and_markdown_registries_are_identical.
_REGISTRY_PATH = (Path(__file__).resolve().parents[2]
                  / "engine" / "engine_params" / "key_types.json")
_REGISTRY: Optional[TypeRegistry] = None


def _registry() -> TypeRegistry:
    """Load the canonical Key-type registry once and cache it.

    Reads the cooked JSON; `TypeRegistry.load` dispatches on suffix, so this is a path change and
    not a behaviour change — the parsed `types` dict is byte-for-byte the same mapping, in the same
    ORD-1 registry order.
    """
    global _REGISTRY
    if _REGISTRY is None:
        _REGISTRY = TypeRegistry.load(_REGISTRY_PATH)
    return _REGISTRY


# Operational scheduler caps — CALLER-SUPPLIED bounds, NOT canonical mechanical constants.
# OF-CAP is an open fork; §5.7 ruled ACCEPT-default 2026-07-07 (ED-IN-0026): the caller
# supplies caps, no fabricated canonical constant enters the repo. domain_echo emits exactly
# one non-cascading Key per resolved scene, so depth 0 suffices; the per-tick ceiling is a
# safety bound, caller-tunable via run_campaign params.
DEFAULT_CASCADE_DEPTH_MAX = 0  # [canonical: designs/architecture/key_echo_armature_v1.md §5.7 — OF-CAP caller cap, ED-IN-0026]
DEFAULT_EMISSIONS_PER_TICK_MAX = 64  # [canonical: designs/architecture/key_echo_armature_v1.md §5.7 — OF-CAP operational cap, ED-IN-0026]

# scene_type -> canonical scene.*_resolved Key type (registry §7). Only the two live
# personal-scale resolvers are mapped; adding a scale here without its resolver is
# shape-divergence (guardrail).
KEY_TYPE_BY_SCENE = {
    "contest": "scene.contest_resolved",
    "combat": "scene.combat_resolved",
}

# domain_echo degree -> the registry's documented `outcome` enum token, per scene family.
_OUTCOME_BY_DEGREE = {
    "contest": {"Overwhelming": "initiator_win", "Success": "initiator_win",
                "Partial": "compromise", "Failure": "target_win"},
    "combat": {"Overwhelming": "attacker_win", "Success": "attacker_win",
               "Partial": "draw", "Failure": "defender_win"},
}

# OI-03 (ED-IN-0091 plan §3 Wave 2) — §5.5 Accord Domain Echo outcome classification.
# The closed vocabulary scale_transitions_v30.md §5.5's table keys on
# ("PC Scene Outcome" -> "Accord Domain Echo").
_ACCORD_SCENE_OUTCOMES = frozenset(
    {"governance", "destabilisation", "territorial_transfer", "violence"})

# WAVE-2 CORRECTION (OI-03 fix 1, 2026-07-29, orchestrator-adjudicated): the prior
# `_ACCORD_OUTCOME_BY_SCENE_TYPE = {"combat": "violence"}` fallback is DELETED. Inferring the
# §5.5 Accord-Echo classification from `scene_type` alone conflates "a combat scene resolved"
# with the row's actual trigger, "PC action triggers violence AT TERRITORIAL SCALE (initiating
# battle, coup, uprising)" (scale_transitions_v30.md §5.5 row 4, line 219) -- a narrower, public/
# political claim this boundary cannot verify from `scene_type`/`degree` alone (no witness-count,
# no Exposure/public signal, no confirmation the violence was directed at territorial governance
# rather than e.g. a private duel). Guessing it from scene_type was itself a small fabrication of
# exactly the kind CLAUDE.md §5/§7 warns against, even though it was a single cited row. The leg
# stays WIRED (`compute_accord_echo` retains its one real caller, `emit_scene_echo` below) but
# DORMANT until a caller explicitly declares `echo['scene_outcome']` -- the SC/PC-lane context-
# derivation bridge's job (this module's SCOPE-OF-THIS-SLICE docstring note), never a
# scene_type-shaped guess. Adding a scene_type->outcome inference back here without a caller
# declaration is shape-divergence (ED-1083 guardrail) unless a future §5.5 row is unambiguous
# from scene_type/degree alone with no additional signal required -- not the case for any row
# today.


def classify_scene_outcome(scene_type: str, degree: str, echo: dict) -> Optional[str]:
    """§5.5 Accord Domain Echo outcome classification at the echo boundary (OI-03).

    Maps a resolved scene to scale_transitions_v30.md §5.5's Accord Domain Echo vocabulary
    ('governance' | 'destabilisation' | 'territorial_transfer' | 'violence') for
    `domain_echo.compute_accord_echo`. Derives ONLY from an explicit caller-declared
    `echo['scene_outcome']` -- never infers a PC-action category from `scene_type` alone (see the
    WAVE-2 CORRECTION comment above this function: a prior narrow scene_type fallback was deleted
    for exactly this reason). `scene_type` is still accepted for the declared I/O shape (mirrors
    `emit_scene_echo`'s own call site) but no longer participates in classification. `degree` is
    accepted (mirrors `compute_domain_echo`'s own `(degree, ...)` shape and is part of what's
    "already on hand" at this boundary) but does not currently discriminate any row here --
    §5.5's degree gating (Overwhelming/Success for governance, Success for destabilisation) is
    applied downstream by `compute_accord_echo` itself, not duplicated here.

    Precedence:
      1. `echo['scene_outcome']` -- an explicit caller-declared classification (the SC/PC-lane
         context-derivation bridge's job, per this module's SCOPE-OF-THIS-SLICE docstring
         note); validated against the closed §5.5 vocabulary before being trusted, never
         passed through blind.
      2. `None` -- unmappable (including "declared but not yet wired anywhere"); the caller
         records this and applies nothing, never guesses.

    DORMANCY (recorded, not silent): no live producer in the campaign loop sets
    `echo['scene_outcome']` today (scene_dispatch.py's emergency_council/combat branches,
    parliamentary_bridge.py's vote ctx — re-verified 2026-07-29, none do). This function is
    therefore exercised only by direct unit calls (engine/tests/test_accord_echo.py) and by
    engine/tests/test_pipeline_reach.py's caller-exists-AND-dormancy direction-2b probe, not by
    any seeded campaign.
    """
    del scene_type  # kept for the declared I/O shape (the call site's own scene_type) -- see docstring.
    del degree  # not discriminating today -- see docstring; kept for the declared I/O shape.
    echo = echo or {}
    declared = echo.get("scene_outcome")
    if declared in _ACCORD_SCENE_OUTCOMES:
        return declared
    return None


def make_scheduler(cascade_depth_max: int = DEFAULT_CASCADE_DEPTH_MAX,
                   emissions_per_tick_max: int = DEFAULT_EMISSIONS_PER_TICK_MAX) -> TickScheduler:
    """Create a fresh world-scoped KeyLog + TickScheduler for a campaign.

    defer_apply=True (OF-7) and no_sync_reentry=True (OF-B1) are the substrate's ratified
    defaults (§5.3/§5.4). Caps are caller-supplied (OF-CAP, §5.7) — never defaulted inside
    the substrate itself.
    """
    log = KeyLog(_registry())
    return TickScheduler(log,
                         cascade_depth_max=cascade_depth_max,
                         emissions_per_tick_max=emissions_per_tick_max)


def _derive_degree(scene_type: str, result) -> str:
    """Best-effort §5.2 degree from a resolver result dict. `ctx['echo']['degree']`
    overrides this (the SC bridge / a test supplies it); the fallback only needs to be
    total and deterministic. Combat-side derivation is provisional — the real mapping is
    SC/PC-lane bridge work."""
    if isinstance(result, dict):
        if scene_type == "contest":
            if result.get("total_victory"):
                return "Overwhelming"
            return "Success" if result.get("winner") else "Partial"
    return "Partial"


def _apply_accord_echo(scene_type: str, scene_outcome: str, ar, echo_ctx: dict, world, sched,
                       *, caused_by_key_id: Optional[str] = None) -> dict:
    """Apply an already-computed, already-`fires`-gated §5.5 AccordEchoResult -- the OI-03
    bottom-up settlement Accord WRITE (`engine/cross_scale/domain_echo.py`'s
    `compute_accord_echo`, previously zero callers).

    W3 QUEUE-PARITY (Handoff item 1, ED-IN-0091 plan §3 Wave 3, 2026-07-29 -- closes OI-03 fix 4
    FOR REAL instead of renaming around it): `scene.accord_echo` is now registered in
    `key_type_registry_v30.md` (this wave's Handoff item 1), so the settlement-Order write no
    longer applies inline -- it now builds a real `scene.accord_echo` Key and routes the write
    through `sched.emit(key, apply=...)`, the SAME OF-7 deferred-apply mechanism the sibling §5.2
    domain-echo leg (`emit_scene_echo`, below) already uses. The write lands at
    `accounting_boundary()`, not at scene-resolution time. This matches scale_transitions_v30.md's
    own §5.5 caption (:221, "Accord Domain Echoes fire at Accounting Step 4c") for ALL FOUR rows,
    including violence's -- only that row's RS component is canon-explicit-immediate (:219, "RS -1
    immediate. Accord -1 in that territory." -- the sentence break is deliberate: RS is immediate,
    Accord is not), so the RS write below is UNCHANGED, still a direct, immediate
    `rs_track.apply_rs_delta` call outside this Key.

    Return-shape note: the returned dict KEEPS the `'accord_applied'` key name (not renamed to
    e.g. `'accord_queued'`, even though the write it describes is now queued, not applied) --
    `engine/tests/test_pipeline_reach.py::test_direction6b_accord_echo_leg_receives_a_genuine_in_
    log_causal_id` reads `out.get("accord_applied")` directly, and that file is this wave's
    L-consumers lane's sole-editor scope (file-ownership map), not this stage's to edit. Renaming
    the dict key would silently break a currently-passing assertion in a file this stage may not
    touch -- a worse outcome than keeping a now-slightly-imprecise name with an honest docstring.
    What DOES change is the meaning of each row's `'applied'` boolean: `True` now means "a
    settlement resolved and a `scene.accord_echo` Key was built and queued for
    `accounting_boundary()`", not "already written to `Settlement.order`" -- documented here
    rather than silently reinterpreted. A new, additive `'key_id'` field carries the queued Key's
    id (nothing pre-existing can depend on a field that did not exist before).

    W3 THREADING, NOW GENUINELY POPULATED (OI-28 LIVE half, 2026-07-29 -- the W3
    consumers+causes lane built the `caused_by_key_id` plumbing; this same-wave follow-on closes
    the last step, now that this file and `test_pipeline_reach.py` are BOTH this stage's to edit):
    `caused_by_key_id` is the id of the §5.2 domain-echo Key `emit_scene_echo` (below) already
    appended to the log THIS SAME CALL, when it fired for the SAME scene resolution -- `None` when
    the §5.2 leg did not fire (no genuine upstream Key exists to cite; never fabricated). The new
    Key's `causes` field is now set to `[caused_by_key_id]` when that id is genuinely present,
    `[]` otherwise -- keys.py:325's invariant ("causes[] only references Keys already in the log")
    is satisfiable by construction here: `emit_scene_echo` appends the domain-echo Key via
    `sched.emit` BEFORE calling this function (verified ordering, unchanged), so the referenced id
    is always already in `sched.log` by the time this Key is built. This is the ONE genuine,
    non-decorative live `causes[]` instance corpus-wide (the diagonal Key-direction #6 the
    `test_pipeline_reach.py` acceptance oracle tracks) -- see that file's own manifest-row
    correction (dormancy still applies: no live producer declares `echo['scene_outcome']` yet, so
    this path fires zero times in any seeded campaign, but the code that WOULD populate it is now
    live, not merely threaded telemetry).

    WAVE-2 RETARGET (OI-03 fix 2, AUD-SET-02, 2026-07-29, unchanged this wave): this leg targets
    the SETTLEMENT where the scene occurred, never the province/Territory directly --
    scale_transitions_v30.md:215 ("Settlement targeting (AUD-SET-02): Accord changes from
    personal scenes target the settlement where the scene occurred, not the province directly.
    Province Accord recalculates at Accounting: floor(mean(settlement Order))."), matching
    peninsular_strain_v30.md §2.5 Category B's per-row table ("PC public governance" / "PC
    destabilisation" / "PC territorial violence" all -> "Settlement where scene occurred").
    Province Accord is a READ-ONLY aggregate of settlement Order
    (systems/settlements/sim/registry.py's `province_accord`, `floor(mean(order))`) -- this
    function never writes Territory.accord, and never recomputes the province aggregate itself
    (that stays registry.province_accord's job, called wherever a caller needs a province-level
    read, per CLAUDE.md §8 "every rule lives once"). See also this wave's Handoff item 2
    (`systems/overview/sim/accounting.py`'s new report-only province-Accord drift PROBE, which
    reads the same `registry.province_accord` without writing either value).

    Settlement targeting: `echo_ctx['target_settlement']` is an optional echo-block field
    (replaces the prior `target_territory`, which targeted the wrong scale per AUD-SET-02),
    added alongside the module's already-declared optional `target_faction`/`degree`/
    `scope_met` fields (this module's SCOPE-OF-THIS-SLICE docstring note). The SC/PC-lane
    context-derivation bridge is what will eventually name it; no live echo-block producer sets
    it today (re-verified 2026-07-29: neither `_emergency_council_parties`'s contest branch nor
    `combat_bridge`'s combat branch in scene_dispatch.py, nor parliamentary_bridge.py's vote
    ctx, populate it) -- so this stays a computed-but-unapplied, explicitly recorded outcome
    rather than a guessed settlement.

    Unit (OI-03 fix 3, ONE Accord unit, canonical-index space, never MULTS-scaled continuous):
    `Settlement.order` (systems/settlements/sim/registry.py) is the settlement's OWN native 0-5
    canonical-index scale -- settlement_layer_v30.md §1.3: "Order | Local institutional
    stability and compliance | Analogous to province Accord but at settlement scale." §5.5's
    table is ALREADY expressed in that same index space (+-1 per row; "Transferred territory
    Accord set to 2"), and `domain_echo.compute_accord_echo`'s `accord_delta` is ALREADY that
    same canonical-index +-1/0 (never MULTS-scaled) -- so it is applied to `settlement.order`
    directly, with no MULTS/ACCORD_MAP conversion anywhere in this function. MULTS['accord'] /
    ACCORD_MAP are Territory.accord's OWN continuous 0.5-7.0 representation (game_state.py) --
    a DIFFERENT field this leg no longer touches; mixing the two scales in one function is
    exactly the "MULTS-scaled continuous value in the same function as a canonical-index step"
    defect this fix removes. Clamped to the registry-declared `set.order` bounds (0-5), the
    same bound `Settlement.order` observes everywhere else (registry.py, settlement.py). The
    deferred `_apply` closure below re-resolves the settlement from `world.settlements` by id at
    apply time (mirrors `emit_scene_echo`'s own `_apply` closure for the §5.2 leg, which
    re-resolves the faction by id rather than closing over a captured object reference).
    """
    sid = echo_ctx.get("target_settlement")
    settlements = getattr(world, "settlements", None) or {}
    settlement = settlements.get(sid) if sid else None
    detail = {"scene_outcome": scene_outcome, "target_settlement": sid,
              "accord_delta": ar.accord_delta, "rs_delta": ar.rs_delta,
              "notes": list(ar.notes),
              "caused_by_key_id": caused_by_key_id}  # W3 OI-28 threading, see docstring above.
    if settlement is None:
        detail["applied"] = False
        detail["reason"] = ("no resolvable target_settlement in echo block; §5.5 Accord Echo "
                             "computed, not applied")
        return {"accord_applied": [detail]}

    # W3 Handoff item 1: build the scene.accord_echo Key and queue the settlement-Order write via
    # OF-7 (accounting_boundary()) -- see the docstring's "W3 QUEUE-PARITY" section above.
    seq = getattr(world, "_echo_key_seq", 0)
    world._echo_key_seq = seq + 1
    season = int(getattr(world, "season", 0))
    key = Key(
        id=f"scene.accord_echo.s{season}.n{seq}",
        type="scene.accord_echo",
        emitted_at=EmittedAt(season_index=season),
        # causes[] population (OI-28 LIVE, W3): [caused_by_key_id] when the sibling §5.2 leg fired
        # for this SAME scene (genuinely already in-log by construction -- see the docstring's "W3
        # THREADING" section), [] when it did not (no genuine upstream Key exists to cite --
        # never fabricated, per the honesty test in engine/tests/test_accord_echo.py).
        causes=[caused_by_key_id] if caused_by_key_id else [],
        scale_signature=["settlement"],
        targets=[Target(actor_id=sid, role="subject",
                        stat_deltas=({"order": ar.accord_delta} if ar.accord_delta else {}))],
        payload={"scene_outcome": scene_outcome, "target_settlement": sid,
                 "accord_delta": ar.accord_delta},
    )

    def _apply(_k, _world=world, _sid=sid, _outcome=scene_outcome, _delta=ar.accord_delta):
        settlements_now = getattr(_world, "settlements", None) or {}
        s = settlements_now.get(_sid)
        if s is None:
            return
        if _outcome == "territorial_transfer":
            # [canonical: §5.5 -- "Transferred territory Accord set to 2"] -- 2 is already the
            # canonical-index value (see docstring's Unit note); clamped through the same
            # registry-declared bound as every other settlement.order write, not
            # through ACCORD_MAP (Territory.accord's continuous scale -- untouched here).
            s.order = max(_ORDER_FLOOR, min(_ORDER_CEILING, 2))
        elif _delta:
            # _delta is ALREADY canonical-index (+-1, §5.5's own table) -- settlement.order is
            # natively that same index scale (settlement_layer_v30.md §1.3), so it is added
            # directly, with no MULTS conversion (see docstring's Unit note).
            s.order = max(_ORDER_FLOOR,
                          min(_ORDER_CEILING, s.order + _delta))

    sched.emit(key, apply=_apply)  # OF-7: settlement-Order write lands at accounting_boundary()
    detail["applied"] = True
    detail["key_id"] = key.id

    if ar.rs_delta:
        # RS ("Mending Stability") has no live write path yet — systems.overview.sim.rs_track
        # is a Pass 2l armature stub (OI-17). Route through its own declared entry point (the
        # single-owner call site, CLAUDE.md §8) rather than reaching into World directly; it
        # self-flags as a typed no-op via stubwire until RS is built. Stays IMMEDIATE per canon
        # (:219) -- see the docstring's "W3 QUEUE-PARITY" section for why this is unaffected by
        # the settlement-Order queueing above.
        from systems.overview.sim import rs_track
        rs_track.apply_rs_delta(ar.rs_delta, source=f"accord_echo:{scene_type}", world=world)

    return {"accord_applied": [detail]}


def emit_scene_echo(scene_type: str, result, ctx: dict, world) -> dict:
    """Route one resolved scene through domain_echo → substrate Key (deferred faction apply),
    and (OI-03) through §5.5 Accord Domain Echo (`compute_accord_echo`).

    Fires ONLY when `world.echo_scheduler` is attached AND `ctx` carries an explicit `echo`
    block. Returns a `scene_outcomes` dict for zoom_out — `{}` when nothing fires, which is
    the byte-exact fallback (identical to the historical `zoom_out({})`). Both legs now defer to
    the accounting boundary via OF-7 (`sched.emit(key, apply=...)`): the §5.2 Domain Echo
    substrate `apply` (unchanged), and — as of W3 Handoff item 1, 2026-07-29 — the §5.5 Accord
    Echo settlement-Order write, returned under the `'accord_applied'` key (see
    `_apply_accord_echo`'s "W3 QUEUE-PARITY" docstring section for why that key name is KEPT
    despite the write no longer being immediate). The RS component of the Accord Echo leg (§5.5
    violence row only) stays a direct, immediate `rs_track.apply_rs_delta` call — canon (:219)
    makes RS immediate and Accord queued, a genuine asymmetry, not an inconsistency. There is no
    double-apply between the two legs — they write disjoint state (Faction stat vs. Settlement
    Order/RS). The Accord Echo leg is additionally gated on an explicit caller-declared
    `echo['scene_outcome']` (WAVE-2, OI-03 fix 1 — see `classify_scene_outcome`'s docstring); no
    live producer sets that key today, so this leg is wired but organically dormant.
    """
    sched = getattr(world, "echo_scheduler", None)
    echo_ctx = ctx.get("echo")
    key_type = KEY_TYPE_BY_SCENE.get(scene_type)
    if sched is None or not echo_ctx or key_type is None:
        return {}
    actor_faction = echo_ctx.get("actor_faction")
    stat = echo_ctx.get("most_relevant_stat")
    if actor_faction is None or stat is None:
        return {}

    degree = echo_ctx.get("degree") or _derive_degree(scene_type, result)
    scope_met = bool(echo_ctx.get("scope_met", True))
    source_scene = {
        "actor_faction": actor_faction,
        "target_faction": echo_ctx.get("target_faction", actor_faction),
        "most_relevant_stat": stat,
    }
    out = {}

    # W3 (OI-28 LIVE half): captures the §5.2 domain-echo Key's id, when one fires, so the §5.5
    # Accord leg below can cite it as `caused_by_key_id` -- the SAME scene resolution's two
    # consequences, genuinely ordered (this Key is appended to the log via sched.emit() several
    # lines below, BEFORE the Accord leg runs). CORRECTED (item 7, small/LOW, re-critic pass):
    # this now IS a genuinely populated Key `causes[]` field, not merely telemetry -- see
    # `_apply_accord_echo` at :306 (`causes=[caused_by_key_id] if caused_by_key_id else []`), the
    # one executable, non-decorative `causes[]` instance corpus-wide (still organically DORMANT in
    # any real campaign, since the Accord leg itself never fires without a caller-declared
    # `scene_outcome` -- see the leg's own docstring for that separate reachability fact).
    _domain_echo_key_id = None

    er = domain_echo.compute_domain_echo(degree, scope_met, source_scene, world)
    if er.fires and er.affected_faction is not None and er.affected_stat is not None and er.delta != 0:
        seq = getattr(world, "_echo_key_seq", 0)
        world._echo_key_seq = seq + 1
        season = int(getattr(world, "season", 0))
        participants = [str(getattr(p, "actor_id", i))
                        for i, p in enumerate(ctx.get("parties") or ctx.get("participants") or [])]
        key = Key(
            id=f"scene.{scene_type}.s{season}.n{seq}",
            type=key_type,
            emitted_at=EmittedAt(season_index=season),
            scale_signature=["personal"],  # registry default for scene.*_resolved; enriched in the PR-3 keying wave
            targets=[Target(actor_id=er.affected_faction, role="subject",
                            stat_deltas={er.affected_stat: er.delta})],
            payload={
                "scene_id": echo_ctx.get("scene_id", f"{scene_type}_{seq}"),
                "outcome": _OUTCOME_BY_DEGREE[scene_type].get(degree, "compromise"),
                "participants": participants,
            },
        )

        def _apply(_k, faction=er.affected_faction, _stat=er.affected_stat, _delta=er.delta):
            # domain_echo.delta is in STAT POINTS (§5.2 ±2 Mandate); Faction.adjust expects a
            # GRANULAR delta (points × MULTS) — mirror the §10 Mandate-penalty convention
            # (parliamentary_vote: adjust("L", -1 * MULTS["L"])), so ±N points lands as ±N.
            f = getattr(world, "factions", {}).get(faction)
            if f is not None and hasattr(f, "adjust") and _stat in MULTS:
                f.adjust(_stat, _delta * MULTS[_stat])

        sched.emit(key, apply=_apply)  # OF-7: Key logs LIVE now; _apply lands at accounting_boundary()
        _domain_echo_key_id = key.id  # W3: now genuinely in-log (keys.py:325) — safe to cite below.
        out["other_echoes"] = [{"faction": er.affected_faction,
                                "stat": er.affected_stat, "delta": er.delta}]

    # OI-03: §5.5 Accord Domain Echo — gated on the SAME Sufficient Scope check (§7) as the
    # §5.2 Domain Echo above (scale_transitions_v30.md:55: "Scene events meeting Sufficient
    # Scope (§7) produce Domain Echo per §5 ... See §5.5 ... for the full Echo
    # specifications" — §5.5 IS one of the "per §5" mechanisms that sentence covers).
    if scope_met:
        scene_outcome = classify_scene_outcome(scene_type, degree, echo_ctx)
        if scene_outcome is not None:
            ar = domain_echo.compute_accord_echo(scene_outcome, degree, world)
            if ar.fires:
                out.update(_apply_accord_echo(scene_type, scene_outcome, ar, echo_ctx, world,
                                              sched, caused_by_key_id=_domain_echo_key_id))

    return out
