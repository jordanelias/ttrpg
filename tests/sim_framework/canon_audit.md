# Valoria Campaign Simulation — Canon Audit vs Rebuild Workplan

**Status:** proposed 2026-04-19
**Scope:** audit of `tests/sim_framework/workplan_rebuild_2026-04-19.md` against all canonical design docs, params, and registries enumerated in `references/canonical_sources.yaml` and the file index
**Method:** skeleton survey of 22 primary sources (design docs, BG params, clock registry, NPC behavior + roster), cross-reference against workplan's five phases
**Purpose:** produce a coverage matrix so the engine_v4 rebuild binds every simulation mechanic to a canonical source — not the other way around

---

## Executive finding

The workplan is directionally sound (substrate-first, canon-bound, faction-asymmetric) but mechanically **incomplete on the order of 60–70%**. It captures the perimeter (17 territories, 36 settlements, mass battle phases, four-ruler AI) but misses the interior (resolution substrate, card-hand economy, 8-faction actor list, full clock stack, settlement-level tracks, post-battle cascade, NPC arc state machines, Thread substrate as world-degradation driver, all cross-actor Parliament/Treaty/Casus Belli systems).

Following the workplan as written will produce engine_v4 that runs, but simulates a simplified wireframe of Valoria's game rather than Valoria's game. The workplan's own Phase 0 deliverable — this audit — reveals the scope gap.

---

## Section 1 — What the workplan gets right

1. **Ordering.** Phase 0 audit before Phase 1 substrate before action layer before battle before political layer is correct sequencing.
2. **Principle.** "Every mechanic in the simulation must map to a canonical system already specified in the repo" is the correct foundation.
3. **Substrate priority.** Building territory + settlement + radiation + fortress data structures before AI is correct.
4. **Faction asymmetry.** Rejecting uniform balance targets and naming faction-specific identity (§4.1–§4.4) is correct.
5. **Scope exclusion.** Player character, scene layer, Godot implementation, hybrid TTRPG handoff are correctly deferred.
6. **Geography structure.** 17 territories / 36 settlements / fortress list / T15 special handling are materially accurate per `geography_v30` and `settlement_layer §2.1`.
7. **Mass Seizure formula.** `P=((CI-60)/40)^3.3` is canonically correct per `ci_seizure.md`.
8. **Starting PT values.** Reference to `peninsular_strain §2.2` Starting PT is correct.

---

## Section 2 — Coverage matrix (canonical systems → workplan coverage)

Legend: ✓ covered · ◐ partial · ✗ missing · ⚠ wrong source cited

### 2.1 Resolution substrate (`strategic_layer_v30`)

| Canonical element | Source | Workplan |
|-|-|-|
| d10 dice system | strategic_layer Correction 1 | ✗ |
| Ob minimum = 1 | strategic_layer Correction 2 | ✗ |
| Degree Table on d10 (negative net successes) | strategic_layer Correction 3 | ✗ |
| Majority-1s rule (d10 version) | strategic_layer I-01 | ✗ |
| Card-Hand system (PP-177) | core.md §Batch Card Hand | ✗ |
| Patience Protocol cap | strategic_layer I-02 | ✗ |
| Casus Belli expiration rules | strategic_layer I-03 | ✗ |
| Faction Collapse behavior | strategic_layer I-04 | ✗ |
| Battle Resolution comparison mechanic | strategic_layer I-05, G-12 | ✗ (workplan Phase 3 skeletal) |
| Standard Action Ob reference | core.md §Standard Action Ob | ✗ |
| Prosperity track (1–7 per territory) | clock_registry, G-02 | ✗ |
| Institutional Mandate Uphold/Appease (PP-189) | strategic_layer, parliament.md | ✗ |
| Information Asymmetry / Fog of War | strategic_layer §9.2 | ✗ |

**Gap weight:** CRITICAL. Without the dice system, Ob minimum, and Degree Table, the workplan's references to "canonical Ob, canonical pool" in Phase 2 cannot be implemented. Card-Hand is the strategic layer's core economy per project instructions.

### 2.2 Clock & track registry (`clock_registry_v30`)

| Clock / Track | Range | Owner | Workplan |
|-|-|-|-|
| Rendering Stability (RS) | 0–100 | Shared | ✓ |
| Church Influence (CI) | 0–100 | Shared | ◐ (partial — misses CI-100 Theocracy attempt) |
| Invasion Pressure (IP) | 0–100 | Shared | ◐ (scenario reference only) |
| Parliament Integrity (PI) | 0–20 | Shared | ✗ |
| Vaynard Thread Mastery (VTM) | 0–5 | Varfell | ✗ |
| Altonian Ecclesiastical Relationship (AER) | 0–5 | Church/Hafenmark | ✗ |
| Torben Loyalty | 0–7 | Crown→Löwenritter | ✗ |
| Elske Loyalty | 0–7 | Crown | ✗ |
| Coup Counter | 0–4 | Löwenritter | ◐ (mentions ≥4 trigger; omits counter behavior) |
| Popular Will (PW) | 0–5 | Shared/Hybrid | ✗ |
| Warden Cooperation (WC) | 0–3 | Shared | ✗ |
| Warden Recognition (WR) | 0–4 | Varfell | ✗ |
| Intel Advancement Counter | 0–3 | Varfell | ✗ |
| Reformed Doctrine Track (RDT) | 0–5 | Hafenmark | ✗ |
| Theological Dissatisfaction (TD) | 0–5 | Hafenmark | ✗ |
| Mandate | 1–7 | Faction stat | ◐ (implicit) |
| Influence | 1–7 | Faction stat | ◐ |
| Wealth | 1–7 | Faction stat | ◐ |
| Military | 1–7 | Faction stat | ◐ |
| Stability | 0–7 (0=eliminated) | Faction stat | ✗ |
| Intelligence | 1–7 | Faction stat (Varfell focus) | ✗ |
| Reputation / Standing | 0–5 each | Faction ladder | ✗ |
| Piety Track (PT) | 0–5 | Per-territory | ✓ |
| Fort Level | 0–4 | Per-territory | ✓ |
| Prosperity | 1–7 | Per-territory | ✗ |
| Guild Favour | 0–7 | Per-territory | ✗ |
| Church Attention Pool (AP) | 0–10 | Per-territory | ✗ |
| Cardinal Influence (×3) | 0–5 each | NPC | ✗ |
| Ministry AP-Tokens | per-territory (4) | NPC | ✗ |
| Settlement Prosperity | 0–5 | Per-settlement | ✗ |
| Settlement Defense | 0–5 | Per-settlement | ✗ |
| Settlement Order | 0–5 | Per-settlement | ✗ |
| Local Actor Disposition | −3 to +5 | Per-settlement | ✗ |
| Local Economy (derived) | Prosperity × 50 | Per-settlement | ✗ |
| Garrison Strength (derived) | Defense × 20 + Fort × 30 | Per-settlement | ✗ |
| Public Order (derived) | Order × 20 | Per-settlement | ✗ |
| Thread Debt | per-token | Cooldown | ✗ |
| Casus Belli | per-faction | Cooldown | ✗ |
| Accord (per-territory) | 0–3 (PP-645) | Per-territory | ◐ (named, mechanics missing) |
| Peninsular Strain | 0–10 | Global | ✗ |

