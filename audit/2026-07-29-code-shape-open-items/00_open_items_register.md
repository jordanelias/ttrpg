# Code-Shape Open-Items Register — I/O · Keys · Centralization · Scales · Orphans/Gaps/Interdependencies

## Status: REGISTER (read-only collation; rules nothing) — ED-IN-0091, 2026-07-29

**What this is.** The consolidated register of every OPEN item across the recent audit corpus that
concerns I/O contracts, the Key substrate, centralization (single-owner), scales/transitions, and
code shape (orphans, gaps, stubs, interdependencies) — with emphasis on code. It feeds
`01_orchestration_plan_v1.md` (the Sonnet/Opus orchestration plan over these items).

**Method.** Four parallel extraction lanes over: the vector audits
(`2026-07-21-repo-state-vector-audit`, `2026-07-26-mass-battle-vector-audit` + fable audit,
`2026-07-14-governance-vector-audit`), the wiring/scale audits (`2026-07-17-mc-wiring-coverage-audit`,
`2026-07-23-combat-engine-wiring-audit`, `2026-07-14-scale-chain-and-decision-surface-map`,
`2026-07-14-gameplay-subsystem-observatory`, `2026-07-14-holistic-unification`,
`2026-07-13-cross-scale-governance-grounding`, `2026-07-07-unaddressed-areas-audit`), the machine
registries (`module_contracts.yaml`, `apparatus_registry.yaml`, `PROPOSALS.md`/`DECISIONS.md`,
`ci_checks_registry.yaml`, the 2026-07-26 `structure_audit` run), and the editorial ledgers +
lane handoffs + a live-tree stub census. Then a working-tree adversarial spot-check pass
(2026-07-29) on the load-bearing claims — corrections from that pass are marked **[verified]**
or **[corrected]** below. Old `sim/`-era paths from pre-restructure audits are given at their
current homes.

