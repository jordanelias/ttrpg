"""THE EXTREMES THE PESSIMIST MEASURED, as a three-line probe (B17.04; `U5b_MB_residue` §6, `16_PESSIMIST_MB` §3.3).

`modules/mass_battle/massbattle.py::resolve_field` is called on three hand-built headcount fields, each side one person, on
open ground, and `run_battle` is wrapped to count how many times it is entered:

    0 a side       a field of nobody against nobody
    1 a side       one man a side (a weight of 0.04 is `under_arms_cap` 1, the crash floor `_MIN_TROOPS`)
    20,000 a side  a side past `config.MAX_TROOPS_PER_UNIT` (a weight of 667 is `under_arms_cap` 20,010)

Run from the repository root: `python systems/mass_battle/sim/extremes_probe.py`. EXPECTED (the module refuses each
with a typed result, and `run_battle` is never entered):

    0 a side: PARTY-GAP, run_battle entered 0 time(s)
    1 a side: PARTY-GAP, run_battle entered 0 time(s)
    20000 a side: SCALE-GAP, run_battle entered 0 time(s)

BEFORE the refusals, the reading is red: 0 and 1 a side resolve (the crash floor, the attacker `lost`), 20,000 a side resolves.
Reads only; writes nothing. Exits 0 when all three lines are the expected ones, 1 otherwise.
"""
from __future__ import annotations

import importlib
import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from engine.dice_engine import draw  # noqa: E402

#: (label, the weight of the one person on each side). `under_arms_cap(w)` is floor(w x 300 x 0.10).
CASES = (("0", 0.0, "PARTY-GAP"), ("1", 0.04, "PARTY-GAP"), ("20000", 667.0, "SCALE-GAP"))


def _record(weight: float):
    import yaml
    from engine.season.data import files
    from engine.season.queries.inputs import MassBattleInput
    with open(files.GEOGRAPHY_YAML, encoding="utf-8") as f:
        geo = yaml.safe_load(f)
    return MassBattleInput(weights=((weight,), (weight,)), territory=None, fort_level=0.0, stances=(0.0, 0.0),
                           walls_dr=None, origin=None, loyalties=(0.0, 0.0), loyalty_gain=0, geography=geo,
                           condition_scale=1000, members=(("a",), ("b",)))


def read() -> list[tuple[str, str]]:
    """`[(line, expected_status)]`, one per case: what `resolve_field` returned and how often `run_battle` was entered."""
    mb = importlib.import_module("modules.mass_battle.massbattle")
    entered = [0]
    real = mb.run_battle

    def counting(*a, **k):
        entered[0] += 1
        return real(*a, **k)

    mb.run_battle = counting
    out = []
    try:
        for label, weight, want in CASES:
            entered[0] = 0
            got = mb.resolve_field(_record(weight), draw.seeded(draw.H2("extremes_probe", 0)))
            said = got.get("status") if isinstance(got, dict) else f"resolved ({got.ended})"
            out.append((f"{label} a side: {said}, run_battle entered {entered[0]} time(s)",
                        f"{label} a side: {want}, run_battle entered 0 time(s)"))
    finally:
        mb.run_battle = real
    return out


def main() -> int:
    rows = read()
    for line, _want in rows:
        print(line)
    return 0 if all(line == want for line, want in rows) else 1


if __name__ == "__main__":
    sys.exit(main())
