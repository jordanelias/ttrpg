"""
sim/autoload/game_state.py — Global mutable state container — factions, territories, world tracks

Canon source: designs/architecture/complete_systems_reference.md;
              [FORK: mc_v17.py starting state tables — ref c451bcb, superseded by mc_v18,
              file evacuated 2026-08-05, ED-IN-0145/ED-IN-0188]
Status: [CANONICAL — Phase 1 implementation 2026-05-17]
[PRE-LPS-1 (schema gap, NOT a port block) — ED-FA-0004, 2026-07-07: the Faction dataclass below
 (L/Sta/W/I/Mil; no Mandate / PS / Treasury / da.* Keys) implements the pre-LPS-1 SUPERSEDED
 faction stat model — this is literally where "no Mandate" lives. The ratified LPS-1 model
 (per-settlement L/PS, Mandate = 7T/(T+6), Treasury) is UNIMPLEMENTED. The self-imposed PORT BLOCK that stood here is DELETED (Jordan, 2026-08-15: "delete the code
 that blocks itself from being ported as that is stale" — ED-IN-0193). The SCHEMA GAP IS NOT
 STALE and is stated above; what was stale was gating the port on it. Port with eyes open. See
 systems/factions/faction_canon_v30.md / faction_behavior_v30.md.]

Dependencies:
  - engine.substrate.canon_buckets (canonical_accord re-export only — a no-deps leaf; this
    module remains otherwise a root primitive, everything else here is late-imported, OI-52a)

Entry points:
  - create_world(seed: int | None = None) -> World
  - serialize_world(world: World) -> dict
  - restore_world(snapshot: dict) -> World
"""
from __future__ import annotations

import copy
import random
from dataclasses import dataclass, field, fields as dc_fields

# canonical_accord relocated to engine/substrate/canon_buckets.py (OI-52a, ED-IN-0097, 2026-07-29
# — see that module's docstring for the full cycle-break rationale). Re-exported here so every
# existing `from engine.autoload.game_state import canonical_accord` / `game_state.canonical_accord`
# call site keeps working unchanged — engine/substrate/ has no internal dependents, so this import
# does not reintroduce the cycle it was moved to break.
from engine.substrate.canon_buckets import canonical_accord  # noqa: F401 (re-export)
from engine.substrate import composition
from engine.substrate import descriptors
from engine.substrate import world_initial_state  # sole runtime reader of references/world_initial_state.yaml


# ── The world's opening position (moved to references/ at plan S5b, 2026-08-22) ────────────────
# These were six Python literals here, inherited from mc_v17.py L62-82 (itself from mc_v15.py) with
# no authored source anywhere. They are WORLD DATA: which territories exist, who holds them at
# season 0, how settled and prosperous each is, where the garrisons start, which is Templar-held,
# and what each faction opens with. The authored source is references/world_initial_state.yaml, cooked by
# tools/export_world_initial_state.py behind a blocking --check and read by the leaf below.
#
# The NAMES are unchanged on purpose — they are cited across flow skeletons, design docs and tests,
# and renaming them while moving them would have made one change into two. `ALL_PLAYABLE_15` keeps
# its count-bearing name here while the leaf exposes it as `ALL_PLAYABLE`; the count is a fact about
# today's table, not a constraint on it.
ALL_PLAYABLE_15 = world_initial_state.ALL_PLAYABLE
STARTING_OWNER = world_initial_state.STARTING_OWNER
STARTING_STATS = world_initial_state.STARTING_STATS

# ⚠ MULTS STAYS A LITERAL, AND ITS REASON CHANGED ON 2026-08-23 — Q1 NO LONGER BLOCKS IT.
# It was held because authoring `L` as a faction-stat row in references/descriptor_registry.yaml
# would have answered the open ruling on whether Legitimacy is a base descriptor. Jordan ruled it
# IS, so `fac.legitimacy` is declared and that objection is discharged. The registry is still the
# correct home — it already states two of these values in prose ("Legitimacy (faction, derived) is
# Mandate x 20", "Discipline (faction) is Stability x 10").
#
# TWO REASONS SURVIVE, and they are smaller and nameable rather than a ruling:
#   1. MULTS spans TWO registry blocks. `accord` and `pt` are Territory fields, so a faction-only
#      move would split one dict across two homes — the "one seam owned twice" defect S5a spent two
#      commits removing. The move wants `internal_multiplier` on both `faction_stats` and
#      `territory_stats` entries, in one pass.
#   2. The numbers need provenance. 20 and 10 are stated in the registry's own prose; 100, 15 and
#      the two territory 10s are stated nowhere this session could find, and the anti-fabrication
#      gate would rightly refuse them into an authored surface uncited.
# Do NOT resolve this by moving MULTS into world_initial_state.yaml: it is not initial state, and
# a file whose name lies is worse than a literal that is honest.
MULTS = {'L': 20, 'Sta': 10, 'W': 100, 'I': 15, 'Mil': 10, 'accord': 10, 'pt': 10}

