# 04 · BUILD ORDER — how the governance and built-world work gets built, in dependency order

## Status: **PROPOSED (2026-09-17). HELD BACK IN FULL. NOTHING RATIFIES ON MERGE.**
## Method: `opus` producer, `opus` self-adversarial pass (`CLAUDE.md` §10 — judgment over dispersed surfaces, and the tier is declared because the *order* is the judgment). Read-only against the tree at 2026-09-17; every number below was re-run here and every `path:line` was opened before it was written. Repairs in the APPENDIX.
## Grade: **`paper`** (`CLAUDE.md` §0.2). Nothing in this file executes. Its own first execution artifact is item 1b's.
## Lane: **IN**, sharing `ED-IN-0232` with `03_THE_SURFACE.md`. This file allocates no id and edits no ledger.
## ⚠ **UNIFIED 2026-09-17 (`00_THE_DESIGN.md`).** Suite-wide: **`ARCH`** = `architecture/meta/04_CODE_ARCHITECTURE.md`, **`AX`** = `architecture/meta/01_AXIOMS.md`; a bare `01`/`02`/`03`/`04` means a file in THIS directory — which matters here, because this file HAS a `§A.3` of its own and `04 §A.3` used to mean the architecture's. This file's falsifiers are **`BO-n`**. The multi-season construction is **a `works`** (`01` §A.12). Reconciliation edits are struck in place.

---

> **Jordan, on why `done` had to be redefined:** *"I need to break out of the infrastructure loop."*
>
> **`CLAUDE.md` §0.2, which is the only clause in Layer 0 a session cannot satisfy by writing:** *"A
> milestone juncture is done when the behaviour EXECUTES. Not when a document exists with a
> `## Status:` line."*
>
> ⚠ **SO READ THIS FILE AS A LIST OF THINGS THAT HAVE NOT HAPPENED.** Every row below is a
> prediction with a named falsifier and a named control. The document you are holding is worth
> exactly as much as the first row somebody executes, and no more.

---

# PART A · THE SEQUENCE

## A.0 · The three rules that decide the order

Nothing here is sequenced by preference. Three rules do all the ordering, and each is checkable.

### A.0.1 · THE GATE-CONTRACT RULE, stated once so it is never re-derived

> **A piece of work is downstream of the Arc 2 gate contract (ratified positions 3–7) IF AND ONLY IF
> it is an `@effect_for` body, or it writes a Tenure whose subject is not the actor. Everything else
> is order-free.**

That is the whole test. Applied to the two subjects it partitions them cleanly:

| artifact | downstream? | why |
|---|---|---|
| a roster row — a `site_kinds` member, `wear_per_season`, `band_floors`, `site_yield`, a 7th `remit_acts` | **NO** | the gate's signature is not on the loaders' path. `data/rosters.py`, `data/fixtures.py` and `data/verbs.py` never see a token |
| a `write_matrix.yaml` row | **NO** | `ARCH §B.13` re-spells `social:` as `writer:` and splits `emits:` into `on_write`/`on_condition` at Arc 2 — but mechanically, by a loader edit, not per-row judgment. **Author rows in the CURRENT spelling**; the new one fails the load today |
| a `world_q` / `faction_q` Query | **NO** | `ARCH §A.2` gives `queries/world_q` *owns (writes): nothing*, and no token parameter exists on any function. A Query is structurally outside the write path |
| a `requires_typed` cell or a `REQUIRES_PREDICATES` entry | **NO** | preconditions read; they never write. `_req_revoke` *is* rewritten at position 6 — for `via`, not for the gate |
| a verb row whose `writes:` is `[]` | **NO** | no effect body, nothing to rewrite |
| a question source, a predicate, a person-side eligibility branch | **NO** | `decision/` is on the far side of `ARCH §C.3`; it cannot see a `World`, let alone a token |
| **a verb row with a non-empty `writes:`** | **YES** | it needs an `@effect_for` body, written to a contract that changes at position 7 |
| **anything opening or closing a Tenure whose subject is not the actor** | **YES, TWICE** | position 6 (`Act.via` + F3) *and* position 7 (the contract) |

**Roughly two thirds of both subjects are therefore independent of Arc 2.** The expensive part is
narrow and nameable: the effect bodies and the Tenure-on-another writes. **The arithmetic, not the
doctrine:** paying Arc 2 first costs **11** effect rewrites once (`grep -c "@effect_for"
engine/season/loop/effects.py` → 11, measured); not paying it first costs 11 + N later, and at
N = 12 that is **23 rewrites instead of 11**. `HANDOFF.md:43`'s *"paying for the rewrite twice"* is
this sum and nothing more.

### A.0.2 · The dependency rule

An item precedes another only where the second cannot be *observed* without the first. That is a
weaker relation than "would be convenient", and it is why items 1–12 are nearly unordered among
themselves. Where the plan's order and the observability order disagree, observability wins and the
row says so.

### A.0.3 · The hash rule

Two changes in this file move the corpus content hash: **items 1a+1b TOGETHER** (which put
`work`/`restore`/`examine` into candidate sets for the first time — 1a alone moves nothing, because
Q3 fires on nothing today; see item 1) and **position 7's `NoOpReceipt`** (*"the one Arc-2 clause
licensed to move the hash"*, `_part2` position 7, whose own observable is `work`). **They must land
in separate commits**, each with its own attributed delta, or the two movements are inseparable and
neither is attributable — and note that **both are about `work`**, which is exactly why they would
be confused for one another.

---

## A.1 · THE PRE-FLIGHT — every way a proposed row is refused

**This is the section to use, and it is a checklist, not a summary.** Every row was produced by
**planting the defect and reading the loader's own refusal** — five scratch probes that write a
mutated copy of `verb_table.yaml` / `write_matrix.yaml` / `rosters.yaml` into a temp directory,
repoint the module constant the loader reads, re-call the loader, and restore. Nothing in the tree
was modified. Column 3 is the exception class the built loader actually raises.

> **The single most useful thing to take from A.1:** *the loaders are tight on the grammar and loose
> on the schema.* They refuse a malformed precondition with a paragraph of reasoning, and accept a
> whole invented column in silence. **Design freely; then check §A.1.3 by hand, because it is the
> half that will not check itself.**

### A.1.1 · Refused AT LOAD — the whole package fails to import (32)

| # | the defect | refusal, at | 
|---|---|---|
| L1 | `requires_typed.form` names a form outside the closed seven | `SystemExit` — *"names requires form 'X', which is not in rosters.yaml's requires_forms… an eighth is a new thing a precondition can ASK, which is a design change and not a table edit"* (`data/requires.py:549-554`) |
| L2 | `form:` is in the roster and has no `@requirement_form` class — today `cardinality` and `basis` | `SystemExit` — *"IN the grammar and has no implementation"* (`:556-560`) |
| L3 | the cell binds an operand outside `requires_operands` | `SystemExit` — *"Coining an operand is filling `H-94` by keyword argument"* (`:567-571`) |
| L4 | the operand is rostered but outside **that form's** `needs:` list | `SystemExit` — *"not in that form's `needs:`"* (`:572-575`) |
| L5 | a predicate stem no reader dispatches on | `SystemExit` — *"would evaluate UNKNOWN in every world and refuse the verb everywhere, which is indistinguishable from an honest operand gap"* (`:531-536`) |
| L6 | an `all:` with fewer than two clauses | `SystemExit` — *"a conjunction of one is the clause itself"* (`:544-546`) |
| L7 | `scalar_threshold` with BOTH `threshold:` and `threshold_predicate:`, or NEITHER | `SystemExit` — *"needs exactly one of"* (`:213-216`) |
| L8 | a comparator outside `{">=", "<="}` | `SystemExit` — *"a strict comparator is a change to what a precondition can say"* (`:218-222`) |
| L9 | `requires_typed: none` with no `requires_typed_note:` | `SystemExit` — *"an untyped cell with no reason is indistinguishable from one nobody typed"* (`data/verbs.py:248-252`) |
| L10 | `requires_typed:` is any string other than `none` | `SystemExit` — *"the only string admitted is `none`"* (`data/requires.py:593-598`) |
| L11 | a `writes:` pair on no `write_matrix.yaml` row — **including a retired one** | `SystemExit` — *"§30: ANY UNMARKED CELL IS A WRITE-CLASS VIOLATION. Rule the Part D row first, then add the verb"* (`data/verbs.py:298-307`) |
| L12 | `eligibility:` names `capability` — **even if `capability` is added to the roster** | `SystemExit`, **by name**, independent of the roster (`data/verbs.py:311-315`) |
| L13 | `eligibility:` names a kind outside `[own, remit, hold, presence]` | `SystemExit` — *"a fifth would be a new way to make a verb unavailable"* (`:316-320`) |
| L14 | `scale:` is not a `rung_kinds` member — so **`faction` and `world` both refuse** | `SystemExit` (`:324-326`) |
| L15 | `stratum:` is not one of the five | `SystemExit` (`:327-329`) |
| L16 | a degree-keyed `writes:` with no `contests:` | `SystemExit` — *"Nothing resolves a degree for it"* (`:271-274`) |
| L17 | a degree-keyed `emits:` with no `contests:` | `SystemExit` — *"unlike the `writes:` case this used to load clean and raise at the first fold"* (`:287-290`) |
| L18 | `contests:` with a FLAT `writes:` | `SystemExit` — *"losing the contest writes exactly what winning it does"* (`:265-270`) |
| L19 | `contests:` with a FLAT `emits:` | `SystemExit` — *"a wound emitting `person.died`"* (`:292-297`) |
| L20 | `writes:` and `emits:` keyed on **different band sets** | `SystemExit` — *"an outcome that either changes the world silently or reports a change it did not make"* (`:256-260`) |
| L21 | a duplicate `verb:` name | `SystemExit` (`:216-217`) |
| L22 | a duplicate mapping key **anywhere in any of the three YAMLs** | `ValueError` from `load_yaml`'s `_no_dup` — *"`safe_load` would silently keep the last"* (`data/rosters.py:50-59`) |
| L23 | a duplicate `(kind, field)` in `write_matrix.yaml` | `SystemExit` — *"a duplicate makes the gate's behaviour depend on file order"* (`data/matrix.py:146-155`) |
| L24 | a matrix row whose `class:` disagrees with its `steps:` derivation | `SystemExit` — *"One is wrong; fix the row or fix `STEP_CLASS` — do not let them disagree"* (`data/matrix.py:136-143`) |
| L25 | a `steps:` abbreviation outside `CAL MAT DEL RES WIT CEN` | **bare `KeyError`** (`data/matrix.py:125`) — not a diagnosed refusal |
| L26 | a `social:` outside `true false n/a` | **bare `KeyError`** (`data/matrix.py:128`) |
| L27 | an 8th `tenure_kinds` member without extending `release`'s declared `domain:` | `SystemExit`, loader invariant 6 — *"an edge that can be opened and never closed"* (`data/verbs.py:369-375`) |
| L28 | a `band_floors` or `wear_per_season` outer key that is not a `site_kinds` member | `Forbidden` — *"names site kind(s) no roster carries"* (`data/fixtures.py:111-117`) |
| L29 | a `site_kinds` member **without** a `wear_per_season` rate AND a `band_floors` cell | `Ungraded` — *"has no row for site kind(s)"* (`data/fixtures.py:118-123`) |
| L30 | `site_yield` producing a matter kind outside `matter_kinds` | `Forbidden` — *"Open means addable, not unchecked"* (`data/fixtures.py:125-137`) |
| L31 | `site_yield` empty for every kind | `Ungraded` — *"shipping the control as the default"* (`data/fixtures.py:138-144`) |
| L32 | a roster with two owner pointers, or a pointer **and** `values:` | `Unspecified`, ED-IN-0230 (`data/rosters.py:104-119`) |

> ### RULED: **L28 and L29 are a PAIR, and they are the built world's one hard load constraint.**
> Adding a building kind is **three coordinated data edits, never one** — `site_kinds.values`,
> `wear_per_season.rates`, `band_floors.cells` — because `data/fixtures.py:106-123` checks
> membership in **both directions**. A fourth edit, `site_yield`, is optional and validated against
> `matter_kinds` (L30). The rule's own law line is the reason: *"a wear table that returns 20 for an
> unregistered site kind does not fail — it answers, plausibly and wrongly, forever"*
> (`data/fixtures.py:122-123`).

### A.1.2 · Refused at RUN time — the load is green and the verb dies later (12)

