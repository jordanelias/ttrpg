# Valoria — Master Workplan v8, part 3: orchestration · the pre-flight · Batch 0 · Batch 1 (the retirement head)

## Status: PROPOSED 2026-10-01 — directed by Jordan; adoption on merge (ED-1094). Same status and held-back list as `valoria_master_workplan_v8.md`; this part carries no decision of its own.
## Reads after `workplans/valoria_master_workplan_v8_part2.md`. Owns THE ORDER: the batches, the serial edges, the file census, and the item specs for Batches 0–1.
## Grade under `CLAUDE.md` §0.2: `paper`. Line numbers drift; re-derive every site by its symbol (`CLAUDE.md` §0.1 pt 3).

---

## O. ORCHESTRATION

### O.1 The batches, in dependency order

| batch | items, in serial order (`{…}` = a parallel lane in its own worktree) | R-rows moved | golden / hash moves (declare each) | close |
|---|---|---|---|---|
| **0** | `B0-CI` | — (CI green on `main`) | none | `/code-review` only; no terminal critique (generated artifacts re-derived by their own tools, one ledger ref corrected) |
| **1** | `28-iii` → `29a` → `29b` → `20-iv` → `29d` → `29c` → `28-0` follow-up | R-04 (reason 2, by deletion); R-07 if `20-iv` gets fields fought | **none** for the deletions — `build_realm(0)`'s season `content_hash` must not move (the control); `20-iv` declares a realm hash move only if a field is fought | full `methodology-close`; terminal Opus critique **proportionate** — `28-iii` deletes the last campaign-scale regression oracle, and `20-iv` carries a design candidate |
| **2** | IN: `11-fix` → `11` (baseline) → `8` → `ED-FI-0009` → `10` → `14` (+ `R05-THREAD`) → `17` → `13`-rest → `13d-iii` → `11` (re-take) → `21`-rest; `{WR: 27}`; `{MB/PC: LADDER-MBPC}` (`_part5` §J, "not on the queue") | R-01, R-02 (measured), R-04, R-05, R-06 (reason 1), R-07, R-09 | `8`: none (assert equal); `ED-FI-0009`, `10`, `14`, `17`, `13`-rest: corpus/realm pins move (declared per step); `13d-iii`: `build_realm` census + hash (declared) | full `methodology-close`; terminal critique **proportionate** — `10` and `14` are judgment nodes and `11` is a number nobody else reproduces |
| **3** | SC: `22` steps 11–16 → `22a` → `23` → `22b`; IN: `29f` → `29e` → `29a`-ms → `2-ii`; `{SE: 24h P5}`; `24h` P6 after `22`'s `verb_table.yaml` edits | R-05 (`speak`, `determine`), R-09 (a fourth graded chain), M2 (THE BAR) | `22`: corpus + realm hash move (declared); `2-ii`: none (byte-identity control) | full `methodology-close`; terminal critique **proportionate** — `22` is the largest new mechanism in the plan |
| **4** | one sub-batch per Jordan ruling, as each lands: cells commit (J-1) → H7 → H3 → H9 → `12` → H10 (C3) → H11 (C4) → `12e`; `19b` (J-2); J-3's verbs; `9` (J-7); `24g` (J-6); `24h` P7 (J-10); `26` (J-9) | R-05, R-06, R-08; R-04 (J-3) | cells commit: headless + corpus hash move, `resolvable_verbs()` count moves (declared) | cells commit: full pipeline, terminal critique **proportionate**; `24g`, `26`, `24h` P7: `/code-review` + `/simplify` only — one value or one record each |

**Why this order.** Batch 1 first because it is gate-free, purely subtractive, and every later batch
touches less code once the spine is gone (`29b` removes `game_state.Faction`, which `20-iv`'s test and
the descriptor faction block depend on). Batch 2's IN chain is serial because five of its positions
share `rosters.yaml`/`verb_table.yaml`/`test_season_shape.py` (O.3). `11` runs **twice** in Batch 2 —
once on HEAD after `11-fix` (the baseline the row needs today), once after the verb set has moved — so
the second number has a control taken by the same instrument on a declared earlier tree. Batch 3 waits
on Batch 2 because `22`'s `determine` needs `13d-iii`'s rung purview, and `24h` P6 / `29f` need `14`.
Batch 4 opens only on rulings.

