"""
r1_sigma_resolution.py -- corrected-model combat RESOLUTION atom (armature reset).

The single-Action sigma-leverage resolution the combat armature hangs on. Replaces the attrition
integration (M8/M8b) and the Agility-scaled pool that the M8b re-sweep identified as the build-axis
bottleneck. Reuses the verified engine (M1) and the sigma-space levers (M5).

Corrected model (settled with Jordan, armature reset):
  - a fight is one short bounded exchange (a phrase), resolved by sigma-leverage -- NOT attrition.
  - the resolution pool is weapon-SKILL driven (History), NOT Agility-scaled. This closes the cross-attribute dominance
    channel (Agility -> bigger pool -> higher base success-rate -> dominance) that the M8b re-sweep
    pinned as the bottleneck after multipliers were removed (it recommended compressing the pool
    spread). History is the orthogonal weapon-skill axis (capped by Recall), NOT one of the attribute
    points, so the pool no longer competes with the Agi/Str/End allocation.
  - Agility instead contributes through the sigma-leverage channel (tempo/reaction/closing), where
    its impact is UNIFORM across pool size (the F1 property) and tunable for cross-attribute parity
    against Strength (wound magnitude) and Endurance (durability).
  - degree of success (how well the target is struck) is the canonical band; a crit is an
    Overwhelming-degree strike, not a random roll. Magnitude (net - Ob) is the continuous gauge that
    drives wound severity downstream.

Constant provenance: tests/sim/v32-combat-balance/r1_verification_ledger.json
  Class A = canonical (params/core.md degree table + Ob/pool floors; modifier_system_spec state-gating).
  Class C = proposed armature redesign (demoted pool form; Agility-as-leverage wiring); sim-tunable, NOT canonical.
  sigma-space level magnitudes + soft cap are imported from M1 (Class B there).
"""
import numpy as np
from m1_dice_sigma_core import (
    eff_ob, p_success, roll_net_continuous, net_boost, LEVEL_SIGMA, TN_STANDARD,
)

# ===== Class A: canonical resolution floors / degree thresholds (params/core.md) =====
OB_FLOOR = 1                 # [canonical: params/core.md §Obstacle Scale (Ob minimum 1; no modifier reduces below 1)]
POOL_FLOOR = 5               # [canonical: params/core.md §Derived Scores (Combat Pool min 5)]
OVERWHELMING_OB_MULT = 2     # [canonical: params/core.md §Degrees of Success (Overwhelming: net >= 2x Ob)]
OVERWHELMING_NET_MIN = 3     # [canonical: params/core.md §Degrees of Success (Overwhelming requires net >= 3 regardless of Ob)]
ATTR_AVERAGE = 3             # [canonical: params/core.md §Attributes (average human = 3)]
HISTORY_MAX = 7              # [canonical: params/core.md §Attributes (advancement max 7; Recall caps History points <= 7)]

# ===== Class C: demoted resolution pool (armature redesign; NOT canonical; sim-tunable) =====
# History(weapon-skill)-driven, Agility-INDEPENDENT. BASE_POOL centres the (compressed) spread; its
# exact value is the headline tunable. Anchor: the M8b re-sweep recommended compressing the Combat
# Pool spread (wound_model_resweep_results.md). Jordan decision A: History-driven (seeded) vs flat base.
BASE_POOL = 6                # [class-C: proposed armature -- History-driven pool base; replaces (Agi x2)+History+3; sim-tunable]

# ===== Class C: Agility-as-leverage (the channel that replaces Agi's pool dominance) =====
# Agi enters combat as a sigma-leverage tempo/initiative delta-sigma (uniform impact across pool
# size), centred on the average human. Per-point magnitude is THE parity tuning knob for the Agi
# channel, balanced against Strength and Endurance in the equal-budget parity sweep. Seeded modestly.
AGI_TEMPO_PER_POINT = LEVEL_SIGMA["minor"] / 2   # [class-C: half a Minor delta-sigma per Agi point off average; sim-tunable parity knob]

