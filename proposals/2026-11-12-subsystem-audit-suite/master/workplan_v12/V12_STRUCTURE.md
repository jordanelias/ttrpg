# Workplan v12 — the structure: batches, milestones, parts, and what each stage-6 lane is handed

## Status: WORK ORDER (stage 6 of `STAGES.md`, the structure lane's one deliverable; a plan for the lanes that write v12; resolves nothing at runtime, CLAUDE.md §0.05; not canon; deleted when v12 is adopted)

## Read at: branch `ccr-62958c70-0kjhsw`, HEAD `7c37586`, working tree of 2026-11-12 (a shallow clone: `.git/shallow` is present). Producer: Fable, the structure lane of `master/workplan_v12/V12_ORDER.md`. One round.

**Parts.** This file: §0 what this is, §1 the decisions (every inconsistency settled by the five-step ladder), §2 the batch list, §3 the milestones and the requirement map. `V12_STRUCTURE_part2.md`: §4 the part plan and the author assignments, §5 the rules every author lane follows (the item form, what is copied, what is not), §6 the worked example item and the worked batch skeleton. `V12_STRUCTURE_part3.md`: §7 the head parts' content, §8 adoption, the retirement of v11 and the held-back list, §9 the master-findings plan, §10 the check plan and the verdict's questions, §11 what was not checked.

**Paths.** A path with no directory prefix is under `proposals/2026-11-12-subsystem-audit-suite/` (the suite). `U3` is `unified/U3_DEPENDENCY_ORDER.md`; `the intake` is `master/eval/V12_INTAKE.md`; `IS-A` is `master/instructions/IS_A_NINE.md` and `_part2`; `CIP` is `master/CODEBASE_IMPROVEMENT_PROPOSAL.md` and `_part2`; `MBA` is `master/mb_abstraction/MBA_DESIGN_part3.md`; `PCR` is `master/pc_round/PC_ROUND_SPEC_part2.md`; `the lexicon` is `unified/MB_LEXICON_part3.md`; `the skill` is `.claude/skills/methodology-execute/SKILL.md`; `04` is `architecture/meta/04_CODE_ARCHITECTURE.md`.

**Words.** `unified/U1_GLOSSARY.md`. A person's numbers follow A-98 (attribute, skill, skill score, martial skill, derived score). Armies follow A-99 and the lexicon (army, unit, army formation, unit formation; no size words). A *lap* is one pass of the season's scene budget; a *round* is one engagement of a fight (A-101). A *batch* is one handle with one close (RULED 2026-11-06). An *item* is one content-owner entry that lands as one commit. A *wave* is a dependency level; a *step* is a slot of the lane schedule (one open batch per lane). An *encoding mover* is defined in D-04.

---

## 0. What this file is

`STAGES.md` stage 6 and `V12_ORDER.md` ask for one fold: every proposal and instruction item this session built, with Jordan's rulings A-1 to A-114, as the spine; workplan v11's positions and the hole register's rows only where the evaluation carried them (the intake's 273 entries). This file decides the batch list, the order, the milestones and the parts, and hands each later lane an assignment it can execute without a further decision. It writes no part of v12 itself.

**What was run here** (scratch, not committed; `PYTHONHASHSEED` not needed: no engine run): U3 §8's script, re-pointed at this file's batch changes (§2.3), for acyclicity, waves, every longest chain and the lane schedule; `git grep` and `wc` counts cited where used; no pytest, no seeded run.

**Three facts read from the tree that the suite did not have** (each changes a decision below):

1. `engine/season/state/world.py::_object_head` (`:260-268`) and `_encode_into` (`:294-299`) put a dataclass's class name, its field count and every field name into the canonical encoding that `World.content_hash()` (`:1667`) hashes. So adding, removing or renaming a field of a hashed carrier (`Person`, `Claim`, `Tenure`, `Site`, `Event`…) moves every content hash while changing no behaviour (D-04).
2. Layer 1 names `capability` in the `Person` tuple (`04:234`) and does not name `round` in the `Claim` tuple (`04:430`). `git grep -l -w obligees -- engine modules references tools tests` lists 18 files, none under `state/` as a field.
3. No program opens a workplan file: `git grep -n 'workplans/' -- '*.py'` finds docstring and comment citations only; `valoria_master_workplan_v11` is named by `CURRENT.md`, `references/lane_assignments.yaml`, two `measure:` strings in `engine/season/requirements.yaml`, frozen text in `hole_register.yaml`, two test docstrings, eight lane handoffs and two ED ledgers (§8).

---

## 1. Decisions (the five-step ladder, CLAUDE.md §0; each reversible on Jordan's word)

Steps: 1 superseded · 2 irrelevant · 3 answered by a design document · 4 answered by precedent · 5 answered by what the code architecture needs. "Opened" names the lines read for the decision.

