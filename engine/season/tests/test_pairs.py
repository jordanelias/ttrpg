"""B01a.04 -- THE RANDOM-PAIRS INSTRUMENT (`harness/pairs.py`): outcome by attribute difference, the slope, the spread.

An instrument every later calibration reads, so its own controls come first. Each arm below can observe the failure
it excludes:

  * IDENTICAL PAIRS read the even line (duel) or the roll's own odds (social). An instrument that tilts identical
    sheets, or that cannot reproduce the roll's own exact enumeration, is not measuring the contest.
  * A PLANTED EDGE moves the curve. An instrument blind to an attribute would read the same line with +2 on every key.
  * DETERMINISM: the same arguments print the same block; another seed prints another.
  * THE REFACTOR'S CONTROL: `combat.scene_outcome`, the per-scene reading `fight_estimate` moved into, classifies a
    scene the way `fight_estimate` counted it -- planted traces, and the shares `fight_estimate` returns recounted
    through `scene_outcome` over the same stream.

`[ASSUMPTION: the test names; the item creates them]`.
"""
from __future__ import annotations

import math

from engine.substrate.descriptors import ATTRIBUTE_CEILING, ATTRIBUTES

from ..harness import pairs
from ..harness import probes as P
from ..loop.driver import SeasonDriver
from ..seam.wrappers import combat, sigma
from ..seam.wrappers._estimate import rng_of, samples_of
from ..seam.wrappers._entry import entry_for

FIXED = {k: 3 for k in ATTRIBUTES}          # the social arm's one sheet: the fixed value is the test's subject


def _plus_two(sheet: dict) -> dict:
    return {k: min(v + 2, ATTRIBUTE_CEILING) for k, v in sheet.items()}


def _first_share(rows) -> tuple:
    """`(first-named party's share of the decided duels, decided)`: a draw has no winner, so it is not counted."""
    a = sum(1 for r in rows if r.winner == "a")
    b = sum(1 for r in rows if r.winner == "b")
    return a / (a + b), a + b


def test_identical_fighters_give_the_even_line():
    rows = list(pairs.duel_pairs(0, 4000, "blood", plant=lambda i, a, b: (a, a)))
    share, decided = _first_share(rows)
    assert decided >= 3000, decided
    assert abs(share - 0.5) <= 3 * math.sqrt(0.25 / decided), (share, decided)


def test_a_planted_edge_of_two_moves_the_line():
    rows = list(pairs.duel_pairs(0, 4000, "blood", plant=lambda i, a, b: (_plus_two(a), a)))
    share, decided = _first_share(rows)
    assert decided >= 3000, decided
    assert share > 0.5 + 3 * math.sqrt(0.25 / decided), (share, decided)


def _band_counts(rows) -> dict:
    counts = dict.fromkeys(pairs.BANDS, 0)
    for r in rows:
        counts[r.band] += 1
    return counts


def test_identical_speakers_read_the_roll_s_own_odds():
    n = 20000
    rows = list(pairs.social_pairs(0, n, "argue", plant=lambda i, a, b: (FIXED, FIXED)))
    odds = sigma._odds_of_input(rows[0].inp)
    assert odds is not None and abs(sum(odds) - 1.0) < 1e-9, odds
    assert all(r.inp == rows[0].inp for r in rows), "identical sheets must build one record"
    counts = _band_counts(rows)
    checked = 0
    for band, p in zip(pairs.BANDS, odds):
        se = math.sqrt(p * (1 - p) / n)
        assert abs(counts[band] / n - p) <= 3 * se + 1e-12, (band, counts[band] / n, p, se)
        checked += 1
    assert checked == len(pairs.BANDS) == 4


def test_a_planted_edge_moves_the_carried_share():
    n = 20000

    def carried(plant):
        rows = list(pairs.social_pairs(0, n, "argue", plant=plant))
        counts = _band_counts(rows)
        y = sum(counts[b] for b in pairs.CARRIED) / n
        return y, math.sqrt(y * (1 - y) / n)

    y0, se0 = carried(lambda i, a, b: (FIXED, FIXED))
    y1, se1 = carried(lambda i, a, b: (_plus_two(FIXED), FIXED))
    assert y1 > y0 + 3 * math.hypot(se0, se1), (y0, y1, se0, se1)


def test_the_instrument_is_deterministic_given_its_seed(capsys):
    def printed(*argv):
        pairs.main(list(argv))
        return capsys.readouterr().out

    duel = printed("duel", "--terms", "blood", "--n", "500", "--seed", "0", "--min-bin", "20")
    assert duel and "SLOPE" in duel
    assert printed("duel", "--terms", "blood", "--n", "500", "--seed", "0", "--min-bin", "20") == duel
    assert printed("duel", "--terms", "blood", "--n", "500", "--seed", "1", "--min-bin", "20") != duel
    social = printed("social", "--n", "500", "--seed", "0", "--min-bin", "20")
    assert printed("social", "--n", "500", "--seed", "0", "--min-bin", "20") == social
    assert printed("social", "--n", "500", "--seed", "1", "--min-bin", "20") != social


def _scene(w, actor, target, **felled_yield) -> dict:
    """A planted scene: `felled` names who is down, `yielded` the declarer of a `yield` event, `refused` marks it refused."""
    def state(pid):
        return combat._wound_state(dict(felled=pid in felled_yield.get("felled", ()), wounds=0, max_wounds=3,
                                        health_remaining=5, health_full=5))
    trace = []
    if "yielded" in felled_yield:
        trace.append(dict(kind="yield", by=felled_yield["yielded"], turn=2, accepted=True,
                          refused="contested" if felled_yield.get("refused") else None))
    return dict(trace=trace, wound_state={actor: state(actor), target: state(target)})


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
    assert combat.scene_outcome(_scene(w, a, b, yielded=b, refused=True, felled=(a,)), a, b) == ("actor_felled", None)
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
        inp, rng, n = combat.combat_input(w, [a, b], verb), rng_of(w, a), samples_of(w)
        tally = dict.fromkeys(combat.ESTIMATE_OUTCOMES, 0)
        for _ in range(n):
            tally[combat.scene_outcome(entry.fn(inp, rng), a, b)[0]] += 1
        assert {k: tally[k] / n for k in tally} == {k: got[k] for k in combat.ESTIMATE_OUTCOMES}, verb
        assert sum(tally.values()) == n
