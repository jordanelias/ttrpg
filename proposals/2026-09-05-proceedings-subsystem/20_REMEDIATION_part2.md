# 20 · THE REMEDIATION SUITE, PART 2 — the rest of the suite, the order, and what is refused

## Status: **PROPOSED (2026-09-06). HELD BACK IN FULL. NOTHING RATIFIES ON MERGE.**
## Continues `20_REMEDIATION.md`. Read that first — `PART A`'s three corrections govern everything here.

---

# PART B, CONTINUED

## P5 · ⭐⭐ THE ROOM READS YOU — `reception`, resolver-side, into the obstacle

> **This is the proposal the anti-solver argument is made of. Without it the obstacle is computable
> from a decision and the proceeding is a flowchart with dice.**

**Statement.** A resolver-side Query over the bench's own ledgers composes the hidden obstacle term
— so **two rooms with identical parameter rows and different memories band the same speech
differently**, and no decision can compute which.

**Closes.** `P-30`; `15_WHY_IT_IS_A_GAME.md` PART C; `19_PLAN.md` step 17. ⭐ **`L-1` gains its
first measurable edge** — the standing → reception → outcome → standing loop has been signed `+`
since it was written and has never had a term to measure.

### The mechanism

`Query.reception(w, bench: list[str], speaker: str) -> float`, beside `judging_set`. For each
holder: claims whose `subject == speaker` and whose `predicate` is one of `speak`'s emission kinds
(`matter.carried` / `advanced` / `held` / `turned`), valenced `+2 / +1 / 0 / −1` — **the momentum
ladder `19_PLAN.md:437-438` already accepts** — scaled by `confidence/100` and by a source ordinal
(firsthand `1.0`, `told_by` swept). Summed, scaled by fixture `reception_step`, and added into
`P1`'s `obstacle()` at the slot that already exists for it.

> ⭐⭐ **THOSE CLAIMS EXIST ONLY BECAUSE `P2`'s STANCE WRITE PUT THE SPEAKER IN `claim_subjects`**
> (`shape.py:4148`, `:4150-4152`). **So `P5` needs no attribution rule of its own** — `19_PLAN.md`
> step 2 was going to change the deposit rules to make speakers nameable, and `P2` makes them
> nameable as a side effect of writing a stance. *One of the plan's four foundational steps is
> discharged by a different proposal doing its own job properly.*

⚠ **The convictions arm waits.** `19_PLAN.md:509-512`'s second arm — valence from the hearer's
convictions on the matter's axes — needs `P8`'s producer and the alignment table
(`rosters.yaml:877-903`). **Arm 1 alone is enough to make the room unreadable**; arm 2 makes it
unreadable *for a reason the player can eventually infer*, which is better and is not urgent.

### ⭐ Execution artifact

`test_pr_the_same_speech_bands_differently_before_a_bench_that_remembers`: two `tiny_world`s at one
seed, **identical except that one bench member's ledger holds a `matter.turned` claim about the
speaker**. Assert at least one act id bands differently and the two `content_hash`es differ.

**Falsifier:** set `reception_step = 0` and the two worlds are byte-identical. *That is the control
and the falsifier at once, which is the cheapest honest pairing available.*

⚠ **The `T-f` guard is weak and is stated at its true strength.** `inspect.getsource(make_chooser)`
(`:3471`) contains no `reception`, and `reception`'s first parameter is annotated `World`. **The
tracer has no `decision/` package to path-scan**, so the structural guarantee the design claims for
`T-f` is, here, a source grep plus a type annotation. **`09_IMPOSSIBILITIES.md` row 3 should say
so.**

### Primitive count · NERS

**0 · 0 · 0 · 0.** One Query, two fixtures.

