# Valoria — Master Workplan v8, part 6: standing content carried from the retired plans · held back · history

## Status: PROPOSED 2026-10-01 — directed by Jordan; adoption on merge (ED-1094). Same status and held-back list as `valoria_master_workplan_v8.md`; §K below is that list.
## Reads after `workplans/valoria_master_workplan_v8_part5.md`. §C–§N are standing content the order relies on; §H is history and instructs nothing.
## Grade under `CLAUDE.md` §0.2: `paper`. Retired files are readable at `git show 0671283:workplans/<file>`; a pointer to one here is history, never an owner.

---

## C. THE NINE CONTRADICTIONS (2026-09-28 plan §4) — each resolved to one side; none went to Jordan

| # | subject | resolved to | ladder step | where it now lives |
|---|---|---|---|---|
| 1 | `Office.upkeep` | kept off `18a`'s list; its reader built at `17b` (Layer 1 `Seat :=` includes `upkeep`; r2 `05`: *"Deleting `Office.upkeep` removes the carrier, not the gap"*) | 3 | DONE (§H.1, `17b`) |
| 2 | C1–C4 "derive, no code change" | narrowed: the decision-layer H6 lands the content; the cells are Jordan's | 1 | `_part5` B4, J-1 |
| 3 | the M-7 obstacle remedy | the obstacle **CEILING**, value injected and swept, attacked at `22` — never a pool floor | 5 (ratified by `ED-IN-0270`) | `_part4` §`22` step 14 |
| 4 | the `kill / wound` rename | renamed standalone to `fight` (DONE); the SPLIT rides the cells commit | 1 + 3 | `_part5` B4 |
| 5 | `HANDOFF_IN.md`'s M4 row | a stale fact; `ecacb57` seeded garrisons and ran all four reviews | — | closed |
| 6 | the count of contested verbs | a stale fact; 3 contested verbs (`fight`, `march`, `tell`) | — | closed |
| 7 | proceedings step numbering | `21_RECONCILIATION.md` PHASE 1's numbering | — | closed |
| 8 | `ED-IN-0251` row 2's field against its text | a new `ED-IN-0261` row carrying `needs_jordan: true` | 5 | J-1 |
| 9 | `queries/` — three modules or four | `04 §A.2` edited at `20-ii` to name `faction_q` | 3 | DONE (`20-ii`) |

---

## D. STEP-B DISPOSITIONS — every spine file, role, retire-set tree and importer, and what replaced it

