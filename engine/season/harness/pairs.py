"""THE RANDOM-PAIRS INSTRUMENT (B01a.04; Jordan 2026-11-13/14, rulings (4) and (5)): a contest's outcome by attribute
difference, read over generated random pairs at a very high iteration count, as a CURVE -- never one even-matchup
number. A-79's even centres are the curve's middle bin.

    python -m engine.season.harness.pairs {duel,social,proceeding} [--terms yield blood death] [--verb examine] [--n N]
                                          [--seed S ...] [--diff sheet|read|<registry key>|all] [--min-bin 200]
    python -m engine.season.harness.pairs proceeding [--type conversation] [--form full|abridged] [--side for|against|decider]
                                          [--room none|gallery|crowd] [--off <setting>]

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

THE DIFFERENCE `d`. `sheet` (the duel's default): the mean over the ten keys of `a[k] - b[k]`, bins of 0.5. ⚠ The duel reads six
keys (`modules/combat/attributes.py`) and the realm's `score` is the larger of an attribute and a capability (`pool.py`),
so `sheet`'s slope is diluted by the four keys the duel never reads and is not the realm's; `all` names the keys read, and
a calibration target is set on those (B05.24/B05.25 change which keys a contest reads). `read` (the
social roll's default): the record's `pool` minus its `opposition` (for a duel, the two parties' `scores + addends`, one minus the other; an
opposition `None` reads as `pool_default`, the untrained score the obstacle opposes it at), read off the input so the instrument follows whatever the governing
score becomes, bins of 1. A registry key: `a[k] - b[k]`, bins of 1. `all` prints one SLOPE per key (a slope near 0 names
a key the contest does not read). Bins are rounded half up, `floor(x / width + 0.5)`; the tree's public `round_half_up`
is B38.55's, and this exact local one is replaced by it then (`modules/mass_battle/massbattle.py` holds a private one, not
imported across the module boundary).

WHAT IS PRINTED, per contest and seed. `POPULATION`: the pairs per bin. Per bin with at least `--min-bin` pairs: its
count, the share of each outcome, `y` and its binomial standard error `sqrt(y (1 - y) / n)`.
  SLOPE     the least-squares slope of `y` on the bin centre `x`, weighted by the bin's pair count:
            `sum n_b (x_b - xbar)(y_b - ybar) / sum n_b (x_b - xbar)^2`, `xbar` and `ybar` the count-weighted means.
            It is the change in the curve per point of difference. Printed with its standard error and the window it
            was read over, `SLOPE b +/- se per point of difference (k bins read, x from lo to hi)`: which bins clear
            `--min-bin` depends on `--n`, so a slope is only comparable with another read over the same window.
            THE STANDARD ERROR. `sum n_b (x_b - xbar) = 0`, so the slope is `sum n_b (x_b - xbar) y_b / Sxx` with
            `Sxx = sum n_b (x_b - xbar)^2`: a fixed linear combination of the bin shares once the bins' centres and
            counts are given. Each `y_b` is a binomial share of `n_b` independent pairs (every pair has its own keyed
            stream), `Var(y_b) = p_b (1 - p_b) / n_b`, and the bins are independent, so
            `Var(slope) = sum n_b^2 (x_b - xbar)^2 p_b (1 - p_b) / n_b / Sxx^2`; with `y_b` for `p_b`,
                `se = sqrt(sum n_b (x_b - xbar)^2 y_b (1 - y_b)) / Sxx`.
            Conditional on the bin counts, and it measures sampling noise only, not whether a line fits the curve. A
            bin at `y` 0 or 1 adds no variance, so a window of saturated bins understates it.
  SPREAD   the range `max y_b - min y_b` and the count-weighted standard deviation of `y_b` about `ybar`.
  MONOTONE  `yes` when each bin's `y` is at or above its left neighbour's less two standard errors of their
            difference, `sqrt(se_b^2 + se_left^2)`; else `no`.
  DOMINANT  the largest single outcome share in any bin, with its bin: ruling (4)'s "no bin dominant above a stated
            share" read as one outcome's share of a bin's pairs (UNDECIDED (5)); the stated share is the caller's.

`slope` and `spread` are meant in their ordinary statistical sense; this is no check and no gate (it is a reading).

`proceeding` (B24p.17; V2 p3 §B's readings, INT E-18) the same world and sheets, the proceeding in place of the single roll. Per pair
`proceeding_pairs` seats three persons by the sheets `social` draws (`a` = `p_low`, the bearer and the `for` side; `b` = `p_mid`, the party
addressed; `c` = `p_high`, who holds the Duke's seat and sits where the row's authority seats one) and the room's onlookers, then runs
the act as the host runs it (`sigma._resolve_proceeding`: `proceeding_input` on the row, or `abridged(row)` for `--form abridged`, the
entry the composition row `social_contest.proceeding` names -- never `roll` -- `act_band`, and S27.4 on an `exchange` close), the stream
`draw(f"pair{i}", f"pairs:proceeding:{type_id}:{form}")`. `y` is the share of CARRIED bands as `social`'s; the other classes are the
ladder's bands, `Refused` and `Impasse` (a `consent` sitting nobody accepted). `read` is the act's own margin, `net - ob`, `0` where there is none.
  `--type`  an arrangement id (default `conversation`). A row whose authority seats nobody at the instrument's venue (`inquisition_hearing`,
            `excommunication_deliberation`: a church) refuses in its full form (`refused[no_seat]`); nothing here seats a church.
  `--form`  `abridged` (default; one speech weighed by the one addressed) or `full`.
  `--room`  the onlookers seated at the venue: `none` 0, `gallery` 2, `crowd` one cohort of weight 30. The row's own floor decides whether
            they watch (`closed` seats none, however many stand there).
  `--side`  whose sheet the difference `d` is taken on: `for` `a - b` (the default), `against` `b - a`, `decider` the first person the card
            seats to decide, less the scale's mid-point (an adjudicator has no opposite number; the shift does not move a slope).
  `--off`   one setting of the proceeding's own at its control (`OFF`: `None` for a level, else 0), for an operand's own arm.
  Three lines follow the curve: `EXCHANGES` (the mean count of beats), `ENDS` (the share of each `proceeding_ends` member) and
  `RATTLES` (the beats that rattled someone, per sitting).

DEFAULTS AND TIMING. ⚠ A MEASUREMENT ON ONE MACHINE, not a property of the instrument: every figure in this paragraph
was read once, on the producer's container, 2026-11-14, and another host or a later tree reads others. With the shell's
`time`, `--n 1000` wall seconds, of which 0.62 s is importing the package: duel `yield` 2.26, `blood` 2.04, `death` 2.88; `social` 1.20. The cost per
1,000 pairs once warm, from longer runs: `death` 1.7 s (`--n 5000`: 9.3 s wall) and `social` 0.25 s (`--n 20000`: 5.6 s
wall; the 200,000 default is about 50 s). So the defaults, `--n` 20,000 per duel terms (about 35 to 55 s) and 200,000 for
`social`, each cost under the two minutes a contest the item allows, and none was lowered. (The drafting lane's scratch
reading, on fighters at 3 on every key, was 1.1 / 0.7 / 1.9 s per 1,000 duels and 0.015 s per 1,000 social rolls: a
comparison, not a target. The social figure here includes building the record, `contest_input`, which that reading did not.)

PROCEEDING'S DEFAULT `--n` (B24p.17). ⚠ A MEASUREMENT ON ONE MACHINE, 2026-11-23, the producer's container, tree `b8db4f5` plus this item (`--room none`
and `crowd` read alike): warm seconds per 1,000 pairs (`--n` 22,000 abridged; 1,500 to 6,000 full), nine tenths of it the module's own `proceed`, the
host's build and card the rest. ABRIDGED 0.60 to 0.83 in every row (`conversation` 0.66). FULL by row: `rally` 0.7 to 0.9; `negotiation`, `conversation`,
`interrogation` and `audience` 1.1 to 1.4; `council_of_state` and `parliamentary_debate` 2.0 to 2.3; `examination` 2.9 to 3.2; `arbitration`, `legal_trial`
and `tribunal` 3.4 to 3.7 (the slowest: two to five turns of both sides before a bench). The two church rows refuse in full (`refused[no_seat]`:
nothing here seats a church). The two minutes a contest the item allows is held for the SLOWEST row: abridged 0.83 x 100,000 = 83 s; full 3.7 x 25,000
= 93 s (the dialogue rows 28 to 35 s). The plan's 200,000 and 40,000 [ASSUMPTION, from `social`'s 0.25 s per 1,000 and `DRAWS_PER_EXCHANGE`] would read
120 to 166 s abridged and 136 to 148 s full on the three slowest rows, so the defaults are halved and cut to 100,000 and 25,000. `--n` is the caller's.
"""
from __future__ import annotations