ACCORD_MAP = {0: 1.0, 1: 2.5, 2: 4.0, 3: 5.5, 4: 7.0}
PT_MAP = {0: 1.0, 1: 2.5, 2: 4.0, 3: 5.5, 4: 6.5, 5: 7.0}


# Reverse mappers — continuous → canonical-int.
# Canon PT/Accord are categorical 0-5 / 0-4; game_state stores continuous
# values via PT_MAP / ACCORD_MAP. Modules that look up canon-keyed tables
# (CI_YIELD_BY_PT, Seizure Ob, Ecology weights) MUST bucket through these
# helpers, not via int(t.pt) which drifts (pt=7.0 → int=7 is no canon bucket).
# [canonical: game_state PT_MAP/ACCORD_MAP — the inverse is forced by these tables.]
# canonical_accord moved to engine/substrate/canon_buckets.py and is imported/re-exported near
# the top of this file (OI-52a, ED-IN-0097, 2026-07-29 — cycle break with systems.world.sim.npe).
# canonical_pt stays here: nothing on that cycle's boundary imports it, so moving it was out of
# scope — logged as a residual shape-hygiene split, not chased (CLAUDE.md §0.1 point 5).

def canonical_pt(continuous_pt: float) -> int:
    """Map continuous PT (range 0.5-7.0 per PT_MAP) → canonical integer 0-5.
    Uses nearest-neighbor with midpoints between successive canonical floats.
    PT_MAP: 1.0, 2.5, 4.0, 5.5, 6.5, 7.0. Midpoints: 1.75, 3.25, 4.75, 6.0, 6.75."""
    if continuous_pt < 1.75: return 0
    if continuous_pt < 3.25: return 1
    if continuous_pt < 4.75: return 2
    if continuous_pt < 6.0:  return 3
    if continuous_pt < 6.75: return 4
    return 5


# The other three columns of the same table — see the block above.
STARTING_ACCORD = world_initial_state.STARTING_ACCORD
STARTING_PT = world_initial_state.STARTING_PT
STARTING_GARRISON = world_initial_state.STARTING_GARRISON


