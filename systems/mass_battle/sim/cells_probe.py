#!/usr/bin/env python3
"""cells_probe.py -- how big is a season army in cells? Per army preset, the cells of each unit and the ranks of each block.

WHAT IT RUNS. The doctrine's preset army (`modules/mass_battle/troop_types/presets.py::plan`) for one cohort of the given weight
(default 20) whose realm has a barracks, an archery range and a stable, replayed command by command through the module's own
`armyrecord.apply`, then turned into an `OrderOfBattle` and built for side A through `orderofbattle.build_unit`, the path a season
field takes. Nothing here holds a game number: the weight is the probe's argument and the sizes are the module's.

WHAT IT PRINTS. Per unit: its troop type, its troops, the cells its footprint covers and the ranks (rows) of that footprint, at the
arm `references/troops.yaml: deployment.arm` names (`cap` today). At `cap` a body is packed as densely as its type allows, so a
season army is a few cells deep in one rank; `grid` lays it as `deployment.cell_troops` men a cell in `depth` ranks. It prints a
reading and asserts nothing.

    python systems/mass_battle/sim/cells_probe.py [weight ...]
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))

from engine.season.queries.inputs import ArmyCommand, ArmyPresetQuery  # noqa: E402
from modules.mass_battle import armyrecord  # noqa: E402
from modules.mass_battle.orderofbattle import build_unit  # noqa: E402
from modules.mass_battle.troop_types import presets, table  # noqa: E402


def _sites():
    """The probe's own realm: one of each site a preset trains at, complete (a condition of `full`)."""
    # [JUSTIFIED: the probe's own fixture, read by nothing else -- a complete barracks, range and stable, so the preset raises every arm it has]
    full = 1000.0
    return {"barracks": full, "archery_range": full, "stable": full}, full


def preset_record(weight):
    """The army record the preset gives one cohort of `weight`: the plan's commands folded through `armyrecord.apply`."""
    sites, full = _sites()
    plan = presets.plan(ArmyPresetQuery("probe", (("c1", weight, sites),), full, ()))
    record = armyrecord.new("probe")
    for verb, payload in plan:
        op = {"form_unit": "form", "assign_troops": "assign"}.get(verb, verb)
        args = dict(payload, weight=weight, sites=sites, full=full) if op == "recruit" else dict(payload)
        record = armyrecord.apply(ArmyCommand(record, op, args))
    return record


def readings(weight):
    """`[(unit name, troop type, troops, cells, ranks), ...]` for the preset of `weight`, in unit order."""
    oob = armyrecord.to_order_of_battle(preset_record(weight))
    army = build_unit(oob, "probe", "A", morale_start=5)
    out = []
    for row, unit in zip(oob.units, army.units):
        cells = unit.cells()
        out.append((row.name, row.troop_type, row.troops, len(cells), len({r for r, _c in cells})))
    return out


def main(argv):
    weights = [float(a) for a in argv[1:]] or [20.0]      # [JUSTIFIED: the weight the first audit read, `04_MB_cell_hierarchy_as_data.md`'s "weight-20 preset"]
    dep = table.deployment()
    for weight in weights:
        print(f"preset army, one cohort of weight {weight:g}; deployment.arm = {dep['arm']}, cell_troops = {dep['cell_troops']}")
        for name, troop_type, troops, cells, ranks in readings(weight):
            print(f"  {name}: {troop_type}, {troops:g} troops -> {cells} cells, {ranks} rank(s) deep")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
