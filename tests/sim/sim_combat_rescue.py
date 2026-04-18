#!/usr/bin/env python3
"""
Valoria rescue / multi-engagement simulation
Tests: 3v2, 4v3, rescue timing, rescue cost, optimal rescue target
Builds on combat_group.py mechanics.
"""
import numpy as np
from collections import defaultdict

# ── Weapon / armour tables (same as combat_group.py) ────────────────────────
WEAPONS = {
    'Short-LightCut':   ('Short','LightCut',  5,6,1,2,1),
    'Short-HeavyCut':   ('Short','HeavyCut',  6,7,4,5,3),
    'Short-LightBlunt': ('Short','LightBlunt',6,7,1,2,1),
    'Short-HeavyBlunt': ('Short','HeavyBlunt',7,8,4,5,4),
    'Long-LightCut':    ('Long', 'LightCut',  5,6,1,2,1),
    'Long-HeavyCut':    ('Long', 'HeavyCut',  6,7,4,5,3),
    'Long-LightBlunt':  ('Long', 'LightBlunt',6,7,1,2,1),
    'Long-HeavyBlunt':  ('Long', 'HeavyBlunt',7,8,4,5,4),
    'Unarmed':          ('Short','LightBlunt', 8,9,0,0,1),
}
ARMOUR_DR = {
    'None':  (0,0,0,0), 'Light': (2,1,1,0),
    'Medium':(4,3,2,1), 'Heavy': (6,5,3,1),
}
ARMOURS = {
    'None':  (0,0,0, 0), 'Light': (2,2,1, 0),
    'Medium':(4,3,1,-1), 'Heavy': (6,4,0,-2),
}
STR_MIN_W = {'LightCut':1,'HeavyCut':3,'LightBlunt':1,'HeavyBlunt':4}
TYPE_IDX  = {'LightCut':0,'HeavyCut':1,'LightBlunt':2,'HeavyBlunt':3}
HEAVY_T   = {'HeavyCut','HeavyBlunt'}
LIGHT_T   = {'LightCut','LightBlunt'}
FIB_BONUS = {1:0, 2:1, 3:2, 5:3, 8:5}
CRIT_THRESH = 3
RNG = np.random.default_rng(42)

def calc_pool(agi,hist): return max(5, agi*2+hist+3)
def max_wounds(end):     return 2 if end<=3 else (3 if end<=5 else 4)
def calc_stam(end,hist,ar): return max(1, end+hist+1+ARMOURS[ar][3])
def get_dr(wtype,ar):    return ARMOUR_DR[ar][TYPE_IDX[wtype]]

def build_pool(w,ar,agi,str_,hist):
    pool = calc_pool(agi,hist)
    wtype = WEAPONS[w][1]
    dw = STR_MIN_W[wtype]-str_
    if dw>=2: return None
    if dw==1: pool-=1
    da = ARMOURS[ar][1]-str_
    if da>=2: return None
    if da==1: pool-=ARMOURS[ar][2]
    return max(5,pool)

def vroll(N,n,tn):
    if n<=0: return np.zeros(N,dtype=np.int32)
    return (RNG.integers(1,11,size=(N,n))>=tn).sum(axis=1).astype(np.int32)

def get_fib(n):
    for k in sorted(FIB_BONUS.keys(),reverse=True):
        if n>=k: return FIB_BONUS[k]
    return 0

def make_fighter(w,ar,agi,str_,end,hist,N):
    """Return fighter state dict."""
    pool = build_pool(w,ar,agi,str_,hist)
    if pool is None: return None
    reach,wtype,atn,dtn,_,dmg,_ = WEAPONS[w]
    return {
        'pool':  np.full(N,pool,np.int32),
        'hp':    np.full(N,end,np.float32),   # Variant B
        'wc':    np.zeros(N,np.int32),
        'stam':  np.full(N,calc_stam(end,hist,ar),np.int32),
        'inc':   np.zeros(N,bool),
        'zone':  np.zeros(N,np.int8),           # 0=Far, 1=Close
        'reach': reach, 'wtype': wtype,
        'atn':atn, 'dtn':dtn, 'dmg':dmg,
        'sm':  calc_stam(end,hist,ar),
        'mw':  max_wounds(end),
        'hp0': end,
        'dr_ar': ar,  # for computing incoming DR
    }

