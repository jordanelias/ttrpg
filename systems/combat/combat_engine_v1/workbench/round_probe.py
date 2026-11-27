"""Round probe — what ends a ROUND, and how often a round closes on itself (PCR-1, A-101).

A *round* is one `wrapper.engagement` call: the two close, exchange one to four attempts, and separate. This reads
the engine's own trace (`wrapper._TRACE` via `fight(..., trace=)`, which draws nothing and mutates nothing) over named
pairs and a seed range, and prints, per pair: rounds per fight; exchanges per round (mean and distribution); attack
attempts per round; loop beats per round; the share of rounds in which both fighters attacked; the share RE-OPENED
INSIDE the round (an `approach` event after a beat at closed measure: the fighters separated and closed again with no
round boundary); and the round endings by reason.

The caller is the B15.01 item of the master workplan (`workplans/valoria_master_workplan_v12_part18.md`), whose gate
reads this table before and after the change, and `tests/valoria/test_combat_round_boundary.py`, which imports
`play` and `rounds_of` so the definition of a round's reading lives once. A loop beat is counted by wrapping
`combat_systems.tempo_pressure` (called twice per loop iteration; the wrapper draws nothing); bind sub-beats are not
iterations and are not counted.

CLI:
    PYTHONHASHSEED=0 python systems/combat/combat_engine_v1/workbench/round_probe.py [first_seed] [n_seeds]
"""
import sys, os
from collections import Counter

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..')))  # the repository root: `modules.combat` is a package
from engine.dice_engine import draw
from modules.combat import wrapper, combatant, config
from modules.combat import combat_systems

# (weapon, armour) of each side; the first is A. Lethal terms, every attribute at its class default.
PAIRS = (
    (('arming', 'light'), ('arming', 'light')),
    (('mace', 'heavy'), ('longsword', 'heavy')),
    (('poleaxe', 'heavy'), ('longsword', 'heavy')),
    (('rapier', 'none'), ('arming', 'light')),
    (('staff', 'none'), ('dagger', 'none')),
    (('spear', 'none'), ('arming', 'none')),
    (('longsword', 'none'), ('spear', 'none')),
)


def _name(pair):
    (wa, aa), (wb, ab) = pair
    return f"{wa}/{aa} v {wb}/{ab}"


def play(pair, seed, cfg=None):
    """One lethal fight of `pair` on `seed`. Returns (result, trace); the `engagement_start` and `round_end` events
    carry `beats`, the running count of loop beats, so a round's beats are the difference between its two."""
    (wa, aa), (wb, ab) = pair
    A = combatant.Combatant('A', weapon=wa, armor=aa)
    B = combatant.Combatant('B', weapon=wb, armor=ab)
    trace, calls = [], [0]
    real = combat_systems.tempo_pressure

    def counted(*a, **k):
        calls[0] += 1
        return real(*a, **k)

    def sink(e):
        if e['kind'] in ('engagement_start', 'round_end'):
            e = dict(e, beats=calls[0] // 2)   # two tempo_pressure calls per loop iteration
        trace.append(e)

    combat_systems.tempo_pressure = counted
    try:
        result = wrapper.fight(A, B, cfg or config.CFG, draw.seeded(draw.H2("round_probe", seed)), trace=sink)
    finally:
        combat_systems.tempo_pressure = real
    return result, trace


def rounds_of(trace):
    """The rounds of one fight's trace, each a dict: exchanges, attempts, beats, attackers (the labels that attacked),
    reopened (an `approach` after a beat at closed measure), ended_by (the `round_end` event's `ended_by` when the
    engine says it, else the last `separation` reason of the round, else 'felled' when a fighter fell)."""
    out, cur, closed = [], None, False
    for e in trace:
        k = e['kind']
        if k == 'engagement_start':
            cur = dict(exchanges=0, attempts=0, beats=-e['beats'], attackers=set(), reopened=False, sep=None)
            closed = e['closed']
        elif cur is None:
            continue
        elif k == 'approach':
            if closed:
                cur['reopened'] = True
            closed = closed or e['just_closed']
        elif k == 'outcome':
            closed = True
            cur['exchanges'] += 1; cur['attempts'] += 1; cur['attackers'].add(e['aggressor'])
        elif k == 'stophit':
            cur['attempts'] += 1; cur['attackers'].add(e['longer'])
        elif k == 'disengage':
            if e['ok']:
                closed = False
            else:
                cur['attempts'] += 1; cur['attackers'].add(e['shorter'])
        elif k == 'separation':
            cur['sep'] = e['reason']
        elif k == 'round_end':
            cur['beats'] += e['beats']
            cur['ended_by'] = e.get('ended_by') or cur['sep'] or ('felled' if e['felled'] else None)
            out.append(cur); cur = None
    return out


def _dist(c):
    return ' '.join(f"{k}:{c[k]}" for k in sorted(c))


def table(seeds, pairs=PAIRS):
    print("| pair | fights | rounds | rounds/fight (mean; max) | exchanges/round (mean; dist) | attempts/round (mean; max) "
          "| loop beats/round (mean; max) | both attacked | re-opened inside | ended by |")
    print("|---|---|---|---|---|---|---|---|---|---|")
    for pair in pairs:
        rounds, per_fight = [], []
        for s in seeds:
            _, tr = play(pair, s)
            r = rounds_of(tr)
            rounds += r; per_fight.append(len(r))
        n = len(rounds)
        ex = Counter(r['exchanges'] for r in rounds)
        ends = Counter(r['ended_by'] for r in rounds)
        print(f"| {_name(pair)} | {len(per_fight)} | {n} | {n / len(per_fight):.2f}; {max(per_fight)} "
              f"| {sum(r['exchanges'] for r in rounds) / n:.2f}; {_dist(ex)} "
              f"| {sum(r['attempts'] for r in rounds) / n:.2f}; {max(r['attempts'] for r in rounds)} "
              f"| {sum(r['beats'] for r in rounds) / n:.1f}; {max(r['beats'] for r in rounds)} "
              f"| {100 * sum(len(r['attackers']) == 2 for r in rounds) / n:.0f}% "
              f"| {100 * sum(r['reopened'] for r in rounds) / n:.1f}% "
              f"| {', '.join(f'{k} {v}' for k, v in ends.most_common())} |", flush=True)


if __name__ == '__main__':
    first = int(sys.argv[1]) if len(sys.argv) > 1 else 5000
    count = int(sys.argv[2]) if len(sys.argv) > 2 else 120
    table(range(first, first + count))
