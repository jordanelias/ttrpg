"""B05.22 -- THE CALIBRATION TARGETS AS A TEST (`proposals/13_SC_calibration.md` §1, §2, §4, exact edit 1; OBS §4 step 4, gate 4; C3-N6).

WHAT IT IS. A behaviour test over the shipped fixtures: it builds the grid of CAL §2 -- skill scores 0, 2, 4, 7, "equals" being equal skill
rank (A-79) -- by composing each cell's record from `Fixtures` through the host's own operand readers (`sigma.OBSTACLE_TERMS`,
`sigma.advantage_sigma`, `pool.pool_pair`), handing it to the module's `obstacle` (`modules/social_contest/roll.py::obstacle`, reached by
its composition row as the host reaches it) and reading the odds on the closed form of the one sampler (`sigma_leverage.record_odds`).
Exact odds, never sampled. It READS the tables; it sets nothing, so a value moved in `data/fixtures.py` that breaks a target fails here first.

THE TARGETS ARE DESIGN TARGETS, STATED ONCE (`TARGET`, below); Jordan may move any of them by one edit there. This file asserts C1 to C8
(`U3` §1 item 6's gate); C9 and C10 are 29_DICE 29-4's tests, written by the second half's 29-4 item, so the floor of checked cells here is
`4 ranks x 8 targets` (`CLAUDE.md` §0.1 pt 2).

THE VALUES THIS GRID CHOOSES, because the composer wants them and CAL §2 (written before B05.14 / B05.25) did not:
  * `ATTRIBUTE`: the actor's governing attribute and the opponent's OPPOSING attribute (A-79, A-137) are BOTH the scale's mid-point
    (`pool.attribute_midpoint()`: 4 on 1-7, "neither above nor below: zero levels either way"). The pool is
    `pool_of(ATTRIBUTE + rank, 0, pool_add, pool_floor)` (B05.25: the verb's governing score plus the rank); the opposition operand is
    `rank + ATTRIBUTE` read at `opposition_rate`. So "equals" is equal attribute AND equal rank, and the reference cell is a plain room
    (`reception` 0), neutral regard (`None`), no evidence (`proofs` 0), no stakes, no effort (0 levels). CAL's "pools 6, 8, 10, 13 under A-6" are
    NOT these pools: they were `rank + 6` before the governing attribute entered the pool.
  * the opponent's skill score is the grid's rank as written, 0 included (the host's `pool.score` floors an opponent's at the untrained score,
    `pool_default`; the grid reads CAL's scores, which is the whole of "equals at rank 0").
  * C3 reads an opponent four ranks BETTER than the actor at every grid rank (the opponent's rank is then 4, 6, 8, 11; the composer takes any
    score); C4 an opponent four ranks WORSE at the ranks that have four to give (4 and 7: rank 0 and 2 have no opponent four ranks worse).
  * C5's "one full unit of favour" is read by BOTH routes the target names: T3 at the clamp (a counterparty at stance +1: `regard` +1.0) and a room
    of reception +1; each must clear it.
  * C6 reads an unopposed act at `routine` (the level the inquiries and the self-plea ship at, T13 edit 7) at the grid's two LOWEST pools (ranks 0
    and 2), the nearest this grid has to CAL's "pool 2-4" [ASSUMPTION: copied as CAL §2 states it, not re-solved; B05.23's reader records it].
  * C8 reads, at every grid rank at `routine`, equals: the four levels (3 adjacent pairs), the rooms reception -2 / -1 / 0 / +1 (3 pairs) and the
    regard values -1 / 0 / +1 (2 pairs). Reception +2 is NOT read: two favour units sit past the soft cap's knee, which CAL §3 step 3 says is
    reported, not tuned away.
  * C7 reads every cell any other row read: P(F) <= 0.90 (so P(Partial or better) >= 0.10), P(F) at or above the `OB_MIN` floor's own, and both
    tails open (0 < P(F) < 1, the standing rule). An S27.4-refused cell (`ob > multiple x pool`: no dice dealt) is read as P(F) = 1.

THE REALM READ (OBS gate 4) was `test_every_rolled_verb_with_five_rolls_shows_more_than_two_obstacles` (retired): `Margin.terms` off the
Event's `ending` (B05.18) over `build_realm(0..2)`, one season each.
"""
from __future__ import annotations

import functools
from typing import NamedTuple, Optional

