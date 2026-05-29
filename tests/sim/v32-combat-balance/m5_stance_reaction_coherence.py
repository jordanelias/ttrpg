"""
m5_stance_reaction_coherence.py -- Module five (M5) of the v32 combat-balance sim (matchup systems).

The three sigma-space matchup modifiers fed to M1's Ob grammar, all state-gated:
  - Stance Counter: an authored five-by-five anti-symmetric per-stance counter table, live at the
    Closing state; legacy Ob magnitudes mapped to sigma-levels (|1| Moderate, |2| Strong).
  - Reaction: the two-parameter formula (baseline + depth-slope), depth one-to-five centred at Committed;
    slope sign encodes the physical family (punishes hesitation vs punishes overcommitment).
  - Coherence: named loadout sets carry the synergies (partial credit for near-sets) plus the two
    hand-listed antagonism exceptions (Anticipation x Reaction; Commitment x Disengage). No general matrix.

Reuses M1 LEVEL_SIGMA for every level -> delta-sigma conversion (no re-declared sigma magnitudes).

ALL magnitudes here are flagged v32 draft sim-seeds (the matchup tables the prep doc routes to the
balance pass): the Stance Counter cell values, the Reaction baseline/slope coefficients, the named-set
bonus levels, and the antagonism penalty. They are NOT canonical -- they are the values the balance
sweep exists to tune. Surfaced for Jordan, not silently fixed.

Constant provenance: tests/sim/v32-combat-balance/m5_verification_ledger.json (all Class B, v32 proposal).
"""
import numpy as np
from m1_dice_sigma_core import LEVEL_SIGMA   # level -> delta-sigma (Minor/Moderate/Strong/Major)

# ============ 7.1 Stance Counter Matrix (authored, anti-symmetric, state-gated to Closing) ============
STANCES = ["centered", "raised", "low", "side", "forward_point"]
# legacy Ob magnitudes; rows = Aggressor, cols = Defender; sign negative = Aggressor advantaged.
STANCE_COUNTER_MATRIX = {
    "centered":      {"centered": 0,  "raised": 1,  "low": 0,  "side": -1, "forward_point": 2},   # [canonical: combat_v32_proposal §7.1 -- authored draft]
    "raised":        {"centered": -1, "raised": 0,  "low": 1,  "side": 0,  "forward_point": 1},   # [canonical: combat_v32_proposal §7.1 -- authored draft]
    "low":           {"centered": 0,  "raised": -1, "low": 0,  "side": 1,  "forward_point": 0},   # [canonical: combat_v32_proposal §7.1 -- authored draft]
    "side":          {"centered": 1,  "raised": 0,  "low": -1, "side": 0,  "forward_point": -2},  # [canonical: combat_v32_proposal §7.1 -- authored draft]
    "forward_point": {"centered": -2, "raised": -1, "low": 0,  "side": 2,  "forward_point": 0},   # [canonical: combat_v32_proposal §7.1 -- authored draft]
}
# legacy Ob magnitude -> sigma-space advantage level (the §7.1 reading): |1| -> Moderate, |2| -> Strong
STANCE_OB_TO_LEVEL = {1: "moderate", 2: "strong"}  # [canonical: combat_v32_proposal §7.1 -- draft (±1 Moderate 0.5δσ; ±2 Strong 0.75δσ)]
STANCE_COUNTER_STATE = "closing"                   # state-gated (§12.3); persists from Phase 1 stance until stance changes


def stance_counter_sigma(aggressor_stance, defender_stance):
    """sigma-space stance-counter delta-sigma (§7.1). Convention: positive = Defender advantaged
    (raises Aggressor Ob); negative = Aggressor advantaged. Anti-symmetric; 0 on the diagonal;
    live only at the Closing state."""
    v = STANCE_COUNTER_MATRIX[aggressor_stance][defender_stance]
    if v == 0:
        return 0.0
    level = STANCE_OB_TO_LEVEL[abs(v)]
    sign = 1 if v > 0 else -1
    return sign * LEVEL_SIGMA[level]


# ============ 7.2 Reaction modifier -- two-parameter formula (baseline + depth-slope) ============
DEPTH_CENTRE = 3  # [canonical: combat_v32_proposal §7.2 -- Committed, the centre of depth one..five]
# reaction -> (baseline_r delta-sigma, slope_r delta-sigma/depth); positive delta-sigma = Defender advantaged.
REACTION_PARAMS = {
    "voiding":  (0.40, -0.35),  # [canonical: combat_v32_proposal §7.2 -- draft (punishes hesitation: strong vs probe, weak vs full)]
    "pressing": (0.30, -0.25),  # [canonical: combat_v32_proposal §7.2 -- draft (punishes hesitation: strong early, fades deep)]
    "hand_led": (0.00, -0.25),  # [canonical: combat_v32_proposal §7.2 -- draft (punishes hesitation: deflects light, can't stop deep)]
    "body_led": (0.10, 0.15),   # [canonical: combat_v32_proposal §7.2 -- draft (punishes overcommitment: needs depth to engage)]
    "yielding": (0.10, 0.35),   # [canonical: combat_v32_proposal §7.2 -- draft (punishes overcommitment: reversal vs full)]
}
REACTION_FAMILY = {
    "voiding": "punishes_hesitation", "pressing": "punishes_hesitation", "hand_led": "punishes_hesitation",
    "body_led": "punishes_overcommitment", "yielding": "punishes_overcommitment",
}  # [canonical: combat_v32_proposal §7.2 -- slope sign encodes the physical family]


