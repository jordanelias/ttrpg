"""The cast loader refuses a faction cell it cannot have read whole (an unquoted `#` eats the tail)."""
import re

import pytest

from engine.season.data import cast
from engine.season.gaps import Unspecified


def test_an_unbalanced_faction_cell_is_refused(tmp_path, monkeypatch):
    real = cast.NPC_REGISTRY_YAML.read_text(encoding="utf-8")
    planted = tmp_path / "npc_registry.yaml"
    planted.write_text(re.sub(r"(faction:\s*)[^\n]*", r"\1Crown (Seat", real, count=1), encoding="utf-8")
    monkeypatch.setattr(cast, "NPC_REGISTRY_YAML", planted)
    monkeypatch.setattr(cast, "_CACHE", None)
    with pytest.raises(Unspecified, match="unbalanced parenthesis"):
        cast.load()
    assert cast._CACHE is None   # a refused load keeps nothing
