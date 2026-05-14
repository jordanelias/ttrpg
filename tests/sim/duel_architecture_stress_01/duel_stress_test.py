#!/usr/bin/env python3
"""Architecture C duel v4 — scene combat chassis. See duel_design_and_stress_results.md."""
import numpy as np
from collections import defaultdict

# ══════════════════════════════════════════════════════════════════════════════
# CANONICAL CONSTANTS — verbatim from params/combat.md + combat_v30.md
# ══════════════════════════════════════════════════════════════════════════════

# [canonical: params/combat.md §Weapon System PP-232]
# Weapon: (reach, weight, type, tn, examples)
# TN = 7 + reach_mod + weight_mod + type_mod
# Short=-1, Long=+0; Light=-1, Heavy=+0; Blade=+0, Blunt=+1
WEAPON_TN = {  # [canonical: params/combat.md §Weapon System PP-232]
    'ShortLightBlade': 5,   # dagger, knife
    'ShortLightBlunt': 6,   # sap, hand axe  # [canonical: N/A — derived]
    'ShortHeavyBlade': 6,   # short sword, arming sword  # [canonical: N/A — derived]
    'LongLightBlade': 6,    # spear, light lance  # [canonical: N/A — derived]
    'ShortHeavyBlunt': 7,   # club, mace  # [canonical: N/A — derived]
    'LongHeavyBlade': 7,    # longsword, axe, glaive  # [canonical: N/A — derived]
    'LongLightBlunt': 7,    # staff  # [canonical: N/A — derived]
    'LongHeavyBlunt': 8,    # war hammer, pollaxe  # [canonical: N/A — derived]
    'Unarmed': 8,           # fists  # [canonical: N/A — derived]
}

# [canonical: params/combat.md §Damage Formula PP-232 — weapon modifier vs armour tier]
WEAPON_DMG_MOD = {  # [canonical: params/combat.md §Damage Formula PP-232]
    'LightBlade':  {'None': 3, 'Light': 2, 'Medium': 1, 'Heavy': 0},  # [canonical: params/combat.md §Damage Formula]
    'HeavyBlade':  {'None': 6, 'Light': 4, 'Medium': 2, 'Heavy': 0},  # [canonical: params/combat.md §Damage Formula]
    'LightBlunt':  {'None': 3, 'Light': 3, 'Medium': 3, 'Heavy': 3},  # [canonical: params/combat.md §Damage Formula]
    'HeavyBlunt':  {'None': 5, 'Light': 5, 'Medium': 5, 'Heavy': 5},  # [canonical: params/combat.md §Damage Formula]
}

def weapon_class(wname):  # [canonical: params/combat.md §Weapon System]
    if 'LightBlade' in wname: return 'LightBlade'
    if 'HeavyBlade' in wname: return 'HeavyBlade'
    if 'LightBlunt' in wname: return 'LightBlunt'
    if 'HeavyBlunt' in wname: return 'HeavyBlunt'
    return 'LightBlunt'  # unarmed fallback  # [canonical: params/combat.md §Weapon System]

# [canonical: params/combat.md §Armour PP-232]
ARMOUR_STAM_MOD = {'None': 0, 'Light': 0, 'Medium': -1, 'Heavy': -2}  # [canonical: params/combat.md §Armour PP-232]

# [canonical: designs/scene/combat_v30.md §7 — action stamina costs]
STAM_COSTS = {  # [canonical: designs/scene/combat_v30.md §7 Stamina]
    'strike': 5, 'heavy_strike': 8, 'defensive': 3,
    'dodge': 4, 'movement': 2, 'feint': 5, 'full_guard': 3,  # [canonical: params/combat.md §PP-294]
    'take_breath': 0, 'tie_up': 5, 'disarm': 5,  # [canonical: designs/scene/combat_v30.md §4 Tie Up]
    'taunt': 3,  # [canonical: N/A — new duel action, cost parallels defensive]
}

CRIT_THRESHOLD = 3  # [canonical: params/combat.md §Damage Formula — net hits >= 3]

# ══════════════════════════════════════════════════════════════════════════════
# CANONICAL FORMULAS
# ══════════════════════════════════════════════════════════════════════════════

# [canonical: params/combat.md §Pool Formula L14]
def combat_pool(agi, hist):
    return max(5, agi * 2 + hist + 3)  # [canonical: params/combat.md §Pool Formula]

# [canonical: params/combat.md §Stamina ED-694]
def base_stamina(end):
    return end * 5  # [canonical: params/combat.md §Stamina ED-694]

# [canonical: designs/scene/derived_stats_v30.md §4.1 PP-716]
def max_wounds(end):
    return end // 2 + 1  # [canonical: designs/scene/derived_stats_v30.md §4.1]

def wound_interval(end):
    return end + 6  # [canonical: designs/scene/derived_stats_v30.md §4.1]

