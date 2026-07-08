<!-- SKELETON — mechanical spec only — atomized 2026-04-13 -->
<!-- Infill: scale_transitions_v30_infill.md -->

<!-- v30 baseline — renamed from designs/hybrid/scale_transitions_design_v1.md on 2026-04-13 -->
# Scale Transitions and Mode Bridge Design
## Status: CANONICAL
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

> **Delivery model.** The handoffs below are the *named, curated* cross-scale procedures. Beneath them the universal Key substrate (key_substrate §4.1/§4.2) delivers in **all directions** — top-down, bottom-up, vertical, diagonal, lateral, horizontal — by observer resolution; see §12. A handoff is authored sugar over the substrate, not the only path between scales.


### §3.1 Personal → Thread
Leap triggers. Contact duration starts on the round Leap succeeds. Thread pool and operations become available. Return to Personal scale on Contact end or voluntary withdrawal.

### §3.2 Personal → Faction
GM recognises faction scope. Personal Ob resolves first, then Domain Action Ob. Same roll — the personal action produces the faction consequence through Domain Echo (§5).

### §3.3 Personal → Scene (Contest)

### §3.4 Scene → Faction (Domain Echo)

Scene events meeting Sufficient Scope (§7) produce Domain Echo per §5. Multi-condition scenes (multiple Sufficient Scope conditions met simultaneously) follow §3.2 Multi-condition tie-break: highest-priority condition wins. Priority order: Thread operation → Combat victory → Settlement governance → Disposition reach → Investigation completion → Faction-leader-direct → Other. Cap: 1 Domain Echo per faction per scene (PP-329). See §5.5 (Accord Domain Echo) and §5.6 (Thread Domain Echo) for the full Echo specifications.

[EDITORIAL: ED-748 — §3.4 stub filled with forward-reference. Source: 2026-04-24 audit §3.12.]

### §3.5 Thread → Faction
Thread operation targeting faction-level configuration resolves as Domain Action. Thread pool used, appropriate Ob applied. No extra roll — the Thread operation IS the faction action.

### §3.6 Thread → Mass (Mass Battle Integration)

Thread operations during mass battle resolve per mass_battle §A.10. Substrate cost differential by scale: Skirmish/Company (TS ≥ 30, Coherence cost 0/op), Battle/Campaign (TS ≥ 50, Coherence cost −1/op), War (TS ≥ 70, Coherence cost −2/op). Practitioner positioning per mass_battle §A.7 PP-101: rear/Reserve practitioner = safe Phase 4 Leap; front-line practitioner = conditional Phase 5 Leap. Thread operations are recorded in Phase 4 (offensive) or Phase 6 step 4-5 (support — Weaving, Mending, Rally) and applied at Phase 6 Step 1 (simultaneous with Volley + Engagement damage).

[EDITORIAL: ED-748 — §3.6 stub filled with forward-reference. Source: 2026-04-24 audit §3.12.]

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

### §4.3 Zoom In Triggers (PP-556, extended)

#### §4.3.1 Arc-Specific Triggers (existing)
Certain arcs define mandatory or optional Zoom In triggers at specific thresholds:
- Haelgrund Defection: Church Stability ≤ 2 + AP ≥ 6 in Haelgrund's territory
- Consecration Crisis: Church Stability-dependent (§ED-407 resolution)
- Per-arc triggers documented in arc source files with Zoom In entry conditions

#### §4.3.2 Mandatory Zoom In Triggers (NEW — cannot be declined)

The following events generate Priority 0 Scene Slate entries per player_agency_v30 §4.2 Step 1. The player experiences these events as personal scenes regardless of their current activity. Mandatory scenes consume 1 scene action each.