### O.2 Hard serial edges (live ones only)

Carried from the retired 2026-09-18 plan (§3.9) and 2026-09-28 plan (§3.5); edges both of whose ends
are finished are spent and omitted (`_part6` §H lists them). `isolation: worktree` defers an edge to
the merge; it never removes it.

| # | edge | why | origin |
|---|---|---|---|
| E1 | `28-iii` → `29a` → `29b` → `29d` → `29c` | import direction: overview imports settlements and world; factions imports settlements; world imports settlements | 09-28 §3.5.1 |
| E2 | `27` → `29a`-ms; `27` → `29f` | `threadwork/sim/{co_movement,opposing}.py` import `ms_track.apply_ms_delta` and `knots.sustain_knot` | 09-28 §3.5.2 |
| E3 | `14` → `29f` → `29e` | the `tie / knot` effect first; then `conviction.py` ← `knots.py` | 09-28 §3.5.3 |
| E4 | `29b` → `2-ii`; `22` → `2-ii` | the `parliamentary_*` modules; the prize-row repoint | 09-28 §3.5.4 |
| E5 | the cells commit ↔ `8`, `9`, `10` | same `fight` row and combat wrapper (`10` now writes on `fight`, `_part4` §`10`). Either order; never interleaved | 09-18 §3.9.10, widened here |
| E6 | `29b` → `20-iv` | `29b` deletes `massbattle.py::{resolve_mass_battle,_faction_to_unit,_morale_start_from_stability}`; `20-iv` carries d.1 to `resolve_field` and re-pins `test_mass_battle_d1_morale_baseline.py`, which constructs a `game_state.Faction` — land `20-iv` **immediately** after `29b` or that test is red between commits | new (Fable risk) |
| E7 | `8` → `ED-FI-0009` | both edit `seam/ladder.py` | new |
| E8 | `8` → `ED-FI-0009` → `10` → `14` → `17` → `13d-iii` | shared `rosters.yaml`, `verb_table.yaml`, `engine/season/tests/test_season_shape.py` pins | new |
| E9 | `14` → `24h` P6 | the `repudiate` row and its effect | new |
| E10 | `11-fix` → `11` → `21`-rest | the instrument, then the number, then the records quoting it | new |
| E11 | `13d-iii` → `22` steps 11–12 | `determine`'s bench is a purview read; rungless seats make it empty | new |
| E12 | `28-iii` → `28-0` follow-up | the twelve OI-17 targets `engine/tests/test_pipeline_reach.py` names by string die with that file | 09-28 §8.4 |
| E13 | every position → its own forward sweep's `requirements.yaml` / `hole_register.yaml` edits | the shared record files; never edited from two worktrees at once | §0.4 |

### O.3 File census — open positions × shared files