**Gap weight:** CRITICAL. Workplan covers 4 of 40+ canonical tracks. These are the substrate the simulation reads and writes every season. Half the "Phase 4 political layer" cannot execute without them.

### 2.3 Faction roster (`factions_personal_v30`)

| Faction | Canon section | Workplan |
|-|-|-|
| Crown (Monarchy) | §8.2 | ✓ |
| Church of Solmund | §8.3 | ✓ |
| Hafenmark (Duchy) | §8.4 | ✓ |
| Varfell (Duchy) | §8.5 | ✓ |
| Guilds | §8.6 | ✗ (demoted to "event") |
| Niflhel (Shadow Network) | §8.7 | ✗ |
| People's Revolution / Restoration Movement | §8.8 | ◐ (misclassified as subnational activation only) |
| Löwenritter (Military Order) | §8.9 | ✗ (demoted to "event" — canonical as standalone faction) |
| Ministry of the Peninsula | §8.9b | ✗ |
| Schoenland (Spoiler) | §8.10 | ✗ |
| Parliamentary Vote framework | §8.11 | ✗ |
| Seasonal Accounting — Faction Phase | §8.12 | ✗ |
| Nine Political Axes | §8.1 | ✗ |
| Ethical Framework Modifiers | §8.1 | ✗ |
| Leader vs Institution distinction | §8.1 | ✗ |

**Gap weight:** CRITICAL. Workplan runs 4 factions. Canon has 8 faction actors + 3 special actors + institutional frameworks. Guilds, Niflhel, Löwenritter, Ministry, Schoenland all have canonical toolkits (see §8.6–§8.10) that drive campaign-scale events.

### 2.4 Rank ladder & political structure (`faction_politics_v30`)

| Canonical element | Section | Workplan |
|-|-|-|
| Seven-Rank Ladder Architecture (Standing 0–7) | §1.0 | ✗ |
| Crown Rank Ladder + Specialty Branches + Inner Circle | §1.1–§1.1d | ✗ |
| Hafenmark Rank Ladder | §1.2 | ✗ |
| Varfell Rank Ladder | §1.3 | ✗ |
| Church Rank Ladder + Consecration | §1.4–§1.4c | ✗ |
| Löwenritter Knight Ladder | §2.1 | ✗ |
| Riskbreaker Ladder (sub) | §2.2 | ✗ |
| Inquisitor Ladder | §2.3 | ✗ |
| Templar Ladder | §2.4 | ✗ |
| Guild Ladder | §2.5 | ✗ |
| Niflhel Ladder (4-arm) | §2.6 | ✗ |
| Warden of the Thread Ladder | §2.7 | ✗ |
| Caste Definitions | §3.1 | ✗ |
| Caste × Rank Advancement | §3.2 | ✗ |
| Caste as Renown/Disposition/Duty/Scar modifier | §3.3–§3.6 | ✗ |
| TC × Rank Ladder integration | §5 | ✗ |
| Baralta Crown Claim × Rank interactions (A/B/C outcomes) | §6 | ✗ |
| Ministry System expansion (Hafenmark Committees, Church Dicasteries, Varfell Jarl Councils) | §7.2–§7.4 | ⚠ (workplan claims "Crown is only faction with Ministries" — canonical only at game start; all 4 majors have equivalents) |
| Generational Shift / Torben Readiness | §8 | ✗ |
| Cross-Faction Parity Table | §9 | ✗ |

**Gap weight:** HIGH. Workplan §4.6 mentions caste as "political pressure" without binding to the mechanical layer. Rank ladders are the axis on which NPC progression, faction internal politics, and player advancement all sit.

### 2.5 Faction-layer mechanics (`faction_layer_v30`)

| Canonical element | Section | Workplan |
|-|-|-|
| Stability Trigger 1 — Territorial Occupation/Loss | §1.2 | ◐ |
| Stability Trigger 2 — Unfavourable Treaty Terms | §1.2 | ✗ |
| Stability Trigger 3 — Antagonistic Parliamentary Vote | §1.2 | ✗ |
| Stability Trigger 4 — Major Subterfuge | §1.2 | ✗ |
| Stability Trigger 5 — Failed Military / Significant Losses | §1.2 | ✗ |
| Stability Recovery | §1.3 | ✗ |
| Accounting Stability Check | §1.4 | ✗ |
| Territorial Occupation Establishment | §2.2 | ✗ |
| Occupation Effects | §2.3 | ✗ |
| Occupation Duration / Control Transfer | §2.4 | ✗ |
| Resistance Check | §2.5 | ✗ |
| Political Vacuum (PP-500) | §2.6 | ✗ |
| Church Seizure × Occupation integration | §2.7 | ✗ |
| Treaty Types (universal, not Crown-only) | §3.1 | ⚠ (workplan treats as Crown-specific) |
| Treaty Initiation | §3.2 | ✗ |
| Three-Phase Negotiation Structure | §3.3 | ✗ |
| Treaty Effects on Stability | §3.4 | ✗ |
| Casus Belli (shared resource) | §3.5 | ⚠ (workplan frames as Church-only via Excommunication) |
| Faction-Specific Negotiation Bonuses | §4.1 | ✗ |
| Grand Debate (Hybrid/TTRPG only) | §4.2 | ✗ |
| Parliamentary Mechanics (universal, not Hafenmark-only) | §5 | ⚠ (workplan treats as Hafenmark-specific lever) |
| Phase Placement | §5.2 | ✗ |
| Vote Mechanics | §5.3 | ✗ |
| Parliamentary Actions | §5.4 | ✗ |
| Target Rebuttal | §5.5 | ✗ |
| TC × Parliament Interaction | §5.6 | ✗ |
| Peninsular Strain × Parliament | §5.6b | ✗ |
| Wealth Zero Consequence | §5.7 | ✗ |
| NPC Vote Behavior | §5.8 | ✗ |
| Officer Capture and Significant Loss | §6 | ✗ |
| Three-Condition Gate (Trigger 5 full spec) | §6.2 | ✗ |
| Ransom (ED-334/335) | §6.3 | ✗ |
| BG Mode Officer Fate | §6.4 | ✗ |
| Turn Sequence Integration | §7 | ✗ |
| CI formula (full, for sim) | §9 | ⚠ (workplan cites ci_seizure but full CI formula is here) |

