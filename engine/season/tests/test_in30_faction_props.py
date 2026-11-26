"""B21b.05 (IN-30, with SE-05, FA-02 and §1a-(c)): ONE OWNER OF WHAT A FACTION IS, AND A CREED A PERSON FOUNDS.

`queries/world_q.py::faction_props` is the one owner of "is this a faction": the roster's faction Propositions
(`data/rosters.py::FACTION_BY_PROP`) and every Proposition of the creed shape `rosters.yaml: factions.creed` names
(mood and predicate). No threshold, counter or stored entity; membership is the existing `commit`.

Both tests drive the shipped fold (`SeasonDriver.resolve`) on the built realm, seed 0:
  * THE FALSIFIER: a land-holding seat-holder `release`s his faction `commit`, `utter`s a creed and `commit`s to
    it -> `faction_holding` names the creed, his territory is not `uncontrolled`, and a planted world with every
    SETTLED realm territory (`09_WR_world_motion` edit 3, B12a.09's selector) under the creed's members reports
    `peninsular_sovereignty`, his `commit` its act.
  * THE CONTROL: the same three acts with a non-creed OUGHT -> not a faction (the reading before B21b.05), his
    territory uncontrolled.
The mutation (drop the predicate test, so every uttered OUGHT is a faction) is run once at the build and recorded in
its commit, not kept here (CLAUDE.md §0.1 pt 3).
"""
from __future__ import annotations

from engine.season.boot.realm import build_realm
from engine.season.data import rosters as R
from engine.season.data.matrix import WriteClass
from engine.season.loop.driver import SeasonDriver, mint_token
from engine.season.queries import world_q as Q
from engine.season.state.carriers import Act, Tenure


def _fold(w, d, *acts):
    """Fold hand-built acts through the shipped `SeasonDriver.resolve` and log what it emits, as `season()` does."""
    out = d.resolve(mint_token(w, WriteClass.ACTS), list(acts), contest_max_depth=w.fixtures.get("contest_max_depth"))
    w.log.extend(out)
    return [e.kind for e in out]


def _realm_root(w):
    (root,) = [r for r in w.rungs if w.rungs[r].kind == "realm"]
    return root


def _settled_territories(w):
    """The realm's territories with a `settlement` rung beneath them (what `endings.peninsular_sovereignty`'s
    `settled: true` selects), read off the containment walk, not off the Query under test."""
    root = _realm_root(w)
    return sorted(r for r in Q.descendants(w, root) if r in w.rungs and w.rungs[r].kind == "territory"
                  and any(x in w.rungs and w.rungs[x].kind == "settlement" for x in Q.descendants(w, r)))


def _land_holding_seat_holder(w):
    """The first person, id order, holding a live `hold` on a settled realm territory AND on a seat, and committed to
    exactly one rostered faction (read off his own edges, not off `faction_holding`)."""
    settled = set(_settled_territories(w))
    for pid, p in sorted(w.persons.items()):
        land = sorted(t.object for t in p.tenures if t.kind == "hold" and t.live and t.object in settled)
        seat = any(t.kind == "hold" and t.live and t.object in w.offices for t in p.tenures)
        facs = [t.object for t in p.tenures if t.kind == "commit" and t.live and t.object in R.FACTION_BY_PROP]
        if land and seat and len(facs) == 1:
            return pid, facs[0], land[0]
    raise AssertionError("fixture: no land-holding seat-holder in the built realm")


def _leave_utter_commit(w, d, founder, faction, predicate, tag):
    """His three own acts: `release` his faction membership, `utter` an OUGHT about himself with `predicate`, `commit`
    to it. Returns the uttered Proposition's id."""
    kinds = _fold(w, d, Act(id=f"{tag}_leave", actor=founder, verb="release", payload={"subject": faction}))
    assert "commitment.ended" in kinds and not any(
        t.kind == "commit" and t.live and t.object == faction for t in w.persons[founder].tenures), kinds
    kinds = _fold(w, d, Act(id=f"{tag}_utter", actor=founder, verb="utter",
                            payload={"mood": R.FACTION_CREED["mood"], "subject": founder, "predicate": predicate, "value": founder}))
    assert kinds == ["proposition.uttered"], kinds
    prop = f"prop:{tag}_utter"
    kinds = _fold(w, d, Act(id=f"{tag}_commit", actor=founder, verb="commit", payload={"subject": prop}))
    assert kinds == ["commitment.made"], kinds
    return prop


def test_a_released_member_who_utters_a_creed_and_commits_founds_a_faction():
    w = build_realm(0)
    d = SeasonDriver(w)
    founder, faction, land = _land_holding_seat_holder(w)
    root = _realm_root(w)
    assert Q.faction_holding(w, founder) == faction and land not in Q.uncontrolled(w, root), "fixture"
    assert Q.endings_reached(w) == [], "fixture: the built realm reaches no ending"

    creed = _leave_utter_commit(w, d, founder, faction, R.FACTION_CREED["predicate"], "in30")
    assert creed not in R.FACTION_BY_PROP, "fixture: the creed is no roster member"
    assert creed in Q.faction_props(w), "an uttered creed Proposition is not a faction"
    assert Q.faction_holding(w, founder) == creed, "his one live commit is to the creed and it does not name it"
    assert Q.holder_faction_of(w, land) == creed
    assert land not in Q.uncontrolled(w, root), "his territory reads uncontrolled under an emerged faction"
    assert Q.members(w, creed) == [founder]

    # THE PLANTED WORLD: every settled realm territory under the creed's members. Each other holder's rostered
    # memberships are closed and a creed `commit` planted (no act); the founder's own `commit` is the one act.
    for r in _settled_territories(w):
        t = Q.governing_hold(w, r)
        assert t is not None, f"fixture: settled territory {r} is unheld at build"
        if t.subject == founder:
            continue
        for c in w.persons[t.subject].tenures:
            if c.kind == "commit" and c.live and c.object in R.FACTION_BY_PROP:
                c.until = w.tick
        if not any(c.kind == "commit" and c.live and c.object == creed for c in w.persons[t.subject].tenures):
            w.add_tenure(Tenure(f"t_in30_{t.subject}_creed", t.subject, creed, "commit", 0))
    got = {r.ending: r for r in Q.endings_reached(w)}
    assert "peninsular_sovereignty" in got, got
    ps = got["peninsular_sovereignty"]
    assert ps.victory is True and ps.acts == ("in30_commit",), ps
    assert {t.object for t in Q._ending_edges(w, R.ENDINGS["peninsular_sovereignty"]) if t.kind == "hold"} \
        == set(_settled_territories(w))


def test_a_non_creed_ought_is_not_a_faction():
    w = build_realm(0)
    d = SeasonDriver(w)
    founder, faction, land = _land_holding_seat_holder(w)
    cause = _leave_utter_commit(w, d, founder, faction, "the strait stays open", "in30c")
    assert w.propositions[cause].mood == R.FACTION_CREED["mood"], "control: the same mood, only the predicate differs"
    assert cause not in Q.faction_props(w)
    assert Q.faction_props(w) == frozenset(R.FACTION_BY_PROP), "a non-creed OUGHT changed what a faction is"
    assert Q.faction_holding(w, founder) is None
    assert land in Q.uncontrolled(w, _realm_root(w)), "the control's territory is held under a faction"
