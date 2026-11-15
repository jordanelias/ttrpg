"""The edits `U5a_CORE_owed_edits` §B owed the season loop, one test each, written before the edit and read red.

Nothing here is a shared pin; each test names the falsifier its edit answers.
"""
from __future__ import annotations

from engine.season.data.matrix import Step, WriteClass
from engine.season.data.verbs import VERB_TABLE
from engine.season.harness.populated import build_realm
from engine.season.loop.driver import SeasonDriver, mint_token
from engine.season.state.carriers import Act


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
