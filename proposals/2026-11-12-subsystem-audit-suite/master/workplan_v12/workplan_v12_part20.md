# Workplan v12 — part 20: Batch B12a-world-motion-and-ground, second half (from `B12a.51`) and its boundary row

## Status: PROPOSED (a body part of workplan v12, drafted under `master/workplan_v12/`; unratified input to `methodology-execute`'s 0.1 stop until Jordan adopts v12, `V12_STRUCTURE_part3.md` §8; resolves nothing at runtime, CLAUDE.md §0.05; not canon)

## Written against: the working tree at `aa31fd2` (branch `ccr-62958c70-0kjhsw`), read 2026-11-12; author lane A20 of `master/workplan_v12/V12_STRUCTURE_part2.md` §4.2. Every item is written against the tree as the earlier batches and the first half of this batch leave it: the builder is `engine/season/boot/realm.py` after B03c (`CI-07`); the season's pass is the *lap* after B04 (`PCR-4`); the keyed draw owner is `draw_factory` after B06; the wear draw of `09_WR_B_draws_not_thresholds.md` edit 1 and the drawn hunger shape of its edit 2 have landed earlier in this batch (U3 §1.2, step 4). Where a symbol is named that does not exist at `aa31fd2`, the item says which batch or item makes it.

**What this part holds.** The second half of one batch, `B12a-world-motion-and-ground` (lanes SE and WR, D-21: the in-flight row is in `registers/handoffs/HANDOFF_SE.md`). The first half (lane A19) writes the batch block's head (the lines of `V12_STRUCTURE_part2.md` §5.2 down to the position table) and positions from `B12a.01`; this part writes positions `B12a.51` onward, the re-pin position `B12a.99` (`V12_STRUCTURE_part4.md` E-1) and the boundary row. Because the head is the other lane's, this part opens with what the head must carry from this half: the position-table rows, the `DIALS AT CONTROL`, `IDS`, `UNDECIDED`, `SERIAL EDGES` and `FILE CENSUS` lines for these positions, and the `BATCH GATE` lines these positions add. The head author (or H1/H2) merges them; nothing here re-decides the head.

