"""`season.state.world` -- THE STORE, AND THE GATE ON IT.

Extracted from `shape.py` at step 4 of the decomposition (ED-IN-0203), a PURE MOVE: `World`, the
read-only tenure concatenation `_TenureView`, the per-entity digest `_entity_digest` that
`World.content_hash` folds, and `MATRIX_REFUSAL_LAW`. `shape.py` re-exports all four, so
importers name this module directly (`from ..state.world import World`). The `shape.py`
facade that used to re-export it was deleted at step 10 of the decomposition.

⚠ `MATRIX_REFUSAL_LAW` TRAVELS WITH ITS READER, NOT WITH THE MATRIX. It is a table and it looks
like data, and `data/matrix.py`'s own docstring records the adjudication at step 2: it goes with
`World.write`, its only reader. That docstring used to state the ruling as an ADDRESS -- *"stays in
`shape.py`"* -- which named where the reader happened to be, and went false the moment the reader
moved; it now states the ruling. The table's home followed the gate here, which is the same ruling
applied, not a new one. What makes it not-data is what it holds: a cell's `("no")` here
carries the NAME OF THE LAW REFUSING (`S3-L4`, `S24`, `S9.3`, `S20`, `S30`), so that the gate can
log a refusal as *the design saying no* rather than as bookkeeping. The matrix says which cells are
closed; this says on whose authority.

⚠ THE READ/WRITE ASYMMETRY GUARD IS IN THIS MODULE AND MUST STAY WHOLE. `CLAUDE.md` §0.1 point 1's
worked hazard is exactly `_TenureView` + `World.tenures` + `add_tenure` + `_rehome`: the store moved
onto `Person`, and a getter that returned a plain `list(...)` would have let all nine
`w.add_tenure(...)` sites go on appending to a throwaway, silently, with every test still green.
The decomposition plan §2 item 6 lists the four as un-splittable for that reason, and they are all
here.

⚠ THIS MODULE IMPORTS `state.carriers` AND NOTHING ABOVE IT. The store knows the things it holds;
the things do not know the store. `queries`, `decision` and `loop` are later steps and none of them
may be imported here -- `World` is declared FIRST (S45.1) precisely so that everything reading the
world can be written after it.
"""

from __future__ import annotations

import hashlib
from typing import Any, Callable, Optional

from ..data.fixtures import DEFAULT_FIXTURES, Fixtures
from ..data.matrix import Step, WriteClass, matrix_row, partition_lookup
from ..data.rosters import RUNG_KINDS, TENURE_KINDS, roster
from ..gaps import Forbidden, InstrumentDefect, NoProducer, Unowned, Unspecified
from ..trace_log import TRACE
from .carriers import (
    Event, Office, Person, Proposition, Record, Rung, Site, StateChange, Tenure,
)
from .ids import H

# Where S30's matrix says "no", the refusal belongs to the LAW THE CELL ENFORCES, not to the
# matrix's bookkeeping rule. These are the cells whose "no" is a named law refusing.
MATRIX_REFUSAL_LAW: dict[tuple[tuple[str, str], Step], tuple[str, str]] = {
    (("Person", "stance"), Step.MATTER): (
        "S3-L4",
        "L4 / S25 -- NO SOCIAL QUANTITY MOVES AT MATTER. 'The world may silt a harbour; IT MAY "
        "NOT SOUR A TOWN'S MOOD.' This is the design refusing, not the design failing to say"),
    (("Person", "stance"), Step.CALENDAR): (
        "S24", "S24 -- CALENDAR DECIDES NOTHING; it fires occasions"),
    (("Person", "stance"), Step.WITNESS): (
        "S9.3",
        "S9.3 -- WITNESS NEVER TOUCHES A BELIEF. If evidence can move a conviction the moral "
        "layer has become a second epistemic layer and T2 is gone"),
    (("Rung", "yield"), Step.RESOLVE): (
        "S30", "S30 -- `yield` is written at MATTER ONLY; it is the matrix's one single-cell row"),
    (("Person", "claim_ledger"), Step.RESOLVE): (
        "S20", "S20 -- `witness` is THE ONLY MINTER of a root token, and it runs at WITNESS"),
}