def reaction_sigma(reaction, depth):
    """Reaction delta-sigma (§7.2) = baseline_r + slope_r * (depth - Committed-centre); depth in one..five.
    positive delta-sigma = Defender advantaged / raises Aggressor Ob."""
    baseline, slope = REACTION_PARAMS[reaction]
    return baseline + slope * (depth - DEPTH_CENTRE)


# ============ 7.3 / 6.11 Aspect coherence -- named sets + two antagonism exceptions ============
# Named loadout sets: core aspects + sigma-space set bonus (level, state-gate, sub-actions, optional condition).
NAMED_SETS = {
    "thrust_duelist": {"core": frozenset({"forward_point_stance", "linear_footwork", "standard_grip", "direct_explosive_approach", "kinetic_reading", "hand_led_reaction", "decisive_commitment", "clean_disengage"}),
                       "bonus_level": "moderate", "state": "closing", "applies_to": "thrust", "condition": None},                       # [canonical: combat_v32_proposal §6.11.2/§7.3 -- draft]
    "bind_fighter": {"core": frozenset({"centered_raised_stance", "linear_footwork", "standard_grip", "direct_press_approach", "tactile_reading", "patterned_anticipation", "yielding_reaction", "sustained_commitment"}),
                     "bonus_level": "moderate", "state": "in_bind", "applies_to": "wind_press_yield", "condition": None},               # [canonical: combat_v32_proposal §6.11.2/§7.3 -- draft]
    "counter_time": {"core": frozenset({"centered_side_stance", "linear_footwork", "drawing_approach", "kinetic_reading", "reactive_anticipation", "hand_led_reaction", "cautious_commitment"}),
                     "bonus_level": "strong", "state": "closing", "applies_to": "reactive", "condition": "reading_channel_succeeded"},  # [canonical: combat_v32_proposal §6.11.2/§7.3 -- draft (else +0)]
    "burst": {"core": frozenset({"bursting_footwork", "explosive_approach", "burst_commitment", "sudden_disengage"}),
              "bonus_level": "strong", "state": "opening_closing_transition", "applies_to": "transition", "condition": None},          # [canonical: combat_v32_proposal §6.11.2/§7.3 -- draft (no In-bind bonus)]
    "continuous_flow": {"core": frozenset({"side_stance_flux", "triangular_footwork", "paired_grip", "angled_approach", "rhythmic_reading", "voiding_reaction", "sustained_commitment", "sudden_disengage"}),
                        "bonus_level": "moderate", "state": "consecutive", "applies_to": "voiding_flow", "condition": None, "inherent_tension": "commitment_disengage"},  # [canonical: combat_v32_proposal §6.11.2/§7.3 -- draft (Paired short required)]
}
# Partial credit (N4): full set = stated bonus; near-set (one core missing) = one level lower; fewer = none.
SET_BONUS_DOWNGRADE = {"strong": "moderate", "moderate": "minor", "minor": "none", "none": "none"}  # [canonical: combat_v32_proposal §6.11.2 -- N4 cliff smoothing]
# Two antagonism exceptions -- the ONLY coherence penalties; no general pair matrix.
ANTAGONISMS = [frozenset({"anticipation", "reaction"}), frozenset({"commitment", "disengage"})]  # [canonical: combat_v32_proposal §6.11.3/§7.3 -- draft]


def set_bonus(set_name, equipped_aspects, channel_succeeded=False):
    """Resolve a named set's sigma-space bonus given equipped aspects (partial credit per the coherence rules).
    Returns (level, delta-sigma). Full set = stated level; near-set (exactly one core missing) =
    one level lower; fewer = none. Counter-time's bonus is conditional on a Reading channel succeeding."""
    spec = NAMED_SETS[set_name]
    missing = spec["core"] - set(equipped_aspects)
    if len(missing) == 0:
        level = spec["bonus_level"]
    elif len(missing) == 1:
        level = SET_BONUS_DOWNGRADE[spec["bonus_level"]]
    else:
        level = "none"
    if spec.get("condition") == "reading_channel_succeeded" and not channel_succeeded:
        level = "none"
    dsig = 0.0 if level == "none" else LEVEL_SIGMA[level]
    return level, dsig


def antagonism_penalty(active_aspect_families):
    """-Moderate (delta-sigma -0.5) per antagonistic pair both co-firing on a sub-action (§7.3 (b)).
    Returns the total delta-sigma penalty (<= 0). No general pair matrix -- only these two exceptions."""
    fams = set(active_aspect_families)
    pen = 0.0
    for pair in ANTAGONISMS:
        if pair <= fams:
            pen -= LEVEL_SIGMA["moderate"]
    return pen


