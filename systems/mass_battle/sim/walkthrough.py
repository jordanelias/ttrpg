#!/usr/bin/env python3
"""walkthrough.py -- run the example battle behind the mass battle walkthrough page, and rebuild the page.

WHAT IT RUNS. Two armies built from `walkthrough_example.json` with `orderofbattle.build_unit` and fought with
`orchestration.run_battle` under the engine's per-tick trace. That is the engine path `massbattle.resolve_field`
uses for army records, called directly: no season world is involved, so nothing here says how often a realm fields
these armies. The module is its own system; this file is a harness for it, in the family of `bat.py`.

    python systems/mass_battle/sim/walkthrough.py                  # the page's seed: a tick table and the result
    python systems/mass_battle/sim/walkthrough.py --seed 4         # another draw
    python systems/mass_battle/sim/walkthrough.py --sweep          # winner per seed in the example's sweep list
    python systems/mass_battle/sim/walkthrough.py --role Flanker   # give A's light cavalry a role (Flanker, Feint, ...)
    python systems/mass_battle/sim/walkthrough.py --json out.json  # the per-tick data the page embeds
    python systems/mass_battle/sim/walkthrough.py --page out.html  # rebuild the page from walkthrough_template.html

`--page` is refused for any seed but the example's `page_seed`, because the page's prose and annotations quote
that seed's numbers. Every tunable number is in the JSON; this file holds none. Reference only, not a source of
any value (CLAUDE.md section 0.05).
"""
from __future__ import annotations

import argparse
import json
import os
import random
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(_HERE))))   # repo root, as bat.py does

from modules.mass_battle import rngsource                                      # noqa: E402
from modules.mass_battle.orchestration import run_battle                       # noqa: E402
from modules.mass_battle.orderofbattle import OrderOfBattle, Subformation, build_unit   # noqa: E402
from modules.mass_battle.resolution import tracing                             # noqa: E402

EXAMPLE = os.path.join(_HERE, 'walkthrough_example.json')
TEMPLATE = os.path.join(_HERE, 'walkthrough_template.html')


def _oob(side: dict, role) -> OrderOfBattle:
    subs = []
    for sf in side['subformations']:
        r = role if (role and sf['troop_type'] == 'light_cavalry') else None
        subs.append(Subformation(sf['name'], sf['troop_type'], sf['troops'], role=r))
    return OrderOfBattle(tuple(subs), strategy=side['strategy'])


def _subs(unit) -> list:
    """Deployment centroids before tick 1: [troop_type, row, col, cells, troops, routed]."""
    out = []
    for s in unit.subunits:
        cells = list(s.cells())
        out.append([s.troop_type, sum(c[0] for c in cells) / len(cells), sum(c[1] for c in cells) / len(cells),
                    len(cells), round(s.troop_total()), 0])
    return out


