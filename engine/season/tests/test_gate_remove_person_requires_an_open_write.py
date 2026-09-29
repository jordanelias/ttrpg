"""`GATE-REMOVE-PERSON` (plan position 7, 2026-09-29) -- `World.remove_person` now REFUSES when
called with no gate write open, making AX-4 (`04:115`, "one write path") mechanical for this
function instead of a discipline on its three callers (`state/world.py::remove_person`'s own
docstring has the full history).

THREE ARMS, so this is a measurement and not a one-sided claim (`CLAUDE.md` §0.1 pt 4):

  1. THE FALSIFIER. A bare `w.remove_person(...)` -- no `World.write` window open -- raises
     `InstrumentDefect` and touches nothing: the check is the function's first line, before any
     Tenure closure or `persons.pop`.
  2. THE CONTROL. The exact pattern the tree's three real callers already use --
     `world.write(..., apply=lambda: w.remove_person(...))`, `loop/matter.py`'s own shape -- still
     succeeds unchanged: the person is gone, their edges are closed, and the write's own receipt
     machinery runs exactly as it did before this position (already covered end to end by
     `test_season_shape.py::test_the_partition_seam_is_bounded_by_causation_not_by_the_column` and
     probe P24; reasserted here, narrowly, as this file's own control rather than borrowed).
  3. THE REALISTIC CASE, added at the Phase-1 methodology close (2026-09-29), after this file's
     own first cut tested only a PRISTINE world. `World.write`'s success path did not call
     `gate.close()` when this position first shipped -- only its two refusal branches did -- so
     `gate.is_open` stayed permanently True the instant any world completed its FIRST successful
     write, making arm 1's guard vacuous for every world that had ever done normal play (see
     `state/world.py::write`'s and `remove_person`'s own corrected history, and `hole_register.yaml`
     `H-131`). This arm proves the fix: a write succeeds, the gate closes again, and a LATER bare
     call still raises -- the scenario arm 1 alone could not distinguish from the vacuous-guard
     failure mode, because a pristine world and a "closed again after one write" world both start
     that assertion with `is_open` False."""
from __future__ import annotations

import pytest

from ..data.matrix import Step, WriteClass
from ..gaps import InstrumentDefect
from ..harness.probes import tiny_world
from ..loop.driver import mint_token
from ..state.ids import ROOT


def test_a_bare_call_with_no_write_open_raises_and_mutates_nothing():
    w = tiny_world()
    victim_edges = [t for t in w.tenures if (t.subject == "p_high" or t.object == "p_high")
                    and t.live]
    assert victim_edges, "fixture: p_high owns or is named by no live edge"
    assert not w.gate.is_open, "fixture: a fresh World must not start with a write window open"

    with pytest.raises(InstrumentDefect):
        w.remove_person("p_high")

    assert "p_high" in w.persons, "the refused call removed the person anyway"
    assert all(t.live for t in victim_edges), "the refused call closed an edge anyway"


def test_the_same_call_wrapped_in_the_real_callers_own_pattern_still_succeeds():
    """The control arm: `loop/matter.py`'s own shape (`w.write(..., apply=lambda: ...)`), not a
    new one invented for this test."""
    w = tiny_world()
    w.step = Step.MATTER
    victim_edges = [t for t in w.tenures if (t.subject == "p_high" or t.object == "p_high")
                    and t.live]
    assert victim_edges, "fixture: p_high owns or is named by no live edge"

    w.write("Tenure", mint_token(w, WriteClass.MATTER), lambda: w.remove_person("p_high"),
            record_kind="Tenure", fieldname="until", driver="Event",
            caused_person_exists="p_high", emits="tenure.closed", subject="p_high",
            causes=[ROOT])

    assert "p_high" not in w.persons
    assert all(not t.live for t in victim_edges), "a live edge survived the death"


def test_a_bare_call_after_a_prior_successful_write_still_raises():
    """The realistic case: this is NOT a pristine world. One legitimate write has already
    succeeded, and the gate must have closed again -- not stayed open from that write -- or a
    later bare call would wrongly slip through. Uses a DIFFERENT victim (`p_other`) than the one
    the prior write removed, so this call is genuinely unrelated to it, not a second write on the
    same closure."""
    w = tiny_world()
    w.step = Step.MATTER
    w.write("Tenure", mint_token(w, WriteClass.MATTER), lambda: w.remove_person("p_high"),
            record_kind="Tenure", fieldname="until", driver="Event",
            caused_person_exists="p_high", emits="tenure.closed", subject="p_high",
            causes=[ROOT])
    assert "p_high" not in w.persons, "fixture: the prior write did not actually succeed"
    assert not w.gate.is_open, (
        "the gate stayed open after a successful write -- the exact regression this test exists "
        "to catch (H-131 / the methodology-close antagonist finding on plan position 7)")

    with pytest.raises(InstrumentDefect):
        w.remove_person("p_other")

    assert "p_other" in w.persons, "the refused call removed the person anyway"
