# VALORIA — Canonical Registry (Definitive, Revision 2)
## Supersedes: valoria_canonical_definitive.md (Revision 1)
## All corrections from cross-conversation review and simulation inventory applied
## Date: 2026-04-15

---

# HIERARCHY 1: WORLD SCALE

## 1.1 Global Clocks

| Canonical Name | Range | Start | Direction | Meaning |
|---|---|---|---|---|
| **Metaphysical Stability** | 0–100 | 72 | ↓ decay | Substrate coherence. 0 = Rupture (shared loss). |
| **Church Influence** | 0–100 | 28 | ↑ | Church institutional authority. No freeze. Milestones at 40/55/65/80/100. |
| **Invasion Pressure** | 0–100 | 20 | ↑ | Altonian military threat. 100 + weak diplomacy = Altonian Conquest. |
| **Political Stability** | 0–10 | 0 | ↑ bad | Cumulative violence cost. Gates universal victory (≤ 6). |

**Struck:** Parliament Integrity, Public Instability.

### Metaphysical Stability

Decay: −1/year baseline. Thread operations accelerate. Mending/Community Weaving restore.

Thresholds: 100–80 Stable, 79–60 Strained, 59–40 Fragile, 39–20 Fractured, 19–1 Critical, 0 Rupture.

**Calamity radiation is dynamic.** Fixed node-distance values from calamity_radiation_v30 define geographic susceptibility. Effects at each distance depend on current Metaphysical Stability band. At MS 79–60, only Askeheim (distance 0) and distance-1 territories affected. At MS 19–1, effects reach distance-4. The radiation zone expands as MS drops — this IS the visual expression of the Catastrophe spreading.

### Church Influence

Per tc_political_redesign_v30. Seasonal advancement: conditional passive +1 (requires Church controls T9 AND Stability ≥ 3), Piety Yield weighted by Spiritual Weight, Assert +1, Suppress negates passive. Cap ±5/season total, ±3 from Domain Actions.

**Milestones:** 40 (Church Assertive: +1D Assert/Seizure), 55 (Church Prominent: opposing factions +1 Ob), 65 (Church Dominant: extra action to oppose Church in Parliament), 80 (Church Ascendant: Seizure Ob −1, Piety drift +1/year), 100 (Theocracy Unification: seizure on any territory, secular factions get free Parliamentary motion/season).

**Political legitimacy bonus:** Church in political forums: +floor(Church Influence / 20) bonus dice. Secular factions opposing Church: −floor(Church Influence / 30) effective voting Mandate.

**Simulation data (valoria_sim v4):** Without counter-mechanics, Church wins 53% of pure-AI campaigns. tc_political_redesign addresses this by distributing TC suppression and adding political costs.

### Political Stability

Advances: +1/season with inter-faction battle, +2 per faction elimination, +1 per territory Revolt. Reduces: −1 per peaceful season, −1 per diplomatic resolution.

Thresholds: 0–2 Peace, 3–4 Tension (Mandate check Ob 1), 5–6 Fracture (Accord −1 in one territory), 7–8 Crisis (Accord −1 all non-capitals, Mandate check Ob 2), 9–10 Collapse (Accord cap 2, Mandate check Ob 3, MS −1/season).

---

# HIERARCHY 2: TERRITORY SCALE

## 2.1 Per-Territory Values (all 0–4, balanced at 2)

| Name | Range | Balanced | Meaning |
|---|---|---|---|
| **Accord** | 0–4 | 2 | Population acceptance. 0 Revolt, 1 Resistant, 2 Compliant, 3 Supportive, 4 Aligned. |
| **Piety** | 0–4 | 2 | Religious orientation. 0 Restoration pole, 4 Solmund pole. |
| **Prosperity** | 0–4 | 2 | Economic health. Determines Wealth contribution and muster quality. |
| **Fort Level** | 0–4 | 2 | Fortification. Modifies Battle Ob and defensive bonuses. |

### Prosperity → Wealth

Territories at Prosperity ≥ 2 AND Accord ≥ 2 contribute +1D to faction Trade pool at Accounting. Territories at Accord ≤ 1 contribute nothing.

Prosperity → Muster Size: 0–1 = Size 2 (base), 2–3 = Size 3 (+1), 4 = Size 4 (+2).

