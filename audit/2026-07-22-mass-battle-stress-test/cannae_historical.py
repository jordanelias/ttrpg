"""Historically-faithful Cannae (216 BC) — Jordan directive: match the REAL battle's spread, subunit
count and force ratio (5000 Carthage vs 8600 Rome, ~1.72:1). Rome's infantry is GRANULAR maniples (a
monolith can't be enveloped — ED-MB-0038) in a DEEP, limited-frontage mass; Carthage has a thin wide
crescent centre (baits) + 2 deep African flank columns + CAVALRY SUPERIORITY (~2:1) that wheels to the
rear. Subunit cap is 11/side. Test: does the engine reproduce a Carthaginian win while outnumbered?
Run: python cannae_historical.py [n]"""
import os, sys, random
_HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, _HERE)
_SIM = os.path.abspath(os.path.join(_HERE, '..', '..', 'tests', 'sim')); sys.path.insert(0, _SIM)
import gauge_mb as g
from mass_battle.engine import build_army, SIDE_A_START_ROW, SIDE_B_START_ROW, Order
CONC = 100.0

def sp(col, row, troops, w, d, tt='infantry', stance='balanced', instr=()):
    return {'shape': 'Line', 'troop_type': tt, 'troops': float(troops), 'concentration': CONC,
            'width': w, 'depth': d, 'stance': stance, 'instructions': tuple(instr),
            'starting_position': (row, int(round(col)))}

def carthage(name, faction):
    r = SIDE_A_START_ROW if faction == 'A' else SIDE_B_START_ROW
    A = 20
    subs = []
    # thin WIDE crescent centre (Gauls/Spanish) — 3 maniples spanning frontage ~9, shallow (baits)
    for i,c in enumerate((A-3, A, A+3)):
        subs.append(sp(c, r, 600, 3, 2, stance='hold'))
    # 2 deep African veteran columns at the crescent's ends
    afr_L = sp(A-6, r, 1000, 2, 5, stance='hold', instr=('envelop',))
    afr_R = sp(A+6, r, 1000, 2, 5, stance='hold', instr=('envelop',))
    # cavalry superiority: heavy (decisive, wheels rear) left, Numidian light right
    cav_L = sp(A-11, r, 800, 2, 1, tt='cavalry', stance='hold', instr=('envelop',))
    cav_R = sp(A+11, r, 400, 1, 1, tt='cavalry', stance='hold', instr=('envelop',))
    u = build_army(subs + [afr_L, afr_R, cav_L, cav_R], name, faction, speed='Fast')
    for atom in u.subunits[3:]:                      # flanks + cavalry release into envelopment after the bait
        rel = tuple(dict.fromkeys(atom.instructions + ('envelop',)))
        atom.orders = (Order('tick:4', {'stance': 'balanced', 'instructions': rel}),)
    return u

def rome(name, faction, grid=(3,3)):
    r = SIDE_A_START_ROW if faction == 'A' else SIDE_B_START_ROW
    A = 20
    nw, nd = grid
    per = 8000.0 / (nw*nd)
    subs = []
    row_step = -1 if faction == 'A' else 1
    for gd in range(nd):                              # deep grid of maniples (frontage nw*3, depth nd*3)
        for gw in range(nw):
            col = A + (gw - (nw-1)/2.0)*3
            rr = r + gd*3*row_step
            subs.append(sp(col, rr, per, 3, 3))
    subs[0]['starting_position'] = subs[0]['starting_position']  # noop
    cav_L = sp(A-11, r, 300, 1, 1, tt='cavalry')
    cav_R = sp(A+11, r, 300, 1, 1, tt='cavalry')
    return build_army(subs + [cav_L, cav_R], name, faction, speed='Standard')

def show(u, label):
    print(f"  {label}: {len(u.subunits)} subunits, total {int(round(u.hp))}")
    for a in u.subunits:
        cells=list(a.cells()); rows=len(set(x for x,_ in cells)); cols=len(set(y for _,y in cells))
        print(f"      {a.troop_type:8} {int(round(a.troop_total())):5}  frontage {cols} x depth {rows}")

def run(n, carth_side='A'):
    C=W=D=0
    for s in range(n):
        random.seed(1_000_000+s)
        if carth_side=='A': ua=carthage('A','A'); ub=rome('B','B')
        else: ua=rome('A','A'); ub=carthage('B','B')
        r=g.resolve_battle(ua,ub,'Line','Line',g.ANCHOR_MAP,kind='multi',max_battle_turns=25)
        w=r.get('winner','draw'); C+=w==carth_side; W+=(w in('A','B') and w!=carth_side); D+=w not in('A','B')
    dec=C+W
    print(f"  Carthage side {carth_side}: Carthage {C:2} Rome {W:2} draw {D:2}  Carthage-win {100.0*C/dec if dec else 50:5.1f}%")

if __name__=='__main__':
    n=int(sys.argv[1]) if len(sys.argv)>1 else 30
    random.seed(1); show(carthage('A','A'),'CARTHAGE ~5000'); show(rome('B','B'),'ROME ~8600')
    print(f"\nHistorical Cannae (n={n}) — engine should reproduce a Carthaginian win while outnumbered:")
    run(n,'A'); run(n,'B')
