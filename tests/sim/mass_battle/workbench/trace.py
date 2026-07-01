"""mass_battle.workbench.trace — run ONE traced battle, capturing the tick-by-tick position/state
event stream (Jordan directive 2026-07-01: a visual tool to confirm engine results, especially for
the coordinate-field migration).

Uses the engine's existing observe-only trace seam (resolution.start_trace/trace_event/get_trace,
"no-op unless ON -> byte-exact") plus the tick-by-tick 'positions' snapshots orchestration.py now
emits when tracing is on. Builds units via the wrapper's engine.build_unit adapter and runs via
engine.resolve_battle — the same public surface bat.py dogfoods, so this workbench never reaches
past the wrapper. Read-only: a traced run mutates no engine state beyond the battle it itself runs.

A single run is n=1 by construction — a point sample for visual inspection, not a probability. For
win-rate statistics across many seeds, use gauge_mb.py, never this."""
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))  # tests/sim on path
from mass_battle.engine import build_unit, resolve_battle  # noqa: E402
from mass_battle.resolution import start_trace, get_trace  # noqa: E402
import random  # noqa: E402

# Deployment anchor columns per (shape, tier) — mirrors bat.py's own table (workbench owns its own
# copy rather than reaching into gauge_mb.py, which is a sibling harness script, not a package module).
# [canonical: mass_battle_v30.md §deployment — anchor columns]
ANCHOR_MAP = {
    ('Line', 3): 9, ('Arrowhead', 3): 8, ('Horseshoe', 3): 8,  # [canonical: mass_battle_v30.md §deployment — anchor columns]
    ('GappedLine', 3): 7, ('RefusedFlank', 3): 9, ('Column', 3): 9,  # [canonical: mass_battle_v30.md §deployment — anchor columns]
}


def _anchor_for(shape, tier):
    return ANCHOR_MAP.get((shape, tier), ANCHOR_MAP[('Line', 3)])


def run_traced_battle(spec_a, spec_b, *, seed=0, max_battle_turns=8, kind='multi'):  # [canonical: mass_battle_v30.md §A.7 — battle-turn cap, same default as orchestration.run_multi_turn_battle]
    """spec_a/spec_b: dicts of engine.build_unit kwargs — REQUIRED 'shape'; optional tier (default 3),
    name, troop_type, unit_type, power, command, discipline, morale, morale_start, stance, speed,
    instructions, dr, anchor_col (defaults from ANCHOR_MAP). Faction is fixed ('A' for spec_a, 'B' for
    spec_b) so the trace is always readable the same way.

    Returns {'winner', 'events': [...], 'a': {summary}, 'b': {summary}}. `events` is the ordered
    trace — 'tick'/'melee'/'volley'/'positions' category dicts, exactly as resolution.get_trace()
    returns them (no re-shaping), so the frontend consumes the engine's own event vocabulary."""
    a = dict(spec_a); b = dict(spec_b)
    tier_a = a.pop('tier', 3); tier_b = b.pop('tier', 3)
    shape_a = a.pop('shape'); shape_b = b.pop('shape')
    name_a = a.pop('name', 'A'); name_b = b.pop('name', 'B')
    anchor_a = a.pop('anchor_col', _anchor_for(shape_a, tier_a))
    anchor_b = b.pop('anchor_col', _anchor_for(shape_b, tier_b))

    random.seed(seed)
    ua = build_unit(shape_a, tier_a, name_a, 'A', anchor_a, **a)
    ub = build_unit(shape_b, tier_b, name_b, 'B', anchor_b, **b)
    a0, b0 = ua.hp_max, ub.hp_max

    start_trace(True)
    try:
        if kind == 'single':
            r = resolve_battle(ua, ub, kind='single', max_turns=18)  # [canonical: mass_battle_v30.md §A.7 — 18-tick battle (3 phases x 6), same default as orchestration.run_battle]
        else:
            anchor_map = {(shape_a, tier_a): anchor_a, (shape_b, tier_b): anchor_b}
            r = resolve_battle(ua, ub, shape_a, shape_b, anchor_map,
                                kind='multi', max_battle_turns=max_battle_turns)
        events = get_trace()
    finally:
        start_trace(False)

    return {
        'winner': r.get('winner'), 'events': events,
        'a': {'name': ua.name, 'shape': shape_a, 'hp_max': a0, 'hp_final': ua.hp,
              'morale_final': ua.morale, 'routed': ua.routed},
        'b': {'name': ub.name, 'shape': shape_b, 'hp_max': b0, 'hp_final': ub.hp,
              'morale_final': ub.morale, 'routed': ub.routed},
    }


if __name__ == '__main__':
    import json
    result = run_traced_battle({'shape': 'Horseshoe', 'troop_type': 'cavalry', 'speed': 'Fast'},
                                {'shape': 'Line'}, seed=1)
    n_pos = sum(1 for e in result['events'] if e.get('cat') == 'positions')
    print(f"winner={result['winner']}  events={len(result['events'])}  position-snapshots={n_pos}")
    print(json.dumps(result['a'], indent=2), json.dumps(result['b'], indent=2))
