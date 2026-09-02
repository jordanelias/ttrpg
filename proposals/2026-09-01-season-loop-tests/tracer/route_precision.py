"""A MECHANICAL GUARD AGAINST THE BARE-TOKEN CLASS, which has now recurred FIVE times.

The history, and it is the argument for doing this structurally rather than token by token:

  1. `ambient`   -- matched ambient-MATERIAL rows; a blocker went 8 arcs -> 3   (in-chain, #351)
  2. `counter`   -- matched inside "counter-productive";        10 arcs -> 8   (in-chain, #351)
  3. `standing`  -- matched the ADJECTIVE ("a standing armed institution"); 18 core rows
  4. `standing X`-- escaped the 15-noun whitelist built for (3), via "a standing condition"
  5. `age\\w*`    -- matched AGENT, AGENTS, AGENCY, AGENDA, and produced the arc corpus's
                    ONLY PLAYABLE verdict, on rows about "two AGENTS belonging to rival powers"

Four of the five were caught by a human or an adversary reading output, one at a time, AFTER the
verdict had been published. A whitelist of guarded tokens cannot work: (4) is that whitelist
failing, and (5) was not on it. **The answer is to forbid the SHAPE, not to enumerate the words.**

THE RULE THIS ENFORCES: a route may not be DECISIVE ON A SINGLE COMMON WORD. If a sentence
consisting of one ordinary English word in a neutral carrier is enough to claim a route, that
route will claim rows it has not read.

This is deliberately NOT a repository guard -- it is a module of the instrument, load-bearing on
the instrument's own verdicts, which is what CLAUDE.md S0.1 point 5's predicate requires of
anything that earns its existence.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import run_cases as R

# Ordinary words that appear constantly in this corpus's prose. A route decisive on one of these
# is reading the sentence's furniture, not its requirement.
COMMON = """
    person people character actor agent agents agency agenda action act must able world
    faction institution order house power party body council office post seat rank title
    season turn time state change value quantity level track counter number scale weight
    place region area settlement territory province realm site land condition standing
    fire produce block leave scene invest execute compound crisis appeal hidden everywhere
    make take give hold read write know see move work play cause effect thing kind form
    group set list roster member holder subject object matter event outcome result process
    system module rule law right wrong good bad high low new old same different other
""".split()

CARRIERS = ["{w}", "a {w}", "the {w} must be able to exist",
            "a character interacts with the {w} during a season"]


def audit() -> list[tuple[str, str, str]]:
    """Return (probe_id, word, carrier) for every route decisive on one common word."""
    offenders: list[tuple[str, str, str]] = []
    for pid, rx, neg in R.COMPILED:
        for w in COMMON:
            for c in CARRIERS:
                text = c.format(w=w)
                if rx.search(text) and not (neg and neg.search(text)):
                    offenders.append((pid, w, text))
                    break
            else:
                continue
            break
    return offenders


# Probes NO case row should reach, because they are the instrument testing ITSELF rather than
# testing a need the corpus expresses. Declaring them is what makes the unreachable COUNT honest:
# S44.4's in-chain ruling names "eleven unreachable probes" as a symptom, and an undeclared
# self-check is indistinguishable from a coverage hole.
DELIBERATELY_UNROUTED = {
    "A1":   "provokes causes=[] to show S19.4's refusal fires; A2 is the routed one",
    "A11":  "provokes a stored aggregate on a Rung; W10 is the routed one",
    "A12":  "provokes a cache inside a parallel map -- an instrument-internal S4 check",
    "A20":  "provokes the retracted wrapper rule; no case asks for a wrapper",
    "A30":  "provokes an unregistered fixture -- S42.2's polarity rule on the harness itself",
    "A31b": "a fixture sweep, not a need",
    "A31c": "a fixture sweep, not a need",
    "A37":  "reaches S27's five strata, which no case row names",
    "A38":  "reaches S27.4's Ob>2xPool gate, which no case row names",
    "A39":  "reaches S39.2's causes[]-names-the-act rule at the seam boundary",
    "P19":  "provokes L5's outcome refusal; A3 is the routed one",
    "P25":  "provokes S15.3's causation rule; P24 is the routed one",
    "P2x":  "provokes the engine-truncation refusal; P2 is the routed one",
    "P2y":  "W17's positive half -- that several interactions inside one budgeted scene are "
            "LAWFUL after Jordan's 2026-09-02 ruling. No case row asks for it because the corpus "
            "predates the ruling; P2x is its refusing twin and P2 is the routed one",
    "W1x":  "provokes S42.2.1's no-silent-default rule on the wear table",
}


def unreachable() -> list[str]:
    """Probes no route can ever reach. The in-chain ruling S44.4 names this exact symptom:
    a regex router 'produced ELEVEN UNREACHABLE PROBES and a 46% miss rate'."""
    import probes as P
    routed = {pid for pid, _, _ in R.COMPILED}
    return sorted(set(P.PROBES) - routed - set(DELIBERATELY_UNROUTED))


if __name__ == "__main__":
    off = audit()
    print(f"=== ROUTES DECISIVE ON A SINGLE COMMON WORD: {len(off)} ===")
    for pid, w, text in off:
        print(f"  {pid:5s}  fires on {w!r:14s} via {text!r}")
    un = unreachable()
    print(f"\n=== UNREACHABLE PROBES, UNDECLARED (a genuine coverage hole): {len(un)} ===")
    print("   ", " ".join(un) if un else "(none)")
    print(f"\n=== DELIBERATELY UNROUTED (the instrument testing itself): "
          f"{len(DELIBERATELY_UNROUTED)} ===")
    for k, why in sorted(DELIBERATELY_UNROUTED.items()):
        print(f"  {k:5s}  {why}")
