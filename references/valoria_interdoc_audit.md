# VALORIA — Inter-Document Audit
## Every design doc cross-referenced against every other
## Date: 2026-04-14
## Supplements: valoria_comprehensive_audit.md (design docs vs Godot code vs Jordan's directives)

This document covers what the previous audit missed: design docs audited against EACH OTHER. Organized by conflict type.

---

# 1. FORMULA CONFLICTS BETWEEN DOCUMENTS

## 1.1 Thread Pool — Three conflicting formulas in active documents

| Document | Thread Operation Pool Formula |
|---|---|
| params_threadwork.md (canonical header) | (Spirit × 2) + History + TPS |
| params_threadwork.md (Leap section, pre-PP-619) | Spirit + Attunement + History + TPS |
| params_threadwork.md (Lock/Dissolution section) | Spirit + History (no TPS) |
| params_threadwork.md (Mending section) | Attunement + Focus + TPS |
| params_threadwork.md (Community Weaving, PP-250, pre-PP-616) | Attunement + History + TPS |
| threadwork_v30.md §2.3 (Leap) | (Spirit × 2) + History + TPS (PP-619) |
| threadwork_v30.md §2.4 (Weaving/Pulling) | (Spirit × 2) + History + TPS (PP-616, PP-625) |
| threadwork_v30.md §2.4 (Lock/Dissolution) | (Spirit × 2) + History + TPS (PP-618, PP-625) |
| threadwork_v30.md §2.4 (Mending) | (Spirit × 2) + History + TPS (PP-616, PP-625) |
| combat_v30.md §10 | References "threadwork_redesign_v25.md" for Thread ops — stale cross-ref |

**The canonical formula (PP-616/618/619/625) is (Spirit × 2) + History + TPS for ALL operations.** But params_threadwork.md still contains the pre-PP-619 formulas in its individual operation sections (Leap, Lock, Dissolution, Mending). These struck formulas coexist with the canonical header, creating a document where a reader encounters conflicting formulas depending on which section they read.

**Action:** params_threadwork.md individual operation sections must be updated to show the canonical formula. The pre-PP-619 formulas should be removed or moved to a "patch history" appendix.

## 1.2 Combat Pool — params_core vs params_combat vs combat_v30

| Document | Combat Pool Formula |
|---|---|
| params_core.md | (Agility × 2) + weapon History (points + 3), min 5 |
| params_combat.md | (Agility × 2) + Relevant History + 3 (minimum 5) |
| combat_v30.md §1 | (Agility × 2) + Relevant History + 3 (minimum 5) |

**These agree on the arithmetic but disagree on the semantic structure.** params_core.md says "weapon History (points + 3)" — implying the +3 is inside the History term. params_combat.md and combat_v30.md say "Relevant History + 3" — implying the +3 is a separate constant added alongside History.

For a character with NO relevant History, params_core implies pool = (Agi × 2) + (0 + 3) = (Agi × 2) + 3. params_combat implies the same: (Agi × 2) + 0 + 3 = (Agi × 2) + 3. **Same result.** But the phrasing creates potential confusion about whether History 0 contributes +3D or +0D.

**Resolution:** All documents should use the same phrasing: "(Primary Attribute × 2) + History bonus (0–3D) + 3." The +3 is always present. History adds 0, 1, 2, or 3 on top of it.

## 1.3 Stamina — Three documents, two formulas

| Document | Stamina Formula |
|---|---|
| params_core.md | Endurance + 1, min 2 |
| params_combat.md | Endurance + 1 (modified by armour), min 2. "History component struck." |
| combat_v30.md §7 | Endurance + Relevant History + 1 − armour modifier, min 2 |

**combat_v30 skeleton still includes "Relevant History" in the Stamina formula.** Both params files explicitly say History is struck. The skeleton is stale on this point.

**Action:** Remove "Relevant History" from combat_v30 §7 Stamina formula. Should read: "Stamina = Endurance + 1 − armour modifier. Minimum 2."

Additionally, params_combat.md has a note: "PP-275 — Stamina maximum: Stamina capped at base value (End + H + 1 − armour mod)." This references "H" (History) in the cap formula even though History was struck from the base formula. The cap should reference "End + 1 − armour mod."

## 1.4 Health/Wounds — Excess damage: carried over or lost?

