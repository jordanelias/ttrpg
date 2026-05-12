"""Diagnostic for Side A bias.
Tests:
  T1: standard A-at-bottom vs B-at-top (current setup)
  T2: swap — A-at-top vs B-at-bottom
  T3: swap arg order — call run_battle(b, a) instead of run_battle(a, b)
Reveals whether bias is from advance_dir, starting position, or arg order."""
import sys, random, statistics
sys.path.insert(0, '/home/claude')

# Load sim
src = open('/home/claude/sim_mb_06_v6_phaseC.py').read()
ns = {}
exec(src, ns)
Unit = ns['Unit']; Atom = ns['Atom']
run_battle = ns['run_battle']
SIDE_A_START_ROW = ns['SIDE_A_START_ROW']
SIDE_B_START_ROW = ns['SIDE_B_START_ROW']

def make_line(name, faction_label, start_row, advance_dir, anchor_col=9):
    """Direct construction — decouple faction label from geometry."""
    atoms = [Atom('Line', 'infantry', 3,
                  starting_position=(start_row, anchor_col),
                  advance_dir=advance_dir)]
    return Unit(name=name, faction=faction_label, power=4, command=4,
                discipline=5, discipline_start=5, morale=6, morale_start=6,
                atoms=atoms, dr=1)

def battery(label, n=60, seed_base=600000, swap_geometry=False, swap_args=False):
    """Run n battles, return winrate of first-arg unit."""
    first_wins = 0; second_wins = 0; draws = 0
    for s in range(n):
        random.seed(s + seed_base)
        if swap_geometry:
            # A label at TOP, B label at BOTTOM
            unit_first = make_line("first", "A", SIDE_B_START_ROW, +1)
            unit_second = make_line("second", "B", SIDE_A_START_ROW, -1)
        else:
            # Standard: A at bottom (rises up), B at top (descends)
            unit_first = make_line("first", "A", SIDE_A_START_ROW, -1)
            unit_second = make_line("second", "B", SIDE_B_START_ROW, +1)
        if swap_args:
            r = run_battle(unit_second, unit_first)
            # In this case unit_second is now "A" in run_battle's view
            # We want to track our designated "first" unit
            winner_is_first = (r["winner"] == "B")
        else:
            r = run_battle(unit_first, unit_second)
            winner_is_first = (r["winner"] == "A")
        if winner_is_first: first_wins += 1
        elif r["winner"] == "draw": draws += 1
        else: second_wins += 1
    print(f"  {label:50s}  first:{first_wins/n*100:5.1f}%  second:{second_wins/n*100:5.1f}%  draw:{draws/n*100:5.1f}%")
    return first_wins / n

print("=" * 78)
print("SIDE BIAS DIAGNOSTIC")
print("=" * 78)
print("\nIf there's no bias, all four runs should be ~50%")
print()

battery("T1 standard: first=bottom(↑), second=top(↓), pass(f,s)")
battery("T2 swap geom: first=top(↓), second=bottom(↑), pass(f,s)", swap_geometry=True)
battery("T3 swap args: first=bottom(↑), second=top(↓), pass(s,f)", swap_args=True)
battery("T4 swap both: first=top(↓), second=bottom(↑), pass(s,f)", swap_geometry=True, swap_args=True)

print("\nInterpretation:")
print("  If T1=T2: bias depends on arg order (run_battle's first arg)")
print("  If T1≠T2 and inverts: bias depends on geometry (advance_dir)")
print("  If all four ~50%: no bias (the previous Test 2 result was a fluke)")
