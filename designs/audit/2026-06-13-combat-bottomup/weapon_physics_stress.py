"""
weapon_physics_stress.py -- stress harness for the bottom-up weapon-physics derivations
(percussion_authority.P_auth / puncture_pressure / first_moment) against RANDOM weapons whose every
parameter is bounded by the min/max of the existing 11-weapon roster. Probes the corners the hand-authored
set avoids (incoherent combinations on purpose) for monotonicity, boundedness, continuity (no cliffs),
impact-uniformity (the Lesson-2 lens), and engine-damage sanity (no one-shot; monotone vs armour).

Run: python3 weapon_physics_stress.py   (defaults N=4000). Companion to the 2026-06-13 combat deliverables.
"""
import sys
from math import sqrt, isfinite
sys.path.insert(0, '/home/claude'); sys.path.insert(0, '/home/claude/combat_engine'); sys.path.insert(0, '/home/claude/v32')
import numpy as np
from combatant import WEAPONS, GEOMETRY
import geometry as geo
import core
from config import CFG
import percussion_authority as PA

GEOM_KEYS = ['curvature', 'point_concentration', 'cross_section', 'edge_keenness', 'strike_concentration']
PHYS_KEYS = ['mass', 'pob_frac', 'head_len', 'grip_len']


def weapon_param_bounds():
    """min/max per parameter across the existing roster (the box the random weapons live in)."""
    b = {}
    real = [k for k in WEAPONS if k != 'longsword_halfsword']
    for key in PHYS_KEYS:
        vals = [WEAPONS[w][key] for w in real]
        b[key] = (min(vals), max(vals))
    for key in GEOM_KEYS:
        vals = [GEOMETRY[w][key] for w in real]
        b[key] = (min(vals), max(vals))
    b['_mass_median'] = float(np.median([WEAPONS[w]['mass'] for w in real]))
    return b


def derive_head(g):
    """rough physical head classifier from geometry, so a random weapon has a plausible mode (and exercises
    the head-gated derivations across all modes)."""
    if g['edge_keenness'] >= 0.5 and g['curvature'] >= 0.35:        return 'curved_cut'
    if g['edge_keenness'] >= 0.5 and g['point_concentration'] >= 0.5: return 'cut_thrust'
    if g['edge_keenness'] >= 0.5:                                    return 'straight_cut'
    if g['point_concentration'] >= 0.5:                              return 'point'
    return 'blunt'                                                    # broad/striking head


def random_weapon(b, rng):
    g = {k: float(rng.uniform(*b[k])) for k in GEOM_KEYS}
    w = {k: float(rng.uniform(*b[k])) for k in PHYS_KEYS}
    w['geom'] = g
    w['head'] = derive_head(g)
    w['wt'] = 'heavy' if w['mass'] > b['_mass_median'] else 'light'
    w['gap'] = geo.gap_precision(g['point_concentration'], g['cross_section'])
    return w


def physics(w):
    pa = PA.percussion_authority(w['mass'], w['pob_frac'], w['head'])
    pierce = PA.puncture_pressure(w['mass'], w['pob_frac'], w['geom']['strike_concentration'], w['head'])
    m1 = PA.first_moment(w['mass'], w['pob_frac'], w['grip_len'] + w['head_len'])
    return pa, pierce, m1


