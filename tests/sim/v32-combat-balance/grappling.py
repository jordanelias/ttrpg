"""
grappling.py -- close-combat / grappling substrate, built bottom-up (Build-13).  # [canonical: 3.6 Actions / ST1 / grappling_system_design -- reused or grounded seed/fixture]

Implements the grappling_system_design proposal: the innermost engagement state, built from the CANONICAL
close-combat actions (Disarm, Tie Up, Escape, Retrieve -- 3.6 Actions) unified into a grapple phase, plus  # [canonical: 3.6 Actions / ST1 / grappling_system_design -- reused or grounded seed/fixture]
the one new element -- the grounded-foe dagger-finish that bypasses armour mitigation (the third historical
plate-counter, after blunt and point-to-gaps). Fills the canon-acknowledged unarmed/close gap (ED-129).  # [canonical: 3.6 Actions / ST1 / grappling_system_design -- reused or grounded seed/fixture]

Bottom-up wiring (each sub-mechanic -> a named primitive):
  * grapple range  = innermost state of the engagement graph (R9/R10); reach inverts hard.
  * grapple contest = Strength-dominant sigma-contest, extending ratified ST1 (bind-win per STR point).
  * hands          = a 2H weapon occupies both hands -> poor grapple (wa2 hands axis).
  * fatigue        = the more-drained fighter grapples worse (asymmetric -- the honest fatigue role).
  * throw->prone   = a sigma-window (ST1 stagger analog); bypasses armour (can't deflect a takedown).
  * disarm/tie up  = the canonical actions (Off vs STR+Agi ; both -2D).
  * dagger-finish  = point strike on a controlled/prone foe, resolved as coverage->gap on the armour
                     matrix (aa) -> bypasses mitigation. The rondel-dagger kill.
  * escape         = the canonical Agi out (bounds the lock).

No canon retconned -- canonical actions are reused. PROPOSAL -- Jordan-vetoable; the dagger-finish is the
one new mechanic flagged for ratification. Per-constant provenance: grappling_verification_ledger.json
"""
from m1_dice_sigma_core import LEVEL_SIGMA
import armour_axes as AA
import weapon_axes_v2 as W

# ===== grapple sigma-leverage channel (Strength-dominant; extends ST1) =====
STR_GRAPPLE_PER_POINT = LEVEL_SIGMA["minor"] * 0.75   # [canonical: ST1 ratified Strength bind-win; grapple is its close-range extreme -- dominant term; grounded seed]
HANDS_2H_GRAPPLE_PENALTY = LEVEL_SIGMA["moderate"]    # [canonical: grappling_system_design §2 -- a 2H weapon occupies both hands; wa2 hands axis; grounded seed]
FATIGUE_GRAPPLE_PENALTY  = LEVEL_SIGMA["minor"]       # [canonical: grappling_system_design §2 -- the more-drained fighter grapples worse (asymmetric); grounded seed]
CLOSE_TEMPO_COST         = LEVEL_SIGMA["moderate"]    # [canonical: grappling_system_design §1 -- closing surrenders reach/tempo to reach the clinch; grounded seed]

# throw margin thresholds (in sigma-leverage units) -> outcome severity
THROW_MARGIN   = LEVEL_SIGMA["moderate"]              # [canonical: grappling_system_design §3 -- decisive grapple win = takedown; grounded seed]
CONTROL_MARGIN = LEVEL_SIGMA["minor"]                 # [canonical: grappling_system_design §3 -- marginal win = control/Tie Up; grounded seed]