| # | the defect | what happens |
|---|---|---|
| R1 | `writes:` non-empty and **no `@effect_for` body** | the row is excluded from `resolvable_verbs()` (`loop/driver.py:99`), so no chooser ever offers it; hand-folded, `Unspecified` — *"Part E does not say WHAT VALUE"* (`loop/resolve.py:238`). **`restore` is this today** |
| R2 | a prose `requires:` with no `REQUIRES_PREDICATES` entry and no typed cell | excluded from `resolvable_verbs()` (`driver.py:96-98`); hand-folded, *"a precondition the fold cannot evaluate"* (`resolve.py:194`). **`thread_read` is this today** |
| R3 | `contests:` on a prize with a `module:` and no registered `provider:` | **silently dropped** from `resolvable_verbs()` (`driver.py:145-158`) |
| R4 | `contests:` on a prize absent from `contest_subsystems.prizes` | `manifest.resolve` returns `None` → the same silent drop. **Loads clean** |
| R5 | the effect reaches RESOLVE without an operand the payload carries | `InstrumentDefect` — *"a CALLER defect and not a design gap"* (`loop/effects.py:60-84`) |
| R6 | the effect touches nothing | the fold emits the **refusal**, not the success (`resolve.py:259-266`) |
| R7 | a write whose `(kind, field)` row does not admit the current step | `Forbidden` (`state/world.py:325-346`) |
| R8 | a `social: true` row written by anything other than `driver="Act"` | `Forbidden` — *"L4 — social:true means ONLY AN ACT may write it. The world may silt a harbour; IT MAY NOT SOUR A TOWN'S MOOD"* (`world.py:352-357`) |
| R9 | a `contain` Tenure that does not strictly ascend `rung_kinds` | `Forbidden` from `add_tenure` (`world.py:248-256`); `contain_ascends` (`world.py:197`) is the single owner |
| R10 | a `Tenure.kind` outside the seven | `Unowned` from `add_tenure` (`world.py:242-247`) |
| R11 | a `Rung` attribute outside the 11-name `_DECLARED` whitelist | `Forbidden` — *"a Rung owns NO social aggregate: no norms, no densities, no reputation, no unrest, no legitimacy. EVERY ONE IS A QUERY"* (`carriers.py:568-569`; `__init__`'s refusal `:585-587`, `__setattr__` `:589-596`) |
| R12 | a fixture the code names with no register row, or an unregistered site kind | `Ungraded` from `Fixtures.get` / `.wear` (`data/fixtures.py:45-70`) |

### A.1.3 · Accepted and **INERT** — the silent class, and the dangerous one (11)

**These all load clean and are wrong.** Nothing will tell an author. Five of `ARCH §B.13`'s twelve
loader invariants — **2, 4, 5, 7 and 10** (`ARCH §B.13` at `:456`, `:458`, `:463`, `:466`, `:468`) —
are the reason: they are specified and **unbuilt**, so the defects they exist to refuse land silently.

| # | the defect | consequence | the unbuilt invariant |
|---|---|---|---|
| **S1** | **any unknown column on a verb row** (`via:`, `population_cost:`, `delegates:`) | silently ignored. `_load_verb_table` reads exactly `verb stratum eligibility requires writes emits emits_on_refusal grade scale contests requires_typed requires_typed_note domain` and nothing else. A new column is a declared-but-unread field, which is `AX` **ID-13** (`AX:489`) | **10** |
| S2 | an `emits:` kind no `write_matrix.yaml` row declares | emitted by the fold anyway. `_refuse_undeclared_kind` (`world.py:275-293`) fires only on the `emits=` parameter, which the fold never passes — its emissions go through `ev()` | **7** |
| **S3** | a new `[RES]` matrix row with no producing verb | reported by `rows_without_a_producer()` (`data/verbs.py:485`), whose **only caller asserts the SHAPE and prints the count** (`engine/season/tests/test_season_shape.py:3076-3099`, `assert isinstance(no_producer, dict)` at `:3095`) and **cannot fail** | **2** (REPORT-ONLY) |
| S4 | `social: true` on a row with a `MAT` or `CEN` step | loads clean. The live data happens to satisfy it — **measured, zero violations** — so a proposal is the first thing that could break it | **5** |
| S5 | an eligibility alternative that can decline with `emits_on_refusal: []` | loads clean; a refused act produces the body literal `act.ineligible` (`resolve.py:161`) | **4**, widened form |
| **S6** | a 5th `eligibility_kinds` member, rostered | loads clean, and neither `_eligible` nor `person_side_eligible` has a branch, so the disjunct **falls through to `return False`** with no diagnostic (`decision/options.py:131-172`) | — |
| **S7** | a 9th `requires_operands` member, rostered and admitted by a form's `needs:` | **loads clean**, and `_derive_operand` (`options.py:259-323`) has no branch → `operands_for` returns `None` and **no Candidate ever forms** | — |
| S8 | a 6th `strata` member | loads clean; `stratum_of` maps it by roster index, so it works — and silently **reorders which acts see which world** (`rosters.yaml:142-144`: *"ORDER IS SEMANTIC HERE"*) | — |
| S9 | a 9th `rung_kinds` member | loads clean; changes `title_rank`'s ordinals, `contain_ascends`'s ordering and every `scale:` cell's meaning at once. **Nothing asserts `titles.domains` stays total over the ladder** | — |
| S10 | a 7th `remit_acts` member (the six are at `rosters.yaml:119`) | loads clean — so `levy`'s declared substitution closes as a one-line data edit | — |
| S11 | a roster with `values: []` that nothing reads | loads clean. `roster()`'s empty refusal (`data/rosters.py:189-195`) fires **at READ, not at load** | — |

> ### RULED: **the pre-flight is run BY HAND, and no guard may be built for §A.1.3.**
> Four of the eleven have `verb_table.yaml`, `write_matrix.yaml` or the loader itself as their
> subject, which is `CLAUDE.md` §0.1 pt 5's predicate excluding them by name: *"a guard whose
> subject is another guard"* and *"a grader over the gate list"*. What **is** licensed is the
> planted-violation test per invariant that **ratified position 23** already schedules (`ARCH §E`
> step 2: *"each invariant fails on a planted violation naming the row, then passes"*). Until
> position 23, the enforcement is that an author reads this table. See §B.4.

---

## A.2 · WHAT IS ALREADY CHEAP — the verb rows were never the expensive part

**Constructively loaded against the real loaders**, not argued: the five rows either subject plausibly
wants were written and imported, 43 rows total, all green.

```yaml
found     own · scalar_threshold(of: from, scalar: stores, key: kind, threshold: amount)
          writes [Rung.exists, Tenure.since, Rung.stores]   emits [rung.founded, …]
build     own | presence:<rung> · the same cell
          writes [Site.exists, Rung.stores]                 emits [site.built, …]
repair    own | presence:<site> · all[existence(site, Site), relation(site, present_at)]
          writes [Site.condition]                           emits [condition.worn]
delegate  remit:confer · prose requires (needs a predicate)
          writes [Tenure.since]                             emits [tenure.opened]
capture   own · contests "a field" · existence(subject, Rung)
          writes {Success: [Tenure.until, Tenure.since], Failure: []}
```

> ### RULED: **NO NEW FORM, NO NEW OPERAND, NO NEW STEM, NO NEW ROSTER MEMBER, NO NEW MATRIX ROW.**
> All five load on the grammar as it stands. `found`'s stake is `transfer`'s own cell shape, and
> `from` is the one operand a person can already derive (`containing_rung_of`, `options.py:317`).
> **So the question is never "may we add a verb". It is "what does the effect body do", "which
> question source asks about it", and "what observes it" — which is what the rest of this file is
> about.** The one near-miss worth recording: a cell spelled `form: amount` fails at load, because
> `amount` is an **operand** and never a **form** (L1).

Three things are *not* cheap and the pre-flight says which: `capture` will not RUN (R3/R4 — the
`a field` prize at `rosters.yaml:660` carries a `module:` and no `provider:`, deliberately);
`delegate` needs a predicate (R2); and every one of the five with a non-empty `writes:` needs an
effect body, which is Arc-2-flagged by §A.0.1.

---

## A.3 · THE FIRST FIVE — small, testable today, and none of them Arc-2-flagged

Each block runs **Change → Why here → Artifact → Control → Cost → Breaks if wrong → Falsifier**,
which is the ratified per-instruction template (`C14` §1.6, from `19_PLAN.md`).

### 1 · Q3's referent becomes the site id · **S** · position: fix · Arc-2: **no**

**Change.** `engine/season/queries/world_q.py:518` reads
`out.append(Question(f"q:band:{what}", "band_crossed", (what,), what))`, inside
`for who, what, *_rest in w.crossings:` at `:514`. **`what` is the site-USE VERB** from
`matter.py:272`'s `w.crossings.append((s.id, verb, before, s.condition, ev.id))` (⚠ line repair
2026-09-17: ~~`:271`~~ is `w.log.append(ev)`); **`who` is the
site id, and it is already bound two lines above** (`:515-516` resolve `site` and `at` from it, to
decide whether the person is present). The one question source that fires on a *place* therefore has
a *verb name* as its referent. Repair: `Question(f"q:band:{who}", "band_crossed", (who,), who)`, or
carry both.

