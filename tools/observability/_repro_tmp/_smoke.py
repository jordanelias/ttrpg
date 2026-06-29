import sys, os, traceback
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)   # make every flat module importable; engine's /home/claude inserts are harmless no-ops on win

import numpy as np

print("=== STEP 1: import engine modules ===")
import core
import combatant
from combatant import Combatant
import systems as S
import tradition as TR
from config import CFG
import wrapper
print("  imports OK")
print("  core.DECISIVE_OB =", core.DECISIVE_OB, " core.TN =", core.TN)
print("  resolution_pool(3) =", core.resolution_pool(3), " (expect max(5,3+6)=9)")
print("  resolution_pool(0) =", core.resolution_pool(0))

def winrate(makeA, makeB, n, seed=12345):
    rng = np.random.default_rng(seed)
    A = makeA(); B = makeB()
    wins = 0; draws = 0
    for _ in range(n):
        r = wrapper.fight(A, B, cfg=CFG, rng=rng)
        if r == 1: wins += 1
        elif r == 0: draws += 1
    decided = n - draws
    wr = wins/decided if decided else float('nan')
    return wins, draws, decided, wr

print("\n=== STEP 2: MIRROR uniform-4 (expect ~50% A-win of decided) ===")
def u4(w='arming', ar='light'):
    return lambda: Combatant('X', strength=4, agi=4, end=4, cog=4, att=4, spirit=4, focus=4,
                             history=4, disp=4, weapon=w, armor=ar, tradition='none')
for n in (300, 1000):
    w,d,dec,wr = winrate(u4(), u4(), n)
    print(f"  N={n}: A-wins={w} draws={d} decided={dec} A-winrate_of_decided={wr:.3f}")

print("\n=== STEP 3: asymmetric matchups ===")
# Strength edge
w,d,dec,wr = winrate(
    lambda: Combatant('S', strength=5, agi=4, end=4, cog=4, att=4, spirit=4, focus=4, history=4, weapon='arming', armor='light'),
    lambda: Combatant('w', strength=3, agi=4, end=4, cog=4, att=4, spirit=4, focus=4, history=4, weapon='arming', armor='light'),
    600)
print(f"  Str5 vs Str3 (arming/light): A-winrate_of_decided={wr:.3f} draws={d}/{600}")

# History (skill/pool) edge
w,d,dec,wr = winrate(
    lambda: Combatant('H', strength=4, agi=4, end=4, cog=4, att=4, spirit=4, focus=4, history=5, weapon='arming', armor='light'),
    lambda: Combatant('h', strength=4, agi=4, end=4, cog=4, att=4, spirit=4, focus=4, history=2, weapon='arming', armor='light'),
    600)
print(f"  Hist5 vs Hist2 (arming/light): A-winrate_of_decided={wr:.3f} draws={d}/{600}")

# Armour edge (heavy vs none)
w,d,dec,wr = winrate(
    lambda: Combatant('P', strength=4, agi=4, end=4, cog=4, att=4, spirit=4, focus=4, history=4, weapon='arming', armor='heavy'),
    lambda: Combatant('n', strength=4, agi=4, end=4, cog=4, att=4, spirit=4, focus=4, history=4, weapon='arming', armor='none'),
    600)
print(f"  heavy-armor vs none (arming): A-winrate_of_decided={wr:.3f} draws={d}/{600}")

# Weapon mirror sanity (longsword mirror should also be ~50)
w,d,dec,wr = winrate(u4('longsword'), u4('longsword'), 600)
print(f"  longsword MIRROR: A-winrate_of_decided={wr:.3f} draws={d}/{600}")

# Reach matchup: spear vs dagger
w,d,dec,wr = winrate(
    lambda: Combatant('SP', strength=4, agi=4, end=4, cog=4, att=4, spirit=4, focus=4, history=4, weapon='spear', armor='light'),
    lambda: Combatant('DG', strength=4, agi=4, end=4, cog=4, att=4, spirit=4, focus=4, history=4, weapon='dagger', armor='light'),
    600)
print(f"  spear vs dagger: A(spear)-winrate_of_decided={wr:.3f} draws={d}/{600}")

print("\n=== STEP 4: single-fight damage / wound sanity ===")
A = Combatant('A', strength=4, weapon='arming', armor='light')
B = Combatant('B', strength=4, weapon='arming', armor='light')
# even success damage should be ~1 WI per design note
d_succ = core.damage('success', B.weight, B.head, 4, 'light', False, CFG['DAMAGE_SCALE'], CFG['CAP_END'])
d_ow   = core.damage('overwhelming', B.weight, B.head, 4, 'light', False, CFG['DAMAGE_SCALE'], CFG['CAP_END'])
print(f"  even Success arming vs light dmg={d_succ}  overwhelming={d_ow}  (design: even Success ~= 1 WI; WI~9)")
print("  WoundTracker End4: health_full=", B.wt.health_full, " wi=", getattr(B.wt,'wi',None), " max_wounds=", getattr(B.wt,'max_wounds',None))
print("\nALL SMOKE STEPS COMPLETED")