**Gap weight:** CRITICAL. These are the mechanics that turn territory stat-comparison loops into political campaigns. Stability triggers, treaty negotiation, parliament vote behavior, officer capture/ransom — all missing.

### 2.6 Military layer (`military_layer_v30`)

| Canonical element | Section | Workplan |
|-|-|-|
| Unit Token Representation | §1.1 | ✗ |
| Unit Types and Stats | §1.2 | ✗ |
| Military Stat → Unit Power Ceiling | §1.3 | ✗ |
| Muster Output | §1.4 | ✗ |
| Muster Prerequisites | §1.5 | ✗ |
| Unit Experience | §1.6 | ✗ |
| Wealth Zero → Unit Degradation | §1.7 | ✗ |
| Knights Templar (Church-only unit) | §1.8 | ◐ (mentions Templar deployment only) |
| Siege Action (ED-633) | §1.9 | ✗ |
| BG Battle Pool Formula | §2.1 | ✗ |
| Battle Outcome Margin System | §2.2 | ✗ |
| BG → TTRPG Handoff | §2.3 | n/a (scope-excluded) |
| TC Competitive Formula (Piety Yield, Charity, Templar, Assert, Suppress, Structural Suppression) | §3 | ✗ |
| Conditional Passive | §3.2 | ✗ |
| TC Seasonal Cap | §3.9 | ✗ |
| Full TC Accounting Sequence | §3.11 | ✗ |
| Accord as Population Commitment | §4.1 | ◐ |
| Prosperity → Unit Quality Gate | §4.2 | ✗ |
| Thread Integration cross-references | §5.1 | ✗ |

**Gap weight:** HIGH. The muster system (§1.4/§1.5), Military→Unit Power ceiling (§1.3), and Prosperity-gating (§4.2) govern every army's composition. Workplan's Phase 3 describes battle phases but not where armies come from or what limits their quality.

### 2.7 Mass battle (`mass_battle_v30`)

| Canonical element | Section | Workplan |
|-|-|-|
| Part A TTRPG Mass Battle | A.1–A.14 | n/a (scope) |
| A.13 Reinforcement between battles | A.13 | ✗ |
| A.14b Campaign Supply (NEW — historical_precedents) | A.14b | ✗ |
| A.14c Levy Restriction (NEW) | A.14c | ✗ |
| Part B Board Game Mass Battle — Design Principle | B.1 | ✗ |
| B.2 BG Unit Stats (pre-printed on tokens) | B.2 | ✗ |
| B.3 BG Battle Resolution | B.3 | ◐ (phases 1–6 named) |
| B.4 Tactic Cards | B.4 | ✗ |
| B.5 Hybrid Handoff | B.5 | n/a |
| Army Morale (Derived Composite) | Part C | ✗ |
| Part D Mass Combat World Bridge — Post-Battle Consequence Scenes | §D.1 | ✗ |
| Named Unit Officers | §D.2 | ✗ |
| Player Morale Effect | §D.3 | n/a |
| §E.1 Immediate Consequences | §E.1 | ◐ |
| §E.2 Accounting Consequences | §E.2 | ✗ |
| §E.3 Exceptions | §E.3 | ✗ |
| §E.4 Cumulative caps per season | §E.4 | ✗ |

**Gap weight:** HIGH. Workplan captures the battle-turn loop and cites Part E at a high level but omits supply, levy, reinforcement, named officers, cumulative caps — all of which constrain 120-season campaign rhythm.

### 2.8 Peninsular Strain & Victory (`peninsular_strain_v30`, `victory_v30`)

| Canonical element | Section | Workplan |
|-|-|-|
| Universal Victory Condition — Peninsular Sovereignty | peninsular_strain §6.1 / victory §0 | ✗ (workplan Phase 5 §5.3 cites victory_v30 generically) |
| Faction-Specific Victory Conditions STRUCK | peninsular_strain §6.2 | ⚠ |
| Co-Victory Peninsular Partition | peninsular_strain §6.3 / victory §4 | ✗ |
| Accord — per-territory attribute | §2 | ◐ |
| Starting Accord values | §2.1 | ✗ |
| Accord Gain/Loss rules | §2.3/§2.4 | ✗ |
| Accord vs Order — Scale Distinction (ED-626) | §2.4b | ✗ |
| Accord — RM Exception | §2.5 | ✗ |
| Accord — Löwenritter Adaptation | §2.6 | ✗ |
| Martial Law at Settlement Level (T5) | §2.6b | ✗ |
| Battle Consequences — Substrate Fracture (Pressure 1) | §3.1 | ✗ |
| Battle Consequences — Vulnerability Signal (Pressure 2) | §3.2 | ✗ |
| Peninsular Strain Counter — Advance / Reduce | §4.1/§4.2 | ✗ |
| Strain Threshold Effects | §4.3 | ✗ |
| Strain ↔ IP No Cross-Feeding | §4.4 | ✗ |
| Crown — Formal Crown Treaty | §5.1 | ◐ |
| Church — Graduated Seizure | §5.2 | ◐ |
| Hafenmark — Dynastic Proclamation | §5.3 | ◐ |
| Varfell — Cultural Reformation | §5.4 | ✗ (workplan lists Thread + Askeheim routes; omits Cultural Reformation) |
| World-State Transitions — RS=0 Post-Calamity | victory §5.1 | ◐ (RS collapse mentioned) |
| World-State Transitions — IP=100 Phased Occupation | victory §5.2 | ✗ |
| World-State Transitions — All Dissolved → Anarchy | victory §5.3 | ✗ |
| The Rupture Scene (ED-630) | victory §5 | ✗ |
| Crown — Peninsula Sovereignty strategy | victory §3.1 | ◐ |
| Crown — Dominion strategic milestone | victory §3.1 | ✗ |
| Church — Solmundan Orthodoxy (+ CI=100 Mass Seizure + Altonian Theocracy path) | victory §3.2 | ◐ |
| Hafenmark — Dynastic Assertion (Primary + Alternate ED-307) | victory §3.3 | ◐ |
| Varfell Path A — Intelligence Hegemony | victory §3.4 | ✗ |
| Varfell Path B — Southernmost Dominion | victory §3.4 | ✗ (workplan lists T15 route as geographic, not victory strategy) |
| Varfell Path C — Thread Supremacy | victory §3.4 | ✗ |
| RM — Cultural Revolution (Phase 1 Majority → Phase 2 Uprising T9) | victory §3.5 | ✗ |
| RM Presence Marker Mechanics | victory §3.5 | ✗ |
| Löwenritter — Military Regency | victory §3.6 | ✗ |
| Elske Loyalty Track | victory §3.6 | ✗ |
| Post-Coup Succession Rule (§3.6a ED-674) | victory §3.6a | ✗ |
| RM Founding Mechanic (ED-620) | victory §8 | ✗ |
| Win Probability Assessment | victory §10 | ✗ (workplan proposes own targets 30/20/15/15 without citing §10) |

