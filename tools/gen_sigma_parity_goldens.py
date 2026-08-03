#!/usr/bin/env python3
"""Generate the sigma-leverage parity golden table.

WHY THIS EXISTS
---------------
`engine/tests/test_sigma_leverage_parity.py` validates `engine/autoload/sigma_leverage.py`
against two historical reference implementations that live OUTSIDE the engine tree:

  * `tests/sim/v32-combat-balance/m1_dice_sigma_core.py`  — the numpy original (combat surface)
  * `audit/2026-06-03-contest-groundup/engine.py`         — the ground-up engine (contest surface)

Both are frozen provenance. Neither can move: the groundup file's siblings do
`from engine import ...`, so lifting it out breaks that audit artifact's own 151 tests.
And per the fork plan of record §5 the fork carries `engine/` and LEAVES `audit/` and
`tests/`, so a parity test that reaches into them cannot come along.

Reaching across those boundaries at test time already cost real coverage once: the
groundup load sat inside a bare `except` pointing at the pre-retirement `designs/audit/`
path, so from 2026-07-19 to 2026-08-03 the reference silently read as absent and 184
parity cases skipped while the suite reported green.

So the coupling is inverted, which is the same move the fork plan prescribes for params
(§2.1: "table becomes source"). THIS generator runs in the source repo, where the oracles
live, and emits a data table. The test reads the table. The oracles stay put as
provenance; the fork carries a JSON file and no cross-tree reach.

The table is a regeneration target, not a hand-edited file. If `sigma_leverage.py`
changes behaviour, the test goes red -- that is the point. Regenerate ONLY when the
oracles themselves are re-derived, and say why in the commit.

Usage:
    python3 tools/gen_sigma_parity_goldens.py            # write the table
    python3 tools/gen_sigma_parity_goldens.py --check    # verify it is current (CI)
"""
from __future__ import annotations

import importlib.util
import json
import os
import sys

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
OUT = os.path.join(REPO_ROOT, 'engine', 'tests', 'goldens', 'sigma_leverage_parity.json')

# The grids the parity test asserts over. Kept here because this file OWNS the table;
# the test reads whatever rows it finds rather than re-declaring the grid (one owner).
NET_SIGMA_GRID = [-50.0, -5.0, -2.0, -1.5, -1.0, -0.5, 0.0,
                  0.25, 0.5, 0.75, 1.0, 1.5, 2.0, 5.0, 10.0, 50.0]
POOL_GRID = [1, 5, 10, 26]
TN_GRID = [6, 7, 8]
BASE_OB_GRID = [1.0, 2.0, 3.0, 5.0]
LEVEL_NAMES = ["minor", "moderate", "strong", "major"]
DEGREE_NET_GRID = [-3, 0, 1, 2, 3, 5, 6, 8, 12, 20]
DEGREE_OB_GRID = [1.0, 2.0, 3.0]
DEGREE_POOL_GRID = [None, 2, 5, 9, 16, 22, 25]
# Cases that sit ON the pool-aware Overwhelming bar (mean + OVERWHELM_SIGMA*sd*sqrt(pool)).
# MEASURED: with the grid above alone, changing OVERWHELM_SIGMA 0.85 -> 0.86 left all 1,851
# assertions green -- the bar moves by 0.008*sqrt(pool), less than the spacing between
# consecutive integer `net` values at those pools, so no case could observe it. These are the
# (pool, net) pairs where that 0.01 change DOES flip a degree, found by sweeping pools 1..400.
# Without them the constant is untested at any grid resolution (CLAUDE.md 0.1 point 2).
DEGREE_BAR_EDGE_CASES = [(22, 12), (82, 39), (98, 46), (105, 49), (112, 52)]
LEVELS_CASES = [
    (["minor"], None),
    (["moderate", "strong"], ["minor"]),
    (None, ["major"]),
    (["major", "major"], ["major"]),
    (None, None),
    (["minor", "moderate", "strong", "major"], None),
    (None, ["minor", "moderate", "strong", "major"]),
]