import argparse
import dataclasses
import importlib
import math
from engine.dice_engine import fmath
import sys
from collections import Counter, namedtuple
from typing import Callable, Optional

from engine.dice_engine.dice_engine import DEGREE_LABEL, DEGREE_ORDINAL, Degree
from engine.substrate import composition
from engine.substrate.descriptors import ATTRIBUTES

from ..data.arrangements import ARRANGEMENTS
from ..data.fixtures import DEFAULT_FIXTURES
from ..data.rosters import PROCEEDING_ENDS
from ..loop.driver import SeasonDriver
from ..seam.ladder import degree_of
from ..seam.wrappers import combat, sigma
from ..seam.wrappers._entry import entry_for
from ..seam.wrappers.pool import attribute_midpoint
from ..state.carriers import Person, Rung, Tenure, generated_attributes
from ..state.ids import draw_factory
from . import probes

FIRST, SECOND = "p_low", "p_mid"            # the world's two fighters / speakers (test-fixture ids, `probes.tiny_world`)
# [canonical: engine/season/harness/pairs.py §DEFAULT_N -- an instrument's iteration counts per seed, sized to its wall time (the module docstring's measurement); no game meaning]
DEFAULT_N = {"duel": 20000, "social": 200000,
             "proceeding": {"abridged": 100000, "full": 25000}}   # [JUSTIFIED: instrument default, no game meaning] proceeding: by the form; the docstring's measurement
