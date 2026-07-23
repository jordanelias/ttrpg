"""Wide-mirror symmetry probe: is there a width-scaling side bias? A perfect mirror
MUST be ~50/50. Test increasing frontage width across multiple seed bases."""
import sys, os, random, statistics
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mass_battle.engine import build_army, resolve_battle, SIDE_A_START_ROW, SIDE_B_START_ROW
import mass_battle.config as c


def unit(name, faction, width, depth, conc=100):
    start_row = SIDE_A_START_ROW if faction == 'A' else SIDE_B_START_ROW
    spec = {'shape': 'Line', 'troop_type': 'infantry', 'unit_type': 'melee',
            'width': width, 'depth': depth, 'troops': width * depth * conc,
            'starting_position': (start_row, 25)}
    return build_army([spec], name, faction)


def mirror(width, depth, n=30, seed_base=1_000_000):
    aw = bw = dr = 0
    for s in range(n):
        random.seed(seed_base + s)
        ua = unit('A', 'A', width, depth)
        ub = unit('B', 'B', width, depth)
        r = resolve_battle(ua, ub, 'Line', 'Line', {}, kind='multi', max_battle_turns=30)
        w = r.get('winner', 'draw')
        if w == 'A': aw += 1
        elif w == 'B': bw += 1
        else: dr += 1
    return aw, bw, dr


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 30
    print(f"PC_FRONTAGE_BLEND={c.PC_FRONTAGE_BLEND} n={n} — perfect mirror should be ~50/50", flush=True)
    for w in (2, 4, 6, 12, 18, 24):
        tot_a = tot_b = tot_d = 0
        for sb in (1_000_000, 2_000_000, 3_000_000):
            a, b, d = mirror(w, 1, n=n, seed_base=sb)
            tot_a += a; tot_b += b; tot_d += d
        N = 3 * n
        print(f"  width={w:2} depth=1: A%={100*tot_a/N:5.1f} B%={100*tot_b/N:5.1f} D%={100*tot_d/N:5.1f}  (N={N})", flush=True)