| Document | Excess Damage Rule |
|---|---|
| params_combat.md (ED-200 section) | "Damage does not carry over when a wound threshold is crossed. When Health reaches 0, a wound is taken and Health resets to (Endurance + 6). Any excess damage beyond the 0-threshold is lost." |
| params_combat.md (main section) | "Health = (Endurance + 6) × (wound count + 1) — wound threshold every (Endurance + 6) points. Allows critical hits to deal multiple wounds simultaneously." |
| combat_v30.md §7 | "Health = Endurance + 6. Damage accumulates each round against Health. At 0 Health: take one Wound, Health resets to full." |

**Contradiction within params_combat.md itself.** The ED-200 section says "excess damage is lost" and "wounds are discrete thresholds." The main section says "allows critical hits to deal multiple wounds simultaneously." If excess damage is lost, how can one blow cause multiple wounds?

**The resolution is in the formula:** Health = (End+6) × (Wounds+1). For a character with Endurance 4 and 0 wounds: Health = 10. A blow dealing 20 damage reaches 0 (10 damage), takes wound 1, Health resets to 10 (new total = 20), remaining 10 damage brings Health to 0 again, takes wound 2. **Excess damage IS carried over through the formula** — the "lost" language in ED-200 refers to damage beyond the final wound threshold that doesn't complete another wound cycle.

**But Jordan says "Health is non-replenishing inside scenes."** This changes the model: total HP is a single pool (End+6 per wound level at start of scene), damage accumulates without resetting. A blow of 20 against a 10-HP character inflicts 2 wounds. Simpler, same lethality, no reset confusion.

**Action:** This needs Jordan's final ruling (per previous audit Finding CK-5). The two models produce similar outcomes but different internal logic. The "non-replenishing" model is cleaner for videogame implementation.

## 1.5 Appraise Pool — params_contest vs social_contest_v30

| Document | Appraise Pool |
|---|---|
| params_contest.md (PP-614) | Attunement + Recall, TN 7 |
| social_contest_v30.md §4 Step 1 (PP-278) | Attunement alone (no History), TN 7, Ob 1 |

**These are different.** params_contest gives a pool of (Attunement + Recall). social_contest_v30 gives a pool of Attunement only (single attribute, no History). The PP-614 note in params_contest says "consolidates Read/Judge/Appraise into single canonical entry" — implying it supersedes the design doc.

**But neither follows the universal pool formula** (Attribute × 2) + History + 3. Appraise is a special case — it's a perceptive check, not a full contested action. If it should follow the universal formula, it would be (Attunement × 2) + History + 3.

**Action:** Decide whether Appraise follows the universal pool formula or remains a special-case single-attribute roll. Then reconcile params_contest.md and social_contest_v30.md to use the same formula.

## 1.6 Appraise Ob — ceiling vs floor+1

| Document | Appraise Ob |
|---|---|
| params_contest.md | opponent Charisma ÷ 2 (round up), min 1 |
| social_contest_v30.md §4 | Attunement alone, TN 7, Ob 1 (fixed) |

**params_contest says Ob scales with opponent Charisma. social_contest_v30 says Ob is always 1.** These cannot both be correct.

**PP-614 (in params_contest) is the later patch** and should be canonical. But the design doc skeleton hasn't been updated. 

