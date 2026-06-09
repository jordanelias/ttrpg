<!--
§8 ALIGNMENT (master_workplan §8, 2026-06-06) — read before the framing below:
- The core engine is attribute-AGNOSTIC: it resolves a pool/inputs to a degree;
  pool-assembly (which descriptors feed it) is a wrapper/archetype concern.
- No single universal resolver. The engine's PROBABILISTIC kernel has three regimes:
  discrete-pool, continuous-Normal, and d+sigma-leverage (archetypes A and B below).
  Archetypes C/D/E (deterministic accounting, clock advance, armature dot-product) are
  non-probabilistic resolution mechanisms. The 5-archetype taxonomy here is consistent
  with §8 and remains operative.
- Attributes / 13 Convictions / 4 ethical axes + matrix / Self-Other / etc. -> the
  Descriptor Registry (W1.13; workplan §8.1/§8.2).
Supporting analysis; the master_workplan is the live capstone.
-->

# Valoria — System Wiring Analysis (companion to the Hierarchy Map)
**Key-readiness · Domain-Echo keying · interdependencies · contradiction register · governance framework**
Compiled 2026-06-06. Grounded in canon read this session (Key substrate §1–§8, scale_transitions §3/§5, settlement §1.8, derived_stats §1/§3/§14, conviction taxonomy+matrix, stats_1_7, clock_registry, threadwork §8, 02_canon_constraints P-01–P-15 + GD-1/2/3). `[SELF-AUTHORED — bias risk: this extends my own map; an independent reviewer should re-test the contradiction register against the editorial ledger, which I did not sweep.]`

---

## PART 1 — IS EACH SYSTEM READY TO ACCEPT A KEY?

