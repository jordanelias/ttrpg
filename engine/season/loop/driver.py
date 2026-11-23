"""`season.loop.driver` -- `SeasonDriver` and `season()`.

`04_CODE_ARCHITECTURE.md` §A.2:134 -- *"loop/  driver + six steps. The driver is the ONLY constructor
of write tokens."* (AMENDED 2026-09-28, `ED-IN-0279` clause (a), to SEVEN.) This module is the DRIVER
half. The seven steps are `loop/{calendar,matter,deliberate,resolve,encounter,witness,census}.py`; each
is **bound onto the class at the foot of this file**, not delegated to -- `SeasonDriver.witness` IS
`witness.witness`, so `inspect.getsource` reaches the real body, which the tests that read a step's
source rely on.

The driver mints the write tokens (`mint_token`, one per barrier, handed to the step and never kept),
binds the seven steps onto `SeasonDriver` and owns `resolvable_verbs`.
"""
from __future__ import annotations

from typing import Any, Optional

from ..data import load_all
from ..data.matrix import WriteClass
from ..data.verbs import VERB_TABLE, opportunity_key
from ..gaps import Forbidden
from ..state.carriers import Act, Event, subject_of
from ..state.gate import Token
from ..state.world import World
from ..queries import world_q
from ..queries.world_q import questions_for
# `EFFECTS` and `REQUIRES_PREDICATES` are read below; importing these two modules is also what
# registers the `@effect_for` bodies and the `@requires_predicate` entries.
from ..loop.effects import EFFECTS
from ..loop import effects_combat
from ..loop.predicates import REQUIRES_PREDICATES
from .. import seam  # noqa: F401  -- registers the providers: importing `seam.wrappers` is what does it
from ..seam.wrappers import sigma
from ..trace_log import TRACE


def mint_token(w: World, wclass: WriteClass) -> Token:
    """`G2` / `04:199` -- **THE ONE CONSTRUCTOR OF A WRITE TOKEN.** *"`Token := (write_class, tick)`
    -- constructed by loop/driver and NOWHERE ELSE."* `04:206` grades that MECHANICAL -- *"a test
    asserts `Token(` appears in `loop/driver` only"* -- and `tests/test_g2_token.py` is that test.

    `SeasonDriver.season` calls this once per barrier and hands the result to the step as a
    parameter, which is `04 §C.1` line for line: `cal = Token(CALENDAR,t); calendar(w,cal); drop`.
    DELIBERATE is called with none.

    ⚠ IT IS A MODULE FUNCTION, NOT A `SeasonDriver` METHOD, AND THAT IS DELIBERATE. The seven steps
    are BOUND onto `SeasonDriver` (foot of this file), so a method here would be one `self.` away from
    `deliberate`'s body. A module function is reachable only by importing it, and the same scan
    refuses any game module under `engine/season/` other than this one that calls it.

    ⚠ APPARATUS CALLS IT TOO, AND SAYS SO. `harness/probes.py` and the tests stand in for the driver
    at a synthetic barrier -- `w.step = Step.RESOLVE` by hand, then a write -- and they mint here
    rather than constructing a `Token` themselves, so the construction stays in this file. The scan
    allows `harness/` and `tests/` to CALL this and nothing outside this file to CONSTRUCT one."""
    return Token(wclass, w.tick)


