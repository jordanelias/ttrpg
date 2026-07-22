"""Phase-C diagnostic probe (2026-07-22). Localizes the three coupled levers behind the reach-class dominance +
half-sword liability, and shows each obvious single knob hits a cross-constraint. Report-only; deep-copies CFG,
commits nothing. Run:  python phasec_probe.py"""
import sys, os, copy
ENG = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'systems', 'combat', 'combat_engine_v1'))
sys.path.insert(0, ENG); sys.path.insert(0, os.path.join(ENG, 'workbench'))
import combat_systems as S, weapon_physics as WP, workbench.balance as b  # noqa: E402
from combatant import WEAPONS  # noqa: E402
from config import CFG  # noqa: E402

def wr(w, a, cfg, n=250):
    p, *_ = b.winrate({'weapon': w, 'armor': a}, {'weapon': 'arming', 'armor': a}, cfg, n, seed=b._seed((w, a)))
    return 100 * p

def acc(cfg, tag):
    reach_h = {w: wr(w, 'heavy', cfg) for w in ('spear', 'yari', 'poleaxe', 'guandao')}
    spn = wr('spear', 'none', cfg)
    _oh = S.halfsword_target
    lh = wr('longsword', 'heavy', cfg)
    S.halfsword_target = lambda c, cl, oa: c.weapon; ah = wr('longsword', 'heavy', cfg); S.halfsword_target = _oh
    print(f'  {tag:34} reach@heavy ' + ' '.join(f'{w}={v:.0f}' for w, v in reach_h.items())
          + f' | spear@none={spn:.0f}(grounded>55) | HS-switch@heavy={lh-ah:+.0f}(want>0) | mirror={wr("arming","heavy",cfg):.0f}')

print('LEVER 1 — reach-class dominance @heavy is the APPROACH stop-hit; but a global cut breaks unarmoured reach:')
acc(CFG, 'baseline')
for sh in (0.5, 0.3):
    c = copy.deepcopy(CFG); c['STOPHIT_CHANCE'] = CFG['STOPHIT_CHANCE'] * sh; acc(c, f'STOPHIT×{sh}')
print('  -> compresses reach@heavy (good) BUT spear@none collapses below 55 (ungrounded) -> needs ARMOUR-CONDITIONAL stop-hit')
print('  HETEROGENEITY (adversarial): full ablation STOPHIT=0 -> spear/yari collapse but poleaxe barely moves:')
c0 = copy.deepcopy(CFG); c0['STOPHIT_CHANCE'] = 0.0
for w in ('spear', 'yari', 'poleaxe'):
    print(f'    {w:8} heavy base={wr(w,"heavy",CFG):.0f} STOPHIT=0->{wr(w,"heavy",c0):.0f}')
print('  -> the "reach class" is NOT monolithic: spear/yari are stop-hit-driven; poleaxe is its own mass/adef (dont lump).\n')

print('LEVER 2 — the half-sword liability is SEPARATE (the stop-hit fix above leaves HS-switch negative):')
print('  the half-sword fights in the CLOSE; its loss is reach-volume there, not the approach stop-hit.\n')

print('LEVER 3 — heft-ordering (spear<arming) is a FORWARD-BALANCE / normalization effect, NOT a missing shaft.')
print('  [CORRECTED by the adversarial pass — the earlier "1.6kg shaft unmodelled" claim was WRONG:]')
sp = WEAPONS['spear']; d = WP.derive(sp)
print(f'  spear IS fully mass-modelled: all_parts={[(round(m,2),round(x,2)) for m,x,_ in WP._all_parts(sp)]} (head+haft+butt=2.0kg)')
for n in ('spear', 'arming', 'longsword', 'greatsword'):
    dd = WP.derive(WEAPONS[n])
    print(f'    {n:11} m_head={dd["m_head"]:.2f} PoB_frac={dd["PoB_frac"]:.3f} heft={WP.heft(WEAPONS[n]):.2f}')
print('  -> spear heft is high because its PoB_frac (0.34) is ~3x the swords\' (~0.12): heft=m_head*PoB_frac, and')
print('     PoB_frac=PoB/(head_len+grip_len) reads the long spear as very forward-balanced. The real fix is the')
print('     PoB_frac normalization / haft-position calibration (a formula question), NOT adding mass. And it is')
print('     DECOUPLED from reach-dominance (mass does not move reach_base, which is geometry).')

if __name__ == '__main__':
    pass
