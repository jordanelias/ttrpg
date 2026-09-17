# 05 · THE LEDGER AND THE BUILD — what this suite deletes, what it adds, in what order, and what Jordan must rule

## Status: **PROPOSED (2026-09-17). HELD BACK IN FULL. NOTHING RATIFIES ON MERGE.**
## Method: `opus` author, read-only against the working tree at `46aa21d`. Every `path:line` below was opened in this session before it was written, and every count was re-measured with the command printed beside it. Four documents were authored **concurrently** from one plan; where my measurement and the plan disagree, **my measurement is in the text and the plan's figure is struck beside it.** Repairs in the APPENDIX.
## Grade: **`paper`** (`CLAUDE.md` §0.2). **Nothing in this suite has run.** This file's own first execution artifact is build item 1's. Two probes in §A.2 and one ladder in §A.4 item 3b DID execute in this session; they measure the TREE, not the design, and they are labelled EXECUTED where they appear.
## Lane: **IN**, sharing **`ED-IN-0233`** with `01_ATTENTION_AND_REACH.md` — same lane, same commit. **This file introduces no design claim of its own.** Its two objects are the COUNT (§A.1) and the ORDER (§A.4); everything else it states belongs to `01`–`04` and is cited to them. It allocates no id and edits no ledger.
## Conventions: **`ARCH`** = `architecture/meta/04_CODE_ARCHITECTURE.md`, cited **`§Letter.Number`** and never by line. **`AX`** = `architecture/meta/01_AXIOMS.md`, cited `AX-n` / `AX §Letter.Number`. **`holonic`** = `architecture/holonic_ARCHITECTURE.md`, cited `holonic §NN.N`. A bare **`01`–`05`** means a file in THIS directory. `path:line` is for `engine/` files only. This file's falsifiers are **`LB-n`**. Corrections are struck-and-kept: `~~old~~ → new`.

---

> **Jordan, on the remit this suite was written under:** *"I do not want this work to be constrained
> by existing work. I want the best possible design ideas and concepts, and we can modify code
> accordingly."*
>
> **Jordan, on why `done` had to be redefined (`CLAUDE.md` §0.2):** *"I need to break out of the
> infrastructure loop."*
>
> **And the sentence that makes this file worth reading or worth deleting:** `CLAUDE.md` §0.2 —
> *"A milestone juncture is done when the behaviour EXECUTES. Not when a document exists with a
> `## Status:` line."*
>
> ⚠ **SO READ EVERY ROW OF §A.4 AS A THING THAT HAS NOT HAPPENED.** Each is a prediction with a
> named falsifier, a named control and a named execution artifact. The document you are holding is
> worth exactly as much as the first row somebody executes, and no more.
>
> ⚠ **AND READ §A.1 AS THE ONE CLAIM IN THIS SUITE THAT COULD BE FALSE BY ARITHMETIC.** Round one
> claimed net deletion and was net **+17** in code (`AUDIT_VERDICT.md`, E-OVERHEAD: *"code in ~27
> against code out ~10 … 'Net deletion' holds only against a counterfactual that never existed in
> code (14 design-only verbs, a siege subsystem), not against the tree"*). **Every row below names
> a path and what reads it today.** If a row is wrong, the net is wrong, and the suite's central
> claim falls with it.

---

# PART A · THE LEDGER, THE CHANGES, AND THE ORDER

## A.0 · The counting rule, and the three rules that decide the order

### A.0.1 · THE COUNTING RULE, stated once so it is never re-derived

> **One row per NAMED thing a reader of the engine must currently hold and would no longer:** a
> verb-table row · a roster member · a dataclass field · a Query function · a helper function · a
> `World` collection attribute · a `write_matrix.yaml` row · an `@effect_for` body · a
> `@requires_predicate` entry · a named fixture cell that code reads at runtime.

Four consequences, each taken deliberately and each stated because it can be argued the other way:

1. **An `@effect_for` body for a verb row that already exists counts as +1.** It is a new function
   with a name. Counting it 0 — on the ground that "the row was always there" — would be the
   favourable unit, and §0.1 pt 4 forbids reporting only that one.
2. ⚠ **A MOVED OR FACTORED FUNCTION COUNTS +1, AND ITS NAMED PREDECESSOR COUNTS −1. THIS
   REVERSES THE PLAN AND IT REVERSES THIS FILE'S OWN FIRST DRAFT** (§A.1.6). ~~A moved function
   counts 0, because a reader holds the same concept in a new place.~~ → **A reader holds a NAME,
   not a concept**, and three of this suite's additions are new names: `place_of` (a new signature
   with two limbs `_event_place` does not have), `World.remove_person` (factored from `_eff_kill`'s
   inline cascade), `_crossings` (factored from `matter.py`'s inline site block). `_event_place` is
   a name that goes, so it is counted out; the other two predecessors are **nameless inline code**,
   so nothing comes out against them. **The scheme therefore costs the ledger two objects it would
   otherwise have hidden**, and that is the reason to adopt it.
3. **A nameless code path inside a function that itself survives is NOT a separate object.** The
   `is_title` branch inside `_req_revoke`, and `occasioned_by`'s generic id search, are deleted code
   and are not deleted objects — `_req_revoke` and `occasioned_by` both survive. ⚠ **`01` counts
   `occasioned_by`'s id search as an object and this file does not**; the divergence is one row and
   it is stated in §A.1.6 rather than averaged.
4. **A named RULE counts +1** — the deposit rule, the release-before-mint rule. A rule this suite
   gives a name to is a thing a reader must hold, whether or not it has a `def`.
5. **Content counts 0.** `engine/season/data/offices.yaml`'s rows, a fixture VALUE, a `titles`
   domain — these are what the game is about, not objects a reader must hold. **A fixture NAME
   counts 1**, because a name is a thing code says out loud (`budget_office_bonus` is the worked
   case: the cell is content, the name is mechanism).
6. **A `(kind, field)` matrix row and the field it names are TWO objects.** They are in two files
   with two loaders and two failure modes, and `matrix_rows_without_a_field`
   (`engine/season/state/carriers.py:599`) exists precisely because one can outlive the other.

**This section is the single owner of the count.** `01`–`04` point here; none of them states a net.

### A.0.2 · THE GATE-CONTRACT RULE — carried forward from round one `04_BUILD_ORDER.md` §A.0.1, unchanged

> **A piece of work is downstream of the Arc 2 gate contract (ratified positions 3–7) IF AND ONLY
> IF it is an `@effect_for` body, or it writes a Tenure whose subject is not the actor. Everything
> else is order-free.**

**MEASURED 2026-09-17:** `grep -c "@effect_for" engine/season/loop/effects.py` → **11**. Paying
Arc 2 first costs 11 effect rewrites once; not paying it first costs 11 + N later. The ratified
program's position 7 states the same number: *"`NoOpReceipt`; the effect contract finalised; **11
effects rewritten once**"* (`workplans/2026-09-11-reconciled-program.md:140`).

> ### RULED: **BY THE LITERAL RULE, EVERY ONE OF THIS SUITE'S SEVEN EFFECT BODIES IS ARC-2-FLAGGED. WE BUILD THEM ANYWAY, AND THE ARGUMENT IS RR-C's.**
> Not a loophole and not a re-reading. The rule fires; the flag is real; the cost of being wrong is
> **a re-run, not a rewrite**, and that is the whole of the argument:
>
> | | if we wait for G4 | if we build ahead (this file) |
> |---|---|---|
> | effect rewrites | 11, once | 11 + 7 = 18, once |
> | seasons that behave differently before G4 lands | **0** | **4** (items 1, 2, 3a, 3b) |
> | each artifact after G4 | — | **re-runnable**: every falsifier below is a test or a census, not a hand-verified claim |
>
> **The seven extra rewrites are the price, stated.** What it buys is that §0.2's `done` becomes
> reachable before positions 3–7 — which have been the gate in front of everything for six days and
> are themselves unbuilt. A suite that waits produces documents. **This is RR-C's request and it is
> Jordan's to refuse**; if refused, items 1, 5, 6, 9, 11 and 12 move behind position 7 and items 2,
> 3a, 3b, 4, 7, 8, 10, 13, 14, 16 are unaffected (they add no body and write no other's Tenure).

### A.0.3 · The dependency rule

An item precedes another only where the second **cannot be observed** without the first. That is
weaker than "would be convenient", and it is why most of §A.4's sixteen rows are unordered among
themselves. Where the plan's order and the observability order disagree, observability wins and the
row says so. Two places it does:

- **Item 2's CALENDAR half cannot be observed on any world that runs today** (§A.4 item 2, MEASURED:
  `w.dates` is empty after a populated season). It splits.
- **Item 9's `inferred` count cannot be observed as "rising from 0" without running the 0 first**
  (§0.1 pt 3, first shape). It is run in §A.2 and the figure is 0.

### A.0.4 · The hash rule

Two changes below move the corpus content hash and **they must land in separate commits or neither
delta is attributable**:

1. **Item 2** — CALENDAR emitting `date.fired` puts a new Event in every log that fires a date, and
   the Q1/Q3 folds change what `questions_for` returns, which changes every Candidate downstream.
2. **Position 7's `NoOpReceipt`** — *"the one Arc-2 clause licensed to move the hash"*
   (`workplans/2026-09-11-reconciled-program_part2.md`, position 7).

**Item 2 declares its golden re-record in its own commit message**, per `CLAUDE.md` §7: *"nothing
verifies a golden re-pin was intended — so say plainly when you re-record one."*

---

## A.1 · THE DELETION LEDGER — the single owner of the count

**Every row was opened.** Column `reads it today` is the result of
`grep -rn "<name>" engine/season --include=*.py`, partitioned into non-test production code,
`engine/season/tests/`, `tests/valoria/` and the harness, run 2026-09-17 at `46aa21d`. Where the
answer is "nothing", that is a measurement and not an impression.

### A.1.1 · REMOVED — **39 objects**

#### (a) Verb-table rows — 5

`engine/season/verb_table.yaml`. **MEASURED: 38 rows** (`grep -c '^  - verb:'`), and **18 are
resolvable** (`resolvable_verbs()`, run 2026-09-17).

| # | object | path | what reads it today |
|---|---|---|---|
| 1 | `levy` | `verb_table.yaml:348` | **NOT resolvable** (measured). Writes `Rung.stores` by an `eligibility_substitution` its own cell declares: *"The source cell named `remit:levy`, and `levy` IS NOT IN `remit_acts` … Either `levy` joins the roster (a ruling: it is a SEVENTH remit act) or `issue` is genuinely the remit a levy exercises"*. A state write at a place with no contest — `holonic §37.3` row 2 by name |
| 2 | `comply` | `verb_table.yaml:130` | **NOT resolvable.** `requires_typed: none` with a prose `requires` and no `REQUIRES_PREDICATES` entry → R2 excludes it. Its own cell: *"Stays on REQUIRES_PREDICATES, where it has no predicate, so the fold refuses and names what is missing"* |
| 3 | `evade / defy` | `verb_table.yaml:220` | **NOT resolvable.** `requires: "as comply"`, and it *"inherits `comply`'s reason unchanged"* |
| 4 | `refract` | `verb_table.yaml:406` | **NOT resolvable**, `grade: absent`. `H-36` (`hole_register.yaml:394`) is **RULED**: *"RECEIVER-SIDE. ⚠ AN EMISSION IS NEVER DISTORTED (Jordan, 2026-09-02): what refracts is the PREMISES AND RATIONALE, minted per receiver as a Claim"* |
| 5 | `dispatch` | `verb_table.yaml:197` | **RESOLVABLE — the only one of the five that is** (measured). `writes: []`, so no body is needed; `_req_dispatch` (`predicates.py:291-295`) admits on *the named person exists* |

> ### RULED: **RR-A COSTS EXACTLY ONE LIVE VERB AND FOUR DEAD ROWS, AND THAT NUMBER IS MEASURED RATHER THAN ARGUED.**
> `resolvable_verbs()` returns 18 and `dispatch` is in it; `levy`, `comply`, `evade / defy` and
> `refract` are not. So the deletion takes the row count **38 → 33** and the resolvable count
> **18 → 17**, before `give` and `found` put it back to **35 / 19**. Anyone arguing RR-A on the
> ground that it deletes live behaviour is arguing about one row whose effect is `writes: []`.

#### (b) Question sources — 2

`engine/season/rosters.yaml:250-270`, `values:` at `:270`, four members. **`Question.__post_init__`
(`carriers.py:254-256`) refuses a source outside the roster**, so the roster edit and the
`questions_for` edit must land together.

| # | object | path | what reads it today |
|---|---|---|---|
| 6 | `date_due` | roster `:270`; producer `world_q.py:473-480` | **MEASURED: 0 questions in the populated world after one season.** It reads `w.dates` and `d.get("holder")`; `w.dates` is **empty** (measured: `dates: 0` after one season) because `convene` never forms, and **nothing in production ever writes a date's `holder`** (`grep '"holder"'` → `calendar.py:33` and `world_q.py:477` READ it; `corpus_run.py:324` plants `None`). Its `occasioned_by` route falls through to a generic id search that matches nothing |
| 7 | `band_crossed` | roster `:270`; producer `world_q.py:496-518` | **MEASURED: 0 questions, and 0 crossings after one populated season.** `H-110` (`hole_register.yaml:1533`): *"the question's `about` is a verb name, not an id, and nothing can walk from a band-crossed question to the Event that crossed the band"* |

**The measurement, reproducible:**
```
python3 -c "from engine.season.harness.populated import build_realm, run
from engine.season.queries import world_q; import collections
w=build_realm(0); run(seasons=1, seed=0, w=w)
print(collections.Counter(q.source for p in w.persons.values() for q in world_q.questions_for(w,p)))"
#  -> Counter({'claim_landed': 561, 'need': 81})
```

> ### RULED: **THE TWO DELETED SOURCES PRODUCE ZERO QUESTIONS TODAY, SO THEIR DELETION HAS A CONTROL THAT IS AN IDENTITY.**
> 561 `claim_landed` + 81 `need` before, 561 + 81 after, on the same seed — **that is item 2's
> control and it is exact**, not statistical. Any movement in those two numbers after item 2 is
> REACH's, not the deletion's, and the two effects are therefore separable. The plan asserted the
> deletion was safe; this measures it.

#### (c) `World` collections — 3

| # | object | path | what reads it today |
|---|---|---|---|
| 8 | `World.crossings` | `state/world.py:176` | **LIVE.** Written at `matter.py:272`; read at `world_q.py:514` (Q3) and at `harness/probes.py:680`, `:2562`. The Event emitted at `matter.py:266-270` carries the same fact — **two carriers of one fact**, which is `AX-4` |
| 9 | `World.dispensations` | `state/world.py:165` | **Production: nothing.** Read by `harness/invariants.py:72` (the entity set) and planted by `probes.py:1153`, `:1446` |
| 10 | `World.petitions` | `state/world.py:164` | **Production: nothing.** Same two readers |

⚠ **`harness/invariants.py:72` IS A REAL CONSUMER AND THE PLAN DOES NOT NAME IT.** The entity set a
dangling-Tenure sweep is computed from enumerates every `World` collection, and
`test_the_entity_set_covers_every_world_collection_a_tenure_can_name` **pins it there** — its own
docstring: *"the entity set is enumerated from `World`'s own `__init__` … rather than from what came
to mind, and [that test] pins it there so a collection added later cannot silently start reading as
dangling."* So item 5 edits `invariants.py:72` **in the same commit**, and the pinning test is the
falsifier that it did.

#### (d) `write_matrix.yaml` rows — 6

**MEASURED: 40 rows** (`grep -c '^  - kind:'`). After this ledger: **34**, with no row added.

| # | object | path | what reads it today |
|---|---|---|---|
| 11 | `(Dispensation, exists)` | `write_matrix.yaml:112` | `issue`'s `writes:` (`verb_table.yaml:262`). **EXECUTED, §A.2 PLANT 2: deleting the row while `issue` still writes it is refused at load** |
| 12 | `(Petition, exists)` | `write_matrix.yaml:224` | `petition`'s `writes:` (`verb_table.yaml:400`). Same refusal |
| 13 | `(Tenure, payload)` | `write_matrix.yaml:336`, `field:` `:337` | **No producing verb** — one of the 11 the file's own header lists at `:46-49`. `ARCH §B.8` prescribes its replacement |
| 14 | `(Person, beliefs)` | `write_matrix.yaml:154`, `field:` `:155` | **No producing verb.** The header says so at `:52`: *"`Person.beliefs` is DELETED (§D.1.1 — a belief is a `commit` to an OUGHT, not a field)"* |
| 15 | `(Rung, dates)` | `write_matrix.yaml:280` | **No producing verb.** Header `:48` |
| 16 | `(Office, establishment)` | `write_matrix.yaml:133` | ⚠ **ADDED BY THIS FILE — the plan omits it.** `establish`'s `writes:` (`verb_table.yaml:215`) names it, and the row's own `by:` cell is a warning against exactly this: *"RETIRED BY W2 for having no producing verb, RETURNED BY W3 WITH `establish`, which is the discipline the retirement rule encodes: a row exists because a producer produces it"* |

> ### RULED: **DELETING `Office.establishment` IS THREE EDITS, NOT ONE, AND THE PLAN COUNTED ONE.**
> ~~`Office.{establishment}`: a field with one reader~~ → **a field with one reader
> (`world_q.py:413`), a live matrix row (`:133`), and an entry in a live verb row's `writes:`
> (`verb_table.yaml:215`).** `establish` survives with `writes: ["Office.exists", "Office.remit"]`
> — it is **not resolvable today** (measured) because it has no `@effect_for` body, so shrinking
> its `writes:` costs nothing that runs. But the L11 refusal fires if the row goes and the
> `writes:` entry stays, so all three land together. **REMOVED gains one row; the plan's 37 becomes
> 38 on this ground alone.**

#### (e) Dataclass fields — 13

`engine/season/state/carriers.py`. Reader counts exclude the declaration itself and are partitioned.

| # | object | path | what reads it today |
|---|---|---|---|
| 17 | `Tenure.payload` | `carriers.py:59` | **NOTHING.** ⚠ `grep '\.payload'` returns 27 production hits and **every one is `Act.payload`** (`carriers.py:339`); no `Tenure(...)` construction anywhere passes `payload=`. 12 hits in `engine/season/tests`, 0 in `tests/valoria` |
| 18 | `Person.beliefs` | `carriers.py:381` | **NOTHING** in production; 0 in `engine/season/tests`; 1 in `tests/valoria` |
| 19 | `Office.establishment` | `carriers.py:491` | `world_q.py:413` (inside `establishment_of`, **which has no callers** — §A.1.5 (d)) + `probes.py:1376` (`assert off.establishment == []`). **MEASURED: 0 of 19 offices carry a non-empty value** |
| 20 | `Office.upkeep` | `carriers.py:493` | **NOTHING**, anywhere — 0 production, 0 tests, 0 harness |
| 21 | `Office.dates` | `carriers.py:492` | **NOTHING** |
| 22 | `Office.scope_rung` | `carriers.py:487` | **NOTHING in production.** Written inside `Office.__post_init__` (`carriers.py:546-548`) from `title_domain`; 2 hits in `engine/season/tests` |
| 23 | `Rung.sites` | `_DECLARED`, `carriers.py:568` | **NOTHING.** The one mention is `matter.py:198`'s comment: *"`r.sites` … is a BACK-REFERENCE NOTHING MAINTAINS — it is empty for every rung in the corpus"* |
| 24 | `Rung.records` | `_DECLARED`, `carriers.py:568` | **NOTHING** |
| 25 | `Rung.dates` | `_DECLARED`, `carriers.py:568` | **NOTHING** |
| 26 | `Rung.stake` | `_DECLARED`, `carriers.py:568` | **NOTHING.** Its matrix row is already in `write_matrix.yaml`'s `retired:` list (`:368-372`). `ARCH F.18`: *"'out of the office's stake', and `stake` was retired"* |
| 27 | `Rung.transmission` | `_DECLARED`, `carriers.py:568` | **NOTHING**, anywhere |
| 28 | `Rung.judging_set_rule` | `_DECLARED`, `carriers.py:568` | `world_q.py:147` only — inside `judging_set`'s `Unspecified` raise. `ARCH §B.7` call 3 deletes it by name |
| 29 | `Site.drawers` | `carriers.py:418` | **NOTHING.** Its matrix row is in the `retired:` list (`:372`) |

⚠ **TWO `Office` FIELDS THE PLAN DELETES ARE NOT ON THIS LIST.**
**`Office.binds`** — a dead field by measurement and a **retained** one by ratified prescription
(§A.1.5 (b)); the retention costs the ledger two objects.
**`Office.body_function`** — **`03_SEATS_AND_CONTENT.md` keeps it as a derived cache** and `03` owns
the seat model, so the count books its ruling. ⚠ **Recorded with its cost and not endorsed by this
file:** `body_function` has **zero readers anywhere** (measured), is written only inside
`__post_init__` from `BODY_FUNCTION[self.body]`, and its own comment in `carriers.py:494-500` is a
warning against exactly this — *"these fields exist because the first version validated them and
threw them away … an artifact nothing reads"*, which is the criterion `governance_modes` was deleted
on. **A cache nothing reads is `AX` ID-13.** If `03`'s cache acquires no reader, the honest move is
to delete it later and take the ledger to −18; the count does not pre-empt `03` on `03`'s own
subject.

#### (f) Helpers, Queries and named terms — 9

| # | object | path | what reads it today |
|---|---|---|---|
| 30 | `title_domain` | `data/rosters.py:459` | ⚠ **FIVE call sites in THREE files, not one:** `predicates.py:152` (inside `under_purview`), `predicates.py:252` (`target_is_title`), **`carriers.py:536`** (`Office.__post_init__`'s title-in-a-body refusal), **`carriers.py:546`** (`scope_rung` derivation), `populated.py:671` (world-gen's seat/occupation discriminator). Imported at `predicates.py:27`, `carriers.py:34`, `populated.py:75` |
| 31 | `title_rank` | `data/rosters.py:465` | `predicates.py:163` (inside `highest_title_rank`), `predicates.py:270` |
| 32 | `titles_held` | `predicates.py:144` | `predicates.py:132` (`under_purview`), `:163` |
| 33 | `highest_title_rank` | `predicates.py:157` | `predicates.py:270` |
| 34 | `judging_set` | `world_q.py:146` | ⚠ **`probes.py:1208` and `probes.py:2467` — TWO harness callers, not "itself".** Raises `Unspecified("judging_set_rule", "S61")` |
| 35 | `conferral_path` | `world_q.py:416-437` | ⚠ **ADDED BY THIS FILE — the plan does not name it. NOTHING calls it.** `grep conferral_path` returns its own `def` and its own `TRACE.query` line and nothing else. **It never reads `conferral` either** — the name is a promise the body does not keep: it walks `off.rung → parent_of → root`, which is exactly the walk `descendants` inverts, and its own docstring concedes it is a limit: *"IT RETURNS RUNGS, NOT OFFICES, AND THAT IS A LIMIT RATHER THAN A CHOICE"* |
| 36 | `_req_dispatch` | `predicates.py:291-295` | `REQUIRES_PREDICATES["dispatch"]`. Goes with row 5 |
| 37 | `_event_place` | `epistemic.py:215-242` | ⚠ **ADDED BY THIS FILE AND BY `01`, against the plan.** One caller (`:253`). It is **superseded, not moved**: `place_of` has a different signature (an id, not an `Event`) and **two limbs `_event_place` does not have** — a Record resolving through its live holder, and a Date resolving to its `venue`. **MEASURED: `_event_place` returns `None` for a Record-subject Event today**, because its last loop looks for a `contain` Tenure whose subject is the record id and no such edge exists |
| 38 | `budget_office_bonus` | fixture cell `data/fixtures.py:430`; term `decision/budget.py:56-57` | **LIVE.** `offices = sum(1 for t in p.tenures if t.kind == "hold" and t.live)` then `b = k + offices * fx.get("budget_office_bonus")`. ⚠ **`offices` counts EVERY live `hold`, including one on a Rung** — which is `H-92` (`hole_register.yaml:1108`) in its own words: *"A LANDHOLDING BUYS SCENE ACTIONS"*. One NAME, one object; the fixture cell is content and rides with the term (§A.0.1 pt 3) |

> ### RULED: **`title_domain` IS FIVE CALL SITES AND TWO OF THEM ARE A LIVE GAME REFUSAL. DELETING IT WITHOUT RE-EXPRESSING THAT REFUSAL WOULD RE-OPEN A CLOSED QUESTION.**
> `carriers.py:536-544` refuses an Office that names a TITLE **and** a faction body: *"A TITLE IS
> NOT AN OFFICE, AND CONFLATING THEM PUT A KING IN THE CHURCH. The overlay `{post: "King", body:
> "Cardinal of Justice"}` was ACCEPTED before this check and produced a realm title whose Church
> affiliation existed nowhere in canon."* Round one's closed-question 9 (prince-bishop
> exclusivity) is closed **on that line**.
>
> **The re-expression, and it needs no new object:** under `03`'s model a title is exactly a seat
> whose `revocation == "holdings"`. So the refusal becomes *a seat with `revocation == "holdings"`
> may not carry a `body`* — same guard, same file, reading a rostered value instead of a lookup.
> **Stated here because the plan's "the four helpers are deleted" would have lost it silently.**

