# Valoria — Python→Godot Conversion Strategy & All-Directions Hierarchy (v1)
**2026-06-10 · status: PROPOSED (Jordan-vetoable throughout) · scope: both repos**
**Binds to:** `valoria_master_workplan.md` (W4.1–W4.3 Godot epics) + `valoria_workplan_R2` Phase E (per-system ritual). This document is the *execution spec* for those approved items — it does not fork them.
**Supersedes in part:** `godot/implementation_sequence.md` (2026-04-18 G1–G7 phasing — superseded by Part VI here) and the framing portions of `godot/data_serialization_spec.md` (schemas now derive from `references/module_contracts.yaml` + the Descriptor Registry, not `sim_framework/state.py`). `scene_tree_architecture.md` and `gm_to_engine_conversion.md` remain valid with the amendments noted in Parts III–IV.
**Provenance:** consolidated from the 2026-06-06→06-10 work (commits cited in §X) + all project conversations 2026-06-06→06-10 + live reads of both repos this session. As-of: ttrpg ≈ `496f3d5` (tree advanced mid-session — a parallel session is committing; +2 paths, 5 stale freshness SHAs at last bootstrap); valoria-game `main` (0 commits since 2026-06-06; last design sync 2026-05-04 @ `9057663f`).

---

## 0 — VERDICT & PROBLEM STATEMENT (first, no false balance)

**The conversion problem is not "start porting Python to GDScript." It is a reconciliation problem with a porting problem inside it.** Three bodies of work exist and have drifted apart at different speeds:

1. **The design/Python corpus (ttrpg)** — raced ahead: kernel + 3 probabilistic regimes ratified, combat_engine_v1 ratified (ED-900–904), d+σ resolver ratified (ED-874), LPS-2e Mandate-as-derived, the Key substrate (CANONICAL), 27 module contracts extracted (06-10), Descriptor Registry landed, module-adjudicator enforcer live, and a per-system flatten wave (06-09/10) that produced exactly the IN→resolver→OUT extraction artifacts a port consumes.
2. **The Godot repo (valoria-game)** — a *substantial, real* April-era implementation (5 autoloads incl. an event bus and a KeyStore, 6 containers + GameDirector zoom stack, CoreResolver/CoreEngine, 26 typed Resources, articulation v30, 14 test suites) that has been **frozen since 2026-05-04** and is now superseded in several load-bearing places (Key schema v1, pre-ED-901 combat, pre-d+σ domain actions, Mandate as a base field, faction-specific victory paths).
3. **The Python sim armature (`sim/`)** — deliberately built (2026-05-17) to mirror `godot/scene_tree_architecture.md` **1:1** (autoload + scale subpackages + cross_scale bus), precisely so GDScript ports build from Python reference implementations. Bootstrap index: 27 sim modules verified / 9 canon-gated / 1 partial / 8 stub.

**So the strategy is:** (Part I–III) one consolidated picture of what exists on all three legs; (Part IV) the target all-directions hierarchy with the conversion unit fixed as the **module contract**; (Part V) the Python→Godot dictionary including the determinism/parity protocol; (Part VI) gated sequencing; (Part VII–VIII) the friction register and the consolidated `[OPEN — Jordan]` set. **Nothing here resolves a Jordan-tier decision; every structural option is presented with its anchor and carried open.**

The single most important architectural fact, stated once: **the Key substrate is already the conversion architecture.** Save state = initial conditions + Key log; replay = deterministic re-execution (`key_substrate §1, §6`); §4.1 defines the *only* state-mutation path; §8.8 already maps it to Godot (Key→Resource, registry→autoload, KEY_LOG→typed-array Resource, CAUSAL_GRAPH→sparse dict-of-sets, save=serialize the log). Conversion succeeds to the degree every module honors that substrate and its published contract — which is exactly what the module-adjudicator now machine-checks on the design side. The port's job is to make the same checks hold in GDScript.

---

## PART I — CONSOLIDATED INVENTORY (what the last few days built, stream by stream)

### I.1 The structural substrate (Tier 0)
- **Keys** — universal atomic record, 7 type families ≈30 subtypes (`key_type_registry_v30`), schema per `key_substrate §2.1`: id · type · source_actor · `emitted_at{season_index, sub_step_index}` · `causes[]` · `targets[]` (each `{actor_id, role, impact_vector[4], stat_deltas{}}`) · `scale_signature[]` · `symbolic_dimensions[4]` · visibility{public/semi/private} · time_horizon · permanence · payload. Validation invariants §2.3; single update rule §4.1; determinism guarantees §6 (RNG seeding per emission, deterministic ordering, float reproducibility); Godot mapping §8.8. **CANONICAL.**
- **Value taxonomy (4 buckets)** — base Stats (1–7) feed **Pools** (computed at action time), **Derived Values** (stat×multiplier, read-only — R4 hook guards direct writes), **Tracks** (bounded), **Clocks** (monotonic, `clock_registry_v30` is the manifest). The bucket discipline is what the resolution-diagnostic lessons attach to.
- **Actor model** — 13-Conviction weighted vector × the 13×4 CONVICTION_AXIS_MATRIX → `armature_position[4]`; Self-Other scalar; `interpretation(npc, key)` dot-product is the bridge from event log to character psychology (`conviction_taxonomy/axis_matrix`, hierarchy-map Tier 2).
- **Descriptor Registry (W1.13, landed 06-09 `b9d897c`)** — all engine-processable qualitative descriptors bound by key (attribute scalars, conviction weights, axes, the 13×4 map, orientation, contest styles, temperaments; one mechanism, DOMAIN-partitioned pending W2.9). Makes the taxonomy data-not-code — the exact property a Godot Resource table wants.

