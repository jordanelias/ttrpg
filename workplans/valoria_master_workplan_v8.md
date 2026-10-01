# Valoria — Master Workplan v8: the one plan — the remainder of Phases 1–4, and how each of THE NINE gets built

## Status: PROPOSED 2026-10-01 — directed by Jordan; adoption on merge (ED-1094)
## Lane: IN (cross-cutting). It is the ONE active plan (`CLAUDE.md` §2) for every lane whose items it carries — IN, SC, SE, MB, PC, FI, WR, GO. FA carries no open position: its handoff rows close when `29b` deletes the code they describe.
## Reads in order: this file (head, milestones, state index) → `_part2` (THE NINE, one section per row) → `_part3` (orchestration, pre-flight, Batches 0–1) → `_part4` (Batches 2–3) → `_part5` (Batch 4, the Jordan queue, the answered list) → `_part6` (standing content carried from the retired plans, and history).
## Grade under `CLAUDE.md` §0.2: `paper` throughout. A plan, not an execution artifact. Where a row says DONE it repeats cited evidence; the evidence is the thing cited, never this file.

**Why this exists, in Jordan's words (2026-10-01, verbatim).** *"Retire ALL plans. We will work on one
new plan that builds out the remainder from the 2026-09-28 and 2026-09-30 plans as well as plans out how
to build all remaining core tenets from requirements.yaml"* · *"We are allowed to have one active plan
per lane."* · earlier the same session: *"This plan will fold in all of 2026-09-28 plan. It will become
the new master plan"*. The "core tenets" are **THE NINE**, `R-01`..`R-09` in
`engine/season/requirements.yaml` (ruled 2026-09-05, `ED-IN-0204`).

**What happened before it.** Commit `ebb43bf0` retired every file under `workplans/` (21 files, each with
an exact `FORK:0671283` row in `references/restructure_ledger.md`), wrote the one-active-plan-per-lane
rule into `CLAUDE.md` §2, and re-pointed `tools/m1_acceptance.py` row 3 from the retired progress board to
THE NINE. Read any retired plan with `git show 0671283:workplans/<file>`. **None of them is an owner of
anything any more.** Where this plan needs their content, it carries the text; it never points at a
retired file as the place an instruction lives. A pointer to a retired file is *history* only.

**Name.** The directory's own `vN` lineage: v7 (`ED-IN-0216`, retired at `ebb43bf0`) → this file. It is
both what v7 was (milestones, who-can-answer, lanes) and what the 2026-09-28 plan was (THE ORDER) —
the retirement removed the reason they were two documents, so `master` keeps one sense.

**How it was produced.** A read-only Fable 5.1 reconciliation over HEAD `0671283` (every position
classed by evidence: instrument run, code opened, test listed, plan-only, or needs-run); the
orchestrator's verified findings; this write-up is Opus's, on HEAD `ebb43bf0`. Where Fable's evidence
was plan-only or needs-run and a cheap read or a single-file run could settle it, it was settled here
and the outcome is recorded at the row (`[SETTLED 2026-10-01: …]`). What was not settled is carried as
a first-step check in `_part3` §P.

---

## 0. HOW TO READ THIS PLAN

### 0.1 What it owns, and what it does not

| it owns | it does NOT own | owner |
|---|---|---|
| **THE ORDER** the remaining work is done in, every lane | per-lane **status** | `registers/handoffs/HANDOFF_<LANE>.md` |
| **WHAT** each open position does, its files, falsifier and gate | **which head is canonical** | `CURRENT.md` |
| **WHO** can answer each open question (`_part5` §J) | **whether the behaviour runs** | the instruments: `register --requirements`, `m1_acceptance.py`, `corpus_run`, `aperture`, the tests |
| the milestones M1/M2/M3 and what each is measured by | a figure — every number here is a dated reading of a named command | re-run the command |

v7's rule carries: **this plan has no status column except the one state index (§3), and every row of
it cites its evidence.** A status written twice drifts within days. If a row and its instrument
disagree, the instrument wins and this file is wrong.

