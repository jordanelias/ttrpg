# The unified build order — one program, two suites

## Status: **PROPOSED (2026-09-17). HELD BACK IN FULL. NOTHING RATIFIES ON MERGE.**
## Lane: `IN` · **`ED-IN-0243`** (shared with `00`)
## Grade under `CLAUDE.md` §0.2: **`paper`.** Nothing in this order has run. Phase 1 item 1 is the first thing that would.
## Reads: `00_THE_SEAM.md` for why these two suites are one program. `RULINGS.yaml` for what is still Jordan's.

---

## What this file owns, and what it does not

**It owns the ORDER and the six seam insertions. It owns nothing inside either suite.**

| question | answered by |
|---|---|
| what item `N` changes, why, and what proves it | **`../2026-09-17-governance-and-holdings-r2/EXECUTION_PLAN.md`**, and `05_LEDGER_AND_BUILD.md` §A.4 behind it |
| the deletion arithmetic, the citations, the controls | `05` §A.1 and §A.4 |
| what the behaviour layer's terms ARE | `../2026-09-16-conviction-decision-layer/synthesis.md` |
| **in what order, and with what inserted between** | **this file** |

**Where this and the r2 `EXECUTION_PLAN` disagree on an item's contents, the `EXECUTION_PLAN` wins** —
it carries the reasoning and the citations and this file carries neither. This file may reorder its
items and may require an additional edit inside one; it may not change what an item *is*.

---

## The shape of the program

```
PHASE 0   the seam repairs          7 repairs · no ruling needed · must precede the items they touch
PHASE 1   the critical path          6 items · no ruling needed · buildable today
PHASE 2   the writ and the word      4 items · one carries a seam repair
PHASE 3   seats and content          4 items · one gated on CAT-6
   ── THE APERTURE RE-MEASUREMENT GATE ──   ← the behaviour layer's numbers are re-taken HERE
PHASE 4   works and founding         1 item
PHASE 5   blocked                    2 items · one on RR-A, one on ratified positions 3–5
PHASE 6   the behaviour layer        gated on RULINGS.yaml, and on the gate above
```

**Phases 1–4 are fourteen of r2's sixteen items in dependency order.** Phase 6 is everything #409
wants. The gate between them is the one structural addition this unification makes, and §4 below is
its argument.

---

## PHASE 0 · The seam repairs

Seven small edits. **None needs a ruling from Jordan** — `RULINGS.yaml` ran all 21 open questions
through `CLAUDE.md` §0's five-step gate and **closed 12**, which converts three of these repairs from
*decisions to be taken* into *instructions already answered*. Each exists because two documents written
a day apart wanted the same object.

