"""B01a.04 -- THE RANDOM-PAIRS INSTRUMENT (`harness/pairs.py`): outcome by attribute difference, the slope, the spread.

An instrument every later calibration reads, so its own controls come first. Each arm below can observe the failure
it excludes:

  * IDENTICAL PAIRS read the even line (duel, in both seat orders) or the roll's own odds (social). An instrument that
    tilts identical sheets, or that cannot reproduce the roll's own exact enumeration, is not measuring the contest.
  * A PLANTED EDGE moves the curve. An instrument blind to an attribute would read the same line with +2 on every key.
  * THE SLOPE'S STANDARD ERROR: a key the roll does not read holds the slope within 3 SE of 0; the pool key moves it
    more than 3 SE; and the SE is the binomial formula, worked by hand on planted bins.
  * DETERMINISM: the same arguments print the same block; another seed prints another.
  * THE REFACTOR'S CONTROL: `combat.scene_outcome`, the per-scene reading `fight_estimate` moved into, classifies a
    scene the way `fight_estimate` counted it -- planted traces, and the shares `fight_estimate` returns recounted
    through `scene_outcome` over the same stream.

`[ASSUMPTION: the test names; the item creates them]`.
"""
from __future__ import annotations

import math
from collections import Counter

import pytest

from engine.substrate.descriptors import ATTRIBUTE_CEILING, ATTRIBUTES

from ..data import rosters as R
from ..data import verbs as V
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


@pytest.mark.parametrize("first, second", [("p_low", "p_mid"), ("p_mid", "p_low")])
def test_identical_fighters_give_the_even_line_in_either_seat(first, second, monkeypatch):
    """Both seat orders: with one order only, the first-named party is always `p_low`, so a first-seat advantage and an
    advantage of being `p_low` (any field of his besides the sheet) could not be told apart. Each order reads even."""
    monkeypatch.setattr(pairs, "FIRST", first)
    monkeypatch.setattr(pairs, "SECOND", second)
    rows = list(pairs.duel_pairs(0, 4000, "blood", plant=lambda i, a, b: (a, a)))
    share, decided = _first_share(rows)
    assert decided >= 3000, decided
    assert abs(share - 0.5) <= 3 * math.sqrt(0.25 / decided), (first, share, decided)


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


def _argue_keys() -> tuple:
    """`(pool key, opposition key, a key neither role reads)` for `argue`, off the rosters `seam/wrappers/pool.py` reads."""
    voc = V.VERB_CAPABILITY["argue"]
    pool_key = V.VOCATION_ATTRIBUTE[voc]
    opp_key = V.VOCATION_OPPOSED_BY.get(voc) or pool_key
    unread = next(k for k in ATTRIBUTES if k not in (pool_key, opp_key))
    return pool_key, opp_key, unread


def _social_curve(plant, key: str, n: int = 20000):
    rows = list(pairs.social_pairs(0, n, "argue", plant=plant))
    accs, _, _ = pairs.accumulate(rows, lambda p: p.band, (key,))
    return rows, pairs.curve(accs[key], pairs._width(key), pairs.DEFAULT_MIN_BIN, lambda c: sum(c[b] for b in pairs.CARRIED))


def test_the_slope_s_standard_error_holds_a_null_key_at_zero_and_a_planted_edge_away_from_it():
    """THE SLOPE'S STANDARD ERROR, OBSERVED BOTH WAYS. NULL: the pair differs only on a key neither role reads, so every
    pair builds ONE record (asserted) and the curve over that key is flat by construction: its slope is within 3 SE of 0.
    EDGE: the actor's pool key alone is drawn, the other sheet fixed: the slope is more than 3 SE above 0. An SE too small
    fails the first; an SE too large (or a slope blind to the key) fails the second."""
    pool_key, _, unread = _argue_keys()
    rows, null = _social_curve(lambda i, a, b: (FIXED, {**FIXED, unread: b[unread]}), unread)
    assert all(r.inp == rows[0].inp for r in rows), f"{unread} reaches the record: it is not an unread key"
    assert len(null["rows"]) >= 5 and null["slope_se"] > 0, null
    assert abs(null["slope"]) <= 3 * null["slope_se"], (null["slope"], null["slope_se"])
    _, edge = _social_curve(lambda i, a, b: ({**FIXED, pool_key: a[pool_key]}, FIXED), pool_key)
    assert len(edge["rows"]) >= 5 and edge["slope_se"] > 0, edge
    assert edge["slope"] > 3 * edge["slope_se"], (edge["slope"], edge["slope_se"])


def test_the_slope_s_standard_error_is_the_binomial_formula():
    """`curve`'s `slope_se` against the formula worked by hand on three planted bins (to float rounding: a wrong formula
    misses by far more than 1e-12 relative)."""
    acc = {0: Counter(win=100, loss=300), 1: Counter(win=200, loss=200), 2: Counter(win=150, loss=50)}
    c = pairs.curve(acc, 1.0, 1, lambda k: k["win"])
    xbar = (0 * 400 + 1 * 400 + 2 * 200) / 1000                     # 0.8
    sxx = 400 * 0.8 ** 2 + 400 * 0.2 ** 2 + 200 * 1.2 ** 2         # 560
    var = 400 * 0.8 ** 2 * 0.25 * 0.75 + 400 * 0.2 ** 2 * 0.25 + 200 * 1.2 ** 2 * 0.75 * 0.25
    assert math.isclose(c["slope_se"], math.sqrt(var) / sxx, rel_tol=1e-12, abs_tol=0.0), (c["slope_se"], math.sqrt(var) / sxx)


def test_the_instrument_is_deterministic_given_its_seed(capsys):
    def printed(*argv):
        pairs.main(list(argv))
        return capsys.readouterr().out

    duel = printed("duel", "--terms", "blood", "--n", "500", "--seed", "0", "--min-bin", "20")
    assert duel and "SLOPE" in duel
    # the slope is printed with its standard error and the window of bins it was read over
    slope_line = next(line for line in duel.splitlines() if line.startswith("SLOPE"))
    assert " +/- " in slope_line and "bins read, x from " in slope_line, slope_line
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