**Binds (does not fork):** `references/id_reservations.yaml` (allocation protocol, `CLAUDE.md` §4) ·
`references/lane_assignments.yaml` (its `source:` names the retired v7; re-pointing it here is an
outside edit, `_part6` §H.3) · `HANDOFF.md` + the lane files · `CURRENT.md`.

### 0.2 The state classes

| `STATE` | meaning |
|---|---|
| **OPEN** | buildable; `GATE` names what it waits on. **A `GATE` of `—` is buildable today** |
| **PARTIAL** | some of it landed and runs (evidence named); the remainder is the open item |
| **BLOCKED** | a named position must land first |
| **JORDAN** | a decision or authored content is owed, named exactly in `_part5` §J |
| **DONE-realm / DONE-test** | used only where an open item depends on the distinction: *DONE-test* = a dedicated test executes it from a constructed input; *DONE-realm* = it also occurs in `populated.build_realm(0)` run through the real chooser (`aperture 4 0`). §0.2 accepts both as done; R-row moves usually need the second |
| **REVERTED** | built, attacked, reverted; the design question is registered |

Finished positions are not in the state index. They have one line each, with evidence, in `_part6` §H
(history) — `CLAUDE.md` §2: *"Finished positions leave the plan; the commit is their record."*

### 0.3 Numbering (carried verbatim from the 2026-09-28 plan §0; it still binds)

No existing position number changes meaning. New work takes one of three forms: **lettered
sub-positions** on the position it belongs to (`2-i`/`2-ii`, `12e`, `15d`, `17b`, `19d`,
`20-i`…`20-iv`, `22a`, `22b`, `24g`, `24h`); **new numbers ≥ 28** (`28-0`…`28-iii`, `29a`–`29f`); and
**named steps with no number** where there is no prior position to letter onto. **None of these
handles allocates a ledger id.** An id is allocated when the position is built.

⚠ **One collision, named so nobody resolves it by guessing.** In the 2026-09-28 plan's Phase-1 list,
"item 11" was position `25` (MB-GOLDEN, DONE). Position **`11`** is U6, the first R-01/R-02 corpus
measurement (OPEN). `11a`/`11b` are DONE. This plan uses position numbers only, never Phase-1 item
numbers.

**Added by this plan:** `13d-iii` (rung anchors for seats — the R-04 cap no position owned), `11-fix`
(U6's instrument repair), `B0-CI` (main's red CI), `R05-THREAD` (the `thread_read` operand decision),
`LADDER-MBPC` (the MB/PC lanes' ladder pass over their flagged rows).
Each is defined at its batch.

### 0.4 THE PER-STEP CADENCE — RULED by Jordan, 2026-09-18 (carried in full: this plan is now its only home)

*"at end of each step i expect a /code-review and /simplify to run followed by fixes then a forward
sweep to see how it impacts stuff"*

**One step = one position (or sub-position) = one commit.** Five phases, in order, every time:

| # | phase | what it is |
|---|---|---|
| 1 | **BUILD** | the position's change, and nothing else. No widening. |
| 2 | **`/code-review`** | the native fresh-context reviewer, which never saw the reasoning. Read the findings, then **apply** them. Verify each before applying — a review finding is a bug report, not a verdict. |
| 3 | **`/simplify`** | reuse · simplification · efficiency · altitude. Quality only; it does not hunt bugs. |
| 4 | **FORWARD SWEEP** | defined below. |
| 5 | **CLOSE** | `tools/valoria_local.py --staged`, the lane validator, then the `[scope]` commit citing its `PP`/`ED`. **The full suite runs once per BATCH close, not per step** (§0.5). |

**FORWARD SWEEP — defined, because it is a coinage and `CLAUDE.md` §4 requires it survive the session
reset.** *What did this change reach that nobody asked it to?* Five checks, each with an artifact:

1. **The instruments.** `python -m engine.season.harness.register --requirements` · `corpus_run` ·
   `python tools/m1_acceptance.py --summary`. **Did any row move, and is every move the intended one?**
   An unintended move is the finding.
2. **The hole register.** Did this close, narrow or widen a row — and does its falsifier now behave as
   the row predicts? A row whose falsifier did NOT flip when the code says it should have is the most
   valuable thing this sweep can catch.
3. **The call sites.** Grep the changed symbol's callers, not its declaration (`CLAUDE.md` §0.1 pt 3
   row two: *a roster existing is not a roster being used*).
