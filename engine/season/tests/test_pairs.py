"""B01a.04 -- THE REFACTOR'S CONTROL for the random-pairs instrument (`harness/pairs.py`).

`combat.scene_outcome`, the per-scene reading `fight_estimate` moved into, classifies a scene the way `fight_estimate`
counted it -- planted traces, and the shares `fight_estimate` returns recounted through `scene_outcome` over the same
stream.

B24p.17 -- `pairs proceeding`: the same instrument over the proceeding entry (the entry its composition row names, never `roll`).
"""
from __future__ import annotations

import math

from engine.substrate import descriptors

from ..data.rosters import PROCEEDING_ENDS
from ..harness import pairs as PAIRS
from ..harness import probes as P
from ..loop.driver import SeasonDriver
from ..queries.inputs import CombatOutcome, PartyWounds, SceneShape, Surrender
from ..seam.wrappers import combat
from ..seam.wrappers._estimate import rng_of, samples_of
from ..seam.wrappers._entry import entry_for


def _scene(w, actor, target, **felled_yield) -> CombatOutcome:
    """A planted scene: `felled` names who is down, `yielded` the declarer of a `yield` event (the module entry lifts a refused declaration to no
    `Surrender`, so a refused one is a scene with none)."""
    def state(pid):
        return PartyWounds(felled=pid in felled_yield.get("felled", ()), wounds=0, max_wounds=3,
                           health_remaining=5, health_full=5)
    yielded = felled_yield.get("yielded")
    surrender = None if yielded is None else Surrender(by=yielded, round=2, accepted=True)
    return CombatOutcome(claimants=(actor, target), wounds={actor: state(actor), target: state(target)},
                         surrender=surrender, beat=None, rounds=2,
                         shape=SceneShape(rounds=2, blows={actor: 0, target: 0}, first_blood=None, lead_changes=0, nearest={}), trace=())


def test_scene_outcome_reads_what_fight_estimate_read():
    a, b = "p_low", "p_mid"
    w = P.tiny_world()
    SeasonDriver(w)
    assert combat.scene_outcome(_scene(w, a, b, felled=(a,)), a, b) == ("actor_felled", None)
    assert combat.scene_outcome(_scene(w, a, b, felled=(b,)), a, b) == ("subject_felled", None)
    assert combat.scene_outcome(_scene(w, a, b, felled=(a, b)), a, b) == ("undecided", None)
    assert combat.scene_outcome(_scene(w, a, b), a, b) == ("undecided", None)
    assert combat.scene_outcome(_scene(w, a, b, yielded=b), a, b) == ("yielded", b)
    assert combat.scene_outcome(_scene(w, a, b, yielded=a, felled=(b,)), a, b) == ("yielded", a)   # a yield is read first
    # every outcome is a member of the roster `fight_estimate` shares out
    for felled in ((), (a,), (b,), (a, b)):
        assert combat.scene_outcome(_scene(w, a, b, felled=felled), a, b)[0] in combat.ESTIMATE_OUTCOMES
    # THE WHOLE OF THE REFACTOR'S CONTROL, run: fight_estimate's returned shares equal a recount of the same scenes
    # (same entry, same record, same private stream) through `scene_outcome`.
    for verb in ("fight", "capture", "accept"):
        w = P.tiny_world()
        SeasonDriver(w)
        got = combat.fight_estimate(w, a, None, b, verb)
        assert got["status"] == "ESTIMATED"
        entry, _ = entry_for(combat._PRIZE, combat._PROVIDER)
        # the estimate's own record: no dealt mortal key (B15.07), so its mortal draws are off the same private stream
        inp, rng, n = combat.combat_input(w, [a, b], verb, mortal_keyed=False), rng_of(w, a), samples_of(w)
        tally = dict.fromkeys(combat.ESTIMATE_OUTCOMES, 0)
        for _ in range(n):
            tally[combat.scene_outcome(entry.fn(inp, rng), a, b)[0]] += 1
        assert {k: tally[k] / n for k in tally} == {k: got[k] for k in combat.ESTIMATE_OUTCOMES}, verb
        assert sum(tally.values()) == n


# ---------------------------------------------------------------------------------------------------------------
# B24p.17 -- `pairs proceeding`
# ---------------------------------------------------------------------------------------------------------------

_REASON = descriptors.ATTRIBUTE_NAMES["reason"]










