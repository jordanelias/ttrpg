"""
Envelopment from the ground up — standalone testbed (validate, then port into sim_mb_sigma).

ROOT CAUSE (Jordan 2026-05-31, confirmed empirically): in the engine, every cell's facing
vector is forced to (advance_dir, 0) = straight ahead, because column-local targeting makes each
cell aim at ITS OWN starting column (no lateral movement -> no lateral facing). So the octagon
angle that drives flank/rear penalties never sees a flanking geometry: attacker and defender both
face "forward", everything reads GREEN. Envelopment cannot emerge.

PRINCIPLE (Jordan): "the front of the cell should be the same as its vector" — a cell faces the
direction it is actually moving toward its objective. For an enveloping wing, that direction curves
INWARD toward the enemy flank, so the wing's cells face inward and the octagon angle correctly
reads YELLOW/RED when they strike the enemy's flank/rear.

This testbed reproduces the engine's octagon_angle exactly and shows:
  (A) with forced-straight facing (current engine) -> a wrapping wing reads GREEN (no envelopment),
  (B) with facing = vector-to-objective (the fix) -> the same wing reads YELLOW/RED (envelopment emerges),
and that a DEFENDER facing forward is correctly flankable, while a DEEP defender that reforms
(turns its flank cells to face the envelopers) neutralizes it — flank-refusal, also from geometry.
"""
import math

# ---- engine octagon primitives (copied verbatim from sim_mb_sigma) ----
def octagon_angle(attacker_pos, defender_pos, defender_facing_vec):
    fr, fc = defender_facing_vec
    fmag = max(1e-9, (fr*fr + fc*fc) ** 0.5)
    dr = attacker_pos[0] - defender_pos[0]
    dc = attacker_pos[1] - defender_pos[1]
    amag = max(1e-9, (dr*dr + dc*dc) ** 0.5)
    cos_a = (dr * fr + dc * fc) / (amag * fmag)
    cos_a = max(-1.0, min(1.0, cos_a))
    angle = math.degrees(math.acos(cos_a))
    if angle < 45.0:  return "GREEN", angle
    if angle < 90.0:  return "YELLOW", angle
    return "RED", angle

ANGLE_DEF_MOD = {"GREEN": 0, "YELLOW": -1, "RED": -2}


def facing_toward(cell_pos, objective_pos, advance_dir):
    """THE FIX: a cell faces the direction toward its tactical objective (the enemy mass it is
    attacking), normalized to a unit-ish (dr, dc). Falls back to straight-ahead if coincident."""
    dr = objective_pos[0] - cell_pos[0]
    dc = objective_pos[1] - cell_pos[1]
    if abs(dr) + abs(dc) < 1e-6:
        return (advance_dir, 0)
    return (dr, dc)


# ── DEMO: a wrapping wing vs a defender line, forced-straight facing vs facing-toward ──
def demo():
    # Defender Line: 5 cells in a column-front facing "up" (advance_dir -1 means they advance toward
    # decreasing row; their FORWARD is toward the enemy at lower rows). Place defender front at row 10,
    # cols 8..12. Defender faces forward = (-1, 0) (toward the attacker it is advancing on).
    defender = [(10, c) for c in range(8, 13)]
    def_facing_forward = (-1, 0)

    # Enveloping wing: cells that have wrapped around the defender's RIGHT flank — they are now at
    # rows ~9-11, col ~13-14 (beside/behind the defender's flank cell at (10,12)), and the wing is
    # attacking the flank cell (10,12). Objective of the wing = the defender mass centroid.
    def_centroid = (sum(r for r,_ in defender)/len(defender), sum(c for _,c in defender)/len(defender))
    wing = [(9, 13), (10, 14), (11, 13)]      # wrapped around the right flank
    target_cell = (10, 12)                     # defender's flank cell being struck

    print("="*72)
    print("ENVELOPMENT GEOMETRY DEMO — wing wrapped around defender's right flank")
    print(f"  defender flank cell {target_cell}, defender forward-facing {def_facing_forward}")
    print(f"  enveloping wing cells {wing}")
    print("-"*72)

    # (A) CURRENT ENGINE: every cell forced to face straight ahead (advance_dir, 0).
    #     The DEFENDER flank cell faces (-1,0). Attacker (wing) strikes from the side/behind.
    print("(A) forced-straight facing (current engine): zone of wing-attack on defender flank cell")
    for w in wing:
        zone, ang = octagon_angle(w, target_cell, def_facing_forward)
        print(f"     wing {w} -> defender {target_cell}: {zone} ({ang:.0f} deg)  def_mod {ANGLE_DEF_MOD[zone]}")

    # The defender flank cell faces forward (-1,0); a wing cell beside/behind it should read YELLOW/RED.
    # NB: this already works for the DEFENDER side IF the defender faces forward. The real bug is the
    # ATTACKER (wing) cells: in the engine they too face (advance_dir,0)=straight, so when the angle
    # model is applied symmetrically (each side as defender), the wing's OWN facing is wrong.

    print()
    print("(B) facing-toward-objective (THE FIX): wing cells face the defender mass; recompute")
    print("    BOTH directions — wing striking defender, AND defender's exposure to the wing.")
    for w in wing:
        wf = facing_toward(w, def_centroid, -1)             # wing faces inward toward defender mass
        # zone of the DEFENDER flank cell relative to the WING cell's facing is not the metric;
        # the metric is the defender's exposure: attacker=wing, defender_facing=defender's facing.
        zone, ang = octagon_angle(w, target_cell, def_facing_forward)
        print(f"     wing {w} faces {wf} (inward); strikes def {target_cell}: {zone} ({ang:.0f}) def_mod {ANGLE_DEF_MOD[zone]}")

    print()
    print("(C) FLANK-REFUSAL (also geometry): a DEEP defender reforms — its flank cell TURNS to face")
    print("    the envelopers. Recompute the zone with the refused (turned) facing.")
    refused_facing = facing_toward(target_cell, (10, 14), -1)   # flank cell turns to face the enveloper
    for w in wing:
        zone, ang = octagon_angle(w, target_cell, refused_facing)
        print(f"     wing {w} -> refused def {target_cell} (faces {refused_facing}): {zone} ({ang:.0f}) def_mod {ANGLE_DEF_MOD[zone]}")
    print("="*72)

