"""`season.loop.driver` -- `SeasonDriver` and `season()`.

`04_CODE_ARCHITECTURE.md` §A.2:134 -- *"loop/  driver + six steps. The driver is the ONLY constructor
of write tokens."* This module is the DRIVER half. The six steps are `loop/{calendar,matter,
deliberate,resolve,witness,census}.py` and are **bound onto the class at the foot of this file**, not
delegated to -- `SeasonDriver.witness` IS `witness.witness`, so `inspect.getsource` reaches the real
body and the eight tests that read a step's source keep working. See the note above the bindings.

⚠ **THIS DOCSTRING WAS STALE THE MOMENT L5 LANDED AND SAID SO FOR A DAY.** It listed `stratum_of`,
`as_scenes`, `sense`, `names_a_verb` and `SOURCE_353_TEXT` as living here -- they moved to
`resolve.py` and `deliberate.py` in L5's second cut, to break a real `driver <-> deliberate <->
resolve` import cycle -- and it still promised that *"shape.py re-exports every name below … until
the facade is deleted at step 10"*, of a file step 10 deleted. `resolvable_verbs` is the one module
function that stayed, because its callers are all outside `loop/`.

⚠ **THE IMPORT LIST BELOW IS WIDER THAN THIS MODULE USES**, and that is load-bearing rather than
untidy: `proposals/2026-09-04-degree-sweep/sweep_core.py` builds a read-only `S` aggregate over the
package's owner modules so a frozen measurement's `S.<name>` keeps resolving. ⚠ It is ALSO how a dead
import can make a rebind silent -- `questions_for` sat here unused, so
`wd_extra.py`'s `DRV.questions_for = qspy` went on succeeding while reaching nothing after
`deliberate` moved. Found by the Fable gate on Arc 1; the name is gone and the spy names
`loop.deliberate`. **A name kept here for the aggregate must not also be a name something rebinds.**
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
    Sensation, Site, StateChange, Tenure, View, subject_of,
)
from ..state.ids import H, ROOT
from ..state.world import World
from ..epistemic import CHANNEL_PREDICATES, act_refs, claim_subjects, observers_for
from ..queries import cache, world_q
from ..queries.person_q import entrenchment
from ..queries.person_q import LedgerReader
from ..queries.world_q import WorldReader
from ..queries.world_q import occasioned_by
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
        #
        # ⚠⚠ **`U1` REPLACED `not contested` WITH A MANIFEST-DERIVED TEST, AND WITHOUT THAT
        # AMENDMENT `U1`'s OBSERVABLE COULD NOT OCCUR.** The bare refusal is the right answer to
        # the question *can the seam return* only while the answer is no for everything. The moment
        # a verb declares `contests:` on a prize a provider IS registered for, refusing it here
        # would drop it out of every chooser's candidate set — every corpus driver narrows to this
        # set — so the unit would move R-05's executing count DOWN and its controls would pass
        # trivially.
        #
        # THE TWO CLAUSES ARE THE GATE'S OWN GROUNDS, READ FORWARD:
        #   * **a provider is registered for the prize.** `manifest.has(role, module)` asks the
        #     CODE, not the data — a roster row may name a module the contracts file declares and
        #     nothing may have registered a callable for it, which is `mass_battle` today. This is
        #     the same resolution-by-declaration the rest of the unit is built on, and it keeps one
        #     owner for the question rather than adding a fourth.
        #   * **the verb is typed.** The paragraph above is the reason and it is unchanged:
        #     `operands_for` returns `{}` for an untyped row, so a computed contested act would
        #     reach the seam with ONE claimant and every case producing one would become a
        #     whole-case DESIGN-GAP.
        # `kill / wound` still fails the second clause — its `requires` is `—` — which is what
        # keeps Jordan's *"you can't just kill or wound imo."* true. Admitting it is `H-80`'s item.
        #
        # ⚠ FALSIFIER FOR THE AMENDMENT SPECIFICALLY: delete the `@provider("contest",
        # "sigma_leverage")` registration from `seam/wrappers/sigma.py` and any verb contesting a
        # `sigma_leverage` prize drops back out of this set — the first clause going false with the
        # data unchanged, which is the whole point of asking the code.
        contested = bool(row.contests)
        resolvable_contest = False
        if contested:
            # ⚠ THROUGH `manifest.resolve`, NOT BY RE-READING THE ROSTER. This planted the literals
            # `"contest_subsystems"` / `"prizes"` here and re-implemented the row unwrap, which
            # `registry.py`'s own comment forbids in as many words — *"THE ROLE NAMES ARE DATA, NOT
            # A LITERAL HERE ... the map exists so `resolve` does not branch on a role's name."*
            # Two readings of one row's `provider:` is how a role added to `_ROLE_ROSTERS`, or a new
            # case in the row shape, silently stops reaching the verb set.
            from ..manifest import has as _provider_registered, resolve as _resolve_row
            _mod = (_resolve_row("contest", row.contests) or {}).get("provider")
            resolvable_contest = (bool(_mod) and _provider_registered("contest", _mod)
                                  and row.requires_typed is not None)
        if gated and effected and (not contested or resolvable_contest):
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
        # ⚠ **THE MANIFEST'S ROWS ARE VALIDATED HERE, BECAUSE THIS IS THE ONE PLACE EVERY RUN
        # PASSES.** `04:1031`'s done-condition is *"a misspelled manifest row fails at boot naming
        # the row"*, and unit L4 built `manifest.check_rows()` for it and wired it into
        # `World.boot()` -- which NOTHING ON A RUN PATH CALLS. `headless`, `corpus_run` and
        # `run_cases` never boot a world; only two probes and three tests do. So the behaviour
        # existed and did not EXECUTE, which `CLAUDE.md` §0.2 says is not done. Found by the Fable
        # gate on Arc 1.
        #
        # ⚠ IT IS `check_rows()` AND NOT `check_roles()`, AND THE SPLIT IS FORCED RATHER THAN
        # CHOSEN. `check_roles` needs `w.manifest`, which is populated by exactly one probe and is
        # EMPTY in every real run -- calling it here would raise `NoProducer` on every season.
        # `check_rows` validates the REGISTRY, needs no manifest, and is the half `04:1031` names.
        # The roles half stays on `World.boot()` for the callers that have a manifest to check.
        from ..manifest import check_rows
        check_rows()
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
        # ---------------------------------------------------------------------
        # `U2` / `R-03` — THE SCENE TICK'S OWN STATE, AND ALL OF IT LIVES HERE.
        #
        # ⚠ `D-21`: THE ROUND INDEX IS A DRIVER LOCAL, NEVER A CARRIER FIELD. `Claim.round` is the
        # single exception and it is a different thing — a fact about WHEN a claim landed, which a
        # later deliberation reads. Everything below is a fact about where the LOOP is, and a
        # `round` on `Act`, `Event` or `World` would make it world state and put a fourth clock in
        # the model. U2's falsifier (d) is the AST scan that holds this.
        #
        # ⚠ SEASON-LOCAL, UNLIKE `resolved` / `scenes` / `act_of` ABOVE, and the asymmetry is the
        # point rather than an oversight: those three are the fold's cumulative record and R3
        # depends on them crossing seasons, while a scene budget, a queue of chosen-but-unrun
        # scenes and a "when did this person last deliberate" stamp all reset at the season
        # boundary by definition. `season()` clears them.
        # ---------------------------------------------------------------------
        self.round: int = 0
        # Scenes a person CHOSE and the driver has not released yet. The person's own triage,
        # held rather than re-asked — see `deliberate` for why re-asking is the defect.
        self._queued: dict = {}
        # Scene-action COST each person has spent this season, against `budget(p, v, ...)`.
        self._spent: dict = {}
        # `(tick, round)` of each person's last deliberation — `questions_for`'s `since`.
        self._deliberated_at: dict = {}
        # The fingerprint of everything `questions_for` and `person_side_eligible` read for a
        # person, as of their last deliberation. Unchanged ⇒ their candidate set is identical by
        # construction, so the driver releases their next chosen scene rather than re-deriving it.
        self._inputs: dict = {}
        # ⚠ WHAT `_drop_what_was_already_done` READS, AND IT IS THE REALISED SET RATHER THAN THE
        # ATTEMPTED ONE — which is the whole of a defect this unit's adversarial pass found. A pair
        # enters here only after the fold has run and only when the act's Event was not one of its
        # row's `emits_on_refusal` kinds. Recording the ATTEMPT instead barred a refused act from
        # ever being retried, including in a later round whose world had made its precondition
        # true — the exact channel R-03 exists to open, closed by the filter meant to protect the
        # season's variety.
        # ⚠⚠ **THERE WAS A SECOND SET, `_attempted`, AND IT WAS WRITTEN EVERY ROUND AND READ BY
        # NOTHING.** Its comment claimed both were live; a `/simplify` pass proved otherwise. The
        # split it described is real and survives — it is the difference between what the budget
        # was spent on and what may be retried — but only ONE side of it was ever consulted, so
        # keeping the other was carrying a set the code did not use behind a comment that said it
        # did. Deleted; if the attempted set is ever genuinely needed, it comes back with its
        # reader in the same commit.
        self._realised: dict = {}







    # -- one season --------------------------------------------------------
    def season(self, choose, question, subsistence,
               actorless: Optional[list[Event]] = None,
               contest_max_depth: Optional[int] = None) -> dict:
        """`U2` / `R-03`: **a season is R ROUNDS, and MATTER and CALENDAR are not among them.**

        R-03 reads *seasons must tick scene-by-scene, so what occurs after one scene can impact
        the next scene*. Before this, DELIBERATE ran once, RESOLVE once and WITNESS once — every
        scene for every person was flattened into ONE `acts` list before RESOLVE ever ran, so
        nothing that happened in one scene could reach a later scene inside the same season. The
        only boundary was season-to-season.

        ⚠ **MATTER AND CALENDAR STAY ONCE PER SEASON, AND THAT IS A LAYER-1 CONSTRAINT RATHER THAN
        A PERFORMANCE CHOICE.** `01_AXIOMS.md:151` names AX-5's three motions — *"MATTER, BODIES,
        AND THE FADING OF MEMORY"* — as seasonal, and `04 §C.1:504`'s barrier 1 with D-17/D-21 make
        a docket that formed five times a season A FOURTH CLOCK. **Rounds subdivide ACTS, not
        matter.** So the wear, the decay and the calendar tick once and the scene tick runs inside
        them.

        ⚠ **`w.tick` ADVANCES ONCE (D-45, `04:979`), AND `w.draw` RESETS ONCE.** The round is not a
        tick: ids stay derived from `(seed, tick, subject, purpose)` and the round enters through
        `purpose`, which is what `04 PART D row 35` requires of a new draw (*no counter, no
        service*). U2's falsifier (d) is an AST scan for exactly one assignment to `w.tick` in this
        module.

        ⚠ **THE FREEZE IS PER ROUND.** S26.2 freezes the world from the end of MATTER to the start
        of RESOLVE, and RESOLVE thaws it (`resolve.py`, `w.frozen = False`). With one pass that was
        one freeze; with R rounds each round re-freezes before its DELIBERATE, which is the same
        rule applied R times rather than a second rule.

        ⚠ **WITNESS RUNS PER ROUND AND MATTER'S EVENTS ARE WITNESSED ONCE.** A deposit that only
        landed at the end of the season could not reach a later round's deliberation, which is the
        whole channel R-03 asks for. MATTER's events are seasonal, so they join round 0's fan-out
        and no other — carrying them into every round would deposit one wear five times.

        ⚠ **THE CONTROL IS THE `scene_budget = 1` ARM, AND THE FIRST WRITING OF THIS DOCSTRING
        NAMED THE WRONG ONE.** It read that `H-124`'s `scenes_per_round = 5` gives every person
        their whole season in round 0 and finds them spent in rounds 1..4, which IS the one-pass
        loop. Measured at `build_world(0)`, 2 seasons, it is not: `claim.deposited` 50 -> 53,
        `claim.decayed` 21 -> 24, `finding.made` 2 -> 3. A person whose triage leaves budget
        UNSPENT empties their queue with remainder left, so a later round asks them again and they
        spend it — where the one-pass loop simply lost it. What DOES reproduce the pre-tick season
        is ONE ROUND: at `scene_budget = 1` the act multiset and the Event-kind multiset are
        identical to the pre-`U2` run, and the content hash moves only by `Claim` gaining `round`.
        That arm is the one-pass loop reproduced THROUGH this code path rather than around it."""
        w = self.w
        # ⚠⚠ **THE DEPTH CAP IS THE CALLER'S AND THE DRIVER MUST NOT FILL IT IN. `U2` ADDED A
        # FALLBACK HERE AND IT WAS WRONG; THE REGISTER ROW IS WHAT OVERTURNED IT.**
        # The fallback read `contest_max_depth = w.fixtures.get("contest_max_depth")` when the
        # caller passed none, argued from §8's *the rule lives once*, and reasoned that `H-87` is a
        # declared, sited, swept row rather than an invented number — so reading it here could not
        # be the default S39.3 refuses. **`H-87` says otherwise, in its own fields.** Its `owner:`
        # is *"the harness (the caller of `resolve`), per S39.3"* and its `site:` is *"Fixtures
        # contest_max_depth — read by `headless.run` AND PASSED TO `SeasonDriver.season` for every
        # RESOLVE"*. The row names the call site as the reading place and the driver as the
        # receiver. A driver that reads it is not obeying the row, it is relocating it.
        # ⚠ AND S39.3's REFUSAL IS ABOUT A DECIDER, NOT ONLY ABOUT A NUMBER. `H-87`'s cite: *"That
        # refusal is CORRECT and it is the design working; what was missing is a caller who
        # decided."* Filling the cap in here means no caller ever decides again — the refusal
        # becomes unreachable and the guard that proves it
        # (`test_d9c_max_depth_has_no_default_anywhere`) goes green on a design that no longer
        # holds. §8 does not apply: reading one registry row from several call sites is not
        # re-implementing a rule, and the row's `site:` is where it is read.
        # ⚠ THE COST IS REAL AND WAS THE REASON FOR THE FALLBACK, SO IT IS PAID RATHER THAN
        # ARGUED AWAY: once `U1` gave `tell` a `contests:`, every caller whose world can reach a
        # contest needed a cap. MEASURED 2026-09-11: removing the fallback took the suite from 8
        # failures to 17, and the seventeen resolve to SEVENTEEN CALLERS THAT HAD NOT DECIDED.
        # Each now passes `contest_max_depth=<world>.fixtures.get("contest_max_depth")`, which is
        # exactly the shape `H-87`'s `site:` describes.
        w.draw = 0                 # S33: the draw ordinal is per-TICK, so replay is exact
        # `U2`: season-local. See `__init__` for why these four reset and the three above it do not.
        self.round = 0
        self._queued, self._spent, self._deliberated_at = {}, {}, {}
        self._inputs, self._realised = {}, {}
        self.calendar()
        matter_events = self.matter(actorless)
        rounds = int(w.fixtures.get("scene_budget"))
        n_acts, n_events, deposits = 0, len(matter_events), 0
        pending_matter = list(matter_events)
        for r in range(rounds):
            self.round = r
            # S26.2 again, not a second rule: RESOLVE thaws, so each round re-freezes before its
            # own DELIBERATE. MATTER did the first one.
            w.frozen = True
            acts = self.deliberate(choose, question, subsistence)
            events = self.resolve(acts, contest_max_depth)
            # ⚠⚠ **WHAT WAS REALISED, AS OPPOSED TO WHAT WAS ATTEMPTED — AND IT CAN ONLY BE KNOWN
            # HERE, AFTER THE FOLD.** `deliberate` records an attempt at RELEASE, because that is
            # when the scene-action is spent and the budget does not care how it went. Whether the
            # act DID anything is the fold's answer, and `_drop_what_was_already_done` must read the
            # second: an act attempted and REFUSED in round 0 must be retryable in round 3, because
            # a later round's world may have made its precondition true. That is R-03's own channel,
            # and recording the attempt directly closed it.
            # ⚠ A REFUSAL IS THE ROW'S OWN `emits_on_refusal` KIND, WHICH IS THE ONLY DECLARATION
            # OF WHAT A REFUSAL LOOKS LIKE (§E2: *failure emits, never raises*). An act that emitted
            # nothing at all — eligibility declined before the fold reached the table — is not
            # promoted either, for the same reason: nothing happened.
            _refused_acts = set()
            _acted = set()
            for e in events:
                a = self.act_of.get(e.id)
                if a is None:
                    continue
                _row = VERB_TABLE.get(a.verb)
                if _row is not None and e.kind in (_row.emits_on_refusal or ()):
                    _refused_acts.add(a.id)
                else:
                    _acted.add(a.id)
            for a in acts:
                if a.id in _acted and a.id not in _refused_acts:
                    _subj = subject_of(a)
                    if _subj:
                        self._realised.setdefault(a.actor, set()).add((a.verb, _subj))
            for e in events:
                w.log.append(e)              # S19.5 -- ONE LOG, NOT TWO
                TRACE.event(e.id, e.kind, e.causes)
            # MATTER's events are seasonal and join the FIRST round's fan-out only; the alternative
            # deposits one wear once per round, which is the fourth clock this docstring refuses.
            deposits += self.witness(pending_matter + events)
            pending_matter = []
            n_acts += len(acts)
            n_events += len(events)
        self.census()
        w.tick += 1
        # ⚠ `rounds` IS REPORTED BECAUSE THE TICK IS OTHERWISE INVISIBLE IN EVERY ARTIFACT `U2`
        # PRODUCES. The unit reshaped a season into R rounds and no observable said so: the
        # summary read `acts/events/deposits`, all of which a one-pass season also produces, and
        # `--log` prints `(kind, subject, causes)` per Event. A reader could not tell a ticked
        # season from a flat one by looking at the output, which is §0.2's *something ran it*
        # missing its *something*.
        # ⚠ AND NO EVENT CARRIES A ROUND, WHICH IS WHY THIS IS A SEASON-LEVEL FIGURE AND NOT A
        # COLUMN IN `--log`. `D-21` keeps the round index a DRIVER LOCAL; `Claim.round` is the one
        # carrier field `U2` added, because a claim's round is read by `questions_for`'s `since`.
        # Stamping Events too would be a second carrier for a fact nothing reads — the dead-carrier
        # defect — so the artifact reports the COUNT of rounds the season ran and stops there.
        return dict(acts=n_acts, events=n_events, rounds=rounds,
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