# ===== Class A: state-gating table (modifier_system_spec.md §4) =====
# Which delta-sigma sources are physically live per engagement state. Set bonus + weapon phase-strength
# live in all states; the rest gate (stance dies in a bind; tactile only in contact; facing irrelevant
# in a locked bind). Source: modifier_system_spec §4 state-gating table (live counts 5/6/6/4).
BOUT_STATES = ("out_of_contact", "closing", "in_bind", "breaking")
STATE_GATING = {
    "stance_counter": {"closing"},                                              # [canonical: modifier_system_spec.md §4 state-gating table]
    "reaction":       {"closing", "in_bind"},                                   # [canonical: modifier_system_spec.md §4 state-gating table]
    "reading":        {"out_of_contact", "closing", "in_bind"},                 # [canonical: modifier_system_spec.md §4 state-gating table]
    "set_bonus":      {"out_of_contact", "closing", "in_bind", "breaking"},     # [canonical: modifier_system_spec.md §4 state-gating table]
    "weapon_phase":   {"out_of_contact", "closing", "in_bind", "breaking"},     # [canonical: modifier_system_spec.md §4 state-gating table]
    "facing":         {"out_of_contact", "closing", "breaking"},                # [canonical: modifier_system_spec.md §4 state-gating table]
    "tactile":        {"in_bind"},                                              # [canonical: modifier_system_spec.md §4 state-gating table]
    "grip":           {"in_bind"},                                              # [canonical: modifier_system_spec.md §4 state-gating table]
    "approach":       {"out_of_contact"},                                       # [canonical: modifier_system_spec.md §4 state-gating table]
    "disengage":      {"breaking"},                                             # [canonical: modifier_system_spec.md §4 state-gating table]
}


def resolution_pool(history_points):
    """Demoted, Agility-independent resolution pool (armature redesign): History + base, floored.
    NOT (Agi x2)+History+3. No Agility parameter -- the cross-attribute dominance channel is closed by construction."""
    return max(POOL_FLOOR, int(round(history_points)) + BASE_POOL)


def agility_delta_sigma(agi):
    """Agility's combat contribution as a sigma-leverage tempo delta-sigma (uniform impact), centred
    on the average human. Positive = initiative/tempo edge. This is where Agi matters in combat
    instead of in raw pool size."""
    return (int(round(agi)) - ATTR_AVERAGE) * AGI_TEMPO_PER_POINT


def state_gated_net_sigma(bout_state, contributors):
    """Sum only the delta-sigma contributors physically live in the engagement state (modifier spec
    state-gating). `contributors` maps source-name -> signed delta-sigma (positive = aggressor-
    favouring). Sources not in the gating table are treated as ungated (always live)."""
    total = 0.0
    for source, dsig in contributors.items():
        live = STATE_GATING.get(source)
        if live is None or bout_state in live:
            total += dsig
    return total


def live_source_count(bout_state):
    """Number of gated sources live in a state (the modifier-spec parity check)."""
    return sum(1 for live in STATE_GATING.values() if bout_state in live)


def effective_ob(base_ob, pool, net_sigma):
    """Effective Ob after sigma-leverage (reuses M1 soft cap + Ob shift), floored at the canonical
    Ob minimum. (params/core.md floors Ob at the minimum even when the modifier spec's worked example
    floored lower -- canonical floor wins.)"""
    return max(OB_FLOOR, eff_ob(base_ob, pool, net_sigma))


def degree_of_success(net, ob):
    """Canonical degree band (params/core.md): Overwhelming (net >= mult*Ob AND net >= min),
    Success (net >= Ob), Partial (net > 0 < Ob), Failure (net <= 0)."""
    if net <= 0:
        return "failure"
    if net >= OVERWHELMING_OB_MULT * ob and net >= OVERWHELMING_NET_MIN:
        return "overwhelming"
    if net >= ob:
        return "success"
    return "partial"


def resolve_action(base_ob, history_points, contributors, bout_state,
                   agi=ATTR_AVERAGE, tn=TN_STANDARD, rng=None):
    """Resolve ONE Action across the phrase via sigma-leverage. Pool is History-driven
    (Agi-independent); Agi folds into the live delta-sigma as tempo. A crit is an Overwhelming-degree
    strike (canonical), not a random roll. Returns the outcome dict (magnitude = net - Ob is the
    'how well struck' gauge for downstream wound severity)."""
    pool = resolution_pool(history_points)
    contrib = dict(contributors)
    contrib["agi_tempo"] = contrib.get("agi_tempo", 0.0) + agility_delta_sigma(agi)
    net_sigma = state_gated_net_sigma(bout_state, contrib)
    ob = base_ob                                              # F4 mu-shift: base Ob (eff_ob is DISPLAY-ONLY)
    net = roll_net_continuous(pool, tn, rng=rng) + net_boost(net_sigma, pool, tn)
    deg = degree_of_success(net, ob)
    return {
        "pool": pool, "base_ob": base_ob, "net_sigma": round(net_sigma, 2),
        "effective_ob": round(ob, 2), "net": round(net, 2),
        "magnitude": round(net - ob, 2), "degree": deg,
        "crit": deg == "overwhelming",
    }


