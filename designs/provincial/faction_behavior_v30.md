<!-- [PROVISIONAL: 2026-05-01 — PP-686 v2 spec, faction behavior architecture, ratified per integration plan §3.2 commit 3] -->
<!-- STATUS: PROVISIONAL — Class A canonical document; consumes PP-687 substrate. -->
<!-- AUTHORITY: PP-686 (this doc); supersedes params/bg/core.md §Ethical Framework Modifiers and partial supersession of Mandate-as-single-scalar. -->

# Faction Behavior Architecture (PP-686 v2)

**Class:** A — strategic-layer system replacing legacy Ethical Framework Modifiers.
**Status:** PROVISIONAL.
**Sequencing:** consumes PP-687 substrate; reads PP-684 Conviction taxonomy.
**Companion docs:** `designs/architecture/key_substrate_v30.md`, `designs/architecture/key_type_registry_v30.md`, `designs/personal/conviction_taxonomy_v30.md`, `designs/personal/conviction_axis_matrix_v30.md`.
**Co-files updated:** `references/canonical_sources.yaml`, `params/bg/core.md` (Ethical Framework Modifiers struck), `params/factions.md`, `params/factions_personal.md` (faction-stat schema), `params/bg/tracks.md` (Mandate becomes derived), `references/glossary.md`, `references/alias_registry.yaml`, `canon/supersession_register.yaml`.

---

## §1 Statement

A faction's behavior is determined by four interacting components:

1. **Mission** — what the faction is trying to accomplish (telos, authored, evolves under defined triggers)
2. **Cascade** — how the faction conducts itself (modus, derived from leadership Convictions through hierarchical α-weighted blending)
3. **Public Expectation** — what the populace expects from the faction's role (Conviction-shaped, derived from role + Mission consistency)
4. **Legitimacy + Popular Support** — populace acceptance and active backing (separately tracked, modulating Public Expectation strictness)

Domain Action Ob is computed from action alignment with all four. Mandate is retained as a derived value during transition.

The architecture eliminates philosophical-tradition vocabulary (Categorical Imperative, Rawlsian, etc.), unifies Conviction vocabulary across personal and faction scales (per PP-684), and produces dynamic faction behavior from a small authored input set + leader Convictions + Public temperament.

This is v2 of the original proposal (`designs/audit/2026-04-30-architecture-session/03_PP-686_proposal.md`) with the C1–C10 calibration set and audit P1/P2 resolutions applied.

---

## §2 Faction State Schema

```yaml
faction:
  # Authored
  id: <faction_id>
  role: <sovereign | ecclesiastical | mercantile-procedural | intelligence-diplomatic | reformist | military-order>
  mission:
    text: <short string>
    primary_objective: <victory_track | DA_category>
    beneficiary: <actor_or_population_ref>
    aligned_categories: [<da_subtype>, ...]
    contradicted_categories: [<da_subtype>, ...]
    authored_at: <date>
    prior_mission: <mission | null>
  leader: <npc_id>
  organizational_hierarchy:
    nodes: [<npc_id>, ...]
    edges:                                   # supervisor edges per §3.2.1
      - {npc: <id>, supervisor: <id | null>}
    cascade_roots: [<npc_id>, ...]           # multi-root per §3.2.2
  institutional_culture: <-0.2..+0.2>        # α_institution adjustment

  # Stateful (decay/integrate per Accounting)
  legitimacy: <0..7>
  popular_support: <0..7>

  # Derived (recomputed each Accounting; emit cascade_resolution Key)
  aggregate_effective_convictions: {<conviction>: <weight>, ...}
  cascade_fidelity: <-1..+1>
  expected_convictions: {<conviction>: <weight>, ...}
  strictness: <0..1>
  mandate: <0..7>                            # transitional, derived
```

---

## §3 Components

### §3.1 Mission

A faction has one Mission (`faction.mission`) — a stated telos with authored alignment categories.

**Mission alignment evaluation per DA:**

```
mission_alignment_modifier(da_outcome_key, mission):
    if da_outcome_key.type in mission.aligned_categories:
        return -1                            # Ob bonus
    if da_outcome_key.type in mission.contradicted_categories:
        return +1                            # Ob penalty
    return 0
```

