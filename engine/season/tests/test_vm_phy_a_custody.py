"""`14_VERBS_PHYSICAL_A` (custody and force) -- the gates of the audit's §1.7, §2.7, §3.7 and §4.7, one function each.
This file holds A4's (B14.27); A3's (B15) and A1/A2's (B29) are added by their items.

A4, THE REAL CHOOSER. `test_b11a_duel_reach.py` drives the chain through formed Candidates and hand-built acts and
reverts the whole of lane A at once; this test plants ONE grievance between two co-located persons and plays a season
through `harness.probes.chooser` (the game's own policy) and `SeasonDriver.season`: no act is built here. The only
instruments are two spies that watch and change nothing -- one on what the chooser releases, one on the terms a
fight is built under -- and the stamp's own planted failure, `challenges_heard` returning `()` alone.
"""
from __future__ import annotations

import pytest

from ..decision import assemble
from ..decision import options as O
from ..harness import probes as P
from ..loop.driver import SeasonDriver, resolvable_verbs
from ..queries import world_q
from ..seam.wrappers import combat as CW
from ..state.carriers import Claim

A, B = "p_mid", "p_low"           # `tiny_world`: both stand at the hearth; A holds the grievance, B is its object
#: Seeds at which the real chooser reaches the whole chain on this world (measured 0-5 on `tiny_world`: 0, 3 and 5 reach
#: it by A challenging and B accepting; 1 and 2 stop earlier, and 4's accept is a third man's, so none of those is a pin).
SEEDS = (0, 3, 5)


def _play(seed, monkeypatch):
    """One season of the planted world through the real chooser; returns the world, what the chooser released in order
    (`(actor, verb)`), and the terms every fight was built under."""
    w = P.tiny_world()
    w.world_seed = seed
    me = w.persons[A]
    me.ledger.append(Claim("c_vm_phy_a_deed", A, B, "fight.declared", True, w.tick, "firsthand", 100, "own"))
    me.pursuits = {"liberty": 1.0}                    # his own pursuits judge the deed against him: a dispute

    terms, released = [], []
    real_input = CW.combat_input

    def spy_input(*a, **k):
        inp = real_input(*a, **k)
        terms.append(inp.terms)
        return inp
    monkeypatch.setattr(CW, "combat_input", spy_input)

    base = P.chooser(w, verbs=resolvable_verbs())

    def choose(p, v, s, ask_budget):
        scenes = base(p, v, s, ask_budget)
        released.extend((a.actor, a.verb) for sc in scenes for a in sc.acts)
        return scenes
    SeasonDriver(w).season(choose, None, contest_max_depth=w.fixtures.get("contest_max_depth"))
    return w, released, terms


def _accepts_formed(w, pid):
    """`accept` Candidates in `pid`'s own opening set, on every question the world puts to him."""
    p = w.persons[pid]
    return [c for q in world_q.questions_for(w, p)
            for c in O.opening_set(p, assemble(p, q, 12), q, w.fixtures) if c.verb == "accept"]


def test_accept_forms_on_a_heard_challenge(monkeypatch):
    """The audit §4.7 gate. Planted failure: `challenges_heard` returning `()` alone (a monkeypatch of that one reader)
    turns this red at the first `accept` assertion. Control: the challenged's opening set holds `accept` with the stamp
    and none without it."""
    checked = 0
    for seed in SEEDS:
        with monkeypatch.context() as m:
            w, released, terms = _play(seed, m)
            kinds = [e.kind for e in w.log]
            assert "challenge.issued" in kinds, (seed, kinds)
            # the challenge came from the real chooser, then the challenged attempted `accept`, in that order
            assert (A, "challenge") in released, (seed, released)
            assert (B, "accept") in released, (seed, released)
            assert released.index((A, "challenge")) < released.index((B, "accept")), (seed, released)
            # `accept` resolved, and the scene it set off ended in one of the duel's typed outcomes, after the challenge
            assert "accept.declared" in kinds, (seed, kinds)
            assert kinds.index("challenge.issued") < kinds.index("accept.declared"), (seed, kinds)
            assert {"duel.yielded", "body.changed"} & set(kinds[kinds.index("accept.declared"):]), (seed, kinds)
            # a challenge names no stakes, so the one fight was built under the roster's `accept` line, `blood`
            assert terms == ["blood"], (seed, terms)
            # CONTROL: B's opening set has `accept` while the stamp stands, and none with the stamp's reader at `()`
            assert _accepts_formed(w, B), (seed, "the challenged holds an `accept` with the stamp")
            m.setattr(world_q, "challenges_heard", lambda w, p, named=None: ())
            assert _accepts_formed(w, B) == [], (seed, "without the stamp the challenged has no `accept`")
        checked += 1
    assert checked == len(SEEDS) >= 3
