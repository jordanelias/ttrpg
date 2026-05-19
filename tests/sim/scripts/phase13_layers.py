#!/usr/bin/env python3
# Phase 13 — Intermediating layer test (Layer A Posture / Layer B Advantage Bar / Layer C Stamina-primary)
# Question: which layer compresses within-class dominance closest to 60-70% from 94% baseline?
# Baseline: Phase 10 best-stack (undoubled pool + 1/End Ob wound + Disarm + canonical stam + STR-strong)
# Layers TESTED IN ISOLATION — M1/M2/M3 from C4 not included; layers stand alone vs Phase 10.

import random
import math

# Phase 10 canonical baseline constants
DIE_MEAN_TN7 = 0.4  # [canonical: params/core.md §Expected Value, TN 7]
DIE_STD_TN7 = 0.8  # [canonical: params/core.md §Expected Value, TN 7]
POOL_FLOOR = 1  # [canonical: params/core.md L185-187]
COMBAT_POOL_FLOOR = 5  # [canonical: params/combat.md L14]
ACTION_COST = 5  # [canonical: params/combat.md L15]
TAKE_BREATH_COST = 3  # [canonical: params/combat.md L15 defensive 3]
TAKE_BREATH_TRIGGER = 8  # [canonical: N/A - Phase 8 AI heuristic]
CRIT_MAGNITUDE = 4.0  # [canonical: params/combat.md L91 PP-717 D3]
DISARM_NET_THRESHOLD = 2.0  # [canonical: N/A - Phase 10 proxy]

WEAPONS = {  # [canonical: params/combat.md damage table]
    'light_blade':  {'damage_mod': 3, 'str_mult': 1.0},
    'heavy_weapon': {'damage_mod': 5, 'str_mult': 2.0},
    'unarmed':      {'damage_mod': 0, 'str_mult': 0.5},
}

