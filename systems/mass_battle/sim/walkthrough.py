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

The page reads every number from the run's data, so `--page` works for any seed or role. Every tunable number is in
the JSON; this file holds none. Reference only, not a source of
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
from modules.mass_battle.massbattle import _grade                              # noqa: E402
from modules.mass_battle.geometry import _oriented                             # noqa: E402
from modules.mass_battle.orchestration import run_battle                       # noqa: E402
from modules.mass_battle.orderofbattle import OrderOfBattle, Subformation, build_unit   # noqa: E402
from modules.mass_battle.resolution import tracing                             # noqa: E402

EXAMPLE = os.path.join(_HERE, 'walkthrough_example.json')
TEMPLATE = os.path.join(_HERE, 'walkthrough_template.html')


def _oob(side: dict, role) -> OrderOfBattle:
    subs = []
    for sf in side['subformations']:
        r = role if (role and sf['troop_type'] == 'light_cavalry') else sf.get('role')
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


def _snap_unit(u, d: int) -> dict:
    """Full state of one side: per subunit, every node's true float position, troops and facing, plus the
    subunit's morale, discipline, stamina, stance and rout flags. Positions are the engine's `cells_float()`
    (the point field), not the integer-binned `cells()`."""
    subs = []
    for s in u.subunits:
        ids = [(o_r, o_c) for o_r, o_c, _a, _b in _oriented(s)]
        nodes = []
        for cid, (r, c) in zip(ids, s.cells_float()):
            f = s.cell_facing_vec.get(cid, getattr(s, '_node_facing', None))
            nodes.append([round(r, d), round(c, d), round(s.cell_troops.get(cid, 0.0)),
                          None if f is None else [round(f[0], d), round(f[1], d)]])
        bf = getattr(s, '_node_facing', None)
        subs.append({'type': s.troop_type, 'routed': bool(s.routed), 'broken': bool(s.broken), 'stance': s.eff_stance,
                     'morale': round(s.eff_morale, d), 'discipline': s.eff_discipline,
                     'stamina': round(s.eff_stamina, d),
                     'body_facing': None if bf is None else [round(bf[0], d), round(bf[1], d)], 'nodes': nodes})
    return {'hp': round(u.hp, d), 'morale': round(u.morale, d), 'routed': bool(u.routed), 'subs': subs}


class _Recorder:
    """Profiles `run_battle`'s direct callees, so what is recorded is what executed, in order. At each tick
    boundary it snapshots both sides, which is the end of the tick before (positions are final after movement,
    damage and the phase boundary). The last `find_contacts` return in a tick is the post-movement contact set."""

    def __init__(self, a, b, d: int):
        self.a, self.b, self.d = a, b, d
        self.code = run_battle.__code__
        self.t = 0
        self.stages, self.contacts, self.snaps = {}, {}, {}
        self.snaps[0] = {'a': _snap_unit(a, d), 'b': _snap_unit(b, d)}

    def close_tick(self):
        if self.t:
            self.snaps[self.t] = {'a': _snap_unit(self.a, self.d), 'b': _snap_unit(self.b, self.d)}

    def __call__(self, frame, event, arg):
        par = frame.f_back
        if par is None or par.f_code is not self.code:
            return
        name = frame.f_code.co_name
        if event == 'call':
            if name == 'trace_event' and frame.f_locals.get('cat') == 'tick':
                self.close_tick()
                self.t = frame.f_locals['kw']['t']
            elif not name.startswith('<'):
                self.stages.setdefault(self.t, []).append(name)
        elif event == 'return' and name == 'find_contacts':
            ia = {id(s): i for i, s in enumerate(self.a.subunits)}
            ib = {id(s): i for i, s in enumerate(self.b.subunits)}
            self.contacts[self.t] = [[ia[id(p['atom_a'])], ib[id(p['atom_b'])], len(p['a_cells']), len(p['b_cells'])]
                                     for p in arg]


def _collapse(names: list) -> list:
    out = []
    for n in names:
        if out and out[-1][0] == n:
            out[-1][1] += 1
        else:
            out.append([n, 1])
    return out


def fight(example: dict, seed: int, role=None) -> dict:
    """One seeded battle. Returns {'result', 'ticks', 'hpmax'}; `ticks` maps tick -> per-side hp, subunit
    centroids and the tick's volley / melee / casualty events, the shape the page's script reads."""
    a = build_unit(_oob(example['side_a'], role), 'side_a', 'A', morale_start=example['morale_start'])
    b = build_unit(_oob(example['side_b'], None), 'side_b', 'B', morale_start=example['morale_start'])
    ticks = {0: {'a': {'hp': a.hp, 'subs': _subs(a), 'routed': False},
                 'b': {'hp': b.hp, 'subs': _subs(b), 'routed': False}, 'ev': []}}
    hpmax = {'a': a.hp_max, 'b': b.hp_max}
    rec = _Recorder(a, b, example['round_digits'])
    sys.setprofile(rec)
    try:
        with rngsource.using(random.Random(seed)):
            with tracing() as events:
                result = run_battle(a, b, max_turns=example['max_turns'])
    finally:
        sys.setprofile(None)
    if rec.t not in rec.snaps:
        rec.close_tick()
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
    for k, v in ticks.items():
        v['detail'] = rec.snaps[k]
        v['contacts'] = rec.contacts.get(k, [])
    stages = {k: _collapse(v) for k, v in rec.stages.items()}
    return {'result': result, 'ticks': ticks, 'hpmax': hpmax, 'stages': stages, 'grade': _grade(a, b, by_troops=True)}