**Gap weight:** CRITICAL. The workplan's balance targets in §5.7 are not canonical. Canon §10 Win Probability Assessment contains the approved targets. The workplan also misses that Faction-Specific Victory Conditions are STRUCK — there's one universal condition (Peninsular Sovereignty) with faction-asymmetric *strategies*, not 4 separate win paths.

### 2.9 Settlement layer (`settlement_layer_v30`)

| Canonical element | Section | Workplan |
|-|-|-|
| Two-Tier Map | §1.1 | ✓ |
| Settlement Types (Capital / Major / Minor / Rural) | §1.2 | ✓ |
| Settlement Stats (0–5 tracks) | §1.3 | ✗ |
| Institutional Facility Tiers (PP-661) | §1.4 | ✗ |
| Facility Slot Capacity by Settlement Type | §1.4.1 | ✗ |
| Allocation Rules | §1.4.2 | ✗ |
| Capacity Pressure as Political Mechanic | §1.4.3 | ✗ |
| Cross-Faction Wing Allocation | §1.4.4 | ✗ |
| Church Settlement Infrastructure — Four Independent Axes | §1.5 | ◐ (axes: workplan names Chapel/Church/Cathedral as single axis) |
| Parish Social Services | §1.6 | ✗ |
| Pastoral Assumption | §1.7 | ✗ |
| Settlement Registry (36 settlements) | §2.1 | ✓ |
| Two-Tier Authority Model | §3.1 | ✓ |
| Governor Assignment | §3.2 | ✗ |
| Subnational Faction Governance | §3.3 | ⚠ (workplan flags as gap; here) |
| Scene Slate Settlement Anchoring | §4.1 | n/a |
| Subnational Faction Visibility | §4.2 | ✗ |
| Settlement Events | §4.3 | ✗ |
| Thread Operations at Settlement (T1) | §4.4 | ✗ |
| Local Actors (T7) | §4.5 | ✗ |
| Settlement POI Templates (T3) | §4.6 | ✗ |
| Invasion and Defense | §5.1 | ◐ |
| Garrison and Defense | §5.2 | ✗ |
| Stature Ladder | §6.1 | ✗ |
| Faction Emergence — Local to National | §6.2 | ⚠ (workplan flags as gap) |
| Faction Collapse — National to Local | §6.3 | ✗ |
| Clock Recalibration for Extended Timeline | §7.1 | ✗ |
| Succession System | §7.2 | ✗ |

**Gap weight:** HIGH. The Institutional Facility Tiers system (§1.4 — capacity pressure, cross-faction wing allocation) is a major unstated political mechanic. Faction Emergence (§6.2) and Subnational Governance (§3.3) are in canon — the workplan erroneously flags them as gaps.

### 2.10 Threadwork (`threadwork_v30`)

| Canonical element | Section | Workplan |
|-|-|-|
| Mode Applicability Index (what applies to BG) | Mode Index | ✗ |
| Settlement-Level Thread Consequences (T1) | §[prelude] | ✗ |
| The Leap — Suspending Rendering | §2.3 | ✗ |
| Thread Operation Visibility | §2.3 | ✗ |
| Weaving — Things Cohere | §2.4 | ✗ |
| Pulling — Things Open | §2.4 | ✗ |
| Past-Oriented Pulling | §2.4 | ✗ |
| Locking — Unable to Become | §2.4 | ✗ |
| Dissolution — Unable to Be | §2.4 | ✗ |
| Mending — Repairing the Substrate | §2.4 | ✗ |
| Collective Operations | §2.5 | ✗ |
| Opposing Operations (Contested Intentionality PP-632) | §2.6 | ✗ |
| Coherence 10→0 — Reduction | §3.2 | ✗ |
| Coherence Thresholds | §3.3 | ✗ |
| Dissolution Residue | §3.4 | ✗ |
| Fallout Tables | §3.6 | ✗ |
| Rendering Crisis Resolution (PP-194) | §3.7 | ✗ |
| Co-Movement (Version C) — 15/18 card deck | §4 | ✗ |
| RS Degradation Sources | §5.2 | ✗ |
| RS Thresholds | §5.3 | ✗ |
| RS in Board Game | §5.4 | ✗ |
| Thread Revelation Curve | §5.6 | ✗ |
| Threadcut Beings — Ontological Status | §6.1 | ✗ |
| Observer-Dependent Rendering | §6.2 | ✗ |
| De-Actualisation | §6.4 | ✗ |
| BG-mode Thread Operations (Mend, Lock Chronic Drift) | §7.1 | ✗ |

**Gap weight:** CRITICAL. Workplan flags Thread ops as a `[GAP]`; canon has a complete 18k-token system. Thread is not just Varfell's mechanic — it's the world-degradation substrate that drives RS decline, Threadcut Beings (territories/NPCs can cease to exist), and Rendering Crisis events. Co-Movement 15-card deck is canonical.

