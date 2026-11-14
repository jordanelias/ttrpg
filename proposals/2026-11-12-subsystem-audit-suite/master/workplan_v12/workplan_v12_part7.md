# Workplan v12 — part 7: Batch B04-capability-home

## Status: PROPOSED (a body part of workplan v12, drafted under the suite; ratified only by Jordan's adoption, `V12_STRUCTURE_part3.md` §8; resolves nothing at runtime, CLAUDE.md §0.05; not canon)

## Written against: the working tree at `8ce8d6a` (branch `ccr-62958c70-0kjhsw`), read 2026-11-12; author lane A07 of `master/workplan_v12/V12_STRUCTURE_part2.md` §4.2. Every item is written against the tree as B00 to B03a will leave it (lane A rebased by B01; the builder moved by B03c); where a symbol is named that does not exist at `8ce8d6a`, the item says which batch makes it.

**How this part was assembled.** The batch's items are the members of U3 §1 item 5 in CAP Part A's row order (`proposals/U5a_capability_home_and_two_inputs.md` "Part A": "In order; each row is an edit some proposal already states"), each row one item naming the edits that carry it; the members' edits CAP does not list follow in U3 §1.2's member order (DEF, then SC-P7, then SC-B3, then FA-P6, then `29_DICE` row 1). The plan's additions sit where `V12_STRUCTURE.md` §2.2 puts them: PCR-4 first (D-05), the trait roster (U1 §2a, A-107) after the uses loader its step 5 edits, `IS-B2-CHAR-05` in the roster's commit, `IS-A-11` stage 1 last. Where U1 §11 batch U1-A and CAP Part A disagree about what lands in B04, U1-A governs (U1 line 20: "the executable plan is CAP, as amended by §11"), and each such place says so.

---

