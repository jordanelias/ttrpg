# Workplan v12 — part 4, continued: Batch B03-hygiene, positions B03.18 to B03.28, and this half's serial edges and file census

## Status: PROPOSED (the continuation of part 4 of workplan v12, `V12_STRUCTURE_part2.md` §4.1's `_cont` rule; resolves nothing at runtime, CLAUDE.md §0.05; not canon)

The batch block's head, its position table and B03.01 to B03.17 are in the file this one continues (part 4). Words, paths and the realm reading `R(s)` are defined there.

### B03.18 — pointer and stale text at the owners a porter reads first · 11_GO_pointer_and_stale_text_resolutions items 1, 2, 11, 12, 13 · BUILD · HASH EQUAL
- SOURCE: `proposals/11_GO_pointer_and_stale_text_resolutions.md` "Resolutions" rows 1, 2, 11, 12, 13, "The gate", "Lands it" ("items 1–3, then 7–8 (with GO-11), 9, 11, 12, 13 in one `[cleanup]` commit in B03"); closes F-GO-10, F-GO-11 (part). Item 3 lands in B03.21 (UNDECIDED (4)); items 7–8 are B03.20; item 6 is B03.19; item 9 is not carried (UNDECIDED (6)).
- ADVANCES: none of the nine; the porter is sent to the ratified owner first.
- INSTRUCTION (copied, with the corrections UNDECIDED (5) states):
  1. Item 1, `CURRENT.md`, the GO row. Old: `| **Godot conversion** | `godot/godot_conversion_strategy_v1.md` — PROPOSED | ED-GO-0001; ED-GO-0002 (the engine version); `registers/handoffs/HANDOFF_GO.md` |`. New: `| **Godot conversion** | `architecture/meta/04_CODE_ARCHITECTURE.md` §C.12 (RATIFIED, the Godot mapping); the port gate: batch `B41-go-port-gate` of the active master workplan; `godot/godot_conversion_strategy_v1.md` — PROPOSED, intent only | ED-GO-0001; ED-GO-0002 (the engine version); `registers/handoffs/HANDOFF_GO.md` |` (the source's "the B10-20 card in `workplans/valoria_master_workplan_v11_part3.md`" is v11's, deleted in v12's adopting commit; `B41-go-port-gate` is v12's port gate, `V12_STRUCTURE.md` §2.2). Ladder step 3: "`CLAUDE.md` §6 already says the season loop's ratified Godot mapping is `04` §C.12".
  2. Item 2, `godot/README.md`: old "It **is** the eventual `res://` project root." → new "The Godot project is `jordanelias/valoria-game`, a separate repository; this directory holds design reference for the port and no project files." (ladder step 1: CLAUDE.md's preamble).
  3. Item 11, `engine/season/tests/test_go07_canonical_digest.py`: the source deletes "`_old_entity_digest`, `_old_content_hash`, every `old` pin, the `assert got["old"] != got["new"]` line, and the RE-RECORDED / RE-PINNED notes (72)" and keeps "the vector half … unchanged; one `new` hash, act count, census digest and counts per seed; the build-world pin". B02.01 already removed the `_old_content_hash` half of the two control tests and moved the shipped pins to `_realm_goldens.py`. So, in order: (a) open the file on B03's base and record in the commit body which of the five named pieces remain; (b) delete those that remain (a helper with no caller left; every `old` literal; the `assert got["old"] != got["new"]` line if present; every `#: RE-RECORDED …` / `RE-PINNED …` comment block); (c) leave the encoding-vector tests and the imports of `BUILD`, `SHIPPED`, `CENSUS` from `_realm_goldens.py` untouched. Ladder step 2: "the control compared two digests across one commit (`b9beec9d` → GO-07); both are now re-read from the same run at each mover, so their agreement observes nothing. The notes are dated narrative whose home is the commits that made them."
  4. Item 12, `godot/godot_conversion_strategy_v1.md`, §V.2, after item 3 ("**Statistical parity** (second tier)…"), one line in the document's own marker convention (the `> **[LAYER 1 ANSWERS — marker only; the clause above is unchanged and this document stays PROPOSED]**` lines above it): `> **[LAYER 1 ANSWERS — marker only; the clause above is unchanged and this document stays PROPOSED]** (W3-1, A-30) The port implements the oracle's keyed draw (the port gate, `B41-go-port-gate`); parity is exact, by `(key, n) → u` vectors and `content_hash` at any seed. 'Statistical parity (second tier)' has no instrument in either repository and needs none.` ("(B10-20)" in the source → the v12 handle, UNDECIDED (5).) "The document stays PROPOSED."
  5. Item 13, the word: "'parity' used for two things: the auto/manual doctrine's 'parity harness' (played against auto-resolved, ED-SC-0013) and the port gate's 'parity' (oracle against port)" → "in new text, **fidelity parity** for the first and **port parity** for the second; no retrofit of existing text". `unified/U1_GLOSSARY.md` §F gains one row (§5.11): `| **fidelity parity** / **port parity** | fidelity parity: a played subsystem against its auto-resolved form (ED-SC-0013); port parity: the Godot port against the Python oracle, by `(key, n) → u` vectors and `content_hash` | — (coined by `11_GO_pointer_and_stale_text_resolutions` item 13; CLAUDE.md §4) | bare "parity" in new text, which a reader cannot place | new suite and plan text; no retrofit |`.
- WHERE: `CURRENT.md` (row *Godot conversion*); `godot/README.md` (the `res://` sentence); `engine/season/tests/test_go07_canonical_digest.py` (helpers, `old` pins and the re-record notes that remain); `godot/godot_conversion_strategy_v1.md` (§V.2, one marker line); `unified/U1_GLOSSARY.md` (§F, one row).
- TESTS: `test_go07_canonical_digest.py`, "red before the edit only if the spent control is reintroduced (control: the mutation its head records)"; green before and after.
- FALSIFIER and CONTROL: "if deleting the `old` digest removed the test's ability to see a world move, a planted one-field change in a built realm would pass; it does not, because the `new` hash, the act count and the counts are still pinned." Run the plant the file's head records ("drop a dataclass's last field in `_object_head`") once after the edit → the file reddens; revert. Control: `R(0)` hash equal to B03.17's.
- GATE: `python tools/currency_consistency_check.py` → exit 0 and `python tools/freshness_gate.py` → exit 0 ("clean after items 1–3"); `python -m pytest engine/season/tests/test_go07_canonical_digest.py -q` → green, and the recorded mutation still reddens it; `git grep -n "RE-RECORDED\|RE-PINNED\|_old_content_hash\|_old_entity_digest" -- engine/season/tests/test_go07_canonical_digest.py` → no hit.
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `CURRENT.md` row *Godot conversion* (opened at `aa31fd2`); `godot/README.md` (the `res://` sentence); `godot/godot_conversion_strategy_v1.md` §V.2 items 2–3 and the marker lines; `test_go07_canonical_digest.py::_old_entity_digest`, `::_old_content_hash`; V12 B02.01 (pins moved to `_realm_goldens.py`), B03.17 (`CURRENT.md`, earlier: "`09_WR_B_pointer_text_for_the_orchestrator.md` (B03, before this file in U3's chain)"); V12 Batch B41 named, not depended on.
- GLOSSARY: §F *fidelity parity* / *port parity* (step 5): "port parity" means the port gives the oracle's results, as a currency's parity means equal value.
- COST and TIER: edit (transcription); `haiku` for items 1, 2, 11–13 (the source's), `sonnet` reads the go07 file's remains.
- LANDS IT: B03's producer; one `Item: B03.18` commit, `[skip ci]`. GO reviews (the source's).

### B03.19 — Layer 1's rejection-5 measurement paragraph becomes a command · 11_GO_pointer_and_stale_text_resolutions item 6 · HELD (Jordan: a Layer 1 amendment; trigger: Jordan merges the hunk) · HASH —
- SOURCE: the same file, row 6 and "Lands it": "item 6's Layer 1 sentence in the same B03 PR, held for Jordan's merge"; "Item 6 (rejection 5's measurement paragraph, still quoting 167 / 128 / 18 / 4) was not an A-n node and is NOT applied; it stays owed text for Jordan's merge."
- ADVANCES: none of the nine; Layer 1 stops quoting counts over files that do not exist (`shape.py`, `seam.py`).
- INSTRUCTION (the text Jordan is offered; no agent applies it): in `architecture/meta/04_CODE_ARCHITECTURE.md` §C.12, rejection 5's measurement paragraph (the sentences that quote "167 times", "128 of them in `shape.py`", "18 `except` clauses, 4 of them in `shape.py`" and `engine/season/seam.py::contest`) becomes one sentence: "Measured with `grep -rE '^\s*raise ' engine/season` outside `tests/`, `harness/`, `data/` and `manifest/`; re-run it rather than quoting a figure. One site returns a typed value (`seam/contest.py::ContestError`)." Ladder step 2 (the source's): "the files it counts do not exist; a pointer to a command replaces a stale figure". The B03 PR body lists it under *held back*, with this text; v12 does not edit Layer 1 to match code (CLAUDE.md §0.05).
- WHERE: `architecture/meta/04_CODE_ARCHITECTURE.md` (§C.12, rejection 5's measurement paragraph), on Jordan's merge only.
- TESTS: none.
- FALSIFIER and CONTROL: on the merged tree, the sentence's command runs and prints lines; `seam/contest.py::ContestError` exists (returned, not raised; checked at the tree by the source's lane). Control: no file of this batch's diff touches `architecture/` unless Jordan merged the hunk (`git diff --stat <batch-start-sha>..HEAD -- architecture`).
- GATE: `git diff --stat <batch-start-sha>..HEAD -- architecture` → empty (held), or exactly this paragraph if Jordan merged it in the batch's PR.
- HASH MOVERS: none.
- DEPENDS ON: Jordan (a Layer 1 amendment, CLAUDE.md layer table; not an A-n node, `unified/U3_LAYER1_AMENDMENTS.md` has no row for it); EXISTS-IN-TREE `engine/season/seam/contest.py::ContestError`.
- GLOSSARY: none.
- COST and TIER: none to build; `sonnet` wrote the hunk's wording (the source's tier for Layer 1 hunks).
- LANDS IT: nobody in this batch; Jordan's merge. For the held-back list of `V12_STRUCTURE_part3.md` §8.2, which does not yet name it.