**N** — it is *"the difference between a flowchart and a game"* by the design's own account, and it
is Jordan's ruling *"enacted by characters OF the world"* (`15:99-101`) arriving in the resolver
rather than in prose. **R** — the no-player half: **benches remember NPCs too**, so the loop runs
where nobody is watching, which is `R`'s half with no player in it, satisfied directly.
*Completeness:* a bench with empty ledgers returns `0.0`, not a refusal — **a room that has never
heard of you is neutral, which is right.** **S** — ⚠ the term swings a small pool more than a large
one (`06_RESOLUTION.md:754-771`), so **`M-3` must run before any further Ob term is added.**
**E, as a ratio** — one Query against the design's central claim; nothing to amputate.

### What it breaks

Nothing executable today — it depends on `P1` + `P2` + `P3`. ⚠ **And if `M-3` says the weak
speaker's room is a lottery, the remedy is moving THIS TERM ALONE to the σ-channel** (`P-27`), not
the other three, which are properties of the room and the claim rather than of a person.

---

## P6 · TWELVE ROWS, ONE PROVIDER — the loader, the nested run, the veto, and a falsifier that can see

**Statement.** Land `arrangements.yaml` with a loader, have the convener declare the arrangement on
the Date, let the provider order and bound its nested run from the row, hang Fig. 26's licence on
the ladder's existing extension seam, and **replace the `grep` falsifier with rename-invariance.**

**Closes.** `12_BUILD_ORDER.md` steps 2 and 10; `19_PLAN.md` steps 11, 12(d), 14;
**`09_IMPOSSIBILITIES.md` rows 13 and 16**; `P-34`; `P-08` (the provider owns its own order);
`P-16`/`P-17`; and it makes `L-5` signable at all.

⚠ **First, the fact that governs this proposal: there is no `arrangements.yaml` anywhere in the
repository.** Searched, not assumed. **The closure claim — *nothing branches on a game's name*, this
design's central promise — has ZERO execution surface today.** `README.md` says fifteen keys and
`03_PARAMETERS.md:432` says fourteen; neither is a file.

### The mechanism

1. **`data/arrangements.yaml`** beside `rosters.yaml`, thirteen keys per `19_PLAN.md:357`, loaded by
   `_load_arrangements()` next to `_load_verb_table()` (`shape.py:1546`), with `08_SEAM.md:131-144`'s
   invariants: an unknown key fails **naming the row**, and a declared disposal requires a quorum.
2. **`_eff_convene` writes `date["arrangement"] = a.payload["arrangement"]`** — ⭐ **the opener
   declares the terms, which is `T-n` executing rather than being cited.** Dates are dicts
   (`:5033-5035`), so this costs no schema.
3. **The provider reads it** and runs `05_PROCEDURE.md:52-58`'s loop: order attendees
   (`Query.presence`, `:3166-3171`) per `order`, fold inner acts through `SeasonDriver._fold` with a
   provider-computed `Resolution`. ⛔ **Never a write** — the provider holds no token; `_fold` writes
   through `w.write`. *That is the seam's no-write-token guarantee surviving contact with a nested
   run, which is the thing most likely to break it.*
4. **`class LicenceVeto(BandExtension)`** (`dice_engine.py:95-138`) with
   `context_keys=("licence_failures",)` and `may_overwhelm` returning `failures == 0`. The seam
   passes it: `degree_of` (`shape.py:6679`) gains an `extension=` argument read off
   `result.get("extension")` — ⭐ **which also gives `contest()`'s dead `extension` parameter
   (`:6692`) a reader, or licenses deleting it.** Find 5 closes either way.
5. ⭐⭐ **The falsifier, and it is the reason this proposal exists in this shape.** A test that loads
   `arrangements.yaml`, **rewrites every `id` to an opaque token**, reruns one seeded proceeding per
   row, and asserts every `content_hash` is unchanged.

> ### **WHY RENAME-INVARIANCE AND NOT A GREP.**
> `P-34` says the closure falsifier *"cannot see the failure it excludes"*: a scan for
> `arrangement.id ==` is green against a lookup table keyed on the name, against a dict comprehension
> over ids, against anything that reaches the name by a variable. **A grep catches
> `== "tribunal"`. Rename-invariance catches ANY path from a name to an outcome** — which is the
> claim's actual scope (`03_PARAMETERS.md:812-826`). §0.1 point 2: an assertion must be able to
> observe the failure it excludes.

