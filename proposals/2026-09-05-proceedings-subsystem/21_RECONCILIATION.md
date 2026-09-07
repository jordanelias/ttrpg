# 21 · THE RECONCILIATION — every issue the stress suite raised, ruled against the doctrine, and ordered

## Status: **PROPOSED (2026-09-07). HELD BACK IN FULL. NOTHING RATIFIES ON MERGE.**
## Review: a read-only **Fable 5.1** audit-and-planning pass over `20_STRESS_TESTS.md` PARTS A–F,
## judged against `proposals/2026-09-03-meta-architecture/04_CODE_ARCHITECTURE.md` and
## `references/design_rulings_2026-09-06.md` (R1–R8). Per `CLAUDE.md` §10 that tier is
## **read-only audit, planning and decomposition — never synthesis or artifact authorship**, so the
## pass returned findings, rulings and an order, and this file is the Opus write-up of them.
## ⚠ **Its citations were re-verified by hand before use.** PART A is that record, including the one
## ruling of its own that does not survive.

---

# WHAT THIS FILE IS, AND THE OBJECTION TO ITS EXISTENCE

`04_CODE_ARCHITECTURE.md` §G.4.4 forbids an adversarial pass from producing a document, and §G.3.3
forbids a finding *as* a document. **The review charges `20_STRESS_TESTS.md` with breaching both** —
751 lines of findings-as-prose, twenty of which its own column marks as restating a registered row.
**The charge lands, and this file is not a second offence: it is the instruction for undoing the
first.** PHASE 0 below is entirely *fold the surviving findings into the design files as edits and
delete the register*, which is what §G.4.4 requires and what a report cannot do to itself.

**A plan is a permitted artifact** — `19_PLAN.md` is one — and this is a plan. It supersedes nothing
in `19_PLAN.md` except at the eleven points named in PART F, and it opens no register.

---

# PART A · THE VERIFICATION RECORD — what was checked before anything was believed

**A planning pass taken on trust is a planning pass nobody can defend.** Every claim below that
changes a decision was re-read at its cited line before being used. The review's coverage note
declares it ran nothing and did not open `results.json`; that is the right disclosure and it is why
the checks below were run rather than skipped.

| the claim | verdict | what was read |
|---|---|---|
| `claim_subjects` **replaces** the actor with the act's referents when the act names a subject and writes nothing — so `F-32`'s correction ran the wrong case | ✅ **HOLDS** | `shape.py:4203-4205` — `if not any(c.subject for c in e.changes) and any(refs or ()): out = [r for r in (refs or ()) if r]`, then `return out or [e.subject]` |
| `p_success` exists, in `sigma_leverage.py` and not `dice_engine.py`, so `F-34` searched one module | ✅ **HOLDS** | `engine/autoload/sigma_leverage.py:246` — `def p_success(base_ob, pool, net_sigma=0.0, tn=TN_STANDARD, capped=True)` |
| `exists:DocketItem` cannot evaluate at all: `WorldReader.read` derives `attr = "docketitems"`, which is not in `_STATE_COLLECTIONS`, and returns `UNKNOWN` | ✅ **HOLDS, and it is sharper than either prior reading** | `shape.py:1152-1164` and `2988-2993` — `docket` is a `_STATE_SEQUENCES` member, not a collection |
| `19_PLAN.md` step 15 already answers `F-14`: *the declaring act is the determination … the declaration writes the disposal* | ✅ **HOLDS** | `19_PLAN.md:454-462`, verbatim |
| `determine`'s corrected conjunct names an operand its form does not admit — `{form: basis, of: actor}` against `basis: [subject, from, to]` | ✅ **HOLDS, and it is new** | `rosters.yaml` `requires_forms.needs.basis`. **The correction that fixed one load failure introduced another** |
| `ST-09` executed the **live** `speak` row (`requires: "—"`, `writes: []`), not the design's | ✅ **HOLDS** | `verb_table.yaml:448-457` |
| `R7` refuses the echo model, so `fan_out_mode="total"` is refused by ruling rather than by preference | ✅ **HOLDS** | `design_rulings:161-194` — *legitimacy falls where the news has reached*; and it names `H-62` first-rank |

## A.1 · ⛔ The one ruling of the review's that does NOT survive

**`C-7` rules that the quorum needs no grammar widening, on the ground that form 4 (`cardinality`)
can carry a threshold bound to `amount` from the arrangement row.** It cannot.

```
rosters.yaml  requires_forms.needs.cardinality : [subject, from, to]
                                  scalar_threshold : [subject, site, from, to, kind, amount, floor]
```

**`cardinality` does not admit `amount`.** A cell of that form naming one refuses at load, which is
the same class of defect the review itself caught in `determine`'s `basis` conjunct — and it caught
that one while committing this one. So the choice is real and is between:

| option | cost |
|---|---|
| **add `amount` to `cardinality`'s `needs`** | a one-member roster edit — **but it IS a widening of the closed grammar**, and `§F.24a` derived those `needs` sets from the 32 live cells rather than designing them, so adding an operand to a form is exactly the eighth-form inflation it warns against, arriving through the operand column instead of the form column |
| **keep `19_PLAN.md` step 15's own account** | it says plainly: *"⭐ this widens the precondition grammar by two entries — counted as a design change and taken because it is what works best"* |

> ### **RULED HERE: `19_PLAN.md` step 15 stands as written, and the widening is paid for openly.**
> The plan already counted the cost, named it a design change, and took it under Jordan's *"of course
> we accept those shapes"* (`ED-SC-0034`). The review's attempt to make it free is the more elegant
> answer and it is unavailable. **`C-7`'s conclusion — no new verb, no stored tally, the declaring
> act is `determine` — survives intact; only its "no widening" clause is struck.**
>
> ⚠ **And this is the shape of error to expect from a planning tier**: it optimised toward the count
> the directory is proudest of (zero additions) and reached for the one form that would preserve it.
> The check that caught it was reading the roster, not reading the argument.

---

# PART B · WHAT THIS OVERTURNS IN `20_STRESS_TESTS.md`

