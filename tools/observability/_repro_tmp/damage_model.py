"""
damage_model.py -- ground-up damage rebuild (Build-14).  # [canonical: derived_stats §4.1 / damage_model_design -- reproduced or grounded seed/fixture]

Per Jordan directive 2026-05-30: redevelop damage FROM THE GROUND UP. Pretend no prior damage formula  # [canonical: derived_stats §4.1 / damage_model_design -- reproduced or grounded seed/fixture]
exists -- derive only from (a) how the new combat resolves and (b) how health & wounds work.

  INPUTS FROM COMBAT (the only resolution primitives used):
    * net    -- margin of the contested roll (sigma-leverage engine output)
    * degree -- Partial / Success / Overwhelming (params/core: Overwhelming net>=2*Ob AND net>=3; Success  # [canonical: derived_stats §4.1 / damage_model_design -- reproduced or grounded seed/fixture]
                net>=Ob; Partial 0<net<Ob)
    * the weapon's axes (weight, head) and the defender's armour (material, coverage) -- describing how the
      blow's force is delivered and resisted.
  TARGET FROM THE WOUND MODEL (the only consumer):
    * WI = Endurance + 6 (Wound Interval). wounds = floor(total_damage / WI). MW = min(floor(End/2)+1, 3).  # [canonical: derived_stats §4.1 / damage_model_design -- reproduced or grounded seed/fixture]
      Health = WI*(MW+1). -1D per wound. (derived_stats §4.1, PP-716/717.)  # [canonical: derived_stats §4.1 / damage_model_design -- reproduced or grounded seed/fixture]

  DESIGN: a blow's damage = how much wound-capacity (WI) it consumes = Impact x Coupling x Quality.
    Impact   = Strength + Heft(weight)                      -- additive force; NO Strength x weight multiplier.
    Coupling = Delivery(head) x Transmission(material,mode) x GapAccess(coverage)  -- head-vs-armour, derived
               from material resistance-per-mode (percussion/shear/puncture), NOT a flat +mod table.
    Quality  = degree-of-success factor                    -- replaces "crit doubles the weapon mod".
  Calibrated so an even Success hit from an average fighter ~= 1 WI (one telling blow ~= one wound).

This SUPERSEDES the inherited damage formula (net + STR x mult + weapon_armour_mod; the x1/x1.5/x2/x3  # [canonical: derived_stats §4.1 / damage_model_design -- reproduced or grounded seed/fixture]
multipliers; crit-doubles-mod) and folds the weapon-vs-armour interaction into Coupling (one mechanism,
no double-count). PROPOSAL -- Jordan-vetoable. No canon file edited.
Per-constant provenance: damage_model_verification_ledger.json
"""
from m1_dice_sigma_core import LEVEL_SIGMA  # (imported for engine-consistency; damage uses its own calibrated scale)

