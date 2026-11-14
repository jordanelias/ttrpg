"""THE RANDOM-PAIRS INSTRUMENT (B01a.04; Jordan 2026-11-13/14, rulings (4) and (5)): a contest's outcome by attribute
difference, read over generated random pairs at a very high iteration count, as a CURVE -- never one even-matchup
number. A-79's even centres are the curve's middle bin.

    python -m engine.season.harness.pairs {duel,social} [--terms yield blood death] [--verb argue] [--n N]
                                          [--seed S ...] [--diff sheet|read|<registry key>|all] [--min-bin 200]

WHAT IS DRAWN. For each seed `s` and pair `i` in `0 .. N-1` the two sheets are `state/carriers.py::generated_attributes`
(`s`, `f"pair{i}.a"` / `f"pair{i}.b"`, `Fixtures generated_attribute_range`): the instrument's population is the
generated world's. The pair's stream is `draw_factory(s, lambda: 0)(f"pair{i}", f"pairs:{contest}:{terms or verb}")`.
Deterministic given its arguments: no `random.Random(`, no clock.
  `duel`   one `probes.tiny_world()` per seed, `SeasonDriver` built once (the registrar fills the module entries); per
           pair the two fighters (`p_low`, `p_mid`) are replaced by `dataclasses.replace(person, attributes=sheet)`;
           `combat.combat_input` (its `terms` replaced by the terms under test) goes to the combat module entry, and the
           scene is read by `combat.scene_outcome` (the one owner `fight_estimate` also reads by). The first-named
           party (`a`) wins when the subject is felled and he is not, or the subject yielded; `b` wins the mirror;
           anything else is `undecided`. The curve's value `y` is `a`'s share of ALL the bin's pairs.
  `social` the same world; `sigma.contest_input(w, [a, b], verb=<verb>, subject=b)`; the module's roll found by its
           composition row (`composition.ROLES["social_contest.roll"]["target"]`); the margin graded as the fold grades
           it (S27.4's refusal, the margin's fraction settled by the pair's own stream, `ladder.degree_of`). `y` is the
           share of the CARRIED bands (Success and Overwhelming: the margin cleared the obstacle by a whole success);
           every band's share is printed.

THE DIFFERENCE `d`. `sheet` (the duel's default): the mean over the ten keys of `a[k] - b[k]`, bins of 0.5. `read` (the
social roll's default): the record's `pool` minus its `opposition` (for a duel, `faculties[0] - faculties[1]`; an
opposition `None` reads as `obstacle_default`), read off the input so the instrument follows whatever the governing
score becomes, bins of 1. A registry key: `a[k] - b[k]`, bins of 1. `all` prints one SLOPE per key (a slope near 0 names
a key the contest does not read). Bins are rounded half up, `floor(x / width + 0.5)`; the tree's public `round_half_up`
is B38.55's, and this exact local one is replaced by it then (`modules/mass_battle/massbattle.py` holds a private one, not
imported across the module boundary).

WHAT IS PRINTED, per contest and seed. `POPULATION`: the pairs per bin. Per bin with at least `--min-bin` pairs: its
count, the share of each outcome, `y` and its binomial standard error `sqrt(y (1 - y) / n)`.
  SLOPE     the least-squares slope of `y` on the bin centre `x`, weighted by the bin's pair count:
            `sum n_b (x_b - xbar)(y_b - ybar) / sum n_b (x_b - xbar)^2`, `xbar` and `ybar` the count-weighted means.
            It is the change in the curve per point of difference.
  SPREAD    the range `max y_b - min y_b` and the count-weighted standard deviation of `y_b` about `ybar`.
  MONOTONE  `yes` when each bin's `y` is at or above its left neighbour's less two standard errors of their
            difference, `sqrt(se_b^2 + se_left^2)`; else `no`.
  DOMINANT  the largest single outcome share in any bin, with its bin: ruling (4)'s "no bin dominant above a stated
            share" read as one outcome's share of a bin's pairs (UNDECIDED (5)); the stated share is the caller's.

`slope` and `spread` are meant in their ordinary statistical sense; this is no check and no gate (it is a reading).

DEFAULTS AND TIMING (measured on the producer's machine, 2026-11-14, with the shell's `time`, `--n 1000` wall seconds,
of which 0.62 s is importing the package): duel `yield` 2.26, `blood` 2.04, `death` 2.88; `social` 1.20. The cost per
1,000 pairs once warm, from longer runs: `death` 1.7 s (`--n 5000`: 9.3 s wall) and `social` 0.25 s (`--n 20000`: 5.6 s
wall; the 200,000 default is about 50 s). So the defaults, `--n` 20,000 per duel terms (about 35 to 55 s) and 200,000 for
`social`, each cost under the two minutes a contest the item allows, and none was lowered. (The drafting lane's scratch
reading, on fighters at 3 on every key, was 1.1 / 0.7 / 1.9 s per 1,000 duels and 0.015 s per 1,000 social rolls: a
comparison, not a target. The social figure here includes building the record, `contest_input`, which that reading did not.)
"""
from __future__ import annotations

