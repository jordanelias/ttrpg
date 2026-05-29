"""
m4a_bout_state_graph.py -- Module 4a of the v32 combat-balance sim (bout state graph + control flow).

The engagement control flow that Module 4b's sub-action mechanics run inside:
  - the Bout state subgraph (Out-of-contact / Closing / In-bind / Breaking / terminal states)
  - Phase 5 Commit depth structure (Stamina/Concentration cost, chain-length cap, wound-state ceiling)
  - termination conditions + priority order
  - Disengage resolution and end-of-pass recovery

M4 was budgeted at two modules and split per the prep-doc manifest: M4a (this file, state graph
+ control flow) and M4b (sub-action Pool/Ob/degree mechanics). Depends on Module 1 (roll_net for
the opposed disengage roll).

Constant provenance: tests/sim/v32-combat-balance/m4a_verification_ledger.json
  Class A = canonical (derived_stats_v30: Take a Breath, Out of Breath, wound penalty, Felled).
  Class B = v32 draft sim-seeds (combat_v32_proposal, engagement-phase sections); sim-tunable, NOT canonical.
"""
import numpy as np
from m1_dice_sigma_core import roll_net

# ===== Class B: Phase 5 Commit depth structure (combat_v32_proposal §4.6 -- draft) =====
DEPTH2_STAMINA = 3        # [canonical: combat_v32_proposal §4.6 -- draft (Preparatory)]
DEPTH3_STAMINA = 5        # [canonical: combat_v32_proposal §4.6 -- draft (Committed)]
DEPTH4_STAMINA = 7        # [canonical: combat_v32_proposal §4.6 -- draft (Deep)]
DEPTH5_STAMINA = 10       # [canonical: combat_v32_proposal §4.6 -- draft (Full)]
DEPTH3_CONCENTRATION = 1  # [canonical: combat_v32_proposal §4.6 -- draft]
DEPTH4_CONCENTRATION = 2  # [canonical: combat_v32_proposal §4.6 -- draft]
DEPTH5_CONCENTRATION = 4  # [canonical: combat_v32_proposal §4.6 -- draft]
DEPTH3_CHAIN_CAP = 4      # [canonical: combat_v32_proposal §4.6 / §12.6 -- draft]
DEPTH4_CHAIN_CAP = 6      # [canonical: combat_v32_proposal §4.6 / §12.6 -- draft]
DEPTH_TABLE = {
    1: {"stamina": 2, "concentration": 0, "chain_cap": 1},                                                  # [canonical: combat_v32_proposal §4.6 -- draft (Probe)]
    2: {"stamina": DEPTH2_STAMINA, "concentration": 0, "chain_cap": 2},                                     # [canonical: combat_v32_proposal §4.6 -- draft (Preparatory)]
    3: {"stamina": DEPTH3_STAMINA, "concentration": DEPTH3_CONCENTRATION, "chain_cap": DEPTH3_CHAIN_CAP},   # [canonical: combat_v32_proposal §4.6 -- draft (Committed)]
    4: {"stamina": DEPTH4_STAMINA, "concentration": DEPTH4_CONCENTRATION, "chain_cap": DEPTH4_CHAIN_CAP},   # [canonical: combat_v32_proposal §4.6 -- draft (Deep)]
    5: {"stamina": DEPTH5_STAMINA, "concentration": DEPTH5_CONCENTRATION, "chain_cap": None},               # [canonical: combat_v32_proposal §4.6 -- draft (Full, unlimited chain)]
}

# Class B: depth ceiling per wound state (combat_v32_proposal §4.6 -- draft)
DEPTH_CEILING_UNWOUNDED = 5         # [canonical: combat_v32_proposal §4.6 -- draft]
DEPTH_CEILING_WOUNDED = 4           # [canonical: combat_v32_proposal §4.6 -- draft]
DEPTH_CEILING_HEAVILY_WOUNDED = 3   # [canonical: combat_v32_proposal §4.6 -- draft (>= MW-1 wounds)]

