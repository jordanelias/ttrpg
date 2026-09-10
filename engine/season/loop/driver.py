"""`engine/season/loop/driver.py` -- THE SEASON LOOP ITSELF. Step 9 of the decomposition.

`SeasonDriver` and the five module-level functions the loop uses around it: `stratum_of`,
`resolvable_verbs`, `as_scenes`, `sense`, `names_a_verb`, and the #353 source reader
(`_S353_CACHE`/`SOURCE_353_TEXT`) that `names_a_verb` asks.

⚠ THIS IS `loop/driver.py`, NOT `loop.py`. `engine/season/loop/` has been a PACKAGE since step 5
(`effects.py`, `predicates.py`), so a sibling `loop.py` would be shadowed by it and never import.

⚠ `sense()` IS HERE AND NOT IN `decision.py`, WHICH IS WHERE THE FIRST PLAN PUT IT.
`04_CODE_ARCHITECTURE.md:116` is explicit -- *"`sense()` called by the loop, never by the
decision"* -- and `:133` enumerates `decision/`'s four members without it. It takes a `World`,
and `decision.py` is the one module forbidden to name one (AX-2), so filing it there would have
violated the axiom in the same commit that created the island. `:158` grants `loop/deliberate`
the frozen World *"for `sense` only"*, which is this module.

WHOLE BODIES, NO DELEGATION. An earlier plan proposed leaving module functions in `shape.py` that
delegate here. Three tests read `SeasonDriver.witness`'s own source (`inspect.getsource`), one of
them a NEGATIVE assertion, so a delegating stub would fail two and silently vacate the third --
it would keep passing while covering nothing.

`shape.py` re-exports every name below, so `S.<name>` and the harness keep resolving until the
facade is deleted at step 10.
"""
from __future__ import annotations

import hashlib
import inspect
import itertools
import json
import random
import re
from typing import Any, Callable, Optional

from ..data import files
from ..data.fixtures import Fixtures, SITE_YIELD
from ..data.matrix import Step, WriteClass, matrix_row
from ..data.rosters import OBSERVATION_DEPOSIT_MODES, STRATA, WITNESS_CHANNELS
from ..data.requires import (
    LEDGER_DERIVED_STEMS, UNKNOWN, Verdict, binding_from_act, binding_of, evaluate,
)
from ..data.verbs import NO_PRECONDITION, VERB_TABLE, VerbRow
from ..gaps import (
    Collision, Forbidden, InstrumentDefect, NoProducer, Ungraded, Unowned, Unspecified,
)
from ..state.carriers import (
    Act, Candidate, Claim, Event, Office, Person, Proposition, Question, Record, Rung, Scene,
    Sensation, Site, StateChange, Tenure, View,
)
from ..state.ids import H, ROOT
from ..state.world import World
from ..epistemic import CHANNEL_PREDICATES, act_refs, claim_subjects, observers_for
from ..queries import cache, world_q
from ..queries.person_q import entrenchment
from ..queries.person_q import LedgerReader
from ..queries.world_q import WorldReader
from ..queries.world_q import occasioned_by, questions_for
from ..loop.effects import EFFECTS, effect_for
from ..loop.predicates import REQUIRES_PREDICATES, requires_predicate
from .. import decision
from ..decision import (
    aggregate_questions, agreement, align, assemble, body_band_penalty, budget,
    containing_rung_of, make_chooser, opening_set, operands_for, pack_scenes,
    person_side_eligible, stance_toward, standing_of, store_kind_of, urgency, view_ids,
)
from ..seam import (
    ContestError, Resolution, combat_degree, contest, contest_subsystem, degree_of,
    degree_ladder, ladder_error,
)
from ..trace_log import TRACE


