"""
m7_facing_fov.py -- Module seven (M7) of the v32 combat-balance sim (perception / facing / field-of-view).

v32 replaces v31's authored Facing Ob table: facing's combat effect is now EMERGENT from perception
(Pillar 5). The direction a fighter faces sets their field of view; FoV sets what they can read,
anticipate, and react to. This module implements that model in full:

  - FoV zones: the opponent's relative angular position -> Central / Near-peripheral / Far-peripheral
    / Blind, each with an FoV factor and a reaction-availability set.
  - Reading scaling: each sight-mediated Reading channel Pool is scaled by the opponent's FoV factor;
    Tactile (the bind) is contact-mediated and exempt ("you feel the bind regardless of where you look").
  - Reaction gating: reactive aspects require the incoming line within FoV at the listed factor or
    better -- no reaction from the blind rear, only reflexive Hand-led from far-peripheral.
  - Emergent facing advantage: the aggressor's advantage attacking into the defender's periphery/rear
    is DERIVED from two compounding channels (the defender's Reading scaled down + the defender's
    reaction options gated away), not an authored Ob line. Composes M5.reaction_sigma.

The advantage reproduces v31's authored values (about -1 effective Ob at flank, about -2 at rear),
which emerge super-linearly from the perception model (reframe_blueprint section 4). NOTE: the exact
emergent magnitude depends on the defender's base Reading delta-sigma, which comes from the Phase-4
Reading net-success table (not modelled here). M8 wires that with M5 reactions to pin the magnitude;
M7 validates the STRUCTURE (compounding, monotonic by zone, total loss at the rear) and supplies the
composition. The flank/rear Ob figures are the validation reference, not asserted by M7.

Constant provenance: tests/sim/v32-combat-balance/m7_verification_ledger.json (all Class B, v32 proposal).
"""
import numpy as np
from m5_stance_reaction_coherence import reaction_sigma, REACTION_PARAMS

# ===== Class B: FoV model (combat_v32_proposal §11.2 -- draft) =====
FOV_ZONES = ["central", "near_peripheral", "far_peripheral", "blind"]
# upper angular bound (degrees from facing centre) per zone; beyond far-peripheral = blind:
ANGULAR_BANDS = {"central": 30, "near_peripheral": 70, "far_peripheral": 110}  # [canonical: combat_v32_proposal §11.2 -- draft (±30 / 30-70 / 70-110 / >110)]
FOV_FACTORS = {"central": 1.0, "near_peripheral": 0.6, "far_peripheral": 0.3, "blind": 0.0}  # [canonical: combat_v32_proposal §11.2 -- draft]
# reactive aspects usable against an attack arriving in each zone (Central = all reactions, M5):
REACTIONS_BY_ZONE = {
    "central": list(REACTION_PARAMS.keys()),     # all reactive aspects available
    "near_peripheral": ["body_led", "hand_led"],  # Hand-led + Body-led only
    "far_peripheral": ["hand_led"],               # Hand-led only (reflexive)
    "blind": [],                                  # none -- you cannot void what you cannot see
}  # [canonical: combat_v32_proposal §11.2 -- draft (reaction availability by zone)]
SIGHT_CHANNELS = ["geometric", "kinetic", "rhythmic"]   # FoV-scaled
TACTILE_CHANNEL = "tactile"                              # contact-mediated, FoV-exempt
# emergent advantage reproduces these v31 authored values (validation reference; reframe_blueprint section 4):
FLANK_OB_TARGET = -1   # [canonical: combat_v32_proposal §11.2 -- about -1 effective Ob at flank]
REAR_OB_TARGET = -2    # [canonical: combat_v32_proposal §11.2 -- about -2 effective Ob at rear]


def fov_zone(angle_deg):
    """Map the opponent's absolute angular position (degrees from the fighter's facing centre) to a
    FoV zone."""
    a = abs(angle_deg)
    if a <= ANGULAR_BANDS["central"]:
        return "central"
    if a <= ANGULAR_BANDS["near_peripheral"]:
        return "near_peripheral"
    if a <= ANGULAR_BANDS["far_peripheral"]:
        return "far_peripheral"
    return "blind"


def fov_factor(zone):
    """FoV scaling factor for a zone (§11.2)."""
    return FOV_FACTORS[zone]


