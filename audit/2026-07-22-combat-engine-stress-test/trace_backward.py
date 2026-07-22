"""Explicit-trace + backward-causal analysis of simulated battles (2026-07-22).

(1) TRACE EVERYTHING CONSUMED: wires the engine's `_TRACE` seam + spies on `assemble_net_sigma` (the net-σ
    decomposition each roll consumes) and `core.strike` (the damage inputs), so every input every decision node
    reads is captured — reach/measure, stop-hit p, commit depth + Beta, read margins, mode σ's, the net-σ
    components, the roll, the blow.
(2) BACKWARD ANALYSIS: from each battle's terminal state (the felling blow, or the draw reason) it walks the
    causal chain in REVERSE to the origin — decisive blow → its roll (net, degree) → the net-σ components that
    built it → the commit/read/mode that fed it → the range/approach that set it → the engagement origin.

Report-only; spies are in-process. Run:  python trace_backward.py
"""
import sys, os, random
ENG = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'systems', 'combat', 'combat_engine_v1'))
sys.path.insert(0, ENG); sys.path.insert(0, os.path.join(ENG, 'workbench'))
import wrapper, core, combat_systems as S  # noqa: E402
from combatant import Combatant  # noqa: E402
from config import CFG  # noqa: E402

def traced_fight(specA, specB, seed):
    """Run one fight capturing a unified, ordered event log with every consumed input."""
    ev = []
    wrapper._TRACE = ev.append
    _oa = S.assemble_net_sigma
    def spy_ns(atk, dsig, reach, adef, init, agg, dfd, cfg):
        ev.append(dict(kind='netsig', agg=agg.label, atk_sig=round(atk, 3), dsig=round(dsig, 3),
                       reach_pen=round(reach, 3), adef=round(adef, 3), init_edge=round(init, 3)))
        return _oa(atk, dsig, reach, adef, init, agg, dfd, cfg)
    _os = core.strike
    def spy_strike(att, dfd, deg, close, cfg, net=None, pool=None):
        d = _os(att, dfd, deg, close, cfg, net=net, pool=pool)
        ev.append(dict(kind='strike', attacker=att.label, defender=dfd.label, deg=deg,
                       head=getattr(att, 'sel_head', None) or att.head, dmg=d,
                       def_armor=dfd.armor, def_wounds=dfd.wt.wounds, def_felled=dfd.felled))
        return d
    S.assemble_net_sigma = spy_ns; core.strike = spy_strike
    try:
        A = Combatant('LS', **specA); B = Combatant('AR', **specB)
        wrapper.fight(A, B, CFG, random.Random(seed))
    finally:
        wrapper._TRACE = None; S.assemble_net_sigma = _oa; core.strike = _os
    return ev

def summarize_forward(ev, limit_turns=2):
    """Compact forward trace: the consumed inputs at each node, for the first couple of turns."""
    out = []; turn = 0
    for e in ev:
        k = e['kind']
        if k == 'fight_start':
            out.append(f"FIGHT {e['A']}({e['weapon_A']}/{e['armor_A']}) vs {e['B']}({e['weapon_B']}/{e['armor_B']})")
        elif k == 'turn_start':
            turn = e['turn']
            if turn <= limit_turns: out.append(f"  turn {turn} (first={e['first']})")
        elif turn > limit_turns:
            continue
        elif k == 'engagement_start':
            out.append(f"    engage: longer={e['longer']} reach {e['reach_A']}/{e['reach_B']} gap={e['measure_gap']} closed={e['closed']}")
        elif k == 'approach':
            out.append(f"    approach b{e['beat']}: gap={e['gap']} close_rate={e['close_rate']} stophit_p={e['stophit_p']} just_closed={e['just_closed']}")
        elif k == 'stophit':
            out.append(f"      STOPHIT {e['longer']}->{e['shorter']} pool={e['pool']} netσ={e['net_sigma']} net={e['net']} → {e['degree']}")
        elif k == 'commit':
            out.append(f"    commit[{e['aggressor']}]={e['commit']} (Beta {e['beta_a']}/{e['beta_b']} lean={e['stance_lean']})")
        elif k == 'read':
            out.append(f"      read[def={e['defender']}]: read_d={e['read_d']} read_a={e['read_a']} p={e['p_read_win']} → win={e['read_win']}")
        elif k == 'mode':
            out.append(f"      mode[def={e['defender']}]={e['mode']} ({e['chosen_by']}) σ={e['msig']}")
        elif k == 'netsig':
            out.append(f"      netσ[{e['agg']}]: atk={e['atk_sig']} def={e['dsig']} reach={e['reach_pen']} adef={e['adef']} init={e['init_edge']}")
        elif k == 'roll':
            out.append(f"    ROLL[{e['aggressor']}] pool={e['pool']} netσ={e['net_sigma']} net={e['net']} → {e['degree']} (mode {e['mode']})")
        elif k == 'strike':
            out.append(f"      STRIKE {e['attacker']}→{e['defender']} {e['deg']} head={e['head']} dmg={e['dmg']} → wounds={e['def_wounds']} felled={e['def_felled']}")
        elif k == 'outcome':
            out.append(f"    outcome: hit={e['hit']} bind={e['bind']} riposte={e['riposte']} wounds A={e['A_wounds']} B={e['B_wounds']}")
        elif k == 'contact':
            out.append(f"      CONTACT {e['actor']}→{e['opponent']} {e['outcome']} gsig={e['gsig']}")
        elif k == 'separation':
            if turn <= limit_turns: out.append(f"    separation: {e['reason']}")
        elif k == 'engagement_end':
            out.append(f"    engagement_end turn {e['turn']} felled={e['felled']}")
    return "\n".join(out)

