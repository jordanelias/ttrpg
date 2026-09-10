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

from engine.season.data.verbs import VERB_TABLE
from engine.season.loop.driver import resolvable_verbs

# ⚠ `S` IS A COMPATIBILITY SHIM, NOT THE FACADE COMING BACK (step 10, ED-IN-0203).
# `engine/season/shape.py` was DELETED at step 10; seventeen files in this frozen sweep tree do
# `from sweep_core import S` and read ~35 names off it. Rewriting all seventeen would be a large
# edit to a set of instruments whose committed outputs are the record of a finished measurement,
# so the alias is rebuilt here, over the real owner modules, instead.
#
# ⚠ READS ONLY. Assigning through this object rebinds THE SHIM, never the owner, so a spy
# installed as `S.<name> = ...` would be a silent no-op. The three chains that do that
# (`pack_scenes`, `belief_contradicts`, `questions_for`) name their owner module directly --
# `PS` (= `season.decision`) since steps 7-8, and `DRV` (= `season.loop.driver`) since step 10.
# Do not add a fourth without giving it the same treatment.
import types as _types
from engine.season import decision as _dec, epistemic as _epi, seam as _seam
from engine.season.data import fixtures as _fx, matrix as _mx, requires as _req, rosters as _ros, verbs as _vb
from engine.season.loop import driver as _drv
from engine.season.queries import readers as _rd, world_q as _wq
from engine.season import gaps as _gaps
from engine.season.state import carriers as _car, ids as _ids, world as _wld

S = _types.ModuleType("sweep_core.S")
S.__doc__ = "read-only aggregate over season's owner modules; see the note in sweep_core.py"
for _m in (_gaps, _ids, _car, _wld, _ros, _mx, _req, _vb, _fx, _wq, _rd, _epi, _dec, _seam, _drv):
    for _k in dir(_m):
        if not _k.startswith("__"):
            setattr(S, _k, getattr(_m, _k))
del _m, _k

DRV = _drv                                              # for rebinds whose reader lives in the loop
from engine.season.harness import corpus_run as C       # noqa: E402
from engine.season.harness import run_cases as R        # noqa: E402
from engine.season.seam.wrappers import combat as CS   # noqa: E402
# ⚠ `combat_seam.py` MOVED to `seam/wrappers/combat.py` at unit L2 (ED-IN-0206): `04:135` and
# §A.2's `seam/wrappers/*` row put one wrapper per deferred subsystem there. The alias `CS` is
# unchanged, so every arm reading `CS.<name>` is unaffected.
from engine.season.decision import choose as PS_CHOOSE    # noqa: E402
from engine.season.decision import options as PS_OPTIONS  # noqa: E402

# ⚠ TWO ALIASES, AND THE SPLIT IS THE WHOLE POINT (L1, ED-IN-0206). `season.decision` IS A PACKAGE
# as of unit L1: `04_CODE_ARCHITECTURE.md:1046` requires a DIRECTORY so the AX-2 isolation scan can
# match by path. A bare name resolves in ITS OWN module's globals, so an alias that names the
# PACKAGE reaches neither reader: `make_chooser` calls `pack_scenes` bare and lives in
# `decision/choose.py`; `opening_set` reads `belief_contradicts` bare and lives in
# `decision/options.py`. `PS` was one alias for one flat module and is replaced by `PS_CHOOSE` and
# `PS_OPTIONS`, each named for the module it IS -- rebinding the package would not raise, it would
# report every branch identical, which is the fabricated null `CLAUDE.md` §0.1 pt 4 calls the worse
# direction. The paragraph below is the step-7 record and still explains WHY a rebind must reach
# the reader's own namespace.
#
# ⚠ `PS` WAS THE ONE ALIAS THE STEP-7 DECOMPOSITION ADDED HERE (ED-IN-0203). `pack_scenes` moved
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
    return {v: r for v, r in VERB_TABLE.items() if getattr(r, "contests", "")}


def foldable() -> set:
    return set(resolvable_verbs())


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