### ⭐ Execution artifact

Four, and they are cheap once the loader exists: the **rename-invariance test** (red on a planted
`if arr.id == "tribunal"`, green otherwise); **the thirteenth game** (`03_PARAMETERS.md:742-758`)
loads with no code change; **permuting `order` moves the hash and permuting nothing else does not**
(`08_SEAM.md:94-95`); and a nested appeal at `max_depth` returns `ContestError` (`:6722-6726`) while
a `licence_failures=1` result at margin ≥ 3 bands `Success` rather than `Overwhelming`.

### Primitive count · NERS

**0 · 0 · 0 · 0.** One data file, one loader, one Date-dict key (declared, no schema), one
`BandExtension` subclass, one keyword argument.

**N** — this is the ruled framing (`README.md:18-21`): games as rows. Without it there is one game.
**R** — *completeness at the extremes:* a row with `order: rank` needs a rank source — the title
ladder (`rosters.yaml:448-470`) — which is **data the loader can validate**; a `floor: closed` row's
witness set is `presence_only` fan-out (`:4438-4439`), which exists. **S** — ⭐ *pauses correctly*
becomes real for the first time: **the nested run is the seam nesting itself**, under the caller's
cap, rather than a second mechanism. **E, as a ratio** — the largest overhead in the suite, a loader
and a run loop, against the design's central promise. **Still no primitive.**

### What it breaks

**The provider becomes the first caller of `_fold` from inside the seam.** A scan asserting that no
provider evaluates a precondition or writes (`19_PLAN.md:453-454`) is the guard — and it **earns its
existence under §0.1 point 5**, because the artifact it guards is load-bearing on the game rather
than on this repository's process. **And the outer `speak`'s band must be chosen — see `PART F`.**

---

## P7 · ⭐ `P-04` CLOSES AT ZERO — the term is `Record.stages`, and it already executes

> **The plan's one new field is not built. Not deferred — not built.**

**Statement.** Do not build `Tenure.term`. The declared horizon this design needs already exists,
matures at MATTER citing the act that wound it, **stops when its winder is gone**, and is tested.

**Closes.** `P-04`; `19_PLAN.md` step 22's field — **the new-field count goes to zero, as that
step's own text allows** (`:620-624`); and all three of `05_PROCEDURE.md:105-118`'s open questions.

### The mechanism — none. The answers, each cited.

| the question `P-04` asked | the tree's answer |
|---|---|
| **`Tenure` or `DocketItem`?** | ⭐ **Neither: the `Record`.** `open_case` writes `Record.stages` (`verb_table.yaml:370`); `_eff_create_record` stamps `(due_tick, label, winding_act)` (`shape.py:5137-5140`); **MATTER matures the stage at `due == w.tick` and emits `term.matured`** (`:5424-5444`, declared at `write_matrix.yaml:265`) **citing the record's last change**, so `causes[]` walks |
| **Does `convene`'s `Date.due_at` already carry the summons?** | **Yes.** `convene` writes it (`:5044-5046`); CALENDAR fires it (`:5363-5381`) |
| **Is `Tenure.until` the horizon?** | **No, and nothing needs it to be.** It is a closure stamp; `live` is `until is None` |
| **An in-run limit — *"each party heard twice"*?** | A key on the opening act's payload that the provider reads. ⭐ **A clock a person wound, which is what `T-c` requires rather than what it forbids** |

⭐⭐ **AND THE BEST PART IS ALREADY WRITTEN AND ALREADY PASSING.** `shape.py:5427-5432` refuses to
mature a stage whose holder is gone:

> *"`{rid}` stage `{label}` did not mature: its winder is gone (#353 :496 — a half-made copy STOPS
> rather than finishing itself)"*

**That is `T-c`'s dividend executing**: reach the person who wound the clock and the clock stops.
`05_PROCEDURE.md` argued for exactly this as a *better game* and did not know the tree already did
it.

