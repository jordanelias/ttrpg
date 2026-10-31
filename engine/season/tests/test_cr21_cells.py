"""CR-21 (M14) -- THE CELL-VALUE AND COSINE PASS, its falsifiers executed.

`workplans/valoria_master_workplan_v10_part4.md` CR-21, EXIT and FALSIFIER: a test over
`PURSUIT_PROJECTION` that reads cos(wealth, happiness) 0.818 (0.969 before), computed here from the
roster's own 15x7 table and not through `data.pursuits`; a planted deontological witness of a `release`
that ends a vow reads LOWER regard for the releaser with the `deed:commitment.ended` cells than without;
the loader refuses `restore` or `thread_read` if celled and also listed `uncelled:`.
CONTROL: the doctrine pair is unchanged by this pass (the `doctrine` row is not touched), and the
pre-pass table reproduces 0.969 by evaluating the OLD cell.

Each cell value is asserted off the shipped table it lives in, and each loader case runs on a PLANTED
copy, so the shipped table is never edited.
"""
from __future__ import annotations

import copy
import math

import pytest

from ..data import verbs as V
from ..data.pursuits import to_axes
from ..data.rosters import PURSUIT_AXES, PURSUITS, table, table_meta
from ..gaps import Forbidden
from ..queries import person_q as PQ
from ..state.carriers import Claim, Person
from .test_in08_cells import _doctrine_pair_cosine

DI = "deontological_instrumental"
RF = "rigid_flexible"
PS = "precedent_substantive"


def _cosine(rows: dict, a: str, b: str) -> float:
    """cos(a, b) between two pursuits' rows of a 15x7 projection table: the arithmetic done here, off the
    roster's own table, so the number is the decision's computation re-run and not `pursuit_cosine`'s."""
    va = [float(rows[a][ax]) for ax in sorted(PURSUIT_AXES)]
    vb = [float(rows[b][ax]) for ax in sorted(PURSUIT_AXES)]
    return sum(x * y for x, y in zip(va, vb)) / (math.sqrt(sum(x * x for x in va)) * math.sqrt(sum(y * y for y in vb)))


def test_cr21_wealth_and_happiness_read_0_818_and_the_pre_pass_table_reproduces_0_969():
    rows = table("pursuit_projection")
    assert len(rows) == len(PURSUITS) and all(len(r) == len(PURSUIT_AXES) for r in rows.values())
    now = _cosine(rows, "wealth", "happiness")
    assert round(now, 3) == 0.818, now
    # the CONTROL: evaluate the OLD cell (D/I +0.4) on a copy and the pre-pass number comes back
    old = copy.deepcopy(rows)
    assert rows["happiness"][DI] == 0.0, "the shipped happiness D/I is the new cell"
    old["happiness"][DI] = 0.4
    before = _cosine(old, "wealth", "happiness")
    assert round(before, 3) == 0.969, before
    assert before > now                                   # the pass moved the cosine the way it was meant to
    # and the runtime reader agrees with the arithmetic above (the live binding, not the raw table)
    from ..data.pursuits import pursuit_cosine
    assert pursuit_cosine({"wealth": 1.0}, {"happiness": 1.0}) == pytest.approx(now, abs=1e-12)


def test_cr21_the_aggregate_spread_figure_moves_with_the_one_cell_and_the_old_cell_reproduces_the_old_figure():
    """`conviction_spread`'s effective-axes figure was 3.81 before the pass (the pin
    `test_conviction_spread_solver` held) and reads 3.93 after: the happiness D/I cell is the whole move.
    Evaluate the OLD cell through the instrument's own candidate parameter and 3.81 returns; the within-60-degree
    count (4 of 15) does not move."""
    from ..harness.conviction_spread import spread
    axes = sorted(PURSUIT_AXES)
    live = table("pursuit_projection")
    now = spread((axes, live))
    old = copy.deepcopy(live)
    old["happiness"][DI] = 0.4
    before = spread((axes, old))
    assert before["spectrum"]["effective_axes"] == pytest.approx(3.81, abs=0.01)
    assert now["spectrum"]["effective_axes"] == pytest.approx(3.93, abs=0.01)
    assert now["spectrum"]["effective_axes"] == pytest.approx(spread()["spectrum"]["effective_axes"], abs=1e-12)
    assert (before["within_60deg"], before["total"]) == (now["within_60deg"], now["total"]) == (4, 15)


def test_cr21_the_doctrine_pair_is_unchanged_by_the_pass(monkeypatch):
    """The `doctrine` row is NOT changed (ED-IN-0301): the pair neither holds nor projects `happiness`, so
    restoring the old happiness cell leaves its cosine exactly where it is, at the recorded +0.229."""
    shipped = _doctrine_pair_cosine()
    assert round(shipped, 3) == 0.229, shipped
    old = copy.deepcopy(V.PURSUIT_PROJECTION)
    old["happiness"][DI] = 0.4
    monkeypatch.setattr(V, "PURSUIT_PROJECTION", old)
    assert to_axes({"happiness": 1.0})[DI] == 0.4, "the planted old cell is not the one read"
    assert _doctrine_pair_cosine() == shipped
    rows = V.PURSUIT_PROJECTION
    assert rows["doctrine"][DI] == -0.3 and rows["doctrine"]["partisan_equitable"] == 0.2
    assert all(rows["doctrine"][ax] == 0.0 for ax in PURSUIT_AXES if ax not in (DI, "partisan_equitable"))


