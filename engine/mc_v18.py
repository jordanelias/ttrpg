"""
sim/mc_v18.py — Top-level strategic simulator runner — orchestrator only

Canon source: canon/02_canon_constraints.md §B (GD-1, GD-2, GD-3);
              designs/architecture/campaign_architecture_v30.md (campaign flow).
Game Design constraints applicable: GD-1, GD-2, GD-3
Status: [CANONICAL — Phase 2 implementation 2026-05-17;
                    Deferred Migration Batch 2026-05-20]

Replaces tests/sim/v17-integration/mc_v17.py (39k monolith).
Phase 2: faction actions (conquest/muster/govern) + accounting wired in.

[2026-05-20 — Deferred Migration Batch: inline season block deleted.
 Composition (advance_season → faction actions → accounting) now routes
 through sim.peninsular.season.run_season with action_callback.
 Pure refactor — ordering identical to v17/Phase-2 inline path.]

Dependencies:
  - sim/autoload/* (all autoload services)
  - sim/peninsular/season (season composition)
  - systems/factions/sim/faction_action

Entry points:
  - run_campaign(seed, max_seasons, params) -> CampaignResult
  - run_batch(n, base_seed, params) -> BatchResult
"""
from __future__ import annotations

import os
import sys
import time
from collections import Counter
from dataclasses import dataclass, field

from engine.autoload import game_state, victory, scene_slate
from engine.substrate import stubwire
from systems.factions.sim.faction_action import faction_take_action
from systems.overview.sim.season import run_season
from engine.cross_scale import scene_dispatch


DEFAULT_PARAMS = {
    'CAMPAIGN_SEASONS': 50,
    # VICTORY_THRESHOLD: 11 is a DEAD param copy — the live gate is
    # engine/autoload/victory.py's own VICTORY_THRESHOLD = 15 (Jordan 2026-06-19, J-22), which
    # this dict does not feed. It is deliberately kept, not deleted: it is the exact subject of
    # the F7 tripwire, engine/tests/test_f7_smoke_oracle.py::test_f7_victory_threshold_is_a_dead_param
    # (C-EMERGE-8 / C-FA-9), which asserts sweeping this value (11 -> 999 -> 1) moves NO outcome
    # — i.e. that it is still unwired. Deleting this entry does not fix anything; it silently
    # kills the tripwire's ability to trip if the param is ever accidentally wired live.
    # Verified 2026-07-29 (Wave 4 mechanical sweep, OI-32a): still unread anywhere in
    # engine/cross_scale/, systems/overview/sim/season.py, or engine/autoload/victory.py.
    'VICTORY_THRESHOLD': 11,
}


def _echo_transport_on(effective_params: dict) -> bool:
    """ECHO_TRANSPORT flag (ED-IN-0028 / ED-SC-0006/0007) — **default ON** (Jordan ratification
    2026-07-08: "Yes echo transport on"). The consequence spine (per-season §10 Parliamentary vote
    + composed Domain Echo, sim/cross_scale/parliamentary_bridge.py) is now the baseline campaign.
    A `params['ECHO_TRANSPORT']` override wins; otherwise the env var (default '1'). Set
    ECHO_TRANSPORT=0 (or params={'ECHO_TRANSPORT': 0}) for the pre-spine byte-exact regression
    oracle, still pinned OFF in test_echo_transport.py (the MB FIELD_MOVEMENT/ED-1089 pattern:
    default flipped, the old path retained as the frozen oracle)."""
    if 'ECHO_TRANSPORT' in effective_params:
        return bool(effective_params['ECHO_TRANSPORT'])
    return os.environ.get('ECHO_TRANSPORT', '1') == '1'


def _dispatch_combat_bridge_on(effective_params: dict) -> bool:
    """DISPATCH_COMBAT_BRIDGE flag (ED-IN-0091, plan §2.2, OI-01) — **default OFF**, mirroring
    `_echo_transport_on`'s params-override-then-env-var resolution (ED-IN-0028) as the plan's §2.2
    "find the existing flag pattern... and mirror it; single owner" instruction directs. With the
    flag off `world.dispatch_combat_bridge` is False and scene_dispatch's combat branch takes the
    UNCHANGED historical path (the deprecated `systems.combat.sim.combat.resolve_combat_round`
    call stays in place — byte-identical to pre-bridge behaviour, per the plan's "ship-flag-off"
    term). The flip to ON is a deliberate, separately-scheduled IN action after PC's E0-E3 batches
    merge (plan §0/§2.2), never a side effect of this wave."""
    if 'DISPATCH_COMBAT_BRIDGE' in effective_params:
        return bool(effective_params['DISPATCH_COMBAT_BRIDGE'])
    return os.environ.get('DISPATCH_COMBAT_BRIDGE', '0') == '1'


