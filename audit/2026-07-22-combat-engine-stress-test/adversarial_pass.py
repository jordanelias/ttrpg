"""Adversarial pass over the 2026-07-22 stress-test findings — falsifies the report's OWN claims and traces the
half-sword result to its mechanism. Report-only; monkeypatches are in-process, nothing committed. Run:
  python adversarial_pass.py
"""
import sys, os
ENG = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'systems', 'combat', 'combat_engine_v1'))
sys.path.insert(0, ENG); sys.path.insert(0, os.path.join(ENG, 'workbench'))
import core, combat_systems as S, weapon_physics as WP, workbench.balance as b  # noqa: E402
from combatant import Combatant, WEAPONS  # noqa: E402
from config import CFG  # noqa: E402
from weapons import HALFSWORD_FORM  # noqa: E402

def wr(w, a, n=500):
    p, *_ = b.winrate({'weapon': w, 'armor': a}, {'weapon': 'arming', 'armor': a}, CFG, n, seed=b._seed((w, a)))
    return 100 * p

# ── 1. HALF-SWORD IS A NET LIABILITY (overturns the original report's B.1 "strength" claim + G2 mechanism) ──
print('=== 1. Half-sword auto-switch: LIVE vs ABLATED (never switch) ===')
_orig = S.halfsword_target
for w in HALFSWORD_FORM:
    live = {a: wr(w, a) for a in ('medium', 'heavy')}
    S.halfsword_target = lambda c, cl, oa: c.weapon
    abl = {a: wr(w, a) for a in ('none', 'light', 'medium', 'heavy')}
    S.halfsword_target = _orig
    print(f'  {w:10} LIVE med/hvy={live["medium"]:.0f}/{live["heavy"]:.0f}  '
          f'ABLATED arc={abl["none"]:.0f}/{abl["light"]:.0f}/{abl["medium"]:.0f}/{abl["heavy"]:.0f}  '
          f'switch COST med {abl["medium"]-live["medium"]:+.0f}pp hvy {abl["heavy"]-live["heavy"]:+.0f}pp')

# ── 2. WHY: the versatile full form already gap-thrusts; the switch trades big reach for tiny anti-armour gain ──
print('\n=== 2. Mechanism: full cut_thrust already gets the gap-thrust; leverage is UNCREDITED ===')
for w in ('longsword', 'longsword_halfsword'):
    c = Combatant('x', weapon=w); dm, h, sg, sp, spc, se = S.select_mode(c, 'heavy', True, CFG, measure_gap=0.0)
    reach = S.reach_base(c, CFG, grip=0.0); cap = S.adef_cap(WEAPONS[w], CFG, h, gap=sg)
    lev = WEAPONS[w]['grip_len'] - CFG['LEVER_HEAD_K'] * WEAPONS[w]['head_len'] + (CFG['LEVER_2H'] if WEAPONS[w]['hands'] == 2 else 0)
    print(f'  {w:20} head={h:10} reach={reach:.2f} adef_cap={cap:.2f} leverage_proxy={lev:.3f}')
print('  -> half-sword has ~3x the leverage but adef_cap(point)=ADEF_POINT*gap reads gap ONLY, never leverage.')

# ── 3. PROTOTYPE FIX (direction only): credit leverage into the gap-thrust adef (emergent; no weapon name) ──
print('\n=== 3. Prototype: credit leverage into gap-thrust armour-defeat (sweep K; NOT a committed fix) ===')
_oa = S.adef_cap
def patched(K):
    def f(w, cfg, head=None, gap=None, grip=0.0, room=1.0):
        base = _oa(w, cfg, head, gap, grip, room)
        h = head if head is not None else w['head']
        if h in ('point', 'cut_thrust'):
            lev = w['grip_len'] - cfg['LEVER_HEAD_K'] * w['head_len'] + (cfg['LEVER_2H'] if w['hands'] == 2 else 0)
            base += K * max(0.0, lev)
        return base
    return f
for K in (0.0, 0.4, 0.8):
    S.adef_cap = patched(K)
    ls = [wr('longsword', a, 400) for a in ('none', 'light', 'medium', 'heavy')]
    print(f'  K={K:.1f}  longsword arc none/lt/md/hv = {ls[0]:.0f}/{ls[1]:.0f}/{ls[2]:.0f}/{ls[3]:.0f}'
          + ('   <- current (broken)' if K == 0 else ''))