#### (g) Roster members — 1

| # | object | path | what reads it today |
|---|---|---|---|
| 39 | `remit_acts.dispatch` | `rosters.yaml:119` (block `:111-119`) | `Office.__post_init__`'s remit validation (`carriers.py:527-533`) and every `remit:dispatch` eligibility. **MEASURED: 16 of 19 offices carry `remit_acts: []`**, so nothing in the populated world exercises it |

**REMOVED = 5 + 2 + 3 + 6 + 13 + 9 + 1 = 39.**

### A.1.2 · ADDED — **22 objects**

| kind | # | names | n |
|---|---|---|---|
| Queries | 1–2 | `reach(w, p)`, `nearest_store(w, rung, kind)` — **both absent today** (`grep 'def reach\|def nearest_store\|def place_of'` over `engine/season` → nothing) | 2 |
| verb rows | 3–4 | `give` (the `H-84` verb; ratified position 16 chose the shape), `found` (the `ARCH F.20` verb) | 2 |
| effect bodies | 5–11 | `commit`, `oblige`, `issue`, `petition`, `give`, `restore`, `found`. **All seven verified absent:** the 11 `@effect_for` decorators are `confer` `:92`, `release` `:129`, `revoke` `:159`, `convene` `:173`, `move` `:193`, `work` `:244`, `create_record` `:262`, `destroy_record` `:293`, `kill / wound` `:308`, `utter` `:422`, `transfer` `:437`. Count goes **11 → 18** | 7 |
| predicates | 12–14 | `_req_oblige`, `_req_issue`, `_req_give`. Today `REQUIRES_PREDICATES` holds `confer` `:166`, `release` `:193`, `revoke` `:221`, `dispatch` `:290`, `convene` `:297` — **five**, going to **seven** (`dispatch` out, three in) | 3 |
| rosters | 15–18 | `record_kinds`, `conferral_bases`, `revocation_bases`, **`binds_bases`** (see §A.1.5 (b)) | 4 |
| named rule | 19 | the **document-content deposit rule** at WITNESS — one branch keyed on a hold-on-a-Record in `changes[]` (`epistemic.py:260`'s existing channel). ⚠ **It is counted because its host is NOT counted:** the branch goes inside the existing witness deposit, which survives. By the same test the **release-before-mint rule** on `give` (⊕ R14) is **NOT** counted — its host is `_eff_give`, already +1 at row 9, and counting both would double-count |
| ⚠ **moved / factored (+1 each, NOT 0)** | 20–22 | `place_of` (supersedes `_event_place`, which is counted OUT at row 38) · `World.remove_person` (factored from `_eff_kill`'s **nameless** inline cascade `:416-418`) · `_crossings` (factored from `matter.py`'s **nameless** inline site block `:255-275`) | 3 |
| **content (0)** | — | `engine/season/data/offices.yaml`; `fixtures.body_step`; `fixtures.told_drift_band`; `binds_bases`' one value; `record_kinds`' five key-lists | 0 |
| **WITHDRAWN from the plan (0)** | — | ⚠ ~~`band_floors.person`~~ — **it does not load.** §A.2 PLANT 1, EXECUTED | 0 |

**ADDED = 2 + 2 + 7 + 3 + 4 + 1 + 3 = 22.**

### A.1.3 · NET — three units, and the least favourable one is stated first

> ## **NET: −17 ENGINE OBJECTS. 39 removed against 22 added.**
>
> ⚠ **THIS IS THREE WORSE THAN THE PLAN'S HEADLINE AND IT IS THE NUMBER THIS SUITE CARRIES.** The
> plan said **−20**, and it was counting three new function names as free and two retained fields as
> deleted. §A.1.6 shows the counting schemes in circulation across the four concurrently-authored
> documents, their different answers, and why this file rules **the one that flatters least at every
> fork.**
>
> **Per-document shares, for reconciliation and NOT for addition** — they overlap, so they do not
> sum: `01_ATTENTION_AND_REACH.md` reports **−3** on its own share (5 out / 2 in);
> `03_SEATS_AND_CONTENT.md` reports **−8** (12 out / 5 in). **Only this section's 39/22 is the
> suite's figure**, and where a share and this ledger differ the difference is stated in §A.1.6.

| unit | out | in | net | is it the favourable unit? |
|---|---|---|---|---|
| **systems / families** (the coarsest) | 8 | 5 | **−3** | **no — the worst one, and still negative** |
| **names and named rules** (§A.0.1 — the headline) | 39 | 22 | **−17** | **no — the strict scheme, adopted here** |
| **concepts** (a moved function counts 0 — the plan's scheme, and this file's first draft) | 38 | 19 | **−19** | **yes, and it is not used** |
| **vocabulary** (terms a reader must hold) | 24 | 17 | **−7** | no |

**The eight families out:** the four response verbs · the title/rank family (four helpers, one
branch, one roster) · the two parallel document stores · the duplicate crossing carrier · the
`establishment`-as-a-field membership model · the office-bonus budget term · the two uncalled
purview-adjacent Queries (`judging_set`, `conferral_path`) · the dead-field residue as one sweep.
**The five in:** the Record-kind family (`record_kinds` + the deposit rule + `give`) · the reach/place
walk (`reach` + `place_of`) · the store walk (`nearest_store`) · the seat-basis family (three rosters,
three predicates) · the works/found family.

> ### RULED: **THE PLAN'S TWO ROW-LEVEL SLIPS CANCELLED, AND ITS HEADLINE SURVIVED BY COINCIDENCE. RE-DERIVED STRICTLY, IT DOES NOT.**
> The plan's REMOVED table lists 5 + 2 + 3 + 5 + 15 + **6** + 1 and states 37; its helpers row names
> **seven** names and counts them as six, so the table's own contents sum to **38**. Its ADDED table
> lists 2 + 2 + 7 + 3 + 3 + 1, which sums to **18**, and states **17**. ~~37 − 17 = 20~~ →
> **38 − 18 = 20.** *Both sub-counts were one low, in compensating directions.* The stated net was
> right and neither stated sub-count was — which is `CLAUDE.md` §0.1 pt 4 in miniature: a figure can
> be correct and its support wrong, and **the support is the one to check.**
>
> A third slip is in the plan's own caveat: *"roughly −8 systems (four verbs, three World
> collections, one title family gone; one Record family, one walk family in)"* is **8 out and 2 in,
> i.e. −6**, not −8 — and on the family scheme actually applied here it is **−3**.
>
> **And a fourth, which is the plan's real error rather than an arithmetic slip:** counting three new
> function names as free because a predecessor was being promoted. §A.1.6.

**The six variants within the strict scheme, so nobody thinks the number was tuned:**

