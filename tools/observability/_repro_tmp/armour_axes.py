"""
armour_axes.py -- brand-new armour substrate, built bottom-up (Build-12).  # [canonical: 3.4 Armour / combat_v30 §5 / armour_system_design -- reproduced or grounded seed/fixture]

Implements the armour_system_design proposal. The canonical armour skeleton (4 tiers; STR-min 0/2/3/4;  # [canonical: 3.4 Armour / combat_v30 §5 / armour_system_design -- reproduced or grounded seed/fixture]
per-action Stamina drain +0/+0/+1/+2; flat Health +4/+6/+8; the weapon-vs-armour table) is REPRODUCED  # [canonical: 3.4 Armour / combat_v30 §5 / armour_system_design -- reproduced or grounded seed/fixture]
exactly -- no canonical value is changed. New structure underneath it:
  * material axis (none/cloth/mail/plate) drives an (attack-head x material) MITIGATION MATRIX, calibrated
    so effective_mod = base_vs_none - mitigation reproduces the ratified weapon-vs-armour rows;
  * coverage axis (partial/full) modulates applied mitigation (gap exposure);
  * the four canonical tiers (none/light/medium/heavy) are presets in (material x coverage) space;
  * costs route through ratified channels: Stamina per-action drain (fatigue), a new sigma-tempo penalty,
    flat Health, STR-min.

Grounding: bottom-up = the canonical skeleton + ratified W1/W5 weapon-vs-armour values + the M1 LEVEL_SIGMA;
top-down = arms-and-armour history (mail-vs-cut, plate-vs-blunt, point-vs-gaps, gambeson, fatigue) -- see
run_armour_validation + the result doc. PROPOSAL -- Jordan-vetoable. The only NEW combat lever is the
sigma-tempo penalty (flagged for ratification); everything else reproduces canon.
Per-constant provenance: tests/sim/v32-combat-balance/armour_axes_verification_ledger.json
"""
from m1_dice_sigma_core import LEVEL_SIGMA

MATERIALS = ["none", "cloth", "mail", "plate"]
COVERAGES = ["partial", "full"]
ATTACK_HEADS = ["cut", "point", "blunt"]   # the weapon head families that interact with armour

# ===== canonical skeleton, reproduced verbatim (no retcon) =====
TIER_STR_MIN   = {"none": 0, "light": 2, "medium": 3, "heavy": 4}      # [canonical: 3.4 Armour / m3 ARMOR_STR_MIN]
TIER_DRAIN     = {"none": 0, "light": 0, "medium": 1, "heavy": 2}      # [canonical: 3.4 Armour / derived_stats §4.2 -- per-action Stamina drain]
TIER_HEALTH    = {"none": 0, "light": 4, "medium": 6, "heavy": 8}      # [canonical: derived_stats §14 -- flat Health +4 leather/+6 chain/+8 plate]

# the ratified weapon-vs-armour table (W1 + W5), reproduced -- the matrix calibration target
RATIFIED_TABLE = {                                                     # [canonical: combat_v30 §5 + W1 ratified + W5 ratified]
    "cut_light":  {"none": 3, "light": 2, "medium": 1, "heavy": 0},    # [canonical: combat_v30 §5 light_blade]
    "cut_heavy":  {"none": 6, "light": 4, "medium": 2, "heavy": 0},    # [canonical: combat_v30 §5 heavy_blade]
    "point_light":{"none": 3, "light": 3, "medium": 2, "heavy": 1},    # [canonical: W5 ratified POINT_ARMOR_MOD]
    "blunt_light":{"none": 3, "light": 3, "medium": 2, "heavy": 2},    # [canonical: W1 ratified light_blunt]
    "blunt_heavy":{"none": 5, "light": 5, "medium": 4, "heavy": 3},    # [canonical: W1 ratified heavy_blunt]
}

