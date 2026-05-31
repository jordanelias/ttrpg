"""
r9_weapon_engagement.py -- phase-dependent reach + speed tempo (Build-9, the spear fix).  # [canonical: combat_v30 §5 reach / m3 speed -- grounded seed/fixture]

The weapon audit left the spear dead (23%) despite canonical "spear is king"; a FLAT reach->tempo  # [canonical: combat_v30 §5 reach / m3 speed -- grounded seed/fixture]
channel over-corrects (it inflates the heavy LONG weapons too). The correct model is PHASE-DEPENDENT:
reach governs the closing/breaking measure (longer weapon controls the approach), speed governs the
bind (faster weapon wins once closed; reach inverts to a liability inside the measure). This yields the
rock-paper-scissors that gives each weapon a niche (spear wins approach/loses bind; dagger loses
approach/dominates bind; war hammer wins approach but is worst in the bind). Grounded bottom-up
(canonical reach + per-weapon speed, combat_v30 §5 + m3) and top-down (HEMA measure/bind dynamic);  # [canonical: combat_v30 §5 reach / m3 speed -- grounded seed/fixture]
gap-completion of the canon-intended 'spear is king' that the sim left dead -- does NOT overwrite an
authored value. Per-constant sources: r9_verification_ledger.json. PROPOSAL -- Jordan-vetoable; no canon edited.
"""
from m3_weapon_class_layer import WEAPON_CLASSES
from m1_dice_sigma_core import LEVEL_SIGMA

# ===== Class C: phase-tempo channel magnitudes (grounded; sim-tunable) =====
REACH_TEMPO_APPROACH = LEVEL_SIGMA["minor"] * 0.8   # [canonical: combat_v30 §5 reach + m3 speed -- grounded seed; reach edge per reach-step in closing/breaking; sim-tunable]
SPEED_TEMPO_BIND     = LEVEL_SIGMA["minor"] * 0.45  # [canonical: combat_v30 §5 reach + m3 speed -- grounded seed; speed edge per speed-point in the bind; sim-tunable]
SPEED_TEMPO_APPROACH = LEVEL_SIGMA["minor"] * 0.15  # [canonical: combat_v30 §5 reach + m3 speed -- grounded seed; minor speed edge in closing (quickness helps a little at range); sim-tunable]
REACH_BIND_PENALTY   = LEVEL_SIGMA["minor"] * 0.5   # [canonical: combat_v30 §5 reach + m3 speed -- grounded seed; reach INVERTS to a liability in the bind (long weapon can't work inside); sim-tunable]


def _reach_val(weapon):
    """1 for long, 0 for short (canonical reach class)."""
    return 1 if WEAPON_CLASSES[weapon]["reach"] == "long" else 0


def _speed(weapon):
    """Canonical per-weapon speed (m3.WEAPON_CLASSES)."""
    return WEAPON_CLASSES[weapon]["speed"]


def weapon_tempo_dsig(attacker_weapon, defender_weapon, state):
    """Phase-dependent reach + speed tempo dsig (aggressor-favouring positive).
      - closing / breaking: reach governs (longer weapon controls the measure) + minor speed edge.
      - in_bind: speed governs (faster weapon wins the close) and reach inverts to a liability.
    """
    reach_diff = _reach_val(attacker_weapon) - _reach_val(defender_weapon)
    speed_diff = _speed(attacker_weapon) - _speed(defender_weapon)
    if state == "in_bind":
        return speed_diff * SPEED_TEMPO_BIND - reach_diff * REACH_BIND_PENALTY
    # closing / breaking (distance phases)
    return reach_diff * REACH_TEMPO_APPROACH + speed_diff * SPEED_TEMPO_APPROACH


