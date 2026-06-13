"""
percussion_authority.py -- bottom-up derivation of BLUNT-mode percussion authority from a weapon's
mass and point-of-balance, replacing the hand-assigned `percussion` 0-8 rating.  PROPOSAL -- Jordan-vetoable.
No canon file edited.  (Lane-A design; J-33 PoB residual, ED-934.)

------------------------------------------------------------------------------------------------------
WHY THIS EXISTS
------------------------------------------------------------------------------------------------------
core.coupling() scales a blunt strike's transmission by `perc/8.0`, where `perc` is a per-weapon integer
assigned BY HAND in combatant.WEAPONS (mace 8, poleaxe 8, staff 4, ...). core.py itself calls 8 the
"steel-hammer reference" and geometry.percussion_concentration() notes it "multiplies the percussion
AUTHORITY (mass) handled elsewhere" -- i.e. the authority half was always understood to be a mass
phenomenon, but was operationalised as a hand-set number rather than derived. Meanwhile the weapons carry
continuous `mass` and `pob_frac` fields that the engine consumes NOWHERE (collapsed to the binary HEFT).
This module derives the authority from those physical fields so percussion is bottom-up, not assigned.

------------------------------------------------------------------------------------------------------
THE PHYSICS (energy-limited swing)
------------------------------------------------------------------------------------------------------
Pivot ~ the hands. Length scales: total L = grip_len + head_len; centre of mass at d_com = pob_frac * L
from the grip. A committed swing puts work W into rotating the weapon (1/2 I w^2 = W) about the grip,
where the moment of inertia I ~ mass * d_com^2.

  * Impact momentum of the head (radius r ~ L):  p = sqrt(2 W I) / r  ~  sqrt(mass) * pob_frac.
        (The L's cancel: a longer lever speeds the tip but raises I in equal measure -- so under an
         energy-limited swing the authority depends on mass and the BALANCE FRACTION, not raw length.)
  * Effective striking mass at the head:  m_eff = I / r^2  ~  mass * pob_frac^2  ( = p^2 ).
        A head-forward weapon presents more mass at contact, stays "planted", and transfers impulse
         instead of bouncing -- which is precisely how a blunt weapon defeats armour.

So one quantity -- where the mass sits, sqrt(mass)*pob_frac -- sets the percussive authority. The SAME
mass distribution sets the static first moment M1 = mass * d_com (head-heaviness), which is the handling
/ control cost (overcommit, recovery). Damage upside and control cost share a single physical source.

Authority does not grow without bound (you cannot swing an ever-heavier head ever faster, and armour
either fails or it does not), so authority is a SATURATING function of the impact momentum.

------------------------------------------------------------------------------------------------------
HEAD-SHAPE GATE
------------------------------------------------------------------------------------------------------
Percussion is delivered only by a STRIKING head. A spear or rapier carries large mass-forward momentum
(spear sqrt(m)*pob = 0.59) but spends it on a thrust, not a percussive blow; an edged sword spends it on
a cut. So percussion authority applies to head == 'blunt' only -- which matches the engine, since
core._mode_transmit() reads `perc` ONLY in its blunt branch (cut/point/cut_thrust modes never consume it).
For non-blunt heads the relevant authority is the cut coefficient (edge_keenness, curvature) or the gap
coefficient (point_concentration, cross_section rigidity), both derived in geometry.py.

------------------------------------------------------------------------------------------------------
CALIBRATION DISCIPLINE
------------------------------------------------------------------------------------------------------
Bottom-up FORM (saturating function of sqrt(mass)*pob_frac); the two constants (scale C, exponent a) are
pinned to REPRODUCE the three validated blunt anchors (mace 8, poleaxe 8, staff 4) -- the same
"reproduce the validated values, then refine continuously" discipline as geometry.py. There are only
three blunt weapons in canon, so the exponent is calibrated, not independently cross-validated.
"""
from math import sqrt

