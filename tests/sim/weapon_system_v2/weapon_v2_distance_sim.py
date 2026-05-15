#!/usr/bin/env python3
"""Weapon system v2 sim — distance mechanics + Cut/Thrust/Bash damage.

Tests T2.4 (warhammer dominance) and T6.1 (longsword dominance) with distance.  # [canonical: N/A — sim internal]
Extends duel v9 chassis (Architecture C).
"""
import numpy as np
from collections import defaultdict

# === DICE ENGINE ===
# [canonical: params/combat.md — d10 pool TN system, 1s subtract, 10s chain]
def roll(rng, n, tn):
    if n <= 0: return 0  # [canonical: N/A — sim internal]
    tn_floor = int(np.floor(tn))
    tn_frac = tn - tn_floor
    d = rng.integers(1, 11, size=n)  # [canonical: params/core.md §dice engine — d10]
    if tn_frac > 0:  # [canonical: N/A — sim internal]
        # Half-point TN: >= ceil(TN) always hits; exact floor(TN) has 50% hit  # [canonical: N/A — sim internal]
        hits = int(np.sum(d > tn_floor))
        exact = d == tn_floor
        if np.any(exact):
            coin = rng.random(size=int(np.sum(exact)))
            hits += int(np.sum(coin >= 0.5))  # [canonical: testing_plan.md §T1.3 — 50% at floor(TN)]
    else:
        hits = int(np.sum(d >= tn_floor))
    subs = int(np.sum(d == 1))  # [canonical: params/core.md §dice engine — 1s subtract]
    tens = int(np.sum(d == 10))  # [canonical: params/core.md §dice engine — 10s chain]
    h = hits - subs
    if tens > 0:  # [canonical: N/A — sim internal]
        h += int(np.sum(rng.integers(1, 11, size=tens) >= tn_floor))  # [canonical: params/core.md §dice engine — d10]
    return max(0, h)  # [canonical: N/A — sim internal]

# === DERIVED STATS ===
def mk_pool(agi, hist): return max(5, agi * 2 + hist + 3)  # [canonical: params/combat.md §Pool Formula]
def mk_wi(end): return end + 6  # [canonical: designs/scene/derived_stats_v30.md §4.1 — wound interval]
def mk_mw(end): return end // 2 + 1  # [canonical: designs/scene/derived_stats_v30.md §4.1 — max wounds]
def mk_hp(end): return mk_wi(end) * (mk_mw(end) + 1)  # [canonical: designs/scene/derived_stats_v30.md §4.1 — health]
def mk_stam(end): return 15 + end * 2  # [canonical: duel_design_and_stress_results.md — C flat stamina]

# === WEAPON SYSTEM V2 ===
ATK_DAMAGE = {
    'Cut':    [4, 3, 1, 0],  # [canonical: testing_plan.md §Phase 2 — Cut +4/+3/+1/+0]
    'Thrust': [3, 3, 2, -1],  # -1 = sentinel for floor(STR/2)  # [canonical: testing_plan.md §Phase 2 — Thrust +3/+3/+2/floor(STR/2)]
    'Bash':   [2, 3, 4, 4],  # [canonical: testing_plan.md §Phase 2 — Bash +2/+3/+4/+4]
}
ARMOUR_TIERS = ['None', 'Light', 'Medium', 'Heavy']
ARMOUR_IDX = {t: i for i, t in enumerate(ARMOUR_TIERS)}

DIST_SHORT, DIST_MID, DIST_LONG = 0, 1, 2  # [canonical: testing_plan.md §Phase 5 — Short/Mid/Long]
DIST_NAMES = ['Short', 'Mid', 'Long']