**Four of that report's results do not survive, and two of them were in its headline.** They are
corrected here and PHASE 0 folds the corrections into the report itself.

## B.1 · ⛔ `F-32` is withdrawn — and the diagnosis it "corrected" was right all along

`20_STRESS_TESTS.md` claims the lane's headline diagnosis (*no deposit names the actor*) is false,
because after a speech the bench member's ledger holds `(p_party_a, speech.made, 100, firsthand)`.

**The claim is an artifact of the test.** `ST-32` builds its `speak` with **no payload**
(`stress_proceedings.py`, `act(w, "p_party_a", "speak", key="press")`), so the act has no referents,
`claim_subjects` falls through to `return out or [e.subject]`, and the actor survives **by the
default branch rather than by the rule**. Run with an act that names a subject — which every real
`speak` at a proceeding does, since it presses a matter about somebody — the actor is **replaced**.

> **So `18_FINDINGS.md` PART B and `HANDOFF_SC.md` were correct, this suite's correction of them was
> not, and `MD-08` falls with it.** The lesson is `§0.1` point 1's, in the other direction: I checked
> a claim about a rule by running a case the rule does not cover, and a green result read as a
> refutation.

⭐ **And the replacement mechanism is already ruled.** `R8.1` specifies one `seen` claim per
`(witness, event)` carrying a struct in `Claim.value`, subjected to the changed thing or else **to
the rung** — which for a speech (writes nothing) means the venue, so every person contained there can
raise a question from it. **That is the propagation the actor-subject claim cannot raise**, and it
supersedes `19_PLAN.md` step 2's *prepend the actor* mechanism rather than re-aiming it.

## B.2 · ⛔ `F-34` is withdrawn — the blocking measurement is runnable today

`ST-34` reported that the design's own **blocking** deprivation-floor check cannot be run because the
ladder module exports no `p_success`. It searched `engine/autoload/dice_engine.py` only.
**`p_success` is at `engine/autoload/sigma_leverage.py:246`**, with exactly the signature the check
needs (`base_ob`, `pool`, `net_sigma`, `tn`, `capped`). **`M-7` and `M-8` are runnable now**, against
`MD-07`'s injected magnitudes, and PHASE 2 step 14 runs them.

## B.3 · `F-14` is downgraded from *the strongest finding here, needs a design answer* to *the row contradicts the plan*

The execution fact stands: `determine.writes = ["Tenure.degree"]` opens nothing, and `disposes:` has
no writer in the verb table. **What does not stand is *the design never says which act opens it*.**
`19_PLAN.md` step 15 says it: *the declaring act is the determination … the declaration writes the
disposal.* `04_CODE_ARCHITECTURE.md` §B.7 names `determine` as a seat's conferral basis, and
`01_AXIOMS.md`'s `ID-14` opener map puts it there.

> **So the finding is real and its grade was wrong.** It is not an open design question; it is
> `04_VERBS.md` §B.2 having been corrected *away* from the plan — the draft that would have written
> `Tenure.since` was struck for contradicting the live row, and the live row is the thing the plan
> changes. That is `§G.4.3`'s third direction: a correction graded backwards.

## B.4 · `F-05` is sharper than either version of it

Neither the original finding (*the docket never names a matter, so a clerk is mandatory*) nor the
critic's revision (*the typed cell is satisfied by an empty sitting*) is right. **`exists:DocketItem`
returns `UNKNOWN`**, because `WorldReader.read` looks for a `docketitems` collection and `docket` is a
sequence. **The design's `speak` cannot form at all against the live reader** — not "forms too
easily", not "cannot form until a clerk acts". The fix is a reader branch, and it is in PHASE 2.

## B.5 · Three headline claims in that report are overstated and are corrected in PHASE 0

| claim | correction |
|---|---|
| *"a seatless `speak` folds and emits"* is credited as **the design working** | `ST-09` ran the **live** row — `requires: "—"`, `writes: []`, the pre-design row. It is a fact about what the tree had before this directory existed, which is the same thing the report says of the other four supplied steps, and it should be filed there rather than as a pass |
| *"a seeded proceeding replays identically"* | `ST-35` replays a **season containing one uncontested `speak`**. No draw occurred, no seam was entered, no margin was produced. It is season-loop determinism, not `06_RESOLUTION.md` C.5's *the same seam draw replays* |
| *"permuting who attends does not move the outcome"* | `ST-36` permutes the **insertion order of the same attendee set** and compares Event multisets. That is `PART D` row 41a's DELIBERATE permutation, and row 41a demands the **content hash**. The attendance claim is untested |

**None of the three is a false statement about what ran; all three are the wrong claim attached to a
true run.** That is the failure `§0.1` point 3 exists to catch, and it survived two critics.

---

# PART C · THE CONFLICT MAP — twelve collisions, each ruled

**This is the part the *holistic and conflict-free* requirement turns on.** The fixes interact, and
several are mutually exclusive: closing one finding the obvious way breaks a count, an axiom or a
ruling that closes another. Each row below names the two things that cannot both be done, cites
where each comes from, and rules — under the doctrine, the 2026-09-06 rulings, and `R2`'s five
terminal properties.

**⭐ Every collision resolves without escalation.** `CLAUDE.md` §0's five tests (superseded ·
irrelevant · answered by a design document · answered by precedent · answered by what makes sense
for the architecture) were run over all twelve; PART H records what was tried on the one that came
closest.

## C-1 · The verdict Tenure — who opens it, and who owns it

| | |
|---|---|
| **A** | give `determine` a `Tenure.since` write, so `disposes:` has a writer |
| **B** | `04_VERBS.md` §B.2 keeps the live row *UNCHANGED*; `AX-4` forbids a non-owner opening an edge on somebody else |

> ### ⭐ **RULED: A — and it is not a collision, it is the plan and the doctrine already agreeing while one row disagrees with both.**

