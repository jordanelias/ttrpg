# Independent re-derivation: references/module_contracts.yaml → systems/ folders

Method note: file read whole, sequentially, via the Read tool in five chunks (lines 1-200,
200-400, 400-600, 600-800, 800-999, 999-1108). No Grep/grep/rg/sed/awk used at any point.
Did not open any `*_flow_skeleton_v1.md` file.

The file declares schema_version 2, 27 `modules:` entries (confirmed by full read-through
count) plus a trailing `accounting_sequence:` block (not a module).

---

## Per-module record

### 1. faction_state
- doc: systems/factions/faction_behavior_v30.md | sim_module: engine/autoload/game_state.py (real — the `Faction` dataclass/state half only; resolver/cascade logic has NO code anywhere per the module's own comment)
- resolver: deterministic_accounting | scales: [provincial]
- consumes: 24 edges | emits: 3 edges
- state: Mandate (derived_value, not writable), Treasury (derived_value, not writable), "faction stats 1-7" (track, **writable**)
- gap_notes (3): registry-name vocabulary unification OPEN-Jordan; SCOPE note (module = faction_layer_v30 + faction_behavior_v30 doc union); "state joins; behavior does not yet exist" (self-admitted resolver gap)
- Folder: **factions** — high confidence (doc path)

### 2. npc_behavior
- doc: systems/factions/political_dynamics_keys_migration_v30.md (repointed 2026-07-29 from systems/npcs/npc_behavior_v30.md) | sim_module: none (explicit; near-miss npc_ai_service is a flagged `stubwire`, deliberately not counted)
- resolver: deterministic_accounting | scales: [personal, scene]
- consumes: 31 edges | emits: 11 edges
- state: beliefs/opinions, concerns, projects, arc state — all 4 **writable**
- gates: g_stall8, g_drift
- gap_notes (5): CONSOLIDATED note (absorbed former political_dynamics); SUPERSEDED note (4 types registered by ED-935); accounting-sequence note; OI-24 stale-comment-correction note; C-KEY-2 doc repoint note
- Folder: **npcs** conceptually, but its `doc:` lives physically under `systems/factions/` and `systems/npcs/` has zero .py files — **ambiguous / low-medium confidence**, flagged in §C below.

### 3. npc_memory
- doc: null | sim_module: none
- resolver: state_reader | scales: [personal]
- consumes: 4 edges | emits: 0
- state: []
- gap_notes (1): "home doc unlocated ... standalone spec [GAP]"
- Folder: **npcs** — weak confidence (conceptual fit only, no doc/code evidence)

### 4. piety_track
- doc: systems/characters/conviction_track_v1.md | sim_module: systems/characters/sim/conviction.py (real, verified)
- resolver: deterministic_accounting | scales: [personal]
- consumes: 9 edges | emits: 1 edge
- state: "conviction scars" (clock, **writable**)
- gates: g_scar2, g_scar3
- gap_notes (1): 3-way name collision with territorial_piety (and a third substrate reference) [OPEN-Jordan]
- Folder: **characters** — high confidence

### 5. territorial_piety
- doc: systems/characters/conviction_track_v30.md | sim_module: systems/overview/sim/ci_track.py (CI half only; CV half lives in engine/autoload/game_state.py — disclosed split, no single-file owner)
- resolver: deterministic_accounting | scales: [territory, provincial]
- consumes: 0 | emits: 0
- state: CV (track, **writable**), CI (clock, **writable**); "TC" row struck 2026-07-08 (retired duplicate name for CI, not a second clock)
- gates: g_ci100, g_cicap
- gap_notes (3): zero Key integration in a canonical doc; name collision w/ piety_track; Key types registered W3
- Folder: **ambiguous** — doc under characters/, sim under overview/, scales say territory/provincial. No single clean owner; leaning **overview** (sim + scale) but doc says characters. Flagged in §C.

### 6. threadwork
- doc: systems/threadwork/threadwork_v30.md | sim_module: systems/threadwork/sim/operations.py (real)
- resolver: dice_pool | scales: [personal, thread]
- consumes: 0 | emits: 2
- state: Coherence (track, **writable**), Thread Fatigue (clock, **writable**)
- gap_notes (1): doc self-declares "design proposal, requires editorial approval" yet carries a CANONICAL pool notice — status ambiguity [OPEN-Jordan]
- Folder: **threadwork** — high confidence

### 7. fieldwork_knots
- doc: systems/fieldwork/knots_v30.md | sim_module: systems/fieldwork/sim/knots.py (real; sibling fieldwork.py implements Evidence/Disposition Track rows, disclosed not silently merged)
- resolver: dice_pool | scales: [personal, scene]
- consumes: 1 edge, and it is a **wildcard `*` from engine** (Memory Query API)
- emits: 4
- state: knot strain, Bonds, Evidence Track, Disposition Track — all 4 **writable**
- gates: g_strain, g_decay, g_bond5
- gap_notes (2): scene.gift dual-attribution cross-check vs scene_slate; TIER-DRIFT/COMPOSURE-DRIFT resolution history + residual §6.2 unverified
- Folder: **fieldwork** — high confidence

### 8. scene_slate
- doc: **null** | sim_module: engine/autoload/scene_slate.py (real — explicitly flagged in-file as a correction to a prior "9 doc:null/no-sim" preflight claim that wrongly lumped this module in as no-sim)
- resolver: manifest | scales: [scene]
- consumes: 0 | emits: 8
- state: []
- gap_notes (1): home doc unlocated [GAP]
- Folder: **none clean** — engine/autoload-level scene manifest, not owned by any systems/ subsystem doc. Low confidence for any folder.

### 9. game_director
- doc: null | sim_module: none (two near-misses disclosed and rejected: season_manager.py, engine/cross_scale/scene_dispatch.py — neither emits this module's declared Keys)
- resolver: manifest | scales: [scene]
- consumes: 0 | emits: 3
- state: []
- gap_notes (1): registry-derived, home doc unlocated [GAP]
- Folder: **none** — cross-cutting orchestrator, unhomed.

### 10. scene_timer
- doc: null | sim_module: none
- resolver: state_reader (observability sidecar, "advances no game clock") | scales: [scene]
- consumes: 3 | emits: 0
- state: []
- gap_notes (1): home doc unlocated [GAP]
- Folder: **none** — tooling/observability, not a gameplay subsystem.

### 11. audit
- doc: null | sim_module: none
- resolver: state_reader (QA/telemetry) | scales: [scene]
- consumes: 3 | emits: 0
- state: []
- gap_notes (1): runtime-system vs QA-tooling classification [OPEN-Jordan]; home doc [GAP]
- Folder: **none** — QA tooling, not a gameplay subsystem.

### 12. social_contest
- doc: systems/social_contest/social_contest_v30.md | sim_module: systems/social_contest/sim/contest/ (dir, real)
- resolver: dice_pool | scales: [scene]
- consumes: 1 | emits: 4
- state: persuasion_track (clock, **writable**)
- gap_notes: **none present** (no gap_notes key at all — only module besides mass_battle without one)
- Folder: **social_contest** — high confidence

### 13. mass_battle
- doc: systems/mass_battle/mass_battle_v30.md | **sim_module field itself is absent** (deliberately, per an inline comment: this module's rows are MB-lane-owned in a shared-file single-writer table; IN lane doesn't touch them even to add a field). Lead note: mechanics_index.yaml already has `mass_battle -> systems/mass_battle/sim/massbattle.py`.
- resolver: dice_pool | scales: [scene]
- consumes: 0 | emits: 1
- state: []
- gap_notes: **none present**
- Folder: **mass_battle** — high confidence

### 14. domain_actions
- doc: **null** | sim_module: none (near-miss engine/cross_scale/domain_echo.py disclosed and rejected — it transports an unrelated "Domain Echo" concept, name-collision only)
- resolver: d_sigma | scales: [provincial]
- consumes: 0 | emits: 6 (scene.draft_da + 5x da.*)
- state: []
- gap_notes (3): home doc unlocated; ED-FA-0006 reclassifies this as a per-verb tag scheme on EXISTING catalogs, not a standalone module; residual per-verb authoring task, boundaries open for Jordan
- Folder: **ambiguous, no clean folder** — weakly factions-leaning per ED-FA-0006 but the note explicitly says it isn't meant to be its own module/doc.

### 15. peninsular_strain
- doc: systems/overview/peninsular_strain_v30.md | sim_module: systems/overview/sim/ (dir; MS = ms_track.py, IP = ip_track.py, **Turmoil has no tracker file anywhere** — disclosed open fork)
- resolver: deterministic_accounting | scales: [peninsula]
- consumes: 0 | emits: 4
- state: Turmoil, IP, MS — all 3 **writable** (Turmoil despite having no code)
- gates: g_ip100, g_ip85, g_ip80, g_ipfall
- gap_notes (1): GAP-F1 residual — MS ownership resolved but no consumer exists for a would-be env.ms_delta emit
- Folder: **overview** — high confidence

### 16. settlement_layer
- doc: systems/settlements/settlement_layer_v30.md | sim_module: systems/settlements/sim/settlement.py (Legitimacy/PS split into sim/registry.py, disclosed)
- resolver: deterministic_accounting | scales: [settlement, territory]
- consumes: 2 | emits: 1
- state: 4 rows — Prosperity/Defense/Order (track, writable), Local Economy/Garrison/Public Order (derived_value, **not writable**), Legitimacy/PS (track, writable), province Accord (derived_value, **not writable**)
- gates: g_ord0, g_def0, g_dv0 | derivations: 5 formulas
- gap_notes (2): index doc stale (predates §1.8); Key types registered W3
- Folder: **settlements** — high confidence

### 17. settlement_economy
- doc: null | sim_module: none — this module's own gap_notes call it a "phantom module (no doc/state/logic)"
- resolver: deterministic_accounting | scales: [settlement]
- consumes: 2 | emits: 0
- state: []
- gap_notes (3): relationship to settlement_layer's Local Economy unestablished [OPEN]; RECOMMEND RETIRE (phantom); ED-SE-0005 confirms the player-action half of the retirement
- Folder: **settlements** nominally, but explicitly flagged retire-candidate/phantom — low-confidence, dying module.

### 18. ci_political
- doc: systems/factions/ci_political_v30.md | sim_module: none ("ZERO Key integration in a CANONICAL doc")
- resolver: deterministic_accounting | scales: [provincial]
- consumes: 0 | emits: 0
- state: CI (clock, **not writable** — reader only, generation owned by territorial_piety), faction political pool (pool, writable), card hands/cooldown (track, writable)
- gap_notes (2)
- Folder: **factions** — high confidence

### 19. victory
- doc: systems/victory/victory_v30.md | sim_module: engine/autoload/victory.py (real)
- resolver: state_reader | scales: [provincial, peninsula]
- consumes: 0 | emits: 0
- state: 1 aggregate row (MS/IP/CI/Turmoil/Accord/Mandate/PV/PT reads, clock, **not writable** — reader only)
- gates: g_ms0, g_ms5, g_msrec, g_diss
- gap_notes (4): era transitions unkeyed; doc not CANONICAL (pending Varfell Path B); index doc stale; gate-ownership annotations corrected 2026-07-29
- Folder: **victory** — high confidence

### 20. engine_clock
- doc: null | sim_module: none (season_manager.py near-miss: advances a counter but emits neither declared Key)
- resolver: clock_advance | scales: [provincial]
- consumes: 0 | emits: 2
- state: season counter (clock, **writable**, [ASSUMPTION]-tagged)
- gap_notes (2): home doc unlocated (campaign_architecture checked and rejected); systems/_architecture/propagation_spec_v1.md is a CANDIDATE home doc but doc: stays null pending ED-1051
- Folder: **_architecture** (candidate only, per its own gap_note) — low-medium confidence.

### 21. faction_politics
- doc: systems/factions/faction_politics_v30.md (verified CANONICAL, was stale null) | sim_module: none — contract-truth declaration only, sim explicitly DEFERRED to FA lane
- resolver: deterministic_accounting | scales: [provincial]
- consumes: 0 | emits: 4
- state: Standing, Coup posture, Succession status — all 3 **writable** (track)
- gap_notes (3): boundary vs faction_state genuinely open; home-doc gap closed 2026-07-08; state:[] closed 2026-07-29 as contract-truth-only
- Folder: **factions** — high confidence

### 22. miraculous_event
- doc: systems/world/miraculous_event_v30.md (CANONICAL) | sim_module: systems/world/sim/miraculous_event.py (real)
- resolver: state_reader | scales: [personal, settlement, peninsula]
- consumes: 0 | emits: 1
- state: []
- gap_notes (1): system-vs-event-source classification open; home doc resolved
- Folder: **world** — high confidence

### 23. scenario_authoring
- doc: null | sim_module: none (authoring-time; execution unbuilt)
- resolver: manifest | scales: [peninsula]
- consumes: 0 | emits: 2
- state: []
- gap_notes (1): authoring-time confirmed by ruling; execution unbuilt; "no dedicated scenario_authoring design doc exists" [GAP]
- Folder: **none** — explicitly no home doc exists; weak world/overview candidate at best.

### 24. articulation_layer
- doc: systems/articulation/articulation_layer_v30.md | sim_module: engine/cross_scale/articulation.py (real, differently-located but explicit legitimate path)
- resolver: deterministic_accounting | scales: [personal, scene, provincial]
- consumes: 1 edge, and it is a **wildcard `*` from engine** (universal Key-stream reader; registry separately lists 31 explicit subscriptions not itemized here)
- emits: 0
- state: []
- gap_notes (1): significance function / belief_revised emission path not extracted
- Folder: **articulation** — high confidence

### 25. clock_registry
- doc: systems/overview/clock_registry_v30.md | sim_module: none — **by design**, not a gap ("owns no state, resolves nothing")
- resolver: manifest | scales: [provincial]
- consumes: 0 | emits: 0
- state: []
- gap_notes (1): pure manifest; carries PROVISIONAL staleness flags
- Folder: **overview** — high confidence

### 26. personal_combat
- doc: systems/combat/combat_engine_v1/ (dir, CANONICAL) | sim_module: same dir (real, canonical)
- resolver: d_sigma | scales: [personal]
- consumes: 2 | emits: 3
- state: 6 rows — Health (derived_value, **not writable**), cumulative_damage/Wounds/Stamina/Initiative/Poise (track/pool, all **writable**)
- derivations: 1 (Health formula)
- also carries a nested `modules:` list of 11 EngineModules (2 PORTED, 1 RETIRED, 1 FOLDED, 1 PARTIAL, 6 PENDING) — unique to this entry
- gap_notes (5)
- Folder: **combat** — high confidence

### 27. campaign_architecture
- doc: systems/_architecture/campaign_architecture_v30.md | sim_module: none (reclassified 2026-06-10 as a cross-cutting consolidation doc, not a runtime module)
- **no resolver:, consumes:, emits:, state:, transitions:, or loops: keys present at all** (unlike every other doc:null/sim:none module, which still carries `consumes: []` etc. as empty lists)
- scales: [provincial]
- gap_notes (2): recommend stub retirement [OPEN-Jordan]; clock-spine hypothesis withdrawn
- status: **stub** (only module with this status; the file header defines stub == "pointer only, ZERO edges" — consistent in spirit, but structurally implemented by field-omission rather than empty-list, unlike every other zero-edge module)
- Folder: **_architecture** — high confidence

---

## Folder mapping summary (systems/ subsystem folders)

| Folder | Modules mapped | Confidence |
|---|---|---|
| _architecture | campaign_architecture; engine_clock (candidate only) | high / low |
| articulation | articulation_layer | high |
| characters | piety_track; territorial_piety (contested, see below) | high / ambiguous |
| combat | personal_combat | high |
| factions | faction_state, ci_political, faction_politics; npc_behavior (doc-location only, contested); domain_actions (weak, contested) | high / ambiguous / weak |
| fieldwork | fieldwork_knots | high |
| mass_battle | mass_battle | high |
| npcs | npc_behavior (contested — doc lives in factions/), npc_memory (conceptual only) | ambiguous / weak |
| overview | peninsular_strain, clock_registry; territorial_piety (sim-location, contested) | high / ambiguous |
| settlements | settlement_layer; settlement_economy (flagged phantom/retire) | high / low |
| social_contest | social_contest | high |
| threadwork | threadwork | high |
| **ui** | **none** — no module in this file maps to ui | — |
| victory | victory | high |
| world | miraculous_event; scenario_authoring (weak, no home doc at all) | high / weak |

**Unhomed / no folder** (engine-level or tooling modules with no systems/ doc, and explicitly not claiming one): scene_slate, game_director, scene_timer, audit, and weakly domain_actions/scenario_authoring/engine_clock.

---

## List A — sim_module names real code (13 modules)
faction_state, piety_track, territorial_piety, threadwork, fieldwork_knots, scene_slate,
social_contest, peninsular_strain, settlement_layer, victory, miraculous_event,
articulation_layer, personal_combat.

(Several are partial/split code homes, disclosed in-line rather than papered over: faction_state
state-only, territorial_piety CI-only, fieldwork_knots state-only-partial, peninsular_strain
directory with Turmoil untracked, settlement_layer Legitimacy/PS split out.)

## List B — sim_module none/absent, or doc: null (15 modules)
npc_behavior, npc_memory, scene_slate (doc:null despite real sim — also in A), game_director,
scene_timer, audit, mass_battle (sim_module field structurally absent, not "none"),
domain_actions, settlement_economy, ci_political, engine_clock, faction_politics,
scenario_authoring, clock_registry (none by design, not a gap), campaign_architecture.

## List C — internal contradictions noticed

1. **Multi-attribution emit conflicts, self-flagged OPEN—Jordan, on at least three Key types:**
   `mechanical.scene_entered` (scene_slate AND game_director both emit it — cross-doc
   attribution conflict noted at scene_slate's own emit line); `scene.dialogue` (scene_slate,
   social_contest, AND npc_behavior all emit it — npc_behavior's own comment flags the registry
   as attributing it to only the other two); `state.belief_revised` (both fieldwork_knots and
   npc_behavior emit it — npc_behavior's comment flags the registry attributing it to fieldwork
   only).
2. **domain_actions is doc:null, sim_module:none, yet is the single most heavily-relied-upon
   emitter in the whole graph** — its 6 emitted types (scene.draft_da + 5× da.*) are consumed by
   faction_state, npc_behavior, piety_track, and settlement_economy's consumes: lists. A module
   with zero code and no home doc is load-bearing for at least four other modules' declared
   inputs.
3. **Two different absence conventions for "nothing here" inside the same schema:** every other
   zero-edge module (npc_memory, game_director, scene_timer, audit, domain_actions,
   settlement_economy, ci_political, engine_clock, scenario_authoring, clock_registry) still
   carries explicit empty lists (`consumes: []`, `emits: []`, `state: []`, etc.). campaign_architecture
   (status: stub) and mass_battle (sim_module) instead omit the keys entirely rather than
   emptying them — a structural inconsistency the file's own header (status: stub == "pointer
   only, ZERO edges") doesn't fully anticipate.
4. Scale/folder mismatch: territorial_piety's doc lives under `systems/characters/` (a personal-scale
   folder) while its own `scales:` field is `[territory, provincial]` and its sim code lives under
   `systems/overview/sim/` — three different homes point three different directions.
5. faction_state's own state: block is real code (game_state.py) for the *data* half, but its
   consumes/emits reference `mechanical.cascade_resolution`/`mechanical.mission_shift` as if
   resolved, while the module's own comment admits "the RESOLVER half ... has no dedicated
   implementation anywhere in the tree" — state and behavior are split, not jointly verified.
6. The 3-way "Piety Track" name collision (piety_track vs territorial_piety vs a third substrate
   reference) is declared as an open naming defect in both modules' own gap_notes, not resolved
   anywhere in this file.