@dataclass
class CampaignResult:
    winner: str | None
    season: int
    surviving: int
    battle_count: int
    scenes_resolved: int = 0        # F7 telemetry (ED-IN-0021): personal-scale scenes actually resolved
    insurgencies_formed: int = 0    # F7 telemetry: len(world.insurgencies)
    npcs_generated: int = 0         # F7 telemetry: world.npc_counter (generate_npc call-count proxy)
    stub_hits: int = 0              # F7-pattern telemetry (ED-IN-0091, plan §2.1): per-campaign delta of
                                     # engine.substrate.stubwire.invocations — 0 while no live call site is
                                     # stub-wired yet (Wave 1 stage 4 converts the OI-17 class); additive-only,
                                     # never a fabricated value (§0.1 / §7 no-fabrication).
    accord_drift_probe_hits: int = 0  # W3 Handoff item 2 telemetry (ED-IN-0091 plan §3 Wave 3):
                                     # systems.overview.sim.accounting's REPORT-ONLY province-Accord
                                     # drift probe — count of (season, province) divergences between
                                     # registry.province_accord and Territory.accord this campaign.
                                     # 0 when nothing diverges; never writes either compared value
                                     # (OI-37/SE routes the actual write-model reconciliation).
    key_log_hash: str = ""          # ED-IN-0028: sha256 of the campaign's canonical KeyLog ("" when ECHO_TRANSPORT off)
    keys_emitted: int = 0           # ED-IN-0028: len(world.key_log) — 0 while scenes defer (SC bridge pending)
    final_state: dict = field(default_factory=dict)


@dataclass
class BatchResult:
    n: int
    win_share: dict[str, float] = field(default_factory=dict)
    all_winners: dict[str, int] = field(default_factory=dict)
    battles_mean: float = 0.0


