# VALORIA — All-Directions Interdependency Atlas (granular, primitive-grounded)
**Date: 2026-06-11 · Status: PROPOSED (Jordan-vetoable) · Companion to & granular extension of `valoria_interdependency_master_v1.md` §5**

`[SELF-AUTHORED — bias risk: extends my own master. The §5 findings here should be re-tested by an independent reviewer against the editorial ledger, not swept. This atlas asserts no canonical content Jordan has not authored; the top-down gap is enumerated, never filled.]`

**What this is.** The master's §5 is the all-directions graph at *pointer* level. This atlas builds it out **bottom-up from the canonical primitives** — `key_substrate_v30` (the single-update rule + observer resolution + per-system integration contracts), `key_type_registry_v30` (the 37 registered types with per-type emitter/consumer), and `scale_transitions_v30` + `params/scale_transitions` (the eight handoffs + zoom + Domain Echo) — all read in full this session at their pinned canonical SHAs. Every edge cites its primitive. The six canonical directions (`canon/definitions.yaml`: top-down · bottom-up · vertical · diagonal · lateral · horizontal) are each enumerated edge-by-edge. Where canon has no rule (the top-down Key-delivery gap, docket **J-1** — note `ED-1006` is a *different* finding, the module-contract extraction; see §7-bis P2), the gap is enumerated granularly and carried OPEN — not invented.

**Source SHAs (this session):** `scale_transitions_v30.md`@`17e75c6e` · `key_type_registry_v30.md`@`19a69b89` · `key_substrate_v30.md`@`3a4259e7` · `params/scale_transitions.md`@`99522462`. Cross-referenced against `module_map_flat.md §4.5` (generated from `module_contracts.yaml`).

---

## §0 — METHOD & THE NAME-RECONCILIATION MAP (read first — load-bearing)

**Method.** For each direction: enumerate every cross-system edge as `[source] --(Key type / coupling, citation)--> [target]`, with mechanism, cap/gate, and direction tag. Bottom-up means the rows derive from the registry's per-type `emitting_systems`/`consuming_systems` and the substrate's §8 integration contracts, **not** from the audit summaries.