### Execution artifact

**Already green** — `test_tracer_is_honest.py:3926-3952` counts `term.matured` and walks its
ancestry. One assertion is worth adding inside `P3`'s test: a case record whose stage matures cites
**the opening act's emission**, not `[ROOT]` (`:5437-5438`).

### Primitive count · NERS

**−1 field against the plan.** **N** — a second horizon carrier would be `ID-2`'s second home for a
fact the record already holds. **R** — complete: the winder-gone case is the extreme, and it is
handled. **S** — one maturation mechanism for every clock in the game. **E, as a ratio** — maximal,
and it is the only proposal here where that is true: **nothing is built.**

### What it breaks

`05_PROCEDURE.md:84-128` and `19_PLAN.md:600-640` must be rewritten — **the second time in two days
that `Tenure.term` has shrunk**, and this time to nothing. ⚠ `P-33`'s *declined vs could not*
still needs `evade / defy` to execute, which is blocked on `comply`'s untyped operand
(`verb_table.yaml:115-117`) — **FI/IN work, not this lane's.**

---

## P8 · CONSEQUENCE MOVES CONVICTION — the `L-6` producer

**Statement.** `determine` writes the determiner's own convictions on the axis its disposition
aligns with, by a swept magnitude — **so `L-6` gains a sign in a forty-season run.**

**Closes.** `P-21`; `L-6`'s severance; `19_PLAN.md` step 24; `H-62`'s convictions entry;
and `P-32` in part — the normative track gets a producer.

**Mechanism.** `(Person, convictions)` is already a live RES/ACTS matrix row emitting
`conviction.moved` (`write_matrix.yaml:182-188`) with a reader at `shape.py:3503`. `determine`'s
`writes` gains `Person.convictions`; the effect adds `conviction_step × sign` to
`p.convictions[axis]`, where the axis is `align("determine", axis)`'s strongest column
(`rosters.yaml:877-903`, four axes at `:145-160`) and the sign comes from the disposition.

> **Flat in v1, deliberately.** `determine` is uncontested, so there is no band to key on. The
> degree-keyed version (`19_PLAN.md:663-667`) waits on a ruling about **what a determination rolls
> against** — which nobody has asked for, and which this suite is not asking for either.

**Execution artifact.** Three lenient findings by one judge move `p_high.convictions[axis]` by
`3 × step`, printed. **The same speech before that bench then bands differently under `P5` arm 2** —
which is the loop closing, observably. The existing invariant that WITNESS never touches convictions
(`:6448-6450`) stays green as the control. **`M-5` is the falsifier for the sign.**

**Primitive count.** **0 · 0 · 0 · 0.** One `writes` pair, one magnitude.

**NERS.** **N** — ⭐ `AX-3`'s normative half has **no producer anywhere in the game**, and this is
the one place a person is *compelled* to hold something right. **R** — no-player half: NPC benches
drift with nobody watching; *completeness:* a judge with no axis alignment moves nothing, stated.
**S** — the write is at RESOLVE, by the actor, on their own store. No fourth clock. **E, ratio** —
one line of effect against a loop nobody has been able to sign.

**What it breaks.** ⚠ **A positive loop hardens a caricature over forty seasons; a negative one
converges every bench** (`19_PLAN.md:674-675`). The magnitude is swept `{0, small, large}` and
**at `0` this proposal is inert, which is its own control.**

---

## P9 · FOLD REFUSAL KINDS AS DATA — row 15, at its true count

**Statement.** Declare the fold's generic refusal kinds in one roster and assert, over a corpus run,
that every emitted kind is declared somewhere.

**Closes.** `09_IMPOSSIBILITIES.md` row 15, **at the corrected membership** — `act.ineligible`
(`:5866`), `act.refused` (`:5913`, `:5975`), `attempt.refused` (`:6101`).