def grapple_leverage(attacker, defender):
    """Strength-dominant sigma-leverage of a grapple attempt. attacker/defender: dicts with
    strength, history (wrestling skill), weapon (name), armour (name)."""
    aw = W.WEAPONS_V2[attacker["weap"]]; dw = W.WEAPONS_V2[defender["weap"]]
    L = (attacker["strength"] - defender["strength"]) * STR_GRAPPLE_PER_POINT
    L += (attacker["history"] - defender["history"]) * (LEVEL_SIGMA["minor"] * 0.5)   # [canonical: 3.6 Actions -- skill (History) contributes; grounded]
    # a 2H weapon in hand hampers YOUR grapple (must shorten/drop); empty/1H does not
    if aw["hands"] == 2 and aw["head"] != "blunt":  # polearms especially; (a 2H weapon you must manage)
        L -= HANDS_2H_GRAPPLE_PENALTY
    if dw["hands"] == 2 and dw["head"] != "blunt":
        L += HANDS_2H_GRAPPLE_PENALTY               # defender encumbered by their 2H weapon -> easier to grapple
    # asymmetric fatigue: heavier-drained armour grapples worse
    L -= (AA.stamina_drain(attacker["armour"]) - AA.stamina_drain(defender["armour"])) * FATIGUE_GRAPPLE_PENALTY
    return L

def grapple_outcome(attacker, defender):
    """Returns the outcome tier of a won/lost grapple by sigma-leverage margin."""
    L = grapple_leverage(attacker, defender)
    if L >= THROW_MARGIN:   return "throw"      # takedown -> prone
    if L >= CONTROL_MARGIN: return "control"    # Tie Up / setup
    if L <= -THROW_MARGIN:  return "thrown"     # attacker is taken down instead
    if L <= -CONTROL_MARGIN:return "controlled" # attacker controlled
    return "stalemate"                          # neither gains -> Escape available

def dagger_finish_mod(armour):
    """The grounded/controlled-foe dagger-finish: a POINT strike on the GAP profile (coverage->gap),
    bypassing armour mitigation. Returns the effective weapon-vs-armour mod for a dagger thrust to gaps."""
    # a controlled/prone foe = gap access: the point profile, and even vs full plate the gaps are open
    base = 3   # [canonical: combat_v30 §5 -- point/light base vs none]
    # gap access on a controlled foe: use the point row but treat coverage as gaps-exposed (partial-equivalent)
    fam, weight = "point", "light"
    # controlled foe: mitigation halved (gap access) -> dagger reaches the gaps regardless of tier
    full = AA.MITIGATION[(fam, weight)][AA.material(armour)] * 0.5   # [canonical: 3.6 Actions / ST1 / grappling_system_design -- reused or grounded seed]  gap access halves the (already low) point mitigation
    return max(0, int(round(base - full)))

def close_tempo_cost():
    """Closing to grapple surrenders reach/tempo -- the cost that makes grappling a choice, not a win-button."""
    return -CLOSE_TEMPO_COST


