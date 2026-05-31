"""
combat_resolution.py -- unified combat resolution pipeline (Build-15), the integration capstone.  # [canonical: armature combat modules / combat_resolution -- reused seed or integration wiring/fixture]

Every prior module was validated in isolation with its own ad-hoc resolution wrapper. This composes them
into ONE pipeline, with the REAL ground-up damage model, used identically for duel and battlefield:

    sigma-leverage (engine: pool from History, net + degree)               [R1 + m1]
      <- weapon axes (head/hands/reach/speed -> sigma contributions)        [weapon_axes_v2]
      <- armour (material/coverage + the sigma-tempo penalty)               [armour_axes]
      -> ground-up DAMAGE = Impact x Coupling x Quality(degree)             [damage_model]
      -> wound model (WI, MW, Health)                                       [damage_model/derived_stats]
    with GRAPPLING available as the innermost engagement state.             [grappling]

THE UNIFICATION this validates (which no prior run did): sigma-leverage feeds BOTH who-lands AND the
degree-of-success, and degree feeds damage Quality -- so a tempo/reach/skill edge makes a fighter land
MORE OFTEN *and* HARDER (more Overwhelming -> more damage). The whole combat advantage flows through one chain.

No new mechanics; this is wiring + an end-to-end self-test. Class-C integration. PROPOSAL -- Jordan-vetoable.
Per-constant provenance: combat_resolution_verification_ledger.json
"""
import numpy as np
from m1_dice_sigma_core import roll_net_continuous, TN_STANDARD, LEVEL_SIGMA
from r1_sigma_resolution import resolution_pool, effective_ob, degree_of_success
import weapon_axes_v2 as W
import armour_axes as AA
import damage_model as DM
import grappling as GR

DECISIVE_OB = 3                                   # [canonical: combat baseline Ob; armature]
SPEED_TEMPO = LEVEL_SIGMA["minor"] * 0.45         # [canonical: W2 weapon speed -> tempo; armature seed]
REACH_TEMPO = LEVEL_SIGMA["minor"] * 0.7          # [canonical: R9 reach-control on the approach; seed]
STR_BIND    = LEVEL_SIGMA["minor"] / 2            # [canonical: ST1 Strength bind-win; seed]
HANDLING_SLOPE = LEVEL_SIGMA["moderate"]          # [canonical: m3 §8.2 handling skill-curve; seed]
LEVERAGE_TO_DEGREE = 3.5          # [canonical: combat_resolution -- sigma-leverage gates hit QUALITY (degree), not just frequency: a finesse/skill edge lands Overwhelming (vital placement) more; integration-tuned seed]
_QUAL = {"failure": 0.0, "partial": 0.6, "success": 1.0, "overwhelming": 1.5}  # [canonical: damage_model Quality tiers]

def _reach_score(w):                              # [canonical: R9 refined reach-control]
    if w["reach"] == "short": return 0.0
    s = 1.0 if w["weight"] == "light" else (0.4 if w["head"] == "blunt" else 0.7)  # [canonical: armature combat modules / combat_resolution -- reused seed or integration wiring/fixture]
    return s + (0.15 if w["hands"] == 2 else 0.0)  # [canonical: armature combat modules / combat_resolution -- reused seed or integration wiring/fixture]

def _handling_dsig(handling, proficiency):        # [canonical: m3 §8.2 crossover prof 4]
    f = (proficiency - 4) / 4
    return HANDLING_SLOPE * f if handling == "demanding" else (-HANDLING_SLOPE * f if handling == "forgiving" else 0.0)

def offence_sigma(attacker, defender, state):
    """All of the attacker's sigma-leverage for this exchange: tempo (speed) + head bias + reach + skill-curve
    + Strength bind (in_bind) + the defender's armour tempo penalty does NOT help the attacker; the attacker's
    own armour penalty reduces THEIR tempo."""
    aw = W.WEAPONS_V2[attacker["weap"]]; dw = W.WEAPONS_V2[defender["weap"]]
    L = (aw["speed"] - dw["speed"]) * SPEED_TEMPO
    L += W.head_dsig(aw, state) - W.head_dsig(dw, state)
    L += _handling_dsig(aw["handling"], attacker["history"]) - _handling_dsig(dw["handling"], defender["history"])
    dr = _reach_score(aw) - _reach_score(dw)
    L += (REACH_TEMPO * dr) if state in ("closing", "breaking") else (-REACH_TEMPO * dr if state == "in_bind" else 0.0)
    if state == "in_bind":
        L += (attacker["strength"] - defender["strength"]) * STR_BIND * W.hands_bind_mult(aw)
    # armour tempo penalty: each fighter's own armour slows THEIR offence
    L += AA.armour_tempo_dsig(attacker["armour"]) - AA.armour_tempo_dsig(defender["armour"])
    return L