# ================================= self-test =================================
if __name__ == "__main__":
    M = STANCE_COUNTER_MATRIX
    checks = []
    rule = "================================================================"
    print("Module five (M5) -- stance counter / reaction / coherence -- validation against §7")
    print(rule)

    # (a) Stance matrix: anti-symmetry + zero diagonal (§7.1 structural invariants)
    asym = all(M[a][b] == -M[b][a] for a in STANCES for b in STANCES)
    diag = all(M[s][s] == 0 for s in STANCES)
    checks.append(asym and diag)
    print(f"\n(a) Stance matrix anti-symmetric ([A][B]=-[B][A]) + zero diagonal: {'OK' if asym and diag else 'FAIL'}")

    # (b) the two hard counters (both involve Forward-point) + the worked-example cell
    cells = (M["forward_point"]["centered"] == -2 and M["centered"]["forward_point"] == 2
             and M["side"]["forward_point"] == -2)
    checks.append(cells)
    print(f"(b) hard counters (Forward-point vs Centered -2; Side vs Forward-point -2): {'OK' if cells else 'FAIL'}")

    # (c) stance_counter_sigma: sign convention + |1|->Moderate, |2|->Strong (reuses M1 LEVEL_SIGMA)
    sc_fp = stance_counter_sigma("forward_point", "centered")  # aggressor advantaged (worked example)
    sc_cr = stance_counter_sigma("centered", "raised")         # defender advantaged
    sc_ok = (sc_fp == -LEVEL_SIGMA["strong"] and sc_cr == LEVEL_SIGMA["moderate"]
             and stance_counter_sigma("low", "low") == 0)
    checks.append(sc_ok)
    print(f"(c) stance->sigma (FP/Centered {sc_fp}=-Strong aggressor; Centered/Raised {sc_cr}=+Moderate defender): {'OK' if sc_ok else 'FAIL'}")

    # (d) Reaction families: slope sign behaviour (the §7.2 physical claim), not the draft magnitudes
    v1, v5 = reaction_sigma("voiding", 1), reaction_sigma("voiding", 5)
    y1, y5 = reaction_sigma("yielding", 1), reaction_sigma("yielding", 5)
    hl = reaction_sigma("hand_led", DEPTH_CENTRE)
    react_ok = (v1 > 0 > v5 and v1 > v5        # Voiding: strong vs probe, weak vs full (slope < 0)
                and y5 > 0 > y1 and y5 > y1    # Yielding: reversal vs full, weak vs light (slope > 0)
                and hl == 0)                   # Hand-led: neutral at Committed centre
    checks.append(react_ok)
    print(f"(d) Reaction families (Voiding probe>0>full; Yielding full>0>light; Hand-led 0 at Committed): {'OK' if react_ok else 'FAIL'}")

    # (e) Named-set partial credit (N4): full / near-set (one lower) / fewer (none) + conditional set
    TD = NAMED_SETS["thrust_duelist"]["core"]
    full = set_bonus("thrust_duelist", TD)[0]
    near = set_bonus("thrust_duelist", set(list(TD)[1:]))[0]    # exactly one core missing
    fewer = set_bonus("thrust_duelist", set(list(TD)[2:]))[0]   # two missing
    CT = NAMED_SETS["counter_time"]["core"]
    ct_on = set_bonus("counter_time", CT, channel_succeeded=True)[0]
    ct_off = set_bonus("counter_time", CT, channel_succeeded=False)[0]
    set_ok = (full == "moderate" and near == "minor" and fewer == "none"
              and ct_on == "strong" and ct_off == "none")
    checks.append(set_ok)
    print(f"(e) set partial credit (full moderate / near {near} / fewer {fewer}; Counter-time on {ct_on}/off {ct_off}): {'OK' if set_ok else 'FAIL'}")

    # (f) Antagonisms: -Moderate per co-firing pair; only the two exceptions exist (no general matrix)
    ap_both = antagonism_penalty({"anticipation", "reaction", "commitment", "disengage"})
    ap_one = antagonism_penalty({"anticipation", "reaction"})
    ap_none = antagonism_penalty({"stance", "footwork"})
    antag_ok = (ap_both == -2 * LEVEL_SIGMA["moderate"] and ap_one == -LEVEL_SIGMA["moderate"]
                and ap_none == 0 and len(ANTAGONISMS) == 2)
    checks.append(antag_ok)
    print(f"(f) antagonisms (both pairs {ap_both}=-2*Moderate; one {ap_one}=-Moderate; none 0; exactly 2 exceptions): {'OK' if antag_ok else 'FAIL'}")

    print("\n" + rule)
    bad = [i for i, c in enumerate(checks) if not c]
    if bad:
        print(f"RESULT: FAIL -- check indices failing: {bad}")
        raise SystemExit(1)
    print(f"RESULT: PASS -- all {len(checks)} checks match §7 "
          f"(stance anti-symmetry + sign, reaction families, set partial credit, antagonism exceptions).")