**Who owns the Tenure a determiner opens: its SUBJECT.** That is not a new rule — it is exactly
`confer`, which opens a `hold` whose subject is the conferee and not the conferrer. What licenses the
opening is the **seat's conferral basis** (`04_CODE_ARCHITECTURE.md` §B.7: `Seat.conferral: determine
by <judging seats>`), which is the opener mirror of `T-o`'s revocation basis.

**What follows, precisely:**

1. `determine.writes` becomes **degree-keyed** — `Tenure.since` **and** `Tenure.degree` — because
   step 13 gives the row a `contests:` and loader invariant 12 then requires degree-keyed `writes`
   and `emits` with equal key sets.
2. ⭐ **`disposes:` finds its reader**, which is what `ID-13` demands of every key: a load check that
   each arrangement row's `disposes` kind appears in `ID-14`'s opener map for `determine` (or, for
   `disposal: mutual`, in the parties' `oblige`). **The key stops being decorative in the same edit
   that gives it a writer.**
3. **The write gate needs one clause**, and this is an `IN`-lane consequence stated rather than
   smuggled: `§C.2`'s `F3` admits `actor == subject`, `T-n`, `T-o`-with-`via`, and the destroy
   cascade — **and `confer` matches none of the four today.** The clause both need is
   *`via` is a Seat whose conferral basis names this verb for this kind*, which is `ID-14`'s opener
   map read at the gate rather than a fifth exception.
4. **The price, stated because a refusal with no cost is not a refusal:** the subject may `release`
   what the finding opened (`T-m`, and `D-5`/`ED-SC-0035` left `T-m` unamended). A convict can
   discharge his own penance. **That is not a hole — it is public, witnessed, priced by reception,
   and accepted by ruling**, and the `release` row should carry that sentence.

**Property served: capable.** `14_THE_WORLD_IN_THE_ROOM.md` §E — *a disposal must write a thing
somebody can lose.*

## C-2 · The ladder rung — a field, an Event kind, or neither

| | |
|---|---|
| **A** | give the rung a carrier (a field, or a rung-bearing Event kind) so the fold has an operand |
| **B** | `00_DERIVATION.md` §B.2 retracted the field on five grounds; loader invariant 7 forbids multiplying the declared kind roster |

> ### ⭐ **RULED: NEITHER. The rung is an operand of the `speak` act, and the provider folds over its own resolved acts.**

`ED-SC-0034` licenses per-proceeding aggregates outright — *aggregates that die with the run are
free* — and the fold already keeps `act_of` (Event id → the Act that emitted it). So the rung is read
from the acts the run itself resolved, needs **zero fields and zero Event kinds**, and dies at the
barrier exactly as `§B.2` said it should.

⚠ **What `§B.2` must be corrected to say:** *a fold over the run's own **acts***, not *over emitted
`matter.*` **Events***. The sentence as written names an operand the emission does not carry, and
that is the whole of `F-28`.

⚠ **And the residue is real and is deferred by ruling, not by oversight.** What a *witness* learns
about **which** rung was conceded is not carried by the Event kind. `R8.2` sequences per-term
observation content behind a recognition producer, so the witnessed rung becomes an
`observation_terms` member later (`IN` lane). **Until then, `00_DERIVATION.md`'s *the concession is
visible because it was witnessed* is true at kind granularity only** — the room learns that a descent
happened, not how far. That sentence needs the qualifier.

**Property: dynamic** — in-run state with no carrier.

## C-3 · Fan-out off `total` — forced by ruling, and ordered behind a repair

| | |
|---|---|
| **A** | flip `fan_out_mode` off `total` (`19_PLAN.md` step 1), so absence means something |
| **B** | 89 corpus worlds and six campaign goldens sit on that arm; `chronicle` matches nobody; `document_key` cannot fire on any act — so the narrowed arm may **starve** the propagation chain rather than shape it |

> ### ⭐ **RULED: A, and it is not this design's call — `R7` already made it.**

*Legitimacy falls where the news has reached* is the architecture model; **`total` IS the echo model
Jordan refused** — instant, uniform, everywhere — arriving at the deposit layer instead of the
aggregate layer. The goldens are the **control**, not a dependency: they re-baseline and the deltas
are printed.

⚠ **But the ORDER is the ruling's content, and getting it wrong measures the wrong thing.**
`R8.4` records that `document_key` cannot fire on any act at all — it tests `t.object == e.subject`
while every fold Event sets `subject = actor`, and no `hold` Tenure takes a person as object. **So on
the narrowed arm, the bureaucratic channel `R5` requires is dead**, and `M-6` would measure
starvation rather than the design.

**Therefore: `R8.4`'s repair and `H-84`'s record-moving route come BEFORE the flip.** That is PHASE 1
steps 1 → 2, and it is the single most important ordering constraint in this plan.

**Properties: emergent, persistent.**

## C-4 · The deposit's content — `R8` already decided it

| | |
|---|---|
| **A** | fix what a speech deposits (`F-32`'s programme) |
| **B** | `R8.1` rules the shape already; `R8.2` refuses the per-term split for now; `PART D` row 39 forbids widening the eviction comparator |

> ### ⭐ **RULED: B wins by test 1 (superseded). `F-32` proposes nothing `R8` has not decided, and its premise is withdrawn anyway (B.1).**

One `seen` claim per `(witness, event)`, `value = {stratum, marks, who, why}`, **subject = the changed
thing, else the rung.** For a speech — which writes nothing — that is the **venue**, so `Q2` fires for
everyone contained there, because a person's `contain` Tenure puts their rung in the `mine` set.
`reception` then reads `c.value.who == speaker`, a third reader of `Claim.value` beside the two
`R8.3` enumerates. Cost: **+1 claim per witness-event**, which the cap absorbs; **nothing touches row
39's comparator.**

**Property: emergent** — misattribution, hearsay, and the wrong person blamed all become reachable.

## C-5 · The clerk — no verb, two edits and one build step

| | |
|---|---|
| **A** | a clerk verb, or a clerk role field |
| **B** | `03_PARAMETERS.md` §C.2 defines the clerk as *whoever holds the case `Record`*, conferred by `carry`; `04_VERBS.md` adds ZERO verbs |

> ### ⭐ **RULED: B, and the fix is smaller than the finding.**

1. **`open_case.writes` gains `DocketItem.matter`** — the exact precedent `04_VERBS.md` §B.1 (vii)
   used for `Partial`: *a live `[CAL, RES]` matrix row; `carry` already writes it; no carrier, no
   field, no Event kind, no verb.*
2. **A `docket` reader branch** so `exists:DocketItem` can evaluate at all (B.4). Without it the cell
   returns `UNKNOWN` forever and no `speak` forms in any of the twelve games.
3. **`12_BUILD_ORDER.md` gains the step** that is currently in none of its twelve — which is why its
   own step 9 BAR is unreachable by its own plan.

For the bench-less games, where nobody may `open_case`, the route is `petition` → `carry`.

**Property: capable.**

## C-6 · The disposal's reach — one channel, not six, and not zero

| | |
|---|---|
| **A** | the reach is free; `post_remit` and `chronicle` already carry it (`20_STRESS_TESTS.md` PART F's kill of `INV-14`) |
| **B** | `<rung kind>` means *the containment walk from the venue up to that tier*, and no channel computes that |

> ### ⭐ **RULED: BOTH ARE HALF-RIGHT, AND PART F OVER-CORRECTED.**

| reach | carrier | state |
|---|---|---|
| **`room`** | `co_located` | **today's behaviour.** Free |
| **`body`** | `post_remit` — it walks live `hold` Tenures for an office whose `remit_acts` intersect the emitting verb's `remit:`, **with no presence test** | free **once `determine` emits the disposal** |
| **`<rung kind>`** | ⚠ **nothing** | needs the one channel `19_PLAN.md` step 16 adds, keyed on the disposal's emission and the row's `disposal_reach` |

⚠ **And `F-21`'s "neither fires" was a fixture artifact**: the probe used a `tenure.opened` Event,
which rides on `confer`'s emissions, and the fixture office holds no `confer` remit. **It is not that
nobody holds the remit** — it is that nothing in the fixture emitted a disposal. `chronicle` matching
nobody is separately real, registered, and **deleted by step 16**.

**Properties: persistent, flexible** — the same emission reaches differently by a data value.

## C-7 · The quorum — no verb, no stored tally, and the widening is paid for

| | |
|---|---|
| **A** | a `declare` verb, or a stored tally |
| **B** | `04_VERBS.md`'s zero-verbs count; `T-a` refuses a tally across holders |

> ### ⭐ **RULED: the declaring act is `determine`; members `commit`, which are their own edges; nothing is stored.**
> ### ⚠ **AND THE GRAMMAR WIDENING IS REAL — see PART A.1, where the review's attempt to make it free is struck.**

`19_PLAN.md` step 15's own account stands: the precondition gains a cardinality conjunct over live
commitments to the disposition, **and that widens the grammar by two entries, counted as a design
change and taken under `ED-SC-0034`**. `cardinality`'s operand set does not admit `amount`, so there
is no free construction available.

**No count is stored anywhere** (`PART D` row 9 survives), and the falsifier is a grep for a
`count`/`tally`/`quorum_reached` field returning nothing.

**Property: flexible** — thresholds live in data.

## C-8 · The seam signature — the venue is already in it

| | |
|---|---|
| **A** | widen `seam.contest` with `matter` and `arrangement` (`MD-01`'s third amendment) |
| **B** | `§C.5` fixes the signature at `(proj, place, prize, claimants, depth, max_depth)`; `17_PLAYABILITY.md` already charged one position for amending a signature in a directory this one does not own |

> ### ⭐ **RULED: B. Zero signature change, and `MD-01` is withdrawn.**

| what was thought missing | where it actually is |
|---|---|
| the venue | **`place`, already the second parameter.** The tracer derives it wrongly — `rung=(a.payload if isinstance(a.payload, str) else None) or "R"` — and should read `Scene.place`. **A wiring defect, not a contract gap** |
| the matter | the causing act's referents, reachable resolver-side from `causes[0]` |
| the arrangement | `occasion_at(place)` — a Query over the docketed Date at the venue |

**Property: flexible** — one seam for every provider, which is the property a third amendment would
have spent.

## C-9 · The investigation bands — one ladder until a provider earns an exemption

| | |
|---|---|
| **A** | keep `Found/Partial/Nothing`, `Read/Misread/Nothing`, `Sound/Wrong/Nothing`, `Seen/Glimpsed/Nothing` |
| **B** | `PART D` row 30: one ladder for every scale; `§C.4`: *a verb may not declare a band its subsystem cannot report* |

> ### ⭐ **RULED: B by test 5 — no investigation provider exists, so nothing can report a non-margin band.**

Combat's three-band exemption exists **by ruling**, because it reads a scene rather than a margin.
These five rows have no provider at all and no ruling, so they are margin-graded and must key on the
ladder's four names — **the same correction `04_VERBS.md` §B.1 already made for `speak`, applied to
the rows on the next page.** `Found → Success`, `Partial → Partial`, `Nothing → Failure`,
`Overwhelming` declared; an empty write is lawful for a deposit-producing act.

**Property: S — *calculations consistent in methodology with sibling mechanics*.**

## C-10 · `Tenure.term` versus `Record.ttl` — not a collision once split

> ### ⭐ **RULED: two different clocks, two different carriers.**

| the clock | carrier |
|---|---|
| a summons's **return day**, a stay's length — a **document's** life | `Record.ttl` / `Record.stages`, which `open_case` already writes ⚠ *subject to `term.matured` actually marking something, which it does not yet* |
| a **term of service**, `surveil`'s declared interval, an oblige's deadline — an **edge's** life | `Tenure.term`, which is **`04_CODE_ARCHITECTURE.md` §B.8's own specified field** |

⚠ **So `19_PLAN.md` step 22's *the one new field in the whole plan* is misattributed**: it is the
doctrine's unbuilt field, not this design's addition, and the sentence should say so. `F-18`'s
`Record`-carrier half stands for the document clock; its *the design never considered it* half does
not survive, because the two clocks are genuinely different objects.

⚠ **`(Record, matured)` remains a matrix row for a field the class does not have.** That defect is
real, unregistered, and is a PHASE 0 fix.

## C-11 · `convene`'s ordinal — a predicate stem, not an operand

The `scale:` key is **live** at `verb_table.yaml:138` and deliberately kept pending `Act.via` carrying
scope. **Jordan's 2026-09-05 correction supersedes that for `convene`'s value**, and invariant 10
deletes the key. The replacement `rank(venue.kind) > rank(person)` needs **a `rank` stem in
`REQUIRES_STEMS`**, not a `venue` operand — `subject` already binds the rung. One stem, added to a
closed set that refuses undeclared members at load. **Stated as a cost, not smuggled.**

## C-12 · The bench-less games' missing term and cap — the rows already declare it

`F-07` and `F-19` report that five games have no term, no stages and no depth cap because nobody may
`open_case` there. **Those five rows declare `term_required: false` and `appeal_basis: none`.** The
absence is the row's own statement, not a gap in it, and a negotiation ends by mutual `commit` —
which `F-07` omits from `05_PROCEDURE.md`'s four endings. **Not a gap. Closed by test 3.**

---

# PART D · THE PLAN

**Ordered by dependency, not by severity.** Each step names what it unblocks, its **execution
artifact** (`§0.2` — a juncture is done when the behaviour EXECUTES; `m1_acceptance` row 4 is
doc-derived and is cited for nothing here) and its **falsifier** (`ID-11` — ship the falsifier with
the claim).

**Cost class:** **free** = a documentation correction carrying no design decision · **spec** = an
unbuilt specification with a named home · **new** = something that must earn its place against
`03_VERBS_AND_LOOPS.md` §F.1's no-new-primitive bar, and whose price is stated.

⭐ **The whole plan adds: zero carriers, zero verbs, zero Event kinds, zero edge kinds. It adds one
predicate stem, one reader branch, one witness channel, two grammar entries, and one field that is
the doctrine's own.** Every one of the six is named as a cost below.

## ✅ PHASE 0 · EXECUTED 2026-09-07 — with two deviations and one result that changes PHASE 2

**All ten edits are made and their falsifiers are green.** `ST-06 · ST-12 · ST-13 · ST-23 · ST-27 ·
ST-37 · ST-38` return RAN; the suite's RAN count went 4 → 11.

⚠ **SIX OF THE FALSIFIERS HAD TO BE REBUILT BEFORE THEY COULD FIRE**, and that is worth recording
because it is the same defect in six places: they were **substring searches over a whole document**,
so a correction that *quotes the retracted claim while withdrawing it* still read as the defect. A
test that cannot go green when the thing it names is fixed is not a falsifier — `§0.1` point 2 from
the other side. `ST-06` now asks whether a retraction marker governs the claim; `ST-12` scans the
YAML blocks rather than the prose; `ST-23`, `ST-27`, `ST-13` and `ST-38` compare parsed values
rather than the presence of a word.

### Deviation 1 — `03_PARAMETERS.md`'s header says **fifteen**, not thirteen

**The plan said thirteen, per step 11's deletions. Writing thirteen now would have reintroduced the
same defect pointing the other way**, since the block below the header lists fifteen keys today.
The header states today's count and carries a note that step 11 takes it to thirteen, and the header
moves in that commit. **A header that miscounts the block it introduces is the defect; the direction
of the miscount is not a mitigation.**

### Deviation 2 — `20_STRESS_TESTS.md` is **not deleted**, and PHASE 0h is narrowed

**PHASE 0h said *retire the findings register*.** I have not, and the reason is on the file's own
front page rather than only here. **§G.4.4 governs an adversarial pass that creates a document
nobody asked for; Jordan asked for this one** — *"log all instances where you have had to
create/invent something … log all mechanical decisions as well as gaps and conflicts and failures."*
**What the rule protects against is a parallel queue that accumulates**, and that is closed by
marking the file a **closed record** with the surviving findings folded into the design files —
which is what the other nine edits did — rather than by deleting the logs that were requested.

### ⛔ Result — `M-7` was run, and the deprivation floor FAILS

**PHASE 2 step 14 said *`M-7` is runnable now*. It was run, in PHASE 0, and it does not hold.**

| at the **1D pool floor** | `p_success` |
|---|---|
| Ob 1 | 0.2266 |
| Ob 2 | 0.0228 |
| **Ob 3** | **0.0006** |
| Ob 4 and above | **0.0000** |

`06_RESOLUTION.md` §B.3a requires that *at the minimum lawful pool against the maximum plausible
composed obstacle, `p_success` must not be effectively zero*, and calls it **a blocking check on
shipping the composed obstacle, not an advisory one**. It reaches zero at **Ob 3** — a value
`base_Ob = opposition_score / 2` produces on its own against an opposition score of 6, **before a
single room term is added.**

⭐ **And one of the two remedies §B.3a names is refuted by measurement.** It offers *(a) the σ-channel
must be REACHABLE in that room* or *(b) the obstacle takes a ceiling*. Buying σ-leverage at the floor
against Ob 7 gives `0.0000` at net_σ of 0, 1, 2 **and 3** — **the uniform channel this design leans on
throughout is uniform in Δz and cannot lift a probability that is already zero.** §B.3a item 3 calls
it *the engine's own answer to this exact problem*; at the floor it is not an answer.

> **So PHASE 2 step 14 changes from *run the measurement* to *the measurement failed and the
> obstacle needs a ceiling*** — remedy (b), or a pool floor above 1D. ⚠ **Stated at its true
> strength**: the magnitudes are `MD-07`'s injected set and the 1D pool is the pathological case,
> since a `latitude` floored near 0.7 makes a real pool `brought + 0.7 × conduct`. Against Ob 11 the
> pool sweep reads `pool 9 → 0.0010`, `pool 16 → 0.0753` — **the room is survivable with a dossier
> and not without one**, which is §B.3a's *preparation game* working and simultaneously the case its
> own floor forbids. **The design predicted this shape in the same section** — *the obstacle is
> floored at 1 and ceilinged at nothing* — and this is that shape, measured.

---

## PHASE 0 · the ten edits — **free**

**These advance none of the five properties and are done first anyway**, because each removes a false
statement a next session would act on, and because `§G.4.4` requires an adversarial pass's output to
be *edits to the thing under review*, which is what PHASE 0 is.

| # | edit | artifact / falsifier |
|---|---|---|
| **0a** | `10_LOOPS_AND_GAPS.md` — add the five orphan rows `P-22 · P-23 · P-24 · P-28 · P-29`; mark `P-15` and `P-29` **closed** citing `ED-SC-0034`, and `P-33` closed citing `19_PLAN.md` PART H; mark `P-08` *answered by `08_SEAM.md` §C.1* | `ST-37` returns RAN |
| **0b** | `00_DERIVATION.md` §B.1's count table — fields **0** · verbs **0 new** · carriers: `Seat` → `Office` + a `hold` Tenure | `ST-38` returns RAN |
| **0c** | `03_PARAMETERS.md` — PART D's header to **thirteen** keys (per step 11's deletions); §C.1.1's *vacant* → *held* | `ST-06`, `ST-23` |
| **0d** | `08_SEAM.md` §D.1 — quote the matrix's actual emission kinds (`tenure.graded`, `stance.moved`, `record.created · record.destroyed`, `record.staged`), and state that at RESOLVE what fires is the verb's `emits_at(degree) ∩ earned` | `ST-27` |
| **0e** | `04_VERBS.md` — §B.1 speaker-only stance on all three bands · §B.2 `writes` degree-keyed with `Tenure.since` + `Tenure.degree` (C-1), the `basis` conjunct's `of:` corrected to an operand the form admits, the *UNCHANGED* note struck with the reason recorded · §B.3.2 `path` → `contain_path` and the nine band names → the ladder's four (C-9) | the `ST-12` loader probe, **extended to check each form's `needs`** — which is what would have caught the `basis` defect |
| **0f** | `12_BUILD_ORDER.md` — insert the docketing step; move the obstacle step after the loader and the provider site exist; note that `Tenure.term` is the doctrine's field | — |
| **0g** | `21`'s own corrections into `20_STRESS_TESTS.md` — withdraw `F-32` and `F-34`, downgrade `F-14`, re-cut `F-05`, and correct the three overstated headlines (B.5) | the harness still reproduces |
| **0h** | `20_STRESS_TESTS.md` — fold the surviving findings into the design files as edits and **retire the findings register**, per `§G.4.4`. Keep the harness and `results.json` | the register is gone; the harness runs |
| **0i** | `19_PLAN.md` — step 1 gains `R8.4` as a prerequisite · step 2's mechanism → `R8.1`'s struct · step 15 keeps its widening and gains PART A.1's reason · step 22's *one new field* attributed to `§B.8` | — |
| **0j** | `HANDOFF_SC.md` — retract next-actions 2, 3 and 4, which this review overturns | — |

## PHASE 1 · The epistemic substrate the rulings force — **`IN` lane owns most of it; this lane consumes it**
### Properties: **emergent · persistent · dynamic**

| # | step | class | artifact | falsifier | unblocks |
|---|---|---|---|---|---|
| **1** | ⭐ **`document_key`'s repair** — test the changed record in `changes[]` rather than `e.subject` (`R8.4`) — plus `H-84`'s record-moving route | spec | a non-author holding a `Record` deposits from a `record.*` Event | the channel still fires for nobody but the author | **2**, 6, and all of `R5` |
| **2** | ⭐ **fan-out off `total`** (`19_PLAN.md` step 1), `M-6` measured at both arms | spec, **ruled by `R7`** | two persons' ledgers differ after two seasons; the six goldens re-baseline with deltas printed | the propagation chain collapses on the narrowed arm → step 1 was incomplete | secrets, absence, `F-33`, C-3 |
| **3** | `R8.1`'s `seen` claim and the `observation_terms` roster, declared at load | spec | a witness holds `(rung, seen, {stratum, who, …})`; `Q2` fires for everyone in the rung | an undeclared struct member loads | PHASE 3 |
| **4** | `told_by` minted from the channel at the teller's confidence (`19_PLAN.md` step 4) | spec | a told claim at less than firsthand confidence; standing stops returning its maximum | every deposit is still firsthand | 17, 18 |
| **5** | the ledger-cap measurement (`19_PLAN.md` step 3, `M-1`) with 1–4 live | spec | the printed 3×3 | a witnessed concession survives twelve seasons → no change needed | PHASE 3, `P-42` |

> ⚠ **The ordering 1 → 2 is the plan's single hardest constraint.** Flip fan-out before repairing
> `document_key` and `M-6` measures a starved chain rather than a narrowed one, and the ruling that
> forced the flip gets read back as evidence against itself.

## PHASE 2 · The structure exists and resolves — **this lane's own work**
### Properties: **capable · flexible**

| # | step | class | artifact | falsifier |
|---|---|---|---|---|
| **6** | the six rosters (`speech_kinds` with reachable bands, `ladder_rungs`, `interposition_kinds`, `genres`, `proofs`, `standing_routes`) and **`arrangements.yaml` at thirteen keys**, with `declared` and the quorum. ⭐ **Plus the new load check C-1 earns: every row's `disposes` kind must name `determine` in `ID-14`'s opener map** (or the parties' `oblige` for `disposal: mutual`) | spec | twelve rows load; a fourteenth key fails **naming the row**; the examination loads with no code change; **a `disposes` kind with no opener fails the load** | `PART D` row 28's roster-permutation falsifier — change a roster's membership and see what breaks |
| **7** | `Query.judging_set(w, venue, matter)` | spec | removing the seat's remit empties the bench; a purview walk one rung up still finds it | two matters with disjoint remit coverage return the same seats |
| **8** | the `release` row, carrying `D-5`'s sentence about why closure is the obligor's | spec | invariant 6 satisfiable for the first time; a person resigns an office | — |
| **9** | `convene` corrected — `scale:` deleted, `scalar_threshold` over `subject`, **a `rank` stem added to `REQUIRES_STEMS`** | **new** — one stem | a convening at a hearth and at a realm both load; **one at a person-rung is refused by the ordinal** | the loader accepts `rank` before it is declared |
| **10** | ⭐ **docketing** — `open_case.writes` gains `DocketItem.matter`; **a `docket` reader branch so `exists:DocketItem` evaluates** | **new** — one reader branch — + spec | after `open_case` a `speak` forms; before it, `speech.unheard` emits | the cell still returns `UNKNOWN` |
| **11** | `determine`'s row per C-1 and C-7; the write gate's conferral clause (`IN` lane) | spec + 2 grammar entries | a determination **opens the disposal Tenure on its subject** via the seat; below quorum, `determine.refused` | a grep for a `count`/`tally`/`quorum_reached` field returns anything; a non-owner opening without `via` passes the gate |
| **12** | `speak`'s row with the `Partial` docket operand | spec | four `writes` and four `emits` with equal key sets; `Partial` dockets the speaker's operand | — |
| **13** | the manifest row and the two prize repoints (`ED-SC-0033`); **fix the tracer's `rung=` derivation to read `Scene.place`** (C-8) | spec | a contested `speak` at a settlement **dispatches at the settlement**; the combat goldens do not move | a module-equality test survives inside `contest` |
| **14** | the composed obstacle, and ⭐ **`M-7` and `M-8` run now** via `sigma_leverage.p_success` with `MD-07`'s injected magnitudes | spec | a printed `p_success` at the 1D floor against the maximum composed Ob; `M-8`'s two arms at every latitude including the floor | Ob composes below 1; any path returns a band without a margin |
| **15** | the provider — the nested run, in-run folds over **its own acts** (the rung per C-2, momentum, proofs told), `order` as a registry of sort keys resolved by name, and ⭐ **the `<rung kind>` reach channel**; delete `chronicle` | spec + **new** — one channel | argument emissions deposit identically at `room` and at `realm`; **the disposal's do not** | the provider writes anything; a precondition is evaluated outside the fold |
| **16** | ⭐ **THE BAR** — one seeded proceeding, zero authored acts, twice, **byte-identical including the content hash**; and the two permutations run correctly this time: **speaking order moves the outcome, deliberation order does not** | — | the hash | `ST-35`/`ST-36` re-run against the design's rows rather than the live ones, and against the hash rather than an Event multiset |

## PHASE 3 · The room reads you — `19_PLAN.md` steps 17–21, unchanged but for two corrections
### Properties: **emergent · dynamic**

Depends on PHASE 1 steps 3–4. Two corrections carry forward: **step 17's `reception` reads
`c.value.who`** from `R8.1`'s struct rather than a bare claim subject, and **step 21's observer-set
severity is confirmed** — the `visibility` field is inert and is deleted rather than read.

## PHASE 4 · Forty seasons stop looking like four — `19_PLAN.md` steps 22–27
### Properties: **persistent · emergent**

`Tenure.term` as **`§B.8`'s field** (C-10), with the document half able to ride `Record.ttl` earlier
once `term.matured` marks something. The conviction producer (step 24) closes `P-21` and gives `L-6`
its sign. `M-5` measures whether standing concentrates over forty seasons, which is `P-20`.

---

# PART E · WHAT MUST NOT BE DONE

`§G.1.4`: **a shape is a set of refusals, each with what pays for it.** Each row names the section
that forbids it, so a later session meets the refusal before the temptation.

| temptation | forbidden by |
|---|---|
| a `Proceeding`, `Verdict` or role object | `00_DERIVATION.md` §A.1 runs question 1 over all five candidate values and none survives; `§G.2.1`'s *you can name two* |
| a `Tenure.rung` or `Proposition.rung` field, or a rung inside the Event kind | `00_DERIVATION.md` §B.2's five grounds; loader invariant 7; `ID-13` |
| a second degree ladder, or renamed bands for the investigation rows | `PART D` row 30; `§C.4`; and `04_VERBS.md` §B.1 already made this exact correction once |
| widening `seam.contest` for the matter or the arrangement | `§C.5` — `place` is already the second parameter (C-8) |
| an eighth `requires` form for the quorum — **or an operand added to `cardinality` to fake one** | `§F.24a` derived the operand sets from the 32 live cells; PART A.1. **The widening `19_PLAN.md` step 15 already declared is the honest route** |
| a stored tally, count, or `quorum_reached` | `T-a`; `PART D` row 9 |
| a turn limit or round cap | `05_PROCEDURE.md` §B.1; `AX-5` — a clock nobody wound |
| a public channel matching everyone, or restoring `chronicle` | `19_PLAN.md` step 16; the channel's own docstring |
| a sixth channel written as a dict literal in a body | the channel registry refuses an undeclared member at import |
| `Act.via` as a convention rather than the field | `§B.9` — the grade is MECHANICAL only with the field |
| raising the ledger cap as the memory remedy | `18_FINDINGS.md` — *the right question with the wrong remedy* |
| a creditor verb, or an obligee-side closer | `D-5` / `ED-SC-0035` — the second-person lever stays refused |
| showing the player reception, the obstacle, or the odds | `§C.11`; `07_THE_GAME.md` PART D. `R7` makes this **structural** rather than a courtesy |
| a clerk verb or a role field | `03_PARAMETERS.md` §C.2; C-5 |
| a `subject_absent` flag or a declared cast | `03_PARAMETERS.md` §C.1.1; `19_PLAN.md` PART H |
| re-aiming `19_PLAN.md` step 2 per `F-32` | **withdrawn** — B.1; `R8.1` supersedes the mechanism |
| a "third seam amendment" register row | C-8 |
| **another findings register** | `§G.4.4`; PHASE 0h retires the one that exists |

---

# PART F · RECONCILIATION WITH THE FOUR ORDERS THAT ALREADY EXIST

**Four build orders are live in this directory and they disagree.** A fifth written in ignorance of
them would be the defect this repo keeps filing, so each is reconciled explicitly.

| order | where this supersedes | where it defers | where it was already right |
|---|---|---|---|
| **`12_BUILD_ORDER.md`** | the obstacle step moves after the loader and provider exist; **a docketing step is inserted** (it is in none of the twelve, which is why the BAR is unreachable); `determine`'s row gains the disposal write; the `<rung kind>` channel is added | steps 1 (`judging_set`), 3 (`release`) and 4 (`convene`) as **buildable today** — all three survive | ⭐ **the BAR at step 9**, which is now reachable rather than aspirational |
| **`17_PLAYABILITY.md` PART I** | items 1–4 are absorbed (P-29 is ruled; the cap becomes `M-1`; the stance binding becomes PHASE 0e; the rosters become step 6) | items 5, 7 and 8 fold into steps 15, 17 and 14 | its §G.3 *A/B on the term* is adopted as the shape of every magnitude falsifier here |
| **`18_FINDINGS.md` PART L** | item 1 — *prepend the actor* — is **replaced by `R8.1`'s struct**; the order had no structural phase and PHASE 2 subsumes it | items 2–8 map onto PHASE 1 steps 5 and 4, PHASE 3 and PHASE 4 | ⭐ **its convergence claim stands and is this plan's PHASE 3 motive**: the ledger cannot hold a reading of a person |
| **`19_PLAN.md`** | step 1 gains `R8.4` as a prerequisite (C-3); step 2's mechanism → `R8.1`; step 13 gains the disposal write and the corrected conjunct; step 22's *one new field* is reattributed; step 12's `M-7` is runnable **now** | steps 3–11, 14, 16–21 and 23–27 unchanged | ⭐ **its four-phase shape, and every one of PART H's five closures.** The escalation count stays at zero |

---

# PART G · THE FIVE PROPERTIES, AND WHAT ADVANCES NONE

`R2` makes **dynamic · capable · flexible · emergent · persistent** the terminal criteria, and says
the ratified refusals are *instrumental* to them and must be argued rather than deferred to. So each
phase is scored against them, and anything advancing none is a cut candidate.

| phase | dynamic | capable | flexible | emergent | persistent |
|---|---|---|---|---|---|
| **0 · corrections** | — | — | — | — | — |
| **1 · the substrate** | ● | | | ● | ● |
| **2 · the structure** | ● | ● | ● | | |
| **3 · the room reads you** | ● | | | ● | |
| **4 · forty seasons** | | | | ● | ● |

⭐ **PHASE 0 advances nothing and is still first.** Each of its ten edits is one line that removes a
false statement, and a next session acting on `F-32`, `F-34` or the stale `P-15` row would spend a
session on a settled question — which is the 156-row queue forming again. **They are cheap because
they are documentation; they are urgent because documentation is what the next session reads.**

**Nothing else in the plan is inert.** `F-17`, `F-22`, `F-24` and `F-26` are **dropped rather than
planned** — each is marked *ADDS: nothing* by the report's own column, and `§G.4.4` says a finding
that needs no ruling is either fixed in this commit or dropped.

⭐ **And one result is worth stating plainly, because it changes what this subsystem is for.**
`R7` names `H-62` — *no verb in the table writes any `Person` interior field* — **first-rank and
unavoidable**: nothing propagates until a verb moves an interior. **`speak` writing `Person.stance`
is a producer for exactly that row**, and `determine` opening a Tenure is a producer for the other
half. So the proceedings subsystem is not merely a consumer of the propagation chain the rulings
demand — **it is the first producer the chain has**, and PHASE 2 is on `R7`'s critical path rather
than beside it.

---

# PART H · WHAT IS GENUINELY JORDAN'S — and the honest answer is nothing

**`CLAUDE.md` §0's amendment is explicit that `needs_jordan` is not a parking space**, and that a
session must try to answer in five ordered ways before escalating: superseded · irrelevant · answered
by a design document · answered by precedent · answered by what makes sense for the architecture.

**All twelve collisions were run through the five tests, and none survived to an escalation.** Nine
close on tests 1–4 (a later ruling, a plan step, a doctrine section or a precedent already decided
them); three close on test 5, where one option is clearly right for the code and the reasoning is
recorded above rather than deferred.

⚠ **The one that came closest, recorded with what was tried:** C-7's quorum. A filtered-cardinality
form — a count over edges restricted by a seat Query — would be more expressive than the construction
taken, and it would need an eighth form. **It is refused by default** because `§F.24a` derived the
seven from the 32 live cells rather than designing them, and because `19_PLAN.md` step 15's declared
two-entry widening already buys what the quorum needs. **The trigger is named so the refusal can be
revisited honestly**: if in play a non-bench person's commitment to the same disposition counting
toward quorum reads wrong, *that* is when the eighth form is earned — and it must then be argued as a
design change, not smuggled as a fix.

**One item is escalation-adjacent and is not a design call**, so it is filed rather than asked: the
write gate's `F3` clause needs a fifth exception for a conferral-basis opener (C-1 item 3), and
`confer` — a live, `ruled` verb — **matches none of the four exceptions today.** That is an `IN`-lane
defect this design merely reveals, and it should be registered there rather than answered here.

---

## Provenance

Read-only Fable 5.1 review of `20_STRESS_TESTS.md` PARTS A–F against `04_CODE_ARCHITECTURE.md`,
`00_THE_METHOD.md`, `01_AXIOMS.md`, `02_HIERARCHIES.md`, `03_VERBS_AND_LOOPS.md`,
`references/design_rulings_2026-09-06.md` (R1–R8) and `ED-SC-0033..0036`; written up here after every
decision-changing citation was re-verified by hand (PART A). **The review's own `C-7` ruling did not
survive that check and is struck at PART A.1.** Nothing in this file edits a design document — it is
the instruction for the edits, and PHASE 0 is where they happen.