DEFAULT_MIN_BIN = 200   # [JUSTIFIED: instrument default, no game meaning]
REFUSED = "Refused"                          # S27.4: ob > obstacle_refusal_multiple x pool, no dice dealt (not a band)
# the four bands in the owner's order (`DEGREE_ORDINAL`, the tuple `band_odds` returns), and the two a carried contest reaches
BANDS = tuple(DEGREE_LABEL[d] for d in sorted(DEGREE_ORDINAL, key=DEGREE_ORDINAL.get))
CARRIED = tuple(DEGREE_LABEL[d] for d in (Degree.SUCCESS, Degree.OVERWHELMING))
DUEL_OUTCOMES = ("a_wins", "b_wins", "undecided")
DIFF_WIDTH = {"sheet": 0.5, "read": 1.0}     # [JUSTIFIED: instrument default, no game meaning] a registry key's bin is 1.0

IMPASSE = "Impasse"                          # a `consent` sitting nobody accepted: no margin, no band (`act_band`'s `IMPASSE`)

DuelPair = namedtuple("DuelPair", "i a b read outcome yielder winner")
SocialPair = namedtuple("SocialPair", "i a b read inp band")
ProceedingPair = namedtuple("ProceedingPair", "i a b c read band outcome judge")
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
        # `mortal_keyed=False`: the mortal draw then takes a sub-key of THIS pair's own `Draw` (distinct per pair), not the one host key
        # `(world_seed, tick, pid, "fight.mortal:")` every pair would share; `terms` goes in, so `mortal` reads `mortal_wound_ob[terms]`
        inp = combat.combat_input(w, [FIRST, SECOND], "fight", mortal_keyed=False, terms=terms)
        got = entry.fn(inp, draw(f"pair{i}", f"pairs:duel:{terms}"))
        outcome, yielder = combat.scene_outcome(got, FIRST, SECOND)
        if outcome == "subject_felled" or (outcome == "yielded" and yielder == SECOND):
            winner = "a"
        elif outcome == "actor_felled" or (outcome == "yielded" and yielder == FIRST):
            winner = "b"
        else:
            winner = None
        yield DuelPair(i, a, b, (inp.scores[0] + inp.addends[0]) - (inp.scores[1] + inp.addends[1]), outcome, yielder, winner)


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
            band = degree_of({"net": margin.net, "ob": margin.ob, "settled_margin": margin.net - margin.ob})
        opposition = inp.pool_default if inp.opposition is None else inp.opposition
        yield SocialPair(i, a, b, inp.pool - opposition, inp, band)