| | repair | why now | precedes |
|---|---|---|---|
| **S1** | **CAT-6 gains a fourth arm** — r2's commission-claim route, stated in r2's own words with its `03_SEATS_AND_CONTENT.md:794` citation. The three original arms stand | Jordan must not rule H-71 from a menu missing the option that already has a build item attached | the CAT-6 ruling, and item 11 |
| **S2** | **One instrument for the told-channel control.** #409's M3 (12-person harness) and r2's `01`/`02` (`harness.populated 1`) measure the same channel at different scales. Pick `harness.populated`, re-take M3 on it, record both numbers | §0.1 pt 4 — a number without a control is not a measurement, and two arms that are different experiments is the ED-MB-0042 confound exactly | item 8 |
| **S3** | **The teller field rides WITH item 8.** One edit to `witness.py:315-369` adds both the lossy copy at `Partial` and the teller's identity on the deposited Claim | two edits to one function, and item 8's falsifier is stronger with the teller present. ✅ **CAT-3 is now CLOSED at step 5 — *store the teller*** — so this is an instruction, not a choice. It is also **one extra positional argument** (`_act.actor`, in scope at `:316`), not the schema change both suites priced | item 8 |
| **S4** | **STR-4's fold-rule constraint is carried into item 2a.** `aggregate_questions` re-mints the Question keeping only `source`, `about` and a flattened referent union — so the new `reach` source must declare how it folds | ✅ **STR-4 is CLOSED at step 5 — *no type dimension; fix the gate*** — and the two suites reached that from opposite ends, which is step-4 precedent arriving twice. What survives is the **fold rule for `reach`**, which item 2a owes regardless | item 2a |
| **S5** | **Item 7 records in one line that `operands` stays four-field**, so `benefits_me(c)` knows what it inherits | ✅ **CAT-2 is CLOSED at step 5 — the beneficiary is a *static column on `verb_table.yaml`* resolving to a carrier the Candidate already holds, explicitly NOT a fifth field.** So the feared ordering **does not exist**: a static column never touches `_derive_operand`. S5 shrinks to a one-line note and item 7 is independent of CAT-2 | — (**no longer an ordering**) |
| **S6** | **The aperture re-measurement is scheduled, not assumed** — see §4 | #409's CAT-6 evidence and STR-4's conclusion are inferences from a shut aperture that phases 1–3 open | Phase 6 |
| **S7** | **Item 8 carries a falsifier for its effect on `standing_of`.** Populating `told_by` moves `standing_of` (`decision/options.py:443-465`) off its measured `1000`-for-everyone default — CAT-9's carrier, a category item 8 does not think it touches | `00` §3.6. The effect is real, wanted, and **unfalsified in both suites**: item 8's own falsifier licenses *"one drifted operand"*, and that drift lands in the `c.value` `agreement()` diffs | item 8 |

> ⚠ **S1 and S3 are the two that cost something if skipped, and they fail differently.** Skipping S1
> produces a *ruling* taken on a stale option set — silent, and discovered only when item 11 contradicts
> it. Skipping S3 produces a *second edit to a function already edited this program* — loud, cheap to
> fix, and it invalidates item 8's recorded falsifier. **Neither is expensive. Both are expensive later.**
>
> ⚠ **And S1 grew a price after it was written.** `00` §2(b): **arm 2's carrier, `Tenure.payload`, is
> deletion-ledger row 13 in r2's own `05`**, and ratified `ARCH §B.8` prescribes its replacement. Arm 2
> is therefore not a free menu choice any more — picking it is an `RR-B`-shaped amendment. **S1 must
> put that price on the sheet**, or the four-arm menu is honest about its options and dishonest about
> their cost.

---

## PHASE 1 · The critical path — six commits, no ruling, buildable today

Straight from the r2 `EXECUTION_PLAN`, unchanged. This is the part of the program that needs nobody.

| # | change | size | depends on |
|---|---|---|---|
| **1** | `@effect_for("commit")` — mint the Tenure the `commit` row already declares | S | — |
| **16** | `add_tenure`'s hold-object guard; re-home the 16 faction rung-holds to persons | S | — ⚠ **before 10** |
| **4** | delete `budget_office_bonus` | S | — |
| **3a** | `nearest_store` + the per-eater draw | M | — |
| **3b** | the body write · shared `_crossings` · `remove_person` | M | **3a** |

⚠ **Two path defects in the r2 plan, reported at `00` §7 and NOT repaired here:** its Trap 5 and item
3b cite `engine/season/loop/budget.py`, which does not exist — the live reader of `band_floors["body"]`
is **`engine/season/decision/budget.py:73`** — and *"`band_floors.person` refuses at load"* is really a
`KeyError` at the access site, since nothing cross-checks a table's cells against its `keys:` roster.
**The traps are real; build to the corrected paths.**
| **2a** | `reach` · `place_of` · two question sources deleted · `w.crossings` deleted · `occasioned_by` → one route | M | **S4** |

**Item 1 first, and it is ~12 lines.** `commit` is Q4 `need`'s producer, `need` is already 81 questions
on the populated world, and every one is hand-minted by the harness because no act can make one today.
⚠ Its trap, from the plan: *an effect body that touches nothing makes the fold emit the refusal* — the
body must return the object it opened.

