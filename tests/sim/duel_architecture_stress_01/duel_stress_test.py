#!/usr/bin/env python3
"""Architecture C duel v5 — initiative info advantage + PP-294 Feint fix."""  # [canonical: N/A]
import numpy as np  # [canonical: N/A]
from collections import defaultdict  # [canonical: N/A]

# ══ CANONICAL CONSTANTS ══════════════════════════════════════════════════════
# [canonical: params/combat.md §Weapon System PP-232]
WEAPON_TN = {
    'ShortLightBlade': 5, 'ShortLightBlunt': 6,  # [canonical: params/combat.md §Weapon System PP-232]
    'ShortHeavyBlade': 6, 'LongLightBlade': 6,  # [canonical: params/combat.md §Weapon System PP-232]
    'ShortHeavyBlunt': 7, 'LongHeavyBlade': 7, 'LongLightBlunt': 7,  # [canonical: params/combat.md §Weapon System PP-232]
    'LongHeavyBlunt': 8, 'Unarmed': 8,  # [canonical: params/combat.md §Weapon System PP-232]
}
# [canonical: params/combat.md §Damage Formula PP-232]
WEAPON_DMG = {
    'LightBlade':  {'None': 3, 'Light': 2, 'Medium': 1, 'Heavy': 0},  # [canonical: params/combat.md §Damage Formula]
    'HeavyBlade':  {'None': 6, 'Light': 4, 'Medium': 2, 'Heavy': 0},  # [canonical: params/combat.md §Damage Formula]
    'LightBlunt':  {'None': 3, 'Light': 3, 'Medium': 3, 'Heavy': 3},  # [canonical: params/combat.md §Damage Formula]
    'HeavyBlunt':  {'None': 5, 'Light': 5, 'Medium': 5, 'Heavy': 5},  # [canonical: params/combat.md §Damage Formula]
}
def wclass(w):  # [canonical: params/combat.md §Weapon System]
    for c in ['LightBlade','HeavyBlade','LightBlunt','HeavyBlunt']:
        if c in w: return c
    return 'LightBlunt'  # [canonical: params/combat.md §Weapon System — unarmed fallback]

ARMOUR_STAM = {'None': 0, 'Light': 0, 'Medium': -1, 'Heavy': -2}  # [canonical: params/combat.md §Armour PP-232]
STAM = {'strike': 5, 'feint': 5, 'full_guard': 3, 'take_breath': 0, 'taunt': 5, 'tie_up': 5}  # [canonical: designs/scene/combat_v30.md §7]
CRIT = 3  # [canonical: params/combat.md §Damage Formula — net hits >= 3]

def pool(agi, hist): return max(5, agi * 2 + hist + 3)  # [canonical: params/combat.md §Pool Formula]
def stam_max(end): return end * 5  # [canonical: params/combat.md §Stamina ED-694]
def mw(end): return end // 2 + 1  # [canonical: designs/scene/derived_stats_v30.md §4.1 PP-716]
def wi(end): return end + 6  # [canonical: designs/scene/derived_stats_v30.md §4.1]
def hp(end): return wi(end) * (mw(end) + 1)  # [canonical: designs/scene/derived_stats_v30.md §4.1]

def roll(rng, n, tn):  # [canonical: params/core.md §dice engine]
    if n <= 0: return 0  # [canonical: N/A — floor]
    d = rng.integers(1, 11, size=n)  # [canonical: params/core.md §dice engine]
    h = int(np.sum(d >= tn)) - int(np.sum(d == 1))  # [canonical: params/core.md — hits minus 1s]
    t = int(np.sum(d == 10))  # [canonical: params/core.md — chain on 10]
    if t > 0: h += int(np.sum(rng.integers(1, 11, size=t) >= tn))  # [canonical: params/core.md — chain]
    return max(0, h)

# ══ DUELIST ══════════════════════════════════════════════════════════════════

