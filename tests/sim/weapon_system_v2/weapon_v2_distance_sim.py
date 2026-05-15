#!/usr/bin/env python3
"""Weapon system v2 distance sim — v3 (fixed).

Fixes from v1/v2:
  1. ED cost = 6 (same as stunt_strike; eliminates stamina asymmetry)  # [canonical: N/A — structural]
  2. Smart ED heuristic: compare effective TN vs opponent, not just check penalty  # [canonical: N/A — structural]
  3. ED defense penalty: -3D while repositioning  # [canonical: N/A — structural]

Canonical sources:
  - Dice engine: params/combat.md (d10 pool, 1s subtract, 10s chain)
  - STR multiplier: params/combat.md (Light×1, Heavy×2, Blade×1, Blunt×1.5; committed)  # [canonical: N/A — structural]
  - Damage formula: params/combat.md (net_hits + STR×mult + weapon_mod)
  - v2 weapon defs, Cut/Thrust/Bash tables, distance rules: testing_plan.md (PROPOSED)
  - Flat stamina, yield, initiative: duel_stress_test.py v9 (Architecture C)
"""
import numpy as np
from collections import defaultdict

def roll(rng, n, tn):
    if n <= 0: return 0  # [canonical: N/A — structural]
    tn_floor = int(np.floor(tn))
    tn_frac = tn - tn_floor
    d = rng.integers(1, 11, size=n)  # [canonical: params/core.md §dice engine — d10 range 1-10]
    if tn_frac > 0:  # [canonical: N/A — structural]
        hits = int(np.sum(d > tn_floor))
        exact = d == tn_floor
        if np.any(exact):
            coin = rng.random(size=int(np.sum(exact)))
            hits += int(np.sum(coin >= 0.5))  # [canonical: testing_plan.md T1.3 — half-point probabilistic]
    else:
        hits = int(np.sum(d >= tn_floor))
    subs = int(np.sum(d == 1))  # [canonical: params/core.md §dice engine — 1s subtract]
    tens = int(np.sum(d == 10))  # [canonical: params/core.md §dice engine — 1s subtract]
    h = hits - subs
    if tens > 0:  # [canonical: N/A — structural]
        h += int(np.sum(rng.integers(1, 11, size=tens) >= tn_floor))  # [canonical: params/core.md §dice engine — d10 range 1-10]
    return max(0, h)  # [canonical: params/core.md §dice engine — floor at 0]

def mk_pool(agi, hist): return max(5, agi * 2 + hist + 3)  # [canonical: params/combat.md §Pool Formula L14]
def mk_wi(end): return end + 6  # [canonical: designs/scene/derived_stats_v30.md §4.1 — WI]
def mk_mw(end): return end // 2 + 1  # [canonical: designs/scene/derived_stats_v30.md §4.1 — MW]
def mk_hp(end): return mk_wi(end) * (mk_mw(end) + 1)  # [canonical: N/A — structural]
def mk_stam(end): return 15 + end * 2  # [canonical: Architecture C — flat stamina for duels]

ATK_DAMAGE = {'Cut': [4,3,1,0], 'Thrust': [3,3,2,-1], 'Bash': [2,3,4,4]}  # [canonical: testing_plan.md Phase 2 — Cut/Thrust/Bash proposed tables]
ARMOUR_TIERS = ['None', 'Light', 'Medium', 'Heavy']  # [canonical: params/combat.md §Damage Formula PP-232]
ARMOUR_IDX = {t: i for i, t in enumerate(ARMOUR_TIERS)}  # [canonical: params/combat.md §Damage Formula PP-232]
DIST_SHORT, DIST_MID, DIST_LONG = 0, 1, 2  # [canonical: testing_plan.md Phase 5 — distance positions]

