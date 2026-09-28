# THE PLAN — part 2: every `mc_v18` spine file, role and importer; the Layer-1 mapping; where every absorbed item went

## Status: ADOPTED 2026-09-28 (`ED-IN-0280`) with the file this reads after, on the same instruction and with the same held-back list — see its `## Status:` line and its §7. **This part carries no Jordan decision of its own**: where a disposition waits on one, it names the item number in the main file's §5.1.
## Reads after `workplans/2026-09-28-the-plan-one-order-mc-v18-retired.md`. That file owns the ORDER, the supersession verdict and the Jordan roster; this one owns the disposition detail behind Phase 4 and the mapping tables. For a position the 2026-09-18 plan already carried, the per-position INSTRUCTION / WHERE / FALSIFIER / GATE stay in `workplans/2026-09-18-governance-settlement-behaviour-plan_part2.md` §8, which is not superseded.
## Owner: infrastructure / cross-cutting (IN lane)
## Grade under CLAUDE.md §0.2: `paper` throughout. Every citation is as a read-only Fable 5.1 pass read it at HEAD `6f6ef84` over `ecacb57`'s code; line numbers drift, so re-derive by symbol.

**The disposition key**, used throughout §1:

| key | meaning |
|---|---|
| **(a)** | a season-native replacement EXISTS, and it is named |
| **(b)** | a replacement must be BUILT; it is named and given a position |
| **(c)** | dead or orphaned — delete it with a `FORK:` row, and the justification is given |

**Position handles** (`28-iii`, `29b`, …) are the main file's §2.3 rows. **Section cross-references**
run both ways; §4 is the index.

---

## 1. STEP B — every spine file, every composition role, every retire-set tree, every importer

**What "supersede all calls for `mc_v18`" means here, measured.** The spine is `engine/mc_v18.py`
plus what it drives:

- `engine/autoload/{game_state, engine_clock, season_manager, scene_slate, victory, npc_ai}.py`;
- `engine/cross_scale/*`;
- `systems/overview/sim/{season, accounting, ci_track, ms_track, ip_track, rs_track}.py`;
- the 26 composition roles that are not `mass_battle.resolve_field`.

Its callers are **12 production files** (4 of them the spine itself) and **17 test/tool files**, by
an `ast` walk re-run by the author (main §1). Every one has a row below.

### 1.1 The engine spine

