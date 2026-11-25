"""B04.18 -- THE ONE SOCIAL SKILL: `law` (ED-IN-0378: the social contest's V2 governs; `insight`, `deception` and
`rhetoric` are not created).

`references/descriptor_registry.yaml: capabilities.rows` is the one definition of a skill; the leaf reader
`engine/substrate/descriptors.py::CAPABILITIES` reads it from `engine/engine_params/descriptors.json`.
"""
from __future__ import annotations

import pytest

from engine.season.data import rosters as R
from engine.season.gaps import Unspecified
from engine.substrate import descriptors


def test_rhetoric_is_not_a_capability_row():
    rows = set(descriptors.CAPABILITIES)
    assert "law" in rows
    for absent in ("rhetoric", "insight", "deception"):
        assert absent not in rows, f"{absent} is not a skill row (D-U1-03; ED-IN-0378)"
    law = descriptors.capability("law")
    # B05.25 step 7: a skill row carries no `base:` and no `opposed_by:` (the verb row names its attributes); was
    # `law.base == "attr.mind.acuity" and law.opposed_by is None`
    assert law.kind == "skill" and not hasattr(law, "base") and not hasattr(law, "opposed_by")
    assert (law.floor, law.ceiling) == (0, 7) and law.grows_by == ("train", "practice")
    assert "judge" not in law.gloss.lower()  # a judge's close rolls no skill (V2 part 2 §D)


# B24.04 -- each rolled move names the skill it draws on (HCAP edit 3). A plant is a row the loader is handed, never a shipped row.
_RUNGS = tuple(R.ISSUE_RUNGS)
_BY_RUNG = {"procedure": "law", "definition": "law", "fact": "argue", "justification": "argue"}


def _move(**cells):
    return [{"id": "m", "effect": "track", **cells}]


def test_each_rolled_move_draws_on_the_skill_its_rung_names():
    moves = R.PROCEEDING_MOVES
    assert moves["argue"]["capability"] == moves["answer"]["capability"] == _BY_RUNG          # answer is a rolled move: argue's map (D-02)
    assert set(_BY_RUNG) == set(_RUNGS) and set(_BY_RUNG.values()) <= set(descriptors.CAPABILITIES)
    assert moves["impugn"]["capability"] == "argue"                                          # an attack on a source, made to the room
    assert [m for m, r in moves.items() if not r["draw"]] == ["concede", "rest", "present", "rule", "adjourn"]
    assert not [m for m, r in moves.items() if not r["draw"] and "capability" in r]          # a draw-free move names no skill


def test_a_rolled_move_with_no_capability_is_refused():
    with pytest.raises(Unspecified, match="draws and names no skill"):
        R._load_proceeding_moves(_move(draw=True), _RUNGS)
    assert R._load_proceeding_moves(_move(draw=True, capability="argue"), _RUNGS)["m"]["capability"] == "argue"          # control: the same row, with one
    assert R._load_proceeding_moves(_move(draw=True, capability=dict(_BY_RUNG)), _RUNGS)["m"]["capability"] == _BY_RUNG


@pytest.mark.parametrize("cell, draw, said", [
    ("rhetoric", True, "rhetoric"),                                                       # not a skill (D-U1-03)
    ({**_BY_RUNG, "fact": "deception"}, True, "deception"),                              # an unknown id inside a map
    ({k: v for k, v in _BY_RUNG.items() if k != "fact"}, True, "fact"),                  # a map missing a rung
    ({**_BY_RUNG, "equity": "law"}, True, "equity"),                                     # a key that is no rung
    ("argue", False, "draws nothing"),                                                    # a skill on a draw-free move
    (dict(_BY_RUNG), False, "draws nothing"),
])
def test_a_capability_cell_the_roster_cannot_close_is_refused(cell, draw, said):
    with pytest.raises(Unspecified, match=said):
        R._load_proceeding_moves(_move(draw=draw, capability=cell), _RUNGS)