| Trigger | Condition | Scene Content |
|---------|-----------|---------------|
| Settlement Revolt | Player is in a province containing a settlement at Order 0. **Deduplication (ED-750):** Settlement-events (settlement_layer §4.3) at same settlement same season collapse into this single Mandatory entry, not two. | The revolt unfolds at the specific settlement. The player is present at or travels to the settlement in revolt. They choose: support the garrison (combat), negotiate with the populace (social contest), investigate the cause (fieldwork), or flee (movement). |
| Heresy Investigation Target | Player is the target of an active Heresy Investigation | The Inquisitor arrives. Interrogation scene (asymmetric social contest per social_contest §7). The player may resist, comply, or attempt to redirect. |
| Faction Leader Removal | Player's faction leader is assassinated, overthrown, or incapacitated | The player witnesses or learns of the event directly. Succession mechanics fire (player_agency §5.2). If Standing ≥ 5: leadership offer. If Standing < 5: the player is present for the transition and may intervene. |
| Mass Battle at Settlement | A mass battle targets a settlement in the player's current province | The player is caught in the battle. They must participate (command or personal combat) or attempt to escape (Endurance check Ob 2; failure = caught in crossfire, take 1 wound). |
| Companion Arc Trigger | A companion's arc branch trigger fires (npc_behavior §5.2) | The companion's transformation scene plays out with the player present. The player witnesses and may influence the companion's arc resolution. |
| Knot Partner in Crisis | An NPC Knotted to the player reaches Conviction crisis (Scar count ≥ 3) | The Knot transmits the crisis. The player perceives the NPC's distress through the relational thread (per P-12). Scene: the player may seek out the NPC or experience the crisis at distance through Thread perception. |
| Stability Crisis | Player's faction Stability drops to ≤ 2 at Accounting OR drops by ≥ 2 in a single Accounting (ED-587). **Hysteresis (ED-749):** Trigger fires once per Stab ≤ 2 entry. Re-arms only after Stab ≥ 3 maintained for 2 consecutive Accountings. | Emergency faction council: social contest or fieldwork scene revealing the source of the crisis. Player may intervene (Govern action Ob 2 → +1 Stability queued to next Accounting, per Domain Echo §5) or assess (Fieldwork Evidence +2 on "faction stability sources" investigation). Cannot be declined — faction is in crisis. |
| Rank Advancement Recognition Event | Player's Standing crosses a rank threshold (per faction_politics_expanded_v1.md §1, Std 3 and above) AND Formal Recognition Event conditions are met | The recognition ceremony unfolds as a formal faction scene. The player receives the rank, insignia, and attendant obligations. Recognition can be withheld in-scene if inner-circle Disposition or rival-candidate conditions fire — creating a debt scene per §1. |

If mandatory scenes exceed the scene action budget, the player chooses which to attend personally. Remaining mandatory scenes resolve through NPC AI with reduced player influence: the player is present but overwhelmed, able to observe but not direct.

#### §4.3.3 World-State Zoom In Triggers (NEW — Scene Slate Priority 1)

These events generate Priority 1 Scene Slate entries. They are presented but optional — the player may choose not to attend.