**Members, in U3 §1.2's order for B12, steps 6 to 10, then the plan's additions** (`V12_STRUCTURE.md` §2.2, B12a row; D-10): `07_SE_ground_and_granaries` with `07_SE_treasury_granary_B` (steps 6–7; the intake's CP-T08-02, which the first proposal amends, is closed by them) → `16_PESSIMIST_GAME_the_world_draws` (step 8) → `16_PESSIMIST_WR_B_the_calamity_strains_and_breaks` edits 1–4 (step 9) → `U5d_WR_owed_edits` §4, §1, §3, §2 (a) (step 10, in its own land order "§4 (text), §1, §3, §2") → `09_WR_world_motion` edit 1's `lattice_coupling` flip (HELD here; see `B12a.71`) → H-138 (D-10) → `B12a.99`.

**Words.** `unified/U1_GLOSSARY.md`. A *lap* is one pass of the season's scene budget; a *round* is one engagement of a fight (A-101); nothing in this part uses either for the other. A *Site* is a place's fabric (`state/carriers.py::Site`); a *rung* is a node of the place ladder; a *treasury* is the stores on the rung where a seat sits (`07_SE_treasury_granary_B.md` R-SE-28). A person's numbers follow A-98; no army word is used.

**Paths.** As `V12_STRUCTURE.md` states: a bare path is under `proposals/2026-11-12-subsystem-audit-suite/`; a path under `engine/`, `modules/`, `tools/`, `references/`, `registers/` is the repository's. A line number into a file edited at or before B03a is dropped and the symbol kept (`V12_STRUCTURE_part2.md` §5.4).

---

## What the batch head carries from this half (for A19, H1 and H2 to merge)

**Position table, continued** (landing order; one row per position; the first half's rows precede these):

| pos | item | source | state | hash | gates on |
|---|---|---|---|---|---|
| B12a.51 | places are endowed by territory: the `field` kind, the `site_endowment` table, its loader, `endowment_for`, two fixtures, the site loop | `07_SE_ground_and_granaries` §4 (a), (b), (c) site loop, (e) first half; CP-T08-02 as amended | BUILD | EQUAL | `09_WR_B_draws_not_thresholds` edits 1–2 (earlier in B12a); Batch B03c |
| B12a.52 | the treasury is the granary: `treasury_above` and the stores seed | `07_SE_treasury_granary_B` §4 (a), (b) (superseding `07_SE_ground_and_granaries` (c)'s seed) | BUILD | EQUAL | B12a.51 |
| B12a.53 | the larder walk continues up the ladder for the remainder | `07_SE_ground_and_granaries` §4 (d), (e) third half; H-303 | BUILD | EQUAL | B12a.51 |
| B12a.54 | the `endowment_mode` flip: `uniform` → `ground` | `07_SE_ground_and_granaries` §8 (the `ground` flip); CP-T08-02 | BUILD | MOVER(behaviour) | B12a.51, B12a.52, B12a.53 |
| B12a.55 | the `granary_seasons` flip: 0 → 4 | `07_SE_ground_and_granaries` §8; `07_SE_treasury_granary_B` §4 (c) (the flip's gate) | BUILD | MOVER(behaviour) | B12a.54 |
| B12a.56 | the `larder_walk` flip: `first` → `through` | `07_SE_ground_and_granaries` §8 | BUILD | MOVER(behaviour) | B12a.55 |
| B12a.57 | how a body and a shortfall become a pool and an obstacle | `16_PESSIMIST_GAME_the_world_draws` edit 3 (INCOMPLETE: DESIGN, `U4_DOCUMENT_STATUS.md` §3.4) | DESIGN-FIRST | EQUAL | Batch B05, Batch B06 |
| B12a.58 | the hunger draw's fixtures, at control | `16_PESSIMIST_GAME_the_world_draws` edit 1 | BUILD | EQUAL | B12a.57 |
| B12a.59 | `SubsistInput.severity` | `16_PESSIMIST_GAME_the_world_draws` edit 2 | BUILD | EQUAL | B12a.58 |
| B12a.60 | `subsist` reads the severity | `16_PESSIMIST_GAME_the_world_draws` edit 4 | BUILD | EQUAL | B12a.59 |
| B12a.61 | the host draws the severity per hungry eater | `16_PESSIMIST_GAME_the_world_draws` edit 3 | BUILD | EQUAL | B12a.57, B12a.60 |
| B12a.62 | the `hunger_severity_draw` flip: `False` → `True` | `16_PESSIMIST_GAME_the_world_draws` "Lands it" (the flip) | BUILD | MOVER(behaviour) | B12a.61 |
| B12a.63 | only a broken Site pulls | `16_PESSIMIST_WR_B` edit 1 | BUILD | EQUAL | `09_WR_world_motion` edit 1 (earlier in B12a) |
| B12a.64 | a strained Site breaks, holds or knits by a draw | `16_PESSIMIST_WR_B` edit 2 | BUILD | EQUAL | B12a.63; `09_WR_B_draws_not_thresholds` edit 1 |
| B12a.65 | `restore` declines at a broken Site while the coupling runs | `16_PESSIMIST_WR_B` edit 3 | BUILD | EQUAL | B12a.64 |
| B12a.66 | a crossing a person stands beside raises a question about the place | `16_PESSIMIST_WR_B` edit 4 | BUILD | MOVER(behaviour) | B12a.64 |
| B12a.67 | the `restore` roster sentence brought to the tree | `U5d_WR_owed_edits` §4 | BUILD | EQUAL | — |
| B12a.68 | a real execution reads as a killing | `U5d_WR_owed_edits` §1 (H-257) | BUILD | EQUAL | — |
| B12a.69 | a witnessed recovery clears a believed wound | `U5d_WR_owed_edits` §3 | BUILD | MOVER(behaviour) | Batch B04 |
| B12a.70 | the order in which WR's draws land | `U5d_WR_owed_edits` §2 (a), (b) | POINTER | — | B12a.63, B12a.64 |
| B12a.71 | the `lattice_coupling` flip and `wound=True` | `09_WR_world_motion` edit 1 (second commit), as `16_PESSIMIST_WR_B` amends it | HELD (B35's Mend; H-165/H-07's wear-0 kinds) | — | Batch B35 (set by B98) |
| B12a.72 | a zero-amount store move changes no store | H-138 (D-10; E6 block 5) | BUILD | EQUAL | — |
| B12a.99 | re-pin and close readings | `V12_STRUCTURE_part4.md` E-1 | BUILD | MOVER (the re-pin) | B12a.01 to B12a.72 |

**Intake entries this half placed, and those it did not (`V12_STRUCTURE_part2.md` §5.6, `V12_STRUCTURE_part4.md` E-8).** Each id of the intake's three B12 headings (`:172`, `:310`, `:352`) was grepped in the 25 B12 members; for those a member of this half names:

- **CP-T08-02** (intake `:315`; E1 carry-forward `:1229`): first named by `07_SE_ground_and_granaries` (this half), which "amends" it (its `:13`, R1). One item with the proposal (§5.6, the evaluation's rule 2): closed by `B12a.51` (the roster, the loader, the site loop) and `B12a.54` (the flip). The carry-forward's falsifier (a mountain polygon gets a seam) and its `ground_class` are withdrawn by the proposal's R1 (8 of 37 settlements fall in no polygon); its control (`shortfall:salt` over two seasons) is kept as a reading at `B12a.54`.
- **CR-22, H-11, H-125** (intake `:321`): first named by `07_SE_ground_and_granaries` (§4 (f): "CR-22's rule gains one clause"; H-125 is also named by `09_WR_B_draws_not_thresholds`, the first half). **Not placed here: E-8's exception (the dependency wins).** CR-22's NEEDS are CP-T10-03 (the calendar, named first by `09_WR_B_weather_with_memory_and_the_year`, B12b), CL-EVENTS (2) (the live weather draw, B12b with that same file, intake `:356`), and CR-08, whose successor is `07_SE_population_census` (B12b, `master/V11_EVALUATION_part3.md:146`); its exit runs "calendar on, the live weather draw on" (E1 `:2443`). It joins **B12b**, after those, carrying `07_SE_ground_and_granaries` §4 (f)'s clause ("its arms run under `ground` with `granary_seasons` at the shipped value, and its exit records the band spread across settlements"); this half's `B12a.54` and `B12a.55` set the arms it runs under. Noted here and owed to B12b's author (receipt).
- **CP-T08-05** (intake `:316`): first named by `07_SE_ground_and_granaries` (§7, its NERS reading only). **Not placed here (E-8):** its card names CP-T08-02 and the recipes of CP-T08-04 (E1 `:1272`), and CP-T08-04 is named first by `07_SE_capability_rate_B` (B12c). It joins **B12c**. Noted for B12c's author.
- **IN-52 and DEF-7** (intake `:320`, `:325`): IN-52 first named by `07_SE_ground_and_granaries` (§7, NERS only). **Not placed here (E-8):** its flip "lands inside plan IN-52's flip entry, after `07_SE_treasury_granary_B.md` and with `16_PESSIMIST_SE_B_harvest_walls_and_the_supply_gate.md` edit 4" (`U5d_SE_owed_edits.md` §4), both B12b members; DEF-7 is "with IN-52". They join **B12b**. Noted for B12b's author.
- No other B12 entry is named first by a member of this half (the grep, at `aa31fd2`: CR-47, CR-40, CP-T08-01, -03, -04, -06, -08, CR-49, CR-67, H-171, CP-T10-01, -02, -03, CL-EVENTS and the MISSING-DEP "P14 B10-16 gates" entry are named first, if at all, by members of the first half, B12b or B12c, or by none).

**DIALS AT CONTROL (this half):**
- `lattice_coupling` = 0 with `wound=False` the default; set by B98; target: `16_PESSIMIST_WR_B`'s gate on `build_realm` with the wound planted and the weight at 250 — the realm's yield differs between seeds 0 and 1 and a `site.ruptured` is emitted in at least one with its season differing, and "the front stops where it is mended" (fourteen seasons in the source; B98 reads it at two, A-114); preconditions: B35's Mend (`09_WR_B_threadwork_session_and_practitioner`) and H-165/H-07's wear-0 kinds (`09_WR_world_motion.md` edit 1).
- `site_yield.harbour.grain` under `ground` = 40 (today's, both arms); the source's "a reduced `grain` (fish) of 10" under `ground` is not built here (`B12a.51`, UNDECIDED 3); set by B98; target: none stated ("joins JQ-6's sweep") → `BLOCKED (design: no target reading)` (D-22).
- `rupture_band` = 100, `rupture_base` = 2, `rupture_pool_cap` = 6 (`B12a.64`): inert while `lattice_coupling` is 0; "re-read at the joint calibration of A-5/A-6 before the weight leaves 0" (the source) → set with the flip in B98; target: the same reading as `lattice_coupling`'s.
- `granary_seasons`, `endowment_mode`, `larder_walk`, `hunger_severity_draw`: set in this batch (`B12a.55`, `.54`, `.56`, `.62`); not B98's.

**IDS (this half):** ED-SE 0; H 10 — three for `endowment_mode`, `granary_seasons`, `larder_walk` (`B12a.51`, `.53`) `[ASSUMPTION: a new fixture carries a hole-register row and its `[JUSTIFIED: …]` tag, as every swept fixture of `data/fixtures.py` does (`lattice_coupling`'s H-235 line) — basis: CP-T08-02's "the fixture and its H-row"; the other two are not named by the source]`; four for `hunger_severity_draw`, `hunger_band_steps` and the two conversion fixtures (`B12a.57`, `.58`; the source names the first two); three for `rupture_band`, `rupture_base`, `rupture_pool_cap` (`B12a.64`, the source). H-138's row is edited, not added.

**UNDECIDED (this half; each written with the reading that changes less):**
1. *Steps 8 and 9 in which order.* `16_PESSIMIST_GAME_the_world_draws.md` (its Status line) lands after `16_PESSIMIST_WR_B` edits 1–2; `16_PESSIMIST_WR_B` (its Reconciled line) lands before the GAME file; U3 §1.2 (the later repair, U6 R-A) orders GAME (8) before WR_B (9) and the batch row of `V12_STRUCTURE.md` §2.2 follows U3. Followed U3 §1.2. No symbol is shared between the two files' edits except `data/fixtures.py` (different keys) and `queries/world_q.py` (different functions), so either order builds.
2. *The `lattice_coupling` flip.* `V12_STRUCTURE.md` §2.2 and U3 §1 item 13 put it in B12a; `16_PESSIMIST_WR_B` ("the flip after B35"; edit 3: "Until that module lands the weight stays 0"), U3 §4.1 row 48 (LATER: "the calamity ships with `lattice_coupling` 0") and `09_WR_world_motion.md` edit 1 ("the flip waits on" H-165/H-07's wear-0 kinds) put it after B35. Flipping here would run a calamity whose only mender (`restore`) `B12a.65` declines and whose Mend does not exist. Taken: the position is `HELD`, the setting is a `DIALS AT CONTROL` line set by B98.
3. *The harbour's reduced grain under `ground`.* `07_SE_ground_and_granaries.md` §4 (a) gives the value ("under `ground`, `harbour` yields `salt: 30` and a reduced `grain` (fish) of 10 [ASSUMPTION; JQ-6's family]") and no mechanism (`site_yield` is one table keyed by kind, read in both arms). Not built here; kept as a dial (above).
4. *The `field` kind's use floors, capacity floor and works cost.* `07_SE_ground_and_granaries.md` says they join "exactly as CP-T08-02's build text already states"; CP-T08-02's text states none ("Magnitudes are JQ-6's family; none is set here", E1 `:1243`). `B12a.51` writes `band_floors.cells.field: {}` (`dwelling`'s empty control cell), `capacity_floor.floors.field: 0` and `works_cost.costs.field: {timber: 10}` (the value every other Site kind's row holds at `aa31fd2`), each tagged `[ASSUMPTION; JQ-6]` and listed in the PR body (D-19).
5. *Gates past two seasons.* The sources' readings at eight and fourteen seasons are rewritten at two (D-17, A-114): `B12a.52`'s run-down arm uses `granary_seasons` 1 inside its own test so the granary empties inside the cap; `B12a.64`'s rupture tests plant Sites below the rupture floor beside a broken Site at season 0 so the draw is taken in the first MATTER.
6. *H-138's two fix shapes.* E6 block 5: "compare stores by value with zero-valued keys normalised out (or do not touch the dict at amount 0)". Taken: the second, at the one body (`loop/effects_shared.py::_shift`), which moves no digest; E6's note that H-138 "may be cut" as unreached at the shipped amount is not taken, because D-10 attaches that drop condition to H-130 and H-139 only and H-94's swept arm 0 reaches it in `test_season_shape.py`.
7. *`07_SE_treasury_granary_B.md` (d)* re-words an audit table (ARC-20's gate, first audit §13): not code, not carried; the re-worded gate is a reading at `B12a.55`.
8. *`07_SE_ground_and_granaries.md` (f)* edits v11 text (AM-E-13, CR-22): AM-E-13 is SUPERSEDED (`master/V11_EVALUATION_part15.md:29`) and the CR-22 clause travels with CR-22 to B12b; no v11 file is edited.
9. *CP-T08-02's v11 NEEDS column names CP-T08-03* (E1 `:1234`, "ids named in its gate"); the amended gate (`07_SE_ground_and_granaries.md` §5) names none, so CP-T08-02 does not wait for CP-T08-03 (B12c). Session content wins (`STAGES.md` stage 6).
10. *The first commit that creates `test_endowment.py`.* U3 §1.3 and §6.1 say "B12 first commit"; after the cut it is `B12a.51`'s first step (nothing earlier in B12a reads it).
11. *`U5d_WR_owed_edits` §4's sentence.* The source's text ("formed nowhere since REM-22") predates `16_PESSIMIST_WR_B` edit 4, which U3's order lands first (B12a.66) and which makes `restore` form where a crossing is witnessed. `B12a.67` writes the source's sentence with one clause naming B12a.66; the `verb_table.yaml` `restore` row's `referent_class_note` ("attempted 0/0/0") is not edited by any item of this half (no source asks it), and B12a.66's reading is quoted in its commit body.
12. *`U5d_WR_owed_edits` §3's "carrying the ceiling".* No source states the shape; `_eff_kill`'s precedent is the `(pid, "body", v)` Observation alone. Taken: the Observation with `v` the mended body; a believed ceiling stays the `wounded_with` docstring's GAP. The "recovery step" half has no carrier at `aa31fd2` (MATTER writes falls only); it is owed to CP-T10-04 (B37p).
13. *Steps 6–10 against U3 item 13's text.* U3 item 13 names `16_PESSIMIST_WR_B` "edits 1–2" and `U5d_WR_owed_edits` "§2 (a), §3, §4"; the sources land edits 3–4 ("order 1 → 2 → 3 → 4") and §1 ("§1 placed in B12 beside §3") in B12 too, and U3 §3.1's node rows place both whole files in B12. All are carried here, in the sources' orders.

**BATCH GATE lines this half adds** (the head author merges them into the one `BATCH GATE`, read once on the closing tree, `PYTHONHASHSEED=0` on every seeded command):
  `python -m pytest engine/season/tests/test_endowment.py engine/season/tests/test_demand_delivery.py engine/season/tests/test_hunger.py engine/season/tests/test_in35_lattice_coupling.py engine/season/tests/test_strife_execution.py engine/season/tests/test_territorial_subsistence.py -q` → all pass;
  `python -m pytest engine/season/tests/test_season_shape.py -k "wounded or transfer or exchange" -q` → pass;
  `python tools/ci_sim_fabrication_check.py` → exit 0 (every new fixture carries its tag); `python -m engine.season.harness.register --check` → exit 0 (the ten new H rows; H-138's row);
  under the batch's shipped arms (`ground`, `granary_seasons` 4, `through`, `hunger_severity_draw` True), two seasons: at seed 0 the hunger band differs between at least two settlements in season 1 (`07_SE_ground_and_granaries.md` §5, "in every season after the first", its seed), and at each of seeds 0 to 2 at least one draw cell's `source` is a rung at which an Office sits (`B12a.55`'s gate); quoted before (`reading @<B12a.53's sha>`) and after;
  with every switch of this half at its control (`uniform`, 0, `first`, `False`, `lattice_coupling` 0): `build_realm(s)` and its one-season hash for s = 0 to 2 equal the first half's last reading (`reading @<sha>`) — the controls equal (U3 §1 item 13's gate).

**SERIAL EDGES (this half):** within: B12a.51 → B12a.52 (the seed reads the Sites the loop mints) → B12a.53 → B12a.54 → B12a.55 → B12a.56 (each flip its own commit, after every edit it switches on); B12a.57 → B12a.58 → B12a.59 → B12a.60 → B12a.61 → B12a.62 (the source's "1 (fixtures at control) → 2 → 4 → 3 → the flip", with the design ahead of the fixtures it names); B12a.63 → B12a.64 → B12a.65 → B12a.66 (the source's "order 1 → 2 → 3 → 4, each with its test"); B12a.67 → B12a.68 → B12a.69 (`U5d_WR_owed_edits`' "Land order: §4 (text), §1, §3, §2"); B12a.63, B12a.64 → B12a.70 → B12a.71; B12a.72 has no edge inside the batch; B12a.99 last. With the first half: `09_WR_B_draws_not_thresholds` edits 1–2 → B12a.51 (the drawn yield and body, `07_SE_ground_and_granaries.md` "Depends on") and → B12a.61 (the hunger draw's shape) and → B12a.64 (the wear write the break follows); `09_WR_world_motion` edit 1 (the wound row and switch) → B12a.63. With other batches: `07_SE_ground_and_granaries` → `21_PROCEDURAL_D_world_cards_and_churn` (B39, U3 §4.1 row 42, LATER: the bounded starting draw); `16_PESSIMIST_WR_B` → `09_WR_B_threadwork_session_and_practitioner` (B35, row 48, LATER) → B98 (`B12a.71`'s setting); `U5d_WR_owed_edits` §2 (c) → B37 (rows 49–50); CR-22 → B12b (E-8, above).
**FILE CENSUS (this half; U3 §5.1's chains):** `engine/season/rosters.yaml` (B12a.51, .67) B11 → B12a → B12b; `engine/season/data/fixtures.py` (B12a.51, .53, .54, .55, .56, .58, .62, .64) B11 → B12a → B12b; `engine/season/queries/world_q.py` (B12a.52, .53, .61, .66) B11 → B12a → B12b; `engine/season/queries/inputs.py` (B12a.53, .59) B05 → B12a → B14; `engine/season/boot/realm.py` (was `harness/populated.py`; B12a.51, .52) B11 → B12a → B20; `modules/settlements/larder.py` (B12a.53) B12a only; `modules/settlements/subsist.py` (B12a.53, .60) B12a → B39; `engine/season/loop/matter.py` (B12a.63, .64; the first half's `09_WR_B` edit 1 before) B09 → B12a → B22; `engine/season/write_matrix.yaml` (B12a.64) B10 → B12a → B35; `engine/season/loop/effects_economy.py` (B12a.65) B12a → B12c (`14_VERBS_MATERIAL_A`) → B33; `engine/season/loop/effects_combat.py` (B12a.69) B04 → B12a → B14; `engine/season/harness/strife.py` (B12a.68) B12a → B32; `engine/season/loop/effects_shared.py` (B12a.72) B12a → B21; `engine/season/hole_register.yaml` (ten rows, H-138) the permanent surface; tests: `test_endowment.py` NEW (B12a.51), `test_demand_delivery.py`, `test_hunger.py`, `test_territorial_subsistence.py`, `test_in35_lattice_coupling.py`, `test_strife_execution.py`, `test_season_shape.py` (B02 → B11 → B12a).
**C(B12a) additions (this half):** the files of the census above; `modules/settlements/larder.py`, `modules/settlements/subsist.py`; `engine/season/state/ids.py` (`draw_factory`); `engine/season/seam/ladder.py` (`degree_from_net`); `engine/season/harness/scarce.py` (the planted-treasury precedent); `engine/season/tests/_realm_goldens.py` (B02's pin file); read whole for B12a.57: `proposals/16_PESSIMIST_GAME_the_world_draws.md` and `proposals/09_WR_B_draws_not_thresholds.md` edit 2; instruments `register`, `tools/ci_sim_fabrication_check.py`, `tools/tests_for_diff.py`, `tools/m1_acceptance.py`.
**COST (this half):** small builds and edits; four in-batch flips; one design. Producer `valoria-author` on `sonnet`, `high`; `B12a.57` on `opus`, `high`, with a `ners` critic; the flips' readings read by `opus` at the close.
**EST (this half):** 11.6 h [estimate: `V12_STRUCTURE.md` §2.4's per-commit formula over this half's 23 positions, 0.4 h × 23 + 2.5 h for the close (the close is the batch's one close and is counted once, here)].

---

### B12a.51 — places are endowed by territory: the `field` kind, the `site_endowment` table, its loader and `endowment_for`, two fixtures, the site loop · `07_SE_ground_and_granaries` (a), (b), (c) site loop; CP-T08-02 · BUILD · HASH EQUAL
- SOURCE: `proposals/07_SE_ground_and_granaries.md` §3 R1, §4 (a), (b), (c) (the site loop), (e) (`test_endowment.py`, first half), §5; intake `:315` (CP-T08-02, E1 carry-forward `:1229`, E4 `:1464`); U3 §6.1 (`test_endowment.py` MISSING: "write it as the batch's first commit"); rulings A-50 (the starting draw, at its zero-width control here); closes CP-T08-02 (with B12a.54), F-SE-01, R-SE-01.
- ADVANCES: none of the nine by itself; the ground every scarcity reading of B12b (CR-22) and B12c (CP-T08-05, CR-49) steers.
- INSTRUCTION:
  1. Create `engine/season/tests/test_endowment.py` first (step 6 below), and read it red (no `site_endowment`).
  2. `engine/season/rosters.yaml`, a new table (the source's text, exactly):
     ```yaml
       site_endowment:
         source: "CP-T08-02 as amended (proposals/2026-11-12-subsystem-audit-suite/proposals/07_SE_ground_and_granaries.md)"
         row: H-07
         keys: [territories, site_kinds]
         uniform: [harbour, seam]            # the control: today's placement, every settlement
         ground:                             # [ASSUMPTION; medium; Jordan to correct; revert: endowment_mode uniform]
           T1:  [harbour]                    # capital, river-sea nexus
           T2:  [field]                      # heartland farmland
           T3:  [seam]                       # border fortress, mountain pass
           T4:  [seam]                       # highland timber
           T5:  [field, field]               # breadbasket
           T6:  [field]                      # southern farmland
           T7:  [seam]                       # timber valley
           T8:  [harbour]                    # west sea trade
           T9:  [seam]                       # mountain ridge
           T10: [seam]                       # border castle
           T11: [harbour]                    # central fjords
           T12: [harbour]                    # western fjords
           T13: [harbour]                    # southern fjords
           T14: [field]                      # central plains
           T16: [harbour]                    # island republic
           T17: [seam, seam]                 # northern mines
         settlement: {}                      # optional override, keyed by geography code (S-NNN)
     ```
     Additions go at the end of their family's block (CIP part 2 §5 note 1).
  3. The `field` kind (source: "`field` joins `site_kinds`, `site_yield` (`grain: 40`), `wear_per_season` (10), `band_floors` and `works_cost`"): `site_kinds` gains `field`; `site_yield.field: {grain: 40}`; `wear_per_season.rates.field: 10`; `band_floors.cells.field: {}`; `capacity_floor.floors.field: 0`; `works_cost.costs.field: {timber: 10}` — the last three `[ASSUMPTION; JQ-6]` (UNDECIDED 4; `capacity_floor` is checked against `site_kinds` in both directions, `data/fixtures.py::_check_keyed_on_site_kinds`, so it needs a row). Every magnitude "is a shape proposal and joins JQ-6's sweep" (the source). `harbour`'s cells are not changed (UNDECIDED 3).
  4. `engine/season/data/fixtures.py`: the loader, beside `_load_capacity_floor` — "refuses a territory holding a settlement with no row, a kind outside `site_kinds`, and an empty list" — and the pure function `endowment_for(fixtures, sid, territory) -> tuple[str, ...]`, "returning the `uniform` list or the `ground` row (settlement override first)". Two fixtures: `endowment_mode="uniform"` (swept `uniform / ground`) and `granary_seasons=0` (swept `0 / 4 / 8`; "0 is the control, no territory stock"), each with its `[JUSTIFIED: engine/season/hole_register.yaml H-<block slot> -- …]` line and its new hole-register row (`site: Fixtures endowment_mode`, `site: Fixtures granary_seasons`, graded `assumption`, the sweep as stated).
  5. `engine/season/boot/realm.py::build_realm` (moved there from `harness/populated.py` by B03c), the site loop. Old (at `aa31fd2`, `harness/populated.py`):
     ```python
         for sid in geo["settlements"]:
             for k in sorted(SITE_YIELD):
                 if SITE_YIELD[k]:
                     s_id = f"s_{_slug(sid)}_{k}"
                     w.sites[s_id] = Site(s_id, f"set_{_slug(sid)}", k,
                                          condition=w.fixtures.get("condition_scale"))
     ```
     New (the source's structure): `kinds = endowment_for(w.fixtures, sid, geo["settlements"][sid]["territory"])`; "one Site per list entry, id `s_<slug>_<kind>` for the first of a kind and `s_<slug>_<kind>_<n>` for the rest, so the `uniform` arm mints today's ids byte for byte". (The old loop would mint a `field` everywhere once `site_yield` has the row: the new loop is what keeps `uniform` equal.) The stores seed of the source's (c) is not written here: `B12a.52` writes it, re-keyed.
  6. Tests, in the new `engine/season/tests/test_endowment.py` (the source's (e), first half): `test_ground_t5_holds_a_field_and_no_seam` and `test_ground_t17_holds_a_seam_and_no_field` (under `ground`, built with the fixture overridden, every settlement of T5 holds a `field` and none a `seam`; T17's a `seam` and no `field`; each loop asserts it asserted); `test_a_territory_with_a_settlement_and_no_row_refuses_at_load`; `test_uniform_mints_todays_site_ids` (the `uniform` arm's Site id set equals the set at the batch's start, `reading @<sha>`) `[ASSUMPTION: test names; the item creates them — E-3]`.
  7. Glossary: `unified/U1_GLOSSARY.md` gains (or points) a row *endowment*: "what producing Sites a place is given at the world's making, as a town is endowed with fields or a harbour", owner `rosters.yaml: site_endowment`; and *field* (the Site kind): "a Site that yields grain".
- WHERE: `engine/season/rosters.yaml` (`site_endowment`; `site_kinds`, `site_yield`, `wear_per_season`, `band_floors`, `capacity_floor`, `works_cost` rows for `field`); `engine/season/data/fixtures.py` (the loader beside `_load_capacity_floor`; `endowment_for`; `endowment_mode`, `granary_seasons`); `engine/season/boot/realm.py` (`build_realm`, the site loop); `engine/season/hole_register.yaml` (two rows); NEW `engine/season/tests/test_endowment.py`; `unified/U1_GLOSSARY.md` (*endowment*, *field*).
- TESTS: step 6, written before steps 2–5 and read red; green after. `engine/season/tests/test_hunger.py` stays green unedited (the `uniform` arm).
- FALSIFIER and CONTROL: "If under `ground` every settlement still shares one band in every season, the endowment is not reaching `produce` (the planted failure: map every territory to `[harbour, seam]`; the test reds). If the `uniform` arm's `build_realm(0)` hash differs from the base, the id scheme moved" (the source). Control: `build_realm(s)` at s = 0 to 2 and its one-season hash equal to the previous item's reading (`reading @<sha>`).
- GATE: `python -m pytest engine/season/tests/test_endowment.py engine/season/tests/test_hunger.py -q` → pass; `python tools/ci_sim_fabrication_check.py` → exit 0; `python -m engine.season.harness.register --check` → exit 0; `build_realm(0)`'s content hash after one season, `PYTHONHASHSEED=0` → equal to the previous item's reading.
- HASH MOVERS: none (`Fixtures` is not folded by `World.content_hash()`, `state/world.py::_STATE_COLLECTIONS`; the `uniform` loop mints today's Sites).
- DEPENDS ON: EXISTS-IN-TREE `engine/season/data/fixtures.py::_load_capacity_floor`, `::_check_keyed_on_site_kinds`, `rosters.yaml: site_kinds`, `site_yield`, `wear_per_season`, `band_floors`, `capacity_floor`, `works_cost`; V12 Batch B03c (`boot/realm.py`); V12 `09_WR_B_draws_not_thresholds` edits 1–2 (earlier in B12a: "the drawn yield and body", the source's "Depends on").
- GLOSSARY: *endowment*, *field* (step 7).
- NAMES: `harness/populated.py::build_realm` → `boot/realm.py::build_realm` (§5.10, B03c).
- IDS: H block slots 1–2.
- COST and TIER: small build (the table, the loader, the loop); `sonnet`, `high` (the source: "Tier: `sonnet` (R3 7b-0)").
- LANDS IT: B12a's `valoria-author` producer, `isolation: worktree`; `Item: B12a.51`, `[skip ci]`.

### B12a.52 — the treasury is the granary: `treasury_above` and the stores seed · `07_SE_treasury_granary_B` (a), (b) · BUILD · HASH EQUAL
- SOURCE: `proposals/07_SE_treasury_granary_B.md` §3 R-SE-28 to R-SE-30, §4 (a), (b), §5, §8 (the named test); `proposals/07_SE_ground_and_granaries.md` §4 (c) (the seed it supersedes: "It supersedes only resolution R3 and the territory-rung clause of edit (c)"), §5 (the named test); rulings A-23, A-50, A-57, A-58; closes F-SE-17, F-SE-22, R-SE-28, R-SE-29, F-SE-03, R-SE-02.
- ADVANCES: none of the nine by itself; the relief path the `ground` flip's gate reads (`B12a.55`).
- INSTRUCTION:
  1. `engine/season/queries/world_q.py`, one reader beside `governing_hold` (the source's text):
     ```python
     def treasury_above(w: World, rung_id: str) -> Optional[str]:
         """The nearest rung strictly above `rung_id` at which some Office sits, or None. The one owner of
         *whose treasury relieves this place*; read-only; traces as a resolver."""
         seated = {o.rung for o in w.offices.values() if o.rung is not None}
         return next((r for r in ancestry(w, rung_id)[1:] if r in seated), None)
     ```
     (`ancestry` is `state/containment.py::ancestry(w, rung_id)`, which `world_q.py` already calls; at `aa31fd2` `ancestry(w, rung_id)[0]` is `rung_id` itself, so `[1:]` is "strictly above".)
  2. `engine/season/boot/realm.py::build_realm`: "The seed … runs instead **after the offices are seated** (it reads them), beside `mint_planned_works`. Under `endowment_mode == "ground"`:
     - each settlement's `stores`: one season of its Sites' base yield;
     - for each settlement `S` with `t = treasury_above(w, S)` not `None`: `w.rungs[t].stores[k] += granary_seasons × max(0, want_k(S) − yield_k(S))` for each eaten kind `k`, where `want_k` is the subsistence weight times the cohort weight seated at `S` and `yield_k` its Sites' base yield."
     "`granary_seasons` keeps its sweep (`0 / 4 / 8`; 0 is the control). The id scheme and the `uniform` arm are untouched, so `build_realm(0)` hashes as the base under `uniform`." The starting value is the centre of A-50's bounded draw at zero width (`21_PROCEDURAL_D`, B39, U3 §4.1 row 42 LATER); "both are world-gen writes before any season (the precedent is `harness/scarce.py`'s planted treasury)".
  3. Tests in `engine/season/tests/test_endowment.py`: `test_every_draw_source_above_a_settlement_is_a_seat_rung` (the source's named test, "with the planted `terr_T15` failure as its mutation": under `ground`, `granary_seasons` 4, seed 0, two seasons, every draw cell whose `source` is above a settlement names a rung at which an Office sits, and at least one such cell exists); `test_ground_granaries_feed_the_highlands_then_run_down` (`07_SE_ground_and_granaries.md` §5, at two seasons: "eight seasons" and `granary_seasons 4` in the source; A-114 — the arm runs `granary_seasons 1` inside the test so the granary empties after one season: expected, seed 0, no acts, weather draw off: no cohort under a seam territory below full body in season 0 while its treasury holds grain, the treasury's grain lower after season 0, that cohort's body lower in season 1, every cohort under a field or harbour territory at full body; control `granary_seasons 0`: the seam territories' cohorts fall from season 0; each loop asserts it asserted, `checked >= 10`) `[ASSUMPTION: the arm value 1 and the two-season form — basis: the seed is granary_seasons × the deficit, so 1 covers exactly one season; UNDECIDED 5]`.
- WHERE: `engine/season/queries/world_q.py` (`treasury_above`); `engine/season/boot/realm.py` (`build_realm`, the stores seed after the offices are seated); `engine/season/tests/test_endowment.py` (two tests).
- TESTS: step 3, written before steps 1–2 and read red (no `treasury_above`); green after, run with the fixtures overridden inside the test (the shipped arm is still `uniform`).
- FALSIFIER and CONTROL: "A draw sourced at a rung with no Office; or a seat rung holding relief stock that no ladder reaches (the planted failure: seed at `terr_T15`). If under `ground` no duchy's treasury is ever drawn, the endowment left nobody short and the proposal moved nothing" (the source). Control: "`uniform` reproduces the base hash; `granary_seasons 0` under `ground` shows the dependants short from the first season."
- GATE: `python -m pytest engine/season/tests/test_endowment.py -q` → pass; `build_realm(0)`'s one-season hash under the shipped arm → equal to B12a.51's reading.
- HASH MOVERS: none at the shipped arm (`uniform`); under `ground` "it is part of that flip's declared mover" (`B12a.54`, `B12a.55`).
- DEPENDS ON: V12 B12a.51 (`endowment_mode`, `granary_seasons`, the Sites); EXISTS-IN-TREE `state/containment.py::ancestry`, `queries/world_q.py::governing_hold`, `::larder_input`, `harness/populated.py::mint_planned_works` (moved by B03c), `harness/scarce.py`; `World.offices` (`Office.rung`).
- GLOSSARY: row *treasury*: "the stores on the rung where a seat sits; the granary of every town beneath it" (owner `world_q.treasury_above`); *granary* refused as a second store kind ("one stock, not a second kind of store", R-SE-28).
- NAMES: `harness/populated.py::build_realm` → `boot/realm.py::build_realm` (B03c).
- COST and TIER: edit inside the first proposal's small build; `sonnet`, `high`.
- LANDS IT: B12a's producer; `Item: B12a.52`, `[skip ci]`.

### B12a.53 — the larder walk continues up the ladder for the remainder · `07_SE_ground_and_granaries` (d), H-303 · BUILD · HASH EQUAL
- SOURCE: `proposals/07_SE_ground_and_granaries.md` §3 R4, §4 (d), (e) (the H-303 pair); rulings ED-IN-0246 item 3a (the ladder draw, built), ED-SE-0053 (not crossed: no delivery across `contain`); closes H-303's resolution, R-SE-03.
- ADVANCES: none of the nine by itself; a short town with a few units at home reaches the treasury above (R4).
- INSTRUCTION:
  1. `engine/season/queries/inputs.py::LarderInput` gains `walk: str` — `"first"` (shipped, today's rule) or `"through"` — as a fifth field with the default `"first"`, so the positional empty `LarderInput((), (), (), ())` at `world_q._larder_parts`' head still builds `[ASSUMPTION: the default — basis: that one positional call site, read at aa31fd2]`; its docstring gains the line. The fixture is `larder_walk` (`data/fixtures.py`, swept `first / through`, its hole-register row and `[JUSTIFIED: …]` line), "projected by `world_q.larder_input`" (`_larder_parts` passes `w.fixtures.get("larder_walk")`).
  2. `modules/settlements/larder.py::larder_draw`, under `"through"` (the source's text):
     ```python
                 taken, src = 0, None
                 for rung in ladders.get(e.home, ()):
                     held = left.get((rung, kind), stock.get((rung, kind), 0))
                     if held <= 0:
                         continue
                     part = min(want - taken, held)
                     left[(rung, kind)] = held - part
                     taken += part
                     src = src or rung
                     if taken == want:
                         break
                 cells.append((kind, want, taken, src))
     ```
     Under `"first"` the existing loop runs unchanged.
  3. "A `DrawRow` cell then names the first source only; `subsist`'s debit must be per rung, so the cell gains a fifth element `parts: ((rung, units), ...)` and `subsist.py`'s debit loop sums `parts` instead of `(src, take)`." Under `"first"` `parts` is `((src, take),)` when `src` is not `None`, else `()`, so the debit is today's. Every reader that unpacks a cell as four names is widened in this commit: at `aa31fd2` they are `modules/settlements/subsist.py::subsist` (`for kind, want, take, src in row.cells`), `modules/settlements/larder.py::drawn_under` (`for kind, want, take, _src in row.cells`) and `engine/season/queries/world_q.py::_draw_dict` (`for k, want, take, src in r.cells`); `git grep -n "in r.cells\|in row.cells\|\.cells)" engine modules` at the item's open lists them, and the list goes in the commit body. `_draw_record` (the inverse) is widened to match. `DrawRow`'s docstring ("`cells` is `((kind, want, take, source or None), ...)`") gains `parts`.
  4. "The module docstring's rule text is rewritten in the same commit" (`larder.py`).
  5. Tests (the source's (e)): `engine/season/tests/test_demand_delivery.py` gains "the H-303 pair: home 1, above 1,000, want 6 gives take 1 under `first` and 6 under `through`, with the debit split 1 and 5" — `test_h303_first_takes_one_through_takes_six_and_splits_the_debit` `[ASSUMPTION: test name — E-3]`.
- WHERE: `engine/season/queries/inputs.py` (`LarderInput.walk`; `DrawRow` docstring); `modules/settlements/larder.py` (`larder_draw`, `drawn_under`, the module docstring); `modules/settlements/subsist.py` (`subsist`, the debit loop); `engine/season/queries/world_q.py` (`_larder_parts`, `_draw_dict`, `_draw_record`); `engine/season/data/fixtures.py` (`larder_walk`); `engine/season/hole_register.yaml` (one row); `engine/season/tests/test_demand_delivery.py`.
- TESTS: step 5, written before step 2 and read red (no `walk`); green after; the file's other `test_19d_*` tests stay green unedited (the `first` arm).
- FALSIFIER and CONTROL: under `"through"`, the H-303 world takes 1 (the walk stops at the first stocked rung), or the debit lands 6 on the home rung (the per-rung split is lost; matter is created). Control: `"first"` reproduces `build_realm(0)`'s one-season hash (`reading @` B12a.52's).
- GATE: `python -m pytest engine/season/tests/test_demand_delivery.py engine/season/tests/test_hunger.py -q` → pass; `python -m pytest tests/valoria/test_module_registrar.py -q` → pass (the one `tests/valoria` file naming `larder_draw` at `aa31fd2`); the seed-0 one-season hash → equal to B12a.52's reading.
- HASH MOVERS: none at `"first"`; the flip is `B12a.56`.
- DEPENDS ON: EXISTS-IN-TREE `modules/settlements/larder.py::larder_draw`, `::drawn_under`, `modules/settlements/subsist.py::subsist`, `queries/inputs.py::LarderInput`, `::DrawRow`, `queries/world_q.py::_larder_parts`, `::_draw_dict`, `::_draw_record`; V12 B12a.51.
- GLOSSARY: none (the *larder ladder* row's owner stays `larder_draw`; "walk" is the plain word for going up the ladder).
- IDS: H block slot 3.
- COST and TIER: edit to a pure module function with its record type; `sonnet`, `high`.
- LANDS IT: B12a's producer; `Item: B12a.53`, `[skip ci]`.

### B12a.54 — the `endowment_mode` flip: `uniform` → `ground` · `07_SE_ground_and_granaries` §8; CP-T08-02 · BUILD · HASH MOVER(behaviour)
- SOURCE: `proposals/07_SE_ground_and_granaries.md` §4 (e) (`test_hunger.py::test_i` re-recorded), §5, §8 ("the `ground` flip, the `granary_seasons` flip and the `larder_walk` flip are each a declared mover in a commit of their own"); intake `:315` (CP-T08-02: its control, the `shortfall:salt` reading); closes CP-T08-02 (with B12a.51), F-SE-01.
- ADVANCES: none of the nine by itself; the place differs from its neighbour (the source's §1: "the 11 highland settlements … starve when it empties, while the 26 lowland settlements stay fed").
- INSTRUCTION:
  1. `engine/season/data/fixtures.py`: `endowment_mode="uniform"` → `endowment_mode="ground"`; its hole-register row records the flip and the revert (`uniform`).
  2. `engine/season/tests/test_hunger.py::test_i_on_the_built_realm_every_populated_settlement_starves_before_the_first_yield` is "re-recorded under `ground` to assert the opposite (no cohort short at season 0) and kept as written under `uniform`": the existing test is parametrized or pinned to `uniform` (built with the fixture overridden) and a sibling `test_i_under_ground_no_cohort_is_short_at_season_0` asserts the opposite on the shipped realm, `checked >= 30`.
  3. Read, at the item's open and after the flip, every test that builds the shipped realm and asserts a larder or hunger reading, and record each one's reading in the commit body: at `aa31fd2` `engine/season/tests/test_territorial_subsistence.py` (its drain guard, "its first draw finds no stock (silent) and its second is in surplus", named by `test_demand_delivery.py::test_19d_the_shipped_worlds_record_no_shortfall`'s docstring). A test whose assertion is the uniform arm's world-gen artefact is pinned to `uniform` with the arm named, as step 2; a test that reds for any other reason stops the item (`STOPS IF`).
  4. Reading (CP-T08-02's control, kept): over two seasons at seeds 0 to 2, the count of `shortfall:salt` Observations under `ground` and under `uniform`, quoted (the card expects > 0 under `ground` where `uniform` reads 0, "with RB-5 on"; a reading, not a pass condition, because `B12a.55` seeds the treasuries that answer it).
- WHERE: `engine/season/data/fixtures.py` (`endowment_mode`); `engine/season/hole_register.yaml` (the row of B12a.51's slot 1); `engine/season/tests/test_hunger.py` (`test_i` and its sibling); `engine/season/tests/test_territorial_subsistence.py` (only if step 3 finds it so).
- TESTS: step 2's sibling, written before step 1 and read red (the shipped realm starves at season 0); green after.
- FALSIFIER and CONTROL: under `ground` every settlement still shares one hunger band in every season (the source's falsifier; the planted failure of B12a.51 reds it); a cohort short at season 0. Control: `endowment_mode="uniform"` reproduces B12a.53's hash (`reading @<sha>`).
- GATE: `python -m pytest engine/season/tests/test_endowment.py engine/season/tests/test_hunger.py engine/season/tests/test_territorial_subsistence.py engine/season/tests/test_demand_delivery.py -q` → pass; `build_realm(0)` after one season → hash moved from B12a.53's (declared); after two seasons at seed 0, `census(realm)["hunger_by_settlement"]` in season 1 names at least two bands (the source's execution artifact: "the hunger band differs between at least two settlements in every season after the first", read at two seasons, A-114; if it names one, the falsifier above has fired and the item stops).
- HASH MOVERS: every seeded world built by `build_realm`: the Site set and the settlements' starting stores change. Declared; re-pinned at B12a.99.
- EXPECTED RED UNTIL B12a.99: the realm pins in `engine/season/tests/_realm_goldens.py` (B02's one pin file) and every golden that reads them, under `[skip ci]`.
- DEPENDS ON: V12 B12a.51, B12a.52, B12a.53.
- GLOSSARY: none.
- COST and TIER: edit, one declared mover; `sonnet`, `high`; the readings read by `opus` at the close.
- LANDS IT: B12a's producer; `Item: B12a.54`, `[skip ci]`.

### B12a.55 — the `granary_seasons` flip: 0 → 4 · `07_SE_ground_and_granaries` §8; `07_SE_treasury_granary_B` (c) · BUILD · HASH MOVER(behaviour)
- SOURCE: `proposals/07_SE_ground_and_granaries.md` §3 R3, §5 ("`ground`, `granary_seasons 4`"), §8; `proposals/07_SE_treasury_granary_B.md` §4 (c) (the flip's gate, replacing the superseded R3's and v11's AM-E-13), §4 (d) (ARC-20's reading, re-worded), §5; closes R-SE-30.
- ADVANCES: none of the nine by itself; the treasury is the clock (`07_SE_ground_and_granaries.md` §5: "the ladder is the relief path and the granary is the clock").
- INSTRUCTION:
  1. `engine/season/data/fixtures.py`: `granary_seasons=0` → `granary_seasons=4` `[ASSUMPTION: the value — basis: both sources' execution artifact and named test run at 4; the sweep is 0 / 4 / 8]`; its row records the flip and the revert (0).
  2. The flip's gate (`07_SE_treasury_granary_B.md` (c), the source's sentence): "*In a seeded realm run under `ground`, every draw cell whose `source` is above a settlement names a rung at which an Office sits, and at least one such cell exists.*" — read on the shipped realm at seeds 0 to 2, two seasons, as `test_every_draw_source_above_a_settlement_is_a_seat_rung` (B12a.52) with the fixture overrides removed (it now runs the shipped arm).
  3. Readings, quoted in the commit body (not pass conditions): every `source` above a settlement is one of the seat rungs `07_SE_treasury_granary_B.md` §5 lists (`terr_T1`, `terr_T9`, `duchy_hafenmark`, `duchy_valorsmark`, `duchy_varfell`, `r_valoria`) or the item names the other; "with play (seed 2 …): at least one requisitioned unit is later named in a draw cell's source" at two seasons; ARC-20's re-worded reading — a `transfer.made` or `exchange.made` by a person whose giving rung lies under one duchy and whose receiving rung under another, under `ground` — counted at seeds 0 to 2 (it "depends on CR-49's destination class", B12c, so 0 is the expected count here).
- WHERE: `engine/season/data/fixtures.py` (`granary_seasons`); `engine/season/hole_register.yaml` (B12a.51's slot 2 row); `engine/season/tests/test_endowment.py` (`test_every_draw_source_above_a_settlement_is_a_seat_rung` reads the shipped arm).
- TESTS: none new; step 2's test is re-pointed at the shipped arm and was red there before step 1 (no stock above any settlement at `granary_seasons` 0).
- FALSIFIER and CONTROL: "A draw sourced at a rung with no Office; … If under `ground` no duchy's treasury is ever drawn, the endowment left nobody short and the proposal moved nothing" (`07_SE_treasury_granary_B.md` §5). Control: `granary_seasons 0` under `ground` reproduces B12a.54's hash.
- GATE: `python -m pytest engine/season/tests/test_endowment.py -q` → pass; seeds 0 to 2, two seasons, `PYTHONHASHSEED=0`: at least one draw cell's `source` is a seat rung at each seed (`checked >= 3`).
- HASH MOVERS: every seeded realm: the treasuries' starting stores, and every draw that reaches them. Declared; re-pinned at B12a.99.
- EXPECTED RED UNTIL B12a.99: the realm pins, as B12a.54.
- DEPENDS ON: V12 B12a.52 (the seed), B12a.54.
- GLOSSARY: none.
- COST and TIER: edit, one declared mover; `sonnet`, `high`.
- LANDS IT: B12a's producer; `Item: B12a.55`, `[skip ci]`.

### B12a.56 — the `larder_walk` flip: `first` → `through` · `07_SE_ground_and_granaries` §8 · BUILD · HASH MOVER(behaviour)
- SOURCE: `proposals/07_SE_ground_and_granaries.md` §3 R4 ("under R3 a short town with a few units at home must reach the granary above, or the granary feeds only towns that are wholly empty"), §8.
- ADVANCES: none of the nine by itself.
- INSTRUCTION: `engine/season/data/fixtures.py`: `larder_walk="first"` → `larder_walk="through"`; its row records the flip and the revert (`first`). Reading, quoted: over seeds 0 to 2, two seasons, the count of draw cells whose `parts` names two or more rungs (zero under `first` by construction).
- WHERE: `engine/season/data/fixtures.py` (`larder_walk`); `engine/season/hole_register.yaml` (B12a.53's slot 3 row).
- TESTS: none new; B12a.53's pair covers both arms.
- FALSIFIER and CONTROL: on the shipped realm no draw cell names two rungs in two seasons at any of seeds 0 to 2 (then the walk is unreached and the flip moved nothing: report it, do not revert it, R4 is a completeness rule). Control: `first` reproduces B12a.55's hash.
- GATE: `python -m pytest engine/season/tests/test_demand_delivery.py engine/season/tests/test_endowment.py -q` → pass; the reading above quoted with its seeds.
- HASH MOVERS: every seeded realm where a short town holds part of its want. Declared; re-pinned at B12a.99.
- EXPECTED RED UNTIL B12a.99: the realm pins, as B12a.54.
- DEPENDS ON: V12 B12a.53, B12a.55.
- GLOSSARY: none.
- COST and TIER: edit, one declared mover; `sonnet`, `high`.
- LANDS IT: B12a's producer; `Item: B12a.56`, `[skip ci]`.

### B12a.57 — how a body and a shortfall become a pool and an obstacle · `16_PESSIMIST_GAME_the_world_draws` edit 3 (INCOMPLETE) · DESIGN-FIRST · HASH EQUAL
- SOURCE: `proposals/16_PESSIMIST_GAME_the_world_draws.md` edit 3 ("**INCOMPLETE (not decidable from the repository):** the conversion of a body (0-1000) and a shortfall to a pool and an obstacle on the A-5 sampler is not stated by the owner; it is set by the joint calibration (A-5, A-6), the batch's first commit writing it as two named fixtures beside `hunger_band_steps`"); `proposals/09_WR_B_draws_not_thresholds.md` edit 2 ("pool from the cohort's own body … obstacle from the shortfall's depth (how far the larder fell short of want) `[CALIBRATE: the body-to-pool and depth-to-obstacle conversions, joint calibration, OWED §B]`") and its Reconciled line ("pool from the roller's score plus base, floor five; obstacle from the task's difficulty and named terms"); `unified/U4_DOCUMENT_STATUS.md` §3.4 (code DESIGN, owner "calibration batch (B12)"); rulings A-5, A-6, A-54; D-18, E-14.
- ADVANCES: nothing by itself; it settles the INCOMPLETE part B12a.61 and B12a.62 need.
- INSTRUCTION: write the design stating (1) to (5) with falsifiers; no code.
  1. The pool a cohort's body gives: a function of `Person.body` (0 to `condition_scale`) on the one sampler B05 owns, written as a fixture `hunger_body_pool` (its form and value), with the floor `09_WR_B_draws_not_thresholds.md`'s Reconciled line states for a pool ("floor five") or the reason it does not apply to a body.
  2. The obstacle a shortfall gives: a function of the depth (`want − take`, in units, or its share of `want`), written as a fixture `hunger_depth_obstacle` (its form and value).
  3. The expected band shares at three named states (a full body with a one-unit shortfall; a half body with half the want short; a body at the first floor with the whole want short), computed with `engine/dice_engine` at the item's tree, so the reader sees that a worse body and a deeper shortfall make Failure likelier, never certain.
  4. Which value each fixture ships at, marked `[ASSUMPTION; medium; Jordan to correct]`, and that `hunger_band_steps` stays `09_WR_B` edit 2's multiples.
  5. The falsifier of each: a deeper shortfall that does not raise Failure's share; a body at 1000 that cannot fall to Failure (the draw collapsed into a threshold, `09_WR_B_draws_not_thresholds.md` "The falsifier").
  What the ladder (CLAUDE.md §0) cannot settle ends the run `STOPPED` for Jordan (D-18); B12a.61 and B12a.62 gate on this item.
- WHERE: NEW `proposals/2026-11-12-subsystem-audit-suite/proposals/16_PESSIMIST_GAME_hunger_draw_conversion.md` `[ASSUMPTION: the path — basis: CLAUDE.md §3 sends new design work to proposals/, and the pilot parts write design items beside their source; the two fixtures themselves live in data/fixtures.py (B12a.58), never in this file]`.
- TESTS: none (a design).
- FALSIFIER and CONTROL: a conversion the design leaves unstated; a stated conversion under which (3)'s shares do not order by body and depth. Control: nothing under `engine/` or `modules/` changes in this commit.
- GATE: `test -f proposals/2026-11-12-subsystem-audit-suite/proposals/16_PESSIMIST_GAME_hunger_draw_conversion.md && grep -c -E 'hunger_body_pool|hunger_depth_obstacle' <that file>` → the file exists and names both fixtures; `git diff --stat <B12a.56's sha>..HEAD -- engine modules references` → empty for this commit.
- HASH MOVERS: none.
- DEPENDS ON: V12 Batch B05 (the one roll and its sampler, U3 §1 item 6); V12 Batch B06 (`draw_factory`, the keyed-draw owner); V12 `09_WR_B_draws_not_thresholds` edit 2 (earlier in B12a, the shape).
- GLOSSARY: none (no new word: *pool* and *obstacle* are the dice glossary's).
- COST and TIER: design; `opus`, `high`; a `ners` critic (the source: "`opus` for the pool and obstacle conversion at the calibration").
- LANDS IT: B12a's producer; `Item: B12a.57`, `[skip ci]`.

### B12a.58 — the hunger draw's fixtures, at control · `16_PESSIMIST_GAME_the_world_draws` edit 1 · BUILD · HASH EQUAL
- SOURCE: `proposals/16_PESSIMIST_GAME_the_world_draws.md` edit 1, "Lands it" ("order 1 (fixtures at control) → 2 → 4 → 3 → the flip to `True`"); rulings A-54.
- ADVANCES: none by itself.
- INSTRUCTION: `engine/season/data/fixtures.py`, two rows graded `assumption` (the source): "`hunger_severity_draw: bool` (`False` control, today's exact step; `True` the arm …) and `hunger_band_steps: {Overwhelming: 0.0, Success: 0.5, Partial: 1.0, Failure: 2.0}` (the multiples of `body_step` that `09_WR_B` edit 2 states; `[ASSUMPTION; medium; Jordan to correct]` as there), each with its hole-register row (id from `references/id_reservations.yaml` `next_free`)" — here, from B12a's H block. "The shape matches `wear_draw` in `09_WR_B` edit 1 (one methodology for the clock draws)." With them, the two fixtures B12a.57 names (`hunger_body_pool`, `hunger_depth_obstacle`) at the values it states, each with its row and `[JUSTIFIED: …]` line. Every row ships at control: `hunger_severity_draw=False`.
- WHERE: `engine/season/data/fixtures.py` (four rows); `engine/season/hole_register.yaml` (four rows).
- TESTS: none new (no reader yet).
- FALSIFIER and CONTROL: a row with no hole-register row (`tools/ci_sim_fabrication_check.py` reds). Control: the seed-0 one-season hash equal to B12a.56's (no reader).
- GATE: `python tools/ci_sim_fabrication_check.py` → exit 0; `python -m engine.season.harness.register --check` → exit 0; the seed-0 hash → equal to B12a.56's reading.
- HASH MOVERS: none.
- DEPENDS ON: V12 B12a.57; V12 `09_WR_B_draws_not_thresholds` edit 1 (`wear_draw`, the shape matched; earlier in B12a).
- GLOSSARY: none.
- IDS: H block slots 4–7.
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B12a's producer; `Item: B12a.58`, `[skip ci]`.

### B12a.59 — `SubsistInput.severity` · `16_PESSIMIST_GAME_the_world_draws` edit 2 · BUILD · HASH EQUAL
- SOURCE: `proposals/16_PESSIMIST_GAME_the_world_draws.md` edit 2.
- ADVANCES: none by itself.
- INSTRUCTION: `engine/season/queries/inputs.py::SubsistInput` gains one field (the source): "`severity: tuple = ()` — `((pid, multiplier), …)`, empty meaning 1 for every eater." Its docstring's field list gains the line.
- WHERE: `engine/season/queries/inputs.py` (`SubsistInput`).
- TESTS: none new.
- FALSIFIER and CONTROL: a caller that builds `SubsistInput` positionally breaks (the default keeps `world_q.subsist_input`'s four-argument call valid). Control: the seed-0 hash equal to B12a.58's (`SubsistInput` is not folded by `World.content_hash()`).
- GATE: `python -m pytest engine/season/tests/test_hunger.py -q` → pass; the seed-0 hash → equal.
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `queries/inputs.py::SubsistInput`; V12 B12a.58.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B12a's producer; `Item: B12a.59`, `[skip ci]`.

### B12a.60 — `subsist` reads the severity · `16_PESSIMIST_GAME_the_world_draws` edit 4 · BUILD · HASH EQUAL
- SOURCE: `proposals/16_PESSIMIST_GAME_the_world_draws.md` edit 4.
- ADVANCES: none by itself.
- INSTRUCTION: `modules/settlements/subsist.py::subsist`, the body loop's line `lost = inp.body_step * sum(short[pid].values())` becomes (the source):
  ```python
  sev = dict(inp.severity)
  lost = int(inp.body_step * sum(short[pid].values()) * sev.get(pid, 1))
  ```
  (`sev` is built once, above the `for pid in sorted(short)` loop.) "`lost <= 0` already means no fall (the `body_step = 0` control branch), so a spared season needs no second branch." The module docstring's line "THE BODY: `lost = body_step x (units short, summed in kind order)`" gains "× the eater's severity multiplier (1 when none is given)"; it keeps "draws nothing" (the host draws, `16_PESSIMIST_GAME` "The resolution").
- WHERE: `modules/settlements/subsist.py` (`subsist`, the docstring).
- TESTS: `engine/season/tests/test_hunger.py` gains `test_a_severity_of_two_doubles_the_fall_and_zero_spares_it` (a hand-built `SubsistInput` with one short eater: multiplier 2 gives twice `body_step × units`, 0 gives no `BodyFall`) `[ASSUMPTION: test name — E-3]`, written before the edit and read red.
- FALSIFIER and CONTROL: an empty `severity` that changes any fall. Control: the seed-0 hash equal to B12a.59's.
- GATE: `python -m pytest engine/season/tests/test_hunger.py -q` → pass; the seed-0 hash → equal.
- HASH MOVERS: none (no caller fills `severity` yet).
- DEPENDS ON: V12 B12a.59; V12 B12a.53 (the same function's debit loop, edited earlier in this batch).
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B12a's producer; `Item: B12a.60`, `[skip ci]`.

### B12a.61 — the host draws the severity per hungry eater · `16_PESSIMIST_GAME_the_world_draws` edit 3 · BUILD · HASH EQUAL
- SOURCE: `proposals/16_PESSIMIST_GAME_the_world_draws.md` edit 3, "What it changes" ("The draw is keyed `(world_seed, tick, pid, "hunger_severity")` through the one keyed-draw owner (A-30), so the same seed gives the same world and no other stream moves"), "The resolution" (the `season_factor_of` precedent for a keyed draw inside a Query); rulings A-30, A-54; closes F-PES-GAME-05 (with B12a.62).
- ADVANCES: none by itself (at `False` nothing is drawn).
- INSTRUCTION: `engine/season/queries/world_q.py::subsist_input` (the host's projection) fills `severity` (the source): "For each eater short this season, when `hunger_severity_draw` is on: one draw keyed `(pid, "hunger_severity")` through the keyed-draw owner (`draw_factory`, B06's `Draw`), rolled on the one sampler with the cohort's own body as pool ground and the shortfall's depth (how far the larder fell short of want) as obstacle ground (`09_WR_B` edit 2), graded by `degree_from_net`; `multiplier = hunger_band_steps[band]`." The pool and obstacle are read from `hunger_body_pool` and `hunger_depth_obstacle` in the form B12a.57 states. Which eaters are short is read by running `larder_draw` on the same `LarderInput` the projection already builds (`_larder_parts`), the module's own pure function; no second ladder. At `False` the projection returns `severity=()`.
- WHERE: `engine/season/queries/world_q.py` (`subsist_input`).
- TESTS: `engine/season/tests/test_hunger.py` gains (the source's names) `test_hunger_draw_on_bodies_diverge_and_first_deaths_differ` — "with `hunger_severity_draw` on and a planted shortfall on every cohort for eight seasons, the cohorts' bodies are not all equal at the end and the season of first death differs between at least two cohorts; the loop asserts it asserted (at least 30 cohorts read)" — written at two seasons (eight in the source; A-114) with the planted shortfall deep enough that a first death falls inside two seasons for some cohorts `[ASSUMPTION: the plant's depth — basis: body 1000, body_step 10, Failure's multiple 2; the producer states the depth it uses]`; and `test_hunger_draw_off_is_the_base_hash` ("with `False` they are all equal and the hash is the base hash (the control)"). Both written before the edit; the first red (no draw), the second green.
- FALSIFIER and CONTROL: "the scratch `x3_famine.py 0 0 20 nullglobal` (not in the repository) printed one synchronized death season; the first test above is its committed form and must no longer show it" (the source). Control: `False` reproduces B12a.60's seed-0 hash.
- GATE: `python -m pytest engine/season/tests/test_hunger.py -q` → pass; the seed-0 hash at the shipped `False` → equal to B12a.60's reading.
- HASH MOVERS: none at `False`; the flip is B12a.62.
- DEPENDS ON: V12 B12a.57, B12a.58, B12a.59, B12a.60; V12 Batch B06 (`state/ids.py::draw_factory` as the keyed-draw owner; `EXISTS-IN-TREE draw_factory` at `aa31fd2`); EXISTS-IN-TREE `queries/world_q.py::season_factor_of` (the precedent), `seam/ladder.py::degree_ladder` (which returns `engine/dice_engine/dice_engine.py::degree_from_net`, the one owner of the degree; "the ladder lives once, in the seam").
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B12a's producer; `Item: B12a.61`, `[skip ci]`.

### B12a.62 — the `hunger_severity_draw` flip: `False` → `True` · `16_PESSIMIST_GAME_the_world_draws` "Lands it" · BUILD · HASH MOVER(behaviour)
- SOURCE: `proposals/16_PESSIMIST_GAME_the_world_draws.md` edit 1 ("`True` the arm, shipped per the standing rule"), "Hash movers declared" ("every world with a hungry eater at `True` (one re-pin at B12's close)"), "Lands it" ("→ the flip to `True`"); `AUDIT_BRIEF.md`'s standing rule ("a thing that could go either way for the people in the fiction goes by a draw").
- ADVANCES: none of the nine by itself; "a hard year and … a town that fares worse than its neighbour" (the source's "The problem").
- INSTRUCTION: `engine/season/data/fixtures.py`: `hunger_severity_draw=False` → `True`; its row records the flip and the revert (`False`). Readings, quoted: over seeds 0 to 2, two seasons, the count of hungry eaters and the band counts their draws took (each band's share, `checked >= 1` per seed where any eater went short), before (`reading @<B12a.61's sha>`, all at today's step) and after.
- WHERE: `engine/season/data/fixtures.py` (`hunger_severity_draw`); `engine/season/hole_register.yaml` (its row, B12a.58's slot).
- TESTS: none new; `test_hunger_draw_off_is_the_base_hash` keeps its control by building with the fixture overridden to `False`.
- FALSIFIER and CONTROL: over seeds 0 to 2 every hungry eater's draw takes one band (the draw collapsed into a threshold). Control: `False` reproduces B12a.61's hash.
- GATE: `python -m pytest engine/season/tests/test_hunger.py -q` → pass; the readings above, with their seeds.
- HASH MOVERS: "every world with a hungry eater at `True`" (the source). Declared; re-pinned at B12a.99.
- EXPECTED RED UNTIL B12a.99: the realm pins, as B12a.54.
- DEPENDS ON: V12 B12a.61; V12 B12a.57 (the design merged; if it is not, this item is `HELD`, D-18).
- GLOSSARY: none.
- COST and TIER: edit, one declared mover; `sonnet`, `high`; the band reading by `opus` at the close.
- LANDS IT: B12a's producer; `Item: B12a.62`, `[skip ci]`.

### B12a.63 — only a broken Site pulls · `16_PESSIMIST_WR_B` edit 1 · BUILD · HASH EQUAL
- SOURCE: `proposals/16_PESSIMIST_WR_B_the_calamity_strains_and_breaks.md` "The resolution" ("strain flows from what is broken, so it has a source and a direction and stops when the source is mended"), edit 1, "The gate"; rulings A-40 ("one Site per territory"), A-54; `U5d_WR_owed_edits.md` §2 (a); closes F-PES-WR-02 (with B12a.64).
- ADVANCES: none of the nine by itself (inert while `lattice_coupling` is 0).
- INSTRUCTION: `engine/season/loop/matter.py::_lattice_strain`. Old (the source's text, present at `aa31fd2`):
  ```python
  near = [n for u in (t, *sorted(borders.get(t, ()))) for n in by_terr.get(u, ()) if n != sid]
  if not near:
      continue
  gap = max(0, w.sites[sid].condition) - max(0, min(w.sites[n].condition for n in near))
  ```
  New:
  ```python
  broken = [n for u in (t, *sorted(borders.get(t, ()))) for n in by_terr.get(u, ())
            if n != sid and w.sites[n].condition <= 0]
  if not broken:
      continue
  gap = max(0, w.sites[sid].condition)          # the pull is toward a hole in the fabric
  ```
  "No new field: a Site at 0 *is* the broken Site (the wound row of `09_WR_world_motion.md` edit 1 is built at 0). Ordinary uneven wear no longer propagates; a realm with nothing broken couples nothing." The function's docstring ("RULE, NO SOURCE AND NO SCALAR …") and its `TRACE.decision` line ("pulls … toward their weakest neighbour") are rewritten to say the pull is toward a broken Site (A-40), in the same commit.
- WHERE: `engine/season/loop/matter.py` (`_lattice_strain`, its docstring and trace line).
- TESTS: `engine/season/tests/test_in35_lattice_coupling.py` gains `test_a_realm_with_nothing_broken_couples_nothing` (weight 250, every Site above 0: `_lattice_strain` returns `{}`) and `test_the_pull_is_toward_a_broken_neighbour_only` (weight 250, one Site planted at 0: only Sites in its own and bordering territories are pulled) `[ASSUMPTION: test names — E-3]`; written before the edit, the first red (today's rule pulls toward the weakest). The file's existing weakest-neighbour tests (`test_in35_unmanaged_the_lattice_falls_and_crossings_reach_territories_in_order_of_distance`, `test_in35_the_front_advances_one_ring_a_season_at_most`, `test_in35_managed_holding_the_first_ring_stops_the_front_there_and_the_unmanaged_arm_does_not`, `test_in35_a_mended_source_does_not_recall_a_ring_matter_has_already_pulled`) are read at the item's open: each one whose plant has a Site at 0 stays; each that relies on pulling toward a weaker, unbroken neighbour is rewritten to plant its source at 0, and the commit body names each one changed and why.
- FALSIFIER and CONTROL: the falsifier world of the source (the ring table the same at both seeds) is B12a.64's; this edit's: a Site pulled with no broken Site in its own or a bordering territory. Control: "at weight 0 the season is the base hash" — `test_in35_weight_zero_is_wear_alone_and_a_nonzero_weight_differs` and `test_in35_the_shipped_weight_is_the_control` green unedited; the seed-0 hash equal to B12a.62's.
- GATE: `python -m pytest engine/season/tests/test_in35_lattice_coupling.py -q` → pass; the seed-0 one-season hash → equal to B12a.62's reading.
- HASH MOVERS: none (behind `lattice_coupling`, shipped 0).
- DEPENDS ON: EXISTS-IN-TREE `loop/matter.py::_lattice_strain`; V12 `09_WR_world_motion` edit 1 (the wound row and the `build_realm(wound=…)` switch, earlier in B12a); V12 `09_WR_B_draws_not_thresholds` edit 1 (the wear draw that reads the pull as obstacle, earlier in B12a).
- GLOSSARY: row *broken (Site)*: "a Site at condition 0, a hole in the fabric" (owner: the comparison `condition <= 0` in `_lattice_strain`); A-40's "wearing-down" row unchanged.
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B12a's producer; `Item: B12a.63`, `[skip ci]`.

### B12a.64 — a strained Site breaks, holds or knits by a draw · `16_PESSIMIST_WR_B` edit 2 · BUILD · HASH EQUAL
- SOURCE: `proposals/16_PESSIMIST_WR_B_the_calamity_strains_and_breaks.md` edit 2, "The gate", "The falsifier"; rulings A-40, A-54; `U5d_WR_owed_edits.md` §2 (a) ("edits 1–2 before `09_WR_world_motion.md` edit 1's non-zero lattice weight"); closes F-PES-WR-02, F-PES-WR-11 (with B12a.63).
- ADVANCES: none of the nine by itself (inert at weight 0).
- INSTRUCTION (the source's text): `loop/matter.py`, the wear loop. "After the wear write, for each Site that (a) has a broken neighbour by edit 1's reading and (b) stands below the lowest floor of its kind (`band_floors`; for a kind whose cell is `{}`, below `rupture_band`), one keyed draw (`draw_factory(w.world_seed, lambda: w.tick)(site.id, "rupture")`), resolved on the one ladder (`seam/ladder.py`, `degree_from_net`):
  - *Pool (the strain upon it):* the count of broken Sites in its own and bordering territories, capped at `rupture_pool_cap`.
  - *Obstacle (what holds it):* `rupture_base` + the number of its own territory's Sites standing in their top band (sound fabric beside it resists).

  | the strain's degree | the Site | write on `(Site, condition)` at MATTER |
  |---|---|---|
  | Overwhelming, Success | **breaks**: condition → 0 | emits `site.ruptured`, cause the wear Event; witnessed like every MATTER emission |
  | Partial | holds | none |
  | Failure | **knits**: recovers one season's pull | emits `condition.worn` with a positive delta (the fabric held) |"

  Like every edit of the source, the draw runs only while `lattice_coupling` is non-zero ("every edit is behind that weight; the control is byte identical"): at 0, `_lattice_strain` returns `{}` and no Site has a pull, and the block is skipped before any draw is taken. "The wear write" is the write `09_WR_B_draws_not_thresholds` edit 1 left (drawn under `wear_draw`), earlier in B12a. The pool is rolled on the one sampler B05 owns, as the hunger draw is (B12a.61).
  Fixtures, "each `[ASSUMPTION; medium; Jordan to correct]` with its hole row": `rupture_band=100`, `rupture_base=2`, `rupture_pool_cap=6` ("the last two were sized on the whole-dice sampler; re-read at the joint calibration of A-5/A-6 before the weight leaves 0"). "`write_matrix.yaml`'s `(Site, condition)` MAT row gains the kind `site.ruptured`" (its `emits:` becomes "`condition.worn` · `condition.band_crossed` · `site.ruptured`"). "L5 is kept: this is matter's licensed clock writing its own cell; no social row is written and nobody is made to act." The Event kind `site.ruptured` is registered wherever the tree's Event-kind roster requires a new kind (`git grep -n "condition.band_crossed" engine/season/*.yaml` at the item's open names the roster rows to extend; each is listed in the commit body).
- WHERE: `engine/season/loop/matter.py` (the wear loop); `engine/season/data/fixtures.py` (`rupture_band`, `rupture_base`, `rupture_pool_cap`); `engine/season/write_matrix.yaml` (`(Site, condition)`, `emits:`); the Event-kind roster rows the grep names; `engine/season/hole_register.yaml` (three rows).
- TESTS: in `engine/season/tests/test_in35_lattice_coupling.py` (the source's names, at two seasons: "fourteen seasons" in the source; A-114), written before the edit and read red: `test_a_rupture_is_emitted_and_its_season_differs` — weight 250, the wound planted and, at season 0, every Site of the wound's bordering territories set below its kind's lowest floor (so each takes the draw in the first MATTER), seeds 0 to 9: a `site.ruptured` is emitted at some seed and the set of ruptured Sites differs between at least two seeds (`checked >= 10`); `test_yield_at_season_13_differs_between_seeds` — written as `test_yield_differs_between_seeds_after_two_seasons` on the same plant: the realm's summed yield after season 1 differs between seeds 0 and 1 `[ASSUMPTION: the planted form — basis: a drawn break cannot be relied on to occur within two seasons from an unplanted wound; UNDECIDED 5]`; `test_weight_zero_is_the_base_hash` ("at weight 0 the season is the base hash (the control)"). `test_front_stops_where_the_source_is_mended` (the source: the source raised above 0 at season 5, ring means at season 13) is written at two seasons: the source planted at 0 at season 0 and raised to `condition_scale` before season 1; after season 1 no Site is pulled (`_lattice_strain` returns `{}`) and no `site.ruptured` is emitted.
- FALSIFIER and CONTROL: "The ring table (4,810 → 719) the same at both seeds after the change" (the source; `test_yield_differs_between_seeds_after_two_seasons` is its committed form). Control: weight 0 reproduces B12a.63's seed-0 hash.
- GATE: `python -m pytest engine/season/tests/test_in35_lattice_coupling.py -q` → pass; `python tools/ci_sim_fabrication_check.py` → exit 0; `python -m engine.season.harness.register --check` → exit 0; the seed-0 hash → equal to B12a.63's reading.
- HASH MOVERS: none (behind the weight).
- DEPENDS ON: V12 B12a.63; V12 `09_WR_B_draws_not_thresholds` edit 1 (earlier in B12a); V12 Batch B06 (`draw_factory`); EXISTS-IN-TREE `loop/matter.py::_crossings`, `seam/ladder.py::degree_ladder`, `write_matrix.yaml` (`Site`, `condition`), the `body_hazard` keyed draw in the same barrier (the precedent, `loop/matter.py`).
- GLOSSARY: rows *rupture* ("a Site's breaking to condition 0 by a drawn strain") and *knit* ("a strained Site recovering a season's pull") `[new words; the plain words "break" and "hold" are used in prose]`.
- IDS: H block slots 8–10.
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B12a's producer; `Item: B12a.64`, `[skip ci]`.

### B12a.65 — `restore` declines at a broken Site while the coupling runs · `16_PESSIMIST_WR_B` edit 3 · BUILD · HASH EQUAL
- SOURCE: `proposals/16_PESSIMIST_WR_B_the_calamity_strains_and_breaks.md` edit 3; the Mend is `09_WR_B_threadwork_session_and_practitioner.md` (B35; U3 §4.1 row 48, LATER).
- ADVANCES: none of the nine by itself (unreached while the weight is 0).
- INSTRUCTION: `engine/season/loop/effects_economy.py::_eff_restore`, "one decline, beside the existing `site is None` decline":
  ```python
  if site.condition <= 0 and w.fixtures.get("lattice_coupling"):
      return NO_CHANGE        # -> restore.refused: a hole in the fabric is not repaired with mortar
  ```
  The docstring's DECLINES paragraph gains the clause. "Until that module lands the weight stays 0, so this decline is unreached and nothing is orphaned" (the source; `B12a.71`).
- WHERE: `engine/season/loop/effects_economy.py` (`_eff_restore`).
- TESTS: `engine/season/tests/test_in35_lattice_coupling.py` gains `test_restore_is_refused_at_a_broken_site_while_the_coupling_runs` (a hand-built `restore` at a Site at 0: refused at weight 250, admitted at weight 0) `[ASSUMPTION: test name — E-3]`, written before the edit, its first arm red.
- FALSIFIER and CONTROL: a `restore` at a broken Site executed while the weight is non-zero. Control: at weight 0 a `restore` at a Site at 0 executes as today; the seed-0 hash equal to B12a.64's.
- GATE: `python -m pytest engine/season/tests/test_in35_lattice_coupling.py -q` → pass; the seed-0 hash → equal.
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `loop/effects_economy.py::_eff_restore`, `NO_CHANGE`; V12 B12a.64.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B12a's producer; `Item: B12a.65`, `[skip ci]`.

### B12a.66 — a crossing a person stands beside raises a question about the place · `16_PESSIMIST_WR_B` edit 4 · BUILD · HASH MOVER(behaviour)
- SOURCE: `proposals/16_PESSIMIST_WR_B_the_calamity_strains_and_breaks.md` edit 4 ("Owner: CORE's file; listed here with its gate because the Calamity is inert without it"; "lands in this batch with CORE's review"), "The gate" (the played reading); `verb_table.yaml`'s `restore` row (`referent_class_note`: "no question the realm delivers carries a Site among its referents").
- ADVANCES: none of the nine by itself; `restore` forms on a question the realm delivers (the source: "attempted 0/0/0" today).
- INSTRUCTION: `engine/season/queries/world_q.py::questions_for` (the source): "A new claim in a person's ledger whose Event is a `condition.band_crossed` or `site.ruptured` anchored on a Site at the rung he stands on is stamped as a `Site`-classed referent (`own_referents_of_class`, REM-21's term), so `restore` (and, at a broken Site, the Mend) forms for him." Where he stands is `place_of` (the `with` stem's one owner); the stamp goes through the same `_stamped` path the existing classes use.
- WHERE: `engine/season/queries/world_q.py` (`questions_for`).
- TESTS: `engine/season/tests/test_in35_lattice_coupling.py` gains (the source's name) `test_restore_or_mend_attempted_at_a_crossed_site`: "Played, three seasons, the wound planted: `restore` or the Mend is attempted at least once by a person standing at a crossed Site, in at least one of two seeds" — at two seasons (A-114), weight 250, the B12a.64 plant (so crossings occur in season 0), seeds 0 and 1; written before the edit and read red (no Site-classed referent). A hand-built check beside it: `test_a_witnessed_crossing_at_his_rung_stamps_the_site` (one person, one claim of a `condition.band_crossed` on a Site at his rung: `own_referents_of_class(..., {"Site"})` names it) `[ASSUMPTION: second test name — E-3]`.
- FALSIFIER and CONTROL: a crossing witnessed at a rung the person does not stand on stamps the Site; no `restore` attempted in the played test at either seed. Control: a world with no crossing has an unchanged question set (the seed-0 hash, if no crossing is witnessed in two seasons at the shipped weight, is equal, and the commit says so).
- GATE: `python -m pytest engine/season/tests/test_in35_lattice_coupling.py engine/season/tests/test_season_shape.py -k "restore or crossed or referent" -q` → pass; seeds 0 to 2, two seasons: executed and attempted `restore` before (`reading @<B12a.65's sha>`) and after, quoted.
- HASH MOVERS: "edit 4 moves the question set wherever a crossing is witnessed" (the source). Declared; re-pinned at B12a.99.
- EXPECTED RED UNTIL B12a.99: the realm pins, if a crossing is witnessed in their seasons.
- DEPENDS ON: EXISTS-IN-TREE `queries/world_q.py::questions_for`, `::own_referents_of_class`, `::place_of`, `World.class_of`; V12 B12a.64 (`site.ruptured`); review by the CORE owner at the batch close (the source).
- GLOSSARY: none.
- COST and TIER: small build at CORE's owner; `sonnet`, `high`; the close's review reads it as CORE's (an `opus` critic on the stamp's reach).
- LANDS IT: B12a's producer; `Item: B12a.66`, `[skip ci]`.

### B12a.67 — the `restore` roster sentence brought to the tree · `U5d_WR_owed_edits` §4 · BUILD · HASH EQUAL
- SOURCE: `proposals/U5d_WR_owed_edits.md` §4 ("`engine/season/rosters.yaml:1903-1906` says `restore` executes on the realm; `verb_table.yaml`'s `restore` row and eight arms read 0. Text for the orchestrator's next WR commit: the sentence reads 'formed nowhere since REM-22'. Same reading as `U5d_SE_owed_edits.md` §1 (one decision, two rows)"); "Land order: §4 (text), §1, §3, §2"; closes PES-WR R-4.
- ADVANCES: none (roster text).
- INSTRUCTION: `engine/season/rosters.yaml`, `wear_per_season`'s `note:`, the clause "⚠ CORRECTED (`24f`, 2026-09-30): `restore` now executes on the populated realm's SETTLEMENT fabrics (harbour, seam -- rate 10, a cohort stands beside them)" is rewritten: "`restore` is formed nowhere since REM-22 (its `verb_table.yaml` row: no question the realm delivers carries a Site among its referents) until `16_PESSIMIST_WR_B` edit 4 (B12a.66), and since then only where a person witnesses a crossing at the rung he stands on"; the rest of the note is kept. (The source's sentence predates edit 4, which lands before this item in U3's order; UNDECIDED 11.) The paired row of `U5d_SE_owed_edits.md` §1 is that file's item (B12b).
- WHERE: `engine/season/rosters.yaml` (`wear_per_season`, `note:`).
- TESTS: none (roster text; no reader parses the note).
- FALSIFIER and CONTROL: the note still says `restore` "executes" on the realm. Control: the seed-0 hash equal to B12a.66's; `git diff` of the commit touches only the note.
- GATE: `git grep -n "restore. now executes on the" engine/season/rosters.yaml` → no hit; `python -m engine.season.harness.register --check` → exit 0.
- HASH MOVERS: none.
- DEPENDS ON: V12 B12a.66.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `medium`.
- LANDS IT: B12a's producer; `Item: B12a.67`, `[skip ci]`.

### B12a.68 — a real execution reads as a killing · `U5d_WR_owed_edits` §1 (H-257) · BUILD · HASH EQUAL
- SOURCE: `proposals/U5d_WR_owed_edits.md` §1, "Named tests and call sites" §1; carries `audits/09_WR_audit.md` R-06 (H-257); U5d's own Status line places §1 in B12 "beside §3" `[ASSUMPTION in the source: U3 places no batch for §1]`; closes R-06's reader half (the lawful-basis half "waits on SC's verdict naming its party (A-38)").
- ADVANCES: none of the nine (a harness reading).
- INSTRUCTION: `engine/season/harness/strife.py::readers_for`, its `victim_held` reader: "The reader reads the death's `body` change as well as `exists` (one line; the audit's own decision)." At `aa31fd2` the line is `victims = {c.subject for c in e.changes if c.field == "exists"}`; it becomes `… if c.field in ("exists", "body")`. "The other half of H-257 (telling an execution from a killing by its lawful basis) is an interface need, not built: it waits on SC's verdict naming its party (A-38)."
- WHERE: `engine/season/harness/strife.py` (`readers_for`, `victim_held`); `engine/season/tests/test_strife_execution.py`.
- TESTS: (the source) "new function `engine/season/tests/test_strife_execution.py::test_a_hand_built_execution_reads_xe` … It plants a lawful execution whose `person.died` Event carries the `body` change, and asserts `victim_held` is true; control: the same Event with only the `exists` change (today's reader) is the failing reading the falsifier names." Written before the edit and read red.
- FALSIFIER and CONTROL: "The same world still reads KL" (the source). Control: the file's existing tests (`test_a_planted_fight_death_of_a_held_man_reads_xe_on_the_live_tenure`, `test_mutation_closing_the_tenure_one_tick_before_the_death_moves_xe_to_kl`) green unedited.
- GATE: `python -m pytest engine/season/tests/test_strife_execution.py -q` → pass; `PYTHONHASHSEED=0 python -m engine.season.harness.strife 2 0` → exit 0, its move table quoted (the source's "on a hand-built execution: the move reads XE" is the test above).
- HASH MOVERS: none ("Movers: none (harness)").
- DEPENDS ON: EXISTS-IN-TREE `harness/strife.py::readers_for`, `engine/season/tests/test_strife_execution.py`.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B12a's producer; `Item: B12a.68`, `[skip ci]`.

### B12a.69 — a witnessed recovery clears a believed wound · `U5d_WR_owed_edits` §3 · BUILD · HASH MOVER(behaviour)
- SOURCE: `proposals/U5d_WR_owed_edits.md` §3 (F-WR-23; "owed at PC's and CHAR's owner"), "Named tests and call sites" §3; `engine/season/queries/world_q.py::wounded_with`'s docstring ("⚠ STATED LIMIT -- NOTHING CLEARS A BELIEVED WOUND. Only `_eff_kill` writes a `(pid, "body", v)` Observation; `_eff_tend` and MATTER write none"); closes F-WR-23.
- ADVANCES: none of the nine by itself; "mended bodies stop drawing care they do not need" (the source's NERS line).
- INSTRUCTION:
  1. Open MATTER for a write that raises `Person.body` (`git grep -n "setattr(person, \"body\"\|\.body = " engine/season/loop`) and record what is found in the commit body (§5.7, SITE). At `aa31fd2` MATTER's bodies pass writes falls only (`loop/matter.py`, the `body_after` write); the "recovery step" the source names is CP-T10-04's (intake `:363`, B37p), which "makes bodies rise" — so only `_eff_tend` is edited here, and the recovery half is owed to CP-T10-04's item (its author is told in the receipt). If a recovery write exists at the item's open, it gets the same Observation in this commit.
  2. `engine/season/loop/effects_combat.py::_eff_tend` writes "a `(pid, "body", v)` Observation as `_eff_kill` does": its subject becomes `Subject.entity("persons", who, fields=("body",), observed=body_observed(who, whole))`, `v` the written (mended) body, "so a witness's claim of the wound is superseded by a claim of the mended body". The source's "carrying the ceiling" is not built as a second field: `v` is the written body, which for a marked man is his ceiling, and `wounded_with`'s comparison for another person (`v < condition_scale`) is unchanged, so a marked survivor stays stamped for his believers (the docstring's `[GAP: a believed ceiling is not carried]`, kept; UNDECIDED 12).
  3. `wounded_with`'s docstring: "NOTHING CLEARS A BELIEVED WOUND" becomes "a tend writes the mended body as an Observation (U5d_WR §3); MATTER's recovery does not yet", with the measurement re-taken (step 4).
  4. "Lands before `09_WR_provided_arcs.md` edit 2 and plan CP-T10-04 (each makes bodies rise and would otherwise leave stale beliefs and a growing `tend` tax)": `09_WR_provided_arcs` is B12b, CP-T10-04 is B37p; both later.
- WHERE: `engine/season/loop/effects_combat.py` (`_eff_tend`); `engine/season/queries/world_q.py` (`wounded_with`, docstring only); `engine/season/tests/test_season_shape.py`.
- TESTS: (the source) "new function `engine/season/tests/test_season_shape.py::test_a_witnessed_recovery_clears_a_believed_wound` … Plants a believed wound, runs `_eff_tend` to a recovery, and asserts the pair count of `tend` formed on the healed man reads 0; control: the same world without the Observation write reads the old non-zero count." Written before the edit and read red.
- FALSIFIER and CONTROL: "A `NoOpReceipt` refusal of `tend` on a man a witness saw mended" (the source). Control: a `tend` that heals nobody (already whole) is still refused `NoOpReceipt` and writes no Observation.
- GATE: `python -m pytest engine/season/tests/test_season_shape.py -k "wounded or tend" -q` → pass; "the docstring's measurement re-run (pairs forming `tend` on a healed man: 0, 3, 9 at seeds 0 to 2 today) reads 0 after a recovery is witnessed": seeds 0 to 2, two seasons, the pair count before (`reading @<B12a.68's sha>`) and after, quoted.
- HASH MOVERS: "Every run with a `tend`. Declared." (the source) — the Observation rides `body.changed`'s Event (`Event.observed` is folded by `World.content_hash()`). Re-pinned at B12a.99.
- EXPECTED RED UNTIL B12a.99: the realm pins.
- DEPENDS ON: EXISTS-IN-TREE `loop/effects_combat.py::_eff_tend`, `::body_observed`, `::_eff_kill` (the precedent), `queries/world_q.py::wounded_with`, `state/gate.py::Subject.entity` (`observed=`); V12 Batch B04 (`wounded_with`'s `(when, lap)` key after PCR-4).
- GLOSSARY: none.
- NAMES: in `wounded_with`'s docstring, `(when, round)` → `(when, lap)` (§5.10, B04).
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B12a's producer; `Item: B12a.69`, `[skip ci]`.

### B12a.70 — the order in which WR's draws land · `U5d_WR_owed_edits` §2 (a), (b) · POINTER · HASH —
- SOURCE: `proposals/U5d_WR_owed_edits.md` §2 ("No new edit: an ordering constraint on existing carriers, written so no builder flips a fixed-function arm"); (c) is B37's (U3 §4.1 rows 49–50).
- What the pointed section does: (a) `16_PESSIMIST_WR_B` edits 1–2 land before any non-zero `lattice_coupling` — met by B12a.63 and B12a.64 preceding B12a.71, which holds the flip for B98; (b) `09_WR_B_draws_not_thresholds` edits 1–2 land before the weather arm of `09_WR_B_weather_with_memory_and_the_year` — met by the first half of B12a preceding B12b. Target files: none of its own. Gate (the source's): "the control arm reproduces the base hash before the flip; the flip is one declared re-pin" — read at B12a.63 and B12a.64 (weight 0 equal) and at B98's flip.

### B12a.71 — the `lattice_coupling` flip and `wound=True` · `09_WR_world_motion` edit 1 (second commit), as `16_PESSIMIST_WR_B` amends it · HELD (B35's Mend; H-165/H-07's wear-0 kinds) · HASH —
- SOURCE: `proposals/09_WR_world_motion.md` edit 1 ("Then, as its own commit and its own mover: `lattice_coupling` 0 → 250 (H-235's swept arm) with `wound=True` the default. H-235's unblock names a second precondition, the wear-0 kinds … that is H-165/H-07's and is not decided here, so the flip waits on it"); `proposals/16_PESSIMIST_WR_B_the_calamity_strains_and_breaks.md` ("amends `09_WR_world_motion.md` edit 1's second commit … The flip does not [stand], until edits 1 and 2 below land"; "The weight's flip is a declared hash mover and its own commit, after the threadwork module"; edit 3: "Until that module lands the weight stays 0"); U3 §4.1 row 48; UNDECIDED 2.
- Not built in this batch. Trigger: `09_WR_B_threadwork_session_and_practitioner`'s Mend has landed (Batch B35) and H-165/H-07's wear-0 kinds are decided. Owner of the flip: B98 (`DIALS AT CONTROL`, D-22), one item there: `lattice_coupling` 0 → 250 and `build_realm(wound=True)` the default, one declared mover, its target `16_PESSIMIST_WR_B`'s gate as the dial line states, its control weight 0 reproducing the previous item's hash. The wound's Site kind stays Jordan's content (`09_WR_world_motion.md` edit 1, "`<a `site_kinds` member that has `band_floors`>`"; `U4_DOCUMENT_STATUS.md` §3.4: CONTENT, owner Jordan) and is set by the first half's item for that edit.

### B12a.72 — a zero-amount store move changes no store · H-138 · BUILD · HASH EQUAL
- SOURCE: `master/eval/E6.md:151` (H-138: "`loop/effects_economy.py:215 _eff_transfer` and `_shift` insert `kind: 0`; only at `default_transfer_amount` 0 (H-94's declared control arm, not shipped) … hash EQUAL at shipped arms; gate: at amount 0 a transfer is refused `NoOpReceipt`"), E6 carry-forward block 5 ("`H-138`: 'compare stores by value with zero-valued keys normalised out' (or do not touch the dict at amount 0)"); `engine/season/hole_register.yaml` H-138 (its `hole:` and `unblocks:`: reachable "at `H-94`'s own declared sweep point `amount = 0` … for any transfer whose giver or receiver does not already hold the swept `kind`", and since REM-2B for `exchange`'s `return_kind`); intake `:137`; D-10 (placed in B12a); closes H-138.
- ADVANCES: none of the nine; F9 stops reading a move of nothing as a move (`transfer.made`, `exchange.made` at amount 0).
- INSTRUCTION:
  1. `engine/season/loop/effects_shared.py::_shift` (the one body of every store move; E6 names `effects_economy.py`, where its callers are): at `amount == 0` it returns without touching either store — no `_debit`, no copy, no key inserted (E6's second fix shape; UNDECIDED 6). Its docstring gains the reason (H-138). The digest reader (`state/world.py`) is not changed.
  2. `engine/season/hole_register.yaml` H-138: closed by this commit (the row's closing text names `_shift` and the test), by the register's own closing convention.
- WHERE: `engine/season/loop/effects_shared.py` (`_shift`); `engine/season/hole_register.yaml` (H-138); `engine/season/tests/test_gate_observation.py`.
- TESTS: `test_a_zero_amount_transfer_to_a_side_without_the_kind_is_refused` and `test_a_zero_return_exchange_is_refused` (the row's own counterexample: a transfer at `amount=0` of a `kind` absent from both rungs' `stores` reads `transfer.refused` with `NoOpReceipt`, and neither rung's `stores` gains the key; the same for an `exchange` at `return_amount` 0) in `engine/season/tests/test_gate_observation.py` (E6 block 5's coined file, "`[ASSUMPTION: name]`"; created by B03's gate-observation items if they landed, else created here) `[ASSUMPTION: test names — E-3]`; written before the edit and read red (today the key is inserted and `transfer.made` is emitted).
- FALSIFIER and CONTROL: a zero-amount transfer still publishes `transfer.made`, or a rung gains a `kind: 0` key. Control: at the shipped `default_transfer_amount` 1 the seed-0 to seed-2 one-season hashes equal B12a.69's (the row: "nothing at the shipped `default_transfer_amount = 1` fixture"); `engine/season/tests/test_in33_exchange.py` and `test_season_shape.py`'s H-94 sweep test (all three points executed) green, the 0 point's readings quoted before and after.
- GATE: `python -m pytest engine/season/tests/test_gate_observation.py engine/season/tests/test_in33_exchange.py -q` → pass; `python -m pytest engine/season/tests/test_season_shape.py -k "transfer or exchange" -q` → pass; `python -m engine.season.harness.register --check` → exit 0; the shipped-arm hash → equal.
- HASH MOVERS: none at the shipped arm.
- STOPS IF: at the item's open `_shift` (or each caller) already returns before touching a store at amount 0 — then the item is a POINTER and the row is closed with the landing commit cited.
- DEPENDS ON: EXISTS-IN-TREE `loop/effects_shared.py::_shift`, `::_debit`, `loop/effects_economy.py::_eff_transfer`, `::_eff_exchange`, `data/fixtures.py` `default_transfer_amount` (H-94); V12 Batch B03 (its gate-observation items, which may create `test_gate_observation.py`).
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B12a's producer; `Item: B12a.72`, `[skip ci]`.

### B12a.99 — re-pin and close readings · `V12_STRUCTURE_part4.md` E-1, E-2 · BUILD · HASH MOVER (the re-pin)
- SOURCE: `V12_STRUCTURE_part4.md` E-1 ("Every batch ends with a re-pin position … re-record the realm and corpus pins that any item in the batch moved, once; write the batch's readings"), E-2; `V12_STRUCTURE_part2.md` §5.9, §5.12; `IS-A-12` (the readings written into the conjuncts' `reading:` records; `status:` not edited).
- ADVANCES: the requirement readings the head's `REQUIREMENT:` line names ("re-read only", `V12_STRUCTURE.md` §2.2's B12a row).
- INSTRUCTION:
  1. Re-pin once, for the whole batch: the realm pins in `engine/season/tests/_realm_goldens.py` (B02's one pin file) and every golden B02 routes through it, at seeds 0 to 2, one and two seasons, `PYTHONHASHSEED=0`, read against the previous batch's close (`reading @<sha>`). The commit says "re-pin" and names each mover it carries: from this half, B12a.54 (`endowment_mode`), B12a.55 (`granary_seasons`), B12a.56 (`larder_walk`), B12a.62 (`hunger_severity_draw`), B12a.66 (the Site-classed stamp, if a crossing is witnessed in the pins' seasons), B12a.69 (the tend Observation); from the first half, each mover its items declare. Behaviour controls read, not hashes: with every switch of the batch at its control the hashes equal the previous close's.
  2. The batch's readings, in the commit body (`V12_STRUCTURE_part2.md` §5.12): `register --requirements` (nine lines), `m1_acceptance --summary`'s verdict line, the head's named conjuncts' readings with their tree, the `BUILT OUT`, `ENGINES` and `NULL SCENES` lines before (`reading @<sha>`) and after, the readings each item of this half asked to be quoted, and the batch's measured wall time; the conjuncts' `reading:` records are written in `engine/season/requirements.yaml`; `status:` is not edited.
  3. The full suite once (CLAUDE.md §0.4: this batch touches engine core and registries); the confirming CI push follows the close's fixes (the skill, CHECKPOINTS AND BASELINES).
- WHERE: `engine/season/tests/_realm_goldens.py` and the goldens it owns; `engine/season/requirements.yaml` (`reading:` records only).
- TESTS: every `EXPECTED RED UNTIL B12a.99` test turns green.
- FALSIFIER and CONTROL: a pin moved by no declared mover (then an item's HASH line was wrong: the close stops and names it). Control: every switch at its control reproduces the previous close's hashes.
- GATE: the head's `BATCH GATE`, with this half's lines; `python -m pytest tests/valoria -q -n auto` and the engine suites `python tools/tests_for_diff.py --base <batch-start-sha>` names → pass.
- HASH MOVERS: the re-pin itself.
- DEPENDS ON: every position of B12a.
- GLOSSARY: the close reads every glossary row this batch's items named against the code it landed (`STAGES.md`, "The glossary always matches" rule 2): from this half *endowment*, *field*, *treasury*, *broken (Site)*, *rupture*, *knit*.
- COST and TIER: reading and a re-pin; `sonnet`, `high`; the flips' readings and the close's terminal critique `opus`.
- LANDS IT: B12a's producer; `Item: B12a.99`, the batch's last `Item:` commit, pushed without `[skip ci]`.

| STOP. Batch B12a-world-motion-and-ground closes here |