def _faction_actions_callback(world):
    """Per-season faction action dispatch — passed to season.run_season.

    GD-2 mandatory-actions precedence is enforced inside faction_take_action
    (mandatory pass before stochastic candidates per HR-9). Parliamentary +
    territory-holding gate matches the pre-migration inline block at
    mc_v18 L75-87 prior to 2026-05-20.
    """
    for fn, faction in world.factions.items():
        if not faction.parliamentary:
            continue
        if not faction.territories:
            continue
        try:
            faction_take_action(faction, world, world.rng)
        except Exception as e:
            # Resilience: one faction's action error must not abort the whole season — but
            # it must NOT be swallowed SILENTLY either (audit ED-IN-0074 D7). Surface it to
            # stderr so batch runs reveal errors instead of hiding a degenerate campaign.
            print(f"[mc_v18] faction_take_action error for {fn!r}: "
                  f"{type(e).__name__}: {e}", file=sys.stderr)
    # Scale seam (§4 zoom protocol): dispatch personal-scale scenes triggered by
    # this season's world-state. Caller-side per season.py design. Side-effect-free
    # on strategic stats until the context-derivation bridge lands — see
    # sim/cross_scale/scene_dispatch.py GAP notes.
    _report = scene_dispatch.run_scene_phase(world, world.rng)
    world.scenes_resolved += _report["dispatch"]["resolved"]

    # Parliamentary vote (ED-SC-0006/0007, Jordan ruling "wire the canonical Parliamentary vote"):
    # the faction-scale §10 vote resolves directly on aggregate state, applies the §10 loser Mandate
    # penalty, and composes a winner Domain Echo (ED-SC-0002 composed keying) through the substrate.
    # Flag-gated by the scheduler's presence — a no-op when ECHO_TRANSPORT is off.
    if getattr(world, "echo_scheduler", None) is not None:
        from engine.cross_scale import parliamentary_bridge
        _pr = parliamentary_bridge.run_parliamentary_scene(world, world.rng)
        if _pr.get("resolved"):
            world.scenes_resolved += 1

    # ACTION->ACCOUNTING boundary (ED-IN-0028, OF-7): any echo Keys emitted during the scene
    # phase logged LIVE; their deferred faction/territory applies land here as accounting
    # begins, then the per-tick emission counter resets for next season. No-op when
    # ECHO_TRANSPORT is off (no scheduler) or while all scenes defer (empty queue).
    _sched = getattr(world, "echo_scheduler", None)
    if _sched is not None:
        _sched.accounting_boundary()
        _sched.next_tick()

    # OI-05/OI-07 (ED-IN-0091 plan §3 Wave 2 items 3-4) — the Accounting-adjacent point: this is
    # the last thing that runs in the season's action_callback before season.run_season's Step 3
    # (systems/overview/sim/season.py) hands off to accounting.run_accounting.
    #
    # OI-05 half already reachable, no change needed here: accounting.run_accounting already
    # calls systems.world.sim.npe.simulate_npc_actions every season (systems/overview/sim/
    # accounting.py:78-82, wired 2026-05-20 — "NPE — territory-level NPC stance drift", citing
    # investigation_systems_v30.md SYSTEM 1 §Persistence: "at season end, NPCs with shared
    # worldview and adjacent Stance positions make a Volatility check"). That call was already
    # here before this wave; verified live via accounting.py's own import + call site, not
    # re-implemented.
    #
    # generate_npc itself gets NO auto-call here (re-verified against investigation_systems_v30.md
    # SYSTEM 1 this wave, correcting the plan's assumption that "the season path IS specified"
    # for generation, not just drift): §Two-Tier Generation's Tier-1 archetype seed is driven
    # entirely by "Scene specification declares density and composition" — a per-SCENE trigger,
    # not a world-gen or season-tick count. No canon head names an initial world-gen population
    # nor a season-tick generation count (NPE-02's "cap at 3 persistent minor NPCs... Propose:"
    # is an unresolved Open Question, not a ratified number — not usable as a cited constant).
    # Per the no-fabrication rule (CLAUDE.md §5/§7, this wave's own instruction), the honest move
    # is to generate none automatically rather than invent a count or a trigger. Recorded via
    # stubwire (not silent) so the gap is greppable/counted, same discipline as the knots stub
    # immediately below.
    stubwire.stub_resolve(
        'engine.mc_v18', 'generate_npc(world-gen|season-tick)',
        reason="OI-05: investigation_systems_v30.md SYSTEM 1 Two-Tier Generation is scene-"
               "specification-driven only (\"Scene specification declares density and "
               "composition\") — no world-gen initial count and no season-tick generation "
               "trigger exist in canon to cite; NPE-02's proposed persistence-cap number is an "
               "unresolved Open Question. Honest deferral, not fabrication (CLAUDE.md §5/§7). "
               "simulate_npc_actions (the drift half) is already wired every season via "
               "accounting.run_accounting — see the comment above this call.")

    # OI-07 (world.knots half) — form_knot gets NO auto-call either, for the same no-fabrication
    # reason, re-verified against systems/fieldwork/knots_v30.md §3.1 this wave: Prerequisites
    # ("Disposition +5 with target NPC", "PC Bonds >= 5", "PC's current Knot count < "
    # "floor(Bonds/2) + 1") are personal-scale actor fields (Disposition, Bonds) that do not
    # exist anywhere on the aggregate strategic World — the same "context-derivation gap" the
    # scene_dispatch.py module docstring already names for combat/contest actor derivation, not
    # a new one. No world-gen or season-tick formation rule exists in canon to cite. Honest
    # deferral beats invented knots (this wave's own instruction).
    stubwire.stub_resolve(
        'engine.mc_v18', 'form_knot(world-gen|season-tick)',
        reason="OI-07: knots_v30.md §3.1 Prerequisites require personal-scale actor fields "
               "(Disposition, Bonds, TS) absent from the aggregate strategic World — no "
               "world-gen or season-tick formation rule exists in canon to cite. Honest "
               "deferral, not fabrication (CLAUDE.md §5/§7); world.knots stays empty this wave.")


