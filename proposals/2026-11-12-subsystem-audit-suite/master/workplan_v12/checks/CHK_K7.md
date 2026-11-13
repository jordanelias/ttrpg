# CHK_K7 — check lane K7 (Sonnet), workplan v12 parts 29 to 32 and their continuations

## Status: WORK ORDER (a check lane's table, one round; resolves nothing at runtime, CLAUDE.md §0.05; deleted with the suite)

**Scope (the brief of `chk_7.txt`, not `V12_STRUCTURE_part3.md` §10.1's grouping, which gives K7 parts 23 to 27):** `workplan_v12_part29.md`, `_part29_cont.md`, `_part30.md`, `_part30_cont.md`, `_part31.md`, `_part31_cont.md`, `_part32.md`, `_part32_cont.md`. Eight batch blocks: B21d-fa-arc, B41-go-port-gate, B11F1-flow-se (29); B20-mb-orders, B25-fi-questioning (30); B27-sc-proceedings (31); B37-happenings, B11F2-flow-in (32). 137 item headings, 137 position rows.

**Rulers used:** `V12_STRUCTURE.md` §5 (via `_part2` §5.2/5.3/6), `V12_STRUCTURE_part3.md` §10.1, `V12_STRUCTURE_part4.md` E-1..E-15 (they win), `workplan_v12_part2.md` §1.3 (the after-lists, HEAD `7257911`) and §11 (the conflicts register). Scripts: scratchpad `k7/parse.py`, `form.py`, `fieldcheck2.py`.

Sections are appended as each check finishes. Findings table at the end of the file (worst first) is written last.

---

## 1. Check 1, forms (script `form.py`, parsed from the files)

| batch | head lines §5.2 in order | INVOCATION exact | `GATE: Batch` = part 2's after-list | positions = items | `.99` position | one boundary row, exact |
|---|---|---|---|---|---|---|
| B21d | yes | yes | yes (2 of 2) | 10 = 10 | B21d.99 "re-pin and close readings" | yes |
| B41 | yes | yes | yes (8 of 8; B17, B20 added by H2 HD-10) | 15 = 15 | B41.99 titled "the close's readings (EQUAL)" | yes |
| B11F1 | yes | yes | yes (1 of 1) | 8 = 8 | B11F1.99 | yes |
| B20 | `SERIAL EDGES` present (carries "(written after the position table, E-11)") | yes | yes (10 of 10) | 23 = 23 | B20.99 | yes |
| B25 | order differs: COST, EST come before SERIAL EDGES, PARALLEL | yes | yes (6 of 6) | 22 = 22 | B25.99 | yes |
| B27 | yes | yes | yes (6 of 6) | 28 = 28 | B27.99 | yes |
| B37 | yes | yes | yes (11 of 11; B29 added by H2 HD-11) | 19 = 19 | B37.99 | yes |
| B11F2 | yes | yes | yes (3 of 3) | 12 = 12 | B11F2.99 "close readings (EQUAL: nothing re-pinned)" | yes |

Every block names its in-flight lane file (`HANDOFF_FA/GO/SE/MB/FI/SC/IN.md`, Open table; B11F1 is SE alone, not a two-lane batch).

## 2. Check 2, fields of §5.3 (script `fieldcheck2.py`; 122 full-form items = BUILD, DESIGN-FIRST, CONTENT and HELD-with-HASH; 12 fields each)

Grade rule used: ABSENT = field line missing; THIN = under 40 characters and not `none`, or "as B21d.07"-style reference, or a COST line with no tier; `.99` positions grade GATE/HASH MOVERS/DEPENDS ON/ADVANCES/GLOSSARY by reference as PRESENT (the form of E-1). NAMES and IDS are conditional and not counted. The 15 POINTER/READING/HELD-without-HASH items (B41.01, B41.12, B11F1.07, B20.18, B20.22, B25.07, B25.08, B25.12, B25.18, B25.21, B37.07, B37.17, B37.18, B11F2.01, B11F2.04) are graded under E-5/§5.3 as pointers/readings (3 to 8 lines, target, gate) and are all present as such.

| field | PRESENT | THIN | ABSENT |
|---|---|---|---|
| SOURCE | 119 | 3 (B21d.08, B21d.09, B27.08) | 0 |
| ADVANCES | 112 | 10 | 0 |
| INSTRUCTION | 121 | 0 | 1 (B27.27, a READING) |
| WHERE | 121 | 0 | 1 (B27.27) |
| TESTS | 120 | 1 (B27.24) | 1 (B27.27) |
| FALSIFIER and CONTROL | 119 | 2 (B21d.08, B21d.09: "as B21d.07") | 1 (B27.27) |
| GATE | 120 | 2 (B21d.08, B21d.09: "as B21d.07.") | 0 |
| HASH MOVERS | 120 | 1 (B20.06 "as B20.05") | 1 (B27.27) |
| DEPENDS ON | 113 | 8 | 1 (B27.27) |
| GLOSSARY | 105 | 16 (a row name and a step number only) | 1 (B27.27) |
| COST and TIER | 122 | 0 | 0 |
| LANDS IT | 121 | 0 | 1 (B27.27) |

B27.27 is a READING that carries a position-table row, an item heading with HASH EQUAL and four fields (SOURCE, ADVANCES, GATE, COST); the other READING items (B20.22, B25.07, B25.21, B37.17, B37.18, B41.12) carry no fields at all, and all READING items have no COST/TIER line, so check 8 grades them "reading, tier not stated" (B27.27 alone says `haiku`; B20.22 says `haiku` inline).

Per batch, PRESENT/THIN/ABSENT cells of the 12 fields over the full-form items: B21d 108/12/0 (10 items); B41 155/1/0 (13); B11F1 81/3/0 (7 incl. B11F1.99); B20 247/5/0 (21); B25 197/7/0 (18); B27 315/13/8 (27); B37 190/2/0 (16); B11F2 120/0/0 (10).

THIN items an agent cannot run from the item alone (check 10) are listed in §9.

## 3. Check 3, gates (scripts `gates.py`, `deps.py`, a grep for season counts)

- **Every named file in a GATE resolves** to the tree (`git ls-files`) or to a `NEW` path of an earlier item. Lists: B21d: `harness/clocks.py` (B21d.04), `test_cr89_clocks.py` (B21d.02), `test_cr90_clock_marks.py` (B21d.04), `test_cr88_duty_of_office.py` (B21d.05), all created before the gate that reads them. B41: `tools/export_oracle_pins.py`, `harness/port_oracle.py`, `test_oracle_pins.py` (B41.06), `test_go12_providers.py` (B41.02), `test_go10_refusal_values.py` (B41.03), `test_surface_trace.py` (B41.05); `harness/scenarios.py` and `test_scenarios_runner.py` come from B11 (reachable: B41 after B34 after B16 after B11); `engine/tests/test_draw.py`, `test_fmath.py` from B06. B20: `field_scene.py`, `test_field_scene.py` (B20.11/.05); `scene.py`/`test_scene_contract.py` from B34 (in B20's after-list); `tools/export_troops.py` from B17 (in list); `tests/valoria/test_conditional_orders.py`, `test_mass_battle_signals.py`, `test_army_battle.py`, `test_army_verbs.py` exist (`git ls-files`). B25: `test_vm_s2_a/b/c/d_*.py` created by B25.02/.04/.09/.19; `test_sc_hearing_evidence.py` by B24 (opened: part22 lines 396-412); `test_conclusion.py` by B11 (part17); `test_task_draw.py` by B07. B27: `test_sc_hearing_sitting.py` by B24; `engine/season/tests/test_sc02_22b_standing_crossing.py` exists (the script's "MISSING" was a path-prefix artefact). B37: `boot/realm.py` does not exist today and is B03c's (B37 follows B03c transitively); the two new tests are B37.15/.16's. B11F2: `test_cr17_odds_weighting.py` and `test_strife_flows.py` exist; `test_cr105_choice_stakes.py` is "or a new" file in HELD B11F2.11.
- **No gate reads past two seasons.** Grep over all eight files for season counts 3 to 24 in gate lines: every source figure of three, four, six, eight, twelve or forty seasons is rewritten at two and says so (B21d "clocks 2 0 1 2"; B25 R1 "four seasons in the source; A-114"; B27.01, .07, .09 "two seasons (six/three/four in the source)"; B37 "two seasons (UNDECIDED (3); 12 seasons in the source)"; B11F2 horizon "two seasons"). One residue that is not a gate: B21d's DIALS/UNDECIDED 2 say the four Church-Influence band flips cannot be crossed in two seasons and leave the question to B98/B99 (finding F-19).
- **No gate is a `## Status:` line or a count read off a document.** The design items B21d.01, B11F1.06 gate on `test -f` plus `grep -c "^## Status: PROPOSED" <file>` → 1, and B27.14/.15/.19/.20/.22/.23 on "the file exists, `## Status: PROPOSED`, states (1) to (n)": allowed for DESIGN-FIRST by `_part2` §5.8, and read by a `ners` critic. B27.08 reads `grep -c "deed:argument.held" engine/season/rosters.yaml` equal to the `argument.won` count (a registry the code reads; an equality that could be wrong, thin).
- **BATCH GATE lines**: all eight carry `register --check`, `--requirements`, `m1_acceptance --summary`, `tests_for_diff.py --base`, `PYTHONHASHSEED`, and the §5.12 close record (script over each block).
- **Gate arms that cannot be wrong** (not fixed): B20.06 and B20.14 each end their GATE on "the seed-2 one-season realm hash → moved or equal, recorded"; their pytest arm is falsifiable. B27.12's GATE adds `modules/social_contest` to a pytest line: that directory holds `__init__.py` and `roll.py` only, so the arm collects nothing (the item's test file still runs). 14 item-level seeded commands in 11 items carry no `PYTHONHASHSEED=0` prefix (B41.07 `port_oracle`; B20.12, B20.21 `field_scene`; B25.03, .14, .15 `aperture 1 s`; B37.05, .10, .16; B11F2.03, .05) against `_part2` §5.8 and each batch's own header line (which says the prefix is on every seeded command); not edited.

