# Workplan v12 — part 29, continued: B41-go-port-gate from B41.07, and B11F1-flow-se

## Status: PROPOSED (the continuation of part 29's file, `V12_STRUCTURE_part2.md` §4.1: an author whose text passes the cap writes the rest to a `_cont` file; renumbered by the orchestrator; resolves nothing at runtime, CLAUDE.md §0.05; not canon)

## Written against: the working tree at `9c2c3ab` (branch `ccr-62958c70-0kjhsw`), read 2026-11-12; author lane A29. Words, paths and short names as part 29's head states them.

The batch block of `B41-go-port-gate` (its head lines, PORT GATE RULES, UNDECIDED, C, SERIAL EDGES, PARALLEL and the position table) is in the file before this one; its items continue here from `B41.07`.

### B41.07 — the `surface` block · `16_PESSIMIST_GO_surface_pins` §2 · BUILD · HASH EQUAL
- SOURCE: `proposals/16_PESSIMIST_GO_surface_pins.md` "2. GO-08's artifact gains a `surface` block", "Exact edits" rows 3–5, "The falsifier", "Cost class" ("`opus` for the seat-set rule"); closes F-PES-GO-01, F-PES-GO-12 (with B41.05); the plan edit its row 5 asks ("the v12 card for GO-08 … add "the `surface` block (per seed, the declared seats' offer digests)"") is this item.
- ADVANCES: GO "S7 integrated": "the pin now sees what the hash cannot" (78.3 % of the offer moved no pinned value in the source's probe).
- INSTRUCTION (copied; `round` → `lap`, NAMES): "`engine/engine_params/oracle_pins.json`, per seed 0–2, slice 2 (the computed two-season run):
  ```
  "surface": {
    "seats": ["<id>", ...],          # declared in the exporter: the first six named persons by id and the
                                     # first two cohorts by id, so the set is a rule and not a choice
    "rows": [[tick, lap, person, budget, [question ids], rows, digest], ...],
    "content_hash": "<the run's hash; must equal slice 2's>"
  }
  ```
  `tools/export_oracle_pins.py --check` rebuilds it; `port_oracle.py` prints one line per seat. The port's parity job reproduces the block from its own sheet." Exact edits: "`tools/export_oracle_pins.py` … the `surface` block in `--build` and `--check`"; "`engine/season/harness/port_oracle.py` … one printed line per seat". "named persons" are the cast (`w.persons` that are not cohorts, sorted by id); "cohorts" are persons whose id begins `boot/realm.py::COHORT_PREFIX` (B03c moved it from `harness/populated.py`), sorted by id.
- WHERE: `tools/export_oracle_pins.py` (the `surface` block, `--build`, `--check`); `engine/season/harness/port_oracle.py` (one line per seat); `engine/engine_params/oracle_pins.json` (rebuilt by `--build`); `tests/valoria/test_oracle_pins.py`.
- TESTS: in `test_oracle_pins.py`, written before the block and read red: `test_the_surface_block_content_hash_equals_slice_two`, `test_the_surface_seats_are_the_declared_rule` `[ASSUMPTION: names; the first is the falsifier's clause]`.
- FALSIFIER and CONTROL: "A `surface` block whose `content_hash` differs from slice 2's (the trace moved the run)." Control: slices 1 and 2 of B41.06 unchanged by the rebuild.
- GATE: `python tools/export_oracle_pins.py --build` then `--check` → OK; `python -m pytest tests/valoria/test_oracle_pins.py engine/season/tests/test_surface_trace.py -q` → pass; `python -m engine.season.harness.port_oracle --slice 2 --seed 0` → one line per declared seat.
- HASH MOVERS: none (a pin of a run, no game state; the `--build` is this item's own, PORT GATE RULES 1).
- DEPENDS ON: V12 B41.05 (`surface_trace`), B41.06 (the exporter); V12 Batch B03c (`boot/realm.py::COHORT_PREFIX`).
- GLOSSARY: none.
- NAMES: `harness/populated.py::COHORT_PREFIX` → `boot/realm.py::COHORT_PREFIX` (B03c, CI-07); `round` → `lap` in the row (B04).
- COST and TIER: small build; `sonnet`, `high`; the seat-set rule read by `opus`.
- LANDS IT: B41's producer; `Item: B41.07`, `[skip ci]`.

### B41.08 — each module pinned at its own entry · `11_GO_port_gate_order_and_coverage` §3 · BUILD · HASH EQUAL
- SOURCE: `proposals/11_GO_port_gate_order_and_coverage.md` "3. Module-scene pins" (the block, the twelve names, the builders, the mass-battle table and its paragraph), "The gate" 2, "The falsifier", "Build order" (2)–(3); `IS-B3-GO-05` (2) ("The twelve `module_scenes` scenario names of §3 (`duel_even` … `finding_full`) are keys of `SCENARIOS`, so the fixture worlds have one owner"); `IS-B3-GO-01` (3) (B11.05: "the `scenario:` names of the port gate's `module_scenes` block … Neither holds a list of its own"); A-1, `ED-IN-0285`, A-3, A-4; closes F-GO-04, F-GO-06, the mass-battle part of F-GO-08.
- ADVANCES: GO "S7 integrated": "a port wrong about a duel or a battle is shown wrong" (slice 2 enters `combat.fight` 0, 2 and 4 times and a fought field 0, 0 and 1 times at seeds 0, 1, 2).
- INSTRUCTION (copied; `harness/populated.py` → `boot/realm.py`, "subunits" → units, NAMES): "For each `composition_roles:` row of `references/module_contracts.yaml` that resolves by a draw (`combat.fight`, `mass_battle.resolve_field`, the social-contest role, `fieldwork.find`), `tools/export_oracle_pins.py` adds a `module_scenes` block:
  ```
  module_scenes:
    - role: combat.fight
      scenario: <name>                 # a fixture world from which the SEAM builds the input (never a hand-built input)
      input:  <the typed input the seam built, in the GO-07 encoding>
      key:    <the Draw key>
      outcome: <the typed outcome, GO-07 encoding>
      trace_digest: <blake2b of the module's own per-step trace, where it returns one>
  ```
  At least: three duels (an even match, a mismatch, one that ends by yield), three fields (line against line; an envelopment; a rout cascade), three contested speech acts, three graded findings. Scenario names, one per entry, in the block's `scenario:` field: `duel_even`, `duel_mismatch`, `duel_yield`; `field_line`, `field_envelop`, `field_rout_cascade` (the one with units, below); `speech_even`, `speech_mismatch`, `speech_refused`; `finding_none`, `finding_partial`, `finding_full`. The scenario worlds are built by the same builders the corpus uses (`boot/realm.py`, `headless.py`), and the input is produced by the seam wrapper (`seam/wrappers/combat.py::combat_input`, `mass_battle.py`'s input builder), so the pin tests **the loop's code path**, not a parallel one." The social-contest role is `social_contest.roll` and the mass-battle input builder `seam/wrappers/mass_battle.py::field_input` (both read at `9c2c3ab`).
  `IS-B3-GO-05` (2): each of the twelve is registered as a row of `harness/scenarios.py::SCENARIOS` (B11.05's `Scenario`: `build`, `verbs`, `seat`, `ending`, `role`, `kinds`, `unreached`), with `role` the composition role it enters; the block's `scenario:` is the row's key, and no list of names is kept in the exporter.
  The mass-battle paragraph, copied in part: "Auto-resolve and the played battle are then one call with and without the decider, which is what keeps them consistent, and the module-scene pin covers both: the automated outcome, and a played run whose decider returns the default orders reproducing it." "Whether the order of battle carries units ["subunits" in the source, corrected by the MB lexicon] is MB's; the pin's three field scenarios must include one that does, or the trace has nothing in it for a port to get wrong" (`field_rout_cascade`, an army of several units). The decider arm `IF` `04_MB_manager_battle_one_resolver.md` §4's decider is on this batch's base (B20 merged; UNDECIDED 1): each field entry gains the played run with the default-orders decider, asserted equal to the automated outcome; otherwise the commit body says the arm waits on B20 and the batch that merges after B20 adds it with a `--build`. `trace_digest` is read where the module returns a per-step trace (the field's `FieldOutcome.report` from B17, 27C-1 in B19); where none, the key is omitted, not null.
- WHERE: `tools/export_oracle_pins.py` (`module_scenes`); `engine/season/harness/scenarios.py` (twelve `SCENARIOS` rows); `engine/engine_params/oracle_pins.json`; `tests/valoria/test_oracle_pins.py`.
- TESTS: "`tests/valoria/test_oracle_pins.py::test_each_module_scene_reproduces_from_its_key`, red before the block exists": "each scene's `key` re-seeds `draw.seeded(key)` and reproduces its `outcome`"; `engine/season/tests/test_scenarios_runner.py`'s `test_every_ending_name_a_reader_can_return_has_a_kind` and `test_a_role_declared_unreached_reads_zero` (B11.05) cover the twelve new rows.
- FALSIFIER and CONTROL: "Changing a module's entry so that the seam builds a different input reds that scene's pin while slices 1 and 2 stay green, which is the case the season-shaped slices cannot see." Control: slices 1 and 2 unchanged by the rebuild; the realm hash at seed 0 equal to B41.07's.
- GATE: `python tools/export_oracle_pins.py --build` then `--check` → OK "with a `module_scenes` block of the twelve named entries"; `python -m pytest tests/valoria/test_oracle_pins.py engine/season/tests/test_scenarios_runner.py -q` → pass.
- HASH MOVERS: none ("the pins re-read the run").
- DEPENDS ON: V12 B41.06; V12 B11.05 (`SCENARIOS`, `Scenario`); V12 Batch B06 (`draw.seeded`); V12 Batch B16M (L2: the engine's `Unit` is the army, `Subunit` → `Unit`); V12 Batch B17 (`04_MB_typed_outcome_and_one_path` §3, the field's typed outcome; not in §2.1's after-list, closed by S9: UNDECIDED 1); V12 Batch B20 (the decider; conditional, above); EXISTS-IN-TREE `references/module_contracts.yaml` `composition_roles:` (`combat.fight`, `mass_battle.resolve_field`, `social_contest.roll`, `fieldwork.find`), `seam/wrappers/mass_battle.py::field_input`, `seam/wrappers/combat.py::combat_input` (located by symbol).
- GLOSSARY: none (*scenario* is B11.05's row).
- NAMES: `harness/populated.py` → `boot/realm.py` (B03c); "subunits" → units, `Subunit` → `Unit` (B16M, L2).
- COST and TIER: small build per module; `sonnet`, `high`; MB reviews the field scenes, PC the duels (the source's "Lands it").
- LANDS IT: B41's producer; `Item: B41.08`, `[skip ci]`.

### B41.09 — the halt roster and its planted worlds · `11_GO_port_gate_order_and_coverage` §4 · BUILD · HASH EQUAL
- SOURCE: `proposals/11_GO_port_gate_order_and_coverage.md` "4. Halts and refusals" (the second bullet), "The gate" 3, "The falsifier"; U3 §1.4 row 151 ("a new `raise` on a port-reached path needs a `where` tag", `U5b_PC_residue.md` §4); closes F-GO-05 with B41.03.
- ADVANCES: GO "S7 integrated": the mechanism at its extreme (a halt) is pinned.
- INSTRUCTION (copied): "`oracle_pins.json` gains `halts`: the closed roster of `where` tags reachable in the loop (derived by the exporter from the `raise` sites, never typed by hand), and a handful of planted worlds each pinned to the tag it halts on. The port's parity job asserts it stops at the same tag." "The `raise` sites are counted by `grep -rE '^\s*raise ' engine/season` outside `tests/`, `harness/`, `data/` and `manifest/`; re-run it rather than quoting a figure." At the tree: the exporter derives the roster by walking those modules' source with `ast` (the `where` argument of each `ShapeGap`-family raise), not by a regular expression over text, and records the grep's count beside it in the commit body; "a handful" is three planted worlds `[ASSUMPTION: three — basis: the source's "a handful"; one per defect family the roster's largest three tags name]`, each built in the exporter from `boot/realm.py` with one planted defect.
- WHERE: `tools/export_oracle_pins.py` (`halts`); `engine/engine_params/oracle_pins.json`; `tests/valoria/test_oracle_pins.py`.
- TESTS: in `test_oracle_pins.py`, written before the block and read red: `test_a_planted_defect_world_halts_with_its_pinned_where_tag` (gate 3), `test_a_new_raise_with_a_new_where_tag_reds_check_until_rebuilt` (the falsifier, on a temporary copy of one module) `[ASSUMPTION: names]`.
- FALSIFIER and CONTROL: "A `raise` added on the loop path with a new `where` tag reds `--check` until the roster is rebuilt." Gate 3's other half, "a planted no-op write still yields its refusal Event (GO-10's own falsifier)", is B41.03's test, re-run here. Control: the other blocks unchanged by the rebuild.
- GATE: `python tools/export_oracle_pins.py --build` then `--check` → OK with a `halts` block; `python -m pytest tests/valoria/test_oracle_pins.py engine/season/tests/test_go10_refusal_values.py -q` → pass.
- HASH MOVERS: none.
- DEPENDS ON: V12 B41.03 (the defect shape and `where`), B41.06, B41.08; EXISTS-IN-TREE `engine/season/gaps.py::ShapeGap`.
- GLOSSARY: none (*halt* is B41.03's row).
- COST and TIER: small build; `sonnet`, `high`; the roster's derivation `opus` ("`opus` for the halt roster's derivation").
- LANDS IT: B41's producer; `Item: B41.09`, `[skip ci]`.

### B41.10 — the scenario worlds are pinned · `IS-B3-GO-05` · BUILD · HASH EQUAL
- SOURCE: `master/instructions/IS_B3_FA_SE_WR_GO_part2.md` "Item: IS-B3-GO-05" (`:198-207`); A-114 (UNDECIDED 5); closes H-02's port half ("the port plays them without porting a builder").
- ADVANCES: GO "S7 integrated"; "the standing requirement on the port's side".
- INSTRUCTION (copied; "or 8" written "or 2"): "(1) `tools/export_oracle_pins.py` gains a `scenarios` block: for each `SCENARIOS` row and seeds 0 to 2, `initial` (the snapshot of the world `build` returns, in `U5d_GO_owed_edits.md` §1's format with `IS-B3-GO-03`'s key), `seasons` (a count declared on the block, the smallest at which the unwatched run reaches an ending, or 2), `content_hash` of the unwatched run, and `ending` (its name and kind). (2) [B41.08.] (3) `--check` rebuilds the block. A batch that lands or changes a row re-runs `--build` in its own commit and says so (the proposal's rule for behaviour pins; no ledger row)." The source's `[ASSUMPTION: GO-08's artifact can hold a world in the GO-07 encoding]` is confirmed: GO-08's entry lists "the initial world in GO-07's encoding" (B41.06). A row that has not ended by season 2 is pinned with `ending: null` (UNDECIDED 5).
- WHERE: `tools/export_oracle_pins.py` (`scenarios`); `engine/engine_params/oracle_pins.json`; `tests/valoria/test_oracle_pins.py`.
- TESTS: "`test_each_scenario_pin_decodes_to_its_initial_hash_and_replays_to_its_ending` (red before the block exists)".
- FALSIFIER and CONTROL: "Editing one row's builder without a re-export reds `--check`. Control: slices 1 and 2 stay green under that edit, which is the case the season-shaped slices cannot see."
- GATE: "`python tools/export_oracle_pins.py --check` OK with a `scenarios` block of every row landed by B41"; `python -m pytest tests/valoria/test_oracle_pins.py -q` → pass.
- HASH MOVERS: "None."
- DEPENDS ON: V12 B41.08 ("after the `module_scenes` block"); V12 B11.05 (`IS-B2-CORE-01`, `IS-B3-GO-01`); V12 Batch B34 (`IS-B3-GO-03`, the snapshot's `scenario` key and `scenarios.resume`); V12 Batch B06 (`U5d_GO_owed_edits` §1, `decode`).
- GLOSSARY: none.
- COST and TIER: small build; `sonnet`, `high` ("small build · `sonnet` · the B41 session").
- LANDS IT: B41's producer; `Item: B41.10`, `[skip ci]`.

### B41.11 — words for every verb and Event kind · `16_PESSIMIST_GO_surface_pins` §3 · CONTENT · HASH EQUAL
- SOURCE: `proposals/16_PESSIMIST_GO_surface_pins.md` "3. A vocabulary block behind the names exporter", "Exact edits" row 6, "The gate" 3; `unified/U4_DOCUMENT_STATUS.md:206` ("CONTENT | about 150 display strings (line 101) | Jordan, or authored under his review"); `V12_STRUCTURE_part2.md` §5.7 (CONTENT → a drafting item, D-19); closes F-PES-GO-09 (in part).
- ADVANCES: GO "S7 integrated": the port reads the game's vocabulary from one owner instead of writing it.
- INSTRUCTION (copied): "`references/names_index.yaml` gains two classes, `verb` and `event_kind`, each entry a key and a display string. `tools/export_names.py --check` gains one rule: every key of `verb_table.yaml`'s `verbs:` and every member of the derived Event-kind roster (`04_CODE_ARCHITECTURE.md:500`, loader invariant 7: "the Event-kind roster is **derived** from every emission column") has an entry, and no entry names a key that is in neither. This is the exporter's own round-trip for its own chain (§0.05's licensed form), not a tree-wide guard. The strings are authored once, by Jordan or under his review, in the YAML; the port reads `names.json`. The key sets are derivable now: `python -c "from engine.season.data.verbs import VERB_TABLE; print(sorted(VERB_TABLE))"` (the verb keys) and the derived Event-kind roster of loader inv. 7 (the `event_kind` keys) are what `--check` will require." "(the `--check` rule ships with the strings, or reds)."
  At the tree (D-19: drafted here, ratified at the batch's merge): (1) the two key sets read on this batch's base (the derived roster is `data/verbs.py::EMITTED_KINDS`, from `_derive_kind_verb()`) and their counts quoted; (2) one entry per key, in the key form of UNDECIDED 4, each display string a plain-English phrase drafted from the verb row's own `gloss`/note or the Event kind's emitting row, marked `[ASSUMPTION; drafted for Jordan's correction]` in a block comment over each class; (3) the completeness rule in `tools/export_names.py`, landing in the same commit as the strings; (4) `engine/engine_params/names.json` re-derived with the tool. The PR body lists the class counts and says the strings are drafted for Jordan's correction (`V12_STRUCTURE_part3.md` §8.2, "every authored value").
  A rule from this commit on, for every later batch (named for the head's rules, H1): a commit that adds a verb row to `verb_table.yaml` or a new emitted Event kind adds its `names_index.yaml` entry in the same commit, or `export_names.py --check` reds.
- WHERE: `references/names_index.yaml` (two classes; the prefix table's comment); `tools/export_names.py` (the completeness rule); `engine/engine_params/names.json` (re-derived); `tests/valoria/test_export_names.py` or the existing test of the exporter (located by `grep -rl export_names tests`) `[ASSUMPTION: the existing test file is extended; if none, NEW `tests/valoria/test_names_vocabulary.py`]`.
- TESTS: `test_a_verb_row_with_no_entry_reds_check_and_its_entry_clears_it` (gate 3), `test_an_entry_naming_no_verb_or_kind_reds_check` `[ASSUMPTION: names]`, written before step 3 and read red.
- FALSIFIER and CONTROL: "A verb or Event kind with no word that `--check` passes." Gate 3: "`python tools/export_names.py --check` reds when one verb row is added to `verb_table.yaml` with no entry, and passes when the entry is added." Control: `tools/ci_naming_check.py` and `tools/ci_names_consistency.py` exit 0 (no new entry's `legacy:` names a live word).
- GATE: `python tools/export_names.py --check` → OK; `python tools/ci_naming_check.py` → exit 0; `python tools/ci_names_consistency.py` → exit 0; the tests above → pass.
- HASH MOVERS: none (`names.json` is read at import by `engine/substrate/names.py` for name resolution; no new entry is an alias of an existing canonical, which the exporter refuses).
- DEPENDS ON: V12 B41.06 (the batch's exporter work precedes; no data edge); EXISTS-IN-TREE `references/names_index.yaml` (`entries:`, the prefix table), `tools/export_names.py`, `data/verbs.py::VERB_TABLE`, `::EMITTED_KINDS`.
- GLOSSARY: none (display strings are the names index's, not the suite's glossary).
- COST and TIER: content and a small rule; drafting `opus`, `high`; the rule `sonnet`, `high`.
- LANDS IT: B41's producer; `Item: B41.11`, `[skip ci]`.

### B41.12 — no module reads the process environment · `11_GO_port_gate_order_and_coverage` §5, gate 1 · READING
(no item body: the reading is Reading 1 below; it is a line of the batch gate.)

### B41.13 — the contract freeze row · GO-15a · BUILD · HASH EQUAL
- SOURCE: `E1` §Carry-forward GO-15 (`:3480-3502`; v11 `_part5.md:72-84`), as `proposals/11_GO_port_gate_order_and_coverage.md` §1 amends it ("`GO-15a` CONTRACT FREEZE (the `ED-GO-` row; needs every contract item)"; "The freeze row keeps the oracle SHA and the digests and **drops the freeze list**"); `master/eval/E1.md:207` (GO-15a: "the freeze list is dropped"); A-30 (no draw-log digest); PORT GATE RULES 1; closes GO-15a.
- ADVANCES: GO "S7 integrated": the port has one recorded commit to build against.
- INSTRUCTION: append one row to `registers/editorial_ledger_go.jsonl`, id `ED-GO-<B41 block slot 1>` (B00's block for this batch, `references/id_reservations.yaml`), keys as the file's last row (`id`, `date`, `system`, `status`, `needs_jordan`, `confidence`, `supersedes_row`, `superseded_by`, `description`, `citations`, `source`), `status: "resolved"`, `needs_jordan: false`; its `description` records "the oracle SHA, the pins artifact's digest" (of `engine/engine_params/oracle_pins.json`, `blake2b`-128 over its bytes) "[, the draw log's digest: struck, A-30]" and the contract as PORT GATE RULES 1 lists it, each item with the owner that now holds it (`state/world.py::canonical`; `state/ids.py::H`; the integer contract vectors; `engine/dice_engine/draw.py`; `engine/dice_engine/fmath.py`; `season_registries.json`'s schema; `gaps.py::REFUSAL_CODES` and the `halts` roster; the pins' format), and the rule "a change to any of these writes an `ED-GO-` row; a behaviour mover re-runs `--build` in its own commit and says so; no ledger row". No freeze list.
- WHERE: `registers/editorial_ledger_go.jsonl` (one row).
- TESTS: none new.
- FALSIFIER and CONTROL: a row naming a contract item with no owner in the tree; a freeze list in the row. Control: `validate_ed_citations.py` exit 0 before and after.
- GATE: `python tools/validate_ed_citations.py` → 0 violations, and the last `ED-GO-` row is this one (exit line 7); `python tools/export_oracle_pins.py --check` → OK on this commit.
- HASH MOVERS: none ("EQUAL").
- DEPENDS ON: V12 B41.02 to B41.12 ("needs every contract item"); V12 Batch B00 (the `ED-GO` block); V12 Batch B06 (draw type, float contract); V12 Batch B03g (GO-09's registry schema).
- GLOSSARY: none (*contract* is B41.06's row).
- IDS: ED-GO block slot 1.
- COST and TIER: edit; `opus`, `high` ("third tier (judgment)": which items are contract).
- LANDS IT: B41's producer; `Item: B41.13`, `[skip ci]`.

### B41.14 — the first behaviour pin and the exit lines · GO-15b · BUILD · HASH EQUAL
- SOURCE: `E1` §Carry-forward GO-15 ("EXIT and FALSIFIER": "GO-08's `--check` on the freeze commit; each of B10-20's exit lines … prints"), as `11_GO_port_gate_order_and_coverage.md` §1 amends it ("`GO-15b` FIRST BEHAVIOUR PIN (a `--build` and the card's exit lines; repeatable, no row)") and "The gate" 4; B10-20's exit lines, copied from `workplans/valoria_master_workplan_v11_part3.md` B10-20 "Exit" (read at `9c2c3ab`; the file is deleted at v12's adoption, so the lines live here); `U5d_GO_owed_edits.md` §3; UNDECIDED 6; closes GO-15b and GO-15.
- ADVANCES: GO "S7 integrated".
- INSTRUCTION: run `python tools/export_oracle_pins.py --build` on the tree after B41.13, commit the artifact, and read each exit line, quoting its output in the commit body (a line that does not print keeps the batch open: "a line that does not keeps B10-20 open"):
  (1) "`game_constants.json`'s `engine_series`" equals `references/engine_series.yaml`'s value (GO-01, B03g; `ED-GO-0002` owns the value, which this plan does not write);
  (2) "`python tools/export_oracle_pins.py --check` OK with the oracle SHA equal to `git rev-parse HEAD`";
  (3) "`port_oracle --slice 1 --seed 0` under `PYTHONHASHSEED` 0, 1 and 2 prints three identical lines equal to the pin";
  (4) "the seven existing `--check`s (`export_sim_params`, `export_engine_params`, `export_game_constants`, `export_descriptors`, `export_composition`, `export_npc_roster`, `export_names`) and `export_season_registries --check` … print OK", with every other exporter the `validators` job runs at this tree (`grep -n -- "--check" .github/workflows/valoria-ci.yml`: `export_troops`, `export_mb_contact` and their kin from B17, B19a); [`export_oracle_draws --check`: struck, A-30]; and `export_npc_roster --check` named apart: "reports hand-corrected rows; fails only on a row naming no case, place or seated person" (`U5d_GO_owed_edits.md` §3);
  (5) "`python tools/m1_acceptance.py --summary` prints its same-seed hash row and its zero-invariant-violation row PASS";
  (6) "`grep -c "key-log" references/module_contracts.yaml` prints `0`";
  (7) "`python tools/validate_ed_citations.py` 0 violations, and the last `ED-GO-` row is the freeze row";
  (8) "the three pytest gates once at the close, CI green on the freeze commit": the batch close's one suite run and CI's runs (the skill, CHECKPOINTS);
  (9) "Jordan's side, not checkable here: `valoria-game`'s CI prints" a build at the series `ED-GO-0002` rules "and its parity job reads `oracle_pins.json`" [and replays `oracle_draws.json`: struck, A-30; the port implements the keyed draw]. Line (9) is quoted as not checkable, never as passed.
  "OPEN lines, listed in the row: an exit line whose Layer 0/1 hunk or deletion did not land in its own position's PR (a (RULED) mark stopped it) stays OPEN; it does not block the freeze or the port": a line stopped so is named in the commit body.
- WHERE: `engine/engine_params/oracle_pins.json` (`--build`).
- TESTS: none new.
- FALSIFIER and CONTROL: "CONTROL: GO-08's `--check` under two hash seeds" (`PYTHONHASHSEED` 0 and 1).
- GATE: lines (1) to (8) print as stated; `PYTHONHASHSEED=1 python tools/export_oracle_pins.py --check` → OK.
- HASH MOVERS: none ("EQUAL").
- DEPENDS ON: V12 B41.13; V12 Batch B03g (GO-01's `engine_series.yaml`, GO-11, GO-05, GO-09); EXISTS-IN-TREE every exporter line (4) names.
- GLOSSARY: none.
- COST and TIER: reading and one build; `sonnet`, `high`; the OPEN-line judgment `opus`.
- LANDS IT: B41's producer; `Item: B41.14`, `[skip ci]`.

## Readings (B41)

**Reading 1 (B41.12), copied from `proposals/11_GO_port_gate_order_and_coverage.md` "The gate" 1 and §5:** "`grep -rn "os.environ" modules --include=*.py` (tests excluded) prints nothing; the realm hash at seeds 0–2, two seasons, is equal before and after; `CASUALTY_SCALE=9 python -m … port_oracle` prints the same line as with the variable unset." "The build is `04_MB_typed_outcome_and_one_path.md` §3's (B17, MB); this file adds none of it and, in B41, only checks it (gate 1)." Read at the close: the `grep` (its output, empty, quoted); `CASUALTY_SCALE=9 python -m engine.season.harness.port_oracle --slice 2 --seed 2` against the same command unset (seed 2: the one seed whose slice 2 fights a field, the source's "0, 0 and 1 fought field at seeds 0, 1, 2"). STOPS IF B17 is not on the base (UNDECIDED 1): then the reading is `STOPPED` with the grep's count, never written as passed.

### B41.99 — re-pin and close readings: the EQUAL readings recorded · `V12_STRUCTURE_part4.md` E-1 · BUILD · HASH EQUAL
- SOURCE: `V12_STRUCTURE_part4.md` E-1, E-2; `V12_STRUCTURE_part2.md` §5.12; PORT GATE RULES 1.
- ADVANCES: the close's record.
- INSTRUCTION: (1) record the realm content hash at seeds 0, 1, 2 (one season) equal to the baseline named in the BATCH GATE, re-pinning nothing; (2) if a hash-moving batch of S15 merged before this one, re-run `python tools/export_oracle_pins.py --build` on the rebased tree and commit the artifact, saying so (PORT GATE RULES 1); (3) the BATCH GATE's readings and the wall time in the commit body.
- WHERE: `engine/engine_params/oracle_pins.json` (only under (2)).
- TESTS: none new.
- FALSIFIER and CONTROL: a realm hash that moved (every item was declared EQUAL).
- GATE: the BATCH GATE.
- HASH MOVERS: none.
- DEPENDS ON: V12 B41.01 to B41.14.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B41's producer; `Item: B41.99`, the batch's last commit (no `[skip ci]`).

| STOP. Batch B41-go-port-gate closes here |

---

## Batch B11F1-flow-se · lane SE · wave W16 · step S16 · HASH MOVER, one re-pin
INVOCATION: /methodology-execute Batch B11F1-flow-se
IN-FLIGHT ROW: registers/handoffs/HANDOFF_SE.md, Open table
GATE: Batch B12c-material-verbs-and-valley
HASH READING: `PYTHONHASHSEED=0 python -c "import sys; from engine.season.boot.realm import build_realm; from engine.season.harness.populated import run; s, k = int(sys.argv[1]), int(sys.argv[2]); w = build_realm(s); run(k, s, w=w); print(w.content_hash())" <s> <k>` → the realm content hash at seed `<s>` after `<k>` seasons: `<k>` = 1, one season, unless the gate names two (never more before B99, D-17); `<k>` = 0 reads the build hash; per item `<s>` = 0 (a mover's reading, E-2), at `.99` `<s>` = 0, 1, 2; each value quoted `reading @<sha>`, the tree it was read on (`workplan_v12.md` §3.B, "the hash reading").
REQUIREMENT: none of its own — carried v11 positions (Jordan's settlement rules of 2026-11-08, `ED-IN-0352` items (6) and (7); v11 part 16 §3, RATIFIED "ratify all and merge", every content cell `[ASSUMPTION; medium; Jordan to correct]`). It serves B11F2 (CR-104's owned-site term reads the Sites CR-106 mints), B38 (`31_WR_B_the_revival_gathers` commit 2 and `U5d_SE_cohort_heavy_moves_and_caste` need several cohorts a settlement: `master/V11_EVALUATION_part2.md:179`) and B39. The close re-reads R-01 and R-02 (the realm builds and runs with the new Sites and cohorts) and states their readings beside B12c's (`reading @<sha>`); no `status:` is edited
BATCH GATE (read once, on the closing tree; `PYTHONHASHSEED=0` on every seeded command):
  `python -m pytest engine/season/tests/test_cr106_church_sites.py engine/season/tests/test_cr107_cohort_identity.py engine/season/tests/test_governance_build.py engine/season/tests/test_migrate_capacity.py -q` → all pass;
  `python proposals/2026-11-08-flow-conditioning/content_validate.py` → exit 0 (the content draft's own validator, re-run against the transcribed rows);
  `python -m engine.season.harness.aperture 2 0` → no verb's `executed` count falls to 0 that was above 0 at B12c's close (`reading @<sha>`); `migrate`'s executed count quoted before and after (CR-107's stated consequence: every two-cohort village is at capacity);
  the realm content hash of `build_realm(s)` after one season at s = 0, 1, 2 → moved by the three content items only (B11F1.02, B11F1.04, B11F1.05), each value recorded by the re-pin; with no venue row carrying `site:`, the shipped `cohorts.yaml` and no `engages:` change (the controls) equal to B12c's close (or the after-reading of the mover merged before this batch in S16);
  `python -m engine.season.harness.register --check` → each check's violation count (R2, G6 and any other that reports) does not rise from the reading taken at the batch's opening (quote both, `reading @<sha>`); `--requirements` → nine lines; `python tools/m1_acceptance.py --summary` → its verdict line quoted; `python tools/export_descriptors.py --check` → OK (the `engages:` cell); `python tools/ci_sim_fabrication_check.py` → exit 0;
  the suites `python tools/tests_for_diff.py --base <batch-start-sha>` names;
  the glossary rows each item names, read against the code it landed: a mismatch fails the close;
  the close's commit body records `register --requirements` (nine lines), `m1_acceptance --summary`'s verdict line, the named conjuncts' readings with their tree, the `BUILT OUT`, `ENGINES` and `NULL SCENES` lines before (`reading @<sha>`) and after, and the batch's measured wall time; the last `Item:` commit writes the conjuncts' `reading:` records; `status:` is not edited (`IS-A-12`).
RE-PIN: once, in B11F1.99: the realm pins in `engine/season/tests/_realm_goldens.py` and `engine/season/runs/results.json` (by `harness/report.py`), and every test-local pin two items move, read against B12c's close (`reading @<sha>`): §2.1's row order puts B11F1 before B20, B25, B27 and B37, so B11F1 merges first among S16's movers and the others rebase on it (`V12_STRUCTURE_part3.md` §7.4). The commit says "re-pin: content (CR-106's Church Sites, CR-107's cohort rows, the Schoenland `engages:` cell)". The new Sites and cohorts are new entities in hashed collections, not a field of a carrier: no encoding mover (D-04).
EXPECTED RED UNTIL B11F1.99 (under `[skip ci]`, E-1; one batch line, repair lane R1): the realm and corpus pins any mover item of this batch moves read red from its first mover (B11F1.02) to the re-pin; the files that pin them (`git grep -lE '"[0-9a-f]{32}"'` over the test trees and the golden files, those this batch names): `engine/season/tests/_realm_goldens.py` (B02's one pin file); `engine/season/tests/test_go07_canonical_digest.py` (its asserting test, `SHIPPED`/`CENSUS`).
IDS: ED-SE 0; H 2 (B11F1.01 1: "kind `RULING`, grade `assumption`: the three names, the null-cell rule and the first-reading rows"; B11F1.03 1: "kind `RULING`, grade `assumption`) for the summed-ceiling reading")
DIALS AT CONTROL: `wear_per_season` = 0 for `worship`, `templar_quarters`, `school` ("`wear_per_season` 0 ships as the control arm, as `dwelling` did"); set by: no batch names a setting reading (CR-106 gives no target), so `BLOCKED (design: no target reading)` in B98 (D-22); every other content cell is Jordan's to correct (D-19), not a dial.
UNDECIDED (each taken as the reading that changes less; the orchestrator may reverse it):
  1. **The territory caps.** v11 part 16's head (item 6) reads "Territory caps on developments and their sizes: RATIFIED as out of scope, no position (§3.4)" under Jordan's "ratify all and merge"; the evaluation carries the row STILL-NEEDED ("design-first, post-F1; UNVERIFIED whether any suite file covers it", the intake `:331`). Searched here: `07_SE_ground_and_granaries.md` R1 keys a territory's endowment (what it yields: `T5: [field, field] # breadbasket`) on the geography territory code, which is the cap's key but not a cap on what may be built. Taken: one DESIGN-FIRST item (B11F1.06), no build (no source writes build text; `STAGES.md`: v12 takes no item without a coding instruction). Other reading: no item, the v11 ruling standing.
  2. **The Schoenland `engages:` cell.** `E1`'s copy of CR-107 says it is "recorded here and left for the owner of that registry, not made"; v11 part 16's head item 4, later and ratified, says "RATIFIED as part of CR-107 … made at CR-107's build". Taken: the head (B11F1.05).
  3. **CR-106's control test.** The entry names "the control-arm identity `test_24d_i_...moves_no_question_in_one_season`"; at `9c2c3ab` the `test_24d_i_*` family is `engine/season/tests/test_governance_build.py:2559-2639` and no test there ends `moves_no_question_in_one_season`. Taken: B11F1.02 re-reads the four `test_24d_i_*` tests and `test_migrate_capacity.py`'s `test_24d_ii_*` with the Church Sites present and states each result; the named test is `MISSING (SE: renamed or never landed)`.
C(B11F1-flow-se): this batch's entries; the plan's head parts; `unified/U1_GLOSSARY.md` rows *site*, *owner*, *cohort*, *heritage*, *conviction*, *capacity*;
  `engine/season/rosters.yaml` (`site_kinds`, `wear_per_season`, `capacity_floor`, `works_cost`, `band_floors`, the new `site_owner`); `engine/season/data/rosters.py` (`HEAD_SEAT`, `require_member`); `engine/season/data/fixtures.py` (the kind tables' loader checks); `engine/season/venues.yaml`; `engine/season/cohorts.yaml`; `engine/season/boot/realm.py` (B03c: `build_realm`, `seat_cohorts`, the cohort loader, the dwelling loop, `COHORT_PREFIX`); `engine/season/queries/faction_q.py`; `engine/season/queries/world_q.py` (`holder_faction_of`, `capacity`, `population`, `has_room`, `commensurate`); `engine/season/loop/witness.py` (`_credit`); `engine/season/data/affiliations.py` (`conviction_map`, read only); `references/descriptor_registry.yaml` (`heritage_roster.engages`); `tools/export_descriptors.py`; `engine/season/hole_register.yaml`;
  read whole by B11F1.02 and B11F1.04: `proposals/2026-11-08-flow-conditioning/content_church_sites.yaml`, `content_cohorts.yaml`, `content_provenance.md` (tables A and B), `content_validate.py`;
  the tests named in the items; instruments `aperture`, `register`, `report`, `tools/m1_acceptance.py`, `tools/tests_for_diff.py`; `engine/season/tests/_realm_goldens.py` (B02);
  the closing SHA of B12c; the permanent surface.
SERIAL EDGES: within the batch: B11F1.01 → B11F1.02 (the content rows need the kinds, the table and the `site:` key) ; B11F1.03 → B11F1.04 (the cohort rows need the new keys and the summed ceiling) → B11F1.05 (the Schoenland cohort row is what the cell reaches); B11F1.06 has no edge (a design); B11F1.07 (HELD) none; → B11F1.99. CR-106 and CR-107 are "independent" (v11 part 16 §3.2), so B11F1.01–.02 and .03–.05 commute; the source's order (CR-106 first) is kept.
  With other batches, by file: `engine/season/rosters.yaml` and `boot/realm.py` (hot, `V12_STRUCTURE_part3.md` §7.3): in S16 with B20, B25, B27, B37, kept to different keys and functions, merged in §2.1's row order (B11F1 first); `queries/faction_q.py`: B21b → B21d → B11F1 (`owner_of` beside `civil_war`); `engine/season/venues.yaml`, `engine/season/cohorts.yaml`: B11F1 only among the batches this lane read (U3 §5.1 lists neither); `references/descriptor_registry.yaml`: B04 → B19 → B11F1 → B38.
PARALLEL: S16 with B20 (MB), B25 (FI), B27 (SC), B37 (IN). Shared: `rosters.yaml`, `boot/realm.py`, `queries/world_q.py` (read only here) — checked by the coordinator from H2's census at the step's open. B11F1 merges first among S16's movers.
COST: builds and content transcription; producer `valoria-author` on `sonnet`, `high` ("second tier for the rows and loader"); a third-tier critic (`opus`) on CR-106's null-cell rule; CR-107's content pass "a separate judgment lane" (`opus`); B11F1.06's design `opus` with a `ners` critic; the close's terminal critique `opus`.
EST: 5.7 h [estimate: `V12_STRUCTURE.md` §2.4's formula over 8 positions (0.4 h × 8 + 2.5 h); §2.2's 4 h counted three entries]

| pos | item | source | state | hash | gates on |
|---|---|---|---|---|---|
| B11F1.01 | the Church's buildings: three kinds, an owner table, one owner of ownership, a `site:` key | CR-106 (a)–(d) | BUILD | EQUAL | Batch B12c |
| B11F1.02 | the Church's buildings placed in every settlement's venues | CR-106 CONTENT | CONTENT | MOVER(behaviour) | B11F1.01 |
| B11F1.03 | several cohorts a settlement: `label`, `heritage`, `conviction`, and the summed ceiling | CR-107 (the loader) | BUILD | EQUAL | Batch B12c |
| B11F1.04 | the cohort rows | CR-107 CONTENT | CONTENT | MOVER(behaviour) | B11F1.03 |
| B11F1.05 | the Schoenland heritage engages Altonia | CR-107 (v11 part 16 head item 4) | BUILD | MOVER(behaviour) | B11F1.04 |
| B11F1.06 | territory caps on developments and their sizes: the design | part 16 §3.4 | DESIGN-FIRST | EQUAL | Batch B12c |
| B11F1.07 | a cohort's faction commitment | CR-107b | HELD (a reader audit of `occupies`, `mustered`, `standing_at`, `raisable_by`, `acquaintance_pairs`, `opinion_referents`, `footprint`, `density`, and the re-pin of `test_in36_foreign.py`) | — | — |
| B11F1.99 | re-pin and close readings | `V12_STRUCTURE_part4.md` E-1 | BUILD | MOVER (the re-pin) | B11F1.01 to B11F1.06 |

Not in this batch, and where each is: CR-104 (B11F2; reads B11F1.02's Sites); SE-06's conviction half (SUPERSEDED by `31_WR_B` commit 2 with `31_WR_A`, B38: `master/V11_EVALUATION_part2.md:179`); "convergence and divergence for everyday needs" (CR-107: "NOT CARRIED … a `pursuits:` field on the row is the carrier and is not designed here"); the Church Sites' `site_yield` (none: "no `site_yield` row").

### B11F1.01 — the Church's buildings: three kinds, an owner table, one owner of ownership, a `site:` key · CR-106 (a)–(d) · BUILD · HASH EQUAL
- SOURCE: `E1` §Carry-forward CR-106 (`:2901-2933`; v11 `_part16.md:131-153`: "WHAT" (a)–(d), "REMAINING UNBUILT", "EXIT and FALSIFIER", "HASH MOVERS", "HOLES AND LEDGER IDS", "FILES", "LAYER 1", "BUILDER"); the intake `:187`; `ED-IN-0352` item (7); `master/eval/E5.md` Block F3; closes CR-106's machinery.
- ADVANCES: R-01 (re-read): the realm's fabric carries its owner as data.
- INSTRUCTION (copied, `harness/populated.py` → `boot/realm.py` by symbol, NAMES; line numbers kept as the source's text, each located by symbol):
  "(a) KINDS. Three rows appended to `site_kinds` (`rosters.yaml:1741`, appended after `:1778`): `worship`, `templar_quarters`, `school` (names Jordan's; "schools/monasteries" is one function) `[ASSUMPTION; medium; Jordan to correct; revert: rename the rows]`. SCALE is `Site.condition` with `band_floors` rows (chapel, church, cathedral as bands of `worship`; sizes of `templar_quarters` likewise) … so an upgrade needs no new verb; three separate kinds per function would duplicate that ladder. Each kind carries the required cells (`wear_per_season`, `band_floors`, `capacity_floor`; both-direction loader checks, `data/fixtures.py:106-111`; `rosters.yaml:1890-1896`); `wear_per_season` 0 ships as the control arm, as `dwelling` did (`rosters.yaml:1831`); `works_cost` optional (unpriced means `build` refuses, `loop/effects_founding.py:218-221`); no `site_yield` row."
  "(b) THE OWNER TABLE. A new table `site_owner` in `rosters.yaml`, `keys: [site_kinds]`, `default_cell: null`; a non-null cell names an owning institution, validated at load as a `factions` member (precedent: `HEAD_SEAT`, `data/rosters.py:1268-1274`, `require_member`). The three new kinds' cells name the Church of Solmund; null means owned through the rung, as today. The exception is DATA on the kind row; there is no branch on "Church" anywhere in code, and any institution with exclusive buildings uses the same cell."
  "(c) ONE OWNER OF OWNERSHIP. `queries/faction_q.py::owner_of(w, site) = SITE_OWNER[site.kind] or holder_faction_of(w, site.rung)`. No `hold` Tenure on a Site … no `Site.owner` field (a hash mover and a second home for what the kind row decides, §0.05 clause 3)."
  "(d) MINTING. `venues.yaml` building rows gain an optional `site:` mapping `{kind, condition}` (a `site_kinds` member and its starting `condition`; ONE key, because the starting condition differs by row …) `[ASSUMPTION; medium; Jordan to correct; revert: the flat pair]`; the builder mints `Site(f"s_{sid}_{slug}_{kind}", bid, kind, condition)` for any row carrying it, in the dwelling loop (`populated.py:1236-1240`); it reads no `serves` tag and no name. Uniform: any row may carry `site:`."
  In this commit the three kinds' cells are those of `content_church_sites.yaml` PART 1 (`wear_per_season` 0, `capacity_floor` 0, `works_cost` `{timber: 10}`, the one three-floor `band_floors` ladder, `site_owner` naming the Church of Solmund), each cell with its `[ASSUMPTION; medium; Jordan to correct]` note; no `venues.yaml` row carries `site:` yet (B11F1.02). The hole-register row, from B11F1's H block: "kind `RULING`, grade `assumption`: the three names, the null-cell rule and the first-reading rows, with the revert above".
- WHERE: `engine/season/rosters.yaml` (`site_kinds` values; `wear_per_season`, `capacity_floor`, `works_cost`, `band_floors` cells; NEW table `site_owner`, at the end of its family's block); `engine/season/data/rosters.py` (`SITE_OWNER` and its loader); `engine/season/data/fixtures.py` (the per-kind checks, if the loader lives there); `engine/season/queries/faction_q.py` (`owner_of`); `engine/season/boot/realm.py` (the `site:` minting step in the dwelling loop); `engine/season/hole_register.yaml` (one row); NEW `engine/season/tests/test_cr106_church_sites.py`; `unified/U1_GLOSSARY.md` (*owner*).
- TESTS: in the new file, written before the edit and read red: (1) "a planted `worship` Site on a rung held by another faction: `owner_of` reads the Church's proposition; set that table cell null and it reads the rung's holder"; (2) "the rename falsifier (every id and faction name renamed consistently, `site_owner` cells included) changes no reading"; (4) "with no row carrying `site:`, the World and its hash are unchanged" `[ASSUMPTION: test names written by the producer from the clauses, `test_cr106_1_…` to `test_cr106_4_…`]`. (3) is B11F1.02's.
- FALSIFIER and CONTROL: "MUTATION: key `owner_of` on the kind's name and (1)'s null-cell variant reads red." "CONTROLS: `wear_per_season` 0 (the control arm); `content_hash` EQUAL when no row carries `site:`."
- GATE: `python -m pytest engine/season/tests/test_cr106_church_sites.py -q` → (1), (2), (4) pass; the realm hash (`HASH READING`) at seeds 0 to 2, one season → equal to B12c's close (`reading @<sha>`).
- HASH MOVERS: none (no row carries `site:`).
- DEPENDS ON: EXISTS-IN-TREE `rosters.yaml: site_kinds` (`:1784` at `9c2c3ab`), `queries/world_q.py::holder_faction_of`, `data/rosters.py::HEAD_SEAT`, `::require_member`, `Site.condition`, `band_floors`; V12 Batch B03c (`boot/realm.py`'s dwelling loop, moved from `populated.py`); `ED-IN-0352` (landed). "RE-BASE: `venues.yaml` and `populated.py`'s dwelling loop as the settlement-lane batches that edit them leave them" (B12a to B12c).
- GLOSSARY: row *owner* (new if absent): "the faction a Site belongs to: its kind's `site_owner` cell if set, else the faction holding its rung (`faction_q.owner_of`)"; ordinary reading: who a thing belongs to.
- NAMES: `harness/populated.py` dwelling loop → `boot/realm.py` (B03c, CI-07).
- COST and TIER: small build; `sonnet`, `high`; a third-tier critic (`opus`) on the null-cell rule.
- LANDS IT: B11F1's producer; `Item: B11F1.01`, `[skip ci]`.

### B11F1.02 — the Church's buildings placed in every settlement's venues · CR-106 CONTENT · CONTENT · HASH MOVER(behaviour)
- SOURCE: `E1` §Carry-forward CR-106 ("CONTENT", "EXIT and FALSIFIER" (3), "CONTROLS", "HASH MOVERS"); `proposals/2026-11-08-flow-conditioning/content_church_sites.yaml` (PART 2, the `venues.yaml` rows), `content_provenance.md` table A, `content_validate.py`; RATIFIED by Jordan 2026-11-08 as "the accepted first reading; every cell keeps `[ASSUMPTION; medium; Jordan to correct]` and its revert".
- ADVANCES: R-01 (re-read): "the Church's reach into every territory, which canon makes the source of its political weight" exists in the World.
- INSTRUCTION: transcribe the draft's `venues.yaml` rows (the `site:` mapping on each building row the draft names, "ONE key … which the builder nests"), keeping every `[ASSUMPTION; medium; Jordan to correct]` note and revert as a comment. The draft's stated outcome, copied: "41 Church Sites in `build_realm(0)` (37 places of worship, 3 schools, 1 Templar quarters), Himmelenger's cathedral highest (1000) and the scale order village chapel < town church < cathedral holding; the `chapter_house` row carries the Templar quarters …, the `almonry` row carries no `site:` … Coverage: every territory under `r_valoria` that holds a settlement holds at least one Church Site". The counts are the validator's and the test's, never a literal.
- WHERE: `engine/season/venues.yaml` (the `site:` keys); `engine/season/tests/test_cr106_church_sites.py`.
- TESTS: (3), written before the transcription and read red: "in `build_realm(0)` the number of `worship` Sites equals the number of settlements whose venue rows carry `worship`, asserted by counting `venues.yaml` rows in the test and not by a literal, and every territory under `r_valoria` that holds a settlement holds at least one Church-owned Site (the validator's check; `terr_T15` holds no settlement, and `terr_ALT` is a foreign root whose one settlement, `set_alt_1`, has no venue rows)".
- FALSIFIER and CONTROL: (3) red. "the control-arm identity `test_24d_i_...` is re-read with the Church Sites present and its result stated (… the Church kinds' `{100,500,800}` rows remove that guard; MATTER also writes every Site every season at rate 0 and emits `condition.worn` …, and `work` forms on a Site-classed referent …, so the Church Sites enter `work`/`restore`'s referent space: a reading, stated, not hidden)" (UNDECIDED 3: the four `test_24d_i_*` tests and the `test_24d_ii_*` tests are run and each result stated).
- GATE: `python -m pytest engine/season/tests/test_cr106_church_sites.py engine/season/tests/test_governance_build.py engine/season/tests/test_migrate_capacity.py -k "cr106 or 24d" -q` → pass, or a red `test_24d_*` quoted with its reason in the commit body; `python proposals/2026-11-08-flow-conditioning/content_validate.py` → exit 0; the realm hash (`HASH READING`) at seed 0 after one season → moved (declared), the value quoted; `aperture 2 0`'s `work` and `restore` formed counts quoted beside B11F1.01's.
- HASH MOVERS: "`build_realm(0).content_hash()` MOVES where rows carry `site:` (new Sites fold into the encoding, `state/world.py:1664,1704-1707`)". Declared; re-pinned in B11F1.99.
- EXPECTED RED UNTIL B11F1.99: `engine/season/tests/_realm_goldens.py`.
- DEPENDS ON: V12 B11F1.01.
- GLOSSARY: none.
- COST and TIER: content transcription; `sonnet`, `high`.
- LANDS IT: B11F1's producer; `Item: B11F1.02`, `[skip ci]`. The PR body lists the rows as Jordan's to correct (D-19).

### B11F1.03 — several cohorts a settlement: `label`, `heritage`, `conviction`, and the summed ceiling · CR-107 (the loader) · BUILD · HASH EQUAL
- SOURCE: `E1` §Carry-forward CR-107 (`:2937-2974`; v11 `_part16.md:154-181`: "WHAT", "REMAINING UNBUILT", "EXIT and FALSIFIER", "HASH MOVERS", "HOLES AND LEDGER IDS", "FILES", "BUILDER"); the intake `:330`; `master/eval/E5.md` Block F4; `ED-IN-0352` item (7); closes CR-107's loader.
- ADVANCES: R-01 (re-read).
- INSTRUCTION (copied; the cohort loader and `seat_cohorts` by symbol in `boot/realm.py`, NAMES): "Three additions to the row and one held, all optional so that an old row reproduces today's id and hash: `label:` (one word): the id becomes `cohort_<rung>_<label>`, and the duplicate test runs over `(rung, label)`. The `guards:` block … is the precedent for a second cohort family with its own fields. `heritage:` a `Person.heritage` member (`state/carriers.py:819-826`; five members, `descriptor_registry.yaml:240-244`): the caste carrier … `conviction:` a map validated by `data/affiliations.py::conviction_map` (`:39`) over the affiliations (`solmund_orthodoxy`, `einhir_restoration`, `altonian_civics`, the others)." "`faction:` HELD (CR-107b, not built here)" (B11F1.07). "THE CEILING FIX: `seat_cohorts` checks each row's weight against `capacity(w, rung)` … while `population` sums residents' weights … and `has_room` throttles `migrate` on that sum …; two cohorts of weight 2 at a capacity-4 settlement would each pass and fill it. The check becomes the SUM of the rung's cohort weights against `capacity`."
  At `9c2c3ab`: the loader's duplicate check is the `row["rung"] in seen` refusal and the per-row ceiling is `seat_cohorts`'s `wt > room` refusal, both in `harness/populated.py` (B03c moves them). The hole-register row from B11F1's H block: "kind `RULING`, grade `assumption`) for the summed-ceiling reading". `cohorts.yaml`'s stale comment lines (`:21-23` at the source's read) are corrected in this commit ("comment lines `:21-23`, stale, corrected").
- WHERE: `engine/season/boot/realm.py` (the cohort loader, `seat_cohorts`, the id); `engine/season/cohorts.yaml` (the comment lines only); `engine/season/hole_register.yaml` (one row); NEW `engine/season/tests/test_cr107_cohort_identity.py`; `unified/U1_GLOSSARY.md` (*cohort*).
- TESTS: in the new file, written before the edit and read red: "(1) two planted cohorts of opposed creeds (an `incompatible` pair) in one settlement: `commensurate` reads -1 and a telling between them lands at a discounted confidence (`_credit`), the same teller to a cohort of the same creed does not; (2) a summed weight over `capacity` is refused at seating; (3) two rows on one `(rung, label)` are refused, and a row with no new key reproduces today's id and hash (EQUAL); … (5) the rename falsifier" `[ASSUMPTION: names `test_cr107_1_…` to `test_cr107_5_…`; (4), "a `faction:` row mints exactly one `commit` Tenure", is CR-107b's and is not written while it is HELD]`.
- FALSIFIER and CONTROL: "MUTATION: check each row's weight alone and (2) reads red. CONTROLS: the shipped `cohorts.yaml` unchanged gives `content_hash` EQUAL".
- GATE: `python -m pytest engine/season/tests/test_cr107_cohort_identity.py -q` → (1), (2), (3), (5) pass; the realm hash (`HASH READING`) at seeds 0 to 2, one season → equal to B11F1.02's after-reading.
- HASH MOVERS: "none from the loader change alone".
- DEPENDS ON: EXISTS-IN-TREE `harness/populated.py::seat_cohorts`, `COHORT_PREFIX` (moved to `boot/realm.py` by B03c), `queries/world_q.py::capacity`, `::population`, `data/affiliations.py::conviction_map`, `Person.heritage`; V12 Batch B03c. "RE-BASE: … the `temperament_rows`/`seat_cohorts` code as the held batch leaves them."
- GLOSSARY: row *cohort*: its owner gains the `label:`, `heritage:`, `conviction:` keys and the id `cohort_<rung>_<label>`; "a cohort is the people of a settlement who share a caste, creed or allegiance, seated as one person of weight"; ordinary reading: a group of people with something in common.
- NAMES: `harness/populated.py::seat_cohorts` and the cohort loader → `boot/realm.py` (B03c).
- COST and TIER: small build; `sonnet`, `high` ("second tier for the loader").
- LANDS IT: B11F1's producer; `Item: B11F1.03`, `[skip ci]`.

### B11F1.04 — the cohort rows · CR-107 CONTENT · CONTENT · HASH MOVER(behaviour)
- SOURCE: `E1` §Carry-forward CR-107 ("CONTENT", "CONSEQUENCES THE CONTENT CREATES", "BEHAVIOUR WITH SEVERAL COHORTS", "HASH MOVERS"); `proposals/2026-11-08-flow-conditioning/content_cohorts.yaml`, `content_provenance.md` table B, `content_validate.py` ("69 PASS, 0 FAIL, exit 0" at the source's read); RATIFIED 2026-11-08 as the accepted first reading.
- ADVANCES: R-01, R-02 (re-read): "the caste, creed and allegiance contests Jordan describes" can occur inside a settlement.
- INSTRUCTION: replace `cohorts.yaml`'s `cohorts:` block with the draft's rows ("51 rows over the 37 settlements, replacing the `cohorts:` block; `temperaments:` and `guards:` stay"), each row's `[ASSUMPTION; medium; Jordan to correct]` note kept; "Majority cohorts carry no `label:`; their ids stay as today"; "no row carries `faction:`". The commit body quotes, as readings, "the CONSEQUENCES THE CONTENT CREATES (stated, not hidden)": "every two-cohort village and fortress is at `capacity`, so `migrate` into it is refused from the first tick …; orthodox and Revivalist cohorts in one settlement are `incompatible` under `commensurate`, so their tellings discount each other at once; no `commit` Tenure is minted, so no faction reader moves".
- WHERE: `engine/season/cohorts.yaml` (`cohorts:`); `engine/season/tests/test_cr107_cohort_identity.py`.
- TESTS: one test, written before the transcription and read red: the draft's counts read from the file, not literals (`test_cr107_the_shipped_rows_seat_one_cohort_per_row_and_none_over_capacity`) `[ASSUMPTION: name]`.
- FALSIFIER and CONTROL: a seated cohort count unequal to the row count; a summed weight over capacity. Control: the loader's tests (B11F1.03) stay green.
- GATE: `python -m pytest engine/season/tests/test_cr107_cohort_identity.py -q` → pass; `python proposals/2026-11-08-flow-conditioning/content_validate.py` → exit 0; `aperture 2 0`'s `migrate` executed count quoted beside B11F1.03's; the realm hash (`HASH READING`) at seed 0 → moved (declared), quoted.
- HASH MOVERS: "the authored rows move every hash from `build_realm(0)` on (a golden re-record, stated plainly)". Declared; re-pinned in B11F1.99.
- EXPECTED RED UNTIL B11F1.99: `engine/season/tests/_realm_goldens.py`.
- DEPENDS ON: V12 B11F1.03.
- GLOSSARY: none.
- COST and TIER: content transcription; `sonnet`, `high`; "the content pass is a separate judgment lane" (`opus` reads the PR body's list).
- LANDS IT: B11F1's producer; `Item: B11F1.04`, `[skip ci]`. The PR body lists the rows as Jordan's to correct (D-19).

### B11F1.05 — the Schoenland heritage engages Altonia · CR-107 (v11 part 16 head item 4) · BUILD · HASH MOVER(behaviour)
- SOURCE: `workplans/valoria_master_workplan_v11_part16.md` head item 4 (read at `9c2c3ab`): "**The Schoenland `engages:` registry cell** (`schoenlander: altonia` in `references/descriptor_registry.yaml`): RATIFIED as part of CR-107. It is a registry row edit with its own tests and is made at CR-107's build, not in this change."; `E1` §Carry-forward CR-107 "A GAP, NOT FILLED" (superseded on this point by the head, UNDECIDED 2); `ED-IN-0301` (the confirmed cells).
- ADVANCES: R-02 (re-read): "the Schoenland cohort (S-037) holds 1 throughout and that populace has a heritage but no intensity" is corrected.
- INSTRUCTION: `references/descriptor_registry.yaml` `heritage_roster.engages:` gains `schoenlander: altonia` (beside `southern_einhir: einhir` and `altonian: altonia`), with a comment citing CR-107 and v11 part 16 head item 4; re-derive `engine/engine_params/descriptors.json` with `tools/export_descriptors.py`, never by hand.
- WHERE: `references/descriptor_registry.yaml` (`heritage_roster.engages`); `engine/engine_params/descriptors.json` (re-derived); `engine/season/tests/test_cr107_cohort_identity.py`.
- TESTS: `test_cr107_the_schoenland_cohort_engages_altonian_civics` (`queries/person_q.py::heritage_regard` reads the cell for a planted `schoenlander` person), written before the edit and read red `[ASSUMPTION: name]`.
- FALSIFIER and CONTROL: the S-037 cohort's engaged affiliation still reads 1. Control: the other four heritages' `heritage_regard` unchanged.
- GATE: `python tools/export_descriptors.py --check` → OK; `python -m pytest engine/season/tests/test_cr107_cohort_identity.py -q` → pass; the realm hash (`HASH READING`) at seed 0 → moved only if a `schoenlander` person is in the realm (quoted either way).
- HASH MOVERS: every seeded world holding a `schoenlander` person whose regard is read (the S-037 cohort). Declared; B11F1.99.
- DEPENDS ON: V12 B11F1.04 (the S-037 row); EXISTS-IN-TREE `references/descriptor_registry.yaml::heritage_roster.engages`, `queries/person_q.py::heritage_regard`, `tools/export_descriptors.py`.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B11F1's producer; `Item: B11F1.05`, `[skip ci]`.

### B11F1.06 — territory caps on developments and their sizes: the design · part 16 §3.4 · DESIGN-FIRST · HASH EQUAL
- SOURCE: `workplans/valoria_master_workplan_v11_part16.md` §3.4 (read at `9c2c3ab`); the intake `:331` ("design-first, post-F1"); `master/eval/E5.md:172`; `proposals/07_SE_ground_and_granaries.md` R1 (the endowment keyed on the territory code); D-18; UNDECIDED 1.
- ADVANCES: none (a file).
- INSTRUCTION: write ONE design file, `proposals/v12_B11F1_territory_caps.md` `[ASSUMPTION: the name]`, `## Status: PROPOSED`, no code, whose charge is the source's paragraph, copied: "TERRITORY CAPS on developments and their sizes (Jordan: a bread-basket territory may hold far more farms than a mining territory, which holds the mines the other cannot; a large city a large market, a small town a small one). Not needed for CR-104, CR-106 or CR-107 (size is `Site.condition` …). `capacity(w, rung)` bounds POPULATION from dwellings and is not this shape. The cap would be a roster table keyed on `[settlement type or geography sub, site_kinds]` read as a `build` decline in `_eff_build`, using the geography YAML's per-province cells (`fort_level`, `starting_pros`; `fort_level` is pinned by `HANDOFF_SE.md:18`'s standing order). It is its own design-first position, after ED-IN-0297's authored works (`venues.yaml:157-198`) … Economic function (farms, markets, mines, town squares) rides on the same kinds and `site_yield`, which today covers harbour and seam only." The design states (1) the table's key (whether `07_SE_ground_and_granaries` R1's territory-code key, landed in B12, is that key), (2) the decline and where it reads, (3) the content it needs and who authors it, (4) its falsifier and control (the cap table empty reproduces today's `build`), (5) the batch a build would join.
- WHERE: NEW `proposals/v12_B11F1_territory_caps.md`.
- TESTS: none (no code).
- FALSIFIER and CONTROL: the file exists and states (1) to (5); no code.
- GATE: `test -f proposals/v12_B11F1_territory_caps.md` and `grep -c "^## Status: PROPOSED" proposals/v12_B11F1_territory_caps.md` → 1; no file outside it in the commit's diff.
- HASH MOVERS: none.
- DEPENDS ON: V12 Batch B12a to B12c (`07_SE_ground_and_granaries` R1, the endowment rows keyed on the territory code, lands in the B12 chain, which B12c closes); EXISTS-IN-TREE `loop/effects_founding.py` (`_eff_build`), `venues.yaml`.
- GLOSSARY: none.
- COST and TIER: design; `opus`, `high`, with a `ners` critic.
- LANDS IT: B11F1's producer; `Item: B11F1.06`, `[skip ci]`. No build follows in v12: no source writes one; what the design leaves to Jordan is reported at the close, not built.

### B11F1.07 — a cohort's faction commitment · CR-107b · HELD
- What it is: CR-107's "`faction:` HELD (CR-107b, not built here): a faction member whose `commit` Tenure the builder would mint", RATIFIED "as a held position. Its gate is a design fact, not a pending sign-off: a `commit` makes the faction occupy the settlement at build, so it is built only after the reader audit" (v11 part 16 head item 3; `master/eval/E5.md:161`).
- Trigger: "a reader audit enumerates `occupies`, `mustered`, `standing_at`, `raisable_by`, `acquaintance_pairs`, `opinion_referents`, `footprint` and `density` and re-pins that test" (`engine/season/tests/test_in36_foreign.py`'s `members(foreign, FID) == CAST`). No batch of v12 runs the audit; the row goes to the held table (`V12_STRUCTURE_part3.md` §7.9) with this trigger.
- No commit, no gate.

### B11F1.99 — re-pin and close readings · `V12_STRUCTURE_part4.md` E-1 · BUILD · HASH MOVER (the re-pin)
- SOURCE: `V12_STRUCTURE_part4.md` E-1, E-2; `V12_STRUCTURE_part2.md` §5.9, §5.12; `IS-A-12`.
- ADVANCES: the close's readings of R-01, R-02.
- INSTRUCTION: (1) re-record `engine/season/tests/_realm_goldens.py` at seeds 0, 1, 2 (one season) and regenerate `engine/season/runs/results.json` with `harness/report.py`, against the RE-PIN baseline; the commit says "re-pin: content (…)". (2) Write R-01's and R-02's conjuncts' `reading:` records in `engine/season/requirements.yaml` (`status:` untouched). (3) The BATCH GATE's readings and the wall time in the commit body.
- WHERE: `engine/season/tests/_realm_goldens.py`; `engine/season/runs/results.json`; `engine/season/requirements.yaml` (`reading:` records).
- TESTS: `_realm_goldens.py`'s tests green after the re-pin.
- FALSIFIER and CONTROL: a pin moved by an item not declared MOVER; a pin that moves with no `site:` key, the shipped `cohorts.yaml` and the old `engages:` (the controls).
- GATE: the BATCH GATE above.
- HASH MOVERS: the re-pin itself.
- DEPENDS ON: V12 B11F1.01 to B11F1.06.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B11F1's producer; `Item: B11F1.99`, the batch's last commit (no `[skip ci]`).

| STOP. Batch B11F1-flow-se closes here |
