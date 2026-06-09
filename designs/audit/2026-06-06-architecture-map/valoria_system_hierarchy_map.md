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

# Valoria — Hierarchical System Map
**Wrappers · Containers · Arrays · Keys — with confirmed resolver I/O**
Compiled 2026-06-06 from canon. Sources read this session listed per section. Not a commit; chat-side compilation. `[SELF-AUTHORED — bias risk: this is a structural reading; an independent reviewer should re-confirm the personal-attribute roster against params/core.md, which I named but did not fully read.]`

> **Reading convention.** Every Valoria system is a **wrapper** (a resolver) that pulls **inputs** (Stats / Derived Values / Tracks / Clocks / Keys), runs one of five **resolver archetypes**, and emits **outputs** (stat deltas, resource drains, track/clock moves, and — universally — **Keys**). The Key is the atomic record beneath everything; the four value buckets are the containers; vectors (conviction/axis) are the arrays.

---

## TIER 0 — THE SUBSTRATE (what everything is made of)

*Source: `key_substrate_v30.md` §1–§5, `key_type_registry_v30.md`, `derived_stats_v30.md` §1.*

### 0.1 The Key — universal atomic record
Every consequential event is a **Key**: a typed, validated, append-only record. No system keeps a private event channel; **every system emits Keys and consumes Keys.** Save state = initial conditions + Key log; replay = deterministic re-execution.

**Key schema (the universal wrapper):**

| Field | Type | Role |
|---|---|---|
| `id` | uuid | globally unique |
| `type` | string | registered type (see 0.2) |
| `source_actor` | actor_id \| null | proximate cause (null = environmental) |
| `emitted_at` | `{season_index, sub_step_index}` | total order |
| `causes[]` | array of key_id | provenance graph (0–3 typical) |
| `targets[]` | array | each: `{actor_id, role, impact_vector{4-axis}, stat_deltas{}}` |
| `scale_signature[]` | array | `[personal\|settlement\|territory\|peninsula]` |
| `symbolic_dimensions` | `{hierarchical, sacred, instrumental, traditional}` | event's position in axis-space |
| `visibility` | `{public, semi_public_observers[], private_observers[]}` | who can form Memory |
| `time_horizon` | immediate \| near \| far | |
| `permanence` | transient \| persistent \| indelible | decay behavior |
| `payload` | type-specific dict | |

`target.role` ∈ {subject, object, witness, beneficiary, bystander}. **`impact_vector`** and **`symbolic_dimensions`** are the two **4-axis arrays** that make Keys "vectorized."

### 0.2 Key Type Registry — 7 families
`scene_event` · `da_outcome` · `mechanical_event` · `state_transition` · `environmental` · `scene_outcome` · `system_meta` (≈30 subtypes total, e.g. `scene.contest_resolved`, `da.covert_betrayal`, `state.scar_acquired`, `env.peninsular_strain_shock`, `meta.knot_formed`, `state.belief_revised`). Adding a type = Class B extension; changing a type's required payload = supersession event.

### 0.3 The 4-Axis Conviction Space (the vector basis)
All symbolic effect projects onto four signed axes:

| Axis | + pole | − pole |
|---|---|---|
| **hierarchical** | rank-asserting, deferential to position | egalitarian, peer-leveling |
| **sacred** | numinous, oath-binding | secular, contractual |
| **instrumental** | ends-justify-means, calculative | principled, deontological |
| **traditional** | precedent-respecting, ancestral | reformist, generative |

*(A 5th axis is a permitted-but-deferred Class B extension: Community vs Identity collapse.)*

### 0.4 The Resolution Engine (dual-mode)
The dice engine is specified **two equivalent ways** (`derived_stats §1`, `params/core.md §Continuous Engine`):
- **Discrete** — d10 success-counting pool vs TN (legacy / TTRPG mode).
- **Continuous** — Normal-distribution sampling (videogame / Godot mode); enables fractional Ob, fractional TN, continuous degrees.

Both produce statistically equivalent outputs. **This is the core engine.** Five resolver archetypes sit on top (see Tier 3 header).

---

## TIER 1 — THE VALUE TAXONOMY (the containers)