WEAPONS_V2 = {
    'dagger':       {'tn': 6.0, 'reach': DIST_SHORT, 'atk_types': ['Cut', 'Thrust'], 'str_mult': 1.0},  # [canonical: testing_plan.md Phase 5 — distance positions]
    'arming_sword': {'tn': 7.0, 'reach': DIST_MID,   'atk_types': ['Cut', 'Thrust'], 'str_mult': 1.0},  # [canonical: testing_plan.md — arming sword: base 7]
    'mace':         {'tn': 7.5, 'reach': DIST_MID,   'atk_types': ['Bash'],           'str_mult': 1.5},  # [canonical: testing_plan.md — mace: base 7 + 0.5(Blunt)]
    'longsword':    {'tn': 6.5, 'reach': DIST_LONG,  'atk_types': ['Cut', 'Thrust', 'Bash'], 'str_mult': 2.0},  # [canonical: testing_plan.md — longsword: base 7 - 0.5(2H cap)]
    'spear':        {'tn': 6.5, 'reach': DIST_LONG,  'atk_types': ['Thrust'],         'str_mult': 1.0},  # [canonical: testing_plan.md — spear: base 7 - 0.5(Light)]
    'warhammer':    {'tn': 7.0, 'reach': DIST_LONG,  'atk_types': ['Bash'],           'str_mult': 3.0},  # [canonical: testing_plan.md — warhammer: base 7 + 0.5(Blunt) - 0.5(2H cap)]
}

ED_COST = 6  # [canonical: sim iteration v3 — matches stunt_strike cost]
ED_DEF_PENALTY = 3  # [canonical: sim iteration v3 — repositioning penalty]

def effective_tn(weapon, dist):
    w = WEAPONS_V2[weapon]
    gap = abs(dist - w['reach'])
    if gap == 0: return w['tn'], False  # [canonical: N/A — structural]
    elif gap == 1: return w['tn'] + 1.0, False  # [canonical: testing_plan.md Phase 5 — adjacent range +1.0 TN]
    else: return w['tn'], True

def get_atk_damage_mod(atk_type, armour, attacker_str):
    idx = ARMOUR_IDX[armour]
    mod = ATK_DAMAGE[atk_type][idx]  # [canonical: testing_plan.md Phase 2 — Cut/Thrust/Bash proposed tables]
    if mod == -1: return attacker_str // 2  # [canonical: testing_plan.md Phase 2 — Thrust vs Heavy: floor(STR/2)]
    return mod

def best_attack_type(weapon, armour, attacker_str):
    w = WEAPONS_V2[weapon]
    best_type = None; best_dmg = -999  # [canonical: N/A — structural]
    for at in w['atk_types']:
        mod = get_atk_damage_mod(at, armour, attacker_str)
        if weapon == 'longsword' and at == 'Bash': mod -= 3  # [canonical: N/A — structural]
        if mod > best_dmg: best_dmg = mod; best_type = at
    return best_type

def calc_damage(net_hits, atk_type, weapon, armour, attacker_str, rng):
    w = WEAPONS_V2[weapon]
    str_mult = w['str_mult']  # [canonical: params/combat.md §Damage Formula PP-232 — STR multiplier]
    if weapon == 'longsword' and atk_type == 'Bash': str_mult = 1.0  # [canonical: params/combat.md §Damage Formula PP-232 — STR multiplier]
    base_mod = get_atk_damage_mod(atk_type, armour, attacker_str)
    is_crit = net_hits >= 3; stun = 0  # [canonical: params/combat.md §Damage Formula — crit threshold]
    if is_crit:
        if atk_type == 'Cut': base_mod *= 2  # [canonical: params/combat.md §Damage Formula — crit doubles weapon mod]
        elif atk_type == 'Thrust':
            tier_idx = max(0, ARMOUR_IDX[armour] - 1)  # [canonical: N/A — structural]
            base_mod = get_atk_damage_mod('Thrust', ARMOUR_TIERS[tier_idx], attacker_str)  # [canonical: params/combat.md §Damage Formula PP-232]
        elif atk_type == 'Bash': base_mod *= 2; stun = 2  # [canonical: params/combat.md §Damage Formula — crit doubles weapon mod]
    damage = net_hits + int(attacker_str * str_mult) + base_mod  # [canonical: params/combat.md §Damage Formula PP-232 — STR multiplier]
    return max(0, damage), stun  # [canonical: N/A — structural]