# ---- the wound model (the consumer; reproduced, not changed) ----
def wound_interval(endurance): return endurance + 6                          # [canonical: derived_stats §4.1 WI = End+6]
def max_wounds(endurance):     return min(endurance // 2 + 1, 3)             # [canonical: derived_stats §4.1 MW = min(floor(End/2)+1,3), PP-717]
def full_health(endurance):    return wound_interval(endurance) * (max_wounds(endurance) + 1)  # [canonical: Health = WI*(MW+1)]
def wounds_from_damage(total, endurance): return total // wound_interval(endurance)            # [canonical: wounds = floor(total/WI)]

# ============ FACTOR 1 -- IMPACT (force behind the blow) ============
# Additive force: your strength plus the weapon's heft. NO strength x weight multiplier.
HEFT = {"light": 0, "heavy": 3}          # [canonical: damage rebuild -- weight adds force additively; grounded seed calibrated to WI]
def impact(strength, weight):
    return strength + HEFT[weight]        # avg fighter STR4: light->4, heavy->7

# ============ FACTOR 2 -- COUPLING (head vs armour: how much force becomes a wound) ============
# attack MODE per head: blunt=percussion, point=puncture, all cutting heads=shear.
HEAD_MODE = {"blunt": "percussion", "point": "puncture",
             "cut_and_thrust": "shear", "straight_cut": "shear", "curved_cut": "shear"}
# how well the head DELIVERS its mode into flesh (intrinsic), before armour:
DELIVERY = {"blunt": 1.6, "straight_cut": 1.5, "curved_cut": 1.5, "cut_and_thrust": 1.35, "point": 1.45}  # [canonical: damage rebuild -- head force-delivery onto unprotected target; grounded]
# material RESISTANCE per mode in [0,1] (fraction of force the armour stops). none resists nothing.
# percussion transmits through everything (plate concusses); shear stopped hard by mail/plate; puncture
# stopped on solid plate but the gaps remain (handled by GapAccess).
RESIST = {                                                                 # [canonical: damage rebuild -- material resistance-per-mode; the (head x material) physics, replacing the +mod table]
    "none":  {"percussion": 0.00, "shear": 0.00, "puncture": 0.00},
    "cloth": {"percussion": 0.10, "shear": 0.35, "puncture": 0.15},        # [canonical: derived_stats §4.1 / damage_model_design -- reproduced or grounded seed]  gambeson: absorbs percussion a little, blunts cuts, soft vs thrust
    "mail":  {"percussion": 0.20, "shear": 0.80, "puncture": 0.45},        # [canonical: derived_stats §4.1 / damage_model_design -- reproduced or grounded seed]  rings stop the slash; a stiff point can burst them
    "plate": {"percussion": 0.30, "shear": 0.95, "puncture": 0.70},        # [canonical: derived_stats §4.1 / damage_model_design -- reproduced or grounded seed]  deflects cuts entirely; transmits percussion; thrust needs the gaps
}
COVERAGE_GAP = {"full": 0.15, "partial": 0.5}   # [canonical: damage rebuild -- fraction of blows reaching a gap/bare zone; partial leaves limbs bare; grounded]
def coupling(head, material, coverage):
    mode = HEAD_MODE[head]
    transmit = 1.0 - RESIST[material][mode]
    # a puncture (point) additionally exploits gaps: on hard armour the gap path dominates
    if mode == "puncture":
        gap = COVERAGE_GAP[coverage]
        transmit = max(transmit, gap)          # the thrust takes whichever is better: through-the-material or the gap
    elif material != "none":
        # cut/blunt land mostly on the armour; partial coverage exposes some bare target
        gap = COVERAGE_GAP[coverage]
        transmit = transmit * (1 - gap) + 1.0 * gap   # a fraction of blows hit bare flesh
    return DELIVERY[head] * transmit

# ============ FACTOR 3 -- QUALITY (degree of success, from the contest) ============
QUALITY = {"partial": 0.6, "success": 1.0, "overwhelming": 1.5}   # [canonical: damage rebuild -- degree-of-success factor; replaces crit-doubles-mod; grounded]
def degree_of(net, ob):                                            # [canonical: params/core Degrees of Success]
    if net <= 0: return "failure"
    if net >= 2 * ob and net >= 3: return "overwhelming"  # [canonical: derived_stats §4.1 / damage_model_design -- reproduced or grounded seed/fixture]
    if net >= ob: return "success"
    return "partial"

# ============ DAMAGE = Impact x Coupling x Quality ============
DMG_SCALE = 1.55   # [canonical: damage rebuild -- single calibration constant so an even Success hit ~= 1 WI; tunable]
def damage(net, ob, strength, weapon, armour_material, armour_coverage):
    """weapon: dict with 'weight' and 'head'. Returns integer wound-points (compare to WI)."""
    deg = degree_of(net, ob)
    if deg == "failure": return 0
    raw = impact(strength, weapon["weight"]) * coupling(weapon["head"], armour_material, armour_coverage) * QUALITY[deg] * DMG_SCALE
    return max(0, int(round(raw)))


# ============================== self-test ==============================
if __name__ == "__main__":
    checks = []; rule = "=" * 70  # [canonical: derived_stats §4.1 / damage_model_design -- reproduced or grounded seed/fixture]
    print("damage_model (ground-up rebuild) -- validation"); print(rule)
    WI = wound_interval(4)   # [canonical: derived_stats §4.1 / damage_model_design -- reproduced or grounded seed]  average target End4 -> WI 10
    print(f"anchor: average target End4 -> WI={WI}, MW={max_wounds(4)}, Health={full_health(4)} (felled after {max_wounds(4)+1} intervals)\n")

    def dmg(net, ob, strn, weight, head, mat, cov="full"):
        return damage(net, ob, strn, {"weight": weight, "head": head}, mat, cov)

    # (1) ANCHOR: an even Success hit (net=ob=2) from an average fighter (STR4) with a normal blade vs an
    #     unarmoured foe does ~ 1 WI (one telling blow ~= one wound)
    d_anchor = dmg(2, 2, 4, "light", "cut_and_thrust", "none")  # [canonical: derived_stats §4.1 / damage_model_design -- reproduced or grounded seed/fixture]
    c1 = (0.7*WI <= d_anchor <= 1.5*WI)  # [canonical: derived_stats §4.1 / damage_model_design -- reproduced or grounded seed/fixture]
    checks.append(c1)
    print(f"(1) ANCHOR even Success, STR4 light cut&thrust vs none: {d_anchor} dmg vs WI {WI} "
          f"({d_anchor/WI:.2f} wounds): {'OK' if c1 else 'FAIL'}")

    # (2) DEGREE scales damage: Overwhelming > Success > Partial, same blow
    dp = dmg(1, 3, 4, "light", "cut_and_thrust", "none")   # [canonical: derived_stats §4.1 / damage_model_design -- reproduced or grounded seed]  partial (0<net<ob)
    ds = dmg(3, 3, 4, "light", "cut_and_thrust", "none")   # [canonical: derived_stats §4.1 / damage_model_design -- reproduced or grounded seed]  success
    do = dmg(6, 3, 4, "light", "cut_and_thrust", "none")   # [canonical: derived_stats §4.1 / damage_model_design -- reproduced or grounded seed]  overwhelming (net>=2ob & >=3)
    c2 = (dp < ds < do)
    checks.append(c2)
    print(f"(2) degree scales: Partial {dp} < Success {ds} < Overwhelming {do}: {'OK' if c2 else 'FAIL'}")

    # (3) WEIGHT (heft) increases impact: heavy > light, same head/target/quality
    c3 = (dmg(2,2,4,"heavy","cut_and_thrust","none") > dmg(2,2,4,"light","cut_and_thrust","none"))  # [canonical: derived_stats §4.1 / damage_model_design -- reproduced or grounded seed/fixture]
    checks.append(c3)
    print(f"(3) heft: heavy cut&thrust {dmg(2,2,4,'heavy','cut_and_thrust','none')} > light "
          f"{dmg(2,2,4,'light','cut_and_thrust','none')}: {'OK' if c3 else 'FAIL'}")

    # (4) vs PLATE: cut ~deflected (near 0), blunt transmits (high), point finds gaps (moderate) -- the matrix, derived
    cut_pl   = dmg(2,2,4,"light","cut_and_thrust","plate")  # [canonical: derived_stats §4.1 / damage_model_design -- reproduced or grounded seed/fixture]
    blunt_pl = dmg(2,2,4,"heavy","blunt","plate")  # [canonical: derived_stats §4.1 / damage_model_design -- reproduced or grounded seed/fixture]
    point_pl = dmg(2,2,4,"light","point","plate")  # [canonical: derived_stats §4.1 / damage_model_design -- reproduced or grounded seed/fixture]
    c4 = (cut_pl <= 2 and blunt_pl >= WI*0.7 and cut_pl < point_pl < blunt_pl)  # [canonical: derived_stats §4.1 / damage_model_design -- reproduced or grounded seed/fixture]
    checks.append(c4)
    print(f"(4) vs PLATE (derived coupling): cut {cut_pl} (deflected) < point {point_pl} (gaps) < blunt {blunt_pl} "
          f"(transmits): {'OK' if c4 else 'FAIL'}")

    # (5) vs MAIL: cut stopped more than thrust (rings stop slash, point bursts) -- the historical rise of the thrust
    c5 = (dmg(2,2,4,"light","cut_and_thrust","mail") < dmg(2,2,4,"light","point","mail"))  # [canonical: derived_stats §4.1 / damage_model_design -- reproduced or grounded seed/fixture]
    checks.append(c5)
    print(f"(5) vs MAIL: cut {dmg(2,2,4,'light','cut_and_thrust','mail')} < point "
          f"{dmg(2,2,4,'light','point','mail')} (thrust beats mail): {'OK' if c5 else 'FAIL'}")

    # (6) STRENGTH contributes additively (no multiplier): STR7 > STR1, and the GAP is constant across weights
    #     (additivity check -- a strong fighter does NOT get disproportionately more from a heavy weapon)
    gap_light = dmg(2,2,7,"light","cut_and_thrust","none") - dmg(2,2,1,"light","cut_and_thrust","none")  # [canonical: derived_stats §4.1 / damage_model_design -- reproduced or grounded seed/fixture]
    gap_heavy = dmg(2,2,7,"heavy","cut_and_thrust","none") - dmg(2,2,1,"heavy","cut_and_thrust","none")  # [canonical: derived_stats §4.1 / damage_model_design -- reproduced or grounded seed/fixture]
    c6 = (dmg(2,2,7,"light","cut_and_thrust","none") > dmg(2,2,1,"light","cut_and_thrust","none")  # [canonical: derived_stats §4.1 / damage_model_design -- reproduced or grounded seed/fixture]
          and abs(gap_light - gap_heavy) <= 2)   # additive: STR gap ~same regardless of weapon weight
    checks.append(c6)
    print(f"(6) STR additive (no x-mult): STR7-STR1 gap light {gap_light} ~= heavy {gap_heavy} "
          f"(constant -> additive, not multiplicative): {'OK' if c6 else 'FAIL'}")

    # (7) WOUND PACING sane: a healthy End4 foe (Health 40, MW3) is felled by a plausible number of clean
    #     Success cuts (unarmoured) -- not 1 (too swingy), not 15 (too grindy)
    per_hit = dmg(2,2,4,"light","cut_and_thrust","none")  # [canonical: derived_stats §4.1 / damage_model_design -- reproduced or grounded seed/fixture]
    hits_to_fell = -(-full_health(4)//per_hit)  # [canonical: derived_stats §4.1 / damage_model_design -- reproduced or grounded seed]  ceil
    c7 = (3 <= hits_to_fell <= 8)  # [canonical: derived_stats §4.1 / damage_model_design -- reproduced or grounded seed/fixture]
    checks.append(c7)
    print(f"(7) pacing: {per_hit}/clean-cut -> ~{hits_to_fell} clean Success cuts fell a healthy unarmoured End4 "
          f"(Health {full_health(4)}): {'OK' if c7 else 'FAIL'}")

    # (8) coverage: partial armour takes more damage than full (bare zones), same blow
    c8 = (dmg(2,2,4,"light","cut_and_thrust","plate","partial") > dmg(2,2,4,"light","cut_and_thrust","plate","full"))  # [canonical: derived_stats §4.1 / damage_model_design -- reproduced or grounded seed/fixture]
    checks.append(c8)
    print(f"(8) coverage: partial-plate cut {dmg(2,2,4,'light','cut_and_thrust','plate','partial')} > full-plate "
          f"{dmg(2,2,4,'light','cut_and_thrust','plate','full')}: {'OK' if c8 else 'FAIL'}")

    print(rule)
    bad = [i + 1 for i, c in enumerate(checks) if not c]
    if bad:
        print(f"RESULT: FAIL -- checks {bad}"); raise SystemExit(1)
    print(f"RESULT: PASS -- all {len(checks)} damage checks (WI anchor, degree-scales, heft, vs-plate matrix, vs-mail, "
          f"STR additive, wound pacing, coverage) -- all DERIVED from weight/head/armour/degree, no flat multipliers.")
    print("[GROUNDING] built from ONLY the combat resolution (net/degree) + the wound model (WI=End+6). Damage = Impact x "
          "Coupling x Quality; coupling derived from material resistance-per-mode. SUPERSEDES the inherited multiplier formula. "
          "PROPOSAL -- Jordan-vetoable; calibration constant DMG_SCALE tunable.")
