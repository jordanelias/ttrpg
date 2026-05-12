"""SIM-MB-06 v7 Phase E battery — tip support constraint at different gap values.
Goal: Arrowhead-vs-Line winrate climbs from 0% (current) to ~40-60% with tip support."""
import sys, random, statistics
sys.path.insert(0, '/home/claude')

def load_sim(enabled, gap):
    """Load sim with tip support settings."""
    src = open('/home/claude/sim_mb_06_v7_phaseE.py').read()
    src = src.replace(f'TIP_SUPPORT_ENABLED = True', f'TIP_SUPPORT_ENABLED = {enabled}', 1)
    src = src.replace('TIP_SUPPORT_GAP = 2', f'TIP_SUPPORT_GAP = {gap}', 1)
    ns = {}
    exec(src, ns)
    return ns

def make_uniform_unit(shape, tier, name, faction, sim_ns):
    Unit = sim_ns['Unit']; Atom = sim_ns['Atom']
    advance_dir = -1 if faction == 'A' else 1
    start_row = sim_ns['SIDE_A_START_ROW'] if faction == 'A' else sim_ns['SIDE_B_START_ROW']
    anchor_map = {
        ('Line', 1): 11, ('Line', 2): 10, ('Line', 3): 9, ('Line', 4): 8,
        ('Arrowhead', 1): 11, ('Arrowhead', 2): 10, ('Arrowhead', 3): 8, ('Arrowhead', 4): 7,
        ('Horseshoe', 1): 11, ('Horseshoe', 2): 10, ('Horseshoe', 3): 8, ('Horseshoe', 4): 7,
        ('GappedLine', 1): 11, ('GappedLine', 2): 10, ('GappedLine', 3): 8, ('GappedLine', 4): 7,
        ('RefusedFlank', 1): 11, ('RefusedFlank', 2): 10, ('RefusedFlank', 3): 9, ('RefusedFlank', 4): 8,
    }
    anchor_col = anchor_map.get((shape, tier), 10)
    atoms = [Atom(shape, 'infantry', tier,
                  starting_position=(start_row, anchor_col),
                  advance_dir=advance_dir)]
    return Unit(name=name, faction=faction, power=4, command=4,
                discipline=5, discipline_start=5, morale=6, morale_start=6,
                atoms=atoms, dr=1)

def matchup(make_a, make_b, enabled, gap, n=100, seed_base=700000):
    sim_ns = load_sim(enabled, gap)
    a_wins = 0; b_wins = 0; draws = 0; turns_list = []
    for s in range(n):
        random.seed(s + seed_base)
        a = make_a(sim_ns); b = make_b(sim_ns)
        r = sim_ns['run_battle'](a, b)
        if r['winner'] == 'A': a_wins += 1
        elif r['winner'] == 'B': b_wins += 1
        else: draws += 1
        turns_list.append(r.get('turns', 15))
    return {
        "a_pct": a_wins/n*100, "b_pct": b_wins/n*100, "draw_pct": draws/n*100,
        "mean_turns": statistics.mean(turns_list), "n": n
    }

def row(label, r):
    return f"  {label:45s}  A:{r['a_pct']:5.1f}%  B:{r['b_pct']:5.1f}%  D:{r['draw_pct']:5.1f}%  t={r['mean_turns']:.1f}"

def main():
    out = ["="*78, "SIM-MB-06 v7 Phase E — tip support constraint", "="*78]
    configs = [
        ("OFF (baseline)",   False, 99),
        ("X=1 strict",       True,  1),
        ("X=2 moderate",     True,  2),
        ("X=3 loose",        True,  3),
    ]
    # KEY test: Arrowhead vs Line (currently 0%, target 40-60%)
    out.append("\n[TEST 1] Arrowhead vs Line — KEY metric for tension E")
    out.append("Baseline: 0% (tip races forward, dies isolated).")
    for label, enabled, gap in configs:
        r = matchup(
            lambda ns: make_uniform_unit("Arrowhead", 3, "A", "A", ns),
            lambda ns: make_uniform_unit("Line", 3, "B", "B", ns),
            enabled, gap, n=80
        )
        out.append(row(f"{label}: Arrowhead-A vs Line-B", r))

    # Sanity: tip support shouldn't hurt unaffected matchups
    out.append("\n[TEST 2] Line vs Line mirror (no fast cells — should be unchanged)")
    for label, enabled, gap in configs:
        r = matchup(
            lambda ns: make_uniform_unit("Line", 3, "A", "A", ns),
            lambda ns: make_uniform_unit("Line", 3, "B", "B", ns),
            enabled, gap, n=60
        )
        out.append(row(f"{label}: Line-A vs Line-B", r))

    # Cannae check — Horseshoe wings vs Arrowhead tip with constraint
    out.append("\n[TEST 3] Cannae — Horseshoe vs Arrowhead (tip support changes Arrow dynamics)")
    for label, enabled, gap in configs:
        r = matchup(
            lambda ns: make_uniform_unit("Horseshoe", 3, "H", "A", ns),
            lambda ns: make_uniform_unit("Arrowhead", 3, "Arr", "B", ns),
            enabled, gap, n=60
        )
        out.append(row(f"{label}: Horseshoe-A vs Arrowhead-B", r))

    # Arrowhead vs Horseshoe — reversed Cannae
    out.append("\n[TEST 4] Arrowhead vs Horseshoe — does tip support help Arrowhead break through?")
    for label, enabled, gap in configs:
        r = matchup(
            lambda ns: make_uniform_unit("Arrowhead", 3, "Arr", "A", ns),
            lambda ns: make_uniform_unit("Horseshoe", 3, "H", "B", ns),
            enabled, gap, n=60
        )
        out.append(row(f"{label}: Arrowhead-A vs Horseshoe-B", r))

    # Shape matrix sanity
    out.append("\n[TEST 5] Tier sweep — Arrowhead vs Line at T2, T3, T4")
    for tier in [2, 3, 4]:
        for label, enabled, gap in configs:
            r = matchup(
                lambda ns, t=tier: make_uniform_unit("Arrowhead", t, "A", "A", ns),
                lambda ns, t=tier: make_uniform_unit("Line", t, "B", "B", ns),
                enabled, gap, n=50
            )
            out.append(row(f"{label}: Arrowhead T{tier} vs Line T{tier}", r))

    out.append("\n" + "="*78)
    out.append("INTERPRETATION:")
    out.append("- X=1 strict: tip can be 1 ahead, very tight cohesion")
    out.append("- X=2 moderate: tip can be 2 ahead, allows wedge formation")
    out.append("- X=3 loose: tip can be 3 ahead, close to unconstrained")
    out.append("- Pick gap value that rescues Arrowhead vs Line without breaking Cannae")
    out.append("="*78)
    return "\n".join(out)

if __name__ == "__main__":
    print(main())
