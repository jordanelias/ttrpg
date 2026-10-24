# Valoria — Master Workplan v9: the one plan for every lane — what is genuinely open, in build order

## Status: RATIFIED on merge (ED-1094, ED-IN-0286) — held back: §K; the common-fact store (RS-29, `_part5` §J.2 row 7)
## Lane: IN (cross-cutting). It is the ONE active plan (`CLAUDE.md` §2) for all nine lanes — IN, SC, SE, MB, PC, FI, WR, GO, FA. **No carve-out:** the 2026-10-01 telling workplan is absorbed (§0.6).
## Reads in order: this file (how to read, milestones, start here, state index, crosswalk) → `_part2` (THE NINE, one section per row) → `_part3` (orchestration: dependency graph §A, the file-affinity batches §B with their membership rules and handoff cards, file-collision matrix, pre-flight) → `_part4` (IN I: the instruments, the modules specs, the telling tail's G5, G8) → `_part5` (IN II: cells, verbs, forcing, cast; §A answered; A-25; §J the Jordan queue) → `_part6` (SC, SE, FI) → `_part7` (MB, PC, WR, GO, FA) → `_part8` (standing content; §K the adoption ledger; the Layer-0/1 edits owed).
## Grade under `CLAUDE.md` §0.2: `paper` throughout. A plan, not an execution artifact. Every reading here names its command and the date it was read; the evidence is the thing cited, never this file.

