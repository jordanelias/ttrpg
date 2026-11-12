# Workplan v12 — part 5: Batch B03-hygiene, second half (B03.51 to B03.99, the boundary row)

## Status: PROPOSED (a body part of workplan v12, drafted under `master/workplan_v12/`; unratified input to `methodology-execute`'s 0.1 stop until Jordan adopts v12, `V12_STRUCTURE_part3.md` §8; resolves nothing at runtime, CLAUDE.md §0.05; not canon)

## Written against: the working tree at `aa31fd2` (branch `ccr-62958c70-0kjhsw`), read 2026-11-12; author lane A05 of `master/workplan_v12/V12_STRUCTURE_part2.md` §4.2. Every item is written against the tree as B00, B01, B02 and B03's first half leave it. Line numbers are the sources' (read at their trees) and convenience only: every edit is placed by symbol (CIP part 2 §5 note 2).

**What this part holds.** The second half of `B03-hygiene` (IN): the batch block's head, its `BATCH GATE`, `C(B03-hygiene)` and its first items `B03.01` to `B03.50` are in the part that holds B03's first half (author lane A04); this part continues the same batch from `B03.51`, writes its `## Readings` block, its re-pin position `B03.99` (`V12_STRUCTURE_part4.md` E-1) and its boundary row. Section "Lines this half adds to B03's block" (below the position table) states what the batch head must carry for these items (ids, settings, serial edges, the census rows, the undecided readings); H1 and H2 merge it into the head and the tables. A part cites another part's batch or item by handle only.

**Order, and why.** `V12_STRUCTURE.md` §2.2's row for B03 and §4.2's row for A05: `U5a_CORE_owed_edits` (its sections in the source's own "Who lands it" order, hash-EQUAL ones first, §5.9), then `CI-06` (after `U5a_CORE_owed_edits`, which edits `harness/probes.py` first: CIP part 2 `CI-06` "Depends on"), then `09_WR_threadwork_module` edit 3 (U3 §1 item 4's last member), then `IS-B2-CORE-06` (its BLOCKED part is the CR-07/H-89 intake entry, merged with it), then the intake's B03 entries under `:112` (lane IN) and `:227` (lane FA) in the intake's order (§5.6 rule 3: no member names their ids; E-8: the intake heading chose the batch, §2.2 the place), then the dangling-cite fix (`master/V11_EVALUATION.md` §6), then H-137, H-130, H-139 (D-10), then the one behaviour mover (`U5a_CORE_owed_edits` §H, last because §5.9 puts hash-EQUAL items first and its source says only "after C"), then `B03.99`.

**Words.** `unified/U1_GLOSSARY.md`. A *lap* is one pass of the season's scene budget and a *round* is one engagement of a fight (A-101): every item here lands before B04's `PCR-4`, so the code identifiers keep the tree's word (`scene_budget`, `scenes_per_round`, `test_u2_the_one_round_arm_…`) and the plan's prose says *lap*; where copied source text says "round" for the season's pass it is corrected to "lap" and the item says so. A person's numbers are attributes, skills and skill scores (A-98).

**Paths.** As `V12_STRUCTURE.md` states: a bare path is under `proposals/2026-11-12-subsystem-audit-suite/`; `U3` is `unified/U3_DEPENDENCY_ORDER.md`; `CIP` is `master/CODEBASE_IMPROVEMENT_PROPOSAL.md` and `_part2`; `the intake` is `master/eval/V12_INTAKE.md`; `04` is `architecture/meta/04_CODE_ARCHITECTURE.md`. A path under `engine/`, `modules/`, `systems/`, `tools/`, `references/`, `registers/`, `research/`, `tests/` is the repository's.

---

## Batch B03-hygiene, continued (positions B03.51 to B03.99)

| pos | item | source | state | hash | gates on |
|---|---|---|---|---|---|
| B03.51 | register rows the CORE audits decided (H-87, H-30, H-47, H-48, H-59, H-56, H-82, H-24, D-51) | `U5a_CORE_owed_edits` §A | BUILD | EQUAL | Batch B02 (`_realm_goldens.py`) |
| B03.52 | comment and docstring corrections; the shortfall field initialised; the forward declaration deleted | `U5a_CORE_owed_edits` §B rows 1–3, 5, 7–9, 11 | BUILD | EQUAL | B03.51 |
| B03.53 | a contest that errors emits its row's refusal | `U5a_CORE_owed_edits` §B row 4 | BUILD | EQUAL | B03.52 |
| B03.54 | a provider handed no generator refuses | `U5a_CORE_owed_edits` §B row 6 | BUILD | EQUAL | B03.52 |
| B03.55 | an act carries no obstacle or pool of its own | `U5a_CORE_owed_edits` §B row 12 | BUILD | EQUAL | B03.52 |
| B03.56 | a season with a scene budget under one refuses at construction | `U5a_CORE_owed_edits` §B row 18 | BUILD | EQUAL | B03.52 |
| B03.57 | the log accepts only declared Event kinds | `U5a_CORE_owed_edits` §E row 2 | BUILD | EQUAL | B03.56 |
| B03.58 | the chooser receives a frozen copy of the person | `U5a_CORE_owed_edits` §E row 1 | BUILD | EQUAL | B03.57 |
| B03.59 | the hot path: live tenures from the cache; the trace records only when opened | `U5a_CORE_owed_edits` §C | BUILD | EQUAL | B03.58; Batch B02 |
| B03.60 | `arms` counts fought fields and refuses a z at zero | `U5a_CORE_owed_edits` §B row 13 | BUILD | EQUAL | B03.59 |
| B03.61 | the six chain case files are plain YAML | `U5a_CORE_owed_edits` §B row 14 | BUILD | EQUAL | B03.59 |
| B03.62 | `report.py` reads `TRACE` and the step list from their owners | `U5a_CORE_owed_edits` §B row 15 | BUILD | EQUAL | B03.59 |
| B03.63 | the case verdict `PLAYABLE` becomes `DECLARED-PRESENT` | `U5a_CORE_owed_edits` §B row 16 | BUILD | EQUAL | B03.62 |
| B03.64 | where an Event happened, at the time it happened | `U5a_CORE_owed_edits` §B row 17 | BUILD | EQUAL | B03.59 |
| B03.65 | one composed reading of where a faction stands | `U5a_CORE_owed_edits` §I | BUILD | EQUAL | B03.59 |
| B03.66 | `CLAUDE.md` §7's sentence on the seeded pins | `U5a_CORE_owed_edits` §G | BUILD | EQUAL | B03.51 |
| B03.67 | the chooser is composed in one place | `CI-06` | BUILD | EQUAL | B03.52 to B03.65 (`probes.py` edited by B03.55) |
| B03.68 | the threadwork tables become a typed file; the operation roster | `09_WR_threadwork_module` edit 3 | BUILD | EQUAL | B03.67; Batch B03 first half (`17_CENSUS_C1B_01` D3) |
| B03.69 | cut the stored `scale:` column | `IS-B2-CORE-06`; `U5a_CORE_owed_edits` §E row 3; CR-07, H-89, DEF-5, A1-46 | BLOCKED (Jordan: `off_npc_084`'s rung is content; or A1-46's revert) | EQUAL | — |
| B03.70 | the stale Layer 0 and Layer 1 passages, re-derived row by row | IN-44 (rows 2–13, 15, ALSO OWED) | BUILD | EQUAL | B03.57 (ALSO OWED), B03.66 (row 5) |
| B03.71 | the `succeed` designation nodes of `04` read the title route | A1-81 (IN-44 row 14) | BUILD | EQUAL | B03.70 |
| B03.72 | the citations of ED-IN-0225 say what it ruled | A2-40 | BUILD | EQUAL | B03.67 (`soak.py`, `storybar.py`) |
| B03.73 | the remit roster's `open:` flag agrees with its closed values | ER-C4 | BUILD | EQUAL | Batch B03 first half (`rosters.yaml`) |
| B03.74 | dead threadwork constants leave the port contract | ER-GF9 | BUILD | EQUAL | B03.68 |
| B03.75 | a subject that earns every kind cannot be silenced by a named one | H-141 | BUILD | EQUAL | B03.57 |
| B03.76 | a gate refusal in the fold emits, never raises | H-143 | BUILD | EQUAL | B03.53, B03.75 |
| B03.77 | lane handoff rows that name a v9 file | V9-02 | BUILD | EQUAL | — |
| B03.78 | `MB-05r` leaves the mass-battle synthesis | V9-20 | BUILD | EQUAL | — |
| B03.79 | the share of refusals on a non-Rung referent | REM-26 | READING | — | B03.52 |
| B03.80 | the suite's repo-fix list | H-4 | BUILD | EQUAL | B03.52 |
| B03.81 | an `establish` on an overlay key asks the founder's purview | H-291 | BUILD | EQUAL | Batch B03 first half (`06_FA_hygiene` item 2) |
| B03.82 | three mass-battle cites of a forked file | `master/V11_EVALUATION.md` §6 | BUILD | EQUAL | — |
| B03.83 | an effect body may not move an entity field before it returns | H-137 | BUILD | EQUAL | B03.76 |
| B03.84 | a write validates its subject and causes before it applies | H-130 | BUILD (DROP IF unreached) | EQUAL | B03.83 |
| B03.85 | a deleted Tenure is seen by the tenure diff | H-139 | BUILD (DROP IF unreached) | EQUAL | B03.84 |
| B03.86 | a seat buys no scene | `U5a_CORE_owed_edits` §H (C3-L8) | BUILD | MOVER(behaviour) | B03.59 |
| B03.99 | re-pin and close readings | `V12_STRUCTURE_part4.md` E-1 | BUILD | MOVER (the re-pin) | B03.51 to B03.86 |