Prosperity changes: Govern Success +1, Govern Failure at 0 = Stability −1, Battle in territory −1, Blockade −2/season.

### Accord

| Accord | Name | Effects |
|---|---|---|
| 0 | Revolt | Territory becomes Uncontrolled. Garrison fights Uprising (Military vs Ob 2). |
| 1 | Resistant | No Prosperity contribution. Govern +1 Ob. Garrison required or → 0. |
| 2 | Compliant | Normal operations. Full Prosperity contribution. |
| 3 | Supportive | Full Prosperity. +1D Govern in this territory. |
| 4 | Aligned | Full Prosperity. Defender +1D in Battle. −1 Ob Govern. |

Starting: capitals = 4, home territories = 2. Military conquest → Accord 1. Defender territory in battle → Accord −1.

Territory Value counts only at Accord ≥ 2.

### Piety

0 = Restoration pole, 4 = Solmund pole. Church Seizure Ob = 6 − Piety (revised for 0–4 scale).

### Territory Value (was Territory Consolidation Value)

Range 0–5 (Askeheim = 0). Starting: Crown 12, Hafenmark 6, Church 5, Varfell 6.

### Spiritual Weight

Fixed per territory. Gates Church Influence flow and political legitimacy. Range 0–5. T9 Himmelenger = 5, T8 Gransol = 3, T14 Ehrenfeld = 3, all others 1–2, T15 Askeheim = 0.

### Church Attention Pool

Per-territory 0–10. Advances from visible Thread ops (+1), fieldwork Exposure at Watched (+1), public practitioner identification (+2). At ≥ 3: first Inquisitor (+1D Church Investigate). At ≥ 6: second Inquisitor (+2D, Heresy Investigation Ob −1). Resets Year-End.

**Simulation data:** Fieldwork contributes ~11% of max TC acceleration over 4 seasons. Cap (+1/character/season, +2/territory/season) is sufficient (SIM-DEBT-FW-04).

---

# HIERARCHY 3: FACTION SCALE

## 3.1 Faction Stats (1–7)

Mandate (0–7, 0 = subjugated), Influence (1–7), Wealth (1–7), Military (1–7), Stability (0–7, 0 = dissolved). Seasonal cap ±2.

**Intel: STRUCK.** Replaced by fieldwork Investigation + VTM.

## 3.2 Card System

| Faction | Hand | Domain Expertise |
|---|---|---|
| Crown | 2× Legionary, 1× Consul, 1× Senator, 1× Prefect, 1× Recess | Legionary (+1D) |
| Church | 2× Senator, 1× Pontifex, 1× Consul, 1× Legionary, 1× Recess | Senator (+1D) |
| Hafenmark | 2× Consul, 1× Senator, 1× Legionary, 1× Diplomat, 1× Recess | Consul/Prefect (+1D) |
| Varfell | 2× Tribune, 1× Legionary, 1× Consul, 1× Colonist, 1× Recess | Tribune (+1D) |

Cooldown: most cards 1 season; Pontifex/Prefect/Colonist 2 seasons; Recess 0.

## 3.3 Faction-Specific Tracks

VTM (Varfell, 0–5), Warden Cooperation (shared, 0–3), Warden Recognition (Varfell, 0–4), Torben Loyalty (Crown→Löwenritter, 0–7, start 3), Elske Loyalty (Crown, 0–7, start 4), Coup Counter (Löwenritter hidden, 0–4).

**Struck:** AER, RDT, Patience Counter, Intel Advancement Counter.

---

# HIERARCHY 4: INDIVIDUAL SCALE

## 4.1 Attributes (10, range 1–7)

Physical: Agility, Endurance, Strength. Mental: Cognition, Recall, Focus. Social: Attunement, Bonds, Charisma. Metaphysical: Spirit.

Creation: 31 points, min 1 each, max 5 for one/4 for rest. Advancement max 7. No attribute may reach 0.

## 4.2 Histories

Level 1/2/3, each = +1D. Cap = Recall score.

## 4.3 Universal Pool

**(Primary Attribute × 2) + History (0–3D) + 3. Minimum 5D. TN 7.**

Thread exception: (Spirit × 2) + History + TPS (replaces +3). TN 7 standard, TN 8 Binding/POP, TN 9 POP-Binding.

## 4.4 Universal Obstacle

**Ob = floor(Attribute / 2) + 1.**

