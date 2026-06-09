"""
sim/autoload/game_state.py — Global mutable state container — factions, territories, world tracks

Canon source: designs/architecture/complete_systems_reference.md; mc_v17.py starting state tables
Status: [CANONICAL — Phase 1 implementation 2026-05-17]

Dependencies:
  - none — root primitive

Entry points:
  - create_world(seed: int | None = None) -> World
  - serialize_world(world: World) -> dict
  - restore_world(snapshot: dict) -> World
"""
from __future__ import annotations

import copy
import random
from dataclasses import dataclass, field


# Canonical starting state (mc_v17.py L62-82, sourced from mc_v15.py)
ALL_PLAYABLE_15 = frozenset({
    'T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'T9', 'T10',
    'T11', 'T12', 'T13', 'T14', 'T17',
})

MULTS = {'L': 20, 'Sta': 10, 'W': 100, 'I': 15, 'Mil': 10, 'accord': 10, 'pt': 10}

STARTING_OWNER = {
    'T1': 'Crown', 'T2': 'Crown', 'T3': 'Crown', 'T4': 'Varfell',
    'T5': 'Crown', 'T6': 'Crown', 'T7': 'Hafenmark', 'T8': 'Hafenmark',
    'T9': 'Church', 'T10': 'Hafenmark', 'T11': 'Varfell', 'T12': 'Varfell',
    'T13': 'Varfell', 'T14': 'Crown', 'T15': None, 'T17': 'Hafenmark',
}

STARTING_STATS = {
    'Crown':     {'L': 5.0, 'Sta': 4.0, 'W': 4.0, 'I': 5.0, 'Mil': 4.0},
    'Church':    {'L': 5.0, 'Sta': 5.0, 'W': 5.0, 'I': 6.0, 'Mil': 4.0},
    'Hafenmark': {'L': 4.0, 'Sta': 4.0, 'W': 5.0, 'I': 4.0, 'Mil': 3.0},
    'Varfell':   {'L': 4.0, 'Sta': 4.0, 'W': 4.0, 'I': 4.0, 'Mil': 4.0},
}

ACCORD_MAP = {0: 1.0, 1: 2.5, 2: 4.0, 3: 5.5, 4: 7.0}
PT_MAP = {0: 1.0, 1: 2.5, 2: 4.0, 3: 5.5, 4: 6.5, 5: 7.0}


# Reverse mappers — continuous → canonical-int.
# Canon PT/Accord are categorical 0-5 / 0-4; game_state stores continuous
# values via PT_MAP / ACCORD_MAP. Modules that look up canon-keyed tables
# (CI_YIELD_BY_PT, Seizure Ob, Ecology weights) MUST bucket through these
# helpers, not via int(t.pt) which drifts (pt=7.0 → int=7 is no canon bucket).
# [canonical: game_state PT_MAP/ACCORD_MAP — the inverse is forced by these tables.]

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


def canonical_accord(continuous_accord: float) -> int:
    """Map continuous Accord (range 0.5-7.0 per ACCORD_MAP) → canonical integer 0-4.
    ACCORD_MAP: 1.0, 2.5, 4.0, 5.5, 7.0. Midpoints: 1.75, 3.25, 4.75, 6.25."""
    if continuous_accord < 1.75: return 0
    if continuous_accord < 3.25: return 1
    if continuous_accord < 4.75: return 2
    if continuous_accord < 6.25: return 3
    return 4
STARTING_ACCORD = {'T1': 3, 'T2': 3, 'T3': 3, 'T4': 2, 'T5': 2, 'T6': 2,
                   'T7': 2, 'T8': 3, 'T9': 4, 'T10': 2, 'T11': 2, 'T12': 2,
                   'T13': 1, 'T14': 3, 'T15': 0, 'T17': 2}
STARTING_PT = {'T1': 3, 'T2': 3, 'T3': 3, 'T4': 2, 'T5': 3, 'T6': 1,
               'T7': 3, 'T8': 3, 'T9': 5, 'T10': 3, 'T11': 2, 'T12': 2,
               'T13': 1, 'T14': 3, 'T15': 3, 'T17': 3}
