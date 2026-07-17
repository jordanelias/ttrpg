"""Sports-commentator transcript of a traced fight (WS-6) — legible play-by-play + the mechanics underneath.

Turns the engine's event stream into a flowing call of the action, and for every beat says BOTH what happened
(the commentator line) AND the specific mechanical interaction driving it (what commit-depth means, why the read
mattered, what a bind contests, where the initiative/Vor swung). Shared by the CLI narrator and the workbench.

Each beat of a closed exchange weaves five engine decisions into one call: commit-depth -> read -> defence-mode
-> resolution roll -> outcome. The `mech` note names the levers; the `branches` carry the odds for the explorer.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
import probabilities as P

# ---- how the engine's numbers read in plain language -----------------------------------------------------
COMMIT_LINE = {
    'feint': "{a} flicks out a light feint — a threat {a} can fully pull back",
    'light': "{a} commits to a clean, measured strike",
    'committed': "{a} drives in hard, putting weight behind it",
    'all-in': "{a} throws everything into one all-out blow — no taking it back now",
}
COMMIT_MECH = {
    'feint': "the FEINT pole (commit ~{c}): minimal commitment, FULL recovery — near-zero exposure, {a} can abort and reset (to commit is to give up recovery; here {a} gives up almost none)",
    'light': "a measured commit (~{c}): a balanced trade of power for recoverability",
    'committed': "a deep commit (~{c}): more power and reach but LESS recoverable — the exposure window opens (the Indes counter), scaled by how hard {a}'s weapon is to retract (a hand-balanced blade recovers; a forward-heavy one can't)",
    'all-in': "all-in (commit ~{c}): maximum power, but committed = IRRECOVERABLE — {a} can't stop or retract it, so a clean read by {d} flips the whole exchange",
}
def _commit_band(commit):
    return 'feint' if commit < 2.75 else 'light' if commit < 3.5 else 'committed' if commit < 4.25 else 'all-in'
MODE_LINE = {
    'parry': "{d} sweeps the blade aside with a parry",
    'dodge': "{d} slips off the line of attack",
    'wind':  "{d} meets the blade and winds into a bind",
}
DEG_LINE = {  # the attacker's roll, before the defender's mode decides the outcome
    'fail': "the attack is read and smothered",
    'partial': "it only half-lands",
    'success': "it comes through cleanly",
    'overwhelming': "it lands with crushing force",
}


def _who(events):
    fs = next((e for e in events if e['kind'] == 'fight_start'), None)
    return (fs['A'], fs['B']) if fs else ('A', 'B')


def commentate(events, cfg):
    """Return a list of transcript entries: {type, line, mech?, branches?, cls?}."""
    a_label, b_label = _who(events)
    out, cur = [], {}

    def wound_str(e):
        return f"{a_label} {e['A_wounds']}w / {b_label} {e['B_wounds']}w"

    for e in events:
        k = e['kind']
        if k == 'fight_start':
            out.append({'type': 'header',
                        'line': f"{e['A']} ({e['weapon_A']}, {e['tradition_A']}) faces {e['B']} ({e['weapon_B']}, {e['tradition_B']}).",
                        'mech': "Each fights to fell the other; wounds and fatigue carry across the whole bout."})
        elif k == 'turn_start':
            out.append({'type': 'turn', 'line': f"Turn {e['turn']}. {e['first']} has the first move."})
        elif k == 'engagement_start':
            if e['closed']:
                out.append({'type': 'measure', 'line': "They start already at close quarters, blades almost touching.",
                            'mech': "measure <= 0.3: the fight opens closed — straight to the tempo-gated exchange."})
            else:
                out.append({'type': 'measure',
                            'line': f"They square off at distance — {e['longer']} holds the longer reach, {e['shorter']} must close.",
                            'mech': f"measure gap {e['measure_gap']}: {e['shorter']} has to cross the point to land; {e['longer']} can threaten on the way in."})
        elif k == 'approach':
            line = f"{e['shorter']} steps in" + (" and closes the distance" if e.get('just_closed') else ", working past the point")
            mech = f"closing at {e['close_rate']}/beat; {e['longer']} has a {round(e['stophit_p']*100)}% shot at a stop-hit as {e['shorter']} comes in"
            out.append({'type': 'approach', 'line': line + ".", 'mech': mech,
                        'branches': [{'label': 'longer lands a stop-hit', 'dist': P.node_distribution(e), 'took': None}] if e.get('stophit_p') else None})
        elif k == 'stophit':
            landed = e['degree'] in ('success', 'overwhelming')
            out.append({'type': 'approach',
                        'line': (f"{e['longer']} lances out as {e['shorter']} closes — and catches them!" if landed
                                 else f"{e['longer']} thrusts to keep {e['shorter']} off, but it's slipped."),
                        'mech': f"stop-hit roll {e['degree']} (pool {e['pool']}D, edge {e['net_sigma']:+}sig)",
                        'cls': 'hit' if landed else 'clean'})
        elif k == 'commit':
            cur = {'a': e['aggressor'], 'd': e['defender'], 'commit': e['commit'], 'beta_a': e['beta_a'], 'beta_b': e['beta_b']}
        elif k == 'read':
            cur['read_win'] = e['read_win']; cur['read_p'] = e['p_read_win']; cur['read_d'] = e['read_d']; cur['read_a'] = e['read_a']
        elif k == 'mode':
            cur['mode'] = e['mode']; cur['chosen_by'] = e['chosen_by']
        elif k == 'roll':
            cur['pool'] = e['pool']; cur['net_sigma'] = e['net_sigma']; cur['degree'] = e['degree']
        elif k == 'outcome':
            out.append(_beat(cur, e, cfg, wound_str))
            cur = {}
        elif k == 'separation':
            reasons = {'collapse': "both are spent — they fall apart, gasping",
                       'burst_ceiling': "the flurry burns out and they break",
                       'clean_defence': "the exchange resolves cleanly and the measure breaks",
                       'beat_exhaustion': "the moment passes and they reset"}
            out.append({'type': 'sep', 'line': reasons.get(e['reason'], "they separate") + ".",
                        'mech': f"engagement ends: {e['reason']} (no decision this turn; wounds/fatigue persist)"})
        elif k == 'engagement_end':
            if e['felled']:
                out.append({'type': 'sep', 'line': f"{e['felled']} goes down — they can't continue.", 'cls': 'felled',
                            'mech': "wounds crossed the felled threshold (Max Wounds + 1)."})
        elif k == 'fight_result':
            if e['winner']:
                out.append({'type': 'result', 'line': f"It's over — {e['winner']} takes it.",
                            'mech': "decided by a felling (a 5% upset chance is always live, so nothing is certain)."})
            else:
                out.append({'type': 'result', 'line': "Time — neither could put the other down. No decision.",
                            'mech': "12 turns elapsed with no felling: a legitimate draw (no wound-count tiebreak)."})
    return out


def _beat(cur, outcome, cfg, wound_str):
    """Weave one closed exchange (commit -> read -> mode -> roll -> outcome) into a call + mechanics + odds."""
    a, d = cur['a'], cur['d']
    commit, mode = cur['commit'], cur.get('mode', 'parry')
    rw, rp = cur.get('read_win', False), cur.get('read_p', 0.5)
    deg = cur.get('degree', 'fail')

    # the call: attack -> read -> defence -> result
    band = _commit_band(commit)
    call = COMMIT_LINE[band].format(a=a)
    if rw:
        call += f", but {d} sees it coming — " + MODE_LINE[mode].format(d=d)
    else:
        call += f", and {d} is caught guessing — " + MODE_LINE[mode].format(d=d) + " on instinct"

    hit, bind, rip = outcome['hit'], outcome['bind'], outcome['riposte']
    if hit > 0:
        call += f". {DEG_LINE[deg]}, and {a} draws blood!"
        cls = 'hit'
    elif bind:
        call += ". Their blades lock together."
        cls = 'bind'
    elif rip:
        call += f". {d} turns it around — riposte! The initiative flips."
        cls = 'riposte'
    else:
        call += f". {d} turns it aside."
        cls = 'clean'

    # the mechanics underneath
    mech = [COMMIT_MECH[band].format(a=a, d=d, c=round(commit, 1))]
    if rw:
        mech.append(f"the read: {d} out-reads the attack ({round(rp*100)}% to read it) — so {d} picks the BEST defence (not a guess)" +
                    (f", and since {a} committed deep, {d} can steal the initiative (Vor)" if commit >= 4 else ""))
    else:
        mech.append(f"the read: {a} hid the intent ({d} only had {round(rp*100)}% to read it) — {d} must pick a defence blind (random mode)")
    mech.append({'parry': "parry = deflect with the blade (wants hand-guard)",
                 'dodge': "dodge = void the line with footwork (wants balance)",
                 'wind': "wind = meet and dominate the bind (wants blade-guard + leverage)"}[mode])
    mech.append(f"resolution: pool {cur.get('pool','?')}D, net edge {cur.get('net_sigma',0):+}sig -> {deg.upper()}")
    if hit > 0:
        mech.append(f"{deg} beat {d}'s defence: wound applied ({wound_str(outcome)}); the initiative (Vor) swings to {a}")
    elif bind:
        mech.append("bind entry: whoever dominates the crossing (leverage + tactile feel — the German Fuehlen) steals the Vor through the contact")
    elif rip:
        mech.append(f"{d}'s defence beat the attack: ROLE FLIP — {d} is now the aggressor and presses")
    else:
        mech.append(f"defence held: no wound ({wound_str(outcome)})")

    # odds for the explorer
    branches = [
        {'label': 'how deep ' + a + ' committed', 'dist': P.beta_band_probs(cur['beta_a'], cur['beta_b']),
         'took': band},
        {'label': 'the read', 'dist': {f'{d} reads it': round(rp, 3), f'{a} hides it': round(1 - rp, 3)},
         'took': f'{d} reads it' if rw else f'{a} hides it'},
        {'label': 'the resolution roll', 'dist': P.degree_distribution(cur.get('pool', 5), cur.get('net_sigma', 0.0)),
         'took': deg, 'dist2': {dg: P.outcome_distribution(dg, mode, cfg) for dg in ('fail', 'partial', 'success', 'overwhelming')}},
    ]
    return {'type': 'beat', 'line': call, 'mech': mech, 'branches': branches, 'cls': cls}


def render_text(entries):
    """Plain-text transcript for the CLI: the call, then the mechanics indented under it."""
    lines = []
    for e in entries:
        t = e['type']
        if t == 'header':
            lines += ["=" * 78, "  COMMENTARY  [n=1 — one outcome, not a probability]", "=" * 78, "  " + e['line']]
        elif t == 'turn':
            lines += ["", "  >> " + e['line']]
        elif t == 'result':
            lines += ["", "  ** " + e['line'] + " **"]
        else:
            lines.append("     " + e['line'])
        if e.get('mech'):
            for m in (e['mech'] if isinstance(e['mech'], list) else [e['mech']]):
                lines.append("        - " + m)
    return "\n".join(lines)


if __name__ == '__main__':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
    import config
    from combatant import Combatant
    from trace import run_traced_fight
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    A = Combatant('Bryn', weapon='arming', tradition='italian')
    B = Combatant('Halla', weapon='longsword', tradition='german')
    _, events = run_traced_fight(A, B, seed=seed)
    print(render_text(commentate(events, config.CFG)))
