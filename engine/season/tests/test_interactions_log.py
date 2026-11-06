"""ED-IN-0335 -- the interaction audit log (`harness/interactions.py`) observes, and observing changes nothing.

Three controls (the module docstring says what each row holds):
  1. HASH-EQUAL: `World.content_hash()`, the log length, the draw ordinal and the act-id sequence after two
     seasons with the chooser watched equal the same run unwatched (seed 0 here; seeds 1-2 under `slow`).
  2. PLANTED FAILURE: `interactions.same_faction` inverted makes `_assert_finding` fail, so the finding below
     is one the log can be seen to get wrong.
  3. THE FINDING: at `build_realm(0)`, season 1, the Cardinal of Prudence (`p_npc_013`) is logged taking
     `fight` against the Senior Inquisitor (`p_npc_004`), same faction, stance 0.0, answering the question
     raised by the CR-81 acquaintance claim `c_acq_p_npc_013_p_npc_004`, and the act is in `--audit`'s set.
  Plus the re-read table IS the chooser's: every act the chooser returned matches a re-read candidate.
"""
from __future__ import annotations

import pytest

from ..harness import interactions as I
from .test_cr87_violence_contexts import revert_cr87

CARDINAL, INQUISITOR = "p_npc_013", "p_npc_004"


@pytest.fixture(scope="module")
def season_one():
    return I.run(0, 1)


def _assert_finding(rows) -> None:
    hits = [r for r in I.audit(rows)
            if r["actor"] == CARDINAL and r["target"] == INQUISITOR and r["verb"] == "fight"]
    assert hits, "the Cardinal's fight on the Inquisitor is not among the audited rows"
    r = hits[0]
    assert r["relation"]["same_faction"] is True
    assert r["relation"]["stance"] == 0.0
    assert r["question"]["source"] == "claim_landed"
    assert r["question"]["claim"]["id"] == f"c_acq_{CARDINAL}_{INQUISITOR}"
    assert r["question"]["claim"]["origin"].startswith("acquaintance")
    assert r["candidate"]["chosen"] and r["candidate"]["verb"] == "fight"


def test_the_log_names_the_cardinals_fight_on_the_inquisitor(monkeypatch):
    """v11 CR-87 MADE THE FINDING ITS FALSIFIER: with `fight`'s contexts the Cardinal forms no `fight` on the Inquisitor
    (`test_cr87_violence_contexts.py` asserts it gone on the shipped tree). The instrument's own claim -- that it names the
    case where the case occurs -- is read on the world it was found in, CR-87 at its revert (`revert_cr87`)."""
    revert_cr87(monkeypatch)
    _, _, rows = I.run(0, 1)
    _assert_finding(rows)


def test_the_re_read_table_is_the_choosers(season_one):
    _, _, rows = season_one
    delib = [r for r in rows if r["kind"] == "deliberation" and r["table_check"]]
    assert sum(r["table_check"]["returned_acts"] for r in delib) > 0
    assert sum(r["table_check"]["unmatched"] for r in delib) == 0
    acts = [r for r in rows if r["kind"] == "act"]
    assert acts and all(r["deliberation"] is not None for r in acts)


def test_the_logged_scores_carry_the_believed_odds_factor(monkeypatch):
    """The membership check cannot see a score: a reader that dropped `View.odds` would pass it. Planted: the reader's
    `score_terms` call made with no query (the game's own chooser is left alone) moves the logged scores of some
    deliberations (28 of 328 at seed 0, one season), so the shipped log is sensitive to the query it reads."""
    import types
    from ..decision import choose as CH
    shipped = [r for r in I.run(0, 1)[2] if r["kind"] == "deliberation" and r["candidates"]]
    real = CH.score_terms
    shim = types.SimpleNamespace(**{k: v for k, v in vars(CH).items() if not k.startswith("__")})
    shim.score_terms = lambda p, c, fx, memo, odds=None: real(p, c, fx, memo, None)
    monkeypatch.setattr(I, "CH", shim)
    dropped = [r for r in I.run(0, 1)[2] if r["kind"] == "deliberation" and r["candidates"]]
    assert len(shipped) == len(dropped) > 0
    moved = sum(1 for a, b in zip(shipped, dropped)
                if [c["score"] for c in a["candidates"]] != [c["score"] for c in b["candidates"]])
    assert moved >= 1, "a reader that dropped the believed-odds query logs the same scores: the log cannot see it"


def test_a_planted_wrong_relation_reading_is_seen(monkeypatch):
    revert_cr87(monkeypatch)            # v11 CR-87: the finding the plant must break exists only at the revert (above)
    real = I.same_faction
    monkeypatch.setattr(I, "same_faction", lambda w, a, t: not real(w, a, t))
    _, _, rows = I.run(0, 1)
    with pytest.raises(AssertionError):
        _assert_finding(rows)


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
