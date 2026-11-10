"""calibrate_kits.py — paired per-ability measurement of the draft's LIVE-lever abilities against PCA section 6.2's band.

    python proposals/2026-11-10-personal-combat-tradition-sets/calibrate_kits.py [--fights N] [--only name,name]

For each ability: fighter A (the teaching tradition, the named weapon, ONE ability at level 1) against fighter B
(tradition 'none', same weapon, no kit), N seeds; then the SAME seeds with A's kit empty. Paired, so the seed
noise cancels. Prints, per ability:
    dWin  = (A wins with the ability - A wins without) / N, in percentage points (a draw counts as no win)
    texture = share of seeds whose event sequence differs; flip = share whose RESULT differs.
PCA band (6.2), at level 1 vs an equal opponent: |dWin| <= 2pp at n >= 2000; texture >= 15% (the repo's own test
floor is 2%, ED-PC-0058: Ob-from-defender halved the true rate); flip 3-10%.
Read-only; merges the draft into the in-process registry copy.
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'modules', 'combat'))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, 'systems', 'combat', 'combat_engine_v1', 'workbench'))
import ability_primitives as ABIL   # noqa: E402
from combatant import Combatant     # noqa: E402
from config import CFG              # noqa: E402
from trace import run_traced_fight  # noqa: E402
import kits_draft as K              # noqa: E402

# (ability, weapon it is exercised on). The weapon is one the tradition teaches AND on which the lever has a site.
PLAN = [('fuehlen', 'longsword'), ('contratempo', 'rapier'), ('sen_no_sen', 'katana'), ('metsuke', 'katana'),
        ('zanshin', 'katana'), ('compas', 'rapier'), ('circulo', 'rapier'), ('shinogi', 'katana'),
        ('indes', 'longsword'), ('staerke_schwaeche', 'longsword'), ('mezzo_tempo', 'rapier'),
        ('misura', 'rapier'), ('true_times', 'arming'), ('atajo', 'rapier')]

draft = {n: a for kit in K.KITS.values() for n, a in kit['abilities'].items() if a['lever_status'] == 'live'}
for n, a in draft.items():
    ABIL.ABILITIES.setdefault(n, a)
for t in ABIL.TRADITION_KIT:
    ABIL.TRADITION_KIT[t] = [a for a, d in ABIL.ABILITIES.items() if d['tradition'] == t]

n = int(sys.argv[sys.argv.index('--fights') + 1]) if '--fights' in sys.argv else 600
only = set(sys.argv[sys.argv.index('--only') + 1].split(',')) if '--only' in sys.argv else None
sig = lambda ev: tuple((e['kind'], e.get('outcome'), e.get('hit')) for e in ev if e['kind'] in ('outcome', 'contact', 'separation'))   # noqa: E731
override = {}
for kv in (sys.argv[sys.argv.index('--set') + 1].split(',') if '--set' in sys.argv else []):
    k, v = kv.split('='); override[k] = float(v)

print(f'{"ability":18s} {"lever":16s} {"weapon":9s} {"value":>6s} {"dWin pp":>8s} {"+-95":>5s} {"texture":>8s} {"flip":>6s}')
for name, weapon in PLAN:
    if only and name not in only:
        continue
    a = ABIL.ABILITIES[name]
    if name in override:
        a = dict(a, value=override[name]); ABIL.ABILITIES[name] = a
    trad = a['tradition']
    d_win = []; tex = flip = 0
    for s in range(n):
        r_on, e_on = run_traced_fight(Combatant('A', weapon=weapon, tradition=trad, equipped=[name]),
                                      Combatant('B', weapon=weapon), cfg=CFG, seed=s)
        r_off, e_off = run_traced_fight(Combatant('A', weapon=weapon, tradition=trad, equipped=[]),
                                        Combatant('B', weapon=weapon), cfg=CFG, seed=s)
        d_win.append((r_on == 1) - (r_off == 1))
        tex += sig(e_on) != sig(e_off); flip += r_on != r_off
    m = sum(d_win) / n
    sd = math.sqrt(sum((x - m) ** 2 for x in d_win) / (n - 1))
    print(f'{name:18s} {a["lever"]:16s} {weapon:9s} {a["value"]:6.2f} {100*m:8.1f} {196*sd/math.sqrt(n):5.1f} {100*tex/n:7.1f}% {100*flip/n:5.1f}%', flush=True)
