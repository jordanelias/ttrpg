# VALORIA — Unified Interdependency & I/O Master
**Date: 2026-06-11 · Status: PROPOSED (Jordan-vetoable throughout) · Scope: the whole game as one addressable interdependency graph — canon → campaign flow → architecture → mechanical systems → modules, all directions, all scales**

`[SELF-AUTHORED — bias risk: every consolidated input was authored by my own sessions. This master folds them; it does not re-bless them. An independent reviewer should re-test the unified OPEN register (§8) against the editorial ledger, which is not swept here. The verdict's §7 reviewer addendum is the one external-leaning counterweight and is carried forward in §8/§9.]`

**What this is.** The single working master for "how everything wires together." It consolidates the three complementary graph views built across 2026-06-06 → 06-11 (structural topology · module I/O · temporal flow) plus their per-system feeders into one navigable layer. It is a **consolidation, not a new analysis**: no mechanical value is invented here; every row traces to a cited source view read in full this session. Substantive conflicts are **carried OPEN for Jordan**, never silently resolved — this is document hygiene, not design authority (PI `<document_consolidation>`).

**What this is NOT.** It does not re-transcribe the full value/formula/gate tables — those live in `game_flow_flat_spec_v1.md` (registries A–G) and the per-system design docs; this master points to them. It does not regenerate or hand-edit the generated graph artifacts (mermaids, `module_map_flat.md`) — those regenerate from `module_contracts.yaml` (§10).

---

## §0 — PROVENANCE & CONSOLIDATION RECORD

**The three views consolidated (each a complement, not a rival — they cover different axes of the same machine):**

| View | Axis it owns | Source files | Last commit |
|---|---|---|---|
| **Structural topology** | the static wiring: substrate → taxonomy → actors → 17 systems → edges | `2026-06-06-architecture-map/valoria_system_hierarchy_map.md` · `…/valoria_system_wiring_analysis.md` | `f1b3f4c9` (2026-06-09) |
| **Module I/O graph** | the 27-module Key-flow graph + all-directions coverage + per-module conformance | `2026-06-10-module-adjudication/verdict_full_graph.md` · `…/module_map_flat.md` (generated) | `8d8a2081` / `c8e982b5` (2026-06-10/11) |
| **Temporal flow** | the campaign as a clock: init → season tick → arcs → resolution, with directed cross-scale edges | `2026-06-11-game-flow/game_flow_analysis_v1.md` · `…/game_flow_flat_spec_v1.md` | `c005da27` / `6199d83a` (2026-06-11) |

**Feeders (per-system flatten + flowchart + state-graph; inputs to the above, stay live as inputs):**
- `2026-06-09-faction-comprehensive/faction_play_system_flatten.md` (+ `.mermaid` ×2) — `df489902`
- `2026-06-09-massbattle-comprehensive/massbattle_flow_state_flatmap_critique.md` — `bedbf41d`
- `2026-06-09-personal-combat-comprehensive/combat_engine_flow_and_state_map.md` — `6165471a`
- `2026-06-10-settlement-analysis/settlement_flattened_map.md` (+ `.mermaid` ×2) — `7cf58954`

**Shared spine (the generated source of truth; never hand-merged — regenerated):**
- `references/module_contracts.yaml` (v2.1/v3 schema, commit `c8e982b5`) → generates `module_map_flat.md` + `module_flowchart.mermaid` + `state_graph.mermaid`.

**Binding capstone (stays the live workplan; this master is its canon-state graph input):**
- `2026-06-10-master-workplan-v3/valoria_master_workplan_v3.md` (`ac49cea6`) §6 cross-lane dependency map already *binds* the module verdict + map + contracts. This master is the unified read-side of that binding.

**Disposition.** The three authored analysis views (hierarchy_map, wiring_analysis, game_flow_analysis, game_flow_flat_spec, verdict_full_graph) are **consolidated into this master** (supersession marked, non-blocking; git preserves them — §11). The generated artifacts, `module_contracts.yaml`, the per-system feeders, and `workplan_v3` **stay live**.

### §0.1 — Reconciliation note (why this adds value, not bulk)
The three views each carry a contradiction/finding register, and **those registers overlap heavily** — the same defect appears under a wiring `Fn`, a flat-spec `Fn`, and a verdict `An`/ED-NNN. The consolidation work is the **de-duplication** in §8: one unified OPEN register, each entry mapped to its canonical mechanism, ledger ED, severity, and the single Jordan decision that closes it. The structural/loop/NERS content (§5/§7/§9) is likewise merged so the three damper tables and the two all-directions passes become one.

---

## §1 — THE SUBSTRATE (Tier 0 — what everything is made of)
*Source: hierarchy_map Tier 0 (`key_substrate_v30`, `key_type_registry_v30`, `derived_stats_v30 §1`); flat-spec B1/F.1.*

**The Key is the atomic record.** Every consequential event is a typed, validated, append-only Key. **No system keeps a private channel; every system emits Keys and consumes Keys.** Save state = `initial_conditions + Key log`; load = deterministic replay (the save file *is* the campaign history). Key emission is the **only** state-mutation path.