4. **Figures the change just made stale.** Any `measured:` block, `cite:` field, handoff or plan row
   quoting a number this step moved. **This is the defect this repository pays for most** — §0.1 pt 3
   row four — and a sweep that skips it hands the next session a confident wrong number.
5. **The goldens.** Did anything output-moving change, and was a re-record INTENDED? Nothing verifies a
   golden re-pin was deliberate (`CLAUDE.md` §7), so say so plainly when one happens.

**The sweep's output is edits plus at most one paragraph in the commit message** (`CLAUDE.md` §0's
adversarial-pass bound). It creates no document and no directory. A finding that needs no ruling is
fixed in that commit or dropped.

### 0.5 Verification cadence, stopping rule, and what every producer must not do

- **Suite cadence (`CLAUDE.md` §0.4, RULED 2026-09-23).** Mid-step: only the file covering the edit.
  `python -m pytest tests/valoria -q -n auto` (and `engine/season/tests`, `engine/tests` where the batch
  can reach them) runs **once per batch close**, as `methodology-execute` prescribes — never to
  re-confirm a green already held. ⚠ The 2026-09-18 cadence put the suite at every step's CLOSE; the
  later §0.4 ruling (*"stop running suites so frequently"*) governs, and this is the reconciliation.
- **THE STOPPING RULE.** A falsifier that fails → `git revert` that position's commit(s) (never
  `--no-verify`, never skip/xfail/quarantine a test) → append **one** `hole_register.yaml` row only if the
  gap is measured, **one** ledger row only if a human decision is needed (`needs_jordan: true`, after the
  five-step ladder) → record the attack in the commit message → continue with the next gate-free item.
  **Never widen the position to make the falsifier pass.** `10`'s 2026-09-29 revert (H-79) is the
  precedent.
- **Must NOT, in any batch:** edit `.designs/` or `.audit/`; cite a `.md` as the reason a behaviour is
  correct; build a guard whose subject is process (§0.1 pt 5); create a directory or standing document;
  author a cell, a Godot version, or a Jordan item's answer; interleave the cells commit with `8`/`9`;
  build anything in `engine/mc_v18.py`; `git add` a file another lane is editing (use
  `isolation: worktree`); re-fetch from the GitHub API; write a count into `CURRENT.md`/`HANDOFF.md`.

---

## 1. THE MILESTONES — what "done" is measured by (v7 §1, re-read on HEAD `ebb43bf0`)

### M1 — ONE PLAYABLE SEASON

**Instrument:** `python tools/m1_acceptance.py --summary`. **[RAN 2026-10-01, HEAD `ebb43bf0`, 29 s]
verdict `NOT MET`, 1 row failing.**

| # | row | reading | kind |
|---|---|---|---|
| 1 | stub invocations on the M1 path == 0 | **PASS** — 0 `stub_resolve` calls, 1-season headless run of `engine/season`, seed 20260819 | executes |
| 2 | same seed → same `World.content_hash()` | **PASS** — `d58470198e22…` twice | executes |
| 3 | the nine requirements met | **FAIL 1/9** — met 1 · partial 5 · not_met 3 | ⚠ DOC-DERIVED: counts `status:` strings, each validated by `register --requirements`; not execution |
| 4 | N seeds, zero invariant violations | **PASS** — 24 headless seeds × 4 seasons + 2 populated × 1, 8 invariants, 0 violations over 50,073 events | executes |

