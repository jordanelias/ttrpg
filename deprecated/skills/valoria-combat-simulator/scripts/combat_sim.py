#!/usr/bin/env python3
"""
Valoria Combat Simulator
Canonical script — parameters sourced from references/combat_params.md
Update CONFIG block when ruleset patches land. Do not hardcode elsewhere.
Last updated: 2026-03-31 — Establish Distance uses Defence dice at TN7;
             Long weapon AI attempts Establish Distance at Close unless
             opponent is one strike from incapacitation or fighter is in Full Guard.
"""

import math, random, argparse, sys
from collections import defaultdict

# ── CONFIG — update when ruleset patches land ─────────────────────────────────

WEAPONS = {
    'Short-LightCut':   ('Short', 'LightCut',   5, 6, 1),
    'Short-HeavyCut':   ('Short', 'HeavyCut',   6, 7, 4),
    'Short-LightBlunt': ('Short', 'LightBlunt', 6, 7, 1),
    'Short-HeavyBlunt': ('Short', 'HeavyBlunt', 7, 8, 4),
    'Long-LightCut':    ('Long',  'LightCut',   5, 6, 1),
    'Long-HeavyCut':    ('Long',  'HeavyCut',   6, 7, 4),
    'Long-LightBlunt':  ('Long',  'LightBlunt', 6, 7, 1),
    'Long-HeavyBlunt':  ('Long',  'HeavyBlunt', 7, 8, 4),
    'Unarmed':          ('Short', 'Unarmed',    8, 9, 0),
}

STR_MIN_WEAPON = {
    'LightCut': 1, 'LightBlunt': 1,
    'HeavyCut': 3, 'HeavyBlunt': 4,
    'Unarmed':  0,
}

ARMOUR_DR = {
    'None':   {'LightCut': 0, 'HeavyCut': 0, 'LightBlunt': 0, 'HeavyBlunt': 0, 'Unarmed': 0},
    'Light':  {'LightCut': 2, 'HeavyCut': 1, 'LightBlunt': 1, 'HeavyBlunt': 0, 'Unarmed': 0},
    'Medium': {'LightCut': 4, 'HeavyCut': 3, 'LightBlunt': 2, 'HeavyBlunt': 1, 'Unarmed': 0},
    'Heavy':  {'LightCut': 6, 'HeavyCut': 5, 'LightBlunt': 3, 'HeavyBlunt': 1, 'Unarmed': 0},
}

# armour → (str_min, pool_penalty_at_one_below, stamina_mod)
ARMOURS = {
    'None':   (0, 0,  0),
    'Light':  (2, 1,  0),
    'Medium': (3, 1, -1),
    'Heavy':  (4, 2, -2),
}

PROFICIENCY_POINTS = {'untrained': 0, 'beginner': 1, 'competent': 2, 'veteran': 3}

MANOEUVRE_TN     = 7
DEFAULT_N_FIGHTS  = 20000
DEFAULT_MAX_ROUNDS = 30
CRIT_THRESHOLD   = 3
# ─────────────────────────────────────────────────────────────────────────────


def stamina_max(ar, end, history_points):
    _, _, stam_mod = ARMOURS[ar]
    return max(1, end + history_points + 1 + stam_mod)


def build_pool(w, ar, agi, str_, proficiency):
    reach, wtype, _, _, _ = WEAPONS[w]
    ar_str, ar_pen, _ = ARMOURS[ar]
    points = PROFICIENCY_POINTS[proficiency]
    base = (agi * 2) + points + 3
    pool = base

    dw = STR_MIN_WEAPON[wtype] - str_
    if dw >= 2:   return None
    elif dw == 1: pool -= 1

    da = ar_str - str_
    if da >= 2:   return None
    elif da == 1: pool -= ar_pen

    return max(5, pool)


def roll(n, tn):
    if n <= 0: return 0
    return sum(1 for _ in range(n) if random.randint(1, 10) >= tn)


def _incap_threshold(end):
    if end <= 3: return 2
    if end <= 5: return 3
    return 4


def _one_strike_from_incap(hp, wounds, end, opponent_pool, opponent_dmg, opponent_dr):
    """
    True if opponent can plausibly incapacitate this fighter in one hit.
    Conservative estimate: opponent hits with 1 excess success (minimum damage).
    """
    incap_wounds = _incap_threshold(end)
    if wounds >= incap_wounds - 1:
        # Already at last wound — any damage reaching Health 0 incapacitates
        min_damage = max(0, 1 + opponent_dmg - opponent_dr)  # 1 excess + dmg bonus - DR
        return min_damage >= hp
    return False


