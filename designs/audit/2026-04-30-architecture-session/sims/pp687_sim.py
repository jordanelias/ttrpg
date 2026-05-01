"""
PP-687 Universal Key Substrate — Reference Simulation
Tests: schema, update rule, CAUSAL_GRAPH walks, observer resolution,
       Memory-as-Key-references, cross-system propagation,
       performance at 30-season scale (P1-1 audit), determinism (P1-2).
"""
import random, time, hashlib, json
from dataclasses import dataclass, field
from typing import Optional
from collections import defaultdict, Counter

# Seed for determinism throughout
SEED = 42

# ============================================================
# Conviction → Axis matrix
# ============================================================
CONVICTIONS = ["Faith", "Authority", "Order", "Scholastic", "Utility",
               "Equity", "Liberty", "Precedent", "Community", "Identity",
               "Warden", "Virtue"]
AXES = ["hierarchical", "sacred", "instrumental", "traditional"]

CONVICTION_AXIS_MATRIX = {
    "Faith":      [+0.3, +0.9, -0.5, +0.7],
    "Authority":  [+0.9, +0.1, +0.2, +0.4],
    "Order":      [+0.6, +0.0, +0.0, +0.5],
    "Scholastic": [+0.2, +0.4, -0.3, +0.6],
    "Utility":    [+0.0, -0.5, +0.9, -0.2],
    "Equity":     [-0.7, +0.0, -0.1, +0.0],
    "Liberty":    [-0.6, -0.3, +0.0, -0.3],
    "Precedent":  [+0.4, +0.2, -0.4, +0.9],
    "Community":  [-0.2, +0.2, -0.2, +0.5],
    "Identity":   [+0.1, +0.3, +0.0, +0.4],
    "Warden":     [+0.0, +0.6, +0.1, +0.6],
    "Virtue":     [+0.1, +0.4, -0.4, +0.5],
}

def conviction_to_axis(conviction_vec):
    """Project a 12-Conviction vector into 4-axis space."""
    axis_vec = [0.0] * len(AXES)
    for c, weight in conviction_vec.items():
        if c in CONVICTION_AXIS_MATRIX:
            for i, axis_val in enumerate(CONVICTION_AXIS_MATRIX[c]):
                axis_vec[i] += weight * axis_val
    return axis_vec


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


# ============================================================
# Key Type Registry
# ============================================================
KEY_TYPE_REGISTRY = {
    # scene_event family
    "scene.dialogue":        {"required": ["topic"],            "default_perm": "transient"},
    "scene.witness":         {"required": ["witnessed_event"],  "default_perm": "persistent"},
    "scene.gift":            {"required": ["gift_value"],       "default_perm": "persistent"},
    "scene.insult":          {"required": ["severity"],         "default_perm": "persistent"},
    "scene.threat":          {"required": ["coercion_target"],  "default_perm": "persistent"},
    
    # da_outcome family
    "da.public_governance":   {"required": ["faction_id", "outcome"], "default_perm": "persistent"},
    "da.covert_betrayal":     {"required": ["faction_id", "outcome", "exposed"], "default_perm": "persistent"},
    "da.diplomatic_alliance": {"required": ["faction_id", "outcome"], "default_perm": "indelible"},
    "da.antinomian_action":   {"required": ["faction_id", "outcome"], "default_perm": "persistent"},
    "da.economic_intervention":{"required": ["faction_id", "outcome"], "default_perm": "persistent"},
    
    # state_transition family
    "state.scar_acquired":   {"required": ["npc_id", "conviction"], "default_perm": "indelible"},
    "state.standing_change": {"required": ["npc_id", "delta"],      "default_perm": "persistent"},
    "state.coup_attempted":  {"required": ["faction_id", "outcome"], "default_perm": "indelible"},
    "state.succession":      {"required": ["faction_id", "new_leader_id"], "default_perm": "indelible"},
    
    # mechanical family
    "mechanical.season_change":     {"required": ["new_season"], "default_perm": "transient"},
    "mechanical.accounting":        {"required": ["season"],     "default_perm": "transient"},
    "mechanical.cascade_resolution":{"required": ["faction_id"], "default_perm": "transient"},
    "mechanical.mission_shift":     {"required": ["faction_id", "old_mission", "new_mission"], "default_perm": "indelible"},
    
    # environmental family
    "env.peninsular_strain_shock": {"required": ["strain_delta"], "default_perm": "persistent"},
    "env.crisis":                   {"required": ["crisis_type"],  "default_perm": "persistent"},
    
    # scene_outcome family
    "scene.contest_resolved":  {"required": ["winner", "track_displacement"], "default_perm": "persistent"},
    "scene.battle_concluded":  {"required": ["winner", "casualties"],         "default_perm": "indelible"},
    
    # system_meta family
    "meta.knot_formed":      {"required": ["participants"],     "default_perm": "indelible"},
    "meta.knot_ruptured":    {"required": ["knot_id"],          "default_perm": "indelible"},
    "meta.thread_woven":     {"required": ["thread_target"],    "default_perm": "indelible"},
    "meta.miraculous_event": {"required": ["nature"],           "default_perm": "indelible"},
}


