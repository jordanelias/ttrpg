#!/usr/bin/env python3
"""
Valoria Combat Simulator
Canonical script — parameters sourced from references/combat_params.md
Update CONFIG block when ruleset patches land. Do not hardcode elsewhere.
Last updated: 2026-03-31 — stage8_combat.md sync
"""

import math, random, argparse, sys
from collections import defaultdict

# ── CONFIG — update when ruleset patches land ─────────────────────────────────

# Weapons: name → (reach, cut_or_blunt, atk_tn, def_tn, dmg_bonus)
# cut_or_blunt: 'Cut' or 'Blunt' — used to look up per-type DR
WEAPONS = {
    # Short reach
    'Short-LightCut':   ('Short',      'LightCut',   5, 6, 1),
    'Short-HeavyCut':   ('Short',      'HeavyCut',   6, 7, 4),
    'Short-LightBlunt': ('Short',      'LightBlunt', 6, 7, 1),
    'Short-HeavyBlunt': ('Short',      'HeavyBlunt', 7, 8, 4),
    # Long reach
    'Long-LightCut':    ('Long',       'LightCut',   5, 6, 1),
    'Long-HeavyCut':    ('Long',       'HeavyCut',   6, 7, 4),
    'Long-LightBlunt':  ('Long',       'LightBlunt', 6, 7, 1),
    'Long-HeavyBlunt':  ('Long',       'HeavyBlunt', 7, 8, 4),
    # Unarmed
    'Unarmed':          ('Short',      'Unarmed',    8, 9, 0),
}

# Str minimums per weapon weight class
STR_MIN_WEAPON = {
    'LightCut': 1, 'LightBlunt': 1,
    'HeavyCut': 3, 'HeavyBlunt': 4,
    'Unarmed':  0,
}

# DR per armour tier, keyed by weapon type
# armour → {weapon_type → DR}
ARMOUR_DR = {
    'None':   {'LightCut': 0, 'HeavyCut': 0, 'LightBlunt': 0, 'HeavyBlunt': 0, 'Unarmed': 0},
    'Light':  {'LightCut': 2, 'HeavyCut': 1, 'LightBlunt': 1, 'HeavyBlunt': 0, 'Unarmed': 0},
    'Medium': {'LightCut': 4, 'HeavyCut': 3, 'LightBlunt': 2, 'HeavyBlunt': 1, 'Unarmed': 0},
    'Heavy':  {'LightCut': 6, 'HeavyCut': 5, 'LightBlunt': 3, 'HeavyBlunt': 1, 'Unarmed': 0},
}

# armour → (str_min, pool_penalty_at_one_below, stamina_mod)
# pool_penalty: dice subtracted if 1 below str_min (2+ = cannot wear)
# stamina_mod: added to (End + History + 1)
ARMOURS = {
    'None':   (0, 0,  0),
    'Light':  (2, 1,  0),
    'Medium': (3, 1, -1),
    'Heavy':  (4, 2, -2),
}

PROFICIENCY_POINTS = {'untrained': 0, 'beginner': 1, 'competent': 2, 'veteran': 3}

MANOEUVRE_TN    = 7
DEFAULT_N_FIGHTS  = 20000
DEFAULT_MAX_ROUNDS = 30
CRIT_THRESHOLD  = 3  # excess successes ≥ this → double weapon modifier
# ─────────────────────────────────────────────────────────────────────────────


def stamina_max(ar, end, history_points):
    _, _, stam_mod = ARMOURS[ar]
    return max(1, end + history_points + 1 + stam_mod)


def build_pool(w, ar, agi, str_, proficiency):
    """Return effective combat pool, or None if build is invalid."""
    reach, wtype, _, _, _ = WEAPONS[w]
    ar_str, ar_pen, _ = ARMOURS[ar]
    points = PROFICIENCY_POINTS[proficiency]

    base = (agi * 2) + points + 3
    pool = base

    # Weapon str check
    dw = STR_MIN_WEAPON[wtype] - str_
    if dw >= 2:   return None
    elif dw == 1: pool -= 1

    # Armour str check
    da = ar_str - str_
    if da >= 2:   return None
    elif da == 1: pool -= ar_pen

    return max(5, pool)  # minimum pool 5 per §8.1


def roll(n, tn):
    if n <= 0: return 0
    return sum(1 for _ in range(n) if random.randint(1, 10) >= tn)


def at_correct_range(reach, band):
    """Short = needs Close; Long = prefers Far but can fight at Close degraded."""
    if reach == 'Short': return band == 'Close'
    if reach == 'Long':  return True   # can always act (degraded at Close)
    return True