def resolvable_verbs() -> frozenset:
    """The verbs the fold can actually carry through RESOLVE: a precondition the fold can evaluate
    (`VerbRow.precondition_evaluable`: none, a typed cell, or a `REQUIRES_PREDICATES` entry).

    COMPUTED, NEVER LISTED. A caller narrowing an option set to these is not authoring a roster --
    it is asking the fold what it can execute, and the answer moves when `verb_table.yaml` or the
    predicate registry moves.

    THREE GATES: a precondition the fold can evaluate, an effect for whatever it writes, and, for
    a verb that contests, a prize whose row names a provider and a typed row (the comment below)."""
    out = set()
    for v, row in VERB_TABLE.items():
        # BOTH GATES, NOT JUST THE PRECONDITION: `create_record` has no precondition and no EFFECT,
        # so checking `requires:` alone would count it, and the fold would then raise `Unspecified`.
        # `precondition_evaluable` is the question `_fold` asks, answered by one owner on `VerbRow`
        # (§8): a row it drops reaches this gate only if its `verb_table.yaml` row carries a
        # `requires_decline_note:`; `manifest.check_preconditions()` refuses every other such row at
        # `SeasonDriver` construction, naming it (plan position IN-41, `SM-11`).
        gated = row.precondition_evaluable(REQUIRES_PREDICATES)
        effected = row.effect_carried(EFFECTS)
        # A writing row with no effect reaches the exclusion above only if its `verb_table.yaml` row
        # carries an `effect_decline_note:`; `manifest.check_effects()` refuses every other such row
        # at `SeasonDriver` construction, naming it (refusal (a)) -- a CONTESTED row included,
        # because `loop/resolve.py::_contest` folds the seam's result through `EFFECTS`.
        # The third gate: a verb that contests ROUTES TO THE SEAM FIRST and folds what it returns
        # (`ARCHITECTURE_V2.md:394`, *"`contests: <prize>` -- if set, ROUTES TO THE SEAM at RESOLVE
        # (§39)"*), so it is executable only if the seam can return. Jordan, 2026-09-02: *"you can't
        # just kill or wound imo."*
        #
        # THE CLAUSES:
        #   * the prize's row names a provider -- `manifest.resolve("contest", prize)`'s `provider:`.
        #     There is no `manifest.has(role, module)` clause here: `manifest.check_contest_prizes()`
        #     refuses an unregistered provider at `SeasonDriver` construction, naming the prize, so
        #     such a clause could never be false. `tests/valoria/test_season_providers_are_registered.py`
        #     watches the refusal.
        #   * the verb is typed: a contested act needs a `subject` operand to name the second
        #     claimant, and `operands_for` returns `{}` for an UNTYPED verb (`H-80`, `H-94`). A
        #     computed `kill / wound` (`requires` is `—`, so untyped) would reach the seam with ONE
        #     claimant, `combat_seam` would return `PARTY-GAP`, and every case producing one would
        #     become a whole-case DESIGN-GAP. Admitting it is `H-80`'s item.
        #   * ⚠ v10 IN-12 step 5 (H-226 route (a) [ASSUMPTION; medium; Jordan to correct; revert:
        #     `row.requires_typed is not None` alone]): **OR the untyped row names `counterparty:
        #     subject`.** `decision/options.py::_operands` carries the referent on `subject` when the
        #     row names it as its counterparty, so the seam has its second claimant. NARROWED TO A
        #     ROW DECLARING A REGISTERED PREDICATE, because an untyped row with a precondition
        #     reaches here only through `REQUIRES_PREDICATES` (the first gate) and one with none
        #     would contest with no custody or party read at all.
        #   * B21.09 (VB-A commit A3) [ASSUMPTION; medium; Jordan to correct; revert: the two clauses above alone, under which a
        #     drawn `establish` leaves the chooser's verb set]: **OR the untyped row names NO counterparty and its prize's row
        #     names a room that hears it (`heard_by:`).** Such a contest has no second claimant to miss: the actor alone claims,
        #     the room the prize names is what stands opposite (`seam/wrappers/sigma.py::audience_of`), and the social roll
        #     opposes nobody at the untrained score (`roll.py::obstacle`, never absent). Narrowed to a registered predicate, as
        #     the clause above is. Today: `establish` (`a seat`) alone.
        #   * B21.14 (VB-C commit C3) [ASSUMPTION; medium; Jordan to correct; revert: the three clauses above alone, under which a
        #     drawn `confer` leaves the chooser's verb set]: **OR the prize's row names who stands opposite (`opposed_by:`).** The
        #     opponent is then read off the world by the prize (`loop/sides.py::sides_of`: the named seat's live holder), not off an
        #     operand the act must carry, so `confer` (whose `counterparty: to` is the conferee, not the opponent) has nothing to
        #     miss. Narrowed to a registered predicate, as above. Today: `a seat`'s rows -- `confer`, `revoke`, `succeed`, `establish`.
        contested = bool(row.contests)
        resolvable_contest = False
        if contested:
            # THROUGH `manifest.resolve`, NOT BY RE-READING THE ROSTER: `registry.py` forbids a
            # literal role name here -- *"THE ROLE NAMES ARE DATA, NOT A LITERAL HERE ... the map
            # exists so `resolve` does not branch on a role's name."* Two readings of one row's
            # `provider:` is how a new role or row shape silently stops reaching the verb set.
            from ..manifest import resolve as _resolve_row
            _prize = _resolve_row("contest", row.contests) or {}
            _mod = _prize.get("provider")
            resolvable_contest = bool(_mod) and (
                row.requires_typed is not None
                or (row.counterparty == "subject" and v in REQUIRES_PREDICATES)
                or (not row.counterparty and bool(_prize.get("heard_by")) and v in REQUIRES_PREDICATES)
                or (bool(_prize.get("opposed_by")) and v in REQUIRES_PREDICATES))
        if gated and effected and (not contested or resolvable_contest):
            out.add(v)
    return frozenset(out)