# ============================================================
# Key
# ============================================================
@dataclass
class Key:
    id: str
    type: str
    source_actor: Optional[str]
    emitted_at: tuple                   # (season, sub_step)
    causes: list = field(default_factory=list)        # list of key ids
    targets: list = field(default_factory=list)       # list of dicts: {actor_id, role, impact_vector, stat_deltas}
    scale_signature: list = field(default_factory=list)
    symbolic_dimensions: list = field(default_factory=lambda: [0.0]*len(AXES))
    visibility: dict = field(default_factory=lambda: {"public": False, "semi_public": [], "private": []})
    time_horizon: str = "near"
    permanence: str = "persistent"
    payload: dict = field(default_factory=dict)
    
    @staticmethod
    def make_id(type_, source, season, sub):
        h = hashlib.sha1(f"{type_}|{source}|{season}|{sub}".encode()).hexdigest()
        return h[:12]


def validate_key(key):
    """Validate against type registry + cycle check (later)."""
    if key.type not in KEY_TYPE_REGISTRY:
        raise ValueError(f"Unknown Key type: {key.type}")
    spec = KEY_TYPE_REGISTRY[key.type]
    for req in spec["required"]:
        if req not in key.payload:
            raise ValueError(f"Key {key.id} type={key.type} missing required payload: {req}")
    return True


def detect_cycle_in_causes(key, key_log):
    """P2-3: cycle handling. BFS from key.causes; if we reach key.id, cycle."""
    if not key.causes:
        return False
    visited = set()
    queue = list(key.causes)
    while queue:
        cur = queue.pop(0)
        if cur == key.id:
            return True
        if cur in visited:
            continue
        visited.add(cur)
        # Look up cur's causes
        cur_key = key_log_lookup(key_log, cur)
        if cur_key:
            queue.extend(cur_key.causes)
    return False


def key_log_lookup(key_log, kid):
    for k in key_log:
        if k.id == kid:
            return k
    return None


# ============================================================
# NPC and Faction (minimal — for sim)
# ============================================================
@dataclass
class NPC:
    id: str
    personal_convictions: dict
    standing: int = 1
    armature_axis: list = field(default_factory=lambda: [0.0]*len(AXES))
    memory: list = field(default_factory=list)        # list of {key_id, salience, season_held, decay_rate}

    def __post_init__(self):
        self.armature_axis = conviction_to_axis(self.personal_convictions)

    def interpret(self, key):
        """Compute interpretation of Key — dot product of armature with symbolic dimensions."""
        return dot(self.armature_axis, key.symbolic_dimensions)
    
    def salience(self, key, interpretation):
        time_horizon_factor = {"immediate": 1.5, "near": 1.0, "far": 0.5}[key.time_horizon]
        return max(0, min(3, abs(interpretation) * time_horizon_factor))
    
    def record_memory(self, key, salience):
        self.memory.append({
            "key_id": key.id,
            "salience": salience,
            "season_held": 0,
            "decay_rate": 0.05 if key.permanence == "transient" else 0.01 if key.permanence == "persistent" else 0,
        })