# ---------------------------------------------------------------------------------------------------------------
# proceeding (B24p.17)
# ---------------------------------------------------------------------------------------------------------------

VENUE = "Hh"                                 # the hearth where the two speakers stand (`probes.tiny_world`)
THIRD = "p_high"                             # the third person: the Duke, who sits where a row's authority seats one (`probes.tiny_world`)
FORMS = ("abridged", "full")
SIDES = ("for", "against", "decider")
#: the weights of the onlookers each `--room` seats at the venue: none, two, one cohort (weight 30). [JUSTIFIED: instrument default, no game meaning -- B24p.17's `--room`: 0, 2, a cohort of weight 30]
ROOMS = {"none": (), "gallery": (1, 1), "crowd": (30,)}    # [canonical: engine/season/harness/pairs.py §ROOMS -- the onlookers the instrument seats (none, two, one cohort of weight 30); an instrument choice, no game meaning]
#: THE SETTINGS `--off` ACCEPTS: V2 p2 §K's control set (the settings it names a control for; `fixtures.py` ships each at it) and the three
#: B24p.18's control arms switch off besides (`relevance`, `sense_step`, `comfort_step`). Off is `None` for a level and 0 for a step or a gain
#: (`_off_value`); a threshold or a scale at 0 is no control, and is not named here. [ASSUMPTION: a closed set of the instrument's -- basis: V2 p2 §K's control column]
OFF = ("fit_level", "answer_level", "repeat_step", "esteem_step", "off_step", "ploy_step", "grain_strain", "heard_step", "gap_step",
       "weary_step", "awe_step", "room_level", "heckle", "crowd_lean", "start_step", "relevance", "sense_step", "comfort_step")


def _off_value(fx, name: str):
    """A setting at its control: `None` where it is a level, else 0."""
    return None if fx.get(name) is None else 0


def _proceeding_world(room: str, off: Optional[str]):
    """`tiny_world` with the instrument's room at the venue (`Hh`, where `a` and `b` stand): the fixture's stranger leaves (the room is the
    instrument's), the onlookers `ROOMS[room]` names arrive, and `off` is one setting at its control. The driver registers the entries."""
    fx = DEFAULT_FIXTURES
    if off is not None:
        if off not in OFF:
            raise SystemExit(f"--off {off!r}: expected one of {', '.join(OFF)}")
        fx = fx.sweep(off, _off_value(fx, off))
    w = probes.tiny_world(fx)
    for t in w.tenures:
        if t.kind == "contain" and t.object == VENUE and t.subject not in (FIRST, SECOND):      # whoever else stands at the venue leaves
            t.until = 0
    for j, weight in enumerate(ROOMS[room]):
        pid = f"onlook{j}"
        w.persons[pid] = Person(pid, "an onlooker", weight=weight)
        w.rungs[pid] = Rung(pid, "person")
        w.add_tenure(Tenure(f"t_{pid}", pid, VENUE, "contain", since=0))
    SeasonDriver(w)
    return w