**The naming map (the bottom-up read's first finding).** The **registry and substrate use canonical *system* names; the contracts/modules use *implementation* names.** They are the same nodes under two vocabularies — and the divergence is exactly the 3-way name-collision finding (master item 7), now confirmed at the primitive, not just the adjudicator. Reconcile before reading any edge table:

| Registry / substrate name (canon) | Contract / module name (impl) | Note |
|---|---|---|
| `da_framework` | `domain_actions` | the DA emitter |
| `faction_layer` | `faction_state` (+ `faction_politics` for succession/coup/standing subset) | the strategic accumulator |
| `conviction_track` | `piety_track` | the personal Conviction-Scar module — **the collision**: distinct from `territorial_piety` (per-territory CV/Piety + CI clock) and `ci_political` (CI clock reader). Three "piety/CI" nodes; the registry↔contract name swap compounds it. |
| `articulation` | `articulation_layer` | the universal reader (consumes the full stream via the engine wildcard, so it is rarely listed per-type in contracts) |
| `settlement_layer` / `settlement_economy` | (same) | — |

Edge rows below use the **registry/canon name** and give the impl name once where it first matters.

---

## §1 — THE UNIVERSAL EDGE MECHANISM (every edge is a Key)
*Source: `key_substrate §4.1` (single-update rule), `§4.2` (observer resolution), `§2.3` (validation invariants).*

Every edge in this atlas is a Key traversing the **single update rule** (`§4.1`), the *only* state-mutation path:
`validate(key) → KEY_LOG.append → observers = compute_observers(key) → for each observer: armature.interpret → memory.record(salience) → apply_state_changes(interpretation, stat_deltas) → for each subscribing_system in TYPE_SUBSCRIPTIONS[type]: system.consume(key) → for each cause in causes[]: CAUSAL_GRAPH.add_edge + awareness bump`.

**Observer resolution (`§4.2`) defines the lateral/witness fan-out of every edge — and is scale-agnostic, which is the crux of the top-down question (§2.4):**
```
compute_observers(key):
  observers = {source_actor} ∪ {t.actor_id for t in targets}
  if visibility.public: observers ∪= actors_in_scale(scale_signature)
  observers ∪= semi_public_observers ∪ private_observers
```
`actors_in_scale(scales)` returns **all actors whose state intersects those scales — for a peninsula-scale Key, every faction-aware actor; for personal, the scene members**. There is **no scale predicate gating delivery**: any observer may read any appended Key whose scale its state intersects. Validation invariants (`§2.3`): type registered (#2 — the F2 wall), `causes[]` acyclic DAG (#4), `scale_signature` non-empty (#7), exactly-one visibility mode (#8). A Key failing any is rejected (`ValueError`) and never enters the log.

**Edge legality is therefore two-gated:** (a) the type is in the registry (else `validate` rejects — the 7 F2 types fail here), and (b) an observer's scale intersects the Key's `scale_signature` (else no delivery). Caps/dampers are per-edge below.

---

## §2 — THE EDGE ATLAS BY CANONICAL DIRECTION

### §2.1 — LATERAL / HORIZONTAL (same-scale edges)
*Scene-internal and provincial-internal. Source: registry per-type emitter/consumer; `scale_transitions §3.9` (lateral fieldwork); module_map §1.*

| Source | Key / mechanism | Target | Scale | Citation |
|---|---|---|---|---|
| `scene_slate`, `social_contest` | `scene.dialogue` / `scene.insult` / `scene.threat` | `npc_behavior`, `conviction_track`(piety_track), `faction_layer`(faction_state), `articulation` | personal | registry §2 |
| `scene_slate`, `fieldwork` | `scene.gift` | `npc_behavior`, `faction_layer`, `articulation` | personal | registry §2 (scene.gift) |
| `scene_slate`, `npc_behavior` | `scene.witness` | `conviction_track`, `npc_behavior`, `articulation` | personal | registry §2 (scene.witness) |
| `npc_behavior` | `state.opinion_revised` (Procedure D) | `social_contest`, `npc_memory`, `articulation` | personal | registry §5 (opinion_revised) |
| `da_framework`(domain_actions) | `da.*` (the 5 DA subtypes) | `faction_layer`(faction_state) | provincial | registry §3 |
| `faction_layer` | `mechanical.cascade_resolution` / `mechanical.mission_shift` | `faction_layer`, `npc_behavior` | provincial | registry §4 |
| `faction_politics` | `state.coup_attempted` / `state.succession` / `state.standing_change` | `faction_layer`, `npc_behavior` | provincial | registry §5 |
| Combat scene → `fieldwork` | post-combat site investigation (Exposure +1/+2/+3) = 1 new fieldwork scene | `fieldwork` | personal/scene | `scale_transitions §3.9` (F-TRANS-09) |
| Contest → `fieldwork` | Appraise success → +1 Evidence (Testimonial); winner +1 / loser −1 Disposition | `fieldwork` | personal/scene | `scale_transitions §3.9` (F-TRANS-10/05) |

### §2.2 — BOTTOM-UP (substrate → aggregate recompute; **covered & safeguarded**)
*The deliberately narrow, capped, queued personal→strategic channel. Source: `scale_transitions §5` (Domain Echo) + `§7` (Sufficient Scope gate); `settlement §1.8` (aggregate recompute); registry.*

**The gate (`§7` Sufficient Scope — a scene Echoes only if ≥1 holds):** named faction leader/representative · direct challenge to institutional authority · completed Complex/Structural investigation of institutional acts · Thread op at Relational+ scale · combat victory over a faction officer · Disposition +4/+5 with a faction officer · settlement governance moving Order ±1. (+1 to net successes if a companion is present.) **Multi-condition tie-break (`§3.4`):** Thread op → combat victory → settlement governance → Disposition → investigation → faction-leader-direct → other.

| Channel | Source degree → effect | Target | Cap / timing | Citation |
|---|---|---|---|---|
| **Standard Domain Echo** | OW ±2 / Success ±1 / Partial narrative-only / Failure −1 own faction | most-relevant faction stat | **±2/stat; 1 Echo/scene/faction (PP-329); queued to next Accounting** (§5.3/PP-109 — prevents real-time BG manipulation) | `scale_transitions §5.1–5.3` |
| **Debate → Echo** | Piety Track ≥7 → winner +1 Mandate (loser −1 if held authority); 4–6 → none; ≤3 → reversed | faction Mandate | queued; **routes via settlement ΔL/ΔPS, not ±Mandate directly (R4 — item 2/F1)** | `scale_transitions §5.4` |
| **Accord Echo** | public governance OW/Success → Accord +1; destabilize → −1; territorial transfer → set 2; violence → −1 + MS −1 immediate | the **settlement** where the scene occurred (province Accord recomputes ⌊mean Order⌋, AUD-SET-02) | **±1/territory/Zoom-In; queued to Accounting 4c; does not stack with same-season Govern (higher wins)** | `scale_transitions §5.5` |
| **Thread Echo** | Dissolution → Stability −1; Mending(Territorial+) → Mandate +1; Gap → Stability −1; Lock(unauth) → Mandate −1; public Thread op Church-terr → Church Mandate −1; Varfell(VTM≥3) → +1 | controlling faction stat | fires on RS-change ≥1 / Scar-firing witness / Territorial+ Gap-Lock-Knot; **1/scene/faction; queued**; extends Epistemic CI trigger to all factions | `scale_transitions §5.6` (ED-673) |
| **Accounting recompute** | settlement L/PS/W → `Mandate = clamp(round(7T/(T+6)),0,7)`; settlement Order → province Accord = ⌊mean Order⌋ | faction Mandate / province Accord (derived) | saturating + clamped (L3 damper); **A5 guards the illegal inverse — no direct aggregate write** | `settlement §1.8`; module_map §4.4 |

### §2.3 — VERTICAL (cross-scale edges; **half-covered** — up yes, down is the gap)
*The Eight Handoff Rules + the cross-scale fieldwork edges + PC embedding + Thread timing. Source: `scale_transitions §3 / §3.9 / §9 / §10`; `params/scale_transitions`. Direction tag: ↑ up · ↓ down · ↔ lateral-cross.*

| # | Edge | Scale pair | Dir | Rule | Citation |
|---|---|---|---|---|---|
| §3.1 | Personal → Thread | personal → thread | ↑ | Leap triggers; Contact opens; Thread pool/ops available | `§3.1` |
| §3.2 | Personal → Faction | personal → provincial | ↑ | personal Ob resolves first, then DA Ob — **same roll**, consequence via Domain Echo (§5) | `§3.2` |
| §3.3 | Personal → Scene (Contest) | personal → scene | ↔ | personal roll = opening move / Appeal in a social scene | `§3.3` |
| §3.4 | Scene → Faction | scene → provincial | ↑ | Sufficient Scope → Domain Echo; tie-break priority; 1/faction/scene | `§3.4` |
| §3.5 | Thread → Faction | thread → provincial | ↑ | Thread op targeting faction config resolves *as* a Domain Action — no extra roll | `§3.5` |
| §3.6 | Thread → Mass | thread → scene(battle) | ↔ | substrate cost by scale (Skirmish TS≥30/0 · Battle TS≥50/−1 · War TS≥70/−2); recorded Phase 4/6, applied Phase 6 Step 1 | `§3.6` |
| §3.7 | **Mass → Personal** (general duel) | territory(battle) → personal | **↓** | Personal Action at Phase 5 (Pri 8); 1 exchange/turn; CR suspended; max 5 exchanges. **The one explicit down-edge in §3 — and it is a narrow duel mechanic, not Key-delivery.** | `§3.7` (PP-111/232) |
| §3.8 | Scene → Mass | scene → scene(battle) | ↔ | social win +1D Command / investigation +1D first Volley / combat win free Reform; 1 turn | `§3.8` (PP-261) |
| §3.9 | Fieldwork ↔ All | personal ↔ all | ↑↔↓ | full bidirectional matrix (Combat/Contest/Thread/Mass + BG-Survey→TTRPG-Discovery offset ±2) | `§3.9` (F-TRANS-*) |
| §9 | PC embedding | personal → provincial | ↑ | PC physically present → faction +1D on one DA in that territory/season | `§9` (ED-075) |
| §10 | Thread → CI (Hybrid timing) | thread → peninsula | ↑ | Dissolution → CI +1; POP → CI −1 (1-season paradox window); Lock/Weave/Mend → none | `§10` (PP-125/260) |

**Vertical coverage:** every cross-scale edge in §3 runs **up or lateral-cross**, except §3.7's narrow general-duel down-edge. There is **no general strategic→personal vertical handoff** — see §2.4.

### §2.4 — TOP-DOWN (aggregate → substrate; **OPEN — J-1**, the single largest hole)
*Source: `scale_transitions §4` (zoom), `§3.7` (the one §3 down-edge); `key_substrate §4.2` (the scale-agnostic delivery mechanism). Direction: strategic/peninsula → personal/scene/settlement.*

**The down-channels that DO exist (enumerated granularly):**

| Channel | Mechanism | What it carries | Citation |
|---|---|---|---|
| **C1 · Mass → Personal duel** | Personal Action at battle Phase 5, 1 exchange/turn, max 5 | a *combat opportunity* — not arbitrary strategic state | `§3.7` |
| **C2 · Mandatory Zoom-In forcing-functions** | strategic condition → undeclinable Priority-0 scene (1 SA each; overflow → Witness) | Settlement Revolt (Order 0) · Heresy Investigation target · Faction-Leader Removal · Mass Battle at settlement · Companion Arc · Knot-Partner Crisis (Scar ≥3) · Stability Crisis (Stab ≤2, ED-749 hysteresis) · Rank Recognition | `§4.3.2` |
| **C3 · World-State Zoom-In (optional)** | strategic trigger → Priority-1 offered scene | Clock Band Transition (MS/CI/IP) · NPC Conviction Crisis · Treaty Proposed/Broken · Territory Control Change (adjacent) · Warden Emergency (RS≤40) | `§4.3.3` |
| **C4 · Retrospective "Where Were You?"** | missed major event → free narrative scene next season (no SA) | emotional weight of the event; **explicitly cannot change the outcome** | `§4.4` |
| **C5 · Board-degree → scene Ob** | strategic DA degree shades the personal scene | FAILURE +1 Ob / SUCCESS −1 / OW −2 (a *modifier*, not state) | `§4.1` |
| **C6 · Scene Slate read-down** | slate generation reads world state to compose options | clocks, Accord, NPC Scars, Duty, Convictions → the player's surfaced choices (*presentation*) | master §6 (S0.3) |
| **C7 · Substrate observer delivery** | `compute_observers` is scale-agnostic (`§4.2`) | **any** peninsula/territory Key reaches a personal-scale observer whose state intersects its scale — the engine *already* delivers down | `key_substrate §4.2` |

**The gap (what is missing).** C2–C6 are **condition-driven or presentational** — a strategic *condition* (Order 0) spawns a scene, or a strategic *degree* shades a scene, or the slate *reads* state. **None defines how a provincial/peninsula *Key* (`da.*` / `state.*` / `env.*`) is delivered to a personal/scene/settlement consumer's contract as a Key with a payload and a mandatory effect on the present player.** C7 *is* such delivery at the engine level — but `scale_transitions §3`'s eight handoffs contain no matching explicit top-down rule, so the contract assessor's A6 check fires on every cross-scale consume seam.

**The tension is two-source and is exactly J-1:** `key_substrate §4.2` (scale-agnostic observer delivery — the stream already flows down) **vs** `scale_transitions §3` (no explicit down-handoff). The ruling: **(a)** declare §4.2 the canonical down-channel — engine-mediated delivery, A6-exempt, assessor gains a scale-agnostic-stream carve-out + tests (well-grounded: §4.2 has no scale predicate); **or (b)** author an explicit §3 top-down Key-delivery rule. *Not Claude's to choose — enumerated, carried OPEN.*

**The mechanism is more complete than "delivery" (second-pass sharpening, P3).** `key_substrate §4.1` step 4 runs `observer.apply_state_changes(interpretation, key.stat_deltas)` for **every** observer — so the engine not only *delivers* a Key down (via the scale-agnostic `§4.2`) but **applies its `stat_deltas`** to any intersecting personal-scale observer. The down-path already exists end-to-end. The real gap is **target-population, not capability**: strategic `da.*`/`env.*` Keys carry **faction/territory-scoped** targets and `stat_deltas` (registry schemas — `faction_id`, `target_territories`, `affected_territories`), **not personal-actor** ones, so there is no personal down-*effect* for step 4 to apply — and no §3 rule prescribes populating personal targets when a strategic event should land on a present player. This *strengthens* J-1 option (a): the engine machinery is in place; (a) adds authoring discipline (strategic emitters populate personal targets where intended) + §3 documentation, not a new delivery mechanism.

**The down-gap seams, enumerated** (cross-scale consume edges with no §3 delivery rule; module_map §1 `!A6`). The genuine strategic/peninsula→personal/settlement gap is **8 cross-band seam-pairs = 15 type-edges** (#1–8 below). The adjudicator's *raw* A6 count is **19**, because it also flags seam #9 (`scene_slate→piety_track`, scene→personal) — near-lateral, already covered as normal scene-event delivery in §2.1. Lead with **8 / 15**; 19 is the raw count:

| # | Seam (emitter → consumer) | Scale crossing | Key types (count) |
|---|---|---|---|
| 1 | `domain_actions` → `npc_behavior` | provincial → personal | `da.*` ×3 |
| 2 | `domain_actions` → `piety_track` | provincial → personal | `da.*` ×2 |
| 3 | `domain_actions` → `settlement_economy` | provincial → settlement | `da.economic_intervention` ×1 |
| 4 | `faction_politics` → `npc_behavior` | provincial → personal | `scene.investigation_resolved`, `state.*` ×3 (4) |
| 5 | `peninsular_strain` → `npc_behavior` | peninsula → personal | `env.peninsular_strain_shock` ×1 |
| 6 | `peninsular_strain` → `settlement_economy` | peninsula → settlement | `env.population_change` ×1 |
| 7 | `peninsular_strain` → `settlement_layer` | peninsula → settlement | `env.*` ×2 |
| 8 | `scenario_authoring` → `settlement_layer` | peninsula → settlement | `env.disaster` ×1 |
| 9 | `scene_slate` → `piety_track` | scene → personal | `scene.*` ×4 |

**Classification caveat (adversarial-review fix R4).** Seam 9 (`scene_slate → piety_track`, scene→personal) is **near-lateral, not strategic→personal top-down** — `scene_slate` is the scene-scale slate reader feeding Conviction Scars, so this edge sits *within* the personal/scene band rather than crossing down from the strategic layer. The "19" is the adjudicator's A6 count and is retained as-reported, but the **genuine strategic/peninsula→personal/settlement down-gap is the 8 cross-band seams (#1–8) = 15 type-edges**; seam 9 (4 edges) is a borderline inclusion. This does not change the J-1 decision — it sharpens the count the assessor's carve-out would clear.

`[OPEN — J-1: the eight cross-band seams resolve the same way once Jordan rules C7-exempt-vs-explicit-§3-rule. (`ED-1006` is the module-contract-extraction finding, **not** this gap — mis-cited in prior passes, corrected §7-bis P2; the gap's only handle is the docket key J-1.) The registry already lists these consumers for these types (e.g. `env.peninsular_strain_shock` consuming_systems include `npc_behavior`, `settlement_layer`) — the consume intent is canonical; only the *delivery rule* is missing. Not invented here.]`

### §2.5 — DIAGONAL (cross-scale AND cross-family; bottom-up covered, top-down absent)
*An edge is diagonal when it crosses both a scale and a Key-family boundary. Source: registry scale_signature + family; `scale_transitions §5.6`.*

| Diagonal edge | Crossing | Status |
|---|---|---|
| **Thread Echo:** personal Thread op (`meta.thread_woven`, personal) → faction stat (provincial) | personal→provincial + meta→faction | **COVERED** (bottom-up; capped ±, queued; §5.6) |
| **Accord Echo:** settlement-governance scene → faction-tier Accord | settlement→province + scene→derived | **COVERED** (bottom-up; ±1/Zoom-In; §5.5) |
| `da.public_governance` / `da.covert_betrayal` / `da.antinomian_action` (provincial, `da_outcome`) → `npc_behavior` (personal) | provincial→personal + da→scene-consumer | **ABSENT** — top-down diagonal; in the A6 seam set (#1) |
| `env.peninsular_strain_shock` / `env.crisis` (peninsula, `environmental`) → `npc_behavior` (personal) | peninsula→personal + env→scene-consumer | **ABSENT** — top-down diagonal; A6 seam #5 |

**Diagonal verdict:** the bottom-up diagonals (Thread/Accord Echo) are covered and safeguarded; the top-down diagonals (`da.*`/`env.*` → personal) are absent — the *same* J-1 gap, viewed across a family boundary as well as a scale boundary.

---

## §3 — THE KEY-TYPE EDGE MATRIX (primitive-grounded, with registry↔contract reconciliation)
*The 37 registered types (`key_type_registry §1–§9`) as directed edges: canonical emitter → canonical consumer. Drift column flags where the contract (`module_map §4.5`) diverges from the registry — read through the §0 name map. `[UNREG]` = emitted by a system per the substrate's own §8 but **absent from the registry** ⇒ `validate()` rejects (the F2 wall, master item 3), confirmed at the primitive.*

**Source-tier (read before trusting any row — adversarial-review fix R1).** The **emitter/consumer columns are PRIMARY canon** (`key_type_registry`, read live `ref=main` this session — fresh). The **"drift vs contract" column is DERIVED/SECONDARY** (`module_map §4.5`, generated from `module_contracts.yaml`) and inherits two known weaknesses: the verdict §7 caveat that ~40% of the contract graph is registry-shadow over-claim, and the fact that **`module_contracts.yaml` is itself one of the 6 currently registry-stale sources** (its declared pin lags live). Treat a registry edge as bedrock and a contract-only drift flag as a lead to verify, not a settled fact.

### Registered types by family
| Type | Emitter(s) (registry) | Consumer(s) (registry) | Scale | Drift vs contract |
|---|---|---|---|---|
| **scene_event** | | | | |
| `scene.dialogue` | scene_slate, social_contest | npc_behavior, conviction_track, faction_layer, articulation | personal | contract consumers = faction_state, npc_behavior, piety_track — **name map only** |
| `scene.witness` | scene_slate, npc_behavior | conviction_track, npc_behavior, articulation | personal | aligns (name map) |
| `scene.gift` | scene_slate, fieldwork | npc_behavior, faction_layer, articulation | personal | aligns |
| `scene.insult` / `scene.threat` | scene_slate, social_contest | npc_behavior, conviction_track, faction_layer, articulation | personal | aligns |
| `scene.interaction` | npc_behavior (Proc E) | npc_memory, articulation | personal | aligns |
| `scene.gossip` | npc_behavior (Proc E) | npc_memory, articulation | personal | **malformed yaml block in registry-derived view** (master item 11; LA-5) |
| **da_outcome** | | | | |
| `da.public_governance` | da_framework | faction_layer, npc_behavior, articulation | territory | emitter name `da_framework`→`domain_actions`; **npc_behavior consume = A6 seam #1** |
| `da.covert_betrayal` | da_framework | faction_layer, npc_behavior, articulation, conviction_track | territory | A6 seam #1/#2 |
| `da.diplomatic_alliance` | da_framework | faction_layer, articulation | territory/peninsula | aligns |
| `da.antinomian_action` | da_framework | faction_layer, npc_behavior, articulation, conviction_track | territory | A6 seam #1/#2 |
| `da.economic_intervention` | da_framework | faction_layer, settlement_economy, articulation | territory | **settlement_economy consume = A6 seam #3** |
| **mechanical_event** | | | | |
| `mechanical.season_change` | engine_clock | all subscribing | peninsula | contract: **no declared consumer (orphan A4)** — wildcard "all" not modeled |
| `mechanical.accounting` | engine_clock | faction_layer, articulation | peninsula | aligns |
| `mechanical.cascade_resolution` / `mechanical.mission_shift` | faction_layer | faction_layer, npc_behavior, articulation | territory | aligns |
| `mechanical.scene_entered/exited/skipped` | game_director | scene_timer, articulation, audit | personal/territory/peninsula | aligns (Class-B telemetry) |
| **state_transition** | | | | |
| `state.scar_acquired` | conviction_track | npc_behavior, faction_layer, articulation | personal | emitter `conviction_track`→`piety_track` |
| `state.standing_change` | faction_layer, faction_politics | npc_behavior, faction_layer, articulation | territory | aligns |
| `state.coup_attempted` / `state.succession` | faction_politics | faction_layer, npc_behavior, articulation | territory/peninsula | **npc_behavior consume = A6 seam #4** |
| `state.opinion_revised` | npc_behavior (Proc D) | articulation, npc_memory, social_contest | personal | aligns |
| `state.concern_resolved` | npc_behavior (Proc B) | npc_memory, articulation | personal | aligns |
| `state.belief_revised` | fieldwork | npc_behavior, articulation | personal | aligns (PP-688 Class-B) |
| **environmental** (source_actor=null) | | | | |
| `env.peninsular_strain_shock` | peninsular_strain | faction_layer, npc_behavior, articulation, settlement_layer | peninsula | **npc_behavior + settlement_layer consume = A6 seams #5/#7** |
| `env.crisis` | peninsular_strain, scenario_authoring | all | peninsula | contract: **orphan/pseudo-only** (no concrete consumer) |
| `env.disaster` | scenario_authoring, peninsular_strain | faction_layer, settlement_layer, articulation | territory | **settlement_layer consume = A6 seam #7/#8** |
| `env.population_change` | settlement_layer, peninsular_strain | faction_layer, settlement_economy | settlement/territory | **A6 seam #6** |
| **scene_outcome** | | | | |
| `scene.contest_resolved` | social_contest | npc_behavior, faction_layer, articulation | personal | aligns |
| `scene.battle_concluded` | mass_battle | faction_layer, npc_behavior, articulation, conviction_track | territory | **but module ALSO emits `scene_outcome.battle_concluded` [UNREG]** — naming drift (item 3/F2/J-2) |
| `scene.investigation_resolved` | scene_slate, faction_politics | faction_layer, npc_behavior, articulation | territory | A6 seam #4 (faction_politics path) |
| **system_meta** | | | | |
| `meta.knot_formed` / `meta.knot_ruptured` | fieldwork | npc_behavior, articulation (+conviction_track on rupture) | personal | aligns (PP-688 Class-B) |
| `meta.thread_woven` | threadwork | conviction_track, npc_behavior, articulation | personal | aligns |
| `meta.miraculous_event` | miraculous_event | faction_layer, npc_behavior, articulation | personal/settlement/peninsula | aligns; **always public + indelible regardless of scene scope** |
| `meta.legacy_event` | substrate (auto) | legacy-aware only | system_meta | Phase-B wrapper (pruned post-migration) |

### Unregistered-but-emitted (`[UNREG]` — the 7 F2 types, confirmed at the primitive)
| Type | Declared emitter | Primitive that declares it | Registry has it? |
|---|---|---|---|
| `scene.thread_operation` | threadwork | **`key_substrate §8.4`** ("thread operations emit scene.thread_operation Keys") | **NO** — registry §2/§8 omits it |
| `scene.draft_da` | domain_actions | **`key_substrate §8.6`** ("submission emits scene.draft_da") | **NO** — and DA outcomes are keyed `da.*`; strike candidate |
| `scene_outcome.battle_concluded` | mass_battle | module_map §4.5 | **NO** — registry has `scene.battle_concluded` (naming drift) |
| `mechanical.project_advanced` | npc_behavior (Proc C) | doc-12 §8 / module_map §4.5 | **NO** |
| `state.project_completed` | npc_behavior (Proc C) | doc-12 §8 | **NO** |
| `state.project_failed` | npc_behavior (Proc C, stall ≥8) | doc-12 §8 | **NO** |
| `scene.displacement` | npc_behavior | doc-12 §8 (displacement_neglect) | **NO** |

**This is the F2 root at the primitive, not the adjudicator:** the substrate's *own* §8 integration contract (§8.4, §8.6) declares emit types its *own* companion registry does not define — an internal contradiction in the canonical substrate pair, resolved only by J-2 (register via §10 Class-B, or strike from doc-12 §8 / substrate §8). Registry §9 also self-drifts: declares 37 types, parser counts 38 headings (A9, master item 11).

## §4 — THE QUANTITY-COUPLING LATTICE (granular stat→quantity edges beneath the Key edges)
*The resource lattice the Keys move. Each row: source → formula/mechanism → target, direction, cap/damper.*

**Source & verification status (adversarial-review fix R6).** The **faction multipliers and the settlement Mandate/Accord block below were re-read against the live primaries this session** (`derived_stats_v30 §14` + `settlement_layer_v30 §1.8`, `ref=main`) and **verified exact** — note both are among the 6 registry-stale sources, so the live read (not the stale pin) is the authority here. **Not re-verified this session:** the *personal* multipliers (Health/Stamina/Concentration/**Composure** — Composure carries the live ×3-vs-+6 drift, item 10/J-12), sourced from `derived_stats §14`'s personal block which was not extracted. **Out of scope here (pointed to, not transcribed):** the full seasonal **income/drain ledger** (`derived_stats §8.1` — Treasury ±, Legitimacy ±, Reputation ±, Discipline ± per action/event) and the **derived→stat ratchet** (`§8.2` — derived-value-at-0-through-Accounting → owning stat −1) are the edges that actually *move* these quantities; §4 captures the static derivation, not the per-season movement.

**Settlement-derived (deterministic accounting; A5 — never write the derived value, write the source):**
- settlement Order → **province Accord** = `⌊mean settlement Order⌋` (Order 0–5 → Accord 0–3; **clamp implied/unstated — item 8 / J-19**)
- settlement Prosperity → Local Economy `×50`; settlement Defense+Fort → Garrison `×20 + Fort×30`; settlement Order → Public Order `×20` (0 → riots)
- settlement L/PS/W → **faction Mandate** = `clamp(round(7T/(T+6)),0,7)`, `q=0.5L+0.5PS`, `T=ΣW·(q/7)` — **saturating + clamped (L3 damper)**
- faction Mandate → settlement L/PS = `drift ±1/settlement/season` — **mean-reverting (closes L3)**
- settlement Prosperity → faction Treasury income = `Σ Prosperity ×10`

**Faction-derived (`Stat×multiplier`; ✅ all five verified vs live `derived_stats §14` this session):** Wealth→Treasury `×100` · Stability→Discipline `×10` · Influence→Reputation `×15` · Military→Levies `×2` · Mandate→Legitimacy-meter `×20`.

**Personal-derived:** Endurance→Health `(End+6)×(MW+1)` (MW cap 3) · End+Spirit→Stamina `(3·End)+(2·Spi)` · Focus+Spirit→Concentration `(3·Foc)+(2·Spi)` · Charisma→Composure `×3` **[drift: ×3 vs +6 — item 10 / J-12]** · Spirit→Thread-Fatigue `×5`. **Wounds → every personal pool: −1D each** (the universal personal-scale debuff edge).

**Clock couplings (the campaign metronome — directed, with the central valve flagged):**
| Source | → Target | Rule | Cap / damper |
|---|---|---|---|
| **CI ≥ 60** | → **IP** | +2/season (**the Church→Altonia valve — the campaign's central pacing coupling**, E3.3) | — |
| territory Accord ≤1 (count) | → IP | banded +0/+1/+2/+3 (0–1 / 2–3 / 4–5 / 6+) | ED-743 |
| territory Accord ≤1 (each) | → Strain | +1/territory | **cap +3/season** |
| battles (in-phase) | → MS | −1 (−2 Campaign/War) | flat (×3 struck); net cap ±10 |
| MS (level) | → revelation bands | fall 60/40/20 | **recover 68/48/28 (hysteresis +8) + leading warnings (L5)** |
| Strain (bands) | → Legitimacy-pool / Accord / Mandate / MS | 3–4 / 5–6 / 7–8 / 9–10 threshold effects | C9.5 source caps |
| CI | → Parliament weight | Church `+⌊CI/20⌋`; anti-Church `−⌊CI/30⌋` | — |
| CI 100 | → Mass Seizure (forced) | declaration on `((CI−60)/40)^3.3` curve from 60 | one-shot |
| faction collapse | → Strain +2 / IP +2 / territories Uncontrolled | §1.5 exit | L6 amplifier (gated) |
| active treaty pair (each) | → Strain | −1 | cap −2/season |
| PI ≥ 20 | → Crown elimination | auto-resolve | — |

---

## §5 — FINDINGS THE PRIMITIVE PASS NEWLY GROUNDS (bottom-up; keyed to the live docket)
*What going to the primitives surfaces that the summary layer did not. No new ED IDs (ID-conflict backlog); each maps to an existing J-NN / LA item.*

1. **The 3-way name collision is confirmed at the source, not just the adjudicator.** The registry/substrate use canon names (`da_framework`, `faction_layer`, `conviction_track`); the contracts use impl names (`domain_actions`, `faction_state`, `piety_track`); `conviction_track`(→piety_track) further collides with `territorial_piety` and `ci_political`. → **item 7 / J-2·J-4 / LA-4.**
2. **F2 is an internal contradiction in the canonical substrate pair.** `key_substrate §8.4` declares threadwork emits `scene.thread_operation` and `§8.6` declares DA submission emits `scene.draft_da` — neither is in the companion `key_type_registry`. The substrate spec contradicts its own registry; `validate()` (§2.3 #2) would reject both. → **item 3 / J-2 (register via §10 or strike from §8).**
3. **`scene.battle_concluded` (registered) vs `scene_outcome.battle_concluded` (emitted) is a live naming drift**, with the registered form in the `scene_outcome` family but carrying a `scene.` prefix. → **item 3 / J-2 (resolve to the registered form).**
4. **The top-down "engine-mediated exempt" option (J-1 path a) is well-grounded — newly confirmed.** `key_substrate §4.2 compute_observers` has **no scale predicate**: `actors_in_scale` already delivers a peninsula/territory Key to any intersecting personal-scale observer. The stream *already flows down*; the only thing missing is a matching `scale_transitions §3` handoff rule for the assessor to cite. This strengthens ruling (a) over (b). **Sharpened (P3):** `§4.1` step 4 applies `stat_deltas` for every observer, so the engine already *delivers and mutates* down — the gap is **target-population** (strategic `da.*`/`env.*` Keys carry faction/territory-scoped targets, not personal ones), not delivery capability. → **item 1 / J-1.**
5. **Domain Echo writes `±Mandate` directly in canon text.** `scale_transitions §5.4` (Debate→Echo) literally specifies "+1 Mandate / −1 Mandate" and `params/scale_transitions` repeats it — but Mandate is a derived aggregate (R4). The echo must route ΔL/ΔPS to the settlement and re-aggregate (the Accord Echo §5.5 already does this correctly via AUD-SET-02; the Mandate/Debate/Thread echoes do not). → **item 2 / F1 / J-7·J-8.**
6. **`params/scale_transitions` is pre-pivot TTRPG-framed.** v0.14, dated 2026-04-03, repeatedly invokes "GM recognises faction scope" / "GM makes final scope determination" — but the project is videogame-only with no GM (every "GM decides" must resolve to Authored/Deterministic/AI/Player/Default). The design doc `scale_transitions_v30` is cleaner but inherits the mode framing in §1/§6. → **item 11 (mode residue, C-11 class) / LA-11.**
7. **Orphans and coverage gaps reconfirmed at type level:** `mechanical.season_change` (registry "all subscribing" vs contract no concrete consumer) and `env.crisis` (registry "all" vs orphan) are unconsumed; **MS has no owning module** in the contracts (module_map §2). → **item 11 / A4 / LB-5 regen.**

`[NULL: examined the full registry (37 types) + substrate §4/§8 + scale_transitions §3–§10 for *new* P1 edge defects beyond the already-ledgered J-1/J-2/J-7 set — none found. The edge architecture is sound; the gaps are the known missing-direction (J-1), missing-registration (J-2), and derived-write-routing (J-7) classes, now grounded at the primitive.]`

---

## §6 — COVERAGE VERDICT PER DIRECTION & SUPERSESSION

**Verdict (granular, per the six canonical directions):**

| Direction | Coverage | Basis |
|---|---|---|
| **lateral / horizontal** | ✅ complete | §2.1 — scene-internal + provincial-internal + §3.9 lateral fieldwork, all canonically wired |
| **bottom-up** | ✅ covered & safeguarded | §2.2 — Domain/Debate/Accord/Thread Echo (capped, gated, queued) + Accounting recompute; A5 guards the inverse |
| **vertical** | ◐ half-covered | §2.3 — all eight named §3 handoffs run up/lateral; §3.7's narrow duel is the lone down-*handoff*; §3.9 carries a down-*modifier* (BG-Survey→TTRPG-Discovery) — none is Key-delivery |
| **top-down** | ⛔ OPEN (J-1) | §2.4 — C1–C7 channels exist (condition/modifier/presentation/engine-observer); the engine already delivers+applies down (§4.1 step 4) but no §3 rule + strategic Keys carry no personal targets; **8 cross-band seams / 15 type-edges** (19 raw assessor count) |
| **diagonal** | ◐ split | §2.5 — bottom-up diagonals (Thread/Accord Echo) covered; top-down diagonals (`da.*`/`env.*`→personal) absent (same J-1 gap) |
| **substrate (universal)** | ✅ complete | §1 — single-update rule routes every edge; observer resolution defines the fan-out |

**The single structural sentence, granular:** the graph is **fully wired laterally and bottom-up, safeguarded at every loop, and delivers down at the engine level (§4.2) — but has no canonical `scale_transitions §3` top-down handoff rule, which is the J-1 decision and the only thing between this graph and Robust.**

**Supersession.** This atlas **extends** `valoria_interdependency_master_v1.md` §5 (granular companion); it does **not** supersede it — both stay live, master as the navigable layer, atlas as the edge-level depth. The primitives read this session (`scale_transitions_v30`, `key_type_registry_v30`, `key_substrate_v30`, `params/scale_transitions`) are **canon, read-only** — not folded. No new ED IDs assigned; every finding routes to the existing J-1/J-2/J-7/J-19/LA-5/LA-11 docket for Jordan adjudication.

## §7 — ADVERSARIAL REVIEW & RECONCILIATION RECORD (2026-06-11, this session)

`[SELF-AUTHORED — bias risk]` Dispassionate self-audit of this atlas **and** `valoria_interdependency_master_v1.md`, treating both as external work and hunting what the author is incentivized to miss. **Verdict: the registry-/scale_transitions-/substrate-grounded core is sound and now partly live-verified; the weaknesses are epistemic — source-tier conflation, inherited (not re-derived) safety claims, and a supersession over-claim — all reconciled below. No fabricated findings; no claim cleared without the look.**

**The meta-finding (subsumes R1/R2):** this is a large synthesis built almost entirely on the author's own prior synthesis, and the one external check already on record (verdict §7) warned ~40% of the contract graph is registry-shadow over-claim. The master and atlas *amplified* confidence rather than damping it. Reconciliation: the bedrock is the **primary canon** read live this session (`key_type_registry`, `key_substrate §4.1/§4.2/§8`, `scale_transitions §3–§10`, and now `derived_stats §14` + `settlement §1.8`); everything **contract-/module_map-derived** is demoted to secondary and flagged inline.

| # | Finding (what a dispassionate reviewer attacks) | Sev | Disposition |
|---|---|---|---|
| **R1** | Edge tables conflated **primary** (registry) and **derived** (contract/module_map) sources as co-equal. | 1 | **FIXED** — §3 now tier-marks; registry = bedrock, contract drift = lead-to-verify. |
| **R2** | Loop-safety / sim results ("ratified; P(collapse) 0.41→0.97") presented as fact; trail = reads, not re-derivation. | 1 | **RECONCILED (labelled)** — these are **INHERITED from the source audits (game_flow §8, verdict A7), not re-verified this session.** Master §7 / §9 carry the same inheritance. |
| **R3** | Master §11 claimed the 3 source views "consolidated into this master" (superseded) **while also** calling flat-spec a live "value-table reference" — a contradiction; and no `[SUPERSEDED-BY]` markers were ever written. | 1 | **FIXED** — master §11 reframed: the views are **complementary live sources synthesized/indexed**, not superseded. Honest framing: this was *build-one-index-over-N*, not *collapse-N-to-1*; artifact count rose because master+atlas are new synthesis layers — appropriate, since the sources are distinct detail, not redundant copies. |
| **R4** | Seam-9 (`scene_slate→piety_track`) is near-lateral, not top-down — inflates the down-gap count. | 2 | **FIXED** — §2.4 caveat; genuine down-gap = 8 seams / 15 edges. |
| **R5** | Master item 2 bundles two distinct Jordan decisions (faction-stat write-path **J-7** vs Mandate-echo routing **J-8**). | 2 | **NOTED** — the row already names both; flagged here as two decisions, not one. |
| **R6** | §4 multipliers were secondary-sourced, in a drift-prone area whose primary (`derived_stats`) is registry-stale. | 2 | **FIXED by verification** — faction multipliers + Mandate/Accord block **re-read live and verified exact**; personal multipliers + the §8.1/§8.2 income-drain ledger marked unverified/out-of-scope (§4). |
| **R7** | Freshness never investigated — 6 stale canonical sources flagged every bootstrap. | 3 | **RESOLVED** — checked: 6 stale = settlement_layer, derived_stats, key_substrate, articulation_layer, module_contracts; **4 are load-bearing here.** All primitives I cite were read live (`ref=main`), ahead of their stale registry pins — citations are current; the staleness is a pre-existing pin lag (LB-6), not a read defect. |
| **R8** | Master item 10's non-Composure drifts (Stamina/Concentration/Combat-pool/Intel) waved at "LA-5"; LA-5 is index-regen, not formula propagation. | 3 | **NOTED** — these are mechanical propagation lacking a precise docket home; surface for a docket entry. |

`[NULL: searched both artifacts for a *substantive* error — a wrong edge, a fabricated mechanism, a mis-cited formula. None found beyond the tier/inheritance/framing weaknesses above. The §4 formulas verified exact against live primaries; the edge set matches the registry; the gap is enumerated honestly. The defects are epistemic-presentation, not factual.]`

**Net effect of reconciliation:** confidence is now **calibrated, not flattened** — the primary-canon core is verified-live and marked bedrock; the contract-derived layer is demoted and flagged; the safety verdict is labelled inherited; the supersession story is corrected. Nothing was invented to fill the top-down gap, and nothing factual required retraction.

### §7-bis — SECOND ADVERSARIAL PASS (post-granular-extension, this session)

`[SELF-AUTHORED — bias risk]` A second dispassionate pass, *after* the granular extension, treating the §0–§6 build and the master as external work. **Verdict: the first pass (R1–R8) is present, but two of its fixes were never propagated and one canonical mis-citation survived both prior passes. Three findings are real and corrected here; the granular edge set itself survives the second look. No new fabrication.**

| # | Finding (what a dispassionate reviewer attacks) | Sev | Disposition |
|---|---|---|---|
| **P1** | **R4's seam correction (8/15) was added as a footnote-caveat but never propagated** — the §2.4 header, the "19 A6 seams" intro, the `[OPEN]` tag, and the §6 summary all still headlined **19/9**, contradicting the caveat. A fix stated once and contradicted four times. | 2 | **FIXED** — propagated: every assertion now leads with **8 cross-band seams / 15 type-edges**; **19 (9 pairs)** is named as the raw assessor count, with seam #9 flagged near-lateral. |
| **P2** | **`ED-1006` mis-cited — survived both prior passes** (neither verified ED IDs against the ledger). The canonical `editorial_ledger.jsonl` has `ED-1006` = *"Stage-1 module-contract extraction (27 modules)"*, **not** the top-down gap. The atlas attached it to J-1; the master attached it to items 1/7. | 2 (worst-failure class: wrong canonical claim) | **FIXED** — ED-1006 removed from the top-down/naming references; the handles are the docket keys **J-1 / J-2 / J-4**, and the source ED for those *adjudication* sub-findings is **ED-1009** (the verdict), not ED-1006 (the extraction — which legitimately is item-5/shadow-modules). Verified against the live ledger this session. |
| **P3** | **Down-delivery was under-characterized** — the atlas said §4.2 "delivers down" and stopped. `§4.1` step 4 (`apply_state_changes(interpretation, key.stat_deltas)`) means every observer **applies** the Key's deltas; with §4.2 scale-agnostic, the engine already **delivers *and* mutates** down. | 2 (logic extension) | **FIXED (extended)** — §2.4/§5/§6 sharpened: the gap is **not delivery capability** but **target-population** — strategic `da.*`/`env.*` Keys carry faction/territory-scoped targets+deltas (registry schemas), not personal ones, so step 4 has no personal effect to apply; and no §3 rule prescribes populating them. This strengthens J-1 option (a) further. |
| **P4** | **The master self-contradicts on the down-handoff** — it *lists* `Mass→Personal (general duel)` among the handoffs, then asserts "all run upward — none downward" / "all 9 run upward" (rows 130/137/202). | 2 | **FIXED** — master corrected: the eight named §3 handoffs run up/lateral **except §3.7 (the lone down-handoff, a duel)**; §3.9 carries a down-*modifier*; none is top-down Key-*delivery*. |
| **P5** | **§6 vertical row omitted the §3.9 BG-Survey→TTRPG-Discovery down-modifier** (a sibling of the C5 board-degree modifier). | 3 | **FIXED** — noted in §6 + the §2.4 channel set. |

**Two process lessons (extend the method):**
1. **Propagate, don't caveat.** A correction added as a single footnote while the headline assertions keep the old number is *worse* than no fix — it manufactures internal contradiction. Every restatement of a corrected fact must change, not get annotated once.
2. **ED citations must be ledger-verified.** Two passes asserted `ED-1006` for the top-down gap without opening `editorial_ledger.jsonl`; the third did and found it wrong. Given the ~94-ID-conflict backlog, no ED reference is trustworthy from memory — verify against the canonical ledger or use the docket J-key.

`[NULL: this second pass found no NEW substantive edge error — no wrong edge, no fabricated mechanism, no mis-derived formula — beyond the non-propagated fix (P1), the memory-sourced citation (P2), and the under-stated mechanism (P3). The granular edge set, the registry/substrate groundings, and the §4 live-verified formulas all survive. The defects were epistemic/consistency, not factual; nothing factual was retracted.]`

---
*Method: bottom-up from the four canonical primitives (full reads, pinned SHAs in the banner; `derived_stats §14` + `settlement §1.8` additionally verified live in §4) cross-checked against `module_map_flat.md §4.5`. Every edge cites its primitive. No mechanical value invented; the top-down gap is enumerated seam-by-seam, never filled. §7 is the adversarial-review record. `[SELF-AUTHORED — bias risk]` throughout.*