import argparse
import dataclasses
import importlib
import math
import sys
from collections import Counter, namedtuple
from typing import Callable, Optional

from engine.dice_engine.dice_engine import DEGREE_LABEL, DEGREE_ORDINAL, Degree
from engine.dice_engine.sigma_leverage import settle_record
from engine.substrate import composition
from engine.substrate.descriptors import ATTRIBUTES

from ..data.fixtures import DEFAULT_FIXTURES
from ..loop.driver import SeasonDriver
from ..seam.ladder import degree_of
from ..seam.wrappers import combat, sigma
from ..seam.wrappers._entry import entry_for
from ..state.carriers import generated_attributes
from ..state.ids import draw_factory
from . import probes

FIRST, SECOND = "p_low", "p_mid"            # the world's two fighters / speakers (test-fixture ids, `probes.tiny_world`)
DEFAULT_N = {"duel": 20000, "social": 200000}
DEFAULT_MIN_BIN = 200
REFUSED = "Refused"                          # S27.4: ob > obstacle_refusal_multiple x pool, no dice dealt (not a band)
# the four bands in the owner's order (`DEGREE_ORDINAL`, the tuple `band_odds` returns), and the two a carried contest reaches
BANDS = tuple(DEGREE_LABEL[d] for d in sorted(DEGREE_ORDINAL, key=DEGREE_ORDINAL.get))
CARRIED = tuple(DEGREE_LABEL[d] for d in (Degree.SUCCESS, Degree.OVERWHELMING))
DUEL_OUTCOMES = ("a_wins", "b_wins", "undecided")
DIFF_WIDTH = {"sheet": 0.5, "read": 1.0}     # a registry key's bin is 1.0

DuelPair = namedtuple("DuelPair", "i a b read outcome yielder winner")
SocialPair = namedtuple("SocialPair", "i a b read inp band")
Plant = Optional[Callable[[int, dict, dict], tuple]]


def _span():
    return DEFAULT_FIXTURES.get("generated_attribute_range")


def _bin(x: float, width: float) -> int:
    """Half-up rounding of `x / width` (exact): B38.55 provides the public `round_half_up` owner, and this is replaced by it."""
    return math.floor(x / width + 0.5)


def _world():
    w = probes.tiny_world()
    SeasonDriver(w)
    return w


def _sheets(seed: int, i: int, plant: Plant) -> tuple:
    a = generated_attributes(seed, f"pair{i}.a", _span())
    b = generated_attributes(seed, f"pair{i}.b", _span())
    return plant(i, a, b) if plant is not None else (a, b)


def _seat(w, a: dict, b: dict) -> None:
    """The two fighters become new `Person`s holding the sheets (a new record, never a field assignment)."""
    w.persons[FIRST] = dataclasses.replace(w.persons[FIRST], attributes=a)
    w.persons[SECOND] = dataclasses.replace(w.persons[SECOND], attributes=b)


def duel_pairs(seed: int, n: int, terms: str, plant: Plant = None):
    """Yield one `DuelPair` per pair `0 .. n-1`; `plant(i, a, b) -> (a, b)` replaces the drawn sheets (a test's planted pair)."""
    w = _world()
    entry, refusal = entry_for(combat._PRIZE, combat._PROVIDER)
    if entry is None:
        raise RuntimeError(f"the combat module entry is unavailable: {refusal}")
    draw = draw_factory(seed, lambda: 0)
    for i in range(n):
        a, b = _sheets(seed, i, plant)
        _seat(w, a, b)
        inp = dataclasses.replace(combat.combat_input(w, [FIRST, SECOND], "fight"), terms=terms)
        got = entry.fn(inp, draw(f"pair{i}", f"pairs:duel:{terms}"))
        outcome, yielder = combat.scene_outcome(got, FIRST, SECOND)
        if outcome == "subject_felled" or (outcome == "yielded" and yielder == SECOND):
            winner = "a"
        elif outcome == "actor_felled" or (outcome == "yielded" and yielder == FIRST):
            winner = "b"
        else:
            winner = None
        yield DuelPair(i, a, b, inp.faculties[0] - inp.faculties[1], outcome, yielder, winner)


