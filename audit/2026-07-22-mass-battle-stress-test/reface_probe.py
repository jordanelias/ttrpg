"""Confirm the persistent-defender-reface hypothesis for the envelopment over-decisiveness.
Monkeypatch: each tick, before resolution, a contacted defender subunit's engaged cells slew their
PERSISTENT cell_facing_vec toward the nearest attacker centroid -- IF the threat is not in the rear arc
(variant B) or unconditionally (variant A). Hypothesis: flank reface drops H3 (infantry, flanks) toward
55-72 while leaving C4/C7 (cavalry, REAR -- unrefaceable) near-total.
Run: python reface_probe.py [n]"""
import os, sys, random, math
_HERE = os.path.dirname(os.path.abspath(__file__))
_SIM = os.path.abspath(os.path.join(_HERE, '..', '..', 'tests', 'sim'))
sys.path.insert(0, _SIM)
import gauge_mb as g                       # noqa: E402
import mass_battle.orchestration as O      # noqa: E402
from mass_battle.geometry import _oriented_abs_map  # noqa: E402
from cannae_calib import granular_line     # noqa: E402

_orig = O.resolve_engagements_cascading
REAR_GUARD = [True]   # variant toggle


def _reface(defender, def_cells, atk_cells):
    if not atk_cells or not def_cells:
        return
    ar = sum(c[0] for c in atk_cells) / len(atk_cells)
    ac = sum(c[1] for c in atk_cells) / len(atk_cells)
    amap = _oriented_abs_map(defender)
    for (br, bc) in def_cells:
        oc = amap.get((br, bc))
        if oc is None:
            continue
        cur = defender.get_cell_facing(*oc)
        dr, dc = ar - br, ac - bc
        mag = math.hypot(dr, dc) or 1.0
        want = (dr / mag, dc / mag)
        if REAR_GUARD[0]:
            # angle between CURRENT facing and the threat; if threat is behind (>110deg) can't reface
            cm = math.hypot(*cur) or 1.0
            cosang = (cur[0] * want[0] + cur[1] * want[1]) / cm
            if cosang < math.cos(math.radians(110)):   # threat in rear arc -> cannot turn to face
                continue
        # slew fully (round to cardinal-ish) and PERSIST
        defender.cell_facing_vec[oc] = (round(want[0]), round(want[1]))


def _patched(unit_a, unit_b, pairs, t=None):
    for p in pairs:
        _reface(p["atom_b"], p["b_cells"], p["a_cells"])
        _reface(p["atom_a"], p["a_cells"], p["b_cells"])
    return _orig(unit_a, unit_b, pairs, t=t)


def run(n, ba, bb, label):
    A = B = draw = 0
    for s in range(n):
        random.seed(1_000_000 + s)
        ua = ba('A', 'A'); ub = bb('B', 'B')
        r = g.resolve_battle(ua, ub, 'Line', 'Line', g.ANCHOR_MAP, kind='multi', max_battle_turns=20)
        w = r.get('winner', 'draw'); A += w == 'A'; B += w == 'B'; draw += w not in ('A', 'B')
    dec = A + B; decA = 100.0 * A / dec if dec else 50.0
    print(f"  {label:44} A {A:2} B {B:2} draw {draw:2}   decA={decA:5.1f}%")


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 20
    L6 = lambda nm, fc: granular_line(nm, fc, n_sub=6)
    thin = lambda nm, fc: g._envelop_army(nm, fc)
    cav = lambda nm, fc: g._envelop_army(nm, fc, pin_frac=2/3, wing_troop_type='cavalry', wing_speed='Fast')
    for label, guard in (('NO reface (baseline)', None), ('reface FULL (variant A)', False), ('reface REAR-GUARD (variant B)', True)):
        if guard is None:
            O.resolve_engagements_cascading = _orig
        else:
            REAR_GUARD[0] = guard; O.resolve_engagements_cascading = _patched
        print(f"--- {label} ---")
        run(n, thin, L6, 'H3 thin-envelop(inf) vs 6-line   [band 55-72]')
        run(n, cav, L6, 'C4-like cav-envelop vs 6-line     [band 75-95]')