def effective_reading_pool(base_pool, zone, channel):
    """FoV-scaled Reading Pool for a channel: base x FoV_factor for sight-mediated channels;
    Tactile is contact-mediated and NOT scaled."""
    if channel == TACTILE_CHANNEL:
        return base_pool
    return base_pool * FOV_FACTORS[zone]


def reactive_aspects_available(zone):
    """Which reactive aspects are usable against an attack arriving in this zone (§11.2)."""
    return list(REACTIONS_BY_ZONE[zone])


def reaction_available(reaction, zone):
    """Whether a specific reaction can be used against an attack arriving in this zone (§11.2)."""
    return reaction in REACTIONS_BY_ZONE[zone]


def emergent_facing_advantage(zone, base_reading_dsig, depth, reaction_fn=reaction_sigma):
    """Estimate the sigma-space Ob advantage an aggressor gains attacking into the defender's `zone`
    EMERGENT from two compounding channels, not an authored Ob line:
      (1) Reading: the defender's sight-mediated Reading delta-sigma is FoV-scaled down -> lost anticipation,
          = base_reading_dsig x (1 - FoV_factor(zone)).
      (2) Reaction: the defender's best available reaction delta-sigma is capped by zone gating,
          = best_central_reaction - best_zone_reaction (at this commit depth).
    Returns a breakdown dict; total_ob_shift is negative = aggressor advantaged. The flank/rear Ob
    targets are the validation reference; the exact base_reading_dsig is supplied by the caller
    (M8 / the Phase-4 Reading net-success table)."""
    f = FOV_FACTORS[zone]
    reading_loss = base_reading_dsig * (1 - f)
    full_best = max((reaction_fn(r, depth) for r in REACTIONS_BY_ZONE["central"]), default=0.0)
    zone_best = max((reaction_fn(r, depth) for r in REACTIONS_BY_ZONE[zone]), default=0.0)
    reaction_loss = full_best - zone_best
    total = -(reading_loss + reaction_loss)
    return {"zone": zone, "reading_loss": reading_loss, "reaction_loss": reaction_loss,
            "total_ob_shift": total}


# ===== facing-change levers (which actions move/hold/reset relative facing) — §11.2 =====
FACING_CHANGE = {
    "angled_approach": "toward_periphery",      # Phase 3: flanking approaches move aggressor to defender periphery
    "drawing_approach": "hold",                 # Phase 3: holds relative facing
    "voiding": "change",                        # Phase 6: Voiding changes facing
    "curvilinear_footwork": "change",           # Phase 6: enables mid-bout facing change
    "triangular_footwork": "change",            # Phase 6: enables mid-bout facing change
    "bursting_footwork": "reset",               # Phase 6: re-centres opponent in FoV
}  # [canonical: combat_v32_proposal §11.2 -- facing changes during]


