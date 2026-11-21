"""`14_VERBS_PHYSICAL_A` (custody and force) -- the gates of the audit's §1.7, §2.7, §3.7 and §4.7, one function each.
This file holds A4's (B14.27); A3's (B15) and A1/A2's (B29) are added by their items.

A4, THE REAL CHOOSER. `test_b11a_duel_reach.py` drives the chain through formed Candidates and hand-built acts and
reverts the whole of lane A at once; this test plants ONE grievance between two co-located persons and plays a season
through `harness.probes.chooser` (the game's own policy) and `SeasonDriver.season`: no act is built here. The chain is
bound to the two persons through the driver's own `act_of` (event id -> the act that made it), which the test keeps:
the challenge was issued by A, the accept was declared by B on that challenge's Record, and the scene's outcome
(`body.changed` / `duel.yielded`) is an event of that accept's own act. The instruments watch and change nothing,
except the stamp's own planted failure (`challenges_heard` returning `()` alone), which the second test plays through
a whole season.

LIMITS. (1) The world is `probes.tiny_world()`, not `build_realm` (the gate says "a seeded realm"): a stated
departure, because a realm has no fixed co-located pair to plant a dispute between. (2) Existence at measured seeds,
not a rate: at the tree of this commit the chain completes at seeds 8, 13, 20 of 0-20 (it was 0, 3, 5 of 0-5 before the
keyed stream, B06; seeds 4-7 attempt accept with no accept.declared following, most others attempt none); a hash-moving
change re-measures.
"""
from __future__ import annotations

import pytest

from ..data.rosters import CHALLENGE_KIND
from ..decision import assemble
from ..decision import options as O
from ..harness import probes as P
from ..loop.driver import SeasonDriver, resolvable_verbs
from ..queries import world_q
from ..seam.wrappers import combat as CW
from ..state.carriers import Claim, subject_of

A, B = "p_mid", "p_low"           # `tiny_world`: both stand at the hearth; A holds the grievance, B is its object
SEEDS = range(21)                 # measured on `tiny_world`; see LIMITS above. Was range(6): under the keyed stream (B06) the chain completes at none of 0-5
#: How many of `SEEDS` the whole bound chain completes at, measured at the tree this floor was written on (8, 13, 20 of 0-20;
#: was 0, 3, 5 of 0-5 before B06's stream, and the floor is unchanged).
FLOOR = 3


def _play(seed, monkeypatch):
    """One season of the planted world through the real chooser; returns the world, the driver (whose `act_of` binds an
    event to the act that made it), what the chooser returned in order (`(actor, verb)`, a diagnostic: the driver
    drops done acts and releases at most `per_lap` scenes, so this is what was OFFERED, not what was attempted) and
    the terms every fight was built under."""
    w = P.tiny_world()
    w.world_seed = seed
    me = w.persons[A]
    me.ledger.append(Claim("c_vm_phy_a_deed", A, B, "fight.declared", True, w.tick, "firsthand", 100, "own"))
    me.pursuits = {"liberty": 1.0}                    # his own pursuits judge the deed against him: a dispute

    terms, offered = [], []
    real_input = CW.combat_input

    def spy_input(*a, **k):
        inp = real_input(*a, **k)
        terms.append(inp.terms)
        return inp
    monkeypatch.setattr(CW, "combat_input", spy_input)

    base = P.chooser(w, verbs=resolvable_verbs())

    def choose(p, v, s, ask_budget):
        scenes = base(p, v, s, ask_budget)
        offered.extend((a.actor, a.verb) for sc in scenes for a in sc.acts)
        return scenes
    d = SeasonDriver(w)
    d.season(choose, None, contest_max_depth=w.fixtures.get("contest_max_depth"))
    return w, d, offered, terms


def _made(w, d, kind, verb, actor=None):
    """`(event, act)` for each logged event of `kind` whose act (by `act_of`) is `verb` by `actor` (any, when `None`)."""
    return [(e, d.act_of[e.id]) for e in w.log
            if e.kind == kind and e.id in d.act_of and d.act_of[e.id].verb == verb
            and (actor is None or d.act_of[e.id].actor == actor)]


