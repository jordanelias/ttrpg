# Valoria — Master Workplan v9, part 8: standing content · the adoption ledger (§K) · the Layer 0/1 table

## Status: part of v9 — see valoria_master_workplan_v9.md
## Reads after `workplans/valoria_master_workplan_v9_part7.md`. §C–§N are standing content the order relies on; §H.3/§H.4 are what adoption owes and where each retired plan's live content went. §K is the list of what adoption ratifies and what it does not; §M defines the session ids RS-n and G-n that every v9 file cites.
## Grade under `CLAUDE.md` §0.2: `paper`. Retired files are readable at the `FORK:` ref each row names; a pointer to one here is history, never an owner.

---

Position keys: v8 numbers stay as ALIAS in the blocks below — `22` = SC-01, `22a`/`23`/`22b` = SC-02, `2-ii` = SC-05, `31a`/`31b`/`31c` = IN-03/IN-04/IN-05, `30` = IN-02 (partly built), `33`/`36` = IN-06/IN-07, `34`/`35` landed, `27` = WR-01..03 (`_part7`), `24g` = SE-01, `19b` = IN-09. The home of each is `valoria_master_workplan_v9.md` §3 (state index) and §4 (crosswalk).

## C. THE NINE CONTRADICTIONS (2026-09-28 plan §4, `FORK:0671283`) — each resolved to one side; none went to Jordan

