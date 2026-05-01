"""
PP-686 Simulator v2 — Structured-concentration NPCs + Self-Other orientation
+ calibration deltas from v1 evaluation:
  - Ob ±2 cap (was ±3)
  - drift_coef = 0.45 (was 0.3)
  - β-fidelity gating: if outcome negative, β-fid contribution scales 0.5x
  - strictness reward path: low strictness adds bonus to aligned actions
  - orphan NPC rule: alpha=1.0, contribute normally
  - structured-concentration NPCs: primary (1-3 entries, 0.6-0.8) + cultural background (0.2-0.4)
  - Self-Other orientation [-1, +1] modulates outcome attribution
"""
import math, random, json
from dataclasses import dataclass, field
from typing import Optional

random.seed(0)

CONVICTIONS = ["Faith", "Authority", "Order", "Scholastic", "Utility",
               "Equity", "Liberty", "Precedent", "Community", "Identity",
               "Warden", "Virtue"]

# Cultural background templates — fill in background distribution
CULTURAL_BACKGROUNDS = {
    "crown_court_florentine": {
        "Virtue": 0.05, "Authority": 0.04, "Honor": 0.03, "Order": 0.03,
        "Scholastic": 0.03, "Identity": 0.03, "Precedent": 0.02, "Community": 0.02,
        "Faith": 0.02, "Liberty": 0.01, "Utility": 0.01, "Warden": 0.01, "Equity": 0.00,
    },
    "rural_devout_peasant": {
        "Faith": 0.07, "Community": 0.05, "Precedent": 0.04, "Authority": 0.03,
        "Identity": 0.02, "Virtue": 0.02, "Order": 0.02, "Equity": 0.01,
        "Warden": 0.01, "Honor": 0.01, "Liberty": 0.01, "Scholastic": 0.01, "Utility": 0.00,
    },
    "ecclesiastical_curia": {
        "Faith": 0.06, "Scholastic": 0.06, "Authority": 0.04, "Precedent": 0.04,
        "Order": 0.02, "Identity": 0.02, "Community": 0.01, "Virtue": 0.01,
        "Honor": 0.01, "Equity": 0.01, "Warden": 0.01, "Utility": 0.01, "Liberty": 0.00,
    },
    "martial_nobility": {
        "Honor": 0.06, "Authority": 0.04, "Virtue": 0.04, "Identity": 0.03,
        "Order": 0.03, "Liberty": 0.02, "Precedent": 0.02, "Faith": 0.02,
        "Community": 0.01, "Warden": 0.01, "Utility": 0.01, "Scholastic": 0.01, "Equity": 0.00,
    },
    "mercantile_class": {
        "Utility": 0.05, "Order": 0.04, "Liberty": 0.04, "Community": 0.03,
        "Scholastic": 0.03, "Precedent": 0.02, "Identity": 0.02, "Authority": 0.02,
        "Faith": 0.02, "Equity": 0.01, "Honor": 0.01, "Virtue": 0.01, "Warden": 0.00,
    },
}
# Strip Honor (not yet ratified) — fold into Virtue
for k, t in CULTURAL_BACKGROUNDS.items():
    if "Honor" in t:
        t["Virtue"] = t.get("Virtue", 0) + t.pop("Honor")

ROLE_TEMPLATES = {
    "sovereign":             {"Virtue": 0.40, "Authority": 0.40, "Honor": 0.20},
    "ecclesiastical":        {"Faith": 0.50, "Authority": 0.30, "Scholastic": 0.20},
    "mercantile_procedural": {"Order": 0.40, "Utility": 0.30, "Scholastic": 0.30},
    "intelligence":          {"Scholastic": 0.40, "Utility": 0.40, "Authority": 0.20},
    "reformist":             {"Equity": 0.40, "Liberty": 0.30, "Community": 0.30},
    "military_order":        {"Authority": 0.40, "Virtue": 0.30, "Honor": 0.30},
}
def _strip_honor(d):
    if "Honor" in d:
        d["Virtue"] = d.get("Virtue", 0) + d.pop("Honor")
    return d
def _normalize(d):
    s = sum(d.values())
    return {k: v/s for k,v in d.items()} if s>0 else d