@dataclass
class Faction:
    name: str
    parliamentary: bool = True
    L: float = 2.0
    Sta: float = 3.0
    W: float = 2.0
    I: float = 2.0
    Mil: float = 3.0
    # fac.intel — ratified 2026-07-08 (descriptor_registry.yaml, OPT-AV-18 / ED-IN-0029) with
    # floor 0, scale 0-7, but the Faction dataclass never carried the field (audit ED-IN-0074 D4).
    # Added at the ratified floor. Currently unread/unwritten by live code (adjust() is not wired
    # for it — no MULTS['intel'] entry until its mechanic is designed); this only closes the
    # canon-vs-code gap so a future reader of `faction.intel` doesn't AttributeError.
    intel: float = 0.0
    territories: list = field(default_factory=list)  # [hash-seed fix 2026-05-20] was set; set iteration depends on PYTHONHASHSEED for str keys, producing cross-process variance in mc_v18 batches. list preserves insertion order; faction territories ≤15 so O(n) membership is negligible.
    # Seasonal resets
    senator_inward_used: bool = False
    consul_used: bool = False
    peaceful: bool = True
    standing: int = 0
    # NEW Phase 5/9 faction-unique action flags
    excommunicated: bool = False
    council_used_this_arc: bool = False
    # OI-04 Wave-2 canon gate (parliamentary_transfer_v30.md §1.1, ":27" — "Frequency: 1 per arc
    # per faction"): mirrors council_used_this_arc's own per-arc-flag shape exactly (same field,
    # same reset hook) — one faction may attempt Parliamentary Transfer at most once per arc,
    # regardless of outcome.
    parl_transfer_used_this_arc: bool = False

    #: The bounds `adjust` falls back to when `references/descriptor_registry.yaml` declares none.
    #: ⚠ NO FACTION STAT REACHES THIS ANY MORE (2026-08-23). It existed for `L`, whose registry
    #: status was the open Q1 ruling; Jordan ruled Legitimacy IS a base descriptor, so all six
    #: faction stats are declared and clamp from the registry. What still reaches it is a caller
    #: passing a stat that is not a faction descriptor at all — `MULTS` carries `accord` and `pt`,
    #: which are Territory fields, and `echo_transport`'s dynamic write is gated on MULTS
    #: membership rather than on the registry. So this is now a genuine fallback for a genuine
    #: hole, not a placeholder for an unruled stat. These were the BLANKET bounds every stat used
    #: before ED-IN-0029 was wired at plan S5d.
    UNDECLARED_FLOOR = 0.5
    # Same ceiling the registry declares for every stat it DOES declare, so the undeclared case is
    # not quietly more permissive than the declared ones.
    UNDECLARED_CEILING = 7.0  # [canonical: references/descriptor_registry.yaml faction_stats — scale "0-7"/"1-7"]

    def adjust(self, stat: str, granular_delta: float,
               floor: float | None = None, ceiling: float | None = None):
        """Apply a granular delta to a faction stat, clamped to the bounds the REGISTRY declares.

        ED-IN-0029 (ratified 2026-07-08, OPT-AV-14/D14 + OPT-AV-18) set per-stat floors: Influence
        floors at 1 — an institution's influence never fully vanishes — and Wealth, Military,
        Stability and Intel float at 0. This method applied a blanket 0.5/7.0 to every stat for the
        six weeks after that ratification, and none of its 31 call sites overrode it, so a ratified
        canon decision had never reached the executable model. `descriptors.faction_bounds()` is
        the single owner of those numbers; this is its first runtime caller.

        ⚠ FOUR OF THE FIVE FLOORS REACH THE CODE. `intel` does not, and saying "ED-IN-0029 is now
        wired" without this qualification would be the false-claim class §1(a) of the plan exists to
        stop. `MULTS` has no `intel` key, so `adjust('intel', …)` raises `KeyError` on the line
        below before any bound is consulted — `faction_bounds('intel')` returns (0, 7) that no code
        path can reach. That is consistent with the field's own history: `fac.intel` was added to
        the dataclass at its ratified floor and is documented as unread and unwritten by live code.
        Wiring it needs a multiplier, which is a canon value nobody has stated, so it is recorded
        here rather than invented.

        `L` KEEPS THE OLD BOUNDS, and that is a decision rather than an omission. The registry
        declares no entry for Legitimacy — whether it is a base faction descriptor or derived like
        Mandate is Q1, open to Jordan — so `faction_bounds` returns None for it and this falls back
        to 0.5/7.0. Twenty of the 31 call sites adjust `L`, so this is the majority of traffic and
        it is deliberately unchanged: wiring a floor for a stat the registry does not declare would
        be inventing canon, which is the one thing a wiring commit must not do.

        The explicit `floor`/`ceiling` parameters survive with no live caller. They are how a call
        site would state a locally-canonical bound, and removing an unused parameter is its own
        change; what they no longer do is silently supply the DEFAULT for every stat.
        """
        bounds = descriptors.faction_bounds(stat)
        if floor is None:
            floor = bounds[0] if bounds else self.UNDECLARED_FLOOR
        if ceiling is None:
            ceiling = bounds[1] if bounds else self.UNDECLARED_CEILING
        mult = MULTS[stat]
        val = getattr(self, stat)
        val = max(floor, min(ceiling, val + granular_delta / mult))
        setattr(self, stat, val)

    def reset_seasonal(self):
        self.senator_inward_used = False
        self.consul_used = False

    def reset_arc(self):
        """Called by season_manager on arc boundary (new_arc=True)."""
        self.council_used_this_arc = False
        self.parl_transfer_used_this_arc = False  # OI-04 Wave-2 canon gate (§1.1 Frequency)