# ================================= self-test =================================
if __name__ == "__main__":
    checks = []
    rule = "================================================================"
    print("Module seven (M7) -- perception / facing / FoV -- validation against §11.2")
    print(rule)

    # (a) angular position -> FoV zone (§11.2 bands)
    ZONE_CASES = [(0, "central"), (30, "central"), (50, "near_peripheral"), (70, "near_peripheral"), (90, "far_peripheral"), (110, "far_peripheral"), (150, "blind")]  # [canonical: combat_v32_proposal §11.2 -- FoV angular bands]
    a_ok = all(fov_zone(ang) == z for ang, z in ZONE_CASES)
    checks.append(a_ok)
    print(f"\n(a) angular -> zone (±30 central, 30-70 near, 70-110 far, >110 blind): {'OK' if a_ok else 'FAIL'}")

    # (b) FoV factors per zone
    b_ok = (fov_factor("central") == 1.0 and fov_factor("near_peripheral") == 0.6
            and fov_factor("far_peripheral") == 0.3 and fov_factor("blind") == 0.0)  # [canonical: combat_v32_proposal §11.2 -- FoV factors]
    checks.append(b_ok)
    print(f"(b) FoV factors (central 1.0 / near 0.6 / far 0.3 / blind 0.0): {'OK' if b_ok else 'FAIL'}")

    # (c) Reading scaling: sight channels scaled by FoV; Tactile exempt
    base = 10
    sight_scaled = (effective_reading_pool(base, "near_peripheral", "geometric") == base * 0.6
                    and effective_reading_pool(base, "blind", "kinetic") == 0.0)  # [canonical: combat_v32_proposal §11.2 -- sight channels FoV-scaled]
    tactile_exempt = (effective_reading_pool(base, "blind", TACTILE_CHANNEL) == base
                      and effective_reading_pool(base, "far_peripheral", TACTILE_CHANNEL) == base)
    c_ok = sight_scaled and tactile_exempt
    checks.append(c_ok)
    print(f"(c) Reading scaling (Geometric@near {effective_reading_pool(base,'near_peripheral','geometric')}=6.0; Tactile exempt = base): {'OK' if c_ok else 'FAIL'}")

    # (d) reaction gating + "you cannot void what you cannot see"
    d_ok = (reaction_available("voiding", "central") and not reaction_available("voiding", "near_peripheral")
            and not reaction_available("voiding", "far_peripheral") and not reaction_available("voiding", "blind")
            and reaction_available("hand_led", "far_peripheral") and not reaction_available("hand_led", "blind")
            and reaction_available("body_led", "near_peripheral") and not reaction_available("body_led", "far_peripheral")
            and reactive_aspects_available("blind") == [])
    checks.append(d_ok)
    print(f"(d) reaction gating (Voiding central-only; Hand-led to far; nothing in blind): {'OK' if d_ok else 'FAIL'}")

    # (e) emergent facing advantage: structure (no authored Ob line)
    #     base_reading_dsig is a unit placeholder here -- the real magnitude comes from the Phase-4
    #     Reading net-success table (M8 pins). M7 validates the STRUCTURE only.
    base_rd = float(abs(FLANK_OB_TARGET))   # unit placeholder (1.0); exact value from §4.5 [ASSUMPTION]
    adv = {z: emergent_facing_advantage(z, base_rd, DEPTH := 3) for z in FOV_ZONES}  # depth 3 = Committed
    central0 = (adv["central"]["total_ob_shift"] == 0)                               # no advantage facing square
    monotonic = (adv["central"]["total_ob_shift"] > adv["near_peripheral"]["total_ob_shift"]
                 > adv["far_peripheral"]["total_ob_shift"] > adv["blind"]["total_ob_shift"])
    blind_total_loss = (adv["blind"]["reading_loss"] == base_rd                       # full Reading lost (factor 0)
                        and adv["blind"]["reaction_loss"] == max(reaction_sigma(r, 3) for r in REACTIONS_BY_ZONE["central"]))
    e_ok = central0 and monotonic and blind_total_loss
    checks.append(e_ok)
    print(f"(e) emergent advantage STRUCTURE (central 0; monotonic central>near>far>blind; blind = total loss): {'OK' if e_ok else 'FAIL'}")
    print(f"      derived Ob shift by zone (unit base Reading δσ): "
          f"central {adv['central']['total_ob_shift']:.2f}, near {adv['near_peripheral']['total_ob_shift']:.2f}, "
          f"far {adv['far_peripheral']['total_ob_shift']:.2f}, blind {adv['blind']['total_ob_shift']:.2f} "
          f"[same ordering as the v31 flank≈-1 / rear≈-2 targets; exact magnitude from §4.5 + M5, pinned in M8]")

    # (f) facing-change levers (§11.2)
    f_ok = (FACING_CHANGE["angled_approach"] == "toward_periphery" and FACING_CHANGE["drawing_approach"] == "hold"
            and FACING_CHANGE["bursting_footwork"] == "reset" and FACING_CHANGE["voiding"] == "change")
    checks.append(f_ok)
    print(f"(f) facing-change levers (Angled->periphery, Drawing->hold, Bursting->reset, Voiding->change): {'OK' if f_ok else 'FAIL'}")

    print("\n" + rule)
    bad = [i for i, c in enumerate(checks) if not c]
    if bad:
        print(f"RESULT: FAIL -- check indices failing: {bad}")
        raise SystemExit(1)
    print(f"RESULT: PASS -- all {len(checks)} checks match §11.2 "
          f"(zone mapping, FoV factors, Reading scaling + Tactile exemption, reaction gating, emergent structure, facing levers).")
    print("[ASSUMPTION] emergent magnitude uses a unit base Reading delta-sigma; the exact value (Phase-4 Reading "
          "net-success table) is wired in M8. [GAP] §4.5 Reading->delta-sigma mapping not modelled in M7.")
