"""Leave-one-out flag ablation on the historical Cannae OOB, with PC_FRICTION_CEV pinned ON.
Baseline = ALL boolean flags ON. Each row turns exactly ONE flag OFF and reports the change in the
outnumbered side's (Carthage) win-rate, averaged over both deployment sides. A flag whose removal HURTS
is load-bearing; a flag whose removal HELPS is actively costing the historical result.
Run: python flag_ablation.py [n]"""
import os, sys, subprocess, json

ALL = ['PC_CELL_DAMAGE','PC_CLOSE_RANKS','PC_FEIGNED_RETREAT','PC_FRACTIONAL_POOL','PC_FRICTION_CEV',
       'PC_INTENT_RESOLUTION','PC_RESERVE_COMMIT','PC_STOCHASTIC_ROUT','PC_TROOP_DENSITY_CAP',
       'PC_YIELD_EMERGENT','PC_YIELD_POCKET','PC_YIELD_RALLY']
PIN = 'PC_FRICTION_CEV'      # pinned ON in every configuration (Jordan: "if we leave that on")
HERE = os.path.dirname(os.path.abspath(__file__))

RUNNER = r'''
import os, sys, random
sys.path.insert(0, %r); sys.path.insert(0, %r)
import cannae_historical as C
import gauge_mb as g
n = int(os.environ["ABL_N"])
tot = []
for side in ("A","B"):
    c=w=0
    for s in range(n):
        random.seed(1_000_000+s)
        if side=="A": ua=C.carthage("A","A"); ub=C.rome("B","B")
        else: ua=C.rome("A","A"); ub=C.carthage("B","B")
        r=g.resolve_battle(ua,ub,"Line","Line",g.ANCHOR_MAP,kind="multi",max_battle_turns=25)
        wn=r.get("winner","draw"); c+= wn==side; w+= (wn in ("A","B") and wn!=side)
    dec=c+w
    tot.append(100.0*c/dec if dec else 50.0)
print("RESULT", (tot[0]+tot[1])/2.0, tot[0], tot[1])
''' % (HERE, os.path.abspath(os.path.join(HERE,'..','..','tests','sim')))

def run(env_flags, n):
    env = dict(os.environ)
    for f in ALL:
        env[f] = '1' if f in env_flags else '0'
    env['ABL_N'] = str(n)
    out = subprocess.run([sys.executable, '-c', RUNNER], capture_output=True, text=True, env=env, timeout=900)
    for line in out.stdout.splitlines():
        if line.startswith('RESULT'):
            p = line.split()
            return float(p[1]), float(p[2]), float(p[3])
    return None, None, None

if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 12
    base, ba, bb = run(set(ALL), n)
    print(f"BASELINE all-ON: avg {base:5.1f}%  (A {ba:5.1f} / B {bb:5.1f})\n")
    print(f"leave-one-out (PIN {PIN} stays ON):")
    rows = []
    for f in ALL:
        if f == PIN:
            continue
        cfg = set(ALL) - {f}
        avg, a, b = run(cfg, n)
        rows.append((avg - base, f, avg, a, b))
    for d, f, avg, a, b in sorted(rows):
        tag = 'LOAD-BEARING (removal hurts)' if d < -1 else ('COSTLY (removal helps)' if d > 1 else 'neutral')
        print(f"  -{f:24} avg {avg:5.1f}%  delta {d:+6.1f}pp   {tag}")
