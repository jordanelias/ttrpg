"""v9 IN-59 (a) (RS-26) -- THE ATTACK HALF OF THE ACCESS GATE: `fight`, `challenge` and `accept` need
the subject WHERE THE ACTOR IS.

The carrier is ONE `relation: with` conjunct on `subject` in each row's typed `requires`
(`engine/season/verb_table.yaml`), `give`'s co-location stem: WORLD-ONLY, answered by
`queries/world_q.py::WorldReader.read` through `place_of`. Nothing else changed -- `presence:` is
still declined (`H-33`), no eligibility kind was edited.

Every case drives the verb through the real fold (`SeasonDriver.resolve`) on `probes.tiny_world`,
where `p_low` and `p_mid` live at the hearth `Hh`, `p_high` at the settlement `S` (the hearth's
parent: a different rung) and `p_king` at the realm `R`. The cause is controlled: the same actor, the
same verb and the same world, only the subject's place differs.

FALSIFIERS, each able to observe its failure (`CLAUDE.md` §0.1 pt 2):
  1. a cross-rung act EXECUTES -> the refusal assertion fails;
  2. the co-located act is REFUSED -> the execution assertion fails (the gate killed the verb);
  3. MUTATION, in-test: the same row with the `with` conjunct dropped, everything else as shipped,
     EXECUTES the cross-rung act -- so the conjunct, and nothing else on the row, is the cause.
"""
from __future__ import annotations

import dataclasses

import pytest
from unittest import mock

from engine.season.data import verbs as V
from engine.season.data.matrix import Step, WriteClass
from engine.season.data.requires import build_typed_requires
from engine.season.harness import probes as P
from engine.season.loop.driver import SeasonDriver, mint_token
from engine.season.queries import world_q
from engine.season.seam.wrappers import combat as C
from engine.season.state.carriers import Act

DUEL_VERBS = ("fight", "challenge", "accept")
# `probes.tiny_world`'s fixture ids (corpus: no exemption needed, they duplicate no roster).
ACTOR, BESIDE, ELSEWHERE, FAR = "p_low", "p_mid", "p_high", "p_king"


@pytest.fixture
def engine_available():
    """`test_combat_band_edges.py`'s fixture: `fight` and `accept` resolve through `combat_seam`, so a
    co-located one needs the combat engine; loaded when a test RUNS, never at import."""
    if C.engine() is None:
        pytest.skip(f"personal_combat engine unavailable: {C.load_error()}")
    SeasonDriver(P.tiny_world())


def _fold(verb: str, subject: str) -> list:
    w = P.tiny_world()
    w.step = Step.RESOLVE
    d = SeasonDriver(w)
    return d.resolve(mint_token(d.w, WriteClass.ACTS),
                     [Act(id="in59", actor=ACTOR, verb=verb, payload={"subject": subject})], 2)


def _refused(verb: str, evs: list) -> bool:
    kinds = set(V.VERB_TABLE[verb].emits_on_refusal)
    assert evs, f"{verb}: the fold returned no Event at all"
    return all(e.kind in kinds for e in evs)


def _without_with(verb: str):
    """The shipped row with its `with` conjunct dropped, every other conjunct and column as shipped."""
    row = V.VERB_TABLE[verb]
    cell = {"form": "existence", "of": "subject", "kind": "Person"}
    return dataclasses.replace(row, requires_typed=build_typed_requires(verb, cell))


def test_the_fixture_places_the_pairs_where_the_cases_say():
    """The control: if `tiny_world` ever moved a person, the cases below would test nothing."""
    w = P.tiny_world()
    here = world_q.place_of(w, ACTOR)
    assert here is not None
    assert world_q.place_of(w, BESIDE) == here
    for other in (ELSEWHERE, FAR):
        there = world_q.place_of(w, other)
        assert there is not None and there != here, (other, there, here)


def test_each_duel_row_carries_the_with_conjunct_on_subject():
    checked = 0
    for verb in DUEL_VERBS:
        cell = V.VERB_TABLE[verb].requires_typed
        assert cell is not None, verb
        stems = [(c.of, c.relation) for c in getattr(cell.requirement, "clauses", ())
                 if type(c).__name__ == "Relation"]
        assert ("subject", "with") in stems, (verb, stems)
        assert cell.known_person_operands() == (), verb   # no fan-out over known persons
        checked += 1
    assert checked == len(DUEL_VERBS) == 3


@pytest.mark.usefixtures("engine_available")
def test_a_duel_verb_across_rungs_is_refused_and_the_same_pair_co_located_executes():
    checked = 0
    for verb in DUEL_VERBS:
        for subject in (ELSEWHERE, FAR):
            evs = _fold(verb, subject)
            assert _refused(verb, evs), (verb, subject, [e.kind for e in evs])
            checked += 1
        evs = _fold(verb, BESIDE)
        assert not _refused(verb, evs), (verb, BESIDE, [e.kind for e in evs])
        checked += 1
    assert checked == 3 * len(DUEL_VERBS) == 9


@pytest.mark.usefixtures("engine_available")
def test_mutation_dropping_the_with_conjunct_lets_the_cross_rung_act_execute():
    """The conjunct is the cause: the same row without it executes exactly the act the shipped row
    refuses. If a different clause were refusing, this would stay refused and the test fails."""
    checked = 0
    for verb in DUEL_VERBS:
        assert _refused(verb, _fold(verb, ELSEWHERE)), verb
        with mock.patch.dict(V.VERB_TABLE, {verb: _without_with(verb)}):
            evs = _fold(verb, ELSEWHERE)
        assert not _refused(verb, evs), (verb, [e.kind for e in evs])
        checked += 1
    assert checked == len(DUEL_VERBS) == 3
