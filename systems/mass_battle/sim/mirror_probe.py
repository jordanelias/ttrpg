#!/usr/bin/env python3
"""mirror_probe.py -- is the field side-fair? Two IDENTICAL bodies fight, once per seed; the side wins are counted.

WHAT IT RUNS. `n` fields (default 300, seeds 0..n-1), each two identical single bodies of 600 heavy infantry on open
ground, built through the module's own builder (`massbattle._oob_unit`) and fought and graded through its own
`_run_and_grade` -- the call `resolve_field` makes -- with the seed's `random.Random` scoped by `rngsource`. Nothing
here holds a number of the game: the body, the size and the count are the probe's own, and the ruling is the grade.

WHAT IT PRINTS. Per side the win count, the drawn count, and the difference of the two win counts in standard
deviations of a fair coin over the decided fields: `(A - B) / sqrt(A + B)`. A side-fair field reads under 1.5.
A win is the grade's own: a side whose survivor share is higher while it stands and its opponent routed or conceded
or fell behind; a field neither side wins is drawn. The exit code is 1 when the difference is 1.5 or over.

THE CONTROL IT IS. A mirror cannot show a balance, only a bias: every asymmetry it finds (deployment row, the order
the two sides are walked, an unmirrored draw) is the engine's, since the two bodies are the same. It is the
side-fairness reading U5b §1's gate (3) asks of the one sampler (B05.03); it gives no balance claim.

    python systems/mass_battle/sim/mirror_probe.py [n]
"""
from __future__ import annotations

import math
import os
import random
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))
from engine.dice_engine import draw

from modules.mass_battle import massbattle  # noqa: E402
from modules.mass_battle.orderofbattle import OrderOfBattle, UnitRow  # noqa: E402
from modules.mass_battle.terrain import OPEN_FLAT  # noqa: E402

def _body_spec():
    """The probe's own sizes: troop type, troops a side, the standard-deviation limit. A function, not module
    scalars: `tools/export_sim_params.py` reads every module-level literal under `systems/mass_battle/sim/` as a game
    constant, and none of these is one."""
    # [JUSTIFIED: the probe's own sizes, read by nothing else -- a heavy-infantry body of 600 a side and a 1.5 standard-deviation limit make a symmetric mirror whose two sides differ only by the draw]
    return "heavy_infantry", 600.0, 1.5


def _body(side):
    troop_type, troops, _limit = _body_spec()
    oob = OrderOfBattle((UnitRow("line", troop_type, troops),))
    return massbattle._oob_unit(oob, troops, side, massbattle._MORALE_START_BASE)


def one_field(seed):
    """`'A'`, `'B'` or `'drawn'` for the mirror fought with `random.Random(seed)`."""
    a, b = _body("A"), _body("B")
    got = massbattle._run_and_grade(a, b, OPEN_FLAT, draw.seeded(draw.H2("mirror_probe", seed)), by_troops=True)
    if got["attacker_wins"]:
        return "A"
    b_stands = not (b.routed or massbattle.unit_conceded(b))
    if b_stands and (a.routed or massbattle.unit_conceded(a) or got["defender_size_pct"] > got["attacker_size_pct"]):
        return "B"
    return "drawn"


# [JUSTIFIED: the probe's own sample count, a trial number and not a game magnitude]
def run(n=300):
    tally = {"A": 0, "B": 0, "drawn": 0}
    for seed in range(n):
        tally[one_field(seed)] += 1
    decided = tally["A"] + tally["B"]
    sd = abs(tally["A"] - tally["B"]) / math.sqrt(decided) if decided else float("inf")
    return tally, sd


def main(argv):
    n = int(argv[1]) if len(argv) > 1 else 300   # [JUSTIFIED: the same sample count as `run`'s default]
    tally, sd = run(n)
    troop_type, troops, limit = _body_spec()
    print(f"mirror of two {troops:g}-troop {troop_type} bodies, seeds 0..{n - 1}")
    print(f"side A wins {tally['A']}, side B wins {tally['B']}, drawn {tally['drawn']}")
    print(f"difference {abs(tally['A'] - tally['B'])} = {sd:.2f} standard deviations (limit {limit})")
    return 0 if sd < limit else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
