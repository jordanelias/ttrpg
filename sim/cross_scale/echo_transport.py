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

Guardrails (holonic doctrine ED-1083 §2): implement the local rule only; declared I/O
only; never special-case an entity/outcome; never grow a scale-local dialect.
"""
from __future__ import annotations

from pathlib import Path
from typing import Optional

from sim.cross_scale import domain_echo
from sim.autoload.game_state import MULTS
from sim.substrate import EmittedAt, Key, KeyLog, Target, TickScheduler, TypeRegistry


_REGISTRY_PATH = (Path(__file__).resolve().parents[2]
                  / "designs" / "architecture" / "key_type_registry_v30.md")
_REGISTRY: Optional[TypeRegistry] = None


def _registry() -> TypeRegistry:
    """Load the canonical Key-type registry once and cache it (the registry markdown
    stays the single source of truth — the substrate parses it, never a copy)."""
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


def emit_scene_echo(scene_type: str, result, ctx: dict, world) -> dict:
    """Route one resolved scene through domain_echo → substrate Key (deferred faction apply).

    Fires ONLY when `world.echo_scheduler` is attached AND `ctx` carries an explicit `echo`
    block. Returns a `scene_outcomes` dict for zoom_out — `{}` when nothing fires, which is
    the byte-exact fallback (identical to the historical `zoom_out({})`). The substrate's
    deferred `apply` is the real state mutation (at the accounting boundary); zoom_out's
    queue stays report-only, so there is no double-apply.
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
    er = domain_echo.compute_domain_echo(degree, scope_met, source_scene, world)
    if not er.fires or er.affected_faction is None or er.affected_stat is None or er.delta == 0:
        return {}

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
    return {"other_echoes": [{"faction": er.affected_faction,
                              "stat": er.affected_stat, "delta": er.delta}]}