def test_cr21_the_four_value_changes_and_the_role_template_cell_are_what_the_decision_names():
    assert V.PURSUIT_PROJECTION["happiness"][DI] == 0.0
    assert V.ROLE_TEMPLATE_PURSUITS["intelligence-diplomatic"]["community"] == 0.10
    assert V.align("restore", PS) == -0.2
    assert [V.align("restore", ax) for ax in sorted(PURSUIT_AXES) if ax != PS] == [0.0] * (len(PURSUIT_AXES) - 1)
    assert V.ALIGNMENT[RF]["deed:commitment.ended"] == 0.4
    assert V.ALIGNMENT[DI]["deed:commitment.ended"] == 0.8
    # `restore` now has a celled axis, so R-08's G-1 counts it; `thread_read` is CONSIDERED and `null` on all seven
    # (the draft's §3.7 grade `null`: no source, no lean), so it leaves `uncelled:` and still scores 0.0 and counts as none
    assert "restore" in V.celled_verbs() and "thread_read" not in V.celled_verbs()
    uncelled = table_meta("alignment")["uncelled"]
    assert "restore" not in uncelled and "thread_read" not in uncelled
    cells = table("alignment")
    assert [cells[ax]["thread_read"] for ax in sorted(PURSUIT_AXES)] == [None] * len(PURSUIT_AXES)
    assert [V.align("thread_read", ax) for ax in sorted(PURSUIT_AXES)] == [0.0] * len(PURSUIT_AXES)


def _vow_break_regard(judge_pursuit: str, with_cells: bool, monkeypatch) -> float:
    """What a judge holding only `judge_pursuit` makes of ONE firsthand `commitment.ended` deed about
    `x`: `deeds_judged`'s judged half, off the live `ALIGNMENT` (the `deed:commitment.ended` cells in or out)."""
    if not with_cells:
        stripped = {ax: {k: v for k, v in row.items() if k != "deed:commitment.ended"}
                    for ax, row in V.ALIGNMENT.items()}
        monkeypatch.setattr(V, "ALIGNMENT", stripped)
    judge = Person("p_judge", "a judge")
    judge.pursuits = {judge_pursuit: 1.0}
    judge.ledger = [Claim("c_vow_broken", "p_judge", "x", "commitment.ended", True, 0, "firsthand",
                          100, "own", 0, chain=())]
    return PQ.deeds_judged(judge, "x")[0]


def test_cr21_a_deontological_witness_of_a_vow_break_reads_less_regard_with_the_cells(monkeypatch):
    # the most deontological pursuit, found on the shipped projection and not named; the most instrumental as the control
    rows = V.PURSUIT_PROJECTION
    deont = min(sorted(PURSUITS), key=lambda e: rows[e][DI])
    instr = max(sorted(PURSUITS), key=lambda e: rows[e][DI])
    assert rows[deont][DI] < 0 < rows[instr][DI]
    assert V.KIND_VERB["commitment.ended"] == "release"           # the one emitter: without cells it reads `release`'s
    with_cells = _vow_break_regard(deont, True, monkeypatch)
    monkeypatch.undo()
    without = _vow_break_regard(deont, False, monkeypatch)
    monkeypatch.undo()
    assert with_cells < without, (with_cells, without)
    assert with_cells < 0                                         # a deontological witness thinks the worse of the releaser
    # CONTROL: an instrumental witness reads the same cells the other way (the cells are read, not constant)
    i_with = _vow_break_regard(instr, True, monkeypatch)
    monkeypatch.undo()
    i_without = _vow_break_regard(instr, False, monkeypatch)
    monkeypatch.undo()
    assert i_with > i_without, (i_with, i_without)


def test_cr21_the_loader_refuses_restore_or_thread_read_celled_and_also_uncelled():
    shipped_cells = table("alignment")
    uncelled = dict(table_meta("alignment")["uncelled"])
    checked = 0
    for verb in ("restore", "thread_read"):
        planted = copy.deepcopy(shipped_cells)
        for ax in PURSUIT_AXES:
            planted[ax][verb] = 0.1 if ax == PS else None      # celled on every axis, as a celled verb must be
        with pytest.raises(Forbidden, match="is declared `uncelled:` and is celled on"):
            V._load_alignment(planted, dict(uncelled, **{verb: "planted"}))
        checked += 1
    assert checked == 2
    # and the shipped pair is lawful as it stands: `restore` celled and not listed, `thread_read` null on every axis and not listed
    V._load_alignment(shipped_cells, uncelled)
    assert V._load_alignment(shipped_cells, uncelled)[PS]["restore"] == -0.2
