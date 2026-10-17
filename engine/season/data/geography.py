"""`data/geography.py` -- THE GEOGRAPHY FILE, READ ONCE PER PROCESS, FOR THE BATTLE FIELD.

`files.GEOGRAPHY_YAML` (canon's world map) is a DATA INPUT of the `mass_battle` module: its terrain
lookup and river test (`modules/mass_battle/terrain.py`) read `provinces:`, `terrain:` and `water:`.
The module may not read it itself -- AX-4 leaves it no state between calls, so it re-parsed 37 KB on
every fought field, and a file it opens by path is an input outside `modules/**` that the module's
port input set cannot see. So the HOST reads it, here, and hands it on: `seam/wrappers/mass_battle.py::
field_input` puts it on the record (`queries/inputs.py::MassBattleInput.geography`).

ONE READ PER PROCESS, `data/cast.py`'s idiom: the file is repository content that cannot change under a
running season (`manifest/registry.py`'s `_CONTRACTS_CACHE` states the same licence). AX-4 binds the
module, not the host. ⚠ THE MAPPING IS SHARED by every record built in the process: nothing may write
into it (the module only reads it). A test that needs the file re-read sets `_CACHE` back to `None`.
"""
from __future__ import annotations

from typing import Optional

from .files import GEOGRAPHY_YAML
from .rosters import load_yaml

_CACHE: Optional[dict] = None


def geography() -> dict:
    """The parsed geography file, read on first use and kept (`data/rosters.load_yaml`, the package's
    one YAML reader, so a duplicated key raises rather than silently keeping the last)."""
    global _CACHE
    if _CACHE is None:
        _CACHE = load_yaml(GEOGRAPHY_YAML.read_text(encoding="utf-8")) or {}
    return _CACHE


def load() -> dict:
    """`data.load_all`'s handle on this loader: read the file now. The same cache `geography()` fills."""
    return geography()