**Verb rename (2026-10-16).** The verb this plan, `requirements.yaml`, `hole_register.yaml`, the ledgers and the earlier proposals call `levy` (it moves `Rung.stores` into a seat's treasury) is now `requisition` in the code, the verb table, the event names (`requisition.taken` / `.refused` / `.unauthorized`) and the tests. Dated measurements and quotations below keep the name they were made under; read `levy` there as `requisition`. Jordan: *"levy typically doesn't refer to goods/stores. that verb is wrong as currently used"*. `levy` is reserved for the verb that raises troops: `proposals/2026-10-16-troop-stock-design.md` (PROPOSED).

**Why this exists, in Jordan's words (2026-10-06, verbatim).** *"…collate all information gathered including unfinished
workplans v8, sort and organize all information into lane-based categories, adjudicate stale vs fresh then ratify all
provisional as required so long as it is not superseded, adjudicate dependency orders, sift lane-based categories based upon
interdependency requirements and build sequencing, reconcile all items accordingly such that only the genuinely open items
are remaining, orchestrate all these items into a new v9 master workplan that supersedes everything…"*

**What it supersedes.** v8 (`valoria_master_workplan_v8.md` + `_part2`…`_part6`, PR #448) and the telling workplan
(`2026-10-01-telling-workplan.md`, `ED-IN-0282`, PR #449). Adoption (B-A) retires both — delete plus one exact-file
`FORK:` row each in `references/restructure_ledger.md`, target = the adoption commit's parent — with the proposal files the
Gather's dispositions retire (the list: `_part8` §K (b)). The plans v8 retired stay at `FORK:0671283`. **None of them is an
owner of anything any more:** where this plan needs their content it carries the text; a pointer to one is *history* only.

**How it was produced.** A read-only adjudication over HEAD `8b57336` (2026-10-06) classed every v8 position, handoff row,
`absent` hole-register row, flagged ledger row and in-window proposal as open, stale, superseded, merged or cut; answered the
Jordan queue through `CLAUDE.md` §0's five-step ladder; and sequenced the survivors. It is not a repo artifact: each row here
carries its own evidence, and a medium-confidence verdict says so at its entry.

## 0. HOW TO READ THIS PLAN

### 0.1 What it owns, and what it does not

| it owns | it does NOT own | owner |
|---|---|---|
| **THE ORDER** the remaining work is done in, every lane | per-lane **status** | `registers/handoffs/HANDOFF_<LANE>.md` |
| **WHAT** each open position does, its files, falsifier and gate | **which head is canonical** | `CURRENT.md` |
| **WHO** can answer each open question (`_part5` §J) | **whether the behaviour runs** | the instruments: `register --requirements`, `m1_acceptance.py`, `corpus_run`, `aperture`, the tests |
| the milestones M1/M2/M3 and what each is measured by | a figure — every number here is a dated reading of a named command | re-run the command |

v7's rule carries: **this plan has no status column except the one state index (§3), and every row of it cites its
evidence.** A status written twice drifts within days. If a row and its instrument disagree, the instrument wins and this
file is wrong.

**Binds (does not fork):** `references/id_reservations.yaml` (allocation protocol, `CLAUDE.md` §4) ·
`references/lane_assignments.yaml` (its `source:` names v8 until B-A re-points it, `_part8` §H.3) · `HANDOFF.md` + the
lane files · `CURRENT.md`.

### 0.2 The state classes

| `STATE` | meaning |
|---|---|
| **B** | buildable. `GATE` is `—`, or names only an ORDER edge (`_part3` §A: D data · F file · I instrument · R ruling) it sits behind. **A `GATE` of `—` is buildable today** |
| **BLK** | a named position must land first |
| **J** | a decision or authored content is owed, named exactly in `_part5` §J |
| **ask-then** | the question is put to Jordan when the named position lands; it holds no place in §J's ranked queue |
| **HELD** | Jordan held it (`_part5` A-24); carried, never scheduled |
| **LEAVE** | named so it is not lost; no position schedules it |
| **DONE-realm / DONE-test** | used only where an open item depends on the distinction: *DONE-test* = a dedicated test executes it from a constructed input; *DONE-realm* = it also occurs in `populated.build_realm(0)` run through the real chooser (`aperture 4 0`). §0.2 accepts both as done; R-row moves usually need the second |

Finished positions are not in the state index (`CLAUDE.md` §2: *"Finished positions leave the plan; the commit is their
record."*). v8's one-line history (its `_part6` §H.1) is not carried; read it at v8's `FORK:` ref.

### 0.3 Numbering (carried from v8 §0.3, itself from the 2026-09-28 plan §0, `FORK:0671283`; it still binds)

No existing position number changes meaning. Every surviving v8 number (`31a`, `22`, `19b`, `9`, `26`, `33`, `36`,
`2-ii`, …) is kept as the **ALIAS** of a v9 handle. **The v9 handle is lane-tagged, `<LANE>-nn`** (§3; §4 maps both ways,
plus the #453 and #457 handles). A position added after adoption continues its lane's run of handles; a bare number (from
`37`) is used only for a position with neither an alias nor a handle — none today. A handle's batch is `_part3` §B's; `B-A`…`B-Z` are file-affinity batches (§B.0's rules place a late position), not a count of phases. Retired numbers and handles are never reused (§4,
last list). **None of these handles allocates a ledger id.** An id is allocated when the position is built.

⚠ **One collision, named so nobody resolves it by guessing.** In the 2026-09-28 plan's Phase-1 list, "item 11" was position
`25` (MB-GOLDEN, DONE). Position **`11`** is U6, the first R-01/R-02 corpus measurement, re-taken at B-G (as the control, `0f998f64`), B-I and B-M
(`_part3` §O.2, E15). `11a`/`11b` are DONE. This plan uses handles and position numbers only, never Phase-1 item numbers.

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

**SUPERSEDED IN PART, 2026-10-06 (Jordan: *"code review and simplify to be at batch close"*):** phases 2 and 3 run once per
BATCH at the close (`methodology-execute`'s BATCH-CLOSE; `methodology-close` Phase 2), not at each step. Phases 1, 4 and 5
stand per step.

**FORWARD SWEEP — defined, because it is a coinage and `CLAUDE.md` §4 requires it survive the session reset.** *What did
this change reach that nobody asked it to?* Five checks, each with an artifact:

1. **The instruments.** `python -m engine.season.harness.register --requirements` · `corpus_run` ·
   `python tools/m1_acceptance.py --summary`. **Did any row move, and is every move the intended one?** An unintended move
   is the finding.
2. **The hole register.** Did this close, narrow or widen a row — and does its falsifier now behave as the row predicts? A
   row whose falsifier did NOT flip when the code says it should have is the most valuable thing this sweep can catch.
3. **The call sites.** Grep the changed symbol's callers, not its declaration (`CLAUDE.md` §0.1 pt 3 row two: *a roster
   existing is not a roster being used*).
4. **Figures the change just made stale.** Any `measured:` block, `cite:` field, handoff or plan row quoting a number this
   step moved. **This is the defect this repository pays for most** — §0.1 pt 3 row four — and a sweep that skips it hands
   the next session a confident wrong number.
5. **The goldens.** Did anything output-moving change, and was a re-record INTENDED? Nothing verifies a golden re-pin was
   deliberate (`CLAUDE.md` §7), so say so plainly when one happens.

**The sweep's output is edits plus at most one paragraph in the commit message** (`CLAUDE.md` §0's adversarial-pass
bound). It creates no document and no directory. A finding that needs no ruling is fixed in that commit or dropped.

### 0.5 Verification cadence, stopping rule, and what every producer must not do

- **Suite cadence (`CLAUDE.md` §0.4, RULED 2026-09-23).** Mid-step: only the file covering the edit.
  `python -m pytest tests/valoria -q -n auto` (and `engine/season/tests`, `engine/tests` where the batch can reach them)
  runs **once per batch close**, as `methodology-execute` prescribes — never to re-confirm a green already held. ⚠ The
  2026-09-18 cadence put the suite at every step's CLOSE; the later §0.4 ruling (*"stop running suites so frequently"*)
  governs, and this is the reconciliation.
- **THE STOPPING RULE.** A falsifier that fails → `git revert` that position's commit(s) (never `--no-verify`, never
  skip/xfail/quarantine a test) → append **one** `hole_register.yaml` row only if the gap is measured, **one** ledger row
  only if a human decision is needed (`needs_jordan: true`, after the five-step ladder) → record the attack in the commit
  message → continue with the next gate-free item. **Never widen the position to make the falsifier pass.** `10`'s
  2026-09-29 revert (H-79) is the precedent.
  **RULED 2026-10-13 (the session's user: *"Relax exit rules."*), applied to every position's EXIT and FALSIFIER:** a
  verb position is BUILT when it is wired and proven by a falsifier on a hand-built world (the cause controlled, a
  mutation red): DONE-test (§0.2), which `CLAUDE.md` §0.2 accepts as written — a test that drives the verb through the
  real fold is an execution artifact. Its executed count in the realm is **not required and not taken for it**; when a
  propagation reading (TEST HORIZON, below) runs, the verb's row is recorded at its hole row. The stopping rule reverts
  a falsifier that fails on a hand-built world; it does not revert a verb for executing 0 times through the real
  chooser, whose selection is authored alignment-cell and character data, not wiring. **No test asserts that a verb
  executed in the seed-0 realm:** the ones that did (IN-53 (e), IN-10 (a) (4), IN-09 (7)) and their shared four-season
  fixture were deleted under this rule on 2026-10-13 — deleting an assertion a ruling retired, never a skip or xfail.
  Positions reverted at B-I for a realm count of 0 (IN-09's `evade / defy` and `construe`, IN-33's `exchange`) are
  restorable from their checkpoints under this rule (`_part5` IN-09, IN-33). An entry's EXIT or FALSIFIER still
  written as "executes ≥ 1 in `aperture 4 0`" or "0 times → not built" reads under this bullet. It relaxes a
  POSITION's exit, not a requirement's `met`: R-04's and R-05's `met` still read computed play through their own
  `measure:` (`engine/season/requirements.yaml`) [ASSUMPTION; medium; the user to correct. Revert: those `met`s read
  DONE-test too, an edit to `requirements.yaml` and `_part2` R-04/R-05].
- **CI CADENCE, RULED 2026-10-13 (the session's user; the words and the mechanics — `[skip ci]`, baselines — are in
  `methodology-execute`'s CHECKPOINTS AND BASELINES; where CI falls among the closing phases is `methodology-close`'s).**
  CI runs twice per batch: at its end, and once more to confirm the commit carrying every fix, CI's and the closing
  sequence's. No WIP checkpoint or other commit in between starts a run; a one- or two-season probe or the covering
  test file judges a change in between. The previous CI run is the baseline for the next: readings are not re-taken.
- **TEST HORIZON, RULED 2026-10-13 (the session's user: *"a verb error etc in season 1 is just as valid as a verb error in
  season 4 because the issue is with the machinery itself"*; *"whatever season has the error is the season that is the last
  in sequence for testing"*).** A probe or test runs season by season and ENDS at the first season in which a verb errors;
  it does not run on to a fixed season count. An error at season 1 is as real a defect as one at season 4 (a refusal, an
  `InstrumentDefect`, a gate raise). A fixed four-season run is only for a reading that needs four seasons to occur.
  **`aperture 4 0` runs only when how a change PROPAGATES over game time is what is being evaluated, never as a
  per-verb execution gate** (RULED 2026-10-13, the session's user: *"the point of aperture 4 0 0 0 to simulate four
  seasons is to see how the simulation propagates changes and behaves accoridngly over a longer period of game time.
  there's no point running it in full unless we're evaluating how something propagates over time"*). [ASSUMPTION;
  medium; the user to correct: a requirement row's `measure:` naming it (R-04, R-05) is such a reading, taken when
  the row is measured, not per position. Revert: those rows move to a shorter horizon too.]
- **Must NOT, in any batch:** edit `.designs/` or `.audit/`; cite a `.md` as the reason a behaviour is correct; build a
  guard whose subject is process (§0.1 pt 5); create a directory or standing document; author a cell, a Godot version, or
  a Jordan item's answer; build anything in `engine/mc_v18.py`;
  `git add` a file another lane is editing (use `isolation: worktree`); re-fetch from the GitHub API; write a count into
  `CURRENT.md`/`HANDOFF.md`.

### 0.6 The telling workplan — ABSORBED, not carved out

`workplans/2026-10-01-telling-workplan.md` (RATIFIED by Jordan, `ED-IN-0282`; T0–T6 built, PR #449 `fd321c81`) was v8's one
carve-out. Jordan's word that v9 *"supersedes everything"* ends it: adoption retires the file (`FORK:` row; its As-built
record stays at that ref and is not carried) and writes one superseding row on `ED-IN-0282` — *absorbed into v9; nothing
re-ruled*. What it still owed is scheduled under IN handles in `_part4`, its gate and trigger text carried unchanged: T7
(G9, declared intent) is IN-16; the owed measurement and the `absent` re-check of H-180/H-181/H-182 are IN-17; the gated
tail G1–G8 is IN-18. IN-16, IN-17 and IN-18's step 2a, G1, G2 and G3 landed at B-E (`ac9724fc`), G6 at B-I (`66bf51f9`); G5 and G8 remain
(`_part4` §4.4). Its rulings stand as written: `tell` writes no stance and told valence enters regard at read (G1; AX-3),
so v8's withdrawn `fight`-write rewrite of `10` stays withdrawn, `10` is retired (§4) and former J-12 stays closed. Of v8's
edges against it, E14 and E16 are spent (T4 and T6 landed); E15 survives, re-keyed to v9's batches (`_part3` §O.2).

## 1. THE MILESTONES — what "done" is measured by (re-read on HEAD `8b57336`, 2026-10-06)

### M1 — ONE PLAYABLE SEASON

**Instrument:** `python tools/m1_acceptance.py --summary`. **[RAN 2026-10-06, HEAD `8b57336`, exit 0] verdict `NOT MET`, 1 row failing.**

| # | row | reading | kind |
|---|---|---|---|
| 1 | stub invocations on the M1 path == 0 | **PASS** — 1-season headless run of `engine/season` | executes |
| 2 | same seed → same `World.content_hash()` | **PASS** — two runs, hashes equal | executes |
| 3 | the nine requirements met | **FAIL 2/9** — met 2 · partial 5 · not_met 2 | ⚠ DOC-DERIVED: counts `status:` strings, each validated by `register --requirements`; not execution |
| 4 | N seeds, zero invariant violations | **PASS** — 0 violations | executes |

**[RAN 2026-10-10, HEAD `627e4bc6`, `register --requirements`, exit 0]** the count row 3 reads: met 3 (R-01 R-02 R-03) · partial 5 (R-04 R-06 R-07 R-08 R-09) · not_met 1 (R-05). R-01 flipped at B-I by its verbatim `met` (`wd_collect.py`; `engine/season/requirements.yaml` R-01).

Row 1 was re-pointed from `mc_v18` to `engine/season` on 2026-09-13. **M1 is now exactly THE NINE.** Row 3 greens when all
nine rows read `met`, and a row reads `met` only on a `measured:` block `register --requirements` accepts — so M1 is closed by
`_part2`, nowhere else. Row 3 stays DOC-DERIVED by its own declaration; do not re-wire it to anything a status edit could green.

**⚠ Two rows cannot read `met` under v9 as it stands, and so neither can M1 (`m1_acceptance.py:320` passes only when every row is met):** R-04's conjunct (3) waits on IN-46 and IN-47, which are design positions with no build batch until their designs are reviewed; and R-09's by-person pool waits on a ruled SOURCE for `capability` (J-13 (iii) is the adopted interim, which leaves the by-person conjunct partial). Both are stated at their rows (`_part2`) and in `_part3` §A(4).

### M1's companion — THE NINE

**Instrument:** `python -m engine.season.harness.register --requirements`. **[RAN 2026-10-06, exit 0] met 2 (R-02 R-03) ·
partial 5 (R-04 R-06 R-07 R-08 R-09) · not_met 2 (R-01 R-05).** `_part2` has one section per row: statement, measured
reading, what moves it, what no position yet owns, `met` as an instrument outcome. Critical paths: `_part3` §A(1).

### M2 — THE ANY-SEED STORY BAR

v7: *N seeds each yield a chronicle that is connected, continuous, rooted, live and distinct* — M1's invariant sweep
generalized. **Its precondition is met** (M1 row 4, read above). **Its instrument landed at B-C:** `harness/storybar.py`
(IN-19, #457 STORY-BAR — cross-person antecedent share and chain depth per season over N seeds, forcing arms compared; it
grades nothing) and `harness/soak.py`'s cost and act-mix grades (IN-20). `corpus_run`'s `ARC ENDS` count prints
`NOT-COMPUTABLE — closed by W23 + W26 + W30` [v8's reading, 2026-10-01; not re-run here]. Candidate gates:
(i) THE BAR for proceedings, built at SC-01 step 16 (`22`; `801f733e`, B-N closed `cf69ceed`) as a test on seeds picked from a
sweep (`engine/season/tests/test_sc01_the_bar.py`: the chain can close with zero authored acts, not that it usually does);
(ii) `corpus_run`'s ARC ENDS becoming computable, not built, and (iii) a chronicle render, `engine/season/harness/chronicle.py` (IN-37, landed `bd5d5b45`) (the
`chronicle` witness channel's deletion at SC-01 step 13 is held, `hole_register.yaml` H-214: it waits on the `<rung kind>`
reach channel). Path: SC-01 step 16 (landed `801f733e`) → IN-37 (landed `bd5d5b45`) → IN-27 (#457 D6, the ending vocabulary:
answered as the plan's recommendation, RS-21 item 3; landed `6ae70998`) (`_part3` §A(2)).

### M3 — GODOT VERTICAL SLICE

Last, unchanged in substance: GO-01 (`26`). **The Godot engine version is UNRESOLVED and nothing here asserts one**
(`_part5` §J, J-9). `godot/godot_conversion_strategy_v1.md` is PROPOSED and HELD (§K); its version string was struck and its
Key-runtime rows marked RETIRED at B-C (GO-03, landed). `references/module_contracts.yaml`'s `engine_clock` row got its `doc:`
(the propagation spec) at B-C (IN-42 = GO-02, landed). `engine/autoload/engine_clock.py` is deleted (`28-iii`, PR #450); the temporal spine is `engine/season/loop/driver.py` +
`loop/calendar.py`, which that row describes, so `CLAUDE.md` §6's "starting with `engine_clock`" means the season calendar
(Layer 0: listed at IN-44, not edited here). `godot/skeleton/` is not a head start. Path: GO-01 (J-9) → GO-05 (its IN-05 gate met: B-L closed, `fc4f3ba9`)
(`_part3` §A(2)).

## 2. ⭐ START HERE — the first commands the next session runs

```sh
git rev-parse --short HEAD; cat .git/shallow 2>/dev/null || echo "full clone"   # a shallow clone unshallows first (CLAUDE.md §2)
python tools/session_provision.py
python -m engine.season.harness.register --requirements        # read the output; the command holds the counts, not this file
python tools/m1_acceptance.py --summary                         # read the output; the command holds the verdict and the row-3 fraction
gh run list --branch main --limit 3                             # read `All Gates Green`
```

**How a session works from here.** One session works ONE batch, then its context is cleared; continuity is the batch's HANDOFF
line (`_part3` §B.2) and git. At the boundary the batch's finished positions are deleted from the plan in one net-deleting
commit and the run stops for a cleared window (`methodology-execute`, `CLAUDE.md` §9). The first batch is **B-A**, the adoption of this plan (`_part8` §K): it opens only after Jordan
has read §K's still-held list and `_part5` §J. `main` was red from PR #456 on one test
(`test_flow_skeletons.py::test_contract_names_resolve_in_the_generated_index[combat]`); the one-line fix (`personal_combat`
joins `RETIRED_CONTRACTS`) is built and rides the adoption branch (`7b619328`), so it is not a position — read `All Gates
Green` on `main` once the branch merges. B-C is closed. B-D is closed: D1 (`9054df80`), D2 (`b31d2c31`), D3 (`0a690b30`). B-G is closed (`0f998f64`). B-H is closed (`c13144b9`). B-E is closed (`ac9724fc`). B-F is closed (`53807be4`). B-L is closed (`fc4f3ba9`). B-I is closed (`9d93cfab`); what it left open is in the entries (§3: IN-09, IN-18, IN-33). B-J is closed (`42c5588c`: SC-03a, IN-40, FA-01's mechanism, IN-31's design; IN-48 left as B-JR). B-W is closed (`3bf936ee`: IN-54, IN-55, IN-56, IN-57, IN-58's stance-only half). B-X is closed (`2f0c0227`: IN-62 … IN-69, IN-71, IN-72, FA-04 … FA-06; what it left open is in `engine/season/hole_register.yaml` H-209, ED-IN-0296 and `_part3` §B's header). B-K is closed (`c8d1db3a`: IN-10, IN-45's `forge`, `carry`, `migrate`, `survey` + Rung, IN-49, IN-28 with SE-03; what it left open is in `_part5` IN-45 (`work`, ED-IN-0297) and `_part3` §B's header); B-M is closed (`be02666e`: IN-12 step 6, `5ea1bb47`, and IN-13, `2e19aee8`; the realm still fights 0 fields: `_part2` R-07 conjunct 3); B-N is closed (`cf69ceed`: SC-01 steps 11–16 and the fired-slot step; what it left open is in `engine/season/hole_register.yaml` H-161, H-163, H-214 and `_part3` §B's header); then … the spine `_part3` §B names. Every batch runs
through `methodology-execute` (`CLAUDE.md` §9), and a batch's READ-FIRST list names the sites to read (the pins file is far too
large to read whole: grep the assertion).

## 3. THE STATE INDEX — every open position, all lanes, one row each (generated from the entries; read 2026-10-06)

**Read from the entries, not hand-kept:** each row is read from its entry's `STATE`/`LANE`/`BATCH`/`R` line in the
home part; no tool generates it (`CLAUDE.md` §0.1 pt 5), so a row that disagrees with its entry is wrong — the entry wins and the row is re-read. When a batch closes, its positions leave the plan (`CLAUDE.md` §2) and their rows leave with them. The full entry
lives once, at the home part; a row reading `= X` is an alias whose entry is X's. `GATE` here is the head of the entry's gate —
the entry holds the whole of it. Evidence tags (`[RAN]`, `[CODE]`, `[PLAN]`) live in the entry, not here. `R` = the R-rows or
milestone the position moves. `batch` = `_part3` §B (a position in two batches lists both, in landing order). Closed positions
are not here (`CLAUDE.md` §2) — among them the CI fix that had left `main` red, built at `7b619328`.

| handle | alias | lane | STATE | GATE (the entry holds the whole of it) | R | batch | home |
|---|---|---|---|---|---|---|---|
| IN-09 | `19b`: `evade / defy`, `construe` (`comply` landed `128299db`) | IN | B | — (restorable under §0.5: `a1c83e62`, `60073e75`) | R-05 | none (B-I closed `9d93cfab`) | `_part5` |
| IN-12 | #453 steps 5, 5a: their remainder (step 5's built half `34642a96`; 11 `68eaaa41`, `give` + Rung `c6459377`; 6, 7, 9, 10, 13: `5ea1bb47`, `664986ee`, `996c16dc`, `67686661`, `5da7c44e`) | IN/SC | BLK | H-226, H-227, H-209 | R-04, R-05 | none (B-R closed `541c8d12`) | `_part5` |
| IN-14 | #457 BOUND-ATTENTION; H-92, H-10 | IN | ask-then | — | — | B-Z | `_part4` |
| IN-18 | telling G5, G8 (step 2a, G1–G3 landed `ac9724fc`; G6 landed `66bf51f9`) | IN | BLK | G5's trigger, M0e > 0 (`oblige` landed `905b7a21`) | — | none (B-I closed `9d93cfab`) | `_part4` |
| IN-30 | `24h` P5 remainder; H-186 | IN/FA/SE | stopped | H-149 (`raze` landed `68eaaa41`) | — | none | `_part5` |
| IN-32 | H-182 ties | IN/FI | B (narrowed: attempted `53ed995d`, falsified by its own stopping rule, reverted `7c6df560`) | — (H-182's `cite:`, H-237) | R-05 | none (B-S closed `6e833a57`) | `_part5` |
| IN-33 | H-58 `exchange` | IN | B | — (reverted `cdc03f67`; restorable under §0.5: `ad2f930f`..`b5c4685d`) | R-05 | none (B-I closed `9d93cfab`) | `_part5` |
| IN-36 | #457 FORCE-FOREIGN | IN/FA/MB | B (landed `7c59d74c` at B-V, closed `b1eabf5d`; narrowed) | IN-13 (landed `2e19aee8`; B-M closed `be02666e`) | — | none (B-V closed) | `_part5` |
| IN-38 | `13`-rest | IN | B (landed `1dcfce10`, narrowed) | — | R-09, R-06 | none (B-V closed) | `_part5` |
| IN-44 | SM-10, SM-12; A-24's wording | IN | J | Layer 0/1: Jordan's files | — | — | `_part8` (table, not an entry) |
| IN-45 | `work` (`forge`, `carry`, `migrate` landed at B-K) | IN/SE | J | ED-IN-0297 (`needs_jordan`) | R-05 | none (B-K closed `c8d1db3a`) | `_part5` |
| IN-46 | = SM-6 | IN/PC | B | build (design landed at B-C); no build batch | R-04 | none (re-read at B-L, `e77794a2`) | `_part4` |
| IN-47 | #445 (character sheet) | IN/PC/WR | B | review (design landed at B-C); no build batch | R-04 | none (reviewed at B-H, `c13144b9`) | `_part4` |
| IN-48 | H-108 (delegation half) | IN/FA/SE | B | — (IN-40 landed `3f320093`; IN-10 (a), (b) and IN-11 landed `905b7a21`, `2a2ed152`) | R-04 | B-JR | `_part5` |
| IN-52 | the levy-to-field feed's flip ON (built OFF `128bc9db`); LF-1..LF-3 | IN/SE/MB | BLK | `requisition` executing in computed play (H-163 limit 3(a)) | — | B-Z | `_part4` |
| IN-58 | RS-23, RS-24: grievance at read — its sworn-to half (the stance-only half landed `3bf936ee`) | IN/FA | BLK | IN-40's `oblige` edge readable person-side (D) | R-07 (contributor) | none (B-W closed `3bf936ee`) | `_part5` |
| IN-61 | RS-27: succession (replaces IN-51, retired); #453 R-5 (b) re-specified | IN/FA/SE | stopped | H-230 (limits (1), (2)); SC-04's `succession` row (H-217: IN-61 owns it); ED-IN-0292 (2) (J) | R-05, R-04 | none (stopped at B-R, closed `541c8d12`) | `_part5` |
| SC-02 | `22a` → `23` → `22b` (RESIDUE after B-P, `eba20137`) | SC | BLK | H-218, H-219, H-221, H-222; ED-SC-0040 (J) | — | B-Z | `_part6` |
| SC-03b | #453 step 4; H-162 | SC | BLK | SC-08 (SC-01 landed, B-N closed `cf69ceed`; SC-03a landed `c2f855d2`) | R-05, R-04 | B-O | `_part6` |
| SC-04 | `18` tails (RESIDUE after B-P, `eba20137`) | SC | B | H-217 (IN-61's) | — | B-Z | `_part6` |
| SC-05 | `2-ii`; SM-2, SM-15 | SC | ask-then | SM-15 | — | B-Z | `_part6` |
| SC-06 | SM-1 | SC | ask-then | SM-1 | — | B-Z | `_part6` |
| SC-07 | #445 P-4, V-4, V-5 | SC | BLK | a carrier per item (SC-01 landed, B-N closed `cf69ceed`) | — | B-Z | `_part6` |
| SC-08 | — | SC | B | — (SC-01 landed; B-N closed `cf69ceed`) | — | B-O | `_part6` |
| SE-04 | (b) H-171, (c) #457 CAST-POPULACE; (a) done `dd0a1c5a` | SE | BLK | (b) IN-44; (c) the spread construal (J) | — | B-Z | `_part6` |
| SE-05 | = IN-30 | — | — | — | — | none (= IN-30, stopped) | `_part5` |
| SE-06 | SE-04 (c)'s vector half; ED-IN-0293 reading (b) | SE/IN | J | §J.2 row 4; ED-IN-0296 (written at B-X's close `2f0c0227`, `needs_jordan`) | R-06 (contributor) | B-Z | `_part6` |
| MB-07r | J-18 (A): flip the depth support cap ON | MB | BLK | J (recalibration; the golden gate's time budget) | — | B-Z | `_part7` |
| MB-08 | #445 U-1, U-2, U-6 | MB | LEAVE | named, unscheduled | — | B-Z | `_part7` |
| PC-05 | ED-PC-0013 (1) | PC | BLK | GO-01, GO-05 | — | B-Z | `_part7` |
| PC-06 | #445 K-1/K-5 (K-3 landed at B-S, `1023197b`; S-1 landed at B-E, `ac9724fc`; M-1/S-4, S-2/L-1 at B-L, `9ad86e87`) | PC | LEAVE (K-1/K-5, unscheduled: K-2 first) | K-2 with its first reader | — | none (B-S closed `6e833a57`) | `_part7` |
| PC-08 | Phase 4a/4b/5, WS-7; #445 M-2..M-6, K-4/V-3 | PC | LEAVE | named, unscheduled | — | B-Z | `_part7` |
| PC-10 | RS-25: duel terms and the yield (PC-10a landed `daae7401`; PC-10b season, STOPPED at B-Y, unbuilt) | IN | BLK:H-240 (design-first stopped; needs a declared grammar change) | H-240 limit (1): a declared grammar change or a derivation route | R-05 | none (B-Y closed `8071ca36`) | `_part7` |
| FI-05 | = IN-32 | — | — | — | — | none (= IN-32) | `_part5` |
| WR-01 | `27` remainder: the R-14 term, the `engine/season/` reach | WR | BLK (narrowed) | a working with a cost running in the season (IN-06's re-review, `759eefb8`, §6 item 11) | — | none (B-S closed `6e833a57`) | `_part7` |
| GO-01 | `26`; D2 tenth attribute | GO | J | J-9 | — | B-Z | `_part7` |
| GO-05 | SM-13; ED-PC-0013 (1) | GO | BLK | GO-01 | — | B-Z | `_part7` |
| GO-06 | `valoria-game` parity | GO | BLK | `valoria-game` checkout | — | B-Z | `_part7` |
| FA-01 | #445 P-3; FORCE-FOREIGN's cast | FA | mechanism landed at B-J; content landed at B-V; the trade-demand clause BLK:J (`ED-IN-0298`) | mechanism landed at B-J | R-04 | B-Z (the clause) | `_part7` |
| FA-02 | = IN-30 | — | — | — | — | none (= IN-30, stopped) | `_part5` |
| FA-03 | #453 §10.2 faction map | FA | LEAVE | reference | — | B-Z | `_part7` |
| FA-07 | the original design's faction-vs-faction mechanisms | FA | LEAVE | named, unscheduled | — | B-Z | `_part7` |

## 4. CROSSWALK — v8 and the proposals ↔ v9

**Batches B-A … B-T, B-U, B-V, B-X, B-Y, B-Z** (B-Y placed by ruling, RS-28, B-W closed `3bf936ee`; B-X closed `2f0c0227`, placed by RS-30; B-U closed `156f3e5d`; B-R closed `541c8d12`; B-S closed `6e833a57`; B-Y closed `8071ca36`, PR #502; B-T closed `2c6684e6`, PR #503; members, shared files, entry gates, exit instruments, re-records, lanes, handoff cards): `_part3` §B, the only copy.

| v8 position · telling · §SM | v9 |
|---|---|
| `B0-CI` · `30` · `31a` · `31b` · `31c` · `33` · `36` | built (`7b619328`; not a position) · IN-02 · IN-03 · IN-04 (= PC-09) · IN-05 (= MB-09) · IN-06 (re-reviewed, landed `759eefb8`; nothing plugs) · IN-07 (landed `befce041`..`5099cb24`; its levy feed split to IN-52 at B-C) |
| cells commit, `12b`/`12c`/`12d`, H6–H11, `12`, `12e`, Phase 6f | IN-08 (landed: the cells commit `0f998f64`, the chain `c13144b9`) |
| `19b` · `13`-rest · pre-flight P-4, P-6 | IN-09 · IN-38 · read at B-C (IN-39, landed; `_part3` §P) |
| `22` · `22a` → `23` → `22b` · `2-ii` | SC-01 (landed; B-N closed `cf69ceed`) · SC-02 · SC-05 |
| `24g` · `24h` P5 · `24` (umbrella) | landed, `d12c8db9` · IN-30 (= SE-05, FA-02) · not carried — its letters are the rows |
| `9` · `26` · `27` remainder · `ED-FI-0009` | PC-01 (landed, `9054df80`) · GO-01 · WR-01 (the reach; WR-02 and WR-03 landed, `0a690b30`) · FI-01 |
| `11` | no handle: re-taken at B-G (control, `0f998f64`), B-I, B-M and B-N (`cf69ceed`) (E15); P-4 passed before it, at B-C |
| SM-1 · SM-2, SM-15 · SM-3 · SM-7 · SM-9, SM-11 · SM-10, SM-12 · SM-13 · SM-5, SM-6 | SC-06 · SC-05 · FI-02 · IN-05 · IN-41 · IN-44 · GO-05 · SM-5 confirmed (RS-6), SM-6 = IN-46 |
| telling T7 · its measurement + H-180/181/182 re-check · G1–G8 | IN-16 · IN-17 (both landed: `ac9724fc`) · IN-18 (step 2a, G1–G3 landed `ac9724fc`; G6 landed `66bf51f9`; G5, G8 open) |

| #453 — `proposals/2026-10-03-verb-coverage-and-gap-fill.md` | v9 |
|---|---|
| §10.4 step 1 · step 2 · steps 2b + 3 · step 4 · step 8 | IN-10 (sub-steps landed `905b7a21`; the enabler `fae9e623`) · IN-11 (landed `2a2ed152`) · SC-03a (landed `c2f855d2`) · SC-03b · IN-13 (landed `2e19aee8`) |
| steps 5, 5a, 6, 7, 9, 10, 11, 13 | IN-12, one sub-entry per open step (11 landed `68eaaa41`) |
| step 2a (`known_persons` widening) | IN-18 (landed at B-E, `ac9724fc`, with its re-pin) |
| "later" (R-5, `inheritance`) | IN-61 (stopped at B-R, H-230; RS-21 item 9, re-specified by RS-27: the heir's claim) |
| R-1(b) R-3(b) R-4(b) R-8(b) R-9(a) · §13.9 kill/wound | adopted at the step each names (§K (a)) · adopted: `kill` and `wound` are not verbs (RS-5, Jordan's own words), only `challenge` → `accept` is added (`_part5` IN-08) |

| #457 — `proposals/2026-10-04-forcing-churn-and-the-story-bar.md` | v9 |
|---|---|
| STORY-BAR · STORY-SOAK · STORY-READ | landed at B-C (IN-19, `harness/storybar.py`) · landed at B-C (IN-20, `harness/soak.py`'s grades) · landed `bd5d5b45` (IN-37, `harness/chronicle.py`) |
| FORCE-WEATHER · FORCE-BODIES · FORCE-HAZARD (+ SEAM-CLOCK) · FORCE-FOREIGN | landed, `3544d568` · IN-34 (landed `44fdb4df`) · IN-35 (landed `23b33e9e`, weight 0) · IN-36 (+ FA-01's cast) |
| CARRY-INTERIOR · CARRY-SHORTFALL · CARRY-STABILITY | merged into IN-08 · IN-22 · landed `c4eb6f84` (IN-23) |
| BOUND-LOOPS · BOUND-STAKES · BOUND-ATTENTION · BOUND-PAPER | instrument landed at B-C (IN-24, `harness/loops.py`; the church ratchet's bound waits on IN-12: IN-10 landed `fae9e623` without its loop half) · IN-25 (landed `ac9724fc`) · IN-14 · IN-26 (landed `ceadc2a7`) |
| CAST-POPULACE · CAST-DISPOSITION | SE-04 · merged into IN-08 + IN-12 step 9 (landed `996c16dc`; J-13 (iii) the adopted interim; `tell` stays uncelled, G-1) |
| SEAM-LADDER · END-VICTORY | merged into IN-04 · landed `6ae70998` (IN-27) |
| §7 D1 · D2 · D3 · D4 · D5 · D6 | IN-35 (landed `23b33e9e`) · IN-34 (landed `44fdb4df`) · answered: no dated pins (T-c) · IN-36, FA-01 · A-24 → IN-06 (landed `759eefb8`) · IN-27 (landed `6ae70998`; D2, D4, D6 answered as the plan's recommendation, RS-21) |

**#445** (`proposals/2026-09-30-character-and-play-surface/`): S-1 → landed at B-E (`ac9724fc`) · M-1/S-4, S-2/L-1 → landed at B-L (`9ad86e87`) · K-1/K-5 → PC-06 · K-3 → landed at B-S (`1023197b`) · U-3 → landed at B-D2 (`b31d2c31`)
· U-1/U-2/U-6 → MB-08 · P-1 → IN-08 · P-2 → IN-22 · P-3 → FA-01 · P-4, V-4, V-5 → SC-07 · S-6 → FI-01 · V-1 → J-2
(answered) · K-2 only with its first reader · M-2..M-6, K-4/V-3 → PC-08.

**Hole-register rows a position now owns:** H-25, H-106 → IN-10's loop half, not built when IN-10 landed (`fae9e623`): the church ratchet waits on IN-12 (their instrument landed at B-C: `engine/season/harness/loops.py`) · H-26 (IN-21 landed `3544d568`) · H-44 (re-scoped at IN-09, `128299db`) · H-47 (IN-06 landed `759eefb8` with no `coherence` field: the proposal's §6 item 4; unowned) · H-48 →
IN-18 G6 (landed `66bf51f9`) · H-51 (SE-01 landed `d12c8db9`) · H-58 → IN-33 · H-59 → IN-12 (`forgive`, landed `5da7c44e`) · H-92, H-10 → IN-14 · H-100 → IN-31 (landed `d16bd895`) · H-101 → IN-40 (landed `3f320093`) ·
H-110 → IN-29 · H-160 → IN-22 · H-162 → SC-03b · H-166 → limit 3's closer `raze` (IN-12 step 11, landed `68eaaa41`; its limits: H-228) · H-170, H-171 → SE-04 · H-175 → read at B-C (IN-39, landed; the reading is its `cite:`), its remainder unowned · H-176 → IN-27 (landed `6ae70998`) ·
H-180, H-181 → re-checked at IN-17 (landed `ac9724fc`; both stay absent) · H-182 → IN-32 (re-checked at IN-17) · H-186 → IN-30.

**Retired, never reused:**
- `31d` — drafted 2026-10-03 (`ED-IN-0284`, `ED-IN-0285`); retired unbuilt before anything built it (v8 §0.3).
- `31e` — the same.
- `32` — the same.
- `24h` P6 — superseded by IN-11 (landed `2a2ed152`): #453 R-3 cuts `repudiate`; its pricing, owed as a `deed:commitment.ended` cell, is `engine/season/hole_register.yaml` H-205.
- `24h` P7 — retired on IN-09's typed `comply` cell (`128299db`); J-10 closes with J-2 there [medium].
- `10` — U5/R-07; carved out to the telling workplan by v8, absorbed here as IN-16–IN-18 (§0.6).
- IN-51 — #453 R-5 (b) read as `inheritance` filled by CENSUS at `person.died`; retired unbuilt on 2026-10-14, superseded by IN-61 (RS-27: the heir is a title who claims the throne by his own act). The handle is not reused.
