#!/usr/bin/env python3
"""
Valoria group combat simulation — Fibonacci + zone collapse
Mechanics:
  - Fibonacci bonus: 2v1=+1D, 3v1=+2D, 5v1=+3D, 8v1=+5D per attacker
  - Zone collapse: first Short attacker must establish distance normally;
    subsequent Short attackers enter Close zone automatically once one ally is inside
  - Defender splits defence pool across all attackers (evenly, rounded down, remainder to first)
  - Long weapons at Close zone: -1D offence, half damage
  - Mass mismatch penalty: -1 def success when Light splits vs Heavy (not Full Guard)
  - DR by weapon type vs armour tier
  - Crits: excess >= 3, modifier doubled
  - Wounds: HP=End, armour=DR (Variant B)
  - Stamina: OOB gives opponent(s) +2D
"""
import numpy as np
from collections import defaultdict

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
    'None':  (0,0,0,0),
    'Light': (2,1,1,0),
    'Medium':(4,3,2,1),
    'Heavy': (6,5,3,1),
}
ARMOURS = {
    'None':  (0,0,0, 0),
    'Light': (2,2,1, 0),
    'Medium':(4,3,1,-1),
    'Heavy': (6,4,0,-2),
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
    dw = STR_MIN_W[wtype] - str_
    if dw >= 2: return None
    if dw == 1: pool -= 1
    da = ARMOURS[ar][1] - str_
    if da >= 2: return None
    if da == 1: pool -= ARMOURS[ar][2]
    return max(5, pool)

def vroll(N, n, tn):
    if n <= 0: return np.zeros(N, dtype=np.int32)
    return (RNG.integers(1,11,size=(N,n)) >= tn).sum(axis=1).astype(np.int32)

def fib_bonus(n_attackers):
    """Closest Fibonacci number <= n_attackers"""
    for k in sorted(FIB_BONUS.keys(), reverse=True):
        if n_attackers >= k:
            return FIB_BONUS[k]
    return 0

def sim_group(
    atk_weapons,   # list of weapon names for attackers
    atk_armours,   # list of armour names for attackers
    def_weapon,    # defender weapon name
    def_armour,    # defender armour name
    agi, str_, end, hist,
    N=2000, MR=25
):
    """
    N_ATK attackers vs 1 defender.
    Returns dict of outcome stats.
    """
    N_ATK = len(atk_weapons)
    assert len(atk_armours) == N_ATK

    # Validate builds
    def_pool = build_pool(def_weapon, def_armour, agi, str_, hist)
    if def_pool is None: return None
    atk_pools = []
    for w,ar in zip(atk_weapons, atk_armours):
        p = build_pool(w, ar, agi, str_, hist)
        if p is None: return None
        atk_pools.append(p)

    # Defender stats
    dr,_,atnD,dtnD,dloD,dhiD,_ = WEAPONS[def_weapon]
    dmgD = dhiD
    hpD  = end  # Variant B
    drD_self = 0  # DR applied TO defender from attacker weapons
    smD  = calc_stam(end, hist, def_armour)
    mw   = max_wounds(end)
    defR = dr  # reach of defender

    # Attacker stats
    atk_reach  = [WEAPONS[w][0] for w in atk_weapons]
    atk_wtype  = [WEAPONS[w][1] for w in atk_weapons]
    atk_atn    = [WEAPONS[w][2] for w in atk_weapons]
    atk_dtn    = [WEAPONS[w][3] for w in atk_weapons]
    atk_dmg    = [WEAPONS[w][5] for w in atk_weapons]  # hi dmg
    atk_sm     = [calc_stam(end, hist, ar) for ar in atk_armours]
    # Expand scalar pools to N-length arrays for vectorised ops
    atk_pools  = [np.full(N, p, np.int32) for p in atk_pools]
    atk_hp     = end  # same for all in Variant B
    atk_dr     = [get_dr(WEAPONS[def_weapon][1], ar) for ar in atk_armours]  # DR vs defender's weapon
    def_dr_vs  = [get_dr(wt, def_armour) for wt in atk_wtype]  # defender's DR vs each attacker

    # State arrays (N simulations)
    hD   = np.full(N, hpD,  np.float32)
    wcD  = np.zeros(N, np.int32)
    sD   = np.full(N, smD,  np.int32)
    incD = np.zeros(N, bool)

    # Per-attacker state
    hA   = [np.full(N, atk_hp,   np.float32) for _ in range(N_ATK)]
    wcA  = [np.zeros(N, np.int32)             for _ in range(N_ATK)]
    sA   = [np.full(N, sm,       np.int32)    for sm in atk_sm]
    incA = [np.zeros(N, bool)                 for _ in range(N_ATK)]

    # Zone state per attacker (0=Far/Long, 1=Close/Short)
    # All start at Long (Far) zone
    zone = [np.zeros(N, np.int8) for _ in range(N_ATK)]
    # Zone collapsed flag: once one Short attacker is at Close, others enter free
    zone_collapsed = np.zeros(N, bool)

    rounds = np.full(N, MR, np.int32)
    # Off successes for defender this round (for establish distance ob)
    def_off_s = np.zeros(N, np.int32)

    for rnd in range(MR):
        # Which sims are still running?
        alive_D = ~incD
        alive_A = [~inc for inc in incA]
        any_alive = alive_D & np.any(np.stack([~inc for inc in incA], axis=1), axis=1)
        if not any_alive.any(): break

        # Active attackers this round
        active = [any_alive & ~incA[i] for i in range(N_ATK)]

        # OOB check — defender
        oobD = alive_D & (sD <= 0)
        sD   = np.where(oobD, smD, sD)
        eD   = np.where(oobD, np.maximum(1,(def_pool+1)//2), def_pool).astype(np.int32)

        # OOB check — attackers
        oobA = [active[i] & (sA[i] <= 0) for i in range(N_ATK)]
        for i in range(N_ATK):
            sA[i] = np.where(oobA[i], atk_sm[i], sA[i])

        # Fibonacci bonus
        # Count active attackers at correct range this round
        n_correct = np.zeros(N, np.int32)
        correct_range = []
        for i in range(N_ATK):
            if atk_reach[i] == 'Short':
                cr = active[i] & (zone[i] == 1)
            elif atk_reach[i] == 'Long':
                cr = active[i] & (zone[i] == 0)
            else:
                cr = active[i]
            correct_range.append(cr)
            n_correct += cr.astype(np.int32)

        # Fibonacci bonus dice per attacker
        fib_d = np.zeros(N, np.int32)
        for k in sorted(FIB_BONUS.keys(), reverse=True):
            fib_d = np.where(n_correct >= k, FIB_BONUS[k], fib_d)

        # Defender splits defence pool across all correct-range attackers
        # Even split; min 1 die per attacker if possible
        def_def_per = np.where(n_correct > 0,
                               np.maximum(1, eD // np.maximum(1, n_correct)),
                               eD)

        # OOB defender: attackers get +2D
        oob_bonus_D = np.where(oobD, 2, 0)

        # ── Phase 1: Zone establishment ─────────────────────────────────────
        # Short attackers at wrong range try to establish distance
        # First Short attacker to succeed collapses zone for others
        # Long attackers at wrong range (Close) don't establish — they fight at penalty

        # Defender offence (if they strike — simplified: always strike if alive)
        # Defender allocates ~50% to offence
        def_off_alloc = np.maximum(1, eD // 2)
        def_def_alloc = eD - def_off_alloc

        def_off_s = np.zeros(N, np.int32)
        if alive_D.any():
            dos = vroll(N, max(1, int(np.median(def_off_alloc[alive_D]))) if alive_D.any() else 4, atnD)
            def_off_s = np.where(alive_D, dos, 0)

        for i in range(N_ATK):
            if atk_reach[i] != 'Short': continue
            needs_close = active[i] & (zone[i] == 0) & ~zone_collapsed
            # Auto-close if zone already collapsed by another attacker
            auto_close  = active[i] & (zone[i] == 0) & zone_collapsed
            zone[i]     = np.where(auto_close, 1, zone[i])

            if needs_close.any():
                # Roll establish distance: TN7 vs defender offence successes
                n_pool = max(1, int(np.median(atk_pools[i])) // 2)
                est_s    = vroll(N, n_pool, 7)
                ob       = def_off_s
                success  = needs_close & (est_s >= ob)
                zone[i]  = np.where(success, 1, zone[i])
                # If this is first closer, collapse zone for others
                zone_collapsed = zone_collapsed | (success & ~zone_collapsed)

        # ── Phase 2: Attack resolution ───────────────────────────────────────
        dmg_to_D  = np.zeros(N, np.float32)
        dmg_to_A  = [np.zeros(N, np.float32) for _ in range(N_ATK)]
        hits_on_D = np.zeros(N, bool)

        for i in range(N_ATK):
            striking = correct_range[i] | (
                (atk_reach[i] == 'Long') & (zone[i] == 1)  # Long at close, penalised
            )
            striking = striking & active[i] & ~oobA[i]
            if not striking.any(): continue

            long_wrong = (atk_reach[i] == 'Long') & (zone[i] == 1) & striking

            # Offence pool with Fibonacci bonus
            off_pool = np.maximum(1, atk_pools[i] // 2).astype(np.int32)
            off_pool = np.where(long_wrong, np.maximum(1, off_pool - 1), off_pool)
            eff_off  = off_pool + fib_d + oob_bonus_D

            # Defender defence for this attacker
            ddef = def_def_per

            atn_i = atk_atn[i]
            a = vroll(N, max(1, int(np.median(eff_off[striking]))) if striking.any() else 4, atn_i)
            d = vroll(N, max(1, int(np.median(ddef[striking]))) if striking.any() else 4,    dtnD)

            # Mass mismatch: attacker Heavy, defender Light → -1 def success
            if atk_wtype[i] in HEAVY_T and WEAPONS[def_weapon][1] in LIGHT_T:
                d = np.maximum(0, d - 1)

            h = striking & (a > d)
            hits_on_D |= h
            excess = np.maximum(0.0, (a-d).astype(float))
            is_crit = h & (excess >= CRIT_THRESH)
            wmod = atk_dmg[i]
            raw  = np.where(is_crit, excess+str_+wmod*2, excess+str_+wmod)
            raw  = np.maximum(0.0, raw - def_dr_vs[i])
            raw  = np.where(h & long_wrong, np.ceil(raw/2), raw)
            dmg_to_D += np.where(h, raw, 0.0)

        # Defender strikes back — picks one attacker at correct range
        # Targets the attacker at correct range with lowest HP (greedy)
        if alive_D.any():
            def_targets = []
            for i in range(N_ATK):
                if defR == 'Short': in_range = (zone[i] == 1)
                elif defR == 'Long': in_range = (zone[i] == 0)
                else: in_range = np.ones(N, bool)
                in_range = in_range & active[i] & ~oobA[i]
                # Long at wrong range can still attack
                long_w = (defR == 'Long') & (zone[i] == 1) & active[i]
                in_range = in_range | long_w
                def_targets.append(in_range)

            # Defender attacks the first available target each sim
            # (simplified: attack attacker 0 if in range, else 1, etc.)
            def_off_eff = def_off_alloc
            for i in range(N_ATK):
                can_target = alive_D & def_targets[i]
                if not can_target.any(): continue

                long_w_def = (defR == 'Long') & (zone[i] == 1)

                aoff = vroll(N, max(1, int(np.median(def_off_eff[can_target]))) if can_target.any() else 4, atnD)
                # Attacker defends with ~half their pool
                atk_def = np.maximum(1, atk_pools[i] // 2).astype(np.int32)
                addef = vroll(N, max(1, int(np.median(atk_def[can_target]))) if can_target.any() else 4, atk_dtn[i])

                # Mismatch: defender Heavy, attacker Light
                if WEAPONS[def_weapon][1] in HEAVY_T and atk_wtype[i] in LIGHT_T:
                    addef = np.maximum(0, addef - 1)

                h = can_target & (aoff > addef)
                excess = np.maximum(0.0, (aoff-addef).astype(float))
                is_crit = h & (excess >= CRIT_THRESH)
                raw = np.where(is_crit, excess+str_+dmgD*2, excess+str_+dmgD)
                raw = np.maximum(0.0, raw - atk_dr[i])
                raw = np.where(h & long_w_def, np.ceil(raw/2), raw)
                dmg_to_A[i] += np.where(h, raw, 0.0)
                # Defender can only attack one per round — break after first target
                break

        # ── Apply damage ─────────────────────────────────────────────────────
        hD -= dmg_to_D
        for i in range(N_ATK):
            hA[i] -= dmg_to_A[i]

        # ── Wound resolution ─────────────────────────────────────────────────
        # Defender
        wD_ = alive_D & (hD <= 0)
        if wD_.any():
            wcD = np.where(wD_, wcD+1, wcD)
            incD = np.where(wD_, wcD >= mw, incD)
            hD   = np.where(wD_ & ~incD, hpD, hD)

        # Attackers
        for i in range(N_ATK):
            wA_ = active[i] & (hA[i] <= 0)
            if wA_.any():
                wcA[i] = np.where(wA_, wcA[i]+1, wcA[i])
                incA[i] = np.where(wA_, wcA[i] >= mw, incA[i])
                hA[i]   = np.where(wA_ & ~incA[i], atk_hp, hA[i])

        # ── Stamina ───────────────────────────────────────────────────────────
        sD = np.where(alive_D, np.maximum(0, sD-1), sD)
        for i in range(N_ATK):
            sA[i] = np.where(active[i], np.maximum(0, sA[i]-1), sA[i])

        # ── Check termination ─────────────────────────────────────────────────
        all_atk_inc = np.all(np.stack(incA, axis=1), axis=1)
        done = any_alive & (incD | all_atk_inc)
        rounds = np.where(done & (rounds == MR), rnd+1, rounds)

    atk_wins    = (incD & ~np.all(np.stack(incA,axis=1),axis=1)).sum() / N
    def_wins    = (~incD & np.any(np.stack([~inc for inc in incA],axis=1),axis=1)).sum() / N
    res         = rounds[rounds < MR]
    return {
        'def_wins':  def_wins,
        'atk_wins':  atk_wins,
        'pDraw':     (rounds == MR).sum() / N,
        'pct_res':   len(res)/N,
        'rounds':    res,
        'med':       float(np.median(res)) if len(res) else 0,
        'mean':      float(np.mean(res))   if len(res) else 0,
        'le10':      float((res<=10).mean()*100) if len(res) else 0,
    }

def report(label, r):
    if r is None: print(f"  {label}: invalid build"); return
    print(f"  {label}")
    print(f"    Def wins:{r['def_wins']*100:5.1f}%  "
          f"Atk wins:{r['atk_wins']*100:5.1f}%  "
          f"Draw:{r['pDraw']*100:4.1f}%  "
          f"Res:{r['pct_res']*100:4.0f}%  "
          f"Med:{r['med']:.0f}  Mean:{r['mean']:.1f}  ≤10:{r['le10']:.0f}%")

N=2000; MR=25; agi=3; str_=3; end=3; hist=2

print("="*72)
print("VALORIA GROUP COMBAT SIMULATION")
print("Variant B (HP=End, armour=DR) | Fibonacci + Zone Collapse")
print(f"STR{str_}/END{end}/AGI{agi}/HIST{hist}  N={N}  MR={MR}")

# ── SECTION 1: Fibonacci bonus effect — same weapon, scale up ────────────────
print(f"\n{'─'*72}")
print("1. FIBONACCI SCALING — Short-LightCut/None vs Long-LightCut/None")
print("   Isolates the numerical advantage across attacker counts")
for n in [1,2,3,5]:
    r = sim_group(
        ['Short-LightCut']*n, ['None']*n,
        'Long-LightCut', 'None',
        agi, str_, end, hist, N, MR
    )
    report(f"  {n}v1", r)

# ── SECTION 2: Heavy weapon defender vs increasing attackers ─────────────────
print(f"\n{'─'*72}")
print("2. HEAVY WEAPON DEFENDER — Long-HeavyBlunt/Heavy vs Short-LightCut/None")
print("   Tests Heavy weapon + armour holding off swarm")
for n in [1,2,3,5]:
    r = sim_group(
        ['Short-LightCut']*n, ['None']*n,
        'Long-HeavyBlunt', 'Heavy',
        agi, str_, end, hist, N, MR
    )
    report(f"  {n}v1", r)

# ── SECTION 3: Mixed attacker weapons vs armoured defender ───────────────────
print(f"\n{'─'*72}")
print("3. MIXED ATTACKERS — various combos vs Long-HeavyBlunt/Heavy")
combos = [
    ([('Short-LightCut','None'),('Short-HeavyBlunt','None')], "2v1: LightCut + HeavyBlunt vs HeavyBlunt/Heavy"),
    ([('Short-LightCut','None')]*2+[('Short-HeavyBlunt','None')], "3v1: 2×LightCut + HeavyBlunt vs HeavyBlunt/Heavy"),
    ([('Short-LightCut','None')]*2+[('Short-HeavyBlunt','Light')], "3v1: 2×LightCut + HeavyBlunt/Light vs HeavyBlunt/Heavy"),
    ([('Short-HeavyBlunt','None')]*3, "3v1: 3×HeavyBlunt vs HeavyBlunt/Heavy"),
    ([('Short-LightCut','Light')]*3, "3v1: 3×LightCut/Light vs HeavyBlunt/Heavy"),
]
for builds, label in combos:
    ws=[b[0] for b in builds]; ars=[b[1] for b in builds]
    r = sim_group(ws, ars, 'Long-HeavyBlunt', 'Heavy', agi, str_, end, hist, N, MR)
    report(f"  {label}", r)

# ── SECTION 4: Zone collapse — Long vs Short at different attacker counts ─────
print(f"\n{'─'*72}")
print("4. ZONE COLLAPSE — Long-HeavyCut/Medium vs Short attackers")
print("   Tests reach advantage holding/failing as numbers increase")
for n in [1,2,3,5]:
    r = sim_group(
        ['Short-LightCut']*n, ['None']*n,
        'Long-HeavyCut', 'Medium',
        agi, str_, end, hist, N, MR
    )
    report(f"  {n}v1 vs Long-HeavyCut/Medium", r)

# ── SECTION 5: Heavy weapon attackers in group ────────────────────────────────
print(f"\n{'─'*72}")
print("5. HEAVY ATTACKER GROUP — HeavyBlunt attackers vs armoured defender")
print("   Tests war hammer swarm — where Heavy weapons should shine")
matchups = [
    (['Short-HeavyBlunt']*2, ['None']*2,  'Short-HeavyCut', 'Heavy',  "2×HvyBlunt/None vs HvyCut/Heavy"),
    (['Short-HeavyBlunt']*3, ['None']*3,  'Short-HeavyCut', 'Heavy',  "3×HvyBlunt/None vs HvyCut/Heavy"),
    (['Short-HeavyBlunt']*2, ['Light']*2, 'Long-HeavyBlunt','Heavy',  "2×HvyBlunt/Light vs HvyBlunt/Heavy"),
    (['Short-HeavyBlunt']*3, ['Light']*3, 'Long-HeavyBlunt','Heavy',  "3×HvyBlunt/Light vs HvyBlunt/Heavy"),
    (['Short-HeavyBlunt']*2, ['None']*2,  'Short-LightCut', 'None',   "2×HvyBlunt vs LightCut/None (unarmoured)"),
    (['Short-HeavyBlunt']*3, ['None']*3,  'Short-LightCut', 'None',   "3×HvyBlunt vs LightCut/None (unarmoured)"),
]
for ws,ars,dw,dar,label in matchups:
    r = sim_group(ws, ars, dw, dar, agi, str_, end, hist, N, MR)
    report(f"  {label}", r)

# ── SECTION 6: 1v1 baseline for comparison ────────────────────────────────────
print(f"\n{'─'*72}")
print("6. 1v1 BASELINES (for comparison)")
baselines = [
    ('Short-LightCut','None',   'Long-LightCut','None',  "LC/None vs LC/None"),
    ('Short-LightCut','None',   'Long-HeavyCut','Medium',"LC/None vs HC/Medium"),
    ('Short-LightCut','None',   'Long-HeavyBlunt','Heavy',"LC/None vs HB/Heavy"),
    ('Short-HeavyBlunt','None', 'Long-HeavyBlunt','Heavy',"HB/None vs HB/Heavy"),
    ('Short-HeavyBlunt','Light','Long-HeavyBlunt','Heavy',"HB/Light vs HB/Heavy"),
]
for aw,aar,dw,dar,label in baselines:
    r = sim_group([aw],[aar],dw,dar,agi,str_,end,hist,N,MR)
    report(f"  {label}", r)

# ── SECTION 7: Defender weapon choice in group combat ────────────────────────
print(f"\n{'─'*72}")
print("7. DEFENDER WEAPON CHOICE — 3v1, attackers Short-LightCut/None")
print("   What weapon/armour gives defender best survival?")
defenders = [
    ('Long-LightCut',   'None',   "Long-LightCut/None"),
    ('Long-LightCut',   'Heavy',  "Long-LightCut/Heavy"),
    ('Long-HeavyCut',   'None',   "Long-HeavyCut/None"),
    ('Long-HeavyCut',   'Heavy',  "Long-HeavyCut/Heavy"),
    ('Long-HeavyBlunt', 'None',   "Long-HeavyBlunt/None"),
    ('Long-HeavyBlunt', 'Heavy',  "Long-HeavyBlunt/Heavy"),
    ('Short-HeavyBlunt','Heavy',  "Short-HeavyBlunt/Heavy"),
    ('Short-LightCut',  'Heavy',  "Short-LightCut/Heavy"),
]
for dw,dar,label in defenders:
    r = sim_group(
        ['Short-LightCut']*3, ['None']*3,
        dw, dar, agi, str_, end, hist, N, MR
    )
    report(f"  {label}", r)

print("\nDone.")