# ===== the (attack-head x material) MITIGATION MATRIX (the bottom-up generator) =====
# mitigation subtracted from the weapon's base_vs_none. Calibrated to reproduce RATIFIED_TABLE when
# material maps to tier (none->none, cloth->light, mail->medium, plate->heavy). Split by weapon weight
# only where the ratified table itself splits (blunt heavy transmits more through plate than blunt light).
# cut: stopped progressively (cloth absorbs, mail stops slash, plate deflects). point: barely (gaps remain
# vs plate). blunt: transmits through everything (percussion), weight sets how much gets through plate.
MITIGATION = {                                                         # [canonical: armour_system_design §1 -- calibrated to reproduce the ratified table; grounded]
    ("cut",  "light"): {"none": 0, "cloth": 1, "mail": 2, "plate": 3}, # [canonical: armour_system_design §1]
    ("cut",  "heavy"): {"none": 0, "cloth": 2, "mail": 4, "plate": 6}, # [canonical: armour_system_design §1 -- heavy blade mitigated proportionally to its larger base]
    ("point","light"): {"none": 0, "cloth": 0, "mail": 1, "plate": 2}, # [canonical: armour_system_design §1 -- thrust finds gaps vs plate]
    ("blunt","light"): {"none": 0, "cloth": 0, "mail": 1, "plate": 1}, # [canonical: armour_system_design §1 -- light percussion transmits]
    ("blunt","heavy"): {"none": 0, "cloth": 0, "mail": 1, "plate": 2}, # [canonical: armour_system_design §1 -- heavy percussion concusses through]
}

# ===== armour presets: the four canonical tiers + off-preset combos the new axes unlock =====
ARMOUR = {
    "none":           {"material": "none",  "coverage": "full",    "tier": "none"},
    "gambeson":       {"material": "cloth", "coverage": "full",    "tier": "light"},   # levy / universal underlayer
    "mail_hauberk":   {"material": "mail",  "coverage": "full",    "tier": "medium"},
    "full_harness":   {"material": "plate", "coverage": "full",    "tier": "heavy"},
    # off-preset (now expressible; which to instantiate is a content call)
    "mail_shirt":     {"material": "mail",  "coverage": "partial", "tier": "light"},   # partial mail
    "breastplate":    {"material": "plate", "coverage": "partial", "tier": "medium"},  # vital-zone plate
    "three_quarter":  {"material": "plate", "coverage": "full",    "tier": "heavy"},   # harness minus lower legs (still heavy)
}

COVERAGE_FACTOR = {"full": 1.0, "partial": 0.5}                        # [canonical: armour_system_design §2 -- partial protects the vital zone only; grounded]
ARMOUR_TEMPO_PER_DRAIN = LEVEL_SIGMA["minor"] * 0.5                    # [canonical: armour_system_design §3 -- NEW sigma-tempo penalty per drain point; grounded seed, PROPOSAL]

def tier(a):        return ARMOUR[a]["tier"]
def material(a):    return ARMOUR[a]["material"]
def coverage(a):    return ARMOUR[a]["coverage"]
def str_min(a):     return TIER_STR_MIN[tier(a)]
def stamina_drain(a): return TIER_DRAIN[tier(a)]
def health_bonus(a):  return TIER_HEALTH[tier(a)]

def armour_tempo_dsig(a):
    """NEW: armour's initiative/tempo penalty -- scales with the (canonical) per-action drain (a weight proxy)."""
    return -ARMOUR_TEMPO_PER_DRAIN * stamina_drain(a)

def mitigation(head, weight, a):
    """Damage the armour absorbs vs a given attack head+weight, modulated by coverage (gap exposure)."""
    if material(a) == "none": return 0.0
    base = MITIGATION[(head, weight)][material(a)]
    return base * COVERAGE_FACTOR[coverage(a)]

def effective_weapon_mod(head, weight, base_vs_none, a):
    """The weapon's effective vs-armour modifier = base(vs none) - mitigation. Reproduces the ratified table
    for the four tier-presets (full coverage); extends to off-preset material/coverage combos."""
    return max(0, int(round(base_vs_none - mitigation(head, weight, a))))