STARTING_GARRISON = {'T1': True, 'T8': True, 'T9': True, 'T12': True}


@dataclass
class Faction:
    name: str
    parliamentary: bool = True
    L: float = 2.0
    Sta: float = 3.0
    W: float = 2.0
    I: float = 2.0
    Mil: float = 3.0
    territories: list = field(default_factory=list)  # [hash-seed fix 2026-05-20] was set; set iteration depends on PYTHONHASHSEED for str keys, producing cross-process variance in mc_v18 batches. list preserves insertion order; faction territories ≤15 so O(n) membership is negligible.
    # Seasonal resets
    senator_inward_used: bool = False
    consul_used: bool = False
    peaceful: bool = True
    standing: int = 0
    # NEW Phase 5/9 faction-unique action flags
    excommunicated: bool = False
    council_used_this_arc: bool = False

    def adjust(self, stat: str, granular_delta: float,
               floor: float = 0.5, ceiling: float = 7.0):
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
    rng: random.Random = field(default_factory=random.Random)
    # ─── Schema migration 2026-05-19 ──────────────────────────────────────
    # Registries for Tier 0 modules that previously held module-level state.
    # Values use Any-typing because the owning module defines its own
    # dataclass (CoherenceState, InsurgencyRecord, NPC, TreatyRecord) and
    # bidirectional typing would create import cycles. Consumer modules
    # check type at runtime.
    # [canonical: designs/proposals/stub_infill_plan.md Amendment 2026-05-19
    #  "schema-migration commit that adds the missing registries"]
    practitioners: dict = field(default_factory=dict)            # actor_id → CoherenceState (from sim/thread/coherence)
    insurgencies: dict = field(default_factory=dict)             # insurgency_id → InsurgencyRecord (from sim/world/insurgency_pipeline)
    uncontrolled_streaks: dict = field(default_factory=dict)     # frozenset[tid] → consecutive seasons (from sim/world/insurgency_pipeline)
    npcs: dict = field(default_factory=dict)                     # territory_id → list[NPC] (from sim/world/npe)
    npc_counter: int = 0                                          # incrementing id source for NPC generation
    treaties: dict = field(default_factory=dict)                 # frozenset[parties] → TreatyRecord (from sim/provincial/treaty)
    # ─── Schema migration #2 — 2026-05-19 ─────────────────────────────────
    # Tier 1/2 registries. Same Any-typing rationale + _store(world) router
    # pattern as migration #1. Modules retain module-level fallback when
    # world is None (legacy callers + tests).
    # [canonical: designs/proposals/stub_infill_plan.md Amendment 2026-05-19c
    #  follow-on "Schema migration #2 to add world.convictions, world.beliefs..."]
    convictions: dict = field(default_factory=dict)              # actor_id → ConvictionState (from sim/personal/conviction)
    beliefs: dict = field(default_factory=dict)                  # actor_id → list[Belief] (from sim/personal/beliefs)
    knots: dict = field(default_factory=dict)                    # knot_id → Knot (from sim/personal/knots)
    knot_id_counter: int = 0                                      # incrementing id source for Knot generation
    territory_infrastructure: dict = field(default_factory=dict) # territory_id → InfrastructureState (from sim/territory/infrastructure)
    npc_drift_state: dict = field(default_factory=dict)          # territory_id → drift float (from sim/territory/temperaments)
    threadcut_beings: dict = field(default_factory=dict)         # being_id → ThreadcutState (from sim/thread/threadcut)
    comovement_deck: dict = field(default_factory=lambda: {'remaining': [], 'discard': []})  # global deck state (from sim/thread/co_movement)


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
            prosperity=2 if tid in {'T1', 'T2', 'T3', 'T8', 'T9', 'T14'} else 1,
            fort_level=1 if STARTING_GARRISON.get(tid, False) else 0,
            templar=(tid == 'T9'),
        )
        territories[tid] = t

    return World(
        factions=factions,
        territories=territories,
        clocks={'CI': 30.0, 'MS': 60.0, 'PI': 0.0, 'Strain': 0.0, 'Turmoil': 0.0},
        rng=rng,
    )


