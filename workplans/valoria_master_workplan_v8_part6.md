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

## D. STEP-B DISPOSITIONS — every spine file, role, retire-set tree and importer still on disk

Carried from the 2026-09-28 plan's `_part2` §1, refreshed 2026-10-01 (S-9: 25 roles). Keys: **(a)** a
season-native replacement exists, named · **(b)** a replacement must be built, positioned · **(c)** dead
or orphaned, deleted with a `FORK:` row.

**D.1 The engine spine.**

| file | disposition | position |
|---|---|---|
| `engine/mc_v18.py` | **(a)** `loop/driver.py::SeasonDriver.season`. Jordan's 2026-09-13 *"just deprecate it and archive it"* is satisfied by deletion with a `FORK:` row — the fork ledger IS the archive (`CLAUDE.md` §1 allows no `deprecated/` tree). OI-05/OI-07 die with it | `28-iii` |
| `engine/autoload/game_state.py` | the hub, taken apart: `Faction`'s stat vector **(c)** — no season replacement by architecture (`04`: never *"a field of its own"*; a seat *"adds no verb and no modifier"*; Layer 1 PART D forbids porting it as-is); `faction_q.resolve` **(a)** for `(proposition, members, holdings, seats)`; `Territory` **(a)** `Rung` + `hold` + Sites; `World` **(a)** `state/world.py`; `create_world` **(a)** `populated.build_realm`; `serialize_world`/`restore_world` **(c)** (the season's identity is `content_hash`) | `serialize/restore` at `28-iii`; the rest `29b` |
| `engine/autoload/engine_clock.py` | **(a)** `loop/driver.py` (seven steps, four barriers, `04 §C.1`) | `28-iii` |
| `engine/autoload/season_manager.py` | **(a)** `loop/calendar.py` + `Date` | `28-iii` |
| `engine/autoload/scene_slate.py` | **(a)** `loop/deliberate.py` + `pack_scenes` + `Scene` | `28-iii` |
| `engine/autoload/victory.py` | **(c)**; the GD-1 requirement survives as an `ABSENT_RULE` hole | `28-iii` |
| `engine/autoload/npc_ai.py` | **(c)**; season counterpart `engine/season/decision/` (it is NOT zero-caller: `test_pipeline_reach.py`'s string probe names it) | `28-iii` |
| `engine/cross_scale/scene_dispatch.py` | **(a)** `seam/contest.py` + `manifest/` + the prize rows | `28-iii` |
| `engine/cross_scale/combat_bridge.py` | **(a)** `seam/wrappers/combat.py` → `substrate/pc_engine.py` | `28-iii` |
| `engine/cross_scale/handoff_rules.py` | **(c)**; the eight `scale_transitions_v30.md §3` handoff rules are R-04's content (*"the loop implements none of them"*) | `28-iii` |
| `engine/cross_scale/zoom_in_out.py` | **(c)**; the Hybrid-mode zoom is R-03/R-04's content; ENCOUNTER is the first in-season zoom | `28-iii` |
| `systems/overview/sim/season.py` | **(a)** `loop/driver.py`; goes with its `season_driver` row | `28-iii` |
| `systems/overview/sim/{accounting,ci_track,ip_track,rs_track}.py` | **(c)**; MATTER + CENSUS replace accounting's work; the clocks have no season analogue by architecture | `29a` |
| `systems/overview/sim/ms_track.py` | **(c)**, after `27` frees threadwork of it | `29a`-ms |

**D.2 The 25 composition roles** (`references/module_contracts.yaml`).

| role(s) | disposition | position |
|---|---|---|
| `mass_battle.resolve_field` | **the one survivor (a)** — consumed by `seam/wrappers/mass_battle.py` | — |
| `season_driver`, `faction_action`, `accounting` | **(a)** the driver + `march`/`via`-seat acts; MATTER/CENSUS | rows `28-iii` |
| `scene_builder.contest`, `scene_resolver.contest`, `contest_side.a/.b` | rows **(c)**; the kernel's resolution line is **(a)** `sigma.py`; the veto is **(b)**, relocated at `2-ii` | rows `28-iii`; kernel `2-ii` |
| `snapshot_state.*` ×10 | **(c)** with `restore_world` (its only caller is a test); the threadwork modules stay (`27`); `knots` until `29f`; `beliefs` orphaned by design | `28-iii` |
| `world_gen_settlements` | **(a)** `build_realm` | `29b` |
| `parliamentary_vote/motion/vote_declaration` | **(c)**; their caller `parliamentary_transfer.py` is production-orphaned; faction acts are person acts `via` seats (G3); their verb content is `levy`/`open_case`/`determine`/`issue` + `march` | `29b` |
| `rs_track_delta`, `territory_transfer_candidate/proposal` | **(c)**; "kept named" had no reader (`ID-13`) — record the ruling's expiry | `28-iii` |

**D.3 Retire-set trees** (each goes only when the loop expresses its scale — `requirements.yaml`'s gate).

| tree | scale | season expression | notes | position |
|---|---|---|---|---|
| `systems/factions/sim/` | grand strategy politics | `20-ii` ✓ | `resolve_mass_battle`/`_faction_to_unit`/`_morale_start_from_stability` die with `game_state.Faction`; d.1 moves to `resolve_field` at `20-iv` | `29b` |
| `systems/settlements/sim/` | settlement management | `24e` ✓ + `24d-ii` ✓ | `registry` → `build_realm`; `infrastructure` → `Site.condition`/`fortification_of`; `temperaments` → stance; `adjacency` **(c)** — no province graph, invent none; **the geography YAML stays** | `29c` |
| `systems/world/sim/` | grand strategy / settlement | `20-ii` ✓ | `npe` → `decision/` + stance; `insurgency_pipeline` → `24h` P5 | `29d` |
| `systems/characters/sim/` | character creation/development | the cells commit + `12` (+ `14` for `conviction` ← `knots`) | `beliefs` **(c)** by design; `conviction` → `Person.pursuits` / scar counts | `29e` (`beliefs` at the `28-0` follow-up) |
| `systems/fieldwork/sim/knots.py` | investigations | `14` (`tie / knot`) + `27` | the `knot` Tenure kind and `firsthand_via_knot` exist; ED-912's gauge → `Tenure.degree` | `29f` |
| `systems/threadwork/sim/` | — | RETAINED (`ED-WR-0010`) | not in Step B; only its snapshot roles delete | — |
| `systems/social_contest/sim/` | social contests | `22` | the whole tree goes by `2-ii`; prize rows keep the logical name | `2-ii` |
| `systems/mass_battle/`, `systems/combat/` | retained | — | untouched except `massbattle.py`'s old entry | — |

**D.4 Test and tool importers still on disk.**

| file | disposition | position |
|---|---|---|
| `engine/tests/{test_mc_v18_regression,test_f7_smoke_oracle,test_combat_bridge_seam,test_pipeline_reach,test_world_population}.py`, `tests/valoria/test_engine_clock_phases.py` | `FORK:` (successors ran at `28-ii`; `test_combat_bridge_seam` needs none) | `28-iii` |
| `engine/tests/test_accounting_accord_drift_probe.py` | `FORK:` | `29a` |
| `engine/tests/test_parliamentary_action.py`; `tests/valoria/test_{faction_write_sweep,faction_stat_bounds,mass_seizure_accord_write,faction_obstacle_conventions}.py` | `FORK:`; `ED-FA-0038`, `ED-IN-0029`'s floors close (step 2) | `29b` |
| `tests/valoria/test_descriptors_runtime.py`, `test_world_initial_state.py` | lose one test each | `29b` |
| `tests/valoria/test_mass_battle_d1_morale_baseline.py` | **re-pin** against `resolve_field` | `20-iv` |
| `tests/valoria/test_settlement_temperament_drift.py` | `FORK:` | `29c` |
| `tests/valoria/test_conviction_roster_single_owner.py` | re-point | `29d`/`29e` |
| `engine/tests/test_knots_ed912.py` | `FORK:` | `29f` |
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
| MOD 1 — three routes into `systems/` | closes by sequence: after `2-ii` and `28-iii` there are exactly two (the combat PATH seam; one composition role for mass battle) | Lens B at `28-iii`, again at `2-ii` |
| MOD 4 — `npe`/`conviction` read `CONVICTIONS` | closes at `29d`/`29e`; shrinks the cells commit's audit | — |
| H-137 — the `write()` calling convention | step 4: CONVENTION grade, enforced by `/code-review` on each effect | every effect in Batches 2–4 |

## S. WHERE `/layer-conformance` HAS NEW SUBJECT MATTER — its output must be READ, not passed

| position | Lens B's subject |
|---|---|
| `28-iii` | `04 §A.2`'s module table, §C.5's routes, the provider-returns-a-Margin rule; `ID-13` over the deleted registry rows. **Lens A** matters most here: the `FORK:` rows and registry edits |
| each `29x` | `ID-13`'s consequences: the descriptor faction block, the re-pointed fixtures |
| `10` | the write class (ACTS at RESOLVE), the no-ledger-reference signature |
| `14` | the counterparty check in the fold; invariant 4 per conjunct |
| `22` | the provider returns a Margin, never a winner; the obstacle has one owner |
| `23` | the invariants |
| `2-ii` | the veto relocation only |

## G. THE 2026-09-18 PLAN'S §6 GAPS — what each is now

| gap | now |
|---|---|
| PART E step 12 (a parallel DELIBERATE map) and D-41a's permutation falsifier | unchanged — beside the critical path; no R-row moves on them |
| the FA lane | `20-ii` expressed the scale; `29b` retires `systems/factions/` |
| proceedings PHASE 1/3/4 | PHASE 1 done (`16`, `15d`); PHASE 3 → `22a`; PHASE 4 → `22b` |
| any GDScript grade | unchanged — nothing targets GDScript before `26` |
| the 143-case count has no single owner | unchanged — positions use the harness loader's count (`len(wd_acceptance.CASES)` for `11`) |
| `2026-08-15-character-and-faction-stats-and-progression.md`, ownership unresolved | unchanged; its live question is D2 (J-9) |
| the birth-side consumer of `capacity` | unchanged — no position builds one |
| D1-b #1, the chronicle render | unpositioned; the `chronicle` channel dies at `22` step 13 — a candidate M2 gate (main file §1) |

---

## E. THE END-STATE — true when Batches 1 and 3 complete

- `engine/mc_v18.py` is deleted with a `FORK:` row; `tests/valoria/test_mc_v18_is_deprecated.py` is
  deleted in the same commit after passing `ALLOWED_IMPORTERS == set()` as the intermediate state.
- `references/module_contracts.yaml` `composition_roles:` holds exactly ONE row,
  `mass_battle.resolve_field`. `composition.json` is regenerated behind `export_composition --check`. The
  `adapters:` block and its wiring rule are retired. The `engine_clock` contract row names the season
  calendar or is retired (M3's forward note).
- `engine/autoload/` is `{__init__, dice_engine, sigma_leverage}` — the substrate. `engine/cross_scale/`
  is gone. `engine/substrate/` keeps `canon_buckets`, `world_initial_state`, `pc_engine`, `composition`,
  `descriptors` (minus the faction-stat roster), `stubwire`, `names`.
- `systems/{overview, factions, world, characters, fieldwork}/` are gone with `FORK:` rows;
  `systems/settlements/` is reduced to `valoria_geography_v30.yaml`; `systems/social_contest/` is gone and
  its prize rows point at the proceedings provider; `systems/threadwork/`, `systems/mass_battle/`,
  `systems/combat/` are retained (`massbattle.py`'s old entry deleted; d.1 on `resolve_field`).
- Zero production imports of any spine module (the `ast` walk returns the empty set);
  `test_engine_does_not_import_systems.py` green at `BASELINE_TOTAL = 0`,
  `PATH_SEAM_ALLOWED = {'substrate/pc_engine.py'}`, fixtures re-pointed.
- Zero mentions of `mc_v18` outside the fork ledger, `CLAUDE_RATIONALE.md` and `registers/archive/`.
- `engine/tests/` is reduced to `test_thread_mending_ed871.py` (+ `test_sigma_leverage_parity.py` until it
  moves); the `sim-regression` job is folded into `unit-tests`; the `engine/season/tests` job is unchanged.
- `requirements.yaml`'s retire-set notes are rewritten: Step B executed; every scale row reads `in_loop`
  with its position, or (grid combat, character creation) names J-11.
- The successor artifacts have RUN: the same-seed hash pin (`test_build_realm_determinism.py`), the
  two-arm comparison on the season harness (`harness/arms.py`, P-7), and a battle from a chooser-formed
  decision (`test_march.py`; the realm fights one only if P-5/`20-iv` allow it). ⚠ The campaign-scale
  balance instrument `CLAUDE.md` §7 names has **no live successor**; that gap stays open and stated.

---

## K. HELD BACK FROM RATIFICATION-ON-MERGE (`CLAUDE.md` §2, ED-1094)

A merge of this plan ratifies **its ORDER** (`_part3` O.1–O.3 and the batch specs) **and the record that
it is the one active plan for the lanes it names**. Explicitly NOT ratified:
1. **Every §J item is OPEN** (`_part5`). Nothing gated on one becomes buildable because this merged.
2. **The §A answers ratify only as which ladder step answers each question and which candidate gets
   attacked** — never as the answer, which is decided at its position with the code in front of it. An
   attack that lands sends the question back through the ladder, not to Jordan by default.
3. **Content placements an ORDER document makes, each revertible alone:** `10` re-scoped to `fight`
   (A-12); `14`'s "no new closer rows" (A-16); the new handles `11-fix`, `13d-iii`, `R05-THREAD`,
   `LADDER-MBPC`; the decision-layer H-item deliverables carried into `_part5` B4; position 2's veto
   relocation carried into `2-ii`. If a content owner or a critic disputes one, that position reverts and
   nothing else in the order moves.
4. **No `## Status:` line on an absorbed proposal moves here.** Whether
   `proposals/2026-09-26-decision-layer-execution-plan/PROPOSAL.md` (a queue by its own declaration) and
   `proposals/2026-09-27-mc-v18-retirement-plan/PROPOSAL.md` are retired under the one-active-plan rule,
   now that this plan carries their remaining content, is the adoption commit's decision.
5. **No ledger id is allocated by this plan.** The adoption record and any `next_free` bump are the
   adoption commit's.

## N. NOT VERIFIED IN WRITING THIS PLAN — carried honestly

- Every pre-flight row P-1…P-8 (`_part3` §P).
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
| `28-0` (narrowed) | `domain_echo.py`, the fieldwork/investigation stubs | PR #439 — remainder is the `28-0` follow-up |
| `28-i` M5 | `balance_oracle.py` → `harness/arms.py`; the execution-map cluster retired | PR #439 (`FORK:c9daad6` rows, corrected by `f6d7af27`) |
| `28-ii` M6 | the `build_realm` hash pin; a battle from a chooser-formed decision **in a test** (`test_march.py`) | `013a5b1b`, `7ba66fde`, `6090af6b`; `test_build_realm_determinism.py` |
| `FIGHT-RENAME` · `OPENERS-DERIVE` · `GATE-REMOVE-PERSON` | `kill / wound` → `fight`; openers derived by AST; `remove_person` gated | PR #439; `test_gate_remove_person_requires_an_open_write.py` |
| PC lane item | `partisan` deletion; Ob-from-defender; `ED-PC-0058` | PR #439; `HANDOFF_PC.md` |
| MB slate | A1–A8, C4, C2/C3, d.1 | `ED-MB-0068`..`0074` |
| H1, H2 | record hygiene; the deontology gate (inert at `refusal_axis=None`) | 2026-09-27; H-146 |
| EFFECTS-SPLIT · CITATION-FIX · NERS/FABLE PASS · REGISTER/PLAN FIXES | `loop/effects.py` → six domain modules + shared + aggregator | `309a17d9`, `a882cc32`, `30dc8c65` |
| `27` (partial) · `10` (attempted, reverted) | coherence elastic/plastic + P-25 term; `tell`→stance reverted, side findings landed | PR #442 `c6f42528` |
| soak prerequisites | `wd_collect.py` rebased onto the rounds loop; `harness/soak.py`; U6/U5 decoupled | PR #446 `85afbf53` |
| realm measurements | H-156 cross-cite; R-01/R-06/R-07 realm paragraphs | PR #447 `06712837` |
| `B0-CI` (pending CI) | seven red `unit-tests` cleared | `f6d7af27` |

### H.2 Spent serial edges (both ends finished)

From the 2026-09-18 plan §3.9: 1 (G1b → `11a`), 2 (`13f` → `13e`), 3 (`13d-i` → G3), 4 (`13e` → `17a`),
5 (`18` → `18a`), 6 (`15` → `24e`, `15/15c` → `7a` → `17a`; `15` → `19b` is satisfied), 7 (`24d-i` →
`24e`, `19c`), 8 (`24f` → `body_step` — satisfied; the pick is J-6), 9 (G4 → `_eff_work`), 11 (`18a` must
not delete `Tenure.payload`). From the 2026-09-28 plan §3.5: 5 (FIGHT-RENAME → `8`), 6 (GATE-REMOVE-PERSON
↔ `24f`), 7 (`20-ii` → `20-iv`, satisfied), 8 (`13d-i` item 5 → `18a`).

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
| `2026-09-28-the-plan-one-order-mc-v18-retired.md` | §0 numbering/legend → main §0.2–0.3; §2.3 state → main §3; §3.3/§3.4 → Batches 1–3; §3.5 → `_part3` O.2; §3.6 → §S; §3.7 → §G; §4 → §C; §5.1 → `_part5` §J; §5.2 → `_part5` A-1; §6 → §E; §7 → §K; §8 records → §H.1; §9 → §N |
| `…_part2.md` | §1 → §D; §2 → §L; §3's live mappings → the batch specs (H-items, `24g`/`24h`, `20-iv`, `22a`/`22b`, `15d`/`17b` DONE) |
| `2026-09-30-phase-4-post-ners-revision.md` | §1.4 (eight always-refused) → `_part2` R-05; §1.5 (the retirement's cost) → `28-iii`; §2 → main §3; §3 (effect-file targets, `22`'s step-by-step state, `28-ii`'s evidence) → the batch specs; §4 → `_part5` J-4/J-16/J-17 |
| `2026-09-18-governance-settlement-behaviour-plan.md` + `_part2` | §3.0 cadence → main §0.4 (now its only home); §3.9 → `_part3` O.2/O.3; `_part2` §8 per-position text → the batch specs for `8`, `9`, `10`, `11`, `12`, `12b`–`12d`, `13`, `14`, `17`, `19b`, `21`, `22`, `23`, `24g`, `26`, `27`, `2-ii` |
| `2026-09-09-r-execution-plan.md` + `_part2` | U5 → `10` (re-scoped); U6's acceptance block → `11` (verbatim, slices re-derived); U7 → `14` (its group arithmetic superseded by `_part2` R-05's measured table); U8 → `17`; U10 → `21`-rest. U1–U4, U9: DONE |
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