import pytest

from engine.dice_engine.sigma_leverage import OB_MIN, band_odds, net_boost, pool_of, record_odds

from ..data.fixtures import DEFAULT_FIXTURES, DIFFICULTY_OB_ARMS
from ..data.rosters import roster
from ..queries.inputs import SocialContestInput
from ..seam.wrappers import pool, sigma
from .test_sc01_obstacle_ceiling import _module

# ---------------------------------------------------------------------------------------------------------------------
# THE TARGETS, STATED ONCE (CAL §2). Jordan moves one by editing it here.
# ---------------------------------------------------------------------------------------------------------------------
TARGET = {
    "C1_F": (0.50, 0.65),          # equals, `routine`: P(Failure)
    "C1_S": (0.15, 0.30),          # equals, `routine`: P(Success or better)
    "C2_STEP": (0.05, 0.20),       # each difficulty step at equals: the rise in P(Failure)
    "C3_F": (0.75, 0.90),          # overmatched (an opponent four ranks better), `routine`: P(Failure)
    "C4_F_MAX": 0.45,              # underdog opponent (four ranks worse), `routine`: P(Failure) at most
    "C5_DELTA_MIN": 0.12,          # one full unit of favour at equals, `routine`: the fall in P(Failure) at least
    "C6_F": (0.25, 0.60),          # unopposed act at its row's level: P(Failure)
    "C7_F_MAX": 0.90,              # every calibrated cell: P(Failure) at most (so P(Partial or better) >= 0.10, the chance floor)
    "C8_APART": 0.03,              # adjacent levels / rooms / regard values: P(Failure) at least this far apart
}
C7_PARTIAL_OR_BETTER_MIN = 0.10    # the same line from the other side: P(Partial or better) at least
RANKS = (0, 2, 4, 7)               # the grid's skill scores (CAL §2)
ATTRIBUTE = pool.attribute_midpoint()          # the actor's governing attribute and the opponent's opposing attribute (see the head)
LEVELS = tuple(roster("difficulty_levels", ordered=True))
RECEPTIONS = (-2.0, -1.0, 0.0, 1.0)            # C8's rooms, one unit apart (the bench's signed regard for the actor)
REGARDS = (-1.0, 0.0, 1.0)                     # C8's regard values: the counterparty's stance in the clamp unit, hostile .. favourable
FLOOR_OF_CELLS = len(RANKS) * 8                # CLAUDE.md §0.1 pt 2: `>= 4 ranks x 8 targets`
TARGETS = ("C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8")


def _arm(**sweeps):
    """`DEFAULT_FIXTURES` with `sweeps` applied (`Fixtures.sweep` returns a NEW one; the shared singleton is never written)."""
    fx = DEFAULT_FIXTURES
    for name, value in sweeps.items():
        fx = fx.sweep(name, value)
    return fx


#: The control arm, pinned EXPLICITLY so the falsifier below holds whatever ships: the base 0, no floor, the rate 0.5, the sizes 0/1/2/3, and the
#: tables B05.23 flipped at their controls (`regard_step` 0, `proof_admission` off, `attribute_level` None) and the ceiling's form at its control
#: (`hard`, B05.53), every one of them named here.
CONTROL = dict(pool_add=0, pool_floor=0, opposition_rate=0.5, difficulty_ob=DIFFICULTY_OB_ARMS["control"], regard_step=0, proof_admission="off",
               attribute_level=None, ceiling_form="hard")


# ---------------------------------------------------------------------------------------------------------------------
# the instrument: one cell's record -> the module's obstacle -> the closed-form odds
# ---------------------------------------------------------------------------------------------------------------------
class Cell(NamedTuple):
    label: str
    rank: int
    pool: float
    ob: float
    leverage: float
    bands: tuple          # (F, P, S, O) -- the owner's order
    terms: tuple
    refused: bool

    @property
    def f(self) -> float:
        return self.bands[0]

    @property
    def success_or_better(self) -> float:
        return self.bands[2] + self.bands[3]