*Source: `derived_stats_v30.md` §3, §14 (Decision-C 4-bucket taxonomy); `clock_registry_v30.md`.*

Two layers under the Keys: **base Stats** (capability) and **four buckets of derived state** (current condition).

### 1.0 Base Stats — the 1–7 capability layer
Small integers; feed dice pools. Change rarely (structural events), ±2/season cap.
- **Faction stats (6):** Mandate*, Influence, Wealth, Military, Intel, Stability. (*Mandate is **derived** — see Settlement layer.)
- **Settlement stats (per settlement):** Legitimacy (0–7), Popular Support (0–7), Prosperity (0–5), Defense (0–5), Order (0–5), Fort Level (0–4).
- **Personal attributes (the character 1–7 layer):** Endurance, Strength, Agility, Cognition, Charisma/Presence†, Focus, Recall, Spirit, Attunement, Bonds — plus **History** (universal skill additive). `[CONFIDENCE: medium — roster inferred from resolver/derived formulas; master list lives in params/core.md, not fully read this session.]` †name drift Charisma↔Presence, see Tier 4.

### 1.1 POOLS — dice quantities computed at action time (resolver INPUTS)

| Pool | Formula | Range | System |
|---|---|---|---|
| Combat | `max(5, History + 6)` — **Agility-independent, weapon-skill(History)-driven** (ED-901, 2026-06-04; old `(Agi×2)+H+3` STRUCK) | 6–12D | Combat |
| Argue | `(Primary×2) + History + 3 + style` | 5–18D | Social Contest |
| Thread | `(Spirit×2) + History + TPS`, min 5 | 5–17D+ | Threadwork |
| Fieldwork | `(Primary×2) + History + 3` | 5–17D | Investigation/Fieldwork |
| Knot | `(Bonds×2) + 3` | 5–17D | Knot Formation |
| Mass Combat (unit) | `min(Size, Command) + Command` | 2–14D | Mass Combat |
| Faction Domain | bare faction stat *(superseded as a roll — now d+σ, see 3.6)* | 1–7D | Faction action |

### 1.2 DERIVED VALUES — `Stat × multiplier`; resources that drain/refill

| Scale | Stat → Derived Value | Formula | Dir |
|---|---|---|---|
| Personal | Endurance → **Health** | `(End+6)×(MW+1)`, MW cap 3 (non-multiplier exception) | drains |
| Personal | End+Spirit → **Stamina** | `(3×End)+(2×Spirit)` (ratified S1) | drains |
| Personal | Charisma → **Composure** | ×3 †(drift: see Tier 4) | drains |
| Personal | Focus+Spirit → **Concentration** | `(3×Focus)+(2×Spirit)` (ED-902, 2026-06-04) | drains |
| Personal | Spirit → **Thread Fatigue** | ×5 (threshold) | counts up |
| Personal | Spirit → **Resolve/Inspiration cap** | ×1 | ceiling |
| Unit | Size → **TroopCount** | ×block_size | drains |
| Faction | Wealth → **Treasury** | ×100 | drains |
| Faction | Influence → **Reputation** | ×15 | drains |
| Faction | Stability → **Discipline** | ×10 | drains |
| Faction | Military → **Levies Available** | ×2 (ceiling) | ceiling |
| Faction | Mandate → **Legitimacy meter** | ×20 (displayed aggregate) | drains |
| Settlement | Prosperity → **Local Economy** | ×50 (0–250) | income |
| Settlement | Defense → **Garrison Strength** | ×20 + Fort×30 (0–250) | defense |
| Settlement | Order → **Public Order** | ×20 (0–100) | 0 = riots |

Multiplier tiers calibrated to interaction frequency (High ×10 / Medium ×5 / Low ×3 / Faction ×10–100); no master formula.

### 1.3 TRACKS — bounded counters (relationship / character / perceptual state)

