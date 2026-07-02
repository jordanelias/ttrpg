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
from mass_battle.engine import (  # noqa: E402
    build_unit, build_army, build_envelopment, build_refused_flank, resolve_battle,
    SIDE_A_START_ROW, SIDE_B_START_ROW)
from mass_battle.resolution import start_trace, get_trace  # noqa: E402
import random  # noqa: E402

# Deployment anchor columns per (shape, tier) — mirrors bat.py's own table (workbench owns its own
# copy rather than reaching into gauge_mb.py, which is a sibling harness script, not a package module).
# [LC-8, ED-909, 2026-07-02] Horseshoe/RefusedFlank entries retired along with the shapes themselves —
# Envelopment/RefusedFlank presets below build Line-shaped subunits, so ('Line', tier) covers them.
# [canonical: mass_battle_v30.md §deployment — anchor columns]
ANCHOR_MAP = {
    ('Line', 3): 9, ('Arrowhead', 3): 8,  # [canonical: mass_battle_v30.md §deployment — anchor columns]
    ('GappedLine', 3): 7, ('Column', 3): 9,  # [canonical: mass_battle_v30.md §deployment — anchor columns]
}


def _anchor_for(shape, tier):
    return ANCHOR_MAP.get((shape, tier), ANCHOR_MAP[('Line', 3)])


def _build_side(spec, faction):
    """Build one side's Unit from a workbench spec dict. Two spec shapes:

    - **single-subunit** (existing, unchanged): {'shape': ..., 'tier': ..., 'name': ...,
      'anchor_col': ..., ...build_unit kwargs}.
    - **multi-subunit preset** (new, LC-8 — Horseshoe/RefusedFlank are retired as literal shapes, so
      visualizing 'Envelopment'/'Refused Flank' now means building the real Unit-level composition):
      {'preset': 'army'|'envelopment'|'refused_flank', 'name': ..., ...shared build_* kwargs} plus,
      per preset: 'specs' (a build_army-style per-subunit spec list) for 'army'; 'center'/'wings' for
      'envelopment'; 'strong'/'refused' for 'refused_flank' — matching engine.build_army/
      build_envelopment/build_refused_flank's own parameter names exactly, so this is a thin dispatch,
      not a new schema.

    Returns (unit, shape_label, tier_label, anchor_col) — the label/anchor are consulted only by
    resolve_battle's now-fallback-only shape_a/shape_b/anchor_map positional args (every subunit built
    through __post_init__ carries its own _spawn_position; see orchestration.reset_positions)."""
    spec = dict(spec)
    preset = spec.pop('preset', None)
    name = spec.pop('name', 'A' if faction == 'A' else 'B')
    tier = spec.pop('tier', 3)
    if preset is None:
        shape = spec.pop('shape')
        anchor = spec.pop('anchor_col', _anchor_for(shape, tier))
        unit = build_unit(shape, tier, name, faction, anchor, **spec)
        return unit, shape, tier, anchor
    if preset == 'army':
        unit = build_army(spec.pop('specs'), name, faction, **spec)
    elif preset == 'envelopment':
        unit = build_envelopment(spec.pop('center'), spec.pop('wings'), name, faction, **spec)
    elif preset == 'refused_flank':
        unit = build_refused_flank(spec.pop('strong'), spec.pop('refused'), name, faction, **spec)
    else:
        raise ValueError(f"unknown preset {preset!r} (expected 'army'|'envelopment'|'refused_flank')")
    return unit, 'Line', tier, _anchor_for('Line', tier)


def run_traced_battle(spec_a, spec_b, *, seed=0, max_battle_turns=8, kind='multi'):  # [canonical: mass_battle_v30.md §A.7 — battle-turn cap, same default as orchestration.run_multi_turn_battle]
    """spec_a/spec_b: see _build_side — either a single-subunit build_unit spec, or a multi-subunit
    'preset' spec (army/envelopment/refused_flank). Faction is fixed ('A' for spec_a, 'B' for spec_b)
    so the trace is always readable the same way.

    Returns {'winner', 'events': [...], 'a': {summary}, 'b': {summary}}. `events` is the ordered
    trace — 'tick'/'melee'/'volley'/'positions' category dicts, exactly as resolution.get_trace()
    returns them (no re-shaping), so the frontend consumes the engine's own event vocabulary."""
    random.seed(seed)
    ua, shape_a, tier_a, anchor_a = _build_side(spec_a, 'A')
    ub, shape_b, tier_b, anchor_b = _build_side(spec_b, 'B')
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
    result = run_traced_battle(
        {'preset': 'envelopment',
         'center': [{'shape': 'Line', 'tier': 3, 'starting_position': (SIDE_A_START_ROW, _anchor_for('Line', 3))}],
         'wings': [{'shape': 'Line', 'tier': 3, 'troop_type': 'cavalry', 'speed': 'Fast',
                    'starting_position': (SIDE_A_START_ROW, 3)},
                   {'shape': 'Line', 'tier': 3, 'troop_type': 'cavalry', 'speed': 'Fast',
                    'starting_position': (SIDE_A_START_ROW, 15)}]},
        {'shape': 'Line'}, seed=1)
    n_pos = sum(1 for e in result['events'] if e.get('cat') == 'positions')
    print(f"winner={result['winner']}  events={len(result['events'])}  position-snapshots={n_pos}")
    print(json.dumps(result['a'], indent=2), json.dumps(result['b'], indent=2))