**Mechanism.** `rosters.yaml: fold_refusal_kinds: [...]`, read at the four sites. **Test:** run
`headless` for three seasons and assert
`{e.kind for e in w.log} ⊆ verb emits ∪ write-matrix emits ∪ fold_refusal_kinds`.

**Primitive count.** One roster entry.

**NERS — and this is the one place the honest score is *thin*.** **N is weak**: loader invariant 7
does not exist in the tracer, so these literals break nothing today. **What earns it a place is
`ID-12` hygiene *with a corpus-executing test*** — and had it been a guard over a checker rather
than over the log the game actually emits, **§0.1 point 5 would forbid it.** It sits near the bottom
of the ranking for that reason. **Breaks: nothing.**

---

## P10 · ATTUNEMENT'S READ IS A DEPOSIT — and that deposit is `P-46`'s enforcer

**Statement.** The provider deposits its read of the room — *who decides* — to the actor alone, at a
fidelity set by `attunement` against an injected room-opacity, **at the same confidence whether true
or misread.**

**Closes.** ⭐ **`P-46`, by relocating it.** `07_THE_GAME.md:223-227` says rule 1 has no enforcer
*because it is a constraint on a renderer*. **It is not.** The design's own mechanism
(`06_RESOLUTION.md:277-285`) is *"a MISREAD deposits at the SAME confidence with the WRONG value"* —
**and a deposit rule is testable.** Also `06` §B.1c read #1.

**Mechanism.** In the provider, at entry: `truth = judging_set(w, venue)`;
`misread = H(seed, "attunement") mod opacity > attunement`; deposit
`Observation(venue, "bench.holders", truth or a plausible wrong set)` onto the opening Event's
`observed` — **the existing `actor`-mode loop (`shape.py:6389-6423`) lands it in the actor's ledger
at the default confidence.** ⛔ **No draw, no verb, no field** — which is what §B.1c already ruled.

**Execution artifact.** A low-`attunement` and a high-`attunement` speaker in identical worlds hold
`bench.holders` claims that **differ only in `value`**; assert equality of the
`(source, confidence, when)` triple. ⭐ **That assertion is `P-46`'s enforcer**, and it is a test
rather than a hope.

**Primitive count.** **0 · 0 · 0 · 0**; one magnitude. **Breaks:** the `bench.holders` predicate must
not fall in `LEDGER_DERIVED_STEMS`; it does not. **Ranked low** — it needs `P3` and `P6`.

---

## P11 · `P-45` — the word stays with the code

**Statement.** `eloquence` is the attribute — ruled, on Jordan's own phrasing
(`06_RESOLUTION.md:110-117`), and it **reaches code** in `P1`. Fig. 14's room axis is a derived
Query with **no reader** (`03_PARAMETERS.md:481`) and is therefore reference under §0.05. **Rename
the prose axis** to what it measures — *persuasion-rewarding vs constraint-rewarding* — at
`03_PARAMETERS.md:38`, `:481`, `:483-500`.

> **Why this direction and not the other.** §4's test is whether a later session reading the word
> cold lands on the same meaning. **After `P1`, `eloquence` appears in executable code as a
> `Person.capability` key and nowhere else.** The room axis appears only in prose. So the collision
> resolves itself in the reader's favour by renaming the half that never becomes a mechanism.

⚠ **Execution artifact: NONE of its own.** It rides on `P1` reading `capability["eloquence"]`.
**Under §0.2 this is a naming closure, not a juncture, and it is listed here so that it is not
mistaken for one.** **Count: zero. Breaks: nothing.**

---

# PART C · THE ORDER, AND THE SHORTEST PATH