`aligned_categories` and `contradicted_categories` reference **PP-687 da_outcome subtypes** (per `key_type_registry_v30.md` §3): `da.public_governance`, `da.covert_betrayal`, `da.diplomatic_alliance`, `da.antinomian_action`, `da.economic_intervention`. This resolves audit P1-3.

**Mission shift triggers** (resolves 686-OQ8). Mission shifts on any of:

1. **Victory-track milestone passes/fails** — faction crosses (or definitively fails to cross) a victory-condition threshold (e.g., Hafenmark Parliamentary Sovereignty victory milestone).
2. **Leader replacement under exceptional circumstances** — `state.succession` Key with `succession_mode in [contested, emergency, imposed]`.
3. **Mission failure threshold reached** — ≥4 consecutive seasons of Mission-contradicting outcomes (counted via `da_outcome.*` Key stream filtered by `mission_alignment == penalty`).
4. **Authored event in scenario** — explicit Mission-shift trigger from scenario authoring.

A Mission shift emits `mechanical.mission_shift` Key (PP-687 §4); existing `da.aligned/contradicted` interpretations recompute against the new Mission.

### §3.2 Cascade

#### §3.2.1 Supervisor graph schema (resolves audit P1-1)

Each NPC carries an optional `supervisor_id`:

```yaml
NPC.supervisor_id: <npc_id | null>
```

For cascade leaders, `supervisor_id = null` AND the NPC appears in `faction.organizational_hierarchy.cascade_roots`.

**Orphan handling (C6):** if `NPC.supervisor_id` references a non-existent or out-of-faction NPC, the orphan is treated with `α = 1.0` (full self-determination); their `effective_convictions = personal_convictions`; they contribute to faction aggregate normally. Validator emits a warning at faction state load.

**Zero-vector leader:** if cascade root's `personal_convictions` magnitude < 0.1, faction enters Provisional state where succession is forced next Accounting; aggregate computes only from non-leader NPCs in the interim.

#### §3.2.2 Multi-root cascade allowance (resolves audit P2-2 = D3)

A faction may have **multiple parallel cascade roots**, one per institutional sub-hierarchy. The Crown's secular governance, military command, and household are three distinct hierarchies that can cascade locally even though all serve the same Mission.

```yaml
faction.organizational_hierarchy.cascade_roots:
  - <npc_id_secular_root>
  - <npc_id_military_root>
  - <npc_id_household_root>
```

Each cascade root spawns a separate cascade graph. Each root's effective_convictions are computed independently. Faction aggregate = weighted average of per-root aggregates, weighted by role-extent within faction (default uniform; authored per faction).

A faction with a single cascade root (e.g., a small reformist movement) has `cascade_roots: [leader]` and the multi-root form degenerates to single-root. Default for new factions: single-root.

#### §3.2.3 Cascade math

For each NPC with non-null supervisor:

```
effective_convictions(npc) =
    α(npc) × personal_convictions(npc)
  + (1 − α(npc)) × effective_convictions(supervisor(npc))
```

For cascade root: `effective_convictions(root) = personal_convictions(root)`.

**Setting α:**

```
α(npc) = clamp(
    α_base
  + α_seniority(npc.standing)
  + α_institution(faction.institutional_culture)
  , 0, 1)
```

| Component | Range | Notes |
|---|---|---|
| `α_base` | 0.4 | Default |
| `α_seniority` | -0.2 to +0.4 | Standing 1: -0.2; Standing 7: +0.4 (linear) |
| `α_institution` | -0.2 to +0.2 | Hafenmark = -0.2 (rigid); Crown = 0; Restoration = +0.1; Lowenritter = -0.1 |

These are starting values; calibrated at Stage 10 sim.

#### §3.2.4 Cascade re-resolution timing (resolves audit P2-5)

Cascade re-resolves at each Accounting (season boundary) or on `state.succession` Key emission.

**Mid-season ordering rule:** DAs fired within a season use the cascade resolved at the **prior** Accounting. A mid-season `state.succession` Key triggers immediate cascade re-resolution but the new values apply only to subsequent sub-step Keys; earlier sub-step Keys in the same season retain their prior cascade context.

`mechanical.cascade_resolution` Key emitted with old + new aggregates and triggered_by reason. Effective Convictions damp toward new equilibrium with **drift_coef = 0.6** per season (C3 finalization; calibrate at Stage 10).

#### §3.2.5 Crisis-bypass rule (C4)