## 4. Check 4, dependencies

- `DEPENDS ON` lines: 80 items carry EXISTS-IN-TREE and V12 marks, 39 carry V12 marks only, 2 carry EXISTS-IN-TREE only; no item uses `MISSING` (and no item is `BLOCKED`).
- **EXISTS-IN-TREE opened at the symbol:** 444 backticked tokens were parsed from the 121 lines that carry the mark and each symbol was searched in the named file (script `deps.py`); 28 tokens the script could not place were each re-opened by `grep` over `engine/ modules/ tools/`. 26 are in the tree (e.g. `world_q.docket_question` at `world_q.py:401`, `governing_hold` `:2539`, `person_q.held_against` `:85`, `Fixtures.odds_weighting` `fixtures.py:971`, `Fixtures.field_casualty_model` `:745`, `resolution.tracing`/`trace_event` in `modules/mass_battle/resolution.py:8,25`, `feigned_retreat_recognized` `orchestration.py:2101`, `Person.heritage` `carriers.py:826`, `guard_weight` `world_q.py:1543`, `restrained` `:1766`, `sworn_to` `gate.py:473`). **Two are not in the tree and are marked as if they were:** `stand_draw` (B20.10: `orchestration.py::stand_draw`; no hit in `engine/ modules/`; created by B19.54, part27 position table) and `rosters.yaml: task_fraction` (B25.20: no hit; created by the B07 item at part10_cont2:75-78).
- **`V12 <handle>` resolution (script `vref.py`):** every `Bnn.mm` handle in DEPENDS ON, GATE, TESTS, INSTRUCTION, SOURCE, ADVANCES, WHERE and FALSIFIER resolves to a position row in some part (0 unresolved). Cross-batch handles all belong to a batch in the cited batch's transitive after-list except B25.14's step 6 naming B26.01 (a forward note with its control: "until then the press term reads nothing"). Same-batch handles that point to a later position are forward notes ("lands with", "until B27.07 the Failure band writes nothing", "turns green at") in 49 of 52 cases; three are listed in §5.

