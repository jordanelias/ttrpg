<!-- [PROVISIONAL: 2026-05-07 — Faction canon consolidation; supersedes piecemeal lookup across faction_layer_v30 / faction_behavior_v30 / faction_state_authoring_v30 / faction_politics_v30 / factions_personal_v30 / params/factions/* for per-faction texture. Substrate (PP-684 13-Conviction taxonomy + PP-685 migration roster + PP-686 v2 4-component model) remains in source files; this consolidation references, does not duplicate.] -->
<!-- STATUS: PROVISIONAL — pending Jordan ratification. Source files remain canonical until ratification commits. -->
<!-- AUTHORITY: consolidates PP-686 v2 (faction_behavior_v30) + Phase B Stage 5 (faction_state_authoring_v30) + faction-doctrine canon (faction_layer_v30 §1.5) + factions_personal_v30 §8 + stats_1_7_scale + atoms-pending faction-balance findings. -->

# Valoria — Faction Canon (Consolidated)
## Status: CANONICAL
## Status: PROVISIONAL — pending ratification.

> **⚙️ Implementation note (ED-FA-0004, 2026-07-07):** the `sim/` oracle (`sim/autoload/game_state.py` Faction = {L, Sta, W, I, Mil}) does NOT yet implement the LPS-2e 6-stat / per-settlement L-PS split this sheet authorizes — no Mandate/PS/Treasury engine, no `da.*` Keys. This DOC is correct canon; the ORACLE lags it. Full LPS-1 sim implementation is Stratum-B work — do not treat `sim/` as canon-conformant until then.
## Date: 2026-05-07
## Companion: `designs/npcs/character_canon_v30.md` (per-NPC sheets) — pending.
## Substrate: `designs/personal/conviction_taxonomy_v30.md` (PP-684 13-Conviction) + `designs/personal/conviction_axis_matrix_v30.md` — both files remain canonical and are referenced, not duplicated, here.

---

# PART A — FRAMEWORK

## §1 Status, Scope, and Supersession

This document consolidates per-faction texture canon scattered across:

- `designs/provincial/faction_layer_v30.md` (architecture: stability triggers, treaties, parliament, occupation, faction doctrine notes §1.5)
- `designs/provincial/faction_behavior_v30.md` (PP-686 v2: Mission / Cascade / Public Expectation / Legitimacy + Popular Support — the 4-component canonical model)
- `designs/provincial/faction_state_authoring_v30.md` (PP-686 Phase B Stage 5: per-faction Mission specs)
- `designs/provincial/faction_politics_v30.md` (rank ladders, Inner Circle Named NPCs, caste integration)
- `designs/provincial/faction_succession_split_v30.md` (succession + split mechanics)
- `designs/provincial/factions_personal_v30.md` (TTRPG-mode faction specs §8.1–§8.12; substrate-postures T-15a/T-15b/T-15c)
- `params/factions/stats_1_7_scale.md` (post-ED-787; per LPS-2e the faction lineup is 6-stat (Mandate headline) — L/PS are per-settlement (settlement_layer §1.8), NOT faction stats)
- `params/factions/npc_stance_triangles.md` (Framework Drift table — superseded labels retained as descriptive tags)
- `params/factions/riskbreakers_identity.md` (sub-org identity sample)
- `params/bg/faction_actions.md` (BG faction action lists)

**What this consolidation does:**
- Pulls per-faction texture into a single sheet per faction (Part B).
- Lifts the Mission specs from `faction_state_authoring_v30` verbatim (single source of truth retained — this file references).
- Surfaces every conflict between sources rather than silently resolving (per Decision Log §12).
- Marks every stat `PROVISIONAL` with a flagged design-issue note — see §5.

**What this consolidation does NOT do:**
- Does not retcon Mission text. The Stage 5 author's values are canonical.
- Does not silently fix the 6-stat (`factions_personal §8.1`) vs 7-stat (`stats_1_7_scale` post-ED-787) schema conflict at source. Surfaces both; [RESOLVED by LPS-2e: 6-stat canonical; L/PS per-settlement, not faction stats] formerly used 7-stat as primary per most-recent-canonical, with Mandate shown as derived. Source-file propagation is a separate commit cycle.
- Does not author missing substrate-postures (Crown / Church / Varfell / Guilds — all four are flagged `[GAP — Phase B]`).
- Does not commit. This file lands as artifact for Jordan review.

**Supersession (informational — recorded in `canon/supersession_register.yaml`):**
- `params/bg/core.md §Ethical Framework Modifiers` → SUPERSEDED by `faction_behavior_v30 §3.7` (triadic Ob calc) per SUPERSESSION-PP686-001.
- `params/factions/stats_1_7_scale.md §Ethical Framework Ob Modifiers` → SUPERSEDED 2026-05-02 per SUPERSESSION-PP686-002.
- Ethical-framework labels (Virtue / Faith / Categorical Imperative / Utility-driven Pragmatism / Equity Social Contract / Moral Relativism / Martial Honour / Administrative Proceduralism) — all formally retired as mechanical anchors. Retained per-faction below as **descriptive disposition tags** for prose-writer continuity, with `[SUPERSEDED — see PP-686 §3.7]` notes inline. Mechanical Ob modifiers come from PP-686 §3.7 triadic calculation, not these labels.

---

## §2 How to Read a Faction Sheet

Each faction in Part B follows this schema. The schema parallels the per-NPC sheet schema in `character_canon_v30.md` (pending) — convictions are the shared substrate; what differs is what gets aggregated and how the populace dimension layers in.

```
## <Faction Name> — <Role>
[Player-eligibility · Mode coverage · Status]

Identity            — full name, role, archetype, leader, succession line
Mission             — text · primary_objective · beneficiary · aligned/contradicted DA categories (PP-686 v2)
Expected Convictions— per role template (PP-686 §3.3.1) — what the populace expects from this role
Cultural Identity   — how this faction reads in-world; period-realistic anchoring
Institutional Beliefs — first-person doctrinal claims (faction-scale voice anchors for prose-writer)
Strategic Goals     — Mission goal + situational layer + win-condition path
Inspiration         — historical_parallel + in_character_aspiration  ← lifted from scattered prose into structured field
Substrate-Posture   — T-15 series where authored; [GAP — Phase B] for unauthored
Ethical Disposition — descriptive label (legacy framework, [SUPERSEDED] tag) + Ob modifier intent
Stats               — L / PS / I / W / Mil / Int / Sta with TTRPG vs BG values where they differ. PROVISIONAL.
Tactic / Unique Action — single signature mechanic with degree table
Priority Tree       — BG behavioral AI summary (links to npc_behavior_v30 §8)
Doctrine Notes      — published §1.5 material where present; [GAP] otherwise
Stability Profile   — faction-specific triggers and recovery patterns
Arc Trajectories    — faction-level arc state machine
Legitimacy / PS Dynamics — what builds and erodes per faction
Sub-Organizations   — Inner Circle, Riskbreakers, Inquisitors, etc.
Member NPCs         — pointer to character_canon entries (not duplicated)
Foil Dynamics       — cross-faction structural relationships
Provenance          — source files this entry consolidates from
```

---

## §3 The PP-686 v2 Four-Component Model

A faction's behavior is determined by four interacting components. This replaces the legacy Ethical Framework Modifier system entirely.

### §3.1 Mission

The faction's stated telos. Authored at scenario init; evolves under defined triggers.

```yaml
mission:
  text: <short string>                  # public-facing statement
  primary_objective: <victory_track | DA_category>
  beneficiary: <actor_or_population_ref>
  aligned_categories: [<da_subtype>, ...]      # -1 Ob bonus
  contradicted_categories: [<da_subtype>, ...] # +1 Ob penalty
  authored_at: <date>
  prior_mission: <mission | null>
```

DA categories reference PP-687 `da_outcome` subtypes: `da.public_governance`, `da.covert_betrayal`, `da.diplomatic_alliance`, `da.antinomian_action`, `da.economic_intervention`.

**Mission-shift triggers** (PP-686 §3.1):
1. Victory-track milestone passes/fails.
2. Leader replacement under exceptional circumstances (`state.succession` with mode in `[contested, emergency, imposed]`).
3. ≥4 consecutive seasons of Mission-contradicting outcomes.
4. Authored event in scenario.

A shift emits `mechanical.mission_shift` Key (PP-687 §4); existing alignment interpretations recompute against the new Mission.

### §3.2 Cascade

How the faction conducts itself. **Derived** from leadership Convictions through hierarchical α-weighted blending.

```
effective_convictions(npc) =
    α(npc) × personal_convictions(npc)
  + (1 − α(npc)) × effective_convictions(supervisor(npc))

aggregate_effective_convictions(faction) = normalize(
    Σ over npc in faction:
        npc.standing × effective_convictions(npc)
)
```

α defaults: `α_base = 0.4`; `α_seniority` ranges -0.2 to +0.4 (Standing 1 → 7); `α_institution` ranges -0.2 to +0.2 per faction culture (Hafenmark -0.2 rigid; Crown 0; Restoration +0.1; Löwenritter -0.1).

**Multi-root cascade** (PP-686 §3.2.2): a faction may have multiple parallel cascade roots, one per institutional sub-hierarchy. Crown has secular/military/household; Church has Four-Cardinal; Varfell has Jarl Confederacy. Default per Phase B Stage 5: single-root; multi-root upgrade deferred to Stage 10 sim observation.

### §3.3 Public Expectation

What the populace expects from the faction's role. **Derived** from role + Mission consistency.

```
expected_convictions(faction) = role_template(faction.role)
```

Role templates per §4 below.

**Cascade Fidelity** (how well the faction's actual conduct matches role expectation):

```
cascade_fidelity(faction) = cosine_similarity(
    aggregate_effective_convictions(faction),
    expected_convictions(faction.role)
)
```

Range `[-1, +1]`. 1 = perfect role fidelity; 0 = orthogonal; -1 = inverse.

### §3.4 Legitimacy + Popular Support

> **[REVISED by LPS-1 → LPS-2e (settlement_layer_v30 §1.8), Jordan ruling 2026-05-30 — resolves the §5.2 design-issue below.]** Legitimacy and Popular Support are **per-settlement** values (0–7 each), **not** faction scalars. Faction **Mandate is the aggregate** (round(mean over controlled territories of 0.5L+0.5PS)); the faction retains derived **aggregate_Legitimacy / aggregate_Popular_Support** (territory means) for consumers (e.g. strictness). See settlement_layer §1.8.

Two per-settlement scalars `[0, 7]` tracking populace relation **in a settlement** (Mandate aggregates them per §5 / settlement_layer §1.8).

- **Legitimacy** (slow-moving): populace acceptance. Integrates over many seasons via `λ_continuity`, `λ_procedural`, `λ_expectation`, `λ_violation`.
- **Popular Support** (faster-moving): active populace backing. Integrates Mission outcomes + Cascade Fidelity + random shocks per Public Temperament.

**Public Temperament** (per-territory, 5 types):

| Temperament | α (outcomes) | β (conduct) | Period example |
|---|---|---|---|
| pragmatic | 0.7 | 0.3 | Florentine merchant class |
| traditional | 0.3 | 0.7 | rural devout populace |
| balanced | 0.5 | 0.5 | mixed urban populace |
| principled | 0.2 | 0.8 | reformist enclaves |
| outcomes-only | 0.9 | 0.1 | hardship populations under direct threat |

Faction's effective temperament = population-weighted average across faction's territories. Strain shifts territories toward `outcomes-only`.

---

## §4 Role Templates and Expected Convictions

Per PP-686 §3.3.1. Templates use the 13-Conviction taxonomy from PP-684 §2.

| Role | Expected Convictions (weighted) | Faction (player-eligible) |
|---|---|---|
| sovereign | Virtue 0.30, Authority 0.30, Honor 0.20, Faith 0.10, Warden 0.10 | **Crown** |
| ecclesiastical | Faith 0.40, Authority 0.20, Scholastic 0.20, Precedent 0.10, Virtue 0.10 | **Church of Solmund** |
| mercantile-procedural | Order 0.35, Utility 0.25, Scholastic 0.20, Liberty 0.10, Equity 0.10 | **Hafenmark** |
| intelligence-diplomatic | Scholastic 0.30, Utility 0.30, Authority 0.20, Precedent 0.10, Identity 0.10 | (Varfell candidate; see below) |
| reformist | Equity 0.30, Liberty 0.25, Community 0.20, Virtue 0.15, Scholastic 0.10 | **Restoration Movement** |
| military-order | Honor 0.30, Authority 0.25, Virtue 0.15, Identity 0.15, Order 0.15 | **Varfell**, **Löwenritter** |

**Note on Varfell role assignment.** `faction_state_authoring_v30 §5` assigns Varfell to `military-order` (matches the Vaynard "cunning + pride" doctrine, `faction_layer §1.5`). The `intelligence-diplomatic` template is a candidate — Varfell's Talleyrand-style diplomatic stratagem could justify it — but Vaynard expansion is "purely military per Jordan decision 2026-04-19" (faction_layer §1.5), so the military-order role is correct. Both Varfell and Löwenritter use `military-order` template; their differentiation comes from Mission, leader Convictions, and stat profile, not role template.

**Cascade fidelity between two `military-order` factions** is computed against the same expected_convictions vector. Their aggregate_effective_convictions diverge based on leader+member personal_convictions (Vaynard's `Authority + Utility` profile vs Ehrenwall's canonical `Order + Autonomy` legacy mapping).

---

## §5 Stat Lineup

**[PROVISIONAL — every stat in Part B is flagged PROVISIONAL.]**

### §5.1 The faction stat lineup — REVISED by LPS-1 (Jordan ruling 2026-05-30; resolves §5.2)

> **The faction stat lineup is 6-stat: Mandate (headline, derived) / Influence / Wealth / Military / Intel / Stability.** Legitimacy and Popular Support are **per-settlement** values (0–7 each, settlement_layer §1.8), **not** faction stats — the prior "7-stat" faction lineup put them at the wrong level (the §5.2 design-issue, now resolved). The two rows below are retained as the per-territory value definitions.

| Stat | Range | Renaissance analogue |
|---|---|---|
| **Legitimacy** (per-settlement, settlement_layer §1.8) | 0–7 | Populace acceptance — papal bulls, dynastic claims, constitutional authority |
| **Popular Support** (per-settlement, settlement_layer §1.8) | 0–7 | Active populace backing — Florentine signoria support, urban guild mobilization |
| **Influence** | 1–7 | Diplomatic reach — Medici banking diplomacy, Venetian diplomatic service |
| **Wealth** | 1–7 | Economic resources — trade revenue, mercenary funding, treasury |
| **Military** | 1–7 | Armed forces — standing armies, fortification networks |
| **Intel** | 1–7 | Institutional intelligence — Venice's Council of Ten, papal nuncio network |
| **Stability** | 0–7 | Internal cohesion — Pazzi conspiracy resistance, Visconti-Sforza succession discipline |

Mandate is **the faction headline stat, derived by aggregation** (LPS-1; no longer "transitional"):

```
Mandate(faction) = clamp( round( 7 · T / (T + K) ), 0, 7 ),   T = Σ over controlled settlements of W_s·(0.5 × Legitimacy_s + 0.5 × Popular_Support_s)/7,   K = 6   (size-weighted, saturating; Settlement Weight W and full spec authoritative in settlement_layer §1.8, LPS-2e)
```

### §5.2 [DESIGN-ISSUE — flagged 2026-05-07 by Jordan; RESOLVED 2026-05-30 by LPS-1]

> **[RESOLVED by LPS-1 → LPS-2e (settlement_layer_v30 §1.8), Jordan ruling 2026-05-30.]** L and PS are **per-settlement** (0–7); faction **Mandate is the size-weighted saturating aggregate** of controlled settlements' L/PS (Weight W=base(Type)+Prosperity+FacilityTier; Mandate=clamp(round(7·T/(T+K))), K=6; full spec §1.8). The "perfect L/PS, one province" concern is resolved: a small holding gives modest total weighted legitimacy → modest Mandate; a large loyal holding → high Mandate.

> **A faction could have perfect Legitimacy and Popular Support but hold only one province, and the system would compute Mandate normally — but the underlying mechanic doesn't capture territorial scope.**

PP-686 v2 §3.4–§3.5 defines L and PS as 0–7 scalars without specifying populace scope:
- §3.4: "scalar `[0, 7]` tracking active populace backing" — does not say *which* populace.
- §3.5: "scalar `[0, 7]` tracking populace acceptance" — does not say *which* populace.
- §3.4.1 says "Faction effective temperament = population-weighted average across faction's territories" — implying territory-weighted aggregation, but leaves L/PS scope unspecified.

Two readings, both broken:
1. **Scope-blind L/PS** (each scalar reflects intra-faction support density): a one-province faction with strong internal backing reads Mandate=7, equal to a peninsula-spanning faction with the same density. Action resolution doesn't reflect that the small faction's political mass is bounded by territorial reach.
2. **Peninsula-aggregate L/PS** (each scalar reflects faction's share of peninsula-wide acceptance): a one-province faction with perfect intra-province support computes low absolute L+PS because it can only command ~its territorial fraction of the total populace. Mandate computes low; Domain Actions become prone to fail despite the faction being internally cohesive.

Neither resolves cleanly. The mechanic needs either:
- (a) Explicit scope flag on L and PS (intra-faction vs peninsula-aggregate), with separate effects.
- (b) Mandate derivation that includes a territorial-extent multiplier or scope-modifier.
- (c) Two-tier Mandate: "internal Mandate" (governs within-faction action capacity) vs "external Mandate" (governs peninsula-scale political weight).

**Stat values in Part B are PROVISIONAL pending design resolution of this issue.** Per-faction stat tables are reproduced from current canonical sources (`stats_1_7_scale.md` Starting Stats table) but should not be treated as load-bearing until scope is resolved.

### §5.3 Stat schema conflict (RESOLVED 2026-05-30 by LPS-1 / Jordan ruling)

`factions_personal_v30 §8.1` documents a 6-stat faction sheet (Mandate / Influence / Wealth / Military / Intel / Stability). `params/factions/stats_1_7_scale.md` (post-ED-787; 7-stat header superseded — L/PS per-settlement per LPS-2e, lineup is 6-stat) documented a 7-stat lineup adding faction-level Legitimacy + Popular Support. **Jordan ruling (2026-05-30): the 6-stat faction lineup is correct** — L and PS are per-territory, not faction stats; Mandate (headline) aggregates them (settlement_layer §1.8). The "7-stat" faction lineup was the defect. Propagation: this consolidation + LPS-2 (stats_1_7_scale header + faction_behavior + faction_state_authoring corrected this session).

---

## §6 Public Temperament (per-territory)

Per PP-686 §3.4.1 — see §3.4 above for the table. Per-faction temperament is computed at Accounting from per-territory current temperaments. Strain shocks bias affected territories toward `outcomes-only`.

Per-territory authoring is Phase B Stage 6 work (`faction_behavior_v30 §6.2`), pending. This consolidation does not author per-territory temperament; faction sheets reference temperament intent qualitatively where doctrine notes provide guidance (e.g., Hafenmark's burgher class is `pragmatic`; Solmund Alpine populations are `traditional`).

---

## §7 The Nine Political Axes (qualitative positioning)

Per `params/factions/stats_1_7_scale.md` and `factions_personal_v30 §8.1`. Not tracked numerically. Used for: war justification (casus belli), Domain Echo content framing, faction-foil structural analysis.

| Axis | Pole A | Pole B | Primary opposition |
|---|---|---|---|
| 1. Sovereignty | Crown authority | Church authority | Crown vs Church |
| 2. Knowledge | Thread truth accessible | Thread truth suppressed | Varfell / Restoration vs Church |
| 3. Legitimacy | Constitutional monarchy | Theocratic governance | Crown / Hafenmark vs Church |
| 4. Cultural identity | Einhir recovery | Colonial settlement | Restoration vs Crown / Church |
| 5. Economic control | Guild autonomy | State / Church taxation | Guilds vs Crown / Church |
| 6. Military authority | Ducal / Crown command | Templar independence | Hafenmark / Crown vs Church |
| 7. Information | Transparency | Secrecy | Restoration vs Varfell |
| 8. External threat | Accommodation of Altonia | Resistance | Crown (split) vs all |
| 9. Ontological | The world is what it appears | The world is more | Church vs practitioners |

Per-faction position on each axis appears in faction sheets under **Foil Dynamics**.

---

## §8 Stability Mechanics

Per `faction_layer_v30 §1`. Five canonical triggers, recovery paths, collapse procedure.

### §8.1 Stability triggers (5)

1. **Territorial Occupation or Loss** (§1.2 Trigger 1): own territory occupied −1; control lost −1 additional; capital lost −2/−3.
2. **Unfavourable Treaty Terms** (Trigger 2): Capitulation −3 / Major cession −2 / Minor cession −1 / Tributary −1/year.
3. **Antagonistic Parliamentary Vote** (Trigger 3): Censure −1; Blockade −1 once; Combined Embargo+Blockade −1/season; Outlawry −2.
4. **Major Subterfuge** (Trigger 4): Sabotage −1; Assassination −2 + Mandate −1.
5. **Failed Military Engagement: Significant Losses** (Trigger 5): three-condition gate (committed force ≥4 + clear defeat + severity threshold) → −1 to −4 max.

### §8.2 Recovery paths

- Mutual peace treaty (both ≥ Stability 2): +1.
- Recapture own occupied territory (Success): +1.
- Rebuttal Overwhelming (Parliament): +1.
- Institutional consolidation (no Trigger 1–5 fired this season): +1 + Accord +1 in one territory.
- Church Absolution (Church unique action): +1 to target.
- Löwenritter public endorsement: +1 to target.

Seasonal cap: ±2 Stability per season from any combination.

### §8.3 Collapse (Stability = 0 at Accounting)

Per `faction_layer_v30 §1.5`. Six-step procedure: Mandate → 0 immediate; territories → Uncontrolled; named officers → Independent; PC affiliated to faction loses Standing-derived bonuses; Parliamentary seat lost; victory conditions close.

**Collapse immunity** (one-time per faction per campaign): Stability 1 facing reduction to 0 may invoke Survival Exception — Stability stays 1, Mandate −1, one territory becomes Contested.

---

## §9 Tactic / Unique Action Overview

Each player faction has one signature mechanic. Detailed degree tables in faction sheets.

| Faction | Unique Action | Roll | Resource cost |
|---|---|---|---|
| Crown | Royal Decree | d+σ resolver: M = Mandate − 2 | 1/season; +1 Ob/season consecutive |  <!-- LPS-2e: L per-settlement, not a faction roll stat; Mandate is the faction stat (matches factions_personal §8.2). Method = sim-deferred resolver migration. -->
| Church | Excommunication | d+σ resolver: M = Mandate − target Mandate (leader) / Mandate − 2 (non-leader) | Requires Church Mandate ≥ 3 |  <!-- LPS-1: L→Mandate; 'faction L' effects reconcile to Mandate / per-territory L per settlement_layer §1.8 -->
| Church | CI 60 Territorial Seizure | Influence + floor(CI/15) vs Ob = 7 − PT | Per-territory; CI ≥ 60 trigger; AUTHORITATIVE per faction_layer §2.7; Failure → Mandate −1 (FCN-SEIZURE-DRIFT reconciled; was stale L-based) |
| Hafenmark | Sovereign Authority Doctrine | Mandate vs Ob 4 | 1/campaign arc |  <!-- LPS-1: L→Mandate (matches factions_personal §8.4) -->
| Varfell | The Private Collection | d+σ resolver: M = Intel − 2 | 1/season; long-term TS cost |
| Guilds | Economic Leverage | d+σ resolver: M = Wealth − target Wealth | Requires Guild Favour ≥ 5 in territory |
| Restoration | Community Weaving (PP-616 canonical) | (Spirit × 2) + History + TPS pool | Thread operation, not DA; PS ≥ 1 prerequisite = COMMUNITY-level PS in a Presence locality (RM is territoryless; per faction_state_authoring §6 / PP-460 its L/PS are community-scoped — settlement_layer §1.8) |
| Löwenritter | Martial Law / Coup Trigger | No roll — Graduated Autonomy stage 4 | Triggered by Crown failure conditions |

---

## §10 Sub-Organization Layers

Each major faction has one or more sub-ladders. Per `faction_politics_v30 PART 2`. These are Standing tracks parallel to the main faction Standing ladder.

| Faction | Sub-organizations |
|---|---|
| Crown | Inner Circle (5 named NPCs per `npc_behavior §2.15`); Specialty Branches at Standing 3 |
| Church | Four-Cardinal structure (Justice / Temperance / Fortitude / Prudence); Inquisitor sub-ladder; Templar sub-ladder |
| Hafenmark | Inner Council (2 named per `npc_behavior §2.16`); Parliamentary Committees (§7.2); Guild sub-ladder (Hafenmark-integrated track) |
| Varfell | Jarl Council (2 named per `npc_behavior §2.17`); Senior Jarls of Highlands / Skald-Chiefs |
| Löwenritter | Knight Ladder (§2.1); Riskbreaker covert sub-ladder (§2.2); Shadow Renown + Deniability Debt mechanics |
| Restoration | Loose collective; no formal hierarchy; Yrsa Vossen + Aldric Hann as visible leadership |

Ministry of the Peninsula carries its own sub-ladder (Registrar → archivist → settlement clerk).

---

## §11 Partial Sheet Handling

Three factions operate on partial sheets — they intentionally lack stats other factions have:

**Restoration Movement:** No Mandate / No Military / No Wealth. Operates via Influence / Stability / Intel + Presence markers + Community Weaving. Per PP-460. PP-686 schema partially applies — Mission and Cascade are meaningful; PE+L+PS scoped to community level rather than peninsula-wide.

**Löwenritter:** No Mandate / No Wealth pre-coup; embedded under Crown until Graduated Autonomy track reaches stage 4. Post-coup: Löwenritter becomes playable faction with own Mandate/Wealth from Crown's reduced stats.

**Ministry of the Peninsula:** Influence + Stability only. No Mandate / no Military / no Wealth / no Intel. Treated as institutional infrastructure, not a faction. Operates as Throughline T4 actor.

---

## §12 Decision Log

Decisions made in producing this consolidation. Surfaced rather than silently resolved.

| # | Decision | Resolution |
|---|---|---|
| **D1** | Convictions when sources conflict (faction role template vs leader cascade) | Use PP-686 §3.3.1 role template as `expected_convictions`; show leader's `personal_convictions` from migration roster as cascade input. Both legitimate; serve different roles. |
| **D2** | Ethical Framework labels (SUPERSEDED by PP-686 §3.7) | Retain as **descriptive disposition tag** with `[SUPERSEDED → mechanical role replaced by PP-686 §3.7 triadic Ob calc]` note. Don't silently re-derive Ob modifiers. |
| **D3** | Stat schema conflict (6-stat factions_personal vs 7-stat stats_1_7_scale) | 6-stat canonical post-LPS-2e — L/PS per-settlement (settlement_layer §1.8), not faction stats. Mandate shown derived. Source-file propagation deferred. |
| **D4** | Substrate-Posture gaps for Crown / Church / Varfell / Guilds | Mark `[GAP — Phase B authoring]`. Do not invent. Three factions (Hafenmark / Restoration / Löwenritter) have authored T-15 postures; rest pending per ED-717. |
| **D5** | Inspirations field — lift scattered Venice/Florence/Lohengramm/Talleyrand prose into structured `inspiration` field | Two facets per faction: `historical_parallel` (period-realistic anchor) + `in_character_aspiration` (in-fiction aim). Where no parallel is documented, mark `[GAP]`. |
| **D6** | Niflhel — STRUCK across all canonical files (CR-STRIKE-2026-04-19) | Preserve as `## §Historical — Niflhel (DISSOLVED)` marker section pointing to settlement-layer §4.7-4.9 redirect. No full sheet. |
| **D7** | [DESIGN-ISSUE] L+PS scope (§5.2 Jordan flag 2026-05-07) | All stats marked PROVISIONAL throughout Part B. No silent fix. Issue documented for design resolution. |

---

# PART B — FACTION SHEETS

---

## Crown — Sovereign

**Player-eligible** (BG mode 2–4 player roster) · **Mode coverage:** TTRPG / BG / Hybrid · **Status:** PROVISIONAL

### Identity

- **Full name:** The Valorian Crown (Almqvist dynasty)
- **Role:** sovereign (PP-686 §3.3.1)
- **Archetype:** deed-monarchy whose authority derives from continuous demonstrated competence, not from divine sanction mediated through Church
- **Leader:** King Almud Almqvist (canonical Crown Captain per sim continuity §1.2)
- **Heir apparent:** Prince Torben Almqvist (Conviction emergence window Seasons 1–8; ED-618)
- **Princess:** Elske Almqvist (married to Doux Alexios Laskaris of Altonia — see Altonian-relations branch)
- **Royal Assassination Fuse** (sub-roll target on Royal Crisis Tension Card): Torben (Arc E Bereaved Father) / Almud (Arc F Eliminated → Lenneth Widow Regent) / Lenneth (Arc D The Avenger)
- **Capital:** T1 Valorsplatz (also T2 Kronmark, T5 Feldmark, T6 Stillhelm, T14 Ehrenfeld held)

### Mission (per `faction_state_authoring_v30 §2`, verbatim)

```yaml
text: "Restore and maintain Peninsular Sovereignty under the Almqvist dynasty"
primary_objective: victory.peninsular_sovereignty
beneficiary: populace_of_valoria
aligned_categories:
  - da.public_governance              # public administration is core role
  - da.diplomatic_alliance            # treaties advance sovereignty
contradicted_categories:
  - da.covert_betrayal                # the Almqvist code is honor-bound
  - da.antinomian_action              # contradicts sovereign role
prior_mission: null
```

### Expected Convictions (sovereign role template, PP-686 §3.3.1)

`Virtue 0.30, Authority 0.30, Honor 0.20, Faith 0.10, Warden 0.10`

Cascade Fidelity computed as cosine similarity between this and the aggregate of leader + Inner Circle effective_convictions (Almud per migration roster: `Virtue 0.45 + Authority 0.30, valorian_court template, self_other -0.10`).

### Cultural Identity

The deed-monarchy: Crown legitimacy is the continuously demonstrated act of governing well, not divine right or pure heredity. The first Almqvist earned the throne through a war of unification; each successor must continually re-earn it through demonstrated competence in defense, justice, and stewardship. Failure to perform is failure of legitimacy, not a temporary lapse. This is the structural source of Almud's central tension: every season he must choose the least-bad option, because his position is assailed from every axis simultaneously, and the deed-logic requires he keep the throne by performing visibly across all of them.

### Institutional Beliefs (first-person voice anchors)

1. "The realm is what we hold together against all who would take it."
2. "Authority that is not earned this season is not authority next season."
3. "We govern by what we do, not by what we are."

### Strategic Goals

- **Standing Mission:** Peninsular Sovereignty — the Almqvist line continues as the recognized throne of the peninsula's territories.
- **Situational (current scenario):** Manage Crown structural fragility per `faction_layer §1.5`. Press multiple competing pressures (Altonian threat, Schoenland mediation, Restoration cultural infiltration in T2/T5, Church Sovereignty axis, Hafenmark commercial competition, Varfell's Vaynard ambition, Löwenritter graduated autonomy) without losing on any one.
- **Win path:** `victory.peninsular_sovereignty` per `victory_v30 §3.1` — Crown Treaty mechanic + multi-territory consolidation + capital retention.

### Inspiration

- **Historical parallel:** Wars of the Roses Lancaster / York deed-claim dynamic; Avignon papacy as competing-legitimacy model; Investiture Contest as Crown-Church axis precedent. The Crown's fragility-from-perceived-strength echoes the late-medieval English crown — the most resourced power on its peninsula, structurally fragile because every faction has incentive to press, simultaneously.
- **In-character aspiration:** To be the throne the deed-monarchy actually demands — a sovereign whose performance closes the gap between the throne's appearance and the throne's substance.

### Substrate-Posture

`[GAP — Phase B authoring per ED-717]`. Crown's substrate-posture is not yet documented. Likely structural shape: substrate-disengaged-or-sovereignty-focal — Crown treats Thread / rendering as Church's domain while quietly recognizing it is real but inactionable through sovereign tools. Almud's `Certainty 3 (Questioning)` per `npc_behavior §2.1` and his "privately sympathises with Restoration; recognises Thread reality may be true; does not act on it" stance suggests substrate-acknowledgment-without-engagement. Author at Phase B.

### Ethical Disposition

- **Legacy label:** Virtue `[SUPERSEDED 2026-05-02 — mechanical role replaced by PP-686 §3.7 triadic Ob calc]`. Retained as descriptive disposition tag for prose-writer continuity.
- **Public, visible, virtuous actions:** −1 Ob (legacy modifier; intent preserved through PP-686 mission_alignment_modifier on `da.public_governance`).
- **Covert / expedient action:** +1 Ob (legacy; intent preserved through PP-686 mission_alignment_modifier on `da.covert_betrayal` contradicted).
- **Leadership Deviation Ob:** 2 (Almud breaks treaty / supports practitioners / ignores Parliament → Stability check Ob 2 at next Accounting).

### Stats `[PROVISIONAL — see §5.2]`

| Stat | TTRPG | BG |
|---|---|---|
| Legitimacy | 5 | 5 |
| Popular Support | 5 | 5 |
| Influence | 5 | 5 |
| Wealth | 4 | 4 |
| Military | 4 | 4 |
| Intel | 3 | 3 |
| Stability | 4 | 4 |
| **Mandate (derived)** | 5 | 5 |

Crown standing army is **Löwenritter Order** (`faction_layer §1.5`). All Crown military operations field Löwenritter units pre-coup. Crown faction Military 4 expressed through Löwenritter Power 5 / Discipline 6 elite units. Post-coup, Löwenritter becomes independent faction with its own Military 5 sheet.

### Tactic / Unique Action — Royal Decree

Roll: Mandate vs Ob 2. Once per season.  <!-- LPS-1: L→Mandate -->

| Degree | Result |
|---|---|
| Overwhelming / Success | One faction stat ±1 immediate (any faction); consecutive seasons: +1 Ob/season |
| Failure | Legitimacy −1 (overreach) |

Cannot target Intel (decrees are public acts). Cannot target a stat absent from the target's sheet. Decree fatigue +1 Ob/season for consecutive use.

### Priority Tree (BG)

Per `npc_behavior_v30 §8.3`. Summary: Almud's tree weights stability-preservation high; Constrained-arc rule (`§5.1 ED-586`) shifts to institutional rebuilding when Mandate < 3.

### Doctrine Notes (`faction_layer §1.5`, canonical 2026-04-30 ED-775)

> Crown holds the highest perceived strength at game start: highest Mandate, highest Wealth, capital + heartland territory plus the Löwenritter standing army. It is also the campaign's central locus of structural tension. Almud is canonically constrained to choosing the least-bad option in every season because his position is assailed from every axis simultaneously: Altonia (external invasion), Schoenland (naval mediation), Restoration (cultural infiltration in T2/T5), Church (Sovereignty axis), Hafenmark (commercial competition), Varfell (Vaynard's ambition), and Löwenritter Order itself (graduated autonomy). Crown's perceived strength is exactly what makes its fracture the campaign's central dramatic possibility — every faction has reason to press, and Almud cannot resist all simultaneously. **The fragility is structural, not stat-based.**

### Stability Profile

Above-average baseline (Stability 4) but exposed to Trigger 1 (territorial loss — multiple capitals at risk: T1 Valorsplatz capital, T14 Ehrenfeld key) and Trigger 5 (failed military engagement — Crown commits Löwenritter elite at Pool ≥ 6 frequently, severity threshold easily met).

### Arc Trajectories (per `npc_behavior §5.2 Almud Arc Map`)

- **Arc A — The Reformer.** Almud Certainty ≤ 1 + Löwenritter Autonomy = Loyal. Hardest arc; window narrow. Player must destabilize Almud's worldview while keeping Crown stable enough that Löwenritter doesn't intervene. Reform from within is the most demanding path.
- **Arc B — The Fortress.** Crown Stability ≤ 2 + Almud Certainty ≥ 3 (unconfronted). Order doubles down; Reason secondary suppressed. Authority-only Resonant Style.
- **Arc C — The Overthrown.** Löwenritter Autonomy reaches Split (stage 4). Order → Autonomy survival. Almud becomes exile. Torben transfers to Löwenritter.
- **Arc D — The Avenger** (Royal Assassination sub-roll 1–2: Lenneth target).
- **Arc E — The Bereaved Father** (sub-roll 3–4: Torben target). Crown must retrieve Elske from Altonia. Compound provocation.
- **Arc F — Eliminated** (sub-roll 5–6: Almud target). Lenneth assumes throne — Widow Regent arc; Crown identity inverts (pro-Einhir, pro-Thread-research, anti-caste-suppression becomes explicit policy); Church opens Heresy Investigation.

Arcs D/E/F mutually exclusive — one sub-roll determines which (if any) fires per `params/bg/royal_assassination.md`.

### Legitimacy / Popular Support Dynamics

> **[Per LPS-1 (settlement_layer §1.8):** these dynamics operate **per controlled settlement** — builds/erodes apply to the faction's held settlements' L/PS; the aggregate (W-weighted settlement means) feeds Mandate.]

- **Builds L:** routine governance, peace treaties signed, succession events under `mode == normal`, formal acknowledgement by foreign powers.
- **Erodes L:** exposed `da.covert_betrayal`, coup attempts, Total Dismissal of Crown leader, sustained Cascade Fidelity violation (Almud acting against sovereign role expectations for ≥4 seasons).
- **Builds PS:** Mission outcomes attributed to Crown (Self-Other modulated; Almud's `-0.10` orientation gives near-full attribution).
- **Erodes PS:** Mission outcome failures + low Cascade Fidelity (β-fidelity gating active per §3.4 outcome_polarity_gate).

### Sub-Organizations

**Crown Inner Circle** (per `npc_behavior_v30 §2.15`, ED-634):
- Royal Marshal — **Wilhelm Voss** (Order / Authority MS / Certainty 4)
- Lord Treasurer — **Annalie Reichard** (Precedent / Evidence MS / Certainty 5)
- Spymaster — **Kolbrun Thale** (Autonomy / Consequence MS / Certainty 3) — sole inner-circle contact to settlement-layer intelligence brokers
- Archbishop's Representative — **Father Gustav Linder** (Faith / Authority MS / Certainty 5) — Himlensendt's agent
- Royal Guard Captain / Löwenritter Liaison — **Theodor Kreutz** (Order / Authority MS / Certainty 4) — pre-designated allegiance to Almud personally; his removal triggers Löwenritter Autonomy escalation toward Split

**Specialty Branches** (Standing 3+ unlock per `faction_politics §1.1b`).

**The Banner** — Standing 3 recognition token (`§1.1c`).

### Member NPCs

→ See `character_canon_v30.md` (pending) entries: Almud Almqvist · Lenneth Almqvist · Torben Almqvist · Elske Almqvist · Wilhelm Voss · Annalie Reichard · Kolbrun Thale · Father Gustav Linder · Theodor Kreutz · Gerik Strand (Lord Steward).

### Foil Dynamics (per `npc_foils_v30` and Nine Political Axes)

| Axis | Crown position | Primary opposition |
|---|---|---|
| 1. Sovereignty | Pole A (Crown authority) | Church (Pole B) |
| 3. Legitimacy | Pole A (Constitutional monarchy / deed-claim) | Church (Theocratic) |
| 6. Military authority | Pole A (Ducal/Crown command) | Church Templar independence |
| 8. External threat | **split internal position** | Altonian accommodation faction (Almud-leaning) vs resistance faction (Lenneth-leaning) within Crown |
| 9. Ontological | substrate-disengaged (Almud's quiet acknowledgment) | Practitioners on Pole B |

**Six pairings** (per `npc_foils_v30 PART ONE`): Almud ↔ Lenneth (Custodian / Reformist); Almud ↔ Baralta (Custodian / Claimant); Almud ↔ Vaynard (Manager / Revolutionary); Lenneth ↔ Baralta (campaign-defining confrontation); Lenneth ↔ Vaynard (diagnosis without agreement on treatment); Baralta ↔ Vaynard (total opposition).

### Provenance

Consolidates from: `faction_state_authoring_v30 §2`; `faction_layer_v30 §1.5` Crown doctrine notes; `factions_personal_v30 §8.2`; `npc_behavior_v30 §2.1, §2.15, §5.2 Almud Arc Map, §8.3`; `npc_foils_v30 PART ONE+TWO`; `params/factions/stats_1_7_scale.md` Starting Stats; `conviction_migration_roster_v30 §2.1`.

---

## Church of Solmund — Ecclesiastical

**Player-eligible** · **Mode coverage:** TTRPG / BG / Hybrid · **Status:** PROVISIONAL

### Identity

- **Full name:** The Church of Solmund
- **Role:** ecclesiastical (PP-686 §3.3.1)
- **Archetype:** the institutional rendering of Solmund's revelation — the body whose structural function is to interpret, transmit, and enforce the cosmological framework that distinguishes orthodoxy from heresy
- **Leader:** Confessor Arne Himlensendt (canonical per `params/bg/core.md L233`)
- **Cardinal officers** (Four-Cardinal structure per `worldbuilding_v30 §3.1`):
  - Cardinal of **Justice** — Sæmund Haelgrund (Inquisitor; TS 12 unrecognized — see character_canon)
  - Cardinal of **Temperance** — (Altonian diplomacy track; canonical scholar — Cardinal Magnus Klapp candidate)
  - Cardinal of **Fortitude** — (Templar arm; Cardinal Osten Jarnstal — candidate)
  - Cardinal of **Prudence** — Aldric Tormann (per `npc_roster #13`)
- **Capital:** T9 Himmelenger (cathedral city)
- **Other holdings:** T6 Stillhelm (PT 2)

### Mission (per `faction_state_authoring_v30 §3`, verbatim)

```yaml
text: "Establish Solmundan Orthodoxy across the peninsula"
primary_objective: victory.solmundan_orthodoxy   # CI=100 Mass Seizure path per victory_v30 §3.2
beneficiary: populace_of_valoria                 # the faithful
aligned_categories:
  - da.public_governance              # CI Suppression, doctrinal acts
  - da.diplomatic_alliance            # ecclesiastical alliances (Altonia)
contradicted_categories:
  - da.covert_betrayal                # public orthodoxy means visible action
  - da.antinomian_action              # heresy is the antithesis
prior_mission: null
```

### Expected Convictions (ecclesiastical role template, PP-686 §3.3.1)

`Faith 0.40, Authority 0.20, Scholastic 0.20, Precedent 0.10, Virtue 0.10`

Himlensendt per migration roster: `Faith 0.40 + Precedent 0.20 + Authority 0.15, ecclesiastical template, self_other +0.10` — Cardinal Reichard profile applied as Himlensendt mapping. High Cascade Fidelity expected at scenario init.

### Cultural Identity

The institutional body of Solmundan revelation. The Church reads the world through Solmund's revealed framework — Thread phenomena, practitioner activity, and the Southernmost crisis are interpreted as heresy or as confirmations of the doctrine that the Catastrophe was caused by Einhir overreach. Himlensendt is sincerely devout, not cynical: his faith is the load-bearing wall of the entire post-war settlement, and that is exactly what makes him the most dangerous person on the peninsula.

### Institutional Beliefs (first-person voice anchors)

1. "Solmund's word is the only truth — heresy is to be rooted out wherever it is found."
2. "The people require the Church's protection — pastoral care extends to every territory."
3. "Thread practitioners are deluded or deceived — compassion demands their salvation from themselves."

### Strategic Goals

- **Standing Mission:** Solmundan Orthodoxy across the peninsula — the Church as the integrative cosmological authority.
- **Situational:** Drive Church Influence (CI) to 60+ for territorial seizure; suppress Restoration Movement; counter Hafenmark Sovereign Authority Doctrine; prepare for the Consecration Crisis (if Baralta presses Crown claim).
- **Win path:** `victory.solmundan_orthodoxy` per `victory_v30 §3.2` (CI 100 Mass Seizure path).

### Inspiration

- **Historical parallel:** Avignon papacy + medieval Inquisition + Counter-Reformation Catholic Church. Doctrine treated as fully rationally intelligible — categorical commitment to a world that yields to the framework. The Spanish Inquisition's pattern of using procedural law to enforce doctrinal categories on populations who didn't fit them. Himlensendt's pastoral-not-political reflex echoes the "good cardinal" framing — sincerity is the structural strength and the structural blind spot.
- **In-character aspiration:** To be the institutional body that returns the peninsula to the integrative orthodoxy revelation demanded — not from cynicism but from genuine pastoral conviction that the alternative is suffering.

### Substrate-Posture

`[GAP — Phase B authoring per ED-717]`. Likely structural shape: rendering-reinforcement posture (T-08 candidate per cross-references). Church's framework actively suppresses Thread perception (perceptual prophylaxis at `Foundations §9.1`) — Faith Conviction interprets Thread phenomena as illusion-or-heresy. Theologically forecloses TS development. This is the strongest substrate-posture position in the canon (most-active-suppressor) but has not been formally authored as T-XX per ED-717. Author at Phase B.

### Ethical Disposition

- **Legacy label:** Faith `[SUPERSEDED 2026-05-02 — mechanical role replaced by PP-686 §3.7 triadic Ob calc]`. Descriptive disposition tag retained.
- **Doctrine-aligned (heresy suppression / Piety expansion / moral law enforcement):** −1 Ob.
- **Doctrine-contradicting:** +1 Ob.
- **Reveals Thread truth:** +2 Ob (institutional perceptual prophylaxis — Church-only modifier).
- **Leadership Deviation Ob:** 3 (highest of any faction — theological coherence is the Church's structural strength; deviation is structurally costly).

### Stats `[PROVISIONAL — see §5.2]`

| Stat | TTRPG | BG |
|---|---|---|
| Legitimacy | 5 | 5 |
| Popular Support | 5 | 5 |
| Influence | 6 | 6 |
| Wealth | 5 | 5 |
| Military | 4 | 4 |
| Intel | 4 | 4 |
| Stability | 5 | 5 |
| **Mandate (derived)** | 5 | 5 |

Influence 6 is the highest single-stat in the Starting Stats table — Church's diplomatic and pastoral reach exceeds all other factions. Intel 4 reflects Inquisition + nuncio network as institutional intelligence (per ED-787 closure: "institutional intelligence woven into existing diocesan and missionary infrastructure").

### Tactic / Unique Actions (Church has two)

#### Excommunication

Resolution: d+σ resolver (stats_1_7_scale §Domain Action Resolution) — contested (faction leader): M = Mandate − target Mandate; non-leader: M = Mandate − 2 (legacy Ob 2).  <!-- LPS-2e: L→Mandate; the 'faction L ±1' degree effects reconcile to Mandate / per-settlement L per settlement_layer §1.8 (entangled — see master ledger) -->

| Degree | Result |
|---|---|
| Overwhelming | Strips target's Circles bonus with Church contacts; −1 Legitimacy to each of the target's controlled settlements (lowers aggregate L → Mandate, settlement_layer §1.8); target barred from public office and Church-loyal command; personal Reputation −1 with all factions |
| Success | As Overwhelming minus the personal Reputation penalty |
| Failure | −1 Legitimacy to each Church-controlled settlement; target gains +1 Legitimacy in each of its controlled settlements (sympathy martyr) |

Requires Church Mandate ≥ 3. Reversal: Grand Debate (5 exchanges) or new Confessor.

#### CI 60 Territorial Seizure

Trigger: Church Influence (CI) reaches 60. Fires once per territory.

Roll: Influence + floor(CI/15) vs Ob = 7 − PT (AUTHORITATIVE per faction_layer §2.7; supersedes the stale L-based formula). Failure → Mandate −1.

| Degree | Result |
|---|---|
| Success | Administrative control of territory. Domain Actions vs Church authority require +2 Ob. Church Influence (territory-level value) fires immediately. |
| Failure | Mandate −1 (authoritative faction_layer §2.7) |

Riskbreaker exposure removes seized territory and prevents re-seizure for one season.

### Priority Tree (BG)

Per `npc_behavior_v30 §8.2`. Summary: Himlensendt's tree weights doctrinal expansion (Suppress, Assert, CI advance) high; pastoral protection second; Church Influence advancement structurally embedded.

### Doctrine Notes

`[GAP]` — no published §1.5 Church doctrine note in `faction_layer_v30`. The §3 ecclesiastical material lives in `factions_personal §8.3` and is captured above. Author at Phase B if differentiation from generic ecclesiastical role is needed.

### Stability Profile

Highest baseline (Stability 5) — theological coherence + institutional consolidation tradition. Most exposed to Trigger 4 (Subterfuge — Niflhel-era assassinations of cardinals; now via settlement-layer broker compromise) and Trigger 2 (Treaty terms unfavourable in Altonia diplomacy track). Church Absolution mechanic provides recovery to other factions at cost of 1 Mandate.

### Arc Trajectories (per `npc_behavior §5.2 Arne Himlensendt — Arc Map`)

- **Arc A — The Zealot** (Default — No Intervention). Faith remains unchallenged. CI advances to 75+. Territorial seizure begins.
- **Arc B — Crisis of Faith.** Total Victory Contest defeat via Evidence Resonant Style. OR: Cardinal of Temperance presents Thread-adjacent scholarly findings Himlensendt cannot dismiss (Altonian diplomacy ≥ 3 + Temperance Cardinal Conviction Reason). CI pressure decreases. Church Stability may drop −1 if Scar publicly known.
- **Arc C — Confrontation.** Public confrontation. If Confessor heretic publicly known: Church Stability −3. CI may decrease rapidly as institutional engine loses driver. **The vacuum may be worse — Cardinal of Justice or Fortitude may seize control and be more dangerous than Himlensendt ever was.**

### Legitimacy / Popular Support Dynamics

> **[Per LPS-1 (settlement_layer §1.8):** these dynamics operate **per controlled settlement**; the aggregate (W-weighted settlement means) feeds Mandate.]

- **Builds L:** procedural-event Keys (consecrations, ordinations, formal alliances), `meta.miraculous_event` favorable, sustained Cascade Fidelity to ecclesiastical role (high default at scenario init).
- **Erodes L:** exposed Inquisition overreach, Cardinal defection, miraculous_event unfavorable to Church (heresy declaration against itself), Thread-revelation publicly tied to Church suppression.
- **Builds PS:** doctrinal outcomes attributed to Church + traditional/principled-temperament populace alignment.
- **Erodes PS:** outcomes-only-temperament populations under hardship (Strain shifts territories toward outcomes-only — Church suffers Cascade Fidelity weight reduction).

### Sub-Organizations

**Four-Cardinal structure** (canonical per `worldbuilding_v30 §3.1`): Justice / Temperance / Fortitude / Prudence. See **Member NPCs** below.

**Inquisitor sub-ladder** (per `faction_politics §2.3`): Cardinal of Justice's branch. Heresy Investigation apparatus. Sæmund Haelgrund operates here.

**Templar sub-ladder** (per `faction_politics §2.4`): Cardinal of Fortitude's branch. Military arm of Church.

**Cardinal Officers** as sub-NPCs per `npc_behavior §2.13`. Extra-Territorial Heresy Jurisdiction per `§2.13a` (ED-670).

### Member NPCs

→ See `character_canon_v30.md`: Confessor Arne Himlensendt · Sæmund Haelgrund (Cardinal Justice / Inquisitor) · Cardinal Magnus Klapp (Temperance candidate) · Cardinal Arnlod Olafsson · Cardinal Osten Jarnstal · Aldric Tormann (Cardinal Prudence) · Father Gustav Linder (Crown's Archbishop's Representative — dual-loyalty NPC) · Cardinal Magnus Klapp (Scholar's Dilemma — TS exposure via archive work).

### Foil Dynamics

| Axis | Church position | Primary opposition |
|---|---|---|
| 1. Sovereignty | Pole B (Church authority) | Crown (Pole A) |
| 2. Knowledge | Pole B (Thread truth suppressed) | Varfell, Restoration, practitioners (Pole A) |
| 3. Legitimacy | Pole B (Theocratic governance) | Crown / Hafenmark |
| 4. Cultural identity | Pole B (Colonial settlement) | Restoration |
| 6. Military authority | Pole B (Templar independence) | Crown / Hafenmark |
| 9. Ontological | Pole A (World as it appears) | Practitioners (Pole B) |

**Consecration Triangle** (Almud — Baralta — Himlensendt): if Baralta claims the Crown, Himlensendt faces the question the Church has not faced since the Secession Wars — consecrating Baralta would confirm a divine right that includes Church subordination. His theology says he must refuse. His refusal cracks the settlement.

### Provenance

Consolidates from: `faction_state_authoring_v30 §3`; `factions_personal_v30 §8.3`; `npc_behavior_v30 §2.2, §2.13, §5.2 Himlensendt Arc Map, §8.2`; `worldbuilding_v30 §3.1` Four-Cardinal structure; `faction_politics_v30 §1.4, §2.3, §2.4`; `params/factions/stats_1_7_scale.md` Starting Stats; `conviction_migration_roster_v30 §2.3`.

---