# ===========================================================================
# PART III -- THE SEASON LOOP
# ===========================================================================


class SeasonDriver:
    """S23. Six steps, four barriers. DELIBERATE is a MAP, not a barrier; CENSUS SHARES
    WITNESS'S JOIN. S40.3/S44.3: NO RUNG GETS A CLOCK -- there is exactly one `season()`."""

    def __init__(self, w: World):
        self.w = w
        # THE `data/` LOADERS BEHIND ONE ENTRY (`04:131`, *"the ONE loader"*). Every run constructs
        # a driver, so a loader's refusal (a `SystemExit` naming its row, or `Unspecified` for a lazy
        # file that is gone) fires here, first, rather than at the first world to read that file.
        # Idempotent; `data/__init__.py::load_all` has the rest.
        load_all()
        # THE MANIFEST'S ROWS ARE VALIDATED HERE, THE ONE PLACE EVERY RUN PASSES. `04 PART E
        # step 10`: *"a misspelled manifest row fails at boot naming the row"*. `check_rows()` and not
        # `check_roles()`: `check_roles` needs `w.manifest`, which is EMPTY in every real run, and
        # would raise `NoProducer` on every season. `check_rows` validates the REGISTRY and needs no
        # manifest; the roles half stays on `World.boot()` for callers that have one.
        #
        # PLAN POSITION `30` (A-25): THE REGISTRAR RUNS FIRST, THEN THE REFUSALS, EACH NAMING ITS
        # ROW. The registrar records every composition row carrying `entry:` in
        # `manifest.MODULE_ENTRIES`, resolving by string (never at import), and refuses (b) a
        # `verb:` naming no verb row and (d) an entry registered twice; it is idempotent. Then (c)
        # the contest roster, all three halves, and (a) a writing row with no effect and no
        # `effect_decline_note:` (and its converse), and -- plan position IN-41, `SM-11` -- (a)'s
        # precondition twin: a precondition nothing evaluates and no `requires_decline_note:` (and
        # its converse). `manifest/registrar.py` and `manifest/registry.py` hold the rules.
        from ..manifest import (
            check_contest_prizes, check_effects, check_graded_tasks, check_inquiry_modules,
            check_preconditions, check_rows, register_module_entries, require_entries,
        )
        register_module_entries(VERB_TABLE)
        # v9 IN-07: the host's declared needs, held against the table just filled -- the refusal a
        # deleted role-less row (a `query` or `step_call` no role roster names) meets in a fresh
        # process. The `query` entries `world_q` declares (E1, E4-E6, IN-52's `provision`), and the
        # step_calls MATTER calls (E2, E3).
        require_entries(world_q.QUERY_ENTRIES + sigma.QUERY_ENTRIES + effects_combat.QUERY_ENTRIES + MATTER_STEP_CALLS)
        check_rows()
        check_contest_prizes(VERB_TABLE)
        check_graded_tasks(VERB_TABLE)
        # v9 FI-02 + FI-03 (`SM-3`, `ED-FI-0002`): the `inquiry` role's rows -- provider registered, entry
        # agreeing with its composition row; the declaration that `fieldwork.find`'s row must exist.
        check_inquiry_modules(VERB_TABLE)
        check_effects(VERB_TABLE, EFFECTS)
        check_preconditions(VERB_TABLE, REQUIRES_PREDICATES)
        # `U5a_CORE_owed_edits` §B row 18: a season with no lap is not a season. The fixture's own refusal,
        # at construction (a boot refusal, never a raise in play), naming the fixture.
        if int(w.fixtures.get("scene_budget")) < 1:
            raise Forbidden(
                f"scene_budget is {w.fixtures.get('scene_budget')}, under one: a season with no lap deposits nothing",
                "loop/driver.py::SeasonDriver.__init__",
                needs="a `scene_budget` of at least one",
                law="a season with no lap is not a season (a loader-family refusal, at boot)")
        # OBSERVATION ONLY: the fold appends here and nothing inside it reads the list. It is a
        # thing to WATCH, not to DECIDE; giving it back as a resolver parameter is how a second
        # resolver returns.
        self.resolved: list[Act] = []
        # COMPANION SET, `ActStore._by_id`'s OWN SHAPE. `_fold` dedupes `resolved` by id -- a march
        # act reaches it once from RESOLVE's Declared fold and once more from ENCOUNTER's real fold --
        # and `resolved` is NEVER RESET across a campaign's `season()` calls, so a per-call scan would
        # make every act's fold O(N) over the run's total act count. `_resolved_ids` is maintained
        # alongside `resolved`, never read on its own, so the dedup check in `loop/resolve.py::_fold`
        # is a set membership test.
        self._resolved_ids: set = set()
        # H-465 (B10.06): `Fixtures scar_season_cap`'s tally, the (observer, element) pairs or observers `loop/resolve.py::_scar_witnesses` has
        # counted this tick. Driver scratch, not world state (never hashed); `season()` clears it where it resets `w.draw`. Unread at the control.
        self._scar_tally: set = set()
        # B09.16: THE DRIVER HOLDS NO SCENES. The Scene (the budgeted unit, carrying the `occasion`) is kept beside its
        # acts in `World.acts` (`ActStore.scene_of`), cumulative across seasons as R3 needs and surviving the driver.
        # Event id -> the Act that emitted it. See the note at the `_fold` call site.
        self.act_of: dict = {}
        # v9 FI-03 (`ED-FI-0002`): finding Event id -> `((trail event id, terms shown), ...)`, what the
        # `inquiry` role uncovered at RESOLVE (`loop/resolve.py`'s per-act bookkeeping, `seam.find_trail`);
        # WITNESS pops each entry when it deposits the find (`loop/witness.py`). `act_of`'s shape:
        # event-keyed, driver-owned, resolver-side, and read by no person-side Query. Unlike `act_of` it
        # does not accumulate: an entry lives from its lap's RESOLVE to that lap's WITNESS.
        self.findings: dict = {}
        # ---------------------------------------------------------------------
        # `U2` / `R-03` -- THE SCENE TICK'S OWN STATE, AND ALL OF IT LIVES HERE.
        #
        # `D-21`: THE LAP INDEX IS A DRIVER LOCAL, NEVER A CARRIER FIELD. `Claim.lap` is the
        # single exception, a fact about WHEN a claim landed, which a later deliberation reads.
        # Everything below is a fact about where the LOOP is; a `lap` on `Act`, `Event` or `World`
        # would make it world state and put a fourth clock in the model (U2's falsifier (d) is the
        # AST scan that holds this).
        #
        # SEASON-LOCAL, UNLIKE `resolved` / `act_of` ABOVE (and the Scene store in `World.acts`): those are the fold's
        # cumulative record and R3 depends on them crossing seasons, while a scene budget and a
        # "when did this person last deliberate" stamp reset at the season boundary by definition.
        # `season()` clears them.
        # ---------------------------------------------------------------------
        self.lap: int = 0
        # Scene-action COST each person has spent this season, against `budget(p, v, ...)`.
        self._spent: dict = {}
        # `(tick, lap)` of each person's last deliberation — `questions_for`'s `since`.
        self._deliberated_at: dict = {}
        # WHAT `_drop_what_was_already_done` READS: the REALISED set, not the ATTEMPTED one. An
        # opportunity KEY (`data/verbs.py::opportunity_key`: `(verb, subject)`, plus the row's
        # counterparty, `T4b`) enters here only after the fold has run and only when the act's
        # Event was not one of its row's `emits_on_refusal` kinds. Recording the ATTEMPT would bar a
        # refused act from ever being retried, including in a later lap whose world had made its
        # precondition true -- the channel R-03 exists to open. What the budget was spent on and what
        # may be retried are different sets; only the second is kept.
        self._realised: dict = {}

    # -- the question projection, built at barrier 2 -----------------------
    def _questions_at_barrier(self) -> dict:
        """`{person id: Question[]}` -- the per-person projection `04:976` (PART D row 41) says is
        built at barrier 2, and which DELIBERATE receives rather than reads off the World
        (`04:158`: it reads a frozen World "for `sense` only"; `04:154`: a decision may read
        `Question[]`). `since` is SINCE THIS PERSON LAST DELIBERATED (`U2`), exactly the argument
        DELIBERATE passed when it made this call itself."""
        w = self.w
        return {p.id: questions_for(w, p, self._deliberated_at.get(p.id))
                for p in w.persons.values()}

    # -- one season --------------------------------------------------------
    def season(self, choose, question,
               actorless: Optional[list[Event]] = None,
               contest_max_depth: Optional[int] = None,
               host: Optional[Any] = None) -> dict:
        """`U2` / `R-03`: **a season is R LAPS, and MATTER and CALENDAR are not among them.**

        R-03 reads *seasons must tick scene-by-scene, so what occurs after one scene can impact
        the next scene*. DELIBERATE, RESOLVE and WITNESS run once per lap, so what happens in one
        scene reaches a later scene inside the same season.

        ⚠ **MATTER AND CALENDAR STAY ONCE PER SEASON, AND THAT IS A LAYER-1 CONSTRAINT RATHER THAN
        A PERFORMANCE CHOICE.** `01_AXIOMS.md:151` names AX-5's three motions — *"MATTER, BODIES,
        AND THE FADING OF MEMORY"* — as seasonal, and `04 §C.1:504`'s barrier 1 with D-17/D-21 make
        a docket that formed five times a season A FOURTH CLOCK. **Laps subdivide ACTS, not
        matter.** So the wear, the decay and the calendar tick once and the scene tick runs inside
        them.

        ⚠ **`w.tick` ADVANCES ONCE (D-45, `04:979`), AND `w.draw` RESETS ONCE.** The lap is not a
        tick: ids stay derived from `(seed, tick, subject, purpose)` and the lap enters through
        `purpose`, which is what `04 PART D row 35` requires of a new draw (*no counter, no
        service*). U2's falsifier (d) is an AST scan for exactly one assignment to `w.tick` in this
        module.

        ⚠ **THE FREEZE IS PER LAP.** S26.2 freezes the world from the end of MATTER to the start
        of RESOLVE, and RESOLVE thaws it (`resolve.py`, `w.frozen = False`). With one pass that was
        one freeze; with R laps each lap re-freezes before its DELIBERATE, which is the same
        rule applied R times rather than a second rule.

        ⚠ **WITNESS RUNS PER LAP AND MATTER'S EVENTS ARE WITNESSED ONCE.** A deposit that only
        landed at the end of the season could not reach a later lap's deliberation, which is the
        whole channel R-03 asks for. MATTER's and CALENDAR's events are seasonal, so they join lap
        0's fan-out and no other — carrying them into every lap would deposit one wear five times.

        ⚠ **THE CONTROL IS THE `scene_budget = 1` ARM**: one lap, which is the one-pass loop
        reproduced THROUGH this code path rather than around it. (`H-124`'s `scenes_per_lap = 5`
        is not that arm: a person whose triage leaves budget UNSPENT empties their queue with
        remainder left, so a later lap asks them again.)

        ⚠ `host` (v10 REM-31, IN-46: the grid mode's suspension) IS THE PLAYABLE MODE'S ONE ARGUMENT
        (`queries/inputs.py::PlayHost`), and it reaches ENCOUNTER ALONE: RESOLVE is called without it, so
        the season can suspend at one step only, inside one provider call for one deferred act. `None` is
        AUTOMATED, every fight engine-decided. The suspension is a CALL-OUT: the lap's `acts`, `events`
        and `pending_matter` stay in this frame, and ENCOUNTER's token is minted ONCE, in the argument
        expression below, never kept, never re-minted on resume -- there is no resume but the decider's
        return. The draw ordinal resets once per tick (above) and the decider is handed no `World`, so by convention it
        consumes none (`test_rem31_grid_suspension.py::test_no_draw_and_no_mint_while_suspended`; its planted drawing decider is retired). `choose` -- a host's own callback included (`harness/play_surface.py`) -- runs inside
        DELIBERATE's per-person map, which must not depend on the order it visits persons
        (`loop/deliberate.py::deliberation_order`)."""
        w = self.w
        # ⚠⚠ **THE DEPTH CAP IS THE CALLER'S AND THE DRIVER MUST NOT FILL IT IN.** `H-87`'s
        # `owner:` is *"the harness (the caller of `resolve`), per S39.3"* and its `site:` is
        # *"Fixtures contest_max_depth — read by `headless.run` AND PASSED TO `SeasonDriver.season`
        # for every RESOLVE"*: the row names the call site as the reading place and the driver as
        # the receiver, so a driver that reads it relocates the row. S39.3's refusal is about a
        # DECIDER, not only a number (`H-87`'s cite: *"what was missing is a caller who decided"*);
        # a fallback here means no caller decides again and the refusal becomes unreachable
        # (`test_d9c_max_depth_has_no_default_anywhere`). §8 does not apply: reading one registry
        # row from several call sites is not re-implementing a rule. Every caller whose world can
        # reach a contest passes `contest_max_depth=<world>.fixtures.get("contest_max_depth")`.
        w.draw = 0                 # S33: the draw ordinal is per-TICK, so replay is exact
        w._departed.clear()        # H-206: per-tick scratch (`departed_from` answers only for its own tick)
        self._scar_tally.clear()   # H-465: the season's scar counts already taken (`_scar_witnesses`), per-tick scratch like the line above
        # `U2`: season-local. See `__init__` for why these reset and the three above it do not.
        self.lap = 0
        self._spent, self._deliberated_at, self._realised = {}, {}, {}
        # G2 / `04 §C.1`: ONE TOKEN PER BARRIER, MINTED HERE, PASSED IN, NEVER KEPT. Each is built
        # inline in the call so no local outlives its step -- the pseudocode's `drop` is the end of
        # the expression. DELIBERATE, below, is the one step called with none.
        calendar_events = self.calendar(mint_token(w, WriteClass.CALENDAR))
        matter_events = self.matter(mint_token(w, WriteClass.MATTER), actorless)
        laps = int(w.fixtures.get("scene_budget"))
        n_acts, n_events, deposits = 0, len(matter_events), 0
        # IN-29: CALENDAR's own Events (`date.fired`) are seasonal like MATTER's and ride the same
        # first-lap fan-out, in barrier order. `n_events` does not count them (it counts MATTER's
        # and each lap's); the log already holds these.
        pending_matter = calendar_events + matter_events
        for r in range(laps):
            self.lap = r
            # S26.2 again, not a second rule: RESOLVE thaws, so each lap re-freezes before its
            # own DELIBERATE. MATTER did the first one.
            # Barrier 2 (04:509): the tenure store is made whole BEFORE the freeze, by the driver --
            # the owner of barrier lifetimes (04:155). DELIBERATE owns nothing (04:158). `_rehome`
            # exists so a Tenure added before its subject Person existed still reaches its owner;
            # `budget`, `person_side_eligible` and `questions_for` read `p.tenures` directly.
            w._rehome()
            w.frozen = True
            scenes = self.deliberate(choose, question,
                                     self._questions_at_barrier())      # a MAP: no token; returns {scene id: Scene}
            acts = [a for sc in scenes.values() for a in sc.acts]       # release order, as the map was built
            events = self.resolve(mint_token(w, WriteClass.ACTS), acts, contest_max_depth, scenes=scenes)
            # M4 (`ED-IN-0279` clause (a), `04 §A.2:134` as amended 2026-09-28): the SEVENTH
            # step, sharing barrier 3 -- no `TRACE.barrier(...)` call, so "four barriers" stays
            # true. Fights whatever RESOLVE just declared and deferred; appended onto the SAME
            # `events` list, before the bookkeeping below, so a field battle's own outcome
            # counts toward `_realised` and reaches the log/WITNESS fan-out exactly as any other
            # verb's events do -- ENCOUNTER is not a second, parallel accounting.
            # v10 REM-31: the host rides THIS call only -- the one step a PLAYABLE fight suspends at.
            events = events + self.encounter(mint_token(w, WriteClass.ACTS), events,
                                             contest_max_depth, host)
            # ⚠⚠ **WHAT WAS REALISED, AS OPPOSED TO WHAT WAS ATTEMPTED -- KNOWABLE ONLY HERE,
            # AFTER THE FOLD.** `deliberate` records an attempt at RELEASE, when the scene-action is
            # spent. Whether the act DID anything is the fold's answer, and
            # `_drop_what_was_already_done` must read that: an act attempted and REFUSED in lap 0
            # must be retryable in lap 3, because a later lap's world may have made its
            # precondition true (R-03's own channel).
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
                    _key = opportunity_key(a.verb, subject_of(a), a.payload)
                    if _key is not None:        # an act that names nothing is never recorded
                        self._realised.setdefault(a.actor, set()).add(_key)
            for e in events:
                w.log.append(e)              # S19.5 -- ONE LOG, NOT TWO
                TRACE.event(e.id, e.kind, e.causes)
            # MATTER's and CALENDAR's events are seasonal and join the FIRST lap's fan-out only;
            # the alternative deposits one wear once per lap, which is the fourth clock this
            # docstring refuses.
            deposits += self.witness(mint_token(w, WriteClass.INTERIOR), pending_matter + events)
            pending_matter = []
            n_acts += len(acts)
            n_events += len(events)
        self.census(mint_token(w, WriteClass.MATTER))
        # v9 IN-27 (H-176; #457 D6): THE ENDING STEP IS A READ THE SEASON REPORTS -- never an actor. No
        # token, no Event, no write, and the run does not halt on it; `world_q.endings_reached` says
        # what an ending is and why the realm as built reaches none.
        endings = world_q.endings_reached(w)
        w.tick += 1
        # `rounds` (the lap count; the output key keeps its string) IS REPORTED because the tick is otherwise invisible in the artifacts: the
        # summary's `acts/events/deposits` are also what a one-pass season produces. It is a
        # SEASON-LEVEL FIGURE and no Event carries a lap (`D-21`: the lap index is a driver
        # local; `Claim.lap` is the one carrier field, because `questions_for`'s `since` reads it).
        return dict(acts=n_acts, events=n_events, rounds=laps,
                    deposits=deposits, hash=w.content_hash(), endings=endings)