**Action:** Update social_contest_v30 §4 Step 1 to use the PP-614 formula: Pool = Attunement + Recall, Ob = floor(opponent Charisma / 2) + 1 (using floor+1 per Jordan's universal Ob directive, not ceiling).

## 1.7 Contest initiative — params_contest vs social_contest_v30

| Document | Exchange 1 Initiative |
|---|---|
| params_contest.md | "Higher Attunement acts last (information advantage). [ED-138: deterministic vs rolled?]" |
| social_contest_v30.md §5 | Same: "higher Attunement acts last. [ED-138]" |

Both documents flag ED-138 as unresolved. Jordan has now resolved it: versus roll (Contest Pool vs Contest Pool) for first exchange, then held by winner. Both documents need updating.

## 1.8 Combat initiative — params_combat vs combat_v30

| Document | Exchange 1 Initiative |
|---|---|
| params_combat.md | "Exchange 1 initiative: higher Attunement acts last." |
| combat_v30.md §3 | Doesn't specify Exchange 1 method clearly. References "Speed + Instinct" (struck). |

**params_combat says Attunement (deterministic). Jordan says versus roll (Combat Pool vs Combat Pool).** Both need updating.

---

# 2. TERMINOLOGY DRIFT BETWEEN DOCUMENTS

## 2.1 Unit stat names

| Document | Unit health stat | Unit fighting stat | Unit organization stat | Unit rout stat |
|---|---|---|---|---|
| mass_battle_v30.md | Size | Power | Discipline | Morale |
| combat_v30.md §9 | Strength | Combat Power (CP) | Cohesion | Morale |
| combat_v30.md §11 (faction rosters) | — | Martial, Cohesion | — | — |
| params_board_game.md (BG unit table) | Health | Martial | Discipline | (not listed) |

**Four different naming conventions for the same concepts across three documents and four tables.** mass_battle_v30 performed a rename (PP-232: Strength→Size, CP→Power, Cohesion→Discipline, CR→Command) but this rename didn't propagate everywhere.

**combat_v30 §9 still uses the pre-rename terms** (Strength, Combat Power, Cohesion). combat_v30 §11 uses "Martial" and "Cohesion" (a third variant). params_board_game uses "Health" and "Martial" (a fourth variant).

**Action:** Propagate the PP-232 rename (Size, Power, Discipline, Morale, Command) to all documents. Specifically: combat_v30 §9, combat_v30 §11, and the BG unit table in params_board_game.md.

## 2.2 "Resonant Style" vs nothing else

**npc_behavior_v30.md** uses "Resonant Style" throughout (Evidence, Consequence, Authority, Solidarity). **No other design doc references this term.** social_contest_v30 uses "Genre" and "Orientation" for argument structure. The NPC document maps Resonant Styles to Contest interaction types in §1.3, but the Contest document doesn't reference Resonant Styles at all.

**This is a one-way dependency.** The NPC system knows about the Contest system but the Contest system doesn't know about the NPC system. When the player uses a Contest against an NPC, they need to know which argument Style (Citation, Suppression, Vision, Insinuation) maps to the NPC's Pressure Point — but that mapping is only in npc_behavior_v30.

**Action:** Add a cross-reference in social_contest_v30 §9 (TTRPG Rules) or a new section noting that NPCs have Pressure Points (renamed from Resonant Styles per Jordan) and how those map to Contest Styles.

## 2.3 "Mending Stability" vs "Thread Tension"

**All active design docs use "Mending Stability" (MS).** The old term "Thread Tension" appears in:
- threadwork_v30 §8.1: "Thread Tension (Thread Tension, 0→100) | Replaced By: Mending Stability (MS, 100→0)" — correctly documenting the rename.
- mass_battle_v30 §A.14: "must be converted to Mending Stability with inversion (Thread Tension +N → Mending Stability −N)" — stale reference noting conversion needed.
- params_threadwork.md: Multiple references to "Thread Tension" in pre-PP-600 sections that are marked as superseded.

**No active conflicts** — the rename is documented. But the stale references in mass_battle_v30 and params_threadwork should be cleaned up.

## 2.4 Zone terminology in combat

**combat_v30 §5:** "Close zone renamed Melee range; Far zone renamed Ranged distance (PP-268)." 

**But ED-129 is still open:** "Ranged weapon TN integration into Short/Long matrix pending." The zone terminology rename happened but the ranged weapon system still uses the old LP/HP/Sling classification (pre-matrix). These ranged weapons need integration into the Reach × Weight × Type matrix to resolve ED-129.

## 2.5 "Debate" vs "Contest" system name

**social_contest_v30.md:** Opens with "[EDITORIAL: ED-136 — System name: 'Contest' proposed.]" The document title says "Social Contest System v2." params_contest.md is named params_contest.md.

**But:** The Godot code has `DebateContainer.gd`, `DebateContainer.tscn`, `scenes/containers/debate/`, and `scenes/ui/debate_ui/`. All code files use "Debate" not "Contest."

**No document uses "Debate" as the canonical name anymore.** But the code does. ED-136 is unresolved — the rename to "Contest" is proposed but not confirmed.

**Action:** Resolve ED-136. If "Contest" is canonical, the Godot code directory/class names should be queued for rename.

---

# 3. MECHANIC OVERLAPS AND REDUNDANCIES

## 3.1 Domain Echo — defined in three documents

| Document | Domain Echo Definition |
|---|---|
| scale_transitions_v30 §5 | Full definition: trigger (Sufficient Scope), amount table (Overwhelming ±2, Success ±1, Partial narrative only, Failure −1), timing by mode, cap (one Echo/scene/faction). |
| board_game_v30 §5 | Same definition, embedded in the BG rules. |
| fieldwork_v30 §2.5 | Investigation-specific Domain Echo rules: "Finding has faction-level scope when..." with additional criteria. |

**The definitions are consistent** but scattered. A developer implementing Domain Echoes must consult three documents. The fieldwork version adds criteria (Structural investigation, Complex investigation about a named faction's institutional acts, Documentary/Verified evidence) that don't appear in the other two.

**No contradiction found** — but a single canonical Domain Echo reference section (in scale_transitions_v30 or a dedicated section) would reduce cross-document hunting.

## 3.2 Exposure — defined in two documents

| Document | Exposure System |
|---|---|
| fieldwork_v30 §6 | Full Exposure system: Cover (derived), thresholds (Noticed/Watched/Compromised), sources (+1/+2 per action type), reduction methods, Church Attention Pool interaction. |
| scale_transitions_v30 §3.9 | References Exposure: "Combat Exposure codified: quiet +1, conspicuous +2, public +3." |

**fieldwork_v30 is canonical** for Exposure. scale_transitions_v30 adds combat-specific Exposure values. Consistent, no conflict.

## 3.3 Piety Track — owned by two documents

| Document | Piety Track Definition |
|---|---|
| victory_v30 §2 | Full PT definition: range 0–5, action cap (±1 per faction per territory per season), Calamity Drift (MS-linked erosion), T15 hard-fixed at 0. |
| peninsular_strain_v1 §2.2 | Starting PT values per territory. |

**These are complementary, not overlapping.** victory_v30 defines mechanics, peninsular_strain defines starting values. No conflict.

## 3.4 Church Seizure — defined in three documents

| Document | Church Seizure Rules |
|---|---|
| victory_v30 §3.2 | Full Graduated Seizure mechanics. Pool = Influence + floor(TC/15). Ob = 7 − PT. Church Mandate ≥ 4. Prominence required. |
| peninsular_strain_v1 §5.2 | Same mechanics + Accord formula for Seizure outcomes. |
| params_board_game.md | Pool and Ob repeated. TC 60 seizure threshold (different from victory_v30's graduated model). |

**Conflict:** params_board_game.md has `TC_CHURCH_SEIZURE_THRESHOLD: int = 60` — implying seizure only available at TC ≥ 60. victory_v30 and peninsular_strain say Graduated Seizure is available at ANY TC value (PP-494) — the pool just grows with TC. The TC 60 threshold in params_board_game is stale (pre-PP-494).

**Action:** Update params_board_game.md to remove the TC 60 seizure threshold. Church Seizure is available whenever Church Mandate ≥ 4 and Prominence exists, per PP-494.

## 3.5 Treaty mechanics — defined in two documents

| Document | Crown Treaty |
|---|---|
| victory_v30 §3.1 | Full Treaty mechanics: Ob, consent, degree effects, treaty period, break conditions, lapse timing. |
| peninsular_strain_v1 §5.1 | Cross-references victory_v30 §3.1, adds Accord on diplomatic transfer = 2. |

**Consistent.** No overlap or conflict.

## 3.6 Fieldwork → Contest transition — defined in two documents

| Document | Fieldwork to Contest Handoff |
|---|---|
| fieldwork_v30 §2.3 | "Current Disposition maps to Piety Track offset (±1 per 2 Disposition, cap ±2). Evidence from fieldwork may be cited in the Contest for +2D Recall bonus." |
| social_contest_v30 §9.1 | "Pre-contest Preparation: +1D on Exchange 1." Evidence Track Findings: "+1D per Finding cited, max +2D." |

**Slight conflict:** fieldwork_v30 says Evidence gives "+2D Recall bonus." social_contest_v30 says "+1D per Finding, max +2D." These produce the same ceiling (+2D) but different framing (flat +2D for any evidence vs. +1D per Finding). The per-Finding model from social_contest_v30 is more granular and should be canonical.

**Action:** Update fieldwork_v30 §2.3 to reference the per-Finding model from social_contest_v30 §9.1: "+1D per Finding cited in Contest opening, maximum +2D."

---

# 4. MISSING CROSS-REFERENCES

## 4.1 combat_v30 → threadwork_v30

**combat_v30 §10:** "See designs/ttrpg/threadwork_redesign_v25.md for full Thread operation rules." This is a stale filename — the file was renamed to threadwork_v30.md.

**Action:** Update cross-reference to threadwork_v30.md.

## 4.2 mass_battle_v30 → threadwork_v30

**mass_battle_v30 §A.10:** References "threadwork_redesign_v25.md §2.3" and "§5.2.2" and "§5.2.3." These section numbers may have shifted during the v25→v30 rename and content restructuring.

**Action:** Verify all section number references in mass_battle_v30 against threadwork_v30 and update.

## 4.3 npc_behavior_v30 → social_contest_v30

**npc_behavior_v30 §1.3:** Maps Resonant Styles to Contest interaction types (Evidence → Memory + Revealing, Consequence → Projection + Revealing, Authority → Memory + Obscuring, Solidarity → Any + Revealing). But social_contest_v30 uses "Precedent" and "Projection" (or "Memory" and "Projection" — see genre name issue below). The mapping uses "Memory" which may be the pre-rename genre name.

**If the Contest genre "Memory" has been renamed** (per the attribute rename where Memory → Recall), then the NPC behavior mapping uses a stale genre name. Check whether the Contest genre was also renamed.

**Finding:** social_contest_v30 §2 Step 2 still uses "Memory" and "Projection" as genre names. The attribute was renamed (Memory → Recall) but the genre was NOT renamed. So "Memory" as a genre name is current. However, this creates confusion: the attribute is "Recall" but the genre is "Memory" — two different things with the same root concept in different parts of the system.

**Action:** Either rename the genre "Memory" to something distinct (e.g., "Precedent" — which is already the argument style name for Memory + Revealing) or note the potential confusion explicitly in both documents.

## 4.4 fieldwork_v30 → npc_behavior_v30

**fieldwork_v30 §5 (Socializing):** Defines Disposition (−3 to +5), social actions (Read, Converse, Connect, Impress, Negotiate, Rumour), and the Sincerity Gate. **Does not reference NPC Conviction, Pressure Point, or AI behavior.**

**npc_behavior_v30 §4 (Decision Procedure):** Defines how NPCs make decisions based on Conviction. References Contest system for social contests. **Does not reference the fieldwork Disposition system.**

**These two systems operate in parallel without acknowledging each other.** A player socializing with an NPC uses the fieldwork Disposition system. That same NPC's behavior is governed by the npc_behavior Conviction system. The two tracks (Disposition and Conviction) are independent — Disposition measures the NPC's warmth toward the PC; Conviction measures the NPC's core values. Both are active simultaneously but neither document references the other.

**Action:** Add a cross-reference in fieldwork_v30 §5 noting that NPC responses to social actions are filtered through their Conviction and Ethical Framework (see npc_behavior_v30). Add a cross-reference in npc_behavior_v30 noting that NPC Disposition toward the PC (see fieldwork_v30 §5.1) modifies their willingness to engage in Conviction-adjacent conversations.

## 4.5 peninsular_strain_v1 → fieldwork_v30

**peninsular_strain_v1** defines Accord (0–3 per territory) and its effects on governance. **fieldwork_v30** defines Exposure and its effects on detection/response by the controlling faction. These interact: low Accord territories (Resistant/Revolt) should affect fieldwork Exposure differently from high Accord territories, but neither document acknowledges the other.

**Expected interaction:** In an Accord 1 (Resistant) territory, the population is hostile to the governor — a character investigating the governor should have LOWER Exposure (the population shelters investigators against the government). In an Accord 3 (Aligned) territory, the population supports the governor — investigators face HIGHER Exposure. But fieldwork_v30's Exposure system doesn't reference Accord at all.

**Action:** Consider adding an Accord modifier to Exposure thresholds in fieldwork_v30 §6. Low Accord = more permissive environment for anti-government fieldwork. High Accord = more permissive for pro-government fieldwork.

---

# 5. STALE SECTIONS STILL IN ACTIVE SKELETONS

| Document | Stale Content | Issue |
|---|---|---|
| threadwork_v30 §2.4 | Pre-PP-622 single-axis Ob tables with "(struck)" annotations | Clutter; three-axis system in params_threadwork is canonical |
| threadwork_v30 §2.4 | Pre-PP-619 pool formulas in individual operation subsections | Superseded by canonical header formula |
| combat_v30 §7 | "Stamina = Endurance + Relevant History + 1" | History struck per PP-611 |
| combat_v30 §9 | Pre-PP-232 unit stat names (Strength, Combat Power, Cohesion) | Renamed to Size, Power, Discipline |
| combat_v30 §10 | Cross-ref to "threadwork_redesign_v25.md" | Renamed to threadwork_v30.md |
| mass_battle_v30 §A.14 | "Thread Tension" references | Should be "Mending Stability" |
| params_board_game.md | TC_CHURCH_SEIZURE_THRESHOLD = 60 | Graduated Seizure has no TC threshold (PP-494) |
| params_combat.md PP-275 | "Stamina capped at base value (End + H + 1 − armour mod)" | "H" (History) struck from Stamina formula |
| social_contest_v30 §4 Step 1 | "Attunement alone (no History), TN 7, Ob 1" | Superseded by PP-614: Pool = Attunement + Recall, Ob = Cha÷2 |

---

# 6. SPECIFIC MECHANIC CROSS-CHECKS

## 6.1 Feint: combat_v30 vs params_combat

| Aspect | combat_v30 §4 | params_combat.md |
|---|---|---|
| Commit | "allocate N dice (minimum 3) to Offence" | "commits full Combat Pool to Offence; Defence = 0" |
| Roll | "versus roll: N dice vs opponent's Defence pool" | "Roll: N dice TN 7 vs opponent's Defence pool TN 7 (sequential per initiative)" |
| Effect | "opponent loses [margin] dice from total pool next round" | Same |

**Contradiction on commit.** combat_v30 says commit N dice (minimum 3), leaving the rest for Defence. params_combat says commit FULL pool, Defence = 0. PP-294 (cited in combat_v30) defines the versus roll but doesn't resolve whether partial or full commitment is canonical.

**This matters significantly for gameplay.** Full-pool Feint is extremely risky (0 Defence = free hits from opponent). Partial Feint (commit N, keep rest for Defence) is a calculated risk. PP-294 says "allocate N dice (minimum 3) to Offence for the feint; remaining dice available for Defence this round" — this matches combat_v30 (partial commitment is canonical).

**Action:** Update params_combat.md to match combat_v30/PP-294: partial commitment (N dice minimum 3, remainder available for Defence).

## 6.2 Rescue: combat_v30 vs params_combat

Both documents describe Rescue identically (PP-290/292). **No conflict.** The mechanic is consistent: Rescue is an exclusive action, rescuer commits N Offence dice to contest the redirect, requires the rescued actor to be outnumbered, successful intercept grants +2 Momentum.

## 6.3 Treaty: victory_v30 vs peninsular_strain_v1

Both define Crown Treaty. victory_v30 has the full mechanical specification. peninsular_strain_v1 cross-references victory_v30 and adds the Accord on transfer (= 2). **No conflict.**

## 6.4 Church Seized Territory Accord: victory_v30 vs peninsular_strain_v1

| Document | Seizure Accord Formula |
|---|---|
| victory_v30 §3.2 | Not specified — references "PP-494" |
| peninsular_strain_v1 §5.2 | Success: max(floor(PT/2)+1, 2). Overwhelming: floor(PT/2)+2, max 3. Partial: 1. |

**victory_v30 lacks the Accord formula that peninsular_strain provides.** Since peninsular_strain is the newer document and specifically addresses Accord, it's canonical. But victory_v30 should cross-reference it.

**Action:** Add "See peninsular_strain_v1 §5.2 for Seizure Accord" to victory_v30 §3.2.

## 6.5 Hafenmark Dynastic Proclamation: peninsular_strain_v1 vs victory_v30

**peninsular_strain_v1 §5.3** defines Dynastic Proclamation as Hafenmark's non-military acquisition tool. **victory_v30 §3.3** still lists "Parliamentary Sovereignty" as Hafenmark's primary victory condition, with Dynastic Assertion as an alternate.

**peninsular_strain_v1 explicitly says:** "[Parliamentary Sovereignty STRUCK — replaced by Dynastic Assertion as primary per peninsular_strain_v1.md.]" This replacement appears in victory_v30's text but only as an editorial note — the victory condition tables still list both.

**Action:** Remove Parliamentary Sovereignty from victory_v30 §3.3 entirely. Dynastic Assertion is the primary. Dynastic Proclamation (from peninsular_strain) is the acquisition tool.

## 6.6 Invasion Pressure starting value

| Document | IP Start |
|---|---|
| params_factions.md | 20 |
| params_board_game.md | 20 |
| clock_registry_v30.md | 5 |

**clock_registry says IP starts at 5. Both params files say 20.** The params files have more recent patches applied. clock_registry_v30 may be stale on this value.

**Action:** Update clock_registry_v30 to IP start = 20 (matching params_factions and params_board_game).

## 6.7 Parliament Integrity starting value

| Document | PI Start |
|---|---|
| params_board_game.md | 5 (BG), 0 (TTRPG) |
| clock_registry_v30.md | 7 |

**Another starting value conflict.** clock_registry says 7. params_board_game says 5 (BG) or 0 (TTRPG).

**Action:** Reconcile. If PI is retained (pending Jordan's decision), set a single canonical starting value.

## 6.8 Mass combat Command formula

| Document | Command Formula |
|---|---|
| mass_battle_v30 §A.5 | Command = ⌈(Charisma + Cognition) ÷ 2⌉ |
| combat_v30 §9 (interface section) | References "Commander Coordination modifier" without defining it |
| social_contest_v30 | References "Coherence Rating derivation: ⌈(Charisma + Cognition) ÷ 2⌉" in propagation notes |

**social_contest_v30's propagation notes reference "Coherence Rating derivation: ⌈(Charisma + Cognition) ÷ 2⌉."** This is a stale cross-reference — social_contest uses Charisma (renamed from Presence) and Cognition to derive Command Rating (CR → Command per PP-232 rename), but the propagation note still says "Coherence Rating" which is a different concept (the 10→0 personal track). "Coherence Rating" should read "Command Rating" in that propagation note.

**Action:** Fix stale "Coherence Rating" reference in social_contest_v30 propagation notes to "Command Rating" (or just "Command").

---

# 7. CROSS-SYSTEM INTERACTION GAPS

## 7.1 Stealth — not defined anywhere

No design doc defines stealth actions (Sneak, Hide, Lockpick, Pickpocket, Disguise, Sabotage). fieldwork_v30 has the Exposure system (which is the detection/consequence side of stealth) but no stealth ACTIONS that generate or avoid Exposure proactively. Surveil (Cognition, +2 Exposure) is the closest, but it's observation, not infiltration.

**This is a genuine gap.** The fieldwork system has the infrastructure (Exposure tracks, Cover derived value, threshold consequences) but not the player-facing actions.

## 7.2 Accord → Fieldwork interaction undefined

As noted in §4.5 above: Accord (peninsular_strain) affects territory governance, and Exposure (fieldwork) tracks detection risk in territories. These should interact but don't.

## 7.3 NPC Recruitment — defined in npc_behavior but not referenced elsewhere

**npc_behavior_v30 §9.5** defines a full NPC Recruitment procedure (Identify → Approach → Offer → Resolution). This mechanic doesn't appear in any other design doc. fieldwork_v30 doesn't reference it. social_contest_v30 doesn't reference it. params_board_game doesn't reference it (though it defines Officer templates).

**Recruitment is a complex social mechanic** (pool = (Charisma × 2) + History, Ob from NPC Disposition, incentive modifiers, Hook system) that sits between fieldwork socializing and Domain Actions. It's fully designed but orphaned from the other systems.

**Action:** Cross-reference in fieldwork_v30 §5 (Socializing) that NPCs at specific Disposition levels become recruitment candidates, and reference npc_behavior_v30 §9.5 for the full procedure.

## 7.4 Knot mechanics — defined in params_threadwork but referenced from many

**params_threadwork.md (PP-632):** Full Knot mechanics (pool, tiers, formation, effects, breaking). **fieldwork_v30 §5.6:** Knot integration with socializing. **social_contest_v30 §4 Step 6:** Shared Composure buffer via Knots. **threadwork_v30 §2.5:** Conflicting Beliefs through Knots. **npc_behavior_v30:** Knot strain for threadcut beings.

**All references are consistent.** Knot mechanics are well-integrated across documents. No conflicts found.

## 7.5 Warden Cooperation / Warden Recognition — defined in victory_v30, referenced in multiple

**victory_v30 §6:** WC (0–3) and WR (0–4) tracks. **params_board_game:** WR advancement rules. **fieldwork_v30 §8.1:** Survey action Anomaly result mentions WC.

**Slight confusion:** WC (Warden Cooperation) is a shared track. WR (Warden Recognition) is Varfell-specific. Both affect Thread operations and MS. They're distinct tracks with distinct functions but similar names. In a videogame UI, these need clear visual differentiation.

---

# 8. SUMMARY: INTER-DOCUMENT CONFLICTS REQUIRING ACTION

## Formula Conflicts (fix before any extraction)

| ID | Conflict | Documents | Resolution |
|---|---|---|---|
| F-1 | Thread pool — 3+ formulas in params_threadwork | params_threadwork individual sections vs canonical header | Propagate canonical formula to all sections |
| F-2 | Stamina — History still in combat_v30 | combat_v30 vs params_combat vs params_core | Remove History from combat_v30 §7 |
| F-3 | Appraise pool — Att+Rec vs Att alone | params_contest vs social_contest_v30 | Adopt PP-614 (Att+Rec) in social_contest_v30 |
| F-4 | Appraise Ob — scaled vs fixed | params_contest vs social_contest_v30 | Adopt PP-614 Ob in social_contest_v30 |
| F-5 | Feint commit — partial vs full | combat_v30 vs params_combat | params_combat stale; combat_v30/PP-294 canonical (partial) |
| F-6 | Health excess damage — carried vs lost | Two sections of params_combat contradict each other | Needs Jordan ruling (reset per wound vs single pool) |

## Terminology Drift (fix during propagation)

| ID | Drift | Documents | Resolution |
|---|---|---|---|
| D-1 | Unit stats: Size/Power/Discipline vs Strength/CP/Cohesion vs Martial/Health | mass_battle_v30 vs combat_v30 vs params_board_game | Propagate PP-232 rename everywhere |
| D-2 | "Resonant Style" → "Pressure Point" | npc_behavior_v30 | Rename pending Jordan confirmation |
| D-3 | "Debate" vs "Contest" system name | social_contest_v30 vs Godot code | Resolve ED-136 |
| D-4 | Genre "Memory" vs Attribute "Recall" confusion | social_contest_v30 | Consider renaming genre |
| D-5 | "Coherence Rating" in social_contest propagation note = stale | social_contest_v30 | Should read "Command" |

## Stale Cross-References

| ID | Location | Stale Reference | Correct Reference |
|---|---|---|---|
| X-1 | combat_v30 §10 | threadwork_redesign_v25.md | threadwork_v30.md |
| X-2 | mass_battle_v30 §A.14 | "Thread Tension" | "Mending Stability" |
| X-3 | params_board_game | TC_CHURCH_SEIZURE_THRESHOLD = 60 | Graduated Seizure, no threshold (PP-494) |
| X-4 | params_combat PP-275 | "End + H + 1 − armour mod" | "End + 1 − armour mod" (H struck) |
| X-5 | clock_registry_v30 | IP start = 5 | IP start = 20 |
| X-6 | clock_registry_v30 | PI start = 7 | PI start = 5 (or struck entirely) |
| X-7 | victory_v30 §3.3 | Parliamentary Sovereignty still listed | Struck; Dynastic Assertion is primary |

## Missing Cross-References

| ID | Gap | Action |
|---|---|---|
| M-1 | npc_behavior → social_contest (one-way dependency) | Add Pressure Point mapping in social_contest |
| M-2 | fieldwork socializing → npc_behavior Convictions | Cross-reference both directions |
| M-3 | peninsular_strain Accord → fieldwork Exposure | Consider Accord modifier on Exposure thresholds |
| M-4 | npc_behavior Recruitment → fieldwork socializing | Cross-reference in fieldwork §5 |
| M-5 | victory_v30 Seizure → peninsular_strain Accord formula | Add cross-reference in victory_v30 §3.2 |

## System Gaps

| ID | Gap | Scope |
|---|---|---|
| G-1 | No stealth actions defined in any design doc | New fieldwork sub-system needed |
| G-2 | Accord × Exposure interaction undefined | Design decision needed |
| G-3 | Three missing NPC stance triangles (Lenneth, Elske, Haelgrund) | Design work needed |