When `leader.scars >= 3`, cascade damping is suspended for that leader's tier. New leader Convictions propagate immediately each season until `scars < 3`. This produces visible institutional instability under leader Conviction crisis (per artifact 06 §1.3 finding).

#### §3.2.6 Aggregate effective Convictions (resolves audit P1-2 = C9)

```
aggregate_effective_convictions(faction) = normalize(
    Σ over npc in faction:
        npc.standing × effective_convictions(npc)
)
```

Standing-weighted normalized sum. Senior NPCs contribute more to faction modus. Sim §1.5 v1 confirmed this produces sensible aggregate values.

For multi-root cascade (§3.2.2), per-root aggregates compute first, then faction aggregate is a weighted average over roots.

### §3.3 Public Expectation

Each faction has an expected Conviction profile derived from role:

```
expected_convictions(faction) = role_template(faction.role)
```

#### §3.3.1 Role templates (with Honor as 13th Conviction per D1)

| Role | Expected Convictions (weighted) |
|---|---|
| sovereign | Virtue: 0.30, Authority: 0.30, Honor: 0.20, Faith: 0.10, Warden: 0.10 |
| ecclesiastical | Faith: 0.40, Authority: 0.20, Scholastic: 0.20, Precedent: 0.10, Virtue: 0.10 |
| mercantile-procedural | Order: 0.35, Utility: 0.25, Scholastic: 0.20, Liberty: 0.10, Equity: 0.10 |
| intelligence-diplomatic | Scholastic: 0.30, Utility: 0.30, Authority: 0.20, Precedent: 0.10, Identity: 0.10 |
| reformist | Equity: 0.30, Liberty: 0.25, Community: 0.20, Virtue: 0.15, Scholastic: 0.10 |
| military-order | Honor: 0.30, Authority: 0.25, Virtue: 0.15, Identity: 0.15, Order: 0.15 |

Templates use the 13-Conviction taxonomy from PP-684 §2. Honor appears in sovereign, intelligence-diplomatic (low weight), and military-order templates per D1 ratification.

#### §3.3.2 Cascade Fidelity

```
cascade_fidelity(faction) = cosine_similarity(
    aggregate_effective_convictions(faction),
    expected_convictions(faction.role)
)
```

Range `[-1, +1]`. 1 = perfect role fidelity; 0 = orthogonal; -1 = inverse.

Computed in 13-Conviction vector space (not 4-axis) for player legibility. Engine math may use the matrix-projected 4-axis form for dot-product efficiency where appropriate.

#### §3.3.3 Public Expectation = expected Convictions + Mission consistency

A faction whose stated Mission contradicts its role's expected Convictions reads as "incoherent" to populace and pays a per-season Legitimacy cost (per §3.5 violation event score).

### §3.4 Popular Support

A scalar `[0, 7]` tracking active populace backing. Updates per Accounting:

```
ΔPopular_Support per season =
    α_temperament × attributed_mission_outcome(faction)
  + β_temperament × cascade_fidelity(faction) × outcome_polarity_gate
  + γ × (random shock; events)
```

where:

- `attributed_mission_outcome(faction)` ∈ `[-1, +1]`: aggregated `da_outcome.*` Key stream, with **Self-Other modulation per actor** (PP-684 §3.1):
  ```
  attributed_outcome = raw_outcome × (1 − 0.5 × max(0, leader.self_other_orientation))
  ```
  This is C7. Self-aggrandizing leaders see reduced PS attribution.

- `outcome_polarity_gate` ∈ `{0.5, 1.0}`: **β-fidelity gating (C5)** — if `attributed_mission_outcome` < 0, gate = 0.5; otherwise 1.0. Prevents pure-conduct PS climbing during persistent failures.

- `α_temperament + β_temperament = 1` (per OQ7 default — keep constraint).

- `γ`: scaling for major events (default 0.5; specific to event type).

#### §3.4.1 Public temperament (5-temperament typology, OQ4)

Authored per-territory:

| Public temperament | α (outcomes) | β (conduct) | Period example |
|---|---|---|---|
| pragmatic | 0.7 | 0.3 | Florentine merchant class |
| traditional | 0.3 | 0.7 | rural devout populace |
| balanced | 0.5 | 0.5 | mixed urban populace |
| principled | 0.2 | 0.8 | reformist enclaves |
| outcomes-only | 0.9 | 0.1 | hardship populations under direct threat |