ROLE_TEMPLATES = {k: _normalize(_strip_honor(dict(v))) for k,v in ROLE_TEMPLATES.items()}

PUBLIC_TEMPERAMENTS = {
    "pragmatic":     (0.7, 0.3),
    "traditional":   (0.3, 0.7),
    "balanced":      (0.5, 0.5),
    "principled":    (0.2, 0.8),
    "outcomes_only": (0.9, 0.1),
}

def vec_zero():
    return {c: 0.0 for c in CONVICTIONS}

def vec_add(a, b, w_a=1.0, w_b=1.0):
    return {c: w_a * a.get(c, 0) + w_b * b.get(c, 0) for c in CONVICTIONS}

def vec_normalize(v):
    s = sum(v.values())
    return {k: val/s for k, val in v.items()} if s > 0 else vec_zero()

def cosine(a, b):
    dot = sum(a.get(c, 0) * b.get(c, 0) for c in CONVICTIONS)
    na = math.sqrt(sum(a.get(c, 0)**2 for c in CONVICTIONS))
    nb = math.sqrt(sum(b.get(c, 0)**2 for c in CONVICTIONS))
    return dot / (na * nb) if na > 0 and nb > 0 else 0.0


def build_npc_personal(primary, cultural_template_name, target_primary_sum=0.7):
    """Compose NPC's full personal_convictions vector from primary + cultural background.
    primary: dict, e.g. {"Virtue": 0.45, "Authority": 0.30}
    cultural_template_name: key into CULTURAL_BACKGROUNDS
    target_primary_sum: how much weight primary should occupy [0.6, 0.8]
    """
    template = CULTURAL_BACKGROUNDS[cultural_template_name]
    # Normalize primary to target sum
    p_sum = sum(primary.values())
    primary_scaled = {k: v * (target_primary_sum / p_sum) for k, v in primary.items()}
    # Background gets remaining (1 - target_primary_sum), distributed per template
    bg_total = 1 - target_primary_sum
    template_sum = sum(template.values())
    background = {k: v * (bg_total / template_sum) for k, v in template.items()}
    # Sum primary + background
    full = vec_zero()
    for k, v in primary_scaled.items():
        full[k] = full.get(k, 0) + v
    for k, v in background.items():
        full[k] = full.get(k, 0) + v
    return vec_normalize(full)


@dataclass
class NPC:
    id: str
    primary_convictions: dict
    cultural_background: str
    personal_convictions: dict = field(default_factory=vec_zero)
    self_other_orientation: float = 0.0      # [-1 altruism, +1 self]
    standing: int = 1
    supervisor_id: Optional[str] = None
    effective_convictions: dict = field(default_factory=vec_zero)

    def __post_init__(self):
        if not self.personal_convictions or sum(self.personal_convictions.values()) == 0:
            self.personal_convictions = build_npc_personal(
                self.primary_convictions, self.cultural_background)

    def alpha(self, institutional_culture: float) -> float:
        a_base = 0.4
        a_seniority = -0.2 + (0.6 * (self.standing - 1) / 6)
        return max(0.0, min(1.0, a_base + a_seniority + institutional_culture))


@dataclass
class Faction:
    id: str
    role: str
    leader_id: str
    npcs: dict
    institutional_culture: float = 0.0
    legitimacy: float = 4.0
    popular_support: float = 4.0
    territorial_temperaments: list = field(default_factory=lambda: ["balanced"])
    mission_aligned_categories: set = field(default_factory=set)
    mission_contradicted_categories: set = field(default_factory=set)
    drift_coef: float = 0.45                  # CALIBRATION: was 0.3

    def expected_convictions(self):
        return ROLE_TEMPLATES[self.role]

    def temperament_weights(self):
        a_sum = b_sum = 0
        for t in self.territorial_temperaments:
            a, b = PUBLIC_TEMPERAMENTS[t]
            a_sum += a; b_sum += b
        n = len(self.territorial_temperaments)
        return a_sum/n, b_sum/n

    def aggregate_effective(self):
        """Standing-weighted (codified per sim v1 finding P1-2)."""
        agg = vec_zero()
        for npc in self.npcs.values():
            for c, val in npc.effective_convictions.items():
                agg[c] += npc.standing * val
        return vec_normalize(agg)

    def cascade_fidelity(self):
        return cosine(self.aggregate_effective(), self.expected_convictions())

    def strictness(self):
        return max(0.0, min(1.0,
            0.4 + 0.5 * (self.legitimacy / 7) - 0.3 * (self.popular_support / 7)))

    def mandate(self):
        return round(0.5 * self.legitimacy + 0.5 * self.popular_support)