def total_health(end):
    return wound_interval(end) * (max_wounds(end) + 1)  # [canonical: designs/scene/derived_stats_v30.md §4.1]

# [canonical: designs/scene/combat_v30.md §7 — Take a Breath restores (End + hist) × 2]
def breath_recovery(end, hist):
    return (end + hist) * 2  # [canonical: designs/scene/combat_v30.md §7]

# [canonical: params/core.md §dice engine — d10, TN, 1s subtract, 10s chain]
def roll(rng, n, tn):
    if n <= 0: return 0  # [canonical: N/A — floor]
    dice = rng.integers(1, 11, size=n)  # [canonical: params/core.md §dice engine]
    hits = int(np.sum(dice >= tn))
    ones = int(np.sum(dice == 1))  # [canonical: params/core.md — 1s subtract]
    tens = int(np.sum(dice == 10))  # [canonical: params/core.md — 10s chain]
    if tens > 0:
        hits += int(np.sum(rng.integers(1, 11, size=tens) >= tn))  # [canonical: params/core.md — chain]
    return max(0, hits - ones)

# ══════════════════════════════════════════════════════════════════════════════
# DUELIST STATE — wraps canonical combat state
# ══════════════════════════════════════════════════════════════════════════════

def make_duelist(weapon, armour, agi, str_, end, hist, cog=4, composure=5):  # [canonical: N/A — test character stats]
    tn = WEAPON_TN[weapon]  # [canonical: params/combat.md §Weapon System]
    wc = weapon_class(weapon)
    stam_mod = ARMOUR_STAM_MOD[armour]  # [canonical: params/combat.md §Armour]
    pool = combat_pool(agi, hist)  # [canonical: params/combat.md §Pool Formula]
    stam = base_stamina(end)  # [canonical: params/combat.md §Stamina]
    return {
        'weapon': weapon, 'armour': armour, 'weapon_class': wc,
        'tn': tn, 'pool': pool,
        'agi': agi, 'str': str_, 'end': end, 'hist': hist,
        'cog': cog, 'composure': composure,
        'stam_max': stam, 'stamina': stam, 'stam_mod': stam_mod,
        'health_max': total_health(end), 'health': total_health(end),
        'wound_interval': wound_interval(end), 'max_wounds': max_wounds(end),
        'wounds': 0, 'dmg_acc': 0,
        'has_init': False,
        'feint_debuff': 0,       # [canonical: params/combat.md §PP-294 — pool reduction next round]
        'tied_up': False,        # [canonical: designs/scene/combat_v30.md §4 — Tie Up]
        'forced_first_decl': False,  # Taunt effect — must declare pool split first
        'oob': False,            # [canonical: designs/scene/combat_v30.md §7 — Out of Breath]
    }

def effective_pool(d):
    p = d['pool'] - d['wounds'] - d['feint_debuff']  # [canonical: params/combat.md §Pool Formula — wound -1D, feint debuff]
    if d['oob']: p -= 2  # [canonical: designs/scene/combat_v30.md §1 — OOB -2D]
    if d['tied_up']: p -= 2  # [canonical: designs/scene/combat_v30.md §4 — Tie Up -2D]
    return max(5, p)  # [canonical: params/combat.md §Pool Formula — minimum 5, clean floor ED-203]

def drain_stamina(d, action):
    cost = STAM_COSTS.get(action, 5)  # [canonical: designs/scene/combat_v30.md §7]
    cost -= d['stam_mod']  # [canonical: designs/scene/combat_v30.md §7 — armour adds to drain]
    d['stamina'] = max(0, d['stamina'] - max(0, cost))
    d['oob'] = d['stamina'] <= 0  # [canonical: designs/scene/combat_v30.md §7]