def simulate_fight(wA, arA, wB, arB, agi, str_, end, proficiency, n_fights, max_rounds):
    rA, wtA, atnA, dtnA, dmgA = WEAPONS[wA]
    rB, wtB, atnB, dtnB, dmgB = WEAPONS[wB]

    points = PROFICIENCY_POINTS[proficiency]
    poolA_base = build_pool(wA, arA, agi, str_, proficiency)
    poolB_base = build_pool(wB, arB, agi, str_, proficiency)
    if poolA_base is None or poolB_base is None:
        return None

    health      = end + 6
    stamA_max_  = stamina_max(arA, end, points)
    stamB_max_  = stamina_max(arB, end, points)
    drA_vs      = ARMOUR_DR[arA]
    drB_vs      = ARMOUR_DR[arB]
    incap_thr   = _incap_threshold(end)

    wins_A = wins_B = draws = 0

    for _ in range(n_fights):
        hpA = hpB = health
        woundsA = woundsB = 0
        stamA = stamA_max_
        stamB = stamB_max_
        range_band = 'Far'
        full_guard_A = full_guard_B = False  # set externally if rescue scenario modelled

        for rnd in range(max_rounds):
            if hpA <= 0 or hpB <= 0:
                break

            # Out of Breath
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

            # Defence dice = pool - offence allocation (pool - pool//2)
            defA = effA - effA // 2
            defB = effB - effB // 2

            # ── Long weapon AI: attempt Establish Distance at Close zone
            #    UNLESS: opponent one strike from incap, OR fighter in Full Guard
            def long_wants_far(reach, band, hp_self, wounds_self,
                               hp_opp, wounds_opp,
                               opp_pool, opp_dmg, opp_dr, full_guard):
                if reach != 'Long' or band != 'Close':
                    return False
                if full_guard:
                    return False
                if _one_strike_from_incap(hp_opp, wounds_opp, end, opp_pool, opp_dmg, opp_dr):
                    return False  # opponent near-dead: press the attack
                return True

            A_needs_close  = (rA == 'Short' and range_band == 'Far')
            B_needs_close  = (rB == 'Short' and range_band == 'Far')
            A_wants_far    = long_wants_far(rA, range_band, hpA, woundsA,
                                            hpB, woundsB, poolB, dmgB,
                                            drA_vs.get(wtB, 0), full_guard_A)
            B_wants_far    = long_wants_far(rB, range_band, hpB, woundsB,
                                            hpA, woundsA, poolA, dmgA,
                                            drB_vs.get(wtA, 0), full_guard_B)

            A_manoeuvres = can_A and (A_needs_close or A_wants_far)
            B_manoeuvres = can_B and (B_needs_close or B_wants_far)

            A_attacks = B_attacks = False

            if A_manoeuvres or B_manoeuvres:
                # Establish Distance: roll Defence dice at TN 7
                if can_A and can_B:
                    sA = roll(defA, MANOEUVRE_TN)
                    sB = roll(defB, MANOEUVRE_TN)

                    # Determine who wins: each pushes toward their preferred range
                    # If both manoeuvre, treat as contested — higher successes wins
                    # Tie → Long holds (Far)
                    if A_manoeuvres and B_manoeuvres:
                        # Both contesting range — Long fighter wins ties
                        a_wants = 'Close' if A_needs_close else 'Far'
                        b_wants = 'Close' if B_needs_close else 'Far'
                        if sA > sB:   range_band = a_wants
                        elif sB > sA: range_band = b_wants
                        else:         range_band = 'Far'  # tie → Long holds
                    elif A_manoeuvres:
                        # A manoeuvres; B may contest (rational: always contest)
                        a_wants = 'Close' if A_needs_close else 'Far'
                        if sA > sB:   range_band = a_wants
                        elif sB > sA: pass  # B wins, range unchanged
                        else:         range_band = 'Far'  # tie → Long holds
                    else:
                        # B manoeuvres; A contests
                        b_wants = 'Close' if B_needs_close else 'Far'
                        if sB > sA:   range_band = b_wants
                        elif sA > sB: pass
                        else:         range_band = 'Far'

                    stamA -= 1; stamB -= 1

                elif can_A and not can_B:
                    if A_manoeuvres:
                        range_band = 'Close' if A_needs_close else 'Far'
                    stamA -= 1
                elif can_B and not can_A:
                    if B_manoeuvres:
                        range_band = 'Close' if B_needs_close else 'Far'
                    stamB -= 1
            else:
                A_attacks = can_A
                B_attacks = can_B

            def resolve_attack(attacker_pool, oob, reach, atk_tn, def_tn, dmg_bonus,
                               defender_pool, def_oob, dr_dict, wtype, band):
                if oob: return 0

                close_penalty = (reach == 'Long' and band == 'Close')
                off_pool = max(1, attacker_pool // 2 - (1 if close_penalty else 0))
                def_pool = max(1, defender_pool - defender_pool // 2)

                atk = roll(off_pool, atk_tn)
                dfn = roll(def_pool, def_tn)

                if atk <= dfn:
                    return 0

                excess   = atk - dfn
                modifier = dmg_bonus * 2 if excess >= CRIT_THRESHOLD else dmg_bonus
                dr       = dr_dict.get(wtype, 0)
                raw      = excess + str_ + modifier - dr
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

            hpA -= dmg_to_A
            hpB -= dmg_to_B

            while hpA <= 0 and woundsA < incap_thr:
                woundsA += 1
                hpA += health
            while hpB <= 0 and woundsB < incap_thr:
                woundsB += 1
                hpB += health

            stamA = max(0, stamA)
            stamB = max(0, stamB)

        A_incap = hpA <= 0 or woundsA >= incap_thr
        B_incap = hpB <= 0 or woundsB >= incap_thr

        if not A_incap and B_incap:   wins_A += 1
        elif not B_incap and A_incap: wins_B += 1
        else:                          draws  += 1

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
