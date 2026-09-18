# 01 · DISPOSITIONS — the four GOVERNANCE trees

## Status: **MEASURED (2026-09-18)** for every `## Status:` line, banner, ledger row and `file:line` quoted below — each was opened at the line cited, and §4 lists the two I could not. **`paper`** for every verdict, which is a judgment (`CLAUDE.md` §0.2).
## Scope: the four governance trees of `00_THE_CENSUS.md` §2. **No other tree is dispositioned here**, and the ORDER is a different file's business.
## Counts (files, lines, inbound refs) are `00_THE_CENSUS.md`'s, handed to this pass and **not re-measured** (`CLAUDE.md` §10 pt 1).
## Closed verdict set: `LIVE` · `SUPERSEDED` · `ABSORBED` · `SPENT` · `ORPHAN` · `NEEDS-STATUS`. Nothing outside it appears below. **`ORPHAN` is unused — see §3.**
## One execution artifact was taken for this file: `python -m pytest engine/season/tests/test_governance_build.py -q` → **25 passed in 6.78s** (2026-09-18, this tree).

---

## §1 · The table

| # | tree · files | verdict | why, with its citation | `engine_season:` |
|---|---|---|---|---|
| **1** | `2026-09-03-governance-corpus-rebuild/` — **all 7** | **NEEDS-STATUS** | No `## Status:` heading anywhere; the equivalent is prose at `README.md:3` — *"**Status: PROPOSAL.** Nothing here is ratified"* — which is why the census grep misses it. And it **cannot be dispositioned against this tree at all:** `README.md:8-11` scopes the work to an uploaded zip (`governance_play_redesign_v1.zip`, 33 documents) and states *"no repository file was read as a source, and no claim in these documents is grounded in the working tree."* SPENT or ORPHAN would each assert something about `main` that its own provenance section forbids | **NONE.** By construction — no path in this repo was an input. `README.md:47` also declares its numeric parameters *"**unvalidated**"* |
| **2** | `2026-09-17-governance-and-holdings/` — `00_THE_DESIGN.md`, `01_SEATS_AND_POLICY.md`, `02_THE_BUILT_WORLD.md`, `04_BUILD_ORDER.md` | **SUPERSEDED** | Its own banner, `README.md:4-9`: *"**ROUND TWO IS THE CURRENT SUITE: `../2026-09-17-governance-and-holdings-r2/`**"*, and per-file supersession banners on each (e.g. `02_THE_BUILT_WORLD.md:4` → `…-r2/04_MATTER_AND_WORKS.md`). Successors by path: `00`/`01` → `…-r2/02_THE_WRIT_AND_THE_WORD.md` and `…-r2/03_SEATS_AND_CONTENT.md`; `02` → `…-r2/04_MATTER_AND_WORKS.md`; `04` → `…-r2/05_LEDGER_AND_BUILD.md` §6 (`README.md:79`, *"which supersedes `04` §C.4 as the owner"*). The ledger records the same: `registers/editorial_ledger_in.jsonl:17`, `ED-IN-0237` with `supersedes_row: true`, `superseded_by: ["ED-IN-0233"]` | **NONE, and that is a warning rather than an absence.** `04_BUILD_ORDER.md` is a build order whose arithmetic was regraded and **one of whose dependency edges reverses** (ledger `:17`: all 16 rung-holds in `build_realm(0)` are faction-subject, which puts the content item *after* the holds item). Anything it implied reaches `engine/season/` only through row 5's items. **Do not build from `04`** |
| **3** | `2026-09-17-governance-and-holdings/03_THE_SURFACE.md` | **LIVE** | Explicitly not superseded — `03_THE_SURFACE.md:4`: *"✅ **STANDS 2026-09-17 — NOT superseded.**"*, confirmed independently by the ledger at `registers/editorial_ledger_in.jsonl:17` (*"SPLIT DISPOSITION, and the split is the point"*). Something depends on it: five r2 files cite it (`README.md`, `01`, `02`, `03`, `05`) plus `2026-09-17-governance-and-behaviour/RULINGS.yaml`. Its Surface Law `L-1..L-3`, cell law and causation worksheet bind round two; three substitutions are struck **into** it in place. Its own **RR-3** is no longer open — closed at gate step 3 (`RULINGS.yaml:1879-1900`) | **NONE, and the reason is a refusal.** Its one engine-touching proposal was a fifth `purview` question source in `engine/season/queries/world_q.py::questions_for`; its §A.7 refused it and round two withdrew it (`03_THE_SURFACE.md:186`, `:313`). A refusal changes no path. What it governs — a player surface — **does not exist in `engine/season/` to change** |
| **4** | `2026-09-17-governance-and-holdings/` — `AUDIT_VERDICT.md`, `UNIFICATION_LEDGER.md` | **SPENT** | Both judge round one and, in the suite's own words, *"die with it"* (`README.md:8-9`); `UNIFICATION_LEDGER.md` is described at `README.md:43` as *"A closed record, not a queue."* `AUDIT_VERDICT.md`'s nine limits are mapped one by one in `…-r2/README.md` — **three answered by name, four die with the mechanism that raised them, two carried forward as limits on r2 itself**, which is r2's debt now, not round one's. Round one's two surviving ruling requests are both disposed: **RR-2 RULED** by Jordan 2026-09-17 (`RULINGS.yaml:1838-1845` — *"MATTER PLUS HEARTH CAPACITY… a `capacity(w, rung)` QUERY… with a FLOOR"*), **RR-3 closed** at step 3. It raises nothing that is still open | **NONE.** A terminal verdict and a divergence record change no path. The one engine consequence that *came out* of RR-2 is recorded in row 6, where the order that fails to schedule it lives |
| **5** | `2026-09-17-governance-and-holdings-r2/` — **all 8** | **LIVE** | The named current suite (row 2's banner), the most-read tree in `proposals/` (**54** inbound), and **nothing supersedes it**. Its own status is honest about what it is not: `README.md:5` — *"**Nothing in this suite has run.** `05` §A.4 item 1 is the first thing that would"* — and `EXECUTION_PLAN.md:3` adds that *"Landing an item here ratifies nothing; it makes a behaviour run."* All six of its ruling requests are now disposed by `RULINGS.yaml` (RR-P, RR-A, RR-B, RR-C, RR-2 ruled; RR-1 closed at step 2 per `README.md`; RR-3 closed at step 3). **Disposed questions do not make a design SPENT** — its sixteen build items are unbuilt, and five of them landed through row 7, which is a dependency in code, not a supersession | **LARGE, CONCRETE, and mostly unbuilt: 11 of 16 items.** From `EXECUTION_PLAN.md:26-31` and its whole-order table at `:51-75`, at the `engine/season/` modules that hold those names: `loop/effects.py` — item 1's `@effect_for("commit")` (**measured absent**: no `effect_for("commit")` in that file today), and the `give`/`oblige`/`found` bodies of items 6, 9, 12 · `queries/world_q.py` — item 2a's `reach` and `place_of` · `verb_table.yaml` + `write_matrix.yaml` — items 5, 13, 14 (record-kind fold, four verb rows, 13 field deletions) · `state/world.py` — two `World` dicts and `w.crossings` deleted · **a new `engine/season/offices.yaml`** for item 10 (**measured absent**: eight YAML files there, none named `offices.yaml`) · `loop/matter.py` — item 12's `works` and `found`. Item 13 is unblocked (`RR-A` → FOLD, ruled); **item 15 stays blocked** on ratified positions 3–5 |
| **6** | `2026-09-17-governance-and-behaviour/` — `README.md`, `00_THE_SEAM.md`, `01_THE_BUILD_ORDER.md` §1–§6, `probe_execution_pass.py` | **LIVE** | **The only one of the four trees `engine/season/` itself reads** — `engine/season/rosters.yaml:1119` (*"`CAT-2`, closed at step 5"*), `engine/season/hole_register.yaml:922` and `:963` (*"item 3b of…"*, *"item 6e of… §7.5"*), `engine/season/harness/probes.py:1102`, and `engine/season/tests/test_governance_build.py:7`, whose module docstring names this file as the subject its 25 tests observe. That is the census's reading too: **20 repo-side refs against 1 from `proposals/`** — points outward, nothing in the corpus depends on it. It supersedes neither subject suite and takes no position inside either (`README.md:6`) | **The remaining schedule, plus a gap it records and does not schedule.** Phase 6 items 6a–6c land in `engine/season/decision/` (`01_THE_BUILD_ORDER.md:1019-1031`). ⚠ And its own preamble at `:24-39` records **four ruled items no phase schedules**, of which two are measured absent here: a **migration verb** — `residence` is one of five `person_predicates` (`engine/season/rosters.yaml:312`) and **no verb writes it** (grepped tree-wide over `engine/season/`; `move` writes `Person.travel_leg`, `engine/season/verb_table.yaml:404`) — and **`capacity(w, rung)`**, absent from `engine/season/queries/`. The other two are an affiliation roster with an incompatibility relation, and the thirteen re-authored. **This row records the gap; it schedules nothing** |
| **7** | `2026-09-17-governance-and-behaviour/01_THE_BUILD_ORDER.md` §7 — **items 16, 3a, 3b, 6d, 6e** | **ABSORBED** | Its content is now in code, and something ran it. `:362`: *"items 16, 3a, 3b, 6d and 6e **LANDED**"*, `ED-IN-0246`/`0248`/`0249`, all present in `registers/editorial_ledger_in.jsonl`. Verified in the tree: item 16 → `hold_subject_kinds`/`hold_object_kinds` in `engine/season/rosters.yaml`, `state/world.py`, `data/rosters.py` · 3a → `nearest_store` in `engine/season/queries/world_q.py` and `loop/matter.py` · 6d → the `beneficiary:` column in `engine/season/verb_table.yaml` and `decision/choose.py` · 6e → `_scar` at `engine/season/loop/effects.py:324`. **Execution artifact:** `engine/season/tests/test_governance_build.py`, **25 passed in 6.78s** on this tree today | **LANDED — the paths above.** ⚠ **Two items of the five are not absorbed and the row says which:** item **1 HELD** (its headline claim retracted, `:451`) — consistent with `@effect_for("commit")` being absent from `loop/effects.py`; item **4 REVERTED** (*"it starves the corpus"*) — consistent with `budget_office_bonus` still live at `engine/season/decision/budget.py:57` and `engine/season/data/fixtures.py:430`. §7 is `measured`; §1–§6 remain `paper` (`:361`) |
| **8** | `2026-09-17-governance-and-behaviour/RULINGS.yaml` | **SPENT** | It stands at **12 closed · 9 ruled · 0 escalated** (`01_THE_BUILD_ORDER.md:22`, corrected in place from *"what is still Jordan's"*; `ED-IN-0244`, `ED-IN-0245`, both in `registers/editorial_ledger_in.jsonl`). Every one of its 21 questions is closed by `CLAUDE.md` §0's five-step gate or ruled by Jordan 2026-09-17: the nine that escalated — `RR-A`, `RR-B`, `RR-C`, `RR-P`, `RR-2`, `CAT-6`, `STR-2`, `STR-5`, `STR-6` (`:2210-2218`) — were all ruled. **Zero open.** It is history and a citation source, which is exactly what `engine/season/rosters.yaml:1119` uses it as. **Recording it as an open queue is the defect `CLAUDE.md` §0.3 names**, and its own header is already careful: *"`closed` does not mean built, ratified or agreed"* | **NONE.** It decides; it changes no path. The engine consequences of its rulings belong to rows 5 and 6 |

---

## §2 · The four things a reader would otherwise rediscover

**(a) The 09-03 rebuild is not dispositionable against this tree, and that is a provenance fact, not a
gap in this pass.** Its subject is 33 documents that were uploaded to a session. Several share
filenames with files under `systems/` and `README.md:15-16` states plainly that they *"are **not**
verified to be identical"* and no comparison was made. Its `NEEDS-STATUS` verdict is therefore about
one thing only: a reader arriving cold sees no `## Status:` heading, and the six-word answer to *"is
this current"* lives in a `**bold**` line the grep does not reach. Its zero inbound references are
**noted and are not the verdict** — see §3.

**(b) The split at round one is recorded in two independent places and they agree.** The suite's own
banner and the `ED-IN-0237` supersession row both say `03_THE_SURFACE.md` STANDS while `00`, `01`,
`02` and `04` are superseded. The ledger row adds the reason the split is not cosmetic: `03` was
**right against its own sibling** on the fifth question source, and round two withdrew the fifth
source. A superseded suite that contains one file which won its argument is why rows 2, 3 and 4 are
three rows and not one.

**(c) One of these four trees is load-bearing on the game, and it is not the biggest one.** r2 is 9,134
lines and is read by 54 things in `proposals/`; `governance-and-behaviour` is 4,216 lines and is read by
**one**. But `engine/season/` cites only the second — in a roster, twice in the hole register, in a
probe and in a test file's own statement of subject. Under `CLAUDE.md` §0.2 that asymmetry is the whole
measurement: the tree with the execution artifact is the tree the code depends on. **Both are LIVE, for
different reasons** — r2 because nothing supersedes it and its items are the work; behaviour because
code would break its own stated subject if it vanished.

**(d) The rulings opened work that no order schedules, and the order says so itself.** The ruled
migration verb, the `capacity` Query, the affiliation roster and the thirteen re-authored sit outside
all six phases (`01_THE_BUILD_ORDER.md:25`: *"It is **not** added to the phases below"*). Two are
measured absent from `engine/season/` in row 6. `residence` is the sharpest case: it is a rostered
predicate a claim may assert, measured in `engine/season/hole_register.yaml:1777`, and reachable by
nothing that writes it — which
is the same shape `CLAUDE.md` §0.05 flags for `fac.intel` — *"has ruled bounds and is reachable by
nothing."* **Recorded here because it is where the gap is true. Not scheduled here.**

---

## §3 · What this file does not do

- **It schedules nothing.** Every row states what a tree *is* and what it *implies* at a path that
  already exists. No row says a thing should be built (`CLAUDE.md` §0's test: *does this document
  create work for a future session?*).
- **`ORPHAN` is unused, deliberately.** Row 1 is the only tree with zero inbound references, and its
  primary defect is that it cannot be read cold — `NEEDS-STATUS` is the verdict that says so. Calling
  it an orphan would imply a disposal this pass has no grounds to assert, since its own provenance
  section forbids comparing it to `main`.
- **It flips no `## Status:` line, in any file, in any of the four trees.** All four remain **HELD BACK**
  where they say they are; `ED-1094`'s merge-ratifies default is refused by each of them in their own
  words, and nothing here changes that.
- **It ratifies no verdict as canon.** The verdicts are `paper` (§0.2). The measured half is what was
  opened and what was run, listed in §4.

---

## §4 · Citation register — and the two claims written without a line

Every `file:line` in §1 and §2 was opened at that line. **Two claims are deliberately line-free**, per
`CLAUDE.md` §0.1 pt 3 row three:

1. **`…-r2/README.md`'s nine-limit map** (row 4) — read as a block; the table is long and its rows
   carry no stable numbering. The claim is the map's own summary sentence: *"Three are answered by name;
   four die with the mechanism that raised them; two are carried forward as live limits on THIS suite."*
2. **The path attributions in row 5** — `EXECUTION_PLAN.md` names **bare filenames** (`verb_table.yaml`,
   `budget.py`) and never a full path. The `engine/season/` modules named in that cell are the ones that
   hold those names, resolved by grep on this tree, not quoted from the plan. Where the plan's file does
   not exist yet (`offices.yaml`) the cell says **measured absent** and gives the `ls` that shows it.

**Absence claims, and the command that would have shown presence** (§0.1 pt 3 row one):

| claim | what was run |
|---|---|
| no verb writes `residence` | `grep -rn residence engine/season/` — hits only `rosters.yaml:312` (the roster) and `hole_register.yaml:1777` (a measurement); none in `verb_table.yaml` or `write_matrix.yaml` |
| `capacity(w, rung)` does not exist | `grep -rn 'def capacity\|capacity(w' engine/season/queries/*.py` — no output |
| item 1 has not landed | `grep -n 'effect_for("commit")' engine/season/loop/effects.py` — no output |
| `engine/season/offices.yaml` does not exist | `ls engine/season/*.yaml` — eight files, not among them |
| item 4 is reverted, not landed | `grep -n budget_office_bonus` — live at `decision/budget.py:57`, `data/fixtures.py:430` |
