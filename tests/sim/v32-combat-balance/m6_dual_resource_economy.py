"""
m6_dual_resource_economy.py -- Module six (M6) of the v32 combat-balance sim (dual-resource economy).

The stateful Stamina + Concentration economy for a combat pass. Composes the maxima from M2
(Endurance-scaled Stamina, Focus-scaled Concentration), the commit-depth costs and recovery from M4a,
and adds the rest of the v32 drain table: movement costs, per-sub-action costs, passive armour drain,
and the per-exchange Concentration cost. Reports the threshold bands for both pools (Out-of-Breath /
Spent and the fractional warning bands) and classifies the dual-resource shape a build produces
(Stamina-fast vs Concentration-vulnerable).

Boundary with M4a: M4a owns commit-depth cost + chain cap + wound ceiling + disengage cost + recovery
formula (the bout-control surface). M6 owns the stateful pools, the full per-action drain accounting,
the threshold-band reporting, and the dual-resource characterization (the economy surface).

ResourceState is the tracker: init at max, spend per action, recover at end-of-pass, query bands.

Constant provenance: tests/sim/v32-combat-balance/m6_verification_ledger.json
  Class A = canonical (derived_stats armour drain, per-exchange Concentration, Out-of-Breath / Spent).
  Class B = v32 draft drain costs + threshold fractions (proposal dual-resource sections); sim-tunable.
"""
import numpy as np
from m2_attribute_pool_builder import stamina as max_stamina, concentration as max_concentration
from m4a_bout_state_graph import (DEPTH_TABLE,
                                   DISENGAGE_CLEAN_STAMINA, DISENGAGE_DEFENSIVE_STAMINA, DISENGAGE_SUDDEN_STAMINA,
                                   STAMINA_RECOVERY_MULT, OUT_OF_BREATH_PENALTY)

# ===== Class A: canonical resource anchors (derived_stats §4.2 / §5.2) =====
CONCENTRATION_PER_EXCHANGE = 3   # [canonical: derived_stats_v30 §5.2 (Concentration -3 per exchange)]
SPENT_PENALTY = 2                # [canonical: derived_stats_v30 §5.2 (Concentration Spent at 0: -2D, resets to max)]
ARMOR_PASSIVE_DRAIN = {"none": 0, "light": 0, "medium": 1, "heavy": 2}  # [canonical: derived_stats_v30 §4.2 (armour Stamina drain)]

# ===== Class B: v32 drain table + threshold bands (combat_v32_proposal §11.5/§11.6 -- draft) =====
MOVEMENT_STAMINA = {"direct_press": 0, "drawing": 0, "feinted": 0, "angled": 1, "explosive": 3}  # [canonical: combat_v32_proposal §11.5 -- draft (Phase 3 movement)]
SUBACTION_STAMINA = {"cut": 1, "thrust": 1, "yield": 1, "void": 1, "press": 2, "wind": 2, "displace": 2, "grip_change": 3}  # [canonical: combat_v32_proposal §11.5 -- draft (Phase 6 per step)]
# Threshold bands as fraction of max (effects sim-tunable):
STAMINA_THRESHOLDS = {"chain_compress": 0.30, "depth_drop": 0.20, "probe_only": 0.10}  # [canonical: combat_v32_proposal §11.5 -- draft (<30% chain-1, <20% depth ceiling-1, <10% probe/prep)]
CONCENTRATION_THRESHOLDS = {"reading_penalty": 0.30, "depth_drop": 0.20, "no_bout": 0.10}  # [canonical: combat_v32_proposal §11.4 -- draft (<30% Reading-1D+oppOb, <20% depth-1, <10% no Bout)]
CONCENTRATION_OPP_OB = 0.5  # [canonical: combat_v32_proposal §11.4 -- draft (<30% Concentration: opponent +0.5 Ob)]


def movement_stamina(approach):
    """Phase 3 movement Stamina cost (§11.5 draft)."""
    return MOVEMENT_STAMINA[approach]


def sub_action_stamina(subaction):
    """Phase 6 Bout per-step Stamina cost (§11.5 draft)."""
    return SUBACTION_STAMINA[subaction]


def armor_drain(armor_tier):
    """Passive Stamina drain per round from armour (canonical derived_stats §4.2)."""
    return ARMOR_PASSIVE_DRAIN[armor_tier]


def stamina_threshold_band(current, maximum):
    """Stamina threshold band for the current pool. out_of_breath at 0; then the fractional bands
    probe_only / depth_drop / chain_compress / ok (lowest pool to highest)."""
    if current <= 0:
        return "out_of_breath"                       # -2D all combat rolls (OUT_OF_BREATH_PENALTY)
    frac = current / maximum
    if frac < STAMINA_THRESHOLDS["probe_only"]:
        return "probe_only"                          # Commit at probe/preparatory depths only
    if frac < STAMINA_THRESHOLDS["depth_drop"]:
        return "depth_drop"                          # Commit depth ceiling drops
    if frac < STAMINA_THRESHOLDS["chain_compress"]:
        return "chain_compress"                      # Bout chain max compresses
    return "ok"