| Track | Range | Owner |
|---|---|---|
| Disposition | −4 to +Bonds | per NPC (relational) |
| Piety Track | 0–10 | per character |
| Certainty | 0–5 (drifts ↓ with Thread exposure) | per character |
| Coherence | 0–10 (monotonic drain) | per character |
| Thread Sensitivity (TS) | 0–100 cap | per character |
| Renown / Standing | varies | per character |
| Torben/Elske Loyalty | 0–7 | faction-indexed |
| Löwenritter Autonomy | Loyal/Restless/Autonomous/Split | categorical |
| Accord | 0–3 | per territory |
| Piety Territory (PT) | 0–5 | per territory |
| Guild Favour / Church Attention Pool | 0–7 / 0–10 | per territory |
| Exposure / Cover(=Cog+History) | 0–10+ / 2–14 | per character·territory |

### 1.4 CLOCKS — world/scene/campaign progress, mostly monotonic

| Clock | Range | Start | Dir | Scope |
|---|---|---|---|---|
| Mending Stability (MS) | 0–100 | 72 | ↓ −1/yr | peninsula (cosmological) |
| Crown/Church Influence (CI) | 0–100 | 28 | ↑ | peninsula |
| Imperial/Institutional Pressure (IP) | 0–100 | 20 | ↑ | peninsula (Altonia) |
| Turmoil | 0–10 | 0 | ↑ | peninsula |
| Evidence Track | 0–3/5/8 | 0 | ↑ | per investigation |
| Saturation Counter | 0–N (resets/turn) | 0 | ↑ | per battle turn (Thread Ob escalator) |
| Coup Counter | 0–N | 0 | ↑ | Löwenritter |

---

## TIER 2 — CHARACTERS (the actor model)

*Source: `conviction_taxonomy_v30.md`, `conviction_axis_matrix_v30.md`, `key_substrate §2.5`, `complete_systems_reference §1`.*

An actor = base attributes (1.0) + derived resources/tracks (1.2–1.3) + an **ethical vector**:

### 2.1 The 13 Convictions (the ethical array)
`personal_convictions` = a **13-entry weighted vector** (Structured Concentration: 1–3 *primary* Convictions at weight 0.6–0.8 + a *cultural background* distribution at 0.2–0.4, normalized to 1.0):

`Faith · Authority · Order · Scholastic · Utility · Equity · Liberty · Precedent · Community · Identity · Warden · Virtue · Honor`

### 2.2 Conviction → Axis Matrix (13×4)
Each Conviction projects onto the 4 axes `[hierarchical, sacred, instrumental, traditional]`:

```
Faith     [+0.4, +0.9, -0.3, +0.6]    Precedent  [+0.3, +0.4, -0.4, +0.9]
Authority [+0.9, +0.2, +0.1, +0.4]    Community  [+0.0, +0.3, -0.2, +0.5]
Order     [+0.5, -0.1, +0.2, +0.4]    Identity   [+0.4, +0.2, +0.0, +0.6]
Scholastic[+0.1, +0.2, +0.3, -0.1]    Warden     [+0.5, +0.4, -0.1, +0.4]
Utility   [-0.1, -0.5, +0.9, -0.4]    Virtue     [+0.2, +0.4, -0.5, +0.3]
Equity    [-0.4, +0.2, -0.2, -0.2]    Honor      [+0.5, +0.4, -0.7, +0.8]
Liberty   [-0.7, -0.2, +0.1, -0.5]
```
**Derived array:** `armature_position[axis] = Σ_c personal_convictions[c] × MATRIX[c][axis]` (a 4-vector).

### 2.3 Self-Other Orientation (the scalar)
A single scalar in `[−1, +1]` per actor; **not** a Conviction. Captures *for whom* one acts (greed/ambition vs altruism). Modulates outcome attribution: `attributed_outcome = raw × (1 − 0.5·max(0, orient))`. Drifts under accumulated outcomes (κ≈0.03) → emergent Macbeth/fall-from-grace arcs.

### 2.4 The armature interpretation (how a character "reads" a Key)
`interpretation(npc, key) = Σ_axes armature_position[axis] × key.symbolic_dimensions[axis] × key.impact_vector[npc][axis]` → scalar driving Concern salience, Disposition shift, Memory salience. **This is the bridge from the Key substrate into character psychology.**

### 2.5 Named faction leaders (actor instances)
*Source: `complete_systems_reference §1.4–1.10`. Note: convictions below use the legacy 7-set vocabulary in that Rev-2 doc; current canon maps them onto the 13-set/4-axis model above.* Each carries: primary/secondary Conviction, Pressure-Point type (Evidence/Consequence/Authority/Loyalty), Thread Sensitivity, Certainty, Authority-Challenge Ob, and a 7-step **AI Priority Stack** (Survival → Existential → Framework-aligned → Institutional → Secondary → Reactive → Pass).