| if… | out | in | net |
|---|---|---|---|
| `Office.binds` is DELETED and `binds_bases` never exists (the plan's shape) | 40 | 21 | **−19** |
| `Office.body_function` is DELETED rather than kept as `03`'s derived cache | 40 | 22 | **−18** |
| **BOTH retained, which is what `01`–`04` actually propose (RULED here)** | 39 | 22 | **−17** |
| the `titles` roster is also deleted, its domains moving into `offices.yaml` (residue, §A.1.5 (c)) | 40 | 22 | **−18** |
| item 9 does not land, so `establishment_of` is deleted rather than rewritten (§A.1.5 (d)) | 40 | 22 | **−18** |
| **RR-A is REFUSED, so item 13 never lands and the four response rows stay** | 35 | 22 | **−13** |

> ### RULED: **THIS FILE TAKES THE LEAST FAVOURABLE OF EVERY FORK IT MEETS.**
> −19 is available on the plan's own `binds` shape and is not taken, because `ARCH §B.7`'s ratified
> `Seat :=` line spells `remit(acts[], binds)` and `ARCH F.17` names `binds` as `oblige`'s own
> operand. **A suite whose headline is a deletion count has exactly one bias, and it is toward
> deleting**; the check on it is to publish the arithmetic for the option not taken, and to adopt the
> counting scheme that costs the most. Both are done — **six times, and every one of the first five
> alternatives above is better for the headline than the number printed.**

### A.1.4 · Vocabulary — 24 out, 17 in

**Rule:** a name in the engine's vocabulary that a reader must hold today and would not after.

**OUT (24).** Verbs: `levy`, `comply`, `evade`, `defy`, `refract`, `dispatch` (6). Question sources:
`date_due`, `band_crossed` (2). Carriers and stores: `Dispensation` as a type, `Petition` as a type,
`crossings` (3). The whole title family as one concept: `title` (1). Queries: `judging_set`,
`conferral_path`, `_event_place` (3). Retired field names, as TERMS — so `establishment` is excluded (it survives as a Query name),
`dates`/`records`/`sites` are excluded (they survive as `World` collections), and `body_function` is
excluded because `03` keeps it: `payload` (on a Tenure), `beliefs`, `upkeep`, `scope_rung`, `stake`,
`transmission`, `judging_set_rule`, `drawers` (8). Fixture: `budget_office_bonus` (1).

**IN (17).** Queries: `reach`, `nearest_store`, `place_of` (3). Verbs: `give`, `found` (2). Rosters:
`record_kinds`, `conferral_bases`, `revocation_bases`, `binds_bases` (4). New Record kinds:
`commission`, `works`, `text` (3 — `dispensation` and `petition` already exist as type names and are
re-used, not coined). Claim-predicate namespace: `content:` (1). Fixtures: `body_step`,
`told_drift_band` (2). `World.remove_person`, `_crossings` (2).

**Shorter by 7.** ⚠ The plan's *"removed 11, added 5, shorter by 6"* counted only verb-and-source
names and included `in_force`, which **was never in the engine** — it was round one's proposal. A
withdrawn proposal is not a deletion, and counting it as one is the exact move `AUDIT_VERDICT.md`
faulted round one for: *"'Net deletion' holds only against a counterfactual that never existed in
code."*

**Round one's eight proposed-and-withdrawn Queries** — `in_force`, `ceiling`, `capacity`,
`character`, `delivered`, `demanded`, `serves`, `occupiable` — are on **a separate line and count
zero.** None was built. They change this proposal's count against round one's; they do not change
the engine's.

### A.1.5 · What the plan miscounted — five verdicts

> ### RULED (a): **`band_floors.person` DOES NOT LOAD, AND THE TABLE IT WOULD DUPLICATE ALREADY RUNS.**
> ~~`persons use a NEW `band_floors.person` cell set ({able: 500, failing: 100})`~~ → **`band_floors`
> already carries the person's body bands, under the key `body`, and `decision/budget.py` already
> reads them.**
>
> `rosters.yaml:805-816`'s own note, verbatim: *"⚠⚠ `body` IS NOT A SITE. It is `(Person, body)`'s
> band row, here because `band_floors` keys on THIS roster and `H-38` ruled '`Site.condition` is the
> model' — no second scheme."* And `budget.py:63-75`:
> `body_band_penalty(p, fx)` → `floors = fx.get("band_floors")["body"]`, whose docstring says
> *"A second band scheme would have been the invention `H-38` was closed to avoid."*
>
> **EXECUTED 2026-09-17 (§A.2 PLANT 1):** adding a `person` key to `band_floors` raises
> `Forbidden: band_floors names site kind(s) no roster carries: ['person']`
> (`data/fixtures.py:111-117`, which validates the outer key **in both directions**).
>
> **EXECUTED 2026-09-17:** the ladder already runs end to end.
> ```
> band_floors['body'] = {'full_operations': 800, 'limited': 500, 'withdrawal_only': 100}
>   body=1000  bands_lost=0  budget(k=5)=5      body=499  bands_lost=2  budget(k=5)=3
>   body= 799  bands_lost=1  budget(k=5)=4      body= 99  bands_lost=3  budget(k=5)=2
> ```
> **Three consequences, all favourable and none of them the plan's:** the ADDED side loses a content
> item; **S gains** (one table, one helper, no second ladder — which is the S-defect the plan would
> have introduced); and **item 3b's N-line gets much stronger**, because `Person.body` already has a
> live consumer that narrows a person's season. `04` is the owner of the design statement; this is
> the ledger consequence.

> ### RULED (b): **`Office.binds` IS RETAINED AND WIRED, NOT DELETED.**
> ~~`Office.{establishment, upkeep, dates, scope_rung, body_function, binds}` (0 readers each)~~ →
> five fields deleted, `binds` retained. `binds` is a dead field **by measurement** (0 readers
> anywhere) and a **prescribed** one by two ratified surfaces: `ARCH §B.7`'s `Seat :=` spells
> `remit(acts[], binds)`, and `ARCH F.17` gives the resolution for *how a person joins an
> establishment* as **`oblige`'s `requires` reads the seat's `binds`** — with the alternative
> explicitly costed: *"if admission is a seat's own act, the closed remit roster needs a sixth
> member — a ruling, not a row."*
>
> So `_req_oblige` reads `binds`, `binds` joins a closed roster `binds_bases` with its one live
> value `members_by_admission`, and **a dead field becomes a live one instead of a deleted one.**
> Cost: **+2 to the net** (−19 → −17), published in §A.1.3. Benefit: two RR-B limbs do not open, and
> `ARCH F.17` closes **as F.17 itself states it** rather than by a substitute rule.
>
> ⚠ **The counter-argument, recorded because it is good:** a roster with one value and one reader is
> the `governance_modes` shape (*"They were not wrong; they were UNREAD"*, `rosters.yaml`) with extra
> steps. **It is answered by the reader, not by the roster** — `binds_bases` has a consumer on the
> day it lands, which `governance_modes` never did. If Jordan prefers the deletion, take −19 and add
> two RR-B limbs.

> ### RULED (c): **TWO OBJECTS THE PLAN DOES NOT NAME ARE DELETED HERE, AND ONE IS RESIDUE.**
> **`(Office, establishment)`**, the matrix row (§A.1.1 row 16) — forced, counted.
> **`conferral_path`** (`world_q.py:416-437`) — a Query with **zero callers**, superseded by
> `descendants(w, seat.rung)`, which `03`'s purview rule uses. Counted.
> **`titles`, the roster** (`rosters.yaml:692`) — RESIDUE. Its only code reader is `title_domain`
> (via `TITLE_DOMAINS`), so deleting the helpers orphans it, and an orphaned roster is `S11`: loads
> clean, `roster()` raises at READ, not at load. **Ruling: its domains move into `offices.yaml` as
> each seat's `rung` and the roster goes** — which is where Jordan's 2026-09-02 content belongs once
> every seat has a rung. Counted on the supplementary line only (−18), because a reader may fairly
> call a content roster content.

> ### RULED (d): **`establishment_of` IS REWRITTEN ONLY IF ITS CONSUMER LANDS IN THE SAME COMMIT.**
> **MEASURED: `establishment_of` (`world_q.py:399-413`) has zero callers** — `grep` returns its own
> `def` and its own `TRACE.query` line. Rewriting it over `oblige` tenures would produce a Query
> with no consumer, which round one's own §B.4 forbids by name: *"a Query with no consumer is a
> false N-line."*
>
> **It has a consumer under this design and exactly one:** item 9's `_ch_post_remit`, which needs
> *the obligees of a seat* and must not re-derive them (§8 — the rule lives once). So
> `establishment_of` becomes the single owner of the obligee set **and `_ch_post_remit` calls it, in
> the same commit.** If item 9 does not land, `establishment_of` is deleted, REMOVED becomes 40 and
> the net becomes −18. Counted as a rewrite (0) on the assumption that item 9 lands.

> ### RULED (e): **`judging_set` HAS TWO HARNESS CALLERS, NOT "ITSELF".**
> ~~its one caller is itself~~ → `probes.py:1208` and `probes.py:2467` both call
> `world_q.judging_set(w, "D")` and both expect the `Unspecified` raise. Deleting the Query breaks
> two probes, which must be re-pointed or dropped in the same commit. `ARCH §B.7` call 3 gives the
> replacement: *"The judging set is the seats whose remit covers the matter at that venue — a Query
> over seats … not a rule stored on a place"* — **and this design does not build that Query.** So
> `judging_set` is deleted and `ARCH §B.7` call 3's replacement is **not** supplied; the sitting
> stays ratified position 18's (PROC-A, which names `judging_set` in its own instruction). Said here
> rather than implied.

---
### A.1.6 · RECONCILIATION — three counting schemes, two sibling findings, and what each costs

Four documents were authored **concurrently** from one plan. Three of them count objects, and they
did not agree. **This section is the reconciliation and this file is the suite's single owner of the
count** (§A.0.1), so the number below is the suite's number and `01`–`04` point here.

#### (a) THE THREE SCHEMES, AND THE RULING

| scheme | `place_of` | `remove_person`, `_crossings` | `_event_place` | `occasioned_by`'s id search | net |
|---|---|---|---|---|---|
| **the PLAN's** (concept) | +0 "moved" | +0 "moved" | not counted | not counted | ~~−20~~ |
| **`01`'s** (name, partial) | **+1** | not its subject | **−1** | **−1** | −3 on its own share |
| ✅ **THIS FILE's** (name + named rule, symmetric) | **+1** | **+1 each** | **−1** | **+0** — a nameless path inside a surviving function | **−17** |

> ### RULED: **`01` IS RIGHT THAT `place_of` IS NOT FREE, AND RIGHT AGAINST ITS OWN INTEREST, SO ITS ARGUMENT WINS AND IS THEN APPLIED SYMMETRICALLY — WHICH COSTS TWO MORE THAN `01`'s OWN FIGURE.**
> **`01`'s argument, verified here:** `place_of` is *"a new signature with two added limbs and two
> added callers"*. **OPENED, `epistemic.py:215-242`:** `_event_place` takes an **`Event`** and
> branches on `e.subject` over persons, sites and rungs, with a trailing `contain` lookup.
> `place_of` takes **an id of any kind** and adds **a Record limb** (resolve through the live holder,
> else `Record.rung`) and **a Date limb** (`venue`). ⚠ **And the Record limb is not cosmetic:
> `_event_place` returns `None` for a Record-subject Event today** — its trailing loop looks for a
> `contain` Tenure whose subject is the record id, and no such edge exists. So `place_of` is a
> **supersession**, and a supersession is one name out and one name in, not a move.
>
> **Applied symmetrically, the same argument catches two more.** `World.remove_person` and
> `_crossings` are new names too. Their predecessors — `_eff_kill`'s inline cascade and `matter.py`'s
> inline site block — are **nameless**, so nothing comes out against them. **Net effect of adopting
> `01`'s reasoning in full: ADDED +3, REMOVED +1, i.e. the headline gets TWO WORSE, not one better —
> and `03`'s retained `body_function` makes it a third.** `01` stopped at the row it owned; this file owns the count, so it pays the rest.
>
> **The one place this file declines `01`'s reading:** `occasioned_by`'s generic id search is deleted
> **code** inside a function that survives, exactly as the `is_title` branch is deleted code inside a
> surviving `_req_revoke`. Counting one and not the other would be incoherent, and counting both
> would let a suite inflate its deletions by naming branches. **Divergence stated, not averaged:
> `01` has 5 out / 2 in on its share; this file has 4 out / 3 in on the same objects.** Either way
> `01`'s own share is negative, and either way the suite's total is negative.

#### (b) ⚠ A `body`-KIND **SITE** IS ACTUALLY CONSTRUCTED, AND THE ROSTER'S NOTE SAYS IT IS NOT A SITE

**OPENED, `engine/season/harness/headless.py:64-65`, verbatim:**
```python
w.sites["scriptorium"] = Site("scriptorium", "hearth_ostvik", "body",
                                condition=w.fixtures.get("condition_scale"))
```
A Site of kind **`body`**, seated at a **hearth** rung, named **a scriptorium**. Against
`rosters.yaml:814-816`'s note: *"⚠⚠ `body` IS NOT A SITE. It is `(Person, body)`'s band row, here
because `band_floors` keys on THIS roster."*

> ### RULED: **BOTH READINGS ARE TRUE AT ONCE, THE CODE IS THE MECHANISM, AND NOTHING IN THIS SUITE BREAKS — BUT THE AMBIGUITY MUST BE NAMED BECAUSE THE SHARED `_crossings` HELPER WALKS STRAIGHT INTO IT.**
> Under `CLAUDE.md` §0.05 the code decides: **`body` is a constructible `site_kinds` member today**,
> and a `body` Site wears at 10/season (`wear_per_season.body: 10`) and crosses
> `{full_operations: 800, limited: 500, withdrawal_only: 100}` **as a site**. The roster note records
> the **intent** — the row exists so `band_floors` can key a PERSON's body — and `headless.py` looks
> like a fixture that reached for a registered kind because it needed one, not like a design decision
> that a scriptorium is a body.
>
> **What this suite does about it: nothing to `site_kinds`, and one explicit statement in
> `_crossings`.** The helper is keyed on **the floor table's key**, not on "is this a person or a
> site" — `_crossings(w, id, kind_floors, before, after, cause)` — so a `body` Site passes
> `band_floors["body"]` because that is its `site.kind`, and a Person passes `band_floors["body"]`
> because that is where `budget` already reads the person's bands (`budget.py:73`). **The two
> callers converge on one table by two routes, which is `H-38`'s "no second scheme" holding, and it
> is also a genuine referent ambiguity in one line of a harness.**
>
> ⚠ **THE MIGRATION LINE, so this is not a silent contradiction.** If a later session decides `body`
> must **not** be a site kind, the edit is: `headless.py:64`'s Site becomes a kind that is one —
> `seam` is the closer fit for a scriptorium's wear profile, and its condition is already seeded from
> `condition_scale` so no arm of the sweep moves — **and then L29 forces `body` out of
> `wear_per_season` too, while `band_floors.body` must STAY** because `budget` reads it and L28 would
> then refuse it for naming a kind `site_kinds` no longer carries. **That is a three-edit,
> load-refusing knot and it is NOT this suite's to untie.** It is stated, not filed (§B.4).
>
> **And the correction this forces on this file's own earlier framing:** *"the baseline is two site
> kinds"* would be wrong. **It is three — `harbour`, `seam`, `body` — and the third is constructed.**

#### (c) ⚠ `descendants` EXCLUDES THE RUNG IT IS CALLED ON. A DUKE LOSES HIS OWN DUCHY.

**OPENED, `engine/season/queries/world_q.py:54-64`:** `out, seen, stack = [], {rung_id}, [rung_id]`,
and the walk appends only `t.subject` for a `contain` edge whose object is already seen. **`rung_id`
is seeded into `seen` and never into `out`.** So `descendants(w, d)` is the **strict** subtree.

> ### RULED: **EVERY REACH LIMB IS `{rung} ∪ descendants(w, rung)`; PURVIEW IS THAT SET *MINUS THE SEAT EXERCISED*. `descendants(w, rung)` ALONE IS A REGRESSION, NOT A NEW GAP.**
> `under_purview` **today** does not have this defect: it walks **UP** from the holding
> (`predicates.py:130-143`, `seen, cur = set(), holding`, ascending by `parent_of` until it meets a
> seat's rung), so `under_purview(actor, seat.rung)` is **true** — a Duke can act on his own duchy.
> `03_SEATS_AND_CONTENT.md` measures that reflexivity directly (**365 admitted against 364**), so it
> is not inferred. Rewriting it as `office.rung in descendants(w, seat.rung)` would make it
> **false**, and 3 of 19 seats are on the ladder today, so the loss would be immediate.
>
> **The correction, for both sibling documents and for this file's §A.3.5 — and the two sets are NOT
> the same set:**
> - **REACH** (`01`): `⋃ ({seat.rung} ∪ descendants(w, seat.rung))` over live holds on an Office.
>   **Inclusive**, because a duke must be asked about his own duchy.
> - **PURVIEW** (`03`): `({seat.rung} ∪ descendants(w, seat.rung)) \ {the seat exercised}`.
>   **Inclusive of the rung, exclusive of the seat**, because a seat may not revoke itself — the
>   equal-rank case `_req_revoke`'s rank conjunct excludes today (`predicates.py:270-274`: *"which
>   also forbids revoking YOUR OWN title, an equal-rank case nothing else in the branch excluded"*).
>
> **`01` owns REACH's statement and `03` owns purview's; this is the ledger's note that the walk is
> inclusive of its argument and that the two consumers subtract different things.** Zero objects
> either way — two set expressions, not a Query.
>
> **`nearest_store` is UNAFFECTED and it is worth saying so.** It walks **UP** with `parent_of`
> (`world_q.py:48-52`) and **starts at `rung` itself**, so a hearth with its own larder draws
> locally — which is item 3a's declared control arm, and it would have been silently broken by a
> `descendants`-shaped walk. **Falsifier LB-3a's paired control is the assertion that it is not.**
>
> **Falsifier for the general case: LB-2e** —
> `test_a_duke_is_reached_by_a_claim_about_his_own_duchy_rung`, and
> `test_purview_admits_an_office_seated_at_the_seats_own_rung`. Both fail on a bare `descendants`
> and pass on the union, so they can observe the failure they exclude (§0.1 pt 2).

---

## A.2 · THE PRE-FLIGHT — every way a row this suite proposes is refused, and the ways it is not

**Round one's most reusable artifact, carried forward and extended.** It is a **checklist, not a
summary**: run it by hand against the row you are about to write. Round one built its rows by
planting each defect and reading the loader's own refusal; this round re-opened every citation it
carries and **added twelve rows that only this suite's schema changes can hit** (marked ⊕), plus
**two new executed plants** (`PLANT 1`, `PLANT 2`).

> **THE ONE SENTENCE TO TAKE FROM §A.2, unchanged from round one because it is still true:**
> *the loaders are tight on the grammar and loose on the schema.* They refuse a malformed
> precondition with a paragraph of reasoning and accept a whole invented column in silence.
> **Design freely; then check §A.2.3 by hand, because it is the half that will not check itself.**

### A.2.0 · TWO PLANTS EXECUTED THIS SESSION

**PLANT 1 — `band_floors` gains a `person` outer key.** Method: monkeypatch
`engine.season.data.fixtures.table` to return `band_floors` with one extra key, call
`_load_matter_tables()`. Nothing in the tree was modified.
```
PLANT1 REFUSED: Forbidden | [FORBIDDEN] band_floors names site kind(s) no roster carries: ['person']
                @rosters.yaml  needs: add the kind to `site_kinds`, or drop the row
```
**Verdict: the plan's `band_floors.person` is refused at load.** `data/fixtures.py:106-123` validates
the outer key in **both** directions against `site_kinds`, so the cell set would also need a
`site_kinds` member **and** a `wear_per_season` rate (L29). The bands already exist under `body`
(§A.1.5 (a)). **Withdrawn.**

**PLANT 2 — `(Dispensation, exists)` deleted from the matrix while `issue` still writes it.**
Method: pop the key from `data.matrix.MATRIX`, reload `data.verbs`.
```
verb_table.yaml: 'issue' writes (Dispensation, exists), which is on no row of write_matrix.yaml.
§30: ANY UNMARKED CELL IS A WRITE-CLASS VIOLATION. Rule the Part D row first, then add the verb.
```
**Verdict: item 5's matrix deletion and verb-row re-key are ONE commit.** Same for
`(Petition, exists)`/`petition` and `(Office, establishment)`/`establish`. Three coupled pairs, and
the loader is the enforcement.

### A.2.1 · Refused AT LOAD — the whole package fails to import (44)

| # | the defect | refusal, at |
|---|---|---|
| L1 | `requires_typed.form` names a form outside the closed seven | `SystemExit` — *"names requires form 'X', which is not in rosters.yaml's requires_forms … an eighth is a new thing a precondition can ASK, which is a design change and not a table edit"* (`data/requires.py:549-554`) |
| L2 | `form:` is in the roster and has no `@requirement_form` class — today `cardinality` and `basis` | `SystemExit` — *"IN the grammar and has no implementation"* (`data/requires.py:556-560`) |
| L3 | the cell binds an operand outside `requires_operands` | `SystemExit` — *"Coining an operand is filling `H-94` by keyword argument"* (`:567-571`) |
| L4 | the operand is rostered but outside **that form's** `needs:` list | `SystemExit` (`:572-575`) |
| L5 | a predicate stem no reader dispatches on | `SystemExit` — *"would evaluate UNKNOWN in every world and refuse the verb everywhere, which is indistinguishable from an honest operand gap"* (`:531-536`) |
| L6 | an `all:` with fewer than two clauses | `SystemExit` — *"a conjunction of one is the clause itself"* (`:544-546`) |
| L7 | `scalar_threshold` with BOTH `threshold:` and `threshold_predicate:`, or NEITHER | `SystemExit` (`:213-216`) |
| L8 | a comparator outside `{">=", "<="}` | `SystemExit` — *"a strict comparator is a change to what a precondition can say"* (`:218-222`) |
| L9 | `requires_typed: none` with no `requires_typed_note:` | `SystemExit` — *"An untyped cell with no reason is indistinguishable from one nobody typed"* (`data/verbs.py:248-252`) |
| L10 | `requires_typed:` is any string other than `none` | `SystemExit` (`data/requires.py:593-598`) |
| **L11** | **a `writes:` pair on no `write_matrix.yaml` row — including a retired one** | `SystemExit` — *"§30: ANY UNMARKED CELL IS A WRITE-CLASS VIOLATION. Rule the Part D row first, then add the verb"* (`data/verbs.py:298-307`). **EXECUTED: PLANT 2.** This is the suite's single most load-bearing refusal — it couples three matrix deletions to three verb-row edits |
| L12 | `eligibility:` names `capability` — **even if `capability` is added to the roster** | `SystemExit`, **by name**, independent of the roster (`data/verbs.py:311-315`) |
| L13 | `eligibility:` names a kind outside `[own, remit, hold, presence]` | `SystemExit` — *"a fifth would be a new way to make a verb unavailable"* (`:316-320`) |
| L14 | `scale:` is not a `rung_kinds` member — so **`faction` and `world` both refuse** | `SystemExit` (`:324-326`) |
| L15 | `stratum:` is not one of the five | `SystemExit` (`:327-329`) |
| L16 | a degree-keyed `writes:` with no `contests:` | `SystemExit` — *"Nothing resolves a degree for it"* (`:271-274`) |
| L17 | a degree-keyed `emits:` with no `contests:` | `SystemExit` (`:287-290`) |
| L18 | `contests:` with a FLAT `writes:` | `SystemExit` — *"losing the contest writes exactly what winning it does"* (`:265-270`) |
| L19 | `contests:` with a FLAT `emits:` | `SystemExit` — *"a wound emitting `person.died`"* (`:292-297`) |
| L20 | `writes:` and `emits:` keyed on **different band sets** | `SystemExit` (`:256-260`) |
| L21 | a duplicate `verb:` name | `SystemExit` (`data/verbs.py:216-217`) |
| L22 | a duplicate mapping key **anywhere in any of the three YAMLs** | `ValueError` from `load_yaml`'s `_no_dup` — *"`safe_load` would silently keep the last, which is how two `writes_note` cells became one"* (`data/rosters.py:50-59`) |
| L23 | a duplicate `(kind, field)` in `write_matrix.yaml` | `SystemExit` — *"a duplicate makes the gate's behaviour depend on file order"* (`data/matrix.py:146-155`) |
| L24 | a matrix row whose `class:` disagrees with its `steps:` derivation | `SystemExit` (`data/matrix.py:131-143`) |
| L25 | a `steps:` abbreviation outside `CAL MAT DEL RES WIT CEN` | **bare `KeyError`** (`data/matrix.py:125`) — not a diagnosed refusal |
| L26 | a `social:` outside `true false n/a` | **bare `KeyError`** (`data/matrix.py:128`) |
| L27 | an 8th `tenure_kinds` member without extending `release`'s declared `domain:` | `SystemExit`, loader invariant 6 — *"an edge that can be opened and never closed, and a kind here and not in the roster is a closer for a relation that does not exist"* (`data/verbs.py:369-375`) |
| L28 | a `band_floors` or `wear_per_season` outer key that is not a `site_kinds` member | `Forbidden` — *"names site kind(s) no roster carries"* (`data/fixtures.py:111-117`). **EXECUTED: PLANT 1** |
| L29 | a `site_kinds` member **without** a `wear_per_season` rate AND a `band_floors` cell | `Ungraded` — *"has no row for site kind(s)"* (`data/fixtures.py:118-123`) |
| L30 | `site_yield` producing a matter kind outside `matter_kinds` | `Forbidden` — *"Open means addable, not unchecked"* (`data/fixtures.py:125-137`) |
| L31 | `site_yield` empty for every kind | `Ungraded` — *"shipping the control as the default"* (`data/fixtures.py:138-144`) |
| L32 | a roster with two owner pointers, or a pointer **and** `values:` | `Unspecified`, ED-IN-0230 (`data/rosters.py:104-119`) |
| **⊕ L33** | **a `remit_acts` value on an Office that is not on the roster** — which is what item 13 creates for any seat still carrying `remit_acts: [dispatch]` | `Unowned` at **construction**, not load — `Office.__post_init__` (`carriers.py:527-533`): *"A typo here would mint a remit act and every `remit:<that act>` eligibility would silently never match — a verb quietly unavailable to everyone, which is the worst shape a failure can take"*. **So `rosters.yaml` and `offices.yaml` must change in one commit** |
| **⊕ L34** | **a `Question` whose `source` is not on `question_sources`** — which every surviving `date_due`/`band_crossed` construction becomes at item 2 | `Forbidden` from `Question.__post_init__` (`carriers.py:254-256`). **This is item 2's own guard**: the roster edit makes the dead producers raise instead of returning `[]` |
| **⊕ L35** | **a `Record` whose `subject_matter` keys are not its kind's**, once `record_kinds` lands | **NOT BUILT — this is a row this suite must WRITE.** The refusal shape to copy is `Rung.__setattr__` (`carriers.py:589-596`), which whitelists against a declared set and raises `Forbidden` with the law inline. Until it is written, `⊕ S12` applies |
| **⊕ L36** | **a `conferral` / `revocation` / `binds` value outside its new roster** | **NOT BUILT.** Same shape, same file (`Office.__post_init__`, beside the `remit_acts` check at `:527-533`). Item 10 writes it; **without it, `03`'s closed sets are prose** (§0.05) |
| **⊕ L37** | `give`'s `writes:` naming `Tenure.since` + `Tenure.until` — both rows exist (`:343`, `:350`) | **loads.** Round one loaded five speculative rows against the real loaders, 43 rows, all green; `give`'s shape is `release`'s plus `confer`'s and needs no new row, form, operand or stem |
| **⊕ L38** | `found`'s `writes:` naming `Rung.exists` + `Site.exists` + `Rung.stores` | **loads** — all three rows exist (`:294`, `:322`, `:301`) |
| **⊕ L39** | deleting `(Person, beliefs)` while `Person.beliefs` the field stays, or vice versa | **NEITHER is refused at load.** `matrix_rows_without_a_field` (`carriers.py:599`) **REPORTS** it; the class stays constructible. This is `⊕ S13` |
| **⊕ L40** | deleting `Rung.judging_set_rule` from `_DECLARED` while `Rung.__init__` still pops it (`carriers.py:580`) | `Forbidden` from `__setattr__` — the `object.__setattr__` calls in `__init__` bypass it, so **the pop must go with the whitelist entry.** Item 14's one real coupling inside `carriers.py` |
| **⊕ L41** | deleting `Site.drawers` while `populated.py`/`corpus_run.py` construct a `Site(...)` with it | `TypeError`. **MEASURED: neither does** (`grep 'drawers'` → the `retired:` list only), so this one is clean |
| **⊕ L42** | adding `record_kinds` as a roster with `values: []` | **loads clean** and raises at the first `roster()` read (`data/rosters.py:189-195`): *"an empty set makes every membership test silently false, so it REFUSES exactly as an absent roster does"*. `record_kinds` is a **mapping**, so it must be read with `roster_map`/`table`, not `roster` — and `roster()` raises on a mapping and vice versa |
| **⊕ L43** | `emits:` on the CALENDAR `Date.fired` write naming a kind the row does not declare | `Forbidden` from `_refuse_undeclared_kind` (`world.py:275-293`). **The row DOES declare `date.fired`** (`write_matrix.yaml:100-111`), so item 2's one-argument change is admitted — *and the reverse is refused*: a MATTER-class write on a row declaring an `emits:` that names none is the silent write the gate forbids (`world.py:295-310`) |
| **⊕ L44** | `(Person, body)` written with `driver` other than `"Act"` | **NOT refused** — the row is `social: "false"` (checked: `write_matrix.yaml:161-167`), so `world.py:352-357`'s L4 limb does not fire and MATTER may write it. **Item 3b is admitted by the gate as it stands** |

> ### RULED: **L28/L29 REMAIN THE BUILT WORLD'S ONE HARD LOAD CONSTRAINT, AND THIS SUITE NOW HAS A SECOND ONE.**
> Adding a site kind is **three coordinated data edits, never one** — `site_kinds.values`,
> `wear_per_season.rates`, `band_floors.cells` — because `data/fixtures.py:106-123` checks membership
> in both directions. **And `L11` is the governance equivalent:** a matrix row and every `writes:`
> entry naming it are one edit. Three pairs in this suite:
> `(Dispensation, exists)`↔`issue`, `(Petition, exists)`↔`petition`, `(Office, establishment)`↔`establish`.

### A.2.2 · Refused at RUN time — the load is green and the verb dies later (14)

| # | the defect | what happens |
|---|---|---|
| R1 | `writes:` non-empty and **no `@effect_for` body** | the row is excluded from `resolvable_verbs()` (`loop/driver.py:96-99`); hand-folded, `Unspecified` — *"Part E does not say WHAT VALUE"* (`loop/resolve.py:238`). **MEASURED: `restore`, `issue`, `petition`, `commit`, `oblige`, `succeed`, `levy`, `establish` are all this today** |
| R2 | a prose `requires:` with no `REQUIRES_PREDICATES` entry and no typed cell | excluded from `resolvable_verbs()`; hand-folded, *"a precondition the fold cannot evaluate"* (`resolve.py:194`). **`comply`, `evade / defy`, `refract`, `thread_read` are this today** |
| R3 | `contests:` on a prize with a `module:` and no registered `provider:` | **silently dropped** from `resolvable_verbs()` (`driver.py:145-158`) |
| R4 | `contests:` on a prize absent from `contest_subsystems.prizes` | `manifest.resolve` returns `None` → the same silent drop. **Loads clean** |
| R5 | the effect reaches RESOLVE without an operand the payload carries | `InstrumentDefect` — *"a CALLER defect and not a design gap"* (`loop/effects.py:60-84`) |
| R6 | the effect touches nothing | the fold emits the **refusal**, not the success (`resolve.py:259-266`). ⚠ **Item 1's trap:** `@effect_for("commit")` must RETURN something, or `commit` will refuse every time it succeeds — `_eff_work` carries the worked comment: *"the fold now refuses an act whose effect touched nothing … saying so is what keeps the deferral from reading as a no-op"* |
| R7 | a write whose `(kind, field)` row does not admit the current step | `Forbidden` (`state/world.py:325-346`) |
| R8 | a `social: true` row written by anything other than `driver="Act"` | `Forbidden` — *"L4 — social:true means ONLY AN ACT may write it. The world may silt a harbour; IT MAY NOT SOUR A TOWN'S MOOD"* (`world.py:352-357`) |
| R9 | a `contain` Tenure that does not strictly ascend `rung_kinds` | `Forbidden` from `add_tenure` (`world.py:248-256`); `contain_ascends` (`world.py:197`) is the single owner |
| R10 | a `Tenure.kind` outside the seven | `Unowned` from `add_tenure` (`world.py:242-247`) |
| R11 | a `Rung` attribute outside the 11-name `_DECLARED` whitelist | `Forbidden` — *"a Rung owns NO social aggregate … EVERY ONE IS A QUERY"* (`carriers.py:568`; `__setattr__` `:589-596`) |
| R12 | a fixture the code names with no register row, or an unregistered site kind | `Ungraded` from `Fixtures.get` / `.wear` (`data/fixtures.py:45-70`). ⚠ **`fixtures.body_step` and `fixtures.told_drift_band` each need a `hole_register.yaml` row not graded `absent`, or the run refuses at the call site** — loader invariant 11, and it fires at RUN, not load |
| **⊕ R13** | **a `hold` Tenure whose object is not `Office \| Rung \| Record \| Proposition`** | **NOTHING today.** `add_tenure` checks the KIND (`:242-247`) and `contain`'s direction (`:248-256`) and never the object's class. `holonic §15`'s table: *"`hold` \| Person → Office \| Rung \| Record \| Proposition \| **1 per object**"*. Item 16 adds the conjunct |
| **⊕ R14** | **a `hold` Tenure opened on an object a person already holds** — the *1 per object* half | **NOTHING today**, and item 6 depends on it: `give` must **release** the giver's hold before minting the receiver's, or two people hold one writ. `_req_confer` (`predicates.py:180-190`) implements 1-per-object for OFFICES only, as a precondition, not as a carrier invariant |

### A.2.3 · Accepted and **INERT** — the silent class, and the dangerous one (15)

**These all load clean and are wrong, and nothing will tell an author.** Five of `ARCH §B.13`'s twelve
loader invariants — **2, 4, 5, 7 and 10** — are the reason: **they are specified and UNBUILT**, so the
defects they exist to refuse land silently and sit inert. §B.13's own grade line says *"MECHANICAL,
all twelve"*, and five of the twelve do not exist; that gap is what §A.2.3 is a manual substitute for.

| # | the defect | consequence | unbuilt invariant |
|---|---|---|---|
| **S1** | **any unknown column on a verb row** (`via:`, `population_cost:`, `conferral:`) | silently ignored. `_load_verb_table` reads exactly `verb stratum eligibility requires writes emits emits_on_refusal grade scale contests requires_typed requires_typed_note domain` and nothing else. A new column is a declared-but-unread field, which is `AX` **ID-13** | **10** |
| S2 | an `emits:` kind no `write_matrix.yaml` row declares | emitted by the fold anyway. `_refuse_undeclared_kind` (`world.py:275-293`) fires only on the `emits=` parameter, which the fold never passes — its emissions go through `ev()` | **7** |
| **S3** | a new `[RES]` matrix row with no producing verb | reported by `rows_without_a_producer()` (`data/verbs.py:485`), whose **only caller asserts the SHAPE and prints the count** (`engine/season/tests/test_season_shape.py:3076-3099`, `assert isinstance(no_producer, dict)` at `:3095`) and **cannot fail** | **2** (REPORT-ONLY) |
| S4 | `social: true` on a row with a `MAT` or `CEN` step | loads clean. The live data happens to satisfy it — **zero violations measured** — so a proposal is the first thing that could break it | **5** |
| S5 | an eligibility alternative that can decline with `emits_on_refusal: []` | loads clean; a refused act produces the body literal `act.ineligible` (`resolve.py:161`) | **4**, widened |
| **S6** | a 5th `eligibility_kinds` member, rostered | loads clean, and neither `_eligible` nor `person_side_eligible` has a branch, so the disjunct **falls through to `return False`** with no diagnostic (`decision/options.py:131-172`) | — |
| **S7** | a 9th `requires_operands` member, rostered and admitted by a form's `needs:` | **loads clean**, and `_derive_operand` (`options.py:259-323`) has no branch → `operands_for` returns `None` and **no Candidate ever forms** | — |
| S8 | a 6th `strata` member | loads clean; `stratum_of` maps it by roster index, so it works — and silently **reorders which acts see which world** (`rosters.yaml:142-146`: *"ORDER IS SEMANTIC HERE"*) | — |
| S9 | a 9th `rung_kinds` member | loads clean; changes `title_rank`'s ordinals, `contain_ascends`'s ordering and every `scale:` cell's meaning at once. ⚠ **This suite makes it WORSE before it makes it better:** `03`'s `rank(seat) = rung_kinds.index(seat.rung.kind)` gives the roster a second consumer with the same silence | — |
| S10 | a 7th `remit_acts` member | loads clean — which is why `levy`'s declared substitution *could* have closed as a one-line data edit, and `01`–`04` refuse that route | — |
| S11 | a roster with `values: []` that nothing reads | loads clean. `roster()`'s empty refusal (`data/rosters.py:189-195`) fires **at READ, not at load** | — |
| **⊕ S12** | **a `Record` whose `subject_matter` carries keys its kind does not declare** | ⚠⚠ **THE DANGEROUS ONE FOR THIS SUITE. `subject_matter: Any` (`carriers.py:429`)** takes anything. A writ with `to` misspelled `too` **mints, holds, deposits a content claim, and is asked about** — and `_derive_operand` reads `to` from the claim's value, finds nothing, `operands_for` returns `None`, and **no Candidate forms.** A malformed writ is therefore indistinguishable from an ignored one, which is the exact distinction `holonic §37.1` says *"is the whole of enforcement drama"*. **`⊕ L35` is the repair and item 5 must ship it in the same commit as the roster** | — (new) |
| **⊕ S13** | **a matrix row whose field is deleted, or a field whose row is deleted** | `matrix_rows_without_a_field` (`carriers.py:599`) **reports and does not raise**, and its own docstring says why: *"a row can legitimately outrun the model: Part D is the SPECIFICATION and this file is one implementation of it."* So item 14 must read the report, not trust the suite | **2**, sibling |
| **⊕ S14** | **a `content:` claim predicate nobody dispatches on** | loads clean, deposits, is asked about, and produces **no operand**. `store_kind_of` (`options.py:234-256`) is the precedent: it partitions on `stem == "stores"` and returns `None` for everything else, silently. Item 7 is the branch; **until it lands, item 5's claims are inert and the season looks identical** | — (new) |
| **⊕ S15** | **an `offices.yaml` seat whose `rung` names no Rung `build_realm` builds** | `Office` is constructed with a bare string; **nothing checks it against `w.rungs`.** A seat at `province 0` — which `build_realm` does not build (`AUDIT_VERDICT.md` limit 2: *"`build_realm` builds `province 0` and no `contain` chain names one"*) — would have empty `descendants` and **zero purview, silently.** Item 10 must assert every seat's `rung` is in `w.rungs` at build | — (new) |

> ### RULED: **THE PRE-FLIGHT IS RUN BY HAND AND NO GUARD MAY BE BUILT FOR §A.2.3.**
> Four of the original eleven, and `⊕ S13`, have `verb_table.yaml`, `write_matrix.yaml` or the loader
> itself as their subject — `CLAUDE.md` §0.1 pt 5's predicate excluding them by name: *"a guard whose
> subject is another guard"*, *"a grader over the gate list"*.
>
> ⚠ **BUT THREE OF THE FOUR NEW ROWS ARE NOT IN THAT CLASS, AND THE DISTINCTION IS THE POINT.**
> `⊕ S12`'s subject is **a writ a player wrote** — game state that crosses into the engine. `⊕ S14`'s
> is **whether an executor is ever asked.** `⊕ S15`'s is **whether a duke has purview.** Each is
> load-bearing *on the game*, so each **earns its guard** under the same predicate that forbids the
> others: `⊕ L35`'s loader refusal, item 7's branch with item 7's falsifier, and item 10's build-time
> assertion. **The predicate is not a ban on guards; it is a test of subjects, and these pass it.**
>
> What remains forbidden here is the planted-violation suite for §B.13's five unbuilt invariants —
> not because it is worthless but because **ratified position 23 already schedules it** (`ARCH §E`
> step 2: *"each invariant fails on a planted violation naming the row, then passes"*). Until
> position 23, the enforcement is that an author reads this table.

---

## A.3 · THE ENGINE CHANGES, PER FILE — today → becomes → what breaks → migration

**⚖ RR-B** marks a touch that makes a RATIFIED `architecture/` sentence false. **Those are ruling
requests, not edits** (`architecture/` is RATIFIED, ED-IN-0204), and every one is quoted at its `§`
in §C.4 and **is not edited by this suite.**

### A.3.1 · `engine/season/queries/world_q.py` (748 lines)

**Today.** `parent_of` `:48` · `descendants` `:54` · `judging_set` `:146` (raises
`Unspecified("judging_set_rule")`; **2 harness callers**) · `presence` `:172` ·
`establishment_of` `:399-413` (reads `off.establishment` at `:413`; **0 callers**) ·
`conferral_path` `:416-437` (**0 callers**) · `questions_for` `:439-550`, four sources at
`:473-480` / `:482-494` / `:496-518` / `:520-528`, `mine` at `:471`, the two-key sort at `:548-549` ·
`occasioned_by` `:553-632`.

**Becomes.** `reach(w, p)` NEW, beside `descendants` · `place_of(w, x)` MOVED IN from
`epistemic._event_place` `:215` · `nearest_store(w, rung, kind)` NEW, on `parent_of` ·
`questions_for` with **two** sources and `01`'s three-clause Q2 test · `occasioned_by` with **one**
route · `establishment_of` over `oblige` Tenures, **with item 9 as its caller or not at all**
(§A.1.5 (d)) · `judging_set` and `conferral_path` **deleted**.

**What breaks.**
- ⚠ `occasioned_by`'s shape, and **the plan described it wrongly.** ~~*"the `date_due` and
  `band_crossed` routes are dead (the branches return `[]`)"*~~ → **there is no `date_due` branch and
  no `band_crossed` branch.** `claim_landed` has a branch at `:616-620`; **everything else falls
  through** a guard at `:621-628` that raises `Unspecified` for any source *not* in
  `("date_due", "band_crossed")` and then into a **generic id search over `reversed(w.log)`** at
  `:629-632`. The two routes are *live code that finds nothing*, not empty returns. Deleting the two
  sources makes the guard's tuple empty, so **the guard and the id search both become dead and must
  go with them** — one route, one branch, no fallthrough.
- `test_w5_q_has_a_producer_across_all_four_sources` (`engine/season/tests/test_season_shape.py:2361`)
  loops over `QUESTION_SOURCES` with a per-source branch, so it **passes unchanged and its NAME
  becomes false.** Rename it in the same commit; that rename is item 2's cheapest falsifier.
- Nothing pins the roster's LENGTH at four (`grep -n 'QUESTION_SOURCES' engine/season/tests
  tests/valoria` → `:35` import, `:2369` the loop, `:9590` a docstring about the sort).
- Every golden through DELIBERATE.

**Migration.** One commit, with the `rosters.yaml` edit (§A.3.6) — `Question.__post_init__`
(`carriers.py:254-256`) makes the order irrelevant by refusing either way (⊕ L34).

### A.3.2 · `engine/season/loop/calendar.py`

**Today.** `:37-38` writes `Date.fired` through the gate with **no `emits=` and no `subject=`**,
while the matrix row declares `emits: "date.fired"` (`write_matrix.yaml:100-111`, `steps: [CAL]`).

**Becomes.** `emits="date.fired"`, `subject=<the date's venue>`. Nothing else.

**What breaks.** Every hash through CALENDAR **on a world that fires a date.**

> ### RULED: **THE Q1 FOLD HAS NO PRODUCER TODAY, AND THE PLAN'S WITNESS SET HAS NO SOURCE. BOTH MUST BE SAID.**
> **MEASURED 2026-09-17:** after one populated season, `w.dates` is **empty** and `w.docket` is
> **empty** — `convene` is resolvable but never executes in that world, so `date_due` fires on
> nothing (§A.1.1 (b)). **Item 2's CALENDAR half is therefore unobservable on any world any gate
> runs**, exactly as round one's item 1 was, and it splits the same way: **2a** (reach + sources,
> observable today) and **2b** (the CALENDAR emit, observable on a planted date).
>
> And the plan's *"the parties named on the date … are its `witness_key`"* names a key that does not
> exist. **OPENED, `_eff_convene` (`loop/effects.py:174-190`): a date is
> `{"id", "venue", "due_at", "convening_attached"}` and nothing else.** No party list, and **no
> `holder`** — which `grep '"holder"'` confirms is written nowhere in production, so `calendar.py:33`'s
> `vacant = not d.get("holder")` is **always true** and Q1's `d.get("holder") in (p.id, None)` admits
> **everybody**. So the witness set for a fired date is **the convener plus whoever is co-located at
> the `venue`**, by `_ch_co_located` (`epistemic.py:244`) — and the `witness_key` channel
> (`epistemic.py:336`) reaches only `e.subject` and knot-partners. `01` owns the design statement;
> the ledger consequence is that item 2b adds **no** party carrier and claims **no** named-party
> witness.

### A.3.3 · `engine/season/loop/matter.py`

**Today.** The decision row at `:48-50` declares
`not_implemented=["the death cascade (S31.1 exception 2)", "bodies, larders, yield, travel (S25's
other rows)"]` — **stale about larders and yield, both of which run at `:155-224`.** Larder loop
`:167-195`: `eaters = world_q.presence(w, rid)` `:169`, `draw = {k: wt * len(eaters) …}` `:174`
against `r.stores` of the **same** rung, shortfall TRACE-only `:184-185`. Wear + crossing block
`:226-275`: `if before >= floor > s.condition:` `:262`, Event `:266-270` with `subject=s.id` and
`changes=[]`, `w.crossings.append(...)` `:272`.

**Becomes.** Larder **per eater** at `nearest_store(w, place_of(p), kind)`, drawing `wt * p.weight`
(`Person.weight` `:376`, which the current draw ignores) · shortfall → `Person.body` through
`w.write(..., record_kind="Person", fieldname="body", emits="body.changed")` · `_crossings(...)`
helper shared by sites and persons, **both reading `band_floors`** (§A.1.5 (a)) · body 0 →
`World.remove_person` · `w.crossings.append` deleted · `not_implemented` reduced to `["travel"]`.

**What breaks.** `test_w8_...order...` asserts larder-before-yield — **kept true, re-run.** Goldens
through MATTER. The two `probes.py` readers of `w.crossings` (`:680`, `:2562`) re-point to `w.log`.

> ### RULED: **`Person.body`'s CONSUMER IS ALREADY WIRED, AND THAT IS ITEM 3b's REAL ARTIFACT.**
> `AX-5`, ratified: *"THE WORLD MOVES BY ITSELF IN EXACTLY THREE WAYS: MATTER, BODIES, AND THE
> FADING OF MEMORY."* Matter runs (`:155-224`). Memory fades (`claim.decayed`, `:146-153`). **Bodies
> have no writer** — `(Person, body)` is a matrix row (`write_matrix.yaml:161`), `Person.body` is a
> field (`carriers.py:392`), and nothing between them.
>
> **EXECUTED 2026-09-17, on the tree as it stands:**
> ```
> body=1000 → budget 5   body=799 → budget 4   body=499 → budget 3   body=99 → budget 2
> ```
> `body_band_penalty` → `budget` → `pack_scenes`. **So the one missing object is the writer**, and
> the moment it lands a hungry hearth's people get fewer scenes — no new consumer, no new table, no
> new ladder. Item 3b's execution artifact is therefore a **budget histogram**, not only a census.

### A.3.4 · `engine/season/loop/witness.py` and `engine/season/epistemic.py`

**Today.** `_told_content` `:31` passes the teller's claim **verbatim** at every degree; the told
channel `:280-365` with `news.told` at `:316`. `_event_place` `:215`, one caller `:253`.
`_ch_co_located` `:244` · `_ch_document_key` `:260` (reads `changes[]`, `R8.4`) ·
`_ch_witness_key` `:336` · `_ch_post_remit` `:343-362` · `_ch_chronicle` `:365` ·
`observers_for` `:405`. **MEASURED: `"inferred"` has ZERO occurrences in non-test `.py`** — the
`claim_sources` roster (`rosters.yaml:129-136`) declares it and nothing writes it.

**Becomes.** The **deposit rule** as one branch where the observation deposit runs, keyed on a
hold-on-a-Record in `changes[]` · `_told_content` takes the resolution degree and returns a **lossy
copy at `Partial`**, the teller's own ledger untouched · `_event_place` → `world_q.place_of` ·
`_ch_post_remit` → **the obligees of a seat, co-located**, minting `inferred`.

**What breaks.** `test_r8_4_document_key_reaches_a_non_author_through_a_store` — **kept, re-run.**
**MEASURED 2026-09-17: `told_by` = 1 claim of 2,175 after one populated season** (`firsthand` 2,174),
so `_told_content`'s Partial branch has a producer of exactly one and the 89-world figure must be
re-measured on the corpus, not the populated world.

> ### RULED: **`_ch_post_remit` MINTING `inferred` CONFORMS TO RATIFIED `ARCH §C.6` — IT IS NOT A DEPARTURE.**
> `ARCH §C.6`'s mint table already says: `post_remit` mints *"the change claims, `inferred`"*. The
> channel exists (`epistemic.py:343`) and the source exists on the roster; **the writer is what is
> missing.** So item 9 implements a ratified row. ⚠ **The deposit rule does NOT conform**: §C.6 gives
> `document_key` *"the change claims only. No attribution"*, and a content mint is a **sixth cell
> the table does not have.** That is RR-B limb 5, stated in §C.4 and not edited here.
>
> ⚠ **And `refract`'s deletion EXECUTES a Jordan ruling rather than discarding one.** `H-36`
> (`hole_register.yaml:394`, `grade: ruled`): *"RECEIVER-SIDE. ⚠ AN EMISSION IS NEVER DISTORTED
> (Jordan, 2026-09-02): what refracts is the PREMISES AND RATIONALE, minted per receiver as a
> Claim."* `02`'s lossy `tell` **is** that mechanism. The verb row goes; the ruled behaviour arrives.

### A.3.5 · `engine/season/loop/effects.py` and `loop/predicates.py`

**Today.** 11 bodies (§A.1.2). `_eff_confer` `:93-126` · `_eff_work` `:245-260` (**returns the site
and applies no delta** — §27.3 sums and clamps once) · `_eff_create_record` `:263-290`, minting the
maker's hold at `:288-289` · `_eff_kill` `:309-419`, cascade `:416-418`. Predicates:
`in_holdings` `:60` · `under_purview` `:105-143` (walks `titles_held`, and **ascends from the holding**, so it already admits the seat's own rung — §A.1.6 (c)) · `titles_held` `:144` ·
`highest_title_rank` `:157` · `_req_confer` `:167-191` (empty-`conferral` refusal `:181-182`) ·
`_req_release` `:194` · `_req_revoke` `:222-288` (empty-`revocation` refusal `:234-235`, the
`is_title` branch `:252-274`) · `_req_dispatch` `:291-295` · `_req_convene` `:298`.

**Becomes.** NEW bodies `commit`, `oblige`, `issue`, `petition`, `give`, `restore`, `found` ·
`_eff_confer` also mints the `commission` Record · `_eff_work` advances a `works` Record's `stage`
and applies the plan at the last stage · `_eff_kill` calls `World.remove_person` · `_req_confer` /
`_req_revoke` on rostered values · NEW `_req_oblige`, `_req_issue`, `_req_give` · `_req_dispatch`,
`titles_held`, `highest_title_rank` deleted.

> ### RULED: ⚠⚠ **`revocation: "holdings"` IS A CONJUNCTION OF THREE, AND `in_holdings` ALONE IS A DEFECT THIS TREE ALREADY FOUND AND FIXED.**
> ~~`"holdings"` → `in_holdings` (`:60`)~~ → **`"holdings"` → `under_purview` AND `in_holdings` AND
> strictly-higher rank.**
>
> `_req_revoke`'s own comment at `:255-266`, verbatim: *"⚠ A CONJUNCTION, AND THE FIRST VERSION WAS A
> SINGLE TERM. It tested `in_holdings` ALONE, which makes holdings SUFFICIENT — so a Dicastery clerk
> who happened to hold a duchy could unmake its Duke, and a Duke holding the realm could unmake the
> King."* Three of Jordan's 2026-09-02 sentences are in that branch, and the single-term reading
> **was tried and reverted.**
>
> **And ratified `ARCH §B.7` call 1 says the same thing in the same words:** *"An ordinary seat
> revocable on purview alone and a title needing **purview + holdings + higher rank** are two values
> of `revocation.conjuncts`."* So the repair is not a concession to the old code — **it is what
> Layer 1 prescribes**, and the plan's version contradicted it.
>
> ⚠ **THE RANK TERM IS DERIVED, NOT DELETED, AND `03` DERIVES IT FROM CONTAINMENT RATHER THAN FROM
> AN ORDINAL.** ~~`rank(seat) = rung_kinds.index(seat.rung.kind)`~~ → **`03_SEATS_AND_CONTENT.md`
> derives the conjunct from `World.contain_ascends` (`state/world.py:197`), the single owner of the
> ladder, enforced at the one writer (`add_tenure`) and verified by `03` over all 373 `contain`
> edges.** That is strictly better than an ordinal lookup, because `rung_kinds.index` is **S9** —
> a ninth roster member silently re-ranks every seat — whereas `contain_ascends` is checked at the
> only place a `contain` edge can be created.
>
> **So all four title helpers go as NAMES (§A.1.1 (f) rows 30–33) and the RULE survives as a
> derivation.** The ledger books four deletions and **zero additions**, because the derivation adds
> no name: it asks an owner that already exists.
>
> ⚠ **AND IT BUYS ONE DECLARED BEHAVIOUR CHANGE, WHICH `03` STATES AND THIS LEDGER REPEATS RATHER
> THAN BURYING:** under containment-derived rank, **a lower seat that holds the land may now unmake
> the seat above it.** Today `highest_title_rank(actor) <= title_rank(target)` refuses that by
> ordinal. It is a design consequence, not a slip — but it is a *change to who may unmake whom*, and
> it belongs in front of Jordan beside RR-B rather than inside an item. **`03`'s RR-B.2 is where it
> is filed; §C.4's B-8 carries it here.**
>
> **What does NOT change: the conjunction is three terms.** Without all three, a Dicastery clerk who
> holds a duchy can unmake its Duke — a defect this tree already found and reverted. That is the
> single most important correction in this file.
>
> ⚠ **The residue, stated and DOWNGRADED from this file's first draft:** `ARCH F.21` —
> *"the rank of a cluster seat (`scope = null`): no rank; the loader forbids a `higher_rank` conjunct
> on one"* — is **NARROWED, not closed.** ~~closes by construction~~ → every seat getting a `rung`
> abolishes F.21's *subject* (there is no cluster seat) and **leaves its remedy unwritten** (no loader
> forbids the conjunct). A hole whose subject is gone and whose remedy is absent is narrowed, and it
> is filed as `03`'s **RR-B.2** / this file's **B-8** rather than as a closure — because
> `§B.7`'s `Seat :=` spells `scope? (null = a cluster)` and `holonic §37.3` row 3 protects
> *"office-clusters with `rung? = null`, which have no place"* by name.

**What breaks.** `grep title_domain engine/season/tests` → `test_season_shape.py` (imports it at
`:35`); the `@effect_for` count 11 wherever asserted; the H-71 person-side decline test, **which
item 11 turns RED on purpose and rewrites as its own control.**

**Migration.** **Bodies first** (they add and break nothing), **predicates second** (they change
behaviour), **deletions last** (they need the tests rewritten). Three commits minimum.

### A.3.6 · `rosters.yaml`, `verb_table.yaml`, `write_matrix.yaml`, `data/rosters.py`

**Today.** `tenure_kinds` `:101-104` (seven) · `rung_kinds` `:106-109` (eight) · `remit_acts`
`:111-119` (six, with `dispatch`) · `claim_sources` `:129-136` · `question_sources` `:250-270`
(four) · `titles` `:692` · `site_kinds` `:805-816` `[harbour, seam, body]` · `wear_per_season`
`:830-844` (`body: 10`) · `band_floors` `:1175-1199`, `sweep: [declared, halved, doubled]` `:1179`,
`keys: [site_kinds]`, **`body: {full_operations: 800, limited: 500, withdrawal_only: 100}`** ·
**38 verb rows** · **40 matrix rows** · `title_domain` `data/rosters.py:459`, `title_rank` `:465`.

**Becomes.** `question_sources: [claim_landed, need]` · `remit_acts` minus `dispatch` (five) · NEW
`record_kinds`, `conferral_bases`, `revocation_bases`, `binds_bases` · `titles` deleted, its domains
moving into `offices.yaml` · verb rows: `levy` deleted now, the four response/dispatch rows deleted
**under RR-A**, NEW `give`, `found` → **35 rows** · matrix: the six rows of §A.1.1 (d) deleted →
**34**, `(Person, body)` gains MATTER as its writer, `(Rung, exists)`/`(Site, exists)` gain `found`,
`(Record, exists)` gains `issue` and `petition` · `fixtures.body_step`, `fixtures.told_drift_band`,
each with a `hole_register.yaml` row (⊕ R12) · `title_domain`/`title_rank` deleted.

**What breaks.** The matrix header's own stale counts (`write_matrix.yaml:36-53`) get re-measured.
**MEASURED: 10 producerless `[RES]` rows today** (the header's own reproduce command at `:41-45`).
After this suite: `Rung.dates`, `Tenure.payload`, `Person.beliefs` deleted; `Rung.exists`,
`Site.exists` get `found` — leaving **`Person.{axis_count, coherence, convictions, scar, stance}` =
5**, which is exactly `ARCH F.20a` / `H-62` and **is not this suite's**.

> ### RULED: **PRODUCERLESS `[RES]` ROWS 10 → 5, AND THE FIVE THAT REMAIN ARE `H-62` AND NOBODY ELSE'S.**
> Stated because a reader will otherwise attribute the residue to this suite. `ARCH F.20a`:
> *"NO VERB WRITES ANY `Person` INTERIOR FIELD … every interior consequence is inert."* `(Person,
> body)` is **not** one of F.20a's four, so writing it neither closes F.20a nor touches it. Ratified
> position 12 (`H-62-rest`) owns the five.

### A.3.7 · `state/carriers.py` and `state/world.py`

**Today.** The fields of §A.1.1 (e), with `Office.__post_init__` `:506-548` calling `title_domain`
**twice** (`:536`, `:546`) and `BODY_FUNCTION` once (`:545`). `Rung._DECLARED` `:568`,
`__init__`'s pops `:574-582`, `__setattr__` `:589-596`, `matrix_rows_without_a_field` `:599`.
`World.__init__` `:151-177`; `add_tenure` `:223-258` with the kind check `:242-247` and
`contain_ascends` `:248-256` and **no object-class check**. `Record` `:422-445`, `subject_matter:
Any` `:429`.

**Becomes.** Fields deleted (⊕ L40 couples `_DECLARED` to the `__init__` pops) · the title-in-a-body
refusal re-expressed on `revocation == "holdings"` · `Record.subject_matter` **typed per
`record_kinds`** (⊕ L35) · `add_tenure` refuses a `hold` whose object is not
`Office | Rung | Record | Proposition` as **one more conjunct beside `:242-247`** (⊕ R13) ·
`World.remove_person`.

**What breaks.** `matrix_rows_without_a_field` reports change — **desired, and it is a report, so
item 14 must read it** (⊕ S13). `harness/invariants.py:72`'s entity set loses two members, and
`test_the_entity_set_covers_every_world_collection_a_tenure_can_name` is the falsifier that it was
edited.

**⚖ RR-B.** `ARCH §B.7`'s `Seat :=` line spells `scope?`, `remit(acts[], binds)`, `upkeep`,
`dates[]`. `ARCH §B.8`'s `Tenure :=` spells `term? … -- T-n. Replaces payload?`. Quoted in §C.4.

### A.3.8 · `decision/options.py`, `decision/budget.py`, `data/fixtures.py`

**Today.** `opening_set` `:35-104` · `person_side_eligible` `:107-169`, the `remit:` decline
`:163-165` and the `presence:` decline `:166-168` · `containing_rung_of` `:172-177` ·
`store_kind_of` `:234-256` · `_derive_operand` `:259-343`: `to` ← the referent `:308-309`, `site` ←
the referent `:310-311`, `from` ← `containing_rung_of` `:316-317`, `kind` ← `store_kind_of` or
`default_store_kind` `:319-320`, `amount` ← `default_transfer_amount` `:321-322` ·
`agreement` `:412` · `budget.py:56-57` · `body_band_penalty` `:63-75` · `fixtures.py:430`.

**Becomes.** `remit:` person-side via the `content:commission` claim (`03`) · `_derive_operand` reads
`to`/`amount`/`kind`/`at` **from a `content:` claim's value** when the question's referent is one —
the same shape as `store_kind_of` reading the question · `budget_office_bonus` term **and** its
fixture deleted.

> ### RULED: **DELETING `budget_office_bonus` CLOSES `H-92`'s FIRST CONSUMER AND THE UNSPENDABLE SIXTH SCENE WITH IT, AND IT IS OBSERVABLE ON A WORLD THAT RUNS.**
> `budget.py:56` counts **every live `hold`**, not every Office — so a landholding pays. And
> `hole_register.yaml:176` measures the consequence: *"planting one live `hold` on `p_carin` moves
> her budget 5 → 6 and leaves the releasable count at 5, so the sixth scene is unspendable."*
> **Two defects, one deletion, one line.** ⚠ The same row records that *"0 of 143 cases carry an
> `office.post` … so all 258 persons across the 86 buildable worlds hold zero offices and budget
> exactly 5"* — **so the deletion changes nothing that runs today, and that is the control.** It goes
> live the day item 10 seats office-holders, which is precisely why it is deleted **before** item 10.

### A.3.9 · `harness/populated.py`, NEW `engine/season/data/offices.yaml`

**Today (all MEASURED 2026-09-17 on `build_realm(0)`).** 19 offices · **19 of 19** with empty
`conferral` AND empty `revocation` · **16 of 19** with `rung is None` · **16 of 19** with
`remit_acts: []` · **0 of 19** with a non-empty `establishment` · 35 `hold` Tenures = **19
person-subject + 16 faction-subject** · 46 persons in **26** hearths · 74 sites, **all** keyed to
settlements, **0** with anyone present at their own rung · **13 of 37** settlements with anybody in
their `contain` subtree · rungs `{realm 1, duchy 3, territory 17, settlement 37, community 60,
hearth 211, person 46}` · stores **0** at build and **4,810 after one season, all 4,810 at the 37
settlements and 0 at the 211 hearths** · 0 records/dates/docket/crossings at build, **69 records and
still 0 dates/docket/crossings** after one season.

**Becomes.** Offices from `offices.yaml` with a `rung`, `remit_acts`, `conferral`, `revocation` and
`binds` for **every** seat; holders **seated at their seat's rung**; the 16 faction-subject holds
re-homed to the seat-holder of the faction's head seat, with ⊕ R13's guard refusing the old shape.

**What breaks.** `census` counts — **declared re-record.** `probes.py:1376`'s
`assert off.establishment == []`.

---
## A.4 · THE BUILD ORDER

Sizes: **S** < 60 lines, one file · **M** one barrier or two files · **L** a schema or a roster with
its loader and its tests.

### A.4.1 · THE FIRST FIVE — each needing no ruling, each yielding a running season

Every block runs **Change → Why here → Execution artifact → Control → Cost → Breaks if wrong →
Falsifier**, which is the ratified per-instruction template.

#### 1 · `@effect_for("commit")` — mint the Tenure the row already declares · **S** · Arc-2: YES · ratified position: 14 (`U7-own`)

**Change.** `verb_table.yaml:115-128`'s `commit` row declares `writes: ["Tenure.since"]`,
`emits: ["commitment.made"]`, `eligibility: ["own"]`, and a typed cell
`existence(of: subject, kind: Proposition)`. It has **no `@effect_for` body**, so **R1** excludes it
from `resolvable_verbs()` — MEASURED: `commit` is not among the 18. Add
`_eff_commit(w, a, res)` → `w.add_tenure(Tenure(H(...), a.actor, <the Proposition>, "commit",
since=w.tick))`, returning `[the proposition id]`.

**Why here.** `AUDIT_VERDICT.md`'s own verdict names it: *"'The whole difference is one artifact' —
`@effect_for("commit")`."* It is the smallest object in the suite and it unblocks the most, because
`commit` is **Q4 `need`'s producer**: `questions_for`'s Q4 (`world_q.py:520-528`) fires on *a live
`commit` Tenure whose object is an OUGHT Proposition*, and `need` is already **81 questions** on the
populated world — supplied entirely by `build_realm`'s hand-minted commits
(`harness/populated.py:823`). Today no ACT can make one. After item 1, a person can.

**Execution artifact.** A seeded season in which a person with a `content:` claim naming a
Proposition commits, and `Tenure.since` is set; plus `resolvable_verbs()` going **18 → 19** and
`corpus_run`'s `VERBS THAT EXECUTED` line rising by one (`harness/corpus_run.py:645`).

**Control.** Same seed, body absent → **no Tenure, and `commit` back outside `resolvable_verbs()`**.
The control is an identity on every other count.

**Cost.** One function, ~12 lines. No new row, form, operand, stem or roster.

**Breaks if wrong.** **⊕ R6 is the trap**: an effect that touches nothing makes the fold emit the
*refusal* (`resolve.py:259-266`). The body must return the object it opened.

**Falsifier.** `test_commit_opens_a_tenure_and_need_then_fires_for_its_holder` — and it must observe
**both** halves, because a body that mints a Tenure the Q4 branch cannot see is the
`(Person, body)`-style half-wiring this suite is full of. **LB-1**: if `need` does not rise on the
next season for that person, the mint named the wrong object.

#### 2 · The Q1/Q3 fold — `reach`, `place_of`, two sources, `w.crossings` deleted · **M** · Arc-2: no · position: fix

⚠ **SPLIT, on §A.0.3's rule.** The plan had one item; **2b is unobservable today** (§A.3.2).

**2a — `reach`, `place_of`, the three-clause Q2 test, the two roster deletions, `w.crossings`
deleted, `occasioned_by` reduced to one route.** Observable on the populated world.
**2b — CALENDAR passes `emits="date.fired"`, `subject=venue`.** Observable only on a planted date, or
after `convene` executes in a world that runs.

**Why here.** It needs no ruling, it touches no effect body, and it is the only item that **reduces**
the question machinery while adding a term.

**Execution artifact (2a).** The question histogram, before and after, same seed:
```
before (MEASURED 2026-09-17):  {'claim_landed': 561, 'need': 81}   date_due 0, band_crossed 0
after:                         {'claim_landed': N,   'need': 81}    two sources only
```
Plus **a declared golden re-record in the commit message** (`CLAUDE.md` §7).

**Control — and it is an identity, which is what makes the two effects separable.** The two deleted
sources contribute **0** questions today (MEASURED). So *every unit* of movement in `claim_landed` is
REACH's, and none of it is the deletion's. A second control arm: a person with **no seat** must show
the **same** question count before and after, because REACH adds `⋃ descendants(seat.rung)` and
nothing else.

**Cost.** Two Queries (one new, one moved), one roster edit, one `World` attribute deleted, one dead
guard and one dead id search deleted (§A.3.1).

**Breaks if wrong.** `H-110`'s own warning applies to the referent change: *"A one-line change to a
rule three other rows depend on is a design edit, not a repair"* — the dependent rows are `H-54`'s
source-order tiebreak and the aggregation rule. **Two questions must not collide on one `q.id`.**

**Falsifiers.** **LB-2a** `test_a_duke_is_reached_by_a_crossing_in_his_purview_that_he_witnessed`.
**LB-2b — THE FLOOD TEST, and it is the one that matters:**
`test_a_duke_is_NOT_reached_by_a_crossing_in_his_purview_that_nobody_witnessed`. REACH must filter
claims that already landed by a witness channel and **never widen the fan** — `observers_for`
(`epistemic.py:405`) is untouched, and the test asserts that by counting observers before and after.
**LB-2c** `test_a_fired_date_deposits_a_claim_in_the_conveners_ledger` (2b, on a planted date).
**LB-2d** the rename: `test_w5_q_has_a_producer_across_all_four_sources` →
`..._across_both_sources`, because a test whose name says four while the roster says two is
`CLAUDE.md` §4's idempotence failure in a test name.
**LB-2e — THE INCLUSIVE-WALK TEST (§A.1.6 (c)):**
`test_a_duke_is_reached_by_a_claim_about_his_own_duchy_rung`. `descendants(w, rung)` **excludes
`rung`**, so a `reach` limb written as `⋃ descendants(seat.rung)` silently loses the seat's own rung
and a Duke is not asked about his own duchy. The limb is `{seat.rung} ∪ descendants(...)`, and this
test fails on the bare form.

#### 3a · `nearest_store` and the per-eater draw · **M** · Arc-2: no · position: fix

**Change.** `matter.py:167-195`'s loop is per RUNG against that rung's own stores. It becomes: per
EATER, at `nearest_store(w, place_of(p), kind)`, drawing `wt * p.weight`.

**Why here.** **MEASURED 2026-09-17:** after one season the world holds **4,810 units, all 4,810 at
the 37 settlement rungs, and the 211 hearth rungs hold none**, while all 46 persons live in **26
hearths** and **0 of 74 sites** have anyone present at their own rung. So
`draw = {k: wt * len(eaters)}` counts **zero eaters at every rung that has stores**. The subsistence
economy is two halves that never meet, and one walk joins them with **no content move and no new
store** — which is why `02_THE_BUILT_WORLD.md`'s two content moves are withdrawn.

**Execution artifact.** `harness/populated.py::census` before/after on the 37/211 world:
```
before:  settlement stores 4810 · hearth stores 0 · draw executed at 0 rungs
after:   26 hearths draw from their settlement; settlement stores fall by Σ(wt × weight)
```
With `subsistence_weight {grain: 2, salt: 1}`, 46 persons at weight 1 draw **92 grain + 46 salt** per
season against 4,810 produced. ⚠ **The draw must use `p.weight`, which the current loop ignores**
(`Person.weight` `:376`, *"A COHORT IS A PERSON AT weight > 1"*), or a cohort of 200 eats like one man.

**Control.** A hearth **that has its own stores** must draw locally and unchanged — `nearest_store`
returns the rung itself when `stores.get(kind, 0) > 0`, so the walk is a no-op where the old code was
already right. If that arm moves, the walk is not a generalisation.

**Cost.** One Query (~10 lines), one loop rewritten.

**Breaks if wrong.** `test_w8_...order...` asserts larders before yield. **Kept true** — the order at
`matter.py:155-166` is `#353 §25`'s and is not this item's to change: *"a season's subsistence is
drawn against LAST season's stores."*

**Falsifier. LB-3a** `test_a_hearth_with_no_larder_eats_from_its_settlement`, plus
`test_a_hearth_with_its_own_larder_eats_locally` as the paired control, plus
`test_the_root_larder_at_zero_feeds_nobody_and_raises_nothing` (`nearest_store` returns `None` at the
root, and `None` must produce a shortfall, not a `KeyError`).

#### 3b · The body write, the shared `_crossings`, `remove_person` · **M** · depends on 3a · Arc-2: no

**Change.** Shortfall → `Person.body` through the gate. The crossing block at `matter.py:255-275`
factors into `_crossings(w, id, kind_floors, before, after, cause)` called for sites **and for
persons**, both reading `band_floors`. Body 0 → `World.remove_person`, factored from `_eff_kill`
`:416-418`, with MATTER and RESOLVE as its two callers.

⚠ **NO NEW BAND TABLE. `band_floors["body"]` ALREADY EXISTS AND `budget` ALREADY READS IT**
(§A.1.5 (a)). The plan's `band_floors.person` is **refused at load** (PLANT 1) and would have been
the second scheme `H-38` was closed to avoid.

**Why here.** `AX-5` names three self-motions; **bodies is the one with no writer.**

**Execution artifact.** An empty-root world: bodies fall by `body_step`, cross
`full_operations` (800) then `limited` (500), a `condition.band_crossed`-shaped claim lands, the
hearth's holder and the settlement's seat are asked by REACH — **and the budget histogram moves**,
which is the consequence that is already wired:
```
EXECUTED on today's tree:  body 1000→budget 5 · 799→4 · 499→3 · 99→2
```

**Control.** A **stocked** world: bodies constant at `condition_scale`, budget histogram flat at 5,
`_crossings` fires for sites only. Same seed, same everything else.

**Cost.** One write, one helper factored (0 net objects), one method factored (0 net), two fixtures.

**Breaks if wrong.** ⚠ **The read/write asymmetry `CLAUDE.md` §0.1 pt 1 is about.** `budget` reads
`p.body` **today**; if the MATTER write lands on a copy, or on a `Person` the tenure view rehomed,
every reader silently keeps seeing 1000. **Grep the field's ASSIGNMENTS, not its readers**, and the
template is `tests/valoria/test_morale_write_sweep.py`, whose `_CELL_OWNED` registry is
field-parameterized — **`Person.body` inherits the guard by adding one key**, which is the one guard
in this suite that is free.

**Falsifier. LB-3b** `test_a_short_larder_falls_a_body_a_band_and_narrows_the_season` — it must
assert the crossing **and** the budget drop, because either alone is half-wiring.
**LB-3c** `test_death_at_body_zero_closes_every_tenure_through_the_same_owner_as_kill`, asserting
**one** cascade site: `grep -c "t.until = w.tick" engine/season` must be **1**.

#### 4 · Delete `budget_office_bonus` · **S** · Arc-2: no · ratified position: 14

**Change.** `budget.py:56-57`'s two lines become one: `b = k - body_band_penalty(p, fx) - len(...)`.
`fixtures.py:430` goes with it.

**Why here.** Before item 10. The moment seats are filled, the defect goes live
(`hole_register.yaml:176`: 0 of 143 cases carry an `office.post` today, so all 258 persons across the
86 buildable worlds budget exactly 5). Deleting it first means **no world ever runs with the defect
reachable.**

**Execution artifact.** `python -m pytest engine/season/tests -q -k test_u2_` and the planted-hold
measurement: budget stays **5**, not 6.

**Control.** The other two budget terms unchanged — `body_band_penalty` and the leg penalty must
still move the number, or the deletion removed the wrong line.

**Cost.** Two lines and a fixture cell. **This is the cheapest item in the suite and it closes two
register rows** (`H-92`'s first consumer; `hole_register.yaml:176`'s unspendable sixth scene).

**Falsifier. LB-4** `test_budget_ignores_held_offices_and_holdings_alike`, with a planted hold on a
**Rung** as well as one on an Office — because `H-92` is about the Rung case and a test that plants
only an Office cannot observe it.

### A.4.2 · THE WHOLE ORDER, dependency-sorted

| # | item | size | depends on | falsifier | execution artifact | control | Arc-2 | ratified position |
|---|---|---|---|---|---|---|---|---|
| **1** | `@effect_for("commit")` | S | — | LB-1 | `resolvable_verbs()` 18→19; a `commit` Tenure in a seeded season | body absent, same seed: no Tenure | **YES** | 14 |
| **2a** | `reach` · `place_of` · two sources · `w.crossings` deleted · `occasioned_by` → one route | M | — | LB-2a, **LB-2b**, LB-2e | question histogram, same seed; golden re-record **declared** | the two deleted sources contribute **0** (MEASURED) — an identity; and a seatless person's count is unchanged | no | fix |
| **2b** | CALENDAR `emits="date.fired"`, `subject=venue` | S | 2a | LB-2c | a planted date deposits a claim in the convener's ledger | no date planted: no Event, no claim | no | fix |
| **3a** | `nearest_store` + the per-eater draw | M | — | LB-3a | `census` before/after on 37/211 | a stocked hearth draws locally, unchanged | no | fix |
| **3b** | body write · shared `_crossings` · `remove_person` | M | 3a | LB-3b, **LB-3c** | empty-root run: bands crossed **and** budget histogram moves | stocked world: bodies flat, budget flat at 5 | no | fix |
| **4** | delete `budget_office_bonus` | S | — | LB-4 | `pytest engine/season/tests -k test_u2_`; planted hold → budget 5 | the other two budget terms still move | no | 14 |
| 5 | Record-kind fold: `record_kinds` + **⊕ L35's refusal** · `issue`/`petition` bodies · two matrix rows + two `World` dicts deleted · `invariants.py:72` edited · the deposit rule | **L** | 2a | LB-5 | a season log showing a `content:dispensation` claim in the issuer's ledger; the ⊕ L35 refusal test | `create_record kind: text` deposits a claim with an **empty** value | **YES** | **15** |
| 6 | `give` verb + body + `_req_give` + the release-before-mint rule (⊕ R14) | M | 5 | LB-6 | a three-season trace: issue → carry → give → claim | a non-co-located `give` is refused; a `give` without release leaves two holders (must fail) | **YES** | **16** |
| 7 | content-claim operands: `_derive_operand` reads `to`/`amount`/`kind`/`at`; Q2's third clause | M | 5, 6 | LB-7 | `probes` on the corpus: Candidates with writ-derived operands > 0 | a person **not** named in the writ, same world, is not asked | no | 19 |
| 8 | `tell` at `Partial` deposits a lossy copy | S | 5 | LB-8 | `Full` → identical value; `Partial` → one omitted `to` key or one drifted operand | **the teller's own ledger is byte-identical** — RR-P's test as an assertion | no | fix |
| 9 | `_ch_post_remit` → obligees co-located, minting `inferred`; `oblige` body + `_req_oblige` reading `binds`; `establishment_of` rewritten **with this as its caller**; `Office.establishment` + its matrix row + `establish`'s `writes:` entry deleted | M | 1 | LB-9 | corpus claim-source histogram: `inferred` **0 → N** (MEASURED 0 today) | an obligee **elsewhere** does not witness | **YES** | 19 / fix |
| 10 | `offices.yaml` · bases as rostered values · `_req_confer`/`_req_revoke` rewritten **with the three-conjunct `holdings` rule** · four title helpers + `is_title` + the `titles` roster deleted · the title-in-a-body refusal re-expressed · holders seated · purview as `({seat.rung} ∪ descendants(...)) \ {the seat exercised}` (§A.1.6 (c)) · ⊕ S15's build assertion | **L** | **4, 16** ⚠ | LB-10a, **LB-10b**, LB-2e, **LB-10c** | `resolvable_verbs()` and `corpus_run`'s `VERBS ONLY REFUSED` line both change, quoted in the commit | today's 19-of-19 refusals; and `grep title_domain engine/season` = 0 | no | 6 (rides) |
| 11 | commission Record on `confer`; person-side `remit:` via the claim | M | 5, 10 | LB-11 | the H-71 test goes **RED** and is rewritten to assert the claim | a revoked holder still believes and the world still refuses — **two** assertions | **YES** | 19 |
| 12 | `works` kind; `_eff_work` advances `stage`; `restore` body; `found` verb + body; `(Rung, exists)`/`(Site, exists)` get a producer | **L** | 5 | LB-12 | `census` shows one more rung; a Site's condition rises | a `text` Record is **not** advanced by `work` | **YES** | 7 / 24 |
| 13 | RR-A's four verb deletions + `remit_acts.dispatch` + ⊕ L33 | S | **RR-A** | LB-13 | the loader's row count 35; `resolvable_verbs()` loses `dispatch` | no test references the four | no | **19b (deleted)** |
| 14 | the **13** field deletions (§A.1.1 (e)) + `judging_set` + `conferral_path` + ⊕ L40's coupling | S | 9, 10 | LB-14 | `matrix_rows_without_a_field`'s report line, before and after | `pytest tests/valoria -q -n auto` green | no | fix |
| 15 | `Act.via` + F3 | **L** | positions 3–5 | position 6's own | as `_part2.md` position 6 states | — | **the gate** | **6** |
| 16 | `add_tenure`'s hold-object guard (⊕ R13) + the 16 faction holds re-homed to persons | S | — ⚠ **moved BEFORE 10** | LB-16 | `Tenure(..., "fac_x", "terr_y", "hold")` raises; `build_realm` builds with **0** faction-subject holds | today's 16 | no | 12 |

> ### RULED: ⚠⚠ **ITEM 10 DEPENDS ON ITEM 16, WHICH IS THE OPPOSITE OF THE PLAN'S ORDER, AND THE REASON IS MEASURED: `revocation: "holdings"` IS UNSATISFIABLE ON A WORLD THAT RUNS.**
> ~~item 16 depends on item 10~~ → **item 10 depends on item 16.** Reported by
> `03_SEATS_AND_CONTENT.md` and re-measured here on `build_realm(0)`:
> ```
> hold Tenures by (subject class, object class):
>   {('person', 'Office'): 19, ('NON-person', 'Rung'): 16}
> in_holdings(w, p, r) true for ANY person over ANY rung:  False
> ```
> **All 19 person-subject holds are on OFFICES and all 16 rung-holds are FACTION-subject**, so
> `in_holdings` (`predicates.py:60-90`, *"a `hold` Tenure whose object is a RUNG"*) is **false for
> every person over every rung in the world.** A seat whose `revocation` is `"holdings"` therefore
> refuses **every** revocation, forever, and would look exactly like a working precondition.
>
> **So item 16 is not a tidy-up that follows the seat work; it is the precondition of the seat
> work's most important branch.** Landing item 10 first ships a row that cannot execute when
> reached — which is the shape §0.2 exists to catch, arriving through an order rather than through a
> document. **Item 16 moves ahead of item 10 and depends on nothing** (⊕ R13's guard plus a
> `populated.py` re-home, **S**) — so the dependency edge `10 → 16` costs the order nothing and buys
> the difference between a branch that refuses for a reason and a branch that refuses always.
>
> **Falsifier LB-10c:** `test_a_titled_seat_is_revocable_only_by_a_holder_of_its_domain` — it must
> fail before item 16 (nobody holds any rung) and pass after. ⚠ **And it must ASSERT that it
> asserted** (§0.1 pt 2): a test that iterates candidate revokers and finds none is indistinguishable
> from a test whose loop body never ran.

**THE FIRST DAY: items 1, 2a, 3a, 3b, 4** — five commits, each with a running season and a census,
a question histogram or a budget histogram, **and none of the five needing a ruling.** ⚠ **Item 16 is
the sixth cheapest and it is now a PRECONDITION rather than a follow-up** (see the ruling above): it
is **S**, depends on nothing, and without it item 10's `revocation: "holdings"` branch cannot fire on
any world that runs. **Blocked on a ruling:** 13 (RR-A). **Blocked on
positions 3–5:** 15. Everything else builds ahead of the Arc-2 gate under RR-C and is re-run after
G4. ⚠ **Nothing in this table marks a juncture done** (§0.2); a juncture is done when something runs
it and prints.

## A.5 · THE VERIFICATION CADENCE — stated because a reader of a build order is exactly the person about to get this wrong

`CLAUDE.md` §0.4, ruled: the full suite is a **CLOSE step, not an inner loop.**

| when | what |
|---|---|
| after **this commit's last** edit, immediately before the commit | `python -m pytest tests/valoria -q -n auto` — **once per commit**, ~2m36s. Serial it is 9m01s for the identical 1817 tests |
| mid-session, after an edit | `python -m pytest tests/valoria/test_<the one file>.py -q` — seconds |
| a red close run | re-run **the failing file only** while you fix it; the full suite comes back once, when you believe you are done |
| anywhere, freely | `python tools/valoria_local.py --staged` — it does **not** run pytest and never has, so local-green ≠ CI-green |

**This governs every pytest gate.** `engine/season/tests` takes the same cadence. **Items 1–14 and 16
all touch `engine/season/`, so they need `engine/season/tests`; none of them can reach
`engine/tests`** — "run everything just in case" is the habit §0.4 exists to end.

**Two container facts, so nobody debugs their clone.** A **shallow** checkout cannot reach the commits
`FORK:` rows name, so `tests/valoria/test_forked_status.py` fails two tests on arrival —
`cat .git/shallow` settles it (**this checkout IS shallow**, verified 2026-09-17). And
`engine/season/requirements.yaml` carries mutually inconsistent R3 figures: **re-run, never quote.**
The baseline this session measured: `python -m engine.season.harness.register --requirements` →
**met 1 · not_met 4 (R-01 R-02 R-04 R-05) · partial 4**; `python tools/m1_acceptance.py --summary` →
**verdict NOT MET, 1 row failing (row 4, which says DOC-DERIVED in its own detail)**.

---

# PART B · WHAT THIS ADDS AND WHAT IT MAKES UNNECESSARY

The bar is `ARCH` PART D row 1 / `AX` ID-13 — **a dead carrier is refused, so every addition owes a
reader and a removal.**

## B.1 · Adds — every one with its reader, on the day it lands

| added | its reader, on day one | new primitive? |
|---|---|---|
| `reach(w, p)` | `questions_for`'s Q2 test | no — `descendants` `:54` and `parent_of` `:48` exist |
| `nearest_store(w, rung, kind)` | `matter.py`'s larder loop | no — `parent_of` |
| `place_of(w, x)` | Q2's second clause, `_ch_co_located`, `_crossings` | **moved**, not added |
| `give` + body + `_req_give` | item 6's trace; the H-84 hole names the verb | no new row/form/operand/stem |
| `found` + body | `(Rung, exists)` and `(Site, exists)`, two live rows with **0** producers | no — round one loaded the row against the real loaders, green |
| `commit` body | Q4 `need`, **81 questions already** | no |
| `oblige` body + `_req_oblige` | `establishment_of`, itself read by `_ch_post_remit` (item 9) | no |
| `issue` / `petition` bodies | the deposit rule → a `content:` claim → Q2 | no |
| `restore` body | `(Site, condition)`, and `work`'s 723 corpus refusals | no |
| `record_kinds` + ⊕ L35 | the loader; `_derive_operand`'s key reads | one roster, and it is **⊕ S12**'s answer |
| `conferral_bases` / `revocation_bases` | `_req_confer` / `_req_revoke` | two rosters replacing **four helpers and a branch** |
| `binds_bases` | `_req_oblige` | one roster that **converts a dead field into a live one** (§A.1.5 (b)) |
| the deposit rule | Q2, with **no extension** — a held Record is in `mine(p)` | one branch |
| `World.remove_person` | MATTER **and** `_eff_kill` | **factored**, not added |
| `_crossings` | sites **and** persons | **factored**, not added |

## B.2 · Makes unnecessary — the free cuts, each at zero cost to anything that runs

| what dies | because | what it cost to run today |
|---|---|---|
| `w.crossings` | the crossing Event carries the same fact and is already witnessed | one `World` attribute, two probe readers |
| `date_due`, `band_crossed` | **0 questions each, MEASURED** | two roster members, two producers, a dead guard, a dead id search |
| `comply`, `evade / defy`, `refract` | all three **NOT resolvable**; `H-36` is ruled receiver-side | nothing |
| `levy` | `holonic §37.3` row 2 forbids the shape; **NOT resolvable** | nothing |
| the four title helpers + `is_title` | two rostered values plus `rung_kinds`'s existing ordinal | five call sites in three files |
| `judging_set`, `conferral_path` | one raises, one has **0 callers** | two probe calls |
| the 14 fields | **0 production readers each**, measured one at a time | nothing |
| `budget_office_bonus` | `H-92`'s first consumer; 0 of 143 cases seat an office | nothing |
| `w.dispensations`, `w.petitions` | `ARCH §B.5`'s ratified synthesis call folds both into `Record` | `invariants.py:72`'s entity set |

## B.3 · Disqualified as cuts — say so, because each looks like one

| looks cuttable | **KEEP**, and why |
|---|---|
| `Rung.envelope` | P2's carrier and **`ED-SE-0051`'s subject** (RR-2). Nothing here decides the demographic bound |
| `Office.binds` | ratified `Seat :=` **and** `ARCH F.17`'s named operand (§A.1.5 (b)) |
| `wear_per_season.body: 10` | **L29 forces it** — every `site_kinds` member needs a rate. It is unread and must stay unread; a body does not wear on a clock |
| `Office.body`, `Office.faction` | `office_faction` refuses an office belonging to nothing (`carriers.py:534-544`) — Jordan, 2026-09-02: *"Wouldn't it just imply that we don't have enough factions?"* |
| `Record.matured` | **RULED BY JORDAN 2026-09-10** — *"add `Record.matured`, write it at MATTER"* |
| `Tenure.degree` | in the ratified `Tenure :=`; `H-36`-adjacent and not this suite's |
| `_ch_chronicle`, `witness_key` | `ARCH §C.6`'s ratified mint table has a row for each |
| the `establishment_of` Query | **only** if item 9 lands as its caller; otherwise delete it (§A.1.5 (d)) |

## B.4 · WHAT NOT TO BUILD — `CLAUDE.md` §0.1 pt 5's predicate, applied

> *A pattern defect earns a guard only if the defective artifact is load-bearing on **the game**, the
> **exported params**, the **port**, or the **`needs_jordan` queue**. A pattern defect in an artifact
> load-bearing only on this repository's process is not evidence the artifact needs a guard; it is
> evidence the artifact can be wrong without cost.*

| tempting | **FORBIDDEN**, and why |
|---|---|
| a guard that every `[RES]` row has a producing verb (invariant 2 / **S3**) | its subject is `write_matrix.yaml`, a process artifact — and the design **needs** five rows producerless (`H-62`). `rows_without_a_producer`'s own docstring: *"a gap in Part E, not a reason to delete a row #353 mandates."* Add the producer or leave the report a report |
| a guard over unknown verb-table columns (invariant 10 / **S1**) | its subject is the loader. If a column matters, give it a **reader** — an unread column is ID-13 and no checker fixes that |
| **a checker that this file's net is still −17** | its subject is this document. A ledger that grades itself is `CLAUDE.md` §0.3's loop with arithmetic |
| **a freshness checker over `hole_register.yaml`, or a coverage grader over §C.5's closure list** | the register has `register.py --check`; a second instrument over it is the same loop |
| a cadence checker, or a citation checker | §0.4 and §0.1 pt 3 both say in terms that their subject is a reader's discipline and **no guard may be built** |
| a `governance_modes` / `power_bases` roster | **both were BUILT AND DELETED**: *"They were not wrong; they were UNREAD"* |
| a second band table for a non-site quantity | **PLANT 1 refuses it at load**, and `band_floors["body"]` already exists |
| `population()` / `faction_value()` / `character()` with no consumer | a Query with no consumer is a false N-line. **`conferral_path` and `establishment_of` are what that looks like after eighteen months** |
| `raze` / `build` / `repair` / `convert` / `garrison` as verbs | `restore` + `found` + one Record kind cover them |
| a latency, distance or speed parameter on the writ | `02` forbids it by construction; **speed is not an axis, control is** |
| an `.audit/` file, or a findings document from the adversarial pass | §0 retires `.audit/` as a category (~~`audit/`~~ — renamed 2026-09-16, ED-IN-0231) |

**And what IS licensed, so the predicate does not read as a ban.** ⊕ L35's loader refusal (subject: a
writ a player wrote) · item 7's operand branch with its falsifier (subject: whether an executor is
ever asked) · ⊕ S15's build-time rung assertion (subject: whether a duke has purview) · ⊕ R13's
hold-object conjunct (subject: whether a book can be revoked like an office) ·
`Person.body`'s one-key addition to `test_morale_write_sweep.py`'s `_CELL_OWNED` registry · and the
planted-violation suite for §B.13's five unbuilt invariants, **which ratified position 23 already
schedules and this suite must not pre-empt.**