| # | subject | resolved to | ladder step | where it now lives |
|---|---|---|---|---|
| 1 | `Office.upkeep` | kept off `18a`'s list; its reader built at `17b` (Layer 1 `Seat :=` includes `upkeep`; r2 `05`: *"Deleting `Office.upkeep` removes the carrier, not the gap"*) | 3 | DONE (`17b`) |
| 2 | C1–C4 "derive, no code change" | narrowed: the decision-layer H6 lands the content; the cells are Jordan's | 1 | IN-08 (`_part5`), J-1 (answered 2026-10-06: the candidate drafts are folded in, §K (a)) |
| 3 | the M-7 obstacle remedy | the obstacle **CEILING**, value injected and swept, attacked at `22` — never a pool floor | 5 (ratified by `ED-IN-0270`) | SC-01 step 14 (`_part6`) |
| 4 | the `kill / wound` rename | renamed standalone to `fight` (DONE). The `kill`/`wound` half of the SPLIT is CLOSED: they are not verbs, they are outputs of a `fight` or duel having been called (Jordan's own words, §K (a), #453 §13.9 adopted); only `challenge` → `accept` ride the cells commit | 1 + 3 | IN-08 (`_part5`), B-G |
| 5 | `HANDOFF_IN.md`'s M4 row | a stale fact; `ecacb57` seeded garrisons and ran all four reviews | — | closed |
| 6 | the count of contested verbs | a stale fact; 3 contested verbs (`fight`, `march`, `tell`) | — | closed |
| 7 | proceedings step numbering | `21_RECONCILIATION.md` PHASE 1's numbering | — | closed |
| 8 | `ED-IN-0251` row 2's field against its text | a new `ED-IN-0261` row carrying `needs_jordan: true` | 5 | J-1 (answered 2026-10-06, §K (a)) |
| 9 | `queries/` — three modules or four | `04 §A.2` edited at `20-ii` to name `faction_q` | 3 | DONE (`20-ii`) |

---

## D. STEP-B DISPOSITIONS — every spine file, role, retire-set tree and importer, and what replaced it

Carried from the 2026-09-28 plan's `_part2` §1 (`FORK:0671283`), refreshed 2026-10-01 (25 roles when written). Keys: **(a)** a
season-native replacement exists, named · **(b)** a replacement must be built, positioned · **(c)** dead
or orphaned, deleted with a `FORK:` row. **A row marked DONE was deleted at v8's Batch 1 (PR #450)**: it stays
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
| `systems/overview/sim/ms_track.py` | **(c)**, after `27` frees threadwork of it | `29a`-ms — CANCELLED 2026-10-02 (A-24): the tree stays |
| `engine/autoload/` (what survived: `__init__`, `dice_engine`, `sigma_leverage`) | renamed `engine/dice_engine/`, names kept (A-25) | `34` |

**D.2 The 25 composition roles** (`references/module_contracts.yaml`; one survives; from `30` the block's rows carry an `entry:` kind and are the module-entry surface, `_part5` A-25).

| role(s) | disposition | position |
|---|---|---|
| `mass_battle.resolve_field` | **the one survivor (a)** — consumed by `seam/wrappers/mass_battle.py`; re-keyed to `modules/mass_battle/` with `entry: verb_call` | `31c` |
| `season_driver`, `faction_action`, `accounting` | **(a)** the driver + `march`/`via`-seat acts; MATTER/CENSUS | rows `28-iii` — DONE |
| `scene_builder.contest`, `scene_resolver.contest`, `contest_side.a/.b` | rows **(c)**; the kernel's resolution line is **(a)** `sigma.py`; the veto is **(b)**, relocated at `2-ii` | rows `28-iii` — DONE; kernel `2-ii` |
| `snapshot_state.*` ×10 | **(c)** with `restore_world` (its only caller is a test); the threadwork modules stay (`27`); `knots` stays (`29f` cancelled, A-24); `beliefs` orphaned by design | `28-iii` — DONE |
| `world_gen_settlements` | **(a)** `build_realm` | `29b` — DONE |
| `parliamentary_vote/motion/vote_declaration` | **(c)**; their caller `parliamentary_transfer.py` is production-orphaned; faction acts are person acts `via` seats (G3); their verb content is `levy`/`open_case`/`determine`/`issue` + `march` | `29b` — DONE |
| `rs_track_delta`, `territory_transfer_candidate/proposal` | **(c)**; "kept named" had no reader (`ID-13`) — record the ruling's expiry | `28-iii` — DONE |

**D.3 Retire-set trees** (each goes only when the loop expresses its scale — `requirements.yaml`'s gate). ⚠ SUPERSEDED 2026-10-02 (A-24) for `characters`, `fieldwork` and `overview`: the `systems/` folders are kept as the homes of their systems, and the `retire-set` label was wrong. Whether the PR #450 deletions below return is OPEN with Jordan. ⚠ SUPERSEDED (A-25; `ED-IN-0284`, `ED-IN-0285`) for `systems/social_contest/`: it keeps its name, the social contest module's running code is `modules/social_contest/` from `31a`, `22` evaluates the kernel, and `2-ii` (HELD) would delete `contest/` only, not "the whole tree".

| tree | scale | season expression | notes | position |
|---|---|---|---|---|
| `systems/factions/sim/` | grand strategy politics | `20-ii` ✓ | `resolve_mass_battle`/`_faction_to_unit`/`_morale_start_from_stability` die with `game_state.Faction`; d.1 moves to `resolve_field` at `20-iv` | `29b` — DONE |
| `systems/settlements/sim/` | settlement management | `24e` ✓ + `24d-ii` ✓ | `registry` → `build_realm` (which reads `territory` and `type` only: `settlements.*.stats` and `.controller`, the latter a copy of the province's `faction`, have had no reader since `29c`); `infrastructure` → `Site.condition`/`fortification_of`; `temperaments` → stance; `adjacency` **(c)** — no province graph, invent none; **the geography YAML stays** | `29c` — DONE |
| `systems/world/sim/` | grand strategy / settlement | `20-ii` ✓ | `npe` → `decision/` + stance; `insurgency_pipeline` → `24h` P5 | `29d` — DONE |
| `systems/characters/sim/` | character creation/development | the cells commit + `12` (+ `14` for `conviction` ← `knots`) | `beliefs` **(c)** by design; `conviction` → `Person.pursuits` / scar counts | `29e` — CANCELLED (A-24): the tree stays |
| `systems/fieldwork/sim/knots.py` | investigations | `14` (`tie / knot`) + `27` | the `knot` Tenure kind and `firsthand_via_knot` exist; ED-912's gauge → `Tenure.degree` — **that mapping's source is UNLOCATED** (`H-182`'s cite) | `29f` — CANCELLED (A-24): the tree stays |
| `systems/threadwork/sim/` | — | RETAINED (`ED-WR-0010`) | not in Step B; only its snapshot roles delete | — |
| `systems/social_contest/sim/` | social contests | `22` | the whole tree goes by `2-ii`; prize rows keep the logical name | `2-ii` (HELD, A-24) |
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
| `tests/valoria/test_conviction_roster_single_owner.py` | re-point | `29d` — DONE (`systems.world` site); `29e` — CANCELLED (A-24): the site stays |
| `engine/tests/test_knots_ed912.py` | `FORK:` | `29f` — CANCELLED (A-24): the test stays |
| `engine/tests/test_contest_kernel.py` | `FORK:` | `2-ii` |
| `engine/tests/test_thread_mending_ed871.py` | stays (`27`) | — |
| `engine/tests/test_sigma_leverage_parity.py` | substrate — stays; moves out of `engine/tests` when `sim-regression` folds | `2-ii` |

---

## L. LAYER-1 NODES STILL LIVE (2026-09-28 plan `_part2` §2, `FORK:0671283`; the rest are closed)

| node | verdict | destination |
|---|---|---|
| invariant 4, the per-conjunct half | built at `19` | `23` checks what remains flat |
| F.20b — three body-literal Event kinds (invariant 7): *"the loop as built cannot run under the loader as specified"* | survives | `23` |
| invariant 2 — producerless matrix rows | step 3: each row is some position's content | enforceable at `23` once producers exist |
| MOD 1 — three routes into `systems/` | closes by sequence: `28-iii` landed (one composition role remains, `mass_battle.resolve_field`); after `2-ii` there are exactly two routes (the combat PATH seam; that one role) | Lens B at `2-ii` |
| MOD 4 — `npe`/`conviction` read `CONVICTIONS` | `29d` landed (`npe`); `conviction` stays (`29e` cancelled, A-24); shrinks the cells commit's audit | `29d` (`npe`) landed; `conviction` STAYS (`29e` cancelled, A-24), so MOD 4 stays open until the cells commit (IN-08, B-G) |
| H-137 — the `write()` calling convention | step 4: CONVENTION grade, enforced by `/code-review` on each effect | every effect written from B-G through B-L in `_part3` §B's spine order (B-G, B-H, B-E, B-F, B-I, B-J, B-K, B-L: the cells, telling, matter, verb and module positions that carried it), and every later batch that writes one |

## S. WHERE `/layer-conformance` HAS NEW SUBJECT MATTER — its output must be READ, not passed

| position | Lens B's subject |
|---|---|
| `10` | retired — the telling workplan is absorbed (`valoria_master_workplan_v9.md` §0.6); IN-16..IN-18 carry its Lens A/B subjects (A on T3a, B on T2), and its As-built stays at `FORK:<sha>` |
| `14` | the counterparty check in the fold; invariant 4 per conjunct |
| `30` | the registrar runs at driver construction, never at `World.boot` or at import; module entries are reached by string only; `EFFECTS` stays host (`_part5` A-25) |
| `31a`–`31c` | each module reads a typed input record, never `World`; it holds no token, opens no write, imports no other module, keeps no module-level state; every re-pinned floor sits under a superset assertion; `31b` against `04` T-k |
| `33`, `36` | a design is read before anything is built; the clause cited for a store is AX-4 at D-3, never D-8 |
| `22` | the provider returns a margin, never a winner; the obstacle has one owner; the provider is reached by string, never imported, and lands in the prize re-point's commit (A-25) |
| `23` | the invariants |
| `2-ii` | the veto relocation only |

## G. THE 2026-09-18 PLAN'S §6 GAPS (`FORK:0671283`) — what each is now

| gap | now |
|---|---|
| PART E step 12 (a parallel DELIBERATE map) and D-41a's permutation falsifier | unchanged — beside the critical path; no R-row moves on them |
| the FA lane | `20-ii` expressed the scale; `29b` retired `systems/factions/sim/` (PR #450) |
| proceedings PHASE 1/3/4 | PHASE 1 done (`16`, `15d`); PHASE 3 → `22a`; PHASE 4 → `22b` |
| any GDScript grade | unchanged — nothing targets GDScript before `26` |
| the 143-case count has no single owner | unchanged — positions use the harness loader's count (`len(wd_acceptance.CASES)` for `11`) |
| `2026-08-15-character-and-faction-stats-and-progression.md`, ownership unresolved | unchanged; its live question is D2 (J-9) |
| the birth-side consumer of `capacity` | unchanged — no position builds one |
| D1-b #1, the chronicle render | the `chronicle` channel dies at `22` step 13 — a candidate M2 gate (`valoria_master_workplan_v9.md` §1); a chronicle render outside the simulation is IN-37 (STORY-READ, ENP v2 proposal 1, B-U) [UNVERIFIED: that D1-b #1 is the same render was not re-opened] |

---

## E. v8's END-STATE — each target is history, superseded, or carried by a named v9 owner

v8 framed this list on its own Batches 1 and 3. Each bullet is marked **[LANDED]** (read against the tree
2026-10-01, v8's Batch 1, PR #450: history, kept as the record of why the files went), **[SUPERSEDED]**, or
**[v9: owner]** where a v9 position carries what remains; a target no v9 position owns says so.

- **[LANDED]** `engine/mc_v18.py` is deleted with a `FORK:` row; `tests/valoria/test_mc_v18_is_deprecated.py` is
  deleted in the same commit after passing `ALLOWED_IMPORTERS == set()` as the intermediate state.
- **[LANDED]** `references/module_contracts.yaml` `composition_roles:` holds exactly ONE row,
  `mass_battle.resolve_field`. `composition.json` is regenerated behind `export_composition --check`. The
  `adapters:` block and its wiring rule are retired. The `engine_clock` contract row names the season
  driver and calendar (M3's note, `valoria_master_workplan_v9.md` §1). ⚠ This records v8's Batch 1. **[v9: IN-02, B-B; IN-05, B-L]**
  From `30` (A-25) the block's rows carry an `entry:` kind and are the module-entry surface; `31c` re-keys `mass_battle.resolve_field`.
- **[LANDED]** `engine/autoload/` is `{__init__, dice_engine, sigma_leverage}` — the substrate (renamed
  `engine/dice_engine/` at `34`). `engine/cross_scale/`
  is gone. `engine/substrate/` keeps `canon_buckets`, `world_initial_state`, `pc_engine`, `composition`,
  `descriptors` (minus the faction-stat roster), `stubwire`, `names` — ⚠ `canon_buckets` and
  `world_initial_state` now have no production importer (`29d-ii`).
- **[SUPERSEDED, A-24; v9: SC-05 for `contest/`, held on its timing in B-Z]** `systems/{overview, factions, world, characters, fieldwork}/` are gone with `FORK:` rows — SUPERSEDED 2026-10-02 (A-24);
  `systems/settlements/` is reduced to `valoria_geography_v30.yaml`, its svg and a package marker; `systems/social_contest/` is gone and
  its prize rows point at the proceedings provider; `systems/threadwork/`, `systems/mass_battle/`,
  `systems/combat/` are retained (`massbattle.py`'s old entry deleted; d.1 on `resolve_field`).
  **Partly landed:** `systems/factions/sim/`, `systems/world/sim/`, `systems/settlements/sim/` and
  `massbattle.py`'s old entry are gone (PR #450) and Jordan has been asked whether they return (A-24);
  `systems/overview/`, `systems/characters/` and `systems/fieldwork/` STAY; `social_contest` is `2-ii`'s
  and HELD. ⚠ SUPERSEDED (A-25) as to `systems/social_contest/` being "gone": it stays, the module's running
  code is `modules/social_contest/` from `31a`, and `2-ii` would delete `contest/` only.
- **[LANDED]** Zero production imports of any spine module (the `ast` walk returns the empty set);
  `test_engine_does_not_import_systems.py` green at `BASELINE_TOTAL = 0`,
  `PATH_SEAM_ALLOWED = {'substrate/pc_engine.py'}`, fixtures re-pointed.
- **[v9: IN-43, B-C; `CLAUDE.md`'s paragraph is IN-44's]** Zero mentions of `mc_v18` outside the fork ledger, `CLAUDE_RATIONALE.md` and `registers/archive/`.
  **Not yet:** `git grep -l mc_v18 -- ':!.audit' ':!.designs' ':!registers/archive' ':!references/restructure_ledger.md' ':!CLAUDE_RATIONALE.md'` lists 147 tracked files (re-measured 2026-10-06 on `7b619328`; the adoption's retirements remove some). The sweep of those mentions is IN-43's sub-item (B-C), on Jordan's 2026-09-27 *"we need to move beyond any mention or use of this mc_v18"*; `CLAUDE.md`'s own paragraph is Layer 0 and stays in the IN-44 table below.
- **[SUPERSEDED in part, A-24; v9: SC-05 for the rest; the job fold has NO v9 owner]** `engine/tests/` is reduced to `test_thread_mending_ed871.py` (+ `test_sigma_leverage_parity.py` until it
  moves); the `sim-regression` job is folded into `unit-tests`; the `engine/season/tests` job is unchanged.
  `git ls-files engine/tests` (2026-10-06) lists `test_contest_kernel.py`, `test_knots_ed912.py`,
  `test_sigma_leverage_parity.py` (+ its golden) and `test_thread_mending_ed871.py`: `test_knots_ed912.py` stays
  (`29f` cancelled, A-24); `test_contest_kernel.py` and the parity test's move are `2-ii`'s (SC-05, §D.4); no
  position schedules the `sim-regression` fold, so it is a target only.
- **[SUPERSEDED, A-24; v9: `_part2` R-04's table of the `scales:` rows]** `requirements.yaml`'s retire-set notes are rewritten: Step B executed; every scale row reads `in_loop`
  with its position, or (grid combat, character creation) names J-11 — SUPERSEDED 2026-10-02 (A-24): the
  scale roster now says RETAINED for characters, factions, settlements/overview and fieldwork. What each
  `scales:` row now waits on is `_part2` R-04 conjunct (3)'s; grid combat and character creation are
  IN-46 and IN-47 (designs, B-C).
- **[LANDED]** The successor artifacts have RUN: the same-seed hash pin (`test_build_realm_determinism.py`), the
  two-arm comparison on the season harness (`harness/arms.py`; ran end to end at P-7, both arms
  identical), and a battle from a chooser-formed decision (`test_march.py`; the realm fights none — P-5
  found H-149's target-kind check refuses all 11 marches, and `20-iv` did not change it; the realm's first
  fought field is IN-13's, B-M). ⚠ The campaign-scale
  balance instrument `CLAUDE.md` §7 names has **no live successor**; that gap stays open and stated.

---

## K. THE ADOPTION LEDGER — what merging v9 ratifies, retires and holds back (`CLAUDE.md` §2, ED-1094; ED-IN-0286)

A merge of v9 ratifies **its ORDER** (`valoria_master_workplan_v9_part3.md` §B's file-affinity batches B-A … B-T with B-Z, their membership rules and §C's collision matrix) **and the record that it is the one active plan for all nine lanes** — no carve-out, every earlier plan retired (b). The adoption commit is B-A's (after the CI-fix commit `7b619328`, its own commit). A design document ratified in (a) is ratified **AS INTENT only** (`CLAUDE.md` §0.05): the `## Status:` flip and the ledger row adopt what the document wants; nothing exists in `engine/season/` until its executing position is built with its test, and no document here is the reason a behaviour is correct. (c) has two halves: the ten items Jordan's 2026-10-06 *"adopt plan recommendations then"* (RS-21) turned into the plan's adopted recommendations — **ratified on merge as the plan's recommendation, [medium; Jordan to correct]**, each revertible alone — and the STILL HELD list, which this merge does not answer: no position gated on a still-held item becomes buildable because v9 merged. **The exhaustive list of what adoption changes is the adoption commit's own diff** (`git show --stat <adoption commit>`), with the `FORK:` rows and ledger rows it adds; a `## Status:` line or ledger row that diff does not touch is unchanged, and there is no mass flip.

**(a) RATIFIED BY ADOPTION — intent only, with the executing handle**

| object | what the flipped Status and the ledger row say | executes at | ledger row |
|---|---|---|---|
| `proposals/2026-09-26-decision-layer-execution-plan/candidate_pursuit_cells.md` and `candidate_affiliation_content.md` (with ED-IN-0261's fifteen pursuits) | **FOLDED INTO THE BUILD** as the source of the cells — Jordan, 2026-10-06: "so for candidate_*, let's just fold them in to build unless we can find any reason why not to?" (the 105 projection cells, the alignment re-cell and the doctrine pair, and the affiliation roster, the ten `incompatible:` cells, the intensity scale, the verb × affiliation table and G-Q6, are answered). They stay on disk as the authoring surface until IN-08's cells commit lands, then retire with `proposals/2026-09-18-character-decision-layer/PROPOSAL.md`, which they cite as S11. Folding in also accepts what the drafts ask Jordan to accept: the sign convention (`candidate_pursuit_cells.md` §0.1: negative = first-named pole); G-Q5 = NEITHER a per-person precedence (keep gate-then-score; no `Person.precedence`; drop PROPOSAL.md §7 steps 3–6, H12); the 55 REASONED cells as placed; G-Q6 as the affiliation file recommends. Two build conditions: (1) coverage — the extension of the alignment table to build, found, give, march, migrate and survey lands INSIDE IN-08's atomic cells commit (B-G), by the draft's own method, each cell graded `reasoned` and showing its reasoning. The loader does not raise on a sparse table (`engine/season/data/verbs.py:956-957`: *"IT DOES NOT CHECK THAT ALL ... CELLS ARE PRESENT"*); "partial landing" means a half-done roster swap, so the falsifier is that every table verb has a cell on each axis or sits in a declared `uncelled:` set (`tell`, `thread_read`, `restore`) with its reason, and every verb row added after IN-08 lands with its cells. `tell` stays uncelled by design (the draft's §3.6: telling is driven by regard, not pursuit): R-06 and R-08 count only candidates whose verb has at least one celled axis (G-1, [medium; Jordan to correct]; revert: Jordan states that `tell` gets cells). `engine/season/requirements.yaml` carries no `met` wording for either row (R-06 `:833-979`, R-08 `:1033-1088`: `statement:`, `status:`, `measured:`, `measure:`, `blocks:`, and one `disposition:` and `needs_jordan:` across R-06..R-08), so nothing there is re-worded; what IN-08 owes (B-G) is `corpus_run`'s RANKING line (`engine/season/harness/corpus_run.py:969`) counting only candidates whose verb has a celled axis, with its numerator and denominator printed, and a `measured:` note in R-06 and R-08 recording that reading; neither is made at adoption; (2) the doctrine pair is pinned at the draft's weights and its margin recorded, not gated. `kill` and `wound` are moot in the draft (they are not verbs, the #453 row below); `challenge` and `accept` arrive with the cells commit. **Renames, Jordan 2026-10-06:** the pursuit `faith` is `doctrine` ("you can change \"faith\" to \"doctrine\""); its row is PROVISIONAL — "when we get to cell values and cosines for the axes*poles stuff, doctrine will change" — so the doctrine-pair margin is not a blocker and the pair is judged on the row as it stands at that pass (the CELL-VALUE AND COSINE PASS, ask-then after B-G, (c)); the pursuit `warden` is `stewardship` ("sure, stewardship works for warden"; RULED); the in-world Warden offices, faction and titles are unchanged | IN-08 (B-G, B-H) | ED-IN-0291 (new, `ratified`): RS-1..RS-4 as ruled and the ten RS-21 adoptions as the plan's recommendations (`needs_jordan: false`), allocated by the adoption commit; and a superseding row on ED-IN-0261 (e) |
| `proposals/2026-10-04-forcing-churn-and-the-story-bar.md` | RATIFIED AS INTENT (v9) for the §4 handles whose class is not held — STORY-BAR, STORY-SOAK, STORY-READ, FORCE-WEATHER, FORCE-HAZARD with SEAM-CLOCK (its class answered [medium] by ladder step 3/4, the plan's own recommendation: `canon/philosophy/RULINGS.md` D-3 reads "Ruled: tensile", so the Calamity is a consequence of held configurations failing, not a matter motion, and its baseline is Jordan's 2026-10-04 "if not managed, will expand ... with ever increasing intensity"; the build waits on IN-06's build), CARRY-INTERIOR, CARRY-SHORTFALL, CARRY-STABILITY, BOUND-LOOPS, BOUND-STAKES, BOUND-ATTENTION, BOUND-PAPER, SEAM-LADDER, and CAST-DISPOSITION's alignment cells (its `tell` half answered by the draft: `tell` stays uncelled, G-1, the row above). CARRY-INTERIOR's falsifier (*"after a lost field or famine, stance rows change for witnesses"*, `:161`) is IN-18 G1's and IN-13's, re-expressed as regard-at-read. **Ratified on merge as the plan's recommendation, [medium; Jordan to correct]** (RS-21, (c)): FORCE-BODIES (§7 item 2, D2 → IN-34), FORCE-FOREIGN (§7 item 4, D4 → IN-36, with FA-01's content, which owns the Schoenland trade demand, G-6), END-VICTORY (§7 item 6, D6 → IN-27, IN-30) and CAST-DISPOSITION's capability writer (J-13 (iii) → IN-12 step 9). §5 cuts stand; §6 superseded by v9's order; §7 item 1 answered [medium] (below), item 3 answered (a dated pin is a clock, T-c), item 5 is A-24's threadwork re-plug, scheduled as IN-06 (design B-C, build B-S). **CAST-POPULACE is NOT ratified:** its spread construal is still held, (c) | IN-19, IN-20, IN-37, IN-21, IN-35, IN-08, IN-18, IN-13, IN-22, IN-23, IN-24, IN-25, IN-14, IN-26, IN-04; and IN-34, IN-36, IN-27, IN-30, IN-12 step 9 as adopted recommendations | ED-IN-0287 (its text as this row: CAST-POPULACE the one handle not ratified) |
| `proposals/2026-10-03-verb-coverage-and-gap-fill.md` | RATIFIED AS INTENT (v9): §7 suite and §10.4 build order scheduled — step 2a (`known_persons` stops discarding the topic) is IN-18's; steps 5, 5a, 8 and 11 build on `remit_default` (J-8 is partly answered [medium], (c)); step 9 (`train`, IN-12, B-Q) is ratified on merge as the plan's recommendation (J-13 (iii), RS-21 item 10, [medium; Jordan to correct]); §13 R-1(b) no `execute`, R-3(b) cut `repudiate`, R-4(b) no basis for a rungless top seat, R-8(b) closed set, R-9(a) grudges end by `forgive` — each adopted at the step it names; R-5 (b), `inheritance` as a fourth conferral basis, is IN-51 (B-R; RS-21 item 9, [medium; Jordan to correct]); §6.1 reference. The positions its hooks need beyond §10.4: `oblige` formable from a held Record's terms and `confer` + `Tenure.term` (IN-10 sub-steps, B-I), `survey` + Rung (B-K) and `give` + Rung (B-R), the occupation-subsistence hole row and R-6/R-7 (IN-13, B-M), the `open_case` fired-slot → `convene` step (SC-01, B-N), `levy`'s question source (IN-49, B-K), H-108's delegation half (IN-48, B-J). **§13.9's kill/wound reading is ADOPTED — Jordan's own words, DIRECT, not [medium]:** `kill` and `wound` are not verbs, the pending split of `fight` is closed, death and wounding are outputs of a `fight`/`duel` having been called, and `challenge` → `accept` stay (the duel; that composition rests on a short reply, *"3 accept"*, so it carries [medium] per the 2026-09-09 caution on lettered answers). **Not ratified with the suite: K-23** — #453's reading of a challenge as a `petition` answered by the acceptor's `fight`, with no new verb (`:242-244`; the `fight` hook *"the acceptor of a challenge `petition` (K-23)"*, `:514`; the judicial-duel composition, `:2070`) — is struck by IN-08 (RS-18), which adds the two rows instead. Jordan: 2026-09-20 "kill and wound should not be verbs" / "there needs to be fight and duel"; 2026-09-27 (rPzvoNzn, ea741a6c-7194-4564-9f6c-cce425b2fa3b) "I ruled that kill/wound doesn't make sense as a verb choice because a character can't choose to kill or wound a other -- they can only attempt to do so. Kill/wound is the output from a duel/personal combat having been called."; 2026-10-03 (#453 `:234-235`, `:2292-2293`); the same direction on 2026-09-02/03 (f137d58d-eb77-46ae-9609-f0bf71d47511, 7ddd542d-2301-4e7c-8410-5147f6268abe); `engine/season/verb_table.yaml:442-448` | IN-10..IN-13, IN-18 (step 2a), SC-03a/b, SC-01 (the fired slot), IN-08 (the verb split without `kill`/`wound`; the K-23 strike), IN-45, IN-48, IN-49, IN-51 | ED-IN-0288 (its text: §13.9 kill/wound ADOPTED and the K-23 strike, as this row) |
| `proposals/2026-09-05-proceedings-subsystem/` — `README.md`, `21_RECONCILIATION.md`, `04_VERBS.md` only | RATIFIED AS INTENT (v9): ownership `ED-SC-0033`; PHASE 2–4; 00–20 reference, superseded in part by 21 | SC-01, SC-02 | ED-SC-0039 |
| `proposals/2026-09-17-governance-and-behaviour/` | `RULINGS.yaml` SPENT; `01_THE_BUILD_ORDER.md` ABSORBED (Phases 1–5 landed; Phase 6 → IN-08: 6f at B-H; 6g, H-71's second half, as IN-08's entry maps it or states it unmapped); `00`, README reference | IN-08 | ED-IN-0243 → `ratified` (intent) |
| `proposals/2026-09-17-governance-and-holdings/03_THE_SURFACE.md` | RATIFIED AS INTENT (v9): the Surface behind PC-06 S-2/L-1 | PC-06 | ED-IN-0237 → `ratified` for `03` as intent, worded as the row's own 2026-09-17 split: `03_THE_SURFACE.md` STANDS; `04_BUILD_ORDER.md` IS SUPERSEDED by r2's `05_LEDGER_AND_BUILD.md` (ED-IN-0233) and retires with its `FORK:` row (b) |
| `…-holdings-r2/` `01`–`05` | RATIFIED AS INTENT (v9); absorbed where built (`03` → `offices.yaml`, `04` §A.3–A.4 → `matter.py`, `05` → the plans); residue → IN-28, SE-03 (B-K); `EXECUTION_PLAN.md` retires (b) | IN-28, SE-03 | ED-IN-0233, ED-IN-0234 (`02`; its flag was cleared 2026-09-17 by AX-7, ED-IN-0244), ED-IN-0235, ED-SE-0053 → `ratified` (intent) |
| `proposals/2026-09-16-conviction-decision-layer/` — the four kept files | status REFERENCE: rulings absorbed into ED-IN-0251/0261, cited as a register; ratifies no mechanism | — | — |
| `proposals/2026-09-30-character-and-play-surface/README.md` | RATIFIED AS INTENT (v9) for S-1, M-1/S-4, S-2/L-1, K-3, U-3, P-1 (→ IN-18 G1 / IN-13, re-expressed as regard-at-read), P-2 and P-3's mechanism; S-6 → FI-01, its deposit half built as H-111's SKIP arm (RS-21 item 1, [medium; Jordan to correct]); V-1 follows IN-09's `comply` cell; K-2 only with its first reader; K-4 (a `practice` verb) superseded by IN-12 step 9's `train`; `05` §4.1/§4.2 attach to M-2; `05`'s two modes of one bout are Jordan's stated intent (SM-5, below), and the suspension design is IN-46 (design, B-C). P-3's content (FA-01 content, B-V) is ratified on merge as the plan's recommendation (#457 D4, RS-21 item 4, [medium; Jordan to correct]). The character-sheet management space (creation, development, chronicling) is IN-47 (design, B-C). The rest reference | PC-06, MB-04, IN-08, IN-18, IN-13, IN-22, FA-01 (mechanism; content as adopted), FI-01, IN-46, IN-47 (designs) | ED-IN-0290 |
| `proposals/2026-09-10-settlements-factions-populations/00_INDEX.md` | RATIFIED AS INTENT (v9): P2/P3 → SE-01; P5 → IN-30 (B-U), ratified on merge as the plan's recommendation (#457 D6, RS-21 item 3, [medium; Jordan to correct]); P1/P4/P6/P7 absorbed or superseded; rest reference | SE-01, IN-30 | — |
| `proposals/2026-09-12-emergent-narrative-primitives-v2/00_INDEX.md` (ENP v2) | RATIFIED AS INTENT (v9) for proposal 1 (the chronicle render, IN-37) and proposal 5 (the bodies clock → IN-34, ratified on merge as the plan's recommendation: #457 D2, RS-21 item 5, [medium; Jordan to correct]); proposal 13 (the populace as a weighted Person → SE-04 (c)) is NOT ratified: the CAST-POPULACE spread construal is still held, (c); rest unscheduled | IN-37, IN-34 | ED-IN-0217 → `ratified` (partial: proposals 1 and 5; 13 held) |

**(b) SUPERSEDED / RETIRED — pointer only.** Deleted in the adoption commit (B-A), each with an exact-file `FORK:` row in `references/restructure_ledger.md`, plus a directory-prefix row where a directory is cited as a directory (`tools/pathres.py` matches a directory only through a prefix row): v8's six files, the telling workplan, and the superseded proposal files the Gather's dispositions name. **The retirement set is 47 files with 50 `FORK:` rows: 47 exact-file rows and THREE directory-prefix rows.** Every path below was checked with `git ls-files` on `7b619328` (2026-10-06): all 47 are tracked, and each prefix directory's tracked set equals the files listed for it (15, 7 and 3), so a prefix row retires nothing unlisted.

| group | files deleted | n | kept beside them |
|---|---|---|---|
| `workplans/` | `valoria_master_workplan_v8.md`, `valoria_master_workplan_v8_part{2,3,4,5,6}.md`, `2026-10-01-telling-workplan.md` | 7 | — |
| `proposals/2026-09-17-governance-and-holdings/` | `00_THE_DESIGN.md`, `01_SEATS_AND_POLICY.md`, `02_THE_BUILT_WORLD.md`, `04_BUILD_ORDER.md`, `AUDIT_VERDICT.md`, `UNIFICATION_LEDGER.md` | 6 | `03_THE_SURFACE.md`, `README.md` |
| `proposals/2026-09-17-governance-and-holdings-r2/` | `EXECUTION_PLAN.md` | 1 | `01`–`05` |
| `proposals/2026-09-16-conviction-decision-layer/` | `behaviour_algorithms.md`, `behaviour_census.md`, `interrogation.md`, `decision_layer_v1.md` | 4 | the four reference files ((a)) |
| `proposals/` (loose) | `2026-09-18-conviction-basis-worksheet.yaml` | 1 | `2026-09-18-conviction-basis-probe.py` |
| `proposals/2026-09-18-the-gather/` | `05_THE_ORDER.md`, `README.md` | 2 | `00`–`04` |
| `proposals/2026-09-28-repository-armature/` | `ARMATURE.md` | 1 | — (no prefix row: nothing cites the directory as a directory) |
| `proposals/2026-09-12-emergent-narrative-primitives/` **+ prefix row** | `00_INDEX.md` … `06_VALORIA_UNPLOTTED.md` | 7 | v2 is a different directory |
| `proposals/2026-09-16-term-ownership/` **+ prefix row** | `README.md`, `key_type_registry.yaml`, `offices_draft.yaml` | 3 | — |
| `proposals/2026-09-04-social-contest-branches/` **+ prefix row** | `00_BRANCH_SHAPES.md` … `13_PARLIAMENT_FOLD_AND_RECALIBRATION.md`, `OUT_OF_SCOPE.md` | 15 | — |

Re-derive both counts after the commit: the deleted paths are `git show --diff-filter=D --name-only <adoption commit>`; the rows are the `FORK:` rows citing ED-IN-0289 in `references/restructure_ledger.md` (`<sha>` = the parent of the deleting commit); `grep -c 'ED-IN-0289' references/restructure_ledger.md` reads 0 before the commit — the rows land with it. A file with a live reader is not deleted until the reader is re-pointed in the same commit; a cite left in a comment, docstring or provenance string (for example `engine/season/offices.yaml:112`'s `derivation:` string, which no loader reads) resolves through its `FORK:` row. **`proposals/2026-09-18-character-decision-layer/PROPOSAL.md` is NOT retired:** the Gather's own disposition splits it (`proposals/2026-09-18-the-gather/03_DECISIONS.md` §2) — §1 is superseded, but §2 (the class-test vocabulary FIELD/READOUT/STRUCTURE/DISPOSED and the `bend_price` collapse), §4 (F1) and §6 (the measurements the probe reproduces) are live reference, and the class-test text exists only there; it stays until the cells commit (IN-08, B-G) lands, then retires with the two drafts that cite it as S11, by that commit's own `FORK:` rows. ED-IN-0289 records the Gather's dispositions as applied; ED-IN-0282's superseding row reads "absorbed; nothing re-ruled" — the telling workplan's order is restated at IN-16..IN-18, never re-decided. Nothing under `systems/`, `engine/`, `architecture/`, `.designs/` or `.audit/` is touched.

**(c) THE TEN ADOPTED RECOMMENDATIONS, AND WHAT IS STILL HELD.** `_part5` §J carries each item's options; this list is unranked, and `_part5` §J ranks what is still held.

**(c-adopted) RATIFIED ON MERGE AS THE PLAN'S RECOMMENDATION, [medium; Jordan to correct].** Jordan, 2026-10-06, verbatim: *"adopt plan recommendations then"* (RS-21), answering the offer that the held rulings stay held unless he says to take the plan's recommendations for them. Each row is the recommendation `_part5` §J carried that day, not Jordan's choice between the options; each is **revertible alone** — the revert is that Jordan states the other option, and only that row's building position moves.

| # | item | the adopted recommendation | builds at | revert (Jordan states the other option) |
|---|---|---|---|---|
| 1 | H-111 refusal-as-news | SKIP at WITNESS, except keyed kinds a verb declares (`news.untold` stays, T4): a refused inquiry deposits nothing; no `finding.none` deposit | FI-01's deposit half, built as the skip arm (B-O); J-22 whole; R-05's inquiry rows (three graded at B-O: `research`, `examine`, `surveil`'s place case; three waiting); R-09 | refusals deposit as news |
| 2 | `13`-rest scale | scale the overlays on the NPC lane only, on the per-case observable (distinct executed sets per case against its no-overlay arm) | IN-38 (B-V) | another scale or observable |
| 3 | #457 D6 ending vocabulary | a Query over holds and seats that the season reports, never an actor. Context: Jordan's 2026-10-04 list item (3) intends a Church theocratic-takeover endpoint (event d0c5277a-795c-49e4-9640-39f3909306ab) — an endpoint, which the Query can report, not a vocabulary | IN-27 → IN-30 (B-U); M2's terminal | the other terminal |
| 4 | #457 D4 foreign cast | one foreign faction, two seats, in `references/npc_registry.yaml`. Context: foreign content is intended (the 2026-10-04 items (2) and (8)) and names no leaders | IN-36 → FA-01 content (B-V); the Schoenland trade demand has one copy, in FA-01, carried by `exchange` (IN-33, B-I) [ASSUMPTION] (G-6, [medium]: the churn engine "external trade demands by Schoenland" had no driver; revert: a `covenant` reader, B-Q) | other cast content |
| 5 | #457 D2 ageing and illness | in J-6's scope, a hazard reader only, rates swept. Context: the 2026-10-04 items (4) and (9) intend succession crises and say nothing on ageing or illness | IN-34 (B-F); its birth-tick field moves `content_hash` by schema, so "age step 0 reproduces today" is read as equal event kinds and counts or against a re-recorded hash | out of scope |
| 6 | J-18 depth stack | (A) cap support at the ranks a troop type's weapon reaches; depth's value lives in the relief terms and the refill | MB-07 (B-D2, on the pre-move paths) | the other option |
| 7 | J-20 off-hand | (B) out of scope: delete the dead branch (`COVERAGE_GAP['partial']` and the `coverage` parameters); re-add it with its first weapon | PC-07, first half (B-D1) | the other option |
| 8 | J-21 katana anchor | (A) keep the flip as a guarded asymmetry exactly as batched; `test_a_poor_edge_is_poor_everywhere` stays the guard | PC-07, second half (B-D1): nothing to build; it closes | the other option |
| 9 | #453 R-5 `inheritance` | (b) `inheritance` as a fourth conferral basis, read by CENSUS at `person.died`, dispatching to a rule table whose first rule is the designated heir, after IN-12 (#453 §10.4's "later" row). Context: Jordan's 2026-09-18 list of how an office is filled is "appointed, elected, annex", with no `inheritance`, and he deferred ("don't worry about it for now"); his 2026-10-04 item (9), "royal succession crises", needs `succeed` to have a basis | IN-51 (B-R): `succeed`'s reader, so R-5 is on R-05's critical path | (a) — under which R-05 cannot read `met` |
| 10 | J-13 `capability`'s scale and source | (iii) as the interim: `pool_default` wherever a case names no vocation; (i) fails as written. Context: `verb_capability`'s values are only `copying` (`engine/season/rosters.yaml:1039`, values `:1063-1064`), and `references/npc_registry.yaml`'s `stats:` is null on 28 of the 29 rows that carry the key (both read 2026-10-06), so an attribute→capability map would be a number nobody chose; Jordan's constraints (2026-09-06): latitude enters through the pool only ("pool only it is, but ensure you don't go so far as to deprive player of a chance at winning"), and social figures are derived ("It's a derived score that is used for the subsystem for a character, but it is not a character attribute in and of itself") | IN-12 step 9 (`train`, B-Q) writes `Person.capability` only where a case names a vocation; R-09's by-person pool stays partial until a source is ruled | a source Jordan rules |

**(c-held) STILL HELD — not ratified, not answered by this merge.** Each holds the B-Z members named beside it (`_part3` §B); a held item, once ruled, slots into the next unopened batch of its cluster by `_part3`'s membership rules.

| item | held because | holds (B-Z) |
|---|---|---|
| J-9 Godot version + the tenth attribute | nothing may assert a version (`CLAUDE.md` preamble). EVIDENCE, not an answer (event ids as the session search reported them): Jordan typed "Godot 4.6" three times — 2026-09-01 18:32:41 (tnuwsf6W, 0b52767e-7f81-4b51-a266-f2ee591111ef: "idealized code shape that must work for Godot 4.6 would function best in a holonic manner ..."), and on 2026-09-05 "Use Godot 4.6 logic to organize" (65c48d15-e058-466e-83db-f7d5f8121ec8) and a docs URL for that release (ebde5b0d-54ca-4a37-9652-9bbc48585064), with 9603989b "...we may as well do the Godot logic now" — all organising instructions, none a pin; `godot/godot_conversion_strategy_v1.md:138` carries the string in a heading. THE ONE QUESTION: does Jordan rule 4.6, which would settle the open item in `CLAUDE.md`'s preamble? The count of ten attributes is confirmed ("it will be 10 attributes", 2026-08-14 Q7, ED-IN-0185); no name from Jordan; "spirit" (resilience: R-14) is a candidate input only | GO-01 (`26`) → GO-05 → PC-05 (1); M3; `godot/godot_conversion_strategy_v1.md` |
| J-14 | overwrites a ratified ladder; unblocks nothing. Context: "systems should not need different degree bands" (2026-08-15) favours one ladder, and fail-forward (2026-09-06, 33fb9762-32c2-4a5d-bb92-6756fb8ee70c); no ruling on re-banding | — |
| SM-1 (which module owns the proceedings verbs) | two indirect leans conflict: authoring a verb "likely belongs in the main system ... flag this", and "create the correct verb for the subsystem" | SC-06 (asked at B-N) |
| CAST-POPULACE's spread construal | #457's own gate for it is "Jordan (construal)" (`proposals/2026-10-04-forcing-churn-and-the-story-bar.md:171`): how a cohort's internal spread is read; the 2026-10-06 rulings do not answer it, and the plan records no recommendation | SE-04 (c); ENP v2 proposal 13 |
| Layer 0 and Layer 1 text | Jordan's files | IN-44 (the table at the end of this file) |

B-Z also parks GO-06 (another repository) and the LEAVE rows MB-08, PC-08 and FA-03; none of them waits on a ruling.

**Left the held list — answered since the first draft, each with its tag and its revert.**
- **J-1 and J-5**: answered, Jordan 2026-10-06 (the candidate drafts, (a)).
- **#457 D1 (the Calamity's class)**: ANSWERED by ladder step 3/4, [medium] — the plan's own recommendation: the Calamity is a consequence of held configurations failing (strain as an act's cost; Mending acts hold the balance), not a matter motion, with the baseline sign that, unmanaged, it worsens outward with increasing intensity (`canon/philosophy/RULINGS.md:126-136`, D-3 "Ruled: tensile"; Jordan 2026-10-04, event d0c5277a-795c-49e4-9640-39f3909306ab, item (6)). IN-35's class gate is answered; its build waits on IN-06's build. Revert: Jordan says the ongoing expansion is ambient matter motion.
- **J-8 (`dispatch` as a remit act)**: PARTLY ANSWERED, [medium]. Jordan rejected deleting `dispatch` (2026-09-18, 03eeb811-3355-4264-bc4b-567c9ca0c1ec: "i think that's wrong") and said of the remit "for testing purposes for now, just build out a generic remit" (e07b7146-7c34-4f61-b32b-4c16dbe0a434), the origin of `remit_default`; `march` ships `eligibility: ["remit:dispatch"]` (`engine/season/verb_table.yaml:593`). So the delete arm is out, `dispatch` stays in the generic remit, IN-12 steps 5, 5a, 8 and 11 build on `remit_default`, and per-post naming is deferred by Jordan until posts are authored: it is an ask-then item below. Revert: Jordan names the posts.
- **SM-5 (a grid or map variant is a MODE of one module)**: CONFIRMED BY JORDAN'S WORDS, recorded at `proposals/2026-09-30-character-and-play-surface/05_two_modes_of_one_bout.md:8-11`: "I want there to be a grid map-based version where you choose to attack and then in fire emblem style you see the bout, but it's my personal combat engine resolving there for a round — and then a duel version where you actually decide at each step/beat". Two playable modes of one combat engine, no second resolver. J-11's residual (R-04 conjunct 3) reads "mode"; SM-6, the suspension design, is IN-46 (design, B-C), and the character-sheet management space is IN-47 (design, B-C). Neither has a build batch until its design is reviewed, so R-04 conjunct (3), hence M1, cannot read `met` until both have one.
- **H-101 (vassalage — something can be under something)**: ANSWERED by ladder step 4/5 on Jordan's typed requirements, [medium; Jordan to correct]. 2026-09-02 (aSQSVswo): "do our factions have the ability to understand the purview of larger factions? eg Lowenritter is a faction that is technically under control of King" / "the ability to be under*" (b2133a54-992d-4505-82fc-3b9bb2b703eb, d111dc52-31a9-4903-b0a8-d3b3fa897324); "same applies to nesting offices." (5959df57-b1e8-43b9-9478-34a7c26bac17); "King/Queen cannot revoke title of Duke/Duchess if they do not have duchy is in their holdings. King/Queen can revoke title of Duke/Duchess if the duchy is one of their holdings." (41eb0216-3f37-4004-877f-28dc5379d782); "This means that a Duke can revoke office from any individual in that office so long as that office is for a holding under their purview." (8980df9f-2b11-430c-bff8-901eaca46721); 2026-09-03 "Regency and puppet rulers must be possible." / "Same with delegation" (95b03164-d4a1-4216-92a6-1b52bc74f1e0, 40966503-d8a0-43b1-be74-3ad5fa55aa33). Reading: a faction can be under a larger faction and offices nest; reach is rank plus containment (the held thing must be in the superior's holdings). **The relation is DERIVED, never a stored `superior:` field** (G-4, [medium; Jordan to correct]): H-101's own row rejects a static parent (*"BOTH ARE TRACKS, NOT FACTS, WHICH IS WHY A STATIC PARENT FIELD WOULD BE WRONG AT EITHER SCALE"*, `engine/season/hole_register.yaml:1999-2010`), and Jordan's 2026-09-17/18 words fix the shape: purview reaches *"Descendants only"* (EmTzEZD5, 3e4e860e-6ece-4fd3-9f98-f116f2fea180); who is above is the *"rung above of same faction"*; *"factions can be of any scale"*. So "under" is (i) rung containment within a faction, descendants only, plus (ii) a seat-holder's own `oblige` to another seat for subordination across factions — #453 §7.2's vassalage, owned by the person who swore it — read by an added oblige-edge clause in `purview_reaches`, which never asks upward (`engine/season/state/gate.py:283-284`). IN-40 builds it in B-J on IN-10's `oblige` (formable from a held Record's terms) and IN-11; its EXIT is the Ehrenwall Split in a seeded season by an `oblige` lapsing or released, so that who has purview over whom changes, and its falsifier is purview over an office whose holding is not in the superior's holdings. Regency is IN-10's `confer` + `Tenure.term` sub-step (B-I); delegation by someone who does not hold the seat is IN-48 (B-J, design-first). Revert: Jordan prefers a stored parent.

**Ask-then** (still held, but attached to a position, so they hold no batch; asked when the position reaches them): J-15 (M-2), J-16 (`22`, asked at B-N), J-17 (a cross-bench `move`, asked at B-N), J-19 (cavalry), **SM-15 / `2-ii`** (Jordan's lean is to adopt, indirect, [medium]: the proceedings subsystem owns all social contests and the orphaned `contest/` code retires; only the TIMING, after SC-01's measurement, is held — SC-05, asked at B-N), **J-8's per-post naming** of `dispatch`'s remit (above), and the **CELL-VALUE AND COSINE PASS** — non-blocking: Jordan revises cell values (at least the `doctrine` row) against the cosine instruments (the doctrine pair, `conviction_spread`, the correlation table of `candidate_pursuit_cells.md` §5.3); it follows IN-08's landing (after B-G) and does not hold it.

**What (a) names conditionally.** Each item below is named by a document or position in (a). One is still "ratified only if"; the rest are ratified on merge as the plan's recommendation by the (c-adopted) row named.

| item (where it appears) | at this merge | by |
|---|---|---|
| FORCE-BODIES → IN-34 (#457); ENP v2 proposal 5 | ratified as the plan's recommendation, [medium; Jordan to correct] | (c-adopted) row 5 (#457 D2) |
| FORCE-FOREIGN → IN-36 (#457); #445 P-3's content (FA-01) | ratified as the plan's recommendation, [medium; Jordan to correct] | (c-adopted) row 4 (#457 D4) |
| END-VICTORY → IN-27 (#457); settlements P5 → IN-30 | ratified as the plan's recommendation, [medium; Jordan to correct] | (c-adopted) row 3 (#457 D6) |
| CAST-DISPOSITION's capability writer; #453 step 9 (IN-12) | ratified as the plan's recommendation, [medium; Jordan to correct] | (c-adopted) row 10 (J-13 (iii)) |
| #445 S-6's deposit half (FI-01) | ratified as the plan's recommendation, [medium; Jordan to correct] | (c-adopted) row 1 (H-111) |
| CAST-POPULACE → SE-04 (c) (#457); ENP v2 proposal 13 | **ratified only if** the spread construal answers so | (c-held), still held |

Also still held (RS-21's list; none holds a B-Z position except as named): **`decision_policy_v1.md`** (quarantined; DRAFT FOR RULING; ED-IN-0113's fork, whether metaphysical canon may be struck, is Jordan's and binds how rulings are made; his broad stance of 2026-09 — "Proposals don't die because of conflicts with existing work. If a proposal is better, then it must be considered." — concerns code-attached commitments and does not settle it); **`godot/godot_conversion_strategy_v1.md`** (PROPOSED, held on J-9, the one question above; GO-03 removes a version string and Key-runtime rows and ratifies nothing); **A-24 (i), "do the PR #450 deletions return?"** — v9 records the working answer NO at ladder step 5 [medium] (`FORK:` rows are the archive; a file is restored from `5c5d8ec6` only when `33`/`36` names it) and Jordan may overrule; his 2026-09-16 words "I also have repository snapshots, so nothing gets lost/broken forever if we delete/break it" (jbyp1aCT, 44320bea-40e9-4cb2-9ed8-1fb9d0485df2) fit NO but are not the 2026-10-02 ruling; **H-89** (the `Verb.scale:` column: its own row says it must not be deleted on the argument that it is inert — it is Jordan's 2026-09-02 governance/management axis ask — and a reader is a design decision; held, or routed to R-04, never cut) and **H-56's nested-DELIBERATE-in-RESOLVE half** (probe A14, `engine/season/harness/probes.py:2162-2170`, raises `Collision` with `needs="a ruling on which sentence binds"`; the rounds loop answers R-03's half only, `engine/season/requirements.yaml:507-510`); **`2026-09-03-governance-corpus-rebuild/`** (scoped to a zip not in the tree; cannot be dispositioned); and **all Layer 0/1 text** (the table below). Every `[medium]` or `[low]` verdict in the v9 adjudication (ED-IN-0286) is **revertible alone**: a content owner or a reviewer who disputes one reverts that position and nothing else in the order moves; the revert path is on the row in `_part5` §A or the lane part.
- **(c-i)** **The §A answers ratify only as which ladder step answers each question and which candidate gets
   attacked** — never as the answer, which is decided at its position with the code in front of it. An
   attack that lands sends the question back through the ladder, not to Jordan by default.
- **(c-ii)** `ED-IN-0284` and `ED-IN-0285` (`_part5` A-25) fix the STRUCTURE; they do not ratify this plan's staging. Each of these is revertible alone (the revertible-alone rule above): the order and content of `30`–`36` (IN-02..IN-07, `_part4`); `30`'s [ASSUMPTION]s (the `entry:` key; refusal (a) one-sided); `30` wiring the registrar at `SeasonDriver.__init__`; the `04` T-k reading at `31b`. A-25's [ASSUMPTION] that a grid or map variant is a mode is CONFIRMED by Jordan's own words (SM-5, above). A-24's open items and `SM-1`…`SM-15` (IN-02..IN-07, `_part4`) stay open except where this section marks them answered; SM-6 is IN-46's design (B-C).

**(d) RECORD EDITS AND LEAVES — ratify nothing.** The squad-engagement synthesis keeps its RULED status; its "unimplemented" line becomes "built: HANDOFF_MB (ED-MB-0069..0077); open: MB-01..07 (J-18 adopted as (A), MB-07)". `2026-09-04-degree-sweep/README.md` gains `INSTRUMENT HOME` (`wd_*` are R-01/R-02's `measure:`). The five flat `provisional` rows (ED-400 539 567 647 1080) and ED-914 are left as they are — frozen flat rows; adoption writes no row for them. Also left as they are: `2026-09-20-pursuit-basis-worksheet.yaml` (ED-IN-0261's ruled head), the squad concept v5, the Gather's `00`–`04`, the 2026-07-26 and 2026-08-15 documents. Ledger ids this adoption allocates, and the `next_free` bumps in `references/id_reservations.yaml`, are the adoption commit's; this plan allocates none.

**(e) LEDGER DISPOSITIONS the adoption commit writes or leaves — the summary.** The rows themselves are the commit's diff; an archived id gets its row in the archive file `tests/valoria/test_ledger_hygiene.py` requires.

| id(s) | disposition |
|---|---|
| ED-IN-0291 (new; status `ratified`, so a citation of it reads resolved) | records RS-1..RS-4 as ruled by Jordan 2026-10-06 (the drafts folded in; `faith` → `doctrine`, its row PROVISIONAL; `warden` → `stewardship`) and RS-21's ten adoptions as the plan's recommendations, each [medium; Jordan to correct] and revertible alone ((c-adopted)); `needs_jordan: false` |
| ED-IN-0261 | a superseding row (the ruled rows are not edited): the 2026-09-28 row's `needs_jordan: true`, which names C1–C4 and G-Q6, is cleared by RS-1, and G-Q5 (answered NEITHER by the same fold) is recorded with them; the fifteen-pursuit list reads `doctrine` where it read `faith` and `stewardship` where it read `warden`; its verb split narrows to `challenge` → `accept` (`kill`/`wound` are not verbs, the ED-IN-0288 row); status stays `partial` until IN-08 lands |
| ED-IN-0288 | #453 ratified as intent with §13.9's kill/wound reading ADOPTED and K-23 struck, worded as (a) |
| ED-FI-0009, ED-IN-0247, ED-MB-0041, ED-PC-0055, ED-PC-0051 | superseding rows recording (c-adopted) rows 1, 5, 6, 7 and 8 (H-111 SKIP; ageing and illness in scope; J-18 (A), with J-19 left as ask-then at MB-07; J-20 (B); J-21 (A)) as the plan's recommendation, [medium; Jordan to correct], flag cleared [UNVERIFIED here: which ledger row is each item's source is the lane parts' reading (`_part5`, `_part6`, `_part7`); each id exists, read 2026-10-06] |
| ED-IN-0287 | #457 ratified as intent as (a) says: FORCE-BODIES, FORCE-FOREIGN, END-VICTORY and CAST-DISPOSITION's capability writer as the plan's recommendations; CAST-POPULACE not ratified |
| ED-IN-0217 | `ratified` in part: ENP v2 proposals 1 and 5; proposal 13 held |
| ED-IN-0237 | `ratified` for `03` as intent, with the row's own split wording ((a)): `03_THE_SURFACE.md` stands, `04_BUILD_ORDER.md` is superseded by r2's `05` |
| ED-IN-0234 | `ratified` (intent), not `ruled`: the r2 `02` document; its flag was cleared 2026-09-17 |
| ED-FA-0021 | LEFT AS IT IS — not superseded: `ratified`, D5/D6 ruled by Jordan (ED-IN-0046/0047); `_part7`'s closed-in-lane table |
| ED-SE-0007 | superseded, heir IN-23 (CARRY-STABILITY), not `36` (`_part6` §C) |
| ED-SE-0001, 0008–0012, 0016, 0018–0020, 0022, 0024 | superseded, heir `36` (IN-07), [medium] (`_part6` §C) |
| ED-SE-0003, 0006, 0025–0030 | OPEN, left as they are: no heir in v9 (`_part6` §C.2) |
| ED-SE-0021, ED-SE-0023 | `ratified` (ED-IN-0046), left as they are, never superseded |

Read 2026-10-06: ED-FA-0021, ED-SE-0021 and ED-SE-0023 read `ratified`; ED-SE-0003, 0006, 0007 and 0025–0030 read `open`; ED-IN-0234 and ED-IN-0237 read `proposed`; ED-IN-0261's last row reads `partial`, `needs_jordan: true`; ED-IN-0286..0291 and ED-SC-0039 do not exist yet (`references/id_reservations.yaml`'s IN `next_free` is 286, SC's 39): the adoption commit allocates them and bumps IN to 292 and SC to 40.

---

## M. THE SESSION RULINGS AND DECISIONS THIS PLAN CITES (RS-1..RS-21, G-1..G-7)

**RS-n** is a ruling or finding recorded in the 2026-10-06 adoption session: Jordan's words typed in that session, or found in an earlier session by that session's search of the transcripts. **G-n** is a gap the same session decided by logic and precedent on Jordan's 2026-10-06 instruction, verbatim: *"apply all critic fixes, author fixes for all gaps without my rulings based on logical and precedent, then re-batch"*. These ids exist only in this plan and name no repo object; an event id (a UUID, or a short session tag such as `aSQSVswo`) names an event in a session transcript, not anything in the tree. **Basis:** DIRECT = Jordan's own words answer the question; indirect = his words bear on it without answering it; reading = the orchestrator's reading of the sources, [medium; Jordan to correct], whose revert is that Jordan states the other option. Each row holds only what the session's record holds; no ruling is added here.

| id | date | what (Jordan's words where recorded; otherwise the decision) | basis | carried at |
|---|---|---|---|---|
| RS-1 | 2026-10-06 | "so for candidate_\*, let's just fold them in to build unless we can find any reason why not to?" — J-1 and J-5 answered: the two `candidate_*` drafts are the source of the cells, with what they ask Jordan to accept (the sign convention, G-Q5 = NEITHER, the 55 reasoned cells, G-Q6) | DIRECT | §K (a) row 1; IN-08 |
| RS-2 | 2026-10-06 | *"you can change "faith" to "doctrine""* — the PURSUIT `faith` is `doctrine`; `faith` meaning religion is untouched | DIRECT | §K (a) row 1; IN-08 |
| RS-3 | 2026-10-06 | "that will solve it", then amended: "when we get to cell values and cosines for the axes\*poles stuff, doctrine will change" — the `doctrine` row is PROVISIONAL; the doctrine-pair margin is recorded, not gated; the CELL-VALUE AND COSINE PASS is ask-then after IN-08 | DIRECT | §K (a) row 1, (c-held) ask-then; IN-08 |
| RS-4 | 2026-10-06 | *""warden" is specific to threadwork calamity, so it's weird"*, then *"sure, stewardship works for warden"* — the PURSUIT `warden` is `stewardship` (the name was proposed to Jordan, who accepted it); the in-world Warden offices, faction, titles and fixtures are unchanged | DIRECT | §K (a) row 1; IN-08 |
| RS-5 | 2026-09-02/03, 09-20, 09-27, 10-03 | *"I ruled that kill/wound doesn't make sense as a verb choice because a character can't choose to kill or wound a other -- they can only attempt to do so. Kill/wound is the output from a duel/personal combat having been called."* (2026-09-27, ea741a6c-7194-4564-9f6c-cce425b2fa3b); 2026-09-20 *"kill and wound should not be verbs"* / *"there needs to be fight and duel"* — `kill` and `wound` are not verbs; `fight`, `challenge` and `accept` are | DIRECT | §C row 4; §K (a) #453 row; §H.3 item 5; IN-08 |
| RS-6 | as recorded at `proposals/2026-09-30-character-and-play-surface/05_two_modes_of_one_bout.md:8-11` | *"I want there to be a grid map-based version where you choose to attack and then in fire emblem style you see the bout, but it's my personal combat engine resolving there for a round — and then a duel version where you actually decide at each step/beat"* — SM-5 confirmed: two playable modes of one combat engine; SM-6 stays a design item | DIRECT | §K (c) SM-5 bullet; IN-46 |
| RS-7 | 2026-09-30; an earlier M4 answer | *"If the telling fails, ie the person is seen to be lying or not credible, then the person receiving the information may have their stance decrease towards the person who told them the telling"*; the M4 answer "March eligibility = remit:dispatch substitution" (known from a summary) — context for J-8 and for `news.untold` | indirect, [medium] | §K (c) J-8 bullet |
| RS-8 | 2026-09-18 | *"i think that's wrong"* (on deleting `dispatch`); *"for testing purposes for now, just build out a generic remit"* — J-8 partly answered: the delete arm is out, `dispatch` stays in `remit_default`, per-post naming waits until posts are authored | reading [medium; Jordan to correct]; revert: Jordan names the posts | §K (c) J-8 bullet; IN-12 steps 5, 5a, 8, 11 |
| RS-9 | 2026-09-17, 09-18, 10-04 | purview reaches *"Descendants only"*; who is above is the *"rung above of same faction"*; *"factions can be of any scale"*; an office is filled *"appointed, elected, annex"*, and *"don't worry about it for now"*; 2026-10-04 *"(9) royal succession crises"* — no stored parent is stated; `succeed` needs a basis | indirect | §K (c) H-101 bullet, (c-adopted) row 9; IN-40, IN-51 |
| RS-10 | 2026-09-17 | *"Too noisy for a character to have assailable/uncertain remits. That's just complexity for the sake of itself without any real gameplay value"* — a tension with J-3 (ii), not a contradiction: J-3 keeps [medium], and its revert gains "if a held-Record read makes a conferrer's authority uncertain or forgeable" | indirect | `_part5` §A (J-3) |
| RS-11 | 2026-09-17 | *"please ensure holonic shape for things like decision making so that they aren't directly in season loop"* — A-25 (2026-10-03, later) keeps `decision/` as host; the later governs; noted for Jordan | indirect | IN-44 table (the SM-12 row) |
| RS-12 | `canon/philosophy/RULINGS.md` D-3; 2026-10-04 | *"Ruled: tensile."*; *"(6) the Calamity in the Southernmost, if not managed, will expand and begin impacting the peninsula itself with ever increasing intensity"* — #457 D1: the Calamity is a consequence of held configurations failing, not a matter motion; unmanaged, it worsens outward | reading (ladder steps 3/4) [medium; Jordan to correct]; revert: the expansion is ambient matter motion | §K (a) #457 row, (c) D1 bullet; IN-35 |
| RS-13 | 2026-09-05 | *"well, we have to adjust whatever declaration for this. investigation is not a contest seam. it is its own thing."* — SM-3 confirmed: FI-02's second role | DIRECT | FI-02 (`_part6`) |
| RS-14 | 2026-09-06 | *"this subsystem obviously owns all social contests"*; *"orphaned social contest code: retire it"*; *"whatever works best for the subsystem is what goes, basically, so long as it can receive input and give output to seasons"* — SM-15 / `2-ii` leans to adopt, only its timing held; SM-1 stays held on two conflicting leans | indirect, [medium] | §K (c-held) SM-1 row and ask-then; SC-05, SC-06 |
| RS-15 | 2026-09-05; 2026-08-14 | *"Use Godot 4.6 logic to organize"*; *"it will be 10 attributes"* — evidence for J-9, not an answer: the one question (does Jordan rule 4.6?) stands, and the tenth attribute has no name | indirect (evidence only) | §K (c-held) J-9 row |
| RS-16 | 2026-09-06 | *"pool only it is, but ensure you don't go so far as to deprive player of a chance at winning"*; *"It's a derived score that is used for the subsystem for a character, but it is not a character attribute in and of itself"* — constraints on J-13, which RS-21 item 10 later takes | indirect | §K (c-adopted) row 10 |
| RS-17 | 2026-08-15; 2026-09-06 | *"systems should not need different degree bands"*; fail-forward — favours one ladder; J-14 stays held | indirect | §K (c-held) J-14 row |
| RS-18 | 2026-09-09 | *"C-3: it was nonsense so I had no idea that's what I apparently ruled"* — a ruling taken from a short or lettered reply carries [medium] | DIRECT (a caution) | §K (a) #453 row (the duel; K-23) |
| RS-19 | 2026-09-02, 09-03 | *"do our factions have the ability to understand the purview of larger factions? eg Lowenritter is a faction that is technically under control of King"*; *"same applies to nesting offices."*; *"Regency and puppet rulers must be possible."* / *"Same with delegation"* — H-101 answered: something can be under something; its shape is G-4's | reading (ladder steps 4/5) [medium; Jordan to correct] | §K (c) H-101 bullet; IN-40, IN-10, IN-48 |
| RS-20 | 2026-09-01..09-05 | *"idealized code shape that must work for Godot 4.6 would function best in a holonic manner ..."*; on D6 *"Leave it, file the finding"*; *"5 scenes for a character to play per season"*; *"petition spray is allowable"*; on J-P1 *"Banded degree, probably?"* / *"I don't know the consequences of j-p1"* — context; J-P1 is unruled | indirect (context) | §K (c-held) J-9 row; `_part5` (J-P1) |
| RS-21 | 2026-10-06 | *"adopt plan recommendations then"* — the ten held items in (c-adopted) take the plan's recommendations | DIRECT as to adopting; each item's content is the plan's recommendation, [medium; Jordan to correct] | §K (c-adopted); the entries each row names |
| G-1 | 2026-10-06 | `tell`'s alignment, option (a): R-06 and R-08 count only candidates whose verb has at least one celled axis; `tell` stays uncelled by design | reading [medium; Jordan to correct] | §K (a) row 1, §H.3 item 4; IN-08 |
| G-2 | 2026-10-06 | H-52: `own` stays swept as shipped; closed "assumption stands" | reading [medium; Jordan to correct] | IN-43 |
| G-3 | 2026-10-06 | `refusal_axis` (H-146) is not armed until a ruling | reading [medium; Jordan to correct] | IN-08 |
| G-4 | 2026-10-06 | IN-40 / H-101: no stored parent; derived rung containment plus an `oblige`-edge clause in `purview_reaches` | reading [medium; Jordan to correct]; revert: a stored parent | §K (c) H-101 bullet; IN-40 |
| G-5 | 2026-10-06 | IN-46 (SM-6) and IN-47 (the character-sheet management space) design-first; IN-48 (H-108's delegation half) design-first; IN-49 (`levy`, H-163 limit 3); IN-50 (the failing ARC R3 case) | reading [medium; Jordan to correct] | §K (a) #445 and #453 rows; those entries |
| G-6 | 2026-10-06 | the Schoenland trade demand gets a driver, a clause whose one copy is FA-01's content | reading [medium; Jordan to correct] | §K (c-adopted) row 4; FA-01 |
| G-7 | 2026-10-06 | every other gap the session's full-plan review found, decided the same way and carried at its entry with its tag | reading [medium; Jordan to correct] | the entries |

---

## N. NOT VERIFIED IN WRITING THIS PLAN — carried honestly (v8's list, then v9's)

- Pre-flight rows P-4 and P-6 (`_part3` §P; run by IN-39 in B-C); P-1…P-3, P-5, P-7 and P-8 were consumed in v8's Batch 1 (PR #450).
- The MB/PC `needs_jordan` rows — v9 read their heads and governing rows and cleared the flags it could; the bodies of the July MB rows (`ED-MB-0007`, `0018`–`0025`, `0028`, `0029`, `0031`, `0032`, `0040`, `0043`) were not opened. `ED-PC-0019` and `ED-PC-0021` are superseded by `ED-PC-0022` (U10, `ratified` 2026-07-23): `CHOKE_THRUST` is retired from the force channel and its cost re-homed to `CHOKE_ACCURACY_K` (`systems/combat/combat_engine_v1/weapon_physics.py:236-245`, `config.py:56-60`, read 2026-10-06), as `_part5` §A records.
- Whether any WITNESS channel predicate filters refusal kinds (H-111) — one probe; FI-01's skip arm (B-O) reads the answer before it edits `loop/witness.py`.
- `ED-916`'s full row — only its head was read (consistent with `28-0`).
- The planning pass's `[PLAN]`-class evidence for `11a`/`11b`/`13b`/`13e`/`13f`/`13d-ii`/`24d-i` and the 2026-09-30 SHAs
  — carried, not re-run.
- Line numbers: every one in this plan drifts; re-derive a site by its symbol.
- v9 (unverified, carried): MW-11/MW-5 red (SE-03); `ED-PC-0013` item 3's referent (PC-05); `tools/build_fork.py` cannot run here (IN-43); `valoria-game`'s parity reader (GO-06); `ED-IN-0214`/`ED-IN-0211` content (in `registers/archive/` only, fold-blind); H-56's closure by the rounds loop; the five flat `provisional` rows; `evacuation_plan.py`'s partition at `31a`; `capability` overlays beyond NPC-088 since `21`-rest; R-04's aperture paragraph (`march 16/16` against 11 refused at ENCOUNTER, the `both` two-Event convention — not re-run, ~25 minutes).

---

### H.3 Edits OUTSIDE this plan that its adoption needs — listed, NOT made here

The file-and-line actions are the adoption commit's own diff, written and applied only after Jordan has read §K. This section names the surfaces, not the lines. **It is B-A's whole edit set and its covering runs** (the adoption commit, after IN-01's own commit); `_part3`'s B-A row defers here.

1. `CURRENT.md`: the plan row (`:24`) and the Social contest row (`:28`), in the adoption commit. The stamp (`:15`), the retire-set wording (`:22`) and `engine/autoload` (`:41`) are Jordan's — the table at the end of this file.
2. `references/lane_assignments.yaml:29` `source:` → v9 (lineage string kept).
3. The ledger: the adoption row ED-IN-0286 and its siblings, ED-IN-0291 (the RS-1..RS-4/RS-21 row) and ED-IN-0261's superseding row (§K (e)), and the `next_free` bumps in `references/id_reservations.yaml` — allocated at adoption, never max+1.
4. `engine/season/requirements.yaml` names retired v8 files at four sites (each re-opened 2026-10-06): `:113` cites `valoria_master_workplan_v8.md` for the kernel's retirement at `2-ii` (→ `valoria_master_workplan_v9.md`, SC-05); `:322` and `:405` cite `valoria_master_workplan_v8_part4.md` §`11`, and R-02's `measure:` string at `:504` cites the same (→ `valoria_master_workplan_v9_part2.md` §11, where the command is carried verbatim). `engine/season/rosters.yaml:750` (a `source:` provenance string) names `v8_part4.md`'s plan position `8`, which landed and has no v9 handle (→ "plan position `8` (closed; `…v8_part4.md`, retired, at `FORK:<sha>`)"); `tests/valoria/test_module_registrar.py:19` (a docstring) names `v8_part5.md`'s position `30` (→ `_part4` IN-02). Re-point; `register --requirements` must still exit 0. **NOT made at adoption, and not a re-wording:** R-06 and R-08 carry no `met` text in this file; the record IN-08 owes in B-G (G-1, [medium; Jordan to correct]) is a `measured:` note on each row recording `corpus_run`'s RANKING line once that line counts only candidates whose verb has at least one celled axis (`tell` stays uncelled). Neither row's `measure:` command changes.
5. The nine lane handoffs: rows citing retired plans as owners are re-pointed or deleted; the per-row actions are the adoption commit's diff of `registers/handoffs/`. Root `HANDOFF.md` keeps every row. This plan cites handoff rows by their content (the row's own first words), never by line number, because the adoption commit deletes rows and a line number would open a different row afterwards. One standing order is AMENDED, not re-pointed: `HANDOFF_IN.md`'s order beginning *"The `kill`/`wound` slashed name is ruled wrong. The SPLIT (`kill`, `wound`, `challenge`→`accept`, added beside `fight`) rides the cells commit only"* now reads that `kill` and `wound` are not verbs (the split of `fight` into them is closed, §K (a)) and that `challenge` → `accept` alone ride the cells commit (IN-08, B-G) — still never authored standalone.
6. The proposal `## Status:` lines and retirements of §K (a) and (b).

**Covering runs for that commit:** `python tools/currency_consistency_check.py`;
`python tools/valoria_local.py --staged`; `pytest tests/valoria/test_single_status_line.py
tests/valoria/test_currency_consistency_check.py tests/valoria/test_tool_input_paths_resolve.py
tests/valoria/test_ledger_hygiene.py tests/valoria/test_forked_status.py -q`;
`python -m engine.season.harness.register --requirements`.
A shallow clone runs `git fetch --unshallow` before `test_forked_status.py` (`CLAUDE.md` §0.4). `test_single_status_line.py` walks only `.designs/systems` (`:60`, `:87`) and cannot see v9; the check over v9 is `grep -c '^## Status:' workplans/valoria_master_workplan_v9*.md` (each file reads 1).

---

### H.4 Where each retired plan's live content went (the `FORK:` ref is on each file's own row)

The right-hand column of the first nine rows names the v8 section (v8's numbering, readable at `FORK:0671283`); the last two rows map v8 and the telling workplan into v9.

| retired file | live content → where in v8 |
|---|---|
| `2026-09-28-the-plan-one-order-mc-v18-retired.md` | §0 numbering/legend → main §0.2–0.3; §2.3 state → main §3; §3.3/§3.4 → v8's Batches 2–3 (v8's Batch 1 landed: v8 §H.1); §3.5 → `_part3` O.2; §3.6 → §S; §3.7 → §G; §4 → §C; §5.1 → `_part5` §J; §5.2 → `_part5` A-1; §6 → §E; §7 → §K; §8 records → §H.1; §9 → §N |
| `…_part2.md` | §1 → §D; §2 → §L; §3's live mappings → the batch specs (H-items, `24g`/`24h`, `22a`/`22b`; `20-iv` and `15d`/`17b` DONE) |
| `2026-09-30-phase-4-post-ners-revision.md` | §1.4 (eight always-refused) → `_part2` R-05; §1.5 (the retirement's cost) → v8 `_part3` `## B1`; §2 → main §3; §3 (effect-file targets, `22`'s step-by-step state, `28-ii`'s evidence) → the batch specs; §4 → `_part5` J-4/J-16/J-17 |
| `2026-09-18-governance-settlement-behaviour-plan.md` + `_part2` | §3.0 cadence → main §0.4 (now its only home); §3.9 → `_part3` O.2/O.3; `_part2` §8 per-position text → the batch specs for `8`, `9`, `10`, `11`, `12`, `12b`–`12d`, `13`, `14`, `17`, `19b`, `21`, `22`, `23`, `24g`, `26`, `27`, `2-ii` |
| `2026-09-09-r-execution-plan.md` + `_part2` | U5 → the telling workplan (position `10` re-scoped there, main §0.6); U6's acceptance block → `11` (verbatim, slices re-derived); U7 → `14` (its group arithmetic superseded by `_part2` R-05's measured table); U8 → `17`; U10 → `21`-rest. U1–U4, U9: DONE |
| `2026-09-13-work-order.md` | units 13, 14, 19b → those positions; 13b, 15, 19, 20 DONE |
| `valoria_master_workplan_v7.md` | §0 owns-table → main §0.1; §1 M1/M2/M3 → main §1 with current readings; §3's who-can-answer sort → `_part5` §J's ranking; §4 lane sections → the lane handoffs (v7's text was stale on every lane); §5's binding rules → `CLAUDE.md` (pointer); ruling R-7 → A-14 |
| `2026-09-06-season-loop-execution-plan.md` | work item 4.5 (investigation: the loop is the mechanism) → `ED-FI-0009` |
| `2026-09-09-layer1-conformance-plan.md` + `_part2` | the live nodes → §L |
| `2026-09-05-…`, `2026-09-06-shape-…`, `2026-09-09-shape-…-v2`, `2026-09-10-unblocking-strategy`, `2026-09-11-arc-sequence-spine`, `README.md`, `return_to_game_queue.yaml`, `valoria_master_workplan_v6.md`, `workplan_v6_progress.yaml` | none live — spent, superseded, or retired by `ebb43bf0` (the progress board's last reader was m1 row 3, re-pointed to THE NINE) |
| `valoria_master_workplan_v8.md` + `_part2`…`_part6` | head §0.1–0.5 → v9 §0; §0.6 → v9 §0.6 (telling absorbed); §1–§2 → v9 §1–§2; §3 → v9 §3 (state index; dated readings are re-read by instrument, not carried); `_part2` (THE NINE) → v9 `_part2`; `_part3` → v9 `_part3`; `_part4`: `22` → SC-01, `2-ii` → SC-05, `ED-FI-0009` → FI-01, `27` → WR-01..03; `_part5`: B4 → IN-08, §SM → IN-02..IN-07, §J and A-1..A-25 → v9 `_part5`, `9` → PC-01, `26` → GO-01; `_part6` → this file (§C, §D, §L, §S, §G, §E, §K, §N); §H.1, §H.2 and §H.5 are history and are not carried — the commits are the record |
| `2026-10-01-telling-workplan.md` | T7 → IN-16; the owed measurement → IN-17; the gated tail G1–G8 with §5/§6/§10 → IN-18 (`_part4`); its As-built stays at the `FORK:` ref; ED-IN-0282's superseding row reads "absorbed; nothing re-ruled" |

---

## IN-44 — Layer 0 and Layer 1 edits owed: LISTED, NOT MADE (Jordan's)

`CLAUDE.md`, `CURRENT.md` and `HANDOFF.md` are Layer 0; `architecture/` is Layer 1. Adoption edits none of them except the two `CURRENT.md` rows named in H.3 item 1, which ride the adoption commit and take effect only on Jordan's merge. IN-44 sits in B-Z: no batch edits these files; Jordan does.

| file:line | stale | reading owed |
|---|---|---|
| `CLAUDE.md:278-281` §0.2 | `mc_v18` DEPRECATED-in-place; file deleted (`FORK:5c5d8ec6`) | retire the paragraph (the mention sweep outside Layer 0 and 1 is IN-43's, B-C) — now supported by Jordan's own words: 2026-09-16 "Remember that mc_v18 is being fully retired." (jbyp1aCT, 4ad2140c-14e1-44f4-9122-f8b912810229); 2026-09-27 "we need to move beyond any mention or use of this mc_v18. that is critical.", "ensure this will allow us to 100% retire mc_v18", and "remember that we are still using mass battle. just not having it called through mc_v18" (75793876-f884-4b2d-9586-0e85514f58f1) |
| `CLAUDE.md:407-414` §3 | `engine/` bullet names `cross_scale`, two seams; `modules/` arrives at IN-03 | re-describe per A-25 |
| `CLAUDE.md:395-447` §3 (the repository map; the `engine/season/` bullet is `:415`) | no `modules/` row | add per A-25 |
| `CLAUDE.md:527-531` §6 | "starting with `engine_clock`" | the season calendar (`loop/driver.py` + `loop/calendar.py`) |
| `CLAUDE.md:540-547` §7 | retired `balance_oracle` paragraph | keep the gap statement |
| `CLAUDE.md:155` §0.05 | `fac.intel` "reachable by nothing" | deleted at `29b` |
| `CLAUDE.md:514` | (SM-10 cite) | re-read at edit |
| `CURRENT.md:15, :22, :41` | stamp; retire-set wording, and `:22`'s "Layer-1 conformance ED-IN-0206" pointer (ED-IN-0206 becomes `superseded` → `23`, SC-02, at adoption); `engine/autoload` | re-reconcile; A-24; repoint the conformance pointer to `23`; `engine/dice_engine/` |
| `architecture/meta/04_CODE_ARCHITECTURE.md:1000`; `architecture/PLAN.md:1271`; `architecture/VOCABULARY.md:125` | (SM-10) | re-read at edit |
| `architecture/holonic_ARCHITECTURE.md:75` `[engine]` tag | collides with *engine* = season loop (SM-12) | rename |
| SM-12 / A-24's holonic item (`architecture/holonic_ARCHITECTURE.md`; `decision/` as host, A-25) | Jordan 2026-09-17 (gboNy7Ap, 6ef0472d-f017-413f-8470-5ed0e9d02d68): "please ensure holonic shape for things like decision making so that they aren't directly in season loop"; A-25 (ED-IN-0284/0285, 2026-10-03, later) keeps `decision/` as host, the AX-2 island | later governs; Jordan to note the earlier preference when he edits |
| `CLAUDE.md:727-730` §11 (the denied-primitive list); `.claude/settings.json` `permissions.deny`; `tests/valoria/test_no_polling_triggers.py` `REQUIRED_DENY` | `RemoteTrigger` is in none of the three (`git grep RemoteTrigger` finds nothing in the tree, 2026-10-06) | if `RemoteTrigger` arms, fires or re-arms a Routine, it is a self-scheduling primitive §11 forbids and joins the deny-list, `REQUIRED_DENY` and §11's list in one commit; the deny-list is configuration, so the edit is Jordan's [UNVERIFIED: what `RemoteTrigger` does in the current tool surface was not observed here] |

`CURRENT.md:41`'s pointer repair is the same class as #448's and may ride adoption at Jordan's word.