def make(w, arm, agi, str_, end, hist, cog=4, comp=5):  # [canonical: N/A — constructor]
    return dict(w=w, arm=arm, wc=wclass(w), tn=WEAPON_TN[w],  # [canonical: params/combat.md §Weapon System]
        pool=pool(agi,hist), agi=agi, str=str_, end=end, hist=hist, cog=cog, comp=comp,  # [canonical: params/combat.md §Pool Formula]
        sm=stam_max(end), stam=stam_max(end), smod=ARMOUR_STAM[arm],  # [canonical: params/combat.md §Stamina]
        hmax=hp(end), hp=hp(end), wi=wi(end), mw=mw(end),  # [canonical: designs/scene/derived_stats_v30.md §4.1]
        wounds=0, dacc=0, init=False, fdeb=0, forced1st=False, oob=False)  # [canonical: N/A — state]

def epool(d):  # [canonical: params/combat.md §Pool Formula]
    p = d['pool'] - d['wounds'] - d['fdeb']  # [canonical: params/combat.md — wound -1D, feint debuff]
    if d['oob']: p -= 2  # [canonical: designs/scene/combat_v30.md §1 — OOB -2D]
    return max(5, p)  # [canonical: params/combat.md §Pool Formula — minimum 5 ED-203]

def drain(d, act):  # [canonical: designs/scene/combat_v30.md §7 Stamina]
    c = STAM.get(act, 5) - d['smod']  # [canonical: designs/scene/combat_v30.md §7]
    d['stam'] = max(0, d['stam'] - max(0, c))  # [canonical: N/A — floor]
    d['oob'] = d['stam'] <= 0  # [canonical: designs/scene/combat_v30.md §7]