| file | consumers at HEAD | disposition | position |
|---|---|---|---|
| `engine/mc_v18.py` | the six `ALLOWED_IMPORTERS` | **(a)** `engine/season/loop/driver.py::SeasonDriver.season`. Jordan's 2026-09-13 *"just deprecate it and archive it"* (`test_mc_v18_is_deprecated.py:5-6`) is satisfied by deletion with a `FORK:` row: `CLAUDE.md` §1 allows no `deprecated/` tree, so the fork ledger IS the archive. His 2026-09-28 instruction supersedes it on timing (§0 test 1). The OI-05/OI-07 stubwire deferrals die with it: OI-05 is implemented in the head per `ED-WR-0011` (`mc_v18.py:7-8`), and OI-07 → the `knots` Tenure kind | `28-iii` |
| `engine/autoload/game_state.py` | 8 `systems/` + 4 spine + 9 tests + `balance_oracle` | **The hub; it is taken apart class by class.** `Faction` (the L/Sta/W/I/Mil/accord/pt stat vector, `adjust`) → **(a)** `faction_q.resolve` for `(proposition, members, holdings, seats)`, per `04 §B.6.1:286-292` (five members at `20-ii`). **The stat vector has no season replacement, and by architecture needs none**: `04:292` says NEVER *"a field of its own"*; `04:334` says *"a seat adds no verb and no modifier"*; and `requirements.yaml:82` says *"Layer 1 PART D rows 1/8/14 forbid porting `game_state.Faction` as-is"* → **(c)**. `Territory` → **(a)** `Rung` + `hold` Tenures + `dwelling`/garrison Sites. `World` → **(a)** `state/world.py`. `create_world` → **(a)** `harness/populated.py::build_realm`. `serialize_world`/`restore_world` → **(c)**: the season's identity is `content_hash`, and save/replay is `module_contracts.yaml:1308` `save_replay_premise` (Godot, position `26`). `MULTS/ACCORD_MAP/PT_MAP` → **(c)**, with `Faction`. `canonical_pt/accord` and `ALL_PLAYABLE_15/STARTING_*` are re-exports of the SUBSTRATE (`engine/substrate/{canon_buckets,world_initial_state}.py`), which stays | `serialize/restore_world` at `28-iii`; the module at `29b` |
| `engine/autoload/engine_clock.py` | `season.py:37`, tests | **(a)** `loop/driver.py` (seven steps, four barriers, `04 §C.1`). `ED-1051`'s "engine_clock ratification" clause already closed in the 2026-09-18 plan's §2.1 (test 1) | `28-iii` |
| `engine/autoload/season_manager.py` | `engine_clock:43`, `season.py:38` | **(a)** `loop/calendar.py` + `Date` | `28-iii` |
| `engine/autoload/scene_slate.py` | `mc_v18`, `scene_dispatch:66`, tests | **(a)** `loop/deliberate.py` + `pack_scenes` + `Scene` (`04 §B.9`) | `28-iii` |
| `engine/autoload/victory.py` | `mc_v18`, `test_world_population` | **(c)** delete. **The REQUIREMENT (GD-1, sole victory) does not die with it.** Register an `ABSENT_RULE` hole: *"no season-side ending/victory condition; `ENDINGS_CLASSIFIED.yaml` + `forced_by_threshold` are the ending vocabulary; `20-ii`'s observable '≥1 faction-scale ARC ends' is its precondition"*. It is not a build item here: it is unruled, and `systems/victory/` holds zero `.py` | `28-iii` (+ the hole, main §8.2) |
| `engine/autoload/npc_ai.py` | NONE | **(c)** already orphaned. Its season counterpart is **(a)** `engine/season/decision/` | `28-0` |
| `engine/cross_scale/scene_dispatch.py` | `mc_v18:66,152`, tests | **(a)** `seam/contest.py` + `manifest/` + the prize rows (`04 §C.5`), for contest and combat. The fieldwork/investigation branches were stub-wired to entirely-stubbed modules → **(c)** (their removal is `28-0`'s). `test_pipeline_reach.py` (OI-56, the OLD pipeline's P1 oracle) → `FORK:`; its season successor is `register --requirements` (R-04) + `corpus_run`'s `unrepresentable scales:` | `28-iii` |
| `engine/cross_scale/combat_bridge.py` | `scene_dispatch:235` (lazy), `test_combat_bridge_seam` | **(a)** `seam/wrappers/combat.py` → `substrate/pc_engine.py` (the one PATH seam) | `28-iii` |
| `engine/cross_scale/handoff_rules.py` | `scene_dispatch:159-165` — constants only; *"8 §3 rules built, ZERO callers"* (`module_contracts.yaml:1290-1295`) | **(c)** delete. The eight `scale_transitions_v30.md §3` handoff rules are R-04's content (`requirements.yaml:55-58`, *"the loop implements none of them"*) and are already on R-04, so there is no new row | `28-iii` |
| `engine/cross_scale/zoom_in_out.py` | `scene_dispatch:88,98` | **(c)** delete. The Hybrid-mode zoom is R-03/R-04's content (`requirements.yaml:38-41`); ENCOUNTER (M4) is the first in-season zoom | `28-iii` |
| `engine/cross_scale/domain_echo.py` | NONE | **(c)** already orphaned. Scene → Faction echo is WITNESS fan-out + `faction_q` on the season side; the §3 handoff rule stays on R-04 | `28-0` |
| `systems/overview/sim/season.py` | the `season_driver` role ← `mc_v18` | **(a)** `loop/driver.py`. The module goes with its role row, because `--check` imports every target | `28-iii` |
| `systems/overview/sim/accounting.py` | the `accounting` role ← `engine_clock:80`; tests | **(a)** MATTER (wear, subsistence) + CENSUS. The Accord / CI / MS / PT / insurgency CLOCKS have no season analogue, and by architecture none is wanted (`loop/census.py:33`: *"NO CLOCK GENERATES ANYTHING"*; ED-WR-0011 option A; `21` PART E: *"a clock nobody wound"*) → **(c)** | role `28-iii`; module `29a` |
| `systems/overview/sim/{ci_track,ms_track}.py` | `accounting`; `excommunication:166`; **threadwork** (`ms_track`) | **(c)**. `ms_track` is gated on `27` | `29a` |
| `systems/overview/sim/{ip_track,rs_track}.py` | NONE / an orphan role | **(c)** | `28-0` |

