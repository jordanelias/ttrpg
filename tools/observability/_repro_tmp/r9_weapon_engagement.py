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
HEAVY_REACH_FRACTION = 0.25                          # [canonical: combat_v30 §5 weight -- heavy long weapons have reach but poor reach-CONTROL (commit to each swing); sim-tunable]
SPEED_TEMPO_BIND     = LEVEL_SIGMA["minor"] * 0.45  # [canonical: combat_v30 §5 reach + m3 speed -- grounded seed; speed edge per speed-point in the bind; sim-tunable]
SPEED_TEMPO_APPROACH = LEVEL_SIGMA["minor"] * 0.15  # [canonical: combat_v30 §5 reach + m3 speed -- grounded seed; minor speed edge in closing (quickness helps a little at range); sim-tunable]
REACH_BIND_PENALTY   = LEVEL_SIGMA["minor"] * 0.5   # [canonical: combat_v30 §5 reach + m3 speed -- grounded seed; reach INVERTS to a liability in the bind (long weapon can't work inside); sim-tunable]


def _reach_val(weapon):
    """1 for long, 0 for short (canonical reach class)."""
    return 1 if WEAPON_CLASSES[weapon]["reach"] == "long" else 0


def _speed(weapon):
    """Canonical per-weapon speed (m3.WEAPON_CLASSES)."""
    return WEAPON_CLASSES[weapon]["speed"]


def _eff_reach_control(weapon):
    """Effective reach-CONTROL: a long weapon controls the measure only if wieldy enough to fence with
    it. Light long weapons (spear, staff) get full control; heavy long weapons (war hammer) get little
    -- they have the reach but commit to each swing. History: a spearman out-fences a hammerman at
    distance, even though both are 'long'."""
    if _reach_val(weapon) == 0:
        return 0.0
    return 1.0 if WEAPON_CLASSES[weapon]["weight"] == "light" else HEAVY_REACH_FRACTION


def weapon_tempo_dsig(attacker_weapon, defender_weapon, state):
    """Phase-dependent reach-control + speed tempo dsig (aggressor-favouring positive).
      - closing / breaking: reach-CONTROL governs (a WIELDY long weapon controls the measure; a heavy
        long weapon barely does) + an all-phase speed term (a slow weapon is disadvantaged everywhere).
      - in_bind: speed governs (faster weapon wins the close) and raw reach inverts to a liability
        (a long weapon -- especially a heavy one -- cannot work inside the measure).
    A heavy slow weapon (war hammer) is therefore disadvantaged in EVERY duel phase: it cannot fence at
    reach (low reach-control) and loses the bind (slowest). Its damage is its only edge -- which only
    pays off when the foe cannot exploit that slowness, i.e. the BATTLEFIELD (see r10_battlefield_context)."""
    speed_diff = _speed(attacker_weapon) - _speed(defender_weapon)
    if state == "in_bind":
        reach_diff = _reach_val(attacker_weapon) - _reach_val(defender_weapon)
        return speed_diff * SPEED_TEMPO_BIND - reach_diff * REACH_BIND_PENALTY
    reach_ctrl_diff = _eff_reach_control(attacker_weapon) - _eff_reach_control(defender_weapon)
    return reach_ctrl_diff * REACH_TEMPO_APPROACH + speed_diff * SPEED_TEMPO_APPROACH


# ============================== self-test ==============================
if __name__ == "__main__":
    checks = []
    rule = "================================================================"
    print("R9 weapon engagement -- weight-modulated reach + speed (validation)")
    print(rule)

    spear = "long_pole_spear"      # long, LIGHT, speed 0  -> full reach-control
    dagger = "single_short"        # short, light, speed 3
    hammer = "long_heavy_blunt"    # long, HEAVY, speed -0.5 -> poor reach-control, slowest

    # (a) Spear vs dagger: spear WINS the approach (reach-control, it is light+long), LOSES the bind.
    sc = weapon_tempo_dsig(spear, dagger, "closing")
    sb = weapon_tempo_dsig(spear, dagger, "in_bind")
    a_ok = (sc > 0 and sb < 0)
    checks.append(a_ok)
    print(f"\n(a) spear vs dagger: closing {sc:+.2f} (reach-control wins approach) | bind {sb:+.2f} (dagger wins close): {'OK' if a_ok else 'FAIL'}")

    # (b) Spear vs HAMMER: the spear OUT-FENCES the hammer at distance (both long, but spear is light ->
    #     full reach-control; hammer heavy -> poor). New corrected result: spear beats hammer in the approach.
    sh_c = weapon_tempo_dsig(spear, hammer, "closing")
    sh_b = weapon_tempo_dsig(spear, hammer, "in_bind")
    b_ok = (sh_c > 0 and sh_b > 0)   # spear wins approach (reach-control) AND bind (faster than the hammer)
    checks.append(b_ok)
    print(f"(b) spear vs hammer: closing {sh_c:+.2f} (spear out-fences) | bind {sh_b:+.2f} (spear faster): {'OK' if b_ok else 'FAIL'}")

    # (c) Hammer vs dagger: hammer is DISADVANTAGED in every phase (poor reach-control + slowest).
    #     Historically a dagger-man closing on a war hammer in a duel: the hammer is in trouble.
    hd_c = weapon_tempo_dsig(hammer, dagger, "closing")
    hd_b = weapon_tempo_dsig(hammer, dagger, "in_bind")
    c_ok = (hd_c < 0 and hd_b < 0)
    checks.append(c_ok)
    print(f"(c) hammer vs dagger: closing {hd_c:+.2f} | bind {hd_b:+.2f} (hammer disadvantaged BOTH phases -- a duel weapon it is not): {'OK' if c_ok else 'FAIL'}")

    # (d) Heavy long weapon has POOR reach-control vs a light long weapon: eff_reach_control hammer < spear.
    d_ok = (_eff_reach_control(hammer) < _eff_reach_control(spear) and _eff_reach_control(spear) == 1.0
            and _eff_reach_control(dagger) == 0.0)
    checks.append(d_ok)
    print(f"(d) reach-control: spear {_eff_reach_control(spear)}, hammer {_eff_reach_control(hammer)} (heavy=poor), dagger {_eff_reach_control(dagger)} (short=0): {'OK' if d_ok else 'FAIL'}")

    # (e) Mirror weapon = 0 tempo all phases.
    e_ok = all(abs(weapon_tempo_dsig(spear, spear, st)) < 1e-9 for st in ("closing", "in_bind", "breaking"))  # [canonical: combat_v30 §5 / m3 -- grounded seed/fixture]
    checks.append(e_ok)
    print(f"(e) mirror weapon = 0 tempo all phases: {'OK' if e_ok else 'FAIL'}")

    print("\n" + rule)
    bad = [i for i, c in enumerate(checks) if not c]
    if bad:
        print(f"RESULT: FAIL -- {bad}"); raise SystemExit(1)
    print(f"RESULT: PASS -- all {len(checks)} checks (light-long out-fences heavy-long; heavy slow weapon "
          f"disadvantaged every duel phase; spear/dagger phase niches; mirror = 0).")
    print("[GROUNDING] bottom-up: canonical reach + weight + per-weapon speed (combat_v30 §5; m3). top-down: "
          "HEMA -- reach-CONTROL needs a wieldy weapon; a heavy battlefield weapon (war hammer) is not a duel "
          "weapon (its niche is r10_battlefield_context). Gap-completion; PROPOSAL -- Jordan-vetoable; no canon edited.")
