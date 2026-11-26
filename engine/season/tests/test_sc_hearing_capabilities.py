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


# B24.29 -- a reading of the bench, drawn and never revealed (HCAP edit 4). A sitting that wrote one seat's public lean is witnessed; each man in its room who does not decide holds
# his OWN keyed reading of the sign, true with chance (1 + acc) / 2 on his Attunement (`sigma.bench_reading`). A game-state test of the `sc_season` lane.
def _bench_read(attunement, trials, bench=(("p_mid", -1),)):
    """`(true, wrong)` over `trials` seeds: the readings of the seat's lean `p_low` (a speaker) and `p_other` (a bystander) hold, at `attunement`, about the seat `p_mid`."""
    from .test_sc_proceeding_host import _beat, _folded, _held, _planted, _room, _world
    true = wrong = 0
    for seed in range(trials):
        w = _world()
        w.world_seed = seed
        for who in ("p_low", "p_other"):
            w.persons[who].attributes[descriptors.ATTRIBUTE_NAMES["attunement"]] = attunement
        result = _planted([_beat(1, "p_low", "for", 0.0), _beat(2, "p_mid", "against", 0.0)], **_room())
        result["bench"] = bench
        _folded(w, result, witness=True)
        assert _held(w, "p_mid", "leans") == []                                      # a man holds no reading of himself
        for who in ("p_low", "p_other"):
            held = _held(w, who, "leans")
            assert [(s, v in (-1, 1)) for _, s, v, _ in held] == ([("p_mid", True)] if bench else [])
            true += sum(v == bench[0][1] for _, _, v, _ in held)
            wrong += sum(v == -bench[0][1] for _, _, v, _ in held)
    return true, wrong


def test_bench_reading_is_drawn_and_can_be_wrong_at_every_insight():
    """GATE 2 (`insight` is not a row: his Attunement is the reading, V2 p2 §C.6): over 400 seeds the share of readings that hold the seat's lean with the true sign is
    strictly between 0.5 and 1 at Attunement 2 and at 5, and higher at 5; a wrong sign is possible at both. CONTROL: a sitting that wrote no public lean deposits no
    `leans`. FALSIFIER: a share of 1.0 (a turn view that shows the true lean), a share that does not rise with Attunement, or a reading that is no man's own."""
    checked, share = 0, {}
    for attunement in (2, 5):
        true, wrong = _bench_read(attunement, 400)
        checked += true + wrong
        assert true + wrong == 800 and wrong > 0, (attunement, true, wrong)
        share[attunement] = true / (true + wrong)
        assert 0.5 < share[attunement] < 1.0, (attunement, share[attunement])
    assert share[5] > share[2], share
    assert checked >= 400
    assert _bench_read(5, 5, bench=()) == (0, 0)