def _roll():
    target = composition.ROLES["social_contest.roll"]["target"]
    module, _, name = target.partition(":")
    return getattr(importlib.import_module(module), name)


def social_pairs(seed: int, n: int, verb: str, plant: Plant = None):
    """Yield one `SocialPair` per pair: the record, and the band the margin grades to (`REFUSED` where S27.4 refuses)."""
    w = _world()
    roll = _roll()
    draw = draw_factory(seed, lambda: 0)
    for i in range(n):
        a, b = _sheets(seed, i, plant)
        _seat(w, a, b)
        inp = sigma.contest_input(w, [FIRST, SECOND], verb=verb, subject=SECOND)
        rng = draw(f"pair{i}", f"pairs:social:{verb}")
        margin = roll(inp, rng)
        if margin.ob > inp.obstacle_refusal_multiple * max(inp.pool, 0):
            band = REFUSED
        else:
            settled = settle_record(margin.net, inp.leverage, inp.pool, margin.ob, rng.random)
            band = degree_of(dict(net=margin.net, ob=margin.ob, settled_margin=settled))
        opposition = inp.obstacle_default if inp.opposition is None else inp.opposition
        yield SocialPair(i, a, b, inp.pool - opposition, inp, band)


# ---------------------------------------------------------------------------------------------------------------
# the curve
# ---------------------------------------------------------------------------------------------------------------

def _diffs(p, which: tuple) -> dict:
    """`{diff name: d}` for the differences asked."""
    out = {}
    for name in which:
        if name == "sheet":
            out[name] = sum(p.a[k] - p.b[k] for k in ATTRIBUTES) / len(ATTRIBUTES)
        elif name == "read":
            out[name] = p.read
        else:
            out[name] = p.a[name] - p.b[name]
    return out


def _width(name: str) -> float:
    return DIFF_WIDTH.get(name, 1.0)


def curve(acc: dict, width: float, min_bin: int, carried: Callable[[Counter], int]) -> dict:
    """The curve of one difference: `acc` is `{bin index: Counter of outcomes}`. Pure; returns the bins with at least
    `min_bin` pairs and SLOPE, SPREAD, MONOTONE and DOMINANT."""
    rows = []
    for idx in sorted(acc):
        c = acc[idx]
        n = sum(c.values())
        if n < min_bin:
            continue
        y = carried(c) / n
        rows.append(dict(idx=idx, x=idx * width, n=n, counts=c, y=y, se=math.sqrt(y * (1 - y) / n)))
    out = dict(rows=rows, slope=None, range=None, sd=None, monotone=None, dominant=None)
    if not rows:
        return out
    total = sum(r["n"] for r in rows)
    xbar = sum(r["n"] * r["x"] for r in rows) / total
    ybar = sum(r["n"] * r["y"] for r in rows) / total
    sxx = sum(r["n"] * (r["x"] - xbar) ** 2 for r in rows)
    out["slope"] = sum(r["n"] * (r["x"] - xbar) * (r["y"] - ybar) for r in rows) / sxx if sxx > 0 else None
    out["range"] = max(r["y"] for r in rows) - min(r["y"] for r in rows)
    out["sd"] = math.sqrt(sum(r["n"] * (r["y"] - ybar) ** 2 for r in rows) / total)
    out["monotone"] = all(r["y"] >= l["y"] - 2 * math.hypot(r["se"], l["se"]) for l, r in zip(rows, rows[1:]))
    out["dominant"] = max(((v / r["n"], r["x"], k) for r in rows for k, v in r["counts"].items()),
                          key=lambda t: (t[0], -t[1], t[2]))
    return out


def _fmt(v: Optional[float], places: int = 4) -> str:
    return "n/a" if v is None else f"{v:.{places}f}"


def _render(title: str, classes: tuple, population: Counter, c: dict, width: float, min_bin: int, label: str) -> list:
    lines = [f"{title} diff={label} bin={width:g} min-bin={min_bin}",
             "POPULATION " + " ".join(f"{i * width:g}:{population[i]}" for i in sorted(population))]
    lines.append("  x      n      " + " ".join(f"{k:>11}" for k in classes) + "        y      se")
    for r in c["rows"]:
        shares = " ".join(f"{r['counts'].get(k, 0) / r['n']:11.4f}" for k in classes)
        lines.append(f"  {r['x']:<6g} {r['n']:<6d} {shares}  {r['y']:.4f} {r['se']:.4f}")
    lines.append(f"SLOPE {_fmt(c['slope'])} per point of difference ({len(c['rows'])} bins read)")
    lines.append(f"SPREAD range={_fmt(c['range'])} sd={_fmt(c['sd'])}")
    lines.append(f"MONOTONE {'n/a' if c['monotone'] is None else ('yes' if c['monotone'] else 'no')}")
    d = c["dominant"]
    lines.append("DOMINANT n/a" if d is None else f"DOMINANT {d[0]:.4f} at x={d[1]:g} ({d[2]})")
    return lines