⚠ **The reroute to watch.** Forbid the guard and a session writes **a finding** instead, because the
carrier is prose. Nothing in §B.4 is a thing to *file*. If work on these subjects finds a defect
outside its own load-bearing path: **fix it in that commit, or drop it.**

---
# PART C · THE THREE QUESTIONS, THE GRADE, AND THE RULING LEDGER

## C.1 · Who owns this?

| the thing | owner |
|---|---|
| **the object COUNT across this suite** | **§A.1 of this file.** `01`–`04` point here and state no net of their own. §A.1.6 reconciles the schemes |
| **the ORDER across this suite** | **§A.4 of this file** |
| the ORDER across all lanes | `workplans/2026-09-11-reconciled-program.md` §3, **RATIFIED 2026-09-12 (ED-IN-0215)**, scoped to §3's order and §1's supersession verdict and nothing else. This file **places items into** that order and **departs from it** — RR-C |
| the gate's F3 branch, `Act.via`, the purview readers' re-pointing | **ratified position 6, exclusively** |
| the effect contract | **ratified position 7** |
| the closed sets | `engine/season/rosters.yaml`, read at runtime — mechanism under §0.05 |
| the write schema | `engine/season/write_matrix.yaml`, one row per `(kind, field)` (L23) |
| the containment ladder | `World.contain_ascends` (`state/world.py:197`), single owner |
| the seven precondition forms | `rosters.yaml`, **closed at seven**, refusing an eighth at load (L1) |
| the person's body bands | `band_floors["body"]` + `body_band_penalty` (`decision/budget.py:63-75`), **already the single owner** |
| the tenure cascade on a death | `_eff_kill` today; `World.remove_person` after item 3b, **one site** (LB-3c) |
| this file | **nobody, after it is read.** It is reference (§0.05): delete it and the game behaves identically |

