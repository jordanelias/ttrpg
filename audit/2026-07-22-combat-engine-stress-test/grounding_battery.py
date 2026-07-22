"""Combat-engine GROUNDING-validation battery (2026-07-22 stress test).

Falsifiable HEMA / physics / treatise assertions checked against the engine's deterministic physics layer
(select_mode / coupling / core.damage / adef / halfsword). Each cites the authority the repo itself grounds
on: Williams, 'The Knight and the Blast Furnace' (2003); Fiore / Talhoffer / Ringeck Harnischfechten;
Le Jeu de la Hache. Reports MATCH / DIVERGE — a DIVERGE is where emergent play contradicts the historical/
physical source, i.e. the finding the user cares about. Report-only. Run:  python grounding_battery.py
"""
import sys, os
ENG = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'systems', 'combat', 'combat_engine_v1'))
sys.path.insert(0, ENG)
import core, combat_systems as S, weapon_physics as WP  # noqa: E402
from combatant import Combatant, WEAPONS  # noqa: E402
from config import CFG  # noqa: E402

out = []
def check(claim, cite, ok, detail=''): out.append(('MATCH' if ok else 'DIVERGE', claim, cite, detail))
def dmg(head, armor, strg=5, gap=0.5, perc=8.0, heftw=1.0, deg='success'):
    return core.damage(deg, heftw, head, strg, armor, True, gap=gap, perc=perc)
def sel(name, armor, closed=False, gap=None):
    return S.select_mode(Combatant('x', weapon=name), armor, closed, CFG, measure_gap=gap)[1]

# G1: a cut collapses vs plate (Williams: cutting riveted mail impossible; hardened plate sheds the edge)
for w in ['falchion', 'scimitar', 'katana', 'sabre', 'tachi', 'shamshir', 'pulwar']:
    wv = WEAPONS[w]
    dn = dmg(wv['head'], 'none', heftw=WP.heft(wv)); dh = dmg(wv['head'], 'heavy', heftw=WP.heft(wv))
    r = dh / dn if dn else 0
    check(f'{w}: native-cut collapses vs plate', 'Williams KBF: shear vs mail/plate ~impossible',
          r <= 0.30, f'dmg none={dn} heavy={dh} ratio={r:.2f}')

# G2: thrust-to-gap is the armoured kill
cp = core.coupling('point', 'heavy', perc=8.0, gap_prec=0.78); cc = core.coupling('curved_cut', 'heavy')
check('point out-couples cut vs plate', 'Le Jeu de la Hache / Fiore: thrust-to-gap is the armoured kill',
      cp > cc, f'point/heavy={cp:.2f} vs cut/heavy={cc:.2f}')
# G3: percussion transmits through rigid armour
cb = core.coupling('blunt', 'heavy', perc=8.0)
check('blunt(high perc) out-couples cut vs plate', 'Williams KBF: percussion transmits behind plate',
      cb > cc, f'blunt/heavy={cb:.2f} vs cut/heavy={cc:.2f}')
mace = WEAPONS['mace']; sabre = WEAPONS['sabre']
check('mace out-damages sabre vs plate', 'Williams KBF: the war-hammer owns the armoured press',
      dmg('blunt', 'heavy', perc=WP.percussion_authority(mace), heftw=WP.heft(mace)) >
      dmg(sabre['head'], 'heavy', perc=WP.percussion_authority(sabre), heftw=WP.heft(sabre)),
      'mace vs sabre, both in plate')

# G4: half-swording vs harness
for base in ('longsword', 'estoc'):
    c = Combatant('x', weapon=base)
    hh = S.halfsword_target(c, True, 'heavy'); fn = S.halfsword_target(c, False, 'none')
    check(f'{base} half-swords vs plate in close', 'Talhoffer/Ringeck Harnischfechten',
          hh.endswith('_halfsword') and fn == base, f'closed/heavy->{hh}; open/none->{fn}')