def _read(pairs_iter, classes: tuple, outcome_of: Callable, carried: Callable, which: tuple, min_bin: int,
          title: str) -> list:
    """One contest's pairs binned by every difference in `which`, rendered. `all` prints a SLOPE per key only."""
    accs = {name: {} for name in which}
    pops = {name: Counter() for name in which}
    seen = Counter()
    for p in pairs_iter:
        o = outcome_of(p)
        seen[o] += 1
        for name, d in _diffs(p, which).items():
            idx = _bin(d, _width(name))
            accs[name].setdefault(idx, Counter())[o] += 1
            pops[name][idx] += 1
    classes = tuple(k for k in classes if k in seen) or classes
    out = []
    if len(which) == 1:
        name = which[0]
        return _render(title, classes, pops[name], curve(accs[name], _width(name), min_bin, carried), _width(name),
                       min_bin, name)
    out.append(f"{title} diff=all bin=1 min-bin={min_bin}")
    for name in which:
        c = curve(accs[name], _width(name), min_bin, carried)
        out.append(f"SLOPE {name} {_fmt(c['slope'])} ({len(c['rows'])} bins read)")
    return out


def _which(diff: str) -> tuple:
    if diff == "all":
        return tuple(ATTRIBUTES)
    if diff in ("sheet", "read") or diff in ATTRIBUTES:
        return (diff,)
    raise SystemExit(f"--diff {diff!r}: expected sheet, read, all or one of {', '.join(ATTRIBUTES)}")


def _duel_outcome(p) -> str:
    return "undecided" if p.winner is None else f"{p.winner}_wins"


def duel_report(seed: int, n: int, terms: str, diff: str, min_bin: int) -> list:
    return _read(duel_pairs(seed, n, terms), DUEL_OUTCOMES, _duel_outcome, lambda c: c["a_wins"], _which(diff), min_bin,
                 f"duel terms={terms} seed={seed} n={n}")


def social_report(seed: int, n: int, verb: str, diff: str, min_bin: int) -> list:
    return _read(social_pairs(seed, n, verb), BANDS + (REFUSED,), lambda p: p.band,
                 lambda c: sum(c[b] for b in CARRIED), _which(diff), min_bin, f"social verb={verb} seed={seed} n={n}")


def main(argv: Optional[list] = None) -> int:
    ap = argparse.ArgumentParser(prog="python -m engine.season.harness.pairs", description=(
        "Outcome by attribute difference over generated random pairs: the curve, its SLOPE (least-squares, count-weighted), "
        "its SPREAD, MONOTONE and DOMINANT. A reading, not a gate."))
    ap.add_argument("contest", choices=("duel", "social"))
    ap.add_argument("--terms", nargs="+", default=None, help="duel terms (default: every term the combat module deals)")
    ap.add_argument("--verb", default="argue", help="the social verb (default argue)")
    ap.add_argument("--n", type=int, default=None, help=f"pairs per seed ({DEFAULT_N})")
    ap.add_argument("--seed", type=int, nargs="+", default=[0])
    ap.add_argument("--diff", default=None, help="sheet | read | <registry key> | all (duel: sheet; social: read)")
    ap.add_argument("--min-bin", type=int, default=DEFAULT_MIN_BIN)
    args = ap.parse_args(argv)
    n = args.n if args.n is not None else DEFAULT_N[args.contest]
    diff = args.diff or ("sheet" if args.contest == "duel" else "read")
    if args.contest == "duel":
        known = tuple(combat.engine()[0].DUEL_TERMS)
        terms = tuple(args.terms) if args.terms else known
        for t in terms:
            if t not in known:
                raise SystemExit(f"--terms {t!r}: the combat module deals {known}")
        jobs = [lambda s=s, t=t: duel_report(s, n, t, diff, args.min_bin) for s in args.seed for t in terms]
    else:
        jobs = [lambda s=s: social_report(s, n, args.verb, diff, args.min_bin) for s in args.seed]
    for job in jobs:
        print("\n".join(job()))
        print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