**Item 16 is a precondition, not a tidy-up.** `in_holdings` is false for every person over every rung,
so a seat whose `revocation` is `"holdings"` refuses every revocation forever *while looking exactly
like a working precondition*. Land item 10 first and you ship a row that cannot execute when reached.

---

## PHASE 2 · The writ and the word

| # | change | size | depends on |
|---|---|---|---|
| **5** | the Record-kind fold — `record_kinds` + its refusal · `issue`/`petition` bodies · 2 matrix rows and 2 `World` dicts deleted · the deposit rule | **L** | 2a |
| **6** | `give` + body + `_req_give` + release-before-mint | M | **5** |
| **8** | `tell` at `Partial` deposits a lossy copy — **and the teller's identity** (S3) | S | 5, **S2**, **S3**, **S7** |
| **7** | content-claim operands; Q2's third clause — **and S5's invariant statement** | M | **5, 6, S5** |

Item 5 is the largest single item in the program and everything in phases 2–4 hangs off it.

---

## PHASE 3 · Seats and content

| # | change | size | depends on |
|---|---|---|---|
| **10** | `offices.yaml` — bases as rostered values · both predicates rewritten · four title helpers + `is_title` + the `titles` roster deleted · holders seated · purview corrected | **L** | **4, 16** |
| **11** | commission `Record` on `confer`; person-side `remit:` via the claim | M | **5, 10, and the CAT-6 ruling after S1** |
| **9** | obligees co-located mint `inferred` · `oblige` body · `establishment_of` rewritten with a caller · `Office.establishment` deleted | M | 1 |
| **14** | the 13 field deletions + `judging_set` + `conferral_path` | S | **9, 10** |

⚠ **Item 11 is the one item in phases 1–4 that acquires a ruling dependency under this unification,
and that is a gain rather than a cost.** r2 filed it as unblocked because r2 read H-71 as closed by its
own `03` §A.11. #409 has the same hole open as a three-option question. **S1 makes them one question
with four arms; item 11 then waits on its answer instead of pre-empting it.**

---

## ── THE APERTURE RE-MEASUREMENT GATE ──

**Fires once, after phase 3. It is a measurement, not a build item, and nothing downstream may be
scored before it passes.** §4 is its argument.