def simulate_fight(wA, arA, wB, arB, agi, str_, end, proficiency, n_fights, max_rounds):
    rA, wtA, atnA, dtnA, dmgA = WEAPONS[wA]
    rB, wtB, atnB, dtnB, dmgB = WEAPONS[wB]

    points = PROFICIENCY_POINTS[proficiency]
    poolA_base = build_pool(wA, arA, agi, str_, proficiency)
    poolB_base = build_pool(wB, arB, agi, str_, proficiency)
    if poolA_base is None or poolB_base is None:
        return None

    health     = end + 6
    stamA_max_ = stamina_max(arA, end, points)
    stamB_max_ = stamina_max(arB, end, points)

    drA_vs = ARMOUR_DR[arA]  # DR dict for armour A, keyed by weapon type
    drB_vs = ARMOUR_DR[arB]

    wins_A = wins_B = draws = 0

    for _ in range(n_fights):
        hpA = hpB = health
        woundsA = woundsB = 0
        stamA = stamA_max_
        stamB = stamB_max_
        range_band = 'Far'  # default engagement opening

        for rnd in range(max_rounds):
            if hpA <= 0 or hpB <= 0:
                break

            # Out of Breath check
            oobA = stamA <= 0
            oobB = stamB <= 0
            if oobA: stamA = stamA_max_
            if oobB: stamB = stamB_max_

            # Apply wound pool penalties
            poolA = max(1, poolA_base - woundsA)
            poolB = max(1, poolB_base - woundsB)

            effA = math.ceil(poolA / 2) if oobA else poolA
            effB = math.ceil(poolB / 2) if oobB else poolB
            can_A = not oobA
            can_B = not oobB

            # Range management
            A_needs_close = (rA == 'Short' and range_band == 'Far')
            B_needs_close = (rB == 'Short' and range_band == 'Far')
            A_wants_far   = (rA == 'Long'  and range_band == 'Close')  # prefers Far but can still act
            B_wants_far   = (rB == 'Long'  and range_band == 'Close')

            A_manoeuvres = can_A and A_needs_close
            B_manoeuvres = can_B and B_needs_close

            A_attacks = B_attacks = False

            if A_manoeuvres or B_manoeuvres:
                # Establish Distance contest
                if can_A and can_B:
                    sA = roll(effA // 2, MANOEUVRE_TN)
                    sB = roll(effB // 2, MANOEUVRE_TN)
                    if sA > sB:   range_band = 'Close' if A_manoeuvres else 'Far'
                    elif sB > sA: range_band = 'Close' if B_manoeuvres else 'Far'
                    else:         pass  # tie → Long holds (Far unchanged)
                    stamA -= 1; stamB -= 1
                elif can_A:
                    range_band = 'Close' if A_manoeuvres else range_band
                    stamA -= 1
                elif can_B:
                    range_band = 'Close' if B_manoeuvres else range_band
                    stamB -= 1
            else:
                A_attacks = can_A
                B_attacks = can_B

            def resolve_attack(attacker_pool, oob, reach, atk_tn, def_tn, dmg_bonus,
                               defender_pool, def_oob, dr_dict, wtype, band):
                """Returns damage dealt to defender."""
                if oob: return 0  # Out of Breath: defence only

                # Long at Close zone: -1D offence, half damage
                close_penalty = (reach == 'Long' and band == 'Close')
                off_pool = max(1, attacker_pool // 2 - (1 if close_penalty else 0))
                def_pool = max(1, defender_pool - defender_pool // 2)

                atk = roll(off_pool, atk_tn)
                dfn = roll(def_pool, def_tn)

                if atk <= dfn:
                    return 0

                excess = atk - dfn
                modifier = dmg_bonus * 2 if excess >= CRIT_THRESHOLD else dmg_bonus
                dr = dr_dict.get(wtype, 0)

                raw = excess + str_ + modifier - dr
                if close_penalty:
                    raw = math.ceil(raw / 2)
                return max(0, raw)

            dmg_to_B = dmg_to_A = 0
            if A_attacks:
                dmg_to_B = resolve_attack(effA, oobA, rA, atnA, dtnA, dmgA,
                                          effB, oobB, drB_vs, wtA, range_band)
                stamA -= 1
            if B_attacks:
                dmg_to_A = resolve_attack(effB, oobB, rB, atnB, dtnB, dmgB,
                                          effA, oobA, drA_vs, wtB, range_band)
                stamB -= 1

            # Apply damage simultaneously; check wounds
            hpA -= dmg_to_A
            hpB -= dmg_to_B

            while hpA <= 0 and woundsA < _incap_threshold(end):
                woundsA += 1
                hpA += health  # reset
            while hpB <= 0 and woundsB < _incap_threshold(end):
                woundsB += 1
                hpB += health

            stamA = max(0, stamA)
            stamB = max(0, stamB)

        # Determine fight outcome
        A_incap = hpA <= 0 or woundsA >= _incap_threshold(end)
        B_incap = hpB <= 0 or woundsB >= _incap_threshold(end)

        if not A_incap and B_incap:  wins_A += 1
        elif not B_incap and A_incap: wins_B += 1
        else:                         draws += 1

    return wins_A / n_fights, wins_B / n_fights, draws / n_fights


def _incap_threshold(end):
    if end <= 3: return 2
    if end <= 5: return 3
    return 4


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
    points = PROFICIENCY_POINTS[prof]
    pool_base = (agi * 2) + points + 3
    health = end + 6

    print(f"Valoria Combat Simulator — {args.run_label}")
    print(f"Str {str_} / End {end} / Agi {agi} / {prof.capitalize()} / "
          f"Base Pool {pool_base} / Health {health}")
    print(f"Stamina: None={stamina_max('None',end,points)}, "
          f"Light={stamina_max('Light',end,points)}, "
          f"Medium={stamina_max('Medium',end,points)}, "
          f"Heavy={stamina_max('Heavy',end,points)}")
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

    header = (f"{'Weapon A':<20}{'Armour A':<9}{'Weapon B':<20}"
              f"{'Armour B':<9}{'A Win%':>7}{'B Win%':>7}{'Draw%':>7}")
    divider = "-" * len(header)
    lines = [header, divider]
    for row in sorted(results, key=lambda x: -x[4]):
        wA,arA,wB,arB,pW,pL,pD = row
        lines.append(f"{wA:<20}{arA:<9}{wB:<20}{arB:<9}"
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
        summary.append(f"  {b[0]:<20} {b[1]:<8}  {avg*100:.1f}%")
    summary.append("\nBottom 10:")
    for b, avg in avgs[-10:]:
        summary.append(f"  {b[0]:<20} {b[1]:<8}  {avg*100:.1f}%")

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
