"""
PP-686 Simulator — Faction Behavior Architecture
Tests Mission, Cascade, Public Expectation, Legitimacy + Popular Support against
audit concerns. Runs 7 scenarios; produces evaluation log.
"""
import math
import json
import random
from dataclasses import dataclass, field
from typing import Optional

random.seed(0)  # determinism

# 12-Conviction working taxonomy (per conversation; Honor pending)
CONVICTIONS = [
    "Faith", "Authority", "Order", "Scholastic", "Utility",
    "Equity", "Liberty", "Precedent", "Community", "Identity",
    "Warden", "Virtue",
]

# Role templates (expected_convictions per faction role)
ROLE_TEMPLATES = {
    "sovereign":            {"Virtue": 0.4, "Authority": 0.4, "Honor": 0.2},  # Honor placeholder
    "ecclesiastical":       {"Faith": 0.5, "Authority": 0.3, "Scholastic": 0.2},
    "mercantile_procedural":{"Order": 0.4, "Utility": 0.3, "Scholastic": 0.3},
    "intelligence":         {"Scholastic": 0.4, "Utility": 0.4, "Authority": 0.2},
    "reformist":            {"Equity": 0.4, "Liberty": 0.3, "Community": 0.3},
    "military_order":       {"Authority": 0.4, "Virtue": 0.3, "Honor": 0.3},  # Honor placeholder
}
# strip "Honor" since not yet ratified — fold into Virtue for sims
def _strip_honor(d):
    if "Honor" in d:
        d["Virtue"] = d.get("Virtue", 0) + d.pop("Honor")
    return d
ROLE_TEMPLATES = {k: _normalize(_strip_honor(v)) if False else v for k, v in ROLE_TEMPLATES.items()}

def _normalize(d):
    s = sum(d.values())
    return {k: v/s for k,v in d.items()} if s>0 else d

ROLE_TEMPLATES = {k: _normalize(_strip_honor(dict(v))) for k,v in ROLE_TEMPLATES.items()}