### 2.11 NPC behavior (`npc_behavior_v30`)

| Canonical element | Section | Workplan |
|-|-|-|
| Stance Triangle framework | §1.1 | ✗ |
| Conviction Taxonomy | §1.2 | ✗ |
| Resonant Style Taxonomy | §1.3 | ✗ |
| Named NPC Stance Triangles (14 named NPCs) | §2.1–§2.14 | ✗ (workplan has 4 ruler sketches only) |
| Belief Structure | §3.1 | ✗ |
| Belief Revision | §3.2 | ✗ |
| Scar Accumulation and Conviction Effects | §3.3 | ✗ |
| Thread Operation → Conviction Scar Triggers | §3.4 | ✗ |
| Decision Derivation procedure (Named NPCs) | §4.1 | ✗ |
| Non-Named NPC Behavior | §4.2 | ✗ |
| Practitioner Coherence Decision Thresholds | §4.3 | ✗ |
| Arc Emergence State Machine | §5 | ✗ |
| Named NPC Arc Profiles (Almud/Arne/Inge/Magnus/Edeyja) | §5.2 | ✗ (workplan has own sketches, not canonical profiles) |
| Resonant Style × Contest system | §6 | n/a (scene layer) |
| Faction-Level Framework Drift | §7 | ✗ |
| BG Mode NPC Priority Trees — 10 factions/actors | §8.2–§8.10 | ✗ (workplan implies 4) |
| NPC Personal Outreach Generation | §8.11 | ✗ |
| Subnational Faction Outreach | §8.11.6 | ✗ |
| NPC Recruitment Procedure (PP-642) | §9.5 | n/a (player feature) |
| Named NPC Roster Tracking Capacity (PP-661) — Tiers | §11 | ✗ |

**Gap weight:** CRITICAL. Workplan §4 AI writeup fabricates decision logic for 4 rulers. Canon has a complete state machine + stance triangle + belief/scar/drift system for 14+ named NPCs across all 10 factions/actors.

### 2.12 NPC roster (`npc_roster_v30`)

| Named NPC | Canon entry | Workplan |
|-|-|-|
| Edeyja (Southernmost Warden-Chief) | Roster #1 | ✗ |
| Maret Uln (Varfell succession) | #2 | ✗ |
| Yrsa Vossen (RM leader) | #3 | ✗ |
| Sæmund Haelgrund (Church Justice Cardinal/Inquisitor) | #4 | ✗ |
| Sigrid Torsvald (Löwenritter Riskbreaker) | #5 | ✗ |
| Halvar Brandt (Löwenritter officer) | #6 | ✗ |
| Annika Feldhaus (Guilds representative) | #7 | ✗ |
| Peder Almstedt (Ministry bureaucrat) | #8 | ✗ |
| Gerik Strand (Crown Lord Steward) | #9 | ✗ |
| Dalla Virke (Niflhel syndicate) | #10 | ✗ |
| Doux Alexios Laskaris (Altonian, m. Elske) | #11 | ✗ |
| Rikard Solberg (Schoenland factor) | #12 | ✗ |
| Aldric Tormann (Cardinal Prudence) | #13 | ✗ |
| Almud Almqvist (Crown king) | npc_behavior §2.1 | ◐ (ruler sketch only) |
| Arne Himlensendt (Church Confessor) | §2.2 | ◐ |
| Inge Baralta (Hafenmark Duchess) | §2.3 | ◐ |
| Magnus Vaynard (Varfell Duke) | §2.4 | ◐ |
| Lisbeth Ehrenwall (Löwenritter Grandmaster) | §2.5 | ✗ |
| Aldric Hann (RM Secondary) | §2.7 | ✗ |
| Torben Almqvist (Crown Heir) | §2.8 | ◐ (Torben tutoring mentioned as IP 30 event) |
| Guildmaster Council (Collective) | §2.11 | ✗ |
| Niflhel four-arm structure | §2.12 | ✗ |
| Cardinal Officers (Church sub-NPCs) | §2.13 | ✗ |
| Registrar Lennart Haelgrund (Ministry T4) | §2.14 | ✗ |

**Gap weight:** HIGH. 20+ named NPCs with canonical stance triangles, arcs, and priority trees. Workplan simulates 4.

### 2.13 Geography (`geography_v30`)

| Canonical element | Workplan |
|-|-|
| 17 territories | ✓ |
| Adjacency graph | ✓ |
| Starting control summary | ✓ |
| Points of Interest per territory | ◐ (scope-excluded per workplan; correct deferral) |
| Altonian Invasion Routes | ✗ |
| Southernmost Access | ✓ |
| Church Geography | ✗ |
| Restoration Movement Geography | ✗ |
| Maritime Forgetting Zone | ✗ |
| Calamity Bleed Gradient | ◐ (captured via calamity_radiation) |

### 2.14 Calamity radiation (`calamity_radiation_v30`)

| Canonical element | Workplan |
|-|-|
| Node Distance Map from T15 | ✓ |
| Settlement-Type Radiation Modifier (T1) | ✗ |
| Radiation Matrix (RS 100–80 / 79–60 / 59–40 / 39–20 / 19–1 / 0) | ◐ (named; specific effects per band missing) |
| Southernmost Surge (RS ≤ 10 threshold) | ✗ |
| Threadcut Being Classification by Gap Severity | ✗ |
| Forgetting — Permanent Askeheim Condition (B-03) | ✗ |

### 2.15 Southernmost (`southernmost_v30`)

| Canonical element | Workplan |
|-|-|
| The Forgetting | ✗ |
| Southernmost Awareness (faction stat) | ✗ |
| Expedition Procedures — Prerequisites | ◐ |
| Expedition Multi-Season Extended Action | ✗ |
| Zone Hazard Table | ✗ |
| Expedition Failure | ✗ |
| Expedition Success Indicators | ✗ |
| Encounter Reference | ✗ |
| [NAME-PENDING: ED-048] Ritual | ✗ |
| Extraordinary Repair Weaving | ✗ |
| Combined TT Reduction Cap (SIM-STH-E1 PP-635) | ✗ |
| Southernmost Crisis Timeline | ✗ |
| Southernmost in BG mode | ✗ |