- **Schema (the universal wrapper):** `{id, type, source_actor, emitted_at{season,sub_step}, causes[], targets[]{actor,role,impact_vector[4],stat_deltas}, scale_signature[], symbolic_dimensions[4], visibility, time_horizon, permanence, payload}`. `causes[]` is the provenance backbone — the causal graph linking all events.
- **7 type families** (≈30 subtypes): `scene_event · da_outcome · mechanical_event · state_transition · environmental · scene_outcome · system_meta`. Adding a type = Class-B registry extension.
- **4-axis conviction space** (the vector basis for all symbolic effect): `hierarchical · sacred · instrumental · traditional`. `impact_vector` and `symbolic_dimensions` are the two 4-axis arrays that vectorize a Key. (5th axis = deferred Class-B extension.)
- **The core engine is dual-mode and attribute-agnostic:** discrete d10 success-pool ≡ continuous-Normal sampling (videogame/Godot mode; fractional Ob/TN, continuous degrees). No single universal resolver — one probabilistic kernel, the archetypes below sit on top.

**Five resolver archetypes** (flat-spec B1):
| | Archetype | Rule | Used by |
|---|---|---|---|
| A | Dice pool | d10 vs TN 7; degrees Failure/Partial/Success/Overwhelming; crit net ≥ 4 | all personal-scale rolls |
| B | d+σ | `M = stat − difficulty`; `P = clamp(0.5 + 0.1·M, 0.05, 0.90)`; uniform slope across 1–7 (closes small-pool √N) | every faction-stat action (ED-874) |
| C | Deterministic accounting | ledger formulas, no roll (Mandate, CI sequence, muster, income) | strategic Accounting |
| D | Clock advance | increment toward thresholds | world + scene clocks |
| E | Armature dot-product | `Σ_axes armature[axis]·symbolic[axis]·impact[npc][axis]`; cut-scene ≥ 0.40 | articulation read-side |

---

## §2 — THE VALUE TAXONOMY (Tier 1 — the containers)
*Source: hierarchy_map Tier 1 (`derived_stats_v30 §3/§14`, `clock_registry_v30`).*

Four buckets under the Keys; **classification dictates legal operations** (this is load-bearing — conflating buckets is the root of the value-drift findings in §8):

1. **Base stats (1–7):** faction (Mandate\*, Influence, Wealth, Military, Intel, Stability) · settlement (Legitimacy, Popular Support 0–7; Prosperity, Defense, Order 0–5; Fort 0–4) · personal (End, Str, Agi, Cog, Cha/Presence†, Foc, Recall, Spirit, Attunement, Bonds + History). \*Mandate is **derived** (settlement aggregate). †name drift, §8.
2. **Pools** — computed at action time, never stored (resolver INPUTS): Combat `max(5,H+6)` · Argue `(P×2)+H+3+style` · Thread `(Spi×2)+H+TPS` · Fieldwork `(P×2)+H+3` · Knot `(Bonds×2)+3` · Mass `min(Size,Command)+Command`.
3. **Derived values** — `Stat×multiplier`, drain/refill, **never written directly** (write the source): Health, Stamina `(3·End)+(2·Spi)`, Composure, Concentration `(3·Foc)+(2·Spi)`, Treasury `W×100`, Discipline `Stab×10`, Local Economy, Garrison, Public Order, **Mandate** (settlement aggregate).
4. **Tracks** (bounded oscillating: Disposition, Piety, Certainty, Coherence, TS, Renown/Standing, Accord, PT, loyalties) and **Clocks** (monotonic: MS, CI, IP, Turmoil/Strain, Evidence, Saturation, Coup Counter).

---

## §3 — THE ACTOR MODEL (Tier 2 — characters)
*Source: hierarchy_map Tier 2 (`conviction_taxonomy_v30`, `conviction_axis_matrix_v30`, `key_substrate §2.5`).*

An actor = base attributes + derived resources/tracks + an **ethical vector**:
- **13 Convictions** (weighted vector, Structured Concentration 1–3 primaries @ 0.6–0.8 + background @ 0.2–0.4): Faith · Authority · Order · Scholastic · Utility · Equity · Liberty · Precedent · Community · Identity · Warden · Virtue · Honor.
- **13×4 matrix** → `armature_position[axis] = Σ_c convictions[c]·MATRIX[c][axis]` (a derived 4-vector; never authored directly).
- **Self-Other orientation** — scalar in `[−1,+1]`, modulates attribution `attributed = raw·(1 − 0.5·max(0,orient))`; drifts (κ≈0.03) → emergent fall-from-grace arcs.
- **Armature interpretation** (archetype E) is **the bridge from the Key substrate into character psychology** — drives Concern salience, Disposition, Memory.
- Named leaders (Crown/Church/Hafenmark/Varfell/Guilds/Löwenritter/Restoration) are actor instances carrying convictions, pressure-point type, TS, Certainty, and a 7-step AI Priority Stack.

---

## §4 — THE SYSTEMS (Tier 3 — resolvers as wrappers)
*Source: hierarchy_map Tier 3 (each system IN→resolver→OUT) merged with verdict §3 per-module conformance. Full IN/OUT detail per system in hierarchy_map; this is the node table.*

Every system is a wrapper: pulls inputs (stats/derived/tracks/clocks/Keys) → runs one archetype → emits outputs that **always include Keys**. Conformance column from the module-adjudicator run (27 violations / 58 warnings; **graph verdict OPEN — incomplete/under-specified, not unsafe**).