| NPC | Faction | Convictions | Pressure Pt | TS | Cert |
|---|---|---|---|---|---|
| King Almud Almqvist | Crown | Order / Reason(suppressed) | Consequence / Loyalty | 28 | 3 |
| Confessor Arne Himlensendt | Church | Faith / Order | Evidence / Authority | 0 | 5 |
| Duchess Inge Baralta | Hafenmark | Precedent / Faith | Evidence / Consequence | 0 | 5 |
| Duke Magnus Vaynard | Varfell | Reason / Autonomy | Consequence / Evidence | 14 | 3 |
| Grandmaster Lisbeth Ehrenwall | Löwenritter | Order / Autonomy | Consequence / Loyalty | 0–5 | 4 |
| Yrsa Vossen | Restoration | Equity / Continuity | Loyalty / Consequence | 0 | 2 |

Plus Ethical-Framework Ob modifiers per faction (−1 aligned / +1–2 contradictory). *(The §1.3 framework-modifier table is SUPERSEDED 2026-05-02 per PP-686 v2/ED-784; current effects route through the conviction/axis model.)*

---

## TIER 3 — THE SYSTEMS (resolvers as wrappers)

**Five resolver archetypes:** (A) **Dice pool** vs TN/Ob → degree ladder; (B) **d+σ** deterministic-stochastic (faction bare-stat); (C) **Deterministic accounting** (ledger formulas, no roll); (D) **Clock advance** (increment toward thresholds); (E) **Armature dot-product** (Key → interpretation). Each system below: **IN → resolver → OUT**, where OUT always includes emitted Keys.

### A. PERSONAL / SCENE SCALE

#### 3.1 Combat  — `combat_v30.md` (lore) + `combat_engine_v1/` (CANONICAL resolver, ED-900/901/902; config.py = live params)
- **IN:** Combat Pool `max(5, History+6)`; Strength (+damage); Endurance (Health, Stamina, Wounds, max-wounds=floor(End/2)+1); Agility (initiative, dodge, escape, disarm contests); weapon (Reach/Weight/Type axes → TN 5–8, plus three-regime mass/pob physics in engine_v1); armour DR; Stamina; Wounds.
- **Resolver:** (A) dice pool, TN 7 (½-step weapon TN conventions); crit at net ≥ **4** (PP-717). Damage = net hits + STR + weapon mod − DR. Group combat Fibonacci bonus (2v1 +1D … 8+ +5D cap).
- **OUT:** Wound accumulation (each −1D all pools), Stamina drain, Out-of-Breath (−2D at 0), Momentum, death; `scene.battle_concluded` / state Keys. `[CONFIDENCE: medium on whether Agility fully exits the offensive pool — engine_v1 internals not deep-read per "no hyper-granular" scope; config.py authoritative.]`

#### 3.2 Social Contest  — `social_contest_v30.md` + `params/contest.md`
- **IN:** Argue Pool `(Primary×2)+H+3+style`, Primary = Cognition (Expert adjudicator) / Charisma (Crowd) / Attunement (None); **Style** (1 of 4: Precedent, Suppression, Vision, Insinuation = Memory/Projection × Revealing/Obscuring); Composure (Cha+6 / ×3 †drift); Concentration; Piety Track (0–10, start 5); Institutional Mandate.
- **Resolver:** (A) dice pool + (D) Persuasion clock. Exchange loop: Appraise → Declare → Corroborate → Argue → Resolve (Clash/Reinforce/Cross/Tie). ±1 Cha ≈ 25–30% win; ±4 Cha = Total Victory in 2 exchanges.
- **OUT:** Persuasion-track movement, Composure/Concentration drain, Total Victory/Concede, Mandate −1 (Appease); `scene.contest_resolved` Key.

