<!-- SKELETON — mechanical spec only — atomized 2026-04-13 -->
<!-- Infill: scale_transitions_v30_infill.md -->

<!-- v30 baseline — renamed from designs/hybrid/scale_transitions_design_v1.md on 2026-04-13 -->
# Scale Transitions and Mode Bridge Design
## Version: v1.0 | Date: 2026-04-13
## Status: DESIGN — canonical for scale transitions and mode bridging
## Sources: params_scale_transitions.md, PP-089/090, PP-103, PP-107–112, PP-232, PP-261, PP-340–343
## Supersedes: compilation/v0.14/stage11_scale_transitions_deprecated.md

---

## §1 Three-Mode Architecture


| Mode | Resolution | Time scale | Character presence |
|------|-----------|------------|-------------------|
| TTRPG | Scene-by-scene, player narration, GM adjudication | Rounds/scenes/sessions | Full character sheet, personal actions |
| Hybrid | BG strategic layer + TTRPG personal scenes via Zoom In/Out | Seasons (BG) + scenes (TTRPG within) | Faction mat + character sheet when zoomed |
| BG | Turn-based, faction-level Domain Actions, seasonal Accounting | Seasons/arcs | Faction mat only; characters abstracted |


---

## §2 Scale Table

Operations span five scales. Scale determines base difficulty and Thread requirements.

| Scale | Scope | Base Ob | Min Thread Sensitivity (TS) | Coherence auto-cost | Examples |
|-------|-------|---------|----------------------------|--------------------|---------| 
| Object | One item, one wound | 1 | 30+ | 0 | Healing a wound, reading a letter's Thread signature |
| Personal | One person | 2 | 30+ | 0 | Changing someone's emotional state via Thread, diagnosing TS |
| Relational | Small group, social agreement | 3 | 50+ | −1 | Knot-sharing between 3 people, community ritual |
| Territorial | A duchy, a district | 4 | 50+ | −1 | Mending a territory's RS damage, territorial Weaving |
| Structural | A kingdom, an institution | 5+ | 70+ | −2 | Institutional-level Thread configuration change |

---

## §3 Eight Handoff Rules


### §3.1 Personal → Thread
Leap triggers. Contact duration starts on the round Leap succeeds. Thread pool and operations become available. Return to Personal scale on Contact end or voluntary withdrawal.

### §3.2 Personal → Faction
GM recognises faction scope. Personal Ob resolves first, then Domain Action Ob. Same roll — the personal action produces the faction consequence through Domain Echo (§5).

### §3.3 Personal → Scene (Contest)

### §3.4 Scene → Faction (Domain Echo)

### §3.5 Thread → Faction
Thread operation targeting faction-level configuration resolves as Domain Action. Thread pool used, appropriate Ob applied. No extra roll — the Thread operation IS the faction action.

### §3.6 Thread → Mass (Mass Battle Integration)

### §3.7 Mass → Personal (General Duel)
Personal Action available at Phase 5 (Priority 8). Limit: 1 exchange per battle turn. General's Command Rating suspended while in personal combat (PP-232). Maximum 5 exchanges before forced disengage or incapacitation. One mass combat turn = one personal combat exchange. (PP-111)

### §3.8 Scene → Mass
Social/investigation win modifiers apply to the next mass battle turn only:
- Social win: +1D to relevant unit Command
- Investigation win: +1D to first Volley
- Combat win: one free Reform action
Modifier to most relevant unit; 1 turn duration. (PP-261, ED-151)

---


### §3.9 Fieldwork ↔ All Systems