def proceeding_pairs(seed: int, n: int, type_id: str, form: str, room: str, off: Optional[str] = None, plant: Plant = None,
                     verb: str = "argue"):
    """Yield one `ProceedingPair(i, a, b, c, read, band, outcome, judge)` per pair `0 .. n-1`. `a`, `b` are drawn as `social_pairs`' (and
    `plant(i, a, b)` replaces them), `c` is `p_high`'s sheet (`pair{i}.c`), the onlookers' `pair{i}.o{j}`; `read` the act's own margin
    (`net - ob`, 0 where there is none); `band` a ladder band, `REFUSED` (S27.4 on an `exchange` close) or `IMPASSE`; `outcome` the
    sitting's `Outcome`; `judge` the sheet of the first person the card seats to decide (`None` where nobody decides: `consent`)."""
    if type_id not in ARRANGEMENTS:
        raise SystemExit(f"--type {type_id!r}: expected one of {', '.join(ARRANGEMENTS)}")
    if form not in FORMS or room not in ROOMS:
        raise SystemExit(f"--form {form!r} / --room {room!r}: expected {FORMS} / {tuple(ROOMS)}")
    w = _proceeding_world(room, off)
    onlookers = [f"onlook{j}" for j in range(len(ROOMS[room]))]
    proceeds = (ARRANGEMENTS[type_id], form, None, None)
    draw = draw_factory(seed, lambda: 0)
    for i in range(n):
        a, b = _sheets(seed, i, plant)
        sheets = {FIRST: a, SECOND: b, THIRD: generated_attributes(seed, f"pair{i}.c", _span()),
                  **{pid: generated_attributes(seed, f"pair{i}.o{j}", _span()) for j, pid in enumerate(onlookers)}}
        for pid, sheet in sheets.items():
            w.persons[pid] = dataclasses.replace(w.persons[pid], attributes=sheet)
        got = sigma._resolve_proceeding(w, [FIRST, SECOND], draw(f"pair{i}", f"pairs:proceeding:{type_id}:{form}"), verb=verb,
                                        subject=SECOND, effort=0, proceeds=proceeds)
        if got["status"] == "REFUSED":
            band, read = REFUSED, 0.0
        elif got["status"] == "IMPASSE":
            band, read = IMPASSE, 0.0
        else:
            band, read = degree_of({k: got[k] for k in ("net", "ob", "settled_margin")}), got["net"] - got["ob"]
        deciders = got["card"].decided_by
        yield ProceedingPair(i, a, b, sheets[THIRD], read, band, got["proceeding"], sheets[deciders[0]] if deciders else None)


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
    out = dict(rows=rows, slope=None, slope_se=None, range=None, sd=None, monotone=None, dominant=None)
    if not rows:
        return out
    total = sum(r["n"] for r in rows)
    xbar = sum(r["n"] * r["x"] for r in rows) / total
    ybar = sum(r["n"] * r["y"] for r in rows) / total
    sxx = sum(r["n"] * (r["x"] - xbar) ** 2 for r in rows)
    out["slope"] = sum(r["n"] * (r["x"] - xbar) * (r["y"] - ybar) for r in rows) / sxx if sxx > 0 else None
    # the slope's binomial standard error (the module docstring derives it)
    out["slope_se"] = (math.sqrt(sum(r["n"] * (r["x"] - xbar) ** 2 * r["y"] * (1 - r["y"]) for r in rows)) / sxx
                       if sxx > 0 else None)
    out["range"] = max(r["y"] for r in rows) - min(r["y"] for r in rows)
    out["sd"] = math.sqrt(sum(r["n"] * (r["y"] - ybar) ** 2 for r in rows) / total)
    out["monotone"] = None if len(rows) < 2 else all(r["y"] >= l["y"] - 2 * fmath.hypot(r["se"], l["se"]) for l, r in zip(rows, rows[1:]))
    out["dominant"] = max(((v / r["n"], r["x"], k) for r in rows for k, v in r["counts"].items()),
                          key=lambda t: (t[0], -t[1], t[2]))
    return out


def _fmt(v: Optional[float], places: int = 4) -> str:
    return "n/a" if v is None else f"{v:.{places}f}"