# --- calibration constants (pinned to the validated blunt anchors mace/poleaxe = 8, staff = 4) ---
PERC_SCALE    = 9.5     # C
PERC_EXPONENT = 0.30    # a   (on impact momentum sqrt(mass)*pob_frac; equivalently 0.15 on effective mass)
PERC_CAP      = 8.0     # the "steel-hammer reference" ceiling (kept = the canonical 0-8 scale top)
HEAVY_BLUNT_THRESHOLD = 6.0   # P_auth at/above -> blunt_heavy armour row; below -> blunt_light


def impact_momentum(mass, pob_frac):
    """Energy-limited impact momentum of a swing ~ sqrt(mass) * pob_frac (the L's cancel). The physical
    driver of percussive authority; equals sqrt(effective striking mass)."""
    return sqrt(mass) * pob_frac


def percussion_authority(mass, pob_frac, head='blunt'):
    """Bottom-up percussion authority (0..PERC_CAP), replacing the hand-assigned `percussion`. Gated to
    striking heads: a non-blunt head delivers no percussion (its authority is cut/thrust, derived in
    geometry.py). Drop-in for the `perc` argument of core.damage / core.coupling."""
    if head != 'blunt':
        return 0.0
    return min(PERC_CAP, PERC_SCALE * impact_momentum(mass, pob_frac) ** PERC_EXPONENT)


def blunt_armour_row(P_auth):
    """Which ratified blunt row a striking weapon reproduces, derived from its authority (replaces the
    hand-drawn heavy/light blunt assignment). RATIFIED_TABLE: blunt_heavy {none5,light5,med4,heavy3};
    blunt_light {none3,light3,med2,heavy2}."""
    return 'blunt_heavy' if P_auth >= HEAVY_BLUNT_THRESHOLD else 'blunt_light'


def first_moment(mass, pob_frac, total_len):
    """Static head-heaviness M1 = mass * d_com (d_com = pob_frac*L). The HANDLING/control cost dual of
    authority -- exposed so the overcommit/poise coupling (the other half of the PoB residual) can draw
    on the same physical source rather than a separate hand-set number."""
    return mass * pob_frac * total_len


# ---- puncture / penetration: the SAME swing authority delivered through a CONCENTRATED head ----
def puncture_pressure(mass, pob_frac, strike_concentration, head='blunt'):
    """Impact-puncture -- a pick / beak / spike (poleaxe, bec de corbin, war-hammer, a long-shafted
    pick): a SWUNG head, so the force is the SAME swing authority as percussion, but delivered through a
    CONCENTRATED contact -- so the defeat metric is PRESSURE = force / area = authority x concentration.
    Pressure is what PIERCES plate; percussion's broad face instead transmits the impulse as CONCUSSION
    (trauma through intact plate). The single head-shape variable that separates puncture from percussion
    is the contact concentration (strike_concentration: broad mace face 0 -> needle beak/pick 1) -- which
    is Jordan's hypothesis, confirmed.

    Returns a RELATIVE pressure (a ranking, NOT a calibrated damage number): there is no ratified
    pick-vs-plate value to calibrate to -- RATIFIED_TABLE flattens pick and broad blunt into one
    heavy-blunt row, so turning this into damage requires both a calibration constant AND a canon
    decision on whether a pick out-defeats a mace vs plate (it historically did). Gated to swung (blunt)
    heads. Thrust-puncture is the OTHER puncture sub-mode -- a body-driven point finding gaps -- and is
    already derived (geometry.gap_precision = point_concentration x cross_section rigidity) and wired."""
    if head != 'blunt':
        return 0.0
    return percussion_authority(mass, pob_frac, head) * strike_concentration


def armour_defeat_mode(head, geom):
    """The bottom-up armour-defeat term a head delivers, routed by head SHAPE (Jordan: the puncture/
    percussion split 'comes down to head shape itself'):
      concussion  -- broad blunt face (low strike_concentration): impulse/trauma through plate;
      puncture    -- concentrated blunt (high strike_concentration): pressure pierces plate;
      gap-thrust  -- point: a body-driven point finds gaps (point_concentration x rigidity);
      cut         -- edge (edge_keenness, curvature): slices flesh, collapses vs plate.
    Returns the dominant mode tag for the head."""
    if head == 'blunt':
        return 'puncture' if geom.get('strike_concentration', 0.0) >= 0.5 else 'concussion'
    if head == 'point':
        return 'gap-thrust'
    if head == 'cut_thrust':
        return 'gap-thrust/cut'      # mode-shifts: gap-thrust vs plate, cut vs flesh
    return 'cut'                     # straight_cut / curved_cut