### 1.2 The 27 composition roles

`references/module_contracts.yaml:71-207`, loaded with PyYAML: **27 keys**, not 16 or 17 (main §1).

| role(s) | consumer | disposition | position |
|---|---|---|---|
| `mass_battle.resolve_field` | `seam/wrappers/mass_battle.py:80` | **the one survivor** — **(a)** | — |
| `faction_action`, `season_driver` | `mc_v18` | **(a)** the driver + `march` / `via`-seat acts. The rows delete at `28-iii`; the `faction_action.py` module goes at `29b` | `28-iii` / `29b` |
| `accounting` | `engine_clock` | **(c)** | row `28-iii`; module `29a` |
| `world_gen_settlements` | `game_state.create_world:351` | **(a)** `build_realm` (37 settlements, 211 hearths + dwellings + garrisons) | row `29b` |
| `snapshot_state.{practitioners, insurgencies, npcs, treaties, convictions, beliefs, knots, territory_infrastructure, threadcut_beings, settlements}` ×10 | `game_state.restore_world:458-510` (its only caller is `test_world_population.py:78-82`) | **(c)**. Delete the rows at `28-iii`, with `restore_world`. The two threadwork targets' MODULES stay (`27`). The `knots` module stays until `29f`. The `beliefs` module is orphaned: the season deleted `Person.beliefs` in PR #430, by design | `28-iii` |
| `scene_builder.contest`, `scene_resolver.contest`, `contest_side.a/.b` | `scene_dispatch:288-339` | The rows go at `28-iii`, and the kernel at `2-ii`. It is **(a)** for the RESOLUTION line (`sigma.py` reproduces `resolver.py:302`) and **(b)** for the veto (`degree_extension.py` → a forwarded `extension=` at `ladder.py:164`, unreachable until `22`'s provider) | `28-iii` / `2-ii` |
| `scene_resolver.fieldwork/investigation` | `scene_dispatch:354-356` (a stub branch) | **(c)**. The targets are entirely stubbed (ARMATURE §3.6, *"confirmed by function list"*). The investigation scale's season item is `ED-FI-0009` (after `13`) | `28-0` |
| `parliamentary_vote/motion/vote_declaration` | `parliamentary_transfer.py:263-270` — which is itself production-orphaned | **(c)** at `29b` — see main §1, row 3. The `tribunal`/`parliamentary` mechanics have no season port licensed: `04:302` says *"it has no verbs"*, and faction acts are person acts `via` seats (G3). Their VERB content is `19` (`levy` / `open_case` / `determine` / `issue`) + `march` | `29b` |
| `rs_track_delta`, `territory_transfer_candidate/proposal` | NOBODY | **(c)**. *"Kept named"* (`module_contracts.yaml:202`) was a convenience with no reader: `ID-13` | `28-0` |

**The tally:** 1 survivor, 20 spine-only, 3 orphaned, 3 `parliamentary_*`. Main §6's end-state is the
consequence: one row left.

### 1.3 The retire-set trees not covered above

`requirements.yaml:65-115` lists the scales. Each tree retires only when the position that expresses
its scale has landed (`requirements.yaml:27-31`).

| tree | scale | season expression (gate) | notes | Step-B position |
|---|---|---|---|---|
| `systems/factions/sim/` (18 `.py`; six stubs go at `28-0`) | grand strategy politics | **`20-ii`** | `faction_action.py:393-394` lazily imports `massbattle.resolve_mass_battle` + `terrain` — the last caller of the OLD mass-battle entry. **`resolve_mass_battle` / `_faction_to_unit` / `_morale_start_from_stability` (`massbattle.py:120-260,376+`) read `game_state.Faction.{Mil,Sta,name}` duck-typed, and die with it.** `20-iv` therefore carries d.1 to `resolve_field`, and `test_mass_battle_d1_morale_baseline.py` (which constructs a `game_state.Faction`) is re-pinned there | `29b` |
| `systems/settlements/sim/` (8 `.py`) | settlement management | **`24e` + `24d-ii`** (dwelling ✓, found/build, capacity) | `registry.py` **(a)** `build_realm`. `infrastructure.py` **(a)** `Site.condition` / `fortification_of`. `temperaments.py` **(a)** position `10`'s stance. `adjacency.py` **(c)**: the season has no province graph (`move` re-homes by `contain`; H-149 restricts `march` targets) — record that, do not invent a graph. `ledger.py` / `settlement.py` **(c)**. **The YAML stays** | `29c` |
| `systems/world/sim/` (6 `.py`; two stubs go at `28-0`) | grand strategy / settlement | **`20-ii` + `10`** (`24h` recommended first) | `npe.py` **(a)** `decision/` + stance. `insurgency_pipeline.py` → `24h`'s P5 revolt Query (the successor design is LIVE, per the-gather `02_SETTLEMENTS.md:20`) | `29d` |
| `systems/characters/sim/` (three modules; `companion` goes at `28-0`) | character creation, development, chronicling | **the cells commit + `12`** (+ `14` for `conviction` ← `knots`) | `beliefs.py` **(c)** by design (PR #430). `conviction.py` **(a)** `Person.pursuits` / the scar counts (H3) | `29e` |
| `systems/fieldwork/sim/` (three modules; two stubs go at `28-0`) | investigations | **`14`** (`tie / knot`) + `27` | `knots.py` is **(a)-partial**: the `knot` Tenure kind and the `firsthand_via_knot` channel exist; ED-912's gauge → `Tenure.degree` (F.4), recorded on `14` | `29f` |
| `systems/threadwork/sim/` (7 modules) | — | **RETAINED by ruling** (`ED-WR-0010`; position `27`) | **NOT in Step B.** Only its two snapshot roles delete. The `rendering.py` stubs ride `27` | — |
| `systems/social_contest/sim/` (20 `.py`) | social contests | **`2-i` now; `2-ii` at `22`** | The whole tree goes by `2-ii`. `rosters.yaml`'s prize rows keep the logical name and repoint at `22` | `2-i` / `2-ii` |
| `systems/mass_battle/`, `systems/combat/` | retained | — | Untouched, except `massbattle.py`'s old entry (above) | — |

### 1.4 The 17 test/tool importers of the spine (AST), plus the six `ALLOWED_IMPORTERS`

| file | tests | disposition | position |
|---|---|---|---|
| `engine/tests/test_mc_v18_regression.py` | 5 | successor (1) at `28-ii`, then `FORK:` | `28-ii` → `28-iii` |
| `engine/tests/test_f7_smoke_oracle.py` | 6 | successor (2) at `28-ii`, then `FORK:` | `28-ii` → `28-iii` |
| `engine/tests/test_combat_bridge_seam.py` | 7 | `FORK:`; **no successor needed** (main §3.4 c) | `28-iii` |
| `engine/tests/test_pipeline_reach.py` | 7 | `FORK:` | `28-iii` |
| `engine/tests/test_world_population.py` | 6 | `FORK:` — its OI-05/OI-07 falsifiers; both subjects moved to the head | `28-iii` |
| `tests/valoria/test_engine_clock_phases.py` | 5 | `FORK:` (precedent: `ED-IN-0232` already halved it) | `28-iii` |
| `engine/tests/test_accounting_accord_drift_probe.py` | 6 | `FORK:` | `29a` |
| `engine/tests/test_parliamentary_action.py` | 14 | `FORK:` | `29b` |
| `tests/valoria/test_faction_write_sweep.py` | 6 | `FORK:`; `ED-FA-0038` closes (test 2) | `29b` |
| `tests/valoria/test_faction_stat_bounds.py` | 7 | `FORK:`; `ED-IN-0029`'s floors close (test 2) | `29b` |
| `tests/valoria/test_mass_seizure_accord_write.py` | 4 | `FORK:` | `29b` |
| `tests/valoria/test_mass_battle_d1_morale_baseline.py` | 6 | **re-pin**, against `resolve_field` | `20-iv` |
| `tests/valoria/test_descriptors_runtime.py:105` / `test_world_initial_state.py:84,253` | 1 each | delete those tests; the `descriptor_registry` faction block goes with them | `29b` |
| `tools/balance_oracle.py` (+ `test_balance_oracle_arms.py`, 4) | — | **port** to `engine/season/harness/arms.py` | `28-i` |
| `tools/campaign_output_probe.py`, `tools/trace_execution_phases.py` | — | **retire** (+ the execution-map cluster) | `28-i` |

**Not importers, but they exercise retire-set code:**

| file | disposition | position |
|---|---|---|
| `test_knots_ed912.py` | `FORK:` | `29f` |
| `test_thread_mending_ed871.py` | stays | `27` |
| `test_settlement_temperament_drift.py` | `FORK:` | `29c` |
| `test_faction_obstacle_conventions.py` | `FORK:` | `29b` |
| `test_conviction_roster_single_owner.py:52-55` | re-point | `29d` / `29e` |
| `test_contest_kernel.py` | retires | `2-ii` |
| `test_sigma_leverage_parity.py` | substrate — **stays**; it moves out of `engine/tests` when the `sim-regression` job folds | `28-iii` |

**The six `ALLOWED_IMPORTERS`** (`tests/valoria/test_mc_v18_is_deprecated.py:49+`) are three
`engine/tests` files (`28-ii` → `28-iii`) and three `tools/` files (`28-i`). The set reaches `set()` —
the intermediate, falsifiable state — before the file and `mc_v18.py` are deleted together at `28-iii`.

---

## 2. LAYER-1 CONFORMANCE — every open ARMATURE §2.3 node, through the five-step test

Each node gets a verdict on the `CLAUDE.md` §0 ladder (1 superseded · 2 irrelevant · 3 answered by a
design document · 4 answered by precedent · 5 answered by what makes sense for the architecture), or
**survives**, in which case it gets a destination.

| node | test | verdict | destination |
|---|---|---|---|
| **Invariant #4, the per-conjunct half** (a keyed `emits_on_refusal`) | **survives** — open, and load-bearing on R-05: 3 live verbs have 2 conjuncts, and `19` adds more | **ride-along on `19`**. The schema is `23`'s invariant work, brought forward to its first consumer | main §3.2 row 14 |
| **The AX-4 setter scan** (25 false positives) | 5 — the PROPERTY is MECHANICAL via `World.write` + tokens (G2/G4), which makes the scan a CONVENTION duplicate. **But the property has one live violation: `World.remove_person`** (MOD 7, H-152) | close the scan; **build `GATE-REMOVE-PERSON`** | main §3.1 item 7 |
| **Typed ids / the AX-3 split** (S3/S4) | 4 — already position `23`, with the explicit *"no CI type-checker, runtime grade is real"* note (old `_part2:1519-1521`). Verified: `valoria-ci.yml` runs no mypy or pyright | stays at `23`; no new item | main §3.4 m |
| **`PersonInterior` + the two cache indexes** | 5 — recorded false N-lines (PR #430) | **CLOSED** | — |
| **The `openers:` roster hand-copy** | **survives** — every Phase-2 effect risks it | **`OPENERS-DERIVE`** (Phase 1) | main §3.1 item 6 |
| **The seam-import detector's one-hop falsifier** | **survives**, and is cheap | ride-along on **`2-i`** | main §3.1 item 3 |
| **`faction_q` against `04 §A.2:132`** | 5 — recorded in `faction_q.py:4-26` | edit `04` at **`20-ii`** (contradiction 9) | main §3.4 a |
| **H-137, the `write()` calling convention** | 4 — `7a`'s row already prescribes the convention (`Change(...)`, never eager) | CONVENTION grade, enforced by the cadence's `/code-review` on each effect. Upgrade it only if a Phase-2 effect trips it | main §3.2 |
| **F.20b — three body-literal Event kinds** (invariant 7) | **survives** — *"the loop as built cannot run under the loader as specified"* (`04:1103`) | **`23`**, with invariant 4 widened | main §3.4 m |
| **Invariant 2 — nine producerless matrix rows** | 3 — each row is some position's content: F.20 → `24e`; F.20a → `12`/`10`; `(Date, fired)` → `11b` | no item; enforceable at `23` once the producers exist | — |
| **`march`'s `requires_typed` does not narrow** (H-149) | 5 — a recorded placement choice | **CLOSED** | — |
| **The `03` / `holonic` step counts** | 3 — pointer notes cover them | **CLOSED** | — |
| **MOD 1 — three routes into `systems/`** | closes by sequence: after `2-ii` and `28-iii` there are exactly two (the PATH seam for combat; one composition role for mass battle), because proceedings is engine code | `/layer-conformance` Lens B on `04:679-684` at `28-iii` | main §3.6 |
| **MOD 4 — `npe` / `conviction` read `CONVICTIONS`** | closes at `29d`/`29e`, and shrinks the cells commit's audit item | — | main §3.4 h, j |
| **MOD 5 — `populated` reads `titles`** | 3 — `04 §B.7:308`, *"no `Title` type"*; `04 §E.1:1067`, *"`titles.domains` … world-generation content read at step 9"*. So titles is world-gen DATA, and r2 `05` says it *"folds into `offices.yaml`"* | **`13d-i` item (5)** — not Jordan | main §3.1 item 8a |
| **MOD 8 — the balance instrument on the spine** | — | `28-i` | main §3.1 item 4 |
| **MOD 10 — the degree-sweep's dead import** | recorded | no item | — |

**Where `/layer-conformance` must be READ, not just passed**, is main §3.6. It runs at every CLOSE
already; the table there names the positions where Lens B has new subject matter.

---

## 3. THE MAPPING — every absorbed item to its new handle

**Read this before citing an item from an absorbed document.** The handles are PROPOSALS for the
builder; none allocates a ledger id. The same discipline as the 2026-09-18 plan's §3.4 applies: that
plan's two numbering schemes collided three times (item 5 ≡ position 15, item 15 → position 6,
item 6 ≡ position 16). This table exists so the retirement plan's M/G/S numbers, the decision-layer
plan's H numbers and the narrative numbers cannot collide with position numbers in the same way.

| absorbed item | handle | note |
|---|---|---|
| retirement plan **M5** | **`28-i`** | port / retire the tools (Phase 1) |
| **M6** | **`28-ii`** | successor goldens |
| the `mc_v18` + engine-spine deletion (M6's terminal clause) | **`28-iii`** | after `28-ii` |
| **Step B**, per tree | **`29a`** overview · **`29b`** factions (+ `game_state.py`, its last importers) · **`29c`** settlements (`.py` only) · **`29d`** world · **`29e`** characters · **`29f`** fieldwork/knots | each with its own scale gate (§1.3) |
| already-orphaned spine and retire-set code (`npc_ai`, `domain_echo`, `rs_track`/`ip_track`, the three orphan roles, six FA stubs, two FI stubs, two WR stubs, `companion.py`; `beliefs.py` after `28-iii`) | **`28-0`** | gate-free, Phase 1 |
| ADJACENT **G2** — economic pressure | **`17b`** | + `Tenure.term` (= `21` PHASE 4 step 22, work-order item 6, narrative #4) |
| ADJACENT **G3** — demand / delivery | **`19d`** | after `15c`; beside `24f` |
| **S2** — the hearth-capacity remainder | **`24d-ii`** (existing) | rides `19c` |
| **S3** — works and founding | **`24e`** (existing) | = narrative #9 |
| **S4** — the bodies clock + individuation | **`24g`** | = narrative #5 = `24` P2/P3 |
| **S5** — revolt (P5) / forswearing (P6) | **`24h`** | after `20-ii`. P7, dispensation-as-document → **JORDAN** (overturn the written refusal; main §5.1 item 11) |
| **D1-a** — the information cluster (narrative #14, §F) | **`20-iii`** | after `15` + 20-i ✓ |
| **D1-b #1** — the chronicle render | after **`21`** | U6/U10's `causes[]` printer IS its proof of concept. Unpositioned; no R-row |
| narrative **#2** — the patron as a person | **`13`** (a `cast:` entry) + **`17`** | |
| narrative **#3** — embezzlement "already runs" | observable at **`17b`** | |
| narrative **#6** — complication as the modal outcome | **JORDAN** (re-bands the ONE ladder; main §5.1 item 12) | non-blocking |
| narrative **#7** — intelligence before action | **`20-iii`** + `ED-FI-0009` | |
| narrative **#10** — casus belli as a Record | **`15`** (`record_kinds`), then **`20-ii`** / H-151 | |
| narrative **#11** — the writ | after **`16`** | *"there is no player"* (v7 §8.5) |
| narrative **#12** — telling renews belief | **`15b`** (existing) | |
| narrative **#13** — the populace as a weighted person | **`24f`**'s missing cohort producer — **it IS that item** | Phase 1 item 10 names it |
| **D2** — `offices_draft.yaml` (570 rows) | **`13d-i` item (5)** | verify against canon first |
| **C1 / C2 / C3 / C4** | **JORDAN** — the 2026-09-18 plan's §5 item 11 (+ C3/C4 as its siblings) | main §5.1 items 1–4; `ED-IN-0261`'s new row |
| **H6 + H8** — the landing commit | **`12b`/`12c`/`12d`**'s one R6-atomic commit (+ the verb split) | main §3.3 row 5 |
| **H3** — scar counts (pursuits track) | **`12`** (the scar rebuild) | after H6 |
| **H7** — the faith-pair falsifier | **`12c`**'s falsifier | needs C2's placement |
| **H9** — crisis threshold 2 | **`12`**'s remainder | after H3 |
| **H10** — affiliation plumbing | **`12b`** (carrier, `incompatible`, `confliction`) | after C3 |
| **H11** — conviction-track scars | **`12`** | after H3, H10, C4 |
| **H12** precedence / **H13** threshold 3 + threshold 1 | **`12e`** (held) | H12's gate is a measurement, not Jordan (main §5.2); H13 waits on G-Q6 |
| — (there is no **H4** or **H5**; the decision-layer plan's `:324` says so) | — | do not look for them |
| MB: A5, A9, the dead primitives (`ED-MB-0057`), the gauge fix (`ED-MB-0044`), the config comment | MB hand pass, Phase 1 | not positions — the plan's *"parked, with reasons"* convention |
| MB Sequenced rows now unblocked: headless duels (the provider exists); the generated map (A1 done); AI generals (A1–A4 done) | MB lane, Phase 1 onward | |
| MB per-cell Q; army-scale envelopment (the multiunit Phase 0 spike) | MB lane, unchanged gates | |
| MB "strategic outputs" | **`20-ii`** + `28-ii` | `ED-IN-0279` (b) already rules that a loss writes casualties only. Discipline (PP-712) is the persistence owner, and "familiarity" is dropped (§0 test 4) |
| Part D's C2/C3 coupling (`ED-MB-0075`) | MB lane, after its superseding row | demoted (main §5.2) |
| d.1 + terrain/garrison ON THE SEASON PATH (H-150) | **`20-iv`** (MB/IN) | after `20-ii`'s `scale_of_rung` |
| SC PHASE 1 step 1 — the record-moving route | **`16`** (H-84) | |
| SC step 4 (a)/(b) — the `told_by` precedence walk + source map | **`15d`** (new; WITNESS-side, after `15b`) | R-07 rests on it; no position had it |
| SC step 5 — the ledger-cap 3×3 | rides **`11`** / **`21`** | moot while the cap evicts nothing (`21:553`) |
| SC PHASE 2 steps 6, 7, 9, 10 + the 28 stress tests | **`18`** (existing) | D-6/D-7 as swept fixtures (the `H-128` shape; §0 test 5) |
| SC steps 11–16 | **`22`** (existing) | |
| SC PHASE 3 (steps 17–21) | **`22a`** | after `22` + `15d` |
| SC PHASE 4 (steps 23–27; step 22 = `Tenure.term` at `17b`) | **`22b`** | |
| RET-SC | **`2-i`** (the stub + its export ripple, now) / **`2-ii`** (the kernel + the veto relocation + `parliamentary_*`, at `22`) | |
| the Layer-1 items that survive §0 (§2) | ride-alongs on `19`, `23`, `2-i`, `20-ii` + two Phase-1 steps (`OPENERS-DERIVE`, `GATE-REMOVE-PERSON`) | |
| FA: the `score/2` three-site disagreement; `ED-FA-0002`/`0003`/`0008`/`0021`; the round-2 dockets | CLOSE-PASS (test 2 at `29b`) | |
| SE: `ED-SE-0001`, `0007`–`0012`, `0016`, `0018`–`0024`; the card decks; D6 (G606) | CLOSE-PASS (test 1/2) | `ED-SE-0052`/`0053` ride `24d`/`24e`. (`ED-SE-0054` accepted P1/P3/P4 for build; the prose ratification is reference under §0.05) |
| FI: `ED-FI-0009` — the degree producer | after **`13`** | the cast gives `capability` its world-gen value (F.6, *"world-gen writes it once"*); today it is zeroed on every corpus person. `ED-FI-0002` and `ED-914` are unchanged |
| PC: the `partisan` deletion; Ob-from-defender | PC lane, Phase 1 | both ruled, ungated |
| `HANDOFF_IN.md`'s AX-7 wiring (`agreement` / `standing_of` / `belief_contradicts` into the Claim producers) | proposed home **`10`** | verify RR-P's text first: `Person.beliefs` is deleted, so the third may be moot. It had no row in the old §3.2 |
| `HANDOFF_IN.md`'s reverted item 4 (`budget()` counting `granted_acts`; the `test_n3` floors) | **`11`** | re-pin declared per `CLAUDE.md` §7, unless U6 shows the floor is an R-01/R-02 property (§0 test 5; not Jordan) |

---

## 4. CROSS-REFERENCE INDEX — either direction

**From a position to its detail.**

| position | the ORDER (main) | the detail |
|---|---|---|
| `1` · `2-i` · `13` · `13d-i` (5) · `18` · `24f` (design) · `25` | §3.1 | old `_part2` §8 (the same number) |
| `28-0` · `28-i` · `FIGHT-RENAME` · `OPENERS-DERIVE` · `GATE-REMOVE-PERSON` | §3.1 | main §3.1 items 2, 4, 5, 6, 7; this file §1 and §2 |
| `11a` · `11b` · `15` · `16` · `15c` · `15b` · `7a` · `17a` · `18a` · `★` · `19` · `19b` · `24e` · `19c` · `24d-ii` · `24f` (build) | §3.2 | old `_part2` §8 |
| `15d` · `17b` · `19d` · `20-iii` | §3.2 | main §3.2 (and contradiction 1 for `17b`); this file §3 |
| `10` · `11` · `8` · `9` · `12`–`12d` · `14` · `17` · `27` | §3.3 | old `_part2` §8 |
| `12e`; H3, H6–H13 | §3.3 | the decision-layer plan §3.3; this file §3 |
| `20-ii` · `21` · `22` · `23` · `26` | §3.4 | old `_part2` §8 (positions 20–23, 26) |
| `20-iv` · `22a` · `22b` · `24g` · `24h` | §3.4 | main §3.4; this file §3 |
| `28-ii` · `28-iii` · `29a`–`29f` · `2-ii` | §3.4 | this file §1 (every file, role, tree, importer); old `_part2` position 2 for `2-ii`'s kernel detail |

**From a row here to the position that acts on it.** Every row in §1 carries its position in the last
column. Every row in §2 carries its destination. Every row in §3 carries its handle. A row with no
position is either the survivor (`mass_battle.resolve_field`), retained by ruling (threadwork), or
closed (marked **CLOSED**).
