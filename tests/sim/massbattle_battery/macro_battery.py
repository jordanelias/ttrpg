"""Macro + micro mass-battle battery — demonstrates the cell -> subunit -> unit hierarchy
with army-level (macro) strategy AND subunits in distinct roles (micro), all components wired.

LAYER 1 (micro): ONE unit = several subunits in distinct roles (Anvil heavy infantry,
  Shock cavalry, Skirmish light infantry). Driven tick-by-tick via run_battle(max_turns=1)
  (positions persist; byte-exact to run_battle(N)) so per-subunit trajectories are captured.

LAYER 2 (macro): an ARMY = several units, fought via run_multi_unit_battle. Army-level
  envelopment emerges from wing victories -> freed flankers -> pursuit -> morale cascade /
  rout contagion across adjacent pairings. Sampled over seeds for a win-rate.

Run (from repo root):
  PER_CELL=1 LANCHESTER_ENABLED=1 COMMAND_SIGMA_ENABLED=1 PC_BRACE_ENABLED=1 \
    python tests/sim/massbattle_battery/macro_battery.py
Output: tests/sim/massbattle_battery/macro_micro_telemetry.json  (+ console summary)
"""
import os, sys, json, random

for _k in ('PER_CELL', 'LANCHESTER_ENABLED', 'COMMAND_SIGMA_ENABLED', 'PC_BRACE_ENABLED'):
    os.environ.setdefault(_k, '1')

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..'))   # tests/sim -> mass_battle pkg

from mass_battle.config import SIDE_A_START_ROW, SIDE_B_START_ROW   # noqa: E402
from mass_battle.orchestration import (                             # noqa: E402
    Subunit, Unit, run_battle, run_multi_unit_battle)

ANCHOR_MAP = {
    ('Line', 1): 11, ('Line', 2): 10, ('Line', 3): 9, ('Line', 4): 8,
    ('Arrowhead', 1): 11, ('Arrowhead', 2): 10, ('Arrowhead', 3): 8, ('Arrowhead', 4): 7,
    ('Horseshoe', 1): 11, ('Horseshoe', 2): 10, ('Horseshoe', 3): 8, ('Horseshoe', 4): 7,
    ('GappedLine', 1): 11, ('GappedLine', 2): 9, ('GappedLine', 3): 7,
    ('RefusedFlank', 1): 11, ('RefusedFlank', 2): 10, ('RefusedFlank', 3): 9,
}


def _sub(faction, troop_type, shape, col, tier=3, unit_type='melee', stance='balanced', instructions=()):
    row = SIDE_A_START_ROW if faction == 'A' else SIDE_B_START_ROW
    adv = -1 if faction == 'A' else 1
    return Subunit.of_type(troop_type, shape, tier, (row, col), advance_dir=adv,
                           unit_type=unit_type, stance=stance, instructions=tuple(instructions))


def mk_unit(faction, name, subs, command=4, discipline=5, morale=6, power=4,
            stance='balanced', speed='Standard', dr=1):
    return Unit(name=name, faction=faction, power=power, command=command,
                discipline=discipline, discipline_start=discipline,
                morale=morale, morale_start=morale, subunits=subs, dr=dr,
                stance=stance, speed=speed)


def snap_subunit(role, a):
    return dict(
        role=role, troop_type=a.troop_type, shape=a.shape, unit_type=a.unit_type,
        troops=round(float(getattr(a, 'cur_troops', getattr(a, 'troop_count', 0))), 1),
        cohesion=round(float(getattr(a, 'cohesion', 0.0)), 3),
        morale=round(float(getattr(a, 'eff_morale', 0.0)), 2),
        discipline=round(float(getattr(a, 'eff_discipline', 0.0)), 2),
        routed=bool(getattr(a, 'routed', False)),
        broken=bool(getattr(a, 'broken', False)),
    )


# ───────────────────────── LAYER 1: micro (subunits in distinct roles) ─────────────────────────
def layer1_micro(seed=1_000_000, max_ticks=24):
    """A combined-arms unit (Anvil + Shock + Skirmish subunits) vs a plain heavy line.
    Captures the per-subunit trajectory so distinct roles + per-subunit degradation are visible."""
    random.seed(seed)
    # Side A: ONE unit, three subunits in distinct roles (distinct columns = distinct frontage).
    roles_a = [
        ('Anvil (heavy inf)',     _sub('A', 'heavy_infantry', 'Line',      10, instructions=('brace', 'hold'), stance='hold')),
        ('Shock (cavalry)',       _sub('A', 'cavalry',        'Arrowhead', 15, instructions=('charge',), stance='aggressive')),
        ('Skirmish (light inf)',  _sub('A', 'light_infantry', 'GappedLine', 5, instructions=('harass',))),
    ]
    ua = mk_unit('A', 'CombinedArms', [s for _, s in roles_a], command=5, discipline=5, morale=6, speed='Fast')
    # Side B: a plain heavy-infantry line (single role) at the matching columns.
    roles_b = [('Heavy line', _sub('B', 'heavy_infantry', 'Line', 10))]
    ub = mk_unit('B', 'HeavyLine', [s for _, s in roles_b], command=4, discipline=5, morale=6)

    timeline = []
    timeline.append(dict(tick=0,
                         A=[snap_subunit(r, s) for r, s in roles_a],
                         B=[snap_subunit(r, s) for r, s in roles_b],
                         A_hp=round(ua.hp, 1), B_hp=round(ub.hp, 1)))
    for t in range(1, max_ticks + 1):
        run_battle(ua, ub, max_turns=1)          # advance ONE tick (positions persist)
        timeline.append(dict(tick=t,
                             A=[snap_subunit(r, s) for r, s in roles_a],
                             B=[snap_subunit(r, s) for r, s in roles_b],
                             A_hp=round(ua.hp, 1), B_hp=round(ub.hp, 1)))
        if ua.routed or ub.routed:
            break
    return dict(scenario='combined-arms unit (3 roles) vs heavy line',
                A_roles=[r for r, _ in roles_a], B_roles=[r for r, _ in roles_b],
                final_winner=('B' if ua.routed and not ub.routed else 'A' if ub.routed and not ua.routed else 'draw'),
                ticks=len(timeline) - 1, timeline=timeline)