| file | edited by | consequence |
|---|---|---|
| `engine/season/verb_table.yaml` | `10` (`fight`), `14`, `R05-THREAD`, `ED-FI-0009`, `22` (`speak`, `determine`), `24h` P6, `19b`, cells commit | serial in the IN/SC chains (E8, E9) |
| `engine/season/rosters.yaml` | `8`, `10`, `14`, `13d-iii` (`titles` block deleted), `22` (prize rows, `chronicle`), cells commit | serial (E8) |
| `engine/season/seam/ladder.py` | `8`, `ED-FI-0009`, `2-ii` (veto `extension=`) | E7; `2-ii` is Batch 3 |
| `engine/season/loop/effects_combat.py` | `10`, `20-iv` (only if an effect change is needed), cells commit | E5 |
| `engine/season/loop/effects_information.py` | `14`, `ED-FI-0009`, `22` | serial |
| `engine/season/loop/effects_governance.py` | `14` | — |
| `engine/season/decision/options.py` | `14` | — |
| `engine/season/queries/person_q.py` | `17`, cells commit | Batch 2 vs 4 |
| `engine/season/queries/world_q.py` | `20-iv`, `24h` P5 | Batch 1 vs 3 |
| `engine/season/harness/populated.py` | `13d-iii` | — |
| `engine/season/harness/corpus_run.py` | `17` | — |
| `engine/season/cases/exercises/*.yaml` | `13`-rest | parallel authoring; merges after `17` |
| `engine/season/offices.yaml` | `13d-iii` | — |
| `engine/season/tests/test_season_shape.py` | `8`, `10`, `14`, `17`, `13`-rest, `22` | every pin re-taken serially |
| `engine/season/requirements.yaml`, `engine/season/hole_register.yaml` | every forward sweep; `11`, `21`-rest | E13 |
| `references/module_contracts.yaml` | `28-iii`, `29a`, `29b` | E1 |
| `references/restructure_ledger.md` | `28-iii`, `29a`–`29f`, `2-ii`, `28-0` follow-up | serial; appended rows conflict at the file end |
| `.github/workflows/valoria-ci.yml` | `28-iii` (sim-regression re-scope), `2-ii` (the job folds) | Batch 1 vs 3 |
| `tests/valoria/test_engine_does_not_import_systems.py` | `28-iii` (snapshot guard), `29b` (fixtures), `2-ii` | E1, E4 |
| `systems/threadwork/sim/*` | `27`, `29a`-ms (import site), `29f` (import site) | E2 |
| `systems/mass_battle/sim/massbattle.py` | `29b` (deletes the old entry), `20-iv` | E6 |

**Parallel lanes this census permits:** Batch 2 `{WR: 27}` (only `systems/threadwork/` and
`tests/valoria/test_coherence_elastic_plastic.py`) and `{MB/PC: LADDER-MBPC}` (only
`registers/editorial_ledger_{mb,pc}.jsonl`); Batch 3 `{SE: 24h P5}` (`queries/world_q.py` or
`faction_q.py`, read-only Query). Nothing else runs in parallel. Fable proposed FI `ED-FI-0009` as a
parallel lane; it shares `verb_table.yaml` and `effects_information.py` with `14`, so it is serial
here (a departure, recorded in the receipt).

### O.4 The run discipline every batch uses

- **Driver:** `methodology-execute` (`CLAUDE.md` §9): `valoria-author` builds and commits each
  position cheaply; `methodology-close`'s pipeline (agonist/antagonist → `/code-review` → `/simplify`
  → `layer-conformance` → terminal Opus critique where O.1 says proportionate) and the pytest suite run
  **once per batch**. The per-step cadence (main file §0.4) runs inside each step, minus the suite.
- **Share the reading** (`CLAUDE.md` §10): one Haiku `valoria-measure` extract per batch, from the
  batch's reading list, handed to every producer. Fire one producer, await its first token, then fan
  out.
- **Receipt (fixed, every producer):** `POSITION <handle> | COMMIT <sha> | FILES <paths> | RAN
  <commands, exit codes> | FALSIFIER <test::name → pass/fail> | HASH <unchanged | moved old→new,
  declared> | HOLES <H-ids touched> | NOT DONE <named remainders>`.
- **Commit shape:** `[scope] <≤72-char subject naming the handle>`; body cites `PP`/`ED`; scopes per
  `CLAUDE.md` §2. Ids from `references/id_reservations.yaml` `next_free` at allocation time, never
  max+1.
- **Tiers:** `haiku` extraction and measurement; `sonnet` bounded builds, deletions, re-hosts; `opus`
  judgment nodes (verify, critique, any effect body with a design choice). Per step below.
- **Stopping rule:** main file §0.5. Revert and register; never widen.

---

## P. PRE-FLIGHT — the checks Fable could not settle read-only

**Settled 2026-10-01 while writing this plan** (no re-run needed unless the tree moves):

