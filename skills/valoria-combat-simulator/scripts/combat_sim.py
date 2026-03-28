#!/usr/bin/env python3
"""
Valoria Combat Simulator
Canonical script — parameters sourced from references/combat_params.md
Update CONFIG block when ruleset patches land. Do not hardcode elsewhere.
"""

import math, random, argparse, sys
from collections import defaultdict

# ── CONFIG — update when ruleset patches land ─────────────────────────────────
WEAPONS = {
    # name: (reach, weight, atk_tn, parry_tn, dmg_bonus)
    'Short-Light':  ('Short',     'Light',  5, 6, 1),
    'Short-Medium': ('Short',     'Medium', 6, 7, 2),
    'Short-Heavy':  ('Short',     'Heavy',  7, 8, 3),
    'Long-Light':   ('Long',      'Light',  5, 6, 1),
    'Long-Medium':  ('Long',      'Medium', 6, 7, 2),
    'Long-Heavy':   ('Long',      'Heavy',  7, 8, 3),
    'Vers-Light':   ('Versatile', 'Light',  5, 6, 1),
    'Vers-Medium':  ('Versatile', 'Medium', 6, 7, 2),
    'Vers-Heavy':   ('Versatile', 'Heavy',  7, 8, 3),
}

STR_MIN_WEAPON = {'Light': 0, 'Medium': 3, 'Heavy': 4}

# armour: (DR, str_min, pool_penalty_at_one_below, stamina_formula)
# stamina_formula: 1=End+1, 0=End, -1=End-1
ARMOURS = {
    'None':   (0, 0, 0,  1),
    'Light':  (1, 2, 1,  1),
    'Medium': (2, 3, 1,  0),
    'Heavy':  (3, 4, 2, -1),  # NOTE: Heavy = -2D penalty, not -1D
}

PROFICIENCY_POINTS = {'untrained': 0, 'beginner': 1, 'competent': 2, 'veteran': 3}

MANOEUVRE_TN = 7
DEFAULT_N_FIGHTS = 20000
DEFAULT_MAX_ROUNDS = 30
# ─────────────────────────────────────────────────────────────────────────────


def get_stamina_max(ar, end):
    _, _, _, stam_mod = ARMOURS[ar]
    return max(1, end + stam_mod + (1 if stam_mod == 1 else 0) if stam_mod == 1 else end + stam_mod)

def stamina_max(ar, end):
    _, _, _, mod = ARMOURS[ar]
    # mod: 1 = End+1, 0 = End, -1 = End-1
    return max(1, end + mod)

def build_pool(w, ar, agi, str_, proficiency):
    _, wt, _, _, _ = WEAPONS[w]
    _, ar_str, ar_pen, _ = ARMOURS[ar]
    points = PROFICIENCY_POINTS[proficiency]
    base = agi + (points + 3)

    pool = base
    dw = STR_MIN_WEAPON[wt] - str_
    if dw >= 2:   return None          # cannot wield
    elif dw == 1: pool -= 1            # -1D

    da = ar_str - str_
    if da >= 2:   return None          # cannot wear
    elif da == 1: pool -= ar_pen       # -1D or -2D depending on armour

    return max(1, pool)

def roll(n, tn):
    if n <= 0: return 0
    return sum(1 for _ in range(n) if random.randint(1, 10) >= tn)

def at_correct_range(reach, band):
    if reach == 'Versatile': return True
    return reach == band

def preferred_range(reach):
    if reach == 'Short': return 'Short'
    return 'Long'  # Long and Versatile prefer Long (Versatile has no locked preference but defaults Long)