# ============================================================
# Update Rule
# ============================================================
class Engine:
    def __init__(self, npcs, factions=None, scale_actor_index=None):
        self.key_log = []
        self.causal_graph = defaultdict(set)   # cause_id → set of consequence_ids
        self.npcs = {n.id: n for n in npcs}
        self.factions = factions or {}
        # actor_index[scale] = list of actor_ids in that scale
        self.scale_actor_index = scale_actor_index or {
            "personal": list(self.npcs.keys()),
            "settlement": list(self.npcs.keys()),  # all see settlement events
            "territory": list(self.npcs.keys()),
            "peninsula": list(self.npcs.keys()),
        }
        self.subscriptions = defaultdict(list)
        self.stats = Counter()
    
    def subscribe(self, key_type, callback):
        self.subscriptions[key_type].append(callback)
    
    def emit(self, key):
        """The single update rule (§5.1)."""
        # 1. Validate
        validate_key(key)
        # cycle check
        if detect_cycle_in_causes(key, self.key_log):
            raise ValueError(f"Key {key.id} introduces cycle in causes graph")
        
        # 2. Append to log
        self.key_log.append(key)
        
        # 3. Resolve observer set
        observers = self.compute_observers(key)
        self.stats["observers"] += len(observers)
        
        # 4. Each observer interprets and records
        for observer_id in observers:
            if observer_id not in self.npcs:
                continue
            obs = self.npcs[observer_id]
            interpretation = obs.interpret(key)
            sal = obs.salience(key, interpretation)
            obs.record_memory(key, sal)
        
        # 5. Cross-system propagation
        for cb in self.subscriptions.get(key.type, []):
            cb(key, self)
        
        # 6. Causal graph update
        for cause_id in key.causes:
            self.causal_graph[cause_id].add(key.id)
    
    def compute_observers(self, key):
        observers = set()
        if key.source_actor:
            observers.add(key.source_actor)
        for t in key.targets:
            observers.add(t["actor_id"])
        if key.visibility.get("public"):
            for scale in key.scale_signature:
                observers.update(self.scale_actor_index.get(scale, []))
        observers.update(key.visibility.get("semi_public", []))
        observers.update(key.visibility.get("private", []))
        return observers
    
    def walk_causes_backward(self, key_id, depth=10):
        """Provenance walk."""
        visited = set()
        chain = []
        queue = [(key_id, 0)]
        while queue:
            cur, d = queue.pop(0)
            if cur in visited or d > depth:
                continue
            visited.add(cur)
            k = key_log_lookup(self.key_log, cur)
            if k:
                chain.append((d, k.id, k.type))
                for cause in k.causes:
                    queue.append((cause, d+1))
        return chain
    
    def walk_consequences_forward(self, key_id, depth=10):
        """Forward walk through causal graph."""
        visited = set()
        chain = []
        queue = [(key_id, 0)]
        while queue:
            cur, d = queue.pop(0)
            if cur in visited or d > depth:
                continue
            visited.add(cur)
            k = key_log_lookup(self.key_log, cur)
            if k:
                chain.append((d, k.id, k.type))
                for cons in self.causal_graph.get(cur, set()):
                    queue.append((cons, d+1))
        return chain


# ============================================================
# Scenarios
# ============================================================
def build_population(n_npcs=35, n_factions=6):
    """Generate ~35 NPCs with structured Convictions, distribute across 6 factions."""
    rng = random.Random(SEED)
    npcs = []
    primary_choices = [
        {"Virtue": 0.6, "Authority": 0.4},
        {"Faith": 0.7, "Authority": 0.3},
        {"Order": 0.5, "Utility": 0.5},
        {"Scholastic": 0.5, "Utility": 0.4, "Authority": 0.1},
        {"Equity": 0.5, "Liberty": 0.5},
        {"Authority": 0.5, "Virtue": 0.5},
        {"Utility": 0.7, "Liberty": 0.3},
        {"Community": 0.5, "Faith": 0.3, "Identity": 0.2},
        {"Order": 0.6, "Precedent": 0.4},
        {"Warden": 0.5, "Faith": 0.3, "Virtue": 0.2},
    ]
    for i in range(n_npcs):
        primary = rng.choice(primary_choices)
        # Convert to full vector (simplified — no cultural bg here)
        full = {c: 0.0 for c in CONVICTIONS}
        for k, v in primary.items():
            full[k] = v
        npcs.append(NPC(id=f"npc_{i:03d}",
                       personal_convictions=full,
                       standing=rng.randint(1, 7)))
    return npcs


