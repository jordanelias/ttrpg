#!/usr/bin/env python3
"""stress.py -- stress the mass battle module at battle scale, flags on, and measure what goes wrong.

WHAT IT RUNS. Armies of at least `troops_floor` troops a side (stress_scenarios.json), built through the module's
own builders (`build_army`, `build_envelopment`, `build_refused_flank`, and `orderofbattle.build_unit` for the
season's path) and fought with `run_battle` at each tick cap in the file. It calls the module directly, as `bat.py`
does; no season world is involved. Every tunable number is in the JSON; this file holds none.

WHAT IT MEASURES, per battle, from end-of-tick snapshots (`walkthrough._Recorder`: every node's float position,
facing and troops, plus the post-movement contact set):
  overlap   body-box interpenetration by the engine's own `obb_overlap` test, with penetration depth (the metric
            ED-MB-0060 requires; a raw boolean over-counts), split into same subunit / same side other subunit /
            opposing sides.
  idle      subunit-ticks a live, not-holding subunit did not move and was not in contact; and of those, the ones
            where a same-side subunit WAS in contact (an ally watching an ally fight).
  edge      nodes within `edge_margin` of the field boundary, and nodes pinned on it (the clamp in `_node_advance`).
  fit       the deployed extent of each side, and any build error (a cell off the field raises at construction).
  fight     winner, ticks, survivor share, first contact, share of subunits engaged.

FLAGS. `--arm shipped` is every flag at its shipped default (all on but one); `--arm all_on` also turns on the one
flag that ships off (`MB_SUPPORT_RANK_CAP`). The arms are in the JSON. Flags are read at import, so run one arm per
process. `--grid N` sets BATTLEFIELD_SIZE to N before the module loads, and moves the season path's deployment
constants with it, to test whether the 51x51 field is the limit.

    python systems/mass_battle/sim/stress.py --arm shipped --out out_shipped.json
    python systems/mass_battle/sim/stress.py --arm all_on --grid 101 --only S03_cannae_double_envelopment

Reference only, not a source of any value (CLAUDE.md section 0.05).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import multiprocessing
import os
import random
import sys
import time
import traceback

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(_HERE))))   # repo root, as bat.py does
sys.path.insert(0, _HERE)
PARAMS = os.path.join(_HERE, 'stress_scenarios.json')

M = {}   # the module's names, filled by _load() AFTER the arm's flags and the grid size are set


def _load(arm_env: dict, grid) -> None:
    os.environ.update(arm_env)
    import modules.mass_battle.config as cfg
    if grid:
        cfg.BATTLEFIELD_SIZE = grid            # before anything else star-imports it
    from modules.mass_battle import rngsource
    from modules.mass_battle.armies import ENVELOP_WING_GAP, _centered_line_cols, _spec_span
    from modules.mass_battle.config import cell_cap_for
    from modules.mass_battle.geometry import _cellbox_axes, _cellbox_corners, cellbox_from, footprint_for
    from modules.mass_battle.orchestration import run_battle
    from modules.mass_battle.orderofbattle import OrderOfBattle, Subformation, build_unit
    from systems.mass_battle.sim.engine import REFUSE_ECHELON, build_army, build_envelopment, build_refused_flank
    import walkthrough
    M.update(rngsource=rngsource, ENVELOP_WING_GAP=ENVELOP_WING_GAP, _centered_line_cols=_centered_line_cols,
             _spec_span=_spec_span, cell_cap_for=cell_cap_for, _cellbox_axes=_cellbox_axes,
             _cellbox_corners=_cellbox_corners, cellbox_from=cellbox_from, footprint_for=footprint_for,
             run_battle=run_battle, OrderOfBattle=OrderOfBattle, Subformation=Subformation, build_unit=build_unit,
             REFUSE_ECHELON=REFUSE_ECHELON, build_army=build_army, build_envelopment=build_envelopment,
             build_refused_flank=build_refused_flank, Recorder=walkthrough._Recorder, cfg=cfg)
    if grid:
        import modules.mass_battle.orderofbattle as ob
        ob._A_FRONT_ROW = grid // 2 + 2        # the season path's fixed deployment rows, moved with the field
        ob._ANCHOR_COL = grid // 2
        ob._MAX_COL = grid - 2


# ─── layout: front faces aligned, as the prior scenario builder does ─────────────────────────────────────────────

def _layout(P: dict, field: int) -> dict:
    b_front = (field - P['approach_rows']) // 2 - 1
    return {'anchor': field // 2, 'b_front': b_front, 'a_front': b_front + P['approach_rows'] + 1}


def _prep(specs: list) -> list:
    out = []
    for sp in specs:
        s = dict(sp)
        s['troops'] = float(s['troops'])
        s.setdefault('concentration', float(M['cell_cap_for'](s['troop_type'])))
        out.append(s)
    return out


def _depth(sp: dict) -> int:
    if sp.get('width') and sp.get('depth'):
        return int(sp['depth'])
    pat = M['footprint_for'](sp.get('shape', 'Line'), sp['troops'], sp['concentration'], sp['troop_type'])
    rows = [r for r, _c in pat]
    return max(rows) - min(rows) + 1


def _row(side: str, depth: int, ech: int, ex: dict) -> int:
    return ex['a_front'] + ech if side == 'A' else ex['b_front'] - depth + 1 - ech


def _place_line(specs: list, side: str, ex: dict) -> None:
    """Front bodies side by side on the front line; echeloned bodies (archers) as their own centred line behind."""
    front = [s for s in specs if not s.get('echelon')]
    rear = [s for s in specs if s.get('echelon')]
    for group in (front, rear):
        if not group:
            continue
        cols = M['_centered_line_cols'](group, ex['anchor'])
        for sp, col in zip(group, cols):
            sp['starting_position'] = (_row(side, _depth(sp), sp.get('echelon', 0), ex), col)
    for sp in specs:
        sp.pop('echelon', None)


def _build_side(desc: dict, side: str, ex: dict, P: dict):
    ms = P['morale_start']
    name = 'side_' + side.lower()
    kind = desc['kind']
    if kind == 'oob':
        oob = M['OrderOfBattle'](tuple(M['Subformation'](s['name'], s['troop_type'], s['troops'], role=s.get('role'))
                                       for s in desc['subformations']), strategy=desc['strategy'])
        return M['build_unit'](oob, name, side, morale_start=ms)
    if kind == 'army':
        specs = _prep(desc['subunits'])
        _place_line(specs, side, ex)
        return M['build_army'](specs, name, side, morale=ms, morale_start=ms)
    if kind == 'envelopment':
        center, wings = _prep(desc['center']), _prep(desc['wings'])
        _place_line(center, side, ex)
        spans = [M['_spec_span'](s) for s in center]
        c_left = min(s['starting_position'][1] + sp[0] for s, sp in zip(center, spans))
        c_right = max(s['starting_position'][1] + sp[1] for s, sp in zip(center, spans))
        left_x, right_x = c_left - M['ENVELOP_WING_GAP'], c_right + M['ENVELOP_WING_GAP']
        for i, sp in enumerate(wings):
            cmin, cmax = M['_spec_span'](sp)
            if i % 2 == 0:
                col = int(round(left_x - cmax))
                left_x = (col + cmin) - M['ENVELOP_WING_GAP']
            else:
                col = int(round(right_x - cmin))
                right_x = (col + cmax) + M['ENVELOP_WING_GAP']
            sp['starting_position'] = (_row(side, _depth(sp), sp.pop('echelon', 0), ex), col)
        return M['build_envelopment'](center, wings, name, side, morale=ms, morale_start=ms)
    if kind == 'refused':
        strong, refused = _prep(desc['strong']), _prep(desc['refused'])
        cols = M['_centered_line_cols'](strong + refused, ex['anchor'])
        for i, sp in enumerate(strong + refused):
            ech = M['REFUSE_ECHELON'] if i >= len(strong) else 0
            sp.pop('echelon', None)
            sp['starting_position'] = (_row(side, _depth(sp), ech, ex), cols[i])
        return M['build_refused_flank'](strong, refused, name, side, morale=ms, morale_start=ms)
    raise ValueError(f'unknown side kind {kind!r}')


# ─── measurement ─────────────────────────────────────────────────────────────────────────────────────────────────

def _penetration(a, b):
    """Penetration depth of two oriented unit boxes by SAT (the engine's own box and axes), or None if separated."""
    ca, cb = M['_cellbox_corners'](a, False), M['_cellbox_corners'](b, False)
    best = None
    for axis in M['_cellbox_axes'](a) + M['_cellbox_axes'](b):
        pa = [p[0] * axis[0] + p[1] * axis[1] for p in ca]
        pb = [p[0] * axis[0] + p[1] * axis[1] for p in cb]
        ov = min(max(pa), max(pb)) - max(min(pa), min(pb))
        if ov <= 0:
            return None
        best = ov if best is None else min(best, ov)
    return best


def _nodes(det: dict, side: str) -> list:
    dflt = (-1.0, 0.0) if side == 'A' else (1.0, 0.0)
    out = []
    for si, s in enumerate(det[side.lower()]['subs']):
        for n in s['nodes']:
            out.append((side, si, n[0], n[1], tuple(n[3]) if n[3] else dflt, n[2]))
    return out


def _centroid(sub: dict):
    ns = sub['nodes']
    return (sum(n[0] for n in ns) / len(ns), sum(n[1] for n in ns) / len(ns)) if ns else (0.0, 0.0)


def analyse(rec, res: dict, P: dict, field: int) -> dict:
    ticks = sorted(rec.snaps)
    deep, reach = P['deep_depth'], P['pair_reach']
    per_tick, prev_c, idle_run = [], {}, {}
    tot = {'deep_same_sub': 0, 'deep_same_side': 0, 'deep_cross': 0}
    mx = {'same_sub': 0.0, 'same_side': 0.0, 'cross': 0.0}
    idle_st = idle_watch = live_st = 0
    idle_troops = live_troops = 0
    edge_max = pinned_max = 0
    min_edge = float(field)
    engaged_frac, first_contact = [], None
    for t in ticks:
        snap = rec.snaps[t]
        nodes = _nodes(snap, 'A') + _nodes(snap, 'B')
        boxes = [M['cellbox_from'](n[2], n[3], n[4]) for n in nodes]
        cnt = {'deep_same_sub': 0, 'deep_same_side': 0, 'deep_cross': 0}
        for i in range(len(nodes)):
            for j in range(i + 1, len(nodes)):
                if math.hypot(nodes[i][2] - nodes[j][2], nodes[i][3] - nodes[j][3]) >= reach:
                    continue
                d = _penetration(boxes[i], boxes[j])
                if d is None:
                    continue
                if nodes[i][0] != nodes[j][0]:
                    key, mk = 'deep_cross', 'cross'
                elif nodes[i][1] == nodes[j][1]:
                    key, mk = 'deep_same_sub', 'same_sub'
                else:
                    key, mk = 'deep_same_side', 'same_side'
                mx[mk] = max(mx[mk], d)
                if d >= deep:
                    cnt[key] += 1
        for k in cnt:
            tot[k] = max(tot[k], cnt[k])
        # edge
        e = p_ = 0
        for n in nodes:
            dm = min(n[2], n[3], field - 1 - n[2], field - 1 - n[3])
            min_edge = min(min_edge, dm)
            e += dm <= P['edge_margin']
            p_ += dm <= P['move_eps']
        edge_max, pinned_max = max(edge_max, e), max(pinned_max, p_)
        # idle and engagement
        con = rec.contacts.get(t, [])
        eng = {'A': {c[0] for c in con}, 'B': {c[1] for c in con}}
        if con and first_contact is None:
            first_contact = t
        live_n = eng_n = 0
        for side in ('A', 'B'):
            for si, s in enumerate(snap[side.lower()]['subs']):
                key = (side, si)
                c = _centroid(s)
                troops = sum(n[2] for n in s['nodes'])
                moved = key in prev_c and math.hypot(c[0] - prev_c[key][0], c[1] - prev_c[key][1]) > P['move_eps']
                prev_c[key] = c
                if s['routed'] or s['broken']:
                    idle_run[key] = 0
                    continue
                live_n += 1
                eng_n += si in eng[side]
                live_st += 1
                live_troops += troops
                idle = (t > 0 and not moved and si not in eng[side] and s['stance'] != 'hold')
                idle_run[key] = idle_run.get(key, 0) + 1 if idle else 0
                if idle_run[key] >= P['idle_window']:
                    idle_st += 1
                    idle_troops += troops
                    if any(o != si for o in eng[side]):
                        idle_watch += 1
        if live_n:
            engaged_frac.append(eng_n / live_n)
        per_tick.append([t, snap['a']['hp'], snap['b']['hp'], cnt['deep_same_side'], cnt['deep_cross'], len(con)])
    first, last = rec.snaps[ticks[0]], rec.snaps[ticks[-1]]
    ext = {}
    for side in ('A', 'B'):
        ns = _nodes(first, side)
        ext[side] = {'rows': [min(n[2] for n in ns), max(n[2] for n in ns)], 'cols': [min(n[3] for n in ns), max(n[3] for n in ns)],
                     'nodes': len(ns), 'troops': sum(n[5] for n in ns), 'subunits': len(first[side.lower()]['subs'])}
    return {
        'result': {k: res[k] for k in ('winner', 'turns', 'phases', 'a_hp_pct', 'b_hp_pct')},
        'start': ext,
        'peak_deep_pairs': tot,
        'max_depth': {k: round(v, P['round_digits']) for k, v in mx.items()},
        'idle_subunit_ticks': idle_st, 'idle_while_ally_engaged': idle_watch, 'live_subunit_ticks': live_st,
        'idle_troop_share': round(idle_troops / live_troops, P['round_digits']) if live_troops else 0.0,
        'edge_nodes_peak': edge_max, 'pinned_nodes_peak': pinned_max, 'closest_to_edge': round(min_edge, P['round_digits']),
        'first_contact_tick': first_contact,
        'mean_engaged_share': round(sum(engaged_frac) / len(engaged_frac), P['round_digits']) if engaged_frac else 0.0,
        'series': per_tick,
    }


def fight_one(task: tuple) -> dict:
    sid, seed, cap, P, field = task
    sc = next(s for s in P['scenarios'] if s['id'] == sid)
    t0 = time.time()
    out = {'id': sid, 'seed': seed, 'cap': cap}
    try:
        ex = _layout(P, field)
        a = _build_side(sc['a'], 'A', ex, P)
        b = _build_side(sc['b'], 'B', ex, P)
        rec = M['Recorder'](a, b, P['round_digits'])
        sys.setprofile(rec)
        try:
            with M['rngsource'].using(random.Random(seed)):
                res = M['run_battle'](a, b, max_turns=cap)
        finally:
            sys.setprofile(None)
        if rec.t not in rec.snaps:
            rec.close_tick()
        out.update(analyse(rec, res, P, field))
    except Exception as e:                                           # a crash is a result, not a stop
        out['error'] = f'{type(e).__name__}: {e}'
        out['trace'] = traceback.format_exc().splitlines()[-3:]
    out['seconds'] = round(time.time() - t0, P['round_digits'])
    return out


# ─── reporting ───────────────────────────────────────────────────────────────────────────────────────────────────

def summary(rows: list, P: dict) -> str:
    lines = ['scenario                          cap  winners  ticks hpA%/hpB%  deep same-side/cross  idle%  watch%  edge pin  sec']
    keys = sorted({(r['id'], r['cap']) for r in rows})
    for sid, cap in keys:
        rs = [r for r in rows if r['id'] == sid and r['cap'] == cap]
        errs = [r for r in rs if 'error' in r]
        ok = [r for r in rs if 'error' not in r]
        if not ok:
            lines.append(f'{sid:33} {cap:>3}  ERROR {errs[0]["error"][:70]}')
            continue
        w = ''.join(r['result']['winner'][0] for r in ok)
        live = sum(r['live_subunit_ticks'] for r in ok) or 1
        idle = 100 * sum(r['idle_subunit_ticks'] for r in ok) / live
        watch = 100 * sum(r['idle_while_ally_engaged'] for r in ok) / live
        avg = lambda f: sum(f(r) for r in ok) / len(ok)
        lines.append(f"{sid:33} {cap:>3}  {w:7} {avg(lambda r: r['result']['turns']):>5.0f} "
                     f"{avg(lambda r: r['result']['a_hp_pct']):>4.0f}/{avg(lambda r: r['result']['b_hp_pct']):<4.0f}  "
                     f"{max(r['peak_deep_pairs']['deep_same_side'] for r in ok):>5}/{max(r['peak_deep_pairs']['deep_cross'] for r in ok):<5}"
                     f"        {idle:>5.1f}  {watch:>5.1f}  {max(r['edge_nodes_peak'] for r in ok):>4} {max(r['pinned_nodes_peak'] for r in ok):>3}"
                     f"  {avg(lambda r: r['seconds']):>5.0f}" + (f'  [{len(errs)} errors]' if errs else ''))
    return '\n'.join(lines)


def main(argv=None) -> int:
    with open(PARAMS, encoding='utf-8') as f:
        P = json.load(f)
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--arm', default='shipped', choices=sorted(P['arms']))
    ap.add_argument('--grid', type=int, default=None, help='BATTLEFIELD_SIZE for this run (default: the module\'s)')
    ap.add_argument('--only', action='append', help='scenario id; repeatable')
    ap.add_argument('--seeds', type=int, nargs='+')
    ap.add_argument('--cap', type=int, nargs='+', help='tick cap(s), overriding the file')
    ap.add_argument('--procs', type=int, default=os.cpu_count())
    ap.add_argument('--out', metavar='PATH')
    args = ap.parse_args(argv)
    _load(P['arms'][args.arm], args.grid)
    field = M['cfg'].BATTLEFIELD_SIZE
    scs = [s for s in P['scenarios'] if not args.only or s['id'] in args.only]
    tasks = [(s['id'], seed, cap, P, field) for s in scs for cap in (args.cap or P['tick_caps'])
             for seed in (args.seeds or P['seeds'])]
    print(f"arm {args.arm} {P['arms'][args.arm]}  field {field}x{field}  {len(tasks)} battles on {args.procs} procs", flush=True)
    with multiprocessing.get_context('fork').Pool(args.procs) as pool:
        rows = pool.map(fight_one, tasks, chunksize=1)
    floor = P['troops_floor']
    short = [(r['id'], s) for r in rows if 'start' in r for s in ('A', 'B') if r['start'][s]['troops'] < floor]
    print(summary(rows, P))
    print('sides under the troop floor:', sorted(set(short)) or 'none')
    if args.out:
        with open(args.out, 'w', encoding='utf-8') as f:
            json.dump({'arm': args.arm, 'field': field, 'rows': rows}, f)
        print('wrote', args.out)
    return 0


if __name__ == '__main__':
    sys.exit(main())