## C.2 · What can check this?

| claim | grade | the construction |
|---|---|---|
| an eighth `requires` form cannot ship | **STRUCTURAL** | `data/requires.py:549-554`, at load, independent of the roster |
| `capability` never gates a verb | **STRUCTURAL** | `data/verbs.py:311-315`, **by name**, even if rostered |
| a matrix row and its `writes:` entries move together | **MECHANICAL** | L11, **EXECUTED: PLANT 2** |
| a second band table cannot ship | **MECHANICAL** | L28, **EXECUTED: PLANT 1** |
| a `hold` never reaches a `Site` | **NOTHING today**; MECHANICAL after item 16 | `add_tenure` checks kind and `contain` direction only (`world.py:242-256`) |
| a `Record`'s `subject_matter` matches its kind | **NOTHING today** (⊕ S12); MECHANICAL after ⊕ L35 | the refusal shape to copy is `Rung.__setattr__` (`carriers.py:589-596`) |
| a `content:` claim produces an operand | **NOTHING today** (⊕ S14); MECHANICAL after item 7 | one branch in `_derive_operand` |
| every seat's `rung` exists | **NOTHING today** (⊕ S15); MECHANICAL after item 10 | one build-time assertion |
| `Person.body`'s writers are the cell's owners | **MECHANICAL, and it is free** | one key in `tests/valoria/test_morale_write_sweep.py`'s `_CELL_OWNED` |
| a new `[RES]` row has a producer | **CONVENTION — report-only** (S3) | `rows_without_a_producer`'s only caller asserts the shape |
| an unknown verb-table column is refused | **NOTHING** — invariant 10 is unbuilt (S1) | give the column a reader instead |
| `decision/` sees no World | **STRUCTURAL by path** | `ARCH §C.3`, plus the AST test `test_w5_sense_is_still_the_only_world_taking_non_decision_function` |
| the net is −17 | **CONVENTION, and no guard is permitted** (§B.4) | the rows of §A.1, each with a path. Re-run the greps |
| the cadence is followed | **CONVENTION, and no guard is permitted** | §0.4's own sentence: *"the enforcement is that you read it"* |

