#!/usr/bin/env python3
"""Emit the numbers the Godot port must agree with, keyed by the port's own constant names.

WHY THIS EXISTS.

`engine/` and `references/` are the root that `systems/` stems from (Jordan, 2026-08-20). Measured
the same day, they were the root of nothing that ships: this repository generates five parameter
files under `engine/engine_params/`, each behind a blocking round-trip check, and
`jordanelias/valoria-game` reads **zero bytes** of any of them. A grep across that repo for
`engine_params`, `key_types.json`, `combat_engine_v1.json` or `params_tables` returns nothing; its
only runtime `FileAccess`/`JSON.parse` sites are scene telemetry. All ~200 constants in
`systems/util/Constants.gd` are hand-transcribed, and no gate in either repo can observe the drift.

This file is the writer half of the bridge. `valoria-game/tools/check_constants_parity.py` is the
reader half, and the pair is the fourth instance of the generate + blocking `--check` pattern that
`export_key_types.py` (ED-IN-0136) and `export_engine_params.py` already run.

WHAT THIS DOES NOT DO — and this is the whole design.

**It does not match by name.** A first pass that did was written and thrown away: bare-name matching
across the two repos produced SIX divergences, and adversarial re-checking found that *none of them
were real*. Four came from near-name guessing (`MOMENTUM_MAX` vs the kernel's `M_MAX`; `OB_CAP` vs
`SEIZURE_OB_CAP`) and two from exact-name collisions where the same word names different quantities
(below). Meanwhile the two divergences that ARE real share no name with anything and would have been
missed entirely. A number without a control is not a measurement (CLAUDE.md §0.1 pt 4), and a name
whose meaning is not idempotent across surfaces is a trap (§4).

So every pair in MAPPING was confirmed BY HAND against both call sites, COLLISIONS records the
near-misses so the next session cannot re-derive them, and DIVERGENCES records real disagreements
that need a ruling rather than a value copy.

It also composes rather than re-extracts: the values come from `sim_params.json` and
`combat_engine_v1.json`, which are already generated from the Python owners by their own exporters.
Adding a third extractor here would re-commit the duplication §8 forbids.

Usage:
    python3 tools/export_game_constants.py           # write engine/engine_params/game_constants.json
    python3 tools/export_game_constants.py --check   # re-derive and diff vs committed (exit 1 on drift)
"""
from __future__ import annotations

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ci_common  # noqa: E402

REPO = ci_common.REPO
OUT = os.path.join(REPO, 'engine', 'engine_params', 'game_constants.json')

# GD constant name -> fully qualified owner key in sim_params.json / combat_engine_v1.json.
# EVERY pair here was confirmed by reading both call sites. Never add one by name similarity.
MAPPING = {
    'TN_STANDARD':                   'engine.autoload.TN_STANDARD',
    'OB_FLOOR':                      'factions.OB_FLOOR',
    'WEAPON_TN_BASE':                'combat.WEAPON_TN_BASE',
    'COMBAT_POOL_MINIMUM':           'combat.COMBAT_POOL_MIN',
    'COHERENCE_START':               'threadwork.COHERENCE_START',
    'COHERENCE_MAX':                 'threadwork.COHERENCE_MAX',
    'COHERENCE_MIN':                 'threadwork.COHERENCE_MIN',
    'COHERENCE_FRACTURED_THRESHOLD': 'threadwork.COHERENCE_FRACTURED',
    'KNOT_FORMATION_TN':             'fieldwork.KNOT_FORMATION_TN',
    'KNOT_FORMATION_OB':             'fieldwork.KNOT_FORMATION_OB',
    'SEASONS_PER_YEAR':              'overview.SEASONS_PER_YEAR',
    'CI_START':                      'overview.CI_STARTING',
    'VICTORY_SUSTAIN_SEASONS':       'engine.autoload.SUSTAIN_SEASONS',
}

# Pairs that LOOK like matches and are NOT. Recorded so the next session does not re-derive them
# and "fix" a value that was never wrong. Each entry: why the two names are different quantities.
COLLISIONS = {
    'POOL_FLOOR': {
        'python_name': 'combat.core.POOL_FLOOR',
        'python_value': 5,
        'gd_value': 1,
        'reason': "Different quantities sharing a word. combat_engine_v1/core.py:47 POOL_FLOOR is the "
                  "COMBAT POOL minimum, used as max(POOL_FLOOR, history + BASE_POOL) at :52 — the game "
                  "calls that COMBAT_POOL_MINIMUM and it AGREES at 5. The game's POOL_FLOOR is the "
                  "universal dice-pool floor applied by RollContext.effective_pool() (RollContext.gd:26). "
                  "Not a divergence.",
    },
    'ACCORD_MIN': {
        'python_name': 'engine.autoload.ACCORD_MIN',
        'python_value': 2.0,
        'gd_value': 0,
        'reason': "Different quantities sharing a name. victory.py:28 ACCORD_MIN is a VICTORY THRESHOLD "
                  "(held territories must have accord >= 2.0, :71). Constants.gd:144-145 ACCORD_MIN/MAX "
                  "is the CLAMP RANGE for the accord tracker (SettingState.gd:34,82). Not a divergence — "
                  "but see DIVERGENCES['accord_range'], which is.",
    },
    'MOMENTUM_MAX': {
        'python_name': 'engine.autoload.M_MAX',
        'python_value': 1.5,
        'gd_value': 4,
        'reason': "M_MAX is the kernel's tanh multiplier ceiling (sigma_leverage), not a Momentum cap. "
                  "Momentum 0-4 has no scalar owner in engine/ today. Not a divergence.",
    },
    'OB_CAP': {
        'python_name': 'settlements.SEIZURE_OB_CAP',
        'python_value': -4,
        'gd_value': 20,
        'reason': "SEIZURE_OB_CAP bounds a mass-seizure Ob MODIFIER (negative); the game's OB_CAP is the "
                  "absolute Ob ceiling. Not a divergence.",
    },
}