def resolvable_verbs() -> frozenset:
    """The verbs the fold can actually carry through RESOLVE: no precondition, or a precondition
    some `REQUIRES_PREDICATES` entry evaluates.

    COMPUTED, NEVER LISTED. A caller narrowing an option set to these is not authoring a roster --
    it is asking the fold what it can execute, and the answer moves when `verb_table.yaml` or the
    predicate registry moves. W3 measured 12 of 32; this is that measurement as a function, so a
    probe can report both numbers instead of hardcoding either.

    THREE GATES: a precondition the fold can evaluate, an effect for whatever it writes, and NOT
    routing to a contest — a contesting verb's resolution is the seam's, and the seam does not
    return yet (`H-31`, `W7`)."""
    out = set()
    for v, row in VERB_TABLE.items():
        # ⚠ BOTH GATES, NOT JUST THE PRECONDITION. The first version checked `requires:` alone and
        # called `create_record` resolvable -- it has no precondition and no EFFECT, so the fold
        # admits it and then raises `Unspecified` on "Part E does not say WHAT VALUE". A caller
        # narrowing to "what the fold can execute" got a set the fold could not execute, and the
        # gap only surfaced when `W17`'s packing started attempting more verbs per season. Found
        # by running the corpus, not by reading it.
        # ⚠ `requires_typed` IS THE FIRST OF THE THREE, AND ONE OWNER IS WHY IT IS HERE. This
        # question -- *can the fold evaluate this precondition* -- is the same question `_fold`
        # asks two hundred lines down, and leaving it reading only `REQUIRES_PREDICATES` would
        # give the two sites different answers for every typed verb (§8: the rule lives once).
        gated = ((row.requires or "").strip() in NO_PRECONDITION
                 or row.requires_typed is not None
                 or v in REQUIRES_PREDICATES)
        effected = not row.writes or v in EFFECTS
        # ⚠ AND A THIRD GATE: A VERB THAT CONTESTS DOES NOT TAKE THE EFFECT PATH AT ALL.
        # `ARCHITECTURE_V2.md:394` — *"`contests: <prize>` — if set, ROUTES TO THE SEAM at
        # RESOLVE (§39)"* — so such a verb is executable only if the SEAM can return. It was
        # counted as executable only because the instrument read its own `EFFECTS` entry and never
        # read the column that says the effect is not the path. Jordan, 2026-09-02: *"you can't
        # just kill or wound imo."* Correct, and the design agreed at `:434` all along.
        #
        # ⚠ THE GATE'S OLD REASON IS NOW FALSE AND ITS NEW ONE IS NARROWER AND MEASURED. What
        # stood here said *"today `contest()` raises `Unspecified` at S39.4 before it returns
        # anything"*. That stopped being true for `the body` when the seam started CALLING
        # personal combat, and `W-E` (2026-09-04) closed the rest: the seam returns, `degree_of`
        # reads the band off the scene, and `_fold` executes all three branches. THE GATE STAYS,
        # ON A DIFFERENT AND CHECKABLE GROUND: a contested act needs a `subject` operand to name
        # the second claimant, and `operands_for` returns `{}` for an UNTYPED verb (`H-80`,
        # `H-94`) — `kill / wound`'s `requires` is `—`, so it is untyped. A computed
        # `kill / wound` would therefore reach the seam with ONE claimant, `combat_seam` would
        # return `PARTY-GAP`, and every case that produced one would become a whole-case
        # DESIGN-GAP. Admitting the verb here is `H-80`'s item, not this one, and the corpus
        # measures the difference: at the shipped fixtures no contested act arises from the loop,
        # which is why closing the seam moved ZERO bytes of the run artifacts.
        contested = bool(row.contests)
        if gated and effected and not contested:
            out.add(v)
    return frozenset(out)


# ⚠ `sense_subsistence_only(p, w, formula)` STOOD HERE AND W5 DELETED IT, on the evidence of its
# own proof. It was a SECOND non-decision function taking a `World` -- exactly what #353 `:634`
# permits only `sense()` to be -- and it had ZERO CALLERS anywhere in the tree. It survived
# because nothing checked SIGNATURES: the file's dead-code guard looks for switched-off rules
# (`if False`), not for unused functions, and every claim about "the ONE" was made in prose.
# `test_w5_sense_is_still_the_only_world_taking_non_decision_function` walks the AST for any
# person-side function annotated with a `World` and found this on its first run. Recovered at
# `git log -S sense_subsistence_only` if the injected-formula helper is ever wanted again.


# ===========================================================================
# PART III -- THE SEASON LOOP
# ===========================================================================


# ===========================================================================
# THE FOLD -- W3. ONE `resolve`, READING `verb_table.yaml`.
#
# What was here: `resolve(acts, effect, ...)`, where `effect` was a CALLER-SUPPLIED LAMBDA that
# inspected `a.verb` and returned Events. Every probe wrote its own. That is defect `D20` and it
# is §27.2's "no second resolver" arriving as a PARAMETER rather than as a function -- a resolver
# per caller, each free to disagree with the others about what a verb does.
#
# THE FOLD, per §E2: eligibility -> `requires` AGAINST THE WORLD THE PREDECESSORS LEFT -> each




# Verbs the probe corpus uses that #353 does not name AS A VERB — checked, not assumed: the
# strings `take_seat`, `press_claim`, `raid` and `confer_authority` appear ZERO times in its 2,067
# lines, and `fight`/`refuse`/`do`/`act` appear only as ordinary English. They are the caller's
# inventions and the fold says so, rather than charging them to the design. Register row H-64.



