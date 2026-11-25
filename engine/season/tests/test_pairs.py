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


def _carried(pairs) -> tuple:
    """`(carried, pairs)` of an iterable of `ProceedingPair`s: a pair carried where its band is Success or Overwhelming."""
    bands = [p.band for p in pairs]
    return sum(b in PAIRS.CARRIED for b in bands), len(bands)


def test_proceeding_pairs_are_reproducible():
    """The same arguments give equal pairs: sheets, the third person's, the record, the band and the whole `Outcome` (every beat), in both
    forms and in the room that seats a bench and onlookers."""
    for type_id, form, room in (("conversation", "abridged", "none"), ("conversation", "full", "none"), ("legal_trial", "full", "gallery")):
        one = list(PAIRS.proceeding_pairs(3, 40, type_id, form, room))
        two = list(PAIRS.proceeding_pairs(3, 40, type_id, form, room))
        assert one == two and len(one) == 40, (type_id, form, room)
        assert any(len(p.outcome.beats) for p in one)     # a sitting, not an empty record that equals itself


def test_a_planted_speaker_of_higher_reason_carries_more_often():
    """The instrument can see an effect: `a` at Reason 6 and `b` at Reason 2 (everything else equal, the pair's own other keys) carries more
    often than the mirror, `a` at 2 and `b` at 6, on the same streams, by more than two standard errors of the difference. The shipped
    settings, in an abridged conversation (the speech weighed by the one addressed)."""
    def planted(a_reason, b_reason):
        def plant(i, a, b):
            return {**a, _REASON: a_reason}, {**a, _REASON: b_reason}
        return plant
    n = 1000
    (hi, _), (lo, _) = (_carried(PAIRS.proceeding_pairs(0, n, "conversation", "abridged", "none", plant=planted(*r))) for r in ((6, 2), (2, 6)))
    p_hi, p_lo = hi / n, lo / n
    se = math.sqrt(p_hi * (1 - p_hi) / n + p_lo * (1 - p_lo) / n)
    assert p_hi - p_lo > 2 * se, (p_hi, p_lo, se)


def test_the_instrument_reads_an_end_and_an_exchange_count():
    """The instrument calls the module's entry and not `roll`: a full sitting ends in a member of `proceeding_ends` and counts its
    exchanges (an abridged act is one speech); a `roll` would return no beats and no end, and `ENDS` would be empty."""
    full = PAIRS.proceeding_report(0, 400, "conversation", "full", "none", "for", None, "read", 20)
    ends = next(x for x in full if x.startswith("ENDS"))
    shares = {k: float(v) for k, _, v in (part.partition("=") for part in ends.split()[1:])}
    assert set(shares) == set(PROCEEDING_ENDS) and abs(sum(shares.values()) - 1.0) < 1e-9     # every sitting ended as the roster says: no `none`
    assert float(next(x for x in full if x.startswith("EXCHANGES")).split()[1]) > 1.0
    assert float(next(x for x in PAIRS.proceeding_report(0, 400, "conversation", "abridged", "none", "for", None, "read", 20)
                      if x.startswith("EXCHANGES")).split()[1]) == 1.0


def test_an_operand_off_reads_a_flat_curve():
    """An operand at its control reads a flat curve exactly: Reason's own beat field `relevance` (`--off relevance`) by the Reason difference,
    the abridged form. The class read is whether the speech's `relevance` departs from the plain 1.0; off it never does (slope and range
    exactly 0 over a curve of several bins), on it does, so the flat curve is not a curve too short to slope. (The carried share is NOT
    flat in Reason at the controls, and cannot be: the ground's `reason` column ships 1.0, the dice are Reason's.)"""
    def read(off):
        accs, _, _ = PAIRS.accumulate(PAIRS.proceeding_pairs(0, 1500, "conversation", "abridged", "none", off=off),
                                      lambda p: "moved" if p.outcome.beats[0].relevance != 1.0 else "plain", (_REASON,))
        return PAIRS.curve(accs[_REASON], 1.0, 20, lambda c: c["moved"])
    on, off = read(None), read("relevance")
    assert len(off["rows"]) >= 5 and off["slope"] == 0.0 and off["range"] == 0.0
    assert len(on["rows"]) >= 5 and on["range"] > 0.0
