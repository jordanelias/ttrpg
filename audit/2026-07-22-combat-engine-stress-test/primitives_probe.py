"""Adversarial probe of the L0 primitive-law + emergence (2026-07-22).

The engine's claim: weapon behaviour EMERGES from physical geometry primitives {curvature, point_concentration,
cross_section, edge_keenness, strike_concentration} via geometry.bake -> {gap, thrust, cut, perc_conc, halfsword},
with NO weapon-name tables. This probe hammers that claim three ways:

  A. DEAD-COEFFICIENT: geo['halfsword'] (can_halfsword_thrust) is computed by bake() for every weapon and read by
     NOTHING at runtime — an orphan derived coefficient.
  B. NAME-TABLE-vs-EMERGENCE: half-sword CAPABILITY is a hardcoded 2-name fiat list (HALFSWORD_FORM), not emergent.
     (The dead primitive that WOULD make it emergent is also mis-specified — no length/2H term — so it can't just
      be wired in as-is; the honest fix needs a length/hands-gated rule + authored forms.)
  C. DEAD-PRIMITIVE ABLATION: zero / max each RAW primitive roster-wide, re-bake geo, and measure whether a basket
     of win-rates actually moves (the methodology's own ablation gate: a lever that moves nothing is dead).

Report-only; re-bakes in-process, restores. Run:  python primitives_probe.py
"""
import sys, os, copy
ENG = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'systems', 'combat', 'combat_engine_v1'))
sys.path.insert(0, ENG); sys.path.insert(0, os.path.join(ENG, 'workbench'))
import geometry as G, workbench.balance as b  # noqa: E402
from combatant import WEAPONS  # noqa: E402
from weapons import HALFSWORD_FORM  # noqa: E402
from config import CFG  # noqa: E402
PRIMS = ['curvature', 'point_concentration', 'cross_section', 'edge_keenness', 'strike_concentration']

def wr(w, a, n=120):
    p, *_ = b.winrate({'weapon': w, 'armor': a}, {'weapon': 'arming', 'armor': a}, CFG, n, seed=b._seed((w, a)))
    return 100 * p

# ── A + B: half-sword is dead-primitive + name-table ────────────────────────────────────────────────
print('=== A. geo["halfsword"] (can_halfsword_thrust) is a DEAD derived coefficient (computed by bake, read by nothing) ===')
print('=== B. half-sword CAPABILITY is a 2-name FIAT list, not emergent ===')
print(f'  HALFSWORD_FORM (fiat): {list(HALFSWORD_FORM.keys())}')
emergent = [n for n, w in WEAPONS.items() if 'base' not in w and w.get('geometry')
            and n not in HALFSWORD_FORM
            and G.can_halfsword_thrust(w['geometry']['curvature'], w['geometry']['point_concentration'])]
print(f'  primitive can_halfsword_thrust ALSO flags {len(emergent)} more weapons (but the gate is TOO BROAD — no length/2H term,')
print(f'    so it wrongly includes daggers/spears). Long 2H straight blades it SHOULD add but the fiat list denies:')
LONG2H = [n for n in emergent if WEAPONS[n]['hands'] == 2 and WEAPONS[n]['head_len'] >= 0.7
          and WEAPONS[n]['head'] in ('cut_thrust', 'straight_cut', 'curved_cut')]
print(f'    {LONG2H}')

# ── C: dead-primitive ablation (re-bake each raw primitive roster-wide, measure basket movement) ──────
print('\n=== C. DEAD-PRIMITIVE ABLATION — zero & max each raw primitive roster-wide, re-bake, measure |dwin%| ===')
BASKET = [('rapier', 'none'), ('rapier', 'heavy'), ('sabre', 'none'), ('sabre', 'heavy'),
          ('mace', 'heavy'), ('rondel', 'heavy'), ('katana', 'heavy'), ('stiletto', 'heavy')]
def snapshot():
    return {n: (copy.deepcopy(w['geometry']), copy.deepcopy(w['geo'])) for n, w in WEAPONS.items() if 'geometry' in w}
def restore(snap):
    for n, (geom, geo) in snap.items():
        WEAPONS[n]['geometry'] = geom; WEAPONS[n]['geo'] = geo
def set_prim_all(P, val):
    for n, w in WEAPONS.items():
        if 'geometry' in w and P in w['geometry']:
            w['geometry'][P] = val; w['geo'] = G.bake(w['geometry'])
def basket_vec():
    return {c: wr(*c) for c in BASKET}

snap = snapshot()
base = basket_vec()
print('  baseline basket: ' + ' '.join(f'{w[:4]}/{a[0]}={v:.0f}' for (w, a), v in base.items()))
results = []
for P in PRIMS:
    maxshift = 0.0; detail = ''
    for val in (0.0, 1.0):
        set_prim_all(P, val)
        vec = basket_vec()
        restore(snap)
        shift = max(abs(vec[c] - base[c]) for c in BASKET)
        if shift > maxshift:
            maxshift = shift
            worst = max(BASKET, key=lambda c: abs(vec[c] - base[c]))
            detail = f'@{val:.0f}: {worst[0]}/{worst[1]} {base[worst]:.0f}->{vec[worst]:.0f}'
    verdict = 'DEAD/inert' if maxshift < 3 else ('weak' if maxshift < 10 else 'LIVE')
    results.append((P, maxshift, verdict, detail))
for P, ms, v, d in sorted(results, key=lambda r: r[1]):
    print(f'  {P:22} max|d|={ms:4.0f}pp  [{v}]  {d}')
print('  (a primitive whose zero AND max barely move the basket fails the methodology ablation gate)')
restore(snap)