#### 3.3 Threadwork  — `threadwork_v30.md` + `params/threadwork.md`
- **IN:** Thread Pool `(Spirit×2)+H+TPS` min 5; Leap eligibility (TS ≥ 30); **Coherence** (0–10 depleting resource, the key constraint); three-axis Ob (Depth Fibonacci + Breadth + Distance); opponent TPS (opposing); Thread Fatigue.
- **Resolver:** (A) dice pool, TN 7/8/9. Operations: Weaving (cohere), Pulling (open), POP (temporal, TN8), Locking (TN8, chronic MS drift), Dissolution (TN8, Gap risk), Mending (Depth −1, **immune to opposition**), Community Weaving. N-way (3+) → automatic lattice collapse, all fail, Gap, MS −(2×practitioners).
- **OUT:** Coherence drain (war-scale 7-turn battle = 10→3; recovery +1/season or Knot anchoring), MS clock drift, Gap formation, Knot strain; `meta.thread_woven` / `meta.knot_*` / `meta.miraculous_event` Keys.

#### 3.4 Investigation / Fieldwork  — `investigation_systems_v30.md`
- **IN:** Fieldwork Pool `(Primary×2)+H+3`; Evidence Track threshold (Simple 3 / Complex 5 / Structural 8); Cover (=Cog+History, 2–14); Exposure (0–10+); Disposition/Bonds (Socializing); Intel (offensive quality / Spy Ob = floor(target Intel/2)+1).
- **Resolver:** (D) clock-driven (dice feed the Evidence clock; deterministic five-filter chain owns decisions) + (A) dice for individual actions (Examine, Interview, Research, Surveil +2 Exp, Thread-Read, Reconstruct; Stealth: Sneak/Hide/Lockpick/Pickpocket/Disguise/Sabotage).
- **OUT:** Evidence accumulation → case resolution, Exposure→Cover breach, Disposition shift (Neutral→Bonded = 6–8 actions / 3–4 seasons), Sincerity-Gate failures; `scene.investigation_resolved` Key.

#### 3.5 Knots  — `fieldwork_v30 §5.6a` (PP-632)
- **IN:** Bonds (requires ≥5 to form first Knot); Knot Pool `(Bonds×2)+3`; Knot Count cap = floor(Bonds/2)+1.
- **Resolver:** (A) dice pool — being-with, *not* a Thread op. Close 5 / Medium 2 / Loose 1.
- **OUT:** Disposition (Rupture → −4), Coherence −1 mandatory on loss, Knot-anchoring (+1 Coherence recovery); `meta.knot_formed` / `meta.knot_ruptured` Keys.

### B. STRATEGIC / FACTION SCALE

