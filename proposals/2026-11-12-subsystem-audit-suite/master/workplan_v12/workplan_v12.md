# Valoria master workplan v12 — part 1, the head: what v12 is, how it is run, the rules it carries, the ids (lane IN)

## Status: PROPOSED, ratified on merge (ED-1094, `ED-IN-<the adoption id>`: one id allocated by the adopting commit, §11 step 3; `ED-IN-0361` at this read of `references/id_reservations.yaml` `[ASSUMPTION: no other session allocates in IN before adoption — basis: `lane_ids.lanes.IN.next_free` reads 361 at `bba489b`]`; ⚠ the assumption failed: `ED-IN-0361` went to Layer 1 node `L1-A115` (A-115), so the adoption id is `ED-IN-0362` at the current read, §12). Drafted under `proposals/2026-11-12-subsystem-audit-suite/master/workplan_v12/`; until Jordan adopts it, it is an unratified plan: input to `methodology-execute`'s 0.1 stop, presented and never adopted silently (the skill, §BATCHES, source 4; `STAGES.md` step 6 rule 7). Resolves nothing at runtime (CLAUDE.md §0.05).
## Lane: IN (cross-cutting), covering all nine lanes — IN, SC, SE, MB, PC, FI, WR, GO, FA. The successor of workplan v11 (`workplans/valoria_master_workplan_v11.md` + `_part2` … `_part17`), retired in the commit that adopts this plan (§11); not a second plan in force.
## Grade under CLAUDE.md §0.2: `paper`. A plan, not an execution artifact. It moves no row of THE NINE: a conjunct's `reading:` record is written by the last `Item:` commit of the batch that reads it (`IS-A-12`), and a row's `status:` is edited only by B99, the one re-take (A-114; §6).
## Written against: this part, HEAD `bba489b` (branch `ccr-62958c70-0kjhsw`, 2026-11-12, a shallow clone: `.git/shallow` is present); each body part names its own tree in its own head. Author: lane H1 of `master/workplan_v12/V12_STRUCTURE_part3.md` §7.1, one round.
## Parts, in reading order (execution order): this head (part 1; `workplan_v12_cont.md` continues it if present) → part 2, the tables (lane H2: the batch table, the serial-edge table, the file census, the hash-mover table, the settings-at-control table, the Layer 1 status, the tests and tools tables, the held table) → parts 3 to 43, the batches, each with its `_cont` files → part 44, B98 and B99 (lane A44, written after part 2's settings table exists). §14 maps every batch handle to its file.

**Short forms.** A path with no directory prefix is under `proposals/2026-11-12-subsystem-audit-suite/` (the suite); a path under `engine/`, `modules/`, `tools/`, `references/`, `registers/`, `tests/`, `architecture/`, `workplans/` is the repository's. `the structure` is `master/workplan_v12/V12_STRUCTURE.md` with `_part2`, `_part3` and `_part4`; `D-nn` is a decision of its §1; `E-nn` is an erratum of `V12_STRUCTURE_part4.md` (which wins where the structure differs). `A-nn` is a ruling in `unified/DECISIONS_ANSWERED.md`. `the skill` is `.claude/skills/methodology-execute/SKILL.md`; `the intake` is `master/eval/V12_INTAKE.md`; `the evaluation` is `master/V11_EVALUATION.md` and its parts, with `master/GAP_REGISTER_EVALUATION.md` and its parts; `IS-A` is `master/instructions/IS_A_NINE.md` and `_part2`; `U3` is `unified/U3_DEPENDENCY_ORDER.md`; `CIP` is `master/CODEBASE_IMPROVEMENT_PROPOSAL.md` and `_part2`; `MBA` is `master/mb_abstraction/MBA_DESIGN_part3.md`; `PCR` is `master/pc_round/PC_ROUND_SPEC_part2.md`; `the lexicon` is `unified/MB_LEXICON.md` and its parts; `04` is `architecture/meta/04_CODE_ARCHITECTURE.md`. Every suite file the adopting commit deletes (§11 step 6) is cited after adoption through its exact-file `FORK:` row.

**This part's sections.** §0 what v12 is · §1 how it is run · §2 the plan's rule for finished positions · §3 the head rules · §4 words · §5 time efficiency and the critical path · §6 two seasons, the settings batch, the re-take · §7 parallel sessions and the coordinator · §8 the schedule and the milestones · §9 defaults in force · §10 what part 2 holds · §11 adoption, the retirement of v11, and what is held back · §12 ids and row blocks · §13 definitions coined here · §14 the index.

---

## 0. What v12 is

**Jordan's direction** (2026-11-12, `STAGES.md` step 6): *"the instruction suite and the workplan items need to be folded in together. priority goes to this session new content in case of any conflicts. new workplan v12 will carry an entirely new plan in batches based upon all findings and instructions from this session"*; *"everything that fable recommends we build is the basis of new workplan alongside everything from workplan v11 folded in carefully"*; *"v11 items survive if nothing supersedes them"*.

**The basis.** v12 is an entirely new plan, not v11 amended. Its spine is everything this session recommends be built: every proposal a closure table (`unified/U5_FINDINGS_CLOSURE_U5a.md` to `_U5d.md`) dispositions RESOLVED-BY, the instruction suite (`master/instructions/IS_*`), the codebase items `CI-01` to `CI-11` (CIP), the mass-battle abstraction `MBA-01` to `MBA-09` (MBA), the fight's round `PCR-1` to `PCR-4` (PCR) and the lexicon's renames `L1` and `L2`, read with Jordan's rulings A-1 to A-114. A v11 position or a hole-register row enters only where the evaluation settled it STILL-NEEDED or MISSING-DEP: the intake's 273 entries, of which 22 are this head's rules (§3), 54 are held (no work until a trigger fires; part 2's held table) and the rest are items in the batches. **On any conflict the session's content wins**: a v11 item that a session item supersedes is retired, with the superseding item cited in the evaluation, and is not carried in any form; every v11 position and every gap-register row has exactly one recorded disposition there, so nothing is dropped silently.

**Structured to meet the nine** (R-01 to R-09 in `engine/season/requirements.yaml`, read with `python -m engine.season.harness.register --requirements`): dependencies fix the order of batches; the requirements fix the grouping and the milestones (§8). Each batch block names the conjuncts its close reads and the reading expected (`REQUIREMENT:`), or says why it serves none. A requirement is met when its behaviour executes and something ran it, never because a batch landed (CLAUDE.md §0.2; rule V4).

**Run by `methodology-execute`, not made by it** (Jordan: *"methodology-execute to be specified in plan, not used to make plan"*). The authors were Fable (the structure), Opus (the body parts and this head) and Sonnet (the checks); no stage before adoption invoked the skill.

**Where the plan's decisions are.** Every inconsistency between U3, the intake and the instruction suite was settled by CLAUDE.md §0's five-step ladder in the structure §1 (D-01 to D-22) and the errata E-1 to E-15; nothing survived it for Jordan, so no `V12_FOR_JORDAN.md` was written (the structure §1, last paragraph). This head restates those decisions as rules where they bind every batch (§3 table B); it decides nothing of its own beyond what it marks `[ASSUMPTION]`.

---

## 1. How v12 is run

**One invocation per batch:**

```
/methodology-execute Batch <handle>
```

`<handle>` is the batch's full handle as its block heading writes it (`B21-fa-governance`, `B12a-world-motion-and-ground`). A driver (`tools/methodology_drive.py`) re-invokes as `approved: /methodology-execute Batch <handle>` with the `[next: <handle>]` the previous status line printed (the skill, §THE STATUS LINE). The skill derives nothing the plan states; v12 states it in the forms the skill recognises (the skill, §BATCHES, "Where the batches live", source 2):

| form | as v12 writes it | the skill reads it as |
|---|---|---|
| a batch | one block, headed `## Batch <handle> · lane <LANE> · wave <Wn> · step <Sn> · HASH <EQUAL \| MOVER, one re-pin>`, holding the batch's lines (the structure §5.2), its position table and its items | a batch table or heading; ONE close (RULED 2026-11-06) |
| the position table | `\| pos \| item \| source \| state \| hash \| gates on \|`, one row per item in landing order; its `pos` column is the item handle `<batch number>.<two digits>` (`B21.09`) | the `Batch` column of a position table |
| the boundary row | `\| STOP. Batch <handle> closes here \|`, after the batch's last item | building stops there: BATCH-CLOSE, the boundary, the status line |
| a gate that names a batch | `GATE: Batch <handle>`, one line per batch it waits on; rewritten `GATE: Batch <handle> @<closing sha>` at that batch's expunge (§2) | met iff that batch's close has landed and its closing SHA is an ancestor of `HEAD` (BATCH OPEN item 3) |
| a batch with nothing to wait on | `GATE: none (record only); closes on the boundary row` (E-6; B00 alone) | buildable now (rule P2) |
| the content-owner entry | the item: `SOURCE`, `ADVANCES`, `INSTRUCTION`, `WHERE`, `TESTS`, `FALSIFIER and CONTROL`, `GATE`, `HASH MOVERS`, `DEPENDS ON`, `GLOSSARY`, `NAMES`, `IDS`, `COST and TIER`, `LANDS IT` (the structure §5.3) | INSTRUCTION / WHERE / FALSIFIER / GATE, read in full before dispatch (the skill, 0.2) |
| the context set | `C(<handle>):` in the block | `C(k)`, the reading list BATCH OPEN loads |
| serial edges and the file census | the block's `SERIAL EDGES:` and `PARALLEL:` lines, and part 2's serial-edge table and file census | the gates and edit sets; derive nothing the plan states |
| the in-flight row | the block's `IN-FLIGHT ROW:` line names `registers/handoffs/HANDOFF_<LANE>.md`, Open table; a two-lane batch (B12a, B12b, B12c: SE and WR) keeps its row in `HANDOFF_SE.md`, and `HANDOFF_WR.md` carries one pointer row `Batch <handle> — IN FLIGHT (row in HANDOFF_SE.md)`, deleted at the same expunge (D-21) | the in-flight row, one per lane |
| cost and tier | each item's `COST and TIER:` line; the block's `COST:` line | the tier per dispatch (CLAUDE.md §10) |

**Item states** (the `state` column; the structure §5.3 with E-5, E-7, E-10): `BUILD` · `DESIGN-FIRST` (a design written and merged before its build, D-18) · `CONTENT` (authored values, drafted for Jordan's correction, D-19) · `READING` (a reading quoted at the close: no code, no commit of its own; its text is copied byte for byte into the batch's `## Readings` block, after the last item and before `.99`, E-10) · `POINTER` (no work here; a body of three to eight lines naming what the pointed item does, its files and symbols and its gate, E-5) · `GIT` (exact `git` commands, the base SHA and the expected result; its gate is the covering tests and the hash reading; never a force-push without the permission the plan cites, A-93 for B01; E-7) · `BLOCKED (<owner>: <what is missing>)` · `HELD (<trigger>)`.