# ── references/ IS LOAD-BEARING HERE, AT RUNTIME (2026-08-20) ────────────────────────────────────
# Until this line, `references/descriptor_registry.yaml` was read by TOOLS ONLY: measured across
# both trees, no module under engine/ or systems/ loaded it, and every runtime mention was a comment
# or a docstring — while MULTS above and the Faction fields below were hardcoded twins of what it
# declares. A registry nothing executes is a document, not a root, and the premise this repo works
# from is that systems/ stems from engine/ AND references/.
#
# The check runs at import and ONE WAY: a faction stat declared in the registry with no field here
# stops the engine from importing. It deliberately does NOT fail on the reverse, because exactly one
# such field existed — `L` (written by 20 of .adjust()'s 31 non-test call sites, AST-counted
# 2026-08-22; the 32 this line used to claim was a grep that counted comments). It is DECLARED as
# of 2026-08-23, so the count of unregistered Faction fields is zero and the one-way direction now
# protects nothing that exists. It is kept because a NEW dataclass field's registry status is a
# ruling, not a check's call — see assert_faction_roster_is_covered's own docstring.
#
# WIRED 2026-08-22 (plan S5d). The registry's PER-STAT floors, ratified 2026-07-08 (ED-IN-0029) —
# Influence floors at 1, the rest at 0 — reach the executable model: `Faction.adjust` above reads
# `descriptors.faction_bounds()` instead of applying a blanket 0.5 to every stat. It had been
# ratified canon that never reached code for six weeks. `L` keeps the old bounds because the
# registry declares no entry for it and Q1 (is Legitimacy a base descriptor?) is Jordan's open
# ruling; inventing a floor for it here would be authoring canon inside a wiring commit.
# The goldens moved and were re-recorded against a measured n=120 control — see that commit.
descriptors.assert_faction_roster_is_covered({f.name for f in dc_fields(Faction)})


@dataclass
class Territory:
    tid: str
    owner: str | None
    accord: float
    pt: float
    garrison: bool
    prosperity: int
    fort_level: int
    templar: bool = False
    uncontrolled_since: int | None = None

    def is_uncontrolled(self) -> bool:
        return self.owner is None

    def adjust_accord(self, granular_delta: float):
        self.accord = max(0.5, min(7.0, self.accord + granular_delta / MULTS['accord']))

    def adjust_pt(self, granular_delta: float):
        self.pt = max(0.5, min(7.0, self.pt + granular_delta / MULTS['pt']))


@dataclass
class World:
    factions: dict[str, Faction] = field(default_factory=dict)
    territories: dict[str, Territory] = field(default_factory=dict)
    clocks: dict[str, float] = field(default_factory=dict)
    season: int = 0
    arc: int = 0
    winner: str | None = None
    battle_count: int = 0
    scenes_resolved: int = 0        # F7 telemetry (ED-IN-0021): personal-scale scenes actually resolved (not deferred) — additive counter, no behaviour effect
    rng: random.Random = field(default_factory=random.Random)
    # ─── Schema migration 2026-05-19 ──────────────────────────────────────
    # Registries for Tier 0 modules that previously held module-level state.
    # Values use Any-typing because the owning module defines its own
    # dataclass (CoherenceState, InsurgencyRecord, NPC, TreatyRecord) and
    # bidirectional typing would create import cycles. Consumer modules
    # check type at runtime.
    # [canonical: proposals/stub_infill_plan.md Amendment 2026-05-19
    #  "schema-migration commit that adds the missing registries"]
    practitioners: dict = field(default_factory=dict)            # actor_id → CoherenceState (from systems/threadwork/sim/coherence)
    insurgencies: dict = field(default_factory=dict)             # insurgency_id → InsurgencyRecord (from systems/world/sim/insurgency_pipeline)
    uncontrolled_streaks: dict = field(default_factory=dict)     # frozenset[tid] → consecutive seasons (from systems/world/sim/insurgency_pipeline)
    npcs: dict = field(default_factory=dict)                     # territory_id → list[NPC] (from systems/world/sim/npe)
    npc_counter: int = 0                                          # incrementing id source for NPC generation
    treaties: dict = field(default_factory=dict)                 # frozenset[parties] → TreatyRecord (from systems/factions/sim/treaty)
    # ─── Schema migration #2 — 2026-05-19 ─────────────────────────────────
    # Tier 1/2 registries. Same Any-typing rationale + _store(world) router
    # pattern as migration #1. Modules retain module-level fallback when
    # world is None (legacy callers + tests).
    # [canonical: proposals/stub_infill_plan.md Amendment 2026-05-19c
    #  follow-on "Schema migration #2 to add world.convictions, world.beliefs..."]
    convictions: dict = field(default_factory=dict)              # actor_id → ConvictionState (from sim/personal/conviction)
    beliefs: dict = field(default_factory=dict)                  # actor_id → list[Belief] (from sim/personal/beliefs)
    knots: dict = field(default_factory=dict)                    # knot_id → Knot (from sim/personal/knots)
    knot_id_counter: int = 0                                      # incrementing id source for Knot generation
    territory_infrastructure: dict = field(default_factory=dict) # territory_id → InfrastructureState (from systems/settlements/sim/infrastructure)
    npc_drift_state: dict = field(default_factory=dict)          # territory_id → drift float (from systems/settlements/sim/temperaments)
    threadcut_beings: dict = field(default_factory=dict)         # being_id → ThreadcutState (from systems/threadwork/sim/threadcut)
    comovement_deck: dict = field(default_factory=lambda: {'remaining': [], 'discard': []})  # global deck state (from systems/threadwork/sim/co_movement)
    # ─── Schema migration #3 — 2026-06-23 (settlement registry, audit gap G1) ──
    # A province now holds its canonical 1-3 settlements (settlement_layer
    # §1.1/§2.1) instead of the prior 1:1 territory->settlement stub. Same
    # Any-typing + store-router rationale as migrations #1/#2; the owning module
    # systems/settlements/sim/registry defines Settlement and falls back to a module-level
    # store when world is None (legacy callers + tests).
    # [canonical: systems/settlements/goldenfurt_slice/sim_build_spec.md §1]
    settlements: dict = field(default_factory=dict)             # sid → Settlement (from systems/settlements/sim/registry)