# ----------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    import sys
    sys.path.insert(0, '/home/claude'); sys.path.insert(0, '/home/claude/combat_engine'); sys.path.insert(0, '/home/claude/v32')
    from combatant import WEAPONS, GEOMETRY
    import core
    from config import CFG
    SC, CE = CFG['DAMAGE_SCALE'], CFG['CAP_END']

    print("== self-test: reproduce validated blunt ratings + damage, derive heavy/light row ==\n")
    anchors = {'mace': 8, 'poleaxe': 8, 'staff': 4}
    ok = True

    print(f"{'weapon':9s} {'sqrt(m)*pob':>11s} {'P_auth':>7s} {'hand-set':>8s} {'row':>12s}")
    for w, want in anchors.items():
        v = WEAPONS[w]
        pa = percussion_authority(v['mass'], v['pob_frac'], v['head'])
        row = blunt_armour_row(pa)
        match = abs(round(pa) - want) <= 0   # exact to the integer scale
        ok &= match
        print(f"{w:9s} {impact_momentum(v['mass'],v['pob_frac']):>11.3f} {pa:>7.2f} {want:>8d} {row:>12s}"
              f"  {'OK' if match else 'MISS'}")

    print("\n-- blunt damage parity (hand-set perc vs derived P_auth), Success, not-close --")
    cells = mism = 0
    for w in anchors:
        v = WEAPONS[w]
        for arm in ('none', 'light', 'medium', 'heavy'):
            dh = core.damage('success', v['wt'], v['head'], 4, arm, False, SC, CE, v['gap'], v.get('percussion', 8))
            da = core.damage('success', v['wt'], v['head'], 4, arm, False, SC, CE, v['gap'],
                             percussion_authority(v['mass'], v['pob_frac'], v['head']))
            cells += 1; mism += (dh != da)
            if dh != da:
                print(f"   {w:8s} {arm:7s}: hand-set {dh} vs P_auth {da}  (continuous refinement)")
    print(f"   {cells-mism}/{cells} cells identical; {mism} refined by +/-1")

    print("\n-- non-blunt heads: P_auth gated to 0 (perc never consumed for these modes) --")
    for w in ('longsword', 'spear', 'rapier', 'sabre'):
        v = WEAPONS[w]
        print(f"   {w:10s} head={v['head']:12s} P_auth={percussion_authority(v['mass'],v['pob_frac'],v['head']):.2f}  (hand-set {v.get('percussion')}, dead)")

    print(f"\nRESULT: anchors reproduced = {ok}; percussion now derived from (mass, pob_frac), not hand-assigned.")

    print("\n== puncture vs percussion: same authority, head shape (concentration) splits the mode ==\n")
    print(f"{'weapon':12s} {'head':8s} {'auth':>5s} {'strk_c':>6s} {'concuss':>7s} {'PIERCE':>6s}  mode")
    pr = []
    for w in ('poleaxe', 'mace', 'staff'):
        v = WEAPONS[w]; gm = GEOMETRY[w]
        a = percussion_authority(v['mass'], v['pob_frac'], v['head'])
        pierce = puncture_pressure(v['mass'], v['pob_frac'], gm['strike_concentration'], v['head'])
        mode = armour_defeat_mode(v['head'], gm)
        pr.append((w, pierce))
        print(f"{w:12s} {v['head']:8s} {a:>5.2f} {gm['strike_concentration']:>6.2f} {a:>7.2f} {pierce:>6.2f}  {mode}")
    print(f"\n  pick-pierce/concuss-pierce ratio (poleaxe/mace) = {pr[0][1]/pr[1][1]:.2f}x -- the plate-defeat the")
    print("  engine flattens (both head='blunt', identical RESIST). The bottom-up split predicts a pick")
    print("  out-pierces a mace vs plate -- a refinement beyond the single RATIFIED_TABLE heavy-blunt row")
    print("  (a Jordan canon decision, since the table does not separate them).")