## C.3 · Whose act makes it happen?

| step | whose act |
|---|---|
| items 1, 2a, 3a, 4 | a session's, one commit each, **no ruling needed** |
| item 2b's golden re-record | a session's, **declared in the commit message** (`CLAUDE.md` §7) |
| items 5, 6, 7, 9, 11, 12 | a session's, **ahead of the Arc-2 gate under RR-C** — and again after G4, as a re-run |
| item 10's departure from `ARCH §B.7`'s `Seat :=` | **Jordan's** — RR-B |
| item 13 | **Jordan's** — RR-A. Nothing else is blocked on it |
| item 15 | ratified position 6's, unchanged in content |
| whether §A.4's order may run at all | **Jordan's** — RR-C |
| the principle behind all of it | **Jordan's** — RR-P, owned by `02` |
| ratification of anything in this directory | **Jordan's, and not by merging it.** Every file here is held back in full |

## C.4 · THE RULING REQUESTS — through `CLAUDE.md` §0's five-step gate

Each candidate ran **Superseded → Irrelevant → Answered by a design document → Answered by precedent
→ Answered by what makes sense for the architecture.** The step that answered it is named. **Only
survivors reach Jordan**, and the standing queue is cleared in §C.5.

### Surviving from round one — 2

- **RR-2 · `ED-SE-0051`, the demographic bound: matter only, or matter plus hearth capacity.**
  **OPEN, untouched, NOT GATING.** `registers/editorial_ledger_se.jsonl:51`, minted 2026-09-10,
  `status: open`, `needs_jordan: true`. Nothing in `01`–`04` decides it; `Rung.envelope` is kept as
  its carrier (§B.3). **Step 5 cannot take it** — the two arms are materially different games.
  ⚠ `ED-WR-0011` says the two must be answered together: *"Answering them in either order separately
  risks two rulings that do not compose."* **It gates no item in §A.4.**
- **RR-3 · the zoom-trigger table on `scale_transitions_v30.md`'s `CANONICAL` line.** **SURVIVES as
  `03_THE_SURFACE.md` states it, and it is still the weakest of all six**, because that file carries
  a second, different `## Status:` line, sits in a retire set, and holds **zero `.py`** — so under
  §0.05 it binds nothing at runtime. Unchanged by this round. **It gates no item in §A.4.**

### Closed from round one — 1

- **RR-1 · policy collision on the same `(rung, clause)`: nearness or rank?**
  **CLOSED at step 2 — IRRELEVANT.** There is no `in_force` walk and no place-keyed clause left to
  collide: `01`'s Q-shape and `02`'s two channels make a policy **a Record held by a person and a
  claim in a ledger**, so two writs naming the same executor are **two content claims in one
  ledger**, and `agreement` (`decision/options.py:412`) already scores told-against-own. **The
  collision is the executor's and is resolved by his act.** Round one graded this its most expensive
  open ruling and gave it a feel-of-the-game table; **the design deleted the question rather than
  answering it**, which is the outcome §0's gate exists to find. Its `needs_jordan` row on
  `ED-IN-0236` closes with this citation.

### NEW — 4

#### RR-P · the principle, as a candidate `AX-7` — **owned by `02`, cross-referenced here**

**Jordan, verbatim:** *"the player must have the sanctity of their choices/actions/decisions
preserved in terms of the contents of those choices/actions/decisions themselves — the worldly churn
is in how those contents are received and acted upon by others."* The test: **a draw may decide what
HAPPENS, never what you MEANT.**

**Survives all five steps.** It is axiom-shaped — a candidate seventh beside the six at
`AX-1`..`AX-6` (`architecture/meta/01_AXIOMS.md`, *"There are SIX"*) — no design document states it,
and it would bind every subsystem. **Its home in code already exists and this file's only
contribution is to name the two halves:** the `Act` dataclass (`carriers.py:332-365`, `payload`
`:339`) is the actor's content, and `write_matrix.yaml:72-78`'s `(Act[], returned)` row is
`steps: [DEL]` with `by: "DELIBERATE writes nothing else"`; the `Claim` dataclass
(`carriers.py:129-156`) is a witness's reception. **The split exists; the principle names it and
forbids a bridge from `Claim` back into `Act`.**

> ### RULED: **RR-P's SUBSTANCE HAS ONE PRECEDENT AND ITS GENERALITY HAS NONE — WHICH IS EXACTLY WHY IT STILL REACHES JORDAN.**
> Step 4 is not silent. **`H-36` (`hole_register.yaml:394`, `grade: ruled`) is Jordan on
> 2026-09-02:** *"RECEIVER-SIDE. ⚠ AN EMISSION IS NEVER DISTORTED … what refracts is the PREMISES
> AND RATIONALE, minted per receiver as a Claim."* That is RR-P's test, ruled, **for one verb.** A
> precedent about `refract` is not an axiom about every subsystem, so step 4 narrows the request
> without closing it: **what reaches Jordan is the GENERALISATION, and the evidence that he has
> already taken the specific case the same way.** Every proposal that leans on the principle says
> *"under RR-P"*.

#### RR-A · fold the response verbs — **delete `comply`, `evade / defy`, `refract`, `dispatch` and `remit_acts.dispatch`**

**Why it reaches Jordan: `ED-IN-0210` (`registers/editorial_ledger_in.jsonl:104`, ruled 2026-09-15)
REJECTED the "no response verb" option by name.** Verbatim: *"Asked as an either/or — 'Does an order
(`dispatch`) carry terms like a Dispensation (`issue`), so `comply`/`evade`/`refract` answer both —
or does a dispatched order need no response verb at all?' — answered 'yes, I think that makes most
sense.' … AN ORDER CARRIES TERMS LIKE A DISPENSATION, and `comply`/`evade`/`refract` answer both.
The second option (no response verb) is REJECTED."*

**Step 1 does not close it** (nothing supersedes 0210). **Step 5 may not overwrite a ruling.** So it
survives — but the question must be put *precisely*, and the plan put it too broadly.