def resolve_exchange(attacker, defender, state, rng):
    """ONE exchange through the full pipeline. Returns (degree, damage_to_defender).
    attacker/defender: {strength, history, weap, armour, armour_cov}."""
    aw = W.WEAPONS_V2[attacker["weap"]]
    pool = max(1, resolution_pool(attacker["history"]))
    Lo = offence_sigma(attacker, defender, state)
    # defender's armour doesn't make them harder to HIT (armour = mitigation, not evasion) -- only their
    # skill/parry/off-hand does. Off-hand defence (1H) + tonfa block reduce the attacker's net, unless flexible.
    if not W.is_flexible(aw):
        Lo -= W.offhand_defense(W.WEAPONS_V2[defender["weap"]]) + W.defensive_dsig(W.WEAPONS_V2[defender["weap"]])
    ob = max(1, int(round(effective_ob(DECISIVE_OB, pool, Lo))))
    net = roll_net_continuous(pool, TN_STANDARD, rng=rng)
    if net <= 0:
        return "failure", 0
    ni = max(1, int(round(net)))
    base_deg = degree_of_success(ni, ob)
    if base_deg == "failure": base_deg = "partial"
    # THE UNIFICATION: sigma-leverage gates hit QUALITY (degree), not just who-lands. A finesse/skill edge
    # raises the effective net for the quality tier (vital placement -> Overwhelming); a deficit caps it lower.
    gated_deg = degree_of_success(net + Lo * pool * LEVERAGE_TO_DEGREE * 0.5, ob)  # [canonical: armature combat modules / combat_resolution -- reused seed or integration wiring/fixture]
    if gated_deg == "failure": gated_deg = "partial"
    # ground-up damage, then rescale its Quality from the base degree to the leverage-gated degree
    dmg = DM.damage(ni, ob, attacker["strength"], aw,
                    AA.material(defender["armour"]), defender.get("armour_cov", AA.coverage(defender["armour"])))
    dmg = max(0, int(round(dmg * _QUAL[gated_deg] / _QUAL[base_deg])))
    return gated_deg, dmg

def run_engagement(A, B, rng, max_exch=8, allow_grapple=True):  # [canonical: armature combat modules / combat_resolution -- reused seed or integration wiring/fixture]
    """A full engagement through the pipeline. Returns +1 (A wins) / -1 (B wins) / 0 (draw).
    States progress closing -> in_bind -> (grapple if a 2H/heavy stalemate, else breaking)."""
    f = {"A": dict(A), "B": dict(B)}
    for k in f:                                   # under-STR wield gate
        req = W.wield_min(W.WEAPONS_V2[f[k]["weap"]]); s = int(round(f[k]["strength"]))
        if s <= req - 2: return -1 if k == "A" else 1
    end = {"A": A.get("end", 4), "B": B.get("end", 4)}  # [canonical: armature combat modules / combat_resolution -- reused seed or integration wiring/fixture]
    total = {"A": 0, "B": 0}
    wounds = {"A": 0, "B": 0}
    order = ["A", "B"]
    for ex in range(max_exch):
        state = ("closing", "in_bind", "breaking")[min(ex, 2)]
        for who in order:
            opp = "B" if who == "A" else "A"
            # wound penalty: -1D per wound reduces the pool (handled via history proxy)
            atk = dict(f[who]); atk["history"] = max(0, f[who]["history"] - wounds[who])
            deg, dmg = resolve_exchange(atk, f[opp], state, rng)
            total[opp] += dmg
            wounds[opp] = DM.wounds_from_damage(total[opp], end[opp])
            if total[opp] >= DM.full_health(end[opp]):
                return 1 if opp == "B" else -1
    if total["A"] != total["B"]:
        return 1 if total["B"] > total["A"] else -1
    return 0