# ⚠ W2 AUDIT. Rekeying the table on `(kind, field)` NARROWED IT FOUR-FOLD without anyone noticing.
# Under the old thing-keying, every field written with `thing="stance"` INHERITED stance's laws --
# so `(Person, convictions)`, `(Person, beliefs)`, `(Person, scar)` and `(Person, axis_count)` got
# L4/§25 and §9.3 for free, and after the rekey they fell through to the generic "ANY UNMARKED
# CELL" branch. Four of the design's proudest refusals began logging as bookkeeping, which is
# exactly what REV 4's comment in `write()` exists to prevent.
#
# THE FIX IS NOT TO RESTORE THE RIDE-ON -- that inheritance WAS defect D1, and getting the law by
# riding on a neighbour's row is how `(Person, convictions)` became a PASS in the first place.
# Each row states its own law, which is what keying on the pair is for.
# roster-exempt: MECHANISM. The four rows that lost their law to the rekey, listed so each gets
# its own entry. Which rows these are is derivable from the matrix (`social: true`, Person);
# the list is a loop over a fix, not a definition.
for _pk_field in ("convictions", "beliefs", "scar", "axis_count"):
    MATRIX_REFUSAL_LAW[(("Person", _pk_field), Step.MATTER)] = (
        "S3-L4",
        "L4 / S25 -- NO SOCIAL QUANTITY MOVES AT MATTER. 'The world may silt a harbour; IT MAY "
        "NOT SOUR A TOWN'S MOOD.' This is the design refusing, not the design failing to say")
    MATRIX_REFUSAL_LAW[(("Person", _pk_field), Step.CALENDAR)] = (
        "S24", "S24 -- CALENDAR DECIDES NOTHING; it fires occasions")
    MATRIX_REFUSAL_LAW[(("Person", _pk_field), Step.WITNESS)] = (
        "S9.3",
        "S9.3 -- WITNESS NEVER TOUCHES A BELIEF. If evidence can move a conviction the moral "
        "layer has become a second epistemic layer and T2 is gone")




class _TenureView(list):
    """`World.tenures` -- a READ-ONLY concatenation over the owners (S15.1).

    ⚠ IT RAISES ON EVERY MUTATOR, and that is the whole reason it is a class rather than a plain
    `list(...)`. `CLAUDE.md` §0.1 point 1 names this exact hazard: *"when a getter starts computing
    from a new source while setters still write the old one, EVERY WRITER SILENTLY BECOMES A
    NO-OP."* Moving the store onto `Person` did precisely that to nine `w.add_tenure(...)`
    sites. Returning a plain list would have let all nine keep running, keep appending to a
    throwaway, and keep passing -- the Tenure would simply never exist. Every one of them now
    fails at the call, and the fix is `w.add_tenure(t)`, which routes by subject."""

    # roster-exempt: MECHANISM. These are PYTHON'S mutator method names, not a game definition
    # — rosters.yaml's own test is "would changing this change the GAME, or change how the code
    # works?", and editing this list changes only which call raises. It is also not a set anyone
    # may edit: it is fixed by the language. The guard flagging it is the guard working; a
    # declared exemption is the answer, and a name-based whitelist would not be (G2).
    _MUTATORS = ("append", "extend", "insert", "remove", "pop", "clear", "sort", "reverse",
                 "__setitem__", "__delitem__", "__iadd__", "__imul__")

    def _refuse(self, *_a, **_k):
        # `InstrumentDefect`, NOT `Forbidden`: this is a call-site bug, not a law of the design,
        # and filing it as a GAP is what put three false holes in the count. See the class.
        raise InstrumentDefect(
            "w.tenures is a READ-ONLY VIEW over the subjects that own the Tenures (S15.1). "
            "Use w.add_tenure(t) -- it routes by subject to the owner. Mutating the "
            "concatenation would write to a temporary and silently lose the Tenure.")


for _n in _TenureView._MUTATORS:
    setattr(_TenureView, _n, _TenureView._refuse)


def _entity_digest(obj: Any) -> str:
    """`H-118`: a deterministic string for ONE entity's own state, for `World.content_hash`.
    `Person`, `Site` and `Tenure` are `@dataclass` -- their auto-generated `__repr__` lists every
    field in DECLARATION order, which is fixed by the class and not by insertion, so it is stable
    across two runs of the same seed (R4). `Rung` is not a dataclass (S10 -- it stores its fields
    via `object.__setattr__` behind a whitelist, `Rung._DECLARED`), so it is read off `vars()`;
    `Rung.__init__` always inserts the same fields in the same order, so that dict's own iteration
    order is already stable, and `sorted()` over its items makes the point structural rather than
    incidental."""
    if hasattr(obj, "__dataclass_fields__"):
        return repr(obj)
    if isinstance(obj, dict):
        # `dates`, `petitions`, `dispensations` and `docket` hold PLAIN DICTS, not entities.
        # `sorted` on the items makes the digest independent of insertion order (R4).
        return repr(sorted((str(k), repr(v)) for k, v in obj.items()))
    if hasattr(obj, "__dict__"):
        return repr(sorted(vars(obj).items()))
    return repr(obj)