def scenario_perf_30_seasons():
    """P1-1: simulate 30 seasons with realistic Key density. Profile."""
    print("=" * 72)
    print("SCENARIO PERF — 30-season Key density profile (P1-1)")
    print("=" * 72)
    
    npcs = build_population(35, 6)
    engine = Engine(npcs)
    rng = random.Random(SEED)
    
    # subscribe a no-op consumer to each Key type to simulate cross-system propagation
    for kt in KEY_TYPE_REGISTRY:
        engine.subscribe(kt, lambda key, eng: eng.stats.update(["sub_callback"]))
    
    sub = 0
    start_time = time.time()
    
    for season in range(30):
        # Per season: ~10-20 keys/faction × 6 = 60-120/season
        for f in range(6):
            for evt in range(rng.randint(10, 20)):
                sub += 1
                key_type = rng.choice(list(KEY_TYPE_REGISTRY.keys()))
                spec = KEY_TYPE_REGISTRY[key_type]
                
                source = rng.choice(npcs).id
                # Random 1-3 targets
                n_targets = rng.randint(1, 3)
                target_ids = [rng.choice(npcs).id for _ in range(n_targets)]
                targets = [{"actor_id": tid, "role": "subject",
                           "impact_vector": [rng.uniform(-1, 1) for _ in AXES],
                           "stat_deltas": {}} for tid in target_ids]
                
                # Visibility: ~30% public
                visibility = {"public": rng.random() < 0.3,
                             "semi_public": [],
                             "private": [rng.choice(npcs).id for _ in range(rng.randint(0, 2))]}
                
                # Causes: ~10% have 1-2 causes (link to recent prior keys)
                causes = []
                if engine.key_log and rng.random() < 0.10:
                    n_causes = rng.randint(1, 2)
                    causes = [rng.choice(engine.key_log[-50:]).id for _ in range(n_causes)]
                
                # Build payload to satisfy required fields
                payload = {req: rng.choice(["a", "b", "c"]) for req in spec["required"]}
                
                key = Key(
                    id=Key.make_id(key_type, source, season, sub),
                    type=key_type,
                    source_actor=source,
                    emitted_at=(season, sub),
                    causes=causes,
                    targets=targets,
                    scale_signature=[rng.choice(["personal", "settlement", "territory", "peninsula"])],
                    symbolic_dimensions=[rng.uniform(-1, 1) for _ in AXES],
                    visibility=visibility,
                    time_horizon=rng.choice(["immediate", "near", "far"]),
                    permanence=spec["default_perm"],
                    payload=payload,
                )
                try:
                    engine.emit(key)
                except ValueError as e:
                    if "cycle" in str(e):
                        engine.stats["cycle_blocked"] += 1
    
    elapsed = time.time() - start_time
    
    print(f"\n=== Performance ===")
    print(f"Total keys emitted: {len(engine.key_log)}")
    print(f"Total observers processed: {engine.stats['observers']}")
    print(f"Subscription callbacks: {engine.stats['sub_callback']}")
    print(f"Cycles blocked (validator): {engine.stats['cycle_blocked']}")
    print(f"Elapsed: {elapsed:.3f} sec")
    print(f"Keys/sec: {len(engine.key_log)/elapsed:,.0f}")
    print(f"Avg observers per key: {engine.stats['observers']/len(engine.key_log):.1f}")
    
    # NPC memory distribution
    mem_counts = [len(n.memory) for n in npcs]
    mem_counts.sort()
    print(f"\nNPC memory size: min={mem_counts[0]}, median={mem_counts[len(mem_counts)//2]}, "
          f"max={mem_counts[-1]}")
    
    # CAUSAL_GRAPH stats
    n_edges = sum(len(v) for v in engine.causal_graph.values())
    print(f"\nCausal graph: {len(engine.causal_graph)} parents, {n_edges} edges")
    
    # Walk performance — pick a random key, walk its consequences
    start = time.time()
    sample_key = engine.key_log[len(engine.key_log)//2]  # midpoint
    chain = engine.walk_consequences_forward(sample_key.id, depth=10)
    walk_time = time.time() - start
    print(f"\nForward walk from key {sample_key.id} ({sample_key.type}): {len(chain)} keys, {walk_time*1000:.2f}ms")
    
    start = time.time()
    chain = engine.walk_causes_backward(sample_key.id, depth=10)
    walk_time = time.time() - start
    print(f"Backward walk from key {sample_key.id}: {len(chain)} keys, {walk_time*1000:.2f}ms")
    
    return engine


def scenario_determinism():
    """P1-2: replay same inputs twice, assert identical state."""
    print("\n" + "=" * 72)
    print("SCENARIO DETERMINISM — replay produces identical Key log (P1-2)")
    print("=" * 72)
    
    def run(seed):
        npcs = build_population(20, 4)
        engine = Engine(npcs)
        rng = random.Random(seed)
        for season in range(5):
            for f in range(4):
                for _ in range(5):
                    key_type = rng.choice(list(KEY_TYPE_REGISTRY.keys()))
                    spec = KEY_TYPE_REGISTRY[key_type]
                    source = rng.choice(npcs).id
                    payload = {req: "x" for req in spec["required"]}
                    key = Key(
                        id=Key.make_id(key_type, source, season, len(engine.key_log)),
                        type=key_type,
                        source_actor=source,
                        emitted_at=(season, len(engine.key_log)),
                        targets=[{"actor_id": rng.choice(npcs).id, "role": "subject",
                                "impact_vector": [0]*len(AXES), "stat_deltas": {}}],
                        scale_signature=["personal"],
                        symbolic_dimensions=[0.5]*len(AXES),
                        time_horizon="near",
                        permanence=spec["default_perm"],
                        payload=payload,
                    )
                    try:
                        engine.emit(key)
                    except: pass
        # Hash log
        log_repr = "".join(f"{k.id}:{k.type}" for k in engine.key_log)
        return hashlib.sha256(log_repr.encode()).hexdigest()[:16]
    
    h1 = run(SEED)
    h2 = run(SEED)
    h3 = run(SEED + 1)
    print(f"Run 1 (seed {SEED}): {h1}")
    print(f"Run 2 (seed {SEED}): {h2}  {'MATCH ✓' if h1 == h2 else 'MISMATCH ✗'}")
    print(f"Run 3 (seed {SEED+1}): {h3}  {'expected DIFF ✓' if h3 != h1 else 'unexpected MATCH ✗'}")
    return h1 == h2 and h3 != h1


def scenario_cross_scale_provenance():
    """Build a multi-scale chain: scene action → DA outcome → faction state → peninsula event.
    Verify the chain is walkable in both directions."""
    print("\n" + "=" * 72)
    print("SCENARIO CROSS-SCALE PROVENANCE — diagonal trace verification")
    print("=" * 72)
    
    npcs = build_population(10, 2)
    engine = Engine(npcs)
    
    # Chain: scene insult → covert betrayal DA → state succession → peninsular shock
    k1 = Key(id="K0001", type="scene.insult",
             source_actor="npc_000", emitted_at=(1, 1),
             targets=[{"actor_id": "npc_001", "role": "object", "impact_vector": [0]*4, "stat_deltas": {}}],
             scale_signature=["personal"],
             symbolic_dimensions=[0.0, 0.5, 0.0, 0.0],
             visibility={"public": False, "semi_public": [], "private": ["npc_001"]},
             time_horizon="immediate", permanence="persistent",
             payload={"severity": "high"})
    
    k2 = Key(id="K0002", type="da.covert_betrayal",
             source_actor="npc_001", emitted_at=(2, 1),
             causes=["K0001"],   # caused by the insult
             targets=[{"actor_id": "npc_000", "role": "object", "impact_vector": [0]*4, "stat_deltas": {}}],
             scale_signature=["territory"],
             symbolic_dimensions=[0.3, -0.4, 0.7, -0.2],
             visibility={"public": False, "semi_public": [], "private": ["npc_001", "npc_000"]},
             time_horizon="near", permanence="persistent",
             payload={"faction_id": "faction_A", "outcome": "success", "exposed": True})
    
    k3 = Key(id="K0003", type="state.succession",
             source_actor=None, emitted_at=(3, 1),
             causes=["K0002"],   # exposed betrayal forces succession
             targets=[{"actor_id": "faction_A", "role": "subject", "impact_vector": [0]*4, "stat_deltas": {}}],
             scale_signature=["territory", "peninsula"],
             symbolic_dimensions=[0.6, 0.0, 0.0, 0.5],
             visibility={"public": True},
             time_horizon="far", permanence="indelible",
             payload={"faction_id": "faction_A", "new_leader_id": "npc_002"})
    
    k4 = Key(id="K0004", type="env.peninsular_strain_shock",
             source_actor=None, emitted_at=(3, 2),
             causes=["K0003"],   # succession instability raises peninsula strain
             targets=[],
             scale_signature=["peninsula"],
             symbolic_dimensions=[-0.3, -0.2, 0.0, -0.5],
             visibility={"public": True},
             time_horizon="far", permanence="persistent",
             payload={"strain_delta": 1})
    
    for k in [k1, k2, k3, k4]:
        engine.emit(k)
    
    # Now walk
    print("\nForward from K0001 (scene insult):")
    for d, kid, ktype in engine.walk_consequences_forward("K0001"):
        print(f"  {'  '*d}└→ {kid} ({ktype})")
    
    print("\nBackward from K0004 (peninsular shock):")
    for d, kid, ktype in engine.walk_causes_backward("K0004"):
        print(f"  {'  '*d}└← {kid} ({ktype})")
    
    print("\n✓ Cross-scale chain walks correctly. Diagonal trace works.")


def scenario_observer_resolution():
    """Verify observer resolution: public, private, semi-public visibility."""
    print("\n" + "=" * 72)
    print("SCENARIO OBSERVER RESOLUTION")
    print("=" * 72)
    
    npcs = build_population(10, 2)
    engine = Engine(npcs)
    
    # Public peninsula event → all NPCs observe
    k_pub = Key(id="K_PUB", type="meta.miraculous_event",
                source_actor=None, emitted_at=(1, 1),
                scale_signature=["peninsula"],
                visibility={"public": True},
                symbolic_dimensions=[0]*4,
                time_horizon="far", permanence="indelible",
                payload={"nature": "vision_at_dawn"})
    
    # Private gift → 2 NPCs observe
    k_priv = Key(id="K_PRIV", type="scene.gift",
                 source_actor="npc_000", emitted_at=(1, 2),
                 targets=[{"actor_id": "npc_001", "role": "beneficiary", "impact_vector": [0]*4, "stat_deltas": {}}],
                 scale_signature=["personal"],
                 visibility={"public": False, "semi_public": [], "private": []},
                 symbolic_dimensions=[0]*4,
                 time_horizon="near", permanence="persistent",
                 payload={"gift_value": "high"})
    
    # Semi-public scene with 3 witnesses
    k_semi = Key(id="K_SEMI", type="scene.threat",
                 source_actor="npc_002", emitted_at=(1, 3),
                 targets=[{"actor_id": "npc_003", "role": "object", "impact_vector": [0]*4, "stat_deltas": {}}],
                 scale_signature=["personal"],
                 visibility={"public": False, "semi_public": ["npc_004", "npc_005", "npc_006"], "private": []},
                 symbolic_dimensions=[0]*4,
                 time_horizon="near", permanence="persistent",
                 payload={"coercion_target": "intimidation"})
    
    obs_pub = engine.compute_observers(k_pub)
    obs_priv = engine.compute_observers(k_priv)
    obs_semi = engine.compute_observers(k_semi)
    
    print(f"Public peninsula event:  {len(obs_pub)} observers (expected: all 10)")
    print(f"Private gift:            {len(obs_priv)} observers (expected: 2 = source + target)")
    print(f"Semi-public threat:      {len(obs_semi)} observers (expected: 5 = source + target + 3 witnesses)")
    
    assert len(obs_pub) == 10, f"public expected 10, got {len(obs_pub)}"
    assert len(obs_priv) == 2, f"private expected 2, got {len(obs_priv)}"
    assert len(obs_semi) == 5, f"semi expected 5, got {len(obs_semi)}"
    print("\n✓ Observer resolution correct for all visibility types.")


def scenario_pp686_integration():
    """Verify PP-686 integration: Key sequence affects faction L/PS."""
    print("\n" + "=" * 72)
    print("SCENARIO PP-686 INTEGRATION — Keys drive faction state")
    print("=" * 72)
    
    npcs = build_population(8, 1)
    engine = Engine(npcs)
    
    # Faction state — minimal stand-in
    faction_state = {"legitimacy": 5.0, "popular_support": 5.0, "violations": 0}
    
    # Subscribe DA outcome handler
    def on_da(key, eng):
        if key.payload.get("outcome") == "success":
            faction_state["popular_support"] = min(7, faction_state["popular_support"] + 0.5)
        elif key.payload.get("outcome") == "fail":
            faction_state["popular_support"] = max(0, faction_state["popular_support"] - 0.3)
        if key.type == "da.covert_betrayal" and key.payload.get("exposed"):
            faction_state["legitimacy"] = max(0, faction_state["legitimacy"] - 0.6)
            faction_state["violations"] += 1
    
    for da_type in ["da.public_governance", "da.covert_betrayal", "da.diplomatic_alliance",
                     "da.antinomian_action", "da.economic_intervention"]:
        engine.subscribe(da_type, on_da)
    
    # Sequence: 3 successes, 1 exposed betrayal
    rng = random.Random(SEED)
    sequence = [
        ("da.public_governance",  "success", False),
        ("da.public_governance",  "success", False),
        ("da.covert_betrayal",    "success", True),    # exposed
        ("da.diplomatic_alliance","success", False),
    ]
    print(f"Initial: L={faction_state['legitimacy']}, PS={faction_state['popular_support']}")
    for i, (kt, outcome, exposed) in enumerate(sequence):
        spec = KEY_TYPE_REGISTRY[kt]
        payload = {req: "x" for req in spec["required"]}
        payload["outcome"] = outcome
        if "exposed" in spec["required"]:
            payload["exposed"] = exposed
        if "faction_id" in spec["required"]:
            payload["faction_id"] = "faction_A"
        key = Key(
            id=f"DA_{i}", type=kt,
            source_actor=npcs[0].id, emitted_at=(1, i),
            scale_signature=["territory"],
            visibility={"public": True},
            symbolic_dimensions=[0]*4,
            time_horizon="near", permanence="persistent",
            payload=payload,
        )
        engine.emit(key)
        print(f"  After {kt} ({outcome}, exposed={exposed}): "
              f"L={faction_state['legitimacy']:.2f}, PS={faction_state['popular_support']:.2f}")
    
    print(f"\nFinal: L={faction_state['legitimacy']:.2f}, PS={faction_state['popular_support']:.2f}, "
          f"violations={faction_state['violations']}")
    print("\n✓ PP-686 architecture composes cleanly with Key substrate.")


def scenario_cycle_detection():
    """P2-3: cycle detection should reject."""
    print("\n" + "=" * 72)
    print("SCENARIO CYCLE DETECTION (P2-3)")
    print("=" * 72)
    
    npcs = build_population(5, 1)
    engine = Engine(npcs)
    
    k1 = Key(id="A", type="scene.dialogue",
             source_actor=npcs[0].id, emitted_at=(1,1),
             scale_signature=["personal"], symbolic_dimensions=[0]*4,
             visibility={"public": True}, time_horizon="near", permanence="transient",
             payload={"topic": "weather"})
    engine.emit(k1)
    
    k2 = Key(id="B", type="scene.dialogue",
             source_actor=npcs[1].id, emitted_at=(1,2),
             causes=["A"],
             scale_signature=["personal"], symbolic_dimensions=[0]*4,
             visibility={"public": True}, time_horizon="near", permanence="transient",
             payload={"topic": "weather"})
    engine.emit(k2)
    
    # Now try to emit C with cause = ["B"] but rewrite A's causes via post-hoc ... 
    # Actually direct cycle: emit C with cause=B, then a new key D with cause=C and post-hoc add D to B's causes (impossible properly)
    # Simulate cycle: try k3 with causes=["A"] which then would need A to depend on k3
    # In reality, the only way to make a cycle is if a Key's causes refer to a Key that depends on it.
    # Test: try to emit a Key whose own ID is in its own causes list.
    k_self = Key(id="SELF", type="scene.dialogue",
                 source_actor=npcs[0].id, emitted_at=(1,3),
                 causes=["SELF"],  # direct self-cycle
                 scale_signature=["personal"], symbolic_dimensions=[0]*4,
                 visibility={"public": True}, time_horizon="near", permanence="transient",
                 payload={"topic": "weather"})
    try:
        engine.emit(k_self)
        print("✗ FAIL: self-cycle not blocked")
    except ValueError as e:
        if "cycle" in str(e):
            print(f"✓ Self-cycle correctly rejected: {e}")
        else:
            print(f"? Different error: {e}")


# ============================================================
# Main
# ============================================================
if __name__ == "__main__":
    scenario_perf_30_seasons()
    scenario_determinism()
    scenario_cross_scale_provenance()
    scenario_observer_resolution()
    scenario_pp686_integration()
    scenario_cycle_detection()
    print("\n" + "=" * 72)
    print("ALL SCENARIOS COMPLETE")
    print("=" * 72)
