# 07 · TOP-DOWN / BOTTOM-UP — a structural reading of the whole Valoria system

> # ⚠ OUT OF SCOPE — PARKED 2026-09-04. READ THIS BEFORE THE DOCUMENT.
>
> **This reading covers the repository's fifteen subsystems. Jordan did not commission that.** His
> brief asked for *"top-down for all systems as well as bottom-up for each system"* meaning **the
> social contest system's own systems** — agôn, the three unbuilt branches, and the kernel's component
> modules. The orchestrator read one plural in isolation and expanded it to the whole tree.
>
> **The correctly-scoped reading is `10_SC_STRUCTURAL_READING.md`.** Its findings about other
> subsystems are parked in `OUT_OF_SCOPE.md` — real, anchored, and **not prescribed**.
>
> This file is kept as the record of what was actually read, and because its coverage table and its
> stated gaps are honest. **Only its `social_contest` section is inside the commissioned scope, and
> that section is superseded.** Do not rank anything here against the social-contest work.

## Status: **READ-ONLY AUDIT, 2026-09-04. PROPOSED. HELD BACK IN FULL. Nothing here runs; nothing ratifies on merge.**
## Produced by Fable 5.1 under `CLAUDE.md` §10's audit/guardrail row. Branch `claude/social-contest-system-review-dn2y5d`, HEAD `7a23b831`. **This file is the only thing created or edited.** No `pytest` was run; the only executed code was `python3 -c` arithmetic over `key_types.json`, `canon_buckets.canonical_accord`, and file listings.
## Scope: `systems/` (15 subsystems), `engine/`, the registries in `references/`, and — by Jordan's direction — this session's five proposals (`00`–`05`) against PR #362's shape (`proposals/2026-09-03-meta-architecture/04_CODE_ARCHITECTURE.md`, PROPOSED, HELD BACK IN FULL).

---

## §0 · Status, reading log, method, coverage

### §0.1 Method

Two passes, in the order the task names them. **Pass A** read the engine and the registries first, then swept the whole of `systems/` for the same seven questions at once (shape, unity, duplication, logic, primitives, writes, Keys) with greps whose scope was the entire tree, so a finding about one subsystem is measured against every other. **Pass B** then re-entered each subsystem from its leaf modules — `_store()` routers, constants, dice calls — and composed upward to what it actually emits into the campaign. §3 records where the two passes disagree, which is the section the task calls the most valuable.

Discipline applied throughout:

- Every load-bearing claim carries a `path:line symbol` anchor I opened this session. Line numbers were re-derived by `grep -n` after reading, not inherited from the brief or the proposals (the brief's own §11.1 / `05_RECONCILIATION.md:143` §4 record four instances this session of inheriting a summary; I re-verified the two the brief flagged as its own errors and both re-verifications held).
- A null result is reported with its trail (§6); an attack that failed is reported as failed (§5).
- Findings are weighted by what the defective artifact is load-bearing on (`CLAUDE.md:193` §0.1 pt 5): the game, the exported params, the port, or a Jordan decision. Apparatus-only defects are named in one line or dropped.
- Reachability is a property of an EDIT, not a branch (`05_RECONCILIATION.md:136`). Every "live" claim below names the season-loop path that reaches it; every "latent" claim names the missing caller.

### §0.2 Reading log

**Read in full (working tree):** `engine/substrate/{keys,composition,descriptors,stubwire,canon_buckets,__init__}.py` · `engine/autoload/{dice_engine,sigma_leverage,game_state,engine_clock,season_manager,scene_slate,victory,npc_ai}.py` · `engine/cross_scale/{scene_dispatch,echo_transport,parliamentary_bridge,combat_bridge,domain_echo,zoom_in_out,handoff_rules,articulation}.py` · `engine/mc_v18.py` · `engine/engine_params/composition.json` (all rows) · `references/key_graph.json` (per-type producers/consumers) · `references/module_contracts.yaml` (`composition_roles`, the 27 `modules` rows' `emits`/`consumes`, the `social_contest` row) · `references/descriptor_registry.yaml` (top-level blocks) · `systems/social_contest/sim/contest/{wrapper,resolver,contract,primitives,faction,__init__}.py`, `systems/social_contest/sim/{parliamentary_vote,parliamentary_stay}.py` · `systems/factions/sim/faction_action.py` (whole), `parliamentary_transfer.py:181-386`, `mass_seizure.py:270-308`, all 17 factions module heads · `systems/settlements/sim/*` (all six) · `systems/fieldwork/sim/*` (all three) · `systems/threadwork/sim/{operations,opposing}.py` · `systems/characters/sim/*` (all three) · `systems/overview/sim/*` (all six) · `systems/mass_battle/sim/{massbattle,rngsource}.py`, `resolution.py:35-130,195-230`, `orchestration.py:1526-1566`, `engine.py:1-80` · `systems/combat/combat_engine_v1/core.py:40-103`, `wrapper.py:1-47` + `fight`, `systems/combat/sim/combat.py:1-60` · `tests/valoria/test_degree_ladder_single_owner.py` (roster + allow-list), `test_faction_write_sweep.py:1-60`, headers of six other guards · `engine/tests/test_echo_transport.py:95-125`, `test_pipeline_reach.py:825-895`.

**Read in part:** `systems/social_contest/sim/contest/modes.py` (outline + `:520-577`), `armature.py:300-451`, `rhetoric.py:380-440`, `_kernel_tests.py:628-712`, `degree_extension.py` and `dictionaries.py` (symbol greps only) · `systems/world/sim/{npe,insurgency_pipeline}.py` (structure greps + the lines cited) · `systems/threadwork/sim/{collective,coherence,threadcut,co_movement,rendering}.py` (structure greps) · `tools/pathres.py`, `broken_dependency_checker.py`, the two `skills/valoria-vector-audit` scripts (parser sites only) · `tools/m1_acceptance.py` (row roster), `workplans/workplan_v6_progress.yaml` (juncture states).

**Proposals:** `05_RECONCILIATION.md` in full · `00_BRANCH_SHAPES.md` §0-§2, §7 · `01_SPINE.md` §1.9, §2, §3, §4, §7 · `02_NEGOTIATION.md` §5-§6 · `03_INQUIRY.md` §5-§6 · `04_CONSENSUS.md` §5-§6 · PR #362 `04_CODE_ARCHITECTURE.md` rev-2 preamble, §0, Part A, Part C, Part D.

**Not read:** any `.md` under `systems/*/` (design prose — under §0.05 it is reference, and this reading is of the mechanism); `godot/`; `systems/combat/combat_engine_v1/{combat_systems,weapon_physics,weapons,state_graph}.py` (≈3,700 lines of the personal-combat interior); `systems/mass_battle/sim/{hierarchy/units,geometry,percell,config}.py` and the bulk of `orchestration.py` (≈6,600 lines of the mass-battle interior); `references/restructure_ledger.md` itself.

### §0.3 Coverage table

| subsystem | depth | what I read | what I did not |
|---|---|---|---|
| `social_contest` | **full** (kernel spine) / partial (Stage-2/3 leaves) | wrapper, resolver, contract, primitives, faction, package shim, parliamentary vote + stay, the armature dot-product, CR5 backfire, the kernel test block over `GAMES` | `dictionaries.py` bodies, `appraise.py`, `narrative.py`, `policy.py`, `agon_harness.py`, `contest_legacy_stub.py` body |
| `factions` | **full** on the season-loop path / partial on unique actions | `faction_action.py` whole; every write site in `parliamentary_transfer`, `mass_seizure`, `crown_initiative`, `excommunication`, `absolution`, `council_solmund`; `tribunal`, `treaty`, `parliamentary_action` heads | the bodies of the five unique-action resolvers; 6 stub modules (read as stubs only) |
| `settlements` | **full** | all six modules | — |
| `fieldwork` | **full** | all three modules | — |
| `threadwork` | **full** on operations/opposing / partial on the rest | `operations`, `opposing` whole; `coherence`, `collective`, `threadcut`, `co_movement`, `rendering` by structure | the collective/coherence bodies |
| `characters` | **full** | conviction, beliefs, companion | — |
| `world` | **partial** | `npe` and `insurgency_pipeline` by structure + cited lines; the two stubs | `generate_npc`/`simulate_npc_actions` bodies |
| `overview` | **full** | season, accounting, ci/ms/rs/ip tracks | — |
| `mass_battle` | **partial** (seam + resolution primitives) | `massbattle.py` whole, `rngsource.py` whole, `resolution.py` die/ladder/σ sections, `_roll_volley_pool`, `engine.py` MECHANICS | ≈6,600 lines of interior (`hierarchy/units.py`, `geometry`, `percell`, `config`, most of `orchestration`) |
| `combat` | **partial** (seam + resolution primitives) | `core.py` pool/roll/degree/resolve, `wrapper.fight`, the deprecated `sim/combat.py` head, `combat_bridge` | ≈3,700 lines of interior (`combat_systems`, `weapon_physics`, `weapons`, `state_graph`), the workbench |
| `articulation` | partial | `engine/cross_scale/articulation.py` whole (the only code) | the design doc; `systems/articulation/` has no `.py` |
| `victory` | partial | `engine/autoload/victory.py` whole (the only code) | the design doc; `systems/victory/` has no `.py` |
| `_architecture` | surface | reached only through the substrate docstrings that cite it | all 44 docs |
| `npcs` | **not reached** | — | 19 docs, no `.py` anywhere (`npc_behavior` is declared producer of 11 Key types with `authority: prose`, `key_graph.json`) |
| `ui` | **not reached** | — | 10 docs, no `.py` |
| `engine/` | **full** | every module | `engine/tests/` beyond the two files above |
| `references/` | partial | the four registries named above + `key_types.json` | `restructure_ledger.md`, `names_index`, `canonical_sources`, `mechanics_index` |

Two rows say *not reached* and two say *surface*. That is the honest state; I did not read prose to manufacture coverage of the four doc-only subsystems.

---

## §1 · Top-down findings, by axis, worst first

Severity is weighted by load-bearing surface. **[GAME]** the campaign or a scene resolves differently; **[PORT]** the exported params or the Godot bridge; **[RULING]** a Jordan decision is silently unmet or contradicted; **[PROCESS]** apparatus only — named in one line.

### §1.1 Logic — cross-system contradictions

**L1 · [GAME] The victory condition's Political-Stability clause is dead: nothing writes the clock it reads.** `engine/autoload/victory.py:73` `ps = world.clocks.get('Turmoil', 0.0)`; `:74` `ps_ok = ps <= PS_MAX` (`:29` `PS_MAX = 6.0`). A grep for any assignment to `clocks['Turmoil']` (and `'PI'`, `'Strain'`, `'IP'`) across `engine/` and `systems/` outside tests returns nothing; the only clock writers in the tree are `ci_track.py:177` (`CI`), `ms_track.py:69,90` (`MS`) and the one-shot flag `mass_seizure.py:214` (`MASS_SEIZURE_USED`). So `ps` is always `0.0`, `ps_ok` is always `True`, and GD-1's third condition never binds. `create_world` seeds `'Turmoil': 0.0` (`game_state.py:338`) and nothing moves it. **This is not a stub that self-flags — it is a live `True`.** The game's sole victory function (its own docstring: *"the only place in sim that returns a game-end faction-victory result"*) has two operative clauses, not three.

**L2 · [GAME] [RULING] The degree `faction_action` consumes from mass battle is not the ruled ladder — it is a survivor-ratio classifier wearing the ladder's labels.** `systems/mass_battle/sim/massbattle.py:130-139`: `attacker_wins` is rout-state or a size comparison; `'Overwhelming'` requires `a_size_pct >= 0.75 and b_size_pct <= 0.25` (`:46-48`, three thresholds whose own citation reads *"NOT independently derived … no canon states them"*); `'Partial'` is *attacker not routed and ≥ 50 % survivors*. `faction_action.py:470` reads `deg = battle['degree']` and keys **Terms vs Storm** and the Accord delta off it (`:513-524`), and `_emit_battle_concluded` writes it into the `scene.battle_concluded` payload (`:392-424`). Jordan's 2026-08-14 ruling and its guard, `tests/valoria/test_degree_ladder_single_owner.py`, are satisfied **by name and not by mechanism**: the guard enrols `massbattle.py` under `DECLARED_ADAPTERS` (`:394-396`) as *"maps ROUT STATE and surviving-size fractions to a band … Its one real net/ob ladder, compute_degree, IS routed through the owner"* — which is true and is exactly how a second grammar of "degree" escapes: the guard tests ladders over `(net, ob)`, and this one has no `net` or `ob`. The band vocabulary reaches the faction layer with a meaning the ladder never assigned it. Every conquest in every seeded campaign runs through this (`faction_action.py:464` → `resolve_mass_battle`).

**L3 · [GAME] Ownership of a territory is stored in three places, and one writer updates only one of them.** The relation "faction F holds territory T" lives as `Territory.owner` (`game_state.py:234` class, written at `faction_action.py:499`, `parliamentary_transfer.py:361`, `mass_seizure.py:290`), as `Faction.territories` (`game_state.py:124`, written at `faction_action.py:497,502`, `parliamentary_transfer.py:341-342`), and as `Settlement.owner_faction` (`registry.py:60`, written only by `populate_from_geography` at world-gen — no transfer path touches it; grep for `.owner_faction =` finds no assignment anywhere). `mass_seizure.py:290` sets `Territory.owner` and never touches either list. PR #362 Part D row 10 (`:827`, *"two homes for one relation — STRUCTURAL"*) names this defect class, and `parliamentary_transfer.py:347-360`'s own comment records that the second home was already out of sync once (owner left stale until 2026-07-29, invisible to victory scoring). Readers disagree on which home is truth: `victory.py:65-66` and `mc_v18.py:295` read `Territory.owner`; `faction_action._conquest_targets:138` and `_undergoverned_share` read `Faction.territories`; `mc_v18.py:295` reads **both** in one expression (`held * 10 + f.L + len(f.territories)`). *Reachability:* `mass_seizure` has zero production callers (its own test at `tests/valoria/test_mass_seizure_accord_write.py` says so), so the third-home divergence is latent; the `owner_faction` staleness is live on every conquest but read by nothing in production today (`compute_settlement_state` has no non-test caller — §6).

**L4 · [GAME] "Time does not exist within a season" is wider than the SC trace shows.** `01_SPINE.md:320` §1.9 traces the OF-7 deferral for scene echoes. The whole-tree view adds the ordering **around** it: `mc_v18.py:132-138` runs every faction's action first, then `:149` the scene phase, then `:158` the parliamentary scene, then `engine_clock.py:122-123` drains the deferred applies and runs accounting. So a faction action in season N never sees season N's scene echoes; a scene contest **does** see season N's faction actions (`_emergency_council_parties:139` reads `f.L`/`f.Sta` after `_try_conquest`'s `adjust('L', -10)` at `:498` has landed synchronously); and the parliamentary vote's loser penalty (`parliamentary_vote.py:214`, synchronous) lands before the winner echo (deferred). Three timings for "a stat moved this season", decided by call order in one function, not by any rule. The spine's I-S6b names the mechanism; this names the shape.

**L5 · [GAME] GD-3 "promotion to faction" never creates a faction.** `insurgency_pipeline.py:199 check_insurgency_promotion` ends at `:248` `rec.parliamentary_status = new_status`; there is no write to `world.factions` anywhere in the module (grep `world.factions` / `Faction(` returns nothing). A promoted insurgency cannot act (`mc_v18.py:132` iterates `world.factions`), cannot be a conquest target's owner, and cannot win. `accounting.py:125-133` runs the promotion every season, so the flag flips live and means nothing.

**L6 · [RULING] Three Ob-from-score conventions coexist by design against a ruling that names one.** `crown_initiative.py:189 coronation_renewal_ob` = `floor(L/2)+1`; `tribunal.py` = `L*0.5` under formal grounds; `parliamentary_transfer.py:325` = `L + PARL_MAJORITY_OB_BONUS`. `tests/valoria/test_faction_obstacle_conventions.py:36-71` pins all three **as divergent**, its own docstring calling the third *"FULL score, contradicting the ruling, and stated as canon in its design doc."* The workplan (`workplan_v6_progress.yaml:45`) records the score/2 half as SUSPENDED by Jordan. Not new — but it is the one place a guard exists to keep a contradiction stable, which is the opposite of what §0.1 pt 5 licenses a guard for.

**L7 · [GAME] Composure is retired in one subsystem and a live currency in two others, and neither side reads the other's value.** `primitives.py:87` and the CR3 block retire Composure as a contest tracker (`RETIRED_TRACKERS`). `knots.py:84 BREAK_COMPOSURE_DAMAGE = 4` and `opposing.py:56 KNOT_COMPOSURE_STANDARD_LOSER` still price knot breaks and thread contests in Composure — and both return it in a `consequences` dict that nothing consumes (`knots.py:341`; no reader of `composure_damage` outside the module). A currency one subsystem abolished and two still charge, to no account.

**L8 · [GAME] Two Settlement-Order derivations from the same Accord disagree on every value.** `canon_buckets.py:38 canonical_accord` is nearest-neighbour over `ACCORD_MAP`; `settlement.py:120` is `floor(t.accord)` clamped 0-5. Computed: accord 4.0 → canonical 2, floor 4; 5.5 → 3 vs 5; 7.0 → 4 vs 5. The `floor` path is the registry-less fallback in `compute_settlement_state:95-107` and has no production caller (§6), so it is latent — but it is the kind of latent §0.1 pt 1 names: a reader that will be wrong the day it is called.

### §1.2 Keys — the roster against `engine/engine_params/key_types.json`

**K1 · [PORT] The substrate is a hub, not a bus.** 55 declared types (`key_types.json:5`). Non-test `Key(` construction sites in the whole tree: **four** — `echo_transport.py:320` (`scene.accord_echo`), `:427` (`scene.contest_resolved` / `scene.combat_resolved` by `KEY_TYPE_BY_SCENE:108`), `faction_action.py:392` (`scene.battle_concluded`), `parliamentary_transfer.py:228` (`da.public_governance`). Five types constructible; **three fire in a default seeded campaign** (`contest_resolved`, `battle_concluded`, `public_governance`); `combat_resolved` is unreachable (`DISPATCH_COMBAT_BRIDGE` default OFF at `mc_v18.py` `_dispatch_combat_bridge_on`, and no `queue_scene("combat")` exists — `scene_dispatch.py` docstring, verified by grep); `accord_echo` is dormant (`classify_scene_outcome:145` returns `None` unless a caller declares `scene_outcome`, and none does). Subscribers with runtime: the 13 in `articulation.py:116 _TRIGGER_TYPE_IDS`, every one a `stubwire` no-op (`:133`). **`scene.contest_resolved` — the type the campaign emits most — is not in that roster and has zero subscribers.** The only effect any Key has on the world is its own emitter's `apply` closure run at `accounting_boundary` (`keys.py:571,581`). That is a deferred-write queue with a log attached, which is a fine thing, but it is not inter-subsystem transport, and `tests/valoria/test_contract_runtime_conformance.py:17` measured the same shape (*"60 declared emit edges, 0 observed"*).

**K2 · Declared-with-no-producer:** 50 of 55 types have no construction site in non-test code. `key_graph.json` declares producers for 53 (`meta.legacy_event` and `*` are the baseline exceptions, `test_key_graph.py:45`), so the declaration layer says 53 and the code says 5. Eleven types name `npc_behavior` as producer (`key_graph.json`: `scene.witness`, `state.concern_resolved`, `state.belief_revised`, `scene.displacement`, `mechanical.project_advanced`, `state.project_failed`, `state.project_completed`, `state.opinion_revised`, `scene.interaction`, `scene.dialogue`, `scene.gossip`), and `systems/npcs/` has no `.py` file. `mechanical.season_change` and `mechanical.accounting` name `engine_clock` (`key_types.json:351`); `engine_clock.py` constructs no Key.

**K3 · Produced-with-no-consumer:** `scene.contest_resolved` (K1); `scene.battle_concluded` — declared consumers `faction_state`, `npc_behavior`, `piety_track`, `articulation_layer`; only articulation subscribes and it is a stub; `da.public_governance` — same. All three are log-only by design (`faction_action.py:425` *"NO apply= — log-only"*).

**K4 · Payload/schema mismatch — the class is NOT systemic today, and is latent by construction.** I checked every constructible type's payload against `required_payload_fields` (script over `key_types.json`): `scene.contest_resolved`, `scene.combat_resolved`, `scene.accord_echo`, `scene.battle_concluded`, `da.public_governance` — **zero missing required fields**. One undeclared extra (`degree` on `battle_concluded`), which `validate_payload:308` does not check. The session's `A11` defect (`05_RECONCILIATION.md:88` B5) is real and reproduces here — `scene.investigation_resolved` requires `[scene_id, subject_id, finding]` and the builder at `echo_transport.py:434-437` supplies `{scene_id, outcome, participants}` — but it is a property of **adding a row to `KEY_TYPE_BY_SCENE`**, because that one builder hardcodes one payload shape for every scene family. The defect is in the builder's shape, not in the five live types.

**K5 · [PORT] Key ids are minted from three independent per-world counters, none declared, none serialized.** `echo_transport.py:318` `world._echo_key_seq`, `faction_action.py:392` region `world._battle_key_seq`, `parliamentary_transfer.py:228` region `world._parl_key_seq` — all set by `getattr(world, name, 0)` on a `World` dataclass that declares none of them (`game_state.py:256`) and `serialize_world:355` / `restore_world:425` carry none. A restored world re-mints from `n0` and collides with the log it is meant to replay. `references/module_contracts.yaml:1545 save_replay_premise` records the replay premise as the port's master parity check. PR #362 D-35 (`:856`) wants one mint `H(seed, tick, subject, purpose)`; the tree has three sequences and a season index.

**K6 · `KeyLog` invariant 9 never runs in production.** `make_scheduler:184-192` builds `KeyLog(_registry())` with no `stat_vocabulary`; `keys.py:355` keeps it `None`, so the OPT-AV-16 stat-name check is dead on every campaign. Minor; noted because `Target.stat_deltas={"L": …}` (`echo_transport.py:433`) is the one place a stat name crosses the substrate and nothing checks it.

### §1.3 State changes — the whole-tree write map

Fields with more than one writer, or with a writer and no owner:

| field | writers (non-test) | owner? | grade |
|---|---|---|---|
| six `Faction` scalars (`L Sta W I Mil intel`) | 31 call sites in 10 files, **all** via `Faction.adjust` (`game_state.py:153`); zero bare assignments (my grep; `test_faction_write_sweep.py:167` guards it) | yes | **MECHANICAL** — the one clean write path in the tree |
| `Faction.standing` | **9 direct sites, 3 files**: `crown_initiative.py:98,116,119,167,177,254,267,270`, `parliamentary_transfer.py:379`, `absolution.py:86`; no clamp, no bounds; `descriptor_registry.yaml:285` lists Standing only as a track name | no | **CONVENTION**; explicitly excluded by the sweep (`test_faction_write_sweep.py` docstring) |
| `Faction.excommunicated` | `excommunication.py:142` (set), `crown_initiative.py:256,263` (clear); readers: `serialize_world` only — **no game logic reads it** (grep) | no | flag with no consumer |
| `Faction.territories` | `faction_action.py:497,502`, `parliamentary_transfer.py:341,342`; **not** `mass_seizure` | no | L3 |
| `Territory.owner` | `faction_action.py:499`, `parliamentary_transfer.py:361`, `mass_seizure.py:290` | no | L3 |
| `Territory.accord` | `Territory.adjust_accord:248` (granular via `MULTS`, 5 call sites), **direct tier writes** `mass_seizure.py:296`, `parliamentary_transfer.py:346` via `ACCORD_MAP` | two conventions | the drift probe at `accounting.py:54` measures the third home (`Settlement.order` aggregate) but not this split |
| `Territory.entry_terms_l_seed` | `faction_action.py:520` — a **dynamic attribute on a dataclass that does not declare it**, not serialized, read by nothing | no | write-only |
| `Settlement.order` | `echo_transport.py:346,351` (deferred applies), `populate_from_geography` | yes (one path) | dormant (K1) |
| `Settlement.legitimacy`, `.popular_support` | none (`registry.py:74`; the row's own comment: *never read or written*) | — | declared, inert |
| `world.clocks['CI']` | `ci_track.py:177` only (`excommunication.py:167` routes through it) | yes | MECHANICAL |
| `world.clocks['MS']` | `ms_track.py:69,90` only; `opposing.py:233`, `co_movement.py:143` route through it | yes | MECHANICAL |
| `world.clocks['Turmoil' / 'PI' / 'Strain' / 'IP']` | **none** | — | L1 |
| `world.clocks['MASS_SEIZURE_USED']` | `mass_seizure.py:214` — a flag stored in the clock dict | — | a bool wearing a float's home |
| `world.battle_count` | `faction_action.py:526`, **inside** `if battle['attacker_wins']` — counts attacker victories, not battles (`test_battle_concluded_key.py` records 76 resolved / 33 reported on seed 42) | one writer, wrong name | telemetry |
| undeclared `World` attributes | `echo_scheduler`, `key_log`, `_echo_key_seq`, `_battle_key_seq`, `_parl_key_seq`, `dispatch_combat_bridge`, `accord_drift_probe_hits`, `casus_belli` (`parliamentary_transfer.py:29` reads it; nothing writes it) | — | none survive `serialize_world` |
| the 12 per-module stores | each module's `_store(world)` router (§4 row 12) | one per module | consistent, but the **module-level fallback** in each is a second store with no world |

### §1.4 Deduplication — rules that live more than once

Full ledger in §4. Headline: **20 rules with more than one home**, of which the tree already names three (the combat ladder hold, the ledger parsers, the `pathres` prefix hazard). The four that are load-bearing on the game:

**D1 · [GAME] The mass-battle engine re-implements four engine primitives and only one is equivalence-guarded.** `systems/mass_battle/sim/resolution.py:37 roll_pool` re-implements the d10 face rule (`dice_engine.py:153 _die_result`) with its own loop over `rngsource.get().randint(1,10)` (`:50`); `:209 _sigma_softcap` re-implements `sigma_leverage.py:141 soft_cap`; `:221 _sigma_net_boost` re-implements `sigma_leverage.py:190 net_boost` with its own `_SIG_PER_DIE = 0.800` (`:227`); `:104 compute_degree` re-implements `dice_engine.py:227 degree_from_net`. The ladder is guarded (`test_degree_ladder_single_owner.py:312`). **The other three are not**: I searched `tests/valoria` and `engine/tests` for any test naming both `_sigma_net_boost`/`_sigma_softcap` and `sigma_leverage`; `test_degree_boundary_epsilon.py` exercises the mass-battle pair alone and never compares them to the owner. A change to `M_MAX` (`sigma_leverage.py:104`) or to the per-die σ in either home moves every conquest with no test to see it. The re-implementation is deliberate (`resolution.py:104` docstring: *"deliberately takes no `engine.*` dependency … a porting-architecture call nobody has made"*) — which makes it a Jordan call, and the missing guard is the cost of not having made it.

**D2 · [GAME] `MULTS` has seven private copies.** `game_state.py:74` is the owner; `crown_initiative.py:33-35` (`_MULTS_W`, `_MULTS_L`, `_MULTS_ACCORD`), `council_solmund.py:24`, `excommunication.py:35`, `absolution.py:27-28` each re-declare the granularity a stat delta is divided by. `Faction.adjust` reads the owner; the copies feed the *deltas passed to it*, so a change to the owner leaves every unique action mis-scaled with no error.

**D3 · The per-die statistics live in four places in two files.** σ = 0.800 at `dice_engine.py:175`, `sigma_leverage.py:77` (`PER_DIE[7]`), `sigma_leverage.py:113` (`SD_PER_DIE`), `resolution.py:227`; μ = 0.40 at `dice_engine.py:174`, `sigma_leverage.py:77`, `sigma_leverage.py:112`. Two of the four σ homes are in the same file that calls itself the single source.

**D4 · `TN = 7` is declared eleven times** (`sigma_leverage.py:91`, `combat/sim/combat.py:72`, `parliamentary_vote.py:54`, `contest_legacy_stub.py:59`, `parliamentary_transfer.py:66`, `crown_initiative.py:36`, `tribunal.py:54`, `council_solmund.py:25`, `absolution.py:29`, `operations.py:67`, `knots.py:58`). Harmless today because `dice_engine.py:182 _require_tn7` refuses any other value — the duplication is inert only because the owner refuses the argument it is handed.

### §1.5 Unity — several ways to do one thing

**U1 · Four randomness conventions.** (a) a threaded `rng` parameter (`dice_engine`, all of `factions/`, `threadwork/`, `fieldwork/`); (b) the **global** `random` module, reseeded-and-restored by the caller (`resolver.py:32 roll_net` → `_sigma.roll_net(pool, rng=random)`; `:139,:144` `random.gauss`; `:334` `random.uniform`; the dance at `scene_dispatch.py:297-303`); (c) a module-level holder (`rngsource.py:39-58`, scoped by `massbattle.py:124 rngsource.using`); (d) a derived child stream (`combat_bridge.py:131` `Random(rng.getrandbits(32))`). All four are deterministic per seed; that they are four is the finding. PR #362 D-35 (`:856`) grades "a new draw moving unrelated goldens" MECHANICAL under a keyed mint; here a new draw anywhere on `world.rng` moves every later draw, and each convention has its own way of hiding that.

**U2 · Three aggregate-to-actor derivations, three `[SEED]` mappings.** `scene_dispatch.py:139` `(round(L), round(7 - Sta))` → contest faculties; `combat_bridge.py:109` `round(Mil)` → a Combatant's `history`; `massbattle.py:76` `round(Mil)` → a Unit's `power` with six inherited defaults. Each module docstring calls its own mapping provisional. PR #362's answer is one `faction_q.resolve(proj, side)` (`:707` §C.5.1); the tree has three, in three lanes.

**U3 · Two Persuasion-Track band homes, three band vocabularies.** `resolver.py:81-96 PersuasionTrack.resolve` (`A_total/A_decisive/committee/B_decisive/B_total`), `contest_legacy_stub.py:67-71` `PERSUASION_*` consumed by `parliamentary_vote.py:45,200` (`passed/failed/committee`), `parliamentary_bridge.py:110 _winner_and_degree` translating the second into the ladder's four (`Overwhelming/Success/Partial`). Thresholds agree (§5); vocabularies do not.

**U4 · The contest's degree is an ordinal 0-3 (`resolver.py:307` `DEGREE_ORDINAL[...]`), combat's is a lower-case string (`core.py:94`), mass battle's is Title-Case (`resolution.py:117-120`), factions' is `Degree` enum or Title-Case string by module.** `dice_engine.py` owns all three spellings (`DEGREE_LABEL`, `DEGREE_ORDINAL`, `Degree`). One ladder, three encodings — by design, and the design is honest about it.

**U5 · Two dataclasses named `Faction`.** `game_state.py:110` (the world's) and `systems/social_contest/sim/contest/faction.py:13` (an adapter with `mandate`, `fixed_lean`, `discipline`). The consensus critic tripped on exactly this (`05_RECONCILIATION.md:143` §4 item 3).

### §1.6 Primitives — what is genuine, who composes on it

| candidate | verdict | composed on by | reimplemented by |
|---|---|---|---|
| `dice_engine.degree_from_net:227` | **genuine** — one ladder, one extension seam (`BandExtension:95`) | contest (`resolver.py:307` with the injected extension), factions (`faction_action.py:129`), threadwork (`operations.py:152`, `opposing.py:88`), knots (`knots.py:227`), the deprecated combat (`sim/combat.py:160`) | mass battle (`resolution.py:104`, guarded), combat v1 (`core.py:57`, declared hold), the survivor-ratio bands (L2) |
| `sigma_leverage` (`soft_cap:141`, `net_boost:190`, `roll_net_continuous:282`) | **genuine** | combat v1 (`core.py:103`), contest (`resolver.py:32`, `_reception:283`), the armature (`armature.py:357` via `level("moderate")`), factions (`faction_action.py:100`) | mass battle (`resolution.py:209,221`, unguarded) |
| the armature dot-product (`armature.py:346 style_axis_alignment` → `:357 style_axis_dsigma`) | **genuine and composed correctly** — one channel into `net_boost`'s δσ term, `ARMATURE_MAX_DSIGMA = level("moderate")` reused rather than seeded | the Bout (`resolver.py:283` `dsigma_bonus`) | nothing — but it is unreachable from the production seam (`build_contest:110` has no `armature=`; `agon_harness.py:71` WORKAROUND 3) |
| `engine/substrate/keys.py` (Key, KeyLog, TickScheduler) | **genuine as a log and a deferred-apply queue**; not yet a bus (K1) | four emitters, one real subscriber roster of stubs | — |
| `engine/substrate/composition.py:43 require` | **genuine** — the one seam by which `engine/` reaches `systems/` (28 roles in `composition.json`) | `mc_v18`, `engine_clock`, `scene_dispatch`, `parliamentary_bridge`, `echo_transport`, `game_state.restore_world` | `combat_bridge.py:96` — the one path seam, declared |
| `engine/substrate/descriptors.py` | **genuine** for the six faction scalars (`faction_bounds:78`, read by `Faction.adjust:153`) and settlement Order (`SETTLEMENT_STATS:66`, read by `echo_transport`) | game_state, echo_transport, conviction (`CONVICTIONS`), npe | `registry.py:50 STAT_MIN/MAX`, `settlement.py:40` — two literal twins of `set.order`'s bounds |
| `systems/settlements/sim/ledger.py` (`LedgerTag:36`, `ledger_add:47`) | **genuine, single-owner, and composed on by nobody outside its package** — `registry.py:100` `Settlement.add_tag` is its only caller; `ledger_sweep:69`'s only caller is `succeed_governor:199`, which has zero callers; `ledger_has`/`ledger_get` do not filter expiry, so `ttl` is decorative today (the brief's §11.4 last row, re-verified) | — | the SC subsystem emits stat deltas instead (`social_contest_currency_v1.md:23` names the ledger as what it should compose on; zero code references either way — `SESSION_BRIEF.md` §9, re-confirmed by grep) |
| `Faction.adjust:153` | **genuine** — the one clean write path | 31 sites | — |
| `stubwire.stub_resolve:64` | genuine | 20+ sites | — |
| the "store router" (`_store(world)`) | **a pattern, not a primitive** — twelve hand-copied instances (§4 row 12) | — | itself, twelve times |

### §1.7 Code-shape compliance against PR #362

PR #362 §0 (`:66`) grades per invariant; I do the same, and I report the tree's grade, not the document's aspiration. Module-by-module against §A.2 (`:127`):

| PR #362 module | what the tree has | conformance | grade of the tree's enforcement |
|---|---|---|---|
| `state/` — owned stores, **the gate**, the log, the ledgers, the id mint | `game_state.py` (World + 14 `Any`-typed registries) · `keys.py` (the log) · `ledger.py` (a ledger, unused) · no gate · three id counters (K5) | **diverges** — one MECHANICAL write path exists for six scalars (`Faction.adjust`), every other field is bare attribute assignment (§1.3) | six scalars MECHANICAL (guarded); everything else CONVENTION; D-3 (`:820`) "no public setters" is false for every dataclass |
| `data/` — closed sets + **ONE** loader with twelve invariants | `engine_params/*.json`, each cooked by its own `tools/export_*.py --check`; four leaf readers (`descriptors`, `composition`, `world_initial_state`, `keys.TypeRegistry`) | **partial** — per-artifact MECHANICAL (`--check` gates), no cross-artifact validation; `MULTS` and seven copies are literals (D2); `params_tables.yaml` is captured prose | MECHANICAL per file; no loader; D-25 (`:843`) "derived kind roster" holds — `log.append` refuses an unregistered type (`keys.py:308`) |
| `queries/` — ownerless functions, barrier cache | none as a module; `registry.province_accord:185` and `_conquest_targets:138` are queries; `Faction.territories` is a **stored** aggregate of `Territory.owner` (L3) | **diverges** — D-8 (`:825`) "a stored aggregate — no field slot" is violated by the tree's most-read relation | CONVENTION |
| `decision/` — AX-2's island, no `World` in scope | `faction_take_action:208` reads `world` throughout and decides and resolves in one body; `npc_ai.select_action` is a stub; `_derive_vote:90` reads `world.factions` | **absent** — D-2 (`:819`) has no representation | none |
| `loop/` — driver + six steps, tokens minted by the driver | `engine_clock.run_tick:90`: SEASON_TICK → ACTION → ACCOUNTING_BOUNDARY (three phases, one caller-supplied body); `t += 1` once at `season_manager.py:35` | **partial** — D-45 (`:867`) holds; D-41 (deliberate on a frozen projection) has no representation (L4); no tokens | D-45 MECHANICAL; the rest CONVENTION |
| `seam/` — `contest()` returning a **Margin**, one ladder | `scene_dispatch._resolve_slot` returns a **winner/band** (`:308` `out["result"]={"winner": verdict…}`), `combat_bridge.resolve:131` returns ±1/0, `resolve_mass_battle:99` returns a bespoke `degree` (L2); the ladder is one (`dice_engine:227`) with a declared hold | **diverges** on D-24 (`:842`) at every seam; conforms on D-30 (`:849`) by the guard | D-30 MECHANICAL (`test_degree_ladder_single_owner.py`); D-24 CONVENTION; D-19 (`:837`, "no default depth") holds in `keys.py:463` and is defeated one layer up by `echo_transport.py:102` defaults |
| `manifest/` — role → provider, resolved at boot | `composition.json` from `module_contracts.yaml:70 composition_roles`, 28 roles, resolved at first use and cached (`composition.py:43`) | **conforms** — the one place the tree has PR #362's shape today | MECHANICAL (exporter `--check` + `test_engine_does_not_import_systems.py`) |
| `port/` | `godot/` — not read | — | — |
| `tests/` — falsifiers | 168 files in `tests/valoria` + `engine/tests` | present | D-50 (`:872`, `assert_over`) has no representation; the `checked == N` idiom is applied by hand in some guards |

**Summary grade:** the tree conforms to PR #362 in exactly one module (`manifest/`), partially in three (`data/`, `loop/`, `seam/`), and diverges or has nothing in five. PR #362's own D-30 admits "no second resolver" is CONVENTION; in the tree that clause is the best-guarded of all of them. The clauses PR #362 grades STRUCTURAL (the gate, the token, the frozen projection, the Margin return) are the ones the tree does not have at all. That is consistent with PR #362 being HELD BACK IN FULL; it is stated here so nobody reads "PROPOSED" as "partly built".

---

## §2 · Bottom-up, one subsection per subsystem reached

Each: what it owns (state it is the single writer of), what it reads, what it emits into the campaign, what executes on the season loop versus what is declared and dead.

### §2.1 `social_contest` — full on the spine

**Leaves.** `contract.py:7` `A, B`; `:17 FaultState` (per-contestant, built only for `{A, B}` at `resolver.py:211`); `:25 Adjudicator` and `:38 Panel` (frozen; carry no `FaultState`, which is why the consensus antibody cannot bind to a member — `05_RECONCILIATION.md:99` §2, re-verified). `primitives.py:31 Standing` (= `Face`, `:87`), `:49 Reserve` (`COST` `:51`, `REGAIN = 4` `:52` — `support` costs 2 and regains 4, the kernel-wide free stall `03_INQUIRY.md:365` names), `:208 Pool` (`size = max(5, 2·faculty + 3)` `:211`), `:222 Leverage` (`ONGROUND = level("moderate")` `:225` — composed on `sigma_leverage`), `:262 DefeatCatalogue` (`check:272` iterates only `A, B`).

**Composition upward.** `resolver.py:283 _reception` = `Pool.size` → `roll_net:28` (global stream) + `net_boost(lev + dsigma)` → `degree_from_net(..., extension=CONTEST_DEGREE_EXTENSION, pool=pool)` (`:307`) — the one place in the tree that uses the `BandExtension` seam. `_advance:314` multiplies by `random.uniform` jitter (`:334`). `_apply:341` is the move grammar; the evasion fault (`:380-381`) fires only on `Stasis.relevant`'s strict equality (`primitives.py:21`). `Bout.resolve:440` runs `budget` exchanges and checks `faults.check` after every move (`:457`). `Venue:151` carries the win-condition; six `WinCondition` subclasses (`:52-147`), of which `VoteAtClose:98` draws `random.gauss` at `:139` (weighted) and `:144` (simple) — the production proceeding `guild_arbitration` (`modes.py:502`, selected by `scene_dispatch.py:118`) resolves here.

**Seam.** `wrapper.py:110 build_contest` (no `armature=`, no `rng=`) → `Contest:59` → `resolve_contest:248` → `GAMES[game]:236` → `_resolve_agon:203` or `_stub:220`. Two return shapes (`:248` docstring says so). `_resolve(sym):303` is the MECHANICS symbol resolver the spine's `A8` collides with (B3, confirmed by reading).

**What it owns.** Bout-local state only. **One** persistent write: `parliamentary_vote.py:214` `Faction.adjust("L", …)` — synchronous, the only contest-side write that already binds in-scene.

**What it emits.** Nothing — zero `Key(` in the package (grep). Its Key is built at `echo_transport.py:427`.

**Executes on the loop.** `guild_arbitration` via the Stability-Crisis trigger (`scene_dispatch.py:84` `Sta <= 2`); the §10 vote via `parliamentary_bridge.py:150` every season. **Declared and dead:** the three `GAMES` stubs; `DyadicMode/NegotiationMode/CeremonialMode` (`modes.py:333-351`); `INSTITUTIONAL_MODES:150` and the cross-cultural venues (no production caller); `faction.py:86 succession`, `:128 coalition_vote`, `:48 vote` (adapter; no production caller); `agon_harness.py` (zero callers); the `contest_legacy_stub` shim's `run_contest` (`__init__.py:35-36` re-exports it for a caller at a path that no longer exists); `parliamentary_stay.resolve_stay_lift` (zero callers); `Contest.resistance` (`wrapper.py:43 _derive_resistance` — derived, never plumbed; `MECHANICS` says PARTIAL); the armature (unreachable from the seam).

**The split table.** `faction.py:107` `leader = 'a' if t >= 5 else 'b'`, `:117` `ratio = {4: 0.60, 5: 0.55, 6: 0.50}[...]`. Latent (no production caller) — `05_RECONCILIATION.md:194` §6 has it right and I add nothing.

### §2.2 `factions` — full on the loop path

**Leaves.** Seven private `MULTS` copies (D2); eleven `TN=7`s (D4); `_NOOP = 'invalid'` as the dispatch sentinel.

**Composition.** `faction_take_action:208` — RNG-free state signals → re-weighted prior → one `rng.random()` draw → `_try_faction_unique:276` (Crown/Church chains, universal Censure fallback `:286`) → `_try_conquest:433` → `_try_muster:531` → `_try_govern:562`. Conquest calls `resolve_mass_battle:464`, reads L2's degree, transfers ownership (`:497-503` — both homes updated here), writes `adjust('L', -10)` on the loser, `t.garrison = True`, Terms/Storm Accord (`:513-524`), `t.entry_terms_l_seed` (`:520`, write-only), `world.battle_count` (`:526`, wins only). `_successes:100` and `_degree:129` compose on `sigma_leverage.roll_net_continuous` and `degree_label` — correct.

**Owns.** Every faction scalar write in the tree goes through `Faction.adjust`; this package is 27 of the 31 sites. It also owns `Faction.standing` (9 direct sites, no bounds), `Faction.excommunicated` (set/clear), and two of the three `Territory.owner` writers.

**Emits.** `scene.battle_concluded` (`:352`, log-only) and `da.public_governance` (`parliamentary_transfer.py:181`, log-only). The emission wrapper — `sched is None → return`, `try … except Exception: if VALORIA_STRICT_KEYS: raise` — is copy-pasted between the two (`faction_action.py:352-427`, `parliamentary_transfer.py:181-246`).

**Executes.** `faction_take_action` every season per parliamentary faction with territory (`mc_v18.py:132-138`); `propose_transfer:248` via the bridge (`parliamentary_bridge.py:134`); the Church chain gates on `EXCOMM_PREREQ_L_LIGHT` (`excommunication.py:29`) — which is why `03_INQUIRY.md`'s `formal_grounds_check` edit is campaign-reachable (B2, re-traced: `excommunication.py:78` → `tribunal.py:73`). **Declared and dead:** `mass_seizure` (zero callers; `attempt_mass_seizure_declaration:162` never invoked); `treaty.propose_treaty:99` (stub); `process_treaty_expirations:121` (I found no caller in `season_manager`, `accounting` or `faction_action` — the arc-boundary lapse it implements is not on the loop); six OI-17 stubs (`charter_liberties`, `hafenmark_equipment`, `home_sanctuary`, `infrastructure_reclamation`, `varfell_mandate_action`, `varfell_territorial_acquisition`); `tribunal.run_tribunal:143` (stub); `world.casus_belli` (read at `parliamentary_transfer.py:29` region, never written — the only auto-populated CB is `crown_constitutional_restoration`, `derive_transfer_candidate:124`).

### §2.3 `settlements` — full

**Leaves.** `ledger.py` (§1.6); `adjacency.py:9 ADJACENCY` (a literal graph — the fourth home of world geography beside `world_initial_state.yaml`, `valoria_geography_v30.yaml` and `temperaments.py`'s `TERRITORY_TEMPERAMENTS`; not a duplicated rule, but four authored surfaces for one map, with `T16` absent from `ADJACENCY` and present in `TERRITORY_TEMPERAMENTS`); `registry.py:50 STAT_MIN/MAX` and `settlement.py:40` (twins of `descriptors.SETTLEMENT_STATS`).

**Composition.** `registry.populate_from_geography:216` at world-gen (via the `world_gen_settlements` role) registers 37 settlements; `province_accord:185` = `floor(mean order)`; `Settlement.add_tag` → `ledger_add`. `infrastructure.py:139 build_infrastructure` and `seizure_ob_modifier:236` — no production caller (only `mass_seizure`, itself dead). `temperaments.apply_strain_shock:151` — no production caller (`env.peninsular_strain_shock` has no producer, K2).

**Owns.** `Settlement.*` (order written only by `echo_transport`'s deferred apply, dormant); `world.territory_infrastructure`, `world.npc_drift_state` (both empty in every campaign — no writer reaches them).

**Emits.** Nothing (declared `env.population_change`, `key_graph.json`; no construction site).

**Executes.** World-gen population; `province_accord` inside the accounting drift probe (`accounting.py:54`, report-only). **Everything else in this package is dormant on the loop.** The Record primitive the whole SC programme wants to compose on is live code with one caller family and no season-loop path.

### §2.4 `fieldwork` — full

**Leaves.** `knots.py:58 KNOT_FORMATION_TN`, the ED-912 gauge constants; two id counters (`:236` module list, `:238` `world.knot_id_counter`) incremented **both** on every formation.

**Composition.** `form_knot:173` — prerequisites on duck-typed actor objects → `roll_pool` → `degree_label(net, 2)` (`:227`, composed on the owner) → tier. `sustain_knot:251`, `check_knot_rupture:276`, `apply_knot_loss:316` → late-imports `conviction.apply_conviction_scar` (`:361`, `'Honor'` — the 2026-08-24 fix, real name now) and `coherence.apply_coherence_delta` (`:375`), each inside `except (ImportError, AttributeError): pass` (`:364`) — a swallow that would hide a renamed function.

**Owns.** `world.knots`. **Emits.** Nothing (declared `meta.knot_formed`, `meta.knot_ruptured`, `scene.gift`, `state.belief_revised` — none constructed).

**Executes.** Nothing on the loop: `mc_v18.py` records the deferral as a `stub_resolve` (`'form_knot(world-gen|season-tick)'`); `fieldwork.py:38` and `investigation.py:30` are OI-02 stubs reached by `scene_dispatch.py:346` only if a `fieldwork`/`investigation` scene is queued, and none is. **The whole subsystem is declared-and-dormant**, executing only under its own tests.

### §2.5 `threadwork` — full on operations/opposing

**Leaves.** `operations.py:67 TN_STANDARD`, `:71 DEPTH_OB` (Fibonacci), `:122 COHERENCE_COST_BY_SCALE`; `opposing.py:56` the Composure prices (L7).

**Composition.** `_actor_pool:162` (Spirit×2 + History + TPS) → `_resolve_operation:177` → `roll_pool` → `_compute_degree:152` (= `degree_label`, composed) → `apply_coherence_delta:211` (the blanket −1 on Partial/Failure at `:208`, the module's own recorded C-TW-3 defect) → an `ms_delta` returned but **not applied** (`:214-227`; `mending_stability_delta` on the result, applied by nobody — `opposing.py:233` is the one site that routes MS through `ms_track`). `opposing.py:103` — two pools, `_degree_label:88` folding the owner's four bands to three (enrolled, guarded), a six-row table hand-transcribed with its own `d6` (`:191 rng.randint(1, 6)` — the only non-d10 die in the tree), knot strain via late import.

**Owns.** `world.practitioners` (`coherence._store:57`), `world.threadcut_beings`, `world.comovement_deck`. **Emits.** Nothing (declared `scene.thread_operation`, `meta.thread_woven`). **Executes.** Nothing on the loop (no caller of any `attempt_*` in `engine/` or `factions/`); `rendering.py:29 apply_rs_strain` and `rs_track.py:28` are stubs, so RS — the clock `victory` does not read but `domain_echo` and `echo_transport` name — has no live path in either direction.

### §2.6 `characters` — full

`conviction.py:59 CONVICTIONS = descriptors.CONVICTIONS` — composed on the registry, and the module's own header records why (the `'Loyalty'` no-op). `apply_conviction_scar:177` → `resolve_conviction:205` (raises on unknown) → per-Conviction counts; the season-cap heuristic `:212` keys on the **source string** containing `'thread'`/`'witness'` — a rule carried in free text. `beliefs.py:189 social_success` returns a `momentum_delta` it never applies (Momentum has no store anywhere — `MOMENTUM_CAP:41` caps a value no field holds). `companion.py:28` stub. **Owns** `world.convictions`, `world.beliefs`. **Emits** nothing (declared `state.scar_acquired` by `piety_track`, which has no `.py`). **Executes** nothing on the loop.

### §2.7 `world` — partial

`npe.py:353 simulate_npc_actions` runs every season (`accounting.py:139`) over `world.npcs` — which is **always empty**, because `generate_npc:226` has no automatic caller (`mc_v18.py` stub-flags it). So the one world-side module on the loop iterates nothing, every season. `_ecology_weights:186` composes on `canonical_accord` (`:200`) — correct. `insurgency_pipeline.py:139 check_insurgency_triggers` and `:199 check_insurgency_promotion` run every season (`accounting.py:125-133`) and do fire (`CampaignResult.insurgencies_formed` is telemetry) — and promotion writes only a flag (L5). `miraculous_event.py:28`, `restoration_movement.py:30` — stubs.

### §2.8 `overview` — full

`season.py:50 run_season` is an adapter over `engine_clock.run_tick` (`:81`) — the composition moved to the engine and the module says so. `accounting.py:96 run_accounting` — six steps, four of which do something in a campaign (`apply_seasonal_ci:113`, MS decay `:118` every 4 seasons, insurgency `:125-133`, the probe `:54`); `simulate_npc_actions:139` iterates an empty store (§2.7). `ci_track.py:170 apply_ci_delta` is the single CI owner (both callers route through it); `_church_is_prominent:78` reads `Faction.L` as Mandate — the pre-LPS-1 convention every faction module carries. `ms_track.py:73` is the single MS owner. `rs_track.py:28`, `ip_track.py:29` stubs. **This is the cleanest package in `systems/` on the single-owner axis and the one whose docstrings are most often stale about it** (`ms_track.py`'s header still records a DRIFT against an `accounting._ms_decay` that `accounting.py` does not contain).

### §2.9 `mass_battle` — partial (seam and resolution primitives)

`massbattle.py:99 resolve_mass_battle` is the strategic adapter: `_faction_to_unit:63` (Mil → `power`, six inherited defaults, own `[GAP]`), `_GarrisonStub:51` (`Mil=1.5` for an ownerless territory), `rngsource.using(world.rng):124` → `run_battle(…, 18)` → the survivor-ratio bands (L2). `resolution.py`: the four re-implemented primitives (D1); `roll_pool_fractional:57` realises the fractional die stochastically. `orchestration.py:1526 _roll_volley_pool` now delegates to `roll_pool` (`:1547`) — the one TN-6 site the sweep genuinely moved, per its own docstring. `rngsource.py` — a module-level holder, restored on exit; nothing inside the engine calls `set` (`:47`). `hierarchy/units.py:2117` a roll-under `randint(1,10)` inside `resolve_internal_collisions:2062`, dead (zero call sites per its own comment). **Owns** nothing on `World` — the engine writes its own `Unit` objects and the adapter reads survivors. **Emits** nothing itself; `faction_action` emits `scene.battle_concluded` on its behalf. **Executes** on every conquest. Interior (≈6,600 lines) not read.

### §2.10 `combat` — partial (seam and resolution primitives)

`combat_engine_v1/core.py:50 resolution_pool` = `max(5, History + 6)`; `:56 roll_net` → `SL.roll_net_continuous`; `:98 resolve` = roll + `SL.soft_cap · SL.sigma_n` (composed correctly); `:57 degree` — the **declared hold** at the pre-ruling ladder (`:94` `net >= 2*ob - 0.5 and net >= 2.5`), with a 30-line justification and an entry in the guard's `HELD` table (`test_degree_ladder_single_owner.py:265-274`). `wrapper.py:4` `sys.path.insert(0, dirname(__file__))` — the bare-name import convention `combat_bridge.py:96` mirrors (the declared path seam). `fight:465` returns `±1/0` (`:483`). `combat/sim/combat.py:4` DEPRECATED and still the `scene_resolver.combat` composition role's target; its `_degree:160` is routed through the owner. **Executes** on the loop: **nothing** — `combat_bridge` is behind a default-OFF flag and no trigger queues a combat scene. The personal-combat engine's only executions are its own tests and the balance workbench. Interior (≈3,700 lines) not read.

### §2.11 `articulation`, `victory` — partial (code only)

`articulation.py:152 subscribe_all` registers 13 stub callbacks (`:116`); the three declared entry points (`render_protagonist_lens`, `evaluate_articulation_triggers`, `generate_chronicle_entry`) are stubs. `victory.py:27 VICTORY_THRESHOLD = 15` (live; `mc_v18.py:61` carries a dead `11` as a tripwire), `ACCORD_MIN`, `PS_MAX` (L1), `SUSTAIN_SEASONS`; `_qualifying_streak` is module-level state reset per campaign. One operative clause of three is dead (L1); the fallback winner at `mc_v18.py:287-297` (`held * 10 + f.L + len(f.territories)`) decides most seeded campaigns and mixes both ownership homes (L3).

### §2.12 `_architecture`, `npcs`, `ui` — not reached below the docstring layer

No `.py` in any of the three. `npc_behavior` is the declared producer of eleven Key types and the declared consumer of thirty-one (`key_graph.json`) with `authority: prose`. Nothing to compose upward from; recorded as a gap, not as a clean verdict.

---

## §3 · Where the two passes disagree

This is the section the task calls most valuable, so it is kept to the cases where the whole-tree view and the leaf-up view actually give different answers.

**3.1 · "One degree ladder" — top-down says yes, bottom-up says the campaign's conquest degree never touches it.** From the top, the guard, the owner, the extension seam and the ruling all say one ladder, with one declared hold that is campaign-unreachable (`combat_bridge` off). From the leaf, `massbattle.py:130-139` produces the string the faction layer keys Terms/Storm and Accord on, and it is a rout-and-survivors classifier the ladder never sees (L2). Both are true; the guard's own allow-list is where they are reconciled, and the reconciliation is *"not a ladder"*. **Verdict: the leaf view wins for the game.** The ruling is satisfied for every dice roll and unsatisfied for the one degree that moves the most territory.

**3.2 · The Key substrate — top-down says "55 types, 4 producers, a hub"; bottom-up says the four emitters are exactly right.** Read from the leaves, each emitter is disciplined: log-only where the caller needs a synchronous answer (`faction_action.py:352` docstring's *"a request for a computed answer stays a call; an announcement … is a Key"*), a deferred apply where the write is a consequence, no fabricated causes. Read from the top, the roster is a 55-row schema for a 5-row system and the subscriber side is wholly decorative. **Neither pass is wrong; they disagree about what the roster is for.** The bottom-up reading says the roster is a *declaration of intent* the code is honestly under-filling; the top-down reading says a declaration nothing joins to is the drift `test_key_graph.py:8-12` records. Under §0.05 the top-down reading is the one that binds: a Key type no code constructs is reference.

**3.3 · `Faction.adjust` — top-down says one writer; bottom-up says the deltas it is handed are scaled by seven private tables.** The sweep guard sees one write path and is right. The leaf sees `_MULTS_L = 20` re-declared in four modules feeding that path (D2). The whole-tree "MECHANICAL" grade is correct for the *write* and CONVENTION for the *value written*. Both passes agree once the claim is narrowed; the disagreement is about what "single owner" is quantifying over.

**3.4 · The settlements package — top-down says it is the Record primitive the SC programme should compose on; bottom-up says it is not on the loop and its expiry is decorative.** The brief, the shape spec and all three branch proposals treat `LedgerTag` as live infrastructure. From the leaf: one caller family, `ledger_sweep` reachable only through a zero-caller function, `ttl` never consulted by `ledger_has`/`ledger_get`. **Composing on it is right; assuming it *does* anything on the loop today is wrong.** The consensus branch's `Grudge` and the negotiation branch's `Debt` would be written to a ledger whose only season-boundary behaviour is absent — which the brief's §11.4 last row already records for `ttl=1` and which generalises to every `ttl`.

**3.5 · Determinism — top-down says four RNG conventions is a unity defect; bottom-up says each convention is correct in its own package and the goldens prove it.** Every leaf module is reproducible per seed and says how. The whole-tree finding (U1) is not that any one is wrong but that a fifth subsystem will pick a fifth, and the seeded goldens are the only thing that would notice — and they would notice a *change*, not a *convention*. **The passes disagree on severity, not on fact.** I grade it as a unity finding, not a defect.

**3.6 · Fieldwork, threadwork, characters, settlements, world — bottom-up says these are built, composed correctly on the owner primitives, and tested; top-down says four of the five are not on the season loop at all.** From the leaf, `knots.py`, `operations.py`, `conviction.py` are among the cleanest modules in the tree — they compose on `degree_label`, on the registry roster, on the single MS owner. From the top, the campaign never calls them: no trigger queues a fieldwork/investigation/thread scene, `generate_npc` is never called, `world.npcs` is empty every season. **Both are true, and the gap between them is the M1 gap `CLAUDE.md` §0.2 names** — done-in-code and unreachable-from-the-loop. The board (`workplan_v6_progress.yaml:43-159`) shows every juncture `not_started`/`in_progress`/`blocked`, which for once matches the top-down reading.

**3.7 · The session's proposals — bottom-up says each branch adds one object and composes on ruled-in primitives; top-down says all three compose on the same two things the tree has not built.** From inside each document, the N-line hunts are real and the reuse ledgers are honest. From the whole tree: negotiation, inquiry and consensus each write their durable outcome to `Settlement.ledger` at `place` (`02:372`, `03:434`, `04:387` tables) — the ledger of §3.4 — and each reaches production only through `build_contest`'s missing `armature=`/`rng=` and a `scene_dispatch` arm that does not exist (`03_INQUIRY.md:390` names the arm; `04_CONSENSUS.md:222` relies on the prebuilt-`Venue` path, which `scene_dispatch` never takes — it passes `venue=proceeding` by name at `:300`). **The three branches are paper for the same two reasons, and neither is in the branches.** The reconciliation's blocking list (B1-B5) is about the documents; this is about where they land.

---

## §4 · The deduplication ledger — every rule that lives more than once

| # | the rule | home 1 (owner or first) | other homes | guarded? | load-bearing on |
|---|---|---|---|---|---|
| 1 | the degree ladder | `engine/autoload/dice_engine.py:227 degree_from_net` | `systems/mass_battle/sim/resolution.py:104 compute_degree` (re-impl); `systems/combat/combat_engine_v1/core.py:57 degree` (pre-ruling, HELD); `systems/mass_battle/sim/massbattle.py:130-139` (survivor-ratio bands, L2); `combat_engine_v1/workbench/probabilities.py:32` (analytic, apparatus) | ladder equivalence yes (`test_degree_ladder_single_owner.py:312`); the hold is declared (`:265`); the survivor bands are enrolled as *not a ladder* (`:394`) | GAME |
| 2 | the d10 face rule (1→−1, 7-9→+1, 10→+2) | `dice_engine.py:153 _die_result` | `mass_battle/sim/resolution.py:37-54 roll_pool` (own loop) | no parity test found (search: `_die_result` / `roll_pool` cross-references in `tests/valoria`, `engine/tests`) | GAME |
| 3 | σ soft-cap `M·tanh(x/M)` | `sigma_leverage.py:141 soft_cap` (`M_MAX:104`) | `mass_battle/sim/resolution.py:209 _sigma_softcap` (`m=1.5` literal) | **no** — `test_degree_boundary_epsilon.py` exercises the copy alone (D1) | GAME |
| 4 | μ-shift `eff·σ·√N` | `sigma_leverage.py:190 net_boost` | `mass_battle/sim/resolution.py:221 _sigma_net_boost` | **no** (D1) | GAME |
| 5 | per-die σ = 0.800 · μ = 0.40 | `dice_engine.py:174-175` | `sigma_leverage.py:77 PER_DIE`, `:112-113 MU/SD_PER_DIE`, `resolution.py:227 _SIG_PER_DIE` | partial (`test_sigma_leverage_parity.py` pins the engine pair; nothing pins the mass-battle copy) | GAME |
| 6 | TN = 7 | `sigma_leverage.py:91 TN_STANDARD` | ten more (§1.4 D4) | inert by `_require_tn7:182` | — |
| 7 | `MULTS` granularity | `game_state.py:74` | `crown_initiative.py:33-35`, `council_solmund.py:24`, `excommunication.py:35`, `absolution.py:27-28` | no | GAME (D2) |
| 8 | Persuasion-Track bands 9/7/3/1 | `resolver.py:81-96 PersuasionTrack.resolve` | `contest_legacy_stub.py:67-71 PERSUASION_*` (consumed by `parliamentary_vote.py:45,200`); `faction.py:68 band_of` (±0.06 variant) | no (values agree today — §5) | GAME (the §10 vote) |
| 9 | continuous Accord → canonical tier | `engine/substrate/canon_buckets.py:38 canonical_accord` | `systems/settlements/sim/settlement.py:120` (`floor`, divergent — L8); `game_state.py` `ACCORD_MAP` is the forward table | no | latent |
| 10 | territory ownership relation | `Territory.owner` (`game_state.py:234`) | `Faction.territories:124`; `Settlement.owner_faction` (`registry.py:60`) | no (`parliamentary_transfer.py:347-360` records one past divergence) | GAME (L3) |
| 11 | Legitimacy / Mandate | `Faction.L` (`game_state.py:110`) | `Settlement.legitimacy` (`registry.py:74`, inert); `Territory.entry_terms_l_seed` (`faction_action.py:520`, write-only); SC `faction.Faction.mandate` (`faction.py:13`) | no | GAME |
| 12 | the store router (`world.<store>` if world else module dict) | — (a pattern) | `coherence.py:57`, `conviction.py:85`, `beliefs.py:105`, `knots.py:159`, `npe.py:110`, `insurgency_pipeline.py:57,63`, `infrastructure.py:115`, `temperaments.py:89`, `threadcut.py:63`, `co_movement.py:69`, `registry.py:166` — **twelve** | n/a | PORT (twelve fallbacks a Godot port must not carry) |
| 13 | Key id mint | — | `echo_transport.py:318 _echo_key_seq`; `faction_action.py` `_battle_key_seq`; `parliamentary_transfer.py` `_parl_key_seq` | no | PORT (K5) |
| 14 | Key-emission safety wrapper | `faction_action.py:352-427 _emit_battle_concluded` | `parliamentary_transfer.py:181-246 _emit_public_governance_transfer` (verbatim shape) | n/a | — |
| 15 | `restructure_ledger.md` parser | `tools/pathres.py:99 _ROW_RE`, `:198 load_alias_map` | `tools/broken_dependency_checker.py:119`; `skills/valoria-vector-audit/scripts/vector_audit.py:423`; `workbench.py:73` | `CLAUDE.md:733` names the hazard | PROCESS (known) |
| 16 | pool floor | min-1: `dice_engine.py:196` · `sigma_leverage.py:269,282` · `resolution.py:37`; min-5: `core.py:47 POOL_FLOOR` · `primitives.py:211 Pool.size` · `combat/sim/combat.py:48` | two distinct rules, three homes each | no | GAME |
| 17 | Ob from a score | `crown_initiative.py:189` `floor(L/2)+1` | `tribunal.py` `L·0.5`; `parliamentary_transfer.py:325` `L+2` | pinned **as divergent** (`test_faction_obstacle_conventions.py:36-71`) | RULING (L6) |
| 18 | coherence cost of a thread op | `threadwork/sim/operations.py:122 COHERENCE_COST_BY_SCALE` (by scale) | `engine/cross_scale/handoff_rules.py:83 _ts_to_coherence_cost` (by TS band; **zero consumers** of `coherence_cost` — grep) | no | dead twin |
| 19 | settlement stat bounds 0-5 | `descriptors.SETTLEMENT_STATS` (`descriptors.py:66`, read by `echo_transport`) | `registry.py:50 STAT_MIN/MAX`; `settlement.py:40` | no | — |
| 20 | Accord bounds 0.5-7.0 | `game_state.py:248 adjust_accord` literal | `:148 UNDECLARED_FLOOR/CEILING`; `descriptor_registry.yaml:90 territory_stats` declares only `fort_level` | no | — |

**Count: 20 rules with more than one home.** Three were already named in `CLAUDE.md` (rows 1's hold, 15, and the `pathres` prefix hazard which is a *behaviour* of row 15's owner rather than a duplication); **seventeen are new to this reading**, of which rows 2, 3, 4, 7, 10 and 16 are load-bearing on every seeded campaign and unguarded.

---

## §5 · Attacks I ran that FAILED, reported as failed

| attack | result | trail |
|---|---|---|
| "Payload/schema mismatch is systemic across the live Key types" | **FAILED.** All five constructible types carry every `required_payload_fields` entry | script over `key_types.json` vs the four builders; K4 |
| "Some faction scalar has a second writer" | **FAILED.** Zero bare or compound assignments to `L/Sta/W/I/Mil/intel` outside the dataclass | regex over `engine/`+`systems/` non-test; corroborated by `test_faction_write_sweep.py:167`'s own AST sweep |
| "`world.clocks['CI']` has a second owner" | **FAILED.** `excommunication.py:167` routes through `apply_ci_delta`; `ci_track.py:177` is the only assignment | grep `clocks['CI']` |
| "The Persuasion-Track thresholds disagree between the resolver and the legacy stub" | **FAILED.** `resolver.py:91-95` (`≥9, ≥7, >3, >1`) and `contest_legacy_stub.py:67-71` (`≥7 win, ≤3 loss, ≥9, ≤1`) partition the track identically on integers and on reals (at `t=3` both say B-decisive/failed) | read both |
| "The contest's global-RNG reseed leaks into later draws" | **FAILED.** `scene_dispatch.py:297-303` saves and restores `random.getstate()`; `rngsource.using:55` restores on exit; `combat_bridge:131` derives a child | read all three |
| "The combat engine's held pre-ruling ladder reaches the campaign" | **FAILED.** `combat_bridge` is behind `DISPATCH_COMBAT_BRIDGE` default OFF and nothing queues a `combat` scene; with the flag off the branch calls the deprecated `combat/sim/combat.py`, whose `_degree:160` is routed through the owner — and is equally unreachable | `scene_dispatch.py:225-277`, grep `queue_scene("combat"` |
| "`engine/` still imports `systems/` somewhere" | **FAILED.** Every engine→subsystem reach I found goes through `composition.require` (28 roles) or the one declared path seam (`combat_bridge.py:96`) | read `composition.json`, every `engine/` module |
| "`mass_seizure`'s missing `Faction.territories` update is live" | **FAILED (latent).** Zero production callers of `resolve_mass_seizure` or `attempt_mass_seizure_declaration` | grep; `test_mass_seizure_accord_write.py` header agrees |
| "`settlement.py`'s `floor` Accord derivation is live" | **FAILED (latent).** `compute_settlement_state` has no caller outside its own module; the registry path is preferred when the settlement is registered | grep |
| "`scene.contest_resolved`'s emitted payload violates its registry `outcome` enum" | **FAILED.** `_OUTCOME_BY_DEGREE["contest"]:114` emits only `initiator_win/compromise/target_win`, all in the declared enum (`key_types.json:954` region); `stalemate` is declared and never emitted, which is not a violation | read both |
| "`Faction.adjust`'s registry floors are unreachable for a live stat" | **PARTLY — not new.** `intel` is unreachable (`MULTS` has no key); the module says so at `:153` docstring | read |
| "The consensus branch's `INSTITUTIONAL_MODES` venue is reachable through `build_contest`'s prebuilt-Venue path from production" | **FAILED — and it is a finding against the branch.** `build_contest:137` does accept a prebuilt `Venue`, but `scene_dispatch.py:300` calls `build_contest(parts[0], parts[1], venue=proceeding)` with a **string** from `PROCEEDINGS`; no production caller passes a `Venue` object | read `scene_dispatch` + `wrapper` |

---

## §6 · `[NULL:]` rows, each with its evidence

- **[NULL: no second writer of the six faction scalars]** — regex `\.(L|Sta|W|I|Mil|intel)\s*[+\-*]?=[^=]` over `engine/`+`systems/` non-test, excluding `self.`: zero hits; every write is `.adjust(` (31 sites, 10 files).
- **[NULL: no `Key(` inside `systems/social_contest/`]** — grep `\bKey\(` non-test: four sites, none in that package.
- **[NULL: no payload/schema violation among the five constructible Key types]** — K4 script.
- **[NULL: no writer of `clocks['Turmoil'|'PI'|'Strain'|'IP']`]** — grep over both trees non-test: zero (this null is L1's evidence).
- **[NULL: no assignment to `Settlement.owner_faction` after world-gen]** — grep `\.owner_faction\s*=`: zero.
- **[NULL: no runtime subscriber for `scene.contest_resolved`]** — `articulation.py:116-129` roster read; the type is absent.
- **[NULL: no consumer of `handoff_rules` `coherence_cost`, of `knots` `composure_damage`, of `beliefs` `momentum_delta`]** — grep each identifier outside its defining module: zero.
- **[NULL: no production caller of `succession`, `coalition_vote`, `agon_harness`, `resolve_mass_seizure`, `compute_settlement_state`, `aggregate_to_province`, `process_treaty_expirations`, `resolve_stay_lift`, `generate_npc`, `form_knot`, any `threadwork.attempt_*`]** — grep each in `engine/` and `systems/` outside its own module and tests: zero.
- **[NULL: no parity test between `mass_battle/sim/resolution.py`'s σ pair and `sigma_leverage`]** — grep `sigma_leverage|net_boost|soft_cap` in `tests/valoria/test_degree_boundary_epsilon.py` and `test_mass_battle_byte_exact.py`: zero; `engine/tests/test_sigma_leverage_parity.py` compares the engine module to two frozen oracles, not to mass battle.
- **[NULL: no `Faction(` construction in `insurgency_pipeline.py`]** — grep: zero (L5).
- **[NULL: no `engine/` module imports a `systems.*` name]** — read of every `engine/` module; corroborated by `test_engine_does_not_import_systems.py`.

---

## §7 · What would make this reading wrong

1. **A writer of `Turmoil` I could not see.** L1 rests on a grep for assignments to `world.clocks[...]` in Python. If Godot, a test fixture, or a `params` override feeds the clock, the clause is live there and dead only in the Python campaign. A one-line check: instrument `World.clocks` for `'Turmoil'` writes across one seeded campaign.
2. **The survivor-ratio bands being ruled as a deliberate second grammar.** L2 treats "one degree ladder" as applying to the degree `faction_action` consumes. If Jordan's 2026-09-03 ruling in PR #362 §C.4 (*"the degree is READ OFF THE SUBSYSTEM"*, `:616-621`) is read as licensing a subsystem to report bands from whatever it can distinguish, then `massbattle.py:130-139` is the rule working, not breaking — and the finding becomes "three uncited thresholds", which is smaller.
3. **`mass_seizure` or `compute_settlement_state` acquiring a caller.** Every "latent" in L3 and L8 becomes live the day either is wired, and nothing in the tree would announce it.
4. **A parity test for the mass-battle σ pair that lives somewhere I did not search.** D1's "unguarded" is a null over `tests/valoria` and `engine/tests`. `tests/sim/` was not searched; if a frozen oracle there pins `_sigma_net_boost` against the engine, D1 shrinks to "guarded from the wrong side".
5. **The four unread subsystems.** `npcs`, `ui`, `_architecture` and the design side of `articulation`/`victory` were not read. If any of them contains a mechanism rather than prose — a YAML the engine loads — then the "hub, not a bus" verdict (K1) undercounts producers. My check was `.py` files only; a data-driven producer would be missed.
6. **The interiors I did not read.** ≈10,300 lines of combat and mass-battle interior could hold a fourth ladder, a fifth RNG convention, or a direct `world` write. The guard at `test_degree_ladder_single_owner.py:452` scans for band literals tree-wide, which covers the first; nothing covers the other two.
7. **My own line numbers.** Every anchor was re-derived by `grep -n` on the working tree at HEAD `7a23b831` after reading. If the tree moves under this document, the symbols survive and the numbers do not; a reader should trust the symbol.
8. **Self-review bias.** This reading was directed to include the session's own proposals and I have graded them (§3.7) more leniently than the reconciliation did — because I read them for whole-tree fit rather than for their own arithmetic. An independent reviewer would re-run B1-B5 against this document's L2/L3/K5 and ask whether any branch inherits them; I believe consensus's `Precedent` write and negotiation's `Record` both inherit §3.4's decorative-`ttl` finding, and I have not proved it.

---

*End. One file. Nothing else was created or edited.*
