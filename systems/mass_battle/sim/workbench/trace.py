"""mass_battle.workbench.trace — run ONE traced battle, capturing the tick-by-tick position/state
event stream (Jordan directive 2026-07-01: a visual tool to confirm engine results, especially for
the coordinate-field migration).

Uses the engine's existing observe-only trace seam (resolution.tracing/trace_event, "no-op outside
a `tracing()` block -> byte-exact") plus the tick-by-tick 'positions' snapshots orchestration.py now
emits when tracing is on. The default, `kind='field'`, traces the ONE path the season reaches: it builds a
`MassBattleInput` and calls `massbattle.resolve_field` inside `tracing()`. The other kinds ('single', 'multi')
build units via the wrapper's engine.build_unit adapter and run via engine.resolve_battle (the multi-battle
loops of `multi.py`) — the same public surface bat.py dogfoods. Read-only: a traced run mutates no engine
state beyond the battle it itself runs.

A single run is n=1 by construction — a point sample for visual inspection, not a probability. For
win-rate statistics across many seeds, use gauge_mb.py, never this."""
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))  # tests/sim on path
if __name__ == '__main__':   # [B17.12] run as a script, the engine is built from the toggles its caller exported
    from systems.mass_battle.sim import variant
    variant.install(variant.cfg_from_environ(os.environ))
from systems.mass_battle.sim.engine import (  # noqa: E402
    build_unit, build_army, build_envelopment, build_refused_flank, resolve_battle,
    SIDE_A_START_ROW, SIDE_B_START_ROW)
from modules.mass_battle.resolution import tracing  # noqa: E402
from engine.dice_engine import draw  # noqa: E402
from modules.mass_battle import rngsource  # noqa: E402

# Deployment anchor columns per (shape, tier) — mirrors bat.py's own table (workbench owns its own
# copy rather than reaching into gauge_mb.py, which is a sibling harness script, not a package module).
# [LC-8, ED-909, 2026-07-02] Horseshoe/RefusedFlank entries retired along with the shapes themselves —
# Envelopment/RefusedFlank presets below build Line-shaped units, so ('Line', tier) covers them.
# [canonical: mass_battle_v30.md §deployment — anchor columns]
ANCHOR_MAP = {
    ('Line', 3): 9, ('Arrowhead', 3): 8,  # [canonical: mass_battle_v30.md §deployment — anchor columns]
    ('GappedLine', 3): 7, ('Column', 3): 9,  # [canonical: mass_battle_v30.md §deployment — anchor columns]
}


def _anchor_for(shape, tier):
    return ANCHOR_MAP.get((shape, tier), ANCHOR_MAP[('Line', 3)])


def _build_side(spec, faction):
    """Build one side's Army from a workbench spec dict. Two spec shapes:

    - **single-subunit** (existing, unchanged): {'shape': ..., 'tier': ..., 'name': ...,
      'anchor_col': ..., ...build_unit kwargs}.
    - **multi-subunit preset** (new, LC-8 — Horseshoe/RefusedFlank are retired as literal shapes, so
      visualizing 'Envelopment'/'Refused Flank' now means building the real Army-level composition):
      {'preset': 'army'|'envelopment'|'refused_flank', 'name': ..., ...shared build_* kwargs} plus,
      per preset: 'specs' (a build_army-style per-subunit spec list) for 'army'; 'center'/'wings' for
      'envelopment'; 'strong'/'refused' for 'refused_flank' — matching engine.build_army/
      build_envelopment/build_refused_flank's own parameter names exactly, so this is a thin dispatch,
      not a new schema.

    Returns (unit, shape_label, tier_label, anchor_col) — the label/anchor are consulted only by
    resolve_battle's now-fallback-only shape_a/shape_b/anchor_map positional args (every subunit built
    through __post_init__ carries its own _spawn_position; see multi.reset_positions)."""
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