# ───────────────────────── LAYER 2: macro (army of units, envelopment) ─────────────────────────
def build_army(faction, plan):
    """plan = list of (name, troop_type, shape, command, discipline, morale, power, speed)."""
    units, shapes = [], {}
    for i, (name, tt, shape, cmd, disc, mor, pw, spd) in enumerate(plan):
        su = _sub(faction, tt, shape, ANCHOR_MAP.get((shape, 3), 10))
        units.append(mk_unit(faction, name, [su], command=cmd, discipline=disc,
                             morale=mor, power=pw, speed=spd,
                             stance='aggressive' if tt == 'cavalry' else 'balanced'))
        shapes[i] = shape
    return units, shapes


# Combined-arms double envelopment: A's fast cavalry wings vs B's weak levy flanks; heavy centers clash.
PLAN_A = [
    ('A-leftCav',  'cavalry',        'Arrowhead', 5, 5, 5, 5, 'Fast'),
    ('A-center',   'heavy_infantry', 'Line',      5, 5, 6, 4, 'Slow'),
    ('A-rightCav', 'cavalry',        'Arrowhead', 5, 5, 5, 5, 'Fast'),
]
PLAN_B = [
    ('B-leftLevy', 'levy',           'Line', 3, 1, 2, 1, 'Standard'),
    ('B-center',   'heavy_infantry', 'Line', 5, 5, 6, 4, 'Slow'),
    ('B-rightLevy','levy',           'Line', 3, 1, 2, 1, 'Standard'),
]
PAIRINGS = [(0, 0), (1, 1), (2, 2)]


def layer2_macro_once(seed, detailed=False):
    random.seed(seed)
    side_a, shapes_a = build_army('A', PLAN_A)
    side_b, shapes_b = build_army('B', PLAN_B)
    r = run_multi_unit_battle(side_a, side_b, PAIRINGS, shapes_a, shapes_b, ANCHOR_MAP, max_battle_turns=12)
    out = dict(winner=r['winner'], battle_turns=r['battle_turns'],
               a_surviving=r['a_surviving'], b_surviving=r['b_surviving'],
               a_cas={PLAN_A[i][0]: round(v, 3) for i, v in r['a_casualties'].items()},
               b_cas={PLAN_B[i][0]: round(v, 3) for i, v in r['b_casualties'].items()})
    if detailed:
        out['log'] = r['log']
    return out


def layer2_macro(n=40):
    wins = {'A': 0, 'B': 0, 'draw': 0}
    flanks = pursuits = cascades = 0
    for s in range(n):
        r = layer2_macro_once(1_000_000 + s, detailed=True)
        wins[r['winner']] += 1
        for tl in r['log']:
            flanks += len(tl.get('freed_attacks', []))
            pursuits += len(tl.get('pursuits', []))
            cascades += len(tl.get('cascades', []))
    detailed = layer2_macro_once(1_000_000, detailed=True)   # one replay for the timeline viz
    return dict(scenario='combined-arms double envelopment (cav wings + heavy center) vs levy-flanked line',
                plan_a=[p[0] for p in PLAN_A], plan_b=[p[0] for p in PLAN_B],
                pairings=PAIRINGS, n=n, wins=wins,
                avg_flank_attacks=round(flanks / n, 2), avg_pursuits=round(pursuits / n, 2),
                avg_cascades=round(cascades / n, 2), detailed_run=detailed)


if __name__ == '__main__':
    quick = '--quick' in sys.argv
    print("ENV:", {k: os.environ.get(k) for k in ('PER_CELL', 'LANCHESTER_ENABLED', 'COMMAND_SIGMA_ENABLED', 'PC_BRACE_ENABLED')})

    print("\n[Layer 1] micro — combined-arms unit (3 roles) vs heavy line ...")
    l1 = layer1_micro()
    f0, fl = l1['timeline'][0], l1['timeline'][-1]
    print(f"  ticks={l1['ticks']}  winner={l1['final_winner']}")
    for i, r in enumerate(l1['A_roles']):
        print(f"  A {r:24}  troops {f0['A'][i]['troops']:>7} -> {fl['A'][i]['troops']:>7}  "
              f"cohesion {f0['A'][i]['cohesion']:.2f}->{fl['A'][i]['cohesion']:.2f}  routed={fl['A'][i]['routed']}")
    print(f"  B Heavy line              troops {f0['B'][0]['troops']:>7} -> {fl['B'][0]['troops']:>7}  routed={fl['B'][0]['routed']}")

    n = 8 if quick else 40
    print(f"\n[Layer 2] macro — double envelopment, n={n} ...")
    l2 = layer2_macro(n=n)
    print(f"  wins={l2['wins']}  avg flank-attacks/battle={l2['avg_flank_attacks']}  "
          f"avg pursuits={l2['avg_pursuits']}  avg cascades={l2['avg_cascades']}")

    out = dict(config={k: os.environ.get(k) for k in ('PER_CELL', 'LANCHESTER_ENABLED', 'COMMAND_SIGMA_ENABLED', 'PC_BRACE_ENABLED')},
               layer1_micro=l1, layer2_macro=l2)
    path = os.path.join(HERE, 'macro_micro_telemetry.json')
    with open(path, 'w') as fh:
        json.dump(out, fh, indent=1)
    print(f"\nwrote {path}")