def concentration_threshold_band(current, maximum):
    """Concentration threshold band. spent at 0; then no_bout / depth_drop / reading_penalty / ok
    (lowest pool to highest)."""
    if current <= 0:
        return "spent"                               # -2D all combat rolls; resets to max
    frac = current / maximum
    if frac < CONCENTRATION_THRESHOLDS["no_bout"]:
        return "no_bout"                             # cannot enter Bout; Disengage forced
    if frac < CONCENTRATION_THRESHOLDS["depth_drop"]:
        return "depth_drop"                          # Commit depth ceiling drops
    if frac < CONCENTRATION_THRESHOLDS["reading_penalty"]:
        return "reading_penalty"                     # Reading -1D; opponent +CONCENTRATION_OPP_OB Ob
    return "ok"


class ResourceState:
    """A fighter's Stamina + Concentration pools across a pass (the dual-resource economy).
    Init at max (M2); spend per action (M4a commit/disengage + M6 movement/sub-action/armour/exchange);
    recover at end-of-pass (M4a Take a Breath + Focus); query the threshold bands."""

    def __init__(self, end, focus, history=0):
        self.end = end
        self.focus = focus
        self.history = history
        self.stamina_max = max_stamina(end)
        self.concentration_max = max_concentration(focus)
        self.stamina = self.stamina_max
        self.concentration = self.concentration_max

    def spend_commit(self, depth):
        """Commit (M4a DEPTH_TABLE): deduct the depth's Stamina + Concentration cost."""
        d = DEPTH_TABLE[depth]
        self.stamina = max(0, self.stamina - d["stamina"])
        self.concentration = max(0, self.concentration - d["concentration"])
        return d

    def spend_movement(self, approach):
        self.stamina = max(0, self.stamina - movement_stamina(approach))

    def spend_subaction(self, subaction):
        self.stamina = max(0, self.stamina - sub_action_stamina(subaction))

    def spend_disengage(self, kind):
        cost = {"clean": DISENGAGE_CLEAN_STAMINA, "defensive": DISENGAGE_DEFENSIVE_STAMINA,
                "sudden": DISENGAGE_SUDDEN_STAMINA}[kind]
        self.stamina = max(0, self.stamina - cost)

    def apply_armor_drain(self, armor_tier):
        self.stamina = max(0, self.stamina - armor_drain(armor_tier))

    def spend_exchange_concentration(self):
        """Per-exchange Concentration drain (canonical derived_stats §5.2)."""
        self.concentration = max(0, self.concentration - CONCENTRATION_PER_EXCHANGE)

    def recover(self):
        """Phase 8 Return (§4.9): Stamina +(End+History)*recovery-mult (M4a Take a Breath); Concentration +Focus."""
        self.stamina = min(self.stamina_max, self.stamina + (self.end + self.history) * STAMINA_RECOVERY_MULT)
        self.concentration = min(self.concentration_max, self.concentration + self.focus)
        return self.stamina, self.concentration

    def stamina_band(self):
        return stamina_threshold_band(self.stamina, self.stamina_max)

    def concentration_band(self):
        return concentration_threshold_band(self.concentration, self.concentration_max)


# ===== §11.6 dual-resource asymmetry — distinct combat shapes by build =====
DUAL_RESOURCE_SHAPES = {
    "burst": "Stamina-fast (Bursting Footwork + Burst Commitment); must end engagement quickly or disengage",
    "sustained": "Stamina-economical but Concentration-vulnerable in long engagements",
    "counter_time": "high Concentration cost per engagement (Pre-empt + attention splits); conserves Stamina",
}  # [canonical: combat_v32_proposal §11.6 -- distinct combat shapes]


def dominant_drain(rs):
    """Which pool a build/sequence drained harder (dual-resource asymmetry), by fraction remaining.
    Returns 'stamina' (Stamina more depleted), 'concentration', or 'balanced'."""
    sf = rs.stamina / rs.stamina_max
    cf = rs.concentration / rs.concentration_max
    if sf < cf:
        return "stamina"
    if cf < sf:
        return "concentration"
    return "balanced"