## Batch B04-capability-home · lane IN · wave W6 · step S6 · HASH MOVER(encoding), one re-pin
INVOCATION: /methodology-execute Batch B04-capability-home
IN-FLIGHT ROW: registers/handoffs/HANDOFF_IN.md, Open table
GATE: Batch B00-ids @c3418a6a160fc6a17e5a8bf45112a0e55699a695
GATE: Batch B01-laneA @cfd9aefb049c2fe49b55c7ada1b0b624919af23d
GATE: Batch B02-tests
GATE: Batch B03g-go-early-landings
GATE: Batch B03c-boot
GATE: Batch B03a-prose
HASH READING: `PYTHONHASHSEED=0 python -c "import sys; from engine.season.boot.realm import build_realm; from engine.season.harness.populated import run; s, k = int(sys.argv[1]), int(sys.argv[2]); w = build_realm(s); run(k, s, w=w); print(w.content_hash())" <s> <k>` → the realm content hash at seed `<s>` after `<k>` seasons: `<k>` = 1, one season, unless the gate names two (never more before B99, D-17); `<k>` = 0 reads the build hash; per item `<s>` = 0 (a mover's reading, E-2), at `.99` `<s>` = 0, 1, 2; each value quoted `reading @<sha>`, the tree it was read on (`workplan_v12.md` §3.B, "the hash reading").
REQUIREMENT: every conjunct of R-01, R-02, R-03, re-read (M0 closes here, `V12_STRUCTURE.md` §3) → all three hold; R-04 to R-09 print their held counts; no `status:` edited (A-114). No row moves: what the batch serves is A-6, A-7, A-11, A-12, A-98, A-101, A-106, A-107 (one skill roster, its uses as data, the trait roster, "lap" for the season's pass)
BATCH GATE (read once, on the closing tree, `PYTHONHASHSEED=0` on every seeded command):
  `python tools/export_descriptors.py --check` → exit 0 (the `capabilities:` and `traits:` blocks in the artifact);
  `python tools/export_sim_params.py --check` → exit 0; `python tools/ci_sim_fabrication_check.py` → exit 0 (the renamed `scenes_per_lap` and the new `confer_fit_weight` each carry their tag);
  `python -m engine.season.harness.headless --case NPC-088 --seasons 2 --seed 0` → its executed acts and Event tallies equal B03a's close reading (`reading @<sha>`); its `CONTENT HASH` line differs, as declared (D-04), and is the value the re-pin records `[ASSUMPTION: headless prints act and Event tallies beside the hash — basis: D-04 names "the NPC-088 headless act and Event tallies"; the output format was not opened by this lane]`;
  `python -m engine.season.harness.corpus_run --seasons 2` [v12: two seasons a case, D-17; the case's own span, to `MAX_SEASONS`, is B99's] at seed 0 → `DEGREES RESOLVED` and the executed-verb tallies equal B03a's close reading (`reading @<sha>`) (U3 §1 item 5's gate, CORE "Gate (part one)");
  the realm content hash of `build_realm(s)` after one season at s = 0, 1, 2 → moved, each value recorded by the re-pin; every behaviour control above equal (D-04: an encoding mover's control is tallies-equal, never hash-equal);
  `python -m pytest engine/season/tests/test_u1_capability_surface.py engine/season/tests/test_sc_hearing_capabilities.py engine/season/tests/test_fa_office_capabilities.py engine/season/tests/test_sc01_provider.py engine/season/tests/test_cr19_competence_gain.py engine/season/tests/test_k3_thread_sensitivity.py engine/season/tests/test_go07_canonical_digest.py engine/tests/test_opposed_ob.py engine/tests/test_sigma_leverage_parity.py -q` → all pass;
  `python -m engine.season.harness.register --check` → each check's violation count (R2, G6 and any other that reports) does not rise from the reading taken at the batch's opening (quote both, `reading @<sha>`); `python -m engine.season.harness.register --requirements` → nine lines, R-01, R-02, R-03 held; `python tools/m1_acceptance.py --summary` → its verdict line quoted;
  the suites `python tools/tests_for_diff.py --base <batch-start-sha>` names (the batch touches engine core and registries: the full gates, CLAUDE.md §0.4);
  the glossary rows each item names, read against the code it landed (STAGES "The glossary always matches" rule 2): a mismatch fails the close;
  the close's commit body records `register --requirements` (nine lines), `m1_acceptance --summary`'s verdict line, the named conjuncts' readings with their tree, the `BUILT OUT`, `ENGINES` and `NULL SCENES` lines before (`reading @<sha>`) and after, and the batch's measured wall time; the last `Item:` commit writes the conjuncts' `reading:` records; `status:` is not edited (`IS-A-12`).
RE-PIN: once, in B04.99's commit (the batch's last `Item:` commit; moved from B04.26 by repair lane R1, E-1): the realm pins in `engine/season/tests/_realm_goldens.py` (B02's one pin file, `01_CORE_tests_one_golden_owner.md` "A. One owner") and the NPC-088 headless hash, read against B03a's close (`reading @<sha>`); the commit says "re-pin: encoding only (`Claim.round` → `Claim.lap` in B04.01; `Person.traits` in B04.07); tallies equal".
EXPECTED RED UNTIL B04.99 (under `[skip ci]`, E-1; one batch line, repair lane R1): the realm and corpus pins any mover item of this batch moves read red from its first mover (B04.01) to the re-pin; the files that pin them (`git grep -lE '"[0-9a-f]{32}"'` over the test trees and the golden files, those this batch names): `engine/season/tests/_realm_goldens.py` (B02's one pin file); `engine/season/tests/test_go07_canonical_digest.py` (its asserting test, `SHIPPED`/`CENSUS`); `engine/season/tests/test_cp_t03_08_tend_on_the_wounded.py`; `engine/season/tests/test_cr33_lifepaths.py`; `engine/season/tests/test_rem30_character_sheet.py`.
IDS: ED-IN 0; H 1 (B04.22's NUMBER row for `confer_fit_weight`)
DIALS AT CONTROL: `confer_fit_weight` = 0.0; set by B98; target: none stated (`06_FA_office_capabilities.md` edit 4: "the flip to a non-zero value is its own declared mover, made on a reading"; no reading named), so B98 writes it `BLOCKED (design: no target reading)` (D-22)
C(B04-capability-home): this batch's entries; the plan's head parts; `unified/U1_GLOSSARY.md` rows *lap*, *round*, *skill*, *capability*, *trait*, *rank*, *skill score*, *governing attribute*;
  `engine/season/state/carriers.py` (`Claim`, `Person`); `engine/season/loop/driver.py`; `engine/season/loop/deliberate.py`; `engine/season/loop/witness.py`; `engine/season/loop/matter.py`; `engine/season/decision/choose.py`; `engine/season/queries/person_q.py`; `engine/season/queries/world_q.py`; `engine/season/seam/wrappers/sigma.py`; `engine/season/seam/wrappers/pool.py`; `engine/season/seam/wrappers/combat.py`;
  `engine/season/data/fixtures.py`; `engine/season/data/verbs.py`; `engine/season/data/rosters.py`; `engine/season/data/cast.py`; `engine/season/decision/options.py`; `engine/season/decision/sheet.py`; `engine/season/loop/effects_combat.py`; `engine/season/loop/predicates.py`; `engine/season/boot/realm.py` (B03c); `engine/season/harness/corpus_run.py`, `probes.py`, `soak.py`, `interactions.py`;
  `engine/season/verb_table.yaml`; `engine/season/rosters.yaml`; `engine/season/offices.yaml`; `engine/season/write_matrix.yaml`; `engine/season/hole_register.yaml`; `references/descriptor_registry.yaml`; `references/npc_registry.yaml`; `tools/export_descriptors.py`; `engine/engine_params/descriptors.json`; `engine/substrate/descriptors.py`; `engine/dice_engine/sigma_leverage.py`;
  the tests named in the items; instruments: `headless`, `corpus_run`, `register`, `tools/m1_acceptance.py`, `tools/tests_for_diff.py`, `tools/ci_sim_fabrication_check.py`, `tools/export_sim_params.py`; `engine/season/tests/_realm_goldens.py` (B02);
  the closing SHAs of B00, B01, B02, B03g, B03c, B03a; the permanent surface.
SERIAL EDGES: within the batch: B04.01 first (D-05: every later item is written with `lap`); B04.02 → B04.03 (the column refuses a skill with no definition row) → B04.04 (the maps are derived from the column) → B04.05 (the uses loader resolves keys through the leaf and the derived maps) → B04.06 (the choice-side readers read the table) → B04.07 (the uses loader accepts a trait only at `edge`) → B04.17 (a believed trait); B04.05 → B04.08 (`fed_by` names table rows) and → B04.10 (`rank_at_least` is a `when` key of the table); B04.07 → B04.12 (`resonant_style` is read before the unread-key refusal lands); B04.17 → B04.22 (the claim read B04.17 extends is moved into one function); B04.09 → B04.11 (a bundle's rank is checked as a cast row's is); B04.18 → B04.19 (the cells name the new rows) → B04.21 (a seat row names a defined skill) → B04.22; B04.24 has no edge inside the batch (no caller); B04.26 last (the re-pin).
  With other batches, by file (U3 §5.1 rows, `→` is landing order): `rosters.yaml` B03 → B04 → B05; `verb_table.yaml` B03 → B04 → B07; `data/fixtures.py` B04 → B05 (and B16M in S6, a different key: `max_turns`); `seam/wrappers/sigma.py` B03 (CI-03) → B04 → B05; `seam/wrappers/pool.py` B04 → B05 → B12; `engine/dice_engine/sigma_leverage.py` B04 → B05; `queries/person_q.py` B03 → B04 → B09; `decision/options.py` B01 → B04 → B09; `decision/choose.py` B04 → B08; `data/rosters.py`, `data/verbs.py` B04 → B07; `offices.yaml` B04 → B21; `loop/effects_combat.py` B04 → B12; `seam/wrappers/combat.py` B04 → B06; `boot/realm.py` (was `populated.py`) B03c → B04 → B10; `engine/substrate/descriptors.py` B04 only.
PARALLEL: S6 with B13-pc-package (PC) and B16M-mb-engine-words (MB). Shared file: `engine/season/data/fixtures.py` with B16M (B04 edits the `scenes_per_round` key and adds `confer_fit_weight`; B16M renames `max_turns`): different keys, kept by hand at merge (`V12_STRUCTURE_part3.md` §7.3). No item here edits a file under `modules/` (every WHERE below), so CIP's `[UNVERIFIED]` that B04 edits nothing under `modules/combat` reads true for this part. B13 and B16M are hash EQUAL: B04 is the step's one mover and may merge at any position (§7.4). (Patched: P-32) Part 6 (A06) orders S6's merges B13 and B16M before B04: "B04 must re-run `export_composition.py` and `export_sim_params.py --build` after its rebase" (B13 edits `references/module_contracts.yaml` and `composition.json`; B16M.03 rebuilds `sim_params.json` with L2-1's renamed keys). So B04 merges last in S6, and after its rebase, before B04.99, it runs `python tools/export_composition.py` and `python tools/export_sim_params.py --build` and then their `--check` (expected exit 0), and re-reads its own gate lines on the rebased tree. The merge order is H2's to confirm (`H2_DECISIONS.md`).
COST: edits and small builds, one encoding rename; producer `valoria-author` on `sonnet`, `high`; B04.26's drafting on `opus`, `high`; the close's terminal critique `opus` (CAP "Lands it and tier").
EST: 13 h [estimate: `V12_STRUCTURE.md` §2.4's formula over this part's 27 positions (0.4 h × 27 + 2.5 h; B04.99 added by repair lane R1); §2.2's 7 h counted the eight members, not the commits they order]

| pos | item | source | state | hash | gates on |
|---|---|---|---|---|---|
| B04.01 | the season's "round" becomes "lap" | PCR-4 (D-05) | BUILD | MOVER(encoding) | Batch B03a |
| B04.02 | the skill definition block, its exporter check and its leaf reader; one kind | CAP A1: CORE Edits 1–2, DEF Edit 1; `IS-B2-CHAR-05` | BUILD | EQUAL | B04.01 |
| B04.03 | the `capability:` column on contested and graded verb rows | CAP A2: CORE Edit 3 (Edit 8's values) | BUILD | EQUAL | B04.02 |
| B04.04 | the verb maps derived from the column; two rosters deleted | CAP A3: CORE Edit 4 | BUILD | EQUAL | B04.03 |
| B04.05 | the ten roles, the site map and the uses table, with its loader | CAP A4: MAP §G edits 1–2, `02_CHAR_capability_uses_table` edits 1–2 | BUILD | EQUAL | B04.04 |
| B04.06 | the decision layer's two literals become rows | CAP A5: `02_CHAR_capability_uses_table` edits 3–5 | BUILD | EQUAL | B04.05 |
| B04.07 | the trait roster: home, exporter, reader, holding, uses | U1 §2a steps 1–5 (A-107); `02_CHAR_which_ground_moves_whom` edit 1's rows | BUILD | MOVER(encoding) | B04.05 |
| B04.08 | the roll's record names the rows that fed it | CAP A6 (`fed_by`): MAP §G edit 6 | BUILD | EQUAL | B04.05 |
| B04.09 | a cast row may author skill scores | CAP A7: CORE Edit 5 | BUILD | EQUAL | B04.02 |
| B04.10 | `rank_at_least` as a `when` key | CAP A7: DEF Edit 2 | BUILD | EQUAL | B04.05 |
| B04.11 | a bundle may grant a skill at a rank | CAP A7: DEF Edit 3 | BUILD | EQUAL | B04.09 |
| B04.12 | the cast row's unread keys: read, removed or listed | CAP A7: DEF Edit 4 | BUILD | EQUAL | B04.07 |
| B04.13 | the development sheet shows the person | CAP A8: CORE Edit 6, DEF Edit 5 | BUILD | EQUAL | B04.02 |
| B04.14 | one Endurance default in a fight | CAP A9: CORE Edit 7 | BUILD | EQUAL | Batch B03a |
| B04.15 | a rank never passes its row's ceiling | CAP A10: MAP §G part two | BUILD | EQUAL | B04.02 |
| B04.16 | three register rows brought to the tree | DEF Edit 6 | BUILD | EQUAL | Batch B03a |
| B04.17 | a believed trait is read only from a held claim | `05_SC_capability_surface` edit 4 | BUILD | EQUAL | B04.07 |
| B04.18 | three social skills: `law`, `insight`, `deception` | `05_SC_hearing_capabilities` edit 1 | BUILD | EQUAL | B04.02 |
| B04.19 | `lie` draws on `deception`, `determine` on `law` | `05_SC_hearing_capabilities` edit 2 | BUILD | EQUAL | B04.18, B04.03 |
| B04.20 | the governance verbs' cells | `06_FA_office_capabilities` edit 1 | POINTER | — | B04.03, B04.19 |
| B04.21 | a seat row may name the skill its post calls on | `06_FA_office_capabilities` edit 3 | BUILD | EQUAL | B04.19 |
| B04.22 | the conferrer weighs the candidate, behind a setting at 0 | `06_FA_office_capabilities` edit 4 | BUILD | EQUAL | B04.21, B04.17 |
| B04.23 | a founded office's grant as data | `06_FA_office_capabilities` edit 5 | BUILD | EQUAL | Batch B03a |
| B04.24 | the pool rule, the opposition and the even line as pure functions | `29_DICE` item 29-1 (row 1) with `pool_of` (U1-A step 6) | BUILD | EQUAL | Batch B03a |
| B04.25 | a skill is never lost | `IS-B2-CHAR-04` (A-106) | POINTER | — | — |
| B04.26 | the cast's values drafted; the batch's re-pin | `IS-A-11` stage 1 | CONTENT | MOVER (the re-pin) | B04.01 to B04.24 |
| B04.99 | re-pin and close readings | `V12_STRUCTURE_part4.md` E-1; B04.26 steps 2 and 3, moved | BUILD | MOVER (the re-pin) | B04.26 |

Not in this batch, and where each is: CORE Edit 9 and CAP Part B (B05); MAP §G edits 3, 4, 5's call sites, 7 and 8 (B05, as CAP B1, B2, B5, B7 and OBS); `advantage_sources: [effort, capability]` and `obstacle_terms` (B05: U1 §11 U1-B step 4 and `U5c_SC_one_obstacle_form.md`, which owns the `obstacle_terms` roster); the `add:`/`floor:` cells of the `dice` rows (B05, U1-B step 3: the fixtures they name do not exist before CAP B2); `05_SC_hearing_capabilities` edits 3–4 and its gate 2 (B24); `05_SC_capability_surface`'s odds arm (B05, where the `edge` reader lands); `02_CHAR_which_ground_moves_whom` edits 2–4's uses rows and `when` keys (B24); `29_DICE` items 29-2 to 29-5 (B05, B15, B30); CAP Part C (BA1).

### B04.01 — the season's "round" becomes "lap" · PCR-4 · BUILD · HASH MOVER(encoding)
- SOURCE: `master/pc_round/PC_ROUND_SPEC_part2.md` "Item: PCR-4" (`:214-228`); `V12_STRUCTURE.md` D-05 (scheduled here); rulings A-101; closes the *lap* row's "identifiers keep their names until the rename" (`unified/U1_GLOSSARY.md` §D).
- ADVANCES: none of the nine; A-101 (one meaning for "round": the fight's).
- INSTRUCTION: rename the season's within-season pass — `state/carriers.py::Claim.round`, `SeasonDriver.round`, the fixture `scenes_per_round`, the `(tick, round)` keys (`questions_for(since=…)`, `_deliberated_at`), `loop/resolve.py::rival_key`'s `("round", person)` — to `lap` (PCR-4's text). The plan's form of it (D-05, §5.10): `Claim.round` → `Claim.lap`; `SeasonDriver.round` → `SeasonDriver.lap`; `scenes_per_round` → `scenes_per_lap`; the local names and docstrings that say "round" for this pass say "lap". In order:
  1. `git grep -n "\.round\b\|scenes_per_round\|\"round\"" engine/season` (PCR-4's measuring command) and record the list in the commit body; at `8ce8d6a` it names 41 non-test `.round` reads in 12 files and these files: `data/fixtures.py`, `decision/choose.py`, `harness/interactions.py`, `harness/probes.py`, `harness/soak.py`, `loop/deliberate.py`, `loop/driver.py`, `loop/matter.py`, `loop/witness.py`, `queries/person_q.py`, `queries/world_q.py`, `seam/wrappers/sigma.py`, `state/carriers.py`, and the tests `test_fi03_trail.py`, `test_season_shape.py`, `test_cp_t03_08_tend_on_the_wounded.py`, `test_cr31_heritage_regard.py` (the last two pass `round=` to `Claim`).
  2. Rename the field, the driver attribute, the fixture key (its `[JUSTIFIED: …]` tag kept on its line) and every reader and keyword found; `rival_key` is not in the tree at `8ce8d6a` (`grep -n round loop/resolve.py` finds comments only): rename it only if an earlier batch has added it.
  3. `engine/season/hole_register.yaml` H-124: its `site:` text `Fixtures scenes_per_round` → `Fixtures scenes_per_lap` (the row's other text kept; `register --check` reads the site).
  4. Harness output keys keep their strings (D-05): the `"round"` keys written by `harness/soak.py` (`"round": c.round`, `"round": round_`) and `harness/interactions.py` (`"round": d.round`, `dl["round"]`) stay `"round"`; only the attribute they read is renamed.
  5. Glossary: `unified/U1_GLOSSARY.md` row *lap*: its owner column becomes `state/carriers.py::Claim.lap`, `SeasonDriver.lap`, `Fixtures scenes_per_lap` (T), and the parenthesis "identifiers keep their names until the rename candidate … PCR-4" is struck; the rejected-synonym column (**round** for this sense) kept.
- WHERE: `engine/season/state/carriers.py` (`Claim.round`); `engine/season/loop/driver.py` (`SeasonDriver.round`, `_deliberated_at`); `engine/season/data/fixtures.py` (`scenes_per_round`); `engine/season/loop/deliberate.py`; `engine/season/loop/witness.py`; `engine/season/loop/matter.py`; `engine/season/queries/person_q.py` (`questions_for`); `engine/season/queries/world_q.py`; `engine/season/decision/choose.py`; `engine/season/seam/wrappers/sigma.py`; `engine/season/harness/probes.py`, `soak.py`, `interactions.py`; `engine/season/hole_register.yaml` (H-124 `site:`); the four test files of step 1; `unified/U1_GLOSSARY.md` (*lap*).
- TESTS: none new; the four test files of step 1 are edited with the rename and stay green; `engine/season/tests/test_go07_canonical_digest.py` green unedited (its committed vectors encode `Tenure`, `Rung`, `Observation` and a hand-built world, no `Claim`).
- FALSIFIER and CONTROL: a remaining `.round` read of the season's pass, or `scenes_per_round`, under `engine/season` (`git grep -n "\.round\b\|scenes_per_round" engine/season` prints nothing but harness output keys and the fight's words); a moved tally. Control: the NPC-088 headless act and Event tallies and `corpus_run --seasons 2` [v12: two seasons a case, D-17; the case's own span, to `MAX_SEASONS`, is B99's] seed 0's tallies equal B03a's close (`reading @<sha>`).
- GATE: `git grep -n "scenes_per_round\|\.round\b" engine/season -- '*.py'` → no hit naming the season's pass (a numeric `.round(` call, if the grep shows one, is listed in the commit body and kept); `python -m engine.season.harness.register --check` → each check's violation count (R2, G6 and any other that reports) does not rise from the reading taken at the batch's opening (quote both, `reading @<sha>`); `python tools/ci_sim_fabrication_check.py` → exit 0; `python -m pytest engine/season/tests/test_fi03_trail.py engine/season/tests/test_cp_t03_08_tend_on_the_wounded.py engine/season/tests/test_cr31_heritage_regard.py -q` → pass, and the `test_season_shape.py` tests naming `round` (`-k round`) → pass; the realm content hash (`HASH READING`) after one season at seed 0 → moved (field name in the encoding: `state/world.py::_object_head`, `_encode_into`; D-04), the tallies equal.
- HASH MOVERS: every content hash, by encoding only: `Claim`'s field name enters `World.content_hash()` (D-04; `loop/driver.py`'s own docstring: "the content hash moves only by `Claim` gaining `round`"). Declared; B04's one re-pin in B04.26.
- DEPENDS ON: EXISTS-IN-TREE `state/carriers.py::Claim.round`, `loop/driver.py::SeasonDriver.round`, `data/fixtures.py` `scenes_per_round`, `hole_register.yaml` H-124; V12 Batch B03a (comment edits on the same files, CI-02).
- GLOSSARY: *lap* (step 5). "lap": one pass of the season's deliberate, resolve and witness phases, as a runner's lap is one pass of the track.
- NAMES: `Claim.round` → `Claim.lap`; `SeasonDriver.round` → `SeasonDriver.lap`; `scenes_per_round` → `scenes_per_lap` (§5.10's B04 row).
- COST and TIER: wide mechanical rename; `sonnet`, `high` (PCR-4: a `haiku` count first; the count is step 1's command).
- LANDS IT: B04's `valoria-author` producer, `isolation: worktree`; `Item: B04.01`, `[skip ci]`.

### B04.02 — the skill definition block, its exporter check and its leaf reader; one kind · CAP A1 (CORE Edits 1–2, DEF Edit 1) with `IS-B2-CHAR-05` · BUILD · HASH EQUAL
- SOURCE: `proposals/U5a_capability_home_and_two_inputs.md` Part A row A1; `proposals/01_CORE_capability_authoring_surface.md` "Edit 1", "Edit 2"; `proposals/02_CHAR_capability_definitions.md` "Edit 1"; `unified/U1_CAPABILITY_AUTHORING_ARCHITECTURE.md` §2, §11 U1-A step 1; `master/instructions/IS_B2_SC_FI_CORE_CHAR_part2.md` `IS-B2-CHAR-05`; rulings A-6, A-7, A-11, A-98 (4), A-106; closes F-CORE-15 (part), F-CHAR-16.
- ADVANCES: none of the nine; the skill authoring surface (one kind, A-98).
- INSTRUCTION:
  1. `references/descriptor_registry.yaml`, a new block (CORE Edit 1, as U1 §2 decides it):
     ```yaml
     capabilities:
       source: "U1; A-6, A-7, A-11 (2026-11-12)"
       kinds:    [skill]                               # closed, one kind (A-98 (4)); the ten attributes are in `attributes:`, the traits in `traits:` (U1 §2a); neither is re-defined
       grows_by: [train, practice, use]                # closed; each names a rule the engine implements (`fixed` left with the traits, A-98)
       untrained: [default, none]                      # closed; what a non-holder brings (U1 §4)
       rows:
         copying: {kind: skill, gloss: "Carries a text or a message on exactly as it was given.", base: attr.mind.focus,      opposed_by: none,           untrained: default, grows_by: [train, practice],      scale: [0, 7], source: "rosters.yaml vocation_attribute (CR-20)"}
         argue:   {kind: skill, gloss: "Makes a case to someone's face and moves them by it.", base: attr.social.charisma, opposed_by: attr.mind.will, untrained: default, grows_by: [train, practice], scale: [0, 7], source: "rosters.yaml vocation_attribute (CR-20); ED-IN-0350"}
         inquiry: {kind: skill, gloss: "Finds things out: from a record, a place or a watched person.", base: attr.mind.acuity,     opposed_by: attr.mind.will, untrained: default, grows_by: [train, practice],      scale: [0, 7], source: "rosters.yaml vocation_attribute (CR-20)"}
         arms:    {kind: skill, gloss: "Fights with a weapon in hand.", base: attr.body.agility,    untrained: default, grows_by: [train, practice, use], scale: [0, 7], source: "rosters.yaml vocation_attribute (CR-20); CP-T03-04 (iv)"}
     ```
     "The four rows are today's four skills (the tree's `VOCATIONS`) with today's attributes, moved; `opposed_by` values are U1 §2's table (`copying: none`, OBS §2; `argue` and `inquiry` `attr.mind.will`; `arms` absent, which reads `base`). `gloss` is required and non-empty on every row (the exporter refuses an empty one)." (CORE Edit 1.) CAP A1's "`growth_rules` gains `fixed`" is withdrawn by A-98 (U1 §2: `fixed` left with the traits); the block above is U1 §2's. A skill is never lost (A-106): no `lapses_by` column.
  2. `tools/export_descriptors.py`: a `_capability_roster(reg)` validator beside `_heritage_roster`, refusing "a `base` or `opposed_by` that is none of the ten attribute keys or `none`, a `kind`, growth rule or `untrained` value outside its closed set, an empty `gloss`, and a `scale` that is not `[int, int]` with floor ≤ ceiling" (CORE Edit 2; U1-A step 1), and a row whose `kind` is not `skill` (a leftover `aptitude` or `trait` row, U1 §2's `kind` reader; `IS-B2-CHAR-05`: "if any still lists `aptitude` or `trait`, A-98 governs and the roster lands as `[skill]`"). Added to the export dict. Re-derive `engine/engine_params/descriptors.json` with the tool, never by hand; `--check` stays blocking.
  3. `engine/substrate/descriptors.py`, the leaf: `CapabilityRow` (a frozen dataclass: `kind, gloss, base, opposed_by, floor, ceiling, untrained, grows_by`), `CAPABILITIES: Mapping[str, CapabilityRow]`, `def capability(name) -> CapabilityRow` ("raises ValueError naming the roster, as resolve_pursuit does").
  4. DEF Edit 1's other half: "The ten attributes gain the same key [`gloss:`] where they are defined (`references/descriptor_registry.yaml: attributes`); three of them (Focus, Reason, Presence) carry no description today (`rosters.yaml:1588`)" — the three glosses are written from that roster's description lines where they exist, else `[ASSUMPTION]`-marked one-sentence glosses listed in the PR body for Jordan. `decision/sheet.py` gains `describe(key) -> str` ("the leaf's text, no `World`"), returning a skill's or an attribute's `gloss`.
  5. Glossary: row *skill* — its owner column becomes a pointer to `descriptors.CAPABILITIES` (DR `capabilities`), the rejected-synonym column kept.
- WHERE: `references/descriptor_registry.yaml` (`capabilities:`; `attributes:` glosses); `tools/export_descriptors.py` (`_capability_roster`, the export dict); `engine/engine_params/descriptors.json` (re-derived); `engine/substrate/descriptors.py` (`CapabilityRow`, `CAPABILITIES`, `capability`); `engine/season/decision/sheet.py` (`describe`); NEW `engine/season/tests/test_u1_capability_surface.py`; `unified/U1_GLOSSARY.md` (*skill*).
- TESTS: in the new file, written before step 1 and read red (no block): `test_deleting_the_block_refuses_the_load`; `test_a_definition_row_with_no_gloss_is_refused_naming_it` (DEF); `test_a_capability_row_of_a_kind_other_than_skill_is_refused` (`IS-B2-CHAR-05`, planted with a row of kind `aptitude`); `test_describe_returns_the_gloss` (DEF: `describe("inquiry")` returns the sentence). All green after the edit.
- FALSIFIER and CONTROL: "Change `argue`'s `base` to a name outside the ten: the exporter's `--check` refuses" (CORE); a planted `kind: aptitude` row that loads. Control: the shipped `[skill]` roster loads; the realm content hash at seeds 0 to 2, one season, equal to B04.01's reading (nothing reads the block yet).
- GATE: `python tools/export_descriptors.py --check` → exit 0, and → refusal with a planted empty `gloss`; `python -m pytest engine/season/tests/test_u1_capability_surface.py tests/valoria/test_descriptor_registry.py tests/valoria/test_descriptors_runtime.py -q` → pass.
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `tools/export_descriptors.py::_heritage_roster`, `engine/substrate/descriptors.py::resolve_pursuit`, `ATTRIBUTE_FLOOR`, `ATTRIBUTE_CEILING`, `decision/sheet.py::CreationRow`; V12 B04.01.
- GLOSSARY: *skill* (step 5). "gloss": a one-sentence plain description of what a skill or attribute is, as a dictionary gloss is.
- COST and TIER: edit plus a small build (the exporter and the leaf); `sonnet`, `high`.
- LANDS IT: B04's producer; `Item: B04.02`, `[skip ci]`.

### B04.03 — the `capability:` column on contested and graded verb rows · CAP A2 (CORE Edit 3, with Edit 8's values) · BUILD · HASH EQUAL
- SOURCE: CAP Part A row A2; `proposals/01_CORE_capability_authoring_surface.md` "Edit 3", "Edit 8"; U1 §5, §11 U1-A step 2; `V12_STRUCTURE.md` §2.2 (B04 row); closes F-CORE-18's "a verb's facts outside its row" (U1 §1).
- ADVANCES: none of the nine; one row holds a verb's facts.
- INSTRUCTION:
  1. `engine/season/data/verbs.py`: "`VerbRow` gains `capability: str = ""`" (CORE Edit 3).
  2. `engine/season/verb_table.yaml`: the `capability:` column "on every row that contests or is graded, with the values `verb_capability` holds on the base branch (12 rows: `tell`, `speak`, `argue`, `research`, `examine`, `surveil`, `fight`, `accept`, `capture`, `interrogate`, `arrest`, `determine`), each `[ASSUMPTION]` note carried over" (U1-A step 2). The base branch is B01's tree (lane A's three rows `interrogate: inquiry`, `arrest: arms`, `determine: argue`, D-U1-07, move to this column: CORE Edit 8's values, so Edit 8 moves nothing here). The contested rows with no skill carry `capability: none` and `capability_note:` "undeclared at authoring; every person rolls the untrained default" (CORE Edit 3): `lie` ("`capability: none` with a note until the `deception` definition row lands", re-pointed in B04.19) and `march` ("`none`, noted": "the field's skill enters at the `field` site, on the commander's record (`27_MB_A`)"). Read the B01 tree's `rosters.yaml: verb_capability` at the item's open and record its rows in the commit body; a row there not in the list above is carried too and named.
  3. The verb loader in `data/verbs.py` refuses, "as it refuses a missing `beneficiary:`": "a contested or graded row with no `capability:` key; a value that is neither a `CAPABILITIES` id nor `none`; `none` without a `capability_note:`; a `capability:` on a row that neither contests nor is graded (a column nothing reads) unless the row declares `magnitude: rate`" (CORE Edit 3; U1-A step 2: "no default by omission; `none` is spelled"). The `difficulty:` column is not added here (B05, OBS §4 step 1a).
- WHERE: `engine/season/data/verbs.py` (`VerbRow`, the verb loader); `engine/season/verb_table.yaml` (the column).
- TESTS: in `test_u1_capability_surface.py`, written before step 3 and read red: `test_a_contested_row_with_no_capability_is_refused_naming_it`; `test_a_capability_naming_no_definition_is_refused`.
- FALSIFIER and CONTROL: "Delete `capability:` from `argue`'s row: the load refuses naming the row" (CORE). Control: the realm content hash at seeds 0 to 2, one season, equal to B04.02's (`verb_capability` still feeds every reader until B04.04).
- GATE: `python -m pytest engine/season/tests/test_u1_capability_surface.py -q` → pass; the realm hash (`HASH READING`) at seed 0, one season → equal to B04.02's reading.
- HASH MOVERS: none.
- DEPENDS ON: V12 B04.02 (`CAPABILITIES`); V12 Batch B01-laneA @cfd9aefb049c2fe49b55c7ada1b0b624919af23d (lane A's three `verb_capability` rows); EXISTS-IN-TREE `data/verbs.py::VerbRow`.
- GLOSSARY: none (the column's word is *capability*, the tree's identifier for skill, glossary §B).
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B04's producer; `Item: B04.03`, `[skip ci]`.

### B04.04 — the verb maps derived from the column; two rosters deleted · CAP A3 (CORE Edit 4) · BUILD · HASH EQUAL
- SOURCE: CAP Part A row A3; `proposals/01_CORE_capability_authoring_surface.md` "Edit 4"; U1 §1 ("`rosters.yaml: verb_capability` and `vocation_attribute` are deleted in the commit that lands the block and the column"), §11 U1-A steps 2–3.
- ADVANCES: none of the nine; one owner for which skill a verb tests.
- INSTRUCTION:
  1. In `engine/season/data/verbs.py` (not `rosters.py`: "the verb table loads there; `rosters.py` cannot import it"):
     ```python
     VERB_CAPABILITY      = {row.verb: row.capability for row in VERB_TABLE.values() if row.capability not in ("", "none")}
     VOCATIONS            = frozenset(VERB_CAPABILITY.values())
     VOCATION_ATTRIBUTE   = {k: CAPABILITIES[k].base for k in VOCATIONS}
     VOCATION_OPPOSED_BY  = {k: CAPABILITIES[k].opposed_by for k in VOCATIONS if CAPABILITIES[k].opposed_by}
     ```
     "`rosters.py` re-exports nothing of them; `pool.py`, `sigma.py`, `effects_combat.py`, `world_q.py` and `corpus_run.py` change one import line each" (CORE Edit 4). The derived `VOCATION_OPPOSED_BY` holds `argue` and `inquiry` → `attr.mind.will` (the definition rows' cells) and leaves out `arms` (no cell, reads `base`) and `copying` (`none`: nobody's attribute opposes it) `[ASSUMPTION: `none` is not a member of the map — basis: the retired roster's `opposed_by` is empty (CORE "The problem"; lane A's `c5bf18a` `vocation_attribute` carries `values` only), and a `none` entry would reach `_opposition_of` as an attribute key]`. This is a change from the retired empty `opposed_by`; CAP Part A states it hash EQUAL at the shipped cast (every unauthored attribute reads the same value on B01's tree), and the realm hash below is the check: a moved hash stops the item and is reported, never re-pinned as encoding.
  2. Delete `rosters.yaml: verb_capability` and `vocation_attribute`, with `data/rosters.py::_load_vocation_attribute` and `_load_vocation_opposed_by` ("their closure checks are now the exporter's and the verb loader's"). `rosters.yaml` gains `capabilities: {from_descriptor: capabilities}` (U1 §1: "the `pursuit_axes` precedent").
  3. "`tables.lifepath_templates` keeps its place in `rosters.yaml`; its `holds:` check reads the skill ids off the leaf (`descriptors.CAPABILITIES`) instead of `VOCATIONS`, because `rosters.py` loads before the verb table and may not import it. A template may then grant a skill no verb yet tests, which the old check refused; the verb loader reports (does not refuse) a skill no row names, as `tenure_kinds_without_an_opener` reports an unopened kind." (CORE Edit 4.)
  4. The B01 tree's lane-A readers (`pool.py::score`, `rosters.yaml: task_difficulty`, `unauthored_attributes`) are untouched here; each imports the derived names from `data/verbs.py`.
- WHERE: `engine/season/data/verbs.py` (the four bindings); `engine/season/data/rosters.py` (delete `VERB_CAPABILITY`, `VOCATIONS`, `_load_vocation_attribute`, `VOCATION_ATTRIBUTE`, `_load_vocation_opposed_by`, `VOCATION_OPPOSED_BY`; the `lifepath_templates` `holds:` check); `engine/season/rosters.yaml` (delete `verb_capability`, `vocation_attribute`; add `capabilities: {from_descriptor: capabilities}`); the import line in `engine/season/seam/wrappers/pool.py`, `engine/season/seam/wrappers/sigma.py`, `engine/season/loop/effects_combat.py`, `engine/season/queries/world_q.py`, `engine/season/harness/corpus_run.py`.
- TESTS: in `test_u1_capability_surface.py`, written before step 2 against the B01 rosters and green before and after: `test_derived_vocation_maps_equal_the_retired_rosters` ("the derived `VERB_CAPABILITY`/`VOCATION_ATTRIBUTE` equal the base branch's roster values, captured as literals in the test, `==` not `approx`", U1-A tests).
- FALSIFIER and CONTROL: a derived `VERB_CAPABILITY` or `VOCATION_ATTRIBUTE` unequal to the retired roster's literal (the test compares those two, U1-A); a reader still importing from `data/rosters.py` (`git grep -n "rosters import .*VERB_CAPABILITY\|rosters import .*VOCATION" engine` prints nothing). Control: the realm content hash at seeds 0 to 2, one season, equal to B04.03's.
- GATE: `python -m pytest engine/season/tests/test_u1_capability_surface.py engine/season/tests/test_cr20_attributes.py -q` → pass; the realm hash (`HASH READING`) at seeds 0, 1, 2, one season → equal to B04.03's reading.
- HASH MOVERS: none.
- DEPENDS ON: V12 B04.03; EXISTS-IN-TREE `data/rosters.py::_load_vocation_attribute`, `::_load_vocation_opposed_by`, `rosters.yaml: verb_capability`, `vocation_attribute`, `tables.lifepath_templates`.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B04's producer; `Item: B04.04`, `[skip ci]`.

### B04.05 — the ten roles, the site map and the uses table, with its loader · CAP A4 (MAP §G edits 1–2; `02_CHAR_capability_uses_table` edits 1–2) · BUILD · HASH EQUAL
- SOURCE: CAP Part A row A4; `proposals/10_DICE_capability_axiom_map.md` §A, §C, §G "Part one" edits 1–2; `proposals/02_CHAR_capability_uses_table.md` "The resolution, decided", "The exact edits" 1–2; U1 §3 (the seven amendments), §11 U1-A step 4; rulings A-11, A-25.
- ADVANCES: none of the nine; every place a skill changes an outcome is one row.
- INSTRUCTION:
  1. `engine/season/rosters.yaml`: the roster `capability_roles: {values: [dice, addend, opposes, edge, circumstance, resource, threshold, rate, judgement, gate]}` (closed and ordered); the map `capability_use_sites` ("a map: site -> its one reader", U1 §3 item 7), with "only the sites with a reader on this tree" (U1-A step 4):
     ```yaml
     capability_use_sites:
       social_roll:       seam/wrappers/sigma.py::contest_input
       fight:             seam/wrappers/combat.py::combat_input        # applied by the module
       kit:               combat_systems.act_cost's caller (host-side shortfall)
       told_claim_credit: decision/options.py::competence
       own_state_gate:    queries/person_q.py::OwnStateReader (capability_admits)
     ```
     `choice_temper` is not a site at this batch: its reader `decision/choose.py::temper` and its fixture `temper_gain` do not exist at `8ce8d6a` (`grep -rn "temper_gain\|def temper\b" engine/season` finds nothing); it lands with its reader in B10 (`02_CHAR_resolve_and_temper.md`), and this file's loader would refuse it here ("a `use` that no reader registers is refused at import").
  2. `tables.capability_uses`, "today's rules restated (part one: hash equal)" (MAP §C), with U1 §3's columns (`use, role, key, side, when, level, per, against, gain, add, floor`):
     ```yaml
     tables:
       capability_uses:
         rows:
           - {use: social_roll,       role: dice,      key: verb, side: actor}
           - {use: social_roll,       role: opposes,   key: verb, side: subject}
           - {use: fight,             role: dice,      key: verb, side: each}
           - {use: fight,             role: opposes,   key: verb, side: each}
           - {use: fight,             role: resource,  key: attr.body.endurance, side: each}
           - {use: kit,               role: threshold, key: attr.body.strength,  side: each}
           - {use: told_claim_credit, role: judgement, key: attr.social.attunement,  side: actor, gain: competence_gain}
           - {use: own_state_gate,    role: gate,      key: prac.thread_sensitivity, side: actor, gain: thread_sensitivity_gate}
     ```
     The `dice` rows carry no `add:`/`floor:` here: those cells name `pool_add` and `pool_floor`, which CAP B2 creates in B05 (U1-B step 3 writes them there); the loader's refusal of an unregistered fixture would refuse them now. No row ships for `edge`, `circumstance`, `addend`, `rate` (MAP §C).
  3. `engine/season/data/rosters.py::_load_capability_uses`, "on the retired `_load_vocation_attribute`'s shape (every `key` resolved through `substrate.descriptors`, every `gain` a registered Fixture …)" (USES edit 2), refusing (U1-A step 4; USES "Closed both ways"; MAP §G edit 2): an unknown site, role or key (a key is a skill id of `descriptors.CAPABILITIES`, an attribute or practitioner key of the registry, or the selectors `verb` / `verb.base`, U1 §3 item 1); a field the role does not take (MAP §C's role-field table); a `circumstance` row with a negative `gain` (A-25, U1 §3 item 4); a `gate` row on any key but `prac.thread_sensitivity` or at any site but `own_state_gate` / `told_retain` (A-11, U1 §3 item 5); a `level` outside `sigma_leverage.LEVEL_SIGMA`; a `gain`, `add` or `floor` that is not a registered Fixture; a `per` outside `held`, `rank`, `mid` (U1 §3 item 2); a `use` that no reader registers. "A reader whose `use` has no row reads 'no capability' (a factor of exactly 1, or UNKNOWN for a gate), never a default." `against: true` means against the roller; `side` says whose sheet is read (U1 §3 item 3). The trait-key refusals are B04.07's.
  4. Not here: `advantage_sources: [effort, capability]` and the `obstacle_terms` roster (CAP A4 lists them in Part A; U1 §11 U1-A step 4 does not, and U1-B step 4 adds `capability` to `advantage_sources` in B05 while `U5c_SC_one_obstacle_form.md` owns `obstacle_terms` there; U1 §11 governs CAP, U1 line 20). A seat is never a use row (U1 §3 item 6).
- WHERE: `engine/season/rosters.yaml` (`capability_roles`, `capability_use_sites`, `tables.capability_uses`); `engine/season/data/rosters.py` (`_load_capability_uses`, its exports).
- TESTS: in `test_u1_capability_surface.py`, written before step 3 and read red: `test_a_gate_row_on_another_capability_is_refused`; `test_negative_circumstance_gain_is_refused`; `test_a_use_with_no_registered_reader_is_refused` (USES); `test_capability_use_with_an_unregistered_site_is_refused`; `test_a_level_outside_level_sigma_is_refused` (MAP) `[ASSUMPTION: MAP names "the roster test beside `rosters.yaml`'s other closures" with no path; U1-A puts every B04 refusal test in this file]`.
- FALSIFIER and CONTROL: "a negative-gain `circumstance` row, a `gate` row keyed on anything but Thread Sensitivity or at any site but `own_state_gate` and `told_retain` … each refused at load. Any of them loading falsifies the edit" (CAP Part A). Control: the realm content hash at seeds 0 to 2, one season, equal to B04.04's (no reader reads the table until B04.06).
- GATE: `python -m pytest engine/season/tests/test_u1_capability_surface.py -q` → pass; the realm hash (`HASH READING`) at seed 0, one season → equal to B04.04's reading.
- HASH MOVERS: none.
- DEPENDS ON: V12 B04.02, B04.04; EXISTS-IN-TREE `sigma_leverage.LEVEL_SIGMA`, `Fixtures competence_gain`, `Fixtures thread_sensitivity_gate`, `seam/wrappers/sigma.py::contest_input`, `seam/wrappers/combat.py::combat_input`, `decision/options.py::competence`, `queries/person_q.py::OwnStateReader`; MISSING (B10: `02_CHAR_resolve_and_temper.md`) `decision/choose.py::temper`, `Fixtures temper_gain` — the `choice_temper` site and row land there.
- GLOSSARY: none (the row *capability* already names `capability_uses`, `capability_roles`, `capability_use_sites` as identifiers). "use site": the one place in code that reads a given row of the uses table.
- COST and TIER: edit plus a small build (one loader); `sonnet`, `high`.
- LANDS IT: B04's producer; `Item: B04.05`, `[skip ci]`.

### B04.06 — the decision layer's two literals become rows · CAP A5 (`02_CHAR_capability_uses_table` edits 3–5) · BUILD · HASH EQUAL
- SOURCE: CAP Part A row A5; `proposals/02_CHAR_capability_uses_table.md` "The exact edits" 3–5, "Gate, falsifier"; U1 §8 (`capability_factor`, `capability_admits`), §11 U1-A step 5.
- ADVANCES: none of the nine; "no attribute name, no scale constant and no pool arithmetic under `decision/`" (USES).
- INSTRUCTION:
  1. `engine/substrate/descriptors.py`: "`about_mid` and `at_least` beside `ATTRIBUTE_FLOOR` / `ATTRIBUTE_CEILING`; `scale_of(key)` returning `(floor, ceiling)` for an attribute or a practitioner stat" (USES edit 3); `about_mid(value, floor, ceiling, gain)` (role `judgement`) and `at_least(value, threshold)` (role `gate`).
  2. `capability_factor(p, use, fx) -> float | None` ("`judgement` rows; 1 at the scale's mid-point") and `capability_admits(p, use, fx) -> bool | UNKNOWN` ("the one `gate` value (Thread Sensitivity), two sites") (U1 §8), each beside its site's one reader: `capability_factor` in `decision/options.py`, `capability_admits` in `queries/person_q.py` `[ASSUMPTION: CAP A5 says "in the substrate", U1 §8 lists them on the decision side; the leaf cannot read `rosters.yaml`'s table without importing the season, so each sits beside the one reader of its site — basis: U1 §3 item 7, "a row is read by the site's reader and by nothing else"]`.
  3. `engine/season/decision/options.py::competence` "reads its key and role from the table; the module-level `COMPETENCE_ATTRIBUTE`, `COMPETENCE_MID` and the `assert` are deleted" (USES edit 4).
  4. `engine/season/queries/person_q.py::OwnStateReader` — "the gate's key and threshold fixture come from the row; the two stems stay (they are the grammar's)" (USES edit 5). "`Person.thread_sensitivity` stays a field (its write-matrix row and its `ts:` loader are untouched)."
- WHERE: `engine/substrate/descriptors.py` (`about_mid`, `at_least`, `scale_of`); `engine/season/decision/options.py` (`competence`, `capability_factor`; delete `COMPETENCE_ATTRIBUTE`, `COMPETENCE_MID`, the `assert`); `engine/season/queries/person_q.py` (`OwnStateReader`, `capability_admits`).
- TESTS: `engine/season/tests/test_cr19_competence_gain.py` and `engine/season/tests/test_k3_thread_sensitivity.py` "stay green unedited"; new in `test_u1_capability_surface.py`, written before step 3 and read red (the decision layer ignores the table): `test_repointing_told_claim_credit_moves_the_factor_with_no_decision_edit`.
- FALSIFIER and CONTROL: "re-point the `told_claim_credit` row at `attr.mind.perception` in a test's rebound table and a hand-built hearer's refracted confidence follows Perception and ignores Attunement, with no edit under `decision/`" (USES); a failure of that is the falsifier. Control: "Hash EQUAL at seeds 0–2 (`build_realm`, one season)", equal to B04.05's reading.
- GATE: `python -m pytest engine/season/tests/test_u1_capability_surface.py engine/season/tests/test_cr19_competence_gain.py engine/season/tests/test_k3_thread_sensitivity.py -q` → pass; `git grep -n "COMPETENCE_ATTRIBUTE\|COMPETENCE_MID" engine` → no hit; the realm hash (`HASH READING`) at seeds 0, 1, 2, one season → equal to B04.05's reading.
- HASH MOVERS: none.
- DEPENDS ON: V12 B04.05; EXISTS-IN-TREE `decision/options.py::competence`, `::COMPETENCE_ATTRIBUTE`, `::COMPETENCE_MID`, `queries/person_q.py::OwnStateReader`, `descriptors.ATTRIBUTE_FLOOR`, `::ATTRIBUTE_CEILING`.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B04's producer; `Item: B04.06`, `[skip ci]`.

### B04.07 — the trait roster: home, exporter, reader, holding, uses · U1 §2a steps 1–5 (A-107), with `02_CHAR_which_ground_moves_whom` edit 1's four rows · BUILD · HASH MOVER(encoding)
- SOURCE: `unified/U1_CAPABILITY_AUTHORING_ARCHITECTURE.md` §2a (steps 1–5, "Tests", "Check", "Falsifier"); `proposals/02_CHAR_which_ground_moves_whom.md` "Exact edits" 1 (the four rows) and 4 (`traits_of`, as §2a step 4 restates it); rulings A-98 (4), A-107 ("yes, a separate roster"; `Person.traits` "a declared hash mover re-pinned once in its batch"); closes the *trait* row's `[ASSUMPTION, A-98 (4)]` (resolved by A-107).
- ADVANCES: none of the nine; a trait is held or not and never gives dice.
- INSTRUCTION ("each step lands in batch U1-A, after step 1, in one commit with its revert separable", U1 §2a):
  1. **Home.** `references/descriptor_registry.yaml`: "a `traits:` block beside `capabilities:`, schema `{source, scale: [0, 1], seated_from: npc_registry.yaml#resonant_style, rows: {<id>: {gloss, seated_by}}}`, where `seated_by` is the one `resonant_style` value that seats the trait (`evidence`, `consequence`, `authority`, `solidarity`)". The rows (`02_CHAR_which_ground_moves_whom` edit 1):
     ```yaml
     moved_by_evidence:    {seated_by: evidence,    gloss: "Yields to a case that cites something he can check."}
     moved_by_consequence: {seated_by: consequence, gloss: "Yields when shown the harm his own position has already done."}
     moved_by_authority:   {seated_by: authority,   gloss: "Yields to one who stands over him or speaks for his creed."}
     moved_by_solidarity:  {seated_by: solidarity,  gloss: "Yields to one he holds dear."}
     ```
     The four rows land here, not at U1-C or B24 `[ASSUMPTION: §2a says "the CHAR lane authors the four rows at U1-C", and `02_CHAR_which_ground_moves_whom` lands in B24; but step 4 refuses a `resonant_style` value no trait row names, and 18 of 46 cast rows carry one (`02_CHAR_which_ground_moves_whom` "The problem"), so the build refuses with an empty roster — the rows are the definitions edit 1 already writes, not content values; that file's B24 item finds edit 1 landed and is a pointer for it]`.
  2. **Exporter.** `tools/export_descriptors.py`: "a `_trait_roster(reg)` validator beside `_capability_roster`, refusing an empty `gloss`, a `scale` other than `[0, 1]`, a `seated_by` value used twice, and an id that is also a row of `capabilities:` (one id, one roster). Added to the export dict; re-derive `engine/engine_params/descriptors.json` with the tool, never by hand; `--check` stays blocking."
  3. **Reader.** `engine/substrate/descriptors.py`: "`TraitRow` (frozen dataclass: `id`, `gloss`, `seated_by`), `TRAITS: Mapping[str, TraitRow]`, `trait(id) -> TraitRow` (raises naming the roster)."
  4. **Loader and holding.** `engine/season/data/cast.py`: "`traits_of(row) -> frozenset[str]` … maps the cast row's `resonant_style:` value through `descriptors.TRAITS[*].seated_by` (no second roster: `rosters.yaml: susceptibilities` is not created), refuses a value no trait row names, and never writes into `Person.capability` (the skill map holds skills only). Where the person holds his traits is a carrier field `Person.traits: frozenset` with its `write_matrix.yaml` row (written at build only)." The builder sets it beside `heritage`'s seating (`w.persons[pid].heritage = cast.heritage_of(cast.row(cid) or {})`, `harness/populated.py` `:1357-1359` at `8ce8d6a`; in `boot/realm.py` after B03c): `w.persons[pid].traits = cast.traits_of(cast.row(cid) or {})`. A row with no `resonant_style:` gets `frozenset()`. "The registry key keeps its name and its eighteen values."
  5. **Uses.** "`data/rosters.py::_load_capability_uses` accepts a `key` that names a trait only at role `edge` with `per: held`, and refuses a trait key at any other role (this is the old 'refuses a `dice` use of a trait', restated for two rosters), a `per` other than `held` on a trait key, and a key that is in neither roster nor an attribute or registry key. The `edge` reader reads `1` if the subject holds the trait, else `0`." (The `edge` reader itself lands in B05, U1-B step 4; no trait use row ships here.)
  6. Glossary: row *trait* — its owner column becomes a pointer to `descriptors.TRAITS` (DR `traits`) and `Person.traits`; the bracketed `[ASSUMPTION, A-98 (4); reversible, listed for Jordan]` is replaced by "(A-107)"; the rejected-synonym column kept.
- WHERE: `references/descriptor_registry.yaml` (`traits:`); `tools/export_descriptors.py` (`_trait_roster`); `engine/engine_params/descriptors.json` (re-derived); `engine/substrate/descriptors.py` (`TraitRow`, `TRAITS`, `trait`); `engine/season/data/cast.py` (`traits_of`); `engine/season/state/carriers.py` (`Person.traits`); `engine/season/write_matrix.yaml` (the `Person.traits` row); `engine/season/boot/realm.py` (the seating; was `harness/populated.py`); `engine/season/data/rosters.py` (`_load_capability_uses`); `unified/U1_GLOSSARY.md` (*trait*).
- TESTS: in `engine/season/tests/test_u1_capability_surface.py`, written before the edit and read red: `test_a_trait_id_that_is_also_a_skill_is_refused`; `test_a_trait_key_outside_role_edge_is_refused`; `test_a_trait_never_enters_person_capability`; `test_an_unknown_resonant_style_is_refused` (U1 §2a "Tests"); and `test_a_dice_use_of_a_trait_is_refused` (MAP §G "Tests").
- FALSIFIER and CONTROL: "A `dice` row keyed on `moved_by_evidence` that loads; a cast row's trait found in `Person.capability`" (§2a). Control: the NPC-088 headless act and Event tallies and `corpus_run --seasons 2` [v12: two seasons a case, D-17; the case's own span, to `MAX_SEASONS`, is B99's] seed 0's tallies equal B04.06's reading (no reader reads `Person.traits` in this batch).
- GATE: `python tools/export_descriptors.py --check` → exit 0, and → refusal with a planted `scale: [0, 2]` (§2a "Check"); `python -m pytest engine/season/tests/test_u1_capability_surface.py -q` → pass; on `build_realm(0)`: the persons whose cast row carries `resonant_style:` hold exactly one trait each and no trait id appears in any `Person.capability`; the realm content hash (`HASH READING`) at seed 0, one season → moved (a new `Person` field, D-04), tallies equal.
- HASH MOVERS: every content hash, by encoding (`Person` gains a field; A-107: "a declared hash mover"). Declared; B04's one re-pin in B04.26.
- DEPENDS ON: V12 B04.02 (`_capability_roster`, `CAPABILITIES`), B04.05 (`_load_capability_uses`); V12 Batch B03c-boot (`boot/realm.py`); EXISTS-IN-TREE `data/cast.py::heritage_of`, `references/npc_registry.yaml` `resonant_style:`.
- GLOSSARY: *trait* (step 6).
- NAMES: `harness/populated.py` (the builder) → `boot/realm.py` (B03c).
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B04's producer; `Item: B04.07`, `[skip ci]`.

### B04.08 — the roll's record names the rows that fed it · CAP A6 (`fed_by`), MAP §G edit 6 · BUILD · HASH EQUAL
- SOURCE: CAP Part A row A6 and "Gate (Part A)"; `proposals/10_DICE_capability_axiom_map.md` §D "The reason trail", §G edit 6 (its `fed_by` clause), "The gate" 2; U1 §8 ("the returned record gains `fed_by`"); D-U1-06 (no `Event` field).
- ADVANCES: none of the nine; "which skills fed this roll, by which rule" has an answer the engine returns (MAP).
- INSTRUCTION: "`seam/wrappers/sigma.py::resolve` already returns a record (pool, obstacle, leverage, net …). It gains one field, `fed_by`: a tuple of `(use, role, key, side, value, contributed)` for every row that contributed, in table order, built by the same three functions that read the rows (so it cannot disagree with what was rolled). … no `Event.roll` field is added (D-U1-06)" (MAP §D). In this batch the rows that contribute to a social roll are the `social_roll` site's `dice` and `opposes` rows (B04.05): `contest_input` records, for each, the value it read (the pool's score for `dice`, the opposition for `opposes`) and what it contributed; `resolve` adds `fed_by` to both its `RESOLVED` and its `REFUSED` dicts. The rest of CAP A6 is not here: `opposed_ob` is B04.24 (no caller); `SocialContestInput.obstacle_terms` is OBS's in B05; `pool_add`/`pool_floor` carried raw on `PersonalCombatInput` is CAP B7 in B05 (U1 §11 U1-A step 6 governs CAP, U1 line 20).
- WHERE: `engine/season/seam/wrappers/sigma.py` (`contest_input`, `resolve`).
- TESTS: new in `test_u1_capability_surface.py`, written before the edit and read red (no key): `test_fed_by_on_a_graded_argue_lists_its_dice_and_opposes_rows` `[ASSUMPTION: test name; the item creates it (E-3)]` (CAP Part A gate: "`fed_by` on a graded `argue` lists exactly its `dice` and `opposes` rows"; a hand-built world, `==` on the tuple of `(use, role)` pairs).
- FALSIFIER and CONTROL: a `fed_by` that names a row the roll did not read, or omits one it did. Control: MAP's probe E-B04 ("the three host records are byte-equal to today's at shipped data", less the new key) and the realm content hash at seeds 0 to 2, one season, equal to B04.07's reading `[ASSUMPTION: `resolve`'s dict is not written whole into an `Event` — basis: D-U1-06, "no `Event.roll` field"; if a caller stores the dict and the hash moves, the item is declared HASH MOVER(encoding), rides B04's one re-pin (D-04's rule), and the commit body names the caller]`.
- GATE: `python -m pytest engine/season/tests/test_u1_capability_surface.py engine/season/tests/test_sc01_provider.py -q` → pass; the realm hash (`HASH READING`) at seeds 0, 1, 2, one season → equal to B04.07's reading.
- HASH MOVERS: none (see the assumption above).
- DEPENDS ON: V12 B04.05; EXISTS-IN-TREE `seam/wrappers/sigma.py::resolve`, `::contest_input`.
- GLOSSARY: none (the *reason trail* is `fed_by`, D-U1-06; no new word).
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B04's producer; `Item: B04.08`, `[skip ci]`.

### B04.09 — a cast row may author skill scores · CAP A7 (CORE Edit 5) · BUILD · HASH EQUAL
- SOURCE: CAP Part A row A7; `proposals/01_CORE_capability_authoring_surface.md` "Edit 5"; U1 §6.
- ADVANCES: none of the nine; the cast's skill scores have a validated home (the content is BA1's).
- INSTRUCTION: "A cast row may carry `capabilities: {<id>: <whole number>}` beside `stats:`. `cast.capabilities_of(r)` validates each id against `CAPABILITIES` and each value against the row's scale, refusing as `attributes_of` does. `capability_of(r, pool_default)` (the lifepath expansion) is unchanged and the two are merged by the builder with the authored value winning. The case overlay's `cast: capability:` is validated through the same function (`corpus_run._check_capability` calls it instead of re-checking keys against `VERB_CAPABILITY`). No row is authored by this proposal: the CHAR lane owns the content." (CORE Edit 5.)
- WHERE: `engine/season/data/cast.py` (`capabilities_of`); `engine/season/boot/realm.py` (the merge; was `harness/populated.py`); `engine/season/harness/corpus_run.py` (`_check_capability`).
- TESTS: new in `test_u1_capability_surface.py`, written before the edit and read red: `test_a_cast_capability_naming_no_definition_is_refused`, `test_a_cast_capability_above_its_scale_is_refused`, `test_an_authored_capability_wins_over_the_lifepath` `[ASSUMPTION: CORE Edit 5 names no test; these three state its three sentences — basis: §5.8, a gate needs an execution artifact]`.
- FALSIFIER and CONTROL: a cast row naming an undefined skill, or a rank above 7, that builds. Control: no cast row authors `capabilities:` at ship, so the realm content hash at seeds 0 to 2, one season, equals B04.08's reading.
- GATE: `python -m pytest engine/season/tests/test_u1_capability_surface.py -q` → pass; the realm hash (`HASH READING`) at seed 0, one season → equal to B04.08's reading.
- HASH MOVERS: none.
- DEPENDS ON: V12 B04.02; V12 Batch B03c-boot; EXISTS-IN-TREE `data/cast.py::attributes_of`, `::capability_of`, `harness/corpus_run.py::_check_capability` (`:336` at `8ce8d6a`).
- GLOSSARY: none.
- NAMES: `harness/populated.py` (the builder) → `boot/realm.py` (B03c).
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B04's producer; `Item: B04.09`, `[skip ci]`.

### B04.10 — `rank_at_least` as a `when` key · CAP A7 (DEF Edit 2) · BUILD · HASH EQUAL
- SOURCE: CAP Part A row A7; `proposals/02_CHAR_capability_definitions.md` "Edit 2", "The gate" (d); rulings A-11.
- ADVANCES: none of the nine; a skill's higher rank can change what it does.
- INSTRUCTION: "One more member of the uses table's closed `when` keys: `rank_at_least: <n>` holds when the holder's **skill rank** (the held rank on the row's `scale`, never a seat rank) in the row's `key` is at least `n`. It is how a skill's higher rank changes *what* it does: two use rows on one key, the second under `rank_at_least: 3`, selecting which levels apply. It is never a condition of attempting an act and never a `requires` stem (A-11 …). One comparison in the uses reader; no row ships." (DEF Edit 2.) The closed `when` roster and its loader check live with `_load_capability_uses` (B04.05); the comparison is a function beside it that the `edge` reader (B05) calls.
- WHERE: `engine/season/data/rosters.py` (`_load_capability_uses`: the `when` key; the comparison).
- TESTS: in `test_u1_capability_surface.py`, written before the edit and read red: `test_rank_at_least_selects_a_second_use_row` ("a planted row; holders at skill rank 2 and 3 read different levels; `==` on the level names, not `approx`"). The test reads the selected rows from the comparison, not from a roll, since the `edge` reader that turns levels into sigma lands in B05 (§5.8: the arm reading a roll moves to B05).
- FALSIFIER and CONTROL: "(d)'s two holders read alike" (DEF "The falsifier"). Control: no row ships; the realm content hash at seeds 0 to 2, one season, equal to B04.09's reading.
- GATE: `python -m pytest engine/season/tests/test_u1_capability_surface.py -q` → pass; the realm hash (`HASH READING`) at seed 0, one season → equal to B04.09's reading.
- HASH MOVERS: none.
- DEPENDS ON: V12 B04.05.
- GLOSSARY: *rank* (1) gains "`rank_at_least` selects use rows by it; it never gates an act" in the same commit. `rank_at_least`: holds when a person's rank in a skill is at least the number named, as "at least" says.
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B04's producer; `Item: B04.10`, `[skip ci]`.

### B04.11 — a bundle may grant a skill at a rank · CAP A7 (DEF Edit 3) · BUILD · HASH EQUAL
- SOURCE: CAP Part A row A7; `proposals/02_CHAR_capability_definitions.md` "Edit 3".
- ADVANCES: none of the nine; a background can grant a rank (the content is BA1's).
- INSTRUCTION: "In `tables.lifepath_templates`, an entry of `holds:` may be `{<id>: <rank>}` as well as a bare id; a bare id keeps today's meaning (the untrained value). The loader checks the rank against the skill's `scale`. No rank is authored here: which lifepath starts a person at what is content, and it only moves a pool once CORE's edit 9 (a first rank is never a loss) has landed." (DEF Edit 3.) The check reads `descriptors.CAPABILITIES[id].ceiling` (the `holds:` check reads the leaf since B04.04); `data/cast.py::capability_of` expands a `{id: rank}` entry to that rank and a bare id to `pool_default` as today.
- WHERE: `engine/season/data/rosters.py` (the `lifepath_templates` `holds:` check); `engine/season/data/cast.py` (`capability_of`).
- TESTS: new in `test_u1_capability_surface.py`, written before the edit and read red: `test_a_bundle_rank_above_its_scale_is_refused`, `test_a_bare_bundle_id_keeps_the_untrained_value` `[ASSUMPTION: DEF names no test for Edit 3; these two state its two sentences — basis: §5.8]`.
- FALSIFIER and CONTROL: a `{id: 8}` entry that loads; a bare id read as anything but `pool_default`. Control: every shipped entry is a bare id; the realm content hash at seeds 0 to 2, one season, equals B04.10's reading.
- GATE: `python -m pytest engine/season/tests/test_u1_capability_surface.py engine/season/tests/test_cr33_lifepaths.py -q` → pass; the realm hash (`HASH READING`) at seed 0, one season → equal to B04.10's reading.
- HASH MOVERS: none.
- DEPENDS ON: V12 B04.04 (the leaf-reading `holds:` check), B04.09; EXISTS-IN-TREE `rosters.yaml: tables.lifepath_templates`, `data/cast.py::capability_of`.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B04's producer; `Item: B04.11`, `[skip ci]`.

### B04.12 — the cast row's unread keys: read, removed or listed · CAP A7 (DEF Edit 4) · BUILD · HASH EQUAL
- SOURCE: CAP Part A row A7; `proposals/02_CHAR_capability_definitions.md` "Edit 4", "The gate" (a), (b), "The falsifier"; ED-IN-0225, ED-IN-0261 (as DEF cites them).
- ADVANCES: none of the nine; every key in the cast file is read or declared unread.
- INSTRUCTION: DEF Edit 4's table, applied to `references/npc_registry.yaml`:

  | key | rows | decision |
  |---|---|---|
  | `resonant_style` | 18 | **read** (by `cast.traits_of`, B04.07) |
  | `arc_trajectory` | 36 | **move and delete**: "the sentence goes to the person's NPC case file as prose; the key leaves the registry" |
  | `cultural_label` | 43 | **delete**, at both levels (17 at the row's top level, 26 inside `convictions:`) |
  | `self_other_initial` | 28 | **delete**, at both levels |
  | `certainty`, `coherence` | 8, 1 | **keep, marked** ("threadwork's tracks; no reader until that lane builds one") |

  "`engine/season/data/cast.py` gains, beside its readers, `UNREAD_KEYS = ("certainty", "coherence")` and refuses at build a row carrying a key that is neither read nor listed there." The loader's comment that steps over the two nested keys by name (`data/cast.py:220` at `8ce8d6a`, "`cultural_label` / `self_other_initial` sit here too") goes with them. First step (SITE, §5.7): open `engine/season/cases/` (at `8ce8d6a`: `NPC4.yaml`, `NPC5.yaml` at the top, `chain/`, `exercises/`, 44 files named `NPC*` in all) and record in the commit body, per person carrying `arc_trajectory`, the case file that names him or "none". Where one names him, the sentence moves there as a YAML comment beside his entry, never as a key; where none does, the sentence leaves the registry and the commit body quotes it (the commit is its record) `[ASSUMPTION: DEF names "the person's NPC case file" and no path; the case files are the corpus `tools/export_npc_roster.py` derives the roster from — basis: that tool's docstring]`.
- WHERE: `references/npc_registry.yaml` (four keys); `engine/season/data/cast.py` (`UNREAD_KEYS`, the build refusal, the `:220` skip); the case files under `engine/season/cases/` the first step names (comments only).
- TESTS: in `test_u1_capability_surface.py`, written before the edit and read red: `test_a_cast_row_key_neither_read_nor_unread_listed_is_refused` (DEF (b)).
- FALSIFIER and CONTROL: "after edit 4, a search finds a reader of a deleted key (it was not unread)" — `git grep -n "arc_trajectory\|cultural_label\|self_other_initial" engine tools` prints nothing; DEF (a): "the NPC-088 headless hash and `build_realm(0)`'s build hash, EQUAL before and after". Control: B04.11's readings.
- GATE: `python -m pytest engine/season/tests/test_u1_capability_surface.py -q` → pass; `git grep` above → no hit; `build_realm(0)`'s build hash (`HASH READING`) and the realm hash at seeds 0, 1, 2, one season → equal to B04.11's reading (U3 §3.1's "build-hash once after Edit 4 deletions" is this re-check; a moved hash stops the item: no key deleted here has a reader).
- HASH MOVERS: none (DEF "Hash movers. None … edit 4 re-checks `build_realm(0)`'s build hash").
- DEPENDS ON: V12 B04.07 (`resonant_style` read); EXISTS-IN-TREE `data/cast.py` (`:220`), `references/npc_registry.yaml` (the four keys).
- GLOSSARY: none.
- COST and TIER: edit (content edits to a file code reads); `sonnet`, `high`.
- LANDS IT: B04's producer; `Item: B04.12`, `[skip ci]`.

### B04.13 — the development sheet shows the person · CAP A8 (CORE Edit 6, DEF Edit 5) · BUILD · HASH EQUAL
- SOURCE: CAP Part A row A8 ("one change to one dataclass"); `proposals/01_CORE_capability_authoring_surface.md` "Edit 6"; `proposals/02_CHAR_capability_definitions.md` "Edit 5", "The gate" (c).
- ADVANCES: none of the nine; the play surface's sheet holds what is rolled (read by B34's sheet).
- INSTRUCTION: "`DevelopmentSheet` gains `attributes` (a frozen copy, as `CreationRow` has). No derived pool is stored on the sheet; the play surface asks `View.odds` per candidate as the chooser does." (CORE Edit 6.) "`decision/sheet.py::DevelopmentSheet` gains `thread_sensitivity`, `heritage` and `tenures` (a frozen tuple of the person's own live edges as `(kind, object)`: his seats, oaths, commits and residence). Own state only, copies only, as its other fields are." (DEF Edit 5.) One commit.
- WHERE: `engine/season/decision/sheet.py` (`DevelopmentSheet` and the function that fills it).
- TESTS: in `test_u1_capability_surface.py`, written before the edit and read red: `test_development_sheet_shows_thread_sensitivity_heritage_and_tenures` ("`p_npc_001` reads Thread Sensitivity 75", DEF (c)); `engine/season/tests/test_rem30_character_sheet.py` green.
- FALSIFIER and CONTROL: a sheet field that reads a `World` value not the person's own. Control: the sheet is not hashed; the realm content hash at seeds 0 to 2, one season, equal to B04.12's reading.
- GATE: `python -m pytest engine/season/tests/test_u1_capability_surface.py engine/season/tests/test_rem30_character_sheet.py -q` → pass; the realm hash (`HASH READING`) at seed 0, one season → equal to B04.12's reading.
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `decision/sheet.py::DevelopmentSheet`, `::CreationRow`; V12 B04.02 (`describe`, same file).
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B04's producer; `Item: B04.13`, `[skip ci]`.

### B04.14 — one Endurance default in a fight · CAP A9 (CORE Edit 7) · BUILD · HASH EQUAL
- SOURCE: CAP Part A row A9; `proposals/01_CORE_capability_authoring_surface.md` "Edit 7"; U1 §7 row 1.
- ADVANCES: none of the nine; one owner for the fight's Endurance default.
- INSTRUCTION: "`party_end` reads the combat spec's default for `end` through the module's typed export (`engine/engine_params`, section `attributes`, which `tools/export_engine_params.py` already writes) in place of the literal `4`. The registry's `default: 1` is the scale's floor value for an unauthored attribute in a *sheet*; the fight's default is the module's. Two different facts, each with one owner; the literal was a third copy of the second." (CORE Edit 7.) At `8ce8d6a` the literal is `base_end = person.attributes.get(_END_KEY, 4)` in `seam/wrappers/combat.py::party_end`, and the export carries `sections.attributes.end.default: 4` in `engine/engine_params/combat_engine_v1.json`. The reader opens the JSON once at import; the comment above the literal ("`end`'s class default is 4 (`modules/combat/attributes.py`)") is rewritten to name the export.
- WHERE: `engine/season/seam/wrappers/combat.py` (`party_end`; one module-level read of the export).
- TESTS: new in `test_u1_capability_surface.py`, written before the edit and read red: `test_party_end_default_is_the_combat_exports` (an unauthored person's `party_end` with no bands equals the export's `end.default`; with the export's value patched to 5 in the test, it reads 5) `[ASSUMPTION: CORE names no test for Edit 7 — basis: §5.8]`.
- FALSIFIER and CONTROL: a literal `4` for `end` left in `engine/season` (`git grep -n "_END_KEY, 4" engine` prints nothing). Control: the export's value is 4, so every realm hash at seeds 0 to 2, one season, and seed 2's fight (the seed that enters a fight, H-01) equal B04.13's reading.
- GATE: `python -m pytest engine/season/tests/test_u1_capability_surface.py -q` → pass; `python tools/export_engine_params.py --check` → exit 0; the realm hash (`HASH READING`) at seed 2, one season → equal to B04.13's reading.
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `seam/wrappers/combat.py::party_end`, `engine/engine_params/combat_engine_v1.json` `sections.attributes.end`, `tools/export_engine_params.py`.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B04's producer; `Item: B04.14`, `[skip ci]`.

### B04.15 — a rank never passes its row's ceiling · CAP A10 (MAP §G part two) · BUILD · HASH EQUAL
- SOURCE: CAP Part A row A10 ("`raised_capability` reads the row's ceiling … control: no ceiling (today's bytes); a mover only for a rank that would pass 7"); `proposals/10_DICE_capability_axiom_map.md` §A bounds table ("a skill's scale … today a rank has **no** ceiling"), §G "Part two"; U1 §2 (`scale` reader: "a rank never passes its ceiling").
- ADVANCES: none of the nine; R's completeness at the extreme (a rank is bounded).
- INSTRUCTION: `engine/season/loop/effects_combat.py::raised_capability(p, key)` returns `None` where `int(p.capability[key]) + 1` would pass `descriptors.capability(key).ceiling` (the row's `scale` ceiling, 7 for every row shipped), as it returns `None` today for a key `p` does not hold; its docstring names the ceiling. The never-minted rule is unchanged here (CORE Edit 9 changes it in B05).
- WHERE: `engine/season/loop/effects_combat.py` (`raised_capability`).
- TESTS: new in `test_u1_capability_surface.py`, written before the edit and read red: `test_a_rank_at_its_ceiling_is_not_raised` (a hand-built person at `arms: 7`: `raised_capability` returns `None`; at 6 it returns 7) `[ASSUMPTION: CAP names no test for A10 — basis: §5.8]`.
- FALSIFIER and CONTROL: a rank of 8 reachable by `train` or `_grown`. Control: no shipped person reaches 7 in two seasons, so the realm hash at seeds 0 to 2, one season, equals B04.14's reading ("a mover only for a rank that would pass 7").
- GATE: `python -m pytest engine/season/tests/test_u1_capability_surface.py -q` → pass; the realm hash (`HASH READING`) at seed 0, one season → equal to B04.14's reading.
- HASH MOVERS: none at shipped data.
- DEPENDS ON: V12 B04.02 (`descriptors.capability`); EXISTS-IN-TREE `loop/effects_combat.py::raised_capability` (`:262`).
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B04's producer; `Item: B04.15`, `[skip ci]`.

### B04.16 — three register rows brought to the tree · DEF Edit 6 · BUILD · HASH EQUAL
- SOURCE: `proposals/02_CHAR_capability_definitions.md` "Edit 6" and "The problem" 6.
- ADVANCES: none: register text (B6.1 rows of `audits/02_CHAR_audit_addendum_B.md`).
- INSTRUCTION: "`engine/season/hole_register.yaml`, text only: H-46's last sentence (*"`rosters.yaml` still carries the OLD thirteen"*) is struck with the date; H-148's `hole:` opens with the CR-24 state it now describes in a bracket; H-170's cite gains one line that `body_step` reads 10 today and its readings were taken at 0." (DEF Edit 6.) Each claim is re-read on the tree before it is written (the `rosters.yaml` roster H-46 names; CR-24's state for H-148; `Fixtures body_step` for H-170) and a claim no longer true at the item's open is left out and named in the commit body.
- WHERE: `engine/season/hole_register.yaml` (H-46, H-148, H-170: text only).
- TESTS: none new.
- FALSIFIER and CONTROL: a row whose `id`, `grade` or `site` changed (text only). Control: `register --check`'s violation count per check (R2, G6 and any other that reports) equal before and after (quote both, `reading @<sha>`).
- GATE: `python -m engine.season.harness.register --check` → each check's violation count (R2, G6 and any other that reports) does not rise from the reading taken at the batch's opening (quote both, `reading @<sha>`); `git diff --stat` on the item's commit → `hole_register.yaml` only.
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `hole_register.yaml` H-46 (`:522` at `8ce8d6a`), H-148 (`:3132`), H-170.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `medium`.
- LANDS IT: B04's producer; `Item: B04.16`, `[skip ci]`.

### B04.17 — a believed trait is read only from a held claim · `05_SC_capability_surface` edit 4 · BUILD · HASH EQUAL
- SOURCE: `proposals/05_SC_capability_surface.md` "Exact edits" 4, "Gate", "Falsifier"; U1 §2a; rulings A-98 (4).
- ADVANCES: none of the nine; a person knows his own traits and another's only by a claim (`04` §B.2: a decision reads no world truth).
- INSTRUCTION: "`engine/season/seam/wrappers/sigma.py::believed_input` — the believer's own traits are his to know; the subject's are `None` unless he holds a claim of them under the existing `CAPABILITY_CLAIM` rule (`sigma.py:238`, prefix `"capability:"` + the trait's id, value 0 or 1); a trait is a row of the trait roster (U1 §2a, A-98 (4)), not a skill, and the claim prefix stays the one rule `[ASSUMPTION: the prefix is kept for both rosters; a trait id is never a skill id, U1 §2a step 2]`. Unknown → `None`, never a guess. The `edge` rows on the subject's side are evaluated against the believed value in the believed input and against the held value in the true input." (SC-P7 edit 4.) The believer's own traits come from `Person.traits` (B04.07). The source's odds arm (a planted `edge` row moving `sigma.odds_of`) is read in B05, where the `edge` reader lands (§5.8): this item's gate is the claim reading only.
- WHERE: `engine/season/seam/wrappers/sigma.py` (`believed_input`).
- TESTS: in `engine/season/tests/test_sc01_provider.py` (exists), written before the edit and read red: `test_believed_input_reads_a_trait_only_from_a_held_claim` ("a believer holding no `capability:<trait>` claim of the subject reads `None` for it").
- FALSIFIER and CONTROL: a believer who holds no claim reads a subject's trait. Control: no claim of a trait is deposited by anything at ship ("NOTHING DEPOSITS", `sigma.py:235`), so the realm hash at seeds 0 to 2, one season, equals B04.16's reading.
- GATE: `python -m pytest engine/season/tests/test_sc01_provider.py -q` → pass; the realm hash (`HASH READING`) at seed 0, one season → equal to B04.16's reading.
- HASH MOVERS: none.
- DEPENDS ON: V12 B04.07 (`Person.traits`, `descriptors.TRAITS`); EXISTS-IN-TREE `seam/wrappers/sigma.py::believed_input` (`:260`), `::CAPABILITY_CLAIM` (`:238`).
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `high` (SC-P7: "an SC `valoria-author` session … inside the capability batch").
- LANDS IT: B04's producer; `Item: B04.17`, `[skip ci]`.

### B04.18 — three social skills: `law`, `insight`, `deception` · `05_SC_hearing_capabilities` edit 1 · BUILD · HASH EQUAL
- SOURCE: `proposals/05_SC_hearing_capabilities.md` "Three new definition rows", "Exact edits" 1, "Gate" 1, "Named tests"; U1 §2 (rows table), §5; U3 §4.1 row 13 (definition rows in B04, `proceeding_moves` in B24); rulings A-98 (`insight` is a skill), D-U1-03 (`rhetoric` not created).
- ADVANCES: none of the nine; the social roll's skills have names (the cast's ranks in them are BA1's).
- INSTRUCTION: `references/descriptor_registry.yaml: capabilities.rows` gains three rows ("scale `[0, 7]`, `grows_by: [train, practice]`; U1 §2"), each `gloss` the sentence given, each `base` "`grade: assumption`; a designer re-points one by editing one cell":
  ```yaml
      law:       {kind: skill, gloss: "Knows and applies the rules of a forum: procedure, definition, precedent; a judge's skill.", base: attr.mind.acuity,       untrained: default, grows_by: [train, practice], scale: [0, 7], source: "05_SC_hearing_capabilities (SC-B3); D-U1-03; U1 §5 (FA's `judgment` is `law`)"}
      insight:   {kind: skill, gloss: "Reads what a person or a bench is disposed to; never rolled.",                            base: attr.social.attunement, untrained: none,    grows_by: [train, practice], scale: [0, 7], source: "05_SC_hearing_capabilities (SC-B3); A-98 (was `aptitude`)"}
      deception: {kind: skill, gloss: "Makes another believe what one knows to be false, by word or by paper.",                base: attr.social.grace,      opposed_by: attr.mind.perception, untrained: default, grows_by: [train, practice], scale: [0, 7], source: "05_SC_hearing_capabilities (SC-B3)"}
  ```
  "`rhetoric` is **not created** (D-U1-03)". `insight` has no use row in this batch (its one row, `bench_reading`, lands in B24 with HEAR_B); the verb loader reports, and does not refuse, a skill no verb row names (B04.04 step 3). Re-derive `engine/engine_params/descriptors.json` with the tool.
- WHERE: `references/descriptor_registry.yaml` (`capabilities.rows`); `engine/engine_params/descriptors.json` (re-derived); NEW `engine/season/tests/test_sc_hearing_capabilities.py`.
- TESTS: in the new file, written before the edit and read red (no `law` row): `test_rhetoric_is_not_a_capability_row` (asserts `rhetoric` absent and `law`, `insight`, `deception` present).
- FALSIFIER and CONTROL: a `rhetoric` row, or an `insight` row whose `untrained` is not `none`. Control: "`build_realm(0..2)` one season before and after …: content hashes EQUAL (no holder)" (SC-B3 gate 1), equal to B04.17's reading.
- GATE: `python tools/export_descriptors.py --check` → exit 0; `python -m pytest engine/season/tests/test_sc_hearing_capabilities.py engine/season/tests/test_u1_capability_surface.py -q` → pass; the realm hash (`HASH READING`) at seeds 0, 1, 2, one season → equal to B04.17's reading.
- HASH MOVERS: none ("Hash movers. None at the shipped cast").
- DEPENDS ON: V12 B04.02 (the block, its validator).
- GLOSSARY: rows *skill* (U1 §2's rows table) unchanged; if `unified/U1_GLOSSARY.md` has no row naming `law`, `insight`, `deception` as skills, one line is added to *skill*'s row naming the seven skills by id, in the same commit.
- COST and TIER: edit; `sonnet`, `high` (SC-B3: "an SC `valoria-author` session … in the capability batch").
- LANDS IT: B04's producer; `Item: B04.18`, `[skip ci]`.

### B04.19 — `lie` draws on `deception`, `determine` on `law` · `05_SC_hearing_capabilities` edit 2 · BUILD · HASH EQUAL
- SOURCE: `proposals/05_SC_hearing_capabilities.md` "What draws on what", "Sequencing, not a conflict", "Exact edits" 2, "Gate" 1 and 3; `proposals/06_FA_office_capabilities.md` edit 1 and "Gate" (the two judges); `proposals/01_CORE_capability_authoring_surface.md` "Edit 8"; U1 §5.
- ADVANCES: none of the nine; a liar and a judge each roll their own skill (once BA1 gives someone a rank).
- INSTRUCTION: `engine/season/verb_table.yaml`, two cells of CORE's `capability:` column, "after CORE edit 8": `lie: deception` (its `capability: none` and `capability_note:` from B04.03 are removed; revert: restore them) and `determine: law` (was the interim `argue`; revert: `argue`). "Each re-pointing is then one cell with its own revert." `interrogate: inquiry` and `arrest: arms` are B04.03's and unchanged.
- WHERE: `engine/season/verb_table.yaml` (rows `lie`, `determine`: `capability:`); `engine/season/tests/test_sc_hearing_capabilities.py` (B04.18's, two tests added); NEW `engine/season/tests/test_fa_office_capabilities.py` (this item's TESTS create it; B04.21, B04.22, B04.23 add to it; repair lane R2a, K2 #16).
- TESTS: in `engine/season/tests/test_sc_hearing_capabilities.py`, written before the edit and read red (`lie` still `none`): `test_lie_odds_follow_deception_and_perception_not_copying` (SC-B3 gate 1: "a planted cast row holding `deception: 4` and a hearer with `attr.mind.perception: 5`: `sigma.odds_of` for that person's `lie` follows the planted values, and a planted `copying: 4` no longer moves it"); `test_fed_by_on_determine_names_law` (SC-B3 gate 3, on B04.08's record). New `engine/season/tests/test_fa_office_capabilities.py` with `test_a_judge_with_the_capability_wins_more_often_over_200_seeds` (FA gate: "two judges, one holding `law: 5`, determine identical matters over 200 seeds; the Success share differs in the holder's favour. Control: both holding nothing, the shares are equal within the seed spread (measure both)"; the test asserts it ran 200 draws per arm, `assert checked >= 200`).
- FALSIFIER and CONTROL: "A holder of `copying` whose `lie` odds move after edit 2" (SC-B3); "`faculty` ignoring the `determine` row's `capability:` cell reddens the two-judges gate" (FA). Control: nobody holds `deception` or `law` at ship, so the realm hash at seeds 0 to 2, one season, equals B04.18's reading ("With the cast as shipped, the content hash is expected unchanged; the gate measures it").
- GATE: `python -m pytest engine/season/tests/test_sc_hearing_capabilities.py engine/season/tests/test_fa_office_capabilities.py -q` → pass; the realm hash (`HASH READING`) at seeds 0, 1, 2, one season → equal to B04.18's reading (a moved hash stops the item: it would mean a shipped holder of `argue` rolled `determine`, and that is a behaviour mover no source declares).
- HASH MOVERS: none at the shipped cast.
- DEPENDS ON: V12 B04.03 (the column), B04.08 (`fed_by`), B04.18 (the rows).
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B04's producer; `Item: B04.19`, `[skip ci]`.

### B04.20 — the governance verbs' cells · `06_FA_office_capabilities` edit 1 · POINTER
- SOURCE: `proposals/06_FA_office_capabilities.md` edit 1 ("`determine: law`, `interrogate: inquiry`, `arrest: arms`"), edit 2 ("Withdrawn into edit 1").
- No work: `interrogate: inquiry` and `arrest: arms` are written by B04.03, `determine: law` by B04.19; FA edit 2's attribute row is not made ("the attribute a skill starts from is its definition row's `base`", B04.18). Closes FA-P6 edits 1–2 at B04.19's commit.

### B04.21 — a seat row may name the skill its post calls on · `06_FA_office_capabilities` edit 3 · BUILD · HASH EQUAL
- SOURCE: `proposals/06_FA_office_capabilities.md` edit 3, "Gate", "Falsifier"; C3-C15, C-16 (as the file cites them); rulings A-11.
- ADVANCES: none of the nine; a seat's post can name a skill a conferrer weighs (B04.22), never a prerequisite.
- INSTRUCTION: "`engine/season/offices.yaml`, row data, not a `Seat` field (C3-C15). A seat row may carry `capability: <a member of descriptors.CAPABILITIES> | null` (the key named `capability:`, not `vocation:`, C-16). Loader: `data/rosters.py::_load_offices` refuses a value that is not a defined skill, naming the row. No `Office` field is added and nothing is stamped onto the `hold` grant: `04` §B.7's `Seat` tuple is closed …, and the one reader (edit 4) reads the row through `data.rosters.SEAT_ROW_BY_ID[seat_id]["capability"]` (`data/rosters.py:196`; `decision/` may import `data/`, `04:656`). No shipped row names one in the first commit." The candidate content ("the Royal Marshal, the Military Commander and the Military Jarl `arms`; the Cardinal of Justice and the Senior Inquisitor `law` or `inquiry`; the Chief Parliamentary Clerk `copying`") is listed in the PR body for Jordan and not authored (D-19).
- WHERE: `engine/season/offices.yaml` (the optional seat-row key); `engine/season/data/rosters.py` (`_load_offices`).
- TESTS: in `engine/season/tests/test_fa_office_capabilities.py`, written before the edit and read red: `test_a_seat_row_naming_an_undefined_capability_is_refused`.
- FALSIFIER and CONTROL: a seat row naming an undefined skill that loads. Control: no shipped row carries the key; the realm hash at seeds 0 to 2, one season, equals B04.19's reading.
- GATE: `python -m pytest engine/season/tests/test_fa_office_capabilities.py -q` → pass; the realm hash (`HASH READING`) at seed 0, one season → equal to B04.19's reading.
- HASH MOVERS: none.
- DEPENDS ON: V12 B04.02; EXISTS-IN-TREE `data/rosters.py::_load_offices` (`:137`), `::SEAT_ROW_BY_ID` (`:196`).
- GLOSSARY: none (the *capability* row already records "a seat's `vocation:` is spelled `capability:`", U1 §9).
- COST and TIER: edit; `sonnet`, `high` (FA-P6: "Tier: `sonnet`").
- LANDS IT: B04's producer; `Item: B04.21`, `[skip ci]`.

### B04.22 — the conferrer weighs the candidate, behind a setting at 0 · `06_FA_office_capabilities` edit 4 · BUILD · HASH EQUAL
- SOURCE: `proposals/06_FA_office_capabilities.md` edit 4, "Gate", "Falsifier"; `unified/U4_DOCUMENT_STATUS.md` §3.4 (`06_FA_office_capabilities`: DEP-NOCARRIER, "the writer of a claim of another person's skill has no carrier in the suite; the term ships as `None`"); closes H-207 (the positional conferee, part: the mechanism at control).
- ADVANCES: none of the nine; whom a conferrer seats can depend on the candidate (once the setting is flipped).
- INSTRUCTION: "`decision/choose.py`'s score for a `confer` candidate gains a term over its `to` operand, through the existing terms table (`choose.score_terms`), never a branch on the verb name:
  - the conferrer's regard for `to`, read by `queries/person_q.py::regard(p, referent, fx)` (`:424`), the reader `decision/choose.py` already imports (`:44`) for its `regard` term;
  - where the seat's row names a skill (edit 3), the candidate's skill in it **as the conferrer's own ledger holds it**: a new person-side read, `believed_capability(p, other, capability) -> int | None`, over `p`'s claims about `other`. No claim on `main` carries another person's skill, so this half ships as `None` for everyone and the term is regard alone …
  Weight: one fixture, `confer_fit_weight`, shipped `0.0` (the control: today's positional order) and swept `{0.0, 0.5, 1.0}`; the flip to a non-zero value is its own declared mover, made on a reading." (FA-P6 edit 4.) "The ranking term here reads no modifier, so regard and office are not counted twice."
  The plan's one addition (one owner, CLAUDE.md §0, §8): `believed_capability` is the existing claim read inside `seam/wrappers/sigma.py::believed_input` (`[c for c in p.ledger if c.subject == subject and c.predicate == CAPABILITY_CLAIM + key]`, the latest by `(c.when, c.lap, c.confidence)`), moved into one function that `believed_input` (its skill read, and its trait read from B04.17) and this term both call `[ASSUMPTION: it lives in `queries/person_q.py` beside `regard`, a person-side read of his own ledger, and `CAPABILITY_CLAIM` moves with it, `sigma.py` importing both — basis: FA calls it "a new person-side read"; the move keeps the claim rule in one place]`.
  `engine/season/data/fixtures.py`: `confer_fit_weight=0.0` with its tag `# [JUSTIFIED: engine/season/hole_register.yaml H-<block slot 1> -- site: Fixtures confer_fit_weight, graded assumption; 06_FA_office_capabilities edit 4]`; `engine/season/hole_register.yaml`: a NUMBER row at the batch's H block slot 1 (`site: Fixtures confer_fit_weight`, grade `assumption`, sweep `0.0 / 0.5 / 1.0`, control `0.0`), in the form of the file's other fixture rows (e.g. H-239's for `thread_sensitivity_gate`).
- WHERE: `engine/season/decision/choose.py` (`score_terms`: the `confer` candidate's term); `engine/season/queries/person_q.py` (`believed_capability`, `CAPABILITY_CLAIM`); `engine/season/seam/wrappers/sigma.py` (`believed_input` calls it); `engine/season/data/fixtures.py` (`confer_fit_weight`); `engine/season/hole_register.yaml` (one NUMBER row).
- TESTS: in `engine/season/tests/test_fa_office_capabilities.py`, written before the edit and read red: `test_confer_fit_weight_zero_is_positional` ("With `confer_fit_weight` at `1.0` on a hand-built world with one vacancy and two known candidates the conferrer regards differently, the higher-regard candidate is seated; at `0.0` the lowest id is"); `engine/season/tests/test_sc01_provider.py` green (the moved claim read).
- FALSIFIER and CONTROL: "EQUAL at ship: `build_realm(0)` at build and at one and two seasons, with the three rows landed and no one holding `law`" (FA "Falsifier"). Control: `confer_fit_weight` 0.0 reproduces B04.21's reading.
- GATE: `python -m pytest engine/season/tests/test_fa_office_capabilities.py engine/season/tests/test_sc01_provider.py -q` → pass; `python -m engine.season.harness.register --check` → each check's violation count (R2, G6 and any other that reports) does not rise from the reading taken at the batch's opening (quote both, `reading @<sha>`); `python tools/ci_sim_fabrication_check.py` → exit 0; `python tools/export_sim_params.py --check` → exit 0 `[ASSUMPTION: a new fixture enters the exported sim params — basis: CLAUDE.md §0.05's backlog command names the exporter; if `--check` reports drift, re-derive with `--build` in this commit]`; `build_realm(0)`'s build hash (`HASH READING`) and its hash after one and two seasons → equal to B04.21's reading.
- HASH MOVERS: none at `confer_fit_weight = 0.0` (the flip is a declared mover in B98).
- DEPENDS ON: V12 B04.21 (the seat row's `capability:`), B04.17 (`believed_input`'s trait read); EXISTS-IN-TREE `queries/person_q.py::regard` (`:424`), `decision/choose.py::score_terms` (`:193`), `seam/wrappers/sigma.py::CAPABILITY_CLAIM` (`:238`); MISSING the writer of a `capability:` claim about another person (`U4_DOCUMENT_STATUS.md` §3.4, DEP-NOCARRIER; its named owner "U1 capability architecture §8 / CAP lane" defines readers only: `unified/U1_CAPABILITY_AUTHORING_ARCHITECTURE.md` §8 lists no writer of such a claim, and no v12 item writes one: `grep -l believed_capability workplan_v12_part*.md` → this part only). **By E-14 this item ships the machinery and the believed half is a BLOCKED sub-part** (repair lane R2a, K2 #7): `BLOCKED (design, no carrier in the suite: who learns another person's skill, and how)`; the term reads `None` and the weight sits at control (`confer_fit_weight` = 0.0, DIALS AT CONTROL); its follow-up is B98.01 (BLOCKED, design: no target reading), whose PR body names this sub-part beside the weight. Nothing here waits on it.
- GLOSSARY: none. `confer_fit_weight`: how much a conferrer's view of a candidate weighs in whom he seats, as a weight in a sum.
- IDS: H block slot 1.
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B04's producer; `Item: B04.22`, `[skip ci]`.

### B04.23 — a founded office's grant as data · `06_FA_office_capabilities` edit 5 · BUILD · HASH EQUAL
- SOURCE: `proposals/06_FA_office_capabilities.md` edit 5, "The problem" (the three constants).
- ADVANCES: none of the nine; content that sat in code is a designer's row.
- INSTRUCTION: "`engine/season/offices.yaml`, a `founding:` block beside `titles:`: `keeps: [confer, revoke]`, `conferral: appointed`, `revocation: rung_above_in_holdings`, each validated against its roster at load. `loop/predicates.py` reads the three from `data/rosters.py` and loses the constants." (FA-P6 edit 5.) The constants at `8ce8d6a`: `loop/predicates.py:255-257`, `FOUNDER_KEEPS = ("confer", "revoke")`, `FOUNDED_CONFERRAL = "appointed"`, `FOUNDED_REVOCATION = "rung_above_in_holdings"`; each `[ASSUMPTION; medium; Jordan to correct; revert: the full remit]` mark moves with its value to the block. `data/rosters.py` exports the three from `_load_offices`.
- WHERE: `engine/season/offices.yaml` (`founding:`); `engine/season/data/rosters.py` (`_load_offices`: the block, its validation, its three exports); `engine/season/loop/predicates.py` (delete the three constants; read the exports).
- TESTS: new in `test_fa_office_capabilities.py`, written before the edit and read red: `test_a_founding_value_outside_its_roster_is_refused` `[ASSUMPTION: FA names no test for edit 5 — basis: §5.8]`.
- FALSIFIER and CONTROL: `git grep -n "FOUNDER_KEEPS\|FOUNDED_CONFERRAL\|FOUNDED_REVOCATION" engine` finds a definition outside `data/rosters.py`. Control: the same three values, so the realm hash at seeds 0 to 2, one season, equals B04.22's reading.
- GATE: `python -m pytest engine/season/tests/test_fa_office_capabilities.py -q` → pass; the `git grep` above → the three names in `data/rosters.py` and their readers only; the realm hash (`HASH READING`) at seeds 0, 1, 2, one season → equal to B04.22's reading.
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `loop/predicates.py::FOUNDER_KEEPS`, `::FOUNDED_CONFERRAL`, `::FOUNDED_REVOCATION` (`:255-257`), `data/rosters.py::_load_offices`; V12 B04.21 (same loader, earlier).
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B04's producer; `Item: B04.23`, `[skip ci]`.

### B04.24 — the pool rule, the opposition and the even line as pure functions · `29_DICE` item 29-1 (row 1), with `pool_of` · BUILD · HASH EQUAL
- SOURCE: `proposals/29_DICE_one_opposed_rule_form_and_tuning.md` "Item 29-1" (governs its edit table, "where the two differ, this section governs"), "Exact edits" row 1; U1 §4, §8, §11 U1-A step 6 ("`pool_of`, `opposed_ob`, `even_line` (29 item 29-1's two plus `pool_of`), no caller yet"); CAP Part A "Named tests"; rulings A-26, A-71, A-79; D-U1-08.
- ADVANCES: none of the nine; one owner for the pool rule and the opposition (callers in B05).
- INSTRUCTION:
  1. "`engine/dice_engine/sigma_leverage.py`, directly after `net_boost` (the block *Core σ-leverage primitives*), two pure functions: `def opposed_ob(score: float, rate: float) -> float: return float(rate) * max(0.0, float(score))` and `def even_line(pool_add: float) -> float: return MU_PER_DIE * float(pool_add)`. `rate` has no default. Docstrings name A-26 and A-71, and say: the operand is a skill score, never a pool." (29-1 step 1.) Beside them, `pool_of(score, addends, pool_add, pool_floor) -> int` = `max(pool_floor, score + addends + pool_add)` (U1 §4, D-U1-08), its docstring naming A-6.
  2. "New file `engine/tests/test_opposed_ob.py`, four tests: `test_opposed_ob_at_half_is_score_over_two_exactly` (scores 0 to 20 in halves, `==`, no `approx`); `test_opposed_ob_clamps_a_negative_score_to_zero`; `test_opposed_ob_refuses_a_missing_rate` (`TypeError`); `test_even_line_is_the_owner_mean_times_the_base` (`even_line(6) == dice_engine.MU_PER_DIE * 6`)", and in the same file `test_pool_of_is_the_max_of_floor_and_sum` (U1-A tests).
  3. "Run `engine/tests/test_sigma_leverage_parity.py`. It is expected green untouched (it calls functions by golden row, `_call(fn, args)`); if it enumerates the module's names, add no golden row and say so in the commit."
- WHERE: `engine/dice_engine/sigma_leverage.py` (`opposed_ob`, `even_line`, `pool_of`); NEW `engine/tests/test_opposed_ob.py`.
- TESTS: step 2, written before step 1 and read red (no functions); green after.
- FALSIFIER and CONTROL: "No caller exists, so `headless --case NPC-088 --seasons 2 --seed 0` prints the hash of the commit before; a different hash falsifies 'no caller'." Control: B04.23's reading.
- GATE: `python -m pytest engine/tests/test_opposed_ob.py engine/tests/test_sigma_leverage_parity.py -q` → pass; `git grep -n "opposed_ob\|even_line\|pool_of" engine modules -- '*.py'` → the definitions and the test only; the NPC-088 headless hash → equal to B04.23's reading.
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `engine/dice_engine/sigma_leverage.py::net_boost` (`:196`), `::MU_PER_DIE` (`:118`), `engine/tests/test_sigma_leverage_parity.py`. Nothing in this batch (29-1: "Depends on. Nothing").
- GLOSSARY: none (*even line*, *skill score* are rows; the function names are their identifiers).
- COST and TIER: edit; `sonnet` (29-1: "DICE lane · `valoria-author` on `sonnet` · cost: edit").
- LANDS IT: B04's producer; `Item: B04.24`, `[skip ci]`.

### B04.25 — a skill is never lost · `IS-B2-CHAR-04` · POINTER
- SOURCE: `master/instructions/IS_B2_SC_FI_CORE_CHAR_part2.md` `IS-B2-CHAR-04` (ANSWERED, A-106: "no lapse rule and no reserved column is built (no `lapses_by`)"); `IS_B2_SC_FI_CORE_CHAR_part2.md` §5.1's B04 row ("`IS-B2-CHAR-04`'s assumption").
- No work: A-106 is met by B04.02's block, which carries no `lapses_by` column and no loss rule; the item "stays as the record that *lost* in the charge is answered 'never'". Closes G-10.

### B04.26 — the cast's values drafted; the batch's re-pin · `IS-A-11` stage 1 · CONTENT · HASH MOVER (the re-pin)
- SOURCE: `master/instructions/IS_A_NINE_part2.md` `IS-A-11` ("Stage 1, drafting (no code; may start at wave W0 beside the IN spine)"); `V12_STRUCTURE.md` D-19 ("its stage 1 (the five tables) is B04's last item"), D-04 (the re-pin); `IS-A-12` (the `reading:` records); rulings ED-1094 (merge ratifies), A-98.
- ADVANCES: R-06.a, R-08.a, R-09.b through BA1 (stage 2 lands these tables); this commit closes M0 (R-01 to R-03 re-read).
- INSTRUCTION:
  1. "A content lane writes one decision-ready file under the suite's `proposals/` with five tables, each row carrying its basis from the registry (`role`, `faction`, `resonant_style`, `convictions`, `goals`, `notes`, `source`) or marked `[NO BASIS IN THE TREE]`: (a) per cast person, the attributes (`stats:`) and the skills with their skill scores (`capabilities:`), keys from the definition rows B04 lands; (b) per verb, `difficulty:` where it is not `routine` (starting with `interrogate: demanding`, U1-C item 2); (c) the alignment cells of `02_CHAR_choice_alignment` and the pursuit-signature cells of `16_PESSIMIST_CHAR_B`; (d) the six relation rows of `02_CHAR_relations_have_a_ground`; (e) the signature rows and goals of `U5a_CHAR_owed_amendments` §7 and §10. Jordan corrects the tables; merging the batch ratifies them unless the PR body holds one back (ED-1094)." (`IS-A-11` stage 1.) Table (a)'s keys are the seven skills of B04.02 and B04.18 and the ten attributes; it also carries a `manner:` column for `IS-B2-CHAR-07`'s three axes, marked "lands in BA1 after B10" (`IS-B2-CHAR-07` step 5 joins BA1). The file: `proposals/2026-11-12-subsystem-audit-suite/proposals/IS_A_11_cast_values_draft.md` `[ASSUMPTION: `IS-A-11` names "one decision-ready file under the suite's `proposals/`" and no name — basis: the suite's proposal files are named for their subject]`, with a `## Status: PROPOSED` line; it is not under `systems/` and no program reads it (BA1 lands the values into their owners, CLAUDE.md §0.05).
  2. **The re-pin** (the batch's last `Item:` commit; D-04, §5.9): re-record the realm pins in `engine/season/tests/_realm_goldens.py` and every NPC-088 headless hash a test quotes, once, against B03a's close (`reading @<sha>`), after confirming on this tree that the NPC-088 act and Event tallies and `corpus_run --seasons 2` [v12: two seasons a case, D-17; the case's own span, to `MAX_SEASONS`, is B99's] seed 0's tallies equal B03a's close; the commit message says "re-pin: encoding only (`Claim.round` → `Claim.lap`, B04.01; `Person.traits`, B04.07)", and names each pin re-recorded with its old and new value.
  3. **The readings** (`IS-A-12`): write the `reading:` records of R-01, R-02 and R-03's conjuncts in `engine/season/requirements.yaml` from this tree's run; `status:` is not edited.
- WHERE: NEW `proposals/2026-11-12-subsystem-audit-suite/proposals/IS_A_11_cast_values_draft.md`; `engine/season/tests/_realm_goldens.py` (the pins); the test files that quote the NPC-088 hash (`grep -rln 5405522c\|<the B03a NPC-088 hash> engine/season/tests tests/valoria` at the item's open); `engine/season/requirements.yaml` (`reading:` records of R-01 to R-03).
- TESTS: none new; after step 2 every test that reads a pin passes (`python -m pytest $(grep -rl _realm_goldens engine/season/tests) -q`).
- FALSIFIER and CONTROL: for the draft: a table (a) row whose skill key is not a B04 definition row, or a value with no basis cell and no `[NO BASIS IN THE TREE]` mark. For the re-pin: a moved tally (then the batch moved behaviour it did not declare: the re-pin stops and the batch is `STOPPED`). Control: B03a's close readings (`reading @<sha>`).
- GATE: `python -m engine.season.harness.register --requirements` → exit 0, R-01, R-02, R-03 held; the pin tests pass. Record lines, not gate arms (a draft `.md` is reference; counting its sections observes the drafting and no behaviour, CLAUDE.md §0.05; BA1 lands the values where code reads them; repair lane R2a, K2 #12): `grep -c '^### ([a-e])' proposals/2026-11-12-subsystem-audit-suite/proposals/IS_A_11_cast_values_draft.md` → 5; table (a) has one row per cast row of `references/npc_registry.yaml` (46 at `8ce8d6a`; counted by a one-line `yaml.safe_load` in the commit body).
- HASH MOVERS: the batch's re-pin (B04.01's and B04.07's declared encoding movers), recorded here and nowhere else.
- DEPENDS ON: V12 B04.01 to B04.24 (every item before it); V12 Batch B02-tests (`_realm_goldens.py`, `IS-A-01`'s `reading:` record).
- GLOSSARY: none (the draft uses A-98's words: attribute, skill, skill score).
- COST and TIER: content (drafting) and a re-pin; drafting `opus`, `high` ("authorship with competing considerations", `IS-A-11`); the re-pin `sonnet`, `high`.
- LANDS IT: B04's producer (drafting by an `opus` `valoria-author`); `Item: B04.26`, `[skip ci]` (the batch's last `Item:` push is B04.99, which takes steps 2 and 3, the re-pin and the readings, with the GATE's pin-test and `--requirements` arms and HASH MOVERS' re-pin; this commit is the draft; repair lane R1, E-1).

### B04.99 — re-pin and close readings · `V12_STRUCTURE_part4.md` E-1; B04.26 steps 2 and 3, moved · BUILD · HASH MOVER (the re-pin)
- SOURCE: `V12_STRUCTURE_part4.md` E-1 (a drafting item comes before `.99`; the re-pin is a code-and-test commit), E-2; D-04 (the encoding re-pin); B04's RE-PIN and BATCH GATE lines; B04.26 INSTRUCTION steps 2 and 3, moved here by repair lane R1 (part 2 §11 C-01).
- ADVANCES: R-01, R-02, R-03 re-read (M0 closes here, B04's REQUIREMENT line); their conjuncts' `reading:` records written here (`IS-A-12`); no `status:` edited.
- INSTRUCTION: (1) **The re-pin**: B04.26 step 2 as written there (re-record the realm pins in `engine/season/tests/_realm_goldens.py` and every NPC-088 headless hash a test quotes, once, against B03a's close, after confirming the tallies equal; the commit message it gives). (2) **The readings**: B04.26 step 3 as written there (the `reading:` records of R-01, R-02 and R-03's conjuncts from this tree's run). (3) Every BATCH GATE line, the `HASH READING` at `<s>` = 0, 1, 2 (`<k>` = 1) before (`reading @<sha>`) and after, and the batch's measured wall time, into this commit's body. (4) **REM-30, decided here** (the intake `:222`, "HELD, decide at v12 against B04"; part 2 §8 row 6, §11 C-19; repair lane R2a, K2 #6), the record line written into this commit's body: "REM-30: the three spaces are built (`decision/sheet.py`, `fca48e4f`; `proposals/2026-10-07-character-sheet-spaces.md` RATIFIED, ED-IN-0349) and the creation arm stays off (`seat(rows, None, …)`, the shipped state); B04 adds `Person.traits` and the capability home but switches no arm; the arm's open part is the player's sheet, carried by R-04.c1's batches (B34's `creation_sheet` items, B22, B36) — closed here by ladder step 1 (superseded by those carriers), no build. Exit read: `python -m pytest engine/season/tests/test_rem30_character_sheet.py -q` → pass on this commit's tree (the arm-off control reproduces the re-pinned hash)."
- WHERE: `engine/season/tests/_realm_goldens.py` (the pins); the test files that quote the NPC-088 hash (B04.26's WHERE gives the grep); `engine/season/requirements.yaml` (`reading:` records of R-01 to R-03).
- TESTS: none new; after step 1 every test that reads a pin passes (`python -m pytest $(grep -rl _realm_goldens engine/season/tests) -q`).
- FALSIFIER and CONTROL: a moved tally (then the batch moved behaviour it did not declare: the re-pin stops and the batch is `STOPPED`); a pin that moved and that neither B04.01 nor B04.07 declared. Control: B03a's close readings (`reading @<sha>`).
- GATE: the BATCH GATE above, every line, read once on this commit's tree; the pin tests pass; `python -m pytest engine/season/tests/test_rem30_character_sheet.py -q` → pass (REM-30's exit, step 4); `python -m engine.season.harness.register --requirements` → R-01, R-02, R-03 held.
- HASH MOVERS: the batch's one re-pin, here and nowhere else.
- DEPENDS ON: V12 B04.01 to B04.26; V12 Batch B02-tests (`_realm_goldens.py`, `IS-A-01`'s `reading:` record).
- GLOSSARY: none.
- COST and TIER: a re-pin and the readings; `sonnet`, high.
- LANDS IT: B04's producer; `Item: B04.99`, the batch's last `Item:` push (no `[skip ci]`; CI run 1 of the batch).

| STOP. Batch B04-capability-home closes here |
