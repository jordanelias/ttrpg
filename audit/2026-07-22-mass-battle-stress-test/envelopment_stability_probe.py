"""Envelopment STABILITY probe (ED-MB-0039) — root-causes the H3/H10 side-asymmetry that survived the
matched-granularity fix (ED-MB-0038). Establishes three facts against the 3-command (tripartite) Line:
  (1) pure-infantry envelopment is DEPLOYMENT-CHAOTIC: env wins ~70% as side A, ~17% as side B (same
      armies/seeds) — the parity centre is NARROWER than the 3-command enemy, so the enemy out-flanks the
      centre; the knife-edge race is Lanchester-amplified into a ~54pp side swing. Side-symmetric avg ~44%.
  (2) a deep-narrow centre (width=1,depth=N — BOTH keys needed) STABILISES the swing (51->~7pp) but LOSES
      (too narrow -> bypassed). Depth confers no holding power without frontage in the attrition model.
  (3) COMBINED-ARMS (infantry pin + CAVALRY orbital-wheel rear, ED-MB-0035) is STABLE + side-symmetric
      (swing 0-14pp) + decisive (~93-100%): the cavalry reaches the unrefaceable REAR ("you cannot face the
      rear", Burkholder / C7 rationale). This is the ONLY stable envelopment regime the engine produces.
Conclusion: the 55-72 infantry-envelopment band (H3) sits in a gap the engine can't stably reach with
pure infantry at parity. Fix direction (Jordan directive "envelopment needs cavalry that moves quickly"):
make H3/H4 combined-arms Cannae — which reads ~90% (a band-grounding decision, C4-like), OR add a moderate
infantry-envelopment mechanism (elastic/baiting centre with real depth-holding). Run: python envelopment_stability_probe.py [n]"""
import os, sys, random
_HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, _HERE)
_SIM = os.path.abspath(os.path.join(_HERE, '..', '..', 'tests', 'sim')); sys.path.insert(0, _SIM)
import gauge_mb as g
from mass_battle.engine import build_army, SIDE_A_START_ROW, SIDE_B_START_ROW, Order
CONC = g.GAUGE_CONC; TOT = g.GAUGE_TROOPS; ANCH = g.ANCHOR_MAP.get(('Line', 3), 10)


def deep_env(name, faction, center_frac=1/3, cw=None, cd=None, cav=False, release_tick=4, wing_gap=6):
    if cav:
        return g._envelop_army(name, faction, pin_frac=center_frac, wing_troop_type='cavalry', wing_speed='Fast')
    sr = SIDE_A_START_ROW if faction == 'A' else SIDE_B_START_ROW
    ct = TOT * center_frac; wt = (TOT - ct) / 2
    cs = {'shape': 'Line', 'troop_type': 'infantry', 'troops': ct, 'concentration': CONC, 'starting_position': (sr, ANCH)}
    if cw is not None: cs['width'] = cw
    if cd is not None: cs['depth'] = cd
    wings = [{'shape': 'Line', 'troop_type': 'infantry', 'troops': wt, 'concentration': CONC, 'stance': 'hold', 'starting_position': (sr, ANCH - wing_gap)},
             {'shape': 'Line', 'troop_type': 'infantry', 'troops': wt, 'concentration': CONC, 'stance': 'hold', 'starting_position': (sr, ANCH + wing_gap)}]
    u = build_army([cs] + wings, name, faction, speed='Standard')
    for a in u.subunits[1:]:
        a.orders = (Order(f'tick:{release_tick}', {'stance': 'balanced', 'instructions': tuple(dict.fromkeys(a.instructions + ('envelop',)))}),)
    return u


def ew(builder, side, n):
    e = l = 0
    for s in range(n):
        random.seed(1_000_000 + s)
        if side == 'A': ua = builder('A', 'A'); ub = g._command_army('Line')('B', 'B')
        else: ua = g._command_army('Line')('A', 'A'); ub = builder('B', 'B')
        r = g.resolve_battle(ua, ub, 'Line', 'Line', g.ANCHOR_MAP, kind='multi', max_battle_turns=20)
        w = r.get('winner', 'draw'); e += w == side; l += (w in ('A', 'B') and w != side)
    dec = e + l; return 100.0 * e / dec if dec else 50.0


def row(builder, label, n):
    a = ew(builder, 'A', n); b = ew(builder, 'B', n)
    print(f"  {label:34} env-A {a:5.1f}%  env-B {b:5.1f}%  swing {abs(a - b):5.1f}pp  avg {(a + b) / 2:5.1f}%")


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 40
    print(f"Envelopment stability vs 3-command Line (n={n})  [H3 band 55-72]")
    row(lambda nm, fc: deep_env(nm, fc, center_frac=1/3), '(1) pure-infantry, thin centre', n)
    row(lambda nm, fc: deep_env(nm, fc, center_frac=1/3, cw=1, cd=2), '(2) deep-narrow centre (w1d2)', n)
    row(lambda nm, fc: deep_env(nm, fc, center_frac=1/3, cav=True), '(3) combined-arms (cavalry rear)', n)