**Definition.** A system "accepts a key" when (a) it has a `TYPE_SUBSCRIPTIONS[type]` entry + a `consume(key)` callback (consume side) and/or emits a **registered** Key type (emit side), per the single update rule (`key_substrate §4.1`), and (b) the Key types it touches **exist in the registry** (else `validate()` rejects them — invariant §2.3 #2). Two readiness layers: **SPEC** (§8 contract + registry) and **IMPL** (Godot Resources, §8.8 — Phase 5a, *pending across the board*).

**Migration frame (`§7.1`):** Phase A (substrate authored) ✓ done. Phase B (per-system migration) authored in 5 stages; Phase C (Stage-10 verification sims) and §8.8 Godot impl are **not** confirmed complete. So everything below is **spec-ready at best, not implementation-ready.**

| # | System | Emits (per §8) | Consumes / subscribes | Spec readiness |
|---|---|---|---|---|
| 3.1 | **Combat (personal)** | scene.* events; outcome subtype **undefined** | Wounds feed pools internally | ⚠ **PARTIAL** — no `scene.combat_resolved` in registry (F3) |
| 3.2 | **Social Contest** | `scene.dialogue` (+persuasion payload); `scene.contest_resolved` | adjudicator/Piety state | ✅ READY (emit) |
| 3.3 | **Threadwork** | declares `scene.thread_operation` — **not in registry** (F2); registry has `meta.thread_woven` | — | ⚠ **BLOCKED** — emit type unregistered → validate() rejects |
| 3.4 | **Investigation/Fieldwork** | `scene.investigation_resolved`; `meta.knot_*` | Memory queries (Bonds≥5) | ✅ READY (emit) |
| 3.5 | **Knots** | `meta.knot_formed` / `meta.knot_ruptured` | Memory query for prerequisites | ✅ READY (emit+query) |
| 3.6 | **Faction Layer** | `da_outcome.*`; state-change Keys | `da_outcome.*`, `state.succession`, `state.scar_acquired`, `env.peninsular_strain_shock` | ✅ **READY (bidirectional)** — most fully keyed |
| 3.7 | **Settlement/Territory** | state-change Keys on L/PS threshold cross | (rides faction state) | ⚠ EMIT-on-threshold; no explicit consume contract |
| 3.8 | **Military Layer** | — | — | ▢ **NOT SEPARATELY KEYED** — rides faction `da_outcome` (Muster) |
| 3.9 | **Mass Combat** | `scene_outcome.battle_concluded`; phase `scene.*` | thread-phase Keys | ✅ READY (emit) |
| 3.10 | **CI Political** | — | thread/scene Keys (Epistemic CI trigger, PP-182) | ⚠ CONSUME (trigger) + clock-advance |
| 3.11 | **Victory** | — | reads aggregated state at Accounting | ▢ **STATE-READER** — not Key-wired (deterministic check) |
| 3.12 | **Peninsular Strain** | `env.peninsular_strain_shock` / `env.crisis` / `env.disaster` | — | ✅ READY (emit env.*) |
| 3.13 | **Scale Transitions / Domain Echo** | produces the queued downstream faction Key | consumes `scene_outcome.*` | ◐ **PROPAGATION RULE** (see Part 2) |
| 3.14 | **Articulation Layer** | `state.belief_revised`, `meta.*` | **full Key stream** (the universal reader) | ✅ READY (consume/reader) |
| 3.15 | **Campaign Architecture** | `mechanical.season_change` / `accounting` / `cascade_resolution` | all (Accounting is where echoes land) | ✅ READY (emit — the clock spine) |
| 3.16 | **NPC Behavior** | `scene.*` (actions) | **full Key stream via armature** — NPCs *are* the observers in §4.1 | ✅ **READY (bidirectional)** |
| 3.17 | Clock Registry | — | — | n/a (manifest, not a system) |
| — | **DA submission** | declares `scene.draft_da` — **not in registry** (F2) | — | ⚠ **BLOCKED** |
| — | **scene_slate** | declares `mechanical.scene_activated` — **not in registry** (F2; registry has `scene_entered`) | — | ⚠ **BLOCKED** |

**Verdict.** The keying architecture is **spec-complete and bidirectionally wired for the faction/NPC core** (3.6, 3.14, 3.15, 3.16 are the live hubs), **emit-ready for most scene systems**, and **not yet implemented** anywhere (Godot §8.8 pending). Three systems are **blocked at the emit step by unregistered Key types** (Threadwork, DA submission, scene_slate — F2) and **personal combat has no outcome Key type** (F3). Conviction taxonomy/matrix is the **substrate basis**, not a keyed actor. Military, Victory ride other systems and need no direct keying by design.

---

## PART 2 — HOW A SCENE OUTPUT BECOMES A STRATEGIC INPUT (Domain Echo / scale interaction)

Trace of one scene resolving and its result re-entering as input to the faction layer. Sources: `key_substrate §4.1`, `scale_transitions §3.4/§5`, `settlement §1.8`, `campaign_architecture`.

1. **Resolve.** A personal/scene system runs its resolver and yields a **degree** (Overwhelming / Success / Partial / Failure) — e.g. a social contest's Piety-Track outcome, a duel, a public sermon.
2. **Emit the outcome Key.** The scene emits a `scene_outcome.*` Key (`scene.contest_resolved` / `scene.battle_concluded` / `scene.investigation_resolved`) carrying `stat_deltas`, `scale_signature` (e.g. `[personal, territory]`), `symbolic_dimensions` (4-axis), `visibility`, and the degree in `payload`.
3. **Single update rule fires (`§4.1`).** `validate → KEY_LOG.append → compute_observers` (source actor + targets + all faction-aware actors if the scale is peninsula) → each observer's **armature interprets** it (`Σ armature·symbolic·impact`) → `memory.record(salience)` → `apply_state_changes` → `TYPE_SUBSCRIPTIONS[type].consume()` routes it to subscribing systems → `CAUSAL_GRAPH.add_edge` → awareness bump on its causes.
4. **Domain Echo qualifies it (`scale_transitions §5.1, §3.4`).** If the scene meets **Sufficient Scope** (§7), it earns **one Domain Echo per faction** (PP-329, no compounding). The degree maps to a magnitude: **OW ±2 / Success ±1 / Partial → narrative-only / Failure → −1 to the acting faction**, capped ±2.
5. **The echo is queued, not applied live (`§5.3`).** In videogame/BG mode the echo is **queued to the next seasonal Accounting** (the `campaign_architecture` loop) — deliberately, to stop real-time manipulation of strategic stats from personal scenes. (The §5.3 "fires immediately" branch is the TTRPG Register-Shift case — see C-11 in Part 4 for the videogame-mode ambiguity.)
6. **At Accounting, the output becomes an input.** The queued echo is realized as a **new strategic-scale Key** (`da_outcome.*` or `mechanical.accounting`) whose **`causes[] = [scene_outcome_key.id]`**. *This is the literal "output keyed as input":* the scene Key's id is now a provenance entry in the downstream Key's `causes[]` array, and the causal graph holds the edge `scene → faction`. The faction state machine's `consume()` (`§8.1`) reads the `da_outcome.*` and updates Mission scoring / Cascade.
7. **Routing to the right substrate level (the current-canon correction).** Where the echo targets a **base** faction stat (Stability, Influence, Wealth, Military, Intel), the ±delta applies directly. Where it targets **Mandate** — which is now a **derived size-weighted aggregate** (`settlement §1.8`) and *cannot be written directly* — the delta must instead apply **ΔL/ΔPS to the scene's settlement** (settlement §1.8: "faction-level mission outcomes apply ΔL/ΔPS to controlled settlements, re-aggregate into Mandate"), which then re-aggregates upward. **The Accord echo (`§5.5`) already does this correctly** (AUD-SET-02: targets the settlement; province Accord recomputes `floor(mean settlement Order)` at Accounting). **The Mandate/Debate/Thread echoes (`§5.2/§5.4/§5.6`) do not — they still write `±Mandate` directly. That is contradiction F1.**

**Three echo channels can co-fire from one scene** on different stats (`§5.6`): standard Domain Echo (§5.2), Accord Echo (§5.5), Thread Echo (§5.6) — plus the independent Epistemic CI trigger (PP-182). Each obeys the one-per-scene-per-faction cap on its own stat.

---

## PART 3 — INTERDEPENDENCY TRACE

Four edge classes. Sources: `scale_transitions §3` (Eight Handoff Rules), `key_substrate §4.1/§8`, `settlement §1.8`, `derived_stats`, `threadwork §8.1`.

### 3-A. Substrate edges (universal)
Every system ↔ the **Key log** via the single update rule. **NPCs are the observers** (§4.1 step 4) — so NPC Behavior consumes the entire stream through armatures. **Articulation Layer** is the universal *reader* (Concern/cut-scene/chronicle). **Campaign Architecture's Accounting** is the universal *sink* where queued cross-scale effects land. The **causal graph** (`causes[]`) is the provenance backbone linking all of it.

### 3-B. Vertical / scale edges (`scale_transitions §3`, the Eight Handoff Rules)
`Personal→Thread` · `Personal→Faction (Domain Echo)` · `Personal→Scene (Contest)` · `Scene→Faction (Domain Echo)` · `Thread→Faction` · `Thread→Mass (battle integration)` · `Mass→Personal (general duel)` · `Scene→Mass` · `Fieldwork↔All`. These are the scale-transition seams; Domain Echo (Part 2) is the Scene→Faction one.

### 3-C. Resource / stat coupling edges
- **Wounds → all personal pools** (each wound −1D). Combat is the local hub.
- **Settlement L/PS → Mandate** (size-weighted saturating aggregate, K=6) **→ Parliament votes (`faction_layer §5.3`) → Victory**. Reverse: **Mandate → settlement L/PS** (mean-reverting ±1/season feedback).
- **CI clock → Seizure** (`M = Influence + ⌊CI/15⌋ vs Ob 7−PT`; Fail → Mandate −1) **→ settlement control**; **CI → Parliament weight** (+⌊CI/20⌋); **thread events → CI** (Epistemic CI trigger).
- **Threadwork → MS clock → Peninsular Strain → Accord / Turmoil → faction public-temperament**; **MS → Thread Revelation Curve**. Threadwork → **Coherence** (personal, depleting) → fallout tables.
- **Mass Combat outcome →** MS −1 (Campaign −2), IP +2/season, Political Stability +1/season, Accord 1 on conquest.
- **Social Contest → Piety Track → Debate Domain Echo → ±Mandate** (→ via settlement, per F1).
- **Knots ↔ Disposition ↔ Coherence** (rupture → Disp −4; loss → Coherence −1; anchoring → +1 Coherence recovery). **Bonds →** Disposition cap, Knot pool, Knot count.
- **Self-Other scalar → outcome attribution → PS contribution** (`attributed = raw × (1 − 0.5·max(0,orient))`).

### 3-D. Key feedback loops (with damper/bound status, per `valoria-resolution-diagnostic` Lessons)
| Loop | Damped? | Bounded? | Status |
|---|---|---|---|
| Settlement L/PS ⇄ Mandate | ✅ saturating `T/(T+K)` + mean-reverting | ✅ clamp 0–7 | **SAFE** (Lesson-5 bound present) |
| Faction collapse → territory loss → muster (Military) → Mass Combat → Stability | ◐ slow Stability recovery | ✗ terminal state (Stability 0 = collapse, no bound short of extinction) | **WATCH** — diagnostic-flagged undamped-terminal |
| Threadwork → MS decay → (more strain) ; recovery via Mending | ◐ Mending repairs | ✅ MS 0–100 | bounded; MS-0 = Rupture loss |
| `intent_of_game` (decisions ⇄ emergent narrative) | — | — | **intentional positive loop** (Lesson-5 doubly-critical; do not damp the design intent, only its mechanical excesses) |

### 3-E. Internal consolidation (`threadwork §8.1`)
Coherence subsumed **Intelligibility / ThS-CD / Taint**; **MS replaced Thread Tension**; Mending replaced FR-Dissolution gap-closure. "Systems unchanged": core engine, combat engine, social, faction accounting, mass combat, axes (§8.2). This matters for I/O hygiene — those legacy tracks must not reappear as inputs anywhere.

---

## PART 4 — CONTRADICTION REGISTER (verdict-first, severity-ranked)

**Verdict: the architecture is sound, but there are 3 P1 I/O-breaking conflicts and 7 lower-severity drifts — all concentrated at the seams where a recent restructure (combat-engine June pass; LPS-2e settlement-grain) outran the docs that consume it.** None is a metaphysical/structural conflict; all are mechanical/value drift, in scope for evidence-grounded correction (`<identity>` factual tier) and/or Jordan-ratified mechanical fixes.

| ID | Severity | Conflict (input/output) | Sources in conflict |
|---|---|---|---|
| **F1** | **P1** | **Domain Echo writes `±Mandate` directly, but Mandate is a derived aggregate** — a derived value has no direct write path. Correct target = settlement ΔL/ΔPS → re-aggregate. | `scale_transitions §5.2/§5.4/§5.6` (2026-04-13) vs `settlement §1.8` / `derived_stats §14` (2026-05-30) |
| **F2** | **P1** | **Three declared emit types are not in the Key Type Registry → `validate()` rejects them** (invariant §2.3 #2): `scene.thread_operation` (Threadwork), `scene.draft_da` (DA submission), `mechanical.scene_activated` (scene_slate; registry has `scene_entered`). | `key_substrate §8.4/§8.5/§8.6` vs `key_type_registry §2–§8` |
| **F3** | **P1/P2** | **Personal combat has no `scene_outcome` Key subtype** — registry covers contest/battle/investigation resolved, not combat. Combat can't emit a typed outcome. | `key_type_registry §7` vs combat being a scene-scale system (`§8.5` omits it) |
| **F4** | **P2** | **Composure formula divergence** — Charisma×3 vs Presence+6 vs Charisma+6 (name *and* form). Resolver input ambiguous. (Tracked: COMPOSURE-DRIFT-001.) | `derived_stats §14` vs `clock_registry` / `params/contest` / `complete_systems_reference` |
| **F5** | **P2** | **Stamina/Concentration stale** — clock_registry shows `End+1` / `Focus+Recall`; current is `(3·End)+(2·Spi)` / `(3·Foc)+(2·Spi)` (June ED-901/902). | `clock_registry` (2026-04-26) vs `derived_stats §14` (2026-06-04) |
| **F6** | **P2** | **Combat pool stale** — `(Agi×2)+H+3`, crit ≥3 vs current `max(5,H+6)`, crit ≥4 (Agility-independent). | `complete_systems_reference` (Rev-2) vs `derived_stats §14` / `combat_engine_v1` |
| **F7** | **P2** | **Intel stat STRUCK-vs-restored** — registry/board-game flag Intel STRUCK (ED-748/796), but ED-787 restored it as the 6th faction stat with live Spy-Ob formula. | `clock_registry` / board-game vs `stats_1_7` ED-787 + `derived_stats §14` |
| **C-8** | P3 | **"territory" vs "settlement" grain** persists across docs (T1–T17 province-tier vs base settlement); reconciled in §1.8 but dual usage lingers. | `geography_v30` vs `settlement §1.8` |
| **C-9** | P3 | **Index drift** — `params/combat.md` manifest path → missing file (deprecated); 2 audit docs registered to no concept. | bootstrap index report |
| **C-10** | P3 | **Knots contradictions_pending** — TIER-DRIFT-001, TRUNC-DRIFT-001 carried open. | `canonical_sources` knots_unified |
| **C-11** | P2/P3 | **Mode-applicability ambiguity** — `scale_transitions` is TTRPG/BG/Hybrid-framed; project is videogame-only. Echo timing (§5.3 "immediate" vs "queued") needs the single videogame mapping. | `scale_transitions §5.3` vs `<identity>` videogame-only |

`[NULL: searched the I/O seams across all 17 systems + the substrate; the above is the complete set I can ground — no further input/output conflict found in the docs read. Not a ledger sweep: the ~94-ID-conflict editorial backlog and any contradictions living only in unread design bodies are out of scope here.]`
`[OPEN — Jordan: F1/F2/F3 are P1 and warrant `editorial_ledger.jsonl` entries; ID assignment is blocked on the ~94-conflict backlog. Did not commit — no instruction to, and clean-ID pull needs your adjudication.]`

---

## PART 5 — FRAMEWORK: RESPECTING WRAPPERS, CONTAINERS & NESTED ARRAYS GOING FORWARD

Seven rules, each grounded in an existing canon mechanism, each tied to a contradiction it prevents. This is the discipline; where a hook can enforce it, that is noted as a candidate.

**R1 — Everything consequential is a Key; nothing crosses a scale out-of-band.** (`§1`.) No system keeps a private event channel. Any output that persists or crosses a scale is emitted as a Key and obeys the single update rule (`§4.1`). *Prevents:* ad-hoc cross-scale writes (the class F1 lives in).

**R2 — Every emitted Key type exists in the registry first.** (`§2.3 #2`, `key_type_registry §10` extension process.) A system may not emit a type the registry doesn't list; adding a type is a Class-B extension through the registry, not an inline string. A system's `§8` integration contract and the registry **must agree** — divergence is a defect (registry wins). *Prevents:* F2. *Hook candidate:* a pre-commit grep that cross-checks emit-type string literals in design docs against `key_type_registry` entries (Level 3).

**R3 — Classify every quantity into exactly one of the four buckets before wiring it.** (`derived_stats §14`.) Pool (computed at action time, never stored) · Derived Value (`Stat × multiplier`) · Track (bounded oscillating counter) · Clock (monotonic progress). The classification dictates the legal operations (R4). *Prevents:* category-confusion drift (C-10 class).

**R4 — Never write a Derived Value directly; write its source.** (`derived_stats §1`, `settlement §1.8`.) A Derived Value is the read-only output of its formula. To change it, change the underlying Stat or apply the defined drain/refill. **In particular, never increment a derived *aggregate* (Mandate) — route the delta to its substrate (settlement L/PS) and let it re-aggregate.** Pools are recomputed, never persisted. *Prevents:* **F1 directly.**

**R5 — Fixed-shape arrays are indexed by canonical name; derived vectors are read-only; provenance arrays are populated.** (`§2.3 #6`, `§2.5`, `§2.1`.) The 4 axes (`hierarchical/sacred/instrumental/traditional`) and the 13 Convictions are fixed-shape — index by name, never by position-guess; a 5th axis is a registry-gated Class-B extension, never an ad-hoc field. `armature_position` is **derived** (`convictions × matrix`) — never authored directly. `causes[]` is **append-only and must be populated** (sparse causes = shallow narrative, §2.1). *Prevents:* silent axis/vector drift; thin causal graphs.

**R6 — Match the resolver archetype to the mechanic category.** (`valoria-resolution-diagnostic`.) Dice pools only on healthy pools for graded/recoverable outcomes; **d+σ for small-pool bare-stat checks** (the ED-874 fix); deterministic accounting for ledgers; clock-advance for accumulators; armature dot-product for Key interpretation. Don't roll a small bare stat on a pivotal irreversible outcome. *Prevents:* small-pool fragility (the defect d+σ already closed).

**R7 — Drift discipline: change a value, change all its consumers and its manifest in the same commit.** (architecture `<enforcement_spectrum>` co-file rule.) The **clock_registry** is the container manifest, **derived_stats §14** the value-taxonomy authority, **settlement §1.8** the Mandate-aggregation authority — a quantity is defined once, in its home, and every consumer + the manifest updates together. A stale manifest entry is a defect. *Prevents:* **F4/F5/F6/F7** (all are "formula moved, consumer/manifest didn't"). *Hook candidate:* extend the co-file check so a commit touching a derived-value formula must also touch `clock_registry`.

### Pre-wiring checklist (operational; run before adding or changing any system's I/O)
1. **Bucket:** what bucket is each new/changed quantity (Pool / Derived / Track / Clock)? (R3)
2. **Registry:** is every Key type this system emits already in `key_type_registry`? (R2)
3. **Derived-write:** does any output write a Derived Value or aggregate directly? If yes → reroute to its source. (R4)
4. **Keying:** is every cross-scale output emitted as a Key with `causes[]` populated and the causal edge recorded? (R1, R5)
5. **Resolver:** does the resolver archetype match the mechanic category? Any bare small-stat roll on a pivotal outcome? (R6)
6. **Co-file:** are all consumers + the relevant manifest (`clock_registry` / `derived_stats §14` / `settlement §1.8`) updated in the same change? (R7)
7. **Layer gate:** does the change touch metaphysics / world / characters / tone? If yes → **stop, ask Jordan** (`<identity>` creative-tier bar). Mechanical gap-fills: log `[ASSUMPTION:]` with bottom-up source + top-down anchor, Jordan-vetoable.

**Constraint floor (always-on, independent of the above):** P-01–P-15 (immutable Foundations — esp. P-01 inseparability, P-10 Coherence semantics, P-14 co-movement in all modes) and GD-1/2/3 (mutable but Jordan-ratified — single victory path, deterministic-before-stochastic AI, Revolt→Insurgency pipeline). Any I/O that violates these requires revision, not accommodation.