def _load_by_path(name: str, path: str):
    """Load a module by explicit path under a unique name.

    A bare `import engine` collides with the top-level `engine/` package (ED-IN-0071 P3),
    which is cached in sys.modules the moment any `engine.*` import runs -- so the bare
    form would return that package instead of the audit-folder file.
    """
    if not os.path.exists(path):
        raise SystemExit(f"reference oracle missing: {path}\n"
                         f"This generator only runs in the source repo, where the oracles live.")
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def build() -> dict:
    m1_dir = os.path.join(REPO_ROOT, 'tests', 'sim', 'v32-combat-balance')
    if m1_dir not in sys.path:
        sys.path.insert(0, m1_dir)
    m1 = _load_by_path('_m1_oracle_ref', os.path.join(m1_dir, 'm1_dice_sigma_core.py'))
    gu = _load_by_path('_groundup_oracle_ref',
                       os.path.join(REPO_ROOT, 'audit', '2026-06-03-contest-groundup', 'engine.py'))

    rows: list[dict] = []

    def emit(oracle: str, fn: str, args: list, value):
        rows.append({"oracle": oracle, "fn": fn, "args": args, "want": value})

    # --- numpy original (combat surface) -------------------------------------
    for pool in POOL_GRID:
        emit("m1", "sigma_n", [pool], float(m1.sigma_n(pool)))
    for ns in NET_SIGMA_GRID:
        emit("m1", "soft_cap", [ns], float(m1.soft_cap(ns)))
    for ns in NET_SIGMA_GRID:
        for pool in POOL_GRID:
            emit("m1", "sigma_space_ob_shift", [ns, pool],
                 float(m1.sigma_space_ob_shift(ns, pool)))
            for tn in TN_GRID:
                for capped in (True, False):
                    emit("m1", "net_boost", [ns, pool, tn, capped],
                         float(m1.net_boost(ns, pool, tn, capped)))
            for base_ob in BASE_OB_GRID:
                emit("m1", "eff_ob", [base_ob, pool, ns], float(m1.eff_ob(base_ob, pool, ns)))
                for tn in TN_GRID:
                    emit("m1", "p_success", [base_ob, pool, ns, tn],
                         float(m1.p_success(base_ob, pool, ns, tn)))
    # levels_to_net_sigma takes LISTS of level names, not counts. The grid is enumerated
    # rather than crossed: the function is a difference of sums, so a handful of shapes
    # (one-sided, two-sided, empty, repeated) covers it.
    for agg, dfd in LEVELS_CASES:
        emit("m1", "levels_to_net_sigma", [agg, dfd],
             float(m1.levels_to_net_sigma(agg, dfd)))

    # --- groundup engine (contest surface) -----------------------------------
    for name in LEVEL_NAMES:
        emit("groundup", "level", [name], float(gu.level(name)))
    for net in DEGREE_NET_GRID:
        for ob in DEGREE_OB_GRID:
            for pool in DEGREE_POOL_GRID:
                emit("groundup", "degree", [net, ob, pool], gu.degree(net, ob, pool))
    for pool, net in DEGREE_BAR_EDGE_CASES:
        for ob in DEGREE_OB_GRID:
            for n in (net - 1, net, net + 1):
                emit("groundup", "degree", [n, ob, pool], gu.degree(n, ob, pool))

    return {
        "schema": 1,
        "generator": "tools/gen_sigma_parity_goldens.py",
        "subject": "engine/autoload/sigma_leverage.py",
        "oracles": {
            "m1": "tests/sim/v32-combat-balance/m1_dice_sigma_core.py",
            "groundup": "audit/2026-06-03-contest-groundup/engine.py",
        },
        "note": ("Frozen expected values captured from the two reference implementations. "
                 "The oracles stay in the source repo; this table travels with engine/. "
                 "Regenerate only when an oracle is re-derived."),
        "rows": rows,
    }


def main(argv: list[str]) -> int:
    table = build()
    text = json.dumps(table, indent=1, sort_keys=False) + "\n"
    if '--check' in argv:
        if not os.path.exists(OUT):
            print(f"[SIGMA-GOLDENS] missing: {OUT}", file=sys.stderr)
            return 1
        cur = open(OUT, encoding='utf-8').read()
        if cur != text:
            print("[SIGMA-GOLDENS] stale — rerun tools/gen_sigma_parity_goldens.py",
                  file=sys.stderr)
            return 1
        print(f"[SIGMA-GOLDENS] current ({len(table['rows'])} rows)")
        return 0
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, 'w', encoding='utf-8') as fh:
        fh.write(text)
    print(f"[SIGMA-GOLDENS] wrote {len(table['rows'])} rows -> "
          f"{os.path.relpath(OUT, REPO_ROOT)}")
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