### I.2 The kernel (engine framing, master_workplan §8 — Jordan-affirmed)
- **Attribute-agnostic core**: the kernel resolves a pool/inputs → degree; pool assembly is a wrapper concern.
- **One kernel concept, three probabilistic regimes**: discrete d10 pool · continuous-Normal (statistically equivalent; the videogame mode) · **d+σ** deterministic-stochastic (ED-874, ratified 2026-05-31; basis CK3/EU/KoDP) for the small-pool faction regime. Plus two non-probabilistic archetypes — deterministic accounting, clock advance — and the armature dot-product. **Five resolver archetypes total**; a dispatcher over regimes, not one formula. (Reification of the dispatcher is K8-gated, W1.14.)

### I.3 The module-contract layer (the conversion unit) — 06-10
- **`references/module_contracts.yaml` v2** (`ebc3669`, anchored in canonical_sources `dd499d9`/`262d948`): **27 modules** — 25 extracted + 2 stubs — each as `consumes[] → resolver → emits[]` with state buckets, scales, scale-transition routes, loop flags, and gap notes; edges transcribed verbatim, conflicts kept visible. ED-1005 (instrument creation) / ED-1006 (Stage-1 extraction findings).
- **`skills/valoria-module-adjudicator/`** (`cdbd1b5`, +1060) — the enforcer Jordan named: Stage 0 scope → Stage 1 extract → Stage 2 adjudicate (machine checks A1–A9 via `contract_adjudicator.py`) → Stage 3 verdict → Stage 4 enforce & re-test. This is the design-side guarantee that every system is module-shaped with declared I/O Keys.
- **Headline structural finding (ED-1006):** `scale_transitions §3`'s nine handoff rules are all **upward or combat-adjacent — no rule governs top-down Key delivery** (provincial→personal DA outcomes, peninsula→settlement shocks, succession/coup downward). Resolution is Jordan's (Part VIII #1).

### I.4 The enforcement & data layer
33 hook gates live (`safe_commit` family, task_gate, sim_gate, R4 derived-write guard, R7 formula co-file, ID-uniqueness, collision detection); CI mirrors externally in **both** repos (`valoria-ci.yml`, incl. `godot-ci.yml` in valoria-game); editorial store = `editorial_ledger.jsonl` (single-source, 639+ entries, 0 dup IDs); file index = `valoria_index.sql` pipeline; `ecosystem_versions.yaml` pins **Godot 4.6** + model/tokenizer. Workplan governance: master workplan (06-06, Jordan-approved Waves 0–1+K8) + Workplan R2 (06-09) with **Phase E** — the per-system implementation ritual (param export · golden-master parity · property checks · namespaced StringNames) and the engineering floor (typed GDScript, gdlint/gdformat, gdUnit4, headless CI, kernel scene-tree-free, one injected seeded RNG, statechart flow, typed event bus).

### I.5 The extraction artifacts (06-09/10 flatten wave — the port's source material)
Per-system flow/state/flattened maps now exist, line-cited to canon, for: **personal combat** (`6165471`: ~120 config tunables grouped, **19 RNG draw sites censused**, 23-step exchange sequence, full I/O surface), **mass battle** (`bedbf41`/`43e33b1`: inputs→calc→gates→sequence→outputs + N1 "no canonical gate-vector manifest"), **social contest** (`c8394f3`/`68ad7f6`: 26 in / 26 calc / 32 gates / 11 seq / 23 out + 4 state graphs), **faction play** (IN-1…10 / ST-1…12 / CALC-1…15 / GATE-1…16 / CAP-1…11 / OUT-1…12; commit pending Jordan go), **settlement** (flowchart + 3-axis state graph + flattened map; outputs-only, 4 decision-grade gaps), **fieldwork/investigation** (`a11e2fa`: P1 canonical-line split — conversion-blocking for that module), plus the faction-stat consolidation master (`59622c0`) and attribute flatten (`a9cc310`). **These are the bottom-up ground truth each module port transcribes from — not the prose docs alone.**

### I.6 The engines already in Python (reference implementations)
- `designs/scene/combat_engine_v1/` — **CANONICAL** personal-combat resolver (wrapper/systems/core/config/combatant/tradition; `config.py` = live params).
- `tests/sim/mass_battle/` — ratified mass-battle engine (config/orchestration/resolution/percell; flag-gated cell-up layer).
- The contest engine (modes/resolver/primitives/engine/contract; 146-test baseline; periphery NERS-noncompliant, core sound).
- `sim/` armature — autoload (dice_engine, game_state, registry, season_manager, scene_slate, npc_ai, victory) + personal/thread/provincial/territory/peninsular/world + **cross_scale** (domain_echo, handoff_rules, zoom_in_out, scene_dispatch incl. the 06-07 seam wiring `db639e5`, articulation) — built to mirror the Godot scene tree 1:1.

---

## PART II — EVERY SYSTEM, EXPLICITLY (the 27 contracted modules → conversion disposition)

Source: `references/module_contracts.yaml` v2 (verbatim resolver/scale/edges) + this strategy's Godot-home and wave assignments (mechanical-tier, Jordan-vetoable). **Wave key:** S=spine · 1=deterministic · 2=d+σ/provincial · 3=dice engines · 4=actors/read-side · R=retire. "VG home" names where it lands in valoria-game (existing file = refit; otherwise new).

| # | Module | Resolver | Scales | VG home (refit/new) | Wave | Conversion notes / blockers |
|---|---|---|---|---|---|---|
| 1 | settlement_layer | accounting | settlement/territory | `ValoriaSettlementLibrary` + SettlementData (refit to LPS-2e §1.8) | **1 — recommended first** | Pure math (W_s, q_s, T, Mandate K=6 saturating aggregate); cleanest parity; feeds Mandate. Stale index [tooling]. |
| 2 | peninsular_strain | accounting | peninsula | clocks + shock emitter (refit Constants/SettingState) | 1 | Turmoil 0–10, IP clock; env.* Keys (source_actor=null). |
| 3 | territorial_piety | accounting | territory/provincial | CV/CI/TC system (new) | 1 | CANONICAL doc, **zero Key integration** — registry §10 keying pass precedes emit wiring. Name collision with #4 [OPEN]. |
| 4 | piety_track (personal) | accounting | personal | scar system on Tracker (new) | 3 | 3-way name collision (substrate §8.4 "Piety Track" = registry `conviction_track` = personal scars vs territorial doc) [OPEN — Jordan]. |
| 5 | ci_political | accounting + clock | provincial | political-effects reader + card system (refit) | 1 | Reads CI (owner=#3); CI=100 Theocracy attempt **unkeyed** [§10 candidate]. |
| 6 | victory | state_reader | provincial/peninsula | `VictoryManager`-class refit | 1 | **GD-1: single peninsula-control victory only** — existing VG faction paths are superseded code; era transitions unkeyed [§10]; treaty wiring open (Jordan). |
| 7 | clock_registry | manifest | provincial | ClockData resources seeding TrackerRegistry | S | Pure data; carries PROVISIONAL ED-793/794/795 flags. |
| 8 | engine_clock | clock_advance | provincial | `SeasonManager`/`GameStateMachine` (refit) | S | Emits mechanical.accounting / season_change; **home doc unlocated [GAP]** — contract is the spec seed. |
| 9 | game_director | state_reader | scene | `GameDirector.gd` (exists, refit lifecycle Keys) | S | scene_entered/exited/skipped; attribution conflict with scene_slate [OPEN]. |
| 10 | scene_slate | state_reader | scene | `SituationGenerator`+slate (refit) | S/4 | Home doc [GAP] (spec scattered: settlement §4.1 + substrate §8.5). |
| 11 | scene_timer | clock_advance | scene | `autoload/SceneTimer.gd` (**already exists**) | S | Consumes lifecycle Keys; align to registry. |
| 12 | domain_actions | **d_sigma** | provincial | `DomainActionSystem` refit to d+σ ED-874 | 2 | Home doc [GAP — resolver spec sits in an audit dir; promote]. Drop `scene.draft_da` (W3.4). |
| 13 | faction_state | accounting (+d+σ contested) | provincial | `systems/faction_v30/` (exists, refit) | 2 | **Write paths parameterized by the 5 re-route archetypes** (consolidation master A.4) so the faction-stat inversion lands as data, not rewrite. Self-loop damper [OPEN]. |
| 14 | faction_politics | accounting | provincial | succession/coup system (new) | 2 | Boundary vs faction_state unestablished [OPEN]; home doc [GAP]. |
| 15 | settlement_economy | accounting | settlement | fold-vs-distinct vs #1 | 2-hold | Possibly the same system as settlement_layer Local Economy [OPEN — Jordan]; do not double-implement. |
| 16 | personal_combat | dice_pool | personal | **port `combat_engine_v1/` as a package** → `systems/engine/combat_v1/` | **3 — first dice port** | RATIFIED (ED-900–904 + 06-06 fix). Replaces stale `CombatLogic.gd`. F3 outcome Key type via W3.4 first. Martial-traditions D-α/β/γ/δ stay **data-parameterized** (tradition tables), not code forks. |
| 17 | social_contest | dice_pool | scene | Debate container + engine port (refit) | 3 | Python core sound; **N-gate** (verdict→CI/Legitimacy/faction wiring) is Jordan-owned and is what makes it load-bearing; `scene.contest_resolved` Key with Conviction-axis impact_vector is the keystone emit. |
| 18 | mass_battle | dice_pool | scene | Battle container + engine port (`tests/sim/mass_battle/`) | 3 | N1: **no canonical gate-vector/config manifest** — create one as the generated param export before porting; band realignment + per-cell CAP [OPEN]. |
| 19 | threadwork | dice_pool | personal/thread | `ThreadworkSystem.gd` refit | 3 | Emit-type W2.2 (`scene.thread_operation` vs `meta.thread_woven`) decided before port; doc status ambiguity [OPEN]; Coherence = continuous resource (Lessons 2/6 property checks). |
| 20 | fieldwork_knots | dice_pool | personal/scene | new system | 3 — **gated** | **Blocked by the 06-10 P1 canonical-line split** (Disposition/Knot model triple-divergence + Thread-Read stat). Fix canon first; never port a contradiction. |
| 21 | npc_behavior | accounting (procedures) | personal/scene | `systems/npc/` + AI (refit) | 4 | Procedures B/D/E keyed; Procedure C unkeyed [§10]; 2-cycle with social_contest — dampers [OPEN]; OWN-5 cascade BUILT, sim-pending (magnitudes not load-bearing). |
| 22 | npc_memory | state_reader | personal | Memory store under Meta/NarrativeState | 4 | Home doc [GAP] (doc-12 §2.3 bridge); Memory Query API per substrate §4.4. |
| 23 | miraculous_event | state_reader (event source) | personal/scene | world-event emitter | 4 | System-vs-event-source classification [OPEN]. |
| 24 | scenario_authoring | manifest | peninsula | TriggerCondition/TriggerRule resources (**pattern exists**) | 4 | Authoring-time; injects env.crisis/disaster. |
| 25 | audit | state_reader | scene | debug/telemetry consumer | 4 | Runtime-vs-QA classification [OPEN]; pairs with the existing `WhyDiagnostic`/`WalkBackQuery`. |
| 26 | articulation_layer | armature_dot_product | personal/scene/provincial | `ArticulationLayerV30.gd` (exists; refit to substrate v2) | **4 — last runtime** | Universal `*` reader; the K8 fan-out question lives here; Chronicle/cut-scene tiers already ported (v30) — refit not rebuild. |
| 27 | campaign_architecture | — | — | — | **R** | Reclassified 06-10: a consolidation doc, not a runtime module; contents distribute to victory/threadwork/settlement/strain. Stub retirement [OPEN — Jordan]. |

**Cross-cutting (not modules, but conversion units):** `cross_scale/` — domain_echo (Domain Echo write-at-substrate, Part IV law #2), handoff_rules (the nine upward rules + the **downward gap**, Part VIII #1), zoom_in_out (maps to the existing GameDirector zoom stack + ContainerBase snapshot/restore), scene_dispatch (the 06-07 seam), articulation read-side.

**Rule for [GAP]-doc modules** (11 of 27 lack a home doc per the contract gap-notes): a module converts only against an authored spec; until the home doc exists, the module contract + extraction artifact is the spec seed, the port is flagged `[PROVISIONAL]`, and any value not traceable to canon halts the port rather than being invented (`<core_rules>` don't-guess).

---

## PART III — THE GODOT REPO AS IT STANDS (what's live, what's superseded)

### III.1 Live and structurally sound (keep / refit)
- **5 autoloads:** `EventBus`, `GameStateMachine`, `KeyStore` (the substrate store), `Meta` (41.6k — the single state owner: TrackerRegistry/FactionRegistry/CharacterRegistry/SettingState/NarrativeState, all mutation via `receive_consequence`), `SceneTimer`.
- **Container architecture:** `ContainerBase` (typed `SceneContext` in → `ContainerResult{consequences, narrative_log, scene_outcome, scene_degree}` out; `zoom_in_requested` typed; snapshot/restore for the zoom stack) + Conflict/Combat/Debate/Battle/Board/Narrative containers + `GameDirector` (23.7k) zoom-stack coordinator. **This is the wrapper harness the 06-06 conversion conversation identified: build the spine once, plug systems in.** It matches the module-contract shape exactly (context=consumes, result=emits) — the seam is already typed.
- **Kernel seed:** `CoreResolver`/`CoreEngine` + `RollContext`/`RollResult` + six `resolution_modes/` strategy classes + `ConsequenceRouter` + `Tracker`/`TrackerRegistry`/`TrackerThreshold` (the 4-bucket containers, partially).
- **Data discipline:** 26 typed Resource classes + .tres instances (22 characters, 15 triggers, T1–T17 + 36 settlements in libraries); data-driven triggers; `tests/` (14 suites + coverage_matrix); CI workflow.
- **Substrate v1:** `Key.gd` (content-hashed id, §6 determinism intent), `KeyTypeRegistry.gd`, `KeyValidator.gd`, `KeyStore` autoload, `WalkBackQuery` causal walks, articulation v30 + chronicle generator — Phase 5a (PP-684–688) was implemented through ~2026-05-04.

### III.2 The drift census (superseded by design advances since 2026-05-04 — refit targets, severity-ranked)
| # | Sev | VG element | Superseded by | Disposition |
|---|---|---|---|---|
| D1 | **P1** | `Key.gd` schema v1 — bare-string `targets[]`, scalar `salience` field, no per-target `impact_vector[4]`/`stat_deltas`, no `symbolic_dimensions[4]`, no `time_horizon`/`permanence`, single `scale` not `scale_signature[]` | `key_substrate §2.1` current (the vectorized schema the whole armature interpretation depends on) | **Substrate v2 migration is Gate-0 work** (Part VI). Per-observer salience is *computed* (§4.5), not stored. |
| D2 | **P1** | `CombatLogic.gd` (32k) — pre-ED-901 combat (old pool, weapon model) | `combat_engine_v1/` (CANONICAL) | Reference-only; **replaced** by the package port (module 16). Parity is vs Python canon, never vs old GDScript. |
| D3 | **P1** | `DomainActionSystem.gd` — pre-d+σ resolution | d+σ ED-874 (ratified) | Refit to the d+σ regime (module 12). |
| D4 | P1 | `FactionData.mandate` as exported base field; faction victory logic | LPS-2e (Mandate = derived settlement aggregate) + GD-1 (single victory) | Mandate → read-only derived getter (R4 discipline); victory paths struck. ED-784 comment sweeps landed but the schema didn't. |
| D5 | P2 | `data_serialization_spec.md` schemas (1:1 to retired `sim_framework/state.py`; 34 settlements; 8-faction list; weapon 3-axis only) | module_contracts + Descriptor Registry + 35-settlement/17-territory geography + weapon vector objects (W3.1) | Regenerate schemas from the registries (Part V). |
| D6 | P2 | Open since 04-27: Church L+PS 4/4 vs canonical 5/5; Church Man/Wea values | `stats_1_7_scale` / workplan §4.1 | Carried `[OPEN — Jordan]` in design_sync; resolve at first faction-data export. |
| D7 | P2 | `implementation_sequence.md` G1–G7 (manager-per-system autoloads, 04-18 system list) | W4.1–W4.3 + Phase E + this doc | Superseded by Part VI. |
| D8 | P3 | Stale conversion_ledger paths (pre-restructure) | live tree | Mechanical path sweep at next VG commit. |

### III.3 The architecture-doc conflict (consolidation trigger — three answers to "what are the autoloads")
`docs/architecture.md` (one autoload: Meta) vs `godot/scene_tree_architecture.md` (7: DiceEngine/GameState/SeasonManager/SceneSlateManager/NPCAIManager/VictoryManager/AudioManager) vs `sim/README` (6, mirroring the latter) vs **the live tree** (5: EventBus/GameStateMachine/KeyStore/Meta/SceneTimer). Per `<document_consolidation>` this is a collate→reconcile→one-master item. **Recommended reconciliation (mechanical-tier, anchored, Jordan-vetoable):** the live pattern is the keeper — *one state owner (Meta) + thin service autoloads (EventBus, KeyStore, GameStateMachine, SceneTimer; + KeyTypeRegistry and the Descriptor Registry as loaded tables)*; per-system "Manager" autoloads from the 04-18 doc become RefCounted systems under Meta/Director, per `docs/architecture.md`'s own "RefCounted is logic" rule. Anchor: Godot's autoload guidance (few global singletons; state centralized) + the repo's proven "call down, signal up / containers don't know each other" discipline. Action: one consolidated `valoria-game/docs/architecture.md` v2; supersede the scene-tree doc's autoload list; **re-point `sim/README`'s mirror table in the same change** (drift discipline). The *scene* hierarchy (MainScene swap, UILayer/ModalLayer, transitions table) in scene_tree_architecture.md remains valid.

---

## PART IV — THE TARGET ALL-DIRECTIONS HIERARCHY (what the converted game obeys)

### IV.1 The scales and their spine
`personal → scene → settlement → territory → province → peninsula`, with `thread` as the lateral metaphysical scale and the **season/Accounting clock** (engine_clock) as the temporal spine every system hangs off. The player's core UX flow is the zoom across these scales (PI `<design_doc_framing>`); in Godot that is the GameDirector container stack (Board → Battle → Combat, max depth 3, snapshot/suspend/restore) — already built.

### IV.2 The four directional laws (each already canonical; conversion must preserve all four)
1. **Downward = derivation (read-only).** Higher-scale values are computed aggregates of lower-scale substrate (Mandate = saturating settlement L/PS aggregate; Accord = floor(mean Order); Treasury income = Σ Prosperity×10). No system writes a derived value (R4 hook; VG mirror = no setters, getters only).
2. **Upward = echo at the substrate.** Scene outcomes reach higher scales by writing the *substrate* the aggregate derives from (Domain Echo → settlement ΔL/ΔPS → re-aggregate), never the aggregate itself — the F1 rule, and the same primitive the faction-stat inversion generalizes (`aggregate(holdings) ⊕ Σ national-event-Keys`, OPEN). Conversion encodes the five write-archetype re-routes (action_degree / event / accounting / domain_echo / cap) as the *only* upward write shapes.
3. **Lateral = Keys only.** No system keeps a private event channel; every consequential event is an emitted, registry-validated Key; consumers subscribe by type (§4.1 step 5, O(1)/async). In Godot: `KeyStore.emit()` implements §4.1 verbatim; the EventBus carries *UI/lifecycle signals only* — **signals are not Keys** (Keys are persisted facts; signals are transient wiring).
4. **Time = the Accounting cadence.** Stat changes ±-capped per season; accounting-archetype writes apply at the clock, not mid-scene (Consequence IMMEDIATE vs DEFERRED timing already in `docs/architecture.md` — keep it).

**The known gap in the directional laws:** top-down *event* delivery (law 3 downward) has no governing handoff rule (ED-1006). Until Jordan rules (Part VIII #1), ports treat downward delivery as engine-mediated subscription (a lower-scale module subscribing to a higher-scale Key type) and flag each such edge `[DOWNWARD — pending §3 ruling]`.

### IV.3 The conversion unit
**One module contract = one conversion unit = one parity target.** The contract (consumes/emits/state/resolver/scale) is simultaneously: the GDScript class's typed interface, the subscription registration set, the param-export manifest, and the adjudicator's check target (A1–A9). The flatten artifacts (Part I.5) supply the verbatim internals. A port is *done* when (a) the adjudicator-equivalent checks pass on the GDScript side, (b) the golden-master parity scenario matches the Python reference, (c) the property checks (NERS lessons: bounded loop gain, impact-uniformity, no accidental cliffs on continuous resources, clocks legitimately stepped) pass.

---

## PART V — THE CONVERSION DICTIONARY (Python → Godot 4.6)

### V.1 Construct mapping
| Python construct (ttrpg) | Godot construct (valoria-game) | Notes |
|---|---|---|
| `sim/autoload/*.py` services | The 5 thin autoloads + Meta (Part III.3 ruling) | dice_engine → kernel module accessed via service, not its own global per old G1. |
| Module (`resolve_*` fns + dataclass results) | `class_name XSystem extends RefCounted` + typed result `extends RefCounted` | "RefCounted is logic" — no scene-tree presence for resolvers. |
| Module contract consumes/emits | `KeyStore.subscribe(type, callable)` at load + emits via `KeyStore.emit()` (§4.1) | TYPE_SUBSCRIPTIONS table generated from module_contracts.yaml — *the contract registry compiles to the subscription table.* |
| Key (substrate §2.1) | `Key extends Resource` v2 (per-type payload subclasses optional) | §8.8; **K8-gated alternative:** RefCounted runtime Keys + Resource serialization only at save, if Resource alloc costs the frame budget. Decide on K8 verdict, behind one factory. |
| KEY_LOG / CAUSAL_GRAPH | Typed-array Resource / sparse `Dictionary[StringName, PackedStringArray]` | Save = serialize the log (replay = re-execution). |
| 4 buckets | Pool = computed (never stored) · Derived = read-only getter (no setter exists) · Track = `Tracker` bounded · Clock = `Tracker` monotonic + `TrackerThreshold` | TrackerRegistry stays the mutation choke point; tracker key format `scope:owner:id` stays. |
| Descriptor/Key-type/clock registries (yaml) | Resource tables loaded at boot; **bind-at-load** StringName keys; reverse index kept | Generated from the ttrpg yaml by the export ritual — never hand-transcribed (the standing `[GAP]` Phase E names: verify, then adopt exports). |
| Conviction/axis vectors | `PackedFloat32Array` (13 / 4) + const name→index maps; CONVICTION_AXIS_MATRIX as a const table or Resource | Fixed-shape, name-indexed (alignment checklist #3). |
| `params/*.md` + `config.py` values | **Generated, generator-stamped export per system** → `res://data/<system>_params.tres|json` | Phase E ritual #1; the per-system exports accumulate into the pipeline — not built upfront. `d10_success_probabilities.json` is already a ready fixture. |
| `combat_engine_v1/` package | Mirrored GDScript package `systems/engine/combat_v1/` (wrapper/systems/core/config/combatant/tradition) | Package-for-package; `config.py` → generated CombatConfig resource; the 19 censused RNG draw sites become named draw calls (V.2). |
| `tests/sim/*` harnesses | gdUnit4 suites + golden fixtures (JSON) **generated by the Python side** | Headless CI runs (engineering floor). |
| `RuntimeError` on canon violation | `push_error` + typed error result (no exceptions in GDScript) | Property: a violated invariant must be *visible in the result*, not swallowed. |
| Python `dataclass/NamedTuple` returns | Typed RefCounted result objects | Never bare Dictionaries across module boundaries (sim/CONVENTIONS rule carries over). |
| Hooks/ops, index pipeline, adjudicator | **Stay Python** (repo governance, design-side) | VG's enforcement = typing + lint + gdUnit + CI + the GDScript-side contract checks. |

### V.2 Determinism & parity protocol (the load-bearing engineering decision)
Cross-language bit-parity of RNG streams is a false goal; **parity is asserted at the state level under controlled draws**:
1. **One injected seeded RNG service** (Phase E floor) — no scattered `randi()`; every stochastic site is a *named draw* (`rng.draw(&"combat.strike_roll", n)`), which makes the draw census (already done for combat: 19 sites) executable.
2. **Recorded-draw replay harness:** the Python reference runs a scenario with a seeded stream and records `(site, values)`; the GDScript run replays the recorded values through the same named sites and must reproduce **identical downstream state and emitted Key sequence**. This isolates logic parity from RNG-implementation differences. (Anchor: standard deterministic-replay porting practice; the substrate already mandates per-emission RNG seeding, §6.1.)
3. **Statistical parity** (second tier): same seed-class Monte Carlo on both sides; compare distributions against the canonical tables (degree frequencies, ED-504-class checkpoints), tolerance-banded.
4. **Float discipline:** discrete-pool and d+σ regimes are integer/threshold logic at the boundaries — assert in integer domain at degree thresholds; continuous-Normal regime compares quantized (e.g. round to 1e-6) with documented tolerance; never assert raw float equality across languages (§6.3 reproducibility holds *within* a runtime, not across Python↔GDScript).
5. **Key-log equality is the master parity check:** for a fixed scenario + recorded draws, the emitted Key sequence (types, targets, stat_deltas, causes) must match exactly. Save-as-Key-log makes this the same machinery as save/replay testing — one harness, three uses.

### V.3 Language-semantics watchlist (apply per port)
Exceptions→error results (above) · integer division (`//` vs `/` on ints — GDScript `int/int` is float; use `floori`/`@warning_ignore` discipline) · dict iteration order (insertion-ordered in both, but **never order-dependent logic**; sort keys at any serialization point) · StringName vs String at every hot key · typed Arrays everywhere (floor rule) · no default-mutable-argument idiom · `match` vs Python dispatch tables (prefer tables generated from contracts) · GDScript has no dataclass `frozen` — immutability of Keys is by convention + validator, enforce via no-setter pattern.

### V.4 What the Python corpus becomes (the carried Jordan decision, with a recommendation)
The `sim/` armature + engines remain the **specification oracle** for as long as a system's parity harness needs a reference: each module's Python implementation is demoted only after its GDScript port holds golden-master + property checks across the canonical scenario set, at which point the Python module gains a `[PORTED — oracle retained|retired]` flag. Recommendation (mechanical-tier): retain oracles at least through cross-scale integration (the seams are where ports diverge), retire per-module afterward to avoid dual maintenance. Final call is Jordan's (carried docket item: "Python-sim long-term role").

---

## PART VI — SEQUENCING (gates, stages, and the per-module ritual)

### VI.1 Gate-0 — before any module port (blocking preconditions, severity-ordered)
- **G0.1 Key schema v2 in valoria-game (closes D1).** Migrate `Key.gd` v1 → the substrate §2.1 shape: structured `targets[]` (actor_id/role/impact_vector[4]/stat_deltas) replacing bare strings; add `scale_signature[]`, `symbolic_dimensions[4]`, `time_horizon`, `permanence`, `causes[]`; retire the scalar `salience` field (salience is computed per-observer at interpretation, §4.1 step 4 — it is not a property of the Key). Deliverable: a v1→v2 field map + migration of the existing `.tres` Key instances + `KeyTypeRegistry` regenerated from the ttrpg registry yaml. Every other port consumes Keys; nothing sound can be built on the v1 shape.
- **G0.2 Godot-doc consolidation (closes D7/D8, resolves III.3).** One `docs/architecture.md` v2 stating the ruled autoload set (recommendation: the live pattern — Meta as single state owner + thin services), supersession banners on `implementation_sequence.md` (G1–G7) and the 2026-04-18 framing of `data_serialization_spec.md`, `sim/README.md` repointed to the same ruling. Ports must not inherit three contradictory answers to "what are the autoloads."
- **G0.3 K8 verdict.** The commissioned peninsula-scale §4.1 fan-out performance audit (W2.7) decides Key-as-Resource vs RefCounted-runtime (V.1) and any salience/subscription cost ceilings. `[ASSUMPTION: K8 not yet executed — no commit or report evidences it since 2026-06-06; if a verdict exists, substitute it here]`. Wave 1–2 ports may proceed behind the Key factory; Wave 4 (articulation, npc fan-out) must not start without the verdict.
- **G0.4 Key-type registrations (closes F2/F3 = executes W3.4).** Per the master workplan's own reconciliation: register `scene.combat_resolved` (C1, drafted) and `scene.thread_operation` (form per the W2.2 decision), and **drop** `scene.draft_da` (DA outcomes are already keyed as `da.*`); `mechanical.scene_activated` is already resolved (renamed `scene_entered`, present, `1e98edb`). This lands *before* the combat/threadwork ports emit — the generated TYPE_SUBSCRIPTIONS table can only carry registered types, the adjudicator's A-checks will (correctly) fail the port otherwise, and W4.1 declares W3.4 as a dependency.
- **G0.5 Per-module canonical gate.** A module ports only from canonical/ratified sources at fresh SHAs; the 11 `[GAP]`-home-doc modules port `[PROVISIONAL]` against contract + flatten artifact only and **halt on any value untraceable to a cited source** (no invented constants — the sim_fabrication discipline carries to GDScript). fieldwork_knots stays gated on the P1 canonical-line fix (a11e2fa diagnostic); porting a split line would freeze the contradiction into the engine.

### VI.2 Stage 1 — the spine (one session-class unit of work)
Build, in valoria-game, scene-tree-free and headless-testable: (1) the **kernel** — one resolver, three regimes (discrete d10 pool / continuous-Normal / d+σ) + the two non-probabilistic archetypes, attribute-agnostic per master_workplan §8; (2) **KeyStore v2** implementing §4.1's update rule verbatim (validate → append → observers → interpret/salience/memory/apply → typed subscriptions O(1)/async → causal-graph edges → awareness), with save = serialize-the-log; (3) the **seeded RNG service** with named draws (V.2); (4) the **statechart** for game flow + the typed event bus under the "events are past-tense facts, commands call down" rule (Workplan-R2 Phase E floor); (5) **generated registry loaders** (descriptor/Key-type/clock tables from the ttrpg yaml). First parity target: the dice kernel against `references/d10_success_probabilities.json` — a ready fixture, zero new harness work. Engineering floor throughout: typed GDScript, gdlint/gdformat, gdUnit4, headless CI.

### VI.3 Stage 2 — per-module ports in wave order (Part II), each through the Phase E ritual
Per module, in order: **(1)** generated, generator-stamped param export for the system (`res://data/`); **(2)** port written against the module contract + flatten artifact, internals verbatim from the cited sources; **(3)** golden-master parity — Python reference runs the canonical scenario set with recorded draws, GDScript replays, Key-log equality asserted (V.2); **(4)** property checks (bounded loop gain, impact-uniformity, no accidental cliffs, clocks legitimately stepped); **(5)** adjudicator-equivalent checks (A1–A9 analogue) on the GDScript side; **(6)** commit + `docs/conversion_ledger.md` entry + `docs/design_sync.md` sync stamp at the ttrpg SHA consumed. The `[GODOT-IMPACT]` cross-repo tag protocol (scene_tree_architecture Phase 5.5) stays in force in the other direction: ttrpg design changes touching a ported module mint a sync obligation.

### VI.4 Stage 3 — cross-scale, then surface
Only after the spine + first modules hold: scale-transition handoff rules (§3's nine, upward) + the interim downward rule (IV.2), Domain Echo, zoom in/out against the live `ContainerBase`/`SceneContext` seam, articulation **last** (it reads everything; K8-gated). UI binds to trackers/Key log read-only; save/load ships as Key-log serialization + replay (the same harness as parity, third use). The 20-week G1–G7 calendar is not replaced with a new calendar: sequencing here is dependency-ordered, sized in session-class units, and Opus-executed per Part IX — each port session consumes this document's Parts V–VI, the module's contract, its flatten artifact, and its param export as the complete work packet.

---

## PART VII — FRICTIONS REGISTER (severity-ranked; each names its resolution)
- **R1 — Key schema v1 ≠ v2** (P1). Gate-0 G0.1. Everything downstream consumes Keys.
- **R2 — Stale GDScript ports look done** (P1). `CombatLogic.gd` (32k) and `DomainActionSystem.gd` predate combat_engine_v1/d+σ ratification. Resolution: parity is asserted against the *Python canon*, never against prior GDScript; stale files are replaced by the `combat_v1` package port (D2/D3), not patched.
- **R3 — Three contradictory architecture docs** (P1-legibility). Gate-0 G0.2; the III.3 ruling is Jordan-vetoable (Part VIII #5).
- **R4 — Cross-language RNG/float divergence** (P1 if unmanaged, retired by design). Named draws + recorded-draw replay + integer-domain assertions at thresholds (V.2). Bit-parity of RNG streams is explicitly *not* a goal.
- **R5 — §4.1 fan-out cost at peninsula scale** (P2, K8). Per-emission observer iteration × salience computation × Resource allocation is the one hot loop; subscriptions are O(1)/async by spec, but observer interpretation is not. K8 owns the verdict; the Key factory (V.1) is the prepared escape hatch.
- **R6 — Faction-stat inversion undecided** (P2). faction_state's write side is archetype-parameterized (Part II); read-side + derivation (Mandate clamp) port now, write re-routes land when Jordan rules. The port must not freeze the §14 stale side.
- **R7 — Downward-delivery gap** (P2, ED-1006). Interim rule IV.2 + `[DOWNWARD — pending §3 ruling]` flags; Jordan's call is Part VIII #1.
- **R8 — GDScript semantics** (P2, recurring). The V.3 watchlist applies per port; int-division and dict-order are the two that corrupt silently.
- **R9 — Python corpus end-state ambiguity** (P3). V.4 recommendation (oracle until cross-scale parity, then per-module retire); Jordan's call (Part VIII #2). Until ruled, *nothing* in sim/ is deleted on port completion.
- **R10 — Naming-vocabulary collisions imported into code** (P3). The 3-way "Piety Track" collision, CI/Influence stat-vs-clock overload, and the D6 scope-set drift all become *identifier* collisions in GDScript. Namespaced StringNames (`&"territorial_piety.track"` vs `&"conviction_track.scar"`) contain the damage; resolution of the names themselves stays an editorial item, carried.

---

## PART VIII — CONSOLIDATED [OPEN — Jordan] REGISTER (conversion-specific; all vetoable)
1. **Downward Key delivery** (ED-1006 headline): extend `scale_transitions §3` with downward handoff rules, **or** declare engine-mediated subscription exempt from transition coverage. Until ruled, ports use the interim rule (IV.2) and flag every downward edge.
2. **Python corpus role**: specification oracle until cross-scale parity then per-module retirement (recommended, V.4), or earlier retirement. Carried from the Workplan-R2 docket verbatim.
3. **Faction-stat inversion** (`aggregate(holdings) ⊕ Σ national-event-Keys`, + DECIDE-1/2, Intel expand-vs-fold, CI/Influence naming): carried from the consolidation master; gates faction_state's write-side port only (R6).
4. **Key runtime form**: `Resource` (the §8.8 default) vs RefCounted-runtime + serialize-at-save — decide on the K8 verdict; both live behind the one factory until then.
5. **Autoload ruling** (III.3): adopt the live pattern (Meta single state owner + EventBus/GameStateMachine/KeyStore/SceneTimer as thin services) as architecture.md v2, or direct otherwise. G0.2 executes whichever ruling stands.
6. **First module target**: settlement_layer (recommended — deterministic_accounting, canonical home doc, fresh flatten with the four decision-grade gaps explicitly carried, exercises derived-value discipline end-to-end); alternatives: victory (smallest) or combat_v1 (largest validated, parallel-session-owned — coordinate before claiming).
7. **D6 Church L+PS 4/4 vs canonical 5/5** — the standing valoria-game design_sync open item; lands with the settlement_layer port either way.
8. **Standing design dockets carried by reference, not duplicated here**: martial-traditions D-α/β/γ/δ (parallel session), mass-battle band/CAP/ED-910/909, weapon-physics Stage-2 constants, victory treaty.py wiring, OWN-5 SIM-DEFECT confirmation — each blocks only its own module's port-completion, none blocks the spine.

---

## PART IX — IMMEDIATE NEXT THREE SESSIONS (the front-end plan this document orchestrates)
- **S1 (this session + its successor):** commit this strategy (done by this session's close); then execute Gate-0's documentation half — architecture.md v2 + supersession banners + sim/README repoint (G0.2), and author the Key v1→v2 field map (G0.1 spec, not yet the migration). Output: the conversion has one self-consistent doc surface.
- **S2 (spine build):** Stage 1 in valoria-game — KeyStore v2 + kernel (3 regimes) + named-draw RNG service + statechart skeleton + generated registry loaders; dice-kernel parity green against `d10_success_probabilities.json`; gdUnit4 + headless CI green. This is valoria-game's first commit since 2026-06-06 and re-opens the design_sync cadence.
- **S3 (first module ritual):** the chosen Wave-1 module (Part VIII #6) end-to-end through VI.3's six steps — the ritual proven once is the template for the remaining ~24. Each subsequent port session is an Opus-executed work unit whose complete packet is: this document (Parts V–VI), the module contract, the flatten artifact, the param export, and the Python reference.

---

## X — PROVENANCE (sources read in full or at stated depth, this session)
ttrpg @ ~496f3d5: `handoffs/active-work-index-2026-06-09.yaml` · `designs/audit/2026-06-09-session-consolidation-master.md` · `references/module_contracts.yaml` (27 modules) · `references/ecosystem_versions.yaml` · `designs/audit/2026-06-06-architecture-map/` (hierarchy map, master workplan §0–§8.2, wiring analysis headers+Part 4) · `designs/audit/2026-06-09-ecosystem-reconciliation/` (report + workplan R2) · `sim/README.md` + `sim/CONVENTIONS.md` · `godot/` (all four) · `designs/architecture/key_substrate_v30.md` (index + §4.1 + §8.8) · `scale_transitions_v30` (index) · `skills/valoria-module-adjudicator/SKILL.md` (headers) · 60-commit history since 2026-06-06. valoria-game @ design_sync 2026-05-04/9057663f: full tree walk · `docs/` (architecture, design_sync, conversion_ledger) · `Key.gd` · `KeyTypeRegistry.gd` · `ContainerBase.gd` · `SceneContext.gd`. Conversation corpus: 18 project chats 2026-06-06→10 (the eight 24-hour sessions consolidated in Part I.5 plus the 06-06 Godot-scope session whose ContainerBase findings Part III carries).

*End of v1. Status PROPOSED; every recommendation above is Jordan-vetoable; the [OPEN] register (Part VIII) is the veto surface.*
