"""B10.71 -- a goal's LAST stage can open a MANDATORY question, and the question decides nothing.

THE BUILD: `goals.yaml`'s `goal_stages` row carries `opens: mandatory | ordinary` (default `ordinary`); `world_q.questions_for`
marks the `need` question of an ambition whose row says `mandatory` and whose person stands on the row's LAST stage
(`Question.mandatory`) and sorts the marked question first, ahead of `attention_key`. It forms no act: which act he takes
is still the chooser's draw. No stage row is authored in `goals.yaml` (B10.73 authors the first), so the rows here are
planted through the one seam the B2/B3 tests use (`goals.rows_replaced(goals.parse(doc))`).

  (a) THE LAST STAGE OPENS IT, AND IT DECIDES NOTHING: the planted holder has passed the first stage and not the last; his
      `need` question sorts first and is `mandatory`; the same world with `opens: ordinary` (the control) sorts it second and
      unmarked; and the acts he takes across seeds are not one set of verbs. PLANTED FAILURE: `mandatory` never set reddens
      the first assertion; a mark that fixed his act would collapse the last.
  (b) THE LOADER REFUSES AN `opens` VALUE OUTSIDE THE TWO, naming the row.
"""
from __future__ import annotations

import copy

import pytest

from ..data import goals
from ..decision import make_chooser
from ..gaps import Forbidden
from ..harness.probes import tiny_world
from ..loop.driver import SeasonDriver, resolvable_verbs
from ..queries import world_q
from ..state.carriers import Claim, Proposition, Tenure
from ..state.ids import H, draw_factory

SEAT = "off_king"
THRONE = "g_throne"
FIRST = {"form": "existence", "of": "subject", "kind": "Person"}
LAST = {"form": "relation", "of": "subject", "relation": "held_by"}


def _doc(opens=None) -> dict:
    stages = [{"id": sid, "term": term, "predicate": copy.deepcopy(cell), "pursuits": {"honour": 1}}
              for sid, term, cell in (("s1", "short", FIRST), ("s2", "long", LAST))]
    row = {"id": "gs_throne", "for": [THRONE], "stages": stages}
    if opens is not None:
        row["opens"] = opens
    return {"goals": [{"id": THRONE, "org": {"faction": "Valorsmark"}, "text": f"{THRONE}, as a predicate",
                       "object": {"kind": "seat_holders", "seats": [SEAT]}, "pursuits": {"stability": 1},
                       "source": "test_staged_goals", "stance": 1}],
            "goal_stages": [row]}


def _world(seed: int):
    """`p_high` is committed to the throne goal, which names whoever holds `off_king` (`p_king`); his own ledger holds the
    first stage's claim and not the last's, so the last stage is the one he stands on. A claim about the king is also
    landed on him, so the ordinary order puts that claim question ahead of his `need` question."""
    w = tiny_world()
    w.world_seed = seed
    w.propositions[THRONE] = Proposition(THRONE, "OUGHT", "subj_" + THRONE, f"{THRONE} ought", True, 0)
    w.add_tenure(Tenure("t_king_seat", "p_king", SEAT, "hold", 0))
    w.add_tenure(Tenure("t_commit", "p_high", THRONE, "commit", 0))
    w.persons["p_high"].ledger = [Claim("c_first", "p_high", "p_king", "exists:Person", True, 0, "firsthand", 100, "own")]
    return w


def _slate(opens):
    w = _world(0)
    with goals.rows_replaced(goals.parse(_doc(opens))):
        return world_q.questions_for(w, w.persons["p_high"])


def _first_acts(seed: int) -> frozenset:
    """The verbs `p_high` attempts in one season of the planted world, the chooser drawing under `seed`."""
    w = _world(seed)
    mint = lambda pid, verb, subj: H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
    ch = make_chooser(w.fixtures, mint, verbs=resolvable_verbs(), draw=draw_factory(w.world_seed, lambda: w.tick))
    with goals.rows_replaced(goals.parse(_doc("mandatory"))):
        SeasonDriver(w).season(ch, None, contest_max_depth=w.fixtures.get("contest_max_depth"))
    return frozenset(a.verb for a in w.acts if a.actor == "p_high")


def test_the_last_stage_opens_a_mandatory_question_and_decides_nothing():
    ordinary = _slate("ordinary")
    assert [q.source for q in ordinary] == ["claim_landed", "need"] and not any(q.mandatory for q in ordinary), \
        "the control: with `opens: ordinary` the claim question sorts first and nothing is marked"
    assert [q.source for q in _slate(None)] == ["claim_landed", "need"], "and `ordinary` is the default"
    marked = _slate("mandatory")
    assert [q.source for q in marked] == ["need", "claim_landed"], "the last stage's question sorts first"
    assert [q.mandatory for q in marked] == [True, False], "and only it is marked"
    acts = {_first_acts(seed) for seed in range(4)}
    assert len(acts) > 1, f"the mark fixed his act: the same verbs at every seed, {sorted(next(iter(acts)))}"


def test_an_opens_value_outside_the_two_is_refused():
    with pytest.raises(Forbidden) as e:
        goals.parse(_doc("compulsory"))
    assert "gs_throne" in str(e.value) and "'compulsory'" in str(e.value), "the refusal names the row and the value"