**Lane partition (2026-07-29, Jordan directive).** Repo work runs as multiple simultaneous
sessions, with two lanes carved out to dedicated sessions executing their own merged plans:
**MB** → `audit/2026-07-26-mass-battle-fable-audit/03_execution_plan.md` (ED-MB-0045 plan v2,
as corrected by PR #250/G12); **PC** →
`audit/2026-07-26-combat-balance-customization-state/combat_execution_plan.md` (PR #249,
batches E0–E3 + §13 orchestration). Every MB/PC-lane row below is therefore **indexed here but
executed there** — marked **→ MB plan ⟨track⟩** / **→ PC plan ⟨batch⟩**. Items this program
identified that were NOT already in those plans have been physically appended to them as
**MB plan §12** and **PC plan §15** (this PR) — no routed item exists only as a pointer. The
orchestration plan (`01_…`) touches no MB- or PC-owned *code* file.

**Class codes** (dispositions, not rulings):
- **M** — mechanical; agent-executable now, no design decision.
- **B** — build; agent-executable, design/canon already exists (may need a golden re-record, flagged).
- **J** — needs a Jordan ruling before code moves.
- **D** — deliberately deferred by an existing ruling or plan; do NOT act (listed so sweeps don't re-file it).

**Spot-check corrections (2026-07-29).** Three audit claims changed state and are recorded here so
downstream work doesn't chase them: (1) `mc_v18`'s silent `except Exception: pass` (07-17 D7) is
**FIXED** — errors now surface to stderr (`engine/mc_v18.py:97-102`); (2) `handoff_rules.py`'s three
apparent importers are docstring mentions only — the **import-orphan claim stands**; (3) the
dispatch combat branch now exists but routes to the DEPRECATED `systems.combat.sim.combat`, not
`combat_engine_v1` — the canonical resolver still has zero path from the loop (see OI-01).

---

## §1 · Orphans & unreached code (Priority-1 surface)

| ID | Item | Evidence | Paths | Class |
|---|---|---|---|---|
| OI-01 | Campaign loop cannot reach the canonical combat resolver: `scene_dispatch`'s combat branch calls DEPRECATED `systems.combat.sim.combat.resolve_combat_round`; `combat_engine_v1` (17 modules, CANONICAL) is an import-orphan from the loop; branch also defers on "no personal combat actors" context gap **[verified 07-29]** | 07-17 D-corr · 07-23 wiring · 07-07 C-REACH-2 · structure_audit 07-26 | `engine/cross_scale/scene_dispatch.py:137-143`, `systems/combat/combat_engine_v1/wrapper.py` | B |
| OI-02 | Field Investigation has zero live dispatch path; `fieldwork.py`/`investigation.py` are full `NotImplementedError` stubs (3 raises each) | ED-916 · 07-14 NG-2 · stub census | `engine/cross_scale/scene_dispatch.py:214`, `systems/fieldwork/sim/{fieldwork,investigation}.py` | B |
| OI-03 | `compute_accord_echo` — the bottom-up settlement→province Accord write source — has zero callers **[verified]** | 07-14 NG-1/GAP-DIR-2 · Tier-1 #1 | `engine/cross_scale/domain_echo.py` | B |
| OI-04 | `parliamentary_transfer.propose_transfer` never called → territory is a one-way ratchet (lost territory unrecoverable) **[verified]** | 07-14 Tier-1 #2 · GAP-A1 | `systems/factions/sim/parliamentary_transfer.py` | B |
| OI-05 | `generate_npc` zero call sites → `world.npcs` permanently empty, NPE no-ops every season; the F7 golden asserts `npcs_generated == 0` and self-documents needing an update when wired **[verified]** | 07-07 U-2 · 07-17 D6 | `systems/world/sim/npe.py`, `engine/tests/test_f7_smoke_oracle.py:127` | B |
| OI-06 | `handoff_rules.py` (the curated 8-rule cross-scale dispatcher) is an import-orphan — its three "importers" are docstring mentions **[corrected: claim stands]**; runtime fallback emits "No §3 rule defined… transition invalid"; `scale_transitions_v30` §3.3 Personal→Contest is an EMPTY heading | GAP-DIR-4 · ED-IN-0049 (J) · DECISIONS P2 | `engine/cross_scale/handoff_rules.py` (+`:231`), `systems/_architecture/scale_transitions_v30.md:51` | B (+J §3.3) |
| OI-07 | Wired-but-vacuous world chains: `world.knots` and `world.settlements` have the same never-populated shape as `world.npcs`; settlement registry module (`registry.py`, G1) is built but World wiring is absent | 07-17 D6 · 07-14 churn map §5 | `systems/fieldwork/sim/knots.py:172`, `systems/settlements/sim/registry.py:111`, `engine/autoload/game_state.py` | B |
| OI-08 | Key pub/sub has zero subscribers — `articulation` (the intended reader) is a stub (3× `NotImplementedError`); only Key consumption is the narrow paired `apply=` closure; ED-IN-0073 Q1–Q4 qualitative-rendering layer unbuilt; `Belief.statement` read by nothing | 07-17 §2 · ED-IN-0073 | `engine/cross_scale/articulation.py`, `engine/mc_v18.py` | B |
| OI-09 | `engine.autoload.npc_ai` — stub (2 raises) and import-orphan; listed as a Stage-2.5 Layer-B precondition | stub census · structure_audit | `engine/autoload/npc_ai.py` | B |
| OI-10 | 8 placeholder-named FA/MB sim modules are import-orphans AND unresolved `placeholder_names.yaml` rows (`varfell_mandate_action`, `varfell_territorial_acquisition`, `altonian_reinforcements`, `infrastructure_reclamation`, `home_sanctuary`, `hafenmark_equipment`, `charter_liberties`, `tactic_cards` + `mass_seizure`) | structure_audit · DECISIONS P2 naming | `systems/factions/sim/*`, `systems/mass_battle/sim/*`, `registers/placeholder_names.yaml` | B (stub-wire) + J (names) |
| OI-11 | Two disjoint mass-battle code graphs: `tests/sim/mass_battle/` (28 modules, ~10.5k LOC, all current development) has zero production importers and imports nothing from `engine/`/`systems/`; the campaign resolves battles on the stale wired tree (`systems/mass_battle/sim/` via `faction_action.py:349`). Fork (declare / adapter / promote) is Jordan's | ED-MB-0043/0045 · 07-17 D5 | both trees | **J → MB plan §7 fork 1** |
| OI-12 | Other genuine import-orphans (verify-before-wiring per the tool's own caveat): `systems.characters.sim.companion`, `systems.overview.sim.{ip_track,rs_track}` (both also stubs), `systems.threadwork.sim.{co_movement,collective,opposing,rendering}`, `systems.world.sim.{miraculous_event,restoration_movement}`, `systems.settlements.sim.{settlement,temperaments}`, `systems.social_contest.sim.parliamentary_stay`, `engine.autoload.registry` | structure_audit 07-26 (142-row list, CLI/`__init__` noise excluded) | as named | B |
| OI-13 | Dead PC-engine code: 6 vestigial functions (`core.effective_ob`, `combat_systems.{can_choke,stamina_max,conc_max}`, `ability_primitives.kit`, `traditions.profile`) + dead `Combatant.ready` field; 2 separation reasons (`beat_exhaustion`, `collapse`) never fire; `seize`/`vorschlag`/`sen_no_sen` labeled "live" but consumer cut 2026-06-05; M9 unreachable authored elements | 07-23 wiring §1.3/§2.1/§3.2 · PR #249 M12/M9 | `systems/combat/combat_engine_v1/*` | **→ PC plan E0 (M12) / E2 (M9)** |
| OI-14 | Dead MB-tree code: `provenance.py` 0 importers with stale `loc` fields cited as canon; `reform_check` canon-required (PP-241) yet permanently dark; `_find_contacts_field`, `PC_FACING_MODEL` family, `COMMAND_SIGMA_ENABLED` dark; armour catalogue explicitly unwired (ED-MB-0008, docs-only per E3) | ED-MB-0045 S2.4/S2.5 · C6 | `tests/sim/mass_battle/*` | **→ MB plan B3/E3** |
| OI-15 | Orphaned tools: `build_audit_registry_backfill.py`, `geography/jsx_to_canonical.py`, `measure_stamp_false_positives.py`, `observability/npc_audit_report_gen.py` (`orphaned_no_cli`); plus a registry-generator inconsistency (`sim_harness/harness.py` has `invoked_by: []` but `orphaned: false`) | apparatus_registry | `tools/*` | M |
| OI-16 | `tools/registry.py` facade has zero production consumers; `references/head_pointers.yaml` + `docs/REPO_MAP.md` (converged highest-leverage pointer artifacts) do not exist | 07-14 unification §5/§6 | `tools/registry.py` | B |

## §2 · Stubs (the explicit-gap class)

| ID | Item | Evidence | Paths | Class |
|---|---|---|---|---|
| OI-17 | The "Pass 2l armature stub" class: ~20 mechanically-stamped modules that unconditionally `raise NotImplementedError` — `charters/factions` (charter_liberties, infrastructure_reclamation, home_sanctuary, varfell_×2, hafenmark_equipment), `fieldwork` (fieldwork, investigation), `overview` (rs_track, ip_track), `world` (miraculous_event, restoration_movement), `characters` (companion), `threadwork` (rendering), `mass_battle` (altonian_reinforcements — **MB-owned file: conversion handed to the MB session**, same stubwire primitive), `engine/cross_scale/articulation.py`, `engine/autoload/npc_ai.py`. A systemic class, not one-offs (CLAUDE.md §0.1 #5) | stub census 07-29 · 07-07 C-STUB | 61 `NotImplementedError` hits, live trees only | B |
| OI-18 | Contest GAMES router: `agon` WIRED; `consensus`/`negotiation`/`inquiry` STUB rows; `DyadicMode`/`NegotiationMode`/`CeremonialMode.play` scaffold-only; build gated on SC stage 4 + P0 docket (ED-SC-0003..0005) | GAP-C4 (07-13) · stub census | `systems/social_contest/sim/contest/{wrapper.py:199-204,modes.py:328-334}` | B (self-flag) / J (build) |
| OI-19 | Partial `NotImplementedError` branches: `tribunal.py:149` (§7 Asymmetric Proceeding), `treaty.py:107`, `contest/dictionaries.py:710`, `resolver.py:51` (abstract base — benign) | stub census | as named | B |
| OI-20 | `faction_politics` has ZERO sim representation (not even a stub) despite a 1115-line CANONICAL doc; its contract has no `state:` block (Standing ladder, coup/succession undeclared) | 07-07 C-STUB-6 · GAP-K1 | `references/module_contracts.yaml` (faction_politics) | B |

## §3 · Keys & I/O-contract defects

| ID | Item | Evidence | Paths | Class |
|---|---|---|---|---|
| OI-21 | Fabricated Key row: `mass_battle` emits `scene_outcome.battle_concluded` ("substrate verbatim") alongside the real `scene.battle_concluded` — a family name entered as a type. Corroborated by 6 independent instruments **[verified in tree]**. NOT a one-line hygiene fix: needs_jordan ⇒ ED-1094 merge-ratification with ledger flip + alias delete + artifact regen, per E1 | **ED-MB-0010** (open, needs_jordan since 07-13) | `references/module_contracts.yaml:473` | **J → MB plan E1** ("cheapest independent win") |
| OI-22 | Dangling emits, canon-grade: `scene.combat_resolved` + `scene.combat_felled` (declared consumers npc_behavior/faction_state/articulation never wired — GAP-C2); `env.crisis` (2 emitters, zero consumers anywhere, none named in prose — GAP-C4) | structure_audit · 07-14 | `references/module_contracts.yaml` (personal_combat, peninsular_strain) | B (combat pair) / J (env.crisis) |
| OI-23 | `mass_battle` contract declares `consumes: []` / `state: []` — a battle takes no typed inputs and persists nothing; formula/pointer audits structurally blind to MB. Remediation **deliberately deferred** until Track B settles what state a battle owns; honest `status:`/`gap_notes` ships now | ED-MB-0043 **[verified]** | `references/module_contracts.yaml:465-486` | **D → MB plan E6** |
| OI-24 | Contract truth debt: npc_behavior stale gap_note + self-loop consume edges (C-KEY-6, partially fixed 07-07 — residue check); `doc:` points at a Key-silent doc while the real Key-sequencing spec (`political_dynamics_keys_migration_v30.md`) sits in `sources:` (C-KEY-2); 9 modules carry `emits:` never validated against doc prose (C-KEY-1: only faction_state has genuine doc-native emit coverage) | 07-07 C-KEY cluster | `references/module_contracts.yaml` | M/B |
| OI-25 | Silent emitters (zero Key integration in CANONICAL docs + contracts): `settlement_layer` revolt/auto-capture gates (`g_ord0`/`g_def0`), `ci_political`, `victory` era/occupation transitions, `territorial_piety` (in-0/out-0 INERT) | **ED-IN-0014** · GAP-E1/E2 · C-KEY | respective docs + contracts | B |
| OI-26 | `personal_combat`'s internal `_emit()` trace vocabulary (~15–25 kinds) never mapped to the 4 canonical `scene.combat_*` Key types — edits PC-owned files, so **→ PC session** (note PC plan §12: `wrapper.py` has never been audited — this mapping is a natural rider on that pass); the Key-registry half of the mapping (IN side) lands with OI-22's consumers | 07-07 C-KEY-3 · PC plan §12 | `combat_engine_v1/{wrapper.py,state_graph.py}` | B **→ PC session** |
| OI-27 | Registry/type defects: `meta.cascade_cluster_event` cited by CANONICAL articulation trigger #9 but never registered (C-KEY-8); core-five `scene.*` interaction types have zero Tier-2/3 rendering path (C-KEY-9); `state.opinion_revised` registry text contradicts the §3.1 table; zoom-trigger tables cite no `type_id` (C-KEY-10); articulation's §3.1 ruleset omits `scene.battle_concluded`/`scene.investigation_resolved` despite declared consumption (ED-IN-0004) | 07-07 · ED-IN-0004 | `key_type_registry_v30.md`, `articulation_layer_v30.md`, `scale_transitions_v30.md` | B/J mix |
| OI-28 | `causes[]` (diagonal direction) has ZERO executable instances corpus-wide (substrate self-reports ~15%; actual 0); `targets[]` populated in exactly one live emitter (`echo_transport.py:146`); 20 down-seam `!A6` annotation-debt instances | GAP-DIR-1 · C-KEY-5/4 · GAP-D1..3 | `engine/substrate/keys.py`, emitters | B |
| OI-29 | Dual-emit attribution unresolved: `scene.dialogue`, `mechanical.scene_entered`, `state.belief_revised` each claimed by multiple modules — single canonical emitter unassigned | GAP-J3 · DECISIONS P1 | module contracts | J |
| OI-30 | Pointer debt: true keyed rate 21.8% (12/55), not the 52.7% headline; ~26–28 identifiers genuinely unresolved (Wounds, Turmoil, Accord, Poise, Initiative, `engine_clock` season counter, …) — Category B (register the scalars) is real work; Category C2 (are npc beliefs/concerns/projects registry quantities) is a call | 07-14 unification §3 · ED-IN-0059 | `references/descriptor_registry.yaml` | B (+J for C2) |
| OI-31 | Off-Keys writers: `parliamentary_vote` writes `Faction.L` directly on Total Victory, restoration promise unimplemented (flips ~72% of campaign winners if fixed — held); J-36's six off-bus writers class ([VERIFY] pass still deferred); ED-WR-0003 hard-coded `private_observers` at 6 emit sites | 07-17 D3 · workplan T1 J-36 · ED-WR-0003 | `systems/social_contest/sim/parliamentary_vote.py:213` etc. | J (D3) / B (WR-0003) |
| OI-32 | Unowned/dead state: `MS` clock ticked but no contract module declares ownership (GAP-F1, mechanically determinable); `Turmoil` write-dead → victory gate trivially satisfiable (held, balance-affecting); `VICTORY_THRESHOLD` dead constant; `game_state.py:101` field unread/unwritten | 07-14 GAP-F1 · 07-17 D1 · C-EMERGE-8 | `systems/victory/`-adjacent sims, `engine/autoload/game_state.py:101` | M (MS, const) / J (Turmoil) |
| OI-33 | `settlement_layer` L/PS derivation lacks a `bucket:` tag — derived_value (F1-guarded) vs writable track undecided; Mandate-feedback F1 coverage unclear | 07-14 unification §7 · D15 | `references/module_contracts.yaml` | J |
| OI-34 | ED-IN-0003: Convergence Markers (8) have no runtime detector, no Key type, no module contract, no sim module | ED-IN-0003 | `arcs/registers/arc_register_events.md` | B |

## §4 · Scales & transitions

| ID | Item | Evidence | Paths | Class |
|---|---|---|---|---|
| OI-35 | `scale_signature` enum is `(personal, settlement, territory, peninsula)` — province/duchy/country (B12-RULED hierarchy) unrepresentable; validator raises on non-members **[verified `keys.py:62`]** | 07-14 NG-1/X-5 · B12 ruling | `engine/substrate/keys.py:62,355-359`, `key_substrate_v30.md:57` | J (confirm) → M |
| OI-36 | Master finding: only 2 of 7 Key-delivery directions live end-to-end (lateral + bottom-up echo core); diagonal (causes[]) unreached, vertical-up dispatcher orphaned (OI-06), temporal decay deferred (OF-3), Accord leg uncalled (OI-03) | `directional_coverage_v1.md` | cross_scale + substrate | B (roll-up) |
| OI-37 | The L/PS pipeline (#136, Mandate/Legitimacy/Popular-Support loop) is fully SPEC-ONLY: `Settlement.legitimacy`/`popular_support` never read or written; `lps_inert_check` 100/100 red; sim substitutes scalar `Faction.L`. SE handoff: "single highest-priority open item in this entire thread" | 07-14 Tier-1 #1 · ED-FA-0004 · HANDOFF_SE | needs `systems/settlements/sim/` legitimacy owner | B (spec exists) |
| OI-38 | No event_deck runtime: 28-card Goldenfurt deck is prose-only — no card store, predicate evaluator, or Π tracker (M2 critical path); sim_harness's 13-card event-deck engine exists as harness-side prototype only | 07-14 churn map §3/§5 · HANDOFF_SE | none (unbuilt) | B |
| OI-39 | NPC ambition-tick absent from the Accounting cascade — dossier schema fully specified, advancing code nonexistent | 07-14 churn map §1/§5 | none (unbuilt) | B |
| OI-40 | Scale-vocabulary divergence: 4 vocabularies unreconciled (cross-scale locality metric EXPLORATORY) — IN half; `Mass Battle`/`Mass Combat` token scale-class mismatch + zero MB patch-register coverage + `mass_combat.md` describing a different game — MB half | A8 · F6/F7 (ED-MB-0043) | contracts, token registers | B/M (IN half) · **→ MB plan E4/E5/E8** (MB half) |
| OI-41 | Design-blocked cross-scale mechanics: caste cascade unwired (GAP-F2); Church/CI ideological-consent axis not lifted (GAP-G1); insurgency pipeline dead-by-construction; fracture resolution mechanics orphaned (`fractional_province_ownership`); §5.2 claiming/§5.3 chain-bypass RULED but zero armature binding; territorial-tier propagation (`scale_hierarchy_v1.md` §6) un-started — dams NS3 | 07-13 gap register · 07-14 unification §5 | design docs + future sims | B/J mix |
| OI-42 | Cross-tick convergence of Key propagation unproven (per-tick/per-cascade only; bounded-oscillation D.6 risk); `decay()` fork OF-3 unruled — event-builds accumulate without entropy | GAP-DIR-5 · propagation_spec §5 | `systems/_architecture/propagation_spec_v1.md` | D/J |
| OI-43 | ED-1051: `engine_clock` doc:null — the temporal spine; the pointer-flip to `propagation_spec_v1.md` is the sole remaining T0 blocker on M1 and the GO Gate-0 entry; the other 8 doc:null modules (audit, domain_actions [ED-FA-0002], game_director, npc_memory, scenario_authoring, scene_slate, scene_timer, settlement_economy [retire-candidate, GAP-K2]) + `campaign_architecture` stub module (retire-candidate, GAP-K3) | ED-1051 · structure_audit · GAP-K2/K3 | `references/module_contracts.yaml` | J (1051 flip) / B (homes) / J (retires) |

## §5 · Centralization / single-owner violations

| ID | Item | Evidence | Paths | Class |
|---|---|---|---|---|
| OI-44 | PC pool formula duplicated with divergence: `combatant.pool = max(5, history+6)` (no rounding) vs `core.resolution_pool = max(5, int(round(history))+6)` — latent while History is integer | 07-23 §4.2 | `combatant.py:118`, `core.py:30-32` | M **→ PC session** |
| OI-45 | The ≈8.0 percussion-authority anchor triplicated (`core.PERC_AUTH_REF`, `weapon_physics.PERC_CAP`, `config.ADEF_PERC_REF`) with nothing enforcing equality; `damage()` blunt branch re-hardcodes `3.0*(perc/8.0)` + int/float default mismatch | 07-23 §4.2 | `core.py:142,251,264`, `weapon_physics.py:54`, `config.py:62` | M **→ PC session** |
| OI-46 | `config.py`'s "all tunable coefficients in ONE place" claim false — ~60+ SIM-CALIBRATE/FIAT knobs as module globals (**PC plan E0/M15 owns exactly this: 279 unowned literals, vocabulary ownership**); `sel_*` positional tuples manually unpacked at 3 sites; `point_concentration` dual read paths; `capabilities.py` name-keyed second truth (watch, quarantined to diagnostics) | 07-23 §4.2/§4.4 · PR #249 M15 | `combat_engine_v1/*` | **→ PC plan E0 (M15)** / D (capabilities watch) |
| OI-47 | MB engine: seven duplicated rules with no owner — combat-pool ×2 (already diverged), facing/arc ×2, stamina stores ×3 with two live drain laws, morale dialects ×3, damage laws ×2 (canon fork), health ×2, movement dual-owned; TEN per-cell maps with no key-set invariant; `check_drift` re-keys 1 of 10; float-epsilon guard at producer not consumer. Remediation = cell-state owner + invariant + epsilon | ED-MB-0045 §3 | `tests/sim/mass_battle/*` | **→ MB plan A2/B1a-c/B2** (fork 6/7 held there) |
| OI-48 | Six live dice/resolution kernels disagree at floors/ceilings; intra-file d10 duplication in massbattle with zero parity coverage; live contests still resolve via the deprecated raw-dice `contest_legacy_stub` (which IS the formula the loop reaches) while the promoted σ-kernel has zero live callers — dual formulas diverge 9.5–28.9pp (ED-SC-0004 = which formula is canon; ED-SC-0011 = the personal-party bridge) | 07-07 U-3/U-8 · ED-SC-0004/0011 | `systems/social_contest/sim/contest/*`, `systems/mass_battle/sim/massbattle.py` | J (0004) / B (0011) |
| OI-49 | Three competing "faction political power" formulas (franchise NI, `political_value()` TBD scalars, settlement Mandate); Mandate monotone — no withdrawal/collapse path; ~27 distinct cross-scale value-transformation rules with no shared aggregation contract (`Field`/`Gauge` primitive PROPOSED only — Stratum-B conditional) | GAP-B2/B3 · 07-14 value-arch §A/§E | design + future `engine/substrate/fields.py` | J |
| OI-50 | Two incompatible attribute rosters (9 vs 10), no `Character`/`Actor` dataclass anywhere — resolvers duck-type `getattr(actor,'strength',3)` or bypass character state; Combat Pool defined 3 ways. IN FLUX per CLAUDE.md §5 — superseded in scope by the ED-IN-0029 docket (UNRULED). Do not bind | 07-17 D8 · ED-IN-0029 | `descriptor_registry.yaml`, `engine/params/core.md` | **D/J** (docket) |
| OI-51 | Ruled-but-unexecuted class: ED-871 (Mending cost never applied), ED-912 (knot resolution 1-of-4 sites), fork-2/fork-11 ratified-unexecuted, `conviction_track_v30` running a self-documented superseded model | 07-07 U-6 | per item | M (sweep + execute) |

## §6 · Interdependencies & tooling shape

| ID | Item | Evidence | Paths | Class |
|---|---|---|---|---|
| OI-52 | Import cycles (4): `engine.autoload.game_state ↔ systems.world.sim.npe` (IN); 6-module `social_contest.sim.contest.*` cycle (documented intentional-during-rebuild — leave); `systems.mass_battle.sim.massbattle ↔ .units` + 5-module `tests.sim.mass_battle.*` cycle (**→ MB session**; both massbattle members are cut-vertices). FA→MB cross-lane lazy import (`faction_action` → `massbattle`) is the declared seam — untouched here | structure_audit 07-26 | as named | M/B (IN) · **→ MB plan** (MB cycles) |
| OI-53 | Dead retired-`sim/` roots persist in live tooling (F4 class, FILED not fixed): `ci_quantity_vocabulary_check.py:145` `--sim-root` default (a CI gate running blind — sim surface contributes nothing to vocab.a17), 11 dead `sim_module:` paths in `registers/mechanics_index.yaml`, `audit_staleness.py:69`, `build_decisions.py:57`, `workplan_status.py:71`, `build_apparatus_registry.py:169`, `test_persubunit_stress.py:17` sys.path | ED-MB-0043 F4 | as named | **M** (high priority) |
| OI-54 | Contract↔code correspondence is a disclosed black hole: name-matching joins only 6/27 contract modules to the 248 code modules; a fictional contract entry would pass as canon-grade wiring. Needs the `sim_module:` join + a verification signal | A5/C10 · ED-IN-0056 · GAP-I4 | `module_contracts.yaml` × G_code | B |
| OI-55 | Orphan-detector integrity: `__init__` relative-import misresolution inflates the orphan list (P0.1 HIGH instrument fix before triage); CLI entry-point noise unlabeled; `vector_audit.py` analytical core has no known-answer coverage beyond one total-pin | 07-14 obs P0.1 · unification §8 | `skills/valoria-vector-audit/scripts/*` | B |
| OI-56 | No pipeline-reach oracle exists: nothing asserts the campaign loop reaches (or consciously stubs) every scene direction, scale rung, and delivery direction — the Priority-1 acceptance instrument is itself a gap | this register (synthesis) | `engine/tests/` (new) | B |
| OI-57 | Currency-layer orphans: `franchise_v30` absent from CURRENT.md/canonical_sources/mechanics_index despite full spec; `insurgency_pipeline_v30` + `faction_succession_split_v30` unindexed; ED-1054 stale navigation surfaces | GAP-F1/F4 (07-13) · ED-1054 | `references/*` | M |
| OI-58 | Stale audit families at session start: vector-audit 133 in-scope files stale (2026-07-22 refresh), graph-lexicon 8, decisions-digest 4 — re-baseline needed after any wiring wave | SessionStart banner 07-29 | `tools/audit_staleness.py` | M (re-run) |
| OI-59 | NPC family (`npc_behavior`/`npc_memory`/`npc_ai`) has no owning workplan lane despite [ASSUMPTION] resolvers + doc:null + Stage-2.5 precondition status; both integration hubs (`faction_state` in-13, `npc_behavior` in-12 — both cut-vertices) are [ASSUMPTION]-grade: the highest-value Key flow passes through the least-certain resolvers | C-STUB-7 · GAP-B2/B7 | organizational + contracts | J (lane) / B (grounding) |

---

## Counts and shape

- **~60 register rows** consolidating **100+ raw audit findings** (multiply-rediscovered defects
  merged; each row cites all corroborating sources). Highest-corroboration items (4–6 independent
  rediscoveries): OI-21 (fabricated emit), OI-01 (combat unreached), OI-05 (generate_npc),
  OI-22 (combat dangling emits), OI-28 (causes[] zero), OI-54 (contract↔code black hole).
- **Class split:** ~14 M (mechanical), ~30 B (build, design exists), ~12 J (ruling-gated, listed
  loudly in the plan's §5 docket), ~5 D (deliberately deferred — do not touch). Of these,
  **7 rows route wholly or partly to the MB session** (OI-11/14/21/23/40/47/52) and **5 to the
  PC session** (OI-13/26/44/45/46) — see the lane partition note above.
- **The two structural centers of gravity:** (1) the campaign loop reaches a fraction of the built
  game — orphans are concentrated at the *seams* (dispatch, echo, handoff, articulation), not in
  the subsystem interiors; (2) single-owner violations concentrate in the two combat engines and
  the contest dual-formula, all three carrying an unresolved canon fork.

*Companion: `01_orchestration_plan_v1.md` — the wave/agent plan over these rows.*