| Trigger | Condition | Scene Content |
|---------|-----------|---------------|
| Clock Band Transition | Any global clock (MS, CI, IP) crosses a band threshold | Environmental scene: the world visibly changes. At MS band transition: Thread phenomena manifest. At CI milestone: Church institutional action visible. At IP threshold: border activity intensifies. |
| NPC Conviction Crisis | Any NPC with Disposition ≥ +1 has Scar count ≥ 2 | The NPC is visibly struggling. Social scene: the player may engage, support, challenge, or observe. |
| Treaty Proposed or Broken | Any faction proposes, ratifies, or breaks a treaty involving the player's faction | Political scene: the player learns the terms and may advocate for their faction's position (social contest or fieldwork investigation of the treaty's implications). |
| Territory Control Change | Any territory adjacent to the player changes controller | The consequences are visible: new banners, displaced populations, altered trade routes. The player may investigate, assist displaced people, or exploit the transition. |
| Warden Emergency | RS ≤ 40 and the player has WR ≥ 1 or has met Edeyja | Thread crisis scene: the Wardens need help. The player may contribute Thread operations, investigate the cause, or support logistics. |

### §4.4 "Where Were You?" — Retrospective Scene Generation (NEW)

When a major world event occurs that the player was not present for, the game generates a retrospective Scene Slate entry the following season. This entry does not cost a scene action — it is a free narrative moment.

**Qualifying events:** Faction leader removal (if player was not present), territory conquest (if player was not in either territory), mass battle resolution (if player was not present), Church Graduated Seizure, Löwenritter Coup, Altonian Invasion launch.

**Scene content:** The player learns about the event through their social environment. The scene is not about the event — it is about the player's relationship to the event.

| Player Context | Scene Shape |
|---------------|------------|
| Player has a companion | Companion delivers the news and states their reaction. The companion's Conviction colors the report. |
| Player has Knot with involved NPC | The Knot transmits emotional resonance. The player perceives the NPC's state at the moment of the event (fear, triumph, despair). |
| Player has Disposition ≥ +2 with involved NPC | A messenger or letter arrives from the NPC. The NPC's account reflects their Conviction and relationship with the player. |
| Player has no connection to involved parties | The player hears about it from ambient sources — tavern conversation, broadsheet, market rumor. The information is Unverified (reliability tag per fieldwork §4.3). |

The retrospective scene does not allow the player to change the event's outcome. It allows them to experience its emotional weight and decide how to respond in the current season. The response may generate a new Conviction ("I will avenge Almud"), a new Scene Slate entry (investigating the aftermath), or a new Duty (faction reassignment in response to the crisis).

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
| Piety Track outcome | Domain Echo |
|--------------------------|-------------|
| Track ≥ 7 (winner's side) | Winner faction: +1 Mandate. Loser faction: −1 Mandate if they held institutional authority. |
| Track 4–6 (compromise) | No Domain Echo. Scene-level consequence only. |
| Track ≤ 3 (loser's side) | Reversed — loser faction receives penalty. |

**Reconciled with social_contest_v30 §6 as COMPOSED (ED-SC-0002, Jordan ruling 2026-07-08).** This
§5.4 band scheme and §6's genre scheme are not rivals: the **band gates MAGNITUDE** (Total → ±2,
Decisive → ±1, Compromise → none — as above) while the **won genre selects the STAT/CHANNEL** (§6:
Memory → Mandate; Projection → the outward-initiative channel). The loser institutional-authority
penalty and "Compromise fires nothing" are retained verbatim. Sim realization: `sim/cross_scale/
parliamentary_bridge.py` (band → `domain_echo` degree; genre → aggregate stat).

### §5.5 Accord Domain Echo (peninsular_strain_v1.md)

Personal scenes in Hybrid mode may produce Accord changes via Domain Echo. Cap: ±1 Accord in one territory per Zoom In.

| Personal Scene Outcome | Accord Domain Echo |
|----------------------|-------------------|

**Settlement targeting (AUD-SET-02):** Accord changes from personal scenes target the settlement where the scene occurred, not the province directly. Province Accord recalculates at Accounting: floor(mean(settlement Order)). Full targeting rules: peninsular_strain_v30 §2.5.
| PC publicly governs/administers a territory (sermon, public address, dispute resolution) — Overwhelming/Success | Accord +1 in that territory (queued to next Accounting) |
| PC action destabilises territory governance (assassination, public betrayal, inciting unrest) — Success | Accord −1 in that territory (queued to next Accounting) |
| PC negotiates territorial transfer between factions (personal diplomacy success) | Transferred territory Accord set to 2 (queued to next Accounting) |
| PC action triggers violence at territorial scale (initiating battle, coup, uprising) | RS −1 immediate. Accord −1 in that territory. |

Accord Domain Echoes fire at Accounting Step 4c alongside other Accord checks. They do not stack with faction-level Govern actions in the same territory the same season — whichever produces the higher Accord applies.

---

### §5.6 Thread Domain Echo (ED-673)

Thread events produce Domain Echo to faction stats when they meet Thread Significance — distinct from Sufficient Scope (§7).

**Fires when:** (a) Thread operation produces RS change ≥ 1, OR (b) Thread operation witnessed by NPC whose Conviction Scar fires (conviction_track_v1.md §3, formerly npc_behavior_v30 §3.4), OR (c) Thread operation creates/destroys Gap, Lock, or Knot at Territorial+ scale.

| Thread Event | Affected Stat | Direction |
|---|---|---|
| Dissolution Success | Controlling faction Stability | −1 |
| Mending Success (Territorial+) | Controlling faction Mandate | +1 |
| Gap creation | Controlling faction Stability | −1 |
| Lock creation (unauthorized) | Controlling faction Mandate | −1 |
| Public Thread op, Church territory | Church Mandate | −1 |
| Public Thread op, Varfell territory (VTM ≥ 3) | Varfell Mandate | +1 |

**Timing:** Queued to Accounting. **Cap:** 1 Thread Domain Echo per scene per faction (PP-329). **Model:** Extends Epistemic CI Trigger (PP-182) to all factions. CI trigger fires independently. Thread Domain Echo and Accord Domain Echo (§5.5) may both fire from same scene on different stats.

**Known gap (ED-IN-0025, 2026-07-07, C-VERIFY-12):** §5 caps each Domain Echo channel *per-scene-per-faction* (PP-329) but sets **no season-level aggregate ceiling** — a faction generating many qualifying scenes in one season (e.g. Debate-spam) can stack Echoes without limit. Whether a season cap is warranted is not adjudicated here; flagged for Stratum B/E balance review.

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

A personal scene qualifies for Domain Echo when it involves any of the following:

1. A named faction leader or their designated representative
2. A direct challenge to a faction's institutional authority (not personal reputation)
3. A completed Complex or Structural investigation (Evidence Track threshold 5+ reached per fieldwork §4.1) whose subject concerns a faction's institutional acts — the evidence IS the scope
4. A Thread operation targeting a faction-level configuration (Relational+ scale)
5. Combat victory against a named NPC who holds faction office (officer, cardinal, commander, agent) — violence against an institutional representative IS an institutional event
6. Reaching Disposition +4 (Devoted) or +5 (Bonded) with any named NPC who holds faction office — the relationship itself is strategically significant
7. Settlement governance action that changes Order by ±1 or more — the governor's institutional authority produced a measurable political outcome

**Companion modifier:** If the player has a companion present (per companion_specification_v30), add +1 to the player's net successes for Sufficient Scope evaluation. The companion makes personal actions more politically visible.


---

## §8 Scope Shift Rules


---

## §9 PC Faction Embedding (ED-075)

PCs grant +1D to their faction's Domain Action in the territory they are physically present in, once per season. This is the mechanical expression of PC presence in the BG layer — being somewhere matters.

---

## §10 Thread Timing in Hybrid (PP-125, PP-260)

Hybrid Strategic Phase temporal auto-effects from Thread operations:
| Thread Operation | CI Effect |
|-----------------|-----------|
| Dissolution | CI +1 |
| Past-Oriented Pulling (POP) | CI −1 |
| Lock / Weave / Mend | None |

Paradox window = 1 season on POP. Full TTRPG RS values propagate directly to BG RS track. BG Co-Movement ceiling applies only to BG-initiated Thread abstraction (not TTRPG scene Thread ops). (ED-034 resolved)

---

## §11 Contested Figure System (ED-167, ED-168)


- CF wound during personal combat → +1 Ob to commander's BG tactic rolls for remainder of current battle

---

## §12 All-Directions Key Delivery (J-1, ED-1038)

[EDITORIAL: ED-1038 — §12 authored: all-directions Key-delivery rule + authoring discipline + A6 exemption. Jordan ruling J-1, 2026-06-19 ("top down key delivery but ensure it can go all directions"). Source: key_substrate §1/§4.1/§4.2/§2.2. Adds no mechanism; records the rule, the sub-scale-targeting discipline, and the assessor carve-out.]

**Ruling (Jordan, 2026-06-19, J-1):** top-down Key delivery is canonical — and the delivery model must operate in **all directions**. This section records that ruling. It adds no new mechanism: the substrate already delivers in every direction (§12.1). What was missing was the rule, the discipline of populating sub-scale targets (§12.3), and the assessor exemption (§12.2).

### §12.1 The all-directions guarantee
Key delivery is direction-neutral. The single update rule (key_substrate §4.1) resolves an observer set (key_substrate §4.2 `compute_observers`) from three independent sources — `source_actor`, every `targets[].actor_id`, and, for public Keys, `actors_in_scale(scale_signature)` — then **applies** `key.stat_deltas` to each observer (§4.1 step 4, `observer.apply_state_changes`). `actors_in_scale` returns every actor whose state intersects the named scales, with no preferred topology. Direction is therefore an *emergent property* of a Key's `targets[]`, `scale_signature`, and `visibility` — not a separate channel per direction. One substrate carries all six canonical directions:

| Direction | How the substrate carries it | Status |
|---|---|---|
| bottom-up | scene/personal Key meeting Sufficient Scope (§7) -> faction via Domain Echo (§5) | covered (§3, §5, §7) |
| lateral / horizontal | same-scale observers via shared `scale_signature` and scene presence | covered |
| vertical (up) | the eight handoffs (§3.1-§3.8) | covered |
| diagonal | `causes[]`-chained cross-scale consequence (e.g. Thread Echo §5.6) | covered |
| top-down | strategic / environmental Key naming sub-scale `actor_id`(s) in `targets[]` and including the sub-scale in `scale_signature` -> personal / settlement observers | mechanism present; requires §12.3 |
| down-diagonal | as top-down, across a system-family boundary | mechanism present; requires §12.3 |

### §12.2 No private channel; the substrate is the only delivery path (A6 exemption)
Per key_substrate §1, no system maintains a private event channel; every system emits and consumes Keys. Engine-mediated Key delivery is therefore the **sole** canonical cross-scale delivery channel, in every direction, and is exempt from the assessor "no top-down channel" finding (A6 / J-1): that finding identified a missing *rule and populated targets*, never a missing mechanism. A bespoke top-down delivery channel is **not** to be authored — it would duplicate the substrate and violate §1. The fix is discipline (§12.3), not apparatus.

### §12.3 Authoring discipline — populate sub-scale targets
When a strategic-scale or environmental Key carries a consequence that reaches a sub-scale actor, the emitter **must**:
1. add each affected sub-scale actor to `targets[]` with the correct `role` (§2.2: `subject` = acted-upon directly; `object` = territorial / institutional; `witness` / `bystander` = present);
2. include the sub-scale in `scale_signature`, so `actors_in_scale` resolves those observers for public Keys; and
3. set `stat_deltas` and `impact_vector` for each such target.

This extends the §2.2 `causes[]` authoring guideline to targets: a strategic Key with sparse sub-scale `targets[]` delivers blind — the consequence is intended (the consumers are registry-canonical) but unreached. Sparse down-targeting is the §12 defect, exactly as sparse `causes[]` is the diagonal-chain defect.

### §12.4 Known down-seams (Lane-B implementation targets)
The J-1 analysis enumerates eight cross-band down-seams / fifteen type-edges whose *consume intent is already registry-canonical* (the consumers are listed in key_type_registry) but whose strategic emitters do not yet populate sub-scale targets: `domain_actions -> {npc_behavior, piety_track, settlement_economy}`, `faction_politics -> npc_behavior`, `peninsular_strain -> {npc_behavior, settlement_economy, settlement_layer}`, `scenario_authoring -> settlement_layer`. Closing them is emitter-side `targets[]` population per §12.3, plus the assessor carve-out and tests (Lane B) — not a mechanism change. Reference: `designs/audit/2026-06-11-orchestration/valoria_authoritative_graph_v1.md` §2 (top-down / diagonal); key_type_registry consumer schemas.

### §12.5 NERS note
**N** — closes the Robust-direction gap (delivery complete in all six directions) without adding apparatus; the guarantee is a recognition of existing §4.1/§4.2 behaviour. **R** — the eight handoffs plus the substrate guarantee leave no unreachable direction. **S** — identical observer-resolution methodology across every direction; no per-direction special case. **E** — one rule: direction is a property of the Key, not a catalogue of channels.
