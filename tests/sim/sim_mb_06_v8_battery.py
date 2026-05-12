# SIM-MB-06 v8 battery — F-i (cell support) + F-ii (puncture) validation.
# [canonical: tests/sim/sim_mb_06_handoff_2026-05-12.md -- target ranges from Jordan design spec]
# Target ranges in TARGET_LO / TARGET_HI constants below.
# [canonical: tests/sim/sim_mb_06_handoff_2026-05-12.md -- target ranges from Jordan's design spec]
import random, math, statistics, sys
sys.path.insert(0, '/home/claude')
import sim_mb_06_v8 as s

# Test harness parameters (structural -- not mechanical constants)
# [canonical: tests/sim/sim_mb_06_v7_manifest.md -- structural test params]
N_MAIN = 200       # [canonical: tests/sim/sim_mb_06_v7_manifest.md -- structural n=200 main battery]
N_REDUCED = 150    # [canonical: tests/sim/sim_mb_06_v7_manifest.md -- structural n=150 secondary tests]
N_SEED_B = 500     # [canonical: tests/sim/sim_mb_06_v7_manifest.md -- structural second seed set]
SEP = "=" * 78     # [canonical: tests/sim/sim_mb_06_v7_manifest.md -- structural separator]
TIERS = [2, 3, 4]  # [canonical: tests/sim/sim_mb_06_v7_manifest.md -- structural tier sweep]

# Target validation ranges (from Jordan's handoff design spec)
# [canonical: tests/sim/sim_mb_06_handoff_2026-05-12.md -- 40-60% target for all matchups]
TARGET_LO = 40  # [canonical: tests/sim/sim_mb_06_handoff_2026-05-12.md]
TARGET_HI = 60  # [canonical: tests/sim/sim_mb_06_handoff_2026-05-12.md]

# Anchor column map for placing atoms (structural — matching v7 battery)
# [canonical: tests/sim/sim_mb_06_v7_manifest.md -- structural anchor positions]
ANCHOR_MAP = {
    ('Line', 1): 11, ('Line', 2): 10, ('Line', 3): 9, ('Line', 4): 8,  # [canonical: tests/sim/sim_mb_06_v7_manifest.md -- structural]
    ('Arrowhead', 1): 11, ('Arrowhead', 2): 10, ('Arrowhead', 3): 8, ('Arrowhead', 4): 7,  # [canonical: tests/sim/sim_mb_06_v7_manifest.md -- structural]
    ('Horseshoe', 1): 11, ('Horseshoe', 2): 10, ('Horseshoe', 3): 8, ('Horseshoe', 4): 7,  # [canonical: tests/sim/sim_mb_06_v7_manifest.md -- structural]
    ('GappedLine', 1): 11, ('GappedLine', 2): 10, ('GappedLine', 3): 8, ('GappedLine', 4): 7,  # [canonical: tests/sim/sim_mb_06_v7_manifest.md -- structural]
    ('RefusedFlank', 1): 11, ('RefusedFlank', 2): 10, ('RefusedFlank', 3): 9, ('RefusedFlank', 4): 8,  # [canonical: tests/sim/sim_mb_06_v7_manifest.md -- structural]
}  # [canonical: tests/sim/sim_mb_06_v7_manifest.md -- structural]

# Default unit stats (structural -- matching v7 battery)
# [canonical: tests/sim/sim_mb_06_v7_manifest.md -- structural unit params]
DEFAULT_POWER = 4        # [canonical: tests/sim/sim_mb_06_v7_manifest.md -- structural]
DEFAULT_COMMAND = 4      # [canonical: tests/sim/sim_mb_06_v7_manifest.md -- structural]
DEFAULT_DISCIPLINE = 5   # [canonical: tests/sim/sim_mb_06_v7_manifest.md -- structural]
DEFAULT_MORALE = 6       # [canonical: tests/sim/sim_mb_06_v7_manifest.md -- structural]
DEFAULT_DR = 1           # [canonical: tests/sim/sim_mb_06_v7_manifest.md -- structural]

def make_unit(shape, tier, faction):
    advance_dir = -1 if faction == 'A' else 1
    start_row = s.SIDE_A_START_ROW if faction == 'A' else s.SIDE_B_START_ROW
    anchor_col = ANCHOR_MAP.get((shape, tier), 10)
    atoms = [s.Atom(shape, 'infantry', tier,
                    starting_position=(start_row, anchor_col),
                    advance_dir=advance_dir)]
    return s.Unit(name=f"{shape}-{faction}", faction=faction,
                  power=DEFAULT_POWER, command=DEFAULT_COMMAND,
                  discipline=DEFAULT_DISCIPLINE, discipline_start=DEFAULT_DISCIPLINE,
                  morale=DEFAULT_MORALE, morale_start=DEFAULT_MORALE,
                  atoms=atoms, dr=DEFAULT_DR)

