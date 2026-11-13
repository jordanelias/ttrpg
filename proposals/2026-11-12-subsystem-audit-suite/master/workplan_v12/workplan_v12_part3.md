# Workplan v12 — part 3: batches B00-ids, B01-laneA, B02-tests

## Status: PROPOSED (a body part of workplan v12, drafted under `master/workplan_v12/`; unratified input to `methodology-execute`'s 0.1 stop until Jordan adopts v12; resolves nothing at runtime, CLAUDE.md §0.05)

**What this part holds.** Three batches of the IN lane, in execution order: `B00-ids` (the id and row blocks every later batch draws from), `B01-laneA` (implementation lane A's two commits, rebased), `B02-tests` (the test owners, the conjunct record of the nine, and the instrument lines every later close quotes). Each batch is one block with one close, in the form of `V12_STRUCTURE_part2.md` §5.2 and §5.3. A part cites another part's batch or item by handle only; the head's index maps a handle to its file.

**Words.** `unified/U1_GLOSSARY.md`; a person's numbers are an attribute, a skill and its skill score, a derived score (A-98); a *lap* is one pass of the season's scene budget and a *round* is one engagement of a fight (A-101). Source text that says `round` for the season's pass is copied with `NAMES:` where the item lands after B04 (none in this part does: every item here lands before `PCR-4`, so the season's `(season, round)` key keeps the tree's word).

**Paths.** As `V12_STRUCTURE.md` states: a bare path is under `proposals/2026-11-12-subsystem-audit-suite/`; `U3` is `unified/U3_DEPENDENCY_ORDER.md`; `IS-A` is `master/instructions/IS_A_NINE.md` and `_part2`; `CIP` is `master/CODEBASE_IMPROVEMENT_PROPOSAL.md` and `_part2`; `the intake` is `master/eval/V12_INTAKE.md`. A path under `engine/`, `tools/`, `references/`, `registers/`, `tests/` is the repository's.

---

## Batch B00-ids · lane IN · wave W0 · step S0 · HASH EQUAL
INVOCATION: /methodology-execute Batch B00-ids
IN-FLIGHT ROW: registers/handoffs/HANDOFF_IN.md, Open table
GATE: none (the plan's first batch; its base is the working tree head on which v12 is adopted)
HASH READING: `PYTHONHASHSEED=0 python -c "import sys; from engine.season.harness.populated import build_realm; from engine.season.harness.populated import run; s, k = int(sys.argv[1]), int(sys.argv[2]); w = build_realm(s); run(k, s, w=w); print(w.content_hash())" <s> <k>` → the realm content hash at seed `<s>` after `<k>` seasons: `<k>` = 1, one season, unless the gate names two (never more before B99, D-17); `<k>` = 0 reads the build hash; per item `<s>` = 0 (a mover's reading, E-2), at `.99` `<s>` = 0, 1, 2; each value quoted `reading @<sha>`, the tree it was read on (`workplan_v12.md` §3.B, "the hash reading") (this batch runs before B03c moves the builder to `engine/season/boot/realm.py`).
REQUIREMENT: none — allocation (`STAGES.md`, "Parallel sessions" rule 4: ids are allocated up front and land on `main` before any session cites a number; CLAUDE.md §4)
BATCH GATE: `python -m engine.season.harness.register --check` → each check's violation count (R2, G6 and any other that reports) does not rise from the reading taken at the batch's opening (quote both, `reading @<sha>`) (no duplicate id, `register.py::rule_R0`);
  `python tools/validate_ed_citations.py` → exit 0; `python tools/currency_consistency_check.py` → exit 0;
  `python -c "import yaml; d=yaml.safe_load(open('references/id_reservations.yaml')); print({k: v['next_free'] for k, v in d['lane_ids']['lanes'].items()})"` → each lane's value equals the plan's id-block table's last block end + 1 for that lane;
  `python -m engine.season.harness.register --requirements` → exit 0, nine lines (unchanged: `reading @<base sha>`); `python tools/m1_acceptance.py --summary` → its verdict line, quoted;
  the suites `python tools/tests_for_diff.py --base <batch-start-sha>` names;
  the close's commit body records `register --requirements` (nine lines), `m1_acceptance --summary`'s verdict line, the batch's measured wall time (build and close apart, `V12_STRUCTURE.md` §2.4); no conjunct is named, so no `reading:` record is written and `status:` is not edited (`IS-A-12`).
RE-PIN: none
IDS: ED-IN 2; H 0
DIALS AT CONTROL: none
C(B00-ids): this batch's entries; the plan's head parts (the id-block table, the batch table); `references/id_reservations.yaml`; `engine/season/hole_register.yaml` (its highest id only); `registers/editorial_ledger_in.jsonl` (its last row, for the shape);
  `workplans/valoria_master_workplan_v11_part15.md` §5 H-1 and §4 M31, M32 (read whole for B00.02: the relayed words are copied from it); `tools/validate_ed_citations.py`; `engine/season/harness/register.py` (`rule_R0`);
  the permanent surface (CLAUDE.md, `CURRENT.md`, `HANDOFF.md`, `registers/handoffs/HANDOFF_IN.md`, the skill and `methodology-close`).
SERIAL EDGES: B00.01 → B00.02 (B00.02 takes its two ED-IN ids from B00's own block, which B00.01 writes).
  `references/id_reservations.yaml`: B00 alone (no later batch edits `next_free`; each takes from its block).
PARALLEL: S0, alone.
COST: edit; `sonnet`, high; no judgment node (the counts are the authors' declared `IDS:` lines, summed by script).
EST: 3 h [estimate]

| pos | item | source | state | hash | gates on |
|---|---|---|---|---|---|
| B00.01 | every batch's ED and H block, allocated and landed on `main` | U3 §1 item 1; `V12_STRUCTURE_part3.md` §7.5 | BUILD | EQUAL | the plan's id-block table (H2) |
| B00.02 | Jordan's 2026-10-28 words, recorded as relayed (M31, M32) | the intake H-1; A-111 | BUILD | EQUAL | B00.01 |

### B00.01 — allocate every batch's ED block and hole-register block, and land the bump first · U3 §1 item 1 · BUILD · HASH EQUAL
- SOURCE: `unified/U3_DEPENDENCY_ORDER.md` §1 item 1; `master/workplan_v12/V12_STRUCTURE_part3.md` §7.5 (which completes it); `unified/U3_CONFLICT_LEDGER.md` T-4; rulings none; closes nothing (allocation).
- ADVANCES: none of the nine; the precondition of every parallel step (`STAGES.md`, "Parallel sessions" rules 4 and 5).
- INSTRUCTION (U3 item 1, then §7.5's five steps, copied):
  U3: "Allocate, on the working tree head and before any batch cites a number: a block of lane-tagged ED ids per batch from `references/id_reservations.yaml` `next_free` (bumped, co-committed); a block of hole-register ids beginning at the register's next free id (`H-363` at this read; the file has no H key, `U3_CONFLICT_LEDGER.md` T-4), split into per-batch sub-blocks, recorded in the close."
  §7.5: "Readings at `7c37586`, re-read by B00 on its base: `references/id_reservations.yaml` `lane_ids.lanes.<LANE>.next_free` is MB 82, PC 60, FI 10, SC 41, FA 40, WR 13, IN 361, GO 3, SE 57; the highest hole-register id in `engine/season/hole_register.yaml` is H-362, and the file holds no next-id key. B00: (1) sums each batch's declared `IDS:` counts; (2) gives each batch, in §2.1's order within its lane, an ED block of its count plus two and an H block of its count plus five `[ASSUMPTION: the spare — basis: none measured; a batch that runs out stops and takes the next free id on main, it never borrows a sibling's]`; (3) moves each lane's `next_free` past its blocks, with one comment line pointing at the plan's id-block table, co-committed; (4) writes the table into part 2 in the same commit; (5) lands on `main` before any session cites a number (CLAUDE.md §4). A two-lane batch takes its ED ids from SE. Ids a batch did not use are named in its expunge commit body and are not re-used. Lane A's row is renumbered from `H-275` in B01 (C3-A1) from B01's own block."
  Added by this plan (the order of the five steps on the tree): step 0, re-read the nine `next_free` values and the highest `id: H-` in `hole_register.yaml` on this batch's base and write both readings in the commit body (`reading @<base sha>`); the H blocks begin at that highest id + 1, whatever it reads. B00's own block is the first IN block: B00.02 takes its two ids from it. The hole-register blocks live only in the plan's id-block table and in this commit body: `id_reservations.yaml` gains no `H` key (U3 item 1; T-4), and `register.py::rule_R0`'s duplicate refusal stays the one check.
- WHERE: `references/id_reservations.yaml` (`lane_ids.lanes.<LANE>.next_free` for each of the nine lanes, and one comment line per lane pointing at the plan's id-block table); the plan's head part 2, the id-block table (columns: batch · ED lane and range · H range).
- TESTS: none new. The covering reader of `id_reservations.yaml` is `tools/validate_ed_citations.py` and `tools/currency_consistency_check.py` (both read the file; `grep -rl id_reservations tools` lists them with `ci_common.py`, `ci_register_size_check.py`, `build_identifier_census.py`); no test under `tests/valoria` or `engine/season/tests` names the file.
- FALSIFIER and CONTROL: two batches of one lane hold overlapping ranges, or a lane's `next_free` is at or below the end of a block the table gives it (then a session allocating by `next_free` collides with a pre-allocated id). Control: `register --check` and `validate_ed_citations.py` read exit 0 before and after (no id is written to a ledger or register by this item).
- GATE: `python tools/validate_ed_citations.py` → exit 0; `python -m engine.season.harness.register --check` → each check's violation count (R2, G6 and any other that reports) does not rise from the reading taken at the batch's opening (quote both, `reading @<sha>`); a one-line script over the table → no two ranges of one lane overlap, and each lane's `next_free` = its last block's end + 1 → prints `ok` per lane.
- HASH MOVERS: none.
- DEPENDS ON: V12 the plan's id-block table, made by H2 from every batch block's `IDS:` line (`V12_STRUCTURE_part3.md` §7.2, §7.5); EXISTS-IN-TREE `references/id_reservations.yaml::lane_ids.lanes`, `engine/season/harness/register.py::rule_R0`.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, high.
- LANDS IT: B00's `valoria-author` producer, `isolation: worktree`; one `Item: B00.01` commit, `[skip ci]`; the batch's PR lands on `main` before any other session opens (§7.5 step 5).

### B00.02 — Jordan's 2026-10-28 words, recorded in the IN ledger as relayed · H-1 · BUILD · HASH EQUAL
- SOURCE: the intake `:102-104` (H-1, carry-forward E5 Block D8, which copies `workplans/valoria_master_workplan_v11_part15.md` §5 H-1); ruling A-111 (`unified/DECISIONS_ANSWERED.md:147`: "v12 carries the owed ledger rows (M31, M32) as relayed, marked 'Jordan's words relayed, not recorded'; A-104 already supersedes the menu-budget part"); A-104; closes H-1.
- ADVANCES: none of the nine; the record of two rulings v11's M31 and M32 rest on.
- INSTRUCTION:
  1. `registers/editorial_ledger_in.jsonl`: append two rows, ids `ED-IN-<B00 block slot 1>` and `ED-IN-<B00 block slot 2>`, each with the keys of the file's last row (`id`, `date`, `system`, `status`, `needs_jordan`, `confidence`, `supersedes_row`, `superseded_by`, `citations`, `source`, `description`, `canonical_source`), `needs_jordan: false` (A-111 answered it).
  2. Row 1, M32's combat half: `description` opens with "Jordan's words relayed, not recorded:" and quotes, as the carry-forward block gives them, *"we wouldn't really forecast though"* (the no-forecast combat directive M32's combat half waits on), and with it the troop and equipment directions *"troops can be modeled somewhat after games like rotk and total war … equipment can be from tactical RPGs"* and the story-variety concern *"relying 100% on primitive emergence … could produce too many similar stories"*, each marked as relayed in a digest; `citations` name `workplans/valoria_master_workplan_v11_part15.md` §5 H-1 and §4 M32, and A-111.
  3. Row 2, M31 (b)'s budget words: `description` opens the same way and quotes *"menu based management wouldn't take up any budget. the budget is for playable scenes where the character actually interacts within the world"*; `superseded_by: ["ED-IN-0360"]` (the row that records A-104, "management orders cost no scene budget", whose `citations` name "A-104 (E-3 / M31(b))"); `citations` name `…_part15.md` §4 M31 (b), A-111, A-104.
  4. The commit body says "H-1 closed: rows written as relayed (A-111)". The other relayed items H-1 lists (Jordan's three "yes" decisions of 2026-10-28, whose contents are not in hand; the 2026-10-30 instruction; ED-IN-0304's narrowed PLAN line, "its contents Jordan's") are not written: A-111 names M31 and M32 only.
- WHERE: `registers/editorial_ledger_in.jsonl` (two appended rows).
- TESTS: none new.
- FALSIFIER and CONTROL: a row whose `description` does not open "Jordan's words relayed, not recorded" (it would read as a recorded ruling), or an id outside B00's block. Control: `validate_ed_citations.py` exit 0 before and after.
- GATE: `python tools/validate_ed_citations.py` → exit 0; `python -c "import json; rows=[json.loads(l) for l in open('registers/editorial_ledger_in.jsonl')]; print([r['id'] for r in rows[-2:]])"` → the two ids of B00's block.
- HASH MOVERS: none.
- DEPENDS ON: V12 B00.01 (the block); EXISTS-IN-TREE `registers/editorial_ledger_in.jsonl` row `ED-IN-0360`.
- GLOSSARY: none.
- IDS: ED-IN block slots 1 and 2.
- COST and TIER: edit; `sonnet`, medium.
- LANDS IT: B00's producer; `Item: B00.02` commit, the batch's last (no `[skip ci]`).

| STOP. Batch B00-ids closes here |

---

## Batch B01-laneA · lane IN · wave W1 · step S1 · HASH MOVER, one re-pin
INVOCATION: /methodology-execute Batch B01-laneA
IN-FLIGHT ROW: registers/handoffs/HANDOFF_IN.md, Open table
GATE: Batch B00-ids
HASH READING: `PYTHONHASHSEED=0 python -c "import sys; from engine.season.harness.populated import build_realm; from engine.season.harness.populated import run; s, k = int(sys.argv[1]), int(sys.argv[2]); w = build_realm(s); run(k, s, w=w); print(w.content_hash())" <s> <k>` → the realm content hash at seed `<s>` after `<k>` seasons: `<k>` = 1, one season, unless the gate names two (never more before B99, D-17); `<k>` = 0 reads the build hash; per item `<s>` = 0 (a mover's reading, E-2), at `.99` `<s>` = 0, 1, 2; each value quoted `reading @<sha>`, the tree it was read on (`workplan_v12.md` §3.B, "the hash reading") (this batch runs before B03c moves the builder to `engine/season/boot/realm.py`).
REQUIREMENT: R-04.c5 (i) → `aperture 2 s`, s = 0–2: `challenge` executed above 0 at each seed (lane A's 26 / 19 / 24 is a comparison, not a target; IS-A §12.2); and `IS-PC-03`'s reading (below)
BATCH GATE: `PYTHONHASHSEED=0 python -m engine.season.harness.aperture 2 s` for s = 0, 1, 2, before (`reading @<base sha>`) and after, quoted: `challenge` executed above 0 at each seed; at formation `exists:Person` 0, `dispute=False` 0; `accept` refusals with last read `exists:challenge` 0; `comply`'s `exists:dispensation` refusals 0 (U3 §1 item 2; lane A's gate);
  the planted-dispute run fires and its revert does not: `python -m pytest engine/season/tests/test_b11a_duel_reach.py engine/season/tests/test_b11a_scores_and_obstacle.py -q` → green;
  same seed twice, same hash: `build_realm(0)` then one season, run twice → equal `World.content_hash()`;
  `python -m engine.season.harness.register --check` → each check's violation count (R2, G6 and any other that reports) does not rise from the reading taken at the batch's opening (quote both, `reading @<sha>`), and `git grep -n "H-275" -- engine/season` → only CR-79's row and its own citations (C3-A1);
  `IS-PC-03` (a reading, no code): the same `aperture 2 s` runs quote `attempted` and `executed` for `fight`, `challenge`, `accept`, `capture`, and the count of fights by ending kind (`combat.fight` through the `ENGINES` line is read at B02's close: the block is `CI-11`'s, landed in B02; moved there, `V12_STRUCTURE_part2.md` §5.8);
  `python -m engine.season.harness.register --requirements` (nine lines); `python tools/m1_acceptance.py --summary` (its verdict line);
  the suites `python tools/tests_for_diff.py --base <batch-start-sha>` names (engine core: the full gates);
  the close's commit body records `register --requirements`, `m1_acceptance --summary`'s verdict line, R-04.c5 (i)'s reading with its tree, the batch's measured wall time (build and close apart); no `reading:` record is written (the record's form lands in B02, `IS-A-01`); `status:` is not edited.
RE-PIN: every realm and corpus pin the two commits move, re-recorded once in B01.02 against the rebased tree (the branch's own re-recordings are pins of `1424aa7`'s world and are discarded, C3-A2): the build hash at seed 0; the one-season realm hashes at seeds 0–2; the pins the two commit bodies list (`cp_t02_06`, `rem30`, `go07` with its acts, census and counts, `strife`, `weather` `BASE_HASHES`/`EVENTS` and the give/thread-withheld arms, `in27`, `cr33`'s control, `cr81` `PARENT_HASHES`, the governance act counts, the corpus sets, `w9` depths, `tend`, `sc01`'s bar, `cr20`, `odds_of`, `in12_step9`); `engine/season/runs/results.json` regenerated by `engine/season/harness/report.py`. Baseline: the working tree's pins at the batch's base.
EXPECTED RED UNTIL B01.02 (under `[skip ci]`, E-1; one batch line, repair lane R1): the realm and corpus pins any mover item of this batch moves read red from its first mover (B01.01) to the re-pin; the files that pin them (the ones B02.01 names as carrying pins B01's two commits add, `workplan_v12_part3.md` B02.01 item C): `engine/season/tests/test_cp_t02_06_continuations.py`; `engine/season/tests/test_rem30_character_sheet.py`; `engine/season/tests/test_go07_canonical_digest.py`; `engine/season/tests/test_strife_flows.py`; `engine/season/tests/test_strife_credit.py`; `engine/season/tests/test_season_weather.py`; `engine/season/tests/test_in27_endings.py`; `engine/season/tests/test_cr33_lifepaths.py`; `engine/season/tests/test_cr81_realm_acquaintances.py`. (B01's re-pin rides B01.02's cherry-pick, which re-records its own pins; `_realm_goldens.py` is B02's.)
IDS: ED 0; H 1
DIALS AT CONTROL: `unauthored_attributes` = 2 on every key (= `pool_default`); set by BA1's content (`IS-A-11` stage 2: the cast's attributes and skill scores); target: R-09.b, "two actors at different pools: yes" on a non-combat verb. `task_difficulty` rows = person contests 1.0, inquiries 2.0 (a calibration to the old mean, "[ASSUMPTION: the per-task values are Jordan's]" in `c5bf18a`'s body); set by B05 (C3-A3: the roster is re-homed under OBS §1's one roster) and BA1 (`IS-A-11` stage 1 (b): per verb, `difficulty:`); target: none stated beyond R-09.b.
C(B01-laneA): this batch's entries; the plan's head parts; the branch `worktree-agent-a737f996de1fa4752` (`git show e5d6ab9`, `git show c5bf18a`: both commit bodies read whole, they carry the gate's before/after readings and the pin list);
  `unified/U3_CONFLICT_LEDGER.md` T-1 to T-3, T-6, C3-A1, C3-A2, C3-A3; `unified/OWED_TO_UNIFICATION.md` §E; `proposals/03_PC_duel_chain_reach.md` (Gate, Falsifier: read whole);
  the 33 shared files (T-2's list, re-derived by the `comm -12` T-2 names) and the other 16 files of the two commits; `engine/season/hole_register.yaml`; `engine/season/harness/aperture.py`; `engine/season/harness/report.py`; `engine/season/runs/results.json`;
  B00's closing SHA and its id-block row for B01; the permanent surface.
SERIAL EDGES: B01.01 → B01.02 (`c5bf18a` is the child of `e5d6ab9`; `test_b11a_duel_reach.py` is edited by both).
  With other batches: B01 is based on the head after B00 and every later batch on the head after B01 (C3-D1); `rosters.yaml`, `verb_table.yaml`, `data/fixtures.py`, `data/verbs.py`, `decision/options.py`, `queries/world_q.py`, `seam/wrappers/pool.py`, `seam/wrappers/sigma.py`, `loop/witness.py`: B01 first, then their census order (U3 §5.1).
PARALLEL: S1, alone.
COST: build (a rebase over 33 shared files); `sonnet` high produces; `opus` reads the resolution of each conflicted hunk in a shared file (a judgment node: which text is the working tree's and which lane A's).
EST: 3 h [estimate]

| pos | item | source | state | hash | gates on |
|---|---|---|---|---|---|
| B01.01 | computed play reaches the duel: `e5d6ab9`, rebased | `03_PC_duel_chain_reach`; lane A `e5d6ab9`; C3-A2; A-93 | BUILD | MOVER(behaviour) | Batch B00 |
| B01.02 | persons hold scores and the obstacle is the task's difficulty plus named terms: `c5bf18a`, rebased, its hole-register row renumbered; the batch's re-pin | lane A `c5bf18a`; C3-A1, C3-A2 | BUILD | MOVER(behaviour) | B01.01 |

### B01.01 — computed play reaches the duel: lane A's `e5d6ab9` on the current tree · 03_PC_duel_chain_reach · BUILD · HASH MOVER(behaviour)
- SOURCE: `unified/U3_DEPENDENCY_ORDER.md` §1 item 2; `unified/U3_CONFLICT_LEDGER.md` C3-A2 ("Rebase, do not redo"), T-1, T-2; `proposals/03_PC_duel_chain_reach.md` (Gate, Falsifier, Implementation); `unified/OWED_TO_UNIFICATION.md` §E; the commit `e5d6ab9` on branch `worktree-agent-a737f996de1fa4752`; rulings A-93 (B01 may push the rebased branch and open its PR); closes F-PC-01 (as far as formation reaches).
- ADVANCES: R-04.c5 (i).
- INSTRUCTION:
  1. On a worktree at the head after B00: `git cherry-pick --no-commit e5d6ab9`. C3-A2: "resolves the 33 shared files toward the working tree's text and re-applies lane A's edits on top … the branch's `results.json` and realm pins are of `1424aa7`'s world and are discarded, not merged". So: in each conflicted code or data file, keep the working tree's text and re-apply the commit's hunk on top of it; in each pin-bearing test file and in `engine/season/runs/results.json`, keep the working tree's pinned values (they are re-recorded once in B01.02) and keep the commit's non-pin edits (new assertions, new tests, adjusted rows).
  2. What the commit builds, which the rebase keeps unchanged (its own body, the six links, each at its owner): (1) formation: `capture` declares `Person`; a `Record` row whose cell asks a sub-kind forms only on a document the person's own reading says is that kind (writ rows), or that he holds and has not read as another kind (`carry`/`found`/`build`, which join `own_hold_declines`): `options.documents_known_as`, `verbs.RECORD_SUBKINDS_BY_VERB`/`_HELD`; (2) the grievance is the occasion: `world_q.disputes_held` stamps, as the new class `Disputant`, each man beside a person that he holds a dispute with (`person_q.holds_dispute`, the one owner); `challenge` declares it and gains `individual` on both parties; (3) the challenged hears it: `rosters.yaml: read_to_addressee: [challenge]`, WITNESS deposits a challenge's content to a witnessing addressee (`witness.addressee_reads`); `world_q.challenges_heard` stamps it; the Record stays in the challenger's hand (ED-IN-0292 (1) stands); (4) `accept`'s `to` is the challenge's own `challenger` (`operand_bags`' document branch); (5) `rosters.yaml: opposed_without_prize: [challenge]`; (6) `duel` dropped from `fight`'s violence line. The proposal's own "Exact edits" table (a `dispute` violence context, `challenge` classed `Person`) is the first cut the commit body records as replaced ("fell to 11 formations on 53 standing grievances"); C3-A2 lands the commit, not that table.
  3. Commit with the commit's own subject and body, the line "rebased from `e5d6ab9` (C3-A2); pins re-recorded in B01.02", and the trailer `Item: B01.01`.
- WHERE: as the commit: `engine/season/data/rosters.py`, `engine/season/data/verbs.py`, `engine/season/decision/options.py` (`opening_set`, `documents_known_as`, `operand_bags`), `engine/season/loop/witness.py` (`addressee_reads`), `engine/season/queries/world_q.py` (`disputes_held`, `challenges_heard`), `engine/season/rosters.yaml` (`read_to_addressee`, `opposed_without_prize`, `violence_contexts`), `engine/season/verb_table.yaml` (`challenge`, `accept`, `capture`, `fight`), NEW `engine/season/tests/test_b11a_duel_reach.py`, and the 20 adjusted test files the commit lists; `engine/season/runs/results.json` (kept at the working tree's value).
- TESTS: `engine/season/tests/test_b11a_duel_reach.py` (the commit's falsifier: "a planted grievance on a two-man world forms the challenge, the fold issues it, the challenged reads it, forms one `accept` against the challenger and the encounter fights it (a drawn band); with `revert_b11a` the challenged holds no reading and forms no `accept`"); written by the commit, read green after the cherry-pick. The proposal's named file `test_duel_chain_reach.py` is not written: the commit's file carries its assertions.
- FALSIFIER and CONTROL: the proposal's: "A seeded realm with one planted dispute … produces, through the real chooser and with no hand-built act, `challenge.issued`, then an `accept` by the challenged, then a fight under `blood` terms with `duel.yielded`. If it does not, the chain has a further break". Control: `revert_b11a` reproduces the parent's one-season realm hashes at seeds 0–2 exactly (on the rebased tree: the head after B00).
- GATE: `PYTHONHASHSEED=0 python -m engine.season.harness.aperture 2 s`, s = 0, 1, 2: `challenge` executed above 0 at each seed; last-read `exists:Person` 0 and `dispute=False` 0; `accept`'s `exists:challenge` 0; `comply` formed on no non-dispensation Record. `python -m pytest engine/season/tests/test_b11a_duel_reach.py -q` → green. Pin-bearing tests the commit adjusted read red until B01.02's re-pin (expected; their pins are the base's).
- EXPECTED RED UNTIL B01.02 (E-1, under `[skip ci]`): the pin-bearing tests the commit adjusted (the build and one-season realm hashes, the corpus sets, the governance act counts; the "RE-RECORDED PINS" list of `e5d6ab9`'s body) read red between this item and B01.02's re-pin, their pins being the base's. (Added by check lane K1 from this item's own GATE sentence.)
- HASH MOVERS: every seeded pin where `challenge`, `accept`, `comply`, `capture`, `carry`, `found` or `build` formed: the build and one-season realm hashes, the corpus sets and the governance act counts (the commit's "RE-RECORDED PINS" list). Declared; B01's one re-pin in B01.02.
- DEPENDS ON: EXISTS-IN-TREE `queries/person_q.py::holds_dispute`, `decision/options.py::VIOLENCE_CONTEXT_READERS`, `::opening_set`, `rosters.yaml: violence_contexts`; the commit `e5d6ab9` (`git cat-file -t e5d6ab9` → `commit`, read 2026-11-12).
- GLOSSARY: `Disputant` (a new class): the ordinary reading, "a person in a dispute with another", in one sentence at its row of `unified/U1_GLOSSARY.md`, added in this commit if no row has it.
- COST and TIER: build; `sonnet`, high; the resolution of each conflicted hunk in `rosters.yaml`, `verb_table.yaml`, `decision/options.py`, `queries/world_q.py`, `loop/witness.py` read by `opus`.
- LANDS IT: B01's producer; `Item: B01.01`, `[skip ci]`.

### B01.02 — persons hold scores; the obstacle is the task's difficulty plus named terms: lane A's `c5bf18a`, its row renumbered; the batch's re-pin · lane A `c5bf18a` · BUILD · HASH MOVER(behaviour)
- SOURCE: `unified/U3_DEPENDENCY_ORDER.md` §1 item 2; `unified/U3_CONFLICT_LEDGER.md` C3-A1 (the ordered edit instruction), C3-A2, C3-A3, T-3, T-6; the commit `c5bf18a`; rulings A-93; the intake has no entry.
- ADVANCES: none of the nine by itself (R-09.b waits on BA1's values: "THE REALM'S OBSTACLE IS STILL ALMOST ALWAYS 2.0 at the shipped content", the commit's own reading); the starting point B05 replaces (C3-A3).
- INSTRUCTION:
  1. `git cherry-pick --no-commit c5bf18a` on the tree after B01.01, resolving as B01.01 step 1.
  2. What the commit builds, kept: (3) persons hold scores: `rosters.yaml: unauthored_attributes` (closed over the ten registry keys, `data/rosters.py`) seated under every person's authored `stats:`; `build_realm(cast_attributes=...)` ships True; shipped at 2 on every key (= `pool_default`); (4) `seam/wrappers/pool.py::score` split out of `faculty`; `sigma._opposition_of` returns it for any person; `modules/social_contest/roll.py::obstacle_terms`: Ob = the task's difficulty (`rosters.yaml: task_difficulty`, refused at import where a task has none) + the opposing person's score/2 − room terms + forgery, under the ceiling, each term named on the roll's record (`ob_terms`); `Fixtures obstacle_model`: `task` ships, `stand_in` is the control; `verb_capability`: interrogate→inquiry, arrest→arms, determine→argue; `sigma._PROVIDER` reads `data/verbs.py::SOCIAL_ROLL_PROVIDER`. C3-A3: "lane A's code is their starting point, not a second form": `max(attr, have)`, `/ 2.0`, the room's subtraction and the names `task_difficulty`, `ob_terms` are kept here and replaced in B05.
  3. C3-A1, copied: "(1) `hole_register.yaml`: the B11-A row's `id: H-275` → the allocated id; (2) `engine/season/data/fixtures.py:453` and `:458` comments `` `H-275` `` → the allocated id; (3) `engine/season/seam/wrappers/sigma.py:144` comment `H-275` → the allocated id; (4) the commit body says 'renumbered from H-275 (collision with CR-79, #581)'." The allocated id is B01's H block slot 1 (B00). The line numbers are the branch's; on the rebased tree find the three sites by `git grep -n "H-275" -- engine/season` and edit every line whose subject is the obstacle (`obstacle_model`, "HOW THE SOCIAL ROLL'S OBSTACLE IS COMPOSED"), never CR-79's `regime_gain` lines.
  4. The batch's re-pin, in this commit: re-record every pin the RE-PIN line names, once, on this tree, `PYTHONHASHSEED=0`; regenerate `engine/season/runs/results.json` with `engine/season/harness/report.py`; the commit body says "re-pin" and lists each pin's before (`reading @<base sha>`) and after.
  5. Commit with the commit's own subject and body, the renumbering line, "rebased from `c5bf18a` (C3-A2)", "re-pin", and `Item: B01.02`. Then push the branch and open the batch's PR for Jordan's review (A-93).
- WHERE: as the commit: `engine/season/data/fixtures.py` (`obstacle_model`), `engine/season/data/rosters.py`, `engine/season/data/verbs.py` (`SOCIAL_ROLL_PROVIDER`), `engine/season/harness/populated.py` (`build_realm`'s `cast_attributes`), `engine/season/hole_register.yaml` (the B11-A row, renumbered), `engine/season/queries/inputs.py`, `engine/season/rosters.yaml` (`unauthored_attributes`, `task_difficulty`), `engine/season/seam/wrappers/pool.py` (`score`), `engine/season/seam/wrappers/sigma.py` (`_opposition_of`, `_PROVIDER`), `modules/social_contest/roll.py` (`obstacle_terms`), NEW `engine/season/tests/test_b11a_scores_and_obstacle.py`, and the adjusted test files the commit lists; `engine/season/runs/results.json`.
- TESTS: `engine/season/tests/test_b11a_scores_and_obstacle.py` (the commit's: `obstacle_model: stand_in` composes the old obstacle byte for byte over a 72-record grid; scores 1/2/4/6 give strictly rising Ob and P(Failure)); read green after the cherry-pick; every pin-bearing test green after step 4.
- FALSIFIER and CONTROL: the commit's: "`revert_b11a_scores` (the switch, the bundle off, the three rows off) reproduces the reach commit's one-season realm hashes at seeds 0-2 exactly" (on this tree: B01.01's). Planted (C3-A1): a second row `id: H-275` → `register --check` exits non-zero.
- GATE: `python -m pytest engine/season/tests/test_b11a_scores_and_obstacle.py engine/season/tests/test_b11a_duel_reach.py -q` → green; `python -m engine.season.harness.register --check` → each check's violation count (R2, G6 and any other that reports) does not rise from the reading taken at the batch's opening (quote both, `reading @<sha>`); `git grep -n "H-275" -- engine/season` → CR-79's row and its own citations only; then the batch gate.
- HASH MOVERS: the build hash (the seated `unauthored_attributes`) and every season hash (the obstacle by task, `cast_attributes` on); the corpus (`determine` leaves refused_only), the aperture pools {2} → {2, 5}. Declared; this commit is B01's one re-pin.
- DEPENDS ON: V12 B01.01; V12 B00.01 (B01's H block); EXISTS-IN-TREE `engine/season/hole_register.yaml` row `H-275` (CR-79, `regime_gain`), `seam/wrappers/pool.py::faculty`, `modules/social_contest/roll.py`; the commit `c5bf18a` (`git cat-file -t c5bf18a` → `commit`, read 2026-11-12).
- GLOSSARY: `obstacle_model` and `task_difficulty` are tree names U1 replaces in B05 (C3-A3: "Which names survive is U1's"); no row is edited here.
- NAMES: none in this part (the obstacle's names are B05's to change).
- IDS: H block slot 1 (the renumbered row).
- COST and TIER: build and the re-pin; `sonnet`, high; the resolution of `seam/wrappers/sigma.py`, `pool.py` and `data/fixtures.py` read by `opus`.
- LANDS IT: B01's producer; `Item: B01.02`, the batch's last (no `[skip ci]`).

Note for the BA1 author (not an edit here): after B01.02, `build_realm`'s `cast_attributes` ships True at value 2 on every key (`c5bf18a` step 3); `IS-A-11` stage 2 step 2 ("the `cast_attributes` default flips to on") then finds the switch on and lands only the values.

| STOP. Batch B01-laneA closes here |

---

## Batch B02-tests · lane IN · wave W2 · step S2 · HASH EQUAL
INVOCATION: /methodology-execute Batch B02-tests
IN-FLIGHT ROW: registers/handoffs/HANDOFF_IN.md, Open table
GATE: Batch B00-ids
GATE: Batch B01-laneA
HASH READING: `PYTHONHASHSEED=0 python -c "import sys; from engine.season.harness.populated import build_realm; from engine.season.harness.populated import run; s, k = int(sys.argv[1]), int(sys.argv[2]); w = build_realm(s); run(k, s, w=w); print(w.content_hash())" <s> <k>` → the realm content hash at seed `<s>` after `<k>` seasons: `<k>` = 1, one season, unless the gate names two (never more before B99, D-17); `<k>` = 0 reads the build hash; per item `<s>` = 0 (a mover's reading, E-2), at `.99` `<s>` = 0, 1, 2; each value quoted `reading @<sha>`, the tree it was read on (`workplan_v12.md` §3.B, "the hash reading") (this batch runs before B03c moves the builder to `engine/season/boot/realm.py`).
REQUIREMENT: R-01.a, .b, .c; R-02.a, .b; R-03.a, .b; R-04.b; R-06.d, .e; R-07.a; R-08.b, .c; R-09.a → all `yes`; R-01, R-02, R-03 read `met` with every conjunct held and the six others print their held counts; the first `BUILT OUT`, `ENGINES` and `NULL SCENES` baselines (`ENGINES`: `combat.fight` above 0 at seed 0 if B01 did what its gate says; it read 0 at `6e1ea91`) (IS-A §12.2)
BATCH GATE: every pinned hash unchanged against B01's close (`reading @<B01 closing sha>`): `python -m pytest engine/season/tests/test_go07_canonical_digest.py -q` → green with the three shipped pins; each golden has one owner: `git grep -lE '"[0-9a-f]{32}"' -- engine/season/tests` → `_realm_goldens.py` plus the encoding vectors of `test_go07_canonical_digest.py` (U3 §1 item 3);
  `python -m engine.season.harness.register --requirements` → exit 0; nine lines in the form `R-0n  <status>  <held> of <m> conjuncts  tree <oldest reading.tree>`; R-01, R-02, R-03 `met` with every conjunct held; a held row that fails to read is a STOP reported to Jordan, not an edit of the conjunct (`IS-A-02`);
  `python tools/m1_acceptance.py --summary` → its verdict line; row 3 prints `conjuncts held <h> of <m>` and stays DOC-DERIVED;
  `PYTHONHASHSEED=0 python -m engine.season.harness.aperture 1 --seeds 0 1 2` → `CONTROL` EQUAL at each seed; the `ENGINES`, `BUILT OUT`, `FOUGHT FIELDS` and `NULL SCENES` blocks print; their lines are quoted as the baselines every later close reads against (`reading @<B02 closing sha>`);
  `IS-PC-03`'s arm moved here from B01: `PYTHONHASHSEED=0 python -m engine.season.harness.aperture 2 s`, s = 0, 1, 2 → the `ENGINES` line for `combat.fight` above 0 at each seed (expected after B01; a 0 at any seed is `IS-PC-03`'s falsifier);
  `python -m engine.season.harness.storybar --remove --base-seed 0 1 2 --seasons 2` → replay 0 at each seed; `R-01.c` and `R-02.b` lines above 0 at each seed (`IS-A-03`);
  the suites `python tools/tests_for_diff.py --base <batch-start-sha>` names (engine core, tools, a registry: the full gates);
  the close's commit body records `register --requirements` (nine lines), `m1_acceptance --summary`'s verdict line, the named conjuncts' readings with their tree, the `BUILT OUT`, `ENGINES` and `NULL SCENES` lines (no before: they are first printed here) and after, and the batch's measured wall time (build and close apart); the last `Item:` commit writes the conjuncts' `reading:` records; `status:` is not edited outside what `IS-A-02` writes from its own readings (`IS-A-12`).
RE-PIN: none (every item is hash EQUAL; the readings of B01's close are the baseline, `reading @<B01 closing sha>`)
IDS: ED 0; H 0
DIALS AT CONTROL: none
C(B02-tests): this batch's entries; the plan's head parts;
  `engine/season/requirements.yaml` (whole: every row and the `scales:` block); `engine/season/harness/register.py` (`check_requirements`, `REQUIREMENTS`, `main`); `tools/m1_acceptance.py` (`row_nine_requirements`);
  `engine/season/harness/storybar.py` (`drive`, `draw_seed_arm`, the CLI); `engine/season/harness/aperture.py` (`measure_world`, `report`, `pooled_report`, the `CONTROL` line); `engine/season/harness/chronicle.py` (`main`'s parser); `engine/season/harness/decision_spread.py` (`read_decisions`, `play_season`, `print_season`); `engine/season/harness/arms.py`; `engine/season/harness/corpus_run.py` (`attempts`, the `EMITS AND WRITES NOTHING` census); `engine/season/data/verbs.py` (`emits_at`, `writes_at`); `engine/season/write_matrix.yaml`; `engine/substrate/composition.py` (`ROLES`, `require`); `engine/season/data/rosters.py` (`SCALE_OF_RUNG`);
  the test files the items name: `engine/season/tests/test_go07_canonical_digest.py` and the fourteen files of B02.01's table; `engine/season/tests/test_season_shape.py`; `engine/season/tests/test_storybar.py`; `engine/season/tests/test_aperture.py`; `engine/season/tests/test_march.py`; `engine/season/tests/test_content_operands.py`; `engine/season/tests/test_interactions_log.py`; `engine/season/tests/test_in62_decision_spread.py`; `tests/valoria/test_season_invariant_sweep.py`; `tests/valoria/test_m1_acceptance_probe.py`; `tests/valoria/test_balance_oracle_arms.py`; the sites of B02.09 to B02.12 (opened by each item's first step);
  `master/instructions/IS_A_NINE.md` §2 to §10 (read whole by B02.38: its conjunct tables are copied into that item, and the `text` of each conjunct quotes them); `references/restructure_ledger.md` (the `engine/season/harness/arms.py` row);
  B00's and B01's closing SHAs and B01's readings; the permanent surface.
SERIAL EDGES: within the batch: B02.01 first (every later re-pin is one edit of `_realm_goldens.py`, C3-N27); `engine/season/tests/test_season_shape.py`: B02.01 → B02.04 → B02.08 → B02.09 → B02.10 → B02.12 → B02.23 → B02.26; `engine/season/requirements.yaml`: B02.05 → B02.13 → B02.15 → B02.31 → B02.34 → B02.36 → B02.38; `engine/season/harness/register.py`: B02.13 only; `engine/season/harness/storybar.py` (C3-K7, one batch at a time): B02.14 → B02.19 → B02.20; `engine/season/harness/aperture.py` and `engine/season/tests/test_aperture.py`: B02.17 → B02.18 → B02.20; `engine/season/tests/test_storybar.py`: B02.14 → B02.19 → B02.20; `engine/season/tests/test_realm_requirements.py`: B02.21 (creates it) → B02.22 → B02.32; `harness/decision_spread.py`: B02.28 → B02.32.
  With other batches (U3 §5.1): `harness/storybar.py` B02 → B36 → B38; `requirements.yaml` B02 → B03 → B09 → B11 → B17 → B26; `harness/register.py` B02; `decision_spread.py` B02 → B10; `test_season_shape.py` B02 → B11 → B12; `references/restructure_ledger.md` B02 → B03; `test_realm_requirements.py` B02 → B10 (`IS-A-05` part 2).
PARALLEL: S2, alone.
COST: edits and small builds; `sonnet` high produces; no judgment node in the build; `opus` reads `IS-A-02`'s readings against each conjunct's text at the close (the readings move rows' `holds`). Instrument time: `corpus_run` (recorded at 2.5 and at 8 minutes by two lanes), the removal test (about two minutes an arm, six arms), `aperture 1` and `2` at three seeds: launched in the background at B02.38's open on the tree after B02.37 (`STAGES.md` practice 5), each sized first on one seed.
EST: 10 h [estimate]

| pos | item | source | state | hash | gates on |
|---|---|---|---|---|---|
| B02.01 | one owner of the realm goldens; the shipped world is what is pinned | `01_CORE_tests_one_golden_owner` A–D | BUILD | EQUAL | Batch B01 |
| B02.02 | delete the knot-pool prose test | `01_CORE_tests_delete_what_cannot_fail` row 1 | BUILD | EQUAL | — |
| B02.03 | delete the flow-skeleton anchor test and the comment it forced | the same, row 2 | BUILD | EQUAL | — |
| B02.04 | delete the eight substring tests, after their successors are shown to see the change | the same, row 3 | BUILD | EQUAL | B02.01 |
| B02.05 | R-07's `measure:` names the tests that observe it | the same, row 4; `U5a_tests_digest_additions` §F1 | BUILD | EQUAL | B02.04 |
| B02.06 | delete the retired pool-arm pair and the test that kept it importable | the same, row 5 | BUILD | EQUAL | — |
| B02.07 | the envelop test counts two arms over twenty seeds | the same, row 6 | HELD (the MB lane's file: lands in B02 only with that lane's agreement, else in B17) | EQUAL | — |
| B02.08 | delete an unused helper | the same, row 7 | BUILD | EQUAL | B02.04 |
| B02.09 | assertions that cannot fail: a floor or a deletion | `U5a_tests_digest_additions` §A (SITE; `IS-B2-CORE-07`'s first step) | BUILD | EQUAL | B02.08 |
| B02.10 | source-text assertions beyond the eight: each mutation run, then delete or keep | the same, §B (SITE) | BUILD | EQUAL | B02.09 |
| B02.11 | hash literals under a revert stack, beyond B02.01's table | the same, §D2 (SITE) | BUILD | EQUAL | B02.01 |
| B02.12 | count pins and re-pin logs beyond B02.01's list | the same, §E (SITE) | BUILD | EQUAL | B02.10 |
| B02.13 | a row's `met` text is a list of conjuncts the register reads | `IS-A-01` (lands as `01_CORE_requirements_reading_record` §1; with `16_PESSIMIST_CORE_the_nine_gate…` edit 1 and `IS-A-04`'s three register lines) | BUILD | EQUAL | B02.05 |
| B02.14 | the removal test, beside the draw-seed arm | `16_PESSIMIST_CORE_the_nine_gate_and_a_knockout_reading` edit 2 | BUILD | EQUAL | B02.13 |
| B02.15 | R-01 and R-02 measure by the removal test | the same, edit 3 | BUILD | EQUAL | B02.14 |
| B02.16 | the chronicle reads what persons moved against a world where nobody acts | `16_PESSIMIST_GAME_consequence_reading` | BUILD | EQUAL | B02.15 |
| B02.17 | the act-count instrument prints which engines a run entered | `CI-11` | BUILD | EQUAL | B02.16 |
| B02.18 | the act-count instrument prints which verbs are built out, and through which seat | `IS-A-06` | BUILD | EQUAL | B02.17 |
| B02.19 | the removal test states what it expects | `IS-A-03` | BUILD | EQUAL | B02.14, B02.18 |
| B02.20 | the count of scenes that wrote nothing, read from here on | `IS-A-07` | BUILD | EQUAL | B02.18, B02.19 |
| B02.21 | R-01 on the played realm, three seeds, with the witness cut as control | `01_CORE_tests_shipped_world_falsifiers` row 1 | BUILD | EQUAL | B02.13 |
| B02.22 | R-02 on the played realm at the shipped budget | the same, row 2 | BUILD | EQUAL | B02.21 |
| B02.23 | the fork test is named for what it runs | the same, row 3 | BUILD | EQUAL | B02.22 |
| B02.24 | the invariant sweep sees a played realm | the same, row 4 | BUILD | EQUAL | — |
| B02.25 | three loops assert that they saw something | the same, row 5 | BUILD | EQUAL | — |
| B02.26 | a skip on an absent combat engine becomes a failure | the same, row 6; `U5a_tests_digest_additions` §C | BUILD | EQUAL | B02.12 |
| B02.27 | the interactions-log finding is read off the shipped season | the same, row 7 | BUILD | EQUAL | — |
| B02.28 | a self-plea and an accusation are two rows; R-06's test drops its revert | the same, row 8 | BUILD | EQUAL | B02.26 |
| B02.29 | the different-seed test cannot pass on an empty season | the same, row 9 | BUILD | EQUAL | — |
| B02.30 | a fixture that reverted three shipped changes plays the shipped tree | `U5a_tests_digest_additions` §D1 (SITE) | BUILD | EQUAL | B02.27 |
| B02.31 | each scale of play names its conjunct; the stale line about the scale words goes | `IS-A-04` | BUILD | EQUAL | B02.13 |
| B02.32 | R-08.c's test: some chosen acts were not the top candidate, and none at zero temperature | `IS-A-05` part 1 | BUILD | EQUAL | B02.22 |
| B02.33 | the sites of `U5a_tests_digest_additions` opened before each edit | `IS-B2-CORE-07` | POINTER (closed by B02.09, B02.10, B02.11, B02.12, B02.26, B02.30, each of whose first step it is) | EQUAL | — |
| B02.34 | R-05's `measure:` carries a command, no figure | the intake V9-27 | BUILD | EQUAL | B02.13 |
| B02.35 | R-01's and R-02's narrative leaves `requirements.yaml` | the intake DEF-8 | POINTER (closed by B02.13: `measured:` leaves, the history is the file's git log) | EQUAL | — |
| B02.36 | R-03's stale opening text and the file header's "one tick granularity" | the intake H-2 | BUILD | EQUAL | B02.13 |
| B02.37 | `IS-A-12`'s close record is written from this batch's close on | `IS-A-12` | READING (a form: the close line of this batch's BATCH GATE) | EQUAL | — |
| B02.39 | the corpus run takes a seasons cap, so a gate reads it at two seasons | v12 repair R1 (K1 F3, K3 F2; D-17) | BUILD | EQUAL | B02.13 |
| B02.38 | the nine's conjuncts, authored, and the readings this batch takes | `IS-A-02` | BUILD | EQUAL | B02.13 to B02.36, B02.39 |

Position numbers in the SERIAL EDGES line above are this table's. The items follow, in the form of `V12_STRUCTURE_part2.md` §5.3.

### B02.01 — one owner for the realm goldens; the shipped world is what is pinned · 01_CORE_tests_one_golden_owner A–D · BUILD · HASH EQUAL
- SOURCE: `proposals/01_CORE_tests_one_golden_owner.md` "The resolution (decided)" A, B, C, D, "Gate", "Falsifier"; `unified/U3_CONFLICT_LEDGER.md` C3-N14, C3-N27, C3-N30; closes F-TEST-02, F-TEST-03, F-TEST-08 (A–D). Its E (the dice golden, superseded in content by A-5) is not here: it lands in B05 with the sampler (the source's own placement).
- ADVANCES: none of the nine by itself; every later mover batch re-pins one file (STAGES practice 1).
- INSTRUCTION (A to D, copied):
  **A. One owner.** New file `engine/season/tests/_realm_goldens.py` (a test-support module beside `_scar_helpers.py`, not a registry: nothing but tests reads it):
  ```python
  """The realm goldens: one literal per (seed, seasons, arm). Every hash test imports from here.
  A re-record is one edit to this file, in the commit that moves the world, with the mover named in
  that commit's message (CLAUDE.md §7)."""
  BUILD = {0: "600d8b27147478e158553552cc1409a5"}                      # build_realm(seed), unplayed
  SHIPPED = {(0, 1): "5ab73af282d0779646c38839fbab85d8",                # (seed, seasons) at DEFAULT_FIXTURES
             (1, 1): "aa58ef0b71c947ce5ff9f0a75ffd8ca6",
             (2, 1): "a21ab6e12e356ccc4261bec1c93ca3b4"}
  CENSUS = {(0, 1): dict(acts=749, log=13379), ...}                      # read with populated.run
  ```
  The literals above are `main`'s readings before B01 and move at B01 (C3-N27): the edit records its own on its base, `build_realm(s)` + `populated.run(1, s)` at `PYTHONHASHSEED=0`, seeds 0, 1, 2, `reading @<B01 closing sha>`, and they must equal B01's re-pinned values. The module docstring also carries the rule: *an item that moves the realm proves in its own commit that its revert reads the previous pin, and records that in the commit message; the proof is not kept as a test.*
  **B. One test owns the shipped pin.** `test_go07_canonical_digest.py::test_go07_control_the_world_did_not_move_only_its_digest` drops `revert_cr79(monkeypatch)` and its `BASE` block and asserts `SHIPPED` and `CENSUS` at the three seeds. `test_go07_control_the_build_world_old_digest_is_unmoved` keeps one assertion, `build_realm(0).content_hash() == BUILD[0]`. The `_old_content_hash` half of both (the pre-GO-07 `repr` digest) and the `foreign=False` / `acquaintances=False` build variants are deleted. The four encoding-vector tests in that file (`TENURE_VECTOR`, `WORLD_FRAMES`, float bit patterns, set order across `PYTHONHASHSEED`) stay untouched.
  **C. The revert-stacked controls are deleted** (15 tests deleted, the hash arm cut from 2 more; the item's own behaviour and mutation tests in the same files stay):

  | file | test deleted | literals deleted |
  |---|---|---|
  | `test_cp_t02_06_continuations.py` | `test_no_death_means_no_behaviour_change_and_the_realm_hash_is_the_pre_build_hash` | `PRE_BUILD` |
  | `test_cp_t03_01_cohorts_never_fight.py` | `test_control_the_realm_ends_at_the_base_hash_wherever_no_cohort_was_a_party`, `test_where_a_cohort_was_a_party_the_realm_moves_and_the_refusals_are_the_conjuncts` (hash arm only; the refusal-conjunct asserts stay) | `BASE` |
  | `test_cp_t03_02_band_ending_and_body.py` | `test_control_the_item_at_its_revert_reproduces_the_pre_item_one_season_hash` | `PRE_ITEM` |
  | `test_cp_t03_04_arms.py` | `test_control_formation_moves_every_hash_and_the_item_off_reproduces_the_pre_item_hash` | `PRE_ITEM`, `POST_ITEM` |
  | `test_cp_t03_07_body_ceiling.py` | `test_hash_post_item_control_and_revert`, `test_build_hash_is_a_schema_mover_and_the_revert_reads_the_old_one` | `PRE_ITEM`, `POST_ITEM`, `CONTROL`, `BUILD_PRE`, `BUILD_POST` |
  | `test_cp_t03_08_tend_on_the_wounded.py` | `test_hash_post_item_and_revert`, `test_build_hash_is_unmoved` | `POST_ITEM`, `BUILD` |
  | `test_cr33_lifepaths.py` | `test_control_the_expansion_skipped_reproduces_the_pre_commit_hash` | the three-seed block |
  | `test_cr85_faculty_replaces_history.py` | `test_control_faculty_3_for_every_party_reproduces_the_pre_item_hash`; the hash arm of `test_falsifier_every_season_roll_reads_pool_8_against_ob_1` | `PRE_ITEM`, `POST_ITEM` |
  | `test_cr87_violence_contexts.py` | `test_control_the_block_empty_and_every_value_at_its_revert_reproduce_the_pre_item_hash` | `BASE_BUILD`, `BASE_SEASON` |
  | `test_rem30_character_sheet.py` | `test_rem30_creation_arm_off_reproduces_the_pre_build_hash` | the three-seed block |
  | `test_season_weather.py` | `test_in21_control_draw_off_and_draw_at_one_reproduce_the_base_hashes`, `test_the_give_withheld_arm_reproduces_the_one_season_pin` | `BASE_HASHES`, `STEP_OFF_ONE_SEASON`, `BASE_EVENTS` |
  | `test_strife_flows.py` | `test_cr78_control_the_switch_off_reproduces_the_base_hash` | `BASE_BUILD`, `BASE_ONE_SEASON` |
  | `test_cp_t04_07_surrender.py`, `test_cr81_realm_acquaintances.py`, `test_strife_credit.py` | none deleted; each imports `BUILD` / `SHIPPED` from the owner in place of its literal | their copies |

  A `revert_*` helper with no remaining caller is deleted with its last caller; one still used by a behaviour test (`revert_cr87` in `test_interactions_log.py`, until B02.27 lands) stays. B01 added pins to several of these files (`c5bf18a`, `e5d6ab9` bodies: `cp_t02_06`, `rem30`, `go07`, `strife`, `weather`, `in27`, `cr33`, `cr81`): each such literal is a trajectory literal and goes by the same rule.
  **D. The corpus counts go; the properties beside them stay.** In `test_season_shape.py` delete the exact pins and the comment logs that exist only to narrate them, keeping the assertion named in the right-hand column (line numbers are the source's at `785bc62`; find each by its text):

  | deleted | kept beside it |
  |---|---|
  | `len(by_sig) == 136` | `universal == set()`; `ever == {…}`; `refused_only == {…}`; the never-attempted set (R-05's state, exactly) |
  | `d_pub == 10` | `d >= 4`; `redeposits == 1`; no late `ROOT`; the chain's origin is hers |
  | `(depths[3], depths[6]) == (16, 14)`; the `== 10` in `max(depth5…) == 10 < depths[3]` | `matured[0] == 0`; `matured[3] < matured[6]`; `depths[3] > depths[0]`; `max(depth5…) < depths[3]` |
  | `(len(before), len(after)) == (20, 18)` | `dropped == ["exchange", "transfer"]`; `len(after) == len(before) - 2` |
  | the eleven-tuple `actor_end` list; `len(dropped) == 18` | `none_arm == []`; `actor_arm` non-empty; `len(total_arm) >= len(actor_arm)`; `bit == {…}` |
  | the fork tuples `(31, 3)`, `(28, 2)`, `(28, 2)`, `_TRAIN_KIND_GAP`, the `{none: (10, 31), …}` dict | `windows >= 90`; `bad_windows == 0`; every arm `genuine > 0`; `got["total"]["diverged"] > 0`; `5 * acts_differ > genuine` |
  | the one-round arm's event census | `d.resolved` non-empty; the planted-round tests |
  | `total == 85` `raise SystemExit` statements (with the 260-line narrative above it) | `test_h115_the_degree_branches_raise_unspecified_not_systemexit` |
  | the first of the two `len(VERB_TABLE) == 67` assertions | the second (R-05's denominator, once): a reading of the tree (67 rows, U3 T-7), re-read and re-recorded at B25 (A-28's `tie`/`knot` split, 68) and B38 (`riot`, if it lands, 69), quoted with its batch (C3-N30) |
- WHERE: NEW `engine/season/tests/_realm_goldens.py`; `engine/season/tests/test_go07_canonical_digest.py`; the fourteen files of C's table; `engine/season/tests/test_season_shape.py`.
- TESTS: `test_go07_canonical_digest.py::test_go07_control_the_world_did_not_move_only_its_digest` (rewritten: `SHIPPED` and `CENSUS` at three seeds), read green on the base before the deletions (it is the instrument, U3 §6.2: the scratch probes `probe_realm_sweep.py`, `probe_realm_gates.py` are not written).
- FALSIFIER and CONTROL: the source's: "Sweep any shipped fixture in process (`DEFAULT_FIXTURES._v["regime_gain"] = 0.0`) and run the go07 file: the seed-0 pin must redden. If it stays green the owner is not what the test reads." Control: the base tree's go07 run (every content hash stationary; tests only).
- GATE: `python -m pytest engine/season/tests/test_go07_canonical_digest.py -q` → green with the three shipped pins; `git grep -lE '"[0-9a-f]{32}"' -- engine/season/tests` → `_realm_goldens.py` and `test_go07_canonical_digest.py` (its encoding vectors) only; `python -m pytest engine/season/tests/test_season_shape.py -q` → green (the kept assertions stand alone). The source's `gen_sigma_parity_goldens.py --check` arm is item E's and is read in B05 (moved, `V12_STRUCTURE_part2.md` §5.8).
- HASH MOVERS: none (tests only).
- DEPENDS ON: V12 Batch B01 (the pins it re-recorded are this file's starting values); EXISTS-IN-TREE `engine/season/tests/_scar_helpers.py`, `test_go07_canonical_digest.py`, `harness/populated.py::build_realm`, `::run`.
- GLOSSARY: none.
- COST and TIER: edit, mechanical in fourteen files, the judgement in D (each kept assertion still stands alone, which the table settles); `sonnet`, high.
- LANDS IT: B02's `valoria-author` producer, `isolation: worktree`; one `Item: B02.01` commit, `[skip ci]`.

### B02.02 — delete the test whose subject is a formula in archived prose · 01_CORE_tests_delete_what_cannot_fail row 1 · BUILD · HASH EQUAL
- SOURCE: `proposals/01_CORE_tests_delete_what_cannot_fail.md` "The resolution (decided)" row 1; closes F-TEST-04 (its first half). The source orders one commit per row.
- ADVANCES: none: test hygiene (CLAUDE.md §0.1 pt 5: the guarded artifact is load-bearing on this repository's process only).
- INSTRUCTION: delete `tests/valoria/test_knot_pool_formula.py` (three tests asserting the text `(Spirit*2)+History(Relevant)+3` occurs in three files under `.designs/`; the code reads `pool = spirit * 2`, `systems/fieldwork/sim/knots.py`).
- WHERE: DELETE `tests/valoria/test_knot_pool_formula.py`.
- TESTS: none.
- FALSIFIER and CONTROL: a file under `engine/` or `modules/` imports or reads the deleted file (then it was not process-only). Control: `python -m pytest tests/valoria -q -k knot` collects no test from the deleted file and nothing else changes.
- GATE: `git ls-files tests/valoria | grep -c 'knot_pool_formula'` → 0.
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `tests/valoria/test_knot_pool_formula.py`.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, high.
- LANDS IT: B02's producer; `Item: B02.02`, `[skip ci]`.

### B02.03 — delete the flow-skeleton anchor test, and the comment sentence it forced on a module · 01_CORE_tests_delete_what_cannot_fail row 2 · BUILD · HASH EQUAL
- SOURCE: the same file, row 2; closes F-TEST-04 (its second half).
- ADVANCES: none: test hygiene (§0.1 pt 5).
- INSTRUCTION: "delete `tests/valoria/test_flow_skeletons.py`; in `modules/mass_battle/terrain.py` delete the comment sentence that says `WALLS_DEFENDER_DR` is kept below the lookup so a skeleton's line anchor stays put (a constant's position in a module should not be decided by an archived document's line number). `tools/build_engine_atlas.py` is left as it is: its output is reference, and an unguarded reference that can be wrong without cost is the accepted state (§0.1 pt 5)." (The source cites the comment at `terrain.py:269-270`; find it by `WALLS_DEFENDER_DR`.)
- WHERE: DELETE `tests/valoria/test_flow_skeletons.py`; `modules/mass_battle/terrain.py` (the comment beside `WALLS_DEFENDER_DR`; comment only).
- TESTS: none.
- FALSIFIER and CONTROL: a file under `engine/` or `modules/` reads `test_flow_skeletons.py` or the skeleton files' anchors (`grep -rln engine_atlas --include=*.py` lists tools, tests and one skill only, per the source). Control: `modules/mass_battle/terrain.py` compiles to the same AST (a comment edit): `python -c "import ast,sys; ast.parse(open('modules/mass_battle/terrain.py').read())"` and `git diff -U0` shows `#` lines only.
- GATE: `git ls-files tests/valoria | grep -c 'flow_skeletons'` → 0; `python -m pytest -m mass_battle tests/valoria -q` → green.
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `tests/valoria/test_flow_skeletons.py`, `modules/mass_battle/terrain.py::WALLS_DEFENDER_DR`.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, high.
- LANDS IT: B02's producer; `Item: B02.03`, `[skip ci]`. The comment edit is in an MB-lane module: named in the batch's PR body.

### B02.04 — delete the eight substring tests, after each successor is shown to see the change · 01_CORE_tests_delete_what_cannot_fail row 3 · BUILD · HASH EQUAL
- SOURCE: the same file, row 3 and "Falsifier"; closes F-TEST-05.
- ADVANCES: none: test hygiene; R-07's `measure:` is re-pointed in B02.05.
- INSTRUCTION:
  1. First, the source's falsifier, run and recorded before anything is deleted ("the batch's first step runs this mutation and records the outcome in the commit body before row 3 deletes anything"): "in process, apply each staged delta as its own clamped write in `loop/resolve.py` and keep the trace string; `test_a_sabotage_a_restore_cancels_is_refused_after_the_fact` must redden (it would read `site.restored` and `site.damaged`)." If it does not redden: `d10b`'s deletion is wrong and that test gains "a mixed-sign case at the ceiling (a `restore` of more than the headroom and a `sabotage`, folded in both orders, one end condition)" in place of the deletion.
  2. Delete from `engine/season/tests/test_season_shape.py` the eight tests: `test_d10b_resolve_sums_then_clamps_once`, `test_choose_receives_no_world`, `test_d2_witness_does_not_lie_about_its_driver`, `test_witness_writes_no_belief_and_no_pursuit`, `test_d10c_the_obstacle_refusal_gate_exists`, `test_an_unfired_refusal_is_never_reported_as_a_pass`, `test_unmapped_rows_are_never_silently_passed`, `test_an_unclear_row_is_not_counted_as_an_unrouted_one`. Each one's successor (the source's table): `d10b` → `test_in12_step9.py::test_a_sabotage_a_restore_cancels_is_refused_after_the_fact`; `choose_receives_no_world` → `test_a_view_raises_on_any_world_collection`, `test_decision_package_never_names_world_anywhere_under_it`, `test_w5_sense_is_still_the_only_world_taking_non_decision_function`, `test_g2_deliberate_mutates_no_store_by_any_route`; `d2`, `witness_writes_no_belief…` → `test_d1c_…`, `test_r3_the_l4_limb_is_actually_exercised`, `test_w2_every_write_call_site_names_a_pair_on_the_matrix`; `d10c` → `test_w4_a_refused_attempt_names_the_attempt_not_the_campaign_seed`; the three `run_probe` / `grade` word tests → `test_playable_requires_that_every_core_row_was_actually_aimed_at`, `test_a_blocker_outranks_an_unaimed_row`, `test_no_probe_currently_returns_unreachable`.
- WHERE: `engine/season/tests/test_season_shape.py` (eight test functions); `engine/season/loop/resolve.py` touched in process only (the mutation is never committed).
- TESTS: none new (or the mixed-sign case of step 1's failing branch, in `test_in12_step9.py`).
- FALSIFIER and CONTROL: step 1's mutation leaves `test_a_sabotage_a_restore_cancels_is_refused_after_the_fact` green. Control: every named successor collects and passes on the unmutated tree.
- GATE: `python -m pytest engine/season/tests/test_season_shape.py -q` → green; `python -m pytest engine/season/tests -q -k "sabotage_a_restore_cancels or a_view_raises or decision_package_never_names_world or w4_a_refused_attempt or playable_requires"` → green; the commit body records step 1's outcome.
- HASH MOVERS: none.
- DEPENDS ON: V12 B02.01 (the same file, edited first); EXISTS-IN-TREE each successor test named above (`grep -rn "def <name>" engine/season/tests` at the batch's open).
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, high.
- LANDS IT: B02's producer; `Item: B02.04`, `[skip ci]`.

### B02.05 — R-07's `measure:` names the tests that observe it · 01_CORE_tests_delete_what_cannot_fail row 4, with U5a_tests_digest_additions §F1 · BUILD · HASH EQUAL
- SOURCE: the same file, row 4 and "Falsifier" (row 4); `proposals/U5a_tests_digest_additions.md` §F1 ("T2 row 4's `-k` expression for R-07's `measure:` gains `or r07_realm_regard_differs`"); closes F-TEST-05 (R-07's `measure:`).
- ADVANCES: R-07.a (its command; read in B02.38).
- INSTRUCTION: `engine/season/requirements.yaml`, R-07's `measure:` becomes
  `python -m pytest engine/season/tests -k 'a_view_raises or a_view_is_capped or r7_two_persons or wa_a_planted_claim or decision_package_never_names_world or another_modules_prize_and_a_foreign_actor or r07_realm_regard_differs'`
  (the source's expression with §F1's addition; "the last two [of the source's six] are the type half and the query half; `wa_a_planted_claim` is the test in which a person holding a false belief about a granary declines `transfer` while the world holds the grain"; `r07_realm_regard_differs` is `test_told_by_channel.py::test_r07_realm_regard_differs_between_hearers_by_claim_not_stance_alone`). The current `-k a_view` also selects `test_a_view_with_no_query_forms_no_effort`, about effort; the tightened expression does not.
- WHERE: `engine/season/requirements.yaml` (R-07, `measure:`).
- TESTS: none new.
- FALSIFIER and CONTROL: the source's: "delete `View.__getattr__`'s refusal in process; `a_view_raises` must redden." Control: the expression selects no test of effort (`test_a_view_with_no_query_forms_no_effort` absent from the collection).
- GATE: `python -m engine.season.harness.register --requirements` → exit 0 (every name resolves); `python -m pytest engine/season/tests -k '<the expression>' -q --collect-only` → seven tests (six of the source's and §F1's one; U5a's gate: "R-07's new expression collecting seven tests"), then the same without `--collect-only` → seven pass.
- HASH MOVERS: none.
- DEPENDS ON: V12 B02.04 (deletes `test_choose_receives_no_world`, the expression's former first name); EXISTS-IN-TREE `engine/season/tests/test_told_by_channel.py::test_r07_realm_regard_differs_between_hearers_by_claim_not_stance_alone`.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, high.
- LANDS IT: B02's producer; `Item: B02.05`, `[skip ci]`.

### B02.06 — delete the retired pool-arm pair, and the test that kept it importable · 01_CORE_tests_delete_what_cannot_fail row 5 · BUILD · HASH EQUAL
- SOURCE: the same file, row 5; closes F-TEST-09.
- ADVANCES: none: retirement (CLAUDE.md §1: retiring is deleting plus a `FORK:` row).
- INSTRUCTION: "delete `test_the_retired_pair_definitions_still_import`; delete `_ARMS_POOL`, `_pool_arm` and the `# noqa: F401 (kept for _pool_arm)` import note in `engine/season/harness/arms.py`; add a symbol-level sentence to the existing `engine/season/harness/arms.py` row in `references/restructure_ledger.md` (the `29b` precedent, same row)." `python -m engine.season.harness.arms`'s `main` reads `ARMS`, not `_ARMS_POOL`.
- WHERE: `tests/valoria/test_balance_oracle_arms.py` (`test_the_retired_pair_definitions_still_import`); `engine/season/harness/arms.py` (`_ARMS_POOL`, `_pool_arm`, the `noqa` import note); `references/restructure_ledger.md` (the `engine/season/harness/arms.py` row, one sentence).
- TESTS: none new.
- FALSIFIER and CONTROL: `python -m engine.season.harness.arms` or any import reaches `_ARMS_POOL` after the deletion (`git grep -n "_ARMS_POOL\|_pool_arm"` → nothing). Control: `python -m engine.season.harness.arms --n 1 --seasons 1` runs as before.
- GATE: `python -m engine.season.harness.arms --n 1 --seasons 1` → exits 0; `git grep -n "_ARMS_POOL\|_pool_arm" -- engine tests tools` → nothing; `python -m pytest tests/valoria/test_balance_oracle_arms.py -q` → green; the ledger row read through `pathres.load_alias_map()` (an exact row, CLAUDE.md §8).
- HASH MOVERS: none (dead harness code).
- DEPENDS ON: EXISTS-IN-TREE `engine/season/harness/arms.py::_ARMS_POOL`, `::_pool_arm`; `references/restructure_ledger.md`'s `harness/arms.py` row.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, high.
- LANDS IT: B02's producer; `Item: B02.06`, `[skip ci]`.

### B02.07 — the envelop test counts two arms over twenty seeds · 01_CORE_tests_delete_what_cannot_fail row 6 · HELD (the MB lane's file) · HASH EQUAL
- SOURCE: the same file, row 6 and "Lands it" ("Row 6 is the MB lane's file (`tests/valoria/test_mass_battle_maneuvers.py`): it lands in B02 only with that lane's agreement, else in the MB lane's first batch (B17)"); closes F-TEST-10.
- ADVANCES: none of the nine: test strength in the MB lane (CLAUDE.md §0.1 pt 2).
- INSTRUCTION: "`test_envelop_reaches_rear_node`: remove the `xfail` and replace the single-fixture pass/fail with a two-arm count over the same twenty seeds its reason text already cites: the detachment ordered to envelop reaches behind the defender in strictly more seeds than the same detachment ordered to hold, and the hold arm reaches it in none. A direction with a control, no threshold invented. If the envelop arm does not beat the hold arm, the test is red and the mechanism is the finding."
- WHERE: `tests/valoria/test_mass_battle_maneuvers.py` (`test_envelop_reaches_rear_node`).
- TESTS: the rewritten test; `assert checked >= 20` over the seeds (§0.1 pt 2).
- FALSIFIER and CONTROL: the hold arm reaches the rear node in any seed. Control: the hold arm reads 0.
- GATE: `python -m pytest tests/valoria/test_mass_battle_maneuvers.py -q -k envelop` → passes with no `xfail` marker (`grep -n "xfail" tests/valoria/test_mass_battle_maneuvers.py` → nothing at that test).
- HASH MOVERS: none.
- DEPENDS ON: the MB lane's agreement at B02's open (`STAGES.md` "Parallel sessions" rule 6: a session never edits another lane's files); EXISTS-IN-TREE `tests/valoria/test_mass_battle_maneuvers.py::test_envelop_reaches_rear_node`.
- GLOSSARY: none.
- COST and TIER: small build; `sonnet`, high.
- LANDS IT: if the MB lane agrees at B02's open, B02's producer, `Item: B02.07`, `[skip ci]`; otherwise the item leaves this batch at its expunge and is B17's (the B17 block carries it, `UNDECIDED` in this part's receipt).

### B02.08 — delete an unused helper · 01_CORE_tests_delete_what_cannot_fail row 7 · BUILD · HASH EQUAL
- SOURCE: the same file, row 7.
- ADVANCES: none: test hygiene.
- INSTRUCTION: "delete the unused `effect` in `test_r3_witness_fans_to_everyone_as_specified`" (it defines `effect` and never passes it).
- WHERE: `engine/season/tests/test_season_shape.py` (`test_r3_witness_fans_to_everyone_as_specified`).
- TESTS: none new.
- FALSIFIER and CONTROL: `effect` is read after its definition in that function (then it is not unused). Control: the test passes before and after.
- GATE: `python -m pytest engine/season/tests/test_season_shape.py -q -k r3_witness_fans` → passes.
- HASH MOVERS: none.
- DEPENDS ON: V12 B02.04 (same file).
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, medium.
- LANDS IT: B02's producer; `Item: B02.08`, `[skip ci]`.

### B02.09 — assertions that cannot fail get a floor or go · U5a_tests_digest_additions §A · BUILD · HASH EQUAL
- SOURCE: `proposals/U5a_tests_digest_additions.md` §A and "Not edited, with the reason"; `unified/U4_DOCUMENT_STATUS.md` §3.4 code SITE; `master/instructions/IS_B2_SC_FI_CORE_CHAR_part2.md` `IS-B2-CORE-07` (this item's first step); closes the digests' instances of F-TEST-01 to F-TEST-12 at these sites.
- ADVANCES: none: test strength (CLAUDE.md §0.1 pt 2).
- INSTRUCTION:
  1. SITE (`IS-B2-CORE-07`, copied): "open each cited site and confirm the symbol and line before the edit; a site that does not match is dropped from the member with a line in the commit body, not repaired by guess." Record in the commit body, per row, what was found (the line numbers are the digests' at `785bc62`; find each by its symbol or text). Only A3 was opened by the source lane.
  2. The edits, per row, copied:

  | # | site | defect | exact edit |
  |---|---|---|---|
  | A1 | `engine/season/tests/test_information_cluster.py` (`test_20iii_every_sheet_the_populated_realm_makes_says_what_its_holder_holds`) | asserts per sheet inside the loop and `checked + skipped == len(sheets)`; with no sheets both pass | add `assert checked >= 1` after the loop (no count pin) |
  | A2 | `engine/season/tests/test_in61_succession.py` (the execution half, asserted only `if claimed:`) | the execution half is asserted only `if claimed:` | assert `claimed` before the block. If the fixture cannot make a claim, delete the execution half and keep the formation half; the commit says which |
  | A3 | `engine/season/tests/test_stress_proceedings_rehost.py` (`assert not hasattr(convene, "scale") or True`) | always true | delete the line; the raw-cell assertion below it is the test |
  | A4 | `engine/season/tests/test_season_shape.py` (`len(missing) == len(prose) - len(evaluable)`) | a tautology | delete the assertion |
  | A5 | `engine/season/tests/test_season_shape.py` (`checked >= 1` after unconditional increments) | cannot fail | replace with a floor on the population the loop walks (`assert len(<the iterable>) >= 1` before the loop) |
  | A6 | `tests/valoria/test_degree_ladder_single_owner.py::test_the_held_site_still_diverges` | loops over an empty dict | delete the test |
  | A7 | `tests/valoria/test_descriptor_registry_category_b.py` (two assertions on constants); `tests/valoria/test_descriptors_runtime.py` (assertions on constants) | assertions on constants | delete those assertions |

  Not edited (the source's reasons stand): `test_strife_kinds.py`'s does-not-raise call (the control of the planted-refusal tests below it); `test_season_shape.py`'s three harness probe loops with no floor (they guard `engine/season/harness/`, accepted, §0.1 pt 5); the mass-battle and combat files the source hands to their own closure.
- WHERE: `engine/season/tests/test_information_cluster.py`, `test_in61_succession.py`, `test_stress_proceedings_rehost.py`, `test_season_shape.py`; `tests/valoria/test_degree_ladder_single_owner.py`, `test_descriptor_registry_category_b.py`, `test_descriptors_runtime.py`.
- TESTS: the edited tests themselves.
- FALSIFIER and CONTROL: A1: return no sheets in process; the test must fail (it passed before). A2: make the fixture claim nothing; the test must fail. Control: each edited file passes on the unmutated tree.
- GATE: `python -m pytest <each edited file> -q` → green, one file at a time (the source's gate); the commit body lists per row: found or dropped, and the edit.
- HASH MOVERS: none.
- DEPENDS ON: V12 B02.08 (`test_season_shape.py`, serial); EXISTS-IN-TREE each site, checked by step 1.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, high.
- LANDS IT: B02's producer; `Item: B02.09`, `[skip ci]`.

### B02.10 — source-text assertions beyond the eight: run each mutation, then delete or keep · U5a_tests_digest_additions §B · BUILD · HASH EQUAL
- SOURCE: the same file, §B; code SITE; `IS-B2-CORE-07`.
- ADVANCES: none: test strength.
- INSTRUCTION:
  1. SITE: open each site and record what is found (as B02.09 step 1). Sites (the digests' line numbers at `785bc62`): `test_season_shape.py:258`, `:311`, `:369`, `:409-410`, `:426`, `:580`, `:1551`, `:3609-3615`, `:4159`, `:4176`, `:5613`, `:7574-7578`; `test_sc02_typed_ids_and_loader.py:63`, `:322`; `test_governance_build.py:776-783`; `test_cp_t03_04_arms.py:93-94`. (`tests/valoria/test_combat_halfsword_affordance.py:62-67` is combat's: not edited here, the source hands it to U5b.)
  2. The rule, per line, copied: "In process, make the change the substring guards against. If a behaviour test in the same file goes red, delete the substring assertion: its fact is observed. If none does, keep the line and name it in the commit body; it is then the only observer and a behaviour test is owed by whoever next edits that code. No line is deleted on the digest's word alone."
  3. Kept as they are: `test_army_menu_presets.py:325-341`, the `ast` walks in `test_in23`, `test_k3`, `test_migrate_capacity`, `test_governance_build.py:1559-1604`; `tests/valoria/test_claim_provenance_fields.py:43-53` (reads a tool's text: process, accepted).
- WHERE: `engine/season/tests/test_season_shape.py`, `test_sc02_typed_ids_and_loader.py`, `test_governance_build.py`, `test_cp_t03_04_arms.py` (only the lines step 2 deletes).
- TESTS: none new.
- FALSIFIER and CONTROL: a line deleted whose mutation turned no behaviour test red (the commit body's per-line record shows it). Control: each file green on the unmutated tree.
- GATE: `python -m pytest <each edited file> -q` → green, one file at a time; "for section B the commit body lists, per line, the mutation made and the test that went red" (the source's gate).
- HASH MOVERS: none.
- DEPENDS ON: V12 B02.09 (`test_season_shape.py`, serial).
- GLOSSARY: none.
- COST and TIER: edit, one mutation per line; `sonnet`, high.
- LANDS IT: B02's producer; `Item: B02.10`, `[skip ci]`.

### B02.11 — hash literals read under a revert stack, beyond B02.01's table · U5a_tests_digest_additions §D2 · BUILD · HASH EQUAL
- SOURCE: the same file, §D row D2 ("§D2 after T1 in B02"); code SITE; `IS-B2-CORE-07`.
- ADVANCES: none: test strength.
- INSTRUCTION:
  1. SITE: open each site and record what is found.
  2. Copied: "hash literals asserted under a revert stack in `test_cp_t03_01` (7 reverts), `test_cr17` (8), `test_cr87` (7), `test_cr85` (4), `test_cp_t03_04` (3), `test_in27_endings.py:357-385`, `test_season_weather.py` (first test; the `give`-withheld test) … fall to T1 C by its rule (a hash pin read under `revert_*` is deleted; the one owner holds the shipped trajectory). The behaviour assertions in those files stay." The files B02.01's table already covers are checked, not re-edited; this item deletes what remains: the pins of `test_cr17_odds_weighting.py` and `test_in27_endings.py`, and any other in the list B02.01 left.
- WHERE: `engine/season/tests/test_cr17_odds_weighting.py`, `test_in27_endings.py`; and the other listed files where step 1 finds a pin B02.01 left.
- TESTS: none new.
- FALSIFIER and CONTROL: a deleted literal was the only assertion of a behaviour (then its test loses all its asserts; it must keep at least one). Control: each file green.
- GATE: `python -m pytest engine/season/tests/test_cr17_odds_weighting.py engine/season/tests/test_in27_endings.py -q` → green; `git grep -lE '"[0-9a-f]{32}"' -- engine/season/tests` → as B02.01's gate.
- HASH MOVERS: none.
- DEPENDS ON: V12 B02.01 (the owner and the rule).
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, high.
- LANDS IT: B02's producer; `Item: B02.11`, `[skip ci]`.

### B02.12 — count pins and re-pin logs beyond B02.01's list · U5a_tests_digest_additions §E · BUILD · HASH EQUAL
- SOURCE: the same file, §E; code SITE; `IS-B2-CORE-07`; C3-N30.
- ADVANCES: none: test strength.
- INSTRUCTION:
  1. SITE: open each site and record what is found. Sites (the digests' line numbers): `test_season_shape.py:2407`, `:4122`, `:4873`, `:6384`, `:6971`, `:7040`, `:7746`, `:10083`, `:12366`, `:12713`, `:13580`, `:13723`, `:13771`, `:14829`, `:14889`, `:14933`, `:15143`, `:16649`, `:17845`, `:17878`; the `ever` literal at `:8164`, `:9425`, `:11122`; `test_governance_build.py:913`, `:1975-1991`, `:2421`, `:2957`; `test_in53_vacancy_need.py:246`, `:298`; `test_in36_foreign.py:99`, `:273-286`; `test_told_by_channel.py:234-300` (a seed re-picked eight times). Those B02.01 already edited are checked, not re-edited.
  2. The rule, per pin, copied: "A pin whose comment states the property it stands for is replaced by that property (a floor, a set inclusion, an equality between two readings of the same run). A pin that states none, and whose re-pin log shows it moved with unrelated commits, is deleted with its log. A pin on a closed roster's size that a loader already refuses (`len(REFERENT_CLASSES) == 8`, `len(VERB_TABLE)`) is deleted: the loader is the owner. The one exception is the pin T1 D keeps (R-05's denominator): it is a reading of `main` (67), re-read and re-recorded at B25 (A-28's `tie`/`knot` split, 68) and B38 (`riot`, 69, if it lands), quoted with its batch (C3-N30); every other copy of `len(VERB_TABLE) == 67` is deleted."
- WHERE: `engine/season/tests/test_season_shape.py`, `test_governance_build.py`, `test_in53_vacancy_need.py`, `test_in36_foreign.py`, `test_told_by_channel.py`.
- TESTS: none new.
- FALSIFIER and CONTROL: a replaced pin's property assertion passes on a mutated run that the pin caught (then the property is weaker than the pin claimed: keep the pin and say so). Control: each file green.
- GATE: `python -m pytest <each edited file> -q` → green, one file at a time; `git grep -n "len(VERB_TABLE) == 67" -- engine/season/tests` → one line.
- HASH MOVERS: none.
- DEPENDS ON: V12 B02.10 (`test_season_shape.py`, serial); V12 B02.01 (its D list).
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, high.
- LANDS IT: B02's producer; `Item: B02.12`, `[skip ci]`.

### B02.13 — a row's `met` text is a list of conjuncts the register reads · IS-A-01, landing as 01_CORE_requirements_reading_record §1, with 16_PESSIMIST_CORE_the_nine_gate… edit 1 and IS-A-04's register lines · BUILD · HASH EQUAL
- SOURCE: `master/instructions/IS_A_NINE_part2.md` `IS-A-01` (one commit, "landing *as* §1 of `proposals/01_CORE_requirements_reading_record.md` rather than after it, so the nine rows are reshaped once"); `proposals/01_CORE_requirements_reading_record.md` §1, "Gate", "Falsifier"; `proposals/16_PESSIMIST_CORE_the_nine_gate_and_a_knockout_reading.md` "Exact edits" 1 and "Gate" (its named test file), whose regexes `IS-A-01` says "are not written at all"; `IS-A-04`'s WHERE ("three lines, in `IS-A-01`'s commit"); C-U5a-01, C3-K5; closes F-CORE-03 (the shape), F-PES-CORE-04.
- ADVANCES: all nine (the definition of done gets an owner; no row moves).
- INSTRUCTION (`IS-A-01`'s three steps, copied; the reading record's shape and the nine-gate's rules folded where `IS-A-01` names them):
  1. `engine/season/requirements.yaml`, each of the nine rows: `measured:` leaves (the file's history is its git log); the row gains `conjuncts:`, a list of `{id, text, argv, expects, holds, reading}` where `id` is `R-0n.x`, `argv` is a list (the command, no shell string), `expects` is the printed line or the test names, `holds` is one of `yes | no | unread`, and `reading` is the record (`tree`, `date`, `seed`, `seasons`, `line`, `control`, `does_not_show`), required where `holds` is `yes` or `no`. A retired conjunct is deleted; the commit body names it. `measure:` stays one line per row for `tools/m1_acceptance.py` and the dossier script, and names the row's cheapest conjunct (R-01's and R-02's are B02.15's). The record's shape, as the reading-record proposal gives it for one row:
     ```yaml
     - id: R-05
       statement: ...
       status: not_met
       measure: python -m engine.season.harness.corpus_run --seasons 2
       reading:
         tree: 601e715
         date: 2026-11-12
         seed: 0
         seasons: per case
         line: "VERBS THAT EXECUTED : 23 of 67"
         control: none            # or the arm and what it read
         does_not_show: "one seed; a verb executing is not a verb built out"
       blocks: [...]
     ```
     (here the `reading:` record sits on each conjunct, not on the row). The `scales:` block is untouched by this step (B02.31). This commit writes the key with an empty list on each row; B02.38 writes the conjuncts.
  2. `engine/season/harness/register.py::check_requirements` (the owner of the shape): refuse `status: met` unless every conjunct reads `holds: yes` with a `reading.tree`, `reading.seed` and `reading.line`; refuse `partial` with no conjunct at `yes`; refuse a conjunct with no `argv`; resolve `argv[0:3]` by the three rules of the nine-gate edit 1: "a `python -m <module>` head: resolve `<module>` with `importlib.util.find_spec`; absent is a violation, with the same wording as the missing-file case"; a path by existence; "the `-k` case: collect the test names once (`re.findall(r"def (test_\w+)", src)`); **every** identifier in the expression not under a `not` must be a substring of at least one test name" (`names = re.findall(r"[A-Za-z_]\w*", expr)`, drop `and`/`or`/`not` and every identifier directly under a `not`; each remaining name must be a substring of some name in `re.findall(r"def (test_\w+)", src)` over the test files named before `-k`); "a head matching none of `python <path>.py`, `python -m <module>`, `pytest … -k` is a violation (*'the measure is not a command this check can find'*)". The regexes over a prose `measure:` string that the nine-gate edit 1 would have written are not written (`IS-A-01`). The three rules resolve the `argv` of a conjunct at `holds: yes` or `no`; a conjunct at `unread` must carry an `argv` but is not resolved, because `IS-A-02` writes in B02 conjuncts whose instrument a later batch builds (R-03.c's `test_scene_sequence.py` in B08, R-09.e's `engine/tests/test_draw.py` in B06, and others) `[ASSUMPTION: basis: IS-A-02 writes every conjunct in B02 and IS-A-01 refuses an unresolvable argv; the two hold together only this way; the alternative, each such conjunct written by the batch that builds its instrument, edits the met texts many times; UNDECIDED in this part's receipt]`. Print, per row, `R-0n  <status>  <held> of <m> conjuncts  tree <oldest reading.tree>`. The old `measured:` test and its print line go.
  3. `IS-A-04`'s three lines, in this commit: `check_requirements` reads `scales[].conjunct` and refuses one that names no conjunct of R-04.
  4. `tools/m1_acceptance.py::row_nine_requirements`: its detail line adds `conjuncts held <h> of <m>`; it stays DOC-DERIVED and says so.
- WHERE: `engine/season/requirements.yaml` (every row: `measured:` → `conjuncts: []`); `engine/season/harness/register.py` (`check_requirements`); `tools/m1_acceptance.py` (`row_nine_requirements`); NEW `engine/season/tests/test_register_reading.py`; NEW `engine/season/tests/test_check_requirements.py`.
- TESTS: written before the edits and read red against today's `check_requirements` (planted scratch copies through `monkeypatch.setattr(register, "REQUIREMENTS", scratch)`; `register.REQUIREMENTS` exists): in `test_register_reading.py`, `test_a_met_row_without_a_reading_is_refused` (the reading record's), `test_a_met_row_with_one_conjunct_unread_is_refused` (`IS-A-01` (a)), `test_a_met_row_whose_conjunct_has_no_reading_line_is_refused` (`IS-A-01` (b)); in `test_check_requirements.py` (the nine-gate's names, on the conjunct form): `test_all_met_with_missing_module_exits_nonzero` (`argv: ["python", "-m", "engine.season.harness.no_such_module"]`, `IS-A-01` (c)), `test_k_expression_naming_only_import_is_refused`, `test_measure_true_is_refused` (`argv: ["true"]`), `test_a_scales_row_naming_no_r04_conjunct_is_refused` (`IS-A-04`'s falsifier: `conjunct: R-04.c9`), and the control `test_shipped_file_exits_zero`, which reads red from this commit until B02.38 writes the conjuncts (expected: the five `partial` rows carry no conjunct at `yes` until then).
- FALSIFIER and CONTROL: `IS-A-01`'s: (a) a `met` row with one conjunct at `unread` exits non-zero; (b) a `met` row whose conjunct has no `reading.line` exits non-zero; (c) a missing module exits non-zero; (d) control: the shipped file exits 0 (read at B02.38). The nine-gate's stated limit stands: a bare relabel to `met` with honest readings still exits 0; the register executes nothing.
- GATE: `python -m pytest engine/season/tests/test_register_reading.py engine/season/tests/test_check_requirements.py -q` → every test passes but `test_shipped_file_exits_zero` (expected until B02.38). The arms "`register --requirements` prints nine lines in the new form and exits 0" and "`m1_acceptance --summary` row 3 prints the held count" read the conjuncts B02.38 writes: moved to B02.38's GATE (`V12_STRUCTURE_part2.md` §5.8). Between this item and B02.38, `register --requirements` exits non-zero (expected; every commit between carries `[skip ci]`).
- EXPECTED RED UNTIL B02.38 (E-9, under `[skip ci]`): `test_check_requirements.py::test_shipped_file_exits_zero` and `register --requirements` (exit non-zero): the five `partial` rows carry no conjunct at `yes` until B02.38 writes them. (Added by check lane K1 from this item's own GATE sentence; no pin is involved.)
- HASH MOVERS: none.
- DEPENDS ON: V12 B02.05 (R-07's `measure:` string, carried into the row); EXISTS-IN-TREE `engine/season/harness/register.py::check_requirements`, `::REQUIREMENTS`, `tools/m1_acceptance.py::row_nine_requirements`.
- GLOSSARY: *conjunct* (one of the readings a row's `met` text joins by "and"; the ordinary word for a term of a conjunction): its row of `unified/U1_GLOSSARY.md` becomes a pointer to `requirements.yaml`'s `conjuncts:` key and `register.py::check_requirements`, in this commit; *reading* likewise points at the `reading:` record.
- COST and TIER: edit; `sonnet`, high.
- LANDS IT: B02's producer; `Item: B02.13`, `[skip ci]`. Why this is not a new guard (`IS-A-01`, CLAUDE.md §0.1 pt 5): the register is the existing check of a file its own header calls mechanism, and its count reaches `m1_acceptance`; the edit changes the shape that check owns.

### B02.14 — the removal test, beside the draw-seed arm · 16_PESSIMIST_CORE_the_nine_gate… edit 2 · BUILD · HASH EQUAL
- SOURCE: `proposals/16_PESSIMIST_CORE_the_nine_gate_and_a_knockout_reading.md` "Exact edits" 2, "Gate" (second bullet), "Falsifier", "Cost class" (one commit for edit 2); C3-K7 (this file edits `harness/storybar.py` first); closes F-PES-CORE-05.
- ADVANCES: R-01.c, R-02.b (the instrument; the expected readings are B02.19's).
- INSTRUCTION (copied): "`engine/season/harness/storybar.py` — beside `draw_seed_arm` (same shape, same `fork`, same `drive`). Definition, written in the function's docstring and the `--help` text (CLAUDE.md §4): *a removal test: suppress one person's choice at one round and count how many of the other persons' acts differ from the unperturbed copy.* Signatures: `drive(seed, seasons, arm, cap=None, on_season=None, world=None, draw_seed=None, wrap_chooser=None)` (the existing signature plus one keyword; `wrap_chooser(chooser) -> chooser`, default `None` = today); `removal_arm(base, seasons: int, who: str, when: tuple[int, int]) -> dict[tuple, int]`. `removal_arm(base, seasons, who, when)` runs the copy with the chooser wrapped to return no scene for person `who` at `(tick, round) == when`, and returns the multiset of the *other* persons' `(actor, tick, round, verb, opportunity, executed|refused)`; a `--remove PERSON` CLI switch prints, against the unperturbed copy: acts differing, persons affected, by `(season, round)`, with three control lines in the same output — **replay** (nobody removed: must be 0), **a cohort's scene**, and **`--draw-seeds`'s existing arm** (the floor). `drive` gains one optional parameter (`wrap_chooser`), default `None`, the shipped reading unchanged. About 40 lines; no new module." (`round` here is the season's pass, the tree's identifier until B04's `PCR-4`; the docstring says "lap" in prose with `round` once in backticks.)
- WHERE: `engine/season/harness/storybar.py` (`drive`, NEW `removal_arm`, the CLI's `--remove`); `engine/season/tests/test_storybar.py` (NEW `test_removal_replay_arm_reads_zero`).
- TESTS: `test_storybar.py::test_removal_replay_arm_reads_zero` (a planted case: replay with nobody removed reads 0), written with the edit; it fails at import before it (no `removal_arm`).
- FALSIFIER and CONTROL: the source's: "The replay control prints a non-zero difference (the wrapper perturbs the run, and every figure is void)". Control: `drive(...)` with `wrap_chooser=None` reproduces the unwrapped run's hash.
- GATE: `python -m pytest engine/season/tests/test_storybar.py -q` → green; `python -m engine.season.harness.storybar --remove <a person id> --base-seed 0 --seasons 2` → the replay line prints 0 differing acts and the baseline hash; the removed line is reported (its expected reading is B02.19's).
- HASH MOVERS: none (the chooser's draw is keyed per person, `state/ids.py::draw_factory`; a wrapper with `None` changes nothing).
- DEPENDS ON: EXISTS-IN-TREE `engine/season/harness/storybar.py::drive`, `::draw_seed_arm`; `engine/season/tests/test_storybar.py`.
- GLOSSARY: *removal test* (glossary row exists, U4d: "knockout" → "removal test"): the row becomes a pointer to `storybar.py::removal_arm`, keeping its rejected word "knockout".
- COST and TIER: small build; `sonnet`, high.
- LANDS IT: B02's producer; `Item: B02.14`, `[skip ci]`.

### B02.15 — R-01 and R-02 are measured by the removal test · 16_PESSIMIST_CORE_the_nine_gate… edit 3 · BUILD · HASH EQUAL
- SOURCE: the same file, "Exact edits" 3; C-U5a-01 and C3-K5 (one instrument per property: the removal arm is R-01's and R-02's `measure:`).
- ADVANCES: R-01, R-02 (their `measure:` line).
- INSTRUCTION: "`engine/season/requirements.yaml` — R-01 and R-02 `measure:` re-pointed to `python -m engine.season.harness.storybar --remove <most-cited person> --base-seed 0 --seasons 2`, keeping the corpus `R3` line as a second measure in the comment. The statuses are **not** changed by this proposal." `<most-cited person>` is the bare `--remove` of B02.19 (no name: the instrument picks him); until B02.19 lands, the string names the flag as B02.19 defines it.
- WHERE: `engine/season/requirements.yaml` (R-01, R-02: `measure:`).
- TESTS: none new.
- FALSIFIER and CONTROL: R-02's `measure:` still names `proposals/2026-09-04-degree-sweep/wd_collect.py` (the instrument under `proposals/` the source retires as a measure). Control: `status:` of both rows unchanged (`git diff` shows the `measure:` lines only).
- GATE: `git diff -U0 engine/season/requirements.yaml` → two `measure:` lines; `python -m engine.season.harness.storybar --help` lists `--remove`. The register's exit-0 arm is read at B02.38 (moved, §5.8).
- HASH MOVERS: none.
- DEPENDS ON: V12 B02.13 (the row shape), B02.14 (the flag).
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, high.
- LANDS IT: B02's producer; `Item: B02.15`, `[skip ci]`.

### B02.16 — the chronicle reads what persons moved, against a world where nobody acts · 16_PESSIMIST_GAME_consequence_reading · BUILD · HASH EQUAL
- SOURCE: `proposals/16_PESSIMIST_GAME_consequence_reading.md` (head "Reconciled: … U5d closure": the column of tenure changes by cause), "The resolution (decided)", "Edits", "Gate"; C3-K5 (its `requirements.yaml` edit is withdrawn); rulings A-15, A-19, A-57, A-58, A-66 (the producers of the terminals); closes F-PES-GAME-01, F-PES-GAME-02.
- ADVANCES: none of the nine as a conjunct (C3-K5: no `measure:` reads it); a reading beside the removal test.
- INSTRUCTION (copied):
  1. "`engine/season/harness/chronicle.py`: a `--propagation` flag (new; `main`'s parser), running the played arm and the null arm (the same built world, a chooser that returns no act, MATTER and CALENDAR running) for `--seed` and `--seasons`, and printing the three columns. Three pure functions over `World` (they read the stores the content hash reads and own no rule): `moved_by_persons(w_played, w_null) -> dict[str, int]` (column 1, by component), `answered_outside_writing(w, verb_table) -> int` (column 2; reads `verb_table.yaml`'s `writes` column and `corpus_run`'s `EMITS AND WRITES NOTHING` census, the engine map in the scratch file is NOT carried), `terminals_answered(w) -> dict[str, tuple[int, int]]` (column 3: emitted, and among another person's executed act's causes). Source of the projection: the scratch `runs/PES_GAME/pes.py::proj`, rewritten here, not copied (the scratch is not in the repository). The docstring and `--help` define the reading in one sentence (CLAUDE.md §4)."
  2. The columns: (1) **Moved by persons**: "the state projection of the played arm against the null arm, by component: persons, seat `hold`s, site conditions, rungs, stores, stance rows, pursuits, convictions. Printed as counts of differing entries", with the column the U5d head adds: tenure changes by cause (death, term, revocation, claim, conquest); (2) **Answered outside writing**: "executed cross-person answers whose answering verb is not a deposit-only or emission-only row" (`corpus_run`'s `EMITS AND WRITES NOTHING` census plus the rows whose only `writes` is a `Record`, a `Proposition` or a `Claim`); (3) **Terminals answered**: "for `person.died`, `tenure.closed`, `field.won`/`field.lost`, `matter.determined`, `news.told`, `body.changed`: emitted, and of those, how many stand among the causes of another person's executed act."
  3. "Nothing else. No `requirements.yaml` edit (withdrawn, C3-K5)." No status is read on these; no threshold beyond "above the null arm".
- WHERE: `engine/season/harness/chronicle.py` (`main`'s parser; NEW `moved_by_persons`, `answered_outside_writing`, `terminals_answered`); NEW `engine/season/tests/test_chronicle_propagation.py`.
- TESTS: in the new file, written with the edit: `test_null_arm_against_itself_reads_zero_in_every_column` (control a), `test_planted_body_hazard_moves_persons_and_seat_holds` (control b: the bodies hazard set to 1 for one seat-holder, replacing the scratch `x2_death.py`); red before the edit (no functions).
- FALSIFIER and CONTROL: the source's two controls: (a) the null arm against itself reads zero in every column; (b) a planted consequence is seen (the hazard moves `persons` and `seat holds` in column 1 and puts a `person.died` in column 3's denominator). "If either control fails the reading is void."
- GATE: `python -m pytest engine/season/tests/test_chronicle_propagation.py -q` → 2 passed; `PYTHONHASHSEED=0 python -m engine.season.harness.chronicle --seed N --seasons 2 --propagation` for N in 0, 1, 2 → prints the columns (three seasons in the source; A-114).
- HASH MOVERS: none (a harness reading).
- DEPENDS ON: V12 B02.15 (after the nine-gate file, the source's order); EXISTS-IN-TREE `engine/season/harness/chronicle.py::main` (its arguments `--seed`, `--seasons`, `--arm`, `--cap`, `--all-acts`, `--chains`, `--min-depth`), `corpus_run`'s census, `verb_table.yaml`'s `writes` column.
- GLOSSARY: *propagation reading* (new, if no row has it): "how far the played world's state differs from the same world where nobody acts", in one sentence, added in this commit.
- COST and TIER: edit; `sonnet`, high.
- LANDS IT: B02's producer; `Item: B02.16`, `[skip ci]`.

### B02.17 — the act-count instrument prints which engines a run entered · CI-11 · BUILD · HASH EQUAL
- SOURCE: `master/CODEBASE_IMPROVEMENT_PROPOSAL_part2.md` `CI-11` ("Exact edits, in order" 1–4, "Tests", "Gate", "Falsifier and control", "How later batches use it"); closes H-01 (the instrument half).
- ADVANCES: none of the nine as a conjunct; the `ENGINES` reading `IS-PC-03`, `IS-MB-05` and IS-A §12.2 read at closes (`combat.fight` at this batch's close).
- INSTRUCTION (copied; line numbers dropped, `aperture.py` is edited here, before B03a):
  1. "`engine/season/harness/aperture.py`: a function `engines_entered(run: Callable[[], Any]) -> tuple[Any, dict | None]` that, on Python 3.12 or later, takes a monitoring tool id (`sys.monitoring.use_tool_id`), and for each role of `engine.substrate.composition.ROLES` whose resolved target has a `__code__` enables `PY_START` on that code object alone (`sys.monitoring.set_local_events`), counting entries per role; runs `run()`; frees the tool id in a `finally`; returns `run`'s value and `{role: count}`. Where the interpreter is older or the tool id is taken, it returns `None` for the counts and the block says why. A `kind: value` row has no code object and is listed as `value`."
  2. "`measure_world` wraps its seasons in it and stores the counts as `m["engines"]`."
  3. "`report` gains a block after the per-verb lines:
     ```
     ENGINES (composition rows entered in this run)
       fieldwork.find              62
       settlements.housing         79
       social_contest.roll         48
       ...
       rows entered 6 of 16
     ```
     every row printed, zeros included, sorted by role."
  4. "`pooled_report` prints, per role, the number of seeds whose run entered it."
- WHERE: `engine/season/harness/aperture.py` (NEW `engines_entered`; `measure_world`, `report`, `pooled_report`); `engine/season/tests/test_aperture.py` (NEW `test_the_engines_reading_counts_an_entry_it_can_see`).
- TESTS: "`test_the_engines_reading_counts_an_entry_it_can_see`: inside `engines_entered`, call one module entry through its row once (`composition.require("settlements.fortification")` on a built `FortInput`, or the row the file's existing tests can already build an input for); assert that role reads `1` and that another role reads `0`, and assert the counts are not `None` on the interpreter CI uses (a named skip below 3.12)." Red before the edit (no `engines_entered`).
- FALSIFIER and CONTROL: "In a scratch worktree: remove the `set_local_events` call → the new test must fail (the role reads 0, not 1). Restore." Control: the file's existing `CONTROL` line (the measured arm ends in the same `content_hash()` as `populated.run`).
- GATE: `python -m pytest engine/season/tests/test_aperture.py -q` → green; `PYTHONHASHSEED=0 python -m engine.season.harness.aperture 1 0` → its `CONTROL` line reads as before and the block prints (expected at `4dc8a7b`, before B01: `social_contest.roll` 48, `fieldwork.find` 62, ten rows at 0 with `combat.fight` and `mass_battle.resolve_field` among them, `rows entered 6 of 16`; on this tree it is a reading, quoted, never a threshold).
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `engine/season/harness/aperture.py::measure_world`, `::report`, `::pooled_report`; `engine/substrate/composition.py::ROLES`, `::require`.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, medium.
- LANDS IT: B02's producer; `Item: B02.17`, `[skip ci]`.

### B02.18 — the act-count instrument prints which verbs are built out, and through which seat · IS-A-06 · BUILD · HASH EQUAL
- SOURCE: `master/instructions/IS_A_NINE_part2.md` `IS-A-06`; closes nothing by itself (the instrument R-05.b, R-04.a and R-07.c read).
- ADVANCES: R-05.b, R-04.a, R-07.c (the instrument).
- INSTRUCTION (copied; "after CI-11 in the same batch, one edit of `report` and `pooled_report` for both"):
  1. "`built_out(m) -> dict`: per verb of `VERB_TABLE`, over the acts of `corpus_run.attempts(w, n)` that are `made` and not `refused` (a clean execution, the instrument's `ex - both`): `clean` (the count); `kinds` (true where the Events caused by one such act include every kind of the row's `emits_at(degree)` for the band it folded, `data/verbs.py`); `wrote` (true where the row's `writes_at(degree)` is empty for every band the verb can fold, or at least one such Event carries a `Receipt` whose `delta` is not empty: before ≠ after); `via` (the count of clean executions whose `Act.via` is set). A verb is **built out** when `clean >= 1`, `kinds` and `wrote`."
  2. "`report` gains, after the per-verb lines, `BUILT OUT` with one line per verb (zeros included, sorted) and the total `built out <k> of <len(VERB_TABLE)>`; then one line `FOUGHT FIELDS  won+lost <a>  unopposed <b>  stance receipts on the losing side <c>`, `c` counted over the `Person.stance` receipts of Events caused by a `march` act whose field Event is `field.won` or `field.lost`."
  3. "`pooled_report` prints, per verb, the number of seeds in which it is built out, and the pooled total."
- WHERE: `engine/season/harness/aperture.py` (NEW `built_out`; `report`, `pooled_report`); `engine/season/tests/test_aperture.py` (NEW `test_built_out_counts_a_clean_execution_with_its_kinds_and_its_receipt`).
- TESTS: "`test_built_out_counts_a_clean_execution_with_its_kinds_and_its_receipt` (one planted act through the fold on the file's existing world: reads 1; the same act refused reads 0; a hand-built `Act` appended to the log without the fold reads 0, which is the 'a hand-built execution never counts' clause)". Red before the edit.
- FALSIFIER and CONTROL: "the instrument's existing `CONTROL` line shows the block moves no world; plant: drop the `Receipt` test from `wrote` and the new test's refused arm must still read 0 while a write-less band now reads built out (it must not)."
- GATE: `python -m pytest engine/season/tests/test_aperture.py -q` → green; `PYTHONHASHSEED=0 python -m engine.season.harness.aperture 1 --seeds 0 1 2` → `CONTROL` EQUAL at each seed; the block prints one line per verb of `VERB_TABLE` (67 at `6e1ea91`; the count read by command); the `FOUGHT FIELDS` line is quoted (at `6e1ea91` it read `won+lost 0` at seed 0 and `1` at seed 2; B01 moved the tree). "The built-out total is a reading, never a threshold, until the re-take that closes R-05."
- HASH MOVERS: none.
- DEPENDS ON: V12 B02.17 (the shared edit of `report`); EXISTS-IN-TREE `harness/corpus_run.py::attempts`, `data/verbs.py::emits_at`, `::writes_at`, `state/carriers.py` (`Receipt.delta`, from the class docstring: `[UNVERIFIED]` in the source, the producer opens the fold first).
- GLOSSARY: *built out* (a verb with at least one clean execution that emits its kinds and, where it declares writes, writes): its row becomes a pointer to `aperture.py::built_out`.
- COST and TIER: small build; `sonnet`, high.
- LANDS IT: B02's producer; `Item: B02.18`, `[skip ci]`.

### B02.19 — the removal test states what it expects, and whom it removes · IS-A-03 · BUILD · HASH EQUAL
- SOURCE: `master/instructions/IS_A_NINE_part2.md` `IS-A-03` ("added to that proposal's edit 2"; placed here by `V12_STRUCTURE.md` §2.2's order, after B02.14 on `harness/storybar.py`, C3-K7).
- ADVANCES: R-01.c, R-02.b.
- INSTRUCTION (copied): "`engine/season/harness/storybar.py`: (1) `--remove` with no name takes the person who is the actor of the most `Event.causes` antecedents of other persons' acts in the unperturbed copy's first season (ties by person id), and prints the name; (2) the report ends with two verdict lines: `R-01.c  others' acts differing: <n>  (replay <0>)` and `R-02.b  differing at a later (season, round): <m>`; (3) `--base-seed` accepts several seeds and prints one pair of lines per seed."
- WHERE: `engine/season/harness/storybar.py` (the `--remove` CLI, `removal_arm`'s report); `engine/season/tests/test_storybar.py` (NEW `test_removal_changes_another_persons_later_act`).
- TESTS: "`test_removal_changes_another_persons_later_act` (seed 0, two seasons: `n >= 1` and `m >= 1`; in the same test the replay arm reads 0 and the removed person's own acts are excluded from `n`)". Red before the edit (no verdict lines).
- FALSIFIER and CONTROL: "the replay arm non-zero voids every figure (the proposal's own); second control: remove a person at a round in which the unperturbed copy shows him forming no scene: `n` must be 0."
- GATE: `PYTHONHASHSEED=0 python -m engine.season.harness.storybar --remove --base-seed 0 1 2 --seasons 2` → replay 0 at each seed; `n >= 1` and `m >= 1` at each seed `[ASSUMPTION: above 0 with a control of exactly 0 is the right form — basis: it is the form 01_CORE_tests_shipped_world_falsifiers gives rows 1 and 2; the audit's seed-0 arms read 236 to 634 against 0 on the controls, a scratch comparison]`; `python -m pytest engine/season/tests/test_storybar.py -q` → green.
- HASH MOVERS: none ("the chooser's draw is keyed on `(world_seed, tick, person, purpose)`, `state/ids.py::draw_factory`, so a suppressed choice shifts no other person's stream").
- DEPENDS ON: V12 B02.14 (`removal_arm`, `--remove`); V12 B02.18 (placed after it by §2.2's order; no data edge).
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, high; about two minutes an arm, six arms.
- LANDS IT: B02's producer; `Item: B02.19`, `[skip ci]`.

### B02.20 — the count of scenes that wrote nothing is read from here on · IS-A-07 · BUILD · HASH EQUAL
- SOURCE: `master/instructions/IS_A_NINE_part2.md` `IS-A-07` (adopts `U4_TRACEABILITY.md` G-11); `proposals/30_WR_E_cascade_chains_and_the_census.md` "Instructions to code" 1 (the function); `proposals/30_WR_D_momentum_and_its_brakes.md` §3 (the definition, copied forward in this commit); ruling A-81, A-62; closes G-11. `IS-B2-CORE-03` is a pointer to this item (`IS-A-07`'s head: "the one owner of `null_scenes` in B02").
- ADVANCES: R-05.c (the instrument; its asserted zero and clause C9 stay in B38).
- INSTRUCTION:
  1. Land `null_scenes` where `30_WR_E` puts it, report-only, as that proposal's instruction 1 gives it: "**`null_scenes(w, n) -> dict`**: `{"total": int, "null": Counter((verb, cls))}` over `corpus_run.attempts(w, n)` (the one owner of made and refused), `cls` in `made`, `graded_loss`, `refused`. An act is null when no Receipt on any Event naming it in `causes[]` writes a `write_matrix.yaml` cell with a `RES` or `WIT` step, counting a `claim.deposited` only where the claim's holder is the actor or the act's counterparty (`state/carriers.py::subject_of(act)` when it is a person, or a seat's live holder). A-62: the budget is a Query and writes no cell, so nothing is excluded for it; if a later build makes the debit a write, that cell is excluded by name here. CLI `--null-scenes`, printed per season and pooled: `null_scenes total=<n> null=<n> | <verb/cls=n, …>`." In `engine/season/harness/storybar.py`.
  2. The definition of a durable write, copied forward from `30_WR_D` §3 into `null_scenes`'s docstring (`30_WR_D` then points at it): "A *durable write* is a Receipt on a `write_matrix.yaml` cell whose `steps` include `RES` or `WIT`, other than the scene budget's own cell; a claim deposited in the actor's or a counterparty's ledger counts; a sighting in a bystander's ledger alone does not (the act must matter to someone in it). `[ASSUMPTION; medium; Jordan to correct; revert: any claim counts]`."
  3. `harness/aperture.py::report` prints after `BUILT OUT` one block `NULL SCENES (acts whose Events carry no durable write)` by verb and by outcome class (made, refused, graded loss), with the total. The budget debit does not count (A-81). The asserted zero and clause C9 stay in B38.
- WHERE: `engine/season/harness/storybar.py` (NEW `null_scenes`, `--null-scenes`); `engine/season/harness/aperture.py` (`report`); `engine/season/tests/test_storybar.py` (NEW `test_null_scenes_sees_a_planted_act_that_writes_nothing`).
- TESTS: "`test_null_scenes_sees_a_planted_act_that_writes_nothing` (clause C9's planted control, moved forward)", with `assert checked >= 1`; red before the edit.
- FALSIFIER and CONTROL: "the planted act not counted" (`IS-A-07`); `30_WR_E`'s: "`null_scenes` reading 0 on the shipped engine: the definition counts bystanders' sightings". Control: `aperture`'s `CONTROL` line EQUAL (a report-only block).
- GATE: `python -m pytest engine/season/tests/test_storybar.py -q` → green; `PYTHONHASHSEED=0 python -m engine.season.harness.aperture 1 0` → prints the block; "the count at `6e1ea91` is unread here and is recorded at B02's close as the baseline every later close quotes" (`30_WR_E` P-2's looser probe read 59 of 821 acts at seed 0, one season: a comparison, not a target).
- HASH MOVERS: none.
- DEPENDS ON: V12 B02.18 (`BUILT OUT`, `IS-A-06`); V12 B02.19 (`harness/storybar.py`: the order is the nine-gate proposal, `IS-A-03`, this item, C3-K7); EXISTS-IN-TREE `engine/season/write_matrix.yaml`, `harness/corpus_run.py::attempts`, `state/carriers.py::subject_of`.
- GLOSSARY: *durable write* and *null scene* (the plain words: "a change that outlasts the scene"; "a scene that changed nothing that lasts"): rows added or pointed at `storybar.py::null_scenes` in this commit.
- COST and TIER: edit; `sonnet`, medium.
- LANDS IT: B02's producer; `Item: B02.20`, `[skip ci]`.

### B02.21 — R-01 on the played realm, three seeds, with the witness cut as its control · 01_CORE_tests_shipped_world_falsifiers row 1 · BUILD · HASH EQUAL
- SOURCE: `proposals/01_CORE_tests_shipped_world_falsifiers.md` "The resolution (decided)" row 1 and the typed shape of the new file; U3 §6.1 (`test_realm_requirements.py` MISSING, written in this batch before its reading); C3-N14, C3-N27; closes F-TEST-01 (R-01). The source orders one commit per row.
- ADVANCES: R-01.b.
- INSTRUCTION: create `engine/season/tests/test_realm_requirements.py` with the source's typed shape (composing on existing owners only: `populated.build_realm`, `probes.chooser`, `world_q.occasioned_by`, `SeasonDriver`):
  ```python
  SEEDS = (0, 1, 2)

  def _play(seed: int, fx: Fixtures | None = None) -> tuple[World, SeasonDriver]: ...
  def _occasioned_by_another(w: World, d: SeasonDriver) -> int: ...
  def _sequence(d: SeasonDriver) -> list[tuple[str, str, str | None]]: ...

  @pytest.mark.parametrize("seed", SEEDS)
  def test_r01_an_act_is_occasioned_by_a_claim_that_walks_back_to_another_persons_act(seed): ...
  def test_r01_control_with_witness_cut_no_act_is_so_occasioned(monkeypatch): ...
  ```
  Row 1, copied: "New test, parametrised over seeds 0, 1, 2: build the realm, play one season with `P.chooser(w, verbs=resolvable_verbs())`, count resolved acts whose scene's `occasion.source == "claim_landed"` and whose `occasioned_by(w, q)` Events have a cause that is an `Act` by a different person; assert the count is `> 0`. Control in the same test at seed 0: `monkeypatch.setattr(SeasonDriver, "witness", lambda self, token, events: 0)`, same count, assert `== 0`." (`_sequence` and the R-02 tests are B02.22's.)
- WHERE: NEW `engine/season/tests/test_realm_requirements.py`.
- TESTS: the two above: green at the base where the claim is a property that holds today, and the control red with the cause removed (it reads `== 0` only with the witness cut). Readings at `main` before B01 (a comparison, not a target): 134 of 749, 141 of 731, 162 of 751; control 0 of 388.
- FALSIFIER and CONTROL: the witness-cut arm must read 0 (in the file).
- GATE: `python -m pytest engine/season/tests/test_realm_requirements.py -q -k r01` → three seeds green and the control green.
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `harness/populated.py::build_realm`, `harness/probes.py::chooser`, `queries/world_q.py::occasioned_by`, `loop/driver.py::SeasonDriver` (`witness`).
- GLOSSARY: none.
- COST and TIER: small build; `sonnet`, high; about 25 s of test time `[estimate: 7.3 s a realm season, the source's probe]`.
- LANDS IT: B02's producer; `Item: B02.21`, `[skip ci]`.

### B02.22 — R-02 on the played realm at the shipped budget · 01_CORE_tests_shipped_world_falsifiers row 2 · BUILD · HASH EQUAL
- SOURCE: the same file, row 2 and the typed shape; `proposals/U5a_tests_digest_additions.md` §F2 (what R-02's reading says, carried into B02.38); closes F-TEST-01 (R-02).
- ADVANCES: R-02.a.
- INSTRUCTION: in `engine/season/tests/test_realm_requirements.py`, `_sequence` and:
  ```python
  @pytest.mark.parametrize("seed", SEEDS)
  def test_r02_withholding_what_acts_observe_changes_later_acts_at_the_shipped_budget(seed): ...
  def test_r02_control_one_seed_played_twice_is_one_sequence(): ...
  ```
  Row 2, copied: "Same file, seeds 0, 1, 2: play one season at `DEFAULT_FIXTURES` and one at `.sweep("observation_deposit_mode", "none")`; assert the two `(actor, verb, subject)` sequences differ and share a non-empty common prefix (the worlds start equal and part). Control: the same seed played twice at `DEFAULT_FIXTURES` gives equal sequences."
- WHERE: `engine/season/tests/test_realm_requirements.py`.
- TESTS: the two above (readings at `main` before B01, a comparison: the sequences first differ at positions 191, 183, 182).
- FALSIFIER and CONTROL: the same-seed arm must read equal (in the file).
- GATE: `python -m pytest engine/season/tests/test_realm_requirements.py -q` → six parametrised cases and two controls green (the source's gate, about 80 s).
- HASH MOVERS: none.
- DEPENDS ON: V12 B02.21 (the file, `_play`).
- GLOSSARY: none.
- COST and TIER: small build; `sonnet`, high.
- LANDS IT: B02's producer; `Item: B02.22`, `[skip ci]`.

Last item in this file: B02.22. Batch B02-tests continues at item B02.23 (the head's index maps the handle to its file).