def _slope_text(c: dict) -> str:
    """`b +/- se ... (k bins read, x from lo to hi)`: the slope, its standard error and the window of bins it was read over."""
    window = (f", x from {c['rows'][0]['x']:g} to {c['rows'][-1]['x']:g}" if c["rows"] else "")
    return f"{_fmt(c['slope'])} +/- {_fmt(c['slope_se'])} per point of difference ({len(c['rows'])} bins read{window})"


def _render(title: str, classes: tuple, population: Counter, c: dict, width: float, min_bin: int, label: str) -> list:
    lines = [f"{title} diff={label} bin={width:g} min-bin={min_bin}",
             "POPULATION " + " ".join(f"{i * width:g}:{population[i]}" for i in sorted(population))]
    lines.append("  x      n      " + " ".join(f"{k:>11}" for k in classes) + "        y      se")
    for r in c["rows"]:
        shares = " ".join(f"{r['counts'].get(k, 0) / r['n']:11.4f}" for k in classes)
        lines.append(f"  {r['x']:<6g} {r['n']:<6d} {shares}  {r['y']:.4f} {r['se']:.4f}")
    lines.append(f"SLOPE {_slope_text(c)}")
    win = (f" (over the {len(c['rows'])} bins read, x from {c['rows'][0]['x']:g} to {c['rows'][-1]['x']:g}; "
           f"a bin under min-bin is left out of all four lines)" if c["rows"] else "")
    lines.append(f"SPREAD range={_fmt(c['range'])} sd={_fmt(c['sd'])}{win}")
    lines.append(f"MONOTONE {'n/a (under two bins)' if c['monotone'] is None else ('yes' if c['monotone'] else 'no')}{win}")
    d = c["dominant"]
    lines.append("DOMINANT n/a" if d is None else f"DOMINANT {d[0]:.4f} at x={d[1]:g} ({d[2]}){win}")
    return lines


def accumulate(pairs_iter, outcome_of: Callable, which: tuple) -> tuple:
    """`(accs, pops, seen)`: per difference in `which`, `{bin index: Counter of outcomes}` (what `curve` reads) and
    `{bin index: pairs}`; and the outcome tally over every pair. The one binning the report and the tests read by."""
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
    return accs, pops, seen


def _read(pairs_iter, classes: tuple, outcome_of: Callable, carried: Callable, which: tuple, min_bin: int,
          title: str) -> list:
    """One contest's pairs binned by every difference in `which`, rendered. `all` prints a SLOPE per key only."""
    accs, pops, seen = accumulate(pairs_iter, outcome_of, which)
    classes = tuple(k for k in classes if k in seen) or classes
    out = []
    if len(which) == 1:
        name = which[0]
        return _render(title, classes, pops[name], curve(accs[name], _width(name), min_bin, carried), _width(name),
                       min_bin, name)
    out.append(f"{title} diff=all bin=1 min-bin={min_bin}")
    for name in which:
        c = curve(accs[name], _width(name), min_bin, carried)
        out.append(f"SLOPE {name} {_slope_text(c)}")
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


def _sided(pairs, side: str):
    """The pairs seen from `side`: `a` and `b` become the two sheets the difference `a[k] - b[k]` is taken on (`for` as drawn; `against`
    swapped; `decider` the judge's, less the scale's mid-point, which no slope sees)."""
    mid = {k: attribute_midpoint() for k in ATTRIBUTES}
    for p in pairs:
        yield p if side == "for" else p._replace(a=p.b, b=p.a) if side == "against" else p._replace(a=p.judge or mid, b=mid)