### B03.20 — the contract file's Key-era `parity:` values and the skeleton note · 11_GO_pointer_and_stale_text_resolutions items 7–8 · POINTER (GO-11, Batch B03g-go-early-landings) · HASH —
- SOURCE: the same file, rows 7 ("This is GO-11's own edit; listed so GO-11's re-base names it") and 8 ("GO-11 as planned"); the intake GO-11 (its gate: `grep -c "key-log" references/module_contracts.yaml` prints 0); `V12_STRUCTURE.md` D-11 (GO-11 lands in B03g, after B03).
- What the pointed edit does: deletes `references/module_contracts.yaml`'s `golden_path:` note about `BaseEngine / EngineModule / KeyBus / Resolver / GameState` (its subject, `godot/skeleton/`, was deleted by GO-14), and rewrites the twenty `parity:` values `key-log` and `key-log + typed-export round-trip` to `state-hash` or `seam-io` (`11_GO_port_gate_order_and_coverage.md` §3 supplies `seam-io`'s meaning).
- Target: `references/module_contracts.yaml` (`golden_path:` note; every `wiring.parity:`). B03.10, B03.12, B03.13, B03.22 and B03.26 edit other keys of the same file first; GO-11 re-bases on B03's merge.
- Gate (GO-11's, read in B03g): `grep -c "key-log" references/module_contracts.yaml` → 0; `python tools/export_composition.py --check` → OK.
- No work in B03. `17_CENSUS_REST_3` C-1 "does not repeat" row 8 for `combat` (B03.22).

### B03.21 — which design reference binds the port: two owner sentences and a standing order · 11_GO_design_reference_disposition edits 1, 2, 4, with 11_GO_pointer_and_stale_text_resolutions item 3 · BUILD · HASH EQUAL
- SOURCE: `proposals/11_GO_design_reference_disposition.md` "Exact edits, by owner" 1, 2, 4, "The gate", "The falsifier"; `proposals/11_GO_pointer_and_stale_text_resolutions.md` row 3 (UNDECIDED (4): "TEXT item 3's replacement sentence gains one clause, applied as one edit"); ladder steps 2 and 3 (the source's); closes F-GO-13, F-GO-14, F-GO-20, F-GO-21.
- ADVANCES: none of the nine; "one sentence at each of two owners tells a porter which document binds."
- INSTRUCTION (copied):
  1. "`godot/godot_architecture_specification.md` (its Status line) — old: 'retained for its pipeline/procedure structure, not its numbers. The GOVERNING spec for the port is `godot/godot_conversion_strategy_v1.md`.' New: 'retained for its extraction procedure (Part Seven) only. The ratified Godot mapping is `architecture/meta/04_CODE_ARCHITECTURE.md` §C.12, which this document contradicts at three points: one autoload holding all state (rejection 1), container signals as the consequence stream (rejection 3), and one seeded generator for the campaign (rejection 4). `godot/godot_conversion_strategy_v1.md` is PROPOSED, intent only.'" The file's `## Engine:` line is not touched (ED-GO-0002 owns any engine version).
  2. `godot/README.md`, the contents entry. Old: "`godot_architecture_specification.md` — the Godot architecture specification (formerly under `designs/videogame/`)." New (pointer item 3's sentence with this edit's clause, one edit): "`godot_architecture_specification.md` — STALE REFERENCE by its own Status line (pre-d+σ). Do not implement from it; its autoload, signal and generator designs are each rejected by name in `04` §C.12."
  3. "`CURRENT.md` — **no `ui` row is added.**" (no edit).
  4. "`registers/handoffs/HANDOFF_GO.md`, Standing orders — one row: 'The player surface is specified by the oracle's readings (`decision/sheet.py`, `harness/play_surface.py`); the UI design set and the stale architecture specification are intent only.'" Its `source` cell: `11_GO_design_reference_disposition` (workplan v12 B03.21).
  "It adds no file, guard or corpus, edits nothing under `.designs/` or `.audit/`."
- WHERE: `godot/godot_architecture_specification.md` (the `## Status:` line); `godot/README.md` (the contents entry); `registers/handoffs/HANDOFF_GO.md` (Standing orders, one row).
- TESTS: none.
- FALSIFIER and CONTROL: "A port artifact, test or tool that opens a path under `.designs/systems/ui/` or names a v4 section as its source: `grep -rn "valoria_ui_ux" tools engine modules tests` prints nothing today … and must still." Control: `git diff --stat -- .designs .audit` empty.
- GATE: `python tools/currency_consistency_check.py` → exit 0 and `python tools/freshness_gate.py` → exit 0 ("clean after items 1–2 and 4"); `git diff --stat <batch-start-sha>..HEAD -- .designs .audit` → empty; the falsifier's grep → nothing.
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `godot/godot_architecture_specification.md` (the Status sentence, opened at `aa31fd2`), `godot/README.md` (the contents entry), `registers/handoffs/HANDOFF_GO.md` (Standing orders, `| order | source |`), `engine/season/decision/sheet.py`, `engine/season/harness/play_surface.py`; V12 B03.18 (`godot/README.md`, earlier: "after `11_GO_pointer_and_stale_text_resolutions.md`'s hash-equal items").
- GLOSSARY: none.
- COST and TIER: edit; `sonnet` (or `haiku` for the two sentence edits, the source's).
- LANDS IT: B03's producer; `Item: B03.21`, `[skip ci]`. GO reviews.

### B03.22 — twenty-seven stale substrings, two contract rows, a header that claims a check · 17_CENSUS_REST_3 A, B, C · BUILD · HASH EQUAL
- SOURCE: `proposals/17_CENSUS_REST_3_corrections.md` §A, §B (C-1, C-2), §C (C-3); its head ("one `[cleanup]` commit"); C3-N8 (22 rows), C3-L4. §D and §E are not carried (the part's "Not in this batch").
- ADVANCES: none of the nine; "a pointer that names the wrong file sends a session to code that is not the owner".
- INSTRUCTION (copied):
  **A. `engine/season/hole_register.yaml` — 27 exact substrings in 22 rows.** "One cause covers thirteen of them: `loop/effects.py` was split into `loop/effects_{army,combat,economy,founding,governance,information,migration,shared}.py`."
  | row · field | old substring | new substring |
  |---|---|---|
  | H-72 · site | `` `queries/readers.py` — `LedgerReader` `` | `` `queries/person_q.py` — `LedgerReader` `` |
  | H-138 · owner | ``loop/effects.py -- `_eff_transfer` `` | ``loop/effects_economy.py -- `_eff_transfer` `` |
  | H-138 · owner | `` `tests/test_season_shape.py:8103-8112`'s `norm` helper `` | `` `tests/test_season_shape.py`'s `norm` helper (two definitions, in the tests of the semantically-empty mutation) `` |
  | H-148 · site | `` `loop/effects.py::_eff_march` `` | `` `loop/effects_combat.py::_eff_march` `` |
  | H-152 · owner | `` `loop/effects.py::_eff_march` `` | `` `loop/effects_combat.py::_eff_march` `` |
  | H-152 · site | ``engine/season/loop/effects.py -- `_eff_march` `` | ``engine/season/loop/effects_combat.py -- `_eff_march` `` |
  | H-155 · site | ``(`isinstance(held.value, (int, float))`, `witness.py:189`)`` | ``(`isinstance(held.value, (int, float))`, in `loop/witness.py::_told_value`)`` |
  | H-207 · owner | `` `decision/options.py::aggregate_questions` `` | `` `decision/questions.py::aggregate_questions` `` |
  | H-210 · owner | ``(`workplans/valoria_master_workplan_v9_part6.md`, B-P)`` | ``(the v9 plan's part 6, B-P; retired, `FORK:c1374059`)`` |
  | H-230 · owner | ``(`workplans/valoria_master_workplan_v9_part5.md` IN-61:`` | ``(the v9 plan's part 5, retired, `FORK:c1374059`, IN-61:`` |
  | H-238 · owner | `` `workplans/valoria_master_workplan_v9.md` §0.5 (RULED 2026-10-13, *Relax exit rules*)`` | `` workplan v12's head rule P9 (RULED 2026-10-13, *Relax exit rules*; first written as the v9 head's §0.5, `FORK:c1374059`; carried by v11 and v12)`` (the source's new text names `workplans/valoria_master_workplan_v11.md` P9, deleted at v12's adoption: UNDECIDED (5)) `[ASSUMPTION: v12's head keeps P9's id — basis: `V12_STRUCTURE_part3.md` §7.1 item 4 carries P1 to P12 as head rules]` |
  | H-140 · owner | ``loop/effects.py -- `_eff_move` `` | ``loop/effects_migration.py -- `_eff_move` `` |
  | H-156 · owner | ``loop/effects.py -- `_eff_commit` `` | ``loop/effects_information.py -- `_eff_commit` `` |
  | H-43 · default | `` `loop/effects.py::_eff_petition` / `_eff_issue` `` | `` `loop/effects_information.py::_eff_petition` / `_eff_issue` `` |
  | H-105 · hole | `` `loop/effects.py::_rise` `` | `` `loop/effects_economy.py::_rise` `` |
  | H-164 · hole | `` `loop/effects.py::_rise` `` | `` `loop/effects_economy.py::_rise` `` |
  | H-164 · owner | ``loop/effects.py -- `_rise` `` | ``loop/effects_economy.py -- `_rise` `` |
  | H-158 · site | `` `loop/effects.py::_renewals` `` | `` `loop/effects_economy.py::_renewals` `` |
  | H-174 · owner | `loop/effects.py::_renewals` | `loop/effects_economy.py::_renewals` |
  | H-159 · site | `` `loop/effects.py::_oblige_term` `` | `` `loop/effects_shared.py::_oblige_term` `` |
  | H-126 · site | `seam/wrappers/sigma.py::faculty` | `seam/wrappers/pool.py::faculty` |
  | H-245, H-246, H-247 · site | `` `seam/wrappers/sigma.py::faculty` `` | `` `seam/wrappers/pool.py::faculty` `` |
  | H-245 · owner | `` `seam/wrappers/sigma.py::register_pool_addend` `` | `` `seam/wrappers/pool.py::register_pool_addend` `` |
  | H-172 · owner | `decision/options.py::belief_contradicts` | `epistemic.py::belief_contradicts` |
  | H-174 · owner | `queries/world_q.py::home_of` | `state/containment.py::home_of` |
  "Not edited, with the reason (so the next census does not re-raise them): H-220, H-224, H-357, H-358, H-361 ×3, H-79, H-213, H-153, H-222" (the source's reasons stand). Each new target is opened at the item's open (`grep -n "def <symbol>" <file>`); one that is gone (B01 or B02 moved it) is named in the commit body and its row left as is. (`pool.py::faculty` is renamed later, D-U1-08 in B05; that batch re-points these rows.)
  **B. `references/module_contracts.yaml`.** C-1, `combat`: "`build: unwired` → `build: gated`. … Replace the note with: `'built and typed-exported; reached from the season loop through composition role combat.fight (engine/season/seam/wrappers/combat.py). BUILD gated: a fight needs a challenge accepted or a violence context; the realm at seed 0 forms none in three seasons, the corpus executes it. The pre-season campaign driver this note used to describe was deleted at plan position 28-iii.'` `parity:` is [`11_GO_pointer…`] row 8's edit, not repeated here." B01 (lane A, `03_PC_duel_chain_reach`) makes computed play reach the duel: the note's clause "the realm at seed 0 forms none in three seasons" is re-read at the item's open (`python -m engine.season.harness.aperture 2 0`, the `fight` line) and written as the tree reads, two seasons (three in the source; A-114). C-2, `mass_battle`: "Add `sim_module: modules/mass_battle/` (the directory `composition_roles: mass_battle.resolve_field` targets); delete the comment ('`sim_module:` deliberately absent until the MB lane adds it'). Replace the note with its last bracket, restated: `'modules/mass_battle/ is the reachable closure (moved from systems/mass_battle/sim/ at plan position 31c, which keeps the harnesses and workbench); the one caller is engine/season/seam/wrappers/mass_battle.py through resolve_field. BUILD gated: the provider runs when ENCOUNTER admits a march at a held target (H-149).'` The sentence 'none of the realm marches do' is dropped."
  **C. `engine/season/write_matrix.yaml` — the header (C-3).**
  | line | old | new |
  |---|---|---|
  | header, the gate sentence | "`engine/season/shape.py`'s `write()` gate reads it" | "`engine/season/state/world.py::World.write` reads it through `data/matrix.py`" |
  | header, PROVENANCE | "The 28 rows carried over are extracted mechanically from §D3's markdown table; `python engine/season/register.py --verify-write-matrix` re-extracts and fails on drift." | "The 28 rows carried over were extracted from §D3's markdown table once. This file is now the head (CLAUDE.md §0.05: prose is reference); nothing re-extracts it, and a difference from §D3 is decided here and recorded in the row." |
  "The correction removes a claimed safeguard rather than building it."
- WHERE: `engine/season/hole_register.yaml` (22 rows' `site:`, `owner:`, `hole:`, `default:` substrings); `references/module_contracts.yaml` (`modules:` rows `combat` and `mass_battle`: `wiring.build`, notes, `sim_module:`, one comment); `engine/season/write_matrix.yaml` (header comment, two sentences).
- TESTS: none added; covering: `engine/season/tests/test_season_shape.py` ("for the register's schema") and `tests/valoria/test_wiring_validation.py`.
- FALSIFIER and CONTROL: "for each row of the table, `grep -cF '<old substring>' engine/season/hole_register.yaml` reads 0 and `grep -cF '<new substring>' engine/season/hole_register.yaml` reads at least 1 (27 pairs; the falsifier is a pair that reads otherwise)", run as one loop that asserts it checked 27 pairs (CLAUDE.md §0.1 pt 2). Control: `R(0)` hash equal to B03.21's (`site:` and `owner:` are read for non-emptiness only; `modules:` notes and `wiring.build` for vocabulary membership only; the matrix header is comment).
- GATE: `python -m engine.season.harness.register --check` → exit 0 and `--verify-citations` → unchanged; the 27-pair loop → 27 checked, 0 failed; `python tools/export_composition.py --check` → `OK` ("`gated` is a member of `wiring_vocabularies.build_states`"); `python -m pytest engine/season/tests/test_season_shape.py -q -k register` `[ASSUMPTION: selector]` → green.
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE every row and substring of §A (the substrings were read at `4995824` by the source; the loop is the check), `module_contracts.yaml` rows `combat`, `mass_battle`, `composition_roles: combat.fight`, `mass_battle.resolve_field`, `wiring_vocabularies.build_states` (`gated` present at `aa31fd2`); `write_matrix.yaml` header; V12 B03.17 (`hole_register.yaml`, earlier: H-159, H-172, H-230 `cite:`), B03.10, B03.12, B03.13 (`module_contracts.yaml`, earlier); V12 Batch B01 (the duel reach the C-1 note reads).
- GLOSSARY: none.
- COST and TIER: edit, one `[cleanup]` commit; `sonnet`, `high`.
- LANDS IT: B03's producer; `Item: B03.22`, `[skip ci]`.

### B03.23 — two register rows describe a tree that no longer exists · 06_FA_hygiene item 1 · BUILD · HASH EQUAL
- SOURCE: `proposals/06_FA_hygiene.md` "1. Two register rows describe a tree that no longer exists (R-13)"; ladder step 1 (the source's); closes F-FA-09 (part).
- ADVANCES: none of the nine.
- INSTRUCTION (copied): "`engine/season/hole_register.yaml` H-230 opens 'IN-61 … STOPPED AT ITS DESIGN-FIRST STEP, UNBUILT' and its `default:` says '`succeed` stays declined … no `successions` registry'. [In the tree]: `loop/effects_governance.py::_eff_succeed`, `data/rosters.py::SUCCESSIONS`, `state/gate.py::may_claim` and `death_subjects` (which names each seat `hold` a death closes so witnesses hold a claim about the seat) are all in the tree, and the batch card records IN-61, CP-T02-01 and CP-T02-02 as landed at `f9e4cef`. H-206 says the office and `hold` half of a death is unbuilt; `death_subjects` is that half. *Edit:* prepend each row's `hole:` and `cite:` with one sentence stating what landed and where, and set H-230's `default:` to the built state; keep the measured history below it (the register's own R0 rule: append, never rewrite the measurement)."
  The sentences `[ASSUMPTION: wording — basis: the source gives the facts and the form, not the text]`:
  - H-230, `hole:` and `cite:` prefix: "BUILT (IN-61, CP-T02-01, CP-T02-02, landed at `f9e4cef`): `succeed` is `loop/effects_governance.py::_eff_succeed` over `data/rosters.py::SUCCESSIONS`; the claim gate is `state/gate.py::may_claim`; a death names each seat `hold` it closes (`state/gate.py::death_subjects`). The text below is the row's history." `default:`: "`succeed` executes through `_eff_succeed` over the `successions` registry (`SUCCESSIONS`); the declined default below it is history."
  - H-206, `hole:` and `cite:` prefix: "BUILT IN PART (landed at `f9e4cef`): the office and `hold` half of a death is `state/gate.py::death_subjects`, which names each seat `hold` a death closes so witnesses hold a claim about the seat. The text below is the row's history."
  Each symbol is opened at the item's open (`grep -n "def _eff_succeed\|^SUCCESSIONS\|def may_claim\|def death_subjects"`); `git cat-file -e f9e4cef` succeeds at `aa31fd2`.
- WHERE: `engine/season/hole_register.yaml` (H-230 `hole:`, `cite:`, `default:`; H-206 `hole:`, `cite:`).
- TESTS: none; covering: `engine/season/tests/test_season_shape.py -k register` `[ASSUMPTION: selector]`.
- FALSIFIER and CONTROL: a prepended sentence that names a symbol `grep` does not find, or a row whose measured history is shortened (`git diff` shows only additions to the two rows, and one replaced `default:`). Control: `R(0)` hash equal to B03.22's.
- GATE: "`python -m engine.season.harness.register --check` after item 1" → exit 0; `--verify-citations` → exit 0.
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `loop/effects_governance.py::_eff_succeed`, `data/rosters.py::SUCCESSIONS`, `state/gate.py::may_claim`, `::death_subjects`, `hole_register.yaml` H-206, H-230 (each opened at `aa31fd2`); V12 B03.17 (H-230 `cite:` appended, earlier), B03.22 (H-230 `owner:`, earlier).
- GLOSSARY: none.
- COST and TIER: edit (text and data); `sonnet` (the source's tier), `medium`.
- LANDS IT: B03's producer; `Item: B03.23`, `[skip ci]`.

### B03.24 — every refusal of `confer` and `establish` names its clause · 06_FA_hygiene item 2 · BUILD · HASH EQUAL
- SOURCE: `proposals/06_FA_hygiene.md` "2. Three refusals name no clause (R-14, H-252)"; ladder step 4 (the source's: `_req_release` and `_req_revoke` are the precedent); closes F-FA-10 (part); bears on H-252 (its row is not edited by the source).
- ADVANCES: none of the nine; `aperture`'s DECIDING READ names a clause where it printed `no-read`.
- INSTRUCTION (copied): "`_req_confer` and `_req_establish` return a bare `False` at each of their clauses (`loop/predicates.py`), so `aperture`'s DECIDING READ prints `no-read` (`establish` 7 of 7 and `release` 15 of 15 at seed 0, two seasons). `_req_release` and `_req_revoke` already route each refusal through `_refuse(clause, ids)`, which writes a trace row and nothing else. *Edit:* each `return False` in the two predicates becomes `return _refuse("<the clause, in the words of its own comment>", f"{a.actor} …")`. No Event, no claim, no hash. `harness/aperture.py`'s `no-read` class then reads the trace row for a predicate row." Step 0 (§5.7 SITE form, because B01's lane-A rebase resolved 33 shared files): open `_req_confer` and `_req_establish` on the base and list each `return False` with its comment in the commit body; each becomes one `_refuse` call.
- WHERE: `engine/season/loop/predicates.py` (`_req_confer`, `_req_establish`).
- TESTS: `test_every_confer_and_establish_refusal_names_a_clause` in `engine/season/tests/test_predicate_refusals.py` `[ASSUMPTION: test name and file; the item creates it, E-3]`: over `build_realm(0)` and one season, every `confer` and `establish` refusal's trace row carries a non-empty clause; asserts it checked at least one refusal (`checked >= 1`); written before the edit and read red (bare `False` writes no trace row).
- FALSIFIER and CONTROL: an `establish` refusal still read as `no-read`. Control: `R(0)`, `R(2)` hashes equal to B03.23's ("No Event, no claim, no hash").
- GATE: `PYTHONHASHSEED=0 python -m engine.season.harness.aperture 2 0` → "printing a clause in place of `no-read` for `establish`" (and for `confer` where it refuses); `python -m pytest engine/season/tests/test_predicate_refusals.py -q` → green; `R(0)` hash equal to B03.23's.
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `loop/predicates.py::_req_confer`, `::_req_establish`, `::_refuse`, `harness/aperture.py` (DECIDING READ); V12 Batch B02 (`aperture`'s added lines, B02.17, B02.18).
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B03's producer; `Item: B03.24`, `[skip ci]`.

### B03.25 — `faction_q.superiors`, which nothing calls · 06_FA_hygiene item 3 · BUILD · HASH EQUAL
- SOURCE: `proposals/06_FA_hygiene.md` "3. Unreached query surface (R-10)", with its U6 R-A reconciliation (C3-V3: `holdings` kept, `04` §B.6.1 names it); ladder step 5 (the source's); closes F-FA-11 (part).
- ADVANCES: none of the nine.
- INSTRUCTION (copied): "`grep -rn "\.superiors(\|faction_q\.holdings(" engine/season --include=*.py` outside tests returns nothing; `purview` and `subordinates` are read only by `harness/interactions.py`. *Edit:* delete `faction_q.superiors` with its tests (`engine/season/tests/test_faction_q.py`'s `test_superiors_of_a_person_with_no_oblige_is_empty`, and the `superiors` assertion of `test_superiors_and_subordinates_read_a_hand_built_oblige_in_both_directions`, whose `subordinates` half stays; the `holdings` case stays). **keep the standalone `faction_q.holdings`** … Keep `purview` and `subordinates`. Keep `head`'s `Tenure.degree` branch, which `04` §B.6.1 and §F.34 name, and add one line at the site: unreachable until something writes a degree on a `commit`." Added to the copy: the name `superiors` leaves the two docstring lists that enumerate the module (`queries/faction_q.py`'s module docstring, `queries/__init__.py`'s `faction_q` line), so no list names a deleted function; the narrowed test keeps its name `[ASSUMPTION: a renamed test is not in the source]`.
- WHERE: `engine/season/queries/faction_q.py` (`superiors`; `head`'s comment line; the module docstring's list); `engine/season/queries/__init__.py` (the `faction_q` line); `engine/season/tests/test_faction_q.py` (one test deleted, one narrowed).
- TESTS: the narrowed `test_superiors_and_subordinates_read_a_hand_built_oblige_in_both_directions` (its `subordinates` half) green.
- FALSIFIER and CONTROL: "For item 3, a grep that finds a caller is the falsifier, run before the deletion": `grep -rn "superiors(" engine modules tools --include=*.py` outside `engine/season/tests` → only the definition. Control: `R(0)` hash equal to B03.24's.
- GATE: `python -m pytest engine/season/tests/test_faction_q.py -q` → green ("the `engine/season/tests` files that import the deleted functions pass"); `python -c "import engine.season.queries.faction_q"` → exit 0.
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `queries/faction_q.py::superiors`, `::holdings`, `::head`, `::purview`, `::subordinates`; `tests/test_faction_q.py` (the two tests named, at `aa31fd2`).
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `medium`.
- LANDS IT: B03's producer; `Item: B03.25`, `[skip ci]`.

### B03.26 — contract rows for a retired faction · 06_FA_hygiene item 5 · BUILD · HASH EQUAL
- SOURCE: `proposals/06_FA_hygiene.md` "5. Contract rows for a retired faction (R-09)"; ladder step 2 (the source's); ED-IN-0232; closes F-FA-12 (part).
- ADVANCES: none of the nine.
- INSTRUCTION (copied, one correction): "`references/module_contracts.yaml` `modules:` carries `faction_state` and `faction_politics` with stored state ('faction stats 1-7', 'Standing', 'Coup posture'), Key-registry vocabulary and `doc:` pointers into `.designs/`. The stat-vector faction was deleted at plan position `29b`, the Key substrate retired by ED-IN-0232, and no code under `engine/season/` or `modules/` implements either row. Known readers of the names: `tools/build_engine_atlas.py`; `engine/season/manifest/registry.py` parses the `modules:` list. *Edit:* in one commit, reduce each of the two rows to its `module:` name and a one-line note (a faction is `engine/season/queries/faction_q.py`'s view; it has no contract, no state and no composition role), and re-point or drop `build_engine_atlas.py`'s `VALORIA_CONTRACTS` entry. Before the edit, list every reader of the two rows' fields (`grep -rn "faction_state\|faction_politics" tools engine tests`) and name them in the commit."
  The correction (fact 2 at part 4's head): each row also **keeps its `wiring:` block** unchanged, because `tools/export_composition.py::validate_wiring` refuses "a module contract without a `wiring:` block" and its `--check` is blocking; and `faction_state` keeps its `module:` name because "other contracts' `with:` joins name it" (the row's own comment). Its `accounting_phase` line is already `[settlement_accounting]` (B03.13) and goes with the row's other keys. Whether `doc:` stays: the workbench node-state and the census read `doc:` by code (the row's own comment); the readers' list decides, and the commit names which `[ASSUMPTION: keep `doc:` if a reader the grep lists reads it — basis: the row comment "`doc:` is read by CODE"]`.
- WHERE: `references/module_contracts.yaml` (`modules:` rows `faction_state`, `faction_politics`); `tools/build_engine_atlas.py` (`VALORIA_CONTRACTS`, the entry naming either).
- TESTS: none added; covering: `tests/valoria/test_wiring_validation.py`, and any test the readers' grep lists.
- FALSIFIER and CONTROL: a reader the grep lists that fails on the narrowed row (a `KeyError` on `state:`, `transitions:` or `doc:`); `python tools/export_composition.py --check` not OK. Control: `R(0)` hash equal to B03.25's.
- GATE: `python tools/export_composition.py --check` → `OK — 17 role(s) … wiring valid for 23 module(s)`; `python -c "import engine.season.manifest.registry as r; print(len(r._contracts()))"` → the same row count as before the edit (the parse survives); "`tools/valoria_local.py --staged` after items 5 and 6" → green; `python tools/build_engine_atlas.py` → runs as its caller runs it (`grep -rn build_engine_atlas .github tools skills` names the caller; none → it is run bare) `[ASSUMPTION: the atlas tool's invocation — basis: not opened]`.
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `module_contracts.yaml` rows `faction_state`, `faction_politics` (with `wiring:` blocks, opened at `aa31fd2`); `tools/export_composition.py::validate_wiring`; `tools/build_engine_atlas.py::VALORIA_CONTRACTS`; `manifest/registry.py::_contracts`; V12 B03.13 (`faction_state.accounting_phase`, earlier), B03.22 (the same file, earlier).
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `medium`.
- LANDS IT: B03's producer; `Item: B03.26`, `[skip ci]`.

### B03.27 — a process row that orders work no plan schedules · 06_FA_hygiene item 6 (first half) · BUILD · HASH EQUAL
- SOURCE: `proposals/06_FA_hygiene.md` "6. Two process rows" (R-15); its second row (the B10-17 card's CP-T09-06 wording) is not carried: UNDECIDED (6).
- ADVANCES: none of the nine.
- INSTRUCTION (copied): "`registers/handoffs/HANDOFF_FA.md` row 3 orders authoring a merge into a quarantined `.designs/` file 'in the same pass as E11', in the cell that says v9 schedules none (R-15). *Edit:* delete the row; ED-FA-0021 stays ratified as intent, and what it intends is built as a fold by FA-P1." The row is the Open table's "§1.0d Kaochengfa merge + E11 counter-mechanic authoring" (`ED-FA-0021`, `faction_politics_v30.md:137`) at `aa31fd2`.
- WHERE: `registers/handoffs/HANDOFF_FA.md` (Open table, one row).
- TESTS: none; covering: the tests that read the handoff files (`grep -rl HANDOFF_FA tests`; run each, or none if none).
- FALSIFIER and CONTROL: a remaining Open row that names the `.designs/` merge. Control: `git diff` shows one deleted row and nothing else in the file.
- GATE: "`tools/valoria_local.py --staged` after items 5 and 6" → green; `python tools/currency_consistency_check.py` → exit 0.
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `registers/handoffs/HANDOFF_FA.md` Open row "§1.0d Kaochengfa merge + E11 counter-mechanic authoring".
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `low`.
- LANDS IT: B03's producer; `Item: B03.27`, `[skip ci]`.

### B03.28 — `Office.body_function`, written and never read · 17_CENSUS_REST_1 D1 row 2 · BUILD · HASH MOVER(encoding)
- SOURCE: `proposals/17_CENSUS_REST_1_deletions.md` "D1 — six dead fields", row 2; D-04 (`V12_STRUCTURE.md` §1: "an item that adds, removes or renames a field or class of a hashed carrier is declared `HASH MOVER(encoding)`, is co-batched with a re-pin, and its control is tallies-equal"); placed last in this half (UNDECIDED (1), (2)).
- ADVANCES: none of the nine; one unread field leaves a carrier (`04` ID-13: "a field nothing reads is not a field").
- INSTRUCTION (copied): "`engine/season/state/carriers.py`: delete the field [`Office.body_function`]; delete the two-line write [`self.body_function = BODY_FUNCTION[self.body]` and its guard]; drop `BODY_FUNCTION` from the import. **Keep** `data/rosters.py` `BODY_FUNCTION` and the `function:` map (`rosters.yaml`)." "test edit: none (`test_season_shape.py`'s office test reads the roster, not the field)." Added by this plan: the commit body says "encoding mover: `Office`'s field names enter `World.content_hash()` (`state/world.py::_object_head`; `carriers.py::Office`'s own `establishment` note); behaviour unchanged; re-pinned at B03.99".
- WHERE: `engine/season/state/carriers.py` (`Office.body_function`; the write in `Office`'s post-init; the `BODY_FUNCTION` import).
- TESTS: none added; covering: `engine/season/tests/test_season_shape.py -k office` (the source's "file to run"); `engine/season/tests/test_go07_canonical_digest.py`.
- EXPECTED RED UNTIL B03.99 (E-1, under `[skip ci]`): every test that pins a realm hash through `engine/season/tests/_realm_goldens.py` (`BUILD`, `SHIPPED`), among them `test_go07_canonical_digest.py`'s shipped-pin tests; the `CENSUS` assertions stay green (tallies).
- FALSIFIER and CONTROL: a reader the grep missed — `grep -rn "body_function" engine modules tools tests --include=*.py` → no read outside the deleted lines, and the import of `engine.season.state.carriers` succeeds. Control (D-04, tallies-equal): `R(0)` acts and log length equal to B03.27's; the hash differs, and only because a field name left the encoding: with the field restored in a scratch worktree (and nothing else), `R(0)` reproduces B03.27's hash exactly.
- GATE: `python -m pytest engine/season/tests/test_season_shape.py -q -k office` → green; `R(0)` → hash moved, `acts` and `log` equal to B03.27's; the scratch restore → B03.27's hash; `python -m engine.season.harness.register --requirements` → unchanged from B02's close.
- HASH MOVERS: every content hash of a world holding an office, by encoding only (`Office`'s field list). Declared; B03's one re-pin at B03.99.
- DEPENDS ON: EXISTS-IN-TREE `state/carriers.py::Office.body_function`, the `BODY_FUNCTION` import and write; `data/rosters.py::BODY_FUNCTION` (kept); `state/world.py::_object_head`, `World._STATE_COLLECTIONS` (`offices` hashed); V12 B03.09 (REST_1 D1's other rows, earlier).
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B03's producer; `Item: B03.28`, `[skip ci]`; the re-pin is B03.99's.

---

### This half's serial edges (E-11: written after the position table)

SERIAL EDGES: within the batch (`→` is landing order; the reason is the shared file or the read):
  `engine/engine_params/value_pointer_links.json` and `sim_params.json`: B03.01 (deleted) → B03.07 → B03.14 → B03.15 (each rebuild by `tools/export_sim_params.py --build`, never by hand); `tools/export_sim_params.py`: B03.14 → B03.15 → the second half's ER-GF9 entry (the intake `:112`, edit set "the exporter source").
  `references/restructure_ledger.md`: B03.01 → B03.03 → B03.07 (rows appended in this order).
  `modules/mass_battle/hierarchy/units.py`: B03.05 → B03.06 → B03.09. `systems/characters/sim/conviction.py`: B03.05 alone (three sources, one commit).
  `references/module_contracts.yaml`: B03.10 → B03.12 → B03.13 → B03.22 → B03.26 (`faction_state.accounting_phase`: B03.13 → B03.26).
  `engine/season/loop/driver.py`: B03.11 → B03.12 (one name added to the list B03.11 re-derived) → B03.16.
  `engine/season/requirements.yaml` (the settlement row's note): B03.13 (the contracts sentence) → B03.17 (the `restore` clause).
  `engine/season/hole_register.yaml`: B03.07 (H-326) → B03.17 (nine `cite:` appends) → B03.22 (22 rows' substrings) → B03.23 (H-230, H-206 prefixes) → the second half's rows. H-230 alone: B03.17 `cite:` (append) → B03.22 `owner:` → B03.23 `hole:`, `cite:` (prepend), `default:`.
  `CURRENT.md`: B03.17 → B03.18. `godot/README.md`: B03.18 (the `res://` sentence) → B03.21 (the contents entry).
  `engine/season/tests/test_go07_canonical_digest.py`: B03.18 (notes and `old` pieces) → B03.28 (its shipped pins red) → B03.99 (re-pin through `_realm_goldens.py`).
  `engine/season/loop/predicates.py`: B03.24 → the second half's H-291 entry (the intake `:227`, "item 2 already edits `_req_establish`").
  `engine/season/state/carriers.py`: B03.28 last; the re-pin is B03.99.
With other batches, by file (U3 §5.1 and CIP §3.2 where they hold the row; `→` is batch order):
  `references/module_contracts.yaml`: B03 → B03g (GO-11's `parity:` and `golden_path:`, B03.20) → the later editors U3 §5.1 lists.
  `references/restructure_ledger.md`: B02 → B03 → B13 (`CI-09`'s `pc_engine.py` row).
  `engine/season/hole_register.yaml`: B03 → B05 → B10 → B11 → … (U3 §5.1). `engine/season/requirements.yaml`: B02 → B03 → B09 → B11 → B17 → B26.
  `engine/season/state/carriers.py`: B03 → B04 (`Claim.lap`, `Person.traits`) → B05 → … (U3 §5.1). `engine/season/state/world.py`: B03 → B06 → B09 → B12 → B41. `engine/dice_engine/dice_engine.py`: B03 → B05 → B06.
  `engine/season/loop/driver.py`, `loop/deliberate.py`, `seam/wrappers/sigma.py`, `queries/world_q.py`, `queries/person_q.py`: B03 → B03a (`CI-02`, comments) → B04 → … ; `engine/season/data/files.py`: B03 → B03c (`files.REALM_PY`) → B12.
  `tools/export_sim_params.py`: B03 (B03.15 reads `harness/populated.py::build_realm`) → B03c (`CI-07` moves the builder; the one path line in `_realm_arm_records` is re-pointed there).
  `modules/mass_battle/hierarchy/units.py`: B03 → B16L → B16M (the renames) → B32. `systems/threadwork/sim/`: B03 (B03.07) → B03 second half (`09_WR_threadwork_module` edit 3) → B35.
  `engine/season/tests/test_go07_canonical_digest.py`: B02 → B03 → B04 (read green) → B06. `unified/U1_GLOSSARY.md`: B03 (B03.18) → B04 → … .
PARALLEL: S3, alone; no file is shared with an open batch.

### This half's file census (file · items in landing order)

| file or symbol | items |
|---|---|
| `references/module_contracts.yaml` | B03.10, B03.12, B03.13, B03.22, B03.26 (B03.20 points at B03g) |
| `engine/season/hole_register.yaml` | B03.07, B03.17, B03.22, B03.23 |
| `engine/engine_params/sim_params.json` (re-derived) | B03.07, B03.14, B03.15 |
| `tools/export_sim_params.py` | B03.14, B03.15 |
| `references/restructure_ledger.md` | B03.01, B03.03, B03.07 |
| `modules/mass_battle/hierarchy/units.py` | B03.05, B03.06, B03.09 |
| `engine/season/loop/driver.py` | B03.11, B03.12, B03.16 |
| `engine/season/requirements.yaml` | B03.13, B03.17 |
| `CURRENT.md` | B03.17, B03.18 |
| `godot/README.md` | B03.18, B03.21 |
| `engine/season/tests/test_go07_canonical_digest.py` | B03.18 (B03.28 reddens its pins; B03.99 re-pins) |
| `engine/season/tests/test_season_shape.py` | B03.16 |
| `engine/season/state/carriers.py` | B03.28 |
| `engine/season/data/cast.py` | B03.01, B03.02 |
| `engine/season/queries/world_q.py` · `person_q.py` · `faction_q.py` | B03.03 · B03.04 · B03.25 |
| `engine/season/seam/wrappers/sigma.py` | B03.12 |
| `engine/season/loop/deliberate.py` · `loop/predicates.py` | B03.16 · B03.24 |
| `systems/characters/sim/conviction.py` · `systems/fieldwork/sim/knots.py` · `calibrate_generics.py` | B03.05 |
| `modules/mass_battle/perimeter.py` · `tools/ci_golden_modes_check.py` | B03.06 |
| `systems/threadwork/sim/` (`threadcut.py`, `co_movement.py` deleted; `__init__.py`, `operations.py`) · `registers/mechanics_index.yaml` | B03.07 |
| `engine/dice_engine/dice_engine.py` | B03.09 |
| `references/action_vocabulary.yaml` | B03.13 |
| `godot/godot_conversion_strategy_v1.md` · `unified/U1_GLOSSARY.md` | B03.18 |
| `godot/godot_architecture_specification.md` · `registers/handoffs/HANDOFF_GO.md` | B03.21 |
| `engine/season/write_matrix.yaml` (header) | B03.22 |
| `tools/build_engine_atlas.py` | B03.26 |
| `registers/handoffs/HANDOFF_FA.md` | B03.27 |
| `architecture/meta/04_CODE_ARCHITECTURE.md` | B03.19 (HELD: Jordan's merge only) |

Hot files of U3 §1.1 this half edits: `world_q.py` (B03.03), `person_q.py` (B03.04); no other batch is open at S3.

Last item written in this part: B03.28. The second half begins at B03.51.
