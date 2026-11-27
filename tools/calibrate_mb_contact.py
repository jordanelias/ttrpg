#!/usr/bin/env python3
"""Runs the duel engine over a grid of matchups and writes the measured felling chances the mass-battle contact draw reads.

A FELLING CHANCE, `h_k`, is the share of the duel rounds of index `k` that were fought in which one side's man was taken
out of the fight (felled by a blow, or yielding on a failed yield roll). A duel of two fighter types gives both sides'
rows from the same duels. A FIGHTER TYPE is `(arm, armour, skill)`: `arm` is the duel weapon key the troop file's
`arms.<key>.duel_key` (or `sidearm`) names, `armour` one of its `armour_tiers`, `skill` the men's martial skill, passed to
the duel as the `scores` entry (`faculty`'s scale). Every duel is run with the default attributes of
`modules/combat/attributes.py`, under the lethal terms ('death'), round by round through `modules/combat/fight.py::fight_round`
(D-09: `from modules.combat import fight, wrapper`; never `modules/mass_battle`; the module never imports this tool).

WHAT IT READS AND WRITES. The grid is read from `references/troops.yaml` (the distinct duel arms, the `armour_tiers`, `contact.K`)
and the skill levels the grid runs (1, 3, 5; the twelve interpolation check cells run skill 2 and 4 against 3 in light armour, MBA §2.1,
§2.5). The measured table is `references/mb_contact/duel_grid.json` in the schema of MBA §2.3 (round_source, terms, K, seed_rule, cells[]
with duels, outcome, and per side h / h_lo / h_hi / rounds_at_k / flags / damage / felled_mortal); it is written by this tool and never
by hand. `engine_fingerprint()` below is the ONE owner of the duel-engine fingerprint the table records; `tools/export_mb_contact.py`
imports it.

THE MEASURE (MBA §2.2). Per cell one `random.Random(crc32(repr(cell_key)) % 100000)` (no shared stream, so the table does not depend
on `--workers`); duels are position-swapped in halves (even duels put the cell's `a` in the claimant-A slot, odd duels in B); the stop
rule is checked at FIXED duel counts, every 500 duels from 2,000, and never before 2,000; a cell stops when, for each side, the Wilson
95% half-width of `h_1`, `h_2`, `h_3` is at most `max(0.10 x h, 0.002)`; the cap is 20,000 duels, where a side not within it carries the
flag `precision:absolute`; an index with no removal is stored as its Wilson upper bound with the flag `below_resolution:<k>`, never 0;
rounds `k >= 4` are read where at least 400 duels reached round `k`, else `h_k` is the last estimated index's, flagged `carried:<k>`.
Damage is what a side takes per round fought as a fraction of its `health_full` (the tracker's `health_full`, read in the same
`out.wounds` lift as `cumulative_damage`), pooled over the rounds fought. `felled_mortal` is null: the round's result carries no
mortal-wound band.

[ASSUMPTION: a side is taken out by a felling OR by a failed yield roll -- basis: MBA §1.5, "a man who yields in the press is a
casualty"; `h_yield` in each side's row is the yield part of `h`, so the split stays readable; reversible: read `h - h_yield`.]
[ASSUMPTION: a cell whose side-count of wins is 0 for either side is not stopped by the stop rule before the cap, so that a rare
win is given 20,000 duels before the cell is called certain -- basis: MBA §5.2 check 5 calls a cell certain, and a 2,000-duel
zero is not that; at the cap a still-certain cell is left out of the table and printed `CERTAIN <key> ...` to stderr (to be reported to
the PC lane), the run finishes every other cell, and `run` exits 3.]
[ASSUMPTION: the two interpolation mirrors are `arming` light, skill 2 against 2 and 4 against 4 -- basis: MBA §2.1 says "plus two
mirrors" without naming them.]

Usage:
  python tools/calibrate_mb_contact.py run OUT [--workers W] [--cells REGEX]   # write the measured table
  python tools/calibrate_mb_contact.py run --cells REGEX --dry                 # count the cells REGEX selects; run no duel
  python tools/calibrate_mb_contact.py merge OUT IN1 IN2 ... [--complete]      # chunk tables -> one table, the bytes `run` writes
  python tools/calibrate_mb_contact.py --cell KEY N [--table PATH]             # re-derive one cell at N duels, print it
  python tools/calibrate_mb_contact.py --spot M [--table PATH] [--workers W]   # re-run M stored cells, each h_1 inside its interval
  python tools/calibrate_mb_contact.py --trust [--table PATH]                  # the seven checks of MBA §5.2, stop on the first failure
CHUNKING THE GRID. `--cells` is a regex searched in a cell's key text, `arm/armour/skill,arm/armour/skill`, whose first side is the
lower in grid order (arms as `troops.yaml` first names them, then armour tier, then skill), so `^<arm>/<armour>/` selects every cell
whose first side is that arm in that armour: for each arm in (arming, falchion, mace, spear, dagger) and armour in (none, light,
medium, heavy), `^<arm>/<armour>/` is one of 20 chunks that are disjoint and, together, the whole grid (each cell has one first side;
the twelve check cells' first side is a light-armour type, so they fall in the `light` chunks). Run each chunk to its own file
(`run chunk_arming_none.json --cells '^arming/none/' --workers 4`), `run --cells REGEX --dry` for the count, then
`merge duel_grid.json chunk_*.json --complete`: the merged bytes equal one whole `run`'s. Combine chunks as an alternation
(`'^arming/(none|light)/'`) to size them.

KEY is `arm/armour/skill,arm/armour/skill` (either order), e.g. `spear/light/3,arming/light/3`. An instrument, run by hand at a
calibration pass; not a CI check.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import random
import re
import sys
import time
import zlib
from collections import Counter

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TROOPS = os.path.join(REPO, "references", "troops.yaml")
PARAMS = os.path.join(REPO, "engine", "engine_params", "combat_engine_v1.json")
COMBAT_DIR = os.path.join(REPO, "modules", "combat")
TABLE = os.path.join(REPO, "references", "mb_contact", "duel_grid.json")

GRID_SKILLS = (1, 3, 5)          # MBA §2.1: the troop table's span; 2 and 4 are interpolated and checked
CHECK_SKILLS = (2, 4)
CHECK_ARMOUR = "light"
FLOOR_N, STEP_N, CAP_N = 2000, 500, 20000   # MBA §2.2: never before 2,000; checked at fixed counts; the cap
CARRY_MIN = 400                  # MBA §2.2: rounds k >= 4 are read where at least this many duels reached them
Z = 1.96
SEED_RULE = "crc32(repr(cell_key)) % 100000"
ROUND_SOURCE = "modules.combat.fight.fight_round"
TERMS = "death"
SCHEMA = 1
Skill = int


# ---------------------------------------------------------------------------------------------------- the fingerprint
def engine_fingerprint() -> str:
    """THE ONE OWNER of the duel-engine fingerprint: sha256 over `engine/engine_params/combat_engine_v1.json` and then every
    `modules/combat/*.py` in sorted filename order. Byte order: for each file, its repo-relative posix path, one NUL, its raw
    bytes, one NUL. A pure read; no import-time work."""
    h = hashlib.sha256()
    files = [PARAMS] + [os.path.join(COMBAT_DIR, f) for f in sorted(os.listdir(COMBAT_DIR)) if f.endswith(".py")]
    for p in files:
        h.update(os.path.relpath(p, REPO).replace(os.sep, "/").encode() + b"\0")
        with open(p, "rb") as f:
            h.update(f.read())
        h.update(b"\0")
    return h.hexdigest()


# ---------------------------------------------------------------------------------------------------- the grid
class Grid:
    """The grid as `references/troops.yaml` fields it: `arms` in first-appearance order of the effective duel key
    (`duel_key`, else `sidearm`), `armours` its `armour_tiers`, `K` its `contact.K.value`."""

    def __init__(self, troops_path: str = TROOPS):
        import yaml
        with open(troops_path, encoding="utf-8") as f:
            doc = yaml.safe_load(f)
        eff = {name: (a.get("duel_key") or a.get("sidearm")) for name, a in doc["arms"].items()}
        for name, k in eff.items():
            if not k:
                raise ValueError(f"arm {name!r} has neither a duel_key nor a sidearm")
        self.arms = tuple(dict.fromkeys(eff.values()))
        self.armours = tuple(doc["armour_tiers"])
        self.K = int(doc["contact"]["K"]["value"])
        self.types_fielded = set()
        for tname, row in doc["troops"].items():
            if row.get("skill") is None or row.get("armour") is None or row.get("primary") is None:
                continue
            sk = row["skill"]
            if sk not in GRID_SKILLS + CHECK_SKILLS:
                raise ValueError(f"troop {tname!r}: skill {sk!r} is on neither the grid {GRID_SKILLS} nor the check cells {CHECK_SKILLS}")
            if row["armour"] not in self.armours:
                raise ValueError(f"troop {tname!r}: armour {row['armour']!r} is not an armour tier")
            self.types_fielded.add((eff[row["primary"]], row["armour"], sk))
        if CHECK_ARMOUR not in self.armours:
            raise ValueError(f"the interpolation check cells run in {CHECK_ARMOUR!r} armour, which is not a tier")

    def sortkey(self, t: tuple) -> tuple:
        return (self.arms.index(t[0]), self.armours.index(t[1]), t[2])

    def canon(self, t1: tuple, t2: tuple) -> tuple:
        return (t1, t2) if self.sortkey(t1) <= self.sortkey(t2) else (t2, t1)

    def types(self) -> list:
        return sorted(((a, ar, s) for a in self.arms for ar in self.armours for s in GRID_SKILLS), key=self.sortkey)

    def cells(self) -> list:
        """Every cell key in key order: the unordered pairs with mirrors of the fighter types (60 x 61 / 2 = 1,830), then the
        twelve interpolation check cells (skill 2 and 4 against 3, each arm, light armour; plus two mirrors of the first arm)."""
        ts = self.types()
        out = {self.canon(ts[i], ts[j]) for i in range(len(ts)) for j in range(i, len(ts))}
        for arm in self.arms:
            for sk in CHECK_SKILLS:
                out.add(self.canon((arm, CHECK_ARMOUR, sk), (arm, CHECK_ARMOUR, 3)))
        for sk in CHECK_SKILLS:
            out.add(((self.arms[0], CHECK_ARMOUR, sk),) * 2)
        return sorted(out, key=lambda k: (self.sortkey(k[0]), self.sortkey(k[1])))

    def key_text(self, key: tuple) -> str:
        return ",".join("/".join(str(x) for x in t) for t in key)

    def parse_key(self, text: str) -> tuple:
        parts = text.split(",")
        if len(parts) != 2:
            raise ValueError(f"KEY is `arm/armour/skill,arm/armour/skill`, got {text!r}")
        ts = []
        for p in parts:
            arm, armour, skill = p.strip().split("/")
            if arm not in self.arms or armour not in self.armours:
                raise ValueError(f"{p!r}: arm {arm!r} or armour {armour!r} is not on the grid")
            ts.append((arm, armour, int(skill)))
        return self.canon(*ts)


# ---------------------------------------------------------------------------------------------------- the statistics
def wilson(x: int, n: int) -> tuple:
    """The Wilson 95% interval `(lo, hi)` of `x` in `n`; `(0, 1)` for `n == 0`."""
    if n == 0:
        return 0.0, 1.0
    p = x / n
    d = 1 + Z * Z / n
    c = (p + Z * Z / (2 * n)) / d
    w = Z * math.sqrt(p * (1 - p) / n + Z * Z / (4 * n * n)) / d
    return max(0.0, c - w), min(1.0, c + w)


def _q(hist: Counter, total: int, q: float) -> float:
    """The smallest value whose cumulative share is at least `q`."""
    acc = 0
    for v in sorted(hist):
        acc += hist[v]
        if acc >= q * total:
            return v
    return 0.0


def _r(x: float) -> float:
    return round(float(x), 6)


# ---------------------------------------------------------------------------------------------------- the duel
_ENGINE = None


def _engine():
    """The duel engine, loaded once per process (D-09): `modules.combat.fight` and `.wrapper`, and the typed records."""
    global _ENGINE
    if _ENGINE is None:
        if REPO not in sys.path:
            sys.path.insert(0, REPO)
        from engine.dice_engine.draw import seeded
        from engine.season.queries.inputs import DuelRoundInput, DuelState, PersonalCombatInput
        from modules.combat import fight, wrapper
        _ENGINE = dict(seeded=seeded, DuelRoundInput=DuelRoundInput, DuelState=DuelState, PersonalCombatInput=PersonalCombatInput,
                       fight=fight, wrapper=wrapper)
    return _ENGINE


def _inputs(key: tuple) -> tuple:
    """The two orientations of a cell: orientation 0 puts side `a` in the claimant-A slot, 1 puts it in B."""
    E = _engine()
    (wa, aa, sa), (wb, ab, sb) = key
    mk = lambda kits, scores: E["PersonalCombatInput"](claimants=("A", "B"), ends=(4, 4), wound_quantities=("cumulative_damage", "health_full"),
                                                       terms=TERMS, kits=kits, scores=scores)
    return mk(((wa, aa), (wb, ab)), (sa, sb)), mk(((wb, ab), (wa, aa)), (sb, sa))


def play(inp, hexkey: str):
    """One duel, read per round: the loop of `fight.fight()` run by hand through `fight.fight_round` (the same `fight_draw`, the same
    `round_draw` per round). Returns `(rounds, tie)`; `rounds` is a list of `(felled_slot, yielded_slot, dmg0, dmg1, hf0, hf1)`
    (a slot is 'A', 'B' or None; `dmg` is the round's `cumulative_damage` delta), `tie` that both yield rolls tied."""
    E = _engine()
    fight, wrapper = E["fight"], E["wrapper"]
    fk = wrapper.fight_draw(E["seeded"](hexkey))
    states, closed, prev = (E["DuelState"](), E["DuelState"]()), False, (0, 0)
    rounds, tie = [], False
    for r in range(1, wrapper.DEFAULT_ROUNDS + 1):
        out = fight.fight_round(E["DuelRoundInput"](fighters=inp, states=states, plans=({}, {}), round=r, prev_closed=closed),
                                wrapper.round_draw(fk, r))
        states, closed = out.states, out.closed
        wa, wb = out.wounds["A"], out.wounds["B"]
        cum = (wa["cumulative_damage"], wb["cumulative_damage"])
        rounds.append((out.felled, out.yielded, cum[0] - prev[0], cum[1] - prev[1], wa["health_full"], wb["health_full"]))
        prev = cum
        if out.felled is not None or out.yielded is not None:
            break
        if any(e.get("kind") == "fight_result" for e in out.trace):
            tie = True
            break
    return rounds, tie


def _side_row(x: list, y: list, nk: list, dmg: Counter, nd: int, K: int, n: int) -> tuple:
    """One side's stored row from its counts. Returns `(row, ok)`, `ok` whether the stop rule's precision holds for `h_1..h_3`."""
    h, lo, hi, hy, flags = [], [], [], [], set()
    ok = True
    last = None
    for k in range(1, K + 1):
        nn = nk[k - 1]
        if (k >= 4 and nn < CARRY_MIN) or nn == 0:
            if last is None:
                h.append(0.0), lo.append(0.0), hi.append(1.0), hy.append(0.0)
            else:
                h.append(h[last]), lo.append(lo[last]), hi.append(hi[last]), hy.append(hy[last])
            flags.add(f"carried:{k}")
            if k <= 3:
                ok = False
            continue
        last = k - 1
        xx = x[k - 1]
        l, u = wilson(xx, nn)
        if xx == 0:
            h.append(u), lo.append(0.0), hi.append(u), hy.append(0.0)
            flags.add(f"below_resolution:{k}")
        else:
            h.append(xx / nn), lo.append(l), hi.append(u), hy.append(y[k - 1] / nn)
        if k <= 3 and (u - l) / 2 > max(0.10 * (xx / nn), 0.002):
            ok = False
    if n >= CAP_N and not ok:
        flags.add("precision:absolute")
    row = dict(h=[_r(v) for v in h], h_lo=[_r(v) for v in lo], h_hi=[_r(v) for v in hi], h_yield=[_r(v) for v in hy],
               rounds_at_k=list(nk), flags=sorted(flags),
               damage=dict(p_zero=_r(dmg[0.0] / nd) if nd else 0.0, mean=_r(sum(v * c for v, c in dmg.items()) / nd) if nd else 0.0,
                           q50=_r(_q(dmg, nd, 0.5)), q90=_r(_q(dmg, nd, 0.9)), q99=_r(_q(dmg, nd, 0.99))),
               felled_mortal=None)
    return row, ok


def run_cell(key: tuple, K: int, n: int | None = None, orient: str = "half") -> tuple:
    """Run one cell. `n=None` runs the stop rule (checked at 2,000 and every 500 after, to the 20,000 cap); an `n` runs exactly `n`
    duels. `orient` is 'half' (alternating, the position swap) or 'a_first' / 'b_first' (every duel one way: check 3).
    Returns `(cell, extra)`; `extra` is `{rounds_total, certain}` (not stored)."""
    insp = _inputs(key)
    rng = random.Random(zlib.crc32(repr(key).encode()) % 100000)
    x = [[0] * K, [0] * K]       # per side (0 = a, 1 = b): removals at round index k
    y = [[0] * K, [0] * K]       # ... of which by a failed yield roll
    dmg = [Counter(), Counter()]
    nd = [0, 0]
    nk = [0] * K
    wins = [0, 0]                # a's wins (b was taken out), b's wins
    unresolved = 0
    rounds_total = 0
    i = 0
    while True:
        hexkey = f"{rng.getrandbits(64):016x}"
        o = 0 if orient == "a_first" else 1 if orient == "b_first" else i % 2
        slot_side = (0, 1) if o == 0 else (1, 0)     # claimant slot A, B -> side index (0 = a)
        rounds, tie = play(insp[o], hexkey)
        rounds_total += len(rounds)
        for r, (fe, yi, d0, d1, f0, f1) in enumerate(rounds, 1):
            if r <= K:
                nk[r - 1] += 1
            for slot, d, hf in ((0, d0, f0), (1, d1, f1)):
                dmg[slot_side[slot]][_r(d / hf)] += 1
                nd[slot_side[slot]] += 1
        fe, yi = rounds[-1][0], rounds[-1][1]
        out_slot = fe if fe is not None else yi
        if out_slot is not None:
            loser = slot_side[0 if out_slot == "A" else 1]
            wins[1 - loser] += 1
            r = len(rounds)
            if r <= K:
                x[loser][r - 1] += 1
                if fe is None:
                    y[loser][r - 1] += 1
        else:
            unresolved += 1
        i += 1
        if n is not None:
            if i >= n:
                break
        elif i >= FLOOR_N and (i - FLOOR_N) % STEP_N == 0:
            rows = [_side_row(x[s], y[s], nk, dmg[s], nd[s], K, i) for s in (0, 1)]
            if i >= CAP_N or (rows[0][1] and rows[1][1] and wins[0] > 0 and wins[1] > 0):
                break
    rows = [_side_row(x[s], y[s], nk, dmg[s], nd[s], K, i)[0] for s in (0, 1)]
    cell = dict(a=dict(arm=key[0][0], armour=key[0][1], skill=key[0][2]), b=dict(arm=key[1][0], armour=key[1][1], skill=key[1][2]),
                duels=i, outcome=dict(a=_r(wins[0] / i), b=_r(wins[1] / i), unresolved=_r(unresolved / i)),
                sides=dict(a=rows[0], b=rows[1]))
    return cell, dict(rounds_total=rounds_total, certain=wins[0] == 0 or wins[1] == 0)


def _worker(args):
    key, K = args
    return key, run_cell(key, K)


def cell_json(cell: dict) -> str:
    return json.dumps(cell, sort_keys=True, separators=(",", ":"))


def table_text(cells: list, K: int, head: dict | None = None) -> str:
    """The table, deterministic: sorted keys, floats already rounded to six places, one cell a line. `head` is the table's
    header (default: this tree's); `merge` passes the header its inputs share, so a merged table is the bytes `run` writes."""
    head = head or dict(K=K, engine_fingerprint=engine_fingerprint(), round_source=ROUND_SOURCE, schema=SCHEMA, seed_rule=SEED_RULE, terms=TERMS)
    lines = [f"{json.dumps(k)}: {json.dumps(v)}" for k, v in sorted(head.items()) if k < "cells"]
    out = "{\n" + ",\n".join(lines) + ",\n\"cells\": [\n" + ",\n".join(cell_json(c) for c in cells) + "\n]"
    out += "".join(f",\n{json.dumps(k)}: {json.dumps(v)}" for k, v in sorted(head.items()) if k > "cells") + "\n}\n"
    return out


def _load_table(path: str) -> dict | None:
    if not os.path.exists(path):
        return None
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def _cell_key(c: dict) -> tuple:
    return ((c["a"]["arm"], c["a"]["armour"], c["a"]["skill"]), (c["b"]["arm"], c["b"]["armour"], c["b"]["skill"]))


def _pool_map(tasks: list, workers: int):
    """`(key, (cell, extra))` for each task, in task order; one process when `workers == 1`."""
    if workers <= 1:
        for t in tasks:
            yield _worker(t)
        return
    import multiprocessing as mp
    with mp.get_context("fork").Pool(workers) as pool:
        yield from pool.imap(_worker, tasks, chunksize=1)


# ---------------------------------------------------------------------------------------------------- sub-commands
def _keyorder(grid: Grid):
    return lambda k: (grid.sortkey(k[0]), grid.sortkey(k[1]))


def cmd_run(grid: Grid, out: str | None, workers: int, cells_re: str | None, dry: bool = False) -> int:
    keys = grid.cells()
    if cells_re:
        pat = re.compile(cells_re)
        keys = [k for k in keys if pat.search(grid.key_text(k))]
    if dry:
        print(f"{len(keys)} cells match" + (f" {cells_re!r}" if cells_re else ""))
        return 0 if keys else 2
    if not keys:
        print("no cell matches", file=sys.stderr)
        return 2
    if not out:
        print("run needs OUT (or --dry)", file=sys.stderr)
        return 2
    t0, done, results, certain = time.time(), 0, {}, []
    for key, (cell, extra) in _pool_map([(k, grid.K) for k in keys], workers):
        if extra["certain"]:   # not stored, and it does not cost the rest of the run
            certain.append(key)
            print(f"CERTAIN {grid.key_text(key)}: outcome {cell['outcome']} in {cell['duels']} duels -- not stored; report to the PC lane",
                  file=sys.stderr, flush=True)
        else:
            results[key] = cell
        done += 1
        if done % 25 == 0 or done == len(keys):
            print(f"  {done}/{len(keys)} cells, {time.time() - t0:.0f} s", file=sys.stderr, flush=True)
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(table_text([results[k] for k in sorted(results, key=_keyorder(grid))], grid.K))
    print(f"wrote {len(results)} cells to {out} in {time.time() - t0:.0f} s on {workers} worker(s)"
          + (f"; {len(certain)} certain cell(s) left out" if certain else ""))
    return 3 if certain else 0


def cmd_merge(grid: Grid, out: str, ins: list, complete: bool) -> int:
    """Concatenate chunk tables (disjoint `run --cells` outputs) into one table, in the bytes `run` writes. Refuses a header that
    differs between inputs and a cell in two inputs; reports the cells of the full grid still missing (`--complete`: refuses to write)."""
    heads, cells, seen = [], [], {}
    for p in ins:
        t = _load_table(p)
        if t is None:
            print(f"no table at {p}", file=sys.stderr)
            return 2
        head = {k: v for k, v in t.items() if k != "cells"}
        for h0, p0 in heads[:1]:
            for k in sorted(set(head) | set(h0)):
                if head.get(k) != h0.get(k):
                    print(f"REFUSED: {p} and {p0} differ in {k!r}: {head.get(k)!r} against {h0.get(k)!r}", file=sys.stderr)
                    return 2
        heads.append((head, p))
        for c in t["cells"]:
            key = _cell_key(c)
            if key in seen:
                print(f"REFUSED: cell {grid.key_text(key)} is in both {seen[key]} and {p}", file=sys.stderr)
                return 2
            seen[key] = p
            cells.append(c)
    missing = [k for k in grid.cells() if k not in seen]
    on_grid = set(grid.cells())
    unknown = [k for k in seen if k not in on_grid]
    print(f"{len(cells)} cells from {len(ins)} inputs; {len(missing)} of the grid's {len(on_grid)} still missing"
          + (f"; {len(unknown)} not on the grid" if unknown else ""))
    if missing:
        print("missing: " + " ".join(grid.key_text(k) for k in missing[:20]) + (" ..." if len(missing) > 20 else ""))
    if complete and (missing or unknown):
        return 4
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    cells.sort(key=lambda c: _keyorder(grid)(_cell_key(c)))
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(table_text(cells, heads[0][0]["K"], heads[0][0]))
    print(f"wrote {len(cells)} cells to {out}")
    return 0


def cmd_cell(grid: Grid, keytext: str, n: int, table: str) -> int:
    key = grid.parse_key(keytext)
    t0 = time.time()
    cell, extra = run_cell(key, grid.K, n=n)
    print(json.dumps(cell, sort_keys=True, indent=1))
    print(f"# {n} duels in {time.time() - t0:.1f} s; mean rounds a duel {extra['rounds_total'] / n:.3f}", file=sys.stderr)
    t = _load_table(table)
    stored = None if t is None else next((c for c in t["cells"] if _cell_key(c) == key), None)
    if stored is not None and stored["duels"] == n:
        print("# vs the stored row: " + ("reproduces it byte for byte" if cell_json(cell) == cell_json(stored) else "DIFFERS"), file=sys.stderr)
        return 0 if cell_json(cell) == cell_json(stored) else 1
    return 0


def cmd_spot(grid: Grid, m: int, table: str, workers: int) -> int:
    t = _load_table(table)
    if t is None:
        print(f"no table at {table}", file=sys.stderr)
        return 2
    cells = t["cells"]
    step = max(1, len(cells) // m)
    chosen = [cells[i * step] for i in range(m) if i * step < len(cells)]
    if t.get("engine_fingerprint") != engine_fingerprint():
        print("# WARNING: the table's engine fingerprint is not the tree's; a re-run is expected to differ", file=sys.stderr)
    bad = 0
    # each cell is re-run at its own stored duel count (the stop rule's checkpoint), so an unchanged engine reproduces the row
    for c, (key, (cell, _)) in zip(chosen, _pool_fixed(chosen, grid.K, workers)):
        verdicts = []
        for s in ("a", "b"):
            h1 = cell["sides"][s]["h"][0]
            lo, hi = c["sides"][s]["h_lo"][0], c["sides"][s]["h_hi"][0]
            verdicts.append(lo <= h1 <= hi)
        same = cell_json(cell) == cell_json(c)
        bad += not all(verdicts)
        print(f"{'inside' if all(verdicts) else 'OUTSIDE'}  {grid.key_text(key)}  duels {c['duels']}  h_1 "
              f"{cell['sides']['a']['h'][0]:.4f}/{cell['sides']['b']['h'][0]:.4f} in [{c['sides']['a']['h_lo'][0]:.4f},{c['sides']['a']['h_hi'][0]:.4f}]"
              f"/[{c['sides']['b']['h_lo'][0]:.4f},{c['sides']['b']['h_hi'][0]:.4f}]  {'identical' if same else 'differs'}")
    return 1 if bad else 0


def _fixed_worker(args):
    key, K, n = args
    return key, run_cell(key, K, n=n)


def _pool_fixed(chosen: list, K: int, workers: int):
    if workers <= 1:
        for c in chosen:
            yield _fixed_worker((_cell_key(c), K, c["duels"]))
        return
    import multiprocessing as mp
    with mp.get_context("fork").Pool(workers) as pool:
        yield from pool.imap(_fixed_worker, [(_cell_key(c), K, c["duels"]) for c in chosen], chunksize=1)


def _agree(r1: dict, r2: dict) -> bool:
    """Two measurements of one `h_1` agree when their 95% intervals overlap. [ASSUMPTION: overlap, not 'each point inside the other's
    interval' (MBA §5.2 checks 2 and 3) -- basis: of two independent estimates of one chance each point lies inside the other's
    interval only about 83 times in 100 (the difference has sqrt(2) times one estimate's standard error), so five mirrors would
    fail by chance more often than not (the spear mirror did, at 0.048 against 0.0536); overlap fails about 0.6 times in 100 on a
    true tie, and passes everything the literal test passes; reversible: this function.]"""
    return r1["h_lo"][0] <= r2["h_hi"][0] and r2["h_lo"][0] <= r1["h_hi"][0]


def cmd_trust(grid: Grid, table: str) -> int:
    """The seven checks of MBA §5.2, in order; stops on the first failure."""
    K = grid.K
    cache: dict = {}

    def cell(key, n=None, orient="half"):
        if (key, n, orient) not in cache:
            t0 = time.time()
            cache[(key, n, orient)] = run_cell(key, K, n=n, orient=orient)
            print(f"  ({grid.key_text(key)} {orient}: {cache[(key, n, orient)][0]['duels']} duels, {time.time() - t0:.1f} s)", file=sys.stderr, flush=True)
        return cache[(key, n, orient)]

    def fail(num, name, why):
        print(f"FAIL {num} {name}: {why}")
        return 1

    mirrors = [((arm, "light", 3),) * 2 for arm in grid.arms]
    pilot = grid.parse_key("spear/light/3,arming/light/3")
    t = _load_table(table)
    fp = engine_fingerprint()

    # 1. fingerprint
    if t is None:
        print(f"ok 1 fingerprint: no table yet; tree fingerprint {fp[:12]}")
    elif t.get("engine_fingerprint") != fp:
        return fail(1, "fingerprint", f"the table's {str(t.get('engine_fingerprint'))[:12]} is not the tree's {fp[:12]}; re-run `python tools/calibrate_mb_contact.py run ...`")
    else:
        print(f"ok 1 fingerprint: the table's equals the tree's {fp[:12]}")

    # 2. symmetry: five mirror cells
    for key in mirrors:
        c, _ = cell(key)
        a, b = c["sides"]["a"], c["sides"]["b"]
        if not _agree(a, b):
            return fail(2, "symmetry", f"{grid.key_text(key)}: h_1 {a['h'][0]} vs {b['h'][0]}: the intervals do not overlap "
                        f"[{a['h_lo'][0]}, {a['h_hi'][0]}] / [{b['h_lo'][0]}, {b['h_hi'][0]}]")
        pa, pb, n = c["outcome"]["a"], c["outcome"]["b"], c["duels"]
        se = math.sqrt(max(pa + pb - (pa - pb) ** 2, 1e-12) / n)
        if abs(pa - pb) > 3 * se:
            return fail(2, "symmetry", f"{grid.key_text(key)}: win shares {pa} vs {pb} differ by more than 3 se ({3 * se:.4f}, n {n})")
    print(f"ok 2 symmetry: {len(mirrors)} mirror cells, h_1 intervals overlap, win shares within 3 se")

    # 3. swap: two asymmetric cells both ways
    swap_cells = [grid.parse_key("arming/light/5,arming/light/3"), pilot]
    for key in swap_cells:
        c1, _ = cell(key, 4000, "a_first")
        c2, _ = cell(key, 4000, "b_first")
        for s in ("a", "b"):
            r1, r2 = c1["sides"][s], c2["sides"][s]
            if not _agree(r1, r2):
                return fail(3, "swap", f"{grid.key_text(key)} side {s}: h_1 {r1['h'][0]} (a first) vs {r2['h'][0]} (b first): the intervals do not overlap")
    print(f"ok 3 swap: {len(swap_cells)} asymmetric cells run both ways agree (h_1 intervals overlap)")

    # 4. reproducibility
    c1, _ = run_cell(pilot, K, n=2000)
    c2, _ = run_cell(pilot, K, n=2000)
    if cell_json(c1) != cell_json(c2):
        return fail(4, "reproducibility", f"{grid.key_text(pilot)} at 2000 duels differs between two runs of one seed")
    print("ok 4 reproducibility: one cell twice at one seed, byte-identical")

    # 5. no certainty: the cells run above, and every cell of the table
    seen = [c for (k, n, o), (c, _) in cache.items()] + [c1, c2] + (t["cells"] if t else [])
    for c in seen:
        if c["outcome"]["a"] in (0.0, 1.0) or c["outcome"]["b"] in (0.0, 1.0):
            return fail(5, "no certainty", f"{grid.key_text(_cell_key(c))}: outcome {c['outcome']} in {c['duels']} duels; report to the PC lane")
    print(f"ok 5 no certainty: no outcome share is 0 or 1 in {len(seen)} cells read")

    # 6. rounds run: the arming mirror (the pilot's mirror)
    mk = ((grid.arms[0], "light", 3),) * 2
    c, extra = cell(mk)
    mean = extra["rounds_total"] / c["duels"]
    if mean < 2:
        return fail(6, "rounds run", f"{grid.key_text(mk)}: mean rounds a duel {mean:.3f} is below 2")
    others = ", ".join(f"{k[0][0]} {cell(k)[1]['rounds_total'] / cell(k)[0]['duels']:.2f}" for k in mirrors)
    print(f"ok 6 rounds run: the {mk[0][0]} mirror's mean rounds a duel is {mean:.3f} (mirrors: {others})")

    # 7. round boundary: the rounds the instrument reads against fight.fight()'s own count, 100 duels, one key each
    E = _engine()
    insp = _inputs(pilot)
    rng = random.Random(zlib.crc32(repr(pilot).encode()) % 100000)
    for i in range(100):
        hexkey = f"{rng.getrandbits(64):016x}"
        o = i % 2
        mine = len(play(insp[o], hexkey)[0])
        theirs = E["fight"].fight(insp[o], E["seeded"](hexkey)).rounds
        if mine != theirs:
            return fail(7, "round boundary", f"duel {i} (key {hexkey}): the instrument reads {mine} rounds, fight.fight() {theirs}")
    print("ok 7 round boundary: the instrument's round count equals fight.fight()'s for 100 duels")
    return 0


def main(argv=None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if argv and argv[0] == "run":
        p = argparse.ArgumentParser(prog="calibrate_mb_contact.py run", description=__doc__.splitlines()[0])
        p.add_argument("out", nargs="?")
        p.add_argument("--workers", type=int, default=1)
        p.add_argument("--cells", default=None, help="a regex over the cell's key text, e.g. 'spear/light/3'")
        p.add_argument("--dry", action="store_true", help="print how many cells the regex selects; run no duel")
        a = p.parse_args(argv[1:])
        return cmd_run(Grid(), a.out, a.workers, a.cells, a.dry)
    if argv and argv[0] == "merge":
        p = argparse.ArgumentParser(prog="calibrate_mb_contact.py merge", description="Merges chunk tables of disjoint `run --cells` runs into one table.")
        p.add_argument("out")
        p.add_argument("ins", nargs="+")
        p.add_argument("--complete", action="store_true", help="write nothing (exit 4) unless the inputs cover every cell of the grid")
        a = p.parse_args(argv[1:])
        return cmd_merge(Grid(), a.out, a.ins, a.complete)
    p = argparse.ArgumentParser(prog="calibrate_mb_contact.py", description=__doc__.splitlines()[0])
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--cell", nargs=2, metavar=("KEY", "N"))
    g.add_argument("--spot", type=int, metavar="M")
    g.add_argument("--trust", action="store_true")
    p.add_argument("--table", default=TABLE)
    p.add_argument("--workers", type=int, default=1)
    a = p.parse_args(argv)
    grid = Grid()
    if a.cell:
        return cmd_cell(grid, a.cell[0], int(a.cell[1]), a.table)
    if a.spot:
        return cmd_spot(grid, a.spot, a.table, a.workers)
    return cmd_trust(grid, a.table)


if __name__ == "__main__":
    sys.exit(main())
