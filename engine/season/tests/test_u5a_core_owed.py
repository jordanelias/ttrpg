"""The edits `U5a_CORE_owed_edits` §B owed the season loop, one test each, written before the edit and read red.

Nothing here is a shared pin; each test names the falsifier its edit answers.
"""
from __future__ import annotations

import random
from engine.dice_engine import draw

import pytest

from engine.season.data.matrix import Step, WriteClass
from engine.season.data.verbs import VERB_TABLE
from engine.season.gaps import InstrumentDefect
from engine.season.boot.realm import build_realm
from engine.season.loop.driver import SeasonDriver, mint_token
from engine.season.seam.wrappers import sigma
from engine.season.state.carriers import Act
from engine.season.tests.test_u7_remit import _world


def test_contest_error_at_depth_zero_emits_one_refusal():
    """§B row 4: a contest that reaches the depth cap emits its row's refusal, so an act never leaves the fold with
    no Event.

    A hand-built `march` (the fight is deferred to ENCOUNTER, `the body`'s `step:`) is declared at RESOLVE, then
    folded at ENCOUNTER with `contest_max_depth=0`: `contest()` returns `ContestError("max_depth reached")` before it
    rolls. FALSIFIER: the fold returns `[]` (the act has no Event). The declaration beforehand is the control that the
    act was admitted and reached the contest at all, and the kind read is the row's own `emits_on_refusal`."""
    w = build_realm(0)
    act = Act(id="m1", actor="p_npc_036", verb="march", payload={"subject": "set_s_036"}, via="off_royal_marshal")   # a seat granting `dispatch` (the Spymaster's grant is `issue` alone, B21.03)
    d = SeasonDriver(w)
    w.step = Step.RESOLVE
    w.frozen = False
    declared = d.resolve(mint_token(w, WriteClass.ACTS), [act], 0)
    assert [e.kind for e in declared] == ["march.declared"], "the act did not reach the contest as a declaration"
    produced = d.encounter(mint_token(w, WriteClass.ACTS), declared, 0)
    row = VERB_TABLE["march"]
    assert [e.kind for e in produced] == [row.emits_on_refusal[0]], (
        f"a contest at depth cap 0 left {[e.kind for e in produced]}, not the one refusal {row.emits_on_refusal}")


def test_sigma_provider_with_no_rng_raises_instrument_defect():
    """§B row 6: the social contest provider handed no generator refuses, naming itself, in place of drawing from a
    fresh unseeded `random.Random()`.

    A direct call with `rng=None` on a world the provider can roll. FALSIFIER: the call returns a RESOLVED dict (it
    drew from a generator nobody seeded). The control is the same call handed `random.Random(3)`: it resolves, so the
    refusal is the missing generator and not the party, the verb or the prize."""
    w, _d = _world()
    args = (w, ["p_low", "p_mid"], ["c"], "a standing")
    kw = dict(verb="tell", subject="p_mid")
    ok = sigma.resolve(*args, **kw, rng=draw.seeded(draw.H2("test_u5a_core_owed", 3)))
    assert ok["status"] == "RESOLVED", ok
    with pytest.raises(InstrumentDefect, match="sigma"):
        sigma.resolve(*args, **kw, rng=None)
    with pytest.raises(TypeError, match="rng"):      # B06.05: the parameter has no default, so none at all fails at the call
        sigma.resolve(*args, **kw)


def test_scene_budget_zero_refuses_at_construction():
    """§B row 18: a season with no lap is not a season, so a `scene_budget` under one is refused when the driver is
    CONSTRUCTED (a boot refusal naming the fixture), never raised in play.

    FALSIFIER: `SeasonDriver(w)` constructs at `scene_budget = 0`, and a season would run and deposit nothing. The
    control is the shipped value (and 1, the tick's own control arm): the driver constructs, so the refusal is the
    bound and not construction itself."""
    from engine.season.gaps import Forbidden, expect_refusal

    w = build_realm(0)
    assert SeasonDriver(w).w is w, "the shipped scene_budget did not construct"
    w.fixtures = w.fixtures.sweep("scene_budget", 1)
    SeasonDriver(w)
    for bad in (0, -1):
        w.fixtures = w.fixtures.sweep("scene_budget", bad)
        with expect_refusal(), pytest.raises(Forbidden, match="scene_budget"):
            SeasonDriver(w)
