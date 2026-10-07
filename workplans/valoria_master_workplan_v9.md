# Valoria — Master Workplan v9: the one plan for every lane — what is genuinely open, in build order

## Status: RATIFIED on merge (ED-1094, ED-IN-0286) — held back: §K
## Lane: IN (cross-cutting). It is the ONE active plan (`CLAUDE.md` §2) for all nine lanes — IN, SC, SE, MB, PC, FI, WR, GO, FA. **No carve-out:** the 2026-10-01 telling workplan is absorbed (§0.6).
## Reads in order: this file (how to read, milestones, start here, state index, crosswalk) → `_part2` (THE NINE, one section per row) → `_part3` (orchestration: dependency graph §A, the file-affinity batches §B with their membership rules and handoff cards, file-collision matrix, pre-flight) → `_part4` (IN I: the instruments, the modules specs, the telling tail) → `_part5` (IN II: cells, verbs, forcing, cast; §A answered; A-25; §J the Jordan queue) → `_part6` (SC, SE, FI) → `_part7` (MB, PC, WR, GO, FA) → `_part8` (standing content; §K the adoption ledger; the Layer-0/1 edits owed).
## Grade under `CLAUDE.md` §0.2: `paper` throughout. A plan, not an execution artifact. Every reading here names its command and the date it was read; the evidence is the thing cited, never this file.

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

No existing position number changes meaning. Every surviving v8 number (`31a`, `22`, `24g`, `19b`, `9`, `26`, `33`, `36`,
`2-ii`, …) is kept as the **ALIAS** of a v9 handle. **The v9 handle is lane-tagged, `<LANE>-nn`** (§3; §4 maps both ways,
plus the #453 and #457 handles). A position added after adoption continues its lane's run of handles; a bare number (from
`37`) is used only for a position with neither an alias nor a handle — none today. A handle's batch is `_part3` §B's; `B-A`…`B-Z` are file-affinity batches (§B.0's rules place a late position), not a count of phases. Retired numbers are never reused (§4,
last list). **None of these handles allocates a ledger id.** An id is allocated when the position is built.

⚠ **One collision, named so nobody resolves it by guessing.** In the 2026-09-28 plan's Phase-1 list, "item 11" was position
`25` (MB-GOLDEN, DONE). Position **`11`** is U6, the first R-01/R-02 corpus measurement, re-taken at B-G (as the control), B-I and B-M
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
- **Must NOT, in any batch:** edit `.designs/` or `.audit/`; cite a `.md` as the reason a behaviour is correct; build a
  guard whose subject is process (§0.1 pt 5); create a directory or standing document; author a cell, a Godot version, or
  a Jordan item's answer; interleave the cells commit (IN-08) with `9` (PC-01); build anything in `engine/mc_v18.py`;
  `git add` a file another lane is editing (use `isolation: worktree`); re-fetch from the GitHub API; write a count into
  `CURRENT.md`/`HANDOFF.md`.

### 0.6 The telling workplan — ABSORBED, not carved out

