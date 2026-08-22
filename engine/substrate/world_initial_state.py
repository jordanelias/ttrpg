"""engine.substrate.world_initial_state — the world's opening position, read from references/.

Status: [live, 2026-08-22]

WHY. `engine/autoload/game_state.py` carried the campaign's opening position as six Python
literals inherited from `mc_v17.py` with no authored source. Who holds T4 at season 0 is world
data, and editing it should be editing a table, not editing the executable model.

`references/world_initial_state.yaml` is the authored source; `tools/export_world_initial_state.py`
cooks it into `engine/engine_params/world_initial_state.json` behind a blocking `--check`; this is
its single runtime reader. Same shape as `descriptors.py`, `composition.py` and `keys.py`.

IT IS A LEAF. stdlib only — no `engine.*`, no `systems.*`. `game_state.py` imports it at module
load, so anything it imported would become a dependency of the entire engine.

THE NAMES BELOW ARE THE ONES `game_state.py` USED, deliberately. `STARTING_OWNER` and friends are
cited across the corpus by name — flow skeletons, design docs, tests — and renaming them while
moving them would have made one change into two. The literals are gone; the vocabulary is not.
"""
from __future__ import annotations

import json
import os

_HERE = os.path.dirname(os.path.abspath(__file__))
_PATH = os.path.normpath(os.path.join(_HERE, '..', 'engine_params', 'world_initial_state.json'))

with open(_PATH) as _fh:
    _DATA = json.load(_fh)

#: {tid -> {owner, accord, pt, garrison, playable}} exactly as `references/` declares it.
TERRITORIES = _DATA['territories']

#: The playable set. Authored per-territory rather than derived from `owner`, because "unowned
#: means unplayable" is a rule nobody has stated — see the authored file's own note.
ALL_PLAYABLE = frozenset(t for t, r in TERRITORIES.items() if r['playable'])

STARTING_OWNER = {t: r['owner'] for t, r in TERRITORIES.items()}
STARTING_ACCORD = {t: r['accord'] for t, r in TERRITORIES.items()}
STARTING_PT = {t: r['pt'] for t, r in TERRITORIES.items()}

#: Only the garrisoned territories, matching the original literal's shape: `game_state` reads it
#: with `.get(tid)`, so absence means "no garrison" and a False value never appears.
STARTING_GARRISON = {t: True for t, r in TERRITORIES.items() if r['garrison']}

#: {faction -> {L, Sta, W, I, Mil}}
STARTING_STATS = {f: dict(r) for f, r in _DATA['faction_starting_stats'].items()}