def _cell(fx, label: str, *, rank: int, level: str = "routine", opposed_rank: Optional[int] = None, opposed: bool = True,
          reception: float = 0.0, regard: Optional[float] = None) -> Cell:
    """One cell of the grid. `opposed_rank` is the opponent's skill score (default: the actor's, i.e. equals); `opposed=False` is an unopposed act
    (a docket item, a self-plea: no person opposite, the module opposes at `pool_default`)."""
    add, floor = pool.pool_pair(fx)
    pool_ = pool_of(ATTRIBUTE + rank, 0, add, floor)
    opposition = None
    if opposed:
        opposition = (rank if opposed_rank is None else opposed_rank) + ATTRIBUTE         # his skill score + his opposing attribute (A-137)
    facts = {"verb": "", "opposition": opposition, "circumstance": (), "reception": reception, "docketed": None, "heard": reception != 0.0,
             "regard": regard}
    fields: dict = {}
    operands: list = []
    for name, read in sigma.OBSTACLE_TERMS.items():
        if name in ("difficulty", "stakes"):          # difficulty: the LEVEL below; stakes: the reference cell has none (no verb, no tenure opened)
            continue
        got = dict(read(fx, facts))
        operands.extend(got.pop("obstacle_operands", ()))
        fields.update(got)
    leverage = sigma.advantage_sigma(fx, {sigma.EFFORT: 0, sigma.EDGE: (), "proofs": 0.0, "reception": reception, sigma.OFFICE: None,
                                          "regard": regard})
    inp = SocialContestInput(pool=pool_, obstacle_ceiling=fx.get("obstacle_ceiling"), ceiling_per_pool=fx.get("ceiling_per_pool"), ceiling_form=fx.get("ceiling_form"),
                             obstacle_refusal_multiple=fx.get("obstacle_refusal_multiple"), leverage=leverage,
                             difficulty=float(fx.get("difficulty_ob")[level]), reception=reception, reception_gain=fx.get("reception_gain"),
                             **{**fields, "obstacle_operands": tuple(operands)})
    ob, terms = _module().obstacle(inp)
    refused = ob > inp.obstacle_refusal_multiple * max(inp.pool, 0)                      # S27.4: no dice dealt (`sigma.resolve`)
    bands = (1.0, 0.0, 0.0, 0.0) if refused else record_odds(inp.pool, ob, inp.leverage)
    return Cell(label, rank, float(inp.pool), ob, leverage, bands, terms, refused)


class Row(NamedTuple):
    target: str           # "C1" .. "C8"
    rank: int             # the actor's skill score
    cell: str             # which cell
    ok: bool
    reading: str          # what was read, for the failure message and the commit body


# ---------------------------------------------------------------------------------------------------------------------
# the checks: pure over numbers, so a planted value can show each one sees its failure
# ---------------------------------------------------------------------------------------------------------------------
def check_c1(f: float, s: float) -> bool:
    return TARGET["C1_F"][0] <= f <= TARGET["C1_F"][1] and TARGET["C1_S"][0] <= s <= TARGET["C1_S"][1]


def check_c2(step: float) -> bool:
    return TARGET["C2_STEP"][0] <= step <= TARGET["C2_STEP"][1]


def check_c3(f: float) -> bool:
    return TARGET["C3_F"][0] <= f <= TARGET["C3_F"][1]


def check_c4(f: float) -> bool:
    return f <= TARGET["C4_F_MAX"]


def check_c5(delta: float) -> bool:
    return delta >= TARGET["C5_DELTA_MIN"]


def check_c6(f: float) -> bool:
    return TARGET["C6_F"][0] <= f <= TARGET["C6_F"][1]


def check_c7(f: float, floor_f: float) -> bool:
    return f <= TARGET["C7_F_MAX"] and (1.0 - f) >= C7_PARTIAL_OR_BETTER_MIN and f >= floor_f - 1e-12 and 0.0 < f < 1.0


def check_c8(a: float, b: float) -> bool:
    return abs(a - b) >= TARGET["C8_APART"]


