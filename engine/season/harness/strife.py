"""`harness.strife` -- WHICH OF THE STUDY'S 40 STRIFE MOVES THE SEASON LOOP CAN REACH, AND WHICH IT DID.

An INSTRUMENT, like `harness/aperture.py`: it reads the Event log and writes nothing, so it moves no
hash. The vocabulary is `strife_moves.yaml` (loaded by `data/strife.py`), a reading of the study
"Mechanics of Strife to c. 1600". Each code is graded on three separate things, because one number
would hide which owner closed it:

    declared   every verb the row names is in `verb_table.yaml` and every Event kind it names is one
               the loop declares (the loader refuses otherwise); a row with no kind states its gap
    observed   Events of those kinds in the log of a populated realm run through `populated.run`,
               summed over the seeds given
    bound      `side` / `office` / `context` the row says a kind alone cannot tell: the observed
               count is an UPPER BOUND on that move, because the same kind also covers other moves
               (`tenure.closed` is a death's seat and a dismissal alike)

A code is OBSERVED when its count is above 0, DARK when the row names a switch that ships off and the
count is 0, UNOBSERVED when it is declared and 0 with no switch to blame, and GAP when no verb or kind
produces it. A count of 0 over a few seeds is a finding about default play, not a proof of absence;
the same run at more seeds is the control.

    python -m engine.season.harness.strife <seasons> <seed> [seed ...]
"""
from __future__ import annotations

import sys
from collections import Counter

from ..data.strife import MOVES
from . import populated


def kinds_in(w) -> Counter:
    """Event kinds in a built, run world's log."""
    return Counter(e.kind for e in w.log)


def grade(row: dict, seen: Counter) -> tuple:
    """`(status, count)` for one row against a pooled kind count."""
    n = sum(seen[k] for k in row["kinds"])
    if not row["kinds"]:
        return "GAP", 0
    if n:
        return "OBSERVED", n
    return ("DARK" if row.get("dark") else "UNOBSERVED"), 0


def measure(seasons: int, seeds: tuple) -> dict:
    """Run each seed through the owner (`populated.run`) and pool the kind counts."""
    seen = Counter()
    for s in seeds:
        w = populated.build_realm(s)
        populated.run(seasons, s, w=w)
        seen.update(kinds_in(w))
    return {"seasons": seasons, "seeds": tuple(seeds), "seen": seen,
            "rows": [(r, *grade(r, seen)) for r in MOVES]}


def report(m: dict) -> str:
    out = [f"strife moves: {len(m['rows'])} codes, {m['seasons']} seasons, seeds {list(m['seeds'])}", ""]
    tally = Counter(st for _, st, _ in m["rows"])
    out.append("  ".join(f"{k} {tally[k]}" for k in ("OBSERVED", "UNOBSERVED", "DARK", "GAP")))
    out.append("")
    out.append(f"{'code':<4} {'move':<24} {'status':<11} {'n':>6}  bound    kinds / note")
    for r, st, n in m["rows"]:
        bound = ",".join(r.get("needs", ())) or "-"
        note = r.get("gap") or r.get("dark") or ",".join(r["kinds"])
        out.append(f"{r['code']:<4} {r['name']:<24} {st:<11} {n:>6}  {bound:<8} {note}")
    return "\n".join(out)


def main(argv=None) -> int:
    a = list(sys.argv[1:] if argv is None else argv)
    if len(a) < 2:
        print("usage: python -m engine.season.harness.strife <seasons> <seed> [seed ...]")
        return 2
    seasons, seeds = int(a[0]), tuple(int(x) for x in a[1:])
    print(report(measure(seasons, seeds)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