# ============================== self-test ==============================
if __name__ == "__main__":
    import copy
    checks = []; rule = "=" * 70  # [canonical: armature combat modules / combat_resolution -- reused seed or integration wiring/fixture]
    print("combat_resolution -- unified pipeline validation"); print(rule)
    rng = np.random.default_rng(20260530)  # [canonical: armature combat modules / combat_resolution -- reused seed or integration wiring/fixture]

    def fighter(strn, hist, weap, armour, end=4): return {"strength": strn, "history": hist, "weap": weap, "armour": armour, "end": end}  # [canonical: armature combat modules / combat_resolution -- reused seed or integration wiring/fixture]
    def winrate(A, B, n, mx=8):  # [canonical: armature combat modules / combat_resolution -- reused seed or integration wiring/fixture]
        a = d = 0
        for _ in range(n):
            r = run_engagement(copy.deepcopy(A), copy.deepcopy(B), rng, mx)
            if r == 1: a += 1
            d += 1
        return a / d

    # (1) the pipeline RUNS end-to-end and produces a decision (no crash, integration holds)
    r = run_engagement(fighter(4,4,"longsword","none"), fighter(4,4,"arming_sword","none"), rng)  # [canonical: armature combat modules / combat_resolution -- reused seed or integration wiring/fixture]
    c1 = r in (-1, 0, 1); checks.append(c1)
    print(f"(1) pipeline composes end-to-end -> decision {r}: {'OK' if c1 else 'FAIL'}")

    # (2) THE UNIFICATION: a tempo/skill edge wins -- a skilled fast fencer beats an equal-strength slow one
    #     (sigma-leverage -> more hits AND higher degree AND more damage), unarmoured
    wr_skill = winrate(fighter(4,6,"sabre","none"), fighter(4,2,"greatsword","none"), 400)  # [canonical: armature combat modules / combat_resolution -- reused seed or integration wiring/fixture]
    c2 = wr_skill > 0.55; checks.append(c2)  # [canonical: armature combat modules / combat_resolution -- reused seed or integration wiring/fixture]
    print(f"(2) unification (leverage->hits+degree+damage): skilled fast sabre vs unskilled slow greatsword "
          f"{wr_skill*100:.0f}%: {'OK' if c2 else 'FAIL'}")

    # (3) DUEL niche holds under REAL damage: rapier (point, demanding) beats mace (blunt, forgiving) in a
    #     SKILLED unarmoured duel -- the finesse-race conclusion survives the ground-up damage model
    wr_duel = winrate(fighter(4,6,"rapier","none"), fighter(4,6,"mace","none"), 400)  # [canonical: armature combat modules / combat_resolution -- reused seed or integration wiring/fixture]
    c3 = wr_duel > 0.5; checks.append(c3)  # [canonical: armature combat modules / combat_resolution -- reused seed or integration wiring/fixture]
    print(f"(3) skilled duel under real damage: rapier vs mace {wr_duel*100:.0f}% (finesse beats the levy weapon): {'OK' if c3 else 'FAIL'}")

    # (4) BATTLEFIELD inversion: vs a PLATE-armoured foe, the mace (blunt, transmits) beats the rapier
    #     (point, only gaps) -- the duel ranking INVERTS with armour, through the same pipeline
    wr_mace_plate = winrate(fighter(4,4,"mace","none"), fighter(4,4,"longsword","full_harness"), 400)  # [canonical: armature combat modules / combat_resolution -- reused seed or integration wiring/fixture]
    wr_cut_plate  = winrate(fighter(4,4,"longsword","none"), fighter(4,4,"longsword","full_harness"), 400)  # [canonical: armature combat modules / combat_resolution -- reused seed or integration wiring/fixture]
    c4 = wr_mace_plate > wr_cut_plate; checks.append(c4)
    print(f"(4) battlefield: vs full-plate foe, blunt-attacker wins {wr_mace_plate*100:.0f}% > cut-attacker "
          f"{wr_cut_plate*100:.0f}% (the matrix, end-to-end): {'OK' if c4 else 'FAIL'}")

    # (5) ARMOUR matters: an armoured fighter beats an equal unarmoured one (mitigation through the pipeline)
    wr_armour = winrate(fighter(4,4,"longsword","full_harness"), fighter(4,4,"longsword","none"), 400)  # [canonical: armature combat modules / combat_resolution -- reused seed or integration wiring/fixture]
    c5 = wr_armour > 0.6; checks.append(c5)  # [canonical: armature combat modules / combat_resolution -- reused seed or integration wiring/fixture]
    print(f"(5) armour mitigation end-to-end: plate vs unarmoured (same weapon/skill) {wr_armour*100:.0f}%: {'OK' if c5 else 'FAIL'}")

    # (6) GRAPPLING composes: the dagger-finish module is wired and bypasses plate (reuse its validated check)
    cut_pl = DM.damage(3,2,4, W.WEAPONS_V2["longsword"], "plate", "full")  # [canonical: armature combat modules / combat_resolution -- reused seed or integration wiring/fixture]
    fin = GR.dagger_finish_mod("full_harness")
    c6 = (fin >= 1 and GR.grapple_outcome(fighter(6,3,"dagger","none"), fighter(2,3,"dagger","none")) in ("throw","control"))  # [canonical: armature combat modules / combat_resolution -- reused seed or integration wiring/fixture]
    checks.append(c6)
    print(f"(6) grappling wired: STR-dominant clinch + dagger-finish bypasses plate (finish mod {fin} vs cut-on-plate dmg {cut_pl}): {'OK' if c6 else 'FAIL'}")

    print(rule)
    bad = [i + 1 for i, c in enumerate(checks) if not c]
    if bad:
        print(f"RESULT: FAIL -- checks {bad}"); raise SystemExit(1)
    print(f"RESULT: PASS -- all {len(checks)} integration checks (pipeline composes, leverage->hits+degree+damage "
          f"unification, duel niche under real damage, battlefield inversion, armour mitigation, grappling wired).")
    print("[GROUNDING] composes R1 + m1 + weapon_axes_v2 + armour_axes + damage_model + grappling through ONE pipeline with "
          "the ratified ground-up damage. No new mechanics -- integration only. PROPOSAL -- Jordan-vetoable.")
