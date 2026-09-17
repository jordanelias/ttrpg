"""Isolate the envelopment side-asymmetry: same two armies, swap which is A/B, same seeds.
If the engine were side-symmetric the enveloper's decisive win-rate would match. Run: python side_probe.py [n]"""
import os, sys, random
_HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, _HERE)
_SIM = os.path.abspath(os.path.join(_HERE, '..', '..', 'tests', 'sim')); sys.path.insert(0, _SIM)
import gauge_mb as g

def trial(n, env_side):
    ew=lw=d=0
    for s in range(n):
        random.seed(1_000_000+s)
        if env_side == 'A':
            ua = g._envelop_army('A','A'); ub = g._command_army('Line')('B','B')
        else:
            ua = g._command_army('Line')('A','A'); ub = g._envelop_army('B','B')
        r = g.resolve_battle(ua,ub,'Line','Line',g.ANCHOR_MAP,kind='multi',max_battle_turns=20)
        w = r.get('winner','draw')
        env_won = (w == env_side)
        line_won = (w in ('A','B') and w != env_side)
        ew += env_won; lw += line_won; d += not (env_won or line_won)
    dec = ew+lw
    print(f"  enveloper as side {env_side}: enveloper {ew:2}  line {lw:2}  draw {d:2}   env decisive-win {100.0*ew/dec if dec else 50:5.1f}%")

if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 40
    print(f"Envelop vs 3-command Line, sides swapped, same seeds, n={n}")
    trial(n, 'A'); trial(n, 'B')