# ===== Class B: Bout termination (combat_v32_proposal §4.7 / §12.5 -- draft) =====
RESOURCE_CRITICAL_FRACTION = 0.3    # [canonical: combat_v32_proposal §4.7 -- draft (<30% forces Phase 7)]
WOUND_TRANSITION_OFFSET = 1         # [canonical: combat_v32_proposal §4.7 -- draft (net >= Ob + wounds + 1)]
BASE_OB_MIN = 1                     # [canonical: combat_v32_proposal §4.7 -- draft (base Ob 1-3)]
BASE_OB_MAX = 3                     # [canonical: combat_v32_proposal §4.7 -- draft (base Ob 1-3)]
# §12.5 chain-termination priority (wound, chain-cap, mutual-separation, clash, then resource depletion)
TERMINATION_PRIORITY = ["wound_transition", "chain_cap", "mutual_separation", "deep_commit_clash", "concentration_depletion", "stamina_depletion"]  # [canonical: combat_v32_proposal §12.5 -- draft (priority 1,5,2,6,3,4)]

# ===== Class B: Phase 7 Disengage (combat_v32_proposal §4.8 -- draft) =====
DISENGAGE_CLEAN_STAMINA = 1            # [canonical: combat_v32_proposal §4.8 -- draft]
DISENGAGE_DEFENSIVE_STAMINA = 2       # [canonical: combat_v32_proposal §4.8 -- draft]
DISENGAGE_SUDDEN_STAMINA = 3          # [canonical: combat_v32_proposal §4.8 -- draft]
DISENGAGE_DEFENSIVE_PURSUIT_OB = 2    # [canonical: combat_v32_proposal §4.8 -- draft]
DISENGAGE_CLEAN_NET = 2               # [canonical: combat_v32_proposal §4.8 -- draft (net >= +2 clean)]
DISENGAGE_FAILURE_NET = -3            # [canonical: combat_v32_proposal §4.8 -- draft (net <= -3 failure)]
DISENGAGE_OPTIONS = {
    "clean":     {"stamina": DISENGAGE_CLEAN_STAMINA, "concentration": 0, "pursuit_ob": 0},                              # [canonical: combat_v32_proposal §4.8 -- draft]
    "pursuing":  {"stamina": 0, "concentration": 0, "pursuit_ob": 0},                                                    # [canonical: combat_v32_proposal §4.8 -- draft (conditional)]
    "defensive": {"stamina": DISENGAGE_DEFENSIVE_STAMINA, "concentration": 0, "pursuit_ob": DISENGAGE_DEFENSIVE_PURSUIT_OB},  # [canonical: combat_v32_proposal §4.8 -- draft]
    "drawing":   {"stamina": 0, "concentration": 0, "pursuit_ob": 1},                                                    # [canonical: combat_v32_proposal §4.8 -- draft (+1 Ob drawn-in)]
    "sudden":    {"stamina": DISENGAGE_SUDDEN_STAMINA, "concentration": 1, "pursuit_ob": 0},                             # [canonical: combat_v32_proposal §4.8 -- draft]
}

# ===== Class B: Phase 8 recovery (combat_v32_proposal §4.9 -- draft) =====
COHERENCE_RECOVERY = 1   # [canonical: combat_v32_proposal §4.9 -- draft (+1 if no Thread-op, P-15)]

# ===== Class A: canonical anchors (derived_stats_v30) =====
STAMINA_RECOVERY_MULT = 2   # [canonical: derived_stats_v30 §4.2 (Take a Breath: (End + History) x2)]
OUT_OF_BREATH_PENALTY = 2   # [canonical: derived_stats_v30 §4.2 (Out of Breath at 0: -2D)]
WOUND_POOL_PENALTY = 1      # [canonical: derived_stats_v30 §4.1 (-1D per wound, no Ob)]
FELLED_WOUND_OFFSET = 1     # [canonical: derived_stats_v30 §4.1 (Felled at MW + 1 wounds)]

