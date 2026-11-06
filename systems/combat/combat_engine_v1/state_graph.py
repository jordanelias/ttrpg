"""state_graph.py — the engagement/fight state graph as DATA (scene-combat WS-1).

The canonical engine's control flow (wrapper.fight -> wrapper.engagement) expressed as a single declarative
STATES dict, modelled on tests/sim/v32-combat-balance/m4a_bout_state_graph.py's ENGAGEMENT_STATES idiom.
This is the source of truth the dynamic coverage harness (run this file) diffs the live trace against — so "the state graph flows correctly" (requirement 1)
becomes a repeatable CHECK, not a hand-traced paragraph that drifts.

Each node carries: `to` (target states), `emits` (trace-event kinds the engine fires at this node),
`site` (wrapper.py reference), and `entry`/`terminal` flags. Edges and emits are kept in sync with the live
trace by the dynamic coverage check (run this file: `python state_graph.py`).

Drift note (reconciliation, WS-1): the 2026-06-09 flow-and-state-map prose is superseded as the source of
truth by THIS file. The map's stale items (DAMAGE_SCALE removed; precommit now consumed) do not recur here
because the graph is data + tested, not prose."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'modules', 'combat'))  # the engine, moved at plan position `31b`

# Trace-event kinds the engine emits (wrapper._emit). The emit-legality test checks every `emits` is here.
TRACE_KINDS = {
    'fight_start', 'turn_start', 'engagement_start', 'approach', 'stophit',
    'commit', 'read', 'mode', 'roll', 'outcome', 'contact', 'separation', 'engagement_end', 'fight_result',
    'yield',   # §11.4 (PC-01): a Phase-1 declaration; an unrefused one ends the fight at FinalResult via Yielded
    'wound',   # PC-13: every point of damage the tracker takes, from the ONE helper wrapper._wound (pursuit, stophit, displace_graze, exchange, bind)
    'disengage',   # the closed-phase withdrawal attempt (ED-PC-0030): ok=True re-opens to measure, ok=False is pursued
    'withdraw',    # REM-31: the decider's early UNRESOLVED exit, taken at the head of a turn
}

# Separation reasons the engine can emit (wrapper.engagement `return None` sites). The dynamic coverage check
# flags any reason that NEVER fires across a sweep — that is how a dead transition (e.g. the stamina<=-4
# collapse abort the 2026-06-09 map flagged as "never observed") is surfaced repeatably.
SEPARATION_REASONS = {'collapse', 'burst_ceiling', 'clean_defence', 'beat_exhaustion', 'terms'}   # 'terms' (RS-25): a duel's terms were met at a beat head
# [ED-PC-0042 — MEASURED, do not re-litigate] The (e) sweep below used to flag 'collapse' and 'beat_exhaustion' as
# never-fired, and the 2026-07-26 defect register carried them as dead branches on that basis. They are NOT dead:
# over 5,184 fights spanning 12 weapons x end in {1,2,6} x armour in {none,heavy} they fire 164 and 1,135 times
# respectively. The flag was a FALSE POSITIVE of that sweep's build coverage — its 4 matchups all use DEFAULT
# fighters, who reach clean_defence/burst_ceiling long before stamina <= -4 or the beat budget runs out. PC-13 widened
# the sweep (the WIDE builds, the duel-terms fight and the withdraw fight in the self-test below) rather than delete two
# reachable guards on the strength of an under-powered probe.

STATES = {
    # ---- outer loop (fight) ----
    'FightInit':      {'entry': True, 'to': ['EngagementInit', 'Yielded', 'Withdrawal'], 'emits': ['fight_start'], 'site': 'wrapper.fight:282'},
    'EngagementInit': {'to': ['Approach', 'AwaitTempo'], 'emits': ['turn_start', 'engagement_start'], 'site': 'wrapper.engagement:16-34'},
    # ---- inner loop (engagement), per beat ----
    'Approach':       {'to': ['Approach', 'AwaitTempo', 'Felled', 'Separation'], 'emits': ['approach', 'stophit', 'wound'], 'site': 'wrapper.engagement:66-85'},
    'AwaitTempo':     {'to': ['Exchange', 'AwaitTempo', 'Approach', 'Felled', 'Separation'], 'emits': ['disengage', 'wound'], 'site': 'wrapper.engagement:58-88'},   # disengage (+ its pursuit wound) and the terms separation are beat-head events
    'Exchange':       {'to': ['Bind', 'Riposte', 'HitLanded', 'Contact', 'AwaitTempo', 'Felled', 'Separation'],
                       'emits': ['commit', 'read', 'mode', 'roll', 'outcome', 'wound'], 'site': 'wrapper.engagement:86-262'},
    'Bind':           {'to': ['HitLanded', 'Riposte', 'Contact', 'Felled'], 'emits': ['wound'], 'site': 'wrapper.engagement:233-252'},
    'Riposte':        {'to': ['AwaitTempo', 'Contact', 'Felled'], 'emits': [], 'site': 'wrapper.engagement:253-261'},
    'HitLanded':      {'to': ['AwaitTempo', 'Contact', 'Felled'], 'emits': ['wound'], 'site': 'wrapper.engagement:226-232'},
    # ---- contact axis (I7b, D8/D9): a real Contact node — BUILT, not activated (M-11). Reachable from Exchange
    # directly (the deep-commit reopen precondition needs neither Bind/Riposte/HitLanded) as well as from all
    # three, since a grab is opportunistic on ANY of the three opening_created precondition sites.
    'Contact':        {'to': ['AwaitTempo', 'Separation'], 'emits': ['contact'], 'site': 'wrapper.engagement (outcome tail, contact-axis block)'},
    # ---- engagement terminals -> back to the outer loop ----
    'Felled':         {'to': ['Decided'], 'emits': ['engagement_end'], 'site': 'wrapper.engagement:82,212,232,250,259'},
    'Separation':     {'to': ['InterTurn'], 'emits': ['separation', 'engagement_end'], 'site': 'wrapper.engagement:84,270-273'},
    'InterTurn':      {'to': ['EngagementInit', 'Unresolved', 'Yielded', 'Withdrawal'], 'emits': [], 'site': 'wrapper.fight:290-292'},
    # ---- decision ----
    # §11.4 (PC-01): an unrefused Yield, declared at Phase 1 of a turn (so from FightInit or InterTurn), ends the fight
    # straight at FinalResult with no UPSET_FLOOR draw. A REFUSED declaration emits `yield` and falls through unchanged.
    'Yielded':        {'to': ['FinalResult'], 'emits': ['yield'], 'site': 'wrapper.fight (Phase-1 yield declaration)'},
    # REM-31: the decider's 'withdraw', taken at the head of a turn (so from FightInit or InterTurn): the early UNRESOLVED exit,
    # no UPSET_FLOOR draw.
    'Withdrawal':     {'to': ['Unresolved'], 'emits': ['withdraw'], 'site': 'wrapper.fight (per-turn decider, WITHDRAW)'},
    'Decided':        {'to': ['UpsetCheck'], 'emits': [], 'site': 'wrapper.fight:287-289'},
    'UpsetCheck':     {'to': ['FinalResult'], 'emits': [], 'site': 'wrapper.fight:298'},
    'Unresolved':     {'to': ['FinalResult'], 'emits': [], 'site': 'wrapper.fight:293'},
    'FinalResult':    {'terminal': True, 'to': [], 'emits': ['fight_result'], 'site': 'wrapper.fight:299-300'},
}
TERMINAL_STATES = {s for s, v in STATES.items() if v.get('terminal')}
ENTRY_STATES = {s for s, v in STATES.items() if v.get('entry')}

# ── INJECTION POINTS: where a fighter's learned abilities reach the graph ─────────────────────────
# REWRITTEN at PC-17 (ED-PC-0059) to say what the code does. A tradition does NOT bias a branch: the imposition gate
# is retired (ED-PC-0023) and a tradition only gates ACCESS to its kit (ability_primitives._invested, ED-PC-0028).
# What reaches the graph is the invested ABILITY, through a named lever: `eff_cw` / `ability_factor` ('*' abilities,
# exactly 1.0 when none is equipped) or `ability_bonus` ('+' abilities, exactly 0.0), read inside the
# `combat_systems` function each entry names, which `wrapper.engagement` calls at that node. Familiarity (tradition
# vs tradition) is the one tradition-level input, and is named where it is read. An entry whose node reads no lever
# says so. There is no separate Feint state: the feint lives inside the Exchange read (feint-as-attack, WS-5).
# Each entry was checked against the call sites in `modules/combat/wrapper.py` and the lever reads in
# `modules/combat/combat_systems.py` / `contact.py` (grep `eff_cw`, `ability_factor`, `ability_bonus`). Line
# numbers are deliberately absent (D12b: they drift); the node name is checked against STATES by this file's
# self-test, check (g).
INJECTION_POINTS = {
    'beat.head':           {'node': 'AwaitTempo',
                            'generic': 'every beat, before both Approach and AwaitTempo: initiative decay, grip, facing, readiness = cadence x tempo_pressure',
                            'injects': "measure lever: init_hold_decay (a factor above 1 slows the decay of the held initiative); tempo lever: tempo_pressure's READ_TEMPO_K term, each side's reading x its own tempo factor; facing_regime lever: facing_target (no ability authored: weapon geometry only)"},
    'approach.close':      {'node': 'Approach',
                            'generic': 'shorter closes / longer stop-hits (close_rate, approach_displace, stophit_sigma)',
                            'injects': 'no ability lever is read by these functions; only the beat-head levers act on an Approach beat'},
    'reopen.measure':      {'node': 'AwaitTempo',
                            'generic': 'on a created moment, the longer weapon reopens distance or stays closed (reopen_prob)',
                            'injects': "visual lever, both sides: the longer fighter's reading x its visual factor against the shorter's (the denial); no measure lever is read here"},
    'disengage.withdraw':  {'node': 'AwaitTempo',
                            'generic': 'the longer weapon attempts a withdrawal (disengage_attempt_p); clean break or pursued',
                            'injects': 'visual lever, both sides: disengage_clean_p (each reading x its own visual factor); balance lever, both sides: pursuit_sigma\'s footwork term (each balance_eff x its own balance factor) on the pursued branch'},
    'exchange.commit':     {'node': 'Exchange',
                            'generic': 'commit depth 2-5, a Beta draw skewed by disposition (commit_depth)',
                            'injects': 'no ability lever; familiarity (tradition vs tradition) sets the WARINESS that skews the draw shallow'},
    'exchange.read':       {'node': 'Exchange',
                            'generic': 'read_win logistic; the best mode on a won read (read_contest)',
                            'injects': "visual and precommit levers: the defender's reading x visual x precommit, scaled by familiarity and the aggressor's legibility; the aggressor's reading x visual. Inside legibility, the aggressor's edge_read factor amplifies the double/false-edge return-line term (lowers legibility) and its choke_control factor scales the gathered-pole telegraph term (raises it; a factor below 1 mitigates)"},
    'exchange.mode':       {'node': 'Exchange',
                            'generic': 'parry/dodge/wind by mode_sigma on a won read, else uniform random',
                            'injects': 'no ability lever is read by mode_sigma'},
    'exchange.roll':       {'node': 'Exchange',
                            'generic': 'the net sigma of the main roll, and the over-commitment cost after it',
                            'injects': "measure lever: reach_sigma's lever_log_edge (defender over aggressor); balance lever: reach_sigma's footwork term, each side's own; tempo lever: init_emphasis_sigma's INIT_TEMPO_LEVER_K x lever_log_edge (aggressor over defender, PC-17); anti_overcommit ('+'): overcommit_exposure; tempo lever: init_overcommit_loss divides the initiative lost"},
    'exchange.counter':    {'node': 'Exchange',
                            'generic': 'on a won read against a deep commit: the initiative steal and the single-time counter selection',
                            'injects': "init_steal_factor: on a wind, the defender's (tactile + leverage)/2, else its tempo factor; counter_select: the defender's tempo factor x its counter_select factor"},
    'riposte.counter':     {'node': 'Riposte',
                            'generic': 'whether a selected counter lands (counter_success_prob)',
                            'injects': "counter_success ('+'): added to the success probability before its [0.05, 0.92] bounds"},
    'exchange.bind_entry': {'node': 'Bind',
                            'generic': 'bind on wind/partial; up to three bind iterations',
                            'injects': "bind_sigma: leverage lever as lever_log_edge, tactile lever on each side's own read (x familiarity), spine_press lever on each side's own spine; at entry the winner's init_steal_factor (tactile + leverage)/2 and a poise break scaled by its leverage factor"},
    'burst.continuation':  {'node': 'AwaitTempo',
                            'generic': 'continue the burst vs separate (clean defence, burst ceiling, collapse)',
                            'injects': 'no ability lever is read at this decision'},
    'contact.axis':        {'node': 'Contact',
                            'generic': 'strength+leverage grab affinity; a flat branching menu (disarm/throw/pin/control/foot_pin/escape)',
                            'injects': "edge_grab lever: contact.grab_sigma scales the self-hazard of seizing a live edge by the actor's factor (ringen_am_schwert, a mitigator below 1); the outcome menu reads no lever"},
}


def injection_markdown():
    out = ["### Ability injection points (where an invested ability's lever is read in the state graph)",
           "| point | state | generic choice today | levers read there |",
           "|---|---|---|---|"]
    for k, v in INJECTION_POINTS.items():
        out.append(f"| `{k}` | {v['node']} | {v['generic']} | {v['injects']} |")
    return "\n".join(out)


# ED-PC-0035: `transitions_from` REMOVED — zero callers; even this module's own self-test uses reachable_from().


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
        if k == 'yield':
            if e.get('refused') is None: fired.add('Yielded')   # a refused declaration falls through: no state of its own
        elif k == 'fight_start': fired.add('FightInit')
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
        elif k == 'withdraw': fired.add('Withdrawal')
        elif k == 'stophit': fired.add('Approach')   # a stop-thrust that fells ends the engagement before the `approach` emit
        elif k == 'separation': fired.add('Separation'); fired.add('InterTurn')
        elif k == 'engagement_end':
            fired.add('Felled' if e['felled'] else 'Separation')
            fired.add('Decided' if e['felled'] else 'InterTurn')
        elif k == 'fight_result':
            fired.add('FinalResult')
            if e['winner'] is None: fired.add('Unresolved')
            elif 'Yielded' not in fired:   # a yield ends the fight before the decision nodes
                fired.add('Decided'); fired.add('UpsetCheck')
    return fired


def separation_reasons_from_events(events):
    return {e['reason'] for e in events if e['kind'] == 'separation'}


# ============================== self-test ==============================
if __name__ == '__main__':
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
    # PC-13: the widened builds. Each pins a (build, seed range) that REACHES a branch the default fighters do not:
    # 'collapse' (low-end heavy-armoured fighters run to stamina <= -4) and 'beat_exhaustion' (two heavy end-6 fighters
    # exhaust the beat budget). Found by searching weapons x end x armour; if a rebalance moves them the (e) flag below prints.
    WIDE = [(('longsword', 'staff'), dict(end=1, armor='heavy'), range(0, 6)),
            (('cinquedea', 'greatsword'), dict(end=6, armor='heavy'), range(0, 6))]
    for (wa, wb), kit, seeds in WIDE:
        for s in seeds:
            A = Combatant('A', weapon=wa, **kit); B = Combatant('B', weapon=wb, **kit)
            _, ev = run_traced_fight(A, B, seed=s)
            fired |= fired_states_from_events(ev); reasons |= separation_reasons_from_events(ev)
    # PC-13: the duel-terms fight ('terms' separation + the terms yield) and the decider's withdraw (Withdrawal), both
    # through run_traced_fight's `**fight_kw`.
    import wrapper as _W
    def _traced(A, B, seed, **kw):
        return run_traced_fight(A, B, seed=seed, **kw)[1]
    for s in range(30):
        ev = _traced(Combatant('A', weapon='arming'), Combatant('B', weapon='sabre'), s, terms='blood')
        fired |= fired_states_from_events(ev); reasons |= separation_reasons_from_events(ev)
    for s in range(3):
        ev = _traced(Combatant('A', weapon='arming'), Combatant('B', weapon='arming'), s, decide=lambda turn: _W.WITHDRAW if turn == 2 else _W.ENGAGE)
        fired |= fired_states_from_events(ev); reasons |= separation_reasons_from_events(ev)
    KNOWN_RARE = {'Felled'}  # felled needs a kill within the matchup; covered separately by the long sweep below
    never = (valid - TERMINAL_STATES - fired) - KNOWN_RARE - {'Unresolved', 'Yielded'}
    e_ok = not never
    checks.append(e_ok); print(f"(e) dynamic coverage (live trace visits declared states): {'OK' if e_ok else 'FAIL — never fired: ' + str(never)}")
    dead_reasons = SEPARATION_REASONS - reasons
    print(f"    separation reasons observed: {sorted(reasons)}")
    if dead_reasons:
        print(f"    [DEAD-BRANCH FLAG] separation reasons that NEVER fired in the sweep: {sorted(dead_reasons)}")
        print("    -> these `return None` sites may be unreachable (cf. the 2026-06-09 map's stamina<=-4 note); "
              "give them a reachable trigger, demote to a documented guard, or delete.")

    # (f) Felled reachability over a longer decisive sweep (a kill must occur somewhere)
    felled_seen = False
    for s in range(120):
        A = Combatant('A', weapon='greatsword', strength=6); B = Combatant('B', weapon='dagger', strength=2, end=2)
        _, ev = run_traced_fight(A, B, seed=s)
        if any(e['kind'] == 'engagement_end' and e['felled'] for e in ev):
            felled_seen = True; break
    checks.append(felled_seen); print(f"(f) Felled terminal reachable (a kill occurs): {'OK' if felled_seen else 'FAIL'}")

    # (g) the §11.4 yield path (PC-01): an unrefused Yield visits Yielded and FinalResult and skips the decision nodes
    _B = Combatant('B')
    _ev = _traced(Combatant('A'), _B, 0, yield_decl=_W.Yield(by=_B, turn=1))
    _fy = fired_states_from_events(_ev)
    g_ok = {'Yielded', 'FinalResult'} <= _fy and not ({'UpsetCheck', 'Decided'} & _fy)
    checks.append(g_ok); print(f"(g) yield path (Yielded -> FinalResult, decision nodes skipped): {'OK' if g_ok else 'FAIL — ' + str(sorted(_fy))}")

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