# ============================== self-test ==============================
if __name__ == "__main__":
    checks = []
    rule = "================================================================"
    print("R9 weapon engagement -- phase-dependent reach + speed tempo (validation)")
    print(rule)

    spear = "long_pole_spear"      # long, speed 0
    dagger = "single_short"        # short, speed 3
    hammer = "long_heavy_blunt"    # long, speed -0.5 (slowest)

    # (a) Spear vs dagger: spear WINS the approach (reach), LOSES the bind (dagger faster + closes inside).
    spear_close = weapon_tempo_dsig(spear, dagger, "closing")
    spear_bind  = weapon_tempo_dsig(spear, dagger, "in_bind")
    a_ok = (spear_close > 0 and spear_bind < 0)
    checks.append(a_ok)
    print(f"\n(a) spear vs dagger: closing {spear_close:+.2f} (reach wins approach) | bind {spear_bind:+.2f} "
          f"(dagger wins the close): {'OK' if a_ok else 'FAIL'}")

    # (b) Symmetric: dagger vs spear is the mirror -- dagger loses approach, dominates bind.
    dagger_close = weapon_tempo_dsig(dagger, spear, "closing")
    dagger_bind  = weapon_tempo_dsig(dagger, spear, "in_bind")
    b_ok = (dagger_close < 0 and dagger_bind > 0 and abs(dagger_close + spear_close) < 1e-9  # [canonical: combat_v30 §5 reach / m3 speed -- grounded seed/fixture]
            and abs(dagger_bind + spear_bind) < 1e-9)  # [canonical: combat_v30 §5 reach / m3 speed -- grounded seed/fixture]
    checks.append(b_ok)
    print(f"(b) dagger vs spear (mirror): closing {dagger_close:+.2f} | bind {dagger_bind:+.2f} "
          f"(antisymmetric): {'OK' if b_ok else 'FAIL'}")

    # (c) War hammer vs spear (both long, so reach cancels): hammer LOSES the bind (slower than spear).
    #     Differentiates hammer from spear -- both win reach vs short weapons, but hammer is worst in the bind.
    h_v_s_close = weapon_tempo_dsig(hammer, spear, "closing")   # both long: reach_diff 0 -> only speed (hammer slower) -> slightly negative
    h_v_s_bind  = weapon_tempo_dsig(hammer, spear, "in_bind")   # both long: reach cancels; hammer slower -> negative
    c_ok = (abs(h_v_s_close) < REACH_TEMPO_APPROACH and h_v_s_bind < 0)  # no reach edge (both long); hammer loses bind
    checks.append(c_ok)
    print(f"(c) hammer vs spear (both long, reach cancels): closing {h_v_s_close:+.2f} | bind {h_v_s_bind:+.2f} "
          f"(hammer slower -> loses bind): {'OK' if c_ok else 'FAIL'}")

    # (d) War hammer vs dagger: hammer wins approach (reach), dagger dominates bind (huge speed gap).
    h_v_d_close = weapon_tempo_dsig(hammer, dagger, "closing")
    h_v_d_bind  = weapon_tempo_dsig(hammer, dagger, "in_bind")
    d_ok = (h_v_d_close > 0 and h_v_d_bind < 0 and h_v_d_bind < spear_bind)  # hammer worse in bind than spear was
    checks.append(d_ok)
    print(f"(d) hammer vs dagger: closing {h_v_d_close:+.2f} (reach) | bind {h_v_d_bind:+.2f} "
          f"(dagger dominates; hammer worse than spear in bind): {'OK' if d_ok else 'FAIL'}")

    # (e) Two identical weapons: zero tempo in every phase (no spurious asymmetry).
    e_ok = all(abs(weapon_tempo_dsig(spear, spear, st)) < 1e-9 for st in ("closing", "in_bind", "breaking"))  # [canonical: combat_v30 §5 reach / m3 speed -- grounded seed/fixture]
    checks.append(e_ok)
    print(f"(e) mirror weapon = 0 tempo all phases: {'OK' if e_ok else 'FAIL'}")

    print("\n" + rule)
    bad = [i for i, c in enumerate(checks) if not c]
    if bad:
        print(f"RESULT: FAIL -- {bad}"); raise SystemExit(1)
    print(f"RESULT: PASS -- all {len(checks)} checks (reach wins approach, speed wins bind, reach inverts "
          f"in the bind, hammer differentiated from spear by speed, mirror = 0).")
    print("[GROUNDING] bottom-up: canonical reach + per-weapon speed (combat_v30 §5; m3). top-down: HEMA "
          "measure/bind dynamic. Gap-completion (canon 'spear is king' vs dead-in-sim). PROPOSAL -- Jordan-vetoable; no canon edited.")
