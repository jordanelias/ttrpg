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
2. **A MOVED function counts 0.** `place_of` is `epistemic._event_place` promoted and generalised
   (`engine/season/epistemic.py:215`, one caller at `:253`); `World.remove_person` is `_eff_kill`'s
   cascade factored out (`engine/season/loop/effects.py:416-418`); `_crossings` is the site block
   factored out (`engine/season/loop/matter.py:255-275`). A reader holds the same concept in a new
   place. Counting them +1 would inflate the ADDED side to look conservative, which is the mirror
   bias.
3. **Content counts 0.** `engine/season/data/offices.yaml`'s rows, a fixture VALUE, a `titles`
   domain — these are what the game is about, not objects a reader must hold. **A fixture NAME
   counts 1**, because a name is a thing code says out loud (`budget_office_bonus` is the worked
   case: the cell is content, the name is mechanism).
4. **A `(kind, field)` matrix row and the field it names are TWO objects.** They are in two files
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

#### (e) Dataclass fields — 14

`engine/season/state/carriers.py`. Reader counts exclude the declaration itself and are partitioned.

| # | object | path | what reads it today |
|---|---|---|---|
| 17 | `Tenure.payload` | `carriers.py:59` | **NOTHING.** ⚠ `grep '\.payload'` returns 27 production hits and **every one is `Act.payload`** (`carriers.py:339`); no `Tenure(...)` construction anywhere passes `payload=`. 12 hits in `engine/season/tests`, 0 in `tests/valoria` |
| 18 | `Person.beliefs` | `carriers.py:381` | **NOTHING** in production; 0 in `engine/season/tests`; 1 in `tests/valoria` |
| 19 | `Office.establishment` | `carriers.py:491` | `world_q.py:413` (inside `establishment_of`, **which has no callers** — see row 34) + `probes.py:1376` (`assert off.establishment == []`). **MEASURED: 0 of 19 offices carry a non-empty value** |
| 20 | `Office.upkeep` | `carriers.py:493` | **NOTHING**, anywhere — 0 production, 0 tests, 0 harness |
| 21 | `Office.dates` | `carriers.py:492` | **NOTHING** |
| 22 | `Office.scope_rung` | `carriers.py:487` | **NOTHING in production.** Written inside `Office.__post_init__` (`carriers.py:546-548`) from `title_domain`; 2 hits in `engine/season/tests` |
| 23 | `Office.body_function` | `carriers.py:503` | **NOTHING in production.** Written inside `__post_init__` from `BODY_FUNCTION`. Its own comment: *"these fields exist because the first version validated them and threw them away … an artifact nothing reads"* |
| 24 | `Rung.sites` | `_DECLARED`, `carriers.py:568` | **NOTHING.** The one mention is `matter.py:198`'s comment: *"`r.sites` … is a BACK-REFERENCE NOTHING MAINTAINS — it is empty for every rung in the corpus"* |
| 25 | `Rung.records` | `_DECLARED`, `carriers.py:568` | **NOTHING** |
| 26 | `Rung.dates` | `_DECLARED`, `carriers.py:568` | **NOTHING** |
| 27 | `Rung.stake` | `_DECLARED`, `carriers.py:568` | **NOTHING.** Its matrix row is already in `write_matrix.yaml`'s `retired:` list (`:368-372`). `ARCH F.18`: *"'out of the office's stake', and `stake` was retired"* |
| 28 | `Rung.transmission` | `_DECLARED`, `carriers.py:568` | **NOTHING**, anywhere |
| 29 | `Rung.judging_set_rule` | `_DECLARED`, `carriers.py:568` | `world_q.py:147` only — inside `judging_set`'s `Unspecified` raise. `ARCH §B.7` call 3 deletes it by name |
| 30 | `Site.drawers` | `carriers.py:418` | **NOTHING.** Its matrix row is in the `retired:` list (`:372`) |

⚠ **`Office.binds` IS NOT ON THIS LIST, AND THE PLAN PUT IT HERE.** See §A.1.5 (b) — it is a dead
field by measurement and a **retained** one by ratified prescription, and the retention costs the
ledger two objects.

#### (f) Helpers, Queries and named terms — 8

| # | object | path | what reads it today |
|---|---|---|---|
| 31 | `title_domain` | `data/rosters.py:459` | ⚠ **FIVE call sites in THREE files, not one:** `predicates.py:152` (inside `under_purview`), `predicates.py:252` (`target_is_title`), **`carriers.py:536`** (`Office.__post_init__`'s title-in-a-body refusal), **`carriers.py:546`** (`scope_rung` derivation), `populated.py:671` (world-gen's seat/occupation discriminator). Imported at `predicates.py:27`, `carriers.py:34`, `populated.py:75` |
| 32 | `title_rank` | `data/rosters.py:465` | `predicates.py:163` (inside `highest_title_rank`), `predicates.py:270` |
| 33 | `titles_held` | `predicates.py:144` | `predicates.py:132` (`under_purview`), `:163` |
| 34 | `highest_title_rank` | `predicates.py:157` | `predicates.py:270` |
| 35 | `judging_set` | `world_q.py:146` | ⚠ **`probes.py:1208` and `probes.py:2467` — TWO harness callers, not "itself".** Raises `Unspecified("judging_set_rule", "S61")` |
| 36 | `conferral_path` | `world_q.py:416-437` | ⚠ **ADDED BY THIS FILE — the plan does not name it. NOTHING calls it.** `grep conferral_path` returns its own `def` and its own `TRACE.query` line and nothing else. It walks `off.rung → parent_of → root`, which is exactly the walk `descendants` inverts, and its own docstring concedes it is a limit: *"IT RETURNS RUNGS, NOT OFFICES, AND THAT IS A LIMIT RATHER THAN A CHOICE"* |
| 37 | `_req_dispatch` | `predicates.py:291-295` | `REQUIRES_PREDICATES["dispatch"]`. Goes with row 5 |
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