v7's M1 blocker (rows 1's OI-05/OI-07 stubs in `mc_v18`) is history: row 1 was re-pointed to
`engine/season` on 2026-09-13 and passes. **M1 is now exactly THE NINE.** Row 3 greens when all nine
rows read `met`, and a row reads `met` only on a `measured:` block `register --requirements` accepts —
so M1 is closed by `_part2`, nowhere else. Row 3 stays DOC-DERIVED by its own declaration; do not
re-wire it to anything that a status edit could green faster.

### M1's companion — THE NINE

**Instrument:** `python -m engine.season.harness.register --requirements`. **[RAN 2026-10-01] met 1
(R-03) · partial 5 (R-04 R-06 R-07 R-08 R-09) · not_met 3 (R-01 R-02 R-05).** `_part2` has one section
per row: statement, measured reading, what moves it, what no position yet owns, and `met` as an
instrument outcome.

### M2 — THE ANY-SEED STORY BAR

v7: *N seeds each yield a chronicle that is connected, continuous, rooted, live and distinct* — M1's
invariant sweep generalized. **Its precondition is now met** (M1 row 4 exists and passes). **Its bar
still has no instrument:** `harness/soak.py` (#446) runs seasons and grades nothing; `corpus_run`'s
`ARC ENDS` count prints `NOT-COMPUTABLE — closed by W23 + W26 + W30`. Candidate gates, none built:
(i) `22` step 16 — THE BAR for proceedings (two seeded proceedings run end to end twice byte-identical,
`causes[]` walking to the raising date); (ii) `corpus_run`'s ARC ENDS becoming computable;
(iii) a chronicle render (the `chronicle` witness channel dies at `22` step 13, so this is open).
**M2 is not schedulable until one of those is an instrument; this plan builds (i) at `22` and names
(ii) as the R-01/R-02 instrument question in `_part2` §R-01.** v7's ruling R-7 (does the Churn Engine
workstream survive `ED-IN-0204`) closes at ladder step 2 — its head was under the dissolved `designs/`
tree; nothing builds on it (`_part5` §A, A-14).

### M3 — GODOT VERTICAL SLICE

Last, unchanged in substance. Position `26`. **The Godot engine version is UNRESOLVED and nothing here
asserts one** (`_part5` §J, J-9). `godot/godot_conversion_strategy_v1.md` is PROPOSED;
`references/module_contracts.yaml` has `doc: null` rows including `engine_clock`. ⚠ **A forward note
this plan creates and does not settle:** `28-iii` deletes `engine/autoload/engine_clock.py`; the
temporal spine of the adopted game is `engine/season/loop/driver.py` + `loop/calendar.py`. When `28-iii`
lands, the `engine_clock` contract row must say which code it now describes (§`28-iii`'s role-row
item) — `CLAUDE.md` §6's "starting with `engine_clock`" then means the season calendar, not the
deleted module. `godot/skeleton/` is not a head start.

---

## 2. ⭐ START HERE — the first commands the next session runs

```sh
git rev-parse --short HEAD; cat .git/shallow 2>/dev/null || echo "full clone"   # a shallow clone unshallows first (CLAUDE.md §2)
python tools/session_provision.py
python -m engine.season.harness.register --requirements        # expect met 1 · partial 5 · not_met 3
python tools/m1_acceptance.py --summary                         # expect NOT MET, row 3 FAIL 1/9
gh run list --branch main --limit 3                             # 'failure' until f6d7af27 (B0-CI) reaches main; then it must read green
```

Then **Batch 0** (`_part3` §B0: main's CI was red; the fix landed as `f6d7af27`, so Batch 0 is its
falsifier — CI green), then `_part3` §P (the pre-flight checks still open), then Batch 1. Each batch runs through `methodology-execute` (`CLAUDE.md` §9).

---

## 3. THE STATE INDEX — every position still in the plan (re-read on HEAD `ebb43bf0`)