def matchup(shape_a, tier_a, shape_b, tier_b, n=N_MAIN, seed_base=0):  # [canonical: tests/sim/sim_mb_06_v7_manifest.md -- structural]
    a_wins = b_wins = draws = 0
    turns_list = []
    for seed in range(n):
        random.seed(seed + seed_base)
        ua = make_unit(shape_a, tier_a, 'A')
        ub = make_unit(shape_b, tier_b, 'B')
        r = s.run_battle(ua, ub)
        if r['winner'] == 'A': a_wins += 1
        elif r['winner'] == 'B': b_wins += 1
        else: draws += 1
        turns_list.append(r['turns'])
    return {
        'a': a_wins/n*100, 'b': b_wins/n*100, 'd': draws/n*100,
        'turns': statistics.mean(turns_list), 'n': n
    }

def row(label, r, check_a=True):
    status = ''
    if check_a:
        status = ' ok' if TARGET_LO <= r['a'] <= TARGET_HI else ' MISS'
    return f"  {label:50s}  A:{r['a']:5.1f}%  B:{r['b']:5.1f}%  D:{r['d']:5.1f}%  t={r['turns']:.1f}{status}"

def main():
    out = [SEP, "SIM-MB-06 v8 Battery", SEP,
           f"F_SUPPORT_ENABLED={s.F_SUPPORT_ENABLED}  F_PUNCTURE_ENABLED={s.F_PUNCTURE_ENABLED}",
           f"SUPPORT_WEIGHTS={s.SUPPORT_WEIGHTS}  PUNCTURE_CAP={s.PUNCTURE_CAP}",
           ""]

    out.append("[TEST 1] KEY: Arrowhead vs Line -- tension F resolution")
    out.append(f"  Target A: {TARGET_LO}-{TARGET_HI}% | v7: 0%")
    for tier in TIERS:
        r = matchup("Arrowhead", tier, "Line", tier, n=N_MAIN)
        out.append(row(f"  Arrowhead T{tier} vs Line T{tier}", r))

    out.append("\n[TEST 2] Side bias -- Line mirror")
    out.append("  Target: ~50/50 | v7: 51.5/48.5")
    for tier in [2, 3]:
        r = matchup("Line", tier, "Line", tier, n=N_MAIN)
        out.append(row(f"  Line T{tier} mirror", r, check_a=False) +
                   f"  lethality={r['turns']:.1f}t (target 3-6)")

    out.append("\n[TEST 3] Cannae -- Horseshoe vs Arrowhead")
    out.append(f"  Target A: {TARGET_LO}-{TARGET_HI}% | v7: 62%")
    r = matchup("Horseshoe", 3, "Arrowhead", 3, n=N_MAIN)
    out.append(row("  Horseshoe T3 vs Arrowhead T3", r))

    out.append("\n[TEST 4] Horseshoe vs Line -- separate tension")
    out.append(f"  Target A: {TARGET_LO}-{TARGET_HI}% | v7: 0%")
    r = matchup("Horseshoe", 3, "Line", 3, n=N_MAIN)
    out.append(row("  Horseshoe T3 vs Line T3", r))

    out.append("\n[TEST 5] Reversed Cannae -- Arrowhead vs Horseshoe")
    r = matchup("Arrowhead", 3, "Horseshoe", 3, n=N_MAIN)
    out.append(row("  Arrowhead T3 vs Horseshoe T3", r, check_a=False))

    out.append("\n[TEST 6] Shape mods sanity")
    r = matchup("GappedLine", 3, "Line", 3, n=N_REDUCED)
    out.append(row("  GappedLine T3 vs Line T3", r, check_a=False))
    r = matchup("RefusedFlank", 3, "Line", 3, n=N_REDUCED)
    out.append(row("  RefusedFlank T3 vs Line T3", r, check_a=False))

    out.append("\n" + SEP)
    out.append("SUMMARY")
    out.append(SEP)
    r_key = matchup("Arrowhead", 3, "Line", 3, n=N_MAIN, seed_base=N_SEED_B)
    r_bias = matchup("Line", 3, "Line", 3, n=N_MAIN, seed_base=N_SEED_B)
    r_cannae = matchup("Horseshoe", 3, "Arrowhead", 3, n=N_MAIN, seed_base=N_SEED_B)
    r_hvl = matchup("Horseshoe", 3, "Line", 3, n=N_MAIN, seed_base=N_SEED_B)
    for label, rv, target_note in [
        (f"Arrowhead T3 vs Line T3", r_key, f"(target {TARGET_LO}-{TARGET_HI}%)"),
        (f"Line T3 mirror", r_bias, f"(target ~50/50, lethality t={r_bias['turns']:.1f})"),
        (f"Cannae (Horseshoe vs Arrow)", r_cannae, f"(target {TARGET_LO}-{TARGET_HI}%)"),
        (f"Horseshoe vs Line T3", r_hvl, f"(target {TARGET_LO}-{TARGET_HI}% -- open)"),
    ]:
        out.append(f"  {label:40s} A={rv['a']:.1f}%  {target_note}")
    return "\n".join(out)

if __name__ == "__main__":
    print(main())
