"""bat.py — byte-exact DIGEST harness for the mass-battle engine (the G5 gate).

Runs a fixed, deterministic battery (per-trial random.seed, exactly as gauge_mb.py does) of
representative matchups and hashes the FULL per-trial end state (winner, battle-turns, hp, morale,
discipline, rout flags — not just the aggregate win-rate). A behaviour-preserving refactor must
reproduce the digest digit-for-digit; any change to the number is a refactor bug, not a tuning
question. Covers both engine paths:

    PER_CELL=0 python3 tests/sim/mass_battle/bat.py     # baseline (unit pool)
    PER_CELL=1 python3 tests/sim/mass_battle/bat.py     # per-cell layer

Prints one `DIGEST <mode> <hash>` line. This is the committed golden-digest gate the coverage
matrix previously referenced but that was never committed; Stage 1 of the bottom-up re-architecture
adds it so every later stage has a reproducible byte-exact check.
[canonical: tests/sim/gauge_mb.py — deterministic seed battery; mass_battle_gauge_grounding.md §1]
"""
import os, sys, hashlib

# import the package exactly as the stress harness / gauge do
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # tests/sim on path
from mass_battle.engine import (  # noqa: E402
    build_unit, resolve_battle, SIDE_A_START_ROW, SIDE_B_START_ROW)
import random  # noqa: E402

# anchor columns per (shape,tier) — copied from gauge_mb.py ANCHOR_MAP (T3 row used below)
# [canonical: mass_battle_v30.md §deployment — anchor columns]
ANCHOR_MAP = {
    ('Line', 3): 9, ('Arrowhead', 3): 8, ('Horseshoe', 3): 8,    # [canonical: gauge_mb.py ANCHOR_MAP — T3 anchor columns]
    ('GappedLine', 3): 7, ('RefusedFlank', 3): 9, ('Column', 3): 9,  # [canonical: gauge_mb.py ANCHOR_MAP — T3 anchor columns]
}
TIER = 3                                  # [canonical: sim_mb_06_v9_historical_spec.md — T3 uniform stats]
N_SEEDS = 24                              # [canonical: gauge_mb.py matchup — deterministic seed battery]
SEED_BASE = 1_000_000                     # [canonical: gauge_mb.py matchup — seed base]
MAX_TURNS = 20                            # [canonical: gauge_mb.py — multi-mode battle-turn cap]


def make_unit(shape, name, faction, **kw):
    """Single-subunit unit at tier-3 defaults (P4/C4/D5/M6 infantry). Dogfoods the wrapper adapter
    engine.build_unit — resolving the deployment column here, the engine builds the data model. If the
    battery digest is unchanged vs the direct-construction baseline, build_unit is provably transparent."""
    anchor_col = ANCHOR_MAP.get((shape, TIER), ANCHOR_MAP[('Line', TIER)])
    return build_unit(shape, TIER, name, faction, anchor_col,
                      troop_type=kw.pop('troop_type', 'infantry'),
                      unit_type=kw.pop('unit_type', 'melee'),
                      power=kw.pop('power', 4),             # [canonical: sim_mb_06_v9_historical_spec.md — P4]
                      command=kw.pop('command', 4),         # [canonical: sim_mb_06_v9_historical_spec.md — C4]
                      discipline=kw.pop('discipline', 5),   # [canonical: sim_mb_06_v9_historical_spec.md — D5]
                      morale=kw.pop('morale', 6),           # [canonical: sim_mb_06_v9_historical_spec.md — M6]
                      morale_start=kw.pop('morale_start', None),
                      stance=kw.pop('stance', 'balanced'),
                      speed=kw.pop('speed', 'Standard'),
                      instructions=tuple(kw.pop('instructions', ())))