class SeasonDriver:
    """S23. Six steps, four barriers. DELIBERATE is a MAP, not a barrier; CENSUS SHARES
    WITNESS'S JOIN. S40.3/S44.3: NO CONTAINER GETS A CLOCK -- there is exactly one `season()`."""

    def __init__(self, w: World):
        self.w = w
        # OBSERVATION ONLY, and the distinction matters. Six probes used the removed `effect` hook
        # to record which acts reached RESOLVE and in what order. That is a thing to WATCH, not a
        # thing to DECIDE, and giving it back as a resolver parameter is how the second resolver
        # returns. This list is appended by the fold and read by nobody inside it.
        self.resolved: list[Act] = []
        # ⚠ RESOLVER-SIDE, AND CUMULATIVE — like `resolved`, which is also never reset. The
        # Scene is the budgeted unit and carries the `occasion`, so the fold can name what
        # occasioned an act. No person-side Query reaches it, exactly as none reaches `resolved`.
        # It is NOT season-local: see the note at the `_fold` call site for why R3 depends on
        # that, and do not "fix" it into one.
        self.scenes: dict = {}
        # Event id -> the Act that emitted it. See the note at the `_fold` call site.
        self.act_of: dict = {}







    # -- one season --------------------------------------------------------
    def season(self, choose, question, subsistence,
               actorless: Optional[list[Event]] = None,
               contest_max_depth: Optional[int] = None) -> dict:
        w = self.w
        w.draw = 0                 # S33: the draw ordinal is per-TICK, so replay is exact
        self.calendar()
        matter_events = self.matter(actorless)
        acts = self.deliberate(choose, question, subsistence)
        events = self.resolve(acts, contest_max_depth)
        for e in events:
            w.log.append(e)                  # S19.5 -- ONE LOG, NOT TWO
            TRACE.event(e.id, e.kind, e.causes)
        deposits = self.witness(matter_events + events)
        self.census()
        w.tick += 1
        return dict(acts=len(acts), events=len(events) + len(matter_events),
                    deposits=deposits, hash=w.content_hash())

# ---------------------------------------------------------------------------
# THE SIX STEPS, BOUND BACK ONTO THE CLASS (unit L5, ED-IN-0206).
#
# `04_CODE_ARCHITECTURE.md` §A.2:134 -- *"loop/  driver + six steps. The driver is the ONLY
# constructor of write tokens."* -- and the §A.2 table gives each of the six its own owned state,
# its own `emits`, and its own token. They were methods on this class; each body now lives in its
# own module and is BOUND HERE.
#
# ⚠ **BOUND, NOT DELEGATED, AND THE DIFFERENCE IS LOAD-BEARING.** `SeasonDriver.witness` IS
# `witness.witness` after this line runs, so `inspect.getsource(SeasonDriver.witness)` returns the
# MOVED BODY. Eight tests read a step's source that way -- `test_d2` looks for `driver="Event"`,
# `test_d9b` pins the eviction comparator string, and
# `test_witness_writes_no_belief_and_no_conviction` is a PURE NEGATIVE assertion. A delegating stub
# would fail the first two and SILENTLY VACATE the third, which is why step 9 of the decomposition
# refused to delegate and why this does not either. Step 5 established the technique when
# `class Query` bound `world_q`'s functions as staticmethods.
#
# ⚠ `self.<step>()` IS UNCHANGED AT EVERY CALL SITE. `season()` calls all six through `self`, so the
# binding is what keeps those six calls resolving without editing one of them.
# ---------------------------------------------------------------------------
from .calendar import calendar                                            # noqa: E402
from .census import census                                                # noqa: E402
from .deliberate import deliberate                                        # noqa: E402
from .matter import matter                                               # noqa: E402
from .resolve import _apply_write, _eligible, _fold, _occasion_ids, resolve  # noqa: E402
from .witness import witness                                              # noqa: E402

SeasonDriver.calendar = calendar
SeasonDriver.matter = matter
SeasonDriver.deliberate = deliberate
SeasonDriver.resolve = resolve
SeasonDriver.witness = witness
SeasonDriver.census = census
# RESOLVE's own machinery, bound for the same reason: `_fold` reaches all three through `self`, and
# two source-scanning guards read `_apply_write`'s and `_fold`'s spans by name.
SeasonDriver._eligible = _eligible
SeasonDriver._occasion_ids = _occasion_ids
SeasonDriver._fold = _fold
SeasonDriver._apply_write = _apply_write