# ---------------------------------------------------------------------------
# THE SEVEN STEPS, BOUND BACK ONTO THE CLASS (unit L5, ED-IN-0206; the seventh, `encounter`,
# `ED-IN-0279` clause (a)).
#
# `04_CODE_ARCHITECTURE.md` §A.2:134 -- *"loop/  driver + six steps. The driver is the ONLY
# constructor of write tokens."* (AMENDED 2026-09-28 to seven). The §A.2 table gives each step its
# own owned state, its own `emits`, and its own token; each body lives in its own module and is
# BOUND HERE.
#
# ⚠ **BOUND, NOT DELEGATED, AND THE DIFFERENCE IS LOAD-BEARING.** `SeasonDriver.witness` IS
# `witness.witness` after this line runs, so `inspect.getsource(SeasonDriver.witness)` returns the
# MOVED BODY. Tests read a step's source that way (`test_d9b` checks that `witness` calls
# `ledgers.evict_over_cap(`); a delegating stub would fail them and SILENTLY VACATE any negative
# assertion over the step's source.
#
# ⚠ `season()` CALLS ALL SEVEN THROUGH `self`, so the binding is what keeps those calls resolving.
# Six of them take the barrier's `Token` as their first argument after `self` -- `04 §C.1`'s
# `calendar(w,cal)`, `matter(w,mat)`, `resolve(w,act,scenes)`, `witness(w,intr,cache)`,
# `census(w,mat2)`, and `encounter` -- and `deliberate` takes none.
# ---------------------------------------------------------------------------
from .calendar import calendar                                            # noqa: E402
from .census import census                                                # noqa: E402
from .deliberate import deliberate                                        # noqa: E402
from .encounter import encounter                                         # noqa: E402
from .matter import STEP_CALLS as MATTER_STEP_CALLS, matter              # noqa: E402
from .resolve import (_admits, _apply_write, _contest, _eligible, _fold,  # noqa: E402
                       _grade, _occasion_ids, _survives, resolve)
