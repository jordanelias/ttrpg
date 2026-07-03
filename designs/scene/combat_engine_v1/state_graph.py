"""state_graph.py — the engagement/fight state graph as DATA (scene-combat WS-1).

The canonical engine's control flow (wrapper.fight -> wrapper.engagement) expressed as a single declarative
STATES dict, modelled on tests/sim/v32-combat-balance/m4a_bout_state_graph.py's ENGAGEMENT_STATES idiom.
This is the source of truth the integrity tests read (tests/valoria/test_combat_state_graph.py) and the
dynamic coverage harness diffs the live trace against — so "the state graph flows correctly" (requirement 1)
becomes a repeatable CHECK, not a hand-traced paragraph that drifts.

Each node carries: `to` (target states), `emits` (trace-event kinds the engine fires at this node),
`site` (wrapper.py reference), and `entry`/`terminal` flags. Edges and emits are kept in sync with the live
trace by the dynamic coverage check (run this file: `python state_graph.py`).

Drift note (reconciliation, WS-1): the 2026-06-09 flow-and-state-map prose is superseded as the source of
truth by THIS file. The map's stale items (DAMAGE_SCALE removed; precommit now consumed) do not recur here
because the graph is data + tested, not prose."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

# Trace-event kinds the engine emits (wrapper._emit). The emit-legality test checks every `emits` is here.
TRACE_KINDS = {
    'fight_start', 'turn_start', 'engagement_start', 'approach', 'stophit',
    'commit', 'read', 'mode', 'roll', 'outcome', 'contact', 'separation', 'engagement_end', 'fight_result',
}

# Separation reasons the engine can emit (wrapper.engagement `return None` sites). The dynamic coverage check
# flags any reason that NEVER fires across a sweep — that is how a dead transition (e.g. the stamina<=-4
# collapse abort the 2026-06-09 map flagged as "never observed") is surfaced repeatably.
SEPARATION_REASONS = {'collapse', 'burst_ceiling', 'clean_defence', 'beat_exhaustion'}

STATES = {
    # ---- outer loop (fight) ----
    'FightInit':      {'entry': True, 'to': ['EngagementInit'], 'emits': ['fight_start'], 'site': 'wrapper.fight:282'},
    'EngagementInit': {'to': ['Approach', 'AwaitTempo'], 'emits': ['turn_start', 'engagement_start'], 'site': 'wrapper.engagement:16-34'},
    # ---- inner loop (engagement), per beat ----
    'Approach':       {'to': ['Approach', 'AwaitTempo', 'Felled', 'Separation'], 'emits': ['approach', 'stophit'], 'site': 'wrapper.engagement:66-85'},
    'AwaitTempo':     {'to': ['Exchange', 'AwaitTempo', 'Approach'], 'emits': [], 'site': 'wrapper.engagement:58-88'},
    'Exchange':       {'to': ['Bind', 'Riposte', 'HitLanded', 'Contact', 'AwaitTempo', 'Felled', 'Separation'],
                       'emits': ['commit', 'read', 'mode', 'roll', 'outcome'], 'site': 'wrapper.engagement:86-262'},
    'Bind':           {'to': ['HitLanded', 'Riposte', 'Contact', 'Felled'], 'emits': [], 'site': 'wrapper.engagement:233-252'},
    'Riposte':        {'to': ['AwaitTempo', 'Contact', 'Felled'], 'emits': [], 'site': 'wrapper.engagement:253-261'},
    'HitLanded':      {'to': ['AwaitTempo', 'Contact', 'Felled'], 'emits': [], 'site': 'wrapper.engagement:226-232'},
    # ---- contact axis (I7b, D8/D9): a real Contact node — BUILT, not activated (M-11). Reachable from Exchange
    # directly (the deep-commit reopen precondition needs neither Bind/Riposte/HitLanded) as well as from all
    # three, since a grab is opportunistic on ANY of the three opening_created precondition sites.
    'Contact':        {'to': ['AwaitTempo', 'Separation'], 'emits': ['contact'], 'site': 'wrapper.engagement (outcome tail, contact-axis block)'},
    # ---- engagement terminals -> back to the outer loop ----
    'Felled':         {'to': ['Decided'], 'emits': ['engagement_end'], 'site': 'wrapper.engagement:82,212,232,250,259'},
    'Separation':     {'to': ['InterTurn'], 'emits': ['separation', 'engagement_end'], 'site': 'wrapper.engagement:84,270-273'},
    'InterTurn':      {'to': ['EngagementInit', 'Unresolved'], 'emits': [], 'site': 'wrapper.fight:290-292'},
    # ---- decision ----
    'Decided':        {'to': ['UpsetCheck'], 'emits': [], 'site': 'wrapper.fight:287-289'},
    'UpsetCheck':     {'to': ['FinalResult'], 'emits': [], 'site': 'wrapper.fight:298'},
    'Unresolved':     {'to': ['FinalResult'], 'emits': [], 'site': 'wrapper.fight:293'},
    'FinalResult':    {'terminal': True, 'to': [], 'emits': ['fight_result'], 'site': 'wrapper.fight:299-300'},
}
TERMINAL_STATES = {s for s, v in STATES.items() if v.get('terminal')}
ENTRY_STATES = {s for s, v in STATES.items() if v.get('entry')}

# ── INJECTION POINTS (WS-1): where a tradition's methodology plugs into the graph ────────────────
# "The state graph must be able to accept all these differences across traditions" — this is that, as data.
# Each decision node where the engine currently makes a GENERIC choice is an injection point: a tradition's
# preferred-node / access / bias (from tradition_decomposition_v1.md) biases the branch HERE. This is the
# single-source bridge WS-4 (the access catalogue) and WS-5 (The Approach imposition) wire against. Note the
# FEINT-NODE ABSORB: there is deliberately no separate Feint state — the feint/micro-read lives inside
# Exchange.read (feint-as-attack), so the graph already reflects the dissolved structure; WS-5 removes the
# separate feint_eval CODE, not a graph node.
INJECTION_POINTS = {
    'approach.measure':    {'node': 'Approach',  'site': 'wrapper.py:66-74',
                            'generic': 'shorter closes / longer stop-hits',
                            'injects': 'measure-control: Spanish circulo / Italian misura bias close_rate + preferred measure'},
    'reopen.measure':      {'node': 'AwaitTempo', 'site': 'wrapper.py:58-64',
                            'generic': 'reopen vs stay closed (reopen_prob)',
                            'injects': 'reach/measure-hold: Spanish/Reach impose re-opening (the geometric Vor hold)'},
    'exchange.commit':     {'node': 'Exchange',  'site': 'wrapper.py:98-105',
                            'generic': 'commit depth 2-5, disposition-skewed',
                            'injects': 'Stance posture (The Approach) + wariness vs unread tradition (WS-5)'},
    'exchange.read':       {'node': 'Exchange',  'site': 'wrapper.py:131-133',
                            'generic': 'read_win logistic',
                            'injects': 'precommit (Japanese sen-sen-no-sen) + the FEINT/micro-read manipulation (feint-as-attack, WS-5)'},
    'exchange.mode':       {'node': 'Exchange',  'site': 'wrapper.py:135-136',
                            'generic': 'parry/dodge/wind by mode_sigma',
                            'injects': 'defence-mode preference: German prefers wind, Italian refuses it (stay at the point)'},
    'exchange.bind_entry': {'node': 'Bind',      'site': 'wrapper.py:178-180',
                            'generic': 'bind on wind/partial',
                            'injects': 'German IMPOSE the bind (Winden); Italian/English REFUSE it (cavazione/disengage) — the contact axis'},
    'exchange.counter':    {'node': 'Riposte',   'site': 'wrapper.py:147-158',
                            'generic': 'single-time counter select',
                            'injects': 'Italian mezzo_tempo / Japanese sen-no-sen / English true-times'},
    'burst.continuation':  {'node': 'AwaitTempo', 'site': 'wrapper.py:272',
                            'generic': 'continue burst vs separate (clean defence)',
                            'injects': 'Chinese/Filipino flow: extend the burst on a clean beat'},
    'contact.axis':        {'node': 'Contact',   'site': 'contact.py (grab_available/grab_sigma/grab_outcome) + wrapper.py outcome tail',
                            'generic': 'strength+leverage grab affinity; a flat branching menu (disarm/throw/pin/control/foot_pin/escape)',
                            'injects': 'German Ringen imposes/prefers the bind-entry grab; Italian/English favour the disengage/escape branch — BUILT (I7b, D8/D9), tradition-weighting of the menu is a FUTURE increment, not yet wired'},
}


def injection_markdown():
    out = ["### Tradition injection points (where each methodology biases the state graph)",
           "| point | state | engine site | generic choice today | what a tradition injects |",
           "|---|---|---|---|---|"]
    for k, v in INJECTION_POINTS.items():
        out.append(f"| `{k}` | {v['node']} | `{v['site']}` | {v['generic']} | {v['injects']} |")
    return "\n".join(out)


def transitions_from(state):
    return STATES[state]['to']


def reachable_from(start):
    """BFS closure of states reachable from `start`."""
    seen, stack = set(), [start]
    while stack:
        s = stack.pop()
        if s in seen:
            continue
        seen.add(s)
        stack.extend(STATES[s]['to'])
    return seen


def fired_states_from_events(events):
    """Map a trace event stream to the SET of state-graph nodes it visited (for dynamic coverage)."""
    fired = set()
    for e in events:
        k = e['kind']
        if k == 'fight_start': fired.add('FightInit')
        elif k == 'turn_start': fired.add('EngagementInit')
        elif k == 'engagement_start': fired.add('AwaitTempo' if e['closed'] else 'Approach')
        elif k == 'approach': fired.add('Approach'); fired.add('AwaitTempo') if e.get('just_closed') else None
        elif k in ('commit', 'read', 'mode', 'roll'): fired.add('Exchange')
        elif k == 'outcome':
            fired.add('Exchange')
            if e['hit'] > 0: fired.add('HitLanded')
            if e['bind']: fired.add('Bind')
            if e['riposte']: fired.add('Riposte')
        elif k == 'contact': fired.add('Contact')
        elif k == 'separation': fired.add('Separation'); fired.add('InterTurn')
        elif k == 'engagement_end':
            fired.add('Felled' if e['felled'] else 'Separation')
            fired.add('Decided' if e['felled'] else 'InterTurn')
        elif k == 'fight_result':
            fired.add('FinalResult')
            fired.add('Unresolved' if e['winner'] is None else 'UpsetCheck')
            if e['winner'] is not None: fired.add('Decided')
    return fired


def separation_reasons_from_events(events):
    return {e['reason'] for e in events if e['kind'] == 'separation'}


# ============================== self-test ==============================
if __name__ == '__main__':
    import numpy as np
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'workbench'))
    from combatant import Combatant
    from trace import run_traced_fight

    checks, rule = [], '=' * 64
    print('state_graph.py — engagement/fight state graph integrity'); print(rule)

    # (a) closure: every transition target is a defined state
    valid = set(STATES)
    a_ok = all(all(t in valid for t in v['to']) for v in STATES.values())
    checks.append(a_ok); print(f"(a) edge closure ({len(STATES)} states; all targets defined): {'OK' if a_ok else 'FAIL'}")

    # (b) terminal reachability: a terminal is reachable from every entry
    b_ok = bool(TERMINAL_STATES) and all(TERMINAL_STATES & reachable_from(e) for e in ENTRY_STATES)
    checks.append(b_ok); print(f"(b) terminal {TERMINAL_STATES} reachable from entry {ENTRY_STATES}: {'OK' if b_ok else 'FAIL'}")

    # (c) entry coverage: every state reachable from an entry (no islands)
    cover = set().union(*[reachable_from(e) for e in ENTRY_STATES])
    islands = valid - cover
    c_ok = not islands
    checks.append(c_ok); print(f"(c) entry coverage (no islands): {'OK' if c_ok else 'FAIL — ' + str(islands)}")

    # (d) emit legality: every declared emit is a known trace kind
    bad_emits = {em for v in STATES.values() for em in v['emits'] if em not in TRACE_KINDS}
    d_ok = not bad_emits
    checks.append(d_ok); print(f"(d) emit legality (all emits are known trace kinds): {'OK' if d_ok else 'FAIL — ' + str(bad_emits)}")

    # (e) dynamic coverage: run a sweep, confirm the live trace visits the declared states + flag dead reasons
    fired, reasons = set(), set()
    matchups = [('arming', 'arming'), ('spear', 'dagger'), ('rapier', 'mace'), ('longsword', 'staff')]
    for wa, wb in matchups:
        for s in range(30):
            A = Combatant('A', weapon=wa); B = Combatant('B', weapon=wb)
            _, ev = run_traced_fight(A, B, seed=s)
            fired |= fired_states_from_events(ev); reasons |= separation_reasons_from_events(ev)
    KNOWN_RARE = {'Felled'}  # felled needs a kill within the matchup; covered separately by the long sweep below
    never = (valid - TERMINAL_STATES - fired) - KNOWN_RARE - {'Unresolved'}
    e_ok = not never
    checks.append(e_ok); print(f"(e) dynamic coverage (live trace visits declared states): {'OK' if e_ok else 'FAIL — never fired: ' + str(never)}")
    dead_reasons = SEPARATION_REASONS - reasons
    print(f"    separation reasons observed: {sorted(reasons)}")
    if dead_reasons:
        print(f"    [DEAD-BRANCH FLAG] separation reasons that NEVER fired in the sweep: {sorted(dead_reasons)}")
        print(f"    -> these `return None` sites may be unreachable (cf. the 2026-06-09 map's stamina<=-4 note); "
              f"give them a reachable trigger, demote to a documented guard, or delete.")

    # (f) Felled reachability over a longer decisive sweep (a kill must occur somewhere)
    felled_seen = False
    for s in range(120):
        A = Combatant('A', weapon='greatsword', strength=6); B = Combatant('B', weapon='dagger', strength=2, end=2)
        _, ev = run_traced_fight(A, B, seed=s)
        if any(e['kind'] == 'engagement_end' and e['felled'] for e in ev):
            felled_seen = True; break
    checks.append(felled_seen); print(f"(f) Felled terminal reachable (a kill occurs): {'OK' if felled_seen else 'FAIL'}")

    # (g) every injection point references a defined state (the WS-1 bridge stays synced with the graph)
    bad_inj = {k: v['node'] for k, v in INJECTION_POINTS.items() if v['node'] not in valid}
    g_ok = not bad_inj
    checks.append(g_ok); print(f"(g) {len(INJECTION_POINTS)} injection points reference defined states: {'OK' if g_ok else 'FAIL — ' + str(bad_inj)}")
    print('\n' + injection_markdown())

    print('\n' + rule)
    bad = [i for i, c in enumerate(checks) if not c]
    if bad:
        print(f"RESULT: FAIL — check indices failing: {bad}"); raise SystemExit(1)
    print(f"RESULT: PASS — all {len(checks)} checks (closure, reachability, coverage, emit-legality, dead-branch scan).")
