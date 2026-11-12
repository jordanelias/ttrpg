# V12 intake: every carried v11 position and gap-register row, by lane and batch

## Status: WORK LEDGER (stage 5 of `STAGES.md`, settle-and-merge; the input stage 6 folds into workplan v12; reference, resolves nothing at runtime, CLAUDE.md §0.05; deleted when v12 is adopted)

**What this is.** The list of everything the evaluation settled as STILL-NEEDED or MISSING-DEP (lanes E1 to E8, after the settlement in `master/V11_EVALUATION_part2.md` and `master/GAP_REGISTER_EVALUATION_part2.md`), one entry per item. Items the lanes found under two ids are one entry with both ids. Each entry is placed in a lane (the nine-lane roster of `tools/ci_common.py`; the suite's `CHAR` tag is filed under IN, which owns the character files, `[ASSUMPTION: basis E8's 'CHAR lane (IN-owned file)']`) and in the U3 batch it joins (`unified/U3_DEPENDENCY_ORDER.md` §2.1), or in one of the nine new batches of §3. Each entry gives the lane rows it comes from (`E<k>:<line>`, the lane file's line) and where its carry-forward block is (the lane file's own line, also copied byte for byte into the evaluation parts), so stage 6 reopens the content-owner text without reopening v11.

**Counts.** 273 entries: 264 STILL-NEEDED, 9 MISSING-DEP, from 631 settled table rows (609 STILL-NEEDED and 22 MISSING-DEP). 22 entries are v12 head rules, not batch items; 54 are held (LEAVE: no work until the trigger the entry names fires; they are carried so nothing drops silently). By lane: IN 90, FA 53, WR 49, SE 24 (H-325's group filed SE), SC 21, GO 11, FI 10, PC 8, MB 7 (the generated body below is the count's source). A carried row of 'held' kind keeps its lane's 'held and leave' wording; nothing in it is work until its trigger fires.

**How to read an entry.** `ids · disposition · rows · carry-forward · lane's target · settled`. The *lane's target* is quoted from the lane file and may name a batch handle the lanes proposed before this reconciliation (B21b-fa-plan, B42-fa-arc, B11b-verbs-r05, B35a, B10b-loops, B03e-scale-cut, B21c-arc, B37p-wr-npc-life, `strife-supply`, F1 to F3): the heading the entry sits under governs (§3 maps every old name). *Settled* quotes the reason when this pass changed or re-cited a row.

## 1. Merged items (one item, several ids)

| item | ids | lane, batch | why one item |
|---|---|---|---|
| the record holds what changed (closure branch of `state/log.py`) | H-145, NM-W9 (b) | IN, B09-memory | E7's cross-lane note; `U5_FINDINGS_CLOSURE_U5a.md:72` leaves the branch to NM-W9 by name |
| `own_purview` through `purview_reaches` | H-101, CR-09 | FA, B21b | the register row is CR-09's residue (E7, E3 Block 17) |
| the event-kind reach channel and `chronicle`'s paired deletion | H-214, CR-29, H-224 (its window measurement rides CR-29's exit), ED-IN-0298, A2-43 | FI/IN, B11 (first item) | E3 Block 11; `08_FI_01_claim-sourced-referents` depends on CR-29; H-234 is SUPERSEDED by FI-02 edit 1, a row on CR-29's roster |
| declare the loops with sign and bound | H-25, H-106, CR-98 | IN, B11F2 | E6 Block 1; U5a gives both rows to CR-98 |
| cut the `scale:` column | H-89, CR-07, DEF-5 | IN, B03 tail, MISSING-DEP | IS-B2-CORE-06 BLOCKED: `off_npc_084`'s rung is content |
| delegation without a `hold` | H-108 (b), IN-48 | FA, B21b | `U5_FINDINGS_CLOSURE_U5d.md:77`: A-10 leaves IN-48 the owner |
| the `Person.coherence` writer | H-47, H-62, CP-T07-02 | WR, B35 (first card item) | U3 §6.3 names CP-T07-02 as the only carrier |
| `rank` reads one scale; its producer | H-181, CR-32 | FA, B21c | CR-32 is 'H-181's producer' (E3 Block 18) |
| the `succession` row | H-217, CR-35, SC-04's residue | FA, B21c | E3 Block 13 |
| hunger binds | H-11, H-125, CR-22 | SE, B12 | E3 Block 16 |
| Parliament as a constraint | H-90, CR-38 (with CR-35 to CR-37, IN-48) | FA, B21c | `U5_FINDINGS_CLOSURE_U5d.md:75` |
| a writer of person-predicate claims | H-222, A1-87 | SC, B27 | E3 Block 9 |
| the deed lie | H-198, M9, E4's §2 deed-lie row | IN (CHAR), held, MISSING-DEP | E7, E4 |
| a lie can be found in its trail | H-314, CP-T06-03, CP-T06-04 | FI, B11 | E8 CF-E8-4 |
| finding what is hidden (A-109) | H-325, H-326 (r) | SE+FI, design-first | A-109; E8 CF-E8-5 |
| the march cap and `guards` | IN-36, §1a-M1res, V9-14 (and G-19, TL-B5.2 after the flip) | FA, B21b | A-103: only the cap and `guards` ON survive |
| one ladder for the remove ordinal | H-199 | SC/IN, B05 or B10 (E3 Block 12) | an S defect; the re-read found it |

## 2. Batches the items join (U3's, unchanged)

The U3 batches keep U3's members, dependencies and waves. The intake adds items to them; the largest additions are B12 (21 entries: the SE card positions as the SE proposals amend them, CR-22, CR-40, CR-47, CR-49, IN-52), B03 (19: hygiene and early GO landings), B35 (15: the thread card in IS-B3-WR-01's order), B10 (14), B27 (13). Two placements this pass fixed that the lanes left open:

- **CR-47 and CR-49 join B12's head** (E2's placement). E4's `B11b-verbs-r05` is not needed: of v11's B10-18b, CR-46, CR-48, CR-50, CR-51 (a), CR-52, CR-53 and CR-54 are SUPERSEDED. `[ASSUMPTION: 14_VERBS_MATERIAL_B_stores.md:170's 'CR-49 after CR-48' is the v11 card's order only; if it is a data edge, B12 gains B21 (06_FA_decree_binds) in its after-list; checked: no cycle]`.
- **CR-51 (b), the arrest re-measure, joins B29-pc-custody's tail**: it reads `arrest.made` after custody lands (B29) and after B21, which B29 already follows; putting it in an FA batch would add a PC-to-FA edge and lengthen the chain.

## 3. New batches (each listed once; reconciled from the lanes' proposals)