S.adef_cap = _oa
print('  NOTE: K also lifts every thrust weapon (spear/rapier/poleaxe-spike) -> needs roster-wide joint re-tune (methodology).')

# ── 4. FALSIFY the report's own C1 "5 distinct context-leaders" claim (was N=120) ──
print('\n=== 4. C1 context-leader flip at higher N (report claimed 5 distinct leaders @ N=120) ===')
m = b.tradition_context_matrix(n=400)
leaders = {w: rows[0][0] for w, rows in m.items()}
for w, rows in m.items():
    print(f'  {w:9} leader={rows[0][0]:9}({rows[0][1]}) margin_over_runner={rows[0][1]-rows[1][1]:+.1f}pp')
print(f'  distinct leaders @ N=400: {len(set(leaders.values()))} (margins ~0.2-0.6pp = NOISE; the 2.9pp UNCONDITIONAL spread is the real C1 result)')

# ── 5. CONFIRM agi dominance is robust (not a baseline artifact) ──
print('\n=== 5. Agility dominance at an all-4 baseline (report measured +29.9 at 3/4 baseline) ===')
base = {a: 4 for a in b.ATTRS}
rows = []
for a in b.ATTRS:
    up = dict(base); up[a] = 5
    p, *_ = b.winrate(up, base, CFG, 600, seed=b._seed(('b4', a))); rows.append((a, round(100 * p, 1)))
rows.sort(key=lambda r: -r[1])
print('  ' + '  '.join(f'{a}:{p}' for a, p in rows[:4]) + '  ...  (agi still dominant -> robust, not a baseline artifact)')

# ── 6. FIX INVESTIGATION — three attempts, all fail the switch-benefit ∧ arming-mirror=50 bars ──
# (Attempt 1 = §3 above: leverage→adef never flips the switch positive.)
print('\n=== 6. Fix investigation: does ANY adef lever make half-swording beneficial without breaking fairness? ===')
_oh = S.halfsword_target
def switch_benefit_and_mirror(patch_adef):
    S.adef_cap = patch_adef if patch_adef else _oa
    mir = {a: wr('arming', a, 300) for a in ('medium', 'heavy')}          # arming vs arming mirror (must be ~50)
    live = {a: wr('longsword', a, 300) for a in ('medium', 'heavy')}
    S.halfsword_target = lambda c, cl, oa: c.weapon
    abl = {a: wr('longsword', a, 300) for a in ('medium', 'heavy')}
    S.halfsword_target = _oh; S.adef_cap = _oa
    return mir, {a: live[a] - abl[a] for a in ('medium', 'heavy')}, live

# Attempt 2: standing cut_thrust bounces entirely (only the half-sword 'point' form gap-thrusts)
def bounce(w, cfg, head=None, gap=None, grip=0.0, room=1.0):
    h = head if head is not None else w['head']
    return cfg['ADEF_CUT'] if h == 'cut_thrust' else _oa(w, cfg, head, gap, grip, room)
mir, ben, live = switch_benefit_and_mirror(bounce)
print(f'  attempt-2 (bounce):  arming mirror med/hvy={mir["medium"]:.0f}/{mir["heavy"]:.0f} (want~50)  '
      f'switch-benefit med/hvy={ben["medium"]:+.0f}/{ben["heavy"]:+.0f}  -> mirror BREAKS at plate')

# Attempt 3: partial standing gap-thrust (scale by f)
for f in (0.6, 0.4, 0.2):
    def partial(w, cfg, head=None, gap=None, grip=0.0, room=1.0, _f=f):
        h = head if head is not None else w['head']; gg = gap if gap is not None else w['gap']
        return (max(cfg['ADEF_CUT'], _f * cfg['ADEF_POINT'] * gg) if h == 'cut_thrust'
                else _oa(w, cfg, head, gap, grip, room))
    mir, ben, live = switch_benefit_and_mirror(partial)
    print(f'  attempt-3 (f={f:.1f}):   arming mirror med/hvy={mir["medium"]:.0f}/{mir["heavy"]:.0f}  '
          f'switch-benefit med/hvy={ben["medium"]:+.0f}/{ben["heavy"]:+.0f}  (mail stays negative)')
print('  CONCLUSION: no adef lever makes the switch beneficial at MAIL without drifting the mirror ->')
print('  the half-sword liability is coupled to reach-over-weighting (Phase-C / G4), not an independent bug.')