def backward(ev):
    """Walk from the terminal state back to origin, reconstructing the causal chain of the decision."""
    from collections import Counter
    res = next((e for e in ev if e['kind'] == 'fight_result'), None)
    winner = res['winner'] if res else None
    lines = [f"OUTCOME: winner={winner} (result={res['result'] if res else '?'})"]
    rolls = [e for e in ev if e['kind'] == 'roll']
    stoph = [e for e in ev if e['kind'] == 'stophit']
    agg_beats = Counter(e['aggressor'] for e in rolls)
    # felling is detected from the POST-apply engagement_end (strike's own def_felled is pre-wound-apply)
    felled_end = next((i for i, e in enumerate(ev) if e['kind'] == 'engagement_end' and e['felled']), None)
    if felled_end is None:
        reasons = [e['reason'] for e in ev if e['kind'] == 'separation']
        lines.append(f"  DRAWN/UNDECIDED (no fighter felled). separations: {dict(Counter(reasons))}")
        lines.append(f"  attacking beats {dict(agg_beats)} + stop-hits {len(stoph)} — volume/attrition asymmetry, no decisive gate crossed")
        return "\n".join(lines)
    loser = ev[felled_end]['felled']
    di = next((j for j in range(felled_end, -1, -1) if ev[j]['kind'] == 'strike' and ev[j]['defender'] == loser), None)
    if di is None:
        lines.append(f"  felled={loser} but no strike captured (bind/contact path)"); return "\n".join(lines)
    blow = ev[di]
    lines.append(f"  ← FELLING BLOW: {blow['attacker']}→{blow['defender']} {blow['deg']} head={blow['head']} dmg={blow['dmg']} (def had {blow['def_wounds']} wounds)")
    # the roll that produced it = last 'roll' before di
    roll = next((ev[j] for j in range(di, -1, -1) if ev[j]['kind'] == 'roll'), None)
    if roll:
        lines.append(f"    ← from ROLL[{roll['aggressor']}] net={roll['net']} vs Ob → {roll['degree']} (pool={roll['pool']} netσ={roll['net_sigma']}, mode={roll['mode']})")
    ns = next((ev[j] for j in range(di, -1, -1) if ev[j]['kind'] == 'netsig'), None)
    if ns:
        lines.append(f"    ← net-σ built from: attack={ns['atk_sig']} defence={ns['dsig']} reach={ns['reach_pen']} armour-defeat={ns['adef']} initiative={ns['init_edge']}")
    cm = next((ev[j] for j in range(di, -1, -1) if ev[j]['kind'] == 'commit'), None)
    rd = next((ev[j] for j in range(di, -1, -1) if ev[j]['kind'] == 'read'), None)
    md = next((ev[j] for j in range(di, -1, -1) if ev[j]['kind'] == 'mode'), None)
    if cm: lines.append(f"    ← aggressor committed depth={cm['commit']} (lean={cm['stance_lean']})")
    if rd and md: lines.append(f"    ← defender read {'WON' if rd['read_win'] else 'LOST'} (p={rd['p_read_win']}) → mode={md['mode']} ({md['chosen_by']})")
    # origin: the engagement_start for the felling turn
    est = None
    for j in range(di, -1, -1):
        if ev[j]['kind'] == 'engagement_start': est = ev[j]; break
    if est:
        lines.append(f"    ← ORIGIN: {est['aggressor']} opened vs {est['defender']}; longer={est['longer']} reach {est['reach_A']}/{est['reach_B']} gap={est['measure_gap']} closed={est['closed']}")
    # volume context
    rolls = [e for e in ev if e['kind'] == 'roll']
    from collections import Counter
    agg_beats = Counter(e['aggressor'] for e in rolls)
    lines.append(f"    context: total attacking beats {dict(agg_beats)}")
    return "\n".join(lines)

CASES = [
    ('HALF-SWORD LOSS (longsword vs arming, both heavy plate)',
     dict(weapon='longsword', armor='heavy'), dict(weapon='arming', armor='heavy'), 'LS-lost'),
    ('REACH WIN (spear vs arming, both none)',
     dict(weapon='spear', armor='none'), dict(weapon='arming', armor='none'), 'LS-won'),
    ('GAP-THRUST DAGGER vs PLATE (rondel vs arming, both heavy)',
     dict(weapon='rondel', armor='heavy'), dict(weapon='arming', armor='heavy'), 'LS-won'),
]

if __name__ == '__main__':
    for title, sa, sb, want in CASES:
        # find a seed matching the wanted outcome (LS=A: result +1 = LS won, -1 = LS lost, 0 = draw)
        chosen = None
        for seed in range(200):
            ev = traced_fight(sa, sb, seed)
            r = next((e['result'] for e in ev if e['kind'] == 'fight_result'), 0)
            if (want == 'LS-won' and r == 1) or (want == 'LS-lost' and r == -1) or (want == 'draw' and r == 0):
                chosen = (seed, ev); break
        print('=' * 100); print(title, f'(seed {chosen[0] if chosen else "?"})'); print('=' * 100)
        if not chosen:
            print(f'  no {want} outcome in 200 seeds\n'); continue
        seed, ev = chosen
        print('--- FORWARD TRACE (every consumed input, first 2 turns) ---')
        print(summarize_forward(ev))
        print('\n--- BACKWARD CAUSAL CHAIN (terminal → origin) ---')
        print(backward(ev)); print()
