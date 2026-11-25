"""B21.72 (`06_FA_playable_scenario`) -- A GOVERNANCE SCENARIO THAT PLAYS: `situation`, `digest`, `offered`, `play`
(`harness/governance_spine.py`), on the governance test world. Every test reads the world: the control compares two worlds'
`content_hash`, the digest tests read a built log, the refusal test reads the fold's Event, and the restoration test reads
`SUCCESSIONS` while a run is under way and after it. Nothing here runs a realm.

THE CONTROL IS THE ONE THAT MATTERS: `pick=None` is the shipped chooser for everyone, so `play` must leave the world exactly
where `populated.run` leaves the same world; if it does not, the harness moved the game.
"""
from __future__ import annotations

import pytest

from ..data.matrix import WriteClass
from ..data.rosters import SUCCESSIONS
from ..gaps import Forbidden
from ..harness import governance_spine as G
from ..harness import populated
from ..harness.probes import apparatus_receipt
from ..loop.driver import SeasonDriver, mint_token
from ..state.carriers import Act, Event
from ..state.ids import ROOT
from ._seat_at_success import seat_at_success  # noqa: F401  (the fixture; its reason is in its module)


def _quiet(_line: str) -> None:
    pass


def _situated(name: str, seed: int = 0):
    w = G.build(seed)
    player = G.default_player(w)
    with G._successions_set(G.successions_for(w, name, player)):
        G.situation(w, name, player)
    return w, player


def test_pick_none_reproduces_populated_run_hash():
    """THE CONTROL (B21.72's falsifier): for each situation, the world `play(pick=None)` returns after one season has the `content_hash` of the same
    world, made by the same `situation`, run through `populated.run`. The reference is not the start state: the situation moved the build and the
    season moved the situation (both asserted), so equal hashes are not two untouched worlds."""
    checked = 0
    for name in G.SITUATIONS:
        ref, player = _situated(name)
        built, opened = G.build(0).content_hash(), ref.content_hash()
        with G._successions_set(G.successions_for(ref, name, player)):
            populated.run(1, 0, w=ref)
        got = G.play(0, 1, name, pick=None, out=_quiet)["world"]
        assert opened != built and ref.content_hash() != opened, f"{name}: the situation or the season moved nothing"
        assert got.content_hash() == ref.content_hash(), f"{name}: play(pick=None) is not populated.run's run"
        checked += 1
    assert checked == len(G.SITUATIONS) == 3


def test_digest_on_an_empty_log_prints_nothing():
    """FALSIFIER: a world with no governance Event prints nothing -- a planted empty log, and a log holding only an Event of a kind no
    digested verb emits (an utterance), which a digest reading every Event would print."""
    w = G.build(0)
    assert len(w.log) == 0 and G.digest(w, 0) == []
    w.log.append(Event(id="plant_utter", kind="proposition.uttered", changes=[], causes=[ROOT], emitted_at=0))
    assert len(w.log) == 1 and G.digest(w, 0) == []


def test_digest_prints_one_line_for_a_planted_tenure_opened():
    """FALSIFIER: a planted `tenure.opened` naming a seat-hold prints exactly one line, naming the holder and the seat; `since` past it prints none."""
    w = G.build(0)
    edge = next(t for t in w.tenures if t.kind == "hold" and t.object in w.offices)
    w.log.append(Event(id="plant_opened", kind="tenure.opened", causes=[ROOT], emitted_at=0,
                       changes=[apparatus_receipt(w, edge.id, "set", "apparatus", "until")]))
    lines = G.digest(w, 0)
    assert len(lines) == 1, lines
    assert edge.subject in lines[0] and edge.object in lines[0] and "opened" in lines[0], lines
    assert G.digest(w, 1) == []


def test_a_refused_opening_act_stops_the_run_naming_the_event():
    """FALSIFIER: a situation the fold refuses raises with the refusing Event's kind, never a silent fallback. The Sovereign's writ is addressed to the
    Count, whom his seat does not command (the Duke stands between), so the fold refuses the `issue`; the refusal names `issue.refused`, the writ is not
    minted, and the refused act's Event is not logged. CONTROL: the same writ to the Duke, whom the Sovereign's seat does command, is admitted."""
    w = G.build(0)
    count = "lp_province_a"
    with pytest.raises(Forbidden) as e:
        G.situation(w, "order", count)
    assert "issue.refused" in str(e.value) and "scn:order:writ" in str(e.value), str(e.value)
    assert not any(r.startswith("rec:scn:order:writ") for r in w.records), "a refused writ was minted"
    assert not any(ev.kind == "issue.refused" for ev in w.log), "the refusing Event was logged as the scenario's own"
    ok = G.build(0)
    assert [a.verb for a in G.situation(ok, "order", G.default_player(ok))] == ["utter", "issue"]


def test_successions_is_restored_after_play():
    """`SUCCESSIONS` is the scenario's row for the run and the loader's after it, a run that raises included. DURING the run the throne key is read
    in place (the gate reads the one dict, G-28); AFTER it the dict is what it was, key for key, and the same object."""
    before, identity = dict(SUCCESSIONS), id(SUCCESSIONS)
    w = G.build(0)
    (throne, titles), = G.successions_for(w, "succession", G.default_player(w)).items()
    assert throne not in SUCCESSIONS and len(titles) == 2
    seen = []
    G.play(0, 1, "succession", pick=None, out=lambda line: seen.append(SUCCESSIONS.get(throne)))
    assert seen and all(row == titles for row in seen), "the run did not read the scenario's row in place"
    assert SUCCESSIONS == before and id(SUCCESSIONS) == identity
    # a pick that is no selection from the candidates stops the run inside its first season: the dict is restored all the same
    with pytest.raises(Forbidden):
        G.play(0, 1, "succession", pick=(10 ** 6,), out=_quiet)
    assert SUCCESSIONS == before and id(SUCCESSIONS) == identity and throne not in SUCCESSIONS


def test_a_two_title_succession_digest_names_each_claimant(seat_at_success):     # the claim's write, not its draw
    """Two listed titles (A-19) held by two persons: each makes his claim on the vacated throne in one fold. The first valid claim wins, the second is
    refused, and the digest names BOTH claimants, each with what his claim reached."""
    w = G.build(0)
    player = G.default_player(w)
    (throne, titles), = G.successions_for(w, "succession", player).items()
    with G._successions_set({throne: titles}):
        G.situation(w, "succession", player)
        claimants = sorted(G._holder_of(w, t) for t in titles)
        assert len(claimants) == 2 and player in claimants
        start = len(w.log)
        d = SeasonDriver(w)
        events = d.resolve(mint_token(w, WriteClass.ACTS),
                           [Act(id=f"claim_{c}", actor=c, verb="succeed", payload={"subject": throne}) for c in claimants],
                           contest_max_depth=w.fixtures.get("contest_max_depth"))
        for e in events:
            w.log.append(e)
        lines = G.digest(w, start)
    assert len(lines) == 2, lines
    for c in claimants:
        assert sum(c in line for line in lines) == 1, (c, lines)
    kinds = sorted(line.split()[1].rstrip(":") for line in lines)
    assert kinds == ["succession.claimed", "succession.refused"], kinds