`workplans/2026-10-01-telling-workplan.md` (RATIFIED by Jordan, `ED-IN-0282`; T0–T6 built, PR #449 `fd321c81`) was v8's one
carve-out. Jordan's word that v9 *"supersedes everything"* ends it: adoption retires the file (`FORK:` row; its As-built
record stays at that ref and is not carried) and writes one superseding row on `ED-IN-0282` — *absorbed into v9; nothing
re-ruled*. What it still owed is scheduled under IN handles in `_part4`, its gate and trigger text carried unchanged: T7
(G9, declared intent) is IN-16; the owed measurement and the `absent` re-check of H-180/H-181/H-182 are IN-17; the gated
tail G1–G8 is IN-18. Its rulings stand as written: `tell` writes no stance and told valence enters regard at read (G1; AX-3),
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
generalized. **Its precondition is met** (M1 row 4, read above). **Its bar still has no instrument:** `harness/soak.py`
(#446) runs seasons and grades nothing; `corpus_run`'s `ARC ENDS` count prints `NOT-COMPUTABLE — closed by W23 + W26 + W30`
[v8's reading, 2026-10-01; not re-run here]. Candidate gates, none built: (i) SC-01 step 16 (`22`) — THE BAR for
proceedings (two seeded proceedings run end to end twice byte-identical, `causes[]` walking to the raising date);
(ii) `corpus_run`'s ARC ENDS becoming computable; (iii) a chronicle render, IN-37 (the `chronicle` witness channel dies at
SC-01 step 13). **v9 builds the instrument first:** IN-19 (#457 STORY-BAR — cross-person antecedent share and chain depth
per season over N seeds, forcing on/off), with IN-20 making `soak.py` grade. Path: IN-19 → SC-01 step 16 → IN-37 → IN-27
(#457 D6, the ending vocabulary: answered as the plan's recommendation, RS-21 item 3) (`_part3` §A(2)).

### M3 — GODOT VERTICAL SLICE

Last, unchanged in substance: GO-01 (`26`). **The Godot engine version is UNRESOLVED and nothing here asserts one**
(`_part5` §J, J-9). `godot/godot_conversion_strategy_v1.md` is PROPOSED and HELD (§K); GO-03 strikes its version string and
Key-runtime rows. `references/module_contracts.yaml`'s `engine_clock` row keeps `doc:` null until IN-42 (= GO-02).
`engine/autoload/engine_clock.py` is deleted (`28-iii`, PR #450); the temporal spine is `engine/season/loop/driver.py` +
`loop/calendar.py`, which that row describes, so `CLAUDE.md` §6's "starting with `engine_clock`" means the season calendar
(Layer 0: listed at IN-44, not edited here). `godot/skeleton/` is not a head start. Path: IN-42 → GO-03 and GO-04 (B-L, behind IN-42 only) → GO-01 (J-9) → (IN-05 → GO-05)
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
Green` on `main` once the branch merges. Then **B-B, B-C and
B-D1/D2/D3 in parallel sessions**, then B-G → B-H → B-E → {B-F ∥ B-I} → B-J → … the spine `_part3` §B names. Every batch runs
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
| IN-02 | `30` | IN | B | — | — | B-B | `_part4` |
| IN-03 | `31a` | IN/SC | BLK | IN-02 | — | B-L | `_part4` |
| IN-04 | `31b`; #457 SEAM-LADDER | IN/PC | BLK | IN-03, PC-02, PC-03, PC-04 | — | B-L | `_part4` |
| IN-05 | `31c`; SM-7 | IN/MB | BLK | IN-04, MB-01, MB-02, MB-05 | — | B-L | `_part4` |
| IN-06 | `33`; #457 D5; A-24's threadwork; H-47 | IN/WR/FI | B | design | — | B-C · B-S | `_part4` |
| IN-07 | `36` | IN/SE | B | design | — | B-C · B-T | `_part4` |
| IN-08 | cells commit; `12b` `12c` `12d`, H6–H11, `12`, `12e`, 6f; #457 CARRY-INTERIOR; #445 P-1 | IN | BLK | PC-01 | R-05, R-06, R-08 | B-G · B-H | `_part5` |
| IN-09 | `19b` | IN | B | after B-G | R-05 | B-I | `_part5` |
| IN-10 | #453 step 1 | IN/SC | B | after B-G | R-04, R-05 | B-I | `_part5` |
| IN-11 | #453 step 2 | IN/SE | B | after B-G | R-05, R-06 | B-I | `_part5` |
| IN-12 | #453 steps 5, 5a, 6, 7, 9, 10, 11, 13 | IN/SC/SE/MB | BLK | per step | R-04, R-05, R-09 | B-K · B-M · B-Q · B-R | `_part5` |
| IN-13 | #453 step 8 | IN/MB | BLK | IN-05 | R-07, R-05, R-01 | B-M | `_part5` |
| IN-14 | #457 BOUND-ATTENTION; H-92, H-10 | IN | B | — | — | B-B | `_part4` |
| IN-15 | AX-7 wiring | IN | BLK | IN-16, IN-18 | — | B-E | `_part4` |
| IN-16 | telling T7 (G9) | IN | B | — | — | B-E | `_part4` |
| IN-17 | telling measurement; H-180/181/182 re-check | IN | BLK | IN-16 | — | B-E | `_part4` |
| IN-18 | telling G1–G8 | IN | BLK | IN-17 | R-07 | B-E · B-I | `_part4` |
| IN-19 | #457 STORY-BAR | IN | B | — | — | B-C | `_part4` |
| IN-20 | #457 STORY-SOAK | IN | B | — | — | B-C | `_part4` |
| IN-21 | #457 FORCE-WEATHER; H-26 | IN/SE | BLK | IN-19 | — | B-F | `_part5` |
| IN-22 | #457 CARRY-SHORTFALL; H-160 limit 1; #445 P-2 | IN/SE | BLK | IN-15, IN-18 | — | B-E · B-F | `_part5` |
| IN-23 | #457 CARRY-STABILITY | IN | BLK | IN-19 | — | B-U | `_part5` |
| IN-24 | #457 BOUND-LOOPS; H-106, H-25 | IN | B | — | — | B-C | `_part4` |
| IN-25 | #457 BOUND-STAKES | IN | BLK | IN-18 | — | B-E | `_part5` |
| IN-26 | #457 BOUND-PAPER; H-156 (a)/(b); `Record.ttl` | IN/SC | BLK | SC-01, FI-01 | R-05 | B-Q | `_part5` |
| IN-27 | #457 END-VICTORY; H-176 (GD-1) | IN/FA | BLK | IN-37 | — | B-U | `_part5` |
| IN-28 | H-166 | IN/SE | BLK | IN-45 `work` | R-05 | B-K | `_part5` |
| IN-29 | H-110 | IN | B | — | R-03 | B-B | `_part4` |
| IN-30 | `24h` P5 remainder; H-186 | IN/FA/SE | BLK | IN-27 | — | B-U | `_part5` |
| IN-31 | H-100 | IN/SE | BLK | SC-03a | — | B-J · B-Q | `_part5` |
| IN-32 | H-182 ties | IN/FI | BLK | IN-06 | R-05 | B-S | `_part5` |
| IN-33 | H-58 `exchange` | IN | B | after B-G | R-05 | B-I | `_part5` |
| IN-34 | #457 FORCE-BODIES | IN/SE | BLK | SE-01, IN-21 | — | B-F | `_part5` |
| IN-35 | #457 FORCE-HAZARD; SEAM-CLOCK | IN/WR/SE | BLK | IN-06 | — | B-S | `_part5` |
| IN-36 | #457 FORCE-FOREIGN | IN/FA/MB | BLK | IN-13 | — | B-V | `_part5` |
| IN-37 | #457 STORY-READ | IN | BLK | IN-19, SC-01 step 16 | — | B-U | `_part5` |
| IN-38 | `13`-rest | IN | B | — | R-09, R-06 | B-V | `_part5` |
| IN-39 | pre-flight P-4, P-6; H-175 | IN | B | — | R-01, R-04 | B-C | `_part4` |
| IN-40 | H-101 | IN/FA/SE | BLK | IN-10 | R-04 | B-J | `_part5` |
| IN-41 | SM-9, SM-11 | IN | BLK | IN-02 | — | B-B | `_part4` |
| IN-42 | Gate-0: `engine_clock`'s `doc:`; ED-1051 | IN/GO | B | — | — | B-C | `_part4` |
| IN-43 | housekeeping: stale handoff rows, retired-plan cites, R-09's `u1_` selector, `domain_echo` rows | IN | B | — | R-01, R-09 | B-C | `_part4` |
| IN-44 | SM-10, SM-12; A-24's wording | IN | J | Layer 0/1: Jordan's files | — | — | `_part8` (table, not an entry) |
| IN-45 | `forge` `carry` `work` `migrate` | IN/SC/SE | BLK | IN-10, SC-03a, IN-22 | R-05 | B-K | `_part5` |
| IN-46 | = SM-6 | IN/PC | B | design | R-04 | B-C | `_part4` |
| IN-47 | #445 (character sheet) | IN/PC/WR | B | design | R-04 | B-C | `_part4` |
| IN-48 | H-108 (delegation half) | IN/FA/SE | BLK | IN-10, IN-11 | R-04 | B-J | `_part5` |
| IN-49 | H-163 limit 3 | SE/IN | BLK | IN-10 | R-04, R-05 | B-K | `_part5` |
| IN-50 | — | IN | BLK | IN-43 | R-01 | B-C | `_part4` |
| IN-51 | #453 R-5 (b) | IN/FA/SE | BLK | IN-12 | R-05 | B-R | `_part5` |
| SC-01 | `22` steps 11–16 | SC | BLK | IN-02, IN-03 | R-04, R-05, R-08, R-09, M2 | B-N | `_part6` |
| SC-02 | `22a` → `23` → `22b` | SC | BLK | SC-01 | — | B-P | `_part6` |
| SC-03a | #453 steps 2b, 3 | SC | BLK | IN-10, IN-11 | R-05 | B-J | `_part6` |
| SC-03b | #453 step 4; H-162 | SC | BLK | SC-01, SC-08, SC-03a | R-05, R-04 | B-O | `_part6` |
| SC-04 | `18` tails | SC | BLK | SC-03a, SC-01 | — | B-P | `_part6` |
| SC-05 | `2-ii`; SM-2, SM-15 | SC | ask-then | SM-15 | — | B-Z | `_part6` |
| SC-06 | SM-1 | SC | ask-then | SM-1 | — | B-Z | `_part6` |
| SC-07 | #445 P-4, V-4, V-5 | SC | BLK | SC-01 | — | B-N | `_part6` |
| SC-08 | — | SC | BLK | SC-01 | — | B-O | `_part6` |
| SE-01 | `24g`; H-51 | SE | BLK | IN-21 | R-07 | B-F | `_part6` |
| SE-02 | = IN-07 | — | — | — | — | B-C · B-T | `_part4` |
| SE-03 | ED-SE-0053 §A.6–A.8 | SE | BLK | IN-28 | — | B-K | `_part6` |
| SE-04 | #457 CAST-POPULACE; H-170, H-171 | SE | BLK | IN-07 | — | B-T | `_part6` |
| SE-05 | = IN-30 | — | — | — | — | B-U | `_part5` |
| MB-01 | ED-MB-0045 build | MB | B | — | — | B-D2 | `_part7` |
| MB-02 | ED-MB-0057 | MB | B | — | — | B-D2 | `_part7` |
| MB-03 | ED-MB-0078 | MB | BLK | IN-05 | — | B-L | `_part7` |
| MB-04 | A5; #445 U-3 | MB | B | — | — | B-D2 | `_part7` |
| MB-05 | A7 terrain; ED-MB-0074 | MB | B | — | — | B-D2 | `_part7` |
| MB-06 | ED-MB-0075 attack | MB | B | — | — | B-D2 | `_part7` |
| MB-07 | J-18 | MB | B | — | — | B-D2 | `_part7` |
| MB-08 | #445 U-1, U-2, U-6 | MB | LEAVE | named, unscheduled | — | B-Z | `_part7` |
| MB-09 | = IN-05 | — | — | — | — | B-L | `_part4` |
| PC-01 | `9`; ED-PC-0056 | PC | B | J-7 answered: build | — | B-D1 | `_part7` |
| PC-02 | ED-PC-0003; ED-IN-0187's held site | PC | B | — | — | B-D1 | `_part7` |
| PC-03 | ED-PC-0058 | PC | B | finding 1 | — | B-D1 | `_part7` |
| PC-04 | ED-PC-0016, 0049, 0050 | PC | B | — | — | B-D1 | `_part7` |
| PC-05 | ED-PC-0013 (1), (3) | PC | B | item 3, after a check | — | B-D1 · B-Z | `_part7` |
| PC-06 | #445 S-1, M-1/S-4, S-2/L-1, K-1/K-5, K-3; ED-PC-0001 | PC | B | S-1 | R-03; R-05 | B-E · B-L · B-S | `_part7` |
| PC-07 | J-20, J-21 | PC | B | J-20 (B) | — | B-D1 | `_part7` |
| PC-08 | Phase 4a/4b/5, WS-7; #445 M-2..M-6, K-4/V-3 | PC | LEAVE | named, unscheduled | — | B-Z | `_part7` |
| PC-09 | = IN-04 | — | — | — | — | B-L | `_part4` |
| FI-01 | `ED-FI-0009`; J-22 (A); #445 S-6 | FI | BLK | SC-01, SC-03b, IN-03 | R-05, R-09 | B-O | `_part6` |
| FI-02 | SM-3 | FI | BLK | FI-01 | — | B-O | `_part6` |
| FI-03 | ED-FI-0002 | FI | BLK | IN-06 | — | B-S | `_part6` |
| FI-04 | ED-914 residual; PP-719 | FI | B | a ledger row, no code | — | B-C | `_part6` |
| FI-05 | = IN-32 | — | — | — | — | B-S | `_part5` |
| WR-01 | `27` remainder: the R-14 term | WR | B | in-module | — | B-D3 · B-S | `_part7` |
| WR-02 | `27` remainder: own-configuration Mending | WR | BLK | WR-01 | — | B-D3 | `_part7` |
| WR-03 | `27` remainder: Mending feedback, one pricing owner | WR | BLK | WR-02 | — | B-D3 | `_part7` |
| WR-04 | ED-WR-0010 c.3 doc half | WR | B | tiny | — | B-C | `_part7` |
| WR-05 | = IN-35 | — | — | — | — | B-S | `_part5` |
| GO-01 | `26`; D2 tenth attribute | GO | J | J-9 | — | B-Z | `_part7` |
| GO-02 | = IN-42 | — | — | — | — | B-C | `_part4` |
| GO-03 | strategy-doc record edit | GO | B | a GO-lane document edit | — | B-C | `_part7` |
| GO-04 | ED-IN-0017 seam audit | GO | BLK | GO-02 | — | B-L | `_part7` |
| GO-05 | SM-13; ED-PC-0013 (1) | GO | BLK | IN-05, GO-01 | — | B-Z | `_part7` |
| GO-06 | `valoria-game` parity | GO | BLK | `valoria-game` checkout | — | B-Z | `_part7` |
| FA-01 | #445 P-3; FORCE-FOREIGN's cast | FA | B | mechanism | R-04 | B-J · B-V | `_part7` |
| FA-02 | = IN-30 | — | — | — | — | B-U | `_part5` |
| FA-03 | #453 §10.2 faction map | FA | LEAVE | reference | — | B-Z | `_part7` |

## 4. CROSSWALK — v8 and the proposals ↔ v9

**Batches B-A … B-T, B-U, B-V, B-Z** (members, shared files, entry gates, exit instruments, re-records, lanes, handoff cards): `_part3` §B, the only copy.

| v8 position · telling · §SM | v9 |
|---|---|
| `B0-CI` · `30` · `31a` · `31b` · `31c` · `33` · `36` | built (`7b619328`; not a position) · IN-02 · IN-03 · IN-04 (= PC-09) · IN-05 (= MB-09) · IN-06 · IN-07 (= SE-02) |
| cells commit, `12b`/`12c`/`12d`, H6–H11, `12`, `12e`, Phase 6f | IN-08 |
| `19b` · `13`-rest · pre-flight P-4, P-6 | IN-09 · IN-38 · IN-39 |
| `22` · `22a` → `23` → `22b` · `2-ii` | SC-01 · SC-02 · SC-05 |
| `24g` · `24h` P5 · `24` (umbrella) | SE-01 · IN-30 (= SE-05, FA-02) · not carried — its letters are the rows |
| `9` · `26` · `27` remainder · `ED-FI-0009` | PC-01 · GO-01 · WR-01, WR-02, WR-03 · FI-01 |
| `11` | no handle: re-taken at B-G (control), B-I and B-M (E15), after IN-39's P-4 |
| SM-1 · SM-2, SM-15 · SM-3 · SM-7 · SM-9, SM-11 · SM-10, SM-12 · SM-13 · SM-5, SM-6 | SC-06 · SC-05 · FI-02 · IN-05 · IN-41 · IN-44 · GO-05 · SM-5 confirmed (RS-6), SM-6 = IN-46 |
| telling T7 · its measurement + H-180/181/182 re-check · G1–G8 | IN-16 · IN-17 · IN-18 |

| #453 — `proposals/2026-10-03-verb-coverage-and-gap-fill.md` | v9 |
|---|---|
| §10.4 step 1 · step 2 · steps 2b + 3 · step 4 · step 8 | IN-10 · IN-11 · SC-03a · SC-03b · IN-13 |
| steps 5, 5a, 6, 7, 9, 10, 11, 13 | IN-12, one sub-entry per step |
| step 2a (`known_persons` widening) | IN-18 (B-E): its EXIT carries the step-2a re-pin |
| "later" (R-5, `inheritance`) | IN-51 (B-R; RS-21 item 9) |
| R-1(b) R-3(b) R-4(b) R-8(b) R-9(a) · §13.9 kill/wound | adopted at the step each names (§K (a)) · adopted: `kill` and `wound` are not verbs (RS-5, Jordan's own words), only `challenge` → `accept` is added (`_part5` IN-08) |

| #457 — `proposals/2026-10-04-forcing-churn-and-the-story-bar.md` | v9 |
|---|---|
| STORY-BAR · STORY-SOAK · STORY-READ | IN-19 · IN-20 · IN-37 |
| FORCE-WEATHER · FORCE-BODIES · FORCE-HAZARD (+ SEAM-CLOCK) · FORCE-FOREIGN | IN-21 · IN-34 · IN-35 · IN-36 (+ FA-01's cast) |
| CARRY-INTERIOR · CARRY-SHORTFALL · CARRY-STABILITY | merged into IN-08 · IN-22 · IN-23 |
| BOUND-LOOPS · BOUND-STAKES · BOUND-ATTENTION · BOUND-PAPER | IN-24 · IN-25 · IN-14 · IN-26 |
| CAST-POPULACE · CAST-DISPOSITION | SE-04 · merged into IN-08 + IN-12 step 9 (J-13 (iii) the adopted interim; `tell` stays uncelled, G-1) |
| SEAM-LADDER · END-VICTORY | merged into IN-04 · IN-27 |
| §7 D1 · D2 · D3 · D4 · D5 · D6 | IN-35 · IN-34 · answered: no dated pins (T-c) · IN-36, FA-01 · A-24 → IN-06 · IN-27 (D2, D4, D6 answered as the plan's recommendation, RS-21) |

**#445** (`proposals/2026-09-30-character-and-play-surface/`): S-1, M-1/S-4, S-2/L-1, K-1/K-5, K-3 → PC-06 · U-3 → MB-04
· U-1/U-2/U-6 → MB-08 · P-1 → IN-08 · P-2 → IN-22 · P-3 → FA-01 · P-4, V-4, V-5 → SC-07 · S-6 → FI-01 · V-1 → J-2
(answered) · K-2 only with its first reader · M-2..M-6, K-4/V-3 → PC-08.

**Hole-register rows a position now owns:** H-25, H-106 → IN-24 · H-26 → IN-21 · H-44 → IN-09 · H-47 → IN-06 · H-48 →
IN-18 (G6) · H-51 → SE-01 · H-58 → IN-33 · H-59 → IN-12 (`forgive`) · H-92, H-10 → IN-14 · H-100 → IN-31 · H-101 → IN-40 ·
H-110 → IN-29 · H-160 → IN-22 · H-162 → SC-03b · H-166 → IN-28 · H-170, H-171 → SE-04 · H-175 → IN-39 · H-176 → IN-27 ·
H-180, H-181 → IN-17 · H-182 → IN-17, IN-32 · H-186 → IN-30.

**Retired, never reused:**
- `31d` — drafted 2026-10-03 (`ED-IN-0284`, `ED-IN-0285`); retired unbuilt before anything built it (v8 §0.3).
- `31e` — the same.
- `32` — the same.
- `24h` P6 — superseded by IN-11: #453 R-3 cuts `repudiate`; its pricing is a `deed:` cell (J-1).
- `24h` P7 — retired on IN-09's typed `comply` cell; J-10 closes with J-2 there [medium].
- `10` — U5/R-07; carved out to the telling workplan by v8, absorbed here as IN-16–IN-18 (§0.6).