| id | inconsistency or open choice | decision | step | opened |
|---|---|---|---|---|
| D-01 | **H-132's batch.** The intake §3 and U3 §2.1 put H-132 in B21b; `IS-B3-FA-07` lands the same clause in B21. | **B21, as `IS-B3-FA-07`.** It is the complete item (edits, tests, gate), and all it depends on is in B21 or B05 (`14_VERBS_BINDING_C`, `U5d_FA_owed_edits` §3–§4, `16_PESSIMIST_FA_B`, `U5c_SC_one_obstacle_form`). The B21b entry becomes a pointer with no work; B21's close records H-132's register row. | 4 (the Sonnet check's rule for `IS-A-09`: one owner, the complete item wins, `IS_CHECK.md` C1) | `IS_B3_FA_SE_WR_GO.md:161-170`; the intake `:47`, `:64`, `:255`; U3 `:453` |
| D-02 | **The CR-48 → CR-49 edge** (the intake §2's `[ASSUMPTION]`: if it is a data edge, B12 gains B21). | **Not a data edge; B12 does not gain B21.** v11's own entry reads "GATE: after CR-48 (P13). NEEDS: REM-2B, REM-21": P13 is the file-serialisation rule for the verb cluster, CR-48 is not among the NEEDS, and CR-48 is SUPERSEDED. The file serialisation is carried by this plan's hot-file rule (§7). | 3 | `workplans/valoria_master_workplan_v11_part4.md:417-421`; `valoria_master_workplan_v11.md:44` |
| D-03 | **E2's B23 and B36 in the arc batch's after-list** (B42 there, B21d here). | **Not taken: B21d follows B11 and B21b only.** CR-89's NEEDS are CR-91, CR-86 (landed), CR-29, CR-34 (landed), CP-T09-02, CP-T09-04: B21b and B11. E2's B23 is a re-base on the symbol `occupying_faction` (E2 `:117`, "serialise with B23"), which the FA lane's one-open-batch rule already gives; B36 is a name collision with `harness/arc.py`, not a dependency. With both edges and D-02's the graph is still acyclic with the same wave and step counts as §2.3 (run). | 3 | v11 `_part4.md:175-186`; `master/eval/E2.md:15`, `:36-39`, `:117` |
| D-04 | **B04 is called hash EQUAL** (U3 §1 item 5, `IS-B2-CHAR-05`) **and carries a declared mover** (A-107's `Person.traits`, U1 §2a; U3 §2.1 "3 of 8"). | **B04 is an encoding mover: one re-pin, in its last `Item:` commit, said plainly.** A new field on `Person` moves every content hash (§0 fact 1). Its behaviour controls stay as U3 states them (the NPC-088 headless act and Event tallies and `corpus_run` tallies unchanged), read instead of the hash. **Rule for the whole plan:** an item that adds, removes or renames a field or class of a hashed carrier is declared `HASH MOVER(encoding)`, is co-batched with a re-pin, and its control is tallies-equal, never hash-equal. Authors apply it to every item that widens a carrier (`manner_offset?` in B10, `Scene.cost` in B34, and whatever their sources add). | 5 | `state/world.py:260-299`, `:1667-1726`; `04:233-241` |
| D-05 | **PCR-4** (the season's `round` becomes `lap`): a candidate, "not scheduled". | **Scheduled: B04's first item.** A-101 gives "round" to the fight; after PCR-3 the code would say `round` for two things. It is measured (41 non-test `.round` reads, 17 files under `engine/season`), needs no Layer 1 edit (§0 fact 2), and renaming `Claim.round` is an encoding mover (D-04), so it rides B04's one re-pin and every later item is written with `lap`. Harness output keys (`"round"` in `harness/soak.py`, `interactions.py`) keep their strings. Revert: drop the item; nothing depends on it. | 5 | PCR `:214-228`; `engine/season/state/carriers.py:327-338`; counts run here |
| D-06 | **The other tree names that fail the word test** (`U1_GLOSSARY.md` §H: `Fixtures`, `obligees`, `storybar`, `aperture`, `governance_spine`, `capability`, Tenure "edge"). | **Not scheduled.** None has a written coding instruction, and v12 takes no item without one (`STAGES.md`, standing constraints). `capability` is named by Layer 1 (a rename is Jordan's amendment and an encoding mover); "edge" is Layer 1 wording; the three harness names are in almost every gate of this plan. Each stays a glossary candidate; prose keeps the plain word. Scheduled renames, each with its instruction: L1 (B16L), L2 (B16M), PCR-3 (B16), PCR-4 (D-05), `IS-PC-05` (B15), `VOCATIONS` and `pool.py::faculty` (already ordered by CAP A2/A3 and D-U1-08, B04/B05). | 3, 5 | `U1_GLOSSARY.md:207-245`; `STAGES.md:41`, `:58` |
| D-07 | **L2 "may be cut"** (the engine's names, about 80 files). | **Kept, as `B16M`, beside B04.** The lexicon's own test is whether the critical path can carry it; in the schedule of §2.3 it runs in the MB lane at step S6 while B04 holds the IN lane, and B17, its first follower, opens at S9. Cut rule, stated in the batch: a moved golden digest stops the batch and the batch is cut, never turned into a mover. | 3 (the lexicon's test), 5 | the lexicon `:103-142` |
| D-08 | **Where the two rename batches sit.** The lexicon: after B02, before B17. | **B16L after B03, before B03a; B16M after B03a, before B05.** B03's census deletions and corrections edit files L1 and L2 rename (`hierarchy/units.py`, `rosters.yaml`, `world_q.py`: U3 §5.1); CI-02 (B03a) rewrites the comments of every file both rename; B05 is the first mover that edits mass-battle code (`resolution.py`, U3 §5.1 row for `core/contact_draw.py`). Renames ahead of movers (`STAGES.md` practice 1). | 3, 5 | the lexicon `:47-53`; U3 §5.1; CIP `:80-102` |
| D-09 | **`engine/substrate/pc_engine.py`**: CI-09 (B13) deletes it; MBA-02 (B19a) and U3 §1.3 load the duel through it. | **B13 lands first, so MBA-02 loads the duel as CI-09 step 7 re-points the workbench and `tools/export_engine_params.py`: `from modules.combat import wrapper, combatant`** (a tool under `tools/`, not the engine). U3 §1.3's B19a row and MBA-02 step 2 are read that way by the B19a author. CLAUDE.md §3's sentence naming the seam is edited in B13's commit and named in its PR body. | 4 | CIP part 2 `:243-297`; MBA `:44`; U3 `:410` |
| D-10 | **B03d-gate-observation** is its own IN batch (four items) and costs the lane schedule a step (U3 §2.3 note). | **Merged into B03's tail** (H-137, H-130, H-139, in that order); **H-138 goes to B12a** (its edit set is `loop/effects_economy.py`, SE's file; E6 offers "B03d or B12"). Merged saves a close and a step on the IN lane, the plan's bottleneck; the cost is `state/world.py`'s write path in B03's reading list. H-130 and H-139 keep E6's condition: if the grep the block names finds no caller at the batch's open, the item is dropped and the register row says so (CLAUDE.md §0.1 pt 5). | 5 | `master/eval/E6.md:143-152`; the intake `:44`, `:133-138` |
| D-11 | **B03's size** with the four early port landings and the GO items the intake adds. | **Cut: `B03g-go-early-landings` (GO), after B03, before B04 and B41.** Every link cut points forward (`references/module_contracts.yaml` is edited by CI-03 in B03, then by GO-11). Carried whole, B03 would hold about 45 items in one close; apart, the GO lane, idle until B34, closes them at S4 and GO-09's `--check` is live before B04, the first registry-editing batch (`IS-B3-GO-06`'s reason). | 5 | `IS_B3_FA_SE_WR_GO_part2.md:209-218`; the intake `:537-542` |
| D-12 | **B12's size**: 24 proposals, four instruction items and 21 intake entries (the intake §2) in one SE+WR close. | **Cut in three along U3 §1.2's own order** (a total order whose every dependency lands earlier, so each cut link points forward): **B12a** steps 1–10 and the `lattice_coupling` flip; **B12b** steps 11–19; **B12c** steps 20–25. Carried whole: one review and one critique over about 50 items and 19 declared movers, and no checkpoint. The cut costs two closes and removes the slack B12 had (its chain now ties the critical path; it does not lengthen it, §2.3). Every follower of B12 follows B12c. | 5 | U3 `:154-165`, §1.2's B12 row |
| D-13 | **B10's size** (17 proposals, 3 instruction items, 14 intake entries) and **B05's** (16 proposals, one calibration). | **Both kept whole.** B10 is on the critical path's head: a cut adds a step to every later batch. B05's items are one calibration read on the joint diff (C1–C8 red, then green) with one re-pin of every seeded result. Each is built in bounded pieces with checkpoints (the skill, CHECKPOINTS), and its review fan is sized by family. | 5 | U3 `:106-119`, `:142-149` |
| D-14 | **The intake's heading, an entry's `lane's target` and its `settled:` text disagree** (ED-1043 sits under B17; its settled text says B19, MBA-04 step 0). | **`settled:` governs, then the heading, then the lane's target** (`V11_EVALUATION.md` §7 item 4). ED-1043 lands in B19. | 3 | the intake `:9`, `:515-517`; `master/V11_EVALUATION.md` §7 |
| D-15 | **`IS-MB-06`** names B31 or B19. | **Not carried: SUPERSEDED by MBA-04** (no pool arithmetic remains). MBA §8.1 and §8.2 are the supersession table every MB author applies. | 1 | MBA `:181-186` |
| D-16 | **Two "first items" of B11** (`IS-B2-CORE-01`; the CR-29 group). | Order: the design items (D-18), then the CR-29 group (`08_FI_01` depends on it), then `IS-B2-CORE-01` with `IS-B3-GO-01`, then U3 §1 item 12's order. | 3 | the intake `:17`; `IS_B2_SC_FI_CORE_CHAR_part2.md:55-64` |
| D-17 | **The re-take** (`IS-A-13`) needs a batch. | **`B99-nine-retake`**, IN, one item, after every other batch (A-114). No batch close before it runs past two seasons; a gate copied from a source at three or four seasons is rewritten to two, and the longer form is left to B99's conjunct `argv` (§5). | 1 (A-114) | `IS_A_NINE_part2.md:325-339` |
| D-18 | **Design-first parts** (23 INCOMPLETE proposals coded DESIGN; the intake's design-first entries; A-109). | **A design item is an item**: INSTRUCTION "write the design stating (1) to (n) with falsifiers", GATE "the file exists and states them; no code" (v11's form), `opus` with a `ners` critic, placed first in the batch that builds it or where its source says ("at B11's open"). Its build item gates on it. What the design cannot settle by the ladder ends the run `STOPPED` for Jordan; a build whose design is unmerged at its batch's open is HELD and leaves for the held list at the expunge (v11's rule for CR-88). No design batch is added. | 4 | v11 `_part4.md:161-166`; `IS_B2_SC_FI_CORE_CHAR.md:293` |
| D-19 | **Authored values** (15 INCOMPLETE proposals coded CONTENT; the cast). | **Drafted early, landed at its batch, ratified at that batch's merge** (ED-1094), as `IS-A-11` does for the cast: its stage 1 (the five tables) is B04's last item; other content is a drafting item first in its own batch, values marked `[ASSUMPTION]` or `status: seed`, the batch's PR body listing each for Jordan's correction. | 4 (`IS-A-11`) | `IS_A_NINE_part2.md:263-307` |
| D-20 | **In the PC lane, B18 or B29 first.** | **B29 first** (IS-A §12.3 item 2: it completes two verbs of R-05). | 3 | `IS_A_NINE_part2.md:406-408` |
| D-21 | **A two-lane batch's in-flight row** (B12a, B12b, B12c hold SE and WR). | The row lives in `registers/handoffs/HANDOFF_SE.md`; `HANDOFF_WR.md` carries one pointer row `Batch <handle> — IN FLIGHT (row in HANDOFF_SE.md)`, deleted at the same expunge, so a WR invocation finds the lane held. | 5 | the skill, "The in-flight row" |
| D-22 | **"The calibration batch"** that sets a setting shipped at its control value. For the fight, the field and the one roll it is B15, B19 and B05. `31_WR_B_the_revival_gathers` (`sway_gain`), `IS-B3-FA-07` (`faction_power_step`) and others name one that no list defines; A-92's own consequence says "the calibration batch after B38". | **`B98-dials`**, IN, after every batch but B99. Its members are every setting an item ships at control whose source says a later calibration sets it and which its own batch does not set: each author lists them (`DIALS AT CONTROL`, §5.2), H2 collects them (§7.8), and one item per setting flips it in its own commit against its source's target reading, one re-pin at the end. A setting whose source states no target is `BLOCKED (design: no target reading)`. B99 then reads the nine on the settings as set. Not folded into B99: a reading and a mover in one close would make the re-take's tree the one being re-pinned. | 3 (A-92), 5 | `unified/DECISIONS_ANSWERED.md:128`; `proposals/31_WR_B_the_revival_gathers.md:7`, `:20`; U3 `:448` |

**Nothing survives the ladder for Jordan**, so `V12_FOR_JORDAN.md` is not written. What waits on him is adoption and the held-back list (§8), neither a question with two options.

---

## 2. The batch list

**61 batches**: U3's 52 (§2.1 there), less B03d (D-10), with B12 as three (D-12), plus `B03g` (D-11), `B03a-prose` and `B13-pc-package` (CIP §2), `B16L` and `B16M` (the lexicon §4), `BA1-cast-content` (`IS-A-11`), `B98-dials` (D-22) and `B99-nine-retake` (D-17). Handles are final; `B13` is CIP's use of the handle U3 left free.

### 2.1 The graph (generated by the script of §2.3; `after` is the full list a batch gates on, each `GATE: Batch <handle>`)

| batch | lane | wave | step | slack | after |
|---|---|---|---|---|---|
| B00-ids | IN | W0 | S0 | 0 | — |
| B01-laneA | IN | W1 | S1 | 0 | B00 |
| B02-tests | IN | W2 | S2 | 0 | B00, B01 |
| B03-hygiene | IN | W3 | S3 | 0 | B00, B01, B02 |
| B03g-go-early-landings | GO | W4 | S4 | 1 | B00, B01, B02, B03 |
| B03c-boot | IN | W4 | S4 | 0 | B00, B01, B02, B03 |
| B16L-mb-words | MB | W4 | S4 | 0 | B00, B01, B02, B03 |
| B03a-prose | IN | W5 | S5 | 0 | B00, B01, B02, B03, B03c, B16L |
| B13-pc-package | PC | W6 | S6 | 0 | B00, B01, B02, B03, B03a |
| B16M-mb-engine-words | MB | W6 | S6 | 0 | B16L, B03a |
| B04-capability-home | IN | W6 | S6 | 0 | B00, B01, B02, B03g, B03c, B03a |
| B05-one-roll | IN | W7 | S7 | 0 | B00, B01, B02, B03a, B13, B16M, B04 |
| B06-keyed-draw | IN | W8 | S8 | 0 | B00, B01, B02, B03, B05 |
| B07-task-draw | IN | W9 | S9 | 0 | B00, B01, B02, B05, B06 |
| B08-scene-order | IN | W6 | S13 | 12 | B00, B01, B02, B03a |
| B09-memory | IN | W10 | S10 | 0 | B00, B01, B02, B05, B07 |
| B10-character | IN | W11 | S11 | 0 | B00, B01, B02, B04, B05, B09 |
| BA1-cast-content | IN | W12 | S12 | 10 | B00, B01, B02, B04, B05, B10 |
| B11-fi-readers | FI | W12 | S12 | 0 | B00, B01, B02, B03, B04, B05, B07, B10 |
| B11F1-flow-se | SE | W16 | S16 | 2 | B12c |
| B11F2-flow-in | IN | W17 | S17 | 2 | B09, B10, B11F1 |
| B12a-world-motion-and-ground | SE+WR | W13 | S13 | 0 | B00, B01, B02, B04, B05, B07, B10, B11 |
| B12b-weather-arcs-population | SE+WR | W14 | S14 | 0 | B12a |
| B12c-material-verbs-and-valley | SE+WR | W15 | S15 | 0 | B12b |
| B14-pc-outcome | PC | W8 | S8 | 3 | B00, B01, B02, B13, B05 |
| B15-pc-calibration | PC | W12 | S12 | 0 | B00, B01, B02, B04, B05, B10, B14 |
| B16-pc-round | PC | W13 | S13 | 0 | B00, B01, B02, B06, B07, B10, B15 |
| B17-mb-scale | MB | W9 | S9 | 4 | B00, B01, B02, B16L, B16M, B05, B14 |
| B18-pc-content | PC | W14 | S15 (D-20) | 7 | B00, B01, B02, B14, B15, B16, B17 |
| B19a-mb-contact-instrument | MB | W14 | S14 | 0 | B00, B01, B02, B16M, B14, B15, B16, B17 |
| B19-mb-field-calibration | MB | W15 | S15 | 0 | B00, B01, B02, B16L, B04, B05, B06, B15, B16, B17, B19a |
| B20-mb-orders | MB | W16 | S16 | 0 | B00, B01, B02, B16L, B05, B15, B16, B17, B19 |
| B21-fa-governance | FA | W12 | S12 | 0 | B00, B01, B02, B05, B07, B10 |
| B21b-fa-war | FA | W13 | S13 | 0 | B11, B21 |
| B21c-fa-seats | FA | W14 | S14 | 0 | B21b |
| B21d-fa-arc | FA | W14 | S15 | 8 | B11, B21b |
| B21s-strife-supply | IN | W16 | S18 | 6 | B12c, B21 |
| B22-mb-armies | MB | W17 | S17 | 1 | B00, B01, B02, B16L, B04, B05, B07, B10, B12c, B17, B19, B20, B21, B21b |
| B23-land | FA | W18 | S18 | 1 | B00, B01, B02, B07, B12c, B17, B19, B20, B21, B21b, B22 |
| B24-sc-hearing | SC | W13 | S13 | 1 | B00, B01, B02, B03, B04, B07, B10, B11 |
| B24a-sc-outside-the-room | SC | W15 | S15 | 0 | B21c, B24 |
| B25-fi-questioning | FI | W16 | S16 | 0 | B00, B01, B02, B11, B12c, B24 |
| B26-fi-inquiry | FI | W17 | S17 | 2 | B00, B01, B02, B10, B11, B12c, B24, B25 |
| B27-sc-proceedings | SC | W16 | S16 | 0 | B00, B01, B02, B11, B24, B24a |
| B28-social-verbs | SC | W17 | S17 | 2 | B00, B01, B02, B05, B07, B08, B11, B15, B21, B25 |
| B29-pc-custody | PC | W14 | S14 (D-20) | 8 | B00, B01, B02, B15, B16, B21 |
| B30-mb-nested | MB | W17 | S18 | 5 | B00, B01, B02, B16L, B05, B15, B16, B20, B24 |
| B31-mb-loadout-economy | MB | W16 | S19 | 6 | B00, B01, B02, B16L, B17, B18, B19 |
| B32-inst-kit | FA | W17 | S17 | 0 | B00, B01, B02, B04, B05, B07, B20, B21, B21b, B21c, B24, B24a, B25, B27 |
| B33-inst-economy-hands | FA | W18 | S19 | 2 | B00, B01, B02, B04, B05, B07, B12c, B21, B24, B25, B26, B27, B28, B32 |
| B34-go-surface | GO | W14 | S14 | 3 | B00, B01, B02, B03, B10, B21, B24 |
| B35-wr-thread | WR | W18 | S18 | 0 | B00, B01, B02, B03, B05, B09, B11, B12c, B32, B34 |
| B36-wr-story-instruments | WR | W19 | S19 | 0 | B00, B01, B02, B03, B09, B12c, B27, B34, B35 |
| B37-happenings | IN | W16 | S16 | 3 | B00, B01, B02, B05, B10, B11, B12c, B15, B16, B21 |
| B37p-wr-kin-and-life | WR | W17 | S17 | 3 | B12c, B37 |
| B38-narrative-regimes | WR | W20 | S20 | 0 | B00, B01, B02, B05, B07, B09, B10, B11, B11F1, B11F2, B12c, B21, B22, B23, B27, B28, B32, B34, B36 |
| B39-procgen-and-cases | WR | W21 | S21 | 0 | B00, B01, B02, B04, B06, B07, B10, B11, B11F1, B12c, B15, B21, B22, B24, B25, B26, B27, B32, B33, B36, B37, B37p, B38 |
| B40-inst-scenarios | FA | W22 | S22 | 0 | B00, B01, B02, B12c, B21, B21b, B21c, B32, B33, B39 |
| B41-go-port-gate | GO | W15 | S15 | 7 | B00, B01, B02, B03g, B06, B34 |
| B98-dials | IN | W23 | S23 | 0 | every batch but B99 |
| B99-nine-retake | IN | W24 | S24 | 0 | every batch |

Edges this file adds to U3's (each points forward; the rest are U3 §2.1 and §8 as read): B03 → B03g → B04, B03g → B41; B03 → B16L → B03a, B03c → B03a → B04, B05, B08 (CIP §2); B03a → B13 → B05, B14 (CIP §2); B16L → B17, B19, B20, B22, B30, B31 and B03a → B16M → B05, B17, B19a (the lexicon, D-08); B04, B05, B10 → BA1 (`IS-A-11`); B12a → B12b → B12c, and B12c in the place of B12 everywhere; B03 in the place of B03d before B11; every batch → B98 → B99. Soft, not an edge: BA1 before B15, B19, B24 (a calibration that closes first names the control it ran at and is re-read once at BA1's close, `IS_CHECK.md` C2).

### 2.2 What each batch holds

Columns: **items** in landing order, by source (U3 §1 "item n" is that numbered paragraph and its order, read with §1.2 for the within-batch edges; `IS-`, `CI-`, `MBA-`, `PCR-`, `L` handles are the instruction items; "intake `:n`" is the heading at that line of the intake, every entry under it); **requirement** from IS-A §12.2 (the conjuncts the close reads), or the reason it serves none; **hash** (EQUAL, or the movers and the one re-pin); **cost** (the dominant class and tiers; each item states its own); **est.** in hours, §2.4.

| batch | items, in order | requirement | hash | cost and tier | est. |
|---|---|---|---|---|---|
| B00 | the id and row-block allocation (U3 §1 item 1, completed by §7.5); H-1 (intake `:102`, A-111's ledger rows as relayed) | none: allocation (`STAGES.md` parallel rule 4) | EQUAL | edit; `sonnet` | 3 |
| B01 | U3 §1 item 2 (the lane-A rebase, `03_PC_duel_chain_reach`; A-93) | R-04.c5 (i); `IS-PC-03`'s reading | MOVER: every realm pin, once | build (a rebase over 33 shared files); `opus` reads the resolution | 3 |
| B02 | U3 §1 item 3 with `IS-A-01` in the place of `01_CORE_requirements_reading_record` §1; `CI-11` after `16_PESSIMIST_GAME_consequence_reading`; `IS-A-06`, `IS-A-03`, `IS-A-07` (`storybar.py` order: the nine-gate proposal, `IS-A-03`, `IS-A-07`); `IS-A-04`; `IS-A-05` part 1; `IS-B2-CORE-07`; intake `:106` (V9-27, DEF-8, H-2); `IS-A-02` last | R-01.a–c, R-02.a–b, R-03.a–b, R-04.b, R-06.d–e, R-07.a, R-08.b–c, R-09.a; the first `BUILT OUT`, `ENGINES`, `NULL SCENES` baselines | EQUAL | small builds; `sonnet` high; `corpus_run` instrument time | 10 |
| B03 | U3 §1 item 4 with `CI-10` first, `CI-08` after the census deletions, `CI-03` after `17_CENSUS_REST_1` D4, `IS-B3-SE-04` after `CI-03`, `CI-04` and `CI-05` after `17_CENSUS_C1B_01` D3, `CI-06` after `U5a_CORE_owed_edits`; `IS-B2-CORE-06` (its BLOCKED part is the CR-07/H-89 entry); intake `:112` and `:227`; the dangling-cite comment fix of `master/V11_EVALUATION.md` §6; then H-137, H-130, H-139 (D-10) | none: deletions and owners (STAGES rule 5); `CI-10`'s `FORK:` rows | EQUAL | edits; `sonnet`; fan by family at the close | 20 |
| B03g | GO-09, GO-11, GO-01, GO-05 (intake `:537`; `IS-B3-GO-06` (2)) | none: the port's early checks (CLAUDE.md §6) | EQUAL | edits; `sonnet` | 4 |
| B03c | `CI-07` | none: the builder's home (A-102) | EQUAL | wide move; `sonnet` high | 3 |
| B16L | L1-3, L1-2, L1-1, L1-4 (the lexicon's order) | none: Jordan's A-95 and A-99 words in code | EQUAL (gate (b) of the lexicon measures it; D-07's stop rule) | wide mechanical; `sonnet` | 4 |
| B03a | `CI-01`, `CI-02` | none: reading cost of every later batch (H-03, H-07) | EQUAL (AST-equality over every edited file) | wide, comment-only; `sonnet`, one producer per package, disjoint files | 3 |
| B13 | `CI-09` (with CLAUDE.md §3's seam sentence, D-09) | none: personal combat as a package (H-08) | EQUAL (`combat_engine_v1.json` byte-identical) | wide mechanical; `sonnet` high | 3 |
| B16M | L2-3, L2-2, L2-1 | none: the port's vocabulary | EQUAL (stop rule, D-07) | wide mechanical; `sonnet`; readings `haiku` | 4 |
| B04 | `PCR-4` (D-05); U3 §1 item 5 with U1 §2a's trait roster (A-107) and `IS-B2-CHAR-05` in the roster's commit; `IS-A-11` stage 1 (drafting, no code) last | R-01, R-02, R-03 re-read; the other six print their held counts | MOVER(encoding), one re-pin (D-04) | builds; `sonnet`; drafting `opus` | 7 |
| B05 | U3 §1 item 6; H-199 (intake `:422`); `IS-B2-CHAR-06`'s reading | R-09.c; re-read R-08.b | MOVER: every seeded result, once | calibration; `opus` reads C1–C8 and the tuning | 12 |
| B06 | U3 §1 item 7 (GO-12's fallback part lands here as `11_GO_one_draw_owner`'s four fallbacks) | R-09.e; re-read R-01.b, R-02.a, R-03.a, R-08.b | MOVER, once | build; `sonnet` high | 4 |
| B14 | U3 §1 item 14; `IS-PC-04`; intake `:489` (CP-T03-06, PC-21) | none of its own (the typed outcome B15 to B19a read) | MOVER (`standing`, `fell_to`), once | small builds; `sonnet` | 6 |
| B07 | U3 §1 item 8; `IS-A-10` in the task-draw arm's commit | R-09.a (re-pointed), R-09.d; `BUILT OUT` for every converted verb (`IS-A-08`) | MOVER, once | build; `sonnet` high | 5 |
| B17 | U3 §1 item 17; `IS-MB-05`'s reading | none of its own (scale and the troop file) | MOVER (seed 2's pin), once | builds; `sonnet` | 5 |
| B09 | U3 §1 item 10; intake `:140` (H-145 with NM-W9 (b), IN-58, H-135) | re-read R-01.b–c, R-02.a–b, R-07.a | MOVER (8 of 9 members), once | small builds; `sonnet` | 7 |
| B10 | U3 §1 item 11; `IS-A-05` part 2 after `02_CHAR_scar_cap_and_regard_unit`; `IS-B2-CHAR-02` after `02_CHAR_choice_alignment`; `IS-B2-CHAR-07` (CL-PERSON's build, neutral control); intake `:146` | R-07.d; re-read R-06.c–d, R-07.b, R-08.c | MOVER (encoding too: `manner_offset?`), once | builds and design items; `sonnet`, `opus` on designs | 16 |
| BA1 | `IS-A-11` stage 2; `IS-B2-CHAR-03`'s members; `IS-B2-CHAR-07`'s offsets; `IS-B2-CHAR-06`'s reading | R-06.a, R-08.a, R-09.b; re-read R-06.d–e | MOVER: the build hash and every season hash, once | content; drafting `opus`, landing `sonnet` | 6 |
| B11 | D-16's order: design items (`IS-B2-FI-07` with `IS-B3-SE-06`; `IS-B2-FI-05` with CR-83); the CR-29 group (intake `:17`); `IS-B2-CORE-01` with `IS-B3-GO-01`; `IS-B2-CORE-02`; U3 §1 item 12; `IS-B2-FI-03`, `-04`, `IS-B2-CHAR-01`; intake `:163` and `:464` (as `IS-B2-FI-02` folds them, less CR-94); `IS-B2-FI-06`, `IS-B2-FI-01` and `IS-B2-CORE-03`'s summary line at the close | R-04.c7; `covenant` formed | MOVER (13 of 13), once | builds; `sonnet`; designs `opus` | 15 |
| B15 | `PCR-1` first; U3 §1 item 15; `IS-PC-05` with UPR §1 rows 1–2; ED-SC-0001 (intake `:494`); `IS-PC-03`'s reading | none of its own (R-04's combat scale becomes observable) | MOVER: combat goldens, the armour reference and the export, one re-record | calibration; `sonnet` builds, `opus` reads | 9 |
| B21 | U3 §1 item 21; `IS-B3-FA-07` after `14_VERBS_BINDING_C` and `U5d_FA_owed_edits` §3–§4 (D-01); `IS-B3-FA-05` after `14_VERBS_BINDING_D`; `IS-B3-FA-06` with the rest of `U5d_FA_owed_edits`; `IS-B3-FA-01` after `06_FA_shortest_loop_B`; intake `:168` and `:231` | R-04.a (`establish`, `confer`, `revoke`, `dispatch`, `issue`, `requisition`), R-04.c2; `BUILT OUT`: `confer`, `revoke`, `succeed` | MOVER, once | builds; `sonnet`, `opus` on the two judgment items | 12 |
| B08 | U3 §1 item 9; H-249 (intake `:129`) | R-03.c; re-read R-03.a–b, R-01.b | MOVER (2 of 2), once | small builds; `sonnet` | 4 |
| B12a | `IS-B3-SE-03` first; U3 §1 item 13, steps 1–10 and the `lattice_coupling` flip; H-138; the intake's B12 entries that belong here by §5.6's rule (`:172`, `:310`, `:352`) | re-read only | MOVER, once | builds; `sonnet` | 16 |
| B16 | U3 §1 item 16 with `PCR-2`, `PCR-3`; `IS-PC-01` last (its step 6 in B34); `IS-PC-03`'s reading | none of its own (the round M4 reads) | MOVER (3 of 3), once | builds; `sonnet` | 5 |
| B21b | intake `:237` and `:177` in the intake §3's order (IN-36's cap first; CR-91's carrier as occasion, A-103); H-132's entry is a pointer to B21 (D-01) | carried v11 positions; each entry's own R line | per entry; one re-pin | builds; tiers per entry | 13 |
| B24 | `IS-B2-SC-02` first; U3 §1 item 24 with `IS-B2-SC-03` (after HEAR_B edit 1, before edit 6), `IS-B2-SC-04`, `IS-B2-SC-08` (after HEAR_B edit 9), `IS-B2-SC-09`; intake `:181` and `:426`; `IS-B2-SC-01` at the close | R-04.c3 | MOVER (7 of 12; `IS-B2-SC-02`), once | builds; `sonnet`; cost terms `opus` with `ners` | 11 |
| B12b | U3 §1 item 13, steps 11–19; its intake entries (§5.6) | re-read only | MOVER, once | builds; `sonnet` | 6 |
| B19a | `MBA-01`, `MBA-02` stage 1, `MBA-03` (D-09) | none of its own (the table B19 reads) | EQUAL | small builds and one background run; `sonnet`; a `--trust` failure read by `opus` | 6 |
| B29 | U3 §1 item 29; CR-51 (b), the arrest re-measure (intake `:193`), last | `BUILT OUT`: `arrest`, `accept` | MOVER, once | small build; `sonnet` | 3 |
| B21c | intake `:266` (CR-38 design-first, D-18) | carried v11 positions | per entry; one re-pin | builds; `opus` on CR-38 | 5 |
| B34 | U3 §1 item 34; `IS-B3-FA-02` and `IS-B3-GO-02` after `11_GO_fidelity_and_campaign_modes`; `IS-B3-GO-03`; `IS-B3-GO-07` after `IS-B3-FA-02`; `IS-DICE-01` after `01_CORE_one_scene_contract`; `IS-PC-01` step 6; `IS-MB-01` step 4 | R-04.c1 (the sheet) | MOVER (1 of 5; encoding: `Scene.cost`), once | builds; `sonnet` | 7 |
| B12c | U3 §1 item 13, steps 20–25, with `IS-B3-SE-05` beside `14_VERBS_MATERIAL_A`; `IS-B3-SE-06`'s build; its intake entries (§5.6: CR-49 with `14_VERBS_MATERIAL_B`); `IS-B3-SE-01` last | R-04.c6; `BUILT OUT`: `restore`, `work`, `sabotage`, `exchange`, `requisition`, `found`, `build` | MOVER, once | builds; `sonnet` | 6 |
| B18 | U3 §1 item 18 | none: content for the standalone duel | MOVER (2 of 2), once | content and small builds | 3 |
| B19 | U3 §1 item 19 (the T-rows first; MBA-04 with ED-1043 at its step 0, D-14; ED-MB-0045 before `04_MB_cell_hierarchy_as_data`; L1-6 after that file's §3; MBA-05, MBA-06, MBA-04 step 5, MBA-08 with 27C-2 and 27C-3) | R-04.c4, R-04.c5 (ii)–(iii), R-07.c (with B20) | MOVER: every fought field, one re-record | calibration; `sonnet` builds, `opus` reads | 11 |
| B21d | CR-89 (1), (2) → CR-90 → CR-88 (design first) → CR-89 (3), (4) (intake `:276`) | carried v11 positions (R-04, R-02, R-06 contributors per entry) | commits (1)–(3) EQUAL; each flip a mover; one re-pin | `opus` builder per entry | 4 |
| B24a | intake `:431` as the intake §3 narrows it (CR-58 to CR-64) | carried v11 positions | per entry; one re-pin | builds; `sonnet` | 5 |
| B41 | U3 §1 item 41 with `IS-B3-GO-06` (1) as the entry's own text; `IS-B3-GO-05`; intake `:544` (GO-08 first) | none: the port's pins (CLAUDE.md §6) | EQUAL (0 of 2) | builds; `sonnet` | 6 |
| B11F1 | CR-106 (intake `:185`); CR-107 and the territory caps (`:328`) | carried v11 positions | MOVER (CR-106; the cohort rows), once | builds | 4 |
| B20 | U3 §1 item 20; `IS-MB-01` after the scenario proposal's §A–§D; `IS-MB-03` after `27_MB_D`; `IS-MB-05`'s reading | R-04.c4, c5 (with B19) | MOVER (2 of 4), once | builds; `sonnet` | 5 |
| B25 | U3 §1 item 25; `IS-B2-SC-07` (its B25 half); intake `:282` and `:474` | R-04.a (`open_case`); `BUILT OUT`: `construe`, `interrogate`, `tie` (the table reads 68 by command) | MOVER (4 of 5), once | builds; `sonnet` | 6 |
| B27 | U3 §1 item 27; `IS-B2-SC-07` (its B27 half); intake `:370`, `:445`, `:498` | none of its own (the proceedings B32 and B36 read) | MOVER (6 of 6), once | builds; `sonnet`; the contested degree `opus` | 10 |
| B37 | U3 §1 item 37; `IS-PC-03`'s reading | none: A-15, A-16, A-96 | MOVER (4 of 4), once | builds; content (ages) | 4 |
| B11F2 | intake `:197` (CR-103 and CR-105 its held tail) | carried v11 positions | per entry (EQUAL as shipped) | builds | 7 |
| B22 | U3 §1 item 22; `IS-MB-02` after `14_VERBS_MILITARY_A` (`IS-A-09` points at it; its step 5's condition is met by `14_VERBS_MATERIAL_A` edit 4 in B12c, which makes `_fall` graded); `IS-MB-05`'s reading | R-04.c1 (`train`); `BUILT OUT`: `train`, `recruit`, `discharge_troops`, `form_unit`, `assign_troops`, `disband_unit`, `order_unit`, `raze`, `besiege`; `ENGINES`: `mass_battle.army`, `mass_battle.army_order` | MOVER (6 of 7), once | builds; `sonnet`; `opus` reads the siege table | 6 |
| B26 | U3 §1 item 26; H-169 (intake `:478`) | `BUILT OUT`: `destroy_record`, `examine`, `seize` (a Record) | MOVER (5 of 6), once | builds; `sonnet` | 5 |
| B28 | U3 §1 item 28; `IS-B2-SC-05` after `14_VERBS_SOCIAL1_B`; `IS-B2-CORE-05`; `IS-B2-SC-06` (BLOCKED: SE names the store exchange); H-286 (intake `:441`) | `BUILT OUT`: `comply`, `evade / defy`, `forgive`, `covenant`; re-read R-03.a | MOVER (5 of 5), once | builds; `sonnet` | 6 |
| B32 | U3 §1 item 32; H-278 (intake `:286`) | R-04.a (`determine`, `convene`); `BUILT OUT`: `determine`, `pardon` | MOVER (7 of 10), once | builds; `sonnet` | 7 |
| B37p | intake `:363` (CP-T10-04, -06, -07, -09) | carried v11 positions | per entry; one re-pin | builds | 4 |
| B21s | CR-73 (intake `:359`), CR-74 (`:189`) | carried v11 positions | per entry | builds | 3 |
| B23 | U3 §1 item 23; `IS-B3-FA-04` after `U5d_FA_land_and_seats_pass_on_a_won_march`; intake `:290` and `:523`; `IS-MB-05`'s reading | `BUILT OUT`: `marshal`, `surrender`, `seize`; the land gate's arms a–i | MOVER (3 of 4), once | builds; `sonnet`; `opus` for the claim reader | 6 |
| B30 | U3 §1 item 30 with `IS-MB-04` after the squad file, then `IS-PC-02`, then `MBA-07` | R-04.c5 (the grid) | MOVER (1 of 1), once | builds; `sonnet` | 4 |
| B35 | U3 §1 item 35 with `IS-B3-WR-01` (first build item; CP-T07-02 with H-47, H-62) to `IS-B3-WR-05`; intake `:376` in `IS-B3-WR-01`'s order | `BUILT OUT`: `knot`, `thread_read`, and `weave`, `lock`, `mend`, `ward` | MOVER: every executed thread row, once | builds; `sonnet`; `opus` critic on two | 12 |
| B31 | U3 §1 item 31; `MBA-09` last | none: A-69, A-78, A-113 | MOVER, once | builds; `sonnet` | 4 |
| B33 | U3 §1 item 33; CP-T08-07 (intake `:333`, MISSING-DEP) | none: A-12, A-13, A-14 | MOVER (9 of 13), once | builds; `sonnet` | 8 |
| B36 | U3 §1 item 36 (`harness/storybar.py` serially, C3-K7); NM-W5 (intake `:211`) | R-04.c1 (the chronicle) | EQUAL (0 of 7) | builds; `sonnet` | 6 |
| B38 | U3 §1 item 38, with A-103's correction of `30_WR_A_the_era_is_a_named_period.md:65`; `IS-B3-GO-04` with `30_GO_F`; `IS-B3-FA-03` after `30_WR_E`; `IS-B3-SE-02` last | re-read R-05 (`riot`); `NULL SCENES` asserted 0 (C9) | MOVER (12 of 18), once | builds; `sonnet`; `opus` on the calibration reads | 11 |
| B39 | U3 §1 item 39; CR-85's hooks half (intake `:502`) | re-read R-06.e, R-09.b on the generated cast | MOVER (7 of 11), once | builds and content | 7 |
| B40 | U3 §1 item 40 | all nine re-read (no status edit) | EQUAL (0 of 9) | scenario builds; `sonnet` | 6 |
| B98 | one item per setting still at its control value, from the collected `DIALS AT CONTROL` lines (D-22; written by lane A44 after the body parts return) | none of its own: the mechanisms shipped dormant begin to run (CLAUDE.md §0.2) | MOVER: every realm pin, one re-pin | calibration; `sonnet` runs, `opus` reads each flip against its target | 8 |
| B99 | `IS-A-13` | **the re-take of all nine** (A-114) | EQUAL | instrument time; `sonnet` runs, `opus` reads each reading against its conjunct | 5 |

Not in any batch: the intake's 22 head rules (§7.1), its 54 held entries (§7.9) and the A-109 design entry (carried as B11's design item, D-18).

### 2.3 Waves, the critical path and the schedule

The script of U3 §8, with this file's changes applied to U3's parsed table (scratch, not committed), prints: **61 batches, 501 edges, acyclic; 25 waves (W0–W24); a critical path of 25 batches; 25 steps under the lane rule, the wave count, so no step is lost to a lane** (27 in handle order). Against U3 (22 waves, 23 steps): +1 for B03a on the head, +1 each for B98 and B99, −1 step for D-10.

**Critical path.** The head B00 → B01 → B02 → B03 → (B03c or B16L) → B03a → (B04, B13 or B16M) → B05 → B06 → B07 → B09 → B10, then one of four middles of equal length, then the tail B32 → B35 → B36 → B38 → B39 → B40 → B98 → B99:
(a) B15 → B16 → B19a → B19 → B20;
(b) B11 → B21b → B21c → B24a → B27;
(c) B21 → B21b → B21c → B24a → B27;
(d) B11 → B12a → B12b → B12c → B25 (new with D-12).
Shortening one middle alone shortens nothing. Batches with slack: B03g 1, B22 1, B23 1, B24 1, B11F1 2, B11F2 2, B26 2, B28 2, B33 2, B14 3, B34 3, B37 3, B37p 3, B17 4, B30 5, B21s 6, B31 6, B18 7, B41 7, B21d 8, B29 8, BA1 10, B08 12.

**Schedule (one open batch per lane; critical path first among ties, then IS-A §12.3):**

| step | open at once |
|---|---|
| S0–S3 | B00 · B01 · B02 · B03, one each (IN) |
| S4 | B03c (IN), B16L (MB), B03g (GO) |
| S5 | B03a (IN), alone in the whole plan: it edits the comments of every game-code file |
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

A step is a wave of `STAGES.md`'s parallel rules only where its batches' edit sets are disjoint or meet in different keys or functions of a hot file (§7.3); the coordinator checks that from the file census at the step's open and serialises a pair that fails it. Concurrency cap: six open batches (S15, S17) `[ASSUMPTION: the machine gives each session's `pytest -n auto` its cores in turn — basis: `nproc` is 4 here; the cap is the coordinator's to lower]`.

### 2.4 Runtime

**No batch has a measured runtime.** The est. column is a formula, not a measurement: `0.4 h × (members + instruction items + intake entries) + 2.5 h for the one close, + 2 h where the batch runs a calibration or a long instrument` `[estimate — basis: CIP's own two to three hours of agent time for CI-09, a 60-file mechanical item; no close has been timed under v12's rules]`. By it: the serial sum is about 415 h, the schedule's makespan (the longest batch of each step) about 221 h, the MB middle of the critical path about 190 h end to end (B98's 8 h is a guess: its members are not yet listed). **B00, B01 and B02 each record their measured wall time, build and close apart, in their closing commit bodies; the head's est. column is replaced by measured values from then on, batch by batch, in each expunge commit.** Instrument times measured by other lanes and to be re-measured, not quoted: `register --requirements` 0.7 s, `m1_acceptance --summary` 21 s, a realm build with one season 7 to 8 s, a season's cost roughly doubling with each season played (CIP part 2 §5 note 4; IS-A §12.4).

### 2.5 Where each batch's gate is stated

Every batch gate is a set of commands read once on the closing tree, each with its expected reading (§5.2 adds the readings every close takes). The author copies it from:

| batches | the gate's source |
|---|---|
| every batch with a paragraph in U3 §1 (B00 to B41 there, B19a, B03c) | that paragraph's "Gate:" sentence, with U3 §1.3's row for the instrument and when it exists; where the paragraph names none (U3 §1.3's last sentence lists them), the union of its members' own gates |
| B03g | each early landing's `--check` prints OK at the close (`IS-B3-GO-06`'s gate; each entry's own falsifier in the intake) |
| B16L, B16M | the lexicon's "Gate (expected reading)" for L1 (a) to (c) and for L2; a moved digest stops the batch (D-07) |
| B03a | `CI-02`'s AST-equality reading over every edited file, and `CI-01`'s two loaders reading the same rosters |
| B13 | `CI-09`'s five gate rows (the seed-2 and seed-0 hashes, the export byte-identical with no rebuild, the golden modes, the freshness gate, no `sys.path.insert` left) |
| B04 | U3 §1 item 5's gate with the hash reading replaced by tallies (D-04), and the re-pin |
| BA1 | `IS-A-11`'s gate, its `aperture` reading at two seasons |
| B12a, B12b, B12c | U3 §1 item 13's gate split with the items: controls equal and each flip its own declared mover in all three; the valley loader test in B12c |
| B21b, B21c, B21d, B24a, B11F1, B11F2, B21s, B37p | each entry's own gate and falsifier, as the intake prints them and its carry-forward block states them |
| B98 | per setting: its source's target reading on named seeds, and the control (the setting at its control value reproduces the previous item's hash) |
| B99 | `IS-A-13`'s gate |

---

## 3. Milestones and the requirement map

A milestone is a set of batches whose last close is a point at which every conjunct of its rows has a reading on one tree. **No row's `status:` is edited at a milestone** (A-114): the readings are written into the conjuncts' `reading:` records by each batch's last `Item:` commit (`IS-A-12`), and the one re-take that may move a row is B99. Two seasons is the cap on every probe and close before B99 (B98 included) (v11's P10, carried as a head rule).

| milestone | closes at | batches | rows whose conjuncts are all read by then | expected reading |
|---|---|---|---|---|
| **M0 · ground** | B04 | B00, B01, B02, B03, B03g, B03c, B16L, B03a, B13, B16M, B04 | R-01, R-02 (on the new instruments), R-03 | all three hold; the other six print their held counts for the first time |
| **M1 · every outcome is drawn** | B08 (at S13: it has slack 12 and yields the IN lane to BA1 at S12, IS-A §12.3 item 1; R-09's four conjuncts are read by B07's close, R-03.c at B08's) | B05, B06, B07, B08 | R-03 (with R-03.c); R-09.a, .c, .d, .e | R-09 short of R-09.b only |
| **M2 · persons** | BA1 | B09, B10, BA1 | R-06, R-08, R-09; R-07 if R-07.c reads with its receipt | R-06, R-08, R-09 hold; R-07 holds or is one conjunct short |
| **M3 · every verb** | B35 | B11, B12a, B12b, B12c, B14, B15, B21, B21b, B21c, B22, B23, B24a, B25, B26, B27, B28, B29, B32, B35 | R-05; R-07 if still open | `built out n of n` at B35's `n` |
| **M4 · every scale** | B36 | B16, B17, B19a, B19, B20, B24, B30, B34, B36 | R-04 | every R-04 conjunct holds |
| **M5 · the rulings beyond the nine, and the carried positions** | B40 | B18, B31, B33, B37, B38, B39, B40, B41, B11F1, B11F2, B21d, B21s, B37p | none new; R-05 re-read at B38, R-06.e and R-09.b at B39, all nine at B40 | all nine hold |
| **the settings, then the re-take** | B99 | B98, B99 | all nine, on B98's closing tree (the settings as set) | `m1_acceptance --summary` row 3 reads what the readings say |

M3 lists B21b, B21c, B24a and B27 because B32 follows them (U3 §2.1 as recomputed), which IS-A §12.1 did not have. **The map** (batch → conjuncts its close reads → expected) is the requirement column of §2.2 with the expected readings of IS-A §12.2, copied by each author into its batch's `REQUIREMENT:` line; B12's row there is B12c's, and the rows for B03d and B10c do not exist. A batch whose column says "none" states the reason given (STAGES rule 5). `IS-A-08`'s rule holds for every batch that adds, splits or re-draws a verb row: the `BUILT OUT` line of `aperture 2 --seeds 0 1 2` for each such verb is in the gate, and a verb not built out at the close is a failed gate. Dependency order and requirement order did not conflict anywhere this lane looked (IS-A §12.3 item 4 holds on the 61-batch graph: every row's last batch is at or before B36).