**REMOVED = 5 + 2 + 3 + 6 + 14 + 8 + 1 = 39.**

### A.1.2 · ADDED — **19 objects**

| kind | # | names | n |
|---|---|---|---|
| Queries | 1–2 | `reach(w, p)`, `nearest_store(w, rung, kind)` — **both absent today** (`grep 'def reach\|def nearest_store\|def place_of'` over `engine/season` → nothing) | 2 |
| verb rows | 3–4 | `give` (the `H-84` verb; ratified position 16 chose the shape), `found` (the `ARCH F.20` verb) | 2 |
| effect bodies | 5–11 | `commit`, `oblige`, `issue`, `petition`, `give`, `restore`, `found`. **All seven verified absent:** the 11 `@effect_for` decorators are `confer` `:92`, `release` `:129`, `revoke` `:159`, `convene` `:173`, `move` `:193`, `work` `:244`, `create_record` `:262`, `destroy_record` `:293`, `kill / wound` `:308`, `utter` `:422`, `transfer` `:437`. Count goes **11 → 18** | 7 |
| predicates | 12–14 | `_req_oblige`, `_req_issue`, `_req_give`. Today `REQUIRES_PREDICATES` holds `confer` `:166`, `release` `:193`, `revoke` `:221`, `dispatch` `:290`, `convene` `:297` — **five**, going to **seven** (`dispatch` out, three in) | 3 |
| rosters | 15–18 | `record_kinds`, `conferral_bases`, `revocation_bases`, **`binds_bases`** (see §A.1.5 (b)) | 4 |
| deposit rule | 19 | the document-content mint at WITNESS — one branch where the observation deposit runs, keyed on a hold-on-a-Record in `changes[]` (`epistemic.py:260`'s existing channel) | 1 |
| **content (0)** | — | `engine/season/data/offices.yaml`; `fixtures.body_step`; `fixtures.told_drift_band`; `binds_bases`' one value; `record_kinds`' five key-lists | 0 |
| **moved (0)** | — | `place_of` (← `_event_place` `:215`), `World.remove_person` (← `_eff_kill` `:416-418`), `_crossings` (← `matter.py:255-275`) | 0 |
| **WITHDRAWN from the plan (0)** | — | ⚠ ~~`band_floors.person`~~ — **it does not load.** §A.2 PLANT 1, EXECUTED | 0 |

**ADDED = 2 + 2 + 7 + 3 + 4 + 1 = 19.**

### A.1.3 · NET — three units, and the least favourable one is stated first

> ## **NET: −20 ENGINE OBJECTS. 39 removed against 19 added.**

| unit | out | in | net | is it the favourable unit? |
|---|---|---|---|---|
| **systems / families** (the coarsest, and the one that flatters least) | 8 | 5 | **−3** | **no — this is the worst one, and it is still negative** |
| **names** (§A.0.1's rule — the headline) | 39 | 19 | **−20** | it is the middle unit |
| **vocabulary** (terms a reader must hold) | 24 | 17 | **−7** | no |

**The eight families out:** the four response verbs · the title/rank family (four helpers, one
branch, one roster) · the two parallel document stores · the duplicate crossing carrier · the
`establishment`-as-a-field membership model · the office-bonus budget term · the two uncalled
purview-adjacent Queries (`judging_set`, `conferral_path`) · the dead-field residue as one sweep.
**The five in:** the Record-kind family (`record_kinds` + the deposit rule + `give`) · the reach/place
walk (`reach` + `place_of`) · the store walk (`nearest_store`) · the seat-basis family (three rosters,
three predicates) · the works/found family.

> ### RULED: **THE PLAN'S TWO ROW-LEVEL SLIPS CANCELLED, AND THE HEADLINE SURVIVED BY COINCIDENCE. RE-DERIVED HERE, IT HOLDS.**
> The plan's REMOVED table lists 5 + 2 + 3 + 5 + 15 + **6** + 1 and states 37; its helpers row names
> **seven** names and counts them as six, so the table's own contents sum to **38**. Its ADDED table
> lists 2 + 2 + 7 + 3 + 3 + 1, which sums to **18**, and states **17**. ~~37 − 17 = 20~~ →
> **38 − 18 = 20.** *Both sub-counts were one low, in compensating directions.* The stated net was
> right and neither stated sub-count was — which is `CLAUDE.md` §0.1 pt 4 in miniature: a figure can
> be correct and its support wrong, and **the support is the one to check.** A third slip is in the
> plan's own caveat: *"roughly −8 systems (four verbs, three World collections, one title family
> gone; one Record family, one walk family in)"* is **8 out and 2 in, i.e. −6**, not −8.
>
> **My independent count is 39 − 19 = −20** on a rule stated before the counting, with two rows the
> plan missed added (`(Office, establishment)`, `conferral_path`) and one row the plan had removed
> (`Office.binds`) returned at a cost of two.

**The two alternatives, so nobody thinks the number was tuned:**

| if… | out | in | net |
|---|---|---|---|
| `Office.binds` is DELETED and `binds_bases` never exists (the plan's shape) | 40 | 18 | **−22** |
| **`Office.binds` is RETAINED and given a reader (RULED here)** | 39 | 19 | **−20** |
| the `titles` roster is also deleted, its domains moving into `offices.yaml` (residue, §A.1.5 (c)) | 40 | 19 | **−21** |

> ### RULED: **THIS FILE TAKES THE LEAST FAVOURABLE OF THE THREE.**
> −22 is available and is not taken, because `ARCH §B.7`'s ratified `Seat :=` line spells
> `remit(acts[], binds)` and `ARCH F.17` names `binds` as `oblige`'s own operand. **A suite whose
> headline is a deletion count has exactly one bias, and it is toward deleting**; the check on it is
> to publish the arithmetic for the option not taken. It is published above.

### A.1.4 · Vocabulary — 24 out, 17 in

**Rule:** a name in the engine's vocabulary that a reader must hold today and would not after.

**OUT (24).** Verbs: `levy`, `comply`, `evade`, `defy`, `refract`, `dispatch` (6). Question sources:
`date_due`, `band_crossed` (2). Carriers and stores: `Dispensation` as a type, `Petition` as a type,
`crossings` (3). The whole title family as one concept: `title` (1). Queries: `judging_set`,
`conferral_path` (2). Retired field names: `payload` (on a Tenure), `beliefs`, `upkeep`,
`scope_rung`, `body_function`, `stake`, `transmission`, `judging_set_rule`, `drawers` (9). Fixture:
`budget_office_bonus` (1).

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
> Cost: **+2 to the net** (−22 → −20), published in §A.1.3. Benefit: two RR-B limbs do not open, and
> `ARCH F.17` closes **as F.17 itself states it** rather than by a substitute rule.
>
> ⚠ **The counter-argument, recorded because it is good:** a roster with one value and one reader is
> the `governance_modes` shape (*"They were not wrong; they were UNREAD"*, `rosters.yaml`) with extra
> steps. **It is answered by the reader, not by the roster** — `binds_bases` has a consumer on the
> day it lands, which `governance_modes` never did. If Jordan prefers the deletion, take −22 and add
> two RR-B limbs.

> ### RULED (c): **TWO OBJECTS THE PLAN DOES NOT NAME ARE DELETED HERE, AND ONE IS RESIDUE.**
> **`(Office, establishment)`**, the matrix row (§A.1.1 row 16) — forced, counted.
> **`conferral_path`** (`world_q.py:416-437`) — a Query with **zero callers**, superseded by
> `descendants(w, seat.rung)`, which `03`'s purview rule uses. Counted.
> **`titles`, the roster** (`rosters.yaml:692`) — RESIDUE. Its only code reader is `title_domain`
> (via `TITLE_DOMAINS`), so deleting the helpers orphans it, and an orphaned roster is `S11`: loads
> clean, `roster()` raises at READ, not at load. **Ruling: its domains move into `offices.yaml` as
> each seat's `rung` and the roster goes** — which is where Jordan's 2026-09-02 content belongs once
> every seat has a rung. Counted on the supplementary line only (−21), because a reader may fairly
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
> the net becomes −21. Counted as a rewrite (0) on the assumption that item 9 lands.

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
`in_holdings` `:60` · `under_purview` `:105-143` (walks `titles_held`) · `titles_held` `:144` ·
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
> **The rank term survives with no title helper.** `rank(seat) = rung_kinds.index(seat.rung.kind)`
> is exactly what `title_rank` computes (`data/rosters.py:465-473`: *"RANK IS NOT A SECOND LADDER.
> `rung_kinds` is already ordered person → realm"*), and `highest_rank(actor) = max(rank(s) for s in
> the actor's held seats)` is exactly `highest_title_rank` with "title" struck. **So all four helpers
> go, all three conjuncts stay, and no ordinal is invented.** This is the single most important
> correction in this file: without it, `03` would have shipped a known over-admission.
>
> ⚠ **The residue, stated:** `ARCH F.21` — *"the rank of a cluster seat (`scope = null`): no rank;
> the loader forbids a `higher_rank` conjunct on one"* — **closes by construction** once every seat
> has a `rung`, and its remedy becomes unreachable. Counted as a closure in §C.5 and as an RR-B limb
> in §C.4, because `§B.7`'s `Seat :=` spells `scope? (null = a cluster)` and `holonic §37.3` row 3
> protects *"office-clusters with `rung? = null`, which have no place"* by name.

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
