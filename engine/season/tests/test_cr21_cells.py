"""CR-21 (M14) -- THE CELL-VALUE AND COSINE PASS, its falsifiers executed.

CR-21's EXIT and FALSIFIER (its plan entry left the plan at B10-07b's close, P3; the commits are the record): a test over
`PURSUIT_PROJECTION` that reads cos(wealth, happiness) 0.818 (0.969 before), computed here from the
roster's own 15x7 table and not through `data.pursuits`; a planted deontological witness of a `release`
that ends a vow reads LOWER regard for the releaser with the `deed:commitment.ended` cells than without;
the loader refuses `restore` or `thread_read` if celled and also listed `uncelled:`.
CONTROL: the pre-pass table reproduces 0.969 by evaluating the OLD cell. The `doctrine` row is not touched; its
pair (+0.229 before and after the pass) is recorded in the commit body and NOT pinned here, as
`test_in08_cells.py` records it without gating it (the row is PROVISIONAL, Jordan's).

Each cell value is asserted off the shipped table it lives in, and each loader case runs on a PLANTED
copy, so the shipped table is never edited.
"""
from __future__ import annotations

import copy

import pytest

from ..data import verbs as V
from ..data.rosters import PURSUIT_AXES, PURSUITS, table, table_meta
from ..gaps import Forbidden
from ..queries import person_q as PQ
from ..state.carriers import Claim, Person

DI = "deontological_instrumental"
PS = "precedent_substantive"


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


# ---- H-146's repair (CR-21 commit 2): the refusing pole is DATA, read by `refuses` -----------------------
from ..data import rosters as R                      # noqa: E402
from ..decision.options import refusal_tolerance, refuses   # noqa: E402
from ..gaps import Unspecified                       # noqa: E402


def _deontological_axis() -> str:
    """The one axis the roster authors a refusing pole for -- found in the data, not named."""
    authored = sorted(R.roster_map("pursuit_axes", "refusing_pole"))
    assert len(authored) == 1 and authored[0] in PURSUIT_AXES, authored
    return authored[0]


def _planted_cells(monkeypatch, axis: str):
    monkeypatch.setattr(V, "ALIGNMENT", {axis: {"v_toward_pos": 0.3, "v_toward_neg": -0.6, "v_unengaged": 0.0}})
    # B10.21: `refuses` gates only a verb the roster lists as refusable, so the synthetic verbs are listed for the gate under test
    monkeypatch.setitem(R._ROSTERS["pursuit_axes"], "refusable", {axis: ["v_toward_pos", "v_toward_neg", "v_unengaged"]})


def test_cr21_a_verb_off_the_refusable_list_is_never_refused_however_far_past_his_tolerance(monkeypatch):
    """B10.21: the gate refuses a LISTED verb only. One listed verb and one off the list carry the same cell past a
    person's tolerance: the listed one is refused, the other never; and listing the other makes the same cell refuse
    (the verdict follows the roster, nothing else)."""
    axis = _deontological_axis()
    listed = sorted(R.roster_map("pursuit_axes", "refusable")[axis])
    assert listed, "the ruled axis lists no refusable verb"
    off = "v_off_the_list"
    assert off not in listed
    monkeypatch.setattr(V, "ALIGNMENT", {axis: {listed[0]: 0.3, off: 0.3}})
    weight = -0.4
    assert refuses(listed[0], axis, weight) is True
    assert refuses(off, axis, weight) is False
    monkeypatch.setitem(R._ROSTERS["pursuit_axes"], "refusable", {axis: [*listed, off]})
    assert refuses(off, axis, weight) is True                    # CONTROL: the list, not the cell, was what held it back


def test_cr21_refuses_reads_the_pole_from_the_roster_the_shipped_pole_is_the_first_named(monkeypatch):
    axis = _deontological_axis()
    assert R.refusing_pole(axis) == -1                         # the NEG pole refuses (ED-IN-0261)
    _planted_cells(monkeypatch, axis)
    weight = -0.4                                              # a person weighted toward the refusing pole
    assert refuses("v_toward_pos", axis, weight) is True       # further toward the other pole than he tolerates
    assert refuses("v_toward_neg", axis, weight) is False      # past him on his own side: tolerated
    assert refuses("v_unengaged", axis, weight) is False       # a zero cell is no *certain action*
    assert refuses("v_toward_pos", axis, 0.3) is False         # equal is not past


def test_cr21_a_roster_with_the_poles_swapped_inverts_the_verdict(monkeypatch):
    axis = _deontological_axis()
    _planted_cells(monkeypatch, axis)
    weight = -0.4
    shipped = (refuses("v_toward_pos", axis, weight), refuses("v_toward_neg", axis, weight))
    assert shipped == (True, False)
    monkeypatch.setitem(R._ROSTERS["pursuit_axes"], "refusing_pole", {axis: 1})
    assert R.refusing_pole(axis) == 1
    swapped = (refuses("v_toward_pos", axis, weight), refuses("v_toward_neg", axis, weight))
    assert swapped == (False, True), swapped                   # inverted on both verbs
    assert refuses("v_unengaged", axis, weight) is False       # engagement is not a pole question
    monkeypatch.undo()
    _planted_cells(monkeypatch, axis)
    assert (refuses("v_toward_pos", axis, weight), refuses("v_toward_neg", axis, weight)) == shipped


def test_cr21_an_axis_with_no_authored_pole_or_a_malformed_one_refuses_rather_than_defaulting(monkeypatch):
    axis = _deontological_axis()
    other = sorted(a for a in PURSUIT_AXES if a != axis)[0]
    with pytest.raises(Unspecified, match="authors no refusing pole"):
        R.refusing_pole(other)
    _planted_cells(monkeypatch, other)
    with pytest.raises(Unspecified, match="authors no refusing pole"):
        refuses("v_toward_pos", other, -0.4)                   # the gate cannot arm on an unruled axis
    checked = 0
    for bad in (0, 2, -2, "negative", None, True):
        monkeypatch.setitem(R._ROSTERS["pursuit_axes"], "refusing_pole", {axis: bad})
        with pytest.raises(Unspecified, match="not -1 or 1"):
            R.refusing_pole(axis)
        checked += 1
    monkeypatch.setitem(R._ROSTERS["pursuit_axes"], "refusing_pole", {axis: -1, "not_an_axis": 1})
    with pytest.raises(Unspecified, match="not on the roster"):
        R.refusing_pole(axis)
    assert checked == 6


def test_cr21_arming_the_gate_on_an_axis_with_no_authored_pole_refuses_before_any_verb_is_met():
    """C3 of the batch review: the pole was read only inside `refuses`, after `bool(a)`, so an axis with no authored
    pole and no engaged verb armed silently. `refusal_tolerance` is what an armed `refusal_axis` meets first."""
    axis = _deontological_axis()
    other = sorted(a for a in PURSUIT_AXES if a != axis)[0]
    person = Person("p_cr21_arm", "an armed person")
    person.pursuits = {"honour": 1.0}
    assert isinstance(refusal_tolerance(person, axis), float)       # the ruled axis arms
    with pytest.raises(Unspecified, match="authors no refusing pole"):
        refusal_tolerance(person, other)                             # an unruled one refuses at arming
    assert refusal_tolerance(person, None) is None                   # unarmed stays inert
