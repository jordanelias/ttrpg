"""ED-MB-0029 intent-as-resolution probe. Same matched-density mirror lines under different stance
pairings, PC_INTENT_RESOLUTION off vs on (subprocess — flag is import-time). Measures win-split,
mean casualties (both sides), and battle length (tempo). Expected with intent ON:
  hold vs hold        -> slow grind, low casualties (a standoff)
  aggressive vs aggr. -> fast, bloody
  aggressive vs hold  -> holder SURVIVES longer than under balanced (buys time; ~even split)
"""
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

def unit(name, faction, stance, w=6, d=2, conc=100):
    sr = SIDE_A_START_ROW if faction == 'A' else SIDE_B_START_ROW
    return build_army([{'shape':'Line','troop_type':'infantry','unit_type':'melee','stance':stance,
                        'width':w,'depth':d,'troops':w*d*conc,'starting_position':(sr,25)}], name, faction,
                      stance=stance)

def duel(sa, sb, n):
    aw=bw=dr=0; acas=[]; bcas=[]; turns=[]
    for s in range(n):
        random.seed(1_000_000+s)
        ua=unit('A','A',sa); ub=unit('B','B',sb)
        a0,b0=ua.hp_max,ub.hp_max
        r=resolve_battle(ua,ub,'Line','Line',{},kind='multi',max_battle_turns=40)
        w=r.get('winner','draw')
        if w=='A':aw+=1
        elif w=='B':bw+=1
        else:dr+=1
        acas.append(100*(a0-ua.hp)/a0 if a0 else 0); bcas.append(100*(b0-ub.hp)/b0 if b0 else 0)
        turns.append(r.get('battle_turns',40))
    return aw,bw,dr,statistics.mean(acas),statistics.mean(bcas),statistics.mean(turns)

n=int(sys.argv[1])
print('PC_INTENT_RESOLUTION=%s OFF=%s DEF=%s' % (c.PC_INTENT_RESOLUTION, c.INTENT_OFFENSE_D, c.INTENT_DEFENSE_D), flush=True)
for sa,sb in [('balanced','balanced'),('hold','balanced'),('aggressive','balanced'),('aggressive','aggressive'),('aggressive','hold')]:
    aw,bw,dr,ac,bc,t=duel(sa,sb,n)
    print('  A=%-10s B=%-10s A%%=%5.1f B%%=%5.1f D%%=%5.1f  Acas=%4.1f Bcas=%4.1f  t=%4.1f'
          % (sa,sb,100*aw/n,100*bw/n,100*dr/n,ac,bc,t), flush=True)
'''

if __name__ == '__main__':
    n = sys.argv[1] if len(sys.argv) > 1 else '16'
    runner = RUNNER.replace('__SIM__', repr(_SIM))
    for flag in ('0', '1'):
        env = dict(os.environ, PC_INTENT_RESOLUTION=flag)
        print(f"=== PC_INTENT_RESOLUTION={flag} ===", flush=True)
        subprocess.run([sys.executable, '-u', '-c', runner, n], env=env)