**Gap weight:** MEDIUM-HIGH. Workplan §1.5 is one sentence on T15 entry. Canon has Expedition Procedures (multi-season extended action), Zone Hazard Table, Forgetting condition, Crisis Timeline, and a full Ritual system in Askeheim — needed for Varfell Path B Southernmost Dominion victory path.

### 2.16 BG params (`params/bg/*`)

| File | Primary content | Workplan |
|-|-|-|
| `phases.md` | Phase 4 resolution priority, Phase 5 Seasonal Accounting, Year-End Accounting | ◐ (cited; not expanded) |
| `faction_actions.md` | Per-faction unique action specs (PP-428–442) | ◐ (cited; workplan's action list is incomplete vs canon) |
| `npc_priority_trees.md` | 10 faction priority trees + refinements | ✗ (workplan writes own AI logic) |
| `military.md` | Muster rules | ✗ |
| `ministry.md` | Ministry NPC faction + stats + tokens + PI connection + AI tree + Compromise/Corruption | ✗ |
| `parliament.md` | PI scale, Crown Policy Instrument, Mandate Recovery/Suppression, PP-189 Uphold/Appease, Ministry Domain conflict, Open Pledge (PP-515), Crown-Break trigger | ✗ |
| `institutions.md` | Church structure + 4 Cardinals + Levies + Excommunication procedure; Löwenritter structure + reconstitution; Ministry canonical identity; Parish/Cathedral system | ✗ |
| `clocks.md` | RS/CI/IP environmental effects, Cascade Depth Cap | ✗ (workplan doesn't enumerate environmental effects) |
| `tracks.md` | Trade Network Investment, AER, RDT, TD, VTM, Church AP rules, Accord (PP-645), Peninsular Strain (PP-646), Starting PT (PP-652) | ✗ |
| `ci_seizure.md` | CI Generation seasonal, Faction Political Pool, Mass Seizure, Battle Ob Formula (PP-499 ED-343) | ◐ (formula cited; rest missing) |
| `core.md` | Faction assignment (playable vs NPC-only), Dice System (v05), Degree Table (PP-179/249), Starting Values, Faction Starting Stats, Faction Elimination, Stat Ceilings/Floors, Standard Action Ob, Ethical Framework Modifiers, Faction Conviction Texts, Card-Hand system PP-177 | ✗ |
| `stress_patches.md` | BG stress patches, TCV correction PP-470, RM Founding Mechanic PP-478 (status by mode, PW track, founding trigger, community organising) | ✗ |
| `ed_resolutions.md` | Dozens of editorial resolutions (PP-262–322+) including BG Overwhelming thresholds, Zoom In ordering, VTM P-14 compliance, Reformed Settlement responses, Crown territory names | ✗ |
| `npcs_special.md` | Torben Loyalty, Elske Off-Board Card, Patience Protocol, Riskbreakers, Warden Recognition (PP-425 Path B), Warden Emergence, Warden Cooperation, Warden's Accord, Intel Advancement, Command Event Captured/Killed General | ✗ |

**Gap weight:** CRITICAL. These 16 BG param files are the mechanical surface area of the strategic layer. Workplan cites them as a bundle but doesn't bind to specific PP-numbered rules.

### 2.17 Philosophical foundations (`canon/00_philosophical_foundations.md`)

| Canonical element | Workplan |
|-|-|
| P-01 through P-15 principles | ✗ |
| P-01: Thread as substrate | ✗ |
| P-15: settlement identity as cultural-layer persistence | ✗ |

The workplan cites this doc but doesn't bind any P-# principle to any engine behavior. At minimum P-01 (Thread substrate) and P-15 (cultural persistence at settlement layer) should drive Phase 1 substrate design.

---

## Section 3 — Mis-attributions

Workplan source-citations that point at wrong or superseded files:

1. **CI seizure formula** — cited `ci_seizure.md §3.6`. Canonical CI 0–100 political legitimacy + Theocracy Unification at CI=100 lives in `ci_political_v30.md §2–§3`. The `ci_seizure.md` contains the Seizure curve only.
2. **Victory conditions** — cited `victory_v30.md`. `peninsular_strain_v30 §6.2` STRUCK faction-specific victory conditions; universal condition is Peninsular Sovereignty. `victory_v30` §3.x faction strategies are asymmetric paths to the universal condition, not separate wins.
3. **Casus Belli** — framed as Church-only consequence of Excommunication (§2.3 workplan). `faction_layer §3.5` is a shared universal resource.
4. **Parliament** — framed as Hafenmark-specific lever (§2.4 workplan). `faction_layer §5` is a universal system all factions use.
5. **Ministries** — workplan states "Crown is the only faction with Ministries at game start." `faction_politics §7` documents Hafenmark Parliamentary Committees (§7.2), Church Dicasteries (§7.3), Varfell Jarl Assembly Councils (§7.4) as canonical parallel institutions.
6. **RM as subnational** — workplan §4.5 frames People's Revolution/Restoration Movement as "subnational faction activation." Per `factions_personal §8.8` and `victory §3.5`, RM is a full faction with Cultural Revolution victory path (Phase 1 Majority → Phase 2 Uprising T9) and Founding Mechanic (ED-620 / PP-478).

---

## Section 4 — False gaps

Workplan §244–253 flags 6 gaps. Three are documented in canon:

| Claimed gap | Actual canon location |
|-|-|
| `[GAP: RM activation trigger conditions]` | `factions_personal §8.8`, `victory §8` RM Founding (ED-620), `stress_patches PP-478` Founding Trigger |
| `[GAP: Thread operations in mass battle]` | `mass_battle A.10 Thread Operations in Mass Battle` (691 tokens); `threadwork §2.3–§2.6` full Thread ops |
| `[GAP: subnational faction emergence]` | `settlement_layer §3.3 Subnational Faction Governance` + `§6.2 Faction Emergence — Local to National` |

Three may still be real gaps (need full-text read to confirm):

| Claimed gap | Status |
|-|-|
| `[GAP: mine income rate]` | Not in `faction_politics` Hafenmark sections surveyed; needs full read of `factions_personal §8.4` |
| `[GAP: Hafenmark food vulnerability]` | ED-054 referenced by workplan as unresolved; needs editorial ledger check |
| `[GAP: Crown Einhir suppression action]` | No canonical DA surfaced in surveys; needs `character_histories_v30` full read |

---

## Section 5 — Real gaps the workplan missed

Systems where canon is incomplete or where the skeletons show `[EDITORIAL:]` or `OPEN ITEMS` blocks (candidates for editorial resolution before sim can bind):

- Accord starting values per territory (`peninsular_strain §2.1` surveyed at skeleton level — needs full read to confirm complete table)
- TC × Parliament Interaction (§5.6 `faction_layer` — 21 tokens; likely stub)
- §1.9 Siege Action (ED-633 — resolution date 2026-04-17; may be fresh)
- §6.2a Post-Coup Succession Rule (ED-674) — new; needs full read
- §4.3 Settlement Events — full table may have unresolved entries
- `threadwork §3.7 Rendering Crisis Resolution (PP-194) [PROVISIONAL]` — flagged provisional in skeleton
- `victory §11 Open Editorial Items` + `§3.4 Varfell Path B pending user decision (ED-311)` — Varfell Path B status
- Several `PART 9: OPEN ITEMS` and `§10 OPEN EDITORIAL ITEMS` sections across `settlement_layer`, `military_layer` — catalog required

---

## Section 6 — Recommendations for a revised workplan

### 6.1 Phase 0 expansion

Add to mandatory reads:
- `designs/provincial/faction_politics_v30.md` (rank ladders, caste integration, ministry expansion)
- `designs/provincial/ci_political_v30.md` (CI 0–100 political legitimacy, card hand, cooldowns, AI posture)
- `designs/provincial/peninsular_strain_v30.md` (Accord full layer, Strain counter, universal victory)
- `designs/provincial/military_layer_v30.md` (unit tokens, muster, TC competitive formula, Prosperity gate)
- `designs/provincial/strategic_layer_v30.md` (d10, Ob minimum, Degree Table, Institutional Mandate, Patience Protocol, Fog of War)
- `designs/provincial/clock_registry_v30.md` (complete track inventory)
- `designs/threadwork/threadwork_v30.md` (five operation types, Coherence, Co-Movement deck, Threadcut Beings)
- `designs/npcs/npc_behavior_v30.md` (stance triangles, belief/scar/drift, 10 priority trees, arc state machine, roster capacity tiers)
- `designs/npcs/npc_roster_v30.md` (13 additional named NPCs)
- `params/bg/core.md`, `parliament.md`, `institutions.md`, `tracks.md`, `ci_seizure.md`, `stress_patches.md`, `ed_resolutions.md`, `npcs_special.md` (PP-numbered rule binding)

### 6.2 Phase 1 substrate additions

Beyond territories + settlements + radiation + fortresses:
- Full clock stack (all 40+ tracks from `clock_registry`)
- Per-territory tracks: PT, Fort, Prosperity, Guild Favour, Church AP, Accord
- Per-settlement tracks: Prosperity 0–5, Defense 0–5, Order 0–5, Local Actor Disposition, Guild Favor
- Derived settlement stats: Local Economy, Garrison Strength, Public Order
- Institutional Facility Tiers (PP-661) — capacity per settlement type, slot allocation, cross-faction wing
- Named NPC roster (13 from `npc_roster` + 14 from `npc_behavior §2`) with stance triangles

### 6.3 Phase 2 action layer additions

- d10 + Degree Table resolution as the action resolution substrate
- Card-Hand system (PP-177) — actions are drawn/spent, not free-chosen
- Cooldown Track and Renewal (`ci_political §5.3`)
- Universal actions: Treaty (all 3 types), Parliamentary Vote, Casus Belli creation/consumption, Muster, Siege
- Faction-specific actions: full per-faction toolkit from `faction_actions.md` (PP-428–442 × 5 factions × unique actions)
- Ministry/Committee/Dicastery/Council deployment per-faction (not Crown-only)
- Thread operations (all 5 types) gated by TS/Coherence

### 6.4 Phase 3 mass battle additions

- B.2 BG Unit Stats (pre-printed tokens)
- B.3 Pool Formula + Margin System
- B.4 Tactic Cards
- A.13 Reinforcement between battles
- A.14b Campaign Supply
- A.14c Levy Restriction
- Named Unit Officers + capture/ransom/death consequences
- §E.4 Cumulative caps per season

### 6.5 Phase 4 political layer additions

- 5 Stability triggers (not one generic "stability")
- 3-phase Treaty negotiation (Declaration → Terms → Resolution)
- Parliamentary vote cycle with NPC vote behavior (§5.8)
- Officer capture/ransom
- Full NPC Arc state machine per `npc_behavior §5`
- Ten priority trees, not four
- Named NPC Outreach generation (§8.11)
- Framework Drift at faction level (§7)
- Faction Emergence (local-to-national) and Collapse (national-to-local) — RM and Löwenritter as conditional factions

### 6.6 Phase 5 integration additions

- Universal Victory Condition as primary resolution check
- 6 faction victory *strategies* (not conditions), one per faction incl. RM and Löwenritter
- 3 World-State Transitions (RS=0 Post-Calamity, IP=100 Phased Occupation, All Dissolved Anarchy)
- Rupture Scene (ED-630) as explicit event
- Win Probability Assessment (victory §10) as the canonical balance target, not workplan-proposed 30/20/15/15

### 6.7 Session budget revision

Workplan estimates 8 sessions. Realistic estimate given gap scope: **12–14 sessions**, distributed as:
- Phase 0 (audit completion + editorial resolution for ~6 real gaps): 2 sessions
- Phase 1 (substrate including full clock stack + settlements + NPC roster): 2 sessions
- Phase 2 (action layer across 8 factions + card-hand + cooldowns + Thread ops): 3 sessions
- Phase 3 (mass battle full Part B + A.13/14b/14c + Part E): 1 session
- Phase 4 (political layer — Stability × 5 + Treaty × 3-phase + Parliament + Officer capture + NPC state machines × 10): 3 sessions
- Phase 5 (integration + smoke tests + balance verification vs §10 targets): 1–2 sessions
- Contingency for editorial gap resolution: 1 session

---

## Section 7 — Blocking gap register (for editorial resolution)

Items that must be resolved before engine_v4 binds mechanics to canon. Numbered to match editorial ledger convention.

### 7.1 Source attribution corrections (workplan → canon)

- [AUDIT-REB-01] CI formula attribution: primary source is `ci_political_v30 §9`, not `ci_seizure.md §3.6`
- [AUDIT-REB-02] Victory condition: universal Peninsular Sovereignty per `peninsular_strain §6.1`; faction-specific conditions are STRUCK per §6.2; workplan Phase 5 needs revision
- [AUDIT-REB-03] Casus Belli as shared resource per `faction_layer §3.5`; workplan Church-only framing is wrong
- [AUDIT-REB-04] Parliament as universal system per `faction_layer §5`; workplan Hafenmark-only framing is wrong
- [AUDIT-REB-05] Ministry parallel institutions (Committees / Dicasteries / Councils) per `faction_politics §7.2–§7.4`; workplan "Crown-only" framing is partial
- [AUDIT-REB-06] RM as full faction (§8.8) with Cultural Revolution victory path; workplan "subnational faction activation only" is wrong

### 7.2 Systems that require full-text reads before Phase 1 begins

- [AUDIT-REB-07] `strategic_layer_v30` full text — d10 + Ob≥1 + Degree Table + Institutional Mandate + Patience Protocol + VTM/Theocracy Counter / IP advancement + Fog of War
- [AUDIT-REB-08] `faction_politics_v30` full text — 4 main rank ladders + 7 sub-ladders + caste integration × rank × scar × disposition + ministry expansion
- [AUDIT-REB-09] `npc_behavior_v30` full text — stance triangles (14 named) + arc state machine + 10 priority trees + Outreach generation + Roster Capacity
- [AUDIT-REB-10] `npc_roster_v30` full text — 13 additional named NPCs with stance + arc + axis positions + mode interface
- [AUDIT-REB-11] `threadwork_v30` full text — 5 operations + Coherence + Co-Movement deck + Threadcut Beings + De-Actualisation
- [AUDIT-REB-12] `peninsular_strain_v30` full text — Accord full layer + Strain counter + universal victory + 4 faction territorial tools
- [AUDIT-REB-13] `victory_v30` full text — all faction strategies + Elske Loyalty + Post-Coup Succession + RM Founding + World-State Transitions + §10 Win Probability
- [AUDIT-REB-14] `military_layer_v30` full text — unit tokens + muster + TC competitive formula + Prosperity gate + Siege
- [AUDIT-REB-15] `settlement_layer_v30` full text — all 10 parts including Institutional Facility Tiers + Subnational Governance + Stature Ladder + Faction Emergence/Collapse + extended timeline + succession
- [AUDIT-REB-16] `clock_registry_v30` full text (already read) + every track's source file for mechanics
- [AUDIT-REB-17] `params/bg/*` — full text of all 16 files for PP-number binding (core, parliament, institutions, ministry, tracks, ci_seizure, clocks, military, phases, faction_actions, npc_priority_trees, stress_patches, ed_resolutions, npcs_special, victory, geography)
- [AUDIT-REB-18] `canon/00_philosophical_foundations.md` — P-01 through P-15 for substrate principles

### 7.3 Potential real gaps (need full-text verification)

- [AUDIT-REB-19] Hafenmark mine income rate — search `factions_personal §8.4` + `params_bg/tracks.md` Trade Network Investment
- [AUDIT-REB-20] Hafenmark food vulnerability — ED-054 status in editorial ledger
- [AUDIT-REB-21] Crown Einhir suppression action — `character_histories_v30` full read
- [AUDIT-REB-22] Various `OPEN ITEMS` / `§10/§11 Open Editorial Items` sections in surveyed skeletons need catalog pass

---

## Section 8 — Sequencing

1. This audit → review/approval
2. Editorial resolution of AUDIT-REB-19, -20, -21 (real gaps)
3. Full-text reads AUDIT-REB-07 through -18 (substrate for binding)
4. Revised workplan incorporating coverage matrix additions (Section 6)
5. Revised workplan → review/approval
6. Phase 1 substrate build against revised spec

Only after step 6 does engine code get written. The current workplan should not be the implementation spec.

---

## Appendix A — Files surveyed at skeleton/header level

- `designs/provincial/mass_battle_v30_skeleton.md` (42 sections)
- `designs/territory/settlement_layer_v30_skeleton.md` (46 sections)
- `designs/provincial/faction_layer_v30_skeleton.md` (51 sections)
- `designs/provincial/factions_personal_v30_skeleton.md` (19 sections)
- `designs/provincial/faction_politics_v30_skeleton.md` (88 sections)
- `designs/provincial/strategic_layer_v30_skeleton.md` (70 sections)
- `designs/provincial/ci_political_v30_skeleton.md` (34 sections)
- `designs/provincial/military_layer_v30_skeleton.md` (33 sections)
- `designs/provincial/peninsular_strain_v30_skeleton.md` (42 sections)
- `designs/provincial/victory_v30_skeleton.md` (64 sections)
- `designs/provincial/clock_registry_v30.md` (full — not a skeleton)
- `designs/threadwork/threadwork_v30_skeleton.md` (81 sections)
- `designs/npcs/npc_behavior_v30_skeleton.md` (104 sections)
- `designs/npcs/npc_roster_v30_skeleton.md` (40 sections)
- `designs/world/geography_v30.md` (header scan)
- `designs/world/calamity_radiation_v30.md` (header scan)
- `designs/world/southernmost_v30.md` (header scan)
- `params/bg/phases.md`, `faction_actions.md`, `npc_priority_trees.md`, `ministry.md`, `parliament.md`, `institutions.md`, `clocks.md`, `tracks.md`, `ci_seizure.md`, `core.md`, `stress_patches.md`, `ed_resolutions.md`, `npcs_special.md` (header scans)

## Appendix B — Not yet surveyed (for completion in AUDIT-REB-07 through -18)

- `designs/npcs/npc_character_analyses_v30_infill.md` (45k chars — full read needed)
- `designs/provincial/baralta_crown_claim_v30.md` (13k chars — Crown Succession Contest / Consecration Crisis)
- `designs/provincial/varfell_path_b_v30.md` (Varfell Southernmost victory path detail)
- `designs/provincial/clock_registry_v30_infill.md`
- All `*_infill.md` files for systems above
- `canon/00_philosophical_foundations.md` (70k chars — P-01 through P-15 full)
- `canon/editorial_ledger.yaml` — for ED-054 status and other editorial items
- Individual BG param file full reads (beyond headers)