# ================================= self-test =================================
if __name__ == "__main__":
    checks = []
    rule = "================================================================"
    print("Module six (M6) -- dual-resource economy -- validation against canon + §11")
    print(rule)

    # (a) max pools via M2 reproduce canonical derived_stats (End x5, Focus x3)
    rs = ResourceState(4, 3, history=2)
    a_ok = (rs.stamina_max == 20 and rs.concentration_max == 9)  # [canonical: derived_stats_v30 §4.2 (End4 x5=20) / §5.2 (Focus3 x3=9)]
    checks.append(a_ok)
    print(f"\n(a) max pools (End4 Stamina {rs.stamina_max}=20; Focus3 Concentration {rs.concentration_max}=9): {'OK' if a_ok else 'FAIL'}")

    # (b) commit-depth spend pulls from M4a DEPTH_TABLE (depth 3 = Standard = 5 Stamina, 1 Concentration)
    c = rs.spend_commit(3)
    b_ok = (c["stamina"] == 5 and rs.stamina == rs.stamina_max - 5 and rs.concentration == rs.concentration_max - 1)  # [canonical: combat_v32_proposal §4.6 / §11.5 (depth-3 Committed = canonical Standard 5)]
    checks.append(b_ok)
    print(f"(b) commit depth-3 spend via M4a (Stamina -{c['stamina']}=-5, Concentration -1): {'OK' if b_ok else 'FAIL'}")

    # (c) M6 drain costs: movement / sub-action / armour
    d_ok = (movement_stamina("explosive") == 3 and movement_stamina("direct_press") == 0
            and sub_action_stamina("cut") == 1 and sub_action_stamina("press") == 2 and sub_action_stamina("grip_change") == 3
            and armor_drain("heavy") == 2 and armor_drain("light") == 0)
    checks.append(d_ok)
    print(f"(c) drain costs (explosive 3 / cut 1 / press 2 / grip 3 / heavy-armour 2): {'OK' if d_ok else 'FAIL'}")

    # (d) threshold bands for both pools (Out-of-Breath / Spent + fractional bands)
    r2 = ResourceState(4, 3)
    bands = []
    for val, exp in [(0, "out_of_breath"), (1, "probe_only"), (3, "depth_drop"), (5, "chain_compress"), (20, "ok")]:  # [canonical: derived_stats_v30 §4.2 (full pool -> ok band)]
        r2.stamina = val
        bands.append(r2.stamina_band() == exp)
    r2.concentration = 0
    spent_ok = (r2.concentration_band() == "spent")
    r2.concentration = r2.concentration_max
    ok_ok = (r2.concentration_band() == "ok")
    e_ok = all(bands) and spent_ok and ok_ok
    checks.append(e_ok)
    print(f"(d) threshold bands (Stamina out_of_breath/probe_only/depth_drop/chain_compress/ok; Concentration spent/ok): {'OK' if e_ok else 'FAIL'}")

    # (e) recovery: Take a Breath +(End+History)*2 (M4a) + Focus, both capped (§4.9)
    r3 = ResourceState(6, 3, history=2)              # stamina_max 30, concentration_max 9
    r3.spend_commit(5); r3.spend_commit(5)           # Stamina 30->10, Concentration 9->1 (depth-5 = 10 stam / 4 conc)
    st, co = r3.recover()
    f_ok = (st == 26 and co == 4)  # [canonical: derived_stats_v30 §4.2 (Take a Breath (6+2)*2=16 -> 10+16=26) + Focus 3 -> 1+3=4]
    checks.append(f_ok)
    print(f"(e) recovery (Stamina {st}=26 uncapped; Concentration {co}=4): {'OK' if f_ok else 'FAIL'}")

    # (f) per-exchange Concentration drain (canonical -3) and cap on recovery
    r4 = ResourceState(4, 3)
    r4.spend_exchange_concentration()
    g_ok = (r4.concentration == r4.concentration_max - CONCENTRATION_PER_EXCHANGE)
    checks.append(g_ok)
    print(f"(f) per-exchange Concentration drain (-{CONCENTRATION_PER_EXCHANGE} per exchange): {'OK' if g_ok else 'FAIL'}")

    # (g) §11.6 dual-resource shape: Stamina-dominant (movement+cuts) vs Concentration-dominant (exchanges)
    burst = ResourceState(4, 3)
    burst.spend_movement("explosive"); burst.spend_subaction("cut"); burst.spend_subaction("cut")
    sus = ResourceState(4, 3)
    sus.spend_exchange_concentration(); sus.spend_exchange_concentration(); sus.spend_exchange_concentration()
    h_ok = (dominant_drain(burst) == "stamina" and dominant_drain(sus) == "concentration")
    checks.append(h_ok)
    print(f"(g) dual-resource shape (Burst->{dominant_drain(burst)} / Sustained-drain->{dominant_drain(sus)}): {'OK' if h_ok else 'FAIL'}")

    print("\n" + rule)
    bad = [i for i, c in enumerate(checks) if not c]
    if bad:
        print(f"RESULT: FAIL -- check indices failing: {bad}")
        raise SystemExit(1)
    print(f"RESULT: PASS -- all {len(checks)} checks match canon + §11 "
          f"(max pools, M4a commit spend, drain costs, threshold bands, recovery, per-exchange, dual-resource shape).")
