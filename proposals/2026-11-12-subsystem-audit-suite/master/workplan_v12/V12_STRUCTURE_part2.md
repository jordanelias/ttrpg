# Workplan v12 — the structure, part 2: the part plan, the author assignments, the rules every author follows, the worked forms

## Status: WORK ORDER (part 2 of `master/workplan_v12/V12_STRUCTURE.md`; resolves nothing at runtime; deleted when v12 is adopted)

Short names, words and decision ids (`D-nn`) are part 1's. This part is what an author lane is handed with its row of §4.2.

---

## 4. The part plan

### 4.1 Files, and how big v12 is

v12 is drafted as `master/workplan_v12/workplan_v12.md` (part 1, the head) and `master/workplan_v12/workplan_v12_partN.md`, N from 2, in reading order, which is execution order (CLAUDE.md §4: sequential parts). Adoption renames them `workplans/valoria_master_workplan_v12.md` and `_partN.md` (§8).

**Size `[estimate]`.** The 300 proposals are 53,248 lines and 4.6 MB; about 45 % of a proposal is its executable part (resolution, exact edits, gate, falsifier, cost: three files sampled by their headings, `03_PC_weapon_form_at_round_start`, `07_SE_kernel_repairs`, `16_PESSIMIST_FA_C_under_the_seat`). The estimate per batch is `0.45 × its members' bytes + 4 KB per instruction item + 4 KB per intake entry + 4 KB for the batch block`, which sums to about 3.5 MB of body: **44 parts** (two head parts and 42 body parts, the last written after the others return). No intake carry-forward block was measured; a batch of intake entries may run long.