def fight(example: dict, seed: int, role=None) -> dict:
    """One seeded battle. Returns {'result', 'ticks', 'hpmax'}; `ticks` maps tick -> per-side hp, subunit
    centroids and the tick's volley / melee / casualty events, the shape the page's script reads."""
    a = build_unit(_oob(example['side_a'], role), 'side_a', 'A', morale_start=example['morale_start'])
    b = build_unit(_oob(example['side_b'], None), 'side_b', 'B', morale_start=example['morale_start'])
    ticks = {0: {'a': {'hp': a.hp, 'subs': _subs(a), 'routed': False},
                 'b': {'hp': b.hp, 'subs': _subs(b), 'routed': False}, 'ev': []}}
    hpmax = {'a': a.hp_max, 'b': b.hp_max}
    with rngsource.using(random.Random(seed)):
        with tracing() as events:
            result = run_battle(a, b, max_turns=example['max_turns'])
    t = None
    for e in events:
        cat = e['cat']
        if cat == 'tick':
            t = e['t']
            ticks.setdefault(t, {'ev': []})
        elif cat == 'positions':
            d = ticks.setdefault(e['t'], {'ev': []})
            for side in ('a', 'b'):
                u = e[side]
                subs = []
                for s in u['subunits']:
                    cs = s['cells']
                    subs.append([s['troop_type'], round(sum(c['pos'][0] for c in cs) / len(cs), 1),
                                 round(sum(c['pos'][1] for c in cs) / len(cs), 1), len(cs),
                                 round(sum(c['troops'] for c in cs)), 1 if s['routed'] else 0])
                d[side] = {'hp': u['hp'], 'subs': subs, 'routed': u['routed'], 'morale': round(u['morale'], 2)}
        elif cat == 'volley':
            ticks[t]['ev'].append(['v', e['shooter'][-1].upper(), round(e['d'], 1), e['pool'], e['net'],
                                   e['net_dr'], e['dens'], e['loss']])
        elif cat == 'melee':
            ticks[t]['ev'].append(['m', e['a_pool'], e['b_pool'], e['a_net'], e['b_net'], e['a_deg'], e['b_deg']])
        elif cat == 'casualty':
            ticks[t]['ev'].append(['c', e['faction'], e['source'], round(e['delta'], 1)])
    ticks = {k: v for k, v in ticks.items() if 'a' in v}      # the tick the loop exits on has no positions
    return {'result': result, 'ticks': ticks, 'hpmax': hpmax}


def table(run: dict) -> str:
    rows = ['tick   A hp   B hp  A subunits (row,col troops)                         B subunits']
    short = lambda s: f"{s[0][:5]}({s[1]:.0f},{s[2]:.0f}) {s[4]}{'*' if s[5] else ''}"
    for t in sorted(run['ticks']):
        d = run['ticks'][t]
        rows.append(f"{t:>4} {d['a']['hp']:>6.1f} {d['b']['hp']:>6.1f}  "
                    f"{' '.join(short(s) for s in d['a']['subs']):<52} {' '.join(short(s) for s in d['b']['subs'])}")
    rows.append('* = subunit routed')
    return '\n'.join(rows)


def build_page(run: dict, out: str) -> None:
    with open(TEMPLATE, encoding='utf-8') as f:
        html = f.read()
    data = {'ticks': {str(k): v for k, v in run['ticks'].items()}, 'hpmax': run['hpmax']}
    with open(out, 'w', encoding='utf-8') as f:
        f.write(html.replace('/*DATA*/', json.dumps(data)))


def main(argv=None) -> int:
    with open(EXAMPLE, encoding='utf-8') as f:
        example = json.load(f)
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--seed', type=int, default=example['page_seed'])
    ap.add_argument('--role', default=None, help="role for side A's light cavalry, e.g. Flanker or Feint")
    ap.add_argument('--sweep', action='store_true', help='winner for each seed in the example')
    ap.add_argument('--json', metavar='PATH', help='write the per-tick data')
    ap.add_argument('--page', metavar='PATH', help='write the walkthrough page')
    args = ap.parse_args(argv)

    if args.sweep:
        for seed in example['sweep_seeds']:
            r = fight(example, seed, args.role)['result']
            print(f"seed {seed}: winner {r['winner']}, {r['turns']} ticks, "
                  f"A {r['a_hp_pct']}% B {r['b_hp_pct']}% of starting troops")
        return 0

    if args.page and (args.seed != example['page_seed'] or args.role):
        ap.error(f"--page is built for seed {example['page_seed']} with no role: its prose quotes that run")
    run = fight(example, args.seed, args.role)
    print(table(run))
    r = run['result']
    print(f"winner {r['winner']} after {r['turns']} ticks; A {r['a_hp_pct']}% B {r['b_hp_pct']}% of starting troops")
    if args.json:
        with open(args.json, 'w', encoding='utf-8') as f:
            json.dump({'ticks': {str(k): v for k, v in run['ticks'].items()}, 'hpmax': run['hpmax']}, f)
        print('wrote', args.json)
    if args.page:
        build_page(run, args.page)
        print('wrote', args.page)
    return 0


if __name__ == '__main__':
    sys.exit(main())