PUBLIC_TEMPERAMENTS = {
    "pragmatic":     (0.7, 0.3),  # (alpha_outcomes, beta_conduct)
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
    if s == 0:
        return vec_zero()
    return {k: val/s for k, val in v.items()}

def cosine(a, b):
    """Cosine similarity of two Conviction vectors."""
    dot = sum(a.get(c, 0) * b.get(c, 0) for c in CONVICTIONS)
    na = math.sqrt(sum(a.get(c, 0)**2 for c in CONVICTIONS))
    nb = math.sqrt(sum(b.get(c, 0)**2 for c in CONVICTIONS))
    if na == 0 or nb == 0:
        return 0.0
    return dot / (na * nb)


@dataclass
class NPC:
    id: str
    personal_convictions: dict
    standing: int                    # 1-7
    supervisor_id: Optional[str] = None
    effective_convictions: dict = field(default_factory=vec_zero)

    def alpha(self, institutional_culture: float) -> float:
        """α = α_base + α_seniority + α_institution, clamped [0,1]."""
        a_base = 0.4
        a_seniority = -0.2 + (0.6 * (self.standing - 1) / 6)  # standing 1=-0.2, 7=+0.4
        a_inst = institutional_culture
        return max(0.0, min(1.0, a_base + a_seniority + a_inst))


@dataclass
class Faction:
    id: str
    role: str
    leader_id: str
    npcs: dict                                  # id -> NPC
    institutional_culture: float = 0.0          # α_institution adjustment
    legitimacy: float = 4.0                     # 0-7
    popular_support: float = 4.0                # 0-7
    territorial_temperaments: list = field(default_factory=lambda: ["balanced"])
    mission_aligned_categories: set = field(default_factory=set)
    mission_contradicted_categories: set = field(default_factory=set)
    drift_coef: float = 0.3                     # cascade drift speed

    def expected_convictions(self):
        return ROLE_TEMPLATES[self.role]

    def temperament_weights(self):
        """Average alpha/beta across territories."""
        a_sum = b_sum = 0
        for t in self.territorial_temperaments:
            a, b = PUBLIC_TEMPERAMENTS[t]
            a_sum += a; b_sum += b
        n = len(self.territorial_temperaments)
        return a_sum/n, b_sum/n

    def aggregate_effective(self):
        """Power-weighted (Standing × inverse-tier-distance-from-leader) aggregate.
        Resolves audit P1-2 — we use Standing-weighted sum, normalized."""
        agg = vec_zero()
        for npc in self.npcs.values():
            weight = npc.standing  # simplest power weight
            for c, val in npc.effective_convictions.items():
                agg[c] += weight * val
        return vec_normalize(agg)

    def cascade_fidelity(self):
        return cosine(self.aggregate_effective(), self.expected_convictions())

    def strictness(self):
        """0 + 0.5×L/7 + (-0.3)×PS/7 + base 0.4, clamped [0,1]."""
        return max(0.0, min(1.0,
            0.4 + 0.5 * (self.legitimacy / 7) - 0.3 * (self.popular_support / 7)))

    def mandate(self):
        return round(0.5 * self.legitimacy + 0.5 * self.popular_support)


def resolve_cascade(faction: Faction):
    """Recursive cascade resolution. Leader's effective = personal.
    Each subordinate: alpha × personal + (1-alpha) × supervisor's effective.
    Damped toward new value via drift_coef."""
    # First: leader sets root
    leader = faction.npcs[faction.leader_id]
    leader.effective_convictions = dict(leader.personal_convictions)
    
    # BFS through hierarchy
    resolved = {leader.id}
    queue = [n for n in faction.npcs.values() if n.supervisor_id == leader.id]
    while queue:
        next_queue = []
        for npc in queue:
            if npc.supervisor_id not in resolved:
                next_queue.append(npc)
                continue
            sup = faction.npcs[npc.supervisor_id]
            alpha = npc.alpha(faction.institutional_culture)
            target = vec_add(npc.personal_convictions, sup.effective_convictions,
                            w_a=alpha, w_b=(1-alpha))
            # Damping toward target
            current = npc.effective_convictions
            # If first resolution (current is zero), set immediately
            if sum(current.values()) == 0:
                npc.effective_convictions = target
            else:
                npc.effective_convictions = vec_add(current, target,
                    w_a=(1-faction.drift_coef), w_b=faction.drift_coef)
            resolved.add(npc.id)
            # Children
            for child in faction.npcs.values():
                if child.supervisor_id == npc.id and child.id not in resolved:
                    next_queue.append(child)
        if not next_queue:
            break
        queue = next_queue


def ob_modifier(faction: Faction, da_category: str, da_alignment: dict) -> float:
    """Per §3.7. da_alignment is a Conviction-vector representing what the action
    expresses (e.g., a covert betrayal might be high Utility, low Virtue)."""
    # Mission alignment
    if da_category in faction.mission_aligned_categories:
        m_align = -1
    elif da_category in faction.mission_contradicted_categories:
        m_align = +1
    else:
        m_align = 0
    
    # Cascade alignment: cosine between aggregate effective and da_alignment
    c_sim = cosine(faction.aggregate_effective(), da_alignment)
    # Convert to ±1: similarity > 0.5 → -1, < -0.3 → +1, else 0
    if c_sim > 0.5:    c_align = -1
    elif c_sim < -0.3: c_align = +1
    else:              c_align = 0
    
    # Expectation alignment: cosine between role-expected and da_alignment
    e_sim = cosine(faction.expected_convictions(), da_alignment)
    strictness = faction.strictness()
    raw = 0
    if e_sim < -0.3: raw = +1
    elif e_sim > 0.5: raw = -1
    else: raw = 0
    e_align = raw * (0.5 + strictness)  # strictness scales penalty
    
    total = m_align + c_align + e_align
    return max(-3, min(3, round(total)))


def update_legitimacy_and_support(faction: Faction, mission_outcome: int,
                                  violation_score: float = 0,
                                  procedural_score: float = 0):
    """One season's Δ for L and PS.
    mission_outcome: -1 (harm), 0 (neutral), +1 (benefit)
    violation_score: 0..3 (heresy=2, coup=3, oath-break=1, exposed covert=1)
    procedural_score: 0..2 (succession=2, treaty=1)"""
    a, b = faction.temperament_weights()
    fid = faction.cascade_fidelity()  # [-1, 1]
    
    # Popular Support drift
    delta_ps = a * mission_outcome + b * fid * 0.5  # scale fidelity contribution
    faction.popular_support = max(0, min(7, faction.popular_support + delta_ps))
    
    # Legitimacy drift (slower)
    delta_legit = (
        0.05  # tiny continuity gain per season
        + 0.4 * procedural_score
        + 0.05 * fid            # very slow expectation integration
        - 0.6 * violation_score
    )
    faction.legitimacy = max(0, min(7, faction.legitimacy + delta_legit))


# ============================================================
# Scenario builder
# ============================================================
def build_crown_baseline():
    """Crown faction baseline: Almud (Virtue 0.6, Authority 0.4) leads.
    Hierarchy: Almud (s=7) → 2 deputies (s=5, s=4) → 4 ground (s=2-3)."""
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
    crown.npcs["almud"] = NPC("almud", {"Virtue": 0.6, "Authority": 0.4}, standing=7)
    crown.npcs["chamberlain"] = NPC("chamberlain", {"Order": 0.5, "Authority": 0.3, "Virtue": 0.2},
                                    standing=5, supervisor_id="almud")
    crown.npcs["spymaster"] = NPC("spymaster", {"Utility": 0.6, "Scholastic": 0.4},
                                   standing=5, supervisor_id="almud")
    crown.npcs["captain1"] = NPC("captain1", {"Authority": 0.5, "Virtue": 0.5},
                                  standing=4, supervisor_id="chamberlain")
    crown.npcs["captain2"] = NPC("captain2", {"Order": 0.6, "Utility": 0.4},
                                  standing=4, supervisor_id="chamberlain")
    crown.npcs["agent1"] = NPC("agent1", {"Utility": 0.7, "Liberty": 0.3},
                                standing=3, supervisor_id="spymaster")
    crown.npcs["clerk1"] = NPC("clerk1", {"Order": 0.4, "Community": 0.4, "Faith": 0.2},
                                standing=2, supervisor_id="captain1")
    crown.npcs["clerk2"] = NPC("clerk2", {"Authority": 0.4, "Order": 0.4, "Virtue": 0.2},
                                standing=2, supervisor_id="captain1")
    return crown


# ============================================================
# Scenarios
# ============================================================
def fmt_vec(v, top_n=4):
    nonzero = [(k, val) for k, val in v.items() if abs(val) > 0.01]
    nonzero.sort(key=lambda x: -x[1])
    return ", ".join(f"{k}:{val:.2f}" for k, val in nonzero[:top_n])


def scenario_1_static_parity():
    """Sanity: build Crown, resolve cascade, compute Ob for representative DAs."""
    print("=" * 72)
    print("SCENARIO 1 — Static Parity Check")
    print("=" * 72)
    crown = build_crown_baseline()
    resolve_cascade(crown)
    
    print(f"\nCrown leader Almud personal: {fmt_vec(crown.npcs['almud'].personal_convictions)}")
    print(f"Crown aggregate effective:   {fmt_vec(crown.aggregate_effective())}")
    print(f"Crown expected (sovereign):  {fmt_vec(crown.expected_convictions())}")
    print(f"Cascade fidelity:            {crown.cascade_fidelity():.3f}")
    print(f"Legitimacy={crown.legitimacy}, PopularSupport={crown.popular_support}")
    print(f"Strictness={crown.strictness():.2f}")
    print(f"Mandate (derived):           {crown.mandate()}")
    
    # Sample DAs
    das = [
        ("public_governance",  {"Virtue": 0.6, "Authority": 0.4},   "public ceremony"),
        ("covert_betrayal",    {"Utility": 0.7, "Authority": 0.3},  "covert assassination"),
        ("diplomatic_alliance",{"Authority": 0.5, "Order": 0.5},    "treaty signing"),
        ("antinomian_action",  {"Liberty": 0.7, "Utility": 0.3},    "rebellion against Crown laws"),
    ]
    print(f"\n{'DA':<35} {'category':<22} {'Ob mod':<8}")
    for cat, align, desc in das:
        ob = ob_modifier(crown, cat, align)
        print(f"  {desc:<33} {cat:<22} {ob:+d}")
    
    # Compare against current Ethical Framework Modifiers (Crown / Virtue Ethics):
    # public/visible -1, covert/morally-ambiguous +1
    print("\nLegacy comparison (Ethical Framework Modifier table):")
    print("  Public ceremony  →  current: -1   |  PP-686: see above")
    print("  Covert betrayal  →  current: +1   |  PP-686: see above")
    return crown


def scenario_2_succession_dynamics():
    """Replace Almud with two different successors; watch cascade re-resolve over 6 seasons."""
    print("\n" + "=" * 72)
    print("SCENARIO 2 — Succession Dynamics (cascade re-resolution under leader change)")
    print("=" * 72)
    
    for successor_name, successor_convs in [
        ("Cesare (Authority+Utility ruler, low Virtue)", {"Authority": 0.5, "Utility": 0.5}),
        ("Lorenzo (Virtue+Scholastic, principled scholar)", {"Virtue": 0.5, "Scholastic": 0.4, "Authority": 0.1}),
    ]:
        print(f"\n--- Successor: {successor_name} ---")
        crown = build_crown_baseline()
        resolve_cascade(crown)
        before = fmt_vec(crown.aggregate_effective())
        before_fid = crown.cascade_fidelity()
        
        # Replace leader
        crown.npcs["almud"].personal_convictions = successor_convs
        
        for season in range(6):
            resolve_cascade(crown)
            agg = crown.aggregate_effective()
            fid = crown.cascade_fidelity()
            print(f"  S{season+1}: aggregate {fmt_vec(agg, 3)} | fidelity {fid:.3f}")
        
        print(f"  Before: {before} (fid {before_fid:.3f})")
        print(f"  After 6: {fmt_vec(crown.aggregate_effective(), 3)} (fid {crown.cascade_fidelity():.3f})")


def scenario_3_conviction_crisis():
    """Leader enters Conviction crisis (Scars 3+). personal_convictions becomes
    unstable each season per the d6 table from conviction_track_v1.md §2.
    Test: does faction state thrash?"""
    print("\n" + "=" * 72)
    print("SCENARIO 3 — Leader Conviction Crisis (cascade root unstable)")
    print("=" * 72)
    
    crown = build_crown_baseline()
    resolve_cascade(crown)
    
    print("Initial fidelity:", round(crown.cascade_fidelity(), 3))
    print("Simulating 8 seasons with leader oscillating personal_convictions:")
    
    # Simulate the d6 crisis table: each season, leader rolls — primary, secondary, autonomy(self-pres), or pull
    crisis_states = [
        {"Virtue": 0.6, "Authority": 0.4},               # roll 1-2: primary
        {"Authority": 0.7, "Virtue": 0.3},               # roll 3-4: secondary inverted
        {"Liberty": 0.8, "Utility": 0.2},                # roll 5: self-pres / Liberty
        {"Identity": 0.6, "Community": 0.4},             # roll 6: relational pull
    ]
    rng = random.Random(42)
    fidelities = []
    aggs = []
    for season in range(8):
        # Crisis: random new personal each season
        crown.npcs["almud"].personal_convictions = rng.choice(crisis_states)
        resolve_cascade(crown)
        f = crown.cascade_fidelity()
        fidelities.append(f)
        aggs.append(fmt_vec(crown.aggregate_effective(), 3))
        print(f"  S{season+1}: leader={fmt_vec(crown.npcs['almud'].personal_convictions, 2)} | "
              f"agg={aggs[-1]} | fid={f:.3f}")
    
    # Diagnostic: variance of fidelity = thrash measure
    mean = sum(fidelities)/len(fidelities)
    var = sum((f-mean)**2 for f in fidelities)/len(fidelities)
    print(f"\nFidelity variance: {var:.4f}  (high variance = thrashing)")
    print(f"Drift coef: {crown.drift_coef} damps per season; lower drift = more stability")


def scenario_4_strictness_oscillation():
    """Run feedback loop: DA outcomes drive ΔL/PS, which drives strictness, which
    affects next-DA Ob, which affects outcome probability, etc.
    Test: does the loop converge or oscillate?"""
    print("\n" + "=" * 72)
    print("SCENARIO 4 — Strictness Feedback Loop (oscillation test)")
    print("=" * 72)
    
    crown = build_crown_baseline()
    resolve_cascade(crown)
    
    # Sequence of DAs alternating "covert_betrayal" (high Ob) and "public_governance" (low Ob)
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
    
    print(f"{'Season':<8}{'DA':<22}{'Ob':<5}{'Out':<6}{'L':<6}{'PS':<6}{'Str':<6}")
    for i, (cat, align, outcome) in enumerate(sequence):
        ob = ob_modifier(crown, cat, align)
        # Determine outcome score and violation score
        if outcome == "succeed":
            mo = +1 if cat in ("public_governance", "diplomatic_alliance") else 0
            vs = 0
            ps = 0
        elif outcome == "fail":
            mo = -1
            # If covert and exposed/failed, violation
            vs = 1 if cat == "covert_betrayal" else 0.5
            ps = 0
        update_legitimacy_and_support(crown, mo, vs, ps)
        print(f"S{i+1:<7}{cat:<22}{ob:+2d}   {outcome:<6}"
              f"{crown.legitimacy:<6.2f}{crown.popular_support:<6.2f}{crown.strictness():<6.2f}")
    
    # Did it stabilize?
    print(f"\nFinal: L={crown.legitimacy:.2f}, PS={crown.popular_support:.2f}, "
          f"Strictness={crown.strictness():.2f}, Mandate={crown.mandate()}")


def scenario_5_honest_defeat():
    """Crown loses war but maintains Cascade fidelity to expectations.
    Predicted: Legitimacy preserved, Popular Support bleeds (β preserves some)."""
    print("\n" + "=" * 72)
    print("SCENARIO 5 — Honest Defeat (Mission failure with Cascade fidelity)")
    print("=" * 72)
    
    crown = build_crown_baseline()
    crown.territorial_temperaments = ["traditional", "traditional", "balanced"]  # β-weighted
    resolve_cascade(crown)
    
    print(f"Initial: L={crown.legitimacy}, PS={crown.popular_support}, "
          f"Fidelity={crown.cascade_fidelity():.3f}")
    print("8 seasons of Mission failure but high Cascade fidelity (war goes badly, Crown acts honorably):")
    
    history = []
    for season in range(8):
        # Each season: failed Mission (mo=-1) but no violations, no procedural events
        update_legitimacy_and_support(crown, mission_outcome=-1, violation_score=0, procedural_score=0)
        history.append((crown.legitimacy, crown.popular_support))
        print(f"  S{season+1}: L={crown.legitimacy:.2f}, PS={crown.popular_support:.2f}, "
              f"Mandate={crown.mandate()}")
    
    print(f"\nNet ΔL: {history[-1][0] - 5.0:+.2f}, ΔPS: {history[-1][1] - 5.0:+.2f}")
    print("Verdict pattern: Legitimacy preserved? Popular Support eroded?")


def scenario_6_successful_tyrant():
    """Cesare-style: covert action delivers Mission, but anti-role conduct erodes Legitimacy.
    Predicted: Popular Support rises, Legitimacy bleeds, Mandate diverges."""
    print("\n" + "=" * 72)
    print("SCENARIO 6 — Successful Tyrant (Mission win via anti-role conduct)")
    print("=" * 72)
    
    crown = build_crown_baseline()
    crown.territorial_temperaments = ["pragmatic", "pragmatic", "outcomes_only"]  # α-weighted
    # Replace Almud with Cesare-style leader
    crown.npcs["almud"].personal_convictions = {"Authority": 0.5, "Utility": 0.5}
    resolve_cascade(crown)
    
    print(f"Initial (Cesare just took over): L={crown.legitimacy}, PS={crown.popular_support}, "
          f"Fidelity={crown.cascade_fidelity():.3f}")
    print("8 seasons of successful Mission via covert/anti-role action:")
    
    for season in range(8):
        # Mission succeeds (mo=+1), but each success carries small violation cost (covert action)
        update_legitimacy_and_support(crown, mission_outcome=+1, violation_score=0.3, procedural_score=0)
        # Cascade fidelity stays low because Cesare's Convictions don't match sovereign role
        print(f"  S{season+1}: L={crown.legitimacy:.2f}, PS={crown.popular_support:.2f}, "
              f"Mandate={crown.mandate()}, Fid={crown.cascade_fidelity():.3f}")
    
    print(f"\nFinal L-PS divergence: {abs(crown.legitimacy - crown.popular_support):.2f}")
    print("Pattern: PS up, L down? — strong-but-fragile signature")


def scenario_7_edge_cases():
    """Audit P2-4: zero-vector cascade fidelity, leaderless, orphan NPC."""
    print("\n" + "=" * 72)
    print("SCENARIO 7 — Edge Cases (audit P2-4)")
    print("=" * 72)
    
    # Edge 1: leaderless faction (leader Convictions all zero)
    crown = build_crown_baseline()
    crown.npcs["almud"].personal_convictions = vec_zero()  # zero-vector leader
    try:
        resolve_cascade(crown)
        agg = crown.aggregate_effective()
        fid = crown.cascade_fidelity()
        print(f"  Zero-vector leader: agg={fmt_vec(agg, 3)}, fid={fid:.3f}  (cosine returns 0 cleanly)")
    except Exception as e:
        print(f"  CRASH: {e}")
    
    # Edge 2: orphan NPC (supervisor_id refers to nobody)
    crown = build_crown_baseline()
    crown.npcs["orphan"] = NPC("orphan", {"Liberty": 0.8, "Utility": 0.2},
                                standing=3, supervisor_id="ghost_id_does_not_exist")
    try:
        resolve_cascade(crown)
        # Orphan's effective_convictions
        eff = crown.npcs["orphan"].effective_convictions
        print(f"  Orphan NPC effective: {fmt_vec(eff, 3) if sum(eff.values())>0 else 'zero (skipped)'}")
        print(f"  PROBLEM: orphan's contribution to aggregate was {'INCLUDED' if sum(eff.values())>0 else 'SKIPPED — bug'}")
    except Exception as e:
        print(f"  CRASH: {e}")
    
    # Edge 3: zero-magnitude cascade_fidelity (perfectly orthogonal)
    crown = build_crown_baseline()
    # Force aggregate to be all-Equity (orthogonal to sovereign role)
    crown.npcs["almud"].personal_convictions = {"Equity": 1.0}
    for n in crown.npcs.values():
        n.personal_convictions = {"Equity": 1.0}
    resolve_cascade(crown)
    fid = crown.cascade_fidelity()
    print(f"  Orthogonal aggregate: fid={fid:.3f}  (expected near 0)")
    
    # Edge 4: leader Conviction crisis with strictness
    crown = build_crown_baseline()
    crown.legitimacy = 7
    crown.popular_support = 1
    str1 = crown.strictness()
    crown.legitimacy = 1
    crown.popular_support = 7
    str2 = crown.strictness()
    print(f"  High-L low-PS strictness: {str1:.2f}  (expected high — brittle)")
    print(f"  Low-L high-PS strictness: {str2:.2f}  (expected low — populist tolerated)")


# ============================================================
# Main
# ============================================================
if __name__ == "__main__":
    scenario_1_static_parity()
    scenario_2_succession_dynamics()
    scenario_3_conviction_crisis()
    scenario_4_strictness_oscillation()
    scenario_5_honest_defeat()
    scenario_6_successful_tyrant()
    scenario_7_edge_cases()
