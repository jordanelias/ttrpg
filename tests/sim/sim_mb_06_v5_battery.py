import sys, random, statistics, time
sys.path.insert(0, '/home/claude')
exec(open('/home/claude/sim_mb_06_v5.py').read())

def centered_anchor(shape, tier, target_center_col=10, target_top_row=2):
    cells = CELL_PATTERN_FN[shape](tier)
    min_c = min(c for r, c in cells)
    max_c = max(c for r, c in cells)
    return (target_top_row, target_center_col - (min_c + max_c) // 2)

def make_unit(name, faction, side, shape, tier=3, stance="balanced"):
    base = SIDE_A_START_ROW if side == "A" else SIDE_B_START_ROW
    advance = -1 if side == "A" else 1
    anchor = centered_anchor(shape, tier, 10, base)
    a = Atom(shape=shape, troop_type="infantry", tier=tier,
              starting_position=anchor, advance_dir=advance, stance=stance)
    return Unit(name=name, faction=faction, power=4, command=4, discipline=6,
                discipline_start=6, morale=6, morale_start=6, atoms=[a], dr=1, stance=stance)

def make_composite(name, faction, side, atom_specs, stance="balanced"):
    base = SIDE_A_START_ROW if side == "A" else SIDE_B_START_ROW
    advance = -1 if side == "A" else 1
    atoms = []
    for shape, tier, col in atom_specs:
        atoms.append(Atom(shape=shape, troop_type="infantry", tier=tier,
                           starting_position=(base, col), advance_dir=advance, stance=stance))
    return Unit(name=name, faction=faction, power=4, command=4, discipline=6,
                discipline_start=6, morale=6, morale_start=6, atoms=atoms, dr=1, stance=stance)

def render_state(unit_a, unit_b, turn_label):
    grid = [["." for _ in range(BATTLEFIELD_SIZE)] for _ in range(BATTLEFIELD_SIZE)]
    for atom in unit_a.atoms:
        for r, c in atom.cells():
            if 0 <= r < BATTLEFIELD_SIZE and 0 <= c < BATTLEFIELD_SIZE:
                grid[r][c] = atom.shape[0]
    for atom in unit_b.atoms:
        for r, c in atom.cells():
            if 0 <= r < BATTLEFIELD_SIZE and 0 <= c < BATTLEFIELD_SIZE:
                grid[r][c] = atom.shape[0].lower()
    out = [f"  {turn_label}"]
    out.append("     " + " ".join(f"{c:2d}" for c in range(BATTLEFIELD_SIZE)))
    for r in range(BATTLEFIELD_SIZE):
        out.append(f"   {r:2d}: " + "  ".join(grid[r]))
    return "\n".join(out)

# TESTS

def test_lethality(n=150):
    turns, w = [], {"A":0,"B":0,"draw":0}
    for s in range(n):
        random.seed(s+400000)
        a = make_unit("A","A","A","Line",tier=3)
        b = make_unit("B","B","B","Line",tier=3)
        r = run_battle(a, b)
        turns.append(r["turns"]); w[r["winner"]] += 1
    return {"mean": statistics.mean(turns), "med": statistics.median(turns),
            "rng": (min(turns), max(turns)), "winners": w,
            "one_turn": sum(1 for t in turns if t == 1)}

def test_shape_matrix(n=40, tier=3):
    shapes = ["Line","Arrowhead","Horseshoe","GappedLine","RefusedFlank"]
    m = {}
    for sa in shapes:
        m[sa] = {}
        for sb in shapes:
            wa, drw, tt = 0, 0, 0
            for s in range(n):
                random.seed(s+410000)
                a = make_unit("A","A","A",sa,tier=tier)
                b = make_unit("B","B","B",sb,tier=tier)
                r = run_battle(a, b)
                tt += r["turns"]
                if r["winner"] == "A": wa += 1
                elif r["winner"] == "draw": drw += 1
            m[sa][sb] = {"win": wa/n, "turns": tt/n, "draws": drw}
    return m

def test_horseshoe_cannae(n=100):
    """Horseshoe (defender, Side A) vs Arrowhead (attacker, Side B).
    Wings should race forward, center holds, envelopment fires."""
    wh, wa, drw, tt = 0, 0, 0, 0
    for s in range(n):
        random.seed(s+420000)
        h = make_unit("HS","A","A","Horseshoe",tier=3)
        ar = make_unit("AR","B","B","Arrowhead",tier=3)
        r = run_battle(h, ar)
        tt += r["turns"]
        if r["winner"] == "A": wh += 1
        elif r["winner"] == "B": wa += 1
        else: drw += 1
    return {"hs": wh, "ar": wa, "draws": drw, "hs_winrate": wh/n, "turns": tt/n}

def test_composite_vs_uniform(n=150):
    wc, wu, drw, tt = 0, 0, 0, 0
    for s in range(n):
        random.seed(s+430000)
        c = make_composite("C","A","A",[
            ("Arrowhead", 1, 2),
            ("Arrowhead", 1, 7),
            ("Line", 1, 13),
            ("Arrowhead", 1, 16),
        ])
        u = make_unit("U","B","B","Line",tier=3)
        r = run_battle(c, u)
        tt += r["turns"]
        if r["winner"] == "A": wc += 1
        elif r["winner"] == "B": wu += 1
        else: drw += 1
    return {"c": wc, "u": wu, "draws": drw, "c_winrate": wc/n, "turns": tt/n}

def test_horseshoe_with_orders(n=100):
    """Player orders: Horseshoe wings target Arrowhead's tip (encircle the point).
    Center holds (passive bait)."""
    wh, wa, drw, tt = 0, 0, 0, 0
    for s in range(n):
        random.seed(s+440000)
        h = make_unit("HS","A","A","Horseshoe",tier=3)
        ar = make_unit("AR","B","B","Arrowhead",tier=3)
        # No multi-atom unit here so orders don't apply (single atom on each side)
        r = run_battle(h, ar)
        tt += r["turns"]
        if r["winner"] == "A": wh += 1
        elif r["winner"] == "B": wa += 1
        else: drw += 1
    return {"hs": wh, "ar": wa, "draws": drw, "hs_winrate": wh/n}

def show_horseshoe_evolution():
    """Show Horseshoe vs Arrowhead at turns 0, 3, 6, 9 to verify deformation."""
    random.seed(99999)
    h = make_unit("HS","A","A","Horseshoe",tier=3)
    ar = make_unit("AR","B","B","Arrowhead",tier=3)
    out = [render_state(h, ar, "Turn 0 (initial)")]
    for t in [3, 6, 9]:
        random.seed(99999)
        h2 = make_unit("HS","A","A","Horseshoe",tier=3)
        ar2 = make_unit("AR","B","B","Arrowhead",tier=3)
        for _ in range(t):
            if h2.routed or ar2.routed: break
            pre_pairs = find_contacts(h2, ar2)
            for atom in h2.atoms + ar2.atoms:
                atom.halted_cells = set()
            for p in pre_pairs:
                for cell in p["a_cells"]:
                    pattern = CELL_PATTERN_FN[p["atom_a"].shape](p["atom_a"].tier)
                    for r, c in pattern:
                        abs_r = p["atom_a"].starting_position[0] + r + p["atom_a"].cell_offsets.get((r,c), 0) * p["atom_a"].advance_dir
                        abs_c = p["atom_a"].starting_position[1] + c + p["atom_a"].cell_offsets_c.get((r,c), 0)
                        if (abs_r, abs_c) == cell:
                            p["atom_a"].halted_cells.add((r, c)); break
                for cell in p["b_cells"]:
                    pattern = CELL_PATTERN_FN[p["atom_b"].shape](p["atom_b"].tier)
                    for r, c in pattern:
                        abs_r = p["atom_b"].starting_position[0] + r + p["atom_b"].cell_offsets.get((r,c), 0) * p["atom_b"].advance_dir
                        abs_c = p["atom_b"].starting_position[1] + c + p["atom_b"].cell_offsets_c.get((r,c), 0)
                        if (abs_r, abs_c) == cell:
                            p["atom_b"].halted_cells.add((r, c)); break
            assign_targets(h2, ar2)
            for atom in h2.atoms:
                if atom.target_atom: atom.advance_cells(h2.discipline, atom.target_atom.centroid())
            for atom in ar2.atoms:
                if atom.target_atom: atom.advance_cells(ar2.discipline, atom.target_atom.centroid())
        out.append(render_state(h2, ar2, f"Turn {t}"))
    return "\n\n".join(out)

def main():
    out = ["=" * 72, "SIM-MB-06 v5 — Per-cell movement + Bii pool + Ciii orders + Eiii", "=" * 72]

    out.append("\n## DEFORMATION RENDER: Horseshoe (A) vs Arrowhead (B) over time")
    out.append("  (Watch Horseshoe wings race forward while center holds; Arrowhead tip drives in)")
    out.append(show_horseshoe_evolution())

    out.append("\n## Lethality (Line v Line, Size 4)")
    l = test_lethality()
    out.append(f"  Mean turns: {l['mean']:.2f} | Median: {l['med']} | Range: {l['rng']}")
    out.append(f"  Winners: {l['winners']} | One-turn kills: {l['one_turn']}")

    out.append("\n## Shape matrix (40 trials)")
    m = test_shape_matrix(40, tier=3)
    shapes = ["Line","Arrowhead","Horseshoe","GappedLine","RefusedFlank"]
    out.append(f"  {'':14s} " + " ".join(f"{s[:8]:>8s}" for s in shapes))
    for sa in shapes:
        row = [f"  {sa[:14]:14s} "]
        for sb in shapes:
            d = m[sa][sb]
            row.append(f"{d['win']*100:>3.0f}%/{d['turns']:>4.1f}")
        out.append(" ".join(row))

    out.append("\n## CANNAE TEST: Horseshoe (defender) vs Arrowhead (attacker), 100 trials")
    c = test_horseshoe_cannae()
    out.append(f"  Horseshoe wins: {c['hs']} ({c['hs_winrate']*100:.1f}%)")
    out.append(f"  Arrowhead wins: {c['ar']} | Draws: {c['draws']} | Turns: {c['turns']:.1f}")
    out.append(f"  Historical target: Horseshoe should win 60-80% via envelopment")

    out.append("\n## Composite (4×T1) vs Uniform T3 Line (equal 400 troops)")
    cv = test_composite_vs_uniform()
    out.append(f"  Composite wins: {cv['c']} ({cv['c_winrate']*100:.1f}%)")
    out.append(f"  Uniform wins: {cv['u']} | Draws: {cv['draws']} | Turns: {cv['turns']:.1f}")
    out.append(f"  Target 40-60%: {'✓' if 0.40 <= cv['c_winrate'] <= 0.60 else '⚠'}")

    out.append("\n" + "=" * 72)
    return "\n".join(out)

if __name__ == "__main__":
    print(main())