def run_campaign(seed: int | None = None, max_seasons: int = 50,
                 params: dict | None = None) -> CampaignResult:
    """Run a single campaign to completion."""
    if seed is None:
        seed = int(time.time()) & 0xFFFFFFFF

    # F7-pattern telemetry (ED-IN-0091, plan §2.1): snapshot the module-cumulative stubwire
    # counter before the campaign runs so stub_hits below is THIS campaign's delta, not the
    # process-lifetime total (the counter is intentionally process-cumulative — see
    # engine/substrate/stubwire.py's docstring — so a delta is how a single campaign reads it).
    _stub_start = stubwire.invocations

    world = game_state.create_world(seed=seed)
    victory.reset()
    scene_slate.clear()

    effective_params = dict(DEFAULT_PARAMS)
    if params:
        effective_params.update(params)
    max_s = effective_params.get('CAMPAIGN_SEASONS', max_seasons)

    # ED-IN-0091 plan §2.2 (OI-01) — decide the DISPATCH_COMBAT_BRIDGE flag ONCE per campaign and
    # stash it on `world`, exactly as ECHO_TRANSPORT's decision is stashed via `world.echo_scheduler`
    # presence below: scene_dispatch reads the world attribute rather than re-deriving the flag
    # itself (single owner — CLAUDE.md §8), and every call in the season loop sees the same value.
    world.dispatch_combat_bridge = _dispatch_combat_bridge_on(effective_params)

    # ED-IN-0028 — attach the executable Key substrate to the world when ECHO_TRANSPORT is on.
    # Its presence is the flag the scene phase reads; absence => byte-exact legacy path.
    if _echo_transport_on(effective_params):
        from engine.cross_scale import echo_transport
        world.echo_scheduler = echo_transport.make_scheduler(
            cascade_depth_max=effective_params.get(
                'ECHO_CASCADE_DEPTH_MAX', echo_transport.DEFAULT_CASCADE_DEPTH_MAX),
            emissions_per_tick_max=effective_params.get(
                'ECHO_EMISSIONS_PER_TICK_MAX', echo_transport.DEFAULT_EMISSIONS_PER_TICK_MAX),
        )
        world.key_log = world.echo_scheduler.log
        world._echo_key_seq = 0
        # OI-08 (ED-IN-0091 plan §3 Wave 2 item 6) — articulation lane hook, implemented verbatim
        # per that lane's oracle_requests: subscribe_all is the ONLY production TickScheduler(...)
        # construction site's paired subscriber wiring (the seam lane itself does not own
        # mc_v18.py this wave — WORLD lane does). Registers the §3.1 trigger-table type_ids on
        # this campaign's scheduler; each fired trigger routes to a typed stubwire no-op (the
        # render layer stays ED-IN-0073's docket, unbuilt).
        from engine.cross_scale import articulation as _articulation
        _articulation.subscribe_all(world.echo_scheduler)

    for _ in range(max_s):
        if world.winner:
            break

        # season.run_season composes: advance_season → action_callback → run_accounting
        # [canonical: designs/architecture/campaign_architecture_v30.md;
        #  Deferred Migration Batch 2026-05-20 — replaces inline composition]
        run_season(world, action_callback=_faction_actions_callback)

        # === VICTORY CHECK (GD-1) ===
        results = victory.check_all_factions(world)
        for vr in results:
            if vr.won:
                world.winner = vr.faction_id
                break

    # Fallback winner by territory count (v17 L753-761)
    if not world.winner:
        scores = {}
        for fn, f in world.factions.items():
            if not f.parliamentary:
                continue
            held = sum(1 for tid in game_state.ALL_PLAYABLE_15
                       if tid in world.territories and world.territories[tid].owner == fn)
            scores[fn] = held * 10 + f.L + len(f.territories)
        if scores:
            world.winner = max(scores, key=scores.get)

    surviving = sum(1 for f in world.factions.values() if len(f.territories) > 0)

    _kl = getattr(world, "key_log", None)

    return CampaignResult(
        winner=world.winner,
        season=world.season,
        surviving=surviving,
        battle_count=world.battle_count,
        scenes_resolved=world.scenes_resolved,
        insurgencies_formed=len(world.insurgencies),
        npcs_generated=world.npc_counter,
        stub_hits=stubwire.invocations - _stub_start,
        # W3 Handoff item 2: `world` is fresh per campaign (created above), so this is already
        # the campaign's own total — no before/after delta needed (unlike stub_hits, which reads
        # a process-lifetime-cumulative module counter shared across a batch's campaigns).
        accord_drift_probe_hits=getattr(world, "accord_drift_probe_hits", 0),
        key_log_hash=_kl.content_hash() if _kl is not None else "",
        keys_emitted=len(_kl) if _kl is not None else 0,
        final_state=game_state.serialize_world(world),
    )


def run_batch(n: int = 100, base_seed: int = 0,
              params: dict | None = None) -> BatchResult:
    """Run n campaigns and aggregate results."""
    wins = Counter()
    total_battles = 0
    for i in range(n):
        r = run_campaign(seed=base_seed + i, params=params)
        if r.winner:
            wins[r.winner] += 1
        total_battles += r.battle_count

    total = sum(wins.values()) or 1
    factions = ['Crown', 'Church', 'Hafenmark', 'Varfell']
    return BatchResult(
        n=n,
        win_share={fn: round(wins.get(fn, 0) / total * 100, 1) for fn in factions},
        all_winners=dict(wins),
        battles_mean=round(total_battles / n, 1),
    )


if __name__ == '__main__':
    print("=== mc_v18 Phase 2 smoke test — 100 campaigns ===")
    r = run_batch(100, base_seed=42)
    print(f"  win_share: {r.win_share}")
    print(f"  all_winners: {r.all_winners}")
    print(f"  battles_mean: {r.battles_mean}")