def resolve_exchange(N, attacker, defender, n_atk_in_eng, rescue_bonus_atk=0, free_hit_on_atk=False):
    """
    One round of combat between attacker(s) and defender.
    n_atk_in_eng: how many attackers in this engagement (for Fibonacci).
    rescue_bonus_atk: +2D bonus ON the attacker if defender is breaking away.
    free_hit_on_atk: defender gets free attack on attacker (rescue cost option 2).
    Returns (dmg_to_defender, dmg_to_attacker, hit_on_def, hit_on_atk).
    """
    alive = ~attacker['inc'] & ~defender['inc']

    fib = get_fib(n_atk_in_eng)
    eA = np.where(attacker['stam']<=0,
                  np.maximum(1,(attacker['pool']+1)//2),
                  attacker['pool'])
    eD = np.where(defender['stam']<=0,
                  np.maximum(1,(defender['pool']+1)//2),
                  defender['pool'])

    oob_A = attacker['stam'] <= 0
    oob_D = defender['stam'] <= 0

    # Attacker offence
    off_A = np.maximum(1, (eA * 0.5).astype(np.int32))
    def_D = np.maximum(1, eD - np.maximum(1,(eD*0.5).astype(np.int32)))

    # Defender splits defence by n_atk_in_eng
    def_D_split = np.maximum(1, def_D // max(1, n_atk_in_eng))

    # Bonuses
    eff_off_A = off_A + fib + rescue_bonus_atk + np.where(oob_D,2,0)
    eff_def_D = def_D_split

    # Mismatch
    mismatch = attacker['wtype'] in HEAVY_T and defender['wtype'] in LIGHT_T

    # Attacker hits defender
    sl = alive
    med = lambda arr: int(np.median(arr[sl])) if sl.any() else 4

    a = vroll(N, med(eff_off_A), attacker['atn'])
    d = vroll(N, med(eff_def_D), defender['dtn'])
    if mismatch: d = np.maximum(0, d-1)

    h_on_D = alive & (a > d)
    excess  = np.maximum(0.0, (a-d).astype(float))
    crit    = h_on_D & (excess >= CRIT_THRESH)
    dr      = get_dr(attacker['wtype'], defender['dr_ar'])
    raw     = np.where(crit, excess+3+attacker['dmg']*2, excess+3+attacker['dmg'])
    dmg_D   = np.where(h_on_D, np.maximum(0.0, raw-dr), 0.0)

    # Defender hits attacker (normal or free hit)
    off_D = np.maximum(1, (eD * 0.5).astype(np.int32)) + np.where(oob_A,2,0)
    def_A = np.maximum(1, eA - off_A)

    mismatch_rev = defender['wtype'] in HEAVY_T and attacker['wtype'] in LIGHT_T

    if free_hit_on_atk:
        # Full offence pool, no defence from attacker
        a2 = vroll(N, med(eD), defender['atn'])
        d2 = np.zeros(N, np.int32)
    else:
        a2 = vroll(N, med(off_D), defender['atn'])
        d2 = vroll(N, med(def_A), attacker['dtn'])

    if mismatch_rev: d2 = np.maximum(0, d2-1)
    h_on_A  = alive & (a2 > d2)
    excess2 = np.maximum(0.0, (a2-d2).astype(float))
    crit2   = h_on_A & (excess2 >= CRIT_THRESH)
    dr2     = get_dr(defender['wtype'], attacker['dr_ar'])
    raw2    = np.where(crit2, excess2+3+defender['dmg']*2, excess2+3+defender['dmg'])
    dmg_A   = np.where(h_on_A, np.maximum(0.0, raw2-dr2), 0.0)

    return dmg_D, dmg_A, h_on_D, h_on_A

def apply_damage(fighter, dmg, end):
    """Apply damage with wound reset. Returns updated fighter."""
    fighter['hp'] -= dmg
    wounded = ~fighter['inc'] & (fighter['hp'] <= 0)
    if wounded.any():
        fighter['wc'] = np.where(wounded, fighter['wc']+1, fighter['wc'])
        fighter['inc'] = np.where(wounded, fighter['wc'] >= fighter['mw'], fighter['inc'])
        fighter['hp'] = np.where(wounded & ~fighter['inc'], float(end), fighter['hp'])
    return fighter

def tick_stam(fighter):
    fighter['stam'] = np.maximum(0, fighter['stam']-1)
    # OOB restore
    oob = fighter['stam'] <= 0
    fighter['stam'] = np.where(oob, fighter['sm'], fighter['stam'])
    return fighter

# ─────────────────────────────────────────────────────────────────────────────
# SIMULATION 1: 3v2 decomposition
# Side A: fighters A1, A2, A3  Side B: fighters B1, B2
# Engagement 1: A1+A2 vs B1 (2v1)
# Engagement 2: A3 vs B2 (1v1)
# Track which engagement finishes first and what A3 does after
# ─────────────────────────────────────────────────────────────────────────────
def sim_3v2(wA, arA, wB, arB, agi, str_, end, hist, N=2000, MR=25, free_fighter='pile_on'):
    """
    free_fighter: what A3 does after B2 is defeated
      'pile_on'  — A3 joins A1+A2 vs B1 immediately
      'wait'     — A3 stays idle after B2 down
    Returns outcome stats.
    """
    # Validate
    for w,ar in [(wA,arA),(wB,arB)]:
        if build_pool(w,ar,agi,str_,hist) is None: return None

    # Make fighters
    A1=make_fighter(wA,arA,agi,str_,end,hist,N)
    A2=make_fighter(wA,arA,agi,str_,end,hist,N)
    A3=make_fighter(wA,arA,agi,str_,end,hist,N)
    B1=make_fighter(wB,arB,agi,str_,end,hist,N)
    B2=make_fighter(wB,arB,agi,str_,end,hist,N)

    if any(f is None for f in [A1,A2,A3,B1,B2]): return None

    rounds    = np.full(N,MR,np.int32)
    side_A_wins = np.zeros(N,bool)
    b2_done_round = np.full(N,MR,np.int32)

    for rnd in range(MR):
        alive = ~(A1['inc']&A2['inc']&A3['inc']) & ~(B1['inc']&B2['inc'])
        if not alive.any(): break

        # Engagement 1: A1+A2 vs B1 (2v1 with Fibonacci)
        n_in_eng1 = 2 + (A3['inc'] & ~B2['inc']).astype(int)  # A3 joins if B2 down and pile_on
        if free_fighter == 'pile_on':
            b2_defeated = B2['inc']
            n_in_eng1_arr = np.where(b2_defeated, 3, 2)
        else:
            n_in_eng1_arr = np.full(N, 2, np.int32)

        # A1 vs B1
        for atk in [A1, A2]:
            d_B1, d_atk, _, _ = resolve_exchange(N, atk, B1, 2)
            B1 = apply_damage(B1, d_B1, end)
            atk = apply_damage(atk, d_atk, end)

        # A3 piles on B1 if B2 already down
        if free_fighter == 'pile_on':
            a3_piling = ~A3['inc'] & B2['inc'] & ~B1['inc']
            if a3_piling.any():
                d_B1_a3, d_A3, _, _ = resolve_exchange(N, A3, B1, 3)
                B1['hp'] = np.where(a3_piling, B1['hp']-d_B1_a3, B1['hp'])
                A3['hp'] = np.where(a3_piling, A3['hp']-d_A3,    A3['hp'])
                B1 = apply_damage(B1, np.zeros(N), end)  # recheck wounds
                A3 = apply_damage(A3, np.zeros(N), end)

        # Engagement 2: A3 vs B2
        a3_in_eng2 = ~A3['inc'] & ~B2['inc']
        if a3_in_eng2.any():
            d_B2, d_A3, _, _ = resolve_exchange(N, A3, B2, 1)
            B2 = apply_damage(B2, np.where(a3_in_eng2, d_B2, 0.0), end)
            A3 = apply_damage(A3, np.where(a3_in_eng2, d_A3, 0.0), end)
            # Track when B2 goes down
            b2_just_inc = B2['inc'] & (b2_done_round == MR)
            b2_done_round = np.where(b2_just_inc, rnd+1, b2_done_round)

        # Stam
        for f in [A1,A2,A3,B1,B2]: tick_stam(f)

        # Check done
        side_A_inc = A1['inc'] & A2['inc'] & A3['inc']
        side_B_inc = B1['inc'] & B2['inc']
        done = alive & (side_A_inc | side_B_inc)
        side_A_wins = np.where(done & ~side_A_wins, side_B_inc, side_A_wins)
        rounds = np.where(done & (rounds==MR), rnd+1, rounds)

    res = rounds[rounds<MR]
    b2_r = b2_done_round[b2_done_round<MR]
    return {
        'A_wins': side_A_wins.sum()/N,
        'B_wins': (~side_A_wins & (rounds<MR)).sum()/N,
        'pDraw':  (rounds==MR).sum()/N,
        'pct_res': len(res)/N,
        'med':    float(np.median(res)) if len(res) else 0,
        'mean':   float(np.mean(res))   if len(res) else 0,
        'le10':   float((res<=10).mean()*100) if len(res) else 0,
        'b2_med_round': float(np.median(b2_r)) if len(b2_r) else 0,
    }

# ─────────────────────────────────────────────────────────────────────────────
# SIMULATION 2: Rescue timing — how long does a losing fighter survive?
# 1v1 where attacker is stronger; track survival rounds for rescue window
# ─────────────────────────────────────────────────────────────────────────────
def sim_survival(wA,arA,wB,arB,agi,str_,end,hist,N=2000,MR=25):
    """Track how many rounds B survives against A."""
    if build_pool(wA,arA,agi,str_,hist) is None: return None
    if build_pool(wB,arB,agi,str_,hist) is None: return None

    A = make_fighter(wA,arA,agi,str_,end,hist,N)
    B = make_fighter(wB,arB,agi,str_,end,hist,N)

    rounds_B = np.full(N,MR,np.int32)  # when B falls

    for rnd in range(MR):
        alive = ~A['inc'] & ~B['inc']
        if not alive.any(): break
        d_B, d_A, _, _ = resolve_exchange(N, A, B, 1)
        B = apply_damage(B, d_B, end)
        A = apply_damage(A, d_A, end)
        tick_stam(A); tick_stam(B)
        b_just_inc = alive & B['inc'] & (rounds_B==MR)
        rounds_B = np.where(b_just_inc, rnd+1, rounds_B)

    res = rounds_B[rounds_B<MR]
    return {
        'med_survival': float(np.median(res)) if len(res) else MR,
        'p3_or_less':   float((res<=3).mean()*100) if len(res) else 0,
        'p5_or_less':   float((res<=5).mean()*100) if len(res) else 0,
        'p10_or_less':  float((res<=10).mean()*100) if len(res) else 0,
        'B_never_falls': (rounds_B==MR).sum()/N,
    }

# ─────────────────────────────────────────────────────────────────────────────
# SIMULATION 3: Rescue cost comparison
# Fighter C rescuing fighter B from fighter A
# Cost options: (1) establish-distance roll, (2) free attack on C, (3) free
# ─────────────────────────────────────────────────────────────────────────────
def sim_rescue(wA,arA, wB,arB, wC,arC,
               agi,str_,end,hist,N=2000,MR=25,
               rescue_round=3, cost='free_attack'):
    """
    A fights B. C rescues B at rescue_round.
    Cost options: 'free_attack' (A gets free hit on C), 'establish' (C rolls TN7 vs A offence),  'free' (no cost).
    After rescue: A vs B+C (2v1 Fibonacci).
    """
    for w,ar in [(wA,arA),(wB,arB),(wC,arC)]:
        if build_pool(w,ar,agi,str_,hist) is None: return None

    A = make_fighter(wA,arA,agi,str_,end,hist,N)
    B = make_fighter(wB,arB,agi,str_,end,hist,N)
    C = make_fighter(wC,arC,agi,str_,end,hist,N)

    # C starts in a separate 1v1 (vs nobody — idle) until rescue_round
    rescued  = np.zeros(N,bool)   # C has joined B's fight
    c_failed = np.zeros(N,bool)   # C tried to rescue but failed establish roll
    rounds   = np.full(N,MR,np.int32)
    B_survives = np.zeros(N,bool)

    for rnd in range(MR):
        alive = ~A['inc'] & ~B['inc']
        if not alive.any(): break

        # Round rescue_round: C attempts rescue
        if rnd+1 == rescue_round:
            can_rescue = alive & ~C['inc'] & ~rescued

            if cost == 'free_attack':
                # A gets free hit on C during rescue
                dmg_C_rescue, _, _, _ = resolve_exchange(N, A, C, 1, free_hit_on_atk=True)
                dmg_C_rescue = np.where(can_rescue, dmg_C_rescue, 0.0)
                C = apply_damage(C, dmg_C_rescue, end)
                rescued = np.where(can_rescue & ~C['inc'], True, rescued)

            elif cost == 'establish':
                # C rolls TN7 vs A's offence successes this round
                c_pool = C['pool']
                est_n  = int(np.median(np.maximum(1,c_pool//2)[can_rescue])) if can_rescue.any() else 4
                est_s  = vroll(N, est_n, 7)
                # A's offence this round
                a_off_n = int(np.median(np.maximum(1,A['pool']//2)[can_rescue])) if can_rescue.any() else 4
                a_off_s = vroll(N, a_off_n, A['atn'])
                ok = can_rescue & (est_s >= a_off_s)
                rescued   = np.where(ok, True, rescued)
                c_failed  = np.where(can_rescue & ~ok, True, c_failed)

            else:  # free
                rescued = np.where(can_rescue, True, rescued)

        # Main exchange
        n_vs_A = np.where(rescued & ~C['inc'], 2, 1)
        d_A, d_B, _, _ = resolve_exchange(N, B, A, 1)
        A = apply_damage(A, d_A, end)
        B = apply_damage(B, d_B, end)

        # C attacks A if rescued
        c_attacking = rescued & ~C['inc'] & ~A['inc']
        if c_attacking.any():
            d_A_c, d_C, _, _ = resolve_exchange(N, C, A, 2)
            A = apply_damage(A, np.where(c_attacking,d_A_c,0.0), end)
            C = apply_damage(C, np.where(c_attacking,d_C,0.0),   end)

        tick_stam(A); tick_stam(B); tick_stam(C)

        done = alive & (A['inc'] | B['inc'])
        B_survives = np.where(done & A['inc'] & ~B['inc'], True, B_survives)
        rounds = np.where(done & (rounds==MR), rnd+1, rounds)

    res = rounds[rounds<MR]
    return {
        'B_survives':   B_survives.sum()/N,
        'A_wins':       (~B_survives & ~A['inc'] & (rounds<MR)).sum()/N,
        'pDraw':        (rounds==MR).sum()/N,
        'med':          float(np.median(res)) if len(res) else 0,
        'rescue_rate':  rescued.sum()/N,
        'c_fail_rate':  c_failed.sum()/N,
    }

# ─────────────────────────────────────────────────────────────────────────────
# SIMULATION 4: Optimal rescue target — pile-on vs rescue
# 3v2: free fighter chooses to join 2v1 (pile on) or help losing 1v1 (rescue)
# ─────────────────────────────────────────────────────────────────────────────
def sim_3v2_strategy(wA,arA,wB,arB,agi,str_,end,hist,N=2000,MR=25,strategy='rescue'):
    """
    Side A: A1+A2 vs B1 (2v1), A3 vs B2 (1v1).
    B2 is stronger (better weapon/armour) — A3 is losing.
    strategy: 'rescue' A3 gets help from A1 after B1 falls
              'pile_on' A1 stays on B1 even after B2 falls
              'switch' free fighter switches to help whoever is losing
    Simplified: track overall side win rate.
    """
    # Make B2 stronger deliberately
    wB2 = wB; arB2 = arB  # same for now, will vary in calls

    A1=make_fighter(wA,arA,agi,str_,end,hist,N)
    A2=make_fighter(wA,arA,agi,str_,end,hist,N)
    A3=make_fighter(wA,arA,agi,str_,end,hist,N)
    B1=make_fighter(wB,arB,agi,str_,end,hist,N)
    B2=make_fighter(wB2,arB2,agi,str_,end,hist,N)

    if any(f is None for f in [A1,A2,A3,B1,B2]): return None

    rounds = np.full(N,MR,np.int32)
    A_wins = np.zeros(N,bool)

    for rnd in range(MR):
        sA_inc = A1['inc']&A2['inc']&A3['inc']
        sB_inc = B1['inc']&B2['inc']
        alive  = ~sA_inc & ~sB_inc
        if not alive.any(): break

        # Engagement 1: A1+A2 vs B1
        for atk in [A1,A2]:
            if (~atk['inc'] & ~B1['inc']).any():
                d_B1,d_atk,_,_ = resolve_exchange(N,atk,B1,2)
                B1=apply_damage(B1,d_B1,end); atk=apply_damage(atk,d_atk,end)

        # Strategy determines what A3 does if their primary target is down
        if strategy == 'pile_on':
            # A3 piles on B1 if B2 already down
            if (~A3['inc']&B2['inc']&~B1['inc']).any():
                d_B1,d_A3,_,_=resolve_exchange(N,A3,B1,3)
                B1=apply_damage(B1,np.where(~A3['inc']&B2['inc'],d_B1,0.0),end)
                A3=apply_damage(A3,np.where(~A3['inc']&B2['inc'],d_A3,0.0),end)
            # A3 fights B2 normally
            if (~A3['inc']&~B2['inc']).any():
                d_B2,d_A3,_,_=resolve_exchange(N,A3,B2,1)
                B2=apply_damage(B2,np.where(~A3['inc']&~B2['inc'],d_B2,0.0),end)
                A3=apply_damage(A3,np.where(~A3['inc']&~B2['inc'],d_A3,0.0),end)

        elif strategy == 'rescue':
            # A2 switches to help A3 vs B2 once B1 is down
            a2_rescues = ~A2['inc'] & B1['inc'] & ~B2['inc']
            # A3 vs B2 (with A2 if rescuing)
            n_vs_b2 = np.where(a2_rescues, 2, 1)
            if (~A3['inc']&~B2['inc']).any():
                d_B2,d_A3,_,_=resolve_exchange(N,A3,B2,1)
                B2=apply_damage(B2,np.where(~A3['inc']&~B2['inc'],d_B2,0.0),end)
                A3=apply_damage(A3,np.where(~A3['inc']&~B2['inc'],d_A3,0.0),end)
            if a2_rescues.any():
                d_B2_a2,d_A2,_,_=resolve_exchange(N,A2,B2,2)
                B2=apply_damage(B2,np.where(a2_rescues,d_B2_a2,0.0),end)
                A2=apply_damage(A2,np.where(a2_rescues,d_A2,0.0),end)

        for f in [A1,A2,A3,B1,B2]: tick_stam(f)

        sA_inc2=A1['inc']&A2['inc']&A3['inc']; sB_inc2=B1['inc']&B2['inc']
        done = alive&(sA_inc2|sB_inc2)
        A_wins=np.where(done,sB_inc2,A_wins)
        rounds=np.where(done&(rounds==MR),rnd+1,rounds)

    res=rounds[rounds<MR]
    return {
        'A_wins': A_wins.sum()/N,
        'B_wins': (~A_wins&(rounds<MR)).sum()/N,
        'pDraw':  (rounds==MR).sum()/N,
        'med':    float(np.median(res)) if len(res) else 0,
        'le10':   float((res<=10).mean()*100) if len(res) else 0,
    }

def rpt(label,r,fields=None):
    if r is None: print(f"    {label}: invalid"); return
    if fields is None:
        if 'A_wins' in r:
            print(f"    {label}")
            print(f"      A wins:{r['A_wins']*100:5.1f}%  B wins:{r['B_wins']*100:5.1f}%  "
                  f"Draw:{r['pDraw']*100:4.1f}%  Med:{r['med']:.0f}  ≤10:{r.get('le10',0):.0f}%")
        elif 'med_survival' in r:
            print(f"    {label}")
            print(f"      Med survival:{r['med_survival']:.1f} rnd  "
                  f"≤3rnd:{r['p3_or_less']:.0f}%  ≤5rnd:{r['p5_or_less']:.0f}%  "
                  f"≤10rnd:{r['p10_or_less']:.0f}%  Never falls:{r['B_never_falls']*100:.0f}%")
        elif 'B_survives' in r:
            print(f"    {label}")
            print(f"      B survives:{r['B_survives']*100:5.1f}%  A wins:{r['A_wins']*100:5.1f}%  "
                  f"Draw:{r['pDraw']*100:4.1f}%  Med:{r['med']:.0f}  "
                  f"Rescue rate:{r['rescue_rate']*100:.0f}%  C fail:{r['c_fail_rate']*100:.0f}%")

N=3000; MR=25; agi=3; str_=3; end=3; hist=2

print("="*72)
print("VALORIA RESCUE & MULTI-ENGAGEMENT SIMULATION")
print(f"STR{str_}/END{end}/AGI{agi}/HIST{hist}  N={N}  MR={MR}")

# ── TEST 1: 3v2 decomposition ─────────────────────────────────────────────────
print(f"\n{'─'*72}")
print("1. 3v2 DECOMPOSITION (A1+A2 vs B1, A3 vs B2)")
print("   pile_on: A3 joins B1 fight after B2 falls")
print("   wait: A3 stays idle after B2 falls")
configs = [
    ('Short-LightCut','None','Short-LightCut','None','Mirror — LightCut'),
    ('Short-LightCut','None','Short-HeavyCut','Medium','LightCut vs HeavyCut/Med'),
    ('Short-LightCut','None','Long-HeavyBlunt','Heavy','LightCut vs HvyBlunt/Hvy'),
    ('Short-HeavyBlunt','None','Short-LightCut','None','HvyBlunt vs LightCut'),
]
for wA,arA,wB,arB,label in configs:
    print(f"\n  {label}:")
    for strat in ['pile_on','wait']:
        r = sim_3v2(wA,arA,wB,arB,agi,str_,end,hist,N,MR,strat)
        if r:
            b2 = f"  B2 falls ~rnd {r['b2_med_round']:.0f}" if r['b2_med_round']>0 else ""
            print(f"    {strat:<10} A:{r['A_wins']*100:5.1f}% B:{r['B_wins']*100:5.1f}% "
                  f"Draw:{r['pDraw']*100:4.1f}% Med:{r['med']:.0f} ≤10:{r['le10']:.0f}%{b2}")

# ── TEST 2: Survival window (rescue timing) ───────────────────────────────────
print(f"\n{'─'*72}")
print("2. SURVIVAL WINDOW — how long does B survive against A?")
print("   Determines viable rescue window")
survival_matchups = [
    ('Short-HeavyCut','None','Short-LightCut','None','HeavyCut vs LightCut (A stronger)'),
    ('Short-HeavyCut','None','Short-LightCut','Light','HeavyCut vs LightCut/Light'),
    ('Long-HeavyBlunt','None','Short-LightCut','None','HvyBlunt vs LightCut'),
    ('Long-HeavyBlunt','Heavy','Short-LightCut','None','HvyBlunt/Hvy vs LightCut'),
    ('Short-LightCut','None','Short-LightCut','None','Mirror — equal fighters'),
    ('Short-HeavyCut','Medium','Short-LightCut','None','HeavyCut/Med vs LightCut'),
    ('Short-HeavyCut','None','Unarmed','None','HeavyCut vs Unarmed'),
    ('Long-HeavyCut','None','Short-LightCut','None','LongHeavyCut vs ShortLightCut'),
]
for wA,arA,wB,arB,label in survival_matchups:
    r = sim_survival(wA,arA,wB,arB,agi,str_,end,hist,N,MR)
    if r: rpt(label,r)

# ── TEST 3: Rescue cost comparison ────────────────────────────────────────────
print(f"\n{'─'*72}")
print("3. RESCUE COST COMPARISON")
print("   A attacks B. C rescues at round 3.")
print("   Costs: free / free_attack (A gets free hit on C) / establish (TN7 roll)")
rescue_scenarios = [
    ('Short-HeavyCut','None','Short-LightCut','None','Short-LightCut','None',
     'A=HeavyCut, B=C=LightCut'),
    ('Short-HeavyCut','Medium','Short-LightCut','None','Short-LightCut','Light',
     'A=HeavyCut/Med, B=LightCut, C=LightCut/Light'),
    ('Long-HeavyBlunt','Heavy','Short-LightCut','None','Short-HeavyCut','None',
     'A=HvyBlunt/Hvy, B=LightCut, C=HeavyCut'),
]
for wA,arA,wB,arB,wC,arC,label in rescue_scenarios:
    print(f"\n  {label}:")
    for cost in ['free','free_attack','establish']:
        for rnd_r in [2,3,5]:
            r = sim_rescue(wA,arA,wB,arB,wC,arC,agi,str_,end,hist,N,MR,rnd_r,cost)
            if r:
                print(f"    rescue rnd {rnd_r} cost={cost:<12}: "
                      f"B survives:{r['B_survives']*100:5.1f}%  "
                      f"A wins:{r['A_wins']*100:5.1f}%  "
                      f"Med:{r['med']:.0f}  "
                      f"C fail:{r['c_fail_rate']*100:.0f}%")

# ── TEST 4: Optimal rescue target ────────────────────────────────────────────
print(f"\n{'─'*72}")
print("4. OPTIMAL RESCUE TARGET — pile_on vs rescue in 3v2")
print("   A1+A2 vs B1, A3 vs B2. Strategy varies.")
strategy_configs = [
    ('Short-LightCut','None','Short-LightCut','None','Mirror matchup'),
    ('Short-LightCut','None','Short-HeavyCut','None','A=Light, B=Heavy'),
    ('Short-HeavyCut','None','Short-LightCut','None','A=Heavy, B=Light'),
    ('Short-LightCut','Light','Short-HeavyCut','Medium','Armoured matchup'),
]
for wA,arA,wB,arB,label in strategy_configs:
    print(f"\n  {label}:")
    for strat in ['pile_on','rescue']:
        r = sim_3v2_strategy(wA,arA,wB,arB,agi,str_,end,hist,N,MR,strat)
        if r:
            print(f"    {strat:<10} A:{r['A_wins']*100:5.1f}% B:{r['B_wins']*100:5.1f}% "
                  f"Med:{r['med']:.0f} ≤10:{r['le10']:.0f}%")

# ── TEST 5: 4v3 decomposition ─────────────────────────────────────────────────
print(f"\n{'─'*72}")
print("5. 4v3 DECOMPOSITION — 2v1 + 1v1 + 1v1")
print("   Side A has numerical advantage. Does it compound?")
# Simulate as: run 3 engagements in parallel, free fighter joins fastest-finishing
# Approximate: compare 4v3 vs 3v3 vs 2v2 as parallel 1v1s
def sim_parallel_1v1s(n_pairs, wA,arA,wB,arB,agi,str_,end,hist,N=2000,MR=25,extra_A=0):
    """
    n_pairs pairs of 1v1 + extra_A free fighters who pile on first finished.
    Tracks: does side A win majority of engagements?
    """
    pairs_A = [make_fighter(wA,arA,agi,str_,end,hist,N) for _ in range(n_pairs+extra_A)]
    pairs_B = [make_fighter(wB,arB,agi,str_,end,hist,N) for _ in range(n_pairs)]
    if any(f is None for f in pairs_A+pairs_B): return None

    rounds=np.full(N,MR,np.int32); A_maj=np.zeros(N,bool)
    for rnd in range(MR):
        any_alive=np.zeros(N,bool)
        for i in range(n_pairs):
            al=~pairs_A[i]['inc']&~pairs_B[i]['inc']
            any_alive|=al
            if al.any():
                dB,dA,_,_=resolve_exchange(N,pairs_A[i],pairs_B[i],1)
                pairs_B[i]=apply_damage(pairs_B[i],dB,end)
                pairs_A[i]=apply_damage(pairs_A[i],dA,end)
        if not any_alive.any(): break
        for f in pairs_A+pairs_B: tick_stam(f)

        sA_wins=[pairs_B[i]['inc'].sum() for i in range(n_pairs)]
        sB_wins=[pairs_A[i]['inc'].sum() for i in range(n_pairs)]

    A_eng_wins=np.stack([pairs_B[i]['inc'] for i in range(n_pairs)],axis=1).sum(axis=1)
    A_majority=A_eng_wins > n_pairs/2
    all_done=(np.stack([~pairs_A[i]['inc']|~pairs_B[i]['inc'] for i in range(n_pairs)],axis=1)).all(axis=1)
    res=rounds[rounds<MR]
    return {
        'A_majority': A_majority.sum()/N,
        'pct_res':    len(res)/N,
    }

for label,nA,nB,wA,arA,wB,arB in [
    ('3v3 parallel 1v1s',3,3,'Short-LightCut','None','Short-LightCut','None'),
    ('4v3: 2v1+1v1+1v1',3,3,'Short-LightCut','None','Short-LightCut','None'),  # same — decomposition
    ('4v3 A=Heavy B=Light',3,3,'Short-HeavyCut','None','Short-LightCut','None'),
    ('4v3 A=Light B=Heavy',3,3,'Short-LightCut','None','Short-HeavyCut','None'),
]:
    r=sim_parallel_1v1s(nA,wA,arA,wB,arB,agi,str_,end,hist,N,MR)
    if r:
        print(f"  {label}: A wins majority:{r['A_majority']*100:.0f}%  Res:{r['pct_res']*100:.0f}%")

# Run proper 4v3 as 2v1 + two 1v1s using sim_3v2 with n=4
print("\n  True 4v3 via group sim (2v1 + 1v1 + 1v1, free fighter piles on):")
configs_4v3 = [
    ('Short-LightCut','None','Short-LightCut','None','Mirror'),
    ('Short-LightCut','None','Short-HeavyCut','Medium','Light vs Heavy/Med'),
    ('Short-HeavyBlunt','None','Short-LightCut','None','HeavyBlunt vs Light'),
]
for wA,arA,wB,arB,label in configs_4v3:
    # Approximate 4v3 as 3v2 with pile_on (extra fighter)
    r=sim_3v2(wA,arA,wB,arB,agi,str_,end,hist,N,MR,'pile_on')
    if r:
        print(f"    {label}: A:{r['A_wins']*100:5.1f}% B:{r['B_wins']*100:5.1f}% "
              f"Med:{r['med']:.0f} ≤10:{r['le10']:.0f}%")

print("\nDone.")