```
   (P1 steps 1–2: roster + contracts) ─┐
                                       ├─►  P1  provider + dispatch   ◄── the count goes 0 → 1
   P4  tell's product  ────────────────┤        one PR · four files · one test
        independent; may land first    │
        or in parallel                 │
                                       └─►  P2  speak row · effect · grammar branch
                                                 convene's holder · the gate
                                                  │
                                                  └─►  P3  judging_set · determine   (F8/F21 flip)
                                                        │
                                                        ├─►  P5  reception
                                                        │      needs P2's stance write + P3's bench
                                                        │        │
                                                        │        └─►  P6  loader · nested run · veto
                                                        │              · rename-invariance
                                                        │                │
                                                        │                └─►  P10 attunement deposit
                                                        │
                                                        └─►  P8  conviction producer
                                                               feeds P5's second arm

   P7  P-04 closes NOW, by citation      (one assertion added inside P3's test)
   P9  refusal roster                    (any time)
   P11 P-45                              (any time; prose)
```

## ⭐ The shortest path, stated so it can be executed without its author

**Two roster values** (`rosters.yaml:444-445`) · **one registry row**
(`references/module_contracts.yaml`) · **one dispatch table** (`shape.py:6740`) ·
**`proceedings_seam.py`** · **`test_pr_the_margin_branch_has_its_first_producer`**.

**No verb-table edit** — the test sets `Act.contests` directly. **No ruling. No new primitive.**

**Red at `shape.py:6766` today. Green with a degree on the Event and a stable hash.** Everything
after it is what makes the running thing a game.

## Two ordering rules that are not preferences

1. ⛔ **`P1` before `P2`.** Otherwise every corpus case that speaks becomes a DESIGN-GAP at
   `:6766` — the seam raises before it returns.
2. ⛔ **`P2`'s `resolvable_verbs` narrowing lands in the SAME COMMIT as its `contests:` column.**
   Otherwise the corpus's executed set flips twice, and the second flip masks the first.

---

# PART D · THE CONFLICT MATRIX

**The owner's requirement is *"without causing conflicts"*, which is a property of the suite rather
than of any proposal, so this section is load-bearing rather than decorative.**

| proposals | the shared mechanism | how it resolves |
|---|---|---|
| **P1 × P2** | how a `speak` reaches the seam — `Act.contests` vs `row.contests` (`shape.py:6115`) | **both admitted by the same line.** `P2` supersedes `P1`'s test setup; `P1`'s test keeps working unchanged |
| **P1 × P5 × P6** | the obstacle composition | ⭐ **ONE function** — `proceedings_seam.obstacle()`, enumerated once (`06_RESOLUTION.md:669-697`). `P5` fills a declared slot; `P6` supplies `aptness` and rung inputs. **Neither creates a second composition site**, which is why `P1` ships the zero-valued terms rather than omitting them |
| **P1 × the prize name** | `"a proposition"` (exists) vs `"a matter"` (coined) | **the existing name wins**, on `ED-SC-0033` (2) + §4. `04_VERBS.md:74`, `08_SEAM.md:60-73`, `README.md:112-116` and `02_THE_SOCKET.md:207-221` are rewritten in `P1`'s commit |
| **P2 × P4** | ledger pressure at the 200 cap (`:1772`, `:6429`) | **both increase deposits.** `M-1` runs after both and before `P5` reads person-claims across seasons |
| **P2 × P3** | `DocketItem.matter`'s producer | `P2`'s `_eff_convene` fix populates it; `P3`'s predicate reads it; **`judging_set`'s third parameter waits on it** |
| **P3 × `04_VERBS.md:303`** | `determine`'s `writes`, which the file says is UNCHANGED | **one extra pair**, because `commit` has no effect (find 7). **A finding against the file, not a design change** |
| **P4 × H-122** | two recipient rules at one barrier | **kept as two loops** — reads → actor via `observation_deposit_mode`; product → observers via the column. `H-121`'s lesson (`:6355-6360`) forbids one fixture carrying two decisions |
| **P5 × P8** | `Person.convictions` — `P8` writes, `P5` arm 2 reads | **a dependency, not a conflict.** `L-6` is measurable only with both |
| **P6 × P1** | `degree_of`'s ladder call gains `extension=` | **`P6` owns the change.** `P1` returns no extension and the ladder is unmodified |
| **P7 × `19_PLAN` step 22 / `05_PROCEDURE` §B.1** | `Tenure.term` | **deleted from the plan. The field is never built** |
| **P3 × probes F8/F21** | `judging_set` raising *was* the asserted behaviour | **probes rewritten as passes in `P3`'s commit** |

