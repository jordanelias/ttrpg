"""SIM-MB-06 v6 Phase C battery — compare baseline / C-i / C-ii pool formulas.
[canonical: structural — Phase C exploration]"""
import sys, random, statistics
sys.path.insert(0, '/home/claude')

# Reload the sim module fresh for each variant by exec-ing with different POOL_VARIANT
def load_sim(variant):
    """Load sim_mb_06_v6_phaseC.py with POOL_VARIANT set to given value."""
    src = open('/home/claude/sim_mb_06_v6_phaseC.py').read()
    src = src.replace(
        'POOL_VARIANT = "baseline"',
        f'POOL_VARIANT = "{variant}"',
        1
    )
    ns = {}
    exec(src, ns)
    return ns

def make_uniform_unit(shape, tier, name, faction, sim_ns, atoms_count=1):
    Unit = sim_ns['Unit']
    Atom = sim_ns['Atom']
    advance_dir = -1 if faction == 'A' else 1
    start_row = sim_ns['SIDE_A_START_ROW'] if faction == 'A' else sim_ns['SIDE_B_START_ROW']
    # Hardcoded anchor cols by shape — center each on col 12 of 25-wide grid
    anchor_map = {
        ('Line', 1): 11, ('Line', 2): 10, ('Line', 3): 9, ('Line', 4): 8,
        ('Arrowhead', 1): 11, ('Arrowhead', 2): 10, ('Arrowhead', 3): 8, ('Arrowhead', 4): 7,
        ('Horseshoe', 1): 11, ('Horseshoe', 2): 10, ('Horseshoe', 3): 8, ('Horseshoe', 4): 7,
        ('GappedLine', 1): 11, ('GappedLine', 2): 10, ('GappedLine', 3): 8, ('GappedLine', 4): 7,
        ('RefusedFlank', 1): 11, ('RefusedFlank', 2): 10, ('RefusedFlank', 3): 9, ('RefusedFlank', 4): 8,
    }
    anchor_col = anchor_map.get((shape, tier), 10)
    atoms = []
    for i in range(atoms_count):
        a = Atom(shape, 'infantry', tier,
                 starting_position=(start_row, anchor_col + i*3),
                 advance_dir=advance_dir)
        atoms.append(a)
    return Unit(name=name, faction=faction, power=4, command=4,
                discipline=5, discipline_start=5, morale=6, morale_start=6,
                atoms=atoms, dr=1)

def make_composite_unit(name, faction, sim_ns):
    """Mixed atoms: 1 Arrowhead T2 + 2 Line T1."""
    Unit = sim_ns['Unit']
    Atom = sim_ns['Atom']
    advance_dir = -1 if faction == 'A' else 1
    start_row = sim_ns['SIDE_A_START_ROW'] if faction == 'A' else sim_ns['SIDE_B_START_ROW']
    atoms = [
        Atom('Arrowhead', 'infantry', 2, starting_position=(start_row, 11), advance_dir=advance_dir),
        Atom('Line', 'infantry', 1, starting_position=(start_row, 7), advance_dir=advance_dir),
        Atom('Line', 'infantry', 1, starting_position=(start_row, 16), advance_dir=advance_dir),
    ]
    return Unit(name=name, faction=faction, power=4, command=4,
                discipline=5, discipline_start=5, morale=6, morale_start=6,
                atoms=atoms, dr=1)

def matchup(make_a_fn, make_b_fn, variant, n=80, seed_base=500000):
    sim_ns = load_sim(variant)
    a_wins = 0; b_wins = 0; draws = 0; turns_list = []
    for s in range(n):
        random.seed(s + seed_base)
        a = make_a_fn(sim_ns)
        b = make_b_fn(sim_ns)
        result = sim_ns['run_battle'](a, b)
        if result.get('winner') == 'A': a_wins += 1
        elif result.get('winner') == 'B': b_wins += 1
        else: draws += 1
        turns_list.append(result.get('turns', 15))
    return {
        "a_pct": a_wins / n * 100,
        "b_pct": b_wins / n * 100,
        "draw_pct": draws / n * 100,
        "mean_turns": statistics.mean(turns_list),
        "n": n,
    }

def format_row(label, r):
    return f"  {label:40s}  A:{r['a_pct']:5.1f}%  B:{r['b_pct']:5.1f}%  D:{r['draw_pct']:5.1f}%  t={r['mean_turns']:.1f}"

def main():
    out = []
    out.append("=" * 78)
    out.append("SIM-MB-06 v6 Phase C — pool formula variants")
    out.append("=" * 78)
    variants = ["baseline", "C-i", "C-ii"]

    # TEST 1 — Composite (A) vs Uniform Line T3 (B)
    out.append("\n[TEST 1] Composite atoms vs Uniform Line T3 — KEY metric")
    out.append("(Current Bii baseline gives composite ~2.7% — should normalize to 35-50%)")
    for v in variants:
        r = matchup(
            lambda ns: make_composite_unit("Composite", "A", ns),
            lambda ns: make_uniform_unit("Line", 3, "Uniform", "B", ns),
            v, n=60
        )
        out.append(format_row(f"{v:10s} composite-A vs uniform-Line-T3-B", r))

    # TEST 2 — Lethality (Line T3 vs Line T3 — must stay in 3-6 turn window)
    out.append("\n[TEST 2] Lethality control — Line T3 vs Line T3 (target: 3-6 turn mean)")
    for v in variants:
        r = matchup(
            lambda ns: make_uniform_unit("Line", 3, "A", "A", ns),
            lambda ns: make_uniform_unit("Line", 3, "B", "B", ns),
            v, n=80
        )
        out.append(format_row(f"{v:10s} Line-T3 mirror", r))

    # TEST 3 — Shape matrix sanity (Arrowhead vs Line, Horseshoe vs Line)
    out.append("\n[TEST 3] Shape matrix — Arrowhead vs Line, Horseshoe vs Line")
    for v in variants:
        r1 = matchup(
            lambda ns: make_uniform_unit("Arrowhead", 3, "Arrow", "A", ns),
            lambda ns: make_uniform_unit("Line", 3, "Line", "B", ns),
            v, n=50
        )
        out.append(format_row(f"{v:10s} Arrowhead vs Line", r1))
        r2 = matchup(
            lambda ns: make_uniform_unit("Horseshoe", 3, "Horse", "A", ns),
            lambda ns: make_uniform_unit("Line", 3, "Line", "B", ns),
            v, n=50
        )
        out.append(format_row(f"{v:10s} Horseshoe vs Line", r2))

    # TEST 4 — Cannae (Horseshoe vs Arrowhead — expected to stay broken)
    out.append("\n[TEST 4] Cannae — Horseshoe vs Arrowhead (expected to stay ~2-10% — fix is B-ii)")
    for v in variants:
        r = matchup(
            lambda ns: make_uniform_unit("Horseshoe", 3, "Horse", "A", ns),
            lambda ns: make_uniform_unit("Arrowhead", 3, "Arrow", "B", ns),
            v, n=50
        )
        out.append(format_row(f"{v:10s} Horseshoe-A vs Arrowhead-B", r))

    out.append("\n" + "=" * 78)
    out.append("INTERPRETATION:")
    out.append("- C-i drops troop-frac → small atoms get full pool (may overcorrect)")
    out.append("- C-ii floors at 50% → small atoms get min(troop-weighted, 50%-floor)")
    out.append("- Pick variant where Test 1 normalizes AND Tests 2-3 don't break")
    out.append("=" * 78)
    return "\n".join(out)

if __name__ == "__main__":
    print(main())