**Lines an item or a batch may carry beyond the structure's form:**
- **`.99`, the re-pin and close-readings position** (E-1). Every batch ends with `B<nn>.99 — re-pin and close readings`, the last position before the boundary row: one code-and-test commit that re-records, once, every realm and corpus pin any item of the batch moved, writes the batch's readings and the conjuncts' `reading:` records, and, for a hash-EQUAL batch, records the EQUAL reading and re-pins nothing. A drafting item comes before it. A pin that only one item moves (a test-local golden of that item's own new test file) stays in that item's commit; any pin two items move goes to `.99`.
- **`EXPECTED RED UNTIL <handle>`** (E-1, E-9). A test red between its item and the item that turns it green (often `.99`) is listed on the item that leaves it red, with the handle that ends it; it stays under `[skip ci]`. The batch close is green. A batch with any behaviour or encoding mover also carries one block-level line, `EXPECTED RED UNTIL B<nn>.99`, naming the realm and corpus pin files its movers turn red (`_realm_goldens.py`, `test_go07_canonical_digest.py` and the pin files its items name); an item's own line stays where it has one (E-1; repair lane R1).
- **`STOPS IF <tree condition>`** (the pilots' rule, `V12_STRUCTURE_part4.md` "What the pilots found"). An item whose source assumes a symbol or behaviour the tree may lack states the condition; at its turn the producer checks it and, if it holds, the item stops and is reported (`STOPPED`), never guessed around.
- **`UNDECIDED:`** in a batch block lists each choice the author could not read off its source, with the two readings and the one the text takes (the one that changes less, the structure §5.1). The batch's 0.1 stop presents them.
- **`DIALS AT CONTROL:`** in a batch block lists each setting the batch ships at its control value, who sets it and its target reading (D-22; §6).

**Until adoption.** Under `proposals/`, v12 is an unratified plan: an invocation STOPS at 0.1 and presents it. The run starts only after Jordan adopts it (§11). After adoption, rule P16 (3) (§3) reads a batch named by its handle as approved by its own block; that reading is a plan-stated difference from the skill's 0.1 stop and is stated at the first 0.1 stop, not adopted silently (the skill, §BATCHES source 2).

---

## 2. The plan's own rule for finished positions

The skill (BATCH BOUNDARY item 1) removes a finished batch "by the plan's own rule for finished positions, edges and census rows". v12's rule (the structure §7.1 item 3):

1. **At a batch's expunge, in one commit:** its block (items, position table, `## Readings`, boundary row) is deleted from its part; every remaining `GATE: Batch <handle>` naming it, in any part, is rewritten `GATE: Batch <handle> @<closing sha>`; its rows leave part 2's batch table, serial-edge table and id-block table (§12), and any census row that names no other batch; its est. cell has by then been replaced by the measured wall time, which lives in the close's commit body, not in a row. No "done" row, count or narrative is added (CLAUDE.md §1; rule P3b).
2. **A part left with no batch** is deleted in that same commit with an exact-file `FORK:` row in `references/restructure_ledger.md`, and §14 loses its line.
3. **A position only part-finished stays**, narrowed to its receipt's `NOT DONE`.
4. **Before deleting**, grep for what still points at the batch (the skill's pre-deletion check): every remaining block's `C(...)`, `DEPENDS ON` and `SERIAL EDGES` lines and the code and registries (`git grep -n 'workplan_v12'`; `engine/season/requirements.yaml` cites plan sections). A position a remaining batch still reads stays, narrowed, until nothing reads it.
5. **Ids a batch did not use** are named in its expunge commit body and are never re-used (§12).

---

## 3. The head rules

### 3.A Carried from v11, as the evaluation settled them

These are the intake's 22 head rules (`master/eval/V12_INTAKE.md:77-100`: P1 to P12, P14 to P16, V1 to V4 and three risks of v11's `-00` §6), each restated as `master/eval/E1.md:28-61` dispositioned it and as the settlement ledger (`master/V11_EVALUATION_part2.md` §1) changed it. P3a and P13 are SUPERSEDED and are not rules of v12: a card with several closes is several batches (P3a; the skill, RULED 2026-11-06), and the verb-cluster serialisation is replaced by one open batch per lane, the hot-file rule (§7) and part 2's serial-edge table and file census (P13; `E1.md:41`; D-02). Where v11's text names a v11 artifact, the v12 equivalent is named in brackets; nothing else is changed.

| rule | as v12 carries it | settled by |
|---|---|---|
| **P1** | The plan has one status column: the `state` column of each batch's position table; every row cites its evidence. If a row and its instrument disagree, the instrument wins and the plan is wrong. | `E1.md:28` |
| **P2** | A gate that names nothing to wait on (`GATE: none`, E-6) is buildable today. | `E1.md:29` |
| **P3b** | Finished positions leave the plan; the commit is their record. A closed batch's rows are deleted in one net-deleting commit (§2) and the run stops for a cleared window before the next batch opens. The stop is between batches, never inside one. | `E1.md:31` |
| **P4** | No position handle changes meaning; a retired handle is never re-used; a handle allocates no ledger id (an id is allocated when an item is built, from its batch's block, §12). v11's handles (`CR-nn`, `CP-Tnn-nn`, `H-nnn`) keep their meaning inside v12's items. | `E1.md:32` |
| **P5** | One item is one commit. The phases are the skill's: per item, Phase 0 (BUILD, integrate, commit with the `Item: <handle>` trailer); per batch, BATCH-CLOSE (`methodology-close`'s Phases 1 to 3, with `/code-review` and `/simplify` at the close, RULED 2026-10-06, and the accretion pass between Phases 2 and 3), then the BATCH BOUNDARY. `[ASSUMPTION carried from E1: P5's phase names match the skill's — basis: the skill read in full for this head, §PHASE 0, §BATCH-CLOSE, §BATCH BOUNDARY]` | `E1.md:33` |
| **P6** | The forward sweep (inside BATCH-CLOSE) checks instruments, the hole register, call sites, figures made stale, and goldens; it produces edits plus at most one paragraph in the commit message, never a document or a directory. Every close also records the requirement readings (`IS-A-12`; the structure §5.12). | `E1.md:34` |
| **P7** | Mid-batch, run only the file covering the edit; the full suite runs once per batch, at its close, never to re-confirm a green already held. Every validator, suite and golden-modes check runs once, at the batch close, and no earlier item runs them (Jordan, 2026-11-02: *"Ensure all validators etc only run at the very end of a batch"*). Every commit before the batch's last `Item:` push carries `[skip ci]`. CI runs twice per batch (the skill's RULED cadence of 2026-10-13); where parallel sessions merge several batches in one step, §7.9 states the difference and does not choose. | `E1.md:35` |
| **P8** | **Stopping rule.** A falsifier that fails means `git revert` of that item's commits (the commit carries a `Falsified: <handle>` trailer, the skill's form); never `--no-verify`, never skip, xfail or quarantine a test; never widen the item to make the falsifier pass; one hole-register row only if the gap was measured; one ledger row only if a human decision is needed after the five-step ladder. | `E1.md:36` |
| **P9** | **Restoration rule** (RULED 2026-10-13: *"Relax exit rules."*). A verb item is BUILT when it is wired and proven by a falsifier on a hand-built world (the cause controlled, a mutation red); its executed count in the realm is not required. This relaxes an item's exit, not a requirement's: R-04's and R-05's conjuncts still read computed play, and `IS-A-08`'s `BUILT OUT` line is read at the close of every batch that adds, splits or re-draws a verb row (a verb not built out at that close fails the batch gate, the structure §3). | `E1.md:37` |
| **P10** | **Test horizon** (Jordan, 2026-11-02: *"aperture 2 0 should be sufficient to see if one season affects another season"*; 2026-11-07; A-114: *"ideally no? that would take forever"*, amended *"maybe at the very end of the plan?"*). A probe runs season by season and ends at the first season in which a verb errors. **No probe, item gate or batch close runs past two seasons** (`aperture 2 0`, or `aperture 2 s` for seeds s): a gate copied from a source at three or four seasons is written at two, with the source's horizon noted (D-17; the structure §5.8). **The single exception is the longer re-take of THE NINE, run once as the plan's very last item (B99, after M5 and B98).** A reading from seeds 1 and 2 is taken only where the item or batch declares a hash mover (P14; E-2). v11's strife allowance (Jordan, ED-IN-0317: four seasons when testing strife) is a permission of his, not a requirement: no v12 gate uses it, and this plan does not withdraw it. | settlement ledger `E1:38` (A-114) |
| **P11** | **Must not**, in any batch: edit `.designs/` or `.audit/`; cite a `.md` as the reason a behaviour is correct; build a guard whose subject is process (CLAUDE.md §0.1 pt 5); create a directory or standing document; author a cell, an engine version, or an answer to a Jordan item that no source, taken decision or recorded ruling gives (authored values are drafted for his correction, D-19); build in `engine/mc_v18.py`; `git add` a file another lane is editing (use `isolation: worktree`); re-fetch from the GitHub API; write a count into `CURRENT.md` or `HANDOFF.md`; write a `.md` under `systems/`. | `E1.md:39` |
| **P12** | The telling workplan's rulings stand: `tell` writes no stance, and told valence enters regard when it is read (G1; AX-3). A regime's pressure (A-83) enters through regard's stance term, read person-side. | `E1.md:40` |
| **P14** | Every item and batch names its hash movers. A mover's before-reading is the previous item's recorded after-reading (`reading @<sha>`, V1), not a fresh run, and a known-red list is quoted from the previous close, not re-derived. A re-pin states plainly that a golden was re-recorded, and is made in the batch's `.99` commit (P15). | `E1.md:42` |
| **P15** | **Pins are re-recorded once per batch, after the last item is built** (Jordan, 2026-11-07), in the batch's `.99` commit (E-1). An item reports its after-readings in its commit body (for a mover: the seed-0 hash and its covering test file, E-2) and runs only its own test file and the files that read what it touched; it does not re-record a shared seeded golden, a count or set pin, or a derived artifact a byte-check compares (`engine/season/runs/results.json`). A pin only that item can move (its own new test file's numbers) is made in the item. `.99` re-records every shared pin the batch moved, each old → new in its body, and says plainly that goldens were re-recorded. Every source text that says its own commit "re-pins" or "re-records" is read as this rule. | `E1.md:43` |
| **P16** | **Build economy** (Jordan, 2026-11-08: *"I am concerned about the excessive build times that comes with running too many pins, tests and seasons."*). **(1) Horizon:** P10, with the single end-of-plan exception (A-114). **(2) Pins carry forward:** a batch takes one fresh base reading, at entry (V1); an item's recorded after-reading is the next related item's before-reading; a fresh reading is taken only where `git diff <sha>..HEAD` reaches what the instrument reads. **(3) One continuous run:** an invocation that names a batch by its handle is approved by that block (ratified on merge, ED-1094), so from the first item's BUILD to the end of BATCH-CLOSE's Phase 3 the run does not pause to ask; it halts only on a `STOPPED` condition of the skill or an item's `STOPS IF` or P8 revert `[ASSUMPTION carried from v11; medium; Jordan to correct; revert: 0.1 presents a named batch for approval as before — stated at the first 0.1 stop, §1]`. **(4) The full suites run once, as the last act of building:** after the `.99` commit and before Phase 1, over what `python tools/tests_for_diff.py --base <batch-start-sha>` and the batch's close name; Phases 1 to 3 and the accretion pass run no second full suite; each fix they apply runs only its covering file. | settlement ledger `E1:44` (A-114) |
| **V1** | **Re-base at entry.** The first step of every batch re-derives each site by symbol (line numbers drift; this plan cites by symbol, §3.B), takes the batch's base reading from the last recorded `reading @<sha>` (the previous close's, or the previous item's after-reading) and re-takes it only where `git diff <sha>..HEAD` reaches what the instrument reads, at the reading's own season count (the skill, Baselines, RULED 2026-10-13), and compares it with the figure the item's source cites. A premise that moved narrows the item or retires it with a one-line note in the commit; it is not built from stale text. The same step restates the item's N-line, `<object> — cut it and the gameplay experience is worse, because <what the game can no longer do>`; an item whose loss survives the cut is cut with a one-line note, not built (`.claude/skills/ners/SKILL.md` §2, §3). | `E1.md:45`; v11 risk 2 (`E1.md:57`) |
| **V2** | **A reading is a harness reader, never a guard.** Failure classes are tracked by readers in `engine/season/harness/` whose output is quoted in the batch's commit; no test asserts a refusal count or that a verb executed in the realm (P9). | `E1.md:46` |
| **V3** | **Asks are answered by the ladder first** (CLAUDE.md §0). What survives is a short list of questions; the rest are answered, closed, or taken with a stated revert (§9). A taken answer is `[ASSUMPTION; medium; Jordan to correct]` and reverts alone. | `E1.md:47` |
| **V4** | **The plan states what it cannot do.** No row of THE NINE reads `met` because a batch landed: each batch writes its conjuncts' `reading:` records (`IS-A-12`); only B99 may edit a row's `status:` (A-114). | `E1.md:48` |
| **risk 4 → defaults in force** | Nothing is a question to Jordan that the ladder answers (`needs_jordan` is not a parking space). The defaults in force, with A-15 replacing v11's `age_step` and `illness_rate` deferral, are §9. | `E1.md:59` |
| **risk 6** | **Content is not the plan's to author** (P11). Equipment, tradition, troop seeds, the cast's attribute values and skill scores, per-territory weather values, CL-THRUST's ladders, the strife deck's rows and every value marked `[ASSUMPTION]` or `status: seed` are Jordan's; v12 drafts them for his correction (BA1 for the cast, `IS-A-11`; D-19 elsewhere) and lists each in its batch's PR body. Until they exist, the range those systems can reach is unmeasured, not zero. | `E1.md:61` |

