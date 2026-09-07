"""THE DEGREE SWEEP — core: the ladders, the on-ramp, and the narrating log.

⚠ THIS INSTRUMENT DOES NOT MINT A DEGREE, AND THAT IS THE WHOLE OF ITS HONESTY.
`shape.py` S27.2 names "a second resolver" as its highest-value refusal, and `contest()` refuses
to compute a band because no in-chain document supplies a margin model. An instrument that
answered that question by inventing edges would BE the second resolver, wearing a sweep's clothes.

So the degree here is EXOGENOUS: the sweep SUPPLIES each degree as an input and records what the
shape does with it. Every reported band is a band the sweep put in, never one the sweep derived.
That makes each result a statement about the system's CAPACITY to carry a degree -- which is the
question -- and never a statement about which degree is correct, which is `H-98` and stays open.

TWO LADDERS, AND THE GAP BETWEEN THEM IS THE FINDING
----------------------------------------------------
LADDER C -- the CANONICAL four, `engine/autoload/dice_engine.py::degree_from_net`, single owner
  for every scale of the game by Jordan's 2026-08-14 ruling, read off the MARGIN:
      margin >= 3  Overwhelming | >= 1 Success | 0 <= m < 1 Partial | < 0 Failure
LADDER D -- the DECLARED three, `verb_table.yaml`'s `kill / wound` row, the only degree-keyed
  verb in the corpus: Felled | Wounded | Untouched.

They are different alphabets of different arity. Neither document cites the other.
"""
from __future__ import annotations

import sys
from pathlib import Path

TRACER = Path(__file__).resolve().parents[2] / "engine" / "season"
if str(TRACER) not in sys.path:
    sys.path.insert(0, str(TRACER))

import shape as S            # noqa: E402
import corpus_run as C       # noqa: E402
import run_cases as R        # noqa: E402
import combat_seam as CS     # noqa: E402

# `CLAUDE.md` §0.1 pt 5 / G1: declared with its reason, never a bare literal in a body.
LADDER_C = ("Overwhelming", "Success", "Partial", "Failure")
LADDER_C_WHY = ("engine/autoload/dice_engine.py::degree_from_net -- THE ladder, single owner for "
                "every scale (Jordan ruling 2026-08-14), read off the margin `net - ob`")
LADDER_D = ("Felled", "Wounded", "Untouched")
LADDER_D_WHY = ("engine/season/verb_table.yaml, the `kill / wound` "
                "row -- the ONLY degree-keyed verb in the corpus")

# The contested verb. There is exactly one; that is measured, not assumed (see `contested_verbs`).
KW = "kill / wound"


def contested_verbs() -> dict:
    """Every verb declaring `contests:`. Measured from the table, so a second one appearing
    later shows up here rather than silently falling outside a hardcoded name."""
    return {v: r for v, r in S.VERB_TABLE.items() if getattr(r, "contests", "")}


def foldable() -> set:
    return set(S.resolvable_verbs())


class Log:
    """The narrating channel. Every mechanical action, paired with what it means.

    `trace_log.Trace` already records the SHAPE's internals and this does not duplicate it (§8);
    this records the SWEEP's own actions -- which degree was injected where, and what came back."""

    def __init__(self) -> None:
        self.lines: list[str] = []
        self.depth = 0

    def __call__(self, tag: str, what: str, why: str = "") -> None:
        pad = "  " * self.depth
        self.lines.append(f"{pad}[{tag:11}] {what}")
        if why:
            self.lines.append(f"{pad}{'':14}| {why}")

    def rule(self, title: str) -> None:
        self.lines.append("")
        self.lines.append("=" * 78)
        self.lines.append(title)
        self.lines.append("=" * 78)

    def text(self) -> str:
        return "\n".join(self.lines)