def create_world(seed: int | None = None) -> World:
    """Build canonical starting world state."""
    rng = random.Random(seed)
    factions = {}
    for name, stats in STARTING_STATS.items():
        f = Faction(name=name, **stats)
        # [hash-seed fix 2026-05-20] set-comp → list-comp; ordered by STARTING_OWNER dict-insertion order (deterministic)
        f.territories = [tid for tid, o in STARTING_OWNER.items() if o == name]
        factions[name] = f

    territories = {}
    for tid, owner in STARTING_OWNER.items():
        t = Territory(
            tid=tid, owner=owner,
            accord=ACCORD_MAP[STARTING_ACCORD[tid]],
            pt=PT_MAP[STARTING_PT[tid]],
            garrison=STARTING_GARRISON.get(tid, False),
            prosperity=world_initial_state.STARTING_PROSPERITY[tid],
            # fort_level stays DERIVED from garrison rather than authored: it is a rule, not data,
            # and authoring it would give one number two owners.
            fort_level=1 if STARTING_GARRISON.get(tid, False) else 0,
            templar=world_initial_state.STARTING_TEMPLAR[tid],
        )
        territories[tid] = t

    world = World(
        factions=factions,
        territories=territories,
        # IP (Institutional Pressure) added per audit ED-IN-0074 D2 — it was absent from the
        # roster entirely, so the peninsular_strain occupation-phase era ladder could never
        # read it. Currently unread by live code (peninsular_strain is unbuilt), so this is
        # dormant groundwork with no behavioural effect today; recalibrate the start when that
        # module wires readers (the live CI/MS starts already diverge from the registry doc).
        # [canonical: clock_registry_v30.md — IP start 20]
        clocks={'CI': 30.0, 'MS': 60.0, 'IP': 20.0, 'PI': 0.0, 'Strain': 0.0, 'Turmoil': 0.0},
        rng=rng,
    )
    # OI-07 (ED-IN-0091 plan §3 Wave 2 item 4) — populate world.settlements at world-gen from
    # the canonical geography source (systems/settlements/valoria_geography_v30.yaml, the
    # PP-726-rebuilt geography YAML — see registry.populate_from_geography's own docstring for
    # the full field-mapping citation). Late-import: game_state.py stays a root primitive for
    # everything except the engine.substrate.canon_buckets re-export (a no-deps leaf, see the
    # module docstring) and must not statically depend on a downstream sim module. npe.py used to
    # apply the same discipline in reverse for its game_state.canonical_accord import — that edge
    # is now gone (OI-52a, ED-IN-0097, 2026-07-29: canonical_accord moved to
    # engine.substrate.canon_buckets, which both modules import at top level without a cycle).
    # Deterministic — no RNG draw, so this cannot move any RNG-derived campaign golden.
    composition.require('world_gen_settlements')(world)
    return world