#### 3.6 Faction Layer  — `faction_layer_v30.md` / `faction_canon_v30.md` + d+σ resolver (ED-874)
- **IN:** the 6 faction stats; acting_stat vs difficulty (= contested target's stat, OR fixed action-difficulty `D=max(1,(O−1)·2)`); CI institutional weight (+⌊CI/20⌋, Church).
- **Resolver:** **(B) d+σ deterministic-stochastic** — `M = acting_stat − difficulty`; `P_success = clamp(0.5+0.1·M, 0.05, 0.90)`; bands → Overwhelming / Success / Partial / Failure. Slope 0.10/stat-point is **uniform across 1–7** (closes the small-pool √N non-uniformity). Governs all Domain Actions (Assert M=Inf−2, Reconstitute M=Inf−6, Suppress, Parliamentary Rebuttal, Treaty positioning/ratification, §1.4 Accounting Stability Check) + migrated Unique Actions (Royal Decree, Excommunication, Private Collection, Economic Leverage).
- **OUT:** 4-degree ladder → stat deltas, named hooks (Suppress Failure → Stability −1; Parliamentary Overwhelming → +1), Domain Echo (Success +1 / Overwhelming +2, cap ±2); `da.*` Keys.

#### 3.7 Settlement / Territory Layer  — `settlement_layer_v30.md` §1.8 (LPS-2e)
- **IN (containers):** per-settlement Legitimacy (0–7) + Popular Support (0–7); Settlement Weight `W_s = base(Type 1–3) + Prosperity(0–5) + FacilityTier(0–3)` (range 1–11); Order, Defense, Fort.
- **Resolver:** **(C) deterministic accounting (size-weighted saturating aggregate).** `q_s = 0.5·L_s + 0.5·PS_s`; `T = Σ_s W_s·(q_s/7)`; **`Mandate = clamp(round(7·T/(T+K)), 0, 7)`, K=6**. Saturating (diminishing returns) + bounded = the Lesson-5 damper on the legitimacy loop. Mean-reverting feedback Mandate→settlement L/PS (±1/season). Faction aggregate L/PS = Weight-weighted means. Treasury income = Σ settlement Prosperity ×10.
- **OUT:** faction Mandate (the headline derived stat), Accord (province-tier, =floor(mean settlement Order)), control state; province/duchy rollups. **Scale:** 35 settlements / 14 provinces / 3 duchies (+2 march targets = 37 in adjacency graph); 17 province-tier nodes T1–T17.

#### 3.8 Military Layer  — `military_layer_v30.md`
- **IN:** Military stat (muster quality gate); Levies Available (Military×2 ceiling); Stability; settlement control (muster base).
- **Resolver:** (C) deterministic muster + feeds 3.9.
- **OUT:** units (Type × Size), muster availability; couples into Mass Combat and back into faction Stability (the collapse→territory→muster cross-system loop).

#### 3.9 Mass Combat  — `mass_battle_v30.md` + `params/mass_combat.md`
- **IN:** Unit Health = Type Health × Size; Mass Combat Pool `min(Size, Command)+Command`; Formation (Line / Shield Wall −1D+2D / Wedge +2D−1D / Skirmish / Column / Reserve); Tactics (Envelopment, Feigned Retreat, Ambush, Concentration, Refused Flank, Hammer & Anvil); terrain; Saturation Counter (Thread Ob).
- **Resolver:** (A) dice per engagement, inside a **7-phase state machine**: Strategy → Volley → Manoeuvre → Thread → Engagement → Cascade → Reform. (Splitting dominates concentration +9% to +45%; countered by Narrow Pass / Feigned Retreat.)
- **OUT:** casualties (TroopCount drain via output-scaling), Army Morale composite, battle outcome → MS −1 (Campaign −2), IP +2/season, Political Stability +1/season, Accord 1 on conquest; `scene.battle_concluded` Key.

#### 3.10 CI Political  — `ci_political_v30.md`
- **IN:** Church Influence clock (0–100, start 28); faction Assert/Suppress actions; Stability; yearly cycle.
- **Resolver:** (D) clock advance (PP-402 passive advance, gated) + (B) seizure checks.
- **OUT:** CI milestone effects, CI-60 Territorial Seizure (M=Influence+⌊CI/15⌋ vs Ob 7−PT; Fail → Mandate −1), Parliament weight (+⌊CI/20⌋), coup enablement.

#### 3.11 Victory  — `victory_v30.md` + `params/bg/victory.md`
- **IN:** territory control count, Accord, Political Stability (all derived from lower layers).
- **Resolver:** (C) deterministic check.
- **OUT:** **Universal Peninsular Sovereignty** — 11/15 (all 15 w/ Accord ≥2, Pol. Stability ≤6) sustained 2 consecutive seasons = sole win (GD-1 struck all 8 faction-specific paths + Partition). Shared loss: Rupture (MS 0), Altonian Conquest (IP 100), Anarchy.

#### 3.12 Peninsular Strain  — `peninsular_strain_v30.md`
- **IN:** MS, IP clocks; battle/seizure events.
- **Resolver:** (D) clock-driven shock generator.
- **OUT:** Accord shifts, Turmoil, `env.peninsular_strain_shock` / `env.crisis` / `env.disaster` Keys (environmental, source_actor=null).

### C. CONNECTIVE TISSUE

#### 3.13 Scale Transitions  — `scale_transitions_v30.md`
- **IN:** scene scope/sufficiency, resolution degree, scale_signature of Keys.
- **Resolver:** (C) **Domain Echo** mapping — Sufficient Scope → OW ±2, Success ±1, Partial narrative, Failure −1 (cap ±2).
- **OUT:** cross-scale stat deltas; governs personal ↔ settlement ↔ territory ↔ peninsula handoff (the core UX flow). Cost tables shared with the d+σ resolver's degree ladder.

#### 3.14 Articulation Layer  — `articulation_layer_v30.md` (PP-688)
- **IN:** the Key stream + each observer's `armature_position`; significance function.
- **Resolver:** **(E) armature dot-product** + thresholded triggers. Three tiers: **Tier 1** protagonist UI lens (Concern queue, Memory salience, Bonds register, Chronicle search); **Tier 2** trigger ruleset (10 triggers, fire threshold 0.40 → cut scenes); **Tier 3** annual Chronicle generator.
- **OUT:** Concern queue, cut-scene rendering, annual chronicle prose, awareness updates; `state.belief_revised` / `meta.*` Keys. **This is the read-side dual of the Key substrate** — turns the event log into player-facing narrative.

#### 3.15 Campaign Architecture  — `campaign_architecture_v30.md`
- **IN:** season index, accounting triggers, all subsystem Keys.
- **Resolver:** (C) seasonal accounting loop (income/drain, stat-change windows, cascade resolution).
- **OUT:** `mechanical.season_change` / `mechanical.accounting` / `mechanical.cascade_resolution` Keys; drives the season clock everything else hangs off.

#### 3.16 NPC Behavior  — `npc_behavior_v30.md` + `npc_stance_triangles.md` + `npc_relational_graph_v30.md`
- **IN:** NPC conviction vector, armature interpretation of recent Keys, Wound count (0/1/≥2), Stability, AI Priority Stack.
- **Resolver:** (E)/(C) decision procedure — Institutional Filter → Conviction Filter → Decision Fork (Wound 0→Conviction, Wound 1→unaddressed, Wound ≥2→Crisis table, Stability ≤1→Autonomy). Non-named NPCs: Institutional Filter only.
- **OUT:** chosen Domain Action / scene behavior; Disposition/Concern updates; feeds back into 3.6.

#### 3.17 Clock Registry  — `clock_registry_v30.md`
- Not a resolver — the **single-source container manifest** for every clock/track/counter (enumerated in Tier 1.3–1.4). Each entry cites its authoritative rules doc.

---

## TIER 4 — CROSS-CUTTING NOTES, DRIFT & GAPS

**Resolver archetype ↔ mechanic-category mapping** (per `valoria-resolution-diagnostic`): continuous **Derived Values** degrade smoothly (Lessons 2/6); discrete **Clocks/Tracks** are legitimately linear/stepped (Lesson 4); **base Stats** are the small-pool problem source (Lessons 2/3). The d+σ resolver (3.6) exists specifically to fix the small-pool bare-stat-roll defect.

**Confirmed drifts (flagged, not resolved — Jordan's call):**
- `[DRIFT: Composure — Charisma×3 (derived_stats §14) vs Presence/Charisma+6 (clock_registry, contest). Name (Charisma↔Presence) and form (×3↔+6) both diverge.]`
- `[DRIFT: Stamina / Concentration — clock_registry (2026-04-26) shows End+1 / Focus+Recall; superseded by derived_stats §14 (ED-901/902, 2026-06-04): (3·End)+(2·Spi) / (3·Foc)+(2·Spi). Used the June values as current.]`
- `[DRIFT: index files — derived_stats_v30_index.md and settlement/threadwork index returns came back empty or routed; read source bodies directly. Index pipeline may be stale for these paths.]`
- `[INDEX DRIFT (from bootstrap): params/combat.md manifest path points at a missing file (deprecated 2026-06-04); 2 audit design docs registered to no concept.]`

**Gaps:**
- `[GAP: personal-attribute master roster — inferred from resolver/derived formulas (10 attributes + History); params/core.md is the authoritative home and was not fully read this session. Names Charisma vs Presence unresolved.]`
- `[GAP: combat_engine_v1 internal wrapper modules (wrapper/systems/core/config/combatant/geometry/tradition) not deep-read — out of "no hyper-granular" scope. config.py is the live Class-C parameter source.]`
- `[GAP: Intel → Intelligence Holdings derived value marked PENDING (derive-on-use); Settlement-scale derived values §9 marked PENDING in derived_stats.]`

**Authority status to watch:** faction Mandate is purely derived now (settlement→aggregate); the 6th faction stat **Intel** was restored (ED-787) — some clock_registry/board-game entries still flag it STRUCK (stale).