def dmg(defender, net, attacker):  # [canonical: params/combat.md §Damage Formula]
    if net <= 0: return 0  # [canonical: N/A]
    wm = WEAPON_DMG[attacker['wc']][defender['arm']]  # [canonical: params/combat.md §Damage Formula]
    if net >= CRIT: wm *= 2  # [canonical: params/combat.md §Damage Formula — crit]
    d = net + attacker['str'] + wm  # [canonical: params/combat.md §Damage Formula]
    defender['hp'] = max(0, defender['hp'] - d)  # [canonical: N/A — floor]
    defender['dacc'] += d  # [canonical: designs/scene/derived_stats_v30.md §4.1]
    ow = defender['wounds']
    defender['wounds'] = min(defender['mw'] + 1, defender['dacc'] // defender['wi'])  # [canonical: designs/scene/derived_stats_v30.md §4.1]
    return defender['wounds'] - ow

# ══ PROTOCOLS — now with REACTIVE second-declarer awareness ═════════════════

def choose(protocol, me, opp, rd, rng, opp_action=None, opp_split=None):
    """Return (action, offense_fraction).
    opp_action/opp_split are set ONLY for the second declarer (initiative advantage)."""
    sf = me['stam'] / max(1, me['sm'])  # [canonical: N/A — stamina fraction]
    osf = opp['stam'] / max(1, opp['sm'])  # [canonical: N/A]
    ohf = opp['hp'] / max(1, opp['hmax'])  # [canonical: N/A]

    # ── REACTIVE layer: if I can see opponent's commit, exploit it ──
    if opp_action is not None and protocol in ('ADAPTIVE','DUELLIST','COUNTER_PUNCHER','REACTIVE'):
        # I see their action and split. React optimally.
        if opp_action == 'take_breath':
            return ('strike', 0.80)  # free damage round  # [canonical: N/A — reactive protocol]
        if opp_action == 'feint':
            # They committed N dice to feint, remainder to defense.
            # Their defense is reduced. Go aggressive to punish.
            return ('strike', 0.75)  # [canonical: N/A — reactive protocol]
        if opp_action == 'taunt':
            return ('strike', 0.65)  # they're not attacking, punish  # [canonical: N/A — reactive protocol]
        if opp_action == 'full_guard':
            # They're turtling. Don't waste stamina on strikes that won't land.
            if sf > 0.4:  # [canonical: N/A — reactive protocol]
                return ('feint', 0.55)  # setup for next round
            return ('strike', 0.40)  # conserve  # [canonical: N/A — reactive protocol]
        if opp_action == 'strike' and opp_split is not None:
            if opp_split >= 0.65:  # [canonical: N/A — reactive protocol]
                # They're committed high offense. Go defensive, absorb, hold init.
                return ('strike', 0.30)  # [canonical: N/A — reactive protocol]
            elif opp_split <= 0.35:  # [canonical: N/A — reactive protocol]
                # They're defensive. I can commit more offense safely.
                return ('strike', 0.70)  # [canonical: N/A — reactive protocol]

    # ── Base protocol (non-reactive, or first declarer) ──
    if protocol == 'AGGRESSIVE': return ('strike', 0.75)  # [canonical: N/A — test protocol]
    if protocol == 'DEFENSIVE': return ('strike', 0.30)  # [canonical: N/A — test protocol]
    if protocol == 'BALANCED': return ('strike', 0.50)  # [canonical: N/A — test protocol]
    if protocol == 'FULL_GUARD': return ('full_guard', 0.0)  # [canonical: designs/scene/combat_v30.md §4]
    if protocol == 'FEINT_SPAM': return ('feint', 0.65)  # [canonical: N/A — test protocol]

    if protocol == 'FEINTER':  # [canonical: N/A — test protocol]
        if rd % 3 == 1 and me['fdeb'] == 0: return ('feint', 0.55)  # [canonical: N/A]
        return ('strike', 0.60)  # [canonical: N/A]

    if protocol == 'STAMINA_FIGHTER':  # [canonical: N/A — test protocol]
        if sf < 0.4 and not me['oob']: return ('take_breath', 0.0)  # [canonical: N/A]
        return ('strike', 0.30)  # [canonical: N/A]

    if protocol == 'ADAPTIVE':  # [canonical: N/A — test protocol]
        if sf < 0.2 and not me['oob']: return ('take_breath', 0.0)  # [canonical: N/A]
        if opp['fdeb'] > 0: return ('strike', 0.70)  # [canonical: N/A]
        if ohf < 0.3: return ('strike', 0.75)  # [canonical: N/A]
        if me['init'] and rd % 4 == 0: return ('feint', 0.50)  # [canonical: N/A]
        return ('strike', 0.50)  # [canonical: N/A]

    if protocol == 'COUNTER_PUNCHER':  # [canonical: N/A — test protocol]
        if opp['fdeb'] > 0 or ohf < 0.4: return ('strike', 0.65)  # [canonical: N/A]
        return ('strike', 0.30)  # [canonical: N/A]

    if protocol == 'DUELLIST':  # [canonical: N/A — test protocol]
        if rd == 1: return ('taunt', 0.35)  # [canonical: N/A — open with provocation]
        if opp['fdeb'] > 0 or opp['forced1st']: return ('strike', 0.65)  # [canonical: N/A]
        if me['init'] and rd % 4 == 0: return ('feint', 0.50)  # [canonical: N/A]
        if sf < 0.25: return ('take_breath', 0.0)  # [canonical: N/A]
        if rd % 4 == 1 and rd > 1: return ('taunt', 0.35)  # [canonical: N/A]
        return ('strike', 0.45)  # [canonical: N/A]

    if protocol == 'REACTIVE':  # pure reactive — defensive base, exploit with info  # [canonical: N/A]
        if sf < 0.25 and not me['oob']: return ('take_breath', 0.0)  # [canonical: N/A]
        return ('strike', 0.40)  # [canonical: N/A]

    return ('strike', 0.50)  # [canonical: N/A — fallback]

# ══ DUEL SIM v5 ══════════════════════════════════════════════════════════════

def sim(wa, aa, wb, ab, agi=4, str_=4, end=4, hist=2, cog=4, comp=5,  # [canonical: N/A — sim params]
        pa='BALANCED', pb='BALANCED', yield_at_zero=True, seed=42, maxr=30,  # [canonical: N/A]
        agi_a=None, agi_b=None, end_a=None, end_b=None,  # [canonical: N/A]
        str_a=None, str_b=None, cog_a=None, cog_b=None):  # [canonical: N/A]
    rng = np.random.default_rng(seed)  # [canonical: N/A — RNG]
    ea, eb = end_a or end, end_b or end  # [canonical: N/A]
    sa, sb = str_a or str_, str_b or str_  # [canonical: N/A]
    ag_a, ag_b = agi_a or agi, agi_b or agi  # [canonical: N/A]
    ca, cb = cog_a or cog, cog_b or cog  # [canonical: N/A]

    a = make(wa, aa, ag_a, sa, ea, hist, ca, comp)  # [canonical: N/A]
    b = make(wb, ab, ag_b, sb, eb, hist, cb, comp)  # [canonical: N/A]

    if ag_a > ag_b: a['init'] = True  # [canonical: params/combat.md §Initiative PP-232]
    elif ag_b > ag_a: b['init'] = True  # [canonical: params/combat.md §Initiative PP-232]
    else: a['init'] = bool(rng.integers(0, 2)); b['init'] = not a['init']  # [canonical: params/combat.md §PP-239]

    L = defaultdict(int)  # [canonical: N/A — log]

    for rd in range(1, maxr + 1):  # [canonical: N/A — sim loop]
        # End checks  # [canonical: designs/scene/combat_v30.md §4 — Stage 1]
        ai = a['wounds'] > a['mw'] or a['hp'] <= 0  # [canonical: designs/scene/derived_stats_v30.md §4.1]
        bi = b['wounds'] > b['mw'] or b['hp'] <= 0  # [canonical: designs/scene/derived_stats_v30.md §4.1]
        if ai and bi: L.update(rounds=rd-1, winner='draw', end_reason='mutual_incap'); break  # [canonical: N/A]
        if ai: L.update(rounds=rd-1, winner='B', end_reason='incap_A'); break  # [canonical: N/A]
        if bi: L.update(rounds=rd-1, winner='A', end_reason='incap_B'); break  # [canonical: N/A]

        if yield_at_zero:  # [canonical: N/A — E7 duel context]
            ay, by = a['oob'], b['oob']  # [canonical: N/A]
            if ay and by:
                w = 'A' if a['hp'] > b['hp'] else ('B' if b['hp'] > a['hp'] else 'draw')  # [canonical: N/A]
                L.update(rounds=rd, winner=w, end_reason='mutual_yield'); break  # [canonical: N/A]
            elif ay: L.update(rounds=rd, winner='B', end_reason='yield_A'); break  # [canonical: N/A]
            elif by: L.update(rounds=rd, winner='A', end_reason='yield_B'); break  # [canonical: N/A]

        # ── DECLARATION with initiative info advantage (canonical §3) ──
        # [canonical: designs/scene/combat_v30.md §3 — lower init declares first, higher sees split]
        a_first = not a['init']  # [canonical: designs/scene/combat_v30.md §3]
        if a['forced1st']: a_first = True  # [canonical: N/A — Taunt effect]
        b_first = not b['init']  # [canonical: designs/scene/combat_v30.md §3]
        if b['forced1st']: b_first = True  # [canonical: N/A — Taunt effect]

        if a_first and not b_first:
            # A declares blind, B sees A's commit
            act_a, split_a = choose(pa, a, b, rd, rng)  # [canonical: N/A]
            act_b, split_b = choose(pb, b, a, rd, rng, opp_action=act_a, opp_split=split_a)  # [canonical: N/A — reactive]
        elif b_first and not a_first:
            act_b, split_b = choose(pb, b, a, rd, rng)  # [canonical: N/A]
            act_a, split_a = choose(pa, a, b, rd, rng, opp_action=act_b, opp_split=split_b)  # [canonical: N/A — reactive]
        else:
            # Both forced first or both have init — simultaneous blind
            act_a, split_a = choose(pa, a, b, rd, rng)  # [canonical: N/A]
            act_b, split_b = choose(pb, b, a, rd, rng)  # [canonical: N/A]

        L[f'act_a_{act_a}'] += 1; L[f'act_b_{act_b}'] += 1  # [canonical: N/A — log]

        # ── Pool splits ──
        P_a, P_b = epool(a), epool(b)  # [canonical: params/combat.md §Pool Formula]
        off_a = max(0, int(P_a * split_a)); def_a = P_a - off_a  # [canonical: designs/scene/combat_v30.md §3]
        off_b = max(0, int(P_b * split_b)); def_b = P_b - off_b  # [canonical: designs/scene/combat_v30.md §3]

        if act_a == 'full_guard': off_a = 0; def_a = P_a  # [canonical: designs/scene/combat_v30.md §4]
        if act_b == 'full_guard': off_b = 0; def_b = P_b  # [canonical: designs/scene/combat_v30.md §4]

        nfa, nfb = 0, 0  # new feint debuffs for next round  # [canonical: N/A]
        net_a_dmg, net_b_dmg = 0, 0  # [canonical: N/A]

        # ── P1: Strike ──
        if act_a == 'strike':  # [canonical: designs/scene/combat_v30.md §4]
            h = roll(rng, max(1, off_a), a['tn']); bl = roll(rng, def_b, b['tn'])  # [canonical: params/core.md §dice engine]
            net = h - bl  # [canonical: params/combat.md §Damage Formula]
            if net > 0: dmg(b, net, a); net_a_dmg = net  # [canonical: params/combat.md §Damage Formula]
            drain(a, 'strike')  # [canonical: designs/scene/combat_v30.md §7]

        if act_b == 'strike':
            h = roll(rng, max(1, off_b), b['tn']); bl = roll(rng, def_a, a['tn'])
            net = h - bl
            if net > 0: dmg(a, net, b); net_b_dmg = net
            drain(b, 'strike')

        # ── P2: Feint (PP-294 model — NOT PP-238 Defense=0) ──
        # [canonical: designs/scene/combat_v30.md §4 PP-294 — "allocate N dice (minimum 3) to Offence
        #  for the feint; remaining dice available for Defence this round"]
        if act_a == 'feint':
            fn = max(3, off_a)  # [canonical: params/combat.md §PP-294 — minimum 3]
            # Remaining dice go to defense (PP-294, not PP-238)
            feint_def_a = P_a - fn  # [canonical: designs/scene/combat_v30.md §4 PP-294]
            def_a = max(0, feint_def_a)  # update defense for incoming strikes  # [canonical: designs/scene/combat_v30.md §4 PP-294]
            fh = roll(rng, fn, 7); od = roll(rng, def_b, 7)  # [canonical: params/combat.md §PP-294 — TN 7 vs TN 7]
            margin = fh - od  # [canonical: params/combat.md §PP-294]
            if margin > 0: nfb = margin; L['feints_landed'] += 1  # [canonical: params/combat.md §PP-294 — pool reduction]
            drain(a, 'feint')  # [canonical: designs/scene/combat_v30.md §7]

        if act_b == 'feint':
            fn = max(3, off_b)  # [canonical: params/combat.md §PP-294]
            feint_def_b = P_b - fn  # [canonical: designs/scene/combat_v30.md §4 PP-294]
            def_b = max(0, feint_def_b)  # [canonical: designs/scene/combat_v30.md §4 PP-294]
            fh = roll(rng, fn, 7); od = roll(rng, def_a, 7)  # [canonical: params/combat.md §PP-294]
            margin = fh - od  # [canonical: params/combat.md §PP-294]
            if margin > 0: nfa = margin; L['feints_landed'] += 1  # [canonical: params/combat.md §PP-294]
            drain(b, 'feint')  # [canonical: designs/scene/combat_v30.md §7]

        # ── Reactive: Take a Breath ──
        if act_a == 'take_breath':  # [canonical: designs/scene/combat_v30.md §4]
            rec = (a['end'] + a['hist']) * 2  # [canonical: designs/scene/combat_v30.md §7 — (End+hist)×2]
            a['stam'] = min(a['sm'], a['stam'] + rec)  # [canonical: N/A — cap]
            a['oob'] = a['stam'] <= 0  # [canonical: N/A]
            def_a = P_a  # all to defense while breathing  # [canonical: N/A — implied]

        if act_b == 'take_breath':
            rec = (b['end'] + b['hist']) * 2  # [canonical: designs/scene/combat_v30.md §7]
            b['stam'] = min(b['sm'], b['stam'] + rec)  # [canonical: N/A]
            b['oob'] = b['stam'] <= 0  # [canonical: N/A]
            def_b = P_b  # [canonical: N/A]

        # ── Taunt (duel context — Cognition vs Composure, cost 5) ──
        if act_a == 'taunt':  # [canonical: N/A — new duel action]
            th = roll(rng, ca, 7); rh = roll(rng, b['comp'], 7)  # [canonical: N/A — Cog vs Comp]
            if th > rh: b['forced1st'] = True; L['taunts_landed'] += 1  # [canonical: N/A]
            drain(a, 'taunt')  # [canonical: N/A]

        if act_b == 'taunt':
            th = roll(rng, cb, 7); rh = roll(rng, a['comp'], 7)  # [canonical: N/A]
            if th > rh: a['forced1st'] = True; L['taunts_landed'] += 1  # [canonical: N/A]
            drain(b, 'taunt')  # [canonical: N/A]

        if act_a == 'full_guard': drain(a, 'full_guard')  # [canonical: designs/scene/combat_v30.md §4]
        if act_b == 'full_guard': drain(b, 'full_guard')  # [canonical: designs/scene/combat_v30.md §4]

        # ── Initiative transfer ──
        # [canonical: designs/scene/combat_v30.md §3 — transfers to exchange winner]
        if net_a_dmg > 0 and net_b_dmg == 0: a['init'] = True; b['init'] = False  # [canonical: designs/scene/combat_v30.md §3]
        elif net_b_dmg > 0 and net_a_dmg == 0: b['init'] = True; a['init'] = False  # [canonical: designs/scene/combat_v30.md §3]

        a['fdeb'] = nfa; b['fdeb'] = nfb  # [canonical: params/combat.md §PP-294]
        a['forced1st'] = False; b['forced1st'] = False  # [canonical: N/A — clear round effects]
    else:
        if a['hp'] > b['hp']: L.update(rounds=maxr, winner='A', end_reason='timeout')  # [canonical: N/A]
        elif b['hp'] > a['hp']: L.update(rounds=maxr, winner='B', end_reason='timeout')  # [canonical: N/A]
        else: L.update(rounds=maxr, winner='draw', end_reason='timeout')  # [canonical: N/A]

    L['a_hp'] = a['hp']; L['b_hp'] = b['hp']  # [canonical: N/A — log]
    L['a_w'] = a['wounds']; L['b_w'] = b['wounds']  # [canonical: N/A]
    L['a_s'] = a['stam']; L['b_s'] = b['stam']  # [canonical: N/A]
    return L

# ══ RUNNER ═══════════════════════════════════════════════════════════════════

def run(label, N, **kw):  # [canonical: N/A — test runner]
    wa, wb, dr = {'A':0,'B':0,'draw':0}, defaultdict(int), []  # [canonical: N/A]
    aw, bw, ast, bst, fl, tl = [], [], [], [], [], []  # [canonical: N/A]
    for i in range(N):  # [canonical: N/A]
        r = sim(seed=1000000+i, **kw)  # [canonical: N/A — RNG seed]
        w = r.get('winner','draw'); wa[w] += 1  # [canonical: N/A]
        wb[r.get('end_reason','?')] += 1  # [canonical: N/A]
        dr.append(r.get('rounds', 30))  # [canonical: N/A]
        aw.append(r.get('a_w',0)); bw.append(r.get('b_w',0))  # [canonical: N/A]
        ast.append(r.get('a_s',0)); bst.append(r.get('b_s',0))  # [canonical: N/A]
        fl.append(r.get('feints_landed',0)); tl.append(r.get('taunts_landed',0))  # [canonical: N/A]
    ra = np.array(dr)  # [canonical: N/A]
    rs = ', '.join(f"{k}:{v}" for k,v in sorted(wb.items()))  # [canonical: N/A]
    print(f"\n{'='*74}\n  {label}  (N={N})\n{'='*74}")  # [canonical: N/A — output]
    print(f"  A:{wa['A']/N:.1%}  B:{wa['B']/N:.1%}  D:{wa['draw']/N:.1%}")  # [canonical: N/A — output]
    print(f"  Rounds: {ra.mean():.1f}±{ra.std():.1f} [{ra.min()}–{ra.max()}]  End: {rs}")  # [canonical: N/A — output]
    print(f"  Wounds: A {np.mean(aw):.1f} B {np.mean(bw):.1f} | Stam: A {np.mean(ast):.1f} B {np.mean(bst):.1f}")  # [canonical: N/A — output]
    if sum(fl)>0: print(f"  Feints: {np.mean(fl):.2f}/duel")  # [canonical: N/A — output]
    if sum(tl)>0: print(f"  Taunts: {np.mean(tl):.2f}/duel")  # [canonical: N/A — output]

# ══ RUN ══════════════════════════════════════════════════════════════════════

N = 5000  # [canonical: N/A — simulation parameter]
B = dict(agi=4, str_=4, end=4, hist=2)  # [canonical: N/A — test stats]
W = 'ShortHeavyBlade'  # [canonical: N/A — default weapon]

print("=" * 74)  # [canonical: N/A — output]
print("  v5 — INITIATIVE INFO ADVANTAGE + PP-294 FEINT (defense retained)")  # [canonical: N/A — output]
print("=" * 74)  # [canonical: N/A — output]

# §1: POOL SPLIT — does initiative info advantage change the dynamics?
print("\n~~~ §1: POOL SPLIT + INITIATIVE INFO ~~~")  # [canonical: N/A — output]
run("Aggressive vs Defensive", N, wa=W, aa='None', wb=W, ab='None', pa='AGGRESSIVE', pb='DEFENSIVE', **B)
run("Aggressive vs Reactive (has info)", N, wa=W, aa='None', wb=W, ab='None', pa='AGGRESSIVE', pb='REACTIVE', **B)
run("Reactive vs Aggressive", N, wa=W, aa='None', wb=W, ab='None', pa='REACTIVE', pb='AGGRESSIVE', **B)
run("Reactive vs Reactive", N, wa=W, aa='None', wb=W, ab='None', pa='REACTIVE', pb='REACTIVE', **B)
run("Adaptive vs Adaptive", N, wa=W, aa='None', wb=W, ab='None', pa='ADAPTIVE', pb='ADAPTIVE', **B)

# §2: FEINT WITH RETAINED DEFENSE (PP-294)
print("\n~~~ §2: FEINT (PP-294 — defense retained) ~~~")  # [canonical: N/A — output]
run("Feinter vs Balanced", N, wa=W, aa='None', wb=W, ab='None', pa='FEINTER', pb='BALANCED', **B)
run("Feinter vs Adaptive", N, wa=W, aa='None', wb=W, ab='None', pa='FEINTER', pb='ADAPTIVE', **B)
run("Feint-spam vs Balanced", N, wa=W, aa='None', wb=W, ab='None', pa='FEINT_SPAM', pb='BALANCED', **B)

# §3: TAUNT (cost 5, with info advantage)
print("\n~~~ §3: TAUNT (cost=5, info advantage modeled) ~~~")  # [canonical: N/A — output]
run("Duellist vs Balanced", N, wa=W, aa='None', wb=W, ab='None', pa='DUELLIST', pb='BALANCED', **B)
run("Duellist vs Adaptive", N, wa=W, aa='None', wb=W, ab='None', pa='DUELLIST', pb='ADAPTIVE', **B)
run("Duellist vs Aggressive", N, wa=W, aa='None', wb=W, ab='None', pa='DUELLIST', pb='AGGRESSIVE', **B)
run("Duellist vs Stamina-fighter", N, wa=W, aa='None', wb=W, ab='None', pa='DUELLIST', pb='STAMINA_FIGHTER', **B)
run("Duellist vs Counter-puncher", N, wa=W, aa='None', wb=W, ab='None', pa='DUELLIST', pb='COUNTER_PUNCHER', **B)
run("Duellist (COG 6) vs Adaptive", N, wa=W, aa='None', wb=W, ab='None', pa='DUELLIST', pb='ADAPTIVE', cog_a=6, **B)  # [canonical: N/A — test stats]  # [canonical: N/A — test stats]

# §4: STAT ASYMMETRY
print("\n~~~ §4: STAT ASYMMETRY ~~~")  # [canonical: N/A — output]
run("Agi 5v3", N, wa=W, aa='None', wb=W, ab='None', pa='ADAPTIVE', pb='ADAPTIVE', agi_a=5, agi_b=3, **B)  # [canonical: N/A — test stats]
run("End 6v3", N, wa=W, aa='None', wb=W, ab='None', pa='ADAPTIVE', pb='ADAPTIVE', end_a=6, end_b=3, **B)  # [canonical: N/A — test stats]
run("End 5v4", N, wa=W, aa='None', wb=W, ab='None', pa='ADAPTIVE', pb='ADAPTIVE', end_a=5, end_b=4, **B)  # [canonical: N/A — test stats]
run("STR 6v3", N, wa=W, aa='None', wb=W, ab='None', pa='ADAPTIVE', pb='ADAPTIVE', str_a=6, str_b=3, **B)  # [canonical: N/A — test stats]

# §5: WEAPONS
print("\n~~~ §5: WEAPONS ~~~")  # [canonical: N/A — output]
run("Dagger TN5 vs Longsword TN7", N, wa='ShortLightBlade', aa='None', wb='LongHeavyBlade', ab='None', pa='ADAPTIVE', pb='ADAPTIVE', **B)
run("Arming sword TN6 vs Warhammer TN8", N, wa='ShortHeavyBlade', aa='None', wb='LongHeavyBlunt', ab='None', pa='ADAPTIVE', pb='ADAPTIVE', **B)

# §6: BUILD MATCHUPS
print("\n~~~ §6: BUILD MATCHUPS ~~~")  # [canonical: N/A — output]
run("Duellist (COG6,Agi5,End3) vs Brawler (STR6,End5,Agi3)", N,  # [canonical: N/A — test builds]
    wa='ShortLightBlade', aa='None', wb='ShortHeavyBlunt', ab='Medium',
    pa='DUELLIST', pb='AGGRESSIVE',
    agi_a=5, cog_a=6, end_a=3, str_a=3,  # [canonical: N/A — test stats]
    agi_b=3, str_b=6, end_b=5, cog_b=3, **B)  # [canonical: N/A — test stats]

run("Counter-puncher (End6,Agi3) vs Aggressor (Agi5,End3)", N,  # [canonical: N/A — test builds]
    wa='ShortHeavyBlade', aa='Light', wb='ShortLightBlade', ab='None',
    pa='COUNTER_PUNCHER', pb='AGGRESSIVE',
    end_a=6, agi_a=3, str_a=4,  # [canonical: N/A — test stats]
    agi_b=5, end_b=3, str_b=3, **B)  # [canonical: N/A — test stats]

print("\n" + "=" * 74)  # [canonical: N/A — output]
print("  FINDINGS")  # [canonical: N/A — output]
print("=" * 74)  # [canonical: N/A — output]