def grid(fx) -> list:
    """Every row of C1 to C8 over the fixtures `fx`: `list[Row]`."""
    rows: list = []
    cells: list = []                          # every cell read, for C7

    def read(cell: Cell) -> Cell:
        cells.append(cell)
        return cell

    for rank in RANKS:
        by_level = {lv: read(_cell(fx, f"equals {lv}", rank=rank, level=lv)) for lv in LEVELS}
        base = by_level["routine"]
        # C1
        rows.append(Row("C1", rank, "equals routine", check_c1(base.f, base.success_or_better),
                        f"P(F) {base.f:.4f} in {TARGET['C1_F']}, P(S+) {base.success_or_better:.4f} in {TARGET['C1_S']}"))
        # C2: each difficulty step at equals
        for lo, hi in zip(LEVELS, LEVELS[1:]):
            step = by_level[hi].f - by_level[lo].f
            rows.append(Row("C2", rank, f"{lo}->{hi}", check_c2(step),
                            f"dP(F) {step:+.4f} in {TARGET['C2_STEP']} (P(F) {by_level[lo].f:.4f} -> {by_level[hi].f:.4f})"))
        # C3: an opponent four ranks better
        over = read(_cell(fx, "overmatched routine", rank=rank, opposed_rank=rank + 4))
        rows.append(Row("C3", rank, f"opponent rank {rank + 4} routine", check_c3(over.f), f"P(F) {over.f:.4f} in {TARGET['C3_F']}"))
        # C4: an opponent four ranks worse, where there are four to give
        if rank >= 4:
            under = read(_cell(fx, "underdog routine", rank=rank, opposed_rank=rank - 4))
            rows.append(Row("C4", rank, f"opponent rank {rank - 4} routine", check_c4(under.f), f"P(F) {under.f:.4f} <= {TARGET['C4_F_MAX']}"))
        # C5: one full unit of favour at equals, routine, by both routes
        for route, kw in (("regard +1 (T3 at the clamp)", dict(regard=1.0)), ("reception +1 (a friendly room)", dict(reception=1.0))):
            favoured = read(_cell(fx, f"favour: {route}", rank=rank, **kw))
            delta = base.f - favoured.f
            rows.append(Row("C5", rank, route, check_c5(delta),
                            f"dP(F) {delta:+.4f} >= {TARGET['C5_DELTA_MIN']} (P(F) {base.f:.4f} -> {favoured.f:.4f}, leverage {favoured.leverage:+.3f})"))
        # C6: an unopposed act at its row's level, at the grid's two lowest pools
        if rank in RANKS[:2]:
            alone = read(_cell(fx, "unopposed routine", rank=rank, opposed=False))
            rows.append(Row("C6", rank, "unopposed routine", check_c6(alone.f), f"P(F) {alone.f:.4f} in {TARGET['C6_F']} (pool {alone.pool:g})"))
        # C8: adjacent levels, rooms and regard values one unit apart, at equals, routine
        for lo, hi in zip(LEVELS, LEVELS[1:]):
            rows.append(Row("C8", rank, f"levels {lo}/{hi}", check_c8(by_level[lo].f, by_level[hi].f),
                            f"P(F) {by_level[lo].f:.4f} vs {by_level[hi].f:.4f}, apart {abs(by_level[hi].f - by_level[lo].f):.4f} >= {TARGET['C8_APART']}"))
        rooms = [read(_cell(fx, f"room {r:+g}", rank=rank, reception=r)) for r in RECEPTIONS]
        for (ra, ca), (rb, cb) in zip(zip(RECEPTIONS, rooms), zip(RECEPTIONS[1:], rooms[1:])):
            rows.append(Row("C8", rank, f"rooms {ra:+g}/{rb:+g}", check_c8(ca.f, cb.f),
                            f"P(F) {ca.f:.4f} vs {cb.f:.4f}, apart {abs(cb.f - ca.f):.4f} >= {TARGET['C8_APART']}"))
        regards = [read(_cell(fx, f"regard {r:+g}", rank=rank, regard=r)) for r in REGARDS]
        for (ra, ca), (rb, cb) in zip(zip(REGARDS, regards), zip(REGARDS[1:], regards[1:])):
            rows.append(Row("C8", rank, f"regard {ra:+g}/{rb:+g}", check_c8(ca.f, cb.f),
                            f"P(F) {ca.f:.4f} vs {cb.f:.4f}, apart {abs(cb.f - ca.f):.4f} >= {TARGET['C8_APART']}"))
    # C7: every cell read above
    for c in cells:
        floor_f = band_odds(c.pool, OB_MIN, net_boost(c.leverage, c.pool))[0]
        rows.append(Row("C7", c.rank, c.label, check_c7(c.f, floor_f),
                        f"P(F) {c.f:.4f} (<= {TARGET['C7_F_MAX']}, > 0, < 1; floor's own {floor_f:.4f}; ob {c.ob:.3f} pool {c.pool:g}"
                        f"{', REFUSED' if c.refused else ''})"))
    return rows