## 4.5 Derived Values

| Value | Formula | Notes |
|---|---|---|
| Combat Pool | (Agi×2) + Hist + 3, min 5 | — |
| Wound Threshold | End + 6 | Damage accumulates; at threshold → wound, counter resets |
| Max Wounds | floor(End/2) + 1 | At max: incapacitated |
| Damage | Net hits + STR + weapon mod − armour DR | Crit (net ≥ 3): weapon mod doubled |
| Stamina | End + 1, min 2 | Modified by armour. History STRUCK (PP-611). |
| Composure | Cha + 6 | Social health |
| Concentration | Foc + Rec | Social stamina |
| Appraise Pool | Att + Rec | PP-614 canonical. Not doubled — quick perceptive check. |
| Appraise Ob | floor(opponent Cha / 2) + 1 | Universal Ob formula. PP-614. |
| Thread Pool | (Spi×2) + Hist + TPS, min 5 | TPS = TS ÷ 10. |
| Contact Rounds | Focus score | 1–7 |
| Cover | Cog + best concealment History | Exposure thresholds |

**Simulation calibration:** 5D pool at Ob 1 succeeds ~92%. At Ob 2: ~70%. At Ob 3: ~45%. At Ob 4: ~25%. 10D at Ob 3: ~73%.

**Cover calibration (SIM-DEBT-FW-06):** Cover 3 = detected in 3 scenes. Cover 9 = full season. Cover 12+ = near-immune.

## 4.6 Disposition (PP-632 — corrected from prior versions)

**Range: −4 to floor(Bonds/2)+1.** Maximum +4 at Bonds 6–7.

**Ob calculation: max(1, base Ob − Disposition).** One rule, no lookup table.

**Decay threshold: above +2** (was above +3). Decays −1/season.

**Disposition ceiling = floor(Bonds/2)+1.** Same formula as max Knot count. Bonds governs relational depth in both directions simultaneously.

**Starting values:** Derived from faction alignment and lifepath (±0.5 increments, floor). Same faction +1, Allied 0, Neutral 0/−1, Rival −1/−2, Hostile −2/−3.

**Simulation calibration (SIM-DEBT-FW-03):** Neutral→Bonded = 6–8 actions across 3–4 seasons. Sincerity Gate adds ~37% failure on instrumental Connect.

## 4.7 Initiative (Universal — Versus Roll)

| Context | Pool |
|---|---|
| Personal Combat | Combat Pool vs Combat Pool |
| Social Contest | Contest Pool vs Contest Pool (unless institutional format predetermines) |
| Mass Combat | Command vs Command |

Higher net = initiative holder = declares last (information advantage). Tie: random. Transfers to exchange winner. Draws: holder retains.

## 4.8 Personal Tracks

Coherence (10→0, practitioners), Thread Sensitivity (0–100), Certainty (0–5), Momentum (0–4, resets per session), Disposition (per NPC, PP-632), Exposure (per territory per season, 0–10+).

---

# COMPLETE RENAME TABLE

| Old | New | Reason |
|---|---|---|
| Mending Stability | **Metaphysical Stability** | What it measures |
| Theocracy Counter | **Church Influence** | What it measures. Goes to 100. |
| Peninsular Strain | **Political Stability** | What it measures |
| Territory Consolidation Value | **Territory Value** | Simpler. Range 1–5. |
| Resonant Style | **Pressure Point** | Immediately communicable |
| Genre "Memory" | **Precedent** | Avoids collision with Recall |
| Genre "Projection" | **Prospect** | Pairs with Precedent |
| Belief Scar | **Conviction Wound** | Consistent terminology |
| Leadership Deviation Ob | **Authority Challenge Ob** | Clearer |

---

# BATTLE CONSEQUENCES

| Trigger | Metaphysical Stability | Invasion Pressure | Political Stability |
|---|---|---|---|
| Standard Battle | −1 | +2 (once/season) | +1 (per season with battle) |
| Campaign/War scale | −2 | +2 | +1 |
| Popular Uprising | −1 | 0 | +1 |
| Altonian Vanguard | −1 | 0 | 0 |
| Covert action | 0 | 0 | 0 |
| Church Seizure (ungarrisoned) | 0 | 0 | 0 |

Conquest → Accord 1. Defender territory → Accord −1.

---