def serialize_world(world: World) -> dict:
    """Snapshot world state for save/restore.

    Includes the 14 registries from schema migrations #1 (94dac72e) and
    #2 (d2941cde), plus schema migration #3's `settlements` registry (OI-07,
    ED-IN-0091 plan §3 Wave 2 item 4 — previously declared on World but never
    serialized). Each owning dataclass exposes .to_dict() — see modules:
    coherence, insurgency_pipeline, npe, treaty, conviction, beliefs,
    knots, infrastructure, threadcut, registry (settlements).
    """
    return {
        'season': world.season, 'arc': world.arc, 'winner': world.winner,
        'battle_count': world.battle_count,
        'clocks': dict(world.clocks),
        'factions': {
            fn: {'L': f.L, 'Sta': f.Sta, 'W': f.W, 'I': f.I, 'Mil': f.Mil,
                 'territories': list(f.territories), 'parliamentary': f.parliamentary,
                 'standing': f.standing,
                 'excommunicated': f.excommunicated,
                 'council_used_this_arc': f.council_used_this_arc,
                 'parl_transfer_used_this_arc': f.parl_transfer_used_this_arc}
            for fn, f in world.factions.items()
        },
        'territories': {
            tid: {'owner': t.owner, 'accord': t.accord, 'pt': t.pt,
                  'garrison': t.garrison, 'prosperity': t.prosperity,
                  'fort_level': t.fort_level, 'templar': t.templar}
            for tid, t in world.territories.items()
        },
        # ─── Schema migration #1 registries ──────────────────────────────
        'practitioners': {k: (v.to_dict() if hasattr(v, 'to_dict') else v)
                          for k, v in world.practitioners.items()},
        'insurgencies': {k: (v.to_dict() if hasattr(v, 'to_dict') else v)
                         for k, v in world.insurgencies.items()},
        # uncontrolled_streaks: keys are frozensets — encode as sorted-list-of-tids
        'uncontrolled_streaks': [{'tids': sorted(list(fs)), 'streak': cnt}
                                  for fs, cnt in world.uncontrolled_streaks.items()],
        'npcs': {tid: [n.to_dict() if hasattr(n, 'to_dict') else n
                       for n in npc_list]
                 for tid, npc_list in world.npcs.items()},
        'npc_counter': world.npc_counter,
        # treaties: keys are frozensets — encode as sorted-list-of-parties
        'treaties': [{'parties_key': sorted(list(fs)),
                      'record': (rec.to_dict() if hasattr(rec, 'to_dict') else rec)}
                     for fs, rec in world.treaties.items()],
        # ─── Schema migration #2 registries ──────────────────────────────
        'convictions': {k: (v.to_dict() if hasattr(v, 'to_dict') else v)
                        for k, v in world.convictions.items()},
        'beliefs': {k: [b.to_dict() if hasattr(b, 'to_dict') else b
                        for b in v]
                    for k, v in world.beliefs.items()},
        'knots': {k: (v.to_dict() if hasattr(v, 'to_dict') else v)
                  for k, v in world.knots.items()},
        'knot_id_counter': world.knot_id_counter,
        'territory_infrastructure': {k: (v.to_dict() if hasattr(v, 'to_dict') else v)
                                     for k, v in world.territory_infrastructure.items()},
        'npc_drift_state': dict(world.npc_drift_state),
        'threadcut_beings': {k: (v.to_dict() if hasattr(v, 'to_dict') else v)
                             for k, v in world.threadcut_beings.items()},
        # comovement_deck: tuples in 'remaining' / 'discard' lists — coerce to lists
        'comovement_deck': {
            'remaining': [list(c) for c in world.comovement_deck.get('remaining', [])],
            'discard': [list(c) for c in world.comovement_deck.get('discard', [])],
        },
        # ─── Schema migration #3 registry (OI-07) ─────────────────────────
        'settlements': {sid: (s.to_dict() if hasattr(s, 'to_dict') else s)
                        for sid, s in world.settlements.items()},
    }


