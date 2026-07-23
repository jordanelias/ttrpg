"""ED-MB-0028 effect probe: does cell-level close-ranks change combat outcomes by sustaining
front-cell density from the rear? Compares a moderately-deep column vs a wide-shallow line at
equal troops+density, with PC_CLOSE_RANKS off vs on (subprocess, since the flag is import-time)."""
import os
import subprocess
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_SIM = os.path.abspath(os.path.join(_HERE, '..', '..', 'tests', 'sim'))

RUNNER = r'''
import sys, os, random, statistics
sys.path.insert(0, __SIM__)
from mass_battle.engine import build_army, resolve_battle, SIDE_A_START_ROW, SIDE_B_START_ROW
import mass_battle.config as c

def unit(name, faction, w, d, conc=100):
    sr = SIDE_A_START_ROW if faction == 'A' else SIDE_B_START_ROW
    return build_army([{'shape':'Line','troop_type':'infantry','unit_type':'melee',
                        'width':w,'depth':d,'troops':w*d*conc,'starting_position':(sr,25)}], name, faction)

def duel(wa, da, wb, db, n):
    aw=bw=dr=0
    for s in range(n):
        random.seed(1_000_000+s)
        r=resolve_battle(unit('A','A',wa,da), unit('B','B',wb,db), 'Line','Line',{},kind='multi',max_battle_turns=40)
        w=r.get('winner','draw')
        if w=='A':aw+=1
        elif w=='B':bw+=1
        else:dr+=1
    return aw,bw,dr

n=int(sys.argv[1])
print('PC_CLOSE_RANKS=%s' % c.PC_CLOSE_RANKS, flush=True)
for (wa,da,wb,db,label) in [(4,3,12,1,'DEEP(4x3) vs WIDE(12x1)'),(3,4,6,2,'DEEP(3x4) vs SEMI(6x2)'),(6,2,6,2,'mirror(6x2)')]:
    a,b,d=duel(wa,da,wb,db,n)
    print('  %-26s A%%=%5.1f B%%=%5.1f D%%=%5.1f' % (label,100*a/n,100*b/n,100*d/n), flush=True)
'''

if __name__ == '__main__':
    n = sys.argv[1] if len(sys.argv) > 1 else '16'
    runner = RUNNER.replace('__SIM__', repr(_SIM))
    for flag in ('0', '1'):
        env = dict(os.environ, PC_CLOSE_RANKS=flag)
        print(f"=== PC_CLOSE_RANKS={flag} ===", flush=True)
        subprocess.run([sys.executable, '-u', '-c', runner, n], env=env)