def resolve_cascade(faction: Faction):
    """BFS cascade with orphan rule (CALIBRATION): unresolved supervisor = α=1.0."""
    leader = faction.npcs[faction.leader_id]
    leader.effective_convictions = dict(leader.personal_convictions)
    
    resolved = {leader.id}
    pending = [n for n in faction.npcs.values() if n.id != leader.id]
    
    # Iterate until stable
    safety = 50
    while pending and safety > 0:
        progress = False
        next_pending = []
        for npc in pending:
            sup_id = npc.supervisor_id
            if sup_id and sup_id in faction.npcs and sup_id in resolved:
                # Standard cascade
                sup = faction.npcs[sup_id]
                alpha = npc.alpha(faction.institutional_culture)
                target = vec_add(npc.personal_convictions, sup.effective_convictions,
                                w_a=alpha, w_b=(1-alpha))
                current = npc.effective_convictions
                if sum(current.values()) == 0:
                    npc.effective_convictions = target
                else:
                    npc.effective_convictions = vec_add(current, target,
                        w_a=(1-faction.drift_coef), w_b=faction.drift_coef)
                resolved.add(npc.id)
                progress = True
            elif sup_id is None or sup_id not in faction.npcs:
                # Orphan rule (CALIBRATION): no supervisor or invalid → α=1.0
                npc.effective_convictions = dict(npc.personal_convictions)
                resolved.add(npc.id)
                progress = True
            else:
                next_pending.append(npc)
        pending = next_pending
        safety -= 1
        if not progress:
            # Cycle in hierarchy or dead supervisor — break and use orphan rule
            for npc in pending:
                npc.effective_convictions = dict(npc.personal_convictions)
                resolved.add(npc.id)
            break


def ob_modifier(faction: Faction, da_category: str, da_alignment: dict, verbose=False) -> int:
    """Calibrated per v1 findings: ±2 cap, strictness reward path."""
    if da_category in faction.mission_aligned_categories:
        m_align = -1
    elif da_category in faction.mission_contradicted_categories:
        m_align = +1
    else:
        m_align = 0
    
    c_sim = cosine(faction.aggregate_effective(), da_alignment)
    if c_sim > 0.5:    c_align = -1
    elif c_sim < -0.3: c_align = +1
    else:              c_align = 0
    
    e_sim = cosine(faction.expected_convictions(), da_alignment)
    strictness = faction.strictness()
    raw = 0
    if e_sim < -0.3:   raw = +1
    elif e_sim > 0.5:  raw = -1
    
    # CALIBRATION: strictness reward path
    if raw < 0:  # well-aligned: bonus scales inversely with strictness
        e_align = raw * (0.5 + (1 - strictness))   # low strictness = bigger bonus
    elif raw > 0:  # mis-aligned: penalty scales with strictness
        e_align = raw * (0.5 + strictness)
    else:
        e_align = 0
    
    total = m_align + c_align + e_align
    capped = max(-2, min(2, round(total)))   # CALIBRATION: ±2 cap
    if verbose:
        return capped, dict(m=m_align, c=c_align, e=e_align, c_sim=c_sim, e_sim=e_sim, str=strictness)
    return capped