def _field_record(spec_a, spec_b):
    """A hand-built `MassBattleInput`: two headcount sides on open ground, as the module's own tests build one. A side's
    spec is its weight (a number), or `{'weight': w, 'stance': s}` (`stance` defaults to 0.0, the base morale-start)."""
    import yaml
    from engine.season.data import files
    from engine.season.data.fixtures import DEFAULT_FIXTURES
    from engine.season.queries.inputs import MassBattleInput
    sides = [s if isinstance(s, dict) else {'weight': s} for s in (spec_a, spec_b)]
    with open(files.GEOGRAPHY_YAML, encoding='utf-8') as f:
        geo = yaml.safe_load(f)
    return MassBattleInput(weights=((float(sides[0]['weight']),), (float(sides[1]['weight']),)), territory=None,
                           fort_level=0.0, stances=tuple(float(s.get('stance', 0.0)) for s in sides), walls_dr=None,
                           origin=None, loyalties=(0.0, 0.0), loyalty_gain=0, geography=geo,
                           condition_scale=DEFAULT_FIXTURES.get('condition_scale'), members=(('a',), ('b',)))


def _run_traced_field(spec_a, spec_b, seed):
    """The season's one battle path under `tracing()`: `resolve_field` on a hand-built record. Returns the other kinds'
    keys, with the typed outcome under 'outcome'; a refusal (`PARTY-GAP`, `SCALE-GAP`) comes back under 'refused'."""
    from engine.season.seam.ladder import field_degree
    from modules.mass_battle import massbattle
    with tracing() as recorded:
        got = massbattle.resolve_field(_field_record(spec_a, spec_b), draw.seeded(draw.H2("trace", seed)))
    events = list(recorded)
    if isinstance(got, dict):
        return {'winner': None, 'events': events, 'refused': got}
    band = field_degree(got)
    return {'winner': {'Won': 'A', 'Lost': 'B'}.get(band, 'draw'), 'band': band, 'events': events, 'outcome': got,
            'a': {'name': 'side_a', 'share': got.attacker.share, 'routed': got.attacker.routed,
                  'conceded': got.attacker.conceded},
            'b': {'name': 'side_b', 'share': got.defender.share, 'routed': got.defender.routed,
                  'conceded': got.defender.conceded}}


def run_traced_battle(spec_a, spec_b, *, seed=0, max_battle_turns=8, kind='field'):  # [canonical: mass_battle_v30.md §A.7 — battle-turn cap, same default as multi.run_multi_turn_battle]
    """kind='field' (the default): spec_a/spec_b are each a side's weight, or `{'weight', 'stance'}` (`_field_record`).
    kind='single' | 'multi': see _build_side — either a single-subunit build_unit spec, or a multi-subunit
    'preset' spec (army/envelopment/refused_flank). Faction is fixed ('A' for spec_a, 'B' for spec_b)
    so the trace is always readable the same way.

    Returns {'winner', 'events': [...], 'a': {summary}, 'b': {summary}}. `events` is the ordered
    trace — 'tick'/'melee'/'volley'/'positions' category dicts, exactly as a resolution.tracing()
    block records them (no re-shaping), so the frontend consumes the engine's own event vocabulary."""
    if kind == 'field':
        return _run_traced_field(spec_a, spec_b, seed)
    with rngsource.using(draw.seeded(draw.H2("trace", seed))):
        ua, shape_a, tier_a, anchor_a = _build_side(spec_a, 'A')
        ub, shape_b, tier_b, anchor_b = _build_side(spec_b, 'B')
        a0, b0 = ua.hp_max, ub.hp_max

        with tracing() as recorded:
            if kind == 'single':
                r = resolve_battle(ua, ub, kind='single', max_ticks=18)  # [canonical: mass_battle_v30.md §A.7 — 18-tick battle (3 phases x 6), same default as orchestration.run_battle]
            else:
                anchor_map = {(shape_a, tier_a): anchor_a, (shape_b, tier_b): anchor_b}
                r = resolve_battle(ua, ub, shape_a, shape_b, anchor_map,
                                    kind='multi', max_battle_turns=max_battle_turns)
        events = list(recorded)

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
        {'shape': 'Line'}, seed=1, kind='multi')
    n_pos = sum(1 for e in result['events'] if e.get('cat') == 'positions')
    print(f"winner={result['winner']}  events={len(result['events'])}  position-snapshots={n_pos}")
    print(json.dumps(result['a'], indent=2), json.dumps(result['b'], indent=2))