from .witness import witness                                              # noqa: E402

SeasonDriver.calendar = calendar
SeasonDriver.matter = matter
SeasonDriver.deliberate = deliberate
SeasonDriver.resolve = resolve
# `SeasonDriver.encounter` IS `encounter.encounter` after this line, not a delegating stub.
SeasonDriver.encounter = encounter
SeasonDriver.witness = witness
SeasonDriver.census = census
# RESOLVE's own machinery, bound for the same reason: `_fold` reaches all three through `self`, and
# two source-scanning guards read `_apply_write`'s and `_fold`'s spans by name.
SeasonDriver._eligible = _eligible
# §E2's eligibility + `requires`, the ONE owner both the fold and the contest branch read.
SeasonDriver._admits = _admits
SeasonDriver._occasion_ids = _occasion_ids
SeasonDriver._fold = _fold
SeasonDriver._apply_write = _apply_write
# Extracted from `resolve()`'s own loop so `loop/encounter.py` shares both (§8) -- see their own
# docstrings in `resolve.py` for what each does and does not re-check.
SeasonDriver._survives = _survives
SeasonDriver._contest = _contest
# v9 FI-01 (`ED-FI-0009`): an inquiry's routed roll, the branch beside `_contest` in `resolve()`.
SeasonDriver._grade = _grade