**The cap on a part is 900 lines and 120 KB, whichever comes first** (the suite's instruction files run to 2,000 characters a line, so the line count alone caps nothing). A batch estimated above the cap is written by two authors, split at the item named in §4.2. **An author whose text passes the cap stops at an item boundary and writes the rest to a second file named for its part with the suffix `_cont`** (`workplan_v12_part21_cont.md`); the orchestrator renumbers every file once, by script, after all authors return. For that reason **no part cites another part by number**: a part cites a batch or an item by handle, and only the head's index (§7.1) maps a handle to a file, written last.

### 4.2 Parts and author assignments

One Opus lane per body part (`A03` writes part 3, and so on); `H1` and `H2` write the head parts after the body parts return (§7), and `A44` writes the last part after H2's table of settings exists (D-22); `MF` writes the master findings (§9). **41 author lanes in the first fan is the count because each part is one lane's output limit, not because the subject divides 41 ways**: N−1 lanes would leave one part unwritten, and none reads another's part. Fire `A03` alone, await its first token, then fan the rest (CLAUDE.md §10 point 3); every lane is handed this structure file's three parts as a shared prefix, then its row.

"U3 item n" is U3 §1's numbered paragraph with §1.2's row for the same batch. Every author also reads, for each member, U3 §3.1's node row, §4.1's rows that split it, §5.1's rows for its files, §6.1 to §6.3's rows that name it, and `unified/U4_DOCUMENT_STATUS.md` §3.4's row where the member is INCOMPLETE (§5.7).

| part | lane | batches (an item range where a batch is split) | sources beyond the member proposals | est. KB |
|---|---|---|---|---|
| 1 | H1 | the head (§7.1) | this file; `STAGES.md`; the intake `:77-100` (22 head rules); the returned parts | — |
| 2 | H2 | the tables (§7.2 to §7.9) | U3 §1.1, §1.3, §1.4, §5, §6; `unified/U3_LAYER1_AMENDMENTS.md`; the intake's held headings; the returned parts (by script) | — |
| 3 | A03 | B00, B01, B02 | U3 items 1–3; IS-A §0–§11 (`IS-A-01` to `-07`, `-12`; the conjunct tables of `IS_A_NINE.md` §2–§10, copied whole into `IS-A-02`); CIP part 2 `CI-11`; `IS-B2-CORE-07`; the intake `:102`, `:106`; `unified/U3_CONFLICT_LEDGER.md` C3-A1, C3-A2, T-2, T-4 | 114 |
| 4 | A04 | B03, first half: U3 item 4 through `06_FA_hygiene`, with `CI-10`, `CI-08`, `CI-03`, `IS-B3-SE-04`, `CI-04`, `CI-05` | CIP §2–§3, `CI-03` to `CI-05`, `CI-08`, `CI-10`, part 2 §4 (the `FORK:` rows) | 96 |
| 5 | A05 | B03, second half (handles from `B03.51`): `U5a_CORE_owed_edits`, `CI-06`, `09_WR_threadwork_module` edit 3, `IS-B2-CORE-06`, the intake `:112`, `:227`, the cite fix, H-137, H-130, H-139; the boundary row | CIP part 2 `CI-06`; `master/eval/E6.md` block 5 (`:189`); `master/V11_EVALUATION.md` §6 | 96 |
| 6 | A06 | B03g, B03c, B16L, B03a, B13, B16M | `IS-B3-GO-06`; the intake `:537`; CIP `CI-01`, `CI-02`, `CI-07`, `CI-09`; the lexicon §4; `unified/MB_LEXICON.md` (the rows the renames cite) | 88 |
| 7 | A07 | B04 | U3 item 5; `unified/U1_CAPABILITY_AUTHORING_ARCHITECTURE.md` (§2, §2a, batch U1-A); PCR `:214-228` (PCR-4, D-05); `IS-B2-CHAR-05`; `IS-A-11` stage 1 | 78 |
| 8 | A08 | B05, first half: U3 item 6 through `13_SC_calibration`'s green read (its step 5) | `unified/U3_CONFLICT_LEDGER.md` C3-D2, C3-L1, C3-A3, C3-V1, C3-N6 | 60 |
| 9 | A09 | B05, second half (from `B05.51`): from `05_SC_opposed_obstacle_parity` to the R-09 row; H-199; the boundary row | the intake `:422`; `IS-B2-CHAR-06` | 60 |
| 10 | A10 | B06, B14, B07 | U3 items 7, 14, 8; `IS-PC-04`; `IS-A-10`; the intake `:489`, and `:544`'s GO-12 for its B06 half | 111 |
| 11 | A11 | B17, B09 | U3 items 17, 10; the intake `:140`; `IS-MB-05` | 95 |
| 12 | A12 | B10, first half: U3 item 11 through `02_CHAR_what_an_act_risks`, with `IS-A-05` part 2 | `IS_A_NINE_part2.md:137-150` | 84 |
| 13 | A13 | B10, second half (from `B10.51`): from `02_CHAR_voices_and_the_room`; `IS-B2-CHAR-02`, `IS-B2-CHAR-07`; the intake `:146`; the boundary row | `IS_B2_SC_FI_CORE_CHAR_part2.md:125-185` | 84 |
| 14 | A14 | B21, first half: U3 item 21 through `06_FA_decree_binds` edit 3 | `unified/U3_CONFLICT_LEDGER.md` C3-D5, C3-K9 | 64 |
| 15 | A15 | B21, second half (from `B21.51`): from `16_PESSIMIST_FA_A`; `IS-B3-FA-05`, `-06`, `-07`, `-01`; the intake `:168`, `:231`; the boundary row | `IS_B3_FA_SE_WR_GO.md:95-170` | 64 |
| 16 | A16 | B11, first half: the design items, the CR-29 group, `IS-B2-CORE-01` with `IS-B3-GO-01`, `IS-B2-CORE-02`, then U3 item 12 through `08_FI_06` | `IS_B2_SC_FI_CORE_CHAR.md:250-299` and `_part2.md:55-80`; `IS-B3-SE-06`; the intake `:17`, `:163`, `:464` | 73 |
| 17 | A17 | B11, second half (from `B11.51`): from `16_PESSIMIST_FI_A`; `IS-B2-FI-03`, `-04`, `-06`, `-01`, `IS-B2-CHAR-01`, `IS-B2-CORE-03`; the rest of the intake's B11 entries; the boundary row | the same | 73 |
| 18 | A18 | B15, BA1 | U3 item 15; PCR `:106-156` (PCR-1); `IS-PC-05`; the intake `:494`; `IS-A-11`, `IS-B2-CHAR-03`, `-06`, `-07` | 77 |
| 19 | A19 | B12a, first half: `IS-B3-SE-03`; U3 item 13 steps 1–5 and their intake entries | the intake `:172`, `:310`, `:352` (placed by §5.6) | 76 |
| 20 | A20 | B12a, second half (from `B12a.51`): steps 6–10, the `lattice_coupling` flip, H-138, their intake entries; the boundary row | the same; `master/eval/E6.md:151` | 76 |
| 21 | A21 | B21b | the intake `:237`, `:177`, §3's row | 112 |
| 22 | A22 | B24 | U3 item 24; `IS_B2_SC_FI_CORE_CHAR.md:132-205`; the intake `:181`, `:426` | 110 |
| 23 | A23 | B16, B08 | U3 items 16, 9; PCR `:158-212`; `IS-PC-01`; the intake `:129` | 71 |
| 24 | A24 | B12b, B19a, B29 | U3 item 13 steps 11–19; MBA `:24-70` (MBA-01 to MBA-03) and the design sections they cite; U3 item 29; the intake `:193` | 78 |
| 25 | A25 | B21c, B34 | the intake `:266`; U3 item 34; `IS-B3-FA-02`, `IS-B3-GO-02`, `-03`, `-07`; `IS-DICE-01`; `IS-PC-01` step 6; `IS-MB-01` step 4 | 100 |
| 26 | A26 | B19, first half: U3 item 19 through `04_MB_cell_hierarchy_as_data` with `26_MASS_BATTLE_cell_scale_and_time` (the T-rows, 27A, 27C-1, the stamina steps, `04_MB_cr12_linear_law` step 1, MBA-04 with ED-1043, ED-MB-0045, L1-6) | MBA §7.1 (MBA-04), §8; the intake `:515-521` | 62 |
| 27 | A27 | B19, second half (from `B19.51`): MBA-05 to the last read; the boundary row | MBA §7.1 (MBA-05, -06, -08) | 62 |
| 28 | A28 | B12c, B24a, B18 | U3 item 13 steps 20–25; `IS-B3-SE-01`, `-05`, `-06`; the intake `:431` and §3's row; U3 item 18 | 98 |
| 29 | A29 | B21d, B41, B11F1 | the intake `:276`, `:544`, `:185`, `:328`; U3 item 41; `IS-B3-GO-05`, `-06` | 72 |
| 30 | A30 | B20, B25 | U3 items 20, 25; `IS-MB-01`, `-03`, `-05`; `IS-B2-SC-07`; the intake `:282`, `:474` | 92 |
| 31 | A31 | B27 | U3 item 27; `IS-B2-SC-07`; the intake `:370`, `:445`, `:498` | 94 |
| 32 | A32 | B37, B11F2 | U3 item 37; the intake `:197` | 85 |
| 33 | A33 | B22, B26 | U3 items 22, 26; `IS-MB-02` (and `IS-A-09`'s two additions); the intake `:478` | 114 |
| 34 | A34 | B32, B37p | U3 item 32; the intake `:286`, `:363` | 110 |
| 35 | A35 | B28, B21s | U3 item 28; `IS-B2-SC-05`, `-06`, `IS-B2-CORE-05`; the intake `:441`, `:359`, `:189` | 75 |
| 36 | A36 | B35 | U3 item 35; `IS_B3_FA_SE_WR_GO_part2.md:53-111`; the intake `:376` | 105 |
| 37 | A37 | B23, B30 | U3 items 23, 30; `IS-B3-FA-04`; `IS-MB-04`, `IS-PC-02`; MBA-07; the intake `:290`, `:523` | 71 |
| 38 | A38 | B33 | U3 item 33; the intake `:333` | 106 |
| 39 | A39 | B36, B31 | U3 items 36, 31; MBA-09; the intake `:211` | 77 |
| 40 | A40 | B38, first half: U3 item 38 through `31_WR_A` | A-103 (the `30_WR_A` correction) | 90 |
| 41 | A41 | B38, second half (from `B38.51`): from `20_NARRATIVE_D`'s later commits; `IS-B3-GO-04`, `IS-B3-FA-03`, `IS-B3-SE-02`; the boundary row | `IS_B3_FA_SE_WR_GO.md:117-126`, `:224-233`; `_part2.md:187-196` | 90 |
| 42 | A42 | B39 | U3 item 39; the intake `:502` | 83 |
| 43 | A43 | B40 | U3 item 40 | 82 |
| 44 | A44 (second pass) | B98, B99 | H2's table of settings at control (§7.8) and, for each, its source's calibration target; `IS-A-13` | — |

The order of batches across parts 3 to 43 is a topological order of §2.1 (checked by hand against its `after` column). Where two authors share a batch, the first writes the batch block's head (§5.2) and the second the boundary row; the first states, as its part's last line, the handle of the last item it wrote.

---

## 5. Rules for every author lane

**5.1 What an author does.** It reads its row's sources in full (every member proposal, every instruction item, every intake entry with its carry-forward block at the lane-file line the entry cites) and writes one part. It decides nothing this file decides: a choice it cannot read off its sources goes into its receipt under `UNDECIDED:` with the two readings, and the text it writes takes the reading that changes less. It edits no file but its part. It writes the batch block's head and the first items before it finishes reading, and appends (CLAUDE.md §10).

**5.2 The batch block.** In this order, each a line or a small table:

```
## Batch <handle> · lane <LANE> · wave <Wn> · step <Sn> · HASH <EQUAL | MOVER, one re-pin>
INVOCATION: /methodology-execute Batch <handle>
IN-FLIGHT ROW: registers/handoffs/HANDOFF_<LANE>.md, Open table            (a two-lane batch: D-21)
GATE: Batch <handle>                                                       (one line per `after` batch of §2.1)
REQUIREMENT: <conjunct ids> → <expected reading>   |   none — <reason or ruling>
BATCH GATE: <the commands read once, on the closing tree, each with its expected reading>
RE-PIN: none | <what is re-recorded, in the last Item: commit, and the baseline it is read against>
IDS: ED-<LANE> <n>; H <n>                                                  (how many the batch's items write; B00 turns the counts into blocks)
DIALS AT CONTROL: none | <setting> = <control value>; set by <this batch's item | B98>; target: <the source's reading, or "none stated">   (D-22)
C(<handle>): <the reading list>
SERIAL EDGES: <within the batch: item → item, with the reason; with other batches: file, batches in order>
PARALLEL: <the batches of its step, and the files it shares with any of them>
COST: <the dominant class; the tier of producer and of each judgment node>
EST: <hours> [estimate]
| pos | item | source | state | hash | gates on |                          (the position table, one row per item, in landing order)
…the items, in full (§5.3)…
| STOP. Batch <handle> closes here |
```

`BATCH GATE` always includes `python -m engine.season.harness.register --check` and `--requirements` and `python tools/m1_acceptance.py --summary`'s verdict line (U3 §1, `IS-A-12`), the covering suites `python tools/tests_for_diff.py --base <batch-start-sha>` names, and the batch's own gate from U3 §1 and §1.3. `C(<handle>)` is derived from the items (the skill, "The context set"): the batch's own entries; every file in a WHERE; every instrument and registry a GATE or FALSIFIER reads; the batches its gates name; the permanent surface (CLAUDE.md, `CURRENT.md`, `HANDOFF.md`, the lane file, the plan's head parts, the skill and `methodology-close`). **A source proposal is not in `C` unless an item says it must be read whole**: the item copied what executes.

**5.3 The item.** One item is one commit (the skill, 0.1 step 3). Its handle is `<batch number>.<two-digit position>` (`B21.09`); that is what the `Item:` trailer, the in-flight row and every gate use. Source handles (`IS-B3-FA-07`, `CR-49`, `MBA-04`, a proposal's file name) go in the title and SOURCE.

```
### <handle> — <title in plain words> · <source handle> · <STATE> · HASH <EQUAL | MOVER(behaviour) | MOVER(encoding)>
- SOURCE: <file>:<section or lines>; rulings <A-n>; closes <finding, hole or v11 ids>.
- ADVANCES: <conjunct ids, or what else it serves>.
- INSTRUCTION: <the ordered edits, copied (§5.4)>.
- WHERE: `<path>` (<symbol or key>); … ; NEW `<path>`; DELETE `<path>`.
- TESTS: <each named test, the file it is in, written before or with which edit, and its reading before the edit>.
- FALSIFIER and CONTROL: <what would show the item wrong; the control arm that must not move>.
- GATE: <command> → <expected reading>; … (seeds; seasons, two at most).
- HASH MOVERS: none | <what moves, declared; re-pinned in the batch's last Item: commit>.
- DEPENDS ON: <each: EXISTS-IN-TREE `path::symbol` | V12 <item handle> | MISSING (<owner>)>.
- GLOSSARY: none | <the row edited in this commit; a new word's ordinary-English reading in one sentence>.
- NAMES: <old → new, for each identifier of §5.10 the copied text uses>            (omit if none)
- IDS: <the ED and H ids it writes, as "block slot k">                             (omit if none)
- COST and TIER: <class>; <producer tier, effort>; <reader or critic tier where it is a judgment node>.
- LANDS IT: the batch's `valoria-author` producer, `isolation: worktree`; one `Item: <handle>` commit, `[skip ci]` unless it is the batch's last.
```

STATE is one of `BUILD`, `DESIGN-FIRST` (D-18), `CONTENT` (D-19), `READING` (a reading quoted at the close: no code, no commit of its own, a line of the batch gate; it has a row in the position table and no item body), `POINTER` (no work: the id is closed by a named item, e.g. H-132 by B21's), `BLOCKED (<owner>: <what is missing>)`, `HELD (<trigger>)`. Cost classes: `edit`, `small build`, `build`, `wide mechanical`, `calibration`, `content`, `design`, `reading`. Tiers are CLAUDE.md §10's; the source's own tier is copied where it gives one.

**5.4 What is copied, and what is not.** The INSTRUCTION is complete enough to execute with the item and the tree alone. **Copied from the source, exactly:** the edit text, file by file and symbol by symbol; schemas, data rows and seed values; function signatures and pseudocode blocks; call sites; the order of commits; test names and what each asserts; gate commands and expected readings; the falsifier; declared movers; reverts. Where the source cites another section for data the edit needs (a table of levels, a closed set, a list of checks), that data is copied too. **Not copied:** the finding and its evidence, the problem statement, the NERS reading, the earning argument, `Reconciled:` and `Folded:` history, citations of audits, anything a ruling or a later line of the same file withdrew. **Added:** only the plan's fields. A line number into a file edited at or before B03a is dropped and the symbol kept (CIP part 2 §5 note 2). Nothing is paraphrased: where the source's sentence is the instruction, it is the sentence.

**5.5 One source, several items.** A source that orders its edits as separate commits becomes one item per commit, in its order. A proposal U3 splits across batches (§4.1 there) becomes an item in each batch for the part that lands there, and each says where the rest is. Two sources U3 lands "with" each other in one commit are one item naming both. A source superseded in whole is not an item; where a superseded file is to be marked, the marking is a step of the item that supersedes it.

**5.6 Intake entries.** `settled:` governs, then the heading the entry sits under, then its `lane's target` (D-14). An entry is placed **immediately before the first item of its batch whose source names its id** (grep the id in the members and instruction items), otherwise where its own text says ("first", "last", "after X"), otherwise at the batch's tail in the intake's order; the author writes which rule placed it. For B12 the same rule chooses among B12a, B12b and B12c: the part that holds the naming item (CR-49 goes with `14_VERBS_MATERIAL_B` in B12c); an entry no member names goes to B12a's head if the intake says "head", otherwise to B12c's tail. An entry's INSTRUCTION is its carry-forward block's WHAT, REMAINING UNBUILT, EXIT and FALSIFIER and HASH lines, copied; its LANDED ALREADY and RE-BASE lines become DEPENDS ON marks, each re-checked at this tree by opening the symbol. A merged entry (the intake §1) is one item with every id. A MISSING-DEP entry is `BLOCKED` with the owner the entry names. A held entry is not an item (§7.9). Where an instruction item restates a v11 position's whole body, the instruction item is the item and the entry is its `closes` (the evaluation's rule 2). Drop CR-94 from `IS-B2-FI-02`'s B11 list (`master/V11_EVALUATION.md` §7 item 5), and keep one owner of `world_q.hearing` (the same item).

**5.7 INCOMPLETE proposals** (`unified/U4_DOCUMENT_STATUS.md` §3.4: 82 files, by code). The author writes the complete parts as items and treats the rest by code:

| code | what the author writes |
|---|---|
| DEP-v11 | the named v11 position is an intake entry: its item is placed before the dependent item and the dependent's DEPENDS ON names it as `V12 <handle>`. If the id is not in the intake it was retired: the dependent edit names the superseding item from `master/V11_EVALUATION_part2.md`'s ledger, or is dropped with that ledger line cited |
| DEP-NOCARRIER | the carrier: `_eff_dispatch` is `IS-B3-FA-05` (B21); the writer of `Person.coherence` is `IS-B3-WR-01` with CP-T07-02 (B35); `besiege` is `IS-MB-02` (B22); the Court Parliament's working state is CR-38 with H-90 (B21c; A-76's stand-in ships in B23); a goal row's `axis:` is content of B38 (D-19). Any other symbol with no carrier makes the dependent part `BLOCKED (v12: a carrier is owed)` and goes in the receipt |
| DESIGN | a `DESIGN-FIRST` item before the build item (D-18), unless an instruction item already settles it (the lanes IS-B1 to IS-B3 were written to: grep the proposal's file name in `master/instructions/`) |
| CONTENT | a `CONTENT` drafting item (D-19); for the cast's values, a row of `IS-A-11`'s tables |
| SITE | the item's first INSTRUCTION step is "open `<site>` and record what is found in the commit body", then the edit in both branches the source gives |

**5.8 Gates.** Every GATE is a command and the reading expected of it; "the file exists" is a gate only for a design item. A test file a gate names that is not in the tree (U3 §6.1) is written in the item that needs it, before the edit, and its reading before the edit is stated (red where the claim is a defect; green at control and red with the edit reverted where it is new behaviour). A scratch probe a source cites (U3 §6.2) is restated as a named test or a reading of an existing instrument, written first. A gate arm that reads the effect of a later item is moved to that item's GATE, or to the batch gate, and says so. **No gate runs past two seasons** (D-17): a source's `aperture 4 0` or four-season reading is written at two, with "(four seasons in the source; A-114)". A gate that must see a fight between persons names seed 2; one that must see a fought field names seed 2 at one season or seed 0 at three, which is over the cap, so seed 2 (CIP part 2 §5 note 3). Every seeded command is run with `PYTHONHASHSEED=0`. Nothing is asserted certain that is drawn: a gate over a draw states a share over named seeds with `assert checked >= N`.

**5.9 Hash.** Each item says EQUAL, MOVER(behaviour) or MOVER(encoding) (D-04). A batch re-pins once, in its last `Item:` commit, and the commit says "re-pin" (CLAUDE.md §7). Hash-EQUAL items of a mover batch come first where the source's order allows it. A before-reading is the previous close's after-reading, quoted `reading @<sha>`, never re-taken (the skill, Baselines). In a step with two mover batches the later in §2.1's order rebases on the earlier's merge and re-pins once (§7.4).

**5.10 Names that change before an item lands.** Sources were written against today's identifiers. An item in a batch after the rename keeps the source's text and adds `NAMES:` for each identifier it uses:

| lands in | old → new |
|---|---|
| B03c (`CI-07`) | `harness/populated.py::build_realm` and what it reaches → `boot/realm.py`; `harness/probes.py::chooser` → `boot/chooser.py`; by symbol |
| B16L (L1) | `subformations` → `units`; `Subformation` → `UnitRow`; Record kind `order_of_battle` → `standing_order`; the army row and payload key `stance` → `posture`; `STANCES` → `POSTURES` |
| B16M (L2) | `hierarchy.units.Unit` → `Army`; `Subunit` → `Unit`; `subunits` → `units`; `SUBUNIT_*` → `UNIT_*`; `.broken` → `.disordered`; `max_turns` → `max_ticks` |
| B13 (`CI-09`) | flat `import core` and kin → `from modules.combat import …`; `pc_engine.load()` gone (D-09) |
| B04 (`PCR-4`) | `Claim.round` → `Claim.lap`; `SeasonDriver.round` → `.lap`; `scenes_per_round` → `scenes_per_lap` |
| B16 (`PCR-3`) | `max_bouts` → `max_rounds`; `turn_start` → `round_start`; `engagement_end` → `round_end`; `CombatTurnView` → `CombatRoundView`; `TURN_CHOICES` → `ROUND_CHOICES` |
| B15 (`IS-PC-05`) | the combat attribute `faculty` → the skill score read through the skill table |

**5.11 Glossary.** An item that introduces, renames or retires a term edits its row of `unified/U1_GLOSSARY.md` in the same commit and says so; a new word carries its ordinary-English reading in one sentence; once the code defines the word, the row's definition becomes a pointer to the owner and keeps its rejected-synonym column (`STAGES.md`, "The glossary always matches"). The author writes in the glossary's words; where copied source text uses a word a later ruling retired (A-98, A-99, A-101), the copied text is corrected and the correction said.

**5.12 What the close records.** Each batch block ends its BATCH GATE with: "the close's commit body records `register --requirements` (nine lines), `m1_acceptance --summary`'s verdict line, the named conjuncts' readings with their tree, the `BUILT OUT`, `ENGINES` and `NULL SCENES` lines before (`reading @<sha>`) and after, and the batch's measured wall time; the last `Item:` commit writes the conjuncts' `reading:` records; `status:` is not edited" (`IS-A-12`).

**5.13 What an author does not write.** No count in a place a pointer index would hold; no new guard, scorer or register (CLAUDE.md §0.1 pt 5); no `.md` under `systems/`; no engine version; no item for a retired v11 position; no "TBD". An item it cannot complete is `BLOCKED` with an owner, and says what is missing.

**5.14 The receipt** (returned, not the part's text): the file written, its lines and bytes; the batches and the count of items by STATE; the `UNDECIDED:` list; the `BLOCKED` items with owners; each dependency marked MISSING; each source it could not open or read whole; the declared `IDS:` counts; the `DIALS AT CONTROL` lines.

---

## 6. The worked forms

### 6.1 A worked example: `16_PESSIMIST_FA_C_under_the_seat.md` in B21 (three items, because the source orders three commits)

The position numbers are examples; A14 assigns the real ones. Everything under INSTRUCTION is the source's text (`:66-103`), unparaphrased.

```
### B21.09 — one predicate says whom a seat may order · 16_PESSIMIST_FA_C edit 1 · BUILD · HASH EQUAL
- SOURCE: proposals/16_PESSIMIST_FA_C_under_the_seat.md "The resolution, decided" and "Exact edits" 1, "Gate"; rulings A-22; closes F-PES-FA-03.
- ADVANCES: R-04.a (`issue`, `dispatch`) through B21.10 and B21.11; nothing by itself (a Query with no caller).
- INSTRUCTION:
  1. `engine/season/queries/world_q.py`, beside `establishment_of`, a read-only Query:
         commands(w, actor, via, person_id) -> bool
             seat = w.offices[via]
             person_id in establishment_of(w, via)                          # (i) the sworn: a live `oblige` to this seat
          or any(may_revoke(w, actor, via, w.offices[t.object])             # (ii) the holder of a seat this seat may revoke
                 for t in w.seat_holds(person_id) if t.object != via)
          or (not w.seat_holds(person_id)                                   # (iii) an unseated person in its land
              and purview_reaches(w, seat, place_of(w, person_id)))
     `may_revoke` joins the existing `from ..state.gate import …` line. The docstring defines the word: "the command basis: whom a seat may order (A-22)".
  2. This is the one body: `14_VERBS_BINDING_D_orders.md` commit D2's second `commands` in `state/gate.py` is not written; BIND_D's edits 3–5 compose on this one.
- WHERE: `engine/season/queries/world_q.py` (`commands`; the gate import line); NEW `engine/season/tests/test_command_basis.py`.
- TESTS: in the new file, written before the edit and read red (no `commands`): `test_sworn_man_is_commanded_wherever_he_lives`, `test_seated_resident_not_sworn_not_revocable_is_not_commanded`, `test_unseated_resident_is_commanded_by_the_land_lord`, `test_holder_of_a_revocable_seat_is_commanded`; and `test_dispatch_to_a_stranger_refused`, which stays red until B21.11 (the source lands all five with edit 1).
- FALSIFIER and CONTROL: a seated resident who is neither sworn nor revocable reads commanded. Control: the realm content hash at seeds 0 to 2 equal to the previous item's reading (nothing calls the Query yet).
- GATE: `python -m pytest engine/season/tests/test_command_basis.py -q` → four pass, `test_dispatch_to_a_stranger_refused` fails (expected until B21.11).
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `state/gate.py::may_revoke`, `::purview_reaches`, `queries/world_q.py::establishment_of`, `::place_of`, `World.seat_holds`; V12 the items of `14_VERBS_BINDING_C` at control and `06_FA_decree_binds` edits 1–2 (earlier in B21).
- GLOSSARY: row *command basis* becomes a pointer to `world_q.commands`; "under the seat" stays refused.
- COST and TIER: small build; `sonnet`, high.
- LANDS IT: B21's producer; `Item: B21.09`, `[skip ci]`.

### B21.10 — `issue` asks the command basis · 16_PESSIMIST_FA_C edit 2 · BUILD · HASH MOVER(behaviour)
- SOURCE: the same file, "Exact edits" 2, "Gate" G1; A-22; narrows ED-IN-0256 (4) behind its revert.
- ADVANCES: R-04.a (`issue`).
- INSTRUCTION: `engine/season/data/requires.py`: the `basis` form gains the value `command`, dispatched to `world_q.commands` exactly as `purview` is dispatched to `purview_reaches` (a value of an existing form, not a new stem). `engine/season/verb_table.yaml`, row `issue`: its `authority` conjunct `basis: purview` → `basis: command` (revert: `basis: purview`). Rung referents keep `purview` (`requisition`, `seize`). An `issue` whose addressee is not commanded is refused at the fold on that conjunct; formation does not offer it, and the same matter toward a superior is formed as `petition` through `14_VERBS_BINDING_D_orders.md` edit 6's fan (later in B21).
- WHERE: `engine/season/data/requires.py` (the `basis` dispatch); `engine/season/verb_table.yaml` (`issue`).
- TESTS: none new.
- FALSIFIER and CONTROL: the three Varfell council holders still refused after `16_PESSIMIST_FA_A` edit 2 (then the council seats' rungs are not within the ducal purview and the anchor is the defect). Control: the King's unseated residents are unchanged.
- GATE: on `build_realm(0)`: the Duke of Varfell's admitted addressees include his sworn men and the holders of Varfell seats he may revoke, wherever they live; the Restoration leader's are 0 until someone is sworn to his seat. The arm naming the three council holders is read at the item that lands `16_PESSIMIST_FA_A` edit 2 (moved there, §5.8).
- HASH MOVERS: every seeded world with a writ: `issue`'s admitted set widens for the sworn and the revocable and narrows for seated residents of other chains. Declared; B21's one re-pin.
- DEPENDS ON: V12 B21.09.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, high; the A-22 reading of the petition routing `opus`.
- LANDS IT: B21's producer; `Item: B21.10`, `[skip ci]`.

### B21.11 — `dispatch` asks the same basis · 16_PESSIMIST_FA_C edit 3 · BUILD · HASH MOVER(behaviour)
- SOURCE: the same file, "Exact edits" 3, "Gate" G2, G3.
- ADVANCES: R-04.a (`dispatch`).
- INSTRUCTION: `engine/season/loop/predicates.py::_req_dispatch`: after "the named person exists", refuse (`_refuse("not commanded", …)`) unless `world_q.commands(w, a.actor, a.via, subject)`.
- WHERE: `engine/season/loop/predicates.py` (`_req_dispatch`).
- TESTS: `test_dispatch_to_a_stranger_refused` turns green.
- FALSIFIER and CONTROL: an order to a stranger still reads `order.given`. Control: an unseated resident of T1 and a man sworn to the Marshal's seat are still ordered.
- GATE: `python -m pytest engine/season/tests/test_command_basis.py -q` → five pass. On `build_realm(0)`: the Royal Marshal's `dispatch` of the Katepano of Altonia is refused. Over seeds 0 to 2, two seasons: executed `dispatch` before (`reading @<sha>`) and after, and the count refused by the new clause, quoted; a refused share above half is a finding about formation, not a reason to drop the clause.
- HASH MOVERS: every seeded world with an order. Declared; B21's one re-pin.
- DEPENDS ON: V12 B21.09.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, high.
- LANDS IT: B21's producer; `Item: B21.11`, `[skip ci]`.
```

### 6.2 A worked batch skeleton: `B19a-mb-contact-instrument`

```
## Batch B19a-mb-contact-instrument · lane MB · wave W14 · step S14 · HASH EQUAL
INVOCATION: /methodology-execute Batch B19a-mb-contact-instrument
IN-FLIGHT ROW: registers/handoffs/HANDOFF_MB.md, Open table
GATE: Batch B00-ids
GATE: Batch B01-laneA
GATE: Batch B02-tests
GATE: Batch B16M-mb-engine-words
GATE: Batch B14-pc-outcome
GATE: Batch B15-pc-calibration
GATE: Batch B16-pc-round
GATE: Batch B17-mb-scale
REQUIREMENT: none — the measured table B19's contact draw reads (A-100); nothing in a field reads it yet
BATCH GATE: `python tools/calibrate_mb_contact.py --trust` → seven `ok` lines; `--spot 20` → twenty `inside` lines;
  `python tools/export_mb_contact.py --check` → exit 0; `python tools/export_troops.py --check` → exit 0;
  `python tools/ci_golden_modes_check.py` → every digest equal to B17's close (`reading @<sha>`);
  `python -m engine.season.harness.register --check`, `--requirements`; `python tools/m1_acceptance.py --summary`;
  the suites `python tools/tests_for_diff.py --base <batch-start-sha>` names; the close's record (§5.12).
RE-PIN: none
IDS: ED-MB 0; H 0
DIALS AT CONTROL: none (the `contact`, `missile` and matchup values ship `status: seed` and are read by MBA-08 in B19, a batch's own calibration)
C(B19a): this batch's entries; the plan's head parts; `references/troops.yaml`; `tools/export_troops.py`; `engine/engine_params/troops.json`;
  `modules/mass_battle/troop_types/table.py`; `tests/valoria/test_export_troops.py`; `references/ci_checks_registry.yaml`; `tools/valoria_local.py`;
  read only: `modules/combat/fight.py` (`fight_round`), `modules/combat/vocabulary.py` (`ROUND_ENDS`), `engine/engine_params/combat_engine_v1.json`,
  `systems/combat/combat_engine_v1/workbench/balance.py` (`winrate`), `tools/export_battle_orders.py` (the exporter pattern), `tools/ci_golden_modes_check.py`;
  the closing SHAs of B14, B15, B16, B17, B16M; the permanent surface.
SERIAL EDGES: B19a.01 → B19a.02 (the instrument's grid is read from the troop file's new columns) → B19a.03 (the exporter builds from the measured table).
  `modules/mass_battle/troop_types/table.py`: B17 → B19a → B19 → B31. `references/ci_checks_registry.yaml`, `tools/valoria_local.py`: B19a → B19.
PARALLEL: S14 with B12b (SE+WR), B21c (FA), B29 (PC), B34 (GO); no file shared (census rows above). PC review is a read of MBA-02's use of the duel, not a PC batch.
BACKGROUND RUN: B19a.02's first full run, sized on two small runs, launched at the batch's open after B19a.01 lands, read at B19a.02's gate; its wall time and worker count go in that commit body.
COST: small builds, one instrument run; `sonnet` high; a `--trust` failure is read by `opus` (is it the duel or the instrument).
EST: 6 h [estimate]

| pos | item | source | state | hash | gates on |
|---|---|---|---|---|---|
| B19a.01 | the troop file carries the contact's data | MBA-01 | BUILD | EQUAL | Batch B17, Batch B14 |
| B19a.02 | the calibration instrument, melee cells, and its first full run | MBA-02 stage 1 (loads the duel as D-09) | BUILD | EQUAL | B19a.01; Batch B15, Batch B16 |
| B19a.03 | the exporter, its blocking `--check`, the module's reader | MBA-03 | BUILD | EQUAL | B19a.02 |

…the three items in full, in the form of §5.3…

| STOP. Batch B19a-mb-contact-instrument closes here |
```