| Scale | System | Resolver | Emits / role | Module conformance (verdict §3) |
|---|---|---|---|---|
| Personal | **Combat** | A | `scene.battle_concluded`/state | **stub** — F3: no `scene_outcome.combat` subtype (combat-engine handoff owns) |
| Personal | **Social Contest** | A+D | `scene.contest_resolved` | CONFORMANT (clean) |
| Personal | **Threadwork** | A | `meta.thread_woven`/`knot_*` | NON-CONFORMANT — `scene.thread_operation` unregistered (F2) |
| Personal | **Investigation/Fieldwork** | D+A | `scene.investigation_resolved` | CONFORMANT — universal reader |
| Personal | **Knots** | A | `meta.knot_formed/ruptured` | (under fieldwork) CONFORMANT |
| Strategic | **Faction Layer** | **B (d+σ)** | `da.*`; most fully keyed hub | `faction_state` CONFORMANT; `faction_politics`/`domain_actions` NON-CONFORMANT (no home doc, F2) |
| Settlement | **Settlement/Territory** | C (saturating aggregate) | Mandate, Accord, control | NON-CONFORMANT — A6 consume seams; stale pre-LPS-2e index; `settlement_economy` duplicate? `[OPEN]` |
| Strategic | **Military** | C | units, muster | rides faction `da_outcome` (not separately keyed, by design) |
| Scene | **Mass Combat** | A in 7-phase machine | `scene.battle_concluded` | NON-CONFORMANT — naming drift (F2) |
| Provincial | **CI Political** | D+B | CI milestones, Seizure | CONFORMANT — **isolated** (CI unkeyed; §10 migration candidate) |
| Provincial | **Victory** | C (state-reader) | win/era declarations | CONFORMANT — **isolated** (era-transitions unkeyed); doc DESIGN-not-canonical |
| Peninsula | **Peninsular Strain** | D | `env.*` shocks (source_actor=null) | NON-CONFORMANT — A6 down-scale producer; `env.crisis` orphan |
| Connective | **Scale Transitions / Domain Echo** | C | the queued cross-scale delta | the bottom-up bridge (PASS); top-down absent (§5/§8) |
| Connective | **Articulation Layer** | **E** | `state.belief_revised`/`meta.*` | CONFORMANT — **the universal reader** (Key log → narrative) |
| Connective | **Campaign Architecture** | C | `mechanical.*` season spine | **stub** — reclassified consolidation doc, retirement recommended |
| Connective | **NPC Behavior** | E/C | `scene.*`; **the observers** in §4.1 | NON-CONFORMANT — 4× F2 unregistered project/displacement types; A6 consume |
| Connective | **Clock Registry** | manifest | container manifest (not a system) | CONFORMANT — PROVISIONAL staleness flags |

**Reviewer caveat (carried from verdict §7):** ~11/27 modules are *registry-derived shadows* with no home design doc — counting them `extracted` overstates coverage. Honest reading: **~14 specified systems + ~11 registry-shadow + 2 stubs**, and the A6/F2 findings concentrate in the shadows.

**Execution substrate (the architecture/runtime layer — where the graph runs).** *Source: game_flow §1.4 (`videogame_mode_spec §1`, valoria-game scene tree).* **GameDirector** (zoom stack, max depth 3) + **ZoomManager** + **ConsequenceRouter** (Domain Echo) over six containers — **BoardContainer** (strategic map / faction actions / accounting), **CombatContainer**, **BattleContainer** (mass battle + SoloResolution auto-resolve), **DebateContainer** (social contest), **NarrativeContainer** (fieldwork / exploration / dialogue) — plus autoloads (event bus, KeyStore, SeasonManager/GameStateMachine, SceneTimer, TrackerRegistry). The Python `sim/` armature mirrors this tree 1:1 for golden-master parity. **There is no GM** — every "GM decides" resolves to Authored / Deterministic / AI-driven / Player-choice / Default (videogame_mode_spec §3).

---

