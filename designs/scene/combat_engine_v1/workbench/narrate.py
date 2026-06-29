"""Human-digestible narration of one traced fight (WS-6 workbench, panel 2).

Turns the engine's event stream into a beat-by-beat account a person can read, annotating each
probabilistic node with the ALTERNATE branches and their odds — so you see both what happened (n=1)
and what else could have (the local distribution). This is the text backbone the visual workbench renders;
it is also runnable standalone:  python -m workbench.narrate  (from the engine dir)."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import probabilities as P

BANNER = "n = 1  —  ONE OUTCOME, NOT A PROBABILITY"
_RULE = "=" * 78


def _pct(p):
    return f"{round(100 * p):d}%"


def _dist(d, order=None):
    items = [(k, d[k]) for k in (order or d)] if order else list(d.items())
    return " · ".join(f"{k} {_pct(v)}" for k, v in items)


def _sig(x):
    return f"{x:+.2f} sig"


def render(events, seed=None):
    """Render the captured event stream to a readable multi-line string."""
    out = []
    a_label = b_label = None
    DEGORD = ['fail', 'partial', 'success', 'overwhelming']

    def line(s=""):
        out.append(s)

    for ev in events:
        k = ev['kind']
        if k == 'fight_start':
            a_label, b_label = ev['A'], ev['B']
            line(_RULE)
            line(f"  SCENE COMBAT TRACE   ·   {BANNER}" + (f"   ·   seed {seed}" if seed is not None else ""))
            line(_RULE)
            line(f"  {ev['A']:<8} — {ev['weapon_A']}, {ev['armor_A']} armour, {ev['tradition_A']} tradition")
            line(f"  {ev['B']:<8} — {ev['weapon_B']}, {ev['armor_B']} armour, {ev['tradition_B']} tradition")
            line()
        elif k == 'turn_start':
            line(f"  Turn {ev['turn']} — {ev['first']} moves first.")
        elif k == 'engagement_start':
            if ev['closed']:
                line(f"    they begin already closed (measure {ev['measure_gap']})")
            else:
                line(f"    they begin at measure (gap {ev['measure_gap']}; {ev['longer']} has the longer reach)")
        elif k == 'approach':
            d = P.node_distribution(ev)
            tag = "  -> just closed" if ev.get('just_closed') else ""
            line(f"      {ev['shorter']} closes (gap {ev['gap']}, {ev['close_rate']}/beat); "
                 f"{ev['longer']} stop-hit chance {_pct(ev['stophit_p'])}{tag}")
        elif k == 'stophit':
            landed = ev['degree'] in ('success', 'overwhelming')
            verb = f"LANDS ({ev['degree']})" if landed else f"misses ({ev['degree']})"
            line(f"      stop-hit from {ev['longer']} {verb}   "
                 f"[{_dist(P.degree_distribution(ev['pool'], ev['net_sigma']), DEGORD)}]")
        elif k == 'commit':
            line(f"    · {ev['aggressor']} commits {ev['commit']}   "
                 f"[bands {_dist(P.beta_band_probs(ev['beta_a'], ev['beta_b']))}]")
        elif k == 'read':
            res = "READS it (Vor steal opens)" if ev['read_win'] else "misses the read (acts on instinct)"
            line(f"        {ev['defender']}'s read: {_pct(ev['p_read_win'])} to catch it … {res}")
        elif k == 'mode':
            how = "" if ev['chosen_by'] == 'read' else "  (guessing — read missed)"
            verb = {'parry': 'parries', 'dodge': 'dodges', 'wind': 'winds into the bind'}[ev['mode']]
            line(f"        {ev['defender']} {verb}{how}")
        elif k == 'roll':
            line(f"        {ev['aggressor']} resolves: pool {ev['pool']}, edge {_sig(ev['net_sigma'])} -> "
                 f"{ev['degree'].upper()}   [{_dist(P.degree_distribution(ev['pool'], ev['net_sigma']), DEGORD)}]")
        elif k == 'outcome':
            wounds = f"({a_label} {ev['A_wounds']} / {b_label} {ev['B_wounds']} wounds)"
            if ev['hit'] > 0:
                line(f"        -> {ev['aggressor']} lands a hit on {ev['defender']}  {wounds}")
            elif ev['bind']:
                line(f"        -> blades lock in a bind  {wounds}")
            elif ev['riposte']:
                line(f"        -> {ev['defender']} ripostes — initiative flips  {wounds}")
            else:
                line(f"        -> clean defence, no effect  {wounds}")
        elif k == 'engagement_end':
            if ev['felled']:
                line(f"    — engagement ends: {ev['felled']} is felled")
            else:
                line(f"    — they separate (no decision this turn)")
            line()
        elif k == 'fight_result':
            if ev['winner']:
                line(f"  RESULT: {ev['winner']} wins.   [{BANNER}]")
            else:
                line(f"  RESULT: unresolved — neither fighter fell.   [{BANNER}]")
            line(_RULE)
    return "\n".join(out)


if __name__ == '__main__':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass
    import numpy as np
    from combatant import Combatant
    from trace import run_traced_fight
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    A = Combatant('Bryn', weapon='arming', tradition='italian')
    B = Combatant('Halla', weapon='longsword', tradition='german')
    result, events = run_traced_fight(A, B, seed=seed)
    print(render(events, seed=seed))