WEAPONS_V2 = {
    'dagger':       {'tn': 6.0, 'reach': DIST_SHORT, 'atk_types': ['Cut', 'Thrust'],  # [canonical: testing_plan.md — TN 7-0.5(Light)-0.5(Short)=6.0]
                     'str_mult': 1.0, 'is_2h': False},  # [canonical: params/combat.md §STR mult]
    'arming_sword': {'tn': 7.0, 'reach': DIST_MID,   'atk_types': ['Cut', 'Thrust'],  # [canonical: testing_plan.md — TN 7+0+0=7.0]
                     'str_mult': 1.0, 'is_2h': False},  # [canonical: params/combat.md §STR mult]
    'mace':         {'tn': 7.5, 'reach': DIST_MID,   'atk_types': ['Bash'],  # [canonical: testing_plan.md — TN 7+0.5(Blunt)=7.5]
                     'str_mult': 1.5, 'is_2h': False},  # [canonical: params/combat.md §STR mult — Blunt×1.5]
    'longsword':    {'tn': 6.5, 'reach': DIST_LONG,  'atk_types': ['Cut', 'Thrust', 'Bash'],  # [canonical: testing_plan.md — TN 7-0.5(2H cap)=6.5]
                     'str_mult': 2.0, 'is_2h': True},  # [canonical: params/combat.md §STR mult — Heavy×2]
    'spear':        {'tn': 6.5, 'reach': DIST_LONG,  'atk_types': ['Thrust'],  # [canonical: testing_plan.md — TN 7-0.5(Light)-0.5(Long 2H)=6.0; FIXME shows 6.5]
                     'str_mult': 1.0, 'is_2h': False},  # [canonical: params/combat.md §STR mult]
    'warhammer':    {'tn': 7.0, 'reach': DIST_LONG,  'atk_types': ['Bash'],  # [canonical: testing_plan.md — TN 7+0.5(Blunt)-0.5(2H cap)=7.0]
                     'str_mult': 3.0, 'is_2h': True},  # [canonical: params/combat.md §STR mult — Heavy×2×Blunt×1.5=×3]
}

def effective_tn(weapon, current_dist):
    w = WEAPONS_V2[weapon]
    gap = abs(current_dist - w['reach'])
    if gap == 0: return w['tn'], False  # [canonical: N/A — sim internal]
    elif gap == 1: return w['tn'] + 1.0, False  # [canonical: N/A — sim internal]
    else: return w['tn'], True  # BLOCKED

def get_atk_damage_mod(atk_type, armour, attacker_str):
    idx = ARMOUR_IDX[armour]
    mod = ATK_DAMAGE[atk_type][idx]
    if mod == -1: return attacker_str // 2  # [canonical: testing_plan.md §Phase 2 — floor(STR/2) vs Heavy]
    return mod

def best_attack_type(weapon, armour, attacker_str):
    w = WEAPONS_V2[weapon]
    best_type = None
    best_dmg = -999  # [canonical: N/A — sim internal]
    for at in w['atk_types']:
        mod = get_atk_damage_mod(at, armour, attacker_str)
        if weapon == 'longsword' and at == 'Bash':
            mod -= 3  # mordhau penalty approximation for selection  # [canonical: testing_plan.md §T3.1 — mordhau TN +1.0 penalty]
        if mod > best_dmg:
            best_dmg = mod
            best_type = at
    return best_type

def calc_damage(net_hits, atk_type, weapon, armour, attacker_str, rng):
    w = WEAPONS_V2[weapon]
    str_mult = w['str_mult']  # [canonical: N/A — sim internal]
    if weapon == 'longsword' and atk_type == 'Bash':
        str_mult = 1.0  # mordhau  # [canonical: params/combat.md §STR mult]

    base_mod = get_atk_damage_mod(atk_type, armour, attacker_str)
    is_crit = net_hits >= 3  # [canonical: params/combat.md §Damage — crit at net >= 3]
    stun = 0  # [canonical: N/A — sim internal]

    if is_crit:
        if atk_type == 'Cut':
            base_mod *= 2  # [canonical: testing_plan.md §Phase 8 — crit mod ×2]
        elif atk_type == 'Thrust':
            tier_idx = max(0, ARMOUR_IDX[armour] - 1)  # [canonical: testing_plan.md §Phase 8 — Thrust crit armour down]
            base_mod = get_atk_damage_mod('Thrust', ARMOUR_TIERS[tier_idx], attacker_str)
        elif atk_type == 'Bash':
            base_mod *= 2  # [canonical: testing_plan.md §Phase 8 — crit mod ×2]
            stun = 2  # [canonical: testing_plan.md §Phase 8 — Bash crit stun -2D]

    damage = net_hits + int(attacker_str * str_mult) + base_mod  # [canonical: params/combat.md §Damage Formula]
    return max(0, damage), stun  # [canonical: N/A — sim internal]