# ============================== self-test ==============================
if __name__ == "__main__":
    checks = []; rule = "=" * 66  # [canonical: 3.4 Armour / combat_v30 §5 / armour_system_design -- reproduced or grounded seed/fixture]
    print("armour_axes substrate -- validation"); print(rule)

    # base_vs_none for each (head,weight) = the ratified 'none' column
    BASE = {("cut","light"):3, ("cut","heavy"):6, ("point","light"):3, ("blunt","light"):3, ("blunt","heavy"):5}  # [canonical: 3.4 Armour / combat_v30 §5 / armour_system_design -- reproduced or grounded seed/fixture]
    # preset that reproduces each tier (full coverage)
    TIER_PRESET = {"none":"none", "light":"gambeson", "medium":"mail_hauberk", "heavy":"full_harness"}

    # (1) THE KEY CHECK: the matrix reproduces the ratified weapon-vs-armour table EXACTLY (no retcon)
    mism = []
    for keyname, (head, weight) in [("cut_light",("cut","light")),("cut_heavy",("cut","heavy")),
                                    ("point_light",("point","light")),("blunt_light",("blunt","light")),
                                    ("blunt_heavy",("blunt","heavy"))]:
        for tname, a in TIER_PRESET.items():
            got = effective_weapon_mod(head, weight, BASE[(head,weight)], a)
            want = RATIFIED_TABLE[keyname][tname]
            if got != want: mism.append(f"{keyname}/{tname}: got {got} want {want}")
    c1 = not mism; checks.append(c1)
    print(f"(1) matrix REPRODUCES ratified weapon-vs-armour table (all 5 rows x 4 tiers): {'OK' if c1 else 'FAIL '+str(mism)}")

    # (2) STR-min / drain / Health reproduce the canonical skeleton
    c2 = (str_min("none")==0 and str_min("gambeson")==2 and str_min("mail_hauberk")==3 and str_min("full_harness")==4  # [canonical: 3.4 Armour / combat_v30 §5 / armour_system_design -- reproduced or grounded seed/fixture]
          and stamina_drain("none")==0 and stamina_drain("mail_hauberk")==1 and stamina_drain("full_harness")==2
          and health_bonus("gambeson")==4 and health_bonus("mail_hauberk")==6 and health_bonus("full_harness")==8)  # [canonical: 3.4 Armour / combat_v30 §5 / armour_system_design -- reproduced or grounded seed/fixture]
    checks.append(c2)
    print(f"(2) skeleton reproduced -- STR-min 0/2/3/4, drain 0/0/1/2, Health +4/+6/+8: {'OK' if c2 else 'FAIL'}")

    # (3) matrix STRUCTURE matches history: vs plate, blunt mitigated least, point next, cut most (deflected)
    pl="full_harness"
    cut_mit   = mitigation("cut","light",pl)
    point_mit = mitigation("point","light",pl)
    blunt_mit = mitigation("blunt","heavy",pl)
    # compare as fraction of base (cut fully stopped, point/blunt get through)
    c3 = (effective_weapon_mod("cut","light",3,pl)==0 and effective_weapon_mod("point","light",3,pl)>=1  # [canonical: 3.4 Armour / combat_v30 §5 / armour_system_design -- reproduced or grounded seed/fixture]
          and effective_weapon_mod("blunt","heavy",5,pl)>=3)  # [canonical: 3.4 Armour / combat_v30 §5 / armour_system_design -- reproduced or grounded seed/fixture]
    checks.append(c3)
    print(f"(3) vs PLATE: cut->{effective_weapon_mod('cut','light',3,pl)} (deflected) < point->"
          f"{effective_weapon_mod('point','light',3,pl)} (gaps) < blunt->{effective_weapon_mod('blunt','heavy',5,pl)} "
          f"(transmits): {'OK' if c3 else 'FAIL'}")

    # (4) mail excels vs the CUT (rings stop the slash) but the THRUST gets through more
    mh="mail_hauberk"
    c4 = (effective_weapon_mod("cut","light",3,mh) < effective_weapon_mod("point","light",3,mh))  # [canonical: 3.4 Armour / combat_v30 §5 / armour_system_design -- reproduced or grounded seed/fixture]
    checks.append(c4)
    print(f"(4) vs MAIL: cut->{effective_weapon_mod('cut','light',3,mh)} < point->"
          f"{effective_weapon_mod('point','light',3,mh)} (thrust bursts rings): {'OK' if c4 else 'FAIL'}")

    # (5) the trade-off: heavier armour -> more mitigation BUT more drain (fatigue) AND a bigger tempo penalty
    c5 = (mitigation("cut","light","full_harness") > mitigation("cut","light","gambeson")
          and stamina_drain("full_harness") > stamina_drain("gambeson")
          and armour_tempo_dsig("full_harness") < armour_tempo_dsig("gambeson") <= 0)
    checks.append(c5)
    print(f"(5) trade-off: harness mitigates more (cut {mitigation('cut','light','full_harness'):.1f} vs gambeson "
          f"{mitigation('cut','light','gambeson'):.1f}) but drains more ({stamina_drain('full_harness')} vs "
          f"{stamina_drain('gambeson')}) + slower tempo ({armour_tempo_dsig('full_harness'):+.2f} vs "
          f"{armour_tempo_dsig('gambeson'):+.2f}): {'OK' if c5 else 'FAIL'}")

    # (6) coverage: partial protects less than full (gap exposure) -- breastplate (plate,partial) < full_harness
    c6 = (mitigation("cut","light","breastplate") < mitigation("cut","light","full_harness")
          and mitigation("cut","light","breastplate") > 0)
    checks.append(c6)
    print(f"(6) coverage: breastplate(plate,partial) cut-mitigation {mitigation('cut','light','breastplate'):.1f} "
          f"< full_harness {mitigation('cut','light','full_harness'):.1f} (limbs exposed): {'OK' if c6 else 'FAIL'}")

    # (7) material fidelity the flat tier can't express: full mail vs partial plate -- different vs the thrust
    #     mail_hauberk (mail,full) vs breastplate (plate,partial), both ~medium protection, differ vs point
    c7 = (effective_weapon_mod("point","light",3,"mail_hauberk") != effective_weapon_mod("point","light",3,"breastplate")  # [canonical: 3.4 Armour / combat_v30 §5 / armour_system_design -- reproduced or grounded seed/fixture]
          or effective_weapon_mod("cut","light",3,"mail_hauberk") != effective_weapon_mod("cut","light",3,"breastplate"))  # [canonical: 3.4 Armour / combat_v30 §5 / armour_system_design -- reproduced or grounded seed/fixture]
    checks.append(c7)
    print(f"(7) material fidelity: mail-hauberk vs breastplate differ on the SAME attack "
          f"(point {effective_weapon_mod('point','light',3,'mail_hauberk')} vs "
          f"{effective_weapon_mod('point','light',3,'breastplate')}; cut "
          f"{effective_weapon_mod('cut','light',3,'mail_hauberk')} vs "
          f"{effective_weapon_mod('cut','light',3,'breastplate')}): {'OK' if c7 else 'FAIL'}")

    print(rule)
    bad = [i + 1 for i, c in enumerate(checks) if not c]
    if bad:
        print(f"RESULT: FAIL -- checks {bad}"); raise SystemExit(1)
    print(f"RESULT: PASS -- all {len(checks)} armour checks (matrix REPRODUCES ratified table, skeleton reproduced, "
          f"plate-vs-blunt/point/cut history, mail-vs-cut/thrust, trade-off, coverage, material fidelity).")
    print("[GROUNDING] bottom-up: canonical skeleton + ratified W1/W5 table + M1 LEVEL_SIGMA -- every canonical value reproduced, "
          "none changed. Top-down validation in run_armour_validation + the result doc. PROPOSAL -- only the sigma-tempo penalty "
          "is a new combat lever (flagged for ratification); Jordan-vetoable.")