# Real disagreements between the oracle and the port. These are NOT closed by copying a number —
# each is a model difference that needs a ruling. The parity checker reports them and does not fail
# on them; the list can only shrink.
DIVERGENCES = {
    'accord_range': {
        'engine': "accord is a CONTINUOUS float clamped to [0.5, 7.0] "
                  "(engine/autoload/game_state.py:160 adjust_accord), bucketed to a 0-4 canonical index "
                  "by ACCORD_MAP (:61, five entries 0..4) and canonical_accord "
                  "(engine/substrate/canon_buckets.py).",
        'port':   "accord is an INTEGER clamped to [0, 3] (Constants.gd:144-145, cited to "
                  "peninsular_strain_v30 §2), registered and clamped as a tracker "
                  "(SettingState.gd:34,82).",
        'why_it_matters': "Two different state models for the same field: 0-4 continuous-bucketed vs 0-3 "
                          "integer. Every accord-driven outcome differs. No gate in either repo observed "
                          "this before 2026-08-20.",
        'needs': 'ruling — which model is canonical',
    },
    'coherence_bands': {
        'engine': "SIX bands with LOW-edge encoding: Stable >=8, Dissonant 7-5 (COHERENCE_DISSONANT_LOW=5), "
                  "Fragmented 4-3 (COHERENCE_FRAGMENTED_LOW=3), Fractured ==2, Severed ==1, "
                  "Rendering Crisis ==0 (systems/threadwork/sim/coherence.py:43-47,119-125,170).",
        'port':   "FOUR bands with TOP-edge encoding: DISSONANT_THRESHOLD=6, FRAGMENTED_THRESHOLD=4, "
                  "FRACTURED_THRESHOLD=2, SEVERED_THRESHOLD=0 (Constants.gd:54-57). No Crisis band, and "
                  "the port's SEVERED=0 collides with the engine's CRISIS=0 while the engine's SEVERED=1.",
        'why_it_matters': "The ladders disagree in band COUNT, in EDGE CONVENTION, and at the Dissonant "
                          "boundary (engine 5 vs port 6). COHERENCE_FRACTURED is the only rung that "
                          "coincides, which is why it is the one coherence band in MAPPING.",
        'needs': 'ruling — band count and edge convention',
    },
}


def _load_sources():
    """Flatten the two committed exports into {qualified_key: value}. Composes; does not re-extract."""
    vals = {}
    sp = json.load(open(os.path.join(REPO, 'engine', 'engine_params', 'sim_params.json')))
    for p in sp['params']:
        if p['kind'] != 'table' and isinstance(p['value'], (int, float, bool)):
            vals[p['key']] = p['value']
    ce = json.load(open(os.path.join(REPO, 'engine', 'engine_params', 'combat_engine_v1.json')))
    for section, body in ce['sections'].items():
        for k, v in body.items():
            if isinstance(v, (int, float, bool)):
                vals[f'combat.{section}.{k}'] = v
                vals.setdefault(f'combat.{k}', v)   # unqualified alias, first section wins
    return vals


def build():
    src = _load_sources()
    missing = sorted(k for k in MAPPING.values() if k not in src)
    if missing:
        raise SystemExit(
            "MAPPING names owners that no exporter emits: " + ", ".join(missing) +
            "\nEither the owner moved (fix the key) or its exporter stopped emitting it (fix that first)."
        )
    return {
        '_generated': (
            'GENERATED by tools/export_game_constants.py from engine/engine_params/sim_params.json + '
            'combat_engine_v1.json. NEVER hand-edit: regenerate and commit together. Read by '
            'valoria-game/tools/check_constants_parity.py, which is the reader half of the bridge.'
        ),
        'schema_version': 1,
        'contract': (
            'MAPPING pairs are hand-confirmed against BOTH call sites and are the only pairs the parity '
            'checker may fail on. COLLISIONS are name look-alikes that are NOT the same quantity — never '
            'promote one into MAPPING without reading both call sites. DIVERGENCES are real model '
            'disagreements that need a ruling, not a value copy; the checker reports them and the list '
            'can only shrink.'
        ),
        'constants': {gd: src[key] for gd, key in sorted(MAPPING.items())},
        'owners': dict(sorted(MAPPING.items())),
        'collisions': COLLISIONS,
        'divergences': DIVERGENCES,
    }


def main(argv):
    data = build()
    text = json.dumps(data, indent=2, sort_keys=False) + '\n'
    if '--check' in argv:
        if not os.path.exists(OUT):
            print(f'[game-constants] MISSING {os.path.relpath(OUT, REPO)} — run without --check.')
            return 1
        if open(OUT).read() != text:
            print(f'[game-constants] DRIFT — {os.path.relpath(OUT, REPO)} is stale. '
                  f'Run: python3 tools/export_game_constants.py')
            return 1
        print(f'[game-constants] OK — {len(data["constants"])} constant(s), '
              f'{len(data["collisions"])} recorded collision(s), '
              f'{len(data["divergences"])} open divergence(s).')
        return 0
    with open(OUT, 'w') as fh:
        fh.write(text)
    print(f'[game-constants] wrote {os.path.relpath(OUT, REPO)} — {len(data["constants"])} constant(s).')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