def update_legitimacy_and_support(faction: Faction, mission_outcome: int,
                                  violation_score: float = 0,
                                  procedural_score: float = 0,
                                  outcome_beneficiary_orientation: float = 0):
    """CALIBRATION: β-fidelity gated by outcome polarity."""
    a, b = faction.temperament_weights()
    fid = faction.cascade_fidelity()
    
    # CALIBRATION: if outcome is negative, β-fid contribution scales 0.5x
    fid_scale = 1.0 if mission_outcome >= 0 else 0.5
    delta_ps = a * mission_outcome + b * fid * 0.5 * fid_scale
    faction.popular_support = max(0, min(7, faction.popular_support + delta_ps))
    
    delta_legit = (
        0.05
        + 0.4 * procedural_score
        + 0.05 * fid
        - 0.6 * violation_score
    )
    faction.legitimacy = max(0, min(7, faction.legitimacy + delta_legit))


# ============================================================
# Crown baseline with structured NPCs + Self-Other
# ============================================================
def build_crown_v2():
    crown = Faction(
        id="crown",
        role="sovereign",
        leader_id="almud",
        npcs={},
        institutional_culture=0.0,
        legitimacy=5.0,
        popular_support=5.0,
        territorial_temperaments=["balanced", "balanced", "traditional"],
        mission_aligned_categories={"public_governance", "diplomatic_alliance"},
        mission_contradicted_categories={"covert_betrayal", "antinomian_action"},
    )
    crown.npcs["almud"] = NPC("almud",
        primary_convictions={"Virtue": 0.6, "Authority": 0.4},
        cultural_background="crown_court_florentine",
        self_other_orientation=0.1, standing=7)
    crown.npcs["chamberlain"] = NPC("chamberlain",
        primary_convictions={"Order": 0.5, "Authority": 0.3, "Virtue": 0.2},
        cultural_background="crown_court_florentine",
        self_other_orientation=0.0, standing=5, supervisor_id="almud")
    crown.npcs["spymaster"] = NPC("spymaster",
        primary_convictions={"Utility": 0.6, "Scholastic": 0.4},
        cultural_background="ecclesiastical_curia",
        self_other_orientation=0.4, standing=5, supervisor_id="almud")  # higher self-orientation
    crown.npcs["captain1"] = NPC("captain1",
        primary_convictions={"Authority": 0.5, "Virtue": 0.5},
        cultural_background="martial_nobility",
        self_other_orientation=-0.1, standing=4, supervisor_id="chamberlain")
    crown.npcs["captain2"] = NPC("captain2",
        primary_convictions={"Order": 0.6, "Utility": 0.4},
        cultural_background="martial_nobility",
        self_other_orientation=0.2, standing=4, supervisor_id="chamberlain")
    crown.npcs["agent1"] = NPC("agent1",
        primary_convictions={"Utility": 0.7, "Liberty": 0.3},
        cultural_background="mercantile_class",
        self_other_orientation=0.5, standing=3, supervisor_id="spymaster")
    crown.npcs["clerk1"] = NPC("clerk1",
        primary_convictions={"Order": 0.4, "Community": 0.4, "Faith": 0.2},
        cultural_background="rural_devout_peasant",
        self_other_orientation=-0.3, standing=2, supervisor_id="captain1")
    crown.npcs["clerk2"] = NPC("clerk2",
        primary_convictions={"Authority": 0.4, "Order": 0.4, "Virtue": 0.2},
        cultural_background="crown_court_florentine",
        self_other_orientation=0.0, standing=2, supervisor_id="captain1")
    return crown


def fmt_vec(v, top_n=4):
    nonzero = [(k, val) for k, val in v.items() if abs(val) > 0.01]
    nonzero.sort(key=lambda x: -x[1])
    return ", ".join(f"{k}:{val:.2f}" for k, val in nonzero[:top_n])