**Why here.** It is the smallest change in either subject and it unblocks the most: `_derive_operand`
returns the question's referent for the `site` operand (`options.py:311-312`, `if name == "site":
return subject`), so the moment the referent is a site id, `work`, `restore` and `examine` get a
**bound** `site` and their typed cells stop reading UNKNOWN. `restore`'s own note says this in terms:
*"What keeps `restore` unexecutable is the OTHER half… no referent this corpus produces is a Site"*
(`verb_table.yaml:460` — ⚠ line repair 2026-09-17, ~~`:458`~~ is the cell's `of: site` line; `02`
carried `:460` and was right).

⚠ **THIS IS A DESIGN EDIT, NOT A REPAIR, AND ITS OWN ROW SAYS SO.** `H-110`
(`engine/season/hole_register.yaml:1533-1544`, tier 1, kind `WIRING`, **grade `absent`** at `:1538`, registered
**2026-09-03**) declines the one-line fix on purpose: *"THE FIX IS ONE LINE AND IS NOT TAKEN HERE ON
PURPOSE: the crossing Event id is already in the tuple, and carrying it onto the Question changes a
surface `occasioned_by` does not own — `questions_for` is §F1's Q3 and its shape is what `H-54` and
the aggregation rule read. **A one-line change to a rule three other rows depend on is a design
edit, not a repair**"* (its `cite:` field, `:1543`). Treat it as a design edit: name the three dependent rows, decide
the shape, and **re-record the goldens once, declared and attributed** (§A.0.3).

**Artifact.** ⚠ **CORRECTED HERE, AND THE CORRECTION SPLITS THE ITEM.** The reconciling plan gave
this row the artifact *"`work` candidates rising from 0 of 723"*. **The second half is wrong and
load-bearing; the first half was this file's own error and is struck.**

(a) ⛔ **STRUCK 2026-09-17, RE-MEASURED.** ~~"723 is `transfer`'s corpus fold count, not `work`'s …
so no `work` count is printed anywhere."~~ **723 is the corpus's per-verb CANDIDATE count, so it is
both verbs' number and the tree measures it for `work` by name:** *"`work` 723 refusals with no
execution"* (`engine/season/tests/test_season_shape.py:7279`, measured 2026-09-04 and attributed by
act id), *"`work` alone refuses 723 times"* (`:7240`), and `verb_table.yaml:765`'s own note — *"the
corpus refuses all 723 because no referent it produces is a Site"*. `02` §A.6.2 and `03` §A.5.1 quoted
the tree correctly and this file contradicted them on a misreading of `hole_register.yaml:2155`, which
is the `coin` arm's identical count. **`CLAUDE.md` §0.1 pt 3, the third shape, applied to my own
repair: the citation was not opened.** What survives, and is why the artifact still had to change:
**723 Candidates DO form and the FOLD refuses all of them**, so *"candidates rising from 0"* names a
number that is already 723. The artifact is **`work` EXECUTIONS**, i.e. `work` leaving
`corpus_run`'s `VERBS ONLY REFUSED` list — `corpus_run` prints a **set** of refused verb names
(`harness/corpus_run.py:644`, `tried = sorted({v for r in live for v in r["refused"]})`), and that set
losing `work` is the observable.

(b) **MEASURED 2026-09-17, and re-run for the unification: Q3 fires on nothing in any world any gate
executes**, so the referent fix alone changes no observable. Every site in the populated world starts at `condition_scale = 1000`
(`data/fixtures.py:160`; `harness/populated.py:373-374`) and `wear_per_season` is 10 for every kind
(`rosters.yaml:841-844`); the highest floor is `bulk_shipping: 800` (`rosters.yaml:1191`). Driving
MATTER on `build_realm(0)`, **the first crossing fires at pass 21** (37 of them, `s_s_001_harbour`
`bulk_shipping` 800 → 790). CI runs the populated world for **1** season (`tools/m1_acceptance.py`
row 5: *"2 populated x 1"*) and `corpus_run` for at most **6** (`DISTINCT WORLDS RUN 89 … season
counts [1, 2, 3, 4, 5, 6]`). `w.crossings` is empty after one populated season — measured.

So the item is **1a + 1b**, and 1a is not observable without 1b:

- **1a · the referent** (**S**). Artifact: a **unit** test that plants a crossing tuple and reads the
  Question — no season required. This is the right instrument precisely because a 21-season run is not.
- **1b · a world in which a floor is crossed** (**S**). Either seed a subset of sites below a floor at
  build time (`populated.py:373-374` / `corpus_run.py:216-217`, both of which pass
  `condition=w.fixtures.get("condition_scale")`), or run the observing probe past pass 21. **The
  seeded arm is better**: a world where nothing is worn has no repair to do, which makes the wear
  clock scenery — R4's own falsifier, *"pressure that changes nobody's decision is scenery"*
  (`references/design_rulings_2026-09-06.md:92`).

With 1a+1b: `corpus_run` prints `VERBS ONLY REFUSED : 2 — ['examine', 'work']` today; **`work`
leaves that list** and `VERBS THAT EXECUTED : 11 of 38` rises.

**Control.** The `band_floors` declared sweep — `sweep: [declared, halved, doubled]`
(`rosters.yaml:1179`). Halve the floors and the crossing season moves; the question count must move
with it, or the route is not closed. ⚠ **`wear_per_season` declares NO sweep** (`rosters.yaml:831-844`
has `row: H-07` and no `sweep:` key), so *"wear halved and doubled"* is not an available control arm
and must not be cited as one.

**Cost.** One tuple index. No new primitive.

**Breaks if wrong.** Q3's shape is read by `H-54` (the source-order tiebreak) and the aggregation
rule; changing the referent without changing the id would give two questions the same `q.id`.

**Falsifier.** `test_q3_a_band_crossing_raises_a_question_about_the_site_not_the_verb`.
⚠ **The existing `test_wa_work_refuses_for_want_of_a_site_and_that_is_a_polarity_correction`
(`engine/season/tests/test_season_shape.py:7104`) does NOT go red** — it hand-folds Acts with an
explicit `payload={"site": …}`, so it never passes through `operands_for`. It stays green **as the
control**: `work` must still refuse an act naming no site and still admit a workable one. Verified
by reading it, not assumed.

### 2 · Matter reaches the people · **S** · position: fix · Arc-2: **no**

**Change.** Two parts, in this order. **(i)** At `loop/matter.py:169`, `eaters = world_q.presence(w,
rid)` reads presence **at that rung only**; a commons site's eaters are the persons under its rung by
`contain` closure (`world.py:197 contain_ascends` is the single owner of the ladder). A commons feeds
the settlement — that is what a commons is. **(ii)** DWELLING/PRODUCER sites key to the
hearth/community they stand on, rather than all to the settlement (`populated.py:357` mints the
community, `:361` the hearth, `:373` the Site — and `:373` hardcodes `f"set_{_slug(sid)}"`).

**Why here.** Because today the two halves of the matter economy never meet. **MEASURED 2026-09-17 on
`build_realm(0)`:** every store is **0 at build time**; after one season the world holds **4,810
units, all of them at the 37 `settlement` rungs, and the 211 `hearth` rungs hold none** — 37 × 130
being exactly one season of `site_yield` (harbour `grain 40 · salt 30`, seam `ore 50 · timber 10`,
`rosters.yaml:1166-1173`). All **46** persons are contained in a `hearth`. All **74** sites key to a
`settlement`. **Sites with anyone present at their rung: 0 of 74.** So `draw = {k: wt * len(eaters)}`
(`matter.py:174`) counts zero eaters at every rung that has stores, and `presence:<site>` has no
referent anywhere.

**Artifact.** `harness/populated.py::census` gains a line, and the numbers are predictable:
**13 of 37 settlements have anybody in their `contain` subtree** (distribution
`1×4, 2×1, 3×4, 4×1, 6×1, 8×1, 10×1`; 46 person-rung pairs), and after one season those 13 hold
**1,690** of the 4,810 units while the other 24 hold **3,120**. With `subsistence_weight
{grain: 2, salt: 1}` (`rosters.yaml`, read via `Fixtures`), part (i) alone makes `draw` non-zero at
those 13 — **92 grain + 46 salt per season against 4,810 produced**. ⚠ **Part (i) alone leaves 24
settlements producing for nobody**; part (ii) is what makes matter reach where people actually are.
Second artifact: `sites with anyone present > 0`.

**Control.** The `site_yield` `none` arm — `sweep: [declared, uniform, none]` (`rosters.yaml:1150`),
whose note is explicit that it is the control and not a third opinion: *"with every cell zero the
economy has no source, every store depletes monotonically, and `W8`'s own proof clause must fail. A
sweep whose control arm cannot break the claim is not a control"* (`:1163-1165`). With the `none`
arm the draw must exhaust the stores; if it does not, the draw is not reading them.

**Cost.** One reader widened, one content key changed. No new primitive.

**Breaks if wrong.** A shortfall today *"emits nothing and decides nothing"* on L5's rule
(`matter.py:179-185`), so a mis-scoped closure produces a silent permanent shortfall rather than a
failure. Assert the draw, not the absence of an error.

**Falsifier.** `test_a_commons_site_draws_for_everyone_under_its_rung` ·
`test_some_site_has_a_person_present_at_its_rung`.

### 3 · `confer` / `revoke` read the office from `subject` · **S** · position 6 (rides) · Arc-2: **no**

**Change.** `_req_confer` and `_eff_confer` both read `payload["office"]`. **`office` is not in
`requires_operands`** — the closed eight are `[actor, subject, from, to, site, kind, amount, floor]`
(`rosters.yaml:1084`) — so `operands_for` can never derive it and `_payload_of` can never carry it.
**Even with H-71 closed, a computed `confer` names no office.** Read it from `subject`, which always
reaches the payload.

**Why here.** It is 4 lines in 2 files and it unblocks `confer` and `revoke` together. The
alternative — a 9th operand `office` — is **S7**: the roster half is free, it loads clean, and it is
**inert** until `_derive_operand` gains a branch.

**Artifact.** A computed `confer` Candidate whose payload names an office. `corpus_run`'s
*"5 foldable but never even attempted (`confer`, `convene`, `destroy_record`, `dispatch`, `revoke`)"*
shrinks — though not on this item alone; item 6 is the other half.

**Control.** A `confer` whose `subject` is **not** an office must still refuse, and refuse for the
office's absence rather than for a missing operand. Assert on which refusal.

**Cost.** Four lines. No new primitive, and it **avoids** one (the 9th operand).

**Breaks if wrong.** `_req_confer` requires `Office.conferral` non-empty; reading the wrong id makes
that check vacuous rather than failing.

**Falsifier.** `test_a_computed_confer_names_its_office_in_subject`.

### 4 · The `add_tenure` object-domain guard for `hold` · **S** · position 12 · Arc-2: **no**

**Change.** `World.add_tenure` (`state/world.py:223`) validates exactly two things: `t.kind` against
the seven `tenure_kinds` (**`:242-247`**, raising `Unowned` under `S15` — ⚠ line repair 2026-09-17,
~~`:239-245`~~ is the tail of the docstring; `02` §A.5.3 carried `:242-247` and was right) and, for a
`contain`, strict ascent (`:248-256`, `Forbidden` under `S10`), then appends at `:257`. **It validates nothing about the object class of a
`hold`.** Add it: a `hold`'s object must be an `Office`, `Rung`, `Record` or `Proposition`, else
refuse in the `S15` idiom.

**Why the guard EARNS its existence.** ⚠ **OWNER: `02` §A.5.3** (unified 2026-09-17 — this block
restated that argument at the same length, and `CLAUDE.md` §8's *every rule lives once* reads the same
way at prose). In one line: **a Tenure is read by the engine on every step** — `hold` edges decide
`decision/budget.py:56`'s action count, `in_holdings` and `under_purview`
(`loop/predicates.py:60-141`), `world_q.footprint` (`:254-273`), `_ch_document_key`'s witness channel
and `_eligible`'s `hold:` branch — so its subject is the edge the game resolves from, not another
guard. The domain is **ratified, not invented**: `holonic_ARCHITECTURE.md:538` types
`hold | Person → Office | Rung | Record | Proposition` and `ARCH §A.3` row 12 restricts the subject to
a Person. **Read `02` §A.5.3 for the full predicate argument and the commons half; this row is the
build step.**

**Artifact.** The guard raises on a planted `Tenure(p, site_id, "hold")`, and
`python -m engine.season.harness.populated` still loads. ⚠ **It will not, unmodified** — see item 8:
16 live `hold` Tenures have a **faction Proposition** as subject, which the subject rule of `ARCH §A.3`
row 12 forbids, so items 4 and 8 land together or the guard reddens the corpus.

**Control.** A `hold` on each of the four admitted classes must still open. A guard that refuses a
`hold` on a `Record` would break `_eff_create_record`, which mints exactly that.

**Cost.** One branch. No new primitive.

**Breaks if wrong.** Too narrow and `create_record` dies; too wide and it is decoration.

**Falsifier.** `test_a_hold_on_a_site_is_refused_at_add_tenure` ·
`test_a_hold_on_each_admitted_object_class_still_opens`.

### 5 · Delete `budget_office_bonus` · **S** · position 14 · Arc-2: **no**

**Change.** `engine/season/decision/budget.py:56-57`:

```python
offices = sum(1 for t in p.tenures if t.kind == "hold" and t.live)
b = k + offices * fx.get("budget_office_bonus")
```

There is **no `w.offices` guard**, so every live `hold` pays — a landholding, a possessed book, a
faction banner. Delete the bonus; do not guard it.

**Why delete rather than guard.** `ARCH §A.3` **row 15** refuses it by name: *"| 15 | `budget`
includes an `office_bonus` | **refused.** A seat's capacity is its establishment — more named
persons, each with their own budget | Stage 3 §A.3 — *no seat carries a bonus* |"* (`:184`). And
`ARCH §B.7`'s invariant table grades *"a seat adds no verb and no modifier"* **STRUCTURAL**. Guarding
the bonus keeps a modifier on a seat that Layer 1 says cannot carry one; deleting it is cheaper and
is what the row asks for. `H-92` (`hole_register.yaml:1106`) is the defect row, and its own
`unblocks` field records that this is **pre-existing and was widened, not introduced**:
`_eff_create_record` already minted a `hold` over a Record, *"so `decision.budget` already counted a
possessed book as an office"*.

**Artifact.** A one-line diff, and `budget` equal for a person holding one office plus one rung and a
person holding one office and no rung.

**Control.** **That equality IS the control, and it is the assertion `H-92` has never had.** Two
persons, identical but for a rung-hold; their budgets must match. Without the control the test passes
on a fixture where nobody holds a rung.

**Cost.** Minus one fixture reader. A **free cut** (§B.2).

**Breaks if wrong.** Scene-action counts fall for anyone who was being overpaid, which moves the
corpus hash. Declare it with the delta; it rides item 1's re-record or takes its own.

**Falsifier.** `test_budget_ignores_held_offices_and_holdings_alike`.

---

## A.4 · Items 6–12 — order-free against Arc 2, no effect body, no gate change

### 6 · `person_side_eligible` reads `remit:` and `presence:` from the holder's own ledger · **M** · position 19 · Arc-2: **no** (the claim's subject is the actor)

`decision/options.py:163-165` declines `remit:<act>` unconditionally and `:166-168` declines
`presence:` on `H-75`, both with a `TRACE.note` so the decline is measurable. **Consequence,
re-measured here 2026-09-17: with a person holding a live `hold` over an office, 10 of the 38 verbs
still cannot be formed person-side** — `confer`, `convene`, `destroy_record`, `determine`,
`dispatch`, `establish`, `issue`, `levy`, `open_case`, `revoke`. **That is the whole governance
surface**: it executes when *handed* an Act and can be **chosen by nobody, in any world**. `H-71` (`hole_register.yaml:795`, tier 0) is the row, and **arm 1 (the
decline) was never decided** — it is what the instrument did when §F1 was silent.

**Repair, shaped to survive AX-2.** The `confer` Event carries the conferred seat's `remit.acts`; the
witness step mints the conferee's firsthand claim of it (`loop/witness.py:175` mints only `firsthand`
/ `firsthand_via_knot`, so this is the existing channel — ⚠ existing *channel*; the deposit's predicate is `e.kind`, `witness.py:191`, so the remit-claim SHAPE is a new deposit rule, `01` §A.6, 2026-09-17); `person_side_eligible` then evaluates
`remit:<act>` from the person's **own ledger**. ⚠ **`ARCH §C.3` binds `engine/season/decision/` by
PATH** — no `World`, as an import, a name, an attribute or a string — so a reader added here must
take a snapshot. That is what makes the ledger arm the arm that fits and the Query-over-`via.scope`
arm position 6's work. **Do not ride `Tenure.payload`:** `ARCH §B.8` retires it in favour of `term?`,
and it is one of the 10 producerless RES rows (measured below).

**Artifact.** A seated holder forms a `confer`/`issue` candidate; a non-holder does not.
**Control.** The same run with the office's `remit_acts` **emptied**: the candidate must not form.
Without it the test passes on a fixture that admits everything.
**Falsifier.** The existing `test_no_person_can_choose_a_governance_verb_and_h71_is_why`
(`engine/season/tests/test_season_shape.py:4992`) **goes RED** — which `H-71`'s own row nominates —
and is rewritten as the control.

### 7 · Both-direction band crossing · **S** · position: fix · Arc-2: **no**

`loop/matter.py:262` is `if before >= floor > s.condition:` — downward only. A site whose condition
**rises** past a floor raises no question, so a repaired place cannot be noticed. Add
`before < floor <= s.condition`. **Artifact.** A Q3 question after a `restore`. **Control.** The
downward case must still fire exactly once per edge (the emission is `w.crossings.append` at `:272`
plus one Event at `:267-270` and the log append at `:271`; a both-direction test that double-counts is worse than none).
**Falsifier.** `test_an_upward_band_crossing_emits_once`. **Note.** This is AX-5 motion 1 and needs
no ruling; see §C.5 row 8.

### 8 · The 16 faction-subject holds become the seat-holder's · **S (content)** · position 12 · Arc-2: **no**

`harness/populated.py:613-618` mints, per province, `Tenure(f"t_hold_terr_{tid}",
f"fac_{_slug(held_by)}", f"terr_{tid}", "hold", 0)`. **Measured at build time: 35 live `hold`
Tenures — subjects person **19**, faction-Proposition **16**; objects office **19**, rung **16**,
site **0**.** `ARCH §A.3` row 12 makes `hold`'s subject **a Person, only**, and `AX §D.11` (`:1054`)
makes `Faction.holdings` *"the union of its members' holds"* — a **derived** field, so a faction
holding directly is a second home for the same fact. The file's own comment concedes the defect
(*"the starting-control table names an owner per PROVINCE and never a person… The declared defect is
§54's, not repaired here"*, `:605-607`). This is a **content defect, not a design choice.**

**Repair.** The 16 become holds by the PERSON who holds that territory's seat, with the faction
relation expressed as that person's `commit`/`oblige`. That keeps the 46-NPC roster of ED-WR-0011
intact; minting persons is the fallback and would re-open that ruling.
**Artifact.** hold subjects: person 35 / faction 0. **Control.** `world_q.footprint` must return the
same rungs for each faction afterwards — it already unions holds and members' presence
(`world_q.py:254-273`), so a correct repair is footprint-neutral. That is the assertion that
distinguishes a repair from a deletion.
**Falsifier.** `test_no_hold_tenure_has_a_faction_subject` · `test_footprint_is_unchanged_by_the_hold_rehoming`.
**Pairs with item 4** — see that block.

### 9 · The site-kind roster tranche · **S per kind** · position 24 · Arc-2: **no**

Five families as `site_kinds` members, each landing with its `wear_per_season` rate **and** its
`band_floors` cell in the same commit (**L28/L29** — the load is the falsifier), plus a `site_yield`
cell per productive kind (**L30**) ~~and `regrowth: 0` rows for built kinds so item 7's upward crossing
is not confused with regrowth~~ (⛔ struck 2026-09-17: no `regrowth` table exists and nothing would read one — `02` §C.2; the guard against unauthored regrowth is a sign assertion over `(Site, condition)` writes by step, not a row). **Artifact.** The loader green with 8 site kinds.
**Control.** `band_floors`' declared sweep (`rosters.yaml:1179`): the offered-use set from
`world_q.verbs` must change under `halved`/`doubled`. **Falsifier.** the import itself ·
`test_built_kinds_do_not_regrow`. ⚠ `body` is on `site_kinds` and **is not a site** — it is
`(Person, body)`'s band row riding the same table (`rosters.yaml:814-816`). Do not model against it.

### 10 · `world_q.verbs` wired into the fold · **M** · position 22 · Arc-2: **no**

`world_q.verbs(w, site, floors)` (`:133`) computes *what this site currently offers at its condition
band*. **Measured: it has zero callers under `loop/`.** Its only callers are five sites in
`harness/probes.py` (`:678`, `:683`, `:1509`, `:1515`, `:2241`). So the set of uses a place offers is
computed by probes and by nothing the game runs — and the use-verbs are **not** verb-table rows
(`rosters.yaml:1182-1185` says so and says the table is therefore not validated against
`verb_table.yaml`), so a person cannot choose one. **This is the licensed shape, not the forbidden
one**: a wear clock that crosses a floor nobody can read is scenery, which is R4's own falsifier.
**Artifact.** A caller under `loop/`. **Control.** `band_floors` halved/doubled changes the offered
set. **Falsifier.** `test_the_loop_reads_the_offered_use_set_from_the_roster`.

### 11 · `Rung.sites` deleted · **S** · position: fix · Arc-2: **no**

**Measured: it has no production reader.** `Rung.sites` appears in `_DECLARED`
(`state/carriers.py:568`) and in the `__init__` default (`:577-578`); the only other mention outside
tests is `loop/matter.py:197-199` telling the reader **not** to use it: *"THE SITE'S OWN `rung`, NOT
THE RUNG'S `sites` LIST. The first version read `r.sites`, and that list is a BACK-REFERENCE NOTHING
MAINTAINS — it is empty for every rung in the corpus, so the whole yield step was INERT."* And there
is **no `(Rung, sites)` write_matrix row** — measured over all 40 rows; the Rung rows are `dates`,
`envelope`, `exists`, `stores`, `yield`. `world_q.footprint` derives the relation from `Site.rung`.
A clean cut. **Artifact.** the whitelist diff. **Control.** `matrix_rows_without_a_field()` must
return the same two keys (`{"absent", "unmodelled"}`) afterwards — the existing shape assertion at
`test_season_shape.py:3093` is the baseline. **Falsifier.** `test_rung_has_no_sites_field`.

### 12 · `capacity(w, rung)` as a Query with a floor · **S** · position 24 · Arc-2: **no** · **GATED on ED-SE-0051**

A Query over DWELLING sites, never a fixture row, with a floor so it does not break at the extreme
(NERS R's completeness half). **Gated, not blocked-by-order:** it is the capacity arm of
`ED-SE-0051`. **Artifact.** the Query plus a named consumer. **Control.** the `uniform` arm — a
`capacity` that does not move between `declared` and `uniform` was never deciding anything.
**Falsifier.** `test_capacity_has_a_floor_and_no_magnitude_field`. ⚠ `Rung.__setattr__` refuses a
magnitude field structurally (R11), and **R7** rules it out anywhere: *"no magnitude carrier is
admitted at any scale. Every aggregate is DERIVED, none is PUSHED"*
(`references/design_rulings_2026-09-06.md:169` — ⚠ line repair 2026-09-17, ~~`:168`~~; `02` carried `:169` and was right). So this is a Query or it is nothing.

---

## A.5 · Items 13–23 — the Arc-2-flagged, and the ones that wait on a reading

### 13 · Policy as a dispensation Record + `in_force` + `reach` + `@effect_for("issue")` · **M** · positions 15, 19 · Arc-2: **YES** (effect body)

A `Record` of kind `dispensation`, opened by `issue`, held by the issuing holder, with operands
`scope` (a RungId), `clause` (one of seven) and `terms` (an OUGHT Proposition). `in_force(w, rung,
clause)` walks `contain` ancestors upward and returns the first live row whose `scope` is an
ancestor-or-self; a superior may declare `reach: all`. **Each gating clause must map to one of the
seven `requires_forms`** with a Query behind the predicate (`sit` → `relation`; `levy` →
`scalar_threshold`; `admit` → `contain_path`; `hear` → `relation`) — a clause that fits none is an
eighth form and **refuses at load** (L1), which is the one genuinely STRUCTURAL question this subject
could raise and today does not. ⚠ **`Dispensation` has no dataclass** (measured: the name appears in
`write_matrix.yaml:112` and in `hole_register.yaml`, and in no Python class), which is why
position 15's Record-kind fold is the carrier. **Artifact.** `issue` resolvable; a hearth's MATTER
step reads the province's `draw` row. **Control.** the same world with the provincial row absent —
the option set at the hearth must differ. **Falsifier.**
`test_a_provincial_draw_policy_is_in_force_at_a_hearth` · `test_nearer_policy_wins_unless_reach_all`.
**Ruling.** the comparator is **RR-1** (§C.4).

### 14 · The works Record kind + one emission rule · **M** · position 15 · Arc-2: **no** (`create_record` exists)

A `Record` of kind **`works`** (`01` §A.12's noun, binding on the suite — never *a work*, which is the live verb, and never *a project*) with `stages`, opened by the existing `create_record`, maturing at MATTER
(`Record.matured`). `stage.stalled` when the stage's `draw` is short, `docket.lapsed` when a date
passes unconvened, the cell going STALE — **ONE emission rule, three uses**. A `cardinality` conjunct
bounds it to one live works per site, and a `ttl` terms operand ends it. **No `undertake` verb**
(§B.4). **Artifact.** a works Record matures under MATTER. **Control.** a stage whose draw is met
must emit nothing — a lapse rule that fires on a healthy stage is a clock, which `T-c` refuses.
**Falsifier.** `test_a_short_draw_stalls_the_stage_and_emits_once`.

### 15 · `@effect_for("restore")` + `ceiling(w, site)` · **S** · position 7 · Arc-2: **YES**

The `restore` row is complete at `verb_table.yaml:448-467` — `own | presence:<site>`, a typed
`all[existence(site, Site), relation(site, present_at)]` cell, `writes: ["Site.condition"]`,
`emits: ["site.restored"]`, `grade: "ruled"` — and its `effect:` **formula is already in the row**
at `:465` (⚠ line repair 2026-09-17: ~~row `:448-466`, formula `:464`~~ — `:464` is `grade:`; `02`'s
appendix carried the right numbers and this file's did not): `Δ = +(1 − condition) × f(degree) × share`. What it lacks is a body, which is R1: no
`@effect_for`, so `resolvable_verbs()` excludes it. The formula's source is **`holonic_ARCHITECTURE.md:1898`, §54
item 7**, which folds in *"restoration's mirrored form"* and lands it at §27.1 — *"The mirror gives a
dead site a road back."* ⚠ **`share = 1` is the SPECIAL case, not the general one, and OWNER of the reading is `02` §A.5.2**
(unified 2026-09-17): the commons arm is `10_SUPERSEDING.md:1275-1279` — *"At a commons with many
drawers, single-act closure is impossible… Closure is a collective outcome"* — and the single-drawer
arm is **`:1280-1282`**, *"`share = 1`, and one Overwhelming season moves a quarter of the
condition."* ~~Citing `:1275-1281` as one span~~ runs the two together, and a `restore` body written
against the single-drawer arm alone **deletes the commons as a category**. Both halves or neither. **Artifact.** condition rises; `VERBS THAT EXECUTED`
gains `restore`. **Control.** `§27.3`'s sum-then-clamp-once accumulator (`loop/resolve.py:551-553`)
already makes `Site.condition` order-independent across the fold, so several repairs and several wear
sources in one season must compose to the same value in any arrival order. Assert that.
**Falsifier.** `test_restore_mirrors_decay_and_stops_at_ceiling`.

### 16 · `found` · **M** · positions 7, 24 · Arc-2: **YES**

`(Rung, exists)` (`write_matrix.yaml:294-300`: `steps: [RES]`, `class: ACTS`, `social: "true"`,
`emits: rung.founded`, `by: "W2/H-41 — founding a hearth"`) and `(Site, exists)` (`:322-328`) are
live rows with **zero producers**. `ARCH` **§F.20** (`:1082`) is the gap in terms: *"no stage names a
verb that founds a hearth or builds a site… the world only decays"*. `social: true` is **correct
as-is** — founding is an act — and `contain_ascends` already refuses a hearth inside a hearth (R9).
**Artifact.** the producerless RES count drops by 2, from a measured **10** to 8. (Reproduce with the
command in `write_matrix.yaml:38-42`; its own header says eleven and projects nine, and **both
figures are stale — it is 10 today**, because `Date.fired` was repaired in place and neither
`Person.beliefs` nor `Tenure.payload` has been deleted.) **Control.** **conservation** — total store
mass across every rung before and after must be equal minus the stake. ⚠ `F10`'s existing checker
cannot see this failure because it never runs `found`; it must be **re-pointed, not cited**.
**Falsifier.** `test_found_is_the_producer_for_rung_exists` ·
`test_a_founded_rung_conserves_matter_minus_the_stake`. ⚠ **A founded Rung has no closer** —
`release`'s domain is `tenure_kinds \ {contain}` and a Rung is not a Tenure — so an abandoned hearth
is a grain tomb. Either a `(Rung, exists)` destroyer (**S**, mirrors `destroy_record`) or a MATTER
rule re-homing its stores (**M**, lawful because `Rung.stores` is `social: false`). Decide in the
same commit or the artifact is a leak.

### 17 · Q5 `purview` question source · **S/M** · position 19 · Arc-2: **no**

ONE new `question_sources` row (`rosters.yaml:250-270` — `open: true` at `:252`, `ordered: true` at `:253`, values
`[date_due, claim_landed, band_crossed, need]` at `:270`): **Q5 `purview`**, raised for the holder of a seat
when a band crossing or a landed claim concerns a rung under `under_purview(seat)`, claim-gated.
**This is the ceiling on both subjects and nothing in the ratified 27 touches it:** a person can only
ever choose about a referent one of four sources supplies, and `questions_for` (`world_q.py:439`) has
exactly four. **Artifact.** the question appears for the Count and for nobody else. **Control.** a
seat whose `scope` does not reach the rung must raise nothing. **Falsifier.**
`test_a_holder_is_asked_about_a_crossing_under_purview`. **Convention.** the roster's own note says
*"ORDER IS SEMANTIC"* and that within one source the tiebreak is `q.id` — and measured over 89
baselines, *"the leading source is SHARED with at least one other question in 801 of 1,068
deliberations"* (`rosters.yaml:260-269`). So Q5's position in the order decides less than it looks
like it does. Say so; do not build a rule for it.

### 18 · The ENCLOSURE bypass reading on `move`'s `contain_path` conjunct · **S** · position 22 (obstacle part only) · Arc-2: **no**

`move` is refused by its `contain_path` conjunct when an enclosure above its floor lies on the path
and the mover is not admitted (the `admit:` clause of the rung's in-force policy). **A reading, not a
mechanism** — no new form, no new stem. **Artifact.** the refusal TRACE. **Control.** the same path
with the enclosure below its floor must admit. **Falsifier.**
`test_move_through_a_standing_enclosure_is_refused_unless_admitted`. ⚠ **The obstacle contribution is
a different item and it waits**: `H-127` (`hole_register.yaml:923`) is live and `sigma_leverage` does
not own the obstacle, so a second contributor lands in the middle of an open single-owner dispute
(§B.4).

### 19 · `Act.via`; the `is_title` branch and three helpers deleted; `establishment` → Query; `judging_set_rule` gone · **L** · position 6 · **IS the gate**

`Act.via` appears **nowhere** in `engine/season/*.py`. The four purview readers that must be
re-pointed are all in one file — `in_holdings` (`loop/predicates.py:60`), `under_purview` (`:105`),
`titles_held` (`:144`), `highest_title_rank` (`:157`) — which is why position 6 sizes it small. The
`is_title` branch is at `predicates.py:252-254`, and `ARCH §B.7` call 1 forbids it in terms: *"**No
`is_title` branch exists anywhere** — ID-4"* (`AX:443`). `Office.establishment` is a stored field
(`state/carriers.py:491`) read at `world_q.py:413`; `ARCH §B.7` call 2 makes it a Query over `oblige`.
`judging_set_rule` is still in `Rung._DECLARED` (`carriers.py:568-569`); `ARCH §A.3` row 7 deletes it.

⚠ **AND POSITION 6 MUST WRITE THE FOURTH F3 CASE.** `ARCH §C.2`'s F3 (`:523-540`) admits `actor ==
subject` (T-m), a `term` maturation (T-n), `via` with a **`revocation`** basis (T-o), and the destroy
cascade — and **a conferral-basis opener matches none of the four.**
`proposals/2026-09-05-proceedings-subsystem/04_VERBS.md:352-357` files it: *"So does `confer`, today,
which is an `IN`-lane defect this design reveals rather than causes."* Counting these two subjects
there are **five** shapes needing it — `confer`, `revoke`, `kill / wound`, `determine` and any
`capture` — so it is written **once, generally, at position 6**, or it is written twice (`_part2`
says so at both 6 and 19). ⚠ **`kill / wound` is NOT the fourth case**: it writes another's Tenure
through the destroy cascade, which is already ground four, and the built gate half-enforces it
(`world.py:374`'s `caused_person_exists`). **Falsifier.** position 6's own: a `T-o` write whose `via`
names a seat whose basis does not reach the edge must raise.

### 20 · `Tenure.term?`; `payload` deleted · **M** · position 6 · Arc-2: gate

`state/carriers.py:59` still declares `payload: Any = None`; `ARCH §B.8` replaces it with `term?`.
`Tenure.payload` is also one of the 10 producerless RES rows (measured), so this closes a matrix row
and a field together. ⚠ **`Tenure.conferrer` is already deleted** and the comment at `carriers.py:48-57`
is the precedent and the reasoning: *"It occurred EXACTLY ONCE in the whole tracer — this line — and
reached no reader, which by `ID-13` is not a weak field but one that does not exist… AND THE DELETION
OPENS NOTHING… A field here would be a second home for a fact the act already holds — `ID-2`."*
**Nothing in either subject may ride `payload`.**

### 21 · the SURFACE LAW's declared read licences; the WITNESS channel carried through the fan so `inferred` has a producer · **M / M** · positions 4, 7 · Arc-2: **no / no**

`inferred` is a rostered `claim_sources` member (`rosters.yaml:136`) with **no producer** — re-measured
2026-09-17: the string `"inferred"` does not occur in **any** `.py` in the repository, and
`loop/witness.py:175` mints only `firsthand` / `firsthand_via_knot`.

⛔ **STRUCK 2026-09-17.** ~~"Its producer is an EFFECT of `thread_read`, which is Arc-2-flagged."~~
Inherited from the reconciling plan and **overturned by `03` §A.6.2 on two grounds this file did not
check.** (1) `thread_read` is **not resolvable** and its own row says why (`verb_table.yaml:697`,
`H-85`), so that would put the producer on a verb nobody can attempt. (2) **`ARCH §C.6:735` already
rules the producer** — the `post_remit` channel mints the change claims `inferred`, RATIFIED
2026-09-05 — so there was never a producer to choose. **The repair is a WIRING change, not an effect
body:** `witness()` builds its fan as `[(pid, e, mode) …]` (`loop/witness.py:104-105`) and the third
element is the fan-out MODE, not the channel, so the channel that admitted each person is discarded
before the deposit. Carry the channel instead and dispatch `src` off `ARCH §C.6`'s five-row mint
table. **This also drops the item's Arc-2 flag**, since it opens no Tenure and writes no effect.
`ARCH §C.3`'s companion half — `assemble` with a declared read list — is unchanged. Owned by
`03_THE_SURFACE.md`; listed here for the order.
**Falsifier.** `test_assemble_reads_only_the_declared_list` ·
`test_a_post_remit_only_witness_holds_an_inferred_claim` (with its control: a `co_located` one does
not) · `03` §PART D's `SU-12`, which is written to GO RED.

### 22 · The delivered/demanded gap as a BAND on a Query · **M** · position 22 · Arc-2: **no**

⚠ **`Office.upkeep` has NO READER — measured**: a grep for `.upkeep` and `.binds` across
`engine/season/**/*.py` excluding tests returns nothing, and `ARCH` §F.18 (the upkeep source) is open.
So *"legitimacy decays through upkeep"* is **dead as stated, not a cut** (§B.3). The replacement is
`AX` ID-17 (`:631`) and `T-b` (`:284`): a gap read as a band on a Query that changes **which options
a subject sees** (`repudiate`, `defy`, `petition`) and never an outcome. **No field.**
**Falsifier.** `test_a_gap_changes_options_not_outcomes`.

### 23 · `character(w, rung)` · **S** · last · Arc-2: **no**

Ship **only with a consumer named**, or not at all. See §B.4's `population()` row for the precedent:
a Query with no consumer was ordered deleted from an earlier proposal's *Adds* as a false N-line
that the proposal itself had marked `[GAP: no consumer]` and still counted.

---

## A.6 · THE WHOLE ORDER, IN ONE TABLE

| # | item | size | Arc-2 | pos. | falsifier |
|---|---|---|---|---|---|
| 1a | Q3's referent becomes the site id | S | no | fix | `test_q3_a_band_crossing_raises_a_question_about_the_site_not_the_verb` |
| 1b | a world in which a floor is crossed | S | no | fix | `test_some_site_is_below_a_floor_in_the_built_world` |
| 2 | matter reaches the people (commons closure; fabrics keyed to the hearth) | S | no | fix | `test_a_commons_site_draws_for_everyone_under_its_rung` |
| 3 | `confer`/`revoke` read the office from `subject` | S | no | 6 (rides) | `test_a_computed_confer_names_its_office_in_subject` |
| 4 | `add_tenure` object-domain guard for `hold` | S | no | 12 | `test_a_hold_on_a_site_is_refused_at_add_tenure` |
| 5 | delete `budget_office_bonus` | S | no | 14 | `test_budget_ignores_held_offices_and_holdings_alike` |
| 6 | `remit:`/`presence:` from the holder's own ledger | M | no | 19 | H-71's own test **goes RED** |
| 7 | both-direction band crossing | S | no | fix | `test_an_upward_band_crossing_emits_once` |
| 8 | 16 faction holds → the seat-holding person | S | no | 12 | `test_no_hold_tenure_has_a_faction_subject` |
| 9 | the site-kind roster tranche | S/kind | no | 24 | the import itself (L28/L29) |
| 10 | `world_q.verbs` wired into the fold | M | no | 22 | `test_the_loop_reads_the_offered_use_set_from_the_roster` |
| 11 | `Rung.sites` deleted | S | no | fix | `test_rung_has_no_sites_field` |
| 12 | `capacity(w, rung)` with a floor | S | no | 24 | `test_capacity_has_a_floor_and_no_magnitude_field` |
| 13 | policy: dispensation Record + `in_force` + `reach` + `issue` effect | M | **YES** | 15, 19 | `test_a_provincial_draw_policy_is_in_force_at_a_hearth` |
| 14 | works Record kind + one emission rule | M | no | 15 | `test_a_short_draw_stalls_the_stage_and_emits_once` |
| 15 | `restore` effect + `ceiling` | S | **YES** | 7 | `test_restore_mirrors_decay_and_stops_at_ceiling` |
| 16 | `found` + its closer | M | **YES** | 7, 24 | `test_found_is_the_producer_for_rung_exists` |
| 17 | Q5 `purview` question source | S/M | no | 19 | `test_a_holder_is_asked_about_a_crossing_under_purview` |
| 18 | ENCLOSURE bypass on `contain_path` | S | no | 22 | `test_move_through_a_standing_enclosure_is_refused_unless_admitted` |
| 19 | `Act.via` · F3's fourth case · `is_title` + 3 helpers gone · `establishment` → Query | L | **IS the gate** | 6 | position 6's own |
| 20 | `Tenure.term?`; `payload` deleted | M | gate | 6 | `HANDOFF.md` row 6's |
| 21 | declared read licences; the WITNESS **channel** carried through the fan → `inferred` (~~`thread_read`~~, struck) | M / M | no / no | 4, 7 | `test_a_post_remit_only_witness_holds_an_inferred_claim` |
| 22 | the delivered/demanded gap as a band | M | no | 22 | `test_a_gap_changes_options_not_outcomes` |
| 23 | `character(w, rung)` | S | no | last | only with a consumer named |

**Items 1–12 are cheap, unflagged, and mostly fixes.** A session may land them one commit each
(`[fix]`, `[simulation]`, `[design]` for item 1's ruling-shaped half). **13, 15, 16 ~~and 21b~~ wait on
19 and 20** (21b's flag was dropped at item 21 and this sentence had not followed; corrected 2026-09-17)**.** ⚠ **Nothing in this table marks a juncture done** (§0.2); a juncture is done when
something runs it and prints.

---

## A.7 · THE VERIFICATION CADENCE — stated because a reader of a build order is exactly the person about to get this wrong

`CLAUDE.md` §0.4, ruled: the full suite is a **CLOSE step, not an inner loop.**

| when | what |
|---|---|
| after this commit's **last** edit, immediately before the commit | `python -m pytest tests/valoria -q -n auto` — **once per commit**, ~2m36s. Serial it is 9m01s for the identical 1817 tests |
| mid-session, after an edit | `python -m pytest tests/valoria/test_<the one file covering your edit>.py -q` — seconds |
| a red close run | re-run **the failing file only** while you fix it; the full suite comes back once, when you believe you are done |
| anywhere, freely | `python tools/valoria_local.py --staged` — it does **not** run pytest and never has, so local-green ≠ CI-green |

**This governs every pytest gate, not just `tests/valoria`.** `engine/season/tests` (CI runs it
`-q -n auto` at `.github/workflows/valoria-ci.yml:383`) and `engine/tests` take the same cadence:
at the close, once, and **only the ones your change can reach.** Items 1–5 and 7–12 touch
`engine/season/` and so need `engine/season/tests`; none of them can reach `engine/tests`, so
"run everything just in case" is exactly the habit §0.4 exists to end.

**Two container facts, so nobody debugs their clone.** A **shallow** checkout cannot reach the
commits `FORK:` rows name, so `tests/valoria/test_forked_status.py` fails two tests on arrival —
`cat .git/shallow` settles it. And `requirements.yaml` carries **four mutually inconsistent R3
figures** with nothing saying which is the baseline: **re-run, never quote.**

---

# PART B · WHAT THIS ADDS AND WHAT IT MAKES UNNECESSARY

The bar is `ARCH` PART D row 1 / `AX` ID-13 — a dead carrier is refused, so every addition owes a
reader and a removal.

## B.1 · Adds

| added | new primitive? | why not |
|---|---|---|
| `found` | one verb row + one effect | the matrix rows `(Rung, exists)` and `(Site, exists)` already exist with zero producers (`write_matrix.yaml:294-300`, `:322-328`); `ARCH` §F.20 asks for the verb by name |
| `@effect_for("restore")` | **no** | the row exists at `verb_table.yaml:448-467` with its `effect:` formula already in it at `:465` |
| `in_force`, `capacity`, `ceiling`, `character` | four Queries | `ARCH §A.2`: `world_q` owns nothing. A Query adds no carrier, and R7 requires exactly this shape |
| Q5 `purview` | one roster row | `question_sources` is `open: true` (`rosters.yaml:252`) and already gained Q4 once |
| five `site_kinds` families | roster rows ×3 each | L28/L29's coordinated triple; a data edit, and Jordan ruled this surface *"must be easy to modify"* |
| the conferral claim carrying the remit | **no** | rides the existing `firsthand` channel at `witness.py:175`; writes no field |
| the delivered/demanded gap as a band | **no** | `AX` ID-17 + T-b; a reading of a Query, not a carrier |
| `reach: all` | one **terms operand** on the dispensation Record | not a column, not a field — an operand on a Record the fold already carries |
| the `hold` object-domain guard | one branch in `add_tenure` | it removes a class of silently-wrong edges; see item 4 for why it clears §0.1 pt 5 |
| `dispensation` and `works` as Record kinds | **no** | already owed by ratified position 15 |

## B.2 · Makes unnecessary — the free cuts, each at zero game cost

`Rung.sites` (no production reader; no matrix row — **measured**) · `budget_office_bonus`
(`ARCH §A.3` row 15 refuses it by name) · the `is_title` branch plus `titles_held`,
`highest_title_rank` and `title_domain`'s use as a discriminator (`ARCH §B.7` call 1, `AX` ID-4) ·
`Office.establishment` **as a field** (`ARCH §B.7` call 2 — a Query over `oblige`) · `Tenure.payload`
(`ARCH §B.8`; also one of the 10 producerless RES rows) · `judging_set_rule` (`ARCH §A.3` row 7) · the
two person-side TRACE declines (item 6) · `domain: RungId[]` (§C.5) · the 16 faction-subject holds
(item 8) · `undertake` as a verb (it is a Record kind plus a stage template) · and **every "+N to a
roll" reading of policy** — policies change OPTIONS, never outcomes (`AX` T-b).

## B.3 · Disqualified as cuts — say so, because each looks like one

| looks cuttable | why it is not |
|---|---|
| `fort_level` | ⚠ **OWNER: `02` §A.3.3** (unified 2026-09-17). **DERIVED** (`engine/autoload/game_state.py:322-324`) **and exported as an authored descriptor key** — ⚠ *not* `tools/registry.py:93`, which is a docstring: the row is `references/descriptor_registry.yaml:94` → `engine/engine_params/descriptors.json:143`, behind `tools/export_descriptors.py --check`, **blocking** at `.github/workflows/valoria-ci.yml:137`. `02`'s own appendix repaired that citation and this file carried the unrepaired one. Neither a free cut nor breakage. Leave it |
| `facility_tier` | ⚠ **OWNER: `02` §A.3.3.** **read live** (`systems/settlements/sim/registry.py:97`), **set by its own loader** (`:146`), same blocking export. Same standing |
| `Office.upkeep` | **dead, not cut** — no reader (measured), and `ARCH` §F.18 is open. It is *replaced* by item 22, which is a different claim from *removed* |
| `wound` widened to `Site` | **deferred**, not refused — position 22, behind `H-127`'s single-owner dispute |
| `hold` reaching `Site` | **refused**: `holonic_ARCHITECTURE.md:538` types the object domain and `Site` is not in it. What is held is the RUNG the site keys to, or the works Record on it |
| the destroy-cascade licence for the plot/fabric ontology | **unsound.** `ARCH §B.8`'s T-o cascades Tenures on a dead object; it says nothing about which objects may exist. The ontology stands on **CARDINALITY** instead (`holonic_ARCHITECTURE.md:449-451`, node-keying refused; one Site per kind per rung today at `populated.py:373`) |

## B.4 · WHAT NOT TO BUILD — `CLAUDE.md` §0.1 pt 5's predicate, applied

> *A pattern defect earns a guard only if the defective artifact is load-bearing on **the game**, the
> **exported params**, the **port**, or the **`needs_jordan` queue**. A pattern defect in an artifact
> load-bearing only on this repository's process is not evidence the artifact needs a guard; it is
> evidence the artifact can be wrong without cost.*

| tempting | **FORBIDDEN**, and why |
|---|---|
| a guard that every `[RES]` matrix row has a producing verb (invariant 2) | its subject is `write_matrix.yaml`, a process artifact — and the design **needs** some rows producerless. `rows_without_a_producer`'s own docstring: *"`(Person, convictions)` has no verb because Part E carries no argument verb, which is a gap in Part E, not a reason to delete a row #353 mandates."* **A guard here would condemn a row canon requires.** Add the producer or leave the report a report |
| a guard over unknown verb-table columns (invariant 10 / **S1**) | its subject is the loader. If a column matters, give it a **reader** — an unread column is ID-13 and no checker fixes that. `scale:` is living this exact life |
| a checker that `ARCH`'s enforcement grades are honest | a guard whose subject is another guard — §0.1 pt 5's own named forbidden case |
| a freshness or coverage checker over `hole_register.yaml` | its subject is the register. `register.py --check` exists; a second instrument over it is §0.3's loop |
| a `governance_modes` / `power_bases` roster | **both were BUILT AND DELETED**, in `rosters.yaml`'s own words: *"They were not wrong; they were UNREAD — nothing in the loop or the office schema consumed either."* Do not re-mint them |
| the other 22 faction organs | *"NOT ONE IS READ by anything that builds a world… They go in the day a seat needs one"* |
| `population()` / `faction_value` / `character()` with no consumer | a Query with no consumer is a false N-line. An earlier proposal was ordered to **delete** exactly this from its *Adds* |
| a second `band_floors`-shaped table for a non-site quantity | `band_floors`' outer key is validated against `site_kinds` (L28). It needs a **dedicated fixture**, one line — not a guard |
| a magnitude field on a `Rung` | against **R7** and against `Rung.__setattr__` (R11). Not apparatus — just wrong |
| a siege subsystem · a fortification obstacle before position 22 | `H-127` is live and the obstacle's owner is disputed (§A.5 item 18) |
| `raze` / `build` / `repair` / `convert` / `garrison` / `undertake` as verbs | `restore` + `found` + a Record kind cover them. Five rows where two suffice is the `governance_modes` shape again |
| a policy-effects readout ("+N") · a legitimacy field · `domain: RungId[]` · a `Tenure.payload` revival · a per-edge council grant | each refused above or in §C.5 |
| an eighth `requires` form without a STRUCTURAL ruling | L1 refuses it at load, and the refusal is the design statement |
| **a cadence checker or a citation checker** | §0.4 and §0.1 pt 3 both say in terms that their subject is a reader's discipline and **no guard may be built** for it |
| **an `audit/` file, or a findings document, from the adversarial pass** | §0 retires `audit/` as a category. The pass's output is **edits to the thing under review and at most one commit-message paragraph** |

**And one thing that IS licensed, so the predicate does not read as a ban.** A guard whose subject is
the **game** or a **ratified loader invariant** earns its keep: the `hold` object-domain guard (item
4); a test that a computed governance act carries an office (item 3); a test that a founded rung
conserves matter (item 16); a test that a lost capture writes nothing; and the **planted-violation
tests for `ARCH`'s twelve loader invariants that ratified position 23 already schedules.**

⚠ **The reroute to watch.** Forbid the guard and a session writes **a finding** instead, because the
carrier is prose. Nothing in §B.4 is a thing to *file*. If work on these subjects finds a defect
outside its own load-bearing path: **fix it in that commit, or drop it.**

---

# PART C · THE THREE QUESTIONS

## C.1 · Who owns this?

| the thing | owner |
|---|---|
| the ORDER across all lanes | `workplans/2026-09-11-reconciled-program.md` §3, **RATIFIED 2026-09-12 (ED-IN-0215)**, scoped to §3's order and §1's supersession verdict and nothing else. This file **places items into** that order and owns none of it |
| the gate's F3 branch, `Act.via`, the four purview readers | **position 6, exclusively.** *"This position is the only place the gate's F3 branch is authored"* |
| the effect contract | **position 7** |
| the closed sets | `engine/season/rosters.yaml`, read at runtime — mechanism under §0.05 |
| the write schema | `engine/season/write_matrix.yaml`, one row per `(kind, field)` (L23) |
| what a `FORK:` row resolves to | `tools/pathres.fork_pointer()` |
| the ladder | `World.contain_ascends` (`state/world.py:197`), single owner |
| the seven precondition forms | `rosters.yaml:1086-1122`, **closed at seven**, refusing an eighth at load |
| this file | nobody, after it is read. It is reference (§0.05): delete it and the game behaves identically |

## C.2 · What can check this?

| claim | grade | the construction |
|---|---|---|
| an eighth `requires` form cannot ship | **STRUCTURAL** | `data/requires.py:549-554` refuses at load, independent of the roster |
| `capability` never gates a verb | **STRUCTURAL** | `data/verbs.py:311-315` refuses **by name**, even if rostered |
| a `hold` never reaches a `Site` | **MECHANICAL** (once item 4 lands) | one branch in `add_tenure`. Today: **nothing** — the object class is unchecked |
| a Rung carries no aggregate | **STRUCTURAL at the type** (R11), **CONVENTION at the schema edit** | `ARCH §B.3`'s own grading: *"a session can add a field. What it cannot do is add one without a matrix row"* |
| a new `[RES]` row has a producer | **CONVENTION** — report-only, and it is **S3** | `rows_without_a_producer`'s only caller asserts the shape |
| an unknown verb-table column is refused | **NOTHING** — invariant 10 is unbuilt (**S1**) | give the column a reader instead |
| `decision/` sees no World | **STRUCTURAL by path** | `ARCH §C.3`, plus the AST test `test_w5_sense_is_still_the_only_world_taking_non_decision_function` (`test_season_shape.py:2514`) |
| adding a building kind is three coordinated edits | **MECHANICAL** | L28/L29, both directions (`data/fixtures.py:106-123`) |
| Q3's referent is a place | **MECHANICAL** (once item 1a lands) | one unit test on `questions_for` |
| policies change options, never outcomes | **CONVENTION** | `AX` T-b is a rule about what a threshold may do; no code refuses a `+N`. State it and review for it |
| the verification cadence is followed | **CONVENTION, and no guard is permitted** | §0.4's own sentence: *"the enforcement is that you read it"* |

## C.3 · Whose act makes it happen?

| step | whose act |
|---|---|
| item 1's design edit on H-110's shape | a session's, in a commit that names the three dependent rows and re-records the goldens once |
| items 2, 4, 5, 7, 8, 11 | a session's, one commit each, no ruling |
| item 6 | a session's — and it makes an existing test go red, so the commit that lands it also rewrites that test as the control |
| items 13, 15, 16, 21b | a session's, **after** positions 6 and 7 land. Building them earlier means building them twice |
| item 12 | **Jordan's**, via `ED-SE-0051` — and `ED-WR-0011` says the two must be answered together |
| item 13's comparator | **Jordan's**, via RR-1 |
| ratification of anything in this directory | **Jordan's**, and not by merging it. Every file here is held back in full |

## C.4 · THE THREE SURVIVING RULING REQUESTS

Each ran `CLAUDE.md` §0's five steps — superseded · irrelevant · answered by a design document ·
answered by precedent · answered by what makes sense for the architecture — and survived all five.

⚠ **THIS SECTION SAID *TWO* UNTIL 2026-09-17 AND THE SUITE CARRIED THREE.** `03` §C.3 escalated a
third — its departure from `scale_transitions_v30.md` — under the heading *"THE ONE ITEM IN THIS FILE
THAT NEEDS JORDAN"*, while this section closed with *"Nothing else survives."* Two files, two counts,
neither visible from inside the other, and **`04` is the suite's ruling ledger, so the defect is
here.** Adjudicated on who opened the source: `03` opened the document and measured it; this file
never cites it. It is **RR-3** below, and `README.md` carries all three.

### RR-1 · Policy collision: **nearness or rank?**

⚠ **OWNER: `01` §C.6** (unified 2026-09-17). It is `ED-IN-0231`'s `needs_jordan` fork and `01` carries
the five-gate argument, the feel-of-the-game table and the recommendation's full case. **What this
section owns is the build consequence**, which is what a ruling ledger is for. Restated here in short,
not re-argued.

When a hearth's `draw` clause has a live row at the settlement and another at the province, which
wins?

| option | what it makes the game |
|---|---|
| **(a) NEAREST ancestor wins; a superior may mark its row `reach: all` to override** | subsidiarity by default, centralism **by declaration** |
| (b) HIGHEST rank always wins | a hierarchy in which a province's row is simply the law everywhere below it |

**Recommendation: (a).** It makes a provincial policy *reach* a hearth **on purpose rather than by
default**, which is what Jordan's *"a provincial policy on farming taxation may end up impacting a
hearth"* describes as a thing a superior **does**; and it keeps `AX` T-c — every clock wound by a
nameable act — true of policy, because `reach: all` is an act's operand and not an ambient property.

**Cost of being wrong: one comparator line in `in_force` and no data migration.** So the cost is
small and the **game** is not: under (b) no seat below the province has a policy worth setting in the
clauses the province has touched, which deletes most of the subject's option-set movement at the
lower rungs. **That is why it survives step 5** — two defensible options, materially different games,
and the engineering is a coin flip.

### RR-2 · `ED-SE-0051` — the bound on the demographic loop

**Already queued** at `registers/editorial_ledger_se.jsonl:51`, `status: open`,
`needs_jordan: true`, minted 2026-09-10: *"matter only, or matter plus hearth capacity?"*

**Recommendation: the CAPACITY arm, as `capacity(w, rung)` — a Query over DWELLING sites with a
floor, never a fixture row.** R7 forbids the fixture shape anywhere (*"no magnitude carrier is
admitted at any scale"*, `design_rulings_2026-09-06.md:169`), so the arm that is buildable is the
Query arm; the ruling is about the **bound**, not the carrier.

**Cost of being wrong: a Query swapped for a fixture — S.** It gates **item 12 only**.
⚠ **`ED-WR-0011` (46 NPCs) does not moot it** — capacity bounds fabrics, not the roster — **and
ED-WR-0011 says the two questions must be answered together**: *"Answering them in either order
separately risks two rulings that do not compose."* Put them in front of Jordan as one question.

### RR-3 · The zoom-trigger table: adopt the claim-landing replacement, or keep thirteen authored rows?

**Raised and argued by `03` §A.7 and §C.3; registered here 2026-09-17 so the suite has one ledger.**
`03` cuts six of thirteen authored zoom triggers in
`systems/_architecture/reference/scale_transitions_v30.md` and replaces the trigger-and-priority logic
of all thirteen with *a trigger is a claim landing (Q2); priority is the claim's `source`*.

| option | what it makes the game |
|---|---|
| **(a) Adopt the claim-landing replacement** | the eight scene-content cells survive verbatim; nothing is triggered by a fact the player holds no claim about |
| (b) Keep the table and give each condition a claim gate | thirteen authored rows whose gates drift from the four question sources — `AX` **ID-12**'s defect with extra steps |

**Recommendation: (a)**, `03`'s. Four of the thirteen conditions name an aggregate no `Rung` may store
and two more name another person's interior, so implementing the table as written requires the surface
to tell a duke about an Order-0 settlement he holds no claim on.

**Why it survives the five steps, and why it is the WEAKEST of the three — both said, because `03`
itself argues both halves.** It survives because the answer **overwrites ratified canon**: the file
carries `## Status: CANONICAL` at `:6`. It is weak because `03` §A.7.1 also measures that the file
carries a **second, different `## Status:` line** at `:8`, sits in the retire set, holds **zero
`.py`**, and therefore binds nothing at runtime under `CLAUDE.md` §0.05 — and the reconciling plan
closed it at step 1 on exactly that ground. **The suite does not average over that.** It is escalated
because a cut to a CANONICAL head is Jordan's to take, and it is marked weakest because the cost of
(a) being wrong is **editorial only**: the scene-content column is untouched either way and nothing in
`engine/season/` implements a trigger table.