| Direction | Trigger | Procedure |
|-----------|---------|-----------|
| Fieldwork → Combat | Exposure threshold reached; ambush triggered | Exposure converts to ambusher Initiative advantage. Active investigation ends; fieldwork scene Ob results carry forward as Combat pre-conditions. (F-TRANS-01) |
| Fieldwork → Contest | Negotiation exceeds §5.7 boundary; investigation find used as Appeal | Evidence from Evidence Track cited in Contest opening move: +1D per Finding, max +2D additional pool. Evidence not consumed by citation. (F-TRANS-10, F-TRANS-11) |
| Fieldwork → Thread | Thread-Read declared during investigation scene | Thread-Read is a perceptive Leap (§4.5, fieldwork_investigation.md). Normal Leap procedure applies. Co-movement fires. Thread operation Ob adds to fieldwork scene time cost (+1 time unit per Thread op in scene). (F-TRANS-07) |
| Fieldwork → Mass Battle | Mass battle declared while fieldwork active | Mass battle suspends fieldwork. Evidence Track state freezes. Exposure does not accumulate during battle. Post-battle: resume as 1 new fieldwork scene (≠ continuation of suspended scene). Battle ≠ fieldwork time. (F-TRANS-06, F-TRANS-12) |
| Combat → Fieldwork | Post-combat investigation of battle site | Counts as 1 fieldwork scene. Combat Exposure codified: quiet engagement +1, conspicuous +2, public +3. Applies before the investigation scene opens. (F-TRANS-09, F-TRANS-12) |
| Contest → Fieldwork | Appraise action in Contest; Contest resolved | Appraise success in Contest: +1 Evidence Track progress (Testimonial tag). Post-Contest Disposition shift: winner +1, loser −1 (with adjudicator present). (F-TRANS-10, F-TRANS-05) |
| BG Survey → TTRPG Discovery | Hybrid mode, Survey degree sets Fieldwork Offset | BG degree: Failure −1 Ob, Partial +0, Success +1 Ob reduction, Overwhelming +2 Ob reduction (cap ±2) on TTRPG personal fieldwork scene. (fieldwork_hybrid.md §9.1) |
| TTRPG Fieldwork → BG Domain Echo | Sufficient Scope (§7) met in fieldwork scene | Follows §3.4 (Scene → Faction) protocol. Investigation Finding that names faction leader = sufficient scope. Disposition shift reaching Bonded with faction-level NPC = sufficient scope. |
| TTRPG Fieldwork → Hybrid Personal Phase | Fieldwork scene during Hybrid play | Fieldwork scenes occur during Personal Phase only. Strategic Phase Survey degree provides Fieldwork Offset. Bonus Personal Phase scene available if Strategic Phase order produces immediate fieldwork opportunity (replaces, does not extend, standard 2–3 Personal Phase scenes). (fieldwork_hybrid.md §9.2) |

## §4 Zoom In / Zoom Out Protocol


### §4.1 Zoom In

**Legal entry points (PP-103):** After Phase 1 (declarations), After Phase 3 (movement), After Phase 6 Step 1 (damage application). Mid-Phase-5 Zoom In defers to after Phase 6 Step 1 (PP-250, ED-158).

**Non-battle Zoom In:** Fires at end of current Domain Action being resolved. No unit conversion required. RS changes apply immediately. Domain Echoes queue to Accounting. (ED-073 resolved)


**Scene Opportunity:** The BG Domain Action degree determines the personal scene difficulty:
- Board FAILURE → scene Ob +1 (harder)
- Board SUCCESS → scene Ob −1 (easier)  
- Board OVERWHELMING → scene Ob −2

### §4.2 Zoom Out
**Definition:** Transition from TTRPG scene back to BG layer.

**State transfer:** Personal scene outcomes translate to BG consequences via Domain Echo (§5). Accord changes from personal scenes queue as Domain Echoes per §5.5 (±1 Accord max per Zoom In). PC incapacitation consequences (Stage 1) apply immediately on Zoom Out (ED-159). Contested Figure wound → +1 Ob to commander's BG tactic rolls for remainder of battle (ED-167).

**Phase 6 continuation:** Steps 2–6 resolve after Zoom Out using the updated state from the personal scene (PP-110). The Zoom In does not pause the BG clock — it inserts a personal scene into the resolution sequence.

### §4.3 Arc-Specific Zoom In Triggers (PP-556)
Certain arcs define mandatory or optional Zoom In triggers at specific thresholds:
- Haelgrund Defection: Church Stability ≤ 2 + AP ≥ 6 in Haelgrund's territory
- Consecration Crisis: Church Stability-dependent (§ED-407 resolution)
- Per-arc triggers documented in arc source files with Zoom In entry conditions

---

## §5 Domain Echo


### §5.1 Trigger
A personal scene qualifies for Domain Echo when it meets Sufficient Scope (§7). One Domain Echo maximum per scene per faction (PP-329).