def _accepts_formed(w, pid):
    """`accept` Candidates in `pid`'s own opening set, on every question the world puts to him (the view is the
    size the real deliberation reads, `w.fixtures["view_k"]`)."""
    p = w.persons[pid]
    k_view = w.fixtures.get("view_k")
    return [c for q in world_q.questions_for(w, p)
            for c in O.opening_set(p, assemble(p, q, k_view), q, w.fixtures) if c.verb == "accept"]


def test_accept_forms_on_a_heard_challenge(monkeypatch):
    """The audit §4.7 gate. Planted failure: `challenges_heard` returning `()` alone turns this red (see the next test,
    which plays it). Control: the challenged's opening set holds `accept` with the stamp and none without it."""
    checked = complete = 0
    for seed in SEEDS:
        with monkeypatch.context() as m:
            w, d, offered, terms = _play(seed, m)
            kinds = [e.kind for e in w.log]
            # the challenge came from A, the real chooser's pick
            issued = _made(w, d, "challenge.issued", "challenge", A)
            assert issued, (seed, kinds, offered)
            challenge = issued[0][1]
            accepted = _made(w, d, "accept.declared", "accept", B)
            if accepted:
                complete += 1
                ev, act = accepted[0]
                # B's accept is on that challenge's own Record, and it came after the challenge
                assert subject_of(act) == "rec:" + challenge.id, (seed, subject_of(act), challenge.id)
                assert w.records[subject_of(act)].kind == CHALLENGE_KIND, (seed, w.records[subject_of(act)].kind)
                log = list(w.log)
                assert log.index(issued[0][0]) < log.index(ev), (seed, kinds)
                # the scene it set off ended in one of the duel's typed outcomes, an event of THAT accept's own act
                ends = [e for e in log[log.index(ev):]
                        if e.kind in ("duel.yielded", "body.changed") and d.act_of.get(e.id) is act]
                assert ends, (seed, kinds, offered)
                # a challenge names no stakes, so the one fight was built under the roster's `accept` line, `blood`
                assert terms and set(terms) == {"blood"}, (seed, terms)   # every fight the scene built, not their number: the draw moves how many a seed plays
                # CONTROL: B's opening set has `accept` while the stamp stands, and none with the stamp's reader at `()`
                assert _accepts_formed(w, B), (seed, "the challenged holds an `accept` with the stamp")
                m.setattr(world_q, "challenges_heard", lambda w, p, named=None: ())
                assert world_q.questions_for(w, w.persons[B]), (seed, "B is asked something at all")
                assert _accepts_formed(w, B) == [], (seed, "without the stamp the challenged has no `accept`")
        checked += 1
    assert checked == len(SEEDS)
    assert complete >= FLOOR, (complete, FLOOR)


def test_without_the_stamp_no_accept_forms_on_a_challenge(monkeypatch):
    """The planted failure, played through the season: with `world_q.challenges_heard` returning `()` (the real call
    shape is `(w, p, told)`) the challenge is still issued by A and B never offers, attempts or declares `accept`."""
    checked = 0
    for seed in SEEDS:
        with monkeypatch.context() as m:
            m.setattr(world_q, "challenges_heard", lambda w, p, named=None: ())
            w, d, offered, _terms = _play(seed, m)
            assert _made(w, d, "challenge.issued", "challenge", A), (seed, [e.kind for e in w.log])
            assert not [a for a in d.act_of.values() if a.actor == B and a.verb == "accept"], (seed, "attempted")
            assert (B, "accept") not in offered, (seed, offered)
            assert not _made(w, d, "accept.declared", "accept"), (seed, [e.kind for e in w.log])
            # the empty `accept` list is the stamp's absence, not B having no question at all
            assert world_q.questions_for(w, w.persons[B]), (seed, "B is asked something at all")
            assert _accepts_formed(w, B) == [], seed
        checked += 1
    assert checked == len(SEEDS)