@functools.lru_cache(maxsize=None)
def _rows(arm: str) -> tuple:
    """The grid over a named arm: `shipped` (`DEFAULT_FIXTURES` as it stands)."""
    fx = {"shipped": DEFAULT_FIXTURES}[arm]
    return tuple(grid(fx))


def _red(rows, target: str) -> list:
    return [r for r in rows if r.target == target and not r.ok]


def _quote(rows: list) -> str:
    return "\n".join(f"  {r.target} rank {r.rank:>2} {r.cell}: {r.reading}" for r in rows)


# ---------------------------------------------------------------------------------------------------------------------
# the targets, one test per row of CAL §2 against the SHIPPED fixtures
# ---------------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("target", TARGETS)
def test_target_reads_green_at_the_shipped_fixtures(target):
    """Each target of CAL §2 against `DEFAULT_FIXTURES`. RED on C1 and C8 at the control arm (the reason for T13 commit 2), green at the calibrated one."""
    rows = _rows("shipped")
    checked = [r for r in rows if r.target == target]
    assert checked, f"{target} read no cell"
    bad = _red(rows, target)
    assert not bad, f"{target}: {len(bad)} of {len(checked)} cells red at the shipped fixtures\n{_quote(bad)}"


def test_the_grid_checked_at_least_four_ranks_by_eight_targets_cells():
    """CLAUDE.md §0.1 pt 2: a loop that asserts conditionally asserts that it asserted. Every target read a cell; C1, C2, C3, C5, C7 and C8 read every rank."""
    rows = _rows("shipped")
    checked = len(rows)
    assert checked >= FLOOR_OF_CELLS, checked
    assert {r.target for r in rows} == set(TARGETS)
    for target in ("C1", "C2", "C3", "C5", "C8"):
        assert {r.rank for r in rows if r.target == target} == set(RANKS), target
    assert {r.rank for r in rows if r.target == "C4"} == {4, 7}
    assert {r.rank for r in rows if r.target == "C6"} == set(RANKS[:2])


# ---------------------------------------------------------------------------------------------------------------------
# B05.59 -- THE BETTER ARGUER WINS ON THE FIGHT'S CURVE (`29_DICE` item 29-4 step 6; gate 6). Read on the same composed cells as the grid above.
# `ORDER_WINDOWS` are the source's TARGETS, copied (the fight's windows, deliberately the same); a reading outside one fails and is named, and no
# window, fixture or ladder is moved here to make it pass. C3 and C4 restated on ranks are NOT written again: the grid's C3 (an opponent four ranks
# better, every rank) and C4 (four ranks worse, ranks 4 and 7) rows above are those readings.
# ---------------------------------------------------------------------------------------------------------------------
DECIDED_LEVEL = "routine"                 # the grid's reference cell (the level C1, C3 and C4 read at)
#: (better rank, worse rank, window of the better arguer's share of decided exchanges): +1, +2 and +4 ranks, two pairs each
ORDER_WINDOWS = ((3, 2, (0.60, 0.70)), (6, 5, (0.60, 0.70)), (4, 2, (0.72, 0.82)), (7, 5, (0.72, 0.82)), (6, 2, (0.88, 0.95)), (7, 3, (0.88, 0.95)))


def test_one_minor_level_against_moves_failure_by_five_points():
    """Gate 6's one-level arm: at equals, `routine`, every grid rank, one `minor` level of leverage AGAINST the actor (`LEVEL_SIGMA["minor"]`, a
    -σ on the roll's boost) raises P(Failure) by at least 0.05, read from `band_odds` on the composed cell's own pool and obstacle."""
    from engine.dice_engine.sigma_leverage import LEVEL_SIGMA
    checked = 0
    for rank in RANKS:
        cell = _cell(DEFAULT_FIXTURES, "equals", rank=rank)
        against = band_odds(cell.pool, cell.ob, net_boost(-LEVEL_SIGMA["minor"], cell.pool))[0]
        assert against - cell.f >= 0.05, (rank, cell.f, against)
        checked += 1
    assert checked == len(RANKS)


# ---------------------------------------------------------------------------------------------------------------------
# the realm read (CAL §3 step 4; OBS §4 step 4 and gate 4): `Margin.terms` off the Event's `ending` (B05.18), `build_realm(0..2)`, one season each
# ---------------------------------------------------------------------------------------------------------------------
REALM_SEEDS = (0, 1, 2)