### §5.2 Amount
| Degree | Effect |
|--------|--------|
| Overwhelming | ±2 to most relevant faction stat |
| Success | ±1 to most relevant faction stat |
| Partial | Narrative only — no faction stat change |
| Failure | −1 to acting faction's own stat |

Cap: ±2 per stat per Echo. (ED-071 resolved by PP-329: one Echo/scene/faction prevents compounding)

### §5.3 Timing by Mode
- **Full TTRPG (Register Shift):** Domain Echo fires immediately at scene end. No extra roll.

This timing difference is intentional (PP-109): Zoom In is a personal intervention in a strategic situation. Faction consequences propagate through seasonal accounting to prevent real-time manipulation of BG stats from personal scenes.

### §5.4 Debate → Domain Echo (PP-108)
| Conviction Track outcome | Domain Echo |
|--------------------------|-------------|
| Track ≥ 7 (winner's side) | Winner faction: +1 Mandate. Loser faction: −1 Mandate if they held institutional authority. |
| Track 4–6 (compromise) | No Domain Echo. Scene-level consequence only. |
| Track ≤ 3 (loser's side) | Reversed — loser faction receives penalty. |

### §5.5 Accord Domain Echo (peninsular_strain_v1.md)

Personal scenes in Hybrid mode may produce Accord changes via Domain Echo. Cap: ±1 Accord in one territory per Zoom In.

| Personal Scene Outcome | Accord Domain Echo |
|----------------------|-------------------|
| PC publicly governs/administers a territory (sermon, public address, dispute resolution) — Overwhelming/Success | Accord +1 in that territory (queued to next Accounting) |
| PC action destabilises territory governance (assassination, public betrayal, inciting unrest) — Success | Accord −1 in that territory (queued to next Accounting) |
| PC negotiates territorial transfer between factions (personal diplomacy success) | Transferred territory Accord set to 2 (queued to next Accounting) |
| PC action triggers violence at territorial scale (initiating battle, coup, uprising) | RS −1 immediate. Accord −1 in that territory. |

Accord Domain Echoes fire at Accounting Step 4c alongside other Accord checks. They do not stack with faction-level Govern actions in the same territory the same season — whichever produces the higher Accord applies.

---

## §6 Mode Transition Procedures

### §6.1 TTRPG → BG (Session Boundary)

### §6.2 BG → Hybrid (Mid-Game Zoom In)
Personal characters enter board state at the BG faction's current position. Character sheet reactivates. Scene resolves under TTRPG rules within the BG strategic context. See §4.

### §6.3 Hybrid → TTRPG (Zoom Out)

### §6.4 Coherence Initialization (PP-200)
First activation of a character in Hybrid mode: Coherence = 10 (full). Subsequent activations: carry forward from last personal scene. No free Coherence reset between Zoom cycles.

### §6.5 Hybrid Coherence Cost (PP-198)
Binary declaration rule: the PC who declares leadership at Phase 1 pays any Coherence costs from Thread operations that affect the BG layer. Co-leadership is not possible — one PC bears the Thread bridge cost.

---

## §7 Sufficient Scope — Register Shift Trigger

1. A named faction leader or their designated representative
2. A direct challenge to a faction's institutional authority (not personal reputation)
4. A Thread operation targeting a faction-level configuration (Relational+ scale)


---

## §8 Scope Shift Rules


---

## §9 PC Faction Embedding (ED-075)

PCs grant +1D to their faction's Domain Action in the territory they are physically present in, once per season. This is the mechanical expression of PC presence in the BG layer — being somewhere matters.

---

## §10 Thread Timing in Hybrid (PP-125, PP-260)

Hybrid Strategic Phase temporal auto-effects from Thread operations:
| Thread Operation | TC Effect |
|-----------------|-----------|
| Dissolution | TC +1 |
| Past-Oriented Pulling (POP) | TC −1 |
| Lock / Weave / Mend | None |

Paradox window = 1 season on POP. Full TTRPG RS values propagate directly to BG RS track. BG Co-Movement ceiling applies only to BG-initiated Thread abstraction (not TTRPG scene Thread ops). (ED-034 resolved)

---

## §11 Contested Figure System (ED-167, ED-168)


- CF wound during personal combat → +1 Ob to commander's BG tactic rolls for remainder of current battle