def serialize_world(world: World) -> dict:
    """Snapshot world state for save/restore.

    Includes the 14 registries from schema migrations #1 (94dac72e) and
    #2 (d2941cde). Each owning dataclass exposes .to_dict() — see modules:
    coherence, insurgency_pipeline, npe, treaty, conviction, beliefs,
    knots, infrastructure, threadcut.
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
                 'council_used_this_arc': f.council_used_this_arc}
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
    }


def restore_world(snapshot: dict) -> World:
    """Restore world state from snapshot.

    Reconstructs all 14 World registries via late-imports on the owning
    modules' .from_dict() classmethods. Snapshots produced by an older
    schema version (pre-migration #1 or pre-#2) are tolerated: missing
    registry keys default to empty dicts.
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
        w.factions[fn] = f
    for tid, td in snapshot['territories'].items():
        t = Territory(tid=tid, owner=td['owner'], accord=td['accord'], pt=td['pt'],
                      garrison=td['garrison'], prosperity=td['prosperity'],
                      fort_level=td['fort_level'], templar=td.get('templar', False))
        w.territories[tid] = t

    # ─── Schema migration #1 registries ──────────────────────────────────
    # Late-import each owning module's dataclass for .from_dict
    if 'practitioners' in snapshot:
        from sim.thread.coherence import CoherenceState
        w.practitioners = {k: CoherenceState.from_dict(v)
                            for k, v in snapshot['practitioners'].items()}
    if 'insurgencies' in snapshot:
        from sim.world.insurgency_pipeline import InsurgencyRecord
        w.insurgencies = {k: InsurgencyRecord.from_dict(v)
                           for k, v in snapshot['insurgencies'].items()}
    if 'uncontrolled_streaks' in snapshot:
        w.uncontrolled_streaks = {frozenset(entry['tids']): entry['streak']
                                   for entry in snapshot['uncontrolled_streaks']}
    if 'npcs' in snapshot:
        from sim.world.npe import NPC
        w.npcs = {tid: [NPC.from_dict(n) for n in npc_list]
                   for tid, npc_list in snapshot['npcs'].items()}
    w.npc_counter = snapshot.get('npc_counter', 0)
    if 'treaties' in snapshot:
        from sim.provincial.treaty import TreatyRecord
        w.treaties = {frozenset(entry['parties_key']): TreatyRecord.from_dict(entry['record'])
                       for entry in snapshot['treaties']}

    # ─── Schema migration #2 registries ──────────────────────────────────
    if 'convictions' in snapshot:
        from sim.personal.conviction import ConvictionState
        w.convictions = {k: ConvictionState.from_dict(v)
                          for k, v in snapshot['convictions'].items()}
    if 'beliefs' in snapshot:
        from sim.personal.beliefs import Belief
        w.beliefs = {k: [Belief.from_dict(b) for b in v]
                      for k, v in snapshot['beliefs'].items()}
    if 'knots' in snapshot:
        from sim.personal.knots import Knot
        w.knots = {k: Knot.from_dict(v) for k, v in snapshot['knots'].items()}
    w.knot_id_counter = snapshot.get('knot_id_counter', 0)
    if 'territory_infrastructure' in snapshot:
        from sim.territory.infrastructure import InfrastructureState
        w.territory_infrastructure = {k: InfrastructureState.from_dict(v)
                                       for k, v in snapshot['territory_infrastructure'].items()}
    if 'npc_drift_state' in snapshot:
        w.npc_drift_state = dict(snapshot['npc_drift_state'])
    if 'threadcut_beings' in snapshot:
        from sim.thread.threadcut import ThreadcutState
        w.threadcut_beings = {k: ThreadcutState.from_dict(v)
                               for k, v in snapshot['threadcut_beings'].items()}
    if 'comovement_deck' in snapshot:
        # Restore tuples from saved lists (matches CO_MOVEMENT_CARDS shape)
        w.comovement_deck = {
            'remaining': [tuple(c) for c in snapshot['comovement_deck'].get('remaining', [])],
            'discard': [tuple(c) for c in snapshot['comovement_deck'].get('discard', [])],
        }

    return w
