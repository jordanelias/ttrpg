"""ED-IN-0335 -- the interaction audit log (`harness/interactions.py`) observes, and observing changes nothing.

Three controls (the module docstring says what each row holds):
  1. HASH-EQUAL: `World.content_hash()`, the log length, the draw ordinal and the act-id sequence after two
     seasons with the chooser watched equal the same run unwatched (seed 0 here; seeds 1-2 under `slow`).
  2. PLANTED FAILURE: `interactions.same_faction` inverted makes `_assert_finding` fail, so the finding below
     is one the log can be seen to get wrong.
  3. THE FINDING: on the shipped season (`build_realm(0)`, season 1), the first audited row whose candidate was chosen
     and whose verb declares `contests:` carries six fields equal to the world's for that pair: same faction, stance,
     the question's source, its claim in the actor's ledger, the claim's origin, and the candidate being the act.
  Plus the re-read table IS the chooser's: every act the chooser returned matches a re-read candidate.
"""
from __future__ import annotations

import pytest

from ..data.verbs import VERB_TABLE
from ..harness import interactions as I
from ..queries import person_q, world_q


@pytest.fixture(scope="module")
def season_one():
    return I.run(0, 1)


def _selected(rows):
    """The first audited row of the season whose candidate was chosen and whose verb declares `contests:`."""
    return next((r for r in I.audit(rows)
                 if r["candidate"] and r["candidate"]["chosen"] and VERB_TABLE[r["verb"]].contests), None)


def _assert_finding(w, rows) -> None:
    r = _selected(rows)
    assert r is not None, "no audited row of the season is a chosen act of a verb that declares `contests:`"
    actor, target = r["actor"], r["target"]
    assert r["relation"]["same_faction"] == (world_q.faction_holding(w, actor) is not None
                                             and world_q.faction_holding(w, actor) == world_q.faction_holding(w, target)), \
        "same_faction: the logged reading is not the world's for this pair"
    assert r["relation"]["stance"] == person_q.stance_toward(w.persons[actor], target)
    assert r["question"]["source"] == "claim_landed"
    claim = r["question"]["claim"]
    assert claim["id"] in {c.id for c in w.persons[actor].ledger}, "the question's claim is not in the actor's ledger"
    assert claim["origin"].startswith("acquaintance") == (claim["id"] in w._acquaintances)
    assert r["candidate"]["chosen"] and r["candidate"]["verb"] == r["verb"]


def test_the_log_names_a_contested_act_between_friends_on_the_shipped_season(season_one):
    """The finding is read off the shipped season, no reverted fixture: the first audited row (a hostile act between
    same-faction persons, stance >= 0) whose candidate was chosen and whose verb declares `contests:` carries the six
    fields the world holds for that pair."""
    w, _, rows = season_one
    checked = len(I.audit(rows))
    assert checked >= 1, "the shipped season has no audited row"
    _assert_finding(w, rows)


def test_the_re_read_table_is_the_choosers(season_one):
    _, _, rows = season_one
    delib = [r for r in rows if r["kind"] == "deliberation" and r["table_check"]]
    assert sum(r["table_check"]["returned_acts"] for r in delib) > 0
    assert sum(r["table_check"]["unmatched"] for r in delib) == 0
    acts = [r for r in rows if r["kind"] == "act"]
    assert acts and all(r["deliberation"] is not None for r in acts)


def test_the_logged_scores_are_the_choosers_own_and_carry_the_believed_odds_factor(monkeypatch):
    """B09.13: the log scores nothing; its candidate table is what `make_chooser(watch=...)` handed it. The membership
    check cannot see a score, so this reads them: a transparent spy on the game's own `score_terms` records every tuple the
    chooser scored for each (actor, verb, subject), and every logged candidate's terms must be one of them. The spy also
    records the same candidate read WITHOUT the View's believed-odds query; some logged terms equal the first and not the
    second (28 of 328 deliberations moved at seed 0, one season, under the old reader's plant), so the log is observed to
    carry the factor the chooser read, not a reading that dropped it."""
    from ..decision import choose as CH
    real = CH.score_terms
    scored: dict = {}
    odds_free: dict = {}

    def spy(p, c, fx, memo, odds=None):
        t = real(p, c, fx, memo, odds)
        scored.setdefault((p.id, c.verb, c.subject), set()).add(t)
        odds_free.setdefault((p.id, c.verb, c.subject), set()).add(real(p, c, fx, memo, None))
        return t
    monkeypatch.setattr(CH, "score_terms", spy)
    rows = [r for r in I.run(0, 1)[2] if r["kind"] == "deliberation" and r["candidates"]]
    checked = carried = 0
    for r in rows:
        for c in r["candidates"]:
            key = (r["actor"], c["verb"], c["subject"])
            t = (c["pursuit"], c["stance"], c["fit"])
            assert t in scored[key], f"a logged candidate's terms are not any the chooser scored: {key} {t}"
            checked += 1
            carried += t not in odds_free[key]
    assert checked >= 1000, f"the season logged only {checked} candidates"
    assert carried >= 1, "no logged term differs from its odds-free reading: the log could not show it dropped the query"


def _hash_arm(seed: int) -> None:
    off, _, _ = I.run(seed, 2, observe=False)
    on, _, rows = I.run(seed, 2)
    assert rows
    assert on.content_hash() == off.content_hash()
    assert len(on.log) == len(off.log)
    assert on.draw == off.draw
    assert [a.id for a in on.acts] == [a.id for a in off.acts]


def test_observing_changes_nothing_seed_0():
    _hash_arm(0)


@pytest.mark.slow
@pytest.mark.parametrize("seed", [1, 2])
def test_observing_changes_nothing_other_seeds(seed):
    _hash_arm(seed)