**Not in this batch, and where each is.** `U5a_CORE_owed_edits` §B row 10 (`decision/sheet.py:2-3`): carried by `02_CHAR_reason_trail_and_small_edits.md` Part C (B09), "landed once, there" (the source's own row). §D (inputs to CR-98): B11F2, the intake's merged item "declare the loops with sign and bound" (H-25, H-106, CR-98), whose carry-forward block (`master/eval/E6.md` block 1) copies §D verbatim. §F (the transcript runner's end conditions): B34, with `11_GO_player_surface_contract_B.md` §8, which specifies the runner (`engine/season/harness/play_surface.py` has no runner at `aa31fd2`: `carry_on` and `dispatching_chooser` only); U3 §4.1 row 12 SPLIT and U3 §1.2's B34 row 6; U4 §3.4 row 289 "B03 +part B34". §B row 6's second site (`modules/combat/wrapper.py`, `rng=rng or random.Random()`): the source names it "for U5b" (the PC lane's module), not this item. The `knot` operation of `09_WR_threadwork_module` edit 3: added to the roster when the `tie`/`knot` split lands (A-28, B35), not here. H-138 (the fourth gate-observation row): B12a (D-10).

### Lines this half adds to B03's block (H1 merges them into the head the first half wrote; H2 into the tables)

- **HASH.** This half carries one behaviour mover, B03.86 (`U5a_CORE_owed_edits` §H: "One declared mover, said plainly as a re-record"; C3-L8), so B03's head line reads `HASH MOVER, one re-pin` and its `RE-PIN` line names B03.99. `UNDECIDED` (below, U-1) gives the other reading.
- **RE-PIN:** once, in B03.99's commit: the realm pins in `engine/season/tests/_realm_goldens.py` (B02's one pin file) at seeds 0, 1, 2 and the NPC-088 headless hash, read against B02's close (`reading @<sha>`); the commit says "re-pin: B03.86 removes `budget_office_bonus` (C3-L8); every other item of B03 hash EQUAL". If B03.86 is falsified (its STOPS IF), B03.99 re-pins nothing and records EQUAL.
- **EXPECTED RED UNTIL B03.99:** between B03.86 and B03.99 the realm-pin test of `_realm_goldens.py` and the NPC-088 headless pin read red under `[skip ci]` (E-1).
- **IDS:** ED-IN 0; H 0 (this half edits existing register rows only: H-24, H-30, H-47, H-48, H-56, H-59, H-70, H-82, H-87, H-92, H-130, H-137, H-139, H-141, H-143, H-291, H-330, and the D-51 row if one exists; it allocates none).
- **DIALS AT CONTROL:** none set later by a named batch. Moved unchanged by B03.68, for H2's table: `RESILIENCE_GAIN` = 0 (the control of a swept fixture, `RESILIENCE_GAIN_SWEEP = (0, 1, 3)`; its magnitude is unruled, R-14, and no source names a calibration that sets it, so it is not a B98 member).
- **SERIAL EDGES (within this half):** B03.51 → B03.52 → {B03.53, B03.54, B03.55, B03.56} (the source's order: "B rows 1–3, 5, 7–11" in one commit, then "B rows 4, 6, 12, 18, one commit each") → B03.57 → B03.58 (the source: "E row 2, then E row 1 (the log's kind check before the frozen interior …)") → B03.59 (the source: "C (after `01_CORE_tests_one_golden_owner.md` lands …)") → B03.60 to B03.65 (harness; "any order") → B03.66 (G: the orchestrator's) → B03.67 (`CI-06` edits `harness/probes.py`, which B03.55 edits first; CIP part 2 "Depends on") → B03.68 → B03.74 (ER-GF9 deletes from the typed file B03.68 makes) ; B03.57 → B03.70 (IN-44's ALSO OWED is met by B03.57's code) ; B03.66 → B03.70 (row 5 and G are one paragraph of `CLAUDE.md` §7) → B03.71 ; B03.67 → B03.72 (`soak.py`, `storybar.py`) ; B03.53 → B03.76 (the same fold, the same refusal form) ; B03.75 → B03.76 (both edit `loop/resolve.py::_fold`) → B03.83 → B03.84 → B03.85 (all three edit `state/world.py`'s write path; E6 block 5 "one batch") ; B03.59 → B03.86 (the source: "H … after C") ; everything → B03.99.
- **SERIAL EDGES (with other batches, by file; `→` is landing order; U3 §5.1 where it has the row):** `harness/probes.py`: B03 (B03.55, B03.67) → B03c (`CI-07` moves `probes.chooser` to `boot/chooser.py`) → B06 (`11_GO_one_draw_owner` changes what `draw_factory` returns: CIP part 2 `CI-06` "Enables"). `harness/storybar.py` (C3-K7, serial instrument file): B03 (B03.67, B03.72) first, before any batch U3 §1.1 names. `loop/resolve.py::_fold` (B03.53, B03.75, B03.76): B03 → B04 → B05 (U3 §5.1). `state/world.py`: B03 (B03.52, B03.59, B03.83 to B03.85) → B06 → B09 → B12 → B41 (U3 §5.1). `state/log.py` (B03.57): B03 → B09 (H-145 with NM-W9). `state/carriers.py` (B03.55, B03.58): B03 → B05 → … (U3 §5.1). `data/fixtures.py` (B03.86): B03 → B04 (`scenes_per_round` → `scenes_per_lap`) → B05. `decision/budget.py` (B03.86): B03 only. `seam/wrappers/sigma.py` (B03.54): B03 (`CI-03` in the first half, then B03.54) → B04 → B05. `engine/season/hole_register.yaml` (B03.51 and others): appended once per batch (§7.6). `queries/world_q.py` (B03.64): B03 → B05 → … (U3 §5.1). `queries/faction_q.py` (B03.65): B03 → B21 (the first caller, `06_FA_playable_scenario`) → B34 (`11_GO_player_surface_contract_B`'s host). `systems/threadwork/sim/` (B03.68, B03.74): B03 → B35 (the move to `modules/threadwork/`). `engine/season/rosters.yaml` (B03.68's `thread_operations`, B03.73): B03 → B04 (U3 §5.1). `CLAUDE.md` (B03.66, B03.70): B03 → B13 (`CI-09`'s §3 seam sentence, D-09). `architecture/meta/04_CODE_ARCHITECTURE.md` (B03.70, B03.71): B03 only in this plan. `modules/mass_battle/core/state.py`, `core/exchange.py` (B03.82): B03 → B16M (L2 renames).
- **FILE CENSUS (this half's WHERE lines, by file):** `engine/season/hole_register.yaml` B03.51, B03.75, B03.76, B03.83 to B03.86 · `engine/season/seam/contest.py` B03.52 · `engine/season/loop/driver.py` B03.52, B03.56 · `engine/season/loop/matter.py` B03.52, B03.57 · `engine/season/loop/resolve.py` B03.52, B03.53, B03.55, B03.59, B03.75, B03.76 · `engine/season/state/world.py` B03.52, B03.57, B03.59, B03.83 to B03.85 · `engine/season/loop/predicates.py` B03.52, B03.81 · `engine/season/data/fixtures.py` B03.52, B03.86 · `engine/season/data/requires.py`, `data/__init__.py` B03.52 · `engine/season/data/verbs.py` B03.52, B03.57, B03.68 · `engine/season/seam/wrappers/sigma.py` B03.54 · `engine/season/state/carriers.py` B03.55, B03.58 · `engine/season/harness/probes.py` B03.55, B03.67 · `engine/season/state/log.py` B03.57 · `engine/season/rosters.yaml` B03.57, B03.68, B03.73, B03.80 · `engine/season/loop/deliberate.py` B03.58 · `engine/season/decision/sheet.py` B03.58 · `engine/season/queries/cache.py`, `state/containment.py`, `state/gate.py` B03.59 (`gate.py` also B03.75) · `engine/season/trace_log.py` B03.59 · `engine/season/harness/soak.py` B03.59, B03.67, B03.72 · `harness/interactions.py`, `harness/aperture.py` B03.59, B03.67 (docstring) · `harness/arms.py` B03.60 · `engine/season/cases/chain/*.yaml`, `harness/run_cases.py` B03.61, B03.63 · `harness/report.py` B03.62, B03.63 · `queries/world_q.py` B03.64 · `queries/faction_q.py` B03.65 · `CLAUDE.md` B03.66, B03.70 · `harness/storybar.py` B03.67, B03.72 · `harness/chronicle.py`, `harness/populated.py` B03.72 · `systems/threadwork/sim/operations.py`, `collective.py`, `opposing.py` B03.68, B03.74 · `tools/export_engine_params.py`, NEW `engine/engine_params/threadwork_params.json` B03.68, B03.74 · `engine/engine_params/sim_params.json` B03.68, B03.74 (re-derived) · `CURRENT.md`, `architecture/…` B03.70, B03.71 · `registers/handoffs/HANDOFF_FA.md`, `HANDOFF_IN.md`, `HANDOFF_SC.md` B03.77 · `research/by_lane/MB_mass_battle.md` B03.78 · `references/descriptor_registry.yaml`, `references/npc_registry.yaml`, `decision/choose.py`, `decision/options.py` B03.80 · `modules/mass_battle/core/state.py`, `core/exchange.py` B03.82 · `loop/effects_*.py` (whichever B03.83's planted test shows) · `decision/budget.py` B03.86 · NEW tests: `engine/season/tests/test_u5a_core_owed.py` (B03.53 to B03.56, B03.64), `test_event_kind_roster.py` (B03.57), `test_person_interior.py` (B03.58), `test_faction_standing.py` (B03.65), `test_thread_operations.py` (B03.68), `test_earns_contract.py` (B03.75), `test_fold_gate_refusal.py` (B03.76), `test_gate_observation.py` (B03.83 to B03.85), `test_budget.py` (B03.86), each `[ASSUMPTION: test-file name; the item creates it]` except where its source names it (E-3).
- **UNDECIDED** (each with both readings; the text takes the one that changes less, `V12_STRUCTURE_part2.md` §5.1):
  - **U-1. Is B03 a mover?** (a) §H lands in B03, as its source's Lands line ("B03 (A, B, C, D, E, H)") and the evaluation (`master/V11_EVALUATION_part15.md:35`: "none: B03 `U5a_CORE_owed_edits` §H"; IN-14 and CP-T08-10 are retired on that carrier) say; B03 is then a mover with one re-pin. (b) U3 §1 item 4 lists only "§A–C, E, F, I" and calls B03 hash EQUAL, so §H would land in B04, the next IN mover. Taken: (a) — it changes no other part, and the item's own STOPS IF (H-92's measured `test_n3` floor) turns it into a `Falsified:` commit and a revert, leaving B03 EQUAL, if the risk the register records is real. H1 writes B03's hash line from the outcome of this choice; H2's hash table lists B03 as a mover.
  - **U-2. §I's batch.** (a) B03, as U3 §1 item 4, §4.1 row 12 and `IS-B2-CORE-06`'s dormant form put it; (b) "with its first caller (B21 FA scenario or B34 GO surface)", as the source's own Lands line and its last sentence ("before that it would be a fifth caller-less Query") say. Taken: (a), the plan's batch list; the source's falsifier (a grep after GO-B's host and FA's scenario land) is moved to B34's batch gate (§5.8), and B03.65's test is its caller until then. The authors of B21 (`06_FA_playable_scenario`) and B34 (`11_GO_player_surface_contract_B`) are to call `faction_q.standing`, not re-define it.
  - **U-3. Where the threadwork tables' head lives** (B03.68). (a) As written, "they move to one typed file under `engine/engine_params/` … and the module reads the loaded form": a JSON the module loads, which then needs a head the exporter derives from. (b) Combat's shape, which the source names ("the shape combat's parameters already have"): one Python owner whose uppercase constants `tools/export_engine_params.py` auto-collects into the JSON, `--check` blocking, the oracle files importing the owner. Taken: (b) — no new head file and no new loader, and it meets the source's falsifier (no table value left in `operations.py`).
  - **U-4. The three dead constants** (B03.74 against B03.68). ER-GF9 deletes `DEPTH_TS_MINIMUM`, `BREADTH_OB`, `DISTANCE_OB` (read by nothing); edit 3 lists `DEPTH_TS_MINIMUM` among the tables that move, and CR-13 (B35, carried) may give it its reader ("if they ask for it"). Taken: `BREADTH_OB` and `DISTANCE_OB` are deleted; `DEPTH_TS_MINIMUM` moves with edit 3 and is kept for CR-13.
  - **U-5. H-143's branch.** The carry-forward block offers fail-loud or fail-soft "at ladder step 5". `04`'s row "a refusal emits, never raises | no raise path after eligibility" (`04` §C's table, MECHANICAL) decides it at step 3 and CLAUDE.md §0.05 cl. 2 forbids editing the spec to match the tests: fail-soft. Both branches are written; the text takes fail-soft.
  - **U-6. Intake placement.** §5.6's first rule would put A2-40 beside `09_WR_B_pointer_text_for_the_orchestrator` and H-291 beside `06_FA_hygiene` item 2, both in B03's first half; §4.2 gives the intake's `:112` and `:227` entries to this half and §2.2 orders them after `IS-B2-CORE-06`. Taken: §2.2's order (E-8); each item names the first-half item it sits beside in DEPENDS ON.
  - **U-7. H-4's unverified half.** The carry-forward block lists three sites "not verified": Edeyja's legacy stats block (re-authoring is cast content: `IS-A-11` stage 1 drafts the cast's values in B04, landed in BA1), the Resonant Style item (B04's item for the cast row's unread keys, `02_CHAR_capability_definitions` DEF Edit 4, reads or removes `resonant_style`) and the `fac.legitimacy` supersession row (a SITE step of B03.80). The first two are pointers, not edits here.

---

### B03.51 — register rows the CORE audits decided · `U5a_CORE_owed_edits` §A · BUILD · HASH EQUAL
- SOURCE: `proposals/U5a_CORE_owed_edits.md` §A ("Register rows", rows 1–10, "Not carried", Gate, Falsifier), "Who lands it" item 1; rulings A-4, A-62 (D-51; `04` PART D row 51 amended, A-97, node `L1-A62`); closes F-CORE-07, F-PES-CORE-09, F-CORE-17 (the audit resolutions 8–12, 14–16 and addendum B res. 9 the rows cite).
- ADVANCES: none of the nine; the register states what the tree does (hygiene, `STAGES.md` rule 5).
- INSTRUCTION (one commit, `engine/season/hole_register.yaml` only; the source's "exact edit" column, copied; row 9 is not a register row and is not edited):
  1. **H-87**: `sweep:` emptied; `cite:` gains: *"`contest_max_depth` 1, 2, 3, 7 give one content hash (headless, seed 0, two seasons, tree `601e715`): nothing recurses and the one caller passes `depth=0`, so the swept arms are identical by construction. The signature and S39.3's refusal stay (`04` D-19, D-20); the sweep returns with the first nested contest."* Jordan's answer A-4 (a duel inside a battle is a nested contest) schedules that first nesting with the PC/MB plan, which sets the cap and restores the sweep.
  2. **H-30**: `grade: measured`; `site: loop/resolve.py::_canonical_order`; `cite:` names the key `(stratum, H(seed, tick, actor, "order:verb:id"))` and the reading *"reversing the hash order inside each stratum flips 1 of 175 lap-0 acts and 6 of 774 common acts in a season (realm, seed 0; `16_PESSIMIST_CORE.md` E-07)"* (the source says "round-0"; corrected to *lap*, A-101; the code's key keeps the tree's `round` until B04).
  3. **H-47**: `hole:` re-stated *"row present, producer absent"*; `cite:` names `write_matrix.yaml`'s `(Person, coherence)` row (`:200-205` at the source's tree), the gate branch in `state/world.py` (`:1305` there) and *"no writer in any `.py`"* with the grep that shows it (`git grep -n "coherence" engine/season -- '*.py'` limited to writes; record the command run in the row).
  4. **H-48**: closed: `grade:` and `cite:` say *"never built: no `disclosure` column in `write_matrix.yaml` or `verb_table.yaml`"* with the grep (`git grep -n "disclosure" engine/season/write_matrix.yaml engine/season/verb_table.yaml` → nothing).
  5. **H-59**: closed, `cite:` *"superseded by H-57: a grudge ends by `forgive`"*.
  6. **H-56**: the held half re-graded: *"irrelevant until a nested contest is designed; returns with its reader"*; the closed half cites the one-lap arm (acts 1/4 against 16/17, seed 0) (the source says "one-round arm": the `scene_budget = 1` arm, `test_u2_the_one_round_arm_reproduces_the_pre_tick_loop`, whose identifier keeps its name).
  7. **H-82**: `grade: measured`; `cite:` names `state/log.py`'s append check (`:84-87` at the source's tree) and `tools/m1_acceptance.py`'s sweep (0 violations over 49,735 Events, 24 seeds × 4 seasons, the audit's reading, quoted as such).
  8. **H-24**: `cite:` filled with the two writers, `loop/census.py` (`:97-100` there) and `loop/matter.py` (`:277-281` there); each re-found by symbol at the item's open (`git grep -n` for the written field) and named by function.
  9. **The row that tracks `04` PART D row 51** (D-51), if one exists (`grep -n "D-51\|PART D row 51" engine/season/hole_register.yaml`): `cite:` says *"behaviour holds (a refused act costs its scene: `loop/deliberate.py` `_spent`, debited at release); the construction's falsifier fails (27 refusal Events, 0 with `changes[]`; headless, seed 0, three seasons). Two Layer-1 sources: `04` D-51 (a debit receipt) and #353 `:877`, `:912-913` (budget is a Query, never a field; H-28). Answered by Jordan's A-62: #353 holds (budget is a Query; a refusal Event carries no `changes[]`); `04` D-51 is amended (APPLIED 2026-11-12, A-97, node `L1-A62`: PART D row 51); nothing is built."* If no row tracks D-51, none is created (a register row for a Layer-1 row is not a hole in the game) and the same sentence goes to `loop/deliberate.py`'s `_spent` site as the site's own comment (that comment edit is then part of this commit).
  10. Not carried: audit res. 13 (mark `(Person, weight)` `unproduced`) — withdrawn by the source (C-U5a-02: workplan CR-08 builds the CENSUS writer). Write nothing for it.
- WHERE: `engine/season/hole_register.yaml` (rows H-87, H-30, H-47, H-48, H-59, H-56, H-82, H-24, the D-51 row if present); `engine/season/loop/deliberate.py` (the `_spent` comment, only under step 9's second branch).
- TESTS: none new; the register's own reader is the instrument.
- FALSIFIER and CONTROL: "`register --check` rejects an edited row's shape (a regrade without a `site:`)" (the source). Control: the realm content hash at seed 0, one season, equal to the batch-start reading (`reading @<sha>`; nothing the loop reads changes).
- GATE: `python -m engine.season.harness.register --check` → exit 0, and "its R2/G6 violation counts do not rise and fall by the rows whose grade moved" (the source; the audit's reading at `601e715`: R2 27, G6 3; read the before-count on the batch's base and quote both); `python -m engine.season.harness.register --requirements` → nine lines, unchanged.
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `engine/season/hole_register.yaml` rows H-87, H-30, H-47, H-48, H-59, H-56, H-82, H-24; `engine/season/harness/register.py` (`--check`); V12 Batch B02 (`01_CORE_tests_one_golden_owner`, the source's "Depends on").
- GLOSSARY: none (the *lap* correction is prose in a register row; the row *lap* is B04's, B04.01).
- COST and TIER: edit; `sonnet`, high.
- LANDS IT: B03's `valoria-author` producer, `isolation: worktree`; one `Item: B03.51` commit, `[skip ci]`.

### B03.52 — comment and docstring corrections; the shortfall field initialised; the forward declaration deleted · `U5a_CORE_owed_edits` §B rows 1–3, 5, 7–9, 11 · BUILD · HASH EQUAL
- SOURCE: `proposals/U5a_CORE_owed_edits.md` §B rows 1, 2, 3, 5, 7, 8, 9, 11; "Who lands it" item 2 ("B rows 1–3, 5, 7–11 (comment and docstring corrections; one commit; no gate beyond the file's own test)"); row 10 is B09's (`02_CHAR_reason_trail_and_small_edits.md` Part C); closes F-CORE-08 a, F-CORE-19, audit res. 18.
- ADVANCES: none of the nine; comments that state the tree.
- INSTRUCTION (one commit; each row's "exact edit", copied; each site found by the quoted text or symbol at the item's open, and a row whose text is not found is dropped with one line in the commit body, never repaired by guess, as `IS-B2-CORE-07` treats a SITE):
  1. **Row 1** — `engine/season/seam/contest.py` (the paragraph at `:222-233` in the source's tree): "delete the paragraph that says wiring the engines is out of scope (the next line dispatches to them); keep one line: what `contest` dispatches and where the provider is resolved".
  2. **Row 2** — `engine/season/loop/driver.py` (`:110-112` there): "delete the sentence that says the seam does not return yet (retracted thirty lines below)". At `aa31fd2` `grep -n "not return yet" loop/driver.py` finds nothing: open the module docstring, find the sentence by its sense (a claim that the contest seam returns nothing) and record in the commit body what was found; if it is gone, the row is dropped with that line.
  3. **Row 3** — `engine/season/loop/matter.py` (the message ending "which `census` counts", beside `w._subsistence_shortfall = short_by_person`): "read by `harness/populated.py`" (the source's `:2012`, the `getattr(w, "_subsistence_shortfall", {})` reader), not `census`. `engine/season/loop/resolve.py` (`:154` there): "the trace names H-75, the cause its own comment gives, not H-33".
  4. **Row 5** — `engine/season/state/world.py` (`World.__init__`) and `loop/matter.py`: "initialise `_subsistence_shortfall` beside `_departed`; clear it at the start of MATTER's subsistence pass; docstring says who reads it (`harness/populated.py`). It stays out of `content_hash` (an instrument's read, not state)." (`_subsistence_shortfall` is not in `World._STATE_COLLECTIONS` or `_STATE_SEQUENCES`; it stays out of both.)
  5. **Row 7** — `engine/season/loop/predicates.py` (the head comment, `:1-4`, and the tail comment, `:685-710`, at the source's tree): "the head and tail comments enumerate the nine registered predicates (`confer, convene, dispatch, establish, interrogate, oblige, release, revoke, succeed`) by reading the registry, or carry no count". Taken: carry no count (a count in a comment goes stale; the registry is the owner).
  6. **Row 8** — `engine/season/data/fixtures.py` (`:434-437` there): "the sentence 'exactly one writer … which ZEROES it' replaced by the writers at HEAD (a cast overlay, `cast.capability_of`, `_eff_train`, `_grown`), or deleted". Taken: deleted, with one line naming the writers by symbol.
  7. **Row 9** — `engine/season/data/requires.py` (`:16-23`, `:765-771` there) and `data/__init__.py` (`:4`): "references to `shape.py` as the home of `WorldReader`/`LedgerReader` and of the loaders' importer corrected to the modules that hold them" (`git grep -n "class WorldReader\|class LedgerReader" engine/season` names them).
  8. **Row 11** — `engine/season/data/verbs.py`: "delete the forward declaration `VERB_TABLE: dict = {}` and the docstring paragraph that explains it" (the declaration beside the roster block's foot, "filled after STRATA loads", and the module-docstring paragraph that begins "forward declaration below"); the assignment that fills `VERB_TABLE` stays.
- WHERE: `engine/season/seam/contest.py` (module docstring); `engine/season/loop/driver.py` (module docstring); `engine/season/loop/matter.py` (the shortfall message; the subsistence pass's head); `engine/season/loop/resolve.py` (the trace comment naming H-33); `engine/season/state/world.py` (`World.__init__`); `engine/season/loop/predicates.py` (head and tail comments); `engine/season/data/fixtures.py` (the writers sentence); `engine/season/data/requires.py`, `engine/season/data/__init__.py` (the `shape.py` references); `engine/season/data/verbs.py` (`VERB_TABLE` forward declaration and its paragraph).
- TESTS: none new; covering files: `engine/season/tests/test_season_shape.py` (the verb loader loads, row 11's gate in the source).
- FALSIFIER and CONTROL: rows 1–3, 7–9: none (comments; the source says so). Row 5: "`populated`'s census prints the same shortfall as before at seed 0". Row 11: the verb loader fails to load. Control: "hash EQUAL (`headless --case NPC-088 --seasons 2 --seed 0`)", read against the batch-start reading (`reading @<sha>`; the source's `5405522c36b0399247f83fd9f6d29494` is the pre-B01 reading, C3-N27: not the baseline).
- GATE: `PYTHONHASHSEED=0 python -m engine.season.harness.headless --case NPC-088 --seasons 2 --seed 0` → `CONTENT HASH` equal to the batch-start reading; `python -m pytest engine/season/tests/test_season_shape.py -q` → pass; `python -c "import engine.season.data.verbs as v; print(len(v.VERB_TABLE) > 0)"` → `True`; `git grep -n "VERB_TABLE: dict = {}" engine/season` → nothing.
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `seam/contest.py`, `loop/matter.py` (`w._subsistence_shortfall = short_by_person`), `harness/populated.py` (the shortfall reader), `data/verbs.py::VERB_TABLE`, `state/world.py::World.__init__` (`_departed`); V12 B03.51.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, medium.
- LANDS IT: B03's producer; `Item: B03.52`, `[skip ci]`.

### B03.53 — a contest that errors emits its row's refusal · `U5a_CORE_owed_edits` §B row 4 · BUILD · HASH EQUAL
- SOURCE: `proposals/U5a_CORE_owed_edits.md` §B row 4; "Who lands it" item 3 ("one commit each, each with its control"); audit res. 20.
- ADVANCES: none of the nine; R (completeness at the extremes: a zero depth cap), the source's NERS line.
- INSTRUCTION: `engine/season/loop/resolve.py`, the contest body (`_contest`, `:861-863` at the source's tree): "on `ContestError`, emit the row's refusal through `_refuse_party_gap`, as the `ContestRefused` arm two lines above does; an act never leaves the fold with no Event".
- WHERE: `engine/season/loop/resolve.py` (the `ContestError` arm of the contest body); NEW `engine/season/tests/test_u5a_core_owed.py` `[ASSUMPTION: test-file name; the item creates it]`.
- TESTS: in the new file, written before the edit and read red: `test_contest_error_at_depth_zero_emits_one_refusal` `[ASSUMPTION: test name]` — "a hand-built act folded at `contest_max_depth=0` yields one refusal Event of the row's kind" (red before: the fold returns `[]`).
- FALSIFIER and CONTROL: "`[]` returned at cap 0" (the source). Control: "headless hash EQUAL at the shipped cap".
- GATE: `python -m pytest engine/season/tests/test_u5a_core_owed.py -q -k contest_error` → pass; `PYTHONHASHSEED=0 python -m engine.season.harness.headless --case NPC-088 --seasons 2 --seed 0` → hash equal to B03.52's reading.
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `seam/contest.py::ContestError`, `::ContestRefused`, `loop/resolve.py::_refuse_party_gap`; V12 B03.52.
- GLOSSARY: none.
- COST and TIER: small build; `sonnet`, high.
- LANDS IT: B03's producer; `Item: B03.53`, `[skip ci]`.

### B03.54 — a provider handed no generator refuses · `U5a_CORE_owed_edits` §B row 6 · BUILD · HASH EQUAL
- SOURCE: `proposals/U5a_CORE_owed_edits.md` §B row 6; audit res. 19; addendum B C5.
- ADVANCES: none of the nine; one refusal form for a missing generator (the source's S line).
- INSTRUCTION: `engine/season/seam/wrappers/sigma.py` (the line `rng = rng if rng is not None else random.Random()`, `:533` at `aa31fd2`): "`rng is None` raises `InstrumentDefect` naming the caller, in place of `random.Random()`." "This is a boot/instrument refusal (a caller handed no generator), the loader-family refusal `04` §C.12's table asks for, not a new `raise` in play." The comment above the line and the docstring sentence "HAND CALL WITH NONE GETS A FRESH UNSEEDED `random.Random()`" are rewritten to say the call refuses. `InstrumentDefect` is imported from `engine/season/gaps.py`. The second site (`modules/combat/wrapper.py`) is not this item's (the source: "named for U5b").
- WHERE: `engine/season/seam/wrappers/sigma.py` (the `rng` default, its comment and the docstring sentence; the `gaps` import).
- TESTS: in `engine/season/tests/test_u5a_core_owed.py`: `test_sigma_provider_with_no_rng_raises_instrument_defect` `[ASSUMPTION: test name]` — "a direct call with `rng=None` raises" (red before: it draws from a fresh generator).
- FALSIFIER and CONTROL: "any season test that relied on the fallback goes red, which is the finding" (the source: such a test is reported in the commit body, not patched around). Control: "hash EQUAL (the driver always hands one)".
- GATE: `python -m pytest engine/season/tests/test_u5a_core_owed.py -q -k no_rng` → pass; the covering files `python tools/tests_for_diff.py` names for `seam/wrappers/sigma.py` → pass; realm content hash at seed 0, one season → equal to B03.52's reading.
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `engine/season/gaps.py::InstrumentDefect`, `seam/wrappers/sigma.py` (the `rng` default); V12 B03.52; Batch B03 first half (`CI-03` edits `sigma.py`'s `_ROLL_ROLE` and import first).
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, high.
- LANDS IT: B03's producer; `Item: B03.54`, `[skip ci]`.

### B03.55 — an act carries no obstacle or pool of its own · `U5a_CORE_owed_edits` §B row 12 · BUILD · HASH EQUAL
- SOURCE: `proposals/U5a_CORE_owed_edits.md` §B row 12 (including its **(U5a)** decision); addendum B res. 29.
- ADVANCES: none of the nine; one owner of the pool-and-obstacle rule (`seam/wrappers/sigma.py`).
- INSTRUCTION: "delete the fold's S27.4 arm and the fields `Act.obstacle`, `Act.pool`; the probe asks the provider (`seam/wrappers/sigma.py:543` is the rule's one owner, on the pool and obstacle the provider derives). No proposal of the suite gives an act an obstacle of its own: the task route's difficulty is a level on the verb row (`18_DETERMINISM_task_draw_for_uncontested_verbs.md` item 3, as reconciled), so this deletion meets nothing." Concretely, at `aa31fd2`: `engine/season/loop/resolve.py` — the block headed "S27.4: an attempt at Ob > 2 x Pool is REFUSED, and the season is spent" (`:1044-1063`) is deleted; `engine/season/state/carriers.py::Act` — the fields `obstacle: Optional[int] = None` and `pool: Optional[int] = None` and their comment are deleted; `engine/season/harness/probes.py` — probe `A38` ("an attempt at Ob > 2 x Pool is refused and the season is spent"), whose acts are built with `obstacle=…, pool=5`, is rewritten to build an act with no `obstacle`/`pool` and read the refusal the provider (`sigma.py`'s S27.4 rule, `ContestRefused` `REFUSED`) returns. Every other reader of `Act.obstacle`/`Act.pool` (`git grep -n "\.obstacle\b\|\.pool\b\|obstacle=\|pool=" engine/season -- '*.py'`) is listed in the commit body and re-pointed to the provider or deleted.
- WHERE: `engine/season/loop/resolve.py` (the S27.4 arm); `engine/season/state/carriers.py` (`Act.obstacle`, `Act.pool`); `engine/season/harness/probes.py` (probe `A38`).
- TESTS: none new; covering: the tests that name probe `A38` or `Act(…, obstacle=` (`grep -rln "A38\|obstacle=" engine/season/tests`), and `engine/season/tests/test_season_shape.py`.
- FALSIFIER and CONTROL: "any pinned hash moves" (the source). Control: "hash EQUAL at seeds 0–2 (realm, one season)" against B03.54's reading (the source's `5ab73af2…`, `aa58ef0b…`, `a21ab6e1…` are pre-B01 readings and are not the baseline); "the pessimist's reading is the control that the arm never fires (0 emissions in three seasons)". `Act` reaches no collection `World.content_hash()` folds (`_STATE_COLLECTIONS` are persons, rungs, offices, sites, records, propositions, dates; the log folds Event fields), so removing two of its fields is not an encoding mover `[ASSUMPTION — basis: `state/world.py::content_hash` read at `aa31fd2`; the seeds 0–2 control observes it]`.
- GATE: the realm content hash after one season at seeds 0, 1, 2 (`PYTHONHASHSEED=0`) → equal to B03.54's readings; `python -m pytest engine/season/tests/test_season_shape.py -q` → pass; `git grep -n "obstacle: Optional\[int\]\|pool: Optional\[int\]" engine/season/state/carriers.py` → nothing.
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `state/carriers.py::Act`, `loop/resolve.py` (the S27.4 block), `harness/probes.py` (probe `A38`), `seam/wrappers/sigma.py` (S27.4's refusal); V12 B03.52.
- GLOSSARY: none.
- COST and TIER: edit (a deletion); `sonnet`, high.
- LANDS IT: B03's producer; `Item: B03.55`, `[skip ci]`.

### B03.56 — a season with a scene budget under one refuses at construction · `U5a_CORE_owed_edits` §B row 18 · BUILD · HASH EQUAL
- SOURCE: `proposals/U5a_CORE_owed_edits.md` §B row 18; `16_PESSIMIST_CORE.md` res. 8; closes F-PES-CORE-10.
- ADVANCES: none of the nine; R at the extreme (a zero budget).
- INSTRUCTION: `engine/season/loop/driver.py`, where `scene_budget` is read (`rounds = int(w.fixtures.get("scene_budget"))`, `:479` at `aa31fd2`): "a `scene_budget < 1` raises the fixture's refusal naming the fixture: a season with no lap is not a season (a loader-family refusal, CLAUDE.md §0.05; not a tree-wide guard)" (the source says "no round": the season's pass, corrected to *lap*, A-101). The check runs when `SeasonDriver` is constructed ("refuses at construction (a boot refusal that aborts, `04` §C.12's loader family; never a raise in play)"); the local name `rounds` keeps the tree's word until B04.
- WHERE: `engine/season/loop/driver.py` (`SeasonDriver.__init__`, or the construction path that first reads `scene_budget`).
- TESTS: in `engine/season/tests/test_u5a_core_owed.py`: `test_scene_budget_zero_refuses_at_construction` `[ASSUMPTION: test name]` — "`SeasonDriver` constructed with `scene_budget = 0` refuses at construction … the shipped value loads" (red before: the driver constructs).
- FALSIFIER and CONTROL: "a season runs at 0 and deposits nothing". Control: the shipped value loads; realm hash at seed 0, one season, equal to B03.55's.
- GATE: `python -m pytest engine/season/tests/test_u5a_core_owed.py -q -k scene_budget` → pass; realm content hash at seed 0, one season → equal to B03.55's reading.
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `loop/driver.py::SeasonDriver` (the `scene_budget` read); V12 B03.52.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, medium.
- LANDS IT: B03's producer; `Item: B03.56`, `[skip ci]`.

### B03.57 — the log accepts only declared Event kinds · `U5a_CORE_owed_edits` §E row 2 · BUILD · HASH EQUAL
- SOURCE: `proposals/U5a_CORE_owed_edits.md` §E row 2 (`04` §B.13 #7, D-25), "Who lands it" item 4 ("E row 2, then E row 1"); H-220; meets IN-44's ALSO OWED (`04`'s "the log accepts no other kind", which `matter.py`'s direct appends did not meet).
- ADVANCES: none of the nine; Layer-1 conformance (MECHANICAL: one path, one refusal).
- INSTRUCTION (the source's exact edit): "`EventLog.append` takes the derived roster (`data/verbs.py::EVENT_KINDS`, handed in at `World` construction; `state/` does not import `data/`) and refuses a kind outside it; MATTER's two crossing kinds are declared where the roster derives (`rosters.yaml: logged_kinds`) if they are not already. Probes and tests that append an undeclared kind declare a test kind through the same roster parameter." At `aa31fd2`: `state/log.py::EventLog.append` checks only `Receipt`-typed changes; `data/rosters.py::check_logged_kinds` holds `logged_kinds` to a closed key set (`standing_crossed`), so a crossing kind `loop/matter.py` appends that is not in `EVENT_KINDS` is added to the roster that derives it, and `check_logged_kinds`'s closed set is widened by the same row if the kind belongs there; the commit body lists every kind `loop/matter.py` appends (`grep -n "kind=" engine/season/loop/matter.py`) and where each is declared.
- WHERE: `engine/season/state/log.py` (`EventLog.__init__`, `EventLog.append`); `engine/season/state/world.py` (`World.__init__` hands the roster in); the `World` construction sites that pass it (`git grep -n "World(" engine/season -- '*.py'`, the builder, `tiny_world`, the harness builders); `engine/season/rosters.yaml` (`logged_kinds`, only if a crossing kind is undeclared); `engine/season/data/rosters.py` (`check_logged_kinds`, the same condition); NEW `engine/season/tests/test_event_kind_roster.py` `[ASSUMPTION: test-file name; the item creates it]`.
- TESTS: in the new file, written before the edit and read red: `test_planted_undeclared_kind_is_refused_at_append` — "a planted `w.log.append(Event(kind="zz.undeclared", …))` raises"; `test_every_shipped_matter_kind_is_accepted` — one season at seed 0 runs with no refusal.
- FALSIFIER and CONTROL: "the planted append succeeds, or a shipped MATTER kind is refused (it was undeclared: declare it, do not weaken the check)". Control: "headless and realm hashes EQUAL".
- GATE: `python -m pytest engine/season/tests/test_event_kind_roster.py -q` → pass; `PYTHONHASHSEED=0 python -m engine.season.harness.headless --case NPC-088 --seasons 2 --seed 0` → hash equal to B03.56's reading; realm content hash at seed 0, one season → equal; the covering files `tools/tests_for_diff.py` names for `state/log.py` → pass (a test that appended an undeclared kind now declares a test kind, listed in the commit body).
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `state/log.py::EventLog.append`, `data/verbs.py::EVENT_KINDS`, `data/rosters.py::check_logged_kinds`, `::LOGGED_KINDS`; V12 B03.56.
- GLOSSARY: none.
- COST and TIER: small build; `sonnet`, high.
- LANDS IT: B03's producer; `Item: B03.57`, `[skip ci]`.

### B03.58 — the chooser receives a frozen copy of the person · `U5a_CORE_owed_edits` §E row 1 · BUILD · HASH EQUAL
- SOURCE: `proposals/U5a_CORE_owed_edits.md` §E row 1 (`04` §B.2 row 2: *"it receives a `PersonInterior` — a frozen copy with no store handle"*; §C.3 *"In: a frozen `PersonInterior`"*); addendum B C8; F-CHAR-12; U3 §6.3 ("`PersonInterior` as a typed class … `U5a_CORE_owed_edits.md` §E, B03"; every `decision/` signature in GO and PC reads it).
- ADVANCES: none of the nine; Layer-1 conformance (MECHANICAL at runtime).
- INSTRUCTION (the source's exact edit): "`state/carriers.py`: a frozen `PersonInterior` built by one function from the fields `decision/` reads (the list is derived by an `ast` walk of attribute reads on the person parameter under `decision/`, not typed from memory; `[UNVERIFIED: the list]`), mappings wrapped read-only, the ledger handed as the existing read-only reader; `deliberate.py:202` passes it; `decision/sheet.py::development_space` (which already copies) takes the same type. Layer 1 is not edited." The `ast` walk is run at the item's open and its output (the field list) is pasted in the commit body; the builder function is named `interior_of(p)` `[ASSUMPTION: name]`; mappings are wrapped in `types.MappingProxyType`.
- WHERE: `engine/season/state/carriers.py` (NEW class `PersonInterior`, `interior_of`); `engine/season/loop/deliberate.py` (the call that hands `choose` the person); `engine/season/decision/sheet.py` (`development_space`'s parameter type); NEW `engine/season/tests/test_person_interior.py` `[ASSUMPTION: test-file name]`.
- TESTS: `test_g2_deliberate_mutates_no_store_by_any_route` (in `engine/season/tests/test_season_shape.py` or `test_g2_token.py`, where `grep -rln` finds it) — "the planted mutation through a seated player raises at the assignment instead of being found by the digest" (edit that test's expectation in this commit); in the new file: `test_a_callback_cannot_assign_a_skill_score` — "a callback's `p.capability["argue"] = 9`" raises (red before: it succeeds).
- FALSIFIER and CONTROL: "a callback's `p.capability["argue"] = 9` succeeds". Control: "headless hash `5405522c…` EQUAL; realm seed 0 one season EQUAL", read against B03.57's readings (the source's hash is pre-B01).
- GATE: `python -m pytest engine/season/tests/test_person_interior.py -q` → pass; the file holding `test_g2_deliberate_mutates_no_store_by_any_route` → pass; headless NPC-088 two seasons seed 0 → hash equal to B03.57's; realm seed 0 one season → equal.
- HASH MOVERS: none (`PersonInterior` is not stored; `Person` is unchanged, so no encoding move, D-04).
- DEPENDS ON: EXISTS-IN-TREE `state/carriers.py::Person`, `loop/deliberate.py` (the `choose` call), `decision/sheet.py::development_space`; V12 B03.57.
- GLOSSARY: row *person interior* `[ASSUMPTION: no row today]` — "a person interior: the frozen copy of a person the chooser reads, which no assignment can change, as an interior is what is inside the person"; the identifier `capability` stays (glossary §H; a rename is Jordan's amendment, D-06).
- COST and TIER: small build; `sonnet`, high; the `ast` field list read by `opus` if any field is ambiguous (a field `decision/` writes, not only reads).
- LANDS IT: B03's producer; `Item: B03.58`, `[skip ci]`.

### B03.59 — the hot path: live tenures from the cache; the trace records only when opened · `U5a_CORE_owed_edits` §C · BUILD · HASH EQUAL
- SOURCE: `proposals/U5a_CORE_owed_edits.md` §C ("The hot path", F-CORE-09), "Who lands it" item 5 ("after `01_CORE_tests_one_golden_owner.md` lands, so 'hash EQUAL' is read against one file"); `04` §A.2, D-34.
- ADVANCES: none of the nine; the instruments' wall time (every later close reads them).
- INSTRUCTION (the source's two edits, one commit, one gate):
  1. "**Owner `engine/season/queries/cache.py`, `state/world.py:455-471`.** `w.tenures` is rebuilt (sort and concatenate) at every access and read inside loops (`containment.parent_of`, `gate.seat_hold`, `resolve._eligible`). The barrier cache already owns object-side Tenure indexes (`04` §A.2, `queries/cache`): the three readers named take the cache's live-tenure view when a cache is in scope and fall back to `w.tenures` otherwise. No new index is stored on `World` (`04` D-34: a cache is a local of the driver's step call)."
  2. "**Owner `engine/season/trace_log.py`.** `TRACE.rows` is appended on every write, event and query and cleared only by `harness/soak.py`. `TRACE` records only while an instrument has opened it (a context manager the instruments already using it enter); outside one it is a no-op. `harness/interactions.py`, `report.py`, `aperture.py` and the probes open it." The context manager is `TRACE.recording()` `[ASSUMPTION: name]`; `harness/soak.py`'s clear stays inside its own opened block.
- WHERE: `engine/season/queries/cache.py` (the live-tenure view); `engine/season/state/containment.py` (`parent_of`); `engine/season/state/gate.py` (`seat_hold`); `engine/season/loop/resolve.py` (`_eligible`); `engine/season/trace_log.py` (`Trace`, the recording switch); `engine/season/harness/interactions.py`, `report.py`, `aperture.py`, `probes.py`, `soak.py` (each opens the trace where it reads it).
- TESTS: none new in the source; covering: `grep -rln "TRACE" engine/season/tests` and the tests of `queries/cache.py`, run once.
- FALSIFIER and CONTROL: "The hash moves (an index went stale inside a step: the edit is withdrawn), or an instrument that reads `TRACE` prints an empty trace." Control: the content hash.
- GATE: "Wall time of `python -m engine.season.harness.aperture 1 0` before and after on an idle machine, with the same content hash at seed 0" (both wall times in the commit body, `time`); "`build_realm(0)` + one season" → equal to B03.58's reading (the source's `5ab73af282d0779646c38839fbab85d8` is pre-B01); seeds 1 and 2, one season → equal; `python -m engine.season.harness.interactions` at its smallest invocation prints a non-empty trace.
- HASH MOVERS: "None."
- DEPENDS ON: EXISTS-IN-TREE `queries/cache.py`, `trace_log.py::Trace` (`query`, `rows`), `state/containment.py::parent_of`, `state/gate.py::seat_hold`, `loop/resolve.py::_eligible`; V12 Batch B02 (`engine/season/tests/_realm_goldens.py`); V12 B03.58.
- GLOSSARY: none.
- COST and TIER: small build; `sonnet`, high.
- LANDS IT: B03's producer; `Item: B03.59`, `[skip ci]`.

### B03.60 — `arms` counts fought fields and refuses a z at zero · `U5a_CORE_owed_edits` §B row 13 · BUILD · HASH EQUAL
- SOURCE: `proposals/U5a_CORE_owed_edits.md` §B row 13; addendum B res. 25; F-CORE-22; CLAUDE.md §7 (`arms` is a season-loop-only n-seed comparison over one mechanic).
- ADVANCES: none of the nine; an instrument that cannot print a z over nothing.
- INSTRUCTION: `engine/season/harness/arms.py`: "`run_arm` returns the count of field Events at a fought band (`FIELD_BANDS`); `main` prints it per arm and prints `NOT-COMPUTABLE` in place of a z when it is zero in both arms; a `--fixture NAME=A,B` flag exposes the mapping form of an arm (`:192-193`)."
- WHERE: `engine/season/harness/arms.py` (`run_arm`, `main`, the argument parser).
- TESTS: none named by the source; covering: `grep -rln "harness.arms\|harness import arms" engine/season/tests`.
- FALSIFIER and CONTROL: "a z printed at zero fought fields". Control: the realm hash (the harness only).
- GATE: `PYTHONHASHSEED=0 python -m engine.season.harness.arms --n 1 --seasons 1` → prints the count line; "with a pair that differs only on a fought field and zero fought fields, the output is `NOT-COMPUTABLE`" (run with `--fixture` naming such a pair; the command and its output in the commit body).
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `harness/arms.py::run_arm`, `::main`, `FIELD_BANDS`; V12 B03.59.
- GLOSSARY: none.
- COST and TIER: small build; `sonnet`, medium.
- LANDS IT: B03's producer; `Item: B03.60`, `[skip ci]`.

### B03.61 — the six chain case files are plain YAML · `U5a_CORE_owed_edits` §B row 14 · BUILD · HASH EQUAL
- SOURCE: `proposals/U5a_CORE_owed_edits.md` §B row 14; addendum B res. 26; F-CORE-23.
- ADVANCES: none of the nine; R (a malformed corpus file), the source's NERS line.
- INSTRUCTION: "normalise the six files to plain YAML (strip the markdown fence and transcript preamble, which carry no case content); `ARC3.yaml` gains one comment stating that 37 lines above the first `- id:` were lost at authoring; delete the recovery path so the loader is `load_yaml`; the lost case is closed as unrecoverable." Before the edit, print the loaded case ids to a scratch file (`python -c "from engine.season.harness import run_cases as r; print(sorted(c.id for c in r.load_cases()))"` or the loader's own id field) and the two counts; after it, the same.
- WHERE: `engine/season/cases/chain/ARC1.yaml`, `ARC2.yaml`, `ARC3.yaml`, `NPC1.yaml`, `NPC2.yaml`, `NPC3.yaml`; `engine/season/harness/run_cases.py` (`_tolerant_yaml` deleted; the loader calls `load_yaml`).
- TESTS: none new; covering: `grep -rln "run_cases\|load_cases\|CORPUS_DEFECTS" engine/season/tests`.
- FALSIFIER and CONTROL: "a case id present before and absent after". Control: the corpus's tallies (`python -m engine.season.harness.corpus_run` at seed 0 → `DEGREES RESOLVED` and the executed-verb tallies equal to B03.60's).
- GATE: "`run_cases.load_cases()` returns 46 NPC and 97 ARC cases with `CORPUS_DEFECTS == []`; the case ids before and after are the same set" (the counts are the source's reading; the gate is the set equality and `CORPUS_DEFECTS == []`, the counts quoted as read); `git grep -n "_tolerant_yaml" engine/season` → nothing.
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `harness/run_cases.py::_tolerant_yaml`, `::load_cases`, `CORPUS_DEFECTS`; V12 B03.59.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, medium.
- LANDS IT: B03's producer; `Item: B03.61`, `[skip ci]`.

### B03.62 — `report.py` reads `TRACE` and the step list from their owners · `U5a_CORE_owed_edits` §B row 15 · BUILD · HASH EQUAL
- SOURCE: `proposals/U5a_CORE_owed_edits.md` §B row 15; addendum B res. 27.
- ADVANCES: none of the nine; an instrument that runs outside `__main__`.
- INSTRUCTION: `engine/season/harness/report.py` (`:171`, `:301`, `:76-81` at the source's tree): "import `TRACE` at module scope; derive the step-sequence text from `data/matrix.py::Step` (ENCOUNTER included); drop the hand count '46 unique NPCs' for `len()` of what was loaded". `TRACE` is opened as B03.59 made it (an instrument opens it).
- WHERE: `engine/season/harness/report.py` (the `TRACE` import, the step-sequence text, the NPC count).
- TESTS: none new.
- FALSIFIER and CONTROL: `TRACE` unresolved outside `__main__`. Control: none needed (a reader).
- GATE: "`python -c "import engine.season.harness.report as r; r.emit"` resolves `TRACE` without `__main__` (do not run `emit` against the tracked `engine/season/runs`: send output to a scratch path)"; `git grep -n "46 unique NPCs" engine/season/harness/report.py` → nothing.
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `harness/report.py::emit`, `data/matrix.py::Step`, `trace_log.py::TRACE`; V12 B03.59.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, medium.
- LANDS IT: B03's producer; `Item: B03.62`, `[skip ci]`.

### B03.63 — the case verdict `PLAYABLE` becomes `DECLARED-PRESENT` · `U5a_CORE_owed_edits` §B row 16 · BUILD · HASH EQUAL
- SOURCE: `proposals/U5a_CORE_owed_edits.md` §B row 16; addendum B res. 28.
- ADVANCES: none of the nine; one word for "playable" (the source's S line): a played run.
- INSTRUCTION: `engine/season/harness/run_cases.py::grade` and `harness/report.py`: "the verdict `PLAYABLE` is renamed `DECLARED-PRESENT` (every declared token resolves to something present); 'playable' is kept for a played run". Every occurrence in the two files (`grep -n PLAYABLE`), including comments and the honesty-rule text, is renamed; the two tests that name the verdict are renamed with it.
- WHERE: `engine/season/harness/run_cases.py` (`grade`, the verdict constants, comments); `engine/season/harness/report.py`; the test file holding `test_playable_requires_that_every_core_row_was_actually_aimed_at` and its sibling (`grep -rln "test_playable_requires" engine/season/tests`).
- TESTS: "the two tests that name the verdict (`test_playable_requires_that_every_core_row_was_actually_aimed_at` and its sibling) are renamed with it" (`test_declared_present_requires_…`), assertions unchanged but for the word.
- FALSIFIER and CONTROL: "`git grep -n PLAYABLE engine/season/harness` non-empty". Control: the verdict counts per class equal before and after.
- GATE: "`python -m engine.season.harness.run_cases` prints no `PLAYABLE`", and its per-verdict counts equal B03.61's run with `PLAYABLE` read as `DECLARED-PRESENT`; `git grep -n PLAYABLE engine/season/harness` → nothing; the renamed tests → pass.
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `harness/run_cases.py::grade`; V12 B03.61, B03.62.
- GLOSSARY: row *declared-present* `[ASSUMPTION: no row today]` — "declared-present: every token a case declares resolves to something present in the built world; it says nothing about play"; *playable* keeps "a run that was played", its rejected sense (a declared token found) noted.
- NAMES: `PLAYABLE` → `DECLARED-PRESENT`.
- COST and TIER: edit; `sonnet`, medium.
- LANDS IT: B03's producer; `Item: B03.63`, `[skip ci]`.

### B03.64 — where an Event happened, at the time it happened · `U5a_CORE_owed_edits` §B row 17 · BUILD · HASH EQUAL
- SOURCE: `proposals/U5a_CORE_owed_edits.md` §B row 17; `16_PESSIMIST_CORE.md` res. 7; F-PES-CORE-08; C3-L4 (the GO surface reads `account`, not a host-side `receipt`).
- ADVANCES: none of the nine; the record of where (a reader for the chronicle, B09's reason trail).
- INSTRUCTION: `engine/season/queries/world_q.py`, beside `event_place`: "new read `event_place_at(w, e)`: the rung of the actor's `contain` edge live at `e.emitted_at` (a closed edge is kept with `since`/`until`, so the answer is recoverable); `event_place` is unchanged and stays WITNESS's read at the Event's own tick. First reader: `harness/chronicle.py`'s per-act line (the reason trail's Edit 5); the GO surface reads the outcome through `account`, not a host-side `receipt` (C3-L4)." The chronicle's per-act line is the reason trail's (B09) and is not edited here; this item's reader until then is its test.
- WHERE: `engine/season/queries/world_q.py` (NEW `event_place_at`, beside `event_place`); `engine/season/tests/test_u5a_core_owed.py`.
- TESTS: `test_event_place_at_answers_the_place_at_emission` `[ASSUMPTION: test name]` — "realm, seed 0, two seasons: for the 39 season-0 act Events whose `event_place` differs a season later, `event_place_at` answers the season-0 place" (the 39 is the source's reading; the test asserts `checked >= 1` and that every checked Event answers the season-0 place, and prints the count; CLAUDE.md §0.1 pt 2). Red before: no `event_place_at`.
- FALSIFIER and CONTROL: "any of the 39 answers the later place". Control: realm hash EQUAL (a Query no season calls).
- GATE: `python -m pytest engine/season/tests/test_u5a_core_owed.py -q -k event_place_at` → pass, the checked count printed; realm content hash at seed 0, one season → equal to B03.63's reading.
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `queries/world_q.py::event_place`, the `contain` Tenure kind with `since`/`until`; V12 B03.59. Its first game reader: V12 Batch B09 (`01_CORE_reason_trail_in_the_act_store` Edit 5).
- GLOSSARY: none.
- COST and TIER: small build; `sonnet`, high.
- LANDS IT: B03's producer; `Item: B03.64`, `[skip ci]`.

### B03.65 — one composed reading of where a faction stands · `U5a_CORE_owed_edits` §I · BUILD · HASH EQUAL
- SOURCE: `proposals/U5a_CORE_owed_edits.md` §I (decided at ladder step 4: `endings_reached` is the precedent); `audits/17_CENSUS_C1A.md` §2, §6 item 1; F-C1A-05; `holonic_ARCHITECTURE.md` §17; `04` §A.2, PART D row 47; R2 §7b-15; placed in B03 by U3 §1 item 4 (U-2).
- ADVANCES: none of the nine; four caller-less Queries get one reader.
- INSTRUCTION (the source's steps 1 and 3; step 2's callers are other batches'):
  1. "`engine/season/queries/faction_q.py`: `standing(w, faction_prop_id, rung_id) -> FactionStanding`, beside `faction_q.resolve` …, composing `faction_q.resolve(w, faction_prop_id).holdings` as the footprint and calling `world_q.density`, `world_q.sovereign_fraction`, `world_q.provinces_of` for the rest. `FactionStanding` is a frozen return record dropped with the view (`04` PART D row 47). It holds exactly the four readings and nothing computed twice: `footprint` (rung ids), `present` and `persons` (`density`'s pair at `rung_id`), `sovereign_share` and `undetermined` (`sovereign_fraction(w, rung_id)`, with which holder is largest), `provinces` (`provinces_of`'s row for this faction). It takes no token, stores nothing and emits nothing. It carries no `TRACE.query` row of its own, for the reason `endings_reached` gives (a read-only step moves no committed artifact); the inner `sovereign_fraction` row is reached only when a host asks, never inside `season()`."
  2. "A person's own reading of where a faction stands stays a belief (AX-2): this record is resolver-side and may not be handed to `decision/`. An NPC weighs territory through the claims he holds, as today." (the docstring says so).
  3. Callers (the source's step 2, not this item): "the host-side faction view of `11_GO_player_surface_contract_B.md` (a seated person's faction, beside `account`), and the per-season print of `06_FA_playable_scenario.md`'s gate" — B34 and B21 call this Query and define no second one.
- WHERE: `engine/season/queries/faction_q.py` (NEW `standing`, NEW frozen dataclass `FactionStanding`); NEW `engine/season/tests/test_faction_standing.py` `[ASSUMPTION: test-file name]`.
- TESTS: in the new file, written before the edit and read red: `test_standing_footprint_equals_footprint_for_every_holding_faction` and `test_present_never_exceeds_persons_at_the_realm` (the source's gate as tests; `checked >= 1` asserted).
- FALSIFIER and CONTROL: the source's falsifier ("After GO-B's host and FA's scenario land, `grep -rn "footprint(\|density(\|sovereign_fraction(\|provinces_of(" engine/season --include=*.py` outside `tests/` still finds only definitions") reads the effect of later batches: moved to B34's batch gate (§5.8; U-2). Here: a `standing` whose `footprint` differs from `footprint(w, f)`. Control: "the season's content hash is EQUAL with and without one call per faction per season (a reader)".
- GATE: "On `build_realm(0)` played one season: for every faction with a live hold, `faction_q.standing(...).footprint` is non-empty and equals `footprint(w, f)`; summed `present` over factions at the realm rung does not exceed `persons`; the season's content hash is EQUAL with and without one call per faction per season" → `python -m pytest engine/season/tests/test_faction_standing.py -q` → pass, and the realm hash at seed 0, one season, equal to B03.64's.
- HASH MOVERS: "None."
- DEPENDS ON: EXISTS-IN-TREE `queries/faction_q.py::resolve`, `queries/world_q.py::footprint`, `::density`, `::sovereign_fraction`, `::provinces_of`, `::endings_reached` (the precedent); V12 B03.59.
- GLOSSARY: row *faction standing* `[ASSUMPTION: no row today]` — "a faction's standing: where a faction stands across the land at a rung, its holdings, people, share of rule and provinces, read when asked and never stored"; it is not *standing* in a fight (`fell_to`, B14) nor *legitimacy*.
- COST and TIER: small build; `sonnet`, high.
- LANDS IT: B03's producer; `Item: B03.65`, `[skip ci]`.

### B03.66 — `CLAUDE.md` §7's sentence on the seeded pins · `U5a_CORE_owed_edits` §G · BUILD · HASH EQUAL
- SOURCE: `proposals/U5a_CORE_owed_edits.md` §G (T-22; Layer 0; "the orchestrator's edit, not an implementation lane's"); `audits/01_CORE_audit_addendum_C_tests.md` §5.
- ADVANCES: none of the nine; Layer 0 states where the pins are.
- INSTRUCTION: in `CLAUDE.md` §7, "Old: *'The seeded goldens under `engine/tests/` observe any output-moving change to campaign-reachable code but cannot separate a balance regression from noise'*. New: *'The seeded hash pins under `engine/season/tests/` observe any output-moving change to season-reachable code but cannot separate a balance regression from noise (`engine/tests/goldens/` holds one pure-function dice table)'*. The rest of §7 stands." Before the edit: `ls engine/tests/goldens/` (the source: `sigma_leverage_parity.json` only) and the B02 pin owner (`engine/season/tests/_realm_goldens.py`) read and named in the commit body; if either reading differs, the sentence names what is there. §7 carries no `(RULED)` mark at `aa31fd2` (checked at the edit: a `(RULED)` mark stops the item and it goes to the PR body's held-back list). The PR body lists the edit under "Layer 0/1 hunks" (ED-IN-0300's form).
- WHERE: `CLAUDE.md` (§7, one sentence).
- TESTS: none; covering: `grep -rl "CLAUDE.md" tests/valoria` (the files that read it, e.g. `test_no_polling_triggers.py` reads §11), run once.
- FALSIFIER and CONTROL: `ls engine/tests/goldens/` lists a seeded realm pin (then the new sentence is false). Control: `wc -l CLAUDE.md` does not rise ("one sentence for one"; the cap is CLAUDE.md's head).
- GATE: `grep -n "seeded hash pins under \`engine/season/tests/\`" CLAUDE.md` → one line; `wc -l CLAUDE.md` → at or below its cap; `python tools/currency_consistency_check.py` → exit 0; `python tools/valoria_local.py --staged` → exit 0.
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `CLAUDE.md` §7, `engine/tests/goldens/`; V12 Batch B02 (`_realm_goldens.py`, the pins the sentence names).
- GLOSSARY: none.
- COST and TIER: edit; the orchestrator's own commit (`opus` session), not a `valoria-author` producer.
- LANDS IT: the batch's orchestrator (Layer 0 is the agent's binding file; CLAUDE.md "EDIT THIS FILE"); one `Item: B03.66` commit, `[skip ci]`; the PR body names it under "Layer 0/1 hunks".