Carried from the 2026-09-28 plan's `_part2` §1, refreshed 2026-10-01 (S-9: 25 roles when written). Keys: **(a)** a
season-native replacement exists, named · **(b)** a replacement must be built, positioned · **(c)** dead
or orphaned, deleted with a `FORK:` row. **A row marked DONE was deleted at Batch 1 (PR #450)**: it stays
only because its (a)/(b)/(c) is the reason it went, and the `FORK:` row in `references/restructure_ledger.md`
is the record; a row not marked DONE is still on disk.

**D.1 The engine spine.**

| file | disposition | position |
|---|---|---|
| `engine/mc_v18.py` | **(a)** `loop/driver.py::SeasonDriver.season`. Jordan's 2026-09-13 *"just deprecate it and archive it"* is satisfied by deletion with a `FORK:` row — the fork ledger IS the archive (`CLAUDE.md` §1 allows no `deprecated/` tree). OI-05/OI-07 die with it | `28-iii` — DONE |
| `engine/autoload/game_state.py` | the hub, taken apart: `Faction`'s stat vector **(c)** — no season replacement by architecture (`04`: never *"a field of its own"*; a seat *"adds no verb and no modifier"*; Layer 1 PART D forbids porting it as-is); `faction_q.resolve` **(a)** for `(proposition, members, holdings, seats)`; `Territory` **(a)** `Rung` + `hold` + Sites; `World` **(a)** `state/world.py`; `create_world` **(a)** `populated.build_realm`; `serialize_world`/`restore_world` **(c)** (the season's identity is `content_hash`) | DONE: `serialize/restore` at `28-iii`, the rest `29b` |
| `engine/autoload/engine_clock.py` | **(a)** `loop/driver.py` (seven steps, four barriers, `04 §C.1`) | `28-iii` — DONE |
| `engine/autoload/season_manager.py` | **(a)** `loop/calendar.py` + `Date` | `28-iii` — DONE |
| `engine/autoload/scene_slate.py` | **(a)** `loop/deliberate.py` + `pack_scenes` + `Scene` | `28-iii` — DONE |
| `engine/autoload/victory.py` | **(c)**; the GD-1 requirement survives as an `ABSENT_RULE` hole | `28-iii` — DONE |
| `engine/autoload/npc_ai.py` | **(c)**; season counterpart `engine/season/decision/` (it is NOT zero-caller: `test_pipeline_reach.py`'s string probe names it) | `28-iii` — DONE |
| `engine/cross_scale/scene_dispatch.py` | **(a)** `seam/contest.py` + `manifest/` + the prize rows | `28-iii` — DONE |
| `engine/cross_scale/combat_bridge.py` | **(a)** `seam/wrappers/combat.py` → `substrate/pc_engine.py` | `28-iii` — DONE |
| `engine/cross_scale/handoff_rules.py` | **(c)**; the eight `scale_transitions_v30.md §3` handoff rules are R-04's content (*"the loop implements none of them"*) | `28-iii` — DONE |
| `engine/cross_scale/zoom_in_out.py` | **(c)**; the Hybrid-mode zoom is R-03/R-04's content; ENCOUNTER is the first in-season zoom | `28-iii` — DONE |
| `systems/overview/sim/season.py` | **(a)** `loop/driver.py`; goes with its `season_driver` row | `28-iii` — DONE |
| `systems/overview/sim/{accounting,ip_track,rs_track}.py` | **(c)**; MATTER + CENSUS replace accounting's work; the clocks have no season analogue by architecture | `29a` — DONE |
| `systems/overview/sim/ci_track.py` | **(c)**; same; `excommunication.py:166` imports it lazily, so it leaves with that file | `29b` — DONE |
| `systems/overview/sim/ms_track.py` | **(c)**, after `27` frees threadwork of it | `29a`-ms — DONE |

**D.2 The 25 composition roles** (`references/module_contracts.yaml`; one survives).

| role(s) | disposition | position |
|---|---|---|
| `mass_battle.resolve_field` | **the one survivor (a)** — consumed by `seam/wrappers/mass_battle.py` | — |
| `season_driver`, `faction_action`, `accounting` | **(a)** the driver + `march`/`via`-seat acts; MATTER/CENSUS | rows `28-iii` — DONE |
| `scene_builder.contest`, `scene_resolver.contest`, `contest_side.a/.b` | rows **(c)**; the kernel's resolution line is **(a)** `sigma.py`; the veto is **(b)**, relocated at `2-ii` | rows `28-iii` — DONE; kernel `2-ii` |
| `snapshot_state.*` ×10 | **(c)** with `restore_world` (its only caller is a test); the threadwork modules stay (`27`); `knots` until `29f`; `beliefs` orphaned by design | `28-iii` — DONE |
| `world_gen_settlements` | **(a)** `build_realm` | `29b` — DONE |
| `parliamentary_vote/motion/vote_declaration` | **(c)**; their caller `parliamentary_transfer.py` is production-orphaned; faction acts are person acts `via` seats (G3); their verb content is `levy`/`open_case`/`determine`/`issue` + `march` | `29b` — DONE |
| `rs_track_delta`, `territory_transfer_candidate/proposal` | **(c)**; "kept named" had no reader (`ID-13`) — record the ruling's expiry | `28-iii` — DONE |

**D.3 Retire-set trees** (each goes only when the loop expresses its scale — `requirements.yaml`'s gate).

| tree | scale | season expression | notes | position |
|---|---|---|---|---|
| `systems/factions/sim/` | grand strategy politics | `20-ii` ✓ | `resolve_mass_battle`/`_faction_to_unit`/`_morale_start_from_stability` die with `game_state.Faction`; d.1 moves to `resolve_field` at `20-iv` | `29b` — DONE |
| `systems/settlements/sim/` | settlement management | `24e` ✓ + `24d-ii` ✓ | `registry` → `build_realm` (which reads `territory` and `type` only: `settlements.*.stats` and `.controller`, the latter a copy of the province's `faction`, have had no reader since `29c`); `infrastructure` → `Site.condition`/`fortification_of`; `temperaments` → stance; `adjacency` **(c)** — no province graph, invent none; **the geography YAML stays** | `29c` — DONE |
| `systems/world/sim/` | grand strategy / settlement | `20-ii` ✓ | `npe` → `decision/` + stance; `insurgency_pipeline` → `24h` P5 | `29d` — DONE |
| `systems/characters/sim/` | character creation/development | the cells commit + `12` (+ `14` for `conviction` ← `knots`) | `beliefs` **(c)** by design; `conviction` → `Person.pursuits` / scar counts | `29e` — DONE (Batch 3a), ahead of its season expression (cells commit and `12` not landed; no caller after `29f`; the Scar-count rebuild stays `12`'s) |
| `systems/fieldwork/sim/knots.py` | investigations | `14` (`tie / knot`) + `27` | the `knot` Tenure kind and `firsthand_via_knot` exist; ED-912's gauge recorded in `H-182`, its `Tenure.degree` mapping UNLOCATED | `29f` — DONE (Batch 3a), ahead of `14`'s declined `tie / knot` |
| `systems/threadwork/sim/` | — | RETAINED (`ED-WR-0010`) | not in Step B; only its snapshot roles delete | — |
| `systems/social_contest/sim/` | social contests | `22` | the whole tree goes by `2-ii`; prize rows keep the logical name | `2-ii` |
| `systems/mass_battle/`, `systems/combat/` | retained | — | untouched except `massbattle.py`'s old entry | — |

**D.4 Test and tool importers** (a row not marked DONE is still on disk).

| file | disposition | position |
|---|---|---|
| `engine/tests/{test_mc_v18_regression,test_f7_smoke_oracle,test_combat_bridge_seam,test_pipeline_reach,test_world_population}.py`, `tests/valoria/test_engine_clock_phases.py` | `FORK:` (successors ran at `28-ii`; `test_combat_bridge_seam` needs none) | `28-iii` — DONE |
| `engine/tests/test_accounting_accord_drift_probe.py` | `FORK:` | `29a` — DONE |
| `engine/tests/test_parliamentary_action.py`; `tests/valoria/test_{faction_write_sweep,faction_stat_bounds,mass_seizure_accord_write,faction_obstacle_conventions}.py` | `FORK:`; `ED-FA-0038`, `ED-IN-0029`'s floors close (step 2) | `29b` — DONE |
| `tests/valoria/test_descriptors_runtime.py`, `test_world_initial_state.py` | lose one test each | `29b` — DONE |
| `tests/valoria/test_mass_battle_d1_morale_baseline.py` | **re-pin** against `resolve_field` | `20-iv` — DONE |
| `tests/valoria/test_settlement_temperament_drift.py` | `FORK:` | `29c` — DONE |
| `tests/valoria/test_conviction_roster_single_owner.py` | re-point | `29d` — DONE (`systems.world` site); `29e` — DONE (`systems.characters` site) |
| `engine/tests/test_knots_ed912.py` | `FORK:` | `29f` — DONE |
| `engine/tests/test_contest_kernel.py` | `FORK:` | `2-ii` |
| `engine/tests/test_thread_mending_ed871.py` | stays (`27`) | — |
| `engine/tests/test_sigma_leverage_parity.py` | substrate — stays; moves out of `engine/tests` when `sim-regression` folds | `2-ii` |

---

## L. LAYER-1 NODES STILL LIVE (2026-09-28 plan `_part2` §2; the rest are closed)

| node | verdict | destination |
|---|---|---|
| invariant 4, the per-conjunct half | built at `19` (S-8) | `23` checks what remains flat |
| F.20b — three body-literal Event kinds (invariant 7): *"the loop as built cannot run under the loader as specified"* | survives | `23` |
| invariant 2 — producerless matrix rows | step 3: each row is some position's content | enforceable at `23` once producers exist |
| MOD 1 — three routes into `systems/` | closes by sequence: `28-iii` landed (one composition role remains, `mass_battle.resolve_field`); after `2-ii` there are exactly two routes (the combat PATH seam; that one role) | Lens B at `2-ii` |
| MOD 4 — `npe`/`conviction` read `CONVICTIONS` | `29d` landed (`npe`); closes at `29e` (`conviction`); shrinks the cells commit's audit | `29d` (`npe`) and `29e` (`conviction`) landed: closed |
| H-137 — the `write()` calling convention | step 4: CONVENTION grade, enforced by `/code-review` on each effect | every effect in Batches 2–4 |

## S. WHERE `/layer-conformance` HAS NEW SUBJECT MATTER — its output must be READ, not passed

| position | Lens B's subject |
|---|---|
| `29a`-ms, `29e`, `29f` — DONE (Batch 3a) | `ID-13`'s consequences: the deleted module's last importers and the re-pointed fixtures. **Lens A:** the `FORK:` rows and registry edits |
| `10` | carved out (main §0.6); the telling workplan names its own Lens A/B subjects (A on T3a, B on T2) |
| `14` | the counterparty check in the fold; invariant 4 per conjunct |
| `22` | the provider returns a Margin, never a winner; the obstacle has one owner |
| `23` | the invariants |
| `2-ii` | the veto relocation only |

## G. THE 2026-09-18 PLAN'S §6 GAPS — what each is now

| gap | now |
|---|---|
| PART E step 12 (a parallel DELIBERATE map) and D-41a's permutation falsifier | unchanged — beside the critical path; no R-row moves on them |
| the FA lane | `20-ii` expressed the scale; `29b` retired `systems/factions/sim/` (PR #450) |
| proceedings PHASE 1/3/4 | PHASE 1 done (`16`, `15d`); PHASE 3 → `22a`; PHASE 4 → `22b` |
| any GDScript grade | unchanged — nothing targets GDScript before `26` |
| the 143-case count has no single owner | unchanged — positions use the harness loader's count (`len(wd_acceptance.CASES)` for `11`) |
| `2026-08-15-character-and-faction-stats-and-progression.md`, ownership unresolved | unchanged; its live question is D2 (J-9) |
| the birth-side consumer of `capacity` | unchanged — no position builds one |
| D1-b #1, the chronicle render | unpositioned; the `chronicle` channel dies at `22` step 13 — a candidate M2 gate (main file §1) |

---

## E. THE END-STATE — true when Batches 1 and 3 complete

Each bullet is marked **[LANDED]** (read against the tree 2026-10-01, Batch 1, PR #450) or left as the
target.

- **[LANDED]** `engine/mc_v18.py` is deleted with a `FORK:` row; `tests/valoria/test_mc_v18_is_deprecated.py` is
  deleted in the same commit after passing `ALLOWED_IMPORTERS == set()` as the intermediate state.
- **[LANDED]** `references/module_contracts.yaml` `composition_roles:` holds exactly ONE row,
  `mass_battle.resolve_field`. `composition.json` is regenerated behind `export_composition --check`. The
  `adapters:` block and its wiring rule are retired. The `engine_clock` contract row names the season
  driver and calendar (M3's note, main §1).
- **[LANDED]** `engine/autoload/` is `{__init__, dice_engine, sigma_leverage}` — the substrate. `engine/cross_scale/`
  is gone. `engine/substrate/` keeps `canon_buckets`, `world_initial_state`, `pc_engine`, `composition`,
  `descriptors` (minus the faction-stat roster), `stubwire`, `names` — ⚠ `canon_buckets` and
  `world_initial_state` now have no production importer (`29d-ii`).
- `systems/{overview, factions, world, characters, fieldwork}/` are gone with `FORK:` rows;
  `systems/settlements/` is reduced to `valoria_geography_v30.yaml`, its svg and a package marker; `systems/social_contest/` is gone and
  its prize rows point at the proceedings provider; `systems/threadwork/`, `systems/mass_battle/`,
  `systems/combat/` are retained (`massbattle.py`'s old entry deleted; d.1 on `resolve_field`).
  **Partly landed:** `systems/factions/sim/`, `systems/world/sim/`, `systems/settlements/sim/`,
  `systems/overview/`, `systems/characters/`, `systems/fieldwork/` and `massbattle.py`'s old entry are
  gone; `social_contest` is `2-ii`'s.
- **[LANDED]** Zero production imports of any spine module (the `ast` walk returns the empty set);
  `test_engine_does_not_import_systems.py` green at `BASELINE_TOTAL = 0`,
  `PATH_SEAM_ALLOWED = {'substrate/pc_engine.py'}`, fixtures re-pointed.
- Zero mentions of `mc_v18` outside the fork ledger, `CLAUDE_RATIONALE.md` and `registers/archive/`.
  **Not yet:** `git grep -l mc_v18 -- ':!.audit' ':!.designs' ':!registers/archive' ':!references/restructure_ledger.md' ':!CLAUDE_RATIONALE.md'` lists 147 tracked files (2026-10-01).
- `engine/tests/` is reduced to `test_thread_mending_ed871.py` (+ `test_sigma_leverage_parity.py` until it
  moves); the `sim-regression` job is folded into `unit-tests`; the `engine/season/tests` job is unchanged.
- `requirements.yaml`'s retire-set notes are rewritten: Step B executed; every scale row reads `in_loop`
  with its position, or (grid combat, character creation) names J-11.
- **[LANDED]** The successor artifacts have RUN: the same-seed hash pin (`test_build_realm_determinism.py`), the
  two-arm comparison on the season harness (`harness/arms.py`; ran end to end at P-7, both arms
  identical), and a battle from a chooser-formed decision (`test_march.py`; the realm fights none — P-5
  found H-149's target-kind check refuses all 11 marches, and `20-iv` did not change it). ⚠ The campaign-scale
  balance instrument `CLAUDE.md` §7 names has **no live successor**; that gap stays open and stated.

---

## K. HELD BACK FROM RATIFICATION-ON-MERGE (`CLAUDE.md` §2, ED-1094)

A merge of this plan ratifies **its ORDER** (`_part3` O.1–O.3 and the batch specs) **and the record that
it is the one active plan for the lanes it names**. Explicitly NOT ratified:
1. **Every §J item is OPEN** (`_part5`). Nothing gated on one becomes buildable because this merged.
2. **The §A answers ratify only as which ladder step answers each question and which candidate gets
   attacked** — never as the answer, which is decided at its position with the code in front of it. An
   attack that lands sends the question back through the ladder, not to Jordan by default.
3. **Content placements an ORDER document makes, each revertible alone:** `14`'s "no new closer rows" (A-16); the new handles `11-fix`, `13d-iii`, `R05-THREAD`,
   `LADDER-MBPC`; the decision-layer H-item deliverables carried into `_part5` B4; position 2's veto
   relocation carried into `2-ii`. If a content owner or a critic disputes one, that position reverts and
   nothing else in the order moves.
4. **No `## Status:` line on an absorbed proposal moves here.** Whether
   `proposals/2026-09-26-decision-layer-execution-plan/PROPOSAL.md` (a queue by its own declaration) and
   `proposals/2026-09-27-mc-v18-retirement-plan/PROPOSAL.md` are retired under the one-active-plan rule
   was the adoption commit's decision: both RETIRED by PR #448 (`FORK:06712837` rows in `references/restructure_ledger.md`); their sibling
   `candidate_*.md` drafts stay.
5. **No ledger id is allocated by this plan.** The adoption record and any `next_free` bump are the
   adoption commit's.

## N. NOT VERIFIED IN WRITING THIS PLAN — carried honestly

- Pre-flight rows P-4 and P-6 (`_part3` §P); P-1…P-3, P-5, P-7 and P-8 were consumed in Batch 1.
- The MB/PC `needs_jordan` rows — not opened; `LADDER-MBPC` is the pass.
- Whether any WITNESS channel predicate filters refusal kinds (H-111) — one probe, at `11`'s close.
- `ED-916`'s full row — only its head was read (consistent with `28-0`).
- Fable's `[PLAN]`-class evidence for `11a`/`11b`/`13b`/`13e`/`13f`/`13d-ii`/`24d-i` and the 2026-09-30 SHAs
  — carried, not re-run.
- Line numbers: every one in this plan drifts; re-derive a site by its symbol.

---

## H. HISTORY — instructs nothing

### H.1 Finished positions (one line each; the commit is the record)

| position | what landed | evidence |
|---|---|---|
| `1` CLOSE-PASS | the fold-to-latest instrument | `ec1a9d0`; `tools/fold_ledger_to_latest.py` |
| `2-i` RET-SC stub | the stub was already gone; the one-hop falsifier planted | `test_engine_does_not_import_systems.py::test_the_one_hop_relative_import_resolution_can_observe_the_seam_it_exists_to_catch` |
| `3`–`7` G1a·G1b·G2·G3·G4 | act store/`Receipt`/gate; `Event.subject` deleted; one `Token`; `NotYours`/`Act.via`; `NoOpReceipt` | `ED-IN-0258/0275/0276/0277/0278`; `engine/season/tests/test_g1a…test_g4…` |
| `7a` COMMIT-EFFECT | `commit` has an effect (never executes in the realm — J-4) | `loop/effects_information.py`; PR #444 |
| `11a` REACH · `11b` CALENDAR-EMIT | rebased onto Phase 1; the calendar emits | PR #441 `77f7f6cd`; PR #444 |
| `13` W28-cast (narrowed) | `cast:` overlays (5 of 46 NPC) + the reader in `build_at`; one sourced `capability` | PR #439; `test_w28_cast_capability_is_authored_world_gen_not_a_zeroed_default` — remainder is `13`-rest + `17` |
| `13b`·`13e`·`13f`·`13d-i`(1–4)·`13d-ii` | H-71 both halves; one remit reading; `establish` effect; offices as data; purview (by `6`) | `ED-IN-0255/0267/0272/0271/0273/0277` |
| `13d-i` item 5 (narrowed) | `offices.yaml` + the `populated.py` overlay | PR #439 — remainder is `13d-iii` |
| `15`·`16`·`15c`·`15b`·`15d` | record-kind fold; `give`; content operands; lossy tell; `told_by` | `test_record_kind_fold.py`, `test_give.py`, `test_content_operands.py`, `test_told_by_channel.py`; PR #444 |
| `17a`·`17b` | obligees; term + upkeep | `test_obligees.py`, `test_term_upkeep.py` |
| `18` PROC-A (narrowed) | `judging_set`, `arrangements.yaml` (3 of 12), its loader | `test_arrangements.py`, `test_stress_proceedings_rehost.py`; PR #439 |
| `18a` | five field deletions | `test_field_deletions.py` |
| `★` APERTURE | `harness/aperture.py`; control acts equal, hash equal | `test_aperture.py` |
| `19` U7-remit | `levy`·`open_case`·`determine`·`issue` resolvable; per-conjunct refusals | `test_u7_remit.py` |
| `19c` + `24d-ii` | `migrate`; `capacity(w, rung)`; the `reside` edge | `test_migrate_capacity.py` |
| `19d` | demand · delivery | `test_demand_delivery.py`; `harness/scarce.py` |
| `20-i` | M0–M4: `faction_q.resolve`, the mass-battle provider, `march` + ENCOUNTER + garrisons | `ecacb57`; `ED-IN-0279` |
| `20-ii` | faction queries + the rescale (143 of 143 cases run) | `80903bf`, `eaf654c`, `006af44`, `33855cd3`; `test_faction_q.py`, `test_scale_of_rung.py` |
| `20-iii` | the information cluster (`survey`) | `test_information_cluster.py` |
| `21` items 1–2 (partial) | U10 bookkeeping, part | `03de9d47` — remainder `21`-rest |
| `22` steps 6–10 (partial) | at `18`/`19`; step 8 a citation | `a1282b02` — remainder steps 11–16 |
| `24d-i`·`24e`·`24f` | dwelling substrate; works + founding (`restore` executes in the realm); territorial subsistence + 37 cohorts | `ED-IN-0274`; `test_works_founding.py`; `test_territorial_subsistence.py`; `engine/season/cohorts.yaml` |
| `25` MB-GOLDEN + hand pass (narrowed) | golden re-record; `ED-MB-0075` option (2) | `HANDOFF_MB.md`; PR #439 |
| `28-0` (narrowed) | `domain_echo.py`, the fieldwork/investigation stubs | PR #439 — remainder landed as the `28-0` follow-up (below) |
| `28-i` M5 | `balance_oracle.py` → `harness/arms.py`; the execution-map cluster retired | PR #439 (`FORK:c9daad6` rows, corrected by the `B0-CI` re-point, PR #450) |
| `28-ii` M6 | the `build_realm` hash pin; a battle from a chooser-formed decision **in a test** (`test_march.py`) | `013a5b1b`, `7ba66fde`, `6090af6b`; `test_build_realm_determinism.py` |
| `FIGHT-RENAME` · `OPENERS-DERIVE` · `GATE-REMOVE-PERSON` | `kill / wound` → `fight`; openers derived by AST; `remove_person` gated | PR #439; `test_gate_remove_person_requires_an_open_write.py` |
| PC lane item | `partisan` deletion; Ob-from-defender; `ED-PC-0058` | PR #439; `HANDOFF_PC.md` |
| MB slate | A1–A8, C4, C2/C3, d.1 | `ED-MB-0068`..`0074` |
| H1, H2 | record hygiene; the deontology gate (inert at `refusal_axis=None`) | 2026-09-27; H-146 |
| EFFECTS-SPLIT · CITATION-FIX · NERS/FABLE PASS · REGISTER/PLAN FIXES | `loop/effects.py` → six domain modules + shared + aggregator | `309a17d9`, `a882cc32`, `30dc8c65` |
| `27` (partial) · `10` (attempted, reverted) | coherence elastic/plastic + P-25 term; `tell`→stance reverted, side findings landed | PR #442 `c6f42528` |
| soak prerequisites | `wd_collect.py` rebased onto the rounds loop; `harness/soak.py`; U6/U5 decoupled | PR #446 `85afbf53` |
| realm measurements | H-156 cross-cite; R-01/R-06/R-07 realm paragraphs | PR #447 `06712837` |
| `B0-CI` (part) | the seven red `tests/valoria` tests cleared: ledger `FORK:` refs re-pointed to commits that are ancestors of `main`, `sim_params.json` and `value_pointer_links.json` re-derived by their exporters, `tools/build_engine_atlas.py`'s stated inputs — remainder is `B0-CI-b` | PR #450: the CI step `pytest tests/valoria -n auto` passes; ⚠ the next step, `pytest engine/season/tests`, fails the one test `B0-CI-b` owns |
| `28-iii` SPINE-DELETE | `engine/mc_v18.py` and its ratchet test, five `engine/autoload` spine modules, `engine/cross_scale/`, `systems/overview/sim/season.py`, five `engine/tests` campaign files, 20 of 25 composition roles and the `adapters:` block; GD-1 registered as hole `H-176`. **Cost: the last campaign-scale regression oracle (34 tests) is gone** | PR #450; an `ast` walk found 18 imports of the deleted modules in 10 files before and 0 after; `build_realm(0)`'s one-season `World.content_hash` `a66820c30fccf63ab78dff03a687fc2e` unchanged |
| `29a` (narrowed) | `systems/overview/sim/{accounting,ip_track,rs_track}.py` and `engine/tests/test_accounting_accord_drift_probe.py`; `ci_track.py` moved to `29b` (`systems/factions/sim/excommunication.py:166` imported it lazily and no test ran that path); `ms_track.py` stays until `29a`-ms (`27` has since landed) | PR #450; the only code importers of `systems.overview` left are `ms_track`'s two, in `systems/threadwork/sim/{co_movement,opposing}.py` — remainder is `29a`-ms |
| `29b` | `systems/factions/sim/`, `ci_track.py`, `parliamentary_{vote,stay}.py`, `engine/autoload/game_state.py`, the descriptor faction block (and six `fac.*` names rows), `massbattle.py`'s three strategic functions, `harness/arms.py`'s retired arms; the five test files the plan named to `FORK:` (it undercounted the tests inside the two it said lose one each: six from `test_descriptors_runtime.py`, three from `test_world_initial_state.py`); the `test_tn7_always` floor re-pinned 8 → 4 | PR #450; `ast` importers of `game_state`: 16 in 14 files before, 1 after (`test_mass_battle_d1_morale_baseline.py`, red at collection until `20-iv` re-pinned it) |
| `20-iv` | season-path morale source (`massbattle._morale_start`: 5 + a side's weight-mean stance toward its own faction, clamp 1..7) and A.9's Walls (+3 on the defender's `dr`) on the battle path, `fortification_of` read at `seam/wrappers/mass_battle.py`; the plan's commit-Tenure-`degree` candidate was attacked and dropped (nothing writes it: 0 of 86 commit Tenures carry one, H-162); `ED-MB-0078` registered `needs_jordan` (loyalty rows as a second morale source; every army starts at 5 until it loses a field); H-150 graded `assumption` (the +3 is applied 1:1 to `Unit.dr`; no instrument checks the unit). **The realm still fights no field** (P-5: all 11 realm marches are refused at ENCOUNTER by H-149's target-kind check) | PR #450; falsifier `engine/season/tests/test_mass_battle_provider.py::test_a_garrisoned_defender_resolves_differently_from_an_ungarrisoned_one` (a constructed test); `test_mass_battle_d1_morale_baseline.py` re-pinned against `resolve_field` |
| `29d` | `systems/world/` (six files); the plan's premise verified first (no season-side reader of `npe.py`) | PR #450; `import systems.world.sim` raises, `import systems.world` still works (a tracked `.jsx` keeps the directory a namespace package) |
| `29c` | `systems/settlements/sim/*.py` (seven) and `tests/valoria/test_settlement_temperament_drift.py`; the geography YAML stays; `adjacency.py` has no successor (no province graph invented) | PR #450; `terrain_row_for_territory` answers byte-identically over the 17 real province ids |
| `28-0` follow-up | `systems/characters/sim/{companion,beliefs}.py`, the last two members of the old `_OI17_FULL_MODULE_ENTRYPOINTS` roster that the deletions had not already emptied (`restructure_ledger.md`'s rows for them say so); `rendering.py` is `27`'s, `conviction.py` is `29e`'s | PR #450 |
| Batch 1 close | `methodology-close` run once on sub-batch 1a's range (five agonists, one antagonist, `/code-review`, `/simplify`, `layer-conformance`, one terminal critique) and, on 1b, a reduced form: two agonists and `/code-review` (the antagonist, `/simplify` and Lens B were not run — 1b changes no Layer-2 code and its survivors are prose and one test line), then one terminal critique; one full-suite run on each sub-batch's head | PR #450: at 1b's head `tests/valoria` 0 failed, `engine/season/tests` the one known failure (`B0-CI-b`) and nothing else, `engine/tests` 0 failed |
| `B0-CI-b` | the `office:` blocks of `engine/season/cases/exercises/NPC-034.yaml` and `NPC-070.yaml` seat their offices with the faction their holders commit to; `test_the_populated_world_has_a_governance_ladder_and_scarce_seats` passes unrelaxed | PR #451 `77f5175a`; `build_realm(0)` hash moved `babee6a4…` → `a6a426d6…` and the one-season populated run `496cb9bd…` → `5a898341…` (659 acts both), declared; `register`, `corpus_run` and `aperture 4 0` read unchanged against a `fd321c81` baseline (aperture differs only in the print order of two equal-valued lines). ⚠ Recorded, not decided: NPC-070's marches now muster Löwenritter (`loop/sides.py:78`); the Crown holds no military-command seat in the realm; the test now forbids any seat whose holder is not committed to its faction, which `world_q.leaders` allows |
| `20-v` | `field_walls_dr` Fixtures value (default `None` = A.9's number, read from `terrain.WALLS_DEFENDER_DR`, authored once) through `seam/wrappers/mass_battle.py` → `resolve_field(walls_dr=)` → `_run_and_grade`; H-150 `sweep: [3, 0, 1]`, `register --check` R2 16 → 15 | PR #451 `e538455a`, `b43d7230`; hash unchanged at the default; `runs/ASSUMPTIONS.md` gained one row. ⚠ The hash control is blind to this edit (the realm fights no field, H-149), so the 16-seed provider test is its only observer; no `arms.py` arm sweeps the knob, and one run through the realm would be a fake control |
| `29d-ii` | `engine/substrate/{world_initial_state,canon_buckets}.py`, `references/world_initial_state.yaml`, `tools/export_world_initial_state.py` and its CI / `valoria_local` / registry entries, `engine/engine_params/world_initial_state.json`, `tests/valoria/test_world_initial_state.py`: six exact-file `FORK:fd321c81` rows; `game_constants.json` re-derived (its `accord_range` prose named `canon_buckets`); ED-IN-0147's H2 closed | PR #451 `e214d267`, `02215b21`; hash unchanged; an `ast` walk found the module's own test as its only importer, none after; code search of `jordanelias/valoria-game` finds no reader of `world_initial_state` [medium confidence: default branch only]; that repo's generated `game_constants.json` keeps the old sentence until it re-syncs |
| Batch A close | `methodology-close` run once on `49f0e28f..`: three agonists in place of five (`B0-CI-b` has no logic and Phase 2 owns placement), one antagonist, `/code-review`, `/simplify` (read directly: about fifty lines of logic), `layer-conformance` Lens B (module-boundary conformant; `04` has no `Fixtures` row), one terminal critique; full suites once: `tests/valoria` 1766 passed · 23 skipped · 14 xfailed, `engine/season/tests` 723 passed, `engine/tests` 913 passed. Caught what the producers' narrow runs missed: the stale `runs/ASSUMPTIONS.md` row, five shifted cites, one stale open ED row. ⚠ The terminal critic read `agonists.txt`, which its brief withheld | PR #451 `39e2c1de` |
| `LADDER-MBPC` | the MB/PC lanes' flagged rows through the five-step ladder: `ED-MB-0039` closed (superseded); `ED-MB-0041` closed on four legs, two survive (J-18, J-19); `ED-MB-0045`, `ED-PC-0016`, `0049`, `0050` decided with the builds owed (status `open`); `ED-PC-0047`, `0052`–`0054` closed; `ED-PC-0051` survives (J-21), `ED-PC-0055` survives (J-20); rows appended to the lane `_archive` ledgers (the split guard forbids placing them live) | the Sonnet producer's measurements (gauge runs, Lanchester signature, a 200-duel scratch engine) were not re-run; an independent Opus check re-opened every cite and OVERTURNED `ED-PC-0051`'s closure and J-19's premise, SOFTENED `ED-MB-0039`, `0041`, `0045` and J-18, upheld the rest; the revision applied each; ED-PC-0019/0021, ED-MB-0040/0043 and about a dozen more MB/PC rows still fold to `needs_jordan: true` outside the named roster |
| `11-fix` | `wd_acceptance.py`/`wd_collect.py`/`wd_chunk.py` repaired: the plant closure forwards to the real function, the forensics spy and comparator plant are controls that fire (`fires`, `detected_all_genuine`), a slice-bounds assertion; the 36 cells and `wd_acceptance.json` untracked and gitignored (`WD_LOG.txt` stays tracked) | PR #451 `c2ee345a`, `53cf0ddb`; the instrument now prints a conditional PLANT INERT / FORENSICS / COMPARATOR warning rather than a verdict it cannot support; `WD_LOG.txt`'s CONTEST line corrected (`A9._run` passes the fixture's own `contest_max_depth`) |
| `11` (first measurement and re-take) | reconvergence at `2x3` over 143 cases: none 77.13 % · actor 43.03 % · total 38.47 % (at `2x1`: 88.39 % · 69.41 % · 69.51 %), below the 96 % bar; R-02 set `met`, R-01 stays `not_met` | PR #451 `b53f9b81`; `register --requirements` met 1 → 2; R-02's `met` attacked by an Opus reader, a Sonnet agonist and a terminal critic and held; RE-TAKE 2026-10-02 on `8b03e518` across `14`, `13d-iii` and `17-cast`: 77.22 % · 42.59 % · 38.58 % at `2x3` (no arm moved half a point), `corpus_run` DISTINCT EXECUTED SETS 117 → 120 and verbs executed 16 → 17 of 44 (`give`); one cell wrote nothing on its first run and was re-run; the instrument's run-to-run noise is not measured |
| `8` | the wound-count band edge is data: `rosters.yaml` `wound_quantities` and `combat_band_edges`, read by `seam/ladder.py::combat_degree` (`wounded_above`) and `degree_of(…, fixtures=)`; `Fixtures.combat_wounded_above` (`None` = the roster's edge, any wound) now has its own `assumption` row, `H-184`, split out of `H-98` on the Batch B critique (04 §B.13 #11) | PR #451 `e88f57b0`; falsifiers `engine/season/tests/test_combat_band_edges.py` (192-state grid and 24 real fights against the old literal; mutation at `above: 1` reddens 5); `build_realm(0)` hash and the one-season run unchanged, a NULL (nothing there is shown to resolve a `fight`) |
| `27` | `rendering.py`'s two stubs struck with their reasons at the site; `ED-WR-0003` closed at ladder step 2 (superseding row in the WR `_archive` ledger); `attempt_mending` calls `recover()` and costs > 0 (`environment_in_equilibrium` defaults to False, so only tests exercise it); threadwork no longer imports `ms_track` or `knots` | PR #451 `ff40b960`; unblocks `29a`-ms and `29f`; three things left to the WR lane (`HANDOFF_WR.md`): the `R-14` term, own-configuration Mending, `collective.py`/`opposing.py` feedback. `tests/valoria/test_flow_skeletons.py` gained `RETIREMENT_SHIFTED` entries for the four re-numbered files and `RETIRED_CALL_SITES` for the three struck calls |
| `ED-FI-0009` | STOP CONDITION HIT, nothing built: the six inquiries resolve Failure/none only; step 3 already closed "graded by degree" (2026-09-06), and what is open (how a degree routes without `contests:`, and whether a refused inquiry's `finding.none` deposits) rests on invariant 12's `emits` arm, a loader check `ED-FI-0009`'s own commit added and not ratified Layer 1 text (`verbs.py:589-604`; `04` §B.13 #12); `rosters.yaml:1031-1034` rules against making investigation a contest to become gradeable | PR #451 `64c20462`, `114229b2`; superseding row in `editorial_ledger_fi.jsonl` (`needs_jordan: true`), J-22 |
| `14` | `loop/resolve.py` `_admits` gains one counterparty clause (a missing or self counterparty refuses with the row's own refusal kind; loader invariant 4 via `data/verbs.py` `COUNTERPARTY_CLAUSE`); `give` typed and formable through T4's `operand_bags`/`known_persons`; `Candidate.why` removed with its one writer. DECLINED or STOPPED, each with a `decline_note` on its verb row: `repudiate`, `succeed`, `tie / knot` (`29f`'s), `forge`, `exchange`, `carry`, `thread_read` (`R05-THREAD`, ladder step 4: Thread Sensitivity ≥ 30 has no carrier), the `H-165` works channel (left with J-4); `oblige` stays unformable; `destroy_record` built, measured and HELD (formable and executing in 3 corpus worlds, but crowds `release` out of 2; its second reason, the `15d` control, no longer applies at HEAD; the variant is not kept) | PR #451 `0a20384f`; always-refused set 8 → 8 asserted; mutation (fold clause off) reddens 4 tests; `build_realm(0)` hash unchanged; one-season populated `5a898341` → `9736318a` (659 → 662 acts, `give`'s); `H-84`, `H-85`, `H-156`, `H-165`, `H-169`, `H-182` amended; R-05's measured paragraph is refreshed at the Batch C close |
| `13d-iii` | `populated.resolve_anchor` — one resolver over `{<rung kind>: <key>}` filled by `build_realm`'s four mint sites; every office row's rung is `Office.rung` and `scope_rung`; `remit_acts` replaces the testing default (`rosters.authored_remit`); six `[NEW]` seats minted; `obligees` become `oblige` Tenures; 29 of 30 offices carry a rung (`off_npc_084` has no row); `H-163` limit 1 lifted | PR #451 `294a152d`; aperture `4 0`: `levy.unauthorized` 18 of 19 → 4 of 23, `issue` executed 0 of 13 → 6 of 30 with `Act.via` set; `transfer` carrying `via` stays 0 of 127 (`H-158`, registered, not fixed); `build_realm(0)` hash `a6a426d6` → `a918cd1f`, one-season populated `9736318a` → `05f022e2`; `J-8` (dispatch's remit) untouched: `offices.yaml: meta: remit_unruled: [dispatch]` |
| `17` + `17-cast` | `queries/world_q.py::ambitions(w, p)` (a read over p's live `commit` edges to OUGHT Propositions; built at `17` as `person_q.ambitions(p, propositions)` and MOVED at the Batch C close because 04 §A.2 :164 gives `person_q` 'a `PersonInterior` snapshot only' and §B.2 :241 'no store handle'; creeds are OUGHT commits and are returned); `world_q` Q4 asks `ambitions`; `corpus_run.build_at` seats from `cast:` through `seating`; `17-cast`: `_check_cast` closes the entry key set, `office:` routes through `_check_office`, `ought: {about, predicate}` seats a commit edge to an OUGHT Proposition; `knows:` refuses at load (no world builder constructs a `Claim`; seeding a belief needs a sixth construction site or pre-history Events through the existing witness sites, `01_AXIOMS.md` AX-7, neither built and nothing in the plan's observables needs it) | PR #451 `5519cf52`, `f429ab2e`; PILOT of eight NPC overlays (NPC-002/011/035/038/072/075/083/086; no `capability`: no case names a vocation `verb_capability` covers): DISTINCT EXECUTED SETS 41 / 41 / 26 (none / pilot / uniform control), observable NOT met, not scaled; an ought's `predicate` is a declared non-causal label (`build_at`, 2026-09-13; `H-185`), and the metric's ceiling was +5 of 46 so the null is weak; `corpus_run` md5 `d714ba5c` → `6a65a264`, world hash moved for exactly the eight pilot cases; `dispatch` always-refused → never-attempted, stable across seven hash seeds; three `test_season_shape` pins re-recorded |
| Batch C close | `methodology-close` on `99a1cf8d..HEAD`: three Sonnet agonists (`14`, `13d-iii`, `17`+`17-cast`), an Opus antagonist over their reports, four fix lanes, `/code-review`, `/simplify` (one reviewer), `/layer-conformance` (one Opus reader, both lenses), one terminal Opus critique; full suites once on the integrated head `0d58757a`: `engine/season/tests` 831 passed, `tests/valoria` 1786 passed · 23 skipped · 14 xfailed, 0 failed (`engine/tests` not run: byte-identical to season changes by construction; the last commit `724c28c8` (capability validation and texts) came after that run and was covered by its own test files and the three hashes, not by a second full run); forward sweep: `register --requirements` met 2 · partial 5 · not_met 2, `corpus_run` md5 `6a65a264` (DISTINCT EXECUTED SETS 117 → 120, verbs executed 16 → 17 of 44, R3 46 of 46 and 96 of 97), `aperture 4 0` 2939 acts with control hash EQUAL, `report` then `delta 99a1cf8d` 0 probe flips (121 probes, 86 gaps) | PR #451 `23bea9da`, `7e7cb23a`, `03bb91ba`, `0d58757a`, `724c28c8`: found and fixed — the `succeed`/`tie / knot` stop rested on superseded holonic §15; `ambitions` took a store argument against 04 §A.2 :164 (moved to `world_q`); silent no-op loaders (cast `case:`, non-list `cast:`, duplicate case and office ids, `capability`); the told-by seed re-pin's cause (now measured: `13d-iii` lowered chained told claims in 3 of 10 seeds, raised 1, seed 5 identical); the pilot metric's ceiling (0, not +5). Not fixed, recorded: the minted seats' `dispatch` and bench-ground defaults differ by build route from the loop-built seats (`H-134`, `H-32`; any single rule is a J-8 grant or moves the realm); `knot`'s undirected read (`29f`); the loader forces a dead refusal key on `determine`; `give` is refused in about 98% of its attempts yet leaves the always-refused set on one execution |
| `21`-rest | R-01's opening R3 sentence, R-03's and R-09's `measured:` blocks (dated 2026-10-02 paragraphs from their own `measure:` commands), R-09's 'capability empty on every corpus person' (13 cases carry a cast, 30 entries, one `capability`: NPC-088's Carin Vedel `{copying: 3}`, 1 of 430 built persons) and `rosters.yaml: verb_capability`'s note, R-04's `measure:` (now `aperture 4 0`'s per-verb lines); item 3 closed at ladder step 2 | PR #451 `444a00e1`+: two figures re-run by the orchestrator (NPC-088 headless hash `293067ea`, the capability count); recorded, not fixed: R-09's `-k 'we_only_a_verb or u1_'` selects one test (`u1_` matches nothing), R-04's quoted always-refused count is now 7, retired-plan citations remain in R-05's older paragraphs, `corpus_run` still does not print which ARC case fails R3 |
| Batch B close | `methodology-close` on `269ab8c7..fcf357cb`: agonists, an Opus antagonist, `/code-review`, `/simplify`, `layer-conformance`, one terminal Opus critique at max effort; full suites once: `engine/season/tests` 747 passed, `engine/tests` 913 passed, `tests/valoria` 1781 passed and 5 failed (four flow-skeleton anchors into the shortened threadwork files, fixed here; `test_no_module_actually_loads_id_reservations`, which fails only while a second worktree nests under `.claude/worktrees/` and passes on a clean checkout); forward sweep: `register` R-02 `met`, `corpus_run` and `aperture 4 0` identical to the `fd321c81` baseline | PR #451 `a0a65cbc`, `fcf357cb`, then the close commit: critique reconciled (T1 `H-184`; T2/T3 this table and `HANDOFF_IN`; B1 J-22/`ED-FI-0009` cites; B2 the CONTEST text; B3, B4, B6, B7). Skipped with reasons: T4 (`rendering.py` keeps its docstring because it is the only site for the strike reasons, and `registers/mechanics_index.yaml` (`rendering_stability`'s `sim_module`) and `tests/valoria/test_flow_skeletons.py` (`RETIREMENT_SHIFTED`) both name the file; retiring it is delete plus a `FORK:` row plus those two edits, left to the WR lane), B5 (`PR #451` is the branch's PR, and `27` is on it) |
| `29f` | `systems/fieldwork/` (`knots.py`, two package markers) and `engine/tests/test_knots_ed912.py`; the ED-912 gauge recorded in `H-182`'s cite as the code defined it, its `Tenure.degree` mapping UNLOCATED (the only attestation was one clause of a retired plan saying `14` would record it); `KNOT_FORMATION_TN/OB` left `game_constants.json`; `test_tn7_always`'s floor re-pinned 4 → 3 | `21c7133f`; four exact `FORK:59004d86` rows; import lines naming `systems.fieldwork`/`systems.characters`/`systems.overview` in tracked `.py` before the batch: 5, in 3 files (the deleted module's own lazy import, its test ×3, the roster test ×1), 0 after; tracked `*.py` 574 → 565 over the batch; `build_realm(0)` hashes unchanged (blind by construction: nothing under `engine/season` imported the module; the import walk is the control) |
| `24h` P5 | `queries/world_q.py::uncontrolled(w, rung_id)`, GD-3's first condition (a territory no faction holds); one caller, `populated.census`'s realm-scoped `uncontrolled_in_realm` row (a report); the oracle's contiguity, two-season streak, promotion and emerged-faction conditions have no season carrier and are `H-186` | `b360c22f`; `engine/season/tests/test_revolt_query.py` 7 passed; `build_realm(0)` reports `terr_T15`; hashes unchanged; `register --check` R2 15, G6 13; DONE-test, not DONE-realm (§0.2) |
| `29e` | `systems/characters/` (`conviction.py`, two package markers); the roster-single-owner test lost its `systems.characters` site; the evacuation-plan control re-pointed at `engine/season/loop/driver.py`; deleted ahead of its season expression | `1b68d590`; three exact `FORK:59004d86` rows; 0 importers after (the roster test was the last); one coverage drop, named in the ledger comment; hashes unchanged, blind by construction |
| `29a`-ms | `systems/overview/` (`ms_track.py`, two package markers); `SEASONS_PER_YEAR` left `game_constants.json` (its only owner; the season loop defines no year) and the descriptor `nc.MS` lost its value links; three threadwork docstrings corrected | `72623b61`, `2a57549f`; three exact `FORK:59004d86` rows; 0 importers before and after; hashes unchanged |
| Batch 3a close | `methodology-close` on `866b3136..`. Phase 1: three Sonnet agonists (the deletions' accuracy and fidelity; the P5 Query's correctness and logic; guard integrity and the CI split) and one Opus antagonist, no blocking finding. Phase 2: `/code-review` (the census key renamed `uncontrolled_in_realm`), `/simplify` read directly (the `uncontrolled` docstring cut from 50 to 32 lines), `layer-conformance` Lens B (`world_q.uncontrolled` takes no token and no `ended()` call sits in its five-function callee chain; its one caller is `populated.census`, reached by `run`, `main` and `soak`; `04` names none of the three deleted modules in a §A.2 row or an invariant). Phase 3: one Opus critique at max effort, no blocking or major finding. Fixes applied: the writes-nothing arm snapshots state `content_hash` does not fold; the `module_contracts` wiring of three retired rows reset to the zero-code states; the `29f` pointers in `verb_table.yaml`, `H-85` and `H-182`; the claim that the season has no Mending Stability clock re-cited from the individuation rule to holonic §25.1 (*the three licensed clocks are exhaustive*); `H-182` gained the knot-pool caveat; plan and handoff state flipped. Lens A read: the FORK rows and registry edits are process surfaces that `pathres` and `test_forked_status` read; no prose is offered as a mechanism; the one new file is a per-property test of Layer-2 code; no new "Layer" scheme | `c92beba2`, `16a15261`, `60f0e1f2`, `2e72eaaf`, `b12f1e4a`. Full suites once on `60f0e1f2`: `tests/valoria` 1786 passed · 23 skipped · 14 xfailed; `engine/tests` 904 passed; `engine/season/tests` 845 passed and 1 failed. ⚠ THE FAILURE WAS A PRE-EXISTING RACE, FIXED IN `b12f1e4a`, NOT A DEFECT OF THE BATCH: `test_the_npc_roster_is_read_and_not_merely_shipped` rewrote the real `engine/season/npcs.yaml` and restored it in a `finally`, so a worker building a realm inside that window read a doctored roster (`test_15d_falsifier_…` read 5,080 claims against 5,110 in its first arm). Failed twice on one `-n 4` schedule, worker `gw3`; passed in every serial configuration tried (alone, eight fixed `PYTHONHASHSEED`s, four file groups, the 17-file chain, and `gw3`'s exact 301-test sequence with and without the new tests); the pre-batch tree and CI at two heads of the branch passed. The new tests only moved the schedule. After the fix `engine/season/tests` 846 passed under `-n 4`, with the same test again on `gw3`; with the redirect removed the roster test fails. CI on `60f0e1f2`: `All Gates Green`, `Season Loop Tests` 12m06s, `Validator Unit Tests` 8m46s. `build_realm(0)` hash `a918cd1f…` and its first season `05f022e2…` unchanged; `register --check` R2 15, G6 13. Not checkable here: `valoria-game`'s parity reader, which loses `KNOT_FORMATION_TN`, `KNOT_FORMATION_OB` and `SEASONS_PER_YEAR` (`HANDOFF_IN.md` carries it) |

### H.2 Spent serial edges (both ends finished)

From the 2026-09-18 plan §3.9: 1 (G1b → `11a`), 2 (`13f` → `13e`), 3 (`13d-i` → G3), 4 (`13e` → `17a`),
5 (`18` → `18a`), 6 (`15` → `24e`, `15/15c` → `7a` → `17a`; `15` → `19b` is satisfied), 7 (`24d-i` →
`24e`, `19c`), 8 (`24f` → `body_step` — satisfied; the pick is J-6), 9 (G4 → `_eff_work`), 11 (`18a` must
not delete `Tenure.payload`). From the 2026-09-28 plan §3.5: 5 (FIGHT-RENAME → `8`), 6 (GATE-REMOVE-PERSON
↔ `24f`), 7 (`20-ii` → `20-iv`, satisfied), 8 (`13d-i` item 5 → `18a`).
From this plan's `_part3` O.2, spent when Batch 1 landed (PR #450): E1 (`28-iii` → `29a` → `29b` → `29d` →
`29c`, import direction), E6 (`29b` → `20-iv`, `massbattle.py`'s old entry and the d.1 re-pin), E12
(`28-iii` → `28-0` follow-up, the OI-17 targets), and E4's `29b` → `2-ii` half (`22` → `2-ii` stays live).
Spent at Batch 3a: E2 (`27` → `29a`-ms, `27` → `29f`); E3 (`14` → `29f` → `29e`; `14` declined `tie / knot`, so E3's first clause was waived at v8 §3, not satisfied).

### H.3 Edits OUTSIDE this plan that its adoption needs — listed, NOT made here

1. `CURRENT.md` "The plan" row → this plan (pointer only; no counts). `tools/currency_consistency_check.py`.
2. `references/lane_assignments.yaml` `source:` → this plan (it names the retired v7).
3. An adoption ledger row (`registers/editorial_ledger_in.jsonl`) and the IN `next_free` bump in
   `references/id_reservations.yaml` — allocated at adoption, never max+1.
4. `engine/season/requirements.yaml`: `:93`'s scale note and R-02's `measure:` comment name retired plan
   files — re-point to this plan's positions; `register --requirements` must still exit 0. (The other
   `requirements.yaml` record edits are `21`-rest's.)
5. Handoff rows citing retired plans as owners: `HANDOFF_IN.md` (rows naming
   `workplans/2026-09-28-…` as the place a record lives — history pointers resolve through `FORK:0671283`
   and may stay; rows naming one as the ORDER must re-point), `HANDOFF_SE.md` (SE-CAPACITY and `found` read
   open — both DONE), `HANDOFF_SC.md` (M-7's disposition), `HANDOFF_MB.md`, `HANDOFF_WR.md` (`27`'s row
   cites "`the-plan...md` position 27"), `HANDOFF_IN.md`'s `test_n3` "Jordan's call" row (stale: A-1).
6. `proposals/2026-09-27-mc-v18-retirement-plan/PROPOSAL.md`'s header (HELD BACK, reason spent; "39
   production files", not reproducible) — or its retirement (§K item 4).
7. Comment-only re-points (`tools/ci_common.py`, `tools/fold_ledger_to_latest.py`,
   `references/ci_checks_registry.yaml`) — run `tests/valoria/test_tool_input_paths_resolve.py` after any
   tool docstring edit.
**Covering runs for that commit:** `python tools/currency_consistency_check.py`;
`python tools/valoria_local.py --staged`; `pytest tests/valoria/test_single_status_line.py
tests/valoria/test_currency_consistency_check.py tests/valoria/test_tool_input_paths_resolve.py
tests/valoria/test_ledger_hygiene.py tests/valoria/test_forked_status.py -q`;
`python -m engine.season.harness.register --requirements`.

### H.4 Where each retired plan's live content went (all at `FORK:0671283`)

| retired file | live content → where in v8 |
|---|---|
| `2026-09-28-the-plan-one-order-mc-v18-retired.md` | §0 numbering/legend → main §0.2–0.3; §2.3 state → main §3; §3.3/§3.4 → Batches 2–3 (Batch 1 landed: §H.1); §3.5 → `_part3` O.2; §3.6 → §S; §3.7 → §G; §4 → §C; §5.1 → `_part5` §J; §5.2 → `_part5` A-1; §6 → §E; §7 → §K; §8 records → §H.1; §9 → §N |
| `…_part2.md` | §1 → §D; §2 → §L; §3's live mappings → the batch specs (H-items, `24g`/`24h`, `22a`/`22b`; `20-iv` and `15d`/`17b` DONE) |
| `2026-09-30-phase-4-post-ners-revision.md` | §1.4 (eight always-refused) → `_part2` R-05; §1.5 (the retirement's cost) → `_part3` `## B1`; §2 → main §3; §3 (effect-file targets, `22`'s step-by-step state, `28-ii`'s evidence) → the batch specs; §4 → `_part5` J-4/J-16/J-17 |
| `2026-09-18-governance-settlement-behaviour-plan.md` + `_part2` | §3.0 cadence → main §0.4 (now its only home); §3.9 → `_part3` O.2/O.3; `_part2` §8 per-position text → the batch specs for `8`, `9`, `10`, `11`, `12`, `12b`–`12d`, `13`, `14`, `17`, `19b`, `21`, `22`, `23`, `24g`, `26`, `27`, `2-ii` |
| `2026-09-09-r-execution-plan.md` + `_part2` | U5 → the telling workplan (position `10` re-scoped there, main §0.6); U6's acceptance block → `11` (verbatim, slices re-derived); U7 → `14` (its group arithmetic superseded by `_part2` R-05's measured table); U8 → `17`; U10 → `21`-rest. U1–U4, U9: DONE |
| `2026-09-13-work-order.md` | units 13, 14, 19b → those positions; 13b, 15, 19, 20 DONE |
| `valoria_master_workplan_v7.md` | §0 owns-table → main §0.1; §1 M1/M2/M3 → main §1 with current readings; §3's who-can-answer sort → `_part5` §J's ranking; §4 lane sections → the lane handoffs (v7's text was stale on every lane); §5's binding rules → `CLAUDE.md` (pointer); ruling R-7 → A-14 |
| `2026-09-06-season-loop-execution-plan.md` | work item 4.5 (investigation: the loop is the mechanism) → `ED-FI-0009` |
| `2026-09-09-layer1-conformance-plan.md` + `_part2` | the live nodes → §L |
| `2026-09-05-…`, `2026-09-06-shape-…`, `2026-09-09-shape-…-v2`, `2026-09-10-unblocking-strategy`, `2026-09-11-arc-sequence-spine`, `README.md`, `return_to_game_queue.yaml`, `valoria_master_workplan_v6.md`, `workplan_v6_progress.yaml` | none live — spent, superseded, or retired by `ebb43bf0` (the progress board's last reader was m1 row 3, re-pointed to THE NINE) |

### H.5 v7's dated sections, one paragraph

v7 (ratified 2026-09-12, `ED-IN-0216`) replaced a July master that cited dissolved trees; its §2 narrated
the tree's state on 2026-09-12; its §3 queue (108 open, ~97 closable) was cleared by position `1`
(`ec1a9d0`, the fold-to-latest instrument); §6 recorded v6's deferred retirement and the ORDER collision,
both since closed (v6 retired at `ebb43bf0`; the collision by `ED-IN-0253`); §7–§8 amended it
(`ED-IN-0218`: `ED-IN-0210`'s two unexecuted rulings moved to work, its fork stays J-2). None of it
instructs anything now.