def simulate_fight(wA, arA, wB, arB, agi, str_, end, proficiency, n_fights, max_rounds):
    rA, _, atnA, ptnA, dmgA = WEAPONS[wA]
    rB, _, atnB, ptnB, dmgB = WEAPONS[wB]
    drA = ARMOURS[arA][0]
    drB = ARMOURS[arB][0]

    poolA = build_pool(wA, arA, agi, str_, proficiency)
    poolB = build_pool(wB, arB, agi, str_, proficiency)
    if poolA is None or poolB is None:
        return None

    health = end + 6
    stamA_max = stamina_max(arA, end)
    stamB_max = stamina_max(arB, end)

    wins_A = wins_B = draws = 0

    for _ in range(n_fights):
        hpA = hpB = health
        stamA = stamA_max
        stamB = stamB_max
        range_band = 'Long'

        for rnd in range(max_rounds):
            if hpA <= 0 or hpB <= 0:
                break

            # Catch Breath check
            catchA = stamA <= 0
            catchB = stamB <= 0
            if catchA: stamA = stamA_max
            if catchB: stamB = stamB_max

            effA = math.ceil(poolA / 2) if catchA else poolA
            effB = math.ceil(poolB / 2) if catchB else poolB
            can_A = not catchA
            can_B = not catchB

            # Range state
            A_ok = at_correct_range(rA, range_band)
            B_ok = at_correct_range(rB, range_band)
            A_wants = can_A and not A_ok
            B_wants = can_B and not B_ok

            A_attacks = B_attacks = False

            if A_wants or B_wants:
                initiator = 'A' if A_wants else 'B'
                if can_A and can_B:
                    sA = roll(agi, MANOEUVRE_TN)
                    sB = roll(agi, MANOEUVRE_TN)
                    if sA > sB:   winner = 'A'
                    elif sB > sA: winner = 'B'
                    else:         winner = 'Long_holds'

                    init_pref = preferred_range(rA if initiator == 'A' else rB)
                    if winner == initiator:
                        range_band = init_pref
                    # neither attacks — both used offensive action
                    stamA -= 1
                    stamB -= 1
                elif can_A and not can_B:
                    if initiator == 'A':
                        range_band = preferred_range(rA)
                    stamA -= 1
                elif can_B and not can_A:
                    if initiator == 'B':
                        range_band = preferred_range(rB)
                    stamB -= 1
            else:
                A_attacks = can_A
                B_attacks = can_B

            if A_attacks:
                pen = 1 if rA == 'Versatile' else 0
                off = max(1, effA // 2 - pen)
                defn_B = effB - (effB // 2)
                atk = roll(off, atnA)
                dfn = roll(defn_B, ptnB)
                if atk > dfn:
                    hpB -= max(0, dmgA + (atk - dfn) - drB)
                stamA -= 1

            if B_attacks:
                pen = 1 if rB == 'Versatile' else 0
                off = max(1, effB // 2 - pen)
                defn_A = effA - (effA // 2)
                atk = roll(off, atnB)
                dfn = roll(defn_A, ptnA)
                if atk > dfn:
                    hpA -= max(0, dmgB + (atk - dfn) - drA)
                stamB -= 1

            stamA = max(0, stamA)
            stamB = max(0, stamB)

        if hpA > 0 and hpB <= 0:    wins_A += 1
        elif hpB > 0 and hpA <= 0:  wins_B += 1
        else:                        draws += 1

    return wins_A / n_fights, wins_B / n_fights, draws / n_fights


def main():
    parser = argparse.ArgumentParser(description='Valoria Combat Simulator')
    parser.add_argument('--str', type=int, default=3, dest='str_')
    parser.add_argument('--end', type=int, default=3)
    parser.add_argument('--agi', type=int, default=3)
    parser.add_argument('--proficiency', default='competent',
                        choices=list(PROFICIENCY_POINTS.keys()))
    parser.add_argument('--n-fights', type=int, default=DEFAULT_N_FIGHTS)
    parser.add_argument('--max-rounds', type=int, default=DEFAULT_MAX_ROUNDS)
    parser.add_argument('--run-label', default='Run-?')
    parser.add_argument('--output', default=None)
    args = parser.parse_args()

    random.seed(42)
    str_ = args.str_; end = args.end; agi = args.agi
    prof = args.proficiency
    pool_base = agi + (PROFICIENCY_POINTS[prof] + 3)
    health = end + 6

    print(f"Valoria Combat Simulator — {args.run_label}")
    print(f"Str {str_} / End {end} / Agi {agi} / {prof.capitalize()} / "
          f"Base Pool {pool_base} / Health {health}")
    print(f"Stamina: None/Light={stamina_max('None',end)}, "
          f"Medium={stamina_max('Medium',end)}, Heavy={stamina_max('Heavy',end)}")
    print(f"N={args.n_fights} fights, max {args.max_rounds} rounds\n")

    valid = [(w, ar) for w in WEAPONS for ar in ARMOURS
             if build_pool(w, ar, agi, str_, prof) is not None]
    print(f"Valid builds: {len(valid)}")

    results = []; seen = set()
    for (wA, arA) in valid:
        for (wB, arB) in valid:
            key = tuple(sorted([(wA,arA),(wB,arB)]))
            if key in seen: continue
            seen.add(key)
            r = simulate_fight(wA, arA, wB, arB, agi, str_, end, prof,
                               args.n_fights, args.max_rounds)
            if r:
                pW, pL, pD = r
                results.append((wA, arA, wB, arB, pW, pL, pD))

    print(f"Matchups computed: {len(results)}\n")

    header = (f"{'Weapon A':<16}{'Armour A':<9}{'Weapon B':<16}"
              f"{'Armour B':<9}{'A Win%':>7}{'B Win%':>7}{'Draw%':>7}")
    divider = "-" * len(header)
    lines = [header, divider]
    for row in sorted(results, key=lambda x: -x[4]):
        wA,arA,wB,arB,pW,pL,pD = row
        lines.append(f"{wA:<16}{arA:<9}{wB:<16}{arB:<9}"
                     f"{pW*100:>6.1f}%{pL*100:>6.1f}%{pD*100:>6.1f}%")

    # Build summary
    win_rates = {}
    for wA,arA,wB,arB,pW,pL,pD in results:
        win_rates.setdefault((wA,arA),[]).append(pW)
        win_rates.setdefault((wB,arB),[]).append(pL)
    avgs = sorted([(b, sum(v)/len(v)) for b,v in win_rates.items()],
                  key=lambda x: -x[1])

    summary = ["\n── TOP / BOTTOM BUILDS ──────────────────────────────────────",
               "\nTop 10:"]
    for b, avg in avgs[:10]:
        summary.append(f"  {b[0]:<16} {b[1]:<8}  {avg*100:.1f}%")
    summary.append("\nBottom 10:")
    for b, avg in avgs[-10:]:
        summary.append(f"  {b[0]:<16} {b[1]:<8}  {avg*100:.1f}%")

    flags = ["\n── BALANCE FLAGS (>80% non-mirror) ─────────────────────────"]
    for wA,arA,wB,arB,pW,pL,pD in results:
        if pW > 0.80 and (wA,arA) != (wB,arB):
            flags.append(f"  {wA}/{arA} vs {wB}/{arB}: {pW*100:.0f}%")

    output = "\n".join(lines + summary + flags)
    print(output)

    if args.output:
        with open(args.output, 'w') as f:
            f.write(f"# Combat Simulation — {args.run_label}\n\n")
            f.write(f"**Str {str_} / End {end} / Agi {agi} / {prof.capitalize()} / "
                    f"Pool {pool_base} / Health {health}**\n\n")
            f.write(output)
        print(f"\nResults written to {args.output}")

if __name__ == '__main__':
    main()