def table(run: dict) -> str:
    rows = ['tick   A hp   B hp  A subunits (row,col troops)                         B subunits']
    short = lambda s: f"{s[0][:5]}({s[1]:.0f},{s[2]:.0f}) {s[4]}{'*' if s[5] else ''}"
    for t in sorted(run['ticks']):
        d = run['ticks'][t]
        rows.append(f"{t:>4} {d['a']['hp']:>6.1f} {d['b']['hp']:>6.1f}  "
                    f"{' '.join(short(s) for s in d['a']['subs']):<52} {' '.join(short(s) for s in d['b']['subs'])}")
    rows.append('* = subunit routed')
    return '\n'.join(rows)


def _summary(example: dict) -> dict:
    """What the page says about the two armies, straight from the example file."""
    def side(d):
        return {'strategy': d['strategy'], 'subformations': [
            {'name': sf['name'], 'type': sf['troop_type'], 'troops': sf['troops'], 'role': sf.get('role')}
            for sf in d['subformations']]}
    return {'a': side(example['side_a']), 'b': side(example['side_b']), 'seed': None,
            'morale_start': example['morale_start'], 'max_turns': example['max_turns']}


def build_page(run: dict, out: str, example: dict, seed: int, role=None) -> None:
    """Write the walkthrough page: the template with this run's data. Every number on the page is read from DATA, so
    the page cannot disagree with the engine it was built from; the sweep over the example's seeds is fought here."""
    with open(TEMPLATE, encoding='utf-8') as f:
        html = f.read()
    sweep = []
    for sd in example['sweep_seeds']:
        r = fight(example, sd, role)
        sweep.append({'seed': sd, 'winner': r['result']['winner'], 'ticks': r['result']['turns'],
                      'a': r['result']['a_hp_pct'], 'b': r['result']['b_hp_pct'], 'degree': r['grade']['degree']})
    armies = _summary(example)
    armies['seed'] = seed
    from modules.mass_battle import config as cfg
    consts = {'volley_scale': cfg.VOLLEY_LETHALITY_SCALE, 'k_square': cfg.K_SQUARE, 'k_linear': cfg.K_LINEAR,
              'ticks_per_phase': cfg.TICKS_PER_PHASE, 'rout_onset': cfg.ROUT_ONSET_FRAC, 'rout_cap': cfg.ROUT_CAP_FRAC,
              'rout_floor': cfg.SUBUNIT_ROUT_FLOOR, 'cascade_frac': cfg.ROUT_CASCADE_FRAC}
    data = {'ticks': {str(k): v for k, v in run['ticks'].items()}, 'hpmax': run['hpmax'], 'grade': run['grade'],
            'result': run['result'], 'sweep': sweep, 'armies': armies, 'consts': consts}
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
    ap.add_argument('--log', metavar='PATH', help='write the full log: per-tick state, contacts, and the call order inside run_battle')
    ap.add_argument('--page', metavar='PATH', help='write the walkthrough page')
    args = ap.parse_args(argv)

    if args.sweep:
        for seed in example['sweep_seeds']:
            r = fight(example, seed, args.role)['result']
            print(f"seed {seed}: winner {r['winner']}, {r['turns']} ticks, "
                  f"A {r['a_hp_pct']}% B {r['b_hp_pct']}% of starting troops")
        return 0

    run = fight(example, args.seed, args.role)
    print(table(run))
    r = run['result']
    print(f"winner {r['winner']} after {r['turns']} ticks; A {r['a_hp_pct']}% B {r['b_hp_pct']}% of starting troops")
    if args.json:
        with open(args.json, 'w', encoding='utf-8') as f:
            json.dump({'ticks': {str(k): v for k, v in run['ticks'].items()}, 'hpmax': run['hpmax']}, f)
        print('wrote', args.json)
    if args.log:
        with open(args.log, 'w', encoding='utf-8') as f:
            json.dump({'stages': {str(k): v for k, v in run['stages'].items()},
                       'ticks': {str(k): v for k, v in run['ticks'].items()}, 'hpmax': run['hpmax']}, f)
        print('wrote', args.log)
    if args.page:
        build_page(run, args.page, example, args.seed, args.role)
        print('wrote', args.page)
    return 0


if __name__ == '__main__':
    sys.exit(main())
