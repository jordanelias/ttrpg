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

# ⚠ THE REPOSITORY ROOT, NOT THE PACKAGE DIRECTORY, AND THE IMPORTS ARE DOTTED. This inserted
# `engine/season/` and imported `shape`/`corpus_run`/`run_cases`/`combat_seam` by BARE NAME, which
# worked while those were loose modules sharing a directory. The decomposition (ED-IN-0203) made
# `engine.season` an ordinary package whose modules import each other relatively, so a bare import
# of `shape` now raises *attempted relative import with no known parent package* — and it does so
# from inside this file, four levels away from the change. Dotted imports also end the second
# identity the flat form created: a module reachable as both `shape` and `engine.season.shape` is
# two module objects with two sets of module-level state in one process.
_REPO_ROOT = Path(__file__).resolve().parents[2]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from engine.season import shape as S                    # noqa: E402
from engine.season.harness import corpus_run as C       # noqa: E402
from engine.season.harness import run_cases as R        # noqa: E402
from engine.season import combat_seam as CS             # noqa: E402
from engine.season import decision as PS                # noqa: E402

# ⚠ `PS` IS THE ONE ALIAS THE STEP-7 DECOMPOSITION ADDS HERE (ED-IN-0203). `pack_scenes` moved
# from `shape.py` to `season.decision` at step 7, together with its sole bare-name caller
# (`make_chooser`). `make_chooser` now resolves `pack_scenes` in `decision`'s OWN globals at call
# time, not `shape`'s -- so a rebind of `S.pack_scenes` (this module's `shape` alias) is a no-op
# on it. `arm9_forking.py` and `arm9_subj.py` install a spy/fake by rebinding the module attribute
# around a scoped run (`_REAL_PACK = S.pack_scenes` / `S.pack_scenes = packed` / restore); both are
# re-pointed to `PS.pack_scenes` in the same commit that adds this alias, so the rebind reaches the
# function `make_chooser` actually calls.
#
# ⚠ SO ARE `arm7_flexibility.py` AND `wd_acceptance.py`, AND THE FIRST DRAFT OF THIS PARAGRAPH SAID
# OTHERWISE ON A FALSE PREMISE. It read: *"`arm7_flexibility.py` ... is DELIBERATELY left
# unrepointed -- nothing imports that file, so it cannot fail the suite"*, and cited §0.1 pt 5 to
# license leaving it. Both halves were wrong. `sweep.py:19` imports `arm7_flexibility` and runs it
# at `:111`; `wd_acceptance` is imported by SIX files (`wd_chunk`, `wd_collect`, `wd_ipc1`,
# `wd_cells`, `wd_subj`, `wd_extra`). The premise came from the decomposition plan's §2.3, was
# repeated by the step-7 brief and by the commit message, and no one ran `rg 'import arm7'` until a
# read-only critic did. Reproduce with: `rg -n 'import (arm7_flexibility|wd_acceptance)'`.
#
# AND THE CITATION WAS A MISREADING. §0.1 pt 5 governs whether a pattern defect earns A GUARD; it
# is not a licence to leave an instrument you just broke returning a wrong number. Its own text is
# *"Delete it, or accept the defect and write nothing"* -- and the draft wrote eleven lines while
# leaving the arm live in the runner. An unrepointed `arm7` reports all four branches identical
# because `take_kth` becomes an inert context manager: a FABRICATED NULL, which is precisely the
# §0.1 pt 4 failure ("a number without a control is not a measurement -- in either direction").

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
