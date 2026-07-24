"""ED-MB-0031 stochastic-rout probe. Measures casualty-at-rout + battle length with
PC_STOCHASTIC_ROUT off vs on. Target (Jordan historical research): the LOSER should break at
~15-30% casualties, not grind to ~58%."""
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

def unit(name, faction, disc=5, mor=6):
    sr = SIDE_A_START_ROW if faction == 'A' else SIDE_B_START_ROW
    return build_army([{'shape':'Line','troop_type':'infantry','unit_type':'melee','discipline':disc,'morale':mor,
                        'width':6,'depth':2,'troops':1200,'starting_position':(sr,25)}], name, faction, discipline=disc, morale=mor)

def batch(n, disc_a=5, disc_b=5):
    winner_cas=[]; loser_cas=[]; turns=[]; draws=0
    for s in range(n):
        random.seed(3_000_000+s)
        ua=unit('A','A',disc_a); ub=unit('B','B',disc_b)
        a0,b0=ua.hp_max,ub.hp_max
        r=resolve_battle(ua,ub,'Line','Line',{},kind='multi',max_battle_turns=40)
        aca=100*(a0-ua.hp)/a0; bca=100*(b0-ub.hp)/b0
        w=r.get('winner','draw'); turns.append(r.get('battle_turns',40))
        if w=='A': winner_cas.append(aca); loser_cas.append(bca)
        elif w=='B': winner_cas.append(bca); loser_cas.append(aca)
        else: draws+=1
    wc=statistics.mean(winner_cas) if winner_cas else 0
    lc=statistics.mean(loser_cas) if loser_cas else 0
    return wc, lc, statistics.mean(turns), draws

n=int(sys.argv[1])
print('PC_STOCHASTIC_ROUT=%s ONSET=%s CAP=%s' % (c.PC_STOCHASTIC_ROUT, c.ROUT_ONSET_FRAC, c.ROUT_CAP_FRAC), flush=True)
wc,lc,t,d = batch(n)
print('  even (disc5 v disc5): winner_cas=%4.1f%% LOSER_cas=%4.1f%% turns=%4.1f draws=%d' % (wc,lc,t,d), flush=True)
wc,lc,t,d = batch(n, disc_a=5, disc_b=3)
print('  disc5 vs disc3:       winner_cas=%4.1f%% LOSER_cas=%4.1f%% turns=%4.1f draws=%d' % (wc,lc,t,d), flush=True)
'''

if __name__ == '__main__':
    n = sys.argv[1] if len(sys.argv) > 1 else '20'
    runner = RUNNER.replace('__SIM__', repr(_SIM))
    for flag in ('0', '1'):
        env = dict(os.environ, PC_STOCHASTIC_ROUT=flag)
        print(f"=== PC_STOCHASTIC_ROUT={flag} ===", flush=True)
        subprocess.run([sys.executable, '-u', '-c', runner, n], env=env)