| new batch | lane | after | before | members (ids) | lane proposals it merges or replaces |
|---|---|---|---|---|---|
| B03d-gate-observation | IN | B03 | B11 | H-130, H-137, H-138, H-139 (hash EQUAL; E6 notes three may be cut as unreached under CLAUDE.md §0.1 pt 5) | E6 `B03d-gate-observation` (H-135 joins B09-memory, as E6 placed it) |
| B11F1-flow-se | SE | B12 | B11F2, B38, B39 | CR-106, CR-107, part 16 §3.4 territory caps | E1 `B11F1`, E5 `F1` |
| B11F2-flow-in | IN | B09, B10, B11F1 | B38 | CR-97 to CR-102, CR-104; CR-103 and CR-105 as its held tail (CR-105 needs its AX-2 hunk at its gate, E5); H-25, H-106 on CR-98; part 16 §3.1, §3.5, §3.6 | E1 `B11F2`, E5 `F2` and `F3`, E6 `B10b-loops` |
| B21b-fa-war | FA | B21, B11 | B21c, B22, B23, B32, B40 | IN-36's cap first; CR-91's carrier (as occasion, A-103; before B22, whose `Field` formation reads the WAR Proposition); CP-T09-01 to -05, -07 (b), -09; CR-09 with H-101; IN-30 (with §1a-(c), SE-05, FA-02); IN-48 with H-108 (b); FA-01; H-132 (A-105, `may_fill`); H-133; H-142; the pointer rows ED-406, ED-407, ED-609, G-19, TL-B5.2 | E1 `B21b`; E2 `B21b-fa-seat-filling` (its war half); E4 `B21b-fa-plan`; E6 `B21b-delegation` |
| B21c-fa-seats | FA | B21b | B24a, B32, B40 | CR-32 with H-181; CR-35 with H-217; CR-36; CR-37 (with `depose` closed); CR-38 (design-first bench; A-76's interim bench); CR-39 (held on CR-38); H-90 | E1 `B21c`; E2 `B21b-fa-seat-filling` (its seat half) |
| B21d-fa-arc | FA | B21b, B11 | — | CR-89 (1) to (4), CR-90, CR-88 (design first, then build), in v11's order CR-89 (1)(2) → CR-90 → CR-88 → CR-89 (3)(4) | E1 `B21d`; E2 `B42-fa-arc` (its after-list also names B23 and B36: not confirmed from CR-89's entry, stage 6 to check); E4 `B21c-arc` |
| B21s-strife-supply | IN | B12, B21 | — | CR-73, CR-74 | E5 `strife-supply` (E5 read part 16, where both live; E4's placement of CR-73 in B37p is not taken) |
| B24a-sc-outside-the-room | SC | B24, B21c | B27, B32 | CR-58, CR-59 (narrowed by A-39), CR-60 (less IS-B2-SC-03's rite default), CR-61 (less the docket key IS-B2-SC-02 lands in B24), CR-62 (less HEAR_B's plea), CR-63 (less IS-B2-SC-05's opening verb), CR-64 | IS-B2-SC-10 ('a v12 batch after B24, named by step 5'); E2 `B24a-sc-intake` placed it BEFORE B24, which IS-B2-SC-10 contradicts; it must close before B27 because `05_SC_arrangement_rows_that_bind.md` edit 5 gates on its close |
| B37p-wr-kin-and-life | WR | B12, B37 | B39 | CP-T10-04, -06, -07, -09 (CP-T10-08 is SUPERSEDED by `23_STORY_B`) | E4 `B37p-wr-npc-life`; E5 'B37/B39 (kin chain)' |

**Not taken.** E4 `B11b-verbs-r05` (§2). E5 `B35a` (a thread-host batch before B35): IS-B3-WR-01 orders the host after `09_WR_B_threadwork_session_and_practitioner` edits 1-2, which are B35 members, so moving the host earlier would move those edits too; the host stays B35's first card item. E6 `B03e-scale-cut`: CR-07 and H-89 are one MISSING-DEP item at B03's tail.

**Cycle check.** The U3 after-lists (§2.1, parsed by script, self-references dropped) plus the edges above form an acyclic graph of 52 batches. The longest chain is 22 batches, the same length as U3's own longest chain once B03c is counted (U3 states 20 before B03c and B19a; neither was recomputed there): B00 → B01 → B02 → B03 → B03c → B04 → B05 → B06 → B07 → B09 → B10 → B21 → B21b → B21c → B24a → B27 → B32 → B35 → B36 → B38 → B39 → B40. It ties U3's own chain through B15/B16/B19a, so the new FA and SC batches are on a critical path, not off it: stage 6 should order B21b, B21c and B24a first among ties (STAGES rule 5).

## 4. Items owed by the new rulings (no v11 row carries them)

These enter v12 from Jordan's answers. They are not v11 rows and so are not in §5, but each retires or narrows a v11 row in the ledger:

- **A-104**: management orders cost no scene budget and may prompt scenes (a declared hash mover; the order list is CL-MGMT's). Retires M31 (b) and E-3.
- **A-108**: a stored offset on each manner axis, built in CL-PERSON with a neutral-control gate. Retires E-4; M34 is built with it.
- **A-105**: one clause at `state/gate.py::may_fill`: a grant reduction is judged as a revocation whose odds read the two factions' relative power. Carried as H-132 in B21b.
- **A-109**: the find-the-hidden design (SE+FI, a proposal first). Carried as H-325/H-326 (r), design-first.
- **A-111**: the ledger rows for Jordan's 2026-10-28 words (M31, M32), written as relayed. Carried as H-1 (IN, B00).
- **A-114**: the longer re-take of THE NINE runs once, as the plan's last item, after M5; every batch close before it stays at two seasons. This governs IS-A-13 and v11 P10, P16 (1).
- **A-103**: correct `30_WR_A_the_era_is_a_named_period.md:65`; build CR-91's carrier as occasion only.
- **A-112** (combat reads skill scores through the skill table; `faculty` dropped) answers the open question that held CR-85's design (ED-IN-0351); CR-85's hooks half (ED-IN-0331) stays carried. **A-100/A-113** (mass battle as an abstraction of personal combat; equipment matchups as stated rows checked against history and banded to the derived results) are in `master/mb_abstraction/` and U3's B19a/B19/B31; they retire CR-12, ED-MB-0045's melee item and MB-07r, and fire ED-1043's trigger at MBA-04 step 0.

## 5. The items, by lane and batch (generated)

Order inside a lane: v12 head rules; then the batches in dependency order (the level the cycle check computes); then the A-109 design item; then the held list.

### Lane IN (90 items)

**v12 head rules (not a batch)**

- **P1** · STILL-NEEDED · rows E1:28 · carry-forward: E1 (no block; the table row is the carry) · lane's target: v12 head rule; IN
- **P2** · STILL-NEEDED · rows E1:29 · carry-forward: E1 (no block; the table row is the carry) · lane's target: v12 head rule; IN
- **P3b** · STILL-NEEDED · rows E1:31 · carry-forward: E1 (no block; the table row is the carry) · lane's target: v12 head rule; IN
- **P4** · STILL-NEEDED · rows E1:32 · carry-forward: E1 (no block; the table row is the carry) · lane's target: v12 head rule; IN
- **P5** · STILL-NEEDED · rows E1:33 · carry-forward: E1 (no block; the table row is the carry) · lane's target: v12 head; IN
- **P6** · STILL-NEEDED · rows E1:34 · carry-forward: E1 (no block; the table row is the carry) · lane's target: v12 head; IN
- **P7** · STILL-NEEDED · rows E1:35 · carry-forward: E1 (no block; the table row is the carry) · lane's target: v12 head; IN
- **P8** · STILL-NEEDED · rows E1:36 · carry-forward: E1 (no block; the table row is the carry) · lane's target: v12 head; IN
- **P9** · STILL-NEEDED · rows E1:37 · carry-forward: E1 (no block; the table row is the carry) · lane's target: v12 head; IN
- **P10** · STILL-NEEDED · rows E1:38 · carry-forward: E1 (no block; the table row is the carry) · lane's target: two options in `## Items for Jordan` · **settled:** A-114 (EVAL-1, Option A as amended): P10 STANDS as a v12 head rule: no probe and no batch close runs past two seasons; the single exception is the longer re-take of THE NINE, run once as the plan's very last item (after M5).
- **P11** · STILL-NEEDED · rows E1:39 · carry-forward: E1 (no block; the table row is the carry) · lane's target: v12 head; IN
- **P12** · STILL-NEEDED · rows E1:40 · carry-forward: E1 (no block; the table row is the carry) · lane's target: v12 head; IN
- **P14** · STILL-NEEDED · rows E1:42 · carry-forward: E1 (no block; the table row is the carry) · lane's target: v12 head; IN
- **P15** · STILL-NEEDED · rows E1:43 · carry-forward: E1 (no block; the table row is the carry) · lane's target: v12 head; IN
- **P16** · STILL-NEEDED · rows E1:44 · carry-forward: E1 (no block; the table row is the carry) · lane's target: v12 head; IN; clause (1) waits on EVAL-1 · **settled:** A-114: P16 clause (1) STANDS with the same single end-of-plan exception; clauses (2)-(4) as E1 found.
- **V1** · STILL-NEEDED · rows E1:45 · carry-forward: E1 (no block; the table row is the carry) · lane's target: v12 head; IN
- **V2** · STILL-NEEDED · rows E1:46 · carry-forward: E1 (no block; the table row is the carry) · lane's target: v12 head; IN
- **V3** · STILL-NEEDED · rows E1:47 · carry-forward: E1 (no block; the table row is the carry) · lane's target: v12 head; IN
- **V4** · STILL-NEEDED · rows E1:48 · carry-forward: E1 (no block; the table row is the carry) · lane's target: v12 head; IN
- **-00 §6 risk 2** · STILL-NEEDED · rows E1:57 · carry-forward: E1 (no block; the table row is the carry) · lane's target: V1 in v12 head
- **-00 §6 risk 4** · STILL-NEEDED · rows E1:59 · carry-forward: E1 (no block; the table row is the carry) · lane's target: v12 head `Defaults in force`; A-15 replaces the `age_step` line
- **-00 §6 risk 6** · STILL-NEEDED · rows E1:61 · carry-forward: E1 (no block; the table row is the carry) · lane's target: v12 head; BA1

**B00-ids**

- **H-1** · STILL-NEEDED · rows E5:141 · carry-forward: E5 Block D8 · lane's target: IN · B00 (ids) · needs Jordan's confirmation. Block D8 · **settled:** re-cited, A-111 (H-1): v12 carries the owed ledger rows (M31, M32) as relayed, marked 'Jordan's words relayed, not recorded'; the menu-budget part is superseded by A-104.

**B02-tests**

- **V9-27** · STILL-NEEDED · rows E3:641 · carry-forward: E3 Block 8 · lane's target: IN, B02 (with `01_CORE_requirements_reading_record`); edit set the R-05 `measure:` comment; gate: no figure in the comment, a command instead; tier haiku. Block 8.
- **DEF-8** · STILL-NEEDED · rows E4:593 · carry-forward: E4 §Carry-forward, line 4360 · lane's target: IN · U3 B02 (decide there)
- **H-2** · STILL-NEEDED · rows E5:142 · carry-forward: E5 Block D9 · lane's target: IN · B02 (`01_CORE_requirements_reading_record`) · gate: `register --requirements`. Block D9

**B03-hygiene**

- **IN-44** · STILL-NEEDED · rows E1:240, E2:95, E3:352, E4:473 · carry-forward: E1 §Carry-forward, line 3992; E2 §Carry-forward, line 854; E3 (no block; the table row is the carry) · lane's target: LEAVE list; re-derive at slot · gate: v9 states none for IN-44 as a table. The instrument v9 names for the adoption-time subset is `python tools/currency_consistency_che… · **settled:** IN-44 rows 2-15: re-derive each anchor against the A-97-amended `04` (E2:95); row 1 done, row 16 superseded.
- **CR-07, H-89** · MISSING-DEP · rows E1:246, E2:22, E3:516, E4:336, E6:119 · carry-forward: E1 §Carry-forward, line 4129; E2 §Carry-forward, line 187; E3 §Carry-forward, line 657 · lane's target: owner: Jordan (the seat's rung) or A1-46's revert (keep the column and author a reader); lane IN · gate: the verb-table loader loads and `tests/test_season_shape.py` pas… · **settled:** CR-07: IS-B2-CORE-06 BLOCKED (DEP-v11): the pre-flight needs `off_npc_084`'s rung, content the plan may not author; owner Jordan (the seat's rung) or A1-46's revert; one item with H-89.
- **A1-46** · STILL-NEEDED · rows E3:141 · carry-forward: E3 §Carry-forward, line 657 · lane's target: IN, B03 (`U5a_CORE_owed_edits` §E 3); edit set `verb_table.yaml`, `data/verbs.py` (`VerbRow.scale`, load check, `:129-137, :619-621`), `tests`; gate: `grep -n "scale:" e…
- **A1-81** · STILL-NEEDED · rows E3:176 · carry-forward: E3 Block 8 · lane's target: IN, B03; edit set `architecture/meta/04_CODE_ARCHITECTURE.md` heir nodes; gate: `grep -n founding` on the nodes reads the title route; hash EQUAL; tier haiku. Block 8.
- **A2-40** · STILL-NEEDED · rows E3:228 · carry-forward: E3 Block 8 · lane's target: IN, B03 (hygiene; with `09_WR_B_pointer_text_for_the_orchestrator`); edit set the three docstrings; gate: `grep -n ED-IN-0225 engine/season/harness/{chronicle,populated,…
- **ER-C4** · STILL-NEEDED · rows E3:420 · carry-forward: E3 Block 8 · lane's target: IN, B03 (hygiene); edit set `rosters.yaml` remit roster flag; gate: the roster loader reads the flag consistently and no comment contradicts it; tier haiku. Block 8.
- **ER-GF9** · STILL-NEEDED · rows E3:421 · carry-forward: E3 Block 8 · lane's target: IN, B03; edit set the exporter source (`tools/export_sim_params.py`); gate: `--check` round-trip without them; tier haiku. Block 8.
- **H-141** · STILL-NEEDED · rows E3:568, E7:26 · carry-forward: E3 (no block; the table row is the carry); E7 §Carry-forward, line 148 · lane's target: — · **settled:** register row governs (E7:26 STILL-NEEDED); E3 convention 6 defers the register row to E6-E8.
- **H-143** · STILL-NEEDED · rows E3:570, E7:28 · carry-forward: E3 (no block; the table row is the carry); E7 §Carry-forward, line 162 · lane's target: — · **settled:** register row governs (E7:28 STILL-NEEDED); E3 convention 6 defers the register row to E6-E8.
- **V9-02** · STILL-NEEDED · rows E3:616 · carry-forward: E3 Block 8 · lane's target: IN, B03 (hygiene); edit set `registers/handoffs/HANDOFF_*.md` Open rows; gate: `grep` finds only history rows; hash EQUAL; tier haiku. Block 8.
- **V9-20** · STILL-NEEDED · rows E3:634 · carry-forward: E3 Block 8 · lane's target: IN, B03; edit set the synthesis Status line; gate: `grep MB-05r` finds only history; tier haiku. Block 8.
- **DEF-5** · STILL-NEEDED · rows E4:590 · carry-forward: E4 §Carry-forward, line 4348 · lane's target: IN · with CR-07
- **REM-26** · STILL-NEEDED · rows E5:88 · carry-forward: E5 Block C36 · lane's target: IN · B03-adjacent reading (haiku) · gate: the REM-11 reading at `aperture 1 s`. Block C36
- **H-4** · STILL-NEEDED · rows E5:144 · carry-forward: E5 Block D10 · lane's target: IN · B03 · gate: `rg` finds no live reader before RETIRED mark. Block D10

**B08-scene-order**

- **H-249** · STILL-NEEDED · rows E8:41 · carry-forward: E8 §Carry-forward, line 172 · lane's target: CHAR lane (IN-owned file), join B08 (`pack_scenes` edit), measure-first; CF-E8-2

**B03d-gate-observation (NEW, §3)**

- **H-130** · STILL-NEEDED · rows E3:557, E6:143 · carry-forward: E3 (no block; the table row is the carry); E6 carry-forward block 5 · lane's target: — · **settled:** register row governs (E6:143 STILL-NEEDED); E3 convention 6 defers the register row to E6-E8.
- **H-137** · STILL-NEEDED · rows E3:564, E6:150 · carry-forward: E3 (no block; the table row is the carry); E6 carry-forward block 5 · lane's target: — · **settled:** register row governs (E6:150 STILL-NEEDED); E3 convention 6 defers the register row to E6-E8.
- **H-138** · STILL-NEEDED · rows E3:565, E6:151 · carry-forward: E3 (no block; the table row is the carry); E6 carry-forward block 5 · lane's target: — · **settled:** register row governs (E6:151 STILL-NEEDED); E3 convention 6 defers the register row to E6-E8.
- **H-139** · STILL-NEEDED · rows E3:566, E6:152 · carry-forward: E3 (no block; the table row is the carry); E6 carry-forward block 5 · lane's target: — · **settled:** register row governs (E6:152 STILL-NEEDED); E3 convention 6 defers the register row to E6-E8.

**B09-memory**

- **H-145, NM-W9** · STILL-NEEDED · rows E1:217, E2:56, E3:572, E4:490, E7:30 · carry-forward: E1 §Carry-forward, line 3542; E2 §Carry-forward, line 508; E3 (no block; the table row is the carry) · lane's target: IN · HELD list · hash: E · **settled:** register row governs (E7:30 STILL-NEEDED); E3 convention 6 defers the register row to E6-E8.
- **IN-58** · STILL-NEEDED · rows E1:248, E2:97, E3:358, E4:477 · carry-forward: E1 §Carry-forward, line 4154; E2 §Carry-forward, line 873; E3 §Carry-forward, line 673 · lane's target: HELD list · gate: the sworn-to falsifier: "two judges with equal stance and pursuits, one sworn to the victim's seat, read different regard for the killer -> else that .…
- **H-135** · STILL-NEEDED · rows E3:562, E6:148 · carry-forward: E3 (no block; the table row is the carry); E6 §Carry-forward, line 189 · lane's target: — · **settled:** register row governs (E6:148 STILL-NEEDED); E3 convention 6 defers the register row to E6-E8.

**B10-character**

- **CL-PERSON** · STILL-NEEDED · rows E1:227, E2:68, E4:237, E5:131 · carry-forward: E1 §Carry-forward, line 3705; E2 §Carry-forward, line 543; E4 §Carry-forward, line 998 · lane's target: IN · HELD on M34-M37, M40, E-4 · hash: E (design). The build: EQUAL at neutral values; a declared m ... · tier: design `opus`, critic per `-10` (the lan ... · **settled:** re-cited: CL-PERSON's E-4 hold is lifted by A-108 (stored offsets allowed); the build stays held on M35-M37, M40 as v11 states.
- **CR-93** · STILL-NEEDED · rows E1:230, E4:422 · carry-forward: E1 §Carry-forward, line 3786; E4 §Carry-forward, line 2938 · lane's target: IN · design-first at B10 · gate: the file exists and states (1) to (4) with falsifiers: two hand-built persons with equal pursuits and different attributes rank one unco…
- **CR-95** · STILL-NEEDED · rows E1:231, E4:424 · carry-forward: E1 §Carry-forward, line 3812; E4 §Carry-forward, line 2988 · lane's target: IN/PC/SC · design-first after B10-11b (landed) and SC-02 · gate: the file states (1) to (4) with falsifiers; the diagnostic's report shows no composed obstacle below `ba…
- **M34** · STILL-NEEDED · rows E3:64, E5:120 · carry-forward: E3 (no block; the table row is the carry); E5 Block D1 · lane's target: — · **settled:** A-108 reverses 'as shipped (no stored offset)': M34 is built with CL-PERSON.
- **M36** · STILL-NEEDED · rows E3:66, E5:122 · carry-forward: E3 (no block; the table row is the carry); E5 Block D2 · lane's target: — · **settled:** M36: part 15 carries a design lane (the beneficiary column has no owner since REM-44), E5:122.
- **M40** · STILL-NEEDED · rows E3:70, E5:127 · carry-forward: E3 (no block; the table row is the carry); E5 Block D3 · lane's target: — · **settled:** M40: the horizon term has no session author (E5:127); the risk term is `02_CHAR_what_an_act_risks.md` (E5:126).
- **A1-05** · STILL-NEEDED · rows E3:99 · carry-forward: E3 §Carry-forward, line 655 · lane's target: IN, B10; edit set `queries/world_q.py` attention tiers (`own_purview` is at `:1080`); gate: a 3-seed reading (R3 figures) with tier-1 echoes spared; moves hashes: yes; t…
- **H-191** · MISSING-DEP · rows E3:262, E7:89 · carry-forward: E3 (no block; the table row is the carry); E7 §Carry-forward, line 227 · lane's target: — · **settled:** register row governs (E7:89 MISSING-DEP); E3 convention 6 defers the register row to E6-E8.
- **H-198, M9** · MISSING-DEP · rows E3:269, E7:96 · carry-forward: E3 (no block; the table row is the carry); E7 §Carry-forward, line 231 · lane's target: — · **settled:** register row governs (E7:96 MISSING-DEP); E3 convention 6 defers the register row to E6-E8.
- **ER-JF10** · STILL-NEEDED · rows E3:423 · carry-forward: E3 Block 12 · lane's target: CHAR, B10 (read there first); edit set none beyond that proposal; gate: pursuit weights sum to one per person or the loader refuses; tier sonnet. Block 12.
- **H-180** · STILL-NEEDED · rows E3:605, E7:78 · carry-forward: E3 (no block; the table row is the carry); E7 §Carry-forward, line 193 · lane's target: — · **settled:** register row governs (E7:78 STILL-NEEDED); E3 convention 6 defers the register row to E6-E8.
- **V9-11** · STILL-NEEDED · rows E3:625 · carry-forward: E3 Block 5 · lane's target: IN, B10.
- **DEF-12** · STILL-NEEDED · rows E4:595 · carry-forward: E4 §Carry-forward, line 4366 · lane's target: IN · see gap register
- **B10-16 gates, IN-52 and `requi** · STILL-NEEDED · rows E4:673 · carry-forward: E4 (no block; the table row is the carry) · lane's target: same target as the B10-16 gates, IN-52 and `requisition` row

**B11-fi-readers**

- **CR-83** · STILL-NEEDED · rows E1:89, E2:30, E4:412 · carry-forward: E1 §Carry-forward, line 508; E2 §Carry-forward, line 257; E4 §Carry-forward, line 2788 · lane's target: IN/FI · design-first beside B11 (IS-B2-FI-05 owner: B11's design pass) · gate: the design file with items (1)-(6) each carrying a falsifier; no code · gate: the design f…
- **A2-43** · STILL-NEEDED · rows E3:231 · carry-forward: E3 §Carry-forward, line 667 · lane's target: IN, before B11 (CR-29 is a dependency of `08_FI_01`): a new batch `B-CR29` or fold into B09-memory; edit set `rosters.yaml` (`reach` roster), `loop/witness.py`; gate: `p…

**B21-fa-governance**

- **M38** · STILL-NEEDED · rows E3:68, E5:124 · carry-forward: E3 §Carry-forward, line 649; E5 Block D5 · lane's target: IN/FA, batch B21 or B32 (no new batch); edit set: none beyond CR-38; gate: n/a (a standing rule: no marquis in canon). Block 2.

**B12-world-motion-and-ground**

- **CR-47** · STILL-NEEDED · rows E1:170, E2:71, E4:376 · carry-forward: E1 §Carry-forward, line 2558; E2 §Carry-forward, line 600; E4 §Carry-forward, line 887 · lane's target: IN/SE · B12 (re-based on B10 chooser edits first, V1) · gate: card exit · gate: `aperture 3 s`, s = 0-2: `build`, `found`, `restore`, `examine` each attempted by a works…
- **G-05** · STILL-NEEDED · rows E4:190 · carry-forward: E4 §Carry-forward, line 887 · lane's target: IN · with CR-47 (see that row) and U3 B12 · gate: `aperture 4 0` seeds 0-2 `rung.founded` >= 1 and `site.built` >= 1 by a computed actor

**B21b-fa-war (NEW, §3)**

- **SE-05** · STILL-NEEDED · rows E2:134, E3:367 · carry-forward: E2 §Carry-forward, line 1067; E3 §Carry-forward, line 653 · lane's target: as IN-30 (no separate row)

**B24-sc-hearing**

- **CR-92** · STILL-NEEDED · rows E1:229, E4:421 · carry-forward: E1 §Carry-forward, line 3760; E4 §Carry-forward, line 2913 · lane's target: IN/SC · design-first beside B24/B10 · design file with six falsifiers · gate: the file exists and states (1) to (6), each with a falsifier and a control (every term at 0…

**B11F1-flow-se (NEW, §3)**

- **CR-106** · STILL-NEEDED · rows E1:187, E4:435, E5:159 · carry-forward: E1 §Carry-forward, line 2901; E4 §Carry-forward, line 3013; E5 Block F3 · lane's target: IN/SE · new batch B11F1 (flow conditioning) · declared hash mover (new Sites) · hash: `build_realm(0).content_hash()` MOVES where rows carry `site ... · tier: second tie…

**B21s-strife-supply (NEW, §3)**

- **CR-74** · STILL-NEEDED · rows E1:185, E4:403, E5:155 · carry-forward: E1 §Carry-forward, line 2844; E4 §Carry-forward, line 2758; E5 Block F2 · lane's target: SC/IN · after CR-63 and CR-51b · harness EQUAL · gate: at the batch close CH above 0 at some seed (`strife 3 0 1 2`; the batch declares movers, P10) or GAP with the carr…

**B29-pc-custody**

- **CR-51** · STILL-NEEDED · rows E1:174, E4:380 · carry-forward: E1 §Carry-forward, line 2610; E4 §Carry-forward, line 2354 · lane's target: IN/FA · after B29 and B21 · gate: card exit (re-taken) · gate: `aperture 3 s`: `arrest.made` and `detention.ended` or `ban.ended` caused by computed acts; or the exit re…

**B11F2-flow-in (NEW, §3)**

- **CR-104** · STILL-NEEDED · rows E1:189, E4:433, E5:162 · carry-forward: E1 §Carry-forward, line 2978; E4 §Carry-forward, line 3013; E5 Block F5 · lane's target: IN · B11F2 first item · EQUAL · hash: none (no loop consumer; hash EQUAL by construction). · tier: second tier; a third-tier (judgment) cri ...
- **CR-97** · STILL-NEEDED · rows E1:190, E4:426, E5:163 · carry-forward: E1 §Carry-forward, line 3011; E4 §Carry-forward, line 3013; E5 Block F6 · lane's target: IN · B11F2 · EQUAL (harness) · hash: none. · tier: second tier; a third-tier (judgment) cri ...
- **CR-98, H-106, H-25** · STILL-NEEDED · rows E1:191, E3:456, E3:533, E4:427, E5:164, E6:49 … · carry-forward: E1 §Carry-forward, line 3062; E3 (no block; the table row is the carry); E4 §Carry-forward, line 3063 · lane's target: IN · B11F2 before B38 · EQUAL · gate: `python -m engine.season.harness.register --check` passes G13 on the new rows; the falsifier: a planted copy of one row with `sign:… · **settled:** register row governs (E6:49 STILL-NEEDED); E3 convention 6 defers the register row to E6-E8.
- **CR-99** · STILL-NEEDED · rows E1:192, E4:428, E5:165 · carry-forward: E1 §Carry-forward, line 3101; E4 §Carry-forward, line 3101; E5 Block F8 · lane's target: IN · B11F2 · EQUAL · gate: the planted concentrator reads FAIL; the one-code off arm reads BLIND; two identical arms read PASS. MUTATION: drop the share clause and the c…
- **CR-100** · STILL-NEEDED · rows E1:193, E4:429, E5:166 · carry-forward: E1 §Carry-forward, line 3132; E4 §Carry-forward, line 3131; E5 Block F9 · lane's target: IN · B11F2 · EQUAL off, mover on · hash: on, a mover of every season in which a strand is open: one-s ... · tier: second tier; a third-tier (judgment) cri ...
- **CR-101** · STILL-NEEDED · rows E1:194, E4:430, E5:167 · carry-forward: E1 §Carry-forward, line 3174; E4 §Carry-forward, line 3013; E5 Block F10 · lane's target: IN · B11F2 · gate: (1) in a hand-built world, a tier-2 claim question whose referent is a within-stake sorts earlier at gain > 0 than at 0, and only inside its tier, whi…
- **CR-102** · STILL-NEEDED · rows E1:195, E4:431, E5:168 · carry-forward: E1 §Carry-forward, line 2989; E4 §Carry-forward, line 3203; E5 Block F11 · lane's target: IN · B11F2 last · NOT BUILT unless the gate holds · gate: (1) in a planted world, swap two offices' rungs and the term follows the offices; (1b) a realm-kind office's te…
- **CR-103** · STILL-NEEDED · rows E1:196, E4:432, E5:169 · carry-forward: E1 §Carry-forward, line 3238; E4 §Carry-forward, line 3013; E5 Block F12 · lane's target: IN · after the FA/WR/SC batches that supply `at_war`, CL-EVENTS (2), docket closure · mover only if an arm ships · gate: the falsifier of T1 on this route: OFF already m…
- **CR-105** · STILL-NEEDED · rows E1:197, E4:434, E5:170 · carry-forward: E1 §Carry-forward, line 3270; E4 §Carry-forward, line 3297; E5 Block F13 · lane's target: HELD list; IN · gate: (1) two hand-built persons with equal pursuits, one whose question carries a stake on a candidate's subject, rank that candidate higher at gain > 0…
- **P16 section 3.1 rules, 3.5 dec** · STILL-NEEDED · rows E5:171 · carry-forward: E5 Block F14 · lane's target: IN/SE · F1/F2 as above. Block F14
- **P16 section 3.6 owed correctio** · STILL-NEEDED · rows E5:173 · carry-forward: E5 Block F14 · lane's target: with F2/F1. Block F14

**B36-wr-story-instruments**

- **NM-W5** · STILL-NEEDED · rows E1:212, E2:52, E4:486 · carry-forward: E1 (no block; the table row is the carry); E2 §Carry-forward, line 508; E4 §Carry-forward, line 3990 · lane's target: none (B36/B38) · **settled:** NM-W5: `09_WR_B_chronicle_that_tells.md:63`: 'The journal NM-W5 owes ... is not built here'.

**held / LEAVE (no batch until the named trigger fires)**

- **CL-MGMT** · STILL-NEEDED · rows E1:228, E2:69, E4:235, E5:132 · carry-forward: E1 §Carry-forward, line 3732; E2 §Carry-forward, line 562; E4 §Carry-forward, line 986 · lane's target: GO/IN · design-first after B34 · HELD on M31 · hash: E (design). The build: EQUAL under the weak reading with the ... · tier: design `opus`; build `sonnet`. · **settled:** re-cited: CL-MGMT's M31 hold is lifted by A-104 (orders cost no scene budget; they may prompt scenes).
- **IN-18** · STILL-NEEDED · rows E1:245, E2:92, E3:347, E4:468 · carry-forward: E1 §Carry-forward, line 4103; E2 §Carry-forward, line 836; E3 (no block; the table row is the carry) · lane's target: HELD list · gate: EXIT "per gate, §5's falsifier column, observed at the batch that builds it" (G1's EXIT, `engine/season/tests/test_told_by_channel.py::test_r07_realm_ … · **settled:** IN-18: held; re-measure M0e after CR-29 (E2:92); E3's three proposals were cited, not opened.
- **DEF-2** · STILL-NEEDED · rows E4:587 · carry-forward: E4 §Carry-forward, line 791 · lane's target: IN · held residue, no work (v12 'held and leave' list), trigger unchanged · gate: none until the trigger fires · hash: n/a · tier: n/a
- **DEF-10** · STILL-NEEDED · rows E4:596 · carry-forward: E4 §Carry-forward, line 4372 · lane's target: IN · held residue, no work (v12 'held and leave' list), trigger unchanged · gate: none until the trigger fires · hash: n/a · tier: n/a
- **DEF-11** · STILL-NEEDED · rows E4:597 · carry-forward: E4 §Carry-forward, line 4378 · lane's target: IN · held residue, no work (v12 'held and leave' list), trigger unchanged · gate: none until the trigger fires · hash: n/a · tier: n/a
- **REM-30** · STILL-NEEDED · rows E5:93 · carry-forward: E5 Block C37 · lane's target: IN/CHAR · HELD, decide at v12 against B04 · gate: arm off reproduces pre-build hash. Block C37


### Lane FA (53 items)

**B03-hygiene**

- **H-291** · STILL-NEEDED · rows E8:83 · carry-forward: E8 §Carry-forward, line 183 · lane's target: FA lane, B03 (item 2 already edits `_req_establish`); hash-EQUAL for computed play; CF-E8-3

**B21-fa-governance**

- **M8** · STILL-NEEDED · rows E3:38 · carry-forward: E3 §Carry-forward, line 647 · lane's target: FA, batch B21 (with `06_FA_seat_terms_by_body_B`); edit set `state/gate.py::REVOCATION_RULES`, `offices.yaml: off_king.revocation`, `data/rosters.py` revocation_bases; g…
- **§1b-3** · STILL-NEEDED · rows E3:85 · carry-forward: E3 Block 1 · lane's target: FA, B21; as M8 (Block 1) plus CR-36's `nominated` basis; gate: `confer` on a body's carried `resolution` fills a `nominated` seat in a hand-built world; hash EQUAL. Bloc…
- **A2-14** · STILL-NEEDED · rows E3:202 · carry-forward: E3 §Carry-forward, line 647 · lane's target: FA, B21; Block 1.

**B21b-fa-war (NEW, §3)**

- **IN-30** · STILL-NEEDED · rows E1:127, E2:117, E3:348, E4:469 · carry-forward: E1 §Carry-forward, line 1434; E2 §Carry-forward, line 1067; E3 §Carry-forward, line 653 · lane's target: FA · new batch B21b (war and seats) · after B21 · gate: card exit (size per season, non-rostered creeds) · gate: EXIT "`grep -rn "uncontrolled(" engine/season/queries en…
- **CP-T09-04** · STILL-NEEDED · rows E1:128, E4:314, E4:686, E4:687, E5:55, E5:56 · carry-forward: E1 §Carry-forward, line 1462; E4 §Carry-forward, line 1655; E5 Block C22 · lane's target: FA · B21b before B23 · amended · gate: (1) Seed 0, tick 1, King dead: the Widow Regent's seat (`off_npc_032`, realm purview, `issue`) seizes a former royal · hash: M · t…
- **CP-T09-01** · STILL-NEEDED · rows E1:129, E4:311, E4:682, E5:51 · carry-forward: E1 §Carry-forward, line 1524; E4 §Carry-forward, line 803; E5 Block C19 · lane's target: FA · B21b · measure first · gate: Hand-built through the real fold, seed 0, tick 0: two Crown members with equal pursuits; one carries a stance row · hash: M · tier: per…
- **CP-T09-05** · STILL-NEEDED · rows E1:130, E4:315, E4:688, E5:57 · carry-forward: E1 §Carry-forward, line 1581; E4 §Carry-forward, line 1681; E5 Block C24 · lane's target: FA · B21b · gate: Hand-built: a territory holder with a seat and a co-located obligee forms `give {subject: terr, to: obligee}`; executed, · hash: M · tier: per home (Si…
- **CP-T09-02** · STILL-NEEDED · rows E1:131, E4:312, E4:683, E4:684, E5:53 · carry-forward: E1 §Carry-forward, line 1624; E4 §Carry-forward, line 1604; E5 Block C20 · lane's target: FA · B21b first (before B23 and `06_FA_war_lives_in_seats_B`'s realm reading) · gate: card exit · gate: (1) Hand-built: a Hafenmark seat-holder with a `dispatch` grant w…
- **CP-T09-03** · STILL-NEEDED · rows E1:132, E4:313, E4:685, E5:54 · carry-forward: E1 §Carry-forward, line 1701; E4 §Carry-forward, line 905; E5 Block C21 · lane's target: FA · B21b · amended by A-20 · gate: (1) Hand-built: a Varfell seat-holder holding the Crown's covenant on W(Crown, Hafenmark) forms `commit` to W; afterwards · hash: M ·…
- **CP-T09-07** · STILL-NEEDED · rows E1:134, E4:317, E4:689, E5:58 · carry-forward: E1 §Carry-forward, line 1748; E4 §Carry-forward, line 1699; E5 Block C25 · lane's target: FA · B21b · gate: card exit · gate: (1) S3's, on H-213's uncapped arm: a seeded `recruit` of an unattached known person opens his `oblige` on Won; over seeds · hash: M ·…
- **CR-09, H-101** · STILL-NEEDED · rows E1:135, E2:24, E3:528, E4:338, E7:33 · carry-forward: E1 §Carry-forward, line 1800; E2 §Carry-forward, line 204; E3 §Carry-forward, line 679 · lane's target: FA · B21b · after CP-T09-07 (b) lands via IS-B3-FA-05 · gate: a hand-built world as `test_in40_oblige_purview.py` builds, where a swearer's ground lies outside the sworn…
- **CP-T09-09** · STILL-NEEDED · rows E1:137, E4:319, E4:690, E5:59 · carry-forward: E1 §Carry-forward, line 1825; E4 §Carry-forward, line 725; E5 Block C26 · lane's target: FA · B21b · measure first · gate: S7's: a `conspire` on a held plot opens the invitee's edge on Won only; over seeds an invitee with a live `oblige` to the · hash: M · t…
- **H-108, IN-48** · STILL-NEEDED · rows E1:144, E2:119, E3:356, E3:535, E4:475, E6:137 · carry-forward: E1 §Carry-forward, line 1938; E2 §Carry-forward, line 402; E3 (no block; the table row is the carry) · lane's target: none (B32/B33) · **settled:** IN-48: `U5_FINDINGS_CLOSURE_U5d.md:75,77` name IN-48 the owner of delegation (A-10, A-22 fix whom a seat commands); one item with H-108b; E1's BYZ_C reading was an [ASSUMPTION].
- **IN-36** · STILL-NEEDED · rows E1:145, E2:118, E4:472 · carry-forward: E1 §Carry-forward, line 2005; E2 §Carry-forward, line 1087; E4 §Carry-forward, line 917 · lane's target: FA · B21b first item (the cap) · declared movers · gate: natural-play half as above (witness seeds). The cap (ED-IN-0317): a planted second march into one territory in o…
- **FA-01** · STILL-NEEDED · rows E1:146, E2:116, E3:380, E4:450 · carry-forward: E1 §Carry-forward, line 2032; E2 §Carry-forward, line 1050; E3 §Carry-forward, line 667 · lane's target: FA · B21b after CR-29 (B11) · gate: EXIT (quoted; R-04's reading runs on Jordan's call, head P10 and V4) "`python -m engine.season.harness.aperture 4 0` (R-04's measure,…
- **CR-91** · STILL-NEEDED · rows E1:147, E2:39, E4:420 · carry-forward: E1 §Carry-forward, line 2057; E2 §Carry-forward, line 329; E4 §Carry-forward, line 2812 · lane's target: two options in `## Items for Jordan` · **settled:** A-103 (J-E2-01 = EVAL-3 = J-E3-1, Option B): the claim gate CR-91 (3) is SUPERSEDED (no `requires_typed` conjunct on `march`); the carrier CR-91 (1)(2)(4)(5) is STILL-NEEDED as occasion and as context for regard and legitimacy; IN-36's cap stays.
- **§1a-M1res** · STILL-NEEDED · rows E3:74 · carry-forward: E3 Block 3 · lane's target: FA, batch B21/B23; edit set `harness/populated.py::build_realm` (`guards`), the march-per-territory cap in `loop/sides.py`; gate: `T:test_in36_foreign.py` extended: no t… · **settled:** re-cited, A-103: only IN-36's cap (one march per season per territory) and `guards` ON after CP-T09-07 (b)'s union survive; no casus-belli gate (B21b).
- **§1a-(c)** · STILL-NEEDED · rows E3:81 · carry-forward: E3 Block 4 · lane's target: FA/WR, batch B12 (with `09_WR_world_motion`); edit set `queries/faction_q.py` (`faction_props`), `data/rosters.py` faction Propositions; gate: a hand-built creed commit …
- **FA-02** · STILL-NEEDED · rows E3:381 · carry-forward: E3 §Carry-forward, line 653 · lane's target: See §1a-(c).
- **H-132** · STILL-NEEDED · rows E3:559, E6:145 · carry-forward: E3 (no block; the table row is the carry); E6 §Carry-forward, line 200 · lane's target: — · **settled:** A-105, as E6:145 (the register row governs, CR-25's landing is the base).
- **H-133** · STILL-NEEDED · rows E3:560, E6:146 · carry-forward: E3 (no block; the table row is the carry); E6 carry-forward block 5 · lane's target: — · **settled:** register row governs (E6:146 STILL-NEEDED); E3 convention 6 defers the register row to E6-E8.
- **H-142** · STILL-NEEDED · rows E3:569, E7:27 · carry-forward: E3 (no block; the table row is the carry); E7 §Carry-forward, line 155 · lane's target: — · **settled:** register row governs (E7:27 STILL-NEEDED); E3 convention 6 defers the register row to E6-E8.
- **V9-14** · STILL-NEEDED · rows E3:628 · carry-forward: E3 Block 3 · lane's target: See there. · **settled:** re-cited, A-103 (as §1a-M1res).
- **ED-406** · STILL-NEEDED · rows E4:73 · carry-forward: E4 §Carry-forward, line 725 · lane's target: FA · with CP-T09-09 (see that row) · trigger: a computed `conspire` executes
- **ED-407** · STILL-NEEDED · rows E4:74 · carry-forward: E4 §Carry-forward, line 731 · lane's target: FA · with CP-T09-09 · trigger: a computed claim on the throne executes
- **ED-609** · STILL-NEEDED · rows E4:100 · carry-forward: E4 §Carry-forward, line 803 · lane's target: FA · with CP-T09-01 (see that row)
- **G-19** · STILL-NEEDED · rows E4:205 · carry-forward: E4 §Carry-forward, line 917 · lane's target: FA · CL-THRUST B5.2, after IN-36's flip (see IN-36) · gate: CR-14 `guards` arm via `run_arm` · hash: mover
- **TL-B5.2** · STILL-NEEDED · rows E4:227 · carry-forward: E4 §Carry-forward, line 953 · lane's target: FA · see G-19
- **§2 `covenant` formation (PR #5** · STILL-NEEDED · rows E4:570 · carry-forward: E4 (no block; the table row is the carry) · lane's target: see CP-T09-03

**B21c-fa-seats (NEW, §3)**

- **CR-32, H-181** · STILL-NEEDED · rows E1:140, E2:33, E3:606, E4:361, E7:79 · carry-forward: E1 §Carry-forward, line 1901; E2 §Carry-forward, line 292; E3 §Carry-forward, line 681 · lane's target: FA · B21c · rename `standing` -> `rank_gap` at re-base · gate: a co-located witness of an act by the holder of a Church-ladder post holds `marks` containing that post; a… · **settled:** H-181: not MISSING-DEP: its producer is v11 CR-32 ('rank reads one scale (H-181's producer)', E3 Block 18), carried in B21c; one item with CR-32.
- **CR-35, H-217** · STILL-NEEDED · rows E1:141, E2:41, E3:288, E4:364, E7:115 · carry-forward: E1 §Carry-forward, line 1927; E2 §Carry-forward, line 400; E3 §Carry-forward, line 671 · lane's target: FA · B21c · before B32 · amended by A-14 · hash: EQUAL in the realm while no computed docket item names `elec ... · tier: `CLAUDE.md` §10's third tier (judgment): ... \| · **settled:** H-217: its closure says 'RESOLVED-BY plan CR-35', a v11 position, not a session item; carried with CR-35 in B21c, amended by A-14/A-19 and `22_HAPPENINGS_B` (E3 Block 13).
- **CR-36** · STILL-NEEDED · rows E1:142, E2:42, E4:365 · carry-forward: E1 §Carry-forward, line 1938; E2 §Carry-forward, line 402; E4 §Carry-forward, line 2091 · lane's target: FA/SC · B21c · before B32 · hash: declared MOVER at build (`off_parliamentary_clerk`'s value; ... · tier: `CLAUDE.md` §10's third tier (judgment): ...
- **CR-37** · STILL-NEEDED · rows E1:143, E2:43, E4:366 · carry-forward: E1 §Carry-forward, line 1938; E2 §Carry-forward, line 402; E4 §Carry-forward, line 2091 · lane's target: FA · B21c · amended: revoke is drawn; Confessor case struck · hash: declared MOVER at build (`off_king`'s value; hashed `w.offic ... · tier: `CLAUDE.md` §10's third tier…
- **CR-38, H-90** · STILL-NEEDED · rows E1:222, E2:44, E3:517, E4:367, E4:572, E5:134 … · carry-forward: E1 §Carry-forward, line 519; E2 §Carry-forward, line 259; E3 (no block; the table row is the carry) · lane's target: FA/SC · design-first beside B21c; approval window per card · hash: EQUAL (a design file); its build a declared MOVER (either ro ... · tier: `CLAUDE.md` §10's third tier … · **settled:** register row governs (E6:120 STILL-NEEDED); E3 convention 6 defers the register row to E6-E8.
- **CR-39** · STILL-NEEDED · rows E1:243, E2:45, E4:368 · carry-forward: E1 §Carry-forward, line 4047; E2 §Carry-forward, line 472; E4 §Carry-forward, line 2179 · lane's target: HELD list; FA · hash: declared MOVER when built (it changes a bench). · tier: `CLAUDE.md` §10's third tier (judgment).
- **§2 `depose` (M8; the verb suit** · STILL-NEEDED · rows E4:574 · carry-forward: E4 (no block; the table row is the carry) · lane's target: see CR-37

**B21d-fa-arc (NEW, §3)**

- **CR-89** · STILL-NEEDED · rows E1:148, E2:37, E4:418 · carry-forward: E1 §Carry-forward, line 2068; E2 §Carry-forward, line 329; E4 §Carry-forward, line 2812 · lane's target: FA/IN · new batch B21d (arc) · after CR-91 and CR-29 · gate: a hand-built log folds to its known value and clamps at cap and range; one planted Church `rung.seized` rais…
- **CR-90** · STILL-NEEDED · rows E1:149, E2:38, E4:419 · carry-forward: E1 §Carry-forward, line 2109; E2 §Carry-forward, line 329; E4 §Carry-forward, line 2812 · lane's target: IN · B21d · gate: a planted log reads its known seasons; feeder weights 0 read "never" on every clock mark. CONTROL: triggers off against on, same seeds; equal arms mea …
- **CR-88** · STILL-NEEDED · rows E1:150, E2:36, E4:417 · carry-forward: E1 §Carry-forward, line 2135; E2 §Carry-forward, line 327; E4 §Carry-forward, line 2812 · lane's target: FA/IN · B21d, after CR-83's design and CR-86 (landed) · gate: (design) the file exists and states (1) to (5); no code. (build) the seed-0 Spymaster (after CR-87's loyalt…

**B25-fi-questioning**

- **H-313** · STILL-NEEDED · rows E8:105 · carry-forward: E8 §Carry-forward, line 183 · lane's target: FA/FI lane, B25 (same predicate edit); CF-E8-3

**B32-inst-kit**

- **H-278** · STILL-NEEDED · rows E8:70 · carry-forward: E8 §Carry-forward, line 183 · lane's target: FA lane, B32 after B09; CF-E8-3

**B23-land**

- **A2-23** · STILL-NEEDED · rows E3:211 · carry-forward: E3 §Carry-forward, line 665 · lane's target: FA, B23 (`14_VERBS_BINDING_E_war_seats`); edit set the treaty edge in `loop/effects_governance.py`; gate: a hand-built treaty lapses when the signer dies and a successor…
- **H-229** · STILL-NEEDED · rows E3:300, E7:127 · carry-forward: E3 (no block; the table row is the carry); E7 §Carry-forward, line 218 · lane's target: — · **settled:** register row governs (E7:127 STILL-NEEDED); E3 convention 6 defers the register row to E6-E8.

**held / LEAVE (no batch until the named trigger fires)**

- **M39** · STILL-NEEDED · rows E3:69, E5:125 · carry-forward: E3 (no block; the table row is the carry); E5 Block D5 · lane's target: — · **settled:** M39: part 15's design-first item (post-freeze mover; A-76 stand-in only), E5:125.
- **ED-640** · STILL-NEEDED · rows E4:104 · carry-forward: E4 §Carry-forward, line 815 · lane's target: FA · held residue, no work (v12 'held and leave' list), trigger unchanged · gate: none until the trigger fires · hash: n/a · tier: n/a · trigger: a Jordan-authored rank …
- **ED-649** · STILL-NEEDED · rows E4:109 · carry-forward: E4 §Carry-forward, line 821 · lane's target: FA · held residue, no work (v12 'held and leave' list), trigger unchanged · gate: none until the trigger fires · hash: n/a · tier: n/a · trigger: an authored Prelate seat
- **ED-650** · STILL-NEEDED · rows E4:110 · carry-forward: E4 §Carry-forward, line 827 · lane's target: FA · held residue, no work (v12 'held and leave' list), trigger unchanged · gate: none until the trigger fires · hash: n/a · tier: n/a · trigger: an authored claimant row
- **ED-651** · STILL-NEEDED · rows E4:111 · carry-forward: E4 §Carry-forward, line 833 · lane's target: FA · held residue, no work (v12 'held and leave' list), trigger unchanged · gate: none until the trigger fires · hash: n/a · tier: n/a · trigger: Jordan names the seat
- **ED-653** · STILL-NEEDED · rows E4:112 · carry-forward: E4 §Carry-forward, line 839 · lane's target: FA · held residue, no work (v12 'held and leave' list), trigger unchanged · gate: none until the trigger fires · hash: n/a · tier: n/a · trigger: an authored banneret-su…
- **G-18** · STILL-NEEDED · rows E4:204 · carry-forward: E4 §Carry-forward, line 911 · lane's target: FA · held residue, no work (v12 'held and leave' list), trigger unchanged · gate: none until the trigger fires · hash: n/a · tier: n/a · trigger as stated
- **§2 an emerged creed's `seize` ** · STILL-NEEDED · rows E4:583 · carry-forward: E4 (no block; the table row is the carry) · lane's target: FA · held residue, no work (v12 'held and leave' list), trigger unchanged · gate: none until the trigger fires · hash: n/a · tier: n/a
- **§2 the Cardinal electorate** · STILL-NEEDED · rows E4:585 · carry-forward: E4 (no block; the table row is the carry) · lane's target: FA · held residue, no work (v12 'held and leave' list), trigger unchanged · gate: none until the trigger fires · hash: n/a · tier: n/a


### Lane SE (24 items)

**B12-world-motion-and-ground**

- **CR-40** · STILL-NEEDED · rows E1:113, E2:46, E4:369 · carry-forward: E1 §Carry-forward, line 1146; E2 §Carry-forward, line 490; E4 §Carry-forward, line 1446 · lane's target: SE · B03-hygiene (hash EQUAL data edit) · gate: card control (`build_realm(0)` hash equal; freshness-gate pin line) · gate: `python -c "import yaml; d=yaml.safe_load(ope…
- **CP-T08-01** · STILL-NEEDED · rows E1:114, E4:301, E4:674, E5:43 · carry-forward: E1 §Carry-forward, line 1157; E4 §Carry-forward, line 1446; E5 Block C13 · lane's target: SE · B12 first (before `07_SE_capability_rate_B`) · shipped `labour_mode` off · gate: `engine/season/tests/test_labour_yield.py` on `harness/scarce.build`: (a) arm on, w…
- **CP-T08-03** · STILL-NEEDED · rows E1:115, E4:303, E5:99 · carry-forward: E1 §Carry-forward, line 1202; E4 §Carry-forward, line 1481; E5 Block C42 · lane's target: SE · B12 after CP-T08-01 · gate: `test_store_spoil.py`: with grain at 100 per-mille, 200 grain becomes 180 at the next MATTER and salt at 0 per-mille is unchanged; the c…
- **CP-T08-02** · STILL-NEEDED · rows E1:116, E4:302, E4:675 · carry-forward: E1 §Carry-forward, line 1229; E4 §Carry-forward, line 1464 · lane's target: SE · B12 · amended per `07_SE_ground_and_granaries` R1 · gate: `test_endowment.py`: under `ground`, a settlement whose coords fall inside a mountain polygon gets a seam …
- **CP-T08-05** · STILL-NEEDED · rows E1:117, E4:305, E4:677, E5:46 · carry-forward: E1 §Carry-forward, line 1258; E4 §Carry-forward, line 1508; E5 Block C15 · lane's target: SE · B12 · paper until an `offer` has a producer · gate: `test_price.py` on a hand-built two-town world: the town short of grain prices grain above the town in surplus; …
- **CP-T08-06** · STILL-NEEDED · rows E1:118, E4:306, E4:678, E5:47 · carry-forward: E1 §Carry-forward, line 1288; E4 §Carry-forward, line 1528; E5 Block C16 · lane's target: SE · B12/B38 · stop rule kept · gate: `test_unrest.py`: a cohort holding three `starving` hunger claims about its town reads the band the floors give; the same claims ab…
- **CP-T08-08** · STILL-NEEDED · rows E1:120, E4:308, E4:680, E5:49 · carry-forward: E1 §Carry-forward, line 1350; E4 §Carry-forward, line 1567; E5 Block C18 · lane's target: SE · B12 · gate: `test_upkeep_question.py` on `scarce.governed`: an obligee sworn three seasons ago puts a `transfer` Candidate through the seat into the holder's ques .…
- **CP-T08-04** · STILL-NEEDED · rows E1:123, E4:304, E4:676, E5:45 · carry-forward: E1 §Carry-forward, line 1379; E4 §Carry-forward, line 1491; E5 Block C14 · lane's target: SE · B12 after B07 (task draw) · amended: a task row · gate: `test_craft.py`: a person at a mint whose rung holds ore 10 crafts coin by the recipe and the rung's ore fal…
- **IN-52** · STILL-NEEDED · rows E1:124, E2:103, E3:357, E4:476 · carry-forward: E1 §Carry-forward, line 1408; E2 §Carry-forward, line 927; E3 (no block; the table row is the carry) · lane's target: SE · B22 after `07_SE_campaign_supply_and_muster` · declared mover on flip · gate: EXIT "with it on, in a seeded season a side's fielded troops are bounded by its levied… · **settled:** IN-52: `U5d_SE_owed_edits.md:61` keeps 'plan IN-52's flip entry'; three lanes carry it.
- **CR-22, H-11, H-125** · STILL-NEEDED · rows E1:162, E2:28, E3:449, E3:552, E4:351, E6:42 … · carry-forward: E1 §Carry-forward, line 2433; E2 §Carry-forward, line 239; E3 §Carry-forward, line 677 · lane's target: SE · B12 after CP-T08-02 · amended · gate: at the shipped arm `hunger_by_settlement` reads a band below `fed` after season 1; planted failure: `want = Person.weight` (pe… · **settled:** H-11: the register row's fixture is shipped, but its closure is v11 CR-22's MEASURE-then-BUILD (E3 Block 16); one item with CR-22 (SE, B12).
- **CR-49** · STILL-NEEDED · rows E1:172, E2:73, E4:378 · carry-forward: E1 §Carry-forward, line 2584; E2 §Carry-forward, line 618; E4 §Carry-forward, line 2229 · lane's target: SE/IN · B12 · gate: card exit · gate: `aperture 3 s`: `exchange.made` at least once from a computed act; `confer` and `oblige` re-read at the realm line against their pr…
- **CR-67** · STILL-NEEDED · rows E1:224, E2:91, E4:397 · carry-forward: E1 §Carry-forward, line 3652; E2 §Carry-forward, line 816; E4 §Carry-forward, line 2704 · lane's target: SE/SC · design-first after CR-58 · gate: design approved by ED-1094's merge default unless held back. · hash: none at the design step (E). · tier: second tier (design).
- **H-171** · STILL-NEEDED · rows E3:597, E7:69 · carry-forward: E3 (no block; the table row is the carry); E7 §Carry-forward, line 188 · lane's target: — · **settled:** register row governs (E7:69 STILL-NEEDED); E3 convention 6 defers the register row to E6-E8.
- **DEF-7** · STILL-NEEDED · rows E4:592 · carry-forward: E4 §Carry-forward, line 4354 · lane's target: SE · with IN-52
- **P14 B10-16 gates, IN-52, `requ** · MISSING-DEP · rows E5:42 · carry-forward: E5 Block C12 · lane's target: dep: a seat-channel stock report or residence-ladder reach (H-163 3(a)); owner none · whoever lands SE B12; design choice, not mine. Block C12

**B11F1-flow-se (NEW, §3)**

- **CR-107** · STILL-NEEDED · rows E1:188, E4:436, E5:160, E5:161 · carry-forward: E1 §Carry-forward, line 2937; E4 §Carry-forward, line 3013; E5 Block F4 · lane's target: IN/SE · B11F1 before B38 · loader EQUAL; content commit a mover · hash: none from the loader change alone; the authored rows move ev ... · tier: second tier for the load…
- **P16 section 3.4 territory caps** · STILL-NEEDED · rows E5:172 · carry-forward: E5 (no block; the table row is the carry) · lane's target: SE · design-first, post-F1; UNVERIFIED whether any suite file covers it (`07_SE_*` not searched for caps)

**B33-inst-economy-hands**

- **CP-T08-07** · MISSING-DEP · rows E1:119, E4:307, E4:679, E5:48 · carry-forward: E1 §Carry-forward, line 1318; E4 §Carry-forward, line 1549; E5 Block C17 · lane's target: SE/FA · before B33 · gate: card exit · gate: `test_tax_edict.py` on `harness/scarce.governed`: with a 200 per-mille edict and `phase_in` 2, the holder's `levy_due` quest… · **settled:** CP-T08-07: its gate H-163 limit 3(a) has no owner in the tree or any proposal (E5:48); owner FA/SE; the tithe and tax kit files wait on it.

**design-first item owed by A-109 (SE+FI; a proposal first)**

- **H-325, H-326** · MISSING-DEP · rows E8:117, E8:119 · carry-forward: E8 CF-E8-5; E8 §Carry-forward, line 243 · lane's target: SE+FI lanes: a design proposal first (owner Jordan's scope call), then a verb row and a `Person` known-places field; CF-E8-5 · **settled:** re-cited, A-109: no general exploration act (the exploration-act part is SUPERSEDED: travel and inquiry cover ordinary discovery; H-327's arrival-teaches lands in B12). STILL owed: a way to find what is hidden (a concealment rating or withheld claim; a drawn f

**held / LEAVE (no batch until the named trigger fires)**

- **CP-T04-10** · STILL-NEEDED · rows E1:256, E4:277 · carry-forward: E1 §Carry-forward, line 4413; E4 §Carry-forward, line 1104 · lane's target: HELD list; SE · gate: TS's per position (TS2 §7), plus: a disbanded stock is re-levyable next season and draws nothing from the larder the · hash: E · tier: per home (Si…
- **H-39** · STILL-NEEDED · rows E3:470, E6:63 · carry-forward: E3 (no block; the table row is the carry); E6 (no block; the table row is the carry) · lane's target: — · **settled:** register row governs (E6:63 STILL-NEEDED); E3 convention 6 defers the register row to E6-E8.
- **ED-507** · STILL-NEEDED · rows E4:80 · carry-forward: E4 §Carry-forward, line 737 · lane's target: SE · held residue, no work (v12 'held and leave' list), trigger unchanged · gate: none until the trigger fires · hash: n/a · tier: n/a · trigger: a reader for `poi_catal…
- **ED-610** · STILL-NEEDED · rows E4:101 · carry-forward: E4 §Carry-forward, line 809 · lane's target: SE · held residue, no work (v12 'held and leave' list), trigger unchanged · gate: none until the trigger fires · hash: n/a · tier: n/a · trigger: Jordan names the heir, …
- **§2 the `heritage` member of `p** · STILL-NEEDED · rows E4:584 · carry-forward: E4 (no block; the table row is the carry) · lane's target: SE · held residue, no work (v12 'held and leave' list), trigger unchanged · gate: none until the trigger fires · hash: n/a · tier: n/a · trigger: a writer of person-pred…


### Lane WR (49 items)

**B12-world-motion-and-ground**

- **CP-T10-01** · STILL-NEEDED · rows E1:154, E4:320, E4:691, E5:60 · carry-forward: E1 §Carry-forward, line 2287; E4 §Carry-forward, line 965; E5 Block C27 · lane's target: WR · B12 first · `IS_B3_FA_SE_WR_GO_part2.md:116` BLOCKED on it · gate: (`engine/season/tests/test_route_leg.py`, new): S-001 → S-002 prices 1 point; S-001 → S-013 (Asch…
- **CP-T10-03** · STILL-NEEDED · rows E1:157, E4:323, E4:693, E5:63 · carry-forward: E1 §Carry-forward, line 2345; E4 §Carry-forward, line 1786; E5 Block C29 · lane's target: WR · B12 after `seasons_of_year` · hash EQUAL as shipped · gate: (`test_calendar.py`): at `year_length` 4, tick 3 is season 3; a weight-2 cohort wants grain 6 at a winte…
- **CL-EVENTS** · STILL-NEEDED · rows E1:158, E2:60, E4:233 · carry-forward: E1 §Carry-forward, line 2381; E2 §Carry-forward, line 241; E4 §Carry-forward, line 965 · lane's target: WR · B12 · before CR-73 and `09_WR_B_weather_with_memory_and_the_year` · amended by A-54 · hash: M (commit 2; commits 1, 3 and 4 EQUAL) · **settled:** CL-EVENTS (2): `U5_FINDINGS_CLOSURE_U5d.md:579` carries 'plan B10-18 CL-EVENTS (2) with `09_WR_B_weather_with_memory_and_the_year`' (amended by A-54), so the plan position survives.
- **CP-T10-02** · STILL-NEEDED · rows E5:62 · carry-forward: E5 Block C28 · lane's target: WR · B12 with `16_PESSIMIST_WR_A`, only if its draw keys on it. Block C28

**B21s-strife-supply (NEW, §3)**

- **CR-73** · STILL-NEEDED · rows E1:160, E4:402, E5:154 · carry-forward: E1 §Carry-forward, line 2403; E4 §Carry-forward, line 2729; E5 Block F1 · lane's target: WR/IN · B12 after CL-EVENTS (2) · hash EQUAL · gate: three hand-built one-territory worlds: a lowest-member draw with a settlement's larder at its floor logs a shortfall…

**B37p-wr-kin-and-life (NEW, §3)**

- **CP-T10-06** · STILL-NEEDED · rows E1:151, E4:326, E4:695, E5:65 · carry-forward: E1 §Carry-forward, line 2162; E4 §Carry-forward, line 1815; E5 Block C30 · lane's target: WR · B39 prerequisite (B12/B37 neighbour) · gate: card exit · gate: (`test_kin.py`): the authored Princess–Doux pair gives two kin edges at build; the Doux dies far away…
- **CP-T10-07** · STILL-NEEDED · rows E1:152, E4:327, E4:696, E4:697, E5:66, E5:67 · carry-forward: E1 §Carry-forward, line 2203; E4 §Carry-forward, line 1835; E5 Block C31 · lane's target: WR · B37 or B39 · after CP-T10-06 · gate: (`test_estate.py`): a holder of a Record and a landholding dies far from his spouse; `w._estates` records both; she · hash: M ·…
- **CP-T10-09** · STILL-NEEDED · rows E1:153, E4:329, E4:700, E5:70 · carry-forward: E1 §Carry-forward, line 2256; E4 §Carry-forward, line 1887; E5 Block C35 · lane's target: WR · after CP-T10-06 · gate: (`test_deeds_to_me.py`): A tends B → B's regard of A rises by `patient_gain` beyond the lean, while C (same pursuits, · hash: M · tier: per …
- **CP-T10-04** · STILL-NEEDED · rows E1:164, E4:324, E5:102 · carry-forward: E1 §Carry-forward, line 2459; E4 §Carry-forward, line 1805; E5 Block C34 · lane's target: WR · B12/B37 after `U5d_WR_owed_edits` §3 · gate: card exit · gate: (`test_recovery.py`): a fed cohort at 450 rises 50 a season and crosses `limited` (500) upward once, …

**B27-sc-proceedings**

- **G-14** · STILL-NEEDED · rows E4:199 · carry-forward: E4 §Carry-forward, line 905 · lane's target: WR · CL-THRUST B4.x, after `determine` executes (U3 B27) and `covenant` executes (see CP-T09-03) · gate: CR-14 pooled census reads both executing · hash: mover
- **TL-B4.1** · STILL-NEEDED · rows E4:224 · carry-forward: E4 §Carry-forward, line 941 · lane's target: WR · see G-14
- **TL-B4.2** · STILL-NEEDED · rows E4:225 · carry-forward: E4 §Carry-forward, line 947 · lane's target: WR · see G-14

**B35-wr-thread**

- **CR-13** · STILL-NEEDED · rows E1:100, E2:26, E4:342 · carry-forward: E1 §Carry-forward, line 723; E2 §Carry-forward, line 221; E4 §Carry-forward, line 869 · lane's target: WR/PC · B35 · re-based on the new module's `leap` · gate: Leap at Partial and Failure each nets 0 Coherence; Weaving keeps penalty · gate: a pinned test beside `test_thr…
- **CP-T07-02, H-47, H-62** · STILL-NEEDED · rows E1:101, E3:478, E3:493, E4:291, E4:664, E4:665 … · carry-forward: E1 §Carry-forward, line 749; E3 (no block; the table row is the carry); E4 §Carry-forward, line 1269 · lane's target: WR · B35 first item (IS-B3-WR-01) · gate: `test_threadwork_loop.py` + `aperture 1 0` thread row executed · gate: A planted practitioner's `weave` at seed s writes exactl… · **settled:** register row governs (E6:71 STILL-NEEDED); E3 convention 6 defers the register row to E6-E8.
- **CP-T07-03** · STILL-NEEDED · rows E1:102, E4:292, E4:667, E5:35 · carry-forward: E1 §Carry-forward, line 789; E4 §Carry-forward, line 1307; E5 Block C6 · lane's target: WR · B35 · gate: Paired seeds, one planted Site woven and its twin not: after one MATTER the woven Site's condition is unchanged and · hash: M · tier: per home (Size lin…
- **CP-T07-05** · STILL-NEEDED · rows E1:103, E4:294, E4:669, E5:37 · carry-forward: E1 §Carry-forward, line 849; E4 §Carry-forward, line 1343; E5 Block C8 · lane's target: WR · B35 · gate: A planted practitioner contained at a locked Site recovers 0 over a season; moved to an unlocked Site he recovers 6. · hash: E · tier: per home (Size li…
- **CP-T07-09** · STILL-NEEDED · rows E1:104, E4:298, E4:672, E5:41 · carry-forward: E1 §Carry-forward, line 877; E4 §Carry-forward, line 1409; E5 Block C11 · lane's target: WR · B35 · gate: A planted orthodox witness co-located with an executed `weave` gains a scar on `solmund_orthodoxy`; with the witness · hash: M · tier: per home (Size li…
- **CP-T07-04** · STILL-NEEDED · rows E1:105, E4:293, E4:668, E5:36 · carry-forward: E1 §Carry-forward, line 911; E4 §Carry-forward, line 1325; E5 Block C7 · lane's target: WR · B35 · gate: At `self_mend_ob_step` 4, a planted practitioner at resting 2 does not reach resting 0 within one season in more than a · hash: M · tier: per home (Size…
- **CP-T07-06** · STILL-NEEDED · rows E1:106, E4:295, E5:96 · carry-forward: E1 §Carry-forward, line 963; E4 §Carry-forward, line 1362; E5 Block C39 · lane's target: WR · B35 · gate: A practitioner at elastic 4 who takes no thread act for one season reads band Stable at the next deliberation and · hash: M · tier: per home (Size line)
- **CP-T07-07** · STILL-NEEDED · rows E1:107, E4:296, E4:670, E5:38 · carry-forward: E1 §Carry-forward, line 994; E4 §Carry-forward, line 1372; E5 Block C9 · lane's target: WR · B35 · gate: At `(0,1,1,2)` a planted practitioner at resting 2 (Dissonant) has a budget one less than his resting-0 twin at the · hash: E · tier: per home (Size lin…
- **CP-T07-10** · STILL-NEEDED · rows E1:108, E4:299, E5:97 · carry-forward: E1 §Carry-forward, line 1030; E4 §Carry-forward, line 1426; E5 Block C40 · lane's target: WR · B35 · gate: A planted practitioner reads a woven Site and holds a Claim naming the weave; a reader at TS · hash: M · tier: per home (Size line)
- **CP-T07-08** · STILL-NEEDED · rows E1:109, E4:297, E4:671, E5:40 · carry-forward: E1 §Carry-forward, line 1065; E4 §Carry-forward, line 1391; E5 Block C10 · lane's target: WR · B35 · amended: the crossing is drawn · gate: A planted practitioner driven 0 → crossing by three Structural lock Failures (T07 §2.3) emits `coherence.crossed` · has…
- **CP-T07-11** · STILL-NEEDED · rows E1:110, E4:300, E5:98 · carry-forward: E1 §Carry-forward, line 1095; E4 §Carry-forward, line 1436; E5 Block C41 · lane's target: WR · B35 · gate: A planted `lock` on a warded Site rolls the opposed resolver (both sides charged); on an unwarded · hash: M · tier: per home (Size line)
- **WR-01** · STILL-NEEDED · rows E1:112, E2:101, E3:376, E4:539 · carry-forward: E1 §Carry-forward, line 1120; E2 §Carry-forward, line 909; E3 (no block; the table row is the carry) · lane's target: WR · B35 after IS-B3-WR-01 · gate: card exit; moves hashes only through the working · gate: EXIT "observed when a working with a cost runs in the season (unobservable at… · **settled:** WR-01: three lanes and IS-B3-WR-01 carry it (after `09_WR_B_threadwork_session_and_practitioner` edits 1-2); E3's cite was a head read.
- **ER-GF10** · STILL-NEEDED · rows E3:422 · carry-forward: E3 Block 8 · lane's target: WR/PC, B35; edit set that function; gate: `ts_minimum` honoured or the docstring corrected; tier haiku. Block 8.
- **ED-WR-0005** · STILL-NEEDED · rows E4:181, E4:567 · carry-forward: E4 §Carry-forward, line 869 · lane's target: WR · with CR-13, U3 B35 (first item) · see CR-13
- **G-21** · STILL-NEEDED · rows E4:207 · carry-forward: E4 §Carry-forward, line 923 · lane's target: WR · with WR-01 (U3 B35) · TL axis J stays out until a source exists

**held / LEAVE (no batch until the named trigger fires)**

- **NM-W6** · STILL-NEEDED · rows E1:213, E2:53, E4:487 · carry-forward: E1 §Carry-forward, line 3531; E2 §Carry-forward, line 508; E4 §Carry-forward, line 4002 · lane's target: HELD list; WR · hash: E
- **NM-W7** · STILL-NEEDED · rows E1:214, E2:54, E4:488 · carry-forward: E1 §Carry-forward, line 3560; E2 §Carry-forward, line 508; E4 §Carry-forward, line 4014 · lane's target: HELD list; WR · hash: E
- **NM-W8** · STILL-NEEDED · rows E1:215, E2:55, E4:489 · carry-forward: E1 §Carry-forward, line 3570; E2 §Carry-forward, line 508; E4 §Carry-forward, line 4026 · lane's target: HELD list; WR · hash: E
- **CL-THRUST** · STILL-NEEDED · rows E1:221, E2:65 · carry-forward: E1 §Carry-forward, line 2392; E2 §Carry-forward, line 529 · lane's target: HELD list; WR · hash: E
- **ED-595** · STILL-NEEDED · rows E4:86 · carry-forward: E4 §Carry-forward, line 749 · lane's target: WR · held residue, no work (v12 'held and leave' list), trigger unchanged · gate: none until the trigger fires · hash: n/a · tier: n/a · trigger: a Jordan-authored arc l…
- **ED-596** · STILL-NEEDED · rows E4:87 · carry-forward: E4 §Carry-forward, line 755 · lane's target: WR · held residue, no work (v12 'held and leave' list), trigger unchanged · gate: none until the trigger fires · hash: n/a · tier: n/a · trigger as ED-595
- **ED-597** · STILL-NEEDED · rows E4:88 · carry-forward: E4 §Carry-forward, line 761 · lane's target: WR · held residue, no work (v12 'held and leave' list), trigger unchanged · gate: none until the trigger fires · hash: n/a · tier: n/a · trigger as ED-595
- **ED-598** · STILL-NEEDED · rows E4:89 · carry-forward: E4 §Carry-forward, line 767 · lane's target: WR · held residue, no work (v12 'held and leave' list), trigger unchanged · gate: none until the trigger fires · hash: n/a · tier: n/a · trigger as ED-595
- **ED-599** · STILL-NEEDED · rows E4:90 · carry-forward: E4 §Carry-forward, line 773 · lane's target: WR · held residue, no work (v12 'held and leave' list), trigger unchanged · gate: none until the trigger fires · hash: n/a · tier: n/a · trigger as ED-595
- **ED-601** · STILL-NEEDED · rows E4:91 · carry-forward: E4 §Carry-forward, line 779 · lane's target: WR · held residue, no work (v12 'held and leave' list), trigger unchanged · gate: none until the trigger fires · hash: n/a · tier: n/a · trigger as ED-595; Pretender wit…
- **ED-602** · STILL-NEEDED · rows E4:92 · carry-forward: E4 §Carry-forward, line 785 · lane's target: WR · held residue, no work (v12 'held and leave' list), trigger unchanged · gate: none until the trigger fires · hash: n/a · tier: n/a · trigger as ED-595
- **G-04** · STILL-NEEDED · rows E4:188, E4:189 · carry-forward: E4 §Carry-forward, line 881 · lane's target: WR · with NM-W4 · held residue, no work (v12 'held and leave' list), trigger unchanged · gate: none until the trigger fires · hash: n/a · tier: n/a
- **G-09** · STILL-NEEDED · rows E4:194 · carry-forward: E4 §Carry-forward, line 893 · lane's target: WR · held residue, no work (v12 'held and leave' list), trigger unchanged · gate: none until the trigger fires · hash: n/a · tier: n/a · trigger: Jordan authors the rows…
- **G-10** · STILL-NEEDED · rows E4:195 · carry-forward: E4 §Carry-forward, line 899 · lane's target: WR · held residue, no work (v12 'held and leave' list), trigger unchanged · gate: none until the trigger fires · hash: n/a · tier: n/a · trigger as G-09
- **G-24** · STILL-NEEDED · rows E4:210 · carry-forward: E4 §Carry-forward, line 929 · lane's target: WR · CL-THRUST B6.n axis H · see TL B6.n
- **G-26** · STILL-NEEDED · rows E4:212 · carry-forward: E4 §Carry-forward, line 935 · lane's target: WR · held residue, no work (v12 'held and leave' list), trigger unchanged · gate: none until the trigger fires · hash: n/a · tier: n/a · trigger: Jordan authors the rows
- **TL-B6.n** · MISSING-DEP · rows E4:228 · carry-forward: E4 §Carry-forward, line 959 · lane's target: WR · owner Jordan (content) · needs: `thrust_axes` rows with referent-bearing goal rows; arc rule: a ladder names its source arc and draws from the first two `ENDINGS_CL…
- **§2 the deed lie (H-198 rule (i** · STILL-NEEDED · rows E4:577 · carry-forward: E4 (no block; the table row is the carry) · lane's target: WR · held residue, no work (v12 'held and leave' list), trigger unchanged · gate: none until the trigger fires · hash: n/a · tier: n/a
- **§2 the Goldenfurt deck (28 car** · STILL-NEEDED · rows E4:580 · carry-forward: E4 (no block; the table row is the carry) · lane's target: WR · held residue, no work (v12 'held and leave' list), trigger unchanged · gate: none until the trigger fires · hash: n/a · tier: n/a · trigger: a named card passes the…
- **§2 the eleven named cards** · STILL-NEEDED · rows E4:581 · carry-forward: E4 (no block; the table row is the carry) · lane's target: WR · held residue, no work (v12 'held and leave' list), trigger unchanged · gate: none until the trigger fires · hash: n/a · tier: n/a
- **§2 the arcs (55 numbers, 58 ar** · STILL-NEEDED · rows E4:582 · carry-forward: E4 (no block; the table row is the carry) · lane's target: WR · held residue, no work (v12 'held and leave' list), trigger unchanged · gate: none until the trigger fires · hash: n/a · tier: n/a (standing rule)
- **DEF-3** · STILL-NEEDED · rows E4:588 · carry-forward: E4 §Carry-forward, line 4342 · lane's target: WR · held residue, no work (v12 'held and leave' list), trigger unchanged · gate: none until the trigger fires · hash: n/a · tier: n/a · trigger: milestone M2


### Lane SC (21 items)

**B05-one-roll**

- **H-199** · STILL-NEEDED · rows E3:270, E7:97 · carry-forward: E3 §Carry-forward, line 669; E7 (no block; the table row is the carry) · lane's target: SC/CHAR, B05 (with `U5c_SC_one_obstacle_form`) or B10; edit set `decision/options.py::refracted_confidence`, `remove_weight` reader; gate: one ladder for one quantity, t… · **settled:** H-199: the full `cite:` (B-P Phase 1) records two functions of one ordinal (`world_q.remove_weight` `(K-k)/K` against `refracted_confidence` `k/(K-1)`): two ladders for one quantity, an S defect (CLAUDE.md §0.06); ladder step 5 picks one spacing; E3 Block 12 c

**B24-sc-hearing**

- **SC-02** · STILL-NEEDED · rows E1:250, E2:99, E4:532 · carry-forward: E1 §Carry-forward, line 3823; E2 §Carry-forward, line 892; E4 §Carry-forward, line 3000 · lane's target: SC · slot by R8 into B24 (before the evidence cycle) · gate: v9 states none. · hash: none stated.
- **H-311** · STILL-NEEDED · rows E8:103 · carry-forward: E8 §Carry-forward, line 220 · lane's target: SC/FI lane, B24 (`person_q.proof_kind`); CF-E8-4

**B24a-sc-outside-the-room (NEW, §3)**

- **CR-58** · STILL-NEEDED · rows E1:178, E2:82, E4:387 · carry-forward: E1 §Carry-forward, line 2662; E2 §Carry-forward, line 654; E4 §Carry-forward, line 2479 · lane's target: SC · after B24 · gate: seeds 0-2: an owner's act is refused for want of a held resolution, its refusal kind is `<verb>.unlicensed`, and a convening follows from it above…
- **CR-59** · STILL-NEEDED · rows E1:179, E2:83, E4:388 · carry-forward: E1 §Carry-forward, line 2688; E2 §Carry-forward, line 672; E4 §Carry-forward, line 2504 · lane's target: SC · after B24 · narrowed by A-39 · gate: a hand-built world: a crown seat voids a church `detain`; the same seat is refused on a restraint under a row with no `appeal_t…
- **CR-60** · STILL-NEEDED · rows E1:180, E2:84, E4:389 · carry-forward: E1 §Carry-forward, line 2714; E2 §Carry-forward, line 690; E4 §Carry-forward, line 2529 · lane's target: SC · after B24 · gate: seeds 0-2: a church seat opens a case on a resident of a territory other than T9; the same accused under two rows gets two benches; the King is ne…
- **CR-61** · STILL-NEEDED · rows E1:181, E2:85, E4:391 · carry-forward: E1 §Carry-forward, line 2740; E2 §Carry-forward, line 708; E4 §Carry-forward, line 2554 · lane's target: SC · before B24's evidence cycle (IS-B2-SC-02 is its first commit) · gate: seeds 0-2: `docket_named_arrangement` above 0; burning the case file stalls `determine` and a …
- **CR-62** · STILL-NEEDED · rows E1:182, E2:86, E4:392 · carry-forward: E1 §Carry-forward, line 2766; E2 §Carry-forward, line 726; E4 §Carry-forward, line 2579 · lane's target: SC · after B24 · amended · gate: a hand-built hearing and a seeded sweep: with the concession reward through the obstacle, deny is not best alone in more than 6 of 9 cel…
- **CR-64** · STILL-NEEDED · rows E1:183, E2:88, E4:394 · carry-forward: E1 §Carry-forward, line 2792; E2 §Carry-forward, line 746; E4 §Carry-forward, line 2616 · lane's target: SC · after B24 · gate: a hand-built hearing: a forum plea changes the item's row with no second case; the sitting bench keeps the matter when no royal party is involved.…
- **CR-63** · STILL-NEEDED · rows E1:184, E2:87, E4:393 · carry-forward: E1 §Carry-forward, line 2818; E2 §Carry-forward, line 744; E4 §Carry-forward, line 2604 · lane's target: SC · after B24 · gate: each of the five above 0 at seeds 0-2 · gate: seeds 0-2, an `aperture`-style run: each of the five is taken above 0; `compliance.given` and `compl…

**B28-social-verbs**

- **H-286** · STILL-NEEDED · rows E8:78 · carry-forward: E8 §Carry-forward, line 183 · lane's target: SC lane, join B28 (it edits the `argue` row); editorial, no hash; CF-E8-3

**B27-sc-proceedings**

- **CR-65** · STILL-NEEDED · rows E1:186, E2:89, E4:395 · carry-forward: E1 §Carry-forward, line 2875; E2 §Carry-forward, line 780; E4 §Carry-forward, line 2654 · lane's target: SC · design-first after CR-60 · HELD on P4 Q2 · gate: design approved by ED-1094's merge default unless held back; a built index shows an L ≡ 1 arm with no draw differen…
- **CR-66** · STILL-NEEDED · rows E1:223, E2:90, E4:396 · carry-forward: E1 §Carry-forward, line 3626; E2 §Carry-forward, line 798; E4 §Carry-forward, line 2679 · lane's target: SC · design-first after CR-60 · gate: design approved by ED-1094's merge default unless held back. · hash: none at the design step (E). · tier: second tier (design).
- **SC-07** · STILL-NEEDED · rows E1:242, E2:129, E3:365, E4:536 · carry-forward: E1 §Carry-forward, line 4019; E2 §Carry-forward, line 1192; E3 (no block; the table row is the carry) · lane's target: LEAVE list · gate: EXIT P-4: "a carried-and-vetoed motion persists as a citable record (`02_against_precedent.md:83`)"; V-4: "two persons differing only in an acquired t… · **settled:** SC-07: waits on CR-36/CR-37 (`U5_FINDINGS_CLOSURE_U5c.md` row 108); E3's cite was a head read.
- **A1-87, H-222** · STILL-NEEDED · rows E3:182, E3:293, E7:120 · carry-forward: E3 §Carry-forward, line 663; E7 (no block; the table row is the carry) · lane's target: SC, B27 (with `16_PESSIMIST_SC_B_one_reader_of_a_ledger`); edit set `loop/witness.py` (a deposit of person-predicate claims through the channels); gate: `standing_of` no… · **settled:** H-222: E7's own evidence names the missing producer ('irrelevant until a `person_predicates` producer exists'); v11 A1-87's writer through the channels is owed (E3 Block 9).
- **H-219** · STILL-NEEDED · rows E3:290, E7:117 · carry-forward: E3 (no block; the table row is the carry); E7 §Carry-forward, line 208 · lane's target: — · **settled:** register row governs (E7:117 STILL-NEEDED); E3 convention 6 defers the register row to E6-E8.
- **H-227** · STILL-NEEDED · rows E3:298, E7:125 · carry-forward: E3 §Carry-forward, line 673; E7 §Carry-forward, line 213 · lane's target: SC/IN, B27 (`05_SC_arrangement_rows_that_bind`); edit set `data/rosters.py` `RECORD_REFERENT_KINDS`/`writs_held`; gate: a `commit` forms on a docketed petition in a hand…
- **H-153** · STILL-NEEDED · rows E3:580, E7:50 · carry-forward: E3 (no block; the table row is the carry); E7 §Carry-forward, line 178 · lane's target: — · **settled:** register row governs (E7:50 STILL-NEEDED); E3 convention 6 defers the register row to E6-E8.
- **H-154** · STILL-NEEDED · rows E3:581, E7:51 · carry-forward: E3 (no block; the table row is the carry); E7 §Carry-forward, line 178 · lane's target: — · **settled:** register row governs (E7:51 STILL-NEEDED); E3 convention 6 defers the register row to E6-E8.
- **H-173** · STILL-NEEDED · rows E3:599, E7:71 · carry-forward: E3 §Carry-forward, line 669; E7 (no block; the table row is the carry) · lane's target: SC, B27 (`05_SC_arrangement_rows_that_bind`); edit set the four readers of `oblige` kind in `queries/`; gate: a seeded reading of the four consequences with `determine` … · **settled:** H-173: the delegated ruling (no distinct reading) closes the design; v11's measurement of the four consequences, whose trigger has fired (`determine` executes), is owed and nothing supersedes it (E3 Block 12); SC, B27.

**held / LEAVE (no batch until the named trigger fires)**

- **§2 social-contest wording rows** · STILL-NEEDED · rows E4:573 · carry-forward: E4 (no block; the table row is the carry) · lane's target: SC · held residue, no work (v12 'held and leave' list), trigger unchanged · gate: none until the trigger fires · hash: n/a · tier: n/a


### Lane FI (10 items)

**B11-fi-readers**

- **CP-T06-09** · STILL-NEEDED · rows E1:91, E4:290, E4:662, E4:663, E5:30 · carry-forward: E1 §Carry-forward, line 533; E4 §Carry-forward, line 1114; E5 Block C2 · lane's target: FI · B11-fi-readers · after CR-29 · gate: T06 §3's cover probe re-run: the bystander holds `(p_other, record.forged, True)`, not `(rec:cv, record.forged, True)`; a `docu…
- **CR-29, H-214, H-224** · STILL-NEEDED · rows E1:92, E2:31, E3:285, E3:295, E4:358, E7:112 … · carry-forward: E1 §Carry-forward, line 554; E2 §Carry-forward, line 274; E3 §Carry-forward, line 667 · lane's target: FI/IN · B11-fi-readers, first item · gate: speakerless `told_by` falls to the kinds the roster carries; `tenure.closed`/`person.died` still reach the realm · gate: the s… · **settled:** H-224: the window-arm measurement rides CR-29's exit (E3 Block 11); the chooser reader is `02_CHAR_voices_and_the_room.md` Edit 5 (B10).
- **CP-T06-01** · STILL-NEEDED · rows E1:93, E4:283, E4:655 · carry-forward: E1 §Carry-forward, line 565; E4 §Carry-forward, line 1114 · lane's target: FI · B11 · amended text: PFI-C edits 1-3 + `08_FI_01` edits 2-5 · gate: (1) `test_fi03_trail.py::trail_world` plus a Site at R: p_other sabotages it with nobody at R; p_…
- **CP-T06-03, CP-T06-04, H-314** · STILL-NEEDED · rows E1:94, E1:95, E4:285, E4:286, E4:657, E4:658 … · carry-forward: E1 §Carry-forward, line 606; E1 §Carry-forward, line 628; E4 §Carry-forward, line 1151 · lane's target: FI · B11 · gate: `test_fi03_trail.py::test_a_partial_find_closes_the_same_trail_to_a_later_better_one` (`:342`) is inverted: Partial, then Success, on one Record depos .…
- **CP-T06-02** · STILL-NEEDED · rows E1:96, E4:284, E4:656 · carry-forward: E1 §Carry-forward, line 652; E4 §Carry-forward, line 1133 · lane's target: FI · B11 · after CP-T06-01, -04 · gate: `trail_world`: p_other forges at R at tick 0 while p_high is at S; at tick 1 p_high moves to R and `surveil`s it. Success deposit…
- **CP-T06-07** · STILL-NEEDED · rows E1:97, E4:288, E4:660, E4:661, E5:29 · carry-forward: E1 §Carry-forward, line 676; E4 §Carry-forward, line 1205; E5 Block C1 · lane's target: FI · B11 · after CP-T06-02, -09 · gate: Hand-built: framer F takes a borrowed-name cover naming V, then does an act at R, where only C stands, whose kind reaches a dista…
- **ED-IN-0298** · STILL-NEEDED · rows E3:334 · carry-forward: E3 §Carry-forward, line 667 · lane's target: See A2-43 (Block 11).

**B25-fi-questioning**

- **CP-T06-05** · STILL-NEEDED · rows E1:98, E4:287, E4:659 · carry-forward: E1 §Carry-forward, line 700; E4 §Carry-forward, line 1114 · lane's target: FI · B25-fi-questioning (+B26 questioning file) · gate: card exit · gate: Hand-built: A and B at R, B holding a claim on X; A interviews B about X in round 1, so B holds…

**B26-fi-inquiry**

- **H-169** · STILL-NEEDED · rows E3:595, E7:67 · carry-forward: E3 (no block; the table row is the carry); E7 §Carry-forward, line 183 · lane's target: — · **settled:** register row governs (E7:67 STILL-NEEDED); E3 convention 6 defers the register row to E6-E8.

**held / LEAVE (no batch until the named trigger fires)**

- **G-03** · STILL-NEEDED · rows E4:186 · carry-forward: E4 §Carry-forward, line 875 · lane's target: FI · held residue, no work (v12 'held and leave' list), trigger unchanged · gate: none until the trigger fires · hash: n/a · tier: n/a · trigger as stated; a hash mover,…


### Lane PC (8 items)

**B14-pc-outcome**

- **CP-T03-06** · STILL-NEEDED · rows E1:86, E4:260, E4:540 · carry-forward: E1 §Carry-forward, line 467; E4 §Carry-forward, line 1074 · lane's target: PC (CHAR) · after B14 (`16_PESSIMIST_PC_C`) and B10 (`02_CHAR_scar_is_a_wound`) · gate: the card's measure at `aperture 2 0` seeds 0-2; CUT if non-zero · hash: M (when b…
- **PC-21** · STILL-NEEDED · rows E1:232, E4:447 · carry-forward: E1 §Carry-forward, line 3838; E4 §Carry-forward, line 3403 · lane's target: PC · design-first at B14/B15 · gate: the file states (1) to (4) with falsifiers: at least, a fighter with a record of fights against a weapon class reads it better than …

**B15-pc-calibration**

- **ED-SC-0001** · STILL-NEEDED · rows E4:171, E4:569 · carry-forward: E4 §Carry-forward, line 863 · lane's target: PC · U3 B15-pc-calibration, as a measurement item · gate: the armour-tier and ability-stacking sweeps run and read (execution artifact: the sweep output at seeds 0-2) · …

**B27-sc-proceedings**

- **GV-G12** · STILL-NEEDED · rows E3:408 · carry-forward: E3 Block 12 · lane's target: PC/SC, B27; edit set none unless `church_standing` is read; gate: `grep church_standing engine/season`; hash EQUAL; tier haiku. Block 12.

**B39-procgen-and-cases**

- **CR-85** · STILL-NEEDED · rows E1:249, E2:35 · carry-forward: E1 §Carry-forward, line 4181; E2 §Carry-forward, line 312 · lane's target: HELD list; PC · slot when the design is approved (ED-IN-0351) · gate: its own falsifier, as the design states it: at the least, a season fight's pool and Ob read the rep…

**held / LEAVE (no batch until the named trigger fires)**

- **CP-T03-10** · STILL-NEEDED · rows E1:87, E4:264, E4:541 · carry-forward: E1 §Carry-forward, line 489; E4 §Carry-forward, line 1084 · lane's target: HELD list only (no batch); trigger unchanged · hash: E · tier: per home (Size line)
- **PC-22** · STILL-NEEDED · rows E1:233, E4:448 · carry-forward: E1 §Carry-forward, line 3864; E4 §Carry-forward, line 3428 · lane's target: PC · design-first after PC-21 · gate: the file states (1) to (7) with falsifiers, at least: a spar leaves both parties' `body` as it was; a person sparring a partner wit…
- **PC-08** · STILL-NEEDED · rows E1:239, E2:127, E3:373, E4:493 · carry-forward: E1 §Carry-forward, line 3967; E2 §Carry-forward, line 1175; E3 (no block; the table row is the carry) · lane's target: LEAVE list; one plan edit · gate: EXIT "`python -m engine.season.harness.register --requirements` — no R-row's measure names any of them; for the channel-leverage residu… · **settled:** PC-08: a named residue with `U5b_PC_residue.md` §6 item 1's clause; 'A-1, A-4' do not carry it.


### Lane MB (7 items)

**B17-mb-scale**

- **ED-1043** · STILL-NEEDED · rows E4:139, E4:566 · carry-forward: E4 §Carry-forward, line 851 · lane's target: MB · U3 B17-mb-scale, as the first commit of its first orchestration.py editor: extract only the functions the editor touches into the `core/` seam · gate: seeded MB gol… · **settled:** re-targeted, A-100: ED-1043 STANDS; its trigger fires at MBA-04 step 0 (MBA-04 edits `orchestration.py`); MB, B19-mb-field-calibration, step 0.

**B19-mb-field-calibration**

- **ED-MB-0045** · STILL-NEEDED · rows E4:160, E4:568 · carry-forward: E4 §Carry-forward, line 857 · lane's target: MB · U3 B19-mb-field-calibration, before `04_MB_cell_hierarchy_as_data` · gate: one owner for per-cell maps named in the entry · hash: EQUAL · tier: sonnet

**B23-land**

- **H-342** · STILL-NEEDED · rows E8:135 · carry-forward: E8 §Carry-forward, line 263 · lane's target: MB lane, B23 (`26_MASS_BATTLE_aggression_and_land.md` edits `_eff_march`); declared mover; CF-E8-6

**held / LEAVE (no batch until the named trigger fires)**

- **CP-T04-04** · STILL-NEEDED · rows E1:254, E4:269 · carry-forward: E1 §Carry-forward, line 4369; E4 §Carry-forward, line 1094 · lane's target: HELD list; MB · gate: A march declared in round r against a holder who surrenders in round r+1 fights no field (the place passes, no body · hash: M · tier: per home (Siz…
- **ED-606** · STILL-NEEDED · rows E4:96 · carry-forward: E4 §Carry-forward, line 791 · lane's target: MB · held residue, no work (v12 'held and leave' list), trigger unchanged · gate: none until the trigger fires · hash: n/a · tier: n/a · trigger: DEF-2 reopens or U3 B30…
- **ED-607** · STILL-NEEDED · rows E4:97 · carry-forward: E4 §Carry-forward, line 797 · lane's target: MB · held residue, no work (v12 'held and leave' list), trigger unchanged · gate: none until the trigger fires · hash: n/a · tier: n/a · trigger as ED-606
- **ED-820** · STILL-NEEDED · rows E4:115 · carry-forward: E4 §Carry-forward, line 845 · lane's target: MB · held residue, no work (v12 'held and leave' list), trigger unchanged · gate: none until the trigger fires · hash: n/a · tier: n/a · trigger: U3 B19/B20 landing a co…


### Lane GO (11 items)

**B03-hygiene**

- **GO-09** · STILL-NEEDED · rows E1:198, E2:107, E4:458 · carry-forward: E1 §Carry-forward, line 3302; E2 §Carry-forward, line 963; E4 §Carry-forward, line 3526 · lane's target: GO · B03 (early landing) · gate: `--check` OK on main before the next registry-editing batch · gate: deleting one key in the JSON reds `--check`; adding a row to `verb_t…
- **GO-11** · STILL-NEEDED · rows E1:200, E2:109, E4:460 · carry-forward: E1 §Carry-forward, line 3352; E2 §Carry-forward, line 997; E4 §Carry-forward, line 3526 · lane's target: GO · B03 (early landing) · gate: `grep -c "key-log" references/module_contracts.yaml` prints 0 (a planted `key-log` row reddens the exit); `python tools/export_compositi…
- **GO-01** · STILL-NEEDED · rows E1:204, E2:122, E3:377, E4:453 · carry-forward: E1 §Carry-forward, line 3403; E2 §Carry-forward, line 1123; E3 §Carry-forward, line 675 · lane's target: GO · B03 (early landing) · gate: `python tools/export_game_constants.py --check` exit 0 after re-export; the version string appears in exactly one machine-read file (`gi…
- **GO-05** · STILL-NEEDED · rows E1:205, E2:123, E3:378, E4:454 · carry-forward: E1 §Carry-forward, line 3414; E2 §Carry-forward, line 947; E3 (no block; the table row is the carry) · lane's target: GO · B03 (early landing) · gate: EXIT "a test that every path the manifest lists exists under `modules/`, beside `test_importing_every_engine_module_pulls_in_no_subsyste… · **settled:** GO-05: an early landing in B03 (`11_GO_port_gate_order_and_coverage.md` §2 drops its GO-01 edge); E3's cite was a head read.

**B41-go-port-gate**

- **GO-10** · STILL-NEEDED · rows E1:199, E2:108, E4:459 · carry-forward: E1 §Carry-forward, line 3327; E2 §Carry-forward, line 980; E4 §Carry-forward, line 3538 · lane's target: GO · B41 · amended · gate: a planted no-op write still yields its refusal Event; `grep` finds no `except NoOpReceipt` left on the fold. CONTROL: seeds 0-2, four seasons,…
- **GO-12** · STILL-NEEDED · rows E1:202, E2:112, E4:461 · carry-forward: E1 §Carry-forward, line 3378; E2 §Carry-forward, line 1015; E4 §Carry-forward, line 3538 · lane's target: GO · B41 (provider list, status roster, missing-contract refusal) / B06 (fallback) · gate: a provider module not on the list reds driver construction; a `None` rng in `m…
- **GO-08** · STILL-NEEDED · rows E1:206, E2:106, E4:457 · carry-forward: E1 §Carry-forward, line 3414; E2 §Carry-forward, line 945; E4 §Carry-forward, line 3538 · lane's target: GO · B41 first item · gate: `--check` reds when one pinned value is edited by hand, and when one registry row changes without a re-build. CONTROL: two `--check` runs und…
- **GO-15** · STILL-NEEDED · rows E1:207, E1:208, E2:113, E4:464 · carry-forward: E1 §Carry-forward, line 3414; E2 §Carry-forward, line 947; E4 §Carry-forward, line 3538 · lane's target: GO · B41 · gate: GO-08's `--check` on the freeze commit; each of B10-20's exit lines (`-03` B10-20: line 1's `engine_series` read and its grep over `README.md`, `refer .…

**held / LEAVE (no batch until the named trigger fires)**

- **GO-06** · MISSING-DEP · rows E1:209, E2:124, E3:379, E4:455 · carry-forward: E1 §Carry-forward, line 3506; E2 §Carry-forward, line 1158; E3 (no block; the table row is the carry) · lane's target: HELD list; Jordan's side · gate: EXIT "here, `python tools/export_game_constants.py --check` exit 0; there, its parity check run against this repository's re-derived con… · **settled:** GO-06: needs a `valoria-game` checkout (another repository); owner the GO lane on Jordan's side (E2:124, E5 H-5).
- **ED-509** · STILL-NEEDED · rows E4:81 · carry-forward: E4 §Carry-forward, line 743 · lane's target: GO · held residue, no work (v12 'held and leave' list), trigger unchanged · gate: none until the trigger fires · hash: n/a · tier: n/a · trigger: GO-01 landed (U3 B03 la…
- **H-5** · MISSING-DEP · rows E5:145 · carry-forward: E5 Block D11 · lane's target: dep: the valoria-game checkout; owner GO lane/Jordan. Block D11