def sim_duel_v2(w_a='arming_sword', w_b='arming_sword',
                arm_a='None', arm_b='None',
                agi_a=4, agi_b=4, str_a=4, str_b=4,  # [canonical: N/A — sim internal]
                end_a=4, end_b=4, cog_a=4, cog_b=4,  # [canonical: N/A — sim internal]
                comp_a=5, comp_b=5, hist=2,  # [canonical: N/A — test Composure default]
                prot_a='ADAPTIVE', prot_b='ADAPTIVE',
                arena=0, start_dist=None,  # [canonical: N/A — sim internal]
                use_distance=True,
                seed=42, maxr=30):  # [canonical: N/A — sim internal]
    rng = np.random.default_rng(seed)
    wa = WEAPONS_V2[w_a]; wb = WEAPONS_V2[w_b]
    pa, pb = mk_pool(agi_a, hist), mk_pool(agi_b, hist)
    sa, sb = mk_stam(end_a), mk_stam(end_b)
    sma, smb = sa, sb
    ha, hb = mk_hp(end_a), mk_hp(end_b)
    wia, wib = mk_wi(end_a), mk_wi(end_b)
    mwa, mwb = mk_mw(end_a), mk_mw(end_b)
    wact, wbct = 0, 0  # [canonical: N/A — sim internal]
    daa, dab = 0, 0  # [canonical: N/A — sim internal]
    if agi_a > agi_b: init_a = True
    elif agi_b > agi_a: init_a = False
    else: init_a = bool(rng.integers(0, 2))  # [canonical: params/combat.md §PP-239 — tiebreak]
    stun_a = stun_b = 0  # [canonical: N/A — sim internal]
    ooa = oob = False
    dist = start_dist if (use_distance and start_dist is not None) else DIST_MID

    L = defaultdict(int)
    L['dist_changes'] = 0  # [canonical: N/A — sim internal]
    L['blocked_rounds'] = 0  # [canonical: N/A — sim internal]
    L['dmg_per_hit_a'] = []
    L['dmg_per_hit_b'] = []

    def ep(base, w, oo, stun_pen):
        p = base - w - stun_pen
        if oo: p -= 2  # [canonical: designs/scene/combat_v30.md §1 — OOB -2D]
        return max(5, p)  # [canonical: params/combat.md §Pool Formula — minimum 5]

    for rd in range(1, maxr + 1):  # [canonical: N/A — sim internal]
        ai = wact > mwa or ha <= 0  # [canonical: designs/scene/derived_stats_v30.md §4.1 — incapacitation]
        bi = wbct > mwb or hb <= 0  # [canonical: N/A — sim internal]
        if ai and bi: L.update(rd=rd-1, w='draw', e='mi'); break  # [canonical: N/A — sim internal]
        if ai: L.update(rd=rd-1, w='B', e='iA'); break  # [canonical: N/A — sim internal]
        if bi: L.update(rd=rd-1, w='A', e='iB'); break  # [canonical: N/A — sim internal]
        if ooa and oob:
            L.update(rd=rd, w='A' if ha > hb else ('B' if hb > ha else 'draw'), e='my'); break
        if ooa: L.update(rd=rd, w='B', e='yA'); break
        if oob: L.update(rd=rd, w='A', e='yB'); break

        Pa = ep(pa, wact, ooa, stun_a)
        Pb = ep(pb, wbct, oob, stun_b)
        stun_a = stun_b = 0  # [canonical: N/A — sim internal]
        sfa = sa / max(1, sma)  # [canonical: N/A — sim internal]
        sfb = sb / max(1, smb)  # [canonical: N/A — sim internal]

        if use_distance:
            tn_a, blocked_a = effective_tn(w_a, dist)
            tn_b, blocked_b = effective_tn(w_b, dist)
        else:
            tn_a, blocked_a = wa['tn'], False
            tn_b, blocked_b = wb['tn'], False

        atk_type_a = best_attack_type(w_a, arm_b, str_a)
        atk_type_b = best_attack_type(w_b, arm_a, str_b)

        # Action selection
        act_a = 'strike'; act_b = 'strike'
        if use_distance:
            if blocked_a:
                act_a = 'establish_distance'
            elif tn_a > wa['tn'] and sfa > 0.3:  # [canonical: N/A — sim protocol stamina threshold]
                # At non-optimal range; try to establish if opponent has advantage here
                opp_penalty = tn_b - wb['tn']
                if opp_penalty < 0.5:  # [canonical: N/A — sim protocol decision threshold]
                    act_a = 'establish_distance'
            if blocked_b:
                act_b = 'establish_distance'
            elif tn_b > wb['tn'] and sfb > 0.3:  # [canonical: N/A — sim protocol stamina threshold]
                opp_penalty = tn_a - wa['tn']
                if opp_penalty < 0.5:  # [canonical: N/A — sim protocol decision threshold]
                    act_b = 'establish_distance'

        if act_a == 'strike' and sfa < 0.2: act_a = 'breath'  # [canonical: N/A — sim protocol breath threshold]
        if act_b == 'strike' and sfb < 0.2: act_b = 'breath'  # [canonical: N/A — sim protocol breath threshold]

        if act_a == 'strike' and arena > 0: act_a = 'stunt_strike'  # [canonical: N/A — sim internal]
        if act_b == 'strike' and arena > 0: act_b = 'stunt_strike'  # [canonical: N/A — sim internal]

        sp_a = 0.55; sp_b = 0.55  # [canonical: N/A — sim protocol default split]

        # Pool splits
        if act_a in ('strike', 'stunt_strike'):
            oa = max(1, int(Pa * sp_a)); dda = Pa - oa  # [canonical: N/A — sim internal]
        else:
            oa = 0; dda = Pa  # [canonical: N/A — sim internal]
        if act_b in ('strike', 'stunt_strike'):
            ob = max(1, int(Pb * sp_b)); ddb = Pb - ob  # [canonical: N/A — sim internal]
        else:
            ob = 0; ddb = Pb  # [canonical: N/A — sim internal]

        nda = ndb = 0  # [canonical: N/A — sim internal]
        sta = arena if act_a == 'stunt_strike' else 0  # [canonical: N/A — sim internal]
        stb = arena if act_b == 'stunt_strike' else 0  # [canonical: N/A — sim internal]

        # === ESTABLISH DISTANCE ===
        if act_a == 'establish_distance' or act_b == 'establish_distance':
            if act_a == 'establish_distance' and act_b == 'establish_distance':
                ra = roll(rng, agi_a, 7); rb = roll(rng, agi_b, 7)  # [canonical: designs/scene/combat_v30.md §3 — ED contested Agi TN 7]
                if ra > rb:
                    if dist < wa['reach']: dist = min(DIST_LONG, dist + 1)  # [canonical: N/A — sim internal]
                    elif dist > wa['reach']: dist = max(DIST_SHORT, dist - 1)  # [canonical: N/A — sim internal]
                    L['dist_changes'] += 1  # [canonical: N/A — sim internal]
                elif rb > ra:
                    if dist < wb['reach']: dist = min(DIST_LONG, dist + 1)  # [canonical: N/A — sim internal]
                    elif dist > wb['reach']: dist = max(DIST_SHORT, dist - 1)  # [canonical: N/A — sim internal]
                    L['dist_changes'] += 1  # [canonical: N/A — sim internal]
                sa = max(0, sa - 3); sb = max(0, sb - 3)  # [canonical: designs/scene/combat_v30.md §7 — ED cost 3]
            elif act_a == 'establish_distance':
                ra = roll(rng, agi_a, 7); rb = roll(rng, agi_b, 7)  # [canonical: designs/scene/combat_v30.md §3 — ED contested Agi TN 7]
                if ra > rb:
                    if dist < wa['reach']: dist = min(DIST_LONG, dist + 1)  # [canonical: N/A — sim internal]
                    elif dist > wa['reach']: dist = max(DIST_SHORT, dist - 1)  # [canonical: N/A — sim internal]
                    L['dist_changes'] += 1  # [canonical: N/A — sim internal]
                if not blocked_b and act_b in ('strike', 'stunt_strike'):
                    tn_eff_b = tn_b + (1.0 if w_b == 'longsword' and atk_type_b == 'Bash' else 0)  # [canonical: N/A — sim internal]
                    h = roll(rng, ob + stb, tn_eff_b)
                    bl = roll(rng, dda, 7.0)  # moving defender uses TN 7  # [canonical: N/A — sim internal]
                    net = h - bl
                    if net > 0:  # [canonical: N/A — sim internal]
                        d, st = calc_damage(net, atk_type_b, w_b, arm_a, str_b, rng)
                        ha = max(0, ha - d); daa += d  # [canonical: N/A — sim internal]
                        wact = min(mwa + 1, daa // wia)  # [canonical: designs/scene/derived_stats_v30.md §4.1 — wound tracking]
                        ndb = d; stun_a = st
                        L['dmg_per_hit_b'].append(d)
                    sb = max(0, sb - 5 - (1 if stb else 0))  # [canonical: designs/scene/combat_v30.md §7 — action cost 5]
                elif blocked_b: L['blocked_rounds'] += 1  # [canonical: N/A — sim internal]
                sa = max(0, sa - 3)  # [canonical: designs/scene/combat_v30.md §7 — ED cost 3]
            else:
                ra = roll(rng, agi_a, 7); rb = roll(rng, agi_b, 7)  # [canonical: designs/scene/combat_v30.md §3 — ED contested Agi TN 7]
                if rb > ra:
                    if dist < wb['reach']: dist = min(DIST_LONG, dist + 1)  # [canonical: N/A — sim internal]
                    elif dist > wb['reach']: dist = max(DIST_SHORT, dist - 1)  # [canonical: N/A — sim internal]
                    L['dist_changes'] += 1  # [canonical: N/A — sim internal]
                if not blocked_a and act_a in ('strike', 'stunt_strike'):
                    tn_eff_a = tn_a + (1.0 if w_a == 'longsword' and atk_type_a == 'Bash' else 0)  # [canonical: N/A — sim internal]
                    h = roll(rng, oa + sta, tn_eff_a)
                    bl = roll(rng, ddb, 7.0)  # [canonical: N/A — sim internal]
                    net = h - bl
                    if net > 0:  # [canonical: N/A — sim internal]
                        d, st = calc_damage(net, atk_type_a, w_a, arm_b, str_a, rng)
                        hb = max(0, hb - d); dab += d  # [canonical: N/A — sim internal]
                        wbct = min(mwb + 1, dab // wib)  # [canonical: N/A — sim internal]
                        nda = d; stun_b = st
                        L['dmg_per_hit_a'].append(d)
                    sa = max(0, sa - 5 - (1 if sta else 0))  # [canonical: designs/scene/combat_v30.md §7 — action cost 5]
                elif blocked_a: L['blocked_rounds'] += 1  # [canonical: N/A — sim internal]
                sb = max(0, sb - 3)  # [canonical: designs/scene/combat_v30.md §7 — ED cost 3]
        else:
            # Both striking/breathing
            if act_a in ('strike', 'stunt_strike') and not blocked_a:
                tn_eff_a = tn_a + (1.0 if w_a == 'longsword' and atk_type_a == 'Bash' else 0)  # [canonical: N/A — sim internal]
                h = roll(rng, oa + sta, tn_eff_a)
                bl = roll(rng, ddb, tn_b if not blocked_b else 7.0)  # [canonical: N/A — sim internal]
                net = h - bl
                if net > 0:  # [canonical: N/A — sim internal]
                    d, st = calc_damage(net, atk_type_a, w_a, arm_b, str_a, rng)
                    hb = max(0, hb - d); dab += d  # [canonical: N/A — sim internal]
                    wbct = min(mwb + 1, dab // wib)  # [canonical: N/A — sim internal]
                    nda = d; stun_b = st
                    L['dmg_per_hit_a'].append(d)
                sa = max(0, sa - 5 - (1 if sta else 0))  # [canonical: designs/scene/combat_v30.md §7 — action cost 5]
            elif blocked_a and act_a in ('strike', 'stunt_strike'):
                L['blocked_rounds'] += 1  # [canonical: N/A — sim internal]
            if act_b in ('strike', 'stunt_strike') and not blocked_b:
                tn_eff_b = tn_b + (1.0 if w_b == 'longsword' and atk_type_b == 'Bash' else 0)  # [canonical: N/A — sim internal]
                h = roll(rng, ob + stb, tn_eff_b)
                bl = roll(rng, dda, tn_a if not blocked_a else 7.0)  # [canonical: N/A — sim internal]
                net = h - bl
                if net > 0:  # [canonical: N/A — sim internal]
                    d, st = calc_damage(net, atk_type_b, w_b, arm_a, str_b, rng)
                    ha = max(0, ha - d); daa += d  # [canonical: N/A — sim internal]
                    wact = min(mwa + 1, daa // wia)  # [canonical: designs/scene/derived_stats_v30.md §4.1 — wound tracking]
                    ndb = d; stun_a = st
                    L['dmg_per_hit_b'].append(d)
                sb = max(0, sb - 5 - (1 if stb else 0))  # [canonical: designs/scene/combat_v30.md §7 — action cost 5]
            elif blocked_b and act_b in ('strike', 'stunt_strike'):
                L['blocked_rounds'] += 1  # [canonical: N/A — sim internal]

        if act_a == 'breath': sa = min(sma, sa + (end_a + hist) * 2)  # [canonical: designs/scene/combat_v30.md §7 — breath recovery (End+Hist)×2]
        if act_b == 'breath': sb = min(smb, sb + (end_b + hist) * 2)  # [canonical: designs/scene/combat_v30.md §7 — breath recovery (End+Hist)×2]

        if nda > 0 and ndb == 0: init_a = True  # [canonical: N/A — sim internal]
        elif ndb > 0 and nda == 0: init_a = False  # [canonical: N/A — sim internal]
        ooa = sa <= 0; oob = sb <= 0  # [canonical: designs/scene/combat_v30.md §7 — OOB at 0 stamina]
    else:
        L.update(rd=maxr, w='A' if ha > hb else ('B' if hb > ha else 'draw'), e='t')

    L['final_dist'] = dist
    return L


def run_batch(n, w_a, w_b, arm_a='None', arm_b='None',
              use_distance=True, start_dist=None, arena=3,  # [canonical: N/A — sim internal]
              agi_a=4, agi_b=4, str_a=4, str_b=4, **kw):  # [canonical: N/A — sim internal]
    wins = {'A': 0, 'B': 0, 'draw': 0}  # [canonical: N/A — sim internal]
    rounds_list = []
    dmg_a_all = []; dmg_b_all = []
    dist_changes = 0; blocked = 0  # [canonical: N/A — sim internal]
    for i in range(n):
        r = sim_duel_v2(w_a=w_a, w_b=w_b, arm_a=arm_a, arm_b=arm_b,
                        use_distance=use_distance, start_dist=start_dist,
                        arena=arena, seed=4000+i,  # [canonical: N/A — sim internal]
                        agi_a=agi_a, agi_b=agi_b, str_a=str_a, str_b=str_b, **kw)
        wins[r['w']] += 1  # [canonical: N/A — sim internal]
        rounds_list.append(r.get('rd', 30))  # [canonical: N/A — sim internal]
        dmg_a_all.extend(r.get('dmg_per_hit_a', []))
        dmg_b_all.extend(r.get('dmg_per_hit_b', []))
        dist_changes += r.get('dist_changes', 0)  # [canonical: N/A — sim internal]
        blocked += r.get('blocked_rounds', 0)  # [canonical: N/A — sim internal]
    return {
        'A_win': wins['A'] / n * 100, 'B_win': wins['B'] / n * 100,  # [canonical: N/A — sim internal]
        'draw': wins['draw'] / n * 100,  # [canonical: N/A — sim internal]
        'avg_rounds': np.mean(rounds_list),
        'avg_dmg_per_hit_A': np.mean(dmg_a_all) if dmg_a_all else 0,  # [canonical: N/A — sim internal]
        'avg_dmg_per_hit_B': np.mean(dmg_b_all) if dmg_b_all else 0,  # [canonical: N/A — sim internal]
        'avg_dist_changes': dist_changes / n,
        'avg_blocked': blocked / n,
    }


if __name__ == '__main__':
    N = 3000  # [canonical: N/A — sim internal]
    print("=" * 75)  # [canonical: N/A — formatting]
    print("T2.4 RERUN: Warhammer vs Arming Sword — WITH and WITHOUT distance")
    print("=" * 75)  # [canonical: N/A — formatting]
    print(f"N={N}. Equal stats: Agi 4, STR 4, End 4, COG 4, Hist 2. Arena 3.")
    print(f"Warhammer: TN 7.0, Long reach, STR×3, Bash only")
    print(f"Arming sword: TN 7.0, Mid reach, STR×1, Cut/Thrust")
    print(f"Start distance: Mid (neutral). Pass: WH DPS <= 1.3× AS at any tier.\n")

    for armour in ARMOUR_TIERS:
        r_no = run_batch(N, 'warhammer', 'arming_sword', arm_a=armour, arm_b=armour,
                         use_distance=False, arena=3)  # [canonical: N/A — sim internal]
        r_dist = run_batch(N, 'warhammer', 'arming_sword', arm_a=armour, arm_b=armour,
                           use_distance=True, arena=3)  # [canonical: N/A — sim internal]
        print(f"  vs {armour:6s}:")
        print(f"    NO DIST:   WH {r_no['A_win']:5.1f}%  AS {r_no['B_win']:5.1f}%  "
              f"Draw {r_no['draw']:4.1f}%  Rds {r_no['avg_rounds']:.1f}  "  # [canonical: N/A — sim internal]
              f"DPH(WH) {r_no['avg_dmg_per_hit_A']:.1f}  DPH(AS) {r_no['avg_dmg_per_hit_B']:.1f}")
        print(f"    WITH DIST: WH {r_dist['A_win']:5.1f}%  AS {r_dist['B_win']:5.1f}%  "
              f"Draw {r_dist['draw']:4.1f}%  Rds {r_dist['avg_rounds']:.1f}  "  # [canonical: N/A — sim internal]
              f"DPH(WH) {r_dist['avg_dmg_per_hit_A']:.1f}  DPH(AS) {r_dist['avg_dmg_per_hit_B']:.1f}  "
              f"DistΔ {r_dist['avg_dist_changes']:.1f}")
        if r_no['avg_dmg_per_hit_B'] > 0:  # [canonical: N/A — sim internal]
            ratio_no = r_no['avg_dmg_per_hit_A'] / max(0.1, r_no['avg_dmg_per_hit_B'])  # [canonical: N/A — sim internal]
            ratio_dist = r_dist['avg_dmg_per_hit_A'] / max(0.1, r_dist['avg_dmg_per_hit_B'])  # [canonical: N/A — sim internal]
            print(f"    DPH ratio: {ratio_no:.2f}× → {ratio_dist:.2f}× | "
                  f"PASS: {'YES' if ratio_dist <= 1.3 else 'NO (>1.3×)'}")  # [canonical: N/A — sim internal]
        print()

    print("\n" + "=" * 75)  # [canonical: N/A — formatting]
    print("T6.1 RERUN: Longsword vs All Weapons — WITH and WITHOUT distance")
    print("=" * 75)  # [canonical: N/A — formatting]
    print(f"N={N}. Equal stats. Arena 3. Pass: no matchup >75% for longsword.\n")

    opponents = ['dagger', 'arming_sword', 'mace', 'spear', 'warhammer']
    for armour in ['None', 'Medium', 'Heavy']:
        print(f"--- {armour} armour ---")
        for opp in opponents:
            r_no = run_batch(N, 'longsword', opp, arm_a=armour, arm_b=armour,
                             use_distance=False, arena=3)  # [canonical: N/A — sim internal]
            r_dist = run_batch(N, 'longsword', opp, arm_a=armour, arm_b=armour,
                               use_distance=True, arena=3)  # [canonical: N/A — sim internal]
            delta = r_dist['A_win'] - r_no['A_win']
            flag = " **FAIL**" if r_dist['A_win'] > 75 else ""  # [canonical: N/A — sim internal]
            print(f"  vs {opp:13s}: NO DIST {r_no['A_win']:5.1f}% | "
                  f"WITH DIST {r_dist['A_win']:5.1f}% (Δ{delta:+5.1f}pp) "  # [canonical: N/A — sim internal]
                  f"Rds {r_dist['avg_rounds']:.1f} DistΔ {r_dist['avg_dist_changes']:.1f}{flag}")
        print()

    print("=" * 75)  # [canonical: N/A — formatting]
    print("T5.1 SANITY: Spear vs Dagger at fixed starting distances")
    print("=" * 75)  # [canonical: N/A — formatting]
    print(f"N={N}. Heavy armour. Arena 3. Pass: specialist wins 75%+ at optimal range.\n")
    for sd, sdn in [(DIST_SHORT, 'Short'), (DIST_MID, 'Mid'), (DIST_LONG, 'Long')]:
        r = run_batch(N, 'spear', 'dagger', arm_a='Heavy', arm_b='Heavy',
                      use_distance=True, start_dist=sd, arena=3)  # [canonical: N/A — sim internal]
        print(f"  Start {sdn:5s}: Spear {r['A_win']:5.1f}%  Dagger {r['B_win']:5.1f}%  "
              f"Draw {r['draw']:4.1f}%  Rds {r['avg_rounds']:.1f}  DistΔ {r['avg_dist_changes']:.1f}")  # [canonical: N/A — sim internal]

    print(f"\n--- Agi asymmetry: Spear(Agi 3) vs Dagger(Agi 5) start Long ---")
    r = run_batch(N, 'spear', 'dagger', arm_a='Heavy', arm_b='Heavy',
                  use_distance=True, start_dist=DIST_LONG, arena=3, agi_a=3, agi_b=5)  # [canonical: N/A — sim internal]
    print(f"  Spear(Agi3) {r['A_win']:5.1f}%  Dagger(Agi5) {r['B_win']:5.1f}%  DistΔ {r['avg_dist_changes']:.1f}")

    print(f"--- Agi asymmetry: Spear(Agi 5) vs Dagger(Agi 3) start Short ---")
    r = run_batch(N, 'spear', 'dagger', arm_a='Heavy', arm_b='Heavy',
                  use_distance=True, start_dist=DIST_SHORT, arena=3, agi_a=5, agi_b=3)  # [canonical: N/A — sim internal]
    print(f"  Spear(Agi5) {r['A_win']:5.1f}%  Dagger(Agi3) {r['B_win']:5.1f}%  DistΔ {r['avg_dist_changes']:.1f}")