## §5 — THE INTERDEPENDENCY GRAPH (the heart — all directions, all scales)
*Source: wiring Part 3 (structural edge classes) ⊕ flat-spec E (directed cross-scale edges) ⊕ module_map §1 (27-module Key-flow flowchart) + §4.5 (Key-type I/O matrix) ⊕ verdict §4 (all-directions coverage). The full type-granularity emitter→consumer table is `module_map_flat.md §4.5` (generated; regenerate, don't hand-edit). This section is the unified navigable layer over it.*

**The universal mechanism.** Every edge in the graph is a Key crossing the single-update rule (`key_substrate §4.1`): `validate (registry + invariants + causes[] DAG) → KEY_LOG.append → compute_observers → each observer's armature interprets → memory.record → apply_state_changes → TYPE_SUBSCRIPTIONS[type].consume() → CAUSAL_GRAPH.add_edge`. Emission is the only state-mutation path; `causes[]` is the provenance backbone. **No system has a private channel** — so the graph is, literally, the typed Key stream.

### §5.1 — By canonical direction (`canon/definitions.yaml`: top-down · bottom-up · vertical · diagonal · lateral · horizontal)
Coverage verdict carried from `verdict_full_graph §4`:

| Direction | Definition | Mechanism | Coverage |
|---|---|---|---|
| **lateral / horizontal** | same-scale | scene-internal (`scene_slate → social_contest / mass_battle`); provincial-internal (`faction_state ↔ domain_actions`) | **present — no gap** |
| **bottom-up** | substrate → aggregate recompute | Domain Echo (§5, capped ±2, 1/scene/faction, queued); Accounting recompute (province Accord = ⌊mean settlement Order⌋; Mandate = LPS-2e aggregate) | **covered & safeguarded** — A5 guards the illegal inverse |
| **vertical** | cross-scale | bottom-up branch yes; **top-down branch absent** | **half-covered** |
| **top-down** | aggregate → substrate delivery | the GAP: no `scale_transitions §3` rule delivers a provincial/peninsula `da.*`/`state.*`/`env.*` Key down to a personal/scene/settlement consumer | **OPEN (J-1 / ED-1006)** — the 19 A6 seams |
| **diagonal** | cross-scale AND cross-family | `da.*` (provincial DA family) → personal `npc_behavior` is both; same A6 gap | **absent — OPEN (J-1)** |

**The single structural finding:** the graph traces **up and across cleanly; down is unwritten.** Bottom-up is the deliberately narrow, capped, queued Domain-Echo channel; top-down has only *presentation* (the Scene Slate reads world state) and *modifier* (board degree → scene Ob) channels — no mechanical Key-delivery. This is the campaign's largest flow hole and is Jordan's to rule (J-1: engine-mediated-exempt vs explicit §3 down-rule). The 19 A6 "violations" are **contingent on that ruling** — if the substrate stream is declared scale-agnostic, they evaporate and the assessor gains a carve-out (verdict §7.2).

### §5.2 — The four structural edge classes (wiring Part 3)
- **3-A · Substrate edges (universal):** every system ↔ the Key log. **NPC Behavior** consumes the entire stream through armatures (NPCs *are* the observers in §4.1 step 4). **Articulation Layer** is the universal *reader* (Concern / cut-scene / Chronicle). **Campaign Architecture's Accounting** is the universal *sink* where queued cross-scale effects land. The causal graph (`causes[]`) links all of it.
- **3-B · Vertical / scale edges** (`scale_transitions §3`, the eight handoff rules): `Personal→Thread · Personal→Faction (Domain Echo) · Personal→Scene (Contest) · Scene→Faction (Domain Echo) · Thread→Faction · Thread→Mass · Mass→Personal (general duel) · Scene→Mass · Fieldwork↔All`. **All run upward or lateral — none downward (the J-1 gap).**
- **3-C · Resource / stat coupling edges** (the strategic spine): `Settlement L/PS → Mandate (saturating aggregate K=6) → Parliament votes → Victory`; reverse `Mandate → settlement L/PS (mean-reverting ±1/season)`. `CI → Seizure → settlement control`; `CI → Parliament weight (+⌊CI/20⌋)`; `thread events → CI (Epistemic trigger)`. `CI ≥ 60 → IP +2/season` — **the Church→Altonia coupling, the campaign's central pacing valve** (E3.3). `Threadwork → MS → Peninsular Strain → Accord/Turmoil → faction temperament`. `Mass Combat → MS −1 / IP +2 / Stability +1 / Accord 1`. `Wounds → all personal pools (−1D each)`. `Knots ↔ Disposition ↔ Coherence`. `Self-Other scalar → outcome attribution`.
- **3-D · Feedback loops:** see §7 (consolidated loop inventory).

### §5.3 — Directed cross-scale edges (flat-spec E — the wiring at edge granularity)
**E1 · Personal → Strategic** (deliberately narrow): scene→faction-stat (Domain Echo, 1/scene/faction, ±2/stat); scene→territory-Accord (Accord Echo, ±1/territory/Zoom-In, queued); scene→Thread/MS (Thread Echo + PP-198 Coherence payment); player-presence→faction-DA (+1D, 1/territory/season); player-rank→faction-orders (Standing 4+ sub-commands; leader replaces AI stack); scene-verdicts→CI/Legitimacy (N-gate wiring, **Jordan-owned**).
**E2 · Strategic → Personal** (the down-channel): world-state→Scene-Slate (built, presentation); board-outcome→scene-difficulty (built, C6.4); strategic-events→forced-presence (built, mandatory zooms + Witness + retrospective); **strategic-outcomes→personal-scale Keys (E2.4 — NO canonical rule, J-1/ED-1006; the single largest flow hole).**
**E3 · Intra-strategic couplings** (10 edges, E3.1–E3.10): the settlement→Mandate, Accord→Strain/IP, CI→IP, battles→MS, Strain-bands→stats, collapse→Strain/IP/insurgency, treaties→decay, Parliament→stats, Crown-weakness→Löwenritter, territory/battle-loss→Stability web.
**Full emitter→consumer at type granularity:** `module_map_flat.md §4.5` (the 44-type matrix — which of the ~30 registered + 7 unregistered types each module emits/consumes).

---

## §6 — THE TEMPORAL SPINE (how the graph executes in time)
*Source: flat-spec D (master sequence) ⊕ game_flow §3 (the season tick) ⊕ module_map §4.2 (Accounting spine). The campaign is `initial_conditions + Key log`; the tick is the master loop everything hangs off.*

**Initialization (Season 0 → live)** — 7 ordered steps (flat-spec D0; game_flow §2): difficulty/economy → world seed (15 playable territories / 35 settlements / 14 provinces / 3 duchies; PT, Accord capitals 3/home 2) → faction seed (stat tables; Mandate derived; Löwenritter dormant; RM statless) → clock seed (MS 72 · CI 28 · IP 20 · PI 7 · Turmoil 0 · loyalties · WC 0) → ignition seed (draw 1 of 6 Tensions cards; fuse fires randomized S8–S12) → character creation (3 Convictions validated; Coherence 10; Standing 0) → first tick.

**The season tick (the master loop)** — four-phase structure + 10-step Accounting:
- **S0 Season open** — `mechanical.season_change`; Duty assignment (Standing ≥ 1); **8-step Slate generation** (Mandatory Crisis P0 → Crisis Events P1 → Thread-state 2b → Duty → Conviction → NPC outreach → Territorial → Ambient, pruned to difficulty slate size; overflow → Witness Mode).
- **S1 Personal Phase** — player spends 3–5 scene actions; scenes resolve in matching containers (combat/contest/fieldwork/threadwork/travel); chaining allowed; Momentum on Conviction pursuit; **unpursued entries resolve by AI** (§4.5 consequence table — *the world does not pause*).
- **S2 Strategic Phase** (per active faction) — GD-2 mandatory pass first (Muster/Govern ≤ 3) → 7-step priority-stack + posture ladder → resolution by priority class (Intel → Military → Domain → Social → Thread → Special → Projects); **all faction-stat actions on d+σ**; player presence +1D.
- **INT Zoom interrupts** — mandatory (P0) / world-state (P1) zooms interleave D2/D3 at legal entry points; board degree shades scene Ob; **the BG clock never pauses** (PP-110); missed events → free retrospective next season.
- **S4 Cascade Phase** — Domain Echo application (caps); Cascade depth guard (cap 3, overflow → next Accounting).
- **S5 Accounting (10 steps, strict order)** — (1) attribute changes + Parliament votes + treaty ratifications → (2) Stability checks + collapse → (3) cooldowns → (4) clock advances (**CI sequence → MS → PI → 4c Accord checks → 4d Strain update + bands**) → (5) Church Attention + Thread Debt → (6) Turmoil consolidation → (7) threshold events + Warden + **GD-3 insurgency check** → (8) Warden Cooperation + loyalties → (9) occupation duration + Institutional Consolidation → (10) **Victory check** (2-consecutive counter) + season advance + Winter Year-End.
- **T Terminal & era transitions** (fire from S5.10) — MS 0 → Post-Calamity (campaign continues) · Second Calamity (sole terminal) · IP 100 → Occupation Era (winnable) · Anarchy Era (quorum-recoverable) · Generational transition (world persists) · Portrait Sequence (player-authored chapter end).

**Implementation-side execution order** (game_flow §10 — the wave order *is* the dependency order): **Wave S** spine (KeyStore + engine_clock + GameDirector/slate; empty calendar) → **Wave 1** deterministic (settlement → strain → CI → victory; *the world simulates, zero-player observable*) → **Wave 2** provincial actors (domain_actions d+σ + faction_state + GD-2/GD-3; *the factions play*) → **Wave 3** dice engines (combat/contest/mass/thread; *player scenes resolve natively, Echo has inputs*) → **Wave 4** actors + read-side (npc_behavior + memory + articulation + scenario). The vertical-slice test of "flow": seed → run Waves S–2 headless under fixed RNG → assert the Key log replays bit-identically and clock trajectories sit inside the derived bands → then zoom one player in.

### §6.1 — The metronome (clock rates; DERIVED pacing — game_flow §4/§5)
The composition rule: **personal dice feed clocks and Echoes → Echoes and Domain Actions move faction stats → faction stats move territory states → territory states drive world clocks → world clocks re-shape the Slate the player sees next season.** One loop, four scales, one log.

| Clock | Net seasonal drive | Key threshold (DERIVED window) |
|---|---|---|
| **CI** (28→) | +2..+3 uncontested / ≈0 firmly contested | Seizure window (60) opens ≈S11 uncontested, ≈S17–20 partial, never under firm contest; declaration on `((CI−60)/40)^3.3` curve; **CI 100 forces Mass Seizure** |
| **IP** (20→) | +0 consolidated / ≤+5 worst-case | Vanguard 75; Phase 1 @100 ⇒ floor ~16 worst-case seasons; full Occupation is a late-game alternative chapter |
| **MS** (72→) | ≈ −0.25/season peace / −1..−4 at war | Fragile edge (60, "observable anomalies") ≈3–12 war-seasons from start; **war-coupled revelation**; hysteresis +8 on recovery |
| **Strain** (0→) | self-limiting (+3 cap vs −1 clean −2 treaties) | ≤4 through a regional war with working diplomacy; the ≤6 victory gate is a *governance* test, not a peace test |
| **PI** (7→) | Hafenmark pressure | ≥20 auto-resolves → Crown elimination |

**Net campaign length (DERIVED):** ~12–25 seasons (3–6 in-game years) ≈ 50–100 player scenes at Normal — with era transitions extending, never ending, campaigns that go badly.

---

## §7 — THE LOOP INVENTORY (the feedbacks that decide whether the flow holds)
*Source: game_flow §8 (ratification + sim status) ⊕ flat-spec E4 ⊕ wiring 3-D ⊕ verdict A7 (PASS) ⊕ module_map §5. Defect test (resolution-diagnostic Phase 4): a loop is a defect only if **both undamped and unbounded.** Verdict A7: no cycle is undamped+unbounded — the graph is incomplete, not unsafe.*

| # | Loop | Path | Damper / cap | Status |
|---|---|---|---|---|
| **L1** | Faction death spiral | losses → Stability checks → more losses → collapse | **FSS-LOOP-1** deterministic floor (Stability ≤ 2 ⇒ Accounting check cannot reduce; collapse only via active Trigger 1–5) + Institutional Consolidation + one-time Survival Exception | **Ratified 2026-05-30** (sim: P(collapse) 0.41→0.97 only under sustained triggers) |
| **L2** | Wealth-0 Military ratchet | blockade → Wealth 0 → Military −1/season one-way | **FSS-LOOP-2** re-muster +1/Accounting while Wealth ≥ 1 | **Ratified 2026-05-30** |
| **L3** | Mandate runaway | territory → Mandate → easier acquisition → more territory | **LPS-2e** saturating `7T/(T+6)` + 0–7 clamp + mean-reverting feedback | **Ratified** (LPS-1/2e) |
| **L4** | Instability contagion | Accord ≤ 1 → Strain/IP → threshold effects → more Accord loss | Strain +3 cap / treaty-pair −2 cap; IP banded +0..+3; Accord passive normalisation (+1 after 2 quiet garrisoned seasons) | **Bounded by construction (ED-743)** |
| **L5** | Substrate spiral | war → MS ↓ → worse bands → harder world | flat −1/battle (**×3 struck**); Mending cumulative recovery; WC accelerators; **hysteresis + leading warnings** (ED-882/PST-1); Post-Calamity recovery path | **Damped + warned** |
| **L6** | Collapse → emergence | neglect → Uncontrolled → Insurgency → invasion | GD-3 is a *deliberate* amplifier (intent-gated); bounded by promotion gates (L ≥ 3, Accord ≥ 4 avg, 2 seasons) | **Intended pressure, gated** |
| **L7** | `intent_of_game` itself | player decisions → mechanics → emergent narrative → more investment | the positive loop the game exists to run; Slate-surplus + Witness budget keep it from saturating the player | **By design** (Lesson-5 doubly-critical: do not damp the design intent, only mechanical excess) |

The one machine-annotated cycle in the contracts (Mandate ↔ settlement L/PS) carries its §1.8 saturating + mean-reverting damper (ED-1008; contracts loop-annotation upgrade pending in LB-5). **All three historical death-spirals (faction passive collapse, Wealth-0 ratchet, Mandate runaway) now carry ratified dampers** — the loop layer is in materially better shape than any pre-June audit recorded.

## §8 — THE UNIFIED OPEN REGISTER (the de-duplicated defect surface, verdict-first)
*The three views each carried a finding register; **the findings overlap heavily**. This is the single de-duplicated set, each row mapped to (a) every view it appears in, (b) the canonical mechanism, (c) the ledger ED, and (d) the **live Jordan decision (J-NN) from `master_workplan_v3 §5`** that closes it. This subsumes wiring Part 4 (F1–F7, C8–C11), flat-spec G (F1–F10), verdict §3/§5, and game_flow §9 (F1–F10) — nothing is now tracked twice under different IDs.*

**Verdict: the architecture is sound and the loop layer is safe; closure is blocked by structural decisions that are Jordan's, not defects to fix. Severity is dominated by missing registrations, missing docs, and one missing direction — not by runaway dynamics.**

| # | Defect | Appears as | Canonical mechanism / fix | Sev | Ledger | Decision |
|---|---|---|---|---|---|---|
| **1** | **Top-down delivery gap** — no rule delivers a provincial/peninsula Key down to a personal/scene/settlement consumer; all 9 `scale_transitions §3` handoffs run upward. The single largest flow hole; blocks Wave-S/4 module specs. | wiring 3-B; flat-spec E2.4 / F1; verdict §4 + A6×19 + §2-J2; game_flow §9-F1; module_map §1 (`!A6` dashed) | extend `scale_transitions §3` with a down-rule **OR** declare engine-mediated delivery A6-exempt (assessor gains scale-agnostic-stream carve-out + tests) | **P2/P3** (contingent) | ED-1006 | **J-1** |
| **2** | **Faction-stat write-path / inversion** — Mandate is derived (LPS-2e) and cannot be written directly; whether faction stats become aggregate(holdings) ⊕ national-event Keys decides every Wave-2 write-path. | wiring F1 (Mandate direct-write); flat-spec F2 / A3.2; verdict A3.2; game_flow §9-F2; consolidation-master Part A | adopt/reject the substrate primitive; until then write-paths parameterized; the Domain Echo must route ΔL/ΔPS to the settlement, not ±Mandate (R4) | **P1** | (gated on ED de-dup backlog) | **J-7** (+ **J-8** echo calibration) |
| **3** | **7 unregistered emitted Key types** — canon-named types the registry never defines ⇒ `validate()` rejects: `scene.thread_operation`, `scene.draft_da`, `mechanical.project_advanced`, `state.project_completed`, `state.project_failed`, `scene.displacement`, + `scene_outcome.battle_concluded` (naming drift). | wiring F2; verdict A2/F2×7; module_map §4.5 `[unreg]`; game_flow (implied) | register (Class-B §10) **or** strike from doc-12 §8; strike `scene.draft_da` (DA keyed `da.*`); resolve `battle_concluded` naming | **P2** | ED-1006/1007/1009 | **J-2** |
| **4** | **Personal combat has no `scene_outcome` subtype** — combat can't emit a typed outcome Key. | wiring F3; verdict `personal_combat` stub; module_map `scene_outcome.battle_concluded [unreg]` | register `scene.combat_resolved` (deferred to combat-engine ratification — that engine itself is RATIFIED, ED-900/904) | **P2** | ED-1009 | **J-2** |
| **5** | **11/27 modules have no home design doc** — registry-derived "shadow" modules; counting them `extracted` overstates graph coverage (honest split: ~14 specified + ~11 shadow + 2 stubs). | verdict §3 W-DOC cluster + §7.1 addendum | author home docs **or** ratify `registry_derived` status (then contracts status-enum field lands) | **P2** | ED-1006/1009 | **J-4** |
| **6** | **Two over-coupling / duplicate-module candidates** — `settlement_economy` vs `settlement_layer §1.3`; `faction_politics` vs `faction_state`. | verdict §3 + §5-N (J3 necessity) | fold-vs-distinct ruling; prevents double-implementation of Wave-2 modules 14/15 | **P2** | ED-1009 | **J-5** |
| **7** | **3-way piety/conviction name collision** + CI-clock vs Influence-stat overload — intuitability hazard. | verdict §3/§5-E; game_flow; hierarchy Tier 4 | naming resolution | **P2** | ED-1006 | **J-2 / J-4** (exec LA-4) |
| **8** | **GD-2 threshold vs Accord range** — Accord is 0–3, so GD-2(a) "Accord ≤ 3 ungarrisoned → mandatory Muster" fires *always*. `[INTENT UNDETERMINED]` — "garrison everything" vs "garrison the restive." Plus settlement-Order(0–5)→province-Accord(0–3) clamp unstated. | flat-spec C2.1 + A2.2; game_flow §9-F3/F4; module_map §4.4 | confirm intent + state the clamp; conversion-relevant for the Wave-1 first port (settlement) | **P2** | (gf) | **J-19** |
| **9** | **Assert/Suppress failure penalty divergence** — `faction_layer §9` *Stability −1* (track) vs `victory §7` *Discipline −15* (derived pool; Discipline = Stability×10) — different in kind and magnitude. | flat-spec B-14 + F10; game_flow §9-F10 | pick one quantity for the CI module | **P3** | (gf) | **J-20** |
| **10** | **Value-taxonomy drift** (formula moved, consumer/manifest didn't): Composure ×3 vs +6 / Cha↔Presence; Stamina/Concentration stale in clock_registry; Combat pool stale in CSR; Intel struck-vs-restored. **Current authority = `derived_stats §14` (June ED-901/902) + ED-787 Intel restored.** | wiring F4–F7; hierarchy Tier 4; flat-spec F7 | mechanical co-file fix (R7): update clock_registry + every consumer in the same commit. Composure name is the one genuine open call (J-12). | **P2/P3** | ED-901/902/787; COMPOSURE-DRIFT-001 | **J-12** (Composure name); rest mechanical (LA-5) |
| **11** | **Pre-pivot residue** (contradicts ratified canon; misleads a port): shared-loss text (clocks.md "MS 0 = all lose") vs "No shared loss"; victory §0 "all 15" vs GD-1 11+/15; ×3 MS multiplier vs flat −1/−2; CI 15 vs 28; "2–3 scenes" vs 3–5; settlement count 35/36/37; three names for the Strain quantity. | wiring C-8/C-11; flat-spec F5/F6/F8/F9; game_flow §9-F5/F6/F7/F8/F9 | **propagation of already-decided canon** (mechanical, LA-11) — *not* new decisions; one Jordan ruling only on the four-name world-track fracture (J-21) | **P3** | (gf) | LA-11 (mechanical) + **J-21** (four-name) |

**Three classes that PASS (the defects that would make a graph *dangerous* are absent — verdict §1/§2):** A7 loop annotation (no undamped+unbounded cycle); A5 derived-write guard (0 violations — aggregates route to substrate); A1 stub-edge ban (both stubs correctly empty); J1 bucket fitness (all 27 modules' buckets canon-consistent, examined-null).

`[NULL: new P1 canonical defects beyond the already-ledgered items 1–2 — examined across the full five-view read set this session (trail in §10 citations); none found. The flow's safety apparatus (L1–L7) is materially better than any pre-June audit recorded.]`
`[OPEN — Jordan: items 1–7 + 8–9 are the live J-1/J-2/J-4/J-5/J-7/J-8/J-12/J-19/J-20 docket. This master assigns no new ED IDs (the ~94-ID-conflict backlog is unresolved — unilateral appends would worsen it). Renumbering/registration is Jordan's call.]`

---

## §9 — NERS VERDICT (consolidated — `verdict_full_graph §5`)
The graph is a **lint-level pass away from R**, but the lint is *necessary, not sufficient* — behavioral compliance stays with `valoria-resolution-diagnostic`.

- **N — Necessary: mostly held.** Orphan emissions are load-bearing (read by articulation / fieldwork under `intent_of_game`, not removal candidates). Two over-coupling candidates open (item 6 → J-5). Watch the inverse: the J-1 down-rule must not over-engineer.
- **R — Robust: FAIL.** 7 unregistered emitted types + 11/27 modules with no home doc + no top-down delivery rule ⇒ wiring is not yet "complete, error-free." Closes when items 1/3/5 close.
- **S — Smooth: PARTIAL.** Bottom-up scale machinery is coherent and safeguarded; top-down Key delivery is undefined; stale indices (`settlement_layer`, `victory`) and a malformed `scene.gossip` yaml are friction.
- **E — Elegant: at risk.** The 3-way name collision (item 7) and registry-shadow sprawl (item 5) are intuitability hazards; the contract apparatus itself is lean (no over-engineering).

---

## §10 — GOING-FORWARD DISCIPLINE & GENERATED-ARTIFACT POINTERS

**The 7 wrapper rules** (wiring Part 5 — each grounded in a canon mechanism, each tied to a contradiction it prevents; run the pre-wiring checklist before adding or changing any system's I/O):
- **R1** Everything consequential is a Key; nothing crosses a scale out-of-band. (prevents item 2 class)
- **R2** Every emitted Key type exists in the registry first. (prevents item 3) — *hook candidate: Level-3 grep, LB-17*
- **R3** Classify every quantity into exactly one bucket before wiring it. (prevents item 10 class)
- **R4** Never write a Derived Value directly; write its source — in particular never increment Mandate, route ΔL/ΔPS to the settlement. (prevents item 2 directly)
- **R5** Fixed-shape arrays indexed by canonical name; derived vectors read-only; `causes[]` populated.
- **R6** Match the resolver archetype to the mechanic category (d+σ for small-pool bare-stat — the ED-874 fix).
- **R7** Change a value → change all consumers + the manifest in the same commit. (prevents item 10) — *hook candidate: Level-4 co-file, LB-16*

**Generated artifacts — REGENERATE, never hand-edit** (consumer-enforced correctness; conflict-resolution #9 — tree/source wins):
- `references/module_contracts.yaml` (v3 schema-2) is the spine → generates `module_map_flat.md` + `module_flowchart.mermaid` + `state_graph.mermaid` via `contract_flowchart.py`. The Key-type I/O matrix (§4.5), the era state machine, and the per-module gate/derivation tables live there.
- The editorial store is `canon/editorial_ledger.jsonl` (JSONL single-source). ED filing for items 1–9 is **Jordan-gated** pending the ID-conflict backlog.
- A v3-basis adjudicator re-run is queued (LB-5) — closes the flat-map "56 vs 58" derived-view drift.

**Implementation flow** (game_flow §10 — the wave order is the dependency order, restated in §6): Wave S spine → Wave 1 deterministic (world simulates) → Wave 2 provincial (factions play) → Wave 3 dice engines (scenes resolve, Echo has inputs) → Wave 4 actors + read-side. The conversion unit is the module contract; the Key substrate makes "the whole campaign" a replayable, property-checkable object. Lane C governing spec: `godot_conversion_strategy_v1.md`.

---

## §11 — SUPERSESSION & PROVENANCE LEDGER

**Synthesized & indexed by this master — NOT superseded (adversarial-review fix R3).** This master is a **new synthesis layer over complementary live sources**, not a replacement that retires them. Each source remains the authoritative *detail* for its axis; the master is the navigable *index/synthesis* across them. (The earlier "consolidated into this master / mark `[SUPERSEDED-BY]`" framing was an over-claim and internally contradictory — it called `flat_spec` both "superseded" and "the live value-table reference." Corrected: none of these is superseded; no `[SUPERSEDED-BY]` markers are written.) This was a *build-one-index-over-N* consolidation, **not** a *collapse-N-to-1* — the artifact count rose by design, because these sources are distinct detail, not redundant copies.
- `2026-06-06-architecture-map/valoria_system_hierarchy_map.md` (`f1b3f4c9`) — authoritative system specs → synthesized in §1–§4
- `2026-06-06-architecture-map/valoria_system_wiring_analysis.md` (`f1b3f4c9`) — structural edges + contradiction register → §4–§5, §7, §8, §10
- `2026-06-11-game-flow/game_flow_analysis_v1.md` (`c005da27`) — temporal flow + loop inventory → §6, §6.1, §7, §8
- `2026-06-11-game-flow/game_flow_flat_spec_v1.md` (`6199d83a`) — **the live value-table reference** (registries A–G) → indexed in §5.3, §6, §8
- `2026-06-10-module-adjudication/verdict_full_graph.md` (`8d8a2081`) — per-module conformance + NERS → §4, §5.1, §8, §9

**Stay live (NOT superseded — they are sources or generators, not folded analyses):**
- `references/module_contracts.yaml` (`c8e982b5`) — the generating spine.
- `module_map_flat.md` + the two `.mermaid` files — generated views (regenerate from contracts).
- The four per-system feeders (faction `df489902`, massbattle `bedbf41d`, combat `6165471a`, settlement `7cf58954`) — per-system depth inputs.
- `2026-06-10-master-workplan-v3/valoria_master_workplan_v3.md` (`ac49cea6`) — the live workplan; this master is its canon-state graph input and keys §8 to its J-1…J-21 docket and §6 cross-lane map.
- All canonical design docs (the `designs/**` bodies cited throughout) — canon, read-only here.

**Method note.** Consolidation per PI `<document_consolidation>`: collate → reconcile → one synthesis index. Every row traces to a source read in full this session; no mechanical value is invented; every substantive conflict is carried OPEN to the live J-NN docket (creative/structural-ontology = Jordan), never silently resolved.

**Adversarial review & confidence calibration (2026-06-11).** A dispassionate self-audit of this master and the companion atlas is recorded in `valoria_interdependency_atlas_v1.md §7` (findings R1–R8, all reconciled). Two calibrations apply here: **(1) source tier** — the primary-canon spine (`key_substrate`, `key_type_registry`, `scale_transitions`, and `derived_stats §14` + `settlement §1.8`, read live this session) is bedrock; everything **contract-/`module_map`-derived** is secondary and inherits the verdict §7 registry-shadow over-claim — and **4 of 6 currently-stale canonical sources** (`module_contracts`, `derived_stats`, `settlement_layer`, `key_substrate`) are dependencies, so live reads (not stale pins) are the authority. **(2) The loop-safety verdict (§7) and NERS verdict (§9) are INHERITED** from the source audits (game_flow §8, verdict A7), **not re-derived this session** — the sims are cited, not re-run. `[SELF-AUTHORED — bias risk]` throughout — §8 is the register an independent reviewer should re-test against the editorial ledger, which is not swept here.

---
*Citations (full session `[READ:]` trail in the session log): the five consolidated views above (read in full this session at the pinned SHAs) + `canon/02_canon_constraints.md` (P-01–P-15, GD-1/2/3) + `skills/valoria-mechanic-audit/SKILL.md` (task-gate) + `references/canonical_sources.yaml` + `references/module_contracts.yaml`. Underlying canonical mechanics are cited inline by doc + section as carried from the source views.*

