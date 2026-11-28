#!/usr/bin/env python3
"""pike_probe.py -- does a weapon's reach class show on a field? A pike line and a heavy-infantry line of one size fight the same
defender on the same seeds; the fields that read IDENTICAL are counted.

WHAT IT RUNS. `n` seeds (default 200, seeds 0..n-1). Per seed, two fields on open ground, each a single 600-troop body against the
same 600-troop heavy-infantry defender: the pike body, then the heavy-infantry body, built through the module's own builder
(`massbattle._oob_unit`) and fought and graded through its own `_run_and_grade`, the call `resolve_field` makes. It runs twice:

  as laid     the bodies as `references/troops.yaml: deployment.arm` lays them (at `cap` the densest packing, one or two ranks: a
              weapon's support reach past the contact rank has nothing behind it to reach);
  on the grid each body laid on its troop type's own `depth` (`orderofbattle.cells_for`: pike 4, heavy infantry 2).

WHAT IT PRINTS. Per run, how many of the n field results are identical between the two lines, and the win counts of each line. It
prints a reading and asserts nothing: the pike's edge is its third supporting rank, and whether a field shows it is the field's.

    python systems/mass_battle/sim/pike_probe.py [n]
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))
from engine.dice_engine import draw

from engine.season.data.rosters import WON  # noqa: E402
from engine.season.seam.ladder import field_degree  # noqa: E402
from modules.mass_battle import massbattle  # noqa: E402
from modules.mass_battle.orderofbattle import OrderOfBattle, UnitRow  # noqa: E402
from modules.mass_battle.terrain import OPEN_FLAT  # noqa: E402
from modules.mass_battle.troop_types import table  # noqa: E402


def _bodies():
    """The probe's own sizes: the two lines' troop types, the troops of each body and of the defender."""
    # [JUSTIFIED: the probe's own sizes, read by nothing else -- the two lines differ in their weapon and nothing else, against one defender]
    return ("pike", "heavy_infantry"), 600.0, "heavy_infantry"


def _body(troop_type, troops, side, on_grid):
    depth = table.depth_of(troop_type) if on_grid else None
    oob = OrderOfBattle((UnitRow("line", troop_type, troops, depth=depth),))
    return massbattle._oob_unit(oob, troops, side, massbattle._MORALE_START_BASE)


def one_field(troop_type, seed, on_grid):
    """The graded result of `troop_type`'s body against the defender, on `draw.seeded(draw.H2("pike_probe", seed))`."""
    _lines, troops, defender = _bodies()
    return massbattle._run_and_grade(_body(troop_type, troops, "A", on_grid), _body(defender, troops, "B", False), OPEN_FLAT,
                                     draw.seeded(draw.H2("pike_probe", seed)), 1000)


# [JUSTIFIED: the probe's own sample count, a trial number and not a game magnitude]
def run(n=200):
    (a, b), _troops, _defender = _bodies()
    out = {}
    for label, on_grid in (("as laid", False), ("on the grid", True)):
        same = wins_a = wins_b = 0
        for seed in range(n):
            ra, rb = one_field(a, seed, on_grid), one_field(b, seed, on_grid)
            same += ra == rb
            wins_a += field_degree(ra) == WON
            wins_b += field_degree(rb) == WON
        out[label] = (same, wins_a, wins_b)
    return out


def main(argv):
    n = int(argv[1]) if len(argv) > 1 else 200   # [JUSTIFIED: the same sample count as `run`'s default]
    (a, b), troops, defender = _bodies()
    print(f"{a} and {b} bodies of {troops:g} troops against {troops:g} {defender}, seeds 0..{n - 1}; deployment.arm = {table.deployment()['arm']}")
    for label, (same, wins_a, wins_b) in run(n).items():
        print(f"{label}: {same} of {n} fields identical between the two lines; wins {a} {wins_a}, {b} {wins_b}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