| re-take | was | instrument |
|---|---|---|
| verbs resolvable / table rows | **18 / 38** | `resolvable_verbs()` |
| verbs unformable person-side | **10 of 38**, every governance verb | `person_side_eligible` over the roster |
| claims by source, one populated season | `{firsthand: 2174, told_by: 1}` · `inferred: 0` | `harness.populated 1` (S2's instrument) |
| questions by source | the histogram before item 2a | `questions_for` |

**Then, and only then, re-take #409's CAT-6 evidence block and STR-4's conclusion against the new
numbers.** Both are *inferences from a shut aperture*. Re-citing them is not the same as re-taking them.

---

## PHASE 4 · Works and founding

| # | change | size | depends on |
|---|---|---|---|
| **12** | `works` kind · `work` advances `stage` · `restore` body · `found` + body · `(Rung\|Site, exists)` get a producer | **L** | **5** |

This is the phase that answers `ARCH`'s own `F.20` — *"the world only decays — nothing is ever founded
or built"* — which `architecture/meta/04_CODE_ARCHITECTURE.md:1082` files as one of two gaps that
*"block the build outright"*. It is also the R-half with no player in it under `CLAUDE.md` §0.06.

---

## PHASE 5 · Blocked, and on what

| # | change | blocked by | can it start? |
|---|---|---|---|
| **13** | RR-A's four verb deletions + `remit_acts.dispatch` | **`RR-A`** — folding the four response verb rows overwrites `ED-IN-0210`'s letter | **No.** Jordan's |
| **15** | `Act.via` + F3 | ratified **positions 3–5**; it is the Arc-2 gate itself | No |

---

## PHASE 6 · The behaviour layer

⚠⚠ **THIS PHASE WAS WRITTEN AS UNSCHEDULABLE AND IS NO LONGER.** The first draft read: *"Everything
#409 wants sits here, and none of it is schedulable yet — 15 rows with a `ruling:` field, 0 filled, and
STR-1 gates five of the nine categories simultaneously."* **`RULINGS.yaml` closed 12 of the 21, eight
of the nine `CAT-*` rows among them, and STR-1 fell first** — at gate step 3, on the ratified matrix's
own words: the six `[RES] ACTS` rows are **a licence nobody has taken up, not a prohibition**
(`00` §5).

**What is still Jordan's here is four questions, and they are one shape — a roster and a naming pass:**

| | still escalated | what it holds up |
|---|---|---|
| **CAT-6** | H-71, now over **four** arms (S1) | r2 item 11, and every governance verb person-side |
| **STR-2** | which axes the moral-value basis carries | the `alignment` table's shape — **migration is atomic**, so it cannot be done twice |
| **STR-5 + STR-6** | the vocabulary, escalated as **one decision over five words**: `belief` · `conviction` · `piety` · `temperament` · `stance`/`Disposition` | every table and vector named below |

⚠ **`temperament` is not a free name** (`00` §7.5): `descriptor_registry.yaml:298` already carries
`temp.*`, *"5 territory temperaments"*, at territory/faction scope. #409 names its entire second basis
on it. **STR-6 catches this exact two-scales-one-word failure for `piety` and misses it for
`temperament`.**

**What phases 1–4 hand it, which is the point of the unification:**

| #409 needs (`synthesis.md` §3) | supplied by |
|---|---|
| **the medium** — the second-hand channel carries nothing; susceptibility has nothing to calibrate | **item 8 + S3** — the lossy copy gives the channel a signal, the teller field gives the ladder its operand |
| **the aperture** — 10 of 38 verbs unformable, every governance verb | **items 1, 10, 11, 12** and the gate above |
| **a beneficiary per candidate** for `benefits_me(c)` | **item 7 + S5** — the invariant is stated where the binder is touched |
| a beneficiary for `benefits_me(c)` | ✅ **CAT-2 closed** — a static `verb_table.yaml` column, not a Candidate field. **Buildable now** |
| the person-interior writers (`press`, `scar`, the needs counter, regard) | ✅ **STR-1 closed at step 3** — a verb at RESOLVE writes it, as the matrix already prescribes. **Buildable now**, and it was the claimed blocker for five categories |
| the tables (`alignment` past a third, the bearing table, `serves`) | nothing here. **#409's own work** — but the axis roster is **STR-2**, still Jordan's, and atomic |
| the held vectors, and what they are CALLED | **STR-5/STR-6**, still Jordan's |

**The order within phase 6 is still not this file's to set** — but the reason has changed. It is no
longer *"nothing is ruled"*; it is that **STR-2 is atomic and STR-5/STR-6 name everything the phase
builds.** Rule those three and phase 6 orders itself, from the re-measured numbers rather than the
register's.

---

## §4 · Why the gate exists — the one structural claim this unification makes

Neither suite states this and it is the reason they cannot simply be concatenated.

> #409 `synthesis.md` §3, on its own falsifier: `P(inversion) = 1/(1 + e^{Δ/τ})` at the shipped
> `τ = 0.1` — a term changes what a character does at 95% only when it moves the score by
> **Δ ≥ 0.294**. *"Every term above needs a declared range against that floor. A term that cannot
> clear it is decoration, however well-motivated."*

**A term's range is bounded by what the world offers it to range over.** Measure `serves(candidate,
item)` against an aperture where 10 of 38 verbs never form and every governance verb is among them,
and it reads below the floor — for a reason that is about the **world**, not the term. Measure
susceptibility on a channel depositing one `told_by` claim a season and it reads below the floor for
the same reason. **Build #409 first and its own falsifier condemns terms that are fine.**

That is a stronger dependency than sequencing. It says #409's central instrument **cannot be run
honestly** until phases 1–3 land, and a session that ran it anyway would produce a table of
well-measured, confidently wrong verdicts — the failure `CLAUDE.md` §0.1 pt 4 names: *"a number
without a control is not a measurement — in either direction."*

**And the converse is deliberately NOT claimed.** r2 without #409 is not blocked; it is merely
incomplete. It builds a world that delivers rich input to a chooser that ranks it with an `alignment`
table one-third full and breaks ties alphabetically — measured in #409's `behaviour_algorithms.md`
as a plateau of 2.2 tied candidates resolved by the verb's name. **A defect, not a blocker.** The
dependency runs one way and this file does not pretend it runs both.

---

## §5 · What would show this order wrong

Falsifier prefix `BO-n`. Each is written to be runnable, not persuasive.

| | claim | what would refute it |
|---|---|---|
| **BO-1** | items 1, 16, 4, 3a, 3b, 2a need no ruling | any one of them touches a `## Status: RATIFIED` sentence, or `RULINGS.yaml` lands it on an escalated row. ✅ **Run: none does.** The only escalated row touching phases 1–4 is `CAT-6` → item 11, and `RR-A` → item 13, both already outside the critical path |
| **BO-2** | the aperture gate is necessary — #409's terms cannot be scored before it | a term whose declared range clears **Δ ≥ 0.294** on the **pre**-phase-1 tree. One such term and the gate is merely tidy |
| **BO-3** | item 11 genuinely waits on CAT-6 | CAT-6 closes at gate step 1–4 in `RULINGS.yaml` — then S1 was bookkeeping and item 11 was never blocked |
| **BO-4** | ~~the six seam points are all of them~~ → **the SEVEN seam points are all of them** | an eighth found in code. ⚠ **This falsifier has already fired once.** It was written while a verifier was searching; the search returned `standing_of` (`00` §3.6), the count went six → seven, and S7 was added. **A completeness claim that has failed once is not evidence for the next one** — the standing instruction is that any consumer of an object phases 1–4 change is a seam candidate until checked |
| **BO-5** | phases 1–4 are fourteen items in a valid dependency order | any edge in the r2 `EXECUTION_PLAN` that this order violates. `05` §A.4 is the oracle, and it wins |
| **BO-6** | `(Person, body)` needs no STR-1 ruling | ✅ **Discharged.** STR-1 closed at step 3 and its subject is the six `[RES] ACTS` rows; `(Person, body)` is `[MAT, RES] MATTER/ACTS` and is not among them |
| **BO-7** | phase 6's remaining gates really are only `CAT-6`, `STR-2`, `STR-5/6` | any closed `CAT-*` row whose close does not survive an independent re-run of `CLAUDE.md` §0's gate. **Twelve closes, each with an opened citation — the falsifier is to re-open them** |

---

## §6 · What this file does not do

**It marks no juncture done.** `CLAUDE.md` §0.2 — a juncture is done when the behaviour EXECUTES, and
a tick in a table is not an execution artifact. Every item above carries one in the r2
`EXECUTION_PLAN`; **nothing here has run.**

**It ratifies nothing, and `ED-1094`'s merge-ratifies-by-default is refused in full** for this
directory, as it is for both subject suites. No `## Status:` line flips, no ledger `status` or
`needs_jordan` field changes on merge, and `CURRENT.md` is untouched.

**It adds no build item.** Fourteen items are r2's, two are r2's and blocked, **seven** are seam repairs
that exist only because two documents wanted one object — or, in S7's case, because one document
changes an object a second document reads without either noticing. **Phase 6 is a placeholder with no schedule and
this file declines to give it one.**
