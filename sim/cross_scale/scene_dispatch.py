"""
sim/cross_scale/scene_dispatch.py — Consumer-side scale-seam glue (NEW 2026-06-06)

Wires the previously-disconnected scale-transition seam. The mechanism pieces
already existed (scene_slate queue, zoom_in/zoom_out protocol §4, live
combat/contest resolvers) but nothing connected them into the season loop.
This module is that glue:

    evaluate_triggers  -> queue_triggered_scenes  (scene_slate)
                       -> dispatch_scenes         (zoom_in -> resolver -> zoom_out)
    run_scene_phase    = the season-callback-composable phase

Canon source: designs/architecture/scale_transitions_v30.md §4
              (Zoom In/Out protocol; §4.3.2 mandatory triggers).

Status: [PROVISIONAL — seam-mechanism wiring 2026-06-06].

DELIBERATE BOUNDARIES (not fabricated):
  - CONTEXT-DERIVATION BRIDGE GAP: the strategic World holds AGGREGATE faction
    stats (L/Sta/W/I/Mil), not personal-scale actors. combat/contest resolvers
    need concrete duck-typed actors. Deriving scene actors from aggregate state
    is an undefined design decision; this module does NOT invent actors. When a
    queued scene lacks resolvable actors in its context, dispatch records a
    flagged deferral (reason='context-derivation gap') and resolves nothing.
  - OUTCOME->ECHO MAPPING GAP: resolved-scene outcomes are passed to zoom_out,
    but the resolver-result -> accord/faction-stat echo mapping is
    resolver/canon-specific and is left empty (flagged) rather than fabricated.
    Consequence (intended): the scene phase is SIDE-EFFECT-FREE on strategic
    state, so wiring it in cannot regress the strategic loop.
  - Only field-evaluable canonical triggers fire (Stability Crisis via
    Faction.Sta). The other 7 §4.3.2 triggers need world-state schema not
    present on the aggregate World; they are reported as deferred, not faked.
"""
from __future__ import annotations

import random

from sim.autoload import scene_slate
from sim.cross_scale import zoom_in_out


# ─────────────────────────────────────────────────────────────────────────
# Trigger evaluation — only canonical §4.3.2 triggers whose world-state fields
# actually exist on the aggregate World are fired. The rest are reported.
# ─────────────────────────────────────────────────────────────────────────
def evaluate_triggers(world):
    """Return (fired, deferred). `fired` = list of scene specs; `deferred` =
    list of canonical trigger names whose conditions are not evaluable against
    the current aggregate world schema (flagged, not faked)."""
    fired = []
    # Stability Crisis (§4.3.2): Faction.Sta <= 2 -> emergency council (contest)
    for fid, f in getattr(world, "factions", {}).items():
        sta = getattr(f, "Sta", None)
        if sta is not None and sta <= 2:
            fired.append({
                "trigger": "Stability Crisis",
                "scene_type": "contest",
                "priority": zoom_in_out.MANDATORY_TRIGGER_PRIORITY,
                "context": {
                    "origin": "world_state",
                    "faction": fid,
                    "stakes": {"kind": "emergency_council", "faction": fid},
                    # parties intentionally absent: derivation bridge gap (flagged)
                },
            })
    evaluable = {"Stability Crisis"}
    deferred = [t.trigger_name for t in zoom_in_out.check_mandatory_triggers(world)
                if t.trigger_name not in evaluable]
    return fired, deferred


def queue_triggered_scenes(world):
    fired, deferred = evaluate_triggers(world)
    for ev in fired:
        scene_slate.queue_scene(ev["scene_type"], ev["context"], ev["priority"])
    return {"queued": len(fired), "deferred_triggers": deferred}


# ─────────────────────────────────────────────────────────────────────────
# Dispatch — drain scene_slate, transition (zoom_in), route to live resolver,
# feed back (zoom_out). Defers (flagged) when actors can't be derived.
# ─────────────────────────────────────────────────────────────────────────
def _resolve_slot(slot, world, rng):
    st = slot.scene_type
    ctx = slot.context or {}
    zi = zoom_in_out.zoom_in(ctx.get("from_phase", "after_phase_6_step_1"),
                             ctx.get("board_degree"), world)
    out = {"scene_type": st, "resolved": False, "reason": None,
           "scene_ob_modifier": zi.scene_ob_modifier}
    try:
        if st == "combat":
            parts = ctx.get("participants")
            if not parts or len(parts) < 2:
                out["reason"] = "context-derivation gap: no personal combat actors in aggregate world-state"
                return out
            import sim.personal.combat as combat
            rr = combat.resolve_combat_round(parts, scene=ctx.get("scene"), rng=rng)
            out["resolved"] = True
            out["result"] = getattr(rr, "__dict__", str(rr))
        elif st == "contest":
            parts = ctx.get("parties")
            if not parts or len(parts) < 2:
                out["reason"] = "context-derivation gap: no personal contest parties from aggregate faction state"
                return out
            import sim.personal.contest as contest
            cr = contest.run_contest(parts, ctx.get("stakes", {}), world=world, rng=rng)
            out["resolved"] = True
            out["result"] = getattr(cr, "__dict__", str(cr))
        else:
            out["reason"] = f"resolver for scene_type={st!r} not live (stub or unmapped)"
            return out
    except Exception as e:
        out["reason"] = f"resolver raised: {e!r}"
        return out
    # Outcome->echo transport (ED-IN-0028, flag-gated by world.echo_scheduler presence).
    # With NO scheduler attached (ECHO_TRANSPORT off) this is byte-identical to the historical
    # zoom_out({}) no-echo path. With one attached AND ctx carrying an `echo` block, the
    # resolved outcome routes through domain_echo -> substrate Key (deferred faction apply).
    if getattr(world, "echo_scheduler", None) is not None:
        from sim.cross_scale import echo_transport
        scene_outcomes = echo_transport.emit_scene_echo(st, out["result"], ctx, world)
        out["echo_fired"] = bool(scene_outcomes.get("other_echoes"))
    else:
        scene_outcomes = {}
    zo = zoom_in_out.zoom_out(scene_outcomes, world)
    out["domain_echoes"] = zo.domain_echoes_queued
    return out


def dispatch_scenes(world, rng):
    report = {"dispatched": 0, "resolved": 0, "deferred": []}
    while scene_slate.pending_count() > 0:
        slot = scene_slate.next_scene()
        if slot is None:
            break
        res = _resolve_slot(slot, world, rng)
        report["dispatched"] += 1
        if res.get("resolved"):
            report["resolved"] += 1
        else:
            report["deferred"].append((res["scene_type"], res.get("reason")))
    return report


def run_scene_phase(world, rng=None):
    """Season-callback-composable scene phase. Side-effect-free on strategic
    stats by construction (see module GAP notes)."""
    rng = rng or getattr(world, "rng", None) or random.Random()
    q = queue_triggered_scenes(world)
    d = dispatch_scenes(world, rng)
    return {"queue": q, "dispatch": d}