⚠ **ONE INCONSISTENCY IN THE PLANNER'S OWN OUTPUT, RESOLVED HERE RATHER THAN INHERITED.** The
planner's dependency graph and conflict matrix both referenced a **`P12`** that its suite never
defined — *"P12-half (roster + contracts)"*, *"P1 × P12: the prize name"*, *"P12 orphans it"*.
**There is no `P12`.** Its content is `P1` steps 1 and 2, which is where it belongs: the repoint is
not separable from the provider it points at, because a repointed prize with no provider is a
louder refusal rather than a running one. **Renumbering is refused** — the suite is `P1..P11` and
nothing is missing.

---

# PART E · WHAT IS DELIBERATELY NOT PROPOSED

**`CLAUDE.md` §G.4.5's five tests run before anything is escalated: superseded · irrelevant ·
answered by a design document · answered by precedent · answered by what makes sense for the
architecture.** A stale open row closed with a citation is a real result, and the 156-row queue
that motivated that ruling is why this section exists.

| item | test | disposition |
|---|---|---|
| **`P-03` / `Act.via`** | **precedent + not this lane** | It is `H-108`, a meta-architecture schema column whose `unblocks:` names regency and governors. **A seat-holder already acts as their seat** through `_eligible` (`:5757-5762`). And the form-7 conjunct is **doubly** unevaluable — there is no `basis` stem in `REQUIRES_STEMS` (`:1247-1250`) — so it is unloadable regardless of `via`. **Leave with IN** |
| **`P-04`** | **answered by the tree** | Closed at zero cost. `P7` |
| **`P-01` · `P-15` · `P-29` · `P-36` · `P-37` · `P-41` · `P-43` · `P-44` · `P-48`** | **superseded** | Already closed in the register by rulings. **Nothing to do** |
| **`P-25`** (the `score/2` derivation) | **superseded, and SUSPENDED** | `ED-SC-0033` (3) gives the obstacle a single owner *for this subsystem*. The cross-tree reconciliation is **suspended by Jordan (2026-08-21)** (`dice_engine.py:250-252`). **`P1` derives inside the seam and edits no opposed site** |
| **`P-02`** (Receipt) | **not load-bearing here** | IN's `1g`; eleven append sites; no bearing on the twelve games |
| **`P-07` · `P-09` · `P-11` · `P-12` · `P-14` · `P-18` · `P-26` · `P-27` · `P-28`** | **answered by `ID-6`** | Each is *inject, declare, sweep* or *run it*, on the register's own grading. **They become fixtures and sweep arms inside `P1`/`P5`/`P6`** — not proposals, and **not escalations** |
| **`P-10` · `P-13` · `P-19` · `P-31` · `P-38`–`P-40` · `P-42`** | **irrelevant here, or a measurement** | Data edits, FI's, or measurements (`P-42` **is** `M-1`). ⭐ **`P-31` — the grade-column rewrite — is discharged by `P1`–`P6` making the grades executable**, rather than by rewriting the column |
| **`P-33`** (why the subject is absent) | **blocked elsewhere** | Needs `evade / defy`, which cannot execute (`verb_table.yaml:202-214`, untyped on `comply`'s operand). **FI/IN grammar work** |
| **`L-5`** | **not signable yet** | Interposition does not exist in code. **Signable only after `P6`, and then as a measurement** |
| **`09` row 9** (a stored tally) · **row 10** (a `bias` field) | **refusals by absence** | The only lawful guard is a field-name scan for `count\|tally\|votes\|quorum_reached` (`19_PLAN.md:475-476`), folded into `P6`'s test. **Not separate proposals** |
| **A new verb, of any kind** | ⛔ **`ED-SC-0036`** | **Nothing in this suite adds a roster name.** `product` is a column; `LicenceVeto` subclasses a seam the engine already exposes |
| **The `systems/social_contest/` retirement wave** | **ruled, cross-lane** | Not this suite. **`P1` orphans it; nothing here reads it** |
| **`19_PLAN.md` steps 1–4** | **IN's, mostly — and two are discharged sideways** | Season-loop changes, not proceedings changes (`HANDOFF.md:42`). ⭐ **`P4` mints `told_by`, which is step 4(c)'s core; `P2`'s stance write supplies speaker attribution without step 2's rule change.** The fan-out default and the want/fear term stay IN's |

---

# PART F · WHAT GENUINELY NEEDS A RULING — one item

> ### **WHICH DRAW BANDS THE OUTER `speak`?**

**The problem, stated so it can be decided without re-deriving it.** The fold bands one act with one
`Resolution` (`shape.py:5814`, `:6182`), and the seam returns one Margin (`08_SEAM.md:16`). **Once
`P6`'s nested run exists, a hearing is many draws** — but the season-level Event, the one every
witness deposits from, must carry exactly one degree.

| option | what it makes true |
|---|---|
| ⭐ **the opening speech's own draw** | The act being banded is the act that opened it. A speaker's stance write depends on **how they spoke** |
| **the disposal's degree** | A speaker's stance write depends on **how the whole hearing ended** — so a brilliant speech before a bench that ruled against you writes a loss |

**These are materially different games**, which is the test. `19_PLAN.md:984-988` already names this
as the plan's weakest joint and picks the first; the second has never been argued.

**It survives all five tests:** nothing rules it; nothing retires it; no design document decides it;
**no precedent exists** — combat has one draw, so the tree has never faced the question; and both
are clean engineering answers.

⭐ **The default this suite injects if it goes unruled: the opener's own draw, declared and swept
against the disposal's.** Reason: the act being banded is the act that opened it. **`ID-6` — inject,
declare, sweep — rather than blocking on an answer.**

**Everything else** the register or the readout marks as a decision — the prize name, whose
`composure` is halved, the term carrier, refuse-vs-demote, the six acts' stratum — **is answered
above by a ruling, a precedent, the tree, or an engineering call, and `PART E` says which.**

---

# PART G · THE STANDING WEAKNESSES OF THIS SUITE

**Named here rather than left for a reader, because a remediation document that reads as clean is
the one to distrust.**

1. ⚠ **Find 7 is not fixed.** Six of the seven inert "reused" verbs belong to other lanes. This
   suite adds an effect for `determine` only. **`04_VERBS.md`'s economy claim needs rewording, and
   this suite does not make it true.**
2. ⚠ **`P1`'s `R` is genuinely short in both halves** — no NPC reaches it, and the obstacle is
   computable — and it is still ranked first. **That is a deliberate ordering of `N` over `R`**, on
   the ground that nothing else can run until it does. A reader who disagrees should reorder, not
   re-argue.
3. ⚠ **`P5`'s `T-f` guard is a source grep and a type annotation.** The tracer has no `decision/`
   package to path-scan, so **`09_IMPOSSIBILITIES.md` row 3's "STRUCTURAL (typed)" is stronger than
   what the tracer can currently support.**
4. ⚠ **`P9` is the thinnest `N` in the suite** and is only admissible because its test executes over
   the game's own log. **If it drifts into guarding a checker, §0.1 point 5 deletes it.**
5. ⚠ **`P4` will move the ledger cap into contention** and the suite's answer is *run `M-1`* — which
   is a measurement, not a design. **If the cap evicts firsthand claims that `P5` needs, `P5`'s term
   decays for a reason nobody modelled.**
6. `[UNVERIFIED]` — whether `register.py --check` requires a `cite:` when `H-32` moves from
   `assumption` to `measured` (`P3`). Neither reader opened it.

---

*The adversarial pass on this document, and its reconciliation, are recorded in the commit that
lands it — `CLAUDE.md` §0: the adversarial pass is a STAGE, not a deliverable.*