Faction effective temperament = population-weighted average across faction's territories.

#### §3.4.2 Strain interaction (resolves audit P2-3)

`env.peninsular_strain_shock` Keys consumed by faction's public-temperament dynamics: high Strain shifts effective temperament weights toward `outcomes-only` (raises α, lowers β) reflecting populace urgency under pressure:

```
on env.peninsular_strain_shock(strain_delta, affected_territories):
    for territory in affected_territories:
        if strain_delta > 0:
            territory.temperament_drift = clamp(
                territory.temperament_drift + 0.1 × strain_delta,
                -1, +1
            )
            # drift biases toward outcomes-only over multiple shocks
```

Faction's effective temperament is recomputed at Accounting from per-territory current temperaments (drift-modified).

### §3.5 Legitimacy

A scalar `[0, 7]` tracking populace acceptance. Slower-moving than Popular Support; integrates over many seasons.

```
ΔLegitimacy per season =
    +λ_continuity × seasons_in_role_uninterrupted
  + λ_procedural × procedural_event_score(faction, this_season)
  + λ_expectation × cascade_fidelity(faction)         # slow integration
  - λ_violation × violation_event_score(faction, this_season)
```

with `λ_continuity = 0.05`, `λ_procedural = 0.3`, `λ_expectation = 0.1`, `λ_violation = 0.6` (starting values; calibrate at Stage 10).

#### §3.5.1 Procedural events (build Legitimacy)

Read from PP-687 Key types:
- `da.diplomatic_alliance` (treaty signed) → +1
- `state.succession` with `succession_mode == normal` → +1 (one-time)
- `mechanical.mission_shift` with `trigger == authored` (formal redefinition with public ceremony) → +0.5
- Religious sanction Keys (`meta.miraculous_event` favorable to faction) → +1
- Formal acknowledgement by foreign power Keys → +0.5

#### §3.5.2 Violation events (erode Legitimacy)

- `da.covert_betrayal` with `exposed == true` → +1 (violation score; subtracts from L)
- `state.coup_attempted` (any outcome) → +1
- `meta.miraculous_event` unfavorable (excommunication, heresy declaration) → +2
- `state.standing_change` with `magnitude == 3` (Total Dismissal) involving faction leader → +1
- Public failure of role-defining obligation (low Cascade Fidelity for ≥4 consecutive seasons) → +0.5/season

Multiple violations same season **sum** (not max, per artifact 04 P3-4 default; sequential-processing alternative deferred).

### §3.6 Public Expectation Strictness

```
strictness(faction) = clamp(
    base_strictness + 0.5 × (Legitimacy / 7) − 0.3 × (Popular_Support / 7)
  , 0, 1)
```

with `base_strictness = 0.4` default.

| Legitimacy | Popular Support | Strictness | Effect |
|---|---|---|---|
| high | high | 0.4 | strong but elastic |
| high | low | 0.7 | strong and brittle |
| low | high | 0.2 | weak — populist tolerated |
| low | low | 0.4 | weak — collapse zone |

Strictness is used **only as deviation cost modulator** (C2 — drop the strictness reward path; sim v2 confirmed reward path saturated against Ob cap).

### §3.7 Domain Action Ob Calculation

Per `da_outcome.*` Key submission:

```
expectation_alignment_modifier(da, faction) =
    sign(da.cascade_alignment_with_role) × strictness(faction) × {1, 2}
    # +1 if action is ±1 from role expectation, +2 if ±2 deviation

Ob_modifier(da, faction) =
    mission_alignment_modifier(da, faction.mission)               # -1, 0, +1
  + cascade_alignment_modifier(da, faction.aggregate_effective_convictions)  # -1, 0, +1
  + expectation_alignment_modifier(da, faction)                    # ± strictness × {1, 2}

# Final clamp at ±2 (C1; was ±3)
Ob_modifier = clamp(Ob_modifier, -2, +2)
```

Sim v1+v2 confirmed: ±3 produced dominant-strategy at high alignment; ±2 cap removes that without losing directional signal.

Modifier rounding: ≥0.5 rounds to ±1; ≥1.5 rounds to ±2.

### §3.8 NPC Behavior Coupling (resolves audit P2-1)

NPCs read **effective_convictions** in faction-role context and **personal_convictions** in personal-time context. Context flag from Key payload:

```yaml
Key.payload:
  role_acting: <bool>
  # true: action performed in faction-role capacity (DA submission, formal scene as faction agent, military command)
  # false: personal-time action (private conversation, off-duty scene, personal Threadwork)
```

Both armatures coexist on the NPC:

```yaml
NPC:
  personal_convictions: {<conviction>: <weight>}
  effective_convictions: {<conviction>: <weight>}    # derived per Cascade
  armature_position_personal: [4-axis vector]        # derived from personal_convictions
  armature_position_role: [4-axis vector]            # derived from effective_convictions
```

The armature consulted for a given Key emission depends on `Key.payload.role_acting`. Default for `da_outcome.*` and `mechanical.cascade_resolution`: role_acting=true. Default for `scene.dialogue` in personal time, `scene.gift`, etc.: role_acting=false.

This resolves the major audit P2-1 ambiguity: the architecture supports both, with explicit context flag.

### §3.9 Edge Cases (resolves audit P2-4)

| Case | Rule |
|---|---|
| Orphan NPC (supervisor_id resolves to non-existent NPC) | α = 1.0; effective = personal; warning logged |
| Zero-vector leader (personal_convictions magnitude < 0.1) | Faction enters Provisional state; aggregate from non-leader NPCs only; succession forced next Accounting |
| Cascade cycle (NPC's supervisor chain loops) | Validator rejects faction state load |
| Faction with no leader temporarily | Aggregate from all members with α=1.0 each; Legitimacy decays at +λ_violation × 0.5/season until succession |
| Cosine similarity zero-magnitude vectors | cascade_fidelity = 0 (mathematical fallback) |

---

## §4 Mandate (Transitional)

```
Mandate(faction) = round(0.5 × Legitimacy + 0.5 × Popular_Support)
```

Mandate remains queryable for backward compatibility (resolves OQ6 — transitional retention). Existing consumers (Church Excommunication Ob, AER advancement, victory conditions, etc.) continue to function. Refactor of consumers to read Legitimacy or Popular Support directly is opportunistic.

**Initial values at engine init (preserves continuity for existing scenarios):**
```
Legitimacy_init = current_authored_Mandate × 1.0
Popular_Support_init = current_authored_Mandate × 1.0
```

After first season, dynamics replace seed values.

---

## §5 Integration with PP-687 Substrate

### §5.1 Faction state changes emit Keys

| State change | Emit Key |
|---|---|
| Mission shift | `mechanical.mission_shift` |
| Leader change | `state.succession` |
| Cascade re-resolution | `mechanical.cascade_resolution` |
| L crosses threshold (e.g., L < 2 = "collapse zone") | `state.coup_attempted` (probabilistically) |

### §5.2 Faction consumes Keys

| Key type | Faction-state effect |
|---|---|
| `da_outcome.*` | Mission outcome attribution → ΔPS, ΔL |
| `state.scar_acquired` (leader) | Triggers cascade re-resolution; if scars≥3, crisis-bypass activates |
| `state.succession` | Triggers immediate cascade re-resolution; succession_mode determines violation_event_score |
| `env.peninsular_strain_shock` | Public temperament drift |
| `mechanical.accounting` (annual) | Triggers Self-Other drift integration; emits faction summary Keys |

### §5.3 Subscription pattern

PP-686 registers faction-layer subscribers in `TYPE_SUBSCRIPTIONS` per PP-687 §4.1 step 5. All subscription callbacks O(1) or async. Faction state recomputation runs at season boundaries; per-Key callbacks queue updates rather than execute mid-emission.

---

## §6 Migration Plan

### §6.1 Required prior work

- PP-684 ratification (12-Conviction taxonomy + Self-Other axis): **DONE** (commit 2 of integration plan).
- PP-685 ratification (migration roster): **DONE** (commit 2 of integration plan).
- PP-687 ratification (substrate): **DONE** (commit 1 of integration plan).

### §6.2 Implementation sequence (Phase B per PP-687 §7.1)

| Stage | Task | Effort |
|---|---|---|
| 1 | Author this doc as canonical (this commit) | 0 (this commit) |
| 2 | Update `params/bg/core.md`: Strike Ethical Framework Modifiers; reference §3.7 Ob calculation | 0.3 |
| 3 | Update `params/factions.md`, `params/factions_personal.md`: add Legitimacy + Popular Support fields; deprecate Ethical Framework field | 0.3 |
| 4 | Update `params/bg/tracks.md`: Mandate becomes derived | 0.1 |
| 5 | Author Mission + organizational_hierarchy + institutional_culture for all 6 factions | 0.5 |
| 6 | Author Public temperament for all territories (~30-50 entries) | 0.3 |
| 7 | Mandate-consumer audit: classify each Mandate read as Legitimacy / Popular Support / both | 0.3 |
| 8 | Stage 10 sim verification (lateral chain per integration plan §3.5) | 1-2 |
| **Total Phase B for PP-686** | | ~3 sessions |

### §6.3 Backward compatibility

- Mandate continues to work; existing consumers preserved via §4 derivation.
- Ethical Framework Modifiers table struck; behavior emerges from §3.7 triadic calculation. Per the C1 ±2 cap, no spurious regressions expected against current DA library.

### §6.4 Supersession

```yaml
- id: SUPERSESSION-PP686-001
  superseded: "params/bg/core.md §Ethical Framework Modifiers"
  superseder: "designs/provincial/faction_behavior_v30.md §3.7"
  date: 2026-05-01
  reason: "Philosophical-tradition vocabulary replaced with period-correct triadic decomposition; ±3 → ±2 cap"
```

---

## §7 Vetting Block (per PP-674 framework)

```yaml
vetting:
  class: A
  necessity: pass
  omega: pass
  mu: [Μ-α, Μ-β, Μ-δ]
  m_ratings:
    M-1: "+"
    M-2: "○"
    M-3: "+"
    M-4: "+"
    M-5: "+"
    M-6: "+"
    M-7: "✓"
    M-8: "✓"
    M-9: "+"
    M-10: "✓"
    M-11: "+"
  q: pass
```

Full vetting in `designs/audit/2026-04-30-architecture-session/03_PP-686_proposal.md` §5; sim validation in `05_PP-686_simulation_evaluation.md` and `06_PP-686_sim_v2_evaluation.md`.

---

## §8 Open Items Resolved per Integration Plan §3.4

| Decision | Resolution |
|---|---|
| **D1** Honor 13th Conviction | Yes — used in §3.3.1 sovereign + military-order + intelligence-diplomatic templates |
| **D3** Cascade-per-territory vs cascade-per-faction | Multi-root cascade allowance per §3.2.2 |
| **D4** Mission shift triggers | Enumerated as 4 triggers in §3.1 |
| 686-OQ3 α calibration | Defaults provided (0.4 base / -0.2..+0.4 seniority / -0.2..+0.2 institution); calibrate at Stage 10 |
| 686-OQ4 Public temperament typology | 5-temperament typology per §3.4.1 |
| 686-OQ5 Strictness function form | Per §3.6 (linear, clamped); Stage 10 calibration |
| 686-OQ6 Mandate retention | Transitional retention per §4 |
| 686-OQ7 α + β = 1 constraint | Kept |
| 686-OQ8 Mission shift triggers | Resolved by D4 enumeration |
| **D12** drift_coef = 0.6 | Per §3.2.4 |
| C1 Ob ±2 cap | §3.7 |
| C2 Drop strictness reward path | §3.6 |
| C3 drift_coef 0.6 | §3.2.4 |
| C4 Crisis-bypass | §3.2.5 |
| C5 β-fidelity gating | §3.4 outcome_polarity_gate |
| C6 Orphan NPC rule | §3.2.1 + §3.9 |
| C7 Self-Other formula | §3.4 (reads PP-684 §3.1) |
| C8 Structured-concentration NPCs | Reads PP-684 §4 |
| C9 Standing-weighted aggregate | §3.2.6 |
| C10 Cultural background templates | Reads PP-684 §5 |
| Audit P1-1 supervisor schema | §3.2.1 |
| Audit P1-2 aggregate function | §3.2.6 |
| Audit P1-3 DA category schema | §3.1 references PP-687 da_outcome subtypes |
| Audit P2-1 NPC behavior coupling | §3.8 dual-armature with role_acting flag |
| Audit P2-2 cascade-per-territory | §3.2.2 multi-root |
| Audit P2-3 Strain interaction | §3.4.2 |
| Audit P2-4 edge cases | §3.9 |
| Audit P2-5 mid-season leader change | §3.2.4 |

All audit P1+P2 items resolved.

---

**End spec. PROVISIONAL pending ratification.**