## 5. Check 5, back edges

- Position-table `gates on` cells (script `posgates.py`): no cell gates on a later position, with four exceptions: B20.18, B25.08, B25.18 (POINTER rows whose gate is the built item they point at: B20.19, B25.14, B25.19; H2 §1.1 accepts pointer rows pointing forward) and B27.17.
- **B27.17** is `HELD (Batch B25 closed)` and gates on Batch B25, which is not in B27's after-list (H2 §1.1 HD-08 declined the edge: B25 and B27 open in S16; fallback "B27.17 moves to B32's tail"). Recorded, not a new finding.
- **B11F2.10** is `HELD (Batch B21s-strife-supply and Batch B21b-fa-war closed)`: B21s closes at S18, B11F2 at S17, and neither B21s nor B21b is in B11F2's after-list. H2's list of four forward `gates on` cells (§1.1) does not name it. A HELD row leaves the plan with its trigger, so it executes nothing in B11F2, but the trigger is a later batch (F-7).
- **B20.12** lists `V12 B20.19` under DEPENDS ON for `auto`'s window decider and says it "lands after"; the item is complete without it (F-6).
- B25 gates on B24 and B12c, B11; its steps reach B26.01 only as a note.
- Cut batches: B11F1 depends on B12c (S15) only; B11F2 on B09, B10, B11F1; no item of either depends forward except as above.