class World:
    def __init__(self, world_seed: int, fixtures: Fixtures = DEFAULT_FIXTURES):
        self.world_seed = world_seed
        self.tick = 0
        self.fixtures = fixtures
        self.persons: dict[str, Person] = {}
        self.rungs: dict[str, Rung] = {}
        self.offices: dict[str, Office] = {}
        self.sites: dict[str, Site] = {}
        self.records: dict[str, Record] = {}
        self.propositions: dict[str, Proposition] = {}
        # S15.1 -- the store is the SUBJECT'S. `_unowned` holds only the Tenures whose subject
        # is not a person (`contain : Rung -> Rung` is the bulk of them). See the `tenures` view.
        self._unowned: list[Tenure] = []
        self.log: list[Event] = []
        self.dates: dict[str, dict] = {}
        self.docket: list[dict] = []

        self.petitions: dict[str, dict] = {}
        self.dispensations: dict[str, dict] = {}
        self.manifest: dict[str, str] = {}      # S43 -- role -> provider, resolved AT BOOT
        self.step: Optional[Step] = None
        self.frozen = False
        self._barrier_cache: dict = {}
        self._in_parallel_map = False
        self.writes: list[tuple] = []
        # `W4`. The Events `write()` emitted during the current barrier, so a caller that needs an
        # ANTECEDENT can name the emission its own write just produced -- which is how a band
        # crossing's `causes[]` reaches the wear that crossed the floor.
        self._emitted_by_write: list[Event] = []
        self.crossings: list[tuple] = []        # S12.1/L5 -- band-edge crossings, EMISSIONS
        # S33: "`purpose` must be unique per DRAW, not per operation, or two draws inside one
        # act collide." A per-TICK ordinal is unique within the tick AND identical across runs
        # of the same seed -- a global counter would be unique but NOT REPRODUCIBLE, which
        # destroys the replay contract, and a content hash collides when two draws are alike.
        self.draw = 0

    # -- S30.2: the write class is a PARAMETER of the store API, THE GATE APPLIES THE WRITE,
    # and `record_kind`/`fieldname` are REQUIRED so the L4 limb cannot be silenced by omission.
    # -- THE TENURE STORE, ROUTED BY SUBJECT (S15.1) -----------------------
    @property
    def tenures(self) -> "_TenureView":
        """Every live-or-dead Tenure, owner-first. Read-only -- see `_TenureView`."""
        self._rehome()
        out: list[Tenure] = []
        for pid in sorted(self.persons):
            out.extend(self.persons[pid].tenures)
        out.extend(self._unowned)
        return _TenureView(out)


    def contain_ascends(self, subject: str, object_: str) -> bool:
        """MAY `subject` BE CONTAINED IN `object_`? The §10 ladder, asked rather than raised.

        ⚠ ONE OWNER, TWO POLARITIES, AND `W-C` MADE THE SECOND ONE REACHABLE. The rule lived
        inside `add_tenure`, where its only expression was a `Forbidden`. That was survivable while
        no COMPUTED act ever named a destination: once `move` carries a real `to`, a person can
        name any rung their containment path reaches -- including a SIBLING, because
        `contain.path` asks for a shared ancestor and a sibling has one -- and the ladder then
        refused the write by RAISING, which kills the season. A person attempting a journey the
        world will not seat them in is not an instrument defect and not a design gap; it is a
        BLOCKED TRAVEL, which is the Event `move` already declares.

        So the question is asked here and answered twice: `add_tenure` raises on it, because a
        caller writing an illegal edge directly is a bug, and `_eff_move` declines on it, because a
        person is allowed to try. Two readings of one declaration -- the same shape `evaluate`
        gives a `requires` cell, and the reason neither site re-implements the ladder.

        Non-rungs pass: `add_tenure` never checked an edge whose ends are not both rungs (a
        `contain` onto a Record means something else), and narrowing that here would be a new
        rule wearing a refactor's clothes."""
        sub, obj = self.rungs.get(subject), self.rungs.get(object_)
        if sub is None or obj is None:
            return True
        order = list(RUNG_KINDS)
        return order.index(obj.kind) > order.index(sub.kind)

    def add_tenure(self, t: Tenure) -> Tenure:
        """The ONE writer. Routes to `t.subject`'s own list, or to `_unowned` when the subject is
        not a person (`contain : Rung -> Rung` is most of those).

        ⚠ IT NOW VALIDATES, AND REV 1 VALIDATED NOTHING -- so `rung_kinds` was a MEMBERSHIP SET
        WEARING THE NAME OF A HIERARCHY. Jordan, 2026-09-02: *settlements are nested inside
        territories inside provinces inside duchies inside realm? I think that is required too, or
        is that unnecessary to nest these and instead just explicitly define scale?* The nesting is
        required and it is the thing `under_purview` WALKS -- a scale label cannot be walked, so
        the two are not interchangeable. But no `contain` edge was direction-checked, so a
        settlement containing a duchy was accepted, and `probes` builds an outright cycle.
        Measured: `corpus_run.build_at` gives 37 person-scale cases a `person`-kind rung containing
        three person rungs, and nothing refused.

        ⚠ AND `Tenure.kind` WAS UNCHECKED, which made `TENURE_KINDS` a write-only roster.
        `Tenure(..., "holds", ...)` -- the plural typo -- was accepted, and `_eligible` tests
        `t.kind == "hold"`, so the office would be silently unheld by everybody. That is the same
        failure shape `Office.__post_init__` already refuses for remit acts (§8: one rule, applied
        at every constructor rather than at one)."""
        if t.kind not in TENURE_KINDS:
            raise Unowned(
                f"tenure {t.id!r} has kind {t.kind!r}, which is not on the roster",
                "S15", needs=f"a kind from rosters.yaml: tenure_kinds {sorted(TENURE_KINDS)}",
                law="#353 §15 -- the seven Tenure kinds are a CLOSED set. An unrostered kind is "
                    "not an error at write time and a silent never-match at read time")
        if t.kind == "contain" and not self.contain_ascends(t.subject, t.object):
            sub, obj = self.rungs[t.subject], self.rungs[t.object]
            raise Forbidden(
                f"`contain` from {sub.kind} {t.subject!r} to {obj.kind} {t.object!r} does "
                f"not go up the ladder", "S10",
                needs="a parent strictly above the child on `rung_kinds`",
                law="#353 §10 -- `contain : Rung -> Rung` is the containment LADDER. An "
                    "edge that does not ascend makes `under_purview` walk sideways or "
                    "loop, and Jordan's governance canon reads purview off that walk")
        (self.persons[t.subject].tenures if t.subject in self.persons else self._unowned).append(t)
        return t

    def _rehome(self) -> None:
        """A Tenure added BEFORE its subject existed landed in `_unowned`; move it now.

        Without this, ordering decides ownership: a fixture that appends the Tenure and then
        creates the Person leaves `p.tenures` empty while `w.tenures` still shows it -- so
        `budget` would read zero offices for a duke the world agrees is a duke. That is a
        read/write asymmetry of exactly the shape §0.1 point 1 describes, and it would be
        invisible because both surfaces are individually correct."""
        if not self._unowned:
            return
        keep = []
        for t in self._unowned:
            (self.persons[t.subject].tenures if t.subject in self.persons else keep).append(t)
        self._unowned = keep

    def _refuse_undeclared_kind(self, thing, wclass, sname, record_kind, fieldname,
                                emits, declared) -> None:
        """A kind no Part D row declares is a FABRICATED kind, and the `emits:` column is the only
        thing that may name one.

        ⚠ ONE RULE, ONE MESSAGE. This lived twice — once on the must-name-a-kind path and once on
        the exempt path — and the two copies said *"which Part D does not declare for it"* and
        *"undeclared"*, so a test matching one passed and the other did not. §8 broken inside a
        single function, which is the smallest scale this repo has yet found it at. Found by the
        `W4` adversarial pass."""
        if emits is None or emits in declared:
            return
        TRACE.write(thing, wclass.value, sname, False)
        raise Forbidden(
            f"({record_kind}, {fieldname}) tried to emit {emits!r}, which Part D does not "
            f"declare for it: {list(declared)}", "D22",
            needs=f"one of {list(declared)}",
            law="a kind no row declares is a FABRICATED kind, and the `emits:` column is the "
                "only thing that may name one")

    def write(self, thing: str, wclass: WriteClass, apply: Callable[[], Any],
              record_kind: str, fieldname: str, driver: str,
              caused_person_exists: Optional[str] = None,
              emits: Optional[str] = None,
              causes: Optional[list[str]] = None,
              subject: Optional[str] = None) -> Any:
        """`W4`. THE GATE IS ALSO THE EMITTER, because `H-12` is `ruled` that way: *"MATTER emits
        an Event per write so crossings have an antecedent"*, default *"Part D's `emits:` column"*.

        A MATTER write on a row that declares an `emits:` kind MUST name one, and naming one the
        row does not declare is refused. That pairing is `D22` made mechanical: a MATTER write with
        a declared emission that emits nothing is the SILENT WRITE the design forbids, and an
        emission the matrix never declared is a fabricated kind. Both directions matter — §42.2's
        polarity rule is that absence maps to the verdict against the thing measured, so the
        absence of an emission has to be a refusal rather than a quiet success.

        Emission lives HERE rather than at each call site because §8's invariant is that every rule
        lives once: keyed on `(record_kind, fieldname)`, which is the same key the write class and
        the social partition are already read from, so a new MATTER write inherits its emission by
        existing rather than by remembering."""
        step = self.step
        sname = step.value if step else "-"
        # W2: THE GATE IS KEYED ON `(kind, field)`, which is how S30's own rule is stated. It was
        # keyed on `thing`, and that is defect D1 in one line: `(Person, convictions)` rode on
        # `stance`'s row, so a real gap became a PASS. `thing` survives as a TRACE label only.
        try:
            row = matrix_row(record_kind, fieldname)
        except Unspecified:
            TRACE.write(thing, wclass.value, sname, False)
            raise
        allowed = row.steps
        if step not in allowed:
            TRACE.write(thing, wclass.value, sname, False)
            # ⚠ REV 4. Rev 3 raised Unspecified here on the argument that S30 and S30.1 are
            # one doctrinal condition. THEY ARE NOT, and the over-correction reported THREE OF
            # THE DESIGN'S PROUDEST REFUSALS AS DEBTS: W3 ("the world sours a mood"), A3 ("an
            # arc ends at a counter"), P19 ("a threshold produces an outcome") all showed as
            # UNSPECIFIED at S30 -- L4 and L5 tallied as things the design failed to say.
            #
            #   a cell marked "no"  = the design REFUSING          -> Forbidden, at ITS law
            #   a row that is absent = the design NOT SAYING       -> Unspecified, at S30.1
            #
            law = MATRIX_REFUSAL_LAW.get(((record_kind, fieldname), step))
            if law is not None:
                raise Forbidden(f"({record_kind}, {fieldname}) written during {sname}", law[0],
                                needs=f"one of {sorted(s.value for s in allowed)}", law=law[1])
            raise Forbidden(f"({record_kind}, {fieldname}) written during {sname}", "S30",
                            needs=f"one of {sorted(s.value for s in allowed)}",
                            law="S30 -- ANY UNMARKED CELL IS A WRITE-CLASS VIOLATION")
        expect = row.write_class(step)
        if expect is not wclass:
            TRACE.write(thing, wclass.value, sname, False)
            raise Forbidden(
                f"({record_kind}, {fieldname}) written in class {wclass.value} at {sname}; "
                f"the matrix says {expect.value}",
                "S30.2", law="S30.2 -- the write class is a PARAMETER of the store API, checked PER WRITE SITE")
        social, prov = partition_lookup(record_kind, fieldname)
        if social and driver != "Act":
            TRACE.write(thing, wclass.value, sname, False)
            raise Forbidden(
                f"({record_kind}, {fieldname}) is social:true and was written by {driver}", "S3-L4",
                needs="a named person's act",
                law=f"L4 -- social:true means ONLY AN ACT may write it. The world may silt a harbour; IT MAY NOT SOUR A TOWN'S MOOD. [row provenance: {prov}]")
        # W2 AUDIT: `(Person, coherence)` is written ONLY through seam Events (#353 :1904), and
        # the seam is RESOLVE via `contest` (:98). The row said so IN A COMMENT, which constrains
        # nothing -- this file's own fidelity rule 6: a false claim of enforcement is worse than
        # none. Bounded here, on `(Tenure, until)`'s precedent one block below.
        if (record_kind, fieldname) == ("Person", "coherence") and driver != "Seam":
            TRACE.write(thing, wclass.value, sname, False)
            raise Forbidden(
                f"(Person, coherence) written by {driver}", "S54 item 15",
                needs="driver='Seam' -- a contest Event at RESOLVE",
                law="#353 :1904 -- Coherence is 'written only through SEAM Events', and :98 puts "
                    "the seam at RESOLVE via `contest`. Any other writer makes it a FOURTH "
                    "licensed clock, and §25.1 says the three are exhaustive")

        # S15.3 -- THE SEAM IS BOUNDED BY A CAUSATION RULE, NOT BY THE COLUMN. An actorless row
        # may write Tenure.until ONLY on a (Person, exists) change THE SAME ROW ALSO CAUSED.
        if (record_kind, fieldname) == ("Tenure", "until") and driver != "Act":
            if caused_person_exists is None:
                TRACE.write(thing, wclass.value, sname, False)
                raise Forbidden(
                    "an actorless row wrote Tenure.until with no (Person, exists) change of its own",
                    "S15.3", needs="the same row must cause the death it ends a tenure through",
                    law="S15.3 -- a plague that kills the praefect ends his tenure THROUGH THE DEATH; A STORM CANNOT TOUCH IT. A second such seam means the column is the wrong mechanism")
        # S30.2: "AND THE GATE MUST APPLY THE WRITE." A gate that validates, logs and returns
        # true while the mutation happens beside it is worse than no gate.
        # -- W4: THE EMISSION, GATED ON THE SAME ROW AS THE WRITE ------------------------
        declared = tuple(row.emits or ())
        # `H-86`. A row whose declared emissions are ALL CONDITIONAL is exempt from the
        # must-name-a-kind rule -- `(Record, ttl)` declares only `record.expired`, and emitting
        # that on a non-terminal decrement asserts an expiry that has not happened. The exempt
        # rows are DATA (`rosters.yaml: conditional_emission_rows`), never a literal here, and the
        # ambiguity in Part D's column that makes the roster necessary is registered rather than
        # decided. The exemption is narrow: an UNDECLARED kind is still refused below.
        conditional = roster("conditional_emission_rows")
        if (wclass is WriteClass.MATTER and declared
                and f"{record_kind}.{fieldname}" not in conditional):
            if emits is None:
                TRACE.write(thing, wclass.value, sname, False)
                raise Forbidden(
                    f"({record_kind}, {fieldname}) written at MATTER and emitted nothing, while "
                    f"Part D declares {list(declared)}", "D22",
                    needs="emits=<one of the row's declared kinds>",
                    law="`H-12`, RULED: MATTER emits an Event PER WRITE so crossings have an "
                        "antecedent, and the kind is Part D's `emits:` column. A MATTER write "
                        "that emits nothing is the silent write `D22` names")
            self._refuse_undeclared_kind(thing, wclass, sname, record_kind, fieldname,
                                         emits, declared)
        else:
            self._refuse_undeclared_kind(thing, wclass, sname, record_kind, fieldname,
                                         emits, declared)

        before = apply()
        TRACE.write(thing, wclass.value, sname, True)
        self.writes.append((thing, wclass.value, sname, record_kind, fieldname, driver))
        if emits is not None:
            # ⚠ THE SUBJECT IS THE RECORD, NOT THE TRACE LABEL. `thing` is a human label for the
            # trace line (`"condition"`); the Event's subject has to be the RECORD ID or nothing
            # can find the emission again. The first version used `thing`, so every site's wear
            # emitted under the subject `"condition"` — and `last_emission_of` therefore never
            # matched, so season 1's wear re-rooted at `[ROOT]` and the clock did not chain. That
            # is exactly the failure `W4`'s ROOT-count proof exists to catch, and it caught it.
            if subject is None:
                raise Forbidden(
                    f"({record_kind}, {fieldname}) emits {emits!r} with no `subject=`", "S33",
                    needs="subject=<the record id>",
                    law="THE SUBJECT IS THE RECORD, NOT THE TRACE LABEL. The fallback was "
                        "`subject or thing`, and `thing` is a human label for the trace line -- "
                        "which is exactly the value that made every site's wear emit under the "
                        "subject `\"condition\"`, so `last_emission_of` never matched and the clock "
                        "re-rooted every season. Leaving the fallback in place meant emission was "
                        "inherited by existing while the half that makes a clock CHAIN still had "
                        "to be remembered -- and a one-shot emission with a forgotten `subject=` "
                        "is silent. Found by the `W4` adversarial pass")
            subj = subject
            # ⚠ THE DRAW ORDINAL IS PART OF THE ID, AND IT WAS NOT. Without it the id is
            # `(seed, tick, subject, kind)`, so TWO EMISSIONS OF ONE KIND ON ONE SUBJECT IN ONE
            # TICK GET THE SAME ID — and `W8` produces exactly that: MATTER's larder draw and its
            # yield credit both write `(Rung, stores)` and both emit `stores.changed` for the same
            # rung in the same season. The `W4` adversarial pass named this months of work ago in
            # the abstract (*"the emission id carries no draw ordinal; `new_draw()` has zero
            # callers"*) and nothing could reach it until there were two same-kind writes; the
            # uniqueness guard caught it the moment there were. S33's ordinal is the mechanism the
            # design already carries, reset per tick by `season()`, so ids stay reproducible: the
            # write order is deterministic (every loop here is sorted) and the counter follows it.
            ev = Event(
                # ⚠ IN `purpose`, NOT AS A FIFTH ARGUMENT. `H`'s own docstring states the
                # contract — *"`purpose` must be unique per DRAW, not per operation"* — so the
                # ordinal belongs inside the string the design already reserves for it, and
                # widening `H`'s signature would have been a second way to say the same thing.
                id=H(self.world_seed, self.tick, subj, f"emit:{emits}#{self.new_draw()}"),
                kind=emits, subject=subj,
                changes=[StateChange(subj, "set", wclass.value, fieldname, None)],
                # ⚠ `causes` IS REQUIRED IN SUBSTANCE AND THE DEFAULT IS NOT `[ROOT]`. Handing an
                # un-caused emission the root is how every Event in the `W9` artifact came to
                # carry `causes=[ROOT]` — #353 §19.4 calls that field "the substrate of the entire
                # emergent-narrative claim", and a default root populates it with nothing. A
                # caller with no antecedent must say so by passing `[ROOT]` itself.
                causes=list(causes if causes is not None else []),
                emitted_at=self.tick)
            # ⚠ NO EMPTY-`causes[]` CHECK HERE. `Event.__post_init__` already refuses one at
            # S19.4, and re-implementing it would be `CLAUDE.md` §8's violation one constructor
            # apart — the first version of this block did exactly that and shipped two messages
            # for one rule. The Event constructor raises before this line is reached.
            self.log.append(ev)
            TRACE.event(ev.id, ev.kind, ev.causes)
            # ⚠ BUFFERED ONLY AT MATTER, AND THE SCOPE IS THE POINT. `matter()` drains this to
            # decide what WITNESS fans out. A WITNESS-step emission (`claim.deposited`) left in
            # the buffer survives into the NEXT season's MATTER and is fanned there, which closes
            # a loop: a deposit emits, the emission is witnessed, that deposit emits. Measured
            # before this guard: `claim.deposited` reached 249 in a two-season run and was
            # accelerating. The buffer is MATTER's, so only MATTER fills it.
            if step is Step.MATTER:
                self._emitted_by_write.append(ev)
        return before

    # -- S4: a Query MAY be cached. Built AT a barrier, read-only until the next, DISCARDED there.
    def cache_at_barrier(self, key: str, build: Callable[[], Any]) -> Any:
        if self._in_parallel_map:
            raise Forbidden(f"cache '{key}' built inside a parallel map", "S4",
                            law="S4 -- the cache is built AT A BARRIER; NOTHING INSIDE A PARALLEL MAP BUILDS ONE")
        if key not in self._barrier_cache:
            self._barrier_cache[key] = build()
        return self._barrier_cache[key]

    def last_emission_of(self, kind: str, subject: str) -> Optional[str]:
        """The id of the most recent Event of `kind` about `subject`, or None.

        `W4`'s chaining primitive: a licensed clock's next tick names its previous one, so
        `[ROOT]` stops appearing after the clock's genuine first emission."""
        for e in reversed(self.log):
            if e.kind == kind and e.subject == subject:
                return e.id
        return None

    def discard_caches(self) -> None:
        self._barrier_cache.clear()

    # -- S33/S45.2/S66: THE ARTIFACT IS A CONTENT HASH OVER THE LOG. Rev 1 had none, and it is
    # the one execution artifact the architecture names as its done-condition.
    def new_draw(self) -> int:
        """S33's draw ordinal. Reset at the start of every tick by `season()`."""
        self.draw += 1
        return self.draw

    # `H-118`: EVERY GAME-STATE COLLECTION ON `World`, DECLARED ONCE. A hash that enumerates
    # collections inline goes stale the day someone adds one, silently and in the direction that
    # flatters it -- which is the defect H-118 IS. Declared here so `content_hash` iterates a
    # list rather than a hand-written sequence, and so
    # `test_h118_content_hash_folds_every_game_state_collection` can assert this covers the
    # World's actual attributes rather than a copy of them (§8: the rule lives once).
    #
    # ⚠ THE FIRST VERSION OF THIS FIX FOLDED FOUR OF ELEVEN AND ITS DOCSTRING CLAIMED THE GAP
    # CLOSED. Found by the W-0 adversarial pass, which is the reason the set is derived and
    # tested rather than typed: `records` and `propositions` were among the omissions, and
    # `create_record` and `utter` -- two of the FIVE verbs that execute in the corpus -- write
    # exactly those (`_eff_create_record`, `_eff_destroy_record`, `_eff_utter`). So the same
    # blindness H-118 measured on `persons` was live on the collections the corpus actually
    # moves, behind a docstring saying otherwise.
    # roster-exempt: MECHANISM, on the same ground as `_STEP_CLASS` above. These are `World`'s
    # OWN PYTHON ATTRIBUTE NAMES -- what the object calls its own fields -- not the game's
    # vocabulary. `rosters.yaml` holds what the WORLD contains; this holds where THIS CLASS puts
    # it, and the test below derives the check from `vars(World)` rather than from this tuple, so
    # the tuple is a hash ORDER and not a definition. Moving it to data would invite someone to
    # edit how the hash works while believing they were editing the game.
    _STATE_COLLECTIONS = ("persons", "rungs", "offices", "sites", "records", "propositions",
                          "dates", "petitions", "dispensations")
    # roster-exempt: MECHANISM, as `_STATE_COLLECTIONS` directly above -- the one state field that
    # is a LIST rather than a mapping, split out because its order is semantic (S31's queue) and
    # it is therefore folded positionally rather than sorted.
    _STATE_SEQUENCES = ("docket",)

    def content_hash(self) -> str:
        """`H-118`: REV 1 hashed the log alone. Demonstrated there -- delete a person from one of
        two identical worlds with no Event appended, and the hashes still matched. It now folds
        EVERY game-state collection (`_STATE_COLLECTIONS` + `_STATE_SEQUENCES` + `tenures`) --
        IN ID ORDER -- ahead of the log, so a state divergence that never reaches the log is no
        longer invisible to it.

        ⚠ SORTED-KEY ORDER, NEVER INSERTION ORDER (R4). Every mapping is hashed via `sorted(...)`
        over its own keys, and `self.tenures` (the read-only owner-first VIEW, S15.1) is re-sorted
        by `t.id` rather than trusted -- its own order is owner-then-unowned, a CONSTRUCTION
        order, and R4 (the same seed replaying byte-identically) would break the moment two runs
        added tenures in a different sequence for the same eventual world. `docket` is a LIST and
        its order is semantic (S31's queue), so it is folded in place, positionally.

        `Event.observed` EXISTS AS OF `W-B` (2026-09-04) and this fold reaches it with no edit
        here, which is what the forward-compatibility `getattr` was written for. ⚠ THE `getattr`
        STAYS AND THE SENTENCE THAT SAID THE FIELD DOES NOT EXIST IS GONE: the guard is cheap and
        keeps this callable on a stripped Event a test builds, but a docstring asserting the
        absence of a field the dataclass declares is false, and false in the direction that stops
        the next reader checking (found by the `W-B` adversarial pass)."""
        # [JUSTIFIED: a HASH WIDTH, not a game value -- 16 bytes is the 32 hex characters the content hash is compared as; nothing in the model reads it as a quantity]
        h = hashlib.blake2b(digest_size=16)
        for name in self._STATE_COLLECTIONS:
            for k in sorted(getattr(self, name, {}) or {}):
                h.update(f"{name}|{k}|{_entity_digest(getattr(self, name)[k])}".encode())
        for name in self._STATE_SEQUENCES:
            for n, item in enumerate(getattr(self, name, ()) or ()):
                h.update(f"{name}|{n}|{_entity_digest(item)}".encode())
        for t in sorted(self.tenures, key=lambda t: t.id):
            h.update(f"T|{t.id}|{_entity_digest(t)}".encode())
        for e in self.log:
            h.update(f"{e.id}|{e.kind}|{e.subject}|{e.emitted_at}|{e.degree}|"
                     f"{','.join(e.causes)}".encode())
            for c in e.changes:
                h.update(f"~{c.subject}|{c.mode}|{c.driver}|{c.field}|{c.delta}".encode())
            # `Event.observed` is folded here. The `getattr` default is not a claim that the
            # field is absent -- it is on `Event` since `W-B` -- it keeps this callable on an
            # Event a test has stripped, which `test_wb_the_carrier_moves_the_seeded_hash` does.
            for o in (getattr(e, "observed", None) or []):
                h.update(f"^{o}".encode())
        return h.hexdigest()

    # -- S43: resolution AT BOOT, by string. A missing provider is a STARTUP FAILURE WITH A
    # NAME IN IT, not a null three seasons into a campaign.
    def boot(self, required_roles: tuple[str, ...]) -> None:
        missing = [r for r in required_roles if r not in self.manifest]
        if missing:
            raise NoProducer(
                f"role(s) {missing} have no provider in the manifest", "S43",
                needs="a registry row naming a role and its provider",
                law="S43 -- the engine names the ROLE; the registry names the MODULE; RESOLUTION HAPPENS BY STRING AT BOOT. A missing provider is a startup failure with a name in it. THE MANIFEST IS THE SEAM; A PATH LITERAL IN A BODY IS NOT")