def scenario_1_static_v2():
    print("=" * 72)
    print("SCENARIO 1 — Static parity (v2: structured NPCs)")
    print("=" * 72)
    crown = build_crown_v2()
    resolve_cascade(crown)
    
    print(f"\nLeader Almud:")
    print(f"  primary: {fmt_vec(crown.npcs['almud'].primary_convictions)}")
    print(f"  full personal: {fmt_vec(crown.npcs['almud'].personal_convictions, 6)}")
    print(f"  self_other: {crown.npcs['almud'].self_other_orientation:+.1f}")
    print(f"\nCrown aggregate effective:   {fmt_vec(crown.aggregate_effective(), 6)}")
    print(f"Crown expected (sovereign):  {fmt_vec(crown.expected_convictions(), 6)}")
    print(f"Cascade fidelity:            {crown.cascade_fidelity():.3f}")
    print(f"Strictness:                  {crown.strictness():.2f}")
    print(f"Mandate (derived):           {crown.mandate()}")
    
    das = [
        ("public_governance",  {"Virtue": 0.6, "Authority": 0.4},   "public ceremony"),
        ("covert_betrayal",    {"Utility": 0.7, "Authority": 0.3},  "covert assassination"),
        ("diplomatic_alliance",{"Authority": 0.5, "Order": 0.5},    "treaty signing"),
        ("antinomian_action",  {"Liberty": 0.7, "Utility": 0.3},    "rebellion against laws"),
    ]
    print(f"\n{'DA':<35} {'category':<22} {'Ob':<5} {'(detail: m/c/e/c_sim/e_sim/str)'}")
    for cat, align, desc in das:
        ob, det = ob_modifier(crown, cat, align, verbose=True)
        print(f"  {desc:<33} {cat:<22} {ob:+d}    "
              f"m={det['m']:+d} c={det['c']:+d} e={det['e']:+.2f} | csim={det['c_sim']:.2f} esim={det['e_sim']:.2f} str={det['str']:.2f}")


def scenario_2_succession_v2():
    print("\n" + "=" * 72)
    print("SCENARIO 2 — Succession dynamics (v2: drift_coef=0.45)")
    print("=" * 72)
    
    for successor_name, successor_primary in [
        ("Cesare (Authority+Utility)", {"Authority": 0.5, "Utility": 0.5}),
        ("Lorenzo (Virtue+Scholastic)", {"Virtue": 0.5, "Scholastic": 0.4, "Authority": 0.1}),
    ]:
        print(f"\n--- Successor: {successor_name} ---")
        crown = build_crown_v2()
        resolve_cascade(crown)
        before_fid = crown.cascade_fidelity()
        before_agg = fmt_vec(crown.aggregate_effective(), 4)
        
        # Replace leader
        new_leader = NPC("almud",
            primary_convictions=successor_primary,
            cultural_background="crown_court_florentine",
            self_other_orientation=0.3, standing=7)
        crown.npcs["almud"] = new_leader
        
        for season in range(8):
            resolve_cascade(crown)
            agg = crown.aggregate_effective()
            fid = crown.cascade_fidelity()
            print(f"  S{season+1}: agg={fmt_vec(agg, 4)} | fid={fid:.3f}")
        
        print(f"  Before: {before_agg} (fid {before_fid:.3f})")
        print(f"  After 8: {fmt_vec(crown.aggregate_effective(), 4)} (fid {crown.cascade_fidelity():.3f})")


def scenario_3_crisis_v2():
    print("\n" + "=" * 72)
    print("SCENARIO 3 — Conviction crisis (v2: tests if drift=0.45 reveals instability)")
    print("=" * 72)
    crown = build_crown_v2()
    resolve_cascade(crown)
    print(f"Initial fidelity: {crown.cascade_fidelity():.3f}")
    
    crisis_states = [
        {"Virtue": 0.6, "Authority": 0.4},
        {"Authority": 0.7, "Virtue": 0.3},
        {"Liberty": 0.8, "Utility": 0.2},
        {"Identity": 0.6, "Community": 0.4},
    ]
    rng = random.Random(42)
    fidelities = []
    print("8 seasons leader oscillating personal_convictions:")
    for season in range(8):
        new_primary = rng.choice(crisis_states)
        crown.npcs["almud"].primary_convictions = new_primary
        crown.npcs["almud"].personal_convictions = build_npc_personal(
            new_primary, crown.npcs["almud"].cultural_background)
        resolve_cascade(crown)
        f = crown.cascade_fidelity()
        fidelities.append(f)
        print(f"  S{season+1}: leader={fmt_vec(new_primary,2)} | "
              f"agg={fmt_vec(crown.aggregate_effective(), 3)} | fid={f:.3f}")
    
    mean = sum(fidelities)/len(fidelities)
    var = sum((f-mean)**2 for f in fidelities)/len(fidelities)
    print(f"\nFidelity variance: {var:.4f}  (compared to v1: 0.0074)")