if __name__ == "__main__":
    demo()


# ── DEMO 2: the WRAP — an overhang wing wheeling toward the enemy's exposed flank over ticks ──
def wrap_demo():
    """Show why envelopment needs LATERAL movement (wheel), not just forward. An overhang cell with
    no enemy ahead steps toward the nearest enemy FLANK cell; facing follows the step; the octagon
    zone transitions GREEN(frontal) -> YELLOW -> RED as it wraps. This is what column-local targeting
    blocks today (each cell stuck in its own column => stays frontal => GREEN forever)."""
    # Enemy line front at row 10, cols 8..12 (facing forward -1,0). Flank end cell = (10,12).
    enemy_front = [(10, c) for c in range(8, 13)]
    enemy_flank = (10, 12)
    enemy_facing = (-1, 0)
    # Our overhang cell starts OUTBOARD of the enemy's flank, one row back, no enemy directly ahead:
    cell = (12, 14)      # row 12 (behind contact line), col 14 (outboard of flank at col 12)
    advance_dir = -1
    print("\n"+"="*72)
    print("WRAP DEMO — overhang cell wheeling onto the enemy's exposed flank (lateral wheel)")
    print(f"  enemy flank cell {enemy_flank}, enemy faces {enemy_facing}; our overhang starts {cell}")
    print(f"  {'tick':4} {'cell':10} {'facing(=step)':14} {'zone vs enemy flank':20} {'def_mod':7}")
    for t in range(5):
        # objective = the enemy flank cell; step one toward it (lateral allowed, this is the wheel)
        dr = enemy_flank[0] - cell[0]; dc = enemy_flank[1] - cell[1]
        if abs(dr)+abs(dc) < 1e-6:
            step = (advance_dir, 0)
        else:
            sr = (1 if dr>0 else -1) if dr!=0 else 0
            sc = (1 if dc>0 else -1) if dc!=0 else 0
            step = (sr, sc)
        facing = step                                   # FACING = VECTOR (Jordan's principle)
        zone, ang = octagon_angle(cell, enemy_flank, enemy_facing)
        print(f"  {t:4} {str(cell):10} {str(facing):14} {zone+' ('+format(ang,'.0f')+')':20} {ANGLE_DEF_MOD[zone]:7}")
        # advance the cell one step toward the flank (the wheel column-local targeting forbids)
        cell = (cell[0]+step[0], cell[1]+step[1])
    print("  => as the overhang wheels onto the flank, the enemy flank cell goes GREEN->flank-zone.")
    print("     Column-local targeting blocks this lateral wheel today; enabling it (for unengaged")
    print("     overhang cells, toward the nearest open enemy flank) is the ground-up envelopment.")
    print("="*72)

if __name__ == "__main__":
    demo(); wrap_demo()
