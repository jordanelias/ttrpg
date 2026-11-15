"""The edits `U5a_CORE_owed_edits` §B owed the season loop, one test each, written before the edit and read red.

Nothing here is a shared pin; each test names the falsifier its edit answers.
"""
from __future__ import annotations

import random

import pytest

from engine.season.data.matrix import Step, WriteClass
from engine.season.data.verbs import VERB_TABLE
from engine.season.gaps import InstrumentDefect
from engine.season.harness.populated import build_realm
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
    act = Act(id="m1", actor="p_npc_033", verb="march", payload={"subject": "set_s_036"}, via="off_spymaster")
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
    ok = sigma.resolve(*args, **kw, rng=random.Random(3))
    assert ok["status"] == "RESOLVED", ok
    with pytest.raises(InstrumentDefect, match="sigma"):
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


def test_event_place_at_answers_the_place_at_emission():
    """§B row 17: `event_place_at(w, e)` answers the rung of the actor's `contain` edge live at `e.emitted_at`, so an
    Event's place is recoverable after the actor has moved (`event_place` answers where the actor stands NOW, which is
    WITNESS's read at the Event's own tick and stays).

    Realm, seed 0, two seasons: the season-0 act Events are placed by `event_place` at the close of season 0 (that is
    the place at emission, the world has not moved since); after season 1, those whose `event_place` differs must be
    answered by `event_place_at` with the season-0 place.

    FALSIFIER: any such Event answers the later place (or none). The count of Events checked is asserted and printed,
    so a world in which nobody moved cannot pass."""
    from engine.season.harness import probes as P
    from engine.season.loop.driver import resolvable_verbs
    from engine.season.queries import world_q

    w = build_realm(0)
    d = SeasonDriver(w)
    ch = P.chooser(w, verbs=resolvable_verbs())

    def one_season():
        d.season(ch, question=None, contest_max_depth=w.fixtures.get("contest_max_depth"))

    one_season()
    at_emission = {e.id: world_q.event_place(w, e) for e in w.log
                   if world_q.causing_act(w, e) is not None and e.emitted_at == 0}
    assert at_emission, "season 0 emitted no act Event"
    one_season()
    moved = [e for e in w.log if e.id in at_emission and world_q.event_place(w, e) != at_emission[e.id]]
    checked, wrong = 0, []
    for e in moved:
        if at_emission[e.id] is None:
            continue                       # no place at emission: nothing to recover
        checked += 1
        if world_q.event_place_at(w, e) != at_emission[e.id]:
            wrong.append((e.id, e.kind, at_emission[e.id], world_q.event_place_at(w, e)))
    print(f"event_place_at: {checked} season-0 act Events whose event_place differs a season later "
          f"({len(moved)} differ in all, {len(at_emission)} act Events in season 0)")
    assert checked >= 1, "no season-0 act Event moved: the test observed nothing"
    assert not wrong, f"event_place_at answered a later place for {len(wrong)} Events: {wrong[:5]}"
