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
    PARTIAL CLOSURE (ED-SC-0006, 2026-07-08): the one live trigger, Stability
    Crisis's "emergency council" contest, now derives its two sides from the
    SAME faction's own cited aggregate stats via _emergency_council_parties —
    see that function's docstring for the citation + the [SEED] flag on the
    specific mapping. combat, and any future contest trigger that is not
    emergency_council, still defer (no bridge exists for those actor shapes).
  - OUTCOME->ECHO MAPPING GAP: resolved-scene outcomes are passed to zoom_out,
    but the resolver-result -> accord/faction-stat echo mapping is
    resolver/canon-specific and is left empty (flagged) rather than fabricated.
    Consequence (intended): the scene phase is SIDE-EFFECT-FREE on strategic
    state, so wiring it in cannot regress the strategic loop.
    PARTIAL CLOSURE (ED-SC-0007, 2026-07-08, per the ED-SC-0002 composed-keying
    ruling): the emergency_council contest now sets a `ctx['echo']` block
    (Mandate channel, degree-keyed off the ballot verdict) so echo_transport
    (ED-IN-0028) can fire when ECHO_TRANSPORT is on. Still side-effect-free by
    DEFAULT (the flag stays off); still empty for combat and any other contest
    stakes kind. The Projection-genre bonus-token channel remains unmapped —
    see the inline note at the emergency_council echo block.
  - Only field-evaluable canonical triggers fire (Stability Crisis via
    Faction.Sta). The other 7 §4.3.2 triggers need world-state schema not
    present on the aggregate World; they are reported as deferred, not faked.