**Nothing else survives.** If an author finds a policy clause that fits **none** of the seven
`requires_forms`, that is a **fourth** survivor, it is STRUCTURAL, and it must be written as one — **do
not widen the roster.**

## C.5 · THE THIRTEEN CLOSED — cited, so nobody re-asks them

Clearing the standing queue is session work (`CLAUDE.md` §0: *"find a stale `needs_jordan` on a
settled question and CLOSE it with its citation. Preserving a dead question is not conservatism; it
is how the queue formed"*). ⚠ **THIS SECTION LISTED NINE AND `01` §C.6 LISTED A DIFFERENT NINE — five in common, four unique to
each, THIRTEEN in the union (unified 2026-09-17).** Two lists both saying *"nine"* is drift no reader
inside either file can see. **This section is now the SINGLE OWNER of the closed list** (`CLAUDE.md`
§8 at prose), `01` §C.6 is a pointer to it, and rows 10-13 below are the four it carried.
These thirteen were live candidates for `needs_jordan` and are closed here.

| # | the candidate | verdict | §0 step | citation |
|---|---|---|---|---|
| 1 | **May a policy clause condition eligibility?** | **CLOSED: yes**, as a `requires` conjunct in one of the seven forms with a Query behind the predicate. **No fifth `eligibility_kind`, no eighth form** | 5 (+3) | `AX` ID-17 (`:631`) / T-b (`:284`); `rosters.yaml:1086-1122`; `rosters.yaml:148-160` |
| 2 | **Do three seats mean three times the acts?** | **CLOSED: no.** Delete `budget_office_bonus` | 3 | `ARCH §A.3` row 15 (`:184`); `decision/budget.py:56-57`; `H-92` (`hole_register.yaml:1106`) |
| 3 | **Confirm `hold`'s object domain; does the guard need a ruling?** | **CLOSED as CONFIRMED.** The guard ships; this is a **REPORT** to Jordan, not a question | 3, 4 | `holonic_ARCHITECTURE.md:538`; `ARCH §A.3` rows 12 & 14; `10_SUPERSEDING.md:1275-1281` |
| 4 | **Does the Church's built presence overwrite canon?** | **CLOSED.** The four-axis model lives in the tree ED-IN-0204 Decision 1 superseded; in the head a creed is a Proposition with members plus a HALL site, acting as a **band** (T-b) and never a modifier | 1, 2 | ED-IN-0204 Decision 1; `populated.py:486-492` (creeds minted as Propositions, `scope=template`) |
| 5 | **Who may `open_case`?** | **CLOSED.** `open_case` is `remit:determine`; the person's route is `petition` (`own`) | 3 | ratified position 19; the `verb_table.yaml` rows |
| 6 | **Council cardinality — one seat or many?** | **CLOSED: ONE seat, many holders via `oblige`** | 3 | `AX §E.2.5` (`:1465`); `ARCH §B.7` call 2 |
| 7 | **Is a province stored or emergent?** | **CLOSED: a declared `rung_kind` that `build_realm` never builds — emergent** | 3 | `world_q.py:345 provinces_of`; `rosters.yaml:109` (province is on the ladder); `systems/settlements/reference/scale_hierarchy_v1.md` §2 (`## Status: RATIFIED`, 2026-07-13; *"a province is an emergent aggregation"*, `:32-33`) |
| 8 | **AX-5 bidirectional MATTER — is an upward crossing a fourth motion?** | **CLOSED: motion 1.** ~~Ship `regrowth: 0` rows for built kinds plus~~ item 7's falsifier, plus the sign assertion `02` §C.2 now carries (the `regrowth` rows were struck 2026-09-17 — no table, no reader). No ruling | 5 | `matter.py:262`; R4's four routes (`design_rulings_2026-09-06.md:81-87`) |
| 9 | **Prince-bishop exclusivity — may one person hold a title seat and a body seat?** | **CLOSED: yes, and exclusivity is CONTENT** — refused at `confer` by a `cardinality`/`relation` conjunct once `Act.via` lands. `Office.__post_init__` already refuses a title-in-a-body (`carriers.py:536`) | 5 | `ARCH §B.7`; `state/carriers.py:527-547` |

| 10 | **The council grant fork — where does a council member's grant live?** | **CLOSED at gate 3, and the premise is dead.** `ARCH §B.8` retires `Tenure.payload` in favour of `term?`, so there is no payload to put a grant on; `01` §A.6 puts it nowhere at all — what a person may do by virtue of a seat is a **claim in their own ledger**, deposited by the same witness step for a council member as for a sole holder. `hold` keeps 1-per-object | 3, 1 | `ARCH §B.8`; `01` §A.4, §A.6; `world_q.py:138-145` |
| 11 | **H-91 — is `remit:revoke` NECESSARY or is purview SUFFICIENT?** | **CLOSED: it dissolves rather than compromising.** `remit:revoke` is the **actor's** side (*may this seat take this kind of act?*); the basis is the **target's** side (*what does emptying THIS seat require?*). Two conjuncts, two owners, no over-refusal | 5 | `01` §A.3; `predicates.py:276-286` registers the conflict in place |
| 12 | **`domain: RungId[]` on a Seat, and a per-act `remit: (act, scope?)[]`** | **CLOSED: refused / not adopted in v1.** `ARCH §B.7`'s `scope?` is **singular**, and purview is the `contain` closure of `scope` plus the holder's `hold` Tenures on rungs, which `in_holdings` and `under_purview` already walk — the walk is *"a DISJUNCTION over the seats"*. A Lord whose territories are not under one ancestor is a defect in the `contain` tree, not a reason for a set-valued field; a set also inverts rank, since `max(ordinal(kind(d)))` over a Count's territories computes **territory**. For the per-act scope: name a seat that needs it first; a Duke who may `issue` duchy-wide and `confer` in one province **establishes a sub-seat** | 5 | `ARCH §B.7`; `predicates.py:105-140` (`:127-129`); `rosters.yaml:706-709`; `01` §A.1 |
| 13 | **A `governance_mode` / `power_base` enum** | **CLOSED: refused, and it was cut once already for being unread.** *"They were not wrong; they were UNREAD — nothing in the loop or the office schema consumed either."* A mode is a bundle of clause values, and a bundle is a name for a configuration the clause table already expresses | 1, 2 | `rosters.yaml:86-92`; `01` §B.2 |

**Also closed, and refused rather than deferred:** `undertake` — folded into a Record kind plus a stage
template. `wound` → `Site` — deferred to position 22, which is not the same as refused.

---

# PART D · FALSIFIERS

## D.1 · This document's own claims, and what would show each wrong

| # | claim | what would show it wrong |
|---|---|---|
| BO-1 | **The gate-contract rule partitions the work correctly** | an item with an empty `writes:` and no Tenure-on-another write that nevertheless has to be rewritten at position 7. One such item and the rule is not a rule |
| BO-2 | **Two thirds of both subjects are Arc-2-independent** | count the flagged rows in §A.6: ~~4 of 23~~ **3 of 23** are `YES` (13, 15, 16 — item 21's strike dropped the fourth and this row had not followed; corrected 2026-09-17), 2 are the gate itself. If a reader finds a fifth `@effect_for` hiding in items 1–12, the fraction moves |
| BO-3 | **Items 1–5 are testable today** | any of them needing a carrier, a roster member or a gate parameter that does not exist. Item 4 is the closest call — it needs item 8 to keep `populated` loading, which is why they are paired in the text rather than left to be discovered |
| BO-4 | **Q3's referent fix alone changes nothing observable** | a crossing in any world any gate executes. The falsifier is cheap: `len(w.crossings)` after the runs CI performs. Measured 0; if it is ever non-zero, item 1b is unnecessary and should be dropped |
| BO-5 | **`Rung.sites` is a free cut** | a reader outside tests, or a `(Rung, sites)` matrix row. Measured: neither exists. `grep -rn "\.sites" engine/season --include=*.py` and the 40-row matrix are the instruments |
| BO-6 | **the five verb rows load with no grammar change** | re-plant them. This is the one claim in the file that was established **constructively** rather than by reading, and it is therefore the one most worth re-running |
| BO-7 | **the pre-flight's silent eleven are silent** | a load refusal on any of them. If one refuses, the corresponding invariant is built and the row must move to §A.1.1 — **this is expected to fire eventually**, at ratified position 23, and that is the point of listing which five invariants are unbuilt |
| BO-8 | **no guard in §B.4 earns its existence** | a defect in one of those artifacts that reaches the game, the exported params, the port or the `needs_jordan` queue. That is the predicate; if it is met, the row leaves the list |
| BO-9 | **`Office.upkeep` has no reader** | any `.upkeep` read in `engine/season/**/*.py`. Measured absent 2026-09-17. This one is the shape §0.1 pt 3 warns about — *"X is absent"* is the cheapest claim to make and the hardest to see wrong — so it was checked by grep and by `ARCH` §F.18 being open, not inferred |
| BO-10 | **the measured census is the census** | re-run `python -m engine.season.harness.populated` and the two probes named in items 1 and 2. Build-time: `contain` 373 · `commit` 86 · `hold` 35 (person 19 / faction 16; office 19 / rung 16 / **site 0**). After one season: stores 4,810 at 37 settlements, 0 at 211 hearths; sites with presence 0 of 74; first crossing at MATTER pass 21 |

## D.2 · Falsifiers this file predicts will FIRE

Two, flagged as predictions rather than closed arguments (`00_DERIVATION.md`'s `D-6` precedent — that file's own numbering, not this one's):

1. **BO-7 will fire at position 23.** The planted-violation tests for `ARCH`'s twelve invariants are
   scheduled; when they land, several of §A.1.3's rows become load refusals. The table should shrink
   and the shrinkage is progress, not a correction.
2. **Item 16's conservation control will fire on `found`'s first run.** `F10` destroyed 6 grain on
   every probe run once already, and the existing checker *"cannot see this failure — it never runs
   `found`"*. Expect the re-pointed checker to go red the first time and treat that as the control
   working.

---

# APPENDIX · CITATION REPAIRS

**Standing instruction, per `CLAUDE.md` §0.1 pt 3 — *"A citation you have not opened is not a
citation"*:** every `path:line` in every file of this directory is opened by its author before it is
written. A citation carried forward from an analysis note without opening it is a **defect**, and
four independent critics found drift to be the most common defect in this session's material — one
document wrong at **16 of 30**. The three shapes and what to observe first:

| claiming | observe this first |
|---|---|
| *"X is absent / dead / never fires"* | **RUN the thing that would show presence** |
| *"X works today"* | **open the CALL SITE, not the declaration** |
| *"as `F` says at `:L`"* | **open `F` at `:L`** |

### Repairs made in this file

| source | wrong | actual, verified 2026-09-17 |
|---|---|---|
| the reconciling plan | *"the 723-of-723 `work` refusal"* | **723 is `transfer`'s corpus fold count** (the `coin` control arm's *"0 executed / 723 refused"*, `hole_register.yaml:2155`). `corpus_run` prints a **set** of refused verb names (`corpus_run.py:644`) and no `work` count exists. The artifact is `VERBS ONLY REFUSED` dropping `work` |
| the plan, item 1 | artifact = `work` candidates rising after the Q3 fix | **unreachable by item 1 alone.** Sites start at `condition_scale` 1000, wear 10/season, highest floor 800 → **first crossing at pass 21**, measured; CI runs the populated world 1 season and the corpus ≤ 6. Item 1 splits into 1a + 1b |
| the plan | `carriers.py:557` for `Rung.sites` whitelisted | **`:568-569`** (`_DECLARED`); the class opens at `:553` |
| A3 | `predicates.py:190` for the `is_title` branch | **`:252-254`** (`target_is_title = title_domain(…) is not None`); `_req_revoke` opens at `:222` |
| the plan | `holonic_ARCHITECTURE.md:1281-1295` for §54 item 7's restore mirror | **`holonic_ARCHITECTURE.md:1898`** — the §54 table row, landing at §27.1. `:1280-1294` is **§37.1**, the dispensation head |
| the plan | `holonic_ARCHITECTURE.md:894-926` for §37.1's *"scope enumerates EXECUTORS not places"* | **`holonic_ARCHITECTURE.md:1289-1291`** |
| A3 | *"`wear_per_season` halved and doubled"* as a control | **`wear_per_season` declares no sweep** (`rosters.yaml:831-844`, `row: H-07`, no `sweep:` key). The halved/doubled sweep is **`band_floors`'** (`:1179`); `site_yield`'s is `[declared, uniform, none]` (`:1150`) |
| the plan | `populated.py:612-618` for the faction holds | the loop opens at **`:613`**; the mint is `:617-618` |
| the plan | `rosters.yaml:250-264` for `question_sources` | the block runs **`:250-270`**; `open: true` is `:252` and `values:` is `:270` |
| the plan / A3 | `matter.py:265` for the crossing | **`:262`** (`if before >= floor > s.condition:`); the Event is `:267-270`, `w.log.append` `:271`, and **`w.crossings.append` `:272`** (~~`:271`~~ repaired 2026-09-17) |
| A3 | `resolve.py:225-233` / `:192-203` / `:544-560` | the raises are at **`:238`** (*"Part E does not say WHAT VALUE"*), **`:194`** (*"a precondition the fold cannot evaluate"*), and the clamp-once TRACE at **`:551-553`** |
| A3 | `world.py:295-303` / `:353-358` | the gate signature is **`:295-302`**; the L4 social refusal is **`:352-357`** |
| A3 | `data/fixtures.py:105-125` for the coordinated-row check | **`:106-123`** (`Forbidden` at `:111-117`, `Ungraded` at `:118-123`) |
| A3 | `test_season_shape.py:3092-3100` for invariant 2's only caller | the function opens at **`:3076`**; the shape assertion is **`:3095`** |
| `write_matrix.yaml:43-50` (in-tree) | *"ELEVEN RES-stepped rows with no producing verb"*, *"NINE after two schema changes"* | **10 today**, measured with the file's own reproduce command at `:38-42`. `Date.fired` was repaired in place and neither deletion landed. Both of the file's figures are true of their own basis and neither reproduces |
| `_part2` (RATIFIED) | cites `ARCH` as `04:529-534`, `04:1024`, `04:330` | re-expressed here as **§C.2**, **§E**, **§B.7**. The raw-line form is not repaired in the ratified file; this proposal simply does not use it |
| A3 | H-71's *"9 of 32 verbs cannot be formed person-side"* | the mechanism holds; **10 of 38** today |
| A3's own §2 C-5 | the offered-use set is *"already half-modelled"* | corrected **by its own adversarial pass**: `world_q.verbs` has **zero callers under `loop/`**; its five callers are all in `harness/probes.py`. Re-verified here |

### Citations opened and found CORRECT — so the list above is not read as a complaint

**Opened and matching.** Every `path:line` in §A.1's three tables, checked one at a time against the
raise it names. Plus: `world_q.py:514`/`:518`/`:345`/`:399-413`/`:416-436` ·
`options.py:131-172`/`:259-323` (`site` ← the referent at `:311-312`) ·
`world.py:197`/`:223`/`:242-256`/`:295-302`/`:325-346`/`:352-357`/`:374` · `budget.py:56-57` ·
`matter.py:169`/`:174`/`:179-185`/`:197-199`/`:262`/`:267-271` · `carriers.py:48-57`/`:59`/`:491`/
`:527-547`/`:568-569`/`:577-578`/`:585-587`/`:589-596` · `verb_table.yaml:448-467` (`effect:` at `:465`) and the
`work` row from `:755` · `populated.py:357`/`:361`/`:373-374`/`:486-492`/`:605-618` ·
`corpus_run.py:216-217`/`:644` · `driver.py:96-99`/`:145-158` ·
`resolve.py:161`/`:194`/`:238`/`:259-266`/`:551-553` · `rosters.yaml:104`/`:109`/`:119`/`:136`/
`:142-146`/`:160`/`:250-270`/`:660`/`:814-816`/`:831-844`/`:1084`/`:1086-1122`/`:1146-1199` ·
`ARCH §A.2`, §A.3 rows 12/14/15, §B.3, §B.7, §B.8, §B.13 invariants 2/4/5/7/10 at
`:456`/`:458`/`:463`/`:466`/`:468`, §C.2's F3 at `:523-540`, §C.3 at `:564`, §C.11, PART D rows 1–6,
F.20 at `:1082`, PART E step 2 at `:1023` · `AX` ID-4 `:443`, ID-13 `:489`, ID-16 `:544`, ID-17
`:631`, T-b `:284`, T-c `:304`, §D.11 `:1054`, §E.1.7 `:1319`, §E.2.5 `:1465`, succession `:1235-1240`
· `holonic_ARCHITECTURE.md:449-451`/`:538`/`:1280-1294` (§37.1)/`:1898` (§54 item 7) · `10_SUPERSEDING.md:1275-1281` ·
`04_VERBS.md:345-357` · `design_rulings_2026-09-06.md:77-92` (R4), `:161-193` (R7, **`:169`**) ·
`hole_register.yaml:795`/`:923`/`:1106`/`:1520`/`:1533-1544` · `editorial_ledger_se.jsonl:51` ·
`.github/workflows/valoria-ci.yml:378`/`:383`/`:389` · `test_season_shape.py:2514`, `:3076-3099`,
`:4992`, `:7104`, `:9873`, `:10322` — **all five existing test names at the lines cited, checked with
`grep -n "def <name>"` rather than assumed** ·
`workplans/2026-09-11-reconciled-program.md:127-161` and `_part2:160-291`/`:464-526`/`:586-621`.

**Instruments re-run for this file, 2026-09-17:** `python -m engine.season.harness.populated` ·
`python -m engine.season.harness.corpus_run` · `python -m engine.season.harness.register
--requirements` (**met 1 · not_met 4 (R-01 R-02 R-04 R-05) · partial 4**) ·
`python tools/m1_acceptance.py --summary` (**verdict NOT MET**; row 4 *"All M1 junctures execute"*
is **0/7 FAIL** and says **DOC-DERIVED** in its own detail — *"Editing the board greens this row"*)
· `write_matrix.yaml`'s own producerless-row command · four scratch probes over `build_realm(0)`.
