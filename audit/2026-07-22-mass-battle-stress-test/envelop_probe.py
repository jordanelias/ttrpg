"""Envelopment diagnostic (Phase 1.5): does an H3 envelop army's wings actually reach the enemy's
flank/rear, and does multi-side shock ever become eligible (>=2 distinct faces on one atom in a tick)?
Monkeypatches resolve_engagements_cascading to compute the FULL-tick face set per defender atom (the
_atom_sides model, replicated) BEFORE the cascade split drops it. Run: python envelop_probe.py [n]"""
import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
_SIM = os.path.abspath(os.path.join(_HERE, '..', '..', 'tests', 'sim'))
sys.path.insert(0, _SIM)
import gauge_mb as g            # noqa: E402
import mass_battle.orchestration as O  # noqa: E402


def _nearest_face(dcells, dfac, acen):
    n = len(dcells)
    cr = sum(r for r, c in dcells) / n; cc = sum(c for r, c in dcells) / n
    fm = (dfac[0] ** 2 + dfac[1] ** 2) ** 0.5 or 1.0
    fu = (dfac[0] / fm, dfac[1] / fm); pu = (-fu[1], fu[0])
    al = [(r - cr) * fu[0] + (c - cc) * fu[1] for r, c in dcells]
    pp = [(r - cr) * pu[0] + (c - cc) * pu[1] for r, c in dcells]
    faces = {'F': (cr + max(al) * fu[0], cc + max(al) * fu[1]),
             'B': (cr + min(al) * fu[0], cc + min(al) * fu[1]),
             'L': (cr + max(pp) * pu[0], cc + max(pp) * pu[1]),
             'R': (cr + min(pp) * pu[0], cc + min(pp) * pu[1])}
    return min(faces, key=lambda k: (faces[k][0] - acen[0]) ** 2 + (faces[k][1] - acen[1]) ** 2)


def _mean_facing(atom):
    fv = getattr(atom, 'cell_facing_vec', None)
    if fv:
        rs = sum(v[0] for v in fv.values()); cs = sum(v[1] for v in fv.values())
        if rs or cs:
            return (rs, cs)
    return (atom.advance_dir, 0)


STATS = {'ticks': 0, 'faces_seen': set(), 'max_sides': 0, 'multiside_ticks': 0, 'nonfront_ticks': 0}
_orig = O.resolve_engagements_cascading


def _patched(unit_a, unit_b, pairs, t=None):
    # full-tick face set per defender atom
    sides = {}
    for p in pairs:
        for datom, atk in ((p["atom_b"], p["a_cells"]), (p["atom_a"], p["b_cells"])):
            dc = list(datom.cells()); ac = list(set(atk))
            if not dc or not ac:
                continue
            acen = (sum(r for r, c in ac) / len(ac), sum(c for r, c in ac) / len(ac))
            f = _nearest_face(dc, _mean_facing(datom), acen)
            sides.setdefault(id(datom), set()).add(f)
    if pairs:
        STATS['ticks'] += 1
        allf = set().union(*sides.values()) if sides else set()
        STATS['faces_seen'] |= allf
        m = max((len(s) for s in sides.values()), default=0)
        STATS['max_sides'] = max(STATS['max_sides'], m)
        if m >= 2:
            STATS['multiside_ticks'] += 1
        if any(s - {'F'} for s in sides.values()):
            STATS['nonfront_ticks'] += 1
    return _orig(unit_a, unit_b, pairs, t=t)


O.resolve_engagements_cascading = _patched
# engine.py re-exports the name; patch there too if bound
try:
    import mass_battle.engine as E
    if hasattr(E, 'resolve_engagements_cascading'):
        E.resolve_engagements_cascading = _patched
except Exception:
    pass

if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 20
    import random
    A = B = draw = 0
    for s in range(n):
        random.seed(1_000_000 + s)
        ua = g._envelop_army('A', 'A'); ub = g.make_unit('Line', 3, 'B', 'B')
        r = g.resolve_battle(ua, ub, 'Line', 'Line', g.ANCHOR_MAP, kind='multi', max_battle_turns=20)
        w = r.get('winner', 'draw'); A += w == 'A'; B += w == 'B'; draw += w not in ('A', 'B')
    print(f"H3 Envelop(A) vs Line(B), n={n}: A(envelop) wins {A}, B(line) wins {B}, draw {draw}")
    print(f"  contact ticks seen: {STATS['ticks']}")
    print(f"  faces the DEFENDER was struck on (ever): {sorted(STATS['faces_seen'])}  [F=front only => NO envelopment]")
    print(f"  max distinct faces on one atom in a tick: {STATS['max_sides']}  [>=2 => multi-side ELIGIBLE]")
    print(f"  ticks with any non-front contact: {STATS['nonfront_ticks']}")
    print(f"  ticks with multi-side eligible (>=2 faces): {STATS['multiside_ticks']}")