# Fixed battery: (label, shape_a, shape_b, kwargs_a, kwargs_b). Spans melee mirror / wedge /
# envelopment / oblique / manipular + cavalry charge / braced-repel / shaken / ranged / volley so
# both the PER_CELL=0 and PER_CELL=1 code paths are exercised.
BATTERY = [
    ('mirror',       'Line', 'Line', {}, {}),
    ('wedge',        'Arrowhead', 'Line', {}, {}),
    ('envelop',      'Horseshoe', 'Line', {}, {}),
    ('cannae',       'Horseshoe', 'Arrowhead', {}, {}),
    ('oblique',      'RefusedFlank', 'Horseshoe', {}, {}),
    ('manipular',    'GappedLine', 'Arrowhead', {}, {}),
    ('cav_charge',   'Arrowhead', 'Line', {'troop_type': 'cavalry', 'speed': 'Fast'}, {}),
    ('cav_braced',   'Arrowhead', 'Line', {'troop_type': 'cavalry', 'speed': 'Fast'},
                     {'stance': 'hold', 'discipline': 8, 'instructions': ('brace',)}),  # [canonical: gauge_mb.py CAV — braced disc8+brace]
    ('cav_shaken',   'Arrowhead', 'Line', {'troop_type': 'cavalry', 'speed': 'Fast'},
                     {'morale': 2, 'morale_start': 6}),  # [canonical: gauge_mb.py CAV — shaken morale 2-of-6]
    ('ranged',       'Line', 'Line', {'unit_type': 'ranged', 'stance': 'hold'}, {}),
]


def _fmt(x):
    """Stable float formatting so the digest is reproducible (a pure code move yields identical floats)."""
    return f"{x:.9f}" if isinstance(x, float) else str(x)


def trial_vector(ua, ub, r):
    """Canonical end-state vector — sensitive to any numeric drift."""
    def g(u, a):
        return getattr(u, a, None)
    fields = [
        r.get('winner', '?'), r.get('battle_turns', r.get('turns', -1)),
        g(ua, 'hp'), g(ub, 'hp'), g(ua, 'hp_max'), g(ub, 'hp_max'),
        g(ua, 'morale'), g(ub, 'morale'), g(ua, 'discipline'), g(ub, 'discipline'),
        bool(g(ua, 'routed')), bool(g(ub, 'routed')),
    ]
    return '|'.join(_fmt(x) for x in fields)


# Golden digests for the Stage-1 (behaviour-frozen) baseline. A pure code-move refactor must
# reproduce these. They are updated ONLY on an intentional behaviour change (a later stage), with the
# change recorded in tests/coverage_matrix.md — exactly like the gauge digest history (e.g. ED-1032).
EXPECTED = {
    'unit': '7be8499b4fe6a047a4c01e925719e11d5214ae0c124c784f929bc69ad6511725',
    'cell': '1c5b2851b75761e35cf8d54283af82269383e5c70b894d021eaed981c716d4a7',
}


def compute():
    mode = 'cell' if os.environ.get('PER_CELL', '0') not in ('0', '', 'false', 'False') else 'unit'
    h = hashlib.new('sha256')
    for label, sa, sb, ka, kb in BATTERY:
        if (sa, TIER) not in ANCHOR_MAP or (sb, TIER) not in ANCHOR_MAP:
            continue
        for s in range(N_SEEDS):
            random.seed(s + SEED_BASE)
            ua = make_unit(sa, 'A', 'A', **ka)
            ub = make_unit(sb, 'B', 'B', **kb)
            r = resolve_battle(ua, ub, sa, sb, ANCHOR_MAP, kind='multi', max_battle_turns=MAX_TURNS)
            h.update((label + '#' + str(s) + ':' + trial_vector(ua, ub, r) + '\n').encode())
    return mode, h.hexdigest()


def main():
    mode, digest = compute()
    print(f"DIGEST {mode} {digest}")
    if '--check' in sys.argv:
        exp = EXPECTED.get(mode)
        if digest == exp:
            print(f"[BYTE-EXACT OK] {mode} matches baseline")
            return 0
        print(f"[BYTE-EXACT FAIL] {mode}: expected {exp}, got {digest}")
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
