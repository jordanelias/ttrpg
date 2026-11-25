"""B24.03 -- the hearing's rosters and the `a verdict` prize row (HEAR_B edit 1; U5c_VERBS_residue §2).

What the loader reads, as rows: the five moves the hearing adds beside `argue`, `press`, `concede` and `rest`, the faults a sitting
records, the issue ladder's `procedure` head, and the prize `a verdict` with its bench. Later items of Batch B24-sc-hearing add
their named tests to this file.
"""
from __future__ import annotations

from ..data import rosters as R
from ..data.rosters import PROCEEDING_FAULTS, PROCEEDING_MOVES, ISSUE_RUNGS, roster_map
from ..manifest import registry

HEARING_MOVES = ("present", "answer", "impugn", "rule", "adjourn")


def test_the_hearing_rosters_load_with_the_rows_named():
    assert tuple(PROCEEDING_MOVES)[:4] == ("argue", "press", "concede", "rest")    # the speech's four keep their place and their cells
    assert tuple(PROCEEDING_MOVES)[4:] == HEARING_MOVES
    effects = R.roster("proceeding_effects", ordered=True)
    assert {PROCEEDING_MOVES[m]["effect"] for m in HEARING_MOVES} == {"exhibit", "answer", "impugn", "rule", "adjourn"} <= set(effects)
    assert [m for m, r in PROCEEDING_MOVES.items() if r["draw"]] == ["argue", "press", "answer", "impugn"]
    assert {PROCEEDING_MOVES[m]["capability"] for m in ("answer", "impugn")} == {"argue"}
    assert {m for m, r in PROCEEDING_MOVES.items() if r.get("descends")} == {"concede"}
    # no effect, and so no move, names a winner or a side (V2 p2 §D: the close is each adjudicator's own draw)
    assert not [e for e in effects if any(w in e for w in ("win", "lose", "side", "verdict"))]
    assert PROCEEDING_FAULTS == ("self_contradiction", "silence", "forgery_found", "irrelevance")
    assert tuple(ISSUE_RUNGS) == ("procedure", "fact", "definition", "justification")
    assert ISSUE_RUNGS["procedure"]["weighs"] == {}                                  # every ground alike
    assert all(ISSUE_RUNGS[r]["weighs"] for r in ("fact", "definition", "justification"))


def test_the_verdict_prize_is_heard_by_the_bench_and_sat_at_encounter():
    row = roster_map("contest_subsystems", "prizes")["a verdict"]
    assert (row["heard_by"], row["step"], row["declares"]) == ("bench", "ENCOUNTER", "Declared")
    assert (row["module"], row["provider"]) == (roster_map("contest_subsystems", "prizes")["a matter"]["module"],
                                                  roster_map("contest_subsystems", "prizes")["a matter"]["provider"])
    assert (("contest", "a verdict") in registry.check_rows())                         # `_check_heard_by` and the step pair read the row at boot