def proceeding_report(seed: int, n: int, type_id: str, form: str, room: str, side: str, off: Optional[str], diff: str, min_bin: int,
                      verb: str = "argue") -> list:
    """The curve (`_read`) of the carried share by `diff` on the sheet of `side`, then `EXCHANGES`, `ENDS` and `RATTLES` read off the outcomes."""
    tally = dict(sittings=0, beats=0, rattles=0, ends=Counter())

    def seen():
        for p in proceeding_pairs(seed, n, type_id, form, room, off, verb=verb):
            tally["sittings"] += 1
            tally["beats"] += len(p.outcome.beats)
            tally["rattles"] += sum(b.rattled is not None for b in p.outcome.beats)
            tally["ends"][p.outcome.ended] += 1
            yield p
    title = f"proceeding type={type_id} form={form} room={room} side={side}" + (f" off={off}" if off else "") + f" seed={seed} n={n}"
    lines = _read(_sided(seen(), side), BANDS + (REFUSED, IMPASSE), lambda p: p.band, lambda c: sum(c[b] for b in CARRIED),
                  _which(diff), min_bin, title)
    k = max(tally["sittings"], 1)
    ends = [(e, tally["ends"][e]) for e in PROCEEDING_ENDS] + [(e, c) for e, c in tally["ends"].items() if e not in PROCEEDING_ENDS]
    return lines + [f"EXCHANGES {tally['beats'] / k:.4f}", "ENDS " + " ".join(f"{e}={c / k:.4f}" for e, c in ends),
                    f"RATTLES {tally['rattles'] / k:.4f}"]


def main(argv: Optional[list] = None) -> int:
    ap = argparse.ArgumentParser(prog="python -m engine.season.harness.pairs", description=(
        "Outcome by attribute difference over generated random pairs: the curve, its SLOPE (least-squares, count-weighted), "
        "its SPREAD, MONOTONE and DOMINANT. A reading, not a gate."))
    ap.add_argument("contest", choices=("duel", "social", "proceeding"))
    ap.add_argument("--terms", nargs="+", default=None, help="duel terms (default: every term the combat module deals)")
    ap.add_argument("--verb", default="examine", help="the social verb (default examine; `argue`, `tell`, `lie`, `speak` and `interrogate` proceed: read them with `pairs proceeding`)")
    ap.add_argument("--type", default="conversation", help="proceeding: the arrangement id (default conversation)")
    ap.add_argument("--form", choices=FORMS, default="abridged", help="proceeding: abridged (default) or full")
    ap.add_argument("--side", choices=SIDES, default="for", help="proceeding: whose sheet the difference is taken on (default for)")
    ap.add_argument("--room", choices=tuple(ROOMS), default="none", help="proceeding: the onlookers seated: none, gallery (2), crowd (a cohort of 30)")
    ap.add_argument("--off", default=None, help="proceeding: one setting at its control (" + ", ".join(OFF) + ")")
    ap.add_argument("--n", type=int, default=None, help=f"pairs per seed ({DEFAULT_N})")
    ap.add_argument("--seed", type=int, nargs="+", default=[0])
    ap.add_argument("--diff", default=None, help="sheet | read | <registry key> | all (duel: sheet; social: read)")
    ap.add_argument("--min-bin", type=int, default=DEFAULT_MIN_BIN)
    args = ap.parse_args(argv)
    default_n = DEFAULT_N[args.contest]
    n = args.n if args.n is not None else default_n[args.form] if isinstance(default_n, dict) else default_n
    diff = args.diff or ("sheet" if args.contest == "duel" else "read")
    if args.contest == "duel":
        known = tuple(composition.require("combat.duel_terms"))
        terms = tuple(args.terms) if args.terms else known
        for t in terms:
            if t not in known:
                raise SystemExit(f"--terms {t!r}: the combat module deals {known}")
        jobs = [lambda s=s, t=t: duel_report(s, n, t, diff, args.min_bin) for s in args.seed for t in terms]
    elif args.contest == "social":
        jobs = [lambda s=s: social_report(s, n, args.verb, diff, args.min_bin) for s in args.seed]
    else:
        jobs = [lambda s=s: proceeding_report(s, n, args.type, args.form, args.room, args.side, args.off, diff, args.min_bin, args.verb)
                for s in args.seed]
    for job in jobs:
        try:
            print("\n".join(job()))
        except ValueError as refused:           # a row the venue cannot seat (`refused[no_seat]`): said, not a traceback
            if not str(refused).startswith("refused["):
                raise
            raise SystemExit(f"--type {args.type} --form {args.form}: {refused}")
        print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
