"""B21.72 (`06_FA_playable_scenario`) -- A GOVERNANCE SCENARIO THAT PLAYS: `situation`, `digest`, `offered`, `play`
(`harness/governance_spine.py`), on the governance test world. Every test reads the world: the control compares two worlds'
`content_hash`, the digest tests read a built log, the refusal test reads the fold's Event, and the restoration test reads
`SUCCESSIONS` while a run is under way and after it. Nothing here runs a realm.

THE CONTROL IS THE ONE THAT MATTERS: `pick=None` is the shipped chooser for everyone, so `play` must leave the world exactly
where `populated.run` leaves the same world; if it does not, the harness moved the game.
"""
from __future__ import annotations

import pytest
from engine.dice_engine.dice_engine import DEGREE_LABEL

from ..boot.realm import build_realm
from ..data.matrix import WriteClass
from ..data.rosters import SUCCESSIONS
from ..gaps import Forbidden
from ..harness import governance_spine as G
from ..harness import populated
from ..queries import world_q
from ..harness.probes import apparatus_receipt
from ..loop.driver import SeasonDriver, mint_token
from ..state.carriers import Act, Event
from ..state.ids import ROOT
from ._seat_at_success import seat_at_success  # noqa: F401  (the fixture; its reason is in its module)


def _quiet(_line: str) -> None:
    pass
















# ---------------------------------------------------------------------------------------------------
# B21.74 (`06_FA_shortest_loop_B`): `loop_closed`, `recall`, `play(world="realm")`.
# ---------------------------------------------------------------------------------------------------

WRIT = "rec:scn:order:writ"


def test_loop_closed_reads_one_issue_as_ordered_1_and_four_zeros():
    """The `order` opening is one `issue` through the fold (and an `utter` that is no link): `ordered` 1, the other four links 0, one person, not closed.
    FALSIFIER: the same log read from past its end reads zero everywhere, so the count is of what the slice holds."""
    w = G.build(0)
    G.situation(w, "order", G.default_player(w))
    r = G.loop_closed(w, 0)
    assert [r[k] for k in G.LOOP_LINKS] == [1, 0, 0, 0, 0] and r["persons"] == 1 and r["closed"] is False, r
    past = G.loop_closed(w, len(w.log))
    assert [past[k] for k in (*G.LOOP_LINKS, "persons")] == [0] * 6 and past["closed"] is False


def test_a_non_addressee_comply_is_not_answered():
    """A `compliance.given` by the Count, to whom the writ is not addressed, is not an answer; the same Event by the Duke, to whom it is, is. Both are
    planted on the real writ the fold made (a refused act makes no such Event, so the plant is how a non-addressee's answer reaches the log)."""
    w = G.build(0)
    duke = G.default_player(w)
    G.situation(w, "order", duke)
    assert WRIT in w.records

    def answer(actor):
        act = Act(id=f"plant:comply:{actor}", actor=actor, verb="comply", payload={"subject": WRIT})
        w.acts.append(act)
        w.log.append(Event(id=f"plant_ev:{actor}", kind="compliance.given", changes=[], causes=[act.id], emitted_at=0))
    answer("lp_province_a")
    assert G.loop_closed(w, 0)["answered"] == 0
    answer(duke)
    assert G.loop_closed(w, 0)["answered"] == 1


def test_a_defied_writ_met_by_a_revoke_and_a_conferral_closes_the_loop():
    """The five links on the spine's own acts through the fold, seeds 0 to 11: the Sovereign writes to the Duke, the Duke defies, the Sovereign revokes his
    seat (a resisted draw), and confers it. At every seed `responded` is 1 and reports the band the revoke reached; `vacated` follows the band (a Failure
    leaves the Duke seated) and `filled` follows `vacated`; and at some seed the loop closes. CONTROL: the Duke complies instead and the same revoke is no
    response. Two persons act in a closing run: that is the reader's, not a realm's (`persons >= 3` is the realm's exit)."""
    closed = checked = 0
    for seed in range(12):
        for answer, responds in (("evade / defy", True), ("comply", False)):
            w = G.build(seed)
            duke = G.default_player(w)
            G.situation(w, "order", duke)
            d = SeasonDriver(w)
            for act in (Act(id="t:answer", actor=duke, verb=answer, payload={"subject": WRIT}),
                        Act(id="t:revoke", actor="lp_realm", verb="revoke", via="lo_realm", payload={"subject": "lo_duchy_a"}),
                        Act(id="t:confer", actor="lp_realm", verb="confer", via="lo_realm", payload={"subject": "lo_duchy_a", "to": "lp_province_a"})):
                G._open(w, d, act)
            r = G.loop_closed(w, 0)
            band = next(e.degree for e in w.log if "t:revoke" in e.causes)
            assert r["ordered"] == 1 and r["answered"] == 1, (seed, r)
            if responds:
                assert r["responded"] == 1 and r["responded_bands"] == {band: 1}, (seed, r)
                assert r["vacated"] == (0 if band == "Failure" else 1) and r["filled"] <= r["vacated"], (seed, r)
                assert r["closed"] == (r["vacated"] > 0 and r["filled"] > 0), (seed, r)
                closed += r["closed"]
            else:
                assert r["responded"] == 0 and r["closed"] is False, (seed, r)
            checked += 1
    assert checked == 24 and closed >= 1, (checked, closed)


def test_the_recall_opening_writes_a_writ_at_all_four_bands_and_the_addressee_is_offered_his_answers():
    """B21.56's D3 arm on `recall`, dice seeds 0 to 39 (the opening only, no season): the Sovereign's `issue` reaches all four bands, and at every band, Failure
    included, the man it is addressed to is offered the writ to answer (`world_q.writs_addressed`, A-21). NOT READ HERE: that the answer's composed obstacle carries
    `force` (owed edit 10 of the source, not built: `comply`, `evade / defy` and `construe` do not read it)."""
    bands, checked = set(), 0
    for seed in range(40):
        w = G.build(seed)
        duke = G.default_player(w)
        G.situation(w, "recall", duke)
        band = next(e.degree for e in w.log if e.kind in G._MADE["issue"])
        assert WRIT in world_q.writs_addressed(w, w.persons[duke]), (seed, band)
        bands.add(band)
        checked += 1
    assert checked >= 40 and bands == set(DEGREE_LABEL.values()), bands


def test_world_realm_reproduces_populated_run_hash():
    """THE CONTROL (B21.74's falsifier): `play(world="realm")` leaves the built realm where `populated.run` leaves the same seed after the same season: one
    season, seed 0. The reference moved off its build (asserted), so equal hashes are not two untouched worlds. STATED REASON FOR ITS ~10 s: the control is a
    realm season on each of two paths, ~4.5 s a season; it cannot be read on a smaller world, and zero seasons would compare two builds. The realm refuses a
    situation, a player or a pick (the read is the world as built)."""
    ref = build_realm(0)
    built = ref.content_hash()
    populated.run(1, 0, w=ref)
    got = G.play(0, 1, out=_quiet, world="realm")
    assert ref.content_hash() != built
    assert got["world"].content_hash() == ref.content_hash() and got["loop"]["closed"] is False
    for bad in ({"situation": "order"}, {"player": "lp_duchy_a"}, {"pick": ()}):
        with pytest.raises(Forbidden):
            G.play(0, 1, out=_quiet, world="realm", **bad)