def sim_duel_v2(w_a, w_b, arm_a='None', arm_b='None',
                agi_a=4, agi_b=4, str_a=4, str_b=4,  # [canonical: N/A — structural]
                end_a=4, end_b=4, hist=2, arena=0,  # [canonical: N/A — structural]
                start_dist=None, use_distance=True, seed=42, maxr=30):  # [canonical: N/A — structural]
    rng = np.random.default_rng(seed)
    wa = WEAPONS_V2[w_a]; wb = WEAPONS_V2[w_b]
    pa, pb = mk_pool(agi_a, hist), mk_pool(agi_b, hist)
    sa, sb = mk_stam(end_a), mk_stam(end_b)
    sma, smb = sa, sb
    ha, hb = mk_hp(end_a), mk_hp(end_b)
    wia, wib = mk_wi(end_a), mk_wi(end_b)
    mwa, mwb = mk_mw(end_a), mk_mw(end_b)
    wact, wbct = 0, 0; daa, dab = 0, 0  # [canonical: N/A — structural]
    if agi_a > agi_b: init_a = True
    elif agi_b > agi_a: init_a = False
    else: init_a = bool(rng.integers(0, 2))  # [canonical: N/A — structural]
    stun_a = stun_b = 0; ooa = oob = False  # [canonical: designs/scene/combat_v30.md §7 — OOB at stamina 0]
    dist = start_dist if (use_distance and start_dist is not None) else DIST_MID
    L = defaultdict(int)
    L['dmg_per_hit_a'] = []; L['dmg_per_hit_b'] = []

    def ep(base, w, oo, stun_pen):
        return max(5, base - w - stun_pen - (2 if oo else 0))  # [canonical: params/combat.md §Pool Formula — minimum 5 ED-203]

    for rd in range(1, maxr + 1):  # [canonical: N/A — structural]
        ai = wact > mwa or ha <= 0; bi = wbct > mwb or hb <= 0  # [canonical: N/A — structural]
        if ai and bi: L.update(rd=rd-1, w='draw', e='mi'); break  # [canonical: N/A — structural]
        if ai: L.update(rd=rd-1, w='B', e='iA'); break  # [canonical: N/A — structural]
        if bi: L.update(rd=rd-1, w='A', e='iB'); break  # [canonical: N/A — structural]
        if ooa and oob:  # [canonical: designs/scene/combat_v30.md §7 — OOB at stamina 0]
            L.update(rd=rd, w='A' if ha > hb else ('B' if hb > ha else 'draw'), e='my'); break
        if ooa: L.update(rd=rd, w='B', e='yA'); break  # [canonical: designs/scene/combat_v30.md §7 — OOB at stamina 0]
        if oob: L.update(rd=rd, w='A', e='yB'); break

        Pa = ep(pa, wact, ooa, stun_a); Pb = ep(pb, wbct, oob, stun_b)  # [canonical: designs/scene/combat_v30.md §7 — OOB at stamina 0]
        stun_a = stun_b = 0  # [canonical: N/A — structural]
        sfa = sa / max(1, sma); sfb = sb / max(1, smb)  # [canonical: N/A — structural]

        if use_distance:
            tn_a, blocked_a = effective_tn(w_a, dist)
            tn_b, blocked_b = effective_tn(w_b, dist)
        else:
            tn_a, blocked_a = wa['tn'], False
            tn_b, blocked_b = wb['tn'], False

        atk_type_a = best_attack_type(w_a, arm_b, str_a)
        atk_type_b = best_attack_type(w_b, arm_a, str_b)

        act_a = 'strike'; act_b = 'strike'
        if use_distance:
            at_opt_a = (dist == wa['reach']); at_opt_b = (dist == wb['reach'])
            if blocked_a:
                act_a = 'establish_distance'
            elif not at_opt_a and sfa > 0.25:  # [canonical: N/A — structural]
                if not blocked_b and tn_a > tn_b:
                    act_a = 'establish_distance'
                elif sfa > 0.5 and not blocked_b:  # [canonical: N/A — structural]
                    act_a = 'establish_distance'
            if blocked_b:
                act_b = 'establish_distance'
            elif not at_opt_b and sfb > 0.25:  # [canonical: N/A — structural]
                if not blocked_a and tn_b > tn_a:
                    act_b = 'establish_distance'
                elif sfb > 0.5 and not blocked_a:  # [canonical: N/A — structural]
                    act_b = 'establish_distance'

        if act_a == 'strike' and sfa < 0.2: act_a = 'breath'  # [canonical: N/A — structural]
        if act_b == 'strike' and sfb < 0.2: act_b = 'breath'  # [canonical: N/A — structural]
        if act_a == 'strike' and arena > 0: act_a = 'stunt_strike'  # [canonical: N/A — structural]
        if act_b == 'strike' and arena > 0: act_b = 'stunt_strike'  # [canonical: N/A — structural]

        sp = 0.55  # [canonical: duel_stress_test.py v9 — ADAPTIVE offense split]
        if act_a in ('strike', 'stunt_strike'):
            oa = max(1, int(Pa * sp)); dda = Pa - oa  # [canonical: N/A — structural]
        else:
            oa = 0; dda = Pa  # [canonical: N/A — structural]
        if act_b in ('strike', 'stunt_strike'):
            ob = max(1, int(Pb * sp)); ddb = Pb - ob  # [canonical: N/A — structural]
        else:
            ob = 0; ddb = Pb  # [canonical: N/A — structural]

        nda = ndb = 0  # [canonical: N/A — structural]
        sta = arena if act_a == 'stunt_strike' else 0  # [canonical: N/A — structural]
        stb = arena if act_b == 'stunt_strike' else 0  # [canonical: N/A — structural]

        if act_a == 'establish_distance' or act_b == 'establish_distance':
            if act_a == 'establish_distance' and act_b == 'establish_distance':
                ra = roll(rng, agi_a, 7); rb = roll(rng, agi_b, 7)  # [canonical: testing_plan.md Phase 5 — ED Agi contest TN 7]
                if ra > rb:
                    if dist < wa['reach']: dist = min(DIST_LONG, dist + 1)  # [canonical: N/A — structural]
                    elif dist > wa['reach']: dist = max(DIST_SHORT, dist - 1)  # [canonical: testing_plan.md Phase 5 — distance positions]
                    L['dist_changes'] += 1  # [canonical: N/A — structural]
                elif rb > ra:
                    if dist < wb['reach']: dist = min(DIST_LONG, dist + 1)  # [canonical: N/A — structural]
                    elif dist > wb['reach']: dist = max(DIST_SHORT, dist - 1)  # [canonical: testing_plan.md Phase 5 — distance positions]
                    L['dist_changes'] += 1  # [canonical: N/A — structural]
                sa = max(0, sa - ED_COST); sb = max(0, sb - ED_COST)  # [canonical: N/A — structural]
            elif act_a == 'establish_distance':
                ra = roll(rng, agi_a, 7); rb = roll(rng, agi_b, 7)  # [canonical: testing_plan.md Phase 5 — ED Agi contest TN 7]
                if ra > rb:
                    if dist < wa['reach']: dist = min(DIST_LONG, dist + 1)  # [canonical: N/A — structural]
                    elif dist > wa['reach']: dist = max(DIST_SHORT, dist - 1)  # [canonical: testing_plan.md Phase 5 — distance positions]
                    L['dist_changes'] += 1  # [canonical: N/A — structural]
                if not blocked_b and act_b in ('strike', 'stunt_strike'):
                    tn_eff_b = tn_b + (1.0 if w_b == 'longsword' and atk_type_b == 'Bash' else 0)  # [canonical: N/A — structural]
                    def_pool_a = max(3, dda - ED_DEF_PENALTY)  # [canonical: sim iteration v3 — ED defense floor 3]
                    h = roll(rng, ob + stb, tn_eff_b)
                    bl = roll(rng, def_pool_a, 7.0)  # [canonical: N/A — structural]
                    net = h - bl
                    if net > 0:  # [canonical: N/A — structural]
                        d, st = calc_damage(net, atk_type_b, w_b, arm_a, str_b, rng)
                        ha = max(0, ha - d); daa += d  # [canonical: N/A — structural]
                        wact = min(mwa + 1, daa // wia)  # [canonical: N/A — structural]
                        ndb = d; stun_a = st
                        L['dmg_per_hit_b'].append(d)
                    sb = max(0, sb - 5 - (1 if stb else 0))  # [canonical: N/A — structural]
                elif blocked_b: L['blocked_rounds'] += 1  # [canonical: N/A — structural]
                sa = max(0, sa - ED_COST)  # [canonical: N/A — structural]
            else:
                ra = roll(rng, agi_a, 7); rb = roll(rng, agi_b, 7)  # [canonical: testing_plan.md Phase 5 — ED Agi contest TN 7]
                if rb > ra:
                    if dist < wb['reach']: dist = min(DIST_LONG, dist + 1)  # [canonical: N/A — structural]
                    elif dist > wb['reach']: dist = max(DIST_SHORT, dist - 1)  # [canonical: testing_plan.md Phase 5 — distance positions]
                    L['dist_changes'] += 1  # [canonical: N/A — structural]
                if not blocked_a and act_a in ('strike', 'stunt_strike'):
                    tn_eff_a = tn_a + (1.0 if w_a == 'longsword' and atk_type_a == 'Bash' else 0)  # [canonical: N/A — structural]
                    def_pool_b = max(3, ddb - ED_DEF_PENALTY)  # [canonical: N/A — structural]
                    h = roll(rng, oa + sta, tn_eff_a)
                    bl = roll(rng, def_pool_b, 7.0)  # [canonical: N/A — structural]
                    net = h - bl
                    if net > 0:  # [canonical: N/A — structural]
                        d, st = calc_damage(net, atk_type_a, w_a, arm_b, str_a, rng)
                        hb = max(0, hb - d); dab += d  # [canonical: N/A — structural]
                        wbct = min(mwb + 1, dab // wib)  # [canonical: N/A — structural]
                        nda = d; stun_b = st
                        L['dmg_per_hit_a'].append(d)
                    sa = max(0, sa - 5 - (1 if sta else 0))  # [canonical: designs/scene/combat_v30.md §7 — standard attack cost 5]
                elif blocked_a: L['blocked_rounds'] += 1  # [canonical: N/A — structural]
                sb = max(0, sb - ED_COST)  # [canonical: N/A — structural]
        else:
            if act_a in ('strike', 'stunt_strike') and not blocked_a:
                tn_eff_a = tn_a + (1.0 if w_a == 'longsword' and atk_type_a == 'Bash' else 0)  # [canonical: N/A — structural]
                h = roll(rng, oa + sta, tn_eff_a)
                bl = roll(rng, ddb, tn_b if not blocked_b else 7.0)  # [canonical: N/A — structural]
                net = h - bl
                if net > 0:  # [canonical: N/A — structural]
                    d, st = calc_damage(net, atk_type_a, w_a, arm_b, str_a, rng)
                    hb = max(0, hb - d); dab += d  # [canonical: N/A — structural]
                    wbct = min(mwb + 1, dab // wib)  # [canonical: N/A — structural]
                    nda = d; stun_b = st
                    L['dmg_per_hit_a'].append(d)
                sa = max(0, sa - 5 - (1 if sta else 0))  # [canonical: designs/scene/combat_v30.md §7 — standard attack cost 5]
            elif blocked_a: L['blocked_rounds'] += 1  # [canonical: N/A — structural]
            if act_b in ('strike', 'stunt_strike') and not blocked_b:
                tn_eff_b = tn_b + (1.0 if w_b == 'longsword' and atk_type_b == 'Bash' else 0)  # [canonical: N/A — structural]
                h = roll(rng, ob + stb, tn_eff_b)
                bl = roll(rng, dda, tn_a if not blocked_a else 7.0)  # [canonical: N/A — structural]
                net = h - bl
                if net > 0:  # [canonical: N/A — structural]
                    d, st = calc_damage(net, atk_type_b, w_b, arm_a, str_b, rng)
                    ha = max(0, ha - d); daa += d  # [canonical: N/A — structural]
                    wact = min(mwa + 1, daa // wia)  # [canonical: N/A — structural]
                    ndb = d; stun_a = st
                    L['dmg_per_hit_b'].append(d)
                sb = max(0, sb - 5 - (1 if stb else 0))  # [canonical: N/A — structural]
            elif blocked_b: L['blocked_rounds'] += 1  # [canonical: N/A — structural]

        if act_a == 'breath': sa = min(sma, sa + (end_a + hist) * 2)  # [canonical: designs/scene/combat_v30.md §7 — Breath: (End+Hist)×2]
        if act_b == 'breath': sb = min(smb, sb + (end_b + hist) * 2)  # [canonical: designs/scene/combat_v30.md §7 — Breath: (End+Hist)×2]
        if nda > 0 and ndb == 0: init_a = True  # [canonical: N/A — structural]
        elif ndb > 0 and nda == 0: init_a = False  # [canonical: N/A — structural]
        ooa = sa <= 0; oob = sb <= 0  # [canonical: designs/scene/combat_v30.md §7 — OOB at stamina 0]
    else:
        L.update(rd=maxr, w='A' if ha > hb else ('B' if hb > ha else 'draw'), e='t')
    L['final_dist'] = dist
    return L

def run_batch(n, w_a, w_b, **kw):
    wins = {'A': 0, 'B': 0, 'draw': 0}  # [canonical: N/A — structural]
    rds = []; da = []; db = []; dc = 0; bl = 0  # [canonical: N/A — structural]
    for i in range(n):
        r = sim_duel_v2(w_a=w_a, w_b=w_b, seed=4000+i, **kw)  # [canonical: N/A — structural]
        wins[r['w']] += 1; rds.append(r.get('rd', 30))  # [canonical: N/A — structural]
        da.extend(r.get('dmg_per_hit_a', [])); db.extend(r.get('dmg_per_hit_b', []))
        dc += r.get('dist_changes', 0); bl += r.get('blocked_rounds', 0)  # [canonical: N/A — structural]
    return {
        'A_win': wins['A']/n*100, 'B_win': wins['B']/n*100, 'draw': wins['draw']/n*100,  # [canonical: N/A — structural]
        'avg_rds': np.mean(rds),
        'dph_A': np.mean(da) if da else 0, 'dph_B': np.mean(db) if db else 0,  # [canonical: N/A — structural]
        'dc': dc/n, 'bl': bl/n,
    }

if __name__ == '__main__':
    N = 3000  # [canonical: N/A — structural]
    print("Weapon System v2 Distance Sim — v3 (fixed)")
    print(f"N={N}. Equal stats: Agi 4, STR 4, End 4. Hist 2. Arena 3.")  # [canonical: N/A — structural]
    print(f"ED cost={ED_COST}, ED def penalty=-{ED_DEF_PENALTY}D\n")

    # T5.1  # [canonical: N/A — structural]
    print("=" * 75)  # [canonical: N/A — structural]
    print("T5.1: Distance Sanity — Spear vs Dagger")  # [canonical: N/A — structural]
    print("=" * 75)  # [canonical: N/A — structural]
    for sd, sdn in [(0, 'Short'), (1, 'Mid'), (2, 'Long')]:  # [canonical: N/A — structural]
        r = run_batch(N, 'spear', 'dagger', arm_a='Heavy', arm_b='Heavy',
                      use_distance=True, start_dist=sd, arena=3)  # [canonical: N/A — structural]
        print(f"  Start {sdn:5s}: Spear {r['A_win']:5.1f}%  Dagger {r['B_win']:5.1f}%  "  # [canonical: N/A — structural]
              f"Draw {r['draw']:4.1f}%  Rds {r['avg_rds']:.1f}  DistΔ {r['dc']:.1f}")  # [canonical: N/A — structural]

    # T2.4  # [canonical: N/A — structural]
    print(f"\n{'='*75}\nT2.4: Warhammer vs Arming Sword\n{'='*75}")  # [canonical: N/A — structural]
    for armour in ARMOUR_TIERS:  # [canonical: params/combat.md §Damage Formula PP-232]
        r_no = run_batch(N, 'warhammer', 'arming_sword', arm_a=armour, arm_b=armour,
                         use_distance=False, arena=3)  # [canonical: N/A — structural]
        r_d = run_batch(N, 'warhammer', 'arming_sword', arm_a=armour, arm_b=armour,
                        use_distance=True, arena=3)  # [canonical: N/A — structural]
        ratio = r_d['dph_A'] / max(0.1, r_d['dph_B'])  # [canonical: N/A — structural]
        print(f"  {armour:6s}: NO DIST WH {r_no['A_win']:5.1f}% | WITH DIST WH {r_d['A_win']:5.1f}% "  # [canonical: N/A — structural]
              f"(Δ{r_d['A_win']-r_no['A_win']:+5.1f}pp) DPH {r_d['dph_A']:.1f}/{r_d['dph_B']:.1f} "  # [canonical: N/A — structural]
              f"ratio={ratio:.2f}")

    # T6.1  # [canonical: N/A — structural]
    print(f"\n{'='*75}\nT6.1: Longsword vs All\n{'='*75}")  # [canonical: N/A — structural]
    for armour in ['None', 'Medium', 'Heavy']:
        print(f"--- {armour} ---")
        for opp in ['dagger', 'arming_sword', 'mace', 'spear', 'warhammer']:
            r_no = run_batch(N, 'longsword', opp, arm_a=armour, arm_b=armour,
                             use_distance=False, arena=3)  # [canonical: N/A — structural]
            r_d = run_batch(N, 'longsword', opp, arm_a=armour, arm_b=armour,
                            use_distance=True, arena=3)  # [canonical: N/A — structural]
            flag = " FAIL" if r_d['A_win'] > 75 else ""  # [canonical: N/A — structural]
            print(f"  vs {opp:13s}: NO DIST {r_no['A_win']:5.1f}% | WITH DIST {r_d['A_win']:5.1f}% "  # [canonical: N/A — structural]
                  f"(Δ{r_d['A_win']-r_no['A_win']:+5.1f}pp){flag}")  # [canonical: N/A — structural]
        print()