### 3.B The rules this plan adds

Each binds every batch. Source in the right column; nothing here is decided by this head.

| rule | statement | source |
|---|---|---|
| one item, one commit | An item lands as one `Item: <handle>` commit, `[skip ci]` unless it is the batch's last `Item:` push. Several edits of one source become one item only where they share files and gate (the grouping recorded in `UNDECIDED`); otherwise one item per edit. | the structure §5.3; E-13 |
| encoding movers | An item that adds, removes or renames a field or a class of a carrier that `World.content_hash()` encodes (`state/world.py::_object_head`, `_encode_into` put the class name, field count and field names into the hash) is `HASH MOVER(encoding)`, co-batched with the batch's one re-pin, and its control is tallies-equal, never hash-equal. A method or a class `World.content_hash()` never reaches is not one (B34's `Scene.cost`, A25's finding). | D-04; E-1 |
| two seasons | No gate runs past two seasons before B99 (P10). | D-17; A-114 |
| `settled:` governs | Of an intake entry's `settled:` text, the heading it sits under and its `lane's target`, the first governs. The heading decides which batch an entry joins; the batch table decides the order of batches; an entry whose dependency lands in a later batch joins the later batch, noted in both. | D-14; E-8 |
| design first | A design item (`DESIGN-FIRST`, `opus` with a `ners` critic) precedes its build in the same batch, or lands where its source says; its build gates on it. A build whose design is unmerged at its batch's open is `HELD`. What the design cannot settle by the ladder ends the run `STOPPED` for Jordan. The design items of a batch are listed first in its position table and land when the batch opens (B10's `B10.51`–`.53`, B38's `B38.51`, `.52`). A build may ship its machinery with the design-dependent term absent (a setting at control or an empty roster), with a `DESIGN-FIRST` follow-up in the dependent batch and the setting under `DIALS AT CONTROL`. | D-18; E-14; H2 notes (A13, A41) |
| authored values | Drafted early, landed at their batch, ratified at that batch's merge (ED-1094): values marked `[ASSUMPTION]` or `status: seed`, each listed in the batch's PR body for Jordan's correction. | D-19 |
| settings at control | A setting an item ships at its control value is set either by an item of its own batch or by B98, one item per setting against its source's target reading; one with no stated target is `BLOCKED (design: no target reading)` in B98. | D-22; §6 |
| registry order | An addition to `engine/season/rosters.yaml` or `engine/season/verb_table.yaml` goes at the end of its family's block (so two batches' appends merge without a conflict inside a block). | CIP part 2 §5 note 1 |
| cite by symbol | Items cite code by `path::symbol`, never by line; a line number into a file edited at or before B03a is dropped and the symbol kept. | CIP part 2 §5 note 2; the structure §5.4 |
| a test the source does not name | An item may name it (`test_…` in `engine/season/tests/…py`) with `[ASSUMPTION: test name; the item creates it]`; the item's first step creates it. | E-3 |
| per-item and per-batch readings | Per item: the covering test files and, for a mover, the seed-0 hash. At `.99`: seeds 0 to 2, the batch's declared readings and the one full-suite run. | E-2 |
| the hash reading | One command, written once here and as each block's `HASH READING:` line, under its `GATE:` lines; an item gate that reads "the realm hash" cites it as `` (`HASH READING`) ``: `PYTHONHASHSEED=0 python -c "import sys; from engine.season.boot.realm import build_realm; from engine.season.harness.populated import run; s, k = int(sys.argv[1]), int(sys.argv[2]); w = build_realm(s); run(k, s, w=w); print(w.content_hash())" <s> <k>` → the realm content hash at seed `<s>` after `<k>` seasons (`<k>` = 1 unless the gate names two; `<k>` = 0 the build hash); per item `<s>` = 0, at `.99` `<s>` = 0, 1, 2; each value quoted `reading @<sha>`. Before B03c moves the builder, `build_realm` is imported from `engine.season.harness.populated` (B00 to B03; B03g and B16L if they merge first). `[ASSUMPTION: `run(k, s, w=w)` advances `w` in place — basis: `harness/populated.py::run` builds its driver on the passed world, `workplan_v12_part6.md` head]` | B02.01 (the recipe, item A); `workplan_v12_part6.md` head; repair lane R1 (K3 F3) |
| the register's opening reading | `python -m engine.season.harness.register --check` exits 1 at the tree (the audit's reading at `601e715`: R2 27 violations, G6 3, H-47, H-48, H-59; re-read at B00's open and quoted there). So no gate reads it as exit 0: every gate reads **each check's violation count (R2, G6 and any other that reports) does not rise from the reading taken at the batch's opening (quote both, `reading @<sha>`)**; a gate about a row the batch itself edits keeps its own sentence beside that. | B03.51's form (`workplan_v12_part5.md`, B03.51 GATE); K4 F1; repair lane R1 |
| the corpus reading | Before B99 every gate or reading that runs the corpus runs `python -m engine.season.harness.corpus_run [seed] --seasons 2` (B02.39 adds the cap; without it each case plays its own span, clamped at `MAX_SEASONS`); B99's re-take runs it without the cap, the case's own span. | D-17; B02.39; K1 F3, K3 F2; repair lane R1 |
| a dead edit | A source edit whose target another item removes is not carried; the item says so in `UNDECIDED` with the reason. | `V12_STRUCTURE_part4.md`, "What the pilots found" |
| the verb table's open contests (after B07) | B07 adds the closed roster `contest_owed` (the writing rows still owed a `contests:` block). Every later batch that gives a verb its `contests:` deletes that verb from `contest_owed` in the same commit. | H2 notes (A10); `workplan_v12_part10_cont2.md` B07 |
| keyed refusal rows (after B08.02) | Every keyed refusal row added to `verb_table.yaml` after B08.02 carries a `sequence:` key. | H2 notes (A23) |
| the display names (after B41.11) | Every batch after B41.11 that adds a verb or an Event kind adds its `references/names_index.yaml` entry in the same commit (`16_PESSIMIST_GO_surface_pins.md` §3: the file gains the classes `verb` and `event_kind`). | H2 notes (A29); `workplan_v12_part29.md` B41 |
| the glossary always matches | An item that introduces, renames or retires a term edits its row of `unified/U1_GLOSSARY.md` in the same commit; the batch close reads each such row against the code it landed, and a mismatch fails the close (§4). | `STAGES.md`, "The glossary always matches" rule 2; the structure §5.11 |

---

## 4. Words

**Where a word is defined.** `unified/U1_GLOSSARY.md` is the vocabulary until the code carries the word; from then the tree's own owners are (`references/descriptor_registry.yaml`, `references/names_index.yaml`, Layer 1's vocabulary, the type and key names in code), and the glossary row's definition becomes a pointer to that owner and keeps its rejected-synonym column (`STAGES.md`, "The glossary always matches").

**The three glossary rules** (`STAGES.md`; they bind a reader, and no guard is built for them, CLAUDE.md §0.1 pt 5):
1. **Now.** The glossary reconciliation lane (U4d) has swept every live document; its record is the glossary itself.
2. **Every v12 batch.** An item that introduces, renames or retires a term (a roster key, a verb, a field, a band, a skill, an Event kind) edits the glossary row in the same commit as the code and says so in its `GLOSSARY:` line; the batch close reads the row against the code it landed, and a mismatch is a failed close.
3. **Every document edited after this.** It keeps to the glossary's words; a new word no row covers is added in the same edit, with its owner or "coined by the suite, plain word is X" (CLAUDE.md §4).

**The word test** (CLAUDE.md §4, RULED, ED-IN-0179; `STAGES.md`, "Terms mean what ordinary English says"): (a) a reader with no memory of this repository, given the word in its sentence, lands on the glossary's meaning; (b) the word is used that way outside this repository. If either fails, the ordinary word replaces it. Coin nothing a plain word covers. A new word introduced by an item carries its ordinary-English reading in one sentence, in the item and at the place it is invoked (the docstring, the roster's note, the `role:` line). A tree name that fails the test is not renamed by a document: prose uses the plain word and gives the identifier once, in backticks; the rename is an item only where a source writes its instruction (D-06). Jordan's own words are never renamed by an agent: *regime* (a camp of shared opinion, A-82, A-83), *rung* and *subformation* stand (A-94).

**A person's numbers** (A-98, A-106, A-107, A-112):
- an **attribute** is a person's native quality (`attr.*`); *aptitude* and *talent* are not used (an aptitude is an attribute); the attribute a skill draws on is its **governing attribute**;
- a **skill** is a learned rank, and a person's number in it is his **skill score**; *training* names only the act of learning (`grows_by: train`), never the rank; a learned skill is never lost (A-106);
- **martial skill** is a person's skill score in the skills used in fighting (`arms`); *prowess* is used only of a unit's troops and equipment (A-59), never of a person;
- a **derived score** is computed from attributes, skills and state and is never trained (health, wound count, resolve); a **choice score** is the chooser's valuation; bare "score" is not written without its kind;
- there is one kind of capability, the skill; the identifier `capability` (`Person.capability`, the registry's `capabilities`, `capability_uses`) is a second name for *skill* in code: prose says *skill* (its rename is held, §11);
- **traits** (`moved_by_evidence`, `moved_by_consequence`, `moved_by_authority`, `moved_by_solidarity`) are a separate roster on `Person.traits`, not skills, and give no dice (A-107; B04);
- a combatant's skill scores are read through the skill table like everyone's; the combat attribute `faculty` is dropped (A-112; `IS-PC-05` in B15).

**Armies** (A-2, A-94, A-95, A-99; the lexicon): a **unit** is a row of an army's record; the player sees *unit*; no size word for a body of troops is a game term (A-99's list), and there is no fixed-size level between unit and army. The bare word "formation" is refused: **army formation** is where an army's subformations stand, **unit formation** is how one unit's men stand. A **subformation** is a group of units at one post of the army formation, fighting by one set of tactics (lexicon D-1). The levels are three groups, not one ladder: the ground (realm, place), the raiser (faction, side), the army's chain (army, subformation, unit, troops). The code's names follow in B16L (L1) and B16M (L2) (D-07, D-08).

**The season and the fight** (A-101, D-05):
- a **lap** is one pass of DELIBERATE, RESOLVE and WITNESS inside a season; a season runs `scene_budget` laps. The code says `lap` from B04.01 (`PCR-4`: `Claim.round` → `Claim.lap`, `SeasonDriver.round` → `.lap`, `scenes_per_round` → `scenes_per_lap`); harness output keys keep the string `"round"`; Jordan's quoted words (A-63, A-64) keep his "round";
- a **round** is one engagement of a fight: two combatants close, exchange attempts to attack, then disengage; an **exchange** is one attack and the defence against it; a round holds one to four exchanges; no seconds are counted anywhere. The fight's code names follow in B16 (`PCR-3`: `max_bouts` → `max_rounds`, `turn_start` → `round_start`, `engagement_end` → `round_end`, `CombatTurnView` → `CombatRoundView`, `TURN_CHOICES` → `ROUND_CHOICES`);
- the **riposte** is the answering blow of a fighter about to be felled (one keyed draw at the felling); its code id is `finalblow_riposte` (Jordan reversed the rename to "counterblow" the same day; `U1_GLOSSARY.md`, *riposte*).

**Names that change before an item lands.** Sources were written against today's identifiers; an item after a rename keeps the source's text and adds a `NAMES:` line (old → new). The renames, by batch, are the structure §5.10, completed from the returned parts in part 2's names table.

---

## 5. Time efficiency and the critical path

`STAGES.md` step 6's six practices, as this plan applies them (Jordan: *"ensure plan will be time efficient by making use of all best practices in pinning sequencing common files caching back loading etc"*):

1. **Pinning.** Every deliberate hash mover is declared per item and co-batched; the seeded re-pin happens once per batch, at `.99` (E-1; P15). Hash-EQUAL batches run first where the graph allows: B00, B02, B03g, B03c, B16L, B03a, B13, B16M. **B03 is a mover, not EQUAL** (its authors: B03.28 deletes `Office.body_function`, an encoding mover; B03.86 removes the office bonus, a behaviour mover; one re-pin at B03.99), then B04's encoding re-pin, then the movers. The authors also found B36 and B40 to be movers and B34's `Scene.cost` not an encoding mover; part 2's hash-mover table governs. A before-reading is the last close's after-reading (`reading @<sha>`), never re-taken (the skill, Baselines; V1).
2. **Sequencing common files.** Part 2's file census lists, per file or symbol, the items that edit it in landing order; owners land before consumers (the skill home B04 before every user; the draw owner B06 before the task draw B07; the troop file B17 before the contact table B19a); the four serial instrument files (`harness/storybar.py` C3-K7, `loop/resolve.py::_canonical_order` C3-K8, `decision/choose.py::_stance_arm` C3-K3, `loop/witness.py::_told_value` C3-K1) are edited by one batch at a time; the permanent surface is appended once per batch, from its pre-allocated rows (§7, §12).
3. **Caching.** Prompt caches (CLAUDE.md §10): a shared preamble above the tier's cache minimum; fire one producer, await its first token, then fan the rest; change tier only at a batch boundary; extract shared reading once at the cheapest tier and fork only the judgment. CI and tests: `[skip ci]` on every commit except the batch's last `Item:` push and the confirming push (RULED 2026-10-13); `pytest -n auto`; mid-batch only the covering test file (`python tools/tests_for_diff.py`); the full suite once per batch (P16 (4)); a one- or two-season probe before any longer instrument run. A fact one batch establishes travels as a commit, a plan edit or a handoff pointer, never a recollection (the skill, "The context set").
4. **Back-loading.** The expensive verification (the review fan, the full suite, CI, the terminal critique) is paid once, at the close; calibrations run after what they depend on: B05 after B04; B15 and B19a after the round (B16); MBA-08 last in B19; BA1's soft edge (a calibration that closes before BA1 names the control it ran at and is re-read once at BA1's close, `IS_CHECK.md` C2); B98 after every other batch; drafting that costs no engine time starts early (`IS-A-11` stage 1 in B04).
5. **Parallelism and the critical path.** One open batch per lane; batches of different lanes run at once where §7's conditions hold. The critical path's batches come first among ties. A slow instrument is sized on two small runs (one and two seasons), launched in the background at the batch's open and read at the item that needs it (the skill, "Running a slow instrument"; CLAUDE.md §11 permits `Monitor` on local jobs).
6. **Checkpoints.** Long builds are dispatched in bounded pieces that return in tens of minutes; the orchestrator commits `[<scope>] WIP checkpoint: <handle>` on the producer's branch at each hand-back (`[skip ci]`, no `Item:` trailer), so a container restart loses at most one piece.

**The estimate formula** (E-15, which corrects the structure §2.4 to count positions, not member proposals): `EST(batch) = 0.4 h × positions + 2.5 h for the one close + 2 h where the batch runs a calibration or a long instrument` `[estimate — basis: CIP's two to three hours of agent time for CI-09, a 60-file mechanical item; no close has been timed under v12's rules]`. The `+2 h` batches, from the structure §2.2's cost column: B02 (`corpus_run` instrument time), B05, B15, B19 (calibrations), B19a (a background instrument run). B98 is taken at the structure's 8 h and B99 at 5 h (neither has positions until part 44 is written). ⚠ Part 44 now gives B98 87 positions and B99 2: by the formula with the `+2 h` (B98's probes, B99's long re-take), 39.3 h and 5.3 h; part 2 §1.2 carries the recomputed path (repair lane R1).

**The estimate, computed** (a scratch script, not committed: positions counted as the distinct item handles in every position table of parts 3 to 43, `.99` included; the graph is the structure §2.1's `after` column only, without the edges the authors found, §8): **about 706 h** if every batch ran one after another; **about 354 h** along the longest chain weighted by these estimates, which is the SE middle of the structure's four tied middles: B00 (3.3) → B01 (3.3) → B02 (19.7) → B03 (28.5) → B16L (4.5) → B03a (3.7) → B04 (12.9) → B05 (20.1) → B06 (5.7) → B07 (6.5) → B09 (11.3) → B10 (29.3) → B11 (25.3) → B12a (18.5) → B12b (21.7) → B12c (15.3) → B25 (11.3) → B32 (15.7) → B35 (14.5) → B36 (9.7) → B38 (28.5) → B39 (17.3) → B40 (14.1) → B98 (8.0) → B99 (5.0). Every figure is an estimate. **Measured times replace them:** B00, B01 and B02 record their measured wall time, build and close apart, in their closing commit bodies, and from then on each batch's est. cell in part 2 is replaced by its measured value at its expunge (the structure §2.4). The critical path by steps (25 steps under the one-open-batch-per-lane rule, the structure §2.3) is part 2's to recompute with the added edges.

**What shortens the path.** The four middles are tied by steps (the structure §2.3): shortening one alone shortens nothing. Weighted by hours, the SE chain B11 → B12a → B12b → B12c → B25 is the longest; B10 (67 positions), B03 (65) and B38 (65) are the largest single batches on it. No batch is re-cut by this head (the structure §10.1 item 9: no lane re-cuts a batch).

---

## 6. Two seasons, the settings batch, and the re-take

**The cap** (P10; D-17; A-114). Every probe, item gate and batch close reads at two seasons or fewer. A source's three- or four-season reading is written at two with its source horizon noted; an arm that cannot be seen within two seasons is reported, not asserted, and its longer reading is left to B99.

**B98-dials** (D-22). A setting an item ships at its control value (a switch off, a gain at 0, an empty roster) is listed in its batch's `DIALS AT CONTROL:` line with its control value, who sets it and its target reading. A setting its own batch sets needs nothing more. Every other setting is a member of B98: part 2's settings table collects them from every block; lane A44 writes one item per setting, in the order their mechanisms landed, each from its source's own calibration text: the target reading on named seeds, the control arm (the setting at its control value reproduces the previous item's hash) and the revert. B98 re-pins once, at `B98.99`. A setting whose source states no target is `BLOCKED (design: no target reading)` and ships at control. B98 is not folded into B99: a reading and a mover in one close would make the re-take's tree the one being re-pinned (D-22).

**A setting whose only target lies past two seasons.** B98 is under the cap, and B99 is a reading batch, hash-EQUAL (the structure §2.2), so neither flips it. It is written in B98 as `BLOCKED (target reading beyond two seasons; A-114)`, and B99 quotes its reading on the tree as left `[ASSUMPTION: the consequence of D-17, D-22 and B99's EQUAL row, stated here because two authors met it: `02_CHAR_scar_is_a_wound` gate (b) reads at eight seasons (the scar flip and `scar_weight_shift`, B10's first half); the four Church Influence flips cannot be judged within two seasons (B21d, B41, B11F1's author); A44 applies it; Jordan may call a longer reading, P10's "unless Jordan calls for it"]`.

**B99-nine-retake** (D-17; A-114; `IS-A-13`). One item, the plan's last: the longer re-take of all nine, on B98's closing tree, at the horizon `IS-A-13`'s gate states. It is the only batch that may edit a row's `status:` in `engine/season/requirements.yaml`. `IS-A-13`'s milestone re-takes do not run at the milestones (A-114: *"ideally no? that would take forever"*); between milestones the rows stay as they are and the conjuncts' `reading:` records carry the readings.

---

## 7. Parallel sessions and the coordinator

Jordan (2026-11-12): *"can we set up plan so that it can run parallel sessions"*. What the repository gives: separate in-flight rows per lane, the lane-split ED ledger, `isolation: worktree` for write lanes, and `create_session` not denied (CLAUDE.md §11). What forbids more: the skill allows one open batch per lane's in-flight row and stops an invocation that does not match it, so **parallelism is across lanes, never inside one** (`STAGES.md`, "Parallel sessions").

1. **Lane tags.** Every batch carries one lane of the nine-lane roster (`tools/ci_common.py`: MB, PC, FI, SC, FA, WR, IN, GO, SE); B12a, B12b and B12c carry SE and WR and hold both lanes (D-21). At most one open batch per lane.
2. **Waves and steps.** A wave is a dependency level; a step is a slot of the lane schedule (§8). Batches open in one step only if (a) no gate runs between them, (b) they are in different lanes, (c) their edit sets are disjoint or meet only under the hot-file rule (3), (d) their hash movers have a merge order (4), and (e) the step stays within the concurrency cap: six open batches `[ASSUMPTION carried from the structure §2.3: each session's `pytest -n auto` gets the machine's cores in turn; `nproc` read 4 there; the cap is the coordinator's to lower]`.
3. **The hot-file rule** (U3 §1.1; the structure §7.3). Sixteen files are edited by twenty or more proposals (`rosters.yaml`, `data/fixtures.py`, `queries/world_q.py`, `verb_table.yaml`, `queries/person_q.py`, `loop/effects_information.py`, `decision/options.py`, `queries/inputs.py`, the realm builder (`boot/realm.py` after B03c), `seam/wrappers/sigma.py` and six more; part 2's census). Two batches open in one step may edit one of them only in different top-level keys or functions; the merge keeps both edits by hand in the batch table's order and never regenerates the file. A pair that cannot keep to that is serialised by the coordinator within the step. The four serial instrument files (§5 point 2) are edited by one batch at a time. The coordinator checks the step's batches against the census at the step's open.
4. **Hash movers in one step** (the structure §7.4). Movers of one step merge in the batch table's order; the later rebases on the earlier's merge, takes the earlier's after-reading as its baseline (`reading @<sha>`) and re-pins once; a hash-EQUAL batch merges at any point. Part 2's hash-mover table gives each mover its merge position. Orders the authors already wrote: S4 B03g, B03c, B16L; S6 B13 and B16M before B04, which re-runs `tools/export_composition.py` and `tools/export_sim_params.py --build` after its rebase; S13 B08 first, B16 rebases on it; S17 B28 before B32; S18 B23 before B30 (both edit `seam/wrappers/mass_battle.py::resolve`).
5. **Ids up front.** B00 allocates every batch's ED block and hole-register block before any session cites a number, and lands on `main` first (§12; CLAUDE.md §4: renumbering does not escape a collision).
6. **The permanent surface** (the structure §7.6). `engine/season/hole_register.yaml`, `engine/season/requirements.yaml` (`reading:` records only, by a batch's last `Item:` commit; `status:` only in B99), the ED ledgers (lane-split), `references/id_reservations.yaml`, `references/restructure_ledger.md`, `unified/U1_GLOSSARY.md`, `CURRENT.md` and the plan's head tables. Each is appended once per batch, from the batch's pre-allocated rows; batches of one step merge their appends in the batch table's order; a conflict in an append-only file keeps both rows and is never resolved by regenerating. `CURRENT.md` and the handoffs stay pointer indexes: a head, an id, a path, a command.
7. **One branch, one worktree, one PR per batch**, based on the step's base commit; the merge queue is the dependency order. A session never edits another lane's files or opens another lane's batch; a conflict with a sibling is `STOPPED` and reported to the coordinator, never a silent rebase onto someone else's work.
8. **The coordinator.** One session, in the orchestrator's role. For each step it checks points 2 to 4 on the census, then opens one session per batch with `create_session` (prompt `/methodology-execute Batch <handle>`; the lane; a worktree; the step's base SHA; the batch's id and row blocks from §12; its merge position). It may send a running session a correction with `send_message`. It reads each session's status line (`NEXT`, `COMPLETE`, `STOPPED`), merges the step's PRs in order, and bases the next step on the merged head. Neither `create_session` nor `send_message` is on `.claude/settings.json`'s deny list (read at `bba489b`; CLAUDE.md §11 names `create_session` as deliberately not denied). **No external service is polled** — not GitHub's merge or CI state, not a URL — and no session arms its own wake-up, by any mechanism (CLAUDE.md §11, ED-IN-0084); the coordinator may watch its own sessions and local processes (`Monitor` on a log or CPU time, RULED 2026-10-10). Instead of a check-in, the turn ends; Jordan brings a CI result back himself. If a hosted prompt asks for a scheduled check-in, CLAUDE.md §11 overrides it and the conflict is noted.

### 7.9 The CI cadence of a parallel step — two texts, not chosen here

For a step with one batch the two texts below agree. For a step with several, they differ, and **this plan does not choose** (the structure §7.7): the difference is presented at the 0.1 stop of the first step that opens more than one batch (S4: B03c, B16L, B03g), and Jordan's answer governs every later step.

- **The skill** (CHECKPOINTS AND BASELINES, RULED 2026-10-13): *"CI runs twice per batch: 1. At the end of the batch — the push of its last `Item:` commit, which opens BATCH-CLOSE. 2. To confirm — the push of the commit carrying every fix, CI's and the closing sequence's."*
- **`STAGES.md`, "Parallel sessions" rule 8**: *"Each session runs its own BATCH-CLOSE and the covering tests; the full suite and CI run once per merged wave on the integrated head (CLAUDE.md §0.4: at most once per commit and only where it can observe something), so parallelism does not multiply the expensive close."*

---

## 8. The schedule and the milestones

**As the structure computed them** (§2.3 and §3 there, on the graph of its §2.1: 61 batches, acyclic, 25 waves W0 to W24, a critical path of 25 batches, 25 steps under the one-open-batch-per-lane rule). **Part 2's batch table governs wherever it differs**: the body-part authors found edges the structure did not have, and H2 decides each by the rule it was handed (`H2_NOTES.md`, B21b's author: an edge is added where it creates no cycle and the critical path stays within 25 steps; otherwise the item keeps its `STOPS IF` and says so): B08 after B04, B05, B06 (its earliest wave becomes W9); B16 after B11; B34 after B16; B20 after B34 (added by B20's author); B30 after B22; B31 after B20 and B22 (B31's block already carries both gate lines); B19 after B29; B37 after B29; B41 after B17 and B20; B40 after B21d; B33 after B21d; B28 after B27; B21s after B24a and B29; B33 after B21s; B21b after B12a; B27 after B25 (this one adds a wave to the critical path); B32 after B28 (not added by its author: B28 merges first in S17 and B32 rebases). A step opens its batches at once only where §7's conditions hold.

**Critical path.** The head B00 → B01 → B02 → B03 → (B03c or B16L) → B03a → (B04, B13 or B16M) → B05 → B06 → B07 → B09 → B10, then one of four middles of equal length — (a) B15 → B16 → B19a → B19 → B20; (b) B11 → B21b → B21c → B24a → B27; (c) B21 → B21b → B21c → B24a → B27; (d) B11 → B12a → B12b → B12c → B25 — then the tail B32 → B35 → B36 → B38 → B39 → B40 → B98 → B99. Shortening one middle alone shortens nothing. Weighted by hours, (d) is the longest (§5).

**Steps** (one open batch per lane; the critical path first among ties, then IS-A §12.3):

| step | open at once |
|---|---|
| S0–S3 | B00 · B01 · B02 · B03, one each (IN) |
| S4 | B03c (IN), B16L (MB), B03g (GO) |
| S5 | B03a (IN), alone in the plan: it edits the comments of every game-code file |
| S6 | B04 (IN), B13 (PC), B16M (MB) |
| S7 | B05 (IN), alone: it edits IN, SC, PC and MB code |
| S8 | B06 (IN), B14 (PC) |
| S9 | B07 (IN), B17 (MB) |
| S10 · S11 | B09 · B10 (IN) |
| S12 | BA1 (IN), B11 (FI), B15 (PC), B21 (FA) |
| S13 | B08 (IN), B12a (SE+WR), B16 (PC), B21b (FA), B24 (SC) |
| S14 | B12b (SE+WR), B19a (MB), B21c (FA), B29 (PC), B34 (GO) |
| S15 | B12c (SE+WR), B18 (PC), B19 (MB), B21d (FA), B24a (SC), B41 (GO) |
| S16 | B11F1 (SE), B20 (MB), B25 (FI), B27 (SC), B37 (IN) |
| S17 | B11F2 (IN), B22 (MB), B26 (FI), B28 (SC), B32 (FA), B37p (WR) |
| S18 | B21s (IN), B23 (FA), B30 (MB), B35 (WR) |
| S19 | B31 (MB), B33 (FA), B36 (WR) |
| S20 · S21 · S22 · S23 · S24 | B38 (WR) · B39 (WR) · B40 (FA) · B98 (IN) · B99 (IN) |

**Milestones and the requirement map** (the structure §3, with `IS_A_NINE_part2.md` §12.2's expected readings). A milestone is a set of batches whose last close is a point at which every conjunct of its rows has a reading on one tree. No row's `status:` is edited at a milestone (A-114): readings go into the conjuncts' `reading:` records, and the one re-take that may move a row is B99. Each batch's `REQUIREMENT:` line is the map's row for that batch.

| milestone | closes at | batches | rows whose conjuncts are all read by then | expected reading |
|---|---|---|---|---|
| **M0 · ground** | B04 | B00, B01, B02, B03, B03g, B03c, B16L, B03a, B13, B16M, B04 | R-01, R-02 (on the new instruments), R-03 | all three hold; the other six print their held counts for the first time |
| **M1 · every outcome is drawn** | B08 | B05, B06, B07, B08 | R-03 (with R-03.c); R-09.a, .c, .d, .e | R-09 short of R-09.b only |
| **M2 · persons** | BA1 | B09, B10, BA1 | R-06, R-08, R-09; R-07 if R-07.c reads with its receipt | R-06, R-08, R-09 hold; R-07 holds or is one conjunct short |
| **M3 · every verb** | B35 | B11, B12a, B12b, B12c, B14, B15, B21, B21b, B21c, B22, B23, B24a, B25, B26, B27, B28, B29, B32, B35 | R-05; R-07 if still open | `built out n of n` at B35's `n` |
| **M4 · every scale** | B36 | B16, B17, B19a, B19, B20, B24, B30, B34, B36 | R-04 | every R-04 conjunct holds |
| **M5 · the rulings beyond the nine, and the carried positions** | B40 | B18, B31, B33, B37, B38, B39, B40, B41, B11F1, B11F2, B21d, B21s, B37p | none new; R-05 re-read at B38, R-06.e and R-09.b at B39, all nine at B40 | all nine hold |
| **the settings, then the re-take** | B99 | B98, B99 | all nine, on B98's closing tree (the settings as set) | `m1_acceptance --summary` row 3 reads what the readings say |

One risk the authors named against M3: B35's author found no source that writes `knot`'s effect, so R-05 may read `n − 1 of n` at B35's close and `IS-A-08` would then fail that batch's gate; whether a WR design item precedes B35 or the residue is accepted is part 2's to settle (H2 notes, A36), and until settled B35.28 is `BLOCKED (v12: a carrier is owed)`.

---

## 9. Defaults in force

**No question is open.** No `V12_FOR_JORDAN.md` exists: the structure lane found nothing that survived the ladder (the structure §1). Every decision register reads answered or ladder-closed: `unified/DECISIONS_QUICKSHEET.md` ("Every decision is answered or ladder-closed"), `unified/U3_JORDAN_CALLS.md` (A-92, A-93), `unified/U4D_FOR_JORDAN.md` (A-94, A-98), `unified/U6_FOR_JORDAN.md` (A-96), `master/instructions/IS_FOR_JORDAN.md` (A-106), `master/HOLISTIC_FOR_JORDAN.md` (A-102), `master/eval/EVAL_FOR_JORDAN.md` (A-103 to A-111, A-114), `master/mb_abstraction/MBA_FOR_JORDAN.md` (A-113), `master/pc_round/PCR_FOR_JORDAN.md` (nothing survives). **What stands instead are defaults taken by the ladder or marked `[ASSUMPTION]` inside a ruling**, each reversible on Jordan's word (V3) and each carried by the items that rely on it. They are listed here so he can reverse any with one line.

| default in force | what the game does under it | where it was taken | to reverse |
|---|---|---|---|
| the ladder-closed decisions of the original register | D-20 superseded by A-57/A-58; D-25 A (an arrest needs no officer beside the prisoner); D-27, D-28, D-31 by A-24; D-36 A (three organising verbs); D-40 A now, B behind a dial at zero; D-41 B (first-exchange edge on an unexpected opener); D-44 A, D-45 A (no engine-authored wrong conclusions); D-46 B (a refusal teaches privately); D-48 A (forgetting computed when read); D-68 B (farm work an act, after the cohorts' moves); D-69 A (famine reports once); D-72 A (a lord over an empty land stays); D-74 B (fix the witness code, not Layer 1) | `unified/DECISIONS_ANSWERED.md`, "Closed by the five-step ladder" | each row's other option |
| how a seat helps a roll (D-U1-01) | a seat gives a small named edge, soft-capped, when its holder acts through it before a body he sits on or presides over; a man above you raises the obstacle; a seat never adds dice and never helps resist | `unified/U1_JORDAN_CALLS.md` | the `office` source becomes a pool addend |
| no separate rhetoric skill (D-U1-03) | `argue` covers persuading one person and pleading in court; `law` is knowing a forum's rules; `insight` is reading a room | the same | one definition row, two cells |
| an unauthored attribute is average (D-U1-04) | a sheet that does not name an attribute reads the middle of the 1–7 scale; until the cast's values are authored (BA1), every person holds the untrained skill score and average attributes, and every rolled act is a `routine` task until per-task difficulties are authored | the same; B01's `unauthored_attributes` dial (part 3) | store a value for everyone |
| the year has named seasons (D-U1-10) | four seasons (Jordan's ED-IN-0332), named spring, summer, autumn, winter | the same | rename the four members |
| the U3 conflicts closed by the ladder | no office bonus to scenes; no new Seat fields (data on the seat's arrangement rows; `lot` a value of the filling roster); no new choice-score term for an act's matter; recovered troops computed when an army's strength is read, by a keyed draw; seizure is the victor's act; seats pass with land through the revoke basis; a person appearing in play is minted with the census's fields; no task "stake" expansion; a roll's margin stored as whole thousandths; no float log (vectors); the player's screen reads his firsthand knowledge | `unified/U3_JORDAN_CALLS.md`, "Not yours" (C3-L1, -L3, -L4, -L7 to -L14) | each row's other way |
| the fight's round (PCR) | initiative resets each round; at most four exchanges a round; a landed hit does not end a round, a clean defence does; a clean disengagement or a re-opened measure ends it; no seconds anywhere; the season's pass is a *lap* | `master/pc_round/PCR_FOR_JORDAN.md` items 1–6 | each item's "to reverse" |
| the mass-battle abstraction's ladder answers | the contact draw is a count of duel rounds drawn on the bell curve, not the opposed rule; a contact returns men put out of the fight, their kind drawn at the field's end; the troop column `power` is the men's martial skill, renamed `skill`; exposure is well under one duel round per field tick, its level flagged not established; the duel's reach edge is reported to the PC lane, not tuned in MB; the side-wide luck multiplier is removed (A-77); no seconds | `master/mb_abstraction/MBA_FOR_JORDAN.md`, "Not yours" | each row's other way |
| the codebase proposal's ladder answers | the code's dated history is cut from comments in B03a (`CI-02`); the two big registries lose notes, not values (`CI-01`); the season's settings stay authored in Python and exported (`CI-04`); the big files are not split; the old `systems/` simulation scripts are kept (ED-IN-0283); `tools/` is not held to the efficiency standard, three unread files are deleted (`CI-10`); personal combat becomes a package (`CI-09`) | `master/HOLISTIC_FOR_JORDAN.md`, "Decided by the ladder" | each row's other way |
| the evaluation's ladder answers | EVAL-2 B: the army verbs count as built out only when the chooser forms them (no menu door, CR-52 not built); J-E3-3: no engine version is written anywhere (ED-GO-0002 owns it); J-E3-4: no common-fact store; CR-94 retired `[ASSUMPTION]` | `master/eval/EVAL_FOR_JORDAN.md` | each entry's other option |
| assumptions inside rulings | A-58: entry by the holder's leave is not aggression; consent is read from a standing act or commitment between the two · A-64: precedence orders access and gates nothing; a petition's intensifying is drawn from the laps waited; an appointment is a commitment between two persons · A-66: seizure after a win is an act the victor forms · A-69, A-78: the defender's army carries and recovers losses as the aggressor's does; acting (recall, rally, muster) recovers more than doing nothing; the proportions of the kinds, the rate and the window are content not yet given · A-70: an attack is an attack whoever invited the attacker; standing by leave is not occupying · A-87: the Restoration movement and the Einhir Revival correlate with the anti-caste side · A-104: the rule holds for every person's management orders, not only the player's | `unified/DECISIONS_ANSWERED.md`, each row's `[ASSUMPTION]` | each row's stated revert |
| v11's defaults in force, where nothing supersedes them | M3: the field stays persons at weight; M22 to M40 at their defaults (v11 `-05` §1c) where no v12 item replaces them; the arc's target share is Jordan's: CR-90's reading is recorded, never a bar, and no CR-89 flip is kept for hitting a number (v11's reference reading, at season 24, is past the cap and is no gate of v12); `violence_contexts`: war, crime and duel, with defence (CR-87); Valorsmark is the Crown's faction renamed, "Crown" an alias (CR-86); `guards` ships ON once CP-T09-07 (b)'s union lands (B21b; A-103 keeps only the cap and `guards`); CR-38's design (the Court Parliament's bench) is a design item ratified at B21c's merge, with A-76's interim bench meanwhile; CL-THRUST's B6.n ladders are Jordan's content (TL-B6.n, blocked); `age_step` and `illness_rate` no longer wait: natural death is on once the 46 ages are authored (A-15; B37) | v11 `-00` §6 risk 4 (`E1.md:59`, STILL-NEEDED), with A-15 replacing its last clause | each default's revert in v11's text |

Not defaults but picks the authors left to Jordan's correction inside a batch (listed again in that batch's PR body, D-19): `YIELD_OB` and the `mortal_wound_ob` sweep's pick (B15); the troop file's seed values (B17, B19a). A pick of this kind ships as drafted and is ratified by its batch's merge unless that PR body holds it back.

---

## 10. What part 2 holds (lane H2)

This part does not write them; each is generated by script from the returned parts where it can be, and says so (the structure §7.2): **the batch table** (the structure §2.1's columns with §2.2's requirement, hash and est. columns, the part that holds each batch, and the edges of §8 that H2 adds); **the serial-edge table** (with D-02 and D-03 recorded as edges not taken); **the file census** (every item's `WHERE`, compared with U3 §5.1 and CIP §3.2); **the hash-mover table** (each batch's movers, what `.99` re-pins, and its merge position within its step); **the Layer 1 amendment status** (U3 §1.4, the nodes still held, and the two edits made on ED-IN-0300 with no node, B11.04 and B41.03); **the tests and probes to write**; **the tools, exporters, modules and harness files created**, each with its caller; **the symbols with no carrier**; **the settings at control** (B98's member list, §6); **the names** (old → new, by batch); **the held table** (the intake's 54 held entries with their triggers, in each lane's "held and leave" wording; ED-SC-0001 and ED-1043, whose triggers already fired, are items of B15 and B19). The id and row blocks are this part's §12.

---

## 11. Adoption, the retirement of v11, and what is held back

### 11.1 Adoption is Jordan's

Until he adopts it, v12 stays under the suite as a proposal. Merging the PR that moves it into `workplans/` ratifies its PROPOSED contents (ED-1094), except what the PR body holds back (§11.2), and retires v11 in that same commit (CLAUDE.md §2: one active plan per lane; adopting a plan retires what it supersedes in the same commit). The adopting commit, in order (the structure §8.1):

1. `git fetch --unshallow` if `.git/shallow` exists (it does at this read): every `<sha>` below is read on `main`.
2. `git mv` the draft files to `workplans/valoria_master_workplan_v12.md` and `workplans/valoria_master_workplan_v12_partN.md` (after the orchestrator's one renumbering of the `_cont` files, §14); rewrite the draft path inside them; one `## Status:` line per file.
3. Allocate one `ED-IN-` id for the adoption from `references/id_reservations.yaml` (read `next_free`, allocate, bump, co-commit; CLAUDE.md §4); its row in `registers/editorial_ledger_in.jsonl`. It fills `ED-IN-<the adoption id>` in every Status line, and every IN range of §12 starts after it.
4. **Delete v11**: `workplans/valoria_master_workplan_v11.md` and `_part2.md` to `_part17.md` (eighteen files, listed at `bba489b`), each with this row in `references/restructure_ledger.md`:
   `| \`workplans/valoria_master_workplan_v11<suffix>.md\` | \`FORK:<sha>\` | FORKED (<date>, superseded by \`workplans/valoria_master_workplan_v12.md\`, the one active plan for every lane (\`ED-IN-<id>\`); every position has one recorded disposition, carried into a v12 batch or retired with the superseding item cited, in the evaluation retired in this same commit; \`<sha>\` is the last commit on main that carries the file, so the text there is the file) |`
5. **Delete v11's build files**, which v11's own §9 step 5 ties to its batches: the fourteen `proposals/2026-10-24-master-workplan-v10/2026-10-24-v10-09-build-<name>.md` (`00-sequence`, `B10-11` to `B10-18`, `B10-18b`, `B10-18c`, `B10-19`, `B10-20`, `B10-Z`; all fourteen present at `bba489b`), each with:
   `| \`proposals/2026-10-24-master-workplan-v10/2026-10-24-v10-09-build-<name>.md\` | \`FORK:<sha>\` | FORKED (<date>, workplan v12's adoption (\`ED-IN-<id>\`): the build instructions of a v11 batch; v11 is retired and its carried positions are v12 items; \`<sha>\` is the last commit on main that carries the file) |`
6. **Delete the suite's work ledgers whose own Status line says so**: the list is `grep -l -i -r 'deleted when .*v12 is adopted' proposals/2026-11-12-subsystem-audit-suite`, re-run on the adopting tree (it lists 41 files at `bba489b`: the evaluation and its parts, `master/GAP_REGISTER_EVALUATION.md` and its parts, `master/eval/E1.md` to `E5.md` and `E8.md`, the intake, `master/eval/EVAL_FOR_JORDAN.md`, `master/EVALUATION_ORDER.md`, `master/INSTRUCTION_SUITE_ORDER.md`, `unified/U2_LAYER1_CONFORMANCE.md`, U3, `unified/U3_LAYER1_AMENDMENTS.md`, `unified/U4_DOCUMENT_STATUS.md`, `unified/U4_TRACEABILITY.md`, and under `master/workplan_v12/` the order, the four structure files and `H2_NOTES.md`); with `master/instructions/IS_CHECK.md` (its Status line: "it dies with them when v12 is adopted"); with `master/eval/E6.md` and `E7.md` if their lanes meant the same `[ASSUMPTION carried from the structure §8.1: their Status lines read "read-only lane output" and name no deletion]`. Each gets an exact-file `FORK:` row in the form of step 4, its reason "a work ledger of the v12 fold, deleted on adoption by its own Status line". A v12 `SOURCE:` or `C(...)` line that cites one of them resolves through its row and is read at its `FORK:` SHA (`git show <sha>:<path>`). The proposals, the instruction files, the two design directories (`master/mb_abstraction/`, `master/pc_round/`), CIP and the glossary stay: they are design reference (CLAUDE.md §0.05).
7. **Carry forward what v12 still needs from v11**, and nothing else: the nine `met` texts (inside `IS-A-02`'s item, copied from `IS_A_NINE.md` §2 to §10, until B02 lands them in `requirements.yaml`); the 22 head rules (§3.A); the 54 held entries with their triggers (part 2's held table); the carried positions' own text (in the items).
8. **Re-point the live pointers**: `CURRENT.md`'s plan row, and its rows that cite a v11 part for held residue (mass battle, social contest), to the v12 batch or held row; `references/lane_assignments.yaml`'s `source:`; the Open rows of the lane handoffs that name a v11 position, each to its v12 item or removed where the evaluation retired it. Docstrings, frozen register text and ledgers that cite a v11 file are left as written and resolve through the rows. `engine/season/requirements.yaml`'s two `measure:` strings that name a v11 part (the structure §0 fact 3) are re-pointed in the same commit, as v11's own adoption re-pointed the equivalent strings (v11 §9 step 4) `[ASSUMPTION: precedent, ladder step 4; the structure's step 8 does not list them]`.
9. **Verify**: every new row is read as an exact row through `tools/pathres.py`'s `load_alias_map()`, never `resolve()`, which matches directory prefixes (CLAUDE.md §8); `python tools/currency_consistency_check.py`; `python tools/validate_ed_citations.py`; `python tools/freshness_gate.py`; `python -m engine.season.harness.register --requirements`; `grep -c '^## Status:' workplans/valoria_master_workplan_v12*.md` reads 1 per file; the test files `grep -rl valoria_master_workplan tests engine/season/tests` names. Not the full suite: no program opens a workplan file (the structure §0 fact 3).

`proposals/2026-11-04-strife-flows/00_MASTER.md` and `01_STRIFE_KINDS_DRAFT.md` are **not** deleted, though v11's §9 step 5 scheduled them to go with its last strife position: they are the RATIFIED strife design `CURRENT.md` names (ED-IN-0316), and A-84's held rewording is of that file `[ASSUMPTION carried from the structure §8.1 — basis: CLAUDE.md §0.05, design documents are not deleted by a plan's retirement; Jordan may say otherwise at the merge]`.

### 11.2 The PR body says what is held back

Merging ratifies everything PROPOSED in v12 except what this list holds back (ED-1094: the exception must be loud). The adopting PR's body carries this table; each batch's PR body adds its own authored values.

| held back | why | where its text is |
|---|---|---|
| canon lines 76, 90 and 96 and the Coup Counter wording (A-17) | canon changes only by Jordan's amendment; no v12 item edits canon | `audits/15_INSTITUTIONS_SYNTHESIS.md` §4.6, A1–A4 |
| five sentences of the ratified strife master (A-84) | a ratified design document; B38 builds the era, the master's text waits on his amendment (A-97 names canon and the strife master as held) | `audits/30_ERAS_REGIMES_STRIFE_AND_MOMENTUM.md` §6 |
| the 2026-07-08 directive A-60 narrows | its sentence was not located by any lane; leads, unopened: the `registers/editorial_ledger_mb_archive.jsonl` rows dated that day (ED-MB-0004 to -0007, ED-MB-0041) and the quotation at `proposals/04_MB_cr12_linear_law.md:40-43` | — |
| `CLAUDE.md`'s preamble sentence naming ED-GO-0002 as the one owner of the engine version | B03g lands a machine-read owner (`references/engine_series.yaml`, GO-01); whether the preamble sentence changes is Jordan's (a Layer 0 file) | `workplan_v12_part6.md`, B03g, its `UNDECIDED` (5) |
| `CLAUDE.md` §3's sentence on the `pc_engine` path seam | B13 deletes the seam (`CI-09`); the sentence is edited in B13's own commit and named in that PR, not in the adopting one | D-09 |
| GO-09's line in `.github/workflows/valoria-ci.yml` | `.github/CODEOWNERS` gives Jordan the CI and workflow gates; B03g wires the exporter's `--check` through the local tier, a `references/ci_checks_registry.yaml` row and a suite test, and the workflow line goes in B03g's PR body for him | `workplan_v12_part6.md`, B03g, its `UNDECIDED` (2) |
| Layer 1 items still held | the `REF` rows of `unified/U3_LAYER1_AMENDMENTS.md` (A-17, A-84, A-60, above); Layer 1's word "round" for the lap (`04` row 36; `holonic_ARCHITECTURE.md:1166`) and "exchange" at `03:126`, listed for him and not applied (PCR-4 renames the code, Layer 1 is not edited to match it); the identifier `capability` and Tenure "edge", both named by Layer 1 (D-06); B03.19, Layer 1's rejection-5 measurement paragraph made a command (`11_GO_pointer_and_stale_text_resolutions` item 6; HELD); `U5b_MB_residue` §2 R-38, a Layer 1 text edit (B17's author); B11.04 (`04` §C.6, CR-29) and B41.03 (`04` §C.12), edited on ED-IN-0300 with no node in the amendments ledger: part 2's Layer 1 table confirms the ED covers each or holds it; NM-W5's possible `04` §A.2 row (B36.08 is HELD if it needs one). The `CODE` row for A-26 (the `degree_from_net` docstring) is not held: B05 rewrites it | part 2, the Layer 1 amendment status |
| `off_npc_084`'s rung | B03.69 (`IS-B2-CORE-06` with CR-07, H-89, DEF-5, A1-46) is BLOCKED: the guild leader's seat has `rung` None and needs a rung or a scope authored, or A1-46's revert (keep the `scale:` column and author a reader) | `workplan_v12_part5.md`, B03.69 |
| every authored value | Jordan's, or a content pass he corrects (D-19; risk 6): the cast's five tables (BA1); the troop file's seeds and the stated matchup rows (B17, B19a, B19, B31; A-113); the names and texts of `21_PROCEDURAL_E`; the surface pins; the 46 ages (A-15, B37); the shares of what an army carries back (A-69, A-78); `YIELD_OB` and the `mortal_wound_ob` pick (B15); `territory_weight` (B21); the `wound` kind `harbour` (B12a); which events are concealed (B11); `window_responses` (B20); the `caste_practice` and `riot` cell values (B38); `secondary` (B31); CL-MGMT's list of management orders (held); the court holder's registry row (B33.09); the settings B98 sets | each batch's PR body lists its own |
| the blocked entries | each waits on something outside the tree's reach: CR-07 with H-89 (`off_npc_084`'s rung, above), H-191, H-198 with M9, H-325 with H-326 (the A-109 design), TL-B6.n, GO-06 and H-5 (a `valoria-game` checkout); and every item a body part marks `BLOCKED` with its owner. ⚠ Reconciled 2026-11-12 (A-116): the B10-16 gates entry (SE) and CP-T08-07 left this list: Jordan answered the lift (J-02), its build is B12c.30 to .34, B10.79 is a POINTER to it and B33.30 is HELD on B12c.34 | the intake, each entry; each batch's position table |
| the 54 held entries | no work until a trigger fires | part 2's held table |
| the CI cadence of a parallel step | two texts differ (§7.9); presented at the first parallel step | §7.9 |
| who wrote the design and instruction documents | Fable, by Jordan's direction of this session, a departure from CLAUDE.md §10 ("not artifact authorship") that `STAGES.md` records | `STAGES.md`, "Model assignment per stage" |

No engine version is asserted anywhere in v12 (ED-GO-0002 is the owner).

---

## 12. Ids and row blocks (B00's allocation, proposed)

**This is a proposal, not an allocation.** `references/id_reservations.yaml` is not edited by this part; B00.01 makes the allocation on its own base, from this table (the structure §7.5; `workplan_v12_part3.md` B00.01). B00.01's `WHERE` names "the plan's head part 2" for the table; the table is here, and B00 reads it here.
⚠ Superseded by `workplan_v12_part2_cont2.md` §9 (lane H2): the same method re-run with IN from 0363 and B12c's H count 12; B00 reads that table. ⚠ The table's rows below are now copied from that §9 table by repair lane R1 (2026-11-13), so the two agree (B98-dials `ED-IN-0399..0400`, `H-846..H-850`; B99-nine-retake `ED-IN-0401..0402`, `H-851..H-855`, as part 44 takes them); the method bullets above keep the H1 readings they were made from.

**How it was made.**
- **Readings at `bba489b`:** `lane_ids.lanes.<LANE>.next_free` is MB 82, PC 60, FI 10, SC 41, FA 40, WR 13, IN 361, GO 3, SE 57; the highest hole-register id in `engine/season/hole_register.yaml` is H-362 (the file holds no next-id key, `unified/U3_CONFLICT_LEDGER.md` T-4); the highest registry id in `references/npc_registry.yaml` is NPC-090 (46 rows).
- **IN starts at 0362**: `ED-IN-0361` is taken by the adoption (§11 step 3) `[ASSUMPTION: no other IN allocation lands first]`. ⚠ Reconciled 2026-11-12 (A-115/A-116 lane): the assumption failed. `ED-IN-0361` is the record of Layer 1 node `L1-A115` (A-115), and `next_free` reads 362; so the adoption takes `ED-IN-0362` and every IN range below shifts by +1, by the next bullet but one (B00 re-reads on its base).
- **Counts** are each batch's declared `IDS:` lines, summed across a split batch's halves (grep `IDS:` in every body part). Where two halves disagree the larger count is taken and the spare covers the rest: B19 declares ED-MB 1 in its first half and none new in its second (the superseding row on `ED-MB-0016` keeps its id), so 1 is taken; B05.51's one H row is conditional and is counted.
- **Block size** (the structure §7.5 (2)): every batch gets an ED block of its count plus two and an H block of its count plus five, in the order of the structure §2.1's table (within each lane for ED; one sequence for H) `[ASSUMPTION carried from the structure: the spare — basis: none measured; a batch that runs out stops and takes the next free id on main, it never borrows a sibling's]`. A batch's ED block is in its own lane (a two-lane SE+WR batch takes SE's); a batch that declares ED ids in another lane also gets a block there of that count plus two (B05: ED-SC).
- **If a reading differs on B00's base**, every range of that lane (or of H) shifts by the difference, with every size and order kept; B00's commit body writes both readings.
- **Hole-register and registry blocks live only in this table and B00's commit body**: `id_reservations.yaml` gains no `H` key (U3 §1 item 1; T-4) and, by the same precedent, no `NPC` key (it has no NPC lane at this read; two batches declare registry ids) `[ASSUMPTION: ladder step 4, T-4's precedent for H; `register.py::rule_R0` stays the one duplicate check for H, and the registry's own loader for NPC]`.
- **Unused ids** are named in the batch's expunge commit body and never re-used (§2).

| batch | lane | ED block (declared + spare) | H block (declared + spare) |
|---|---|---|---|
| B00-ids | IN | ED-IN-0363..0366 (2+2) | H-363..H-367 (0+5) |
| B01-laneA | IN | ED-IN-0367..0368 (0+2) | H-368..H-373 (1+5) |
| B02-tests | IN | ED-IN-0369..0370 (0+2) | H-374..H-378 (0+5) |
| B03-hygiene | IN | ED-IN-0371..0372 (0+2) | H-379..H-383 (0+5) |
| B03g-go-early-landings | GO | ED-GO-0003..0004 (0+2) | H-384..H-388 (0+5) |
| B03c-boot | IN | ED-IN-0373..0374 (0+2) | H-389..H-393 (0+5) |
| B16L-mb-words | MB | ED-MB-0082..0083 (0+2) | H-394..H-398 (0+5) |
| B03a-prose | IN | ED-IN-0375..0376 (0+2) | H-399..H-403 (0+5) |
| B13-pc-package | PC | ED-PC-0060..0061 (0+2) | H-404..H-408 (0+5) |
| B16M-mb-engine-words | MB | ED-MB-0084..0085 (0+2) | H-409..H-413 (0+5) |
| B04-capability-home | IN | ED-IN-0377..0378 (0+2) | H-414..H-419 (1+5) |
| B05-one-roll | IN | ED-IN-0379..0380 (0+2); ED-SC-0041..0044 (2+2) | H-420..H-439 (15+5) |
| B06-keyed-draw | IN | ED-IN-0381..0382 (0+2) | H-440..H-444 (0+5) |
| B07-task-draw | IN | ED-IN-0383..0384 (0+2) | H-445..H-450 (1+5) |
| B08-scene-order | IN | ED-IN-0385..0386 (0+2) | H-451..H-455 (0+5) |
| B09-memory | IN | ED-IN-0387..0388 (0+2) | H-456..H-463 (3+5) |
| B10-character | IN | ED-IN-0389..0390 (0+2) | H-464..H-486 (18+5) |
| BA1-cast-content | IN | ED-IN-0391..0392 (0+2) | H-487..H-491 (0+5) |
| B11-fi-readers | FI | ED-FI-0010..0011 (0+2) | H-492..H-498 (2+5) |
| B11F1-flow-se | SE | ED-SE-0057..0058 (0+2) | H-499..H-505 (2+5) |
| B11F2-flow-in | IN | ED-IN-0393..0394 (0+2) | H-506..H-522 (12+5) |
| B12a-world-motion-and-ground | SE+WR | ED-SE-0059..0060 (0+2) | H-523..H-540 (13+5) |
| B12b-weather-arcs-population | SE+WR | ED-SE-0061..0062 (0+2) | H-541..H-549 (4+5) |
| B12c-material-verbs-and-valley | SE+WR | ED-SE-0063..0064 (0+2) | H-550..H-566 (12+5) |
| B14-pc-outcome | PC | ED-PC-0062..0063 (0+2) | H-567..H-573 (2+5) |
| B15-pc-calibration | PC | ED-PC-0064..0065 (0+2) | H-574..H-579 (1+5) |
| B16-pc-round | PC | ED-PC-0066..0067 (0+2) | H-580..H-584 (0+5) |
| B17-mb-scale | MB | ED-MB-0086..0087 (0+2) | H-585..H-589 (0+5) |
| B18-pc-content | PC | ED-PC-0068..0069 (0+2) | H-590..H-594 (0+5) |
| B19a-mb-contact-instrument | MB | ED-MB-0088..0089 (0+2) | H-595..H-599 (0+5) |
| B19-mb-field-calibration | MB | ED-MB-0090..0092 (1+2) | H-600..H-604 (0+5) |
| B20-mb-orders | MB | ED-MB-0093..0094 (0+2) | H-605..H-609 (0+5) |
| B21-fa-governance | FA | ED-FA-0040..0041 (0+2) | H-610..H-619 (5+5) |
| B21b-fa-war | FA | ED-FA-0042..0043 (0+2) | H-620..H-627 (3+5) |
| B21c-fa-seats | FA | ED-FA-0044..0045 (0+2) | H-628..H-632 (0+5) |
| B21d-fa-arc | FA | ED-FA-0046..0047 (0+2) | H-633..H-641 (4+5) |
| B21s-strife-supply | IN | ED-IN-0395..0396 (0+2) | H-642..H-646 (0+5) |
| B22-mb-armies | MB | ED-MB-0095..0096 (0+2) | H-647..H-653 (2+5) |
| B23-land | FA | ED-FA-0048..0049 (0+2) | H-654..H-660 (2+5) |
| B24-sc-hearing | SC | ED-SC-0045..0047 (1+2) | H-661..H-675 (10+5) |
| B24a-sc-outside-the-room | SC | ED-SC-0048..0049 (0+2) | H-676..H-681 (1+5) |
| B25-fi-questioning | FI | ED-FI-0012..0013 (0+2) | H-682..H-686 (0+5) |
| B26-fi-inquiry | FI | ED-FI-0014..0015 (0+2) | H-687..H-693 (2+5) |
| B27-sc-proceedings | SC | ED-SC-0050..0051 (0+2) | H-694..H-701 (3+5) |
| B28-social-verbs | SC | ED-SC-0052..0053 (0+2) | H-702..H-723 (17+5) |
| B29-pc-custody | PC | ED-PC-0070..0071 (0+2) | H-724..H-728 (0+5) |
| B30-mb-nested | MB | ED-MB-0097..0098 (0+2) | H-729..H-733 (0+5) |
| B31-mb-loadout-economy | MB | ED-MB-0099..0100 (0+2) | H-734..H-738 (0+5) |
| B32-inst-kit | FA | ED-FA-0050..0051 (0+2) | H-739..H-745 (2+5) |
| B33-inst-economy-hands | FA | ED-FA-0052..0053 (0+2) | H-746..H-757 (7+5) |
| B34-go-surface | GO | ED-GO-0005..0006 (0+2) | H-758..H-763 (1+5) |
| B35-wr-thread | WR | ED-WR-0013..0014 (0+2) | H-764..H-770 (2+5) |
| B36-wr-story-instruments | WR | ED-WR-0015..0016 (0+2) | H-771..H-775 (0+5) |
| B37-happenings | IN | ED-IN-0397..0398 (0+2) | H-776..H-788 (8+5) |
| B37p-wr-kin-and-life | WR | ED-WR-0017..0018 (0+2) | H-789..H-795 (2+5) |
| B38-narrative-regimes | WR | ED-WR-0019..0021 (1+2) | H-796..H-827 (27+5) |
| B39-procgen-and-cases | WR | ED-WR-0022..0023 (0+2) | H-828..H-835 (3+5) |
| B40-inst-scenarios | FA | ED-FA-0054..0055 (0+2) | H-836..H-840 (0+5) |
| B41-go-port-gate | GO | ED-GO-0007..0009 (1+2) | H-841..H-845 (0+5) |
| B98-dials | IN | ED-IN-0399..0400 (0+2) | H-846..H-850 (0+5) |
| B99-nine-retake | IN | ED-IN-0401..0402 (0+2) | H-851..H-855 (0+5) |

**Registry ids** (`references/npc_registry.yaml`; no spare: each row is a named person whose count its source fixes): B33-inst-economy-hands **NPC-091** (B33.09, the court's holder); B39-procgen-and-cases **NPC-092..NPC-094** (B39.32, the three founders, `SYN_B` §2).

**`next_free` after B00, as this table leaves it:** MB 101, PC 72, FI 16, SC 54, FA 56, WR 24, IN 402, GO 10, SE 65; the hole register's next id H-855; the registry's NPC-095. B98's counts are not known until part 44 is written: it holds the spare block above, and A44's `IDS:` line, if larger, takes the ids that follow H-854 and ED-IN-0401 on `main` at B98's open.

---

## 13. Definitions coined here (CLAUDE.md §4)

Each is also stated where it is invoked (the batch block's lines, the item's fields, the coordinator's prompt).

- **batch**: one handle with one close; the items it holds are built one commit each and verified together once (RULED 2026-11-06).
- **item** (a **position** in the skill's word): one content-owner entry that lands as one commit, handle `<batch number>.<two digits>`.
- **`.99`**: a batch's last position, the one commit that re-pins what the batch moved and writes its readings (E-1).
- **wave**: a dependency level of the batch graph; **step**: one slot of the lane schedule, in which at most one batch per lane is open; **slack**: how many steps a batch can slip without lengthening the plan.
- **critical path**: the longest chain of batches through the graph, by steps (§8) or by estimated hours (§5).
- **re-pin**: re-recording a seeded golden or pin to a new value on purpose, said plainly in the commit (CLAUDE.md §7).
- **behaviour mover**: an item that changes what a seeded run does, so content hashes move; **encoding mover**: an item that changes only how a hashed record is encoded (a field or class added, removed or renamed), so hashes move while behaviour does not (D-04).
- **conjunct**: one of the separately read conditions a requirement row is the conjunction of (`R-04.c5`), with its own `reading:` record (`IS-A-01`).
- **reading**: an instrument's quoted output on a named tree (`reading @<sha>`); never a count kept in a pointer index.
- **held**: carried with no work until a named trigger fires; **blocked**: written in full but waiting on something the plan does not supply, with its owner named.
- **setting at control**: a switch, gain or roster shipped at the value that reproduces the previous behaviour, set later by its own batch or by B98 (D-22).
- **`EXPECTED RED UNTIL`**: the item handle that turns a knowingly red test green (E-1, E-9).
- **`STOPS IF`**: the tree condition under which an item stops instead of building.
- **hot file**: a file twenty or more proposals edit, under §7 point 3's rule.
- **permanent surface**: the files every batch reads or appends to and none owns (§7 point 6); it links no two batches.
- **coordinator**: the one session that opens a step's sessions, merges their PRs in order and bases the next step (§7 point 8).
- **lap**, **round**, **exchange**, **riposte**: §4 (the glossary's rows own them).

---

## 14. The index (batch handle → file)

**The current file names, before the orchestrator's one renumbering of the `_cont` files** (the structure §4.1); the renumbering script rewrites this table, and it is final only after it runs. Generated by a scratch script from each part's `## Batch` headings and `### <handle>` item headings. A batch whose items run across several files lists them in reading order.

| batch | file(s) under `master/workplan_v12/` |
|---|---|
| B00-ids, B01-laneA | `workplan_v12_part3.md` |
| B02-tests | `workplan_v12_part3.md`, `_part3_cont.md` |
| B03-hygiene | `workplan_v12_part4.md`, `_part4_cont.md`, `_part5.md`, `_part5_cont.md` |
| B03g-go-early-landings, B03c-boot, B16L-mb-words | `workplan_v12_part6.md` |
| B03a-prose, B13-pc-package, B16M-mb-engine-words | `workplan_v12_part6_cont.md` |
| B04-capability-home | `workplan_v12_part7.md` |
| B05-one-roll | `workplan_v12_part8.md`, `_part8_cont.md`, `_part9.md` |
| B06-keyed-draw | `workplan_v12_part10.md` |
| B14-pc-outcome | `workplan_v12_part10_cont.md` |
| B07-task-draw | `workplan_v12_part10_cont2.md` |
| B17-mb-scale | `workplan_v12_part11.md` |
| B09-memory | `workplan_v12_part11_cont.md` |
| B10-character | `workplan_v12_part12.md`, `_part12_cont.md`, `_part13.md`, `_part13_cont.md` |
| B21-fa-governance | `workplan_v12_part14.md`, `_part14_cont.md`, `_part15.md`, `_part15_cont.md` |
| B11-fi-readers | `workplan_v12_part16.md`, `_part16_cont.md`, `_part17.md`, `_part17_cont.md` |
| B15-pc-calibration | `workplan_v12_part18.md` |
| BA1-cast-content | `workplan_v12_part18_cont.md` |
| B12a-world-motion-and-ground | `workplan_v12_part19.md`, `_part20.md` |
| B21b-fa-war | `workplan_v12_part21.md`, `_part21_cont.md` |
| B24-sc-hearing | `workplan_v12_part22.md`, `_part22_cont.md` |
| B16-pc-round, B08-scene-order | `workplan_v12_part23.md` |
| B12b-weather-arcs-population | `workplan_v12_part24.md`, `_part24_cont.md` |
| B19a-mb-contact-instrument, B29-pc-custody | `workplan_v12_part24_cont.md` |
| B21c-fa-seats | `workplan_v12_part25.md` |
| B34-go-surface | `workplan_v12_part25_cont.md` |
| B19-mb-field-calibration | `workplan_v12_part26.md`, `_part26_cont.md`, `_part27.md`, `_part27_cont.md` |
| B12c-material-verbs-and-valley | `workplan_v12_part28.md`, `_part28_cont.md` |
| B24a-sc-outside-the-room | `workplan_v12_part28_cont.md` |
| B18-pc-content | `workplan_v12_part28_cont2.md` |
| B21d-fa-arc | `workplan_v12_part29.md` |
| B41-go-port-gate | `workplan_v12_part29.md`, `_part29_cont.md` |
| B11F1-flow-se | `workplan_v12_part29_cont.md` |
| B20-mb-orders | `workplan_v12_part30.md` |
| B25-fi-questioning | `workplan_v12_part30_cont.md` |
| B27-sc-proceedings | `workplan_v12_part31.md`, `_part31_cont.md` |
| B37-happenings | `workplan_v12_part32.md` |
| B11F2-flow-in | `workplan_v12_part32_cont.md` |
| B22-mb-armies | `workplan_v12_part33.md`, `_part33_cont.md` |
| B26-fi-inquiry | `workplan_v12_part33_cont.md` |
| B32-inst-kit | `workplan_v12_part34.md`, `_part34_cont.md` |
| B37p-wr-kin-and-life | `workplan_v12_part34_cont.md` |
| B28-social-verbs | `workplan_v12_part35.md`, `_part35_cont.md` |
| B21s-strife-supply | `workplan_v12_part35_cont.md` |
| B35-wr-thread | `workplan_v12_part36.md`, `_part36_cont.md` |
| B23-land | `workplan_v12_part37.md` |
| B30-mb-nested | `workplan_v12_part37_cont.md` |
| B33-inst-economy-hands | `workplan_v12_part38.md`, `_part38_cont.md` |
| B36-wr-story-instruments | `workplan_v12_part39.md` |
| B31-mb-loadout-economy | `workplan_v12_part39_cont.md` |
| B38-narrative-regimes | `workplan_v12_part40.md`, `_part40_cont.md`, `_part41.md`, `_part41_cont.md` |
| B39-procgen-and-cases | `workplan_v12_part42.md`, `_part42_cont.md` |
| B40-inst-scenarios | `workplan_v12_part43.md`, `_part43_cont.md` |
| B98-dials, B99-nine-retake | `workplan_v12_part44.md`, `_part44_cont.md`, `_part44_cont2.md` (B98); `_part44_cont3.md` (B99) |

The file order is reading order, which is execution order only up to the schedule: where a file holds batches of different steps (part 23: B16 at S13 and B08 at S13; part 24's continuation: B19a and B29 at S14), the step table of §8 governs when each opens.
