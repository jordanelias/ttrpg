#!/usr/bin/env python3
"""role_edges_probe.py -- does a unit role on a menu change the field it fights? (B17.07; `U5b_MB_residue` §1.)

WHAT IT RUNS. For every (troop type, role) pair on a menu of `config.TROOP_TYPE_ROLES`, a one-unit army of that troop type
in that role fights a plain balanced Line of the foe's, once per seed, and the same troop type with NO role (a plain
Line, no instructions) fights the same foe on the same seed. Friction is off (`MB_FRICTION=0`, set before the module is
read) and the movement path is the node path the season runs. The two fields are compared whole: every cell of every
unit of both armies, and each unit's centroid, after the engagement.

WHAT IT PRINTS. One row per pair: the count of seeds, out of `n`, on which the role's field is IDENTICAL to the no-role
field. A pair at `n` of `n` is a menu choice that changes nothing: the role is a label. The exit code is 1 when any
pair outside the recorded rows below reads `n` of `n`.

THE RECORDED ROWS (read, not excused): `VolleyLine` stays as a shape, its instruction tuple emptied (`volley` and
`shoot_move` have no primitive), so it is the plain Line for archers; `Anvil` stays because it differs against horse
(`brace_probe`), recorded as inert against the foot this probe fights. Both are named in `_recorded`, with `Support` and
`Reserve` (the levy's 'any' menu), which the probe found identical and the entry's list does not rule on.

    python systems/mass_battle/sim/role_edges_probe.py [n]
"""
from __future__ import annotations

import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

os.environ["MB_FRICTION"] = "0"   # friction off, read by `config` at import: set before it is imported

from engine.dice_engine import draw  # noqa: E402
from modules.mass_battle import config, rngsource  # noqa: E402
from modules.mass_battle.orchestration import run_battle  # noqa: E402
from systems.mass_battle.sim import validators as _val  # noqa: E402
from systems.mass_battle.sim.engine import build_army, build_unit  # noqa: E402


def _recorded():
    """The (troop type, role) pairs that stay on a menu while reading inert against the foot this probe fights, and why.
    A function, not a module literal: `tools/export_sim_params.py` reads module-level literals here as game constants."""
    return {
        ("archers", "VolleyLine"): "a shape: its instruction tuple is emptied, the plain Line for archers",
        ("heavy_infantry", "Anvil"): "inert against foot; it differs against horse (brace_probe)",
        ("pike", "Anvil"): "inert against foot; it differs against horse (brace_probe)",
        ("spearmen", "Anvil"): "inert against foot; it differs against horse (brace_probe)",
        # not in the entry's list: found by this probe; `reserve` is read only by the workbench loop (`multi.unit_in_reserve`)
        ("levy", "Support"): "NOT RULED: outside B17.07's list; `reserve` is read by the workbench loop only",
        ("levy", "Reserve"): "NOT RULED: outside B17.07's list; `reserve` is read by the workbench loop only",
    }


def _fingerprint(*armies):
    out = []
    for a in armies:
        for u in a.units:
            out.append((u.centroid(), tuple(sorted(u.cell_troops.items()))))
    return repr(out)


def _field(troop_type, role, seed):
    spec = {"troop_type": troop_type}
    if role is None:
        spec["shape"] = "Line"
    else:
        spec["role"] = role
    with rngsource.using(draw.seeded(draw.H2("role_edges_probe", seed))):
        a = build_army([spec], "R", "A")
        b = build_unit("Line", 3, "E", "B", 25)
        run_battle(a, b, max_ticks=18)   # [JUSTIFIED: the probe's own engagement length, the one the role tests fight]
    return _fingerprint(a, b)


def _pairs():
    for troop_type, roles in config.TROOP_TYPE_ROLES.items():
        for role in roles:
            yield ("levy" if troop_type == "any" else troop_type), role


def run(n=60):
    """`[(troop type, role, identical seeds of n)]` for every pair on a menu."""
    _val._set_movement_path("node")
    rows = []
    for troop_type, role in _pairs():
        same = sum(1 for s in range(n) if _field(troop_type, role, s) == _field(troop_type, None, s))
        rows.append((troop_type, role, same))
    return rows


def main(argv):
    n = int(argv[1]) if len(argv) > 1 else 60   # [JUSTIFIED: the sample count the entry names]
    rows = run(n)
    recorded = _recorded()
    bad = 0
    for troop_type, role, same in rows:
        note = ""
        if same == n:
            note = "  recorded: " + recorded[(troop_type, role)] if (troop_type, role) in recorded else "  IDENTICAL: a label"
            bad += (troop_type, role) not in recorded
        print(f"{troop_type:16s} {role:11s} identical {same:3d} of {n}{note}")
    print(f"{bad} pair(s) read identical in {n} of {n} outside the recorded rows")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