| # | check | outcome |
|---|---|---|
| S-1 | `cat .git/shallow` | full clone in the writing container; re-check in yours |
| S-2 | `register --requirements`; `m1_acceptance --summary` | met 1 · partial 5 · not_met 3; M1 NOT MET, row 3 FAIL 1/9 [RAN, 29 s] |
| S-3 | `python -m pytest engine/season/tests -q -k we_only_a_verb_that_declares_contests_can_be_graded_today` (Fable's suspected known-red) | **1 passed** — not red; no Batch-0 fix for it |
| S-4 | `gh run list --branch main --limit 3` + `gh run view 36803379833 --log-failed` | `unit-tests` FAILS on `main` (7 tests) — the `B0-CI` row |
| S-5 | `ls systems/social_contest/sim/contest` | present, 16 files — `2-ii` still has its subject |
| S-6 | `grep -n "GD-1\|victory" engine/season/hole_register.yaml` | nothing — GD-1 is not registered; `28-iii` registers it |
| S-7 | `grep -rn "def ambitions\|def stance_delta" engine/season` | nothing — `17` and `10` are unbuilt |
| S-8 | invariant 4's per-conjunct `emits_on_refusal` schema | **built at `19`**: `data/verbs.py` reads a clause-keyed mapping into `refusals_by_clause`; `engine/season/tests/test_u7_remit.py` asserts it. `23`'s "invariant 4 widened" reduces to whatever row still uses the flat form where a conjunct is failable — re-check there |
| S-9 | `references/module_contracts.yaml` `composition_roles` | **25 keys** (Fable read 26): 1 survivor (`mass_battle.resolve_field`), 7 spine role rows, 10 `snapshot_state.*`, `world_gen_settlements`, 3 `parliamentary_*`, 3 orphans (`rs_track_delta`, `territory_transfer_candidate/proposal`) |
| S-10 | `write_matrix.yaml` `(Person, stance)` | `steps: [RES, ENC]`, `class: ACTS`, `social: "true"` — the fact that re-scopes `10` (`_part4`) |

**Still open — run these first, record outputs in Batch 1's first receipt:**

| # | command | what it decides |
|---|---|---|
| P-1 | `python -m pytest engine/tests -q` (serial) | `28-iii`'s baseline: which `engine/tests` pass before deletion |
| P-2 | `python -m pytest tests/valoria/test_mc_v18_is_deprecated.py tests/valoria/test_engine_does_not_import_systems.py -q` | `ALLOWED_IMPORTERS` = the three `engine/tests` files; `NESTED_BASELINE = 0` |
| P-3 | `python tools/export_composition.py --check`; `python tools/valoria_local.py --staged` | the composition export round-trips before `28-iii` edits it |
| P-4 | `cd proposals/2026-09-04-degree-sweep && python wd_chunk.py none default 0 36 && python wd_chunk.py none default 0 36` (same cell twice) | `11-fix`'s determinism attack: if `probed` differs between two runs of the SAME arm, the break is a determinism defect, not a property — stop and register |
| P-5 | from one `populated.run(4, 0)` (or `aperture 4 0`'s realm section), print each `march.refused` Event's `observed` / reason | **why ENCOUNTER refuses all 11 realm marches** — if it is a missing defender/garrison, `20-iv` is the fix; if it is H-149's target restriction or `_survives`, it is a design question and `20-iv`'s falsifier must not assume fields get fought |
| P-6 | for one `corpus_run` case, list the `questions_for` referents offered to a seated person, and compare with `build_realm(0)` (H-175) | why the 143 cases never give `march` a referent — a measurement for R-04's table, not a build |
| P-7 | `python -m engine.season.harness.arms` default invocation, once, end to end | `28-i`'s successor instrument has never run end to end; `28-iii` deletes the oracle it replaced, so confirm the successor runs before deleting |
| P-8 | `python -m pytest tests/valoria -q -n auto` **once**, only if `B0-CI` has landed | confirms the container's known-red set is empty (§0.4 rule 1: CI cannot tell you which reds are the clone's) |

---

## B0. BATCH 0 — main's CI is red

**`B0-CI` · IN · gate — · sonnet · `[fix]`.** CI's `unit-tests` job has failed on every push to `main`
since at least 2026-09-30 22:37, seven tests, the same seven `ebb43bf0`'s message lists as
pre-existing. A red `main` hides every later regression, so it is the first fix (`CLAUDE.md` §0: *"If
something broken blocks the milestone, fix it minimally, without adding a guard."*).

| failing test | cause (from the CI log) | minimal fix |
|---|---|---|
| `tests/valoria/test_forked_status.py::test_the_fork_rows_name_a_real_ref` | `FORK:6f740d9` names a commit that exists nowhere (a pre-squash branch commit of PR #439) | re-point each such row to a reachable commit where the file existed — the parent of the squash commit that deleted it; verify each with `git cat-file -e <ref>:<path>` |
| `test_forked_status.py::test_the_evacuated_content_is_actually_at_the_ref` | unfollowable rows 78 → 87 (`UNRESOLVABLE_CEILING = 78`, a ceiling) | the same re-point; the count returns to ≤ 78. Never raise the ceiling |
| `tests/valoria/test_link_values_pointers.py::test_links_current` | committed `engine/engine_params/value_pointer_links.json` drifted | re-derive with `tools/link_values_pointers.py`'s own build (`CLAUDE.md` §0.05 cl. 3 — never by hand) |
| `tests/valoria/test_tool_input_paths_resolve.py` ×2 | `tools/build_engine_atlas.py` declares `EXEC_MAP`/`EXEC_TRACE` paths `28-i` retired | remove the two constants and their readers, or retire the tool if nothing calls it — check `references/ci_checks_registry.yaml` first |
| `tests/valoria/test_export_sim_params.py` ×2 | `sim_params.json` drifted; `_SCAR_DP` cited at `loop/effects.py` after the effects split | `python tools/export_sim_params.py --build`, then `--check` |

⚠ **LANDED while this plan was being written: `f6d7af27 [fix] Clear main's red Validator Unit
Tests (7 pre-existing failures)`** — `sim_params.json`, `value_pointer_links.json`,
`restructure_ledger.md` (`FORK:6f740d9` → `FORK:c9daad6`), `tools/build_engine_atlas.py`,
`tests/valoria/test_engine_atlas.py`. **This item reduces to its falsifier**, run once on the push that
carries it; it leaves the plan when CI reads green. **FALSIFIER:** the seven named tests pass in one run of their four files; `gh run list
--branch main` shows `unit-tests` green on the next push. **What runs:** those four test files only
(§0.4 rule 2). **Hash:** none. **R:** none.

---

## B1. BATCH 1 — THE RETIREMENT HEAD

**Reading list** (one Haiku extract, handed to every producer): this part's B1 items; `_part6` §D
(the dispositions carried from the 2026-09-28 plan's `_part2` §1 — every spine file, role, tree and
importer); `references/module_contracts.yaml` `composition_roles:` and `adapters:`;
`tests/valoria/test_mc_v18_is_deprecated.py` `ALLOWED_IMPORTERS`;
`tests/valoria/test_engine_does_not_import_systems.py` (`BASELINE_TOTAL`, `NESTED_BASELINE`,
`PATH_SEAM_ALLOWED`, the snapshot-role guard, the `systems.factions` fixtures);
`tests/valoria/test_wiring_validation.py`'s adapters rule; `.github/workflows/valoria-ci.yml`'s
`sim-regression` job; `tools/m1_acceptance.py`, `tools/valoria_local.py`,
`references/ci_checks_registry.yaml` (every `mc_v18` mention); `engine/tests/test_pipeline_reach.py`
`_OI17_FULL_MODULE_ENTRYPOINTS`; the `game_state` importers under `systems/`;
`systems/threadwork/sim/{co_movement,opposing}.py` import sites;
`architecture/meta/04_CODE_ARCHITECTURE.md` §A.2, §C.5, the provider-returns-a-Margin rule.

**The control for the whole batch:** record `build_realm(0)`'s 1-season `World.content_hash()` before
the first commit; every deletion commit must reproduce it exactly. A move is a failure, not a re-pin.

### `28-iii` · SPINE-DELETE · IN · gate — · `sonnet` build, `opus` verify · `[cleanup]`

**What goes, in one commit or a short serial run** (the 2026-09-28 plan §3.4 d, carried, counts
refreshed):
1. `engine/mc_v18.py` **and** `tests/valoria/test_mc_v18_is_deprecated.py`, together — but first reach
   `ALLOWED_IMPORTERS == set()` and run that test green at that intermediate state.
2. `engine/autoload/{engine_clock,season_manager,scene_slate,victory,npc_ai}.py`. `game_state.py`
   **stays until `29b`** (eight `systems/` importers).
3. `engine/cross_scale/` whole (`__init__`, `scene_dispatch`, `combat_bridge`, `handoff_rules`,
   `zoom_in_out`).
4. `systems/overview/sim/season.py` with its `season_driver` role row (`export_composition --check`
   imports every target, so row and module go together).
5. `game_state.py::{serialize_world,restore_world}`, the ten `snapshot_state.*` role rows, and the
   snapshot-role guard in `test_engine_does_not_import_systems.py`
   (`test_every_snapshot_state_role_resolves_to_something_restore_world_can_call`).
6. Role rows `season_driver`, `faction_action`, `accounting`, `scene_builder.contest`,
   `scene_resolver.contest`, `contest_side.a/.b`; and the three orphans `rs_track_delta`,
   `territory_transfer_candidate`, `territory_transfer_proposal` (re-read the "kept named" ruling at
   their rows and record its expiry — `ID-13`).
7. `module_contracts.yaml`'s `adapters:` block with `test_wiring_validation.py`'s
   adapters-resolve-to-`engine/cross_scale/` rule.
8. `FORK:` rows (exact file, reachable ref) for `engine/tests/{test_combat_bridge_seam,test_f7_smoke_oracle,test_mc_v18_regression,test_pipeline_reach,test_world_population}.py`
   and `tests/valoria/test_engine_clock_phases.py`. `test_accounting_accord_drift_probe.py` survives to
   `29a`.
9. `valoria-ci.yml`'s `sim-regression` job re-scoped to what remains in `engine/tests`.
10. The text that names the spine: `references/ci_checks_registry.yaml`, `tools/valoria_local.py`,
    `tools/m1_acceptance.py` (row 1's "re-pointed from engine/mc_v18" history line may stay as history).
11. Register GD-1 in `hole_register.yaml` as an `ABSENT_RULE` row: *"no season-side ending/victory
    condition; `ENDINGS_CLASSIFIED.yaml` + `forced_by_threshold` are the ending vocabulary; `20-ii`'s
    observable '≥1 faction-scale ARC ends' is its precondition"* (S-6). Not a build item, not a question.
12. `references/module_contracts.yaml`'s `engine_clock` contract row: say which code it now describes
    (`loop/driver.py` + `loop/calendar.py`) or mark it retired — main file §1 M3's forward note.

**What runs:** P-1/P-2/P-3 before; after: `python -m pytest tests/valoria/test_engine_does_not_import_systems.py tests/valoria/test_wiring_validation.py -q`,
`python tools/export_composition.py --check`, `python -m pytest engine/tests -q`.
**FALSIFIER:** an `ast` walk over every tracked `.py` finds an import of `engine.mc_v18`,
`engine.autoload.(engine_clock|season_manager|scene_slate|victory|npc_ai)` or `engine.cross_scale` →
fail; the batch control hash moves → fail; `test_pipeline_reach.py` skipped rather than forked → fail.
**Hash:** none (the control). **R:** R-04 reason 2's "not joined" clause dies by deletion (a `21`-rest
record edit, after). **Lens B (must be READ, not passed):** `04 §A.2`'s module table, §C.5's routes, the
provider-returns-a-Margin rule; `ID-13` over the deleted registry rows. **Lens A:** the `FORK:` rows.
**The cost, stated (carried from the 2026-09-30 revision §1.5):** deleting `mc_v18` is an E gain (one
engine, one vocabulary), **not an S gain**, and it removes the last campaign-scale regression oracle;
`28-ii`'s hash pin is a tripwire, not a balance instrument, and `CLAUDE.md` §7 records the gap as open.

### `29a` · overview, minus `ms_track` · IN · gate `28-iii` · `sonnet` · `[cleanup]`

`systems/overview/sim/{accounting,ci_track,ip_track,rs_track}.py`, the `accounting` role row if
`28-iii` left it, `engine/tests/test_accounting_accord_drift_probe.py` → `FORK:`. **`ms_track.py`
STAYS** until `27` (E2). The Accord / CI / MS / PT / insurgency clocks have no season analogue, by
architecture (`loop/census.py`: *"NO CLOCK GENERATES ANYTHING"*; ED-WR-0011 option A).
**FALSIFIER:** `python -c "import systems.threadwork.sim.co_movement"` still succeeds and
`apply_ms_delta` resolves; `grep -rn "systems.overview" engine systems tools tests` returns only
`ms_track` sites. **Runs:** `pytest engine/tests -q`; `export_composition --check`. **Hash:** none.

### `29b` · factions + `game_state.py` + the descriptor faction block · IN · gate `29a` · `sonnet` build, `opus` verify · `[cleanup]`

- **Modules:** `systems/factions/sim/*` (all remaining), `engine/autoload/game_state.py` (+
  `MULTS`/`ACCORD_MAP`/`PT_MAP`). Anything still imported from it that is substrate
  (`canonical_pt`/`accord`, `ALL_PLAYABLE_15`/`STARTING_*`) moves to `engine/substrate/`
  (`canon_buckets`, `world_initial_state`) if it is not already there — check the call sites first.
- **`systems/social_contest/sim/parliamentary_{vote,stay}.py`** are orphaned at this instant: delete them
  here with `FORK:` rows, or leave them to `2-ii` — say which in the commit.
- **Roles:** `parliamentary_vote/motion/vote_declaration`, `world_gen_settlements`.
- **Descriptor block:** `references/descriptor_registry.yaml`'s faction-stat block,
  `engine/substrate/descriptors.{FACTION_STATS,faction_bounds,assert_faction_roster_is_covered}`,
  `tools/export_descriptors.py`'s faction validation — `ID-13` once `Faction` is gone.
- **`massbattle.py::{resolve_mass_battle,_faction_to_unit,_morale_start_from_stability}`** — they read
  `game_state.Faction` duck-typed and die with it. `20-iv` follows **immediately** (E6).
- **Tests to `FORK:`**, with their EDs closing at ladder step 2: `engine/tests/test_parliamentary_action.py`,
  `tests/valoria/test_{faction_write_sweep,faction_stat_bounds,mass_seizure_accord_write,faction_obstacle_conventions}.py`;
  one test each from `test_descriptors_runtime.py` and `test_world_initial_state.py`; the
  `systems.factions` fixtures in `test_engine_does_not_import_systems.py` re-pointed to a retained
  subsystem.
- **Handoff rows closed with the citation:** `HANDOFF_FA.md` (the `score/2` row; writes via
  `game_state.Faction.adjust`), `HANDOFF_MB.md` (`_faction_to_unit` d.1).

**Runs:** `pytest engine/tests tests/valoria/test_engine_does_not_import_systems.py tests/valoria/test_descriptors_runtime.py tests/valoria/test_world_initial_state.py -q`;
`python tools/export_descriptors.py --check`; `export_composition --check`.
**FALSIFIER:** `python -c "import engine.autoload.game_state"` raises `ImportError`;
`BASELINE_TOTAL = 0` holds; `test_season_providers_are_registered.py` still finds `mass_battle`; the
batch control hash holds. **Hash:** none.

### `20-iv` · d.1 + terrain/garrison on the season path · MB/IN · gate `29b` (E6) · `opus` (a design candidate to attack) · `[simulation]`

- **d.1:** `resolve_field`'s units take `morale_start` from season-native faction state. **Candidate
  (ladder step 5, carried from the 2026-09-28 plan §5.2):** the members' `commit`-Tenure `degree` — F.4's
  own reading and the input `Faction.head` already uses. **Attack it at the build;** if the attack lands,
  it becomes the MB lane's question, run through the ladder before it reaches Jordan.
- **Terrain and garrison (H-150):** a rung→province map off `scale_of_rung` plus `harness/populated.py`'s
  settlement ids ↔ `systems/settlements/valoria_geography_v30.yaml`; call
  `systems/mass_battle/sim/terrain.py::terrain_row_for_territory(tid, fort_level)` with
  `queries/world_q.py::fortification_of`. H-150 closes only if `fortification_of` is read on the battle
  path — grep the call site.
- **Files:** `engine/season/seam/wrappers/mass_battle.py`, `engine/season/queries/world_q.py`,
  `systems/mass_battle/sim/{massbattle,terrain}.py`, `tests/valoria/test_mass_battle_d1_morale_baseline.py`
  (re-pinned against `resolve_field`). Effect target only if an effect-level change is needed:
  `loop/effects_combat.py::_eff_march`.
- **Read P-5 first.** If ENCOUNTER refuses the realm's marches for a reason this position does not
  touch, the realm will still fight no field; the falsifier is then the constructed one below and the
  commit says so.

**Runs:** `pytest engine/season/tests/test_march.py engine/season/tests/test_mass_battle_provider.py tests/valoria/test_mass_battle_d1_morale_baseline.py -q`;
`aperture 1 0` before/after. **FALSIFIER:** a fought field with a garrisoned defender resolves
differently from an ungarrisoned one, with `≥ 1` fought field asserted in the test; `fortification_of`
has a caller on the battle path. **Hash:** declared if any realm field is fought (none today).
**R:** R-04 (strategic texture); R-07 if fields get fought (M4's stance write becomes reachable).

### `29d` · world · IN · gate `29b` · `sonnet` · `[cleanup]`

`systems/world/sim/{npe,insurgency_pipeline,miraculous_event,restoration_movement}.py`;
`tests/valoria/test_conviction_roster_single_owner.py`'s `systems.world` site re-pointed (MOD 4 closes).
**Re-gated off `10`** (answered at ladder step 5, A-6): `requirements.yaml`'s retire gate is "the loop
expresses the scale", and `npe.py` has no season reader; `insurgency_pipeline.py`'s successor design is
`24h` P5 (a Query), which reads, not imports. **If the verify node disagrees, `29d` waits for `10`** and
nothing else moves. **FALSIFIER:** no importer of `systems.world` remains (`grep -rn "systems.world"`);
`test_conviction_roster_single_owner.py` green. **Hash:** none.

### `29c` · settlements `.py` · SE · gate `29b`, `29d` · `sonnet` · `[cleanup]`

`systems/settlements/sim/*.py` (six modules); `tests/valoria/test_settlement_temperament_drift.py` →
`FORK:`. **`systems/settlements/valoria_geography_v30.yaml` STAYS** — `terrain.py` reads it (A7). Moving
it to `references/` is a choice, per the `world_initial_state.yaml` precedent; not made here.
`ED-SE-0052`'s `fort_level`/`facility_tier` readers resolve to `Site.condition`/`fortification_of`.
`adjacency.py` has no successor: the season has no province graph (`move` re-homes by `contain`; H-149
restricts `march` targets) — record that, invent no graph. **FALSIFIER:** `terrain.py` still loads the
YAML; no importer of `systems.settlements.sim` remains. **Hash:** none.

### `28-0` follow-up · the rest of the orphan set · IN · gate `28-iii` (E12) · `sonnet` · `[cleanup]`

The twelve `_OI17_FULL_MODULE_ENTRYPOINTS` targets that waited on `28-iii` (every one except
`systems/threadwork/sim/rendering.py`, which is `27`'s), including `systems/characters/sim/beliefs.py`
(orphaned by design since `Person.beliefs` was deleted). Each with an exact `FORK:` row. **FALSIFIER:**
`grep -rn` for each deleted module's dotted path returns only fork-ledger rows. **Hash:** none.

**Batch 1 close:** agonist/antagonist → `/code-review` → `/simplify` → `layer-conformance` (Lens A on
the `FORK:` rows and registry edits; Lens B as `28-iii` names) → terminal Opus critique → `/close` (full
suite once: `tests/valoria -n auto`, `engine/tests`, `engine/season/tests`; `tools/valoria_local.py
--staged`). **Forward sweep check 4** must re-cite `requirements.yaml`'s scale notes that name
`mc_v18`, `systems/factions` and `game_state` (R-04 reason 2, the `scales:` `subsystem:` fields).
