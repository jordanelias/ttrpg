"""Cannae WITH the commanded bait (ED-MB-0041 probe). The DG-2 `yielding` primitive already exists —
"gives ground under pressure but keeps FIGHTING and keeps FACING the threat" — and its entry is
COMMANDED: an Order whose behavior dict sets {'yielding': True} (check_orders applies it by generic
setattr). The earlier Cannae runs never issued that order, which is why PC_FEIGNED_RETREAT/yield showed
+0.0pp. Here the Carthaginian centre advances, makes contact, then is ORDERED to yield — the bait —
while the African columns + cavalry envelop. Run: python cannae_bait.py [n]"""
import os, sys, random
_HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, _HERE)
_SIM = os.path.abspath(os.path.join(_HERE, '..', '..', 'tests', 'sim')); sys.path.insert(0, _SIM)
import gauge_mb as g
import cannae_historical as C
from mass_battle.engine import build_army, SIDE_A_START_ROW, SIDE_B_START_ROW, Order


def carthage_bait(name, faction, yield_trigger='enemy_range:3'):
    """Same OOB as cannae_historical.carthage, but the 3 centre maniples get a YIELD order that fires
    once the enemy closes — the deliberate fighting withdrawal that draws Rome into the pocket."""
    u = C.carthage(name, faction)
    for atom in u.subunits[:3]:                    # the crescent centre
        atom.orders = (Order(yield_trigger, {'yielding': True}),)
    return u


def run(n, carth_side, builder, label):
    c = w = d = 0
    for s in range(n):
        random.seed(1_000_000 + s)
        if carth_side == 'A': ua = builder('A', 'A'); ub = C.rome('B', 'B')
        else: ua = C.rome('A', 'A'); ub = builder('B', 'B')
        r = g.resolve_battle(ua, ub, 'Line', 'Line', g.ANCHOR_MAP, kind='multi', max_battle_turns=25)
        wn = r.get('winner', 'draw')
        c += wn == carth_side; w += (wn in ('A', 'B') and wn != carth_side); d += wn not in ('A', 'B')
    dec = c + w
    return 100.0 * c / dec if dec else 50.0


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 20
    print(f"Historical Cannae — commanded bait vs no bait (n={n}/side)")
    for label, b in (('NO bait (baseline)', C.carthage), ('COMMANDED yield bait', carthage_bait)):
        a = run(n, 'A', b, label); bb = run(n, 'B', b, label)
        print(f"  {label:24} Carthage A {a:5.1f}%   B {bb:5.1f}%   avg {(a+bb)/2:5.1f}%")