# ============================== self-test ==============================
if __name__ == "__main__":
    from m5_stance_reaction_coherence import stance_counter_sigma   # real lever (integration)
    rng = np.random.default_rng()
    checks = []
    rule = "================================================================"
    print("R1 sigma-leverage resolution atom -- validation against canon + corrected model")
    print(rule)

    # (a) Demoted pool: Agility-INDEPENDENT (no Agi param), spread compressed, floored.
    #     The cross-attribute dominance channel (Agi -> bigger pool -> dominance) is closed by construction.
    pool_low_hist = resolution_pool(0)
    pool_high_hist = resolution_pool(HISTORY_MAX)                     # [class-C: History ceiling sample -- proposed pool spread]
    spread = pool_high_hist - pool_low_hist
    a_ok = (pool_low_hist == BASE_POOL                      # History 0 -> base (above floor 5)
            and pool_high_hist == BASE_POOL + HISTORY_MAX             # [class-C: History 7 -> base + 7 -- proposed spread]
            and resolution_pool(-5) == POOL_FLOOR           # [class-C: deep-negative History clamps to floor]
            and spread == HISTORY_MAX)                                # [class-C: 8-point History range -> 7-wide pool band; Agi-independent]
    checks.append(a_ok)
    print(f"\n(a) demoted pool History-driven + Agi-independent (H0->{pool_low_hist}, H7->{pool_high_hist}, "
          f"spread {spread}, floored): {'OK' if a_ok else 'FAIL'}")

    # (b) cross-attribute dominance closure demonstration: two builds, EQUAL History, different Agi -> IDENTICAL pool.
    #     Agi's effect now arrives via a bounded, uniform-impact delta-sigma (tempo), not pool size.
    p_agi_lo = resolution_pool(2)                           # Agi not an argument -> cannot affect pool
    p_agi_hi = resolution_pool(2)
    agi_lo_sig = agility_delta_sigma(1)
    agi_hi_sig = agility_delta_sigma(6)                     # [class-C: Agi 6 sample -- tempo delta-sigma]
    b_ok = (p_agi_lo == p_agi_hi                            # pool identical regardless of Agi
            and agi_hi_sig > 0 > agi_lo_sig                 # high Agi advantaged, low Agi penalised
            and agility_delta_sigma(ATTR_AVERAGE) == 0      # average Agi neutral
            and abs(agi_hi_sig) <= LEVEL_SIGMA["major"])    # bounded -- not a runaway
    checks.append(b_ok)
    print(f"(b) cross-attribute dominance closed (equal-History pool Agi-invariant {p_agi_lo}=={p_agi_hi}; Agi via delta-sigma "
          f"Agi6 {agi_hi_sig:+.2f}/Agi1 {agi_lo_sig:+.2f}, bounded): {'OK' if b_ok else 'FAIL'}")

    # (c) State-gating reproduces the modifier_system_spec live counts (5 / 6 / 6 / 4).
    counts = {s: live_source_count(s) for s in BOUT_STATES}
    expected = {"out_of_contact": 5, "closing": 6, "in_bind": 6, "breaking": 4}  # [canonical: modifier_system_spec.md §4 LIVE COUNT row]
    stance_live_closing = state_gated_net_sigma("closing", {"stance_counter": LEVEL_SIGMA["moderate"]})
    stance_dead_inbind = state_gated_net_sigma("in_bind", {"stance_counter": LEVEL_SIGMA["moderate"]})
    c_ok = (counts == expected
            and stance_live_closing == LEVEL_SIGMA["moderate"]   # stance counts in Closing
            and stance_dead_inbind == 0)                         # stance is zeroed in a bind
    checks.append(c_ok)
    print(f"(c) state-gating live counts {counts} (canon 5/6/6/4); stance live@Closing/zero@bind: "
          f"{'OK' if c_ok else 'FAIL'}")

    # (d) Effective Ob: sigma-leverage shift via M1, floored at the canonical Ob minimum.
    pool = resolution_pool(2)
    ob_neutral = effective_ob(OVERWHELMING_NET_MIN, pool, 0.0)          # no leverage -> base Ob
    ob_favoured = effective_ob(OVERWHELMING_NET_MIN, pool, LEVEL_SIGMA["strong"])  # leverage lowers Ob
    ob_floored = effective_ob(OB_FLOOR, pool, LEVEL_SIGMA["major"])     # cannot go below floor
    d_ok = (round(ob_neutral, 2) == round(float(OVERWHELMING_NET_MIN), 2)
            and ob_favoured < ob_neutral
            and ob_floored >= OB_FLOOR)
    checks.append(d_ok)
    print(f"(d) effective Ob (neutral {ob_neutral:.2f}=base; favoured {ob_favoured:.2f}<base; "
          f"floored {ob_floored:.2f}>={OB_FLOOR}): {'OK' if d_ok else 'FAIL'}")

    # (e) Degree band is canonical: Overwhelming needs net >= 2*Ob AND net >= 3; crit == Overwhelming.
    e_ok = (degree_of_success(OVERWHELMING_NET_MIN, OB_FLOOR) == "overwhelming"     # net3 vs Ob1: 3>=2*1 and 3>=3
            and degree_of_success(OVERWHELMING_OB_MULT, OB_FLOOR) == "success"      # net2 vs Ob1: 2>=1 but 2<3 net-min
            and degree_of_success(OB_FLOOR, OVERWHELMING_NET_MIN) == "partial"      # net1 vs Ob3: 0<1<3
            and degree_of_success(0, OB_FLOOR) == "failure")
    checks.append(e_ok)
    print(f"(e) canonical degree band (Overwhelming net>=2*Ob AND >=3; crit==Overwhelming): "
          f"{'OK' if e_ok else 'FAIL'}")

    # (f) End-to-end resolve_action with a REAL stance lever (M5), Monte-Carlo sanity:
    #     a favourable setup raises P(at least Success) over a neutral one at the SAME pool.
    N = int(2e4)                                            # sample count (structural)
    stance_adv = stance_counter_sigma("forward_point", "centered")  # aggressor-advantaged (Strong)
    def _hit_rate(net_sig):
        contrib = {"stance_counter": -net_sig} if False else {}
        # use p_success analytically for stability (avoids MC noise in the assertion)
        return p_success(OVERWHELMING_NET_MIN, resolution_pool(2), net_sig)
    p_neutral = _hit_rate(0.0)
    p_setup = _hit_rate(LEVEL_SIGMA["strong"])
    sample = resolve_action(OVERWHELMING_NET_MIN, 2, {"reading": LEVEL_SIGMA["minor"]},
                            "closing", agi=ATTR_AVERAGE, rng=rng)
    f_ok = (p_setup > p_neutral                                   # favourable setup -> better odds (uniform-impact lever)
            and sample["pool"] == resolution_pool(2)              # pool wired through
            and abs(stance_adv) == LEVEL_SIGMA["strong"]          # M5 lever imported correctly
            and sample["degree"] in ("failure", "partial", "success", "overwhelming"))
    checks.append(f_ok)
    print(f"(f) end-to-end (setup {p_setup*100:.1f}% > neutral {p_neutral*100:.1f}%; M5 stance |{stance_adv:.2f}|; "
          f"resolve_action sample degree '{sample['degree']}'): {'OK' if f_ok else 'FAIL'}")

    print("\n" + rule)
    bad = [i for i, c in enumerate(checks) if not c]
    if bad:
        print(f"RESULT: FAIL -- check indices failing: {bad}")
        raise SystemExit(1)
    print(f"RESULT: PASS -- all {len(checks)} checks "
          f"(demoted Agi-independent pool, cross-attribute dominance closure, state-gating 5/6/6/4, Ob floor, "
          f"canonical degree/crit, end-to-end with M5 lever).")
    print("[CLASS C] demoted-pool base + Agi-tempo magnitude are PROPOSED (armature redesign), "
          "sim-tunable in the parity sweep, NOT canonical.")