# STABILITY TRIGGERS (faction_layer_v30)

PP-403 REPEALED. Only canonical triggers:

| Trigger | Δ |
|---|---|
| Own territory occupied | −1 (one-time); −1 each Accounting |
| Capital lost | −2 |
| Capital transferred | −3 |
| Minor cession treaty | −1 |
| Major cession treaty | −2 |
| Capitulation treaty | −3 |
| Officer eliminated | −1 |
| Mandate reaches 0 | −2 |
| Suppress Failure | −1 (named exception) |
| Accounting Check (≥2 attribute losses) | Stability pool vs Ob = loss magnitude |
| Consolidation (clean season) | +1 |

---

# CROSS-SYSTEM PARALLELS

| Concept | Personal Combat | Mass Combat | Social Contest | Thread |
|---|---|---|---|---|
| **Pool** | (Agi×2)+H+3 | min(S,Cmd)+Cmd | (Attr×2)+H+3 | (Spi×2)+H+TPS |
| **Health** | Wound Threshold (End+6) | Type Health × Size | Composure (Cha+6) | Coherence (10→0) |
| **Endurance** | Stamina (End+1) | Discipline (1–7) | Concentration (Foc+Rec) | Contact Rounds (Focus) |
| **Degradation** | −1D/Wound | Size loss, Discipline break | +1 Ob/Rattled | −1 Coherence/op |
| **Collapse** | Incapacitation | Rout | Spent (−2D, resets) | Rendering Crisis |
| **Initiative** | Pool vs Pool | Cmd vs Cmd | Pool vs Pool / institutional | — |

---

# SIMULATION CALIBRATION DATA

| System | Finding | Source |
|---|---|---|
| Campaign outcomes | Church 53%, Crown Treaty 14%, Timeout 32% | valoria_sim v4 |
| Game length | 13.3 years (avg) | valoria_sim v4 |
| Hafenmark collapse | 27.8% | valoria_sim v4 |
| Social contest ±1 Cha | 25–30% Grand Contest win rate | SIM-STRESS-06 |
| Social contest ±4 Cha | Total Victory in 2 exchanges | SIM-STRESS-06 |
| Fieldwork Ob | 5D→D1, 9D→D1-2, 13D→D1-3, 17D→D1-4, 24D→D5 | SIM-DEBT-FW-01 |
| Evidence pacing | 5-threshold: 3-5 scenes (high pool), 4-6 (low pool) | SIM-DEBT-FW-02 |
| Cover | 3=3 scenes, 9=full season, 12+=near-immune | SIM-DEBT-FW-06 |
| Mass combat splitting | Dominates concentration +9% to +45% | PP-508 sim |
| War-scale Coherence | 7-turn battle: 10→3 (Dissonant). 9+ turns: Severance. | SIM-DEBT-06 |

---

# UNVALIDATED (flagged for next simulation)

| Item | Priority |
|---|---|
| Accord + Political Stability + battle consequences compound | P1 (ED-538) |
| TC reform + TCV revaluation + Seizure Accord compound on Church | P1 (ED-539) |
| NPC AI with Accord-aware governance (Hafenmark collapse rate) | P1 |
| Dynastic Proclamation and Cultural Reformation | P1 |
| Unit health = Type Health × Size | P1 |

---

# GODOT IMPLEMENTATION STATUS

**Phases 1–12 fully implemented** (as of April 15 "echoes" session). BoardContainer with territory map. BattleContainer with general Command. check_victory for ALL canonical victory conditions. Nested zoom (Phase 10.1). Season loop runnable end-to-end.

**Stale:** check_victory uses pre-peninsular_strain victory conditions. Universal Peninsular Sovereignty condition, Accord checks, and Political Stability threshold not yet in Godot code.

---

# OPEN DECISIONS

| ID | Question |
|---|---|
| J-1 | Mass combat pool: (min(Size,Command) × 2) + History + 3, or retain current? |
| J-3 | Restoration Movement rethink timing |
| J-4 | Write stance triangles for Lenneth, Elske, Haelgrund |
| J-5 | Accord × Exposure interaction |
| J-6 | Church Seizure Ob on 0–4 Piety: 6 − Piety? |
| J-7 | Confirm 0–4 uniform territory scale |
| J-8 | Confirm Church Influence milestones |
| J-9 | Confirm Spiritual Weight values |