# ===== Bout state subgraph (combat_v32_proposal §4.7 / §12.1 -- draft) =====
ENGAGEMENT_STATES = {
    "out_of_contact": {"options": ["probe_cut", "probe_thrust", "step_around", "disengage"], "transitions": ["closing", "breaking"]},                                   # [canonical: combat_v32_proposal §4.7/§12.1 -- draft]
    "closing":        {"options": ["cut", "thrust", "press_the_bind", "yield_to_bind", "void_and_counter", "targeted_line", "disengage"], "transitions": ["in_bind", "out_of_contact", "wounded", "breaking"]},  # [canonical: combat_v32_proposal §4.7/§12.1 -- draft]
    "in_bind":        {"options": ["wind", "yield", "press", "displace", "break_bind", "grip_change", "targeted_line", "throw_strike"], "transitions": ["closing", "breaking", "wounded"]},                        # [canonical: combat_v32_proposal §4.7/§12.1 -- draft]
    "breaking":       {"options": ["pursue", "release", "throw_strike"], "transitions": ["disengaged", "wounded"]},                                                      # [canonical: combat_v32_proposal §4.7/§12.1 -- draft]
    "wounded":        {"options": [], "transitions": ["breaking", "disengaged"]},                                                                                        # [canonical: combat_v32_proposal §4.7 -- draft (continue or break)]
    "disengaged":     {"options": [], "transitions": []},                                                                                                                # terminal
    "felled":         {"options": [], "transitions": []},                                                                                                                # terminal
}
TERMINAL_STATES = {"disengaged", "felled"}


def depth_cost(depth):
    """Stamina + Concentration cost of a Phase 5 commit at this depth (§4.6 draft)."""
    d = DEPTH_TABLE[depth]
    return d["stamina"], d["concentration"]


def chain_cap(depth):
    """Bout chain-length cap from commit depth (§4.6 / §12.6 draft); None = unlimited (Full)."""
    return DEPTH_TABLE[depth]["chain_cap"]


def depth_ceiling(wounds, max_wounds_val):
    """Maximum commit depth permitted at a wound state (§4.6 draft)."""
    if wounds == 0:
        return DEPTH_CEILING_UNWOUNDED
    if wounds >= max_wounds_val - 1:
        return DEPTH_CEILING_HEAVILY_WOUNDED
    return DEPTH_CEILING_WOUNDED


def wound_transition(net, base_ob, current_wounds):
    """A sub-action lands a wound when net successes reach Ob + (current wounds + offset) (§4.7 draft)."""
    return net >= base_ob + (current_wounds + WOUND_TRANSITION_OFFSET)


def resource_critical(current, maximum):
    """A fighter at < the critical fraction of Stamina/Concentration is forced to Phase 7 (§4.7 draft)."""
    return maximum > 0 and (current / maximum) < RESOURCE_CRITICAL_FRACTION


def felled(wounds, max_wounds_val):
    """Felled at Max Wounds + offset wounds accrued (canonical derived_stats §4.1)."""
    return wounds >= max_wounds_val + FELLED_WOUND_OFFSET


def disengage_outcome(net):
    """Map disengager net successes to the §4.8 outcome band."""
    if net >= DISENGAGE_CLEAN_NET:
        return "clean"
    if net >= 0:
        return "partial"
    if net > DISENGAGE_FAILURE_NET:
        return "bind_held"
    return "failure"


def resolve_disengage(disengager_pool, pursuer_pool, rng=None, pursued=True):
    """Phase 7 disengage (§4.8): if pursued, opposed Disengage vs Reaction roll; else automatic clean."""
    if not pursued:
        return "clean"
    net = roll_net(disengager_pool, rng=rng) - roll_net(pursuer_pool, rng=rng)
    return disengage_outcome(net)


def stamina_recovery(end, history):
    """Take a Breath recovery (canonical derived_stats §4.2): (End + History) x mult."""
    return (end + history) * STAMINA_RECOVERY_MULT


def concentration_recovery(focus):
    """Phase 8 Concentration recovery (combat_v32_proposal §4.9 draft): + Focus."""
    return focus


def options_at(state):
    """Sub-action option set surfaced at an engagement state (§12.1 draft)."""
    return ENGAGEMENT_STATES[state]["options"]


def transitions_from(state):
    """Engagement states reachable from this state (§4.7 subgraph)."""
    return ENGAGEMENT_STATES[state]["transitions"]


def terminal(state):
    return state in TERMINAL_STATES