# G5: emergent gap-game selection
check('poleaxe affords blunt+point', 'poleaxe = hammer + spike bundle',
      set(S.afforded_heads(WEAPONS['poleaxe'])) == {'blunt', 'point'}, str(sorted(S.afforded_heads(WEAPONS['poleaxe']))))
check('mace affords no point', 'a mace has no thrusting spike', 'point' not in S.afforded_heads(WEAPONS['mace']),
      str(sorted(S.afforded_heads(WEAPONS['mace']))))
check('poleaxe SELECTS spike vs plate', 'Le Jeu de la Hache: the spike is the anti-harness answer',
      sel('poleaxe', 'heavy') == 'point', f"none->{sel('poleaxe','none')}, heavy->{sel('poleaxe','heavy')}  [KNOWN PHASE-C]")
check('katana shifts off pure cut vs plate', 'half-swording to the gaps vs harness',
      sel('katana', 'heavy') != sel('katana', 'none'), f"none->{sel('katana','none')}, heavy->{sel('katana','heavy')}")

# G6: reach advantage decays with armour (FIX-1)
lp = Combatant('L', weapon='glaive')
dm, h, sg, sp, spc, se = S.select_mode(lp, 'heavy', False, CFG); lp.sel_head = h; lp.sel_gap = sg
rn = S.reach_threat(lp, Combatant('d', weapon='arming', armor='none'), CFG)
rh = S.reach_threat(lp, Combatant('d', weapon='arming', armor='heavy'), CFG)
check('reach threat decays vs plate for a cut polearm', 'FIX-1 / differential reach-ladder',
      rh < rn and abs(rn - 1.0) < 1e-9, f'reach_threat none={rn:.2f} heavy={rh:.2f}')

# G7: armour is protective — fixed blow monotone-<= vs heavier armour, every head
ARMORS = ['none', 'light', 'medium', 'heavy']; viol = []
for head in ('blunt', 'point', 'straight_cut', 'curved_cut', 'cut_thrust'):
    seq = [dmg(head, a, gap=0.78, perc=8.0) for a in ARMORS]
    if any(seq[i + 1] > seq[i] + 0.001 for i in range(len(seq) - 1)): viol.append((head, list(zip(ARMORS, seq))))
check('fixed blow: damage monotone-<= vs heavier armour (all heads)', 'armour is protective', not viol, f'violations={viol}')

# G8: degree ordering among the DAMAGING tiers (partial is a non-damage/bind tier by design -> excluded)
seq = [dmg('curved_cut', 'none', deg=d) for d in ('graze', 'success', 'overwhelming')]
check('damage increases graze<success<overwhelming', 'a decisive blow hits harder',
      seq == sorted(seq) and len(set(seq)) == len(seq), f'graze/success/overwhelming={seq}')

# G9: strength scales damage
seq = [dmg('blunt', 'light', strg=s, perc=8.0) for s in (1, 3, 5, 7, 9)]
check('damage monotone-increasing in strength', 'more force = more damage',
      all(seq[i] <= seq[i + 1] for i in range(len(seq) - 1)) and seq[0] < seq[-1], f'str1..9={seq}')

# G10 (probe): cutting-polearm anti-armour affordance asymmetry (the vs-plate CLIFF)
print_cliff = []
for w in ['guandao', 'fauchard', 'glaive', 'podao', 'voulge', 'bardiche', 'sparr_axe', 'naginata']:
    print_cliff.append((w, sorted(S.afforded_heads(WEAPONS[w])), sel(w, 'heavy')))

if __name__ == '__main__':
    print('\n=== GROUNDING VALIDATION (deterministic physics layer) ===\n')
    nd = 0
    for st, cl, ci, de in out:
        if st == 'DIVERGE': nd += 1
        print(f'[{st}] {cl}\n      cite: {ci}\n      data: {de}\n')
    print('--- cutting-polearm anti-armour affordance (the vs-plate cliff driver) ---')
    for w, aff, h in print_cliff:
        print(f'  {w:11} affords {aff}  -> selects {h!r} vs plate')
    print(f'\n=== {len(out)} grounded assertions, {nd} DIVERGE ===')