> ### RULED: **THE FOLD EXECUTES ED-IN-0210's FIRST HALF AND CONTESTS ONLY ITS SECOND. THAT IS THE QUESTION, AND IT IS NARROWER THAN "MAY WE DELETE FOUR ROWS".**
> **What the design AGREES with, and builds:** *"an order carries terms like a dispensation"* — `02`
> makes both one `Record` kind with one `subject_matter` schema, which is 0210's own stated unblock:
> *"the nine dispensation terms Layer 1 records as an absence (04:1077) become the shared shape."*
> And *"`dispatch` at person scale is `issue` with a person-scale referent"* is exactly `02`'s
> `issue` whose `to` names one person, plus a `give` to deliver it.
>
> **What it contests, in one sentence to Jordan:** *is `commit` (the oath), `repudiate` (the refusal)
> and the named act itself (the compliance) a response verb — or does the ruling require the three
> rows to exist?* If the former, the ruling's substance holds and the rows are redundant. If the
> latter, item 13 does not land and the four rows stay, at a cost of **4 objects** on §A.1's ledger
> (net −17 → −13) and no other change: **RR-A blocks item 13 and nothing else.**
>
> **`refract` is the strongest half of the request and it should be read first:** deleting the row
> **executes** `H-36`'s ruled receiver-side mechanism as `02`'s lossy `tell`, rather than discarding
> it. **MEASURED: three of the four rows are NOT resolvable and `dispatch` is the only live one**
> (§A.1.1 (a)), so the behavioural cost of the fold is one verb whose `writes:` is `[]`.
>
> **`levy` is NOT part of RR-A.** It closes at **step 5**: `holonic §37.3` forbids *"applying a
> dispensation as a state write"* and *"a `scope` that enumerates places"*, and `levy` is both — a
> lord's hand in a larder with nobody in between, declared `grade: assumption` with an
> `eligibility_substitution` its own cell calls an off-register fill. Deleted without a ruling.

#### RR-B · Layer-1 text — **EIGHT sentences in RATIFIED `architecture/` that this design makes false, one of which is a GAME change and not a text change**

**Reaches Jordan because `architecture/` is RATIFIED (ED-IN-0204, *"adopt in full"*) and step 5 may
not overwrite ratified canon.** ⚠ **The plan listed four limbs. There are eight, and three of the
plan's four were mis-stated.** Limbs **B-6**, **B-7** and **B-8** were found by this round's authors
and none of them is in the plan; **B-8 is `03`'s own RR-B.2** and is the only limb whose cost is paid
by the *game* rather than by a sentence. Each is quoted at its `§` and **not edited by this suite.**

| # | ratified sentence | what becomes false | status |
|---|---|---|---|
| **B-1** | `ARCH §B.7`: `Seat := ( id, post, body?, scope? (null = a cluster), remit(acts[], binds), conferral, revocation, upkeep, dates[], exists )` | **Four of the ten fields go or change:** `scope?` deleted, `upkeep` deleted, `dates[]` deleted, and `scope? (null = a cluster)`'s **null case is abolished** because every seat gets a `rung`. `binds` is **retained** (§A.1.5 (b)) | **LIVE** |
| **B-2** | `ARCH §B.7`: `conferral -- which ACT fills it: confer by <seat> \| determine by <judging seats> \| succeed` | The design makes `conferral` a **bare rostered token**, dropping the `by <seat>` / `by <judging seats>` **operand**. So `_req_confer` cannot ask *which* seat confers and falls back to purview — a **different rule** from the ratified one | **LIVE, and the plan does not name it** |
| **B-3** | `ARCH §B.7`: `revocation -- which seat may revoke, and the CONJUNCTS` | The design makes `revocation` a **basis name**, dropping the *"which seat"* half. ⚠ **The CONJUNCTS half is NOT contested** — §A.3.5 restores all three (purview + holdings + higher rank) exactly as §B.7 call 1 spells them | **LIVE, narrowed** |
| **B-4** | `ARCH §B.8`: `term? (matures_at, declared_by : ActId, closer) -- T-n. Replaces payload?` | ⚠ ~~*The `Tenure :=` line becomes false*~~ → **it does NOT. §B.8 PRESCRIBES the deletion** (*"Replaces payload?"*), and this suite executes **half** of it: `payload` goes, `term?` does not arrive. **Half-satisfied, not falsified** — `term?` is ratified positions 6/20's | ⚠ **DOWNGRADED by this file** |
| **B-5** | `ARCH §C.6`'s mint table: `document_key \| the change claims only. No attribution` | The **document-content deposit rule** is a mint the table does not have — a sixth cell. ⚠ And the table's `post_remit \| the change claims, inferred` row is **CONFORMED to**, not contested: item 9 implements a ratified row that has no writer | **LIVE — the one genuinely new mint** |
| **B-6** | `holonic §37.1`: *"A published dispensation does not apply — it lands as a compliance contest, per relevant Rung, through `contest`"* | `02` makes compliance **the executor's own act** (`transfer` / `commit` / `repudiate`), with **seizure as a declared LIMIT** needing a contest no provider supplies. **The `contest` route is not built** | ⚠ **LIVE, and the plan does not name it** |
| **B-7** | `holonic §37.3` row 3: a `scope` that enumerates places would delete *"office-clusters with `rung? = null`, which have no place"* | Giving every seat a `rung` **abolishes the cluster case §37.3 protects**, and **narrows** `ARCH F.21` (*"the rank of a cluster seat (`scope = null`): no rank; the loader forbids a `higher_rank` conjunct on one"*) by making its subject non-existent while leaving its remedy unwritten | ⚠ **LIVE, and the plan does not name it** |
| **B-8** | `ARCH §B.7` call 1: *"a title needing purview + **higher rank**"*, as enforced today by `highest_title_rank(actor) <= title_rank(target)` (`predicates.py:270`) | `03` derives the rank conjunct from **`World.contain_ascends`** rather than from a `rung_kinds` ordinal — strictly better as a mechanism (the ordinal is **S9**), and it buys **one behaviour change: a lower seat that holds the land may now unmake the seat above it.** The conjunct survives; **who it admits changes** | ⚠ **LIVE — `03`'s RR-B.2, and it is a GAME change rather than a text change** |

> ### RULED: **RR-B IS NOT SOFTENED, AND IT IS NOT ASSUMED EITHER. THE CHOICE IS JORDAN'S AND BOTH BRANCHES ARE COSTED.**
> ~~`ARCH §B.7`'s Seat fields, `§B.8`'s Tenure fields, the "nine typed terms" line, `§C.6`'s mint
> table~~ → **B-1, B-2, B-3, B-5, B-6, B-7, B-8 are live; B-4 is half-satisfied rather than
> falsified; and the *"nine typed terms"* limb is WITHDRAWN.**
>
> **Why the nine-terms limb is withdrawn — opened and read.** `ARCH F.15` files the downward
> mechanism as *"the nine dispensation terms (§B.5) — 'nine typed terms' and nothing lists them | a
> schema for one Record kind, **unspecified** | not an assumption so much as an **absence**: the
> entire downward mechanism has no executable content, and `issue` produces a document nobody can
> comply with."* And `ARCH §B.5`'s synthesis call: *"**Petition and Dispensation become Record
> kinds** … **Cost:** the nine typed dispensation terms become a schema for one Record kind and
> remain unspecified."* **`record_kinds` SUPPLIES the schema §B.5 says remains unspecified and folds
> exactly the two types §B.5 says to fold.** That is conformance, not contradiction; what changes is
> **F.15's grade**, from an absence to a specified schema. **A proposal that counted this as an
> overwritten ratified sentence would have been claiming a conflict it does not have** — the mirror
> of the error RR-B exists to avoid.
>
> **Two branches, and the amendment is NOT assumed:**
> **(i) AMEND `architecture/`** — six sentences, a `## Status:` amendment line and a ledger row. This
> is what `ARCH` itself did three times in its own header (*"AMENDED 2026-09-03 (Jordan-directed)"*,
> *"REV. 3"*), so the mechanism exists.
> **(ii) NARROW THE DESIGN** — keep `scope?`/`upkeep`/`dates[]` as declared-unread fields (**+3
> objects**, net −17 → −14), keep the cluster case (**item 10 becomes L+**, and `ARCH F.21`'s
> loader-forbidden `higher_rank` conjunct must then be written), carry `conferral`'s operand (**+1
> object and a new operand — which `requires_operands` refuses at load, L3, so it is a design
> change**), and build the compliance contest (**a contest provider, which `03`/`04` both grade as
> ABSENT**).
>
> ⚠ **B-6 is the expensive one and it is the one the plan missed.** Branch (ii) on B-6 alone is a
> whole subsystem: `holonic §37.1`'s *"compliance contest, per relevant Rung, through `contest`"*
> needs a prize in `contest_subsystems.prizes` with a registered `provider:` — and **R3/R4 say a
> prize with a `module:` and no `provider:` is SILENTLY DROPPED from `resolvable_verbs()`**, which is
> how `capture` dies today. So branch (ii) is not "write the sentence back in"; it is
> position 22 (PROC-B). **Stated at full cost rather than at the cost that makes the design look
> cheap.**

#### RR-C · sequencing — **§A.4 departs from the RATIFIED order, and it does more than re-order**

**Reaches Jordan because `workplans/2026-09-11-reconciled-program.md:3` is RATIFIED 2026-09-12
(ED-IN-0215), scoped to *"§3's ORDER and §1's supersession verdict"*, and step 5 cannot re-order a
ratified order.** ⚠ **Three limbs, and the plan named one.**

| # | the departure | the ratified text |
|---|---|---|
| **C-1** | §A.4 puts items 1, 5, 6, 9, 11, 12 — **six effect bodies** — AHEAD of positions 3–7, the Arc-2 gate | positions 3–7 are `G1a G1b G2 G3 G4`; position 7 is *"`NoOpReceipt`; the effect contract finalised; **11 effects rewritten once**"*. Building ahead makes it 18 |
| **C-2** | **Item 13 DELETES position 19b in its entirety** | position 19b: *"**U7-disp** \| IN \| `comply`, `evade / defy`, `refract` \| **ED-IN-0210**"*. There is nothing left of it after RR-A |
| **C-3** | **Item 1 and §A.1 delete `levy` from position 19's contents** | position 19: *"**U7-remit** \| IN \| **`levy`**, `establish`, `open_case`, `determine`, `issue`"*. `establish` also loses a third of its `writes:` (§A.1.1 (d)) |

> ### RULED: **THE REQUEST IS NARROWER THAN "MAY WE RE-ORDER" AND THE FIRST FIVE ITEMS DO NOT NEED IT.**
> **Items 2a, 2b, 3a, 3b, 4, 7, 8, 10, 14, 16 are order-free by §A.0.2's own test** — no
> `@effect_for` body, no Tenure written on another. So **four of the first five items need no part of
> RR-C** (item 1 is the exception, and it is one 12-line body whose re-run after G4 is a re-run of
> one test).
>
> **What genuinely needs the ruling is C-2 and C-3** — deleting content from two ratified positions —
> and both are consequences of RR-A and of `levy`'s step-5 closure rather than independent asks.
> **So RR-C reduces to: may a suite that deletes a ratified position's subject-matter record that by
> striking the position, or must the position be re-scoped by Jordan?** Answering *strike it* costs
> one line in `_part2.md`. Answering *re-scope* costs a ruling and blocks item 13.
>
> **The Arc-2 caveat, carried honestly and not buried:** **every one of this suite's seven effect
> bodies is Arc-2-flagged by the literal rule** (§A.0.2), the flag is real, and the cost of building
> ahead is **seven extra rewrites at position 7**. It is not a rewrite of the design — each flagged
> item's execution artifact is a test or a census, **re-runnable after G4**, so being wrong costs a
> re-run. That is the whole of the argument and it is Jordan's to reject.

## C.5 · CLOSED BY DESIGN — no ruling, with the closing mechanism named

Clearing the standing queue is session work (`CLAUDE.md` §0: *"find a stale `needs_jordan` on a
settled question and CLOSE it with its citation. Preserving a dead question is not conservatism; it
is how the queue formed"*). **This section is the suite's single owner of the closure list.**

| the row | verdict | the mechanism, named | §0 step |
|---|---|---|---|
| **`H-71`** (`hole_register.yaml:795`) — *"`remit:<act>` CANNOT be evaluated person-side. The person owns the `hold`; the OFFICE owns the remit"* | **CLOSED on BOTH sides** | `03`'s `commission` Record + the deposit rule give the person a `content:commission` claim naming a seat whose `remit_acts` include the act, so `person_side_eligible`'s decline (`options.py:163-165`) becomes a claim read; world-side `_eligible` keeps checking the actual hold. **They can disagree** — a revoked man still believes he may `issue` and the world refuses. Item 11, LB-11 | 5 |
| **`H-84`** (`:1000`) — *"no verb in the resolvable vocabulary moves a Record to another person"* | **CLOSED** | `give` (item 6). **Ratified position 16 is this verb** and chose its shape; this names it | 3 |
| **`H-92`** (`:1106-1108`) — two consumers of a `hold` on a Rung | **CLOSED, both** | consumer 1: `budget_office_bonus` deleted (item 4). Consumer 2: `document_key` reading `changes[]` **is the deposit rule's own channel** — the widened reading is what makes a writ's arrival witnessable, so it stops being a defect and becomes the mechanism | 5 |
| **`hole_register.yaml:176`** — the unspendable sixth scene | **CLOSED** | rides with item 4. Its own measurement: *"planting one live `hold` on `p_carin` moves her budget 5 → 6 and leaves the releasable count at 5"* | 5 |
| **`H-94`'s three rows** — operands the design names and never supplies | **CLOSED for `to`/`amount`/`kind`/`at`** | item 7: read from the `content:` claim's value. ⚠ **NOT closed for `from`**, which stays `containing_rung_of` (`options.py:316-317`) and is why office-holders must be SEATED (item 10) | 5 |
| **`H-109`** (`:1520`) — *"THERE IS AN `is_title` BRANCH … the meta-architecture makes the difference two VALUES of a seat's declared `revocation` basis instead of two code paths"* | **CLOSED exactly as the row asks** | item 10. **The row itself prescribes the fix**, so this is transcription, not design | 3 |
| **`H-110`** (`:1533`) — a band crossing's question throws away its Event id | **DISSOLVED, not fixed** | `01`'s Q3 fold makes the crossing a **claim**, so the referent is the claim and the site-use verb is read from its predicate. The row asked for a referent repair; the design removes the source that needed one | 2 |
| **`H-34`** (`:370`) — *"establishment size per office kind"* | **CLOSED BY DELETION** | `Office.establishment` goes (item 9). ⚠ **`ARCH §B.7` call 2 pre-authorises this**: *"**Rejected:** the chain's field, with *establishment size* as a number nobody can source"* | 3 |
| **`H-41`** (`:462`) — *"`(Rung, exists)`, `(Office, exists)`, `(Site, exists)` … Part D's existence rows cover ONLY `Person` and `Record`"* | **CLOSED, all three** | `(Office, exists)` already has `establish`; `(Rung, exists)` and `(Site, exists)` gain `found` (item 12). ⚠ **The plan merged H-34 and H-41 into one row; they are two holes with two mechanisms** | 5 |
| **`ARCH F.15`** — *"the entire downward mechanism has no executable content"* | **CLOSED** | `record_kinds`' `dispensation: [terms, to, at]` **is** the schema `§B.5` leaves unspecified; `give` delivers; the deposit rule makes it believed; item 7 makes it executable. **`ARCH §B.5` prescribes the fold, so this conforms** (RR-B, B-4's reasoning) | 3 |
| **`ARCH F.17`** — *"how a person joins an establishment"* | **CLOSED as F.17 states it** | `oblige` body + `_req_oblige` **reading `binds`** (item 9), which is F.17's own proposed resolution. **No sixth `remit_acts` member**, which is the ruling F.17 warns about | 3 |
| **`ARCH F.20`** — *"no stage names a verb that founds a hearth or builds a site … the world only decays"* | **CLOSED at step 5, and the tension is declared** | `found` + the `works` Record kind (item 12). ⚠ **F.20's own resolution column says *"the rows are dropped until a verb is ruled"*, so F.20 asks for a RULING.** Step 5 takes it because two live matrix rows have zero producers, `H-41` is registered, round one loaded the row against the real loaders green, and **no new row, form, operand, stem or roster is needed.** If Jordan wants the ruling, it is here and it is one word | 5 |


### Explicitly NOT closed, and said so

| the row | why not, in one line |
|---|---|
| **`ARCH F.18`** — upkeep's source | Deleting `Office.upkeep` **removes the carrier, not the gap.** F.18's own resolution is *"the repair is a verb"* and no verb is proposed, so *"no economic pressure on any office"* stands and becomes structural. ⚠ **And `upkeep` is in the ratified `Seat :=`** — RR-B limb B-1 |
| **`ARCH F.22`** — how succession fills a seat | ⚠ **DOWNGRADED FROM THE PLAN'S "CLOSED".** `conferral: "succeed"` correctly makes a seat un-conferrable and names the route, but **nothing fills it.** `succeed` (`verb_table.yaml:490`) writes `Tenure.since`, has **no `@effect_for` body** and is therefore **not resolvable** (measured); and `holonic §15`'s table makes a `succeed` Tenure **`Rung → Person`**, whose subject cannot act (`AX-1`), while `succeed`'s eligibility is `own`. **So the basis is declared and the filling act is not built.** `@effect_for("succeed")` is deliberately **not** added to §A.1.2 — adding it would make the closure claim true and the object count one worse, and the honest move is to claim neither |
| **`ARCH F.20a` / `H-62`** — no verb writes any `Person` interior field | `(Person, body)` is **not** one of F.20a's four (`convictions`, `stance[]`, `scar[axis]`, `axis_count[axis]`), so item 3b neither closes it nor touches it. **Producerless `[RES]` rows go 10 → 5 and the five are these** (§A.3.6). Ratified position 12 owns them |
| **`ARCH F.20b`** — the fold mints Event kinds no column declares | Untouched. Item 2b **adds** a declared emission and does not address the three body literals |
| **`ARCH F.16`** — what each witness channel mints | The deposit rule hardcodes its mint in a body; F.16's resolution is **a `mints:` column**, and the column is not built. **Item 9 conforms to §C.6's existing row; the deposit rule needs a new one** (RR-B, B-5) |
| **`ARCH F.21`** — *"the rank of a cluster seat (`scope = null`): no rank; the loader forbids a `higher_rank` conjunct on one"* | ⚠ **NARROWED, NOT CLOSED — corrected from this file's first draft and from the plan.** Giving every seat a `rung` removes the *cluster* case, but F.21's remedy (*"the loader forbids a `higher_rank` conjunct"*) is **not built**, and the rank conjunct is now **derived from containment** rather than refused. `03` files it as its **RR-B.2**; §C.4 carries it as **B-8**. **A hole whose subject is abolished and whose remedy is unwritten is narrowed, and calling that closed is the move `AUDIT_VERDICT.md` faulted round one for** |
| **`ARCH F.14`** — an Event's place | ⚠ **NOT CLOSED, AND `place_of` IS F.14's OWN FUNCTION BY NAME.** F.14: *"`place_of` — the scene's place, or the changed thing's rung \| **a plague is one Event spanning many rungs and has no single place; `place_of` must return a SET and my signature does not**."* This suite promotes `place_of` with the **`Optional[str]`** signature F.14 declares insufficient, and the case it cannot serve is live: `matter()`'s `actorless` channel (`matter.py:42-46`) is *"ONE Event spanning many rungs"* by its own comment. **Declared, not closed** |
| **`ARCH §B.7`'s `judging_set` replacement** | `judging_set` is deleted and *"the seats whose remit covers the matter at that venue"* is **not built.** Ratified position 18 (PROC-A) names `judging_set` in its own instruction and keeps it (§A.1.5 (e)) |
| **seizure / forced compliance** | Needs a contest between the lord's men and the holder, and **no provider supplies one** — R3/R4 drop such a prize silently. `02` states it as a LIMIT; **`levy` is deleted rather than kept as the broadcast it is** |
| **`Act.via`** | Ratified position 6's, exclusively. Until it lands, `issue`/`confer`/`revoke` resolve the seat from the actor's holds as `_eligible` does today (`resolve.py:52-57`) — which is a declared departure from `ARCH §B.7`'s MECHANICAL invariant *"purview is asked of the seat exercised, not the actor"* and from `§B.8`'s `T-o` path, *"exercised through `Act.via`"*. **Interim, named, with its retirement named** |
| **`ED-SE-0051`** | RR-2, open, untouched, not gating |
| **`H-54`** — question aggregation and the within-source tiebreak | The tiebreak stays a **content hash** (`world_q.py:544-547`: *"WHICH QUESTION A PERSON ANSWERS IS SETTLED BY LEXICOGRAPHIC ORDER OVER HASHES … MEASURED over 89 corpus baselines, the leading source is SHARED … in 801 of 1,068 deliberations"*). ⚠ **`01`'s fold makes this WORSE, not better**: with two sources instead of four, the roster's order decides less often and the hash decides more. **`H-54` closed at step 4 on its own precedent with `needs_jordan: false`, and this design does not reopen it — but it does increase the share of deliberations the hash settles, and that is stated rather than left for a later session to discover** |

---

# PART D · FALSIFIERS AND THE NERS PRE-COMMITMENT

## D.1 · This document's own claims, and what would show each wrong

| claim | what would show it wrong |
|---|---|
| **the net is −17** | Open any row of §A.1.1 and find a production reader the table says does not exist, or find a named object in §A.1.2 that already exists. **Each row names a path; re-run the grep.** One false row moves the net |
| the two deleted question sources produce 0 questions | `python3 -c "..."` in §A.1.1 (b) printing a `date_due` or `band_crossed` key |
| `band_floors.person` does not load | `_load_matter_tables()` returning without raising after the plant. **PLANT 1 is the artifact** |
| a matrix deletion and its `writes:` entry are one commit | reloading `data.verbs` with the row popped and getting no `SystemExit`. **PLANT 2 is the artifact** |
| `Person.body` already has a consumer | `body_band_penalty` returning 0 for every body value, or `budget` ignoring it. **The four-row ladder in §A.3.3 is the artifact** |
| `_event_place` returns `None` for a Record-subject Event | constructing such an Event and getting a rung id |
| `descendants` excludes its argument | `rung_id in descendants(w, rung_id)` being true for any rung |
| a `body`-kind Site is constructible | `headless.py:64` raising, or that line not saying `"body"` |
| `establishment_of` and `conferral_path` have no callers | any call site outside their own bodies |
| `dispatch` is the only resolvable row of RR-A's four | `resolvable_verbs()` containing `comply`, `evade / defy` or `refract` |
| **`ARCH §B.7` call 1 prescribes the three-conjunct `holdings` rule** | that sentence not reading *"a title needing purview + holdings + higher rank"* |
| **RR-B has eight limbs and the nine-terms limb is withdrawn** | `ARCH §B.5` or `F.15` asserting that a schema **must not** be supplied |
| the first five items need no ruling | any of items 1, 2a, 2b, 3a, 3b, 4 requiring an `architecture/` amendment, a roster ruling, or `ED-SE-0051` |