# ============================== self-test ==============================
if __name__ == "__main__":
    checks = []
    rule = "================================================================"
    print("Module 4a (bout state graph + control flow) -- validation against spec")
    print(rule)

    # (a) depth table vs §4.6
    DEPTH_EXPECT = {1:(2,0,1), 2:(3,0,2), 3:(5,1,4), 4:(7,2,6), 5:(10,4,None)}  # [canonical: combat_v32_proposal §4.6 depth table -- draft]
    a_ok = all((DEPTH_TABLE[d]["stamina"], DEPTH_TABLE[d]["concentration"], DEPTH_TABLE[d]["chain_cap"]) == v for d, v in DEPTH_EXPECT.items())
    checks.append(a_ok)
    print(f"\n(a) depth structure (Stamina/Concentration/chain-cap) vs §4.6: {'OK' if a_ok else 'FAIL'}")

    # (b) depth ceiling per wound state (MW=3 example)
    b_ok = (depth_ceiling(0, 3) == 5 and depth_ceiling(1, 3) == 4 and depth_ceiling(2, 3) == 3)  # [canonical: combat_v32_proposal §4.6 depth ceilings -- draft]
    checks.append(b_ok)
    print(f"(b) depth ceiling per wound state (unwounded/wounded/heavy -> 5/4/3): {'OK' if b_ok else 'FAIL'}")

    # (c) wound transition threshold + Felled
    c_ok = (wound_transition(4, 2, 1) is True and wound_transition(3, 2, 1) is False and felled(4, 3) is True and felled(3, 3) is False)  # [canonical: combat_v32_proposal §4.7 + derived_stats §4.1]
    checks.append(c_ok)
    print(f"(c) wound transition (net>=Ob+wounds+1) + Felled (MW+1): {'OK' if c_ok else 'FAIL'}")

    # (d) disengage outcome table (§4.8)
    DIS_EXPECT = {3:"clean", 2:"clean", 1:"partial", 0:"partial", -1:"bind_held", -2:"bind_held", -3:"failure", -5:"failure"}  # [canonical: combat_v32_proposal §4.8 outcome table -- draft]
    d_ok = all(disengage_outcome(n) == v for n, v in DIS_EXPECT.items())
    checks.append(d_ok)
    print(f"(d) disengage outcome bands (>=+2 clean / 0..+1 partial / -1..-2 bind / <=-3 fail): {'OK' if d_ok else 'FAIL'}")

    # (e) recovery formulas
    e_ok = (stamina_recovery(3, 3) == 12 and concentration_recovery(3) == 3)  # [canonical: derived_stats §4.2 Take a Breath ((3+3)x2=12); combat_v32_proposal §4.9 (+Focus)]
    checks.append(e_ok)
    print(f"(e) recovery: Stamina (End+H)x2 -> {stamina_recovery(3,3)} (canon 12); Concentration +Focus -> {concentration_recovery(3)}: {'OK' if e_ok else 'FAIL'}")

    # (f) state-graph integrity: every transition target is a defined state
    valid = set(ENGAGEMENT_STATES)
    f_ok = all(all(t in valid for t in s["transitions"]) for s in ENGAGEMENT_STATES.values())
    checks.append(f_ok)
    print(f"(f) state-graph integrity ({len(ENGAGEMENT_STATES)} states; all transitions valid): {'OK' if f_ok else 'FAIL'}")

    # (g) resource critical threshold
    g_ok = (resource_critical(2, 10) is True and resource_critical(5, 10) is False)  # [canonical: combat_v32_proposal §4.7 -- draft (20% critical, 50% not)]
    checks.append(g_ok)
    print(f"(g) resource-critical (<30%): 2/10 critical, 5/10 not: {'OK' if g_ok else 'FAIL'}")

    # (h) disengage opposed-roll smoke (exercises Module 1 roll_net)
    rng = np.random.default_rng()
    out = resolve_disengage(20, 5, rng=rng)  # [canonical: combat_v32_proposal §4.8 -- draft (strong disengager vs weak pursuer)]
    h_ok = out in ("clean", "partial", "bind_held", "failure")
    checks.append(h_ok)
    print(f"(h) opposed disengage roll smoke (M1 roll_net) -> '{out}': {'OK' if h_ok else 'FAIL'}")

    print("\n" + rule)
    bad = [i for i, c in enumerate(checks) if not c]
    if bad:
        print(f"RESULT: FAIL -- check indices failing: {bad}")
        raise SystemExit(1)
    print(f"RESULT: PASS -- all {len(checks)} checks match spec "
          f"(depth structure, wound-state ceilings, wound/Felled, disengage bands, recovery, state-graph integrity).")