def scenario_4_oscillation_v2():
    print("\n" + "=" * 72)
    print("SCENARIO 4 — Strictness feedback (v2: ±2 cap, β-gating)")
    print("=" * 72)
    crown = build_crown_v2()
    resolve_cascade(crown)
    
    sequence = [
        ("covert_betrayal", {"Utility": 0.7, "Authority": 0.3}, "succeed"),
        ("public_governance", {"Virtue": 0.6, "Authority": 0.4}, "succeed"),
        ("covert_betrayal", {"Utility": 0.7, "Authority": 0.3}, "fail"),
        ("public_governance", {"Virtue": 0.6, "Authority": 0.4}, "succeed"),
        ("covert_betrayal", {"Utility": 0.7, "Authority": 0.3}, "succeed"),
        ("antinomian_action", {"Liberty": 0.7, "Utility": 0.3}, "fail"),
        ("public_governance", {"Virtue": 0.6, "Authority": 0.4}, "succeed"),
        ("public_governance", {"Virtue": 0.6, "Authority": 0.4}, "succeed"),
    ]
    print(f"{'S':<3}{'DA':<22}{'Ob':<5}{'Out':<6}{'L':<6}{'PS':<6}{'Str':<6}")
    for i, (cat, align, outcome) in enumerate(sequence):
        ob = ob_modifier(crown, cat, align)
        if outcome == "succeed":
            mo = +1 if cat in ("public_governance", "diplomatic_alliance") else 0
            vs = 0
        else:
            mo = -1
            vs = 1 if cat == "covert_betrayal" else 0.5
        update_legitimacy_and_support(crown, mo, vs, 0)
        print(f"{i+1:<3}{cat:<22}{ob:+2d}   {outcome:<6}"
              f"{crown.legitimacy:<6.2f}{crown.popular_support:<6.2f}{crown.strictness():<6.2f}")
    print(f"\nFinal: L={crown.legitimacy:.2f}, PS={crown.popular_support:.2f}, "
          f"Mandate={crown.mandate()}")


def scenario_5_honest_defeat_v2():
    print("\n" + "=" * 72)
    print("SCENARIO 5 — Honest defeat (v2: β-gating should reduce PS bleed asymmetry)")
    print("=" * 72)
    crown = build_crown_v2()
    crown.territorial_temperaments = ["traditional", "traditional", "balanced"]
    resolve_cascade(crown)
    print(f"Initial: L={crown.legitimacy}, PS={crown.popular_support}, fid={crown.cascade_fidelity():.3f}")
    
    history = []
    for season in range(8):
        update_legitimacy_and_support(crown, mission_outcome=-1, violation_score=0)
        history.append((crown.legitimacy, crown.popular_support))
        print(f"  S{season+1}: L={crown.legitimacy:.2f}, PS={crown.popular_support:.2f}, M={crown.mandate()}")
    print(f"\nNet ΔL: {history[-1][0]-5.0:+.2f}, ΔPS: {history[-1][1]-5.0:+.2f}")
    print("v1 result: ΔL +0.76, ΔPS -0.63")


def scenario_6_tyrant_v2():
    print("\n" + "=" * 72)
    print("SCENARIO 6 — Successful tyrant (v2)")
    print("=" * 72)
    crown = build_crown_v2()
    crown.territorial_temperaments = ["pragmatic", "pragmatic", "outcomes_only"]
    cesare = NPC("almud",
        primary_convictions={"Authority": 0.5, "Utility": 0.5},
        cultural_background="crown_court_florentine",
        self_other_orientation=0.8, standing=7)
    crown.npcs["almud"] = cesare
    resolve_cascade(crown)
    print(f"Initial (Cesare just took over): L={crown.legitimacy}, PS={crown.popular_support}, "
          f"fid={crown.cascade_fidelity():.3f}, self_other={cesare.self_other_orientation:+.1f}")
    
    for season in range(8):
        update_legitimacy_and_support(crown, mission_outcome=+1, violation_score=0.3)
        print(f"  S{season+1}: L={crown.legitimacy:.2f}, PS={crown.popular_support:.2f}, "
              f"M={crown.mandate()}, fid={crown.cascade_fidelity():.3f}")
    print(f"\nL-PS divergence: {abs(crown.legitimacy - crown.popular_support):.2f}")
    print("v1 result: divergence 2.83")