def restore_world(snapshot: dict) -> World:
    """Restore world state from snapshot.

    Reconstructs all 14 World registries via late-imports on the owning
    modules' .from_dict() classmethods, plus migration #3's `settlements`
    registry (OI-07). Snapshots produced by an older schema version
    (pre-migration #1, #2, or #3) are tolerated: missing registry keys
    default to empty dicts.
    """
    w = World()
    w.season = snapshot['season']
    w.arc = snapshot['arc']
    w.winner = snapshot.get('winner')
    w.battle_count = snapshot.get('battle_count', 0)
    w.clocks = dict(snapshot['clocks'])
    for fn, fd in snapshot['factions'].items():
        f = Faction(name=fn, L=fd['L'], Sta=fd['Sta'], W=fd['W'],
                    I=fd['I'], Mil=fd['Mil'], parliamentary=fd.get('parliamentary', True),
                    standing=fd.get('standing', 0))
        f.territories = list(fd['territories'])  # [hash-seed fix 2026-05-20] was set(...)
        f.excommunicated = fd.get('excommunicated', False)
        f.council_used_this_arc = fd.get('council_used_this_arc', False)
        f.parl_transfer_used_this_arc = fd.get('parl_transfer_used_this_arc', False)
        w.factions[fn] = f
    for tid, td in snapshot['territories'].items():
        t = Territory(tid=tid, owner=td['owner'], accord=td['accord'], pt=td['pt'],
                      garrison=td['garrison'], prosperity=td['prosperity'],
                      fort_level=td['fort_level'], templar=td.get('templar', False))
        w.territories[tid] = t

    # ─── Schema migration #1 registries ──────────────────────────────────
    # Late-import each owning module's dataclass for .from_dict
    if 'practitioners' in snapshot:
        CoherenceState = composition.require('snapshot_state.practitioners')
        w.practitioners = {k: CoherenceState.from_dict(v)
                            for k, v in snapshot['practitioners'].items()}
    if 'insurgencies' in snapshot:
        InsurgencyRecord = composition.require('snapshot_state.insurgencies')
        w.insurgencies = {k: InsurgencyRecord.from_dict(v)
                           for k, v in snapshot['insurgencies'].items()}
    if 'uncontrolled_streaks' in snapshot:
        w.uncontrolled_streaks = {frozenset(entry['tids']): entry['streak']
                                   for entry in snapshot['uncontrolled_streaks']}
    if 'npcs' in snapshot:
        NPC = composition.require('snapshot_state.npcs')
        w.npcs = {tid: [NPC.from_dict(n) for n in npc_list]
                   for tid, npc_list in snapshot['npcs'].items()}
    w.npc_counter = snapshot.get('npc_counter', 0)
    if 'treaties' in snapshot:
        TreatyRecord = composition.require('snapshot_state.treaties')
        w.treaties = {frozenset(entry['parties_key']): TreatyRecord.from_dict(entry['record'])
                       for entry in snapshot['treaties']}

    # ─── Schema migration #2 registries ──────────────────────────────────
    if 'convictions' in snapshot:
        ConvictionState = composition.require('snapshot_state.convictions')
        w.convictions = {k: ConvictionState.from_dict(v)
                          for k, v in snapshot['convictions'].items()}
    if 'beliefs' in snapshot:
        Belief = composition.require('snapshot_state.beliefs')
        w.beliefs = {k: [Belief.from_dict(b) for b in v]
                      for k, v in snapshot['beliefs'].items()}
    if 'knots' in snapshot:
        Knot = composition.require('snapshot_state.knots')
        w.knots = {k: Knot.from_dict(v) for k, v in snapshot['knots'].items()}
    w.knot_id_counter = snapshot.get('knot_id_counter', 0)
    if 'territory_infrastructure' in snapshot:
        InfrastructureState = composition.require('snapshot_state.territory_infrastructure')
        w.territory_infrastructure = {k: InfrastructureState.from_dict(v)
                                       for k, v in snapshot['territory_infrastructure'].items()}
    if 'npc_drift_state' in snapshot:
        w.npc_drift_state = dict(snapshot['npc_drift_state'])
    if 'threadcut_beings' in snapshot:
        ThreadcutState = composition.require('snapshot_state.threadcut_beings')
        w.threadcut_beings = {k: ThreadcutState.from_dict(v)
                               for k, v in snapshot['threadcut_beings'].items()}
    if 'comovement_deck' in snapshot:
        # Restore tuples from saved lists (matches CO_MOVEMENT_CARDS shape)
        w.comovement_deck = {
            'remaining': [tuple(c) for c in snapshot['comovement_deck'].get('remaining', [])],
            'discard': [tuple(c) for c in snapshot['comovement_deck'].get('discard', [])],
        }

    # ─── Schema migration #3 registry (OI-07) ─────────────────────────────
    if 'settlements' in snapshot:
        Settlement = composition.require('snapshot_state.settlements')
        w.settlements = {k: Settlement.from_dict(v) for k, v in snapshot['settlements'].items()}

    return w