"""
from __future__ import annotations

import random

from engine.autoload import scene_slate
from engine.cross_scale import zoom_in_out


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
                    # parties intentionally absent here: derived at RESOLVE time (freshest
                    # world state), not queue time — see _emergency_council_parties.
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


# Emergency Council → proceeding mapping (ED-SC-0006 party-derivation bridge).
# scale_transitions_v30.md:137 names the scene "Emergency faction council" but assigns it no
# proceeding. Of the 8 canonical social_contest_v30 proceedings (contest.modes.PROCEEDINGS),
# Guild Arbitration is the closest structural match: its Panel adjudicator is "Masters arbitrate"
# (ED-1059) — a seated bench deliberating together, which mirrors a faction council convening to
# judge its own crisis better than a single expert/crowd judge does. [SEED — a provisional
# proceeding choice, open to Jordan revision; the mechanical routing this module does is
# proceeding-agnostic].
EMERGENCY_COUNCIL_PROCEEDING = "guild_arbitration"


def _emergency_council_parties(fid, world):
    """Derive the two internal sides of a faction's Emergency Council — fired by the Stability
    Crisis trigger (scale_transitions_v30.md:137: "Emergency faction council: social contest ...
    revealing the source of the crisis"). No player-character schema exists at this (aggregate,
    Monte-Carlo) scale — CLAUDE.md §5's no-fabrication rule and this module's own DELIBERATE
    BOUNDARIES note both forbid inventing a personal actor. Both sides are therefore derived
    from the SAME faction's own already-cited aggregate stats, not a new invented attribute:
      side_a = the sitting leadership's case to stay the course — faculty = round(Faction.L),
               its institutional legitimacy/authority to persuade.
      side_b = the crisis's own case for change — faculty = round(7 - Faction.Sta): the worse
               the Stability, the stronger the case.
    Both floor at 1 (build_contest's kernel Pool.size floors the rolled pool at 5 regardless of
    faculty — ED-SC-0004, a separate open fork over the pool formula itself).
    [SEED — a provisional derivation, ED-SC-0006; a design default open to Jordan revision, not
    itself a P0 fork]. Returns None if `fid` does not name a live faction."""
    f = getattr(world, "factions", {}).get(fid)
    if f is None:
        return None
    return (max(1, round(f.L)), max(1, round(7.0 - f.Sta)))


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
            stakes = ctx.get("stakes") or {}
            if (not parts or len(parts) < 2) and stakes.get("kind") == "emergency_council":
                parts = _emergency_council_parties(ctx.get("faction"), world)
            if not parts or len(parts) < 2:
                out["reason"] = "context-derivation gap: no personal contest parties from aggregate faction state"
                return out
            # ED-SC-0006: route to the PROMOTED kernel (build_contest/resolve_contest), retiring
            # the deprecated contest_legacy_stub.run_contest call this branch used to make.
            import systems.social_contest.sim.contest as contest
            proceeding = ctx.get("proceeding", EMERGENCY_COUNCIL_PROCEEDING)
            # The promoted kernel resolves off the GLOBAL `random` module, not an injectable rng
            # (resolver.py's own note: the 151 seeded kernel tests rely on the module-level
            # stream). Reseed it from a value DERIVED from world.rng — NOT a fixed pin, which
            # massbattle.py:1826-1830 already learned breaks batch reproducibility — so the same
            # campaign seed still yields the same contest outcome, then restore the prior global
            # state so nothing else observes the reseed.
            prev_random_state = random.getstate()
            try:
                random.seed(rng.getrandbits(32))
                built = contest.build_contest(parts[0], parts[1], venue=proceeding)
                (verdict, verdict_reason), _bout = contest.resolve_contest(built)
            finally:
                random.setstate(prev_random_state)
            out["resolved"] = True
            # 'verdict'/'verdict_reason' are the promoted kernel's own shape (a win-condition band
            # or side label, plus 'win'|'draw'|'clinch:...') — NOT the deprecated stub's
            # ContestResult(winner='A'|'B'|None, total_victory=bool) shape.
            out["result"] = {"winner": verdict, "reason": verdict_reason, "proceeding": proceeding,
                             "side_a_faculty": parts[0], "side_b_faculty": parts[1]}
            # ED-SC-0007 (Bout outcome -> domain_echo), per the ED-SC-0002 RULING (2026-07-08,
            # composed keying: band gates magnitude/whether an echo fires; genre selects the
            # stat/channel — social_contest_v30 §6 + scale_transitions_v30 §5.4).
            #   Genre channel: resolve_contest's default policies (logos_spammer for both sides,
            #   unchanged by this bridge) only ever move with Appeal.LOGOS, which
            #   dictionaries._APPEAL_TO_GENRE keys to Genre.MEMORY — so, as currently wired, every
            #   Emergency Council verdict is deterministically Memory-genre, i.e. the Mandate
            #   channel ("Decisive win + Memory genre: winning faction's Mandate +1", §6). The
            #   Projection channel (+1D on the first Domain Action) has NO representation in
            #   domain_echo's stat-delta interface — it is a bonus-token mechanism, not a stat
            #   write, and is NOT fabricated here; it stays an explicit residual (would need a new
            #   Key type + a consumption site in faction_action.py, not authored by this change).
            #   If a future policy ever moves on PATHOS/ETHOS this Memory-only assumption breaks
            #   and must be revisited.
            #   Band/magnitude: Guild Arbitration resolves via VoteAtClose (a ballot), not a
            #   Persuasion-Track value, so there is no Overwhelming/Decisive magnitude gradient to
            #   key off (§5.4's own table is itself only binary: decisive win/loss, no tiering).
            #   The honest instantiation of "band gates magnitude" for a ballot verdict is the
            #   degenerate binary case: side_a (leadership) wins -> Success (+1); side_b (the
            #   crisis) wins -> Failure (-1, applied to the acting faction's own stat per §5.2,
            #   which is the same faction here); a draw -> Partial (no echo — "Compromise: no
            #   Domain Echo" per both source docs). Both sides of this contest are the SAME
            #   faction's own facets (_emergency_council_parties), so actor_faction==target_faction.
            # Scoped to emergency_council specifically (matching the party-derivation scoping
            # above) — a future contest stakes kind with a different actor/genre shape needs its
            # own mapping, not a silent fallthrough onto this one.
            if stakes.get("kind") == "emergency_council":
                if verdict == contest.A:
                    echo_degree = "Success"
                elif verdict == contest.B:
                    echo_degree = "Failure"
                else:
                    echo_degree = "Partial"
                fid = ctx.get("faction")
                ctx["echo"] = {"actor_faction": fid, "target_faction": fid,
                              "most_relevant_stat": "L", "degree": echo_degree}
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
        from engine.cross_scale import echo_transport
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