def scenario_7_edge_v2():
    print("\n" + "=" * 72)
    print("SCENARIO 7 — Edge cases (v2: orphan rule applied)")
    print("=" * 72)
    
    # Orphan with new rule
    crown = build_crown_v2()
    orphan = NPC("orphan",
        primary_convictions={"Liberty": 0.8, "Utility": 0.2},
        cultural_background="mercantile_class",
        self_other_orientation=0.0, standing=3,
        supervisor_id="ghost_id_does_not_exist")
    crown.npcs["orphan"] = orphan
    resolve_cascade(crown)
    eff = crown.npcs["orphan"].effective_convictions
    print(f"  Orphan effective (new rule, α=1.0): {fmt_vec(eff, 4)}")
    print(f"  v1 result: zero (silent bug). v2: {'POPULATED' if sum(eff.values())>0.01 else 'still zero'}")
    
    # Aggregate now includes orphan correctly
    print(f"  Aggregate w/ orphan: {fmt_vec(crown.aggregate_effective(), 5)}")
    
    # Strictness sanity
    crown2 = build_crown_v2()
    crown2.legitimacy = 7; crown2.popular_support = 1
    s_brittle = crown2.strictness()
    crown2.legitimacy = 1; crown2.popular_support = 7
    s_loose = crown2.strictness()
    print(f"  High-L low-PS strictness: {s_brittle:.2f}")
    print(f"  Low-L high-PS strictness: {s_loose:.2f}")


def scenario_8_self_other_attribution():
    """NEW: test Self-Other axis modulating outcome attribution."""
    print("\n" + "=" * 72)
    print("SCENARIO 8 — Self-Other orientation: outcome attribution test")
    print("=" * 72)
    
    # Two crowns: one led by Almud (orient +0.1), one by Cesare (+0.8).
    # Both win same DA. Question: does attribution differ?
    print("Same Mission win for two leaders with different self_other_orientation:")
    
    for name, primary, orient in [
        ("Almud (+0.1, public-spirited)", {"Virtue": 0.6, "Authority": 0.4}, 0.1),
        ("Cesare (+0.8, self-aggrandizing)", {"Authority": 0.5, "Utility": 0.5}, 0.8),
    ]:
        crown = build_crown_v2()
        leader = NPC("almud", primary_convictions=primary,
            cultural_background="crown_court_florentine",
            self_other_orientation=orient, standing=7)
        crown.npcs["almud"] = leader
        resolve_cascade(crown)
        
        # Outcome: Mission won, but attribution scales by orientation
        # (proposal §5 rules: high self-orientation reduces fraction of benefit attributed to "populace")
        # Mock: effective mission_outcome = +1 × (1 - 0.5 × max(0, orient))
        raw_outcome = +1
        attributed_outcome = raw_outcome * (1 - 0.5 * max(0, orient))
        
        # Run 4 seasons of these wins
        crown_log = []
        for s in range(4):
            update_legitimacy_and_support(crown, mission_outcome=attributed_outcome,
                                          violation_score=0.1 if orient > 0.5 else 0)
            crown_log.append((crown.legitimacy, crown.popular_support))
        
        print(f"\n  {name}")
        print(f"    raw outcome=+1, attributed={attributed_outcome:.2f}")
        print(f"    Final L={crown.legitimacy:.2f}, PS={crown.popular_support:.2f}, "
              f"M={crown.mandate()}, fid={crown.cascade_fidelity():.3f}")


# ============================================================
# Main
# ============================================================
if __name__ == "__main__":
    scenario_1_static_v2()
    scenario_2_succession_v2()
    scenario_3_crisis_v2()
    scenario_4_oscillation_v2()
    scenario_5_honest_defeat_v2()
    scenario_6_tyrant_v2()
    scenario_7_edge_v2()
    scenario_8_self_other_attribution()