Evidence: **[RAN]** an instrument this session · **[CODE]** a file opened · **[TEST]** a test file
present/run · **[PLAN]** read from a plan only (unverified) · **[SETTLED]** a Fable needs-run closed here.
`R` = the R-rows the position moves. Batch = where it sits in `_part3`/`_part4`/`_part5`.

**By the retired plans' phases, in one sentence each.** Phases 1 and 2: finished to §0.2's bar (a
dedicated test executes every position), but most Phase-2 verbs execute from hand-built acts only — in
the realm, `commit found build levy migrate confer establish revoke determine work` are attempted and
never execute (`aperture 4 0`). **Phase 3: `27` PARTIAL (PR #442); `10`'s `tell`→stance write REVERTED
with its side findings landed (PR #442); everything else open or Jordan-gated.** Phase 4: `20-i`,
`20-ii`, `20-iii`, `28-0` (narrowed), `28-i`, `28-ii` done; `28-iii` open; `29a`–`29f`, `20-iv`, `2-ii`
blocked behind it.

| position | handle | lane | STATE | GATE | R | batch | evidence / note |
|---|---|---|---|---|---|---|---|
| `B0-CI` | main's CI red | IN | **LANDED on this branch (`f6d7af27`), unverified on `main`** — what remains is the falsifier: `unit-tests` green on the push that carries it | — | — | 0 | [RAN `gh run view 36803379833`] `unit-tests` fails 7 on `main` at `0671283` and the two pushes before it: `test_forked_status.py` ×2 (`FORK:6f740d9` names a commit not in the repo — [SETTLED: `git cat-file -t 6f740d9` fails locally on a full clone too]; unfollowable rows 78 → 87), `test_link_values_pointers.py` (drift), `test_tool_input_paths_resolve.py` ×2 (`tools/build_engine_atlas.py` `EXEC_MAP`/`EXEC_TRACE` name files `28-i` retired), `test_export_sim_params.py` ×2 (drift; `_SCAR_DP` cited at `loop/effects.py` after the effects split). ⚠ At the time of writing the working tree holds UNCOMMITTED edits to exactly these surfaces (`engine/engine_params/{sim_params,value_pointer_links}.json`, `references/restructure_ledger.md` — `FORK:6f740d9` → `FORK:c9daad6` — and `tools/build_engine_atlas.py`); they landed as `f6d7af27 [fix] Clear main's red Validator Unit Tests` while this plan was being written |
| `2-ii` | RET-SC: kernel + veto + `parliamentary_*` | IN/SC | BLOCKED | `22`, `28-iii`, `29b` | — | 3 | [SETTLED: `systems/social_contest/sim/contest/` exists, 16 files] — the kernel is still on disk |
| `8` | H-98(b) band edge → data | IN/PC | OPEN | — | R-09 | 2 | edge in `seam/ladder.py`; serial with the cells commit |
| `9` | PC-SURRENDER build-or-strike | PC | JORDAN | J-7 | — | 4 | `HANDOFF_PC.md` [CODE] |
| `10` | U5 / R-07 stance write | IN | REVERTED (the `tell`→stance write only) | `ED-FI-0009` (E8); E5 | R-07, R-01 | 2 | PR #442 (`c6f4252`) landed the side findings — H-62's `(Person, stance)` producer gap recorded closed by `march`'s M4 write, and the `names_index.yaml` `stance` entry — and reverted the `tell` write itself on H-79 [CODE `HANDOFF_IN.md`]; **re-scoped** to a RESOLVE-time write on a resolved `fight`'s subject, on `_eff_march`'s M4 precedent (A-12, `_part4` §`10`); Fable's WITNESS-side candidate is rejected — it contradicts `write_matrix.yaml`'s `(Person, stance)` row (`class: ACTS`, steps RES/ENC) [SETTLED: read]; whether a *telling* moves stance is J-12; [SETTLED: `def stance_delta` absent] |
| `11-fix` | U6 instrument repair | IN | OPEN | — | R-01, R-02 | 2 | `wd_collect.py`'s `probed`-invariant fails at `default` (`requirements.yaml` R-01 U10 paragraph) [CODE] |
| `11` | U6 — first corpus R-01/R-02 reconvergence rate | IN | BLOCKED | `11-fix` | R-01, R-02 | 2 | no number since the corpus grew 89 → 143 |
| `12` | H-62-rest scar rebuild | IN | BLOCKED | cells commit | R-06, R-08 | 4 | |
| `12b`/`12c`/`12d` | affiliations · THE FIFTEEN · THE RENAME (substrate half) | IN | JORDAN | J-1 | R-05, R-06, R-08 | 4 | `ED-IN-0261` 2026-09-28 row `needs_jordan: true` [CODE]; `12d` season side done (`ED-IN-0268`) |
| `12e` | H12 / H13 | IN | BLOCKED | H6 re-measure; G-Q6 (J-5) | R-06 | 4 | |
| `13`-rest | W28-cast: 41 NPC + 97 ARC overlays | IN | PARTIAL | — | R-09, R-06 | 2 | 5 of 46 NPC overlays, 1 `capability` value (2026-09-28 plan §8.7) [PLAN]; `requirements.yaml` R-09 still says capability is empty everywhere — stale |
| `13d-iii` | rung ANCHORS for seats + `[NEW]` seats + remit overlay | IN | OPEN | `17` (shared `populated.py`); remit half J-8 | R-04 | 2 | H-163 limit 1 [CODE]; realm `levy.unauthorized` 19 of 20 [RAN aperture] |
| `14` | U7-own: own-verbs in antonym pairs, `tie / knot`, CANDIDATE-WHY | IN | OPEN | `10` (shared rows) | R-05 | 2 | none of `carry comply construe destroy_record evade/defy exchange forge give oblige repudiate succeed thread_read tie/knot` executes in the realm [RAN aperture] |
| `R05-THREAD` | `thread_read`'s operand (H-85) | IN | OPEN | rides `14` | R-05 | 2 | answered at ladder step 4 (A-7); no position owned it |
| `17` | U8 `ambitions(p)` + cast seating | IN | OPEN | `14` (shared `rosters.yaml`) | R-06, R-09 | 2 | [SETTLED: `def ambitions` absent in `engine/season`] |
| `19b` | U7-disp: `comply` · `evade / defy` · `construe` | IN | JORDAN | J-2 (`ED-IN-0210`) | R-05 | 4 | |
| `20-iv` | d.1 + terrain/garrison on the season path | MB/IN | BLOCKED | `29b` | R-04 (texture) | 1 | `fortification_of` (`queries/world_q.py`) read by no battle [CODE] |
| `21`-rest | U10 bookkeeping: R-03/R-09 `measured:` refresh | IN | PARTIAL | after `11` | — | 2 | item 3 (reconcile the progress board) **closed, ladder step 2**: the board was retired at `ebb43bf0` and m1 row 3 now reads THE NINE |
| `22` | PROC-B steps 11(rest)–16 | SC | PARTIAL | — | R-05, R-09; M2 | 3 | steps 6/7/9/10 done, 8 built, 11 partial (`cardinality` form unimplemented) [PLAN 2026-09-30 §3 l] |
| `22a` → `23` → `22b` | proceedings PHASE 3 · PART-E-0/2 · PHASE 4 | SC/IN | BLOCKED | `22` | R-05 | 3 | |
| `24` | SE-BUILD umbrella | SE | PARTIAL | — | — | — | re-scoped into `24d`–`24h`; tracked by those rows only |
| `24g` | bodies clock + P3 individuation | SE | JORDAN | J-6 (`ED-IN-0247`) | R-07 (texture) | 4 | |
| `24h` P5 | S5 revolt Query | SE/IN | OPEN | — (`20-ii` ✓) | R-06/R-07 texture | 3 | the 2026-09-28/09-30 rows read BLOCKED whole; only P7 is |
| `24h` P6 | forswearing (`repudiate` costs) | SE/IN | BLOCKED | `14` | R-05 | 3 | |
| `24h` P7 | dispensation-as-document | SE/IN | JORDAN | J-10 | — | 4 | |
| `26` | GO-VERSION | GO | JORDAN | J-9 | M3 | 4 | nothing may assert a version |
| `27` | WR-SCOPE remainder | WR | PARTIAL | — | — | 2 | PR #442 (`c6f4252`): `systems/threadwork/sim/coherence.py` reshaped to the elastic/plastic model (`ED-WR-0010`) + `operations.py`'s P-25 scale term, covered by `tests/valoria/test_coherence_elastic_plastic.py` (25 passed, re-run by the orchestrator 2026-10-01) [TEST]; remainder: `rendering.py` stubs, `ED-WR-0003`, mending cost, the R-14 term |
| `28-iii` | SPINE-DELETE | IN | OPEN | — (`28-ii` ✓ by its letter; see note) | R-04 (reason-2 text) | 1 | spine on disk [CODE `ls`]; ⚠ `28-ii`'s battle evidence is `test_march.py` only — every realm `march` is declared then refused at ENCOUNTER (11/11) [RAN aperture] |
| `29a` | overview trees minus `ms_track` | IN | BLOCKED | `28-iii` | — | 1 | |
| `29a`-ms | `ms_track.py` | IN | BLOCKED | `27` | — | 3 | `threadwork/sim/co_movement.py` imports it lazily |
| `29b` | factions + `game_state.py` + descriptor faction block | IN | BLOCKED | `29a` | — | 1 | 8 `game_state` importers in `systems/` [CODE] |
| `29c` | settlements `.py` | SE | BLOCKED | `29b`, `29d` | — | 1 | geography YAML stays |
| `29d` | world | IN | BLOCKED | `29b` | — | 1 | re-gated off `10` (A-6) |
| `29e` / `29f` | characters / fieldwork `knots.py` | IN | BLOCKED | `14`, `27` | — | 3 | `threadwork/sim/opposing.py` imports `sustain_knot` |
| `ED-FI-0009` | investigation degree producer | FI | OPEN | `8` (shared `seam/ladder.py`) | R-05, R-09 | 2 | the six inquiries resolve Failure/none only today [RAN corpus degree histogram] |
| `LADDER-MBPC` | the MB/PC lanes' flagged `needs_jordan` rows, through the five-step ladder | MB/PC | OPEN | — | — | 2 (parallel) | `ED-MB-0039/0041/0045`, `ED-PC-0016/0047/0049`–`0055` never opened (2026-09-28 plan §9); survivors join `_part5` §J |
| cells commit | H6 + H8 with `12b`/`12c`/`12d` | IN | JORDAN | J-1 | R-05, R-06, R-08 | 4 | then H7 → H3 → H9 → `12` → H10 → H11 → `12e` |
| `28-0` follow-up | `systems/characters/sim/beliefs.py` and the rest of the OI-17 set | IN | BLOCKED | `28-iii` | — | 1 | 12 of the 13 `_OI17_FULL_MODULE_ENTRYPOINTS` targets wait on `28-iii`; `rendering.py` is `27`'s |

**Hole-register rows that gate a position but that no position owned until now** (each is placed at a
batch; `_part3`/`_part4` give the step): **H-163** limit 1 → `13d-iii` · **H-94** (`office` operand) →
J-3 · **H-156** (always-refused verbs crowd the scene budget) → J-4 · **H-165** limit 2 (no person-side
works channel) → a `14` ride-along decision, `_part4` · **H-158** (`via` on a computed `transfer`) →
`13d-iii`'s falsifier reads it · **H-161** (`cardinality`) → `22` step 11 · **H-150** → `20-iv` ·
**H-175** (why `corpus_run`'s 143 cases never give `march` a referent) → a measurement step in
`_part2` §R-04 · **GD-1** (victory has no rule) → [SETTLED: not registered — `grep "GD-1\|victory"
engine/season/hole_register.yaml` finds nothing] → registered as an `ABSENT_RULE` row at `28-iii`.