def str_bonus_dice(strength): return strength // 3  # [canonical: N/A - Phase 10 STR-strong reform]
def stamina_max(end): return end * 5  # [canonical: params/combat.md ED-694]
def stamina_recover(end): return end * 2  # [canonical: params/combat.md ED-694]
def max_wounds(end): return min(end // 2 + 1, 3)  # [canonical: params/combat.md L138]
def wound_interval(end): return end + 6  # [canonical: derived_stats §4.1]
def max_health(end): return wound_interval(end) * (max_wounds(end) + 1)
def wound_net_penalty(wounds, end): return wounds * (1.0 / end)  # [canonical: N/A - Phase 10 1/End Ob reform]
def combat_pool(agi, hist): return max(COMBAT_POOL_FLOOR, agi + hist + 3)  # [canonical: N/A - Phase 10 undoubled]
def stam_cost(action, wounds): return (TAKE_BREATH_COST if action in ('full_guard','take_breath') else ACTION_COST) + wounds

def continuous_roll(n):
    if n <= 0: return 0.0
    return random.gauss(DIE_MEAN_TN7 * n, DIE_STD_TN7 * math.sqrt(n))

# === LAYER A — Posture/Composure track ===
POSTURE_MAX = 3  # [canonical: N/A - Phase 13 Layer A: Steady=0, Pressed=1, Reeling=2, Broken=3]
POSTURE_NET_PER_STEP = 1.0  # [canonical: N/A - Phase 13 Layer A: 1 step per 1.5 net successes]
VULNERABILITY_DAMAGE_MULT = 2.0  # [canonical: N/A - Phase 13 Layer A: Strike vs Vulnerable target × 2 damage]
POSTURE_RECOVERY_PER_BREATH = 1  # [canonical: N/A - Phase 13 Layer A: 1 step recovered per Take Breath]

# === LAYER B — Advantage Position track ===
POSITION_MID = 10  # [canonical: N/A - Phase 13 Layer B: bounded 0-20, mid=10, A wins at 0, B wins at 20]
POSITION_PER_NET = 1.5  # [canonical: N/A - Phase 13 Layer B: position movement per net success]
POSITION_WIN_THRESHOLD = 10  # [canonical: N/A - Phase 13 Layer B: distance from mid for win]

# === LAYER C — Stamina-primary ===
STAM_DRAIN_PER_NET = 2.0  # [canonical: N/A - Phase 13 Layer C: opponent stamina drained per net success]
HP_DAMAGE_THRESHOLD = 3.0  # [canonical: N/A - Phase 13 Layer C: net successes above which direct HP damage fires]
SPENT_DAMAGE_MULT = 2.5  # [canonical: N/A - Phase 13 Layer C: Strike on Spent target × 2.5 damage]

# AI: standard Phase 10 heuristic
def choose_action(my_stam, opp_stam, my_pool, opp_pool, disarmed_opp, rd, layer='none', my_posture=0, my_spent=False, opp_vuln=False, opp_spent=False):
    # Prioritize Strike when opponent is Vulnerable (Layer A) or Spent (Layer C) — decisive moment
    if opp_vuln or opp_spent:
        if my_stam >= ACTION_COST + 1:  # need stam to strike
            return 'strike'
    if my_stam < TAKE_BREATH_TRIGGER:
        return 'take_breath'
    if disarmed_opp:
        return 'strike'
    # Layer A: if my_posture is high, defensive recovery
    if layer == 'A' and my_posture >= 3:  # [canonical: N/A - Phase 13 Layer A AI: Take Breath only at Broken]
        return 'take_breath'
    # Layer C: if I'm Spent, recovery
    if layer == 'C' and my_spent:
        return 'take_breath'
    # Try Feint when pool deficit (Phase 10 pattern)
    if my_pool < opp_pool and rd % 2 == 0:
        return 'feint'
    return 'strike'

def simulate_duel(a, b, layer='none', max_rounds=40):
    """One duel a vs b. layer ∈ {'none', 'A', 'B', 'C'}. Returns 'a', 'b', 'draw'."""
    hp_a = a['max_hp']; hp_b = b['max_hp']
    wounds_a = 0; wounds_b = 0
    stam_a = stamina_max(a['end']); stam_b = stamina_max(b['end'])
    disarmed_a = False; disarmed_b = False
    pending_a = 0; pending_b = 0  # Phase 10 PP-294 Feint reductions

    # Layer A state
    posture_a = 0; posture_b = 0
    vuln_a = False; vuln_b = False  # vulnerable from posture break this round

    # Layer B state
    position = POSITION_MID  # 0=A wins, 20=B wins

    # Layer C state
    spent_a = False; spent_b = False

    for rd in range(max_rounds):
        # Stamina-out checks (universal)
        if stam_a <= 0 and stam_b <= 0: return 'draw'
        if layer != 'C':
            # Layers none, A, B — stamina-out is hard loss
            if stam_a <= 0: return 'b'
            if stam_b <= 0: return 'a'
        else:
            # Layer C — stamina-out triggers Spent, not immediate loss
            spent_a = stam_a <= 0
            spent_b = stam_b <= 0

        # Effective pool with PP-294 pending reductions
        eff_a = max(POOL_FLOOR, a['base_pool'] - pending_a); pending_a = 0
        eff_b = max(POOL_FLOOR, b['base_pool'] - pending_b); pending_b = 0
        off_a = eff_a // 2
        def_a = eff_a - off_a
        off_b = eff_b // 2
        def_b = eff_b - off_b

        action_a = choose_action(stam_a, stam_b, eff_a, eff_b, disarmed_b, rd, layer, posture_a, spent_a, vuln_b, spent_b)
        action_b = choose_action(stam_b, stam_a, eff_b, eff_a, disarmed_a, rd, layer, posture_b, spent_b, vuln_a, spent_a)

        weapon_a = WEAPONS['unarmed'] if disarmed_a else a['weapon']
        weapon_b = WEAPONS['unarmed'] if disarmed_b else b['weapon']

        a_attacks = action_a in ('strike', 'feint', 'disarm')
        b_attacks = action_b in ('strike', 'feint', 'disarm')

        str_a = str_bonus_dice(a['str']) if action_a in ('strike', 'disarm') else 0
        str_b = str_bonus_dice(b['str']) if action_b in ('strike', 'disarm') else 0

        a_net_pen = wound_net_penalty(wounds_a, a['end'])
        b_net_pen = wound_net_penalty(wounds_b, b['end'])

        # Roll
        a_off_hits = continuous_roll(off_a + str_a) if a_attacks else 0
        b_def_hits = continuous_roll(def_b) if b_attacks else 0
        a_net = a_off_hits - b_def_hits - a_net_pen if a_attacks else 0

        b_off_hits = continuous_roll(off_b + str_b) if b_attacks else 0
        a_def_hits = continuous_roll(def_a) if a_attacks else 0
        b_net = b_off_hits - a_def_hits - b_net_pen if b_attacks else 0

        dmg_a, dmg_b = 0, 0

        # === LAYER-SPECIFIC DAMAGE PROCESSING ===

        if layer == 'none':
            # Phase 10 baseline: net → direct HP damage
            if action_a == 'strike' and a_net > 0:
                mod = weapon_a['damage_mod']
                if a_net >= CRIT_MAGNITUDE: mod *= 2
                d = max(0, a_net + a['str'] * weapon_a['str_mult'] + mod)
                dmg_a = d; hp_b -= d
                wounds_b = min(int((b['max_hp'] - hp_b) // wound_interval(b['end'])), b['mw'] + 1)
            if action_b == 'strike' and b_net > 0:
                mod = weapon_b['damage_mod']
                if b_net >= CRIT_MAGNITUDE: mod *= 2
                d = max(0, b_net + b['str'] * weapon_b['str_mult'] + mod)
                dmg_b = d; hp_a -= d
                wounds_a = min(int((a['max_hp'] - hp_a) // wound_interval(a['end'])), a['mw'] + 1)

        elif layer == 'A':
            # Layer A — net → posture damage; HP damage only when target Vulnerable
            if action_a == 'strike' and a_net > 0:
                posture_step = a_net / POSTURE_NET_PER_STEP
                posture_b = min(POSTURE_MAX, posture_b + posture_step)
                if vuln_b:
                    # Strike during Vulnerability — direct HP damage at 2× mod
                    mod = weapon_a['damage_mod'] * VULNERABILITY_DAMAGE_MULT
                    if a_net >= CRIT_MAGNITUDE: mod *= 2
                    d = max(0, a_net + a['str'] * weapon_a['str_mult'] + mod)
                    dmg_a = d; hp_b -= d
                    wounds_b = min(int((b['max_hp'] - hp_b) // wound_interval(b['end'])), b['mw'] + 1)
            if action_b == 'strike' and b_net > 0:
                posture_step = b_net / POSTURE_NET_PER_STEP
                posture_a = min(POSTURE_MAX, posture_a + posture_step)
                if vuln_a:
                    mod = weapon_b['damage_mod'] * VULNERABILITY_DAMAGE_MULT
                    if b_net >= CRIT_MAGNITUDE: mod *= 2
                    d = max(0, b_net + b['str'] * weapon_b['str_mult'] + mod)
                    dmg_b = d; hp_a -= d
                    wounds_a = min(int((a['max_hp'] - hp_a) // wound_interval(a['end'])), a['mw'] + 1)
            # Update Vulnerability state for next round
            vuln_a = posture_a >= POSTURE_MAX
            vuln_b = posture_b >= POSTURE_MAX
            # Reset vulnerable on Take Breath (per spec — posture recovery)
            if action_a == 'take_breath':
                posture_a = max(0, posture_a - POSTURE_RECOVERY_PER_BREATH)
                vuln_a = posture_a >= POSTURE_MAX
            if action_b == 'take_breath':
                posture_b = max(0, posture_b - POSTURE_RECOVERY_PER_BREATH)
                vuln_b = posture_b >= POSTURE_MAX

        elif layer == 'B':
            # Layer B — net → position movement; no HP damage
            # position moves toward 0 if A wins exchange, toward 20 if B wins
            # Layer B: discrete exchange wins — 1 position per round to whoever has higher net  # [canonical: N/A - Phase 13 Layer B Pirates! pattern]
            a_exchange_score = a_net if a_attacks else 0
            b_exchange_score = b_net if b_attacks else 0
            if a_exchange_score > b_exchange_score and a_exchange_score > 0:
                position = max(0, position - 1)
            elif b_exchange_score > a_exchange_score and b_exchange_score > 0:
                position = min(20, position + 1)  # [canonical: N/A - Phase 13 Layer B position cap]
            # Win check on position
            if position <= 0: return 'a'
            if position >= 20: return 'b'  # [canonical: N/A - Phase 13 Layer B win threshold]

        elif layer == 'C':
            # Layer C — net → stamina drain; HP damage only on breakthrough (net >= threshold)
            if action_a == 'strike' and a_net > 0:
                stam_b -= a_net * STAM_DRAIN_PER_NET  # Drain opponent stamina
                if a_net >= HP_DAMAGE_THRESHOLD or spent_b:
                    # Breakthrough OR target is Spent — direct HP damage
                    mod = weapon_a['damage_mod']
                    if spent_b: mod *= SPENT_DAMAGE_MULT
                    if a_net >= CRIT_MAGNITUDE: mod *= 2
                    d = max(0, a_net + a['str'] * weapon_a['str_mult'] + mod)
                    dmg_a = d; hp_b -= d
                    wounds_b = min(int((b['max_hp'] - hp_b) // wound_interval(b['end'])), b['mw'] + 1)
            if action_b == 'strike' and b_net > 0:
                stam_a -= b_net * STAM_DRAIN_PER_NET
                if b_net >= HP_DAMAGE_THRESHOLD or spent_a:
                    mod = weapon_b['damage_mod']
                    if spent_a: mod *= SPENT_DAMAGE_MULT
                    if b_net >= CRIT_MAGNITUDE: mod *= 2
                    d = max(0, b_net + b['str'] * weapon_b['str_mult'] + mod)
                    dmg_b = d; hp_a -= d
                    wounds_a = min(int((a['max_hp'] - hp_a) // wound_interval(a['end'])), a['mw'] + 1)

        # Common: Feint pending reductions (Phase 10 baseline)
        if action_a == 'feint' and a_net > 0:
            pending_b = max(pending_b, int(a_net))
        if action_b == 'feint' and b_net > 0:
            pending_a = max(pending_a, int(b_net))
        if action_a == 'disarm' and a_net >= DISARM_NET_THRESHOLD: disarmed_b = True
        if action_b == 'disarm' and b_net >= DISARM_NET_THRESHOLD: disarmed_a = True

        # Stamina updates
        if action_a == 'take_breath':
            stam_a = min(stamina_max(a['end']), stam_a + stamina_recover(a['end']) - TAKE_BREATH_COST)
        else:
            stam_a -= stam_cost(action_a, wounds_a)
        if action_b == 'take_breath':
            stam_b = min(stamina_max(b['end']), stam_b + stamina_recover(b['end']) - TAKE_BREATH_COST)
        else:
            stam_b -= stam_cost(action_b, wounds_b)

        # HP / wound win checks (layers none, A, C)
        if hp_a <= 0 or wounds_a > a['mw']:
            if hp_b <= 0 or wounds_b > b['mw']: return 'draw'
            return 'b'
        if hp_b <= 0 or wounds_b > b['mw']: return 'a'

    # Max rounds reached
    if layer == 'B':
        # Layer B: judge by position
        if position < POSITION_MID - 2: return 'a'
        if position > POSITION_MID + 2: return 'b'
        return 'draw'
    # Other layers: judge by HP delta
    if hp_a > hp_b * 1.1: return 'a'
    if hp_b > hp_a * 1.1: return 'b'
    return 'draw'

def build(name, agi, end, strength, weapon='light_blade', hist=2):
    return {'name': name, 'agi': agi, 'end': end, 'str': strength,
            'weapon': WEAPONS[weapon], 'hist': hist,
            'base_pool': combat_pool(agi, hist),
            'wi': wound_interval(end), 'mw': max_wounds(end), 'max_hp': max_health(end)}

def run(a, b, layer, n=2000):  # [canonical: N/A - Phase 13 trial count]
    wa = wb = dr = 0
    for _ in range(n):
        r = simulate_duel(a, b, layer=layer)
        if r == 'a': wa += 1
        elif r == 'b': wb += 1
        else: dr += 1
    decisive = wa + wb
    cond = (wa / decisive) if decisive > 0 else 0.5
    return wa/n, cond, dr/n

def main():
    print("=" * 92)  # [canonical: N/A - display width]  # [canonical: N/A - display width]
    print("Phase 13 — Intermediating layer test (A Posture / B Advantage Bar / C Stamina-primary)")
    print("Baseline: Phase 10 (undoubled pool + 1/End Ob + Disarm + canon stam + STR-strong)")
    print("Each layer tested in isolation; M1/M2/M3 not included.")
    print("=" * 92)  # [canonical: N/A - display width]

    matchups = [
        ('Calibration: Strong vs Strong',
            lambda: build('S1', 3, 4, 4, 'light_blade'),
            lambda: build('S2', 3, 4, 4, 'light_blade')),
        ('Calibration: Fast vs Fast',
            lambda: build('F1', 6, 4, 4, 'light_blade'),
            lambda: build('F2', 6, 4, 4, 'light_blade')),
        ('Fast (Agi6 light) vs Strong (Agi3 light) [within-class Agi gap]',
            lambda: build('Fast', 6, 4, 4, 'light_blade'),
            lambda: build('Strong', 3, 4, 4, 'light_blade')),
        ('Fast (Agi6 light) vs Tough (Agi3 End6 light) [End-investment within class]',
            lambda: build('Fast', 6, 4, 4, 'light_blade'),
            lambda: build('Tough', 3, 6, 4, 'light_blade')),
        ('Fast (Agi6 light) vs Mighty-light (Agi3 STR7 light) [F3 gap]',
            lambda: build('Fast', 6, 4, 4, 'light_blade'),
            lambda: build('Mighty-l', 3, 4, 7, 'light_blade')),  # [canonical: N/A - Phase 10 archetype STR=7 F3 gap]
        ('Fast (Agi6 light) vs Titan (Agi3 End6 STR7 heavy) [cross-class]',
            lambda: build('Fast', 6, 4, 4, 'light_blade'),
            lambda: build('Titan', 3, 6, 7, 'heavy_weapon')),  # [canonical: N/A - Phase 10 archetype STR=7 max specialization]
        ('Balanced (Agi5 STR5 light) vs Fast (Agi6 light) [balanced build]',
            lambda: build('Bal', 5, 4, 5, 'light_blade'),
            lambda: build('Fast', 6, 4, 4, 'light_blade')),
    ]

    layers = ['none', 'A', 'B', 'C']
    headers = ['Matchup'] + [f'{L}: A%' for L in layers]
    print(f"\n{'Matchup':<68} " + " ".join(f"{h:>9}" for h in [f'none' , f'A_post', f'B_pos', f'C_stam']))
    print("-" * 110)  # [canonical: N/A - display width]

    for label, a_fn, b_fn in matchups:
        results = []
        for L in layers:
            random.seed(42)
            a = a_fn(); b = b_fn()
            wa, cond, draw = run(a, b, L)
            results.append(wa * 100)
        print(f"{label:<68} " + " ".join(f"{r:>8.1f}%" for r in results))

    print()
    print("Reading: A% = A's win rate. Calibration matchups should be ~50%. Within-class Agi gap")
    print("under Phase 10 baseline (layer 'none') is ~94% Fast. Each layer should compress this.")
    print("Target: 60-70% Fast in within-class Agi gap = scaling-defect addressed.")

if __name__ == '__main__':
    main()