## D.2 · Falsifiers this file predicts will FIRE

| it fires | and that is the point |
|---|---|
| the **H-71 person-side decline test** goes RED at item 11 | the decline is the defect; the commit that lands item 11 rewrites the test as its own control |
| `probes.py:1376`'s `assert off.establishment == []` goes RED at item 9 | the field is gone |
| `probes.py:1208` and `:2467` break at item 14 | `judging_set` is gone; they must be re-pointed or dropped in that commit |
| `test_the_entity_set_covers_every_world_collection_a_tenure_can_name` goes RED at item 5 | `invariants.py:72` lost two members; **the test is the evidence it was edited** |
| `test_w5_q_has_a_producer_across_all_four_sources` **stays GREEN and its name goes false** at item 2a | the loop adapts and the name does not. **LB-2d renames it** |
| every golden through CALENDAR and MATTER re-records | **declared in the commit message**, items 2b and 3a/3b |
| `census` counts change at items 3a, 3b, 10, 12, 16 | **declared re-record**; the before/after delta is the artifact |

## D.3 · THE NERS PRE-COMMITMENT

Per `CLAUDE.md` §0.06 and `skills/ners/SKILL.md`: **a PASS is licensed by a NAMED FAILED ATTACK, not
by an absent finding; withholding is symmetric; E is scored LAST as a ratio; the pass fires on
itself.** This is the pre-commitment, written **before** the pass, so a later pass cannot be graded
against criteria chosen after its findings.

### N — the N-lines, each with the cut that would show it false

| N-line | cut it, and: |
|---|---|
| `reach` | the purview defect returns — a duke is asked only about what is in his own hand. **MEASURED baseline: 16 of 19 seats have `rung is None`, so 16 of 19 have no purview today at all** |
| `place_of` | Q2's second clause has nothing to test, and a writ in a carrier's satchel has no location. **And `_event_place` returns `None` for the Record case, measured** |
| the writ as a `Record` | authority is either a broadcast (`holonic §37.3` row 1) or a rumour only, and **the player cannot name whom he binds** |
| the deposit rule | a held writ is paper nobody believes; the executor is never asked; Q2 needs an extension |
| `give` | `H-84` stands and the writ cannot leave the Duke's hand |
| `nearest_store` | **211 hearths starve beside 4,810 units, measured** |
| `commit`'s body | no oath ever binds, and `need`'s 81 questions have no act-made producer |
| bases as rostered values | **19 of 19 seats stay unfillable, measured**, and the `is_title` branch stays |
| the `Person.body` write | **`AX-5` names three self-motions and one has no writer** |
| the three-conjunct `holdings` rule | a Dicastery clerk who holds a duchy can unmake its Duke — **a defect this tree already found and reverted** |

**N is scored from all six directions and an N-line holding in exactly one is NARROWED, not passing.**
Pre-committed: **`place_of` is the line most likely to come back narrowed**, because `ARCH F.14` says
its signature is insufficient and this suite ships the insufficient one.

### E — where E will be attacked, in this order, each answered or conceded

1. **`Record.subject_matter: Any` is a schema hole** → answered by `record_kinds` + ⊕ L35's loader
   refusal. **Conceded: one more roster.**
2. **REACH floods a duke's questions** → answered by construction: REACH filters claims that already
   LANDED by a witness channel and never widens the fan (`observers_for` untouched). **Falsifier
   LB-2b.**
3. **`tell`'s `Partial` branch is a third path through `_told_content`** → **conceded: +1 branch.**
   The alternative (no lossy word) fails Jordan's *"there needs to be noise and slippage"* and
   discards `H-36`'s ruled receiver-side mechanism.
4. **`give` is +1 verb** → answered: it is ratified position 16's verb, named; `dispatch` (−1) folds
   into it.
5. **Two effect bodies for founding (`restore`, `found`)** → **conceded: +2.** One Record kind, one
   `work` path, two plans.
6. **`binds_bases` is a roster with one value** → **conceded**, and answered only by its reader
   landing the same day (§A.1.5 (b)). **If item 9 slips, this concession becomes a finding.**
7. **Three factored functions are counted as additions** → answered: that is §A.0.1 pt 2 and it
   **costs** the ledger two. **Not a concession — a self-inflicted cost, published.**

**E is scored LAST, as a ratio against what N and R found necessary, and never as an independent
axis.** 22 added, of which the pre-commitment concedes **4 as overhead** (`record_kinds`, the
`Partial` branch, `restore`+`found` as two rather than one, `binds_bases`). **The design FAILS E if
the author cannot delete two of those four in authoring.** ⚠ **And the scoring rule that matters
more: an audit that scores four axes and averages them rates an amputated design as elegant.** This
suite deletes 40 objects; **E must be read as a ratio, or the deletion alone will score it.**

### R — the unwatched generators, which must be shown running with no player in any seat

| generator | the chain, end to end | item |
|---|---|---|
| **wear → crossing → claim → question** | `matter.py:226-275` fires today at pass 21 on the populated world (measured baseline: **0 crossings after 1 season**) | 2a |
| **dearth → body → band → question, AND budget** | `nearest_store` shortfall → `Person.body` → `band_floors["body"]` → a claim → REACH → the reeve; **and `budget` falls 5→4→3→2, already wired** | 3a + 3b |
| **a fired date → the convener asked** | needs a date to exist; `convene` is resolvable and never executes today (**`w.dates` = 0**) | 2b |
| **NPC issuers and carriers** | writ → carry → `give` → `transfer`, driven by `alignment`, with no player at either end | 6 + 7 |
| **rumour** | `tell` at `Partial` spreading a distorted writ. **MEASURED baseline: `told_by` = 1 claim of 2,175** | 8 |

> **R-CHOICE's expected finding, pre-committed rather than discovered:** **an executor who ignores a
> writ is VISIBLE and NOT PUNISHED.** `03_THE_SURFACE.md`'s cell law shows him as UNHELD/STALE, and
> nothing sanctions him, because sanction needs a contest no provider supplies. **That is a LIMIT
> until PROC-B, and it is stated here rather than answered with a manufactured penalty.** If a later
> pass reports R-CHOICE as PASS without addressing it, the pass is wrong.

**R-completeness at the extremes, each with the row that covers it:**

| extreme | what happens | covered by |
|---|---|---|
| a writ naming a **dead** executor | the claim lands nowhere; the issuer learns by `document_key` **never firing** — an absence he cannot distinguish from refusal, which `holonic §37.1` says *"is the whole of enforcement drama"* | stated as a LIMIT, not closed |
| a Record with **two** holders | `holonic §15` says `hold` is **1 per object**, and **nothing enforces it** (⊕ R14). `give` must **release then mint** | item 6, LB-6 |
| a **malformed** writ | ⊕ S12: it mints, deposits and is asked about, and **forms no Candidate** — indistinguishable from an ignored one | ⊕ L35, item 5 |
| the **root** larder at 0 | `nearest_store` returns `None`; that must be a shortfall, not a `KeyError` | LB-3a's third arm |
| a seat at a rung `build_realm` never builds | ⊕ S15: empty `descendants`, **zero purview, silently** | item 10's build assertion |
| a person at **weight 200** | the draw must scale by `p.weight` or a cohort eats like one man | item 3a |
| **body exactly 0** | budget bottoms at **2**, not 0 (measured), so death must be MATTER's and not budget's | LB-3c |

### S — and the two tests the shorthand drops

**S passes on:** no scheduler · no latency · **one** walk (`descendants`, inclusive of its argument)
for reach and purview · **one** walk (`parent_of`) for stores · **one** claim shape · MATTER's
`#353 §25` order kept · **one** crossing helper for sites and bodies on **one** floor table.

**S's *pauses correctly* test:** the design **removes** a pause to nowhere — round one's channel-4
handoff to a sitting where `judging_set` raises `Unspecified`. It adds none: compliance is an act in
the same fold, not a handoff.

**S's *calculations consistent in methodology* test — and this is where the plan would have failed
it.** `band_floors["body"]` for a person and `band_floors[site.kind]` for a site is **one table read
one way**; the plan's `band_floors.person` would have been **two ladders for one quantity**, which
§0.06 names as an S defect *"even when each is individually correct"* — and which PLANT 1 shows does
not even load.

> **S FAILS if** the author needs a second ladder for bodies against sites, a second address type, or
> a second walk for reach against purview. **N FAILS if** any N-line above survives its cut, and a
> narrowed N-line is not a passing one. **E FAILS on the ratio rule** — if four conceded items stay
> four. **R FAILS if** any generator above needs a player to fire, or if seizure is presented as
> resolved.

### The pass fires on itself

**This file's own most likely findings, pre-committed:**
1. **The count is the claim most likely to be wrong**, because it is 61 rows of grep and one
   mis-partitioned reader moves it. §D.1 row 1 is how to attack it.
2. **`place_of` is shipped with a signature `ARCH F.14` declares insufficient**, and this file counts
   it as an addition rather than pretending it is free. A pass that finds the multi-rung Event case
   unserved has found something this file already conceded — **that is not a finding, it is a
   reading**, and §0.06's withholding-is-symmetric rule cuts both ways.
3. **Four of the first five items are `fix`-position work, not milestone work.** If a pass concludes
   the suite's cheapest wins are repairs rather than design, **it is right**, and the answer is
   §0.2: a repair that makes a season behave differently is worth more than a design that does not
   run.

---

# APPENDIX · CITATION REPAIRS

**Standing instruction, `CLAUDE.md` §0.1 pt 3 — *"A citation you have not opened is not a
citation."*** Every `path:line` in this file was opened in this session. The three shapes and what to
observe first:

| claiming | observe this first |
|---|---|
| *"X is absent / dead / never fires"* | **RUN the thing that would show presence** |
| *"X works today"* | **open the CALL SITE, not the declaration** |
| *"as `F` says at `:L`"* | **open `F` at `:L`** |

## Repairs made in this file

| source | wrong | actual, verified 2026-09-17 |
|---|---|---|
| the plan, §4 | REMOVED **37** / ADDED **17** | the tables' own contents sum to **38** and **18**; the stated net −20 was right and neither sub-count was (§A.1.3) |
| the plan, §4 | *"roughly −8 systems"* | its own list is 8 out and 2 in = **−6**; on the family scheme applied in §A.1.3 it is **−3** |
| the plan, §4 | the helpers row: *"6 (7 names; the fixture rides with its term)"* | **7 objects.** `budget_office_bonus` is ONE name whose fixture cell rides with it; the other six are six names. The row is 7, not 6 |
| the plan, §4 | `Office.binds` among the deleted fields | **retained** — ratified `Seat :=` spells `remit(acts[], binds)` and `ARCH F.17` names it as `oblige`'s operand (§A.1.5 (b)) |
| the plan, §4 | the matrix deletions: five rows | **six** — `(Office, establishment)` is live at `write_matrix.yaml:133` with `establish` as its producer (§A.1.1 (d)) |
| the plan, §4 | the helpers list | **`conferral_path` (`world_q.py:416-437`) is missing from it and has ZERO callers** |
| the plan, §§2.3, 4 | *"persons use a NEW `band_floors.person` cell set"* and *"`band_floors`' `body` key is the SITE kind `body` … **not** a person's body"* | **`band_floors["body"]` IS the person's body band row** — `rosters.yaml:814-816` says so and `budget.py:73` reads it for a `Person`. **PLANT 1: `band_floors.person` is refused at load** |
| the plan, §2.4 | `"holdings"` → `in_holdings` | **purview AND holdings AND strictly-higher rank.** `predicates.py:255-266` records the single-term version as a reverted defect; `ARCH §B.7` call 1 spells all three |
| the plan, §2.4 | *"the `is_title` branch and the four helpers are deleted"* | **`title_domain` has FIVE call sites in THREE files**, two of them inside `Office.__post_init__` (`carriers.py:536`, `:546`), one of which is the live King-in-the-Church refusal |
| the plan, §2.1 | *"`occasioned_by` … the `date_due` and `band_crossed` routes are dead (the branches return `[]`)"* | **there are no such branches.** They fall through a guard at `world_q.py:621-628` into a **generic id search** at `:629-632` that finds nothing |
| the plan, §2.1 | *"the parties named on the date (`_eff_convene` :174-190 … for the key that holds them)"* | **there is no such key.** A date is `{"id", "venue", "due_at", "convening_attached"}`, and `holder` is written **nowhere** in production |
| the plan, §3.1 | *"`judging_set` deleted (its one caller is itself)"* | **two harness callers**: `probes.py:1208`, `probes.py:2467` |
| the plan, §6 | *"H-34/H-41 (the two producerless rows … gain `found`)"* | **two holes, two mechanisms.** H-34 (*"establishment size per office kind"*) closes by **deleting the field**; H-41's three rows close by `establish` + `found` |
| the plan, §6 | `F.22` among the closed | **NOT closed.** `succeed` has no body, is not resolvable, and `holonic §15` makes a `succeed` Tenure `Rung → Person`, whose subject cannot act |
| the plan, §6 | RR-B: *"four sentences"*, incl. *"the 'nine typed terms' line"* | **eight limbs**, and the nine-terms limb is **withdrawn**: `ARCH §B.5` PRESCRIBES the Record-kind fold and calls the schema *"unspecified"*, so supplying it conforms. `§B.8`'s limb is **half-satisfied**, not falsified. Four new limbs: `conferral`'s operand, `holonic §37.1`'s compliance contest, `holonic §37.3`'s cluster case, and `03`'s containment-derived rank (**B-8**, a GAME change) |
| the plan, §6 | RR-C: *"sequencing"* | **three limbs.** It also deletes **ratified position 19b entirely** and `levy` from **position 19** |
| the plan, §8 | *"17 added, of which the pre-commitment concedes 4"* | **22 added**, and the four conceded are `record_kinds`, the `Partial` branch, `restore`+`found`, **`binds_bases`** |
| the plan, §4 | the vocabulary list, incl. `in_force` | **`in_force` was never in the engine.** Counting a withdrawn proposal as a deletion is the move `AUDIT_VERDICT.md` faulted round one for |
| round one `04_BUILD_ORDER.md` §A.1.3 | `ARCH §B.13` invariants 2/4/5/7/10 at `:456`/`:458`/`:463`/`:466`/`:468` | invariant 2 is at **:457** and 4 at **:459-462**; two of the five were one low. **This file cites `ARCH` by `§` only** (suite convention), which is why the repair is recorded rather than propagated |
| the plan, §7 | item 16 depends on item 10 | ⚠ **REVERSED: item 10 depends on item 16.** MEASURED on `build_realm(0)`: holds are `{('person','Office'): 19, ('NON-person','Rung'): 16}` and **`in_holdings` is false for every person over every rung**, so `revocation: "holdings"` is unsatisfiable until the faction holds are re-homed. Reported by `03` |
| the plan, §2.4 | `rank(seat)` as a `rung_kinds` ordinal | **`03` derives the conjunct from `World.contain_ascends`**, the ladder's single owner, enforced at `add_tenure`. Better than an ordinal (which is **S9**), and it buys one declared behaviour change — a lower seat holding the land may unmake the seat above it (**B-8**) |
| the plan, §2.4 / §4 | `Office.body_function` among the deleted fields | **kept as `03`'s derived cache.** Booked, with its ID-13 cost stated (§A.1.1 (e)) |
| the plan, §6 | `ARCH F.21` unmentioned; **this file's own first draft closed it** | **NARROWED, not closed** — subject abolished, remedy unwritten. `03`'s RR-B.2 / this file's B-8 |
| **this file, first draft** | purview and REACH are the same set | **they are not.** REACH is inclusive of the seat's rung; purview is that set **minus the seat exercised**, so a seat cannot revoke itself |
| the plan, §3.3 | `_eff_kill`'s cascade at `:415-418` | the loop opens at **`:416`**; `del w.persons[who]` is `:419` |
| the plan, §3.7 | `Rung._DECLARED :568` (correct) with the pops unstated | the pops are `carriers.py:574-582` and **`_DECLARED` cannot be edited without them** (⊕ L40) |

## Citations opened and found CORRECT — so the list above is not read as a complaint

**Opened and matching, one at a time.** `verb_table.yaml` — the 38 row starts, including
`commit` `:115`, `comply` `:130`, `confer` `:143`, `convene` `:155`, `create_record` `:166`,
`determine` `:186`, `dispatch` `:197`, `establish` `:209`, `evade / defy` `:220`, `forge` `:247`,
`issue` `:256`, `levy` `:348`, `oblige` `:375`, `petition` `:395`, `refract` `:406`, `release` `:419`,
`repudiate` `:433`, `restore` `:448` (`effect:` at `:465`), `revoke` `:468`, `succeed` `:490`,
`tell` `:507`, `transfer` `:728`, `work` `:755` · `world_q.py` `:48` `:54` `:146` `:172` `:399-413`
`:416-437` `:439` `:471` `:473-480` `:482-494` `:496-518` `:520-528` `:548-549` `:553-632` ·
`matter.py` `:48-50` `:155-166` `:167` `:169` `:174` `:184-185` `:226-275` `:262` `:266-270` `:272` ·
`calendar.py` `:33` `:37-38` · `epistemic.py` `:215-242` `:244` `:253` `:260` `:336` `:343-362` `:365`
`:405` · `witness.py` `:31` `:316` · `effects.py` the 11 decorators, `:93-126` `:174-190` `:245-260`
`:263-290` `:288-289` `:309-419` `:416-418` · `predicates.py` `:35` `:60` `:105-143` `:144` `:157`
`:166-191` `:181-182` `:194` `:222-288` `:234-235` `:252-274` `:290-295` `:297` · `options.py` `:35`
`:107` `:163-165` `:172` `:234-256` `:259-343` `:308-322` `:412` · `budget.py` `:56-57` `:63-75` ·
`fixtures.py` `:45-70` `:95-144` `:430` · `data/rosters.py` `:50-59` `:104-119` `:189-195` `:456-473`
· `data/verbs.py` `:216-217` `:248-252` `:265-329` `:369-375` `:485` · `data/requires.py` `:213-222`
`:531-598` · `data/matrix.py` `:123-155` · `carriers.py` `:36-59` `:129-156` `:216-222` `:254-256`
`:332-345` `:368-393` `:412-418` `:422-445` `:468-477` `:481-548` `:527-548` `:553` `:568` `:574-582`
`:589-596` `:599` · `world.py` `:151-177` `:186-194` `:197` `:223-258` `:242-256` `:275-293`
`:295-310` `:325-357` · `driver.py` `:96-100` `:145-158` `:203` `:283` · `resolve.py` `:52-57` `:161`
`:194` `:238` `:259-266` · `write_matrix.yaml` `:36-53` `:72-78` `:93-111` `:112` `:133-139` `:154-160`
`:161-167` `:224` `:280` `:294` `:301` `:315` `:322` `:329-357` `:368-372`, and **all 40 `(kind,
field)` pairs enumerated by script** · `rosters.yaml` `:95-146` `:250-270` `:692` `:805-816`
`:830-844` `:1175-1199` · `hole_register.yaml` `:166` `:176` `:348` `:370` `:394` `:462` `:618` `:715`
`:795` `:1000` `:1106-1108` `:1520` `:1533` · `populated.py` `:75` `:640-735` `:671` `:693`
`:820-830` `:833-843` `:846-860` · `headless.py` `:58-70` · `invariants.py` `:60-72` ·
`corpus_run.py` `:324` `:420` `:642-648` · `probes.py` `:680` `:970` `:1153` `:1177` `:1208` `:1376`
`:1444-1446` `:2467` `:2562` `:2654` · `test_season_shape.py` `:35` `:2361-2380` `:3076-3099` ·
`ARCH` §A.3, §B.3, §B.5, §B.7, §B.8, §B.13, §C.3, §C.6, §E, PART D rows 1 and 11, F.14–F.22 ·
`AX` the six axioms (AX-1 `:71`, AX-2 `:100`, AX-3 `:111`, AX-4 `:141`, AX-5 `:151`), §E.1.7, §E.2.5 ·
`holonic` §15 (the hold table), §37.1, §37.2, §37.3, and its `## Status:` line (**RATIFIED, ED-IN-0204
— the same ruling as `ARCH`**, which is why B-6 and B-7 are RR-B limbs and not merely departures) ·
`workplans/2026-09-11-reconciled-program.md` `:3` and the 27-position table `:134-161` ·
`_part2.md` positions 6 and 15/16 · `registers/editorial_ledger_in.jsonl:104` (ED-IN-0210, read as
JSON and quoted in full) · `registers/editorial_ledger_se.jsonl:51` · `references/id_reservations.yaml`
`:246` (**IN `next_free: 236`**, ED-IN-0236..0235 already allocated) and `:257` (**SE `next_free:
54`**) · `CLAUDE.md` §0, §0.05, §0.06, §0.1, §0.2, §0.3, §0.4, §4, §7, §8, §10 ·
`proposals/2026-09-17-governance-and-holdings/04_BUILD_ORDER.md` (§A.1's three tables, carried
forward) and `AUDIT_VERDICT.md`.

**Instruments re-run for this file, 2026-09-17, at `46aa21d`:**
`python -m engine.season.harness.register --requirements` → **met 1 · not_met 4 (R-01 R-02 R-04 R-05)
· partial 4** · `python tools/m1_acceptance.py --summary` → **verdict NOT MET; row 4 "All M1 junctures
execute" is 0/7 FAIL and says DOC-DERIVED in its own detail** · `build_realm(0)` + one season, for
every count in §A.3.9 · `questions_for` over all 46 persons, for the source histogram ·
`resolvable_verbs()` · `body_band_penalty` × `budget` over eleven body values · **two planted-defect
probes (PLANT 1, PLANT 2), neither of which modified the tree.**

> **AND THE LAST THING, because §0.2 is the only clause a session cannot satisfy by writing:**
> **nothing above has run.** Grade `paper`. Item 1 is twelve lines. Start there.
