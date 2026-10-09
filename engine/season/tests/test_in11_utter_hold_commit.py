"""v9 IN-11 (#453 §10.4 step 2) -- `utter` mints the utterer's hold, so `commit` executes; with
R-3 (b), `repudiate` is cut and `release` earns `commitment.ended` on a closed `commit`.

What each block proves, and the control that stops it passing vacuously:

  1. THE HOOK, THROUGH THE REAL FOLD. An `utter` opens a live `hold` owned by the utterer on the new
     Proposition, which puts the Proposition in his `reach` (limb 2) -- the one route a placeless
     Proposition has into a question. A `commit` on it then executes (`commitment.made`). Control:
     a Proposition the person did NOT utter is outside his `reach`, so the route is the hold and
     not something else.
  2. R-3 (b): A `release` that closes a `commit` earns `commitment.ended` beside `tenure.closed`.
     Control: a `release` that closes only the maker's `hold` earns `tenure.closed` alone.
  3. COMPUTED PLAY: one seeded `build_realm(0)` season through the real chooser executes `commit`
     at least once, and every Proposition an executed `commit` names is one its committer holds
     (the utter -> hold -> question -> commit chain, not a hand-built act). Before IN-11 the same
     season attempted `commit` and refused every attempt (`aperture 1 0`: 35 of 35).
  4. THE CUT IS COMPLETE AND THE LOADER POLICES IT: `repudiate` is not a verb, and a planted
     `repudiate` cell in the alignment table or in `affiliation_engagement`'s shared column is
     refused at load (`data/verbs.py::_check_sparse_table`, the one owner of that check). Control:
     the shipped tables load.
"""
import collections

import pytest

from engine.season.data import affiliations as AF
from engine.season.data import verbs as VERBS
from engine.season.data.matrix import WriteClass
from engine.season.data.rosters import table, table_meta
from engine.season.gaps import Forbidden
from engine.season.harness import probes as P
from engine.season.harness.populated import build_realm
from engine.season.loop.driver import SeasonDriver, mint_token, resolvable_verbs
from engine.season.queries.world_q import reach
from engine.season.state.carriers import Act


def _fold(w, d, act):
    return [e.kind for e in d.resolve(mint_token(w, WriteClass.ACTS), [act],
                                      contest_max_depth=w.fixtures.get("contest_max_depth"))]


def _live(w, pid, obj):
    return sorted(t.kind for t in w.persons[pid].tenures if t.object == obj and t.live)


# ======================================================================================
# 1, 2 -- THE HOOK AND THE CLOSER, THROUGH THE REAL FOLD
# ======================================================================================

def test_in11_utter_opens_the_utterers_hold_so_commit_executes_and_release_ends_it():
    w = P.tiny_world()
    d = SeasonDriver(w)
    assert _fold(w, d, Act(id="in11_u", actor="p_low", verb="utter")) == ["proposition.uttered"]
    pid = "prop:in11_u"
    assert pid in w.propositions
    assert _live(w, "p_low", pid) == ["hold"], _live(w, "p_low", pid)
    assert pid in reach(w, w.persons["p_low"]), "the maker's hold did not put the Proposition in reach"
    # CONTROL: somebody else's utterance is not in p_low's reach -- the route is the hold.
    assert _fold(w, d, Act(id="in11_m", actor="p_mid", verb="utter")) == ["proposition.uttered"]
    assert "prop:in11_m" not in reach(w, w.persons["p_low"])
    assert "prop:in11_m" in reach(w, w.persons["p_mid"])

    assert _fold(w, d, Act(id="in11_c", actor="p_low", verb="commit",
                           payload={"subject": pid})) == ["commitment.made"]
    assert _live(w, "p_low", pid) == ["commit", "hold"], _live(w, "p_low", pid)

    # R-3 (b): the release closes both of his edges on it and witnesses the vow-break.
    assert _fold(w, d, Act(id="in11_r", actor="p_low", verb="release",
                           payload={"subject": pid})) == ["tenure.closed", "commitment.ended"]
    assert _live(w, "p_low", pid) == []
    # CONTROL: a release that closes no `commit` (p_mid's bare maker's hold) earns no vow-break.
    assert _fold(w, d, Act(id="in11_r2", actor="p_mid", verb="release",
                           payload={"subject": "prop:in11_m"})) == ["tenure.closed"]
    assert _live(w, "p_mid", "prop:in11_m") == []


# ======================================================================================
# 3 -- COMPUTED PLAY
# ======================================================================================

def test_in11_commit_executes_in_a_computed_realm_season_on_a_proposition_its_committer_holds():
    from engine.season.decision import make_chooser
    from engine.season.state.ids import H, draw_factory
    w = build_realm(seed=0)
    d = SeasonDriver(w)
    mint = lambda pid, verb, subj: H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
    ch = make_chooser(w.fixtures, mint, verbs=resolvable_verbs(),
                      draw=draw_factory(w.world_seed, lambda: w.tick))
    d.season(ch, question=None, subsistence=P.SUBSIST,
             contest_max_depth=w.fixtures.get("contest_max_depth"))
    kinds = collections.Counter(e.kind for e in w.log)
    assert kinds["commitment.made"] >= 1, (
        f"`commit` executed {kinds['commitment.made']} times in a computed realm season "
        f"(refused {kinds['commitment.refused']}) -- IN-11 is not built")
    # The acts behind each `commitment.made`: computed (the chooser's), on a Proposition uttered by
    # an act this season, which the committer holds -- the utter -> hold -> question -> commit chain.
    uttered = {f"prop:{a.id}" for a in w.acts if a.verb == "utter"}
    checked = 0
    for e in (e for e in w.log if e.kind == "commitment.made"):
        a = w.acts.get(e.causes[0])
        assert a is not None and a.verb == "commit", (e.causes, a)
        prop = (a.payload or {}).get("subject")
        assert prop in uttered, f"{a.actor} committed to {prop!r}, which no act uttered this season"
        assert any(h.kind == "hold" and h.object == prop for h in w.persons[a.actor].tenures), (
            f"{a.actor} committed to {prop} without holding it -- not the utter -> hold chain")
        checked += 1
    assert checked == kinds["commitment.made"] >= 1


# ======================================================================================
# 4 -- THE CUT, AND THE LOADER THAT REFUSES A SURVIVING CELL
# ======================================================================================

def test_in11_repudiate_is_cut_and_a_surviving_cell_is_refused_at_load():
    assert "repudiate" not in VERBS.VERB_TABLE
    assert "commitment.ended" in VERBS.VERB_TABLE["release"].emits
    assert VERBS.KIND_VERB.get("commitment.ended") == "release"
    # CONTROL: the shipped tables load as they stand.
    cells = table("alignment")
    uncelled = table_meta("alignment").get("uncelled") or {}
    VERBS._load_alignment(cells, uncelled)
    eng = table("affiliation_engagement")
    AF._load_engagement(eng)
    assert not any("repudiate" in row for row in cells.values())
    assert not any("repudiate" in row for row in eng.values())

    axis = next(iter(cells))
    planted = {ax: dict(row) for ax, row in cells.items()}
    planted[axis]["repudiate"] = 0.5
    with pytest.raises(Forbidden, match="repudiate"):
        VERBS._load_alignment(planted, uncelled)
    shared = table_meta("affiliation_engagement").get("shared_column")
    planted_eng = {col: dict(row) for col, row in eng.items()}
    planted_eng[shared]["repudiate"] = -0.6
    with pytest.raises(Forbidden, match="repudiate"):
        AF._load_engagement(planted_eng)