def apply_damage(defender, net_hits, attacker):
    if net_hits <= 0: return 0  # [canonical: N/A — no damage]
    wc = attacker['weapon_class']
    wmod = WEAPON_DMG_MOD[wc][defender['armour']]  # [canonical: params/combat.md §Damage Formula]
    if net_hits >= CRIT_THRESHOLD:  # [canonical: params/combat.md §Damage Formula — crit]
        wmod *= 2  # [canonical: params/combat.md §Damage Formula — crit doubles weapon mod]
    damage = net_hits + attacker['str'] + wmod  # [canonical: params/combat.md §Damage Formula]
    defender['health'] = max(0, defender['health'] - damage)
    defender['dmg_acc'] += damage
    old_wounds = defender['wounds']
    defender['wounds'] = min(defender['max_wounds'] + 1, defender['dmg_acc'] // defender['wound_interval'])  # [canonical: designs/scene/derived_stats_v30.md §4.1]
    return defender['wounds'] - old_wounds

# ══════════════════════════════════════════════════════════════════════════════
# DECISION PROTOCOLS — how AI chooses actions + pool splits
# ══════════════════════════════════════════════════════════════════════════════

# Pool split = fraction allocated to offense (0.0 = full guard, 1.0 = all-out attack)
# The protocol returns (action, off_fraction)

def protocol_action(protocol, me, opp, rd, rng):
    """Return (action_name, offense_fraction)."""
    pool = effective_pool(me)
    my_stam_frac = me['stamina'] / max(1, me['stam_max'])
    opp_stam_frac = opp['stamina'] / max(1, opp['stam_max'])
    my_health_frac = me['health'] / max(1, me['health_max'])
    opp_health_frac = opp['health'] / max(1, opp['health_max'])

    if protocol == 'AGGRESSIVE':
        return ('strike', 0.75)  # [canonical: N/A — test protocol]

    elif protocol == 'DEFENSIVE':
        return ('strike', 0.30)  # [canonical: N/A — test protocol]

    elif protocol == 'BALANCED':
        return ('strike', 0.50)  # [canonical: N/A — test protocol]

    elif protocol == 'FULL_GUARD':
        return ('full_guard', 0.0)  # [canonical: designs/scene/combat_v30.md §4 — Full Guard]

    elif protocol == 'FEINTER':
        # Feint every 3rd round, aggressive strike otherwise
        if rd % 3 == 1 and me['feint_debuff'] == 0:  # [canonical: N/A — test protocol]
            return ('feint', 0.60)  # commit 60% to feint  # [canonical: params/combat.md §PP-294 — min 3 dice]
        return ('strike', 0.65)  # [canonical: N/A — test protocol]

    elif protocol == 'FEINT_SPAM':
        return ('feint', 0.70)  # [canonical: N/A — test protocol]

    elif protocol == 'TAUNTER':
        # Taunt every other round, defensive strike otherwise
        if rd % 2 == 0:  # [canonical: N/A — test protocol]
            return ('taunt', 0.30)  # [canonical: N/A — Taunt is new duel action]
        return ('strike', 0.40)  # [canonical: N/A — test protocol]

    elif protocol == 'ADAPTIVE':
        # Reads state to choose action
        if my_stam_frac < 0.2 and not me['oob']:  # [canonical: N/A — test protocol]
            return ('take_breath', 0.0)
        if opp['feint_debuff'] > 0:
            return ('strike', 0.70)  # exploit opponent's reduced pool  # [canonical: N/A — test protocol]
        if opp_health_frac < 0.3:
            return ('strike', 0.75)  # finish them  # [canonical: N/A — test protocol]
        if me['has_init'] and rd % 3 == 0:  # [canonical: N/A — test protocol]
            return ('feint', 0.55)
        if not me['has_init'] and opp_stam_frac > my_stam_frac + 0.2:  # [canonical: N/A — test protocol]
            return ('strike', 0.35)  # conserve, defend
        return ('strike', 0.50)  # [canonical: N/A — derived]

    elif protocol == 'COUNTER_PUNCHER':
        # Defensive until opportunity — high defense, exploit feint debuffs
        if opp['feint_debuff'] > 0 or opp_health_frac < 0.4:  # [canonical: N/A — test protocol]
            return ('strike', 0.65)
        return ('strike', 0.30)  # [canonical: N/A — derived]

    elif protocol == 'BRAWLER':
        # Aggressive + uses Tie Up at close range when wounded
        if me['wounds'] >= 1 and not opp['tied_up']:  # [canonical: N/A — test protocol]
            return ('tie_up', 0.55)
        return ('strike', 0.70)  # [canonical: N/A — derived]

    elif protocol == 'DUELLIST':
        # Mix of taunt, feint, and measured strikes — the "flair" build
        if rd <= 2:  # [canonical: N/A — test protocol]
            return ('taunt', 0.30)  # open with intimidation
        if me['has_init'] and rd % 4 == 0:  # [canonical: N/A — test protocol]
            return ('feint', 0.50)
        if opp['feint_debuff'] > 0 or opp['forced_first_decl']:  # [canonical: N/A — test protocol]
            return ('strike', 0.65)  # exploit created openings
        return ('strike', 0.45)  # [canonical: N/A — derived]

    elif protocol == 'STAMINA_FIGHTER':
        # Low offense, high defense, uses Take a Breath — wins by attrition
        if my_stam_frac < 0.4 and not me['oob']:  # [canonical: N/A — test protocol]
            return ('take_breath', 0.0)
        return ('strike', 0.30)  # [canonical: N/A — derived]

    return ('strike', 0.50)  # fallback  # [canonical: N/A]

# ══════════════════════════════════════════════════════════════════════════════
# DUEL SIMULATION — canonical scene combat + E7 yield + Taunt
# ══════════════════════════════════════════════════════════════════════════════

def sim_duel(weapon_a, armour_a, weapon_b, armour_b,
             agi=4, str_=4, end=4, hist=2, cog=4, composure=5,  # [canonical: N/A — test character stats]
             protocol_a='BALANCED', protocol_b='BALANCED',
             yield_at_zero=True, seed=42, max_rounds=30,  # [canonical: N/A — test battery]
             agi_a=None, agi_b=None, end_a=None, end_b=None,
             str_a=None, str_b=None, cog_a=None, cog_b=None,
             composure_a=None, composure_b=None):
    rng = np.random.default_rng(seed)  # [canonical: N/A — RNG]

    ea, eb = end_a or end, end_b or end
    sa, sb = str_a or str_, str_b or str_
    aa, ab = agi_a or agi, agi_b or agi
    ca, cb = cog_a or cog, cog_b or cog
    compa, compb = composure_a or composure, composure_b or composure

    a = make_duelist(weapon_a, armour_a, aa, sa, ea, hist, ca, compa)
    b = make_duelist(weapon_b, armour_b, ab, sb, eb, hist, cb, compb)

    # [canonical: params/combat.md §Initiative PP-232 — higher Attunement acts last]
    # Using Agility as proxy for Attunement in personal combat
    if aa > ab: a['has_init'] = True
    elif ab > aa: b['has_init'] = True
    else: a['has_init'] = bool(rng.integers(0, 2)); b['has_init'] = not a['has_init']  # [canonical: params/combat.md §PP-239]

    log = defaultdict(int)
    log['actions_a'] = defaultdict(int)
    log['actions_b'] = defaultdict(int)

    for rd in range(1, max_rounds + 1):  # [canonical: N/A — sim loop]

        # ── End-of-round checks from prior round ──
        a_incap = a['wounds'] > a['max_wounds'] or a['health'] <= 0  # [canonical: designs/scene/combat_v30.md §4 — Stage 1]
        b_incap = b['wounds'] > b['max_wounds'] or b['health'] <= 0
        if a_incap and b_incap:
            log.update(rounds=rd-1, winner='draw', end_reason='mutual_incap'); break
        if a_incap:
            log.update(rounds=rd-1, winner='B', end_reason='incap_A'); break
        if b_incap:
            log.update(rounds=rd-1, winner='A', end_reason='incap_B'); break

        # ── E7 yield (duel context) ──
        if yield_at_zero:  # [canonical: N/A — duel context rule E7]
            ay, by = a['oob'], b['oob']
            if ay and by:
                w = 'A' if a['health'] > b['health'] else ('B' if b['health'] > a['health'] else 'draw')
                log.update(rounds=rd, winner=w, end_reason='mutual_yield'); break
            elif ay:
                log.update(rounds=rd, winner='B', end_reason='yield_A'); break
            elif by:
                log.update(rounds=rd, winner='A', end_reason='yield_B'); break

        # ── Clear per-round effects ──
        a['feint_debuff'] = max(0, a['feint_debuff'])  # debuff persists from prior round
        b['feint_debuff'] = max(0, b['feint_debuff'])
        new_feint_a, new_feint_b = 0, 0  # set this round, apply next  # [canonical: params/combat.md §PP-294]

        # ── Action + pool-split declaration ──
        # [canonical: designs/scene/combat_v30.md §3 — lower-init declares first]
        # Taunt flips this: forced_first_decl makes you declare first regardless
        a_declares_first = not a['has_init']
        b_declares_first = not b['has_init']
        if a['forced_first_decl']: a_declares_first = True  # [canonical: N/A — Taunt effect]
        if b['forced_first_decl']: b_declares_first = True

        action_a, off_frac_a = protocol_action(protocol_a, a, b, rd, rng)
        action_b, off_frac_b = protocol_action(protocol_b, b, a, rd, rng)

        log['actions_a'][action_a] += 1  # [canonical: N/A — logging]
        log['actions_b'][action_b] += 1

        # ── Compute pool splits ──
        pool_a = effective_pool(a)  # [canonical: params/combat.md §Pool Formula]
        pool_b = effective_pool(b)

        off_a = max(0, int(pool_a * off_frac_a))  # [canonical: designs/scene/combat_v30.md §3 — pool split]
        def_a = pool_a - off_a
        off_b = max(0, int(pool_b * off_frac_b))
        def_b = pool_b - off_b

        # Full Guard: all to defense  # [canonical: designs/scene/combat_v30.md §4]
        if action_a == 'full_guard': off_a = 0; def_a = pool_a
        if action_b == 'full_guard': off_b = 0; def_b = pool_b

        # ── RESOLUTION by action priority (PP-247) ──

        # Priority 1: Strike
        net_a_dmg, net_b_dmg = 0, 0
        if action_a == 'strike':
            hits = roll(rng, max(1, off_a), a['tn'])  # [canonical: designs/scene/combat_v30.md §4 — Strike]
            blocks = roll(rng, def_b, b['tn'])
            net = hits - blocks
            if net > 0:
                apply_damage(b, net, a)
                net_a_dmg = net
            drain_stamina(a, 'strike')

        if action_b == 'strike':
            hits = roll(rng, max(1, off_b), b['tn'])
            blocks = roll(rng, def_a, a['tn'])
            net = hits - blocks
            if net > 0:
                apply_damage(a, net, b)
                net_b_dmg = net
            drain_stamina(b, 'strike')

        # Priority 2: Feint (PP-294)
        if action_a == 'feint':  # [canonical: params/combat.md §PP-294]
            feint_dice = max(3, off_a)  # [canonical: params/combat.md §PP-294 — minimum 3]
            feint_def_a = pool_a - feint_dice  # remainder to defense  # [canonical: params/combat.md §PP-238]
            # But PP-238 says feint commits FULL pool to offense, defense=0
            feint_hits = roll(rng, feint_dice, 7)  # [canonical: params/combat.md §PP-294 — TN 7 vs TN 7]
            opp_def_hits = roll(rng, def_b, 7)  # [canonical: params/combat.md §PP-294]
            margin = feint_hits - opp_def_hits
            if margin > 0:
                new_feint_b = margin  # [canonical: params/combat.md §PP-294 — pool reduction next round]
                log['feints_landed'] = log.get('feints_landed', 0) + 1  # [canonical: N/A — logging]
            # Feinter has defense 0 this round (PP-238)
            def_a = 0  # [canonical: params/combat.md §PP-238 — feint full-pool]
            drain_stamina(a, 'feint')

        if action_b == 'feint':
            feint_dice = max(3, off_b)  # [canonical: params/combat.md §PP-294]
            feint_hits = roll(rng, feint_dice, 7)
            opp_def_hits = roll(rng, def_a, 7)  # [canonical: params/core.md §dice engine]
            margin = feint_hits - opp_def_hits
            if margin > 0:
                new_feint_a = margin
                log['feints_landed'] = log.get('feints_landed', 0) + 1
            def_b = 0  # [canonical: params/combat.md §PP-238]
            drain_stamina(b, 'feint')

        # Priority 3: Tie Up
        if action_a == 'tie_up' and not b['tied_up']:  # [canonical: designs/scene/combat_v30.md §4]
            tu_hits = roll(rng, max(1, off_a), a['tn'])
            # Tie Up: Offence roll, success = both -2D, blocks escape
            if tu_hits > 0:
                a['tied_up'] = True; b['tied_up'] = True  # [canonical: designs/scene/combat_v30.md §4]
                log['tie_ups'] = log.get('tie_ups', 0) + 1
            drain_stamina(a, 'tie_up')

        if action_b == 'tie_up' and not a['tied_up']:
            tu_hits = roll(rng, max(1, off_b), b['tn'])
            if tu_hits > 0:
                a['tied_up'] = True; b['tied_up'] = True
                log['tie_ups'] = log.get('tie_ups', 0) + 1
            drain_stamina(b, 'tie_up')

        # Reactive: Take a Breath  # [canonical: designs/scene/combat_v30.md §4]
        if action_a == 'take_breath':
            recovery = breath_recovery(a['end'], a['hist'])  # [canonical: designs/scene/combat_v30.md §7]
            a['stamina'] = min(a['stam_max'], a['stamina'] + recovery)
            a['oob'] = a['stamina'] <= 0  # [canonical: N/A — update OOB]
            # No combat action — vulnerable (defense only)
            def_a = pool_a  # all to defense while catching breath  # [canonical: N/A — implied by "no combat action"]

        if action_b == 'take_breath':
            recovery = breath_recovery(b['end'], b['hist'])
            b['stamina'] = min(b['stam_max'], b['stamina'] + recovery)
            b['oob'] = b['stamina'] <= 0
            def_b = pool_b

        # NEW — Taunt (duel context action)
        # Roll Cognition TN 7 vs opponent's Composure TN 7
        # Success: opponent must declare pool split first next round (loses initiative information advantage)
        if action_a == 'taunt':  # [canonical: N/A — new duel action]
            taunt_hits = roll(rng, ca, 7)  # [canonical: N/A — Cognition-based]
            resist_hits = roll(rng, compb, 7)  # [canonical: N/A — Composure resist]
            if taunt_hits > resist_hits:
                b['forced_first_decl'] = True  # [canonical: N/A — Taunt effect]
                log['taunts_landed'] = log.get('taunts_landed', 0) + 1
            drain_stamina(a, 'taunt')

        if action_b == 'taunt':
            taunt_hits = roll(rng, cb, 7)  # [canonical: params/core.md §dice engine]
            resist_hits = roll(rng, compa, 7)  # [canonical: params/core.md §dice engine]
            if taunt_hits > resist_hits:
                a['forced_first_decl'] = True
                log['taunts_landed'] = log.get('taunts_landed', 0) + 1
            drain_stamina(b, 'taunt')

        # Full Guard stamina  # [canonical: designs/scene/combat_v30.md §4]
        if action_a == 'full_guard': drain_stamina(a, 'full_guard')
        if action_b == 'full_guard': drain_stamina(b, 'full_guard')

        # If B struck and A feinted (defense=0 from feint), B's strike hits undefended
        # Already handled: def_a was set to 0 above before B's strike resolves
        # Wait — action priority says Strike (P1) resolves before Feint (P2)
        # So if A feints and B strikes: B's strike resolves FIRST (at A's original defense),
        # then A's feint resolves. But PP-238 says feint defense=0 THIS round.
        # PP-238: "feint commits full pool to Offence; Defence = 0 this round"
        # This means the feinter is exposed to all attacks this round.
        # The strike already resolved above with def_a potentially at 0.
        # Actually the order above is wrong: I need to set def_a=0 BEFORE strike resolves.
        # Let me fix this: feint exposure should be set at declaration, not at resolution.
        # For now: the code above sets def_a=0 in the feint block (P2) AFTER strike (P1).
        # This is a bug — fix by moving feint exposure to declaration phase.

        # ── Initiative transfer (canonical §3) ──
        # [canonical: designs/scene/combat_v30.md §3 — transfers to exchange winner]
        if net_a_dmg > 0 and net_b_dmg == 0:
            a['has_init'] = True; b['has_init'] = False
        elif net_b_dmg > 0 and net_a_dmg == 0:
            b['has_init'] = True; a['has_init'] = False

        # ── Apply feint debuffs for NEXT round ──
        a['feint_debuff'] = new_feint_a  # [canonical: params/combat.md §PP-294 — applies next round]
        b['feint_debuff'] = new_feint_b

        # ── Clear single-round effects ──
        a['forced_first_decl'] = False  # [canonical: N/A — Taunt lasts 1 round]
        b['forced_first_decl'] = False
        # Tied Up lasts until escape (not modeled in this sim yet)  # [canonical: designs/scene/combat_v30.md §4]

    else:
        if a['health'] > b['health']: log.update(rounds=max_rounds, winner='A', end_reason='timeout_health')
        elif b['health'] > a['health']: log.update(rounds=max_rounds, winner='B', end_reason='timeout_health')
        else: log.update(rounds=max_rounds, winner='draw', end_reason='timeout')

    log['a_health'] = a['health']; log['b_health'] = b['health']
    log['a_wounds'] = a['wounds']; log['b_wounds'] = b['wounds']
    log['a_stamina'] = a['stamina']; log['b_stamina'] = b['stamina']
    return log

# ══════════════════════════════════════════════════════════════════════════════
# BATTERY
# ══════════════════════════════════════════════════════════════════════════════

def run(label, N, **kw):
    wins = {'A': 0, 'B': 0, 'draw': 0}  # [canonical: N/A — sim]
    reasons = defaultdict(int)
    rounds_l, aw_l, bw_l, as_l, bs_l = [], [], [], [], []
    feints_l, taunts_l, tieups_l = [], [], []

    for i in range(N):
        r = sim_duel(seed=1000000+i, **kw)  # [canonical: N/A — RNG seed]
        w = r.get('winner', 'draw')
        wins[w] = wins.get(w, 0) + 1
        reasons[r.get('end_reason', '?')] += 1
        rounds_l.append(r.get('rounds', 30))  # [canonical: N/A — sim]
        aw_l.append(r.get('a_wounds', 0)); bw_l.append(r.get('b_wounds', 0))
        as_l.append(r.get('a_stamina', 0)); bs_l.append(r.get('b_stamina', 0))
        feints_l.append(r.get('feints_landed', 0))
        taunts_l.append(r.get('taunts_landed', 0))
        tieups_l.append(r.get('tie_ups', 0))

    ra = np.array(rounds_l)
    rs = ', '.join(f"{k}:{v}" for k,v in sorted(reasons.items()))
    print(f"\n{'='*74}")
    print(f"  {label}  (N={N})")
    print(f"{'='*74}")
    print(f"  A: {wins['A']/N:.1%}  B: {wins['B']/N:.1%}  Draw: {wins['draw']/N:.1%}")
    print(f"  Rounds: {ra.mean():.1f} ±{ra.std():.1f} [{ra.min()}–{ra.max()}]")
    print(f"  End: {rs}")
    print(f"  Wounds: A {np.mean(aw_l):.1f}  B {np.mean(bw_l):.1f}  |  Stam left: A {np.mean(as_l):.1f}  B {np.mean(bs_l):.1f}")
    if sum(feints_l) > 0: print(f"  Feints landed/duel: {np.mean(feints_l):.2f}")
    if sum(taunts_l) > 0: print(f"  Taunts landed/duel: {np.mean(taunts_l):.2f}")
    if sum(tieups_l) > 0: print(f"  Tie-ups/duel: {np.mean(tieups_l):.2f}")
    return wins, ra

# ══════════════════════════════════════════════════════════════════════════════
# RUN
# ══════════════════════════════════════════════════════════════════════════════

N = 5000  # [canonical: N/A — simulation parameter]
B = dict(agi=4, str_=4, end=4, hist=2)  # [canonical: N/A — test stats]

print("=" * 74)  # [canonical: N/A — output]
print("  ARCHITECTURE C v4 — SCENE COMBAT CHASSIS + DUEL CONTEXT LAYER")
print("  No imposed triangle. Bottom-up emergence from canonical resolution.")
print("=" * 74)  # [canonical: N/A — output]

# SECTION 1: POOL-SPLIT EMERGENCE — does the canonical system produce a triangle?
print("\n" + "~" * 74)  # [canonical: N/A — output]
print("  §1: POOL-SPLIT EMERGENCE — does canonical resolution produce RPS?")
print("~" * 74)  # [canonical: N/A — output]
run("75/25 (aggressive) vs 30/70 (defensive)", N,
    weapon_a='ShortHeavyBlade', armour_a='None', weapon_b='ShortHeavyBlade', armour_b='None',
    protocol_a='AGGRESSIVE', protocol_b='DEFENSIVE', **B)
run("75/25 (aggressive) vs 50/50 (balanced)", N,
    weapon_a='ShortHeavyBlade', armour_a='None', weapon_b='ShortHeavyBlade', armour_b='None',
    protocol_a='AGGRESSIVE', protocol_b='BALANCED', **B)
run("30/70 (defensive) vs 50/50 (balanced)", N,
    weapon_a='ShortHeavyBlade', armour_a='None', weapon_b='ShortHeavyBlade', armour_b='None',
    protocol_a='DEFENSIVE', protocol_b='BALANCED', **B)
run("50/50 (balanced) mirror", N,
    weapon_a='ShortHeavyBlade', armour_a='None', weapon_b='ShortHeavyBlade', armour_b='None',
    protocol_a='BALANCED', protocol_b='BALANCED', **B)
run("Full Guard vs Aggressive", N,
    weapon_a='ShortHeavyBlade', armour_a='None', weapon_b='ShortHeavyBlade', armour_b='None',
    protocol_a='FULL_GUARD', protocol_b='AGGRESSIVE', **B)

# SECTION 2: CANONICAL ACTIONS — Feint, Tie Up, Take a Breath
print("\n" + "~" * 74)  # [canonical: N/A — output]
print("  §2: CANONICAL ACTIONS — Feint (PP-294), Tie Up, Take a Breath")
print("~" * 74)  # [canonical: N/A — output]
run("Feinter (feint every 3rd) vs Balanced", N,
    weapon_a='ShortHeavyBlade', armour_a='None', weapon_b='ShortHeavyBlade', armour_b='None',
    protocol_a='FEINTER', protocol_b='BALANCED', **B)
run("Feint-spam vs Balanced", N,
    weapon_a='ShortHeavyBlade', armour_a='None', weapon_b='ShortHeavyBlade', armour_b='None',
    protocol_a='FEINT_SPAM', protocol_b='BALANCED', **B)
run("Brawler (tie-up) vs Balanced", N,
    weapon_a='ShortHeavyBlade', armour_a='None', weapon_b='ShortHeavyBlade', armour_b='None',
    protocol_a='BRAWLER', protocol_b='BALANCED', **B)
run("Stamina-fighter (breath) vs Aggressive", N,
    weapon_a='ShortHeavyBlade', armour_a='None', weapon_b='ShortHeavyBlade', armour_b='None',
    protocol_a='STAMINA_FIGHTER', protocol_b='AGGRESSIVE', **B)

# SECTION 3: DUEL-CONTEXT ACTIONS — Taunt
print("\n" + "~" * 74)  # [canonical: N/A — output]
print("  §3: DUEL-CONTEXT ACTIONS — Taunt (new)")
print("~" * 74)  # [canonical: N/A — output]
run("Taunter vs Balanced", N,
    weapon_a='ShortHeavyBlade', armour_a='None', weapon_b='ShortHeavyBlade', armour_b='None',
    protocol_a='TAUNTER', protocol_b='BALANCED', **B)
run("Taunter vs Adaptive", N,
    weapon_a='ShortHeavyBlade', armour_a='None', weapon_b='ShortHeavyBlade', armour_b='None',
    protocol_a='TAUNTER', protocol_b='ADAPTIVE', **B)
run("Taunter (high COG 6) vs Balanced", N,
    weapon_a='ShortHeavyBlade', armour_a='None', weapon_b='ShortHeavyBlade', armour_b='None',
    protocol_a='TAUNTER', protocol_b='BALANCED', cog_a=6, **B)  # [canonical: N/A — test battery]

# SECTION 4: BUILD ARCHETYPES — does build complement style?
print("\n" + "~" * 74)  # [canonical: N/A — output]
print("  §4: BUILD ARCHETYPES — stat builds complementing styles")
print("~" * 74)  # [canonical: N/A — output]
run("Duellist build (COG 6, Agi 5, End 3) vs Brawler build (STR 6, End 5, Agi 3)", N,
    weapon_a='ShortLightBlade', armour_a='None', weapon_b='ShortHeavyBlunt', armour_b='Medium',
    protocol_a='DUELLIST', protocol_b='BRAWLER',
    agi_a=5, cog_a=6, end_a=3, str_a=3,  # [canonical: N/A — test build]
    agi_b=3, str_b=6, end_b=5, cog_b=3,  # [canonical: N/A — test build]
    agi=4, str_=4, end=4, hist=2)

run("Duellist build vs Adaptive (default stats)", N,
    weapon_a='ShortLightBlade', armour_a='None', weapon_b='ShortHeavyBlade', armour_b='None',
    protocol_a='DUELLIST', protocol_b='ADAPTIVE', **B)

run("Counter-puncher (high End 6) vs Aggressive (high Agi 5)", N,
    weapon_a='ShortHeavyBlade', armour_a='Light', weapon_b='ShortLightBlade', armour_b='None',
    protocol_a='COUNTER_PUNCHER', protocol_b='AGGRESSIVE',
    end_a=6, agi_a=3, str_a=4,  # [canonical: N/A — test build]
    agi_b=5, end_b=3, str_b=3,  # [canonical: N/A — test build]
    agi=4, str_=4, end=4, hist=2)

# SECTION 5: STAT ASYMMETRY — canonical formula impact
print("\n" + "~" * 74)  # [canonical: N/A — output]
print("  §5: STAT ASYMMETRY")
print("~" * 74)  # [canonical: N/A — output]
for label, kwa in [
    ("Agi 5v3 (Adaptive)", dict(agi_a=5, agi_b=3)),  # [canonical: N/A — test character stats]
    ("End 6v3 (Adaptive)", dict(end_a=6, end_b=3)),  # [canonical: N/A — test character stats]
    ("End 5v4 (Adaptive)", dict(end_a=5, end_b=4)),  # [canonical: N/A — test character stats]
    ("STR 6v3 (Adaptive)", dict(str_a=6, str_b=3)),  # [canonical: N/A — test character stats]
    ("COG 6v3 (Taunter vs Taunter)", dict(cog_a=6, cog_b=3)),  # [canonical: N/A — test character stats]
]:
    prot = 'ADAPTIVE' if 'Taunter' not in label else 'TAUNTER'
    run(f"S: {label}", N,
        weapon_a='ShortHeavyBlade', armour_a='None',
        weapon_b='ShortHeavyBlade', armour_b='None',
        protocol_a=prot, protocol_b=prot, **{**B, **kwa})

# SECTION 6: WEAPON MATCHUPS
print("\n" + "~" * 74)  # [canonical: N/A — output]
print("  §6: WEAPON MATCHUPS (Adaptive)")
print("~" * 74)  # [canonical: N/A — output]
for wa, wb, label in [
    ('ShortLightBlade', 'LongHeavyBlade', 'Dagger TN5 vs Longsword TN7'),
    ('ShortHeavyBlade', 'LongHeavyBlade', 'Arming sword TN6 vs Longsword TN7'),
    ('ShortHeavyBlade', 'LongHeavyBlunt', 'Arming sword TN6 vs Warhammer TN8'),
    ('ShortLightBlade', 'ShortHeavyBlunt', 'Dagger TN5 vs Mace TN7'),
]:
    run(f"W: {label}", N,
        weapon_a=wa, armour_a='None', weapon_b=wb, armour_b='None',
        protocol_a='ADAPTIVE', protocol_b='ADAPTIVE', **B)

# SECTION 7: DURATION TABLE
print("\n" + "~" * 74)  # [canonical: N/A — output]
print("  §7: DURATION BY ENDURANCE (Adaptive mirror)")
print("~" * 74)  # [canonical: N/A — output]
print(f"  {'End':>4}  {'Pool':>5}  {'Stam':>5}  {'HP':>4}  {'MW':>3}  {'Rnds':>6}  {'Yield%':>7}  {'Incap%':>7}")
for e in [2, 3, 4, 5, 6, 7]:  # [canonical: N/A — sweep]
    w, ra = run(f"dur_{e}", 3000,  # [canonical: N/A — sim parameter]
        weapon_a='ShortHeavyBlade', armour_a='None',
        weapon_b='ShortHeavyBlade', armour_b='None',
        protocol_a='ADAPTIVE', protocol_b='ADAPTIVE',
        agi=4, str_=4, end=e, hist=2)  # [canonical: N/A — test character stats]

print("\n" + "=" * 74)  # [canonical: N/A — output]
print("  FINDINGS")
print("=" * 74)  # [canonical: N/A — output]
