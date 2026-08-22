#!/usr/bin/env python3
"""Cook the world's opening position so `engine/` stops carrying it as literals.

WHY THIS EXISTS (plan S5b, 2026-08-22). `engine/autoload/game_state.py` opened with six hardcoded
tables — `ALL_PLAYABLE_15`, `STARTING_OWNER`, `STARTING_ACCORD`, `STARTING_PT`, `STARTING_GARRISON`
and `STARTING_STATS` — carried forward from `mc_v17.py` L62-82 with no authored source anywhere in
the corpus. That is world data living in the engine: changing who holds T4 at season 0 meant editing
the executable model. `references/world_initial_state.yaml` is now the source, this tool cooks it,
and `engine/substrate/world_initial_state.py` is its single runtime reader — the fifth instance of
the pattern the plan's §2 states as the target: one authored surface, one exporter, one artifact,
one leaf.

IT VALIDATES AT EXPORT TIME. Every territory declares all seven columns, owners must be factions the stats table declares, and the numeric ranges are checked against
the canon buckets they index. A typo reds a blocking CI gate rather than silently producing a world
with a territory nobody owns.

Usage:
    python3 tools/export_world_initial_state.py           # write the artifact
    python3 tools/export_world_initial_state.py --check   # re-derive and diff (exit 1 on drift)
"""
from __future__ import annotations

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ci_common  # noqa: E402

REPO = ci_common.REPO
SRC = os.path.join(REPO, 'references', 'world_initial_state.yaml')
OUT = os.path.join(REPO, 'engine', 'engine_params', 'world_initial_state.json')

#: Canon buckets these columns index — `ACCORD_MAP` is 0-4 and `PT_MAP` is 0-5
#: (`engine/autoload/game_state.py`). A value outside them has no canonical meaning, so it is a
#: defect in the authored table rather than an exotic opening position.
ACCORD_RANGE = (0, 4)
PT_RANGE = (0, 5)


def _fail(msg):
    raise SystemExit(f'[world-initial-state] {msg}')


def build():
    data = ci_common.load_yaml(SRC, default=None)
    if not data:
        _fail(f'cannot read {os.path.relpath(SRC, REPO)}')

    territories = data.get('territories') or {}
    stats = data.get('faction_starting_stats') or {}
    if not territories:
        _fail('no territories declared. If the block was emptied, the campaign has no map — '
              'restore it rather than deleting this exporter.')
    if not stats:
        _fail('no faction_starting_stats declared.')

    factions = sorted(stats)
    owners_seen = set()
    for tid, row in sorted(territories.items()):
        for field in ('owner', 'accord', 'pt', 'garrison', 'playable', 'prosperity', 'templar'):
            if field not in row:
                _fail(f'{tid} is missing {field!r}. Every territory declares all seven columns; a '
                      f'missing one would silently default and move the opening position.')
        owner = row['owner']
        if owner is not None:
            if owner not in stats:
                _fail(f'{tid} is owned by {owner!r}, which faction_starting_stats does not declare. '
                      f'Known: {factions}.')
            owners_seen.add(owner)
        if not ACCORD_RANGE[0] <= row['accord'] <= ACCORD_RANGE[1]:
            _fail(f'{tid} accord={row["accord"]} is outside the canonical 0-4 ACCORD_MAP buckets.')
        if not PT_RANGE[0] <= row['pt'] <= PT_RANGE[1]:
            _fail(f'{tid} pt={row["pt"]} is outside the canonical 0-5 PT_MAP buckets.')
        if not all(isinstance(row[f], bool) for f in ('garrison', 'playable', 'templar')):
            _fail(f'{tid}: garrison, playable and templar must be booleans.')
        if row['prosperity'] not in (1, 2):
            _fail(f'{tid} prosperity={row["prosperity"]}; the opening table only ever declares 1 or '
                  f'2. A third value may be legitimate one day — say so in the plan and relax this '
                  f'deliberately, because Territory.prosperity has no declared scale anywhere.')

    if list(stats) != ['Crown', 'Church', 'Hafenmark', 'Varfell']:
        _fail(f'faction order is {list(stats)}, expected [Crown, Church, Hafenmark, Varfell]. '
              f'This is not cosmetic: create_world iterates this table to build world.factions, so '
              f'its order sets the order of every world.factions loop and therefore the RNG draw '
              f'sequence of a seeded campaign. Reordering it MOVES THE GOLDENS. If that is the '
              f'intent, re-record them in the same commit and update this check.')

    landless = sorted(set(stats) - owners_seen)
    if landless:
        _fail(f'faction(s) {landless} hold no territory at season 0. That may be a legitimate '
              f'opening one day, but today it is far more likely a deleted row — state it in the '
              f'plan and relax this check deliberately.')

    for name, row in sorted(stats.items()):
        for field in ('L', 'Sta', 'W', 'I', 'Mil'):
            if field not in row:
                _fail(f'faction {name} is missing starting stat {field!r}.')
            if not isinstance(row[field], (int, float)):
                _fail(f'faction {name} stat {field} is not numeric: {row[field]!r}')

    return {
        '_generated': (
            'GENERATED by tools/export_world_initial_state.py from '
            'references/world_initial_state.yaml. NEVER hand-edit: regenerate and commit together. '
            'Read at runtime by engine/substrate/world_initial_state.py. Every column is validated '
            'at export time, so a broken table fails a blocking CI gate rather than producing a '
            'campaign with an unowned territory or an out-of-canon Accord bucket.'
        ),
        'schema_version': data.get('schema_version', 1),
        'source': 'references/world_initial_state.yaml',
        # ⚠ AUTHORED ORDER IS PRESERVED, AND IT IS LOAD-BEARING. `create_world` iterates
        # `faction_starting_stats` to build `world.factions`, so this dict's order becomes that
        # dict's order, which becomes the order every `world.factions.items()` loop sees, which
        # decides the sequence of RNG draws in a seeded campaign. The first draft of this exporter
        # sorted factions alphabetically — an unremarkable "for determinism" habit — and moved the
        # campaign goldens (Church 0.0 -> 50.0) without touching a single value. Sorting here is
        # not tidying; it is a balance change. Do not reintroduce it. The COLUMNS are sorted
        # because nothing iterates them.
        'territories': {t: dict(sorted(r.items())) for t, r in territories.items()},
        'faction_starting_stats': {f: dict(sorted(r.items())) for f, r in stats.items()},
    }


def main(argv):
    text = json.dumps(build(), indent=2, sort_keys=False) + '\n'
    if '--check' in argv:
        if not os.path.exists(OUT):
            print(f'[world-initial-state] MISSING {os.path.relpath(OUT, REPO)} — run without --check.')
            return 1
        if open(OUT).read() != text:
            print(f'[world-initial-state] DRIFT — {os.path.relpath(OUT, REPO)} is stale. '
                  f'Run: python3 tools/export_world_initial_state.py')
            return 1
        n = len(json.loads(text)['territories'])
        print(f'[world-initial-state] OK — {n} territories, every column validated.')
        return 0
    with open(OUT, 'w') as fh:
        fh.write(text)
    print(f'[world-initial-state] wrote {os.path.relpath(OUT, REPO)}')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