def run_stress(N=4000, seed=20260613):
    rng = np.random.default_rng(seed)
    b = weapon_param_bounds()
    W = [random_weapon(b, rng) for _ in range(N)]
    report = {'N': N, 'bounds': {k: b[k] for k in PHYS_KEYS + GEOM_KEYS}}

    # ---- 1. boundedness / finiteness ----
    viol_bounds = []
    for w in W:
        pa, pierce, m1 = physics(w)
        if not (0.0 <= pa <= 8.0 and isfinite(pa)):       viol_bounds.append(('P_auth', pa, w))
        if not (pierce >= 0.0 and isfinite(pierce)):      viol_bounds.append(('pierce', pierce, w))
        if not isfinite(m1):                              viol_bounds.append(('M1', m1, w))
    report['bounds_violations'] = len(viol_bounds)

    # ---- 2. monotonicity: P_auth is a function of s=sqrt(mass)*pob; sort by s, must be non-decreasing ----
    blunt = [w for w in W if w['head'] == 'blunt']
    bs = sorted(blunt, key=lambda w: sqrt(w['mass']) * w['pob_frac'])
    mono_break = 0
    for i in range(1, len(bs)):
        p0 = PA.percussion_authority(bs[i-1]['mass'], bs[i-1]['pob_frac'], 'blunt')
        p1 = PA.percussion_authority(bs[i]['mass'],   bs[i]['pob_frac'],   'blunt')
        if p1 < p0 - 1e-9:
            mono_break += 1
    report['blunt_count'] = len(blunt)
    report['monotonicity_breaks'] = mono_break

    # ---- 3. continuity / cliff: perturb mass & pob by +/-2% of range, max |dP_auth| ----
    dmass = 0.02 * (b['mass'][1] - b['mass'][0]); dpob = 0.02 * (b['pob_frac'][1] - b['pob_frac'][0])
    max_jump = 0.0
    for w in blunt:
        base = PA.percussion_authority(w['mass'], w['pob_frac'], 'blunt')
        for dm, dp in [(dmass, 0), (0, dpob)]:
            mm = min(b['mass'][1], max(b['mass'][0], w['mass'] + dm))
            pp = min(b['pob_frac'][1], max(b['pob_frac'][0], w['pob_frac'] + dp))
            j = abs(PA.percussion_authority(mm, pp, 'blunt') - base)
            max_jump = max(max_jump, j)
    report['max_continuity_jump_per_2pct'] = round(max_jump, 4)   # small => continuous, no cliff

    # ---- 4. impact-uniformity (Lesson-2): dP_auth per +0.05 pob at LOW vs HIGH mass ----
    lo_m, hi_m = b['mass'][0], b['mass'][1]; pmid = 0.5 * (b['pob_frac'][0] + b['pob_frac'][1])
    d_lo = PA.percussion_authority(lo_m, pmid + 0.05, 'blunt') - PA.percussion_authority(lo_m, pmid, 'blunt')
    d_hi = PA.percussion_authority(hi_m, pmid + 0.05, 'blunt') - PA.percussion_authority(hi_m, pmid, 'blunt')
    report['uniformity_dPauth_per_+0.05pob'] = {'low_mass': round(d_lo, 3), 'high_mass': round(d_hi, 3)}

    # ---- 5. engine damage sanity: core.damage with derived P_auth, default defender (End4 => fell at 40hp) ----
    SC, CE = CFG['DAMAGE_SCALE'], CFG['CAP_END']
    FELL = (CE + 6) * (min(CE // 2 + 1, 3) + 1)   # health_full at default End: WI*(MW+1)
    one_shot = arm_nonmono = neg_dmg = 0; max_hit = 0
    for w in blunt:
        pa = PA.percussion_authority(w['mass'], w['pob_frac'], 'blunt')
        prev = None
        for arm in ['none', 'light', 'medium', 'heavy']:
            dovw = core.damage('overwhelming', w['wt'], 'blunt', 4, arm, False, SC, CE, w['gap'], pa)
            for deg in ['partial', 'graze', 'success', 'overwhelming']:
                d = core.damage(deg, w['wt'], 'blunt', 4, arm, False, SC, CE, w['gap'], pa)
                if d < 0: neg_dmg += 1
            max_hit = max(max_hit, dovw)
            if dovw >= FELL: one_shot += 1
            if prev is not None and dovw > prev + 1e-9: arm_nonmono += 1   # more armour should not raise damage
            prev = dovw
    report['damage'] = {'fell_threshold_End4': FELL, 'max_overwhelming_hit': max_hit,
                        'one_shot_kills': one_shot, 'armour_nonmonotone': arm_nonmono, 'negative_damage': neg_dmg}

    # ---- 6. extremes: the corner weapons of the (mass,pob) box + strike_conc corners ----
    corners = []
    for mm in b['mass']:
        for pp in b['pob_frac']:
            pa = PA.percussion_authority(mm, pp, 'blunt')
            for sc in b['strike_concentration']:
                pierce = PA.puncture_pressure(mm, pp, sc, 'blunt')
                corners.append((round(mm,2), round(pp,2), round(sc,2), round(pa,2), round(pierce,2)))
    report['corners_mass_pob_strikeconc__Pauth_pierce'] = corners
    return report


if __name__ == '__main__':
    r = run_stress()
    print(f"== weapon-physics stress: N={r['N']} random weapons, params bounded by the existing roster ==\n")
    print("bounds (min,max):")
    for k, v in r['bounds'].items():
        print(f"  {k:20s} [{v[0]:.3f}, {v[1]:.3f}]")
    print(f"\nblunt subset (P_auth/puncture apply): {r['blunt_count']} of {r['N']}")
    print(f"\n[1] boundedness/finiteness violations : {r['bounds_violations']}   (P_auth in [0,8], pierce>=0, M1 finite)")
    print(f"[2] monotonicity breaks (P_auth vs s)  : {r['monotonicity_breaks']}")
    print(f"[3] max |dP_auth| per 2% param nudge   : {r['max_continuity_jump_per_2pct']}   (small => continuous, no cliff)")
    u = r['uniformity_dPauth_per_+0.05pob']
    print(f"[4] impact-uniformity dP_auth/+0.05pob : low_mass {u['low_mass']}  vs  high_mass {u['high_mass']}   (Lesson-2 spread)")
    d = r['damage']
    print(f"[5] engine damage sanity (fell@End4 = {d['fell_threshold_End4']} hp):")
    print(f"      max overwhelming single hit  : {d['max_overwhelming_hit']}   one-shot kills: {d['one_shot_kills']}")
    print(f"      armour-nonmonotone cells     : {d['armour_nonmonotone']}     negative-damage cells: {d['negative_damage']}")
    print(f"[6] box corners (mass, pob, strike_conc -> P_auth, pierce):")
    for c in r['corners_mass_pob_strikeconc__Pauth_pierce']:
        print(f"      mass {c[0]:>4} pob {c[1]:>4} sc {c[2]:>4} -> P_auth {c[3]:>4} pierce {c[4]:>4}")