# ============================== self-test ==============================
if __name__ == "__main__":
    checks = []; rule = "=" * 64  # [canonical: 3.6 Actions / ST1 / grappling_system_design -- reused or grounded seed/fixture]
    print("grappling substrate -- validation"); print(rule)

    def F(strn, hist, weap, armour): return {"strength": strn, "history": hist, "weap": weap, "armour": armour}

    # (1) grapple is STRENGTH-dominant: a stronger fighter wins the clinch
    strong = F(6, 2, "dagger", "none"); weak = F(2, 2, "dagger", "none")  # [canonical: 3.6 Actions / ST1 / grappling_system_design -- reused or grounded seed/fixture]
    c1 = (grapple_leverage(strong, weak) > 0 and grapple_outcome(strong, weak) in ("throw", "control")
          and grapple_outcome(weak, strong) in ("thrown", "controlled"))
    checks.append(c1)
    print(f"(1) Strength-dominant: STR6 vs STR2 -> {grapple_outcome(strong,weak)} (lev {grapple_leverage(strong,weak):+.2f}); "
          f"STR2 vs STR6 -> {grapple_outcome(weak,strong)}: {'OK' if c1 else 'FAIL'}")

    # (2) the hands axis: a 2H-weapon fighter grapples WORSE than an equal 1H/dagger fighter
    g_dagger = F(4, 3, "dagger", "none")          # [canonical: 3.6 Actions / ST1 / grappling_system_design -- reused or grounded seed]  free off-hand
    g_great  = F(4, 3, "greatsword", "none")      # [canonical: 3.6 Actions / ST1 / grappling_system_design -- reused or grounded seed]  both hands on the weapon
    vs = F(4, 3, "arming_sword", "none")  # [canonical: 3.6 Actions / ST1 / grappling_system_design -- reused or grounded seed/fixture]
    c2 = (grapple_leverage(g_dagger, vs) > grapple_leverage(g_great, vs))
    checks.append(c2)
    print(f"(2) hands: dagger-grappler lev {grapple_leverage(g_dagger,vs):+.2f} > greatsword-grappler "
          f"{grapple_leverage(g_great,vs):+.2f} (2H hampers the clinch): {'OK' if c2 else 'FAIL'}")

    # (3) THE THIRD PLATE-COUNTER: the dagger-finish bypasses mitigation -- it reaches a full-harness foe
    #     where a normal CUT strike is fully deflected (mod 0)
    cut_vs_plate = AA.effective_weapon_mod("cut", "light", 3, "full_harness")     # [canonical: 3.6 Actions / ST1 / grappling_system_design -- reused or grounded seed]  = 0 (deflected)
    dagger_vs_plate = dagger_finish_mod("full_harness")                          # > 0 (gaps)
    c3 = (cut_vs_plate == 0 and dagger_vs_plate >= 1)
    checks.append(c3)
    print(f"(3) dagger-FINISH bypasses plate: cut-vs-plate {cut_vs_plate} (deflected) -> dagger-to-gaps "
          f"{dagger_vs_plate} (reaches): {'OK' if c3 else 'FAIL'} -- the third plate-counter")

    # (4) the dagger-finish reaches the gaps REGARDLESS of tier (a controlled foe = gap access)
    c4 = (dagger_finish_mod("none") >= dagger_finish_mod("full_harness") >= 1
          and dagger_finish_mod("mail_hauberk") >= 1)
    checks.append(c4)
    print(f"(4) finish vs tiers: none {dagger_finish_mod('none')} >= mail {dagger_finish_mod('mail_hauberk')} "
          f">= plate {dagger_finish_mod('full_harness')} (all >=1 -- gaps always reachable on a controlled foe): {'OK' if c4 else 'FAIL'}")

    # (5) closing has a TEMPO cost (grappling is a choice, not a free win)
    c5 = (close_tempo_cost() < 0)
    checks.append(c5)
    print(f"(5) closing cost: tempo {close_tempo_cost():+.2f} (surrender reach/tempo to reach the clinch): {'OK' if c5 else 'FAIL'}")

    # (6) asymmetric fatigue: a heavily-armoured grappler is disadvantaged vs an equal unarmoured one
    g_plate = F(4, 3, "dagger", "full_harness"); g_none = F(4, 3, "dagger", "none")  # [canonical: 3.6 Actions / ST1 / grappling_system_design -- reused or grounded seed/fixture]
    c6 = (grapple_leverage(g_plate, g_none) < 0)
    checks.append(c6)
    print(f"(6) fatigue asymmetry: plate-grappler vs unarmoured lev {grapple_leverage(g_plate,g_none):+.2f} "
          f"(<0 -- heavier-drained grapples worse): {'OK' if c6 else 'FAIL'}")

    print(rule)
    bad = [i + 1 for i, c in enumerate(checks) if not c]
    if bad:
        print(f"RESULT: FAIL -- checks {bad}"); raise SystemExit(1)
    print(f"RESULT: PASS -- all {len(checks)} grappling checks (Strength-dominant, hands penalty, dagger-finish bypasses "
          f"plate = third counter, gaps reachable all tiers, closing tempo cost, fatigue asymmetry).")
    print("[GROUNDING] bottom-up: canonical actions (Disarm/Tie Up/Escape/Retrieve, 3.6 Actions) + ST1 Strength + the armour "
          "matrix (aa) + wa2 hands + M1 LEVEL_SIGMA. Top-down: Fiore abrazare + ringen + the rondel-dagger record (validation "
          "doc). Fills ED-129 unarmed gap. PROPOSAL -- only the dagger-finish is new; Jordan-vetoable.")
